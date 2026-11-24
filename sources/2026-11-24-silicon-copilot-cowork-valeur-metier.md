# Comment Microsoft calcule la « valeur métier » de Copilot Cowork

**Référence** : Clément Bohic, Silicon.fr, 19 novembre 2026, article (analyse de la méthodologie publiée par Microsoft), https://www.silicon.fr/data-ia-1372/copilot-cowork-valeur-metier-230518

**Axe** : Portefeuille numérique (Investissement tech)

## 1. L'idée clé
Le « gain métier » que le centre d'administration Microsoft 365 affiche pour Copilot Cowork repose sur un barème de minutes gagnées par type de tâche, construit à partir d'études hétérogènes, de correspondances et d'extrapolations. Il permet de quantifier l'usage, pas de prouver un retour sur investissement : il ignore la qualité, le temps de vérification et les coûts de correction.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Thelliez sur le responsable du ROI IA](2026-11-20-jdn-thelliez-responsable-roi-ia.md) (mesurer la performance de bout en bout, pas le temps gagné), la fiche [Babinet et Champain sur la productivité](2026-11-20-itforbusiness-babinet-champain-productivite-ia.md), la fiche [NBER sur les données d'entreprise](2026-11-13-nber-firm-data-on-ai.md) et la fiche [SAP Autonomous Enterprise](2026-11-23-cio-sap-autonomous-enterprise-caio.md) (l'éditeur reconnaît que le lien dépense-valeur reste à construire) ; au discours dominant qui reprend tel quel les « minutes gagnées » des éditeurs.
- **La mesure de valeur intégrée au produit de l'éditeur** : Microsoft ne publie plus seulement des études, il affiche un indicateur de valeur dans la console d'administration. C'est l'éditeur qui fixe le barème avec lequel le client jugera son achat.
- **Le barème décortiqué catégorie par catégorie** : huit catégories de tâches, chacune avec une valeur basse, haute et « typique » (par exemple 67 minutes pour l'analyse et la recherche, 24 pour la création de documents, environ 8 par e-mail, environ 31 par réunion, 5 pour l'assistance générale), et la source de chaque chiffre.
- **Des chiffres fragiles mis au jour** : la valeur réunions vient d'une étude sur 57 employés ; la valeur workflows d'une étude Forrester commandée par Microsoft (200 heures par an, ramenées à 25 minutes par tâche par hypothèse) ; la valeur code multiplie un gain mesuré par trois étapes supposées. L'article montre la mécanique, là où les autres fiches critiquaient le principe.
- **Les angles morts nommés** : ni qualité des résultats, ni temps de vérification, ni coûts de correction ou de supervision, soit exactement ce que la fiche Arquié pointait comme coût caché de l'humain dans la boucle.

## 3. Résumé
L'article part d'une nouvelle fonctionnalité du centre d'administration Microsoft 365 qui estime la valeur métier produite par Cowork, le mode agentique de Copilot, et de la méthodologie que Microsoft a publiée pour la justifier. Le point de départ est l'expérimentation du gouvernement britannique (mi-2025, trois mois, 20 000 licences dans 12 organisations) : environ 26 minutes gagnées par jour et par personne. Microsoft définit ensuite huit catégories de tâches, avec pour chacune une fourchette en minutes, que l'auteur détaille dans l'ordre :
1. Analyse et recherche : 67 minutes typiques (moyenne de cinq correspondances avec des catégories O*NET d'une étude de Stanford de 2025), 92 en haut, 30 en bas (étude McKinsey 2023 de 25 à 40 % de gain appliquée à une tâche d'une heure).
2. Création de documents : 24 minutes typiques, soit 6,1 minutes par interaction (étude interne sur 72 186 utilisateurs de Word) multipliées par quatre interactions supposées.
3. E-mails : environ 8 minutes typiques (étude NBER 2025, 2 heures par semaine divisées par 14,5 réponses), 3 en bas (étude MIT 2023).
4. Réunions : environ 31 minutes typiques, tirées d'une étude sur 57 employés qui rattrapent une réunion Teams de 35 minutes (11 min 13 s avec Copilot, 42 min 34 s sans).
5. Communication : 2 minutes en bas (14 minutes par jour réparties sur 7 interactions, Work Trend Index 2024).
6. Workflows spécialisés : 25 minutes typiques, dérivées d'une étude Forrester commandée par Microsoft sur Power Automate (200 heures par an, soit 32 minutes par automatisation, réduites à 25 car une tâche Cowork compte moins d'étapes).
7. Code : environ 54 minutes typiques (18 minutes gagnées sur une tâche de 70, tirées d'une étude sur 4 867 développeurs, multipliées par trois étapes), 21 en bas (étude GitHub Copilot 2023 sur 95 développeurs), 100 en haut (cinq activités à 20 minutes).
8. Assistance générale : 5 minutes typiques (étude NBER 2025, +14 % de productivité chez des agents de service client).
L'auteur conclut sur les réserves : sources hétérogènes, échantillons parfois très petits, valeurs issues de correspondances et d'hypothèses d'usage, et aucune prise en compte de la qualité, de la vérification ou de la supervision. Pour une DSI, le cadre permet de quantifier les usages, mais un vrai ROI suppose de confronter ces estimations à ses propres données, processus et coûts.

## 4. Citations et noms
**Citations** : rien de notable (la source accessible ne permet pas de restituer de citation exacte fiable ; les propos sont paraphrasés dans le résumé).

**Noms cités** :
- *Microsoft, Copilot Cowork, Microsoft 365* : éditeur et produit dont la valeur est calculée ; Cowork est le mode agentique de Copilot.
- *Gouvernement britannique* : expérimentation de 2025 (26 minutes par jour), point de départ du barème.
- *Stanford* : étude de 2025 fondée sur les catégories O*NET, source des valeurs hautes.
- *O*NET* : base de métiers et de tâches du département américain du Travail.
- *McKinsey* : étude de 2023 utilisée pour la valeur basse de l'analyse.
- *NBER* : études de 2025 sur les e-mails et le service client.
- *MIT* : étude de 2023 sur les réponses rapides.
- *Work Trend Index (2023, 2024)* : études Microsoft utilisées pour les réunions et la communication.
- *Forrester* : étude commandée par Microsoft sur Power Automate.
- *GitHub Copilot* : étude de 2023 sur 95 développeurs, valeur basse du code.
- *Power Automate, Word, Teams* : produits Microsoft dont les études servent de référence.

## 5. Mots-clés
mesure du ROI, productivité, gain de temps, agents IA, budgets IT, contrepoint

## Lecture CPO
- **Implications** :
  - Ne pas reprendre la « valeur métier » de la console Microsoft dans un business case ou un bilan d'investissement : c'est un barème d'éditeur, à remplacer par des mesures sur ses propres processus.
  - Si on l'utilise, retenir les valeurs basses et déduire le temps de vérification et de correction, que l'indicateur ignore.
  - Pour le pilotage de portefeuille, mesurer le résultat de bout en bout (délai, qualité, coût du processus) plutôt que les minutes gagnées par tâche, qui ne se convertissent pas forcément en capacité libérée.
  - Exiger des éditeurs la méthode de calcul de tout indicateur de valeur intégré à leurs consoles avant de l'accepter en comité.
- **Fiabilité** : journaliste spécialisé qui dissèque une méthodologie publiée par l'éditeur ; l'analyse est critique et sourcée, mais plusieurs valeurs hautes ou basses ne sont pas chiffrées dans l'article. Les études sous-jacentes sont de qualité inégale (échantillons de 57 ou 95 personnes, étude commandée par Microsoft, études internes).
- **Maturité** : Tendance émergente : les éditeurs intègrent des indicateurs de valeur à leurs produits, mais leur méthode reste fragile et contestée.
- **Réutilisation** : article OCTO sur la mesure de la valeur de l'IA (« qui fixe le barème ? »), avec les fiches Thelliez et SAP ; post LinkedIn sur les 57 employés derrière les 31 minutes gagnées par réunion ; présentation client DSI ou contrôle de gestion sur la construction d'un business case Copilot.
