---
nav_title: E-Commerce-Events protokollieren
article_title: E-Commerce-Events über das Braze SDK protokollieren
page_order: 3.25
description: "Erfahren Sie, wie Sie empfohlene E-Commerce-Events über die Braze Android-, Swift- und Web-SDKs mithilfe typisierter Event-Klassen und logEcommerceEvent protokollieren."
platform:
  - Android
  - Swift
  - Web
---

# E-Commerce-Events protokollieren {#log-ecommerce-events}

> Erfahren Sie, wie Sie [empfohlene E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/) über die Braze Android-, Swift- und Web-SDKs mithilfe typisierter Event-Klassen und `logEcommerceEvent` protokollieren. Informationen zu Event-Eigenschaftsschemata, Plattform-Features und Ingestion-Validierung finden Sie unter [Empfohlene Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/) und [Event-Validierung und Fehlerbehebung]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-validation-and-troubleshooting).

{% alert note %}
Verwenden Sie für Wrapper-SDKs, die hier nicht aufgeführt sind, stattdessen die entsprechende native Android- oder Swift-Methode.
{% endalert %}

## Event-Schemata {#event-schemas}

Die sechs empfohlenen E-Commerce-Events teilen sich ein Schema auf Bestellebene über alle Plattformen hinweg. Verwenden Sie die folgenden Eigenschaftstabellen, wenn Sie den Payload für jedes Event erstellen. Das kanonische Schema mit vollständigem Validierungsverhalten und REST-API-Beispielen finden Sie unter [Empfohlene Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#event-schemas). Informationen zu Plattform-Features wie Segmentierung, Canvas-Templates und Reporting finden Sie unter [E-Commerce-Events verwenden]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/).

{% tabs local %}
{% tab product_viewed %}

Wird ausgelöst, wenn eine Nutzerin oder ein Nutzer eine Produktdetailseite aufruft.

**Event-Eigenschaften**

| Eigenschaftsname | Datentyp | Erforderlich | Beschreibung |
| ------------- | --------- | -------- | ----------- |
| `product_id` | String | Ja | Eindeutiger Produktbezeichner (zum Beispiel SKU oder Artikel-ID). |
| `product_name` | String | Ja | Anzeigename des Produkts. |
| `variant_id` | String | Ja | Bezeichner der Produktvariante (zum Beispiel `shirt_medium_blue`). |
| `image_url` | String | Nein | Bild-URL des Produkts. |
| `product_url` | String | Nein | URL zur Produktseite für weitere Details. |
| `price` | Gleitkommazahl | Ja | Stückpreis der Variante zum Zeitpunkt der Ansicht. |
| `currency` | String | Ja | Dreibuchstabiger ISO-4217-Code (zum Beispiel `USD` oder `EUR`). |
| `source` | String | Ja | Quelle, von der das Event stammt (zum Beispiel `web`, `ios` oder `android`). |
| `type` | String-Array | Nein | Erforderlich, um Braze-Katalog-Trigger-Features für Wieder-verfügbar- und Preissenkungsbenachrichtigungen zu nutzen. Akzeptierte Werte: `"price_drop"`, `"back_in_stock"`. |
| `metadata` | Objekt | Nein | Flexible Schlüssel-Wert-Paare. Erkannte Untereigenschaft: `sku` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event-Eigenschaften für Produktansicht" }

{% endtab %}
{% tab cart_updated %}

Wird jedes Mal ausgelöst, wenn sich der Inhalt des Warenkorbs ändert. Verwenden Sie den vollständigen Warenkorbersatz (lassen Sie `action` weg oder setzen Sie es auf `replace`) oder inkrementelle Aktualisierungen (`add` oder `remove`).

**Event-Eigenschaften**

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
| -------- | --------- | -------- | ----------- |
| `cart_id` | String | Ja | Eindeutiger Bezeichner für den Warenkorb. Wird über Warenkorb-, Checkout- und Bestell-Events hinweg für die Warenkorbzuordnung geteilt. |
| `action` | String | Nein | `add` (Menge erhöhen oder eine Position hinzufügen), `remove` (Menge verringern; Position bei `0` entfernen) oder `replace` (vollständiger Warenkorbersatz, identisch mit dem Weglassen von `action`). |
| `total_value` | Gleitkommazahl | Bedingt | Erforderlich, wenn `action` weggelassen wird oder `replace` ist. Optional, wenn `action` `add` oder `remove` ist. |
| `subtotal_value` | Gleitkommazahl | Nein | Zwischensumme des Warenkorbs (nach Rabatt, vor Steuern/Versand). |
| `tax` | Gleitkommazahl | Nein | Gesamtsteuer auf den Warenkorb. |
| `shipping` | Gleitkommazahl | Nein | Gesamtversandkosten für den Warenkorb. |
| `currency` | String | Ja | Dreibuchstabiger ISO-4217-Code. |
| `products` | Array | Ja | Einzelposten für diese Aktualisierung. Siehe die Produkteigenschaftstabelle. |
| `source` | String | Ja | Quelle, von der das Event stammt. |
| `metadata` | Objekt | Nein | Flexible Schlüssel-Wert-Paare für zusätzliche Daten auf Event-Ebene. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event-Eigenschaften für Warenkorbaktualisierung" }

**Produkteigenschaften (`products[]`)**

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Ja | Eindeutiger Produktbezeichner. |
| `product_name` | String | Ja | Anzeigename des Produkts. |
| `variant_id` | String | Ja | Variantenbezeichner. |
| `image_url` | String | Nein | Bild-URL des Produkts. |
| `product_url` | String | Nein | URL zur Produktseite. |
| `quantity` | Integer | Ja | Bei vollständigem Ersatz die Anzahl der Einheiten im Warenkorb für diese Position. Bei `add` oder `remove` die Anzahl der hinzuzufügenden oder zu entfernenden Einheiten. |
| `price` | Gleitkommazahl | Ja | Stückpreis der Variante. |
| `metadata` | Objekt | Nein | Flexible Schlüssel-Wert-Paare (zum Beispiel `color` oder `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Produkteigenschaften für Warenkorbaktualisierung" }

{% endtab %}
{% tab checkout_started %}

Wird ausgelöst, wenn die Nutzerin oder der Nutzer den Checkout-Prozess startet.

**Event-Eigenschaften**

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
| -------- | --------- | -------- | ----------- |
| `checkout_id` | String | Ja | Eindeutiger Bezeichner für die Checkout-Sitzung. |
| `cart_id` | String | Nein | Warenkorbbezeichner. Wird über Warenkorb-, Checkout- und Bestell-Events hinweg für die Warenkorbzuordnung geteilt. |
| `total_value` | Gleitkommazahl | Ja | Gesamtgeldwert des Checkouts. |
| `subtotal_value` | Gleitkommazahl | Nein | Zwischensumme (nach Rabatt, vor Steuern/Versand). |
| `tax` | Gleitkommazahl | Nein | Gesamtsteuer auf den Checkout. |
| `shipping` | Gleitkommazahl | Nein | Gesamtversandkosten. |
| `currency` | String | Ja | Dreibuchstabiger ISO-4217-Code. |
| `products` | Array | Ja | Artikel im Checkout. Siehe die Produkteigenschaftstabelle. |
| `source` | String | Ja | Quelle, von der das Event stammt. |
| `metadata` | Objekt | Nein | Flexible Schlüssel-Wert-Paare. Erkannte Untereigenschaft: `checkout_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event-Eigenschaften für Checkout gestartet" }

**Produkteigenschaften (`products[]`)**

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Ja | Eindeutiger Produktbezeichner. |
| `product_name` | String | Ja | Anzeigename des Produkts. |
| `variant_id` | String | Ja | Variantenbezeichner. |
| `image_url` | String | Nein | Bild-URL des Produkts. |
| `product_url` | String | Nein | URL zur Produktseite. |
| `quantity` | Integer | Ja | Anzahl der Einheiten im Warenkorb. |
| `price` | Gleitkommazahl | Ja | Stückpreis der Variante. |
| `metadata` | Objekt | Nein | Flexible Schlüssel-Wert-Paare (zum Beispiel `color` oder `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Produkteigenschaften für Checkout gestartet" }

{% endtab %}
{% tab order_placed %}

Wird ausgelöst, wenn eine Bestellung erfolgreich abgeschlossen oder die Zahlung bestätigt wird.

**Event-Eigenschaften**

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
| -------- | --------- | -------- | ----------- |
| `order_id` | String | Ja | Eindeutiger Bezeichner für die Bestellung. |
| `cart_id` | String | Nein | Warenkorbbezeichner. Wird über Warenkorb-, Checkout- und Bestell-Events hinweg für die Warenkorbzuordnung geteilt. |
| `total_value` | Gleitkommazahl | Ja | Gesamtgeldwert der Bestellung. |
| `subtotal_value` | Gleitkommazahl | Nein | Zwischensumme (nach Rabatt, vor Steuern/Versand). |
| `tax` | Gleitkommazahl | Nein | Gesamtsteuer auf die Bestellung. |
| `shipping` | Gleitkommazahl | Nein | Gesamtversandkosten. |
| `currency` | String | Ja | Dreibuchstabiger ISO-4217-Code. |
| `total_discounts` | Gleitkommazahl | Nein | Gesamtbetrag der auf die Bestellung angewendeten Rabatte. |
| `discounts` | Array | Nein | Detaillierte Liste der angewendeten Rabatte. Jedes Rabattobjekt unterstützt `code` (String), `amount` (Gleitkommazahl) und `type` (String). |
| `products` | Array | Ja | Artikel in der Bestellung. Siehe die Produkteigenschaftstabelle. |
| `source` | String | Ja | Quelle, von der das Event stammt. |
| `metadata` | Objekt | Nein | Flexible Schlüssel-Wert-Paare. Erkannte Untereigenschaft: `order_status_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event-Eigenschaften für Bestellung aufgegeben" }

**Produkteigenschaften (`products[]`)**

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Ja | Eindeutiger Produktbezeichner. |
| `product_name` | String | Ja | Anzeigename des Produkts. |
| `variant_id` | String | Ja | Variantenbezeichner. |
| `image_url` | String | Nein | Bild-URL des Produkts. |
| `product_url` | String | Nein | URL zur Produktseite. |
| `quantity` | Integer | Ja | Anzahl der Einheiten in der Bestellung. |
| `price` | Gleitkommazahl | Ja | Stückpreis der Variante. |
| `metadata` | Objekt | Nein | Flexible Schlüssel-Wert-Paare (zum Beispiel `color` oder `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Produkteigenschaften für Bestellung aufgegeben" }

{% endtab %}
{% tab order_cancelled %}

Wird ausgelöst, wenn eine Bestellung storniert wird.

**Event-Eigenschaften**

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
| -------- | --------- | -------- | ----------- |
| `order_id` | String | Ja | Eindeutiger Bezeichner für die Bestellung. |
| `total_value` | Gleitkommazahl | Ja | Gesamtgeldwert der stornierten Bestellung. Senden Sie den absoluten Betrag (größer oder gleich `0`); Braze übernimmt die Verringerung. |
| `subtotal_value` | Gleitkommazahl | Nein | Zwischensumme (nach Rabatt, vor Steuern/Versand). |
| `tax` | Gleitkommazahl | Nein | Gesamtsteuer auf die Bestellung. |
| `shipping` | Gleitkommazahl | Nein | Gesamtversandkosten. |
| `currency` | String | Ja | Dreibuchstabiger ISO-4217-Code. |
| `total_discounts` | Gleitkommazahl | Nein | Gesamtbetrag der auf die Bestellung angewendeten Rabatte. |
| `discounts` | Array | Nein | Detaillierte Liste der angewendeten Rabatte. |
| `cancel_reason` | String | Ja | Grund für die Stornierung der Bestellung. |
| `products` | Array | Ja | Artikel in der stornierten Bestellung. Siehe die Produkteigenschaftstabelle. |
| `source` | String | Ja | Quelle, von der das Event stammt. |
| `metadata` | Objekt | Nein | Flexible Schlüssel-Wert-Paare. Erkannte Untereigenschaft: `order_status_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event-Eigenschaften für Bestellung storniert" }

**Produkteigenschaften (`products[]`)**

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Ja | Eindeutiger Produktbezeichner. |
| `product_name` | String | Ja | Anzeigename des Produkts. |
| `variant_id` | String | Ja | Variantenbezeichner. |
| `image_url` | String | Nein | Bild-URL des Produkts. |
| `product_url` | String | Nein | URL zur Produktseite. |
| `quantity` | Integer | Ja | Anzahl der Einheiten in der Bestellung. |
| `price` | Gleitkommazahl | Ja | Stückpreis der Variante. |
| `metadata` | Objekt | Nein | Flexible Schlüssel-Wert-Paare (zum Beispiel `color` oder `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Produkteigenschaften für Bestellung storniert" }

{% endtab %}
{% tab order_refunded %}

Wird ausgelöst, wenn eine vollständige oder teilweise Erstattung erfolgt. Bei Teilerstattungen setzen Sie `total_value` nur auf den erstatteten Betrag, nicht auf den ursprünglichen Bestellwert.

**Event-Eigenschaften**

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
| -------- | --------- | -------- | ----------- |
| `order_id` | String | Ja | Eindeutiger Bezeichner für die ursprüngliche Bestellung. |
| `total_value` | Gleitkommazahl | Ja | Gesamtgeldwert der Erstattung. Senden Sie den absoluten Betrag (größer oder gleich `0`); Braze übernimmt die Umsatzanpassung. |
| `currency` | String | Ja | Dreibuchstabiger ISO-4217-Code. |
| `total_discounts` | Gleitkommazahl | Nein | Gesamtbetrag der ursprünglich angewendeten Rabatte. |
| `discounts` | Array | Nein | Detaillierte Liste der Rabatte. |
| `products` | Array | Ja | Erstattete Artikel. Siehe die Produkteigenschaftstabelle. |
| `source` | String | Ja | Quelle, von der das Event stammt. |
| `metadata` | Objekt | Nein | Flexible Schlüssel-Wert-Paare. Erkannte Untereigenschaft: `order_status_url` (String). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event-Eigenschaften für Bestellung erstattet" }

**Produkteigenschaften (`products[]`)**

| Eigenschaft | Datentyp | Erforderlich | Beschreibung |
| -------- | --------- | -------- | ----------- |
| `product_id` | String | Ja | Eindeutiger Produktbezeichner. |
| `product_name` | String | Ja | Anzeigename des Produkts. |
| `variant_id` | String | Ja | Variantenbezeichner. |
| `image_url` | String | Nein | Bild-URL des Produkts. |
| `product_url` | String | Nein | URL zur Produktseite. |
| `quantity` | Integer | Ja | Anzahl der erstatteten Einheiten. |
| `price` | Gleitkommazahl | Ja | Stückpreis der Variante. |
| `metadata` | Objekt | Nein | Flexible Schlüssel-Wert-Paare (zum Beispiel `color` oder `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Produkteigenschaften für Bestellung erstattet" }

{% endtab %}
{% endtabs %}

## Android

Ab Android SDK [42.3.0+](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.3.0) stehen typisierte E-Commerce-Event-Klassen mit clientseitiger Validierung zur Konstruktionszeit und automatischer `snake_case`-Serialisierung beim Aufruf von `Braze.logEcommerceEvent` zur Verfügung.

| Android-Klasse | Event-Name | Hinweise |
| ------------- | ---------- | ----- |
| `ProductViewedEvent` | `ecommerce.product_viewed` | Flacht Produktfelder auf die oberste Ebene von `properties` ab (kein `products`-Array). Diese Klasse unterstützt nicht die `type`-Eigenschaft auf oberster Ebene für Katalog-Trigger. Wenn Sie `type` benötigen, verwenden Sie [`logCustomEvent`](#manual-logging-with-logcustomevent) oder die REST API. |
| `CartUpdatedEvent` | `ecommerce.cart_updated` | Verwenden Sie `CartUpdatedAction` (`ADD`, `REMOVE`, `REPLACE`) für die `action`-Eigenschaft. |
| `CheckoutStartedEvent` | `ecommerce.checkout_started` | |
| `OrderPlacedEvent` | `ecommerce.order_placed` | Unterstützt optionale `cartId`, `totalDiscounts` und `discounts`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android-SDK-E-Commerce-Event-Klassen" }

{% alert important %}
`ecommerce.order_cancelled` und `ecommerce.order_refunded` sind nicht als typisierte Android-SDK-Klassen verfügbar. Protokollieren Sie diese mit [`logCustomEvent`](#manual-logging-with-logcustomevent) oder der REST API.
{% endalert %}

### Gemeinsame Bausteine {#shared-building-blocks}

- `EcommerceProduct`: Einzelposten für Warenkorb-, Checkout- und Bestell-Events.
  - Erforderlich: `productId`, `productName`, `variantId`, `price`, `quantity` (nicht-negativer `Long`)
  - Optional: `imageUrl`, `productUrl`, `metadata`
- `BrazeProperties`: `metadata` auf Event- oder Produktebene. Schlüssel müssen nicht-leere Strings mit höchstens 255 Zeichen ohne führendes Dollarzeichen ($) sein.

### Clientseitige Validierung {#client-side-validation}

Ungültige Payloads lösen beim Konstruieren der Event-Klasse eine `IllegalArgumentException` aus, sodass das Event nie in die Warteschlange gestellt wird. Allgemeine Regeln:

| Feld oder Regel | Validierung |
| ------------ | ---------- |
| String-IDs und -Namen (`product_id`, `product_name`, `variant_id`, `cart_id`, `checkout_id`, `order_id`, `source`, optionale URLs) | Nicht leer, bis zu 255 Zeichen |
| `price`, `total_value`, `total_discounts` | Muss größer oder gleich `0` sein |
| `currency` | Gültiger ISO-4217-Code (vom SDK getrimmt und in Großbuchstaben konvertiert) |
| `products` (Warenkorb-, Checkout-, Bestell-Events) | Mindestens ein `EcommerceProduct` |
| `quantity` (pro Produkt) | Nicht-negative Ganzzahl |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Clientseitige Validierungsregeln für Android-E-Commerce-Events" }

Wenn die serialisierten Eigenschaften zum Versandzeitpunkt das SDK-Größenlimit überschreiten, protokolliert `logEcommerceEvent` einen Fehler und sendet das Event nicht.

### Code-Beispiele {#code-examples}

{% tabs local %}
{% tab Kotlin %}

{% subtabs local %}
{% subtab product_viewed %}

```kotlin
import com.braze.Braze
import com.braze.models.outgoing.BrazeProperties
import com.braze.models.recommended.ecommerce.ProductViewedEvent

val metadata = BrazeProperties()
  .addProperty("sku", "SS-R-101")
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

Legen Sie `action` mit `CartUpdatedAction` fest:

| Wert | Wire-Wert | Beschreibung |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | Menge erhöhen oder eine Position hinzufügen. |
| `CartUpdatedAction.REMOVE` | `remove` | Menge verringern; Position bei `0` entfernen. |
| `CartUpdatedAction.REPLACE` | `replace` | Den gesamten Warenkorb ersetzen (Standard). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CartUpdatedAction-Werte für ecommerce.cart_updated" }

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

Braze stellt für dieses Event keine typisierte SDK-Klasse bereit. Verwenden Sie `logCustomEvent` mit einem Payload, der dem `ecommerce.order_cancelled`-Event-Schema entspricht.

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

Braze stellt für dieses Event keine typisierte SDK-Klasse bereit. Verwenden Sie `logCustomEvent` mit einem Payload, der dem `ecommerce.order_refunded`-Event-Schema entspricht.

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
    .addProperty("sku", "SS-R-101")
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

Legen Sie `action` mit `CartUpdatedAction` fest:

| Wert | Wire-Wert | Beschreibung |
| ----- | ---------- | ----------- |
| `CartUpdatedAction.ADD` | `add` | Menge erhöhen oder eine Position hinzufügen. |
| `CartUpdatedAction.REMOVE` | `remove` | Menge verringern; Position bei `0` entfernen. |
| `CartUpdatedAction.REPLACE` | `replace` | Den gesamten Warenkorb ersetzen (Standard). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CartUpdatedAction-Werte für ecommerce.cart_updated" }

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

Braze stellt für dieses Event keine typisierte SDK-Klasse bereit. Verwenden Sie `logCustomEvent` mit einem Payload, der dem `ecommerce.order_cancelled`-Event-Schema entspricht.

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

Braze stellt für dieses Event keine typisierte SDK-Klasse bereit. Verwenden Sie `logCustomEvent` mit einem Payload, der dem `ecommerce.order_refunded`-Event-Schema entspricht.

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

Das Swift SDK stellt typisierte E-Commerce-Event-Klassen bereit – `ProductViewedEvent`, `CartUpdatedEvent`, `CheckoutStartedEvent` und `OrderPlacedEvent` –, die Sie erstellen und an `logEcommerceEvent` übergeben. Verwenden Sie `ProductLineItem` für die Produkte in Warenkorb-, Checkout- und Bestell-Events. Jeder Initializer kann einen Fehler werfen, daher sollten Sie ihn in `try?` einschließen und das Event nur protokollieren, wenn die Konstruktion erfolgreich ist.
Dies ist ab Swift SDK Version `15.0.0` und höher verfügbar.

`ecommerce.order_cancelled` und `ecommerce.order_refunded` sind nicht als typisierte Swift-SDK-Klassen verfügbar. Protokollieren Sie diese mit `logCustomEvent`.

### Code-Beispiele

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
        "sku": "",
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

Braze stellt für dieses Event keine typisierte SDK-Klasse bereit. Verwenden Sie `logCustomEvent` mit einem Payload, der dem `ecommerce.order_cancelled`-Event-Schema entspricht.

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

Braze stellt für dieses Event keine typisierte SDK-Klasse bereit. Verwenden Sie `logCustomEvent` mit einem Payload, der dem `ecommerce.order_refunded`-Event-Schema entspricht.

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

## Web

Ab Web SDK [6.8.0+](https://github.com/braze-inc/braze-web-sdk) rufen Sie `logEcommerceEvent` mit einem Event-`name` und `properties` auf. Bei älteren SDK-Versionen rufen Sie `logCustomEvent` mit dem Event-Namen und einem Properties-Objekt auf. `ecommerce.order_cancelled` und `ecommerce.order_refunded` verwenden `logCustomEvent`.

### Code-Beispiele

{% tabs local %}
{% tab product_viewed %}

{% sdk_min_versions web:6.8.0 %}

Bei neueren SDK-Versionen rufen Sie `logEcommerceEvent()` auf:

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
            "sku": "",
            "color": "ORANGE",
            "size": "6",
            "brand": "Braze"
        }
    }
});
```

Bei älteren SDK-Versionen rufen Sie `logCustomEvent()` auf:

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
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    }
});
```

{% endtab %}
{% tab cart_updated %}

{% sdk_min_versions web:6.8.0 %}

Bei neueren SDK-Versionen rufen Sie `logEcommerceEvent()` auf:

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

Bei älteren SDK-Versionen rufen Sie `logCustomEvent()` auf:

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

Bei neueren SDK-Versionen rufen Sie `logEcommerceEvent()` auf:

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

Bei älteren SDK-Versionen rufen Sie `logCustomEvent()` auf:

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

Bei neueren SDK-Versionen rufen Sie `logEcommerceEvent()` auf:

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

Bei älteren SDK-Versionen rufen Sie `logCustomEvent()` auf:

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

## Manuelles Protokollieren mit `logCustomEvent` {#manual-logging-with-logcustomevent}

Um ein empfohlenes Event manuell zu protokollieren, rufen Sie `logCustomEvent` mit dem exakten Event-Namen (zum Beispiel `ecommerce.product_viewed`) und einem manuell erstellten `BrazeProperties`- oder `JSONObject`-Payload auf. Das SDK validiert keine Schemata empfohlener Events bei manuellen Aufrufen. Braze validiert diese Payloads während der Ingestion:

- Gültige Payloads werden als empfohlene Events mit vollständiger Nachverarbeitung verarbeitet.
- Ungültige Payloads (fehlende Pflichtfelder, falsche Typen, zusätzliche Eigenschaften auf oberster Ebene) werden nach der Ingestion verworfen. Fehler erscheinen im SDK-Verarbeitungsprotokoll des Workspace und in der [Fehlerübersichts-E-Mail]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/#find-failures).

Verwenden Sie nach Möglichkeit `logEcommerceEvent`, damit Sie ungültige Daten erkennen, bevor sie die App verlassen. Informationen zur allgemeinen Verwendung von `logCustomEvent` finden Sie unter [Angepasste Events protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android).