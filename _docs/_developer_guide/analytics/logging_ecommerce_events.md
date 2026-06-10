---
nav_title: Log eCommerce events
article_title: Log eCommerce events through the Braze SDK
page_order: 3.25
description: "Learn how to log eCommerce recommended events through the Braze Android, Swift, and Web SDKs using typed event classes and logEcommerceEvent."
platform:
  - Android
  - Swift
  - Web
---

# Log eCommerce events

> Learn how to log [eCommerce recommended events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/) through the Braze Android, Swift, and Web SDKs using typed event classes and `logEcommerceEvent`. For event property schemas, platform features, and ingestion validation, see [Recommended events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/) and [Event validation and troubleshooting]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-validation-and-troubleshooting).

{% alert note %}
For wrapper SDKs not listed, use the relevant native Android or Swift method instead.
{% endalert %}

## Event schemas

The six eCommerce recommended events share an order-level schema across all platforms. Use the following property tables when you build each event payload. For the canonical schema with full validation behavior and REST API examples, see [Recommended events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-schemas). For platform features such as segmentation, Canvas templates, and reporting, see [How to use eCommerce events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/).

{% tabs local %}
{% tab product_viewed %}

Trigger when a user views a product detail page.

**Event properties**

| Property name | Data type | Required | Description |
| ------------- | --------- | -------- | ----------- |
| `product_id` | String | Yes | Unique product identifier (for example, SKU or item ID). |
| `product_name` | String | Yes | Product display name. |
| `variant_id` | String | Yes | Product variant identifier (for example, `shirt_medium_blue`). |
| `image_url` | String | No | Product image URL. |
| `product_url` | String | No | URL to the product page for more details. |
| `price` | Float | Yes | Variant unit price at the time of viewing. |
| `currency` | String | Yes | Three-letter ISO 4217 code (for example, `USD` or `EUR`). |
| `source` | String | Yes | Source the event originates from (for example, `web`, `ios`, or `android`). |
| `type` | Array of strings | No | Required to use Braze catalog trigger features for back-in-stock and price-drop alerts. Accepted values: `"price_drop"`, `"back_in_stock"`. |
| `metadata` | Object | No | Flexible key-value pairs. Recognized sub-property: `sku` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Product viewed event properties" }

{% endtab %}
{% tab cart_updated %}

Trigger every time the contents of a user's cart change. Use full cart replacement (omit `action` or set it to `replace`) or incremental updates (`add` or `remove`).

**Event properties**

| Property | Data type | Required | Description |
| -------- | --------- | -------- | ----------- |
| `cart_id` | String | Yes | Unique identifier for the cart. Shared across cart, checkout, and order events for the user's cart mapping. |
| `action` | String | No | `add` (increment quantity or add a line), `remove` (decrement quantity; line removed at `0`), or `replace` (full cart replacement, same as omitting `action`). |
| `total_value` | Float | Conditional | Required when `action` is omitted or `replace`. Optional when `action` is `add` or `remove`. |
| `subtotal_value` | Float | No | Subtotal value of the cart (post-discount, pre-tax/shipping). |
| `tax` | Float | No | Total tax applied to the cart. |
| `shipping` | Float | No | Total shipping cost for the cart. |
| `currency` | String | Yes | Three-letter ISO 4217 code. |
| `products` | Array | Yes | Line items for this update. See the product properties table. |
| `source` | String | Yes | Source the event originates from. |
| `metadata` | Object | No | Flexible key-value pairs for additional event-level data. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Cart updated event properties" }

**Product properties (`products[]`)**

| Property | Data type | Required | Description |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Yes | Unique product identifier. |
| `product_name` | String | Yes | Product display name. |
| `variant_id` | String | Yes | Variant identifier. |
| `image_url` | String | No | Product image URL. |
| `product_url` | String | No | URL to the product page. |
| `quantity` | Integer | Yes | For full replacement, units in the cart for this line. For `add` or `remove`, how many units to add or remove. |
| `price` | Float | Yes | Variant unit price. |
| `metadata` | Object | No | Flexible key-value pairs (for example, `color` or `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Cart updated product properties" }

{% endtab %}
{% tab checkout_started %}

Trigger when the user initiates the checkout flow.

**Event properties**

| Property | Data type | Required | Description |
| -------- | --------- | -------- | ----------- |
| `checkout_id` | String | Yes | Unique identifier for the checkout session. |
| `cart_id` | String | No | Cart identifier. Shared across cart, checkout, and order events for the user's cart mapping. |
| `total_value` | Float | Yes | Total monetary value of the checkout. |
| `subtotal_value` | Float | No | Subtotal value (post-discount, pre-tax/shipping). |
| `tax` | Float | No | Total tax applied to the checkout. |
| `shipping` | Float | No | Total shipping cost. |
| `currency` | String | Yes | Three-letter ISO 4217 code. |
| `products` | Array | Yes | Items being checked out. See the product properties table. |
| `source` | String | Yes | Source the event originates from. |
| `metadata` | Object | No | Flexible key-value pairs. Recognized sub-property: `checkout_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Checkout started event properties" }

**Product properties (`products[]`)**

| Property | Data type | Required | Description |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Yes | Unique product identifier. |
| `product_name` | String | Yes | Product display name. |
| `variant_id` | String | Yes | Variant identifier. |
| `image_url` | String | No | Product image URL. |
| `product_url` | String | No | URL to the product page. |
| `quantity` | Integer | Yes | Number of units in the cart. |
| `price` | Float | Yes | Variant unit price. |
| `metadata` | Object | No | Flexible key-value pairs (for example, `color` or `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Checkout started product properties" }

{% endtab %}
{% tab order_placed %}

Trigger when an order is successfully completed or payment is confirmed.

**Event properties**

| Property | Data type | Required | Description |
| -------- | --------- | -------- | ----------- |
| `order_id` | String | Yes | Unique identifier for the order. |
| `cart_id` | String | No | Cart identifier. Shared across cart, checkout, and order events for the user's cart mapping. |
| `total_value` | Float | Yes | Total monetary value of the order. |
| `subtotal_value` | Float | No | Subtotal value (post-discount, pre-tax/shipping). |
| `tax` | Float | No | Total tax applied to the order. |
| `shipping` | Float | No | Total shipping cost. |
| `currency` | String | Yes | Three-letter ISO 4217 code. |
| `total_discounts` | Float | No | Total amount of discounts applied to the order. |
| `discounts` | Array | No | Detailed list of discounts applied. Each discount object supports `code` (String), `amount` (Float), and `type` (String). |
| `products` | Array | Yes | Items in the order. See the product properties table. |
| `source` | String | Yes | Source the event originates from. |
| `metadata` | Object | No | Flexible key-value pairs. Recognized sub-property: `order_status_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Order placed event properties" }

**Product properties (`products[]`)**

| Property | Data type | Required | Description |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Yes | Unique product identifier. |
| `product_name` | String | Yes | Product display name. |
| `variant_id` | String | Yes | Variant identifier. |
| `image_url` | String | No | Product image URL. |
| `product_url` | String | No | URL to the product page. |
| `quantity` | Integer | Yes | Number of units in the order. |
| `price` | Float | Yes | Variant unit price. |
| `metadata` | Object | No | Flexible key-value pairs (for example, `color` or `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Order placed product properties" }

{% endtab %}
{% tab order_cancelled %}

Trigger when an order is cancelled.

**Event properties**

| Property | Data type | Required | Description |
| -------- | --------- | -------- | ----------- |
| `order_id` | String | Yes | Unique identifier for the order. |
| `total_value` | Float | Yes | Total monetary value of the order being cancelled. Send the absolute amount (greater than or equal to `0`); Braze handles the decrement. |
| `subtotal_value` | Float | No | Subtotal value (post-discount, pre-tax/shipping). |
| `tax` | Float | No | Total tax applied to the order. |
| `shipping` | Float | No | Total shipping cost. |
| `currency` | String | Yes | Three-letter ISO 4217 code. |
| `total_discounts` | Float | No | Total amount of discounts applied to the order. |
| `discounts` | Array | No | Detailed list of discounts applied. |
| `cancel_reason` | String | Yes | Reason the order was cancelled. |
| `products` | Array | Yes | Items in the cancelled order. See the product properties table. |
| `source` | String | Yes | Source the event originates from. |
| `metadata` | Object | No | Flexible key-value pairs. Recognized sub-property: `order_status_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Order cancelled event properties" }

**Product properties (`products[]`)**

| Property | Data type | Required | Description |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Yes | Unique product identifier. |
| `product_name` | String | Yes | Product display name. |
| `variant_id` | String | Yes | Variant identifier. |
| `image_url` | String | No | Product image URL. |
| `product_url` | String | No | URL to the product page. |
| `quantity` | Integer | Yes | Number of units in the order. |
| `price` | Float | Yes | Variant unit price. |
| `metadata` | Object | No | Flexible key-value pairs (for example, `color` or `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Order cancelled product properties" }

{% endtab %}
{% tab order_refunded %}

Trigger when a full or partial refund is issued. For partial refunds, set `total_value` to the refunded amount only, not the original order total.

**Event properties**

| Property | Data type | Required | Description |
| -------- | --------- | -------- | ----------- |
| `order_id` | String | Yes | Unique identifier for the original order. |
| `total_value` | Float | Yes | Total monetary value of the refund. Send the absolute amount (greater than or equal to `0`); Braze handles the revenue adjustment. |
| `currency` | String | Yes | Three-letter ISO 4217 code. |
| `total_discounts` | Float | No | Total amount of discounts originally applied. |
| `discounts` | Array | No | Detailed list of discounts. |
| `products` | Array | Yes | Items being refunded. See the product properties table. |
| `source` | String | Yes | Source the event originates from. |
| `metadata` | Object | No | Flexible key-value pairs. Recognized sub-property: `order_status_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Order refunded event properties" }

**Product properties (`products[]`)**

| Property | Data type | Required | Description |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Yes | Unique product identifier. |
| `product_name` | String | Yes | Product display name. |
| `variant_id` | String | Yes | Variant identifier. |
| `image_url` | String | No | Product image URL. |
| `product_url` | String | No | URL to the product page. |
| `quantity` | Integer | Yes | Number of units refunded. |
| `price` | Float | Yes | Variant unit price. |
| `metadata` | Object | No | Flexible key-value pairs (for example, `color` or `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Order refunded product properties" }

{% endtab %}
{% endtabs %}

## Android

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

### Shared building blocks

- `EcommerceProduct`: Line items for cart, checkout, and order events. 
  - Required: `productId`, `productName`, `variantId`, `price`, `quantity` (non-negative `Long`)
  - Optional: `imageUrl`, `productUrl`, `metadata`
- `BrazeProperties`: Event-level or product-level `metadata`. Keys must be non-empty strings that are at least 255 characters with no leading dollar sign ($).

### Client-side validation {#client-side-validation}

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

### Code examples

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

## iOS

The Swift SDK provides typed eCommerce event classes—`ProductViewedEvent`, `CartUpdatedEvent`, `CheckoutStartedEvent`, and `OrderPlacedEvent`—that you build and pass to `logEcommerceEvent`. Use `ProductLineItem` for the products in cart, checkout, and order events. Each initializer is throwing, so wrap it in `try?` and log the event only when construction succeeds.
This is available in Swift SDK version `15.0.0` and later.

`ecommerce.order_cancelled` and `ecommerce.order_refunded` are not available as typed Swift SDK classes. Log them with `logCustomEvent`.

### Code examples

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

Braze does not provide a typed SDK class for this event. Use `logCustomEvent` with a payload that matches the `ecommerce.order_cancelled` event schema.

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

Braze does not provide a typed SDK class for this event. Use `logCustomEvent` with a payload that matches the `ecommerce.order_refunded` event schema.

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

On Web SDK [6.8.0+](https://github.com/braze-inc/braze-web-sdk), call `logEcommerceEvent` with an event `name` and `properties`. On legacy SDK versions, call `logCustomEvent` with the event name and a properties object. `ecommerce.order_cancelled` and `ecommerce.order_refunded` use `logCustomEvent`.

### Code examples

{% tabs local %}
{% tab product_viewed %}

{% sdk_min_versions web:6.8.0 %}

On newer SDK versions, call `logEcommerceEvent()`:

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

On legacy SDK versions, call `logCustomEvent()`:

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

On newer SDK versions, call `logEcommerceEvent()`:

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

On legacy SDK versions, call `logCustomEvent()`:

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

On newer SDK versions, call `logEcommerceEvent()`:

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

On legacy SDK versions, call `logCustomEvent()`:

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

On newer SDK versions, call `logEcommerceEvent()`:

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

On legacy SDK versions, call `logCustomEvent()`:

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

## Manual logging with `logCustomEvent` {#manual-logging-with-logcustomevent}

To manually log a recommended event, call `logCustomEvent` with the exact event name (for example, `ecommerce.product_viewed`) and a manually built `BrazeProperties` or `JSONObject` payload. The SDK does not validate recommended-event schemas for manual calls. Braze validates these payloads during ingestion:

- Valid payloads are processed as recommended events with full post-processing.
- Invalid payloads (missing required fields, wrong types, extra top-level properties) are dropped after ingestion. Failures appear in the workspace SDK processing log and the [failure summary email]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#find-failures).

Use `logEcommerceEvent` when possible so you catch invalid data before it leaves the app. For general `logCustomEvent` usage, see [Log custom events]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android).
