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

# Étape Agent

> L'étape Agent vous permet d'intégrer la prise de décision et la génération de contenu basées sur l'intelligence artificielle directement dans votre flux de travail Canvas. Pour des informations plus générales, consultez [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/).

![Une étape Agent dans un parcours utilisateur Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Conditions préalables

Les étapes Agent utilisent les [variables de contexte Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/) pour ingérer le contexte pertinent et produire une variable exploitable dans le Canvas.

## Fonctionnement

Lorsqu'un utilisateur atteint une étape Agent dans un Canvas, Braze envoie les données d'entrée que vous avez configurées (contexte complet ou champs sélectionnés) à l'agent choisi. L'agent traite ensuite les données à l'aide de son modèle et de ses instructions, puis renvoie un résultat. Ce résultat est stocké dans la variable de sortie que vous avez définie dans l'étape.

Vous pouvez ensuite utiliser cette variable de trois manières principales :

- **Prise de décision :** Orientez les utilisateurs vers différents parcours Canvas en fonction de la réponse de l'agent. Par exemple, un agent de scoring de leads peut renvoyer un nombre entre 1 et 10. Vous pouvez utiliser ce score pour décider de continuer à envoyer des messages à un utilisateur ou de le retirer du parcours.
- **Personnalisation :** Insérez la réponse de l'agent directement dans un message. Par exemple, un agent pourrait analyser les retours d'un client et générer un e-mail de suivi empathique qui fait référence au commentaire du client et propose une solution.
- **Traitement des données utilisateur :** Analysez et standardisez vos données utilisateur, puis stockez-les dans le profil utilisateur ou envoyez-les via un webhook. Par exemple, un agent pourrait renvoyer un score de sentiment ou une affectation d'affinité produit. Vous pouvez stocker ces données dans un profil utilisateur pour une utilisation ultérieure.

## Créer une étape Agent

### Étape 1 : Ajouter une étape

Glissez-déposez le composant **Agent** depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Agent**.

### Étape 2 : Choisir votre agent

Sélectionnez l'agent qui traitera les données dans cette étape. Choisissez un agent existant. Pour des conseils de configuration, consultez [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Étape 3 : Définir la sortie de votre agent {#define-the-output-variable}

Les sorties de l'agent sont appelées « variables de sortie » et sont stockées dans une [variable de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#context-variable-types) pour un accès facile. Pour définir la variable de sortie, donnez un nom à la variable.

Notez que le type de données de la variable de sortie est défini depuis la [Console des agents]({{site.baseurl}}/user_guide/brazeai/agents). Les sorties de l'agent peuvent être enregistrées sous forme de chaînes de caractères, de nombres, de valeurs booléennes ou d'objets. Cela les rend flexibles aussi bien pour la personnalisation de texte que pour la logique conditionnelle dans votre Canvas. Voici quelques utilisations courantes pour chaque type :

| Type de données | Utilisations courantes |
| --- | --- |
| Chaîne de caractères | Personnalisation des messages (lignes d'objet, texte, réponses) |
| Nombre | Scoring, seuils, routage dans les [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) |
| Valeur booléenne | Branchement Oui/Non dans les [Arbres décisionnels]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) |
| Objet | Exploitez un ou plusieurs des types de données ci-dessus avec un seul appel LLM dans une structure de données prévisible |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Vous pouvez utiliser une variable de sortie dans l'ensemble du Canvas en utilisant la même syntaxe de template que pour une variable de contexte. Utilisez soit le filtre de segment **Context Variable**, soit intégrez directement les réponses de l'agent avec Liquid : {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Pour utiliser une propriété spécifique d'une variable de sortie de type objet, utilisez la notation par points pour accéder à cette propriété avec Liquid : {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Étape Agent pour Body HTML Writer avec un type de données objet en sortie pour la variable « agent_output ».]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Étape 4 : Ajouter du contexte supplémentaire (facultatif)

Vous pouvez choisir d'inclure des valeurs de contexte supplémentaires que l'étape Agent pourra consulter lors de son exécution. Vous pouvez saisir toutes les valeurs Liquid que vous utiliseriez normalement dans un Canvas.

{% alert note %}
L'agent reçoit déjà automatiquement le contexte configuré dans la section **Instructions**. Les variables Liquid déjà configurées à cet endroit n'ont pas besoin d'être saisies à nouveau ici.
{% endalert %}

![L'option d'ajouter du contexte supplémentaire à une étape Agent en utilisant Liquid.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### Étape 5 : Tester l'agent

Après avoir configuré votre étape Agent, vous pouvez tester et prévisualiser la sortie de cette étape.

![Prévisualiser la sortie de l'agent en tant qu'utilisateur aléatoire.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Gestion des erreurs

- Si le modèle connecté renvoie une erreur de limite de débit, Braze effectue jusqu'à cinq nouvelles tentatives avec des délais exponentiels.
- Si l'agent échoue pour toute autre raison (comme une erreur de délai d'attente ou une clé API invalide), la variable de sortie est définie sur `null`.
    - Si un agent atteint sa limite d'invocations quotidiennes, la variable de sortie est définie sur `null`.
- Utilisez les [valeurs Liquid par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/) pour vous prémunir contre les erreurs. Par exemple, dans la boîte de dialogue modale **Add Personalization**, vous pouvez saisir une valeur Liquid par défaut telle que {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} ou {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- Les réponses sont mises en cache pour des entrées identiques et peuvent être réutilisées pour des invocations identiques répétées dans un délai de quelques minutes.
    - Les réponses utilisant des valeurs en cache sont tout de même comptabilisées dans le total et les invocations quotidiennes.
- Les étapes Agent peuvent prendre du temps pour traiter un grand lot d'utilisateurs. Si vous constatez que des utilisateurs sont encore en attente dans cette étape, vérifiez vos journaux pour confirmer que les invocations sont bien en cours.

## Analytique

Consultez les indicateurs suivants pour suivre les performances de vos étapes Agent :

| Indicateur | Description |
| --- | --- |
| _Entrés_ | Le nombre de fois où des utilisateurs sont entrés dans l'étape Agent. |
| _Passés à l'étape suivante_ | Le nombre d'utilisateurs qui sont passés à l'étape suivante du flux après avoir traversé l'étape Agent. |
| _Sortis du Canvas_ | Le nombre d'utilisateurs qui ont quitté le Canvas après avoir traversé l'étape Agent. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Questions fréquentes

### Quand utiliser une étape Agent ?

De manière générale, nous recommandons d'utiliser une étape Agent lorsque vous souhaitez fournir des données contextuelles spécifiques à un LLM et lui faire attribuer de manière agentique une variable de contexte Canvas de façon intelligente, à une échelle impossible pour des humains.

Imaginons que vous envoyez un message personnalisé pour recommander un nouveau parfum de glace à un utilisateur qui a précédemment commandé chocolat et fraise. Voici la différence entre l'utilisation d'une étape Agent et les Recommandations produit basées sur l'IA :

- **Étape Agent :** Utilise des LLM pour prendre une décision qualitative sur ce que l'utilisateur pourrait vouloir, en se basant sur les instructions et les données contextuelles fournies à l'agent. Dans cet exemple, une étape Agent pourrait recommander un nouveau parfum en se basant sur la possibilité que l'utilisateur souhaite essayer des saveurs différentes.
- **Recommandations produit basées sur l'IA :** Utilise des modèles de machine learning pour prédire les produits qu'un utilisateur est le plus susceptible de vouloir, en se basant sur les événements passés de l'utilisateur, comme les achats. Dans cet exemple, les Recommandations produit basées sur l'IA suggéreraient un parfum (vanille) en se basant sur les deux commandes précédentes de l'utilisateur (chocolat et fraise) et sur la comparaison avec les comportements d'autres utilisateurs dans votre espace de travail.

### Comment les étapes Agent utilisent-elles les données d'entrée ?

Une étape Agent analyse les données de contexte que l'agent est configuré pour utiliser, ainsi que tout contexte supplémentaire [fourni à l'agent](#step-4-add-any-additional-context-optional).

## Articles connexes

- [Aperçu des agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/)
- [Créer des agents personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Déployer des agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)
- [Référence pour les agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/)