---
nav_title: "POST: Criar e atualizar usuários (síncrono)"
article_title: "POST: Criar e atualizar usuários (síncrono)"
alias: /post_user_track_synchronous/
layout: api_page
page_order: 4.5
page_type: reference
description: "Este artigo detalha o endpoint síncrono de rastreamento de usuários da Braze."

---
{% api %}
# Criar e atualizar usuários (síncrono) {#create-and-update-users-synchronous}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/sync
{% endapimethod %}

> Use esse endpoint para registrar eventos personalizados e compras e atualizar atributos do perfil de usuário de forma síncrona. Esse endpoint funciona de forma semelhante ao [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), que atualiza perfis de usuário de forma assíncrona.

{% alert important %}
Este endpoint está atualmente em **beta limitado**. Embora não estejamos adicionando novos clientes ao beta neste momento, informe ao seu gerente de conta da Braze se você acha que esse recurso pode ser útil para a sua integração com a Braze.
{% endalert %}

## Chamadas síncronas e assíncronas à API {#synchronous-and-asynchronous-api-calls}

Em uma chamada assíncrona, a API retorna o código de status `201`, indicando que sua solicitação foi recebida, compreendida e aceita com sucesso. No entanto, isso não significa que sua solicitação tenha sido totalmente concluída.

Em uma chamada síncrona, a API retorna o código de status `201`, indicando que sua solicitação foi recebida, compreendida, aceita e concluída com sucesso. A resposta da chamada mostra campos selecionados do perfil do usuário como resultado da operação.

Esse endpoint tem um limite de taxa menor do que o endpoint `/users/track` (consulte o [limite de taxa](#rate-limit) abaixo). Cada solicitação `/users/track/sync` pode conter apenas um objeto de evento, um objeto de atributo **ou** um objeto de compra. Esse endpoint deve ser reservado para atualizações de perfil de usuário em que uma chamada síncrona é necessária. Para uma implementação saudável, recomendamos usar `/users/track/sync` e `/users/track` juntos.

Por exemplo, se você estiver enviando solicitações consecutivas para o mesmo usuário em um curto período de tempo, condições de corrida são possíveis com o endpoint assíncrono `/users/track`, mas com o endpoint `/users/track/sync` você pode enviar essas solicitações em sequência, cada uma após receber uma resposta `2XX`.

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key) com a permissão `users.track.sync`.

Os clientes que usam a API para chamadas de servidor para servidor podem precisar adicionar `rest.iad-01.braze.com` à lista de permissões se estiverem protegidos por um firewall.

## Limite de taxa {#rate-limit}

{% multi_lang_include api/user_track_custom_attributes_data_points.md endpoint="/users/track/sync" %}

Aplicamos um limite de velocidade base de 500 solicitações por minuto para esse endpoint para todos os clientes. Cada solicitação `/users/track/sync` pode conter até um objeto de evento, um objeto de atributo ou um objeto de compra. Cada objeto (evento, atributo e arrays de compra) pode atualizar um usuário cada.

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, one attributes object),
  "events": (optional, one event object),
  "purchases": (optional, one purchase object),
}
```

### Parâmetros de solicitação {#request-parameters}

{% alert important %}
Para cada componente de solicitação listado na tabela a seguir, você deve incluir um dos seguintes: `external_id`, `user_alias`, `braze_id`, `email` ou `phone`.
{% endalert %}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `attributes` | Opcional | Um objeto de atributos | Consulte o [objeto de atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens) |
| `events` | Opcional | Um objeto de evento | Consulte o [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object) |
| `purchases` | Opcional | Um objeto de compra | Consulte o [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Respostas {#responses}

Ao usar os [parâmetros de solicitação](#request-parameters) desse endpoint, você deve receber uma das seguintes respostas: uma mensagem de sucesso ou uma mensagem com erros fatais.

### Mensagem de sucesso {#successful-message}

Mensagens de sucesso retornam a seguinte resposta, que inclui informações sobre os dados do perfil de usuário que a Braze atualizou.

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Braze lists only custom attributes from the request,
        "custom_events": (optional, object), the custom events as a result of the request. Braze lists only custom events from the request,
        "purchase_events": (optional, object), the purchase events as a result of the request. Braze lists only purchase events from the request,
    },
    "message": "success"
```

### Mensagem com erros fatais {#message-with-fatal-errors}

Se sua mensagem tiver um erro fatal, você receberá a seguinte resposta:

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

## Exemplos de solicitações e respostas {#example-requests-and-responses}

### Atualizar um atributo personalizado por ID externo {#update-a-custom-attribute-by-external-id}

#### Solicitação {#request}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
```

#### Resposta {#response}

```
{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
}
```

### Atualizar um evento personalizado por e-mail {#update-a-custom-event-by-email}

#### Solicitação

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "events": [
        {
            "email": "test@example.com",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2022-12-06T19:20:45+01:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "2022"
                },
                "cast": [
                    {
                        "name": "Actor1"
                    },
                    {
                        "name": "Actor2"
                    }
                ]
            }
        }
    ]
}'
```

#### Resposta

```
{
    "users": [
        {
            "email": "test@example.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
}
```

### Atualizar um evento de compra por alias de usuário {#update-a-purchase-event-by-user-alias}

#### Solicitação

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : {
          "alias_name" : "device123",
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            {
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
```

#### Resposta

```
{
    "users": [
        {
          "user_alias" : {
            "alias_name" : "device123",
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
}
```

## Perguntas frequentes {#frequently-asked-questions}

### Devo usar o endpoint assíncrono ou síncrono? {#should-i-use-the-asynchronous-or-synchronous-endpoint}

Para a maioria das atualizações de perfil, o endpoint `/users/track` funciona melhor devido ao seu limite de taxa mais alto e à flexibilidade para agrupar solicitações em lote. No entanto, o endpoint `/users/track/sync` é útil se você estiver enfrentando condições de corrida devido a solicitações rápidas e consecutivas para o mesmo usuário.

### O tempo de resposta é diferente do endpoint `/users/track`? {#does-the-response-time-differ-from-the-userstrack-endpoint}

Com uma chamada síncrona, a API espera até que a Braze conclua a solicitação para retornar uma resposta. Como resultado, solicitações síncronas levam mais tempo em média do que solicitações assíncronas para `/users/track`. Para a maioria das solicitações, você pode esperar uma resposta em segundos.

### Posso enviar várias solicitações ao mesmo tempo? {#can-i-send-multiple-requests-at-the-same-time}

Sim, desde que as solicitações sejam para usuários diferentes ou que cada solicitação atualize atributos, eventos ou compras diferentes para um mesmo usuário.

Se você estiver enviando várias solicitações para um mesmo usuário, para o mesmo atributo, evento ou compra, a Braze recomenda aguardar uma resposta bem-sucedida entre cada solicitação para evitar a ocorrência de condições de corrida.

### Por que o valor da resposta não corresponde ao da minha solicitação original? {#why-doesnt-the-response-value-match-the-one-in-my-original-request}

Embora sua solicitação tenha sido concluída, é possível que o valor do atributo personalizado não tenha sido atualizado. Isso pode acontecer quando a atualização do atributo personalizado excede o número máximo de caracteres, excede os limites do array ou se o usuário não existe na Braze e você definiu `_update_existing_only = true`.

Nessas situações, considere a resposta como um sinal de que sua solicitação foi concluída, mas a atualização desejada não foi efetuada. Investigue os possíveis motivos descritos acima para solucionar o problema.

{% endapi %}