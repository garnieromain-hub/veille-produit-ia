# L'IA dans la discovery produit — veille du 16 octobre 2026

## En une phrase
L'IA rend la discovery moins chère (prototypes, préparation, synthèse), pas facultative : les références convergent pour dire que le goulot passe de la construction au jugement, et que le contact avec de vrais utilisateurs reste non délégable.

## Les quatre mouvements à retenir

### 1. Le goulot se déplace de la delivery vers la discovery
Construire ne coûte presque plus rien, donc décider quoi construire devient le travail. Cagan défend des prototypes multiples, testés en parallèle chaque semaine, y compris sur données réelles. Il prévient aussi : une organisation en mode projet accélérée par l'IA produit seulement de mauvais produits plus vite.
→ [Fiche SVPG](../sources/2026-10-16-svpg-build-to-learn-vs-build-to-earn.md). Même idée chez Cat Wu (Anthropic), via la [fiche SFEIR](../sources/2026-10-15-sfeir-pm-ere-ia-exponentielle.md) : prototyper avant d'écrire un PRD.

### 2. L'IA accélère la recherche, mais seulement aux deux bouts
Elle aide en amont (scripts, recrutement, recherche documentaire) et pour une première passe d'analyse (transcription, codage). Au milieu, elle échoue : elle n'observe pas, ne modère pas un test d'utilisabilité, et ses regroupements restent superficiels. Les intervieweurs IA servent pour des retours structurés en volume, pas pour l'exploration.
→ [Fiche NN/g Accelerating Research with AI](../sources/2026-10-16-nngroup-accelerer-recherche-ia.md)

### 3. Utilisateurs synthétiques : le débat se précise
Il ne s'agit plus de savoir si l'IA remplace les utilisateurs : il faut regarder sur quelles données repose la simulation. Les personas générés par un LLM sont lisses, complaisants, et donnent des tendances sans magnitude. Les jumeaux numériques construits à partir de vrais entretiens atteignent 0,85 de précision. Conséquence pratique : vos entretiens passés deviennent un actif, si votre référentiel de recherche est bien tenu.
→ [Fiche NN/g jumeaux numériques](../sources/2026-10-16-nngroup-jumeaux-numeriques-utilisateurs-synthetiques.md)

### 4. Sur les produits IA, la discovery continue après le lancement
Pour Teresa Torres, les evals sont une nouvelle habitude de discovery : lire des traces, catégoriser les erreurs, définir ce qu'est une « bonne » réponse. Ce travail revient au PM, pas à l'éditeur d'outils.
→ [Fiche Torres AI Evals](../sources/2026-10-16-torres-ai-evals-habitude-discovery.md)

## Signal faible
Des praticiens encodent les méthodes de discovery dans des agents. Exemple : six skills Claude qui reprennent le pipeline de Torres, avec filtre ICP, extraction d'opportunités, regroupement et dimensionnement (Else van der Berg, présenté sur productize.life). Cela vaut le coup d'œil pour l'idée d'inscrire des règles de jugement dans l'outil (« un écart est un signal »). En revanche : ni date, ni auteur clair, ni retour d'usage, donc pas de fiche.

## Ce que j'ai écarté et pourquoi
- **Contenus d'éditeurs d'outils d'entretien IA** (Perspective AI notamment) : très nombreux en 2026, avec des chiffres spectaculaires (« -94 % de time-to-insight ») sans méthodologie vérifiable. C'est du marketing.
- **Lenny's Newsletter, Aparna Chennapragada (Microsoft)**, « Prompt sets are the new PRDs » : formule utile, mais l'épisode date de mai 2025 et seules les notes sont accessibles sans transcription. Pas de fiche.
- **Torres, « Lessons from 9 AI Product Teams »** (nov. 2025) : réservé aux abonnés payants et centré sur la construction de produits IA plutôt que sur la discovery.
- **Cagan, positions sur le « product management theater »** : trouvées seulement dans des résumés tiers, parfois générés par IA. Source originale à retrouver avant de citer.

## Tensions à exploiter (tables rondes, clients)
- **Vitesse ou profondeur** : Cagan pousse à multiplier les prototypes, NN/g rappelle que l'IA rend les insights plus superficiels. Où met-on le curseur ?
- **Qui juge ?** Torres place la définition du « bon » chez le PM. Dans beaucoup d'organisations, ce travail glisse vers la data ou vers l'éditeur.
- **Faire plus de discovery, ou faire semblant ?** Le prototypage IA peut nourrir l'apprentissage ou alimenter un « théâtre » de démos convaincantes.

## Angles de réutilisation
- **Article OCTO** : « L'IA ne supprime pas la discovery, elle la déplace », structuré par les quatre mouvements.
- **Post LinkedIn** : « Votre synthèse d'entretiens par IA est un premier jet, pas un insight » (NN/g).
- **Présentation client** : tableau « ce que l'IA fait / ne fait pas » à chaque étape de discovery, plus la grille d'evals de Torres pour les équipes qui construisent de l'IA.

## Sources fichées
- Teresa Torres, *AI Evals: A Hands-On Guide for Product Teams*, Product Talk, 2 sept. 2026
- Marty Cagan, *Build to Learn vs Build to Earn*, SVPG, 16 avril 2026
- Moran et Rosala, *Accelerating Research with AI*, NN/g, révisé le 21 janv. 2026
- Raluca Budiu, *Evaluating AI-Simulated Behavior*, NN/g, 15 août 2025
- Réutilisée : Thomas Gros, SFEIR Institute, 27 mars 2026 (fiche existante)
