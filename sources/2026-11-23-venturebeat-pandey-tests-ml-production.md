# Your ML model passed every test. Here's what those tests might have missed

**Référence** : Karmendra Pandey (Practice Architect en IA et ML), VentureBeat, 22 novembre 2026, tribune, https://venturebeat.com/orchestration/your-ml-model-passed-every-test-heres-what-those-tests-might-have-missed

**Axe** : IA appliquée au produit

## 1. L'idée clé
Un modèle de machine learning qui réussit tous ses tests sur des données propres peut se dégrader en silence en production. Six vérifications, transformées en barrières de mise en production avec un responsable nommé, suffisent à l'éviter : ce n'est que de la discipline d'ingénierie appliquée à des systèmes qui apprennent.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Torres sur les evals](2026-10-16-torres-ai-evals-habitude-discovery.md) (les evals comme habitude de discovery pour les équipes produit) et le discours établi du MLOps (fuite de données, dérive, déploiement canari sont connus depuis des années).
Redite des bonnes pratiques MLOps ; seuls apports :
- **Une liste de contrôle compacte, avec un responsable par barrière** : six barrières (fuite de données, métriques par segment, calibration, cas limites, plan de dérive, déploiement progressif), chacune avec un critère réussi ou échoué, sur une page. C'est un format directement reprenable dans une définition de « prêt à livrer ».
- **Les métriques par segment comme critère de mise en production** : un modèle à 94 % de précision globale peut tomber à 61 % sur un segment clé du chiffre d'affaires ; une dégradation sur un segment bloque la livraison même si la moyenne est stable. Cela rejoint directement les choix produit (quels segments comptent).
- **« Pas de plan de dérive, pas de livraison »** : la question « saura-t-on quand il ne marche plus ? » est posée avant la mise en production, avec un responsable des alertes.

## 3. Résumé
L'auteur part d'un constat : la plupart des modèles sont testés sur des données propres et familières, puis échouent sur les entrées désordonnées de la production, sans que personne ne le voie. Les équipes qui évitent ce piège appliquent six vérifications avant chaque déploiement, puis en continu.
1. Tester sur des données vraiment inédites : la fuite vient des doublons, des quasi-doublons, du chevauchement temporel ou d'un prétraitement fait avant la séparation des jeux ; exiger un audit de fuite.
2. Découper les métriques : la moyenne masque les échecs (94 % au global, 61 % sur un segment critique) ; l'évaluation par segment (période, source, segment client) devient une barrière.
3. Vérifier la calibration : le renvoi des cas incertains vers un humain ne marche que si la confiance du modèle correspond à sa précision, ce qui se dégrade souvent après un affinage ou un changement de distribution.
4. Sonder les cas limites : une suite hostile de quelques centaines d'exemples écrits par ceux qui savent où le système casse (argot, nouvelles catégories, erreurs d'OCR), enrichie à chaque incident.
5. Prévoir la dérive dès le premier jour : métriques sur les entrées, les prédictions et les indicateurs métier, seuils d'alerte, responsable nommé.
6. Livrer derrière une barrière : mode fantôme, puis canari avec retour arrière automatique ; un retour arrière doit être testé (l'auteur cite une équipe dont le retour « instantané » a pris 40 minutes et trois validations).
Il conclut en intégrant chaque vérification au pipeline (audit de fuite et métriques par segment en intégration continue, calibration et cas limites bloquant la promotion, tableaux de dérive et analyse canari pendant le déploiement), avec un audit d'une page et six barrières.

## 4. Citations et noms
**Citations** :
- « Sans réponses claires, vous n'avez pas de jeu d'évaluation, vous avez un espoir. » (« you do not have an eval set; you have a hope »), Karmendra Pandey
- « Pas de plan de dérive, pas de livraison. » (« No drift plan, no ship. »), Karmendra Pandey
- La validation avant livraison relève de la « discipline d'ingénierie de base, appliquée à des systèmes qui se trouvent apprendre » (« basic engineering discipline, applied to systems that happen to learn »), Karmendra Pandey

**Noms cités** :
- *Diagramme de fiabilité, erreur de calibration attendue (ECE)* : outils proposés pour mesurer la calibration.
- *Mode fantôme (shadow mode), déploiement canari* : méthodes de mise en production progressive.

## 5. Mots-clés
evals, qualité, dérive des modèles, mise en production, conception de produits IA

## Lecture CPO
- **Implications** :
  - Le PM doit choisir les segments sur lesquels un modèle ne peut pas régresser : c'est une décision produit, à inscrire dans les critères de mise en production.
  - Ajouter à la définition de « prêt à livrer » d'une fonctionnalité IA un plan de dérive avec un responsable nommé et un retour arrière testé.
  - Faire du recueil des incidents de production une source d'exemples pour la suite de cas limites, en lien avec les evals de discovery (Torres).
- **Fiabilité** : tribune d'un architecte praticien, sans intérêt commercial affiché ; chiffres illustratifs (94 % contre 61 %, retour arrière de 40 minutes) non sourcés ; contenu de bonnes pratiques connues, sans étude à l'appui.
- **Maturité** : Pratique établie : ce sont des pratiques MLOps reconnues, ici rassemblées en liste de contrôle.
- **Réutilisation** : support de formation ou d'atelier OCTO sur la mise en production de fonctionnalités IA (les six barrières) ; post LinkedIn (« 94 % en moyenne, 61 % sur vos meilleurs clients »). Apport limité pour un article de fond.
