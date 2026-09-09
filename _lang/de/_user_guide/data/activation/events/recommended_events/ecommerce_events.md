---
nav_title: Empfohlene E-Commerce-Events verwenden
article_title: So verwenden Sie E-Commerce-Events
page_type: reference
alias: /ecommerce_events/
description: "Erfahren Sie, wie Sie empfohlene E-Commerce-Events in Braze verwenden – einschließlich unterstützter Features, wichtiger Metriken und Best Practices für Segmentierung, Messaging und Reporting."
---

# So verwenden Sie E-Commerce-Events {#how-to-use-ecommerce-events}

> Empfohlene E-Commerce-[Events]({{site.baseurl}}/recommended_events) verwenden ein gemeinsames Schema auf Bestellebene, das es Braze ermöglicht, zuverlässige Features auf Basis Ihrer E-Commerce-Daten zu erstellen – einschließlich Nutzerprofilen, Segmentierung, Messaging, Reporting und KI-gestützten Empfehlungen. Die Abschnitte in diesem Artikel beschreiben, wie Sie jede Funktion in Braze nutzen können.<br><br> Unter [Event-Schemas]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas) finden Sie Anforderungen an Eigenschaften und Datentypen, und unter [Event-Validierung und Fehlerbehebung]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-validation-and-troubleshooting) erfahren Sie, was passiert, wenn ein Event die Validierung nicht besteht.

Da E-Commerce-Events einem vorhersehbaren Schema folgen, kann Braze zuverlässige Features darauf aufbauen – von Umsatz-Tracking und vorgefertigten Canvas-Templates bis hin zu KI-gestützten Empfehlungen. Die folgenden Abschnitte geben Ihnen einen schnellen Überblick über jede Funktion mit Links zur vollständigen Dokumentation.

{% alert note %}
E-Commerce-Events von Braze und ihre segmentierbaren Event-Eigenschaften zählen nicht als [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points).
{% endalert %}

<a id="transactions-tab" aria-hidden="true"></a>

## Tab „Commerce“ {#commerce-tab}

Der Tab **Commerce** in jedem Kundenprofil kombiniert zwei Module: **Order activity** (berechnete Umsatz- und Bestellmetriken) und **Active cart** (der neueste Warenkorb aus `ecommerce.cart_updated`-Events).

### Bestellaktivität {#order-activity}

Das Modul **Order activity** zeigt drei berechnete Metriken an, die sich in Echtzeit aktualisieren, sobald Events verarbeitet werden. Das Modell auf Bestellebene dieser Berechnungen trennt Produktpreise sauber vom Gesamtbestellwert.

{% alert note %}
Empfohlene E-Commerce-Events werden nicht im Abschnitt **Purchase history** des Tabs **Commerce** angezeigt. Die Kaufhistorie wird durch Legacy-Kauf-Events befüllt. Verwenden Sie die Metriken in der folgenden Tabelle für Umsatz und Bestellaktivität aus empfohlenen Events.
{% endalert %}

| Metrik | Formel |
| ----- | ----- |
| Gesamtumsatz | Summe (`order_placed.total_value`) − Summe (`order_refunded.total_value`) |
| Gesamtbestellungen | Anzahl (eindeutige `order_placed`) − Anzahl (eindeutige `order_cancelled`) |
| Gesamter Erstattungswert | Summe (`order_refunded.total_value`) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Metriken der Bestellaktivität" }

### Aktiver Warenkorb {#active-cart}

Das Modul **Active cart** zeigt den neuesten Warenkorb im Kundenprofil an. Diese Ansicht ist besonders hilfreich beim Testen. Sie können damit Warenkorb-Inhalte bestätigen, warenkorbbasierte Journeys validieren oder überprüfen, ob `ecommerce.cart_updated`-Events das Profil wie erwartet aktualisieren.

**Active cart** umfasst Folgendes:

- **Cart ID** – Bezeichner für den Warenkorb, der zuletzt ein `ecommerce.cart_updated`-Event erhalten hat.
- **Last updated** – Zeitstempel der letzten Warenkorb-Aktualisierung.
- **Total cart value** – Gesamtwert der Positionen im aktuellen Warenkorb.
- **View products** – Ein Link zum Öffnen der Produktliste im Warenkorb (bis zu 50 Produkte).

## E-Commerce-Orchestrierung {#ecommerce-orchestration}

### Segmentierung {#segmentation}

Braze bietet drei Möglichkeiten, Nutzer:innen auf Basis von E-Commerce-Daten zu segmentieren:

- **E-Commerce-Filter:** Verwenden Sie die Kategorie **eCommerce** im Segmentierer, die Filter enthält, die von empfohlenen E-Commerce-Events unterstützt werden (z. B. **Last Order Placed**, **Total Revenue** und **Average Order Value**). Eine vollständige Liste der verfügbaren Filter finden Sie unter [Segment-Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).
- **Filter für angepasste Events:** Da sich E-Commerce-Events wie angepasste Events verhalten, funktionieren alle vorhandenen Filter für angepasste Events sofort. Sie können beispielsweise nach „Hat angepasstes Event `ecommerce.order_placed` mehr als X Mal ausgeführt“ oder „Hat angepasstes Event `ecommerce.order_placed` erstmals ausgeführt“ filtern.
- **Segmenterweiterungen:** Um nach verschachtelten Event-Eigenschaften zu segmentieren – einschließlich des verschachtelten Produkt-Arrays oder der Metadaten-Objekteigenschaften – verwenden Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension) mit Filterung verschachtelter Event-Eigenschaften. So können Sie Zielgruppen wie „Nutzer:innen, die Produkt SKU-123 in den letzten 90 Tagen gekauft haben“ erstellen oder Kriterien über verschiedene Eigenschaften derselben Bestellung hinweg kombinieren.

Wenn Sie nach angepassten Eigenschaften filtern müssen, die nicht Teil des dokumentierten Event-Schemas sind, verschachteln Sie diese beim Protokollieren des Events unter `metadata` (z. B. `metadata.color` anstelle von `color`). Angepasste Top-Level-Eigenschaften, die Sie über die API oder das SDK senden, sind für Erweiterungseigenschafts-Filter nicht gültig – selbst wenn diese Eigenschaften in Ihren Event-Daten erscheinen. Die Verwendung einer nicht zugelassenen Top-Level-Eigenschaft verhindert, dass die Erweiterung gespeichert oder dearchiviert werden kann.

{% alert important %}
Segmenterweiterungen für empfohlene E-Commerce-Events sind ein kostenpflichtiges Feature im Early Access. Wenn Sie an der Teilnahme am Early Access interessiert sind, wenden Sie sich an Ihren Customer-Success-Manager. Bestätigen Sie, dass Ihr Tarif den Zugang beinhaltet, bevor Sie Ihrem Team die Segmentierung nach verschachtelten Eigenschaften empfehlen.
{% endalert %}

### Triggering {#triggering}

Sie können Trigger für ausgeführte angepasste Events mit E-Commerce-Events in ganz Braze verwenden, genau wie bei anderen angepassten Events. Für Warenkorb-Abbruch-Flows verwenden Sie den Trigger **Perform Cart Updated Event**, um Warenkorb-Aktualisierungen korrekt zu erfassen.

Darüber hinaus bietet Braze einen dedizierten **Places Order**-Trigger, mit dem Sie Journeys starten oder Aktionen basierend auf jeder aufgegebenen Bestellung auslösen können – oder auf Bestellungen, die ein bestimmtes Produkt enthalten. Sie können diesen Trigger nach Produktname, `product_id` oder `variant_id` filtern, um bestimmte Kaufszenarien anzusprechen. Weitere Informationen finden Sie unter [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

![Places-Order-Trigger mit einer ausgewählten Option, eine beliebige Bestellung aufzugeben.]({% image_buster /assets/img/recommended_events/places_order_trigger.png %})

### Liquid-Personalisierung {#liquid-personalization}

E-Commerce-Events unterstützen die [Liquid-Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) auf die gleiche Weise wie angepasste Events. Sie können Event-Eigenschaften direkt in Ihren Nachrichten referenzieren. Um Produktbilder, Preise oder andere Katalogdaten in Ihre Nachrichten einzubinden, verknüpfen Sie Ihren Katalog mit dem Event über `product_id` oder `variant_id` als Verbindungskennung. Das {% raw %}`{% shopping_cart %}`{% endraw %} Liquid-Tag ermöglicht es Ihnen, durch die aktuellen Warenkorbinhalte eines Nutzers bzw. einer Nutzerin zu iterieren – für Warenkorb-Abbruch-Erinnerungen, Checkout-Hinweise oder Bestellbestätigungen. Fertige Code-Beispiele finden Sie unter [E-Commerce-Anwendungsfälle]({{site.baseurl}}/ecommerce_use_cases).

Als No-Code-Alternative sind [Drag-and-Drop-Produktblöcke]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks) im Early-Access-Programm verfügbar.

### E-Commerce-Canvas-Templates {#ecommerce-canvas-templates}

Braze stellt sofort einsatzbereite Canvas-Templates bereit, die mit empfohlenen E-Commerce-Events als Entry-, Exit- und Konversionskriterien vorkonfiguriert sind, damit Sie Lifecycle-Flows ohne individuelle Einrichtung starten können. Jedes Template wird mit Drag-and-Drop-E-Mail-Designs geliefert und unterstützt Drag-and-Drop-Produktblöcke (derzeit im Early Access). Detaillierte Anwendungsfälle und Liquid-Beispiele finden Sie unter [E-Commerce-Anwendungsfälle]({{site.baseurl}}/ecommerce_use_cases).

Diese Templates decken die gängigsten E-Commerce-Lifecycle-Flows ab. Verwenden Sie sie als Ausgangspunkt und passen Sie dann Timing, Kanäle und Kreativelemente für Ihre Zielgruppe an.

{% tabs %}
{% tab Abgebrochenes Browsen %}

Spricht Nutzer:innen erneut an, die ein Produkt angesehen, es aber nicht in den Warenkorb gelegt haben.

Verwenden Sie dieses Template, wenn Sie Besucher:innen dazu bringen möchten, Produkte erneut in Betracht zu ziehen, die sie kürzlich angesehen, aber nicht weiter verfolgt haben.

| Einstellung | Wert |
| --- | --- |
| Entry-Event | `ecommerce.product_viewed` |
| Exit-Events | `ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Konversions-Event | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Commerce-Canvas-Templates" }

{% endtab %}
{% tab Warenkorb-Abbruch %}

Gewinnt Nutzer:innen zurück, die Artikel in den Warenkorb gelegt, aber den Checkout nicht begonnen haben.

Verwenden Sie dieses Template, wenn Sie Nutzer:innen an Artikel in ihrem Warenkorb erinnern und sie dazu bringen möchten, den Checkout abzuschließen.

| Einstellung | Wert |
| --- | --- |
| Entry-Event | `ecommerce.cart_updated` |
| Exit-Events | `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Konversions-Event | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Commerce-Canvas-Templates" }

{% alert tip %}
Das `ecommerce.cart_updated`-Event unterstützt vollständigen Warenkorbersatz (jedes Event kann den gesamten Warenkorb beschreiben) oder inkrementelle Updates mit den Werten `add` und `remove` für die optionale Eigenschaft `action`. Wählen Sie einen Ansatz pro Warenkorb und vermeiden Sie es, Ersatz- und inkrementelle Warenkorb-Updates für dieselbe `cart_id` zu mischen. Der gespeicherte Warenkorb behält die `currency` des letzten Warenkorb-Events bei; ein Warenkorb-Update in einer anderen Währung ersetzt den gespeicherten Warenkorb, anstatt Werte aus zwei Währungen zu mischen. Verwenden Sie das {% raw %}`{% shopping_cart %}`{% endraw %} Liquid-Tag in Ihrer Nachricht, um die aktuellen Warenkorbinhalte zum Versandzeitpunkt dynamisch anzuzeigen.
{% endalert %}

{% endtab %}
{% tab Abgebrochener Checkout %}

Gewinnt Nutzer:innen zurück, die den Checkout begonnen, aber den Kauf nicht abgeschlossen haben.

Verwenden Sie dieses Template, wenn Sie Käufe in der Phase mit der höchsten Kaufabsicht im Funnel zurückgewinnen möchten.

| Einstellung | Wert |
| --- | --- |
| Entry-Event | `ecommerce.checkout_started` |
| Exit-Event | Placed Order |
| Konversions-Event | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Commerce-Canvas-Templates" }

{% endtab %}
{% tab Bestellbestätigung und Umfrage %}

Bestätigt einen erfolgreichen Kauf und folgt mit einer Feedback-Umfrage nach, um Bewertungen zu sammeln und das Engagement nach dem Kauf zu fördern.

Verwenden Sie dieses Template, wenn Sie die Kommunikation nach dem Kauf optimieren und Kundenfeedback in einem einzigen Workflow erfassen möchten.

| Einstellung | Wert |
| --- | --- |
| Entry-Event | `ecommerce.order_placed` |
| Konversions-Event | Start Session oder `ecommerce.product_viewed` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Commerce-Canvas-Templates" }

{% endtab %}
{% endtabs %}

#### Templates anpassen {#customize-templates}

Diese Templates sind als Ausgangspunkt konzipiert. Häufige Anpassungen umfassen:
  - **E-Mail anpassen:** Jedes Template enthält eine vorkonfigurierte E-Mail, die mit dem Drag-and-Drop-Editor erstellt wurde und vollständig bearbeitet werden kann, um zu Ihrer Marke und Ihrem Inhalt zu passen.
  - **Kanäle hinzufügen:** Kombinieren Sie E-Mail mit Push, SMS oder In-App-Nachrichten für kanalübergreifende Verstärkung.
  - **Verzögerungen und Decision-Splits hinzufügen:** Verzweigen Sie Nutzer:innen nach Verhalten (z. B. hochwertiger Warenkorb im Vergleich zu niedrigwertigem Warenkorb) oder fügen Sie Wartezeiten zwischen Nachrichten ein.
  - **Kreativelemente austauschen:** Ersetzen Sie das enthaltene E-Mail-Template durch den visuellen Stil Ihrer Marke.
  - **Produktblöcke verwenden:** Nutzen Sie Drag-and-Drop-Produktblöcke (im Early-Access-Programm), um abgebrochene Warenkorbinhalte oder angesehene Produkte dynamisch darzustellen, ohne angepasstes Liquid schreiben zu müssen.

Für fortgeschrittenere Lifecycle-Strategien, einschließlich Liquid-Personalisierungsbeispielen, siehe [E-Commerce-Anwendungsfälle]({{site.baseurl}}/ecommerce_use_cases).

## E-Commerce-Berichte {#ecommerce-reporting}

Empfohlene E-Commerce-Events speisen dieselben Umsatzoberflächen, die Kund:innen bereits heute nutzen. Wenn Ihre Integration E-Commerce-Events sendet, enthalten die folgenden Berichte E-Commerce-Umsätze automatisch:

| Bericht                                      | Was er zeigt                             |
|---------------------------------------------|-------------------------------------------|
| Umsatzbericht                              | Gesamtumsatz, durchschnittlicher Tagesumsatz, tägliche Käufe und Umsatz pro Nutzer:in im Zeitverlauf über alle Quellen für den ausgewählten Zeitraum und die ausgewählten Apps.                                                                                     |
| Last-Touch-Attribution-Umsatz-Dashboard     | Umsatz, der der letzten Campaign oder dem letzten Canvas zugeordnet wird, mit der/dem eine Nutzer:in vor einer Bestellung interagiert hat. Touch-Events umfassen E-Mail-Klicks, Push-Öffnungen, Content-Card-Klicks, In-App-Nachrichten-Klicks sowie SMS- oder WhatsApp-Kurzlink-Klicks. |
| Campaign- und Canvas-Analytics                | Gesamtumsatz, der einer bestimmten Campaign oder einem bestimmten Canvas innerhalb des primären Konversionsfensters zugeordnet wird.                                                                                   |
| Konversionsbericht                          | Umsatz, der an Konversions-Events in Campaigns und Canvases gebunden ist.<br> **Hinweis:** Um den Umsatz von `ecommerce.order_placed` zu zählen, muss die Campaign oder das Canvas den Konversions-Event-Typ „Place Order“ als Konversions-Event verwenden.                                                                                    |
| Segment-Insights                            | Umsatzvergleiche über Segments hinweg im Segment-Insights-Dashboard.                                                               |
| Berichts-Builder                              | Umsatz-Metriken in benutzerdefinierten Berichten, die im Berichts-Builder erstellt wurden.                                                                                  |
| Dashboard-Builder                           | Umsatz-Metriken in benutzerdefinierten Dashboards, die im Dashboard-Builder erstellt wurden.                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Commerce-Berichte" }

Für nicht nutzerbezogene berechnete Felder (zum Beispiel Campaign- oder Canvas-Umsatz) wird der Umsatz in allen Berichten auf die gleiche Weise berechnet: `price` multipliziert mit `quantity` pro Produkt in der Bestellung, summiert über die Produkte in jedem `order_placed`-Event.

{% alert note %}
Bei der Umsatzberechnung werden individuelle Produktmengen auf 1.000 Einheiten pro Bestellung begrenzt. Wenn ein Mengenfeld für ein Produkt fehlt, wird standardmäßig eine Einheit angenommen. Das ursprüngliche `ecommerce.order_placed`-Event behält die vollständige von Ihnen gesendete Menge bei – nur die Umsatzberechnung wendet die Begrenzung an.<br><br>
Wenn Sie von Legacy-Kauf-Events zu `ecommerce.order_placed` migrieren, stimmen Sie sich mit Ihrem Braze-Konto-Team ab, bevor Sie Änderungen an der Integration vornehmen. Senden Sie während der Übergangsphase sowohl Legacy-Kauf- als auch `ecommerce.order_placed`-Events, um zu bestätigen, dass sie korrekt ausgelöst werden, und um Ihre aktiven Campaigns, Canvases und Segments auf die Migration zum neuen Event vorzubereiten. Ihr Konto-Team kann Ihnen dann helfen, die Umstellung zu planen, um die Umsatzberichterstattung von Legacy-Kauf-Events auf `ecommerce.order_placed` umzustellen.
{% endalert %}

### BrazeAI<sup>TM</sup>

[Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events), [voraussichtliche Abwanderung]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) und [Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/item_recommendations) unterstützen E-Commerce-Events als Ziel-Events und Signale und verfügen über eine dedizierte Option „Order Placed“. Das standardisierte Schema macht diese Modelle zuverlässiger, da die Daten über Ihre gesamte Nutzerbasis hinweg konsistent sind.

### Daten exportieren {#export-data}

Braze bietet mehrere Möglichkeiten, E-Commerce-Event-Daten für die Verwendung in Ihrem Data Warehouse, BI-Tools oder nachgelagerten Systemen zu exportieren. Empfohlene E-Commerce-Events werden über dieselben Kanäle wie Ihre anderen Event-Daten exportiert.

| Exportpfad                         | Was enthalten ist                                                                                                                                                                                 |
|------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)                            | E-Commerce-Events werden als angepasste Events gestreamt; suchen Sie im `ecommerce.*`-Namespace, um sie zu finden. Produkte aus jeder Bestellung sind als Käufe verfügbar.                                                |
| [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing)               | E-Commerce-Events werden als angepasste Events geteilt; suchen Sie im `ecommerce.*`-Namespace, um sie zu finden. Produkte aus jeder Bestellung sind in der Kauftabelle verfügbar.                                   |
| [Segment-Daten als CSV exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv)           | CSV-Export von Segment-Mitgliedern. Um E-Commerce-Events einzuschließen, wählen Sie sie nach Namen aus dem Dropdown für angepasste Events aus.                                                                                |
| [Nutzerprofil nach Segment exportieren (API)]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#prerequisites) | Nutzerprofile für Segment-Mitglieder, die über die API zurückgegeben werden. E-Commerce-Events sind als angepasste Events enthalten.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Daten exportieren" }

### Wie segmentiere ich Nutzer:innen nach einem bestimmten Produkt? {#how-do-i-segment-users-by-a-specific-product}

Der Segmentierer ermöglicht es Ihnen, nach der Anzahl der Ausführungen eines E-Commerce-Events durch eine Nutzer:in zu filtern. Um nach bestimmten Produkteigenschaften (wie `product_id` oder `product_name`) zu filtern, verwenden Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension), die das Filtern nach verschachtelten Event-Eigenschaften unterstützen. So können Sie beispielsweise alle Nutzer:innen finden, die das Produkt „SKU-123“ in den letzten 90 Tagen gekauft haben.