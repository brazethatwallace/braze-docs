---
nav_title: E-Commerce-Anwendungsfälle
article_title: E-Commerce-Anwendungsfälle
alias: /ecommerce_use_cases/
page_order: 4
description: "Dieser Referenzartikel behandelt mehrere vorgefertigte Braze Templates, die speziell für E-Commerce-Marketer entwickelt wurden und die Umsetzung wesentlicher Strategien erleichtern."
toc_headers: h2
---

# So verwenden Sie empfohlene E-Commerce-Events {#how-to-use-ecommerce-recommended-events}

> Diese Seite beschreibt, wie und wo Sie empfohlene E-Commerce-Events plattformübergreifend nutzen können, einschließlich der Verwendung von Braze E-Commerce-Canvas-Templates.

{% alert note %}
Wenn Sie den neuen Shopify-Konnektor verwenden, stehen empfohlene E-Commerce-Events automatisch über die Integration zur Verfügung.
{% endalert %}

## Ein Canvas-Template verwenden {#using-a-canvas-template}

So verwenden Sie ein Canvas-Template:
1. Gehen Sie zu **Messaging** > **Canvas**.
2. Wählen Sie **Create Canvas** > **Use a Canvas Template**.
3. Durchsuchen Sie den Tab **Braze templates** nach dem gewünschten Template. Sie können ein Template in der Vorschau anzeigen, indem Sie auf seinen Namen klicken.
4. Wählen Sie **Apply Template** für das gewünschte Template.<br><br>![Die Seite „Canvas templates“ ist auf dem Tab „Braze templates“ geöffnet und zeigt eine Liste der zuletzt verwendeten Templates sowie auswählbare Braze Templates.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## E-Commerce-Canvas-Templates {#ecommerce-canvas-templates}

Braze bietet vier E-Commerce-Canvas-Templates.

{% multi_lang_include canvas/ecommerce_templates.md %}

## Nachrichten-Personalisierung {#message-personalization}

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) ist eine leistungsstarke Template-Sprache, die von Braze verwendet wird und es Ihnen ermöglicht, dynamischen und personalisierten Content für Ihre Kund:innen zu erstellen. Durch die Verwendung von Liquid-Tags können Sie Nachrichten basierend auf Kundendaten, Produktinformationen und anderen Variablen anpassen, das Einkaufserlebnis verbessern und das Engagement steigern.

### Wichtige Features von Liquid {#key-features-of-liquid}

- **Dynamischer Content:** Fügen Sie kundenspezifische Informationen wie Namen, Bestelldetails und Präferenzen in Ihre Nachrichten ein.
- **Bedingte Logik:** Verwenden Sie if/else-Anweisungen, um unterschiedlichen Content basierend auf bestimmten Bedingungen anzuzeigen (z. B. Standort und Kaufhistorie der Kund:innen).
- **Schleifen:** Iterieren Sie über Sammlungen von Produkten oder Kundendaten, um Listen oder Raster von Artikeln anzuzeigen.

### Erste Schritte mit Liquid {#getting-started-with-liquid}

Um mit der Personalisierung Ihrer Nachrichten mithilfe von Liquid-Tags zu beginnen, können Sie die folgenden Ressourcen nutzen:

- [Shopify-Daten]({{site.baseurl}}/shopify_features/#shopify-data)-Referenz mit vordefinierten Liquid-Tags
- [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)

## Segmentierung {#segmentation}

Verwenden Sie Braze Segments, um gezielte Kundensegmente basierend auf bestimmten Attributen und Verhaltensweisen zu erstellen und personalisiertes Messaging und Kampagnen bereitzustellen. Mit diesem leistungsstarken Feature können Sie Ihre Kund:innen effektiv ansprechen, indem Sie die richtige Zielgruppe mit der richtigen Nachricht zur richtigen Zeit erreichen.

Weitere Informationen zu den ersten Schritten mit Segmenten finden Sie unter [Über Braze Segments]({{site.baseurl}}/user_guide/audience/segments/#about-braze-segments).

### Empfohlene Events {#recommended-events}

E-Commerce-Events basieren auf [empfohlenen Events]({{site.baseurl}}/recommended_events/).
Da empfohlene Events stärker vordefinierte angepasste Events sind, können Sie nach den empfohlenen E-Commerce-Event-Namen suchen, indem Sie einen beliebigen [Filter für angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events/#segmentation-filters) auswählen.

### E-Commerce-Filter {#ecommerce-filters}

Segmentieren Sie Ihre Nutzer:innen mit E-Commerce-Filtern wie **Ecommerce Source** und **Total Revenue**, indem Sie im Segmenter zum Abschnitt **Ecommerce** navigieren.

Eine Liste der E-Commerce-Filter und ihrer Definitionen finden Sie unter [Segment-Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/). Wählen Sie dort die Suchkategorie „eCommerce“ aus.

![Dropdown der Segment-Filter mit „Ecommerce“-Filtern.]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## Verschachtelte Event-Eigenschaften {#nested-event-properties}

Um nach verschachtelten Event-Eigenschaften zu segmentieren, können Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/#why-use-segment-extensions) nutzen. Sie können beispielsweise Segmenterweiterungen verwenden, um herauszufinden, wer das Produkt „SKU-123“ in den letzten 90 Tagen gekauft hat.

## Analytics {#analytics}

### Bericht zu angepassten Events {#custom-events-report}

Sie können das Volumen empfohlener E-Commerce-Events im [Bericht zu angepassten Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events/#analytics) verfolgen. Filtern Sie nach **Perform Custom Event** und geben Sie dann den [Namen des empfohlenen E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events) an, um dessen Performance im Zeitverlauf anzuzeigen.

![Chart für angepasste Events mit Ergebnissen für sechs ausgewählte Events.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### Dashboards {#dashboards}

#### Conversions-Dashboard {#conversions-dashboard}

Nachdem Sie eine Kampagne oder ein Canvas mit dem Conversion-Event „Places Order“ gestartet haben, können Sie einen entsprechenden [Conversion-Bericht]({{site.baseurl}}/user_guide/analytics/dashboards/conversions/#setting-up-your-report) erstellen, um die Performance zu verfolgen.

![Tabelle mit Conversion-Details mit Kampagnen und Canvases sowie den zugehörigen Conversion-Statistiken.]({% image_buster /assets/img_archive/conversion_details_table.png %})

#### E-Commerce-Umsatz-Dashboard {#ecommerce-revenue-dashboard}

Um Insights zum Umsatz zu erhalten, der der letzten Kampagne oder dem letzten Canvas zugeordnet wird, mit der bzw. dem ein:e Nutzer:in vor einer Bestellung interagiert hat, verwenden Sie das [E-Commerce-Umsatz-Dashboard]({{site.baseurl}}/ecommerce_revenue_dashboard/) und wählen Sie ein Conversion-Fenster aus.

### Umsatzbericht {#revenue-report}

Um Daten aus diesen neuen Events zu analysieren, gehen Sie zum [Dashboard-Builder]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/) und sehen Sie sich das Dashboard [**eCommerce Revenue - Last Touch Attribution**]({{site.baseurl}}/ecommerce_revenue_dashboard/) an.