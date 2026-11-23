# AI is changing the build-versus-buy equation. Are CIOs ready?

**Référence** : Nick Colisto (SVP et DSI d'Avery Dennison, industriel de 9 Md$), CIO.com, 20 novembre 2026, tribune (rubrique Opinion), https://www.cio.com/article/4250943/ai-is-changing-the-build-versus-buy-equation-are-cios-ready.html

**Axe** : Portefeuille numérique (Investissement tech)

## 1. L'idée clé
L'IA réduit le coût de création du logiciel, pas son coût de possession. Les DSI doivent revoir l'arbitrage entre construire et acheter pour les applications SaaS spécialisées et non critiques, mais garder les plateformes cœur (ERP, RH, paie, finance), et décider sur le cycle de vie complet de l'application.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Crunchbase sur la SaaSpocalypse](2026-11-20-crunchbase-anton-saaspocalypse-marches.md) (les marchés ont surréagi à la menace de l'IA sur le SaaS), la fiche [TPC sur le Product Builder](2026-10-16-tpc-product-builder-outils-internes.md) (des profils qui construisent les outils internes avec l'IA) et la fiche [Talbot sur le vibe coding](2026-10-16-talbot-vibe-coding-decisions-cachees.md) (les décisions cachées dans le code généré).
- **Le point de vue d'un DSI acheteur, pas d'un investisseur ou d'un vendeur** : la menace sur le SaaS est examinée ligne par ligne dans le parc applicatif, en séparant les applications de niche, remplaçables, des plateformes cœur, à garder.
- **Une grille en cinq questions** : différenciation stratégique, complexité, coût total de possession réel, capacité à maintenir ce qu'on construit, possibilité d'étendre l'existant. La cinquième est la plus originale : l'alternative à un nouveau SaaS n'est pas forcément de construire, mais d'étendre ce qu'on possède déjà.
- **Deux gouvernances distinctes** : développeurs professionnels assistés par l'IA dans un cadre d'ingénierie, et utilisateurs métier qui construisent des applications légères dans des limites définies. Le risque de shadow IT est nommé.
- **La renégociation comme levier** : les éditeurs utilisent aussi l'IA, donc le DSI doit demander aux renouvellements si leurs prix vont baisser ou monter.

## 3. Résumé
L'auteur part d'un constat de parc applicatif : les grandes entreprises font tourner des centaines d'applications SaaS, dont certaines se recoupent ou servent peu, pour des abonnements en hausse. Le développement assisté par l'IA pourrait rendre rentable le remplacement des plus simples. Il tempère aussitôt : l'étude randomisée de METR (2025) a montré que des développeurs open source expérimentés mettaient environ 19 % de temps en plus avec des outils d'IA, alors qu'ils pensaient aller plus vite ; il refuse de généraliser ce résultat, mais en retient que produire du code plus vite ne garantit pas de livrer plus vite un logiciel fiable. Il liste ensuite les coûts cachés : selon Veracode (2025), 45 % des échantillons de code généré évalués introduisaient des failles de sécurité ; s'y ajoutent la maintenance, la responsabilité quand les auteurs partent, l'intégration avec l'ERP, le CRM et la gestion des identités, la montée en charge et le shadow IT né du vibe coding des métiers. Il propose cinq questions pour arbitrer, puis distingue la gouvernance des développeurs professionnels de celle des métiers. Il rappelle que les éditeurs utilisent eux aussi l'IA et invite à poser la question des prix aux renouvellements. Conclusion : un modèle hybride est probable, et la bonne question est quelle option donne le meilleur résultat sur toute la vie de l'application.

## 4. Citations et noms
**Citations** :
- « L'IA réduit le coût de création du logiciel. Elle n'a pas supprimé le coût de sa possession. » (« AI is reducing the cost of creating software. It has not eliminated the cost of owning software. »), Nick Colisto
- « Le vibe coding rend peut-être le logiciel plus facile à construire. Pas forcément plus facile à posséder. » (« Vibe coding may make software easier to build. It doesn't necessarily make software easier to own. »), Nick Colisto
- « La meilleure alternative à l'achat d'une nouvelle application SaaS n'est peut-être pas d'en construire une. » (« The best alternative to purchasing another SaaS application may not be building a new one. »), Nick Colisto

**Noms cités** :
- *Avery Dennison* : employeur de l'auteur, industriel mondial de 9 Md$.
- *METR* : étude randomisée de 2025, développeurs open source expérimentés environ 19 % plus lents avec l'IA.
- *Veracode* : rapport 2025, 45 % des échantillons de code généré par IA avec des failles de sécurité.
- *NinjaOne* : éditeur dont l'auteur siège au comité consultatif CXO, mentionné seulement dans sa biographie.
- *Vibe coding* : développement par des non-informaticiens avec l'IA, source de shadow IT.

## 5. Mots-clés
build vs buy, rationalisation applicative, coût total de possession, vibe coding, gouvernance IA, budgets IT

## Lecture CPO
- **Implications** :
  - Intégrer les cinq questions à la revue du portefeuille applicatif, avant chaque renouvellement SaaS ou demande d'outil interne.
  - Chiffrer le coût total de possession d'une application construite avec l'IA (maintenance, sécurité, intégration, propriétaire désigné), pas seulement son coût de développement.
  - Définir deux cadres de gouvernance distincts (ingénierie et métiers) plutôt qu'interdire ou laisser faire le vibe coding.
  - Utiliser la productivité IA des éditeurs comme argument de négociation aux renouvellements.
- **Fiabilité** : DSI praticien d'un grand groupe, discours prudent ; deux chiffres sourcés (METR, Veracode) mais externes, aucun retour d'expérience chiffré d'Avery Dennison. L'auteur siège au comité consultatif d'un éditeur SaaS (NinjaOne), ce qui n'est signalé que dans sa biographie, pas dans le corps de l'article : intérêt plutôt favorable au maintien de l'achat.
- **Maturité** : Tendance émergente : la remise en cause du SaaS par l'IA est très discutée en 2026, mais les grilles d'arbitrage côté DSI restent rares et non éprouvées.
- **Réutilisation** : article OCTO sur la rationalisation du parc applicatif à l'ère de l'IA (les cinq questions comme trame) ; présentation client DSI ; post LinkedIn (« construire coûte moins cher, posséder pas »).
