# Signal part en guerre contre les agents IA d'Apple et de Google pour protéger les conversations privées

**Référence** : Mathilde Florentin, Siècle Digital, 24 novembre 2026, article d'actualité (s'appuie sur un billet de blog de Signal), https://siecledigital.fr/2026/11/24/signal-part-en-guerre-contre-les-agents-ia-dapple-et-de-google-pour-proteger-les-conversations-privees/

**Axe** : IA appliquée au produit

## 1. L'idée clé
Les assistants IA intégrés aux systèmes d'exploitation lisent ce qui s'affiche à l'écran, là où le chiffrement de bout en bout ne protège plus rien. Signal répond en bloquant par défaut leur accès à ses conversations sur iOS 27 et Android, tout en reconnaissant que ces parades restent incomplètes face à un environnement « de plus en plus hostile à la vie privée ».

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Siècle Digital, Meta et Muse](2026-11-23-siecle-digital-meta-muse-incidents.md) (même autrice), sur un agent qui interprète largement ses autorisations et fait remonter des données confidentielles, la fiche [Solutions Numériques, OpenRouter et vols de conversations](2026-11-24-solutions-numeriques-openrouter-vols-conversations.md), et le précédent de Signal contre Recall de Microsoft sous Windows 11 l'an dernier.
- **La lecture d'écran par les agents devient une faille admise** : le chiffrement protège les messages en transit, pas une fois déchiffrés et affichés. Les agents d'OS (Siri AI, Gemini Intelligence) peuvent lire et stocker ce contenu.
- **Une application tierce se défend contre la plateforme qui l'héberge** : fonction « Block Siri AI » sur iOS 27 (captures d'écran bloquées par défaut), Screen Security activé automatiquement sur Android dès qu'un assistant tente de lire l'écran. Là où la fiche Muse décrivait les dérapages d'un agent vus de l'intérieur, on voit ici la riposte d'un éditeur tiers, étendue de Windows (Recall) aux deux grands systèmes mobiles.
- **Des limites assumées** : l'agent peut encore passer par les fichiers stockés sur le téléphone, et rien n'est possible sur Mac, où Signal conseille d'exclure l'application de Siri AI dans les réglages.

## 3. Résumé
L'article part de l'annonce de Signal : la messagerie ajoute des protections pour empêcher les assistants IA de lire le contenu de ses conversations à l'écran, sur iOS 27 et certaines versions d'Android, face à Siri AI et Gemini Intelligence. Le contexte est la multiplication des agents IA et des incidents récents chez Meta autour de données confidentielles. Meredith Whittaker, présidente de la Signal Foundation, explique dans un billet que ces intégrations rendent l'environnement de plus en plus hostile à la vie privée. Le mécanisme du risque est simple : pour répondre ou chercher, l'agent lit l'écran et peut stocker ce qu'il voit, alors que le chiffrement ne protège que la transmission. Signal bloque donc les captures d'écran par défaut sur iOS 27 (« Block Siri AI ») et active Screen Security sur Android dès qu'un assistant tente de lire l'écran, comme elle l'avait fait l'an dernier contre Recall sous Windows 11. L'article termine sur les limites reconnues par Signal : accès possible par les fichiers stockés, impossibilité de bloquer les captures sur Mac, et recommandation d'exclure manuellement Signal de Siri AI dans macOS.

## 4. Citations et noms
**Citations** :
- L'environnement devient « de plus en plus hostile à la vie privée », Meredith Whittaker, présidente de la Signal Foundation (citation partielle rapportée par l'article).

**Noms cités** :
- *Signal / Signal Foundation* : messagerie chiffrée qui bloque les agents IA d'OS.
- *Meredith Whittaker* : présidente de la Signal Foundation, autrice du billet.
- *Siri AI (Apple), Gemini Intelligence (Google)* : assistants IA intégrés aux OS, visés par les protections.
- *Block Siri AI, Screen Security* : fonctions de Signal sur iOS 27 et Android.
- *Recall (Microsoft)* : précédent de l'an dernier, contre lequel Signal avait bloqué les captures sous Windows 11.
- *Meta* : cité pour des incidents récents de fuite de données confidentielles (agent Muse).

## 5. Mots-clés
agents IA, conception de produits IA, sécurité, données personnelles, autonomie des agents

## Lecture CPO
- **Implications** :
  - Pour tout produit qui affiche des données sensibles (santé, banque, RH, messagerie interne) : intégrer au cadrage le scénario « un agent d'OS lit mon écran », et décider explicitement de ce qu'on bloque par défaut.
  - Pour les équipes qui conçoivent des agents : l'accès à l'écran et aux autres applications va se heurter à des refus des éditeurs tiers ; prévoir des voies d'accès autorisées (API, consentement) plutôt que la lecture d'écran.
  - Pour les DSI : les agents d'OS sur les postes et mobiles de l'entreprise posent une question de confidentialité que le chiffrement des outils ne règle pas.
- **Fiabilité** : article court qui relaie le billet de Signal, partie prenante qui défend son positionnement sur la vie privée. Pas de données d'incident chiffrées ni de réponse d'Apple ou de Google.
- **Maturité** : Signal faible : premières mesures d'un éditeur isolé, mais qui préfigurent un conflit plus large entre agents d'OS et applications tierces.
- **Réutilisation** : post LinkedIn sur « le chiffrement ne protège plus ce que l'agent lit à l'écran » ; point de vigilance dans un atelier de conception de produit IA ou une présentation sur la sécurité des agents, avec la fiche Muse.
