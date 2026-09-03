---
nav_title: "POST: Atualizar atividade ao vivo"
article_title: "POST: Atualizar atividade ao vivo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint \"Atualizar atividade ao vivo\"."

---
{% api %}
# Atualizar atividade ao vivo {#update-live-activity}
{% apimethod post %}
/messages/live_activity/update
{% endapimethod %}

> Use este endpoint para atualizar e encerrar [atividades ao vivo]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?sdktab=swift) exibidas pelo seu app iOS. Este endpoint requer configuração adicional.

Depois de registrar uma atividade ao vivo, você pode passar uma carga útil JSON para atualizar seu serviço de Notificações por Push da Apple (APNs). Consulte a documentação da Apple sobre [atualizar sua atividade ao vivo com cargas úteis de notificação por push](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications) para saber mais.

Se `content-available` não estiver definido, a prioridade padrão do serviço de Notificações por Push da Apple (APNs) é 10. Se `content-available` estiver definido, essa prioridade é 5. Consulte [objeto de push da Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object) para mais detalhes.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará concluir o seguinte:

- Gerar uma chave de API com a permissão `messages.live_activity.update`.
- Registrar uma atividade ao vivo [remotamente]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?tab=remote&sdktab=swift) ou [localmente]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?tab=local&sdktab=swift) usando o SDK Swift da Braze.

{% multi_lang_include api/payload_size_alert.md %}

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação {#request-body}

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
| `activity_id` | Required | String | When you register your Live Activity using [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class), you use the `pushTokenTag` parameter to name the Activity's push token to a custom string.<br><br>Set `activity_id` to this custom string to define which Live Activity you want to update. |
| `content_state` | Required | Object | You define the `ContentState` parameters when you create your Live Activity. Pass the updated values for your `ContentState` using this object.<br><br>The format of this request must match the shape you initially defined. |
| `end_activity` | Optional | Boolean | If `true`, this request ends the Live Activity. |
| `dismissal_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | This parameter defines the time to remove the Live Activity from the user's UI. If this time is in the past and `end_activity` is `true`, the Live Activity will be removed immediately.<br><br> If `end_activity` is `false` or omitted, this parameter only updates the Live Activity.|
| `stale_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | This parameter tells the system when the Live Activity content is marked as outdated in the user's UI. |
| `notification` | Optional | Object | Include an [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object) object to define a push notification. The behavior of this push notification depends on if the user is active or if the user is using a proxy device. {::nomarkdown}<ul><li>If a <code>notification</code> is included and the user is active on their iPhone when the update is delivered, the updated Live Activity UI will slide down and display like a push notification.</li><li>If a <code>notification</code> is included and the user is not active on their iPhone, their screen will light up to display the updated Live Activity UI on their lock screen.</li><li>The <code>notification alert</code> will not display as a standard push notification. Additionally, if a user has a proxy device, like an Apple Watch, the <code>alert</code> will be displayed there.</li></ul>{:/} |
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

## Resposta {#response}

Existem dois códigos de status para este endpoint: `201` e `4XX`.

### Exemplo de resposta bem-sucedida {#example-success-response}

Um código de status `201` é retornado se a solicitação foi formatada corretamente e a recebemos. O código de status `201` pode retornar o seguinte corpo de resposta.

```json
{
  "message": "success"
}
```

### Exemplo de resposta de erro {#example-error-response}

A classe de código de status `4XX` indica um erro do cliente. Consulte o artigo [erros e respostas da API]({{site.baseurl}}/api/errors) para saber mais sobre os erros que você pode encontrar.

O código de status `400` pode retornar o seguinte corpo de resposta.

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}