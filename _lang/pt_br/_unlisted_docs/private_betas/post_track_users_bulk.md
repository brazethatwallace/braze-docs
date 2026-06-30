---
nav_title: "POST: Rastrear usuários (em massa)"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk/
description: "Este artigo descreve detalhes sobre o endpoint Rastrear usuários (em massa)."
---

{% api %}
# Rastrear usuários (em massa) {#track-users-bulk}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

> Use este endpoint para registrar eventos personalizados e compras e atualizar atributos de perfis de usuário em massa.

{% alert important %}
Este endpoint está atualmente em beta. Entre em contato com o gerente da sua conta Braze se tiver interesse em participar do beta.
{% endalert %}

## Quando usar este endpoint {#when-to-use-this-endpoint}

Semelhante ao [POST: endpoint Rastrear usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites), você pode usar este endpoint para atualizar perfis de usuário. No entanto, este endpoint é mais adequado para atualizações em massa:

- **Solicitações maiores:** Este endpoint permite 10.000 usuários por solicitação, o que significa que você precisa fazer menos solicitações para atender às suas necessidades de atualização em massa.
- **Priorização:** Durante condições de pico de tráfego, as solicitações de `/users/track` serão priorizadas em relação às solicitações de `/users/track/bulk`. Usar ambos os endpoints oferece mais controle sobre a ingestão de dados.

Considere usar este endpoint quando estiver preenchendo muitos perfis de usuário durante a integração ou sincronizando grandes volumes de perfis de usuário como parte de uma sincronização diária.

{% alert note %}
A partir de 26 de maio de 2025, este endpoint pode ser usado para rastrear métricas de conversão, bem como disparar eventos de exceção ou Campaigns e Canvas baseados em ação. Esse comportamento é semelhante a qualquer outro método de ingestão de dados da Braze.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma chave de API com a permissão `users.track.bulk`.

Se estiver usando a API para chamadas servidor-a-servidor, talvez seja necessário adicionar o endpoint à lista de permissões (por exemplo, `rest.iad-01.braze.com`) se estiver atrás de um firewall. Consulte os [endpoints por instância]({{site.baseurl}}/api/basics/#endpoints) para mais informações.

## Limite de taxa {#rate-limit}

Aplicamos um limite de velocidade base de 5 solicitações por segundo a este endpoint para todos os clientes.

Cada solicitação `/users/track/bulk` tem um limite de carga útil de 4&nbsp;MB e pode conter até 10.000 objetos de evento, atributo ou compra.

Cada objeto (arrays de evento, atributo e compra) pode atualizar um usuário cada, o que significa que até 10.000 usuários diferentes podem ser atualizados em uma única solicitação. Um único perfil de usuário pode ser atualizado com até 100 objetos em uma única solicitação.

{% alert note %}
Se precisar aumentar seu limite de taxa, entre em contato com o gerente de sucesso do cliente.
{% endalert %}


## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### Parâmetros da solicitação {#request-parameters}

{% alert important %}
Para cada componente da solicitação listado na tabela a seguir, um dos seguintes é obrigatório: `external_id`, `user_alias`, `braze_id`, `email` ou `phone`.
{% endalert %}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `attributes` | Opcional | Array de objetos de atributos | Consulte [objeto de atributos de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Opcional | Array de objetos de evento | Consulte [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Opcional | Array de objetos de compra | Consulte [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplos de solicitações {#example-requests}

### Atualizar 10.000 perfis de usuário em massa em uma solicitação {#bulk-update-10000-user-profiles-in-one-request}

Você pode atualizar até 10.000 perfis de usuário. Aqui está um exemplo resumido em que a solicitação consiste em 10.000 objetos de atributo:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        },
        {
            "external_id": "user2",
            "string_attribute": "vegetables",
            "boolean_attribute_1": false,
            "integer_attribute": 25,
            "array_attribute": [
                "broccoli",
                "asparagus",
            ]
        },

...

        {
            "external_id": "user10000",
            "string_attribute": "nuts",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "hazelnut",
                "pistachio"
            ]
        }
    ]
}'
```

Aqui está um exemplo em que a solicitação consiste em objetos de atributo e de evento:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "external_id": "user2",
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
        },
...
        {
            "external_id": "user10000",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2023-09-16T08:00:00+10:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "1988"
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

## Respostas {#responses}

### Mensagens bem-sucedidas {#successful-messages}

Mensagens bem-sucedidas receberão a seguinte resposta:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### Mensagem bem-sucedida com erros não fatais {#successful-message-with-non-fatal-errors}

Se sua mensagem for bem-sucedida, mas tiver erros não fatais, como um objeto de evento inválido em uma longa lista de eventos, você receberá a seguinte resposta:

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
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

#### Códigos de resposta de erros fatais {#fatal-error-response-codes}

Para códigos de status e mensagens de erro associadas que serão retornados se sua solicitação encontrar um erro fatal, consulte [Erros fatais e respostas]({{site.baseurl}}/api/errors/#fatal-errors).

Se você receber o erro `provided external_id is blacklisted and disallowed`, sua solicitação pode ter incluído um "usuário fictício". Para saber mais, consulte [Bloqueio de spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Perguntas frequentes {#frequently-asked-questions}

### Devo usar este endpoint ou o `/users/track` regular? {#should-i-use-this-endpoint-or-regular-userstrack}

Recomendamos usar ambos.

- Para preenchimentos e sincronizações de perfis de usuário em grande volume, use o endpoint `/users/track/bulk`.
- Para casos de uso em tempo real, use o endpoint `/users/track`.

### Quais identificadores posso usar em /users/track/bulk? {#what-identifiers-can-i-use-in-userstrackbulk}

Um dos seguintes é obrigatório: `external_id`, `braze_id`, `user_alias`, `email` ou `phone`. Para mais exemplos, consulte nossa documentação sobre [objeto de atributos de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/), [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) ou [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/).

### Posso incluir atributos, eventos e compras em uma única solicitação? {#can-i-include-attributes-events-and-purchases-in-one-request}

Sim. Você pode construir sua solicitação com qualquer quantidade de objetos de atributos, eventos e compras, até 10.000 objetos por solicitação.


{% endapi %}