# What developers and QA need from each other when AI writes the code

**Référence** : Vittesh Sahni (senior director of AI engineering, Coherent Solutions), CIO.com, 20 novembre 2026, tribune (rubrique Opinion, blog « First Person »), https://www.cio.com/article/4251514/what-developers-and-qa-need-from-each-other-when-ai-writes-the-code.html

**Axe** : IA appliquée au produit (Product management)

## 1. L'idée clé
Quand l'IA écrit le code, le maillon faible n'est pas le test mais le passage de relais entre développement et QA. Il faut le formaliser dans un contrat de livraison, proportionner les preuves au risque et mesurer la confiance obtenue par unité de temps, sinon on paie la vitesse de l'IA en défauts échappés en production.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Thoughtworks Radar vol. 35](2026-11-19-thoughtworks-radar-vol35.md) (le débit de code ne mesure pas la productivité, revenir à DORA), la fiche [Cagan sur le paradoxe de productivité](2026-10-16-svpg-ai-productivity-paradox.md) (plus vite mais pas mieux) et la fiche [Roccaserra sur la qualité interne](2026-11-20-octo-roccaserra-qualite-interne-rythme-livraison.md) (la qualité fait partie du flux).
- **Un contrat de passage de relais co-signé par architecture, développement, QA et produit** : comportement attendu en réussite/échec, composants et services dépendants touchés, travail d'agent inachevé, preuves exigées à chaque étape, qui accepte le risque résiduel. Les fiches précédentes diagnostiquaient le goulot, celle-ci outille la frontière entre deux rôles.
- **Une métrique nouvelle, la confiance par unité de temps** : complétude des preuves divisée par le délai de validation, comptée seulement si la complétude atteint le seuil de la classe de risque. Elle empêche d'afficher une validation plus rapide obtenue en sautant des preuves.
- **Quatre statuts de test** : réussi, échoué, bloqué, vide. Un build vert ne peut plus masquer une preuve absente.
- **Des tests écrits depuis l'exigence, pas depuis le code** : un test dérivé du code généré valide l'erreur par construction (exemple de l'abonnement résilié tout de suite au lieu de la fin de période payée).
- **Sept signaux qualité**, dont le taux de défauts échappés, la reprise du code généré à deux semaines et la complétude des preuves, à lire par paires plutôt qu'en valeur brute.

## 3. Résumé
L'auteur ouvre sur un incident : une petite modification d'un composant partagé passe la revue de code et la QA, tests au vert, mais casse l'étape qui transforme un abonnement payé en accès client ; seule une alerte de production la détecte. Personne n'avait documenté les services dépendants. « Ce ne sont pas les tests qui ont échoué, c'est le passage de relais. » Il explique que l'IA multiplie les petites modifications de code partagé plus vite que les équipes ne documentent leurs dépendances, en citant DORA 2025 (près de 5 000 professionnels) : les équipes qui adoptent l'IA livrent plus, mais la stabilité baisse. Un build vert ne prouve que l'accord du code avec ses propres tests, souvent écrits depuis la même lecture du ticket. Il propose donc de concevoir d'abord le passage de relais (aujourd'hui un simple changement de statut) sous forme de contrat, avec un relecteur IA qui vérifie la conformité au ticket et une QA qui juge séparément si la mise en production est sûre ; la QA renvoie au développement ce qui relève du vrai défaut ou du bruit d'environnement. Il détaille ce dont la QA a besoin : critères d'acceptation binaires, tests issus des exigences, comparaison entre ce que le ticket demandait et ce qui a été touché. Les preuves se proportionnent au risque selon trois facteurs (code neuf ou legacy, part générée par l'IA, liberté laissée aux outils). Il définit la confiance par unité de temps et cite l'enquête Tricentis 2026 (2 501 professionnels IT et QA, commanditée par l'éditeur) : 60 % des organisations déploient du code non testé en production. Il liste sept signaux, avertit d'une courbe en J (DORA) où productivité et stabilité se dégradent d'abord à cause de la « taxe de vérification », et cite McKinsey 2026 : près de trois quarts des entreprises les plus performantes en IA ont refondu leurs processus, contre environ un quart des autres. Conclusion : commencer par un seul flux de livraison, n'accorder plus d'autonomie aux outils que si la confiance par unité de temps progresse, et faire passer la QA du re-test à la conception de la preuve.

## 4. Citations et noms
**Citations** :
- « Ce ne sont pas les tests qui ont échoué. C'est le passage de relais. » (« The tests weren't what failed. The handoff was. »), Vittesh Sahni
- « Un build vert vous dit que le code a passé ses propres tests. » (« A green build tells you the code passed its own tests. »), Vittesh Sahni
- « Les équipes qui ne reconstruisent pas le passage de relais entre développement et QA finissent par payer la vitesse de l'IA en défauts échappés. » (« Teams that do not rebuild the handoff between development and QA end up paying for AI's speed in escaped defects. »), Vittesh Sahni

**Noms cités** :
- *Coherent Solutions* : société de services en ingénierie logicielle, employeur de l'auteur.
- *DORA (Google Cloud)* : étude 2025 (plus de livraisons, moins de stabilité avec l'IA) et recherche sur le ROI du développement assisté par IA (courbe en J).
- *Tricentis* : éditeur de tests, commanditaire de l'enquête Quality Transformation 2026 (60 % déploient du code non testé).
- *McKinsey, State of AI 2026* : les entreprises les plus performantes en IA refondent leurs processus trois fois plus souvent.
- *Confiance par unité de temps* : métrique proposée par l'auteur (complétude des preuves / délai de validation).
- *Taxe de vérification* : coût de relecture du code généré, à l'origine de la courbe en J.

## 5. Mots-clés
vérification, qualité, goulot d'étranglement, mesure de l'impact, agents IA

## Lecture CPO
- **Implications** :
  - Le PM a sa place dans le contrat de passage de relais : critères d'acceptation binaires et décision sur le risque résiduel relèvent du produit.
  - Exiger que les tests soient dérivés des exigences, pas du code généré, et le vérifier en revue.
  - Ajouter à la gouvernance de l'IA de développement la complétude des preuves et le taux de défauts échappés, à côté des métriques DORA, plutôt que le volume de code généré.
  - Anticiper la courbe en J dans les business cases : prévoir une baisse initiale de stabilité.
- **Fiabilité** : directeur IA d'une société de services qui vend ce type d'accompagnement ; chiffres sourcés (DORA, McKinsey) mais l'enquête des 60 % est commanditée par un éditeur de tests (Tricentis) ; la métrique proposée n'est appuyée sur aucun retour d'usage chiffré.
- **Maturité** : Tendance émergente : le goulot de la vérification est largement documenté (DORA, Thoughtworks), la méthode et la métrique proposées sont plus neuves et non éprouvées.
- **Réutilisation** : article OCTO sur la qualité à l'ère du code généré (contrat de passage de relais, quatre statuts de test) ; présentation client DSI sur la mesure ; post LinkedIn (« un build vert ne prouve que l'accord du code avec ses propres tests »).
