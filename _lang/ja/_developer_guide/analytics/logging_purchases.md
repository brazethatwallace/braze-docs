---
nav_title: 購入記録
article_title: Braze SDKを通じて購入を記録する
page_order: 3.2
description: "Braze SDKを使用して購入を記録する方法について説明します。"

---

# 購入記録 {#log-purchases}

> Braze SDKを使用してアプリ内購入を記録する方法について説明します。これにより、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。カスタムイベント、カスタム属性、および購入イベントを使用して、[生涯価値に基づいて]({{site.baseurl}}/developer_guide/analytics#purchase-events-revenue-tracking)ユーザーをセグメント化できます。

{% alert note %}
リストされていないラッパーSDKの場合は、代わりに関連するネイティブAndroidまたはSwiftメソッドを使用してください。
{% endalert %}

米ドル以外の通貨でレポートされた購入は、レポートされた日付の為替レートに基づいて米ドル単位でBrazeに表示されます。通貨換算を防ぐには、通貨をUSDにハードコードしてください。

## 購入と売上の記録 {#logging-purchases-and-revenue}

購入と売上を記録するには、アプリでの購入が正常に完了した後に`logPurchase()`を呼び出します。製品IDが空の場合、購入はBrazeに記録されません。

{% tabs %}
{% tab web %}
標準のWeb SDK実装では、以下のメソッドを使用できます。

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

代わりにGoogle Tag Managerを使用したい場合は、**Purchase**タグタイプを使用して[`logPurchase`メソッド](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)を呼び出すことができます。このタグを使用して、Brazeへの購入をトラッキングします。オプションで購入プロパティを含めることもできます。そのためには以下を行います。

1. **Product ID**と**Price**フィールドは必須です。
2. 購入プロパティを追加するには、**Add Row**ボタンを使用します。

![Brazeアクションタグの設定を示すダイアログボックス。設定項目には「tag type」「external ID」「price」「currency code」「quantity」「purchase properties」が含まれます。]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(context).logPurchase(
   String productId,
   String currencyCode,
   BigDecimal price,
   int quantity
);
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(context).logPurchase(
  productId: String,
  currencyCode: String,
  price: BigDecimal,
  quantity: Int
)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}

```swift
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price)
```

{% endsubtab %}
{% subtab objective-c %}

```objc
[AppDelegate.braze logPurchase:"product_id"
                      currency:@"USD"
                         price:price];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

{% endtab %}

{% tab react native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

{% endtab %}

{% tab unity %}

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

{% endtab %}
{% endtabs %}

{% alert warning %}
`productID`の最大文字数は255文字です。また、製品IDが空の場合、購入はBrazeに記録されません。
{% endalert %}

### プロパティの追加 {#adding-properties}

`Int`、`Double`、`String`、`Bool`、または`Date`の値が入力されたディクショナリを渡すことで、購入に関するメタデータを追加できます。

{% tabs %}
{% tab web %}
標準のWeb SDK実装では、以下のメソッドを使用できます。

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

サイトで標準の[eコマースイベント](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm)データレイヤーアイテムを使用してGoogle Tag Managerに購入を記録する場合は、**E-commerce Purchase**タグタイプを使用できます。このアクションタイプでは、`items`のリストで送信されたアイテムごとに個別の「購入」をBrazeに記録します。

購入プロパティリストでキーを指定することで、購入プロパティとして含める追加のプロパティ名を指定することもできます。Brazeは、リストに追加した購入プロパティについて、記録されている個々の`item`内を検索します。

たとえば、次のeコマースペイロードがあるとします。

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

`item_brand`と`item_name`だけを購入プロパティとして渡す場合は、これら2つのフィールドを購入プロパティテーブルに追加するだけです。プロパティを指定しない場合、Brazeへの[`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)呼び出しで購入プロパティは送信されません。
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
BrazeProperties purchaseProperties = new BrazeProperties();
purchaseProperties.addProperty("key", "value");
Braze.getInstance(context).logPurchase(..., purchaseProperties);
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
val purchaseProperties = BrazeProperties()
purchaseProperties.addProperty("key", "value")
Braze.getInstance(context).logPurchase(..., purchaseProperties)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}

```swift
let purchaseProperties = ["key": "value"]
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price, properties: purchaseProperties)
```

{% endsubtab %}
{% subtab objective-c %}

```objc
NSDictionary *purchaseProperties = @{@"key": @"value"};
[AppDelegate.braze logPurchase:@"product_id"
                      currency:@"USD"
                         price:price
                   properties:purchaseProperties];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["key"] = "value";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: {"key": "value"});
```

{% endtab %}

{% tab react native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, { key: "value" });
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

{% endtab %}

{% tab unity %}

```csharp
Dictionary<string, object> purchaseProperties = new Dictionary<string, object>
{
    { "key", "value" }
};
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), purchaseProperties);
```

{% endtab %}
{% endtabs %}

### 数量の追加 {#adding-quantity}

デフォルトでは、`quantity`は`1`に設定されています。ただし、顧客が1回のチェックアウトで同じ購入を複数回行う場合は、購入に数量を追加できます。数量を追加するには、`Int`値を`quantity`に渡します。

### REST APIの使用 {#using-the-rest-api}

REST APIを使用して購入を記録することもできます。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data)を参照してください。

## 注文の記録 {#logging-orders}

商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを`product_id`として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions)を参照してください。

## 予約済みのキー {#reserved-keys}

以下のキーは予約されているため、購入プロパティとして使用できません。

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## 対応通貨 {#supported-currencies}

Brazeは以下の通貨記号をサポートしています。これ以外の通貨記号を指定すると警告が記録され、購入はBrazeに記録されません。

- `AED`, `AFN`, `ALL`, `AMD`, `ANG`, `AOA`, `ARS`, `AUD`, `AWG`, `AZN`
- `BAM`, `BBD`, `BDT`, `BGN`, `BHD`, `BIF`, `BMD`, `BND`, `BOB`, `BRL`
- `BSD`, `BTC`, `BTN`, `BWP`, `BYR`, `BZD`
- `CAD`, `CDF`, `CHF`, `CLF`, `CLP`, `CNY`, `COP`, `CRC`, `CUC`, `CUP`, `CVE`, `CZK`
- `DJF`, `DKK`, `DOP`, `DZD`
- `EEK`, `EGP`, `ERN`, `ETB`, `EUR`
- `FJD`, `FKP`
- `GBP`, `GEL`, `GGP`, `GHS`, `GIP`, `GMD`, `GNF`, `GTQ`, `GYD`
- `HKD`, `HNL`, `HRK`, `HTG`, `HUF`
- `IDR`, `ILS`, `IMP`, `INR`, `IQD`, `IRR`, `ISK`
- `JEP`, `JMD`, `JOD`, `JPY`
- `KES`, `KGS`, `KHR`, `KMF`, `KPW`, `KRW`, `KWD`, `KYD`, `KZT`
- `LAK`, `LBP`, `LKR`, `LRD`, `LSL`, `LTL`, `LVL`, `LYD`
- `MAD`, `MDL`, `MGA`, `MKD`, `MMK`, `MNT`, `MOP`, `MRO`, `MTL`, `MUR`, `MVR`, `MWK`, `MXN`, `MYR`, `MZN`
- `NAD`, `NGN`, `NIO`, `NOK`, `NPR`, `NZD`
- `OMR`
- `PAB`, `PEN`, `PGK`, `PHP`, `PKR`, `PLN`, `PYG`
- `QAR`
- `RON`, `RSD`, `RUB`, `RWF`
- `SAR`, `SBD`, `SCR`, `SDG`, `SEK`, `SGD`, `SHP`, `SLL`, `SOS`, `SRD`, `STD`, `SVC`, `SYP`, `SZL`
- `THB`, `TJS`, `TMT`, `TND`, `TOP`, `TRY`, `TTD`, `TWD`, `TZS`
- `UAH`, `UGX`, `USD`, `UYU`, `UZS`
- `VEF`, `VND`, `VUV`
- `WST`
- `XAF`, `XAG`, `XAU`, `XCD`, `XDR`, `XOF`, `XPD`, `XPF`, `XPT`
- `YER`
- `ZAR`, `ZMK`, `ZMW`, `ZWL`