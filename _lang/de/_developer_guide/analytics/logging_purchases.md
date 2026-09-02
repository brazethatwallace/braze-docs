---
nav_title: Einkäufe protokollieren
article_title: Käufe über das Braze SDK or Software-Development-Kit protokollieren
page_order: 3.2
description: "Erfahren Sie, wie Sie Einkäufe über das Braze SDK or Software-Development-Kit protokollieren können."

---

# Einkäufe protokollieren {#log-purchases}

> Erfahren Sie, wie Sie In-App-Käufe über das Braze SDK or Software-Development-Kit protokollieren können, damit Sie Ihren Umsatz im Zeitverlauf und über verschiedene Quellen hinweg bestimmen können. So können Sie Nutzer:innen [anhand ihres LTV or Lifetime-Value or Lifetime-Value]({{site.baseurl}}/developer_guide/analytics#purchase-events-revenue-tracking) mit angepassten Events, angepassten Attributen und Kauf-Events segmentieren.

{% alert note %}
Für Wrapper-SDKs, die nicht aufgeführt sind, verwenden Sie stattdessen die entsprechende native Android- oder Swift-Methode.
{% endalert %}

Alle gemeldeten Nicht-USD-Währungen werden in Braze auf Basis des Wechselkurses am Tag der Meldung in USD angezeigt. Informationen zur Dashboard-Konversion, zum Caching und zur Aktualisierung der Wechselkurse finden Sie unter [Währungsumrechnung]({{site.baseurl}}/user_guide/data/activation/events/purchase_events#currency-conversion). Um eine Konversion zu vermeiden, protokollieren Sie Einkäufe mit `USD` als Währungscode.

## Käufe und Umsätze protokollieren {#logging-purchases-and-revenue}

Um Käufe und Umsätze zu protokollieren, rufen Sie `logPurchase()` nach einem erfolgreichen Kauf in Ihrer App auf. Wenn der Produkt-Bezeichner leer ist, wird der Kauf nicht in Braze protokolliert.

{% tabs %}
{% tab web %}
Für eine Standard-Web-SDK or Software-Development-Kit-Implementierung können Sie die folgende Methode verwenden:

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

Wenn Sie stattdessen Google Tag Manager:in verwenden möchten, können Sie den Tag-Typ **Purchase** nutzen, um die [`logPurchase`-Methode](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) aufzurufen. Verwenden Sie diesen Tag, um Käufe in Braze zu tracken, optional einschließlich Kauf-Details. Gehen Sie dazu wie folgt vor:

1. Die Felder **Product ID** und **Price** sind erforderlich.
2. Verwenden Sie den Button **Add Row**, um Kauf-Details hinzuzufügen.

![Ein Dialogfenster mit den Konfigurationseinstellungen für den Braze-Action-Tag. Zu den Einstellungen gehören „Tag-Typ“, „Externe ID“, „Preis“, „Währungscode“, „Menge“ und „Kauf-Details“.]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
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
`productID` darf maximal 255 Zeichen lang sein. Wenn der Produkt-Bezeichner leer ist, wird der Kauf nicht in Braze protokolliert.
{% endalert %}

### Eigenschaften hinzufügen {#adding-properties}

Sie können Metadaten zu Käufen hinzufügen, indem Sie ein Dictionary übergeben, das mit `Int`-, `Double`-, `String`-, `Bool`- oder `Date`-Werten befüllt ist.

{% tabs %}
{% tab web %}
Für eine Standard-Web-SDK or Software-Development-Kit-Implementierung können Sie die folgende Methode verwenden:

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

Wenn Ihre Website Käufe mithilfe des Standard-[eCommerce-Events](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) als Data-Layer-Element im Google Tag Manager:in protokolliert, können Sie den Tag-Typ **E-commerce Purchase** verwenden. Dieser Action-Typ protokolliert einen separaten „Kauf“ in Braze für jeden Artikel, der in der Liste der `items` übermittelt wird.

Sie können auch zusätzliche Eigenschaftsnamen angeben, die als Kauf-Details einbezogen werden sollen, indem Sie deren Schlüssel in der Liste der Kauf-Details angeben. Beachten Sie, dass Braze innerhalb des einzelnen `item`, das protokolliert wird, nach allen Kauf-Details sucht, die Sie der Liste hinzugefügt haben.

Betrachten Sie zum Beispiel folgenden eCommerce-Payload:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

Wenn Sie nur `item_brand` und `item_name` als Kauf-Details übergeben möchten, fügen Sie einfach diese beiden Felder der Tabelle für Kauf-Details hinzu. Wenn Sie keine Eigenschaften angeben, werden keine Kauf-Details im [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase)-Aufruf an Braze übermittelt.
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

### Menge hinzufügen {#adding-quantity}

Standardmäßig ist `quantity` auf `1` gesetzt. Sie können jedoch eine Menge zu Ihren Käufen hinzufügen, wenn Kund:innen denselben Kauf mehrfach in einem einzelnen Bezahlvorgang tätigen. Um eine Menge hinzuzufügen, übergeben Sie einen `Int`-Wert an `quantity`.

### Representational State Transfer API verwenden {#using-the-rest-api}

Sie können auch unsere Representational State Transfer API verwenden, um Käufe zu erfassen. Weitere Informationen finden Sie unter [Nutzerdaten-Endpunkte]({{site.baseurl}}/api/endpoints/user_data).

## Einkäufe auf Bestellebene protokollieren {#logging-orders}

Wenn Sie Einkäufe auf Bestellebene statt auf Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Kauf-Objekt-Spezifikation]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions).

## Reservierte Schlüssel {#reserved-keys}

Die folgenden Schlüssel sind reserviert und können nicht als Kauf-Details verwendet werden:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Unterstützte Währungen {#supported-currencies}

Braze unterstützt die folgenden Währungssymbole. Jedes andere Währungssymbol, das Sie angeben, protokolliert eine Warnung und der Kauf wird nicht in Braze erfasst.

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