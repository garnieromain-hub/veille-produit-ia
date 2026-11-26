# I built an AI agent. It broke my assumptions about my own team

**Référence** : Matthew Finlayson (CTO d'ActivTrak), CIO.com (blog First Person), 25 novembre 2026, retour d'expérience, https://www.cio.com/article/4252552/i-built-an-ai-agent-it-broke-my-assumptions-about-my-own-team.html

**Axe** : IA appliquée au produit (Transformation des entreprises)

## 1. L'idée clé
Construire soi-même un agent, même pour une tâche simple, révèle que le travail d'une équipe repose sur un jugement implicite que personne ne sait formuler. Un dirigeant tech qui code son propre agent comprend mieux ce qu'il demande à ses équipes, et ce que coûte vraiment l'automatisation : validation continue, maintenance des règles et choix de l'endroit où elle s'arrête.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Cutler sur le « contexting »](2026-11-19-cutler-tbm-452-contexting.md) (le savoir tacite des organisations), la fiche [OpenAI Performance Factory](2026-11-20-openai-performance-factory-codex.md) (evals par rétrotest d'un agent d'exploitation) et la fiche [Databricks sur la fidélité aux modèles](2026-11-20-bdm-databricks-fidelite-modeles-ia.md) (changer de modèle sans refonte).
- **Le savoir tacite, mesuré sur un cas réel** : le routage des tickets semblait une simple classification, mais les managers ne pouvaient dire que si une décision précise était juste, pas énoncer la règle. Précision de 60 % au départ (avec des noms inventés), 95 % après corrections des managers.
- **Les modèles interprètent différemment la même consigne** : face à une règle interdisant les recommandations d'emploi, Gemini évite les questions limites, Opus cherche des contournements créatifs, Sonnet applique la règle à la lettre. Changer de modèle, même au sein d'une famille, modifie les appels d'outils, le format et les refus.
- **Un ROI modeste mais chiffré** : environ 2 heures par semaine gagnées pour chacun des sept managers, pour quelques centimes par mois d'exploitation (hors temps de construction).
- **Savoir s'arrêter** : l'auteur renonce à l'apprentissage automatique à partir des corrections, car les raffinements suivants rapportaient moins que leur coût.

## 3. Résumé
Le CTO d'ActivTrak (plus de 9 500 organisations clientes) construit un agent qui route vers la bonne équipe d'ingénierie les incidents clients à escalader, environ 10 % du support, soit une centaine par semaine. Il passe par quatre versions : Claude Code avec un connecteur Jira, un workflow low-code n8n, Claude Managed Agents, puis la plateforme d'agents de Google, où tourne la production d'ActivTrak, pour accéder au code et au suivi des tickets. Premier enseignement : comprendre le flux avant de l'automatiser. Le routage dépendait d'un jugement non écrit (un problème de reporting vient-il du front ou des données ? qui possède telle tâche ?), et construire l'agent a obligé à transformer ce jugement éclaté en règles explicites. Deuxième : valider les sorties. La première version n'avait raison que 60 % du temps et inventait des noms ; les corrections des managers l'ont portée à environ 95 %. Les modèles d'OpenAI, Google et Anthropic n'interprètent pas les restrictions de la même façon, et un changement de modèle modifie le comportement, d'où une validation continue après déploiement. Troisième : décider où s'arrête l'automatisation. Il ajoute des outils (détection de régression, localisation du code, identification du développeur) tout en se demandant si le routage justifiait autant de machinerie, et renonce à l'apprentissage automatique des corrections. Quatrième : mesurer. Deux heures par semaine gagnées par manager, des coûts d'exploitation de quelques centimes, mais des règles à maintenir à chaque changement de responsabilités dans les équipes. Il conclut en invitant les dirigeants tech à construire un agent eux-mêmes, et jugera les prochains sur la gestion des exceptions, l'adaptation aux changements de flux et l'effort de maintenance.

## 4. Citations et noms
**Citations** :
- « Construire l'agent, c'était transformer le jugement éclaté du groupe en règles explicites. » (« Building the agent meant turning the group's fragmented judgment into explicit rules. »), Matthew Finlayson
- « Des coûts d'exploitation faibles ne valent pas grand-chose si le système exige des interventions constantes pour rester utile. » (« Low operating costs mean little if the system needs constant intervention to stay useful. »), Matthew Finlayson
- « J'encourage les autres dirigeants tech à construire un agent eux-mêmes. » (« I encourage other technology leaders to build an agent themselves. »), Matthew Finlayson

**Noms cités** :
- *Matthew Finlayson* : CTO d'ActivTrak, auteur et constructeur de l'agent.
- *ActivTrak* : éditeur dont la plateforme sert plus de 9 500 organisations et plus d'un million d'utilisateurs.
- *Claude Code, Claude Managed Agents (Anthropic)* : première et troisième versions de l'agent ; Opus et Sonnet comparés.
- *n8n* : outil low-code de la deuxième version.
- *Plateforme d'agents de Google, Gemini* : version finale, proche de la production ; Gemini comparé.
- *Jira* : outil de suivi des tickets connecté à l'agent.

## 5. Mots-clés
agents IA, savoir tacite, evals, retour d'expérience, mesure du ROI, routage de modèles

## Lecture CPO
- **Implications** :
  - Avant d'automatiser un flux, faire expliciter les règles de décision par ceux qui les appliquent : c'est un travail de discovery, et souvent la principale valeur du projet.
  - Prévoir des evals rejouées à chaque changement de modèle, y compris au sein d'une même famille : le comportement d'un agent n'est pas stable d'une version à l'autre.
  - Inscrire au business case la maintenance des règles (réorganisations, changements de périmètre), pas seulement le coût d'exploitation.
  - Encourager CPO et responsables produit à construire eux-mêmes un petit agent pour calibrer leurs attentes envers les équipes.
- **Fiabilité** : praticien qui raconte son propre projet, sans intérêt commercial direct (ActivTrak n'est pas un éditeur d'agents) ; chiffres déclaratifs sur un cas unique et un périmètre restreint (sept managers).
- **Maturité** : Signal faible : le dirigeant tech qui construit lui-même un agent pour comprendre son équipe reste rare dans les retours publics, même si les leçons (evals, savoir tacite) recoupent des pratiques émergentes.
- **Réutilisation** : post LinkedIn « 60 % puis 95 % : ce qu'un CTO a appris en codant son propre agent » ; article OCTO sur l'explicitation du savoir tacite comme première étape de l'automatisation (avec Cutler) ; atelier client de dirigeants qui construisent un agent en une demi-journée.
