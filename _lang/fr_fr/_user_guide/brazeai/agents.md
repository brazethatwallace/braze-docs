---
nav_title: Console des agents
article_title: "Agents Braze dans la Console des agents"
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

## Pourquoi utiliser les Braze Agents ? {#why-use-braze-agents}

Les Braze Agents aident votre équipe à offrir des expériences plus intelligentes et plus personnalisées, sans travail supplémentaire. Ils agissent comme des agents autonomes qui ne se contentent pas de répondre à des invites, mais qui comprennent le contexte, prennent des décisions et agissent pour atteindre un objectif.

En pratique, les agents peuvent créer automatiquement du contenu de message, comme des lignes d'objet ou du texte intégré au produit, afin que chaque client reçoive une communication qui semble faite sur mesure. Ils peuvent également s'adapter en temps réel, orientant les utilisateurs dans différents parcours Canvas en fonction de leurs préférences, de leurs comportements ou d'autres données.

Au-delà de la communication, les agents peuvent enrichir vos catalogues en calculant ou en générant des valeurs de champs pour les produits et les profils, ce qui permet de garder vos données actualisées et dynamiques. En prenant en charge les tâches répétitives ou complexes, ils permettent à votre équipe de se concentrer sur la stratégie et la créativité plutôt que sur la configuration manuelle. Les Braze Agents fonctionnent davantage comme des collaborateurs que comme des processus en arrière-plan : ils vous aident à résoudre des problèmes et à avoir un impact à grande échelle.

### Quand utiliser les Braze Agents plutôt que d'autres fonctionnalités BrazeAI {#when-to-use-braze-agents-versus-other-brazeai-features}

Utilisez les agents pour personnaliser du contenu à la volée en s'appuyant sur le contexte spécifique d'un utilisateur. Par exemple, si un agent sait que la saveur de glace préférée d'un utilisateur particulier est le chocolat et que son topping favori est les oursons en gélatine, il peut rédiger un texte de notification push spécifique à cette combinaison pour cet utilisateur au moment où il passe par le Canvas.

Cependant, l'agent n'apprend pas par essais et erreurs, et il n'a pas connaissance d'un objectif marketing ultime qu'il chercherait à mesurer et à maximiser. Même si vous lui demandez de rédiger de manière générale du contenu qui favorise les conversions, il ne dispose d'aucun mécanisme pour « surveiller » l'impact de sa rédaction agentique sur les conversions ni pour intégrer ces données dans ses futures invocations. On peut considérer cela comme une prise de décision « intuitive », et non comme une prise de décision basée sur la récompense (AI Decisioning).

En revanche, d'autres outils BrazeAI sont conçus pour maximiser les indicateurs qu'ils mesurent. Par exemple, les agents sont très efficaces pour évaluer qualitativement comment les caractéristiques d'un utilisateur influencent sa probabilité ou sa propension à réaliser un certain événement ou à apprécier un certain produit. Toutefois, comme l'agent n'apprend pas par essais et erreurs, il ne sait pas comment mesurer la précision de ses prédictions de probabilités ni comment améliorer le signal au fil du temps. C'est pourquoi la Predictive Suite surpasse l'étape d'agent lorsqu'on évalue la précision des prédictions et les améliorations dans le temps.

## Fonctionnalités {#features}

Les fonctionnalités des Braze Agents comprennent :

- **Configuration flexible :** utilisez un LLM fourni par Braze ou connectez vos propres [fournisseurs de modèles IA]({{site.baseurl}}/partners/ai_model_providers) (tels qu'OpenAI, Anthropic, Google Gemini ou Databricks Mosaic).
- **Intégration fluide :** déployez des agents directement dans des étapes Canvas ou des champs de catalogue.
- **Tests, journaux et historique des versions :** prévisualisez la sortie de votre agent en le testant avec des entrées d'exemple avant le lancement. Consultez les journaux pour chaque exécution de l'agent, y compris les entrées et sorties de cette exécution. Utilisez l'onglet **Historique des versions** pour passer en revue les versions précédentes et les différences en ligne des modifications d'instructions.
- **Contrôles d'utilisation :** des limites quotidiennes permettent de gérer les performances et les coûts.

## À propos des Braze Agents {#about-braze-agents}

Les agents sont configurés avec des instructions (prompts système) qui définissent leur comportement. Lorsqu'un agent s'exécute, il utilise vos instructions ainsi que toutes les données que vous lui transmettez explicitement pour générer une réponse. Ils ne peuvent pas accéder aux données utilisateur au-delà de ce que vous configurez : variables Liquid, sélections de contexte d'agent, variables de contexte Canvas et valeurs d'étape de contexte. Les agents ne parcourent pas les profils et n'émettent pas d'avertissement lorsque des données sont manquantes. Consultez [Quelles données les agents reçoivent]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

### Concepts clés {#key-concepts}

| Terme | Définition |
| --- | --- |
| [Modèle]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) | Le « cerveau » de l'agent, en l'occurrence un grand modèle de langage (LLM). Il interprète les entrées, génère des réponses et effectue des raisonnements. Un modèle plus puissant (entraîné sur des données plus pertinentes) rend l'agent plus performant et polyvalent. |
| [Instructions]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) | Les règles ou directives que vous donnez à l'agent (prompt système). Elles définissent comment l'agent doit se comporter à chaque exécution. Des instructions claires rendent l'agent plus fiable et prévisible. |
| Contexte | Les données transmises à l'agent au moment de l'exécution, quel que soit l'endroit où il est déployé, comme les champs du profil utilisateur ou les lignes de catalogue. Ces entrées fournissent les informations que l'agent utilise pour générer ses sorties. |
| [Variables de contexte Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#how-context-variables-work) | Des données temporaires que vous pouvez créer et utiliser au sein du parcours d'un utilisateur dans un Canvas spécifique. |
| [Variable de sortie]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#define-the-output-variable) | La sortie produite par l'agent lorsqu'il est utilisé dans les étapes Canvas. Les variables de sortie stockent le résultat de l'agent pour personnaliser le contenu ou orienter les chemins du workflow. Les variables de sortie peuvent être de type chaîne de caractères, nombre ou booléen. |
| [Invocation](#limitations) | Une seule exécution de l'agent. Elle est décomptée de vos limites quotidiennes. |
| [Format de sortie]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#select-output) | La structure de données prédéfinie de la réponse de l'agent. |
| [Sources de connaissances]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) | Un type de contexte d'agent utilisé pour récupérer des données d'un catalogue de manière plus précise que si le catalogue est directement référencé dans les instructions de l'agent. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Concepts clés" }

## Limitations {#limitations}

Les limitations suivantes s'appliquent :

- Chaque agent dispose d'une limite d'invocations quotidiennes par défaut de 250 000 exécutions, qui peut être augmentée jusqu'à un maximum de 1 000 000 d'exécutions par jour. Contactez votre gestionnaire de la satisfaction client si vous souhaitez augmenter cette limite.
- La Console d'agents affiche une **Limite quotidienne de coût en crédits d'action** pour chaque agent, c'est-à-dire le nombre maximal estimé de crédits par jour en fonction du ratio de crédits par invocation de votre modèle et de la limite d'invocations quotidiennes. Consultez [Limites quotidiennes d'invocations et de crédits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).
- Par défaut, chaque exécution doit se terminer dans un délai de 20 secondes. Au-delà de 20 secondes, l'agent renvoie une réponse `null` là où il est utilisé.
    - Si vos agents dépassent régulièrement le délai, contactez votre gestionnaire de compte Braze pour augmenter cette limite.
- Les données d'entrée sont limitées à 25 Ko par requête. Les entrées plus longues sont tronquées.

## Bonnes pratiques {#best-practices}

Ciblez des cas d'usage à forte valeur ajoutée pour lesquels les agents peuvent générer le meilleur retour sur investissement (ROI), et choisissez des audiences susceptibles de répondre. Une audience plus restreinte mais à fort potentiel surpasse souvent une audience large avec un faible potentiel — par exemple, recibler les utilisateurs qui ont effectué une recherche récemment mais n'ont pas converti, plutôt que d'envoyer du contenu généré par un agent à l'ensemble de votre base d'utilisateurs.

Pour valider le ROI avant de passer à l'échelle, utilisez une étape [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) pour n'envoyer qu'une partie de votre audience dans une étape d'agent. Lorsqu'un test à petite échelle donne de bons résultats, déployez l'agent sur l'ensemble de votre audience cible et augmentez la [limite d'invocations quotidiennes]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits) afin que les invocations ne soient pas plafonnées en cours d'envoi. Assurez-vous que la consommation de crédits estimée vous convient avant de passer à l'ensemble de votre audience. Pour plus de conseils de déploiement, consultez [Déployer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

## Gestion des erreurs {#error-handling}

Si le modèle connecté renvoie une [erreur de limite de débit]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) du fournisseur LLM lors d'une invocation d'agent d'étape Canvas ou d'agent de catalogue, Braze relance continuellement la requête en utilisant des délais exponentiels.

Pour les autres types d'échec (tels qu'un délai d'attente dépassé ou une clé API invalide), la sortie de l'agent d'étape Canvas est définie sur `null`, sauf si l'agent possède des [valeurs de repli configurées]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) dans la Console d'agents (agents d'étape Canvas uniquement). Les agents de catalogue ne relancent pas les échecs autres que ceux liés aux limites de débit. Si un agent atteint sa limite d'invocations quotidiennes, Braze applique les valeurs de repli configurées lorsqu'elles sont présentes ; dans le cas contraire, la sortie est définie sur `null`.

Les erreurs de limite de débit, l'indisponibilité du modèle et les échecs liés à la limite d'invocations quotidiennes ne consomment pas de crédits Braze. Les dépassements de délai consomment des crédits. Consultez [Quand les crédits sont consommés]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).

Lorsque de nombreux utilisateurs entrent simultanément dans une étape d'agent, le traitement peut prendre plus de temps en raison des [contrôles de flux d'invocation]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls). Configurez des valeurs de repli dans la Console d'agents pour les agents d'étape Canvas afin que les utilisateurs reçoivent tout de même une sortie en cas d'échec d'invocation, ou utilisez des [valeurs Liquid par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) dans les étapes de message en aval.

## Comment mes données sont-elles utilisées et envoyées aux LLM fournis par Braze ? {#how-is-my-data-used-and-sent-to-braze-provided-llms}

Afin de générer des résultats d'IA via les fonctionnalités d'IA de Braze que Braze identifie comme exploitant des LLM fournis par Braze (les « résultats »), Braze enverra votre prompt système ou toute autre entrée, le cas échéant (les « entrées »), au LLM fourni par Braze. Les données envoyées au LLM fourni par Braze concerné ne sont pas utilisées pour entraîner ni améliorer le LLM fourni par Braze. Entre vous et Braze, les résultats constituent votre propriété intellectuelle. Braze ne revendiquera aucun droit d'auteur sur ces résultats. Braze ne fournit aucune garantie d'aucune sorte concernant le contenu généré par l'IA en général, y compris les résultats.

Le LLM fourni par Braze pour les Braze Agents, identifié comme « Auto », utilise les modèles Google Gemini. Google conserve les entrées et les résultats soumis via Braze pendant 55 jours, après quoi les données sont supprimées.

## Étapes suivantes {#next-steps}

Maintenant que vous connaissez les agents Braze, vous êtes prêt pour les étapes suivantes :

{% article_tiles %}
- name: Créer des agents personnalisés
  link: /docs/user_guide/brazeai/agents/creating_agents
- name: Déployer des agents personnalisés
  link: /docs/user_guide/brazeai/agents/deploying_agents
{% endarticle_tiles %}