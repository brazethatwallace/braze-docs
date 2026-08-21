---
nav_title: "Kauf-Objekt"
article_title: API Kauf-Objekt
page_order: 8
page_type: reference
description: "In diesem Referenzartikel werden die verschiedenen Komponenten eines Kauf-Objekts erläutert, wie Sie es richtig verwenden und welche Beispiele Sie heranziehen können."

---

# Kauf-Objekt {#purchase-object}

> In diesem Artikel werden die verschiedenen Komponenten eines Kauf-Objekts, die richtige Verwendung, bewährte Verfahren und Beispiele erläutert.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

## Was ist ein Kauf-Objekt? {#what-is-a-purchase-object}

Ein Kauf-Objekt ist ein Objekt, das über die API übergeben wird, wenn ein Kauf getätigt wurde. Jedes Kauf-Objekt befindet sich innerhalb eines Kauf-Arrays, wobei jedes Objekt einen einzelnen Kauf einer bestimmten Nutzer:in zu einem bestimmten Zeitpunkt darstellt. Das Kauf-Objekt verfügt über viele verschiedene Felder, die es dem Braze-Backend ermöglichen, diese Informationen für Anpassung, Datenerfassung und Personalisierung zu speichern und zu verwenden.

### Objektkörper {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required.
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  // See the following product_id naming conventions for clarification.
  "product_id" : (required, string) identifier for the purchase, for example, Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (for example, Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601) Time of purchase,
  // See the following purchase object explanation for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

{% alert note %}
Käufe mit Zeitstempeln in der Zukunft werden standardmäßig auf die aktuelle Zeit gesetzt. Dies stellt sicher, dass Kauf-Events mit genauem Timing erfasst werden.
{% endalert %}

- [Externe Nutzer-ID]({{site.baseurl}}/api/basics#user-ids)
- [App-Bezeichner]({{site.baseurl}}/api/identifier_types)
- [ISO 4217 Währungscode Wiki](http://en.wikipedia.org/wiki/ISO_4217)
- [ISO 8601 Zeitcode Wiki](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
Einige Bezeichnerpaare können nicht zusammen verwendet werden, und `email` hat Vorrang vor `phone`, wenn beide angegeben werden. Vollständige Details finden Sie unter [Bezeichnerauflösung]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution).
{% endalert %}

## Kauf-Produkt-ID {#purchase-product-id}

Innerhalb des Kauf-Objekts ist die `product_id` ein Bezeichner für den Kauf (z. B. `Product Name` oder `Product Category`):

- Braze ermöglicht es Ihnen, bis zu 5.000 `product_id`s im Dashboard zu speichern.
- Die `product_id` kann bis zu 255 Zeichen lang sein.

### Namenskonventionen {#naming-conventions}

Bei Braze bieten wir einige allgemeine Namenskonventionen für die `product_id` des Kauf-Objekts an. Bei der Wahl der `product_id` empfiehlt Braze, einfache Namen wie den Produktnamen oder die Produktkategorie (anstelle von SKUs) zu verwenden, mit dem Ziel, alle protokollierten Artikel nach dieser `product_id` zu gruppieren.

Dies erleichtert die Identifizierung von Produkten für Segmentierung und Triggering.

### Käufe auf Bestellebene protokollieren {#log-purchases-at-the-order-level}

Wenn Sie Käufe auf Bestellebene statt auf Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden (z. B. `Online Order` oder `Completed Order`).

Um beispielsweise Käufe auf Bestellebene im Web SDK zu protokollieren:

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
      }
    }
  ]
}
```

## Kauf-Eigenschaften-Objekt {#purchase-properties-object}

{% include data_activation/purchase_event_property_data_types.md %}

Eine konsolidierte Referenz der Datentypen für angepasste Attribute, Event-Eigenschaften und Kataloge finden Sie unter [Datentypen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#purchase-event-property-data-types).

### Kauf-Eigenschaften {#purchase-properties}

[Kauf-Eigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-properties) können zum Triggern von Nachrichten und zur Personalisierung mit Liquid verwendet werden. Außerdem ist eine Segmentierung auf der Grundlage dieser Eigenschaften möglich.

{% include data_activation/segmentable_purchase_properties_keys_note.md %}

#### Namenskonventionen

Bitte beachten Sie, dass dieses Feature **pro Produkt** und nicht pro Kauf aktiviert wird. Wenn Sie z. B. ein großes Volumen an unterschiedlichen Produkten haben, die aber alle die gleichen Eigenschaften haben, ist eine Segmentierung möglicherweise eher unnötig.

In diesem Fall empfehlen wir, bei der Festlegung der Datenstrukturen Produktnamen auf „Gruppenebene“ anstelle von Bezeichnern auf Transaktionsebene zu verwenden. Zum Beispiel sollte ein Zugunternehmen Produkte für „Einzelfahrt“, „Hin- und Rückfahrt“, „Multi-City“ haben und nicht für bestimmte Transaktionen wie „Transaktion 123“ oder „Transaktion 046“. Ein weiteres Beispiel: Für das Kauf-Event „Essen“ sollten Sie die Eigenschaften „Kuchen“ und „Sandwich“ festlegen.

{% alert important %}
Beachten Sie, dass Produkte über die Braze REST API hinzugefügt werden können. Wenn Sie beispielsweise einen Aufruf an den `/users/track`-Endpunkt senden und eine neue Kauf-ID hinzufügen, erstellt Braze automatisch ein Produkt im Bereich **Dateneinstellungen** > **Produkte** des Dashboards.
{% endalert %}

### Beispiel Kauf-Objekt {#example-purchase-object}

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "backpack",
      "currency" : "USD",
      "price" : 40.00,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogram" : "ABC",
        "checkout_duration" : 180,
        "size" : "Large",
        "brand" : "Backpack Locker"
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pencil",
      "currency" : "USD",
      "price" : 2.00,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "sharpened" : true
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pen",
      "currency" : "USD",
      "price" : 2.50,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

### Kauf-Objekte, Event-Objekte und Webhooks {#purchase-objects-event-objects-and-webhooks}

Anhand des angegebenen Beispiels können wir sehen, dass jemand einen Rucksack mit den Eigenschaften Farbe, Monogramm, Kassendauer, Größe und Marke gekauft hat. Wir können dann Segmente mit diesen Eigenschaften erstellen, indem wir [Kauf-Event-Eigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-properties) verwenden oder angepasste Nachrichten über einen Kanal mit Liquid senden. Zum Beispiel: „Hallo **Ann F.**, vielen Dank für den Kauf dieses **roten, mittelgroßen Rucksacks** für **40,00 $**! Danke für Ihren Einkauf bei **Backpack Locker**!“

Wenn Sie Eigenschaften zur Segmentierung speichern und tracken möchten, müssen Sie diese als angepasste Attribute einrichten. Dies kann mithilfe von [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension) geschehen, die es Ihnen ermöglichen, Nutzer:innen auf der Grundlage von angepassten Events oder Kaufverhalten anzusprechen, die für die Lifetime des jeweiligen Nutzerprofils gespeichert wurden.