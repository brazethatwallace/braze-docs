---
nav_title: Dashboard Builder
article_title: Dashboard Builder
alias: "/dashboard_builder/"
description: "Dieser Referenzartikel beschreibt, wie Sie den Dashboard Builder verwenden, um Dashboards und Visualisierungen mit Berichten zu erstellen, die im Berichts-Builder oder Abfrage-Builder erstellt wurden."
page_type: reference
tool:
    - Reports
page_order: 6
---

# Dashboard Builder {#dashboard-builder}

> Verwenden Sie den Dashboard Builder, um Dashboards und Visualisierungen mit Berichten zu erstellen, die im Berichts-Builder oder Abfrage-Builder erstellt wurden.

Der Dashboard Builder ermöglicht es Ihnen, benutzerdefinierte Analytics-Dashboards von Grund auf oder auf Basis von Braze-bereitgestellten Dashboards zu erstellen und zu visualisieren. Sie können entweder eine No-Code-Datenquelle (Berichts-Builder) oder eine SQL-Datenquelle (Abfrage-Builder) verwenden, um Ihr Dashboard zu betreiben, oder mit einem der vielen von Braze bereitgestellten Dashboards starten.

## Ein benutzerdefiniertes Dashboard erstellen {#creating-a-custom-dashboard}

1. Gehen Sie zu **Analytics** > **Dashboard Builder**.
2. Wählen Sie **Create Dashboard**.
3. Wählen Sie aus, welche Datenquelle Ihre Berichte antreiben soll:
- **Reports**, die im Berichts-Builder erstellt wurden
- **Custom Queries**, die im Abfrage-Builder erstellt wurden<br><br>![Fenster zur Auswahl Ihrer Datenquelle für Ihr Dashboard.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Folgen Sie nun den jeweiligen Schritten für Ihre Datenquelle:

{% tabs %}
{% tab Reports %}

{: start="4"}
4. Wählen Sie **+ Add Tile** und dann einen der Berichte, die Sie im [Berichts-Builder (Neu)]({{site.baseurl}}/user_guide/analytics/reports/report_builder) erstellt haben.

{% alert important %}
Nachdem ein Berichts-Builder-Bericht zu einer Dashboard-Builder-Kachel hinzugefügt wurde, ist die Kachel nicht mit dem ursprünglichen Bericht verbunden. Wenn Sie den ursprünglichen Bericht im Berichts-Builder bearbeiten, müssen Sie die bestehende Dashboard-Kachel löschen und eine neue mit dem aktualisierten Bericht als Datenquelle erstellen.
{% endalert %}

{: start="5"}
5. Wählen Sie das Stiftsymbol, um zu ändern, wie der Titel und der Chart-Typ in der Kachel angezeigt werden.
    - Sie können zwischen verschiedenen Chart-Typen in den Chart-Typ-Steuerelementen umschalten. Die aktuellen Optionen umfassen Balkendiagramme (horizontal oder vertikal) und Liniendiagramme (nur verfügbar, wenn Sie **Date** als Drilldown-Option im Berichts-Builder-Setup ausgewählt haben).<br><br>![Umschalter für verschiedene Chart-Typen.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    - Verwenden Sie das Metriken-Dropdown, um auszuwählen, welche Metriken in Ihrer Visualisierung enthalten sein sollen. Standardmäßig wird die erste Spalte im Bericht als angezeigte Metrik verwendet.
6. Wählen Sie **Save**, nachdem Sie die Visualisierung nach Ihren Wünschen angepasst haben.
7. Fügen Sie einen Namen, eine Beschreibung und einen Tag hinzu, damit Ihr Dashboard später leichter zu finden ist.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4. Wählen Sie **+ Add Tile** und dann eine Abfrage, die Sie im Abfrage-Builder ausgeführt haben.
5. Um zu bearbeiten, wie die Abfrageergebnisse in der Kachel angezeigt werden, wählen Sie das Stiftsymbol, um den Titel und den Chart-Typ zu ändern.
    - Sie können zwischen verschiedenen Chart-Typen in den Chart-Typ-Steuerelementen umschalten. Aktuelle Optionen umfassen Tabellen, Balkendiagramme (horizontal oder vertikal) und Liniendiagramme.<br><br>![Umschalter für verschiedene Chart-Typen.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        - Wenn Sie eine der Chart-Optionen wählen, verwenden Sie das **X-axis**-Dropdown, um eine einzelne Spalte aus Ihren Abfrageergebnissen als X-Achse auszuwählen.
        - Verwenden Sie das **Y-axis**-Dropdown, um auszuwählen, welche Metriken in Ihrer Visualisierung enthalten sein sollen. Standardmäßig werden alle Spalten aus Ihren Abfrageergebnissen angezeigt. Deaktivieren Sie daher die Spalten, die Sie nicht anzeigen möchten.<br><br>![Umschalter für verschiedene Chart-Typen.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        - (Optional) Sie können das **Grouping**-Dropdown verwenden, um Ihre Abfrageergebnisse zu gruppieren. Wenn Sie beispielsweise eine Campaign-ID als Spaltenergebnis haben und alle Zeilen mit diesem Wert zusammenfassen möchten, verwenden Sie das **Grouping**-Dropdown.
        - (Optional) Um die angezeigten Daten zu bearbeiten, wählen Sie die Abfrage aus, die mit der Visualisierung verknüpft ist, und nehmen Sie Ihre Änderungen im [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) vor.
6. Wählen Sie **Save**, nachdem Sie die Visualisierung nach Ihren Wünschen angepasst haben.
7. Fügen Sie einen Namen, eine Beschreibung und einen Tag hinzu, damit Ihr Dashboard später leichter zu finden ist.
{% endtab %}
{% endtabs %}

{: start="8"}
8. Wiederholen Sie die Schritte 4–7 für Ihre jeweilige Methode, bis Sie Ihr gewünschtes Dashboard erstellt haben.
9. Wählen Sie **View Dashboard** > wählen Sie **Run Dashboard**.

Es kann einige Minuten dauern, bis Ihr Dashboard die Berichte fertig generiert hat.

{% alert note %}
Sie können bis zu 10 Kacheln zu einem Dashboard hinzufügen.
{% endalert %}

## Dashboard-Kacheln verwalten {#managing-dashboard-tiles}

### Kacheln löschen {#delete-tiles}

Löschen Sie eine Dashboard-Kachel, indem Sie **Delete Tile** am unteren Rand der Kachel auswählen. **Diese Aktion kann nicht rückgängig gemacht werden.**

### Kacheln duplizieren {#duplicate-tiles}

Erstellen Sie eine Kopie Ihrer Kachel, indem Sie **Duplicate Tile** am unteren Rand der Kachel auswählen.

### Kachelgröße und -position anpassen {#adjust-tile-size-and-position}

Passen Sie die Kachelgröße an, indem Sie den Größenänderungsgriff ziehen, und passen Sie die Kachelposition auf dem Dashboard an, indem Sie den Kachelgriff ziehen.

## Ein Dashboard ausführen {#running-a-dashboard}

1. Gehen Sie zu **Analytics** > **Dashboard Builder**. Die Startseite listet alle vorhandenen Dashboards in Ihrem Workspace auf, wobei von Braze erstellte Dashboards oben stehen. Diese sind mit „(Braze)“ im Titel gekennzeichnet.
2. Wählen Sie das Dashboard aus, das Sie interessiert.
3. Wählen Sie **Run Dashboard**, um das jeweilige Dashboard zu laden.

### Verfügbare Dashboards {#available-dashboards}

Braze stellt vorgefertigte Dashboards für häufige Anwendungsfälle bereit, wie z. B. die Analyse von Umsatz mit Last-Touch-Attribution. Beachten Sie, dass die Möglichkeit, ein Dashboard zu bearbeiten, noch nicht verfügbar ist. Kontaktieren Sie Ihren Customer-Success-Manager, wenn Sie bestimmte Dashboards in Zukunft sehen möchten.

#### Umsatz – Last-Touch-Attribution {#revenue-last-touch-attribution}

Das Dashboard **Umsatz – Last-Touch-Attribution** bietet eine Übersicht über den Umsatz über Campaigns, Canvases und Kanäle hinweg. Alle Umsatzdaten werden der zuletzt berührten Nachricht innerhalb des Attribution-Fensters zugeordnet.

Berührungen umfassen _E-Mail-Klick_ (Link-Klick), _Content-Card-Klick_, _In-App-Nachricht-Klick_ (ohne Schließen-Buttons), _Push-Öffnungen_, _SMS-Kurzlink-Klick_, _WhatsApp-Gelesen_ und _Webhook-Versand_.

| Metrik | Definition |
| --- | --- |
| Gesamter Last-Touch-Umsatz | Eine Summe aller Campaign- und Canvas-Umsatz-Events mit einem Last-Touch-Event innerhalb des ausgewählten Datumsbereichs und Attribution-Fensters. |
| Gesamte Kauf-Conversions | Eine Anzahl aller Campaign- und Canvas-Umsatz-Events mit einem qualifizierenden Last-Touch-Event. |
| Durchschnittliche Tage bis zur Conversion | Die durchschnittliche Zeit zwischen allen Campaign- und Canvas-Kauf-Events mit einem qualifizierenden Last-Touch-Event. |
| Umsatz pro Empfänger:in | Summe des Umsatzes aus qualifizierten Umsatz-Events geteilt durch die Anzahl der eindeutigen Nutzer:innen, die innerhalb des Datumsbereichs eine Nachricht erhalten haben. |
| Eindeutige Käufer:innen | Anzahl der eindeutigen Nutzer:innen mit einem qualifizierten Umsatz-Event. |
| Umsatz nach Land | Summe aller Campaign- und Canvas-Umsatz-Events mit einem Last-Touch-Event, gruppiert nach Land. |
| Umsatz nach Campaign | Summe aller Campaign- und Canvas-Umsatz-Events mit einem qualifizierenden Last-Touch-Event, gruppiert nach Campaign. |
| Umsatz nach Kampagnenvariante | Summe aller Campaign- und Canvas-Umsatz-Events mit einem qualifizierenden Last-Touch-Event, gruppiert nach Kampagnenvariante. |
| Umsatz nach Canvas | Summe aller Campaign- und Canvas-Umsatz-Events mit einem qualifizierenden Last-Touch-Event, gruppiert nach Canvas. |
| Umsatz nach Canvas-Variante | Summe aller Campaign- und Canvas-Umsatz-Events mit einem qualifizierenden Last-Touch-Event, gruppiert nach Canvas-Variante. |
| Käufe pro Produkt | Eine Anzahl aller Käufe, gruppiert nach Produkt. |
| Umsatz nach Kanal | Summe aller Campaign- und Canvas-Umsatz-Events mit einem qualifizierenden Last-Touch-Event, gruppiert nach Kanal. |
| Umsatz-Zeitreihe | Summe aller Campaign- und Canvas-Umsatz-Events mit einem qualifizierenden Last-Touch-Event, gruppiert nach Tag in UTC. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Umsatz – Last-Touch-Attribution" }

#### Geräte und Mobilfunkanbieter {#devices-and-carriers}

| Metrik | Definition |
| --- | --- |
| Geräte-Mobilfunkanbieter | Anzahl der Nutzer:innen im ausgewählten Datumsbereich, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Geräte-Mobilfunkanbieter. |
| Gerätemodell | Anzahl der Nutzer:innen im ausgewählten Datumsbereich, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Gerätemodell. |
| Geräte-Betriebssystem | Anzahl der Nutzer:innen im ausgewählten Datumsbereich, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Geräte-Betriebssystem. |
| Geräte-Bildschirmgröße | Anzahl der Nutzer:innen im ausgewählten Datumsbereich, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Geräte-Bildschirmauflösung (Größe). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Geräte und Mobilfunkanbieter" }

#### Segment-Insights – E-Mail {#segment-insights-email}

| Metrik | Definition |
|---|---|
| Wöchentliche E-Mail-Metriken (Raten) | E-Mail-Engagement-Raten (Zustellungs-, Bounce-, Öffnungs-, Klick-, Abmelderaten), gruppiert nach Segment und als wöchentliche Zeitreihe dargestellt. |
| Wöchentliche E-Mail-Metriken (Anzahl) | E-Mail-Engagement-Zahlen (Versand, Zustellungen, Bounces, Öffnungen, Klicks, Abmeldungen), gruppiert nach Segment und als wöchentliche Zeitreihe dargestellt. |
| Wöchentliche Kauf-Metriken (Raten) | Kauf-Konversionsraten (Umsatz pro Empfänger:in) aus E-Mail-Öffnungen und -Klicks, gruppiert nach Segment und als wöchentliche Zeitreihe dargestellt. |
| Wöchentliche Kauf-Metriken (Anzahl) | Kaufanzahlen und Umsatzsummen aus E-Mail-Öffnungen und -Klicks, gruppiert nach Segment und als wöchentliche Zeitreihe dargestellt. |
| E-Mail-Engagement nach Segment | Übersichtstabelle mit den gesamten E-Mail-Engagement-Metriken (Versand, Zustellungen, Bounces, Öffnungen, Klicks, Abmeldungen und deren Raten), aggregiert nach Segment. |
| Käufe und Umsatz nach Segment | Übersichtstabelle mit den gesamten Kauf-Metriken (Käufe, Umsatz und Umsatz pro Empfänger:in) aus E-Mail-Öffnungen und -Klicks, aggregiert nach Segment. |
| Top-10-Campaigns für Engagement-Metriken | Rangliste der Campaigns mit den höchsten E-Mail-Engagement-Metriken (konfigurierbare Metrik für die Rangfolge). |
| Untere 10 Campaigns für Engagement-Metriken | Rangliste der Campaigns mit den niedrigsten E-Mail-Engagement-Metriken (konfigurierbare Metrik für die Rangfolge). |
| Top-10-Canvases für Engagement-Metriken | Rangliste der Canvases mit den höchsten E-Mail-Engagement-Metriken (konfigurierbare Metrik für die Rangfolge). |
| Untere 10 Canvases für Engagement-Metriken | Rangliste der Canvases mit den niedrigsten E-Mail-Engagement-Metriken (konfigurierbare Metrik für die Rangfolge). |
| Top-10-Campaigns für Kauf-Metriken | Rangliste der Campaigns mit den höchsten Kauf-Conversion-Metriken aus E-Mail-Engagement (konfigurierbare Metrik für die Rangfolge). |
| Untere 10 Campaigns für Kauf-Metriken | Rangliste der Campaigns mit den niedrigsten Kauf-Conversion-Metriken aus E-Mail-Engagement (konfigurierbare Metrik für die Rangfolge). |
| Top-10-Canvases für Kauf-Metriken | Rangliste der Canvases mit den höchsten Kauf-Conversion-Metriken aus E-Mail-Engagement (konfigurierbare Metrik für die Rangfolge). |
| Untere 10 Canvases für Kauf-Metriken | Rangliste der Canvases mit den niedrigsten Kauf-Conversion-Metriken aus E-Mail-Engagement (konfigurierbare Metrik für die Rangfolge). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment-Insights – E-Mail" }

#### Sitzungs-Analytics {#session-analytics}

| Metrik | Definition |
|---|---|
| Anzahl der Sitzungen pro Tag (Zeitreihe) | Anzahl der eindeutigen Sitzungen, gruppiert nach Tag innerhalb des ausgewählten Datumsbereichs, dargestellt als Zeitreihe. |
| Durchschnittliche Anzahl der Sitzungen pro Nutzer:in | Durchschnittliche Anzahl der Sitzungen pro Nutzer:in, berechnet als Gesamtsitzungen geteilt durch eindeutige Nutzer:innen innerhalb des ausgewählten Datumsbereichs. |
| Campaigns konvertieren zu Sitzungen | Anzahl der eindeutigen Sitzungen, die gleichzeitig mit Campaign-Conversions stattfanden, gruppiert nach Campaign-ID und nach Sitzungsanzahl sortiert. |
| Canvases konvertieren zu Sitzungen | Anzahl der eindeutigen Sitzungen, die gleichzeitig mit Canvas-Conversions stattfanden, gruppiert nach Canvas-ID und nach Sitzungsanzahl sortiert. |
| Gesamtanzahl der Sitzungen pro Nutzer:in | Liste der Top 1.000 Nutzer:innen nach ihrer Gesamtsitzungsanzahl innerhalb des ausgewählten Datumsbereichs. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sitzungs-Analytics" }

## Teilen Sie uns Ihr Feedback mit {#share-your-feedback-with-us}

{% multi_lang_include product_feedback_cta.md context="pain_point" channel="ux" feature="Dashboard Builder" %}