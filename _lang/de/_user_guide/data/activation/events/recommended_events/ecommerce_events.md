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

Der Tab **Commerce** in jedem Nutzerprofil kombiniert zwei Module: **Order activity** (berechnete Umsatz- und Bestellmetriken) und **Active cart** (der neueste Warenkorb aus `ecommerce.cart_updated`-Events).

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

Das Modul **Active cart** zeigt den neuesten Warenkorb im Nutzerprofil an. Diese Ansicht ist besonders hilfreich beim Testen. Sie können damit Warenkorb-Inhalte bestätigen, warenkorbbasierte Journeys validieren oder überprüfen, ob `ecommerce.cart_updated`-Events das Profil wie erwartet aktualisieren.

**Active cart** umfasst Folgendes:

- **Cart ID** – Bezeichner für den Warenkorb, der zuletzt ein `ecommerce.cart_updated`-Event erhalten hat.
- **Last updated** – Zeitstempel der letzten Warenkorb-Aktualisierung.
- **Total cart value** – Gesamtwert der Positionen im aktuellen Warenkorb.
- **View products** – Ein Link zum Öffnen der Produktliste im Warenkorb (bis zu 50 Produkte).

## E-Commerce-Orchestrierung {#ecommerce-orchestration}

### Segmentierung {#segmentation}

Braze bietet drei Möglichkeiten, Nutzer:innen auf Basis von E-Commerce-Daten zu segmentieren:

- **E-Commerce-Filter:** Verwenden Sie die Kategorie **eCommerce** im Segmenter, die Filter enthält, die auf empfohlenen E-Commerce-Events basieren (z. B. **Last Order Placed**, **Total Revenue** und **Average Order Value**). Eine vollständige Liste der verfügbaren Filter finden Sie unter [Segment-Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).
- **Filter für angepasste Events:** Da sich E-Commerce-Events wie angepasste Events verhalten, funktionieren alle vorhandenen Filter für angepasste Events sofort. Sie können beispielsweise nach „Hat das angepasste Event `ecommerce.order_placed` mehr als X Mal ausgeführt“ oder „Erstes Ausführen des angepassten Events `ecommerce.order_placed`“ filtern.
- **Segmenterweiterungen:** Für die Segmentierung anhand verschachtelter Event-Eigenschaften – einschließlich des verschachtelten Produkt-Arrays oder der Eigenschaften von Metadatenobjekten – verwenden Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension) mit Filterung nach verschachtelten Event-Eigenschaften. So können Sie Zielgruppen wie „Nutzer:innen, die Produkt SKU-123 in den letzten 90 Tagen gekauft haben“ erstellen oder Kriterien über verschiedene Eigenschaften derselben Bestellung hinweg kombinieren.

{% alert important %}
Segmenterweiterungen für empfohlene E-Commerce-Events sind ein kostenpflichtiges Feature mit eingeschränktem Vorabzugang. Wenn Sie am Vorabzugang teilnehmen möchten, wenden Sie sich an Ihren Customer-Success-Manager. Bestätigen Sie, dass Ihr Tarif den Zugang zur Segmentierung nach verschachtelten Eigenschaften umfasst, bevor Sie diese Funktion Ihrem Team empfehlen.
{% endalert %}

### Triggering {#triggering}

Sie können Trigger für ausgeführte angepasste Events mit E-Commerce-Events in Braze verwenden, genau wie bei anderen angepassten Events. Für Warenkorb-Abbruch-Flows verwenden Sie den Trigger **Perform Cart Updated Event**, um Warenkorb-Aktualisierungen korrekt zu erfassen.

Darüber hinaus bietet Braze einen dedizierten Trigger **Places Order**, mit dem Sie Journeys starten oder Aktionen auf Basis jeder aufgegebenen Bestellung oder auf Basis von Bestellungen auslösen können, die ein bestimmtes Produkt enthalten. Sie können diesen Trigger nach Produktname, `product_id` oder `variant_id` filtern, um bestimmte Kaufszenarien anzusprechen. Weitere Informationen finden Sie unter [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

![Trigger „Places Order“ mit ausgewählter Option zur Aufgabe einer beliebigen Bestellung.]({% image_buster /assets/img/recommended_events/places_order_trigger.png %})

### Liquid-Personalisierung {#liquid-personalization}

E-Commerce-Events unterstützen [Liquid-Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) auf die gleiche Weise wie angepasste Events; Sie können Event-Eigenschaften direkt in Ihren Nachrichten referenzieren. Um Produktbilder, Preise oder andere Katalogdaten in Ihre Nachrichten einzubinden, verknüpfen Sie Ihren Katalog mit dem Event über `product_id` oder `variant_id` als verbindenden Bezeichner. Mit dem {% raw %}`{% shopping_cart %}`{% endraw %} Liquid-Tag können Sie den aktuellen Warenkorbinhalt eines Nutzers bzw. einer Nutzerin durchlaufen – für Warenkorb-Abbruch-Erinnerungen, Checkout-Hinweise oder Bestellbestätigungen. Fertige Code-Beispiele finden Sie unter [E-Commerce-Anwendungsfälle]({{site.baseurl}}/ecommerce_use_cases).

Als No-Code-Alternative sind [Drag-and-Drop-Produktblöcke]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks) im Rahmen des Vorabzugangsprogramms verfügbar.

### E-Commerce-Canvas-Templates {#ecommerce-canvas-templates}

Braze bietet sofort einsetzbare Canvas-Templates, die mit empfohlenen E-Commerce-Events als Entry-, Exit- und Konversionskriterien vorkonfiguriert sind, sodass Sie Lifecycle-Flows ohne individuelle Einrichtung starten können. Jedes Template enthält Drag-and-Drop-E-Mail-Designs und unterstützt Drag-and-Drop-Produktblöcke (derzeit im Vorabzugang). Ausführliche Anwendungsfälle und Liquid-Beispiele finden Sie unter [E-Commerce-Anwendungsfälle]({{site.baseurl}}/ecommerce_use_cases).

Diese Templates decken die häufigsten E-Commerce-Lifecycle-Flows ab. Verwenden Sie sie als Ausgangspunkt und passen Sie dann Timing, Kanäle und Gestaltung für Ihre Zielgruppe an.

{% tabs %}
{% tab Abgebrochenes Browsen %}

Spricht Nutzer:innen erneut an, die ein Produkt angesehen, es aber nicht in den Warenkorb gelegt haben.

Verwenden Sie dieses Template, wenn Sie Nutzer:innen dazu bringen möchten, Produkte erneut in Betracht zu ziehen, die sie kürzlich angesehen, aber nicht weiterverfolgt haben.

| Einstellung | Wert |
| --- | --- |
| Entry-Event | `ecommerce.product_viewed` |
| Exit-Events | `ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Konversions-Event | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Commerce-Canvas-Templates" }

{% endtab %}
{% tab Warenkorb-Abbruch %}

Gewinnt Nutzer:innen zurück, die Artikel in den Warenkorb gelegt, aber den Checkout nicht begonnen haben.

Verwenden Sie dieses Template, wenn Sie Nutzer:innen an Artikel in ihrem Warenkorb erinnern und sie dazu bewegen möchten, den Checkout abzuschließen.

| Einstellung | Wert |
| --- | --- |
| Entry-Event | `ecommerce.cart_updated` |
| Exit-Events | `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Konversions-Event | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Commerce-Canvas-Templates" }

{% alert tip %}
Das Event `ecommerce.cart_updated` unterstützt sowohl vollständigen Warenkorbersatz (jedes Event kann den gesamten Warenkorb beschreiben) als auch inkrementelle Aktualisierungen mit den Werten `add` und `remove` für die optionale Eigenschaft `action`. Wählen Sie einen Ansatz pro Warenkorb und vermeiden Sie es, Ersatz- und inkrementelle Warenkorbaktualisierungen für dieselbe `cart_id` zu mischen. Verwenden Sie den {% raw %}`{% shopping_cart %}`{% endraw %} Liquid-Tag in Ihrer Nachricht, um den aktuellen Warenkorbinhalt zum Sendezeitpunkt dynamisch darzustellen.
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

Bestätigt einen erfolgreichen Kauf und sendet eine Feedback-Umfrage nach, um Bewertungen und Engagement nach dem Kauf zu fördern.

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
  - **E-Mail anpassen:** Jedes Template enthält eine vorkonfigurierte E-Mail, die mit dem Drag-and-Drop-Editor erstellt wurde und vollständig bearbeitbar ist, um sie an Ihre Marke und Ihre Inhalte anzupassen.
  - **Kanäle hinzufügen:** Kombinieren Sie E-Mail mit Push, SMS oder In-App-Nachrichten für kanalübergreifende Verstärkung.
  - **Verzögerungen und Decision-Splits hinzufügen:** Verzweigen Sie Nutzer:innen nach Verhalten (z. B. hochwertiger Warenkorb im Vergleich zu niedrigwertigem Warenkorb) oder Wartezeiten zwischen Nachrichten.
  - **Gestaltung austauschen:** Ersetzen Sie das enthaltene E-Mail-Template durch den visuellen Stil Ihrer Marke.
  - **Produktblöcke verwenden:** Nutzen Sie Drag-and-Drop-Produktblöcke (im Vorabzugangsprogramm), um abgebrochene Warenkorbinhalte oder angesehene Produkte dynamisch darzustellen, ohne eigenes Liquid schreiben zu müssen.

Für fortgeschrittene Lifecycle-Strategien, einschließlich Beispielen zur Liquid-Personalisierung, siehe [E-Commerce-Anwendungsfälle]({{site.baseurl}}/ecommerce_use_cases).

## E-Commerce-Reporting {#ecommerce-reporting}

E-Commerce-Empfehlungs-Events unterstützen dieselben Umsatz-Oberflächen, die Kund:innen bereits heute verwenden. Wenn Ihre Integration E-Commerce-Events sendet, enthalten die folgenden Berichte automatisch E-Commerce-Umsätze:

| Bericht | Was er anzeigt |
|---------------------------------------------|-------------------------------------------|
| Umsatzbericht | Gesamtumsatz, durchschnittlicher Tagesumsatz, tägliche Käufe und Umsatz pro Nutzer:in im Zeitverlauf über alle Quellen für den ausgewählten Datumsbereich und die ausgewählten Apps. |
| Last-Touch-Attribution-Umsatz-Dashboard | Umsatz, der der letzten Campaign oder dem letzten Canvas zugeordnet wird, mit der bzw. dem ein:e Nutzer:in vor einer Bestellung interagiert hat. Touch-Events umfassen E-Mail-Klicks, Push-Öffnungen, Content-Card-Klicks, In-App-Nachrichten-Klicks sowie SMS- oder WhatsApp-Kurzlink-Klicks. |
| Campaign- und Canvas-Analytics | Gesamtumsatz, der einer bestimmten Campaign oder einem bestimmten Canvas innerhalb des primären Konversionsfensters zugeordnet wird. |
| Konversionsbericht | Umsatz, der an Konversions-Events in Campaigns und Canvases gebunden ist.<br> **Hinweis:** Um den Umsatz von `ecommerce.order_placed` zu zählen, muss die Campaign oder das Canvas den Konversions-Event-Typ „Place Order“ als Konversions-Event verwenden. |
| Segment-Insights | Umsatzvergleiche über Segmente im Segment-Insights-Dashboard. |
| Berichts-Builder | Umsatz-Metriken in angepassten Berichten, die im Berichts-Builder erstellt wurden. |
| Dashboard-Builder | Umsatz-Metriken in angepassten Dashboards, die im Dashboard-Builder erstellt wurden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Commerce-Reporting" }

Für nicht nutzerbezogene berechnete Felder (zum Beispiel Campaign- oder Canvas-Umsatz) wird der Umsatz in allen Berichten auf dieselbe Weise berechnet: `price` multipliziert mit `quantity` pro Produkt in der Bestellung, summiert über die Produkte in jedem `order_placed`-Event.

{% alert note %}
Umsatzberechnungen begrenzen einzelne Produktmengen auf 1.000 Einheiten pro Bestellung. Wenn ein Mengenfeld für ein Produkt fehlt, wird standardmäßig eine Einheit angenommen. Das ursprüngliche `ecommerce.order_placed`-Event behält die vollständige Menge bei, die Sie gesendet haben – nur die Umsatzberechnung wendet die Obergrenze an.<br><br>
Wenn Sie von veralteten Kauf-Events zu `ecommerce.order_placed` migrieren, stimmen Sie sich mit Ihrem Braze-Kontoteam ab, bevor Sie Änderungen an der Integration vornehmen. Senden Sie während der Übergangsphase sowohl veraltete Kauf-Events als auch `ecommerce.order_placed`-Events, um zu bestätigen, dass sie korrekt ausgelöst werden, und um Ihre aktiven Campaigns, Canvases und Segmente für die Migration auf das neue Event vorzubereiten. Ihr Kontoteam kann Ihnen dann bei der Planung der Umstellung helfen, um das Umsatz-Reporting von veralteten Kauf-Events auf `ecommerce.order_placed` umzustellen.
{% endalert %}

### BrazeAI<sup>TM</sup>

[Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events), [voraussichtliche Abwanderung]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) und [Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/item_recommendations) unterstützen E-Commerce-Events als Ziel-Events und Signale und bieten eine dedizierte Option „Order Placed“. Das standardisierte Schema macht diese Modelle zuverlässiger, da die Daten über Ihre gesamte Nutzerbasis hinweg konsistent sind.

### Daten exportieren {#export-data}

Braze bietet verschiedene Möglichkeiten, E-Commerce-Event-Daten für die Verwendung in Ihrem Data Warehouse, Ihren BI-Tools oder nachgelagerten Systemen zu exportieren. E-Commerce-Empfehlungs-Events werden über dieselben Kanäle exportiert wie Ihre anderen Event-Daten.

| Exportpfad | Was enthalten ist |
|------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) | E-Commerce-Events werden als angepasste Events gestreamt. Suchen Sie im Namespace `ecommerce.*`, um sie zu finden. Produkte aus jeder Bestellung sind als Käufe verfügbar. |
| [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing) | E-Commerce-Events werden als angepasste Events geteilt. Suchen Sie im Namespace `ecommerce.*`, um sie zu finden. Produkte aus jeder Bestellung sind in der Kauftabelle verfügbar. |
| [Segmentdaten als CSV exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv) | CSV-Export von Segmentmitgliedern. Um E-Commerce-Events einzuschließen, wählen Sie sie namentlich aus dem Dropdown der angepassten Events aus. |
| [Nutzerprofil nach Segment exportieren (API)]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#prerequisites) | Nutzerprofile für Segmentmitglieder, die über die API zurückgegeben werden. E-Commerce-Events sind als angepasste Events enthalten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Daten exportieren" }

### Wie segmentiere ich Nutzer:innen nach einem bestimmten Produkt? {#how-do-i-segment-users-by-a-specific-product}

Der Segmentierer ermöglicht es Ihnen, nach der Anzahl der Ausführungen eines E-Commerce-Events durch eine:n Nutzer:in zu filtern. Um nach bestimmten Produkteigenschaften zu filtern (wie `product_id` oder `product_name`), verwenden Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension), die die Filterung nach verschachtelten Event-Eigenschaften unterstützen. So können Sie beispielsweise alle Nutzer:innen finden, die das Produkt „SKU-123“ in den letzten 90 Tagen gekauft haben.