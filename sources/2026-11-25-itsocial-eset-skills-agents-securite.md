# Skills d'agents, des entités mouvantes après leur installation

**Référence** : Benoît Grunemwald (expert en cybersécurité, ESET France), IT Social, 24 novembre 2026, tribune, https://itsocial.fr/contenus/tribunes/skills-dagents-des-entites-mouvantes-apres-leur-installation/

**Axe** : IA appliquée au produit

## 1. L'idée clé
Un agent d'IA agit avec les droits de son utilisateur : la sécurité porte donc sur ce qu'il peut faire, plus seulement sur la justesse de ses réponses. Les skills qui étendent ses capacités évoluent après leur installation, si bien qu'un contrôle ponctuel ne suffit pas : il faut épingler les versions, limiter les droits et surveiller en continu.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [OpenRouter et les vols de conversations](2026-11-24-solutions-numeriques-openrouter-vols-conversations.md) (le risque dans la chaîne d'inférence), la fiche [Decathlon, IA et cybersécurité](2026-11-23-itforbusiness-decathlon-ghilain-ia-cybersecurite.md) (injection de prompt comme risque de conception) et la fiche [Jain, agents et plateformes](2026-11-24-cio-jain-agents-plateformes-sap-servicenow.md) (le standard Agent Skills) ; plus largement, le discours dominant qui traite la sécurité de l'IA comme un problème de fournisseur de modèle ou de fuite de données.
- **La skill comme maillon mouvant de la chaîne d'approvisionnement** : une skill peut changer par mise à jour silencieuse ou ne révéler une intention malveillante que plusieurs étapes plus tard. La vérification à l'installation, pratique habituelle pour un logiciel, ne suffit plus.
- **Des chiffres sur le catalogue de skills** (ESET, voir Fiabilité) : 33 % des skills examinées communiquent avec internet sans contrôle, 6 % chargent des identifiants ; la part de skills suspectes passe de 16,7 % en mars à moins de 2,8 % en mai, mais par dilution dans un catalogue qui grossit, pas par disparition.
- **La règle de la « trifecta »** : accès à des données sensibles, exposition à des contenus extérieurs et capacité d'agir vers l'extérieur ; retirer l'une des trois réduit fortement le risque. C'est une grille de conception simple, utilisable par une équipe produit.
- **La dérive sémantique sans attaquant** : une consigne en langage naturel mal interprétée (écarter les médias « généralistes » d'une veille finit par retirer tous les médias) se propage dans une chaîne multi-agents. Ce risque d'usage, hors cybersécurité au sens strict, est rarement traité.
- **Méfiance envers les skills « gardiennes »** : les skills de sécurité fondées sur des signatures et des mots-clés donnent un faux sentiment de protection.

## 3. Résumé
La tribune part d'un changement de nature : les agents planifient, naviguent et exécutent des actions avec les droits de leur utilisateur. Elle s'arrête d'abord sur les skills, fichiers d'instructions qui étendent l'agent : chaque bibliothèque ou service appelé est un point de compromission possible, et une skill peut évoluer après installation. L'auteur cite la skill « Credit Claw », capable d'effectuer des achats, et les chiffres d'ESET Research (33 % de skills qui communiquent avec internet sans contrôle, part de skills suspectes tombée de 16,7 % à moins de 2,8 % entre mars et mai, par dilution). Il recommande versions épinglées, moindre privilège et surveillance des changements, et met en garde contre les skills de sécurité à base de signatures. Deuxième risque, l'injection indirecte : des instructions cachées dans un ticket, une facture PDF, un dépôt de code, un courriel (texte blanc sur blanc, caractères invisibles) ou une page web. Il propose la « trifecta » : retirer à l'agent l'accès aux données sensibles, l'exposition aux contenus extérieurs ou la capacité d'agir vers l'extérieur. Troisième risque, les identifiants (6 % des skills en chargent) : coffre de secrets plutôt que fichier en clair, droits limités à la tâche et à sa durée, inventaire des agents, authentification forte de leurs pilotes. Quatrième risque, la dérive sémantique, illustrée par l'exemple de la veille qui retire tous les médias : relire les consignes sensibles, faire reformuler l'agent, vérifier un premier résultat, surveiller tâches planifiées et dépenses. La conclusion fait de l'utilisateur la première ligne de défense, rappelle que 40 % des entreprises n'ont pas de politique d'usage de l'IA (indice ESET, 4 400 décideurs de PME), et présente le module de sécurité IA d'ESET PROTECT ainsi que deux modules annoncés.

## 4. Citations et noms
**Citations** : rien de notable (la tribune ne contient pas de formule courte réutilisable ; ses recommandations sont citées dans le résumé).

**Noms cités** :
- *Benoît Grunemwald* : auteur, expert en cybersécurité chez ESET France.
- *ESET* : éditeur de sécurité, source de tous les chiffres et vendeur des solutions présentées en fin de tribune.
- *ESET Research, « Too big to ignore? The security crisis brewing in AI agent platforms »* (20 mars) : source des 33 %.
- *ESET Threat Report H1 2026* : source de l'évolution de la part de skills suspectes (16,7 % puis moins de 2,8 %).
- *ESET SMB Cyber Readiness Index 2026* : enquête auprès de 4 400 décideurs de PME, source des 40 % sans politique d'usage de l'IA.
- *ESET PROTECT, AI Observability, AI Secure Relay* : module de sécurité IA disponible depuis le 30 septembre et deux modules annoncés sans date.
- *Credit Claw* : skill capable d'effectuer des achats, exemple du pouvoir d'action des agents.
- *Amazon, Shopify* : cités dans le propos sur les agents qui achètent.
- *Trifecta* : grille de risque à trois conditions (données sensibles, contenus extérieurs, capacité d'agir vers l'extérieur).
- *Dérive sémantique* : mauvaise interprétation d'une consigne en langage naturel, amplifiée dans les chaînes multi-agents.

## 5. Mots-clés
agents IA, sécurité, chaîne d'approvisionnement logicielle, autonomie des agents, gouvernance IA

## Lecture CPO
- **Implications** :
  - Pour tout produit agentique, appliquer la « trifecta » dès la conception : décider explicitement laquelle des trois capacités on retire à l'agent.
  - Traiter les skills et connecteurs comme des dépendances logicielles : versions épinglées, revue des mises à jour, droits minimaux, inventaire.
  - Prévoir dans le produit des garde-fous contre la dérive sémantique : reformulation de la consigne par l'agent, validation d'un premier résultat, plafonds de dépenses.
  - Côté organisation, la politique d'usage ne suffit pas : il faut une surveillance des actions des agents, ce qui suppose un responsable et un budget.
- **Fiabilité** : tribune d'un éditeur de sécurité, qui conclut sur ses propres produits (ESET PROTECT et deux modules annoncés) ; intérêt commercial direct. Tous les chiffres viennent d'ESET, avec des sources nommées mais un périmètre d'analyse non précisé pour les skills (nombre examiné, plateformes). Les recommandations restent génériques et valables indépendamment de l'éditeur.
- **Maturité** : Tendance émergente : la sécurité des skills et l'injection indirecte deviennent un sujet de gouvernance à mesure que les agents passent en production, mais les pratiques ne sont pas stabilisées.
- **Réutilisation** : présentation client sur la conception d'agents (grille trifecta, cycle de vie des skills) ; table ronde sur la gouvernance des agents, avec les fiches OpenRouter et Decathlon ; post LinkedIn sur la dérive sémantique (« votre agent n'a pas été piraté, il vous a mal compris »). Citer ESET comme source intéressée.
