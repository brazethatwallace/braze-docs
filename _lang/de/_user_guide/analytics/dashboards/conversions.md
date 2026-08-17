---
nav_title: Conversions
article_title: Conversions-Dashboard
alias: "/conversions_dashboard_v2/"
description: "Das Conversions-Dashboard ermöglicht es Ihnen, Conversions über Kampagnen, Canvases und Kanäle hinweg mit verschiedenen Attributionsmethoden zu analysieren."
page_order: 3
page_type: reference
tool:
  - Reports
---

# Conversions-Dashboard {#conversions-dashboard}

> Das Conversions-Dashboard analysiert Conversions über Kampagnen, Canvases und Kanäle hinweg mithilfe verschiedener [Attributionsmethoden](#attribution-methods). Bei der Messung Ihrer Conversions können Sie den Zeitraum, das Konversions-Event und das Konversionsfenster festlegen.

## Einrichten Ihres Berichts {#setting-up-your-report}

So richten Sie Ihren Bericht im Konversions-Dashboard ein:

1. Gehen Sie zu **Analytics** > **Conversions**.
2. Wählen Sie einen **Date Range** für Ihren Bericht aus – bis zu einem Zeitfenster von 90 Tagen.
3. Wählen Sie die Campaigns oder Canvases (oder beides) aus, die Sie analysieren möchten.
   - (optional) Filtern Sie Campaigns und Canvases, indem Sie einen Tag auswählen.
4. Wählen Sie den/die **Channel(s)** aus, die Sie für Ihre Nachrichten analysieren möchten.
5. Wählen Sie eine **Breakdown by**-Ebene aus, um verschiedene Dimensionen der Daten anzuzeigen, z. B. nach Variante, Canvas-Schritt, Land oder Sprache.
6. (Optional) Wenn Sie Konversionen eines Events berechnen möchten, das nicht als Konversions-Event in der Campaign oder dem Canvas eingerichtet wurde, aktivieren Sie [Angepasste Events verwenden](#using-custom-events).
7. Wählen Sie eine [Attributionsmethode](#attribution-methods) aus, mit der die ausgewählten Nachrichten analysiert werden sollen.

{% alert note %}
Wenn Sie Konversionen für mehrere Kanäle analysieren, wird Ihre **Attribution Method** standardmäßig auf **Last-Touch Attribution** gesetzt.
{% endalert %}

{:start="8"}
8. Wählen Sie **Create** aus, um den Bericht zu erstellen.

Nachdem die Seite geladen wurde, wählen Sie ein **Conversion Event** aus, um den Bericht nach Konversionsdaten zu filtern. Die verfügbaren Auswahlmöglichkeiten umfassen die Events, die in den Canvases und Campaigns vorkonfiguriert wurden. Wenn Sie beim Einrichten Ihres Berichts (Schritt 6) ein angepasstes Event ausgewählt haben, ist diese Option nicht verfügbar.

### Angepasste Events verwenden {#using-custom-events}

Damit Metriken für angepasste Events im Konversions-Dashboard angezeigt werden, müssen Sie ein Konversions-Event und ein Canvas-Entry-Event im auf der Seite angegebenen Datumsbereich haben.

Um Konversionen eines Events zu berechnen, das nicht als Konversions-Event in der Campaign oder dem Canvas eingerichtet wurde, wählen Sie ein bestimmtes angepasstes Event aus, das als Konversions-Event verwendet werden soll.

1. Aktivieren Sie beim Einrichten Ihres Berichts **Use custom events**.
2. Wählen Sie ein angepasstes Event aus, das als Konversions-Event verwendet werden soll.
3. Wählen Sie das Konversionsfenster aus, innerhalb dessen das Event stattgefunden haben muss, um als Konversion gezählt zu werden.

{% alert note %}
Wenn Sie ein angepasstes Event auswählen, wird das **Conversion Event**-Dropdown auf der Seite nicht angezeigt, und Sie müssen den Bericht erneut ausführen, um Konversionen für verschiedene angepasste Events anzuzeigen.
{% endalert %}

### Hinweise {#considerations}

Damit Nutzer:innen im Bericht gezählt werden, müssen sie innerhalb des ausgewählten Datumsbereichs die folgenden Kriterien erfüllen:
1. In den Canvas oder die Campaign eintreten.
2. Eine [Attributionsmethode]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods) protokollieren.
3. Das Konversions-Event ausführen.

Nehmen wir zum Beispiel an, dass Nutzer:innen Folgendes tun:
1. Am 30. September in den Canvas eintreten.
2. Am 1. Oktober eine Attributionsmethode protokollieren.
3. Am 2. Oktober das Konversions-Event ausführen.

Diese Nutzer:innen werden **nicht** in einem Bericht mit einem Datumsbereich vom 1. Oktober bis 7. Oktober erscheinen. Das liegt daran, dass die Nutzer:innen vor dem Berichtszeitraum in den Canvas eingetreten sind, obwohl das Konversions-Event innerhalb des definierten Datumsbereichs stattfand. Damit die Nutzer:innen im Bericht erscheinen, muss der Datumsbereich den 30. September einschließen.

## Ihren Bericht verstehen {#understanding-your-report}

Ihr Bericht ist in drei Abschnitte unterteilt:

- [Konversionsdetails](#conversion-details)
- [Konversions-Funnel](#conversion-funnel)
- [Konversionen im Zeitverlauf](#conversions-over-time)

### Konversionsdetails {#conversion-details}

Die Tabelle mit den Konversionsdetails zeigt immer eine Spalte für *Empfänger:innen* und eine weitere für *Konversionen* (Rate und Gesamtzahl). Die verbleibenden zwei Tabellenspalten hängen von den Optionen ab, die Sie beim Einrichten Ihres Berichts ausgewählt haben.

![Tabelle mit Konversionsdetails, die Touches als Attributionsmethode für die Spalten drei und vier zeigt.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

Die folgende Tabelle beschreibt die möglichen Metriken.

| Angezeigte Metrik | Beschreibung |
| --- | --- |
| Empfänger:innen | Die Anzahl der Nutzer:innen, die innerhalb des Berichtszeitraums eine Nachricht über den ausgewählten Kanal erhalten haben |
| Konversionsrate (Empfänger:innen) | Berechnet als: (Anzahl der Konversionen) / (Anzahl der Empfänger:innen) |
| Attributionsmethode | Definiert durch die [Attributionsmethode](#attribution-methods), die Sie beim Einrichten des Berichts ausgewählt haben. Bei Last-Touch-Attribution oder wenn mehrere Kanäle ausgewählt sind, wird dies als [Touches](#terms-to-know) angezeigt. |
| Konversionsrate (Attributionsmethode) | Definiert durch die [Attributionsmethode](#attribution-methods), die Sie beim Einrichten des Berichts ausgewählt haben. Wenn mehrere Kanäle ausgewählt sind, wird standardmäßig die Last-Touch-Attribution verwendet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Konversionsdetails" }

Wenn Sie beim [Einrichten Ihres Berichts](#setting-up-your-report) (Schritt 5) Details auf Aufschlüsselungsebene für Campaigns oder Canvases ausgewählt haben, können Sie <i class="fas fa-angle-down"></i> **Erweitern** auswählen, um die Tabelle aufzuklappen.

### Konversions-Funnel {#conversion-funnel}

Dieses Balkendiagramm zeigt die absoluten Zahlen für jedes [Engagement-Event]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) basierend auf dem ausgewählten Kanal. Die Konversionsanzahl wird gemäß der ausgewählten Attributionsmethode definiert.

Standardmäßig werden alle ausgewählten Campaigns und Canvases angezeigt. Um eine Campaign oder ein Canvas abzuwählen, wählen Sie den Namen der Campaign oder des Canvas aus, die/das Sie ausschließen möchten. Für zusätzliche Details zum Engagement-Event können Sie mit dem Mauszeiger über den jeweiligen Balken fahren.

Um die Zeitreihendaten herunterzuladen, wählen Sie eine Download-Option: PNG, JPEG, PDF, SVG oder CSV.

{% alert note %}
Dieses Diagramm zeigt jeweils nur Daten für einen einzelnen Kanal an. Verwenden Sie das **Kanal**-Dropdown im Chart, um einen einzelnen Kanal auszuwählen.
{% endalert %}

![Konversions-Funnel-Balkendiagramm für zwei E-Mail-Campaigns mit ähnlichen Ergebnissen für „E-Mail zugestellt“, „E-Mail geöffnet“, „E-Mail geklickt“ und „Konversionen“.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### Konversionen im Zeitverlauf {#conversions-over-time}

Dieses Zeitreihendiagramm enthält eine Darstellung der Konversionen pro Campaign oder Canvas im Zeitverlauf. Standardmäßig werden alle ausgewählten Campaigns und Canvases angezeigt. Um eine Campaign oder ein Canvas abzuwählen, klicken Sie auf den Namen der Campaign oder des Canvas, die/das Sie ausschließen möchten.

Um die Zeitreihendaten herunterzuladen, wählen Sie <i class="fas fa-bars" title="Chart-Kontextmenü"></i> **Chart-Kontextmenü** und dann Ihre Download-Option. Verfügbare Optionen sind PNG, JPEG, PDF, SVG oder CSV.

![Zeitreihendiagramm „Konversionen im Zeitverlauf“ für zwei E-Mail-Campaigns, das Konversionen pro Tag zeigt.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### Attributionsmethoden {#attribution-methods}

| Attributionsmethode | Definition | Ratenberechnung | Kanalspezifische Optionen |
| --- | --- | --- | --- |
| Bei Empfang | Gesamtzahl der Konversionen, die nach dem Empfang der Nachricht stattfanden | Berechnet als (Eindeutige Empfangs-Konversionen) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Bei E-Mail-Zustellung</li><li>Bei SMS-Zustellung</li></ul>{:/} |
| Bei Versand | Gesamtzahl der Konversionen, die nach dem Versand der Nachricht stattfanden | Berechnet als (Eindeutige Versand-Konversionen) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Bei Push-Versand</li><li>Bei Content-Card-Versand</li><li>Bei SMS-Versand</li></ul>{:/} |
| Bei Öffnung | Gesamtzahl der Konversionen, die nach dem Öffnen der Nachricht stattfanden | Berechnet als (Eindeutige Öffnungs-Konversionen) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Bei E-Mail-Öffnung</li><li>Bei Push-Öffnung</li></ul>{:/} |
| Bei Klick | Gesamtzahl der Konversionen, die nach einem Klick auf die Nachricht stattfanden | Berechnet als (Eindeutige Klick-Konversionen) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Bei E-Mail-Klick</li><li>Bei Content-Card-Klick</li><li>Bei IAM-Klick</li></ul>{:/} |
| Bei Impression | Gesamtzahl der Konversionen, die nach einer Impression stattfanden | Berechnet als (Eindeutige Impressions-Konversionen) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Bei IAM-Impression</li><li>Bei Content-Card-Impression</li></ul>{:/} |
| Bei Last-Touch | Konversionen, die der zuletzt berührten oder geklickten Nachricht innerhalb des Konversionsfensters die gesamte Zuordnung geben. | Berechnet als (Anzahl der Touches) / (Eindeutige Empfänger:innen) | Last-Touch-Attribution wird automatisch ausgewählt, wenn dem Bericht mehrere Kanäle hinzugefügt werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Attributionsmethoden" }

## Wichtige Begriffe {#terms-to-know}

| Begriff | Definition |
| --- | --- |
| Touch | Eine physische Interaktion oder ein Touchpoint mit einer Nachricht.<br><br>Touches können Folgendes umfassen:<br>{::nomarkdown}<ul><li>E-Mail-Klick</li><li>Push-Öffnung</li><li>Content-Card-Klick</li><li>In-App-Nachrichten-Klick</li><li>SMS-Klick</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wichtige Begriffe" }

## Fehlerbehebung {#troubleshooting}

### Warum habe ich niedrige Campaign- oder Canvas-Konversionen? {#why-do-i-have-low-campaign-or-canvas-conversions}

Ihre Konversionen sind möglicherweise nicht so hoch, wie Sie es im Vergleich zu früheren Campaigns oder Ihren Erwartungen erwarten. Konversionen hängen von zwei Schlüsselfaktoren ab: Event-Tracking und Konversionsfristen.

Überprüfen Sie zur Fehlerbehebung Ihr Event-Tracking und Ihre Konversionsfristen.

#### Event-Tracking {#event-tracking}

Wenn eine Campaign einen Sitzungsstart oder ein angepasstes Event auslöst, sollten Sie sicherstellen, dass dieses Event oder diese Sitzung häufig genug stattfindet, um die Nachricht auszulösen. Überprüfen Sie das [Home-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/home) für Sitzungsdaten oder Ihren Bericht zu [angepassten Events]({{site.baseurl}}/user_guide/analytics/reports/configure_reporting).

#### Konversionsfristen {#conversion-deadlines}

Für jedes Konversions-Event, das Sie pro Campaign auswählen, legen Sie die [Frist]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#creating-a-campaign-with-conversion-tracking) fest. Das bedeutet, dass Sie ein Zeitlimit festlegen, innerhalb dessen eine Konversion stattfinden muss, damit sie für die jeweilige Campaign gezählt wird.

Lesen Sie die Informationen zu den [Konversions-Tracking-Regeln]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules), um Ihre Campaign-Metriken zu verstehen. Informationen zu Nutzer:innen-Konversionen in Canvas finden Sie in den [Canvas-FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs#how-are-user-conversions-tracked-in-a-canvas).

### Warum stimmen die Gesamtzahlen der E-Mail-Öffnungen nicht mit Campaign Analytics überein? {#why-dont-email-open-totals-match-campaign-analytics}

**Campaign Analytics** und der Berichts-Builder zählen [maschinelle Öffnungen]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) in *Eindeutige Öffnungen*. Weitere Informationen finden Sie unter [Enthält die Metrik *Eindeutige Öffnungen* auch *Maschinelle Öffnungen*?]({{site.baseurl}}/user_guide/channels/email/faq#does-the-unique-opens-metric-include-machine-opens) in den E-Mail-FAQ.

Im **Conversion-Dashboard** zählt die Attribution **Bei E-Mail-Öffnung** nur menschliche Öffnungen. [Maschinelle Öffnungen]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) sind nicht in der Öffnungszahl enthalten, die für diese Attributionsmethode verwendet wird.

Aufgrund dieses Unterschieds können die Gesamtzahlen der Öffnungen in Campaign Analytics höher sein als die Öffnungszahlen, die in der Conversion-Dashboard-Attribution für dieselben Campaigns verwendet werden. Vergleichen Sie Metriken innerhalb derselben Oberfläche oder verwenden Sie *Sonstige Öffnungen* in Campaign Analytics, wenn Sie menschliches Engagement ohne maschinelle Öffnungen betrachten möchten.