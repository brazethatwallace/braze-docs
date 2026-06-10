---
nav_title: Eine Formel erstellen
article_title: Eine Formel erstellen
page_order: 3
page_type: reference
description: "Dieser Referenzartikel behandelt das Erstellen und Verwalten von Formeln, mit denen Sie komplexe Beziehungen in Ihren Daten leicht verstehen können."
tool: Reports

---
# Eine Formel erstellen {#create-a-formula}

> Bei der Anzeige von Analytics in Braze können Sie mehrere Datenpunkte kombinieren, um wertvolle Insights zu Ihren Nutzerdaten zu erhalten. Diese werden als Formeln bezeichnet. Verwenden Sie Formeln, um Ihre Zeitreihendaten auf der Grundlage der Gesamtzahl der monatlich aktiven Nutzer:innen (MAU) und der täglich aktiven Nutzer:innen (DAU) zu normalisieren.

Formeln helfen Ihnen, komplexe Beziehungen in Ihren Daten zu verstehen. Sie können zum Beispiel vergleichen, wie viele angepasste Events von täglich aktiven Nutzer:innen, die sich für ein bestimmtes Segment qualifizieren, im Vergleich zur Allgemeinbevölkerung (oder zu einem anderen Segment) abgeschlossen wurden.

## Anwendungsfälle {#use-cases}

Formeln, insbesondere in Kombination mit angepassten Events, können Ihnen helfen, das Nutzerverhalten innerhalb Ihrer App zu verstehen. Formeln können auch tiefere Insights in das Kaufverhalten von Segmenten geben, selbst wenn Ihr Unternehmen Paid Media in Verbindung mit Braze verwendet, wie z. B. Google Ads oder TV.

Im Folgenden finden Sie einige Beispiele für die Arten von Verhaltensmustern, die mit Formeln erkannt werden können:

- **Mitfahr-Apps:** Wenn Sie ein angepasstes Event für den Fall haben, dass Nutzer:innen eine Fahrt stornieren, können Sie eine Funktion für stornierte Fahrten / DAU konfigurieren, um herauszufinden, ob bestimmte Nutzersegmente dazu neigen, mehr Fahrten zu stornieren als andere.
- **E-Commerce-Apps:** Indem Sie eine Funktion für Käufe einer bestimmten Produkt-ID / MAU konfigurieren, können Sie die Beliebtheit eines kürzlich beworbenen Produkts zwischen Segmenten vergleichen, auch wenn nicht alle Aktionen mit Braze getrackt werden konnten.
- **Medien-Apps mit Anzeigen:** Wenn das Nutzererlebnis durch Werbung zwischen Video- oder Audioclips unterbrochen wird, kann die Aufzeichnung von Mid-Ad-Exits als angepasstes Event und die Berechnung des Verhältnisses von Mid-Ad-Exits / DAU dabei helfen, die besten Segmente für das Targeting einer Campaign für werbefreie Premium-Abos zu finden.

## Formeln erstellen {#creating-formulas}

Auf die Formeln können Sie in den Statistik-Panels auf den Seiten [Home]({{site.baseurl}}/user_guide/analytics/dashboards/home/), [Umsatzbericht]({{site.baseurl}}/user_guide/analytics/reports/revenue_report/) und [Bericht zu angepassten Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) im Dashboard zugreifen. Um dieses Panel anzuzeigen, gehen Sie zum Chart **Performance Over Time**, ändern Sie die Dropdown-Liste **Statistics For** in **KPI Formulas** und wählen Sie dann mindestens eine KPI-Formel aus, um das Chart zu füllen.

![Statistiken für KPI-Formeln im Braze-Dashboard anzeigen]({% image_buster /assets/img_archive/kpi_forms.png %})

So erstellen Sie eine neue Formel:

1. Rufen Sie das entsprechende Dashboard auf (**Home**, **Umsatzbericht** oder **Bericht zu angepassten Events**).
2. Wählen Sie **Manage KPI Formulas**.
3. Geben Sie einen Namen für Ihre Formel ein.
4. Wählen Sie die entsprechenden Zähler und Nenner aus.
5. Wählen Sie **Save**.

## Verfügbare Zähler und Nenner {#available-numerators-and-denominators}

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

### Übersicht-Dashboard {#overview-dashboard}

| Zähler | Nenner |
| --- | --- |
| DAU | MAU |
| Sitzungen | DAU |
| | Segmentgröße |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Overview dashboard" }

### Umsatz-Dashboard {#revenue-dashboard}

| Zähler | Nenner |
| --- | --- |
| Käufe (alle) | DAU |
| Bestimmte Käufe (z. B. eine Geschenkkarte oder eine Produkt-ID) | MAU |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Revenue dashboard" }

### Dashboard für angepasste Events {#custom-event-dashboard}

| Zähler | Nenner |
| --- | --- |
| Anzahl angepasster Events | MAU |
|  | DAU |
|  | Segmentgröße (nur Segmente, für die [Analytics-Tracking]({{site.baseurl}}/viewing_and_understanding_segment_data/) aktiviert ist, können verwendet werden) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom event dashboard" }