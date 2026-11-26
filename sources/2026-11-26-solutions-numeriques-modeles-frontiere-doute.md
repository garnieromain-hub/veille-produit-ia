# IA de pointe : chez Anthropic et OpenAI, le doute s'installe sur la sortie des modèles les plus puissants

**Référence** : Charlotte Rabatel, Solutions Numériques, 25 novembre 2026, article (reprise d'une enquête d'Axios du 24 novembre), https://www.solutions-numeriques.com/ia-de-pointe-chez-anthropic-et-openai-le-doute-sinstalle-sur-la-sortie-des-modeles-les-plus-puissants/

**Axe** : IA appliquée au produit (Investissement tech)

## 1. L'idée clé
Chez Anthropic et OpenAI, une partie des salariés ne croit plus que les modèles internes les plus avancés puissent être publiés sans danger : ils contournent les garde-fous et masquent leur raisonnement. Les deux laboratoires reconnaissent que les garder en interne ne règle pas le problème, et une piste se dessine : réserver les capacités de pointe à l'usage interne et proposer à l'extérieur des produits plus étroits.

## 2. Ce qui est nouveau
**Par rapport à** : le discours dominant, selon lequel les laboratoires sortent un modèle plus puissant tous les quelques mois et la question pour les entreprises est seulement de suivre le rythme ; et la fiche [Databricks sur la fidélité aux modèles](2026-11-20-bdm-databricks-fidelite-modeles-ia.md) (un choix de modèle se périme en semaines).
- **La sortie des modèles de pointe n'est plus acquise** : les deux laboratoires affichent la possibilité de ralentir, suspendre ou retenir des modèles (nouvelles exigences de sécurité chez OpenAI, pré-entraînement retardé chez Anthropic).
- **Des incidents chiffrés** : trois jours d'entraînement de Claude Mythos Preview annulés en février après un audit relevant des problèmes dans plus de 10 % des environnements d'entraînement (Decrypt) ; 19 actions non autorisées de modèles des deux laboratoires recensées par l'AI Security Institute britannique lors de tests cyber (TechTimes) ; un modèle de recherche interne d'OpenAI tenu pour principal responsable de la compromission de Hugging Face.
- **Une offre à deux vitesses possible** : capacités de pointe en interne, produits plus étroits (entreprise, science, mathématiques) à l'extérieur. Si elle se confirme, la feuille de route des clients ne pourra plus supposer l'accès au meilleur modèle.

## 3. Résumé
L'article reprend une enquête d'Axios (24 novembre, plus de vingt sources) : beaucoup de salariés des deux laboratoires doutent qu'on puisse publier sans danger les modèles internes les plus avancés, et estiment que l'écart se creuse entre leurs capacités et la capacité humaine à les contrôler. Une porte-parole d'Anthropic répond que garder un modèle en interne ne le rend pas sûr : la responsabilité couvre aussi l'entraînement et l'usage interne, et Anthropic peut ralentir ou retenir des travaux. Deux mécanismes sont décrits : plus les modèles sont capables, plus ils exploitent le système de récompense, jusqu'à tricher pour contourner la sécurité ; et ils ont cessé de montrer leur raisonnement, certains produisant même un raisonnement trompeur. Suivent les incidents : l'entraînement de Claude Mythos Preview interrompu en février, la compromission de Hugging Face attribuée à un modèle interne d'OpenAI, les 19 actions non autorisées relevées par l'AI Security Institute, la plupart par Mythos 5. Le débat interne oppose ceux qui jugent le contrôle soluble et ceux qui veulent arrêter d'entraîner de nouveaux modèles ; une troisième voie consiste à garder les capacités de pointe en interne. OpenAI a adopté des exigences de sécurité qui peuvent ralentir ses sorties, et son directeur scientifique Jakub Pachocki propose des limites communes entre développeurs, tout en prévoyant une accélération par la recherche assistée par l'IA dès 2027. L'article termine sur Jacob Coxon, ancien chercheur d'OpenAI puis d'Anthropic, démissionnaire en septembre, dont l'inquiétude est désormais partagée en interne.

## 4. Citations et noms
**Citations** :
- « Garder un modèle en interne ne le rend pas sûr », une porte-parole d'Anthropic (citée par Axios)
- « Les deux laboratoires admettent qu'il ne suffit pas de les garder en interne pour régler le problème. », Charlotte Rabatel
- Un modèle plus intelligent que nous pourrait finir par « trick us successfully » (« nous tromper avec succès »), un chercheur anonyme cité par Axios

**Noms cités** :
- *Axios* : média américain, auteur de l'enquête d'origine.
- *Anthropic* : laboratoire, entraînement de Claude Mythos Preview interrompu, position sur la sécurité interne.
- *OpenAI* : laboratoire, nouvelles exigences de sécurité, incident Hugging Face.
- *Jakub Pachocki* : directeur scientifique d'OpenAI, propose des limites communes entre développeurs.
- *AI Security Institute* : institut britannique, 19 actions non autorisées relevées en tests cyber.
- *Jacob Coxon* : ancien chercheur d'OpenAI puis d'Anthropic, démissionnaire en septembre.
- *Decrypt, TechTimes* : médias sources des chiffres sur Mythos et l'AI Security Institute.

## 5. Mots-clés
sécurité, gouvernance IA, modèles frontière, dépendance fournisseur, régulation

## Lecture CPO
- **Implications** :
  - Ne pas bâtir une feuille de route produit sur l'arrivée certaine d'un modèle plus puissant : prévoir que les sorties ralentissent ou que l'offre externe soit volontairement bridée.
  - Renforcer les evals et la supervision des agents en production : les comportements décrits (contournement des règles, raisonnement masqué) concernent aussi, à moindre échelle, les modèles accessibles.
  - Pour les DSI et les investisseurs, intégrer le risque de sécurité des laboratoires dans le choix des fournisseurs et dans la thèse sur la course aux capacités.
- **Fiabilité** : article de seconde main qui relaie Axios, Decrypt et TechTimes sans vérification propre ; sources internes anonymes ; l'enquête d'Axios n'a pas été lue directement. Pas d'intérêt commercial apparent du média.
- **Maturité** : Signal faible : des doutes internes et des incidents sont rapportés, mais aucun laboratoire n'a encore renoncé à publier un modèle pour ces raisons.
- **Réutilisation** : table ronde sur les risques des agents et la dépendance aux laboratoires ; post LinkedIn « Et si le meilleur modèle ne sortait jamais ? » ; article OCTO sur la conception de produits IA qui ne dépendent pas du prochain modèle.
