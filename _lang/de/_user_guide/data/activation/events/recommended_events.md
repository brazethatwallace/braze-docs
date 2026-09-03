---
nav_title: Empfohlene Events
article_title: Empfohlene Events
alias: /recommended_events/
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt empfohlene Events – Empfehlungen von Braze für E-Commerce-Events."
---

# Empfohlene Events {#recommended-events}

> Empfohlene Events basieren auf einem Framework, das standardisierte angepasste Events mit definierten JSON-Schemata sendet. Wenn Sie ein empfohlenes Event senden, validiert Braze es bei der Aufnahme gegen sein Schema und wendet eine spezialisierte Nachbearbeitung an – wie automatische Feldberechnungen oder Warenkorb-Verwaltung –, die generische angepasste Events nicht erhalten. Für bestimmte branchenspezifische Event-Sets unterstützt Braze außerdem eine spezielle Behandlung, wie z. B. dedizierte aktionsbasierte Trigger für Campaigns und Canvases.

## Empfohlene E-Commerce-Events {#ecommerce-recommended-events}

[Empfohlene E-Commerce-Events]({{site.baseurl}}/ecommerce_events) decken sechs Schritte der Kaufreise ab: `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled` und `order_refunded`. Wenn Sie diese Events erfolgreich senden, validiert Braze die Daten und stellt sie einer wachsenden Anzahl von Plattform-Features zur Verfügung.

Zu diesen Features gehören Canvas-Templates für abgebrochenes Browsen, Warenkorb-Abbruch, abgebrochenen Checkout und Bestellbestätigungs-Flows; E-Commerce-Reporting; und berechnete Nutzerprofilfelder für _Gesamtumsatz_, _Gesamtbestellungen_ und _Gesamterstattungen_. Sie können außerdem Segmente mithilfe verschachtelter Produkteigenschafts-Filterung über [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension) erstellen, Warenkorb-Abbruch-Nachrichten mit dem {% raw %}`{% shopping_cart %}`{% endraw %} Liquid-Tag personalisieren und BrazeAI<sup>TM</sup>-Funktionen wie [Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events), [voraussichtliche Abwanderung]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) und [Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/item_recommendations) sowie weitere Funktionen nutzen.

Da diese Events einem definierten Schema folgen, kann jedes unterstützte Feature die strukturierten Daten ohne angepasstes Property-Mapping oder Feature-spezifische Konfiguration auf Ihrer Seite lesen.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

### So funktionieren E-Commerce-Events {#how-ecommerce-events-work}

E-Commerce-Events sind angepasste Events mit vordefinierten Namen und Eigenschafts-Schemas. Sie senden sie über das [Braze SDK]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events), den [`/users/track` REST API-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) oder [Cloud Data Ingestion (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion), und Braze validiert jedes Event bei der Aufnahme gegen sein Schema. Wenn die Validierung erfolgreich ist, wendet Braze automatisch eine für diesen Event-Typ spezifische Nachverarbeitung an, wie z. B. die Berechnung von Umsatzfeldern und die Verwaltung des Warenkorb-Status in Nutzerprofilen.

{% alert note %}
CSV-Uploads unterstützen keine E-Commerce-Events. Verwenden Sie das SDK, `/users/track` oder CDI, um diese Events zu senden.
{% endalert %}

E-Commerce-Events funktionieren überall dort, wo auch andere angepasste Events funktionieren: Trigger und Filter für durchgeführte angepasste Events, Reporting für angepasste Events und mehr. Ihre Schema-Validierung schaltet jedoch zusätzliche Funktionen frei, darunter:

- Trigger-Aktionen „Gibt Bestellung auf“ in Campaigns, Canvases, Aktionspfaden, In-App-Nachricht-Triggern und Content-Card-Entfernung
- Berechnete E-Commerce-Nutzerprofilfelder (**Gesamtumsatz**, **Gesamtbestellungen**, **Gesamterstattungen**)
- Warenkorb-Status-Verwaltung für Warenkorb-Abbruch-Flows
- Umfangreichere Daten für BrazeAI<sup>TM</sup>-Features wie Predictive Events, voraussichtliche Abwanderung und Artikelempfehlungen

Sie können E-Commerce-Events auch überall dort namentlich referenzieren, wo die Plattform angepasste Events unterstützt. Zum Beispiel können Sie eine aktionsbasierte Campaign mit `ecommerce.product_viewed`-Events triggern, ein Segment erstellen, das nach `ecommerce.checkout_started`-Events filtert, oder `ecommerce.order_placed`-Events über Currents exportieren.

#### Event-Benennung {#event-naming}

Event-Namen sind exakt, Groß-/Kleinschreibung wird beachtet, und sie sind durch Punkte getrennt. Verwenden Sie immer das kanonische Format. Wenn ein Event-Name nicht exakt einem der sechs kanonischen Namen entspricht, behandelt Braze ihn als Standard-Event und es findet keine E-Commerce-Nachverarbeitung statt.

Sie können Events nicht anpassen oder umbenennen.

- **Korrekt:** `ecommerce.order_placed`
- **Falsch:** `order.placed`, `eCommerce_order_placed`, `Order_Placed`

#### Event-Schemas {#event-schemas}

Die sechs empfohlenen E-Commerce-Events bilden Phasen der Kaufreise ab. Lösen Sie jedes Event in dem Moment aus, in dem die Nutzer:innen die entsprechende Aktion abschließen.

![Diagramm der Nutzerreise durch alle sechs empfohlenen E-Commerce-Events: product_viewed, cart_updated, checkout_started, order_placed, order_cancelled und order_refunded.]({% image_buster /assets/img/shopify/event_schemas.png %})

{% alert tip %}
Die folgenden Beispiele zeigen den REST API-Payload für jedes Event.
Für die clientseitige Protokollierung verwenden `ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started` und `ecommerce.order_placed` die SDK-E-Commerce-Event-APIs, sofern verfügbar, während `ecommerce.order_cancelled` und `ecommerce.order_refunded` `logCustomEvent` verwenden. Plattformspezifische Implementierungsbeispiele finden Sie unter [E-Commerce-Events über das Braze SDK protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).
{% endalert %}

{% tabs %}
{% tab ecommerce.product_viewed %}

Lösen Sie dieses Event aus, wenn Nutzer:innen eine Produktdetailseite aufrufen. Dieses Event ist kompatibel mit den Braze-Katalog-Features [Wieder-verfügbar-Benachrichtigungen]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) und [Preissenkungsbenachrichtigungen]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications).

#### Clientseitige Implementierung {#client-side-implementation}

Verwenden Sie die SDK-E-Commerce-Event-APIs, sofern verfügbar. Plattformspezifische Implementierungsbeispiele finden Sie unter [E-Commerce-Events über das Braze SDK protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

#### Event-Eigenschaften {#event-properties}

| Eigenschaftsname | Datentyp | Erforderlich | Beschreibung |
| -------------- | ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product_id` | String | Ja | Eindeutiger Produktbezeichner (z. B. SKU oder Artikel-ID). |
| `product_name` | String | Ja | Anzeigename des Produkts. |
| `variant_id` | String | Ja | Produktvarianten-Bezeichner (z. B. `shirt_medium_blue`). |
| `image_url` | String | Nein | Produktbild-URL. |
| `product_url` | String | Nein | URL zur Produktseite für weitere Details. |
| `price` | Gleitkommazahl | Ja | Varianten-Stückpreis zum Zeitpunkt der Ansicht. |
| `currency` | String | Ja | Dreistelliger ISO-4217-Code (z. B. `USD` oder `EUR`). |
| `source` | String | Ja | Quelle, von der das Event stammt (z. B. `web`, `ios` oder `android`). |
| `type` | String-Array | Nein | Erforderlich, um die Braze-Katalog-Trigger-Features für Wieder-verfügbar- und Preissenkungsbenachrichtigungen zu nutzen. Akzeptierte Werte: `"price_drop"`, `"back_in_stock"` |
| `metadata` | Object | Nein | Flexible Schlüssel-Wert-Paare (z. B. `category` oder `brand`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event-Eigenschaften" }

#### REST API-Beispiel {#rest-api-example}

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.product_viewed",
      "time": "2026-04-28T14:22:11Z",
      "properties": {
        "product_id": "SKU-RUN-4821",
        "product_name": "Ultraboost Running Shoe",
        "variant_id": "UB-BLK-11",
        "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
        "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
        "price": 189.99,
        "currency": "USD",
        "source": "web",
        "type": ["price_drop", "back_in_stock"],
        "metadata": {
          "category": "Running Shoes",
          "brand": "Shoe Brand"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.cart_updated %}

Lösen Sie dieses Event jedes Mal aus, wenn sich der Inhalt des Warenkorbs ändert.

#### Clientseitige Implementierung

Verwenden Sie die SDK-E-Commerce-Event-APIs, sofern verfügbar. Plattformspezifische Implementierungsbeispiele finden Sie unter [E-Commerce-Events über das Braze SDK protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

Sie können dieses Event auf zwei Arten senden:

- **Vollständiger Warenkorb-Ersatz:** Lassen Sie `action` weg oder setzen Sie `action` auf `replace`. Fügen Sie den vollständigen Satz an Positionen in `products` mit absoluten Mengen (Gesamteinheiten pro Variante im Warenkorb) ein. Sie müssen `total_value` angeben.
- **Inkrementelle Warenkorb-Aktualisierungen:** Setzen Sie `action` auf `add` oder `remove`. Fügen Sie nur die geänderten Positionen ein. Jede `quantity` ist die Anzahl der hinzuzufügenden oder zu entfernenden Einheiten, nicht die Gesamtmenge im Warenkorb. Bei `add` erhöht Braze die Positionsmenge oder fügt eine neue Position hinzu. Bei `remove` verringert Braze die Positionsmenge und entfernt die Position, wenn die Menge `0` erreicht. `total_value` ist bei `add` und `remove` optional.

{% alert warning %}
Verwenden Sie entweder inkrementelle Warenkorb-Aktualisierungen (`add` oder `remove`) oder vollständigen Ersatz (kein `action` oder `replace`) für einen bestimmten Warenkorb. Das Mischen beider Ansätze für dieselbe `cart_id` wird nicht empfohlen und kann zu einem inkonsistenten Warenkorb-Status in Braze führen.
{% endalert %}

Um Messaging über dieses Event auszulösen, verwenden Sie den Trigger **Warenkorb-Aktualisierungs-Event durchführen** in Canvas und Campaigns. Dieser Trigger enthält eine spezielle Behandlung, um zu verhindern, dass der Warenkorb im Shopping-Funnel weiter fortschreitet.

{% alert tip %}
Der Warenkorb erstellt ein Warenkorb-Mapping-Objekt im Kundenprofil, das den {% raw %}`{% shopping_cart %}`{% endraw %} Liquid-Tag unterstützt. Der Warenkorb läuft nach 30 Tagen ohne Aktualisierung ab. Wenn zwei Nutzerprofile zusammengeführt werden, behält Braze beide Warenkörbe bei.
{% endalert %}

#### Event-Eigenschaften

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
|-----------------|-----------|----------|-------------------------------------------------------------------------------------------------------------------------------|
| `cart_id` | String | Ja | Eindeutiger Bezeichner für den Warenkorb. Wird über Warenkorb-, Checkout- und Bestell-Events für das Warenkorb-Mapping der Nutzer:innen geteilt. |
| `action` | String | Nein | `add` (Menge erhöhen oder Position hinzufügen), `remove` (Menge verringern; Position wird bei `0` entfernt) oder `replace` (vollständiger Warenkorb-Ersatz, identisch mit dem Weglassen von `action`). |
| `total_value` | Gleitkommazahl | Bedingt | Erforderlich, wenn `action` weggelassen wird oder `replace` ist. Optional, wenn `action` `add` oder `remove` ist. |
| `subtotal_value` | Gleitkommazahl | Nein | Zwischensumme des Warenkorbs (nach Rabatt, vor Steuern/Versand). |
| `tax` | Gleitkommazahl | Nein | Gesamtsteuer auf den Warenkorb. |
| `shipping` | Gleitkommazahl | Nein | Gesamtversandkosten für den Warenkorb. |
| `currency` | String | Ja | Dreistelliger ISO-4217-Code. |
| `products` | Array | Ja | Positionen für diese Aktualisierung. Für vollständigen Ersatz (kein `action` oder `replace`) den vollständigen Warenkorb mit absoluten Mengen angeben. Für `add` oder `remove` nur geänderte Positionen angeben; siehe Produkteigenschaften. |
| `source` | String | Ja | Quelle, von der das Event stammt. |
| `metadata` | Object | Nein | Flexible Schlüssel-Wert-Paare für zusätzliche Daten auf Event-Ebene. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event-Eigenschaften" }

#### Produkteigenschaften (`products[]`) {#product-properties-products}

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
|-----------------|-----------|----------|-------------------------------------------------|
| `product_id` | String | Ja | Eindeutiger Produktbezeichner. |
| `product_name` | String | Ja | Anzeigename des Produkts. |
| `variant_id` | String | Ja | Varianten-Bezeichner. |
| `image_url` | String | Nein | Produktbild-URL. |
| `product_url` | String | Nein | URL zur Produktseite. |
| `quantity` | Integer | Ja | Für vollständigen Ersatz (kein `action` oder `replace`) die Einheiten im Warenkorb für diese Position. Für `add` oder `remove` die Anzahl der hinzuzufügenden oder zu entfernenden Einheiten. |
| `price` | Gleitkommazahl | Ja | Varianten-Stückpreis. |
| `metadata` | Object | Nein | Flexible Schlüssel-Wert-Paare (z. B. `color` oder `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Produkteigenschaften (products[])" }

{% comment %}

{% subtabs local %}
{% subtab Web %}

##### `add`

`add` erhöht die Menge oder fügt eine neue Position hinzu. Die Eigenschaft `quantity` gibt an, wie viele Einheiten hinzugefügt werden sollen.

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
  cart_id: "cart_abc123",
  action: "add",
  currency: "USD",
  source: "web",
  products: [
    {
      product_id: "SKU-RUN-4821",
      product_name: "Ultraboost Running Shoe",
      variant_id: "UB-BLK-11",
      quantity: 1,
      price: 189.99,
    },
  ],
});
```
##### `remove`

`remove` verringert die Menge um den Wert in `quantity`. Die Position wird entfernt, wenn die Menge `0` erreicht.

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
  cart_id: "cart_abc123",
  action: "remove",
  currency: "USD",
  source: "web",
  products: [
    {
      product_id: "SKU-SOC-1102",
      product_name: "Performance Running Socks",
      variant_id: "SOC-WHT-L",
      quantity: 1,
      price: 14.99,
    },
  ],
});
```

##### `replace`

`replace` (oder `action` weglassen) sendet den vollständigen Warenkorb. `total_value` ist erforderlich.

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
  cart_id: "cart_abc123",
  action: "replace",
  total_value: 234.96,
  currency: "USD",
  source: "web",
  products: [
    {
      product_id: "SKU-RUN-4821",
      product_name: "Ultraboost Running Shoe",
      variant_id: "UB-BLK-11",
      image_url: "https://cdn.example.com/shoes/ub-blk-11.jpg",
      product_url: "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
      quantity: 1,
      price: 189.99,
    },
    {
      product_id: "SKU-SOC-1102",
      product_name: "Performance Running Socks",
      variant_id: "SOC-WHT-L",
      image_url: "https://cdn.example.com/socks/soc-wht-l.jpg",
      product_url: "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
      quantity: 2,
      price: 14.99,
    },
  ],
});
```

{% endsubtab %}
{% subtab Android %}

##### Add

`add` erhöht die Menge oder fügt eine neue Position hinzu. Die Eigenschaft `quantity` gibt an, wie viele Einheiten hinzugefügt werden sollen.

```text
Kotlin

// add — units to add
Braze.getInstance(context).logCustomEvent(
  "ecommerce.cart_updated",
  BrazeProperties(
    JSONObject()
      .put("cart_id", "cart_abc123")
      .put("action", "add")
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
  ),
)

JavaScript

// add — units to add
Braze.getInstance(context).logCustomEvent(
    "ecommerce.cart_updated",
    new BrazeProperties(new JSONObject()
        .put("cart_id", "cart_abc123")
        .put("action", "add")
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

##### Remove

`remove` verringert die Menge um den Wert in `quantity`. Die Position wird entfernt, wenn die Menge `0` erreicht.

```text
Kotlin

// remove — units to remove
Braze.getInstance(context).logCustomEvent(
  "ecommerce.cart_updated",
  BrazeProperties(
    JSONObject()
      .put("cart_id", "cart_abc123")
      .put("action", "remove")
      .put("currency", "USD")
      .put("source", "android")
      .put(
        "products",
        JSONArray().put(
          JSONObject()
            .put("product_id", "SKU-SOC-1102")
            .put("product_name", "Performance Running Socks")
            .put("variant_id", "SOC-WHT-L")
            .put("quantity", 1)
            .put("price", 14.99),
        ),
      ),
  ),
)

JavaScript

// remove — units to remove
Braze.getInstance(context).logCustomEvent(
    "ecommerce.cart_updated",
    new BrazeProperties(new JSONObject()
        .put("cart_id", "cart_abc123")
        .put("action", "remove")
        .put("currency", "USD")
        .put("source", "android")
        .put("products", new JSONArray()
            .put(new JSONObject()
                .put("product_id", "SKU-SOC-1102")
                .put("product_name", "Performance Running Socks")
                .put("variant_id", "SOC-WHT-L")
                .put("quantity", 1)
                .put("price", 14.99)))));
```

##### Replace

`replace` (oder `action` weglassen) sendet den vollständigen Warenkorb. `total_value` ist erforderlich.

```text
Kotlin

// replace — full cart; total_value required
Braze.getInstance(context).logCustomEvent(
  "ecommerce.cart_updated",
  BrazeProperties(
    JSONObject()
      .put("cart_id", "cart_abc123")
      .put("action", "replace")
      .put("total_value", 234.96)
      .put("currency", "USD")
      .put("source", "android")
      .put(
        "products",
        JSONArray()
          .put(
            JSONObject()
              .put("product_id", "SKU-RUN-4821")
              .put("product_name", "Ultraboost Running Shoe")
              .put("variant_id", "UB-BLK-11")
              .put("quantity", 1)
              .put("price", 189.99),
          )
          .put(
            JSONObject()
              .put("product_id", "SKU-SOC-1102")
              .put("product_name", "Performance Running Socks")
              .put("variant_id", "SOC-WHT-L")
              .put("quantity", 2)
              .put("price", 14.99),
          ),
      ),
  ),
)

JavaScript

// replace — full cart; total_value required
Braze.getInstance(context).logCustomEvent(
    "ecommerce.cart_updated",
    new BrazeProperties(new JSONObject()
        .put("cart_id", "cart_abc123")
        .put("action", "replace")
        .put("total_value", 234.96)
        .put("currency", "USD")
        .put("source", "android")
        .put("products", new JSONArray()
            .put(new JSONObject()
                .put("product_id", "SKU-RUN-4821")
                .put("product_name", "Ultraboost Running Shoe")
                .put("variant_id", "UB-BLK-11")
                .put("quantity", 1)
                .put("price", 189.99))
            .put(new JSONObject()
                .put("product_id", "SKU-SOC-1102")
                .put("product_name", "Performance Running Socks")
                .put("variant_id", "SOC-WHT-L")
                .put("quantity", 2)
                .put("price", 14.99)))));
```

{% endsubtab %}
{% subtab Swift %}

##### Add

`add` erhöht die Menge oder fügt eine neue Position hinzu. Die Eigenschaft `quantity` gibt an, wie viele Einheiten hinzugefügt werden sollen.

```text
Swift

// add — units to add
AppDelegate.braze?.logCustomEvent(
  name: "ecommerce.cart_updated",
  properties: [
    "cart_id": "cart_abc123",
    "action": "add",
    "currency": "USD",
    "source": "ios",
    "products": [
      [
        "product_id": "SKU-RUN-4821",
        "product_name": "Ultraboost Running Shoe",
        "variant_id": "UB-BLK-11",
        "quantity": 1,
        "price": 189.99,
      ],
    ],
  ]
)

Objective-C

// add — units to add
[AppDelegate.braze logCustomEvent:@"ecommerce.cart_updated"
                       properties:@{
  @"cart_id": @"cart_abc123",
  @"action": @"add",
  @"currency": @"USD",
  @"source": @"ios",
  @"products": @[@{
    @"product_id": @"SKU-RUN-4821",
    @"product_name": @"Ultraboost Running Shoe",
    @"variant_id": @"UB-BLK-11",
    @"quantity": @1,
    @"price": @189.99,
  }],
}];
```

##### Remove

`remove` verringert die Menge um den Wert in `quantity`. Die Position wird entfernt, wenn die Menge `0` erreicht.

```text
Swift

// remove — units to remove
AppDelegate.braze?.logCustomEvent(
  name: "ecommerce.cart_updated",
  properties: [
    "cart_id": "cart_abc123",
    "action": "remove",
    "currency": "USD",
    "source": "ios",
    "products": [
      [
        "product_id": "SKU-SOC-1102",
        "product_name": "Performance Running Socks",
        "variant_id": "SOC-WHT-L",
        "quantity": 1,
        "price": 14.99,
      ],
    ],
  ]
)

Objective-C

// remove — units to remove
[AppDelegate.braze logCustomEvent:@"ecommerce.cart_updated"
                       properties:@{
  @"cart_id": @"cart_abc123",
  @"action": @"remove",
  @"currency": @"USD",
  @"source": @"ios",
  @"products": @[@{
    @"product_id": @"SKU-SOC-1102",
    @"product_name": @"Performance Running Socks",
    @"variant_id": @"SOC-WHT-L",
    @"quantity": @1,
    @"price": @14.99,
  }],
}];
```

##### Replace

`replace` (oder `action` weglassen) sendet den vollständigen Warenkorb. `total_value` ist erforderlich.

```text
Swift

// replace — full cart; total_value required
AppDelegate.braze?.logCustomEvent(
  name: "ecommerce.cart_updated",
  properties: [
    "cart_id": "cart_abc123",
    "action": "replace",
    "total_value": 234.96,
    "currency": "USD",
    "source": "ios",
    "products": [
      [
        "product_id": "SKU-RUN-4821",
        "product_name": "Ultraboost Running Shoe",
        "variant_id": "UB-BLK-11",
        "quantity": 1,
        "price": 189.99,
      ],
      [
        "product_id": "SKU-SOC-1102",
        "product_name": "Performance Running Socks",
        "variant_id": "SOC-WHT-L",
        "quantity": 2,
        "price": 14.99,
      ],
    ],
  ]
)

Objective-C

// replace — full cart; total_value required
[AppDelegate.braze logCustomEvent:@"ecommerce.cart_updated"
                       properties:@{
  @"cart_id": @"cart_abc123",
  @"action": @"replace",
  @"total_value": @234.96,
  @"currency": @"USD",
  @"source": @"ios",
  @"products": @[
    @{
      @"product_id": @"SKU-RUN-4821",
      @"product_name": @"Ultraboost Running Shoe",
      @"variant_id": @"UB-BLK-11",
      @"quantity": @1,
      @"price": @189.99,
    },
    @{
      @"product_id": @"SKU-SOC-1102",
      @"product_name": @"Performance Running Socks",
      @"variant_id": @"SOC-WHT-L",
      @"quantity": @2,
      @"price": @14.99,
    },
  ],
}];
```

{% endsubtab %}
{% subtab REST API %}

##### `add`

`add` erhöht die Menge oder fügt eine neue Position hinzu. Die Eigenschaft `quantity` gibt an, wie viele Einheiten hinzugefügt werden sollen.

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.cart_updated",
      "time": "2026-04-28T14:25:33Z",
      "properties": {
        "cart_id": "cart_abc123",
        "action": "add",
        "currency": "USD",
        "source": "web",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "quantity": 1,
            "price": 189.99
          }
        ]
      }
    }
  ]
}
```

##### `remove`

`remove` verringert die Menge um den Wert in `quantity`. Die Position wird entfernt, wenn die Menge `0` erreicht.

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.cart_updated",
      "time": "2026-04-28T14:26:10Z",
      "properties": {
        "cart_id": "cart_abc123",
        "action": "remove",
        "currency": "USD",
        "source": "web",
        "products": [
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "quantity": 1,
            "price": 14.99
          }
        ]
      }
    }
  ]
}
```

##### `replace`

`replace` (oder `action` weglassen) sendet den vollständigen Warenkorb. `total_value` ist erforderlich.

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.cart_updated",
      "time": "2026-04-28T14:27:00Z",
      "properties": {
        "cart_id": "cart_abc123",
        "action": "replace",
        "total_value": 234.96,
        "subtotal_value": 219.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
            "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "cart_source": "product_page_atc_button"
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endcomment %}

{% endtab %}
{% tab ecommerce.checkout_started %}

Lösen Sie dieses Event aus, wenn Nutzer:innen den Checkout-Flow starten (z. B. „Zur Kasse“ auswählen oder auf der Checkout-Seite landen).

#### Clientseitige Implementierung

Verwenden Sie die SDK-E-Commerce-Event-APIs, sofern verfügbar. Plattformspezifische Implementierungsbeispiele finden Sie unter [E-Commerce-Events über das Braze SDK protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

#### Event-Eigenschaften

| Eigenschaft | Typ | Erforderlich | Beschreibung |
|----------------|---------|----------|------------------------------------------------------------------------------------------------------------------|
| checkout_id | String | Ja | Eindeutiger Bezeichner für die Checkout-Sitzung. |
| cart_id | String | Nein | Warenkorb-Bezeichner. Wird über Warenkorb-, Checkout- und Bestell-Events für das Warenkorb-Mapping der Nutzer:innen geteilt. |
| total_value | Gleitkommazahl | Ja | Gesamtgeldwert des Checkouts. |
| subtotal_value | Gleitkommazahl | Nein | Zwischensumme (nach Rabatt, vor Steuern/Versand). |
| tax | Gleitkommazahl | Nein | Gesamtsteuer auf den Checkout. |
| shipping | Gleitkommazahl | Nein | Gesamtversandkosten. |
| currency | String | Ja | Dreistelliger ISO-4217-Code. |
| products | Array | Ja | Artikel im Checkout. Siehe Produkteigenschaften-Untertabelle. |
| source | String | Ja | Quelle, von der das Event stammt. |
| metadata | Object | Nein | Flexible Schlüssel-Wert-Paare. Erkannte Untereigenschaft: `checkout_url` (String) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event-Eigenschaften" }

#### Produkteigenschaften (`products[]`)

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
|----------------|-----------|----------|----------------------------------------------------------|
| `product_id` | String | Ja | Eindeutiger Produktbezeichner. |
| `product_name` | String | Ja | Anzeigename des Produkts. |
| `variant_id` | String | Ja | Varianten-Bezeichner. |
| `image_url` | String | Nein | Produktbild-URL. |
| `product_url` | String | Nein | URL zur Produktseite. |
| `quantity` | Integer | Ja | Anzahl der Einheiten im Warenkorb. |
| `price` | Gleitkommazahl | Ja | Varianten-Stückpreis. |
| `metadata` | Object | Nein | Flexible Schlüssel-Wert-Paare (z. B. Farbe, Größe). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Produkteigenschaften (products[])" }

#### REST API-Beispiel

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.checkout_started",
      "time": "2026-04-28T14:30:05Z",
      "properties": {
        "checkout_id": "chk_88291",
        "cart_id": "cart_abc123",
        "total_value": 234.96,
        "subtotal_value": 219.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
            "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "checkout_url": "https://www.example.com/checkout/chk_88291",
          "checkout_type": "express"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.order_placed %}

Lösen Sie dieses Event aus, wenn eine Bestellung erfolgreich abgeschlossen oder die Zahlung bestätigt wird.

#### Clientseitige Implementierung

Verwenden Sie die SDK-E-Commerce-Event-APIs, sofern verfügbar. Plattformspezifische Implementierungsbeispiele finden Sie unter [E-Commerce-Events über das Braze SDK protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

{% alert important %}
Dieses Event ist der primäre Umsatztreiber. Es erhöht `total_revenue` um den Wert in `total_value` und `total_orders` um 1 im Kundenprofil.
{% endalert %}

#### Event-Eigenschaften

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
|-----------------|-----------|----------|-----------------------------------------------------------------------------------------------|
| `order_id` | String | Ja | Eindeutiger Bezeichner für die Bestellung. |
| `cart_id` | String | Nein | Warenkorb-Bezeichner. Wird über Warenkorb-, Checkout- und Bestell-Events für das Warenkorb-Mapping der Nutzer:innen geteilt. |
| `total_value` | Gleitkommazahl | Ja | Gesamtgeldwert der Bestellung. |
| `subtotal_value` | Gleitkommazahl | Nein | Zwischensumme (nach Rabatt, vor Steuern/Versand). |
| `tax` | Gleitkommazahl | Nein | Gesamtsteuer auf die Bestellung. |
| `shipping` | Gleitkommazahl | Nein | Gesamtversandkosten. |
| `currency` | String | Ja | Dreistelliger ISO-4217-Code. |
| `total_discounts` | Gleitkommazahl | Nein | Gesamtbetrag der auf die Bestellung angewendeten Rabatte. |
| `discounts` | Array | Nein | Detaillierte Liste der angewendeten Rabatte. |
| `products` | Array | Ja | Artikel in der Bestellung. Siehe Produkteigenschaften-Untertabelle. |
| `source` | String | Ja | Quelle, von der das Event stammt. |
| `metadata` | Object | Nein | Flexible Schlüssel-Wert-Paare. Erkannte Untereigenschaft: `order_status_url` (String) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event-Eigenschaften" }

#### Produkteigenschaften (`products[]`)

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
|-----------------|-----------|----------|---------------------------------------------|
| `product_id` | String | Ja | Eindeutiger Produktbezeichner. |
| `product_name` | String | Ja | Anzeigename des Produkts. |
| `variant_id` | String | Ja | Varianten-Bezeichner. |
| `image_url` | String | Nein | Produktbild-URL. |
| `product_url` | String | Nein | URL zur Produktseite. |
| `quantity` | Integer | Ja | Anzahl der Einheiten im Warenkorb. |
| `price` | Gleitkommazahl | Ja | Varianten-Stückpreis. |
| `metadata` | Object | Nein | Flexible Schlüssel-Wert-Paare (z. B. `color` oder `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Produkteigenschaften (products[])" }

#### REST API-Beispiel

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_placed",
      "time": "2026-04-28T14:35:42Z",
      "properties": {
        "order_id": "ord_77821",
        "cart_id": "cart_abc123",
        "total_value": 224.96,
        "subtotal_value": 209.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "total_discounts": 10.0,
        "discounts": [
          {
            "code": "SPRING10",
            "amount": 10.0,
            "type": "percentage"
          }
        ],
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
            "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "order_status_url": "https://www.example.com/orders/ord_77821/status"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.order_cancelled %}

Lösen Sie dieses Event aus, wenn eine Bestellung storniert wird.

#### Clientseitige Implementierung

Verwenden Sie `logCustomEvent`. Plattformspezifische Implementierungsbeispiele finden Sie unter [E-Commerce-Events über das Braze SDK protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

{% alert important %}
Dieses Event verringert `total_orders` um 1 im Kundenprofil. Es hat keinen Einfluss auf `total_revenue`; verwenden Sie `order_refunded`, um den Umsatz anzupassen.
{% endalert %}

#### Event-Eigenschaften

| Eigenschaft | Typ | Erforderlich | Beschreibung |
|------------------|---------|----------|--------------------------------------------------------------------------------------------------|
| `order_id` | String | Ja | Eindeutiger Bezeichner für die Bestellung. |
| `total_value` | Gleitkommazahl | Ja | Gesamtgeldwert der stornierten Bestellung. Muss ≥ 0 sein – senden Sie den absoluten Betrag; Braze übernimmt die Verringerung. |
| `subtotal_value` | Gleitkommazahl | Nein | Zwischensumme (nach Rabatt, vor Steuern/Versand). |
| `tax` | Gleitkommazahl | Nein | Gesamtsteuer auf die Bestellung. |
| `shipping` | Gleitkommazahl | Nein | Gesamtversandkosten. |
| `currency` | String | Ja | Dreistelliger ISO-4217-Code. |
| `total_discounts` | Gleitkommazahl | Nein | Gesamtbetrag der auf die Bestellung angewendeten Rabatte. |
| `discounts` | Array | Nein | Detaillierte Liste der angewendeten Rabatte. |
| `cancel_reason` | String | Ja | Grund für die Stornierung der Bestellung. |
| `products` | Array | Ja | Artikel in der stornierten Bestellung. Siehe Produkteigenschaften-Untertabelle. |
| `source` | String | Ja | Quelle, von der das Event stammt. |
| `metadata` | Object | Nein | Flexible Schlüssel-Wert-Paare. Erkannte Untereigenschaft: `order_status_url` (String) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event-Eigenschaften" }

#### Produkteigenschaften (`products[]`)

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
|----------------|-----------|----------|-----------------------------------------------|
| `product_id` | String | Ja | Eindeutiger Produktbezeichner. |
| `product_name` | String | Ja | Anzeigename des Produkts. |
| `variant_id` | String | Ja | Varianten-Bezeichner. |
| `image_url` | String | Nein | Produktbild-URL. |
| `product_url` | String | Nein | URL zur Produktseite. |
| `quantity` | Integer | Ja | Anzahl der Einheiten im Warenkorb. |
| `price` | Gleitkommazahl | Ja | Varianten-Stückpreis. |
| `metadata` | Object | Nein | Flexible Schlüssel-Wert-Paare (z. B. `color` oder `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Produkteigenschaften (products[])" }

#### REST API-Beispiel

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_cancelled",
      "time": "2026-04-28T16:10:00Z",
      "properties": {
        "order_id": "ord_77821",
        "total_value": 224.96,
        "subtotal_value": 209.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "total_discounts": 10.0,
        "cancel_reason": "customer_request",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "order_status_url": "https://www.example.com/orders/ord_77821/status"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.order_refunded %}

Lösen Sie dieses Event aus, wenn eine vollständige oder teilweise Erstattung ausgestellt wird.

#### Clientseitige Implementierung

Verwenden Sie `logCustomEvent`. Plattformspezifische Implementierungsbeispiele finden Sie unter [E-Commerce-Events über das Braze SDK protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

{% alert important %}
Dieses Event verringert `total_revenue` um den Wert in `total_value` und erhöht `total_refunds` im Kundenprofil. Setzen Sie bei Teilerstattungen `total_value` nur auf den erstatteten Betrag, nicht auf den ursprünglichen Bestellwert.
{% endalert %}

#### Event-Eigenschaften

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
|-------------------|-----------|----------|------------------------------------------------------------------------------------------------------|
| `order_id` | String | Ja | Eindeutiger Bezeichner für die ursprüngliche Bestellung. |
| `total_value` | Gleitkommazahl | Ja | Gesamtgeldwert der Erstattung. Muss ≥ 0 sein – senden Sie den absoluten Betrag; Braze übernimmt die Erhöhung von total_refunds. |
| `currency` | String | Ja | Dreistelliger ISO-4217-Code. |
| `total_discounts` | Gleitkommazahl | Nein | Gesamtbetrag der ursprünglich angewendeten Rabatte. |
| `discounts` | Array | Nein | Detaillierte Liste der Rabatte. |
| `products` | Array | Ja | Erstattete Artikel. Siehe Produkteigenschaften-Untertabelle. |
| `source` | String | Ja | Quelle, von der das Event stammt. |
| `metadata` | Object | Nein | Flexible Schlüssel-Wert-Paare. Erkannte Untereigenschaft: `order_status_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event-Eigenschaften" }

#### Produkteigenschaften (`products[]`)

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
|-----------------|-----------|----------|-------------------------------------------------------|
| `product_id` | String | Ja | Eindeutiger Produktbezeichner. |
| `product_name` | String | Ja | Anzeigename des Produkts. |
| `variant_id` | String | Ja | Varianten-Bezeichner. |
| `image_url` | String | Nein | Produktbild-URL. |
| `product_url` | String | Nein | URL zur Produktseite. |
| `quantity` | Integer | Ja | Anzahl der Einheiten im Warenkorb. |
| `price` | Gleitkommazahl | Ja | Varianten-Stückpreis. |
| `metadata` | Object | Nein | Flexible Schlüssel-Wert-Paare (z. B. `color` oder `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Produkteigenschaften (products[])" }

#### REST API-Beispiele {#rest-api-examples}

{% subtabs %}
{% subtab Vollständige Erstattung %}

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_refunded",
      "time": "2026-04-29T10:05:00Z",
      "properties": {
        "order_id": "ord_77821",
        "total_value": 189.99,
        "currency": "USD",
        "total_discounts": 0,
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11",
              "refund_reason": "size_mismatch"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "order_status_url": "https://www.example.com/orders/ord_77821/status"
        }
      }
    }
  ]
}
```
{% endsubtab %}
{% subtab Teilerstattung %}

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_refunded",
      "time": "2026-05-02T11:08:30Z",
      "properties": {
        "order_id": "ORD-20260428-7891",
        "total_value": 29.98,
        "currency": "USD",
        "products": [
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "refund_method": "store_credit",
          "initiated_by": "customer"
        }
      }
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### E-Commerce-Event-Nachverarbeitung {#ecommerce-event-post-processing}

Wenn Sie ein E-Commerce-Event senden, validiert Braze es gegen das erwartete Schema für diesen Event-Namen.

Die folgende Tabelle fasst zusammen, was Braze automatisch für jedes Event tut, wenn die Validierung erfolgreich ist. Was passiert, wenn die Validierung fehlschlägt, erfahren Sie unter [Event-Validierung und Fehlerbehebung](#event-validation-and-troubleshooting).

| Event | Was Braze automatisch tut |
|------------------------------|-------------------------------------------------------------------------------------------------------------------|
| `ecommerce.order_placed` | Erhöht **Gesamtumsatz** um `total_value` und **Gesamtbestellungen** um 1 im Kundenprofil. |
| `ecommerce.order_cancelled` | Verringert **Gesamtbestellungen** um 1. |
| `ecommerce.order_refunded` | Verringert **Gesamtumsatz** um `total_value` und erhöht **Gesamterstattungswert**. |
| `ecommerce.cart_updated` | Erstellt oder aktualisiert das Warenkorb-Mapping-Objekt im Kundenprofil (vollständige Warenkorb-Payloads oder inkrementelle Warenkorb-Aktualisierungen mit optionalem `action`: `add`, `remove` oder `replace`). Der Warenkorb läuft nach 30 Tagen ohne Aktualisierung ab. |
| `ecommerce.product_viewed` | Keine Änderungen am Kundenprofil. Verfügbar für Segmentierung, Triggering und BrazeAI<sup>TM</sup>-Features (wie Artikelempfehlungen). |
| `ecommerce.checkout_started` | Keine Änderungen am Kundenprofil. Verfügbar für Segmentierung und Triggering (z. B. abgebrochene Checkout-Flows). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Commerce-Event-Nachverarbeitung" }

{% alert important %}
Nicht-USD-Währungswerte werden automatisch anhand des Wechselkurses am Tag der Event-Meldung in USD umgerechnet. Wenn Sie bereits in USD berichten, setzen Sie `USD` als Währung fest, um eine unbeabsichtigte Umrechnung zu vermeiden.
{% endalert %}

## Implementierungsdetails {#implementation-details}

### Datenpunkte und Abrechnung {#data-points-and-billing}

E-Commerce-Events verbrauchen keine [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points). Sie können sie ohne Auswirkungen auf Ihre Datenpunkt-Nutzung protokollieren.

### Begrenzung der Event-Größe {#event-size-limit}

Event-Eigenschaften, die an `/users/track` gesendet werden, sind auf 102.400 Bytes (100 KB) pro Event begrenzt. Für getriggerte Campaign- und Canvas-Nachrichten haben die `trigger_properties`, die an [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) und [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) gesendet werden, ein strengeres Standardlimit von 51.200 Bytes (50 KB).

Als Best Practice senden Sie nur die Produktinformationen, die Sie zum Triggern, Personalisieren oder Zuordnen des Events benötigen. Speichern Sie umfangreichere Produktdetails – wie Beschreibungen, vollständige Variantenlisten, Lagerbestände oder alternative Bilder – in Braze Catalogs. Referenzieren Sie diese Details beim Senden von Nachrichten über `product_id` oder `variant_id`. Verwenden Sie das `metadata`-Objekt gezielt für bestell- oder produktspezifischen Kontext, den das Messaging nutzen wird.

### Währungsbehandlung {#currency-handling}

Braze konvertiert Nicht-USD-Währungswerte automatisch in USD unter Verwendung des Wechselkurses am Tag, an dem das Event gemeldet wird. Dieser konvertierte Wert wird in den Umsatz-Metriken angezeigt.

{% alert tip %}
Wenn Sie ausschließlich in USD arbeiten, codieren Sie `"currency": "USD"` in jedem Event fest, um unnötige Konvertierungen zu vermeiden.
{% endalert %}

### Source-Feld {#source-field}

Die Source-Eigenschaft ist ein erforderlicher String, der angibt, woher das Event stammt. Zum Beispiel `shopify`, `in-store POS` oder `custom_api`. Dies hilft Ihnen, Integrationsquellen zu unterscheiden, wenn Sie Daten in Currents-Exporten analysieren oder Validierungsprobleme debuggen.

### Flexibilität der Metadaten {#metadata-flexibility}

Sowohl die Metadaten-Objekte auf Event-Ebene als auch auf Produktebene akzeptieren beliebige Schlüssel-Wert-Paare, sodass Sie angepasste Dimensionen hinzufügen können, ohne das Kernschema zu ändern. Gängige Beispiele sind `order_status_url`, `gift_wrapped`, `loyalty_points_earned` oder `warehouse_id`. Diese Eigenschaften stehen in der Liquid-Personalisierung, in Currents-Exporten und in der Segmentierung über [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension) zur Verfügung.

{% alert important %}
Empfohlene Events verwenden ein striktes Schema. Daher schlägt das Hinzufügen angepasster Eigenschaften auf der obersten Ebene der Properties die Validierung fehl. Platzieren Sie alle angepassten Eigenschaften im `metadata`-Objekt auf Event-Ebene oder im `metadata`-Objekt auf Produktebene innerhalb von `products[]`. Diese bleiben für Liquid, Currents und Segmentierung genauso verfügbar wie Felder auf der obersten Ebene.
{% endalert %}

## Event-Validierung und Fehlerbehebung {#event-validation-and-troubleshooting}

Wenn Sie ein empfohlenes E-Commerce-Event über `/users/track` oder ein Braze SDK senden, validiert Braze den Payload während der Verarbeitung des empfohlenen Events anhand des JSON-Schemas des Events. Die Validierung läuft automatisch bei jedem Event, dessen Name exakt mit einem empfohlenen Event übereinstimmt (zum Beispiel `ecommerce.order_placed` oder `ecommerce.cart_updated`).

### Was wir validieren {#what-we-validate}

Für jedes Event, dessen Name mit einem empfohlenen E-Commerce-Event übereinstimmt, prüft Braze:

| Prüfung                     | Beispiel                                                                                                                      |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Event-Name                | Muss exakt übereinstimmen. Zum Beispiel ist `ecommerce.cart_updated` korrekt – nicht `ecommerce.Cart_Updated`, `cartupdated` oder `cart_updated`. |
| Erforderliche Eigenschaften vorhanden | `order_placed` erfordert `order_id`, `total_value`, `currency`, `products` und `source`.                                   |
| Korrekte Datentypen        | `total_value` muss eine Zahl sein; `currency` muss ein String sein; `products` muss ein Array sein.                                   |
| Keine zusätzlichen Top-Level-Eigenschaften | Angepasste Felder unter „properties“ führen zum Fehler. Verwenden Sie stattdessen das `metadata`-Objekt.                                         |
| Wertbeschränkungen         | Geldbetragsfelder müssen ≥ `0` sein. `currency` muss ein gültiger ISO-4217-String sein.                                                  |
| Felder pro Produkt        | Jedes Element in `products[]` muss `product_id`, `product_name`, `variant_id`, `quantity` und `price` enthalten.                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Was wir validieren" }

### Warum wir validieren {#why-we-validate}

E-Commerce-Events steuern Features, die auf konsistente, vorhersagbare Daten angewiesen sind – darunter Umsatz-Tracking, der {% raw %}`{% shopping_cart %}`{% endraw %} Liquid-Tag, der Warenkorb-Abbruch-Trigger und Reporting. Wenn Payloads vom Schema abweichen, erzeugen diese Features stille Ungenauigkeiten (falsche Umsatzsummen, fehlende Warenkörbe, fehlerhafte Trigger). Die Validierung erzwingt den Vertrag im Voraus, damit nachgelagerte Features vorhersagbar funktionieren.

### Wenn die Validierung erfolgreich ist {#when-validation-passes}

Das Event wird als empfohlenes E-Commerce-Event mit allen zugehörigen Nachverarbeitungsschritten verarbeitet. Unter [Empfohlene E-Commerce-Events](#event-schemas) finden Sie die vollständige Liste der Verhaltensweisen, die durch jeden Event-Typ ausgelöst werden.

#### Ein erfolgreiches Event überprüfen {#verify-a-successful-event}

Nachdem Sie ein Event gesendet haben, können Sie mit einer der folgenden Methoden bestätigen, dass es akzeptiert und korrekt verarbeitet wurde:

- [Event-Nutzerprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log): Öffnen Sie das Profil der Nutzer:in im Dashboard und überprüfen Sie die Aktivität. Empfohlene Events werden mit ihrem vollständigen Eigenschafts-Payload angezeigt, sodass Sie bestätigen können, dass das Event angekommen ist und die Werte mit dem übereinstimmen, was Sie gesendet haben.
- [Bericht über angepasste Events]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report): Gehen Sie zu **Analytics** > **Custom Events Report**, um aggregierte Zählungen jedes empfohlenen Events über die Zeit zu sehen. Dies ist nützlich, um zu bestätigen, dass der Produktions-Traffic wie erwartet fließt, wenn Ihre Integration live ist.
- [Testnutzer:innen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups?utm_source=operator_user&utm_medium=dashboard#adding-test-users): Markieren Sie eine Nutzer:in in Ihrem Entwicklungs-Workspace als Testnutzer:in und lösen Sie dann Events aus Ihrer Integration für diese Nutzer:in aus. Testnutzer:innen sind im Dashboard gekennzeichnet, sodass Sie das End-to-End-Verhalten leicht isolieren und überprüfen können.

### Wenn die Validierung fehlschlägt {#when-validation-fails}

Das Event wird nicht als empfohlenes Event verarbeitet. Im Einzelnen:

- **Das Event wird vollständig verworfen.** Ungültige empfohlene E-Commerce-Events landen nicht im Kundenprofil, erscheinen nicht in Currents und stehen nicht für die Segmentierung zur Verfügung.
- Nachgelagerte Features für empfohlene Events werden nicht ausgeführt, darunter:
  - Umsatz-Tracking (Umsatz-Reporting, berechnete Nutzerfelder wie `total_revenue`)
  - Warenkorb-Objekt-Aktualisierungen im Kundenprofil
  - „Perform Cart Updated Event“- oder „Placed Order“-Trigger in Canvas und Campaigns

Wie Fehler gemeldet werden, hängt vom Aufnahmepfad ab:

- **REST API (`/users/track`):** Jedes ungültige Event wird im Fehler-Array der Antwort gemeldet. Jeder Eintrag gibt an, welches Event fehlgeschlagen ist (Index) und warum (Typ). Das Top-Level-Feld „message“ zeigt weiterhin „success“ an, was nur bedeutet, dass Ihre Anfrage Braze erreicht hat – nicht, dass jedes Event gültig war. Prüfen Sie immer das Fehler-Array in der Antwort.
- **Braze SDKs:** SDK-Aufrufe kehren sofort zurück, und die Validierung läuft im Hintergrund, sodass Fehler nicht an Ihre App zurückgesendet werden. Um über Validierungsfehler bei E-Commerce-Events informiert zu werden, achten Sie auf die Zusammenfassungs-E-Mail zu Fehlern (siehe [Fehler finden](#find-failures)).

#### Beispiel einer API-Fehlerantwort {#example-api-error-response}

Der `/users/track`-Endpunkt gibt Fehler auf Feldebene zurück, die angeben, welche Eigenschaften fehlgeschlagen sind und warum. Beachten Sie, dass das Top-Level-Feld `message` möglicherweise `"success"` zurückgibt, da das Event in die Pipeline aufgenommen wurde; das `errors`-Array gibt an, welche Felder die Schema-Validierung nicht bestanden haben. Im folgenden Beispiel sehen Sie eine Fehlerantwort.

```json
{
 "message": "success",
 "errors": [{ "index": 0, "input_array": "purchases", "type": "'currency' must be an ISO 4217 currency" }]
}
```

Fehler werden außerdem intern klassifiziert und für die Zusammenfassungs-E-Mail zu Fehlern aggregiert:

| Fehlertyp           | Bedeutung                                           | Beispiel                                                        |
|------------------------|---------------------------------------------------|----------------------------------------------------------------|
| `missing_property`     | Ein erforderliches Feld fehlt.                       | `order_placed` ohne `order_id` gesendet.                        |
| `extra_property`       | Ein Feld wurde hinzugefügt, das das Schema nicht definiert. | Ein angepasstes `gift_wrapped`-Feld auf der obersten Ebene von `properties` statt innerhalb von `metadata`. |
| `unexpected_data_type` | Ein Feld hat den falschen Typ.                        | `total_value: "29.99"` (String) statt `29.99` (Zahl).   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Beispiel einer API-Fehlerantwort" }

{% alert note %}
Event-Namen, die nicht exakt mit einem empfohlenen Event übereinstimmen (zum Beispiel `ecommerce.OrderPlaced`), überspringen die Validierung vollständig und werden als gewöhnliche angepasste Events aufgezeichnet. Sie erscheinen in Currents und der Segmentierung unter dem von Ihnen gesendeten Namen, erhalten aber keine Verarbeitung als empfohlenes Event und keinen `errors`-Eintrag in der Antwort.
{% endalert %}

#### Fehler finden {#find-failures}

Braze sendet Ihren Workspace-Admins eine Zusammenfassung der Validierungsfehler empfohlener Events per E-Mail, damit Sie Integrationsprobleme identifizieren und beheben können, ohne jedes Event manuell überwachen zu müssen.

Die Zusammenfassungs-E-Mail enthält:

- **Gesamtanzahl der Fehler:** Fehlerzählungen für den Berichtszeitraum.
- **Fehler nach Event:** Eine Aufschlüsselung, wie viele Events für jeden empfohlenen Event-Typ fehlgeschlagen sind (zum Beispiel `ecommerce.cart_updated` und `ecommerce.order_placed`). Nutzen Sie dies, um zu identifizieren, welche Events in Ihrer Integration zuerst Aufmerksamkeit benötigen.
- **Fehler nach Quelle:** Eine Aufteilung zwischen API und SDK, damit Sie feststellen können, welche Integration die Fehler verursacht.

Wenn Sie diese E-Mails nicht erhalten oder die Empfängerliste überprüfen möchten, wenden Sie sich an Ihr Braze-Konto-Team.

#### Fehler diagnostizieren und beheben {#diagnose-and-fix-failures}

Wenn Sie eine Zusammenfassungs-E-Mail zu Fehlern erhalten:

1. **Identifizieren Sie das fehlgeschlagene Event und die Quelle.** Die E-Mail trennt Fehler nach Event-Name und Integrationsquelle (`sdk` versus `rest_api`), sodass Sie feststellen können, welche Integration die Korrektur benötigt. Wenn Sie mehrere Quellen haben, die dasselbe Event senden (zum Beispiel Ihr Storefront-SDK und ein Backend-Webhook, die beide `cart_updated` senden), behandeln Sie diese unabhängig voneinander.
2. **Vergleichen Sie Ihren Payload mit dem Schema** unter [Event-Schemas](#event-schemas). Die meisten Fehler fallen in eines von drei Mustern:
   - `missing_property`: Ein erforderliches Feld fehlt. Lösung: Fügen Sie das erforderliche Feld hinzu.
   - `extra_property`: Ein angepasstes Feld befindet sich auf der obersten Ebene von `properties`. Lösung: Verschieben Sie das angepasste Feld in `metadata` (Event-Ebene) oder `products[].metadata` (pro Produkt).
   - `unexpected_data_type`: Ein Wert hat den falschen Typ (zum Beispiel `total_value` als String gesendet). Lösung: Konvertieren Sie den Wert vor dem Senden.
3. **Testen Sie den korrigierten Payload in einem Entwicklungs-Workspace**, bevor Sie ihn in die Produktion ausrollen. Senden Sie ein bekanntes Test-Event für eine Testnutzer:in und überprüfen Sie dann das erwartete Verhalten des empfohlenen Events im Profil dieser Nutzer:in (zum Beispiel ob das Warenkorb-Objekt aktualisiert wird, der Umsatz steigt oder der Warenkorb-Abbruch-Trigger ausgelöst wird).
4. **Überwachen Sie die nächste Fehler-E-Mail**, um zu bestätigen, dass die Fehleranzahl für dieses Event, diese Quelle und diesen Typ auf null sinkt.

Die vollständigen Eigenschaftsanforderungen pro Event finden Sie unter [Event-Schemas](#event-schemas).