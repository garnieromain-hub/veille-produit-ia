# Métriques de l'IA : les DSI doivent tenir le compteur avant de recevoir la facture

**Référence** : Guillaume Geudin (directeur de la performance achats chez Elée, cabinet de conseil en achats), IT for Business, 23 novembre 2026, tribune, https://www.itforbusiness.fr/facturation-ia-metriques-dsi-110051

**Axe** : Investissement tech (Portefeuille numérique)

## 1. L'idée clé
Avec l'IA générative, l'unité de facturation (token, crédit, action, résolution) est définie, mesurée et modifiée par l'éditeur. Négocier le prix unitaire ne suffit plus : il faut encadrer contractuellement la définition de l'unité, et mesurer soi-même ses usages avant les renouvellements pluriannuels de 2026-2027, qui figeront ces métriques pour plusieurs exercices.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Deloitte via IT Social](2026-11-23-itsocial-deloitte-responsabilite-cout-ia.md) (suivre le coût unitaire, nommer un propriétaire économique), la fiche [Cebr / Wasabi](2026-11-19-cebr-wasabi-depassements-infrastructure-ia.md) (l'IA fait déraper les budgets d'infrastructure) et le discours FinOps dominant, centré sur la consommation cloud et le prix par million de tokens.
- **Le risque porte sur la définition de l'unité, pas sur son prix** : l'auteur cite Anthropic (le tokenizer d'Opus 4.7 compte jusqu'à 35 % de tokens en plus pour un même texte, à prix affiché inchangé) et Firecrawl (jusqu'à 2,65 fois plus de tokens selon le fournisseur). Le prix par million de tokens ne dit donc pas le coût d'une tâche.
- **Une liste de clauses contractuelles prête à l'emploi** : préavis et garantie de prix constant pour un même travail en cas de changement de métrique ou de tokenizer, droit de sortie, plafonds fermes, interdiction de la refacturation rétroactive unilatérale, report des crédits non consommés, droit d'audit sur les données brutes. Les fiches précédentes s'arrêtaient au pilotage interne.
- **Le coût caché de l'IA dans les suites bureautiques** : hausses Microsoft au 1er juillet (+13 % Office 365 E3, +25 % Microsoft 365 F3, +33 % F1), justifiées entre autres par l'IA intégrée. Une entreprise qui n'a pas déployé Copilot paie quand même une part de l'IA.
- **Des crédits éditeurs détaillés** : Copilot à 30 $ par mois plus des crédits à un cent (cinq tâches longues dans Copilot Cowork, environ 40 $ de plus), paiement à l'usage activé par défaut sur les nouvelles licences Copilot Business depuis novembre (plafond 4 000 crédits par utilisateur et par mois), Flex Credits de Salesforce à 20 crédits par action et non reportables.
- **SAM et FinOps à réunir** : le SAM gère contrats et métriques, le FinOps les dépenses variables ; l'auteur demande une équipe, un responsable et une vue unique licences, cloud, SaaS, tokens et crédits.

## 3. Résumé
L'auteur part d'un constat : les unités de facturation de l'IA se multiplient et changent de définition presque à chaque renouvellement. Pendant quarante ans, le logiciel s'est acheté sur des métriques que le client pouvait compter et contester (utilisateurs nommés, cœurs, postes). L'IA générative inverse la situation : l'éditeur définit et change l'unité, parfois à prix affiché constant (exemples Anthropic et Firecrawl). Il décrit ensuite les crédits : le modèle Copilot de Microsoft présenté fin septembre, le paiement à l'usage par défaut sur Copilot Business, les trois offres Salesforce de septembre avec leurs Flex Credits ; c'est l'éditeur seul qui fixe le taux de change entre crédit et travail réalisé. Puis il explique pourquoi le signal prix disparaît : trois ans de vente sous le coût pour gagner des parts de marché, une normalisation des prix qui commence par les entreprises, des dirigeants qui jugent l'IA à l'aune de leur abonnement personnel, et une dépense à la consommation, déclenchée sans signal prix, sans plafond naturel et visible après coup ; un agent en boucle peut gonfler la facture autant qu'un déploiement réussi. Il ajoute les coûts cachés dans les suites (hausses Microsoft du 1er juillet), le cloud, les SaaS et les cartes bancaires d'entreprise : aucune ligne budgétaire ne s'appelle « IA ». Vient l'urgence : les contrats pluriannuels de 2026-2027 vont figer les unités, et le report au 2 décembre 2027 des obligations de l'AI Act sur les systèmes à haut risque laisse le temps de poser des règles avant la hausse des volumes. Il liste les clauses à obtenir, puis l'organisation (SAM et FinOps ; 98 % des praticiens FinOps gèrent désormais les dépenses IA contre 31 % deux ans plus tôt, selon la FinOps Foundation). Conclusion : les directions qui mesurent dès maintenant leurs usages arriveront aux renouvellements avec des données que l'éditeur ne pourra plus contester.

## 4. Citations et noms
**Citations** :
- « Préacheter des crédits revient à prépayer dans une devise que l'on ne contrôle pas. », Guillaume Geudin
- « Négocier le prix du token sans encadrer sa définition revient à négocier le prix du litre d'essence [...] », Guillaume Geudin (la phrase se poursuit : en laissant le fournisseur redéfinir le litre)

**Noms cités** :
- *Guillaume Geudin, Elée* : auteur, directeur de la performance achats d'un cabinet de conseil en achats.
- *Anthropic, Opus 4.7* : exemple de tokenizer qui compte jusqu'à 35 % de tokens en plus à prix inchangé.
- *Firecrawl* : source de l'écart de 2,65 fois sur le nombre de tokens selon le fournisseur.
- *Microsoft (Copilot, Copilot Cowork, Copilot Business, Office 365 E3, Microsoft 365 F3 et F1)* : modèle de crédits et hausses de prix des suites.
- *Salesforce, Flex Credits* : nouvelles éditions avec stock de crédits non reportables.
- *AI Act* : report au 2 décembre 2027 des obligations sur les systèmes à haut risque.
- *FinOps Foundation* : source du chiffre 98 % contre 31 %.
- *SAM (Software Asset Management)* : fonction à rapprocher du FinOps.

## 5. Mots-clés
coûts des tokens, FinOps, tarification IA, achats IT, dépendance fournisseur

## Lecture CPO
- **Implications** :
  - Avant tout renouvellement pluriannuel avec un éditeur IA, mettre au contrat la définition de l'unité (préavis, prix constant à travail égal, sortie, plafonds, report des crédits, audit).
  - Mesurer les usages en interne, par cas d'usage et par tâche, plutôt que de s'en remettre au tableau de bord de l'éditeur.
  - Réunir SAM et FinOps sous un seul responsable, avec une vue consolidée licences, cloud, SaaS, tokens et crédits : c'est un chantier de gestion de portefeuille.
  - Côté éditeur d'un produit IA, s'attendre à ce que les acheteurs exigent ces clauses : la stabilité de la métrique devient un argument commercial.
- **Fiabilité** : tribune d'un consultant achats, dont le cabinet vend précisément l'accompagnement des négociations éditeurs : intérêt commercial direct. Les faits cités (hausses Microsoft, crédits Copilot et Salesforce, chiffre Anthropic, FinOps Foundation) sont vérifiables mais sans lien vers leurs sources dans l'article ; le chiffre Firecrawl n'est pas sourcé plus précisément.
- **Maturité** : Tendance émergente : la facturation à l'usage et aux crédits se généralise chez les grands éditeurs, mais les pratiques contractuelles pour l'encadrer ne sont pas encore établies.
- **Réutilisation** : présentation client DSI ou achats (check-list des clauses à négocier) ; post LinkedIn « On négocie le prix du litre, l'éditeur redéfinit le litre » ; article OCTO sur le FinOps de l'IA, à croiser avec les fiches Deloitte et Cebr.
