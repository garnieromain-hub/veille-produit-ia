# Qualité interne et ralentissement du rythme de livraison : pourquoi le code se dégrade et comment l'éviter

**Référence** : Sébastien Roccaserra, OCTO Talks !, 20 novembre 2026, billet de blog, https://blog.octo.com/qualite-interne-et-rythme-de-livraison--pourquoi-le-code-se-degrade-et-comment-l'eviter

**Axe** : Product management

## 1. L'idée clé
Si un changement qui prenait deux jours en prend désormais deux semaines, c'est que la qualité interne du code s'est dégradée sans bruit, parce que les fonctionnalités se voient et se priorisent, et pas la qualité. La vélocité dépend de l'état du code, de la vitesse des boucles de feedback et de la charge absorbée : il faut traiter la qualité interne comme une partie du flux, pas comme un chantier à rattraper.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Ploquin, Lean, IA et Delivery](2026-11-19-octo-ploquin-lean-ia-delivery.md) (l'IA amplifie les bonnes pratiques comme les défauts) et le discours dominant de l'ingénierie logicielle (Fowler, Beck, DORA), que le billet reprend explicitement.
- **Rien de neuf sur le fond par rapport aux références qu'il cite (Fowler, Rainsberger, Beck, DORA, loi de Brooks)** ; l'article ne parle pas d'IA. Seuls apports :
- **L'image de la cuisine et du garage** : une cuisine se range au fil de l'eau, un garage s'accumule puis se vide sous pression. C'est une image simple pour expliquer la dette à un sponsor non technique.
- **La « sur-capacité silencieuse »** : une part croissante de l'énergie part dans les contournements et le travail non prévu, que le backlog ne montre pas. Cela explique pourquoi la vélocité baisse sans que le plan change.
- **Une liste de leviers côté produit et management** : qualité interne dans la définition du « done », réduction du WIP, nettoyage du backlog, refus d'augmenter la pression sur la vélocité, prudence sur les mesures (loi de Goodhart) et sur le calcul de ROI de la qualité.

## 3. Résumé
Le billet part d'un étonnement fréquent : un changement comparable à un autre prend désormais deux semaines au lieu de deux jours. L'auteur explique que la dégradation du code est invisible et se paie avec retard, alors que les fonctionnalités sont visibles et priorisées. S'appuyant sur Martin Fowler, il montre que sans refactoring le design se dégrade de façon cumulative ; J. B. Rainsberger y voit un enjeu de coût, le refactoring réduisant la volatilité du coût marginal des fonctionnalités. Il oppose la cuisine (rangée au fil de l'eau) au garage (rangé sous pression), et précise que « Do the right thing, do the thing right » ne veut pas dire reporter la qualité, mais alterner vite entre faire marcher et améliorer, comme en TDD. Il nomme trois activités invisibles : limiter la dégradation du design, ne pas casser l'existant (tests automatisés), faciliter l'extension (solution la plus simple, options ouvertes selon Kent Beck). Il plaide pour accélérer le feedback plutôt que le développement : quand les boucles s'allongent, l'agilité disparaît même si le vocabulaire reste. Il décrit la sur-capacité silencieuse et rappelle la loi de Brooks. Il propose ensuite des leviers d'équipe (qualité dans le « done » sans « gate keeper », pratiques alignées, petits lots selon DORA, rendre la dégradation visible, prudence sur les métriques, demander à l'équipe ce dont elle a besoin) et des moyens d'éviter la surchauffe (faire moins, réduire le WIP, purger le backlog, ne pas pousser la vélocité). Il conclut que l'arbitrage entre améliorations et fonctionnalités se fait en continu, avec des canaux de communication ouverts.

## 4. Citations et noms
**Citations** :
- « Stop starting, start finishing », formule reprise pour réduire le travail en cours
- « Do the right thing, do the thing right », adage dont l'auteur corrige la lecture (ne pas reporter la qualité)

**Noms cités** :
- *Martin Fowler* : *Refactoring* (2e édition), sur la dégradation du design sans refactoring.
- *J. B. Rainsberger* : « The Eternal Struggle Between Business and Programmers », le refactoring comme stabilisation du coût marginal.
- *Kent Beck* : *Tidy First*, notion de conserver des options.
- *DORA* : capacité « Working in Small Batches ».
- *Loi de Brooks, loi de Goodhart* : limites de l'ajout de personnes et des mesures.
- *Étienne Girot, Christophe Thibaut* : auteurs OCTO cités sur le ROI de la qualité et la dette technique.
- *Todd Conklin* : « The New View of Safety », demander à l'équipe ce dont elle a besoin.

## 5. Mots-clés
dette technique, qualité, vélocité, boucles de feedback, lean

## Lecture CPO
- **Implications** :
  - Mettre la qualité interne dans la définition du « done » et dans les arbitrages du PO, plutôt que dans un chantier « dette » à négocier plus tard.
  - Lire une baisse de vélocité comme un signal sur l'état du code et la charge non prévue, pas comme un problème d'effort : ne pas répondre par plus de pression ou plus de monde.
  - Réduire le WIP et purger le backlog comme leviers produit directs.
  - Se méfier d'un tableau de bord de dette technique pris comme objectif (loi de Goodhart).
- **Fiabilité** : praticien OCTO, qui défend des pratiques que le cabinet vend en accompagnement ; aucun chiffre, argumentation fondée sur des références reconnues et l'expérience de terrain.
- **Maturité** : Pratique établie : refactoring, TDD, petits lots et limitation du WIP sont documentés depuis vingt ans.
- **Réutilisation** : post LinkedIn (« Votre code est un garage, pas une cuisine ») ; présentation client auprès d'un sponsor métier qui ne comprend pas pourquoi l'équipe ralentit ; article OCTO qui relierait ce billet à l'IA (le code généré accélère le remplissage du garage), en s'appuyant sur la fiche Ploquin.
