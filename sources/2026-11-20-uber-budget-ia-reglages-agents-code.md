# Uber a épuisé son budget IA, puis a réduit le contexte et le raisonnement de ses outils de code

**Référence** : Louis Columbus, VentureBeat, 19 novembre 2026, article (retour d'expérience tiré d'une intervention d'Uber au VentureBeat Agentic Infrastructure Stack Summit du 28 octobre 2026, complété par l'enquête VB Pulse d'octobre), https://venturebeat.com/infrastructure/uber-blew-through-its-ai-budget-then-dialed-back-context-and-reasoning-in-its-ai-coding-tools

**Axe** : Investissement tech (IA appliquée au produit)

## 1. L'idée clé
Après avoir épuisé son budget IA 2026 dès les premiers mois, Uber a repris la main sur ses coûts non pas en limitant l'usage, mais en imposant à tous ses ingénieurs quatre réglages par défaut (compaction du contexte, effort de raisonnement moyen, durée du cache, outils MCP chargés à la demande). Plus de contexte et plus de raisonnement ne veulent pas dire de meilleurs résultats : ce sont des paramètres à piloter comme une politique d'entreprise.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Cebr/Wasabi](2026-11-19-cebr-wasabi-depassements-infrastructure-ia.md) et la fiche [Menlo Ventures](2026-11-13-menlo-state-of-enterprise-ai-2026.md), qui constatent le dérapage des budgets IA par enquête, et au [Radar Thoughtworks vol. 35](2026-11-19-thoughtworks-radar-vol35.md), qui met en garde contre l'usage par défaut des modèles frontière.
- **Des leviers FinOps IA concrets et chiffrés** : compaction automatique à 400 000 tokens (même sur des modèles à un million), effort « medium » au lieu de « high », cache d'une heure pour l'agent principal et de cinq minutes pour les sous-agents, aucune définition d'outil MCP chargée au démarrage (50 000 à 70 000 tokens évités pour plus de 100 outils). Les fiches précédentes constataient le dépassement sans dire comment le corriger.
- **Un résultat mesuré à périmètre constant** : coût par 1 000 requêtes en baisse d'environ 34 % depuis le pic, coût par session en baisse de 52 % depuis juin, et 90 % d'économie sur une tâche (nettoyage de feature flags) par le seul choix du modèle.
- **Les réglages sont centralisés et testés en A/B** : une couche interne (AIFX) installe et configure les outils de code pour tous, et compare les cohortes. Le coût devient une affaire de plateforme, pas de discipline individuelle.
- **Le contexte se structure plutôt qu'il ne s'empile** : un graphe de contexte d'entreprise (près de 200 millions de nœuds et arêtes) donne aux agents une « carte » à explorer ; sur un exemple publié, 38 secondes contre 20 minutes et une conclusion erronée sans le graphe.
- **Pas de ROI financier** : Uber mesure le débit (documents de conception, PR, déploiements) à qualité constante, et ne voit que depuis peu une tendance sur les fonctionnalités livrées, sans chiffre. Cela confirme, sur un grand compte, l'écart entre dépenses et retour mesuré.

## 3. Résumé
L'article part d'un aveu : selon son CTO Praveen Neppalli Naga, interrogé par The Information en avril, Uber a consommé son budget IA 2026 en quelques mois, alors que ses requêtes agentiques hebdomadaires ont été multipliées par 9,4 entre février et août. Le cas est replacé dans l'enquête VB Pulse d'octobre : 38 % des 156 répondants ont retardé, réduit ou annulé un projet IA à cause de coûts supérieurs aux prévisions. Uday Kiran Medisetty, distinguished engineer, détaille ensuite les quatre réglages imposés via AIFX et testés en A/B : compaction à 400 000 tokens (les coûts s'envolent au-delà de 700 000 à 800 000), effort de raisonnement moyen (les modèles récents y donneraient de meilleurs résultats), cache différencié parce que les ingénieurs quittent souvent l'agent principal plus de cinq minutes, et outils appelés à la demande via une passerelle MCP centrale. Résultats : environ 34 % de baisse du coût par 1 000 requêtes et 52 % du coût par session, sans ventilation par réglage. L'article élargit avec T-Mobile, pour qui charger toute la documentation dans un agent n'a « pas du tout » marché (contexte réduit, agents spécialisés, cache clé-valeur au lieu d'un graphe trop lent), et Adobe, pour qui plus de contexte peut au contraire aider le marketing. Il revient au graphe de contexte d'Uber, qui a doublé entre août et octobre. Sur le ROI, Uber cherche à maximiser le débit à garde-fous de qualité constants (incidents par changement, retours arrière, délais de revue, suivi des commentaires du relecteur IA, CI auto-réparatrice d'abord validée par un humain). Selon VB Pulse, 26 % des entreprises évaluent leurs dépenses IA par un retour financier mesuré et 44 % par un résultat opérationnel : Uber est dans ce second groupe. L'article conclut par quatre questions à poser à son équipe plateforme (limite de contexte, effort par défaut, durée du cache, tokens de schémas d'outils chargés avant le premier prompt).

## 4. Citations et noms
**Citations** :
- « Maximiser le débit tout en gardant nos garde-fous de qualité inchangés. » (« maximize the throughput while keeping our quality guardrails the same »), Uday Kiran Medisetty, Uber.
- « Ça n'a pas marché du tout. » (« That didn't work at all. »), Jeff Simon, DSI de T-Mobile, à propos du chargement de toute la documentation support dans un agent.
- « Le bon contexte pour la bonne tâche et la bonne personne. » (« the right context for the right task for the right person »), Anjul Bhambhri, Adobe.

**Noms cités** :
- *Uday Kiran Medisetty* : distinguished engineer chez Uber, source principale des réglages et des chiffres.
- *Praveen Neppalli Naga* : CTO d'Uber, à l'origine de l'aveu sur le budget épuisé (via The Information).
- *AIFX* : couche interne d'Uber qui installe et configure les outils de code IA et leurs paramètres.
- *Claude Code* : seul outil nommé, utilisé pour les sessions de code interactives ; les modèles ne sont pas précisés.
- *MCP (Model Context Protocol)* : protocole d'outils dont Uber ne charge plus les définitions au démarrage, au profit d'une passerelle centrale.
- *VB Pulse* : enquête de VentureBeat d'octobre 2026 (156 répondants qualifiés), source des chiffres sectoriels.
- *Jeff Simon (T-Mobile)* et *Anjul Bhambhri (Adobe)* : contrepoints sur la quantité de contexte utile.
- *The Information* : média qui a rapporté l'épuisement du budget en avril.

## 5. Mots-clés
FinOps, coûts des tokens, agents IA, retour d'expérience, mesure du ROI, budgets IT

## Lecture CPO
- **Implications** :
  - Traiter les paramètres des outils IA (contexte, effort, cache, outils chargés) comme une politique d'entreprise portée par une équipe plateforme, avec tests A/B, plutôt que comme des préférences individuelles.
  - Suivre un coût unitaire (par session, par 1 000 requêtes) à modèle constant : c'est l'indicateur qui a permis à Uber de mesurer l'effet de ses réglages.
  - Le choix du modèle par tâche est le levier le plus puissant (90 % sur une tâche) : prévoir un routage par type de tâche dans les produits et les outils internes.
  - Pour le ROI, assumer des indicateurs opérationnels (débit à qualité constante) tant que le retour financier n'est pas mesurable, en le disant explicitement à la direction.
- **Fiabilité** : retour d'un praticien sur scène, relayé par un journaliste ; chiffres déclarés par Uber, sans méthode publiée ni ventilation par réglage, modèles non nommés. L'enquête VB Pulse est petite (156 répondants) et menée par le média. Le constat d'épuisement du budget vient d'une source tierce (The Information).
- **Maturité** : Tendance émergente : le dérapage des coûts est désormais largement documenté, mais les pratiques de maîtrise (réglages par défaut, coût unitaire par session) n'apparaissent que dans quelques grands comptes.
- **Réutilisation** : présentation client DSI (les quatre questions à poser à son équipe plateforme, et les 34 % / 52 % de baisse) ; article OCTO sur le FinOps des agents de code, en regard de la fiche Cebr ; post LinkedIn « Plus de contexte n'est pas mieux : Uber a économisé en en donnant moins » ; table ronde sur la mesure du ROI de l'IA de code.
