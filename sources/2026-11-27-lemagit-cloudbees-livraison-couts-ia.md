# Les outils IA accélèrent la livraison logicielle… et la hausse des coûts IT (étude)

**Référence** : Gaétan Raoul, LeMagIT, 26 novembre 2026, article de reprise d'une enquête (Cloudbees, « State of Code Abundance », Europe, réalisée par TrendCandy), https://www.lemagit.fr/actualites/366655558/Les-outils-IA-accelerent-la-livraison-logicielle-et-la-hausse-des-couts-IT-etude

**Axe** : Investissement tech (IA appliquée au produit)

**Avertissement** : l'enquête est commandée par Cloudbees, éditeur de pipelines CI/CD qui vend précisément de la gouvernance automatisée de la livraison. Le journaliste le signale lui-même.

## 1. L'idée clé
Les outils de code IA accélèrent la livraison, mais ils font monter les coûts de livraison, et les entreprises les mesurent mal : elles budgètent les licences et les tokens, rarement le temps de relecture, la correction ou la conformité. Résultat : moins on mesure finement, plus on croit gagner, au moment où les comex vont exiger un ROI.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [LeadDev sur la revue de code](2026-11-25-venturebeat-leaddev-revue-code-agents.md) (la revue comme goulot, chiffrée aux États-Unis et en Europe), la fiche [Mehta sur la facture IA](2026-11-25-cio-mehta-facture-ia-gouvernance.md) (le coût se déplace de l'écriture vers la gouvernance) et la fiche [Uber](2026-11-20-uber-budget-ia-reglages-agents-code.md) (budget IA épuisé). Le diagnostic est connu ; l'apport est une mesure européenne du coût et de son périmètre.
- **Le périmètre budgétaire chiffré** : 83 % incluent licences et tokens dans le coût de l'IA, 38 % seulement le temps de relecture et 24 % la conformité ; parmi ceux qui voient la revue augmenter, 60 % n'intègrent pas le temps des développeurs. C'est la preuve chiffrée de l'intuition de Mehta.
- **Des montants par entreprise** : 40 % dépensent plus de 500 000 euros par an pour outiller leurs développeurs en IA, environ 22 % plus d'un million ; 64 % constatent une hausse des coûts de livraison. Les autres fiches parlaient de tokens, pas d'enveloppes annuelles européennes.
- **Le paradoxe de la mesure** : 44 % disent que l'IA a réduit le coût de mise en production, 28 % qu'elle l'a augmenté, mais seulement 43 % savent évaluer le coût total ; Cloudbees en conclut que les moins outillés pour mesurer perçoivent le plus de gains.
- **L'échéance ROI** : près de 70 % des DSI français, allemands et britanniques s'attendent à ce que le comex exige un ROI d'ici fin 2027, 43 % se disent confiants pour le démontrer.
- **Un écart franco-allemand-britannique** : la souveraineté restreint le choix d'outils pour 64 % des Allemands et 58 % des Français, contre 41 % des Britanniques.

## 3. Résumé
L'article reprend l'enquête européenne de Cloudbees, menée par TrendCandy en octobre 2026 auprès de 450 responsables IT et logiciel (150 en France, au Royaume-Uni et en Allemagne), issus d'équipes DevOps d'ETI et de grandes entreprises (61 % dans des groupes de plus de 1 000 salariés). Il part de l'accélération : 71 % jugent que l'IA a accéléré le développement, 22 % seulement nettement. Puis la contrepartie : pour 34 %, vérifier le code prend une heure ou plus par heure gagnée à l'écriture (58 % moins d'une heure), 46 % voient le code de mauvaise qualité augmenter dans leurs dépôts, 32 % seulement une hausse de qualité. La traçabilité recule pour 53 % (facilitée pour 19 %), et 52 % seraient pourtant prêts à laisser des agents agir en autonomie. Les priorités restent la sécurité (vulnérabilités 66 %, fuites de données 52 %) ; 75 % disent avoir renforcé la gouvernance de leurs chaînes, et 63 % estiment que le volume de code généré dépasse la capacité de revue humaine, d'où l'appel à automatiser (gouvernance automatisée prioritaire pour 41 %, derrière la sécurité, 61 %, et les tests continus, 52 %). Le journaliste rappelle alors le biais du commanditaire, positionné sur ces enjeux comme GitHub, GitLab ou Anthropic. Vient le volet coûts : enveloppes annuelles (40 % au-delà de 500 000 euros), hausse des coûts de livraison pour 64 %, causes non expliquées par Cloudbees (les analystes citent l'inflation et l'IA intégrée aux outils DevOps). 65 % pensent que les outils IA pèsent au plus 10 % du budget de livraison, mais les postes qui grimpent sont le cloud (51 %), la revue (46 %) et la correction (38 %), et 52 % voient le coût de correction du code défectueux augmenter. L'article termine sur le ROI attendu par les comex d'ici fin 2027, une valeur métier jugée établie par 43 % et contestée par autant, et les écarts nationaux sur la souveraineté et l'AI Act (43 % des Français jugent qu'il encadre sans freiner, 29 % des Britanniques).

## 4. Citations et noms
**Citations** : rien de notable (l'article ne cite personne nommément ; il paraphrase le rapport).

**Noms cités** :
- *Cloudbees* : éditeur de pipelines CI/CD, commanditaire de l'enquête.
- *TrendCandy* : institut qui a réalisé le sondage en octobre 2026.
- *State of Code Abundance* : titre du rapport (écrit « Sate » par coquille dans le chapeau).
- *GitHub, GitLab, Anthropic* : éditeurs cités comme positionnés sur les mêmes enjeux de gouvernance du code IA.
- *AI Act* : règlement européen, vu par 43 % des Français comme un cadre qui ne freine pas l'adoption.

## 5. Mots-clés
budgets IT, mesure du ROI, coût total de possession, vérification, goulot d'étranglement, enquête

## Lecture CPO
- **Implications** :
  - Avant la demande de ROI du comex, élargir le périmètre du coût de l'IA de livraison : temps de revue, correction, conformité et cloud, pas seulement licences et tokens.
  - Se méfier des gains déclarés par les équipes qui ne mesurent pas le coût total : l'enquête suggère qu'ils sont surestimés.
  - Mettre la capacité de revue et la traçabilité (qui a poussé quoi en production) dans les critères avant d'ouvrir l'autonomie aux agents.
  - En contexte français ou allemand, intégrer la contrainte de souveraineté dans le choix des outils dès l'arbitrage budgétaire.
- **Fiabilité** : enquête d'éditeur intéressé (Cloudbees vend la gouvernance automatisée que l'étude justifie), échantillon déclaré (450 répondants, trois pays), rapport PDF public. Données déclaratives ; causes de la hausse des coûts non analysées ; un passage sur le ROI mal formulé dans l'article. Le journaliste signale le biais.
- **Maturité** : Tendance émergente : la hausse des coûts cachés du code IA est documentée par plusieurs enquêtes de novembre, mais la mesure du coût total reste minoritaire (43 %).
- **Réutilisation** : post LinkedIn « 83 % comptent les tokens, 38 % le temps de relecture » ; présentation client DSI sur le business case de l'IA de développement (périmètre de coût complet) ; article OCTO sur le coût total de l'usine logicielle IA, avec LeadDev et Mehta.
