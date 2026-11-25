# The AI invoice is a governance signal most CIOs are failing to read

**Référence** : Yash Mehta (contributeur, entrepreneur, dirigeant de la plateforme Intellectus, fondateur d'Expersight), CIO.com, 24 novembre 2026, tribune (rubrique Opinion, blog « First Person »), https://www.cio.com/article/4252236/the-ai-invoice-is-a-governance-signal-most-cios-are-failing-to-read.html

**Axe** : Investissement tech (Portefeuille numérique)

> **Passage promotionnel** : l'article présente Appinventiv comme un partenaire d'ingénierie qui intègre la gouvernance dès le chiffrage, en précisant qu'il est OpenAI Select Partner et Claude Partner d'Anthropic, avec un lien vers son site glissé dans une affirmation générale sur les « partenaires de livraison ». Aucune relation entre l'auteur et Appinventiv n'est déclarée. Ce passage relève de la publicité déguisée et n'est pas repris comme argument dans la fiche. Le renvoi au blog d'Artefact relève, en moins appuyé, de la même logique.

## 1. L'idée clé
Si la facture d'un prestataire de développement ne baisse pas alors que l'IA accélère l'écriture du code, ce n'est pas forcément une surfacturation : le coût s'est déplacé de l'écriture vers la gouvernance (revue, validation, provenance, accès, sécurité, conformité). Le DSI doit lire la facture comme un signal de gouvernance, et se méfier d'une baisse annoncée de 40 % sans ligne de gouvernance, car ce coût ignoré réapparaît en incidents.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Sahni sur le passage de relais dev-QA](2026-11-23-cio-sahni-dev-qa-code-ia.md) (taxe de vérification, courbe en J), la fiche [Deloitte relu par IT Social](2026-11-23-itsocial-deloitte-responsabilite-cout-ia.md) (gouvernance des agents et coût unitaire mal suivis) et la fiche [IT Social sur les jetons moins chers](2026-11-24-itsocial-jetons-moins-chers-facture-ia.md) (la facture IA monte malgré la baisse du prix du jeton).
- **L'angle achats** : le goulot de la revue, déjà documenté côté ingénierie, est lu ici depuis la facture d'un prestataire externe. Une facture stable masque une réallocation (moins de codage, plus de revue et de tests), et l'absence de ligne de gouvernance devient un signal d'alerte.
- **Des questions à poser aux prestataires** : un tableau de lignes de facturation à questionner et un « test de 10 minutes » sur une facture, plus une répartition indicative de l'effort avant et après IA. Ces pourcentages sont des illustrations de l'auteur, sans données à l'appui.
- **La question de la propriété du budget** : qui porte la facture de la gouvernance, avec le rappel (FinOps Foundation) que 78 % des pratiques FinOps sont rattachées au CTO ou au DSI.
- **Le calendrier réglementaire mis à jour** : le Digital Omnibus repousse les obligations de l'AI Act pour les systèmes à haut risque (décembre 2027 et août 2028), les obligations de transparence s'appliquant depuis le 2 août 2026 ; comité FREE-AI de la RBI (26 recommandations, août 2025).
- Pour les chiffres d'adoption et de maturité de gouvernance (GitLab, Deloitte, Gartner), redite des fiches citées.

## 3. Résumé
L'auteur part d'un paradoxe : l'IA générative devrait faire baisser le coût du développement externalisé, mais les factures restent stables. Il l'explique par le déplacement du goulot : selon le rapport GitLab AI Accountability 2026 (Harris Poll, 1 528 développeurs et acheteurs), 78 % des organisations écrivent et committent le code plus vite, et 85 % estiment que le goulot est désormais la revue et la validation. Il décrit cette « taxe de gouvernance cachée » et décompose la facture IA en postes (revue, provenance, accès, validation, usage), avec une liste de coûts souvent non budgétés. Il souligne la croissance du phénomène : Gartner attend plus de 150 000 agents dans une grande entreprise du Fortune 500 d'ici 2028, contre moins de 15 en 2025, et seuls 13 % des organisations jugent avoir la bonne gouvernance ; Deloitte compte 21 % d'organisations avec un cadre de gouvernance IA mature. Il pose la question de la propriété du budget, puis propose un tableau de signaux et de questions à poser aux prestataires, et décline le sujet par secteur (fintech avec la RBI, santé, retail, industrie, calendrier de l'AI Act via le Digital Omnibus). Il cite DORA 2025 (l'IA amplifie forces et faiblesses de l'ingénierie existante) et Artefact sur l'ingénierie du contexte, et insère le passage promotionnel sur Appinventiv. Il décrit à quoi devrait ressembler une estimation honnête (répartition de l'effort avant et après IA) et conclut sur un test de 10 minutes : une facture sans ligne de gouvernance n'est pas moins chère, elle reporte le coût vers les incidents.

## 4. Citations et noms
**Citations** : rien de notable (aucune formule courte relevée mot pour mot dans la lecture de la source).

**Noms cités** :
- *Yash Mehta* : auteur, entrepreneur, dirigeant d'Intellectus et fondateur d'Expersight.
- *GitLab, AI Accountability Report 2026 (Harris Poll)* : 78 % codent plus vite, 85 % voient la revue comme goulot.
- *Deloitte, State of AI in the Enterprise 2026* : 21 % de cadres de gouvernance IA matures ; environ un dirigeant sur cinq (3 235 interrogés) avec un modèle mature pour les agents autonomes.
- *Gartner* : plus de 150 000 agents par grande entreprise d'ici 2028 ; 13 % des organisations bien gouvernées.
- *FinOps Foundation* : 78 % des pratiques FinOps rattachées au CTO ou au DSI.
- *RBI, comité FREE-AI* : 26 recommandations pour le secteur financier indien (août 2025).
- *Digital Omnibus (UE), AI Act* : report des obligations pour les systèmes à haut risque.
- *DORA, rapport 2025* : l'IA amplifie les forces et faiblesses de l'ingénierie.
- *Artefact* : cité pour ses travaux sur l'ingénierie du contexte et les graphes de connaissances.
- *Appinventiv* : prestataire présenté dans le passage promotionnel (voir l'encadré).
- *Taxe de gouvernance* : coût de revue, validation et conformité que l'IA déplace sans le supprimer.

## 5. Mots-clés
gouvernance IA, achats IT, goulot d'étranglement, vérification, FinOps, budgets IT

## Lecture CPO
- **Implications** :
  - Exiger des prestataires une ligne explicite de revue, validation et conformité dans les devis de développement assisté par IA, et questionner les baisses spectaculaires qui n'en ont pas.
  - Désigner qui porte le budget de gouvernance de l'IA (DSI, FinOps, produit) avant que les agents se multiplient.
  - Dans la mesure de la valeur, comptabiliser le coût de vérification à côté du gain de vitesse de codage.
- **Fiabilité** : tribune d'un entrepreneur contributeur, sans retour d'expérience propre ; chiffres issus d'enquêtes d'éditeurs et de cabinets (GitLab, Deloitte, Gartner) sans méthodologie détaillée ; répartition de l'effort illustrative ; passage promotionnel non déclaré pour Appinventiv, qui affaiblit la neutralité de l'ensemble.
- **Maturité** : Tendance émergente : le goulot de la revue est bien documenté, sa traduction dans les contrats et les factures commence à peine.
- **Réutilisation** : présentation client achats et DSI (questions à poser aux prestataires sur la gouvernance) ; post LinkedIn (« une facture qui ne baisse pas n'est pas forcément une arnaque ») ; à citer avec précaution, en signalant le passage promotionnel.
