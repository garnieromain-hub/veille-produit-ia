# Agents de code : les 4 meilleurs conseils des ingénieurs d'OpenAI

**Référence** : Benjamin Polge, Journal du Net, 23 novembre 2026, article (compte rendu des conseils présentés par OpenAI au DevDay Exchange de Paris, fin octobre), https://www.journaldunet.com/intelligence-artificielle/1558391-agents-de-code-les-4-meilleurs-conseils-des-ingenieurs-d-openai/

**Axe** : IA appliquée au produit

## 1. L'idée clé
Pour tirer parti d'un agent de code, il faut lui donner un objectif vérifiable plutôt que des consignes, garder peu de règles, réserver les équipes d'agents en parallèle aux problèmes difficiles, et remettre à plat ses workflows (skills, plugins, hooks) à chaque nouveau modèle, car les bonnes pratiques ont une date de péremption.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Performance Factory d'OpenAI](2026-11-20-openai-performance-factory-codex.md) (harnais interne à tâches suivies et revue contradictoire), le [Radar Thoughtworks vol. 35](2026-11-19-thoughtworks-radar-vol35.md) (le harnais comme discipline d'ingénierie) et la fiche [OCTO Camus](2026-11-13-octo-camus-agent-ou-comite.md) sur les comités d'agents ; au discours dominant qui consiste à enrichir sans cesse les instructions et les fichiers de règles des agents.
- **Jeter ses workflows à chaque nouveau modèle** : là où le discours dominant accumule skills et règles comme un capital, OpenAI conseille de tout remettre en question à chaque sortie de modèle et de ne réintroduire que ce qui manque, et retire elle-même des fonctionnalités de Codex.
- **La « taxe du middle management »** : trop de règles bloquent l'agent, qui cherche la chaîne de validation ; si un agent semble bloqué, la première chose à chercher est une règle à retirer. C'est l'inverse du réflexe courant d'ajouter une consigne à chaque échec.
- **Un agent seul par défaut, des équipes pour les cas durs** : nuance par rapport à l'engouement multi-agents et aux comités d'agents ; OpenAI déconseille aussi d'attribuer des rôles aux agents et laisse l'orchestrateur s'organiser.
- **L'objectif stocké hors du contexte** : la commande `/goal` de Codex conserve l'objectif dans le harnais pour qu'il survive aux compactions du contexte, avec un critère de succès explicite qui arrête la boucle. Un détail de conception de harnais concret, cohérent avec la Performance Factory.

## 3. Résumé
L'article rapporte les conseils donnés par des ingénieurs d'OpenAI au DevDay Exchange de Paris pour mieux utiliser Codex et les agents de code.
1. **Donner un objectif vérifiable** : la commande `/goal` permet à l'agent de poursuivre sa mission tant qu'elle n'est pas terminée ; l'objectif est stocké par le harnais, hors du contexte, et survit aux compactions. Selon Pranav Deshpande, le modèle évalue lui-même où il en est ; il faut donc préciser l'objectif et le critère de succès. Exemple : migrer un module de paiement vers une nouvelle API, avec pour critère la réussite de tous les tests et l'absence d'appel à l'ancienne API.
2. **Plusieurs équipes d'agents en parallèle pour les problèmes complexes** : approches ou formulations différentes, partage des résultats pour éviter les doublons, création de nouvelles équipes quand une piste ouvre de nouvelles questions. L'exemple donné est le problème de Navier-Stokes, présenté comme résolu par OpenAI. Dominik Kundel nuance : pour le travail courant, un seul agent avec une tâche claire et un moyen de vérifier suffit, et mieux vaut ne pas attribuer de rôles.
3. **Éviter la « taxe du middle management »** : peu de règles, simples, et décrire le résultat attendu avec ses critères de réussite ; identifier le problème avant d'ajouter une règle, et chercher d'abord une règle à retirer quand l'agent bloque.
4. **Jeter ses workflows à chaque nouveau modèle** : les modèles gagnent en autonomie et ont moins besoin de guides ; OpenAI retire des fonctionnalités de Codex à chaque nouveau modèle. Conclusion de Deshpande : il faut parfois repartir de zéro.

## 4. Citations et noms
**Citations** :
- « Avec l'IA, il faut parfois mettre de côté ce qu'on croyait efficace et repartir de zéro. », Pranav Deshpande (OpenAI)
- « Taxe du middle management », expression de Dominik Kundel (OpenAI) pour l'effet d'un excès de règles sur les agents.

**Noms cités** :
- *OpenAI* : éditeur dont les ingénieurs donnent les conseils.
- *Codex* : agent de code d'OpenAI, support de tous les conseils.
- *Pranav Deshpande* : équipe developer marketing d'OpenAI ; objectif vérifiable et remise à plat des workflows.
- *Dominik Kundel* : équipe developer experience d'OpenAI ; un seul agent par défaut, peu de règles.
- *DevDay Exchange Paris* : événement d'OpenAI (fin octobre) où les conseils ont été présentés.
- *`/goal`* : commande de Codex qui fixe un objectif persistant à l'agent.
- *Navier-Stokes* : problème mathématique cité comme exemple de travail par équipes d'agents en parallèle.

## 5. Mots-clés
agents IA, harnais agentique, autonomie des agents, vérification, ingénierie du contexte

## Lecture CPO
- **Implications** :
  - Formuler les tâches confiées aux agents comme des objectifs avec critère de succès vérifiable (tests, absence d'appel à une API) : c'est une compétence de cadrage proche de la rédaction de critères d'acceptation.
  - Auditer régulièrement les fichiers de règles, skills et hooks des équipes : les élaguer à chaque nouveau modèle plutôt que les laisser s'accumuler comme une dette.
  - Ne pas investir par défaut dans des architectures multi-agents à rôles : un agent bien cadré suffit pour le travail courant.
- **Fiabilité** : parole d'éditeur sur son propre produit, rapportée par la presse ; aucune donnée ni mesure, seulement des recommandations et un exemple (Navier-Stokes) non détaillé dans l'article.
- **Maturité** : Tendance émergente : les principes (objectif vérifiable, peu de règles) convergent avec d'autres sources, mais le conseil de jeter ses workflows reste propre à OpenAI et non démontré.
- **Réutilisation** : post LinkedIn sur la « taxe du middle management » des agents (le parallèle avec les organisations humaines est direct) ; article OCTO sur la durée de vie des bonnes pratiques agentiques, avec la fiche Performance Factory ; atelier équipe produit sur la rédaction d'objectifs vérifiables.
