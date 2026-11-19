# Un agent ou un comité ? Ce que l'usage des comités m'a appris depuis leur mise en place

**Référence** : Claude Camus, OCTO Talks !, 30 octobre 2026, retour d'expérience, https://blog.octo.com/un-agent-ou-un-comite-ce-que-l'usage-des-comites-m'a-appris-depuis-leur-mise-en-place

**Axe** : IA appliquée au produit

## 1. L'idée clé
Faire travailler plusieurs agents sur la même question ne prouve rien : leur accord n'est pas une preuve, et le comité coûte cher. Ce qui améliore vraiment la fiabilité, c'est un relecteur neuf (sans contexte) et un script qui revérifie la preuve. Le comité sert à comprendre et à trier, jamais à écrire.

## 2. Ce qui est nouveau
**Par rapport à** : [Torres sur les evals](2026-10-16-torres-ai-evals-habitude-discovery.md) (évaluer les produits IA), [Uber](2026-10-16-uber-prototypage-ia.md) (gouvernance légère du prototypage) et au discours dominant « multi-agents = plus fiable », porté par les éditeurs.
- **Des mesures, pas des impressions** : sur 44 verdicts, l'agent vérificateur a validé à tort 8 preuves que le script rejetait ; le script répond en secondes contre environ six minutes, sans tokens. Rare dans un corpus dominé par les déclarations.
- **Le coût du comité chiffré** : environ 358 000 tokens contre 84 000 pour un agent seul (4,3 fois), au-delà du seuil d'abandon de 2 fois que l'auteur s'était fixé.
- **Le relecteur neuf est le vrai gain** : dans 14 cas sur 29, il a conduit à au moins une correction (dont une protection de sécurité ouverte).
- **L'escalade plutôt que le parallélisme** : un agent d'abord, un second seulement sans preuve valide ; environ 40 % d'exécutions en moins pour la même couverture.
- **Écrit par un coach produit qui ne code pas** : le point de vue est celui d'un utilisateur métier qui orchestre des agents, pas d'un ingénieur.

## 3. Résumé
L'auteur, coach produit, part d'une question : quand faire confiance à ce que produit un agent ? Du 3 au 23 octobre 2026, il compare un mode « classique » (un agent par tâche) et un mode « comité » (plusieurs agents, puis consolidation). Il pose des règles dès le début : le comité ne rédige jamais, un seul rédacteur par sujet, un second agent seulement si le premier revient sans preuve, et « information insuffisante » si les deux échouent, auquel cas l'humain tranche. Quand un petit script peut revérifier, c'est lui qui décide. Il mesure ensuite quatre changements : le relecteur neuf (14 corrections sur 29 relectures), le script contre l'agent vérificateur (8 faux positifs sur 44), l'escalade (de 20 à 12 et de 25 à 15 exécutions), et le comité pour trier une veille (13 constats et 7 tickets répartis en 8 adoptés, 5 rejetés, 3 clos). Les tests de charge montrent que le goulot est le lancement des agents (65 % de refus à 40 lancements simultanés). Il liste les approches abandonnées : le comité pour tout (4,3 fois le coût), l'accord comme preuve (contredit par une escalade le 8 octobre), les conclusions sur un seul cas. Il reconnaît les limites (petits échantillons, un seul poste, classement fait par lui-même, sans groupe témoin) et conclut sur quatre décisions, en gardant la validation manuelle pour les actions irréversibles.

## 4. Citations et noms
**Citations** :
- « Le comité sert à comprendre, jamais à écrire. », Claude Camus
- « Un agent seul se croit toujours dans le vrai. », Claude Camus
- « Qu'est-ce qui me permettrait de vérifier sans croire personne ? », Claude Camus

**Noms cités** :
- *Claude Camus* : coach produit chez OCTO, auteur d'une série de retours d'expérience sur les agents.
- *BMAD* : cadre de développement agentique utilisé dans ses articles précédents.
- *Relecteur neuf, escalade, comité, gardes* : les dispositifs testés.

## 5. Mots-clés
agents IA, evals, qualité, retour d'expérience, coûts des tokens

## Lecture CPO
- **Implications** :
  - Pour les équipes qui outillent leur travail produit avec des agents (synthèse, veille, livrables), exiger une preuve vérifiable par script plutôt qu'un avis d'agent.
  - Budgéter le multi-agents : 4 fois le coût pour un gain non démontré ; commencer par un agent bien briefé.
  - Garder une validation humaine explicite pour les envois clients et les suppressions, quelle que soit la confiance dans l'agent.
- **Fiabilité** : praticien OCTO (donc maison, sans intérêt commercial direct dans un outil), mesures publiées avec leurs limites ; échantillons petits, un seul utilisateur, pas de groupe témoin. Valeur d'exemple de méthode plus que de preuve statistique.
- **Maturité** : Signal faible : pratique individuelle documentée, pas encore une pratique d'équipe.
- **Réutilisation** : article OCTO de synthèse (« ce qu'un non-développeur apprend en pilotant des agents ») avec ses articles sur les tokens et le PowerPoint ; post LinkedIn (« l'accord entre agents n'est pas une preuve ») ; atelier client sur la gouvernance des usages agentiques.
