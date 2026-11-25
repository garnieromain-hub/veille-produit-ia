# Après les classements de tokens et les plafonds de dépense, Snowflake garde le plafond et apprend de ceux qui le dépassent

**Référence** : Matt Marshall, VentureBeat, 24 novembre 2026, article (fondé sur l'événement VentureBeat AI Impact de San Francisco du 12 novembre, sponsorisé par Western Governors University, et sur des travaux d'Atlassian, qui a payé du contenu sponsorisé sur VentureBeat), https://venturebeat.com/orchestration/after-token-leaderboards-and-spending-caps-snowflake-has-a-third-idea-keep-the-cap-then-learn-from-whoever-breaks-it

**Axe** : Investissement tech (Transformation des entreprises)

## 1. L'idée clé
Face à l'envolée des dépenses IA, ni le classement des salariés par consommation de tokens ni le plafond sec ne suffisent. Snowflake garde des budgets par salarié, mais traite chaque dépassement comme une piste : il va voir qui l'a dépassé, comprend le flux de travail, l'optimise et le transforme en compétence réutilisable pour tous.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Uber, budget IA et réglages des agents](2026-11-20-uber-budget-ia-reglages-agents-code.md) (maîtrise par des réglages par défaut centralisés), la fiche [IT Social, jetons moins chers](2026-11-24-itsocial-jetons-moins-chers-facture-ia.md) (le TBM Council juge les plafonds rigides contre-productifs) et la fiche [Atlassian State of Teams 2026](2026-10-16-atlassian-state-of-teams-2026.md) ; et au discours dominant qui oppose « encourager l'usage » et « contenir les coûts ».
- **Le dépassement de budget comme signal de découverte** : le plafond reste (un agent est un « labrador enthousiaste » capable de dépenser quelques milliers de dollars pour une réponse sans valeur), mais le dépassement déclenche un entretien, pas une sanction. Uber réglait les paramètres pour tous ; Snowflake cherche les usages à généraliser.
- **Un circuit pionnier vers compétence partagée** : 5 à 10 % des 2 500 ingénieurs sont des « pionniers » qui pilotent des équipes d'agents ; leurs flux utiles deviennent des skills réutilisables (revue de code par agents parallèles, bilan trimestriel tiré de Slack, Jira et des transcriptions commerciales). Exemple : un commercial dont l'agent régénérait ses skills à chaque rapport client ; l'équipe a optimisé le flux et l'a intégré à l'agent.
- **Des données Atlassian sur l'effet « superutilisateur »** : sur un hackathon interne (870 équipes), une équipe avec un superutilisateur (top 25 % d'usage dans sa fonction) a 18 points de plus de chances de dépasser la médiane ; en avoir deux n'apporte rien de plus. Un seul cas, volontaire, sans causalité établie.
- **Le pari des juniors** : 70 à 80 % des recrutements d'ingénieurs de Snowflake sont des juniors (moins de deux ans d'expérience), jugés plus à l'aise avec les flux natifs IA ; chez Atlassian, les jeunes diplômés sont 19 % plus souvent superutilisateurs. À contre-courant de la baisse d'environ 65 % des recrutements de débutants depuis 2019 dans 12 grandes entreprises tech (SignalFire).
- **La « pénalité de paresse »** : 40 % des 21-24 ans cachent leur usage de l'IA (29 % au-delà de 25 ans) ; déclarer son usage rend dix fois plus probable d'être jugé paresseux (30 % contre 3 %). L'effet disparaît presque dans les entreprises qui célèbrent l'usage de l'IA.

## 3. Résumé
L'article présente l'approche de Snowflake comme une troisième réponse à l'explosion des dépenses IA de 2026. La première a été le classement des salariés par usage de tokens (Amazon, Meta, OpenAI). La deuxième, le plafond : Uber, après avoir épuisé son budget annuel dès avril, limite chaque salarié à 1 500 $ par mois et par outil de code ; Atlassian donne des budgets mensuels et constate que ceux qui les atteignent sont souvent ses utilisateurs les plus inventifs. Will Allen, responsable produit de CoCo et CoWork chez Snowflake, défend le maintien du budget, car un agent insiste comme un labrador et peut dépenser beaucoup pour peu. Mais il va voir ceux qui dépassent pour comprendre leur usage, avec l'exemple du commercial et de son rapport HTML sur 30 jours de tickets, optimisé puis intégré à l'agent. Snowflake célèbre ces « rock stars » à tous les niveaux, créant une émulation qu'Allen appelle une « FOMO puissante ». L'article décrit ensuite les pionniers et leurs skills partagées, puis les travaux d'Atlassian (Molly Sands, Teamwork Lab) sur les superutilisateurs, en soulignant les limites de l'étude ; Sands se dit sceptique sur la formation classique et préfère changer les systèmes de travail. Vient le volet recrutement : 70 à 80 % de juniors chez Snowflake selon Vivek Raghunathan, stratégie analysée par un cas de Stanford GSB, face à Paul Bingham (WGU) qui préfère reconvertir les salariés existants. L'article aborde enfin la dissimulation de l'usage de l'IA et la « pénalité de paresse ». Il conclut sur l'angle mort : Snowflake ne sait pas chiffrer le ROI des flux découverts par ceux qui dépassent, ni dire si cela justifie le coût de les trouver ; il n'a pas non plus répondu sur la base de ses chiffres de recrutement.

## 4. Citations et noms
**Citations** :
- Un agent est comme un labrador enthousiaste qui ne lâche rien : on peut revenir et découvrir quelques milliers de dollars dépensés pour une réponse sans valeur (paraphrase de Will Allen, Snowflake, rapportée par l'article).
- L'émulation créée par la mise en avant des pionniers : une « FOMO puissante » (« powerful FOMO »), Will Allen.
- Les salariés se pénalisent entre eux pour leur honnêteté sur l'usage de l'IA (propos de Molly Sands, Atlassian, rapporté par l'article).

**Noms cités** :
- *Will Allen* : responsable produit de CoCo et CoWork chez Snowflake, source principale.
- *Vivek Raghunathan* : vice-président senior ingénierie de Snowflake, porte-parole du recrutement de juniors.
- *Molly Sands* : responsable du Teamwork Lab d'Atlassian, autrice des travaux sur les superutilisateurs et la pénalité de paresse.
- *Uber, Atlassian* : exemples de plafonds de dépense IA par salarié.
- *Amazon, Meta, OpenAI* : exemples de classements internes par usage de tokens.
- *Raj Joshi et Robert Burgelman (Stanford GSB)* : auteurs d'un cas de 2026 sur la stratégie de talents de Snowflake.
- *Paul Bingham (Western Governors University)* : contrepoint, préfère faire monter en compétences les salariés existants.
- *SignalFire* : source de la baisse d'environ 65 % des recrutements de débutants depuis 2019.

## 5. Mots-clés
FinOps, coûts des tokens, adoption IA, talents juniors, conduite du changement, mesure du ROI

## Lecture CPO
- **Implications** :
  - Garder des budgets IA par personne, mais instrumenter les dépassements : une alerte qui déclenche une conversation, pas un blocage ni une sanction.
  - Organiser une filière « pionnier vers skill partagée » : repérer les usages avancés, les optimiser, puis les industrialiser dans les agents et outils communs. C'est un travail produit sur les outils internes.
  - Rendre l'usage de l'IA visible et valorisé pour lever la « pénalité de paresse », sinon l'usage se cache et ne se diffuse pas.
  - Reposer la question du recrutement de juniors dans les équipes produit et tech, à la lumière de ces données, sans les tenir pour acquises.
- **Fiabilité** : récit construit à partir d'un événement du média, avec des intervenants d'entreprises qui promeuvent leurs pratiques (et leurs produits pour Snowflake) ; Atlassian a payé du contenu sponsorisé sur VentureBeat. L'article est honnête sur ses limites : étude Atlassian non causale et sur un seul hackathon, chiffres de recrutement non étayés, aucun ROI chiffré.
- **Maturité** : Signal faible : l'approche « apprendre des dépassements » n'est décrite que chez Snowflake, sans mesure de résultat ; les plafonds par salarié, eux, deviennent une tendance émergente.
- **Réutilisation** : article OCTO sur les trois réponses aux dépenses IA (classement, plafond, apprentissage), en regard d'Uber ; post LinkedIn « le dépassement de budget IA est un signal, pas une faute » ; table ronde sur la diffusion des usages (pionniers, skills, pénalité de paresse) en contrepoint des plaidoyers pour la formation.
