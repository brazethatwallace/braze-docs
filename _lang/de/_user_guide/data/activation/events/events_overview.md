---
nav_title: Events
article_title: Events
page_order: 0
hidden: true
page_type: reference
description: "Dieser Artikel beschreibt die verschiedenen Events in Braze – Standard-Events, Kauf-Events und angepasste Events – und ihren Zweck."
---

# Events

> Diese Seite behandelt die verschiedenen Events in Braze und ihren Zweck.

Braze verwendet verschiedene Event-Typen, um ein umfassendes Verständnis des Nutzerverhaltens und des Engagements mit Ihrer Marke zu ermöglichen. Jeder Event-Typ erfüllt einen eigenen Zweck:

- [Standard-Events](#standard-events): Bieten ein grundlegendes Verständnis des Nutzer-Engagements mit Ihrer App oder Website.
- [Kauf-Events](#purchase-events): Entscheidend für das Verständnis des Kaufverhaltens und das Tracking von Umsätzen.
- [Angepasste Events](#custom-events): Bieten tiefere Insights in Nutzerverhalten, das spezifisch für Ihre App oder Ihr Unternehmen ist.

Durch das Tracking dieser verschiedenen Event-Typen können Sie ein tieferes Verständnis Ihrer Nutzer:innen gewinnen, das Ihre Marketingstrategien informiert, Ihnen hilft, Ihre App zu optimieren, und Sie in die Lage versetzt, ein personalisierteres Nutzererlebnis zu bieten. Legen wir los!

## Standard-Events {#standard-events}

In Braze sind Standard-Events vordefinierte Aktionen, die Braze plattformübergreifend erkennt. Im Gegensatz zu [angepassten Events](#custom-events) müssen Sie Standard-Events nicht erstellen oder benennen – sie sind bereits integriert. Allerdings werden nicht alle Standard-Events auf die gleiche Weise getrackt.

Die folgenden Events werden nach der SDK-Integration automatisch getrackt:

- Session-Start
- Session-Ende

Die folgenden Events werden nach zusätzlicher Einrichtung getrackt:

- [Kauf-Events](#purchase-events): Ihr Entwicklungsteam protokolliert diese über die Kaufmethoden des SDK. Weitere Informationen finden Sie im Abschnitt Kauf-Events.
- E-Mail-Engagement-Events (wie E-Mail-Öffnungen und Link-Klicks): Werden von Braze getrackt, wenn Sie Braze E-Mail konfigurieren und E-Mail-Tracking aktivieren.
- Push-Engagement-Events (wie Öffnungen und Klicks von Push-Benachrichtigungen): Werden getrackt, nachdem Sie Push in Braze konfiguriert und die Push-Verarbeitung mit dem Braze SDK in Ihrer App integriert haben.

Als Marketer können Sie Standard-Events nutzen, um Nutzerverhalten und Engagement zu verstehen. Zum Beispiel zeigen Session-Daten, wie oft Nutzer:innen Ihre App oder Website öffnen, während Kauf-Events Ihnen helfen, den Umsatz über die Zeit zu verfolgen.

## Kauf-Events {#purchase-events}

Kauf-Events erfassen und tracken Käufe Ihrer Nutzer:innen. Nach der Integration des Braze SDK kann Ihr Entwicklungsteam Käufe über die Kaufmethoden des SDK protokollieren. Wenn Sie Kauf-Events zum Tracking von Käufen verwenden, können Sie Ihren Umsatz über die Zeit und über verschiedene Umsatzquellen hinweg direkt in Braze überwachen.

Kauf-Events erfassen die folgenden wichtigen Informationen über einen Kauf:

- Produkt-ID (typischerweise der Produktname oder die Kategorie)
- Währung
- Preis
- Menge

Sie können diese Daten dann nutzen, um Ihre Nutzer:innen basierend auf ihrem Lifetime-Value, ihrer Kaufhäufigkeit, bestimmten Käufen und mehr zu segmentieren.

Braze unterstützt auch Käufe in mehreren Währungen. Wenn ein Kauf in einer anderen Währung als USD gemeldet wird, wird er im Braze-Dashboard in USD angezeigt, basierend auf dem Wechselkurs zum Zeitpunkt der Kaufmeldung.

Mehr erfahren Sie in unserem speziellen Artikel zu [Kauf-Events]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/).

{% details Beispielimplementierung %}

Beachten Sie, dass die tatsächliche Implementierung von Kauf-Events technisches Wissen erfordert, da sie die Integration des Braze SDK in Ihre App umfasst. Ihr Customer-Success-Manager wird Ihr Team im Rahmen des Onboardings durch diesen Prozess führen, aber die allgemeinen Schritte sind wie folgt:

1. **Integrieren Sie das Braze SDK:** Bevor Sie Events protokollieren können, müssen Sie das Braze SDK in Ihre App integrieren.
2. **Protokollieren Sie das Kauf-Event:** Nach der SDK-Integration können Sie ein Kauf-Event protokollieren, wann immer ein:e Nutzer:in einen Kauf in Ihrer App tätigt. Dies geschieht typischerweise in der Funktion oder Methode, die aufgerufen wird, wenn ein Kauf abgeschlossen wird.

Hier ist ein Beispiel, wie Sie ein Kauf-Event in einer iOS-App mit Swift protokollieren:

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

In diesem Beispiel ist „product_name“ der Name des gekauften Produkts, „USD“ die Währung des Kaufs, „1.99“ der Preis des Produkts und „1“ die gekaufte Menge.

{:start="3"}
3. **Sehen Sie das Kauf-Event im Braze-Dashboard an:** Nachdem das Kauf-Event protokolliert wurde, können Sie es im Braze-Dashboard einsehen. Sie können diese Daten nutzen, um Ihren Umsatz zu analysieren, Ihre Nutzer:innen zu segmentieren und mehr.

Beachten Sie, dass die genaue Implementierung je nach Plattform (iOS, Android, Internet) und den spezifischen Anforderungen Ihrer App variieren kann.

{% enddetails %}

## Angepasste Events {#custom-events}

Angepasste Events sind Events, die Sie basierend auf den spezifischen Aktionen definieren, die Sie in Ihrer App oder auf Ihrer Website tracken möchten. Braze trackt sie nicht automatisch – Sie müssen diese Events manuell in Ihrer Braze-SDK-Implementierung einrichten. Angepasste Events können alles sein, von einem:einer Nutzer:in, der/die ein Level in einem Spiel abschließt, bis hin zu einem:einer Nutzer:in, der/die seine/ihre Profilinformationen aktualisiert.

Hier ist ein Beispiel, wie Sie ein angepasstes Event in einer iOS-App mit Swift protokollieren:

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

In diesem Beispiel ist „completed_level“ der Name des angepassten Events, das protokolliert wird, wenn ein:e Nutzer:in ein Level in einem Spiel abschließt. Dieses angepasste Event wird dann im Nutzerprofil in Braze erfasst, das Sie nutzen können, um Campaigns zu triggern und Messaging zu personalisieren.

Mehr erfahren Sie in unserem speziellen Artikel zu [angepassten Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events/).

{% details Beispielimplementierung %}

Ähnlich wie Kauf-Events erfordern angepasste Events eine zusätzliche Einrichtung. Hier ist ein allgemeiner Prozess für die Implementierung angepasster Events in Braze:

1. **Integrieren Sie das Braze SDK:** Bevor Sie Events protokollieren können, müssen Sie das Braze SDK in Ihre App integrieren.
2. **Definieren Sie Ihr angepasstes Event:** Entscheiden Sie, welche Aktion in Ihrer App Sie als angepasstes Event tracken möchten. Dies kann alles sein, was für Ihre App relevant ist, z. B. ein:e Nutzer:in, der/die ein Level in einem Spiel abschließt, ein:e Nutzer:in, der/die sein/ihr Profil aktualisiert, oder ein:e Nutzer:in, der/die einen bestimmten Kauftyp tätigt.
3. **Protokollieren Sie das angepasste Event:** Nachdem Sie Ihr angepasstes Event definiert haben, können Sie es im Code Ihrer App protokollieren. Dies geschieht typischerweise in der Funktion oder Methode, die aufgerufen wird, wenn die Aktion stattfindet.

Hier ist ein Beispiel, wie Sie ein angepasstes Event in einer iOS-App mit Swift protokollieren:

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

In diesem Beispiel ist „updated_profile“ der Name des angepassten Events, das protokolliert wird, wenn ein:e Nutzer:in sein/ihr Profil aktualisiert.

{:start="4"}
4. **Fügen Sie Ihrem angepassten Event Eigenschaften hinzu (optional):** Wenn Sie zusätzliche Details über das angepasste Event erfassen möchten, können Sie ihm Eigenschaften hinzufügen. Dies geschieht, indem Sie beim Protokollieren des Events ein Dictionary mit Eigenschaften übergeben.

Hier ist ein Beispiel, wie Sie ein angepasstes Event mit Eigenschaften in einer iOS-App mit Swift protokollieren:

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

In diesem Beispiel hat das angepasste Event eine Eigenschaft namens „Property Name“ mit dem Wert „Property Value“.

{:start="5"}
5. **Sehen Sie das angepasste Event im Braze-Dashboard an:** Nachdem das angepasste Event protokolliert wurde, können Sie es im Braze-Dashboard einsehen. Sie können diese Daten nutzen, um Nutzerverhalten zu analysieren, Ihre Nutzer:innen zu segmentieren und mehr.

{% enddetails %}

<!--

### Using custom events instead of purchase events to track purchases

You might prefer to use custom events to track purchases if you need to capture more specific or additional information about the purchase that the standard purchase event doesn't cover. Here's what you can do with custom events that you can't accomplish with purchase events:

- **Custom definitions:** Custom events can be defined based on any significant action within your app. This level of customization is not available with standard purchase events, which are predefined and specifically designed to track purchases.
- **Additional properties:** You can log additional properties to custom events that provide more context about the event. For example, you could log a custom event when a user makes a purchase and include properties such as the product category or the payment method. This is not possible with standard purchase events, which have a fixed schema that only tracks the product name, currency, price, and quantity.
- **Event frequency:** Custom events allow you to track the frequency of specific actions. With purchase events, you can only track the occurrence of purchases, not other types of actions.

#### Use case 1

Let's say you have an eCommerce app, and you want to track the purchase itself and the product category. The standard purchase event in Braze does not capture this level of detail, so you could use a custom event instead.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Product Category": "Electronics"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the product category is "Electronics". Now you can segment your users based on the product categories they purchase from.

#### Use case 2

Consider a fitness app where users can purchase personal training sessions or premium workout plans. In this case, you might want to track these purchases as custom events to capture additional details about the purchase.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Workout Plan": "10 Sessions Personal Training"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the workout plan is "10 Sessions Personal Training". Now you can segment your users based on the types of workout plans they purchase.

-->