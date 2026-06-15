---
nav_title: "Objeto de compra"
article_title: Objeto de compra da API
page_order: 8
page_type: reference
description: "Este artigo de referência explica os diferentes componentes de um objeto de compra, como usá-lo corretamente e exemplos para consulta."

---

# Objeto de compra {#purchase-object}

> Este artigo explica os diferentes componentes de um objeto de compra, como usá-lo corretamente, as práticas recomendadas e exemplos para consulta.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

## O que é um objeto de compra? {#what-is-a-purchase-object}

Um objeto de compra é um objeto que é passado pela API quando uma compra é feita. Cada objeto de compra está localizado em um array de compras, sendo que cada objeto representa uma única compra de um determinado usuário em um determinado momento. O objeto de compra possui muitos campos diferentes que permitem que o backend da Braze armazene e use essas informações para personalização, coleta de dados e customização.

### Corpo do objeto {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required.
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  // See the following product_id naming conventions for clarification.
  "product_id" : (required, string) identifier for the purchase, for example, Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (for example, Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601) Time of purchase,
  // See the following purchase object explanation for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

- [ID de usuário externo]({{site.baseurl}}/api/basics/#user-ids)
- [Identificador do app]({{site.baseurl}}/api/identifier_types/)
- [Wiki do código de moeda ISO 4217](http://en.wikipedia.org/wiki/ISO_4217)
- [Wiki do código de tempo ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
Alguns pares de identificadores não podem ser usados juntos, e `email` tem precedência sobre `phone` quando ambos são fornecidos. Para detalhes completos, consulte [Resolução de identificadores]({{site.baseurl}}/api/objects_filters/user_attributes_object/#identifier-resolution).
{% endalert %}

## ID do produto de compra {#purchase-product-id}

No objeto de compra, o `product_id` é um identificador da compra (como `Product Name` ou `Product Category`):

- A Braze permite que você armazene até 5.000 `product_id`s no dashboard.
- O `product_id` pode ter até 255 caracteres.

### Convenções de nomenclatura {#naming-conventions}

Na Braze, oferecemos algumas convenções gerais de nomenclatura para o `product_id` do objeto de compra. Ao escolher o `product_id`, a Braze sugere o uso de nomes simples, como o nome do produto ou a categoria do produto (em vez de SKUs), com a intenção de agrupar todos os itens registrados por esse `product_id`.

Isso ajuda a tornar os produtos mais fáceis de identificar para segmentação e acionamento.

### Registrar compras no nível do pedido {#log-purchases-at-the-order-level}

Se quiser registrar compras no nível do pedido em vez de no nível do produto, você pode usar o nome do pedido ou a categoria do pedido como `product_id` (como `Online Order` ou `Completed Order`).

Por exemplo, para registrar compras no nível do pedido no Web SDK:

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
      }
    }
  ]
}
```

## Objeto de propriedades de compra {#purchase-properties-object}

{% include data_activation/purchase_event_property_data_types.md %}

Para uma referência consolidada dos tipos de dados em atributos personalizados, propriedades de evento e catálogos, consulte [Tipos de dados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#purchase-event-property-data-types).

### Propriedades de compra {#purchase-properties}

[As propriedades de compra]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) podem ser usadas para disparar mensagens e para personalização usando Liquid, permitindo também a segmentação com base nessas propriedades.

#### Convenções de nomenclatura {#naming-conventions}

É importante notar que esse recurso está ativado **por produto**, não por compra. Por exemplo, se você tiver um alto volume de produtos distintos, mas cada um tiver as mesmas propriedades, a segmentação pode ser desnecessária.

Nesse caso, recomendamos usar nomes de produtos em um nível de "grupo" em vez de identificadores em nível de transação ao definir estruturas de dados. Por exemplo, uma empresa de bilhetes de trem deve ter produtos para "viagem única", "viagem de ida e volta", "várias cidades", e não transações específicas, como "transação 123" ou "transação 046". Como outro exemplo, com o evento de compra "comida", as propriedades seriam melhor definidas como "bolo" e "sanduíche".

{% alert important %}
Observe que os produtos podem ser adicionados por meio da REST API da Braze. Por exemplo, se você enviar uma chamada para o endpoint `/users/track` e incluir um novo ID de compra, a Braze cria automaticamente um produto na seção **Configurações de dados** > **Produtos** do dashboard.
{% endalert %}

### Exemplo de objeto de compra {#example-purchase-object}

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "backpack",
      "currency" : "USD",
      "price" : 40.00,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogram" : "ABC",
        "checkout_duration" : 180,
        "size" : "Large",
        "brand" : "Backpack Locker"
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pencil",
      "currency" : "USD",
      "price" : 2.00,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "sharpened" : true
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pen",
      "currency" : "USD",
      "price" : 2.50,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

### Objetos de compra, objetos de evento e webhooks {#purchase-objects-event-objects-and-webhooks}

Usando o exemplo fornecido, podemos ver que alguém comprou uma mochila com as propriedades: cor, monograma, duração do checkout, tamanho e marca. Em seguida, podemos criar segmentos com essas propriedades usando [propriedades de eventos de compra]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) ou enviar mensagens personalizadas por meio de um canal usando Liquid. Por exemplo, "Olá **Ana F.**, obrigado por comprar aquela **mochila vermelha média** por **R$ 40,00**! Obrigado por comprar na **Backpack Locker**!"

Se quiser salvar, armazenar e rastrear propriedades para segmentar, será necessário configurá-las como atributos personalizados. Isso pode ser feito usando [Extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension/), que permitem o direcionamento de usuários com base em eventos personalizados ou comportamento de compra armazenado durante toda a vida útil desse perfil de usuário.