# À Ignite 2026, Microsoft détaille sept piliers pour devenir l'architecte de votre entreprise agentique

**Référence** : Laurent Delattre, IT for Business, 25 novembre 2026, compte rendu d'événement (Microsoft Ignite 2026, San Francisco, 17-20 novembre), https://www.itforbusiness.fr/microsoft-ignite-2026-entreprise-agentique-110395

**Axe** : IA appliquée au produit (Portefeuille numérique)

## 1. L'idée clé
Microsoft veut être la plateforme de l'entreprise agentique, du poste de travail (Copilot, Windows) jusqu'à l'infrastructure (Azure, puces), en passant par une couche de connaissance (Microsoft IQ) et une console de gouvernance des agents (Agent 365). Mais une grande partie des annonces est en préversion, les coûts sont difficiles à prévoir, et l'ensemble accroît la dépendance à l'écosystème Microsoft.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Orchestration agentique et DSI (IT Social)](2026-11-20-itsocial-orchestration-agentique-dsi.md) (Agent 365 et Entra : le verrouillage se déplace du modèle vers la console) et la fiche [Nadella chez Pragmatic Engineer](2026-11-19-pragmatic-engineer-nadella-code-bon-marche.md) (modèles MAI, intelligence hybride).
- **Les applications Office deviennent des modules de Copilot** : Copilot devient l'environnement de travail (Copilot Home fusionne chat et Cowork, Copilot Auto choisit le modèle), avec un partenariat Salesforce (« Copilotforce ») en préversion. L'inversion de la hiérarchie entre suite bureautique et assistant est une nouveauté.
- **Un prix et une ampleur pour la gouvernance des agents** : Agent 365 à 15 dollars par utilisateur et par mois (ou inclus dans M365 E7), avec détection des agents fantômes, notation des risques et outils FinOps ; Microsoft revendique plus de 50 millions d'agents enregistrés, sans dire combien sont actifs.
- **Des modèles maison spécialisés et moins chers** (MAI-Code-2, MAI-Cyber-2-Flash, Microsoft-Decision-1.1), présentés comme entraînés de zéro ; l'auteur note que MAI-Thinking-1 a utilisé des données du web, et que la vraie protection est contractuelle.
- **Une lecture critique dans un compte rendu de salon** : l'auteur liste ce qui reste à prouver (autonomie, fiabilité, économies) et prévient que les agents « inventent » un nouveau travail d'administration.

## 3. Résumé
Satya Nadella ouvre Ignite 2026 sur deux questions : comment utiliser des capacités d'IA qui progressent vite, et comment en gérer les conséquences. Microsoft y répond par trois fondations (ambition humaine, intelligence organisationnelle, confiance) et sept piliers techniques :
1. Copilot comme environnement de travail : Office devient un ensemble de modules, Copilot Home et Copilot Auto, Autopilot, Workspaces et Code en accès restreint (programme Frontier), Copilotforce avec Salesforce en préversion.
2. Microsoft IQ, couche de connaissance en quatre briques (Work IQ, Fabric IQ, Foundry IQ, Web IQ), plus de 350 connecteurs tiers et des Business Plugins, disponible en général avec des parties en préversion.
3. Agent 365, plan de contrôle des agents : détection des agents fantômes, Entra Agent ID pour les agents tiers, score de risque, gestion des coûts et Business Analytics (en préversion), 15 dollars par utilisateur et par mois ou inclus dans M365 E7 ; plus de 50 millions d'agents enregistrés revendiqués.
4. Modèles MAI maison, spécialisés et moins chers, avec la nuance sur les données d'entraînement et le Customer Copyright Commitment.
5. Sécurité et transparence : agents Red, Blue et Green Team disponibles, AI Transparency Initiative avec plus de 40 organisations pour des traces d'agents vérifiables.
6. Azure : bacs à sable d'agents, Agent Grid (réseau zéro confiance), mémoire contextuelle, outils de modernisation et de SRE assistés, HorizonDB (PostgreSQL avec recherche vectorielle), puces Cobalt 200 et Maia 200 (Maia 300 attendue en 2027).
7. Windows comme plateforme d'agents sécurisée : Microsoft Execution Containers, Windows 365 for Agents (PC cloud pour agents), protection administrateur, IA hybride locale et cloud.
L'auteur conclut sur trois réserves : beaucoup de fonctions sont en préversion ou réservées à Frontier, les coûts (licences, consommation de modèles, crédits) sont difficiles à anticiper, et la couche de connaissance comme la gouvernance renforcent la dépendance à Microsoft, ce que les promesses d'ouverture ne compensent pas.

## 4. Citations et noms
**Citations** :
- « L'alignement reste insaisissable. L'interprétabilité mécaniste de ces modèles aussi. », Satya Nadella
- « Les agents ne suppriment pas le travail d'administration, ils en inventent simplement un nouveau », Laurent Delattre

**Noms cités** :
- *Satya Nadella* : PDG de Microsoft, cadre les deux questions d'ouverture.
- *Copilot (Home, Auto, Autopilot, Workspaces, Code)* : nouvel environnement de travail, Office en modules.
- *Microsoft IQ* : couche de connaissance (Work IQ, Fabric IQ, Foundry IQ, Web IQ).
- *Agent 365 et Entra Agent ID* : gouvernance et identité des agents, y compris tiers.
- *Modèles MAI* : modèles maison spécialisés.
- *Salesforce* : partenaire de Copilotforce.
- *Programme Frontier* : accès anticipé et restreint aux fonctions en préversion.
- *AI Transparency Initiative* : coalition de plus de 40 organisations pour des traces d'agents vérifiables.

## 5. Mots-clés
agents IA, gouvernance IA, dépendance fournisseur, FinOps, bac à sable, infrastructure IA

## Lecture CPO
- **Implications** :
  - Pour les produits construits sur Microsoft 365, anticiper que Copilot devient le point d'entrée de l'utilisateur : la question est de savoir comment son produit s'y branche (plugins, connecteurs, Microsoft IQ).
  - Au niveau portefeuille, traiter Agent 365 comme une décision d'architecture : un inventaire et une console d'agents utiles, mais qui fixent l'écosystème pour plusieurs années.
  - Budgéter les agents avec une marge d'incertitude : licences, consommation de modèles et crédits se cumulent, et beaucoup de briques sont encore en préversion.
- **Fiabilité** : annonces d'éditeur relayées par une rédaction qui ajoute une analyse critique utile ; le chiffre de 50 millions d'agents est une revendication de Microsoft sans mesure de l'activité.
- **Maturité** : Tendance émergente : la gouvernance centralisée des agents s'installe chez tous les grands éditeurs, mais l'essentiel des fonctions n'est pas encore généralement disponible.
- **Réutilisation** : présentation client sur le choix d'une console de gouvernance des agents et le risque de dépendance (avec la fiche IT Social) ; post LinkedIn « Office devient un module de Copilot » ; table ronde DSI sur le coût réel des agents.
