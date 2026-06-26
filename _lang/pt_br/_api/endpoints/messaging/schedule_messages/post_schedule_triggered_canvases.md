---
nav_title: "POST: Agendar Canvas disparados por API"
article_title: "POST: Agendar Canvas disparados por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Agendar Canvas disparados por API\"."

---
{% api %}
# Agendar Canvas disparados por API {#schedule-api-triggered-canvases}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/canvas/trigger/schedule/create
{% endapimethod %}

> Use este endpoint para agendar mensagens do Canvas via entrega disparada por API, permitindo que você decida qual ação deve disparar o envio da mensagem.

Você pode passar `context`, que será aplicado como modelo nas mensagens enviadas pelas primeiras etapas do Canvas.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

Para enviar mensagens com este endpoint, você precisa ter um [ID do Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier), criado quando você constrói um Canvas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4bc75890-b807-405d-b226-5aca284e6b7d {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `canvas.trigger.schedule.create`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='send endpoints' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, array of recipients object),
  // for any keys that conflict between these trigger properties and those in a Recipients Object, the value from the
  // Recipients Object will be used
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the Canvas
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "context": (optional, object) personalization key-value pairs for the first step for all users in this send; see trigger properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Obrigatória | String | Consulte [identificador do Canvas]({{site.baseurl}}/api/identifier_types/). |
| `recipients` | Opcional | Vetor de objetos de destinatários | Consulte [objeto de destinatários]({{site.baseurl}}/api/objects_filters/recipient_object/). |
| `audience` | Opcional | Objeto de público conectado | Consulte [público conectado]({{site.baseurl}}/api/objects_filters/connected_audience/). |
| `broadcast` | Opcional | Booleano | Você deve definir `broadcast` como true ao enviar uma mensagem para um segmento inteiro segmentado por uma Campaign ou Canvas. O padrão desse parâmetro é false (a partir de 31 de agosto de 2017). <br><br> Se `broadcast` estiver definido como true, uma lista `recipients` não poderá ser incluída. No entanto, tenha cuidado ao definir `broadcast: true`, pois definir esse flag de forma não intencional pode fazer com que você envie sua mensagem para um público maior do que o esperado. |
| `context` | Opcional | Objeto | Pares de chave-valor de personalização para todos os usuários neste envio. Consulte [objeto de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/). |
| `schedule` | Obrigatória | Objeto de agendamento | Consulte [objeto de agendamento]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "context": {}
    }
  ],
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "broadcast": false,
  "context": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
```

## Resposta {#response}

### Exemplo de resposta bem-sucedida {#example-success-response}

```
Content-Type: application/json
Authorization: Bearer YOUR-API-KEY-HERE
{
{
    "dispatch_id": "dispatch_identifier",
    "schedule_id": "schedule_identifier",
    "message": "success"
}
```

{% endapi %}