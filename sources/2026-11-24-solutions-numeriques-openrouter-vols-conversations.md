# OpenRouter écarte trois fournisseurs après des vols de conversations d'IA

**Référence** : Camille Suard, Solutions Numériques, 23 novembre 2026, article d'actualité (d'après une enquête de Dragos publiée le 19 novembre et les annonces d'OpenRouter, Phala et Together AI), https://www.solutions-numeriques.com/openrouter-ecarte-trois-fournisseurs-apres-des-vols-de-conversations-dia/

**Axe** : IA appliquée au produit (Investissement tech)

## 1. L'idée clé
Quand une application passe par un routeur de modèles, ses requêtes peuvent traverser plusieurs routeurs, hébergeurs et revendeurs dont le client ignore l'identité. L'enquête de Dragos montre que certains de ces intermédiaires ont lu, réutilisé ou transmis des conversations, y compris sous garantie de non-conservation, souvent sans piratage : la confidentialité dépend de toute la chaîne d'inférence.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [JDN, comparatif des inférenceurs souverains](2026-11-20-jdn-comparatif-inferenceurs-souverains.md) (le zéro rétention présenté comme une garantie de fournisseur) et la fiche [Claire Vo via Willison](2026-11-20-willison-claire-vo-fraude-tokens.md) (OpenRouter vu comme une place de marché de modèles) ; plus largement, le discours dominant selon lequel le risque de confidentialité de l'IA se règle en choisissant un fournisseur de modèle de confiance.
- **Une preuve par leurres** : Dragos a fait circuler près de deux millions de requêtes contenant des identifiants et liens uniques depuis juillet ; des clés AWS leurres ont été réutilisées dès le lendemain pour explorer S3, Secrets Manager et Parameter Store et tenter d'activer Bedrock.
- **Le zéro rétention ne protège pas tout** : deux compromissions concernaient des conversations sous ZDR, et des clés ont été récupérées dans des requêtes rejetées avant même l'exécution du modèle. OpenRouter retire la garantie ZDR sur 125 points d'accès.
- **Le risque vient de l'architecture, pas seulement d'attaques** : revendeurs qui lisent les requêtes en activant la journalisation, modèle à bas prix utilisé comme appât, routeur qui redirige du trafic à l'insu des clients, requêtes adressées à des hébergeurs américains transmises à un laboratoire chinois, lien ouvert 24 jours plus tard depuis Pékin et Shanghai.
- **Deux incidents reconnus** : Phala (requêtes vers un déploiement DeepSeek exposées du 21 octobre au 8 novembre, serveur GPU mis en production sans protections) et Together AI (identifiant publié par erreur sur GitHub par un agent de programmation, donnant accès à des échantillons de conversations).

## 3. Résumé
L'article ouvre sur un fait : le 21 octobre, des identifiants AWS glissés dans des requêtes à un fournisseur d'IA ont été interceptés, puis utilisés le lendemain pour des dizaines de milliers d'appels aux API d'AWS. C'étaient des leurres de Dragos, qui surveillait depuis juillet la circulation d'environ deux millions de requêtes piégées. L'enquête, publiée le 19 novembre, révèle des compromissions chez trois hébergeurs : plusieurs centaines de clés récupérées fin octobre dans le cas le plus grave, et deux cas touchant des conversations sous ZDR. L'article détaille ensuite des accès « sans piratage » : revendeurs de calcul lisant les requêtes via la journalisation, intermédiaire testant des liens confidentiels depuis une connexion domestique, tentatives SSH avec des mots de passe extraits des requêtes, routeur détournant du trafic, transmission à un laboratoire chinois, lien ouvert sur Feishu 24 jours après. Il en tire la tension centrale : ces fuites découlent de l'organisation même des services, faits de chaînes d'intermédiaires opaques. Le 22 novembre, OpenRouter écarte trois fournisseurs, retire la ZDR sur 125 points d'accès, prévient les clients et affirme ne pas avoir été compromis ; il renvoie aux incidents reconnus par Phala et Together AI sans confirmer qu'il s'agit d'eux. OpenRouter prévoit de reproduire régulièrement les tests de Dragos et de vérifier les circuits des requêtes avant de rétablir certaines garanties.

## 4. Citations et noms
**Citations** : rien de notable (l'article ne contient pas de citation directe).

**Noms cités** :
- *Dragos* : société de cybersécurité, auteur de l'enquête par requêtes leurres.
- *OpenRouter* : plateforme d'accès unifié à plusieurs modèles, qui écarte trois fournisseurs et retire la ZDR sur 125 points d'accès.
- *Phala* : hébergeur dont un déploiement DeepSeek a été exposé du 21 octobre au 8 novembre.
- *Together AI* : hébergeur dont un agent de programmation a publié un identifiant sur GitHub.
- *DeepSeek* : modèle servi par le déploiement compromis de Phala.
- *AWS (S3, Secrets Manager, Parameter Store, Bedrock)* : services visés avec les clés leurres.
- *Feishu* : messagerie sur laquelle un lien piégé a été ouvert depuis Pékin et Shanghai.
- *Zero Data Retention (ZDR)* : garantie de non-conservation des requêtes, mise en défaut.

## 5. Mots-clés
sécurité, confidentialité des données, infrastructure IA, dépendance fournisseur, chaîne d'approvisionnement logicielle

## Lecture CPO
- **Implications** :
  - Pour tout produit IA qui passe par un routeur ou une place de marché de modèles, exiger de connaître l'hébergeur final de chaque requête et pouvoir le fixer, plutôt que de laisser le routage chercher le prix le plus bas.
  - Ne jamais faire transiter de secrets (clés, mots de passe, liens signés) dans les prompts : filtrer en amont, côté produit.
  - Traiter la ZDR comme une déclaration à vérifier, pas comme une garantie : l'intégrer aux audits fournisseurs et aux contrats.
  - Dans l'arbitrage coût de l'inférence, intégrer le risque : le modèle le moins cher d'une place de marché peut être un appât.
- **Fiabilité** : article d'actualité qui relaie une enquête de Dragos (société de sécurité, qui a intérêt à montrer des menaces mais publie une méthode vérifiable par leurres) et les communications d'OpenRouter, Phala et Together AI. Les trois fournisseurs écartés ne sont pas nommés. L'enquête d'origine n'a pas été lue pour cette fiche.
- **Maturité** : Signal faible : premier cas documenté à cette échelle, mais qui touche une pratique répandue (routeurs et revendeurs d'inférence).
- **Réutilisation** : présentation client DSI ou RSSI sur la chaîne d'inférence comme chaîne d'approvisionnement ; post LinkedIn « Le zéro rétention, une promesse à vérifier » ; article OCTO sur le choix d'un inférenceur, à croiser avec le comparatif JDN (prix contre garanties).
