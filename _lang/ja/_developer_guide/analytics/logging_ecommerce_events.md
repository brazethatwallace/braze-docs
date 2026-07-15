---
nav_title: eコマースイベントの記録
article_title: Braze SDKを使用したeコマースイベントの記録
page_order: 3.25
description: "Braze Android、Swift、Web SDKで型付きイベントクラスとlogEcommerceEventを使用して、eコマース推奨イベントを記録する方法を説明します。"
platform:
  - Android
  - Swift
  - Web
---

# eコマースイベントの記録 {#log-ecommerce-events}

> Braze Android、Swift、Web SDKで型付きイベントクラスと`logEcommerceEvent`を使用して、[eコマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)を記録する方法を説明します。イベントプロパティスキーマ、プラットフォーム機能、取り込みバリデーションについては、[推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events)および[イベントのバリデーションとトラブルシューティング]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-validation-and-troubleshooting)を参照してください。

{% alert note %}
一覧にないラッパーSDKの場合は、代わりに該当するネイティブAndroidまたはSwiftメソッドを使用してください。
{% endalert %}

## イベントスキーマ {#event-schemas}

6つのeコマース推奨イベントは、すべてのプラットフォームで共通の注文レベルスキーマを共有しています。各イベントペイロードを構築する際は、以下のプロパティテーブルを使用してください。完全なバリデーション動作とREST APIの例を含む正規スキーマについては、[推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas)を参照してください。セグメンテーション、キャンバステンプレート、レポートなどのプラットフォーム機能については、[eコマースイベントの使用方法]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)を参照してください。

{% tabs local %}
{% tab product_viewed %}

ユーザーが製品詳細ページを閲覧したときにトリガーします。

**イベントプロパティ**

| プロパティ名 | データタイプ | 必須 | 説明 |
| ------------- | --------- | -------- | ----------- |
| `product_id` | 文字列 | はい | 一意の製品識別子（例: SKUまたはアイテムID）。 |
| `product_name` | 文字列 | はい | 製品の表示名。 |
| `variant_id` | 文字列 | はい | 製品バリアント識別子（例: `shirt_medium_blue`）。 |
| `image_url` | 文字列 | いいえ | 製品画像のURL。 |
| `product_url` | 文字列 | いいえ | 製品ページの詳細URL。 |
| `price` | Float | はい | 閲覧時のバリアント単価。 |
| `currency` | 文字列 | はい | 3文字のISO 4217コード（例: `USD`または`EUR`）。 |
| `source` | 文字列 | はい | イベントの発生元ソース（例: `web`、`ios`、または`android`）。 |
| `type` | 文字列の配列 | いいえ | 在庫復活や値下げアラートのBrazeカタログトリガー機能を使用するために必須です。許容される値: `"price_drop"`、`"back_in_stock"`。 |
| `metadata` | オブジェクト | いいえ | 柔軟なキーと値のペア（例: `category`や`brand`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Product viewed event properties" }

{% endtab %}
{% tab cart_updated %}

ユーザーのカートの内容が変更されるたびにトリガーします。カート全体の置き換え（`action`を省略するか`replace`に設定）または増分更新（`add`または`remove`）を使用します。

**イベントプロパティ**

| プロパティ | データタイプ | 必須 | 説明 |
| -------- | --------- | -------- | ----------- |
| `cart_id` | 文字列 | はい | カートの一意の識別子。ユーザーのカートマッピングのために、カート、チェックアウト、注文イベント間で共有されます。 |
| `action` | 文字列 | いいえ | `add`（数量を増やすかラインを追加）、`remove`（数量を減らす。`0`でラインを削除）、または`replace`（カート全体の置き換え。`action`を省略した場合と同じ）。 |
| `total_value` | Float | 条件付き | `action`が省略されているか`replace`の場合は必須。`action`が`add`または`remove`の場合はオプション。 |
| `subtotal_value` | Float | いいえ | カートの小計（割引後、税・送料前）。 |
| `tax` | Float | いいえ | カートに適用される合計税額。 |
| `shipping` | Float | いいえ | カートの合計送料。 |
| `currency` | 文字列 | はい | 3文字のISO 4217コード。 |
| `products` | 配列 | はい | この更新のラインアイテム。製品プロパティテーブルを参照してください。 |
| `source` | 文字列 | はい | イベントの発生元ソース。 |
| `metadata` | オブジェクト | いいえ | 追加のイベントレベルデータ用の柔軟なキーと値のペア。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Cart updated event properties" }

**製品プロパティ（`products[]`）**

| プロパティ | データタイプ | 必須 | 説明 |
| -------- | --------- | -------- | ----------- |
| `product_id` | 文字列 | はい | 一意の製品識別子。 |
| `product_name` | 文字列 | はい | 製品の表示名。 |
| `variant_id` | 文字列 | はい | バリアント識別子。 |
| `image_url` | 文字列 | いいえ | 製品画像のURL。 |
| `product_url` | 文字列 | いいえ | 製品ページのURL。 |
| `quantity` | Integer | はい | カート全体の置き換えの場合、このラインのカート内数量。`add`または`remove`の場合、追加または削除する数量。 |
| `price` | Float | はい | バリアント単価。 |
| `metadata` | オブジェクト | いいえ | 柔軟なキーと値のペア（例: `color`や`size`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Cart updated product properties" }

{% endtab %}
{% tab checkout_started %}

ユーザーがチェックアウトフローを開始したときにトリガーします。

**イベントプロパティ**

| プロパティ | データタイプ | 必須 | 説明 |
| -------- | --------- | -------- | ----------- |
| `checkout_id` | 文字列 | はい | チェックアウトセッションの一意の識別子。 |
| `cart_id` | 文字列 | いいえ | カート識別子。ユーザーのカートマッピングのために、カート、チェックアウト、注文イベント間で共有されます。 |
| `total_value` | Float | はい | チェックアウトの合計金額。 |
| `subtotal_value` | Float | いいえ | 小計（割引後、税・送料前）。 |
| `tax` | Float | いいえ | チェックアウトに適用される合計税額。 |
| `shipping` | Float | いいえ | 合計送料。 |
| `currency` | 文字列 | はい | 3文字のISO 4217コード。 |
| `products` | 配列 | はい | チェックアウト対象のアイテム。製品プロパティテーブルを参照してください。 |
| `source` | 文字列 | はい | イベントの発生元ソース。 |
| `metadata` | オブジェクト | いいえ | 柔軟なキーと値のペア。認識されるサブプロパティ: `checkout_url`（文字列）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Checkout started event properties" }

**製品プロパティ（`products[]`）**

| プロパティ | データタイプ | 必須 | 説明 |
| -------- | --------- | -------- | ----------- |
| `product_id` | 文字列 | はい | 一意の製品識別子。 |
| `product_name` | 文字列 | はい | 製品の表示名。 |
| `variant_id` | 文字列 | はい | バリアント識別子。 |
| `image_url` | 文字列 | いいえ | 製品画像のURL。 |
| `product_url` | 文字列 | いいえ | 製品ページのURL。 |
| `quantity` | Integer | はい | カート内の数量。 |
| `price` | Float | はい | バリアント単価。 |
| `metadata` | オブジェクト | いいえ | 柔軟なキーと値のペア（例: `color`や`size`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Checkout started product properties" }

{% endtab %}
{% tab order_placed %}

注文が正常に完了した場合、または支払いが確認されたときにトリガーします。

**イベントプロパティ**

| プロパティ | データタイプ | 必須 | 説明 |
| -------- | --------- | -------- | ----------- |
| `order_id` | 文字列 | はい | 注文の一意の識別子。 |
| `cart_id` | 文字列 | いいえ | カート識別子。ユーザーのカートマッピングのために、カート、チェックアウト、注文イベント間で共有されます。 |
| `total_value` | Float | はい | 注文の合計金額。 |
| `subtotal_value` | Float | いいえ | 小計（割引後、税・送料前）。 |
| `tax` | Float | いいえ | 注文に適用される合計税額。 |
| `shipping` | Float | いいえ | 合計送料。 |
| `currency` | 文字列 | はい | 3文字のISO 4217コード。 |
| `total_discounts` | Float | いいえ | 注文に適用された割引の合計額。 |
| `discounts` | 配列 | いいえ | 適用された割引の詳細リスト。各割引オブジェクトは`code`（文字列）、`amount`（Float）、`type`（文字列）をサポートします。 |
| `products` | 配列 | はい | 注文内のアイテム。製品プロパティテーブルを参照してください。 |
| `source` | 文字列 | はい | イベントの発生元ソース。 |
| `metadata` | オブジェクト | いいえ | 柔軟なキーと値のペア。認識されるサブプロパティ: `order_status_url`（文字列）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Order placed event properties" }

**製品プロパティ（`products[]`）**

| プロパティ | データタイプ | 必須 | 説明 |
| -------- | --------- | -------- | ----------- |
| `product_id` | 文字列 | はい | 一意の製品識別子。 |
| `product_name` | 文字列 | はい | 製品の表示名。 |
| `variant_id` | 文字列 | はい | バリアント識別子。 |
| `image_url` | 文字列 | いいえ | 製品画像のURL。 |
| `product_url` | 文字列 | いいえ | 製品ページのURL。 |
| `quantity` | Integer | はい | 注文内の数量。 |
| `price` | Float | はい | バリアント単価。 |
| `metadata` | オブジェクト | いいえ | 柔軟なキーと値のペア（例: `color`や`size`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Order placed product properties" }

{% endtab %}
{% tab order_cancelled %}

注文がキャンセルされたときにトリガーします。

**イベントプロパティ**

| プロパティ | データタイプ | 必須 | 説明 |
| -------- | --------- | -------- | ----------- |
| `order_id` | 文字列 | はい | 注文の一意の識別子。 |
| `total_value` | Float | はい | キャンセルされる注文の合計金額。絶対値（`0`以上）を送信してください。Brazeが減額を処理します。 |
| `subtotal_value` | Float | いいえ | 小計（割引後、税・送料前）。 |
| `tax` | Float | いいえ | 注文に適用される合計税額。 |
| `shipping` | Float | いいえ | 合計送料。 |
| `currency` | 文字列 | はい | 3文字のISO 4217コード。 |
| `total_discounts` | Float | いいえ | 注文に適用された割引の合計額。 |
| `discounts` | 配列 | いいえ | 適用された割引の詳細リスト。 |
| `cancel_reason` | 文字列 | はい | 注文がキャンセルされた理由。 |
| `products` | 配列 | はい | キャンセルされた注文内のアイテム。製品プロパティテーブルを参照してください。 |
| `source` | 文字列 | はい | イベントの発生元ソース。 |
| `metadata` | オブジェクト | いいえ | 柔軟なキーと値のペア。認識されるサブプロパティ: `order_status_url`（文字列）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Order cancelled event properties" }

**製品プロパティ（`products[]`）**

| プロパティ | データタイプ | 必須 | 説明 |
| -------- | --------- | -------- | ----------- |
| `product_id` | 文字列 | はい | 一意の製品識別子。 |
| `product_name` | 文字列 | はい | 製品の表示名。 |
| `variant_id` | 文字列 | はい | バリアント識別子。 |
| `image_url` | 文字列 | いいえ | 製品画像のURL。 |
| `product_url` | 文字列 | いいえ | 製品ページのURL。 |
| `quantity` | Integer | はい | 注文内の数量。 |
| `price` | Float | はい | バリアント単価。 |
| `metadata` | オブジェクト | いいえ | 柔軟なキーと値のペア（例: `color`や`size`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Order cancelled product properties" }

{% endtab %}
{% tab order_refunded %}

全額または一部の返金が発行されたときにトリガーします。一部返金の場合、`total_value`には元の注文合計ではなく、返金額のみを設定してください。

**イベントプロパティ**

| プロパティ | データタイプ | 必須 | 説明 |
| -------- | --------- | -------- | ----------- |
| `order_id` | 文字列 | はい | 元の注文の一意の識別子。 |
| `total_value` | Float | はい | 返金の合計金額。絶対値（`0`以上）を送信してください。Brazeが収益の調整を処理します。 |
| `currency` | 文字列 | はい | 3文字のISO 4217コード。 |
| `total_discounts` | Float | いいえ | 元々適用されていた割引の合計額。 |
| `discounts` | 配列 | いいえ | 割引の詳細リスト。 |
| `products` | 配列 | はい | 返金対象のアイテム。製品プロパティテーブルを参照してください。 |
| `source` | 文字列 | はい | イベントの発生元ソース。 |
| `metadata` | オブジェクト | いいえ | 柔軟なキーと値のペア。認識されるサブプロパティ: `order_status_url`（文字列）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Order refunded event properties" }

**製品プロパティ（`products[]`）**

| プロパティ | データタイプ | 必須 | 説明 |
| -------- | --------- | -------- | ----------- |
| `product_id` | 文字列 | はい | 一意の製品識別子。 |
| `product_name` | 文字列 | はい | 製品の表示名。 |
| `variant_id` | 文字列 | はい | バリアント識別子。 |
| `image_url` | 文字列 | いいえ | 製品画像のURL。 |
| `product_url` | 文字列 | いいえ | 製品ページのURL。 |
| `quantity` | Integer | はい | 返金された数量。 |
| `price` | Float | はい | バリアント単価。 |
| `metadata` | オブジェクト | いいえ | 柔軟なキーと値のペア（例: `color`や`size`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Order refunded product properties" }

{% endtab %}
{% endtabs %}

## Android

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

### 共通のビルディングブロック {#shared-building-blocks}

- `EcommerceProduct`: カート、チェックアウト、注文イベントのラインアイテムです。
  - 必須: `productId`、`productName`、`variantId`、`price`、`quantity`（非負の`Long`）
  - オプション: `imageUrl`、`productUrl`、`metadata`
- `BrazeProperties`: イベントレベルまたは製品レベルの`metadata`です。キーは先頭にドル記号（$）のない、255文字以内の空でない文字列である必要があります。

### クライアントサイドバリデーション {#client-side-validation}

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

### コード例 {#code-examples}

{% tabs local %}
{% tab Kotlin %}

{% subtabs local %}
{% subtab product_viewed %}

```kotlin
import com.braze.Braze
import com.braze.models.outgoing.BrazeProperties
import com.braze.models.recommended.ecommerce.ProductViewedEvent

val metadata = BrazeProperties()
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

## iOS

Swift SDKは型付きeコマースイベントクラス（`ProductViewedEvent`、`CartUpdatedEvent`、`CheckoutStartedEvent`、`OrderPlacedEvent`）を提供しており、これらを構築して`logEcommerceEvent`に渡します。カート、チェックアウト、注文イベントの製品には`ProductLineItem`を使用します。各イニシャライザはスロー可能なため、`try?`でラップし、構築が成功した場合にのみイベントを記録してください。
これはSwift SDKバージョン`15.0.0`以降で利用可能です。

`ecommerce.order_cancelled`と`ecommerce.order_refunded`は、型付きSwift SDKクラスとして利用できません。`logCustomEvent`を使用して記録してください。

### コード例

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

Brazeはこのイベント用の型付きSDKクラスを提供していません。`ecommerce.order_cancelled`イベントスキーマに一致するペイロードで`logCustomEvent`を使用してください。

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

Brazeはこのイベント用の型付きSDKクラスを提供していません。`ecommerce.order_refunded`イベントスキーマに一致するペイロードで`logCustomEvent`を使用してください。

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

## Web {#web}

Web SDK [6.8.0以降](https://github.com/braze-inc/braze-web-sdk)では、イベントの`name`と`properties`を指定して`logEcommerceEvent`を呼び出します。レガシーSDKバージョンでは、イベント名とプロパティオブジェクトを指定して`logCustomEvent`を呼び出します。`ecommerce.order_cancelled`と`ecommerce.order_refunded`は`logCustomEvent`を使用します。

### コード例

{% tabs local %}
{% tab product_viewed %}

{% sdk_min_versions web:6.8.0 %}

新しいSDKバージョンでは、`logEcommerceEvent()`を呼び出します:

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
            "color": "ORANGE",
            "size": "6",
            "brand": "Braze"
        }
    }
});
```

レガシーSDKバージョンでは、`logCustomEvent()`を呼び出します:

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
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    }
});
```

{% endtab %}
{% tab cart_updated %}

{% sdk_min_versions web:6.8.0 %}

新しいSDKバージョンでは、`logEcommerceEvent()`を呼び出します:

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

レガシーSDKバージョンでは、`logCustomEvent()`を呼び出します:

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

新しいSDKバージョンでは、`logEcommerceEvent()`を呼び出します:

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

レガシーSDKバージョンでは、`logCustomEvent()`を呼び出します:

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

新しいSDKバージョンでは、`logEcommerceEvent()`を呼び出します:

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

レガシーSDKバージョンでは、`logCustomEvent()`を呼び出します:

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

## `logCustomEvent`を使用した手動記録 {#manual-logging-with-logcustomevent}

推奨イベントを手動で記録するには、正確なイベント名（例: `ecommerce.product_viewed`）と、手動で構築した`BrazeProperties`または`JSONObject`ペイロードを指定して`logCustomEvent`を呼び出します。SDKは手動呼び出しに対して推奨イベントスキーマのバリデーションを行いません。Brazeは取り込み時にこれらのペイロードをバリデーションします:

- 有効なペイロードは、完全な後処理を伴う推奨イベントとして処理されます。
- 無効なペイロード（必須フィールドの欠落、型の不一致、余分なトップレベルプロパティ）は取り込み後に破棄されます。失敗はワークスペースのSDK処理ログおよび[失敗サマリーメール]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#find-failures)に表示されます。

無効なデータがアプリから送信される前にキャッチできるよう、可能な限り`logEcommerceEvent`を使用してください。一般的な`logCustomEvent`の使用方法については、[カスタムイベントの記録]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)を参照してください。