---
nav_title: KI-Empfehlungen
article_title: KI-Artikelempfehlungen erstellen
description: "Dieser Artikel beschreibt, wie Sie eine KI-Artikelempfehlung für Artikel in einem Katalog erstellen."
page_order: 1
---

# KI-Artikelempfehlungen erstellen {#create-ai-item-recommendations}

> Erfahren Sie, wie Sie ein KI-Empfehlungssystem aus Artikeln in Ihrem Katalog erstellen.

## Über KI-Artikelempfehlungen {#about-ai-item-recommendations}

Verwenden Sie KI-Artikelempfehlungen, um die beliebtesten Produkte zu berechnen oder personalisierte KI-Empfehlungen für einen bestimmten [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs) zu erstellen. Nachdem Sie Ihre Empfehlung erstellt haben, können Sie Personalisierung nutzen, um diese Produkte in Ihre Nachrichten einzufügen.

{% alert tip %}
[KI-personalisierte Empfehlungen](#recommendation-types) funktionieren am besten mit mindestens einigen Hundert Katalogartikeln, höchstens 100.000 Katalogartikeln und in der Regel mindestens 30.000 Nutzer:innen mit Kauf- oder Interaktionsdaten. Dies ist nur ein grober Richtwert und kann variieren. Die anderen Empfehlungstypen können mit weniger Daten arbeiten, auch wenn **Beliebteste** als Fallback verwendet wird.
{% endalert %}

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Erstellen einer KI-Artikelempfehlung {#creating-an-ai-item-recommendation}

### Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

- Mindestens einen [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs), um einen der [Empfehlungstypen]({{site.baseurl}}/user_guide/brazeai/item_recommendations) nutzen zu können.
- Kauf- oder Event-Daten in Braze (angepasste Events, das Event „Bestellung aufgegeben“ oder das Kauf-Objekt), die eine Referenz auf den Artikel enthalten und mit den Katalog-Artikel-IDs übereinstimmen müssen.

### Schritt 1: Neue Empfehlung erstellen {#step-1-create-a-new-recommendation}

Sie können eine KI-Artikelempfehlung von zwei Stellen im Dashboard aus erstellen:

{% tabs local %}
{% tab Über das Navigationsmenü %}
1. Gehen Sie zu **Analytics** > **AI Item Recommendation**.
2. Wählen Sie **Create Prediction** > **AI Item Recommendation**.
{% endtab %}

{% tab Über einen Katalog %}
Sie können eine Empfehlung auch direkt aus einem einzelnen Katalog heraus erstellen. Wählen Sie Ihren Katalog auf der Seite **Catalogs** aus und wählen Sie dann **Create Recommendation**.
{% endtab %}
{% endtabs %}

### Schritt 2: Empfehlungsdetails hinzufügen {#step-2-add-recommendation-details}

Geben Sie Ihrer Empfehlung einen Namen und eine optionale Beschreibung.

![Schritt „Empfehlungsdetails“ mit den Feldern für Name und Beschreibung.]({% image_buster /assets/img/item_recs_1.png %})

### Schritt 3: Empfehlung definieren {#recommendation-type}

Wählen Sie einen Empfehlungstyp aus. Jeder Typ verwendet die Artikelinteraktionsdaten der letzten sechs Monate, wie z. B. Kauf-, Bestellungs- oder angepasste Event-Daten. Ausführlichere Informationen und Anwendungsfälle für jeden Typ finden Sie unter [Typen und Anwendungsfälle]({{site.baseurl}}/user_guide/brazeai/item_recommendations).

{% alert tip %}
Bei Verwendung von **Neueste** oder **KI-Personalisiert** erhalten Nutzer:innen mit unzureichenden Daten für individualisierte Empfehlungen als Fallback **Beliebteste** Artikel. Der Fallback **Beliebteste** gibt nur Artikel zurück, die im verknüpften Katalog vorhanden sind.<br><br>Für **KI-Personalisiert**-Empfehlungen können Sie die **Personalisierungsrate** auf der Seite **Analytics** einsehen, um zu erfahren, welcher Prozentsatz der Nutzer:innen, die das konfigurierte Event in den letzten 24 Monaten ausgeführt haben, personalisierte Empfehlungen in ihrem Profil gespeichert hat. Für **Neueste**-Empfehlungen zeigt die Seite **Analytics** den Anteil der Nutzer:innen, die **Neueste**-Empfehlungen erhalten, im Vergleich zum Fallback **Beliebteste**.
{% endalert %}

#### Schritt 3.1: Frühere Käufe oder Interaktionen ausschließen (optional) {#step-31-exclude-prior-purchases-or-interactions-optional}

Um zu vermeiden, dass Artikel vorgeschlagen werden, die ein:e Nutzer:in bereits gekauft oder mit denen er/sie bereits interagiert hat, wählen Sie **Do not recommend items users have previously interacted with**. Diese Option ist nur verfügbar, wenn der Empfehlungs-**Typ** auf **KI-Personalisiert** eingestellt ist.

![Schritt „Empfehlung definieren“ mit „KI-Personalisiert“ als Typ und der ausgewählten Option „Keine Artikel empfehlen, mit denen Nutzer:innen zuvor interagiert haben“.]({% image_buster /assets/img/item_recs_2-3.png %})

Diese Einstellung verhindert, dass Nachrichten Artikel wiederverwenden, die ein:e Nutzer:in bereits gekauft oder mit denen er/sie interagiert hat, sofern die Empfehlung kürzlich aktualisiert wurde. Artikel, die zwischen Empfehlungsaktualisierungen gekauft oder mit denen interagiert wurde, können weiterhin erscheinen. Bei der kostenlosen Version der Artikelempfehlungen erfolgen Aktualisierungen wöchentlich. Bei der Pro-Version der KI-Artikelempfehlungen erfolgen Aktualisierungen alle 24 Stunden.

Wenn beispielsweise bei Verwendung der Pro-Version der KI-Artikelempfehlungen ein:e Nutzer:in etwas kauft und dann innerhalb von 30 Minuten eine Marketing-E-Mail erhält, ist der gerade gekaufte Artikel möglicherweise nicht rechtzeitig aus der E-Mail ausgeschlossen. Nachrichten, die nach 24 Stunden gesendet werden, enthalten diesen Artikel jedoch nicht mehr.

#### Schritt 3.2: Katalog auswählen {#step-32-select-a-catalog}

Falls noch nicht ausgefüllt, wählen Sie den [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs) aus, aus dem diese Empfehlung Artikel beziehen soll.

#### Schritt 3.3: Auswahl hinzufügen (optional) {#step-33-add-a-selection-optional}

Wenn Sie mehr Kontrolle über Ihre Empfehlung wünschen, wählen Sie eine [Auswahl]({{site.baseurl}}/user_guide/data/activation/catalogs/selections), um angepasste Filter anzuwenden. Auswahlen filtern Empfehlungen nach bestimmten Spalten in Ihrem Katalog, wie z. B. Marke, Größe oder Standort. Auswahlen, die Liquid enthalten, können nicht in Ihrer Empfehlung verwendet werden.

![Ein Beispiel für die ausgewählte Auswahl „auf Lager“ für die Empfehlung.]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
Wenn Sie Ihre Auswahl nicht finden können, stellen Sie sicher, dass sie zuerst in Ihrem Katalog eingerichtet ist.
{% endalert %}

### Schritt 4: Interaktion für die Empfehlungen auswählen {#step-4-select-the-interaction-to-drive-recommendations}

Wählen Sie das Event aus, für das diese Empfehlung optimiert werden soll. Dieses Event ist in der Regel ein Kauf, kann aber auch jede andere Interaktion mit einem Artikel sein.

{% alert tip %}
Bei der Konfiguration von KI-Artikelempfehlungen ist die Wahl des Events wichtig. Ihr auslösendes Event bestimmt, wer eine KI-generierte Empfehlung erhält – KI-Artikelempfehlungen werden für Nutzer:innen generiert, die das von Ihnen konfigurierte Event abgeschlossen haben, sodass diese Wahl direkt bestimmt, wer Empfehlungen erhält. Wählen Sie ein Event, das das gesamte Zielgruppensegment abdeckt, das Sie erreichen möchten.<br><br>Gleichzeitig sollten Sie Abdeckung und Relevanz abwägen. Events am oberen Ende des Funnels (wie „Produkt angesehen“) erfassen tendenziell eine breitere Zielgruppe, sind aber weniger mit Geschäftsergebnissen verbunden, während Events am unteren Ende des Funnels (wie „Gekauft“) tendenziell gezieltere, geschäftsrelevantere Empfehlungen erzeugen. Das beste Event ist eines, das Abdeckung und Einfluss auf das Geschäftsergebnis in Einklang bringt.
{% endalert %}

Sie können optimieren für:

- Kauf-Events mit dem [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object)
- Angepasste Events, die einen Kauf darstellen
- Angepasste Events, die eine andere Artikelinteraktion darstellen (wie Produktansichten, Klicks oder Medienwiedergaben)
- Aufgegebene Bestellungen mit dem [Event „Bestellung aufgegeben“]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.order_placed)

Wenn Sie **Angepasstes Event** wählen, wählen Sie Ihr Event aus der Liste aus.

![Das angepasste Event „purchase“ als aktuell konfigurierte Event-Erfassung ausgewählt.]({% image_buster /assets/img/item_recs_3.png %})

{% alert note %}
Angepasste Events müssen über ausreichend Daten verfügen, bevor sie in der Event-Liste erscheinen. Wenn Ihr angepasstes Event nicht angezeigt wird, liegt es möglicherweise daran, dass das Braze-Backend es noch nicht verarbeitet hat oder es nicht genügend Daten für das Modelltraining gibt. KI-Empfehlungen basieren auf historischen Daten, um Insights zu generieren, daher sind neu erstellte oder selten ausgelöste Events erst verfügbar, wenn mehr Daten gesammelt wurden.
{% endalert %}

### Schritt 5: Entsprechenden Eigenschaftsnamen auswählen {#property-name}

Um eine Empfehlung zu erstellen, müssen Sie Braze mitteilen, welches Feld Ihres Interaktions-Events (Event „Bestellung aufgegeben“, Kauf-Objekt oder angepasstes Event) den eindeutigen Bezeichner enthält, der mit dem `id`-Feld eines Artikels im Katalog übereinstimmt. Nicht sicher? [Anforderungen anzeigen](#requirements).

Wählen Sie dieses Feld für den **Eigenschaftsnamen** aus.

Das Feld **Eigenschaftsname** wird vorab mit einer Liste von Feldern befüllt, die über das SDK an Braze gesendet werden. Wenn genügend Daten vorhanden sind, werden diese Eigenschaften auch nach Wahrscheinlichkeit sortiert, die richtige Eigenschaft zu sein. Wählen Sie diejenige aus, die dem `id`-Feld des Katalogs entspricht.

![Der Eigenschaftsname „purchase_item“ ausgewählt, der den Artikel-IDs im Katalog entspricht.]({% image_buster /assets/img/item_recs_4.png %})

#### Anforderungen {#requirements}

Es gibt einige Anforderungen für die Auswahl Ihrer Eigenschaft:

- Muss dem `id`-Feld Ihres ausgewählten Katalogs zugeordnet sein.
- **Wenn Sie das Event „Bestellung aufgegeben“ ausgewählt haben oder [E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) zum Trainieren von Artikelempfehlungen verwenden:** Geben Sie `products.product_id` für die Produkt-ID ein.
  - Das Feld kann sich in einem Array von Produkten befinden oder mit einem Array von IDs enden. In beiden Fällen wird jede Produkt-ID als separates, sequenzielles Event mit demselben Zeitstempel behandelt.
- **Wenn Sie das Kauf-Objekt ausgewählt haben:** Muss die `product_id` oder ein Feld der `properties` Ihres Interaktions-Events sein.
- **Wenn Sie ein angepasstes Event ausgewählt haben:** Muss ein Feld der `properties` Ihres angepassten Events sein.
- Verschachtelte Felder müssen im Dropdown **Eigenschaftsname** in Punktnotation im Format `event_property.nested_property` eingegeben werden. Wenn Sie beispielsweise die verschachtelte Eigenschaft `district_name` innerhalb der Event-Eigenschaft `location` auswählen, geben Sie `location.district_name` ein.

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

Angenommen, Sie möchten das angepasste Event `added_to_cart` verwenden, um ähnliche Produkte zu empfehlen, bevor die geschäftskunden zur Kasse geht. Das Event `added_to_cart` hat eine Event-Eigenschaft `product_sku`.

Dann muss die Eigenschaft `product_sku` mindestens einen der Werte aus der Spalte `id` im Beispielkatalog enthalten: „ADI-BL-7“, „ADI-RD-8“, „ADI-WH-9“ oder „ADI-PP-10“. Sie benötigen nicht für jeden Katalogartikel Events, aber Sie brauchen einige davon, damit das Empfehlungssystem genügend Inhalte hat, um damit zu arbeiten.

##### Beispiel für ein angepasstes Event-Objekt {#example-custom-event-object}

Dieses Event hat `"product_sku": "ADI-BL-7"`, was dem ersten Artikel im Beispielkatalog entspricht.

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

Wenn Ihre Event-Eigenschaften mehrere Produkte in einem Array enthalten, wird jede Produkt-ID als separates, sequenzielles Event behandelt. Dieses Event kann die Eigenschaft `products.sku` verwenden, um den ersten und dritten Artikel im Beispielkatalog zuzuordnen.

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

Wenn Ihre Produkt-IDs Werte in einem Array statt Objekte sind, können Sie dieselbe Notation verwenden, und jede Produkt-ID wird als separates, sequenzielles Event behandelt. Dies kann flexibel mit verschachtelten Objekten im folgenden Event kombiniert werden, indem die Eigenschaft als `purchase.product_skus` konfiguriert wird, um den ersten und dritten Artikel im Beispielkatalog zuzuordnen.

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

In Bezug auf die Zuordnung gilt für Kauf-Objekte eine ähnliche Logik wie für angepasste Events, außer dass Sie zwischen der `product_id` des Kauf-Objekts oder einem Feld im `properties`-Objekt wählen können.

Denken Sie daran, dass Sie nicht für jeden Katalogartikel Events benötigen, aber Sie brauchen einige davon, damit das Empfehlungssystem genügend Inhalte hat, um damit zu arbeiten.

##### Beispiel für ein Kauf-Objekt, das der Produkt-ID zugeordnet ist {#example-purchase-object-mapped-to-product-id}

Dieses Event hat `"product_id": "ADI-BL-7"`, was dem ersten Artikel im Katalog zugeordnet ist.

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

Dieses Event hat eine Eigenschaft `"sku": "ADI-RD-8"`, die dem zweiten Artikel im Katalog zugeordnet ist.

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

##### Beispiel für ein Objekt „Bestellung aufgegeben“, das der Produkt-ID zugeordnet ist {#example-order-placed-object-mapped-to-product-id}

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

Wenn Sie bereit sind, wählen Sie **Create Recommendation**. Dieser Vorgang kann zwischen 10 Minuten und 36 Stunden dauern. Sie erhalten eine E-Mail-Benachrichtigung, wenn die Empfehlung erfolgreich trainiert wurde, oder eine Erklärung, warum die Erstellung möglicherweise fehlgeschlagen ist.

Sie finden die Empfehlung auf der Seite **Predictions**, wo Sie sie nach Bedarf bearbeiten oder archivieren können. Empfehlungen werden automatisch einmal pro Woche (kostenpflichtig) oder einmal pro Monat (kostenlos) neu trainiert.