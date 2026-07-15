---
nav_title: Umsatzbericht
article_title: Umsatzbericht
page_order: 7
page_type: reference
description: "Diese Seite beschreibt, wie Sie die Seite „Umsatzbericht“ verwenden, um Daten zum Umsatz über bestimmte Zeiträume, zum Umsatz eines bestimmten Produkts und zum Gesamtumsatz Ihrer App anzuzeigen."
tool: Reports
---

# Umsatzbericht {#revenue-report}

> Die Seite **Umsatzbericht** ermöglicht es Ihnen, Daten zum Umsatz über bestimmte Zeiträume, zum Umsatz eines bestimmten Produkts und zum Gesamtumsatz Ihrer App anzuzeigen.

Um einen Bericht zu Ihrem Umsatz im Dashboard anzuzeigen, gehen Sie zu **Analytics** > **Revenue Report**.

## Ihren Umsatzbericht anpassen {#customizing-your-revenue-report}

Sie können Ihren Umsatzbericht anpassen, indem Sie einen Datumsbereich, die zu berücksichtigenden Apps und Parameter auswählen.

![Die Seite „Revenue Report“ mit dem Diagramm „Performance Over Time“, bei dem „Revenue“ als Parameter eingestellt ist.]({% image_buster /assets/img/revenue_report.png %})

### Nach Datum und Apps filtern {#filtering-by-date-and-apps}

Wählen Sie den Datumsbereich für Ihren Umsatzbericht und optional eine bestimmte App oder eine Auswahl von Apps aus.

### Nach Parametern filtern {#filtering-by-parameters}

Das Diagramm **Performance Over Time** zeigt die Daten für verschiedene Parameter an, die im Dropdown **Statistics for** ausgewählt werden können. Optional können Sie die Daten bestimmter Parameter im Dropdown **Breakdown** aufschlüsseln.

Sie können die folgenden Daten im Diagramm **Performance Over Time** anzeigen:
- KPI-Formeln
- Käufe
    - (Optional) Käufe nach Produkt
- Umsatz
    - (Optional) Umsatz nach Segment
    - (Optional) Umsatz nach Produkt
- Umsatz pro Stunde
    - (Optional) Umsatz pro Stunde nach Segment
- Umsatz pro Nutzer:in

## Umsatzberechnungen verstehen {#understanding-revenue-calculations}

{% alert note %}
Wenn Sie Umsatz für eine Währung ohne Wechselkurs erfassen, zeichnet Braze dies als Kauf von 0,00 US-Dollar auf.
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Umsatzberechnungen verstehen">
  <caption>Umsatzberechnungen verstehen</caption>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-revenue">Lifetime-Umsatz</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-value-per-user">Lifetime-Value pro Nutzer:in</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#average-daily-revenue">Durchschnittlicher Tagesumsatz</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-purchases">Tägliche Käufe</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-revenue-per-user">Täglicher Umsatz pro Nutzer:in</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## Die Produktaufschlüsselung anzeigen {#viewing-the-product-breakdown}

In der Tabelle **Product Breakdown** finden Sie eine Liste der Produkte, die im ausgewählten Datumsbereich gekauft wurden, die Anzahl der Käufe pro Produkt und den Umsatz, den jedes Produkt generiert hat.

![Die Tabelle „Product Breakdown“ mit den Spalten „Product Name“, „Purchased“ und „Revenue“.]({% image_buster /assets/img/revenue_report_product_breakdown.png %})

## Umsatzdaten exportieren {#exporting-revenue-data}

Um Ihre Umsatzdaten zu exportieren, wählen Sie <i class="fas fa-bars" title="Chart-Kontextmenü"></i> **Chart-Kontextmenü** im Diagramm **Performance Over Time** und wählen Sie Ihre Exportoption aus.

{% alert tip %}
Suchen Sie nach weiteren Möglichkeiten, Umsatzdaten zu erhalten? Versuchen Sie, Kaufverhalten (sowie den Kauf eines Produkts) zu Campaigns oder Canvases als [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) hinzuzufügen.
{% endalert %}

Sie können Umsatzstatistiken auch fallweise auf den Seiten [Campaign Analytics]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) oder [Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics) einsehen.

{% alert tip %}
Umsatzberichte können nicht über die API exportiert werden. Hilfe zu CSV-Exporten finden Sie unter [Fehlerbehebung beim Export]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}