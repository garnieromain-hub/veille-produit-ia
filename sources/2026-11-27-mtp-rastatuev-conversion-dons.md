# How to fix your conversion: Three lessons from a fundraising app experiment

**Référence** : Alex Rastatuev (product manager SaaS B2B et B2C, six ans d'expérience), Mind the Product, 26 novembre 2026, retour d'expérience, https://www.mindtheproduct.com/how-to-fix-your-conversion-three-lessons-from-a-fundraising-app-experiment

**Axe** : Product management

## 1. L'idée clé
La finance, le e-commerce et la philanthropie partagent les mêmes problèmes de conversion (confiance, friction, coûts, moyens de paiement, abandons). Une série d'expériences sur une plateforme de dons montre qu'une hypothèse précise, l'attention aux préférences des utilisateurs plutôt qu'aux fonctionnalités, et des idées empruntées à d'autres secteurs permettent de réparer un tunnel, même quand les résultats déçoivent.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Pariy sur la marketplace à rachat instantané](2026-11-25-mtp-pariy-marketplace-risque-prix.md) (même média, retour d'expérience chiffré) et le discours dominant sur l'A/B testing (formuler une hypothèse, mesurer, itérer). Les trois leçons finales sont une redite de ce discours ; l'apport tient aux résultats chiffrés des expériences :
- **La relance d'abandon fonctionne pour les dons** : proposer « Want a reminder later? » puis relancer à 1, 3 et 7 jours convertit 10 % des destinataires, le double de l'objectif, sans baisse de l'ARPU, sur plus de 100 000 visiteurs en 52 jours.
- **Simplifier peut détruire la conversion** : dans l'e-mail de reçu, le bouton unique fait baisser la conversion de l'offre de 44,36 %, alors que deux montants plus un montant libre augmentent le don moyen de 6,19 %, sans effet significatif sur la conversion récurrente.
- **Le moyen de paiement préféré pèse** : Google Pay augmente la conversion de 2,6 % (4 % sur Chrome), Apple Pay de 2 %.
- **Une option à forte valeur peut échouer par la friction** : le don en actions (environ 5 000 $ contre 150 $ pour un don en ligne moyen) n'est utilisé que par 0,15 % des dons, car il ajoute des étapes.

## 3. Résumé
L'auteur part du constat que finance, e-commerce et philanthropie butent sur les mêmes freins de conversion. Les expériences ont été menées chez Fundraise Up, plateforme de dons utilisée notamment par UNICEF, Rainforest Trust et WHO Foundation. Première expérience : récupérer les dons abandonnés en proposant un rappel, puis des e-mails à 1, 3 et 7 jours (52 jours, plus de 100 000 visiteurs, test et contrôle à 50/50) ; objectif 5 % de conversion des personnes ayant accepté, résultat 10 %, ARPU préservé. Deuxième : proposer un don récurrent dans l'e-mail de reçu à environ 200 000 donateurs ponctuels anglophones (44 jours), en trois variantes ; objectif +1,5 % de conversion récurrente ; résultat sans effet significatif, mais don moyen +6,19 % avec deux montants et un montant libre, et −44,36 % de conversion de l'offre avec le bouton unique. Troisième volet : les moyens de paiement. L'auteur cite Baymard (13 % d'abandons faute du moyen préféré, 10 % pour options limitées) et la répartition 2021 des dons (cartes 65 %, PayPal 25 %, Apple Pay 6 %, Google Pay 3 %) ; Google Pay et Apple Pay augmentent la conversion de 2,6 % et 2 %. Quatrième : le don en actions pour les donateurs américains, motivé par l'avantage fiscal (36 jours, plus de 50 000 visiteurs, 80/20) ; 0,45 % de clic, 0,15 % des dons, 0,7 % du montant total, car le parcours se complique. Conclusion en trois leçons : une hypothèse solide, les préférences autant que les fonctionnalités, les idées venues d'ailleurs. L'auteur invite les PM à repérer les points d'abandon de leur tunnel, à emprunter une tactique à un autre secteur et à la tester avec une hypothèse et une métrique de succès claires.

## 4. Citations et noms
**Citations** :
- « Une hypothèse solide oblige à penser l'expérience avant de la construire. » (« A strong hypothesis forces you to think through the experiment before building it »), Alex Rastatuev
- « Les préférences des utilisateurs comptent autant que la fonctionnalité. » (« Users' preferences matter just as much as functionality »), Alex Rastatuev
- « Les bonnes idées produit ne viennent pas forcément de votre propre secteur. » (« Good product ideas don't have to come from within your own industry. »), Alex Rastatuev

**Noms cités** :
- *Fundraise Up* : plateforme de dons en ligne où les expériences ont été menées.
- *UNICEF, Rainforest Trust, WHO Foundation* : organisations clientes de la plateforme.
- *Baymard* : institut d'études UX cité pour les abandons liés aux moyens de paiement.
- *Google Pay, Apple Pay, PayPal* : moyens de paiement testés ou mesurés.
- *ARPU* : revenu moyen par utilisateur, garde-fou des expériences.

## 5. Mots-clés
expérimentation, conversion, friction, discovery, mesure de la valeur

## Lecture CPO
- **Implications** :
  - Fixer pour chaque test une métrique de succès et une métrique garde-fou (ici l'ARPU), et prévoir ce qu'on apprendra de chaque issue.
  - Se méfier de la simplification à outrance : retirer le choix (bouton unique) a fait chuter la conversion.
  - Mesurer l'effet des moyens de paiement comme une fonctionnalité à part entière du tunnel.
  - Évaluer une option à forte valeur unitaire sur le coût de friction qu'elle ajoute, pas seulement sur sa valeur.
- **Fiabilité** : praticien produit, sur des expériences internes à une plateforme ; volumes et durées donnés, mais pas les intervalles de confiance ; certains chiffres (paiement, 2021) non datés précisément ; l'article reste en partie une vitrine de la plateforme.
- **Maturité** : Pratique établie : l'expérimentation par hypothèse est connue, l'article en donne des cas chiffrés.
- **Réutilisation** : formation ou atelier discovery (exemple chiffré d'hypothèse et de garde-fou) ; post LinkedIn « Le bouton unique qui a fait perdre 44 % de conversion ».
