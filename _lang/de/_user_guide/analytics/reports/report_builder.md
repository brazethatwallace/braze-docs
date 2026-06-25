---
nav_title: Berichts-Builder
article_title: Berichts-Builder
alias: /report_builder/
page_type: reference
description: "Dieser Referenzartikel beschreibt das Feature Berichts-Builder."
tool:
    - Reports
page_order: 3
---

# Berichts-Builder {#report-builder}

> Diese Seite beschreibt, wie Sie den Berichts-Builder verwenden, um mit Braze-Daten granulare Berichte zu erstellen und anzuzeigen, und wie Sie Berichte zu Dashboards hinzufügen.

Das folgende Video bietet einen Überblick darüber, wie Sie Berichte im Berichts-Builder erstellen und anpassen.

{% multi_lang_include video.html id="oi66kwwldv" source="wistia" %}

## Ein Berichts-Template verwenden {#using-a-report-template}

1. Gehen Sie zu **Analytics** > **Berichts-Builder (Neu)**.
2. Wählen Sie den Pfeil **Weitere Optionen** neben dem Button **Neuen Bericht erstellen** und dann **Berichts-Template verwenden**.<br><br>![Dropdown des Buttons „Neuen Bericht erstellen“ mit Optionen zum Erstellen eines angepassten Berichts oder zur Verwendung eines Templates.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Wählen Sie eines der Berichts-Templates aus der Braze-Template-Bibliothek.
    - Verwenden Sie die Dropdowns **Zeilenelemente** und **Tags**, um relevante Berichte für Ihre Anwendungsfälle zu finden.<br><br>![Fenster „Braze-Berichts-Templates“ mit einer Liste von Braze-Templates zur Auswahl.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. Folgen Sie Schritt 3 und den weiteren Schritten unter [Einen Bericht erstellen](#creating-a-report), um den Bericht weiter an Ihren Anwendungsfall anzupassen.

## Einen Bericht erstellen {#creating-a-report}

1. Gehen Sie zu **Analytics** > **Berichts-Builder (Neu)**.
2. Wählen Sie **Neuen Bericht erstellen**.
3. Wählen Sie im Dropdown **Zeilen**, worüber Sie berichten möchten:
    - Campaigns
    - Canvases
    - Campaigns und Canvases
    - Kanäle
    - Tags

    Beachten Sie, dass Ihre Auswahl bei **Zeilen** beeinflusst, [welche Metriken Sie anzeigen können](#metrics-availability). Beispielsweise können Sie Multivarianten-Metriken nur anzeigen, wenn Sie über **Canvases** oder **Campaigns** mit einem **Varianten**-Drilldown berichten. Sie können diese Metriken nicht anzeigen, wenn Sie über **Campaigns und Canvases** berichten, selbst wenn diese Campaigns und Canvases Multivarianten-Tests enthalten.

![Der Abschnitt „Zeilen und Spalten“ mit Feldern zur Auswahl der Zeilen und Gruppierungen für Ihren Bericht.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4. (Optional) Wählen Sie **Drilldown hinzufügen**, um Ihre Daten in granularere Ansichten aufzuschlüsseln:
    - Kanäle
    - Datum
        - Verwenden Sie dies, um Ihre Daten in kleinere Zeiträume aufzuteilen. Wenn Sie beispielsweise wissen möchten, wie Ihre Campaigns pro Tag abgeschnitten haben, wählen Sie die folgende Konfiguration:
            - **Zeilen**: Campaigns
            - **Gruppierung:** Datum
            - **Intervall:** Tage
    - Varianten
    - Campaigns und Canvases

{% alert tip %}
Probieren Sie verschiedene Konfigurationen der Drilldown-Optionen aus, um die [vielen Möglichkeiten zur Aufschlüsselung Ihrer Daten](#metrics-availability) zu erkunden.
{% endalert %}

{: start="5"}
5. Wählen Sie im Abschnitt **Spalten** die Option **Metriken anpassen**.

![Der Abschnitt „Metriken anpassen“ mit Optionen zur Auswahl mehrerer Metriken.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6. Durchsuchen Sie Metriken nach Kategorie und aktivieren Sie das entsprechende Kontrollkästchen, um eine Metrik zu Ihrem Bericht hinzuzufügen.
    - Ordnen Sie die Metriken und Spalten neu an, indem Sie das gepunktete Symbol nach oben oder unten ziehen.
7. Konfigurieren Sie unter **Berichtsinhalt** den Datumsbereich, für den Sie Daten in Ihren Bericht aufnehmen möchten.
8. Wählen Sie dann, abhängig von Ihrer Auswahl in Schritt 3, ob Sie Campaigns, Canvases oder beides manuell oder automatisch zu Ihrem Bericht hinzufügen möchten.
    - **Manuell hinzufügen:** Wählen Sie jede Campaign oder jeden Canvas, die/der in den Bericht aufgenommen werden soll, indem Sie die Filter für **Zuletzt gesendet**-Daten und Tags oder Kanäle verwenden oder nach dem Campaign- oder Canvas-Namen suchen.<br><br>![Der Abschnitt „Campaigns und Canvases manuell hinzufügen“ mit einer Liste von Campaigns zur Auswahl.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **Automatisch hinzufügen:** Legen Sie Regeln fest, welche Campaigns oder Canvases in den Bericht aufgenommen werden sollen. Sie müssen nur ein Feld auf dieser Seite auswählen.
        - Beachten Sie, dass zusätzliche Campaigns oder Canvases, die die von Ihnen festgelegten Bedingungen erfüllen, automatisch zu zukünftigen Ausführungen Ihres Berichts hinzugefügt werden.<br><br>![Der Abschnitt „Campaigns und Canvases automatisch hinzufügen“ mit Feldern zum Festlegen von Regeln, welche Campaigns und Canvases zum Bericht hinzugefügt werden sollen.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9. Führen Sie den Bericht aus, indem Sie **Speichern und ausführen** wählen.

{% alert note %}
Die Ausführung des Berichts kann je nach Datumsbereich und Anzahl der in der Konfigurationsphase ausgewählten Campaigns oder Canvases einige Minuten dauern.
{% endalert %}

## Verfügbarkeit von Metriken {#metrics-availability}

Ihre Auswahl bei **Zeilen** beeinflusst die Metriken, die Sie auswählen können.

{% alert tip %}
Wenn Sie über Canvas-Varianten oder -Schritte berichten möchten, wählen Sie **Canvases** für die Zeilen und lassen Sie das Feld entweder leer oder wählen Sie **Datum** als Drilldown. Dadurch wird ein Dropdown **Canvas-Ansicht** erstellt, mit dem Sie Metriken nur für den Canvas anzeigen oder Metriken nach Variante, Schritt oder Nachricht gruppieren können.

![Das geöffnete Dropdown „Canvas-Ansicht“.]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Metrik | Beschreibung |
| --- | --- |
| Conversion-Metriken | Verfügbar für Campaigns, Canvases, Campaigns und Canvases. |
| Eintritte | Verfügbar für Campaigns, Canvases, Campaigns und Canvases, Tags. |
| Datum des letzten Versands | Verfügbar für Campaigns, Canvases, Campaigns und Canvases. Wird nur für geplante Campaigns angezeigt – wird nicht für aktionsbasierte oder API-getriggerte Campaigns befüllt. |
| Versendungen | Verfügbar für jeden relevanten Kanal. |
| Gesendete Nachrichten | Verfügbar für Campaigns, Canvases, Campaigns und Canvases, Tags. |
| Betreffzeile | Verfügbar für E-Mail-Campaigns mit **Varianten**-Drilldown, Canvases und Canvases mit **Varianten**-Drilldown. |
| Gesamtumsatz | Verfügbar für Campaigns, Canvases, Campaigns und Canvases, Tags. Nicht verfügbar mit **Kanäle**-Drilldown. |
| Eindeutige Impressionen | Verfügbar für Campaigns, Canvases, Campaigns und Canvases, Tags. |
| Eindeutige Empfänger:innen | Verfügbar für Campaigns, Canvases, Campaigns und Canvases, Tags. Nicht verfügbar mit **Kanäle**-Drilldown. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verfügbarkeit von Metriken" }

### Gelöschte Nachrichtenvarianten {#deleted-message-variants}

Statistiken für gelöschte Nachrichtenvarianten werden nicht angezeigt, wenn Sie Ihren Bericht nach Campaigns oder Canvases aufschlüsseln. Die Gesamtwerte auf Kanalebene enthalten jedoch alle Statistiken, unabhängig davon, ob die Variante gelöscht wurde. Beispielsweise umfassen die *Versendungen* für E-Mail alle E-Mail-Versendungen, aber wenn Sie diese Statistiken nach Campaign aufschlüsseln, können die Zahlen niedriger sein, da Versendungen für gelöschte Nachrichtenvarianten herausgefiltert werden.

Im selben Bericht können die *eindeutigen Empfänger:innen* höher sein als die *eindeutigen Impressionen*, wenn eine Nachrichtenvariante nach dem Versand gelöscht wurde. Die *eindeutigen Empfänger:innen* auf Campaign-Ebene können weiterhin Nutzer:innen enthalten, die die gelöschte Variante erhalten haben, während die *eindeutigen Impressionen* Statistiken gelöschter Varianten in Aggregationen auf Nachrichtenebene auslassen.

## Einen Bericht anzeigen {#viewing-a-report}

Nachdem Sie Ihren Bericht ausgeführt haben, können Sie Ihre Ergebnisse in Tabellenform auf der Berichtsseite anzeigen.

![Eine Tabelle der Berichtsdaten für die Metriken jeder Campaign.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### Ein Berichts-Chart erstellen {#creating-a-report-chart}

Am unteren Rand der Seite können Sie ein Chart Ihrer Daten erstellen, indem Sie einen **Chart-Typ** auswählen und die Chart-Metriken konfigurieren. Standardmäßig wird die erste Metrik angezeigt.

![Ein Chart der Berichtsdaten mit Optionen zur Konfiguration der X-Achse, Y-Achse, des Chart-Typs und mehr.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
Um ein Liniendiagramm zu erstellen, wählen Sie **Datum** als Drilldown-Option bei der Konfiguration des Berichts. Dadurch werden Trends im Zeitverlauf angezeigt.
{% endalert %}

#### Ein Berichts-Chart herunterladen {#downloading-a-report-chart}

Um ein Bild des Berichts-Charts herunterzuladen, wählen Sie das gepunktete Symbol und dann eine Download-Option.

![Ein Menü mit Download-Optionen für verschiedene Dateiformate.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## Einen Bericht teilen {#sharing-a-report}

Sie können einen Dashboard-Link zum Bericht teilen, indem Sie **Teilen** und eine der folgenden Optionen wählen:
- **Link teilen:** Kopieren und teilen Sie den Link.

![Dropdown „Link teilen“ mit einem Link zum Bericht.]({% image_buster /assets/img/report_builder_2/share_this_report.png %}){: style="max-width:70%;"}

- **E-Mail senden oder planen:** Senden Sie sofort oder zu einem festgelegten Zeitpunkt eine E-Mail mit einem Download-Link, der nach einer Stunde abläuft. Sie können Empfänger:innen aus den im Dropdown **E-Mail-Empfänger:innen** aufgeführten Unternehmensnutzer:innen auswählen oder eine beliebige andere E-Mail-Adresse eingeben.

![Fenster „E-Mail planen“ mit Feldern zur Auswahl des Berichtsformats, der Empfänger:innen und des Sendezeitpunkts.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **CSV herunterladen:** Laden Sie eine CSV-Datei des Berichts herunter.

## Einen Bericht zu einem Dashboard hinzufügen {#adding-a-report-to-a-dashboard}

1. Wählen Sie das gepunktete Symbol oben in der Berichtstabelle.
2. Wählen Sie **Zum Dashboard hinzufügen**.
3. Wählen Sie, ob Sie ein neues Dashboard erstellen oder zu einem bestehenden Dashboard hinzufügen möchten.<br><br>![Fenster mit Optionen zur Auswahl, ob Sie den Bericht zu einem neuen oder bestehenden Dashboard hinzufügen möchten.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. Folgen Sie den Schritten im [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/), um mehr über das Erstellen eines Dashboards zu erfahren.

## Fehlerbehebung {#troubleshooting}

### Bericht zeigt keine Versendungen für eine Campaign oder einen Canvas {#report-shows-no-sends-for-a-campaign-or-canvas}

Eine Campaign oder ein Canvas erscheint im Bericht, wenn das Datum **Zuletzt gesendet** in das von Ihnen konfigurierte Fenster **Zuletzt gesendet** fällt. **Versendungen** und andere Metriken werden nur für Aktivitäten innerhalb des Datumsbereichs **Daten anzeigen für** befüllt. Wenn die Nachricht während des Zeitraums **Daten anzeigen für** nicht gesendet wurde, kann die Zeile die Campaign oder den Canvas trotzdem mit null Versendungen auflisten.

Angenommen, **Zuletzt gesendet** ist 1. Januar 2025 – 14. April 2025, sodass eine Campaign eingeschlossen wird, aber **Daten anzeigen für** ist 1. Dezember 2024 – 14. Januar 2025. Wenn diese Campaign im Dezember oder Januar keine Versendungen hatte, erscheint sie trotzdem in der Tabelle ohne Versandmetriken.

### Download-Link ist abgelaufen {#download-link-has-expired}

Download-Links für Berichte laufen nach einer Stunde ab. Wenn Ihr Link abgelaufen ist, erstellen Sie einen neuen Bericht und laden Sie ihn innerhalb einer Stunde herunter. Es gibt keine Möglichkeit, die Ablaufzeit zu verlängern.

Wenn Sie einen [Amazon-S3-Bucket]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/) in **Partnerintegrationen** verbunden haben, können Sie möglicherweise Daten aus älteren Berichten abrufen, indem Sie Ihren S3-Bucket direkt durchsuchen.