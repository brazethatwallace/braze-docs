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

Les Braze Agents aident votre équipe à offrir des expériences plus intelligentes et plus personnalisées, sans ajouter de travail supplémentaire. Ils agissent comme des agents autonomes qui ne se contentent pas de répondre à des invites, mais qui comprennent le contexte, prennent des décisions et agissent pour atteindre un objectif.

En pratique, les agents peuvent créer automatiquement du contenu de message — comme des lignes d'objet ou du texte intégré au produit — afin que chaque client reçoive une communication qui lui semble personnalisée. Ils peuvent également s'adapter en temps réel, orientant les utilisateurs à travers différents chemins Canvas en fonction de leurs préférences, de leurs comportements ou d'autres données.

Au-delà de la communication, les agents peuvent enrichir vos catalogues en calculant ou en générant des valeurs de champs de produits et de profils, afin de maintenir vos données à jour et dynamiques. En prenant en charge les tâches répétitives ou complexes, ils permettent à votre équipe de se concentrer sur la stratégie et la créativité plutôt que sur la configuration manuelle. Les Braze Agents se comportent davantage comme des collaborateurs que comme des processus en arrière-plan — ils vous aident à résoudre des problèmes et à générer de l'impact à grande échelle.

### Quand utiliser les Braze Agents plutôt que d'autres fonctionnalités BrazeAI {#when-to-use-braze-agents-versus-other-brazeai-features}

Utilisez les agents pour personnaliser le contenu à la volée en exploitant le contexte spécifique d'un utilisateur. Par exemple, si un agent sait que le parfum de glace préféré d'un utilisateur est le chocolat et que sa garniture favorite est les oursons en gélatine, il peut rédiger un texte de notification push spécifique à cette combinaison pour cet utilisateur lorsqu'il passe dans le Canvas.

Cependant, l'agent n'apprend pas par essais et erreurs, et il n'a aucune notion d'un objectif marketing ultime qu'il cherche à mesurer et à maximiser. Même si vous lui indiquez de rédiger de manière générale du contenu qui génère des conversions, il ne dispose d'aucun mécanisme pour « surveiller » l'impact de sa rédaction sur les conversions et intégrer ces données dans ses futurs appels. Vous pouvez considérer cela comme une prise de décision « intuitive », et non comme une prise de décision IA basée sur la récompense.

En revanche, d'autres outils BrazeAI sont conçus pour maximiser les indicateurs qu'ils mesurent. Par exemple, les agents sont très performants pour évaluer qualitativement comment les caractéristiques d'un utilisateur influencent sa probabilité ou sa propension à effectuer un certain événement ou à apprécier un certain produit. Cependant, comme l'agent n'apprend pas par essais et erreurs, il n'a aucun moyen de mesurer la précision de ses prédictions de probabilité ni d'améliorer le signal au fil du temps. Par conséquent, l'utilisation de Predictive Suite surpasse l'étape d'agent lorsqu'elle est évaluée sur la précision de ses prédictions et ses améliorations dans le temps.

## Fonctionnalités {#features}

Les fonctionnalités des Braze Agents comprennent :

- **Configuration flexible :** utilisez un LLM fourni par Braze ou connectez vos propres [fournisseurs de modèles d'IA]({{site.baseurl}}/partners/ai_model_providers) (tels qu'OpenAI, Anthropic, Google Gemini ou Databricks Mosaic).
- **Intégration transparente :** déployez des agents directement dans des étapes Canvas ou des champs de catalogue.
- **Tests, journalisation et historique des versions :** prévisualisez la sortie de votre agent en effectuant des tests avec des entrées d'exemple avant le lancement. Consultez les journaux pour chaque exécution de l'agent, y compris l'entrée et la sortie de cette exécution. Utilisez l'onglet **Historique des versions** pour examiner les versions précédentes et les différences en ligne des modifications d'instructions.
- **Contrôles d'utilisation :** les limites quotidiennes aident à gérer les performances et les coûts.

## À propos des agents Braze {#about-braze-agents}

Les agents sont configurés avec des instructions (invites système) qui définissent leur comportement. Lorsqu'un agent s'exécute, il utilise vos instructions ainsi que toutes les données que vous lui transmettez explicitement pour générer une réponse. Les agents ne peuvent pas accéder aux données utilisateur au-delà de ce que vous configurez : variables Liquid, sélections de contexte d'agent, variables de contexte Canvas et valeurs d'étape de contexte. Les agents ne recherchent pas dans les profils et n'avertissent pas lorsque des données sont manquantes. Consultez [Quelles données les agents reçoivent]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

### Concepts clés {#key-concepts}

| Terme | Définition |
| --- | --- |
| [Modèle]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) | Le « cerveau » de l'agent, en l'occurrence un grand modèle de langage (LLM). Il interprète les entrées, génère des réponses et effectue du raisonnement. Un modèle plus puissant (entraîné sur des données plus pertinentes) rend l'agent plus performant et polyvalent. |
| [Instructions]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) | Les règles ou directives que vous donnez à l'agent (invite système). Elles définissent le comportement que l'agent doit adopter à chaque exécution. Des instructions claires rendent l'agent plus fiable et prévisible. |
| Contexte | Les données transmises à l'agent au moment de l'exécution, quel que soit l'endroit où il est déployé, comme les champs de profil utilisateur ou les lignes de catalogue. Ces entrées fournissent les informations que l'agent utilise pour générer ses sorties. |
| [Variables de contexte Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#how-context-variables-work) | Des éléments de données temporaires que vous pouvez créer et utiliser tout au long du parcours d'un utilisateur dans un Canvas spécifique. |
| [Variable de sortie]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#define-the-output-variable) | La sortie que l'agent produit lorsqu'il est utilisé dans des étapes Canvas. Les variables de sortie stockent le résultat de l'agent pour personnaliser le contenu ou orienter les chemins de workflow. Les variables de sortie peuvent être de type chaîne de caractères, nombre ou booléen. |
| [Invocation](#limitations) | Une seule exécution de l'agent. Elle est décomptée de vos limites quotidiennes. |
| [Format de sortie]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#select-output) | La structure de données prédéfinie de la réponse de l'agent. |
| [Sources de connaissances]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) | Un type de contexte d'agent utilisé pour récupérer des données d'un catalogue de manière plus précise que si le catalogue est directement référencé dans les instructions de l'agent. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Concepts clés" }

## Limitations {#limitations}

Les limitations suivantes s'appliquent :

- Chaque agent dispose d'une limite quotidienne d'invocations par défaut de 250 000 exécutions, qui peut être augmentée jusqu'à un maximum de 1 000 000 d'exécutions par jour. Contactez votre gestionnaire du succès des clients si vous souhaitez augmenter cette limite.
- La Console d'agents affiche une **limite quotidienne de coût en crédits d'action** pour chaque agent, c'est-à-dire le nombre maximum estimé de crédits par jour en fonction du ratio de crédits par invocation de votre modèle et de la limite quotidienne d'invocations. Consultez [Limites quotidiennes d'invocations et de crédits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).
- Par défaut, chaque exécution doit se terminer en 20 secondes. Au-delà de 20 secondes, l'agent renvoie une réponse `null` là où il est utilisé.
    - Si vos agents expirent régulièrement, contactez votre gestionnaire de compte Braze pour augmenter cette limite.
- Les données d'entrée sont limitées à 25 Ko par requête. Les entrées plus longues sont tronquées.

## Bonnes pratiques {#best-practices}

Ciblez les cas d'usage à forte valeur ajoutée où les agents peuvent générer le meilleur retour sur investissement (ROI), et choisissez des audiences susceptibles de répondre. Une audience plus restreinte mais à fort potentiel surpasse souvent une audience large avec peu d'opportunités — par exemple, recibler les utilisateurs qui ont effectué une recherche récemment mais n'ont pas converti, plutôt que d'envoyer du contenu généré par un agent à l'ensemble de votre base d'utilisateurs.

Pour valider le ROI avant de passer à l'échelle, utilisez une étape [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) afin de n'envoyer qu'une partie de votre audience à travers une étape d'agent. Lorsqu'un test à petite échelle donne de bons résultats, étendez l'agent à l'ensemble de votre audience cible et augmentez la [limite quotidienne d'invocations]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits) afin que les invocations ne soient pas plafonnées en cours d'envoi. Assurez-vous que la consommation de crédits estimée vous convient avant de passer à l'échelle sur l'ensemble de votre audience. Pour plus de conseils de déploiement, consultez [Déployer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

## Gestion des erreurs {#error-handling}

Si le modèle connecté renvoie une [erreur de limitation de débit]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) du fournisseur LLM lors d'une invocation d'agent d'étape Canvas ou d'agent de catalogue, Braze réessaie continuellement la requête en utilisant des délais exponentiels.

Pour les autres échecs (tels qu'un délai d'attente dépassé ou une clé API invalide), la sortie de l'agent d'étape Canvas est définie sur `null`, sauf si l'agent dispose de [valeurs de repli configurées]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) dans la Console d'agents (agents d'étape Canvas uniquement). Les agents de catalogue ne réessaient pas les échecs qui ne sont pas liés à la limitation de débit. Si un agent atteint sa limite quotidienne d'invocations, Braze applique les valeurs de repli configurées lorsqu'elles sont présentes ; sinon, la sortie est définie sur `null`.

Les erreurs de limitation de débit, l'indisponibilité du modèle et les échecs liés à la limite quotidienne d'invocations ne consomment pas de crédits Braze. Les délais d'attente dépassés consomment des crédits. Consultez [Quand les crédits sont consommés]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).

Lorsque de nombreux utilisateurs entrent dans une étape d'agent simultanément, le traitement peut prendre plus de temps en raison des [contrôles de flux d'invocation]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls). Configurez des valeurs de repli dans la Console d'agents pour les agents d'étape Canvas afin que les utilisateurs reçoivent toujours une sortie lorsqu'une invocation échoue, ou utilisez des [valeurs Liquid par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) dans les étapes de message en aval.

## Comment mes données sont-elles utilisées et envoyées aux LLM fournis par Braze ? {#how-is-my-data-used-and-sent-to-braze-provided-llms}

Pour générer une sortie IA via les fonctionnalités BrazeAI<sup>TM</sup> que Braze identifie comme exploitant des LLM fournis par Braze (« Sortie »), Braze enverra votre prompt système ou toute autre entrée, selon le cas (« Entrée ») au LLM fourni par Braze. Les données envoyées au LLM fourni par Braze concerné ne sont pas utilisées pour entraîner ou améliorer le LLM fourni par Braze. Entre vous et Braze, la Sortie constitue votre propriété intellectuelle. Braze ne revendiquera aucun droit d'auteur sur cette Sortie. Braze ne fournit aucune garantie de quelque nature que ce soit concernant tout contenu généré par l'IA en général, y compris la Sortie.

Le LLM fourni par Braze pour les Braze Agents, identifié comme « Auto », utilise les modèles Google Gemini. Google conserve les Entrées et les Sorties soumises via Braze pendant 55 jours, après quoi les données sont supprimées.

## Étapes suivantes {#next-steps}

Maintenant que vous connaissez les agents Braze, vous êtes prêt pour les étapes suivantes :

- [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Déployer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)