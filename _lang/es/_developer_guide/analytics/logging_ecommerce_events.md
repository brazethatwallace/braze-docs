---
nav_title: Registrar eventos de comercio electrónico
article_title: Registrar eventos de comercio electrónico a través del SDK de Android
page_order: 3.25
description: "Aprende a registrar eventos recomendados de comercio electrónico a través del SDK de Android de Braze usando clases de eventos tipadas y logEcommerceEvent."
platform:
  - Android
---

# Registrar eventos de comercio electrónico {#log-ecommerce-events}

> Aprende a registrar [eventos recomendados de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/) a través del SDK de Android de Braze usando clases de eventos tipadas y `Braze.logEcommerceEvent`. Para esquemas de propiedades de eventos, características de la plataforma y validación de ingesta, consulta [Eventos recomendados]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/) y [Validación de eventos y solución de problemas]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-validation-and-troubleshooting).

{% alert note %}
Para los SDK envolventes no incluidos en la lista, usa el método nativo de Android correspondiente en su lugar.
{% endalert %}

El SDK de Android [42.3.0+](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.3.0) proporciona clases de eventos de comercio electrónico tipadas con validación del lado del cliente en el momento de la construcción y serialización automática a `snake_case` cuando llamas a `Braze.logEcommerceEvent`.

| Clase de Android | Nombre del evento | Notas |
| ------------- | ---------- | ----- |
| `ProductViewedEvent` | `ecommerce.product_viewed` | Aplana los campos del producto al nivel superior de `properties` (sin array `products`). Esta clase no admite la propiedad `type` de nivel superior para desencadenadores de catálogo. Si necesitas `type`, usa [`logCustomEvent`](#manual-logging-with-logcustomevent) o la REST API. |
| `CartUpdatedEvent` | `ecommerce.cart_updated` | Usa `CartUpdatedAction` (`ADD`, `REMOVE`, `REPLACE`) para la propiedad `action`. |
| `CheckoutStartedEvent` | `ecommerce.checkout_started` | |
| `OrderPlacedEvent` | `ecommerce.order_placed` | Admite `cartId`, `totalDiscounts` y `discounts` opcionales. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Clases de eventos de comercio electrónico del SDK de Android" }

{% alert important %}
`ecommerce.order_cancelled` y `ecommerce.order_refunded` no están disponibles como clases tipadas del SDK de Android. Regístralos con [`logCustomEvent`](#manual-logging-with-logcustomevent) o la REST API.
{% endalert %}

## Bloques de construcción compartidos {#shared-building-blocks}

- `EcommerceProduct`: Elementos de línea para eventos de carrito, pago y pedido.
  - Obligatorios: `productId`, `productName`, `variantId`, `price`, `quantity` (`Long` no negativo)
  - Opcionales: `imageUrl`, `productUrl`, `metadata`
- `BrazeProperties`: `metadata` a nivel de evento o de producto. Las claves deben ser cadenas no vacías de como máximo 255 caracteres sin signo de dólar ($) inicial.

## Validación del lado del cliente {#client-side-validation}

Las cargas útiles no válidas lanzan `IllegalArgumentException` cuando construyes la clase del evento, por lo que el evento nunca se pone en cola. Reglas comunes:

| Campo o regla | Validación |
| ------------ | ---------- |
| IDs y nombres de cadena (`product_id`, `product_name`, `variant_id`, `cart_id`, `checkout_id`, `order_id`, `source`, URLs opcionales) | No vacíos, hasta 255 caracteres |
| `price`, `total_value`, `total_discounts` | Debe ser mayor o igual a `0` |
| `currency` | Código ISO 4217 válido (recortado y convertido a mayúsculas por el SDK) |
| `products` (eventos de carrito, pago, pedido) | Al menos un `EcommerceProduct` |
| `quantity` (por producto) | Entero no negativo |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reglas de validación del lado del cliente de Android para eventos de comercio electrónico" }

En el momento del envío, si las propiedades serializadas superan el límite de tamaño del SDK, `logEcommerceEvent` registra un error y no envía el evento.

## Ejemplos de código {#code-examples}

{% tabs local %}
{% tab Kotlin %}

{% subtabs local %}
{% subtab product_viewed %}

```kotlin
import com.braze.Braze
import com.braze.models.outgoing.BrazeProperties
import com.braze.models.recommended.ecommerce.ProductViewedEvent

val metadata = BrazeProperties()
  .addProperty("sku", "SS-R-101")
  .addProperty("category", "Apparel")

val productViewedEvent = ProductViewedEvent(
  productId = "PROD101",
  productName = "Silk Scarf",
  variantId = "SCARF_RED_SILK",
  price = 150.00,
  currency = "EUR",
  source = "https://braze-fashion.eu",
  imageUrl = "https://braze-fashion.eu/images/scarf_red.jpg",
  productUrl = "https://braze-fashion.eu/products/scarf",
  metadata = metadata,
)

Braze.getInstance(context).logEcommerceEvent(productViewedEvent)
```

{% endsubtab %}
{% subtab cart_updated %}

Establece `action` usando `CartUpdatedAction`:

| Valor | Valor en la transmisión | Descripción |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | Aumenta la cantidad o agrega una línea. |
| `CartUpdatedAction.REMOVE` | `remove` | Disminuye la cantidad; elimina la línea en `0`. |
| `CartUpdatedAction.REPLACE` | `replace` | Reemplaza el carrito completo (predeterminado). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Valores de CartUpdatedAction para ecommerce.cart_updated" }

```kotlin
import com.braze.Braze
import com.braze.models.recommended.ecommerce.CartUpdatedAction
import com.braze.models.recommended.ecommerce.CartUpdatedEvent
import com.braze.models.recommended.ecommerce.EcommerceProduct

val product = EcommerceProduct(
  productId = "SKU-RUN-4821",
  productName = "Ultraboost Running Shoe",
  variantId = "UB-BLK-11",
  price = 189.99,
  quantity = 1,
)

val cartUpdatedEvent = CartUpdatedEvent(
  cartId = "cart_abc123",
  currency = "USD",
  source = "android",
  totalValue = 189.99,
  products = listOf(product),
  action = CartUpdatedAction.ADD,
)

Braze.getInstance(context).logEcommerceEvent(cartUpdatedEvent)
```

{% endsubtab %}
{% subtab checkout_started %}

```kotlin
import com.braze.Braze
import com.braze.models.outgoing.BrazeProperties
import com.braze.models.recommended.ecommerce.CheckoutStartedEvent
import com.braze.models.recommended.ecommerce.EcommerceProduct

val products = listOf(
  EcommerceProduct(
    productId = "SKU-RUN-4821",
    productName = "Ultraboost Running Shoe",
    variantId = "UB-BLK-11",
    price = 189.99,
    quantity = 1,
  ),
)

val checkoutStartedEvent = CheckoutStartedEvent(
  checkoutId = "chk_88291",
  currency = "USD",
  source = "android",
  totalValue = 234.96,
  products = products,
  cartId = "cart_abc123",
  metadata = BrazeProperties().addProperty("checkout_url", "https://www.example.com/checkout/chk_88291"),
)

Braze.getInstance(context).logEcommerceEvent(checkoutStartedEvent)
```

{% endsubtab %}
{% subtab order_placed %}

```kotlin
import com.braze.Braze
import com.braze.models.outgoing.BrazeProperties
import com.braze.models.recommended.ecommerce.EcommerceProduct
import com.braze.models.recommended.ecommerce.OrderPlacedEvent

val products = listOf(
  EcommerceProduct(
    productId = "SKU-RUN-4821",
    productName = "Ultraboost Running Shoe",
    variantId = "UB-BLK-11",
    price = 189.99,
    quantity = 1,
  ),
)

val orderPlacedEvent = OrderPlacedEvent(
  orderId = "ord_77821",
  currency = "USD",
  source = "android",
  totalValue = 224.96,
  products = products,
  cartId = "cart_abc123",
  totalDiscounts = 10.0,
  discounts = listOf(
    mapOf("code" to "SPRING10", "amount" to 10.0, "type" to "percentage"),
  ),
  metadata = BrazeProperties().addProperty("order_status_url", "https://www.example.com/orders/ord_77821/status"),
)

Braze.getInstance(context).logEcommerceEvent(orderPlacedEvent)
```

{% endsubtab %}
{% subtab order_cancelled %}

Braze no proporciona una clase tipada del SDK para este evento. Usa `logCustomEvent` con una carga útil que coincida con el esquema del evento `ecommerce.order_cancelled`.

```kotlin
import com.braze.Braze
import com.braze.models.outgoing.BrazeProperties
import org.json.JSONArray
import org.json.JSONObject

val properties = BrazeProperties(
  JSONObject()
    .put("order_id", "ord_77821")
    .put("total_value", 224.96)
    .put("currency", "USD")
    .put("cancel_reason", "customer_request")
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
)

Braze.getInstance(context).logCustomEvent("ecommerce.order_cancelled", properties)
```

{% endsubtab %}
{% subtab order_refunded %}

Braze no proporciona una clase tipada del SDK para este evento. Usa `logCustomEvent` con una carga útil que coincida con el esquema del evento `ecommerce.order_refunded`.

```kotlin
import com.braze.Braze
import com.braze.models.outgoing.BrazeProperties
import org.json.JSONArray
import org.json.JSONObject

val properties = BrazeProperties(
  JSONObject()
    .put("order_id", "ord_77821")
    .put("total_value", 189.99)
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
)

Braze.getInstance(context).logCustomEvent("ecommerce.order_refunded", properties)
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Java %}

{% subtabs local %}
{% subtab product_viewed %}

```java
import com.braze.Braze;
import com.braze.models.outgoing.BrazeProperties;
import com.braze.models.recommended.ecommerce.ProductViewedEvent;

BrazeProperties metadata = new BrazeProperties()
    .addProperty("sku", "SS-R-101")
    .addProperty("category", "Apparel");

ProductViewedEvent productViewedEvent = new ProductViewedEvent(
    /* productId */ "PROD101",
    /* productName */ "Silk Scarf",
    /* variantId */ "SCARF_RED_SILK",
    /* price */ 150.00,
    /* currency */ "EUR",
    /* source */ "https://braze-fashion.eu",
    /* imageUrl */ "https://braze-fashion.eu/images/scarf_red.jpg",
    /* productUrl */ "https://braze-fashion.eu/products/scarf",
    /* metadata */ metadata
);

Braze.getInstance(context).logEcommerceEvent(productViewedEvent);
```

{% endsubtab %}
{% subtab cart_updated %}

Establece `action` usando `CartUpdatedAction`:

| Valor | Valor en la transmisión | Descripción |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | Aumenta la cantidad o agrega una línea. |
| `CartUpdatedAction.REMOVE` | `remove` | Disminuye la cantidad; elimina la línea en `0`. |
| `CartUpdatedAction.REPLACE` | `replace` | Reemplaza el carrito completo (predeterminado). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Valores de CartUpdatedAction para ecommerce.cart_updated" }

```java
import com.braze.Braze;
import com.braze.models.recommended.ecommerce.CartUpdatedAction;
import com.braze.models.recommended.ecommerce.CartUpdatedEvent;
import com.braze.models.recommended.ecommerce.EcommerceProduct;
import java.util.Collections;

EcommerceProduct product = new EcommerceProduct(
    /* productId */ "SKU-RUN-4821",
    /* productName */ "Ultraboost Running Shoe",
    /* variantId */ "UB-BLK-11",
    /* price */ 189.99,
    /* quantity */ 1
);

CartUpdatedEvent cartUpdatedEvent = new CartUpdatedEvent(
    /* cartId */ "cart_abc123",
    /* currency */ "USD",
    /* source */ "android",
    /* totalValue */ 189.99,
    /* products */ Collections.singletonList(product),
    /* metadata */ null,
    /* action */ CartUpdatedAction.ADD
);

Braze.getInstance(context).logEcommerceEvent(cartUpdatedEvent);
```

{% endsubtab %}
{% subtab checkout_started %}

```java
import com.braze.Braze;
import com.braze.models.outgoing.BrazeProperties;
import com.braze.models.recommended.ecommerce.CheckoutStartedEvent;
import com.braze.models.recommended.ecommerce.EcommerceProduct;
import java.util.Collections;

EcommerceProduct product = new EcommerceProduct(
    /* productId */ "SKU-RUN-4821",
    /* productName */ "Ultraboost Running Shoe",
    /* variantId */ "UB-BLK-11",
    /* price */ 189.99,
    /* quantity */ 1
);

BrazeProperties metadata = new BrazeProperties()
    .addProperty("checkout_url", "https://www.example.com/checkout/chk_88291");

CheckoutStartedEvent checkoutStartedEvent = new CheckoutStartedEvent(
    /* checkoutId */ "chk_88291",
    /* currency */ "USD",
    /* source */ "android",
    /* totalValue */ 234.96,
    /* products */ Collections.singletonList(product),
    /* cartId */ "cart_abc123",
    /* metadata */ metadata
);

Braze.getInstance(context).logEcommerceEvent(checkoutStartedEvent);
```

{% endsubtab %}
{% subtab order_placed %}

```java
import com.braze.Braze;
import com.braze.models.outgoing.BrazeProperties;
import com.braze.models.recommended.ecommerce.EcommerceProduct;
import com.braze.models.recommended.ecommerce.OrderPlacedEvent;
import java.util.Collections;

EcommerceProduct product = new EcommerceProduct(
    /* productId */ "SKU-RUN-4821",
    /* productName */ "Ultraboost Running Shoe",
    /* variantId */ "UB-BLK-11",
    /* price */ 189.99,
    /* quantity */ 1
);

BrazeProperties metadata = new BrazeProperties()
    .addProperty("order_status_url", "https://www.example.com/orders/ord_77821/status");

OrderPlacedEvent orderPlacedEvent = new OrderPlacedEvent(
    /* orderId */ "ord_77821",
    /* currency */ "USD",
    /* source */ "android",
    /* totalValue */ 224.96,
    /* products */ Collections.singletonList(product),
    /* cartId */ "cart_abc123",
    /* totalDiscounts */ 10.0,
    /* discounts */ null,
    /* metadata */ metadata
);

Braze.getInstance(context).logEcommerceEvent(orderPlacedEvent);
```

{% endsubtab %}
{% subtab order_cancelled %}

Braze no proporciona una clase tipada del SDK para este evento. Usa `logCustomEvent` con una carga útil que coincida con el esquema del evento `ecommerce.order_cancelled`.

```java
import com.braze.Braze;
import com.braze.models.outgoing.BrazeProperties;
import org.json.JSONArray;
import org.json.JSONObject;

Braze.getInstance(context).logCustomEvent(
    "ecommerce.order_cancelled",
    new BrazeProperties(new JSONObject()
        .put("order_id", "ord_77821")
        .put("total_value", 224.96)
        .put("currency", "USD")
        .put("cancel_reason", "customer_request")
        .put("source", "android")
        .put("products", new JSONArray()
            .put(new JSONObject()
                .put("product_id", "SKU-RUN-4821")
                .put("product_name", "Ultraboost Running Shoe")
                .put("variant_id", "UB-BLK-11")
                .put("quantity", 1)
                .put("price", 189.99)))));
```

{% endsubtab %}
{% subtab order_refunded %}

Braze no proporciona una clase tipada del SDK para este evento. Usa `logCustomEvent` con una carga útil que coincida con el esquema del evento `ecommerce.order_refunded`.

```java
import com.braze.Braze;
import com.braze.models.outgoing.BrazeProperties;
import org.json.JSONArray;
import org.json.JSONObject;

Braze.getInstance(context).logCustomEvent(
    "ecommerce.order_refunded",
    new BrazeProperties(new JSONObject()
        .put("order_id", "ord_77821")
        .put("total_value", 189.99)
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

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## Registro manual con `logCustomEvent` {#manual-logging-with-logcustomevent}

Para registrar manualmente un evento recomendado, llama a `logCustomEvent` con el nombre exacto del evento (por ejemplo, `ecommerce.product_viewed`) y una carga útil `BrazeProperties` o `JSONObject` construida manualmente. El SDK no valida los esquemas de eventos recomendados en las llamadas manuales. Braze valida estas cargas útiles durante la ingesta:

- Las cargas útiles válidas se procesan como eventos recomendados con posprocesamiento completo.
- Las cargas útiles no válidas (campos obligatorios faltantes, tipos incorrectos, propiedades adicionales de nivel superior) se descartan después de la ingesta. Los fallos aparecen en el registro de procesamiento del SDK del espacio de trabajo y en el [correo electrónico de resumen de fallos]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#find-failures).

Usa `logEcommerceEvent` siempre que sea posible para detectar datos no válidos antes de que salgan de la aplicación. Para el uso general de `logCustomEvent`, consulta [Registrar eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android).