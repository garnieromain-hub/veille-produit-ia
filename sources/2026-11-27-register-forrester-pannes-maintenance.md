# Tech's outage problem needs maintenance, not conspiracy theories

**Référence** : Lindsay Clark, The Register, 26 novembre 2026, article (compte rendu d'un rapport Forrester), https://www.theregister.com/research/2026/11/26/techs-outage-problem-needs-maintenance-not-conspiracy-theories/5312180

**Axe** : Portefeuille numérique (Investissement tech)

## 1. L'idée clé
Selon Forrester, la série de pannes de novembre (Microsoft 365, contrôle aérien américain, banques) ne relève ni d'une cyberattaque coordonnée ni de l'IA, mais d'une cause « tragiquement banale » : des décennies de dette technique et de sous-investissement dans les opérations. Les organisations ont financé des façades modernes posées sur un parc vieillissant, fragile et de plus en plus interconnecté ; sans effort de résilience, il s'effondrera « comme un château de cartes ».

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Anderson sur la panne de la FAA](2026-11-24-cio-anderson-faa-dette-technique-ia.md) (fragilité d'un système hérité rapiécé, dette accélérée par l'IA) et la fiche [Stephens sur l'usure des systèmes hérités](2026-11-26-cio-stephens-legacy-usure.md) (ce n'est pas l'âge mais le manque d'entretien qui rend un système fragile).
- **Un diagnostic d'analyste sur une série, pas un cas** : Forrester relie Microsoft, Google Cloud, AWS, la FAA, JPMorgan Chase, United Airlines, Apple, Workday et Gmail en une seule tendance de fond. Anderson partait de la seule FAA.
- **Le biais d'investissement nommé** : la modernisation a privilégié le changement visible au renouvellement structurel. C'est une critique de l'arbitrage de portefeuille lui-même, là où Stephens parlait d'entretien d'un système donné.
- **Le rejet explicite des explications par le complot ou l'IA** : face aux théories sur une cyberattaque ou l'IA, Forrester juge une cause commune « highly unlikely ».
- **Pour le reste, redite** : cartographier les dépendances, tester pannes et reprises en conditions réalistes, exploiter incidents et quasi-incidents ; recommandations connues, déjà présentes chez Anderson.

## 3. Résumé
L'article s'ouvre sur l'avertissement de Forrester : dette technique accumulée, complexité croissante et sous-investissement dans les opérations rendent les organisations vulnérables aux pannes majeures. Il rappelle la semaine de novembre où des pannes ont touché Microsoft 365, le contrôle aérien américain, des banques et d'autres services critiques, et les théories qui ont suivi sur des cyberattaques ou l'IA ; pour Forrester, la vraie cause est « tragiquement banale ». Le cabinet appelle fournisseurs et équipes IT à donner la priorité à la résilience. L'article recense ensuite les pannes récentes : Microsoft début novembre (un processus central submergé sur certains serveurs, certains services non rétablis pendant 24 heures supplémentaires), Google Cloud en octobre (un « événement électrique » en Europe de l'Ouest touchant BigQuery Data Transfer Service, Cloud Filestore, Cloud Run, App Engine et GKE), AWS en octobre 2025 (région US-East, y compris le site d'Amazon), puis l'arrêt national de la FAA le 13 novembre 2026 après une panne de communication, et des incidents chez JPMorgan Chase, United Airlines, Apple, Workday et Gmail. Il cite l'analyse des auteurs du rapport, Lauren Nelson et Mark Moccia : les organisations ont privilégié les améliorations visibles plutôt que les fondations, d'où une façade moderne sur un parc vieillissant. Conclusion : cartographier les dépendances, tester pannes et reprises en conditions réalistes, et se servir des incidents et quasi-incidents pour repérer les faiblesses avant la prochaine panne.

## 4. Citations et noms
**Citations** :
- « Le vrai coupable est tragiquement banal : l'aboutissement de décennies de dette technique » (« The real culprit is tragically mundane: the culmination of decades of technical debt »), Forrester
- « Les investissements de modernisation ont privilégié le changement visible au renouvellement structurel » (« Modernization investments have favored visible change over structural renewal »), Forrester
- « Une façade moderne posée sur un parc vieillissant, fragile et de plus en plus interconnecté » (« a modern front end resting on an aging, brittle, and increasingly interconnected estate »), Forrester

**Noms cités** :
- *Lindsay Clark* : journaliste à The Register, auteur.
- *Forrester* : cabinet d'analyse, auteur du rapport.
- *Lauren Nelson et Mark Moccia* : analystes de Forrester, auteurs du rapport.
- *Microsoft (Microsoft 365)* : panne début novembre 2026, processus central submergé.
- *Google Cloud* : panne d'octobre attribuée à un événement électrique en Europe de l'Ouest.
- *AWS* : panne majeure de la région US-East en octobre 2025.
- *FAA* : arrêt national du trafic aérien américain le 13 novembre 2026.
- *JPMorgan Chase, United Airlines, Apple, Workday, Gmail* : autres services touchés par des incidents en novembre.

## 5. Mots-clés
dette technique, résilience, dépendance fournisseur, plan de continuité, budgets IT

## Lecture CPO
- **Implications** :
  - Dans l'arbitrage de portefeuille, rendre visible la part consacrée au renouvellement structurel (fondations, exploitation) face aux projets de façade ; sans ligne dédiée, elle perd toujours.
  - Cartographier les dépendances entre produits et plateformes (cloud, SaaS, réseau) et tester les reprises en conditions réalistes, pas sur le papier.
  - Exploiter les quasi-incidents comme signal de pilotage de la dette, au même titre que les incidents.
- **Fiabilité** : cabinet d'analyse qui vend du conseil et de la recherche aux DSI, relayé par un média tech ; le rapport n'est pas chiffré dans l'article (aucune mesure de la dette ni du sous-investissement), et les causes des pannes citées viennent des communications des éditeurs. Le diagnostic est plausible mais d'ordre général.
- **Maturité** : Pratique établie : le lien entre dette technique, sous-investissement en exploitation et pannes est bien connu ; l'apport est la lecture d'ensemble d'une série d'incidents récents.
- **Réutilisation** : article OCTO sur la dette technique et la résilience comme ligne de portefeuille, avec Anderson et Stephens ; post LinkedIn « une façade moderne sur des fondations fragiles » ; présentation client DSI sur l'arbitrage entre visible et structurel.
