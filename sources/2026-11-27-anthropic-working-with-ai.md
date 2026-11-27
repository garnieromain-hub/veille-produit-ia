# Working with AI

**Référence** : Nathan Wilmers, Maxim Massenkoff, Peter McCrory (équipe Economics, Anthropic), Anthropic, 23 novembre 2026, étude qualitative (rapport PDF avec annexe méthodologique), https://www.anthropic.com/research/working-with-ai

**Axe** : Transformation des entreprises

## 1. L'idée clé
La valeur de l'IA en entreprise dépend moins de la technologie que de la façon dont on réorganise le travail autour d'elle. L'automatisation imposée d'en haut est fragile et inquiète, l'expérimentation venue d'en bas reste isolée et crée des inégalités ; les entreprises qui en tirent le plus élargissent les rôles, réaffectent les gens aux tâches goulots et partagent données et infrastructure.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [NBER Firm Data on AI](2026-11-13-nber-firm-data-on-ai.md) (effet modeste sur la productivité, pas d'effet net sur l'emploi mais une forte rotation), la fiche [Fourquet](2026-11-26-silicon-fourquet-ia-individu-organisation.md) (l'IA augmente l'individu, pas l'organisation, avec la même analogie de Paul David) et la fiche [Pragmatic Engineer sur Anthropic](2026-11-26-pragmatic-engineer-anthropic-lesse.md) (comment Anthropic travaille en interne).
- **Du terrain plutôt que des déclarations agrégées** : 66 entretiens dans 58 entreprises américaines clientes et près de 300 usages codés, là où le NBER interroge des dirigeants par questionnaire. On voit les mécanismes, pas seulement les moyennes.
- **Les trois voies d'adoption et leurs échecs propres** : top-down (fragile, résistance des experts, « effet panoptique »), bottom-up (gains forts mais isolés, applications « zombies », « Claude grenades » envoyées à des collègues qui ne les lisent pas), réorganisation (élargir les rôles, réaffecter aux goulots, infrastructure commune). Fourquet ne donnait que la troisième.
- **L'emploi : on n'embauche plus plutôt qu'on ne licencie** : environ deux tiers des entreprises ont réduit leurs embauches à cause de l'IA, dont un tiers par non-remplacement des départs ; 2 seulement ont vu un poste disparaître, 9 ont réduit des prestataires (souvent offshore), 10 ont embauché davantage. Cela donne une forme concrète à la « rotation » du NBER.
- **La valeur vient surtout de la production, pas des coûts** : la plupart des usages augmentent la production (moitié par accélération, moitié par qualité ou nouveaux produits) ; 80 % des 100 logiciels construits automatisent un travail manuel, 20 % remplacent un logiciel souvent acheté à un éditeur.
- **Les goulots nommés** : volume de sorties à relire, décalage entre tâches accélérées et non accélérées (revue de code, ventes, décisions), adoption inégale, manque de contexte et de données ; la réglementation et le scepticisme des clients sont rarement cités.

## 3. Résumé
L'étude part de trois cabinets d'avocats qui utilisent la même technologie autrement : l'un automatise son courrier et menace l'accueil, l'autre n'arrive pas à faire adopter l'IA, le troisième réorganise le travail des juniors autour de brouillons générés. Les auteurs posent la question : comment les entreprises adoptent l'IA, où elles bloquent, comment réorganiser l'expertise humaine. Méthode : 66 entretiens dans 58 entreprises américaines clientes d'Anthropic (droit, startups natives de l'IA, industrie, santé, finance…), choisies pour leur diversité et non tirées au hasard, près de 300 usages codés par des outils automatisés sur la valeur perçue et le degré de changement organisationnel. Premier constat : la valeur vient surtout d'une production accrue (cabinet dentaire qui répond hors horaires, groupe médical qui estime les coûts) ; 100 logiciels décrits, 80 % automatisent un travail manuel. Deuxième partie, l'automatisation top-down : efficace sur les tâches modulaires (une fintech qui remplace plus de 100 prestataires offshore, une société de revue de documents qui prévoit de réduire de plus de 90 % ses relecteurs), mais vite obsolète, freinée par les experts (un processus de validation bloqué par les relecteurs) et porteuse de surveillance. Troisième partie, l'expérimentation bottom-up : des non-développeurs obtiennent de gros gains (un cabinet comptable qui audite des paiements 401(k), un investisseur immobilier qui remplace un outil à 10 000 $ par an), mais les projets restent isolés, demandent maintenance et support, et creusent les écarts entre collègues. Quatrième partie, la réorganisation : élargir les rôles à un flux complet, réaffecter aux tâches goulots (chefs de projet d'une entreprise de construction libérés pour parler aux clients), centraliser les données (une entreprise de transport routier), réorienter les stages (services financiers). Sur l'emploi : 5 entreprises ont écarté des salariés réfractaires, 2 ont supprimé un poste, 10 ont embauché, deux tiers ont réduit leurs embauches, et six startups estiment qu'il leur faudrait en moyenne quatre fois plus de salariés sans IA. Les auteurs listent leurs limites (échantillon non représentatif, valeurs déclarées, codage automatisé, constats vite périssables) et concluent que les employeurs ont une vraie marge de manœuvre, sans garantie contre le chômage induit par l'IA, qui appelle une réponse politique.

## 4. Citations et noms
**Citations** :
- « Peut-être qu'on ne licencie pas, mais on n'embauche pas. » (« We may not be firing, but we're not hiring. »), un interviewé
- « L'individu n'a pas l'autorité pour changer le travail. » (« The individual doesn't have the authority to change the work. »), un interviewé
- « Deux personnes plus Claude, c'est formidable… si deux personnes sont d'accord, on livre. » (« Two people plus Claude is the most amazing thing… if two people agree on something, just ship it. »), un interviewé

**Noms cités** :
- *Nathan Wilmers, Maxim Massenkoff, Peter McCrory* : auteurs, équipe économie d'Anthropic.
- *Paul David* : économiste ; l'image des « mill buildings » (usines passées à l'électricité sans réorganiser l'atelier) explique le retard des gains.
- *Anthropic Economic Index* : travaux précédents de l'équipe, cités sur le lien entre complexité des tâches et volume de contexte.
- *Étude HBS* : les startups natives de l'IA emploient moins de salariés.
- *Étude danoise* : environ 10 % des salariés qui gagnent du temps avec les chatbots prennent plus de pauses.
- *Claude grenades* : grands utilisateurs qui inondent leurs collègues de contenus générés, que ceux-ci refusent de lire.
- *Applications « zombies »* : outils internes générés, de faible qualité, peu utilisés.
- *Effet panoptique* : sentiment de surveillance permanente quand le travail est évalué en continu par l'IA.
- *Élargissement des rôles, tâches goulots* : les deux leviers de réorganisation identifiés.
- *Politique d'usage d'Anthropic* : rappelée sur la surveillance des salariés et l'humain dans la boucle pour les décisions RH.

## 5. Mots-clés
modèle opérationnel, emploi, adoption IA, goulot d'étranglement, conduite du changement, retour d'expérience

## Lecture CPO
- **Implications** :
  - Ne pas choisir entre top-down et bottom-up : prévoir dès le départ comment industrialiser les outils nés sur le terrain (maintenance, support, infrastructure de données commune), sinon ils deviennent des applications zombies.
  - Repérer les tâches non accélérées (revue, ventes, décisions) qui deviennent les goulots, et y réaffecter les gens libérés par l'IA.
  - Élargir les rôles à un flux complet plutôt qu'automatiser une tâche isolée, avec l'autorité pour changer le travail.
  - Côté emploi, regarder les embauches évitées et les prestataires réduits, pas seulement les licenciements : c'est là que l'effet apparaît d'abord.
- **Fiabilité** : étude d'Anthropic sur ses propres clients, donc biaisée vers des adoptants, avec un intérêt évident à montrer la valeur de Claude ; mais les auteurs documentent aussi les échecs et l'effet sur l'emploi, et publient leurs limites. Méthode qualitative, valeurs déclarées, échantillon non représentatif de 58 entreprises américaines, codage partiellement automatisé ; annexe méthodologique dans le PDF.
- **Maturité** : Tendance émergente : le constat « la valeur vient de la réorganisation » converge avec le NBER et plusieurs sources de novembre, mais les pratiques de réorganisation décrites restent des cas, sans mesure quantitative.
- **Réutilisation** : article OCTO sur les trois voies d'adoption et leurs échecs (avec Fourquet et le NBER) ; post LinkedIn « on ne licencie pas, on n'embauche plus » ; présentation comex sur les tâches goulots et l'élargissement des rôles ; table ronde sur les « Claude grenades » et la charge de relecture.
