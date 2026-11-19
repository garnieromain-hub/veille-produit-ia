---
name: veille
description: Lance la veille produit et IA à la demande. Sans argument, veille automatique depuis la dernière veille ; avec un thème (« /veille IA dans la discovery ») ou une période (« /veille 30 jours »), veille ciblée. À utiliser quand Romain tape /veille ou demande de lancer la veille maintenant.
---

# Lancer la veille

0. Lancer `git pull` pour partir de la dernière veille (celle du cloud comprise).
1. Lire la date « Dernière veille » en tête de `liste-articles.md`.
2. Confier la veille à l'agent `veilleur` (outil Agent, `subagent_type: veilleur`),
   avec un brief qui dit :
   - sans argument : « Veille automatique : tous les thèmes, depuis la dernière
     veille du JJ/MM/AAAA jusqu'à aujourd'hui. » ;
   - avec un thème ou une période : le thème ou la période demandés, tels quels.
3. Quand l'agent a fini, vérifier que la note existe dans `notes/`, que les
   nouvelles fiches sont dans `sources/` et que `liste-articles.md` a une
   ligne par nouvelle fiche et une date « Dernière veille » à jour. Corriger
   l'index si une ligne manque.
4. Mettre à jour la page web : `python3 outils/generer_page.py`, puis
   republier `page/veille.html` sur l'URL indiquée dans `CLAUDE.md`
   (section « Page web ») avec l'outil Artifact : `read` sur l'URL, puis
   `publish` avec `url` et `file_path`.
5. Enregistrer dans le dépôt : `git add -A`, commit « Veille du AAAA-MM-JJ »,
   puis `git push`.
6. Rendre à Romain :
   - « En une phrase » de la note ;
   - le lien vers la page web ;
   - les nouveaux articles (titre lié à la fiche, axe, maturité), en liste ;
   - le nombre de sources complémentaires ajoutées ;
   - le chemin de la note ;
   - les sources écartées et ce qui est « À récupérer par Romain ».
