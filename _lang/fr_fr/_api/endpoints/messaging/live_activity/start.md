---
nav_title: "POST : Démarrer une activité en direct"
article_title: "POST : Démarrer une activité en direct"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Démarrer une activité en direct."

---
{% api %}
# Démarrer une activité en direct {#start-live-activity}
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> Utilisez cet endpoint pour démarrer à distance les [activités en direct]({{site.baseurl}}/developer_guide/live_notifications?sdktab=swift) affichées dans votre application iOS. Cet endpoint nécessite une configuration supplémentaire.

Après avoir créé une activité en direct, effectuez une requête POST pour cibler un segment, une audience connectée ou des utilisateurs spécifiques. Identifiez les utilisateurs spécifiques par leur ID utilisateur externe, leur alias d'utilisateur, ou les deux. Pour en savoir plus sur les activités en direct d'Apple, consultez [Starting and updating Live Activities with ActivityKit push notifications](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications).

Si `content-available` n'est pas défini, la priorité par défaut du service Apple Push Notification (APNs) est 10. Si `content-available` est défini, cette priorité est de 5. Pour plus d'informations, consultez l'[objet push Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object).

{% alert tip %}
Pour mettre fin à une activité en direct, utilisez l'endpoint [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) avec `end_activity` défini sur `true`.
{% endalert %}

## Planifier la suppression automatique {#arranging-automatic-dismissal}

Pour planifier la suppression automatique après le démarrage d'une activité en direct, programmez une requête de suivi vers l'endpoint de mise à jour depuis votre backend.

1. Envoyez une requête `/messages/live_activity/start` avec un `activity_id` que vous pourrez réutiliser ultérieurement.
2. Stockez cet `activity_id` et l'heure de fin souhaitée dans le planificateur de votre backend.
3. À l'heure de fin prévue, envoyez une requête `/messages/live_activity/update` avec `end_activity` défini sur `true`.
4. Configurez le comportement de suppression dans la même requête de mise à jour. Pour plus de détails, consultez l'endpoint [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update).
5. Vérifiez les événements d'envoi et de résultat dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous devrez effectuer les opérations suivantes :

- Générer une clé API avec l'autorisation `messages.live_activity.start`.
- [Créer une activité en direct]({{site.baseurl}}/developer_guide/live_notifications/live_activities?tab=local&sdktab=swift#create-an-activity) à l'aide du SDK Braze Swift.

{% multi_lang_include api/payload_size_alert.md %}

{% alert important %}
Lorsque vous ciblez des utilisateurs spécifiques, Braze ne démarre une activité en direct que pour les `external_user_ids` et `user_aliases` qui correspondent à des utilisateurs existants.
{% endalert %}

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la requête {#request-body}

```json
{
  "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
  "activity_id": "(required, string) Define a custom string as your `activity_id`. Use this ID to send update or end events to your Live Activity.",
  "activity_attributes_type": "(required, string) The activity attributes type you define within `liveActivities.registerPushToStart` in your app.",
  "activity_attributes": "(required, object) The static attribute values for the activity type (such as the sports team names, which don't change)",
  "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
  "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
  "notification": "(required, object) Include an `apple_push` object to define a push notification that creates an alert for the user, displayed on paired watchOS devices. Include `notification.alert.title` and `notification.alert.body`.",
  // Include one targeting method:
  // 1. "external_user_ids", "user_aliases", or both (combined maximum 50)
  // 2. "custom_audience"
  // 3. "segment_id"
  "external_user_ids": "(optional, array of strings) see external user identifier",
  "user_aliases": "(optional, array of user alias objects) see user alias object",
  "custom_audience": "(optional, connected audience object) see connected audience",
  "segment_id": "(optional, string) see segment identifier"
}
```

## Paramètres de la requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|-----------|----------|----------|--------------|
| `app_id` | Requis | Chaîne de caractères | [Identifiant API]({{site.baseurl}}/api/identifier_types#app-identifier) de l'application, récupéré depuis la page [Clés API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). |
| `activity_id` | Requis | Chaîne de caractères | Définissez une chaîne de caractères personnalisée comme `activity_id`. Utilisez cet ID pour envoyer des événements de mise à jour ou de fin à votre activité en direct. |
| `activity_attributes_type` | Requis | Chaîne de caractères | Le type d'attributs d'activité que vous définissez dans `liveActivities.registerPushToStart` dans votre application. |
| `activity_attributes` | Requis | Objet | Les valeurs d'attributs statiques pour le type d'activité (comme les noms des équipes sportives, qui ne changent pas). |
| `content_state` | Requis | Objet | Vous définissez les paramètres `ContentState` lorsque vous créez votre activité en direct. Transmettez les valeurs mises à jour pour votre `ContentState` à l'aide de cet objet.<br><br>Le format de cette requête doit correspondre à la structure que vous avez initialement définie. |
| `stale_date` | Facultatif | Datetime <br>(chaîne [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Ce paramètre indique au système quand le contenu de l'activité en direct est marqué comme obsolète dans l'interface utilisateur. |
| `notification` | Requis | Objet | Incluez un objet [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object) pour définir une notification push. Le comportement de cette notification push dépend de l'activité de l'utilisateur ou de l'utilisation éventuelle d'un appareil proxy. {::nomarkdown}<ul><li>Si une <code>notification</code> est incluse et que l'utilisateur est actif sur son iPhone lorsque la mise à jour est livrée, l'interface de l'activité en direct mise à jour glisse vers le bas et s'affiche comme une notification push.</li><li>Si une <code>notification</code> est incluse et que l'utilisateur n'est pas actif sur son iPhone, son écran s'allume pour afficher l'interface de l'activité en direct mise à jour sur l'écran de verrouillage.</li><li>L'alerte <code>notification alert</code> ne s'affiche pas comme une notification push standard. De plus, si l'utilisateur dispose d'un appareil proxy, comme une Apple Watch, l'<code>alert</code> y est affichée.</li></ul>{:/} |
| `external_user_ids` | Facultatif si `user_aliases`, `segment_id` ou `custom_audience` est fourni | Tableau de chaînes de caractères | Voir [ID utilisateur externe]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields). |
| `user_aliases` | Facultatif si `external_user_ids`, `segment_id` ou `custom_audience` est fourni | Tableau d'objets alias d'utilisateur | Voir [objet alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object). |
| `segment_id` | Facultatif si `external_user_ids`, `user_aliases` ou `custom_audience` est fourni | Chaîne de caractères | Voir [identifiant de segment]({{site.baseurl}}/api/identifier_types). |
| `custom_audience` | Facultatif si `external_user_ids`, `user_aliases` ou `segment_id` est fourni | Objet audience connectée | Voir [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de la requête" }

Vous pouvez inclure `external_user_ids` et `user_aliases` dans la même requête. La longueur combinée de leur tableau ne peut pas dépasser 50. Braze cible les utilisateurs qui correspondent à l'un ou l'autre des paramètres et n'envoie qu'une seule fois lorsque plusieurs identifiants correspondent au même utilisateur.

Ne combinez pas `external_user_ids` ou `user_aliases` avec `segment_id` ou `custom_audience`. Sur cet endpoint, utilisez `custom_audience` pour transmettre les filtres d'audience connectée.

## Exemple de requête {#example-request}

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/start' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR_REST_API_KEY}' \
--data-raw '{
  "app_id": "{YOUR_APP_API_IDENTIFIER}",
  "activity_id": "football-chiefs-bills-2024-01-21",
  "content_state": {
    "teamOneScore": 0,
    "teamTwoScore": 0
  },
  "activity_attributes_type": "FootballActivity",
  "activity_attributes": {
    "team1Name": "Chiefs",
    "team2Name": "Bills"
  },
  "stale_date": "2024-01-22T16:55:49+0000",
  "notification": {
    "alert": {
      "body": "The game is starting! Tune in soon!",
      "title": "Chiefs v. Bills"
    }
  },
  "external_user_ids": ["user-id1", "user-id2"],
  "user_aliases": [
    {
      "alias_name": "user-name",
      "alias_label": "user-label"
    }
  ]
}'
```

## Réponse {#response}

Deux codes de statut sont possibles pour cet endpoint : `201` et `4XX`.

### Exemple de réponse réussie {#example-success-response}

Un code de statut `201` est renvoyé si la requête est correctement formatée et que Braze l'a reçue. Le code de statut `201` peut renvoyer le corps de réponse suivant.

```json
{
  "message": "success"
}
```

### Exemple de réponse en erreur {#example-error-response}

La classe de codes de statut `4XX` indique une erreur côté client. Consultez l'article [Erreurs et réponses de l'API]({{site.baseurl}}/api/errors) pour plus d'informations sur les erreurs que vous pouvez rencontrer.

Le code de statut `400` pourrait renvoyer le corps de réponse suivant.

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}