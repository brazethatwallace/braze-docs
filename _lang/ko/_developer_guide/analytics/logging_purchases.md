---
nav_title: 구매 기록
article_title: Braze SDK를 통한 구매 기록
page_order: 3.2
description: "Braze SDK를 통해 구매를 기록하는 방법을 알아보세요."

---

# 구매 기록 {#log-purchases}

> Braze SDK를 통해 인앱 구매를 기록하는 방법을 알아보세요. 이를 통해 시간 경과에 따른 매출과 소스별 매출을 확인할 수 있습니다. 커스텀 이벤트, 커스텀 속성 및 구매 이벤트를 사용하여 [LTV or 생애주기 가치에 따라]({{site.baseurl}}/developer_guide/analytics#purchase-events-revenue-tracking) 사용자를 세분화할 수 있습니다.

{% alert note %}
목록에 없는 래퍼 SDK의 경우 관련 네이티브 Android 또는 Swift 메서드를 대신 사용하세요.
{% endalert %}

USD가 아닌 통화로 보고된 구매는 보고된 날짜의 환율을 기준으로 Braze에서 USD로 표시됩니다. 대시보드 전환, 캐싱 및 환율 갱신 타이밍에 대한 자세한 내용은 [통화 전환]({{site.baseurl}}/user_guide/data/activation/events/purchase_events#currency-conversion)을 참조하세요. 전환을 방지하려면 통화 코드를 `USD`로 설정하여 구매를 기록하세요.

## 구매 및 매출 기록 {#logging-purchases-and-revenue}

구매 및 매출을 기록하려면 앱에서 구매에 성공한 후 `logPurchase()`를 호출합니다. 제품 식별자가 비어 있으면 구매가 Braze에 기록되지 않습니다.

{% tabs %}
{% tab 웹 %}
표준 웹 SDK 구현의 경우 다음 메서드를 사용할 수 있습니다:

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

Google Tag 매니저를 대신 사용하려면 **Purchase** 태그 유형을 사용하여 [`logPurchase` 메서드](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)를 호출할 수 있습니다. 이 태그를 사용하여 구매를 Braze에 추적하고, 선택적으로 구매 속성정보를 포함할 수 있습니다. 방법은 다음과 같습니다:

1. **Product ID** 및 **Price** 필드는 필수입니다.
2. **Add Row** 버튼을 사용하여 구매 속성정보를 추가합니다.

![Braze 액션 태그 구성 설정을 보여주는 대화 상자. 설정에는 '태그 유형', '외부 ID', '가격', '통화 코드', '수량', '구매 속성정보'가 포함됩니다.]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
{% endtab %}

{% tab Android %}
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

{% tab Cordova %}

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab Flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

{% endtab %}

{% tab React Native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

{% endtab %}

{% tab Unity %}

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

{% endtab %}
{% endtabs %}

{% alert warning %}
`productID`는 최대 255자까지만 허용됩니다. 또한 제품 식별자가 비어 있으면 구매가 Braze에 기록되지 않습니다.
{% endalert %}

### 속성정보 추가 {#adding-properties}

`Int`, `Double`, `String`, `Bool` 또는 `Date` 값으로 채워진 Dictionary를 전달하여 구매에 대한 메타데이터를 추가할 수 있습니다.

{% tabs %}
{% tab 웹 %}
표준 웹 SDK 구현의 경우 다음 메서드를 사용할 수 있습니다:

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

사이트에서 Google Tag 매니저에 표준 [이커머스 이벤트](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) 데이터 레이어 항목을 사용하여 구매를 기록하는 경우, **E-commerce Purchase** 태그 유형을 사용할 수 있습니다. 이 액션 유형은 `items` 목록에 전송된 각 항목에 대해 Braze에서 별도의 "purchase"를 기록합니다.

구매 속성정보로 포함할 추가 속성정보 이름을 지정하려면 구매 속성정보 목록에 해당 키를 지정합니다. Braze는 목록에 추가한 구매 속성정보에 대해 기록 중인 개별 `item` 내에서 해당 값을 조회합니다.

예를 들어 다음과 같은 이커머스 페이로드가 있다고 가정합니다:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

`item_brand`와 `item_name`만 구매 속성정보로 전달하려면 해당 두 필드만 구매 속성정보 테이블에 추가하면 됩니다. 속성정보를 제공하지 않으면 Braze에 대한 [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) 호출에 구매 속성정보가 전송되지 않습니다.
{% endtab %}

{% tab Android %}
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

{% tab Cordova %}

```javascript
var properties = {};
properties["key"] = "value";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab Flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: {"key": "value"});
```

{% endtab %}

{% tab React Native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, { key: "value" });
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

{% endtab %}

{% tab Unity %}

```csharp
Dictionary<string, object> purchaseProperties = new Dictionary<string, object>
{
    { "key", "value" }
};
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), purchaseProperties);
```

{% endtab %}
{% endtabs %}

### 수량 추가 {#adding-quantity}

기본적으로 `quantity`는 `1`로 설정됩니다. 그러나 고객이 한 번의 결제에서 동일한 구매를 여러 번 수행하는 경우 구매에 수량을 추가할 수 있습니다. 수량을 추가하려면 `Int` 값을 `quantity`에 전달합니다.

### REST API 사용 {#using-the-rest-api}

REST API를 사용하여 구매를 기록할 수도 있습니다. 자세한 내용은 [사용자 데이터 엔드포인트]({{site.baseurl}}/api/endpoints/user_data)를 참조하세요.

## 주문 기록 {#logging-orders}

제품 수준 대신 주문 수준에서 구매를 기록하려면 주문 이름 또는 주문 카테고리를 `product_id`로 사용하면 됩니다. 자세한 내용은 [구매 오브젝트 사양]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions)을 참조하세요.

## 예약된 키 {#reserved-keys}

다음 키는 예약되어 있으며 구매 속성정보로 사용할 수 없습니다:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## 지원 통화 {#supported-currencies}

Braze는 다음 통화 기호를 지원합니다. 지원되지 않는 다른 통화 기호를 제공하면 경고가 기록되며, 해당 구매는 Braze에 기록되지 않습니다.

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