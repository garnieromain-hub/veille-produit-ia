# Paquets npm malveillants, les agents aggravent le risque des paquets légitimes détournés

**Référence** : Mourad Krim, IT Social, 25 novembre 2026, article (analyse d'une étude de l'équipe de recherche sur les menaces de Databricks, publiée le 23 novembre 2026), https://itsocial.fr/cybersecurite/cybersecurite-articles/paquets-npm-malveillants-les-agents-aggravent-le-risque-des-paquets-legitimes-detournes/

**Axe** : IA appliquée au produit

## 1. L'idée clé
Sur npm, le danger ne vient pas des faux paquets, presque jamais téléchargés, mais des paquets légitimes détournés depuis des chaînes d'intégration compromises : 7 % du corpus, plus de 99 % des téléchargements. Les agents de code, qui installent et mettent à jour des dépendances sans relecture, amplifient ce risque ; il faut donc un registre interne, des chaînes d'intégration durcies et aucune installation par un agent sans approbation.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [ESET sur les skills des agents](2026-11-25-itsocial-eset-skills-agents-securite.md) (les extensions d'agents comme maillon mouvant de la chaîne d'approvisionnement), la fiche [OpenRouter sur les vols de conversations](2026-11-24-solutions-numeriques-openrouter-vols-conversations.md) et le discours dominant, qui vise surtout le typosquattage et les faux paquets.
- **Le risque est dans les dépendances de confiance** : les paquets créés de toutes pièces font 89 % du corpus mais 0,2 % des téléchargements. Cela renverse la priorité habituelle de défense.
- **La publication « de confiance » n'est pas une garantie** : 85 % des paquets publiés par ce canal sont des paquets légitimes compromis, republiés via OpenID Connect depuis des CI piratées ; un ver a même produit des versions de TanStack avec attestations de provenance valides.
- **Les agents comme accélérateur mesuré** : plus de 40 % des demandes de fusion démarrent par un jet d'agent en septembre 2026 contre 17 % en mars (GitHub) ; GPT-5 invente la version dans 27,8 % de 37 000 mises à niveau testées (Sonatype). La fiche ESET posait le principe ; celle-ci chiffre l'exposition.
- **Des retraits lents** : npm neutralise 40 % des paquets en 7,1 jours de médiane, 10 % après plus de 59 jours, et 16 % restaient installables au moment de l'analyse.
- **Des recommandations opérationnelles précises** pour les agents : pas d'installation de paquet ni de serveur MCP sans approbation, versions épinglées, intégrité des fichiers de configuration surveillée.

## 3. Résumé
L'article s'appuie sur l'analyse par Databricks d'environ 5 400 paquets malveillants publiés sur npm entre décembre 2025 et octobre 2026, première année après la révocation des jetons de longue durée, en ne retenant que ceux confirmés par une source indépendante. Il rappelle l'affaire TanStack : un cas isolé en mai, devenu tendance mesurée. Premier constat : les faux paquets sont nombreux (89 %) mais inoffensifs en pratique (0,2 % des téléchargements, 81 % jamais téléchargés), quand les paquets légitimes compromis (7 %) captent plus de 99 % des téléchargements. Deuxième constat : l'attaque passe par les chaînes de construction plutôt que par des jetons volés ; bloquer les scripts d'installation ne couvre qu'une partie du risque, puisque seuls 54 % des paquets en ont un, et la plus grosse campagne de l'année n'en utilisait que dans 1 % des cas. Un ver autoréplicant a compromis plus de cent paquets en mai et août. Troisième constat : le registre ne filtre pas et retire tard (avis OSV en 1,7 jour, neutralisation npm en 7,1 jours de médiane). Le trafic imite un développeur ordinaire (38 % passent par des services légitimes comme Cloudflare Workers, Telegram ou Slack), et une campagne de confusion de dépendances a fourni 78 % des versions malveillantes d'août. Vient alors le rôle des agents : 9 800 milliards de téléchargements de composants en 2025 (+67 %, Sonatype), plus de 40 % des demandes de fusion lancées par un agent (GitHub Octoverse 2026), 30 millions de mises à jour Dependabot fusionnées, versions inventées par les modèles ; les attaquants ciblent déjà serveurs MCP et configurations d'assistants, et les voleurs de clés d'IA font 1 à 4 % des paquets. L'article conclut sur des recommandations (registre interne avec liste blanche ou âge minimal, CI à identifiants éphémères, machine compromise traitée comme telle, identifiants leurres, approbation des installations par les agents) et sur les limites de l'étude : npm seul, détection propre à Databricks.

## 4. Citations et noms
**Citations** : rien de notable (l'article est factuel et ne contient pas de formule citable).

**Noms cités** :
- *Databricks (équipe de recherche sur les menaces)* : auteur de l'étude sur 5 400 paquets npm malveillants.
- *npm* : registre de paquets JavaScript analysé.
- *TanStack* : bibliothèque dont des versions piégées portaient des attestations de provenance valides.
- *Sonatype* : rapport 2026 sur les téléchargements de composants et les versions inventées par les modèles.
- *GitHub Octoverse 2026, Dependabot* : chiffres sur la part des demandes de fusion lancées par des agents et les mises à jour automatisées.
- *OSV* : format public des avis de vulnérabilité.
- *MCP* : protocole dont les serveurs sont devenus une cible.

## 5. Mots-clés
agents IA, sécurité, chaîne d'approvisionnement logicielle, gouvernance IA, autonomie des agents

## Lecture CPO
- **Implications** :
  - Fixer une règle claire pour les agents de code des équipes produit : aucune installation de dépendance ou de serveur MCP sans approbation humaine, versions épinglées.
  - Faire passer toutes les dépendances par un registre interne (liste blanche ou âge minimal), y compris pour les prototypes faits avec l'IA.
  - Intégrer le coût de cette gouvernance (registre, CI durcie, revue) dans le business case des agents de code.
  - Prévoir le scénario d'incident : machine compromise, rotation de tous les identifiants accessibles.
- **Fiabilité** : étude d'un éditeur (Databricks) qui a intérêt à montrer sa capacité de détection, mais méthodologie décrite (corpus, confirmation indépendante, limites assumées) ; chiffres complémentaires sourcés (Sonatype, GitHub). Article de cybersécurité, retenu parce qu'il éclaire directement l'usage des agents de code par les équipes produit.
- **Maturité** : Tendance émergente : les attaques de chaîne d'approvisionnement sont connues, leur amplification par les agents commence à être mesurée.
- **Réutilisation** : présentation client DSI ou RSSI sur la gouvernance des agents de code ; post LinkedIn « 7 % des paquets, 99 % des téléchargements » ; article OCTO sur le coût caché du vibe coding, en croisant avec la fiche ESET.
