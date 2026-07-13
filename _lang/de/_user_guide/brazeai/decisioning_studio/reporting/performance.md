---
nav_title: Performance
article_title: Performance-Bericht
page_order: 1
description: "Erfahren Sie, wie Sie den Performance-Bericht verwenden, um Behandlungsgruppen und Kontrollgruppen in BrazeAI Decisioning Studio zu vergleichen."
---

# Performance-Bericht {#performance-report}

> Der Performance-Bericht zeigt, wie Ihr Decisioning-Agent im Vergleich zu Kontrollgruppen abschneidet. Dieser Leitfaden erklärt, was jeder Abschnitt des Berichts darstellt, wie Metriken berechnet werden und wie Sie die Ergebnisse interpretieren.

## Wie der Bericht aufgebaut ist {#how-the-report-is-built}

Ihr Performance-Bericht wird in Schichten aufgebaut und ist vollständig auf Ihren Anwendungsfall zugeschnitten. In Zusammenarbeit mit Ihrem Team:

1. Braze definiert, was als Aktion zählt (z. B. ein Versand, Klick, Kauf oder eine Konversion).
2. Braze definiert, wie diese Aktion täglich gemessen wird (Volumen, Umsatz, eindeutige Personen und Ähnliches).
3. Braze definiert die Geschäftsmetrik, die Sie sehen möchten (z. B. Konversionsrate oder Umsatz pro Nutzer:in).
4. Zeitregeln und Segmentierung werden angewendet.
5. Der Tab **Performance** zeigt die Ergebnisse an.

Nichts im Dashboard erzeugt neue Daten. Es visualisiert gespeicherte tägliche Ergebnisse basierend auf diesen Definitionen.

## Datumsbereich und Vergleichsgruppen {#date-range-and-comparison-groups}

Oben im Dashboard wählen Sie:

- **Datumsbereich:** Der Zeitraum für den Bericht.
- **Vergleichsgruppen:** Die Gruppen, die verglichen werden (z. B. Decisioning Studio versus Business as Usual).
- **Aggregation:** Die Chart-Aggregationseinstellung (Täglich, 7-Tage-Durchschnitt oder 30-Tage-Durchschnitt).
- **Segments:** Alle angewendeten Segments. Diese werden individuell mit Ihrem AI Expert Services-Team konfiguriert.
- **Timeline-Ereignisse:** Ob konfigurierte Timeline-Ereignisse im Chart eingeblendet werden sollen, um Ihnen zu helfen, Änderungen oder Ereignisse zu verstehen, die die Performance beeinflussen könnten.

![Performance-Bericht mit den Filtern für Vergleichsgruppen, Aggregation, Segments und Timeline-Ereignisse oben sowie der Datumsbereichsauswahl oben rechts.]({% image_buster /assets/img/decisioning_studio/reporting_performance_date_range.png %})

Diese Auswahl bestimmt, welche Tage einbezogen werden, welche Gruppen verglichen werden, wie die Trendlinie geglättet wird und welche Population Sie betrachten.

{% alert important %}
Das Ändern der Aggregationseinstellung (z. B. 7-Tage-Durchschnitt) wirkt sich nur auf die Chart-Anzeige aus. Es ändert keine gespeicherten Daten.
{% endalert %}

Wenn Sie ein aktuelles Datum in der Datumsauswahl nicht auswählen können, ist dieses Datum wahrscheinlich aufgrund konfigurierter Datenverzögerungen deaktiviert. Es gibt zwei Arten von Verzögerungen, die die Datumsverfügbarkeit einschränken können:

- **Datenpipeline-Verzögerungen:** Die Zeit, die benötigt wird, um Daten aus Ihrer CDP in Decisioning Studio aufzunehmen und zu verarbeiten. Dadurch wird sichergestellt, dass Berichte nur vollständige, zuverlässige Daten anzeigen.
- **Empfehlungsaktivierungsverzögerungen:** Die Zeit zwischen dem Zeitpunkt, an dem die Decisioning-Studio-Engine eine Empfehlung vorhersagt, und dem Zeitpunkt, an dem Sie sie in Ihren Campaigns aktivieren. Berichte enthalten keine Tage, an denen Empfehlungen noch nicht aktiviert wurden.

Diese Verzögerungen werden für Ihren Anwendungsfall konfiguriert. Wenn Sie Ihr spezifisches Berichtsfenster verstehen möchten, wenden Sie sich an Ihre:n AI Success Manager:in.

## KPI-Karten {#kpi-cards}

Die KPI-Karten auf der primären Seite des Berichts zeigen die für Ihren Anwendungsfall konfigurierten Leistungskennzahlen, wie z. B.:

- Inkrementeller LTV / Kund:in
- Conversions / Kund:in
- Abmeldungen / Kund:in

Jede Karte stellt die KPI dar, die über den gesamten ausgewählten Datumsbereich berechnet wird. Dies ist ein Gesamtzeitraumwert, kein Tagesdurchschnitt. Wenn Sie beispielsweise „Inkrementeller LTV / Kund:in = 3,192“ sehen, spiegelt das die Performance über das gesamte ausgewählte Fenster wider.

![Performance-Bericht mit den KPI-Zusammenfassungskarten auf der primären Seite, einschließlich Metriken wie „Inkrementeller LTV / Kund:in“, „Conversions / Kund:in“ und „Abmeldungen / Kund:in“.]({% image_buster /assets/img/decisioning_studio/reporting_performance_kpi_cards.png %})

## KPI-Trendchart {#kpi-trend-chart}

Verwenden Sie das Chart, um Trends im Zeitverlauf, Performance-Verschiebungen und Saisonalitäts- oder Timing-Effekte zu verstehen. Verwenden Sie die KPI-Karte, um die Gesamtauswirkung über das gesamte Fenster zu verstehen. Das zentrale Chart zeigt dieselbe KPI wie die obere Karte, aber pro Tag berechnet. Jeder Punkt stellt den KPI-Wert dieses Tages dar. Wenn Sie den 7-Tage-Durchschnitt ausgewählt haben, spiegelt jeder Punkt einen gleitenden Durchschnitt wider, der die tägliche Volatilität glättet.

![Performance-Bericht mit dem zentralen Trendchart „Inkrementeller LTV / Kund:in“ mit Linien für Decisioning Studio und die Business-as-Usual-BAU-Gruppe im Zeitverlauf.]({% image_buster /assets/img/decisioning_studio/reporting_performance_trend_chart.png %})

Das Chart und die KPI-Karte sind darauf ausgelegt, unterschiedliche Dinge zu zeigen. Das Chart zeigt die tägliche Performance („Wie haben Sie an jedem Tag abgeschnitten?“). Die KPI-Karte zeigt die Gesamtzeitraum-Performance („Wie haben Sie über den gesamten Zeitraum abgeschnitten?“). Bei Ratenmetriken beantworten sie unterschiedliche Fragen.

Betrachten Sie das folgende Beispiel mit diesen Konversionsraten:

- Tag 1: 10 Conversions von 100 Kund:innen = 10 %
- Tag 2: 2 Conversions von 10 Kund:innen = 20 %

Das Chart zeigt beides. Die KPI-Karte berechnet über beide Tage zusammen neu (12 Conversions / 110 Kund:innen = 10,9 %), nicht einen Durchschnitt von 10 % und 20 %.

## Uplift-Chart {#uplift-chart}

Das Uplift-Chart zeigt die prozentuale Differenz zwischen Ihren Vergleichsgruppen. Es wird berechnet als: **(Primäre Gruppe - Vergleichsgruppe) / Vergleichsgruppe**. Dies wird dynamisch basierend auf den KPI-Chart-Werten berechnet.

![Performance-Bericht mit dem Uplift-Prozent-Chart auf der rechten Seite, das die prozentuale Differenz zwischen Decisioning Studio und der BAU-Gruppe im Zeitverlauf anzeigt.]({% image_buster /assets/img/decisioning_studio/reporting_performance_uplift.png %})

{% alert important %}
Der Uplift wird nicht gespeichert. Er wird aus den KPI-Ergebnissen berechnet. Wenn sich der Uplift ändert, liegt das daran, dass sich die zugrunde liegende KPI geändert hat.
{% endalert %}

## Aggregierte Tabelle {#aggregate-table}

Die Tabelle am unteren Rand des Berichts zeigt die Rohdaten-Gesamtwerte über den ausgewählten Datumsbereich, wie z. B.:

- Gesamter inkrementeller LTV
- Gesamtzahl der Kund:innen
- Abgeleiteter KPI-Wert

Dieser Abschnitt verdeutlicht die Beziehung zwischen den verschiedenen Ansichten:

- Die KPI-Karte ist eine Berechnung auf Fensterebene.
- Das Chart ist eine tägliche Berechnung.
- Die Tabelle zeigt die zugrunde liegenden Gesamtwerte, die die KPI bestimmen.

![Performance-Bericht mit der aggregierten Tabelle am unteren Rand, mit Spalten für Gruppe, Inkrementeller LTV, Kund:in und Inkrementeller LTV / Kund:in für jede Vergleichsgruppe.]({% image_buster /assets/img/decisioning_studio/reporting_performance_aggregate_table.png %})

## Treiberbaum {#driver-tree}

Der Treiberbaum zerlegt eine KPI in ihre Komponententreiber. Zum Beispiel kann „Inkrementeller LTV / Kund:in“ aufgeteilt werden in:

- Conversions / Kund:in
- Umsatz pro Conversion

![Performance-Bericht in der Treiberbaum-Ansicht, der ein hierarchisches Diagramm zeigt, das KPIs wie „Inkrementeller LTV / Kund:in“ in Komponententreiber wie „Conversions / Kund:in“ und „Klicks / Kund:in“ aufschlüsselt.]({% image_buster /assets/img/decisioning_studio/reporting_performance_driver_tree.png %})

Treiberbäume verwenden dieselben KPI-Definitionen wie der Rest des Dashboards und führen keine neue Berechnungslogik ein. Sie helfen zu erklären, was die Performance antreibt. Wenn sich eine KPI-Definition ändert, werden Charts, Karten, Uplift und Treiberbäume gemeinsam aktualisiert.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie funktionieren Segments? {#how-do-segments-work}

Segments ermöglichen es Ihnen, die Performance nach definierten Gruppen aufzuschlüsseln, z. B. nach Engagement-Level, Kundenmerkmalen, Gerätetyp oder anderen konfigurierten Features.

Die Segmentzugehörigkeit wird individuell für Ihren Anwendungsfall konfiguriert und täglich berechnet. Das bedeutet, dass das vergangene Segment einer Kund:in widerspiegelt, wer sie an diesem Tag war. Wenn sich ihr Verhalten später ändert, bleiben historische Tage unverändert. Dies bewahrt die historische Genauigkeit und verhindert, dass sich Berichte rückwirkend verschieben.

### Unterscheidet sich der Performance-Bericht für Go- und Pro-Agenten? {#does-the-performance-report-for-go-versus-pro-agents-differ}

Die KPIs für Go-Anwendungsfälle werden automatisch festgelegt und standardisiert, da alle Go-Anwendungsfälle dieselbe Zielmetrik haben: eindeutige Klicks.

### Warum kann ich bestimmte aktuelle Daten nicht auswählen? {#why-cant-i-select-certain-recent-dates}

Die Datumsauswahl erlaubt möglicherweise nicht die Auswahl der letzten Tage. Dies ist beabsichtigt. Berichte können die folgenden Einschränkungen anwenden, um zu verhindern, dass unvollständige oder instabile Daten angezeigt werden:

- **Datenpipeline-Verzögerungen:** Konfiguriert, um die Zeit zu berücksichtigen, die für die Aufnahme und Verarbeitung von Daten aus Ihrer CDP benötigt wird. Dadurch wird sichergestellt, dass alle Daten für einen bestimmten Tag vollständig sind, bevor dieser Tag in Berichten erscheint.
- **Empfehlungsaktivierungsverzögerungen:** Konfiguriert, um die Verzögerung zwischen dem Zeitpunkt, an dem Empfehlungen generiert werden, und dem Zeitpunkt, an dem sie in Ihren Campaigns aktiviert werden, zu berücksichtigen. Tage, an denen Empfehlungen noch nicht aktiviert wurden, erscheinen nicht in Berichten.
- **Explizit ausgeschlossene Daten:** Daten, die Sie in den Berichtseinstellungen manuell ausgeschlossen haben.

Wenn Sie Klarheit über Ihr spezifisches Berichtsfenster oder die Datenverfügbarkeitsregeln benötigen, wenden Sie sich an Ihre:n AI Success Manager:in.

### Was ist der Unterschied zwischen „Volumen“- und „Raten“-KPIs? {#whats-the-difference-between-volume-and-rate-kpis}

KPIs fallen typischerweise in zwei Kategorien:

- **Volumenmetriken** (wie Gesamt-Conversions, Gesamtumsatz oder Gesamtklicks) beantworten: „Wie viel ist passiert?“
- **Ratenmetriken** (wie Konversionsrate, Umsatz pro Nutzer:in oder Click-through-Rate) beantworten: „Wie effizient ist es passiert?“

Volumen und Rate erzählen unterschiedliche Geschichten. Eine Campaign kann ein höheres Volumen, aber eine geringere Effizienz erzielen – oder umgekehrt. Wenn Sie Ergebnisse interpretieren, prüfen Sie immer, welche Art von KPI Sie betrachten.

### Was bedeutet „eindeutig“ (oder „distinct“)? {#what-does-unique-or-distinct-mean}

Wenn eine Metrik als „eindeutig“ definiert ist, werden Personen mithilfe eines bestimmten Bezeichners (typischerweise Kund:in) dedupliziert. Jede Person wird einmal pro Tag gezählt.

„Eindeutig pro Tag“ unterscheidet sich von „eindeutig über den gesamten Datumsbereich“. Wenn Sie tägliche eindeutige Zählungen über mehrere Tage summiert sehen, kann dieselbe Person mehr als einmal erscheinen (einmal pro Tag, an dem sie aktiv war). Das ist beabsichtigt.

Wenn Sie verstehen möchten, wie Eindeutigkeit in Ihrem Setup definiert wurde, wenden Sie sich an Ihre:n AI Success Manager:in.

### Warum könnte dieser Bericht von einem anderen System abweichen? {#why-might-this-report-differ-from-another-system}

Wenn Ihr Performance-Bericht nicht mit einem anderen Dashboard übereinstimmt (z. B. einem ESP, Analytics-Tool oder internen BI-Bericht), bedeutet das nicht unbedingt, dass etwas falsch ist. Verschiedene Systeme wenden oft unterschiedliche Definitionen und Regeln an. Häufige Gründe sind:

- **Attributionsregeln:** Einige Metriken wenden Attributionslogik an, was bedeutet, dass nur Aktivitäten gezählt werden, die definierten Kriterien entsprechen. Wenn ein anderes System alle Aktivitäten ohne Attributionslogik zählt, können die Gesamtwerte abweichen.
- **Filterung von Maschinen- und Bot-Engagement:** Bekanntes maschinen- oder bot-gesteuertes Engagement (wie automatisierte Sicherheitsscans oder nicht-menschliche Klicks) wird herausgefiltert, um sicherzustellen, dass die Performance echtes menschliches Verhalten widerspiegelt. Einige Plattformen schließen diese Interaktionen in ihre Gesamtwerte ein.
- **Unterschiedliche Definitionen von „eindeutig“:** In diesem Bericht wird Eindeutigkeit typischerweise pro Tag angewendet. Ein anderes System kann Eindeutigkeit über ein gesamtes Campaign-Fenster berechnen. Das sind unterschiedliche Geschäftsfragen und erzeugen unterschiedliche Zahlen.
- **Datumsbereich und Datenverfügbarkeitsregeln:** Berichte können Aktivierungsverzögerungen, Datenverfügbarkeitsverzögerungen oder ausgeschlossene Daten anwenden. Ein anderes System kann sehr aktuelle oder unvollständige Daten einbeziehen, was vorübergehende Abweichungen verursacht.
- **Volumen- versus Ratenunterschiede:** Ein System kann das Gesamtvolumen anzeigen (z. B. Gesamt-Conversions), während ein anderes eine Rate anzeigt (z. B. Conversions pro Kund:in). Stellen Sie immer sicher, dass Sie denselben Metriktyp vergleichen.

### Warum stimmt die Zahl im Chart nicht mit der Zusammenfassungskarte überein? {#why-doesnt-the-number-in-the-chart-match-the-summary-card}

Das Chart und die Zusammenfassungskarte beantworten unterschiedliche Fragen:

- **Chart:** Zeigt die tägliche Performance. Jeder Punkt spiegelt die KPI wider, die für diesen einzelnen Tag berechnet wurde.
- **Zusammenfassungskarte:** Zeigt die Gesamtzeitraum-Performance. Sie berechnet die KPI über den gesamten ausgewählten Datumsbereich neu.

Verwenden Sie das Chart, um die tägliche Volatilität, Timing-Effekte und Performance-Verschiebungen im Zeitverlauf zu verstehen. Verwenden Sie die Zusammenfassungskarte, um die Gesamtauswirkung über den Zeitraum zu verstehen.

Betrachten Sie dieses Beispiel mit der folgenden Konversionsrate:

- Tag 1: 10 Conversions von 100 Kund:innen = 10 %
- Tag 2: 2 Conversions von 10 Kund:innen = 20 %

Das Chart zeigt 10 % an Tag 1 und 20 % an Tag 2. Die Zusammenfassungskarte berechnet die Performance über beide Tage zusammen: 12 Gesamt-Conversions von 110 Kund:innen = 10,9 %. Es wird kein Durchschnitt aus 10 % und 20 % gebildet.

### Was ist der empfohlene Ansatz für „eindeutige“ Zählungen? {#whats-the-recommended-approach-for-unique-counts}

Wenn Sie eindeutiges Verhalten messen (wie eindeutige Klicker oder Konvertierer), wird Eindeutigkeit pro Tag angewendet. Zum Beispiel:

- Tag 1: Kund:innen, die geklickt haben: A, B, C = 3 eindeutige
- Tag 2: Kund:innen, die geklickt haben: B, C, D = 3 eindeutige

Das Chart zeigt 3 an Tag 1 und 3 an Tag 2. Über beide Tage hinweg sehen Sie 3 + 3 = 6. Die Kund:innen B und C werden einmal pro Tag gezählt, was beabsichtigt ist.

Diese Konfiguration beantwortet: „Wie viele eindeutige Kund:innen-Engagements gab es über die Tage hinweg?“ Sie beantwortet nicht: „Wie viele einzelne Kund:innen haben sich mindestens einmal über den gesamten Zeitraum engagiert?“

Wenn Ihr Ziel die Eindeutigkeit auf Fensterebene ist (eindeutige Personen über die gesamte Campaign oder das gesamte Quartal), ist das ein anderer Modellierungsansatz. Wenden Sie sich an Ihre:n AI Success Manager:in für Hinweise zur Gestaltung.