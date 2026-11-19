# Guide stratégique « Rewire for Data and AI »

**Référence** : Digital Realty (sans auteur nommé), juillet 2025 (PDF daté du 25 juillet 2025, chiffres d'enquête d'août 2024), livre blanc d'éditeur de 23 pages, accessible après formulaire, volume 2 de l'eBook « Are You Data and AI Ready ? » (janvier 2024), https://www.digitalrealty.com/fr/resources/white-papers/rewire-for-data-ai (PDF : https://go2.digitalrealty.com/rs/087-YZJ-646/images/eBook_Digital_Realty_2507_RewireDataAI_FR.pdf)

**Axe** : Investissement tech (Transformation des entreprises)

## 1. L'idée clé
L'infrastructure est le point de défaillance caché des stratégies IA : la latence, la « gravité des données » (les données attirent applications et services), le coût du cloud et les contraintes de résidence imposent de rapprocher le calcul des données. Le cloud seul ne suffit pas ; il faut une infrastructure distribuée, en colocation et interconnectée, et aligner stratégie IA et stratégie data center.

## 2. Ce qui est nouveau
**Par rapport à** : la prévision [Gartner des dépenses IT 2027](2026-11-13-gartner-depenses-it-2027.md) (la croissance est tirée par les data centers), l'étude [Cebr pour Wasabi](2026-11-19-cebr-wasabi-depassements-infrastructure-ia.md) (79 % de dépassement des budgets d'infrastructure en France) et le discours dominant « l'IA impose de moderniser ses fondations data ».

Presque rien de neuf, et le document date de plus d'un an : c'est une brochure commerciale qui redit le discours des hébergeurs. Seuls apports utilisables :
- **Un indicateur de maturité très bas** : 22 % des entreprises seulement sont « matures en IA » selon la définition de Digital Realty (IA intégrée au modèle d'affaires et stratégie de données distribuée). La définition est taillée pour l'offre du vendeur, mais le chiffre recoupe les autres enquêtes sur la minorité qui tire de la valeur.
- **L'écart entre intention et résultat** : 79 % des responsables data et IA mettent en œuvre une stratégie de données formelle, 84 % alignent la localisation des données sur leur feuille de route IA, mais 37 % seulement disent obtenir des résultats fondés sur les données avec l'IA. L'écart est plus parlant que chacun des chiffres.
- **Le cloud public contesté par un acteur de l'infrastructure** : les cinq limites listées (latence, matériel GPU, gravité des données, coût du fonctionnement continu, conformité) argumentent pour un modèle hybride ; c'est le pendant, côté vendeur, de la question des coûts imprévisibles soulevée par l'étude Cebr.

## 3. Résumé
Le guide part de l'enquête Global Data Insights Survey de Digital Realty (plus de 2 200 décideurs data et IA, août 2024) : extraire de la valeur des données est la priorité numéro un, trouver la bonne infrastructure le principal défi. Il introduit la « gravité des données » : plus les données grossissent pour nourrir les modèles, plus elles attirent applications et services, ce qui place la localisation des données au cœur de la stratégie d'entreprise. Il cite IDC (22 300 Md$ d'impact mondial de l'IA en 2030, 3,7 % du PIB) et Statista (marché de l'IA à 244 Md$ en 2025, plus de 800 Md$ en 2030), puis distingue trois formes d'IA (machine learning, IA générative, IA agentique) et annonce le passage de la « transformation numérique » à « l'infrastructure intelligente ».

Vient ensuite la thèse « le cloud ne suffit pas », en cinq limites. Le guide liste les freins : croire que l'IA est un problème de modèle ou de capacité cloud, la prolifération des données, le manque d'expertise, et une stratégie IA conduite à part de la stratégie IT et infrastructure. Il propose six impératifs (capacité, complexité, latence, conformité, risques, éco-responsabilité), chacun avec une « solution » qui renvoie à la colocation et à l'interconnexion, plaide pour « une entreprise, une stratégie d'IA » qui casse les silos, puis présente trois cas clients (Macnica : densité par rack doublée ; CoreWeave : déploiement deux fois plus rapide ; Geyser Data : mise en service en deux semaines, bande passante réduite de 90 %). Il se termine par une grille de douze critères pour choisir un hébergeur (optimisation, technique, proximité des données, sécurité, scalabilité, écosystème, portée, connectivité, pérennité, éco-responsabilité, souveraineté, coût) et la présentation de son offre.

## 4. Citations et noms
**Citations** :
- « L'infrastructure représente le point de défaillance potentiel caché dans la stratégie de nombreuses organisations. », Digital Realty
- « Si vous n'avez pas les bonnes données là où vous en avez besoin, votre stratégie d'IA est déjà compromise avant même d'avoir commencé. », Digital Realty

**Noms cités** :
- *Digital Realty* : opérateur américain de data centers et de colocation (plus de 300 sites, 5 000 clients), auteur et vendeur de la solution.
- *Global Data Insights Survey* : enquête de Digital Realty (plus de 2 200 répondants, août 2024), source des pourcentages.
- *Gravité des données (data gravity)* : concept de Dave McCrory ; Digital Realty en revendique une formule brevetée et un « Data Gravity Index ».
- *IDC* et *Statista* : sources des chiffres macro sur l'impact et le marché de l'IA.
- *Stanford AI100* : rapport de 2016 qui prévoyait les agents conversationnels pour 2030-2040, cité pour montrer que l'IA va plus vite que prévu.
- *Macnica, CoreWeave, Geyser Data* : clients présentés en études de cas.
- *PlatformDIGITAL, ServiceFabric, PDx* : offres et méthodologie commerciales de Digital Realty.

## 5. Mots-clés
infrastructure IA, souveraineté, budgets IT, données, adoption IA

## Lecture CPO
- **Implications** :
  - Pour un produit IA à forte volumétrie ou contrainte de latence, poser tôt la question de l'emplacement des données et du calcul : elle pèse sur le coût unitaire et la conformité autant que le choix du modèle.
  - Utiliser l'écart 79 % / 37 % (stratégie de données formelle contre résultats obtenus) pour rappeler qu'une stratégie data ne vaut que par la mesure de la valeur produite.
  - La grille de douze critères peut servir de point de départ pour un choix d'hébergeur, à compléter par la réversibilité, absente du document.
- **Fiabilité** : brochure commerciale d'un hébergeur, dont toutes les « solutions » mènent à son offre ; enquête propriétaire dont la méthodologie (pays, profils, questions) n'est pas publiée dans le guide ; chiffres d'août 2024, donc antérieurs à la vague agentique ; études de cas sans source indépendante. Les arguments contre le cloud public servent directement le vendeur.
- **Maturité** : Pratique établie : le discours sur la gravité des données et l'infrastructure hybride pour l'IA circule depuis plusieurs années chez les hébergeurs et les analystes.
- **Réutilisation** : à ne citer qu'en contrepoint. Éventuellement en présentation client DSI pour le chiffre des 22 % d'entreprises « matures » ou l'écart 79 % / 37 %, en nommant la source. Pas de matière pour un article OCTO ou un post LinkedIn.
