# Veille produit et IA de Romain

Veille sur le product management, l'IA, la transformation des entreprises à
l'ère de l'IA, la gestion de portefeuille numérique et l'investissement tech.
Public visé : CPO, PM, PO, et les directions (DSI, CDO, comex) qu'ils conseillent.
Je tutoie Claude, Claude me tutoie. Tout le contenu est en français
(les sources peuvent être en anglais).

## Périmètre de la veille
La veille couvre cinq axes. Chaque article retenu est rattaché à un axe
principal (et au plus un axe secondaire). Un article hors de ces axes n'est
pas retenu, sauf s'il éclaire directement l'un d'eux.

1. **Product management** : rôle et compétences des PM, PO et CPO, discovery,
   design, organisation et topologie des équipes produit, modèle produit,
   leadership produit, marché de l'emploi produit.
2. **IA appliquée au produit** : usages de l'IA par les équipes produit
   (prototypage, recherche, evals, agents), conception de produits IA,
   outils et annonces des éditeurs quand ils changent les pratiques.
3. **Transformation des entreprises à l'ère de l'IA** : modèle opérationnel,
   organisation, compétences et emploi, conduite du changement, retours
   d'expérience de grands groupes, gouvernance et mesure de l'impact.
4. **Gestion de portefeuille numérique** : pilotage et arbitrage d'un
   portefeuille de produits et d'initiatives, passage du projet au produit,
   financement par produit ou par flux de valeur, lean portfolio management,
   rationalisation du parc applicatif, mesure de la valeur.
5. **Investissement tech** : deux volets.
   - Budgets IT des entreprises : arbitrages, ROI et business cases de la tech
     et de l'IA, évolution des dépenses, FinOps.
   - Capital-risque : levées et valorisations marquantes, thèses des fonds
     sur l'IA et le logiciel, ce qu'elles disent des produits de demain.

Une bonne veille couvre plusieurs axes, sans quota fixe : on suit l'actualité,
mais un axe absent plusieurs semaines de suite mérite une recherche ciblée.

## Organisation
- `sources-de-reference.md` : mes sources favorites (sites, newsletters, auteurs).
- `liste-articles.md` : index de toutes les fiches (une ligne par article,
  avec son axe), plus les sources complémentaires repérées sans fiche.
  Tenu à jour à chaque fiche créée.
- Page web de la veille : générée depuis `liste-articles.md`, `sources/` et
  `notes/` par `outils/generer_page.py`, publiée sur GitHub Pages (voir « Page web »).
- `sources/` : une fiche par source analysée, nommée `AAAA-MM-JJ-slug.md`.
- `notes/` : notes de veille compilées, nommées `AAAA-MM-JJ-theme.md`.

## Veille
- Toute demande de veille (un thème, une période, la veille hebdo) est confiée
  à l'agent `veilleur`, pas faite en direct dans la conversation.
- Veille automatique quotidienne : une routine cloud la lance du lundi au
  vendredi à 7h (heure de Paris l'hiver, 8h l'été), même Mac éteint, et pousse
  les résultats sur GitHub (`garnieromain-hub/veille-produit-ia`, branche `main`).
  Le lundi couvre le week-end. Le volume quotidien et la répartition des
  langues sont fixés dans `.claude/agents/veilleur.md`, section « Veille
  quotidienne » : c'est là qu'on les change.
- Organisation de la veille quotidienne : l'agent `veilleur` sélectionne les
  articles, quatre agents `ficheur` rédigent les fiches en parallèle, puis le
  `veilleur` écrit une note courte du jour.
- La page web se met à jour toute seule à chaque push (voir « Page web ») :
  aucun ordinateur n'est nécessaire.
- `/veille` la lance à la demande depuis n'importe quel poste où le dépôt est cloné.

## Synthèse d'un article à la demande
Quand je demande une synthèse, une fiche ou « ce qu'il faut retenir » d'un
article (lien ou document), sans autre précision :
1. Appliquer le skill `fiche-source` (grille en cinq parties).
2. Ajouter la ligne dans `liste-articles.md`.
3. Commit « Fiche : <titre court> » et push directement sur `main`, sans me
   demander confirmation et sans ouvrir de pull request : la page publique se
   met à jour toute seule.
4. Me répondre avec l'idée clé, ce qui est nouveau et le lien vers la page.
Si la source est déjà fichée (même lien), ne rien créer et me renvoyer la fiche
existante.

## Dépôt GitHub
- Avant de travailler sur le Mac : `git pull`, pour récupérer la dernière veille.
- Après toute modification (veille, fiche, note, liste) : commit puis `git push`,
  pour que la routine cloud parte de la dernière version.
- `page/` n'est pas versionné : la page se régénère avec `outils/generer_page.py`.

## Page web
- URL : https://garnieromain-hub.github.io/veille-produit-ia/ (publique,
  non indexée par les moteurs de recherche). Le dépôt est public lui aussi.
- Publication automatique : à chaque push sur `main`, le workflow
  `.github/workflows/page.yml` lance `outils/generer_page.py` et publie
  `page/site/index.html` sur GitHub Pages. Il n'y a rien à faire à la main.
- Pour voir la page en local : `python3 outils/generer_page.py`, puis ouvrir
  `page/site/index.html`.
- Ne pas modifier les fichiers de `page/` à la main : changer `outils/gabarit-page.html`.
- L'ancienne page claude.ai (https://claude.ai/artifact/WhGdkNsbncWQyvsUb5Jw6g)
  n'est plus mise à jour.

## Principes
- Une source déjà analysée (même lien) n'est pas refichée : on la réutilise.
- On ne paraphrase pas pour remplir : si une source n'apporte rien de neuf, on le dit.
- Les fiches servent ensuite à mes articles OCTO, posts LinkedIn, tables rondes
  et présentations clients.
