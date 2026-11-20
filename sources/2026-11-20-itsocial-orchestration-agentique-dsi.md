# Outils d'orchestration agentique, la DSI entre projets ouverts et consoles propriétaires d'éditeurs

**Référence** : Mourad Krim, IT Social, 20 novembre 2026, article d'analyse, https://itsocial.fr/intelligence-artificielle/intelligence-artificielle-articles/outils-dorchestration-agentique-la-dsi-entre-projets-ouverts-et-consoles-proprietaires-dediteurs/

**Axe** : IA appliquée au produit (Transformation des entreprises)

## 1. L'idée clé
L'encadrement des agents d'IA se structure en une pile de couches séparables : bac à sable d'exécution, protocole d'échange (MCP), identité et plan de contrôle. Les couches basses ont des options ouvertes (Eclipse Enclave, MCP), les couches hautes restent aux mains des éditeurs (Microsoft, CrowdStrike, SAP). La DSI choisit donc son degré de dépendance couche par couche.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Thoughtworks Radar vol. 35](2026-11-19-thoughtworks-radar-vol35.md) (bac à sable d'agents en « Adopt », harnais agentique), la fiche [Deloitte State of AI in the Enterprise](2026-11-13-deloitte-state-of-ai-enterprise-2026.md) (gouvernance des agents) et le discours dominant qui traite la gouvernance des agents comme une affaire de politique et de chartes.
- **Une lecture en couches de la pile agentique** : l'article sépare bac à sable, protocole, identité et plan de contrôle, et montre que l'ouvert s'arrête aux couches basses. C'est une grille de décision pour la DSI, plus concrète que les cadres de gouvernance génériques.
- **Une option libre pour le bac à sable** : Eclipse Enclave 1.0 (licence MIT, conteneurs Docker éphémères, filtrage du trafic sortant par liste blanche) face à Docker Sandboxes ; ce que le Radar recommande devient un outil disponible.
- **La gouvernance liée à la licence** : Microsoft Agent 365 et l'identité Entra pour agents, CrowdStrike Falcon Guardian, SAP rattachent le contrôle des agents à leur écosystème. Le verrouillage se déplace du modèle vers la console.
- **De la règle au confinement** : une politique écrite ne suffit pas, seul un contrôle au point d'exécution empêche l'agent d'agir ; Deloitte ne trouve que 9 % d'entreprises multi-agents s'estimant entièrement gouvernées.

## 3. Résumé
L'article part du lancement, le 19 novembre à Bruxelles, d'Eclipse Enclave 1.0 par la Fondation Eclipse, pour montrer que les agents sont désormais encadrés par une pile d'outils. Première couche, le bac à sable : Enclave, développé par EclipseSource puis cédé à la fondation, fait tourner Claude Code, Codex, OpenCode, Theia AI ou Pi dans des conteneurs éphémères avec filtrage du DNS et du trafic sortant ; Docker Sandboxes, gratuit et isolé par microVM depuis janvier 2026, occupe le même terrain. L'auteur note qu'Enclave est jeune et ne revendique aucune conformité au CRA ni à l'AI Act. Deuxième couche, le protocole : Anthropic a confié MCP en décembre 2025 à l'Agentic AI Foundation de la Linux Foundation (avec goose de Block et AGENTS.md d'OpenAI), qui revendique plus de 300 membres ; mais le contrôle des échanges reste aux éditeurs, comme le montre le pare-feu MCP intégré à Entra présenté par Microsoft le 17 novembre. Troisième couche, identité et plan de contrôle : Microsoft Agent 365 (disponible depuis mai 2026, avec identité Entra pour les agents locaux et score de risque en préversion), CrowdStrike (fournisseur d'identité pour agents, Falcon Guardian) et SAP (contrôle intégré à ses agents) s'appuient sur l'annuaire existant mais lient la gouvernance à leur écosystème. L'article passe ensuite de la règle au confinement, en s'appuyant sur Deloitte (contrôles au point d'exécution, 9 % d'entreprises entièrement gouvernées) et sur un rapport de 451 Research cité par la fondation. Il conclut qu'une entreprise peut combiner un bac à sable libre, une norme commune et la console de son fournisseur d'identité, en listant les limites de chaque option.

## 4. Citations et noms
**Citations** :
- Les agents ne doivent pas se voir « accorder un accès illimité à nos machines de développement », Philip Langer (co-responsable d'Enclave, PDG d'EclipseSource)
- L'enjeu est de permettre aux développeurs et aux organisations « de garder le contrôle », Mike Milinkovich (directeur exécutif de la Fondation Eclipse)

**Noms cités** :
- *Fondation Eclipse, EclipseSource, Eclipse Enclave* : le projet libre de bac à sable qui sert de point de départ.
- *Philip Langer, Mike Milinkovich* : porte-parole d'Enclave et de la fondation.
- *Docker Sandboxes* : alternative gratuite mais mono-éditeur pour l'isolation des agents.
- *MCP, Agentic AI Foundation (Linux Foundation), goose (Block), AGENTS.md (OpenAI)* : la couche de normes communes.
- *Microsoft (Agent 365, Entra)* : console de gouvernance et identité des agents, pare-feu MCP en préversion.
- *CrowdStrike (Falcon Guardian), SAP* : autres éditeurs qui intègrent le contrôle des agents à leur offre.
- *Deloitte, 451 Research* : études citées sur la gouvernance et l'isolation des agents.
- *CRA, AI Act* : réglementations européennes auxquelles Enclave ne revendique pas de conformité.

## 5. Mots-clés
agents IA, gouvernance IA, bac à sable, dépendance fournisseur, harnais agentique

## Lecture CPO
- **Implications** :
  - Pour la DSI, cartographier la pile agentique couche par couche et décider explicitement où accepter la dépendance à un éditeur (le plan de contrôle) et où rester ouvert (bac à sable, protocole).
  - Pour les équipes produit qui laissent des agents de code agir sur leurs postes, exiger un bac à sable avec filtrage réseau plutôt qu'une simple charte d'usage.
  - Le choix de la console de gouvernance des agents engage autant que celui du modèle : à traiter comme un arbitrage de portefeuille, pas comme un achat de sécurité.
- **Fiabilité** : média IT spécialisé, sans intérêt commercial apparent ; article factuel fondé sur des annonces d'éditeurs et de fondations, avec leurs limites signalées (jeunesse d'Enclave, préversions Microsoft). Le chiffre Deloitte est sourcé ; le rapport 451 Research est cité de seconde main via la fondation.
- **Maturité** : Tendance émergente : les briques existent mais beaucoup sont en version 1.0 ou en préversion, et la pile n'est pas stabilisée.
- **Réutilisation** : présentation client DSI sur l'architecture de gouvernance des agents (schéma en couches, ouvert ou éditeur) ; table ronde sur la souveraineté et la dépendance dans l'agentique ; article OCTO avec le Radar Thoughtworks sur le bac à sable comme prérequis.
