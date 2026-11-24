# Jetons moins chers, facture plus salée, l'offre d'IA cherche encore son modèle tarifaire

**Référence** : Mourad Krim, IT Social, 23 novembre 2026, article d'analyse (s'appuie surtout sur Uptime Institute et des données Ramp), https://itsocial.fr/intelligence-artificielle/intelligence-artificielle-articles/jetons-moins-chers-facture-plus-salee-loffre-dia-cherche-encore-son-modele-tarifaire/

**Axe** : Investissement tech (IA appliquée au produit)

## 1. L'idée clé
Le prix du jeton baisse à chaque génération de modèles, mais la facture IA des entreprises monte, parce que chaque tâche en consomme davantage (raisonnement, agents, nouveaux métiers). La DSI ne doit pas attendre du marché une baisse de coût : son levier est le volume de jetons par tâche, qu'elle maîtrise, pas le prix, qu'elle subit.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Uber, budget IA et réglages des agents](2026-11-20-uber-budget-ia-reglages-agents-code.md) (un retour d'expérience sur les réglages), la fiche [Menlo, State of Enterprise AI](2026-11-13-menlo-state-of-enterprise-ai-2026.md) (dépenses x5,4) et la fiche [IT Social, Deloitte, responsabilité et coût](2026-11-23-itsocial-deloitte-responsabilite-cout-ia.md) (coût unitaire mal suivi) ; et au discours dominant « l'IA va devenir une commodité bon marché ».
- **Le paradoxe chiffré sur un mois** : selon Ramp (clients américains, mi-octobre à mi-novembre), prix moyen du million de jetons -11,2 % (0,45 $), consommation +27,2 %, dépense +12 %. Uptime mesure -27 % sur le prix et +37 % sur la consommation. Les autres fiches donnaient des montants, celle-ci donne le mécanisme.
- **Une unité budgétaire proposée** : Uptime recommande de budgéter en jetons par tâche et en valeur produite par tâche, et de piloter trois leviers (choix du modèle, longueur du contexte, recours ou non à un agent). C'est la généralisation de ce qu'Uber a fait en interne.
- **Les forfaits se durcissent** : plafonds par fenêtre de cinq heures et par semaine chez Anthropic, puis crédits au tarif API ; abonnement à 500 $ par mois chez OpenAI et offre à 200 $ rouverte avec moins d'usage compris. L'abonnement « illimité » recule.
- **Une normalisation en cours** : la Tokenomics Foundation (Linux Foundation, 30 membres fondateurs dont IBM, SAP, ServiceNow, Accenture, JPMorganChase) travaille avec la FinOps Foundation sur des méthodes ouvertes de mesure du coût et de la valeur de l'IA. Le TBM Council juge les plafonds de dépense rigides contre-productifs.
- **Le sur-site n'est rentable qu'à forte utilisation** : dans l'exemple d'Uptime, l'infrastructure dédiée ne bat un néocloud qu'au-delà d'environ 50 % d'utilisation (31 489 $ par cycle à 10 % d'utilisation, contre 7 356 $ en néocloud, et 460 $ à 88 %).

## 3. Résumé
L'article part d'un paradoxe : le jeton est de moins en moins cher, et la facture continue de monter. Owen Rogers (Uptime Institute) explique la baisse par trois forces : du matériel plus productif, des modèles mieux optimisés, la concurrence des modèles à poids ouverts. Les fournisseurs suivent : GPT-6.2 Astra à 8 $ / 40 $ le million de jetons (-20 %), Claude Fable 5.2 à -20 %, cache à -60 % chez les deux, lots à moitié prix, remises Google Cloud de 10 à 20 % contre engagement. Mais la consommation progresse plus vite que les prix ne baissent (données Ramp et Uptime), tirée par les modèles plus gros, les raisonnements longs et les agents. Côté offres, les forfaits se plafonnent, OpenAI lance un abonnement à 500 $, OpenRouter réserve ses modèles gratuits à l'expérimentation ; le GPU renchérit et certains estiment que les modèles de pointe sont vendus à perte. McKinsey (enquête 2026) : 20 % des répondants disent que les coûts d'exploitation ont limité leur usage, 60 % vont investir plus. L'article détaille ensuite les causes techniques (jetons de réflexion invisibles, historique renvoyé à chaque appel d'agent), le paradoxe de Jevons, puis les leviers de la DSI : budget par tâche, outils FinOps (Apptio, CloudHealth, Flexera, Ramp, Revenium, Mavvrik), Tokenomics Foundation, visibilité et alertes souples plutôt que plafonds. Un calcul d'Uptime sur l'entraînement sur site montre que le dédié ne paie qu'au-delà de 50 % d'utilisation, et que la souveraineté ou la conformité pèsent souvent plus que l'écart de coût. Conclusion d'Uptime : consommation et factures vont continuer de monter, car les agents sont encore peu déployés ; compter sur le marché pour baisser le coût de l'IA expose à une déception.

## 4. Citations et noms
**Citations** :
- « la facture de l'IA, elle, poursuit sa courbe ascendante », Mourad Krim, IT Social
- « les GPU inutilisés sont souvent le coût caché de l'ambition », IT Social, à propos du calcul d'Uptime sur l'infrastructure sur site

**Noms cités** :
- *Owen Rogers, Uptime Institute* : directeur de recherche, source principale (trois forces de baisse des prix, budget par tâche, calcul sur site).
- *Ramp* : données de dépenses de ses clients américains sur un mois (prix, volume, dépense).
- *OpenAI, Anthropic, Google Cloud* : baisses de prix, forfaits plafonnés, remises sur engagement.
- *OpenRouter* : agrégateur, routeur vers des modèles gratuits réservés à l'expérimentation.
- *McKinsey* : enquête 2026 (20 % freinés par les coûts, 60 % augmentent leurs investissements).
- *TBM Council* : réunion de Miami, TCO de l'IA mal calculé, plafonds rigides jugés contre-productifs.
- *Tokenomics Foundation (Linux Foundation) et FinOps Foundation* : méthodes ouvertes de mesure du coût et de la valeur.
- *Apptio, CloudHealth, Flexera, Revenium, Mavvrik* : outils de suivi des coûts.
- *CoreWeave, Lambda, Nebius* : néoclouds pris comme référence dans le calcul sur site.
- *Paradoxe de Jevons* : une ressource moins chère trouve de nouveaux usages, la consommation totale monte.

## 5. Mots-clés
coûts des tokens, FinOps, tarification IA, budgets IT, infrastructure IA, mesure du ROI

## Lecture CPO
- **Implications** :
  - Pour un produit IA, le coût unitaire à suivre est le coût par tâche (ou par résolution), pas le prix du jeton : à intégrer dans le business case et les métriques produit.
  - Les choix de conception (modèle, taille du contexte, agent ou non) sont des choix de coût : ils doivent entrer dans les arbitrages de l'équipe produit, pas seulement de l'architecture.
  - Les forfaits plafonnés et le passage aux crédits rendent les budgets d'outils IA des équipes moins prévisibles : prévoir des alertes plutôt que des plafonds durs.
- **Fiabilité** : média IT, article de synthèse ; Uptime est un cabinet de recherche sur les centres de données (intérêt à souligner la demande en capacité) ; Ramp vend des outils de gestion des dépenses et ses données ne couvrent que ses clients américains, sur un mois. Prix fournisseurs vérifiables ; calcul sur site fondé sur un cas fictif avec hypothèses publiées.
- **Maturité** : Tendance émergente : le paradoxe est désormais mesuré et outillé (fondation, outils FinOps), mais l'unité « coût par tâche » n'est pas encore une pratique courante.
- **Réutilisation** : post LinkedIn (« le jeton baisse, la facture monte : changez d'unité de compte ») ; présentation client DSI sur le budget IA 2027 ; article OCTO en complément de la fiche Uber sur les réglages par défaut.
