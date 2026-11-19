# 2026: The State of Enterprise AI

**Référence** : Tim Tully, Joff Redfern, Deedy Das, Derek Xiao, Menlo Ventures, 3 novembre 2026, rapport annuel (4e édition), https://menlovc.com/perspective/2026-the-state-of-enterprise-ai/

**Axe** : Investissement tech (IA appliquée au produit)

## 1. L'idée clé
Les dépenses IA des entreprises ont été multipliées par 5,4 en un an (177 Md$ de run rate en septembre 2026) et ce n'est pas un jeu à somme nulle : 55 % de la hausse vient de budgets nouveaux, et seuls 9 % ont été pris aux éditeurs SaaS. La valeur se concentre chez les labs (69 % des dépenses), tirée par les agents et le code, et c'est la capacité des modèles, pas leur prix, qui fait la différence.

## 2. Ce qui est nouveau
**Par rapport à** : l'édition 2025 du même rapport (reprise à l'époque avec un total de 37 Md$ ; la base 2025 est ramenée à 33 Md$ dans la nouvelle taxonomie, à garder en tête si on compare les deux éditions), et au discours dominant « l'IA va manger le SaaS ».
- **D'où vient l'argent** : 55 % de budgets nouveaux, 22 % de budgets logiciels existants, 13 % de conversions de licences chez les éditeurs en place (Office vers Copilot), 9 % (12,6 Md$) vers des AI-natives. Le rapport chiffre l'effet sur le SaaS applicatif (plus de 600 Md$) à environ 2 points de croissance (13 % à 11 %), et observe peu de remplacements de CRM, SIRH ou ERP. C'est la première ventilation chiffrée de ce type.
- **Les budgets explosent par rapport au plan** : dépense moyenne 4,7 fois celle de 2025 contre 1,9 prévu (médiane 2,2 contre 1,8). Les agents expliquent l'écart : la dépense par entreprise a presque quintuplé alors que l'adoption n'est passée que de 55 % à 65 %.
- **Concentration chez les labs** : Anthropic, OpenAI et Google captent 69 % des dépenses (contre 50 %) ; en API, Anthropic passe de 40 % à 55 %, Google chute de 21 % à 9 %. Claude Code et Codex font 70 % du marché du code (24 Md$).
- **Les agents dominent l'usage** : 80 % des tokens sur OpenRouter, 74 % des builders utilisent des agents (contre 27 %). Les applications restent concentrées : code (34 Md$) et assistants (25 Md$) font 76 % du marché applicatif ; support client 2,7 Md$, RH 0,9 Md$.
- **Open source** : 19 % des tokens mais 4 % des dépenses ; 89 % des dépenses open source vont à des modèles chinois.

## 3. Résumé
Le rapport ouvre sur le passage à l'échelle : 177 Md$ de dépenses de déploiement en run rate annualisé, contre 33 Md$ un an plus tôt (1,7 Md$ en 2023), avec une croissance qui accélère (5,4x contre 3,9x). Les agents génèrent désormais 80 % des tokens observés sur OpenRouter. Il analyse ensuite l'origine des budgets et conclut que l'IA élargit le marché du logiciel plus qu'elle ne le cannibalise, tout en notant que l'IA pèse déjà plus de 30 % du chiffre d'affaires du cloud public. Troisième temps : la concentration chez les labs (69 %), avec la montée d'Anthropic et le recul de Google en API. Le rapport montre ensuite que les entreprises ont dépensé environ 2,5 fois ce qu'elles avaient budgété, à cause des agents. Il détaille l'usage des modèles (bascule vers les modèles frontière : 63 % des dépenses, prix de l'open source divisé par 3,3), puis les applications en production : code et assistants dominent, les fonctions métier restent petites, les AI-natives captent 77 % des dépenses applicatives mais les éditeurs en place tiennent l'IT (ServiceNow), la data et les RH (Workday). Il conclut par des prédictions : agents sur horizons longs, déconcentration progressive, migration de la valeur vers la couche applicative.

Méthodologie : enquête Morning Consult auprès de près de 400 décideurs d'entreprises américaines (8-26 septembre 2026), plus un modèle de marché ascendant (enquête, dépôts publics, rapports tiers) et des données de tokens OpenRouter recoupées avec Ramp et Vercel. Taxonomie reclassée par rapport à 2025.

## 4. Citations et noms
**Citations** :
- « Loin d'être un jeu à somme nulle, l'IA crée de la valeur nouvelle dans toute l'économie. » (« Far from being a zero-sum game, AI is creating new value across the economy »), Menlo Ventures
- « La capacité des modèles, et non leur prix, s'avère l'avantage concurrentiel décisif. » (« model capability—not price—is proving to be the decisive competitive advantage. »), Menlo Ventures

**Noms cités** :
- *Anthropic, OpenAI, Google* : les trois labs qui captent 69 % des dépenses ; Anthropic est une participation de Menlo.
- *Claude Code, Codex* : 70 % du marché du code.
- *OpenRouter* : source des données de tokens, et participation de Menlo (rachetée par Stripe au T3 selon Crunchbase).
- *Morning Consult* : institut qui a mené l'enquête.
- *ServiceNow, Workday, Microsoft Copilot* : éditeurs en place qui résistent ou convertissent leurs licences.
- *Kimi, DeepSeek, GLM, Qwen* : modèles chinois qui dominent l'open source.

## 5. Mots-clés
budgets IT, ROI IA, agents IA, build vs buy, enquête

## Lecture CPO
- **Implications** :
  - Les budgets IA dérapent par les agents (2,5 fois le plan en moyenne) : le pilotage par la consommation (tokens, coût unitaire) devient un sujet produit, pas seulement FinOps.
  - Le « SaaS mort » n'est pas dans les chiffres : pour un portefeuille applicatif, la question 2027 est plutôt la conversion des licences existantes que le remplacement des systèmes cœur.
  - La concentration chez deux ou trois labs crée un risque de dépendance à intégrer dans les choix d'architecture produit.
- **Fiabilité** : fonds de capital-risque, investisseur dans Anthropic, OpenRouter, Cursor, Lovable, Databricks et d'autres acteurs cités (déclaré dans le rapport). La thèse « la capacité gagne » sert directement son portefeuille. Méthodologie décrite (institut, dates, taille) mais questionnaire et modèle de marché non publiés ; échantillon américain uniquement. Les montants sont des estimations de marché, pas des mesures.
- **Maturité** : Tendance émergente : la bascule des dépenses vers les agents et le code est massive mais très concentrée sur deux usages et quelques fournisseurs.
- **Réutilisation** : présentation client DSI (origine des budgets IA et dérapage par rapport au plan) ; post LinkedIn (« 9 % : la part des dépenses IA prise au SaaS ») ; article OCTO sur le pilotage des coûts des produits IA, à mettre en regard de Deloitte (44 % suivent le coût unitaire d'inférence).
