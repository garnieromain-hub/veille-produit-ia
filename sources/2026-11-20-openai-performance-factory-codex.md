# OpenAI dévoile Performance Factory, un système d'optimisation logicielle fondé sur Codex qui garde ChatGPT rapide

**Référence** : Ben Dickson, VentureBeat, 19 novembre 2026, article (exclusivité, présentation d'un système interne par OpenAI), https://venturebeat.com/orchestration/exclusive-openai-reveals-performance-factory-a-codex-powered-software-optimization-system-that-keeps-chatgpt-fast

**Axe** : IA appliquée au produit

## 1. L'idée clé
Quand les agents écrivent de plus en plus de code, le diagnostic des régressions de performance devient le goulot. OpenAI y répond en transformant chaque alerte en tâche suivie, que des sessions Codex font avancer étape par étape (investigation, cause racine, correctif, vérification), avec un agent contradicteur qui conteste chaque diagnostic. Le système trouve bien les causes, mais corrige encore peu.

## 2. Ce qui est nouveau
**Par rapport à** : le [Radar Thoughtworks vol. 35](2026-11-19-thoughtworks-radar-vol35.md) (le goulot se déplace du code vers la revue et le flux jusqu'à la production) et la fiche [OCTO Camus](2026-11-13-octo-camus-agent-ou-comite.md) sur les comités d'agents ; au discours dominant des éditeurs, qui présente les agents de code comme des producteurs de code.
- **Une architecture d'agents de production décrite en détail** : service de tâches configuré par fichiers markdown, boucle de dispatch qui lance Codex, API d'exécution cloud aux permissions contrôlées, abonnements qui mettent une tâche en pause en attendant une revue humaine sur GitHub. C'est un cas concret de « harnais » à l'échelle d'un éditeur.
- **La revue contradictoire chiffrée** : un second agent, dans un contexte neuf, conteste le diagnostic ; il en renvoie environ 25 % après réglage des instructions. Cela donne un ordre de grandeur au principe du comité d'agents.
- **Un entonnoir honnête** : plus de 1 700 investigations en un peu plus de trois mois, plus de 600 causes racines, environ 400 correctifs proposés, environ 50 correctifs livrés influencés par les agents, dont environ 15 PR écrites par Codex. OpenAI reconnaît être en deçà de ses ambitions : l'agent excelle à diagnostiquer, beaucoup moins à corriger les problèmes architecturaux.
- **Passer des conclusions, pas des données** : les agents se transmettent métriques, requêtes et conclusions reproductibles plutôt que des volumes bruts, ce qui préserve les preuves sans saturer le contexte.

## 3. Résumé
L'article part d'un constat : avec la montée du code écrit par des agents, diagnostiquer les régressions de performance devient un goulot. L'équipe d'OpenAI a d'abord enquêté à la main, puis a construit plus de 30 outils spécialisés, avant de les condenser dans une compétence Codex réutilisable, « perf-forensics ». Les ingénieurs servant encore d'intermédiaires entre alertes et Codex, le système a été branché directement sur les alertes, et chaque régression est devenue une tâche suivie. L'article détaille les quatre composants (service de tâches, boucle de dispatch, API d'exécution cloud, abonnements), puis le principe de transmission par conclusions vérifiables. Il décrit la revue contradictoire, d'abord trop sévère, aujourd'hui calibrée à environ 25 % de renvois. Viennent les résultats sur un peu plus de trois mois (environ 17 investigations automatisées par jour) et leur limite : peu de correctifs livrés, l'agent étant efficace quand la cause est claire et le correctif circonscrit. L'article tire quatre leçons pour les entreprises : ne montrer aux humains que l'information pertinente pour éviter la fatigue, préserver les preuves sans surcharger le contexte, évaluer les agents par rétrotest sur des incidents historiques (et la lisibilité des synthèses à part), surveiller les agents eux-mêmes avec un agent quotidien qui analyse leurs journaux. OpenAI prévoit d'étendre le système à l'optimisation proactive (comparaison de profils et traces entre versions, dimensionnement des services) et étudie le déploiement de correctifs à faible risque sans approbation humaine.

## 4. Citations et noms
**Citations** : rien de notable (la source accessible ne permet pas de restituer de citation exacte fiable ; les propos sont paraphrasés dans le résumé).

**Noms cités** :
- *OpenAI* : éditeur, auteur et utilisateur du système.
- *Performance Factory* : système interne qui transforme les alertes de performance en tâches traitées par des agents.
- *Codex* : agent de code d'OpenAI qui exécute les sessions d'investigation et de correction.
- *perf-forensics* : compétence Codex réutilisable qui encode les procédures d'investigation de l'équipe.
- *ChatGPT* : produit dont la performance est surveillée.
- *Revue contradictoire (adversarial review)* : agent distinct qui conteste le diagnostic dans un contexte neuf.

## 5. Mots-clés
agents IA, harnais agentique, evals, qualité, goulot d'étranglement, autonomie des agents

## Lecture CPO
- **Implications** :
  - Les agents sont plus fiables pour diagnostiquer que pour corriger : commencer par des cas d'usage d'investigation (incidents, régressions, analyse de logs) avant d'automatiser les correctifs.
  - Modéliser le travail des agents en tâches à étapes avec des points de pause humains explicites, plutôt qu'en conversations : c'est ce qui rend le système pilotable et mesurable.
  - Évaluer un agent par rétrotest sur des incidents historiques connus : une pratique d'evals reproductible par les équipes produit.
  - Prévoir la supervision des agents eux-mêmes (échecs d'outils, permissions) comme une fonction d'exploitation à part entière.
- **Fiabilité** : l'éditeur présente son propre système en exclusivité ; chiffres auto-déclarés, sans méthode publiée ni comparaison avec le travail manuel. L'aveu d'un taux de correction faible (environ 15 PR Codex livrées sur plus de 1 700 investigations) renforce la crédibilité de l'ensemble.
- **Maturité** : Signal faible : architecture interne d'un laboratoire de pointe, avec ses outils maison ; les principes (tâches à étapes, revue contradictoire, rétrotest) sont transposables, mais rares en entreprise.
- **Réutilisation** : article OCTO sur les agents en exploitation (l'entonnoir 1 700 / 600 / 400 / 50 / 15) ; post LinkedIn « L'agent trouve la cause, l'humain corrige encore » ; présentation client sur la conception d'un harnais avec revue contradictoire et evals par rétrotest.
