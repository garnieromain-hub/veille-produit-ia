# Three LLM inflection points in twelve months

**Référence** : Simon Willison, Simon Willison's Weblog, 24 novembre 2026, billet de blog (version écrite d'une keynote à l'AI Engineer Code Summit), https://simonwillison.net/2026/Nov/24/llm-inflection-points/

**Axe** : IA appliquée au produit (Product management)

> **Conflit d'intérêts** : cette fiche a été rédigée par un modèle Claude, de la même famille que plusieurs des modèles dont le billet décrit les progrès (Opus 4.5, Fable 5, Opus 5.5, Fable 5.2). Les jugements sont ceux de l'auteur, repris sans commentaire sur les modèles eux-mêmes.

## 1. L'idée clé
En douze mois, les LLM ont franchi trois seuils qui changent ce qu'on peut leur confier : des agents de code dont le résultat par défaut est correct (novembre 2025), des modèles qui résolvent par force brute tout problème dont on fixe l'objectif et fournit les outils (été 2026), puis la 3D et le jeu vidéo (automne 2026). Pour l'auteur, si l'on peut imaginer puis décrire clairement un logiciel, le modèle peut le construire.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [VentureBeat sur Fable 5.2 et Opus 5.5](2026-11-24-venturebeat-test-correction-bugs-fable-opus.md) (Fable trois fois plus cher pour un résultat proche sur la correction de bugs) et le discours dominant, qui mesure les progrès des modèles par benchmarks et classements.
- **Une chronologie par seuils d'usage, pas par benchmarks** : chaque point d'inflexion est défini par ce qu'un praticien a pu faire du jour au lendemain (passer au travail réel en janvier 2026, déboguer Safari sans intervention, rendre un jeu « plus amusant »). Une grille de lecture utile pour dater les changements de pratique.
- **La définition de la « classe Fable »** : un modèle qui, si l'on définit un objectif et fournit les outils, trouve la solution par force brute, en construisant lui-même ses instruments (capture d'écran et serveur de journalisation pour un bug Safari, localisation d'un bip à environ 40 cm avec cinq micros WebAudio).
- **Un domaine nouveau, le goût** : après environ 12 heures de tests et de rééquilibrage, Opus 5.5 a rendu un jeu de stratégie nettement plus engageant ; Willison dit de Fable 5.2 qu'il a un goût proche du sien. Le jugement qualitatif, jusqu'ici réservé à l'humain, entre dans le périmètre.
- **Le contrepoint au test VentureBeat** : l'auteur qualifie Opus 5.5 de « Fable bon marché », ce qui rejoint la conclusion de VentureBeat sur l'écart coût/résultat.

## 3. Résumé
Le billet reprend une keynote donnée quelques semaines plus tôt. Premier point d'inflexion, novembre 2025 : un an avant le billet sort Claude Opus 4.5. Claude Code existait depuis février 2025 mais restait peu fiable ; Opus 4.5 est le premier modèle dont le résultat par défaut est généralement correct, et GPT-5.1 (dont Codex et Codex-Max) produit un effet similaire côté Codex. Les vacances de décembre servent à expérimenter, et en janvier ces outils passent au travail réel. Deuxième point, juin-juillet 2026 : Anthropic annonce en avril Claude Mythos, jugé trop dangereux à publier pour ses capacités en cybersécurité, puis sort en juin Claude Fable 5, version bridée, retirée pour des contrôles à l'exportation américains et revenue le 1er juillet. Willison définit la classe Fable par la résolution par force brute et donne ses exemples (bug Safari, bip localisé). Il range Opus 5.5 (« Fable bon marché »), GPT-6 Astra et peut-être Gemini 4 Neon dans cette classe. Troisième point, septembre-octobre 2026 : la 3D (Blender, Three.js, une animation de mech new-yorkais par Gemini 4 Neon) et le jeu vidéo ; un jeu de braquage de raton laveur par Fable 5 en août était médiocre, GPT-5.6 Sol Ultra fait mieux, et Opus 5.5 (sorti le 22 septembre) rend un jeu de stratégie vraiment plus amusant. Il note que la scène indépendante est divisée sur l'IA. Il hésite encore à faire de Fable 5.2 un quatrième point, tout en citant sa productivité (Datasette 1.0a42 à 1.0a44 et LLM 0.37 à 0.38 en trois semaines). Conclusion : il ne pense plus revenir à l'écriture manuelle du code.

## 4. Citations et noms
**Citations** :
- « Si vous pouvez imaginer puis décrire clairement un logiciel, Fable peut le construire. » (« if you can imagine and then clearly describe a piece of software, Fable can build it »), Simon Willison

**Noms cités** :
- *Simon Willison* : développeur (Datasette, LLM), blogueur de référence sur les usages des LLM.
- *Claude Opus 4.5, Claude Code (Anthropic)* : premier point d'inflexion, les agents de code fiables par défaut.
- *GPT-5.1, Codex (OpenAI)* : effet équivalent côté OpenAI.
- *Claude Mythos, Claude Fable 5 et 5.2* : modèle non publié pour raisons de sécurité, puis sa version bridée ; deuxième point d'inflexion.
- *Claude Opus 5.5* : « Fable bon marché », auteur du jeu rendu plus amusant.
- *GPT-6 Astra, GPT-5.6 Sol Ultra (OpenAI), Gemini 4 Neon (Google)* : autres modèles rangés dans la classe Fable ou cités pour la 3D et le jeu.
- *Blender, Three.js, WebAudio* : outils mobilisés par les modèles dans les exemples.
- *AI Engineer Code Summit* : conférence où la keynote a été donnée.

## 5. Mots-clés
agents IA, autonomie des agents, prototypage, productivité IA, modèles de fondation

## Lecture CPO
- **Implications** :
  - Le goulot se déplace vers la capacité à décrire clairement ce qu'on veut : la qualité de la spécification et de l'objectif devient la compétence clé du PM.
  - Donner aux agents des objectifs vérifiables et les outils pour les atteindre (accès à l'environnement, instrumentation) plutôt que des instructions pas à pas.
  - Réévaluer tous les six mois ce qui peut être délégué : les seuils changent à un rythme supérieur aux cycles de planification.
  - Le jugement qualitatif (l'« amusant », le goût) commence à être déléguable, ce qui touche le design et la discovery.
- **Fiabilité** : praticien indépendant reconnu, sans lien commercial déclaré avec les éditeurs, mais retour d'usage personnel sur ses propres projets open source, sans mesure ni comparaison contrôlée. Exemples précis et vérifiables (versions publiées).
- **Maturité** : Tendance émergente : les agents de code sont désormais utilisés au quotidien par les praticiens avancés, mais la délégation par objectif et la 3D restent des usages de pointe.
- **Réutilisation** : présentation client (frise des trois points d'inflexion pour dater les changements de pratique) ; post LinkedIn sur la spécification comme compétence clé ; table ronde PM sur ce qui reste humain dans la construction produit.
