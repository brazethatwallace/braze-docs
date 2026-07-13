---
nav_title: "POST: Criar e atualizar usuários (em massa)"
article_title: "POST: Criar e atualizar usuários (em massa)"
search_tag: Endpoint
page_order: 4.25
layout: api_page
page_type: reference
alias:
  - /unlisted_docs/track_users_bulk_partners/
  - /api/endpoints/user_data/post_user_track_bulk_partners/
description: "Este artigo descreve detalhes sobre o endpoint de rastreamento de usuários em massa."
---
{% api %}
# Criar e atualizar usuários (em massa) {#create-and-update-users-bulk}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

Use este endpoint para registrar eventos personalizados e compras, além de atualizar atributos de perfis de usuário em massa.

{% alert important %}
Este endpoint está atualmente em **beta limitado**. Embora não estejamos adicionando novos clientes ao beta no momento, informe seu gerente de conta da Braze se você achar que esse recurso pode ser útil para sua integração com a Braze.
{% endalert %}

## Quando usar este endpoint {#when-to-use-this-endpoint}

Assim como o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), você pode usar este endpoint para atualizar perfis de usuário. Este endpoint é mais adequado para atualizações em massa:

- **Solicitações maiores:** envie até 1.000 usuários por solicitação, permitindo que você faça menos solicitações para grandes preenchimentos retroativos e sincronizações.
- **Priorização:** durante condições de pico de tráfego, as solicitações para `/users/track` são priorizadas em relação às solicitações para `/users/track/bulk`.

Use este endpoint quando estiver preenchendo retroativamente muitos perfis de usuário durante a integração, ou sincronizando grandes volumes de perfis como parte de uma sincronização diária.

{% alert note %}
Os limites do objeto de solicitação do endpoint `/users/track` variam de acordo com o modelo de preços e a configuração. Use `/users/track/bulk` para ingestão em massa.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/api_key) com a permissão `users.track.bulk`.

Se você estiver fazendo chamadas servidor-a-servidor atrás de um firewall, pode ser necessário adicionar seu endpoint REST da Braze à lista de permissões (por exemplo, `rest.iad-01.braze.com`). Para saber mais, consulte [Endpoints de API]({{site.baseurl}}/api/basics#api-definitions).

## Limite de taxa {#rate-limit}

{% multi_lang_include api/user_track_custom_attributes_data_points.md endpoint="/users/track/bulk" %}

Para a maioria dos clientes, este endpoint tem um limite de velocidade base de 50 solicitações por segundo.

Clientes com contratos mais recentes podem ter limites de pico (por segundo) e estáveis (por hora) baseados nos usuários ativos mensais contratados.

Cada solicitação `/users/track/bulk` tem um limite de carga útil de 2 MB e pode incluir até 1.000 objetos no total entre atributos, eventos e compras, dependendo da política de limite de taxa em massa da sua conta.

Cada objeto pode atualizar um usuário, então uma única solicitação pode atualizar até o limite de objetos de solicitação da sua conta de usuários diferentes. Além disso, cada solicitação pode conter no máximo 100 objetos por perfil de usuário entre atributos, eventos e compras.

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object)
}
```

### Parâmetros da solicitação {#request-parameters}

{% alert important %}
Para cada objeto de solicitação, você deve incluir um dos seguintes: `external_id`, `user_alias`, `braze_id`, `email` ou `phone`.
{% endalert %}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `attributes` | Opcional | Array de objetos de atributos | Consulte [objeto de atributos de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object) |
| `events` | Opcional | Array de objetos de eventos | Consulte [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object) |
| `purchases` | Opcional | Array de objetos de compras | Consulte [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros da solicitação" }

## Exemplos de solicitações {#example-requests}

### Atualizar perfis de usuário em massa em uma única solicitação {#bulk-update-user-profiles-in-one-request}

Atualize até o limite de objetos de solicitação da sua conta de perfis de usuário em uma única solicitação.

```
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
        "asparagus"
      ]
    }
  ]
}'
```

### Enviar atributos e eventos em uma única solicitação {#send-attributes-and-events-in-one-request}

Inclua atributos e eventos na mesma solicitação, até o limite total de objetos da sua conta.

```
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
    }
  ]
}'
```

## Respostas {#responses}

### Mensagem de sucesso {#successful-message}

Mensagens de sucesso retornam a seguinte resposta:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external IDs with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing
}
```

### Mensagem de sucesso com erros não fatais {#successful-message-with-non-fatal-errors}

Se sua solicitação for bem-sucedida, mas tiver erros não fatais (por exemplo, um objeto de evento inválido em um lote grande), você receberá a seguinte resposta:

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

Se sua solicitação tiver um erro fatal, você receberá a seguinte resposta:

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

### Códigos de resposta de erros fatais {#fatal-error-response-codes}

Para códigos de status e mensagens de erro associadas que a Braze retorna quando sua solicitação tem um erro fatal, consulte [Erros fatais e respostas]({{site.baseurl}}/api/errors#fatal-errors).

Se você receber o erro "provided external_id is blacklisted and disallowed", sua solicitação pode incluir um "usuário fictício". Para saber mais, consulte [Bloqueio de spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#spam-blocking).

## Perguntas frequentes {#frequently-asked-questions}

### Devo usar este endpoint ou `/users/track`? {#should-i-use-this-endpoint-or-userstrack}

Use ambos os endpoints com base no seu caso de uso:

- Para grandes preenchimentos retroativos e sincronizações, use `/users/track/bulk`.
- Para casos de uso em tempo real, use `/users/track`.

### Quais identificadores posso usar em `/users/track/bulk`? {#what-identifiers-can-i-use-in-userstrackbulk}

Para cada objeto de solicitação, inclua um dos seguintes: `external_id`, `braze_id`, `user_alias`, `email` ou `phone`.

### Posso incluir atributos, eventos e compras em uma única solicitação? {#can-i-include-attributes-events-and-purchases-in-one-request}

Sim. Inclua qualquer combinação de atributos, eventos e compras, até o limite combinado de objetos de solicitação da sua conta.

{% endapi %}