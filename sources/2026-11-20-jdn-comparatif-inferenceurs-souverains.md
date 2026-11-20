# OVH, Scaleway, Mistral... Comparatif des inférenceurs souverains d'IA

**Référence** : Benjamin Polge, Journal du Net, 20 novembre 2026, article comparatif (tableaux de fonctionnalités et de prix par million de tokens), https://www.journaldunet.com/cloud/1558123-ovh-scaleway-mistral-comparatif-des-inferenceurs-souverains-d-ia/

**Axe** : Investissement tech (IA appliquée au produit)

## 1. L'idée clé
Il n'y a pas d'inférenceur souverain qui gagne sur tout : OVHcloud est le moins cher sur cinq des six modèles partagés, Cloud Temple est le seul qualifié SecNumCloud mais systématiquement le plus cher, Scaleway se distingue par son catalogue et son cache, et Mistral est le moins cher sur ses propres modèles mais le moins souverain des quatre. Le choix dépend du cas d'usage.

## 2. Ce qui est nouveau
**Par rapport à** : la fiche [Thoughtworks Radar vol. 35](2026-11-19-thoughtworks-radar-vol35.md) (le choix du modèle devient une décision de coût et de souveraineté) et la fiche [Cebr / Wasabi](2026-11-19-cebr-wasabi-depassements-infrastructure-ia.md) (l'infrastructure IA fait déraper les budgets des DSI français).
- **Des prix comparés, pas des principes** : le Radar disait d'arbitrer par cas d'usage ; le JDN donne les prix par million de tokens chez quatre acteurs français, par exemple gpt-oss 120B à 0,08 € en entrée chez OVH contre 1,80 € chez Cloud Temple.
- **Des écarts de prix très importants pour le même modèle** : jusqu'à 22 fois plus cher chez Cloud Temple qu'OVH sur gpt-oss 120B, à cause d'un tarif unique qui pénalise les petits modèles. Le coût de la souveraineté maximale se chiffre.
- **Le prompt caching comme critère FinOps** : seuls Scaleway (trois modèles, cache 80 % moins cher que l'entrée) et Mistral (tout le catalogue) le proposent. Pour les prompts répétitifs, ce critère peut peser plus que le prix catalogue.
- **La souveraineté n'est pas binaire** : Mistral ne garantit ni le zéro rétention par défaut, ni HDS, ni SLA sur l'offre standard ; seul Cloud Temple est SecNumCloud.

## 3. Résumé
L'article compare quatre offres d'inférence françaises : Scaleway (Generative APIs), OVHcloud (AI Endpoints), Cloud Temple (LLMaaS) et Mistral AI (La Plateforme). Il commence par les catalogues : Scaleway couvre le plus de familles (Mistral open-weight, Llama, Qwen, gpt-oss, Gemma, DeepSeek, GLM), OVH n'a ni Gemma ni DeepSeek ni GLM, Mistral héberge ses propres modèles plus DeepSeek et GLM ; l'auteur note que GLM et Qwen plaisent aux DSI pour leur rapport qualité-prix. Il passe ensuite aux garanties : tous ont une API batch ; seul Mistral n'applique pas le zéro rétention par défaut (sur demande au support) et, sur son offre gratuite, peut utiliser les données pour l'entraînement ; seul Cloud Temple est SecNumCloud ; Mistral n'a ni HDS ni SLA standard. Viennent les prix en euros HT par million de tokens (Mistral converti depuis le dollar au taux de 0,85) : OVH est le moins cher sur cinq des six modèles partagés, Cloud Temple le plus cher partout, Scaleway en milieu de gamme, Mistral le moins cher sur ses modèles (DeepSeek V4.1 Flash à 0,255 € en entrée contre 0,60 € chez Scaleway). L'article conclut par des recommandations : Cloud Temple pour les garanties maximales (santé, SecNumCloud), OVH pour le prix avec un modèle chinois, Scaleway ou Mistral pour les prompts répétitifs, Mistral pour ses derniers modèles au meilleur prix.

## 4. Citations et noms
**Citations** :
- « Sur le papier, OVH est le cloud provider qui propose les prix les plus bas. », Benjamin Polge

**Noms cités** :
- *Scaleway, OVHcloud, Cloud Temple, Mistral AI* : les quatre fournisseurs d'inférence comparés.
- *Mistral Small 3.2, Llama 3.3 70B, gpt-oss 120B, Qwen3.8 27B, DeepSeek V4.1 Flash, GLM 5.3* : modèles utilisés pour comparer les prix.
- *SecNumCloud, HDS* : qualification de l'ANSSI et certification d'hébergement de données de santé, utilisées comme critères de garantie.

## 5. Mots-clés
coûts des tokens, souveraineté, FinOps, infrastructure IA, build vs buy

## Lecture CPO
- **Implications** :
  - Pour un produit IA en production, comparer le coût par cas d'usage (prompts répétitifs ou non, taille du modèle) plutôt que par fournisseur : le cache peut changer l'ordre du classement.
  - Réserver l'offre SecNumCloud aux données qui l'exigent : appliquée à tout, elle peut multiplier la facture par plus de dix.
  - Prévoir la portabilité entre inférenceurs (même modèle ouvert chez plusieurs fournisseurs) pour garder une capacité de renégociation.
  - Vérifier les conditions de rétention et d'entraînement avant de qualifier un fournisseur de souverain.
- **Fiabilité** : article de rédaction, sans intérêt commercial apparent, fondé sur les grilles tarifaires publiques à la date de publication. Prix susceptibles de changer vite. Les tableaux ont été lus dans une version aplatie : l'alignement de certaines colonnes de prix est à revérifier sur la page avant citation. Aucun test de performance ou de latence.
- **Maturité** : Tendance émergente : l'offre d'inférence souveraine existe chez quatre acteurs, mais les catalogues et les garanties restent hétérogènes et les prix instables.
- **Réutilisation** : présentation client DSI ou FinOps (tableau « garanties contre prix ») ; article OCTO sur le coût réel de la souveraineté en IA ; table ronde souveraineté.
