# Fable 5.2, Opus 5.5, Sonnet 5.5, Haiku 5.5 : quel modèle Claude pour quel usage ?

**Référence** : Benjamin Polge, Journal du Net, 26 novembre 2026, article (guide comparatif), https://www.journaldunet.com/intelligence-artificielle/1559149-fable-5-2-opus-5-5-sonnet-5-5-haiku-5-5-quel-modele-claude-pour-quel-usage/

**Axe** : IA appliquée au produit (Investissement tech)

> **Conflit d'intérêts** : cette fiche a été rédigée par un modèle Claude, de la même famille que les quatre modèles comparés. Les prix, vitesses et recommandations sont repris tels que publiés par le Journal du Net, sans commentaire sur les modèles eux-mêmes.

## 1. L'idée clé
Selon l'auteur, dans la gamme Claude renouvelée entre le 22 septembre et le 9 novembre 2026, le plus gros modèle n'est pas le meilleur partout : chaque modèle a son créneau, et la bonne architecture combine souvent un modèle cher en orchestrateur et un modèle moins cher en exécutant.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [VentureBeat sur le test de correction de bugs Fable contre Opus](2026-11-24-venturebeat-test-correction-bugs-fable-opus.md) (coût par tentative réussie, Fable environ trois fois plus cher pour un résultat proche), la fiche [Databricks sur la fidélité aux modèles](2026-11-20-bdm-databricks-fidelite-modeles-ia.md) (coût par tâche comme critère de choix) et la fiche [OCTO sur l'effort de raisonnement des agents](2026-11-20-octo-boucard-effort-raisonnement-agents.md).
- **Une grille tarifaire complète de la gamme** : en dollars par million de tokens (entrée / sortie), Fable 5.2 à 8 / 40, Opus 5.5 à 4 / 20, Sonnet 5.5 à 2 / 10, Haiku 5.5 à 0,10 / 0,50 jusqu'à 100 000 tokens puis 0,50 / 2,50 ; tous avec un contexte d'un million de tokens. VentureBeat comparait deux modèles ; ici, les quatre niveaux sont posés côte à côte.
- **La vitesse comme critère** : 111, 107, 139 et 217 tokens par seconde selon Artificial Analysis. Haiku est deux fois plus rapide qu'Opus, ce qui compte pour la voix et le service client.
- **Le duo orchestrateur et exécutant** : Opus 5.5 pour planifier, Sonnet 5.5 pour exécuter ; Haiku 5.5 à écarter comme orchestrateur parce qu'il risque de dériver. Une recommandation d'architecture, pas seulement de choix de modèle.
- **Sinon, peu de neuf** : le principe « le bon modèle pour la bonne tâche » est connu ; l'apport est la cartographie de 15 cas d'usage, dont le classement n'a pas pu être relu en détail (code couleur non restitué).

## 3. Résumé
L'article part du renouvellement de la gamme Claude par Anthropic entre le 22 septembre et le 9 novembre 2026 et pose un tableau : contexte, vitesse mesurée par Artificial Analysis, prix d'entrée, de lecture en cache et de sortie. Il passe ensuite les modèles en revue. Fable 5.2, le plus avancé, est présenté comme la version grand public de Claude Mythos 5.2 avec des garde-fous renforcés en cybersécurité et en biologie ; recommandé pour les tâches complexes et les agents à forte valeur ajoutée, comme le débogage d'un projet bloqué, mais jugé trop cher au quotidien. Opus 5.5, modèle « à tout faire », approche Fable pour deux fois moins cher, avec une meilleure adhérence aux consignes en développement dans le harnais de Claude Code ; il raisonne beaucoup et son tokenizer est jugé peu optimisé, d'où le conseil de le réserver aux tâches complexes ou à l'orchestration. Sonnet 5.5 est décrit comme le plus sous-estimé et le meilleur rapport prix et intelligence, adapté aux systèmes agentiques simples et à la rédaction courante, mais pas comme agent de code principal. Haiku 5.5, le moins cher et le plus rapide, vise le service client, l'assistant vocal, le tri de tickets, la modération, la traduction, la classification et le traitement par lots. L'article se termine par un tableau de 15 cas d'usage (code, débogage, tests, service client, RAG, OCR, comptes rendus de réunion, classification d'e-mails, routage de tickets…) avec un classement par modèle, et rappelle que le plus gros modèle n'est pas forcément le meilleur partout.

## 4. Citations et noms
**Citations** :
- « Le plus gros modèle n'est pas forcément le meilleur partout », Benjamin Polge

**Noms cités** :
- *Anthropic* : éditeur de la gamme Claude comparée.
- *Claude Fable 5.2* : modèle le plus avancé de la gamme publique, le plus cher.
- *Claude Mythos 5.2* : modèle dont Fable 5.2 serait la version grand public, avec garde-fous renforcés.
- *Claude Opus 5.5, Sonnet 5.5, Haiku 5.5* : les trois autres niveaux de gamme.
- *Claude Code* : harnais de développement dans lequel Opus 5.5 est jugé le plus fiable.
- *Artificial Analysis* : source des mesures de vitesse.

## 5. Mots-clés
routage de modèles, coûts des tokens, agents IA, harnais agentique, FinOps

## Lecture CPO
- **Implications** :
  - Concevoir les produits agentiques en plusieurs étages (orchestrateur, exécutants, tâches de masse) plutôt que sur un seul modèle : l'écart de prix entre Fable 5.2 et Haiku 5.5 va jusqu'à 80 fois en entrée.
  - Inclure la vitesse dans les critères de choix pour les usages temps réel (voix, service client), pas seulement la qualité.
  - Valider ces recommandations sur ses propres tâches, comme le fait le test VentureBeat : un guide éditorial ne remplace pas des evals maison.
- **Fiabilité** : guide d'un média tech, sans intérêt commercial apparent ; prix publics et vitesses sourcées (Artificial Analysis), mais les jugements qualitatifs (« sous-estimé », « risque de dériver ») relèvent de l'avis de l'auteur, sans test publié. Conflit d'intérêts du rédacteur de la fiche signalé en tête.
- **Maturité** : Pratique établie : le routage entre niveaux de modèles selon la tâche est devenu une pratique courante des équipes qui construisent des agents.
- **Réutilisation** : présentation client DSI ou équipe produit sur le choix et l'étagement des modèles (tableau de prix, duo orchestrateur et exécutant), à croiser avec VentureBeat et Databricks ; support de formation PM sur la conception de produits IA.
