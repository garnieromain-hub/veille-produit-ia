# 3 enseignements à retenir de l'événement Transfo IA avec Adeo, Carrefour et Renault

**Référence** : Tanguy Verluise, Le Ticket, 6 novembre 2026,
https://www.le-ticket.fr/transfo-ia-adeo-carrefour-renault-enseignements/151611/
(lu via un export PDF : https://pub-cdn.apitemplate.io/2026/11/1a2cc409-f0d8-478e-99b7-ef09550a8638.pdf)

> Limite de lecture : l'article est réservé aux membres Premium du Ticket. L'export PDF
> contient le texte, mais pas les visuels : le modèle MASTER de Carrefour, la matrice des
> 4 niveaux de maturité de Renault, celle de Devoteam et la vidéo de SPARK. Les 4 niveaux
> de Renault ne sont donc pas décrits ici.

## Idée clé
Compte rendu d'une table ronde du 30 septembre 2026, co-organisée par Le Ticket et Devoteam
chez Maestro, sur la transformation IA des équipes produit en grand groupe. Les trois
entreprises suivent le même schéma. Elles formalisent d'abord leur processus produit, puis
y branchent des agents IA connectés au contexte interne. Enfin, elles renoncent à mesurer
le ROI tâche par tâche.

## Ce qui est nouveau
Ce sont surtout des retours d'expérience concrets et chiffrés de grands groupes français,
plus rares que les témoignages de scale-ups américaines :
- **Adeo, « construire plutôt qu'adopter »** : l'équipe a d'abord testé le framework
  open-source BMAD, rebaptisé « BMADEO ». Elle l'a abandonné : il impose un IDE (VS Code,
  Claude Code, Copilot…), ce qui freine le passage à l'échelle pour des PM, et il est verbeux,
  donc coûteux en tokens. Adeo a construit à la place SPARK, une plateforme d'une trentaine
  d'agents connectés au design system, aux workflows internes et à Jira. Elle est en bêta
  auprès de plus de 1 200 collaborateurs. Le skill le plus utilisé génère des tickets. Ce
  détail est intéressant : l'usage dominant reste une tâche à faible valeur.
- **Les PRD produits grâce à l'IA** : selon Adeo, l'IA améliore la qualité parce qu'elle
  fait produire des livrables qui n'étaient pas rédigés avant, comme les PRD. L'effet tient
  moins à un travail plus rapide qu'à un travail plus complet.
- **Un cas d'usage peu cité** : vérifier qu'une solution n'a pas déjà été traitée ailleurs
  dans le groupe, pour lutter contre la redondance propre aux grandes organisations.
- **Carrefour, le design comme catalyseur** : plus de 70 agents et « Gems » (Gemini,
  NotebookLM, Figma Make) sont intégrés au processus produit MASTER. La communauté de
  pratique design pilote, avec l'équipe transformation, les formations IA (avec AI
  Discipline) et les rituels de partage.
- **Renault et l'abandon de la mesure fine** : l'équipe a d'abord voulu calculer le temps
  gagné par personne et par tâche. Sébastien Warembourg reconnaît que c'était une erreur :
  on passait plus de temps à mesurer qu'à tirer de la valeur. Renault mesure désormais ce
  qui est produit et suit la progression de maturité par cohorte, avec une matrice en
  4 niveaux. La direction a accepté de traiter le sujet comme un investissement. Autre
  choix : une plateforme volontairement multi-fournisseurs, pour ne pas dépendre d'un seul
  éditeur ni de sa politique de prix.

Sont des redites : l'idée que l'IA agit comme un révélateur des processus (il faut revoir le
processus avant d'y ajouter de l'IA), la lutte contre le shadow AI et le gain de vitesse sur
les tâches à faible valeur.

## Implications pour un CPO ou un PM
- **Process avant outils** : les trois groupes avaient (ou ont formalisé) un cadre produit
  commun avant d'y brancher l'IA. Sans process explicite, il n'y a rien à outiller.
- **Plateforme interne ou outil du marché** : le cas Adeo donne deux critères concrets pour
  trancher, l'accessibilité pour des non-développeurs (pas d'IDE) et la maîtrise des coûts
  en tokens. Une plateforme d'agents contextualisés est aussi la réponse au shadow AI.
- **Mesure** : ne pas lancer de chronométrage tâche par tâche. Mesurer les livrables
  produits et la maturité par cohorte, et obtenir de la direction que le sujet soit traité
  comme un investissement de montée en compétence.
- **Organisation** : une communauté de pratique (ici le design) peut porter la diffusion de
  l'IA de façon transverse, en lien avec l'équipe transformation.
- **Fournisseurs** : penser la réversibilité dès le départ, avec une approche multi-modèles.

## Fiabilité
Il s'agit de témoignages de praticiens en poste (déclaratifs, sans métrique d'impact :
Adeo admet que l'impact est « extrêmement difficile » à mesurer), relayés par un média
produit dans un événement co-organisé avec Devoteam, un cabinet qui vend ce type
d'accompagnement. Le seul chiffre est celui de l'adoption de SPARK (1 200 utilisateurs).

## Maturité
Tendance émergente. Les grands groupes passent de l'expérimentation individuelle à des
plateformes d'agents internes à l'échelle, mais tous sont encore en bêta ou en cours de
structuration, et aucun n'a mesuré l'impact.

## Citation
« On a passé plus de temps à essayer de mesurer qu'à réellement tirer de la valeur de la
mesure ! » (Sébastien Warembourg, Renault)

## Réutilisation
- **Article OCTO** : « Mesurer le ROI de l'IA produit : pourquoi le chronomètre ne marche
  pas ». Le cas Renault (mesure par cohorte et par livrable) sert de pivot.
- **Post LinkedIn** : le skill le plus utilisé chez Adeo génère des tickets Jira. Cela pose
  la question de ce que l'IA change vraiment dans le métier de PM.
- **Table ronde ou présentation client** : le schéma commun aux trois groupes (process
  formalisé, puis agents contextualisés, puis mesure de la maturité) donne une trame de
  feuille de route de transformation IA pour un grand compte. On peut y ajouter l'arbitrage
  plateforme interne ou outil du marché (BMAD contre SPARK).

**Tags** : transformation IA, grands groupes, plateforme d'agents, mesure du ROI, maturité IA
