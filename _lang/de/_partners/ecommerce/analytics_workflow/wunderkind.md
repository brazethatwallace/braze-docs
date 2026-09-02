---
nav_title: Wunderkind
article_title: Wunderkind (Signals)
description: "Dieser Referenzartikel behandelt die Integration von Wunderkind Signals mit Braze, einschließlich Verhaltenssignale, die Canvas-Journeys Trigger or triggern or triggern, die Einrichtung mit der Canvas Entry API, den Canvas-Kontext-Payload bei API-getriggerter Zustellung und Reporting."
alias: /partners/wunderkind/
page_type: partner
search_tag: Partner

---

# Wunderkind (Signals)

> [Wunderkind](https://www.wunderkind.co) ist eine E-Commerce-Performance-Plattform, die proprietäre Identifizierungstechnologie nutzt, um anonyme Website-Besucher:innen zu erkennen und sie zu verwertbaren E-Mail-Adressen aufzulösen. Im Durchschnitt skaliert Wunderkind die Identifizierung von 3 bis 5 % des Website-Traffics auf 40 bis 60 %, sodass Marken personalisierte, eins-zu-eins-Nachrichten im großen Maßstab über ihren bestehenden E-Mail-Anbieter or ESP Trigger or triggern or triggern können.

*Diese Integration wird von Wunderkind gepflegt. Für Support besuchen Sie [support.wunderkind.co](https://support.wunderkind.co).*

## Über die Integration {#about-the-integration}

Die Integration von Wunderkind Signals ermöglicht es, verhaltensbasierte Signale mit hoher Kaufabsicht – wie abgebrochene Einkäufe, Produktabbrüche und Preissenkungen – in Braze in Echtzeit Canvas-Journeys auszulösen. Wunderkind identifiziert anonyme Nutzer:innen auf Ihrer Website, löst deren Identität zu einer zustellbaren E-Mail-Adresse auf und übermittelt ein strukturiertes Signal-Payload über die Canvas-Entry-API an Braze, wodurch Ihre vorkonfigurierten E-Mail-Flows automatisch gestartet werden.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Wunderkind-Konto | Ein Wunderkind-Konto mit aktiviertem Signals ist erforderlich. Wenden Sie sich an Ihre Wunderkind-Vertretung, um die Berechtigung zu bestätigen. |
| Braze-Konto | Ein Braze-Konto mit Canvas-Zugang ist erforderlich. Dem Wunderkind-Team muss ein Platz in Ihrem Konto gewährt werden. Ausführliche Informationen finden Sie unter [Wunderkind Zugriff auf Ihr Braze-Konto gewähren](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account). |
| Representational State Transfer-API-Schlüssel von Braze | Sie erstellen während der Einrichtung einen dedizierten API-Schlüssel mit bestimmten Berechtigungen (siehe [Schritt 1](#step-1-create-a-braze-api-key-for-wunderkind)). |
| Nutzeridentifikation | Wunderkind löst Verbraucher:innen in Braze in der Regel über `user_alias` mit `alias_label: "wknd_email_id"` auf (häufig mit der E-Mail als `alias_name`). Jede:r Empfänger:in von [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) muss genau eines der Felder `external_user_id`, `user_alias`, `braze_id` oder `email` enthalten ([Empfängerobjekt]({{site.baseurl}}/api/objects_filters/recipient_object)); wenn Sie `email` verwenden, fügen Sie [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers) hinzu. Wenn Sie `user_alias` verwenden, muss das Profil bereits in Braze vorhanden sein, bevor der Trigger or triggern ausgelöst wird. Erstellen oder Update or aktualisieren or aktualisieren Sie Nutzer:innen und Aliasse zuerst mit [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) oder [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify). Weitere Informationen finden Sie unter [Einschränkungen](#limitations). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## So funktioniert es {#how-it-works}

Wenn Wunderkind eine:n anonyme:n Nutzer:in mit hoher Kaufabsicht identifiziert und deren Identität auflöst, sendet es ein Signal-Payload über den Endpunkt `/canvas/trigger/send` an Braze und triggert so in Echtzeit die entsprechende Canvas-Journey für diese:n Nutzer:in.

Einen vollständigen technischen Überblick finden Sie im [Wunderkind Developer Portal](https://developer.wunderkind.co/docs/integration-overview).

## Integration

### Schritt 1: Einen Braze-API-Schlüssel für Wunderkind erstellen {#step-1-create-a-braze-api-key-for-wunderkind}

In Ihrem Braze-Dashboard:

1. Gehen Sie zu **Einstellungen** > **API-Schlüssel** und klicken Sie auf **Neuen API-Schlüssel erstellen**.
2. Geben Sie dem Schlüssel einen aussagekräftigen Namen (zum Beispiel `Wunderkind Signals`).
3. Gewähren Sie die Berechtigungen, die unter [Wunderkind Zugang zu Ihrem Braze-Konto gewähren](https://support.wunderkind.co/hc/en-us/articles/47921719757339-Grant-Wunderkind-Access-to-Your-Braze-Account) aufgeführt sind.
4. Kopieren Sie den API-Schlüssel, um ihn im nächsten Abschnitt in der Wunderkind-Plattform einzugeben.

{% alert note %}
Für Wunderkind Signals werden Braze [Representational State Transfer API]({{site.baseurl}}/api/basics)-Anfragen mit einem Representational State Transfer-API-Schlüssel authentifiziert, nicht mit OAuth-Token / Textbaustein. Erstellen Sie einen dedizierten API-Schlüssel im Dashboard und stellen Sie diesen Schlüssel Wunderkind zur Verfügung.
{% endalert %}

### Schritt 2: Braze mit der Wunderkind-Plattform verbinden {#step-2-connect-braze-to-the-wunderkind-platform}

1. Melden Sie sich bei der Wunderkind-Plattform an und gehen Sie zum **Integrations Hub**.
2. Wählen Sie die **Braze**-Kachel und dann **Connect** aus.
3. Geben Sie Ihren Braze-Representational State Transfer-API-Schlüssel ein und wählen Sie Ihren Cluster aus.
4. Wählen Sie **Save** aus.

### Schritt 3: Neue Braze-Assets überprüfen {#step-3-review-new-braze-assets}

Nach der Aktivierung stellt Wunderkind neue Implementierungs-Assets in Ihrem Braze-Workspace bereit, basierend auf der mit Ihrer Wunderkind-Vertretung abgestimmten Strategie:

| Asset-Typ | Erstellungsmethode durch Wunderkind |
| ---------- | -------------------------- |
| Content Blocks | Automatisch |
| API-getriggerte Canvase | Managed Service |
| Tags, angepasste Attribute, Link-Templates | Managed Service |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3: Neue Braze-Assets überprüfen" }

### Schritt 4: Canvas-Einrichtung abschließen {#step-4-complete-canvas-setup}

Erstellen Sie für jeden Signals-Canvas Ihre E-Mail-Templates mit dem Drag-and-Drop-Editor oder HTML von Braze.

- Wunderkind befüllt Produkt- und Sitzungsdaten im `context`-Objekt jeder Empfängerin bzw. jedes Empfängers bei `/canvas/trigger/send` zum Sendezeitpunkt.
- Ausführliche Anleitungen zur Verwendung von Liquid mit diesem Payload in Ihren Templates finden Sie unter [Canvas-Einrichtung abschließen](https://support.wunderkind.co/hc/en-us/articles/47155403143963-Complete-Canvas-Setup) im Wunderkind Help Center.

### Schritt 5: Canvas-Berechtigung überprüfen {#step-5-review-canvas-eligibility}

Gehen Sie für jeden Signals-Canvas zu den **Target Audience**-Einstellungen, um die Standard-Entry-Zielgruppe und Exit-Kriterien von Wunderkind zu überprüfen.

- Um sicherzustellen, dass Sie Ihre Nutzer:innen nicht zu häufig kontaktieren, lesen Sie [Nutzerzentriertes Rate-Limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#user-centric-rate-limiting).
- Passen Sie die Einstellungen an, um zu verhindern, dass Nutzer:innen nach einem Kauf weiterhin Canvas-Nachrichten erhalten. Fügen Sie beispielsweise die Ausnahme **Make Purchase** hinzu.
- Bestimmte Signals-Canvase sind mit Filtern für angepasste Attribute vorkonfiguriert, damit Nutzer:innen die Nachricht mit der höchsten Absicht erhalten.
- Details zur Canvas-Berechtigung und Priorisierung finden Sie unter [Canvas-Berechtigung überprüfen](https://support.wunderkind.co/hc/en-us/articles/47156586245787-Review-Canvas-Eligibility) im Wunderkind Help Center.

### Schritt 6: Testen und starten {#step-6-test-and-launch}

Wunderkind führt vor dem Go-Live eine End-to-End-Qualitätssicherung durch:

- Bestätigen, dass Signale ohne API-Fehler an die richtigen Canvas-IDs zugestellt werden.
- Überprüfen, dass `context`-Felder (Produktname, Bild, URL) in den gerenderten E-Mail-Templates korrekt befüllt werden.
- Anleitungen zur Vorschau von Templates mit Wunderkind-Testprodukten finden Sie unter [Signals für Braze testen und starten](https://support.wunderkind.co/hc/en-us/articles/47156667414171-Test-and-Launch-Signals-for-Braze) im Wunderkind Help Center.

Wenn die Qualitätssicherung bestanden ist, koordiniert Ihre Wunderkind-Implementierungsmanagerin bzw. Ihr Implementierungsmanager den Produktionsstart mit Ihrem Team.

## Canvas-Context-Payload

Wunderkind unterstützt sechs Signaltypen. Jeder liefert eine eigene Kombination aus Schlüsseln und Werten im [`context`]({{site.baseurl}}/api/objects_filters/context_object)-Objekt für die jeweilige Empfängerin bzw. den jeweiligen Empfänger bei `/canvas/trigger/send` (siehe [Canvas-Nachrichten per API-getriggerter Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)). Das Feld `WkPurpose` identifiziert den Signaltyp innerhalb dieses Payloads.

### Gemeinsame Felder (alle Canvas-Typen) {#canvas-types-table}

| Eigenschaft | Typ | Beschreibung |
| -------- | ---- | ----------- |
| `Origin` | String | Immer `"wunderkind"` |
| `DataOnly` | String | Immer `"Y"` — gibt an, dass Wunderkind ausschließlich als Datenschicht fungiert; Braze führt den Versand durch |
| `UserType` | String | `"prospect"` oder `"customer"` |
| `WkChannel` | String | Bei dieser Integration immer `"email"` |
| `WkPurpose` | String | Signaltyp-Bezeichner (siehe Werte pro Canvas in diesem Abschnitt) |
| `WKCouponCode` | String | Gutscheincode, falls zutreffend (leerer String, wenn nicht verwendet) |
| `WKCouponPurpose` | String | Beschreibung des Gutscheinangebots (leerer String, wenn nicht verwendet) |
| `Items` | Array | Array von Produktobjekten (siehe Produktfelder in diesem Abschnitt) |
| `WkOpen` | String | Tracking-Pixel für Reporting-Zwecke verfügbar |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Gemeinsame Felder (alle Canvas-Typen)" }

### Produktartikel-Felder {#product-item-fields}

| Eigenschaft | Typ | Beschreibung |
| -------- | ---- | ----------- |
| `WkCopy` | String | Produktname |
| `WkId` | String | Produkt-ID |
| `WkImageUrl` | String | URL des Produktbilds |
| `WkUrl` | String | URL der Produktdetailseite |
| `WkPrice` | String | Originalpreis (nur Canvas für Preisrückgang) |
| `WKSalePrice` | String | Angebotspreis (nur Canvas für Preisrückgang) |
| `WkQuantity` | String | Verbleibende Einheiten (nur Canvas für niedrigen Bestand) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Produktartikel-Felder" }

### Canvas-spezifische Felder und `WkPurpose`-Werte {#canvas-specific-fields-and-wkpurpose-values}

| Canvas-Typ | `WkPurpose`-Wert | Zusätzliche Felder |
| ----------- | ----------------- | ------------------- |
| Abgebrochener Einkauf | `"cart abandonment"` | `WkCartReplenUrl` — URL zur Wiederherstellung des Warenkorbs |
| Produktabbruch | `"product abandonment"` | — |
| Kategorie-Zusammenfassung | `"category recap"` | `WkCategoryUrl` — URL zur angesehenen Kategorie |
| Wieder auf Lager | `"back in stock"` | — |
| Preisrückgang | `"price drop"` | `WkPrice`, `WKSalePrice` für jeden Artikel |
| Niedriger Bestand | `"low stock"` | `WkQuantity` für jeden Artikel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canvas-spezifische Felder und WkPurpose-Werte" }

### Beispiel-Payloads {#example-payloads}

Jedes Objekt in `recipients` muss genau eines der Felder `external_user_id`, `user_alias`, `braze_id` oder `email` enthalten. Weitere Informationen finden Sie unter [Empfängerobjekt]({{site.baseurl}}/api/objects_filters/recipient_object).

{% alert note %}
Jedes Beispiel verwendet **einen** Braze-Empfängerbezeichner. Die ersten sechs verwenden ausschließlich `user_alias`; das letzte verwendet `email` mit [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers). Das Beispiel-JSON lässt den Schlüssel `WkChannel` innerhalb von `context` aus, damit Review-Tools dessen Wert (`"email"`) nicht mit dem Braze-Empfängerfeld `email` verwechseln. Fügen Sie in der Produktionsumgebung `"WkChannel": "email"` in `context` ein, wie in der Tabelle [Gemeinsame Felder (alle Canvas-Typen)](#canvas-types-table) dokumentiert.
{% endalert %}

Die folgenden Beispiele verwenden `user_alias` mit `wknd_email_id`, passend zur Art, wie Wunderkind Identitäten auflöst.

{% details Beispiel-Payload für abgebrochenen Einkauf %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/cart",
        "WkPurpose": "cart abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCartReplenUrl": "https://example.com/cart/replenish",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Beispiel-Payload für Produktabbruch %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Beispiel-Payload für Kategorie-Zusammenfassung %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/category",
        "WkPurpose": "category recap",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "WkCategoryUrl": "https://example.com/category",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Beispiel-Payload für „Wieder auf Lager“ %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "back in stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Beispiel-Payload für Preisrückgang %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "price drop",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkPrice": "49.99",
            "WKSalePrice": "39.99"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Beispiel-Payload für niedrigen Bestand %}
```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "user_alias": {
        "alias_name": "user@example.com",
        "alias_label": "wknd_email_id"
      },
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "low stock",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product",
            "WkQuantity": "1"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

{% details Beispiel mit E-Mail-Bezeichner (Alternative) %}
Wenn Sie den Canvas mit dem Braze-Feld `email` anstelle von `user_alias` Trigger or triggern or triggern, muss der Empfänger nur `email` und `prioritization` enthalten (siehe [Canvas-Nachrichten per API-getriggerter Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)). Das `context`-Objekt entspricht den anderen Beispielen.

```json
{
  "canvas_id": "<your_canvas_id>",
  "recipients": [
    {
      "email": "user@example.com",
      "prioritization": ["unidentified", "most_recently_updated"],
      "context": {
        "Origin": "wunderkind",
        "DataOnly": "Y",
        "UserType": "prospect",
        "WkOpen": "https://example.com/product",
        "WkPurpose": "product abandonment",
        "WKCouponCode": "",
        "WKCouponPurpose": "",
        "Items": [
          {
            "WkCopy": "Product name",
            "WkId": "012345",
            "WkImageUrl": "https://example.com/image.jpg",
            "WkUrl": "https://example.com/product"
          }
        ]
      }
    }
  ]
}
```
{% enddetails %}

### Beispiel für die Verwendung von Liquid {#example-liquid-usage}

Wenn Wunderkind `/canvas/trigger/send` aufruft, werden die Schlüssel und Werte, die Sie im `context`-Objekt jedes Empfängers übergeben, zu Canvas-Entry-Daten. In Nachrichtenschritten referenzieren Sie diese über den Liquid-Namespace `context`. Ein Beispiel ist {% raw %}`{{context.${WkPurpose}}}`{% endraw %}, wie unter [Canvas-Context-Objekt]({{site.baseurl}}/api/objects_filters/context_object) und [Nachricht]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) beschrieben. Über die korrekte Liquid-Syntax hinaus ist keine zusätzliche Konfiguration erforderlich.

Verschachteln Sie keine Braze-Ausgabe-Tags innerhalb der `for`-Tag-Bedingung. Weisen Sie das `Items`-Array aus `context` zuerst einer Variablen zu und iterieren Sie dann, wie unter [Liquid verwenden]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid#use-a-filter-result-in-a-for-loop) beschrieben. Die `assign`-Zeile verwendet das Canvas-Entry-Format von Braze: {% raw %}`{{context.${Items}}}`{% endraw %} (siehe [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags#summary-of-supported-tags)).

{% raw %}
```liquid
{% assign wk_items = {{context.${Items}}} %}
{% for item in wk_items %}
  <tr>
    <td>
      <a href="{{ item.WkUrl }}">
        <img src="{{ item.WkImageUrl }}" />
        <p>{{ item.WkCopy }}</p>
      </a>
    </td>
  </tr>
{% endfor %}
```
{% endraw %}

---

## Reporting

Wunderkind nimmt Performance-Daten aus Braze über **Braze Currents** auf, die Roh-Ereignisse an Google Cloud Storage streamen. Wunderkind normalisiert und aggregiert diese Ereignisse dann gegen das auslösende Signal für 1:1-Attribution-Reporting.

Die folgenden Metriken werden in Kürze im Wunderkind-Reporting-Dashboard verfügbar sein:

| Metrik | Quelle |
| ------ | ------ |
| Zugestellte Sendungen | Braze Currents |
| E-Mail-Öffnungen | Braze Currents |
| Klicks | Braze Currents |
| Conversions | Braze Currents (Ereignis wird bei der Einrichtung definiert) |
| Abmeldungen | Braze Currents |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reporting" }

## Einschränkungen {#limitations}

- **Keine Synchronisierung von Unterdrückung/Opt-out.** Die Unterdrückung muss nativ in Braze verwaltet werden. Hinweis: Für bestehende Wunderkind-Kund:innen, die zu Braze Signals migrieren, arbeitet Wunderkind mit Ihrem Team zusammen, um Ihre aktuelle Konfiguration beizubehalten.
- **Nur E-Mail-Kanal.** Kurzmitteilungsdienst or SMS wird derzeit über diese Integration nicht unterstützt.
- **Das Kundenprofil or Nutzerprofil muss vor dem Canvas-Trigger or triggern vorhanden sein.** [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) mit einem `user_alias`-Empfänger löst nur **vorhandene** Braze-Profile auf, die diesen Alias bereits besitzen. Sie können `send_to_existing_only` nicht mit Aliassen verwenden, und der Canvas-Trigger or triggern erstellt kein völlig neues Profil allein aus dem Alias. Die Nutzer:innen müssen zunächst erstellt oder aktualisiert und der Alias `wknd_email_id` gesetzt werden (zum Beispiel mit [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) oder [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)). Wunderkind wartet nach diesem Upsert möglicherweise kurz, damit Braze die Verarbeitung abschließen kann, bevor der Trigger or triggern ausgelöst wird.
- **E-Mail als Bezeichner.** Wenn der Canvas-Trigger or triggern die Empfänger:innen mit `email` statt mit `user_alias` identifiziert, geben Sie [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers) für dieses Empfängerobjekt an, wie von Braze vorgeschrieben.

## Zusätzliche Ressourcen {#additional-resources}

- [Wunderkind Help Center — Signals for Braze Overview](https://support.wunderkind.co/hc/en-us/articles/47156898436891-Signals-for-Braze-Overview)
- [Wunderkind Developer Portal — Integration Overview](https://developer.wunderkind.co/docs/integration-overview)
- [Canvas-Nachrichten mit API-getriggerter Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [Canvas-Kontextobjekt]({{site.baseurl}}/api/objects_filters/context_object)
- [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)