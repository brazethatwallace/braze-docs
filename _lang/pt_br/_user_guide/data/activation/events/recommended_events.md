---
nav_title: Eventos recomendados
article_title: Eventos recomendados
alias: /recommended_events/
page_order: 2
page_type: reference
description: "Este artigo de referência descreve os eventos recomendados, que são recomendações fornecidas pela Braze para eventos de eCommerce."
---

# Eventos recomendados {#recommended-events}

> Os eventos recomendados são construídos sobre um framework que envia eventos personalizados padronizados com esquemas JSON definidos. Quando você envia um evento recomendado, a Braze o valida em relação ao seu esquema na ingestão e aplica processamento especializado, como cálculos automáticos de campos ou gerenciamento de carrinho, que eventos personalizados genéricos não recebem. Para determinados conjuntos de eventos do setor, a Braze também oferece tratamento especial, como gatilhos dedicados baseados em ação para Campaigns e Canvas.

## Eventos recomendados de eCommerce {#ecommerce-recommended-events}

Os [eventos recomendados de eCommerce]({{site.baseurl}}/ecommerce_events) cobrem seis etapas da jornada de compra: `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled` e `order_refunded`. Quando você envia esses eventos com sucesso, a Braze valida os dados e os disponibiliza para um conjunto crescente de recursos da plataforma.

Esses recursos incluem modelos de Canvas para fluxos de navegação abandonada, carrinho abandonado, checkout abandonado e confirmação de pedido; relatórios de eCommerce; e campos calculados no perfil do usuário para _Receita Total_, _Total de Pedidos_ e _Total de Reembolsos_. Você também pode criar Segments usando filtragem de propriedades de produto aninhadas por meio de [extensões de Segment or segmento or segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension), personalizar mensagens de carrinho abandonado com a Liquid tag {% raw %}`{% shopping_cart %}`{% endraw %} e alimentar recursos do BrazeAI<sup>TM</sup> como [Eventos Preditivos]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events), [Churn Preditivo]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) e [recomendação de itens]({{site.baseurl}}/user_guide/brazeai/item_recommendations), entre outros recursos.

Como esses eventos seguem um esquema definido, cada recurso suportado pode ler os dados estruturados sem mapeamento de propriedades personalizado ou configuração por recurso da sua parte.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

### Como os eventos de eCommerce funcionam {#how-ecommerce-events-work}

Os eventos de eCommerce são eventos personalizados com nomes e esquemas de propriedades predefinidos. Você os envia usando o [SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events), o [endpoint da REST or transferir estado representacional API or interface de programação do aplicativo (API) `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou a [Ingestão de Dados na Nuvem (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion), e a Braze valida cada evento em relação ao seu esquema na ingestão. Quando a validação é aprovada, a Braze aplica automaticamente o pós-processamento específico para aquele tipo de evento, como calcular campos de receita e gerenciar o estado do carrinho nos perfis de usuário.

{% alert note %}
Uploads de CSV não suportam eventos de eCommerce. Use o SDK or kit de desenvolvimento de software, `/users/track` ou CDI para enviar esses eventos.
{% endalert %}

Os eventos de eCommerce funcionam em todos os lugares onde outros eventos personalizados funcionam: gatilhos e filtros para eventos personalizados realizados, relatórios de eventos personalizados e mais. No entanto, a validação de esquema desbloqueia recursos adicionais, incluindo:

- Ações-gatilho "Realiza pedido" em Campaigns, Canvas, jornadas de ação, gatilhos de mensagens no app e remoção de Content Cards
- Campos calculados de eCommerce no perfil do usuário (**Receita Total**, **Total de Pedidos**, **Total de Reembolsos**)
- Gerenciamento de estado do carrinho para fluxos de carrinho abandonado
- Dados mais ricos para recursos do BrazeAI<sup>TM</sup> como Eventos Preditivos, Churn Preditivo e recomendação de itens

Você também pode referenciar eventos de eCommerce pelo nome em qualquer lugar que a plataforma suporte eventos personalizados. Por exemplo, você pode disparar uma Campaign baseada em ação com eventos `ecommerce.product_viewed`, criar um Segment or segmento filtrando por eventos `ecommerce.checkout_started` ou exportar eventos `ecommerce.order_placed` pelo Currents.

#### Nomenclatura de eventos {#event-naming}

Os nomes dos eventos são exatos, sensíveis a maiúsculas e minúsculas e delimitados por ponto. Sempre use o formato canônico. Se o nome de um evento não corresponder exatamente a um dos seis nomes canônicos, a Braze o trata como um evento personalizado padrão e nenhum pós-processamento de eCommerce ocorre.

Você não pode personalizar ou renomear eventos.

- **Correto:** `ecommerce.order_placed`
- **Incorreto:** `order.placed`, `eCommerce_order_placed`, `Order_Placed`

#### Esquemas de eventos {#event-schemas}

Os seis eventos recomendados de eCommerce correspondem a etapas da jornada de compra. Dispare cada evento no momento em que o usuário conclui a ação correspondente.

![Diagrama da jornada do usuário pelos seis eventos recomendados de eCommerce: product_viewed, cart_updated, checkout_started, order_placed, order_cancelled e order_refunded.]({% image_buster /assets/img/shopify/event_schemas.png %})

{% alert tip %}
Os exemplos a seguir mostram a carga útil da REST or transferir estado representacional API or interface de programação do aplicativo (API) para cada evento.
Para registro no lado do cliente, `ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started` e `ecommerce.order_placed` usam as APIs de eventos de eCommerce do SDK or kit de desenvolvimento de software quando disponíveis, enquanto `ecommerce.order_cancelled` e `ecommerce.order_refunded` usam `logCustomEvent`. Para exemplos de implementação específicos por plataforma, consulte [Registrar eventos de eCommerce pelo SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).
{% endalert %}

{% tabs %}
{% tab ecommerce.product_viewed %}

Dispare quando um usuário visualiza uma página de detalhes do produto. Este evento é compatível com as [notificações de volta ao estoque]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) e [notificações de queda de preço]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications) do catálogo da Braze.

#### Implementação no lado do cliente {#client-side-implementation}

Use as APIs de eventos de eCommerce do SDK or kit de desenvolvimento de software quando disponíveis. Para exemplos de implementação específicos por plataforma, consulte [Registrar eventos de eCommerce pelo SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

#### Propriedades do evento {#event-properties}

| Nome da propriedade | Tipo de dados | Obrigatória | Descrição |
| -------------- | ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product_id` | String | Sim | Identificador único do produto (por exemplo, SKU ou ID do item). |
| `product_name` | String | Sim | Nome de exibição do produto. |
| `variant_id` | String | Sim | Identificador da variante do produto (por exemplo, `shirt_medium_blue`). |
| `image_url` | String | Não | URL da imagem do produto. |
| `product_url` | String | Não | URL da página do produto para mais detalhes. |
| `price` | Float | Sim | Preço unitário da variante no momento da visualização. |
| `currency` | String | Sim | Código ISO 4217 de três letras (por exemplo, `USD` ou `EUR`). |
| `source` | String | Sim | Origem do evento (por exemplo, `web`, `ios` ou `android`). |
| `type` | Array of strings | Não | Obrigatório para usar os recursos de gatilho de catálogo da Braze para alertas de volta ao estoque e queda de preço. Valores aceitos: `"price_drop"`, `"back_in_stock"` |
| `metadata` | Object | Não | Pares chave-valor flexíveis (por exemplo, `category` ou `brand`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do evento" }

#### Exemplo de REST or transferir estado representacional API or interface de programação do aplicativo (API) {#rest-api-example}

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.product_viewed",
      "time": "2026-04-28T14:22:11Z",
      "properties": {
        "product_id": "SKU-RUN-4821",
        "product_name": "Ultraboost Running Shoe",
        "variant_id": "UB-BLK-11",
        "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
        "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
        "price": 189.99,
        "currency": "USD",
        "source": "web",
        "type": ["price_drop", "back_in_stock"],
        "metadata": {
          "category": "Running Shoes",
          "brand": "Shoe Brand"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.cart_updated %}

Dispare sempre que o conteúdo do carrinho de um usuário mudar.

#### Implementação no lado do cliente

Use as APIs de eventos de eCommerce do SDK or kit de desenvolvimento de software quando disponíveis. Para exemplos de implementação específicos por plataforma, consulte [Registrar eventos de eCommerce pelo SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

Você pode enviar este evento de duas formas:

- **Substituição completa do carrinho:** Omita `action` ou defina `action` como `replace`. Inclua o conjunto completo de itens em `products` com quantidades absolutas (total de unidades por variante no carrinho). Você deve incluir `total_value`.
- **Atualizações incrementais do carrinho:** Defina `action` como `add` ou `remove`. Inclua apenas os itens que mudaram. Cada `quantity` é o número de unidades a adicionar ou remover, não a quantidade total no carrinho. Para `add`, a Braze aumenta a quantidade do item ou adiciona um novo item. Para `remove`, a Braze diminui a quantidade do item e remove o item quando a quantidade chega a `0`. `total_value` é opcional para `add` e `remove`.

{% alert warning %}
Use atualizações incrementais do carrinho (`add` ou `remove`) ou substituição completa (sem `action` ou `replace`) para um determinado carrinho. Misturar ambas as abordagens para o mesmo `cart_id` não é recomendado e pode levar a um estado inconsistente do carrinho na Braze.
{% endalert %}

Para disparar mensagens a partir deste evento, use o gatilho **Perform Cart Updated Event** em Canvas e Campaigns. Este gatilho inclui tratamento especial para impedir que o carrinho avance pelo funil de compras.

{% alert tip %}
O carrinho cria um objeto de mapeamento de carrinhos no perfil do usuário que alimenta a Liquid tag {% raw %}`{% shopping_cart %}`{% endraw %}. O carrinho expira após 30 dias sem atualização. Se dois perfis de usuário forem mesclados, a Braze preserva ambos os carrinhos.
{% endalert %}

#### Propriedades do evento

| Propriedade | Tipo de dados | Obrigatória | Descrição |
|-----------------|-----------|----------|-------------------------------------------------------------------------------------------------------------------------------|
| `cart_id` | String | Sim | Identificador único do carrinho. Compartilhado entre eventos de carrinho, checkout e pedido para o mapeamento de carrinhos do usuário. |
| `action` | String | Não | `add` (incrementar quantidade ou adicionar um item), `remove` (decrementar quantidade; item removido em `0`) ou `replace` (substituição completa do carrinho, igual a omitir `action`). |
| `total_value` | Float | Condicional | Obrigatório quando `action` é omitido ou `replace`. Opcional quando `action` é `add` ou `remove`. |
| `subtotal_value` | Float | Não | Valor do subtotal do carrinho (pós-desconto, pré-impostos/frete). |
| `tax` | Float | Não | Total de impostos aplicados ao carrinho. |
| `shipping` | Float | Não | Custo total de frete do carrinho. |
| `currency` | String | Sim | Código ISO 4217 de três letras. |
| `products` | Array | Sim | Itens desta atualização. Para substituição completa (sem `action` ou `replace`), inclua o carrinho completo com quantidades absolutas. Para `add` ou `remove`, inclua apenas os itens alterados; veja propriedades do produto. |
| `source` | String | Sim | Origem do evento. |
| `metadata` | Object | Não | Pares chave-valor flexíveis para dados adicionais no nível do evento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do evento" }

#### Propriedades do produto (`products[]`) {#product-properties-products}

| Propriedade | Tipo de dados | Obrigatória | Descrição |
|-----------------|-----------|----------|-------------------------------------------------|
| `product_id` | String | Sim | Identificador único do produto. |
| `product_name` | String | Sim | Nome de exibição do produto. |
| `variant_id` | String | Sim | Identificador da variante. |
| `image_url` | String | Não | URL da imagem do produto. |
| `product_url` | String | Não | URL da página do produto. |
| `quantity` | Integer | Sim | Para substituição completa (sem `action` ou `replace`), unidades no carrinho para este item. Para `add` ou `remove`, quantas unidades adicionar ou remover. |
| `price` | Float | Sim | Preço unitário da variante. |
| `metadata` | Object | Não | Pares chave-valor flexíveis (por exemplo, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do produto (products[])" }

{% comment %}

{% subtabs local %}
{% subtab Web %}

##### `add`

`add` increases quantity or adds a new line. The `quantity` property is how many units to add.

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
  cart_id: "cart_abc123",
  action: "add",
  currency: "USD",
  source: "web",
  products: [
    {
      product_id: "SKU-RUN-4821",
      product_name: "Ultraboost Running Shoe",
      variant_id: "UB-BLK-11",
      quantity: 1,
      price: 189.99,
    },
  ],
});
```
##### `remove`

`remove` decreases quantity by the amount in `quantity`. The line is removed when quantity reaches `0`.

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
  cart_id: "cart_abc123",
  action: "remove",
  currency: "USD",
  source: "web",
  products: [
    {
      product_id: "SKU-SOC-1102",
      product_name: "Performance Running Socks",
      variant_id: "SOC-WHT-L",
      quantity: 1,
      price: 14.99,
    },
  ],
});
```

##### `replace`

`replace` (or omit `action`) sends the full cart. `total_value` is required.

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
  cart_id: "cart_abc123",
  action: "replace",
  total_value: 234.96,
  currency: "USD",
  source: "web",
  products: [
    {
      product_id: "SKU-RUN-4821",
      product_name: "Ultraboost Running Shoe",
      variant_id: "UB-BLK-11",
      image_url: "https://cdn.example.com/shoes/ub-blk-11.jpg",
      product_url: "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
      quantity: 1,
      price: 189.99,
    },
    {
      product_id: "SKU-SOC-1102",
      product_name: "Performance Running Socks",
      variant_id: "SOC-WHT-L",
      image_url: "https://cdn.example.com/socks/soc-wht-l.jpg",
      product_url: "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
      quantity: 2,
      price: 14.99,
    },
  ],
});
```

{% endsubtab %}
{% subtab Android %}

##### Add

`add` increases quantity or adds a new line. The `quantity` property is how many units to add.

```text
Kotlin

// add — units to add
Braze.getInstance(context).logCustomEvent(
  "ecommerce.cart_updated",
  BrazeProperties(
    JSONObject()
      .put("cart_id", "cart_abc123")
      .put("action", "add")
      .put("currency", "USD")
      .put("source", "android")
      .put(
        "products",
        JSONArray().put(
          JSONObject()
            .put("product_id", "SKU-RUN-4821")
            .put("product_name", "Ultraboost Running Shoe")
            .put("variant_id", "UB-BLK-11")
            .put("quantity", 1)
            .put("price", 189.99),
        ),
      ),
  ),
)

JavaScript

// add — units to add
Braze.getInstance(context).logCustomEvent(
    "ecommerce.cart_updated",
    new BrazeProperties(new JSONObject()
        .put("cart_id", "cart_abc123")
        .put("action", "add")
        .put("currency", "USD")
        .put("source", "android")
        .put("products", new JSONArray()
            .put(new JSONObject()
                .put("product_id", "SKU-RUN-4821")
                .put("product_name", "Ultraboost Running Shoe")
                .put("variant_id", "UB-BLK-11")
                .put("quantity", 1)
                .put("price", 189.99)))));
```

##### Remove

`remove` decreases quantity by the amount in `quantity`. The line is removed when quantity reaches `0`.

```text
Kotlin

// remove — units to remove
Braze.getInstance(context).logCustomEvent(
  "ecommerce.cart_updated",
  BrazeProperties(
    JSONObject()
      .put("cart_id", "cart_abc123")
      .put("action", "remove")
      .put("currency", "USD")
      .put("source", "android")
      .put(
        "products",
        JSONArray().put(
          JSONObject()
            .put("product_id", "SKU-SOC-1102")
            .put("product_name", "Performance Running Socks")
            .put("variant_id", "SOC-WHT-L")
            .put("quantity", 1)
            .put("price", 14.99),
        ),
      ),
  ),
)

JavaScript

// remove — units to remove
Braze.getInstance(context).logCustomEvent(
    "ecommerce.cart_updated",
    new BrazeProperties(new JSONObject()
        .put("cart_id", "cart_abc123")
        .put("action", "remove")
        .put("currency", "USD")
        .put("source", "android")
        .put("products", new JSONArray()
            .put(new JSONObject()
                .put("product_id", "SKU-SOC-1102")
                .put("product_name", "Performance Running Socks")
                .put("variant_id", "SOC-WHT-L")
                .put("quantity", 1)
                .put("price", 14.99)))));
```

##### Replace

`replace` (or omit `action`) sends the full cart. `total_value` is required.

```text
Kotlin

// replace — full cart; total_value required
Braze.getInstance(context).logCustomEvent(
  "ecommerce.cart_updated",
  BrazeProperties(
    JSONObject()
      .put("cart_id", "cart_abc123")
      .put("action", "replace")
      .put("total_value", 234.96)
      .put("currency", "USD")
      .put("source", "android")
      .put(
        "products",
        JSONArray()
          .put(
            JSONObject()
              .put("product_id", "SKU-RUN-4821")
              .put("product_name", "Ultraboost Running Shoe")
              .put("variant_id", "UB-BLK-11")
              .put("quantity", 1)
              .put("price", 189.99),
          )
          .put(
            JSONObject()
              .put("product_id", "SKU-SOC-1102")
              .put("product_name", "Performance Running Socks")
              .put("variant_id", "SOC-WHT-L")
              .put("quantity", 2)
              .put("price", 14.99),
          ),
      ),
  ),
)

JavaScript

// replace — full cart; total_value required
Braze.getInstance(context).logCustomEvent(
    "ecommerce.cart_updated",
    new BrazeProperties(new JSONObject()
        .put("cart_id", "cart_abc123")
        .put("action", "replace")
        .put("total_value", 234.96)
        .put("currency", "USD")
        .put("source", "android")
        .put("products", new JSONArray()
            .put(new JSONObject()
                .put("product_id", "SKU-RUN-4821")
                .put("product_name", "Ultraboost Running Shoe")
                .put("variant_id", "UB-BLK-11")
                .put("quantity", 1)
                .put("price", 189.99))
            .put(new JSONObject()
                .put("product_id", "SKU-SOC-1102")
                .put("product_name", "Performance Running Socks")
                .put("variant_id", "SOC-WHT-L")
                .put("quantity", 2)
                .put("price", 14.99)))));
```

{% endsubtab %}
{% subtab Swift %}

##### Add

`add` increases quantity or adds a new line. The `quantity` property is how many units to add.

```text
Swift

// add — units to add
AppDelegate.braze?.logCustomEvent(
  name: "ecommerce.cart_updated",
  properties: [
    "cart_id": "cart_abc123",
    "action": "add",
    "currency": "USD",
    "source": "ios",
    "products": [
      [
        "product_id": "SKU-RUN-4821",
        "product_name": "Ultraboost Running Shoe",
        "variant_id": "UB-BLK-11",
        "quantity": 1,
        "price": 189.99,
      ],
    ],
  ]
)

Objective-C

// add — units to add
[AppDelegate.braze logCustomEvent:@"ecommerce.cart_updated"
                       properties:@{
  @"cart_id": @"cart_abc123",
  @"action": @"add",
  @"currency": @"USD",
  @"source": @"ios",
  @"products": @[@{
    @"product_id": @"SKU-RUN-4821",
    @"product_name": @"Ultraboost Running Shoe",
    @"variant_id": @"UB-BLK-11",
    @"quantity": @1,
    @"price": @189.99,
  }],
}];
```

##### Remove

`remove` decreases quantity by the amount in `quantity`. The line is removed when quantity reaches `0`.

```text
Swift

// remove — units to remove
AppDelegate.braze?.logCustomEvent(
  name: "ecommerce.cart_updated",
  properties: [
    "cart_id": "cart_abc123",
    "action": "remove",
    "currency": "USD",
    "source": "ios",
    "products": [
      [
        "product_id": "SKU-SOC-1102",
        "product_name": "Performance Running Socks",
        "variant_id": "SOC-WHT-L",
        "quantity": 1,
        "price": 14.99,
      ],
    ],
  ]
)

Objective-C

// remove — units to remove
[AppDelegate.braze logCustomEvent:@"ecommerce.cart_updated"
                       properties:@{
  @"cart_id": @"cart_abc123",
  @"action": @"remove",
  @"currency": @"USD",
  @"source": @"ios",
  @"products": @[@{
    @"product_id": @"SKU-SOC-1102",
    @"product_name": @"Performance Running Socks",
    @"variant_id": @"SOC-WHT-L",
    @"quantity": @1,
    @"price": @14.99,
  }],
}];
```

##### Replace

`replace` (or omit `action`) sends the full cart. `total_value` is required.

```text
Swift

// replace — full cart; total_value required
AppDelegate.braze?.logCustomEvent(
  name: "ecommerce.cart_updated",
  properties: [
    "cart_id": "cart_abc123",
    "action": "replace",
    "total_value": 234.96,
    "currency": "USD",
    "source": "ios",
    "products": [
      [
        "product_id": "SKU-RUN-4821",
        "product_name": "Ultraboost Running Shoe",
        "variant_id": "UB-BLK-11",
        "quantity": 1,
        "price": 189.99,
      ],
      [
        "product_id": "SKU-SOC-1102",
        "product_name": "Performance Running Socks",
        "variant_id": "SOC-WHT-L",
        "quantity": 2,
        "price": 14.99,
      ],
    ],
  ]
)

Objective-C

// replace — full cart; total_value required
[AppDelegate.braze logCustomEvent:@"ecommerce.cart_updated"
                       properties:@{
  @"cart_id": @"cart_abc123",
  @"action": @"replace",
  @"total_value": @234.96,
  @"currency": @"USD",
  @"source": @"ios",
  @"products": @[
    @{
      @"product_id": @"SKU-RUN-4821",
      @"product_name": @"Ultraboost Running Shoe",
      @"variant_id": @"UB-BLK-11",
      @"quantity": @1,
      @"price": @189.99,
    },
    @{
      @"product_id": @"SKU-SOC-1102",
      @"product_name": @"Performance Running Socks",
      @"variant_id": @"SOC-WHT-L",
      @"quantity": @2,
      @"price": @14.99,
    },
  ],
}];
```

{% endsubtab %}
{% subtab REST or transferir estado representacional API or interface de programação do aplicativo (API) %}

##### `add`

`add` increases quantity or adds a new line. The `quantity` property is how many units to add.

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.cart_updated",
      "time": "2026-04-28T14:25:33Z",
      "properties": {
        "cart_id": "cart_abc123",
        "action": "add",
        "currency": "USD",
        "source": "web",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "quantity": 1,
            "price": 189.99
          }
        ]
      }
    }
  ]
}
```

##### `remove`

`remove` decreases quantity by the amount in `quantity`. The line is removed when quantity reaches `0`.

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.cart_updated",
      "time": "2026-04-28T14:26:10Z",
      "properties": {
        "cart_id": "cart_abc123",
        "action": "remove",
        "currency": "USD",
        "source": "web",
        "products": [
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "quantity": 1,
            "price": 14.99
          }
        ]
      }
    }
  ]
}
```

##### `replace`

`replace` (or omit `action`) sends the full cart. `total_value` is required.

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.cart_updated",
      "time": "2026-04-28T14:27:00Z",
      "properties": {
        "cart_id": "cart_abc123",
        "action": "replace",
        "total_value": 234.96,
        "subtotal_value": 219.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
            "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "cart_source": "product_page_atc_button"
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endcomment %}

{% endtab %}
{% tab ecommerce.checkout_started %}

Dispare quando o usuário inicia o fluxo de checkout (por exemplo, seleciona "Checkout" ou acessa a página de checkout).

#### Implementação no lado do cliente

Use as APIs de eventos de eCommerce do SDK or kit de desenvolvimento de software quando disponíveis. Para exemplos de implementação específicos por plataforma, consulte [Registrar eventos de eCommerce pelo SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

#### Propriedades do evento

| Propriedade | Tipo | Obrigatória | Descrição |
|----------------|---------|----------|------------------------------------------------------------------------------------------------------------------|
| checkout_id | String | Sim | Identificador único da sessão de checkout. |
| cart_id | String | Não | Identificador do carrinho. Compartilhado entre eventos de carrinho, checkout e pedido para o mapeamento de carrinhos do usuário. |
| total_value | Float | Sim | Valor monetário total do checkout. |
| subtotal_value | Float | Não | Valor do subtotal (pós-desconto, pré-impostos/frete). |
| tax | Float | Não | Total de impostos aplicados ao checkout. |
| shipping | Float | Não | Custo total de frete. |
| currency | String | Sim | Código ISO 4217 de três letras. |
| products | Array | Sim | Itens sendo processados no checkout. Veja a subtabela de propriedades do produto. |
| source | String | Sim | Origem do evento. |
| metadata | Object | Não | Pares chave-valor flexíveis. Subpropriedade reconhecida: `checkout_url` (String) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do evento" }

#### Propriedades do produto (`products[]`)

| Propriedade | Tipo de dados | Obrigatória | Descrição |
|----------------|-----------|----------|----------------------------------------------------------|
| `product_id` | String | Sim | Identificador único do produto. |
| `product_name` | String | Sim | Nome de exibição do produto. |
| `variant_id` | String | Sim | Identificador da variante. |
| `image_url` | String | Não | URL da imagem do produto. |
| `product_url` | String | Não | URL da página do produto. |
| `quantity` | Integer | Sim | Número de unidades no carrinho. |
| `price` | Float | Sim | Preço unitário da variante. |
| `metadata` | Object | Não | Pares chave-valor flexíveis (por exemplo, cor, tamanho). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do produto (products[])" }

#### Exemplo de REST or transferir estado representacional API or interface de programação do aplicativo (API)

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.checkout_started",
      "time": "2026-04-28T14:30:05Z",
      "properties": {
        "checkout_id": "chk_88291",
        "cart_id": "cart_abc123",
        "total_value": 234.96,
        "subtotal_value": 219.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
            "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "checkout_url": "https://www.example.com/checkout/chk_88291",
          "checkout_type": "express"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.order_placed %}

Dispare quando um pedido é concluído com sucesso ou o pagamento é confirmado.

#### Implementação no lado do cliente

Use as APIs de eventos de eCommerce do SDK or kit de desenvolvimento de software quando disponíveis. Para exemplos de implementação específicos por plataforma, consulte [Registrar eventos de eCommerce pelo SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

{% alert important %}
Este evento é o principal gerador de receita. Ele incrementa `total_revenue` pelo valor em `total_value` e incrementa `total_orders` em 1 no perfil do usuário.
{% endalert %}

#### Propriedades do evento

| Propriedade | Tipo de dados | Obrigatória | Descrição |
|-----------------|-----------|----------|-----------------------------------------------------------------------------------------------|
| `order_id` | String | Sim | Identificador único do pedido. |
| `cart_id` | String | Não | Identificador do carrinho. Compartilhado entre eventos de carrinho, checkout e pedido para o mapeamento de carrinhos do usuário. |
| `total_value` | Float | Sim | Valor monetário total do pedido. |
| `subtotal_value` | Float | Não | Valor do subtotal (pós-desconto, pré-impostos/frete). |
| `tax` | Float | Não | Total de impostos aplicados ao pedido. |
| `shipping` | Float | Não | Custo total de frete. |
| `currency` | String | Sim | Código ISO 4217 de três letras. |
| `total_discounts` | Float | Não | Valor total de descontos aplicados ao pedido. |
| `discounts` | Array | Não | Lista detalhada de descontos aplicados. |
| `products` | Array | Sim | Itens no pedido. Veja a subtabela de propriedades do produto. |
| `source` | String | Sim | Origem do evento. |
| `metadata` | Object | Não | Pares chave-valor flexíveis. Subpropriedade reconhecida: `order_status_url` (String) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do evento" }

#### Propriedades do produto (`products[]`)

| Propriedade | Tipo de dados | Obrigatória | Descrição |
|-----------------|-----------|----------|---------------------------------------------|
| `product_id` | String | Sim | Identificador único do produto. |
| `product_name` | String | Sim | Nome de exibição do produto. |
| `variant_id` | String | Sim | Identificador da variante. |
| `image_url` | String | Não | URL da imagem do produto. |
| `product_url` | String | Não | URL da página do produto. |
| `quantity` | Integer | Sim | Número de unidades no carrinho. |
| `price` | Float | Sim | Preço unitário da variante. |
| `metadata` | Object | Não | Pares chave-valor flexíveis (por exemplo, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do produto (products[])" }

#### Exemplo de REST or transferir estado representacional API or interface de programação do aplicativo (API)

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_placed",
      "time": "2026-04-28T14:35:42Z",
      "properties": {
        "order_id": "ord_77821",
        "cart_id": "cart_abc123",
        "total_value": 224.96,
        "subtotal_value": 209.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "total_discounts": 10.0,
        "discounts": [
          {
            "code": "SPRING10",
            "amount": 10.0,
            "type": "percentage"
          }
        ],
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
            "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "order_status_url": "https://www.example.com/orders/ord_77821/status"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.order_cancelled %}

Dispare quando um pedido é cancelado.

#### Implementação no lado do cliente

Use `logCustomEvent`. Para exemplos de implementação específicos por plataforma, consulte [Registrar eventos de eCommerce pelo SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

{% alert important %}
Este evento decrementa `total_orders` em 1 no perfil do usuário. Ele não afeta `total_revenue`; use `order_refunded` para ajustar a receita.
{% endalert %}

#### Propriedades do evento

| Propriedade | Tipo | Obrigatória | Descrição |
|------------------|---------|----------|--------------------------------------------------------------------------------------------------|
| `order_id` | String | Sim | Identificador único do pedido. |
| `total_value` | Float | Sim | Valor monetário total do pedido sendo cancelado. Deve ser ≥ 0 — envie o valor absoluto; a Braze cuida do decremento. |
| `subtotal_value` | Float | Não | Valor do subtotal (pós-desconto, pré-impostos/frete). |
| `tax` | Float | Não | Total de impostos aplicados ao pedido. |
| `shipping` | Float | Não | Custo total de frete. |
| `currency` | String | Sim | Código ISO 4217 de três letras. |
| `total_discounts` | Float | Não | Valor total de descontos aplicados ao pedido. |
| `discounts` | Array | Não | Lista detalhada de descontos aplicados. |
| `cancel_reason` | String | Sim | Motivo do cancelamento do pedido. |
| `products` | Array | Sim | Itens no pedido cancelado. Veja a subtabela de propriedades do produto. |
| `source` | String | Sim | Origem do evento. |
| `metadata` | Object | Não | Pares chave-valor flexíveis. Subpropriedade reconhecida: `order_status_url` (String) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do evento" }

#### Propriedades do produto (`products[]`)

| Propriedade | Tipo de dados | Obrigatória | Descrição |
|----------------|-----------|----------|-----------------------------------------------|
| `product_id` | String | Sim | Identificador único do produto. |
| `product_name` | String | Sim | Nome de exibição do produto. |
| `variant_id` | String | Sim | Identificador da variante. |
| `image_url` | String | Não | URL da imagem do produto. |
| `product_url` | String | Não | URL da página do produto. |
| `quantity` | Integer | Sim | Número de unidades no carrinho. |
| `price` | Float | Sim | Preço unitário da variante. |
| `metadata` | Object | Não | Pares chave-valor flexíveis (por exemplo, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do produto (products[])" }

#### Exemplo de REST or transferir estado representacional API or interface de programação do aplicativo (API)

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_cancelled",
      "time": "2026-04-28T16:10:00Z",
      "properties": {
        "order_id": "ord_77821",
        "total_value": 224.96,
        "subtotal_value": 209.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "total_discounts": 10.0,
        "cancel_reason": "customer_request",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "order_status_url": "https://www.example.com/orders/ord_77821/status"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.order_refunded %}

Dispare quando um reembolso total ou parcial é emitido.

#### Implementação no lado do cliente

Use `logCustomEvent`. Para exemplos de implementação específicos por plataforma, consulte [Registrar eventos de eCommerce pelo SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

{% alert important %}
Este evento decrementa `total_revenue` pelo valor em `total_value` e incrementa `total_refunds` no perfil do usuário. Para reembolsos parciais, defina `total_value` apenas como o valor reembolsado, não o total original do pedido.
{% endalert %}

#### Propriedades do evento

| Propriedade | Tipo de dados | Obrigatória | Descrição |
|-------------------|-----------|----------|------------------------------------------------------------------------------------------------------|
| `order_id` | String | Sim | Identificador único do pedido original. |
| `total_value` | Float | Sim | Valor monetário total do reembolso. Deve ser ≥ 0 — envie o valor absoluto; a Braze cuida do incremento em total_refunds. |
| `currency` | String | Sim | Código ISO 4217 de três letras. |
| `total_discounts` | Float | Não | Valor total de descontos originalmente aplicados. |
| `discounts` | Array | Não | Lista detalhada de descontos. |
| `products` | Array | Sim | Itens sendo reembolsados. Veja a subtabela de propriedades do produto. |
| `source` | String | Sim | Origem do evento. |
| `metadata` | Object | Não | Pares chave-valor flexíveis. Subpropriedade reconhecida: `order_status_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do evento" }

#### Propriedades do produto (`products[]`)

| Propriedade | Tipo de dados | Obrigatória | Descrição |
|-----------------|-----------|----------|-------------------------------------------------------|
| `product_id` | String | Sim | Identificador único do produto. |
| `product_name` | String | Sim | Nome de exibição do produto. |
| `variant_id` | String | Sim | Identificador da variante. |
| `image_url` | String | Não | URL da imagem do produto. |
| `product_url` | String | Não | URL da página do produto. |
| `quantity` | Integer | Sim | Número de unidades no carrinho. |
| `price` | Float | Sim | Preço unitário da variante. |
| `metadata` | Object | Não | Pares chave-valor flexíveis (por exemplo, `color` ou `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propriedades do produto (products[])" }

#### Exemplos de REST or transferir estado representacional API or interface de programação do aplicativo (API) {#rest-api-examples}

{% subtabs %}
{% subtab Reembolso total %}

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_refunded",
      "time": "2026-04-29T10:05:00Z",
      "properties": {
        "order_id": "ord_77821",
        "total_value": 189.99,
        "currency": "USD",
        "total_discounts": 0,
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11",
              "refund_reason": "size_mismatch"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "order_status_url": "https://www.example.com/orders/ord_77821/status"
        }
      }
    }
  ]
}
```
{% endsubtab %}
{% subtab Reembolso parcial %}

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_refunded",
      "time": "2026-05-02T11:08:30Z",
      "properties": {
        "order_id": "ORD-20260428-7891",
        "total_value": 29.98,
        "currency": "USD",
        "products": [
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "refund_method": "store_credit",
          "initiated_by": "customer"
        }
      }
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Pós-processamento de eventos de eCommerce {#ecommerce-event-post-processing}

Quando você envia um evento de eCommerce, a Braze o valida em relação ao esquema esperado para aquele nome de evento.

A tabela a seguir resume o que a Braze faz automaticamente para cada evento quando a validação é aprovada. Para saber o que acontece quando a validação falha, consulte [Validação de eventos e solução de problemas](#event-validation-and-troubleshooting).

| Evento | O que a Braze faz automaticamente |
|------------------------------|-------------------------------------------------------------------------------------------------------------------|
| `ecommerce.order_placed` | Incrementa **Receita Total** pelo valor de `total_value` e **Total de Pedidos** em 1 no perfil do usuário. |
| `ecommerce.order_cancelled` | Decrementa **Total de Pedidos** em 1. |
| `ecommerce.order_refunded` | Decrementa **Receita Total** pelo valor de `total_value` e incrementa **Valor Total de Reembolsos**. |
| `ecommerce.cart_updated` | Cria ou atualiza o objeto de mapeamento de carrinhos no perfil do usuário (cargas úteis de carrinho completo ou atualizações incrementais de carrinho com `action` opcional: `add`, `remove` ou `replace`). O carrinho expira após 30 dias sem atualização. |
| `ecommerce.product_viewed` | Sem alterações no perfil do usuário. Disponível para segmentação, gatilhos e recursos do BrazeAI<sup>TM</sup> (como recomendação de itens). |
| `ecommerce.checkout_started` | Sem alterações no perfil do usuário. Disponível para segmentação e gatilhos (por exemplo, fluxos de checkout abandonado). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pós-processamento de eventos de eCommerce" }

{% alert important %}
Valores em moedas diferentes de USD são automaticamente convertidos para USD usando a taxa de câmbio da data em que o evento é reportado. Se você já reporta em USD, defina `USD` como a moeda para evitar conversões indesejadas.
{% endalert %}

## Detalhes de implementação {#implementation-details}

### Pontos de dados e faturamento {#data-points-and-billing}

Os eventos de eCommerce não consomem [pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points). Você pode registrá-los sem nenhum impacto no seu uso de pontos de dados.

### Limite de tamanho do evento {#event-size-limit}

As propriedades de evento enviadas para `/users/track` são limitadas a 102.400 bytes (100 KB) por evento. Para mensagens disparadas de Campaign e Canvas, as `trigger_properties` enviadas para [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) e [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) têm um limite padrão mais restrito de 51.200 bytes (50 KB).

Como prática recomendada, envie apenas as informações de produto necessárias para disparar, personalizar ou atribuir o evento. Armazene detalhes mais completos do produto — como descrições, listas completas de variantes, estoque ou imagens alternativas — nos Catálogos da Braze. Faça referência a esses detalhes por `product_id` ou `variant_id` ao enviar mensagens. Use o objeto `metadata` de forma seletiva para contexto específico do pedido ou do produto que será utilizado no envio de mensagens.

### Tratamento de moeda {#currency-handling}

A Braze converte automaticamente valores em moedas diferentes de USD para USD usando a taxa de câmbio da data em que o evento foi registrado. Esse valor convertido é o que aparece nas métricas de receita.

{% alert tip %}
Se você opera apenas em USD, defina `"currency": "USD"` de forma fixa em todos os eventos para evitar conversões desnecessárias.
{% endalert %}

### Campo source {#source-field}

A propriedade source é uma string obrigatória que identifica a origem do evento. Por exemplo, `shopify`, `in-store POS` ou `custom_api`. Isso ajuda a distinguir as fontes de integração ao analisar dados em exportações do Currents ou ao depurar problemas de validação.

### Flexibilidade de metadata {#metadata-flexibility}

Os objetos de metadata no nível do evento e no nível do produto aceitam pares de chave-valor arbitrários, permitindo que você adicione dimensões personalizadas sem modificar o esquema principal. Exemplos comuns incluem `order_status_url`, `gift_wrapped`, `loyalty_points_earned` ou `warehouse_id`. Essas propriedades estão disponíveis na personalização com Liquid, nas exportações do Currents e na segmentação por meio de [extensões de Segment or segmento or segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension).

{% alert important %}
Os eventos recomendados usam um esquema rígido. Por isso, adicionar propriedades personalizadas no nível superior de properties falhará na validação. Coloque todas as propriedades personalizadas dentro do objeto `metadata` no nível do evento ou do objeto `metadata` no nível do produto dentro de `products[]`. Elas continuam disponíveis para Liquid, Currents e segmentação da mesma forma que os campos de nível superior.
{% endalert %}

## Validação de eventos e solução de problemas {#event-validation-and-troubleshooting}

Quando você envia um evento recomendado de eCommerce por meio de `/users/track` ou de qualquer SDK or kit de desenvolvimento de software da Braze, a Braze valida a carga útil em relação ao esquema JSON do evento durante o processamento do evento recomendado. A validação é executada automaticamente em todos os eventos cujo nome corresponde exatamente a um evento recomendado (por exemplo, `ecommerce.order_placed` ou `ecommerce.cart_updated`).

### O que é validado {#what-we-validate}

Para cada evento cujo nome corresponde a um evento recomendado de eCommerce, a Braze verifica:

| Verificação                     | Exemplo                                                                                                                      |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Nome do evento                 | Deve ser exato. Por exemplo, `ecommerce.cart_updated` está correto — não `ecommerce.Cart_Updated`, `cartupdated` ou `cart_updated`. |
| Propriedades obrigatórias presentes | `order_placed` requer `order_id`, `total_value`, `currency`, `products` e `source`.                                   |
| Tipos de dados corretos        | `total_value` deve ser um número; `currency` deve ser uma string; `products` deve ser um array.                              |
| Sem propriedades extras no nível superior | Campos personalizados em properties causam falha. Use o objeto `metadata` em vez disso.                            |
| Restrições de valor            | Campos monetários devem ser ≥ `0`. `currency` deve ser uma string ISO 4217 válida.                                          |
| Campos por produto             | Cada item em `products[]` deve incluir `product_id`, `product_name`, `variant_id`, `quantity` e `price`.                    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="O que é validado" }

### Por que validamos {#why-we-validate}

Os eventos de eCommerce alimentam recursos que dependem de dados consistentes e previsíveis, incluindo rastreamento de receita, a tag Liquid {% raw %}`{% shopping_cart %}`{% endraw %}, o gatilho de carrinho abandonado e relatórios. Quando as cargas úteis divergem do esquema, esses recursos produzem imprecisões silenciosas (totais de receita incorretos, carrinhos ausentes, gatilhos quebrados). A validação aplica o contrato antecipadamente para que os recursos downstream se comportem de forma previsível.

### Quando a validação é aprovada {#when-validation-passes}

O evento é processado como um evento recomendado de eCommerce com todo o pós-processamento associado. Consulte [Eventos recomendados de eCommerce](#event-schemas) para a lista completa de comportamentos acionados por cada tipo de evento.

#### Verificar um evento bem-sucedido {#verify-a-successful-event}

Após enviar um evento, você pode confirmar que ele foi aceito e processado corretamente usando qualquer um dos seguintes métodos:

- [Registro de usuários de eventos]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log): Abra o perfil do usuário no dashboard e revise a atividade. Os eventos recomendados aparecem com a carga útil completa de propriedades, para que você possa confirmar que o evento chegou e que os valores correspondem ao que foi enviado.
- [Relatório de eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report): Acesse **Analytics** > **Custom Events Report** para ver contagens agregadas de cada evento recomendado ao longo do tempo. Isso é útil para confirmar que o tráfego de produção está fluindo conforme esperado quando sua integração está ativa.
- [Usuários teste]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups?utm_source=operator_user&utm_medium=dashboard#adding-test-users): Marque um usuário no seu espaço de trabalho de desenvolvimento como usuário teste e, em seguida, dispare eventos da sua integração para esse usuário. Os usuários teste são sinalizados no dashboard, facilitando o isolamento e a inspeção do comportamento de ponta a ponta.

### Quando a validação falha {#when-validation-fails}

O evento não é processado como um evento recomendado. Especificamente:

- **O evento é descartado por completo.** Eventos recomendados de eCommerce inválidos não são registrados no perfil do usuário, não aparecem no Currents e não ficam disponíveis para segmentação.
- Os recursos downstream de eventos recomendados não são executados, incluindo:
  - Rastreamento de receita (relatórios de receita, campos calculados do usuário como `total_revenue`)
  - Atualizações do objeto de carrinho no perfil do usuário
  - Gatilhos "Perform Cart Updated Event" ou "Placed Order" em Canvas e Campaigns

A forma como os erros são reportados depende do caminho de ingestão:

- **REST or transferir estado representacional API or interface de programação do aplicativo (API) (`/users/track`):** Cada evento inválido é reportado no array de erros da resposta. Cada entrada informa qual evento falhou (índice) e por quê (tipo). O campo `message` no nível superior ainda diz "success", o que significa apenas que sua requisição chegou à Braze, não que todos os eventos eram válidos. Sempre verifique se há um array de erros na resposta.
- **SDKs da Braze:** As chamadas do SDK or kit de desenvolvimento de software retornam imediatamente e a validação é executada em segundo plano, então os erros não são enviados de volta ao seu app. Para saber sobre falhas de validação de eventos de eCommerce, fique atento ao e-mail de resumo de falhas (consulte [Encontrar falhas](#find-failures)).

#### Exemplo de resposta de erro da API or interface de programação do aplicativo (API) {#example-api-error-response}

O endpoint `/users/track` retorna erros no nível do campo indicando quais propriedades falharam e por quê. Observe que o `message` no nível superior pode retornar `"success"` porque o evento foi aceito no pipeline; o array `errors` informa quais campos falharam na validação do esquema. Veja o exemplo de resposta de erro a seguir.

```json
{
 "message": "success",
 "errors": [{ "index": 0, "input_array": "purchases", "type": "'currency' must be an ISO 4217 currency" }]
}
```

As falhas também são classificadas internamente e agregadas para o e-mail de resumo de falhas:

| Tipo de falha            | Significado                                       | Exemplo                                                        |
|--------------------------|---------------------------------------------------|----------------------------------------------------------------|
| `missing_property`       | Um campo obrigatório está ausente.                | `order_placed` enviado sem `order_id`.                         |
| `extra_property`         | Um campo foi adicionado que o esquema não define. | Um campo personalizado `gift_wrapped` no nível superior de `properties` em vez de dentro de `metadata`. |
| `unexpected_data_type`   | Um campo está com o tipo errado.                  | `total_value: "29.99"` (string) em vez de `29.99` (número).    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Exemplo de resposta de erro da API or interface de programação do aplicativo (API)" }

{% alert note %}
Nomes de eventos que não correspondem exatamente a um evento recomendado (por exemplo, `ecommerce.OrderPlaced`) ignoram a validação por completo e são registrados como eventos personalizados comuns. Eles aparecem no Currents e na segmentação com o nome que você enviou, mas não recebem processamento de evento recomendado e nenhuma entrada `errors` na resposta.
{% endalert %}

#### Encontrar falhas {#find-failures}

A Braze envia aos administradores do seu espaço de trabalho um e-mail com o resumo das falhas de validação de eventos recomendados, para que você possa identificar e corrigir problemas de integração sem monitorar manualmente cada evento.

O e-mail de resumo inclui:

- **Contagem total de erros:** Contagens de erros para o período do relatório.
- **Erros por evento:** Um detalhamento de quantos eventos falharam para cada tipo de evento recomendado (por exemplo, `ecommerce.cart_updated` e `ecommerce.order_placed`). Use isso para identificar quais eventos na sua integração precisam de atenção primeiro.
- **Erros por origem:** Uma divisão entre API or interface de programação do aplicativo (API) e SDK or kit de desenvolvimento de software, para que você possa identificar qual integração está gerando as falhas.

Se você não está recebendo esses e-mails ou deseja verificar a lista de destinatários, entre em contato com a equipe da sua conta Braze.

#### Diagnosticar e corrigir falhas {#diagnose-and-fix-failures}

Quando você receber um e-mail de resumo de falhas:

1. **Identifique o evento com falha e a origem.** O e-mail separa as falhas por nome de evento e origem da integração (`sdk` versus `rest_api`), para que você possa identificar qual integração precisa da correção. Se você tem múltiplas origens enviando o mesmo evento (por exemplo, o SDK or kit de desenvolvimento de software da sua loja e um webhook de backend ambos enviando `cart_updated`), trate-os de forma independente.
2. **Compare sua carga útil com o esquema** em [Esquemas de eventos](#event-schemas). A maioria das falhas se enquadra em um de três padrões:
   - `missing_property`: Um campo obrigatório está ausente. Para resolver, adicione o campo obrigatório.
   - `extra_property`: Um campo personalizado está no nível superior de `properties`. Para resolver, mova o campo personalizado para dentro de `metadata` (nível do evento) ou `products[].metadata` (por produto).
   - `unexpected_data_type`: Um valor está com o tipo errado (por exemplo, `total_value` enviado como string). Para resolver, converta o valor antes de enviar.
3. **Teste a carga útil corrigida em um espaço de trabalho de desenvolvimento** antes de implantar em produção. Envie um evento de teste conhecido para um usuário teste e, em seguida, verifique o comportamento esperado do evento recomendado no perfil desse usuário (por exemplo, se o objeto de carrinho é atualizado, se a receita é incrementada ou se o gatilho de carrinho abandonado é disparado).
4. **Monitore o próximo e-mail de falhas** para confirmar que a contagem de falhas para aquele evento, origem e tipo caiu para zero.

Para os requisitos completos de propriedades por evento, consulte [Esquemas de eventos](#event-schemas).