# D'une semaine à 20 minutes : comment le fabricant du Doliprane automatise son marketing grâce à l'IA

**Référence** : Benjamin Polge, Journal du Net, 25 novembre 2026, article (retour d'expérience), https://www.journaldunet.com/intelligence-artificielle/1559115-comment-le-fabricant-du-doliprane-automatise-son-marketing-grace-a-l-ia/

**Axe** : Transformation des entreprises (IA appliquée au produit)

## 1. L'idée clé
Dans un secteur réglementé, le goulot du marketing n'est pas la création mais la validation de conformité. Opella l'a confié à un système de 14 agents spécialisés orchestrés, qui ramène la validation d'un contenu pour les réseaux sociaux d'une semaine à 20 minutes, tout en laissant à un humain le lancement et la responsabilité finale.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Sahni, ce que dev et QA attendent l'un de l'autre](2026-11-23-cio-sahni-dev-qa-code-ia.md), qui situe le goulot dans la vérification quand l'IA produit, et la fiche [Ally Financial et les personas agentiques](2026-11-25-cio-ally-personas-agentiques.md), autre retour d'expérience agentique d'un secteur réglementé ; plus largement, le discours dominant sur l'IA en marketing, centré sur la génération de contenus.
- **L'IA appliquée au goulot plutôt qu'à la production** : Opella automatise d'abord la vérification (allégations, mentions obligatoires, chartes), assurée jusque-là par des médecins et des pharmaciens. C'est la réponse au problème qu'ouvre la génération massive de contenus (jusqu'à 30 fois plus, selon l'entreprise).
- **Une architecture lisible** : un agent par point de contrôle (14 au total) et un agent d'orchestration. Ce découpage par règle rend chaque contrôle testable séparément, ce qui le distingue d'un assistant généraliste.
- **Le routage de modèles en production** : démarré sur des modèles GPT d'OpenAI et des modèles spécialisés de Microsoft, l'outil choisit désormais le modèle le plus adapté à chaque tâche.
- **Une organisation dédiée** : plus de 85 personnes réparties dans six ateliers internes de création par IA, et un principe explicite, « human first, human last ».
- **Le contenu pour les assistants conversationnels** : la prochaine étape est de produire des contenus destinés à ChatGPT ou Gemini, signe que ces assistants deviennent un canal marketing à part entière.

## 3. Résumé
L'article présente Opella, ancienne branche grand public de Sanofi, fabricant du Doliprane, détenue à 50 % par le fonds américain CD&R. Point de départ : dans la santé, chaque contenu marketing doit être validé scientifiquement et réglementairement, par des médecins et des pharmaciens, et cette validation prenait une semaine. Opella a construit Lumen, un système de 14 agents d'IA dont chacun vérifie un point de contrôle (allégations, mentions obligatoires, chartes de marque), coordonnés par un agent d'orchestration. L'outil, développé avec Microsoft sur Microsoft Foundry, a d'abord utilisé des modèles GPT d'OpenAI et des modèles spécialisés de Microsoft, puis a évolué vers une sélection automatique du modèle selon la tâche. Lumen est déployé depuis octobre sur trois marchés : la Pologne, l'Allemagne et le Mexique. Selon Julien Leterrier, global head of martech, la validation d'un contenu pour les réseaux sociaux est passée d'une semaine à 20 minutes, et l'IA générative permet de produire jusqu'à 30 fois plus de contenus. Plus de 85 personnes travaillent dans six ateliers internes de création par IA. Le principe reste « human first, human last » : un humain lance le flux et un humain répond du contenu final. Les prochaines étapes : de nouveaux agents vérificateurs et des contenus pensés pour les assistants conversationnels comme ChatGPT ou Gemini.

## 4. Citations et noms
**Citations** :
- « Ce sont des médecins, des pharmaciens, qui vérifient que chaque contenu est scientifiquement exact » (Julien Leterrier, Opella).
- « Nous avons raccourci les temps de validation, il fallait une semaine pour valider un contenu » (Julien Leterrier).
- « Un humain initie le flux et, à la fin, c'est un humain qui est responsable du contenu » (Julien Leterrier).

**Noms cités** :
- *Benjamin Polge* : journaliste au Journal du Net, auteur.
- *Opella* : ancienne branche santé grand public de Sanofi, fabricant du Doliprane, entreprise étudiée.
- *Sanofi* : ancien propriétaire, encore actionnaire.
- *CD&R* : fonds américain qui détient 50 % d'Opella.
- *Julien Leterrier* : global head of martech d'Opella, source des chiffres.
- *Lumen* : système interne de 14 agents de conformité et d'un agent d'orchestration.
- *Microsoft, Microsoft Foundry* : partenaire de développement et plateforme technique.
- *OpenAI (modèles GPT)* : modèles utilisés dans la première version.
- *ChatGPT, Gemini* : assistants visés par les futurs contenus.
- *« Human first, human last »* : principe de supervision humaine en début et en fin de flux.

## 5. Mots-clés
agents IA, goulot d'étranglement, vérification, routage de modèles, retour d'expérience, gouvernance IA

## Lecture CPO
- **Implications** :
  - Avant d'outiller la production avec l'IA, repérer où se situe le goulot (souvent la validation) : accélérer la création sans traiter la vérification ne fait que déplacer l'attente.
  - Pour un produit agentique en contexte réglementé, découper par règle de contrôle (un agent par point vérifiable) facilite les evals, l'audit et l'ajout de nouvelles règles.
  - Préciser dès la conception qui lance le flux et qui signe le résultat : le « human first, human last » est une décision produit et organisationnelle, pas seulement une précaution.
  - Préparer les équipes marketing et produit aux assistants conversationnels comme canal : contenus, formats et mesure à repenser.
- **Fiabilité** : chiffres déclaratifs de l'entreprise (une semaine à 20 minutes, 30 fois plus de contenus), sans méthode de mesure ni taux d'erreur ou de rejet publié ; projet mené avec Microsoft, qui a intérêt à le mettre en avant. Le gain porte sur les contenus pour les réseaux sociaux, pas sur l'ensemble du marketing, et sur trois marchés seulement.
- **Maturité** : Tendance émergente : les systèmes multi-agents de vérification passent en production dans des secteurs réglementés, mais le recul (deux mois, trois pays) reste faible.
- **Réutilisation** : présentation client sur les agents en secteur réglementé (architecture un agent par contrôle, humain en début et fin de flux) ; post LinkedIn « l'IA sert d'abord à vérifier, pas à produire » ; table ronde sur les goulots déplacés par l'IA, avec la fiche Sahni.
