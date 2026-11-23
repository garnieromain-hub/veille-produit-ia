# Giving its AI more to read made T-Mobile's answers worse

**Référence** : Sean Michael Kerner, VentureBeat, 20 novembre 2026, article (retour d'expérience présenté à l'Agentic Infrastructure Stack Summit de VentureBeat en octobre, et enquête VB Pulse), https://venturebeat.com/orchestration/giving-its-ai-more-to-read-made-t-mobiles-answers-worse

**Axe** : IA appliquée au produit

## 1. L'idée clé
Donner plus de contexte à un agent ne le rend pas meilleur : chez T-Mobile, charger toute la documentation dans la fenêtre de contexte a dégradé les réponses, et un graphe de connaissances s'est révélé trop lent en appel client. Ce qui marche, c'est un contexte précis, filtré avant d'atteindre le modèle, choisi selon le temps dont on dispose pour le chercher.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Cutler TBM 452](2026-11-19-cutler-tbm-452-contexting.md) (critique du « tout écrire pour l'IA »), la fiche [Ploquin (OCTO)](2026-11-19-octo-ploquin-lean-ia-delivery.md) (partage de contexte comme pratique) et le discours dominant selon lequel les grandes fenêtres de contexte rendent le tri inutile.
- **Un échec documenté en production** : la documentation de support complète contenait des consignes contradictoires qui envoyaient les agents sur de fausses pistes. Cutler critiquait le tout-explicite par la théorie ; ici c'est un service client à grande échelle qui le constate.
- **La solution la plus simple a gagné** : une table clé-valeur qui associe les formulations fréquentes des clients à l'étape suivante, mise à jour au fil des nouvelles formulations, plus un agent orchestrateur qui confirme l'intention et route. Contrepoint aux architectures de graphe présentées comme la cible.
- **Le choix d'architecture dépend du temps disponible** : Uber trouve une table en 38 secondes avec son graphe de contexte (plus de 20 minutes sans), parce que ses agents travaillent en ingénierie, pas en appel en direct. Le même outil réussit ou échoue selon la latence tolérée.
- **Un juge LLM sur chaque session** : il signale réponses fausses et clients mécontents pour revue humaine ; il a repéré une musique d'attente entièrement inventée par le modèle, qu'il a fallu deux semaines pour expliquer.
- **Des chiffres sur les erreurs de contexte (VB Pulse)** : 78 % des 97 répondants ont relié au moins une réponse fausse mais assurée à un contexte métier manquant ou incohérent en six mois ; dans 12 % des cas les plus graves, un chiffre faux a atteint un rapport financier, réglementaire ou de conseil d'administration. Seuls 10 % misent surtout sur le chargement massif dans la fenêtre de contexte.

## 3. Résumé
L'article ouvre sur la première tentative de T-Mobile : charger toute la documentation de support dans un modèle à grande fenêtre de contexte. Selon le DSI Jeff Simon, cela « n'a pas marché du tout », car les documents se contredisaient. Deuxième essai, un graphe de connaissances : trop lent à parcourir, et les agents s'y perdaient quand ils comprenaient mal la demande. Troisième essai, retenu : une table clé-valeur « très basique » mais rapide et extensible, avec un orchestrateur qui confirme l'intention et passe la main à l'agent qui porte le contexte de ce parcours. T-Mobile orchestre des modèles plutôt que d'en entraîner, retire le contenu non pertinent avant qu'il n'atteigne le modèle, autorise des actions limitées (achat d'un forfait data international) avec vérification de l'intention, et fait tourner un petit juge LLM sur chaque session, au prix d'un surcoût assumé. Anecdote : ce juge a repéré une musique d'attente que T-Mobile ne diffuse pas, générée par le modèle pendant ses appels d'outils ; le prompt interdit désormais de l'halluciner. L'auteur élargit avec l'enquête VB Pulse d'octobre (erreurs dues au contexte, modes de détection : contrôles automatiques 57 %, revue d'experts 55 %, alertes 52 %, clients 19 %). Il oppose Adobe, qui vise un contexte précis plutôt que maximal (politiques de consentement UE et US séparées, historique de campagnes montrant que la livraison gratuite bat une remise de 20 % pour les clients fidèles), avec un modèle moins cher pour préparer le contexte, et Uber, dont le graphe fonctionne parce que le temps n'est pas compté. Il termine sur quatre questions à se poser : quels documents se contredisent, détecterait-on une réponse fausse, qui possède la table ou le graphe, combien de temps le client peut-il attendre.

## 4. Citations et noms
**Citations** :
- « Ça n'a pas marché du tout. » (« didn't work at all »), Jeff Simon, T-Mobile, à propos du chargement de toute la documentation
- « Complètement inventée. » (« completely invented »), Jeff Simon, à propos de la musique d'attente générée par le modèle

**Noms cités** :
- *Jeff Simon* : DSI de T-Mobile, qui raconte les trois architectures successives.
- *T-Mobile* : opérateur américain, agents de service client en chat et en voix.
- *Anjul Bhambhri* : SVP ingénierie d'Adobe, défend le contexte précis plutôt que maximal.
- *Adobe CX Enterprise Coworker* : agent marketing d'Adobe, pipeline de contexte (amorce, préchargement, fusion et classement).
- *Uber AI Context Graph* : graphe de contexte décrit sur le blog d'ingénierie d'Uber le 27 août, contre-exemple où le graphe réussit.
- *VB Pulse* : enquête de VentureBeat d'octobre 2026 sur les couches de contexte agentiques (97 répondants).
- *Juge LLM* : petit modèle qui évalue chaque session pour déclencher une revue humaine.

## 5. Mots-clés
agents IA, ingénierie du contexte, evals, qualité, retour d'expérience, hallucinations

## Lecture CPO
- **Implications** :
  - Avant de donner « tout le contexte » à un agent, faire l'inventaire des contradictions dans la documentation : c'est un travail de contenu, à confier à un propriétaire, pas un réglage technique.
  - Choisir l'architecture de contexte selon la latence tolérée par l'usage (appel client en direct ou tâche d'ingénierie), et non selon la mode.
  - Budgéter un juge automatique sur chaque session pour un agent en contact client : c'est un coût récurrent, mais c'est lui qui détecte ce que les clients ne signalent pas (19 % seulement des erreurs repérées par eux).
  - Nommer qui possède la table, l'index ou le graphe : sans propriétaire, le contexte se périme.
- **Fiabilité** : média tech, témoignage d'un DSI sur scène lors d'un événement organisé par le média, croisé avec une enquête propriétaire de petite taille (97 répondants, méthode non détaillée). Adobe et Uber parlent de leurs propres produits ou outils.
- **Maturité** : Tendance émergente : l'ingénierie du contexte devient un sujet de production, avec les premiers retours chiffrés d'échecs.
- **Réutilisation** : post LinkedIn « T-Mobile a donné plus à lire à son IA : elle a moins bien répondu » ; table ronde « Faut-il tout écrire pour les agents ? » avec Cutler et Ploquin ; présentation client sur la conception d'agents de service client (contexte, juge, propriétaire).
