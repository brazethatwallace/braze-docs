---
nav_title: Agent
article_title: Étape Agent
alias: /agent_step/
page_order: 2
page_type: reference
description: "Cet article de référence explique comment utiliser l'étape Agent dans Canvas pour générer du contenu ou prendre des décisions intelligentes en temps réel."
tool: Canvas
toc_headers: h2
---

# Étape Agent {#agent-step}

> L'étape Agent vous permet d'intégrer la prise de décision et la génération de contenu basées sur l'intelligence artificielle directement dans votre flux de travail Canvas. Pour des informations plus générales, consultez [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents).

![Une étape Agent dans un parcours utilisateur Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Conditions préalables {#prerequisites}

Les étapes Agent utilisent les [variables de contexte Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) pour ingérer le contexte pertinent et produire une variable exploitable dans le Canvas.

## Fonctionnement {#how-it-works}

Lorsqu'un utilisateur atteint une étape Agent dans un Canvas, Braze envoie les données d'entrée que vous avez configurées (contexte complet ou champs sélectionnés) à l'agent choisi. L'agent traite ensuite les données à l'aide de son modèle et de ses instructions, puis renvoie un résultat. Ce résultat est stocké dans la variable de sortie que vous avez définie dans l'étape.

Vous pouvez ensuite utiliser cette variable de trois manières principales :

- **Prise de décision :** Orientez les utilisateurs vers différents parcours Canvas en fonction de la réponse de l'agent. Par exemple, un agent de scoring de leads peut renvoyer une catégorie de lead telle que « Sales Ready », « Marketing Qualified » ou « Disqualified ». Vous pouvez utiliser cette affectation pour déclencher une alerte Slack ou un message automatisé pour les leads « Sales Ready » tout en retirant les leads « Disqualified » du parcours.
- **Personnalisation :** Insérez la réponse de l'agent directement dans un message. Par exemple, un agent pourrait analyser les retours d'un client et générer un e-mail de suivi empathique qui fait référence au commentaire du client et propose une solution.
- **Traitement des données utilisateur :** Analysez et standardisez vos données utilisateur, puis stockez-les dans le profil utilisateur ou envoyez-les via un webhook. Par exemple, un agent pourrait renvoyer un score de sentiment ou une affectation d'affinité produit. Vous pouvez stocker ces données dans un profil utilisateur pour une utilisation ultérieure.

## Créer une étape Agent {#creating-an-agent-step}

### Étape 1 : Ajouter une étape {#step-1-add-a-step}

Glissez-déposez le composant **Agent** depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Agent**.

### Étape 2 : Choisir votre agent {#step-2-choose-your-agent}

Sélectionnez l'agent qui traitera les données dans cette étape. Pour des conseils de configuration, consultez [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents).

Dans la liste des agents, chaque agent est accompagné de sa [limite d'invocations quotidiennes]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-3-set-up-details). Survolez la limite pour voir la progression du jour, y compris le pourcentage utilisé et le nombre d'invocations effectuées par rapport à la limite.

![Le panneau Configurer l'étape Agent affichant le menu déroulant des agents avec deux agents listés. Chaque agent est accompagné de sa limite d'invocations quotidiennes. Une infobulle sur le premier agent montre le pourcentage utilisé et les invocations effectuées aujourd'hui.]({% image_buster /assets/img/ai_agent/configure_agent_step.png %})

### Étape 3 : Définir la sortie de votre agent {#define-the-output-variable}

Les sorties de l'agent sont appelées « variables de sortie » et sont stockées dans une [variable de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#context-variable-types) pour un accès facile. Pour définir la variable de sortie, donnez un nom à la variable.

Notez que le type de données de la variable de sortie est défini depuis la [Console des agents]({{site.baseurl}}/user_guide/brazeai/agents). Les sorties de l'agent peuvent être enregistrées sous forme de chaînes de caractères, de nombres, de valeurs booléennes ou d'objets. Cela les rend flexibles aussi bien pour la personnalisation de texte que pour la logique conditionnelle dans votre Canvas. Voici quelques utilisations courantes pour chaque type :

| Type de données | Utilisations courantes |
| --- | --- |
| Chaîne de caractères | Personnalisation des messages (lignes d'objet, texte, réponses) |
| Nombre | Scoring, seuils, routage dans les [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) |
| Valeur booléenne | Branchement Oui/Non dans les [Arbres décisionnels]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) |
| Objet | Exploitez un ou plusieurs des types de données ci-dessus avec un seul appel LLM dans une structure de données prévisible |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 3 : Définir la sortie de votre agent" }

Vous pouvez utiliser une variable de sortie dans l'ensemble du Canvas en utilisant la même syntaxe de template que pour une variable de contexte. Utilisez soit le filtre de segment **Context Variable**, soit intégrez directement les réponses de l'agent avec Liquid : {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Pour utiliser une propriété spécifique d'une variable de sortie de type objet, utilisez la notation par points pour accéder à cette propriété avec Liquid : {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Étape Agent pour Body HTML Writer avec un type de données objet en sortie pour la variable « agent_output ».]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Étape 4 : Ajouter du contexte supplémentaire (facultatif) {#step-4-add-any-additional-context-optional}

Vous pouvez choisir d'inclure des valeurs de contexte supplémentaires que l'étape Agent pourra consulter lors de son exécution. Vous pouvez saisir toutes les valeurs Liquid que vous utiliseriez normalement dans un Canvas.

{% alert note %}
L'agent reçoit déjà automatiquement le contexte configuré dans la section **Instructions**. Les variables Liquid déjà configurées à cet endroit n'ont pas besoin d'être saisies à nouveau ici.
{% endalert %}

![L'option d'ajouter du contexte supplémentaire à une étape Agent en utilisant Liquid.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### Étape 5 : Tester l'agent {#step-5-test-the-agent}

Après avoir configuré votre étape Agent, vous pouvez tester et prévisualiser la sortie de cette étape.

![Prévisualiser la sortie de l'agent en tant qu'utilisateur aléatoire.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Gestion des erreurs {#error-handling}

Pour savoir comment Braze gère les échecs d'agents, les erreurs de limite de débit et les contrôles de flux d'invocations, consultez [Gestion des erreurs et comportement de repli]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior) dans Déployer des agents et [Gestion des erreurs]({{site.baseurl}}/user_guide/brazeai/agents#error-handling) dans Agents Braze.

- Si le modèle connecté renvoie une [erreur de limite de débit]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) du fournisseur LLM, Braze retente continuellement la requête en utilisant des délais exponentiels jusqu'à ce que l'appel aboutisse ou que Braze détermine qu'il ne peut pas être complété ; les utilisateurs passent alors à l'étape Canvas suivante.
- Pour les autres échecs (comme une erreur de délai d'attente ou une clé API invalide), ou lorsqu'un agent atteint sa limite d'invocations quotidiennes, la variable de sortie est définie sur `null`, sauf si l'agent dispose de [valeurs de repli configurées]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) dans la Console des agents. Lorsque des valeurs de repli sont configurées, Braze effectue le rendu du repli avec Liquid par utilisateur et stocke le résultat dans la variable de sortie, y compris lorsque la limite quotidienne bloque une invocation.
- Si vous ne configurez pas de valeurs de repli, utilisez les [valeurs Liquid par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) dans les étapes de message en aval pour gérer les sorties null. Par exemple, dans la fenêtre modale **Ajouter une personnalisation**, vous pouvez saisir une valeur Liquid par défaut telle que {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} ou {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- Les réponses sont mises en cache pour des entrées identiques et peuvent être réutilisées pour des invocations identiques répétées dans un délai de quelques minutes.
    - Les réponses utilisant des valeurs en cache sont tout de même comptabilisées dans le total et les invocations quotidiennes.
- Les étapes Agent peuvent prendre du temps pour traiter un grand lot d'utilisateurs. Braze met les invocations en file d'attente conformément aux [contrôles de flux d'invocations]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls), de sorte que les utilisateurs peuvent rester en attente lors d'envois à fort volume. Vérifiez vos journaux pour confirmer que les invocations sont bien en cours.

## Analytique {#analytics}

Consultez les indicateurs suivants pour suivre les performances de vos étapes Agent :

| Indicateur | Description |
| --- | --- |
| _Entrés_ | Le nombre de fois où des utilisateurs sont entrés dans l'étape Agent. |
| _Passés à l'étape suivante_ | Le nombre d'utilisateurs qui sont passés à l'étape suivante du flux après avoir traversé l'étape Agent. |
| _Sortis du Canvas_ | Le nombre d'utilisateurs qui ont quitté le Canvas après avoir traversé l'étape Agent. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytique" }

## Bonnes pratiques {#best-practices}

### Répartir les tâches entre agents pour les cas d'utilisation complexes {#split-tasks-between-agents-for-complicated-use-cases}

Si vous constatez qu'un agent peine face à la complexité des tâches que vous lui demandez, répartissez le travail sur plusieurs étapes Agent. Lorsqu'un même prompt mélange nettoyage de données, logique de routage et rédaction complète de messages, ces objectifs entrent en concurrence et la qualité des résultats peut varier.

Le schéma suivant utilise trois agents pour un exemple dans le domaine du voyage : un utilisateur a effectué une recherche récemment dans votre application sans réserver, et vous souhaitez un texte de reciblage qui l'incite à finaliser sa réservation.

- L'agent 1 résume le contexte Canvas. Il lit des champs tels que le niveau de fidélité, la dernière ville recherchée et le comportement de recherche à forte intention, puis renvoie un résumé structuré court sous forme de variable de sortie que les étapes suivantes peuvent réutiliser.
- L'agent 2 renvoie une valeur de routage sur laquelle votre Canvas peut se brancher. Utilisez un nombre, une valeur booléenne ou un objet structuré afin que la sortie corresponde à votre logique de branchement. Associez cette valeur à une étape [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) ou [Arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split). Par exemple, envisagez des parcours distincts pour un envoi de messages axé sur la fidélité et un envoi axé sur les promotions.
- L'agent 3 rédige le texte du message généré uniquement sur les branches où vous le souhaitez. Transmettez le résumé de l'agent 1 (ainsi que tout contexte spécifique à la branche) afin que cet agent se concentre sur le ton et les limites du canal plutôt que de normaliser les entrées et de choisir la stratégie dans le même prompt.

### Utiliser l'étape Chemins d'expérience pour tester les parcours agentiques à petite échelle {#use-the-experiment-paths-step-to-test-agentic-journeys-at-small-scale}

Pour tester les performances de votre agent et la consommation de crédits par rapport à vos parcours existants, ajoutez une étape [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) afin que seule une partie de votre audience entre dans la branche contenant votre étape Agent.

Par exemple, vous pouvez commencer par envoyer quelques milliers d'utilisateurs par jour dans un parcours avec l'agent et le reste vers un parcours de contrôle ou un parcours sans agent. Collectez des données pendant 1 à 2 semaines et comparez les indicateurs clés de performance (KPI), les contre-indicateurs et la consommation de crédits de l'agent entre les parcours. Ainsi, vous pouvez gagner en confiance et prouver le ROI avant d'augmenter le trafic vers la branche utilisant l'agent, tout en limitant la consommation d'invocations.

## Questions fréquentes {#frequently-asked-questions}

### Quand utiliser une étape Agent ? {#when-should-i-use-an-agent-step}

De manière générale, nous recommandons d'utiliser une étape Agent lorsque vous souhaitez fournir des données contextuelles spécifiques à un LLM et lui faire attribuer de manière agentique une variable de contexte Canvas de façon intelligente, à une échelle impossible pour des humains.

Imaginons que vous envoyez un message personnalisé pour recommander un nouveau parfum de glace à un utilisateur qui a précédemment commandé chocolat et fraise. Voici la différence entre l'utilisation d'une étape Agent et les Recommandations produit basées sur l'IA :

- **Étape Agent :** Utilise des LLM pour prendre une décision qualitative sur ce que l'utilisateur pourrait vouloir, en se basant sur les instructions et les données contextuelles fournies à l'agent. Dans cet exemple, une étape Agent pourrait recommander un nouveau parfum en se basant sur la possibilité que l'utilisateur souhaite essayer des saveurs différentes.
- **Recommandations produit basées sur l'IA :** Utilise des modèles de machine learning pour prédire les produits qu'un utilisateur est le plus susceptible de vouloir, en se basant sur les événements passés de l'utilisateur, comme les achats. Dans cet exemple, les Recommandations produit basées sur l'IA suggéreraient un parfum (vanille) en se basant sur les deux commandes précédentes de l'utilisateur (chocolat et fraise) et sur la comparaison avec les comportements d'autres utilisateurs dans votre espace de travail.

### Comment les étapes Agent utilisent-elles les données d'entrée ? {#how-do-agent-steps-use-input-data}

Une étape Agent analyse les données de contexte que l'agent est configuré pour utiliser, ainsi que tout contexte supplémentaire [fourni à l'agent](#step-4-add-any-additional-context-optional).

## Articles connexes {#related-articles}

- [Aperçu des agents Braze]({{site.baseurl}}/user_guide/brazeai/agents)
- [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Déployer des agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)
- [Référence pour les agents]({{site.baseurl}}/user_guide/brazeai/agents/reference)