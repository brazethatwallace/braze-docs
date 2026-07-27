---
nav_title: Clarisights
article_title: Clarisights
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Clarisights, einer Self-Service-Plattform für Performance-Marketing-Reporting, die es Ihnen ermöglicht, Daten aus Braze Campaigns und Canvases zu importieren, um eine einheitliche Berichtsoberfläche für Performance- und CRM/Bindungsmarketing zu schaffen."
alias: /partners/clarisights/
page_type: partner
search_tag: Partner

---

# Clarisights

> [Clarisights](https://clarisights.com) ist eine Self-Service-Plattform für Performance-Marketing-Berichte für datengestützte Unternehmen. Sie integriert, verarbeitet und visualisiert automatisch alle Ihre Daten aus Marketing-, Analytics- und Attributionsquellen.

_Diese Integration wird von Clarisights gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Clarisights ermöglicht es Ihnen, Daten aus Braze Campaigns und Canvases zu importieren, um eine einheitliche Berichtsoberfläche für Performance- und CRM/Bindungsmarketing zu schaffen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Clarisights-Konto | Ein Clarisights-Workspace ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit den folgenden Berechtigungen: <br> - `campaigns.list` <br>  - `campaigns.details`<br> - `campaigns.data_series` <br> - `canvas.details`<br> - `canvas.list` <br>  - `canvas.data_series` <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Braze-Workspace-Name | Der Name des Workspace, der mit dem Braze-API-Schlüssel verknüpft ist. Dieser Name wird verwendet, um die Workspace-Integration in Clarisights zu identifizieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle {#use-cases}

Mit der Integration von Braze und Clarisights können Nutzer:innen verschiedene Visualisierungen und Tabellen erstellen, um Insights aus den von ihnen erstellten Campaigns zu gewinnen. Beliebte Anwendungsfälle sind unter anderem:

{% tabs %}
{% tab Bessere Sichtbarkeit %}
Bessere Sichtbarkeit der gesamten Performance von Campaigns und Canvases.

![Eine Grafik mit einem Beispiel für bessere Sichtbarkeit in der Clarisights-Plattform. Diese Grafik enthält Statistiken zu Öffnungen, Klicks, Versendungen, Conversions usw. von Campaigns und Canvases.]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab Detaillierte Berichte %}
Detaillierte Berichte für Campaigns und Canvases.

![Eine Grafik mit detaillierten Berichten, wie z. B. „insgesamt gesendet nach Kanal“ und „Konversionsrate“.]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab Einheitliche Dashboards %}
Einheitliche Dashboards für CMOs und CXOs.

![Eine Grafik mit einem Beispiel für einheitliche Dashboards.]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## Integration

Um Braze-Daten mit Clarisights zu synchronisieren, müssen Sie einen Braze-Konnektor erstellen und Braze-Workspaces verbinden.

1. Navigieren Sie in Clarisights zur Seite **Integrations**, suchen Sie den **Braze**-Konnektor und wählen Sie **+ Connect**.<br>![Eine Liste der verfügbaren Konnektoren aus dem Clarisights-Integrationsmarktplatz.]({{site.baseurl}}/assets/img/clarisights/integrations.png)<br><br>
2. Verbinden Sie anschließend über den Integrationsablauf Ihr Clarisights-Konto mit Braze. Dazu müssen Sie Ihren Braze-REST-API-Schlüssel, den Braze-Workspace-Namen und den Braze-REST-Endpunkt angeben.<br>![Braze-Workspace-Konnektor in der Clarisights-Plattform. Diese Seite enthält Felder für den Braze-Workspace-Namen, den Braze-REST-API-Schlüssel und den Braze-REST-Endpunkt.]({{site.baseurl}}/assets/img/clarisights/braze_flow.png)<br><br>Vor der erfolgreichen Integration sehen die Nutzer:innen die verbundenen Workspaces auf derselben Seite.<br>![Unter „Braze Accounts“ finden Sie eine Liste der verbundenen Workspaces.]({{site.baseurl}}/assets/img/clarisights/connected.png)<br><br>

## Verwendung dieser Integration {#using-this-integration}

Um Braze als Datenquelle in Ihre Clarisights-Berichte aufzunehmen, navigieren Sie zu **Create New Report**. Benennen Sie Ihren Bericht und wählen Sie **Braze** als Datenquelle in der angezeigten Eingabeaufforderung aus. Sie können auch die Metriken und Dimensionen auswählen, die in den Bericht aufgenommen werden sollen. Wenn Sie fertig sind, wählen Sie **Create Report**.

Die Daten aus Braze werden ab dem Zeitpunkt des nächsten geplanten Datenimports übertragen. Kontaktieren Sie Ihren Customer-Success-Manager von Clarisights, um Backfills für längere Zeiträume anzufordern.

![Clarisights-Berichtseinstellungen mit Feldern für Name und Datenquelle. In diesem Beispiel ist „Braze“ als Datenquelle ausgewählt.]({{site.baseurl}}/assets/img/clarisights/braze_report.png)

Besuchen Sie Clarisights für weitere Informationen zu den verfügbaren [Metriken und Dimensionen](https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions) oder zur [Erstellung von Berichten](https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights).