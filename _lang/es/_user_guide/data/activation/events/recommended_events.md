---
nav_title: Eventos recomendados
article_title: Eventos recomendados
alias: /recommended_events/
page_order: 2
page_type: reference
description: "Este artículo de referencia describe los eventos recomendados, que son recomendaciones proporcionadas por Braze para eventos de comercio electrónico."
---

# Eventos recomendados {#recommended-events}

> Los eventos recomendados se basan en un marco que envía eventos personalizados estandarizados con esquemas JSON definidos. Cuando envías un evento recomendado, Braze lo valida contra su esquema en la ingesta y aplica un procesamiento especializado, como cálculos automáticos de campos o gestión del carrito, que los eventos personalizados genéricos no reciben. Para ciertos conjuntos de eventos de la industria, Braze también admite un tratamiento especial, como acciones desencadenantes basadas en acciones dedicadas para Campaigns y Canvas.

## Eventos recomendados de comercio electrónico {#ecommerce-recommended-events}

Los [eventos recomendados de comercio electrónico]({{site.baseurl}}/ecommerce_events) cubren seis pasos en el recorrido de compra: `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled` y `order_refunded`. Cuando envías estos eventos correctamente, Braze valida los datos y los pone a disposición de un conjunto creciente de características de la plataforma.

Estas características incluyen plantillas de Canvas para flujos de navegación abandonada, carrito abandonado, pago abandonado y confirmación de pedido; informes de comercio electrónico; y campos calculados del perfil de usuario para _Total Revenue_, _Total Orders_ y _Total Refunds_. También puedes crear segmentos usando filtrado de propiedades de producto anidadas a través de [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension), personalizar mensajes de carrito abandonado con la etiqueta de Liquid {% raw %}`{% shopping_cart %}`{% endraw %}, y alimentar las capacidades de BrazeAI<sup>TM</sup> como [Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events), [Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) y [recomendaciones de artículos]({{site.baseurl}}/user_guide/brazeai/item_recommendations), junto con otras capacidades.

Dado que estos eventos siguen un esquema definido, cada característica compatible puede leer los datos estructurados sin necesidad de mapeado personalizado de propiedades ni configuración por característica de tu parte.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

### Cómo funcionan los eventos de comercio electrónico {#how-ecommerce-events-work}

Los eventos de comercio electrónico son eventos personalizados con nombres y esquemas de propiedades predefinidos. Los envías usando el [SDK de Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events), el [endpoint REST API `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) o la [ingesta de datos en la nube (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion), y Braze valida cada evento contra su esquema en la ingesta. Cuando la validación es exitosa, Braze aplica automáticamente el posprocesamiento específico de ese tipo de evento, como calcular campos de ingresos y gestionar el estado del carrito en los perfiles de usuario.

{% alert note %}
Las cargas de CSV no admiten eventos de comercio electrónico. Usa el SDK, `/users/track` o CDI para enviar estos eventos.
{% endalert %}

Los eventos de comercio electrónico funcionan en todos los lugares donde funcionan otros eventos personalizados: desencadenantes y filtros para eventos personalizados realizados, informes de eventos personalizados y más. Sin embargo, su validación de esquema desbloquea capacidades adicionales, incluyendo:

- Acciones desencadenantes "Realiza un pedido" en Campaigns, Canvas, Rutas de Acción, desencadenantes de mensajes dentro de la aplicación y eliminación de tarjetas de contenido
- Campos calculados del perfil de usuario de comercio electrónico (**Total Revenue**, **Total Orders**, **Total Refunds**)
- Gestión del estado del carrito para flujos de carrito abandonado
- Datos más ricos para las características de BrazeAI<sup>TM</sup> como Predictive Events, Predictive Churn y recomendaciones de artículos

También puedes hacer referencia a los eventos de comercio electrónico por nombre en cualquier lugar donde la plataforma admita eventos personalizados. Por ejemplo, puedes desencadenar una campaña basada en acciones con eventos `ecommerce.product_viewed`, crear un segmento filtrando por eventos `ecommerce.checkout_started`, o exportar eventos `ecommerce.order_placed` a través de Currents.

#### Nomenclatura de eventos {#event-naming}

Los nombres de los eventos son exactos, distinguen entre mayúsculas y minúsculas, y están delimitados por puntos. Usa siempre el formato canónico. Si un nombre de evento no coincide exactamente con uno de los seis nombres canónicos, Braze lo trata como un evento personalizado estándar y no se realiza ningún posprocesamiento de comercio electrónico.

No puedes personalizar ni renombrar eventos.

- **Correcto:** `ecommerce.order_placed`
- **Incorrecto:** `order.placed`, `eCommerce_order_placed`, `Order_Placed`

#### Esquemas de eventos {#event-schemas}

Los seis eventos recomendados de comercio electrónico se corresponden con etapas del recorrido de compra. Dispara cada evento en el momento en que el usuario completa la acción correspondiente.

![Diagrama del recorrido del usuario a través de los seis eventos recomendados de comercio electrónico: product_viewed, cart_updated, checkout_started, order_placed, order_cancelled y order_refunded.]({% image_buster /assets/img/shopify/event_schemas.png %})

{% alert tip %}
Los siguientes ejemplos muestran la carga útil de REST API para cada evento.
Para el registro del lado del cliente, `ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started` y `ecommerce.order_placed` usan las API de eventos de comercio electrónico del SDK donde estén disponibles, mientras que `ecommerce.order_cancelled` y `ecommerce.order_refunded` usan `logCustomEvent`. Para ejemplos de implementación específicos de cada plataforma, consulta [Registrar eventos de comercio electrónico a través del SDK de Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).
{% endalert %}

{% tabs %}
{% tab ecommerce.product_viewed %}

Se desencadena cuando un usuario ve una página de detalle de producto. Este evento es compatible con las [notificaciones de vuelta en stock]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) y las [notificaciones de bajada de precio]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications) del catálogo de Braze.

#### Implementación del lado del cliente {#client-side-implementation}

Usa las API de eventos de comercio electrónico del SDK donde estén disponibles. Para ejemplos de implementación específicos de cada plataforma, consulta [Registrar eventos de comercio electrónico a través del SDK de Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

#### Propiedades del evento {#event-properties}

| Nombre de la propiedad | Tipo de datos | Obligatorio | Descripción |
| -------------- | ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product_id`   | String           | Sí      | Identificador único del producto (por ejemplo, SKU o ID de artículo). |
| `product_name` | String           | Sí      | Nombre de visualización del producto. |
| `variant_id`   | String           | Sí      | Identificador de la variante del producto (por ejemplo, `shirt_medium_blue`). |
| `image_url`    | String           | No       | URL de la imagen del producto. |
| `product_url`  | String           | No       | URL de la página del producto para más detalles. |
| `price`        | Float            | Sí      | Precio unitario de la variante en el momento de la visualización. |
| `currency`     | String           | Sí      | Código ISO 4217 de tres letras (por ejemplo, `USD` o `EUR`). |
| `source`       | String           | Sí      | Fuente de la que se origina el evento (por ejemplo, `web`, `ios` o `android`). |
| `type`         | Array of strings | No       | Obligatorio para usar las características de desencadenantes de catálogo de Braze para alertas de vuelta en stock y bajada de precio. Valores aceptados: `"price_drop"`, `"back_in_stock"` |
| `metadata`     | Object           | No       | Pares clave-valor flexibles (por ejemplo, `category` o `brand`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades del evento" }

#### Ejemplo de REST API {#rest-api-example}

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

Se desencadena cada vez que cambia el contenido del carrito de un usuario.

#### Implementación del lado del cliente

Usa las API de eventos de comercio electrónico del SDK donde estén disponibles. Para ejemplos de implementación específicos de cada plataforma, consulta [Registrar eventos de comercio electrónico a través del SDK de Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

Puedes enviar este evento de dos maneras:

- **Reemplazo completo del carrito:** omite `action` o establece `action` en `replace`. Incluye el conjunto completo de artículos en `products` con cantidades absolutas (unidades totales por variante en el carrito). Debes incluir `total_value`.
- **Actualizaciones incrementales del carrito:** establece `action` en `add` o `remove`. Incluye solo los artículos que cambiaron. Cada `quantity` es el número de unidades a agregar o quitar, no la cantidad total en el carrito. Para `add`, Braze incrementa la cantidad de la línea o agrega una nueva línea. Para `remove`, Braze decrementa la cantidad de la línea y la elimina cuando la cantidad llega a `0`. `total_value` es opcional para `add` y `remove`.

{% alert warning %}
Usa actualizaciones incrementales del carrito (`add` o `remove`) o reemplazo completo (sin `action` o `replace`) para un carrito dado. No se recomienda mezclar ambos enfoques para el mismo `cart_id` y puede llevar a un estado de carrito inconsistente en Braze.
{% endalert %}

Para desencadenar mensajería a partir de este evento, usa el desencadenante **Perform Cart Updated Event** en Canvas y Campaigns. Este desencadenante incluye un tratamiento especial para evitar que el carrito avance a través del embudo de compras.

{% alert tip %}
El carrito crea un objeto de mapeado de carritos en el perfil de usuario que alimenta la etiqueta de Liquid {% raw %}`{% shopping_cart %}`{% endraw %}. El carrito expira después de 30 días sin una actualización. Si dos perfiles de usuario se fusionan, Braze conserva ambos carritos.
{% endalert %}

#### Propiedades del evento

| Propiedad | Tipo de datos | Obligatorio | Descripción |
|-----------------|-----------|----------|-------------------------------------------------------------------------------------------------------------------------------|
| `cart_id`       | String    | Sí      | Identificador único del carrito. Compartido entre los eventos de carrito, pago y pedido para el mapeado del carrito del usuario. |
| `action`        | String    | No       | `add` (incrementar cantidad o agregar una línea), `remove` (decrementar cantidad; la línea se elimina en `0`) o `replace` (reemplazo completo del carrito, igual que omitir `action`). |
| `total_value`   | Float     | Condicional | Obligatorio cuando se omite `action` o es `replace`. Opcional cuando `action` es `add` o `remove`. |
| `subtotal_value`| Float     | No       | Valor del subtotal del carrito (después de descuentos, antes de impuestos/envío). |
| `tax`           | Float     | No       | Impuesto total aplicado al carrito. |
| `shipping`      | Float     | No       | Costo total de envío del carrito. |
| `currency`      | String    | Sí      | Código ISO 4217 de tres letras. |
| `products`      | Array     | Sí      | Artículos para esta actualización. Para reemplazo completo (sin `action` o `replace`), incluye el carrito completo con cantidades absolutas. Para `add` o `remove`, incluye solo las líneas que cambiaron; consulta las propiedades de producto. |
| `source`        | String    | Sí      | Fuente de la que se origina el evento. |
| `metadata`      | Object    | No       | Pares clave-valor flexibles para datos adicionales a nivel de evento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades del evento" }

#### Propiedades de producto (`products[]`) {#product-properties-products}

| Propiedad | Tipo de datos | Obligatorio | Descripción |
|-----------------|-----------|----------|-------------------------------------------------|
| `product_id`    | String    | Sí      | Identificador único del producto. |
| `product_name`  | String    | Sí      | Nombre de visualización del producto. |
| `variant_id`    | String    | Sí      | Identificador de la variante. |
| `image_url`     | String    | No       | URL de la imagen del producto. |
| `product_url`   | String    | No       | URL de la página del producto. |
| `quantity`      | Integer   | Sí      | Para reemplazo completo (sin `action` o `replace`), unidades en el carrito para esta línea. Para `add` o `remove`, cuántas unidades agregar o quitar. |
| `price`         | Float     | Sí      | Precio unitario de la variante. |
| `metadata`      | Object    | No       | Pares clave-valor flexibles (por ejemplo, `color` o `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades de producto (products[])" }

{% comment %}

{% subtabs local %}
{% subtab Web %}

##### `add`

`add` incrementa la cantidad o agrega una nueva línea. La propiedad `quantity` indica cuántas unidades agregar.

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

`remove` decrementa la cantidad en el monto indicado en `quantity`. La línea se elimina cuando la cantidad llega a `0`.

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

`replace` (u omitir `action`) envía el carrito completo. `total_value` es obligatorio.

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

`add` incrementa la cantidad o agrega una nueva línea. La propiedad `quantity` indica cuántas unidades agregar.

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

`remove` decrementa la cantidad en el monto indicado en `quantity`. La línea se elimina cuando la cantidad llega a `0`.

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

`replace` (u omitir `action`) envía el carrito completo. `total_value` es obligatorio.

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

`add` incrementa la cantidad o agrega una nueva línea. La propiedad `quantity` indica cuántas unidades agregar.

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

`remove` decrementa la cantidad en el monto indicado en `quantity`. La línea se elimina cuando la cantidad llega a `0`.

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

`replace` (u omitir `action`) envía el carrito completo. `total_value` es obligatorio.

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
{% subtab REST API %}

##### `add`

`add` incrementa la cantidad o agrega una nueva línea. La propiedad `quantity` indica cuántas unidades agregar.

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

`remove` decrementa la cantidad en el monto indicado en `quantity`. La línea se elimina cuando la cantidad llega a `0`.

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

`replace` (u omitir `action`) envía el carrito completo. `total_value` es obligatorio.

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

Se desencadena cuando el usuario inicia el flujo de pago (por ejemplo, selecciona "Pagar" o llega a la página de pago).

#### Implementación del lado del cliente

Usa las API de eventos de comercio electrónico del SDK donde estén disponibles. Para ejemplos de implementación específicos de cada plataforma, consulta [Registrar eventos de comercio electrónico a través del SDK de Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

#### Propiedades del evento

| Propiedad | Tipo | Obligatorio | Descripción |
|----------------|---------|----------|------------------------------------------------------------------------------------------------------------------|
| checkout_id    | String  | Sí      | Identificador único de la sesión de pago. |
| cart_id        | String  | No       | Identificador del carrito. Compartido entre los eventos de carrito, pago y pedido para el mapeado del carrito del usuario. |
| total_value    | Float   | Sí      | Valor monetario total del pago. |
| subtotal_value | Float   | No       | Valor del subtotal (después de descuentos, antes de impuestos/envío). |
| tax            | Float   | No       | Impuesto total aplicado al pago. |
| shipping       | Float   | No       | Costo total de envío. |
| currency       | String  | Sí      | Código ISO 4217 de tres letras. |
| products       | Array   | Sí      | Artículos en proceso de pago. Consulta la subtabla de propiedades de producto. |
| source         | String  | Sí      | Fuente de la que se origina el evento. |
| metadata       | Object  | No       | Pares clave-valor flexibles. Subpropiedad reconocida: `checkout_url` (String) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades del evento" }

#### Propiedades de producto (`products[]`)

| Propiedad | Tipo de datos | Obligatorio | Descripción |
|----------------|-----------|----------|----------------------------------------------------------|
| `product_id`   | String    | Sí      | Identificador único del producto. |
| `product_name` | String    | Sí      | Nombre de visualización del producto. |
| `variant_id`   | String    | Sí      | Identificador de la variante. |
| `image_url`    | String    | No       | URL de la imagen del producto. |
| `product_url`  | String    | No       | URL de la página del producto. |
| `quantity`     | Integer   | Sí      | Número de unidades en el carrito. |
| `price`        | Float     | Sí      | Precio unitario de la variante. |
| `metadata`     | Object    | No       | Pares clave-valor flexibles (por ejemplo, color, talla). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades de producto (products[])" }

#### Ejemplo de REST API

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

Se desencadena cuando un pedido se completa correctamente o se confirma el pago.

#### Implementación del lado del cliente

Usa las API de eventos de comercio electrónico del SDK donde estén disponibles. Para ejemplos de implementación específicos de cada plataforma, consulta [Registrar eventos de comercio electrónico a través del SDK de Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

{% alert important %}
Este evento es el principal impulsor de ingresos. Incrementa `total_revenue` en el valor de `total_value` e incrementa `total_orders` en 1 en el perfil de usuario.
{% endalert %}

#### Propiedades del evento

| Propiedad | Tipo de datos | Obligatorio | Descripción |
|-----------------|-----------|----------|-----------------------------------------------------------------------------------------------|
| `order_id`      | String    | Sí      | Identificador único del pedido. |
| `cart_id`       | String    | No       | Identificador del carrito. Compartido entre los eventos de carrito, pago y pedido para el mapeado del carrito del usuario. |
| `total_value`   | Float     | Sí      | Valor monetario total del pedido. |
| `subtotal_value`| Float     | No       | Valor del subtotal (después de descuentos, antes de impuestos/envío). |
| `tax`           | Float     | No       | Impuesto total aplicado al pedido. |
| `shipping`      | Float     | No       | Costo total de envío. |
| `currency`      | String    | Sí      | Código ISO 4217 de tres letras. |
| `total_discounts`| Float    | No       | Monto total de descuentos aplicados al pedido. |
| `discounts`     | Array     | No       | Lista detallada de descuentos aplicados. |
| `products`      | Array     | Sí      | Artículos en el pedido. Consulta la subtabla de propiedades de producto. |
| `source`        | String    | Sí      | Fuente de la que se origina el evento. |
| `metadata`      | Object    | No       | Pares clave-valor flexibles. Subpropiedad reconocida: `order_status_url` (String) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades del evento" }

#### Propiedades de producto (`products[]`)

| Propiedad | Tipo de datos | Obligatorio | Descripción |
|-----------------|-----------|----------|---------------------------------------------|
| `product_id`    | String    | Sí      | Identificador único del producto. |
| `product_name`  | String    | Sí      | Nombre de visualización del producto. |
| `variant_id`    | String    | Sí      | Identificador de la variante. |
| `image_url`     | String    | No       | URL de la imagen del producto. |
| `product_url`   | String    | No       | URL de la página del producto. |
| `quantity`      | Integer   | Sí      | Número de unidades en el carrito. |
| `price`         | Float     | Sí      | Precio unitario de la variante. |
| `metadata`      | Object    | No       | Pares clave-valor flexibles (por ejemplo, `color` o `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades de producto (products[])" }

#### Ejemplo de REST API

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

Se desencadena cuando se cancela un pedido.

#### Implementación del lado del cliente

Usa `logCustomEvent`. Para ejemplos de implementación específicos de cada plataforma, consulta [Registrar eventos de comercio electrónico a través del SDK de Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

{% alert important %}
Este evento decrementa `total_orders` en 1 en el perfil de usuario. No afecta a `total_revenue`; usa `order_refunded` para ajustar los ingresos.
{% endalert %}

#### Propiedades del evento

| Propiedad | Tipo | Obligatorio | Descripción |
|------------------|---------|----------|--------------------------------------------------------------------------------------------------|
| `order_id`       | String  | Sí      | Identificador único del pedido. |
| `total_value`    | Float   | Sí      | Valor monetario total del pedido que se cancela. Debe ser ≥ 0; envía el monto absoluto; Braze se encarga del decremento. |
| `subtotal_value` | Float   | No       | Valor del subtotal (después de descuentos, antes de impuestos/envío). |
| `tax`            | Float   | No       | Impuesto total aplicado al pedido. |
| `shipping`       | Float   | No       | Costo total de envío. |
| `currency`       | String  | Sí      | Código ISO 4217 de tres letras. |
| `total_discounts`| Float   | No       | Monto total de descuentos aplicados al pedido. |
| `discounts`      | Array   | No       | Lista detallada de descuentos aplicados. |
| `cancel_reason`  | String  | Sí      | Motivo por el que se canceló el pedido. |
| `products`       | Array   | Sí      | Artículos en el pedido cancelado. Consulta la subtabla de propiedades de producto. |
| `source`         | String  | Sí      | Fuente de la que se origina el evento. |
| `metadata`       | Object  | No       | Pares clave-valor flexibles. Subpropiedad reconocida: `order_status_url` (String) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades del evento" }

#### Propiedades de producto (`products[]`)

| Propiedad | Tipo de datos | Obligatorio | Descripción |
|----------------|-----------|----------|-----------------------------------------------|
| `product_id`   | String    | Sí      | Identificador único del producto. |
| `product_name` | String    | Sí      | Nombre de visualización del producto. |
| `variant_id`   | String    | Sí      | Identificador de la variante. |
| `image_url`    | String    | No       | URL de la imagen del producto. |
| `product_url`  | String    | No       | URL de la página del producto. |
| `quantity`     | Integer   | Sí      | Número de unidades en el carrito. |
| `price`        | Float     | Sí      | Precio unitario de la variante. |
| `metadata`     | Object    | No       | Pares clave-valor flexibles (por ejemplo, `color` o `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades de producto (products[])" }

#### Ejemplo de REST API

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

Se desencadena cuando se emite un reembolso total o parcial.

#### Implementación del lado del cliente

Usa `logCustomEvent`. Para ejemplos de implementación específicos de cada plataforma, consulta [Registrar eventos de comercio electrónico a través del SDK de Braze]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

{% alert important %}
Este evento decrementa `total_revenue` en el valor de `total_value` e incrementa `total_refunds` en el perfil de usuario. Para reembolsos parciales, establece `total_value` solo en el monto reembolsado, no en el total original del pedido.
{% endalert %}

#### Propiedades del evento

| Propiedad | Tipo de datos | Obligatorio | Descripción |
|-------------------|-----------|----------|------------------------------------------------------------------------------------------------------|
| `order_id`        | String    | Sí      | Identificador único del pedido original. |
| `total_value`     | Float     | Sí      | Valor monetario total del reembolso. Debe ser ≥ 0; envía el monto absoluto; Braze se encarga del incremento a total_refunds. |
| `currency`        | String    | Sí      | Código ISO 4217 de tres letras. |
| `total_discounts` | Float     | No       | Monto total de descuentos aplicados originalmente. |
| `discounts`       | Array     | No       | Lista detallada de descuentos. |
| `products`        | Array     | Sí      | Artículos que se reembolsan. Consulta la subtabla de propiedades de producto. |
| `source`          | String    | Sí      | Fuente de la que se origina el evento. |
| `metadata`        | Object    | No       | Pares clave-valor flexibles. Subpropiedad reconocida: `order_status_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades del evento" }

#### Propiedades de producto (`products[]`)

| Propiedad | Tipo de datos | Obligatorio | Descripción |
|-----------------|-----------|----------|-------------------------------------------------------|
| `product_id`    | String    | Sí      | Identificador único del producto. |
| `product_name`  | String    | Sí      | Nombre de visualización del producto. |
| `variant_id`    | String    | Sí      | Identificador de la variante. |
| `image_url`     | String    | No       | URL de la imagen del producto. |
| `product_url`   | String    | No       | URL de la página del producto. |
| `quantity`      | Integer   | Sí      | Número de unidades en el carrito. |
| `price`         | Float     | Sí      | Precio unitario de la variante. |
| `metadata`      | Object    | No       | Pares clave-valor flexibles (por ejemplo, `color` o `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades de producto (products[])" }

#### Ejemplos de REST API {#rest-api-examples}

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

### Posprocesamiento de eventos de comercio electrónico {#ecommerce-event-post-processing}

Cuando envías un evento de comercio electrónico, Braze lo valida contra el esquema esperado para ese nombre de evento.

La siguiente tabla resume lo que Braze hace automáticamente para cada evento cuando la validación es exitosa. Para saber qué sucede cuando la validación falla, consulta [Validación de eventos y solución de problemas](#event-validation-and-troubleshooting).

| Evento | Qué hace Braze automáticamente |
|------------------------------|-------------------------------------------------------------------------------------------------------------------|
| `ecommerce.order_placed`     | Incrementa **Total Revenue** en `total_value` y **Total Orders** en 1 en el perfil de usuario. |
| `ecommerce.order_cancelled`  | Decrementa **Total Orders** en 1. |
| `ecommerce.order_refunded`   | Decrementa **Total Revenue** en `total_value` e incrementa **Total Refund Value**. |
| `ecommerce.cart_updated`     | Crea o actualiza el objeto de mapeado de carritos en el perfil de usuario (cargas útiles de carrito completo o actualizaciones incrementales del carrito con `action` opcional: `add`, `remove` o `replace`). El carrito expira después de 30 días sin una actualización. |
| `ecommerce.product_viewed`   | Sin cambios en el perfil de usuario. Disponible para segmentación, desencadenantes y características de BrazeAI<sup>TM</sup> (como recomendaciones de artículos). |
| `ecommerce.checkout_started` | Sin cambios en el perfil de usuario. Disponible para segmentación y desencadenantes (por ejemplo, flujos de pago abandonado). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Posprocesamiento de eventos de comercio electrónico" }

{% alert important %}
Los valores de moneda que no sean USD se convierten automáticamente a USD usando el tipo de cambio de la fecha en que se reporta el evento. Si ya reportas en USD, codifica `USD` como la moneda para evitar conversiones no deseadas.
{% endalert %}

## Detalles de implementación {#implementation-details}

### Puntos de datos y facturación {#data-points-and-billing}

Los eventos de comercio electrónico no consumen [puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points). Puedes registrarlos sin ningún impacto en tu uso de puntos de datos.

### Límite de tamaño de eventos {#event-size-limit}

Las propiedades de eventos enviadas a `/users/track` tienen un límite de 102 400 bytes (100 KB) por evento. Para mensajes desencadenados de Campaigns y Canvas, las `trigger_properties` enviadas a [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) y [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) tienen un límite predeterminado más estricto de 51 200 bytes (50 KB).

Como práctica recomendada, envía solo la información de producto que necesitas para desencadenar, personalizar o atribuir el evento. Almacena detalles de producto más ricos, como descripciones, listas completas de variantes, inventario o imágenes alternativas, en los catálogos de Braze. Haz referencia a estos detalles por `product_id` o `variant_id` al enviar mensajes. Usa el objeto `metadata` de forma selectiva para el contexto específico del pedido o producto que la mensajería utilizará.

### Manejo de moneda {#currency-handling}

Braze convierte automáticamente los valores de moneda que no sean USD a USD usando el tipo de cambio de la fecha en que se reporta el evento. Este valor convertido es el que aparece en las métricas de ingresos.

{% alert tip %}
Si solo operas en USD, codifica `"currency": "USD"` en cada evento para evitar conversiones innecesarias.
{% endalert %}

### Campo de fuente {#source-field}

La propiedad de fuente es una cadena obligatoria que identifica de dónde se originó el evento. Por ejemplo, `shopify`, `in-store POS` o `custom_api`. Esto te ayuda a distinguir las fuentes de integración al analizar datos en exportaciones de Currents o al depurar problemas de validación.

### Flexibilidad de metadatos {#metadata-flexibility}

Tanto los objetos de metadatos a nivel de evento como a nivel de producto aceptan pares clave-valor arbitrarios, por lo que puedes adjuntar dimensiones personalizadas sin modificar el esquema principal. Ejemplos comunes incluyen `order_status_url`, `gift_wrapped`, `loyalty_points_earned` o `warehouse_id`. Estas propiedades están disponibles en la personalización con Liquid, las exportaciones de Currents y la segmentación a través de [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension).

{% alert important %}
Los eventos recomendados usan un esquema estricto. Como resultado, agregar propiedades personalizadas en el nivel superior de las propiedades hará que la validación falle. Coloca todas las propiedades personalizadas dentro del objeto `metadata` a nivel de evento o del objeto `metadata` a nivel de producto dentro de `products[]`. Estas permanecen disponibles para Liquid, Currents y segmentación igual que los campos de nivel superior.
{% endalert %}

## Validación de eventos y solución de problemas {#event-validation-and-troubleshooting}

Cuando envías un evento recomendado de comercio electrónico a través de `/users/track` o cualquier SDK de Braze, Braze valida la carga útil contra el esquema JSON del evento durante el procesamiento del evento recomendado. La validación se ejecuta automáticamente en cada evento cuyo nombre coincida exactamente con un evento recomendado (por ejemplo, `ecommerce.order_placed` o `ecommerce.cart_updated`).

### Qué validamos {#what-we-validate}

Para cada evento cuyo nombre coincida con un evento recomendado de comercio electrónico, Braze verifica:

| Verificación | Ejemplo |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Nombre del evento | Debe ser exacto. Por ejemplo, `ecommerce.cart_updated` es correcto, no `ecommerce.Cart_Updated`, `cartupdated` ni `cart_updated`. |
| Propiedades obligatorias presentes | `order_placed` requiere `order_id`, `total_value`, `currency`, `products` y `source`. |
| Tipos de datos correctos | `total_value` debe ser un número; `currency` debe ser una cadena; `products` debe ser un array. |
| Sin propiedades adicionales de nivel superior | Los campos personalizados bajo propiedades causan un fallo. Usa el objeto `metadata` en su lugar. |
| Restricciones de valores | Los campos monetarios deben ser ≥ `0`. `currency` debe ser una cadena ISO 4217 válida. |
| Campos por producto | Cada elemento en `products[]` debe incluir `product_id`, `product_name`, `variant_id`, `quantity` y `price`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Qué validamos" }

### Por qué validamos {#why-we-validate}

Los eventos de comercio electrónico alimentan características que dependen de datos consistentes y predecibles, incluyendo el seguimiento de ingresos, la etiqueta de Liquid {% raw %}`{% shopping_cart %}`{% endraw %}, el desencadenante de carrito abandonado y los informes. Cuando las cargas útiles se desvían del esquema, estas características producen inexactitudes silenciosas (totales de ingresos incorrectos, carritos faltantes, desencadenantes rotos). La validación aplica el contrato de forma anticipada para que las características posteriores se comporten de manera predecible.

### Cuando la validación es exitosa {#when-validation-passes}

El evento se procesa como un evento recomendado de comercio electrónico con todo el posprocesamiento asociado. Consulta [Esquemas de eventos](#event-schemas) para la lista completa de comportamientos desencadenados por cada tipo de evento.

#### Verificar un evento exitoso {#verify-a-successful-event}

Después de enviar un evento, puedes confirmar que fue aceptado y procesado correctamente usando cualquiera de los siguientes métodos:

- [Registro de eventos de usuario]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log): abre el perfil del usuario en el panel y revisa su actividad. Los eventos recomendados aparecen con su carga útil completa de propiedades, para que puedas confirmar que el evento llegó y que los valores coinciden con lo que enviaste.
- [Informe de eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report): ve a **Analytics** > **Custom Events** para ver los conteos agregados de cada evento recomendado a lo largo del tiempo. Esto es útil para confirmar que el tráfico de producción fluye como se espera cuando tu integración está en vivo.
- [Usuarios de prueba]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups?utm_source=operator_user&utm_medium=dashboard#adding-test-users): marca a un usuario en tu espacio de trabajo de desarrollo como usuario de prueba, luego desencadena eventos desde tu integración contra ese usuario. Los usuarios de prueba están marcados en el panel, lo que facilita aislar e inspeccionar el comportamiento de extremo a extremo.

### Cuando la validación falla {#when-validation-fails}

El evento no se procesa como un evento recomendado. Específicamente:

- **El evento se descarta por completo.** Los eventos recomendados de comercio electrónico no válidos no se registran en el perfil de usuario, no aparecen en Currents y no están disponibles para segmentación.
- Las características posteriores de eventos recomendados no se ejecutan, incluyendo:
  - Seguimiento de ingresos (informes de ingresos, campos calculados del usuario como `total_revenue`)
  - Actualizaciones del objeto de carrito en el perfil de usuario
  - Desencadenantes "Perform Cart Updated Event" o "Placed Order" en Canvas y Campaigns

La forma en que se reportan los errores depende de la ruta de ingesta:

- **REST API (`/users/track`):** cada evento no válido se reporta en el array de errores de la respuesta. Cada entrada te indica qué evento falló (índice) y por qué (tipo). El campo `message` de nivel superior aún dice "success", lo que solo significa que tu solicitud llegó a Braze, no que cada evento fuera válido. Siempre verifica si hay un array de errores en la respuesta.
- **SDK de Braze:** las llamadas del SDK retornan inmediatamente y la validación se ejecuta en segundo plano, por lo que los errores no se envían de vuelta a tu aplicación. Para enterarte de los fallos de validación de eventos de comercio electrónico, busca el correo electrónico de resumen de fallos (consulta [Encontrar fallos](#find-failures)).

#### Ejemplo de respuesta de error de la API {#example-api-error-response}

El endpoint `/users/track` devuelve errores a nivel de campo que indican qué propiedades fallaron y por qué. Ten en cuenta que el `message` de nivel superior puede devolver `"success"` porque el evento fue aceptado en el pipeline; el array `errors` te indica qué campos fallaron en la validación del esquema. Consulta el siguiente ejemplo de respuesta de error.

```json
{
 "message": "success",
 "errors": [{ "index": 0, "input_array": "purchases", "type": "'currency' must be an ISO 4217 currency" }]
}
```

Los fallos también se clasifican internamente y se agregan para el correo electrónico de resumen de fallos:

| Tipo de fallo | Significado | Ejemplo |
|------------------------|---------------------------------------------------|----------------------------------------------------------------|
| `missing_property`     | Falta un campo obligatorio. | `order_placed` enviado sin `order_id`. |
| `extra_property`       | Se agregó un campo que el esquema no define. | Un campo personalizado `gift_wrapped` en el nivel superior de `properties` en lugar de dentro de `metadata`. |
| `unexpected_data_type` | Un campo tiene el tipo incorrecto. | `total_value: "29.99"` (cadena) en lugar de `29.99` (número). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ejemplo de respuesta de error de la API" }

{% alert note %}
Los nombres de eventos que no coinciden exactamente con un evento recomendado (por ejemplo, `ecommerce.OrderPlaced`) omiten la validación por completo y se registran como eventos personalizados ordinarios. Aparecen en Currents y en la segmentación con el nombre que enviaste, pero no reciben procesamiento de evento recomendado ni una entrada de `errors` en la respuesta.
{% endalert %}

#### Encontrar fallos {#find-failures}

Braze envía por correo electrónico a los administradores de tu espacio de trabajo un resumen de los fallos de validación de eventos recomendados para que puedas identificar y corregir problemas de integración sin monitorear manualmente cada evento.

El correo electrónico de resumen incluye:

- **Conteo total de errores:** conteos de errores para el período de reporte.
- **Errores por evento:** un desglose de cuántos eventos fallaron para cada tipo de evento recomendado (por ejemplo, `ecommerce.cart_updated` y `ecommerce.order_placed`). Usa esto para identificar qué eventos de tu integración necesitan atención primero.
- **Errores por fuente:** una división entre API y SDK, para que puedas identificar qué integración está generando los fallos.

Si no estás recibiendo estos correos electrónicos o deseas verificar la lista de destinatarios, ponte en contacto con tu equipo de cuenta de Braze.

#### Diagnosticar y corregir fallos {#diagnose-and-fix-failures}

Cuando recibas un correo electrónico de resumen de fallos:

1. **Identifica el evento que falla y la fuente.** El correo electrónico separa los fallos por nombre de evento y fuente de integración (`sdk` versus `rest_api`), para que puedas identificar qué integración necesita la corrección. Si tienes múltiples fuentes enviando el mismo evento (por ejemplo, el SDK de tu tienda y un webhook de backend ambos enviando `cart_updated`), abórdalos de forma independiente.
2. **Compara tu carga útil con el esquema** en [Esquemas de eventos](#event-schemas). La mayoría de los fallos caen en uno de tres patrones:
   - `missing_property`: falta un campo obligatorio. Para resolverlo, agrega el campo obligatorio.
   - `extra_property`: un campo personalizado está en el nivel superior de `properties`. Para resolverlo, mueve el campo personalizado dentro de `metadata` (a nivel de evento) o `products[].metadata` (por producto).
   - `unexpected_data_type`: un valor tiene el tipo incorrecto (por ejemplo, `total_value` enviado como cadena). Para resolverlo, convierte el valor antes de enviarlo.
3. **Prueba la carga útil corregida en un espacio de trabajo de desarrollo** antes de implementarla en producción. Envía un evento de prueba conocido para un usuario de prueba, luego verifica el comportamiento esperado del evento recomendado en el perfil de ese usuario (por ejemplo, que el objeto de carrito se actualice, que los ingresos se incrementen o que el desencadenante de carrito abandonado se active).
4. **Monitorea el siguiente correo electrónico de fallos** para confirmar que el conteo de fallos para ese evento, fuente y tipo baja a cero.

Para los requisitos completos de propiedades por evento, consulta [Esquemas de eventos](#event-schemas).