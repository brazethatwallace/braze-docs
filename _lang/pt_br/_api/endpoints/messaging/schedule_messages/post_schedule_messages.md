---
nav_title: "POST: Criar envios de mensagens programadas"
article_title: "POST: Criar envios de mensagens programadas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para criar mensagens programadas."

---
{% api %}
# Criar envios de mensagens programadas {#create-scheduled-messages}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/messages/schedule/create
{% endapimethod %}

> Use esse endpoint para programar o envio de uma Campaign, Canvas ou outra mensagem em um horário designado e obter um identificador para referenciar essa mensagem em atualizações futuras.

Se você estiver direcionando um segmento, um registro da sua solicitação será armazenado no [Console de desenvolvedor](https://dashboard.braze.com/app_settings/developer_console/activitylog/) após o envio de todas as mensagens programadas.

{% alert tip %}
Se você deseja enviar mensagens imediatamente para usuários designados, use o [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) em vez disso.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#25272fb8-bc39-41df-9a41-07ecfd76cb1d {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `messages.schedule.create`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' category='send messages endpoints' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
  // Including 'segment_id' will send to members of that segment
  // Including 'external_user_ids' and/or 'user_aliases' will send to those users
  // Including both a Segment and users will send to the provided users if they are in the segment
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if users are not specified,
  "external_user_ids": (optional, array of strings) see external user identifier,
  "user_aliases": (optional, array of user alias object) see user alias,
  "audience": (optional, connected audience object) see connected audience,
  "campaign_id": (optional, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "override_messaging_limits": (optional, bool) ignore frequency capping rules, defaults to false,
  "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  },
  "messages": {
    "apple_push": (optional, apple push object),
    "android_push": (optional, android push object),
    "kindle_push": (optional, kindle/fireOS push object),
    "web_push": (optional, web push object),
    "email": (optional, email object),
    "webhook": (optional, webhook object),
    "content_card": (optional, content card object),
    "sms": (optional, SMS object)
  }
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `broadcast` | Opcional | Booleano | Você deve definir `broadcast` como true ao enviar uma mensagem para um segmento inteiro segmentado por uma Campaign ou Canvas. O padrão desse parâmetro é `false`. <br><br> Se `broadcast` estiver definido como `true`, não será possível incluir uma lista de destinatários. No entanto, tenha cuidado ao definir `broadcast: true`, pois definir essa flag inadvertidamente pode fazer com que você envie sua mensagem para um público maior do que o esperado. |
| `external_user_ids` | Opcional | Matriz de strings | Consulte [identificador de usuário externo]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields). |
| `user_aliases` | Opcional | Matriz de objetos de alias de usuário | Consulte o [objeto de alias de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object). |
| `audience` | Opcional | Objeto de público conectado | Consulte [público conectado]({{site.baseurl}}/api/objects_filters/connected_audience). |
| `segment_id` | Opcional | String | Consulte [identificador de segmento]({{site.baseurl}}/api/identifier_types). |
| `campaign_id` | Opcional | String | Consulte [identificador de campanha]({{site.baseurl}}/api/identifier_types). |
| `send_id` | Opcional | String | Consulte [identificador de envio]({{site.baseurl}}/api/identifier_types). |
| `override_messaging_limits` | Opcional | Booleano | Ignorar o limite de frequência para campanhas; o padrão é false |
| `recipient_subscription_state` | Opcional | String | Use essa opção para enviar mensagens apenas para usuários que tenham aceitado receber mensagens (`opted_in`), apenas para usuários que tenham feito a inscrição ou aceitado receber mensagens (`subscribed`) ou para todos os usuários, inclusive os que cancelaram a inscrição (`all`). <br><br>O uso de `all` é útil para envio de e-mail de transação. O padrão é `subscribed`. |
| `schedule` | Obrigatório | Objeto de programação | Consulte [objeto de programação]({{site.baseurl}}/api/objects_filters/schedule_object) |
| `messages` | Opcional | Objeto de envio de mensagens | Consulte os [objetos de envio de mensagens disponíveis]({{site.baseurl}}/api/objects_filters#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/create' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name" : "example_name",
    "alias_label" : "example_label"
  },
  "segment_id": "segment_identifiers",
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
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "override_messaging_limits": false,
  "recipient_subscription_state": "subscribed",
  "schedule": {
    "time": "",
    "in_local_time": true,
    "at_optimal_time": true
  },
  "messages": {
    "apple_push": (optional, Apple Push Object),
    "android_push": (optional, Android Push Object),
    "kindle_push": (optional, Kindle/FireOS Push Object),
    "web_push": (optional, Web Push Object),
    "email": (optional, Email object)
    "webhook": (optional, Webhook object)
    "content_card": (optional, Content Card Object)
  }
}'
```

## Resposta {#response}

### Exemplo de resposta bem-sucedida {#example-success-response}

```json
{
    "dispatch_id": (string) the dispatch identifier,
    "schedule_id": (string) the schedule identifier,
    "message": "success"
}
```

{% endapi %}