# Claude, Copilot and Agentforce are ready. Are your SAP and ServiceNow platforms ready?

**Référence** : Vipin Jain (fondateur et architecte en chef de Transformation Enablers Inc.), CIO.com, 23 novembre 2026, tribune (publiée avec l'IASA Chief Architect Forum), https://www.cio.com/article/4251456/claude-copilot-and-agentforce-are-ready-are-your-sap-and-servicenow-platforms-ready.html

**Axe** : Portefeuille numérique (Investissement tech)

## 1. L'idée clé
Les entreprises financent les agents IA et les plateformes sur lesquelles ils tournent par deux circuits budgétaires séparés : les agents passent vite en budget d'innovation, le travail de plateforme (clean core, intégration, données) doit justifier un retour pluriannuel. Les agents dépendent alors d'un socle jamais financé. Il faut financer chaque agent avec sa dépendance de plateforme, un seul responsable et un seul business case.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [SAP Autonomous Enterprise](2026-11-23-cio-sap-autonomous-enterprise-caio.md) (budgets IA et cycle de vie des agents vus par l'éditeur), la fiche [Thelliez sur le responsable du ROI IA](2026-11-20-jdn-thelliez-responsable-roi-ia.md) (chaque cas d'usage piloté comme une ligne de portefeuille), la fiche [Deloitte via IT Social](2026-11-23-itsocial-deloitte-responsabilite-cout-ia.md) et la [prévision Gartner 2027](2026-11-13-gartner-depenses-it-2027.md), dont l'article reprend les chiffres.
- **Le problème est budgétaire, pas technique** : l'auteur situe l'échec des agents dans la séparation entre budget d'innovation et budget de plateforme, avec des tests de financement différents, là où les autres fiches parlent de responsabilité ou de FinOps.
- **Une typologie des quatre échecs, chacun relié à une règle financière cassée** : dépendance (le code spécifique bloque l'agent, casse le coût total de possession), duplication (chaque agent refait intégrations et supervision, casse l'amortissement), fragmentation (trois outils, trois définitions d'« autorisation », casse la propriété des actifs), opacité (factures de tokens non reliées aux résultats, casse l'économie unitaire).
- **Financer le socle partagé comme un produit** : intégration, tests, garde-fous et supervision financés comme un produit, avec pour objectif que chaque nouvel agent coûte moins cher que le précédent. C'est une application directe du financement par produit aux agents.
- **Trois indicateurs pour le comité de direction** : part de la dépense IA rattachée à un workflow, coût par workflow terminé, coût de chaque nouvel agent rapporté au premier.
- **Un écart de croissance qui chiffre le problème** : budgets IT en hausse moyenne de 3,7 % mais financement de l'IA agentique en hausse de 31,8 % (enquête CIO Gartner), et hors centres de données la croissance des dépenses IT 2027 tombe à 8,6 % selon le calcul de l'auteur.

## 3. Résumé
L'auteur part d'un décalage : Claude, Copilot et Agentforce sont prêts, mais les plateformes SAP et ServiceNow sur lesquelles ils doivent agir ne le sont pas, parce que les deux sont financés séparément. Il pose le contexte budgétaire : Gartner prévoit 7,35 billions de dollars de dépenses IT en 2027 (+15 %), dont environ 487 milliards de hausse pour les centres de données (8,6 % de croissance sans eux, selon son calcul) ; les budgets IT progressent de 3,7 % en moyenne quand le financement de l'IA agentique bondit de 31,8 %. IBM (2 000 dirigeants tech) voit la part de l'IA passer de près de 15 % à près de 25 % des budgets IT entre 2025 et 2027, mais 85 % des dirigeants n'ont pas de visibilité complète sur la dépense IA en temps réel ; les organisations disciplinées financièrement déploient 2,4 fois plus d'agents à budget égal. Deloitte (3 500 dirigeants) : 40 % laissent l'IA exécuter des décisions sans validation humaine, 23 % ont une responsabilité floue en cas d'erreur. La Cloud Security Alliance relève que 82 % des organisations ont découvert des agents inconnus dans l'année, 21 % seulement ayant un processus de retrait. Il décrit ensuite quatre modes d'échec illustrés par des cas anonymes (assureur sur la clôture SAP, banque sur Salesforce, payeur santé, programme Medicaid d'un État), puis explique pourquoi les budgets ne les voient pas : circuits distincts, unités de prix hétérogènes (tokens, actions, sièges, heures projet) qui masquent les coûts partagés, refacturation interne mal adaptée aux agents. Le contexte marché suit : toutes les grandes plateformes ont lancé leur offre d'agents (Google, Microsoft Agent 365 à 15 dollars par utilisateur et par mois, ServiceNow AI Control Tower, SAP avec Anthropic, Salesforce Agentforce à 0,10 dollar par action, OpenAI Frontier, AWS), la maintenance standard de SAP ECC 6.0 s'arrête fin 2027, et les obligations de l'AI Act sur les systèmes à haut risque sont repoussées par l'Omnibus numérique (décembre 2027 et août 2028). Forrester juge la vision SAP crédible mais voit dans la concentration sur Claude un risque qui pourrait remonter au conseil d'administration dans les secteurs régulés d'ici 24 mois. L'auteur propose six étapes : partir du plan d'affaires et rattacher chaque dollar IA à un workflow ; associer chaque agent à sa dépendance de plateforme avec un responsable et un business case ; financer la machinerie partagée comme un produit ; garder la maîtrise du contexte métier et des définitions, acheter modèles et orchestration en les gardant interchangeables ; libérer l'autonomie par paliers ; tarifer au workflow terminé et retirer quelque chose chaque trimestre. Il conclut : financer agents et plateformes ensemble, et refuser les uns sans les autres.

## 4. Citations et noms
**Citations** :
- « Les agents sont prêts. Financez la plateforme sur laquelle ils tourneront. » (« The agents are ready. Fund the platform they will run on. »), Vipin Jain

**Noms cités** :
- *Vipin Jain, Transformation Enablers Inc.* : auteur, architecte et conseil en transformation.
- *IASA Chief Architect Forum* : association d'architectes partenaire de la publication.
- *Gartner* : prévisions de dépenses IT 2027 et enquête CIO (3,7 % contre 31,8 %).
- *IBM* : étude auprès de 2 000 dirigeants tech sur la part de l'IA dans les budgets et la visibilité de la dépense.
- *Deloitte* : enquête auprès de 3 500 dirigeants sur l'autonomie des agents et la responsabilité.
- *Cloud Security Alliance* : chiffres sur les agents inconnus et leur retrait.
- *NASCIO* : enquête 2026 auprès des CIO des États américains (28 % ont un financement IA dédié).
- *FinOps Foundation* : 98 % des répondants gèrent désormais la dépense IA (63 % en 2025, 31 % en 2024).
- *Forrester* : avis sur la vision SAP et le risque de concentration sur Claude.
- *SAP, ServiceNow, Salesforce, Microsoft, Google, OpenAI, AWS, Anthropic* : éditeurs de plateformes et d'agents cités dans le contexte marché.
- *Anthropic, Blackstone, Hellman & Friedman, Goldman Sachs* : fondateurs d'une société de services IA pour les entreprises.
- *Agentic AI Foundation* : héberge MCP et le standard Agent Skills donné par Anthropic en octobre.
- *Digital Omnibus (UE)* : texte qui reporte les obligations de l'AI Act.

## 5. Mots-clés
budgets IT, arbitrage de portefeuille, financement par produit, agents IA, FinOps, mesure du ROI

## Lecture CPO
- **Implications** :
  - Dans les comités d'arbitrage, refuser un agent présenté sans sa dépendance de plateforme (intégration, données, nettoyage du cœur ERP), et inversement : un seul dossier, un seul responsable.
  - Financer la couche partagée des agents (intégration, tests, garde-fous, supervision) comme un produit de plateforme, avec un objectif de baisse du coût marginal par agent.
  - Adopter les trois indicateurs proposés (part de la dépense IA rattachée à un workflow, coût par workflow terminé, coût du n-ième agent) dans le reporting de portefeuille.
  - Pour les clients SAP : relier la fin de maintenance d'ECC 6.0 (fin 2027) aux projets d'agents, plutôt que de les arbitrer séparément.
- **Fiabilité** : tribune d'un consultant en transformation (intérêt à vendre de l'accompagnement), publiée avec une association d'architectes. Chiffres nombreux et attribués (Gartner, IBM, Deloitte, CSA, FinOps Foundation), mais sans lien vers les méthodologies dans l'article ; les cas d'échec sont anonymes et illustratifs, et le 8,6 % est un calcul de l'auteur.
- **Maturité** : Tendance émergente : le diagnostic converge avec plusieurs sources de la semaine (SAP, Deloitte, Thelliez), mais le financement conjoint agent-plateforme reste une proposition, sans retour d'expérience.
- **Réutilisation** : article OCTO sur le financement des agents par produit (les quatre modes d'échec et leurs règles financières cassées) ; présentation client DSI ou comité d'investissement avec les trois indicateurs ; post LinkedIn « +3,7 % pour l'IT, +31,8 % pour l'IA agentique : qui paie la plateforme ? ».
