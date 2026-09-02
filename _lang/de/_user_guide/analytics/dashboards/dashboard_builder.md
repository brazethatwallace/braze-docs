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

## Erstellen eines benutzerdefinierten Dashboards {#creating-a-custom-dashboard}

1. Gehen Sie zu **Analytics** > **Dashboard Builder**.
2. Wählen Sie **Create Dashboard** aus.
3. Wählen Sie aus, welche Datenquelle Ihre Berichte speisen soll:
- **Reports**, die im Report Builder erstellt wurden
- **Custom Queries**, die im Query Builder erstellt wurden<br><br>![Fenster zur Auswahl der Datenquelle für Ihr Dashboard.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Folgen Sie nun den jeweiligen Schritten für Ihre Datenquelle:

{% tabs %}
{% tab Reports %}

{: start="4"}
4. Wählen Sie **+ Add Tile** und dann einen der Berichte aus, die Sie im [Report Builder (New)]({{site.baseurl}}/user_guide/analytics/reports/report_builder) erstellt haben.

{% alert important %}
Nachdem ein Report-Builder-Bericht zu einer Dashboard-Builder-Kachel hinzugefügt wurde, ist die Kachel nicht mit dem Originalbericht verbunden. Wenn Sie den Originalbericht im Report Builder bearbeiten, müssen Sie die bestehende Dashboard-Kachel löschen und eine neue mit dem aktualisierten Bericht als Datenquelle erstellen.
{% endalert %}

{: start="5"}
5. Wählen Sie das Stiftsymbol aus, um zu ändern, wie Titel und Chart-Typ in der Kachel angezeigt werden.
    - Sie können über die Chart-Typ-Steuerelemente zwischen verschiedenen Chart-Typen umschalten. Die aktuellen Optionen umfassen Balkendiagramme (horizontal oder vertikal) und Liniendiagramme (nur verfügbar, wenn Sie **Date** als Drilldown-Option im Report-Builder-Setup ausgewählt haben).<br><br>![Umschalter für verschiedene Chart-Typen.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    - Verwenden Sie das Metriken-Dropdown, um auszuwählen, welche Metriken in Ihre Visualisierung aufgenommen werden sollen. Standardmäßig wird die erste Spalte im Bericht als angezeigte Metrik verwendet.
6. Wählen Sie **Save** aus, nachdem Sie die Visualisierung nach Ihren Wünschen angepasst haben.
7. Fügen Sie einen Namen, eine Beschreibung und einen Tag hinzu, damit Ihr Dashboard später leichter zu finden ist.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4. Wählen Sie **+ Add Tile** und dann eine Abfrage aus, die Sie im Query Builder ausgeführt haben.
5. Um zu bearbeiten, wie die Abfrageergebnisse in der Kachel angezeigt werden, wählen Sie das Stiftsymbol aus, um den Titel und den Chart-Typ zu ändern.
    - Sie können über die Chart-Typ-Steuerelemente zwischen verschiedenen Chart-Typen umschalten. Aktuelle Optionen umfassen Tabellen, Balkendiagramme (horizontal oder vertikal) und Liniendiagramme.<br><br>![Umschalter für verschiedene Chart-Typen.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        - Wenn Sie eine der Chart-Optionen auswählen, verwenden Sie das **X-axis**-Dropdown, um eine einzelne Spalte aus Ihren Abfrageergebnissen als x-Achse auszuwählen.
        - Verwenden Sie das **Y-axis**-Dropdown, um auszuwählen, welche Metriken in Ihre Visualisierung aufgenommen werden sollen. Standardmäßig werden alle Spalten aus Ihren Abfrageergebnissen angezeigt. Deaktivieren Sie daher die Spalten, die Sie nicht anzeigen möchten.<br><br>![Umschalter für verschiedene Chart-Typen.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        - (Optional) Sie können das **Grouping**-Dropdown verwenden, um Ihre Abfrageergebnisse zu gruppieren. Wenn Sie beispielsweise die Campaign-ID als Spaltenergebnis haben und alle Zeilen mit diesem Wert zusammenfassen möchten, verwenden Sie das **Grouping**-Dropdown.
        - (Optional) Um die angezeigten Daten zu bearbeiten, wählen Sie die Abfrage aus, die mit der Visualisierung verknüpft ist, und nehmen Sie Ihre Änderungen im [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) vor.
6. Wählen Sie **Save** aus, nachdem Sie die Visualisierung nach Ihren Wünschen angepasst haben.
7. Fügen Sie einen Namen, eine Beschreibung und einen Tag hinzu, damit Ihr Dashboard später leichter zu finden ist.
{% endtab %}
{% endtabs %}

{: start="8"}
8. Wiederholen Sie die Schritte 4–7 für Ihre jeweilige Methode, bis Sie Ihr gewünschtes Dashboard erstellt haben.
9. Wählen Sie **View Dashboard** > **Run Dashboard** aus.

Es kann einige Minuten dauern, bis Ihr Dashboard die Berichte fertig generiert hat.

{% alert note %}
Sie können einem Dashboard bis zu 10 Kacheln hinzufügen.
{% endalert %}

## Dashboard-Kacheln verwalten {#managing-dashboard-tiles}

### Kacheln löschen {#delete-tiles}

Löschen Sie eine Dashboard-Kachel, indem Sie unten in der Kachel **Delete Tile** auswählen. **Diese Aktion kann nicht rückgängig gemacht werden.**

### Kacheln duplizieren {#duplicate-tiles}

Erstellen Sie eine Kopie Ihrer Kachel, indem Sie unten in der Kachel **Duplicate Tile** auswählen.

### Kachelgröße und -position anpassen {#adjust-tile-size-and-position}

Passen Sie die Kachelgröße an, indem Sie den Größenänderungsgriff ziehen, und passen Sie die Position der Kachel auf dem Dashboard an, indem Sie den Kachelgriff ziehen.

## Ein Dashboard ausführen {#running-a-dashboard}

1. Gehen Sie zu **Analytics** > **Dashboard Builder**. Auf der Startseite werden alle bestehenden Dashboards in Ihrem Workspace aufgelistet, wobei von Braze erstellte Dashboards oben stehen. Diese sind mit „(Braze)“ im Titel gekennzeichnet.
2. Wählen Sie das gewünschte Dashboard aus.
3. Wählen Sie **Run Dashboard** aus, um das jeweilige Dashboard zu laden.

### Verfügbare Dashboards {#available-dashboards}

Braze stellt vorgefertigte Dashboards für häufige Anwendungsfälle bereit. Verwenden Sie die folgende Tabelle als zentrale Referenz für die aktuell dokumentierten Dashboards und die jeweiligen Zugriffspfade.

| Dashboard | Zugriffspfad | Dokumentation |
| --- | --- | --- |
| Revenue - Last Touch Attribution | **Analytics** > **Dashboard Builder** | [Revenue - Last Touch Attribution](#revenue---last-touch-attribution) |
| Devices and carriers | **Analytics** > **Dashboard Builder** | [Devices and carriers](#devices-and-carriers) |
| Segment Insights - Email | **Analytics** > **Dashboard Builder** | [Segment Insights - Email](#segment-insights---email) |
| Session Analytics | **Analytics** > **Dashboard Builder** | [Session Analytics](#session-analytics) |
| eCommerce Revenue - Last Touch Attribution | **Analytics** > **Dashboard Builder** | [E-Commerce-Umsatz-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/ecommerce_revenue_dashboard) |
| Messaging Diagnostics | **Analytics** > **Dashboard Builder** | [Messaging-Diagnose-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) |
| Industry Benchmarks | **Analytics** > **Dashboard Builder** | [Industry-Benchmarks-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/industry_benchmarks_dashboard) |
| Email performance | **Analytics** > **Email Performance** | [Kanal-Performance-Dashboards]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#email-performance-dashboard) |
| Kurzmitteilungsdienst or SMS performance | **Analytics** > **Kurzmitteilungsdienst or SMS Performance** | [Kanal-Performance-Dashboards]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#sms-performance-dashboard) |
| Push performance | **Analytics** > **Dashboard Builder** > **Push Channel Dashboard** | [Kanal-Performance-Dashboards]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#push-performance-dashboard) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Verfügbare Dashboards" }

{% alert note %}
Die Möglichkeit, von Braze erstellte Dashboards zu bearbeiten, ist noch nicht verfügbar. Kontaktieren Sie Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in, wenn Sie zusätzliche Dashboards anfordern möchten.
{% endalert %}

#### Revenue - Last Touch Attribution {#revenue---last-touch-attribution}

Das Dashboard **Revenue - Last Touch Attribution** bietet eine Übersicht über den Umsatz aus Campaigns, Canvase und Kanälen. Alle Umsatzdaten werden der zuletzt berührten Nachricht innerhalb des Attributionsfensters zugeordnet.

Berührungen umfassen *E-Mail-Klick* (Linkklick), *Content-Card-Klick*, *In-App-Nachricht-Klick* (ohne Schließen-Buttons), *Push-Öffnungen*, *Kurzmitteilungsdienst or SMS-Kurzlink-Klick*, *WhatsApp gelesen* und *Webhook-Versand*.

| Metrik | Definition |
| --- | --- |
| Gesamter Last-Touch-Umsatz | Summe aller Umsatz-Events aus Campaigns und Canvase mit einem Last-Touch-Ereignis innerhalb des ausgewählten Zeitraums und Attributionsfensters. |
| Kauf-Konversionen gesamt | Anzahl aller Umsatz-Events aus Campaigns und Canvase mit einem qualifizierenden Last-Touch-Ereignis. |
| Durchschnittliche Tage bis zur Konversion | Durchschnittliche Zeitspanne zwischen allen Kauf-Events aus Campaigns und Canvase mit einem qualifizierenden Last-Touch-Ereignis. |
| Umsatz pro Empfänger:in | Summe des Umsatzes aus qualifizierten Umsatz-Events geteilt durch die Anzahl der eindeutigen Nutzer:innen, die im ausgewählten Zeitraum eine Nachricht erhalten haben. |
| Eindeutige Käufer:innen | Anzahl der eindeutigen Nutzer:innen mit einem qualifizierten Umsatz-Event. |
| Umsatz nach Land | Summe aller Umsatz-Events aus Campaigns und Canvase mit einem Last-Touch-Ereignis, gruppiert nach Land. |
| Umsatz nach Campaign | Summe aller Umsatz-Events aus Campaigns und Canvase mit einem qualifizierenden Last-Touch-Ereignis, gruppiert nach Campaign. |
| Umsatz nach Kampagnenvariante | Summe aller Umsatz-Events aus Campaigns und Canvase mit einem qualifizierenden Last-Touch-Ereignis, gruppiert nach Kampagnenvariante. |
| Umsatz nach Canvas | Summe aller Umsatz-Events aus Campaigns und Canvase mit einem qualifizierenden Last-Touch-Ereignis, gruppiert nach Canvas. |
| Umsatz nach Canvas-Variante | Summe aller Umsatz-Events aus Campaigns und Canvase mit einem qualifizierenden Last-Touch-Ereignis, gruppiert nach Canvas-Variante. |
| Käufe pro Produkt | Anzahl aller Käufe, gruppiert nach Produkt. |
| Umsatz nach Kanal | Summe aller Umsatz-Events aus Campaigns und Canvase mit einem qualifizierenden Last-Touch-Ereignis, gruppiert nach Kanal. |
| Umsatz-Zeitreihe | Summe aller Umsatz-Events aus Campaigns und Canvase mit einem qualifizierenden Last-Touch-Ereignis, gruppiert nach Tag in UTC. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Revenue - Last Touch Attribution" }

#### Devices and carriers {#devices-and-carriers}

| Metrik | Definition |
| --- | --- |
| Mobilfunkanbieter | Anzahl der Nutzer:innen im ausgewählten Zeitraum, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Mobilfunkanbieter. |
| Gerätemodell | Anzahl der Nutzer:innen im ausgewählten Zeitraum, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Gerätemodell. |
| Betriebssystem | Anzahl der Nutzer:innen im ausgewählten Zeitraum, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Betriebssystem. |
| Bildschirmgröße | Anzahl der Nutzer:innen im ausgewählten Zeitraum, die eine Push-Benachrichtigung geöffnet haben, gruppiert nach Bildschirmauflösung (Größe). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Geräte und Mobilfunkanbieter" }

#### Segment Insights - Email {#segment-insights---email}

| Metrik | Definition |
|---|---|
| Wöchentliche E-Mail-Metriken (Raten) | E-Mail-Engagement-Raten (Zustellungs-, Bounce-, Öffnungs-, Klick- und Abmelderaten), gruppiert nach Segment und als wöchentliche Zeitreihe dargestellt. |
| Wöchentliche E-Mail-Metriken (Anzahl) | E-Mail-Engagement-Zahlen (gesendet, zugestellt, Bounces, Öffnungen, Klicks, Abmeldungen), gruppiert nach Segment und als wöchentliche Zeitreihe dargestellt. |
| Wöchentliche Kauf-Metriken (Raten) | Kauf-Konversionsraten (Umsatz pro Empfänger:in) aus E-Mail-Öffnungen und -Klicks, gruppiert nach Segment und als wöchentliche Zeitreihe dargestellt. |
| Wöchentliche Kauf-Metriken (Anzahl) | Kaufanzahl und Umsatzgesamtwerte aus E-Mail-Öffnungen und -Klicks, gruppiert nach Segment und als wöchentliche Zeitreihe dargestellt. |
| E-Mail-Engagement nach Segment | Zusammenfassungstabelle mit den gesamten E-Mail-Engagement-Metriken (gesendet, zugestellt, Bounces, Öffnungen, Klicks, Abmeldungen und deren Raten), aggregiert nach Segment. |
| Käufe und Umsatz nach Segment | Zusammenfassungstabelle mit den gesamten Kauf-Metriken (Käufe, Umsatz und Umsatz pro Empfänger:in) aus E-Mail-Öffnungen und -Klicks, aggregiert nach Segment. |
| Top-10-Campaigns nach Engagement-Metriken | Rangfolge der Campaigns mit den höchsten E-Mail-Engagement-Metriken (konfigurierbares Ranking-Kriterium). |
| Untere 10 Campaigns nach Engagement-Metriken | Rangfolge der Campaigns mit den niedrigsten E-Mail-Engagement-Metriken (konfigurierbares Ranking-Kriterium). |
| Top-10-Canvase nach Engagement-Metriken | Rangfolge der Canvase mit den höchsten E-Mail-Engagement-Metriken (konfigurierbares Ranking-Kriterium). |
| Untere 10 Canvase nach Engagement-Metriken | Rangfolge der Canvase mit den niedrigsten E-Mail-Engagement-Metriken (konfigurierbares Ranking-Kriterium). |
| Top-10-Campaigns nach Kauf-Metriken | Rangfolge der Campaigns mit den höchsten Kauf-Konversionsmetriken aus E-Mail-Engagement (konfigurierbares Ranking-Kriterium). |
| Untere 10 Campaigns nach Kauf-Metriken | Rangfolge der Campaigns mit den niedrigsten Kauf-Konversionsmetriken aus E-Mail-Engagement (konfigurierbares Ranking-Kriterium). |
| Top-10-Canvase nach Kauf-Metriken | Rangfolge der Canvase mit den höchsten Kauf-Konversionsmetriken aus E-Mail-Engagement (konfigurierbares Ranking-Kriterium). |
| Untere 10 Canvase nach Kauf-Metriken | Rangfolge der Canvase mit den niedrigsten Kauf-Konversionsmetriken aus E-Mail-Engagement (konfigurierbares Ranking-Kriterium). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment-Insights - E-Mail" }

#### Session Analytics {#session-analytics}

| Metrik | Definition |
|---|---|
| Anzahl der Sitzungen pro Tag (Zeitreihe) | Anzahl der eindeutigen Sitzungen, gruppiert nach Tag innerhalb des ausgewählten Zeitraums, dargestellt als Zeitreihe. |
| Durchschnittliche Sitzungen pro Nutzer:in | Durchschnittliche Anzahl der Sitzungen pro Nutzer:in, berechnet als Gesamtanzahl der Sitzungen geteilt durch eindeutige Nutzer:innen innerhalb des ausgewählten Zeitraums. |
| Campaigns mit Sitzungskonversionen | Anzahl der eindeutigen Sitzungen, die gleichzeitig mit Campaign-Konversionen auftraten, gruppiert nach Campaign-ID und nach Sitzungsanzahl sortiert. |
| Canvase mit Sitzungskonversionen | Anzahl der eindeutigen Sitzungen, die gleichzeitig mit Canvas-Konversionen auftraten, gruppiert nach Canvas-ID und nach Sitzungsanzahl sortiert. |
| Gesamtanzahl der Sitzungen pro Nutzer:in | Liste der Top-1.000-Nutzer:innen nach ihrer gesamten Sitzungsanzahl innerhalb des ausgewählten Zeitraums. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Session Analytics" }

## Teilen Sie Ihr Feedback mit uns {#share-your-feedback-with-us}

{% multi_lang_include product_feedback_cta.md context="pain_point" channel="ux" feature="Dashboard Builder" %}