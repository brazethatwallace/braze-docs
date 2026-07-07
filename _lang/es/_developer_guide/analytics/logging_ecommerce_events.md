---
nav_title: Registrar eventos de comercio electrónico
article_title: Registrar eventos de comercio electrónico a través del SDK de Braze
page_order: 3.25
description: "Aprende a registrar eventos recomendados de comercio electrónico a través de los SDK de Android, Swift y Web de Braze usando clases de eventos tipadas y logEcommerceEvent."
platform:
  - Android
  - Swift
  - Web
---

# Registrar eventos de comercio electrónico {#log-ecommerce-events}

> Aprende a registrar [eventos recomendados de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) a través de los SDK de Android, Swift y Web de Braze usando clases de eventos tipadas y `logEcommerceEvent`. Para esquemas de propiedades de eventos, características de la plataforma y validación de ingesta, consulta [Eventos recomendados]({{site.baseurl}}/user_guide/data/activation/events/recommended_events) y [Validación de eventos y solución de problemas]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-validation-and-troubleshooting).

{% alert note %}
Para los SDK envolventes no incluidos en la lista, usa el método nativo de Android o Swift correspondiente en su lugar.
{% endalert %}

## Esquemas de eventos {#event-schemas}

Los seis eventos recomendados de comercio electrónico comparten un esquema a nivel de pedido en todas las plataformas. Usa las siguientes tablas de propiedades cuando construyas la carga útil de cada evento. Para el esquema canónico con el comportamiento de validación completo y ejemplos de REST API, consulta [Eventos recomendados]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas). Para características de la plataforma como segmentación, plantillas de Canvas e informes, consulta [Cómo usar eventos de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events).

{% tabs local %}
{% tab product_viewed %}

Se desencadena cuando un usuario ve una página de detalle de producto.

**Propiedades del evento**

| Nombre de la propiedad | Tipo de datos | Obligatoria | Descripción |
| ------------- | --------- | -------- | ----------- |
| `product_id` | Cadena | Sí | Identificador único del producto (por ejemplo, SKU o ID de artículo). |
| `product_name` | Cadena | Sí | Nombre de visualización del producto. |
| `variant_id` | Cadena | Sí | Identificador de la variante del producto (por ejemplo, `shirt_medium_blue`). |
| `image_url` | Cadena | No | URL de la imagen del producto. |
| `product_url` | Cadena | No | URL de la página del producto para más detalles. |
| `price` | Número flotante | Sí | Precio unitario de la variante en el momento de la visualización. |
| `currency` | Cadena | Sí | Código ISO 4217 de tres letras (por ejemplo, `USD` o `EUR`). |
| `source` | Cadena | Sí | Fuente de la que se origina el evento (por ejemplo, `web`, `ios` o `android`). |
| `type` | Matriz de cadenas | No | Obligatoria para usar las características de desencadenadores de catálogo de Braze para alertas de vuelta en stock y bajada de precio. Valores aceptados: `"price_drop"`, `"back_in_stock"`. |
| `metadata` | Objeto | No | Pares clave-valor flexibles. Subpropiedad reconocida: `sku` (cadena). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades del evento de producto visualizado" }

{% endtab %}
{% tab cart_updated %}

Se desencadena cada vez que cambia el contenido del carrito de un usuario. Usa el reemplazo completo del carrito (omite `action` o establécelo en `replace`) o actualizaciones incrementales (`add` o `remove`).

**Propiedades del evento**

| Propiedad | Tipo de datos | Obligatoria | Descripción |
| -------- | --------- | -------- | ----------- |
| `cart_id` | Cadena | Sí | Identificador único del carrito. Se comparte entre los eventos de carrito, pago y pedido para el mapeado del carrito del usuario. |
| `action` | Cadena | No | `add` (incrementar cantidad o agregar una línea), `remove` (decrementar cantidad; la línea se elimina en `0`) o `replace` (reemplazo completo del carrito, igual que omitir `action`). |
| `total_value` | Número flotante | Condicional | Obligatoria cuando se omite `action` o es `replace`. Opcional cuando `action` es `add` o `remove`. |
| `subtotal_value` | Número flotante | No | Valor del subtotal del carrito (después de descuentos, antes de impuestos/envío). |
| `tax` | Número flotante | No | Impuesto total aplicado al carrito. |
| `shipping` | Número flotante | No | Costo total de envío del carrito. |
| `currency` | Cadena | Sí | Código ISO 4217 de tres letras. |
| `products` | Array | Sí | Elementos de línea para esta actualización. Consulta la tabla de propiedades de producto. |
| `source` | Cadena | Sí | Fuente de la que se origina el evento. |
| `metadata` | Objeto | No | Pares clave-valor flexibles para datos adicionales a nivel de evento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades del evento de carrito actualizado" }

**Propiedades de producto (`products[]`)**

| Propiedad | Tipo de datos | Obligatoria | Descripción |
| -------- | --------- | -------- | ----------- |
| `product_id` | Cadena | Sí | Identificador único del producto. |
| `product_name` | Cadena | Sí | Nombre de visualización del producto. |
| `variant_id` | Cadena | Sí | Identificador de la variante. |
| `image_url` | Cadena | No | URL de la imagen del producto. |
| `product_url` | Cadena | No | URL de la página del producto. |
| `quantity` | Entero | Sí | Para reemplazo completo, unidades en el carrito para esta línea. Para `add` o `remove`, cuántas unidades agregar o quitar. |
| `price` | Número flotante | Sí | Precio unitario de la variante. |
| `metadata` | Objeto | No | Pares clave-valor flexibles (por ejemplo, `color` o `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades de producto del evento de carrito actualizado" }

{% endtab %}
{% tab checkout_started %}

Se desencadena cuando el usuario inicia el flujo de pago.

**Propiedades del evento**

| Propiedad | Tipo de datos | Obligatoria | Descripción |
| -------- | --------- | -------- | ----------- |
| `checkout_id` | Cadena | Sí | Identificador único de la sesión de pago. |
| `cart_id` | Cadena | No | Identificador del carrito. Se comparte entre los eventos de carrito, pago y pedido para el mapeado del carrito del usuario. |
| `total_value` | Número flotante | Sí | Valor monetario total del pago. |
| `subtotal_value` | Número flotante | No | Valor del subtotal (después de descuentos, antes de impuestos/envío). |
| `tax` | Número flotante | No | Impuesto total aplicado al pago. |
| `shipping` | Número flotante | No | Costo total de envío. |
| `currency` | Cadena | Sí | Código ISO 4217 de tres letras. |
| `products` | Array | Sí | Artículos en proceso de pago. Consulta la tabla de propiedades de producto. |
| `source` | Cadena | Sí | Fuente de la que se origina el evento. |
| `metadata` | Objeto | No | Pares clave-valor flexibles. Subpropiedad reconocida: `checkout_url` (cadena). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades del evento de pago iniciado" }

**Propiedades de producto (`products[]`)**

| Propiedad | Tipo de datos | Obligatoria | Descripción |
| -------- | --------- | -------- | ----------- |
| `product_id` | Cadena | Sí | Identificador único del producto. |
| `product_name` | Cadena | Sí | Nombre de visualización del producto. |
| `variant_id` | Cadena | Sí | Identificador de la variante. |
| `image_url` | Cadena | No | URL de la imagen del producto. |
| `product_url` | Cadena | No | URL de la página del producto. |
| `quantity` | Entero | Sí | Número de unidades en el carrito. |
| `price` | Número flotante | Sí | Precio unitario de la variante. |
| `metadata` | Objeto | No | Pares clave-valor flexibles (por ejemplo, `color` o `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades de producto del evento de pago iniciado" }

{% endtab %}
{% tab order_placed %}

Se desencadena cuando un pedido se completa correctamente o se confirma el pago.

**Propiedades del evento**

| Propiedad | Tipo de datos | Obligatoria | Descripción |
| -------- | --------- | -------- | ----------- |
| `order_id` | Cadena | Sí | Identificador único del pedido. |
| `cart_id` | Cadena | No | Identificador del carrito. Se comparte entre los eventos de carrito, pago y pedido para el mapeado del carrito del usuario. |
| `total_value` | Número flotante | Sí | Valor monetario total del pedido. |
| `subtotal_value` | Número flotante | No | Valor del subtotal (después de descuentos, antes de impuestos/envío). |
| `tax` | Número flotante | No | Impuesto total aplicado al pedido. |
| `shipping` | Número flotante | No | Costo total de envío. |
| `currency` | Cadena | Sí | Código ISO 4217 de tres letras. |
| `total_discounts` | Número flotante | No | Monto total de descuentos aplicados al pedido. |
| `discounts` | Array | No | Lista detallada de descuentos aplicados. Cada objeto de descuento admite `code` (cadena), `amount` (número flotante) y `type` (cadena). |
| `products` | Array | Sí | Artículos en el pedido. Consulta la tabla de propiedades de producto. |
| `source` | Cadena | Sí | Fuente de la que se origina el evento. |
| `metadata` | Objeto | No | Pares clave-valor flexibles. Subpropiedad reconocida: `order_status_url` (cadena). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades del evento de pedido realizado" }

**Propiedades de producto (`products[]`)**

| Propiedad | Tipo de datos | Obligatoria | Descripción |
| -------- | --------- | -------- | ----------- |
| `product_id` | Cadena | Sí | Identificador único del producto. |
| `product_name` | Cadena | Sí | Nombre de visualización del producto. |
| `variant_id` | Cadena | Sí | Identificador de la variante. |
| `image_url` | Cadena | No | URL de la imagen del producto. |
| `product_url` | Cadena | No | URL de la página del producto. |
| `quantity` | Entero | Sí | Número de unidades en el pedido. |
| `price` | Número flotante | Sí | Precio unitario de la variante. |
| `metadata` | Objeto | No | Pares clave-valor flexibles (por ejemplo, `color` o `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades de producto del evento de pedido realizado" }

{% endtab %}
{% tab order_cancelled %}

Se desencadena cuando se cancela un pedido.

**Propiedades del evento**

| Propiedad | Tipo de datos | Obligatoria | Descripción |
| -------- | --------- | -------- | ----------- |
| `order_id` | Cadena | Sí | Identificador único del pedido. |
| `total_value` | Número flotante | Sí | Valor monetario total del pedido que se cancela. Envía el monto absoluto (mayor o igual a `0`); Braze se encarga del decremento. |
| `subtotal_value` | Número flotante | No | Valor del subtotal (después de descuentos, antes de impuestos/envío). |
| `tax` | Número flotante | No | Impuesto total aplicado al pedido. |
| `shipping` | Número flotante | No | Costo total de envío. |
| `currency` | Cadena | Sí | Código ISO 4217 de tres letras. |
| `total_discounts` | Número flotante | No | Monto total de descuentos aplicados al pedido. |
| `discounts` | Array | No | Lista detallada de descuentos aplicados. |
| `cancel_reason` | Cadena | Sí | Motivo por el que se canceló el pedido. |
| `products` | Array | Sí | Artículos en el pedido cancelado. Consulta la tabla de propiedades de producto. |
| `source` | Cadena | Sí | Fuente de la que se origina el evento. |
| `metadata` | Objeto | No | Pares clave-valor flexibles. Subpropiedad reconocida: `order_status_url` (cadena). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades del evento de pedido cancelado" }

**Propiedades de producto (`products[]`)**

| Propiedad | Tipo de datos | Obligatoria | Descripción |
| -------- | --------- | -------- | ----------- |
| `product_id` | Cadena | Sí | Identificador único del producto. |
| `product_name` | Cadena | Sí | Nombre de visualización del producto. |
| `variant_id` | Cadena | Sí | Identificador de la variante. |
| `image_url` | Cadena | No | URL de la imagen del producto. |
| `product_url` | Cadena | No | URL de la página del producto. |
| `quantity` | Entero | Sí | Número de unidades en el pedido. |
| `price` | Número flotante | Sí | Precio unitario de la variante. |
| `metadata` | Objeto | No | Pares clave-valor flexibles (por ejemplo, `color` o `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades de producto del evento de pedido cancelado" }

{% endtab %}
{% tab order_refunded %}

Se desencadena cuando se emite un reembolso total o parcial. Para reembolsos parciales, establece `total_value` solo con el monto reembolsado, no con el total original del pedido.

**Propiedades del evento**

| Propiedad | Tipo de datos | Obligatoria | Descripción |
| -------- | --------- | -------- | ----------- |
| `order_id` | Cadena | Sí | Identificador único del pedido original. |
| `total_value` | Número flotante | Sí | Valor monetario total del reembolso. Envía el monto absoluto (mayor o igual a `0`); Braze se encarga del ajuste de ingresos. |
| `currency` | Cadena | Sí | Código ISO 4217 de tres letras. |
| `total_discounts` | Número flotante | No | Monto total de descuentos aplicados originalmente. |
| `discounts` | Array | No | Lista detallada de descuentos. |
| `products` | Array | Sí | Artículos que se reembolsan. Consulta la tabla de propiedades de producto. |
| `source` | Cadena | Sí | Fuente de la que se origina el evento. |
| `metadata` | Objeto | No | Pares clave-valor flexibles. Subpropiedad reconocida: `order_status_url` (cadena). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades del evento de pedido reembolsado" }

**Propiedades de producto (`products[]`)**

| Propiedad | Tipo de datos | Obligatoria | Descripción |
| -------- | --------- | -------- | ----------- |
| `product_id` | Cadena | Sí | Identificador único del producto. |
| `product_name` | Cadena | Sí | Nombre de visualización del producto. |
| `variant_id` | Cadena | Sí | Identificador de la variante. |
| `image_url` | Cadena | No | URL de la imagen del producto. |
| `product_url` | Cadena | No | URL de la página del producto. |
| `quantity` | Entero | Sí | Número de unidades reembolsadas. |
| `price` | Número flotante | Sí | Precio unitario de la variante. |
| `metadata` | Objeto | No | Pares clave-valor flexibles (por ejemplo, `color` o `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Propiedades de producto del evento de pedido reembolsado" }

{% endtab %}
{% endtabs %}

## Android

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

### Bloques de construcción compartidos {#shared-building-blocks}

- `EcommerceProduct`: elementos de línea para eventos de carrito, pago y pedido.
  - Obligatorios: `productId`, `productName`, `variantId`, `price`, `quantity` (`Long` no negativo)
  - Opcionales: `imageUrl`, `productUrl`, `metadata`
- `BrazeProperties`: `metadata` a nivel de evento o de producto. Las claves deben ser cadenas no vacías de hasta 255 caracteres sin signo de dólar ($) inicial.

### Validación del lado del cliente {#client-side-validation}

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

### Ejemplos de código {#code-examples}

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

## iOS

El SDK de Swift proporciona clases de eventos de comercio electrónico tipadas —`ProductViewedEvent`, `CartUpdatedEvent`, `CheckoutStartedEvent` y `OrderPlacedEvent`— que construyes y pasas a `logEcommerceEvent`. Usa `ProductLineItem` para los productos en eventos de carrito, pago y pedido. Cada inicializador puede lanzar una excepción, así que envuélvelo en `try?` y registra el evento solo cuando la construcción sea exitosa.
Esto está disponible en la versión `15.0.0` del SDK de Swift y posteriores.

`ecommerce.order_cancelled` y `ecommerce.order_refunded` no están disponibles como clases tipadas del SDK de Swift. Regístralos con `logCustomEvent`.

### Ejemplos de código

{% tabs local %}
{% tab product_viewed %}

```swift
if let productViewedEvent = try? Braze.Ecommerce.ProductViewedEvent(
    productId: "4111176",
    productName: "Torchie runners",
    variantId: "4111176700",
    imageUrl: "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    productUrl: "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    price: 85,
    currency: "GBP",
    source: "https://braze-apparel.com/",
    metadata: [
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    ],
    typeIdentifiers: ["price_drop", "back_in_stock"]
) {
    AppDelegate.braze?.logEcommerceEvent(productViewedEvent)
}
```

{% endtab %}
{% tab cart_updated %}

```swift
if let productLine = try? Braze.Ecommerce.ProductLineItem(
    productId: "8266836345064",
    productName: "Classic T-Shirt",
    variantId: "44610569208040",
    imageUrl: "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
    productUrl: "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
    quantity: 2,
    price: 99.99,
    metadata: [
        "sku": "TSH-BLU-M",
        "color": "BLUE",
        "size": "Medium",
        "brand": "Braze"
    ]
), let cartUpdatedEvent = try? Braze.Ecommerce.CartUpdatedEvent(
    cartId: "cart_12345",
    totalValue: 199.98,
    currency: "USD",
    products: [productLine],
    source: "https://braze-apparel.com",
    metadata: [:]
) {
    AppDelegate.braze?.logEcommerceEvent(cartUpdatedEvent)
}
```

{% endtab %}
{% tab checkout_started %}

```swift
if let productLine = try? Braze.Ecommerce.ProductLineItem(
    productId: "632910392",
    productName: "Wireless Headphones",
    variantId: "808950810",
    quantity: 1,
    price: 199.98,
    metadata: [
        "sku": "WH-BLK-PRO",
        "color": "Black",
        "brand": "BrazeAudio"
    ]
), let checkoutStartedEvent = try? Braze.Ecommerce.CheckoutStartedEvent(
    checkoutId: "checkout_abc123",
    cartId: "cart_12345",
    totalValue: 199.98,
    currency: "USD",
    products: [productLine],
    source: "https://braze-audio.com",
    metadata: [
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    ]
) {
    AppDelegate.braze?.logEcommerceEvent(checkoutStartedEvent)
}
```

{% endtab %}
{% tab order_placed %}

```swift
if let productLine = try? Braze.Ecommerce.ProductLineItem(
    productId: "632910392",
    productName: "Wireless Headphones",
    variantId: "808950810",
    quantity: 1,
    price: 199.98,
    metadata: [
        "sku": "WH-BLK-PRO",
        "color": "Black",
        "brand": "BrazeAudio"
    ]
), let orderPlacedEvent = try? Braze.Ecommerce.OrderPlacedEvent(
    orderId: "order_67890",
    cartId: "cart_12345",
    totalValue: 189.98,
    currency: "USD",
    totalDiscounts: 10.00,
    discounts: [.structured(code: "SAVE10", amount: 10.00, type: "fixed")],
    products: [productLine],
    source: "https://braze-audio.com",
    metadata: [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    ]
) {
    AppDelegate.braze?.logEcommerceEvent(orderPlacedEvent)
}
```

{% endtab %}
{% tab order_cancelled %}

Braze no proporciona una clase tipada del SDK para este evento. Usa `logCustomEvent` con una carga útil que coincida con el esquema del evento `ecommerce.order_cancelled`.

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

{% endtab %}
{% tab order_refunded %}

Braze no proporciona una clase tipada del SDK para este evento. Usa `logCustomEvent` con una carga útil que coincida con el esquema del evento `ecommerce.order_refunded`.

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

{% endtab %}
{% endtabs %}

## Web

En el SDK Web [6.8.0+](https://github.com/braze-inc/braze-web-sdk), llama a `logEcommerceEvent` con un `name` de evento y `properties`. En versiones anteriores del SDK, llama a `logCustomEvent` con el nombre del evento y un objeto de propiedades. `ecommerce.order_cancelled` y `ecommerce.order_refunded` usan `logCustomEvent`.

### Ejemplos de código

{% tabs local %}
{% tab product_viewed %}

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

{% endtab %}
{% tab cart_updated %}

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

{% endtab %}
{% tab checkout_started %}

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

{% endtab %}
{% tab order_placed %}

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

{% endtab %}
{% tab order_cancelled %}

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

{% endtab %}
{% tab order_refunded %}

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

{% endtab %}
{% endtabs %}

## Registro manual con `logCustomEvent` {#manual-logging-with-logcustomevent}

Para registrar manualmente un evento recomendado, llama a `logCustomEvent` con el nombre exacto del evento (por ejemplo, `ecommerce.product_viewed`) y una carga útil `BrazeProperties` o `JSONObject` construida manualmente. El SDK no valida los esquemas de eventos recomendados en las llamadas manuales. Braze valida estas cargas útiles durante la ingesta:

- Las cargas útiles válidas se procesan como eventos recomendados con posprocesamiento completo.
- Las cargas útiles no válidas (campos obligatorios faltantes, tipos incorrectos, propiedades adicionales de nivel superior) se descartan después de la ingesta. Los fallos aparecen en el registro de procesamiento del SDK del espacio de trabajo y en el [correo electrónico de resumen de fallos]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#find-failures).

Usa `logEcommerceEvent` siempre que sea posible para detectar datos no válidos antes de que salgan de la aplicación. Para el uso general de `logCustomEvent`, consulta [Registrar eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android).