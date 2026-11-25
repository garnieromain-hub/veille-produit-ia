# Mathieu Wellhoff (ADEME) : « Vous répétez sans cesse que l'IA va sauver la planète… Alors donnez-moi des cas d'usage ! »

**Référence** : Laurent Delattre, IT for Business, 24 novembre 2026, entretien filmé sur le plateau d'IT for Business au Tech Show Paris (18-19 novembre 2026) et article de restitution, https://www.itforbusiness.fr/ademe-ia-generative-sobriete-numerique-110302

**Axe** : Investissement tech (Transformation des entreprises)

## 1. L'idée clé
L'IA générative change l'échelle de l'empreinte du numérique, et ses bénéfices environnementaux restent à démontrer : Wellhoff dit ne connaître qu'une poignée de projets d'IA générative qui réduisent vraiment les émissions. Il demande donc aux DSI de vérifier si l'usage est nécessaire et de choisir la plus petite taille de modèle suffisante, d'autant que l'IA n'est pas aujourd'hui facturée à son coût réel et que l'énergie finira par se retrouver dans les factures.

## 2. Ce qui est nouveau
**Par rapport à** : les fiches [IT Social, jetons moins chers et facture plus salée](2026-11-24-itsocial-jetons-moins-chers-facture-ia.md) et [Elée, métriques de facturation de l'IA](2026-11-24-itforbusiness-metriques-facturation-ia-dsi.md), qui abordent le coût de l'IA sous l'angle de la tarification et du FinOps, et la fiche [Gartner, dépenses IT 2027](2026-11-13-gartner-depenses-it-2027.md) ; plus largement, le discours des éditeurs et des hyperscalers selon lequel l'IA aidera à décarboner l'économie.
- **Une demande de preuve, venue d'un organisme public** : l'ADEME retourne la charge de la preuve vers les promoteurs de l'IA « qui sauve la planète ». Selon Wellhoff, Google et AWS, qu'il a interrogés, n'ont pas pu lui donner de cas d'usage d'IA générative probants. C'est un témoignage, pas une étude.
- **« Il y a IA et IA »** : l'IA classique et le big data produisent des gains d'efficacité réels mais modestes, à corriger des effets rebond ; l'IA générative est jugée beaucoup moins convaincante. Les fiches précédentes ne faisaient pas cette distinction.
- **Le coût caché comme futur risque budgétaire** : les offres d'IA générative ne sont pas facturées à leur coût réel, et l'énergie devrait finir par apparaître dans les factures. C'est le même constat que celui des fiches sur la tarification, mais avec l'argument énergétique plutôt que l'argument financier.
- **Les petits modèles spécialisés, argument à la fois environnemental et de souveraineté** : le modèle européen de petits modèles est présenté comme pertinent sur les deux plans, même si Wellhoff reconnaît que la démonstration environnementale reste difficile.

## 3. Résumé
L'entretien part d'un rappel : « le numérique n'a rien de virtuel », et l'IA générative change l'échelle du sujet car elle exige beaucoup de calcul et d'énergie. Wellhoff juge théoriques les promesses nucléaires des hyperscalers (fusion, petits réacteurs modulaires) : au mieux dans dix ans, alors que les data centers croissent tout de suite. Il distingue ensuite deux IA. L'IA classique et le big data améliorent l'efficacité de l'industrie et des transports, avec des gains modestes et des effets rebond à prendre en compte. Pour l'IA générative, il ne compte que peu de projets efficaces pour réduire les émissions (« sur les doigts d'une main ») et dit avoir posé la question à Google et à AWS, sans réponse convaincante. D'où son conseil aux DSI : se demander si l'usage est nécessaire et dimensionner le modèle au besoin. Il défend les petits modèles spécialisés à l'européenne, pour des raisons de souveraineté (données hors des États-Unis) autant qu'environnementales. Il ajoute que les solutions d'IA générative ne sont pas vendues à leur coût réel et que l'énergie devrait finir par apparaître dans les factures. Le journaliste conclut que la sobriété pourrait devenir une contrainte budgétaire au moment où les budgets 2027 prévoient une hausse des dépenses d'IA, et que le numérique responsable pourrait redevenir un critère de choix, comme la souveraineté. L'article ne contient aucun chiffre.

## 4. Citations et noms
**Citations** :
- « Le numérique n'a rien de virtuel. », Mathieu Wellhoff, ADEME
- « Vous répétez sans cesse que l'IA va sauver la planète… Alors donnez-moi des cas d'usage ! », Mathieu Wellhoff, ADEME
- « Il y a IA et IA. », intertitre de l'article

**Noms cités** :
- *Mathieu Wellhoff* : responsable de la sobriété numérique à l'ADEME, l'invité.
- *ADEME* : agence de la transition écologique, organisme public.
- *Laurent Delattre* : journaliste d'IT for Business, auteur et intervieweur.
- *Google, AWS* : hyperscalers interrogés par Wellhoff, qui ne lui auraient pas fourni de cas d'usage probants.
- *Hyperscalers* : cités pour leurs projets nucléaires (fusion, petits réacteurs modulaires) jugés lointains.
- *Tech Show Paris 2026* : salon où l'entretien a été enregistré.

## 5. Mots-clés
sobriété numérique, infrastructure IA, petits modèles, souveraineté, budgets IT, mesure du ROI

## Lecture CPO
- **Implications** :
  - Ajouter au business case d'un produit IA une question explicite : l'IA générative est-elle nécessaire, ou un modèle plus petit, une IA classique ou une règle suffisent-ils ?
  - Faire du dimensionnement du modèle (taille, routage) un choix de conception documenté, qui sert à la fois le coût, la souveraineté et l'empreinte.
  - Anticiper dans le pilotage budgétaire une hausse du prix réel de l'inférence, et ne pas bâtir de rentabilité sur les prix actuels.
  - Pour les DSI et comex : se préparer à ce que le numérique responsable redevienne un critère d'achat et de reporting.
- **Fiabilité** : un responsable d'organisme public, sans produit à vendre, mais avec une mission de sobriété. Propos oraux, aucun chiffre ni étude cités ; l'échange avec Google et AWS n'est rapporté que par lui. La conclusion budgétaire est celle du journaliste.
- **Maturité** : Signal faible : l'argument environnemental reste marginal dans les arbitrages IA, mais il rejoint le débat déjà vif sur le coût réel de l'inférence.
- **Réutilisation** : post LinkedIn « L'ADEME demande des cas d'usage » ; table ronde DSI sur le coût réel de l'IA, à croiser avec les fiches sur la tarification et le FinOps ; présentation client sur le dimensionnement des modèles (petits modèles, routage).
