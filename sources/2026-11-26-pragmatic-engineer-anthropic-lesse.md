# How Anthropic builds software in 2026 with Katelyn Lesse

**Référence** : Gergely Orosz (animateur) avec Katelyn Lesse (responsable de l'ingénierie plateforme chez Anthropic, ex-Stripe), The Pragmatic Engineer, 25 novembre 2026, podcast (1 h 49 min) ; fiche établie à partir des notes d'épisode publiques (12 points clés, chapitrage, références), la transcription n'étant pas présente sur la page, https://newsletter.pragmaticengineer.com/p/how-anthropic-builds-software-in

**Axe** : Transformation des entreprises (IA appliquée au produit)

## 1. L'idée clé
Chez Anthropic, les agents ont déjà pris en charge une part du travail d'ingénierie (réécriture de l'API en Rust, revue de code, premier niveau d'astreinte, onboarding), mais ils n'ont supprimé ni la planification, ni la coordination, ni les équipes « two-pizza ». Ce qui change le plus, ce sont les pratiques RH : l'entretien de code disparaît et la promotion se juge à l'impact, plus au temps passé.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Nadella sur le code bon marché](2026-11-19-pragmatic-engineer-nadella-code-bon-marche.md) (même podcast, vision d'un PDG), la fiche [OpenAI, performance factory Codex](2026-11-20-openai-performance-factory-codex.md) et la fiche [VentureBeat-LeadDev sur la revue de code par agents](2026-11-25-venturebeat-leaddev-revue-code-agents.md).
- **Un chantier critique mené avec environ 20 % de code relu** : l'API qui sert tous les tokens Claude a été réécrite de Python en Rust en environ cinq mois, par quelques ingénieurs sans expertise Rust. La sécurité venait du « shadowing » (rejouer le trafic de production jusqu'à obtenir des réponses identiques), pas de la relecture. La vérification change de forme : on teste par comportement plutôt que par lecture.
- **Un classifieur qui décide de la revue humaine** : un agent Claude juge chaque PR, décide si une revue humaine est nécessaire, laquelle et par quelle équipe ; les changements mécaniques partent en production sans humain. LeadDev montrait que l'agent relit son propre code ; ici, il trie aussi ce qui mérite un humain.
- **Ce qui ne change pas** : planification et alignement prennent autant de temps, les ingénieurs coordonnent plus qu'ils n'implémentent, et les équipes restent à 5-8 personnes. C'est un contrepoint aux discours sur l'équipe d'une personne.
- **La fin de l'entretien de code et de la promotion « au temps »** : l'entretien de code est abandonné parce que de bons candidats échouaient à coder à la main ; la durée d'un projet n'a plus de sens pour juger une promotion, remplacée par l'impact (CPU, latence, incidents évités). Nadella ne parlait pas de ces sujets RH.
- Les sujets les plus proches du produit (« PM qui livrent en production », « software factory » d'Anthropic) figurent dans le chapitrage mais ne sont pas détaillés dans les notes.

## 3. Résumé
L'épisode part de la réécriture de l'API Messages, créée en Python en 2023 quand Anthropic était surtout un laboratoire de recherche (OpenAI a connu le même parcours). La réécriture en Rust a pris environ cinq mois, sans experts Rust ni revues strictes, et a été validée par trafic fantôme jusqu'à réponses identiques ; Katelyn Lesse estime que les ingénieurs n'ont relu qu'environ 20 % du code. Viennent ensuite les agents au quotidien : un agent de revue tourne en permanence et décide du besoin de revue humaine ; un agent Claude est alerté avant l'humain en astreinte et trie le vrai incident du bruit, sans encore résoudre seul les incidents ; l'onboarding se résume à « parler à Claude », connecté au code et aux systèmes internes. Puis ce qui ne change pas : la planification, l'alignement et les équipes de 5 à 8 personnes qui possèdent leurs systèmes. Les ingénieurs passent beaucoup plus de temps à construire leurs propres outils, et maîtriser un langage compte moins. Côté RH, l'entretien de code est remplacé par des expérimentations avec des agents de codage (les entretiens de conception sont conservés) et les promotions s'évaluent à l'impact. L'introduction rappelle qu'Anthropic vaut environ 1 000 milliards de dollars avec un dixième des effectifs d'entreprises comparables. Conclusion de l'invitée : les ingénieurs ont encore beaucoup de problèmes à résoudre, liés aux agents eux-mêmes.

## 4. Citations et noms
**Citations** :
- « L'onboarding des nouveaux ingénieurs d'Anthropic, c'est "parler à Claude". » (« Onboarding for new Anthropic engineers is "talk to Claude." »), notes d'épisode
- « Pour les promotions, le "temps pour terminer un projet" n'a désormais plus de sens. » (« For promotions, the "time to complete a project" is now meaningless. »), notes d'épisode
- « L'équipe de Katelyn a supprimé l'entretien de code après que de bons candidats y ont échoué à répétition. » (« Katelyn's team phased out the coding interview after strong candidates kept failing it. »), notes d'épisode

**Noms cités** :
- *Katelyn Lesse* : responsable de l'ingénierie plateforme chez Anthropic, invitée.
- *Gergely Orosz* : animateur du podcast.
- *Anthropic* : entreprise décrite ; *Claude Messages API, Claude Code, Claude Managed Agents* : produits utilisés en interne.
- *Stripe* : ancien employeur de l'invitée.
- *OpenAI* : cité pour un parcours technique similaire et pour sa « software factory » agentique.
- *Rust, Python* : langages de la migration.
- *Shadow traffic* : technique de validation par rejeu du trafic de production.
- *Two-pizza teams* : format d'équipe de 5 à 8 personnes, inchangé.

## 5. Mots-clés
agents IA, vérification, modèle opérationnel, recrutement, retour d'expérience, usine logicielle

## Lecture CPO
- **Implications** :
  - Investir dans la vérification par comportement (tests de non-régression, trafic fantôme) plutôt que dans la relecture humaine exhaustive, si l'on confie de gros chantiers aux agents.
  - Ne pas réduire les équipes produit sur la seule promesse des agents : la planification et la coordination restent le goulot, même chez Anthropic.
  - Revoir les critères de recrutement et d'évaluation (entretiens, promotions) des équipes tech et produit : la vitesse d'exécution ne départage plus.
  - Organiser un triage par agent (revue, astreinte) avec des règles explicites sur ce qui exige un humain.
- **Fiabilité** : un éditeur d'IA qui décrit l'usage de ses propres produits, avec un intérêt évident à montrer leur efficacité ; ton plutôt nuancé (l'astreinte autonome n'est pas atteinte). Chiffres (20 % de code relu, cinq mois) estimés par l'invitée, non vérifiables. Fiche fondée sur les notes d'épisode : transcription non lue.
- **Maturité** : Tendance émergente : pratiques en place chez un acteur de pointe, pas encore généralisées ni mesurées ailleurs.
- **Réutilisation** : article OCTO sur la vérification à l'ère des agents (le cas Rust à 20 % de relecture) ; table ronde DSI (« ce que les agents n'ont pas changé chez Anthropic ») ; post LinkedIn sur la fin de l'entretien de code.
