# Lean, AI et Delivery Tech : j'ai observé le futur du développement

**Référence** : Nicolas Ploquin, OCTO Talks !, 16 novembre 2026, article (retour d'observation terrain), https://blog.octo.com/lean-ai-et-delivery-tech-j'ai-observe-le-futur-du-developpement

**Axe** : IA appliquée au produit (Product management)

## 1. L'idée clé
L'IA ne remplace pas les disciplines Lean, elle les rend indispensables : elle amplifie les bonnes pratiques comme les défauts. Là où un standard explicite existe, elle produit du « conforme » ; sans standard, elle produit du « plausible ».

## 2. Ce qui est nouveau
**Par rapport à** : les retours OCTO de Claude Camus sur les agents ([fiche](2026-11-13-octo-camus-agent-ou-comite.md)), la fiche [Uber sur le prototypage IA](2026-10-16-uber-prototypage-ia.md) et le discours dominant selon lequel l'IA accélère le développement par elle-même.
- **Un cas d'équipe produit complète, pas d'un individu** : une petite équipe refait une application web importante en quelques semaines, observée en gemba ; Camus documentait surtout son propre travail avec agents.
- **Séparer specs et changes pour garder l'écart visible** : les specs (état actuel du produit) sont mises à jour par les développeurs avec leur IA, jamais par le PM ; les changes (une évolution par fichier) sont écrits par le PM. Une réponse concrète au risque que l'IA documente le code et masque l'écart entre intention et réalité.
- **Les agents calqués sur les anciens rôles ne marchent pas** : des agents « PO » ou « dev » rapportent peu, l'équipe a supprimé les rôles étanches ; la Lead Tech co-écrit les changes avec le PM. Cela rejoint la fusion des rôles annoncée par [Cagan](2026-11-13-svpg-ai-future-product-role.md), mais observée sur le terrain.
- **Ce qui perd sa pertinence** : estimations, roadmap à un an, user stories et pair programming, au profit du trunk-based development et du pilotage de la consommation de tokens.

## 3. Résumé
L'auteur observe l'équipe de Sara, Lead Tech dans une grande entreprise tech, qui redéveloppe une application web importante avec une petite équipe ; il présente ce témoignage comme un retour d'expérience, pas comme une preuve. Premier constat : le dépôt de code devient la source de vérité, avec la vision produit, les personas, les jobs to be done, les règles métier et un glossaire de termes bannis, que les agents lisent avant d'agir ; les pratiques de Sara sont formalisées en standards Lean intégrés comme skills. Des semaines de cadrage permettent ensuite un changement en cinq minutes, ou une modification de dix mille lignes en une heure. Deuxième constat, l'autonomation (Jidoka) : l'IA signale les écarts si on lui impose de ne rien inventer et de marquer ce qui est sourcé ; contre-exemple, avant que les profils soient définis, un utilisateur a pu accéder à un espace non autorisé sans alerte. Troisième, le paradoxe du système aveugle, résolu par la séparation specs / changes. Quatrième, flux et stock : quinze changes en attente forment un stock, chacun travaille en parallèle avec son IA, ce qui réduit la collaboration ; les rôles étanches et les agents qui les imitent sont abandonnés, et les tokens deviennent un sujet de pilotage (deux profils de gros consommateurs : ceux qui livrent beaucoup, et ceux qui consomment autant sans livrer). Cinquième, le développeur devient expert métier, ce qui rend la spécialisation par domaine plus précieuse. L'auteur conclut prudemment : la prouesse est réelle, mais la mesure de la qualité reste à construire (les tests fonctionnels remplacent la couverture unitaire, en cours), et il se demande si l'on développe les personnes ou si l'on délègue jusqu'à notre compréhension.

## 4. Citations et noms
**Citations** :
- « Retirez-le, et elle produit du plausible ; donnez-le-lui, et elle produit du conforme (à vos standards). », Nicolas Ploquin
- « L'IA respecte le Jidoka uniquement si un standard se tient derrière elle. », Nicolas Ploquin
- « Si tu ne sais pas, tu n'inventes pas ! », règle du référentiel de l'équipe

**Noms cités** :
- *Sara* : Lead Tech observée, source principale du retour d'expérience.
- *Jidoka, autonomation, gemba* : concepts Lean (arrêt sur anomalie, observation sur le terrain) appliqués au travail avec IA.
- *Trunk-based development* : cible de l'équipe pour réduire le stock de changes.
- *Jobs to be done, personas* : artefacts produit versionnés dans le dépôt pour les agents.

## 5. Mots-clés
agents IA, retour d'expérience, lean, organisation produit, qualité, coûts des tokens

## Lecture CPO
- **Implications** :
  - Mettre la connaissance produit (vision, règles métier, glossaire) dans le dépôt, versionnée, pour que les agents la lisent : c'est un travail de PM.
  - Séparer ce que le PM demande (changes) de ce que le produit est (specs) pour garder l'écart visible.
  - Ne pas reproduire l'organigramme dans les agents : un « agent PO » n'apporte pas grand-chose.
  - Garder un indicateur de tokens par personne relié à ce qui est livré.
- **Fiabilité** : praticien OCTO, un seul cas anonymisé, observé par l'auteur ; aucun chiffre de performance globale, ce que l'auteur reconnaît. Intérêt : OCTO vend du conseil Lean et delivery, et la thèse (le Lean devient indispensable) sert cette offre.
- **Maturité** : Signal faible : un cas observé, une pratique (specs / changes) prometteuse mais non généralisée.
- **Réutilisation** : article OCTO croisé avec Thoughtworks (« human-in-the-loop theater ») et Camus ; table ronde « Le PM écrit-il encore des user stories ? » ; présentation client sur le repo comme source de vérité produit.
