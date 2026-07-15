---
nav_title: Console des agents
article_title: Agents Braze
page_order: 1
description: "Les agents Braze peuvent générer du contenu, prendre des décisions intelligentes et enrichir vos données afin que vous puissiez offrir des expériences client plus personnalisées."
---

# Agents Braze dans la Console des agents {#braze-agents-in-agent-console}

> Les agents Braze sont des assistants alimentés par l'intelligence artificielle que vous pouvez créer dans Braze. Ils peuvent générer du contenu, prendre des décisions intelligentes et enrichir vos données pour vous permettre d'offrir des expériences client plus personnalisées.

{% alert important %}
Des crédits de message ou d'action sont nécessaires pour accéder aux agents Braze et les utiliser. Si vous ne disposez pas actuellement de crédits d'action et souhaitez utiliser les agents Braze, contactez votre gestionnaire de compte pour connaître la marche à suivre.
{% endalert %}

Regardez cette vidéo pour un aperçu des agents Braze dans la Console des agents.

{% multi_lang_include video.html id="afd0hp0vrh" source="wistia" title="Braze Agents in Agent Console overview" %}

## Pourquoi utiliser les agents Braze ? {#why-use-braze-agents}

Les agents Braze aident votre équipe à proposer des expériences plus intelligentes et personnalisées, sans travail supplémentaire. Ils agissent comme des agents autonomes qui ne se contentent pas de répondre à des invites : ils comprennent le contexte, prennent des décisions et agissent pour atteindre un objectif.

En pratique, les agents peuvent générer automatiquement des messages — comme des lignes d'objet ou du texte intégré au produit — afin que chaque client reçoive une communication qui semble faite sur mesure. Ils peuvent également s'adapter en temps réel, en orientant les utilisateurs vers différents parcours Canvas en fonction de leurs préférences, comportements ou autres données.

Au-delà de l'envoi de messages, les agents peuvent enrichir vos catalogues en calculant ou en générant des valeurs de champs pour les produits et les profils, ce qui permet de maintenir vos données à jour et dynamiques. En prenant en charge les tâches répétitives ou complexes, ils permettent à votre équipe de se concentrer sur la stratégie et la créativité plutôt que sur la configuration manuelle. Les agents Braze fonctionnent davantage comme des collaborateurs que comme des processus en arrière-plan : ils vous aident à résoudre des problèmes et à avoir un impact à grande échelle.

### Quand utiliser les agents Braze plutôt que d'autres fonctionnalités BrazeAI {#when-to-use-braze-agents-versus-other-brazeai-features}

Utilisez les agents pour personnaliser du contenu à la volée en fonction du contexte spécifique d'un utilisateur. Par exemple, si un agent sait que le parfum de glace préféré d'un utilisateur est le chocolat et que sa garniture préférée est les oursons en gélatine, il peut rédiger un message push spécifique à cette combinaison pour cet utilisateur lorsqu'il passe par le Canvas.

Cependant, l'agent n'apprend pas par essais et erreurs et n'a aucune notion d'un objectif marketing ultime qu'il chercherait à mesurer et à maximiser. Même si vous lui demandez de rédiger des textes qui favorisent les conversions, il ne dispose d'aucun mécanisme pour « surveiller » l'impact de ses textes sur les conversions et intégrer ces données dans ses futures exécutions. Considérez cela comme une prise de décision basée sur l'« intuition », et non comme une décision automatisée par IA basée sur la récompense.

En revanche, les autres outils BrazeAI sont conçus pour optimiser les indicateurs qu'ils mesurent. Par exemple, les agents sont très compétents pour évaluer qualitativement comment les caractéristiques d'un utilisateur influencent sa probabilité ou sa propension à réaliser une certaine action ou à apprécier un certain produit. Cependant, comme l'agent n'apprend pas par essais et erreurs, il ne sait pas comment mesurer la précision de ses prédictions ni améliorer le signal au fil du temps. C'est pourquoi la Predictive Suite surpasse l'étape Agent lorsqu'on évalue la précision des prédictions et les améliorations dans la durée.

## Fonctionnalités {#features}

Les fonctionnalités des agents Braze comprennent :

- **Configuration flexible :** Utilisez un LLM fourni par Braze ou connectez vos propres [fournisseurs de modèles d'IA]({{site.baseurl}}/partners/ai_model_providers) (tels qu'OpenAI, Anthropic, Google Gemini ou Databricks Mosaic).
- **Intégration fluide :** Déployez les agents directement dans les étapes Canvas ou les champs du catalogue.
- **Tests, journalisation et historique des versions :** Prévisualisez les résultats de votre agent en effectuant des tests avec des exemples d'entrées avant le lancement. Consultez les journaux de chaque exécution de l'agent, y compris les entrées et sorties correspondantes. Utilisez l'onglet **Historique des versions** pour consulter les versions précédentes et les différences en ligne des modifications d'instructions.
- **Contrôles d'utilisation :** Les limites quotidiennes facilitent la gestion des performances et des coûts.

## À propos des agents Braze {#about-braze-agents}

Les agents sont configurés avec des instructions (invites système) qui définissent leur comportement. Lorsqu'un agent s'exécute, il utilise vos instructions ainsi que toutes les données que vous lui transmettez explicitement pour générer une réponse. Ils ne peuvent pas accéder aux données utilisateur au-delà de ce que vous configurez — variables Liquid, sélections de contexte de l'agent, variables de contexte Canvas et valeurs de l'étape Contexte. Les agents ne parcourent pas les profils et n'émettent pas d'avertissement lorsque des données sont manquantes. Consultez [Données reçues par les agents]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

### Concepts clés {#key-concepts}

| Terme | Définition |
| --- | --- |
| [Modèle]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) | Le « cerveau » de l'agent, en l'occurrence un grand modèle de langage (LLM). Il interprète les entrées, génère des réponses et effectue des raisonnements. Un modèle plus performant (entraîné sur des données plus pertinentes) rend l'agent plus efficace et polyvalent. |
| [Instructions]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) | Les règles ou directives que vous fournissez à l'agent (invite système). Elles définissent comment l'agent doit se comporter à chaque exécution. Des instructions claires rendent l'agent plus fiable et prévisible. |
| Contexte | Données transmises à l'agent lors de l'exécution, quel que soit son lieu de déploiement, telles que les champs du profil utilisateur ou les lignes du catalogue. Ces entrées fournissent les informations que l'agent utilise pour générer ses sorties. |
| [Variables de contexte Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#how-context-variables-work) | Données temporaires que vous pouvez créer et utiliser dans le parcours d'un utilisateur au sein d'un Canvas spécifique. |
| [Variable de sortie]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#define-the-output-variable) | Le résultat généré par l'agent lorsqu'il est utilisé dans les étapes Canvas. Les variables de sortie enregistrent le résultat de l'agent afin de personnaliser le contenu ou de guider les parcours du workflow. Les variables de sortie peuvent être de type chaîne de caractères, nombre ou valeur booléenne. |
| [Invocation](#limitations) | Une seule exécution de l'agent. Celle-ci est décomptée de vos limites quotidiennes. |
| [Format de sortie]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#select-output) | La structure de données prédéfinie de la réponse de l'agent. |
| [Sources de connaissances]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) | Un type de contexte d'agent utilisé pour récupérer des données d'un catalogue de manière plus précise que si le catalogue est référencé directement dans les instructions de l'agent. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Concepts clés" }

## Restrictions {#limitations}

Les restrictions suivantes s'appliquent :

- Chaque agent dispose d'une limite d'invocation quotidienne par défaut de 250 000 exécutions, qui peut être augmentée jusqu'à un maximum de 1 000 000 exécutions par jour. Contactez votre gestionnaire du succès des clients si vous souhaitez augmenter cette limite.
- La Console des agents affiche une **Limite quotidienne de coût en crédits d'action** pour chaque agent — le nombre maximal estimé de crédits par jour en fonction du ratio de crédits par invocation de votre modèle et de la limite d'invocation quotidienne. Consultez [Limites quotidiennes d'invocation et de crédits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).
- Par défaut, chaque exécution doit se terminer dans un délai de 20 secondes. Passé ce délai, l'agent renvoie une réponse `null` là où il est utilisé.
    - Si vos agents dépassent régulièrement le délai imparti, contactez votre gestionnaire de compte Braze pour augmenter cette limite.
- Les données d'entrée sont limitées à 25 Ko par requête. Les entrées plus longues sont tronquées.

## Bonnes pratiques {#best-practices}

Ciblez les cas d'usage à forte valeur ajoutée où les agents peuvent générer le meilleur retour sur investissement (ROI), et choisissez des audiences susceptibles de répondre. Une audience plus restreinte mais à fort potentiel surpasse souvent une audience large avec peu d'opportunités — par exemple, recibler les utilisateurs qui ont effectué une recherche récemment mais n'ont pas converti, plutôt que d'envoyer du contenu généré par un agent à l'ensemble de votre base d'utilisateurs.

Pour valider le ROI avant de passer à l'échelle, utilisez une étape [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) pour n'envoyer qu'une partie de votre audience à travers une étape Agent. Pour plus de conseils sur le déploiement, consultez [Déployer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

## Gestion des erreurs {#error-handling}

Si le modèle connecté renvoie une [erreur de limite de débit]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) du fournisseur de LLM lors d'une invocation d'**étape Agent dans Canvas** ou d'**agent de catalogue**, Braze relance la requête en continu en utilisant des délais exponentiels. Pour les autres types d'échecs (comme un dépassement de délai ou une clé API invalide), la sortie de l'agent Canvas est définie sur `null`, sauf si l'agent dispose de [valeurs de repli configurées]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) dans la Console des agents (étapes Agent dans Canvas uniquement). Les agents de catalogue ne relancent pas les échecs autres que les erreurs de limite de débit. Si un agent atteint sa limite d'invocation quotidienne, Braze applique les valeurs de repli configurées lorsqu'elles sont présentes ; sinon, la sortie est définie sur `null`.

Lorsque de nombreux utilisateurs entrent simultanément dans une étape Agent, le traitement peut prendre plus de temps en raison des [contrôles de flux d'invocation]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls). Configurez des valeurs de repli dans la Console des agents pour les agents Canvas afin que les utilisateurs reçoivent toujours un résultat en cas d'échec d'une invocation, ou utilisez les [valeurs Liquid par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) dans les étapes Message en aval.

## Comment mes données sont-elles utilisées et transmises aux LLM fournis par Braze ? {#how-is-my-data-used-and-sent-to-braze-provided-llms}

Afin de générer des résultats d'IA via les fonctionnalités d'IA de Braze identifiées comme exploitant les LLM fournis par Braze (« Résultats »), Braze enverra votre invite système ou toute autre entrée, selon le cas (« Entrée »), au LLM fourni par Braze. Les données transmises au LLM fourni par Braze ne sont pas utilisées pour entraîner ou améliorer ledit modèle. Entre vous et Braze, les Résultats constituent votre propriété intellectuelle. Braze ne fera valoir aucun droit d'auteur sur ces Résultats. Braze n'offre aucune garantie de quelque nature que ce soit concernant tout contenu généré par l'IA en général, y compris les Résultats.

Le LLM fourni par Braze pour les agents Braze, identifié comme « Auto », utilise les modèles Google Gemini. Google conserve les Entrées et Résultats soumis via Braze pendant 55 jours, après quoi les données sont supprimées.

## Étapes suivantes {#next-steps}

Maintenant que vous connaissez les agents Braze, vous êtes prêt pour la suite :

- [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Déployer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)