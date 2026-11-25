# Confidences d'un Citizen Developer : quand les équipes métiers se mettent à coder avec l'IA

**Référence** : Charles Fandre (marketing, Thiga), Thiga Media, mis à jour le 24 novembre 2026, article (retour d'expérience), https://www.media.thiga.co/citizen-developer-ia

**Axe** : Transformation des entreprises (IA appliquée au produit)

## 1. L'idée clé
Avec l'IA, n'importe quel salarié peut coder, et la surface de risque explose. Ni la charte ni l'interdiction ne tiennent : ce qui distingue un bon d'un mauvais citizen developer n'est pas son niveau technique mais l'outillage, la culture et l'accompagnement que lui donne l'entreprise, jusqu'à une sécurité « by design » en trois couches (skills, hooks et CI, plateforme interne).

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Ghilain chez Decathlon](2026-11-23-itforbusiness-decathlon-ghilain-ia-cybersecurite.md) (blocage du shadow AI et programme d'outils validés), la fiche [Colisto sur le build versus buy](2026-11-23-cio-colisto-build-versus-buy-ia.md) (deux gouvernances, ingénierie et métiers), la fiche [TPC sur le Product Builder](2026-10-16-tpc-product-builder-outils-internes.md) et la fiche [Talbot sur le vibe coding](2026-10-16-talbot-vibe-coding-decisions-cachees.md).
- **Le point de vue du métier qui code, pas de la DSI qui contrôle** : un marketeur raconte comment il a appris (discussions internes, workshops, retours d'expérience) et adopté des réflexes de développeur (tests en local, pull requests systématiques, dépôt commun). Les fiches précédentes parlaient des citizen developers, celle-ci leur donne la parole.
- **Une architecture de garde-fous en trois couches** : des skills (fichiers markdown qui encodent les standards, comme le design system), des hooks et de la CI qui vérifient ce que produit l'agent, et une plateforme interne, « golden path » qui rend certaines erreurs impossibles (serveurs, accès aux données, authentification). Plus concret que les « limites définies » de Colisto.
- **L'aveu d'une limite** : même avec dépôt commun et pull requests, la relecture humaine ne suit plus le rythme de production ; d'où l'automatisation des contrôles.
- **Deux chiffres de contexte** : Gartner, 41 % des salariés créaient déjà des outils hors DSI avant ChatGPT ; Veracode (juillet 2026), sur plus d'une centaine de modèles, l'option risquée choisie près d'une fois sur deux.

## 3. Résumé
L'article part d'un constat : avec l'IA, tout salarié peut coder, souvent hors du radar de l'IT, et les outils de vibe coding ne gèrent pas la sécurité. Exemple : Enrichlead, SaaS de Leonel Acevedo construit avec Cursor, annoncé sur X mi-mars 2025 comme écrit « sans une ligne de code à la main », piraté deux jours plus tard (paywall vérifié en JavaScript côté navigateur, clé d'API exposée). L'auteur explique ensuite le « trou dans la raquette » : la rareté du code limitait le périmètre à surveiller, sa banalisation l'étend énormément (l'image d'un Louvre aux fenêtres ouvertes). Il écarte deux réponses faciles : la charte assortie d'un atelier, peu suivie, et l'interdiction, mauvais signal qui prive l'entreprise de gains. Il soutient que bon et mauvais citizen developer peuvent avoir le même niveau : la différence tient à l'outillage, la culture et l'accompagnement. Il raconte son propre apprentissage chez Thiga et ses réflexes de développeur, tout en reconnaissant que la relecture humaine ne suit plus. Il détaille alors la sécurité by design en trois couches : skills, hooks et CI, plateforme interne en golden path. Il s'appuie sur Gartner (41 %) et Veracode (option risquée choisie près d'une fois sur deux). Conclusion : les citizen developers deviennent un atout s'ils sont à la fois encouragés et encadrés.

## 4. Citations et noms
**Citations** :
- « Avec l'IA, n'importe quel salarié peut coder », Charles Fandre
- « Près d'une fois sur deux, c'est la risquée qui a été choisie. », Charles Fandre, à propos de l'étude Veracode

**Noms cités** :
- *Charles Fandre* : auteur, marketing chez Thiga, citizen developer lui-même.
- *Olivier Bergeret* : directeur des équipes tech de Thiga, relecteur technique de l'article.
- *Enrichlead, Leonel Acevedo* : SaaS vibe-codé avec Cursor, piraté deux jours après son lancement (mars 2025).
- *Gartner* : 41 % des salariés créaient des outils technologiques ou analytiques hors DSI avant ChatGPT.
- *Veracode* : étude de juillet 2026 sur plus de cent modèles, option risquée choisie près d'une fois sur deux.
- *Windsurf, Cursor, Antigravity, Claude Code, Codex* : outils de code assisté cités.
- *MCP* : serveur interne utilisé pour piloter le CMS.
- *Golden path* : plateforme interne qui balise le chemin sûr et rend certaines erreurs impossibles.

## 5. Mots-clés
vibe coding, shadow AI, sécurité, gouvernance IA, harnais agentique, retour d'expérience

## Lecture CPO
- **Implications** :
  - Préférer à la charte et à l'interdiction un chemin balisé : skills qui encodent les standards, contrôles automatiques, plateforme interne qui gère hébergement, données et authentification.
  - Considérer la plateforme interne pour citizen developers comme un produit à part entière, avec ses utilisateurs (les métiers) et son équipe.
  - Prévoir l'accompagnement (workshops, partage de retours) dans le budget de déploiement des outils de code, pas seulement les licences.
  - Ne pas compter sur la relecture humaine pour absorber le volume : automatiser la vérification.
- **Fiabilité** : témoignage d'un salarié de Thiga, cabinet de conseil produit qui vend de l'accompagnement à la transformation : intérêt à promouvoir l'encadrement plutôt que l'interdiction. Relecture technique interne ; chiffres Gartner et Veracode cités sans détail méthodologique. Retour d'expérience à l'échelle d'un cabinet, pas d'un grand groupe.
- **Maturité** : Tendance émergente : le citizen development par l'IA se diffuse vite, mais les plateformes golden path pour métiers restent rares.
- **Réutilisation** : post LinkedIn (« le bon citizen developer n'est pas plus technique, il est mieux outillé ») ; table ronde DSI et métiers sur le shadow AI ; article OCTO sur la plateforme interne comme réponse au vibe coding.
