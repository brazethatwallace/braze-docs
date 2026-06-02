---
nav_title: Log eCommerce events
article_title: Log eCommerce events through the Android SDK
page_order: 3.25
description: "Learn how to log eCommerce recommended events through the Braze Android SDK using typed event classes and logEcommerceEvent."
platform:
  - Android
---

# Log eCommerce events

> Learn how to log [eCommerce recommended events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/) through the Braze Android SDK using typed event classes and `Braze.logEcommerceEvent`. For event property schemas, platform features, and ingestion validation, see [Recommended events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/) and [Event validation and troubleshooting]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-validation-and-troubleshooting).

{% alert note %}
For wrapper SDKs not listed, use the relevant native Android method instead.
{% endalert %}

Android SDK [42.3.0+](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.3.0) provides typed eCommerce event classes with client-side validation at construction time and automatic `snake_case` serialization when you call `Braze.logEcommerceEvent`.

| Android class | Event name | Notes |
| ------------- | ---------- | ----- |
| `ProductViewedEvent` | `ecommerce.product_viewed` | Flattens product fields to the top level of `properties` (no `products` array). This class does not support the top-level `type` property for catalog triggers. If you need `type`, use [`logCustomEvent`](#manual-logging-with-logcustomevent) or the REST API. |
| `CartUpdatedEvent` | `ecommerce.cart_updated` | Use `CartUpdatedAction` (`ADD`, `REMOVE`, `REPLACE`) for the `action` property. |
| `CheckoutStartedEvent` | `ecommerce.checkout_started` | |
| `OrderPlacedEvent` | `ecommerce.order_placed` | Supports optional `cartId`, `totalDiscounts`, and `discounts`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android SDK eCommerce event classes" }

{% alert important %}
`ecommerce.order_cancelled` and `ecommerce.order_refunded` are not available as typed Android SDK classes. Log them with [`logCustomEvent`](#manual-logging-with-logcustomevent) or the REST API.
{% endalert %}

## Shared building blocks

- `EcommerceProduct`: Line items for cart, checkout, and order events. 
  - Required: `productId`, `productName`, `variantId`, `price`, `quantity` (non-negative `Long`)
  - Optional: `imageUrl`, `productUrl`, `metadata`
- `BrazeProperties`: Event-level or product-level `metadata`. Keys must be non-empty strings that are at least 255 characters with no leading dollar sign ($).

## Client-side validation {#client-side-validation}

Invalid payloads throw `IllegalArgumentException` when you construct the event class, so the event is never queued. Common rules:

| Field or rule | Validation |
| ------------ | ---------- |
| String IDs and names (`product_id`, `product_name`, `variant_id`, `cart_id`, `checkout_id`, `order_id`, `source`, optional URLs) | Non-blank, up to 255 characters |
| `price`, `total_value`, `total_discounts` | Must be greater than or equal to `0` |
| `currency` | Valid ISO 4217 code (trimmed and converted to uppercase by the SDK) |
| `products` (cart, checkout, order events) | At least one `EcommerceProduct` |
| `quantity` (per product) | Non-negative integer |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Android client-side validation rules for eCommerce events" }

At dispatch time, if serialized properties exceed the SDK size limit, `logEcommerceEvent` logs an error and does not send the event.

## Code examples

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

Set `action` using `CartUpdatedAction`:

| Value | Wire value | Description |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | Increase quantity or add a line. |
| `CartUpdatedAction.REMOVE` | `remove` | Decrease quantity; remove the line at `0`. |
| `CartUpdatedAction.REPLACE` | `replace` | Replace the full cart (default). |
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

Braze does not provide a typed SDK class for this event. Use `logCustomEvent` with a payload that matches the `ecommerce.order_cancelled` event schema.

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

Braze does not provide a typed SDK class for this event. Use `logCustomEvent` with a payload that matches the `ecommerce.order_refunded` event schema.

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

Set `action` using `CartUpdatedAction`:

| Value | Wire value | Description |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | Increase quantity or add a line. |
| `CartUpdatedAction.REMOVE` | `remove` | Decrease quantity; remove the line at `0`. |
| `CartUpdatedAction.REPLACE` | `replace` | Replace the full cart (default). |
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

Braze does not provide a typed SDK class for this event. Use `logCustomEvent` with a payload that matches the `ecommerce.order_cancelled` event schema.

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

Braze does not provide a typed SDK class for this event. Use `logCustomEvent` with a payload that matches the `ecommerce.order_refunded` event schema.

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

## Manual logging with `logCustomEvent` {#manual-logging-with-logcustomevent}

To manually log a recommended event, call `logCustomEvent` with the exact event name (for example, `ecommerce.product_viewed`) and a manually built `BrazeProperties` or `JSONObject` payload. The SDK does not validate recommended-event schemas for manual calls. Braze validates these payloads during ingestion:

- Valid payloads are processed as recommended events with full post-processing.
- Invalid payloads (missing required fields, wrong types, extra top-level properties) are dropped after ingestion. Failures appear in the workspace SDK processing log and the [failure summary email]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#find-failures).

Use `logEcommerceEvent` when possible so you catch invalid data before it leaves the app. For general `logCustomEvent` usage, see [Log custom events]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android).
