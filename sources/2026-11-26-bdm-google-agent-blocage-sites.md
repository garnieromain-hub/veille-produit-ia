# Google-Agent : comment éviter de bloquer l'agent IA sur votre site

**Référence** : Matthieu Eugène, Blog du Modérateur, 25 novembre 2026, article pratique (reprise des recommandations de Google), https://www.blogdumoderateur.com/google-agent-comment-eviter-bloquer-agent-ia-site/

**Axe** : IA appliquée au produit

## 1. L'idée clé
Google-Agent, l'agent de Google qui navigue et agit sur les sites pour le compte d'un internaute (recherche, ajout au panier, réservation), est souvent bloqué par les protections anti-bots. Un site qui veut rester utilisable par les agents doit vérifier leur identité et adapter ses règles de CDN et de pare-feu sur tout le parcours.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Signal contre les agents IA d'Apple et de Google](2026-11-25-siecle-digital-signal-agents-ia-ecran.md) (un éditeur qui veut bloquer les agents) ; discours dominant : les sites se protègent des robots IA qui aspirent leurs contenus.
- **Distinguer l'agent qui agit du robot qui indexe** : Google-Agent n'indexe pas, il agit à la demande d'un utilisateur. Le bloquer revient à bloquer un client, pas un scraper.
- **Une procédure de vérification en quatre étapes** : User-Agent, plages d'IP publiées dans user-triggered-agents.json, signature cryptographique (protocole expérimental Web Bot Auth), puis exemption de challenges. C'est le premier mode d'emploi concret de ce type dans la veille.
- **Le parcours entier doit être couvert** : recherche, filtres, fiches, panier, réservation et appels d'API. Un CAPTCHA à une seule étape suffit à faire échouer la tâche.

## 3. Résumé
L'article présente d'abord Google-Agent : un agent qui effectue des actions sur les sites pour un internaute, à la différence de Googlebot qui indexe. Il explique ensuite pourquoi il est bloqué : ses requêtes viennent de serveurs cloud, souvent filtrés par les règles anti-bots ; un CAPTCHA ou un test JavaScript au milieu d'une recherche ou d'un formulaire interrompt la tâche ; les limites de débit par IP se déclenchent parce que de nombreux utilisateurs partagent les mêmes adresses. Vient la vérification recommandée par Google, en quatre contrôles : mention « Google-Agent » dans l'User-Agent (insuffisante seule), IP présente dans le fichier user-triggered-agents.json, signature cryptographique Web Bot Auth quand elle est présente, et exemption de challenges pour les requêtes vérifiées. L'article termine par la liste des réglages CDN et pare-feu : placer la règle d'autorisation avant les blocages plus larges, exempter aussi les CAPTCHA et tests JavaScript, couvrir tout le parcours, adapter les limites de débit, synchroniser les règles IP avec le fichier publié, conserver les en-têtes d'origine à travers proxys et répartiteurs de charge.

## 4. Citations et noms
**Citations** : rien de notable (article descriptif, sans citation).

**Noms cités** :
- *Google-Agent* : agent de Google qui agit sur les sites pour un utilisateur.
- *Googlebot* : robot d'indexation, en contrepoint.
- *Web Bot Auth* : protocole expérimental de signature cryptographique des requêtes d'agents.
- *user-triggered-agents.json* : fichier publié par Google listant les plages d'IP de ses agents.

## 5. Mots-clés
agents IA, conception de produits IA, sécurité, parcours client, commerce agentique

## Lecture CPO
- **Implications** :
  - Pour un site marchand ou de réservation, l'agent devient un nouveau « persona » de parcours : tester les parcours clés avec un agent, pas seulement avec un humain.
  - Mettre d'accord équipes produit et sécurité : une règle anti-bot peut supprimer silencieusement une partie du trafic converti par les agents.
  - Suivre Web Bot Auth : l'authentification des agents est en train de devenir un standard d'infrastructure.
- **Fiabilité** : média spécialisé qui reprend la documentation de Google, sans test ni chiffre ; Google a intérêt à ce que son agent ne soit pas bloqué. Aucune donnée sur le volume de trafic concerné.
- **Maturité** : Signal faible : recommandations techniques récentes, protocole d'authentification encore expérimental, usages des agents marchands à leurs débuts.
- **Réutilisation** : présentation client e-commerce (« votre pare-feu bloque-t-il vos clients agents ? ») ; post LinkedIn sur l'agent comme nouvel utilisateur du parcours.
