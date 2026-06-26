---
nav_title: Características de los datos de Shopify
article_title: Características de los datos de Shopify
description: "Este artículo de referencia cubre las características de los datos de Shopify."
page_type: partner
search_tag: Partner
alias: /shopify_data_features/
page_order: 4
---

# Características de los datos de Shopify {#shopify-data-features}

> Este artículo ofrece un resumen de nuestras características de Shopify, incluyendo qué datos de Shopify se rastrean, ejemplos de cargas útiles, backfill histórico y sincronización de productos.

## Eventos de Shopify rastreados {#tracked-shopify-events}

La integración con Shopify utiliza [eventos recomendados de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/) para captar comportamientos clave de compra. Para ver ejemplos de implementación y estrategias de marketing con estos eventos, consulta los [casos de uso de comercio electrónico]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/).

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

{% tabs %}
{% tab Example Payload %}
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
{% tab Shopify events %}
{% subtabs global %}
{% subtab Product viewed %}
**Evento**: `ecommerce.product_viewed`<br>
**Tipo**: Evento recomendado<br>
**Se desencadena**: Cuando un cliente ve una página de producto<br>
**Origen de datos**: SDK de Braze<br>
**Caso de uso**: Abandono de navegación

{% raw %}
| Variable | Plantilla Liquid |
| --- | --- |
|------------------|-----------------------------------------------------|
| `product_id`       | `{{event_properties.${product_id}}}`                |
| `product_name `    | `{{event_properties.${product_name}}}`              |
| `variant_id`       | `{{event_properties.${variant_id}}}`                |
| `image_url `       | `{{event_properties.${image_url}}}`                 |
| `product_url`      | `<your-store.myshopify.com>{{event_properties.${product_url}}}` <br><br>Añade el dominio de tu sitio Shopify antes de la URL. |
| `price`            | `{{event_properties.${price}}}`                     |
| `currency`         | `{{event_properties.${currency}}}`                  |
| `source`           | `{{event_properties.${source}}}`                    |
| `sku`              | `{{event_properties.${metadata}[0].sku}}`          |
| `type`             | `event_properties.${type}`          |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify rastreados" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**Evento**: `ecommerce.cart_updated`<br>
**Tipo**: Evento recomendado<br>
**Se desencadena**: Cuando un cliente añade, elimina o actualiza su carrito de compras<br>
**Origen de datos**: SDK de Braze<br>
**Caso de uso**: Abandono del carrito de compras

Para los Canvas de carrito abandonado, primero tienes que añadir la etiqueta Liquid inicial del carrito de compras para obtener el contexto del carrito en tu mensaje.

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

A continuación, puedes añadir las siguientes etiquetas Liquid del carrito de compras en tu mensaje.

{% raw %}
| Variable         | Plantilla Liquid                                   |
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
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify rastreados" }
{% endraw %}

{% alert tip %}
Para más información sobre cómo crear un bucle Liquid `for` para añadir dinámicamente todos los productos a tu correo electrónico, consulta [Personalización de productos de carritos abandonados para correos electrónicos]({{site.baseurl}}/ecommerce_use_cases/#abandoned-cart).
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**Evento**: `ecommerce.checkout_started`<br>
**Tipo**: Evento recomendado<br>
**Se desencadena**: Cuando un usuario navega a la página de pago<br>
**Origen de datos**: REST API de Braze<br>
**Caso de uso**: Abandono del proceso de pago

{% alert important %}
Si un cliente utiliza Shop Pay como opción de pago acelerado, Shopify puede omitir ciertos eventos estándar del proceso de pago (como el webhook de inicio de pago de Shopify). Esto significa que Braze puede no recibir los datos necesarios para añadir el alias del token de pago, lo que puede afectar al seguimiento del abandono del proceso de pago y a la reconciliación de perfiles de usuario.
{% endalert %}

Para los Canvas de abandono del proceso de pago, primero tienes que utilizar la siguiente etiqueta Liquid:

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

A continuación, puedes añadir las siguientes etiquetas Liquid en tu mensaje para hacer referencia a los productos de tu carrito en el momento del pago.

{% raw %}
| Variable         | Plantilla Liquid                                   |
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
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify rastreados" }
{% endraw %}

{% endsubtab %}
{% subtab Order placed %}
**Evento**: `ecommerce.order_placed`<br>
**Tipo**: Evento recomendado<br>
**Se desencadena**: Cuando un usuario completa con éxito el proceso de pago y realiza un pedido<br>
**Origen de datos**: REST API de Braze<br>
**Caso de uso**: Confirmación de pedido, reorientación posterior a la compra, upsells o ventas cruzadas

{% raw %}
| Variable                | Plantilla Liquid                                   |
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
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify rastreados" }
{% endraw %}

{% alert tip %}
El webhook de pago completado de Shopify no contiene URL de productos ni URL de imágenes. Como resultado, tienes que utilizar la personalización de Catálogos con Liquid, como se menciona en [Personalización de productos de carritos abandonados para correos electrónicos]({{site.baseurl}}/ecommerce_use_cases/#order-confirmation-and-feedback-survey).
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**Evento**: `shopify_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)<br>
**Se desencadena**: Cuando el pedido de un usuario se ha completado y está listo para su envío<br>
**Origen de datos**: REST API de Braze<br>
**Caso de uso**: (Transaccional) Actualización de cumplimiento

{% raw %}
| Variable | Plantilla Liquid |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify rastreados" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**Evento**: `shopify_partially_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)<br>
**Se desencadena**: Cuando parte del pedido de un usuario se ha completado y está listo para su envío<br>
**Origen de datos**: REST API de Braze<br>
**Caso de uso**: (Transaccional) Actualización de cumplimiento

{% raw %}
| Variable | Plantilla Liquid |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify rastreados" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**Evento**: `shopify_paid_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)<br>
**Se desencadena**: Cuando el pedido de un usuario se marca como pagado en Shopify<br>
**Origen de datos**: REST API de Braze<br>
**Caso de uso**: (Transaccional) Confirmación de pago

{% raw %}
| Variable | Plantilla Liquid |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify rastreados" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**Evento**: `ecommerce.order_cancelled`<br>
**Tipo**: Evento recomendado<br>
**Se desencadena**: Cuando se cancela el pedido de un usuario<br>
**Origen de datos**: REST API de Braze<br>
**Caso de uso**: (Transaccional) Confirmación de cancelación de pedido

{% raw %}
| Variable | Plantilla Liquid |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillments | `{{event_properties.${fulfillments}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Fulfillment Status | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify rastreados" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**Evento**: `ecommerce.order_refunded`<br>
**Tipo**: Evento recomendado<br>
**Se desencadena**: Cuando se reembolsa el pedido de un usuario<br>
**Origen de datos**: REST API de Braze<br>
**Caso de uso**: (Transaccional) Confirmación de reembolso

{% raw %}
| Variable | Plantilla Liquid |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Order Note | `{event_properties.${note}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify rastreados" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**Evento**: `shopify_account_login`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)<br>
**Se desencadena**: Cuando un usuario inicia sesión en su cuenta<br>
**Origen de datos**: REST API de Braze<br>
**Caso de uso**: Series de bienvenida

{% raw %}
| Variable | Plantilla Liquid |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify rastreados" }
{% endraw %}

{% alert note %}
Actualmente, la integración de Shopify no permite rellenar el [evento de compra]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-events) de Braze. En consecuencia, los filtros de compra, las etiquetas Liquid, los desencadenantes basados en acciones y los análisis deben utilizar el evento `ecommerce.order_placed`.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Atributos personalizados de Shopify compatibles {#supported-shopify-custom-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

{% tabs local %}
{% tab Example Payload %}
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
{% tab Shopify Custom Attributes %}
| Nombre del atributo | Descripción |
| --- | --- |
| `shopify_total_spent` | La cantidad total de dinero que el cliente ha gastado en todo su historial de pedidos. |
| `shopify_order_count` | El número de pedidos asociados a este cliente. No se cuentan los pedidos de prueba ni los archivados. |
| `shopify_last_order_id` | El ID del último pedido del cliente. |
| `shopify_last_order_name` | El nombre del último pedido del cliente. Está directamente relacionado con el campo `name` del recurso de pedido. |
| `shopify_zipcode` | El código postal del cliente a partir de su dirección predeterminada. |
| `shopify_province` | La provincia del cliente a partir de su dirección predeterminada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados de Shopify compatibles" }

{% alert important %}
Un problema conocido con la versión actual de la API de Shopify impide que el atributo de usuario `shopify_last_order_name` se rellene correctamente. El impacto sobre los usuarios es el siguiente:<br><br>

- **Usuarios existentes:** Para cualquier usuario que ya tenga un valor para `shopify_last_order_name`, ese valor persiste pero no se actualiza con los pedidos posteriores.
- **Nuevos usuarios:** Para los nuevos usuarios, el campo no se rellena y permanece vacío o nulo.

Esta página se actualizará cuando Shopify resuelva este problema.
{% endalert %}

### Personalización con Liquid {#liquid-personalization}

Para añadir personalización Liquid a tus atributos personalizados de Shopify, selecciona **+ Personalization**. A continuación, selecciona **Custom Attributes** como tipo de personalización.

![La sección "Add Personalization" con el desplegable "Attribute" expandido.]({% image_buster /assets/img/shopify/add_personalization_2.png %}){: style="max-width:40%;"}

Tras seleccionar tu atributo personalizado, introduce un valor predeterminado y copia el fragmento de código Liquid en tu mensaje.

![Pegar un fragmento de código Liquid en un mensaje.]({% image_buster /assets/img/shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## Atributos estándar de Shopify compatibles {#supported-shopify-standard-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

- Email
- First Name
- Last Name
- Phone
- City
- Country

{% alert note %}
Braze solo actualizará los atributos personalizados de Shopify y los atributos estándar de Braze compatibles si hay una diferencia en los datos respecto al perfil de usuario existente. Por ejemplo, si los datos entrantes de Shopify contienen un nombre "Bob" y "Bob" ya existe como nombre en el perfil de usuario de Braze, Braze no desencadenará una actualización y no se te cobrará un punto de datos.
{% endalert %}

## Recopilación de datos del SDK {#sdk-data-collection}

Para más información sobre qué datos recopilan los SDK de Braze, consulta [Recopilación de datos del SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/).

## Backfill histórico {#historical-backfill}

> Los datos históricos de Shopify se importan desde antes de que conectes Braze: eventos de pedidos de los últimos 90 días y datos de clientes del último año. Ambos plazos se cuentan hacia atrás desde la fecha en que completas tu integración.

A través de la [configuración de la integración estándar de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/) o la [configuración de la integración personalizada de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/), puedes activar el backfill histórico para dirigirte a clientes anteriores. Esto importa tus pedidos de Shopify (eventos relacionados con pedidos) de los últimos 90 días y perfiles de usuario del último año. Ambos plazos se cuentan hacia atrás desde la fecha en que completas tu integración.

Cuando Braze importa tus clientes de Shopify, les asigna el tipo de `external_id` que hayas elegido en tus ajustes de configuración.

{% alert note %}
Si ya eres cliente de Braze con Campaigns o Canvas activos, revisa cómo los clientes importados y los eventos de pedidos afectan a tus segmentos y recorridos antes de habilitar el backfill histórico.
{% endalert %}

{% multi_lang_include shopify.md section='Custom external ID historical backfill' %}

### Configuración del backfill histórico de Shopify {#setting-up-shopify-historical-backfill}

1. Activa el backfill histórico en el paso **Track Shopify data**.

![El paso "Track Shopify data" de la integración de Shopify muestra el backfill histórico seleccionado.]({% image_buster /assets/img/shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. Después de completar la configuración de tu integración, Braze comenzará la sincronización inicial de datos. Puedes supervisar el progreso en la pestaña **Shopify Data** de tu configuración de integración.

![La página de configuración de la integración de Shopify con un indicador que muestra que los eventos se están sincronizando activamente.]({% image_buster /assets/img/shopify/historical_data_backfill_syncing.png %})

### Datos sincronizados {#synced-data}

Para la sincronización inicial de datos, Braze importa eventos de pedidos de los últimos 90 días y perfiles de usuario del último año, cada uno contado hacia atrás desde la fecha en que completas tu integración. Cuando Braze importa tus clientes de Shopify, les asigna el tipo de `external_id` que hayas elegido en tus ajustes de configuración.

La siguiente tabla resume los datos incluidos en esa carga inicial.

| Eventos recomendados de Braze | Eventos personalizados de Shopify | Atributos estándar de Braze | Estados de suscripción de Braze |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Order placed</li><li>Order cancelled</li><li>Order refunded</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>Email</li><li>First Name</li><li>Last Name</li><li>Phone</li><li>City</li><li>Country</li><li>Total Revenue</li><li>Total Refunds</li><li>Total Orders</li></ul>{:/} | {::nomarkdown}<ul><li>Suscripciones de marketing por correo electrónico asociadas a esta tienda Shopify</li><li>Suscripciones de marketing por SMS asociadas a esta tienda Shopify</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Datos sincronizados" }