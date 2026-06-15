---
nav_title: Bericht zu angepassten Events
article_title: Bericht zu angepassten Events
page_order: 6
page_type: reference
description: "Diese Seite beschreibt, wie Sie den Bericht zu angepassten Events verwenden, um Vorkommen angepasster Events im Zeitverlauf nach Segment aufgeschlüsselt anzuzeigen."
tool: Reports
---

# Bericht zu angepassten Events {#custom-events-report}

> Der Bericht zu angepassten Events ermöglicht es Ihnen, die Vorkommen eines oder mehrerer angepasster Events im Zeitverlauf anzuzeigen. Sie können Ergebnisse nach Segment aufschlüsseln, KPI-Formeln anwenden und die Daten für weitere Analysen exportieren.

## Einen Bericht anzeigen {#viewing-a-report}

Um diesen Bericht im Dashboard anzuzeigen, gehen Sie zu **Analytics** > **Bericht zu angepassten Events**. Wählen Sie die angepassten Events aus, die Sie analysieren möchten, und wählen Sie dann **Apply**, um das Diagramm zu generieren.

![Angepasste Events]({% image_buster /assets/img_archive/Export_events.png %})

## Ihren Bericht konfigurieren {#configuring-your-report}

Verwenden Sie die folgenden Optionen, um anzupassen, welche Daten im Diagramm **Performance Over Time** angezeigt werden.

| Option | Beschreibung |
| --- | --- |
| Apps | Standardmäßig enthält der Bericht Daten aus allen Apps. Verwenden Sie dieses Dropdown, um den Bericht auf eine bestimmte App einzugrenzen. |
| Angepasste Events aufschlüsseln nach | Steuert, wie die Zeitreihe für Ihr ausgewähltes angepasstes Event gruppiert wird. Standardmäßig zeigt das Chart den aggregierten Gesamttrend nach Datum an. Wechseln Sie zu **Custom Events by Hour**, um Muster innerhalb eines Tages zu sehen, oder zu **Custom Events per MAU**, um das Event-Volumen gegen Ihre Zahl monatlich aktiver Nutzer:innen zu normalisieren. |
| Nach Segmenten filtern | Aktivieren Sie diese Option, um Event-Zahlen nach einem oder mehreren Segmenten aufzuschlüsseln. Wenn aktiviert, wählen Sie die Segmente aus, die Sie vergleichen möchten. Das Diagramm zeigt die Anzahl der Nutzer:innen in jedem Segment, die das angepasste Event ausgeführt haben. |
| KPI-Formel | Ersetzt die rohe Event-Zahl durch eine berechnete Metrik, die aus einem Zähler (z. B. einer Zahl angepasster Events) und einem Nenner (z. B. DAU, MAU oder einer Analytics-fähigen Segmentgröße) besteht. Wenn Sie eine oder mehrere Formeln auswählen, stellt das Chart den Wert jeder Formel über den ausgewählten Zeitraum dar, sodass Sie normalisierte Performance vergleichen können (z. B. „Events pro aktive:n Nutzer:in“) anstelle des gesamten Event-Volumens. Wenn für den ausgewählten Zeitraum und die Formeln keine Daten verfügbar sind, zeigt Braze eine Meldung „Keine Daten“ an – erweitern Sie den Zeitraum oder wählen Sie andere Formeln. Wählen Sie **Manage KPI formulas**, um Formeln zu erstellen oder zu bearbeiten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ihren Bericht konfigurieren" }

## Daten exportieren {#exporting-data}

Um Ihre Daten zu angepassten Events zu exportieren, wählen Sie <i class="fas fa-bars" title="Chart-Kontextmenü"></i> **Chart-Kontextmenü** im Diagramm **Performance Over Time** und wählen Sie Ihre Exportoption.

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung beim Export]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}

## Fehlerbehebung {#troubleshooting}

### Segment-Aufschlüsselung stimmt nicht mit Workspace-Gesamtwerten überein {#segment-breakdown-doesnt-match-workspace-totals}

Wenn Sie **Nach Segmenten filtern** verwenden oder den Bericht über das Dropdown **Apps** eingrenzen, zählt das Diagramm die Nutzer:innen im ausgewählten Segment (oder der App), die das angepasste Event ausgeführt haben – nicht jedes Event-Vorkommen im gesamten Workspace.

Wenn Sie eine Segment-Linie mit einer ungefilterten Ansicht (oder mit **All Apps**) vergleichen, unterscheiden sich die Gesamtwerte häufig, weil:

- **All Apps** Nutzer:innen und Events aus jeder App im Workspace einschließen kann.
- Ein Einzelapp-Filter nur Profile einschließt, die mit dieser App verknüpft sind.
- Segment-Filter Nutzer:innen zählen, die zum Zeitpunkt der Abfrage der Segmentdefinition entsprechen, was Nutzer:innen ausschließen kann, die das Event außerhalb der Segmentkriterien ausgeführt haben.

Um Gleiches mit Gleichem zu vergleichen, verwenden Sie denselben App-Filter und dieselbe Segmentauswahl für jede Reihe, die Sie vergleichen, oder exportieren Sie die Daten und gleichen Sie die Zahlen in Ihrem Analytics-Tool ab.