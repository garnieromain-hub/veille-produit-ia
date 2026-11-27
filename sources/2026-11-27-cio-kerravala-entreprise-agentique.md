# What CIOs use to build an agentic enterprise (Ce que les DSI utilisent pour construire une entreprise agentique)

**Référence** : Zeus Kerravala (ZK Research), CIO.com, 26 novembre 2026, analyse d'actualité (compte rendu du sommet Bloomberg « Building the Agentic Enterprise », en partenariat avec HPE), https://www.cio.com/article/4253028/what-cios-use-to-build-an-agentic-enterprise.html

**Axe** : Transformation des entreprises (Investissement tech)

## 1. L'idée clé
La plupart des grandes entreprises en sont encore au début de l'IA agentique, et ce qui bloque est le modèle opérationnel plus que la technologie. Les DSI qui avancent partent d'un problème métier et d'un modèle de coût réaliste, choisissent le modèle selon la tâche, font de la gouvernance une plateforme plutôt qu'un comité, et laissent les agents gagner leur autonomie par étapes.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [SAP, entreprise autonome et CAIO](2026-11-23-cio-sap-autonomous-enterprise-caio.md) (budgets par service, modèle par défaut, cycle de vie des agents), la fiche [Orchestration agentique et DSI](2026-11-20-itsocial-orchestration-agentique-dsi.md) (plan de contrôle) et la fiche [Deloitte, responsabilité et coût de l'IA](2026-11-23-itsocial-deloitte-responsabilite-cout-ia.md).
Les recommandations sont largement une redite ; apports :
- **Une mesure de la place réelle des agents** : selon une enquête Bloomberg Intelligence (septembre, 100 grandes entreprises européennes et américaines de plus de 5 000 salariés), les workflows agentiques multi-étapes ne pèsent que 9 % des cas d'usage les plus consommateurs de tokens, contre 34 % pour le code et 24 % pour le support client ; le coût des tokens est le premier frein (20 %).
- **Un test de coût simple** : un agent à 200 000 dollars pour un travail qu'un stagiaire à 50 000 dollars par an pourrait faire doit être remis en cause (Kartik Sakthivel, John Hancock). Plus parlant que les cadres FinOps des fiches précédentes.
- **Une autonomie gagnée par type de décision** : Estée Lauder commence par les décisions déterministes et riches en données (prix, stocks, assortiment) et reste prudent sur la relation client ; l'exemple MAC Cosmetics montre qu'un agent qui recommande un produit en rupture détruit la confiance.
- **Le réseau comme angle mort** : environ 10 % des entreprises auraient modernisé leur réseau pour l'agentique (étude non nommée), argument porté par HPE, partenaire de l'événement.

## 3. Résumé
Au sommet de Bloomberg organisé avec HPE, le constat est que les entreprises sont au début de l'agentique, freinées par leur modèle opérationnel. L'enquête Bloomberg Intelligence le chiffre : 9 % des cas d'usage les plus consommateurs de tokens sont des workflows agentiques, loin derrière le code (34 %) et le support client (24 %) ; les freins sont le coût des tokens (20 %), puis la confidentialité, la conformité, le ROI incertain et l'intégration. L'analyste Niraj Patel cite le routage vers de petits modèles, l'optimisation des prompts, le cache, le fine-tuning et la distillation, sans formule magique. Trois responsables interviennent ensuite. Kartik Sakthivel (John Hancock) rappelle que le DSI reste responsable des actes de l'agent même si un fournisseur gère le modèle, et qu'il faut partir du problème métier (le test du stagiaire). Daniela Dimitrova (Mercedes-Benz North America) décrit un agent qui traite des demandes contractuelles pour un support couvrant plus de 380 concessionnaires, avec un humain dans la boucle, une approche agnostique des modèles (frontière pour le complexe, petit modèle pour un e-mail simple), quatre principes de gouvernance (propriétaire métier nommé, explicabilité, protection des données, tests de sécurité avant et après déploiement), une couche sémantique, une ontologie et un plan de contrôle unifié des agents. Rakesh Srinivasan (Estée Lauder) fait gagner l'autonomie par étapes et reconnaît que la supervision des agents à grande échelle reste immature. James Robertson (HPE) plaide pour moderniser le réseau, faute de quoi on automatise un goulot d'étranglement. L'auteur conclut sur sept recommandations, dont investir autant dans les personnes que dans les plateformes.

## 4. Citations et noms
**Citations** :
- « La gouvernance n'est pas un frein » (« Governance isn't a roadblock »), Daniela Dimitrova, Mercedes-Benz North America
- « La responsabilité repose au bout du compte sur nous » (« accountability ultimately rests with us »), Kartik Sakthivel, John Hancock
- « Les agents doivent gagner la confiance avec le temps » (« the agents have to earn the trust over time »), Rakesh Srinivasan, Estée Lauder

**Noms cités** :
- *Zeus Kerravala* : fondateur et analyste principal de ZK Research, auteur ; conseille aussi des fournisseurs et des investisseurs.
- *Bloomberg Intelligence, Niraj Patel* : enquête de septembre et analyste qui la commente.
- *Kartik Sakthivel* : CIO de John Hancock, responsabilité du DSI et test du stagiaire.
- *Daniela Dimitrova* : CIO de Mercedes-Benz North America, agent contractuel et gouvernance en quatre principes.
- *Rakesh Srinivasan* : CDAIO d'Estée Lauder, autonomie progressive des agents.
- *MAC Cosmetics* : marque d'Estée Lauder, exemple de l'importance des stocks en temps réel.
- *James Robertson* : représentant de HPE, argument sur le réseau.
- *HPE* : partenaire de l'événement.

## 5. Mots-clés
agents IA, autonomie des agents, gouvernance IA, coûts des tokens, routage de modèles, enquête

## Lecture CPO
- **Implications** :
  - Avant de lancer un agent, écrire son modèle de coût et le comparer au coût humain de la tâche : le test du stagiaire est un bon garde-fou de discovery.
  - Planifier l'autonomie des agents par type de décision, des décisions déterministes aux interactions client, avec un propriétaire métier nommé pour chaque agent.
  - La qualité des données temps réel (stocks, prix) conditionne la confiance dans un agent client : c'est un prérequis produit, pas un sujet d'infrastructure.
- **Fiabilité** : analyste qui conseille aussi des fournisseurs, événement coorganisé avec HPE (d'où l'insistance sur le réseau) ; l'enquête Bloomberg Intelligence est sourcée mais petite (100 entreprises), le chiffre de 10 % sur les réseaux n'est pas sourcé.
- **Maturité** : Tendance émergente : l'agentique reste minoritaire dans les usages, mais les pratiques de gouvernance et d'autonomie progressive convergent entre grands groupes.
- **Réutilisation** : présentation client (le chiffre de 9 % et le test du stagiaire) ; post LinkedIn « les agents doivent gagner la confiance » ; table ronde DSI sur la gouvernance comme plateforme.
