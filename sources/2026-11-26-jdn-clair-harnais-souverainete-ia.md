# Le harnais, l'angle mort de la souveraineté de l'IA

**Référence** : Jean-Philippe Clair, Journal du Net, 25 novembre 2026, tribune, https://www.journaldunet.com/intelligence-artificielle/1559105-le-harnais-l-angle-mort-de-la-souverainete-de-l-ia/

**Axe** : Portefeuille numérique (IA appliquée au produit)

## 1. L'idée clé
La souveraineté de l'IA ne se joue pas seulement sur le choix du modèle : la dépendance se loge surtout dans le harnais, c'est-à-dire tout ce qui entoure le modèle et détermine le comportement réel des agents. Si l'on ne peut pas changer de modèle en un mois sans réécrire ses agents, on accumule une « dette de souveraineté », et toute organisation qui déploie des agents devra les migrer d'ici trois ans.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [ITSocial sur l'orchestration agentique](2026-11-20-itsocial-orchestration-agentique-dsi.md) (dépendance choisie couche par couche), la fiche [Databricks sur la fidélité aux modèles](2026-11-20-bdm-databricks-fidelite-modeles-ia.md) (on change de modèle en quelques semaines), la fiche [Reuters sur le cloud souverain](2026-11-24-lmi-reuters-cloud-souverain-europe.md) et le discours dominant, qui réduit la souveraineté de l'IA à l'hébergement et au modèle.
- **Le harnais, désigné comme lieu principal du verrouillage** : quand un même fournisseur tient le savoir, le harnais et le modèle, changer de modèle devient très coûteux. Les fiches précédentes parlaient de réversibilité du modèle ou du cloud, pas de celle de la couche agentique.
- **Un test simple : migrer de modèle en un mois sans réécrire les agents**. C'est un critère opérationnel, utilisable en revue de portefeuille.
- **Une architecture en quatre couches** (données et connaissances possédées, modèles remplaçables, harnais, « bon sens » du plus petit outil suffisant), adossée à l'AFNOR Spec 2314 sur l'IA frugale.
- **Les standards ne suffisent pas** : MCP, AGENTS.md et Agent Skills sont salués mais nés aux États-Unis, et un protocole gère la « plomberie », jamais la responsabilité. Contrepoint à la fiche ITSocial, qui voyait dans ces normes ouvertes une sortie de la dépendance.
- **Trois raisons de migrer d'ici trois ans** : coût (+340 % de dépenses d'IA observé par Spendesk), obsolescence rapide des modèles, sécurisation par la multiplicité des modèles.

## 3. Résumé
La tribune s'ouvre sur une question : peut-on changer de modèle d'IA en un mois sans réécrire ses agents ? Si non, une dette de souveraineté se constitue. L'auteur rappelle d'abord l'héritage de dépendance : le Cigref chiffrait en avril 2025 à 264 milliards d'euros par an les achats cloud et logiciels européens profitant à l'économie américaine ; une étude Asterès prolonge le constat (inflation de 8,7 % par an sur trois ans, surcoût moyen de 140 milliards d'euros par an sur 2026-2030 ; sur 54 décideurs IT, 40 % citent le verrouillage et près d'un sur deux ne sait pas mesurer les bénéfices de l'IA). La dette bureautique est jugée difficile à rembourser à court terme ; sur le collaboratif, la généralisation de Visio (DINUM) aux services de l'État d'ici 2027 montre la voie des standards ouverts. Il propose ensuite une architecture en quatre couches : données et connaissances qui doivent appartenir à l'organisation, modèles à rendre remplaçables, harnais qui fixe le comportement des agents, « bon sens » du plus petit outil suffisant (AFNOR Spec 2314). Le harnais est le point de bascule : un fournisseur qui verrouille savoir, harnais et modèle rend la migration très coûteuse. Les standards (MCP, AGENTS.md, rejoints par l'Agentic AI Foundation en décembre 2025, Agent Skills en octobre 2026) aident mais restent américains et ne portent pas la responsabilité. La liberté de changer suppose de connaître ses dépendances et de disposer de formats, protocoles et contrats réversibles, testés régulièrement. Deux exemples d'exposition : le procureur de la CPI qui aurait perdu l'accès à sa messagerie Microsoft en 2025 (selon l'AP, Microsoft conteste), et la panne mondiale de Microsoft 365 de novembre 2026 dans 74 pays. Conclusion : toute organisation devra migrer ses agents d'ici trois ans, pour le coût (Spendesk : +340 % des dépenses d'IA chez 2 568 entreprises européennes entre juin 2025 et juin 2026), l'obsolescence des modèles et la sécurité par la multiplicité ; le prix de cette migration se décide maintenant.

## 4. Citations et noms
**Citations** :
- « Le prix de la migration de vos agents se décide aujourd'hui. », Jean-Philippe Clair

**Noms cités** :
- *Cigref* : source du chiffre de 264 milliards d'euros par an d'achats cloud et logiciels profitant à l'économie américaine (avril 2025).
- *Asterès* : cabinet dont l'étude chiffre l'inflation (8,7 % par an) et le surcoût à venir (140 milliards d'euros par an).
- *DINUM, Visio* : exemple de reprise en main du collaboratif dans l'État d'ici 2027.
- *AFNOR Spec 2314* : référentiel sur l'IA frugale (juin 2024), base de la couche « bon sens ».
- *MCP, AGENTS.md, Agent Skills, Agentic AI Foundation (Linux Foundation)* : standards agentiques utiles mais d'origine américaine.
- *CPI, Microsoft 365* : exemples d'exposition à la dépendance (coupure de messagerie, panne mondiale).
- *Spendesk* : source du chiffre de +340 % de dépenses d'IA en un an.

## 5. Mots-clés
souveraineté, harnais agentique, dépendance fournisseur, réversibilité, agents IA

## Lecture CPO
- **Implications** :
  - Ajouter au portefeuille un test de réversibilité par agent : combien de temps et de réécriture pour changer de modèle ? Le refaire régulièrement.
  - Garder la main sur le harnais (prompts, outils, evals, mémoire) et sur les connaissances, même quand le modèle est acheté.
  - Budgéter dès maintenant une migration des agents à horizon trois ans plutôt que de la découvrir sous contrainte.
  - Ne pas confondre adoption de standards (MCP, AGENTS.md) et maîtrise : la responsabilité reste à l'organisation.
- **Fiabilité** : tribune d'opinion argumentée, fonction de l'auteur non précisée dans l'article ; chiffres sourcés (Cigref, Asterès, Spendesk, AP) mais tirés d'études externes, sans méthodologie détaillée ; l'échantillon Asterès (54 décideurs) est mince.
- **Maturité** : Tendance émergente : la réversibilité des modèles est discutée, celle du harnais commence à peine à l'être.
- **Réutilisation** : article OCTO sur la souveraineté des agents (le harnais comme actif à posséder) ; présentation client sur le test « migrer en un mois » ; post LinkedIn sur la « dette de souveraineté », en croisant avec Thoughtworks et Databricks.
