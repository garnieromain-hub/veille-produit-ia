# An insider's look at SAP's 'Autonomous Enterprise'

**Référence** : Manfred Bremmer, CIO.com (entretien mené pour Computerwoche avec Jonathan von Rüden, Chief AI Officer de SAP), 20 novembre 2026, entretien, https://www.cio.com/article/4249833/sap-caio-we-need-to-be-more-precise-in-managing-the-use-of-ai.html

**Axe** : Transformation des entreprises (Investissement tech)

## 1. L'idée clé
Pour passer à l'« entreprise autonome », il faut piloter l'IA comme un investissement : estimer la consommation, fixer des budgets par salarié, service ou pays, choisir un modèle par défaut raisonnable, et faire passer chaque agent par un cycle de vie avec validation. SAP reconnaît que le lien entre dépense IA et valeur métier reste à construire.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Uber sur son budget IA](2026-11-20-uber-budget-ia-reglages-agents-code.md) (réglages par défaut pour maîtriser les coûts), la fiche [Databricks sur la fidélité aux modèles](2026-11-20-bdm-databricks-fidelite-modeles-ia.md) (routage et coût par tâche), la fiche [IT Social sur l'orchestration agentique](2026-11-20-itsocial-orchestration-agentique-dsi.md) (SAP intègre le contrôle des agents à son offre) et la fiche [Thelliez sur le responsable du ROI IA](2026-11-20-jdn-thelliez-responsable-roi-ia.md).
- **Le FinOps IA vu par un éditeur de progiciel** : estimation de la consommation à partir des effectifs, de la fréquence des processus et du volume de documents, budgets et plafonds journaliers par salarié, service ou pays, avec demande d'allocation supplémentaire. Uber montrait la même logique côté client ; SAP l'intègre au produit.
- **Un ordre de grandeur sur le nombre d'agents** : pour une entreprise d'environ cent applications SaaS, 10 à 30 agents réutilisables au départ, appelés à se consolider. C'est un repère rare face aux promesses de « milliers d'agents ».
- **La gouvernance des agents comme un cycle de vie applicatif** : partage, versions, revue, retrait par workflow de validation, y compris l'accord du comité d'entreprise, suivi dans un AI Agent Hub ; Joule Studio ouvert à quelques milliers de salariés hors IT après formation.
- **Un aveu de l'éditeur** : relier la dépense IA à la valeur métier, réallouer les budgets dynamiquement et rattacher les budgets au compte de résultat restent à faire, et aucun standard de gouvernance des agents n'existe encore.

## 3. Résumé
L'entretien part de la présentation, à la conférence TechEd de Berlin, du concept d'« Autonomous Enterprise » : des agents qui agissent dans les systèmes SAP, via Joule Work et SAP Autonomous Suite, sur la SAP Business AI Platform. Les premières questions portent sur les coûts : SAP estime la consommation à partir des effectifs, de la fréquence des processus, du volume de documents et de clients comparables ; les budgets et plafonds se fixent par salarié, service ou pays, ce qui, selon von Rüden, incite aussi les gens à s'emparer du sujet. Pour éviter que chacun prenne le modèle le plus cher, un modèle par défaut raisonnable réduit « considérablement » les coûts (sans chiffre) ; le routage automatique est testé en interne et prévu pour des premiers clients. Joule Work propose trois modes et 70 LLM, avec la possibilité de privilégier des modèles européens. Les modèles locaux tournent dans l'application de bureau, mais leur déploiement à grande échelle chez les clients reste difficile. L'entretien passe ensuite à la gouvernance : accès à Joule Studio attribué par l'IT, ouvert à quelques milliers de salariés non informaticiens formés ; agents partagés, versionnés, revus et retirés par workflow, avec accord du comité d'entreprise ; suivi dans le SAP AI Agent Hub ; tests générés automatiquement à partir des spécifications et analyse des processus (agent mining). Vient le retournement : von Rüden reconnaît que le lien entre dépense et valeur, la réallocation dynamique des budgets et leur rattachement au compte de résultat restent à travailler, car un directeur financier demande ce qu'a rapporté la dépense. Il cite les outils de gouvernance (SAP Agent Gateway gratuit, SAP Enterprise AI Gateway, fonctions premium), estime à 10 à 30 le nombre d'agents réutilisables pour une entreprise d'une centaine d'applications SaaS, défend l'automatisation classique (dont n8n) et les workflows hybrides où l'IA n'intervient que là où elle sert. Il conclut sur les prochaines étapes : modèles qui apprennent directement l'usage des outils, apprentissage à partir du retour d'expérience, modèles spécialisés en cybersécurité, approches non autorégressives de Yann LeCun.

## 4. Citations et noms
**Citations** :
- « Nous devons devenir encore plus précis dans le pilotage de cet investissement. » (« Nevertheless, we need to become even more precise in managing this investment. »), Jonathan von Rüden
- « Un directeur financier demande à juste titre : nous avons dépensé tant, qu'est-ce que cela nous a rapporté ? » (« Because a CFO rightly asks: We've spent this amount; what did it bring us? »), Jonathan von Rüden
- « Les budgets incitent aussi à s'emparer du sujet. » (« Budgets also create an incentive to engage with the issue. »), Jonathan von Rüden

**Noms cités** :
- *Jonathan von Rüden* : Chief AI Officer de SAP, interviewé.
- *Manfred Bremmer, Computerwoche* : auteur et média d'origine de l'entretien.
- *SAP Autonomous Enterprise, Joule Work, SAP Autonomous Suite, SAP Business AI Platform* : le concept et les offres présentés à TechEd Berlin.
- *Joule Studio, SAP AI Agent Hub* : outil de création d'agents et registre de suivi de leur statut.
- *SAP Agent Gateway, SAP Enterprise AI Gateway* : outils de gouvernance des agents (gratuit, puis application des règles à l'exécution).
- *n8n* : outil d'automatisation classique pris en charge par SAP.
- *Yann LeCun* : ses approches non autorégressives sont citées comme piste d'avenir.

## 5. Mots-clés
FinOps, gouvernance IA, agents IA, routage de modèles, mesure du ROI, budgets IT

## Lecture CPO
- **Implications** :
  - Pour une DSI : définir des budgets IA par salarié, service ou pays et un modèle par défaut avant de généraliser les agents, plutôt que de découvrir la facture après coup (cf. Uber).
  - Traiter les agents comme des applications du portefeuille : registre, versions, validation, retrait, et, en France, associer tôt les instances représentatives (SAP intègre l'accord du comité d'entreprise au workflow).
  - Viser quelques dizaines d'agents réutilisables plutôt qu'une prolifération, et garder l'automatisation classique là où elle suffit.
  - Le lien dépense IA et compte de résultat n'est pas fourni par l'éditeur : c'est au CPO et au contrôle de gestion de construire la mesure de valeur.
- **Fiabilité** : le responsable IA d'un éditeur parle de ses propres produits, donc discours commercial ; mais il reconnaît des manques explicites. Peu de chiffres (70 LLM, 10 à 30 agents, quelques milliers d'utilisateurs de Joule Studio), aucun sur les économies réalisées.
- **Maturité** : Tendance émergente : les mécanismes (budgets, routage, registre d'agents) sont annoncés ou en test, l'éditeur admet qu'aucun standard n'existe encore.
- **Réutilisation** : présentation client DSI sur le FinOps IA et la gouvernance des agents (budgets par entité, modèle par défaut, cycle de vie) ; post LinkedIn (« 10 à 30 agents, pas des milliers ») ; table ronde sur le ROI de l'IA avec la fiche Thelliez.
