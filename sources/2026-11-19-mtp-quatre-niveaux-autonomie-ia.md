# Using the Four Levels of AI autonomy to decide where AI fits into your product

**Référence** : Lucy Pitticas-Rothwell (Head of Product Operations, FreeAgent), Mind the Product, 17 novembre 2026, article de méthode, https://www.mindtheproduct.com/using-the-four-levels-of-ai-autonomy-to-decide-where-ai-fits-into-your-product/

**Axe** : IA appliquée au produit (Product management)

## 1. L'idée clé
Pour savoir où mettre de l'IA dans un produit, il faut croiser trois choses : les jobs to be done des utilisateurs, un niveau d'autonomie de l'IA (de 0 à 4) et le coût de l'erreur. Plus l'erreur coûte cher, moins l'autonomie est possible.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Torres sur les evals](2026-10-16-torres-ai-evals-habitude-discovery.md) (comment mesurer la qualité d'un produit IA) et le discours dominant des éditeurs sur l'agent autonome (Microsoft présente cette semaine un agent « actif en permanence » qui agit sans instruction).
- **Une grille de décision produit, pas technique** : l'autonomie se décide tâche par tâche à partir du coût de l'erreur pour l'utilisateur, et non à partir de ce que le modèle sait faire.
- **Le niveau 4 n'est pas une cible** : l'auteure le juge trop risqué pour beaucoup de tâches (personne ne veut qu'une IA souscrive un prêt à sa place), à rebours de la course à l'autonomie.
- **Un usage de product ops** : l'article vient d'une responsable product operations qui en fait un outil d'atelier (gabarit en annexe), pas un pronostic.

## 3. Résumé
L'auteure part d'une question : où l'IA peut-elle vraiment améliorer l'expérience client ? Elle propose de lister les jobs to be done, puis de situer chaque tâche sur quatre niveaux d'autonomie : 0, pas ou peu d'IA ; 1, l'humain valide chaque sortie ; 2, la confiance est plus élevée grâce à d'autres sources de données et l'humain ne valide qu'une minorité de sorties ; 3, l'IA agit, y compris sur d'autres systèmes et en plusieurs étapes, l'humain restant impliqué dans les validations ; 4, l'humain configure puis n'intervient presque plus. Elle introduit ensuite le coût de l'erreur comme limite : plus il est élevé, plus l'autonomie doit rester basse. Elle l'illustre avec une néobanque pour petites entreprises : obtenir un prêt passe du niveau 0 au niveau 3, mais pas au niveau 4 ; payer une facture passe aussi au niveau 3 grâce à l'extraction de texte des documents et à la mise en place automatique des paiements. Conclusion : partout où une tâche peut être améliorée en la confiant à une IA, elle devrait l'être, dans la limite fixée par le coût de l'erreur. Les annexes (caractéristiques détaillées des niveaux, gabarit) sont des images non lues. Aucun chiffre.

## 4. Citations et noms
**Citations** :
- « En général, un coût de l'erreur plus élevé signifie que moins d'autonomie est possible. » (« Generally, a higher cost of error will mean less autonomy is possible. »), Lucy Pitticas-Rothwell
- « Où, dans le produit, l'IA peut-elle réellement améliorer l'expérience client ? » (« Where in the product can AI actually improve customer experience? »), Lucy Pitticas-Rothwell

**Noms cités** :
- *FreeAgent* : éditeur de logiciel comptable basé à Édimbourg, employeur de l'auteure.
- *Jobs to be done* : cadre de départ pour lister les tâches utilisateur.
- *Quatre niveaux d'autonomie de l'IA* : échelle de 0 à 4 utilisée comme grille.

## 5. Mots-clés
conception de produits IA, autonomie des agents, discovery, gouvernance IA

## Lecture CPO
- **Implications** :
  - Utiliser la grille en atelier de discovery pour chaque parcours : tâche, niveau d'autonomie visé, coût de l'erreur, mode de validation.
  - Fixer un plafond d'autonomie par tâche dans la gouvernance produit, au lieu d'un principe général « humain dans la boucle » (que Thoughtworks qualifie de théâtre quand l'humain ne peut pas juger).
  - Rattacher le niveau d'autonomie aux evals : on ne monte d'un niveau que si la qualité mesurée le permet.
- **Fiabilité** : praticienne, responsable product ops dans un éditeur, sans intérêt commercial direct dans la grille ; texte de méthode sans données ni retour chiffré ; le cadre des « quatre niveaux » n'est pas attribué à une source précise dans la partie lue.
- **Maturité** : Signal faible : une grille utile et simple, mais présentée sans retour d'usage mesuré.
- **Réutilisation** : présentation client (grille autonomie / coût de l'erreur pour prioriser les cas d'usage IA) ; atelier OCTO School of Product ; post LinkedIn (« Le niveau 4 d'autonomie n'est pas une cible »).
