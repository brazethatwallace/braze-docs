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

## Ihren Bericht einrichten {#setting-up-your-report}

So richten Sie Ihren Conversions-Dashboard-Bericht ein:

1. Gehen Sie zu **Analytics** > **Conversions**.
2. Wählen Sie einen **Datumsbereich** für Ihren Bericht aus – bis zu einem 90-Tage-Fenster.
3. Wählen Sie die Kampagnen oder Canvases (oder beides) aus, die Sie analysieren möchten.
   - (Optional) Filtern Sie Kampagnen und Canvases, indem Sie einen Tag auswählen.
4. Wählen Sie die **Kanäle** aus, die Sie für Ihre Nachrichten analysieren möchten.
5. Wählen Sie eine **Aufschlüsselung nach**-Ebene, um verschiedene Datendimensionen anzuzeigen, z. B. nach Variante, Canvas-Schritt, Land oder Sprache.
6. (Optional) Wenn Sie Conversions eines Events berechnen möchten, das nicht als Konversions-Event in der Kampagne oder dem Canvas eingerichtet wurde, aktivieren Sie [Angepasste Events verwenden](#using-custom-events).
7. Wählen Sie eine [Attributionsmethode](#attribution-methods), mit der die ausgewählten Nachrichten analysiert werden sollen.

{% alert note %}
Wenn Sie Conversions für mehrere Kanäle analysieren, wird Ihre **Attributionsmethode** standardmäßig auf **Last-Touch-Attribution** gesetzt.
{% endalert %}

{:start="8"}
8. Wählen Sie **Erstellen**, um den Bericht auszuführen.

Nachdem die Seite geladen wurde, wählen Sie ein **Konversions-Event** aus, um den Bericht nach Conversion-Daten zu filtern. Die verfügbaren Optionen umfassen die Events, die in den Canvases und Kampagnen vorkonfiguriert wurden. Wenn Sie beim Einrichten Ihres Berichts (Schritt 6) ein angepasstes Event ausgewählt haben, ist diese Option nicht verfügbar.

### Angepasste Events verwenden {#using-custom-events}

Damit Metriken für angepasste Events im Conversions-Dashboard angezeigt werden, müssen ein Konversions-Event und ein Canvas-Eingangs-Event im auf der Seite angegebenen Datumsbereich vorhanden sein.

Um Conversions eines Events zu berechnen, das nicht als Konversions-Event in der Kampagne oder dem Canvas eingerichtet wurde, wählen Sie ein bestimmtes angepasstes Event als Konversions-Event aus.

1. Aktivieren Sie beim Einrichten Ihres Berichts **Angepasste Events verwenden**.
2. Wählen Sie ein angepasstes Event als Konversions-Event aus.
3. Wählen Sie das Konversionsfenster, innerhalb dessen das Event stattgefunden haben muss, um als Conversion gezählt zu werden.

{% alert note %}
Wenn Sie ein angepasstes Event auswählen, wird das Dropdown-Menü **Konversions-Event** auf der Seite nicht angezeigt, und Sie müssen den Bericht erneut ausführen, um Conversions für verschiedene angepasste Events anzuzeigen.
{% endalert %}

### Hinweise {#considerations}

Damit Nutzer:innen im Bericht gezählt werden, müssen sie innerhalb des ausgewählten Datumsbereichs die folgenden Kriterien erfüllen:
1. In den Canvas oder die Kampagne eintreten.
2. Eine [Attributionsmethode]({{site.baseurl}}/user_guide/analytics/dashboards/conversions/#attribution-methods) protokollieren.
3. Das Konversions-Event ausführen.

Nehmen wir zum Beispiel an, eine Nutzerin bzw. ein Nutzer tut Folgendes:
1. Tritt am 30. September in den Canvas ein.
2. Protokolliert am 1. Oktober eine Attributionsmethode.
3. Führt am 2. Oktober das Konversions-Event aus.

Diese Nutzerin bzw. dieser Nutzer wird **nicht** in einem Bericht mit dem Datumsbereich 1. Oktober bis 7. Oktober erscheinen. Das liegt daran, dass der Eintritt in den Canvas vor dem Berichtszeitraum erfolgte, obwohl das Konversions-Event innerhalb des definierten Datumsbereichs stattfand. Damit die Person im Bericht erscheint, muss der Datumsbereich den 30. September einschließen.

## Ihren Bericht verstehen {#understanding-your-report}

Ihr Bericht ist in drei Abschnitte unterteilt:

- [Conversion-Details](#conversion-details)
- [Konversionstrichter](#conversion-funnel)
- [Conversions im Zeitverlauf](#conversions-over-time)

### Conversion-Details {#conversion-details}

Die Tabelle mit den Conversion-Details zeigt immer eine Spalte für *Empfänger:innen* und eine weitere für *Conversions* (Rate und Gesamtzahl). Die verbleibenden zwei Tabellenspalten hängen von den Optionen ab, die Sie beim Einrichten Ihres Berichts ausgewählt haben.

![Tabelle mit Conversion-Details, die Touches als Attributionsmethode für die Spalten drei und vier zeigt.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

Die folgende Tabelle beschreibt mögliche Metriken.

| Angezeigte Metrik | Beschreibung |
| --- | --- |
| Empfänger:innen | Die Anzahl der Nutzer:innen, die innerhalb des Datumsbereichs des Berichts eine Nachricht über den ausgewählten Kanal erhalten haben |
| Konversionsrate (Empfänger:innen) | Berechnet als: (Anzahl der Conversions) / (Anzahl der Empfänger:innen) |
| Attributionsmethode | Definiert durch die [Attributionsmethode](#attribution-methods), die Sie beim Einrichten des Berichts ausgewählt haben. Bei Last-Touch-Attribution oder wenn mehrere Kanäle ausgewählt sind, wird dies als [Touches](#terms-to-know) angezeigt. |
| Konversionsrate (Attributionsmethode) | Definiert durch die [Attributionsmethode](#attribution-methods), die Sie beim Einrichten des Berichts ausgewählt haben. Wenn mehrere Kanäle ausgewählt sind, wird standardmäßig Last-Touch-Attribution verwendet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversion-Details" }

Wenn Sie beim [Einrichten Ihres Berichts](#setting-up-your-report) (Schritt 5) Details auf Aufschlüsselungsebene für Kampagnen oder Canvases ausgewählt haben, können Sie auf <i class="fas fa-angle-down"></i> **Erweitern** klicken, um die Tabelle zu erweitern.

### Konversionstrichter {#conversion-funnel}

Dieses Balkendiagramm zeigt die absoluten Zahlen für jedes [Engagement-Event]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) basierend auf dem ausgewählten Kanal. Die Conversion-Anzahl wird gemäß der ausgewählten Attributionsmethode definiert.

Standardmäßig werden alle ausgewählten Kampagnen und Canvases angezeigt. Um eine Kampagne oder einen Canvas abzuwählen, klicken Sie auf den Namen der Kampagne oder des Canvas, die/den Sie ausschließen möchten. Für zusätzliche Details zum Engagement-Event können Sie mit der Maus über jeden Balken fahren.

Um die Zeitreihendaten herunterzuladen, wählen Sie eine Download-Option: PNG, JPEG, PDF, SVG oder CSV.

{% alert note %}
Dieses Diagramm zeigt nur Daten für jeweils einen einzelnen Kanal an. Verwenden Sie das Dropdown-Menü **Kanal** im Chart, um einen einzelnen Kanal auszuwählen.
{% endalert %}

![Konversionstrichter-Balkendiagramm für zwei E-Mail-Kampagnen mit ähnlichen Ergebnissen für „E-Mail zugestellt“, „E-Mail geöffnet“, „E-Mail angeklickt“ und „Conversions“.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### Conversions im Zeitverlauf {#conversions-over-time}

Dieses Zeitreihendiagramm enthält eine Darstellung der Conversions pro Kampagne oder Canvas im Zeitverlauf. Standardmäßig werden alle ausgewählten Kampagnen und Canvases angezeigt. Um eine Kampagne oder einen Canvas abzuwählen, klicken Sie auf den Namen der Kampagne oder des Canvas, die/den Sie ausschließen möchten.

Um die Zeitreihendaten herunterzuladen, wählen Sie <i class="fas fa-bars" title="Chart-Kontextmenü"></i> **Chart-Kontextmenü** und dann Ihre Download-Option. Verfügbare Optionen sind PNG, JPEG, PDF, SVG oder CSV.

![Zeitreihendiagramm „Conversions im Zeitverlauf“ für zwei E-Mail-Kampagnen, das Conversions nach Tag zeigt.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### Attributionsmethoden {#attribution-methods}

| Attributionsmethode | Definition | Ratenberechnung | Kanalspezifische Optionen |
| --- | --- | --- | --- |
| Bei Empfang | Gesamtzahl der Conversions, die nach dem Empfang der Nachricht stattfanden | Berechnet als (Eindeutige Empfangs-Conversions) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Bei E-Mail-Zustellung</li><li>Bei SMS-Zustellung</li></ul>{:/} |
| Bei Versand | Gesamtzahl der Conversions, die nach dem Versand der Nachricht stattfanden | Berechnet als (Eindeutige Versand-Conversions) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Bei Push-Versand</li><li>Bei Content-Card-Versand</li><li>Bei SMS-Versand</li></ul>{:/} |
| Bei Öffnung | Gesamtzahl der Conversions, die nach dem Öffnen der Nachricht stattfanden | Berechnet als (Eindeutige Öffnungs-Conversions) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Bei E-Mail-Öffnung</li><li>Bei Push-Öffnung</li></ul>{:/} |
| Bei Klick | Gesamtzahl der Conversions, die nach dem Klick auf die Nachricht stattfanden | Berechnet als (Eindeutige Klick-Conversions) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Bei E-Mail-Klick</li><li>Bei Content-Card-Klick</li><li>Bei IAM-Klick</li></ul>{:/} |
| Bei Impression | Gesamtzahl der Conversions, die nach einer Impression stattfanden | Berechnet als (Eindeutige Impressions-Conversions) / (Eindeutige Empfänger:innen) | {::nomarkdown}<ul><li>Bei IAM-Impression</li><li>Bei Content-Card-Impression</li></ul>{:/} |
| Bei Last-Touch | Conversions, bei denen die gesamte Zuordnung der zuletzt berührten oder angeklickten Nachricht innerhalb des Konversionsfensters zugeschrieben wird. | Berechnet als (Anzahl der Touches) / (Eindeutige Empfänger:innen) | Last-Touch-Attribution wird automatisch ausgewählt, wenn dem Bericht mehrere Kanäle hinzugefügt werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Attributionsmethoden" }

## Wichtige Begriffe {#terms-to-know}

| Begriff | Definition |
| --- | --- |
| Touch | Eine physische Interaktion oder ein Touchpoint mit einer Nachricht.<br><br>Touches können umfassen:<br>{::nomarkdown}<ul><li>E-Mail-Klick</li><li>Push-Öffnung</li><li>Content-Card-Klick</li><li>In-App-Nachrichten-Klick</li><li>SMS-Klick</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wichtige Begriffe" }

## Fehlerbehebung {#troubleshooting}

### Warum habe ich niedrige Kampagnen- oder Canvas-Conversions? {#why-do-i-have-low-campaign-or-canvas-conversions}

Ihre Conversions sind möglicherweise nicht so hoch, wie Sie es im Vergleich zu früheren Kampagnen oder Ihren Erwartungen erwarten. Conversions hängen von zwei Schlüsselfaktoren ab: Event-Tracking und Conversion-Fristen.

Überprüfen Sie zur Fehlerbehebung Ihr Event-Tracking und Ihre Conversion-Fristen.

#### Event-Tracking {#event-tracking}

Wenn eine Kampagne einen Sitzungsstart oder ein angepasstes Event auslöst, sollten Sie sicherstellen, dass dieses Event oder diese Sitzung häufig genug stattfindet, um die Nachricht auszulösen. Überprüfen Sie das [Home-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/home/) für Sitzungsdaten oder Ihren Bericht zu [angepassten Events]({{site.baseurl}}/user_guide/analytics/reports/configure_reporting/).

#### Conversion-Fristen {#conversion-deadlines}

Für jedes Konversions-Event, das Sie pro Kampagne auswählen, legen Sie die [Frist]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/#creating-a-campaign-with-conversion-tracking) fest. Das bedeutet, dass Sie ein Zeitlimit festlegen, innerhalb dessen eine Conversion stattfinden muss, damit sie für die jeweilige Kampagne gezählt wird.

Stellen Sie sicher, dass Sie die Informationen zu den [Conversion-Tracking-Regeln]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/#conversion-tracking-rules) überprüft haben, um Ihre Kampagnenmetriken zu verstehen. Informationen zu Nutzer:innen-Conversions in Canvas finden Sie in den [Canvas-FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#how-are-user-conversions-tracked-in-a-canvas).