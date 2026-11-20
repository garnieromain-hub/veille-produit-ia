# La fraude aux tokens est là, et c'est grave

**Référence** : Simon Willison, Simon Willison's Weblog, 20 novembre 2026, billet de lien commentant une vidéo YouTube et un post X de Claire Vo (ChatPRD), https://simonwillison.net/2026/Nov/20/token-fraud-is-here-and-its-bad/

**Axe** : IA appliquée au produit (Product management)

## 1. L'idée clé
Les produits IA qui offrent un essai gratuit subissent une fraude organisée : des utilisateurs enchaînent essais et codes promo pour consommer des tokens gratuitement, les revendre ou faire tourner une activité commerciale sur l'agent. Pour ChatPRD, la seule réponse raisonnable a été de supprimer complètement l'essai gratuit.

## 2. Ce qui est nouveau
**Par rapport à** : le discours dominant de la croissance produit, qui fait de l'essai gratuit et du product-led growth le mode d'acquisition par défaut du logiciel, et aux fiches sur le coût des tokens ([Cebr/Wasabi](2026-11-19-cebr-wasabi-depassements-infrastructure-ia.md)), vu jusqu'ici du côté de l'entreprise cliente.
- **Le coût marginal de l'IA casse le freemium** : contrairement au SaaS classique, chaque utilisateur gratuit coûte des tokens, ce qui rend l'essai exploitable à l'échelle par des fraudeurs. C'est le revers, côté éditeur, du sujet FinOps.
- **Une fraude organisée, pas opportuniste** : l'exemple d'un studio de cartes Roblox et Fortnite qui enchaîne essais et codes promo pour produire avec l'agent montre un usage commercial structuré.
- **Le sondage des modèles** : des prompts répétés (SVG de pélicans à vélo) servent, selon Willison, à identifier le modèle sous-jacent d'un produit, chaque famille ayant une signature reconnaissable. Le produit IA est examiné comme une ressource à revendre.

Le billet est court : l'apport tient au témoignage d'une éditrice connue de la communauté produit et à l'hypothèse de Willison sur l'identification des modèles.

## 3. Résumé
Simon Willison relaie une vidéo de Claire Vo, qui dirige ChatPRD, plateforme d'IA aidant les PM à passer d'une idée à une spécification, développée en public depuis l'époque de GPT-4. Elle y décrit une vague de « fraude aux tokens » liée à l'abus de l'essai gratuit : certains veulent simplement de l'IA gratuite, d'autres revendent les tokens ou font tourner une activité commerciale sur son agent. Exemple : un utilisateur qui se présente comme financeur d'un studio international de cartes Roblox et Fortnite fait tourner une boucle d'essais gratuits et de codes promo pour construire ses cartes avec l'agent. Willison relève des prompts récurrents demandant des SVG de pélicans à vélo, son propre test de référence, et suppose que les fraudeurs s'en servent pour reconnaître les modèles sous-jacents, technique qu'il a lui-même utilisée pour identifier des modèles en aperçu anonyme sur OpenRouter. Claire Vo supprime complètement ses essais gratuits ; Willison juge que c'est probablement la bonne décision.

## 4. Citations et noms
**Citations** :
- « Ils font tourner une boucle d'essais gratuits et de codes promo. » (« run a loop of free trials and promo codes »), Claire Vo, rapportée par Simon Willison.

**Noms cités** :
- *Claire Vo* : fondatrice de ChatPRD, témoin de la fraude dans sa vidéo.
- *ChatPRD* : produit IA pour PM (idée vers spécification), victime de la fraude.
- *Simon Willison* : développeur et blogueur, auteur du billet et de l'hypothèse sur l'identification des modèles.
- *Pélican à vélo (pelican riding a bicycle)* : test informel de Willison pour comparer les modèles, détourné pour les identifier.
- *OpenRouter* : place de marché de modèles où Willison a utilisé la même technique sur des modèles anonymes.
- *Roblox, Fortnite* : plateformes de jeu pour lesquelles le studio fraudeur construit des cartes.

## 5. Mots-clés
coûts des tokens, conception de produits IA, tarification, sécurité, product-led growth

## Lecture CPO
- **Implications** :
  - Pour un produit IA, l'essai gratuit est un poste de coût variable exposé à la fraude : le dimensionner (quotas, vérification d'identité, carte bancaire, plafonds de tokens) dès la conception, pas après.
  - Ajouter la détection d'abus (boucles d'essais, codes promo, prompts de sondage des modèles) aux indicateurs suivis par l'équipe produit.
  - Revoir les modèles d'acquisition fondés sur le freemium : la marge brute d'un produit IA ne supporte pas les mêmes hypothèses que le SaaS.
- **Fiabilité** : témoignage d'une éditrice sur son propre produit, relayé par un blogueur technique reconnu et indépendant ; aucun chiffre sur l'ampleur ou le coût de la fraude. L'idée que les pélicans servent à identifier le modèle est une hypothèse de Willison. La vidéo d'origine n'a pas été visionnée pour cette fiche.
- **Maturité** : Signal faible : un cas unique, sans données, mais qui découle mécaniquement du coût marginal des tokens et risque de se généraliser.
- **Réutilisation** : post LinkedIn « L'essai gratuit, angle mort des produits IA » ; table ronde CPO sur la tarification et la marge des produits IA ; article OCTO sur le FinOps côté éditeur, en miroir du FinOps côté client (fiche Uber du même jour).
