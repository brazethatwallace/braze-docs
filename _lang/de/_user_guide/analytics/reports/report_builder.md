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

## Verwendung eines Berichts-Templates {#using-a-report-template}

1. Gehen Sie zu **Analytics** > **Berichts-Builder (Neu)**.
2. Wählen Sie den Pfeil **Mehr Optionen** neben dem Button **Neuen Bericht erstellen** und dann **Berichts-Template verwenden** aus.<br><br>![Dropdown des Buttons „Neuen Bericht erstellen“ mit Optionen zum Erstellen eines angepassten Berichts oder zur Verwendung eines Templates.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Wählen Sie eines der Berichts-Templates aus der Braze-Template-Bibliothek aus.
    - Verwenden Sie die Dropdown-Menüs **Zeilenelemente** und **Tags**, um relevante Berichte für Ihre Anwendungsfälle zu finden.<br><br>![Fenster „Braze-Berichts-Templates“ mit einer Liste von Braze-Templates zur Auswahl.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. Folgen Sie Schritt 3 und den weiteren Schritten unter [Einen Bericht erstellen](#creating-a-report), um den Bericht weiter an Ihren Anwendungsfall anzupassen.

## Erstellen eines Berichts {#creating-a-report}

1. Gehen Sie zu **Analytics** > **Berichts-Builder (Neu)**.
2. Wählen Sie **Neuen Bericht erstellen**.
3. Wählen Sie im Dropdown **Zeilen** aus, worüber Sie berichten möchten:
    - Campaigns
    - Canvases
    - Campaigns und Canvases
    - Kanäle
    - Tags

    Beachten Sie, dass Ihre Auswahl unter **Zeilen** beeinflusst, [welche Metriken Sie anzeigen können](#metrics-availability). Zum Beispiel können Sie multivariate Metriken nur dann anzeigen, wenn Sie über **Canvases** oder **Campaigns** mit einer **Varianten**-Aufschlüsselung berichten. Diese Metriken können Sie nicht anzeigen, wenn Sie über **Campaigns und Canvases** berichten, selbst wenn diese Campaigns und Canvases multivariate Tests enthalten.

![Der Abschnitt „Zeilen und Spalten“ mit Feldern zur Auswahl der Zeilen und Gruppierungen für Ihren Bericht.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4. (Optional) Wählen Sie **Aufschlüsselung hinzufügen**, um Ihre Daten in detailliertere Ansichten aufzuteilen:
    - Kanäle
    - Datum
        - Verwenden Sie diese Option, um Ihre Daten in kleinere Zeiträume aufzuteilen. Wenn Sie zum Beispiel wissen möchten, wie Ihre Campaigns pro Tag abgeschnitten haben, wählen Sie die folgende Konfiguration:
            - **Zeilen**: Campaigns
            - **Gruppierung:** Datum
            - **Intervall:** Tage
    - Varianten
    - Campaigns und Canvases

{% alert tip %}
Probieren Sie verschiedene Konfigurationen der Aufschlüsselungsoptionen aus, um die [vielen Möglichkeiten zur Aufschlüsselung Ihrer Daten](#metrics-availability) zu erkunden.
{% endalert %}

{: start="5"}
5. Wählen Sie im Abschnitt **Spalten** die Option **Metriken anpassen**.

![Der Abschnitt „Metriken anpassen“ mit Optionen zur Auswahl mehrerer Metriken.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6. Durchsuchen Sie Metriken nach Kategorie und aktivieren Sie das entsprechende Kontrollkästchen, um eine Metrik zu Ihrem Bericht hinzuzufügen.
    - Wählen Sie unter **Allgemein** die Option **Tags**, um die auf jede Campaign oder jeden Canvas angewendeten Tags in Ihre Berichtszeilen aufzunehmen.
    - Ordnen Sie die Metriken und Spalten neu an, indem Sie das gepunktete Symbol nach oben oder unten ziehen.
7. Konfigurieren Sie unter **Berichtsinhalt** den Zeitraum, für den Sie Daten in Ihren Bericht aufnehmen möchten.
8. Wählen Sie dann, je nach Ihrer Auswahl in Schritt 3, ob Sie Campaigns, Canvases oder beides manuell oder automatisch zu Ihrem Bericht hinzufügen möchten.
    - **Manuell hinzufügen:** Wählen Sie jede Campaign oder jeden Canvas aus, die/der in den Bericht aufgenommen werden soll, indem Sie die Filter für **Zuletzt gesendet**-Daten und Tags oder Kanäle verwenden oder nach dem Campaign- oder Canvas-Namen suchen.<br><br>![Der Abschnitt „Campaigns und Canvases manuell hinzufügen“ mit einer Liste von Campaigns zur Auswahl.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **Automatisch hinzufügen:** Legen Sie Regeln fest, welche Campaigns oder Canvases in den Bericht aufgenommen werden sollen. Sie müssen nur ein Feld auf dieser Seite auswählen.
        - Beachten Sie, dass zusätzliche Campaigns oder Canvases, die die von Ihnen auf diesem Bildschirm festgelegten Bedingungen erfüllen, automatisch zu zukünftigen Ausführungen Ihres Berichts hinzugefügt werden.
        - Banner ist keine Option im Dropdown **Kanal**, sodass Sie keine Kanalregeln verwenden können, um Banner-Campaigns oder -Canvases automatisch hinzuzufügen. Sie können Banner-KPIs dennoch in Ihre Berichtsmetriken aufnehmen.<br><br>![Der Abschnitt „Campaigns und Canvases automatisch hinzufügen“ mit Feldern zum Festlegen von Regeln, welche Campaigns und Canvases dem Bericht hinzugefügt werden sollen.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9. Führen Sie den Bericht aus, indem Sie **Speichern & Ausführen** wählen.

{% alert note %}
Die Ausführung des Berichts kann je nach Zeitraum und Anzahl der in der Konfigurationsphase ausgewählten Campaigns oder Canvases einige Minuten dauern.
{% endalert %}

## Verfügbarkeit der Metriken {#metrics-availability}

Ihre Auswahl für **Zeilen** beeinflusst, welche Metriken Sie auswählen können.

{% alert tip %}
Wenn Sie über Canvas-Varianten oder -Schritte berichten möchten, wählen Sie **Canvases** für die Zeilen und lassen Sie das Feld entweder leer oder wählen Sie **Datum** als Aufschlüsselung. Nach dem Ausführen des Berichts erscheint auf der Ergebnisseite ein **Canvas-Ansicht**-Dropdown, um Metriken nur für den Canvas anzuzeigen oder Metriken nach Variante, Schritt oder Nachricht zu gruppieren.<br><br> Beim Bearbeiten Ihres Berichts zeigt die Vorschautabelle maximal 50 Zeilen an. Führen Sie den Bericht aus, um alle Zeilen auf der Ergebnisseite mit Seitenumbruch (100 Zeilen pro Seite) anzuzeigen, oder exportieren Sie den vollständigen Datensatz als CSV.

![Das geöffnete „Canvas-Ansicht“-Dropdown.]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Metrik | Beschreibung |
| --- | --- |
| Konversionsmetriken | Verfügbar für Campaigns, Canvases, Campaigns und Canvases. |
| Eintritte | Verfügbar für Campaigns, Canvases, Campaigns und Canvases, Tags. |
| Letztes Sendedatum | Verfügbar für Campaigns, Canvases, Campaigns und Canvases. Wird nur für geplante Campaigns angezeigt – wird bei aktionsbasierten oder API-ausgelösten Campaigns nicht befüllt. |
| Tags | Verfügbar für Campaigns, Canvases, Campaigns und Canvases. Listet die Tags auf, die jeder Campaign oder jedem Canvas zugeordnet sind. Wenn eine Nachricht mehrere Tags hat, werden diese als durch Semikolon getrennte Liste angezeigt. |
| Sendungen | Verfügbar für jeden relevanten Kanal. |
| Gesendete Nachrichten | Verfügbar für Campaigns, Canvases, Campaigns und Canvases, Tags. |
| Betreffzeile | Verfügbar für E-Mail-Campaigns mit **Varianten**-Aufschlüsselung, Canvases und Canvases mit **Varianten**-Aufschlüsselung. |
| Gesamtumsatz | Verfügbar für Campaigns, Canvases, Campaigns und Canvases, Tags. Nicht verfügbar mit **Kanäle**-Aufschlüsselung. |
| Eindeutige Impressionen | Verfügbar für Campaigns, Canvases, Campaigns und Canvases, Tags. |
| Eindeutige Empfänger:innen | Verfügbar für Campaigns, Canvases, Campaigns und Canvases, Tags. Nicht verfügbar mit **Kanäle**-Aufschlüsselung. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verfügbarkeit der Metriken" }

### Gelöschte Nachrichtenvarianten {#deleted-message-variants}

Statistiken für gelöschte Nachrichtenvarianten werden nicht angezeigt, wenn Sie Ihren Bericht nach Campaigns oder Canvases aufschlüsseln. Die Gesamtwerte auf Kanalebene umfassen jedoch alle Statistiken, unabhängig davon, ob die Variante gelöscht wurde. Zum Beispiel umfassen die _Sendungen_ für E-Mail alle E-Mail-Sendungen, aber wenn Sie diese Statistiken nach Campaign aufschlüsseln, können die Zahlen niedriger sein, da Sendungen für gelöschte Nachrichtenvarianten herausgefiltert werden.

Im selben Bericht können _Eindeutige Empfänger:innen_ höher sein als _Eindeutige Impressionen_, wenn eine Nachrichtenvariante nach dem Versand gelöscht wurde. _Eindeutige Empfänger:innen_ auf Campaign-Ebene können weiterhin Nutzer:innen enthalten, die die gelöschte Variante erhalten haben, während _Eindeutige Impressionen_ Statistiken von gelöschten Varianten in Aggregationen auf Nachrichtenebene auslassen.

## Anzeigen eines Berichts {#viewing-a-report}

Nachdem Sie Ihren Bericht ausgeführt haben, können Sie Ihre Ergebnisse im Tabellenformat auf der Seite mit den Berichtsergebnissen anzeigen.

![Eine Tabelle mit den Berichtsdaten für die Metriken jeder Campaign.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### Erstellen eines Berichts-Charts {#creating-a-report-chart}

Am unteren Rand der Seite können Sie ein Chart Ihrer Daten erstellen, indem Sie einen **Chart-Typ** auswählen und die Chart-Metriken konfigurieren. Standardmäßig wird die erste Metrik angezeigt.

![Ein Chart der Berichtsdaten mit Optionen zur Konfiguration der x-Achse, y-Achse, des Chart-Typs und mehr.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
Um ein Liniendiagramm zu erstellen, wählen Sie beim Konfigurieren des Berichts **Datum** als Drilldown-Option aus. Dies zeigt Trends im Zeitverlauf an.
{% endalert %}

#### Herunterladen eines Berichts-Charts {#downloading-a-report-chart}

Um ein Bild des Berichts-Charts herunterzuladen, wählen Sie das Punkte-Symbol aus und wählen Sie dann eine Download-Option.

![Ein Menü mit Download-Optionen für verschiedene Dateiformate.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## Einen Bericht teilen {#sharing-a-report}

Sie können einen Dashboard-Link zum Bericht teilen, indem Sie **Teilen** auswählen und eine der folgenden Optionen wählen:
- **Einen Link teilen:** Kopieren und teilen Sie den Link.
- **Eine E-Mail senden oder planen:** Senden Sie sofort oder zu einem festgelegten Zeitpunkt eine E-Mail mit einem Download-Link, der nach einer Stunde abläuft. Sie können Empfänger:innen aus den im Dropdown **E-Mail-Empfänger:innen** aufgeführten Unternehmensnutzer:innen auswählen oder eine beliebige andere E-Mail-Adresse eingeben.

{% alert note %}
Das Dropdown **E-Mail-Empfänger:innen** listet nur Braze-Unternehmensnutzer:innen auf und speichert deren E-Mail-Adressen über Berichtszeitpläne hinweg. Externe E-Mail-Adressen müssen jedes Mal manuell eingegeben werden, wenn Sie einen neuen Berichtszeitplan erstellen. Wenn Sie häufig Berichte an externe Empfänger:innen senden, beispielsweise an einen Partnerkontakt, sollten Sie diese als Unternehmensnutzer:in mit entsprechenden Berechtigungen hinzufügen, damit deren Adresse im Dropdown angezeigt wird.
{% endalert %}

![Fenster „E-Mail planen“ mit Feldern zur Auswahl des Berichtsformats, der Empfänger:innen und des Sendezeitpunkts.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **CSV herunterladen:** Laden Sie eine CSV-Datei des Berichts herunter.

## Einen Bericht zu einem Dashboard hinzufügen {#adding-a-report-to-a-dashboard}

1. Wählen Sie das Punktsymbol oben in der Berichtstabelle aus.
2. Wählen Sie **Zum Dashboard hinzufügen** aus.
3. Wählen Sie aus, ob Sie ein neues Dashboard erstellen oder zu einem bestehenden Dashboard hinzufügen möchten.<br><br>![Fenster mit Optionen zur Auswahl, ob Sie den Bericht zu einem neuen oder bestehenden Dashboard hinzufügen möchten.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. Folgen Sie den Schritten im [Dashboard-Builder]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder), um mehr über das Erstellen eines Dashboards zu erfahren.

## Team-Berechtigungen {#team-permissions}

Berichte im Berichts-Builder unterstützen keine [Team-Zuweisung]({{site.baseurl}}/user_guide/administer/global/user_management/teams) wie Campaigns oder Canvases. Sie können einen gespeicherten Bericht beim Erstellen nicht auf ein bestimmtes Team beschränken.

Nutzer:innen mit der [„Dashboard-Berichte anzeigen“]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)-Berechtigung auf Team-Ebene (statt auf Workspace-Ebene) können den Berichts-Builder weiterhin verwenden, die Sichtbarkeit von Berichten ist jedoch eingeschränkt:

- Diese Nutzer:innen sehen nur Berichte, bei denen jede ausgewählte Campaign und jedes ausgewählte Canvas ihren Teams zugewiesen ist.
- Berichte mit **Kanälen** als Zeilen werden ausgeblendet.
- Berichte, die eine automatische Auswahl zum Hinzufügen von Campaigns oder Canvases verwenden, werden ausgeblendet, da Braze den Team-Zugriff für Nachrichten, die beim Ausführen des Berichts möglicherweise hinzugefügt werden, nicht überprüfen kann.

Der [Berichts-Builder (Legacy)]({{site.baseurl}}/report_builder_legacy) schränkt ein, welche Campaigns und Canvases Sie nach Team zu einem Bericht hinzufügen können, aber gespeicherte Berichte werden nicht auf die gleiche Weise aus der Liste gefiltert wie im Berichts-Builder (Neu). Informationen zur Einrichtung von Berechtigungen finden Sie unter [Nutzerberechtigungen festlegen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) und [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams).

## Fehlerbehebung {#troubleshooting}

### Bericht zeigt keine Sendungen für eine Campaign oder ein Canvas {#report-shows-no-sends-for-a-campaign-or-canvas}

Eine Campaign oder ein Canvas erscheint im Bericht, wenn das Datum unter **Zuletzt gesendet** in das von Ihnen konfigurierte Fenster **Zuletzt gesendet** fällt. **Sendungen** und andere Metriken werden nur für Aktivitäten innerhalb des Datumsbereichs **Daten anzeigen für** befüllt. Wenn die Nachricht während des Zeitraums **Daten anzeigen für** nicht gesendet wurde, kann die Zeile die Campaign oder das Canvas trotzdem mit null Sendungen anzeigen.

Angenommen, **Zuletzt gesendet** ist der Zeitraum 1. Januar 2025 bis 14. April 2025, sodass eine Campaign eingeschlossen wird, aber **Daten anzeigen für** ist der Zeitraum 1. Dezember 2024 bis 14. Januar 2025. Wenn diese Campaign im Dezember oder Januar keine Sendungen hatte, erscheint sie trotzdem in der Tabelle ohne Sendungsmetriken.

### Download-Link ist abgelaufen {#download-link-has-expired}

Download-Links für Berichte laufen nach einer Stunde ab. Wenn Ihr Link abgelaufen ist, erstellen Sie einen neuen Bericht und laden Sie ihn innerhalb der Stunde herunter. Es gibt keine Möglichkeit, die Ablaufzeit zu verlängern.

Wenn Sie einen [Amazon S3-Bucket]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) unter **Partnerintegrationen** verbunden haben, können Sie möglicherweise Daten aus älteren Berichten abrufen, indem Sie direkt in Ihrem S3-Bucket suchen.