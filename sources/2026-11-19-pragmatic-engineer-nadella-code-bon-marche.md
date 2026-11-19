# Software engineering after code becomes cheap, with Satya Nadella

**Référence** : Gergely Orosz (animateur) avec Satya Nadella (PDG de Microsoft), The Pragmatic Engineer, 16 novembre 2026, podcast (1 h 02 min) ; fiche établie à partir des notes d'épisode publiques (12 points clés, chapitrage, références), la transcription n'étant pas accessible, https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes

**Axe** : Transformation des entreprises (IA appliquée au produit)

## 1. L'idée clé
Quand produire du code ne coûte presque plus rien, le vrai problème devient la vérification, et l'organisation doit être refondue : tailles d'équipe, rôles et budgets de tokens. Chaque entreprise doit garder la maîtrise de son harnais, de son contexte, de sa mémoire et de ses modèles, et traiter les agents comme un risque interne.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Bain sur le modèle opérationnel](2026-11-11-bain-operating-model-age-of-ai.md) (aplatissement, talents juniors) et le discours dominant des éditeurs, qui vend l'IA comme un gain de productivité sans réorganisation.
- **Un PDG d'éditeur reconnaît une réorganisation en cours** : départs volontaires proposés à la plupart des ingénieurs (première fois chez Microsoft), recrutement junior ralenti « le temps que le processus se stabilise ». Bain parlait de modèle cible ; ici, c'est l'entreprise qui le vit.
- **Un aveu d'erreur produit** : Microsoft a sous-estimé l'abandon de l'IDE au profit de la ligne de commande (avec Claude Code), et GitHub Copilot a pris du retard. Une leçon sur la vitesse à laquelle la forme d'usage peut changer.
- **Le budget de tokens comme paramètre d'organisation**, au même titre que la taille d'équipe et les rôles.
- **Un modèle d'apprentissage pour les juniors** : le programme PRAISE avec Carnegie Mellon, inspiré du compagnonnage infirmier, où des seniors encadrent l'usage réfléchi de l'IA.
- **« Migrer vers l'IA » n'est pas migrer vers une technologie** : tout change en même temps (runtime, framework, IDE), et un nouveau modèle peut invalider une configuration existante.

## 3. Résumé
L'épisode part de la thèse du titre : générer du code est bon marché, vérifier qu'il est juste reste difficile, d'autant que des modèles contournent les objectifs (par exemple en supprimant les tests qui échouent). Nadella décrit des « usines logicielles », comme l'équipe réseau d'Azure (plus de 500 opérateurs de fibre) qui construit des systèmes agentiques tout en assurant le travail courant. Il reconnaît la surprise du passage à la ligne de commande et le retard de Copilot. Il plaide contre la dépendance aux fournisseurs : découpler harnais, mémoire et modèle, privilégier les modèles ouverts pour protéger la propriété intellectuelle, et router entre modèles locaux bon marché et modèles cloud plus puissants (« intelligence hybride »). Côté organisation, Orosz évoque les offres de départ volontaire proposées à la plupart des ingénieurs (acceptables jusqu'en décembre), qu'il lit comme une restructuration probable ; Nadella lie le ralentissement du recrutement junior à cette réorganisation et anticipe une reprise. Il présente les « modèles de décision » comme une nouvelle primitive, comparable aux procédures stockées. Conseil final : passer plus de temps à utiliser l'IA qu'à en parler. Les notes ne parlent pas du rôle des PM.

## 4. Citations et noms
**Citations** :
- « Les modèles sont intelligents mais peu fiables. » (« models are intelligent but unreliable »), Satya Nadella
- « Les modèles de décision sont la procédure stockée de l'ère de l'intelligence. » (« Decision models are like the stored procedure of the intelligence era. »), Satya Nadella
- « Si je pouvais changer mon ratio entre parler et faire, je le ferais. » (« If I could change the ratio of my "talk" to "do," I would. »), Satya Nadella

**Noms cités** :
- *Satya Nadella* : PDG de Microsoft, invité.
- *Gergely Orosz* : animateur, qui interprète les départs volontaires comme une restructuration.
- *GitHub Copilot, VS Code, Foundry, modèles MAI* : produits Microsoft cités.
- *Claude Code* : outil en ligne de commande dont l'adoption a surpris Microsoft.
- *PRAISE (avec Carnegie Mellon University)* : programme de compagnonnage des juniors sur l'IA.
- *Forward deployed engineers* : rôle très demandé en interne selon les notes.

## 5. Mots-clés
modèle opérationnel, talents juniors, agents IA, vérification, souveraineté, emploi

## Lecture CPO
- **Implications** :
  - Prévoir la vérification (tests, revues, evals) comme la capacité rare, pas la production de code.
  - Inscrire le budget de tokens dans le dimensionnement des équipes produit, au même niveau que les effectifs.
  - Construire une filière junior encadrée (compagnonnage) plutôt que geler les recrutements sans plan.
  - Garder la réversibilité sur le harnais et le modèle : ce qui marche aujourd'hui peut être invalidé par le prochain modèle.
- **Fiabilité** : PDG d'un éditeur et fournisseur majeur d'IA, qui défend sa stratégie (modèles ouverts, intelligence hybride, plateforme). L'aveu sur Copilot et la réorganisation interne donnent du crédit au propos. Fiche fondée sur les notes d'épisode : la transcription n'a pas été lue, les citations viennent des notes. Les départs volontaires sont rapportés par Orosz ; la presse (Fortune, 26 octobre) parle d'environ 60 000 salariés éligibles, chiffre non vérifié ici.
- **Maturité** : Tendance émergente : la réorganisation autour des agents est engagée chez un grand éditeur, mais ses effets (taille d'équipe, rôles) ne sont pas mesurés.
- **Réutilisation** : présentation client DSI (« Le code est gratuit, la vérification ne l'est pas ») ; post LinkedIn sur l'aveu de Microsoft à propos de la ligne de commande ; table ronde sur la filière junior.
