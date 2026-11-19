# AI Evals: A Hands-On Guide for Product Teams

**Référence** : Teresa Torres, Product Talk, 2 septembre 2026, https://www.producttalk.org/ai-evals/

## Idée clé
Les evals (mesures de la qualité des sorties d'un produit IA) sont une habitude de discovery à part entière, au même titre que les entretiens ou les tests d'hypothèses. Chaque habitude répond à une question : les evals répondent à « nos changements ont-ils marché ? ». Définir ce qu'est une « bonne » réponse est un travail de PM, pas d'éditeur d'outils.

## Ce qui est nouveau
Les evals étaient jusqu'ici un sujet d'ingénieurs ML. Torres les rattache explicitement au cadre *Continuous Discovery Habits* et les ajoute à son glossaire des habitudes de discovery. Elle donne une méthode accessible aux PM : analyse d'erreurs sur les traces, puis choix de l'eval la moins chère qui marche (assertion de code < golden dataset < LLM-as-judge < feedback client), baseline, variante, comparaison. Exemples tirés de ses propres produits : sur Interview Coach, 15 questions orientées sur 105 suggérées dans la baseline.

## Implications pour un CPO ou un PM
- Sur un produit IA, la discovery ne s'arrête pas à la mise en production : lire des traces devient une pratique hebdomadaire, comme les entretiens.
- Le PM doit définir les critères de qualité (« correct » dépend du contexte) et ne pas les sous-traiter à un outil.
- Compétence à acquérir : analyse d'erreurs et lecture de taux de réussite plutôt que pass/fail.

## Maturité
Tendance émergente : le sujet est très présent chez les praticiens IA, mais le cadrage « evals = discovery » est récent et porté surtout par Torres.

## Citation
« La justesse dépend du contexte. Ne laissez pas un éditeur définir la justesse de votre produit. » (traduit de l'anglais)

## Réutilisation
- Article OCTO : « La discovery ne s'arrête plus au lancement » sur les produits IA.
- Table ronde : qui définit le « bon » dans un produit IA, le PM, le data scientist ou l'éditeur ?
- Présentation client : grille des quatre types d'evals, du moins cher au plus cher.

**Tags** : evals, discovery continue, produits IA, qualité, Teresa Torres
