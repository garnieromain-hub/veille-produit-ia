# MCP servers can now deliver AI agent skills, changing what companies approve when they connect one

**Référence** : Sean Michael Kerner, VentureBeat, 25 novembre 2026, article (annonce éditeur commentée), https://venturebeat.com/technology/mcp-servers-can-now-deliver-ai-agent-skills-changing-what-companies-approve-when-they-connect-one

**Axe** : IA appliquée au produit

## 1. L'idée clé
Avec l'extension « Skills over MCP », un serveur MCP ne fournit plus seulement des outils et des données à un agent : il peut aussi lui livrer les instructions pour s'en servir. Connecter un serveur revient donc à approuver ce qu'il dit à l'agent de faire, et plus seulement ce qu'il lui permet de faire.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [ESET, les skills d'agents entités mouvantes](2026-11-25-itsocial-eset-skills-agents-securite.md), qui traitait les skills comme un maillon instable de la chaîne d'approvisionnement, et la fiche [Jain, agents et plateformes SAP et ServiceNow](2026-11-24-cio-jain-agents-plateformes-sap-servicenow.md), qui présentait le standard Agent Skills ; plus largement, le discours dominant qui distingue les outils (MCP) et les consignes (skills) installés séparément.
- **La fusion de l'outil et du mode d'emploi** : l'éditeur d'un serveur peut mettre à jour ses outils et ses consignes en même temps, sans rien à installer côté utilisateur. Le « runbook » voyage avec l'outil qu'il décrit.
- **Une réponse partielle au risque décrit par ESET** : la spécification qualifie les skills fournies par un serveur de risque d'injection de prompt, exige une approbation explicite de chaque skill avant toute exécution de code local, et une nouvelle approbation si une skill approuvée change. C'est le contrôle de version qu'ESET réclamait, cette fois inscrit dans le protocole.
- **Le périmètre d'approbation change pour les entreprises** : selon Guillaume Lebedel (StackOne), approuver un serveur MCP, c'est désormais approuver le comportement qu'il induit chez l'agent. Les processus de validation des connecteurs doivent en tenir compte.
- **Le coût du contexte comme contrainte** : un développeur avertit que charger automatiquement de mauvaises skills dans le contexte coûte vite cher, ce qui rejoint les sujets de FinOps des agents.
- **Des premiers éditeurs de logiciels** : Shopify, HubSpot, Atlassian, bientôt Carta, livrent déjà des skills métiers par ce canal, et Microsoft l'a intégré à VS Code.

## 3. Résumé
L'article s'ouvre sur l'annonce d'Anthropic : deux ans après avoir lancé le Model Context Protocol, l'éditeur ajoute « Skills over MCP » à Claude et Claude Code en bêta publique. Jusqu'ici, un serveur MCP donnait accès à des outils et à des données ; il peut désormais fournir aussi des instructions réutilisables de déroulement du travail, mises à jour en même temps que les outils, sans installation supplémentaire. La bêta est activée par défaut pour les offres Pro, Max et Ultra ; les offres Team supposent une activation par un administrateur, et Enterprise suivra. L'article cite les autres extensions : Tasks, qui permet à un serveur de mener des tâches longues pendant que Claude continue, et Elicitation, qui lui permet de demander des informations à l'utilisateur, toutes deux disponibles pour Pro, Max et Ultra ; File Uploads, à venir, enverra des fichiers aux serveurs sans passer par la fenêtre de contexte. Exemples donnés par Anthropic : des skills de Shopify (conception de boutique), HubSpot (accueil des clients), Atlassian (analyse du travail) et bientôt Carta (rédaction de documents sur le capital). Microsoft prend en charge l'extension dans VS Code à partir de la version 1.147. Rappel de contexte : MCP, publié en open source en novembre 2024, adopté par OpenAI et Microsoft, a rejoint l'Agentic AI Foundation de la Linux Foundation en décembre 2025. Vient ensuite la sécurité : la spécification signale le risque d'injection de prompt, impose une approbation explicite par skill avant toute exécution de code local et une nouvelle approbation à chaque modification ; Claude Code ignore certains paramètres des skills (permissions d'outils, hooks) et permet aux utilisateurs et organisations de fixer leurs propres règles. L'article termine sur les réactions : Filipe Motta, ingénieur DevOps, salue le runbook livré avec l'outil ; Jeff Allen, développeur, s'inquiète du coût d'un chargement automatique ; Guillaume Lebedel, CTO de StackOne, conclut qu'approuver un serveur MCP, c'est désormais approuver ce qu'il dit à l'agent de faire.

## 4. Citations et noms
**Citations** :
- « Le serveur qui expose vos outils Terraform ou Kubernetes peut aussi porter le runbook pour bien s'en servir » (« The server that exposes your Terraform or Kubernetes tools can also carry the runbook for using them well », Filipe Motta, ingénieur DevOps senior).
- « Je tiens toujours au contrôle, parce que charger automatiquement les mauvaises choses dans le contexte coûte vite cher » (« I still care about control, because auto-loading the wrong stuff into context gets expensive fast », Jeff Allen, développeur).
- « Désormais, cela veut aussi dire approuver ce qu'il dit à l'agent de faire » (« Now it also means approving what it tells the agent to do », Guillaume Lebedel, cofondateur et CTO de StackOne).

**Noms cités** :
- *Sean Michael Kerner* : journaliste chez VentureBeat, auteur.
- *Anthropic, Claude, Claude Code* : éditeur et produits qui lancent l'extension.
- *Model Context Protocol (MCP)* : protocole ouvert de connexion des agents aux outils et données.
- *Skills over MCP, Tasks, Elicitation, File Uploads* : extensions du protocole présentées.
- *Shopify, HubSpot, Atlassian, Carta* : éditeurs qui fournissent des skills par MCP.
- *Microsoft, VS Code* : prise en charge de l'extension à partir de la version 1.147.
- *OpenAI* : a adopté MCP.
- *Agentic AI Foundation (Linux Foundation)* : structure qui porte MCP depuis décembre 2025.
- *Filipe Motta, Jeff Allen* : praticiens cités pour l'intérêt et la limite de l'extension.
- *Guillaume Lebedel, StackOne* : CTO d'un éditeur d'intégrations, auteur de la conclusion.

## 5. Mots-clés
agents IA, ingénierie du contexte, sécurité, chaîne d'approvisionnement logicielle, gouvernance IA

## Lecture CPO
- **Implications** :
  - Pour un éditeur SaaS, livrer un serveur MCP avec ses skills devient une façon de distribuer le savoir-faire d'usage du produit (onboarding, bonnes pratiques) directement dans l'agent du client : un sujet de stratégie produit, pas seulement d'intégration.
  - Côté entreprise, les processus de validation des connecteurs doivent couvrir les instructions livrées, leur version et leurs mises à jour, et pas seulement les droits d'accès.
  - Surveiller le coût en contexte des skills chargées automatiquement : prévoir des règles d'activation et une mesure dans le FinOps des agents.
- **Fiabilité** : article de presse fondé sur l'annonce d'Anthropic, éditeur intéressé, et sur la spécification ; les réactions viennent de praticiens et d'un éditeur d'intégrations (StackOne). Pas de chiffres d'adoption ; extension encore en bêta.
- **Maturité** : Tendance émergente : MCP est largement adopté, mais la livraison de skills par serveur est en bêta et ses pratiques de gouvernance restent à construire.
- **Réutilisation** : post LinkedIn sur la formule de Lebedel (on n'approuve plus un accès, on approuve un comportement) ; présentation client sur la gouvernance des agents, avec la fiche ESET ; article OCTO sur le mode d'emploi livré avec le produit comme nouvelle surface produit des éditeurs.
