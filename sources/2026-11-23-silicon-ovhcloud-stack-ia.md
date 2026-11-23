# OVHcloud promeut sa « stack IA » : derrière le narratif, un travail d'unification

**Référence** : Clément Bohic, Silicon.fr, 20 novembre 2026, article d'analyse, https://www.silicon.fr/cloud-1370/ovhcloud-ia-230544

**Axe** : Investissement tech (IA appliquée au produit)

## 1. L'idée clé
OVHcloud se présente comme un fournisseur de « stack IA » complète : modèles, GPU, inférence, RAG, agents et suite de productivité. Derrière ce récit, il y a surtout un travail d'unification d'acquisitions, celles d'OVHcloud (Dragon LLM, Gladia) et celles d'Octave Klaba à titre personnel (Shadow, Qwant), pour proposer des équivalents européens de Modal, d'OpenRouter et de ChatGPT Work.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [JDN, comparatif des inférenceurs souverains](2026-11-20-jdn-comparatif-inferenceurs-souverains.md) (OVH le moins cher sur l'inférence) et la fiche [Atomico via Maddyness](2026-11-19-maddyness-atomico-state-european-tech-2026.md) (souveraineté et infrastructure IA en Europe).
- **Au-delà de l'inférence, une pile complète** : le JDN comparait des prix par million de tokens. Silicon montre qu'OVH empile ses propres modèles (Olala), des GPU serverless (AI Fabric via Shadow/Blade), un RAG managé (AI Search, alpha en janvier 2027), une plateforme d'agents (AI Agents, alpha en décembre) et une suite de productivité (OVHai Workspace).
- **Une stratégie qui passe par le patrimoine Klaba** : Qwant (index commun avec Ecosia, API pour agents) et Shadow (environ 12 000 GPU sous-utilisés relancés comme néocloud Blade) sont rattachés à l'offre OVHcloud alors qu'ils appartiennent à son fondateur à titre personnel. C'est un montage de groupe, pas seulement des produits.
- **Le pari du petit modèle sur CPU** : Olala mini (7 milliards de paramètres, MoE hybride avec Mamba, quantifié à 5 bits) vise l'exécution sur CPU, indispensable à l'inférence locale et au chiffrement de bout en bout prévus en 2027. L'ambition de plus de 100 milliards de paramètres en 2027 reste un objectif.
- **Le cloud devient un éditeur de suite agentique** : avec OVHai Workspace (mail, visio, vibe-coding de sites, moteur de connaissance) hébergé en SecNumCloud, OVH vise des utilisateurs qui ne sont plus seulement des développeurs.

## 3. Résumé
L'article part d'un constat : OVHcloud expérimente des produits proches de Modal, d'OpenRouter et de ChatGPT Work, en s'appuyant sur des acquisitions. Premier bloc : Dragon LLM, racheté en mars 2026 et devenu OVHai LLM, a produit les modèles open-weight Olala, entraînés sur des supercalculateurs européens (Jean Zay, JUPITER, MeluXina). La prochaine version passe de 32k à 128k de contexte, et OVH vise plus de 100 milliards de paramètres en 2027 pour le DevOps et la cyber. Deuxième bloc : Qwant utilise Olala pour ses « réponses flash », hébergées chez Shadow, deux sociétés rachetées par Octave Klaba à titre personnel. L'API de recherche de Qwant pour le RAG et les agents est intégrée à AI Agents, la plateforme agentique d'OVH, avec des sandboxes WebAssembly qui démarrent en 2 ms. Troisième bloc : Shadow relance Blade comme néocloud, avec des modèles en service et des GPU serverless facturés à la minute (AI Fabric, RTX A4500 et RTX 2000 Ada, en France), qui doivent rejoindre le portfolio OVH. Côté OVH, des GPU NVIDIA B300 arrivent (instances à 85,60 € HT/heure, en rupture de stock), et Rubin est prévu en 2027. Quatrième bloc : Gladia, start-up d'IA vocale rachetée, traite une partie du support téléphonique d'OVH depuis septembre, et AI Search (RAG managé hybride) arrive en alpha en janvier 2027. Enfin, la productivité agentique : le Manager devient Console, « agentic-ready ». Les sites sont refondus, OVHcloud.com pour les développeurs et les agents, OVH.com pour les entreprises. OVHai Workspace (en alpha sur liste d'attente) réunit productivité, Web AI et Knowledge Platform, sur bare metal SecNumCloud, avec ouverture aux applications tierces et chiffrement de bout en bout en 2027.

## 4. Citations et noms
**Citations** :
- OVHcloud « vise plus de 100 milliards de paramètres » à l'horizon 2027 (Silicon.fr, reprenant l'annonce d'OVHcloud).

**Noms cités** :
- *Octave Klaba* : fondateur d'OVHcloud, propriétaire à titre personnel de Shadow (via Jezby Ventures) et de Qwant (via Synfonium, avec la Caisse des dépôts).
- *Dragon LLM / OVHai LLM, Olala* : éditeur de modèles racheté en mars 2026 et sa famille de modèles open-weight.
- *Qwant, Ecosia (EUSP)* : moteur de recherche et coentreprise d'index européen, fournisseurs de l'API de recherche pour agents.
- *Shadow, Blade, AI Fabric* : cloud gaming relancé comme néocloud GPU ; Yohann Prigent, son CTO, cite le fine-tuning LoRA comme usage.
- *Gladia, Gladia Vox* : start-up d'IA vocale fondée par Jean-Louis Quéguiner, rachetée par OVHcloud ; agent vocal du support OVH.
- *Yaniv Fdida* : directeur produit et technologie d'OVHcloud.
- *Romain Deveaud* : présente AI Search (réécriture de questions, réordonnancement, recherche multivecteurs).
- *Modal, OpenRouter, ChatGPT Work* : produits américains qui servent de points de repère.
- *NVIDIA B300, Rubin NVL8* : générations de GPU déployées en 2026 et prévues en 2027.

## 5. Mots-clés
souveraineté, infrastructure IA, agents IA, modèles ouverts, dépendance fournisseur

## Lecture CPO
- **Implications** :
  - Pour un DSI qui cherche une alternative européenne, OVH devient un candidat sur toute la pile, mais la plupart des briques sont en alpha (AI Agents, AI Search, Workspace). Il faut des pilotes, pas des engagements de production.
  - Les liens capitalistiques entre OVH, Shadow et Qwant sont à prendre en compte dans l'analyse de dépendance fournisseur : la pile « souveraine » repose sur un seul actionnaire.
  - Le petit modèle sur CPU ouvre des cas d'usage d'inférence locale et chiffrée pour les produits qui manipulent des données sensibles, à suivre en 2027.
- **Fiabilité** : journaliste spécialisé, ton critique (« derrière le narratif »). Les informations viennent surtout d'OVHcloud et de ses dirigeants ; pas de mesure indépendante de la qualité des modèles ni des performances. Les dates de disponibilité sont annoncées par l'éditeur.
- **Maturité** : Signal faible : l'offre est large mais largement en alpha ou annoncée, et son intégration reste à faire.
- **Réutilisation** : présentation client DSI sur la souveraineté IA (carte des briques européennes face aux équivalents américains, avec leur niveau de maturité) ; table ronde souveraineté ; à combiner avec le comparatif de prix du JDN.
