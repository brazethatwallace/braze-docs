---
nav_title: Einkäufe protokollieren
article_title: Käufe für iOS protokollieren
platform: iOS
page_order: 4
description: "Dieser Referenzartikel zeigt, wie Sie In-App-Käufe und Umsätze tracken und Kauf-Details in Ihrer iOS-Anwendung zuweisen können."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Käufe für iOS protokollieren {#log-purchases-for-ios}

Erfassen Sie In-App-Käufe, damit Sie Ihren Umsatz im Zeitverlauf und über verschiedene Umsatzquellen hinweg verfolgen und Ihre Nutzer:innen nach ihrem Lifetime-Value segmentieren können.

Braze unterstützt Einkäufe in mehreren Währungen. Einkäufe, die Sie in einer anderen Währung als dem USD melden, werden im Dashboard in USD auf der Grundlage des Wechselkurses an dem Tag, an dem sie gemeldet wurden, angezeigt.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsoptionen, die angepasste Events, angepasste Attribute und Kauf-Events bieten, in unseren [Best Practices]({{site.baseurl}}/developer_guide/analytics) sowie unsere Hinweise zu den [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

## Käufe und Umsätze protokollieren {#tracking-purchases-and-revenue}

Um dieses Feature zu nutzen, fügen Sie diesen Methodenaufruf nach einem erfolgreichen Kauf in Ihrer App hinzu:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"))
```

{% endtab %}
{% endtabs %}

- Unterstützte Währungssymbole sind unter anderem: USD, CAD, EUR, GBP, JPY, AUD, CHF, NOK, MXN, NZD, CNY, RUB, TRY, INR, IDR, ILS, SAR, ZAR, AED, SEK, HKD, SPD, DKK.
  - Jedes andere angegebene Währungssymbol führt zu einer protokollierten Warnung, ohne dass das SDK weitere Aktionen durchführt.
- Der Produkt-Bezeichner kann maximal 255 Zeichen lang sein.
- Beachten Sie, dass der Kauf nicht in Braze protokolliert wird, wenn der Produkt-Bezeichner leer ist.

### Eigenschaften hinzufügen {#properties-purchases}

Sie können Metadaten zu Käufen hinzufügen, indem Sie entweder ein [Event-Eigenschaft-Array]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties#nested-objects) oder ein `NSDictionary` übergeben, das mit `NSNumber`-, `NSString`- oder `NSDate`-Werten gefüllt ist.

Weitere Details finden Sie in der [iOS-Klassendokumentation](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aaca4b885a8f61ac9fad3936b091448cc).

### Menge hinzufügen {#adding-quantity}
Sie können Ihren Käufen eine Menge hinzufügen, wenn Kund:innen denselben Kauf mehrmals in einem einzelnen Bezahlvorgang tätigen. Dazu übergeben Sie einen `NSUInteger` für die Menge.

* Der Mengenwert muss im Bereich [0, 100] liegen, damit das SDK einen Kauf protokolliert.
* Methoden ohne Mengeneingabe haben einen Standardwert von 1.
* Methoden mit Mengeneingabe haben keinen Standardwert und **müssen** eine Mengeneingabe erhalten, damit das SDK einen Kauf protokolliert.

Weitere Details finden Sie in der [iOS-Klassendokumentation](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ab50403068be47c0acba9943583e259fa).

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]
withProperties:@{@"key1":"value1"}];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"), withProperties: ["key1":"value1"])
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Wenn Sie einen Wert von 10 USD und eine Menge von 3 übergeben, werden im Profil der Nutzer:innen drei Käufe zu je 10 Dollar protokolliert, also insgesamt 30 Dollar.
{% endalert %}

### Käufe auf Bestellebene protokollieren {#log-purchases-at-the-order-level}
Wenn Sie Käufe auf Bestellebene statt auf Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Kauf-Objekt-Spezifikation]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions).

### Reservierte Schlüssel {#reserved-keys}

Die folgenden Schlüssel sind reserviert und können nicht als Kauf-Eigenschaften verwendet werden:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### REST API

Sie können auch unsere REST API verwenden, um Käufe zu erfassen. Weitere Details finden Sie in der [User-API-Dokumentation]({{site.baseurl}}/api/endpoints/user_data).