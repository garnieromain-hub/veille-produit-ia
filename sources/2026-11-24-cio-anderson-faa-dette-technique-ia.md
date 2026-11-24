# The FAA outage is a warning about technical debt in the AI era

**Référence** : Edward Anderson (UT Austin, McCombs School of Business), CIO.com, 23 novembre 2026, tribune (rubrique Opinion), https://www.cio.com/article/4251637/the-faa-outage-is-a-warning-about-technical-debt-in-the-ai-era.html

**Axe** : Portefeuille numérique (IA appliquée au produit)

## 1. L'idée clé
La panne de la FAA du 13 novembre ne s'explique pas par la faute d'un seul fournisseur, mais par la fragilité d'un système hérité, empilé et rapiécé. Avec l'IA, on produit du logiciel plus vite que jamais ; sans investir à proportion pour comprendre, réparer et tester ce qui est dessous, la dette technique accumulée peut annuler les gains de productivité.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Roccaserra (OCTO) sur la qualité interne](2026-11-20-octo-roccaserra-qualite-interne-rythme-livraison.md) (la qualité soutient le rythme de livraison), la fiche [Nadella (Pragmatic Engineer)](2026-11-19-pragmatic-engineer-nadella-code-bon-marche.md) (le code devient bon marché, la vérification non) et la fiche [Pichler](2026-10-16-pichler-pm-product-builders.md) (la dette du code généré se paie plus tard).
- **Un incident d'infrastructure critique comme point de départ** : selon la FAA, un afflux de tentatives de connexion a déstabilisé des équipements anciens et perturbé communications et radars ; l'arrêt national des vols sert d'exemple concret, là où les fiches précédentes restaient au niveau des équipes logicielles.
- **Une recherche académique sur IA et dette technique** : avec Geoffrey Parker et Burcu Tan, entretiens et modèle de simulation dynamique ; les simulations suggèrent que la dette peut éroder les gains de productivité initiaux de l'IA, surtout sur du logiciel hérité, et l'intégration matérielle aggrave la difficulté. Aucun chiffre n'est donné dans la tribune.
- **Des recommandations de pilotage** : mesurer le coût d'exploitation, de modification et d'intégration plutôt que la vitesse de codage ; réserver des ressources au remboursement de la dette ; garder les ingénieurs expérimentés et documenter l'existant.
- Pour le reste, redite du discours connu sur la dette technique, avec une analogie (la maison des années 1970).

## 3. Résumé
L'auteur part de l'arrêt national des vols du 13 novembre : il ne faut pas tout imputer à un fournisseur, même si la responsabilité compte ; au 19 novembre, la cause exacte n'était pas établie. Les enquêteurs examinent un routeur Juniper Networks installé par le prestataire L3Harris ; selon la FAA, un afflux de connexions a déstabilisé des équipements anciens, et bloquer le trafic de deux sites a stabilisé le réseau. Il rapproche ce cas des difficultés de Chase le 16 novembre (un bug logiciel, avec des retards chez d'autres banques), en précisant que le rôle de la dette technique n'y est pas établi. Il définit la dette technique (raccourcis, composants rapiécés ou obsolètes, corrections repoussées) et l'illustre : une maison des années 1970 agrandie et recâblée, puis étendue par trente voisins avec des plans générés par l'IA, tout en précisant que l'IA n'est pas la cause de ces pannes. Il présente ensuite ses recherches avec Parker et Tan (code dupliqué, conflits de dépendances, composants obsolètes, décalages d'architecture ; gains initiaux de l'IA érodés par la dette). Il conclut sur quatre recommandations (mesurer le coût d'exploitation et de modification, financer la réduction de la dette, préserver les seniors et former les juniors à évaluer la production de l'IA, tester les interactions et les conditions de défaillance) : remplacer un composant n'est pas renforcer un système.

## 4. Citations et noms
**Citations** :
- « Nous pouvons générer du logiciel plus vite que jamais. » (« We can generate software faster than ever. »), Edward Anderson

**Noms cités** :
- *Edward Anderson* : professeur de gestion de l'information, du risque et des opérations à UT Austin (McCombs), auteur.
- *Geoffrey Parker et Burcu Tan* : coauteurs de la recherche sur IA et dette technique (publiée via MIT Sloan Management Review et SSRN).
- *FAA* : autorité américaine de l'aviation, panne du 13 novembre.
- *Juniper Networks et L3Harris* : fabricant du routeur examiné et prestataire qui l'a installé.
- *Chase* : banque touchée par un bug le 16 novembre, exemple de dépendance entre systèmes.
- *Dette technique* : coût accumulé des raccourcis et corrections repoussées, cœur du propos.

## 5. Mots-clés
dette technique, qualité, mesure de l'impact, vérification, talents juniors

## Lecture CPO
- **Implications** :
  - Dans les arbitrages de portefeuille, réserver explicitement une part du budget à la réduction de la dette et à la documentation des systèmes hérités, surtout là où l'IA accélère la production de code.
  - Mesurer la productivité de l'IA au coût d'exploitation et de modification, pas au volume de code livré.
  - Tester les interactions et les défaillances entre composants (un équipement anormal peut-il faire tomber les autres ?) dans les produits qui dépendent d'infrastructures anciennes.
  - Garder les profils seniors qui connaissent l'existant et former les juniors à évaluer le code généré.
- **Fiabilité** : universitaire, sans intérêt commercial apparent ; la tribune présente ses propres recherches sans en donner les chiffres. Les faits sur la FAA renvoient à la FAA, au WSJ et à Investing.com ; la cause de la panne n'était pas établie à la date d'écriture, et le lien avec l'IA est présenté comme une illustration, non comme une cause.
- **Maturité** : Pratique établie : le pilotage de la dette technique est connu ; l'apport est de le relier à l'accélération par l'IA, avec une recherche encore peu chiffrée.
- **Réutilisation** : article OCTO sur la dette technique à l'ère du code généré (à croiser avec Roccaserra) ; présentation client DSI sur la mesure de la productivité IA ; post LinkedIn « remplacer un composant n'est pas renforcer un système ».
