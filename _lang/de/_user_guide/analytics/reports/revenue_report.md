---
nav_title: Umsatzbericht
article_title: Umsatzbericht
page_order: 7
page_type: reference
description: "Diese Seite beschreibt, wo Sie den Umsatzbericht im Braze-Dashboard finden und wie Sie Daten zum Umsatz über bestimmte Zeiträume, zum Produktumsatz und zum Gesamtumsatz Ihrer App anzeigen können."
tool: Reports
---

# Umsatzbericht {#revenue-report}

> Die Seite **Umsatzbericht** ermöglicht es Ihnen, Daten zum Umsatz über bestimmte Zeiträume, zum Umsatz eines bestimmten Produkts und zum Gesamtumsatz Ihrer App anzuzeigen.

Um Ihren Umsatzbericht im Braze-Dashboard anzuzeigen, gehen Sie zu **Analytics** > **Reports** > **Revenue Report**.

## Anpassen Ihres Umsatzberichts {#customizing-your-revenue-report}

Sie können Ihren Umsatzbericht anpassen, indem Sie einen Zeitraum, die zu berücksichtigenden Apps und Parameter auswählen.

![Die Seite „Umsatzbericht“ mit dem Diagramm „Performance im Zeitverlauf“, wobei „Umsatz“ als Parameter festgelegt ist.]({% image_buster /assets/img/revenue_report.png %})

### Filtern nach Datum und Apps {#filtering-by-date-and-apps}

Wählen Sie den Zeitraum für Ihren Umsatzbericht und, falls gewünscht, eine bestimmte App oder eine Auswahl von Apps aus.

### Filtern nach Parametern {#filtering-by-parameters}

Das Diagramm **Performance im Zeitverlauf** zeigt die Daten für verschiedene Parameter an, die im Dropdown **Statistiken für** ausgewählt werden können. Optional können Sie die Daten bestimmter Parameter im Dropdown **Aufschlüsselung** aufschlüsseln.

Die folgenden Daten können Sie im Diagramm **Performance im Zeitverlauf** einsehen:
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
Wenn Sie Umsätze für eine Währung ohne Wechselkurs erfassen, speichert Braze diese als Kauf von 0,00 US-Dollar.
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
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-revenue-per-user">Tagesumsatz pro Nutzer:in</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## Anzeigen der Produktaufschlüsselung {#viewing-the-product-breakdown}

In der Tabelle **Product Breakdown** finden Sie eine Liste der Produkte, die im ausgewählten Zeitraum gekauft wurden, die jeweilige Anzahl der Käufe sowie den Umsatz, den jedes Produkt generiert hat.

![Die Tabelle „Product Breakdown“ mit den Spalten „Product Name“, „Purchased“ und „Revenue“.]({% image_buster /assets/img/revenue_report_product_breakdown.png %})

## Umsatzdaten exportieren {#exporting-revenue-data}

Um Ihre Umsatzdaten zu exportieren, wählen Sie <i class="fas fa-bars" title="Kontextmenü des Charts"></i> **Kontextmenü des Charts** im Diagramm **Performance Over Time** aus und wählen Sie Ihre Exportoption.

{% alert tip %}
Suchen Sie nach weiteren Möglichkeiten, Umsatzdaten zu erhalten? Versuchen Sie, Kaufverhalten (sowie den Kauf eines Produkts) zu Campaigns oder Canvases als [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) hinzuzufügen.
{% endalert %}

Sie können Umsatzstatistiken auch fallweise auf den Seiten [Campaign Analytics]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) oder [Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics) einsehen.

{% alert tip %}
Umsatzberichte können nicht über die API exportiert werden. Hilfe zu CSV-Exporten finden Sie unter [Fehlerbehebung beim Export]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}