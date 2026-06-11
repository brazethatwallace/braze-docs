---
nav_title: Fullstory
article_title: Fullstory
description: "Cet article de référence présente le partenariat entre Braze et Fullstory."
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# Fullstory

> La plateforme de données comportementales de [Fullstory](https://www.fullstory.com/) aide les leaders technologiques à prendre de meilleures décisions, plus éclairées. En injectant des données comportementales numériques dans leur pile d'analyse, la technologie brevetée de Fullstory libère la puissance des données comportementales de qualité à grande échelle, transformant chaque visite numérique en informations exploitables.

*Cette intégration est maintenue par Fullstory*

## À propos de cette intégration {#about-this-integration}

Vous pouvez exploiter les informations de Fullstory dans Braze pour créer des images instantanées de l'expérience d'un utilisateur sur un site web ou une application, afin de diffuser des messages hyper-contextuels. L'API de résumé de session de Fullstory permet de capturer des métadonnées détaillées sur le comportement de navigation d'un utilisateur pour les utiliser dans les messages Braze, ce qui est particulièrement puissant dans le cadre d'un parcours de messages en plusieurs étapes comme un Canvas.

La valeur en temps réel des données du résumé de session de Fullstory est mieux exploitée grâce au contenu connecté. En utilisant du contenu connecté dans une étape de contexte Canvas, vous pouvez stocker les données de Fullstory tout au long du parcours Canvas d'un utilisateur pour les utiliser dans toutes les étapes Canvas suivantes. Cela évite également de devoir écrire ces données dans un profil utilisateur Braze par le biais d'événements personnalisés ou d'attributs.

Dans l'exemple suivant, les données de contexte Canvas sont exploitées dans une étape Canvas Agent IA afin de générer le message optimal pour encourager un utilisateur à reprendre un panier abandonné. Cependant, vous pouvez exploiter les données pour personnaliser directement le message, pour déterminer le parcours de l'utilisateur via les parcours d'audience, ou pour déterminer le texte ou les ressources utilisées dans les étapes ultérieures de l'envoi de messages.

## Conditions préalables {#prerequisites}

Avant de commencer, vous devez disposer des éléments suivants :

| Condition | Description |
|-----------------------|-----------------|
| Un jeton d'autorisation de l'API Session de Fullstory | Voir l'étape 1 ci-dessous. |
| Un jeton d'autorisation de contenu connecté Braze activé | Voir la note ci-dessous sur l'accès anticipé. |
| Une étape de contexte Canvas Braze | Voir la note ci-dessous sur l'accès anticipé. |
| Étape Agent IA Braze activée | Voir la note ci-dessous sur l'accès anticipé. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

{% alert important %}
Les agents Braze, le contexte Canvas et les jetons d'autorisation de contenu connecté sont tous en accès anticipé. Si vous souhaitez tirer parti de cette solution, contactez votre CSM Braze pour activer ces outils.
{% endalert %}

## Intégrer Fullstory {#integrate-fullstory}

### Étape 1 : Configurer Fullstory pour l'activation de l'API de résumé de session {#step-1}

#### Étape 1.1 : Récupérer le jeton d'authentification pour l'endpoint de l'API de résumé de session {#step-11-retrieve-the-authentication-token-for-the-session-summary-api-endpoint}

Pour créer une [clé API Fullstory](https://developer.fullstory.com/server/authentication/) :

1. Dans Fullstory, accédez à **Settings** > **API Keys**.
2. Sélectionnez le niveau d'autorisation **Standard**.
3. Copiez immédiatement la valeur de la clé, car elle n'apparaît qu'une seule fois.

#### Étape 1.2 : Créer un ID de profil de résumé de session {#step-12-create-a-session-summary-profile-id}

En suivant les [conseils de Fullstory](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles), créez un profil de résumé de session à l'aide de l'endpoint dédié. C'est ici que vous définissez le type de données que vous souhaitez que la réponse du résumé de session fournisse à Braze.

En réponse à cette requête, Fullstory fournit un ID de profil de session. Cet ID de profil est un élément clé du corps de la requête de contenu connecté utilisé dans le cas d'utilisation suivant.

### Étape 2 : Créer le jeton d'authentification du contenu connecté {#step-2-create-the-connected-content-token-authentication}

1. Dans Braze, accédez à **Settings** > **Workspace Settings** > **Connected Content** > **Add Credential** > **Token Authentication**.
2. Nommez l'authentification `fullstory`.
3. Ajoutez la clé d'en-tête « Authorization ». Indiquez la valeur de l'en-tête fournie par Fullstory à l'étape précédente.
4. Sous **Allowed Domain**, saisissez **api.fullstory.com**.

![Capture d'écran de Braze montrant les champs de modification des identifiants]({% image_buster /assets/img/fullstory/1.png %}){: style="max-width:50%;"}

## Cas d'utilisation {#use-cases}

### Créer des parcours de messages dynamiques {#create-dynamic-message-journeys}

En utilisant les [flux d'activation](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams) de Fullstory, vous pouvez déclencher des Canvas Braze immédiatement après les interactions clés de l'utilisateur. La puissance de cette intégration réside dans l'identifiant unique `client_session_id` (accessible via {% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}), que le système transmet automatiquement de Fullstory à Braze. Cet ID sert de clé, permettant à Braze de récupérer le résumé de session complet de ce que l'utilisateur a vécu.

En tirant parti des étapes de contexte Canvas et du contenu connecté, vous pouvez utiliser cet ID pour effectuer une requête API à Fullstory, récupérer les données de session et les stocker en tant que variable pour les utiliser plus tard dans le parcours.

![Étape de contexte Canvas Braze montrant la variable de contexte « summary_result » créée et alimentée par un appel de contenu connecté à Fullstory pour récupérer un résumé de session]({% image_buster /assets/img/fullstory/2.png %})

Avec le jeton d'autorisation créé précédemment, utilisez la structure de requête suivante pour extraire les données du résumé de session.

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert note %}
La réponse est enregistrée sous la forme de l'étiquette Liquid {% raw %}`{{context.${summary_result}.response}}`{% endraw %}. Utilisez cette étiquette de contexte dans les étapes Canvas suivantes.
{% endalert %}

À ce stade, le Canvas peut accéder à la réponse de l'appel de contenu connecté, qui contient l'intégralité du payload du message pour la session d'un utilisateur.

{% details Exemple de payload de l'API de résumé de session %}

{% raw %}
```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```
{% endraw %}
{% enddetails %}

Vous pouvez exploiter n'importe laquelle des données disponibles dans l'objet ci-dessus à l'aide de l'étiquette Liquid de contexte à un stade ultérieur du parcours Canvas de l'utilisateur. Les étapes suivantes montrent comment utiliser ces données dans une étape [Agent]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/).

{% alert note %}
Pour éviter tout comportement inattendu, incluez une étape de parcours d'audience après l'étape de contexte, qui peut exclure les utilisateurs du contexte si leur étiquette de contexte est vide, ce qui indique que l'appel au contenu connecté a échoué ou n'a renvoyé aucune information.

![Étape de parcours d'audience dans Braze]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

### Produire un texte approprié {#produce-appropriate-copy}

En créant une [étape Agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/) dans un Canvas déclenché par Fullstory, et en incluant l'étape de contexte décrite ci-dessus, vous pouvez référencer les données de résumé de session de Fullstory dans l'agent.

Dans cet exemple, vous utilisez ces données pour permettre à l'agent Braze de générer un texte de message approprié à utiliser dans une carte de contenu, qui peut encourager l'utilisateur à retourner dans son panier abandonné.

![Capture d'écran du créateur de contexte de l'agent Braze avec l'invite]({% image_buster /assets/img/fullstory/4.png %})

Utilisez le même nom pour l'étiquette Liquid de contexte créée dans cette étape que pour l'étiquette Liquid de contexte utilisée dans l'étape Agent IA créée précédemment.

L'invite requise pour votre cas d'utilisation varie. Pour connaître les bonnes pratiques en matière de création d'invites efficaces pour les agents, consultez [Rédaction d'instructions]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions).

Dans votre Canvas, sélectionnez une étape Agent IA, puis sélectionnez l'agent **Session Context** dans le menu déroulant. Enregistrez la sortie sous forme de variable, dans ce cas « message », que vous pouvez placer dans le texte du message en utilisant l'étiquette Liquid {% raw %}`{{context.${message}.message}}`{% endraw %}.

![Capture d'écran de l'étape Canvas de contexte de l'agent Braze avec l'invite]({% image_buster /assets/img/fullstory/5.png %})

Créez une étape de message qui exploite le texte créé par l'agent IA. Utilisez l'étiquette Liquid dans cette étape.

{% alert important %}
L'API de résumé de session de Fullstory peut renvoyer des données utilisateur sensibles et identifiables. Pour garantir la conformité lors du traitement des IIP (informations d'identification personnelle), assurez-vous que vos règles de capture de données Fullstory excluent les IIP avant de tirer parti de ce cas d'utilisation.
{% endalert %}