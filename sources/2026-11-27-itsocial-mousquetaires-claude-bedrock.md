# Le Groupement Mousquetaires intègre Claude à ses points de vente pour exploiter la donnée à la source

**Référence** : Mourad Krim, IT Social, 26 novembre 2026, article d'actualité et d'analyse, https://itsocial.fr/intelligence-artificielle/intelligence-artificielle-actualites/le-groupement-mousquetaires-integre-claude-a-ses-points-de-vente-le-retail-veut-valoriser-la-donnee-de-ses-magasins/

**Axe** : Transformation des entreprises (Portefeuille numérique)

## 1. L'idée clé
Dans la grande distribution, l'actif que chaque enseigne veut valoriser est désormais la donnée de magasin. Les Mousquetaires déploient Claude via Amazon Bedrock pour l'exploiter à la source, mais l'outil ne changera rien en magasin tant qu'il ne sera pas relié aux données de ventes, de stocks et d'approvisionnement.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Transfo IA avec Adeo, Carrefour et Renault](2026-11-10-le-ticket-transfo-ia-adeo-carrefour-renault.md) (l'IA dans le processus produit des grands groupes, plateforme multi-fournisseurs chez Renault) et le discours dominant sur le retail, centré sur l'IA côté client (assistants, commerce agentique).
- **Un déploiement par les magasins, pas par le siège** : la phase 1 vise 500 points de vente et 300 collaborateurs des fonctions support, sur 160 000 salariés, pour repérer les usages avant de généraliser. Chez Adeo ou Carrefour (fiche du 10 novembre), l'IA entrait d'abord par les équipes produit.
- **La passerelle multi-modèles comme choix d'architecture** : Bedrock donne accès à plusieurs familles de modèles et permet de changer de modèle sans refaire l'intégration. C'est la réversibilité de Renault, obtenue par la plateforme cloud plutôt qu'en interne.
- **Trois stratégies de retail comparées** : Carrefour (100 M€ par an, étiquettes et caméras Vusion, ouverture aux agents des clients), Walmart (Agent Gateway ouvert à l'assistant Muse de Meta, permissions par agent) et Schwarz (cloud propriétaire STACKIT, serveurs en Allemagne et en Autriche) visent la même ressource par des chemins différents.
- **Les zones blanches d'un contrat d'IA** : montant, région d'hébergement et calendrier après la phase 1 ne sont pas communiqués ; l'auteur en fait des décisions que la DSI devra trancher.

## 3. Résumé
Le Groupement Mousquetaires (Intermarché, Netto, Bricomarché), soit plus de 3 100 chefs d'entreprise indépendants et plus de 4 300 points de vente, a choisi Claude d'Anthropic, servi par Amazon Bedrock, à partir de janvier 2027. Une première phase couvre 500 points de vente et 300 collaborateurs des fonctions support, pour identifier les usages métier avant de généraliser. L'extension est prévue vers le pilotage des magasins, la production dans près de 60 usines, la logistique, l'informatique, les RH, le juridique et les achats. Le projet est porté par Jean-Philippe Sassi (STIME, la DSI du groupement) et Stéphane Sinopoli (monétisation de la donnée), pour qui l'IA servira la création de valeur, la performance des magasins restant la priorité. Il s'inscrit dans une suite : un Défi Innovation consacré à l'IA en décembre 2024, l'extension du partenariat avec SymphonyAI (plateforme CINDE) en janvier 2025. L'article souligne l'intérêt de Bedrock (changer de modèle sans reconstruire l'intégration) et ce qui manque : montant, hébergement des données, calendrier. Il compare ensuite avec Carrefour (plan Carrefour 2030 du 18 février, l'IA parmi trois axes, 100 M€ par an ; Vusion pour équiper les magasins d'ici 2030 ; Hopla puis panier composable dans ChatGPT depuis le 26 mars ; partenariat avec Google sur le commerce agentique), Walmart (Agent Gateway ouvert le 25 novembre à Muse, le client gérant les autorisations de chaque agent) et Schwarz (Schwarz Digits créé en 2023, cloud STACKIT). Conclusion : les trois stratégies visent la donnée de magasin, et l'outil ne produira d'effets qu'une fois branché sur les ventes, les stocks et l'approvisionnement.

## 4. Citations et noms
**Citations** :
- « Derrière ces choix d'intégration, la donnée de magasin devient l'actif que chaque enseigne veut valoriser. », Mourad Krim (chapeau)
- « L'intelligence artificielle sera au service de la création de valeur », Stéphane Sinopoli

**Noms cités** :
- *Groupement Mousquetaires (Intermarché, Netto, Bricomarché)* : groupement d'indépendants qui déploie Claude.
- *Jean-Philippe Sassi* : responsable de la STIME, DSI du groupement, porteur du projet.
- *Stéphane Sinopoli* : responsable de la monétisation de la donnée, porteur du projet.
- *Anthropic, Claude* : modèle retenu.
- *Amazon Bedrock (AWS)* : plateforme d'accès multi-modèles par laquelle Claude est servi.
- *SymphonyAI (CINDE)* : partenaire data et IA antérieur du groupement.
- *Carrefour, Alexandre Bompard, Vusion, Hopla, Google, ChatGPT* : stratégie concurrente, IA en magasin et ouverture aux agents des clients.
- *Walmart, Agent Gateway, Muse (Meta)* : passerelle pour agents tiers avec permissions gérées par le client.
- *Schwarz (Lidl, Kaufland), Schwarz Digits, STACKIT* : stratégie d'intégration verticale avec cloud propre.

## 5. Mots-clés
adoption IA, données, dépendance fournisseur, souveraineté, retour d'expérience, commerce agentique

## Lecture CPO
- **Implications** :
  - Un déploiement d'IA qui commence par les points de vente oblige à cadrer les cas d'usage avec le terrain avant de généraliser : la phase 1 est une discovery à l'échelle.
  - La valeur dépend de la connexion aux données opérationnelles (ventes, stocks, approvisionnement) : le chantier data est le vrai produit, le modèle n'en est qu'une brique.
  - Une couche d'abstraction multi-modèles (ici Bedrock) devient un critère d'architecture pour garder la main sur le choix du modèle.
  - Pour une DSI, hébergement, coût et calendrier doivent être arbitrés avant la généralisation, pas après.
- **Fiabilité** : journaliste IT, à partir de l'annonce du groupement et d'informations publiques sur les concurrents ; aucun chiffre de coût ni d'impact ; l'article signale lui-même les zones non communiquées.
- **Maturité** : Tendance émergente : annonce de déploiement, pas encore de résultats, mais les grands distributeurs convergent tous vers la valorisation de la donnée de magasin.
- **Réutilisation** : présentation client retail sur les trois modèles (passerelle cloud, cloud propriétaire, ouverture aux agents) ; post LinkedIn « Le modèle n'est rien sans la donnée de stock » ; table ronde sur la réversibilité des choix de modèle.
