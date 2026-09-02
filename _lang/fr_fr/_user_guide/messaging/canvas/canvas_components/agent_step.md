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

> L'étape Agent vous permet d'intégrer la prise de décision et la génération de contenu basées sur l'IA directement dans votre flux de travail Canvas. Pour des informations plus générales, consultez [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents).

![Une étape Agent dans un parcours utilisateur Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Prérequis {#prerequisites}

Les étapes d'agent utilisent les [variables de contexte Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) pour ingérer le contexte pertinent et produire une variable qui peut être exploitée dans le Canvas.

## Fonctionnement {#how-it-works}

Lorsqu'un utilisateur atteint une étape Agent dans un Canvas, Braze envoie les données d'entrée que vous avez configurées (contexte complet ou champs sélectionnés) à l'agent choisi. L'agent traite ensuite l'entrée à l'aide de son modèle et de ses instructions, puis renvoie une sortie. Cette sortie est stockée dans la variable de sortie que vous avez définie dans l'étape.

Vous pouvez ensuite utiliser cette variable de trois manières principales :

- **Prise de décision :** Orientez les utilisateurs vers différents parcours Canvas en fonction de la réponse de l'agent. Par exemple, un agent de scoring de prospects pourrait renvoyer une catégorie de prospect telle que « Prêt pour la vente », « Qualifié marketing » ou « Disqualifié ». Vous pourriez utiliser cette affectation pour déclencher une alerte Slack ou un message automatisé pour les prospects « Prêts pour la vente », tout en retirant les prospects « Disqualifiés » du parcours.
- **Personnalisation :** Insérez la réponse de l'agent directement dans un message. Par exemple, un agent pourrait analyser les retours clients et générer un e-mail de suivi empathique qui fait référence au commentaire du client et suggère une résolution.
- **Traitement des données utilisateur :** Analysez et standardisez vos données utilisateur, puis stockez-les dans le profil utilisateur ou envoyez-les via un webhook. Par exemple, un agent pourrait renvoyer un score de sentiment ou une affectation d'affinité produit. Vous pouvez stocker ces données dans un profil utilisateur pour une utilisation ultérieure.

## Créer une étape Agent {#creating-an-agent-step}

### Étape 1 : Ajouter une étape {#step-1-add-a-step}

Glissez-déposez le composant **Agent** depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Agent**.

### Étape 2 : Choisir votre agent {#step-2-choose-your-agent}

Sélectionnez l'agent qui traitera les données dans cette étape. Pour obtenir des conseils de configuration, consultez [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents).

Dans la liste des agents, chaque agent est identifié par sa [limite d'invocations quotidiennes]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-3-set-up-details). Survolez la limite pour voir la progression du jour par rapport à cette limite, y compris le pourcentage utilisé et le nombre d'invocations utilisées aujourd'hui par rapport à la limite.

![Le panneau Configurer l'étape Agent affichant le menu déroulant des agents avec deux agents répertoriés. Chaque agent est identifié par sa limite d'invocations quotidiennes. Une infobulle sur le premier agent indique le pourcentage utilisé et les invocations utilisées aujourd'hui.]({% image_buster /assets/img/ai_agent/configure_agent_step.png %})

### Étape 3 : Définir la sortie de votre agent {#define-the-output-variable}

Les sorties de l'agent sont appelées « variables de sortie » et sont stockées dans une [variable de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#context-variable-filters) pour un accès facile. Pour définir la variable de sortie, donnez un nom à la variable.

Notez que le type de données de la variable de sortie est défini depuis la [console Agent]({{site.baseurl}}/user_guide/brazeai/agents). Les sorties de l'agent peuvent être enregistrées sous forme de chaînes de caractères, de nombres, de booléens ou d'objets. Cela les rend flexibles tant pour la personnalisation des messages que pour la logique conditionnelle dans votre Canvas. Voici quelques cas d'usage courants pour chaque type :

| Type de données | Cas d'usage courants |
| --- | --- |
| Chaîne de caractères | Personnalisation des messages (lignes d'objet, texte, réponses) |
| Nombre | Scores, seuils, routage dans les [parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) |
| Booléen | Branchement Oui/Non dans les [arbres décisionnels]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) |
| Objet | Exploiter un ou plusieurs des types de données mentionnés plus haut dans cette section avec un seul appel LLM dans une structure de données prévisible |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 3 : Définir la sortie de votre agent" }

Vous pouvez utiliser une variable de sortie dans l'ensemble du Canvas en utilisant la même syntaxe de modèle que pour une variable de contexte. Utilisez le filtre de Segment **Variable de contexte**, ou insérez directement les réponses de l'agent en utilisant Liquid : {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Pour utiliser une propriété spécifique d'une variable de sortie de type objet, utilisez la notation par points pour accéder à cette propriété via Liquid : {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Étape Agent pour Body HTML Writer avec un type de données objet en sortie pour la variable « agent_output ».]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Étape 4 : Ajouter des instructions d'étape facultatives {#step-4-add-optional-step-instructions}

Vous pouvez inclure des instructions d'étape facultatives pour tout ce que votre agent doit savoir de spécifique à cette étape et qui n'est pas déjà couvert dans les instructions principales de l'agent. Vous pouvez saisir toutes les valeurs Liquid que vous utiliseriez normalement dans un Canvas.

### Étape 5 : Tester l'agent {#step-5-test-the-agent}

Vous pouvez tester une étape Agent de deux manières :

**Aperçu dans l'étape (générateur Canvas) :** Après avoir configuré l'étape, utilisez l'aperçu de l'étape pour voir la sortie de l'agent pour un utilisateur aléatoire, un utilisateur existant ou un utilisateur personnalisé. Cela teste l'étape de manière isolée sans parcourir le chemin complet du Canvas.

**Test Canvas (parcours complet) :** Sélectionnez **Test Canvas** dans le pied de page du Canvas pour prévisualiser le parcours utilisateur de bout en bout. Lorsque le test atteint votre étape Agent, Braze demande **Voulez-vous exécuter l'agent « {agentName} » ?**

- Sélectionnez **Oui** pour éventuellement ajouter du contexte, puis sélectionnez **Simuler la réponse** pour invoquer l'agent pour l'utilisateur de prévisualisation. Vous pouvez décrire des entrées d'exemple en langage naturel (par exemple, le contenu du panier ou le texte du message) pour compléter le profil de l'utilisateur test et tout contexte Canvas déjà défini en amont.
- Sélectionnez **Non** pour ignorer l'invocation en direct or en ligne/en production/instantané et utiliser à la place la **sortie de secours** configurée pour l'agent depuis la console Agent.

Les invocations depuis **Simuler la réponse** sont comptabilisées dans la limite d'invocations quotidiennes de l'agent et apparaissent dans **Console Agent** > **Logs**. Pour le comportement complet du test Canvas, consultez [Prévisualiser les parcours utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths#agent-steps).

![Prévisualiser la sortie de l'agent en tant qu'utilisateur aléatoire.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Gestion des erreurs {#error-handling}

Pour savoir comment Braze gère les échecs d'agents, les erreurs de limite de débit et les contrôles de flux d'invocations, consultez [Gestion des erreurs et comportement de repli]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior) dans Déployer des agents et [Gestion des erreurs]({{site.baseurl}}/user_guide/brazeai/agents#error-handling) dans Agents Braze.

- Si le modèle connecté renvoie une [erreur de limite de débit]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) du fournisseur LLM, Braze retente continuellement la requête en utilisant des délais exponentiels jusqu'à ce que l'appel aboutisse ou que Braze détermine qu'il ne peut pas être complété ; les utilisateurs passent alors à l'étape Canvas suivante.
- Pour les autres échecs (comme une erreur de délai d'attente ou une clé API invalide), ou lorsqu'un agent atteint sa limite d'invocations quotidiennes, la variable de sortie est définie sur `null`, sauf si l'agent dispose de [valeurs de repli configurées]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) dans la Console des agents. Lorsque des valeurs de repli sont configurées, Braze effectue le rendu du repli avec Liquid par utilisateur et stocke le résultat dans la variable de sortie, y compris lorsque la limite quotidienne bloque une invocation.
- Si vous ne configurez pas de valeurs de repli, utilisez les [valeurs Liquid par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) dans les étapes de message en aval pour gérer les sorties null. Par exemple, dans la boîte de dialogue modale **Ajouter une personnalisation**, vous pouvez saisir une valeur Liquid par défaut telle que {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} ou {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- Les réponses sont mises en cache pour des entrées identiques et peuvent être réutilisées pour des invocations identiques répétées dans un délai de quelques minutes.
    - Les réponses utilisant des valeurs en cache sont tout de même comptabilisées dans le total et les invocations quotidiennes.
- Les étapes Agent peuvent prendre du temps pour traiter un grand lot d'utilisateurs. Braze met les invocations en file d'attente conformément aux [contrôles de flux d'invocations]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls), de sorte que les utilisateurs peuvent rester en attente lors d'envois à fort volume. Vérifiez vos journaux pour confirmer que les invocations sont bien en cours.

## Analyse {#analytics}

Consultez les indicateurs suivants pour suivre les performances de vos étapes Agent :

| Indicateur | Description |
| --- | --- |
| _Entrés_ | Le nombre de fois où des utilisateurs sont entrés dans l'étape Agent. |
| _Passés à l'étape suivante_ | Le nombre d'utilisateurs qui sont passés à l'étape suivante du flux après avoir traversé l'étape Agent. |
| _Sortis du Canvas_ | Le nombre d'utilisateurs qui sont sortis du Canvas après avoir traversé l'étape Agent. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analyse" }

## Bonnes pratiques {#best-practices}

### Répartir les tâches entre agents pour les cas d'usage complexes {#split-tasks-between-agents-for-complicated-use-cases}

Si vous constatez qu'un agent peine face à la complexité des tâches que vous lui demandez, répartissez le travail sur plusieurs étapes Agent. Lorsqu'un même prompt mêle nettoyage de données, logique de routage et rédaction complète de messages, ces objectifs entrent en concurrence et la qualité des résultats peut varier.

Le schéma suivant utilise trois agents pour un exemple dans le domaine du voyage : un utilisateur a effectué une recherche récemment dans votre application sans réserver, et vous souhaitez rédiger un message de reciblage qui l'incite à finaliser sa réservation.

- L'agent 1 résume le contexte du Canvas. Il lit des champs tels que le niveau de fidélité, la dernière ville recherchée et les comportements de recherche à forte intention, puis renvoie un bref résumé structuré sous forme de variable de sortie que les étapes suivantes peuvent réutiliser.
- L'agent 2 renvoie une valeur de routage sur laquelle votre Canvas peut se brancher. Utilisez un nombre, un booléen ou un objet structuré afin que la sortie corresponde à votre logique de branchement. Associez cette valeur à une étape [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) ou [Arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split). Par exemple, envisagez des parcours distincts pour un message axé sur la fidélité et un message axé sur les promotions.
- L'agent 3 rédige le texte du message généré uniquement sur les branches où vous le souhaitez. Transmettez-lui le résumé de l'agent 1 (ainsi que tout contexte propre à la branche) afin qu'il se concentre sur le ton et les limites du canal, plutôt que de normaliser les entrées et de choisir la stratégie dans le même prompt.

### Utiliser l'étape des chemins d'expérience pour tester les parcours agentiques à petite échelle {#use-the-experiment-paths-step-to-test-agentic-journeys-at-small-scale}

Pour tester les performances de votre agent et sa consommation de crédits par rapport à vos parcours existants, ajoutez une étape [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) afin que seule une partie de votre audience entre dans la branche contenant votre étape Agent.

Par exemple, vous pouvez commencer par envoyer quelques milliers d'utilisateurs par jour sur un parcours avec l'agent, et diriger le reste vers un parcours de contrôle ou un parcours sans agent. Collectez des données pendant une à deux semaines et comparez les indicateurs clés de performance (KPI), les contre-indicateurs et la consommation de crédits de l'agent entre les parcours. Vous pourrez ainsi gagner en confiance et prouver le ROI or retour sur investissement avant d'augmenter le trafic vers la branche utilisant l'agent, tout en maîtrisant la consommation d'invocations.

## Questions fréquemment posées {#frequently-asked-questions}

### Quand dois-je utiliser une étape Agent ? {#when-should-i-use-an-agent-step}

De manière générale, nous recommandons d'utiliser une étape Agent lorsque vous souhaitez fournir des données contextuelles spécifiques à un LLM et lui permettre d'attribuer de manière agentique une variable de contexte Canvas de façon intelligente, à une échelle impossible pour des humains.

Imaginons que vous envoyez un message personnalisé pour recommander un nouveau parfum de glace à un utilisateur qui a précédemment commandé du chocolat et de la fraise. Voici la différence entre l'utilisation d'une étape Agent et les recommandations d'articles par IA :

- **Étape Agent :** utilise des LLM pour prendre une décision qualitative sur ce que l'utilisateur pourrait vouloir, en se basant sur les instructions et les points de données contextuelles fournis à l'agent. Dans cet exemple, une étape Agent pourrait recommander un nouveau parfum en se basant sur la possibilité que l'utilisateur souhaite essayer des saveurs différentes.
- **Recommandations d'articles par IA :** utilise des modèles de machine learning pour prédire les produits qu'un utilisateur est le plus susceptible de vouloir, en se basant sur les événements passés de l'utilisateur, tels que les achats. Dans cet exemple, les recommandations d'articles par IA suggéreraient un parfum (vanille) en se basant sur les deux commandes précédentes de l'utilisateur (chocolat et fraise) et sur la comparaison de ces comportements avec ceux des autres utilisateurs de votre espace de travail.

### Comment les étapes Agent utilisent-elles les données d'entrée ? {#how-do-agent-steps-use-input-data}

Une étape Agent analyse les données contextuelles que l'agent est configuré pour utiliser, ainsi que toutes les [instructions d'étape facultatives](#step-4-add-optional-step-instructions) que vous ajoutez à l'étape.

## Articles connexes {#related-articles}

- [Aperçu de Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents)
- [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Déployer des agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)
- [Référence pour les agents]({{site.baseurl}}/user_guide/brazeai/agents/reference)