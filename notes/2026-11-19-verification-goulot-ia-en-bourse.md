Fiches créées : 10 ([index des articles](../liste-articles.md))

# Tous les axes, la vérification devient le goulot et l'IA entre en Bourse : veille du 19 novembre 2026 (12 au 19 novembre 2026)

*Veille automatique. La dernière veille date du 13 novembre : j'ai appliqué le minimum de 7 jours, donc du 12 au 19 novembre. J'ai fait trois exceptions. Lenny Rachitsky (10 novembre) est retenu parce que la veille du 13 novembre concluait à tort « pas de nouvelle donnée sur le marché de l'emploi PM » : ce baromètre l'avait manqué. Mollick (9 novembre) est placé en source complémentaire pour la même raison. Le Radar Thoughtworks est daté « novembre 2026 » sans jour précis. Doublons vérifiés dans `liste-articles.md` et `sources/` : aucun lien retenu n'y figurait. **Conflit d'intérêts** : cette veille est rédigée par un modèle d'IA d'Anthropic, et l'introduction en Bourse d'Anthropic est un fait marquant de la semaine. J'ai limité la fiche concernée aux chiffres publiés par Crunchbase et Renaissance Capital, signalé les écarts, et je te demande de la relire avant toute réutilisation publique.*

## En une phrase
Produire du code et des contenus avec l'IA ne coûte presque plus rien. Ce qui devient rare et cher, c'est la vérification (revue, tests, jugement), le contexte et l'infrastructure. Pour un CPO, cela veut dire trois choses : mesurer le flux jusqu'à la production plutôt que le volume généré, garder des PM capables de juger (le marché les recrute plus que jamais), et traiter le coût et la dépendance aux fournisseurs d'IA comme des risques de portefeuille, maintenant que le premier lab de pointe est coté.

## Les mouvements à retenir

### 1. Le goulot passe de la production à la vérification
Les sources de la semaine convergent, de l'éditeur au praticien. Thoughtworks (Radar 35) écrit que l'attention et la capacité de revue des développeurs deviennent le goulot, et classe en « Caution » deux pratiques : le débit de code comme mesure de productivité, et le « théâtre » de la validation humaine, où l'on approuve ce qu'on ne peut pas juger. Satya Nadella (Pragmatic Engineer, 16 novembre) dit la même chose côté éditeur : le code est bon marché, la vérification ne l'est pas, et certains modèles contournent les objectifs en supprimant les tests qui échouent. Le cas extrême de CodeRabbit (Harjot Gill, plus de 5 000 PR en un mois) va plus loin : il annonce la fin de la revue humaine des PR, remplacée par la vérification automatique et un droit de livrer qu'on retire après incident. Chez Ploquin (OCTO), l'équipe observée remplace la couverture de tests unitaires par des tests fonctionnels, sans savoir encore mesurer la qualité. Mollick ajoute la limite côté modèle : les agents ne savent pas juger la qualité de leur propre travail.
Désaccord : Thoughtworks et Nadella gardent l'humain dans la vérification, à condition qu'il puisse juger ; Harjot Gill veut le sortir de la revue au profit de garde-fous automatiques.
→ [Fiche Thoughtworks](../sources/2026-11-19-thoughtworks-radar-vol35.md), [Fiche Nadella](../sources/2026-11-19-pragmatic-engineer-nadella-code-bon-marche.md), [Fiche OCTO Ploquin](../sources/2026-11-19-octo-ploquin-lean-ia-delivery.md), [Fiche Cagan, paradoxe de productivité](../sources/2026-10-16-svpg-ai-productivity-paradox.md) (réutilisée)

### 2. Contexte écrit ou contexte vécu : le débat sur la façon de nourrir les agents
Deux thèses s'opposent nettement cette semaine. Ploquin (OCTO) montre qu'une équipe qui écrit ses standards dans le dépôt (vision produit, règles métier, glossaire de termes bannis) obtient de l'IA du « conforme » plutôt que du « plausible ». Il propose une pratique concrète : séparer les specs (l'état du produit, tenues par les développeurs) des changes (les demandes, écrites par le PM). Thoughtworks outille cette voie (harnais, « feedback flywheel », mais aussi alerte sur l'inflation des instructions). Cutler (TBM 452) répond que les experts ne savent pas expliciter leur savoir, que le contexte se crée dans le travail partagé, et que son équipe, après avoir tout essayé, a simplement tenu une réunion. Mind the Product apporte un outil pour arbitrer, côté produit : le niveau d'autonomie confié à l'IA se décide tâche par tâche selon le coût de l'erreur, et le niveau 4 (autonomie complète) n'est pas une cible.
→ [Fiche OCTO Ploquin](../sources/2026-11-19-octo-ploquin-lean-ia-delivery.md), [Fiche Cutler](../sources/2026-11-19-cutler-tbm-452-contexting.md), [Fiche Mind the Product](../sources/2026-11-19-mtp-quatre-niveaux-autonomie-ia.md), [Fiche Thoughtworks](../sources/2026-11-19-thoughtworks-radar-vol35.md)

### 3. L'emploi se recompose : les PM montent, le design, la recherche et les juniors reculent
Le baromètre de Lenny (TrueUp et Live Data Technologies) contredit la « fin du PM ». Les offres PM sont au plus haut depuis près de quatre ans, et les PM gardent la part d'embauches la mieux préservée (21 %). À l'inverse, les offres d'ingénieurs stagnent (+2,5 % sur un an), le design est au plus bas (−28 %) et il ne reste que 108 offres de recherche utilisateur dans le monde. « LLM » devient la compétence la plus citée dans les offres PM, et « evals » progresse. Nadella confirme la recomposition chez un grand employeur : départs volontaires proposés à la plupart des ingénieurs, recrutement junior ralenti pendant la réorganisation, et un programme de compagnonnage des juniors avec Carnegie Mellon. En France, France Travail (16 000 établissements) donne une photographie plus calme. 38 % des employeurs utilisent ou testent l'IA, 6 % pensent qu'elle pourrait concurrencer l'humain sur leur métier principal à cinq ans, mais 22 % seulement des employeurs utilisateurs ont formé leurs équipes.
Désaccord : la scission du rôle décrite par [Cagan](../sources/2026-11-13-svpg-ai-future-product-role.md) (le PO dédié condamné) et le marché américain qui recrute des PM ne se contredisent pas forcément : les offres concernent des PM, pas des PO. Mais aucun chiffre ne mesure encore la disparition du PO.
→ [Fiche Lenny](../sources/2026-11-19-lenny-marche-emploi-tech-fin-2026.md), [Fiche Nadella](../sources/2026-11-19-pragmatic-engineer-nadella-code-bon-marche.md), [Fiche France Travail](../sources/2026-11-19-france-travail-ia-entreprises-metiers.md)

### 4. Le coût de l'IA déborde les budgets, et ce sont les projets IA qui paient
En France, 79 % des entreprises ont dépassé leurs prévisions de dépenses d'infrastructure, et 75 % d'entre elles citent l'IA (étude Cebr pour Wasabi). L'IA est le poste le plus imprévisible (22 %, contre 8 à 12 % pour les autres), avec un dépassement moyen de 20 %. L'effet de report touche le portefeuille : 28 % des entreprises (tous pays) ont déjà retardé ou réduit un projet IA pour des raisons de coût, et en France 39 % désignent les projets IA et data comme les premiers à perdre des financements. Les fournisseurs en tirent les conséquences : Microsoft annonce à Ignite des plafonds et des alertes de dépense par agent, et Thoughtworks rappelle que « l'économie des tokens se ramène à l'économie de l'infrastructure ». C'est la suite directe du mouvement 3 de la veille du 13 novembre (Menlo : budgets réels à 2,5 fois le plan).
→ [Fiche Cebr / IT for Business](../sources/2026-11-19-cebr-wasabi-depassements-infrastructure-ia.md), [Fiche Menlo](../sources/2026-11-13-menlo-state-of-enterprise-ai-2026.md) (réutilisée), [Fiche Thoughtworks](../sources/2026-11-19-thoughtworks-radar-vol35.md)

### 5. L'IA entre en Bourse, l'Europe compte ses forces
Anthropic a fixé son prix d'introduction à 83 $ le 18 novembre, au-dessus de la fourchette, pour plus de 92 Md$ levés avec le placement privé, et la cotation au Nasdaq commence le 19 novembre. Le S-1, lu par Crunchbase, donne pour la première fois des chiffres audités de la dépense des entreprises vue du côté d'un fournisseur. Il en ressort 17 Md$ de revenus au troisième trimestre (x12 sur un an) et plus de 11 900 clients à plus de 100 000 $. On y lit aussi 895 Md$ d'engagements de calcul, l'équivalent pour un seul acteur du risque d'infrastructure que Gartner pointait en octobre. La même semaine, Jensen Huang quitte Nvidia (12 novembre), qui était devenu le premier investisseur corporate de l'IA (121 tours en 2026). En Europe, Atomico chiffre 2026 à environ 81 Md$ (+62 %), et la France double ses levées (12,3 Md$ attendus). Mais le cycle de l'IA a divisé par deux la part européenne de l'investissement mondial, et l'Europe ne détient que 7 % du calcul mondial.
→ [Fiche Crunchbase Anthropic](../sources/2026-11-19-crunchbase-anthropic-ipo-chiffres-cles.md), [Fiche Atomico / Maddyness](../sources/2026-11-19-maddyness-atomico-state-european-tech-2026.md), [Fiche Crunchbase T3](../sources/2026-11-13-crunchbase-q3-2026-capital-risque.md) (réutilisée)

## Par axe
- **Product management** : le baromètre de Lenny (PM en hausse, design et recherche au plus bas) et la grille d'autonomie de Mind the Product. Torres publie le chapitre « mesurer l'impact » de son club de lecture, sans rien sur l'IA. Pas de nouvelle prise de position de Cagan ni de Pichler.
- **IA appliquée au produit** : l'axe le plus riche, avec le Radar Thoughtworks 35, le retour terrain d'OCTO (Ploquin) et le cas CodeRabbit. Microsoft annonce à Ignite des agents autonomes dotés d'une identité et d'un responsable désigné.
- **Transformation des entreprises** : France Travail (première grande enquête française sur l'IA chez les employeurs), Nadella sur la réorganisation de Microsoft, Cutler sur le contexte.
- **Portefeuille numérique** : rien de notable en propre pour la deuxième veille consécutive. Le sujet n'avance que par la bande : projets IA reportés faute de budget (Cebr), « path-to-production mapping » comme outil de flux (Thoughtworks), et des contenus d'éditeurs (OnePlan, Planisware, ITONICS) écartés. **Recherche ciblée à faire à la prochaine veille** (lean portfolio management, financement par produit, rationalisation applicative, côté Gartner, Forrester et praticiens).
- **Investissement tech** : très actif sur le volet capital-risque (introduction en Bourse d'Anthropic, Atomico, Nvidia, voice AI, fonds européens Plural et Orange Ventures). Sur le volet budgets, l'étude Cebr est la seule nouveauté de la semaine.

## Ce que disent les chiffres
- **Lenny's Newsletter, 10 novembre** : TrueUp (offres, plus de 9 000 entreprises tech) et Live Data Technologies (embauches, 124 millions de parcours, États-Unis). Fiabilité bonne pour les tendances, avec plusieurs limites. Les données ne couvrent que les entreprises tech, très majoritairement américaines, et la méthodologie détaillée n'est pas publiée. Écart à signaler : le ratio PM/design de mars (1,27) n'est pas comparable aux ratios cités en novembre (1,9 début 2023, 3,8 aujourd'hui), le périmètre ayant visiblement changé.
- **France Travail, novembre 2026** : 16 000 établissements, privé et public hors fonction publique d'État, métropole et outre-mer. C'est la source la plus solide de la semaine : opérateur public, sans rien à vendre, échantillon très large. Je n'ai pas lu les dates de collecte ni la pondération (elles sont dans les PDF). Écart de reprise : Presse-citron présente les résultats comme « rassurants », ce qui est un cadrage éditorial. Certaines reprises citent les 70 % d'attente de maîtrise de l'IA générative comme s'ils portaient sur tous les employeurs, alors qu'ils ne concernent que les employeurs déjà utilisateurs.
- **Cebr pour Wasabi, 18 novembre** : Sapio Research, 690 décideurs, huit pays, juillet-août 2026, environ 100 répondants en France sur certaines questions. Fiabilité moyenne à faible. Le commanditaire vend un stockage « sans frais cachés » et l'étude parle de frais fournisseurs opaques ; l'extrapolation à 5,4 Md$ pour la France est un modèle, pas une mesure. À citer pour les ordres de grandeur (79 %, 20 % de dépassement, 28 % de projets retardés).
- **S-1 d'Anthropic, via Crunchbase (18 novembre) et Renaissance Capital (10 novembre)** : les chiffres déposés à la SEC sont la meilleure source possible, mais je ne les ai pas lus à la source (document trop volumineux). Les reprises divergent sur plusieurs points. Les engagements de calcul vont de 637 Md$ (S-1 initial du 26 octobre, selon Tomasz Tunguz) à 895,4 Md$ (dépôt amendé), avec 900,9 Md$ chez certains. Crunchbase rattache les 11 900 clients à plus de 100 000 $ à Claude Code, Renaissance à tous les produits. La marge brute n'est pas publiée : les 40 %, 44 % ou 85 % qui circulent sont des calculs d'analystes. Un flash de la plateforme KuCoin annonce « 10,5 Md$ levés », chiffre incompatible avec tous les autres : à ignorer.
- **Atomico, State of European Tech 2026** : rapport d'un fonds, montants 2026 projetés à mi-novembre, méthodologie non lue. Maddyness cite deux montants pour l'investissement IA et calcul (9,5 et 20 Md$) sans les réconcilier : à ne pas reprendre avant vérification.
- **À ne pas citer en l'état** : les comparatifs de coût de Microsoft contre Claude (−84 %) et ChatGPT (−63 %) viennent d'un rapport GigaOm présenté par Microsoft ; les enquêtes sur les licenciements dus à l'IA publiées par des éditeurs de CV (ResumeTemplates, Resume Genius) ont des méthodes faibles ou non publiées.

## Le contrepoint
La thèse dominante de la semaine est que l'IA rend la production quasi gratuite : il suffirait d'écrire le bon contexte et de mettre assez d'agents au travail. Le meilleur contrepoint vient de John Cutler. Le savoir qui compte est tacite, les experts ne savent pas l'expliciter à la demande, et confondre une bonne explication avec un bon jugement mène à confier le contexte des agents à la personne la plus éloquente plutôt qu'à la plus compétente. Deux autres sources le renforcent. Mollick, enthousiaste, constate pourtant que les meilleurs modèles produisent un travail « exact et sans joie », construisent des bureaucraties (un règlement de 87 500 mots en douze jours) et ne savent pas juger quand leur travail n'est pas assez bon. Thoughtworks met en garde contre l'inflation des instructions d'agents et contre la validation humaine de façade. Mises bout à bout, ces sources disent que l'IA ne supprime pas le travail de jugement. Elle le concentre sur moins de personnes, à un moment où le marché réduit justement les juniors, les designers et les chercheurs qui le portaient.

## Signal faible
- **OCTO, Nicolas Ploquin** : la séparation specs (tenues par les développeurs) / changes (écrits par le PM) est une pratique produit concrète et nouvelle. Avec les séries de Claude Camus et Bruno Boucard, OCTO accumule des retours de terrain sur le travail avec agents. Il manque encore une synthèse orientée CPO.
- **Microsoft Autopilot** : des agents qui ont leur propre identité, un responsable désigné et des journaux d'audit à leur nom. La gouvernance des agents commence à ressembler à celle des salariés : à suivre pour les modèles opérationnels.
- **Dassault Systèmes, Capital Markets Day du 17 novembre** : selon un communiqué repéré via ActuIA (non lu en entier), l'éditeur prévoit une tarification à l'usage liée au travail de ses « compagnons virtuels » d'IA. Si les grands éditeurs passent à une tarification au travail fourni, les business cases et les budgets logiciels changent de nature.
- **Départ de Jensen Huang de Nvidia (12 novembre)** : la directrice financière par intérim était réputée réservée sur l'ampleur des paris d'investissement, selon Reuters cité par Crunchbase. Le premier investisseur corporate de l'IA pourrait ralentir.
- **Filières de formation « AI Product Management »** : IIM Calcutta et IIT Delhi lancent des programmes longs (18 novembre), au motif d'une pénurie de talents. Ce sont des annonces promotionnelles, mais elles signalent l'institutionnalisation du rôle.
- **Thiga et Converteo** : je n'ai pas pu consulter leurs blogs (404 pour Thiga, redirection vers le site nord-américain pour Converteo). À revoir à la prochaine veille.

## Ce que j'ai écarté et pourquoi
- **SEC, S-1/A d'Anthropic** : inaccessible (document de plus de 10 Mo, au-delà de la taille lisible). J'ai lu les chiffres via Crunchbase et Renaissance Capital.
- **PitchBook, « Anthropic IPO live updates »** et **Morningstar, « 3 charts on Anthropic's IPO filing »** : inaccessibles (erreur 403).
- **Renaissance Capital, « Anthropic sets terms »** (10 novembre) : redite de la fiche Crunchbase, plus récente, mais utilisé pour recouper les chiffres.
- **Tomasz Tunguz, analyse du S-1** (26 octobre) : hors période. C'est un calcul d'analyste (marge brute dérivée), mentionné pour l'écart sur les engagements de calcul.
- **CNBC, « speculative fiction or generational moment »** (27 octobre) et **Crunchbase, tribune « AI IPO wave is the dot-com bubble's evil twin »** (22 octobre) : hors période.
- **KuCoin, flash sur le prix d'introduction** : chiffre de levée incohérent, source non fiable.
- **Sifted** : inaccessible (erreur 403).
- **Thiga** (blog en 404) et **Converteo** (redirection vers le site nord-américain) : inaccessibles.
- **John Cutler, TBM 451** (12 novembre) : sans lien avec l'IA ni avec les équipes produit.
- **Teresa Torres, Ch. 11 « Measuring Impact »** : guide de lecture sans apport sur l'IA, placé en source complémentaire.
- **Lenny's Newsletter, « 35 premium tools free for a year »** (17 novembre) : contenu promotionnel.
- **Simon Willison, billets de novembre** : usages techniques sans rapport direct avec le périmètre.
- **Journal du Net, Jacques Hanen, « L'IA ne sauvera pas les DSI qui ne savent pas piloter leur portefeuille »** : publié le 7 juillet 2026, donc hors période, et il s'appuie sur le chiffre MIT de 95 % d'échecs, très discuté.
- **ITPro, enquête Cloudera sur les coûts de tokens** (28 octobre) : hors période. Elle est seulement citée dans la fiche Cebr, et Cloudera est un éditeur.
- **BCG, IT Spending Pulse** (17 septembre) et **Applied AI Index** (30 septembre) : hors période.
- **BCG, agents IA dans les banques** (12 novembre) : contenu non lu (titres seulement), et sectoriel.
- **Dataiku et Harris Poll, gouvernance des agents** (29 octobre) : hors période. **Red Hat, 1 400 DSI** : non lu à la source.
- **OnePlan (communiqué de la version de novembre), Planisware, ITONICS** : contenus d'éditeurs de PPM, promotionnels.
- **Mind the Product, Eric Simons (Bolt)** (2 novembre) : hors période.
- **Enquêtes sur les licenciements dus à l'IA** (ResumeTemplates, Resume Genius, Resume.org) : émises par des éditeurs de CV, méthodologie faible.
- **Annonces de formations IIM Calcutta, IIT Delhi, ProductDive, Udacity** : promotionnelles, citées seulement en signal faible.
- **Crunchbase, tribunes d'invités** (recruter des jeunes diplômés managers, risque plateforme, risque fondateur) : opinions sans données.
- **Presse-citron sur l'étude France Travail** : reprise, utilisée seulement pour signaler l'écart de cadrage.
- **ActuIA, veille du 18 novembre** : agrégateur, utilisé seulement pour repérer des sources.

## À récupérer par Romain
- **Lenny's Newsletter, conclusion 7** (« le marché tech croît surtout hors des rôles logiciels ») : réservée aux abonnés, et c'est la conclusion qui relativise toutes les autres.
- **Pragmatic Engineer, transcriptions des épisodes Nadella (16 novembre) et Harjot Gill (18 novembre)** : réservées aux abonnés. Il faut vérifier les citations et ce que Nadella dit des rôles produit, absents des notes d'épisode.
- **S-1/A d'Anthropic sur EDGAR** : pour la concentration des clients, la marge et le détail des engagements de calcul, à lire directement plutôt que via les reprises (et à relire par un humain, vu le conflit d'intérêts signalé).
- **France Travail, *Éclairages & Synthèses* n° 90 et n° 91 (PDF gratuits)** : pour la méthodologie (dates de collecte, pondération) et les projections à cinq ans par métier.
- **Atomico, rapport complet *State of European Tech 2026*** : pour la méthodologie et le bon chiffre d'investissement IA et calcul.
- **Dassault Systèmes, présentation du Capital Markets Day du 17 novembre** : pour vérifier le modèle de tarification à l'usage des compagnons virtuels.
- **McKinsey, *The state of AI in 2026*** : toujours en attente depuis la veille du 13 novembre.

## Tensions à exploiter
- **Faut-il tout écrire pour les agents ?** Ploquin (standards dans le dépôt, du « conforme » plutôt que du « plausible ») contre Cutler (le contexte naît du travail partagé, « alors nous avons tenu une réunion »).
- **La revue humaine est-elle morte ?** Harjot Gill (CodeRabbit) la déclare finie ; Thoughtworks la juge indispensable mais dénonce sa version de façade.
- **Qui fera la discovery ?** Les PM sont recherchés, mais les designers et les chercheurs utilisateurs disparaissent des offres (108 offres de UXR dans le monde).
- **Former ou réorganiser ?** En France, 22 % des employeurs utilisateurs ont formé leurs équipes ; chez Microsoft, on propose des départs volontaires et on gèle les juniors.
- **Bulle ou infrastructure ?** Plus de 92 Md$ levés et une demande « très supérieure » à l'offre pour Anthropic, contre 895 Md$ d'engagements fixes face à des revenus de consommation sans engagement.
- **Souveraineté européenne** : la France double ses levées, mais l'Europe a 7 % du calcul mondial et la moitié de sa part d'investissement d'avant le cycle de l'IA.

## Angles de réutilisation
- **Article OCTO** : « Le code est gratuit, la vérification ne l'est pas ». Structure : le déplacement du goulot (Thoughtworks, Nadella), le théâtre de la validation humaine, la réponse de terrain (Ploquin : specs et changes, standards), le contrepoint (Cutler, Mollick), et une grille pour le CPO. La grille croise ce qu'il faut mesurer (flux jusqu'à la production, pas le volume de code), qui vérifie quoi, et le niveau d'autonomie par tâche selon le coût de l'erreur (Mind the Product).
- **Posts LinkedIn** :
  - « Le débit de code n'est pas une mesure de productivité. Même le Radar Thoughtworks le dit. »
  - « Les PM gagnent, les designers et les chercheurs disparaissent des offres. Qui fera la discovery ? » (Lenny)
  - « 38 % des employeurs français utilisent l'IA. 22 % de ceux-là ont formé leurs équipes. » (France Travail)
  - « 79 % de dépassement sur l'infrastructure, et ce sont les projets IA qui paient. » (Cebr, à présenter avec la réserve sur le commanditaire)
- **Table ronde (School of Product ou client)** : « Contexte écrit ou contexte vécu ? », avec Ploquin et Cutler face à face, puis la grille d'autonomie de Mind the Product.
- **Présentation client DSI ou comex** : la photographie française (France Travail, Cebr) face aux données américaines (Lenny, S-1 d'Anthropic), et le risque fournisseur (engagements de calcul, routage multi-modèles, réversibilité selon Nadella et Thoughtworks).

## Sources fichées
**Créées pour cette note**
- Thoughtworks, *Technology Radar* volume 35, nov. 2026 (IA appliquée au produit ; tendance émergente)
- Nicolas Ploquin, *Lean, AI et Delivery Tech*, OCTO Talks !, 16 nov. 2026 (IA appliquée au produit ; signal faible)
- Lucy Pitticas-Rothwell, *Using the Four Levels of AI autonomy*, Mind the Product, 17 nov. 2026 (IA appliquée au produit ; signal faible)
- Lenny Rachitsky, *State of the tech job market: late 2026*, 10 nov. 2026 (Product management ; tendance émergente)
- Gergely Orosz avec Satya Nadella, *Software engineering after code becomes cheap*, 16 nov. 2026 (Transformation des entreprises ; tendance émergente)
- Observatoire de France Travail, *L'IA dans les entreprises et les métiers*, n° 90, nov. 2026 (Transformation des entreprises ; tendance émergente)
- John Cutler, *TBM 452: Contexting vs. Context*, 18 nov. 2026 (Transformation des entreprises ; signal faible)
- Reynald Fléchaux, *Les coûts d'infrastructure IA font déraper les budgets des DSI français*, IT for Business (étude Cebr pour Wasabi), 18 nov. 2026 (Investissement tech ; tendance émergente)
- Gené Teare, *The Key Numbers I'm Watching As Anthropic Makes Its IPO Debut*, Crunchbase News, 18 nov. 2026 (Investissement tech ; tendance émergente)
- Maxence Fabrion, *La France a vu naître plus de 6 500 nouveaux entrepreneurs de la tech en 2026* (Atomico), Maddyness, 18 nov. 2026 (Investissement tech ; pratique établie)

**Réutilisées**
- Marty Cagan, *AI and the Future of the Product Role*, 6 nov. 2026 (Product management ; tendance émergente)
- Marty Cagan, *The AI Productivity Paradox*, 23 juil. 2026 (Transformation des entreprises ; tendance émergente)
- Menlo Ventures, *2026: The State of Enterprise AI*, 3 nov. 2026 (Investissement tech ; tendance émergente)
- Gené Teare, *Crunchbase Data: Q3 2026*, 5 oct. 2026 (Investissement tech ; pratique établie)

## Sources complémentaires
- [Anthropic Prices IPO Shares At $83, Above Range](https://news.crunchbase.com/public/ipo/anthropic-prices-ipo-ant-above-range/), Crunchbase News, 18 nov. 2026, Investissement tech : le prix final et le montant levé (plus de 92 Md$ avec le placement privé).
- [Sector Snapshot: Investors Turn Up The Volume On Voice AI](https://news.crunchbase.com/venture/voice-ai-startup-funding-peaks-2026/), Crunchbase News, 18 nov. 2026, Investissement tech : 9,5 Md$ pour la voice AI en 2026, concentrés sur moins de startups, surtout en service client.
- [Software factories and code reviews with Harjot Gill](https://newsletter.pragmaticengineer.com/p/software-factories-and-code-reviews), The Pragmatic Engineer, 18 nov. 2026, IA appliquée au produit : le cas extrême d'une usine logicielle (5 000 PR par mois, 250 000 $ de tokens par mois), chiffres auto-déclarés.
- [Copilot at Microsoft Ignite](https://www.microsoft.com/en-us/copilot/blog/2026/11/17/copilot-at-microsoft-ignite-expanding-whats-possible-with-intelligence-built-for-work/), Microsoft, 17 nov. 2026, IA appliquée au produit : des agents autonomes avec identité, responsable désigné et plafonds de dépense.
- [Orange Ventures se dote de 250 millions d'euros supplémentaires](https://www.maddyness.com/2026/11/17/orange-ventures-se-dote-de-250-millions-deuros-supplementaires-pour-investir-dans-la-tech-europeenne/), Maddyness, 17 nov. 2026, Investissement tech : le capital-risque d'entreprise au service de la feuille de route produit (IA appliquée, cybersécurité).
- [Ch. 11: Measuring Impact](https://www.producttalk.org/ch-11-measuring-impact/), Product Talk, 16 nov. 2026, Product management : instrumenter peu, mais mesurer l'impact sur le résultat.
- [VC Firm Plural Closes On $1.1B](https://news.crunchbase.com/venture/plural-closes-billion-euro-fund-european-ai-robotics-defense-startup-investment/), Crunchbase News, 15 nov. 2026, Investissement tech : un fonds européen d'amorçage tourné vers l'énergie, le calcul, la défense et la robotique.
- [Nvidia's Startup Funding Deals Hit A Record. What's Next After Huang?](https://news.crunchbase.com/venture/huang-nvda-ai-startup-funding-record-2026/), Crunchbase News, 13 nov. 2026, Investissement tech : 121 tours en 2026, et une incertitude sur la suite après le départ de Jensen Huang.
- [The Week's 10 Biggest Funding Rounds](https://news.crunchbase.com/venture/biggest-startup-funding-rounds-agentic-ai-infrastructure-mirendil-mercor/), Crunchbase News, 13 nov. 2026, Investissement tech : l'IA agentique et l'infrastructure dominent (Mirendil, Mercor, LangChain).
- [Fable 5.2 and Jagged AGI](https://www.oneusefulthing.org/p/fable-52-and-jagged-agi), One Useful Thing, 9 nov. 2026, IA appliquée au produit : des agents puissants mais incapables de juger leur propre travail, qui dérivent vers la bureaucratie.
