# Product Management à l'ère de l'IA : comment rester pertinent quand tout accélère

**Référence** : Thomas Gros, SFEIR Institute, 27 mars 2026,
https://institute.sfeir.com/fr/articles/product-management-ere-ia-exponentielle/

## Idée clé
Les capacités des modèles progressent si vite qu'on ne peut plus supposer la technologie
stable pendant un projet. Selon les mesures METR citées, la complexité des tâches réalisables
a été multipliée par environ 41 en 16 mois, soit de 21 minutes à près de 12 heures de travail
humain. Le PM doit donc changer quatre pratiques : remplacer la roadmap par l'exploration,
prototyper avant d'écrire un PRD, réexaminer le produit à chaque nouveau modèle et choisir
l'implémentation la plus simple.

## Ce qui est nouveau
Peu de choses. L'article est surtout une reprise en français du billet de Cat Wu, Head of
Product de Claude Code chez Anthropic, publié le 19 mars 2026. On y retrouve le test
Excalidraw rejoué à chaque version de Claude, les « side quests », l'exemple de Claude Code
Desktop et les témoignages de PM de Datadog et Decagon. Mieux vaut lire et citer ce billet
directement.

Les apports propres à l'article sont modestes :
- **un tableau de synthèse en quatre oppositions** (roadmap à 6 mois ou sprints
  d'exploration, PRD avant le code ou prototype d'abord, veille passive ou réexamen à chaque
  modèle, architecture complexe ou implémentation simple), facile à reprendre sur une slide ;
- **l'idée que les contournements deviennent de la dette** : un pipeline de 12 étapes conçu
  pour compenser les faiblesses d'un modèle devient un fardeau quand le modèle suivant sait
  traiter le cas directement. C'est l'angle le plus utile ;
- **le passage du déterministe au probabiliste** et la liste des compétences attendues
  (métriques de qualité, AI Act et RGPD, notions de RAG et d'agents). Le sujet est déjà
  largement traité ailleurs.

Les cinq cas d'usage quotidiens (backlog, User Stories, FAQ, analyse de feedback,
préparation des cérémonies) sont des usages courants, sans nouveauté. La fin de l'article
fait la promotion de deux formations de WEnvision, filiale de SFEIR. L'article reste donc en
partie un support commercial.

## Implications pour un CPO ou un PM
- **Planification** : réserver dans le cycle produit une part de temps à l'exploration, sous
  forme de demi-journées d'expérimentation, plutôt que d'engager tout le monde sur 6 mois.
- **Rituel à chaque nouveau modèle** : prévoir un réexamen à chaque release majeure. Il s'agit
  de vérifier ce qui devient possible et quels contournements peuvent disparaître. Ce point
  est facile à mettre en place et souvent oublié.
- **Arbitrage d'architecture** : poser comme critère de revue la question « cette brique
  compense-t-elle une faiblesse du modèle actuel ? ». Si oui, la considérer comme une dette
  à durée de vie limitée.
- **Documentation** : accepter qu'un prototype remplace une partie du PRD au début du cadrage.
- **Compétences** : savoir définir des métriques de qualité pour des sorties probabilistes,
  comme le taux de succès, la latence perçue ou la pertinence.

## Maturité
Tendance émergente. Les pratiques décrites sont documentées chez des éditeurs de modèles et
des scale-ups tech comme Anthropic, Datadog ou Decagon. L'article ne montre pas leur adoption
dans des organisations plus classiques.

## Citation
« Le rôle évolue du "Feature Orchestrator" vers "l'Architecte de l'incertitude". »
(Thomas Gros, SFEIR Institute)

## Réutilisation
- **Post LinkedIn** : l'angle « vos contournements d'aujourd'hui sont la dette de demain »,
  avec le chiffre METR (×41 en 16 mois) comme accroche. Il faut citer Cat Wu comme source
  première.
- **Présentation client** : le tableau des quatre oppositions, pour lancer une discussion
  sur l'adaptation des rituels produit dans une organisation qui intègre l'IA.
- **Table ronde** : une question à poser, « à quelle fréquence réexaminez-vous votre produit
  quand un nouveau modèle sort ? ».
- **Article OCTO** : à utiliser comme source secondaire seulement. Mieux vaut partir du billet
  de Cat Wu et des données METR.

**Tags** : roadmap, prototypage, dette technique IA, rôle du PM, METR
