---
nav_title: E-Commerce-Events protokollieren
article_title: E-Commerce-Events über das Android SDK protokollieren
page_order: 3.25
description: "Erfahren Sie, wie Sie empfohlene E-Commerce-Events über das Braze Android SDK mithilfe typisierter Event-Klassen und logEcommerceEvent protokollieren."
platform:
  - Android
---

# E-Commerce-Events protokollieren {#log-ecommerce-events}

> Erfahren Sie, wie Sie [empfohlene E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/) über das Braze Android SDK mithilfe typisierter Event-Klassen und `Braze.logEcommerceEvent` protokollieren. Informationen zu Event-Eigenschaftsschemata, Plattform-Features und Ingestion-Validierung finden Sie unter [Empfohlene Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/) und [Event-Validierung und Fehlerbehebung]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-validation-and-troubleshooting).

{% alert note %}
Verwenden Sie für Wrapper-SDKs, die hier nicht aufgeführt sind, stattdessen die entsprechende native Android-Methode.
{% endalert %}

Ab Android SDK [42.3.0+](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.3.0) stehen typisierte E-Commerce-Event-Klassen mit clientseitiger Validierung zur Konstruktionszeit und automatischer `snake_case`-Serialisierung beim Aufruf von `Braze.logEcommerceEvent` zur Verfügung.

| Android-Klasse | Event-Name | Hinweise |
| ------------- | ---------- | ----- |
| `ProductViewedEvent` | `ecommerce.product_viewed` | Flacht Produktfelder auf die oberste Ebene von `properties` ab (kein `products`-Array). Diese Klasse unterstützt nicht die `type`-Eigenschaft auf oberster Ebene für Katalog-Trigger. Wenn Sie `type` benötigen, verwenden Sie [`logCustomEvent`](#manual-logging-with-logcustomevent) oder die REST API. |
| `CartUpdatedEvent` | `ecommerce.cart_updated` | Verwenden Sie `CartUpdatedAction` (`ADD`, `REMOVE`, `REPLACE`) für die `action`-Eigenschaft. |
| `CheckoutStartedEvent` | `ecommerce.checkout_started` | |
| `OrderPlacedEvent` | `ecommerce.order_placed` | Unterstützt optionale `cartId`, `totalDiscounts` und `discounts`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android SDK eCommerce event classes" }

{% alert important %}
`ecommerce.order_cancelled` und `ecommerce.order_refunded` sind nicht als typisierte Android-SDK-Klassen verfügbar. Protokollieren Sie diese mit [`logCustomEvent`](#manual-logging-with-logcustomevent) oder der REST API.
{% endalert %}

## Gemeinsame Bausteine {#shared-building-blocks}

- `EcommerceProduct`: Einzelposten für Warenkorb-, Checkout- und Bestell-Events.
  - Erforderlich: `productId`, `productName`, `variantId`, `price`, `quantity` (nicht-negativer `Long`)
  - Optional: `imageUrl`, `productUrl`, `metadata`
- `BrazeProperties`: `metadata` auf Event- oder Produktebene. Schlüssel müssen nicht-leere Strings mit höchstens 255 Zeichen ohne führendes Dollarzeichen ($) sein.

## Clientseitige Validierung {#client-side-validation}

Ungültige Payloads lösen beim Konstruieren der Event-Klasse eine `IllegalArgumentException` aus, sodass das Event nie in die Warteschlange gestellt wird. Allgemeine Regeln:

| Feld oder Regel | Validierung |
| ------------ | ---------- |
| String-IDs und -Namen (`product_id`, `product_name`, `variant_id`, `cart_id`, `checkout_id`, `order_id`, `source`, optionale URLs) | Nicht leer, bis zu 255 Zeichen |
| `price`, `total_value`, `total_discounts` | Muss größer oder gleich `0` sein |
| `currency` | Gültiger ISO-4217-Code (vom SDK getrimmt und in Großbuchstaben konvertiert) |
| `products` (Warenkorb-, Checkout-, Bestell-Events) | Mindestens ein `EcommerceProduct` |
| `quantity` (pro Produkt) | Nicht-negative Ganzzahl |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Android client-side validation rules for eCommerce events" }

Wenn die serialisierten Eigenschaften zum Versandzeitpunkt das SDK-Größenlimit überschreiten, protokolliert `logEcommerceEvent` einen Fehler und sendet das Event nicht.

## Code-Beispiele {#code-examples}

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

Legen Sie `action` mit `CartUpdatedAction` fest:

| Wert | Wire-Wert | Beschreibung |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | Menge erhöhen oder eine Position hinzufügen. |
| `CartUpdatedAction.REMOVE` | `remove` | Menge verringern; Position bei `0` entfernen. |
| `CartUpdatedAction.REPLACE` | `replace` | Den gesamten Warenkorb ersetzen (Standard). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CartUpdatedAction values for ecommerce.cart_updated" }

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

Braze stellt für dieses Event keine typisierte SDK-Klasse bereit. Verwenden Sie `logCustomEvent` mit einem Payload, der dem `ecommerce.order_cancelled`-Event-Schema entspricht.

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

Braze stellt für dieses Event keine typisierte SDK-Klasse bereit. Verwenden Sie `logCustomEvent` mit einem Payload, der dem `ecommerce.order_refunded`-Event-Schema entspricht.

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

Legen Sie `action` mit `CartUpdatedAction` fest:

| Wert | Wire-Wert | Beschreibung |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | Menge erhöhen oder eine Position hinzufügen. |
| `CartUpdatedAction.REMOVE` | `remove` | Menge verringern; Position bei `0` entfernen. |
| `CartUpdatedAction.REPLACE` | `replace` | Den gesamten Warenkorb ersetzen (Standard). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CartUpdatedAction values for ecommerce.cart_updated" }

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

Braze stellt für dieses Event keine typisierte SDK-Klasse bereit. Verwenden Sie `logCustomEvent` mit einem Payload, der dem `ecommerce.order_cancelled`-Event-Schema entspricht.

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

Braze stellt für dieses Event keine typisierte SDK-Klasse bereit. Verwenden Sie `logCustomEvent` mit einem Payload, der dem `ecommerce.order_refunded`-Event-Schema entspricht.

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

## Manuelles Protokollieren mit `logCustomEvent` {#manual-logging-with-logcustomevent}

Um ein empfohlenes Event manuell zu protokollieren, rufen Sie `logCustomEvent` mit dem exakten Event-Namen (zum Beispiel `ecommerce.product_viewed`) und einem manuell erstellten `BrazeProperties`- oder `JSONObject`-Payload auf. Das SDK validiert keine Schemata empfohlener Events bei manuellen Aufrufen. Braze validiert diese Payloads während der Ingestion:

- Gültige Payloads werden als empfohlene Events mit vollständiger Nachverarbeitung verarbeitet.
- Ungültige Payloads (fehlende Pflichtfelder, falsche Typen, zusätzliche Eigenschaften auf oberster Ebene) werden nach der Ingestion verworfen. Fehler erscheinen im SDK-Verarbeitungsprotokoll des Workspace und in der [Fehlerübersichts-E-Mail]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#find-failures).

Verwenden Sie nach Möglichkeit `logEcommerceEvent`, damit Sie ungültige Daten erkennen, bevor sie die App verlassen. Informationen zur allgemeinen Verwendung von `logCustomEvent` finden Sie unter [Angepasste Events protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android).