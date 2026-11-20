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
    # chaque ligne devient un dictionnaire indexé par les noms de colonnes de l'en-tête,
    # pour que l'ajout ou le déplacement d'une colonne ne casse rien
    resultat = {}
    for nom, lignes in sections.items():
        if not lignes:
            resultat[nom] = []
            continue
        entete = cellules(lignes[0])
        resultat[nom] = [dict(zip(entete, cellules(l))) for l in lignes[1:]]
    return resultat


def titre_md(md, defaut):
    """Premier titre de niveau 1, où qu'il soit (une note peut commencer par « Fiches créées : N »)."""
    for ligne in md.splitlines():
        if ligne.startswith("# "):
            return ligne[2:].strip()
    return defaut


def sans_titre(md):
    """Retire le premier titre de niveau 1 (affiché à part dans la page)."""
    lignes = md.splitlines()
    for i, ligne in enumerate(lignes):
        if ligne.startswith("# "):
            del lignes[i]
            break
    return "\n".join(lignes).strip()


def main():
    texte = LISTE.read_text(encoding="utf-8")
    m = re.search(r"\*\*Dernière veille\*\*\s*:\s*(\S+)", texte)
    derniere = m.group(1) if m else ""
    secs = tableaux(texte)

    articles = []
    for c in secs.get("Articles fichés", []):
        titre, chemin = lien(c.get("Fiche", ""))
        if not chemin:
            continue
        _, url = lien(c.get("Source", ""))
        principal, secondaire = axes(c.get("Axe", ""))
        fichier = RACINE / chemin
        if not fichier.exists():
            print(f"Fiche introuvable, ignorée : {chemin}")
            continue
        articles.append({
            "id": fichier.stem,
            "analyse": c.get("Analysée le", ""),
            "titre": titre,
            "axe": principal,
            "axe2": secondaire,
            "langue": c.get("Langue", ""),
            "auteur": c.get("Auteur, média", ""),
            "publie": c.get("Publiée le", ""),
            "maturite": c.get("Maturité", ""),
            "motscles": [k.strip() for k in c.get("Mots-clés", "").split(",") if k.strip()],
            "url": url,
            "md": sans_titre(fichier.read_text(encoding="utf-8")),
        })

    complementaires = []
    for c in secs.get("Sources complémentaires", []):
        _, url = lien(c.get("Source", ""))
        titre, url_titre = lien(c.get("Titre", ""))
        principal, secondaire = axes(c.get("Axe", ""))
        complementaires.append({
            "veille": c.get("Veille du", ""), "titre": titre, "axe": principal, "axe2": secondaire,
            "langue": c.get("Langue", ""), "media": c.get("Média", ""), "publie": c.get("Publiée le", ""),
            "apport": c.get("Ce qu'elle apporte", ""), "url": url or url_titre,
        })

    notes = []
    for f in sorted((RACINE / "notes").glob("*.md"), reverse=True):
        md = f.read_text(encoding="utf-8")
        notes.append({
            "id": "note-" + f.stem,
            "date": f.stem[:10],
            "titre": titre_md(md, f.stem),
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

    # Version autonome pour GitHub Pages : document HTML complet
    # (l'artifact claude.ai ajoute lui-même doctype, charset et viewport).
    site = SORTIE.parent / "site"
    site.mkdir(exist_ok=True)
    (site / "index.html").write_text(
        '<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="robots" content="noindex">\n'
        "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
        "body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
        "</head>\n<body>\n" + page + "\n</body>\n</html>\n",
        encoding="utf-8",
    )
    (site / ".nojekyll").write_text("", encoding="utf-8")

    print(f"{SORTIE.relative_to(RACINE)} et page/site/index.html : {len(articles)} articles, "
          f"{len(complementaires)} sources complémentaires, {len(notes)} notes")


if __name__ == "__main__":
    main()
