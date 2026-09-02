---
nav_title: "POST : Mettre à jour l'activité en direct or en ligne/en production/instantané"
article_title: "POST : Mettre à jour l'activité en direct or en ligne/en production/instantané"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Mettre à jour l'activité en direct or en ligne/en production/instantané."
---
{% api %}
# Mettre à jour l'activité en direct or en ligne/en production/instantané {#update-live-activity}
{% apimethod post %}
/messages/live_activity/update
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour et terminer les [activités en direct or en ligne/en production/instantané]({{site.baseurl}}/developer_guide/live_notifications?sdktab=swift) affichées par votre application iOS. Cet endpoint nécessite une configuration supplémentaire.

Après avoir enregistré une activité en direct or en ligne/en production/instantané, vous pouvez transmettre un payload JSON pour mettre à jour votre service de notification push Apple (APNs). Consultez la documentation d'Apple sur [la mise à jour de votre activité en direct or en ligne/en production/instantané avec des payloads de notification push](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications) pour plus d'informations.

Si `content-available` n'est pas défini, la priorité par défaut du service de notification push Apple (APNs) est 10. Si `content-available` est défini, cette priorité est de 5. Consultez l'[objet push Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object) pour plus de détails.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous devrez effectuer les opérations suivantes :

- Générer une clé API avec l'autorisation `messages.live_activity.update`.
- Enregistrer une activité en direct or en ligne/en production/instantané [à distance]({{site.baseurl}}/developer_guide/live_notifications?tab=remote&sdktab=swift) ou [localement]({{site.baseurl}}/developer_guide/live_notifications?tab=local&sdktab=swift) à l'aide du SDK Braze Swift.

{% multi_lang_include api/payload_size_alert.md %}

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la requête {#request-body}

```json
{
   "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
   "activity_id": "(required, string) When you register your Live Activity using launchActivity, you use the pushTokenTag parameter to name the Activity’s push token to a custom string. Set activity_id to this custom string to define which Live Activity you want to update.",
   "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
   "end_activity": "(optional, boolean) If true, this request ends the Live Activity.",
   "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
   "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
   "notification": "(optional, object ) Include an `apple_push` object to define a push notification that creates an alert for the user."
 }
 ```

## Request parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `app_id` | Required | String | App [API identifier]({{site.baseurl}}/api/identifier_types#app-identifier) retrieved from the [API Keys]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) page.  |
| `activity_id` | Required | String | When you register your en direct or en ligne/en production/instantané Activity using [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class), you use the `pushTokenTag` parameter to name the Activity's push token to a custom string.<br><br>Set `activity_id` to this custom string to define which en direct or en ligne/en production/instantané Activity you want to update. |
| `content_state` | Required | Object | You define the `ContentState` parameters when you create your en direct or en ligne/en production/instantané Activity. Pass the updated values for your `ContentState` using this object.<br><br>The format of this request must match the shape you initially defined. |
| `end_activity` | Optional | Boolean | If `true`, this request ends the en direct or en ligne/en production/instantané Activity. |
| `dismissal_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | This parameter defines the time to remove the en direct or en ligne/en production/instantané Activity from the user's UI. If this time is in the past and `end_activity` is `true`, the en direct or en ligne/en production/instantané Activity will be removed immediately.<br><br> If `end_activity` is `false` or omitted, this parameter only updates the en direct or en ligne/en production/instantané Activity.|
| `stale_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | This parameter tells the system when the en direct or en ligne/en production/instantané Activity content is marked as outdated in the user's UI. |
| `notification` | Optional | Object | Include an [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object) object to define a push notification. The behavior of this push notification depends on if the user is active or if the user is using a proxy device. {::nomarkdown}<ul><li>If a <code>notification</code> is included and the user is active on their iPhone when the update is delivered, the updated en direct or en ligne/en production/instantané Activity UI will slide down and display like a push notification.</li><li>If a <code>notification</code> is included and the user is not active on their iPhone, their screen will light up to display the updated en direct or en ligne/en production/instantané Activity UI on their lock screen.</li><li>The <code>notification alert</code> will not display as a standard push notification. Additionally, if a user has a proxy device, like an Apple Watch, the <code>alert</code> will be displayed there.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## Example request

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "live-activity-1",
    "content_state": {
        "teamOneScore": 2,
        "teamTwoScore": 4
    },
    "end_activity": false,
    "dismissal_date": "2023-02-28T00:00:00+0000",
    "stale_date": "2023-02-27T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "It's halftime! Let's look at the scores",
            "title": "Halftime"
        }
    }
}'
```

## Réponse {#response}

Deux codes de statut de réponse existent pour cet endpoint : `201` et `4XX`.

### Exemple de réponse réussie {#example-success-response}

Un code de statut `201` est renvoyé si la requête a été correctement formatée et que nous l'avons reçue. Le code de statut `201` pourrait renvoyer le corps de réponse suivant.

```json
{
  "message": "success"
}
```

### Exemple de réponse en erreur {#example-error-response}

La classe de code de statut `4XX` indique une erreur client. Reportez-vous à l'article [Erreurs et réponses de l'API]({{site.baseurl}}/api/errors) pour plus d'informations sur les erreurs que vous pouvez rencontrer.

Le code de statut `400` pourrait renvoyer le corps de réponse suivant.

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}