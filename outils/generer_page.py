#!/usr/bin/env python3
"""Génère la page web de la veille à partir de liste-articles.md, sources/ et notes/.

Usage : python3 outils/generer_page.py
Sortie : page/veille.html (à publier en artifact, voir CLAUDE.md).
"""
import json
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
LISTE = RACINE / "liste-articles.md"
GABARIT = RACINE / "outils" / "gabarit-page.html"
SORTIE = RACINE / "page" / "veille.html"

LIEN_MD = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")


def cellules(ligne):
    return [c.strip() for c in ligne.strip().strip("|").split(" | ")]


def lien(cellule):
    m = LIEN_MD.search(cellule)
    return (m.group(1), m.group(2)) if m else (cellule, "")


def axes(cellule):
    m = re.match(r"\s*([^(]+?)\s*(?:\(([^)]+)\))?\s*$", cellule)
    if not m:
        return cellule, ""
    return m.group(1).strip(), (m.group(2) or "").strip()


def tableaux(texte):
    """Découpe liste-articles.md en sections ## et renvoie les lignes de tableau de chacune."""
    sections, courante = {}, None
    for ligne in texte.splitlines():
        if ligne.startswith("## "):
            courante = ligne[3:].strip()
            sections[courante] = []
        elif courante and ligne.startswith("| ") and not ligne.startswith("|---"):
            sections[courante].append(ligne)
    # on retire la ligne d'en-tête de chaque tableau
    return {k: v[1:] for k, v in sections.items()}


def sans_titre(md):
    lignes = md.splitlines()
    if lignes and lignes[0].startswith("# "):
        lignes = lignes[1:]
    return "\n".join(lignes).strip()


def main():
    texte = LISTE.read_text(encoding="utf-8")
    m = re.search(r"\*\*Dernière veille\*\*\s*:\s*(\S+)", texte)
    derniere = m.group(1) if m else ""
    secs = tableaux(texte)

    articles = []
    for ligne in secs.get("Articles fichés", []):
        c = cellules(ligne)
        if len(c) < 8:
            continue
        titre, chemin = lien(c[1])
        _, url = lien(c[7])
        principal, secondaire = axes(c[2])
        fichier = RACINE / chemin
        if not fichier.exists():
            print(f"Fiche introuvable, ignorée : {chemin}")
            continue
        articles.append({
            "id": fichier.stem,
            "analyse": c[0],
            "titre": titre,
            "axe": principal,
            "axe2": secondaire,
            "auteur": c[3],
            "publie": c[4],
            "maturite": c[5],
            "motscles": [k.strip() for k in c[6].split(",") if k.strip()],
            "url": url,
            "md": sans_titre(fichier.read_text(encoding="utf-8")),
        })

    complementaires = []
    for ligne in secs.get("Sources complémentaires", []):
        c = cellules(ligne)
        if len(c) < 7:
            continue
        _, url = lien(c[6])
        titre, url_titre = lien(c[1])
        principal, secondaire = axes(c[2])
        complementaires.append({
            "veille": c[0], "titre": titre, "axe": principal, "axe2": secondaire,
            "media": c[3], "publie": c[4], "apport": c[5], "url": url or url_titre,
        })

    notes = []
    for f in sorted((RACINE / "notes").glob("*.md"), reverse=True):
        md = f.read_text(encoding="utf-8")
        premiere = md.splitlines()[0] if md else f.stem
        notes.append({
            "id": "note-" + f.stem,
            "date": f.stem[:10],
            "titre": premiere.lstrip("# ").strip(),
            "md": sans_titre(md),
        })

    donnees = {
        "derniereVeille": derniere,
        "articles": articles,
        "complementaires": complementaires,
        "notes": notes,
    }
    json_txt = json.dumps(donnees, ensure_ascii=False).replace("</", "<\\/")
    page = GABARIT.read_text(encoding="utf-8").replace("/*__DONNEES__*/{}", json_txt)
    SORTIE.parent.mkdir(exist_ok=True)
    SORTIE.write_text(page, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} : {len(articles)} articles, "
          f"{len(complementaires)} sources complémentaires, {len(notes)} notes")


if __name__ == "__main__":
    main()
