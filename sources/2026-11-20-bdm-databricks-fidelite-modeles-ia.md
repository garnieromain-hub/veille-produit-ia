# En entreprise, la fidélité aux modèles d'IA ne dure que quelques semaines

**Référence** : Matthieu Eugène, Blog du Modérateur, 20 novembre 2026, article sur une étude (Databricks AI Index), https://www.blogdumoderateur.com/entreprise-fidelite-modeles-ia/

**Axe** : IA appliquée au produit (Investissement tech)

## 1. L'idée clé
Les entreprises changent de modèle d'IA au rythme des sorties : les parts d'usage basculent en quelques semaines, la majorité des clients ont désormais essayé plusieurs fournisseurs, et l'écart de coût entre modèles de performance égale peut aller de 1 à 32. La qualité du modèle reste le premier moteur des parts de marché, mais le coût par tâche devient un critère de choix.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Thoughtworks Radar vol. 35](2026-11-19-thoughtworks-radar-vol35.md) (modèle frontière par défaut en « Caution », routage entre modèles), la fiche [Menlo State of Enterprise AI](2026-11-13-menlo-state-of-enterprise-ai-2026.md) (thèse « la capacité gagne ») et le discours dominant selon lequel les entreprises s'installent chez un fournisseur principal.
- **Des données d'usage, pas déclaratives** : tokens réellement consommés par plus de 10 000 clients via la passerelle de Databricks, du 20 juillet au 2 novembre 2026, là où Menlo et la plupart des études reposent sur des enquêtes.
- **La volatilité chiffrée** : Claude Opus 5.5 passe de 7,2 % à 38 % des tokens propriétaires en six semaines, Claude Fable 5.1 tombe de 5,5 % à 0,6 %. La fidélité se compte en semaines.
- **Le mono-fournisseur recule** : 64 % des clients n'utilisaient qu'un fournisseur en juillet, 28 % au 2 novembre. Nuance de l'auteur : la mesure est cumulative, elle compte les entreprises qui ont essayé plusieurs fournisseurs, pas celles qui les utilisent en parallèle.
- **Le coût par tâche comme critère** : GPT-6 Luna et Opus 5.5 réussissent 89 % des tâches du benchmark interne, pour environ 0,05 $ contre 1,62 $ par tâche ; Fable 5.1 culmine à 96 % pour 7,47 $. Cela donne un ordre de grandeur au « routage » prôné par Thoughtworks.
- **Les modèles ouverts plafonnent** : 7,3 % des tokens servis directement par Databricks en juillet, 31 % début novembre, mais stables depuis septembre ; les fournisseurs dominants sont chinois (Zhipu, DeepSeek, Moonshot AI), Mistral Large 4 n'est pas suivi.

## 3. Résumé
L'article présente le Databricks AI Index, publié par l'éditeur lui-même sans institut tiers. L'auteur en donne d'emblée la méthode : usage anonymisé de plus de 10 000 entreprises clientes passant par la passerelle Unity de Databricks, du 20 juillet au 2 novembre 2026, complété d'un benchmark de code interne arrêté au 10 novembre, et il signale que Databricks vend un outil de routage automatique entre modèles. Premier constat : la rotation rapide des modèles, avec la montée d'Opus 5.5 (de 7,2 % à 38 % des tokens propriétaires en six semaines) et la chute de Fable 5.1. Databricks en conclut que la qualité continue de faire les parts de marché. Deuxième constat : le multi-fournisseur, avec la part des clients mono-fournisseur qui passe de 64 % à 28 %, chiffre cumulatif que l'auteur relativise. Troisième constat : le rapport performance-coût, où des modèles de réussite égale (89 %) diffèrent d'un facteur 32 en coût par tâche, Fable 5.1 restant le plus performant (96 %) et le plus cher, Muse Wonder de Meta à 95 % pour 1,53 $. Dernier constat : les modèles ouverts, montés à 31 % des tokens servis directement par Databricks puis stabilisés, dominés par des acteurs chinois.

## 4. Citations et noms
**Citations** :
- « La qualité des modèles continue d'influencer fortement les parts de marché des fournisseurs. », Databricks (AI Index)

**Noms cités** :
- *Databricks AI Index* : l'étude commentée, fondée sur l'usage des clients de Databricks et un benchmark interne.
- *Databricks (Unity Gateway)* : éditeur de plateforme de données, auteur de l'index, qui vend un outil de routage de modèles.
- *Anthropic (Claude Opus 5.5, Claude Fable 5.1)* : le modèle qui gagne le plus de parts et celui qui en perd le plus ; Fable 5.1 reste le plus performant du benchmark.
- *OpenAI (GPT-6 Luna)* : même taux de réussite qu'Opus 5.5 pour un coût par tâche 32 fois plus faible.
- *Meta (Muse Wonder)* : 95 % de réussite pour 1,53 $ par tâche.
- *Zhipu, DeepSeek, Moonshot AI* : principaux fournisseurs de modèles ouverts dans l'index.
- *Mistral Large 4* : absent des familles suivies.

## 5. Mots-clés
routage de modèles, coûts des tokens, modèles ouverts, dépendance fournisseur, données d'usage

## Lecture CPO
- **Implications** :
  - Concevoir les produits IA pour changer de modèle sans refonte (couche d'abstraction, evals rejouables) : un choix de modèle se périme en semaines.
  - Mettre le coût par tâche réussie dans les critères de choix d'un modèle, à côté du taux de réussite : à qualité égale, l'écart peut atteindre un facteur 30.
  - Côté achats et DSI, éviter les engagements longs sur un seul fournisseur de modèles.
- **Fiabilité** : éditeur directement intéressé (il vend le routage automatique que l'étude justifie) ; échantillon limité à ses propres clients, donc biaisé vers des entreprises déjà outillées en données ; période courte (trois mois et demi) ; benchmark interne non public. L'auteur signale lui-même ces limites et le caractère cumulatif du chiffre multi-fournisseur.
- **Maturité** : Tendance émergente : le multi-modèles progresse vite dans l'usage mesuré, mais sur un échantillon d'early adopters.
- **Réutilisation** : post LinkedIn (« la fidélité aux modèles se compte en semaines ») ; présentation client sur la réversibilité et l'architecture multi-modèles, en croisant avec Thoughtworks et la fiche OCTO Boucard sur l'effort de raisonnement ; table ronde DSI sur la dépendance aux fournisseurs d'IA.
