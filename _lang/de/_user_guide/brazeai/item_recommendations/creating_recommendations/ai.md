---
nav_title: KI-Empfehlungen
article_title: KI-Artikelempfehlungen erstellen
description: "Dieser Artikel beschreibt, wie Sie eine KI-Artikelempfehlung für Artikel in einem Katalog erstellen."
page_order: 1
---

# KI-Artikelempfehlungen erstellen {#create-ai-item-recommendations}

> Erfahren Sie, wie Sie ein KI-Empfehlungssystem aus Artikeln in Ihrem Katalog erstellen.

## Über KI-Artikelempfehlungen {#about-ai-item-recommendations}

Nutzen Sie KI-Artikelempfehlungen, um die beliebtesten Produkte zu berechnen oder personalisierte KI-Empfehlungen für einen bestimmten [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs) zu erstellen. Nachdem Sie Ihre Empfehlung erstellt haben, können Sie die Personalisierung nutzen, um diese Produkte in Ihre Nachrichten einzufügen.

{% alert tip %}
[KI-Personalisierte Empfehlungen](#recommendation-types) funktionieren am besten mit mindestens einigen hundert Katalogartikeln, höchstens 100.000 Katalogartikeln und in der Regel mindestens 30.000 Nutzer:innen mit Kauf- oder Interaktionsdaten. Dies ist nur ein grober Richtwert und kann variieren. Die anderen Empfehlungstypen können mit weniger Daten arbeiten, auch wenn **Beliebteste** als Fallback verwendet wird.
{% endalert %}

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## KI-Artikelempfehlung erstellen {#creating-an-ai-item-recommendation}

### Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

- Mindestens einen [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs), um einen der im folgenden Abschnitt beschriebenen Empfehlungstypen zu verwenden.
- Kauf- oder Event-Daten in Braze (angepasste Events, das Event „Bestellung aufgegeben“ oder das Kauf-Objekt), die eine Referenz auf den Artikel enthalten und mit den Katalog-Artikel-IDs übereinstimmen müssen.

### Schritt 1: Eine neue Empfehlung erstellen {#step-1-create-a-new-recommendation}

Sie können eine KI-Artikelempfehlung von zwei Stellen im Dashboard aus erstellen:

{% tabs local %}
{% tab Über das Navigationsmenü %}
1. Gehen Sie zu **Analytics** > **AI Item Recommendation**.
2. Wählen Sie **Create Prediction** > **AI Item Recommendation**.
{% endtab %}

{% tab Aus einem Katalog %}
Sie können eine Empfehlung auch direkt aus einem einzelnen Katalog erstellen. Wählen Sie Ihren Katalog auf der Seite **Catalogs** aus und wählen Sie dann **Create Recommendation**.
{% endtab %}
{% endtabs %}

### Schritt 2: Details zur Empfehlung hinzufügen {#step-2-add-recommendation-details}

Geben Sie Ihrer Empfehlung einen Namen und eine optionale Beschreibung.

![Schritt „Empfehlungsdetails“ mit den Feldern für Name und Beschreibung.]({% image_buster /assets/img/item_recs_1.png %})

### Schritt 3: Ihre Empfehlung definieren {#recommendation-type}

Wählen Sie einen Empfehlungstyp aus. Jeder Typ verwendet die Artikelinteraktionsdaten der letzten sechs Monate, z. B. Kauf-, Bestellungs- oder angepasste Event-Daten. Ausführlichere Informationen und Anwendungsfälle finden Sie unter [Typen und Anwendungsfälle]({{site.baseurl}}/user_guide/brazeai/item_recommendations).

{% alert tip %}
Wenn Sie **Neueste** oder **KI-Personalisiert** verwenden, erhalten Nutzer:innen, deren Daten nicht ausreichen, um individuelle Empfehlungen zu erstellen, als Fallback die **beliebtesten** Artikel. Auf der **Analytics**-Seite wird eine Schätzung des Anteils der Nutzer:innen angezeigt, die den **Beliebteste**-Fallback erhalten. Der **Beliebteste**-Fallback gibt nur Artikel zurück, die im verknüpften Katalog vorhanden sind.
{% endalert %}

#### Schritt 3.1: Frühere Käufe oder Interaktionen ausschließen (optional) {#step-31-exclude-prior-purchases-or-interactions-optional}

Um zu vermeiden, dass Artikel vorgeschlagen werden, die Nutzer:innen bereits gekauft oder mit denen sie interagiert haben, wählen Sie **Do not recommend items users have previously interacted with**. Diese Option ist nur verfügbar, wenn der Empfehlungs-**Typ** auf **AI Personalized** eingestellt ist.

![Schritt „Ihre Empfehlung definieren“ mit „KI-Personalisiert“ als Typ und der ausgewählten Option „Keine Artikel empfehlen, mit denen Nutzer:innen zuvor interagiert haben“.]({% image_buster /assets/img/item_recs_2-3.png %})

Diese Einstellung verhindert, dass Nachrichten Artikel wiederverwenden, die Nutzer:innen bereits gekauft oder mit denen sie interagiert haben – vorausgesetzt, die Empfehlung wurde kürzlich aktualisiert. Artikel, die zwischen den Empfehlungsaktualisierungen gekauft oder mit denen interagiert wurde, können weiterhin angezeigt werden. Bei der kostenlosen Version der Artikelempfehlungen werden wöchentlich Aktualisierungen vorgenommen. Bei der Pro-Version der KI-Artikelempfehlungen erfolgt die Aktualisierung alle 24 Stunden.

Wenn Sie beispielsweise die Pro-Version der KI-Artikelempfehlungen verwenden und Nutzer:innen etwas kaufen und dann innerhalb von 30 Minuten eine Marketing-E-Mail erhalten, wird der gerade gekaufte Artikel möglicherweise nicht rechtzeitig aus der E-Mail ausgeschlossen. Nachrichten, die nach 24 Stunden gesendet werden, enthalten diesen Artikel jedoch nicht mehr.

#### Schritt 3.2: Katalog auswählen {#step-32-select-a-catalog}

Falls noch nicht ausgefüllt, wählen Sie den [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs) aus, aus dem diese Empfehlung Artikel beziehen soll.

#### Schritt 3.3: Eine Auswahl hinzufügen (optional) {#step-33-add-a-selection-optional}

Wenn Sie mehr Kontrolle über Ihre Empfehlung wünschen, wählen Sie eine [Auswahl]({{site.baseurl}}/user_guide/data/activation/catalogs/selections), um angepasste Filter anzuwenden. Auswahlen filtern Empfehlungen nach bestimmten Spalten im Katalog, z. B. Marke, Größe oder Standort. Auswahlen, die Liquid enthalten, können nicht in Ihrer Empfehlung verwendet werden.

![Ein Beispiel für die Auswahl „auf Lager“, die für die Empfehlung ausgewählt wurde.]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
Wenn Sie Ihre Auswahl nicht finden können, vergewissern Sie sich zunächst, dass sie in Ihrem Katalog eingerichtet ist.
{% endalert %}

### Schritt 4: Interaktion für Empfehlungen auswählen {#step-4-select-the-interaction-to-drive-recommendations}

Wählen Sie das Event aus, für das diese Empfehlung optimiert werden soll. Bei diesem Event handelt es sich in der Regel um einen Kauf, es kann aber auch jede andere Interaktion mit einem Artikel sein.

Sie können optimieren für:

- Kauf-Events mit dem [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object)
- Angepasste Events, die einen Kauf darstellen
- Angepasste Events, die eine andere Artikelinteraktion darstellen (z. B. Produktansichten, Klicks oder Medienwiedergabe)
- Bestellungen mit dem [Event „Bestellung aufgegeben“]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.order_placed)

Wenn Sie **Custom Event** wählen, wählen Sie Ihr Event aus der Liste aus.

![Das angepasste Event „purchase“ als aktuell verwendete Tracking-Methode ausgewählt.]({% image_buster /assets/img/item_recs_3.png %})

{% alert note %}
Angepasste Events müssen über ausreichende Daten verfügen, bevor sie in der Event-Liste angezeigt werden. Sollte Ihr angepasstes Event nicht angezeigt werden, könnte dies daran liegen, dass das Braze-Backend es noch nicht verarbeitet hat oder dass nicht genügend Daten für das Modelltraining vorhanden sind. KI-Empfehlungen basieren auf historischen Daten, um Insights zu generieren. Daher sind neu erstellte oder selten getriggerte Events erst verfügbar, wenn mehr Daten gesammelt wurden.
{% endalert %}

### Schritt 5: Den entsprechenden Eigenschaftsnamen auswählen {#property-name}

Um eine Empfehlung zu erstellen, müssen Sie Braze mitteilen, welches Feld Ihres Interaktions-Events (Event „Bestellung aufgegeben“, Kauf-Objekt oder angepasstes Event) den eindeutigen Bezeichner enthält, der mit dem Feld `id` eines Artikels im Katalog übereinstimmt. Nicht sicher? [Anforderungen anzeigen](#requirements).

Wählen Sie dieses Feld für den **Property Name** aus.

Das Feld **Property Name** wird mit einer Liste von Feldern vorausgefüllt, die über das SDK an Braze gesendet werden. Wenn genügend Daten vorhanden sind, werden diese Eigenschaften auch nach der Wahrscheinlichkeit sortiert, dass es sich um die richtige Eigenschaft handelt. Wählen Sie diejenige aus, die dem Feld `id` des Katalogs entspricht.

![Der ausgewählte Eigenschaftsname „purchase_item“, der den Artikel-IDs im Katalog entspricht.]({% image_buster /assets/img/item_recs_4.png %})

#### Anforderungen {#requirements}

Für die Auswahl Ihrer Eigenschaft gelten einige Anforderungen:

- Sie muss dem Feld `id` des ausgewählten Katalogs zugeordnet sein.
- **Wenn Sie das Event „Bestellung aufgegeben“ ausgewählt haben oder [E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) zum Trainieren von Artikelempfehlungen verwenden:** Geben Sie `products.product_id` für die Produkt-ID ein.
  - Das Feld kann sich innerhalb eines Arrays von Produkten befinden oder mit einem Array von IDs enden. In beiden Fällen wird jede Produkt-ID als separates, aufeinanderfolgendes Event mit demselben Zeitstempel behandelt.
- **Wenn Sie Kauf-Objekt ausgewählt haben:** Muss die `product_id` oder ein Feld der `properties` Ihres Interaktions-Events sein.
- **Wenn Sie Angepasstes Event ausgewählt haben:** Muss ein Feld der `properties` Ihres angepassten Events sein.
- Verschachtelte Felder müssen in der Dropdown-Liste **Property Name** in Punktnotation im Format `event_property.nested_property` eingegeben werden. Wenn Sie zum Beispiel die verschachtelte Eigenschaft `district_name` innerhalb der Event-Eigenschaft `location` auswählen möchten, geben Sie `location.district_name` ein.

#### Beispielzuordnungen {#example-mappings}

Die folgenden Beispielzuordnungen beziehen sich beide auf diesen Beispielkatalog:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table aria-label="Beispielzuordnungen" class="tg">
  <caption>Beispielzuordnungen</caption>
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">ADI-BL-7</td>
    <td class="tg-0pky">Adidas Black Size 7</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-RD-8</td>
    <td class="tg-0pky">Adidas Red Size 8</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-WH-9</td>
    <td class="tg-0pky">Adidas White Size 9</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-PP-10</td>
    <td class="tg-0pky">Adidas Purple Size 10</td>
    <td class="tg-0pky">75.00 USD</td>
  </tr>
</tbody>
</table>

{% tabs %}
{% tab Angepasstes Event %}

Nehmen wir an, Sie möchten das angepasste Event `added_to_cart` verwenden, um ähnliche Produkte zu empfehlen, bevor die Kund:in zur Kasse geht. Das Event `added_to_cart` enthält die Event-Eigenschaft `product_sku`.

Die Eigenschaft `product_sku` muss daher mindestens einen der Werte aus der Spalte `id` im Beispielkatalog enthalten: „ADI-BL-7“, „ADI-RD-8“, „ADI-WH-9“ oder „ADI-PP-10“. Sie benötigen nicht für jeden Katalogartikel Events, aber genügend, damit das Empfehlungssystem ausreichend Inhalte hat, um damit zu arbeiten.

##### Beispiel für ein angepasstes Event-Objekt {#example-custom-event-object}

Dieses Event enthält `"product_sku": "ADI-BL-7"`, das mit dem ersten Artikel im Beispielkatalog übereinstimmt.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "product_sku": "ADI-BL-7"
      }
    }
  ]
}
```

##### Beispiel für ein angepasstes Event-Objekt mit einem Array von Produkten {#example-custom-event-object-with-an-array-of-products}

Wenn die Event-Eigenschaften mehrere Produkte in einem Array enthalten, wird jede Produkt-ID als separates, aufeinanderfolgendes Event behandelt. Dieses Event kann mit der Eigenschaft `products.sku` den ersten und dritten Artikel im Beispielkatalog zuordnen.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "2ff3f9a9-8803-4c3a-91da-14adbf93dc99",
        "products": [
          { "sku": "ADI-BL-7" },
          { "sku": "ADI-WH-9" }
        ]
      }
    }
  ]
}
```

##### Beispiel für ein angepasstes Event-Objekt mit einem verschachtelten Objekt, das ein Produkt-ID-Array enthält {#example-custom-event-object-with-a-nested-object-containing-a-product-id-array}

Wenn Ihre Produkt-IDs Werte in einem Array statt Objekte sind, können Sie dieselbe Notation verwenden, und jede Produkt-ID wird als separates, aufeinanderfolgendes Event behandelt. Dies lässt sich im folgenden Event flexibel mit verschachtelten Objekten kombinieren, indem Sie die Eigenschaft als `purchase.product_skus` konfigurieren, um den ersten und dritten Artikel im Beispielkatalog zuzuordnen.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "13791e08-7c22-4f6c-8cc6-832c76af3743",
        "purchase": {
          "product_skus": ["ADI-BL-7", "ADI-WH-9"]
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Kauf-Objekt %}

Ein Kauf-Objekt wird über die API übergeben, wenn ein Kauf getätigt wurde.

Was die Zuordnung betrifft, gilt für Kauf-Objekte eine ähnliche Logik wie für angepasste Events, mit dem Unterschied, dass Sie zwischen der `product_id` des Kauf-Objekts oder einem Feld im `properties`-Objekt wählen können.

Beachten Sie: Sie benötigen nicht für jeden Katalogartikel Events, aber genügend, damit das Empfehlungssystem ausreichend Inhalte hat, um damit zu arbeiten.

##### Beispiel eines Kauf-Objekts, das einer Produkt-ID zugeordnet ist {#example-purchase-object-mapped-to-product-id}

Dieses Event enthält `"product_id": "ADI-BL-7"`, das dem ersten Artikel im Katalog entspricht.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "ADI-BL-7",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "color": "black",
        "checkout_duration": 180,
        "size": "7",
        "brand": "Adidas"
      }
    }
  ]
}
```

##### Beispiel für ein Kauf-Objekt, das einem Eigenschaftsfeld zugeordnet ist {#example-purchase-object-mapped-to-a-properties-field}

Dieses Event hat die Eigenschaft `"sku": "ADI-RD-8"`, die dem zweiten Artikel im Katalog entspricht.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "shoes",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "sku": "ADI-RD-8",
        "color": "red",
        "checkout_duration": 180,
        "size": "8",
        "brand": "Adidas"
      }
    }
  ]
}
```

{% endtab %}
{% tab Event „Bestellung aufgegeben“ %}

##### Beispiel eines Objekts „Bestellung aufgegeben“, das einer Produkt-ID zugeordnet ist {#example-order-placed-object-mapped-to-product-id}

```json
{
  "name": "ecommerce.order_placed",
  "properties": {
    "order_id": "order_123",
    "total_value": 200.0,
    "currency": "USD",
    "products": [
      {
        "product_id": "ADI-BL-7",
        "product_name": "Adidas Black Size 7",
        "variant_id": "ADI-BL-7-default",
        "quantity": 1,
        "price": 100.0
      }
    ],
    "source": "storefront"
  }
}
```

{% endtab %}
{% endtabs %}

### Schritt 6: Empfehlung trainieren {#step-6-train-the-recommendation}

Wenn Sie so weit sind, wählen Sie **Create Recommendation**. Dieser Vorgang kann zwischen 10 Minuten und 36 Stunden dauern. Sie erhalten eine E-Mail-Benachrichtigung, wenn die Empfehlung erfolgreich trainiert wurde, oder eine Erklärung, warum die Erstellung möglicherweise fehlgeschlagen ist.

Sie finden die Empfehlung auf der Seite **Predictions**, wo Sie sie nach Bedarf bearbeiten oder archivieren können. Empfehlungen werden automatisch einmal pro Woche (kostenpflichtig) oder pro Monat (kostenlos) neu trainiert.