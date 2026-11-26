# Do legacy systems wear out?

**Référence** : David Stephens (lead systems programmer, Longpela Expertise), CIO.com, 25 novembre 2026, tribune (rubrique « First Person »), https://www.cio.com/article/4252566/do-legacy-systems-wear-out.html

**Axe** : Portefeuille numérique

## 1. L'idée clé
Les systèmes hérités ne s'usent pas en eux-mêmes : ce sont la négligence, une maintenance insuffisante et l'absence de support qui en font un passif. Un système ancien bien entretenu et supporté peut durer, et le vrai sujet pour le DSI est de financer cet entretien, pas de remplacer par principe ce qui est vieux.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Anderson sur la panne de la FAA](2026-11-24-cio-anderson-faa-dette-technique-ia.md) (la fragilité vient d'un système hérité empilé et rapiécé) et le discours dominant qui assimile « legacy » à « à remplacer ».
- **Une distinction utile pour la rationalisation applicative** : séparer l'âge d'un système de son état de maintenance et de support, matériel, logiciel et stockage traités à part. La fiche Anderson pointait le sous-investissement ; celle-ci donne une grille pour le diagnostiquer.
- **Le support comme critère décisif** : « personne ne corrige un logiciel non supporté » ; un client a obtenu un correctif éditeur en quelques heures, IBM supporte encore DCF sorti en 1991, alors que Windows 10 (fin de support en octobre 2025) reste installé chez environ 25 % des utilisateurs Windows (StatCounter).
- **Le refus de remplacement préventif, payé cher** : l'entreprise de l'auteur a refusé de remplacer des disques après un déménagement de data center, pour raisons de coût et de coupure, et a subi les pannes.
- Pour le reste (courbe en baignoire, redondance), rien de neuf.

## 3. Résumé
L'auteur ouvre sur une panne à 3 h du matin : un sous-système disque fait tomber un mainframe IBM, pour la énième fois du mois. Il compare ensuite deux voitures : celle de son beau-père, souvent en panne, et la Land Rover bien entretenue de son oncle. Sur le matériel, il rappelle la courbe en baignoire (pannes précoces, période stable, hausse avec l'âge), cite Deutsche Bahn qui fait tourner un système sur un Windows non supporté depuis 2001 et la FAA qui admet des équipements de jusqu'à 50 ans, puis les cycles de support des constructeurs (Apple, IBM). Les remèdes : support externe, maintenance préventive, pièces de rechange, redondance. Sur le logiciel, les octets ne s'usent pas, mais l'environnement change : fin de Windows 10, retrait de produits par Broadcom, an 2000, dépréciation de TLS 1.0 et 1.1 ; un client a pu doubler la charge de ses applications COBOL grâce à des équipes internes compétentes, et IBM supporte toujours DCF. Sur le stockage, CD et bandes peuvent durer plus de 30 ans en bonnes conditions (Library of Congress, Fujifilm), disques et SSD lâchent entre 3 et 10 ans (Backblaze, SanDisk), ce que la redondance compense. Retour à la panne d'ouverture : après un déménagement de data center, les disques défaillaient, le constructeur recommandait de tout remplacer, l'entreprise a refusé pour des raisons de coût et en a payé le prix. Conclusion : un système hérité ne s'use pas, un système hérité mal maintenu, mal géré ou mal supporté, si.

## 4. Citations et noms
**Citations** :
- « Les systèmes hérités ne sont pas le problème. La négligence, si. » (« Legacy systems aren't the problem. Neglect is. »), David Stephens
- « Personne ne corrige un logiciel non supporté. » (« No one is fixing unsupported software. »), David Stephens
- « Les systèmes hérités ne s'usent pas. Ceux qui sont mal maintenus, mal gérés ou mal supportés, si. » (« Legacy systems don't wear out. Poorly maintained, managed or supported legacy systems do. »), David Stephens

**Noms cités** :
- *David Stephens, Longpela Expertise* : expert des mainframes IBM Z, auteur de la tribune.
- *Deutsche Bahn, FAA* : exemples d'organisations qui exploitent des systèmes très anciens.
- *IBM, Apple, Broadcom, Microsoft (Windows 10)* : exemples de cycles et de fins de support.
- *StatCounter* : source de la part de Windows 10 (environ 25 %).
- *Library of Congress, Fujifilm, Backblaze, SanDisk* : sources sur la durée de vie des supports de stockage.

## 5. Mots-clés
dette technique, rationalisation applicative, coût total de possession, qualité

## Lecture CPO
- **Implications** :
  - En revue de portefeuille, noter séparément l'âge d'une application et son état de support (éditeur, compétences internes, pièces), avant de décider remplacement ou maintien.
  - Budgéter la maintenance préventive des systèmes anciens comme une ligne visible, pas comme un reste du budget de run.
  - Intégrer les fins de support connues (systèmes, protocoles) au calendrier du portefeuille.
- **Fiabilité** : praticien expérimenté, consultant mainframe qui a intérêt à défendre le maintien des systèmes existants ; tribune fondée sur des anecdotes et des sources publiques, sans étude ni chiffre de coût.
- **Maturité** : Pratique établie : maintenance préventive et gestion des fins de support sont des classiques ; l'article les rappelle sans les renouveler.
- **Réutilisation** : citation d'ouverture pour un post LinkedIn ou une présentation client sur la rationalisation applicative (le legacy n'est pas un critère en soi), en complément de la fiche Anderson sur la FAA.
