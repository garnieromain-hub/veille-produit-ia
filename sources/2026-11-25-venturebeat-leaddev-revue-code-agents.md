# Nearly half of surveyed engineers and leaders say the AI agents that write their code also review it

**Référence** : Sean Michael Kerner, VentureBeat, 24 novembre 2026, article de reprise d'une enquête (LeadDev AI Code Review Report 2026), https://venturebeat.com/technology/nearly-half-of-surveyed-engineers-and-leaders-say-the-ai-agents-that-write-their-code-also-review-it

**Axe** : IA appliquée au produit (Transformation des entreprises)

**Avertissement** : l'enquête est sponsorisée par CodeRabbit, éditeur d'outils de revue de code par IA, qui a intérêt à présenter la revue comme le nouveau goulot. Son PDG est cité dans l'article.

## 1. L'idée clé
Avec les agents de code, la revue est devenue le goulot de la livraison logicielle, et les organisations y répondent mal : près de la moitié laissent les agents relire le code qu'ils ont écrit, peu ont des règles claires, et personne ne sait vraiment qui est responsable quand un agent écrit, un autre relit et un système fusionne.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Thoughtworks Radar vol. 35](2026-11-19-thoughtworks-radar-vol35.md) (le goulot passe à la capacité de revue), la fiche [Sahni sur le relais dev-QA](2026-11-23-cio-sahni-dev-qa-code-ia.md) (preuves proportionnées au risque) et la fiche [Benachour sur la responsabilité des agents](2026-11-23-itsocial-benachour-responsabilite-agents-ia.md). Le diagnostic est connu ; l'apport est chiffré.
- **L'autorelecture par les agents mesurée** : 47 % des répondants disent que leur organisation confie aux agents la revue du code qu'ils ont écrit, alors que 82 % disent relire à la main tout ou presque tout le code généré avant fusion. Les deux pratiques coexistent.
- **Le goulot chiffré** : 45 % désignent la capacité de revue comme le premier goulot de la livraison ; pour la moitié, les pull requests par développeur ont augmenté d'au moins 25 % ; 67 % les voient grossir ; plus de répondants voient les cycles de revue ralentir (38 %) qu'accélérer (25 %).
- **Peu de règles et peu de mesure** : 14 % ont des standards de revue du code généré, clairs et appliqués ; 24 % ne suivent aucune métrique de revue, 30 % suivent la consommation de tokens, 22 % les défauts échappés.
- **La compréhension en recul** : 26 % seulement se disent très confiants de comprendre les changements générés aussi bien que ceux écrits par un humain ; 18 % disent que les relecteurs ont assez de contexte pour juger l'impact sur l'architecture.
- **La responsabilité, question ouverte** : quand un agent écrit, un autre relit et un système fusionne, 48 % désignent celui qui a demandé le changement, 14 % l'approbateur.

## 3. Résumé
L'article présente le LeadDev AI Code Review Report 2026, sponsorisé par CodeRabbit : 377 ingénieurs et responsables d'ingénierie aux États-Unis et en Europe, dont 325 ont terminé le questionnaire (dates non précisées). Il part du constat de compréhension : 26 % seulement sont très confiants de comprendre le code généré comme du code humain. Il décrit ensuite la pression sur la revue : pull requests plus nombreuses (au moins +25 % pour la moitié) et plus grosses (67 %), revue citée comme premier goulot (45 %), cycles qui ralentissent plus souvent qu'ils n'accélèrent. Vient le chiffre du titre : 47 % laissent les agents relire leur propre code, alors que seuls 14 % ont des standards clairs ; 82 % relisent quand même à la main, mais 68 % disent que les relecteurs ne savent pas quels changements demandent plus d'attention, et 74 % font vérifier par un humain ce que signale l'outil de revue IA. Côté mesure, 24 % ne suivent rien. Sur la responsabilité, les réponses se dispersent (48 % le demandeur, 14 % l'approbateur), et les règles varient : 42 % les appliquent de façon inégale, 42 % laissent chaque équipe décider. Deux voix encadrent le propos : Harjot Gill (CodeRabbit) pour qui la revue est la dernière barrière, Paul Nashawaty (Efficiently Connected) qui ne ferait pas de l'agent générateur le validateur final. L'article conclut sur trois pratiques : escalader selon le risque (logique de paiement, autorisations, migrations de schéma, contrats d'API partagés vers leurs propriétaires), lier la responsabilité aux registres de défauts, et superposer revue IA, tests automatisés, analyse de sécurité, règles et revue humaine selon le risque de chaque changement.

## 4. Citations et noms
**Citations** :
- « Tout le monde peut passer de l'idée au code, donc la revue est la seule barrière qui reste. » (« Anyone can go from idea to code now, so review is the only gate left. »), Harjot Gill, CodeRabbit
- « Je ne compterais pas sur l'agent qui a généré le code pour en être le validateur final. » (« I wouldn't rely on the same agent that generated the code to be the final validator. »), Paul Nashawaty, Efficiently Connected

**Noms cités** :
- *LeadDev* : média et communauté de responsables d'ingénierie, auteur de l'enquête.
- *CodeRabbit* : éditeur d'outils de revue de code par IA, sponsor de l'enquête.
- *Harjot Gill* : PDG et cofondateur de CodeRabbit.
- *Paul Nashawaty* : analyste principal chez Efficiently Connected, voix extérieure.
- *Défauts échappés* : défauts qui passent en production, métrique suivie par 22 % des répondants.

## 5. Mots-clés
agents IA, vérification, goulot d'étranglement, qualité, gouvernance IA, enquête

## Lecture CPO
- **Implications** :
  - Décider explicitement qui est responsable d'un changement écrit et relu par des agents, et l'écrire dans les règles d'équipe : aujourd'hui, la réponse varie d'une organisation à l'autre.
  - Ne pas confier la validation finale à l'agent qui a produit le code ; séparer générateur et relecteur, et escalader vers un humain selon le risque (paiement, droits, schémas, API partagées).
  - Mesurer la revue (délai, défauts échappés) plutôt que les seuls tokens : les gains de vitesse affichés peuvent cacher un ralentissement en aval.
  - Pour un CPO, la capacité de revue devient une contrainte de planification au même titre que la capacité de développement.
- **Fiabilité** : enquête sponsorisée par un éditeur de revue de code par IA, échantillon de 325 répondants complets, méthode et dates non publiées dans l'article. Les chiffres vont dans le sens de l'intérêt du sponsor (la revue comme goulot), mais rejoignent Thoughtworks et DORA. Une seule voix extérieure.
- **Maturité** : Tendance émergente : le déplacement du goulot vers la revue est largement décrit, mais les pratiques de gouvernance (standards, responsabilité, métriques) restent rares et hétérogènes.
- **Réutilisation** : post LinkedIn « 47 % laissent l'agent relire son propre code, 14 % ont des règles » (en citant le sponsor) ; table ronde sur la responsabilité dans les chaînes d'agents (avec Benachour et Sahni) ; article OCTO sur la revue de code comme nouveau goulot de la livraison.
