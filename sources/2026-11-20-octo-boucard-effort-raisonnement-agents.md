# Modèle et effort de raisonnement : trouver le bon équilibre pour vos agents

**Référence** : Bruno Boucard, OCTO Talks !, 19 novembre 2026 (date affichée dans la liste du blog ; l'en-tête de l'article indique 10/11/2026, sans doute la date de rédaction), article de bonnes pratiques, https://blog.octo.com/modele-et-effort-de-raisonnement--trouver-le-bon-equilibre-pour-vos-agents

**Axe** : IA appliquée au produit (Investissement tech)

## 1. L'idée clé
Le choix du modèle et le réglage de l'effort de raisonnement sont deux curseurs indépendants : l'effort règle l'intensité du travail, pas la capacité du modèle. Face à une réponse superficielle, on monte d'abord l'effort ; on change de modèle seulement quand le problème dépasse ce que le modèle sait faire. Réserver gros modèles et efforts élevés à la conception et au diagnostic, et des réglages légers à l'exécution, donne de la qualité sans exploser coût et latence.

## 2. Ce qui est nouveau
**Par rapport à** : la série de Bruno Boucard sur les harnais agentiques (OCTO, octobre 2026, citée en sources complémentaires), la fiche [Thoughtworks Radar vol. 35](2026-11-19-thoughtworks-radar-vol35.md) (modèle frontière par défaut en « Caution », routage entre modèles) et la fiche [OCTO Camus](2026-11-13-octo-camus-agent-ou-comite.md) (coût des comités d'agents).
- **Une grille à trois dimensions (rôle, modèle, effort)** : là où le Radar plaide pour le routage entre modèles, Boucard ajoute un troisième curseur, l'effort, et l'attribue agent par agent dans un système multi-agents.
- **Un exemple de découpage concret** : sur une modernisation applicative, inventaire des fichiers (modèle léger, effort faible), analyse des dépendances (intermédiaire, moyen), architecture cible et risques (puissant, élevé). C'est une règle d'allocation utilisable telle quelle, pas un principe général.
- **Les limites de l'effort explicitées** : ce n'est ni un budget strict de tokens ni une garantie de qualité proportionnelle, et les tokens de réflexion sont facturés même quand ils ne sont pas affichés.
- **Les budgets de tâches (bêta)** : un `task_budget` encadre le travail total d'une boucle agentique (minimum 20 000 tokens), comme indice de pilotage et non comme plafond ; `max_tokens` reste le garde-fou.

## 3. Résumé
L'auteur part du constat que la plupart des fournisseurs de modèles permettent désormais de régler l'effort de raisonnement, levier pour maîtriser tokens, coûts et adaptation à la complexité. Il file l'analogie du football : un joueur a un poste (le rôle de l'agent), un niveau (le modèle) et une intensité de jeu (l'effort) ; l'orchestrateur est l'entraîneur, et augmenter l'effort ne fait pas d'un petit modèle un grand. Il l'illustre par une modernisation applicative découpée en trois tâches de difficulté croissante. Il détaille ensuite les niveaux d'effort (low, medium, high, xhigh, max ; high par défaut sur la plupart des modèles, medium sur Opus 5.5 et Haiku 5.5) et montre, sur un cas de rétrodocumentation, qu'un effort faible limite les appels d'outils et fait reposer la réponse sur des hypothèses, tandis qu'un effort élevé multiplie les vérifications. Il distingue réflexion (capacité de raisonnement interne) et effort (son intensité), puis passe à la configuration dans l'API Messages (`output_config.effort`) et à deux façons de changer d'effort en cours de conversation : par requête, ou par message (bêta), qui préserve mieux le cache. En multi-agents, l'orchestrateur règle l'effort selon la responsabilité de chaque agent, pour éviter deux écueils : gaspiller sur les tâches simples, sous-dimensionner les décisions critiques. Suivent des bonnes pratiques (effort explicite, low pour le simple, medium comme point de départ, high et au-delà pour l'exigeant, mesurer, préserver le cache) et les budgets de tâches en bêta, non supportés dans Claude Code. Il conclut par l'analogie de l'étudiant qui concentre son effort sur son mémoire, là où il crée le plus de valeur.

## 4. Citations et noms
**Citations** :
- « Augmenter l'effort ne transforme donc pas un petit modèle en modèle plus puissant. », Bruno Boucard

**Noms cités** :
- *Bruno Boucard* : OCTO, auteur de la série sur les harnais agentiques et du billet « Plugin Modernization by Anthropic ».
- *Anthropic (API Messages, Opus 5.5, Haiku 5.5, Claude Code)* : la documentation et les paramètres sur lesquels s'appuie l'article (`output_config.effort`, `task_budget`, `max_tokens`).
- *Rôle, modèle, effort* : la grille à trois dimensions proposée pour dimensionner un agent.
- *Orchestrateur* : l'agent « entraîneur » qui attribue modèle et effort à chaque sous-agent.

## 5. Mots-clés
agents IA, coûts des tokens, harnais agentique, routage de modèles, qualité

## Lecture CPO
- **Implications** :
  - Pour une équipe qui construit un produit à base d'agents, le dimensionnement (modèle et effort par tâche) devient une décision de conception à documenter, au même titre que le prompt.
  - Le coût unitaire d'une fonctionnalité IA se pilote par tâche : mesurer qualité et tokens pour chaque niveau d'effort avant de figer le réglage.
  - Côté FinOps, l'effort est un levier de coût plus fin que le changement de modèle, mais sa facture (tokens de réflexion invisibles) doit être suivie.
- **Fiabilité** : praticien OCTO, sans intérêt commercial direct, mais article très adossé à la documentation d'un seul éditeur (Anthropic) ; aucune mesure propre publiée, les effets décrits sont qualitatifs. Fonctionnalités en bêta, donc susceptibles de changer.
- **Maturité** : Tendance émergente : le paramètre d'effort existe chez la plupart des fournisseurs, mais son usage raisonné agent par agent reste peu outillé et peu mesuré.
- **Réutilisation** : présentation client sur le coût des produits agentiques (grille rôle, modèle, effort) ; post LinkedIn (« monter l'effort avant de changer de modèle ») ; article OCTO croisant cette grille avec le routage multi-modèles (Thoughtworks, Databricks).
