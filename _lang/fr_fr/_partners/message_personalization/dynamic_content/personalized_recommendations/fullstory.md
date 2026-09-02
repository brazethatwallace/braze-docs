---
nav_title: Fullstory
article_title: Fullstory
description: "Cet article de référence présente le partenariat entre Braze et Fullstory."
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# Fullstory

> La plateforme de données comportementales de [Fullstory](https://www.fullstory.com/) aide les leaders technologiques à prendre de meilleures décisions, plus éclairées. En injectant des données comportementales numériques dans leur stack d'analyse, la technologie brevetée de Fullstory libère la puissance des données comportementales de qualité à grande échelle, transformant chaque visite numérique en informations exploitables.

*Cette intégration est maintenue par Fullstory*

## À propos de cette intégration {#about-this-integration}

Vous pouvez exploiter les informations de Fullstory dans Braze pour dresser un portrait instantané de l'expérience d'un utilisateur sur votre site web ou votre application, et ainsi diffuser des messages ultra-contextuels. L'API Session Summary de Fullstory permet de capturer des métadonnées détaillées sur le comportement de navigation d'un utilisateur afin de les utiliser dans la communication Braze, ce qui est particulièrement puissant lorsque cette fonctionnalité est exploitée dans un parcours de communication en plusieurs étapes comme un Canvas.

La valeur en temps réel des données de résumé de session de Fullstory est optimisée grâce au contenu connecté. En utilisant le contenu connecté dans une étape Canvas Context, vous pouvez stocker les données de Fullstory tout au long du parcours Canvas d'un utilisateur pour les utiliser dans toutes les étapes Canvas suivantes. Cela évite également d'écrire ces données dans un profil utilisateur Braze par le biais d'événements personnalisés ou d'attributs.

Dans l'exemple suivant, les données Canvas Context sont exploitées dans une étape Canvas Agent IA pour générer le message optimal encourageant un utilisateur à reprendre un panier abandonné. Cependant, vous pouvez exploiter ces données pour personnaliser le message directement, pour déterminer le parcours de l'utilisateur avec des parcours d'audience, ou pour déterminer le texte ou les ressources utilisés dans les étapes de communication suivantes.

## Prérequis {#prerequisites}

Avant de commencer, vous aurez besoin des éléments suivants :

|Condition requise     | Description |
|-----------------------|-----------------|
| Un jeton d'autorisation pour l'API Session de Fullstory   | Voir l'étape 1 de ce guide. |
| Un jeton d'autorisation de contenu connecté Braze activé | Voir la note sur l'accès anticipé dans cette section. |
| Une étape Canvas Context de Braze | Voir la note sur l'accès anticipé dans cette section. |
| Une étape Braze AI Agent activée | Voir la note sur l'accès anticipé dans cette section. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

{% alert important %}
Braze Agents, Canvas Context et les jetons d'autorisation de contenu connecté sont tous en accès anticipé. Si vous souhaitez tirer parti de cette solution, contactez votre CSM or gestionnaire de la satisfaction client or gestionnaire du succès des clients Braze pour activer ces outils.
{% endalert %}

## Intégrer Fullstory {#integrate-fullstory}

### Étape 1 : Configurer Fullstory pour l'activation de l'API Session Summary {#step-1}

#### Étape 1.1 : Récupérer le jeton d'authentification pour l'endpoint de l'API Session Summary {#step-11-retrieve-the-authentication-token-for-the-session-summary-api-endpoint}

Pour créer une [clé API Fullstory](https://developer.fullstory.com/server/authentication/) :

1. Dans Fullstory, accédez à **Settings** > **API Keys**.
2. Sélectionnez le niveau de permission **Standard**.
3. Copiez immédiatement la valeur de la clé, car elle n'apparaît qu'une seule fois.

#### Étape 1.2 : Créer un identifiant de profil de résumé de session {#step-12-create-a-session-summary-profile-id}

En suivant [les instructions de Fullstory](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles), créez un profil de résumé de session à l'aide de l'endpoint dédié. C'est ici que vous définissez le type de données que vous souhaitez que la réponse du résumé de session fournisse à Braze.

Dans la réponse à cette requête, Fullstory fournit un identifiant de profil de session. Cet identifiant de profil est un composant essentiel du corps de la requête de contenu connecté utilisé dans le cas d'usage suivant.

### Étape 2 : Créer l'authentification par jeton pour le contenu connecté {#step-2-create-the-connected-content-token-authentication}

1. Dans Braze, accédez à **Paramètres** > **Paramètres de l'espace de travail** > **Contenu connecté** > **Ajouter des identifiants** > **Authentification par jeton**.
2. Nommez l'authentification `fullstory`.
3. Ajoutez la clé d'en-tête « Authorization ». Renseignez la valeur d'en-tête fournie par Fullstory à l'étape précédente.
4. Sous **Domaine autorisé**, saisissez **api.fullstory.com**.

![Capture d'écran de Braze montrant les champs de modification des identifiants]({% image_buster /assets/img/fullstory/1.png %}){: style="max-width:50%;"}

## Cas d'usage {#use-cases}

### Créer des parcours de messages dynamiques {#create-dynamic-message-journeys}

Grâce aux [Activation Streams](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams) de Fullstory, vous pouvez déclencher des Canvas Braze immédiatement après des interactions clés de l'utilisateur. La puissance de cette intégration réside dans le `client_session_id` unique (accessible via {% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}), que le système transmet automatiquement de Fullstory à Braze. Cet identifiant agit comme une clé, permettant à Braze de récupérer le résumé complet de la session correspondant exactement à ce que l'utilisateur a vécu.

En tirant parti des étapes de contexte Canvas et du contenu connecté, vous pouvez utiliser cet identifiant pour effectuer une requête API vers Fullstory, récupérer les données de session et les stocker comme variable pour les utiliser plus tard dans le parcours.

![Étape de contexte Canvas dans Braze montrant la variable de contexte « summary_result » en cours de création et renseignée par un appel de contenu connecté vers Fullstory pour récupérer un résumé de session]({% image_buster /assets/img/fullstory/2.png %})

Avec le jeton d'autorisation créé précédemment, utilisez la structure de requête suivante pour récupérer les données du résumé de session.

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert note %}
La réponse est stockée sous l'étiquette Liquid {% raw %}`{{context.${summary_result}.response}}`{% endraw %}. Utilisez cette étiquette de contexte dans les étapes Canvas suivantes.
{% endalert %}

À ce stade, le Canvas peut accéder à la réponse de l'appel de contenu connecté, qui contient l'intégralité du payload du message pour la session de l'utilisateur.

{% details Exemple de payload provenant de l'API Session Summary %}

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

Vous pouvez exploiter n'importe quelle donnée disponible dans l'objet précédent en utilisant l'étiquette Liquid de contexte plus tard dans le parcours Canvas de l'utilisateur. Les étapes suivantes montrent comment utiliser ces données dans une étape [Agent]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

{% alert note %}
Pour éviter tout comportement inattendu, ajoutez une étape de parcours d'audience après l'étape de contexte, qui peut exclure les utilisateurs du contexte si leur étiquette de contexte est vide, ce qui indique que l'appel de contenu connecté a échoué ou n'a renvoyé aucune information.

![L'étape de parcours d'audience dans Braze]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

### Produire un contenu approprié {#produce-appropriate-copy}

En créant une [étape Agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) dans un Canvas déclenché par Fullstory, et en incluant l'étape de contexte décrite dans cette section, vous pouvez référencer les données de résumé de session de Fullstory dans l'agent.

Dans cet exemple, vous utilisez ces données pour permettre à l'agent Braze de générer un contenu de message approprié destiné à une Content Card, afin d'encourager l'utilisateur à revenir à son panier abandonné.

![Capture d'écran du créateur de contexte de l'agent Braze avec le prompt]({% image_buster /assets/img/fullstory/4.png %})

Utilisez le même nom pour l'étiquette Liquid de contexte créée dans cette étape que celle utilisée dans l'étape Agent IA créée précédemment.

Le prompt requis varie selon votre cas d'usage. Pour les bonnes pratiques de création de prompts d'agent efficaces, consultez [Rédiger des instructions]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions).

Dans votre Canvas, sélectionnez une étape Agent IA, puis sélectionnez l'agent **Session Context** dans le menu déroulant. Enregistrez la sortie comme variable, dans ce cas « message », que vous pouvez insérer dans le contenu du message en utilisant l'étiquette Liquid {% raw %}`{{context.${message}.message}}`{% endraw %}.

![Capture d'écran de l'étape Canvas de contexte de l'agent Braze avec le prompt]({% image_buster /assets/img/fullstory/5.png %})

Créez une étape Message qui exploite le contenu généré par l'agent IA. Utilisez l'étiquette Liquid dans cette étape.

{% alert important %}
L'API Session Summary de Fullstory peut renvoyer des données d'identification sensibles de l'utilisateur. Pour garantir la conformité lors de la manipulation des données d'identification (PII), confirmez que vos règles de capture de données Fullstory excluent les données d'identification avant d'exploiter ce cas d'usage.
{% endalert %}