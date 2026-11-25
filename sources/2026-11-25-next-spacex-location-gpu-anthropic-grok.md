# SpaceX gagne plus en louant ses GPU à Anthropic qu'avec Grok, « incapable de rivaliser »

**Référence** : Mickael Bazoge, Next, 24 novembre 2026, article (s'appuie sur le New York Times du 23 novembre, le rapport de résultats du troisième trimestre 2026 de SpaceX et son prospectus d'introduction en Bourse), https://next.ink/269521/spacex-gagne-plus-en-louant-ses-gpu-a-anthropic-quavec-grok-incapable-de-rivaliser/

**Axe** : Investissement tech

## 1. L'idée clé
La branche IA de SpaceX (ex-xAI, devenue SpaceXSI) ne parvient pas à rivaliser avec OpenAI et Anthropic sur les modèles : elle gagne désormais davantage en louant la capacité inutilisée de ses centres de données à ses concurrents qu'avec Grok. « Moins glamour que les modèles IA, mais ça rapporte », et cela justifie de nouveaux investissements dans les centres de données.

**Attention au titre** : il surinterprète les chiffres. SpaceX ne publie aucun revenu séparé pour Grok ni pour la location de GPU. Le seul chiffre publié est un segment IA agrégé (7,56 Md$ au T3) qui mélange location de calcul, Cursor, abonnements Grok et X, et publicité sur X. La comparaison « plus qu'avec Grok » est une déduction de l'auteur à partir de montants contractuels non sourcés, pas un chiffre publié.

## 2. Ce qui est nouveau
**Par rapport à** : les fiches sur l'introduction en Bourse d'Anthropic ([Crunchbase](2026-11-19-crunchbase-anthropic-ipo-chiffres-cles.md), [FrenchWeb](2026-11-20-frenchweb-anthropic-ipo-cout-croissance.md)), qui décrivent la dépendance d'Anthropic à ses fournisseurs de calcul, et au discours dominant selon lequel chaque grand acteur de l'IA doit avoir son propre modèle de pointe.
- **Un lab de modèles qui devient loueur de calcul** : SpaceXSI loue depuis le printemps ses GPU inutilisés à Anthropic (premier client) et à Google. Le capital investi dans l'infrastructure trouve un rendement chez les concurrents plutôt que dans le produit maison.
- **Des montants contractuels inédits, mais non sourcés** : 3,1 Md$ par mois pour Anthropic, 920 M$ pour Google, contrats pouvant courir jusqu'en 2029. L'article ne dit pas d'où viennent ces chiffres, et ils ne se réconcilient pas avec le segment publié : 3,1 Md$ par mois feraient environ 9,3 Md$ par trimestre, plus que les 7,56 Md$ du segment IA entier (sans doute un montant à venir ou un autre périmètre, l'article ne le précise pas).
- **Le revenu par GPU comme critère d'arbitrage interne** : Musk demande aux ingénieurs de justifier chaque usage de GPU, la compétitivité se mesurant « au chiffre d'affaires par GPU ». Conséquence : avatars animés (dont Ani) fermés, Digital Optimus réaffecté, équipe Grok Imagine (60 personnes) dissoute.
- **L'aveu du dirigeant** : selon le New York Times, Musk a écrit en août sur le canal interne de la division IA « On loue de la puissance de calcul parce qu'on n'arrive pas à rivaliser ».

## 3. Résumé
L'article part du constat que l'IA de SpaceX, issue de xAI, reste derrière OpenAI et Anthropic. Depuis le printemps, SpaceXSI loue à Anthropic et à Google la capacité de ses centres de données qu'elle n'utilise pas : xAI aurait exploité moins de la moitié de la capacité de Colossus l'an dernier. Anthropic serait devenu le premier client, avec 3,1 Md$ par mois, contre 920 M$ pour Google, sur des contrats pouvant aller jusqu'en 2029. Au troisième trimestre, le segment IA a pesé 7,56 Md$ sur 14,58 Md$ de chiffre d'affaires total (51,9 %), mais ce total mélange location de calcul, revenus de Cursor, abonnements Grok et X et publicité sur X. L'auteur cite ensuite le New York Times : en août, Musk a renommé brièvement le groupe de discussion de la division IA pour écrire qu'il louait du calcul faute de pouvoir rivaliser, et il impose désormais une justification de chaque usage de GPU par le revenu qu'il produit. Plusieurs projets en ont fait les frais (avatars animés, Digital Optimus, Grok Imagine). Le prospectus de SpaceX évoque par ailleurs une « complexité opérationnelle ». L'article conclut que la location « rapporte » et justifie les plus de 74 Md$ d'investissements supplémentaires annoncés le 12 novembre pour des sites en Arizona et au Texas.

## 4. Citations et noms
**Citations** :
- « On loue de la puissance de calcul parce qu'on n'arrive pas à rivaliser », Elon Musk, message interne d'août rapporté par le New York Times.
- « Au bout du compte, la compétitivité se mesure au chiffre d'affaires par GPU », règle de pilotage attribuée à Elon Musk.
- « C'est moins glamour que les modèles IA, mais ça rapporte », Mickael Bazoge, Next.

**Noms cités** :
- *SpaceXSI (ex-xAI, ex-SpaceXAI)* : branche IA de SpaceX, éditrice de Grok, devenue loueuse de GPU.
- *Elon Musk* : dirigeant, auteur de l'aveu et de la règle du revenu par GPU.
- *Anthropic* : premier client de la location de GPU (3,1 Md$ par mois selon l'article).
- *Google* : second client (920 M$ par mois).
- *Grok, Grok Imagine, Ani, Digital Optimus* : produits et projets IA de SpaceXSI, dont plusieurs arrêtés ou réduits.
- *Colossus* : centre de données de xAI, sous-utilisé l'an dernier.
- *Cursor* : éditeur d'outil de code dont les revenus entrent dans le segment IA de SpaceX.
- *The New York Times* : source de l'aveu de Musk (23 novembre) et du DealBook Summit (18 novembre).

## 5. Mots-clés
infrastructure IA, concentration du marché, modèle économique, arbitrage de portefeuille, mesure de la valeur

## Lecture CPO
- **Implications** :
  - Pour un acheteur d'IA : le marché du calcul se concentre et les concurrents s'approvisionnent les uns chez les autres. La dépendance fournisseur se joue aussi au niveau de l'infrastructure, pas seulement du modèle.
  - Le « revenu par GPU » est un critère d'arbitrage de portefeuille brutal mais lisible : il illustre comment une ressource rare (le calcul) devient l'unité de priorisation des produits. Transposable en interne avec le coût en tokens par produit ou par cas d'usage.
  - Ne pas reprendre le titre tel quel : la comparaison location contre Grok n'est pas publiée, et les montants contractuels ne collent pas avec le segment trimestriel.
- **Fiabilité** : média tech français sérieux, mais qui assemble des sources secondaires. Le segment de 7,56 Md$ vient du rapport trimestriel de SpaceX ; l'aveu et la règle par GPU viennent du New York Times ; les montants de 3,1 Md$ et 920 M$ par mois ne sont pas sourcés et paraissent incohérents avec le segment publié. Le titre va au-delà de ce que montrent les chiffres.
- **Maturité** : Signal faible : un cas unique, chiffré de façon partielle, qui suggère qu'un acteur de modèles peut se replier sur la vente de capacité.
- **Réutilisation** : post LinkedIn sur « quand le lab devient loueur de GPU » (en signalant la limite des chiffres) ; présentation client DSI sur la concentration de l'infrastructure IA et la dépendance fournisseur, en regard des fiches sur l'IPO d'Anthropic ; illustration d'un arbitrage de portefeuille par la ressource rare.
