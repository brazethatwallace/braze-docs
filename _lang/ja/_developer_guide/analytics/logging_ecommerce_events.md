---
nav_title: eコマースイベントの記録
article_title: Android SDKを使用したeコマースイベントの記録
page_order: 3.25
description: "Braze Android SDKで型付きイベントクラスとlogEcommerceEventを使用して、eコマース推奨イベントを記録する方法を説明します。"
platform:
  - Android
---

# eコマースイベントの記録 {#log-ecommerce-events}

> Braze Android SDKで型付きイベントクラスと`Braze.logEcommerceEvent`を使用して、[eコマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/)を記録する方法を説明します。イベントプロパティスキーマ、プラットフォーム機能、取り込みバリデーションについては、[推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/)および[イベントのバリデーションとトラブルシューティング]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-validation-and-troubleshooting)を参照してください。

{% alert note %}
一覧にないラッパーSDKの場合は、代わりに該当するネイティブAndroidメソッドを使用してください。
{% endalert %}

Android SDK [42.3.0以降](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.3.0)では、構築時のクライアントサイドバリデーションと、`Braze.logEcommerceEvent`呼び出し時の自動`snake_case`シリアライゼーションを備えた型付きeコマースイベントクラスが提供されています。

| Androidクラス | イベント名 | 備考 |
| ------------- | ---------- | ----- |
| `ProductViewedEvent` | `ecommerce.product_viewed` | 製品フィールドを`properties`のトップレベルにフラット化します（`products`配列なし）。このクラスはカタログトリガー用のトップレベル`type`プロパティをサポートしていません。`type`が必要な場合は、[`logCustomEvent`](#manual-logging-with-logcustomevent)またはREST APIを使用してください。 |
| `CartUpdatedEvent` | `ecommerce.cart_updated` | `action`プロパティには`CartUpdatedAction`（`ADD`、`REMOVE`、`REPLACE`）を使用します。 |
| `CheckoutStartedEvent` | `ecommerce.checkout_started` | |
| `OrderPlacedEvent` | `ecommerce.order_placed` | オプションの`cartId`、`totalDiscounts`、`discounts`をサポートしています。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android SDK eCommerce event classes" }

{% alert important %}
`ecommerce.order_cancelled`と`ecommerce.order_refunded`は、型付きAndroid SDKクラスとして利用できません。[`logCustomEvent`](#manual-logging-with-logcustomevent)またはREST APIを使用して記録してください。
{% endalert %}

## 共通のビルディングブロック {#shared-building-blocks}

- `EcommerceProduct`: カート、チェックアウト、注文イベントのラインアイテムです。
  - 必須: `productId`、`productName`、`variantId`、`price`、`quantity`（非負の`Long`）
  - オプション: `imageUrl`、`productUrl`、`metadata`
- `BrazeProperties`: イベントレベルまたは製品レベルの`metadata`です。キーは先頭にドル記号（$）のない、255文字以内の空でない文字列である必要があります。

## クライアントサイドバリデーション {#client-side-validation}

無効なペイロードは、イベントクラスの構築時に`IllegalArgumentException`をスローするため、イベントはキューに入りません。一般的なルール:

| フィールドまたはルール | バリデーション |
| ------------ | ---------- |
| 文字列IDおよび名前（`product_id`、`product_name`、`variant_id`、`cart_id`、`checkout_id`、`order_id`、`source`、オプションのURL） | 空白でないこと、最大255文字 |
| `price`、`total_value`、`total_discounts` | `0`以上であること |
| `currency` | 有効なISO 4217コード（SDKによりトリムされ大文字に変換されます） |
| `products`（カート、チェックアウト、注文イベント） | 1つ以上の`EcommerceProduct` |
| `quantity`（製品ごと） | 非負の整数 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Android client-side validation rules for eCommerce events" }

ディスパッチ時に、シリアライズされたプロパティがSDKのサイズ制限を超えた場合、`logEcommerceEvent`はエラーをログに記録し、イベントを送信しません。

## コード例 {#code-examples}

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

`CartUpdatedAction`を使用して`action`を設定します:

| 値 | ワイヤー値 | 説明 |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | 数量を増やすか、ラインを追加します。 |
| `CartUpdatedAction.REMOVE` | `remove` | 数量を減らします。`0`でラインを削除します。 |
| `CartUpdatedAction.REPLACE` | `replace` | カート全体を置き換えます（デフォルト）。 |
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

Brazeはこのイベント用の型付きSDKクラスを提供していません。`ecommerce.order_cancelled`イベントスキーマに一致するペイロードで`logCustomEvent`を使用してください。

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

Brazeはこのイベント用の型付きSDKクラスを提供していません。`ecommerce.order_refunded`イベントスキーマに一致するペイロードで`logCustomEvent`を使用してください。

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

`CartUpdatedAction`を使用して`action`を設定します:

| 値 | ワイヤー値 | 説明 |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | 数量を増やすか、ラインを追加します。 |
| `CartUpdatedAction.REMOVE` | `remove` | 数量を減らします。`0`でラインを削除します。 |
| `CartUpdatedAction.REPLACE` | `replace` | カート全体を置き換えます（デフォルト）。 |
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

Brazeはこのイベント用の型付きSDKクラスを提供していません。`ecommerce.order_cancelled`イベントスキーマに一致するペイロードで`logCustomEvent`を使用してください。

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

Brazeはこのイベント用の型付きSDKクラスを提供していません。`ecommerce.order_refunded`イベントスキーマに一致するペイロードで`logCustomEvent`を使用してください。

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

## `logCustomEvent`を使用した手動記録 {#manual-logging-with-logcustomevent}

推奨イベントを手動で記録するには、正確なイベント名（例: `ecommerce.product_viewed`）と、手動で構築した`BrazeProperties`または`JSONObject`ペイロードを指定して`logCustomEvent`を呼び出します。SDKは手動呼び出しに対して推奨イベントスキーマのバリデーションを行いません。Brazeは取り込み時にこれらのペイロードをバリデーションします:

- 有効なペイロードは、完全な後処理を伴う推奨イベントとして処理されます。
- 無効なペイロード（必須フィールドの欠落、型の不一致、余分なトップレベルプロパティ）は取り込み後に破棄されます。失敗はワークスペースのSDK処理ログおよび[失敗サマリーメール]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#find-failures)に表示されます。

無効なデータがアプリから送信される前にキャッチできるよう、可能な限り`logEcommerceEvent`を使用してください。一般的な`logCustomEvent`の使用方法については、[カスタムイベントの記録]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)を参照してください。