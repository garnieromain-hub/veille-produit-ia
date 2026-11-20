---
name: fiche-source
description: Analyse une source (article, étude, billet, vidéo, rapport) et en produit une fiche de veille selon la grille de Romain, orientée CPO et PM. À utiliser dès que Romain partage un lien ou un document à analyser, demande ce qu'il faut retenir d'un contenu, ou qu'une veille produit et IA est en cours, même sans dire « fiche ».
---

# Fiche source

## Étapes

1. Lire la source en entier (pas seulement le chapeau). Si elle est inaccessible
   (paywall, lien mort), le signaler et s'arrêter.
2. Vérifier dans `liste-articles.md` et `sources/` qu'elle n'a pas déjà été
   fichée (même lien).
   Si oui, renvoyer la fiche existante.
3. Repérer le point de comparaison avant d'écrire « Ce qui est nouveau » :
   chercher dans `sources/` les fiches qui partagent des mots-clés ou des noms
   avec la source, et noter ce que l'auteur ou le média a déjà publié sur le
   sujet s'il est cité.
4. Remplir la grille ci-dessous, dans l'ordre. Rester factuel : chaque
   affirmation doit venir de la source. Si un champ n'a pas de matière, écrire
   « rien de notable ».
5. La ligne « Référence » contient toujours le lien complet : c'est lui qui
   sert à repérer les doublons. Sans lien public, le noter explicitement.
6. Écrire la fiche dans `sources/AAAA-MM-JJ-slug.md` (date du jour d'analyse).
7. Ajouter une ligne en haut du tableau de `liste-articles.md`, au même format
   que les lignes existantes, avec la langue de la source (Français ou Anglais) (sauf si c'est l'agent `veilleur` qui s'en charge).

## Grille

Les cinq premières sections forment le cœur de la fiche, toujours dans cet
ordre. La section « Lecture CPO » vient ensuite, en version courte.

```markdown
# Titre de la source

**Référence** : auteur, média, date de publication, format (article, étude,
podcast, vidéo, rapport), lien

**Axe** : axe principal, et au plus un axe secondaire entre parenthèses, parmi
les cinq axes du « Périmètre de la veille » de `CLAUDE.md` (Product management,
IA appliquée au produit, Transformation des entreprises, Portefeuille numérique,
Investissement tech)

## 1. L'idée clé
Une à trois phrases : la thèse de la source, formulée comme l'auteur la
défendrait. Pas un sujet (« l'article parle de… ») mais une affirmation.

## 2. Ce qui est nouveau
**Par rapport à** : nommer explicitement le point de comparaison, au choix ou
cumulés :
- les fiches déjà dans `sources/` (lien relatif vers la fiche) ;
- le discours dominant sur le sujet (le résumer en une phrase) ;
- les publications précédentes du même auteur ou média.

Puis 2 à 5 puces, chacune commençant par l'apport en gras, suivie d'une phrase
qui dit en quoi il diffère du point de comparaison.
Être exigeant : si la source redit ce qu'on sait, l'écrire en une ligne
(« Redite de … ; seul apport : … » ou « Rien de neuf par rapport à … »).

## 3. Résumé
Le fil de l'article, dans l'ordre où l'auteur le déroule : point de départ
(constat, problème, anecdote), développement (arguments, exemples, données),
retournement ou tension s'il y en a, conclusion ou appel à l'action.
5 à 12 lignes en prose, ou une courte liste numérotée si la source est
structurée en étapes. Garder les exemples et chiffres marquants, avec leur
origine. Ne pas réordonner par thème : on doit pouvoir raconter l'article
après l'avoir lu.

## 4. Citations et noms
**Citations** : 1 à 3 phrases courtes, fidèles, réutilisables, avec leur auteur.
Si traduites, donner l'original entre parenthèses.

**Noms cités** : personnes, entreprises, études, frameworks ou concepts nommés
dans la source, chacun avec une précision sur son rôle dans le propos.
- *Nom* : qui il est / ce qu'il apporte dans l'article.

## 5. Mots-clés
3 à 6 mots-clés thématiques, en minuscules, séparés par des virgules.
Uniquement des concepts (pas de noms propres : ils sont dans la section 4).
Réutiliser en priorité les mots-clés déjà présents dans `sources/` pour que
les fiches se retrouvent entre elles ; n'en créer un nouveau que si aucun
existant ne convient.

## Lecture CPO
- **Implications** : 2 à 4 puces concrètes (décision, pratique, organisation
  ou compétence concernée).
- **Fiabilité** : qui parle et avec quel intérêt (éditeur, fonds, vendeur de
  formation, praticien) ; chiffres sourcés ou non, méthodologie publique ou non.
- **Maturité** : Signal faible | Tendance émergente | Pratique établie, avec une
  phrase de justification.
- **Réutilisation** : article OCTO, post LinkedIn, table ronde, présentation
  client : lesquels et sous quel angle.
```

## Ton
Direct, sans jargon inutile, écrit pour un lecteur qui n'a pas le temps de lire
la source et doit pouvoir en parler après la fiche. L'idée clé et « Ce qui est
nouveau » doivent suffire à décider si la source vaut d'être citée ; le résumé
sert à la raconter.
