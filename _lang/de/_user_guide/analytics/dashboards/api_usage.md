---
nav_title: API-Nutzung
article_title: Dashboard für API-Nutzung
alias: "/api_usage/"
page_order: 5
description: "Dieser Artikel bietet eine Übersicht über das Dashboard für API-Nutzung."
---

# Dashboard für API-Nutzung {#api-usage-dashboard}

> Das Dashboard für API-Nutzung ermöglicht es Ihnen, Ihren eingehenden REST API-Traffic in Braze zu überwachen, um Trends in Ihrer Nutzung unserer REST APIs zu verstehen und potenzielle Probleme zu beheben.

## Über das Dashboard für API-Nutzung {#about-the-api-usage-dashboard}

Um Ihr Dashboard für API-Nutzung aufzurufen, gehen Sie zu **Einstellungen** > **APIs und Bezeichner** und wählen Sie dann **Dashboard** aus.

Das Standard-Dashboard zeigt alle eingehenden REST API-Anfragen für Ihren Workspace über den letzten Tag (24 Stunden) an. Je nach Anwendungsfall können Sie die Dashboard-Steuerelemente anpassen, um den Traffic zu filtern oder zu gruppieren, und auch den Zeitraum des Dashboards konfigurieren.

![Dashboard für API-Nutzung mit insgesamt 130 Anfragen, einer Erfolgsrate von 70 Prozent und einer Fehlerrate von 30 Prozent.]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## Verfügbare Metriken {#available-metrics}

Das Dashboard für API-Nutzung enthält die folgenden Statistiken:

| Metrik         | Beschreibung |
|----------------|-------------|
| Anfragen gesamt | Die Gesamtzahl der Anfragen, die für Ihren aktuellen Workspace an Braze gesendet wurden, basierend auf den angewendeten Filtern und Steuerelementen des Dashboards. |
| Erfolgsrate   | Der Prozentsatz der Gesamtanfragen, bei denen Braze eine `2XX`-Erfolgsantwort zurückgegeben hat. |
| Fehlerrate     | Der Prozentsatz der Gesamtanfragen, bei denen Braze eine `4XX`- oder `5XX`-Fehlerantwort zurückgegeben hat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verfügbare Metriken" }

## Das Dashboard verwenden {#using-the-dashboard}

![Filter, die auf das Dashboard angewendet werden können, darunter: API-Schlüssel, Endpunkt, Antwortcodes, Daten gruppieren und Datum.]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### Filter {#filters}

Wählen Sie **Filter** aus, um die Ansicht des REST API-Traffics für Ihren Workspace einzugrenzen, darunter:

- API-Schlüssel
- Endpunkt
- Antwortcode

### Daten gruppieren {#group-data}

Sie können Daten in verschiedene Datenreihen gruppieren, um unterschiedliche Muster in Ihrer Nutzung zu untersuchen, darunter:

- Antwortcodes (Standard)
- API-Endpunkt
- API-Schlüssel
- Nur Erfolg und Fehler

### Datum {#date}

Passen Sie den Datumsfilter an, um bei Bedarf einen kleineren oder größeren Zeitraum anzuzeigen. Dazu gehören:

- Heute (Standard)
- Benutzerdefiniert
- Letzte 3 Stunden
- Letzte 6 Stunden
- Letzte 12 Stunden
- Letzte 24 Stunden
- Gestern
- Letzte 7 Tage
- Letzte 14 Tage
- Letzte 30 Tage
- Letzter Monat bis heute

{% alert note %}
Die Optionen **Letzte 3 Stunden** und **Letzte 6 Stunden** zeigen den Traffic minutenweise an. Größere Zeiträume zeigen den Traffic alle fünf Minuten, stündlich oder täglich an.
{% endalert %}

## Hinweise {#considerations}

Das Dashboard für API-Nutzung umfasst alle REST API-Anfragen, die Braze empfangen hat und für die eine `2XX`-, `4XX`- oder `5XX`-Antwort zurückgegeben wurde. Dies schließt Datentransformation-Ausgaben und Cloud-Datenaufnahme-Synchronisierungen ein. SDK-Traffic und Nutzeraktualisierung-Schritte sind in diesem Dashboard nicht enthalten.

Die im Dashboard angezeigten Daten können eine kurze Verzögerung bei der Darstellung des aktuellen Traffics aufweisen. In Zeiten hoher Nutzung können Sie das Dashboard bis zu 4 Mal pro Minute aktualisieren. Möglicherweise müssen Sie einige Minuten warten, bevor Sie das Dashboard erneut aktualisieren können.

## Verwandte Artikel {#related-articles}

- [API-Nutzungswarnungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts/)
- [Rate-Limits]({{site.baseurl}}/api/api_limits/)