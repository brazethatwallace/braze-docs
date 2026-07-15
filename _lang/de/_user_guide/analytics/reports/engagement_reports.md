---
nav_title: Engagement-Berichte
article_title: Engagement-Berichte
page_order: 5
local_redirect:
  report-glossary: '/docs/user_guide/analytics/metrics_glossary'
page_type: tutorial
description: "Dieser Artikel erklärt, wie Sie Engagement-Berichte für Campaigns und Canvases erstellen, anpassen und planen."
tool:
  - Campaigns
  - Canvas
  - Reports
---

# Engagement-Berichte {#engagement-reports}

> Mit Engagement-Berichten können Sie Engagement-Statistiken für bestimmte Nachrichten aus Campaigns und Canvases abrufen und zu einem von Ihnen gewählten Zeitpunkt per E-Mail erhalten.

{% alert note %}
Sie benötigen die Berechtigung „Nutzerdaten exportieren“, um Engagement-Berichte auszuführen.
{% endalert %}

Mit Engagement-Berichten können Sie Campaigns und Canvases manuell auswählen, die in Ihren E-Mail-Bericht aufgenommen werden sollen, oder Regeln festlegen, um relevante Campaigns und Canvases automatisch auszuwählen.

Unabhängig von der Anzahl der ausgewählten Campaigns oder Canvases werden bis zu zwei CSV-Dateien generiert – eine für alle Campaign-Daten und eine für alle Canvas-Daten. Sie können über den in Ihrer Berichts-E-Mail eingebetteten Link auf diese CSV-Dateien zugreifen. Engagement-Berichte werden nicht im Braze-Dashboard gespeichert.

Bestimmte Daten werden auf Campaign- oder Canvas-Ebene aggregiert und nicht auf der Ebene einzelner Kampagnenvarianten oder Canvas-Schritte. Wenn Sie [einen Canvas-Schritt nach dem Start löschen]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#canvas-details), werden die zugehörigen Daten ebenfalls aus den Engagement-Berichten entfernt.

{% alert tip %}
Sie können den Bericht erneut ausführen, um aktualisierte Statistiken zu generieren.
{% endalert %}

## Einen neuen Bericht erstellen {#creating-a-new-report}

### Schritt 1: Bericht erstellen {#step-1-create-a-report}

Gehen Sie in Ihrem Dashboard-Konto zu **Analytics** > **Engagement Reports**. Wählen Sie **+ Create New Report**.

### Schritt 2: Nachrichten hinzufügen {#step-2-add-messages}

Fügen Sie die Campaigns und Canvas-Nachrichten hinzu, die Sie in Ihrem Bericht zusammenstellen möchten. Sie können Ihre Nachrichten auf zwei Arten auswählen:

- Campaigns und Canvases manuell auswählen
- Campaigns und Canvases automatisch anhand bestimmter Regeln auswählen

![Nachrichtenauswahl für Engagement-Berichte]({% image_buster /assets/img_archive/engagement_report_add_messages.png %})

#### Campaigns oder Canvases manuell auswählen {#manually-select-campaigns-or-canvases}

Diese Option gibt Ihnen die Freiheit, beliebige Campaigns oder Canvases für diesen Bericht auszuwählen.

#### Campaigns oder Canvases automatisch auswählen {#automatically-select-campaigns-or-canvases}

Diese Option ermöglicht es Ihnen, automatisch alle Nachrichten einzuschließen, die einen bestimmten [Tag]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) enthalten. Sie können Nachrichten ansprechen, die einen oder alle der aufgelisteten Tags haben. Diese Option ist nützlich, wenn Sie wiederkehrende Berichte einrichten und Ihre Engagement-Nachrichten regelmäßig taggen.

{% alert important %}
Die Tags müssen mit mindestens einer Campaign oder einem Canvas übereinstimmen, damit ein Bericht generiert wird. Wenn Sie **Campaigns und Canvases automatisch anhand bestimmter Regeln auswählen** verwenden und einen Fehler sehen, bestätigen Sie, dass mindestens eine Campaign oder ein Canvas mit Ihren Tags und anderen Filtern übereinstimmt (z. B. wenn Sie alle aufgelisteten Tags voraussetzen, muss jede übereinstimmende Nachricht jeden Tag haben).
{% endalert %}

### Schritt 3: Statistiken hinzufügen {#add-statistics-to-your-reports}

Im Schritt **Add Stats** werden Ihnen Statistiken für die Typen der ausgewählten Campaigns oder Canvases angezeigt. Wenn Sie beispielsweise E-Mail-Nachrichten ausgewählt haben, können Sie nur relevante E-Mail-Statistiken einsehen. Wenn Sie eine Kombination aus E-Mail und Push gewählt haben, können Sie die Statistiken für diese beiden Kanäle einsehen.

![Statistiken zum Engagement-Bericht hinzufügen]({% image_buster /assets/img_archive/engagement_report_add_stats.png %})

Engagement-Berichte aggregieren Daten pro Campaign oder Canvas, nicht auf Workspace-Ebene. Um das gesamte Sende- oder Impressionsvolumen über alle aktiven Campaigns und Canvases hinweg zu überwachen, z. B. kanalübergreifende Sends und Impressionen für einen gesamten Workspace, verwenden Sie den [Berichts-Builder]({{site.baseurl}}/report_builder).

{% alert note %}
*Sends an Carrier* ist veraltet, wird aber für Nutzer:innen, die es bereits verwenden, weiterhin unterstützt.
{% endalert %}

| Kanal | Verfügbare Statistiken |
| ------| --------------|
| E-Mail | Sends, Öffnungen, eindeutige Öffnungen, Klicks, eindeutige Klicks, Click-to-Open, Abmeldungen, Bounces, zugestellt, als Spam gemeldet |
| Push  | Sends, Öffnungen, beeinflusste Öffnungen, Bounces, Body-Klicks |
| Web-Push | Sends, Öffnungen, Bounces, Body-Klicks |
| In-App-Nachricht | Impressionen, Klicks, Klicks auf ersten Button, Klicks auf zweiten Button |
| Webhook  |  Sends, Fehler |
| SMS | Sends, Sends an Carrier, bestätigte Zustellungen, Zustellungsfehler, Ablehnungen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3: Statistiken hinzufügen" }

### Schritt 4: Berichtseinrichtung abschließen {#step-4-complete-report-setup}

Geben Sie Ihrem Bericht einen Namen, wählen Sie das Format Ihres Berichts und legen Sie die Empfänger:innen fest. Standardmäßig werden Engagement-Berichte als ZIP-Datei gesendet, in der die Daten kommagetrennt sind (jedes Datenelement wird durch ein Komma getrennt).

Sie können aus den folgenden Komprimierungs- und Trennzeichenoptionen wählen:

- **Komprimierung:** ZIP, unkomprimiert oder gzip
- **Trennzeichen:** Komma (`,`), Doppelpunkt (`:`), Semikolon (`;`) oder Pipe (`|`)

{% alert note %}
Statistiken werden nur für den im Bericht angegebenen Zeitraum erfasst. Um genaue Öffnungs- und Klickratenstatistiken zu erhalten, wählen Sie einen Zeitraum, der den Zeitpunkt umfasst, an dem die Sends-Ereignisse für Ihre Campaigns und Canvases durchgeführt wurden.
{% endalert %}

#### Zeitraum auswählen {#select-time-frame}

Standardmäßig basiert der angezeigte Datenbereich auf der Zeitzone Ihres Unternehmens und reicht von der frühesten ausgewählten Nachricht bis zum aktuellen Datum. Sie können dies anpassen, indem Sie das Datums-Dropdown auswählen und die benutzerdefinierte Bereichsauswahl verwenden, oder den nächsten Radiobutton auswählen und Ihren Datumsbereich mit den verfügbaren Dropdown-Optionen definieren.

#### Datenanzeige auswählen {#select-data-display}

Standardmäßig werden die Daten in den Engagement-Berichten täglich (ein Tag) angezeigt. Um diese Daten in anderen Intervallen anzuzeigen, wählen Sie eine explizite Anzahl von Tagen oder Wochen, um die Daten für den Bericht zu aggregieren. Anstatt tägliche Metriken zu sehen, können Sie Ihr Engagement also nach Woche, Monat, Quartal oder ähnlich betrachten. Sollte eine zeitbasierte Aggregation nicht ausreichen, können Sie die Daten auch auf Campaign- oder Canvas-Ebene exportieren.

![Datenabdeckung des Engagement-Berichts]({% image_buster /assets/img_archive/engagement_report_datacoverage.png %})

##### Daten nach gesamter Campaign oder Canvas anzeigen {#show-data-by-entire-campaign-or-canvas}

Wenn Sie **Show Data by Entire Campaign or Canvas** auswählen, aggregiert Braze die Metriken in Blöcken von 1.825 Tagen (fünf Jahre) über den Zeitraum des Berichts hinweg.

Wenn der Zeitraum mehr als einen Block umfasst, sehen Sie möglicherweise mehrere Zeilen für dieselbe Campaign oder denselben Canvas mit unterschiedlichen Daten in der Datumsspalte. Einige Zeilen enthalten möglicherweise nur Metriken, die später im Zeitraum erfasst wurden (z. B. Abmeldungen). Daten können auch Jahre vor dem Beginn Ihres Versands im Workspace liegen, da sie die Block-Grenzen im Export widerspiegeln und nicht nur Ihren ersten Versand.

Um die Datumsspalte mit dem tatsächlichen Versandzeitpunkt Ihrer ausgewählten Campaigns und Canvases abzugleichen, setzen Sie das [Startdatum des Berichts unter **Zeitraum auswählen**](#select-time-frame) auf das früheste Datum, das Sie in der Datei haben möchten – in der Regel den Zeitpunkt, an dem diese Nachrichten gesendet wurden – anstatt den Standardbereich zu verwenden, der bis zur ältesten ausgewählten Nachricht zurückreicht.

#### Bericht planen {#schedule-your-report}

Es gibt zwei Optionen beim Planen Ihres Berichts:

- **Sofort senden:** Nachdem der Bericht gestartet wurde, sendet Braze diesen Bericht sofort.
- **Zu einem festgelegten Zeitpunkt senden:** Diese Option gibt Ihnen die Flexibilität zu wählen, wie häufig Sie diesen Bericht erhalten. Sie können wählen, ob dieser Bericht alle festgelegte Anzahl von Tagen, Wochen oder Monaten gesendet wird. Sie können auch festlegen, wann der Versand des Berichts beendet werden soll.

![Berichtsplanung für Engagement-Berichte]({% image_buster /assets/img_archive/engagement_report_reportschedule.png %}){: style="max-width:65%;" }

### Schritt 5: Überprüfen und starten {#step-5-review-and-launch}

Der letzte Schritt bei der Einrichtung Ihres Berichts zeigt eine schreibgeschützte Übersicht Ihrer konfigurierten Optionen. Überprüfen Sie Ihren Bericht, und wenn Sie zufrieden sind, wählen Sie **Launch Report**.

### Schritt 6: E-Mail prüfen {#step-6-check-your-email}

Sie erhalten eine E-Mail mit Links zu Ihren Berichten zum gewählten Zeitpunkt oder Zeitplan. **Diese Links laufen 1 Stunde nach dem Versand des Berichts ab.** Wenn Sie die bereitgestellten Links auswählen, wird automatisch eine ZIP-Datei mit Ihren CSV-Dateien heruntergeladen – eine für alle Campaigns.

Der Bericht enthält alle Statistiken, die im Abschnitt [Statistiken hinzufügen](#add-statistics-to-your-reports) des Einrichtungsprozesses ausgewählt wurden.

## Fehlerbehebung {#troubleshooting}

### Metriken des Engagement-Berichts weichen vom E-Mail-Performance-Dashboard ab {#engagement-report-metrics-differ-from-the-email-performance-dashboard}

Engagement-Berichte und das [E-Mail-Performance-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance) verwenden dieselben E-Mail-Metrikdefinitionen. Beide ordnen Öffnungen und Klicks dem Tag zu, an dem das jeweilige Ereignis **stattgefunden hat**, und beide berechnen *eindeutige Öffnungen* und *eindeutige Klicks* als 7-Tage-Unique-Counts pro Tag, die über den ausgewählten Zeitraum summiert werden. Definitionen finden Sie unter [E-Mail-Metriken]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#email-metrics) und [Wie Metriken berechnet werden]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#how-metrics-are-calculated) auf der Seite zu den Kanal-Performance-Dashboards.

Wenn die Summen für dieselben Campaigns und denselben Zeitraum dennoch abweichen, prüfen Sie Folgendes:

| Prüfpunkt | Warum es wichtig ist |
| --- | --- |
| Zeitraum und Zeitzone | Beide Oberflächen müssen dieselben Kalendertage in derselben Zeitzone abdecken. |
| Campaign- oder Canvas-Auswahl | Das E-Mail-Performance-Dashboard aggregiert E-Mail-Aktivitäten über den gesamten Workspace. Ein Engagement-Bericht enthält nur die von Ihnen ausgewählten Campaigns oder Canvases. |
| Tägliche Zeilen vs. Berichtssummen | Wenn die **Datenanzeige** den Export in tägliche Zeilen aufteilt, summieren Sie diese Zeilen, um sie mit den Dashboard-Summen für denselben Zeitraum zu vergleichen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prüfpunkte, wenn Engagement-Bericht-E-Mail-Metriken vom E-Mail-Performance-Dashboard abweichen" }

Abweichungen treten häufiger auf, wenn Engagement-Bericht-Werte mit **Campaign**- oder **Canvas**-Analytics verglichen werden, anstatt mit dem E-Mail-Performance-Dashboard. Campaign- und Canvas-Seiten können Sendedatum-Metriken (z. B. Sends oder Konversionen, die dem Sendedatum zugeordnet sind) neben Ereignisdatum-Öffnungen und -Klicks anzeigen. Siehe [Engagement-Bericht stimmt nicht mit den Metriken aus dem Canvas oder der Campaign überein](#engagement-report-doesnt-match-metrics-from-the-canvas-or-campaign).

### Engagement-Bericht stimmt nicht mit den Metriken aus dem Canvas oder der Campaign überein {#engagement-report-doesnt-match-metrics-from-the-canvas-or-campaign}

#### Nicht übereinstimmender Zeitraum {#mismatched-time-range}

Stellen Sie sicher, dass die Daten im Engagement-Bericht mit den Daten in der Canvas- oder Campaign-Analyse übereinstimmen (z. B. beide decken den 1.–15. Dezember ab), auch wenn der Canvas nur einmal gesendet wurde. Überprüfen Sie in den Engagement-Bericht-Einstellungen unter **Data Display**, ob Sie den richtigen Canvas oder die richtige Campaign betrachten. Wenn **Data Display** so eingestellt ist, dass Daten alle *X* Tage angezeigt werden, erhalten Sie eine Zeile pro Datum, an dem Metriken für jeden Schritt erfasst wurden.

Wenn die Summen in einer Tabellenkalkulation falsch aussehen, entfernen Sie zusätzliche Filter aus dem Export. Sie können die täglichen Zeilen summieren, um sie mit den Canvas- oder Campaign-Gesamtwerten für denselben Zeitraum abzugleichen.

{% alert note %}
Wenn Sie Zeilen nach gesamter Campaign oder Canvas aggregiert haben möchten anstatt nach täglichen, wöchentlichen oder anderen wiederkehrenden Buckets, setzen Sie **Data Display** auf **Show Data by Entire Campaign or Canvas**. Wenn Zeilenanzahl oder Daten in der CSV falsch aussehen, siehe [Daten nach gesamter Campaign oder Canvas anzeigen](#show-data-by-entire-campaign-or-canvas).
{% endalert %}

#### Doppelte Button-Klicks in HTML-In-App-Nachrichten {#duplicate-button-clicks-in-html-in-app-messages}

Wenn Sie HTML-In-App-Nachrichten verwenden und **Body-Klicks** im Engagement-Bericht hoch erscheinen, protokollieren Sie möglicherweise Klicks doppelt – zum Beispiel indem Sie `brazeBridge.logClick()` für einen generischen Body-Klick und gleichzeitig `brazeBridge.logClick('body click')` (oder eine andere ID) für dieselbe Interaktion aufrufen. Durchsuchen Sie Ihr Markup nach `brazeBridge.logClick(` und vereinheitlichen Sie auf ein Muster pro Steuerelement. Für die empfohlene Verwendung siehe [Button-Tracking]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#button-tracking-improvements).

#### Fehlerhafte Links in per E-Mail versendeten Engagement-Berichten {#broken-links-in-emailed-engagement-reports}

Wenn Links in einer geplanten Engagement-Bericht-E-Mail in Ihrem E-Mail-Client nicht korrekt geöffnet werden, versuchen Sie folgende Schritte:

1. Leiten Sie den Bericht an ein Gmail-Postfach weiter und öffnen Sie die Links in Google Chrome.
2. Überprüfen Sie in den Engagement-Bericht-Einstellungen, ob **Report Schedule** so konfiguriert ist, dass der Versand zum erwarteten Zeitpunkt erfolgt (z. B. sofort nach der Berichtserstellung und nicht nach einem verzögerten Zeitplan).