# Agents d'intelligence artificielle : qui répond de ce qu'ils font ?

**Référence** : Leila Kaoutar Benachour (consultante en stratégie et transformation data et IA chez DEEP, filiale de POST Luxembourg), IT Social, 20 novembre 2026, tribune, https://itsocial.fr/contenus/tribunes/agents-dintelligence-artificielle-qui-repond-de-ce-quils-font/

**Axe** : Transformation des entreprises (IA appliquée au produit)

## 1. L'idée clé
Confier une action à un agent ne lui transfère pas la responsabilité : avant de fixer son degré d'autonomie, il faut décider qui répond de ce qu'il fait. Cette question, plus que les capacités techniques, conditionne le passage en production.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Mind the Product sur les quatre niveaux d'autonomie](2026-11-19-mtp-quatre-niveaux-autonomie-ia.md) (l'autonomie se règle sur le coût de l'erreur), la fiche [Thoughtworks Radar vol. 35](2026-11-19-thoughtworks-radar-vol35.md) (l'humain dans la boucle peut devenir du théâtre) et la fiche [IT Social sur l'orchestration agentique](2026-11-20-itsocial-orchestration-agentique-dsi.md) (la pile technique de contrôle des agents).
- **Trois rôles nommés avant la mise en service** : le métier répond des résultats, les équipes techniques de la fiabilité et de la traçabilité, et une personne désignée gère les exceptions et peut seule suspendre l'agent. Les fiches précédentes parlaient d'outils et de niveaux, pas de qui porte la responsabilité.
- **Trois droits pour que le contrôle humain soit réel** : voir les actions de l'agent, contester ses propositions, l'interrompre. C'est une réponse opérationnelle au « théâtre » de l'humain dans la boucle relevé par Thoughtworks.
- **Le « coût jumeau »** : le gain de productivité est immédiat et mesurable, la perte de compétences est silencieuse et rend à terme le travail de l'agent invérifiable. L'autrice propose des exercices réguliers sans assistance, comme on prépare une reprise après panne.
- **Calendrier réglementaire mis à jour** : selon l'autrice, l'omnibus numérique entré en vigueur en juillet 2026 reporte les obligations de contrôle humain de l'AI Act pour les systèmes à haut risque au 2 décembre 2027, et au 2 août 2028 pour l'IA intégrée à des produits réglementés.
- Le critère d'autonomie (gravité, détectabilité, réversibilité de l'erreur) redit pour l'essentiel la grille de Mind the Product, en ajoutant la détection et la correction au seul coût de l'erreur.

## 3. Résumé
L'autrice part d'un constat : le débat sur les agents porte sur leurs capacités, alors que leur passage en production bute sur la responsabilité. Elle cite la prévision de Gartner (juin 2025) : plus de 40 % des projets d'IA agentique seraient abandonnés d'ici fin 2027, notamment faute de maîtrise des risques. Elle explique ensuite que le contrôle change de nature : un modèle produit un résultat, un agent enchaîne des actions dans plusieurs systèmes sans validation humaine systématique, donc le contrôle porte sur les droits qu'on lui accorde en amont. Le niveau d'autonomie se règle sur trois critères (gravité d'une erreur, capacité à la détecter à temps, possibilité de la corriger) et peut évoluer avec la fiabilité démontrée : délégation large pour un support informatique simple aux actions réversibles, vérification humaine obligatoire pour l'octroi de crédit, contrôle par échantillonnage pour les cas intermédiaires. Elle met en garde contre le contrôle de façade : à force de valider des résultats justes, la validation devient un réflexe ; il faut donc donner aux superviseurs trois droits (voir, contester, interrompre). Elle demande d'attribuer trois rôles avant la mise en service (métier, technique, responsable des exceptions). Elle décrit ensuite le « coût jumeau », la perte silencieuse de compétences, aggravée par le départ des experts, et recommande des exercices sans assistance pour préparer une panne, une cyberattaque ou la défaillance d'un fournisseur. Elle termine par le cadre juridique : l'AI Act impose un contrôle humain effectif pour les systèmes à haut risque (solvabilité, recrutement, éducation) et le développement des compétences IA du personnel, obligations reportées par l'omnibus numérique. Conclusion : inutile d'attendre ces échéances pour définir le périmètre d'action d'un agent, tracer ses actions et savoir qui accède à quelles données.

## 4. Citations et noms
**Citations** :
- « Un agent peut recevoir une délégation d'action, jamais une délégation de responsabilité. », Leila Kaoutar Benachour
- « Sans ces trois droits, l'humain dans la boucle n'est qu'un tampon. », Leila Kaoutar Benachour
- « Confier une action à un agent ne lui transfère pas la responsabilité qui l'accompagne. », Leila Kaoutar Benachour

**Noms cités** :
- *DEEP (POST Luxembourg)* : employeur de l'autrice, intégrateur et opérateur de services numériques.
- *Gartner* : prévision de juin 2025 sur l'abandon de plus de 40 % des projets d'IA agentique d'ici fin 2027.
- *Règlement européen sur l'IA (AI Act)* : impose un contrôle humain effectif pour les systèmes à haut risque et la formation du personnel à l'IA.
- *Omnibus numérique* : texte européen qui, selon l'autrice, reporte les obligations à haut risque au 2 décembre 2027 et au 2 août 2028.
- *Coût jumeau* : concept de l'autrice pour la perte de compétences qui accompagne le gain de productivité.

## 5. Mots-clés
agents IA, gouvernance IA, autonomie des agents, régulation, compétences, vérification

## Lecture CPO
- **Implications** :
  - Pour chaque agent mis en production, inscrire dans la fiche produit les trois rôles (responsable du résultat, responsable de la fiabilité, responsable des exceptions avec droit d'arrêt).
  - Concevoir l'interface de supervision autour des trois droits (voir, contester, interrompre) : c'est un sujet de design produit, pas seulement de conformité.
  - Prévoir dans la roadmap des exercices « sans agent » pour les processus critiques, au même titre que les plans de reprise.
  - Relier le niveau d'autonomie aux evals : on ne l'élargit qu'avec une fiabilité démontrée.
- **Fiabilité** : consultante d'un intégrateur qui vend de l'accompagnement data et IA ; tribune argumentée, un seul chiffre sourcé (Gartner, prévision et non mesure) ; les dates de report de l'AI Act sont données par l'autrice et sont à vérifier sur le texte officiel avant réutilisation.
- **Maturité** : Tendance émergente : la gouvernance des agents est un sujet partagé par plusieurs sources ce mois-ci, mais les rôles et droits proposés ne s'appuient sur aucun retour d'expérience chiffré.
- **Réutilisation** : post LinkedIn (« délégation d'action, jamais de responsabilité ») ; présentation client (grille trois critères, trois rôles, trois droits) ; table ronde sur le « coût jumeau » et la perte de compétences.
