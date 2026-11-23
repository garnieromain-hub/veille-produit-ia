# Tony Ghilain (Decathlon) : « Il a toujours été plus simple de casser que de réparer »

**Référence** : Laurent Delattre, IT for Business, 20 novembre 2026, interview filmée sur le plateau d'IT for Business au Tech Show Paris 2026, https://www.itforbusiness.fr/tony-ghilain-decathlon-ia-cybersecurite-offensive-110163

**Axe** : Transformation des entreprises

## 1. L'idée clé
L'IA accélère d'abord les attaquants : rapports de failles générés, preuves de concept écrites en trente minutes, agents qui scannent des cibles. Côté entreprise, le risque vient aussi de l'intérieur, avec des applications vibe-codées hors contrôle ; la réponse de Decathlon combine blocage du shadow AI et programme transverse d'outils validés, car « la confiance n'empêche pas le contrôle ».

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Le Ticket (Adeo, Carrefour, Renault)](2026-11-10-le-ticket-transfo-ia-adeo-carrefour-renault.md) et la fiche [Chazal (OCTO)](2026-10-16-octo-chazal-produit-ia-organisations.md), qui traitent le shadow AI comme un symptôme d'outillage insuffisant, et la fiche [Talbot sur le vibe coding](2026-10-16-talbot-vibe-coding-decisions-cachees.md) (décisions cachées).
- **Le vibe coding vu par la sécurité d'un grand distributeur** : Decathlon a découvert de nombreuses applications générées par les métiers (avec les outils de l'entreprise ou avec Base44, qui produit un site complet, serveur compris, en quelques prompts). Les fiches précédentes parlaient de gouvernance en général ; ici c'est un constat d'incident, détecté à temps.
- **Blocage et accompagnement à la fois** : le shadow AI est bloqué au niveau du réseau, et un programme transverse à tous les métiers fournit outils validés, accompagnement et contrôles techniques. Chazal plaidait surtout pour l'outillage ; Decathlon ajoute le blocage.
- **Le pentest automatisé ne convainc pas** : l'IA remonte des pistes utiles mais rate des points majeurs vérifiés à la main ; un humain reste nécessaire pour les attaques sophistiquées. Contrepoint au discours des éditeurs de sécurité agentique.
- **Rien de chiffré** : en dehors du « POC en 30 minutes au lieu de plusieurs mois », l'entretien ne donne ni volume d'applications découvertes, ni coût, ni résultat du programme.

## 3. Résumé
L'entretien part d'un constat vieux d'environ deux ans : Decathlon a reçu, via son bug bounty, des rapports très soignés mais souvent faux, rédigés avec l'IA. Tony Ghilain décrit ensuite des attaques plus sophistiquées, avec le retour des buffer overflows, et l'usage offensif de l'IA par sa propre équipe : une preuve de concept se fait en trente minutes, contre plusieurs mois de travail d'un chercheur. Il passe aux agents attaquants, orchestrés avec des outils comme Nmap ou Shodan, et à une riposte qu'il dit avoir rencontrée sans affirmer qu'elle soit déployée chez Decathlon : glisser des injections de prompt dans les messages d'erreur d'un site pour retourner les agents contre eux-mêmes. Il tempère : les agents ne remplacent pas les meilleurs hackers, et le pentest assisté par IA rate des points majeurs. Vient la menace interne, le vibe coding : de nombreuses applications générées par les métiers, découvertes à temps, d'où le blocage réseau du shadow AI et un programme transverse d'outils validés et de contrôles. Il conclut sur une course-poursuite où les attaquants ont pris de l'avance et où le défenseur doit colmater toutes les failles quand l'attaquant n'en a besoin que d'une.

## 4. Citations et noms
**Citations** :
- « Il a toujours été plus simple de casser que de réparer. », Tony Ghilain, Decathlon
- « La confiance n'empêche pas le contrôle. », Tony Ghilain, Decathlon

**Noms cités** :
- *Tony Ghilain* : Senior Cybersecurity Strategist & Governance chez Decathlon.
- *Decathlon* : distributeur, exemple de vibe coding interne détecté et encadré.
- *Base44* : outil de génération d'applications complètes par prompts, cité comme vecteur de vibe coding.
- *Nmap, Shodan* : outils de reconnaissance réseau que des agents attaquants peuvent piloter.
- *Tech Show Paris 2026* : salon où l'entretien a été tourné.

## 5. Mots-clés
shadow AI, vibe coding, sécurité, gouvernance IA, agents IA, retour d'expérience

## Lecture CPO
- **Implications** :
  - Si l'entreprise pousse ses métiers vers le prototypage IA, prévoir dès le départ le chemin vers la production (outils validés, revue de sécurité) : sinon la sécurité finira par bloquer, comme chez Decathlon.
  - Inscrire les applications vibe-codées dans l'inventaire du portefeuille : ce sont des actifs non référencés, avec données et serveurs.
  - Pour un produit IA exposé (agent, chatbot), traiter l'injection de prompt comme un risque de conception, dans les deux sens : être attaqué et servir de vecteur.
- **Fiabilité** : praticien d'un grand groupe, sans produit à vendre ; propos oraux et anecdotiques, aucun chiffre en dehors du délai de POC. Sujet de cybersécurité, retenu parce qu'il éclaire la gouvernance du shadow AI et du vibe coding en entreprise.
- **Maturité** : Tendance émergente : la prolifération d'applications générées par les métiers commence à être traitée comme un sujet de sécurité et de gouvernance dans les grands groupes.
- **Réutilisation** : post LinkedIn « Le vibe coding des métiers, vu par la sécurité » ; table ronde sur la démocratisation du prototypage IA (avec Talbot et Uber) ; à citer en appui, pas comme source principale.
