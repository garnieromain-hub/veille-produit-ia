# Stratégie cloud du secteur public, la souveraineté choisie usage par usage

**Référence** : Mourad Krim, IT Social, 24 novembre 2026, article d'analyse autour du baromètre Ifop pour Numspot (en partenariat avec Acteurs Publics), https://itsocial.fr/cloud-infrastructure-it/cloud-infrastructure-it-articles/strategie-cloud-du-secteur-public-la-souverainete-choisie-usage-par-usage/

**Axe** : Investissement tech (Portefeuille numérique)

**Avertissement** : le baromètre est commandé par Numspot, fournisseur de cloud souverain qui vend précisément à ce public. L'article le signale lui-même et en discute les limites.

## 1. L'idée clé
Le secteur public français ne se demande plus s'il faut aller dans le cloud, mais quels usages il veut souverains : trois organisations sur quatre ont une stratégie arrêtée, et les services aux usagers et l'IA générative passent en tête des usages à protéger. Le passage à l'acte reste freiné par un surcoût de 25 à 40 % et une offre qualifiée encore étroite, que les DSI doivent budgéter dès maintenant.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Reuters via Le Monde Informatique sur le cloud souverain européen](2026-11-24-lmi-reuters-cloud-souverain-europe.md) (la souveraineté entre dans les achats, mais les hyperscalers gardent plus de 70 % du marché) et la fiche [JDN sur les inférenceurs souverains](2026-11-20-jdn-comparatif-inferenceurs-souverains.md) (Cloud Temple, seul qualifié SecNumCloud, systématiquement le plus cher).
- **L'IA générative devient un usage souverain prioritaire** : 59 % des répondants veulent l'héberger en souverain (38 % en 2025), la plus forte hausse du baromètre. Les fiches précédentes parlaient de la souveraineté de l'infrastructure en général, pas de l'IA comme motif.
- **Une souveraineté sélective, pas globale** : priorités chiffrées par usage (services aux citoyens 61 %, IA générative 59 %, PRA/PCA 52 %, conformité 38 %, hybridation du SI 21 %). C'est une logique de portefeuille d'usages plutôt qu'un choix de fournisseur unique.
- **Le surcoût chiffré par la Cour des comptes** : 25 à 40 % pour une infrastructure SecNumCloud, et seulement environ 55 M€ reçus par le cloud interne Nubo en neuf ans pour environ 3 Md€ de dépense numérique annuelle de l'État. Le JDN donnait des écarts de prix entre fournisseurs, pas un ordre de grandeur budgétaire.
- **Le cadre réglementaire français** : décret du 14 avril 2026 (article 31 de la loi SREN) qui impose un prestataire qualifié pour les données sensibles de l'État et de certains opérateurs, mais pas pour les collectivités.

## 3. Résumé
L'article ouvre sur un changement de question : les organisations publiques « arrêtent leur stratégie cloud et désignent les usages qu'elles veulent souverains ». Il s'appuie sur le baromètre Ifop pour Numspot, avec Acteurs Publics, présenté au Salon des maires le 19 novembre 2026 (195 agents interrogés en ligne du 17 mars au 11 juin 2026 ; 257 agents du numérique en 2025). 73 % des organisations ont une stratégie cloud (27 % n'en ont pas, contre 34 % en 2025) ; l'hybride domine (34 %), devant le cloud public seul (20 %) et le cloud privé seul (16 %). 47 % des répondants utilisent du cloud souverain pour au moins la moitié de leurs usages cloud (39 % en 2025). Viennent les usages prioritaires, avec l'IA générative en plus forte hausse (59 % contre 38 %). L'auteur prend ensuite ses distances : échantillons différents d'une année sur l'autre, tirés du fichier d'Acteurs Publics, répartition État, collectivités et hôpitaux non publiée, préférences déclarées et non achats, commanditaire acteur du marché (Numspot, détenu par la Banque des Territoires, Docaposte, Dassault Systèmes et Bouygues Telecom, IaaS qualifié SecNumCloud le 1er septembre 2026, après la fin de l'enquête, PaaS encore en cours de qualification). Il oppose à l'intention les freins d'exécution relevés par la Cour des comptes le 31 octobre 2025 : faible adoption des clouds internes Nubo et Pi, surcoût de 25 à 40 %, recommandation de cartographier les données sensibles en 2026. Il rappelle le décret du 14 avril 2026. Conclusion pour les DSI : inscrire le surcoût dès la préparation budgétaire, cartographier les données, négocier la réversibilité et vérifier, service par service, ce que couvre la qualification pour les usages d'IA.

## 4. Citations et noms
**Citations** :
- « Les organisations publiques ne raisonnent plus seulement en termes d'adoption du cloud », Éric Haddad, directeur général de Numspot
- « Les DSI ont à inscrire le surcoût de 25 à 40 % dès la préparation budgétaire des projets concernés », Mourad Krim

**Noms cités** :
- *Numspot* : commanditaire du baromètre et fournisseur de cloud souverain (IaaS qualifié SecNumCloud depuis le 1er septembre 2026).
- *Éric Haddad* : directeur général de Numspot, seule personne citée.
- *Ifop* : institut qui a réalisé l'enquête.
- *Acteurs Publics* : média partenaire, dont le fichier de contacts sert de base à l'échantillon.
- *Banque des Territoires, Docaposte, Dassault Systèmes, Bouygues Telecom* : actionnaires de Numspot.
- *Cour des comptes* : rapport du 31 octobre 2025, source du surcoût de 25 à 40 % et du bilan de Nubo et Pi.
- *Nubo et Pi* : clouds internes de l'État, peu adoptés.
- *SecNumCloud* : qualification de l'ANSSI exigée pour les données sensibles.
- *Loi SREN (article 31) et décret du 14 avril 2026* : obligation d'hébergement qualifié pour les données sensibles de l'État.

## 5. Mots-clés
souveraineté, budgets IT, réversibilité, achats IT, réglementation, enquête

## Lecture CPO
- **Implications** :
  - Pour un CPO ou un DSI public : décider la souveraineté usage par usage (services aux usagers, IA générative, PRA) plutôt que pour tout le SI, et l'inscrire dans la feuille de route produit.
  - Prévoir dans les business cases des produits IA publics un surcoût d'hébergement qualifié de 25 à 40 %.
  - Vérifier ce que couvre réellement une qualification : IaaS qualifié ne veut pas dire PaaS ou service d'IA qualifié.
  - Négocier la réversibilité dès le contrat, en lien avec la fiche Reuters (migrations de 12 à 24 mois).
- **Fiabilité** : baromètre commandé par un vendeur de cloud souverain, sur un petit échantillon (195) non représentatif et différent de celui de 2025 ; les évolutions d'une année sur l'autre sont donc fragiles. Le mérite de l'article est de le dire et de croiser avec la Cour des comptes, source indépendante.
- **Maturité** : Tendance émergente : l'intention de souveraineté progresse et l'IA générative devient un motif, mais les achats effectifs ne sont pas mesurés et les freins de coût restent entiers.
- **Réutilisation** : présentation client secteur public sur l'arbitrage souverain usage par usage ; post LinkedIn « l'IA générative, nouvel usage souverain prioritaire du public, à condition d'en payer le surcoût » (en citant le commanditaire) ; matière pour un article OCTO sur la gestion de portefeuille appliquée à la souveraineté.
