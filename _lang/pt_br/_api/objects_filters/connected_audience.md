---
nav_title: "Filtro e objeto do público conectado"
article_title: Objeto do público conectado à API
page_order: 3
page_type: reference
description: "Este artigo explica o objeto de público conectado, incluindo como ele funciona, casos de uso e os diferentes filtros que o compõem."
---

# Objeto de público conectado {#connected-audience-object}

> Um público conectado é um filtro de público dinâmico que você define inline na sua requisição de API, permitindo direcionar os usuários certos no momento do envio sem precisar criar ou gerenciar Segments no dashboard da Braze.

Em vez de pré-criar um Segment para cada combinação possível de público, você passa os critérios de filtro diretamente na sua chamada de API. Dependendo do endpoint, esse objeto é passado como `audience` ou `custom_audience`. A Braze avalia cada usuário em relação a esses critérios em tempo real e entrega a mensagem apenas aos usuários que correspondem. Isso significa que uma única Campaign, Canvas ou definição de mensagem somente via API pode atender a um número ilimitado de variações de público, totalmente orientadas pela sua lógica de negócios.

## Como funciona {#how-it-works}

1. Defina sua mensagem criando uma Campaign ou um Canvas disparado por API no dashboard da Braze, ou defina o conteúdo da mensagem inteiramente inline usando os [objetos de mensagem]({{site.baseurl}}/api/objects_filters#messaging-objects) na sua requisição de API. Use [propriedades de disparo]({{site.baseurl}}/api/objects_filters/trigger_properties_object) ou [contexto do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) para personalização dinâmica.
2. Faça uma chamada a um endpoint compatível e inclua seus filtros de público conectado no parâmetro `audience`, ou em `custom_audience` para `/messages/live_activity/start`. Você pode filtrar por atributos personalizados, status de inscrição em push, status de inscrição em e-mail e horário do último uso do app.
3. A Braze avalia os filtros no momento do envio, entregando a mensagem apenas aos usuários que correspondem aos seus critérios.

{% alert tip %}
Um `campaign_id` não é necessário ao usar o parâmetro `audience`. Os endpoints [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) e [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages) permitem definir o conteúdo da mensagem inline sem uma Campaign pré-criada. No entanto, se você quiser rastrear métricas no nível da Campaign (como envios, cliques ou bounces) no dashboard, inclua um `campaign_id`.
{% endalert %}

Como o público é definido por requisição, seus sistemas de backend podem disparar mensagens contextualmente relevantes em resposta a qualquer evento de negócio (uma mudança de preço, um alerta meteorológico, uma atualização de placar ao vivo) sem intervenção no dashboard.

### Endpoints compatíveis {#compatible-endpoints}

Você pode usar o objeto de público conectado nos seguintes endpoints:

- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) (usa `custom_audience`)

Observe que o parâmetro `audience` não aceita array de objetos.

## Casos de uso {#use-cases}

Use públicos conectados para cenários em que seus sistemas de backend detectam um evento e precisam notificar um conjunto de usuários determinado dinamicamente:

| Categoria | Exemplo |
| --- | --- |
| Alertas meteorológicos | Um provedor de dados meteorológicos detecta um evento climático severo e envia notificações por push para usuários cujo atributo `preferred_city` corresponde à área afetada. |
| Esportes e eventos ao vivo | Um app de esportes envia atualizações de placar em tempo real ou alertas de partidas para usuários cujo atributo `favorite_team` corresponde a um dos times em campo. |
| Conteúdo e entretenimento | Um serviço de streaming notifica usuários cujo array `favorite_shows` inclui o título de uma série sempre que um novo episódio é lançado. |
| E-commerce | Um varejista online envia alertas de queda de preço ou de reposição de estoque para usuários cujo array `wishlisted_products` inclui o ID do produto relevante. |
| Viagens | Um app de viagens envia notificações de atraso de voo para usuários cujo atributo `booked_flight` corresponde ao número do voo afetado. |
| Serviços financeiros | Uma plataforma de negociação alerta usuários cujo array `watchlist` inclui um ticker de ação que ultrapassou um limite de preço. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

Em cada caso, uma única Campaign ou definição de mensagem somente via API lida com todas as variações. Seu backend determina os valores do filtro e os passa na requisição da API, então você não precisa criar um Segment ou Campaign separado para cada produto, série, time ou local.

## Exemplo de solicitação {#example-request}

O exemplo a seguir usa o endpoint [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) para direcionar usuários que favoritaram um programa específico e aceitaram receber notificações por push:

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_shows",
          "comparison": "includes_value",
          "value": "Example Show"
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
  "trigger_properties": {
    "show_title": "Example Show",
    "episode_title": "Season 3, Episode 1",
    "deep_link": "https://example.com/shows/example-show/s3e1"
  },
  "broadcast": false
}
```

## Corpo do objeto {#object-body}

O objeto de público conectado é composto por um único filtro de público conectado ou por vários filtros de público conectado combinados com os operadores `AND` e `OR`.

**Exemplo com vários filtros:**

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## Filtros de público conectado {#connected-audience-filters}

Combine vários filtros com os operadores `AND` e `OR` para criar um filtro de público conectado.

### Considerações {#considerations}

Os públicos conectados não podem filtrar usuários por:

 - Atributos padrão
 - Eventos personalizados
 - Segments
 - Eventos de engajamento com mensagem
 - Atributos personalizados aninhados

Para usar esses filtros, recomendamos incorporá-los a um Segment de público e, em seguida, especificar esse Segment no parâmetro `segment_id` do [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters). Ao usar outros endpoints, você deve primeiro adicionar o Segment à Campaign ou ao Canvas disparado por API no dashboard da Braze. Se você precisar filtrar por atributos aninhados, use um [Segment padrão]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).


### Filtro de atributo personalizado {#custom-attribute-filter}

Esse filtro permite segmentar com base em um atributo personalizado do usuário. Esses filtros contêm até três campos:

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### Comparações permitidas por tipo de dados {#allowed-comparisons-by-data-type}

O tipo de dados do atributo personalizado determina quais comparações são válidas para um determinado filtro.

| Tipo de atributo personalizado | Comparações permitidas |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Array | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Numérico | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Booleano | `equals`, `not_equal`, `exists`, `does_not_exist` |
| Hora | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparações permitidas por tipo de dados" }

#### Ressalvas sobre comparações de atributos {#attribute-comparison-caveats}

| Comparação | Considerações adicionais |
| --- | --- |
| `value` | O `value` não é obrigatório ao usar as comparações `exists` ou `does_not_exist`. O `value` deve ser uma string de data/hora no formato ISO 8601 ao usar as comparações `before` e `after`. |
| `matches_regex` | Ao usar a comparação `matches_regex`, o valor informado deve ser uma string. Para saber mais sobre como usar expressões regulares na Braze, consulte [Expressões regulares]({{site.baseurl}}/user_guide/audience/segments/regex) e [Tipos de dados de atributos personalizados]({{site.baseurl}}/developer_guide/analytics#custom-attribute-data-types). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ressalvas sobre comparações de atributos" }

#### Comparações com múltiplos valores {#multi-value-comparisons}

Tanto `is_any_of` quanto `is_none_of` suportam correspondência com múltiplos valores em uma única comparação. Essas comparações funcionam com atributos personalizados do tipo string e array.

- `is_any_of`: Corresponde a usuários cujo valor do atributo é igual a qualquer um dos valores fornecidos. O `value` pode ser uma única string ou um array de strings.
- `is_none_of`: Corresponde a usuários cujo valor do atributo não corresponde a nenhum dos valores fornecidos. O `value` pode ser uma única string ou um array de strings. Observe que usuários que não possuem o atributo em seu perfil sempre se qualificam para essa comparação.

Para atributos do tipo array:

- `includes_value` também pode aceitar um array de valores para verificar se o array do usuário contém qualquer um dos valores especificados.
- Ao usar `is_any_of` ou `is_none_of` com atributos do tipo array, eles funcionam da mesma forma que `includes_value` e `does_not_include_value`, respectivamente.

{% alert tip %}
Para correspondência com múltiplos valores, use `is_any_of` em vez de `includes_value`.
{% endalert %}

#### Exemplos de atributos personalizados {#custom-attribute-examples}

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```

#### Exemplos de comparações com múltiplos valores {#multi-value-comparison-examples}

##### `is_any_of` com um array de strings {#is_any_of-with-an-array-of-strings}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_color",
    "comparison": "is_any_of",
    "value": ["red", "blue", "green"]
  }
}
```

##### `is_none_of` com um array de strings {#is_none_of-with-an-array-of-strings}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscription_tier",
    "comparison": "is_none_of",
    "value": ["bronze", "silver"]
  }
}
```

##### `includes_value` com um array (atributo do tipo array) {#includes_value-with-an-array-array-attribute}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscribed_products",
    "comparison": "includes_value",
    "value": ["1001", "1002", "1003"]
  }
}
```

Isso corresponde a usuários cujo array `subscribed_products` contém qualquer um dos valores `"1001"`, `"1002"` ou `"1003"`.

### Filtro de inscrição para push {#push-subscription-filter}

Esse filtro permite segmentar com base no status de inscrição para push do usuário.

#### Corpo do filtro {#filter-body}

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Comparações permitidas:** `is`, `is_not`
- **Valores permitidos:** `opted_in`, `subscribed`, `unsubscribed`

### Filtro de inscrição para e-mail {#email-subscription-filter}

Esse filtro permite segmentar com base no status de inscrição para e-mail do usuário.

#### Corpo do filtro

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Comparações permitidas:** `is`, `is_not`
- **Valores permitidos:** `opted_in`, `subscribed`, `unsubscribed`

### Filtro de último uso do app {#last-used-app-filter}

Esse filtro permite segmentar com base na última vez que o usuário usou o app. Esses filtros contêm dois campos:

#### Corpo do filtro

```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **Comparações permitidas:** `after`, `before`
- **Valores permitidos:** data/hora (string ISO 8601)