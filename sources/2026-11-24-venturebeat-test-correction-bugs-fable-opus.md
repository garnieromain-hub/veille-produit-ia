# Claude Fable 5.2 cost three times as much as Opus 5.5 for nearly the same results in a VentureBeat bug-fixing test

**Référence** : Sean Michael Kerner, VentureBeat, 23 novembre 2026, article (test comparatif conduit par la rédaction), https://venturebeat.com/orchestration/claude-fable-5-2-cost-three-times-as-much-as-opus-5-5-for-nearly-the-same-results-in-a-venturebeat-bug-fixing-test

**Axe** : IA appliquée au produit (Investissement tech)

> **Conflit d'intérêts** : cette fiche a été rédigée par un modèle Claude, de la même famille que deux des modèles testés (Fable 5.2 et Opus 5.5). Les chiffres sont repris tels que publiés par VentureBeat, sans commentaire sur les modèles eux-mêmes.

## 1. L'idée clé
Selon l'auteur, sur une vraie base de code de 8 400 lignes, Claude Fable 5.2 a réussi 10 corrections sur 15 pour environ 89 $, et Claude Opus 5.5 9 sur 15 pour environ 29 $ : un écart de résultat trop faible pour conclure, pour un coût environ trois fois supérieur. Le bon indicateur pour une entreprise est le coût par tentative réussie, échecs compris, pas le prix du token.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Databricks sur la fidélité aux modèles](2026-11-20-bdm-databricks-fidelite-modeles-ia.md) (coût par tâche comme critère de choix, écarts jusqu'à 1 à 32), la fiche [Uber sur le budget IA des agents de code](2026-11-20-uber-budget-ia-reglages-agents-code.md) (économies par le choix du modèle) et la fiche [T-Mobile du même auteur](2026-11-23-venturebeat-t-mobile-contexte-agents.md).
- **Une méthode reproductible en entreprise** : base de code réelle, cinq rapports de bug, trois essais par modèle, tests cachés, vérification préalable qu'une bonne correction passe et qu'un raccourci échoue, coûts réellement facturés par OpenRouter. Databricks donnait des résultats de benchmark interne ; ici, la méthode est décrite et transposable.
- **Le coût par tentative réussie** : 8,90 $ (Fable 5.2), 3,22 $ (Opus 5.5), 2,00 $ (Kimi K3.1 Pro), 0,25 $ (DeepSeek V4.1 Flash). L'indicateur intègre l'argent dépensé sur les échecs.
- **Les tests faciles ne départagent rien** : tous les modèles réussissent le bug simple ; les écarts apparaissent quand le symptôme éloigne de la cause, et aucun modèle ne résout deux bugs qui se masquent mutuellement (0 sur 12).
- **Observer comment les modèles échouent** : selon l'article, Flash épuise surtout son budget d'étapes, tandis qu'Opus et Fable soumettent surtout des corrections fausses qui ont l'air terminées. Deux modes d'échec qui ne demandent pas la même supervision.

## 3. Résumé
L'article ouvre sur le résultat principal : 10 sur 15 pour Fable 5.2 (environ 89 $), 9 sur 15 pour Opus 5.5 (environ 29 $), aucun modèle ne passe la tâche la plus difficile. Selon l'auteur, l'écart de coût vient de tarifs d'entrée et de sortie deux fois plus élevés, de plus d'appels d'outils et de plus de texte généré. Il replace le test dans un contexte de coûts : dans l'enquête VB Pulse de septembre, 23 % des répondants citent le coût par million de tokens comme critère de choix d'infrastructure IA (11 % en août), et Gartner prévoit que le coût d'inférence par flux agentique sera multiplié par plus de cinq d'ici 2028, malgré la baisse du prix des tokens. Viennent les résultats complets (Kimi K3.1 Pro 5 sur 15 pour 10 $, DeepSeek V4.1 Flash 4 sur 15 pour 1 $), puis un essai séparé où Opus, avec 100 appels d'outils au lieu de 70, atteint 10 sur 15 pour environ 33 $, sans progrès sur les deux tâches les plus dures. L'auteur détaille les cinq tâches : bug simple (tous réussissent), symptôme trompeur dans un nettoyage de réponses d'enquête (Fable et Opus 3 sur 3, Kimi 1, Flash 0), cause difficile à tracer (Opus 2 sur 3, les autres 1), deux bugs indépendants (Fable 3 sur 3, Opus 1, Kimi et Flash 0), deux bugs qui se masquent, avec un total qui correspond au rapport publié alors que les mauvaises personnes sont comptées (0 sur 12). Il en tire quatre leçons pour les entreprises (coût par réussite, tâches où le symptôme trompe, total juste qui cache des données fausses, suivi des modes d'échec), décrit la méthode et ses limites (15 essais sur une seule base de code, cache non standardisé), et annonce un test mensuel complet à partir de janvier.

## 4. Citations et noms
**Citations** : rien de notable (l'article est un compte rendu de test, sans citation de personne).

**Noms cités** :
- *Claude Fable 5.2 et Claude Opus 5.5 (Anthropic)* : les deux modèles comparés dans le titre.
- *Kimi K3.1 Pro* : modèle testé, 5 sur 15.
- *DeepSeek V4.1 Flash* : modèle le moins cher testé, 4 sur 15.
- *OpenRouter* : plateforme par laquelle les coûts réels ont été mesurés.
- *VB Pulse* : enquête de VentureBeat Intelligence sur les critères de choix d'infrastructure IA.
- *Gartner* : prévision d'une hausse du coût d'inférence par flux agentique d'ici 2028.
- *Coût par tentative réussie* : indicateur proposé, coût total divisé par le nombre de réussites.

## 5. Mots-clés
evals, coûts des tokens, routage de modèles, agents IA, vérification, mesure du ROI

## Lecture CPO
- **Implications** :
  - Choisir un modèle pour un usage donné sur ses propres tâches, avec des tests cachés et des cas où le symptôme trompe, plutôt que sur un classement public.
  - Suivre le coût par tâche réussie dans le pilotage FinOps des agents, à côté du taux de réussite.
  - Prévoir une revue humaine adaptée au mode d'échec : une correction fausse qui a l'air terminée demande plus de vigilance qu'un agent qui abandonne.
  - Un total qui « tombe juste » ne prouve pas que les données sont bonnes : à intégrer dans les evals des produits qui manipulent des chiffres.
- **Fiabilité** : média tech, test conduit par la rédaction, méthode publiée en détail, coûts réellement facturés ; échantillon très petit (15 essais, une seule base de code) que l'auteur reconnaît. Le test est en partie un produit d'appel pour un futur test mensuel de VentureBeat. Conflit d'intérêts du rédacteur de la fiche signalé en tête : les chiffres sont repris sans commentaire.
- **Maturité** : Tendance émergente : l'arbitrage coût et qualité entre modèles devient un sujet de pilotage, avec des méthodes de test qui commencent à se publier.
- **Réutilisation** : présentation client DSI sur le choix et le routage des modèles (méthode de test transposable, indicateur de coût par réussite) ; post LinkedIn sur « le prix du token n'est pas le coût de la tâche » ; table ronde FinOps de l'IA avec Databricks et Uber.
