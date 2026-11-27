# Backlog R&D de Romain (OCTO)

Sujet de R&D mené hors mission : un sujet stratégique pour OCTO, en lien fort
avec l'expertise produit, qui produit des artefacts rapidement et se pitche pour
constituer une équipe.

**Dernière mise à jour** : 2026-11-27

## Mode d'emploi
- Chaque élément a un identifiant (`AP-12`, `SC-B`…), un statut et, si besoin,
  une priorité. On ne renumérote jamais : un élément abandonné garde son
  identifiant.
- Statuts : `à faire` · `en cours` · `fait` · `en attente` · `abandonné`.
- Priorités : `P1` (les 8 prochaines semaines) · `P2` (ensuite) · `P3` (idée).
- Pour ajouter une idée : une ligne dans la bonne épopée, statut `à faire`, sans
  priorité. On la priorise lors de la revue suivante.
- Les décisions et ce qui a été appris vont dans le **Journal**, en bas.
- Les éléments s'appuient sur la veille : cite la fiche ou la note quand c'est
  le cas (`sources/…`, `notes/…`).

---

## Sujet principal : l'agent comme produit

**Thèse** : un agent en production est un produit. Il a un propriétaire de
résultat, des utilisateurs, une valeur attendue, un coût unitaire, des evals,
un critère d'arrêt et une stratégie de sortie. La plupart des entreprises le
gèrent pourtant comme un projet technique.

**Pitch en une phrase** : « Les entreprises mettent des agents en production
comme on lançait des projets en 2010 : sans propriétaire, sans indicateur de
résultat, sans critère d'arrêt. On propose de les piloter comme des produits,
et on outille ça. »

**Pourquoi maintenant (signaux de la veille)**
- 23 % des entreprises ne savent pas qui répond d'une erreur d'IA ; 9 % jugent
  leurs chaînes d'agents entièrement gouvernées
  (`notes/2026-11-23-quotidienne.md`, fiche Deloitte du 13/11).
- Les dépenses IA réelles atteignent 2,5 fois le budget prévu (Menlo) ;
  Uber a épuisé son budget IA 2026 en quelques mois
  (`notes/2026-11-13-valeur-ia-budgets-2027.md`, `notes/2026-11-20-quotidienne.md`).
- La relecture et la vérification, pas la production, fixent le coût et le
  risque (`notes/2026-11-19-verification-goulot-ia-en-bourse.md`,
  `notes/2026-11-25-quotidienne.md`).
- La dépendance se déplace du modèle vers la couche agentique ; la
  réversibilité doit être testée (`notes/2026-11-26-quotidienne.md`).
- Chez OCTO, les publications sur les agents sont surtout techniques (harnais,
  comités d'agents, Lean, qualité du code) : le versant produit n'est pas couvert.

**Critères de réussite (à 8 semaines)**
- Un canvas testé sur au moins 3 agents réels.
- Un atelier joué au moins une fois en interne.
- Un article OCTO publié et un pitch qui a convaincu au moins 2 personnes.

### Paysage concurrentiel (relevé du 2026-11-27)
Recherche sur ce que publient les cabinets concurrents sur les agents, leur
gouvernance et le lien avec le produit. Sources : pages publiques des cabinets
(communiqués, blogs, annonces de recrutement), donc leur propre discours.

| Acteur | Ce qu'il fait sur le sujet | Angle | Recouvrement avec notre sujet |
|---|---|---|---|
| Thiga | Développe une offre « AI Product Ops / POM-AI » : refondre le cycle de développement produit avec l'IA, concevoir des équipes mixtes humains-agents (rôles, points de contrôle), construire de petits agents et mesurer leur impact ([annonce](https://jobs.lever.co/thiga/46434f51-1483-4100-b256-3f1fef577611)). Recrute des « AI Product Builder » et dit monter une équipe pour réinventer le product management ([annonce](https://jobs.lever.co/thiga/b9986cb5-e1e9-48ad-aac6-98c4ae782076)). | L'IA dans l'équipe produit | **Le plus proche** : même communauté, même discours produit. Mais leur objet est l'équipe produit outillée par l'IA, pas l'agent piloté comme un produit. |
| Converteo | Doctrine « product builder », rôles « Agentic Champions » et « Builders », cas en production (Lacoste, Fnac Darty), modèle opérationnel agentique ([article](https://converteo.com/en/blog/agentic-ai-project-enterprise/)). Mesure le ROI d'un agent par son taux d'adoption. | Construire et passer à l'échelle | Partiel : pas de propriétaire par agent, pas de coût unitaire, pas de critère d'arrêt. |
| Sopra Steria Next | CIO Compass d'octobre 2026 : « moins de 20 % des décisions automatisées ont un propriétaire métier identifié », moins de 25 % sont traçables de bout en bout ; cadre à neuf dimensions et « pile de souveraineté » à cinq couches (qui opère, qui peut remplacer, qui répond) ([communiqué](https://www.webdisclosure.com/press-release/ai-fewer-than-20-of-automated-decisions-have-an-identified-owner-szzCnmXYA8d)). Méthodologie non publiée. | Gouvernance des décisions, souveraineté, côté DSI | Fort sur la propriété et la réversibilité, mais vu de la DSI et de la conformité, pas du produit. |
| Capgemini Invent | Rapport avec UCL sur un modèle opérationnel « produit » pour des équipes humains-agents ([rapport](https://www.mgmt.ucl.ac.uk/sites/default/files/upload/Analytics%20Lab%202026%20.pdf)) ; fiche « Agentic Governance » sur le cycle de vie des agents et le retrait des moins performants ([PDF](https://www.capgemini.com/wp-content/uploads/2026/08/Agentic-Governance-One-Pager-2026_Final.pdf), non lisible en entier). | Usine à agents, grands comptes | Recouvre le cycle de vie et le retrait ; approche industrielle, peu outillée côté produit. |
| Wavestone | Benchmark cyber IA 2026 (88 % ont une gouvernance IA, 8 % intègrent les journaux IA à la supervision de sécurité), typologie des risques agentiques ([site](https://www.wavestone.com/en/), [RiskInsight](https://www.riskinsight-wavestone.com/en/?p=29128)). | Risque, cyber, conformité | Faible : complémentaire. |
| onepoint | Objectif interne : 100 % des collaborateurs « AI and agentic-ready » en 2026 ; démonstrations agentiques ([page IA](https://www.groupeonepoint.com/?p=13105748)). Pas d'offre publique repérée sur la gouvernance produit des agents. | Formation interne, data et cloud | Faible à ce stade. |

**Outils existants à connaître** : l'« AI Agent Canvas » d'Agentic Academy
(Boomi, mai 2026), neuf blocs en trois bandes : finalité, capacités,
contraintes ([page](https://agentic-academy.ai/posts/ai-agent-canvas/)) ; le
« Canvas Framework » de MongoDB (preuve de concept puis production)
([article](https://medium.com/mongodb/build-ai-agents-worth-keeping-the-canvas-framework-b582c40db00a)).
Ils couvrent la conception d'un agent, pas son pilotage économique : pas de coût
par tâche, pas de valeur ni de ROI, critère d'arrêt seulement partiel, rien sur
la réversibilité (changer de fournisseur), aucune vue de portefeuille.

**Ce que ça change pour nous**
- **Un canvas seul n'est pas un différenciant** : il en existe déjà. Notre
  apport est le **pilotage économique et le cycle de vie** de l'agent (coût par
  tâche réussie, valeur, critère d'arrêt, réversibilité) et la **vue
  portefeuille** (garder, améliorer, arrêter), avec le vocabulaire et les rites
  du produit.
- **Place libre** : personne ne relie la propriété des agents (sujet DSI chez
  Sopra Steria Next, Capgemini) à la culture produit (sujet de Thiga et
  Converteo). C'est notre pont.
- **Thiga est le concurrent direct** sur la communauté produit : se distinguer
  par l'objet (l'agent comme produit, pas l'équipe augmentée) et par la preuve
  (cas réels mesurés, à commencer par la veille).
- **Chiffre d'appel utile** : « moins de 20 % des décisions automatisées ont un
  propriétaire identifié » (Sopra Steria Next), à citer avec sa limite
  (méthodologie non publiée), à côté du 23 % de Deloitte.

### Épopée 1 : le canvas de l'agent produit
| ID | Élément | Statut | Priorité |
|---|---|---|---|
| AP-01 | Lister les rubriques du canvas à partir de la veille : propriétaire, résultat visé, utilisateurs, coût par tâche réussie, evals, garde-fous, critère d'arrêt, réversibilité | à faire | P1 |
| AP-02 | Canvas v0 sur une page | à faire | P1 |
| AP-03 | Appliquer le canvas aux agents de la veille (`veilleur`, `ficheur`, routine cloud) : premier cas réel | à faire | P1 |
| AP-04 | Mesurer le coût par fiche de la veille (tokens, durée, taux de fiches retenues) | à faire | P1 |
| AP-05 | Définir les evals de la veille : chiffres faux repérés, sources inaccessibles, fiches réutilisées | à faire | P1 |
| AP-06 | Tester le canvas sur 2 ou 3 agents d'OCTO ou de clients | à faire | P1 |
| AP-07 | Canvas v1 après les tests | à faire | P1 |
| AP-08 | Situer le canvas par rapport à l'AI Agent Canvas et au Canvas Framework de MongoDB : reprendre ce qui existe (finalité, garde-fous, escalade), ajouter ce qui manque (coût par tâche réussie, valeur, critère d'arrêt, réversibilité) | à faire | P1 |

### Épopée 2 : la revue de portefeuille d'agents
| ID | Élément | Statut | Priorité |
|---|---|---|---|
| AP-10 | Grille garder / améliorer / arrêter pour un portefeuille d'agents | à faire | P1 |
| AP-11 | Critères d'arrêt types, à partir des cas de la veille (Zefir, Uber, T-Mobile) | à faire | P1 |
| AP-12 | Test de réversibilité : comment changer de modèle ou de fournisseur pour un agent donné | à faire | P2 |
| AP-13 | Reprendre les trois questions de la « pile de souveraineté » de Sopra Steria Next (qui opère, qui peut remplacer, qui répond) et les traduire en rubriques produit | à faire | P2 |

### Épopée 3 : l'atelier
| ID | Élément | Statut | Priorité |
|---|---|---|---|
| AP-20 | Déroulé d'un atelier de 2h autour du canvas | à faire | P1 |
| AP-21 | Le jouer en interne (School of Product ou communauté produit OCTO) | à faire | P1 |
| AP-22 | Kit de mission : canvas, grille, atelier, exemples | à faire | P2 |

### Épopée 4 : publications
| ID | Élément | Statut | Priorité |
|---|---|---|---|
| AP-30 | Billet « J'ai traité ma veille comme un produit » (cas des agents de veille) | à faire | P1 |
| AP-31 | Article OCTO de fond sur l'agent comme produit | à faire | P1 |
| AP-32 | Série de posts LinkedIn tirés du canvas et des cas | à faire | P2 |
| AP-33 | Proposition de talk (meetup produit, conférence) | à faire | P3 |

### Épopée 5 : équipe et pitch
| ID | Élément | Statut | Priorité |
|---|---|---|---|
| AP-40 | Pitch de 5 minutes | à faire | P1 |
| AP-41 | Identifier les profils : ingénierie agentique, PO en mission sur un projet agentique, FinOps | à faire | P1 |
| AP-42 | Rituel de l'équipe (fréquence, format, outils partagés) | à faire | P2 |
| AP-43 | Intégrer le positionnement face aux concurrents dans le pitch (l'agent comme produit, pas l'équipe augmentée ; pilotage économique et portefeuille) | à faire | P1 |
| AP-44 | Suivre les publications des cabinets concurrents sur le sujet dans la veille (Thiga, Converteo, Sopra Steria Next, Capgemini Invent, Wavestone, onepoint) | à faire | P2 |

### Épopée 6 : monter en compétence avec l'IA
| ID | Élément | Statut | Priorité |
|---|---|---|---|
| AP-50 | Ajouter à la veille un thème dédié « l'agent comme produit » (propriété, evals, coût unitaire, arrêt, réversibilité) | à faire | P1 |
| AP-51 | Tenir un journal de R&D court après chaque session (section Journal) | à faire | P1 |
| AP-52 | Sessions de contradiction : Claude joue un CPO sceptique, un DSI centré sur le coût, un ingénieur qui juge le sujet superflu | à faire | P1 |
| AP-53 | Montée en compétence technique : evals, harnais agentiques, coût des tokens, à partir des fiches, avec questions de vérification | à faire | P2 |
| AP-54 | Produire les artefacts avec l'IA (pages, diaporamas, brouillons d'articles) en gardant le fond et les arbitrages | à faire | P2 |

---

## Sujets candidats (plus centrés sur le product management)
À creuser ; l'un d'eux pourra devenir un second sujet ou un module du premier.

### SC-A : la valeur et l'impact quand produire ne coûte plus rien
- **Statut** : à creuser
- **Thèse** : quand le volume livré n'a plus de valeur en soi, les indicateurs
  de livraison ne disent plus rien ; il faut mesurer le flux jusqu'au résultat
  et le travail réel.
- **Signaux** : Thiga (PM et P&L), Pezziardi et Lippi (travail réel), Torres
  (mesure d'impact), 89 % voient l'IA accélérer le travail contre 6 % qui
  montrent un ROI.
- **Artefact possible** : grille de mesure d'impact d'un produit, revue de
  valeur trimestrielle.

### SC-B : le mode produit révélé par l'IA
- **Statut** : à creuser
- **Thèse** : l'IA ne transforme pas les organisations restées en mode projet,
  elle les fait livrer plus vite sans meilleurs résultats.
- **Signaux** : `notes/2026-10-16-mode-produit-ere-ia.md`, Cagan (trois rôles
  produit), note budgets 2027.
- **Artefact possible** : autodiagnostic en 15 questions « votre organisation
  peut-elle tirer de la valeur de l'IA ? ».
- **Remarque** : se combine bien avec SC-A.

### SC-C : l'avenir du PO et du trio produit
- **Statut** : à creuser
- **Thèse** : le PO dédié est annoncé en voie de disparition, les rôles du trio
  se brouillent, le product builder devient une filière.
- **Signaux** : Cagan, article OCTO sur les archétypes produit, AI in Design Report, LinkedIn.
- **Artefact possible** : trajectoires d'évolution du PO, référentiel de
  compétences.
- **Remarque** : très attendu des grands comptes, plus politique à porter.

### SC-D : savoir arrêter un produit
- **Statut** : à creuser
- **Thèse** : décider de garder, d'améliorer ou d'arrêter devient central quand
  les budgets IA dérapent et que tout se lance vite.
- **Signaux** : Zefir, note budgets 2027.
- **Artefact possible** : critères d'arrêt et méthode de revue de portefeuille.
- **Remarque** : prolonge directement l'épopée 2 du sujet principal.

### SC-E : apprendre le métier produit quand l'IA fait le niveau 1
- **Statut** : à creuser
- **Thèse** : si l'IA prend les tâches d'entrée, il faut concevoir
  l'apprentissage des juniors.
- **Signaux** : Bain (cas Cisco), LinkedIn Associate Product Builder,
  mot-clé « talents juniors » (12 fiches).
- **Artefact possible** : parcours APM ou PO junior repensé.

---

## Questions ouvertes
| ID | Question | Statut |
|---|---|---|
| Q-1 | Quels sont les sujets stratégiques officiels d'OCTO ? Vérifier l'alignement du sujet principal | ouverte |
| Q-2 | Combien d'heures par semaine hors mission ? Ajuster le plan de 8 semaines | ouverte |
| Q-3 | Qui solliciter en premier pour l'équipe ? | ouverte |
| Q-4 | Le backlog et le journal doivent-ils rester privés ? (le dépôt GitHub est public) | tranchée : publics, sans noms de personnes sauf accord explicite |
| Q-5 | Le terrain des équipes mixtes humains-agents est occupé par Thiga : le laisser de côté, ou l'aborder sous l'angle de l'agent comme membre d'un portefeuille ? | ouverte |
| Q-6 | Un canvas existe déjà (AI Agent Canvas) : créer le nôtre, ou proposer une extension « pilotage et portefeuille » de l'existant ? | ouverte |

---

## Journal
- **2026-11-26** : choix du sujet principal « l'agent comme produit » parmi
  trois pistes (les deux autres : P&L d'une fonctionnalité IA, discovery à
  l'heure du code gratuit). Cinq sujets plus centrés produit identifiés
  (SC-A à SC-E), à creuser. Création de ce backlog. Décision : le backlog est
  public (dépôt GitHub), sans noms de collègues ni de clients sauf accord.
- **2026-11-27** : confrontation du sujet aux concurrents (Thiga, Converteo,
  Sopra Steria Next, Capgemini Invent, Wavestone, onepoint) et aux canvas
  existants. Conclusion : le canvas seul n'est pas différenciant ; l'apport porte
  sur le pilotage économique, le cycle de vie et la vue portefeuille, en reliant
  la gouvernance (sujet DSI) à la culture produit. Ajout de AP-08, AP-13, AP-43,
  AP-44, Q-5 et Q-6.
