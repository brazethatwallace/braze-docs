---
nav_title: eCommerce 이벤트 기록
article_title: Android SDK를 통한 eCommerce 이벤트 기록
page_order: 3.25
description: "타입이 지정된 이벤트 클래스와 logEcommerceEvent를 사용하여 Braze Android SDK를 통해 eCommerce 권장 이벤트를 기록하는 방법을 알아봅니다."
platform:
  - Android
---

# eCommerce 이벤트 기록 {#log-ecommerce-events}

> 타입이 지정된 이벤트 클래스와 `Braze.logEcommerceEvent`를 사용하여 Braze Android SDK를 통해 [eCommerce 권장 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/)를 기록하는 방법을 알아봅니다. 이벤트 속성정보 스키마, 플랫폼 기능 및 수집 유효성 검사에 대한 자세한 내용은 [권장 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/) 및 [이벤트 유효성 검사 및 문제 해결]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-validation-and-troubleshooting)을 참조하세요.

{% alert note %}
목록에 없는 래퍼 SDK의 경우, 관련 네이티브 Android 메서드를 대신 사용하세요.
{% endalert %}

Android SDK [42.3.0+](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.3.0)는 생성 시 클라이언트 측 유효성 검사와 `Braze.logEcommerceEvent` 호출 시 자동 `snake_case` 직렬화를 제공하는 타입이 지정된 eCommerce 이벤트 클래스를 제공합니다.

| Android 클래스 | 이벤트 이름 | 참고 |
| ------------- | ---------- | ----- |
| `ProductViewedEvent` | `ecommerce.product_viewed` | 제품 필드를 `properties`의 최상위 수준으로 평탄화합니다(`products` 배열 없음). 이 클래스는 카탈로그 트리거를 위한 최상위 `type` 등록정보를 지원하지 않습니다. `type`이 필요한 경우 [`logCustomEvent`](#manual-logging-with-logcustomevent) 또는 REST API를 사용하세요. |
| `CartUpdatedEvent` | `ecommerce.cart_updated` | `action` 등록정보에 `CartUpdatedAction`(`ADD`, `REMOVE`, `REPLACE`)을 사용합니다. |
| `CheckoutStartedEvent` | `ecommerce.checkout_started` | |
| `OrderPlacedEvent` | `ecommerce.order_placed` | 선택 사항인 `cartId`, `totalDiscounts`, `discounts`를 지원합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android SDK eCommerce event classes" }

{% alert important %}
`ecommerce.order_cancelled` 및 `ecommerce.order_refunded`는 타입이 지정된 Android SDK 클래스로 제공되지 않습니다. [`logCustomEvent`](#manual-logging-with-logcustomevent) 또는 REST API를 사용하여 기록하세요.
{% endalert %}

## 공유 빌딩 블록 {#shared-building-blocks}

- `EcommerceProduct`: 장바구니, 결제 및 주문 이벤트의 라인 항목입니다.
  - 필수: `productId`, `productName`, `variantId`, `price`, `quantity`(음수가 아닌 `Long`)
  - 선택 사항: `imageUrl`, `productUrl`, `metadata`
- `BrazeProperties`: 이벤트 수준 또는 제품 수준의 `metadata`입니다. 키는 255자 이하의 비어 있지 않은 문자열이어야 하며 앞에 달러 기호($)가 올 수 없습니다.

## 클라이언트 측 유효성 검사 {#client-side-validation}

잘못된 페이로드는 이벤트 클래스를 생성할 때 `IllegalArgumentException`을 발생시키므로 이벤트가 대기줄에 추가되지 않습니다. 일반적인 규칙:

| 필드 또는 규칙 | 유효성 검사 |
| ------------ | ---------- |
| 문자열 ID 및 이름(`product_id`, `product_name`, `variant_id`, `cart_id`, `checkout_id`, `order_id`, `source`, 선택 사항 URL) | 비어 있지 않으며 최대 255자 |
| `price`, `total_value`, `total_discounts` | `0` 이상이어야 합니다 |
| `currency` | 유효한 ISO 4217 코드(SDK에서 공백 제거 후 대문자로 변환) |
| `products`(장바구니, 결제, 주문 이벤트) | 최소 하나의 `EcommerceProduct` |
| `quantity`(제품당) | 음수가 아닌 정수 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Android client-side validation rules for eCommerce events" }

전송 시 직렬화된 등록정보가 SDK 크기 제한을 초과하면 `logEcommerceEvent`는 오류를 기록하고 이벤트를 전송하지 않습니다.

## 코드 예제 {#code-examples}

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

`CartUpdatedAction`을 사용하여 `action`을 설정합니다:

| 값 | 와이어 값 | 설명 |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | 수량을 늘리거나 라인을 추가합니다. |
| `CartUpdatedAction.REMOVE` | `remove` | 수량을 줄이고, `0`에서 라인을 제거합니다. |
| `CartUpdatedAction.REPLACE` | `replace` | 전체 장바구니를 교체합니다(기본값). |
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

Braze는 이 이벤트에 대한 타입이 지정된 SDK 클래스를 제공하지 않습니다. `ecommerce.order_cancelled` 이벤트 스키마와 일치하는 페이로드로 `logCustomEvent`를 사용하세요.

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

Braze는 이 이벤트에 대한 타입이 지정된 SDK 클래스를 제공하지 않습니다. `ecommerce.order_refunded` 이벤트 스키마와 일치하는 페이로드로 `logCustomEvent`를 사용하세요.

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

`CartUpdatedAction`을 사용하여 `action`을 설정합니다:

| 값 | 와이어 값 | 설명 |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | 수량을 늘리거나 라인을 추가합니다. |
| `CartUpdatedAction.REMOVE` | `remove` | 수량을 줄이고, `0`에서 라인을 제거합니다. |
| `CartUpdatedAction.REPLACE` | `replace` | 전체 장바구니를 교체합니다(기본값). |
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

Braze는 이 이벤트에 대한 타입이 지정된 SDK 클래스를 제공하지 않습니다. `ecommerce.order_cancelled` 이벤트 스키마와 일치하는 페이로드로 `logCustomEvent`를 사용하세요.

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

Braze는 이 이벤트에 대한 타입이 지정된 SDK 클래스를 제공하지 않습니다. `ecommerce.order_refunded` 이벤트 스키마와 일치하는 페이로드로 `logCustomEvent`를 사용하세요.

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

## `logCustomEvent`를 사용한 수동 기록 {#manual-logging-with-logcustomevent}

권장 이벤트를 수동으로 기록하려면 정확한 이벤트 이름(예: `ecommerce.product_viewed`)과 수동으로 구성한 `BrazeProperties` 또는 `JSONObject` 페이로드를 사용하여 `logCustomEvent`를 호출합니다. SDK는 수동 호출에 대해 권장 이벤트 스키마를 유효성 검사하지 않습니다. Braze는 수집 중에 이러한 페이로드를 유효성 검사합니다:

- 유효한 페이로드는 전체 후처리가 적용된 권장 이벤트로 처리됩니다.
- 잘못된 페이로드(필수 필드 누락, 잘못된 유형, 추가 최상위 등록정보)는 수집 후 삭제됩니다. 실패 내역은 워크스페이스 SDK 처리 로그와 [실패 요약 이메일]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#find-failures)에 표시됩니다.

앱에서 잘못된 데이터가 전송되기 전에 포착할 수 있도록 가능하면 `logEcommerceEvent`를 사용하세요. 일반적인 `logCustomEvent` 사용법은 [커스텀 이벤트 기록]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)을 참조하세요.