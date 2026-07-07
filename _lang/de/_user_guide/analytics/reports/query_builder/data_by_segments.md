---
nav_title: Metriken nach Segmenten
article_title: Metriken nach Segmenten
page_order: 3
page_type: reference
description: "Diese Seite beschreibt, wie Sie Berichtsvorlagen im Abfrage-Builder verwenden können, um Performance-Metriken für Campaigns, Canvas, Varianten und Schritte nach Segmenten aufzuschlüsseln."
tool:
  - Segments
  - Reports

---

# Metriken nach Segmenten {#metrics-by-segments}

> Verwenden Sie Berichtsvorlagen im [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder), um Performance-Metriken für Campaigns, Canvas, Varianten und Schritte nach Segmenten aufzuschlüsseln.

[Analytics-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) muss für die Segmente aktiviert sein, für die Sie Metriken abrufen möchten.

Gehen Sie wie folgt vor, um diese Berichte auszuführen:
1. Wählen Sie im **Abfrage-Builder** die Option, einen neuen SQL-Bericht mit einer Vorlage zu erstellen.
2. Wählen Sie **Segment breakdowns** für die Metrik aus, um die Vorlagen zu filtern, bei denen die Metriken Aufschlüsselungen nach Segmenten enthalten. Diese sind:
- E-Mail-Performance-Metriken nach Segment
- E-Mail-Engagement-Metriken für Varianten oder Schritte, nach Segment
- Käufe und Umsatz nach Segment
- Käufe und Umsatz für Varianten oder Schritte, nach Segment
- Push-Performance nach Segment

![Die Seite „Segment breakdown“ enthält einen SQL-Editor, ein Seitenpanel mit Tabs für Variablen, verfügbare Datentabellen, Abfrageverlauf und den KI-Abfrage-Builder sowie einen Ergebnisbereich.]({% image_buster /assets/img_archive/segment_breakdown.png %})

## Berichtsvorlagen {#report-templates}

{% tabs %}
{% tab E-Mail-Engagement-Metriken nach Segment %}

### Metriken für Campaigns oder Canvases anzeigen {#campaign-canvas-email}

Um E-Mail-Performance-Metriken nach Segmenten auf Campaign- oder Canvas-Ebene aufgeschlüsselt anzuzeigen, verwenden Sie den Tab [Variablen](#variables), um die Campaigns oder Canvases und einen Zeitraum für den Datenabruf anzugeben. Wenn keine Campaigns oder Canvases angegeben werden, enthält der Bericht E-Mails aus allen Campaigns und Canvases des angegebenen Zeitraums. Sie können auch alle Campaigns und Canvases mit bestimmten Tags anzeigen lassen.

Die folgenden E-Mail-Metriken sind in diesem Bericht verfügbar:
- Sendungen
- Zustellungen
- Beschwerden
- Eindeutige Öffnungen
- Eindeutige maschinelle Öffnungen
- Eindeutige nicht-maschinelle Öffnungen
- Eindeutige Klicks
- Abmeldungen
- Bounces
- Soft Bounces
- Zurückgestellt

#### Ergebnisse {#results}

Ihre Ergebnisse zeigen E-Mail-Engagement-Metriken nach Segment für die von Ihnen ausgewählten Campaigns oder Canvases. Wenn Sie keine bestimmten Campaigns oder Canvases ausgewählt haben, zeigt Ihr Bericht die E-Mail-Metriken für jedes Segment über alle E-Mail-Campaigns und Canvases innerhalb des Berichtszeitraums an.

- **Zeilen:** Segmente
- **Spalten:** E-Mail-Engagement-Metriken

### Metriken für Varianten oder Schritte anzeigen {#viewing-metrics-for-variants-or-steps}

Um die E-Mail-Performance nach Segmenten auf Ebene der Kampagnenvariante, Canvas-Variante oder des Canvas-Schritts aufgeschlüsselt anzuzeigen, wählen Sie zunächst einen Bericht auf Varianten- oder Schrittebene aus (dies sind Berichte, die „für Varianten oder Schritte“ im Titel enthalten), und verwenden Sie dann den Tab **Variablen**, um Folgendes anzugeben:

- Bestimmte Campaign oder Canvas (erforderlich bei Verwendung eines Berichts auf Varianten- oder Schrittebene)
- Varianten (erforderlich bei Verwendung eines Berichts auf Varianten- oder Schrittebene)
- Canvas-Schritt (optional)

Die Metriken sind dieselben wie die für die Vorlage auf [Campaign- oder Canvas-Ebene](#campaign-canvas-email). Wenn Sie mehrere Varianten auswählen, werden Ihre Ergebnisse nach Variante gruppiert.

#### Ergebnisse

Ihre Ergebnisse zeigen E-Mail-Engagement-Metriken nach Segment für Ihre ausgewählten Varianten oder Schritte.

- **Zeilen:** Segmente
- **Spalten:** E-Mail-Engagement-Metriken

{% endtab %}

{% tab Käufe und Umsatz nach Segment %}
### Metriken für Campaigns oder Canvases anzeigen {#viewing-metrics-for-campaigns-or-canvases}

Um Kauf- und Umsatzmetriken nach Segmenten für eine bestimmte Campaign oder ein bestimmtes Canvas aufgeschlüsselt anzuzeigen, verwenden Sie den Tab [Variablen](#variables), um Folgendes anzugeben:

- Conversion-Fenster (die Anzahl der Tage nach E-Mail-Empfang oder Klick, in denen Braze Käufe oder Umsatz zuordnen soll)
- Bestimmtes Produkt (optional)

Verwenden Sie zusätzlich den Tab **Variablen**, um anzugeben, ob der Bericht für eine oder mehrere Campaigns oder Canvases oder für ein oder mehrere Tags ausgeführt werden soll. Wenn keine Campaigns, Canvases oder Tags ausgewählt werden, wird der Bericht für alle E-Mails aus Campaigns oder Canvases im gewählten Zeitraum ausgeführt.

Derzeit bezieht dieser Bericht Metriken nur aus dem E-Mail-Kanal. Umsatz- oder Kaufdaten aus anderen Kanälen als E-Mail werden im Bericht nicht berücksichtigt.

Die folgenden Metriken sind für E-Mails verfügbar:

- Eindeutige Käufe nach Empfang
- Umsatz nach Empfang
- Eindeutige Käufe nach Klick
- Umsatz nach Klick
- Eindeutige Empfänger:innen
- Eindeutige E-Mail-Klicks

Alle Ratenmetriken verwenden eindeutige E-Mail-Empfänger:innen als Nenner.

#### Definitionen {#definitions}

- „Nach Empfang“ bezieht sich auf Kauf-Events oder Umsatz, die innerhalb Ihres angegebenen Conversion-Fensters nach dem Empfang der angegebenen Campaigns oder Canvases durch die Nutzer:innen aufgetreten sind.
- „Nach Klick“ bezieht sich auf Kauf-Events oder Umsatz, die nach den Kauf-Events innerhalb Ihres angegebenen Conversion-Fensters aufgetreten sind, nachdem die Nutzer:innen die angegebenen Campaigns oder Canvases angeklickt haben.

Nehmen wir beispielsweise an, ein Segment enthält 10 Nutzer:innen und fünf davon haben nach dem Empfang Ihrer E-Mail einen Kauf getätigt. Wenn eine dieser fünf Personen nach dem Klick auf Ihre E-Mail einen Kauf getätigt hat, beträgt Ihre „Rate der eindeutigen Käufe nach Empfang“ 50 % und Ihre „Rate der eindeutigen Käufe nach Klick“ 10 %.

![Der Bericht zeigt E-Mail-Metriken einschließlich eindeutiger Käufe nach Empfang, Umsatz nach Empfang, eindeutiger Käufe nach Klick, Umsatz nach Klick, eindeutiger Empfänger:innen und eindeutiger E-Mail-Klicks.]({% image_buster /assets/img_archive/segment_breakdown_results.png %})

#### Ergebnisse

Ihre Ergebnisse zeigen Kaufmetriken nach Segment für Ihre ausgewählten Campaigns oder Canvases. Wenn Sie keine bestimmten Campaigns oder Canvases ausgewählt haben, zeigt Ihr Bericht die Kaufmetriken für jedes Segment über alle E-Mail-Campaigns oder Canvases innerhalb des Berichtszeitraums an.

- **Zeilen:** Segmente
- **Spalten:** Kaufmetriken


### Metriken für Varianten oder Schritte anzeigen

Um Kauf- und Umsatzmetriken nach Segmenten für eine bestimmte Kampagnenvariante, Canvas-Variante oder einen Canvas-Schritt aufgeschlüsselt anzuzeigen, verwenden Sie den Tab [Variablen](#variables), um Folgendes anzugeben:

- Bestimmte Campaign oder Canvas
- Varianten
- Canvas-Schritt (optional)
- Zeitraum
- Bestimmtes Produkt (optional)

#### Ergebnisse

Ihre Ergebnisse zeigen Kaufmetriken nach Segment für die von Ihnen ausgewählten Varianten oder Schritte.

- **Zeilen:** Segmente
- **Spalten:** Kaufmetriken

{% endtab %}
{% tab Top- oder Bottom-Messaging für E-Mail-Engagement %}

### Metriken für die besten oder schlechtesten Performer anzeigen {#viewing-metrics-for-the-top-or-bottom-performers}

Dieser Bericht im Tab [Variablen](#variables) zeigt die Campaigns, Canvases oder Canvas-Schritte an, die für eine bestimmte E-Mail-Engagement-Metrik die besten oder schlechtesten Performer waren.

Anwendungsfälle umfassen:
- 10 Campaigns mit den höchsten eindeutigen E-Mail-Öffnungsraten
- 25 Canvases mit den meisten E-Mail-Abmeldungen
- 50 Canvas-Schritte mit den höchsten eindeutigen Klicks

Die folgenden E-Mail-Metriken sind in diesem Bericht verfügbar:
- Sendungen
- Zustellungen
- Beschwerden
- Eindeutige Öffnungen
- Eindeutige maschinelle Öffnungen
- Eindeutige nicht-maschinelle Öffnungen
- Eindeutige Klicks
- Abmeldungen
- Bounces
- Soft Bounces
- Beschwerden

Um diesen Bericht anzuzeigen, müssen Sie die folgenden Variablen im Tab **Variablen** angeben:
- **Metriken:** Wählen Sie eine der Metriken aus, nach der Ihre Ergebnisse gerankt werden sollen
- **Anzahl der Berichte:** Wählen Sie die besten oder schlechtesten Ergebnisse und die Anzahl der Ergebnisse aus, z. B. Top 10 oder Bottom 15
- **Nachrichtentyp:** Geben Sie an, ob Ihre Ergebnisse Campaigns, Canvases oder Canvas-Schritte sind

#### Ergebnisse

Ihre Ergebnisse zeigen die besten (oder schlechtesten) Campaigns, Canvases oder Canvas-Schritte, die Sie ausgewählt haben. Wenn Sie beispielsweise die Top 10 Campaigns nach Klickrate ausgewählt haben, zeigen Ihre Ergebnisse die Top 10 Campaigns sortiert von der höchsten zur niedrigsten Klickrate. Ihre Spalten zeigen alle E-Mail-Engagement-Metriken für jede Zeile (Campaigns, Canvases oder Nachrichtenschritte).

{% endtab %}
{% tab Top- oder Bottom-Messaging für Käufe %}

### Metriken für die besten oder schlechtesten Performer anzeigen

Dieser Bericht im Tab [Variablen](#variables) zeigt die Campaigns, Canvases oder Canvas-Schritte an, die für eine bestimmte Kauf- oder Umsatzmetrik die besten oder schlechtesten Performer waren.

Anwendungsfälle umfassen:
- 20 Campaigns mit den höchsten Kaufraten für ein bestimmtes Produkt
- 25 Canvases mit dem meisten generierten Umsatz
- 10 Canvas-Schritte mit der niedrigsten Produktkaufrate

Die folgenden E-Mail-Metriken sind in diesem Bericht verfügbar:
- Eindeutige Käufe nach Empfang
- Umsatz nach Empfang
- Eindeutige Käufe nach Klick
- Umsatz nach Klick
- Eindeutige Empfänger:innen
- Eindeutige E-Mail-Klicks

Um diesen Bericht anzuzeigen, müssen Sie die folgenden Variablen im Tab **Variablen** angeben:
- **Metriken:** Wählen Sie eine der Metriken aus, nach der Ihre Ergebnisse gerankt werden sollen
- **Anzahl der Berichte:** Wählen Sie die besten oder schlechtesten Ergebnisse und die Anzahl der Ergebnisse aus, z. B. Top 10 oder Bottom 15
- **Nachrichtentyp:** Geben Sie an, ob Ihre Ergebnisse Campaigns, Canvases oder Canvas-Schritte sind
- **Conversion-Fenster:** Die Anzahl der Tage nach E-Mail-Empfang oder Klick, in denen Braze Käufe oder Umsatz zuordnen wird

#### Definitionen

- „Nach Empfang“ bezieht sich auf Kauf-Events oder Umsatz, die innerhalb Ihres angegebenen Conversion-Fensters nach dem Empfang der angegebenen Campaigns oder Canvases durch die Nutzer:innen aufgetreten sind.
- „Nach Klick“ bezieht sich auf Kauf-Events oder Umsatz, die nach den Kauf-Events innerhalb Ihres angegebenen Conversion-Fensters aufgetreten sind, nachdem die Nutzer:innen die angegebenen Campaigns oder Canvases angeklickt haben.

Nehmen wir beispielsweise an, ein Segment enthält 10 Nutzer:innen und fünf davon haben nach dem Empfang Ihrer E-Mail einen Kauf getätigt. Wenn eine dieser fünf Personen nach dem Klick auf Ihre E-Mail einen Kauf getätigt hat, beträgt Ihre Rate der „eindeutigen Käufe nach Empfang“ 50 % und Ihre Rate der „eindeutigen Käufe nach Klick“ 10 %.

#### Ergebnisse

Ihre Ergebnisse zeigen die besten (oder schlechtesten) Campaigns, Canvases oder Canvas-Schritte, die Sie ausgewählt haben. Wenn Sie beispielsweise die Top 10 Campaigns nach „Umsatz nach Klick“ ausgewählt haben, zeigen Ihre Ergebnisse die Top 10 Campaigns sortiert vom höchsten zum niedrigsten „Umsatz nach Klick“. Ihre Spalten zeigen alle Kaufmetriken für jede Zeile (Campaigns, Canvases oder Nachrichtenschritte).

{% endtab %}
{% tab Push-Performance nach Segment %}

### Push-Metriken für Segmente anzeigen {#viewing-push-metrics-for-segments}

Dieser Bericht im Tab [Variablen](#variables) zeigt Push-Metriken nach Segmenten aufgeschlüsselt an.

Geben Sie im Tab **Variablen** die Campaigns oder Canvases an, für die Sie Metriken anzeigen möchten, sowie einen Zeitraum für den Datenabruf. Wenn Sie keine Campaigns oder Canvases auswählen, zeigt der Bericht Push-Nachrichten aus allen Campaigns und Canvases im angegebenen Zeitraum an. Sie können auch alle Campaigns und Canvases mit bestimmten Tags anzeigen lassen.

Die folgenden Push-Metriken sind in diesem Bericht verfügbar:

- Sendungen
- Bounces
- Zustellungen
- Direkte Öffnungen

#### Ergebnisse

Ihr Bericht zeigt die folgenden Ergebnisse an:

- **Zeilen:** Segmente
- **Spalten:** Push-Metriken
{% endtab %}
{% endtabs %}