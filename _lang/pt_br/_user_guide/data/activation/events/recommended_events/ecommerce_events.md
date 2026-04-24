---
nav_title: Eventos recomendados de eCommerce
article_title: Eventos recomendados de eCommerce
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "Este artigo de referência descreve os eventos e propriedades recomendados de eCommerce, seu uso, segmentação, onde visualizar análises de dados relevantes e mais."
---

# Eventos recomendados de eCommerce

> Esta página aborda os eventos e propriedades recomendados de eCommerce. Esses eventos foram criados para capturar comportamentos de compra essenciais que profissionais de marketing precisam para disparar mensagens eficazes, como o direcionamento de carrinhos abandonados.

{% alert important %}
Os eventos recomendados de eCommerce estão atualmente em acesso antecipado. Fale com o seu gerente de sucesso do cliente da Braze se tiver interesse em participar desse acesso antecipado. <br><br>Se você está usando o novo [conector Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), esses eventos recomendados estarão disponíveis automaticamente por meio da integração.
{% endalert %}

A Braze reconhece que o planejamento de dados leva tempo. Incentivamos nossos clientes a familiarizar suas equipes de desenvolvimento e começar a enviar esses eventos agora. Embora alguns recursos possam não estar disponíveis imediatamente com os eventos recomendados de eCommerce, você pode esperar a introdução de novos produtos ao longo de 2025 que aprimorarão suas capacidades de eCommerce.

## Tipos de eventos recomendados de eCommerce

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Qualquer moeda diferente de USD será exibida na Braze em USD com base na taxa de câmbio da data em que foi reportada. Para evitar a conversão de moeda, defina a moeda como USD diretamente no código.

{% tabs %}
{% tab ecommerce.product_viewed %}

Você pode usar o evento de produto visualizado para disparar quando um cliente visualiza uma página de detalhes do produto.

#### Propriedades

| Nome da propriedade | Obrigatória | Tipo de dado | Descrição | 
|---|---|---|---|
| `product_id` | Sim | String | Um identificador único para o produto que foi visualizado. <br> Para clientes que não usam Shopify, esse será o valor definido para os IDs de itens do catálogo, como SKUs. |
| `product_name` | Sim | String | O nome do produto que foi visualizado. | 
| `variant_id` | Sim | String | Um identificador único para a variante do produto. Um exemplo é `shirt_medium_blue` |
| `image_url` | Não | String | URL da imagem do produto. |
| `product_url` | Não | String | URL da página do produto para mais detalhes. |
| `price` | Sim | Float | O preço unitário da variante do produto no momento da visualização. |
| `currency` | Sim | String | A moeda em que o preço do produto está listado (como "USD" ou "EUR") no [formato ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `source` | Sim | String | Origem de onde o evento é derivado. (Para Shopify, é storefront). |
| `type` | Não | Object | Funciona com [notificações de volta ao estoque]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) e [notificações de queda de preço]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications). |
| `metadata` | Não | Object | |
| `sku` | Não | String | (Somente Shopify) SKU do Shopify. Pode ser configurado como o campo de ID do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemplos de objetos

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

Em versões mais recentes do SDK, chame `logEcommerceEvent()`:

```javascript
braze.logEcommerceEvent({ 
    "name": "ecommerce.product_viewed", 
    "properties": {
        "product_id": "4111176",
        "product_name": "Torchie runners",
        "variant_id": "4111176700",
        "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
        "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
        "price": 85,
        "currency": "GBP",
        "source": "https://braze-apparel.com/",
        "metadata": {
            "sku": "",
            "color": "ORANGE",
            "size": "6",
            "brand": "Braze"
        }
    }
});
```

Em versões legadas do SDK, chame `logCustomEvent()`:

```javascript
braze.logCustomEvent("ecommerce.product_viewed", {
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": {
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
BrazeProperties properties = new BrazeProperties()
    .addProperty("product_id", "4111176")
    .addProperty("product_name", "Torchie runners")
    .addProperty("variant_id", "4111176700")
    .addProperty("image_url", "https://braze-apparel.com/images/products/large/torchie-runners.jpg")
    .addProperty("product_url", "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/")
    .addProperty("price", 85)
    .addProperty("currency", "GBP")
    .addProperty("source", "https://braze-apparel.com/")
    .addProperty("metadata", new JSONObject()
        .put("sku", "")
        .put("color", "ORANGE")
        .put("size", "6")
        .put("brand", "Braze"));

Braze.getInstance(context).logCustomEvent("ecommerce.product_viewed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let properties: [String: Any] = [
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": [
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.product_viewed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.product_viewed",
      "time": "2024-01-15T09:03:45Z",
      "properties": {
        "product_id": "4111176",
        "product_name": "Torchie runners",
        "variant_id": "4111176700",
        "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
        "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
        "price": 85,
        "currency": "GBP",
        "source": "https://braze-apparel.com/",
        "metadata": {
          "sku": "",
          "color": "ORANGE",
          "size": "6",
          "brand": "Braze"
        },
        "type": [
          "price_drop",
          "back_in_stock"
        ]
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.cart_updated %}

Você pode usar o gatilho **Perform Cart Updated Event** para rastrear quando produtos são adicionados, removidos ou atualizados no carrinho. Esse evento verifica as seguintes informações antes de ser disparado:

- O horário do evento é posterior ao horário `updated_at` do carrinho específico do usuário.
- O carrinho não avançou para o processo de checkout.
- O array `products` não está vazio.

#### Objeto de mapeamento de carrinhos

O evento `ecommerce.cart_updated` possui um objeto de mapeamento de carrinhos. Esse objeto é criado no perfil do usuário e contém um mapeamento de carrinhos com todos os produtos no carrinho do comprador. Você pode acessar os produtos no carrinho de compras por meio da Liquid tag:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

Se um carrinho não for atualizado e não avançar para um evento de pedido realizado dentro de 30 dias, a Braze exclui o carrinho e os produtos associados.

{% alert note %}
Os produtos por carrinho não são limitados na Braze. No entanto, o limite do Shopify é de 500.
{% endalert %}

#### Comportamento do carrinho ao mesclar perfis de usuário

Se houver dois carrinhos, ambos são adicionados ao usuário mesclado. O Canvas é reenfileirado se for o mesmo carrinho ou um carrinho diferente, para enviar uma mensagem com as informações mais recentes do carrinho. O evento `ecommerce.cart_updated` conterá o ID do carrinho mais recente e os produtos mais recentes no carrinho.

#### Propriedades

| Nome da propriedade | Obrigatória | Tipo de dado | Descrição | 
|---|---|---|---|
| `cart_id` | Sim | String | Se você não está usando uma plataforma de terceiros que fornece um `cart_id`, pode usar o [ID de sessão da Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions). |
| `total_value` | Sim | Float | Valor monetário total do carrinho. |
| `subtotal_value` | Não | Float | Valor do subtotal do carrinho após descontos e antes de impostos e frete. |
| `tax` | Não | Float | Total de impostos aplicados ao carrinho. |
| `shipping` | Não | Float | Custo total de frete do carrinho. |
| `currency` | Sim | String | A moeda em que o preço do produto está listado (como "USD" ou "EUR") no [formato ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `products` | Sim | Array |  |
| `product_id` | Sim | String | Um identificador único para o produto que foi visualizado. <br> Esse valor pode ser o ID do produto ou SKU. |
| `product_name` | Sim | String | O nome do produto que foi visualizado. |
| `variant_id` | Sim | String | Um identificador único para a variante do produto. Um exemplo é `shirt_medium_blue` |
| `image_url` | Não | String | URL da imagem do produto. |
| `product_url` | Não | String | URL da página do produto para mais detalhes. |
| `quantity` | Sim | Integer | Número de unidades do produto no carrinho. |
| `price` | Sim | Float | O preço unitário da variante do produto no momento da visualização. |
| `metadata` | Não | Object | Campo de metadados adicionais sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos o SKU. <br> Terá um limite baseado no nosso limite geral de propriedades de evento de 50 kb. |
| `sku` | Não | String | (Somente Shopify) SKU do Shopify. Pode ser configurado como o campo de ID do catálogo. |
| `source` | Sim | String | Origem de onde o evento é derivado. (Para Shopify, é storefront). |
| `metadata` | Não | Object | Campo de metadados adicionais sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos o SKU. <br> Terá um limite baseado no nosso limite geral de propriedades de evento de 50 kb. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemplos de objetos

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

Em versões mais recentes do SDK, chame `logEcommerceEvent()`:

```javascript
braze.logEcommerceEvent({ 
    "name": "ecommerce.cart_updated", 
    "properties": {
        "cart_id": "cart_12345",
        "currency": "USD",
        "total_value": 199.98,
        "products": [
            {
                "product_id": "8266836345064",
                "product_name": "Classic T-Shirt",
                "variant_id": "44610569208040",
                "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
                "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
                "quantity": 2,
                "price": 99.99,
                "metadata": {
                    "sku": "TSH-BLU-M",
                    "color": "BLUE",
                    "size": "Medium",
                    "brand": "Braze"
                }
            }
        ],
        "source": "https://braze-apparel.com",
        "metadata": {}
    }
});
```

Em versões legadas do SDK, chame `logCustomEvent()`:

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "subtotal_value": 179.98,
    "tax": 15.00,
    "shipping": 5.00,
    "products": [
        {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
                "sku": "TSH-BLU-M",
                "color": "BLUE",
                "size": "Medium",
                "brand": "Braze"
            }
        }
    ],
    "source": "https://braze-apparel.com",
    "metadata": {}
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "8266836345064")
    .put("product_name", "Classic T-Shirt")
    .put("variant_id", "44610569208040")
    .put("image_url", "https://braze-apparel.com/images/tshirt-blue-medium.jpg")
    .put("product_url", "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040")
    .put("quantity", 2)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "TSH-BLU-M")
        .put("color", "BLUE")
        .put("size", "Medium")
        .put("brand", "Braze"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("cart_id", "cart_12345")
    .addProperty("currency", "USD")
    .addProperty("total_value", 199.98)
    .addProperty("subtotal_value", 179.98)
    .addProperty("tax", 15.00)
    .addProperty("shipping", 5.00)
    .addProperty("products", products)
    .addProperty("source", "https://braze-apparel.com")
    .addProperty("metadata", new JSONObject());

Braze.getInstance(context).logCustomEvent("ecommerce.cart_updated", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "8266836345064",
        "product_name": "Classic T-Shirt",
        "variant_id": "44610569208040",
        "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
        "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
        "quantity": 2,
        "price": 99.99,
        "metadata": [
            "sku": "TSH-BLU-M",
            "color": "BLUE",
            "size": "Medium",
            "brand": "Braze"
        ]
    ]
]

let properties: [String: Any] = [
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "subtotal_value": 179.98,
    "tax": 15.00,
    "shipping": 5.00,
    "products": products,
    "source": "https://braze-apparel.com",
    "metadata": [:]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.cart_updated", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.cart_updated",
      "time": "2024-01-15T09:15:30Z",
      "properties": {
        "cart_id": "cart_12345",
        "currency": "USD",
        "total_value": 199.98,
        "subtotal_value": 179.98,
        "tax": 15.00,
        "shipping": 5.00,
        "products": [
          {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
              "sku": "TSH-BLU-M",
              "color": "BLUE",
              "size": "Medium",
              "brand": "Braze"
            }
          }
        ],
        "source": "https://braze-apparel.com",
        "metadata": {}
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.checkout_started %}

Você pode usar o evento de checkout iniciado para redirecionar clientes que começaram o processo de checkout, mas não finalizaram o pedido.

Semelhante ao evento `ecommerce.cart_updated`, esse evento permite que você use a Liquid tag do carrinho de compras para acessar todos os produtos no carrinho em mensagens de checkout abandonado:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### Propriedades

| Nome da propriedade | Obrigatória | Tipo de dado | Descrição | 
|---|---|---|---|
| `checkout_id` | Sim | String | Identificador único para o checkout. |
| `cart_id` | Não | String | Se você não está usando uma plataforma de terceiros que fornece um `cart_id`, pode usar o [ID de sessão da Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions). | 
| `total_value` | Sim | Float | Valor monetário total do carrinho. |
| `subtotal_value` | Não | Float | Valor do subtotal do carrinho após descontos e antes de impostos e frete. |
| `tax` | Não | Float | Total de impostos aplicados ao carrinho. |
| `shipping` | Não | Float | Custo total de frete do carrinho. |
| `currency` | Sim | String | Moeda em que o carrinho é avaliado. |
| `products` | Sim | Array of objects |  |
| `product_id` | Sim | String | Um identificador único para o produto que foi visualizado. Por exemplo, esse valor pode ser o ID do produto ou SKU. |
| `product_name` | Sim | String | O nome do produto que foi visualizado.  |
| `variant_id` | Sim | String | Um identificador único para a variante do produto. Um exemplo é `shirt_medium_blue` |
| `image_url` | Não | String | URL da imagem do produto. |
| `product_url` | Não | String | URL da página do produto para mais detalhes. |
| `quantity` | Sim | Integer | Número de unidades do produto no carrinho. |
| `price` | Sim | Float | O preço unitário da variante do produto no momento da visualização. |
| `metadata` | Não | Object | Campo de metadados adicionais sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos o SKU. <br> Terá um limite baseado no nosso limite geral de propriedades de evento de 50 kb. |
| `sku` | Não | String | (Somente Shopify) SKU do Shopify. Pode ser configurado como o campo de ID do catálogo. |
| `source` | Sim | String | Origem de onde o evento é derivado. (Para Shopify, é storefront). |
| `metadata` | Não | Object |  |
| `checkout_url` | Não | String | URL da página de checkout. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemplos de objetos

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

Em versões mais recentes do SDK, chame `logEcommerceEvent()`:

```javascript
braze.logEcommerceEvent({ 
    "name": "ecommerce.checkout_started", 
    "properties": {
        "checkout_id": "checkout_abc123",
        "cart_id": "cart_12345",
        "total_value": 199.98,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "Wireless Headphones",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199.98,
                "metadata": {
                    "sku": "WH-BLK-PRO",
                    "color": "Black",
                    "brand": "BrazeAudio"
                }
            }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
            "checkout_url": "https://checkout.braze-audio.com/abc123"
        }
    }
});
```

Em versões legadas do SDK, chame `logCustomEvent()`:

```javascript
braze.logCustomEvent("ecommerce.checkout_started", {
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "subtotal_value": 179.98,
    "tax": 15.00,
    "shipping": 5.00,
    "currency": "USD",
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("checkout_id", "checkout_abc123")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 199.98)
    .addProperty("subtotal_value", 179.98)
    .addProperty("tax", 15.00)
    .addProperty("shipping", 5.00)
    .addProperty("currency", "USD")
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("checkout_url", "https://checkout.braze-audio.com/abc123"));

Braze.getInstance(context).logCustomEvent("ecommerce.checkout_started", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "subtotal_value": 179.98,
    "tax": 15.00,
    "shipping": 5.00,
    "currency": "USD",
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.checkout_started", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.checkout_started",
      "time": "2024-01-15T09:25:45Z",
      "properties": {
        "checkout_id": "checkout_abc123",
        "cart_id": "cart_12345",
        "total_value": 199.98,
        "subtotal_value": 179.98,
        "tax": 15.00,
        "shipping": 5.00,
        "currency": "USD",
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "checkout_url": "https://checkout.braze-audio.com/abc123"
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_placed %}

Você pode usar o evento de pedido realizado para disparar quando um cliente conclui com sucesso o processo de checkout e faz um pedido.

#### Propriedades

| Nome da propriedade | Obrigatória | Tipo de dado | Descrição | 
|---|---|---|---|
| `order_id` | Sim | String | Identificador único para o pedido realizado. |
| `cart_id` | Não | String | Se você não está usando uma plataforma de terceiros que fornece um `cart_id`, pode usar o [ID de sessão da Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions). |
| `total_value` | Sim | Float | Valor monetário total do carrinho. |
| `subtotal_value` | Não | Float | Valor do subtotal do pedido após descontos e antes de impostos e frete. |
| `tax` | Não | Float | Total de impostos aplicados ao pedido. |
| `shipping` | Não | Float | Custo total de frete do pedido. |
| `currency` | Sim | String | Moeda em que o carrinho é avaliado. |
| `total_discounts` | Não | Float | Valor total de descontos aplicados ao pedido. | 
| `discounts`| Não | Array of objects | Lista detalhada de descontos aplicados ao pedido. |
| `products` | Sim | Array of objects |  |
| `product_id` | Sim | String | Um identificador único para o produto que foi visualizado. Esse valor pode ser o ID do produto ou SKU. |
| `product_name` | Sim | String | O nome do produto que foi visualizado. |
| `variant_id` | Sim | String | Um identificador único para a variante do produto. Um exemplo é `shirt_medium_blue` |
| `image_url` | Não | String | URL da imagem do produto. |
| `product_url` | Não | String | URL da página do produto para mais detalhes. |
| `quantity` | Sim | Integer | Número de unidades do produto no carrinho. |
| `price` | Sim | Float | O preço unitário da variante do produto no momento da visualização. |
| `metadata` | Não | Object | Campo de metadados adicionais sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos o SKU. <br> Terá um limite baseado no nosso limite geral de propriedades de evento de 50 kb. |
| `sku` | Não | String | (Somente Shopify) SKU do Shopify. Pode ser configurado como o campo de ID do catálogo. |
| `source` | Sim | String | Origem de onde o evento é derivado. (Para Shopify, é storefront). |
| `order_status_url` | Não | String | URL para visualizar o status do pedido. |
| `order_number` | Não | String | (Somente Shopify) Número único do pedido realizado. |
| `tags` | Não | Array | (Somente Shopify) Tags do pedido. |
| `referring_site` | Não | String | (Somente Shopify) O site de origem do pedido (como Meta). |
| `payment_gateway_names` | Não | Array | (Somente Shopify) Origem do sistema de pagamento (como ponto de venda ou celular). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemplos de objetos

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

Em versões mais recentes do SDK, chame `logEcommerceEvent()`:

```javascript
braze.logEcommerceEvent({ 
    "name": "ecommerce.order_placed", 
    "properties": {
        "order_id": "order_67890",
        "cart_id": "cart_12345",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
            {
                "code": "SAVE10",
                "amount": 10.00
            }
        ],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "Wireless Headphones",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199.98,
                "metadata": {
                    "sku": "WH-BLK-PRO",
                    "color": "Black",
                    "brand": "BrazeAudio"
                }
            }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
            "order_status_url": "https://braze-audio.com/orders/67890/status",
            "order_number": "ORD-2024-001234",
            "tags": ["electronics", "audio"],
            "referring_site": "https://www.e-referrals.com",
            "payment_gateway_names": ["tap2pay", "dotcash"]
        }
    }
});
```

Em versões legadas do SDK, chame `logCustomEvent()`:

```javascript
braze.logCustomEvent("ecommerce.order_placed", {
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "subtotal_value": 169.98,
    "tax": 14.40,
    "shipping": 5.60,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 189.98)
    .addProperty("subtotal_value", 169.98)
    .addProperty("tax", 14.40)
    .addProperty("shipping", 5.60)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("electronics").put("audio"))
        .put("referring_site", "https://www.e-referrals.com")
        .put("payment_gateway_names", new JSONArray().put("tap2pay").put("dotcash")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_placed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "subtotal_value": 169.98,
    "tax": 14.40,
    "shipping": 5.60,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_placed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_placed",
      "time": "2024-01-15T09:35:20Z",
      "properties": {
        "order_id": "order_67890",
        "cart_id": "cart_12345",
        "total_value": 189.98,
        "subtotal_value": 169.98,
        "tax": 14.40,
        "shipping": 5.60,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["electronics", "audio"],
          "referring_site": "https://www.e-referrals.com",
          "payment_gateway_names": ["tap2pay", "dotcash"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_refunded %}

Você pode usar o evento de pedido reembolsado para disparar quando um pedido é parcial ou totalmente reembolsado.

#### Propriedades

| Nome da propriedade       | Obrigatória | Tipo de dado | Descrição   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | Sim      | String    | Identificador único para o pedido realizado.        |
| `total_value`         | Sim      | Float     | Valor monetário total do carrinho.    |
| `currency`            | Sim      | String    | Moeda em que o carrinho é avaliado.    |
| `total_discounts`     | Não       | Float     | Valor total de descontos aplicados ao pedido.   |
| `discounts`           | Não       | Array of objects     | Lista detalhada de descontos aplicados ao pedido. |
| `products`            | Sim      | Array of objects     |  |
| `product_id`       | Sim      | String    | Um identificador único para o produto que foi visualizado. Esse valor pode ser o ID do produto, SKU ou similar. <br>Se um reembolso parcial for emitido e não houver um `product_id` atribuído ao reembolso (por exemplo, um reembolso no nível do pedido), forneça um `product_id` genérico.             |
| `product_name`     | Sim      | String    | O nome do produto que foi visualizado.                                                                      |
| `variant_id`       | Sim      | String    | Um identificador único para a variante do produto (como `shirt_medium_blue`).                                         |
| `image_url`        | Não       | String    | URL da imagem do produto.     |
| `product_url`      | Não       | String    | URL da página do produto para mais detalhes.  |
| `quantity`         | Sim      | Integer   | Número de unidades do produto no carrinho.   |
| `price`            | Sim      | Float     | O preço unitário da variante do produto no momento da visualização.  |
| `metadata`         | Não       | Object    | Campo de metadados adicionais sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos o SKU. Terá um limite baseado no nosso limite geral de propriedades de evento de 50 kb. |
| `sku`            | Não       | String    | (Somente Shopify) SKU do Shopify. Pode ser configurado como o campo de ID do catálogo.  |
| `source`              | Sim      | String    | Origem de onde o evento é derivado. (Para Shopify, é storefront).    |
| `metadata`            | Não       | Object    |                |
| `order_status_url`  | Não       | String    | URL para visualizar o status do pedido.     |
| `order_note`       | Não       | String    | (Somente Shopify) Nota adicionada ao pedido pelo lojista.    |
| `order_number`     | Não       | String    | (Somente Shopify) Número único do pedido realizado.   |
| `tags`             | Não       | Array     | (Somente Shopify) Tags do pedido.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemplos de objetos

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_refunded", {
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": [
        {
            "code": "SAVE5",
            "amount": 5.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE5")
    .put("amount", 5.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("total_value", 99.99)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 5.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_note", "Customer requested refund due to defective item")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("refund").put("defective")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_refunded", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE5",
        "amount": 5.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 99.99,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_refunded", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_refunded",
      "time": "2024-01-15T10:15:30Z",
      "properties": {
        "order_id": "order_67890",
        "total_value": 99.99,
        "currency": "USD",
        "total_discounts": 5.00,
        "discounts": [
          {
            "code": "SAVE5",
            "amount": 5.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_note": "Customer requested refund due to defective item",
          "order_number": "ORD-2024-001234",
          "tags": ["refund", "defective"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_cancelled %}

Você pode usar o evento de pedido cancelado para disparar quando um cliente cancela um pedido.

#### Propriedades

| Nome da propriedade      | Obrigatória | Tipo de dado | Descrição       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | Sim      | String    | Identificador único para o pedido realizado.              |
| `cancel_reason`       | Sim      | String    | Motivo pelo qual o pedido foi cancelado.           |
| `total_value`         | Sim      | Float     | Valor monetário total do carrinho.         |
| `subtotal_value`      | Não       | Float     | Valor do subtotal do pedido após descontos e antes de impostos e frete. |
| `tax`                 | Não       | Float     | Total de impostos aplicados ao pedido. |
| `shipping`            | Não       | Float     | Custo total de frete do pedido. |
| `currency`            | Sim      | String    | Moeda em que o carrinho é avaliado.           |
| `total_discounts`     | Não       | Float     | Valor total de descontos aplicados ao pedido.     |
| `discounts`           | Não       | Array of objects     | Lista detalhada de descontos aplicados ao pedido.             |
| `products`            | Sim      | Array of objects     |         |
| `product_id`          | Sim      | String    | Um identificador único para o produto que foi visualizado. Esse valor pode ser o ID do produto, SKU ou similar.             |
| `product_name`        | Sim      | String    | O nome do produto que foi visualizado.          |
| `variant_id`          | Sim      | String    | Um identificador único para a variante do produto (como `shirt_medium_blue`).        |
| `image_url`           | Não       | String    | URL da imagem do produto.           |
| `product_url`         | Não       | String    | URL da página do produto para mais detalhes.                                                                     |
| `quantity`            | Sim      | Integer   | Número de unidades do produto no carrinho.        |
| `price`               | Sim      | Float     | O preço unitário da variante do produto no momento da visualização.     |
| `metadata`            | Não       | Object    | Campo de metadados adicionais sobre o produto que o cliente deseja adicionar para seus casos de uso. Para Shopify, adicionaremos o SKU. Terá um limite baseado no nosso limite geral de propriedades de evento de 50 kb. |
| `sku`                 | Não       | String    | (Somente Shopify) SKU do Shopify. Pode ser configurado como o campo de ID do catálogo.        |
| `source`              | Sim      | String    | Origem de onde o evento é derivado. (Para Shopify, é storefront).    |
| `metadata`            | Não       | Object    |       |
| `order_status_url`    | Não       | String    | URL para visualizar o status do pedido.                                                                          |
| `order_number`        | Não       | String    | (Somente Shopify) Número único do pedido realizado.  |
| `tags`                | Não       | Array     | (Somente Shopify) Tags do pedido.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Exemplos de objetos

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_cancelled", {
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "subtotal_value": 169.98,
    "tax": 14.40,
    "shipping": 5.60,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cancel_reason", "customer changed mind")
    .addProperty("total_value", 189.98)
    .addProperty("subtotal_value", 169.98)
    .addProperty("tax", 14.40)
    .addProperty("shipping", 5.60)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("cancelled").put("customer_request")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_cancelled", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "subtotal_value": 169.98,
    "tax": 14.40,
    "shipping": 5.60,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_cancelled", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_cancelled",
      "time": "2024-01-15T10:45:15Z",
      "properties": {
        "order_id": "order_67890",
        "cancel_reason": "customer changed mind",
        "total_value": 189.98,
        "subtotal_value": 169.98,
        "tax": 14.40,
        "shipping": 5.60,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["cancelled", "customer_request"]
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

## Modelos de Canvas para eCommerce

A Braze criou modelos de Canvas pré-construídos que são alimentados por eventos recomendados de eCommerce, como o direcionamento de clientes que iniciaram o processo de checkout mas saíram antes de finalizar o pedido. Você pode usar esses eventos para tomar decisões informadas e aprimorar a jornada do usuário, personalizando mensagens e direcionando públicos específicos.

Confira nossos [casos de uso de eCommerce]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/) dedicados para mais formas de usar esses eventos com modelos de Canvas.

## Campos calculados do usuário

Usamos cálculos padronizados de campos do usuário para os seguintes campos:

- **Receita total** = soma do valor total de pedidos realizados - soma do valor total de pedidos reembolsados
- **Total de pedidos** = contagem de eventos distintos de pedido realizado - contagem de cancelamentos de pedido distintos
- **Valor total de reembolsos** = soma do valor total de pedidos reembolsados

Esses campos calculados do usuário também estão incluídos na guia **Transações** dos perfis de usuário.

![A guia "Transações" com campos calculados do usuário.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:70%;"}

## Perguntas frequentes

### Onde posso visualizar dados de compra no nível do produto?

A guia **Transações** do perfil do usuário mostra campos calculados de alto nível (como receita total e total de pedidos). Para visualizar detalhes no nível do produto de um usuário específico, use o [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) para consultar dados de eventos de eCommerce, ou exporte dados de eventos por meio do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/).

Diferentemente dos eventos de compra legados, os eventos recomendados de eCommerce armazenam detalhes do produto como propriedades de evento aninhadas dentro do array `products`. Essas propriedades estão disponíveis no envio de mensagens por meio de Liquid e na segmentação por meio de [Extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension/).

### Como segmento usuários por um produto específico?

O segmentador permite filtrar pelo número de vezes que um usuário realizou um evento de eCommerce. Para filtrar por propriedades específicas do produto (como `product_id` ou `product_name`), use [Extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension/), que suportam filtragem de propriedades de evento aninhadas. Por exemplo, você pode encontrar todos os usuários que compraram o produto "SKU-123" nos últimos 90 dias.

### Qual é a diferença entre eventos de compra legados e eventos recomendados de eCommerce?

Os eventos de compra legados usam o [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) da Braze e registram compras individuais de produtos com um `product_id` e `price`. Os eventos recomendados de eCommerce (como `ecommerce.order_placed`) usam propriedades de eventos personalizados e capturam o contexto completo do pedido, incluindo múltiplos produtos, descontos e metadados em um único evento.

Com o lançamento dos eventos recomendados de eCommerce, a Braze descontinuará o evento de compra legado no futuro. Se você está usando eventos de compra atualmente, receberá um aviso prévio. Enquanto isso, você pode continuar usando eventos de compra até a data oficial de descontinuação. Consulte a [visão geral de eventos recomendados]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/) para mais detalhes.

### Posso adicionar propriedades personalizadas aos eventos recomendados de eCommerce?

Os eventos recomendados de eCommerce possuem um esquema definido com campos obrigatórios e opcionais. Você pode incluir dados personalizados adicionais dentro do objeto `metadata` de cada evento. No entanto, tags personalizadas no nível do pedido ou campos proprietários (como canal de compra ou informações de loja física) não são suportados como propriedades de nível superior. Se você precisa desses campos para segmentação, continue enviando-os como eventos personalizados separados junto com seus eventos de eCommerce.

### Preciso incluir external_id ao enviar eventos de eCommerce?

Depende de como você está enviando os eventos:

- **Via SDK**: Não. Quando você usa um SDK da Braze, os eventos são automaticamente associados ao contexto do usuário atual do SDK (anônimo ou identificado). Você não precisa passar um identificador de usuário em cada chamada de evento. Em vez disso, pode identificar o usuário para esse contexto usando métodos como `changeUser`.
- **Via API REST** (`/users/track`): Sim. Cada requisição de API deve incluir um identificador de usuário, como `external_id`, `braze_id`, `user_alias`, `email` ou `phone`, porque a API não tem um contexto de "usuário atual".

### Por que as propriedades aninhadas de produto não aparecem no dropdown de configuração de Recomendação de item de IA?

Ao configurar [recomendações de item de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/), o dropdown **Nome da propriedade** lista apenas propriedades de evento de nível superior (como `order_id`, `total_value` e `currency`). Propriedades aninhadas dentro do array `products` (por exemplo, `products.product_id` ou `products.variant_id`) podem não aparecer nessa lista, mas você pode digitá-las manualmente usando notação de ponto no campo. Para a maioria das implementações de eCommerce, a Braze recomenda usar `products.product_id` como identificador do item e combiná-lo com um [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/) cujos IDs de item correspondam aos seus valores de `product_id` ou `variant_id`.

### Por que alguns dos meus eventos de eCommerce não estão aparecendo na Braze?

Se os eventos não estão aparecendo nos perfis de usuário ou nos logs, verifique o seguinte:

- **Timing de envio de dados do SDK**: O SDK da Braze armazena dados localmente e faz upload periodicamente (normalmente entre 10 e 60 segundos). Chame `requestImmediateDataFlush()` após `logCustomEvent()` para forçar um upload imediato.
- **Propriedades obrigatórias**: Os eventos de eCommerce possuem propriedades obrigatórias. Se uma propriedade obrigatória estiver ausente ou com um tipo de dado inválido, o evento pode ser rejeitado. Verifique se a carga útil do seu evento corresponde ao [esquema obrigatório](#types-of-ecommerce-recommended-events).
- **Precisão no nome do evento**: Os nomes dos eventos de eCommerce diferenciam maiúsculas de minúsculas e devem corresponder exatamente (por exemplo, `ecommerce.checkout_started`, não `ecommerce.checkoutStarted`).