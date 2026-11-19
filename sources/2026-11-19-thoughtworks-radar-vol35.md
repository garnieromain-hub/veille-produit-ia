# Technology Radar, volume 35

**Référence** : Thoughtworks Technology Advisory Board (dont Rachel Laycock, CTO), Thoughtworks, novembre 2026 (jour non publié), rapport semestriel, https://www.thoughtworks.com/radar

**Axe** : IA appliquée au produit (Transformation des entreprises)

## 1. L'idée clé
Le travail avec agents devient une discipline d'ingénierie à part entière (le « harnais » : contexte, mémoire, boucles de retour, garde-fous), et son goulot n'est plus le code mais la capacité de revue et le flux jusqu'à la production. Le Radar met en garde contre les fausses mesures (débit de code, validation humaine de façade) et contre l'usage par défaut des modèles frontière.

## 2. Ce qui est nouveau
**Par rapport à** : le volume 34 (avril 2026, « retour aux fondamentaux de l'ingénierie »), à la série OCTO de Bruno Boucard sur les harnais (sources complémentaires du 13 novembre) et à la fiche [OCTO Camus](2026-11-13-octo-camus-agent-ou-comite.md) sur le coût des comités d'agents.
- **« Human-in-the-loop theater » en Caution** : une validation humaine sur des changements que personne ne peut évaluer devient un « puits de responsabilité ». C'est la première fois qu'un référentiel reconnu nomme ce risque ; le discours dominant présente l'humain dans la boucle comme la garantie par défaut.
- **« Coding throughput as a measure of productivity » en Caution** : la part de code généré ou les tokens consommés mesurent l'adoption, pas la productivité. Le Radar renvoie aux métriques DORA et aux résultats business, ce qui rejoint le paradoxe de productivité de [Cagan](2026-10-16-svpg-ai-productivity-paradox.md).
- **« Path-to-production mapping » en Adopt** : une technique d'atelier ancienne remise en avant, parce que le code produit plus vite déplace le goulot ailleurs dans la chaîne.
- **Le modèle frontière par défaut en Caution** : les modèles ouverts ont comblé une grande partie de l'écart, et le routage entre modèles devient un choix d'architecture et de coût.
- **Les agents de nuit en Trial** : confier une tâche de la taille d'une fonctionnalité à un agent le soir et relire le lendemain, réservé aux équipes qui ont déjà bac à sable, spécifications et capteurs de retour.

## 3. Résumé
Le Radar s'organise autour de quatre thèmes. Le premier, le harnais à l'échelle : tout ce qui entoure un agent (mémoire, contexte, boucles de retour, garde-fous) se structure en discipline, avec un écosystème de plugins et un besoin de propriété et de maintenance ; un « harnais d'entreprise » pourrait devenir un produit. Le deuxième, au-delà des modèles frontière : choisir automatiquement un modèle propriétaire de pointe n'est plus évident, les modèles ouverts offrent flexibilité, confidentialité et moindre dépendance. Le troisième, mettre plus d'agents au travail : les développeurs pilotent plusieurs sessions en parallèle et confient des tâches plus longues, si bien que leur attention et leur capacité de revue deviennent le goulot ; quand la revue ne suit pas, la supervision tourne au théâtre. Le quatrième, construire l'usine IA : l'économie des tokens se ramène à l'économie de l'infrastructure (routage, batching, stockage, réseau), avec Kubernetes comme socle. Les blips détaillent ces thèmes : en Adopt, bac à sable d'agents, divulgation progressive du contexte, cartographie du chemin vers la production ; en Trial, « feedback flywheel » (mise à jour régulière des fichiers d'instructions partagés à partir des sessions), sous-agents, petits modèles, agents de nuit ; en Caution, l'inflation des instructions d'agents, le théâtre de la validation humaine, le débit de code comme mesure et l'usage systématique des modèles frontière. Aucun chiffre d'enquête : c'est un avis d'experts fondé sur les missions de Thoughtworks.

## 4. Citations et noms
**Citations** :
- « À mesure que les développeurs font tourner plus d'agents, leur attention et leur capacité de revue deviennent des goulots. » (« As developers run more agents, their attention and review capacity become bottlenecks. »), Thoughtworks
- « L'étape d'approbation fonctionne comme un puits de responsabilité : personne ne possède vraiment la décision. » (« The approval step functions as an accountability sink: no one truly owns the decision. »), Thoughtworks
- « L'économie des tokens se ramène finalement à l'économie de l'infrastructure. » (« Token economics ultimately comes down to infrastructure economics. »), Thoughtworks

**Noms cités** :
- *Rachel Laycock* : CTO de Thoughtworks, membre du comité qui rédige le Radar.
- *Métriques DORA* : indicateurs de performance de livraison recommandés à la place du débit de code.
- *OpenAI Codex, OpenCode* : agents de code passés en Adopt.
- *Claude Managed Agents, Agent Client Protocol* : outils et protocoles en évaluation (Assess).
- *Feedback flywheel* : habitude d'équipe de réviser les instructions partagées des agents (AGENTS.md, skills).
- *Kubernetes, LiteLLM, KServe* : briques de l'« usine IA ».

## 5. Mots-clés
agents IA, harnais agentique, productivité IA, goulot d'étranglement, gouvernance IA, coûts des tokens

## Lecture CPO
- **Implications** :
  - Bannir des tableaux de bord la part de code généré par IA comme indicateur de réussite : mesurer le délai jusqu'à la production et les résultats.
  - Auditer les étapes de validation humaine sur les sorties d'agents : qui peut réellement juger ce qu'il approuve ?
  - Avant d'ajouter des agents, cartographier le chemin vers la production : le goulot est souvent la revue, les tests ou le déploiement.
  - Le choix du modèle (frontière, ouvert, petit) devient une décision produit de coût et de souveraineté, à arbitrer par cas d'usage.
- **Fiabilité** : cabinet de conseil en ingénierie, qui vend la mise en place de ces pratiques ; mais le Radar est une référence ancienne et reconnue, qui s'appuie sur des missions réelles et assume des avis négatifs (Caution). Pas de données chiffrées ni de méthodologie publiée : c'est une opinion collective d'experts. Le jour de publication n'est pas indiqué (seulement « novembre 2026 »).
- **Maturité** : Tendance émergente : le harnais et la revue comme goulot sont observés sur de nombreux projets, mais les pratiques (agents de nuit, feedback flywheel) sont encore en Trial.
- **Réutilisation** : article OCTO (« Le théâtre de la validation humaine », avec les retours de Camus et Ploquin) ; post LinkedIn (« Le débit de code n'est pas une mesure de productivité, même Thoughtworks le dit ») ; présentation client DSI sur les indicateurs de pilotage des agents.
