---
nav_title: Bericht zu angepassten Events
article_title: Bericht zu angepassten Events
page_order: 6
page_type: reference
description: "Diese Seite beschreibt, wie Sie den Bericht zu angepassten Events verwenden, um Vorkommen angepasster Events im Zeitverlauf nach Segment aufgeschlüsselt anzuzeigen."
tool: Reports
---

# Bericht zu angepassten Events {#custom-events-report}

> Der Bericht zu angepassten Events ermöglicht es Ihnen, die Vorkommen eines oder mehrerer angepasster Events im Zeitverlauf anzuzeigen. Sie können Ergebnisse nach Segment aufschlüsseln, KPI or Leistungskennzahl or Leistungskennzahlen-Formeln anwenden und die Daten für weitere Analysen exportieren.

## Einen Bericht anzeigen {#view-a-report}

Um diesen Bericht im Dashboard anzuzeigen, gehen Sie zu **Analytics** > **Custom Events Report**. Wählen Sie die angepassten Events aus, die Sie analysieren möchten. Das Diagramm wird automatisch gerendert, nachdem Sie ein Event ausgewählt haben.

![Angepasste Events]({% image_buster /assets/img_archive/Export_events.png %})

### Angepasste API-Events und App-Filter {#api-custom-events-and-app-filters}

Angepasste Events, die über den [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Endpunkt gesendet werden, können optional eine `app_id` enthalten. Im Gegensatz zu Events, die über das SDK or Software-Development-Kit protokolliert werden, sind API-Events nicht automatisch mit einer App verknüpft. Ohne `app_id` werden Events zwar aufgezeichnet, erscheinen aber nicht im Diagramm für angepasste Events, wenn ein App-Filter angewendet wird.

## Bericht konfigurieren {#configure-your-report}

Verwenden Sie die folgenden Optionen, um festzulegen, welche Daten im Diagramm für angepasste Events angezeigt werden.

| Option | Beschreibung |
| --- | --- |
| Apps | Standardmäßig enthält der Bericht Daten aus allen Apps. Verwenden Sie dieses Dropdown-Menü, um den Bericht auf eine bestimmte App einzugrenzen. |
| Aufschlüsselung angepasster Events nach | Steuert, wie die Zeitreihe für Ihr ausgewähltes angepasstes Event gruppiert wird. Standardmäßig zeigt das Chart den aggregierten Gesamttrend nach Datum. Wechseln Sie zu **Custom Events by Hour**, um Muster innerhalb eines Tages zu sehen, oder zu **Custom Events per MAU or monatlich aktive:r Nutzer:in**, um das Event-Volumen im Verhältnis zur Anzahl Ihrer monatlich aktiven Nutzer:innen zu normalisieren. |
| Nach Segments filtern | Schalten Sie diese Option ein, um Event-Zahlen nach einem oder mehreren Segments aufzuschlüsseln. Wenn aktiviert, wählen Sie die Segments aus, die Sie vergleichen möchten. Das Diagramm zeigt die Anzahl der Nutzer:innen in jedem Segment, die das angepasste Event ausgeführt haben. |
| KPI or Leistungskennzahl or Leistungskennzahlen-Formel | Ersetzt die rohe Event-Anzahl durch eine berechnete Kennzahl, die aus einem Zähler (z. B. Anzahl angepasster Events) und einem Nenner (z. B. täglich aktive:r Nutzer:in; täglich aktiv, MAU or monatlich aktive:r Nutzer:in oder Größe eines Analytics-fähigen Segments) besteht. Wenn Sie eine oder mehrere Formeln auswählen, stellt das Chart den Wert jeder Formel über den ausgewählten Zeitraum dar, sodass Sie normalisierte Performance vergleichen können (z. B. „Events pro aktivem/aktiver Nutzer:in“) anstatt des gesamten Event-Volumens. Falls für den ausgewählten Zeitraum und die Formeln keine Daten verfügbar sind, zeigt Braze eine Meldung „Keine Daten“ an – erweitern Sie den Zeitraum oder wählen Sie andere Formeln. Wählen Sie **Manage KPI or Leistungskennzahl or Leistungskennzahlen formulas**, um Formeln zu erstellen oder zu bearbeiten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bericht konfigurieren" }

## Daten exportieren {#export-data}

Um Ihre Daten zu angepassten Events zu exportieren, wählen Sie <i class="fas fa-bars" title="Chart-Kontextmenü"></i> **Chart-Kontextmenü** im Diagramm für angepasste Events aus und wählen Sie Ihre Exportoption.

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung beim Export]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

## Fehlerbehebung {#troubleshooting}

### Segment-Aufschlüsselung stimmt nicht mit den Workspace-Gesamtwerten überein {#segment-breakdown-doesnt-match-workspace-totals}

Wenn Sie **Nach Segments filtern** oder den Bericht über das **Apps**-Dropdown einschränken, zählt das Chart die Nutzer:innen im ausgewählten Segment (oder der App), die das angepasste Event ausgeführt haben – nicht jedes Event-Vorkommen im gesamten Workspace.

Wenn Sie eine Segment-Linie mit einer ungefilterten Ansicht (oder mit **Alle Apps**) vergleichen, weichen die Gesamtwerte häufig ab, weil:

- **Alle Apps** Nutzer:innen und Events aus jeder App im Workspace einschließen kann.
- Ein Einzelapp-Filter nur Profile umfasst, die mit dieser App verknüpft sind.
- Segment-Filter Nutzer:innen zählen, die zum Zeitpunkt der Abfrage der Segment-Definition entsprechen, was Nutzer:innen ausschließen kann, die das Event außerhalb der Segment-Kriterien ausgeführt haben.

Um Vergleichbares miteinander zu vergleichen, verwenden Sie denselben App-Filter und dieselbe Segment-Auswahl für jede Reihe, die Sie vergleichen, oder exportieren Sie die Daten und gleichen Sie die Zahlen in Ihrem Analytics-Tool ab.