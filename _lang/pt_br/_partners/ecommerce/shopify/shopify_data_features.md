---
nav_title: Recursos de dados da Shopify
article_title: Recursos de dados da Shopify
description: "Este artigo de referência aborda os recursos de dados da Shopify."
page_type: partner
search_tag: Partner
alias: /shopify_data_features/
page_order: 4
---

# Recursos de dados da Shopify {#shopify-data-features}

> Este artigo fornece uma visão geral dos nossos recursos da Shopify, incluindo quais dados da Shopify são rastreados e exemplos de cargas úteis, backfill histórico e sincronizações de produtos.

## Eventos rastreados do Shopify {#tracked-shopify-events}

A integração com o Shopify usa [eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) para capturar comportamentos de compra essenciais. Para exemplos de implementação e estratégias de marketing usando esses eventos, consulte [casos de uso de eCommerce]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases).

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

{% tabs %}
{% tab Carga útil de exemplo %}
{% subtabs global %}
{% subtab Product viewed %}
```json
{
    "name": "ecommerce.product_viewed",
    "properties": {
        "product_id": "12345",
        "product_name": "product",
        "variant_id": "123",
        "image_url": "www.image-url.com",
        "product_url": "mystorefront.myshopify.com/product",
        "price": 10,
        "currency": "USD",
        "source": "mystorefront.myshopify.com",
        "metadata": {
          "sku": "sku"
        },
        "type": [
          "price_drop",
          "back_in_stock"
        ]
    }
}
```
{% endsubtab %}
{% subtab Cart updated %}
```json
{
    "name": "ecommerce.cart_updated",
    "properties": {
        "cart_id": "Z2NwLXVzLWVhc3QxOjAxSjk3UFg4RlFZMjVTVkRHRlc1RlI3SlRY",
        "currency": "USD",
        "total_value": 2000000,
        "products": [
            {
                "product_id": "8266836345064",
                "product_name": "PANTS!!!",
                "variant_id": "44610569208040",
                "image_url": "https://cdn.shopify.com/s/files/1/0604/4211/6328/files/1200px-Trousers-colourisolated.jpg?v=1689256168",
                "product_url": "https://test-store.myshopify.com/products/pants?variant=44610569208040",
                "quantity": 2,
                "price": 1000000,
                "metadata": {
                    "sku": "007"
                }
            }
        ],
        "source": "https://test-store.myshopify.com",
        "metadata": {}
    }
}
```
{% endsubtab %}
{% subtab Checkout started %}
```json
{
    "name": "ecommerce.checkout_started",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "subtotal_value": 396.88,
        "tax": 15.00,
        "shipping": 10.00,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "checkout_id": "123123123",
        "metadata": {
            "checkout_url": "https://checkout.local/548380009/checkouts/123123123/recover?key=example-secret-token"
        }
    }
}
```
{% endsubtab %}
{% subtab Order placed %}
{% raw %}
```json
{
    "name": "ecommerce.order_placed",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "subtotal_value": 396.88,
        "tax": 15.00,
        "shipping": 10.00,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": "1234",
            "tags": [
                "heavy",
                "heavy2"
            ],
            "referring_site": "https://www.google.com",
            "payment_gateway_names": [
                "visa",
                "bogus"
            ]
        }
    }
}
```
{% endraw %}
{% endsubtab %}
{% subtab Fulfilled order %}
```json
{
 "name": "shopify_fulfilled_order",
 "time": "2022-05-23T14:44:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
  "variant_id": 40094740549876,
       "variant_title": "Small Dark Denim Top",


       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": "2022-05-23T14:44:34-04:00",
   "fulfillment_status": "fulfilled",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "456",
       "tracking_numbers": [
         "456"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "Small Dark Denim Top",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Partially fulfilled order %}
```json
{
 "name": "shopify_partially_fulfilled_order",
 "time": "2022-05-23T14:43:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": null,
   "fulfillment_status": "partial",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "123",
       "tracking_numbers": [
         "123"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "properties": [],
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "abc123abc123"
}
```
{% endsubtab %}
{% subtab Paid order %}
```json
{
 "name": "shopify_paid_order",
 "time": "2022-05-23T13:52:38-04:00",
 "properties": {
   "order_id": 4444596371647,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": null,
       "vendor": "partners-demo",
       "name": "LED High Tops",
       "properties": [],
       "price": "80.00",
       "fulfillment_status": null
     }
   ]
 }
}
```
{% endsubtab %}
{% subtab Order cancelled %}
```json
{
    "name": "ecommerce.order_cancelled",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cancel_reason": "no longer necessary",
        "total_value": 421.88,
        "subtotal_value": 396.88,
        "tax": 15.00,
        "shipping": 10.00,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": "1234",
            "tags": [
                "heavy",
                "heavy2"
            ]
        }
    }
}
```
{% endsubtab %}
{% subtab Order refunded %}
```json
{
    "name": "ecommerce.order_refunded",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "total_value": 421.88,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
		"order_note": "item was broken"
        }
    }
}
```
{% endsubtab %}
{% subtab Account login %}
```json
{
	"name": "shopify_account_login",
	"properties": {
	"source": "braze-mock-storefront.myshopify.com"
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Eventos Shopify %}

{% alert note %}
A Braze depende do Shopify para fornecer as propriedades de evento necessárias (como `cart_id` ou `cart_token`) para eventos de eCommerce. Em casos raros, problemas temporários no Shopify podem fazer com que essas propriedades não sejam enviadas, o que pode causar a perda dos eventos afetados.
{% endalert %}

{% subtabs global %}
{% subtab Product viewed %}
**Evento**: `ecommerce.product_viewed`<br>
**Tipo**: Evento recomendado<br>
**Disparado**: Quando um cliente visualiza a página de um produto<br>
**Fonte de dados**: SDKs da Braze<br>
**Caso de uso**: Abandono de navegação

{% raw %}
| Variável | Template Liquid |
| --- | --- |
|------------------|-----------------------------------------------------|
| `product_id`       | `{{event_properties.${product_id}}}`                |
| `product_name `    | `{{event_properties.${product_name}}}`              |
| `variant_id`       | `{{event_properties.${variant_id}}}`                |
| `image_url `       | `{{event_properties.${image_url}}}`                 |
| `product_url`      | `<your-store.myshopify.com>{{event_properties.${product_url}}}` <br><br>Adicione o domínio do seu site Shopify antes da URL. |
| `price`            | `{{event_properties.${price}}}`                     |
| `currency`         | `{{event_properties.${currency}}}`                  |
| `source`           | `{{event_properties.${source}}}`                    |
| `sku`              | `{{event_properties.${metadata}[0].sku}}`          |
| `type`             | `event_properties.${type}`          |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos rastreados do Shopify" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**Evento**: `ecommerce.cart_updated`<br>
**Tipo**: Evento recomendado<br>
**Disparado**: Quando um cliente adiciona, remove ou atualiza itens no carrinho de compras<br>
**Fonte de dados**: SDKs da Braze<br>
**Caso de uso**: Abandono de carrinho

Para Canvas de carrinho abandonado, primeiro é necessário adicionar a Liquid tag inicial do carrinho de compras para obter o contexto do carrinho na sua mensagem.

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

Em seguida, você pode adicionar as seguintes Liquid tags do carrinho de compras à sua mensagem.

{% raw %}
| Variável         | Template Liquid                                   |
|------------------|-----------------------------------------------------|
| `cart_id`          | `{{ shopping_cart.cart_id }}`                       |
| `currency`         | `{{ shopping_cart.currency }}`                      |
| `total_value`      | `{{ shopping_cart.total_value }}`                   |
| `product_id`       | `{{ shopping_cart.products[0].product_id }}`       |
| `product_name`     | `{{ shopping_cart.products[0].product_name }}`     |
| `variant_id`       | `{{ shopping_cart.products[0].variant_id }}`       |
| `image_url`        | `{{ shopping_cart.products[0].image_url }}`        |
| `product_url`      | `{{ shopping_cart.products[0].product_url }}`      |
| `quantity`         | `{{ shopping_cart.products[0].quantity }}`         |
| `price`            | `{{ shopping_cart.products[0].price }}`            |
| `sku`              | `{{ shopping_cart.products[0].metadata[0].sku }}`  |
| `source`           | `{{ shopping_cart.source }}`                        |
| `metadata (value)` | `{{ shopping_cart.metadata[0].<add_value_here> }}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos rastreados do Shopify" }
{% endraw %}

{% alert tip %}
Para saber mais sobre como criar um loop Liquid `for` para adicionar dinamicamente todos os produtos ao seu e-mail, consulte [Personalização de produtos de carrinho abandonado para e-mails]({{site.baseurl}}/ecommerce_use_cases#abandoned-cart).
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**Evento**: `ecommerce.checkout_started`<br>
**Tipo**: Evento recomendado<br>
**Disparado**: Quando um usuário navega até a página de checkout<br>
**Fonte de dados**: REST API da Braze<br>
**Caso de uso**: Abandono de checkout

{% alert important %}
Se um cliente usar o Shop Pay como opção de checkout acelerado, o Shopify pode ignorar certos eventos padrão de checkout (como o webhook de checkout iniciado do Shopify). Isso significa que a Braze pode não receber os dados necessários para adicionar o alias do token de checkout, o que pode impactar o rastreamento de abandono de checkout e a reconciliação do perfil de usuário.
{% endalert %}

Para Canvas de checkout abandonado, primeiro é necessário usar a seguinte Liquid tag:

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

Em seguida, você pode adicionar as seguintes Liquid tags à sua mensagem para referenciar os produtos no carrinho no momento do checkout.

{% raw %}
| Variável         | Template Liquid                                   |
|------------------|-----------------------------------------------------|
| `cart_id`          | `{{ shopping_cart.cart_id }}`                       |
| `currency`         | `{{ shopping_cart.currency }}`                      |
| `total_value`      | `{{ shopping_cart.total_value }}`                   |
| `product_id`       | `{{ shopping_cart.products[0].product_id }}`       |
| `product_name`     | `{{ shopping_cart.products[0].product_name }}`     |
| `variant_id`       | `{{ shopping_cart.products[0].variant_id }}`       |
| `image_url`        | `{{ shopping_cart.products[0].image_url }}`        |
| `product_url`      | `{{ shopping_cart.products[0].product_url }}`      |
| `quantity`         | `{{ shopping_cart.products[0].quantity }}`         |
| `price`            | `{{ shopping_cart.products[0].price }}`            |
| `sku`              | `{{ shopping_cart.products[0].metadata.sku }}`     |
| `source`           | `{{ shopping_cart.source }}`                        |
| `checkout_url`     | `{{ shopping_cart.metadata[0].checkout_url }}`     |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos rastreados do Shopify" }
{% endraw %}

{% endsubtab %}
{% subtab Order placed %}
**Evento**: `ecommerce.order_placed`<br>
**Tipo**: Evento recomendado<br>
**Disparado**: Quando um usuário conclui o processo de checkout com sucesso e realiza um pedido<br>
**Fonte de dados**: REST API da Braze<br>
**Caso de uso**: Confirmação de pedido, redirecionamento pós-compra, upsells ou cross-sells

{% raw %}
| Variável                | Template Liquid                                   |
|-------------------------|-----------------------------------------------------|
| cart_id                 | `{{event_properties.${cart_id}}}`                   |
| currency                | `{{event_properties.${currency}}}`                  |
| discounts               | `{{event_properties.${discounts}}}`                 |
| order_id                | `{{event_properties.${order_id}}}`                  |
| product_id              | `{{event_properties.${products}[0].product_id}}`   |
| product_name            | `{{event_properties.${products}[0].product_name}}` |
| variant_id              | `{{event_properties.${products}[0].variant_id}}`   |
| quantity                | `{{event_properties.${products}[0].quantity}}`     |
| sku                     | `{{event_properties.${products}[0].metadata.sku}}` |
| total_discounts         | `{{event_properties.${total_discounts}}}`           |
| order_status_url        | `{{event_properties.${metadata}.order_status_url}}` |
| order_number            | `{{event_properties.${metadata}.order_number}}`     |
| tags                    | `{{event_properties.${metadata}.tags}}`             |
| referring_site          | `{{event_properties.${metadata}.referring_site}}`   |
| payment_gateway_names    | `{{event_properties.${metadata}.payment_gateway_names}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos rastreados do Shopify" }
{% endraw %}

{% alert tip %}
O webhook de checkout concluído do Shopify não contém URLs de produtos ou URLs de imagens. Por isso, é necessário usar a personalização Liquid de catálogos, conforme descrito em [Personalização de produtos de carrinho abandonado para e-mails]({{site.baseurl}}/ecommerce_use_cases#order-confirmation-and-feedback-survey).
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**Evento**: `shopify_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**Disparado**: Quando o pedido de um usuário é processado e está pronto para envio<br>
**Fonte de dados**: REST API da Braze<br>
**Caso de uso**: (Transacional) Atualização de processamento

{% raw %}
| Variável | Template Liquid |
| --- | --- |
| ID do pedido | `{{event_properties.${order_id}}}` |
| Preço total | `{{event_properties.${total_price}}}` |
| Total de descontos | `{{event_properties.${total_discounts}}}` |
| Status de confirmação | `{{event_properties.${confirmed}}}` |
| URL de status do pedido | `{{event_properties.${order_status_url}}}` |
| Número do pedido | `{{event_properties.${order_number}}}` |
| Data/hora de cancelamento | `{{event_properties.${cancelled_at}}}` |
| Data/hora de fechamento | `{{event_properties.${closed_at}}}` |
| ID do item | `{{event_properties.${line_items}[0].product_id}}` |
| Quantidade do item | `{{event_properties.${line_items}[0].quantity}}` |
| SKU do item | `{{event_properties.${line_items}[0].sku}}` |
| Título do item | `{{event_properties.${line_items}[0].title}}` |
| Fornecedor do item | `{{event_properties.${line_items}[0].vendor}}` |
| Nome do item | `{{event_properties.${line_items}[0].name}}` |
| Propriedades do item | `{{event_properties.${line_items}[0].properties}}` |
| Preço do item | `{{event_properties.${line_items}[0].price}}` |
| Título do frete | `{{event_properties.${shipping}[0].title}}` |
| Preço do frete | `{{event_properties.${shipping}[0].price}}` |
| Status de processamento | `{{event_properties.${fulfillment_status}}}` |
| Status de envio do processamento | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Status | `{{event_properties.${fulfillments}[0].status}}` |
| Transportadora do processamento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Número de rastreamento do processamento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Números de rastreamento do processamento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| URL de rastreamento do processamento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| URLs de rastreamento do processamento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| Status de processamento | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nome do processamento | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Preço do processamento | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| ID do produto do processamento | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Quantidade do processamento | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Envio do processamento | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| SKU do processamento | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Título do processamento | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fornecedor do processamento | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título da variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos rastreados do Shopify" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**Evento**: `shopify_partially_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**Disparado**: Quando parte do pedido de um usuário é processada e está pronta para envio<br>
**Fonte de dados**: REST API da Braze<br>
**Caso de uso**: (Transacional) Atualização de processamento

{% raw %}
| Variável | Template Liquid |
| --- | --- |
| ID do pedido | `{{event_properties.${order_id}}}` |
| Preço total | `{{event_properties.${total_price}}}` |
| Total de descontos | `{{event_properties.${total_discounts}}}` |
| Status de confirmação | `{{event_properties.${confirmed}}}` |
| URL de status do pedido | `{{event_properties.${order_status_url}}}` |
| Número do pedido | `{{event_properties.${order_number}}}` |
| Data/hora de cancelamento | `{{event_properties.${cancelled_at}}}` |
| Data/hora de fechamento | `{{event_properties.${closed_at}}}` |
| ID do item | `{{event_properties.${line_items}[0].product_id}}` |
| Quantidade do item | `{{event_properties.${line_items}[0].quantity}}` |
| SKU do item | `{{event_properties.${line_items}[0].sku}}` |
| Título do item | `{{event_properties.${line_items}[0].title}}` |
| Fornecedor do item | `{{event_properties.${line_items}[0].vendor}}` |
| Nome do item | `{{event_properties.${line_items}[0].name}}` |
| Propriedades do item | `{{event_properties.${line_items}[0].properties}}` |
| Preço do item | `{{event_properties.${line_items}[0].price}}` |
| Título do frete | `{{event_properties.${shipping}[0].title}}` |
| Preço do frete | `{{event_properties.${shipping}[0].price}}` |
| Status de processamento | `{{event_properties.${fulfillment_status}}}` |
| Status de envio do processamento | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Status do processamento | `{{event_properties.${fulfillments}[0].status}}` |
| Transportadora do processamento | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Número de rastreamento do processamento | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Números de rastreamento do processamento | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| URL de rastreamento do processamento | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| URLs de rastreamento do processamento | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| Status de processamento | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nome do processamento | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Preço do processamento | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| ID do produto do processamento | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Quantidade do processamento | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Envio do processamento | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| SKU do processamento | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Título do processamento | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fornecedor do processamento | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título da variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos rastreados do Shopify" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**Evento**: `shopify_paid_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**Disparado**: Quando o pedido de um usuário é marcado como pago no Shopify<br>
**Fonte de dados**: REST API da Braze<br>
**Caso de uso**: (Transacional) Confirmação de pagamento

{% raw %}
| Variável | Template Liquid |
| --- | --- |
| ID do pedido | `{{event_properties.${order_id}}}` |
| Status de confirmação | `{{event_properties.${confirmed}}}` |
| URL de status do pedido | `{{event_properties.${order_status_url}}}` |
| Número do pedido | `{{event_properties.${order_number}}}` |
| Data/hora de cancelamento | `{{event_properties.${cancelled_at}}}` |
| Total de descontos | `{{event_properties.${total_discounts}}}` |
| Preço total | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Códigos de desconto | `{{event_properties.${discount_codes}}}` |
| ID do item | `{{event_properties.${line_items}[0].product_id}}` |
| Quantidade do item | `{{event_properties.${line_items}[0].quantity}}` |
| SKU do item | `{{event_properties.${line_items}[0].sku}}` |
| Título do item | `{{event_properties.${line_items}[0].title}}` |
| Fornecedor do item | `{{event_properties.${line_items}[0].vendor}}` |
| Propriedades do item | `{{event_properties.${line_items}[0].properties}}` |
| Preço do item | `{{event_properties.${line_items}[0].price}}` |
| Título do frete | `{{event_properties.${shipping}[0].title}}` |
| Preço do frete | `{{event_properties.${shipping}[0].price}}` |
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título da variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos rastreados do Shopify" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**Evento**: `ecommerce.order_cancelled`<br>
**Tipo**: Evento recomendado<br>
**Disparado**: Quando o pedido de um usuário é cancelado<br>
**Fonte de dados**: REST API da Braze<br>
**Caso de uso**: (Transacional) Confirmação de cancelamento de pedido

{% raw %}
| Variável | Template Liquid |
| --- | --- |
| ID do pedido | `{{event_properties.${order_id}}}` |
| Preço total | `{{event_properties.${total_price}}}` |
| Total de descontos | `{{event_properties.${total_discounts}}}` |
| Confirmado | `{{event_properties.${confirmed}}}` |
| URL de status do pedido | `{{event_properties.${order_status_url}}}` |
| Número do pedido | `{{event_properties.${order_number}}}` |
| Data/hora de cancelamento | `{{event_properties.${cancelled_at}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Códigos de desconto | `{{event_properties.${discount_codes}}}` |
| Status de processamento | `{{event_properties.${fulfillment_status}}}` |
| Processamentos | `{{event_properties.${fulfillments}}}` |
| ID do item | `{{event_properties.${line_items}[0].product_id}}` |
| Quantidade do item | `{{event_properties.${line_items}[0].quantity}}` |
| SKU do item | `{{event_properties.${line_items}[0].sku}}` |
| Título do item | `{{event_properties.${line_items}[0].title}}` |
| Fornecedor do item | `{{event_properties.${line_items}[0].vendor}}` |
| Nome do item | `{{event_properties.${line_items}[0].name}}` |
| Propriedades do item | `{{event_properties.${line_items}[0].properties}}` |
| Status de processamento | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Título do frete | `{{event_properties.${shipping}[0].title}}` |
| Preço do frete | `{{event_properties.${shipping}[0].price}}` |
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título da variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos rastreados do Shopify" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**Evento**: `ecommerce.order_refunded`<br>
**Tipo**: Evento recomendado<br>
**Disparado**: Quando o pedido de um usuário é reembolsado<br>
**Fonte de dados**: REST API da Braze<br>
**Caso de uso**: (Transacional) Confirmação de reembolso

{% raw %}
| Variável | Template Liquid |
| --- | --- |
| ID do pedido | `{{event_properties.${order_id}}}` |
| Nota do pedido | `{event_properties.${note}}}` |
| ID do item | `{{event_properties.${line_items}[0].product_id}}` |
| Quantidade do item | `{{event_properties.${line_items}[0].quantity}}` |
| SKU do item | `{{event_properties.${line_items}[0].sku}}` |
| Título do item | `{{event_properties.${line_items}[0].title}}` |
| Fornecedor do item | `{{event_properties.${line_items}[0].vendor}}` |
| Nome do item | `{{event_properties.${line_items}[0].name}}` |
| Propriedades do item | `{{event_properties.${line_items}[0].properties}}` |
| Preço do item | `{{event_properties.${line_items}[0].price}}` |
| ID da variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título da variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos rastreados do Shopify" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**Evento**: `shopify_account_login`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**Disparado**: Quando um usuário faz login na sua conta<br>
**Fonte de dados**: REST API da Braze<br>
**Caso de uso**: Série de boas-vindas

{% raw %}
| Variável | Template Liquid |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos rastreados do Shopify" }
{% endraw %}

{% alert note %}
A integração com o Shopify atualmente não suporta o preenchimento do [evento de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) da Braze. Por isso, filtros de compra, Liquid tags, disparos baseados em ação e análises de dados devem usar o evento `ecommerce.order_placed`.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Atributos personalizados do Shopify compatíveis {#supported-shopify-custom-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

{% tabs local %}
{% tab Exemplo de carga útil %}
{% subtabs %}
{% subtab Shopify Tags %}
```json
{
  "attributes": [
    {
      "shopify_tags": "VIP_customer",
      "shopify_total_spent": "60.00",
      "shopify_order_count": "3",
      "shopify_last_order_id": "1234567",
      "shopify_last_order_name": "test_order",
      "shopify_zipcode": "10001",
      "shopify_province": "null"
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Atributos personalizados do Shopify %}
| Nome do atributo | Descrição |
| --- | --- |
| `shopify_total_spent` | O valor total que o cliente gastou em todo o histórico de pedidos. |
| `shopify_order_count` | O número de pedidos associados a esse cliente. Pedidos de teste e arquivados não são contabilizados. |
| `shopify_last_order_id` | O ID do último pedido do cliente. |
| `shopify_last_order_name` | O nome do último pedido do cliente. Está diretamente relacionado ao campo `name` no recurso de pedido. |
| `shopify_zipcode` | O CEP do cliente a partir do endereço padrão. |
| `shopify_province` | O estado/província do cliente a partir do endereço padrão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados do Shopify compatíveis" }

{% alert important %}
Um problema conhecido na versão atual da API do Shopify impede que o atributo de usuário `shopify_last_order_name` seja preenchido corretamente. O impacto nos usuários é o seguinte:<br><br>

- **Usuários existentes:** Para qualquer usuário que já tenha um valor em `shopify_last_order_name`, esse valor é mantido, mas não é atualizado por pedidos subsequentes.
- **Novos usuários:** Para novos usuários, o campo não é preenchido e permanece vazio ou nulo.

Esta página será atualizada após o Shopify resolver esse problema.
{% endalert %}

### Personalização com Liquid {#liquid-personalization}

Para adicionar personalização com Liquid aos seus atributos personalizados do Shopify, selecione **+ Personalization**. Em seguida, selecione **Custom Attributes** como tipo de personalização.

![A seção "Add Personalization" com o menu suspenso "Attribute" expandido.]({% image_buster /assets/img/shopify/add_personalization_2.png %}){: style="max-width:40%;"}

Após selecionar seu atributo personalizado, insira um valor padrão e copie o snippet de Liquid na sua mensagem.

![Colando um snippet de Liquid em uma mensagem.]({% image_buster /assets/img/shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## Atributos padrão do Shopify compatíveis {#supported-shopify-standard-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

- E-mail
- Nome
- Sobrenome
- Telefone
- Cidade
- País

{% alert note %}
A Braze só atualizará os atributos personalizados do Shopify compatíveis e os atributos padrão da Braze se houver uma diferença nos dados em relação ao perfil de usuário existente. Por exemplo, se os dados recebidos do Shopify contiverem o nome Bob e Bob já existir como nome no perfil de usuário da Braze, a Braze não disparará uma atualização e você não será cobrado por um ponto de dados.
{% endalert %}

## Coleta de dados do SDK {#sdk-data-collection}

Para saber mais sobre quais dados são coletados pelos SDKs da Braze, consulte [Coleta de dados do SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection).

## Preenchimento de dados históricos {#historical-backfill}

> Os dados históricos do Shopify são importados antes de você conectar a Braze — eventos de pedidos dos últimos 90 dias e dados de clientes do último ano. Ambos os intervalos são contados a partir da data em que você conclui a integração.

Por meio da [configuração da integração padrão do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) ou da [configuração da integração personalizada do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration), você pode ativar o preenchimento de dados históricos para direcionar clientes anteriores. Isso importa seus pedidos do Shopify (eventos relacionados a pedidos) dos últimos 90 dias e perfis de usuário do último ano. Ambos os intervalos são contados a partir da data em que você conclui a integração.

Quando a Braze importa seus clientes do Shopify, atribuímos o tipo de `external_id` que você escolheu nas configurações.

{% alert note %}
Se você já é cliente da Braze com Campaigns ou Canvas ativos, analise como os clientes importados e os eventos de pedidos afetam seus Segments e jornadas antes de ativar o preenchimento de dados históricos.
{% endalert %}

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

### Configurando o preenchimento de dados históricos do Shopify {#setting-up-shopify-historical-backfill}

1. Ative o preenchimento de dados históricos na etapa **Track Shopify data**.

![A etapa "Track Shopify data" da integração do Shopify mostrando o preenchimento de dados históricos selecionado.]({% image_buster /assets/img/shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. Após concluir a configuração da integração, a Braze iniciará a sincronização inicial dos dados. Você pode acompanhar o progresso na guia **Shopify Data** das configurações de integração.

![A página de configurações de integração do Shopify com um indicador de carregamento mostrando que os eventos estão sendo sincronizados.]({% image_buster /assets/img/shopify/historical_data_backfill_syncing.png %})

### Dados sincronizados {#synced-data}

Na sincronização inicial de dados, a Braze importa eventos de pedidos dos últimos 90 dias e perfis de usuário do último ano, cada um contado a partir da data em que você conclui a integração. Quando a Braze importa seus clientes do Shopify, ela atribui o tipo de `external_id` que você escolheu nas configurações.

A tabela a seguir resume os dados incluídos nessa carga inicial.

| Eventos recomendados da Braze | Eventos personalizados do Shopify | Atributos padrão da Braze | Status de inscrição da Braze |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Order placed</li><li>Order cancelled</li><li>Order refunded</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>Email</li><li>First Name</li><li>Last Name</li><li>Phone</li><li>City</li><li>Country</li><li>Total Revenue</li><li>Total Refunds</li><li>Total Orders</li></ul>{:/} | {::nomarkdown}<ul><li>Inscrições de marketing por e-mail associadas a esta loja Shopify</li><li>Inscrições de marketing por SMS associadas a esta loja Shopify</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Dados sincronizados" }