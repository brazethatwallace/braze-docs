---
nav_title: Eine Formel erstellen
article_title: Eine Formel erstellen
page_order: 3
page_type: reference
description: "Dieser Referenzartikel behandelt das Erstellen und Verwalten von Formeln, mit denen Sie komplexe Beziehungen in Ihren Daten leicht verstehen können."
tool: Reports

---
# Eine Formel erstellen {#create-a-formula}

> Bei der Anzeige von Analytics in Braze können Sie mehrere Datenpunkte kombinieren, um wertvolle Insights zu Ihren Nutzerdaten zu erhalten. Diese werden als Formeln bezeichnet. Verwenden Sie Formeln, um Ihre Zeitreihendaten auf der Grundlage der Gesamtzahl der monatlich aktiven Nutzer:innen (MAU or monatlich aktive:r Nutzer:in) und der täglich aktiven Nutzer:innen (täglich aktive:r Nutzer:in; täglich aktiv) zu normalisieren.

Formeln helfen Ihnen, komplexe Beziehungen in Ihren Daten zu verstehen. Sie können zum Beispiel vergleichen, wie viele angepasste Events von täglich aktiven Nutzer:innen, die sich für ein bestimmtes Segment qualifizieren, im Vergleich zur Allgemeinbevölkerung (oder zu einem anderen Segment) abgeschlossen wurden.

## Anwendungsfälle {#use-cases}

Formeln können, insbesondere in Kombination mit angepassten Events, dabei helfen, das Verhalten von Nutzer:innen innerhalb Ihrer App zu verstehen. Formeln können auch tiefere Insights in die Kaufmuster von Segmenten liefern, selbst wenn Ihr Unternehmen Paid Media in Verbindung mit Braze nutzt, wie z. B. Google Ads oder TV.

Im Folgenden finden Sie einige Beispiele für Verhaltensmuster, die mithilfe von Formeln erkannt werden können:

- **Mitfahr-Apps:** Wenn Sie ein angepasstes Event für den Fall haben, dass Nutzer:innen eine Fahrt stornieren, können Sie eine Funktion für stornierte Fahrten / täglich aktive Nutzer:innen konfigurieren, um herauszufinden, ob bestimmte Nutzer:innen-Segmente dazu neigen, mehr Fahrten zu stornieren als andere.
- **E-Commerce-Apps:** Durch die Konfiguration einer Funktion für Käufe einer bestimmten Produkt-ID / MAU or monatlich aktive:r Nutzer:in können Sie die Beliebtheit eines kürzlich beworbenen Produkts zwischen Segmenten vergleichen, selbst wenn nicht alle Aktionen über Braze getrackt werden konnten.
- **Medien-Apps mit Werbung:** Wenn das Erlebnis der Nutzer:innen durch Werbung zwischen Video- oder Audioclips unterbrochen wird, kann das Erfassen von Abbrüchen während der Werbung als angepasstes Event und die Berechnung des Verhältnisses von Werbeabbrüchen / täglich aktiven Nutzer:innen dabei helfen, die besten Segmente für eine Campaign für werbefreie Premium-Abos zu identifizieren.

## Formeln erstellen {#creating-formulas}

Auf Formeln kann im Dashboard auf den Seiten [Home]({{site.baseurl}}/user_guide/analytics/dashboards/home), [Umsatzbericht]({{site.baseurl}}/user_guide/analytics/reports/revenue_report) und [Bericht zu angepassten Events]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) zugegriffen werden. Öffnen Sie auf **Home** und **Umsatzbericht** das Chart **Performance Over Time**, setzen Sie **Statistics For** auf **KPI or Leistungskennzahl or Leistungskennzahlen Formulas** und wählen Sie mindestens eine Formel aus. Öffnen Sie auf der Seite **Custom Events Report** die **Filter**, wählen Sie eine oder mehrere **KPI or Leistungskennzahl or Leistungskennzahlen formula**-Optionen aus und klicken Sie auf **Apply**.

![Statistiken für KPI or Leistungskennzahl or Leistungskennzahlen-Formeln im Braze-Dashboard anzeigen]({% image_buster /assets/img_archive/kpi_forms.png %})

So erstellen Sie eine neue Formel:

1. Gehen Sie zum entsprechenden Dashboard (**Home**, **Revenue Report** oder **Custom Events Report**).
2. Wählen Sie **Manage KPI or Leistungskennzahl or Leistungskennzahlen Formulas** aus.
3. Geben Sie einen Namen für Ihre Formel ein.
4. Wählen Sie die relevanten Zähler und Nenner aus.
5. Wählen Sie **Save** aus.

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
| täglich aktive:r Nutzer:in; täglich aktiv | MAU or monatlich aktive:r Nutzer:in |
| Sitzungen | täglich aktive:r Nutzer:in; täglich aktiv |
| | Segmentgröße |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Übersicht-Dashboard" }

### Umsatz-Dashboard {#revenue-dashboard}

| Zähler | Nenner |
| --- | --- |
| Käufe (alle) | täglich aktive:r Nutzer:in; täglich aktiv |
| Ausgewählte Käufe (z. B. eine Geschenkkarte oder Produkt-ID) | MAU or monatlich aktive:r Nutzer:in |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Umsatz-Dashboard" }

### Dashboard für angepasste Events {#custom-event-dashboard}

| Zähler | Nenner |
| --- | --- |
| Anzahl angepasster Events | MAU or monatlich aktive:r Nutzer:in |
|  | täglich aktive:r Nutzer:in; täglich aktiv |
|  | Segmentgröße (es können nur Segmente verwendet werden, bei denen [Analytics-Tracking]({{site.baseurl}}/viewing_and_understanding_segment_data) aktiviert ist) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dashboard für angepasste Events" }