# Avec l'IA, les entreprises vont-elles recommencer à développer leurs logiciels ?

**Référence** : Mehdi Medjaoui (cofondateur et CEO de Bunny, fondateur d'APIdays, coanimateur du podcast « À la French »), IT for Business (rubrique @Work, page attribuée à Laurent Delattre), 24 novembre 2026, tribune, https://www.itforbusiness.fr/acheter-ou-developper-logiciel-ia-110299

**Axe** : Portefeuille numérique (Investissement tech)

## 1. L'idée clé
Le réflexe « acheter plutôt que développer », installé depuis trente ans, est rouvert par l'IA : pas pour tous les logiciels ni du jour au lendemain, mais assez pour que le DSI reclasse son portefeuille applicatif et retrouve une « option de sortie » face aux éditeurs. Le vrai enjeu n'est pas de remplacer le SaaS par un modèle de langage mais de reprendre la main sur ses données.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Colisto sur le build versus buy](2026-11-23-cio-colisto-build-versus-buy-ia.md) (l'IA réduit le coût de création, pas celui de possession ; cinq questions d'arbitrage), la fiche [Eriksson sur la renaissance du logiciel](2026-11-24-mtp-eriksson-software-renaissance.md) (la SaaSpocalypse est exagérée) et la fiche [Crunchbase sur la SaaSpocalypse](2026-11-20-crunchbase-anton-saaspocalypse-marches.md).
- **Une relecture du cas Klarna** : selon l'auteur, Klarna n'a pas remplacé Salesforce et Workday par un LLM, elle a rapatrié ses données dans sa propre pile (Neo4j, Cursor). Le discours dominant en faisait un symbole de la fin du SaaS ; ici, c'est un cas de reprise des données, peu transposable (fintech dotée de grosses équipes d'ingénierie, et le PDG doute lui-même que d'autres suivent).
- **Une classification du portefeuille en trois familles** : standard (l'achat reste pertinent), différenciant (le développement interne retrouve du sens), critique (maîtrise et réversibilité priment). Plus simple que les cinq questions de Colisto, et directement utilisable en revue de portefeuille.
- **Le développement interne comme levier de négociation** : savoir construire renforce le rapport de force face aux éditeurs, même si l'on continue d'acheter. Colisto évoquait la renégociation ; Medjaoui en fait la principale valeur de la capacité interne.
- **Le chiffre Cigref** : hausse moyenne de 8,7 % par an des prix du cloud et du logiciel (mai 2026), comme coût caché du « tout acheter ».
- Pour le reste (METR, coût de la maintenance, menace sur les outils périphériques), redite de la fiche Colisto.

## 3. Résumé
L'auteur part d'un constat : acheter plutôt que développer est devenu un réflexe, car le modèle éditeur mutualise les coûts entre clients. Mais ce « tout acheter » a un coût caché : chaque fonction a son catalogue d'applications, les données se diluent, les contrats se multiplient, et le Cigref chiffre à 8,7 % par an la hausse moyenne des prix du cloud et du logiciel (mai 2026). L'IA change la donne en rendant prototypes et composants plus rapides à produire, sans automatiser uniformément la production logicielle. Il revient sur Klarna : en septembre 2024, Sebastian Siemiatkowski annonce l'abandon de Salesforce et de Workday ; l'auteur y voit surtout un rapatriement des données dans une pile maison (Neo4j, Cursor), et rappelle que le PDG lui-même doute que la plupart des entreprises suivent. Vient le « piège du code gratuit » : écrire le code n'est pas l'essentiel du coût, face à la conception, la sécurité, la maintenance et la documentation ; l'étude METR de juillet 2025 mesurait des développeurs expérimentés 19 % plus lents avec l'IA, même si METR a depuis signalé des observations plus favorables. Le SaaS devra justifier sa valeur : les outils périphériques et les fonctions simples facturées cher sont les plus exposés, les solutions fondées sur un savoir métier, un écosystème, des données ou des certifications restent avantagées. D'où l'« option de sortie » : classer le portefeuille en trois familles et privilégier des partenaires ouverts, notamment open source. Conclusion prudente : les éditeurs utilisent aussi l'IA pour baisser leurs coûts, et le bon DSI de demain saura aussi repérer les logiciels dont l'entreprise n'a plus besoin.

## 4. Citations et noms
**Citations** :
- « Pas pour tous les logiciels, ni du jour au lendemain, mais assez pour rouvrir le débat. », Mehdi Medjaoui
- « Klarna n'a donc pas remplacé ses logiciels par un modèle de langage : elle a repris la main sur ses données et cessé de payer des interfaces propriétaires posées dessus. », Mehdi Medjaoui

**Noms cités** :
- *Mehdi Medjaoui* : auteur, CEO de Bunny et fondateur d'APIdays (conférences sur les API).
- *Cigref* : source du chiffre de 8,7 % de hausse annuelle des prix cloud et logiciel (mai 2026).
- *Klarna, Sebastian Siemiatkowski* : cas de l'abandon de Salesforce et Workday (septembre 2024), relu comme une reprise des données.
- *Salesforce, Workday* : logiciels abandonnés par Klarna.
- *Neo4j, Cursor* : base orientée graphe et assistant de code utilisés par Klarna pour sa pile interne.
- *METR* : étude de juillet 2025 (développeurs expérimentés 19 % plus lents avec l'IA), nuancée depuis par METR.
- *Option de sortie* : capacité à développer en interne utilisée comme levier face aux éditeurs.

## 5. Mots-clés
build vs buy, rationalisation applicative, coût total de possession, dépendance fournisseur, réversibilité, achats IT

## Lecture CPO
- **Implications** :
  - Classer le portefeuille applicatif en standard, différenciant et critique avant chaque renouvellement, et ne considérer le développement interne que pour le différenciant.
  - Entretenir une capacité de développement interne aussi pour peser dans les négociations, pas seulement pour remplacer.
  - Traiter la reprise des données comme le vrai sujet : un remplacement de SaaS sans stratégie de données ne fait que déplacer la dépendance.
  - Ajouter le décommissionnement aux revues de portefeuille (« les logiciels dont l'entreprise n'a plus besoin »).
- **Fiabilité** : tribune d'un entrepreneur de l'écosystème API, favorable par position aux architectures ouvertes et à la maîtrise des données ; chiffres sourcés (Cigref, METR) mais externes, aucun retour d'expérience propre. Lecture du cas Klarna argumentée mais non documentée en détail.
- **Maturité** : Tendance émergente : le retour du développement interne est très débattu fin 2026, mais il reste peu de cas hors entreprises tech très outillées.
- **Réutilisation** : article OCTO sur la rationalisation du parc à l'ère de l'IA (les trois familles, en complément des cinq questions de Colisto) ; post LinkedIn sur la relecture du cas Klarna ; présentation client DSI sur l'option de sortie comme levier d'achat.
