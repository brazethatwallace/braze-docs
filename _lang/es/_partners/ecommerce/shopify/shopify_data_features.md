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

## Eventos de Shopify con seguimiento {#tracked-shopify-events}

La integración de Shopify utiliza [eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) para capturar comportamientos de compra clave. Para ver ejemplos de implementación y estrategias de marketing con estos eventos, consulta [ejemplos de eCommerce]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases).

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

{% tabs %}
{% tab Carga útil de ejemplo %}
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
{% tab Eventos de Shopify %}

{% alert note %}
Braze depende de Shopify para proporcionar las propiedades del evento requeridas (como `cart_id` o `cart_token`) para los eventos de eCommerce. En casos poco frecuentes, problemas temporales con Shopify pueden hacer que estas propiedades no se reciban, lo que puede provocar que los eventos afectados se descarten.
{% endalert %}

{% subtabs global %}
{% subtab Product viewed %}
**Evento**: `ecommerce.product_viewed`<br>
**Tipo**: Evento recomendado<br>
**Se desencadena**: Cuando un cliente ve la página de un producto<br>
**Origen de datos**: SDK or kit de desarrollo de software de Braze<br>
**Ejemplo**: Abandono de navegación

{% raw %}
| Variable | Plantilla de Liquid |
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
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify con seguimiento" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**Evento**: `ecommerce.cart_updated`<br>
**Tipo**: Evento recomendado<br>
**Se desencadena**: Cuando un cliente añade, elimina o actualiza su carrito de compras<br>
**Origen de datos**: SDK or kit de desarrollo de software de Braze<br>
**Ejemplo**: Abandono del carrito de compras

Para los Canvas de carrito abandonado, primero necesitas añadir la etiqueta de Liquid del carrito de compras inicial para obtener el contexto del carrito en tu mensaje.

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

Luego puedes añadir las siguientes etiquetas de Liquid del carrito de compras en tu mensaje.

{% raw %}
| Variable         | Plantilla de Liquid                                   |
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
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify con seguimiento" }
{% endraw %}

{% alert tip %}
Para obtener más información sobre cómo crear un bucle `for` de Liquid para añadir dinámicamente todos los productos a tu correo electrónico, consulta [Personalización de productos de carrito abandonado para correos electrónicos]({{site.baseurl}}/ecommerce_use_cases#abandoned-cart).
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**Evento**: `ecommerce.checkout_started`<br>
**Tipo**: Evento recomendado<br>
**Se desencadena**: Cuando un usuario navega a la página de pago<br>
**Origen de datos**: REST or transferencia de estado representacional API de Braze<br>
**Ejemplo**: Abandono de pago

{% alert important %}
Si un cliente utiliza Shop Pay como opción de pago acelerado, Shopify puede omitir ciertos eventos estándar de pago (como el webhook de inicio de pago de Shopify). Esto significa que Braze puede no recibir los datos necesarios para añadir el alias del token de pago, lo que puede afectar el seguimiento de abandono de pago y la reconciliación del perfil de usuario.
{% endalert %}

Para los Canvas de abandono de pago, primero necesitas utilizar la siguiente etiqueta de Liquid:

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

Luego puedes añadir las siguientes etiquetas de Liquid en tu mensaje para hacer referencia a los productos en tu carrito en el momento del pago.

{% raw %}
| Variable         | Plantilla de Liquid                                   |
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
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify con seguimiento" }
{% endraw %}

{% endsubtab %}
{% subtab Order placed %}
**Evento**: `ecommerce.order_placed`<br>
**Tipo**: Evento recomendado<br>
**Se desencadena**: Cuando un usuario completa con éxito el proceso de pago y realiza un pedido<br>
**Origen de datos**: REST or transferencia de estado representacional API de Braze<br>
**Ejemplo**: Confirmación de pedido, reorientación posterior a la compra, ventas adicionales o ventas cruzadas

{% raw %}
| Variable                | Plantilla de Liquid                                   |
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
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify con seguimiento" }
{% endraw %}

{% alert tip %}
El webhook de pago completado de Shopify no incluye URL de productos ni URL de imágenes. Como resultado, necesitas utilizar la personalización de Liquid de catálogos, como se menciona en [Personalización de productos de carrito abandonado para correos electrónicos]({{site.baseurl}}/ecommerce_use_cases#order-confirmation-and-feedback-survey).
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**Evento**: `shopify_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**Se desencadena**: Cuando el pedido de un usuario se completa y está listo para el envío<br>
**Origen de datos**: REST or transferencia de estado representacional API de Braze<br>
**Ejemplo**: (Transaccional) Actualización de cumplimiento

{% raw %}
| Variable | Plantilla de Liquid |
| --- | --- |
| ID del pedido | `{{event_properties.${order_id}}}` |
| Precio total | `{{event_properties.${total_price}}}` |
| Descuentos totales | `{{event_properties.${total_discounts}}}` |
| Estado de confirmación | `{{event_properties.${confirmed}}}` |
| URL de estado del pedido | `{{event_properties.${order_status_url}}}` |
| Número de pedido | `{{event_properties.${order_number}}}` |
| Marca de tiempo de cancelación | `{{event_properties.${cancelled_at}}}` |
| Marca de tiempo de cierre | `{{event_properties.${closed_at}}}` |
| ID del artículo | `{{event_properties.${line_items}[0].product_id}}` |
| Cantidad del artículo | `{{event_properties.${line_items}[0].quantity}}` |
| SKU del artículo | `{{event_properties.${line_items}[0].sku}}` |
| Título del artículo | `{{event_properties.${line_items}[0].title}}` |
| Proveedor del artículo | `{{event_properties.${line_items}[0].vendor}}` |
| Nombre del artículo | `{{event_properties.${line_items}[0].name}}` |
| Propiedades del artículo | `{{event_properties.${line_items}[0].properties}}` |
| Precio del artículo | `{{event_properties.${line_items}[0].price}}` |
| Título de envío | `{{event_properties.${shipping}[0].title}}` |
| Precio de envío | `{{event_properties.${shipping}[0].price}}` |
| Estado de cumplimiento | `{{event_properties.${fulfillment_status}}}` |
| Estado de envío de cumplimiento | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Estado | `{{event_properties.${fulfillments}[0].status}}` |
| Empresa de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Número de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Números de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| URL de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| URLs de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| Estado de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nombre de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Precio de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| ID de producto de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Cantidad de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Envío de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| SKU de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Título de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Proveedor de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título de variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify con seguimiento" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**Evento**: `shopify_partially_fulfilled_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**Se desencadena**: Cuando parte del pedido de un usuario se completa y está lista para el envío<br>
**Origen de datos**: REST or transferencia de estado representacional API de Braze<br>
**Ejemplo**: (Transaccional) Actualización de cumplimiento

{% raw %}
| Variable | Plantilla de Liquid |
| --- | --- |
| ID del pedido | `{{event_properties.${order_id}}}` |
| Precio total | `{{event_properties.${total_price}}}` |
| Descuentos totales | `{{event_properties.${total_discounts}}}` |
| Estado de confirmación | `{{event_properties.${confirmed}}}` |
| URL de estado del pedido | `{{event_properties.${order_status_url}}}` |
| Número de pedido | `{{event_properties.${order_number}}}` |
| Marca de tiempo de cancelación | `{{event_properties.${cancelled_at}}}` |
| Marca de tiempo de cierre | `{{event_properties.${closed_at}}}` |
| ID del artículo | `{{event_properties.${line_items}[0].product_id}}` |
| Cantidad del artículo | `{{event_properties.${line_items}[0].quantity}}` |
| SKU del artículo | `{{event_properties.${line_items}[0].sku}}` |
| Título del artículo | `{{event_properties.${line_items}[0].title}}` |
| Proveedor del artículo | `{{event_properties.${line_items}[0].vendor}}` |
| Nombre del artículo | `{{event_properties.${line_items}[0].name}}` |
| Propiedades del artículo | `{{event_properties.${line_items}[0].properties}}` |
| Precio del artículo | `{{event_properties.${line_items}[0].price}}` |
| Título de envío | `{{event_properties.${shipping}[0].title}}` |
| Precio de envío | `{{event_properties.${shipping}[0].price}}` |
| Estado de cumplimiento | `{{event_properties.${fulfillment_status}}}` |
| Estado de envío de cumplimiento | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Estado de cumplimiento | `{{event_properties.${fulfillments}[0].status}}` |
| Empresa de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Número de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Números de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| URL de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| URLs de seguimiento de cumplimiento | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| Estado de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Nombre de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Precio de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| ID de producto de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Cantidad de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Envío de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| SKU de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Título de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Proveedor de cumplimiento | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título de variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify con seguimiento" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**Evento**: `shopify_paid_order`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**Se desencadena**: Cuando el pedido de un usuario se marca como pagado en Shopify<br>
**Origen de datos**: REST or transferencia de estado representacional API de Braze<br>
**Ejemplo**: (Transaccional) Confirmación de pago

{% raw %}
| Variable | Plantilla de Liquid |
| --- | --- |
| ID del pedido | `{{event_properties.${order_id}}}` |
| Estado de confirmación | `{{event_properties.${confirmed}}}` |
| URL de estado del pedido | `{{event_properties.${order_status_url}}}` |
| Número de pedido | `{{event_properties.${order_number}}}` |
| Marca de tiempo de cancelación | `{{event_properties.${cancelled_at}}}` |
| Descuentos totales | `{{event_properties.${total_discounts}}}` |
| Precio total | `{{event_properties.${total_price}}}` |
| Etiquetas | `{{event_properties.${tags}}}` |
| Códigos de descuento | `{{event_properties.${discount_codes}}}` |
| ID del artículo | `{{event_properties.${line_items}[0].product_id}}` |
| Cantidad del artículo | `{{event_properties.${line_items}[0].quantity}}` |
| SKU del artículo | `{{event_properties.${line_items}[0].sku}}` |
| Título del artículo | `{{event_properties.${line_items}[0].title}}` |
| Proveedor del artículo | `{{event_properties.${line_items}[0].vendor}}` |
| Propiedades del artículo | `{{event_properties.${line_items}[0].properties}}` |
| Precio del artículo | `{{event_properties.${line_items}[0].price}}` |
| Título de envío | `{{event_properties.${shipping}[0].title}}` |
| Precio de envío | `{{event_properties.${shipping}[0].price}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título de variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify con seguimiento" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**Evento**: `ecommerce.order_cancelled`<br>
**Tipo**: Evento recomendado<br>
**Se desencadena**: Cuando el pedido de un usuario se cancela<br>
**Origen de datos**: REST or transferencia de estado representacional API de Braze<br>
**Ejemplo**: (Transaccional) Confirmación de cancelación de pedido

{% raw %}
| Variable | Plantilla de Liquid |
| --- | --- |
| ID del pedido | `{{event_properties.${order_id}}}` |
| Precio total | `{{event_properties.${total_price}}}` |
| Descuentos totales | `{{event_properties.${total_discounts}}}` |
| Confirmado | `{{event_properties.${confirmed}}}` |
| URL de estado del pedido | `{{event_properties.${order_status_url}}}` |
| Número de pedido | `{{event_properties.${order_number}}}` |
| Marca de tiempo de cancelación | `{{event_properties.${cancelled_at}}}` |
| Etiquetas | `{{event_properties.${tags}}}` |
| Códigos de descuento | `{{event_properties.${discount_codes}}}` |
| Estado de cumplimiento | `{{event_properties.${fulfillment_status}}}` |
| Cumplimientos | `{{event_properties.${fulfillments}}}` |
| ID del artículo | `{{event_properties.${line_items}[0].product_id}}` |
| Cantidad del artículo | `{{event_properties.${line_items}[0].quantity}}` |
| SKU del artículo | `{{event_properties.${line_items}[0].sku}}` |
| Título del artículo | `{{event_properties.${line_items}[0].title}}` |
| Proveedor del artículo | `{{event_properties.${line_items}[0].vendor}}` |
| Nombre del artículo | `{{event_properties.${line_items}[0].name}}` |
| Propiedades del artículo | `{{event_properties.${line_items}[0].properties}}` |
| Estado de cumplimiento | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Título de envío | `{{event_properties.${shipping}[0].title}}` |
| Precio de envío | `{{event_properties.${shipping}[0].price}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título de variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify con seguimiento" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**Evento**: `ecommerce.order_refunded`<br>
**Tipo**: Evento recomendado<br>
**Se desencadena**: Cuando el pedido de un usuario se reembolsa<br>
**Origen de datos**: REST or transferencia de estado representacional API de Braze<br>
**Ejemplo**: (Transaccional) Confirmación de reembolso

{% raw %}
| Variable | Plantilla de Liquid |
| --- | --- |
| ID del pedido | `{{event_properties.${order_id}}}` |
| Nota del pedido | `{event_properties.${note}}}` |
| ID del artículo | `{{event_properties.${line_items}[0].product_id}}` |
| Cantidad del artículo | `{{event_properties.${line_items}[0].quantity}}` |
| SKU del artículo | `{{event_properties.${line_items}[0].sku}}` |
| Título del artículo | `{{event_properties.${line_items}[0].title}}` |
| Proveedor del artículo | `{{event_properties.${line_items}[0].vendor}}` |
| Nombre del artículo | `{{event_properties.${line_items}[0].name}}` |
| Propiedades del artículo | `{{event_properties.${line_items}[0].properties}}` |
| Precio del artículo | `{{event_properties.${line_items}[0].price}}` |
| ID de variante | `{{event_properties.${line_items}[0].variant_id}}` |
| Título de variante | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify con seguimiento" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**Evento**: `shopify_account_login`<br>
**Tipo**: [Evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**Se desencadena**: Cuando un usuario inicia sesión en su cuenta<br>
**Origen de datos**: REST or transferencia de estado representacional API de Braze<br>
**Ejemplo**: Serie de bienvenida

{% raw %}
| Variable | Plantilla de Liquid |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Eventos de Shopify con seguimiento" }
{% endraw %}

{% alert note %}
La integración de Shopify actualmente no admite el llenado del [evento de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) de Braze. Como resultado, los filtros de compra, las etiquetas de Liquid, los desencadenadores basados en acciones y los análisis deben usar el evento `ecommerce.order_placed`.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Atributos personalizados de Shopify compatibles {#supported-shopify-custom-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

{% tabs local %}
{% tab Carga útil de ejemplo %}
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
{% tab Atributos personalizados de Shopify %}
| Nombre del atributo | Descripción |
| --- | --- |
| `shopify_total_spent` | La cantidad total de dinero que el cliente ha gastado en todo su historial de pedidos. |
| `shopify_order_count` | El número de pedidos asociados a este cliente. Los pedidos de prueba y archivados no se contabilizan. |
| `shopify_last_order_id` | El ID del último pedido del cliente. |
| `shopify_last_order_name` | El nombre del último pedido del cliente. Está directamente relacionado con el campo `name` en el recurso de pedido. |
| `shopify_zipcode` | El código postal del cliente de su dirección predeterminada. |
| `shopify_province` | La provincia del cliente de su dirección predeterminada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atributos personalizados de Shopify compatibles" }

{% alert important %}
Un problema conocido con la versión actual de la API de Shopify impide que el atributo de usuario `shopify_last_order_name` se complete correctamente. El impacto en los usuarios es el siguiente:<br><br>

- **Usuarios existentes:** Para cualquier usuario que ya tenga un valor para `shopify_last_order_name`, ese valor persiste pero no se actualiza con los pedidos posteriores.
- **Nuevos usuarios:** Para cualquier nuevo usuario, el campo no se completa y permanece vacío o nulo.

Esta página se actualizará después de que Shopify resuelva este problema.
{% endalert %}

### Personalización con Liquid {#liquid-personalization}

Para agregar personalización con Liquid para tus atributos personalizados de Shopify, selecciona **+ Personalización**. Luego selecciona **Atributos personalizados** como tu tipo de personalización.

![La sección "Agregar personalización" con el menú desplegable "Atributo" abierto.]({% image_buster /assets/img/shopify/add_personalization_2.png %}){: style="max-width:40%;"}

Después de seleccionar tu atributo personalizado, ingresa un valor predeterminado y copia el fragmento de Liquid en tu mensaje.

![Pegando un fragmento de Liquid en un mensaje.]({% image_buster /assets/img/shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## Atributos estándar de Shopify compatibles {#supported-shopify-standard-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

- Correo electrónico
- Nombre
- Apellido
- Teléfono
- Ciudad
- País

{% alert note %}
Braze solo actualizará los atributos personalizados de Shopify compatibles y los atributos estándar de Braze si hay una diferencia en los datos respecto al perfil de usuario existente. Por ejemplo, si los datos entrantes de Shopify contienen un nombre de Bob y Bob ya existe como nombre en el perfil de usuario de Braze, Braze no activará una actualización y no se te cobrará un punto de datos.
{% endalert %}

## Recopilación de datos del SDK or kit de desarrollo de software {#sdk-data-collection}

Para obtener más información sobre los datos que recopilan los SDK or kit de desarrollo de software de Braze, consulta [Recopilación de datos del SDK or kit de desarrollo de software]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection).

## Reabastecimiento histórico {#historical-backfill}

> Los datos históricos de Shopify se importan antes de que conectes Braze: eventos de pedidos de los últimos 90 días y datos de clientes del último año. Ambos periodos se cuentan hacia atrás desde la fecha en que completas tu integración.

A través de la [configuración de la integración estándar de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) o la [configuración de la integración personalizada de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration), puedes activar el reabastecimiento histórico para segmentar a clientes anteriores. Esto importa tus pedidos de Shopify (eventos relacionados con pedidos) de los últimos 90 días y perfiles de usuario del último año. Ambos periodos se cuentan hacia atrás desde la fecha en que completas tu integración.

Cuando Braze importa tus clientes de Shopify, asigna el tipo de `external_id` que elegiste en tu configuración.

{% alert note %}
Si ya eres cliente de Braze con Campaigns o Canvas activos, revisa cómo los clientes importados y los eventos de pedidos afectan tus Segments y recorridos antes de habilitar el reabastecimiento histórico.
{% endalert %}

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

### Configurar el reabastecimiento histórico de Shopify {#setting-up-shopify-historical-backfill}

1. Activa el reabastecimiento histórico en el paso **Track Shopify data**.

![El paso "Track Shopify data" de la integración de Shopify mostrando el reabastecimiento histórico seleccionado.]({% image_buster /assets/img/shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. Después de completar la configuración de tu integración, Braze comenzará la sincronización inicial de datos. Puedes monitorear el progreso en la pestaña **Shopify Data** de la configuración de tu integración.

![La página de configuración de la integración de Shopify con un indicador de carga que muestra que los eventos se están sincronizando activamente.]({% image_buster /assets/img/shopify/historical_data_backfill_syncing.png %})

### Datos sincronizados {#synced-data}

Para la sincronización inicial de datos, Braze importa eventos de pedidos de los últimos 90 días y perfiles de usuario del último año, cada uno contado hacia atrás desde la fecha en que completas tu integración. Cuando Braze importa tus clientes de Shopify, asigna el tipo de `external_id` que elegiste en tu configuración.

La siguiente tabla resume los datos incluidos en esa carga inicial.

| Eventos recomendados de Braze | Eventos personalizados de Shopify | Atributos estándar de Braze | Estados de suscripción de Braze |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Order placed</li><li>Order cancelled</li><li>Order refunded</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>Email</li><li>First Name</li><li>Last Name</li><li>Phone</li><li>City</li><li>Country</li><li>Total Revenue</li><li>Total Refunds</li><li>Total Orders</li></ul>{:/} | {::nomarkdown}<ul><li>Suscripciones de marketing por correo electrónico asociadas con esta tienda de Shopify</li><li>Suscripciones de marketing por servicio de mensajes cortos asociadas con esta tienda de Shopify</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Datos sincronizados" }