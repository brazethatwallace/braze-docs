---
nav_title: Eventos recomendados para el comercio electrónico
article_title: Eventos recomendados de comercio electrónico
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "Este artículo de referencia describe los eventos y propiedades recomendados para el comercio electrónico, su uso, segmentación, dónde ver los análisis relevantes y mucho más."
---

# Eventos recomendados para el comercio electrónico {#ecommerce-recommended-events}

> Esta página incluye eventos y propiedades recomendados para el comercio electrónico. Estos eventos se crean para capturar comportamientos de compra clave que los especialistas en marketing necesitan para desencadenar mensajería eficaz, como los dirigidos al abandono del carrito de compras.

{% alert important %}
Los eventos recomendados para el comercio electrónico se encuentran actualmente en fase de acceso anticipado. Si estás interesado en participar en este acceso anticipado, ponte en contacto con tu administrador del éxito del cliente de Braze. <br><br>Si utilizas el nuevo [conector de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), estos eventos recomendados estarán disponibles automáticamente a través de la integración.
{% endalert %}

Braze reconoce que la planificación de datos lleva tiempo. Animamos a nuestros clientes a que familiaricen a sus equipos de desarrollo y comiencen a enviar estos eventos ahora mismo. Aunque es posible que algunas características no estén disponibles de inmediato con los eventos recomendados para el comercio electrónico, puedes esperar la introducción de nuevos productos a lo largo de 2025 que mejorarán tus capacidades de comercio electrónico.

## Tipos de eventos recomendados para el comercio electrónico {#types-of-ecommerce-recommended-events}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Cualquier moneda que no sea USD se mostrará en Braze en USD según el tipo de cambio de la fecha en que se reportó. Para evitar la conversión de moneda, codifica la moneda como USD.

{% tabs %}
{% tab ecommerce.product_viewed %}

Puedes usar el evento de producto visto para desencadenar cuando un cliente ve una página de detalle de producto.

#### Propiedades {#properties}

| Nombre de la propiedad | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `product_id` | Sí | String | Un identificador único para el producto que fue visto. <br> Para clientes que no usan Shopify, este será el valor que establezcas para los ID de elementos del catálogo, como los SKU. |
| `product_name` | Sí | String | El nombre del producto que fue visto. |
| `variant_id` | Sí | String | Un identificador único para la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | String | URL de la imagen del producto. |
| `product_url` | No | String | URL de la página del producto para más detalles. |
| `price` | Sí | Float | El precio unitario de la variante del producto en el momento de la visualización. |
| `currency` | Sí | String | La moneda en la que se lista el precio del producto (como "USD" o "EUR") en [formato ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `source` | Sí | String | Fuente de la que se deriva el evento. (Para Shopify, es storefront). |
| `type` | No | Object | Funciona con [notificaciones de vuelta en stock]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/) y [notificaciones de bajada de precio]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/). |
| `metadata` | No | Object | |
| `sku` | No | String | (Solo Shopify) SKU de Shopify. Se puede configurar como el campo de ID del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Objetos de ejemplo {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

En versiones más recientes del SDK, llama a `logEcommerceEvent()`:

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

En versiones anteriores del SDK, llama a `logCustomEvent()`:

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

Puedes usar el desencadenador **Realizar evento de carrito actualizado** para rastrear cuándo se agregan, eliminan o actualizan productos en el carrito. Este evento verifica la siguiente información antes de desencadenarse:

- La hora del evento es mayor que la hora `updated_at` del carrito específico del usuario.
- El carrito no ha avanzado al proceso de pago.
- El array `products` no está vacío.

#### Objeto de mapeado de carritos {#carts-mapping-object}

El evento `ecommerce.cart_updated` tiene un objeto de mapeado de carritos. Este objeto se crea para el perfil de usuario y contiene un mapeado de carritos con todos los productos en el carrito del comprador. Puedes acceder a los productos en su carrito de compras a través de la etiqueta de Liquid:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

Si un carrito no se actualiza y no avanza a un evento de pedido realizado en 30 días, Braze elimina el carrito y los productos asociados.

{% alert note %}
Los productos por carrito no están limitados en Braze. Sin embargo, el límite de Shopify es 500.
{% endalert %}

#### Comportamiento del carrito al fusionar perfiles de usuario {#cart-behavior-when-merging-user-profiles}

Si hay dos carritos, ambos se agregan al usuario fusionado. Se vuelve a encolar el Canvas si es el mismo carrito o uno diferente para enviar un mensaje con la información más reciente del carrito. El evento `ecommerce.cart_updated` contendrá el último ID de carrito y los últimos productos en el carrito.

#### Propiedades {#properties}

| Nombre de la propiedad | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `cart_id` | Sí | String | Si no estás usando una plataforma de terceros que proporcione un `cart_id`, puedes usar el [ID de sesión de Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/). |
| `total_value` | Sí | Float | Valor monetario total del carrito. |
| `subtotal_value` | No | Float | Valor del subtotal del carrito después de descuentos y antes de impuestos y envío. |
| `tax` | No | Float | Impuesto total aplicado al carrito. |
| `shipping` | No | Float | Costo total de envío del carrito. |
| `currency` | Sí | String | La moneda en la que se lista el precio del producto (como "USD" o "EUR") en [formato ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `products` | Sí | Array |  |
| `product_id` | Sí | String | Un identificador único para el producto que fue visto. <br> Este valor puede ser el ID del producto o el SKU. |
| `product_name` | Sí | String | El nombre del producto que fue visto. |
| `variant_id` | Sí | String | Un identificador único para la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | String | URL de la imagen del producto. |
| `product_url` | No | String | URL de la página del producto para más detalles. |
| `quantity` | Sí | Integer | Número de unidades del producto en el carrito. |
| `price` | Sí | Float | El precio unitario de la variante del producto en el momento de la visualización. |
| `metadata` | No | Object | Campo de metadatos adicional sobre el producto que el cliente quiere agregar para sus casos de uso. Para Shopify, agregaremos el SKU. <br> Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50 kb. |
| `sku` | No | String | (Solo Shopify) SKU de Shopify. Se puede configurar como el campo de ID del catálogo. |
| `source` | Sí | String | Fuente de la que se deriva el evento. (Para Shopify, es storefront). |
| `metadata` | No | Object | Campo de metadatos adicional sobre el producto que el cliente quiere agregar para sus casos de uso. Para Shopify, agregaremos el SKU. <br> Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50 kb. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Objetos de ejemplo {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

En versiones más recientes del SDK, llama a `logEcommerceEvent()`:

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

En versiones anteriores del SDK, llama a `logCustomEvent()`:

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

Puedes usar el evento de pago iniciado para reorientar a los clientes que han comenzado el proceso de pago pero no han realizado un pedido.

De forma similar al evento `ecommerce.cart_updated`, este evento te permite aprovechar la etiqueta de Liquid del carrito de compras para acceder a todos los productos dentro del carrito en mensajes de pago abandonado:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### Propiedades {#properties}

| Nombre de la propiedad | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `checkout_id` | Sí | String | Identificador único para el pago. |
| `cart_id` | No | String | Si no estás usando una plataforma de terceros que proporcione un `cart_id`, puedes usar el [ID de sesión de Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/). |
| `total_value` | Sí | Float | Valor monetario total del carrito. |
| `subtotal_value` | No | Float | Valor del subtotal del carrito después de descuentos y antes de impuestos y envío. |
| `tax` | No | Float | Impuesto total aplicado al carrito. |
| `shipping` | No | Float | Costo total de envío del carrito. |
| `currency` | Sí | String | Moneda en la que se valora el carrito. |
| `products` | Sí | Array of objects |  |
| `product_id` | Sí | String | Un identificador único para el producto que fue visto. Por ejemplo, este valor podría ser el ID del producto o el SKU. |
| `product_name` | Sí | String | El nombre del producto que fue visto.  |
| `variant_id` | Sí | String | Un identificador único para la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | String | URL de la imagen del producto. |
| `product_url` | No | String | URL de la página del producto para más detalles. |
| `quantity` | Sí | Integer | Número de unidades del producto en el carrito. |
| `price` | Sí | Float | El precio unitario de la variante del producto en el momento de la visualización. |
| `metadata` | No | Object | Campo de metadatos adicional sobre el producto que el cliente quiere agregar para sus casos de uso. Para Shopify, agregaremos el SKU. <br> Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50 kb. |
| `sku` | No | String | (Solo Shopify) SKU de Shopify. Se puede configurar como el campo de ID del catálogo. |
| `source` | Sí | String | Fuente de la que se deriva el evento. (Para Shopify, es storefront). |
| `metadata` | No | Object |  |
| `checkout_url` | No | String | URL de la página de pago. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Objetos de ejemplo {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

En versiones más recientes del SDK, llama a `logEcommerceEvent()`:

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

En versiones anteriores del SDK, llama a `logCustomEvent()`:

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

Puedes usar el evento de pedido realizado para desencadenar cuando un cliente completa exitosamente el proceso de pago y realiza un pedido.

#### Propiedades {#properties}

| Nombre de la propiedad | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `order_id` | Sí | String | Identificador único para el pedido realizado. |
| `cart_id` | No | String | Si no estás usando una plataforma de terceros que proporcione un `cart_id`, puedes usar el [ID de sesión de Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/). |
| `total_value` | Sí | Float | Valor monetario total del carrito. |
| `subtotal_value` | No | Float | Valor del subtotal del pedido después de descuentos y antes de impuestos y envío. |
| `tax` | No | Float | Impuesto total aplicado al pedido. |
| `shipping` | No | Float | Costo total de envío del pedido. |
| `currency` | Sí | String | Moneda en la que se valora el carrito. |
| `total_discounts` | No | Float | Monto total de descuentos aplicados al pedido. |
| `discounts`| No | Array of objects | Lista detallada de descuentos aplicados al pedido. |
| `products` | Sí | Array of objects |  |
| `product_id` | Sí | String | Un identificador único para el producto que fue visto. Este valor puede ser el ID del producto o el SKU. |
| `product_name` | Sí | String | El nombre del producto que fue visto. |
| `variant_id` | Sí | String | Un identificador único para la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | String | URL de la imagen del producto. |
| `product_url` | No | String | URL de la página del producto para más detalles. |
| `quantity` | Sí | Integer | Número de unidades del producto en el carrito. |
| `price` | Sí | Float | El precio unitario de la variante del producto en el momento de la visualización. |
| `metadata` | No | Object | Campo de metadatos adicional sobre el producto que el cliente quiere agregar para sus casos de uso. Para Shopify, agregaremos el SKU. <br> Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50 kb. |
| `sku` | No | String | (Solo Shopify) SKU de Shopify. Se puede configurar como el campo de ID del catálogo. |
| `source` | Sí | String | Fuente de la que se deriva el evento. (Para Shopify, es storefront). |
| `order_status_url` | No | String | URL para ver el estado del pedido. |
| `order_number` | No | String | (Solo Shopify) Número de pedido único para el pedido realizado. |
| `tags` | No | Array | (Solo Shopify) Etiquetas del pedido. |
| `referring_site` | No | String | (Solo Shopify) El sitio del que se originó el pedido (como Meta). |
| `payment_gateway_names` | No | Array | (Solo Shopify) Fuente del sistema de pago (como punto de venta o móvil). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Objetos de ejemplo {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

En versiones más recientes del SDK, llama a `logEcommerceEvent()`:

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

En versiones anteriores del SDK, llama a `logCustomEvent()`:

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

Puedes usar el evento de pedido reembolsado para desencadenar cuando un pedido es parcial o totalmente reembolsado.

#### Propiedades {#properties}

| Nombre de la propiedad       | Obligatoria | Tipo de datos | Descripción   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | Sí      | String    | Identificador único para el pedido realizado.        |
| `total_value`         | Sí      | Float     | Valor monetario total del carrito.    |
| `currency`            | Sí      | String    | Moneda en la que se valora el carrito.    |
| `total_discounts`     | No       | Float     | Monto total de descuentos aplicados al pedido.   |
| `discounts`           | No       | Array of objects     | Lista detallada de descuentos aplicados al pedido. |
| `products`            | Sí      | Array of objects     |  |
| `product_id`       | Sí      | String    | Un identificador único para el producto que fue visto. Este valor puede ser el ID del producto, SKU o similar. <br>Si se emite un reembolso parcial y no hay un `product_id` asignado al reembolso (por ejemplo, un reembolso a nivel de pedido), proporciona un `product_id` generalizado.             |
| `product_name`     | Sí      | String    | El nombre del producto que fue visto.                                                                      |
| `variant_id`       | Sí      | String    | Un identificador único para la variante del producto (como `shirt_medium_blue`).                                         |
| `image_url`        | No       | String    | URL de la imagen del producto.     |
| `product_url`      | No       | String    | URL de la página del producto para más detalles.  |
| `quantity`         | Sí      | Integer   | Número de unidades del producto en el carrito.   |
| `price`            | Sí      | Float     | El precio unitario de la variante del producto en el momento de la visualización.  |
| `metadata`         | No       | Object    | Campo de metadatos adicional sobre el producto que el cliente quiere agregar para sus casos de uso. Para Shopify, agregaremos el SKU. Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50 kb. |
| `sku`            | No       | String    | (Solo Shopify) SKU de Shopify. Se puede configurar como el campo de ID del catálogo.  |
| `source`              | Sí      | String    | Fuente de la que se deriva el evento. (Para Shopify, es storefront).    |
| `metadata`            | No       | Object    |                |
| `order_status_url`  | No       | String    | URL para ver el estado del pedido.     |
| `order_note`       | No       | String    | (Solo Shopify) Nota adjunta al pedido por el comerciante.    |
| `order_number`     | No       | String    | (Solo Shopify) Número de pedido único para el pedido realizado.   |
| `tags`             | No       | Array     | (Solo Shopify) Etiquetas del pedido.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Objetos de ejemplo {#example-objects}

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

Puedes usar el evento de pedido cancelado para desencadenar cuando un cliente cancela un pedido.

#### Propiedades {#properties}

| Nombre de la propiedad      | Obligatoria | Tipo de datos | Descripción       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | Sí      | String    | Identificador único para el pedido realizado.              |
| `cancel_reason`       | Sí      | String    | Razón por la que se canceló el pedido.           |
| `total_value`         | Sí      | Float     | Valor monetario total del carrito.         |
| `subtotal_value`      | No       | Float     | Valor del subtotal del pedido después de descuentos y antes de impuestos y envío. |
| `tax`                 | No       | Float     | Impuesto total aplicado al pedido. |
| `shipping`            | No       | Float     | Costo total de envío del pedido. |
| `currency`            | Sí      | String    | Moneda en la que se valora el carrito.           |
| `total_discounts`     | No       | Float     | Monto total de descuentos aplicados al pedido.     |
| `discounts`           | No       | Array of objects     | Lista detallada de descuentos aplicados al pedido.             |
| `products`            | Sí      | Array of objects     |         |
| `product_id`          | Sí      | String    | Un identificador único para el producto que fue visto. Este valor puede ser el ID del producto, SKU o similar.             |
| `product_name`        | Sí      | String    | El nombre del producto que fue visto.          |
| `variant_id`          | Sí      | String    | Un identificador único para la variante del producto (como `shirt_medium_blue`).        |
| `image_url`           | No       | String    | URL de la imagen del producto.           |
| `product_url`         | No       | String    | URL de la página del producto para más detalles.                                                                     |
| `quantity`            | Sí      | Integer   | Número de unidades del producto en el carrito.        |
| `price`               | Sí      | Float     | El precio unitario de la variante del producto en el momento de la visualización.     |
| `metadata`            | No       | Object    | Campo de metadatos adicional sobre el producto que el cliente quiere agregar para sus casos de uso. Para Shopify, agregaremos el SKU. Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50 kb. |
| `sku`                 | No       | String    | (Solo Shopify) SKU de Shopify. Se puede configurar como el campo de ID del catálogo.        |
| `source`              | Sí      | String    | Fuente de la que se deriva el evento. (Para Shopify, es storefront).    |
| `metadata`            | No       | Object    |       |
| `order_status_url`    | No       | String    | URL para ver el estado del pedido.                                                                          |
| `order_number`        | No       | String    | (Solo Shopify) Número de pedido único para el pedido realizado.  |
| `tags`                | No       | Array     | (Solo Shopify) Etiquetas del pedido.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Objetos de ejemplo {#example-objects}

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

## Plantillas de Canvas de comercio electrónico {#ecommerce-canvas-templates}

Braze ha creado plantillas de Canvas prediseñadas que funcionan con los eventos recomendados de comercio electrónico, como dirigirse a clientes que iniciaron el proceso de pago pero se fueron antes de realizar su pedido. Puedes usar estos eventos para tomar decisiones informadas que mejoren el recorrido de tus usuarios personalizando la mensajería y dirigiéndote a audiencias específicas.

Consulta nuestros [casos de uso de comercio electrónico]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/) dedicados para conocer más formas de usar estos eventos con plantillas de Canvas.

## Campos calculados del usuario {#user-calculated-fields}

Usamos cálculos estandarizados de campos de usuario para los siguientes campos:

- **Ingresos totales** = suma del valor total de pedidos realizados - suma del valor total de pedidos reembolsados
- **Conteo total de pedidos** = conteo de eventos distintos de pedido realizado - conteo de cancelaciones de pedido distintas
- **Valor total de reembolsos** = suma del valor total de pedidos reembolsados

Estos cálculos de campos de usuario también se incluyen en la pestaña **Transacciones** de los perfiles de usuario.

![La pestaña "Transacciones" con campos calculados del usuario.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:70%;"}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Dónde puedo ver los datos de compra a nivel de producto? {#where-can-i-view-product-level-purchase-data}

La pestaña **Transacciones** del perfil de usuario muestra campos calculados de alto nivel (como ingresos totales y total de pedidos). Para ver el detalle a nivel de producto de un usuario específico, usa el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) para consultar datos de eventos de comercio electrónico, o exporta los datos de eventos a través de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/).

A diferencia de los eventos de compra heredados, los eventos recomendados de comercio electrónico almacenan los detalles del producto como propiedades de eventos anidados dentro del array `products`. Estas propiedades están disponibles en la mensajería a través de Liquid y en la segmentación a través de [Extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension/).

### ¿Cómo segmento usuarios por un producto específico? {#how-do-i-segment-users-by-a-specific-product}

El segmentador te permite filtrar por el número de veces que un usuario realizó un evento de comercio electrónico. Para filtrar por propiedades específicas del producto (como `product_id` o `product_name`), usa [Extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension/), que admiten el filtrado de propiedades de eventos anidados. Por ejemplo, puedes encontrar todos los usuarios que compraron el producto "SKU-123" en los últimos 90 días.

### ¿Cuál es la diferencia entre los eventos de compra heredados y los eventos recomendados de comercio electrónico? {#whats-the-difference-between-legacy-purchase-events-and-ecommerce-recommended-events}

Los eventos de compra heredados usan el [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) de Braze y registran compras individuales de productos con un `product_id` y `price`. Los eventos recomendados de comercio electrónico (como `ecommerce.order_placed`) usan propiedades de eventos personalizados y capturan el contexto completo del pedido, incluyendo múltiples productos, descuentos y metadatos en un solo evento.

Con el lanzamiento de los eventos recomendados de comercio electrónico, Braze descontinuará el evento de compra heredado en el futuro. Si actualmente estás usando eventos de compra, recibirás un aviso con anticipación. Mientras tanto, puedes seguir usando los eventos de compra hasta la fecha oficial de descontinuación. Consulta el [resumen de eventos recomendados]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/) para más detalles.

### ¿Puedo agregar propiedades personalizadas a los eventos recomendados de comercio electrónico? {#can-i-add-custom-properties-to-ecommerce-recommended-events}

Los eventos recomendados de comercio electrónico tienen un esquema definido con campos obligatorios y opcionales. Puedes incluir datos personalizados adicionales dentro del objeto `metadata` de cada evento. Sin embargo, las etiquetas personalizadas a nivel de pedido o campos propietarios (como canal de compra o información de tienda de comercio minorista) no son compatibles como propiedades de nivel superior. Si necesitas estos campos para la segmentación, continúa enviándolos como eventos personalizados separados junto con tus eventos de comercio electrónico.

### ¿Necesito incluir external_id al enviar eventos de comercio electrónico? {#do-i-need-to-include-externalid-when-sending-ecommerce-events}

Depende de cómo estés enviando los eventos:

- **A través del SDK**: No. Cuando usas un SDK de Braze, los eventos se asocian automáticamente con el contexto del usuario actual del SDK (anónimo o identificado). No necesitas pasar un identificador de usuario con cada llamada de evento; en su lugar, puedes identificar al usuario en ese contexto usando métodos como `changeUser`.
- **A través de la REST API** (`/users/track`): Sí. Cada solicitud de API debe incluir un identificador de usuario, como `external_id`, `braze_id`, `user_alias`, `email` o `phone`, porque la API no tiene un contexto de "usuario actual".

### ¿Por qué las propiedades anidadas de productos no aparecen en el menú desplegable de configuración de Recomendaciones de elementos de IA? {#why-dont-nested-product-properties-appear-in-the-ai-recommendations-setup-dropdown}

Al configurar las [Recomendaciones de elementos de IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/), el menú desplegable **Nombre de la propiedad** solo lista las propiedades del evento de nivel superior (como `order_id`, `total_value` y `currency`). Las propiedades anidadas dentro del array `products` (por ejemplo, `products.product_id` o `products.variant_id`) pueden no aparecer en esta lista, pero puedes escribirlas manualmente usando notación de punto en el campo. Para la mayoría de las implementaciones de comercio electrónico, Braze recomienda usar `products.product_id` como identificador del elemento y emparejarlo con un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/) cuyos ID de elementos coincidan con tus valores de `product_id` o `variant_id`.

### ¿Por qué algunos de mis eventos de comercio electrónico no aparecen en Braze? {#why-are-some-of-my-ecommerce-events-not-appearing-in-braze}

Si los eventos no se muestran en los perfiles de usuario o en los registros, verifica lo siguiente:

- **Temporización del envío de datos del SDK**: El SDK de Braze almacena datos en caché localmente y los carga periódicamente (normalmente en 10-60 segundos). Llama a `requestImmediateDataFlush()` después de `logCustomEvent()` para forzar una carga inmediata.
- **Propiedades obligatorias**: Los eventos de comercio electrónico tienen propiedades obligatorias. Si falta una propiedad obligatoria o tiene un tipo de datos no válido, el evento puede ser rechazado. Verifica que la carga útil de tu evento coincida con el [esquema requerido](#types-of-ecommerce-recommended-events).
- **Precisión del nombre del evento**: Los nombres de eventos de comercio electrónico distinguen entre mayúsculas y minúsculas y deben coincidir exactamente (por ejemplo, `ecommerce.checkout_started`, no `ecommerce.checkoutStarted`).