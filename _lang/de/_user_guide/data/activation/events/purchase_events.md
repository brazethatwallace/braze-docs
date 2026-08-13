---
nav_title: Kauf-Events
article_title: Kauf-Events
page_order: 3
page_type: reference
description: "Dieser Referenzartikel beschreibt Kauf-Events und Kaufeigenschaften, ihre Verwendung, Segmentierung, wo Sie relevante Analytics einsehen können und vieles mehr."
search_rank: 3
---

# Kauf-Events {#purchase-events}

> Diese Seite befasst sich mit Kauf-Events und Eigenschaften, ihrer Verwendung, Segmentierung, wo Sie relevante Analytics einsehen können und mehr.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Kauf-Events sind Kaufaktionen Ihrer Nutzer:innen und werden verwendet, um In-App-Käufe zu erfassen und den Lifetime-Value (LTV) für jedes Nutzerprofil zu ermitteln. Diese Events müssen von Ihrem Team eingerichtet werden. Die Protokollierung von Kauf-Events ermöglicht es Ihnen, Eigenschaften wie Menge und Typ hinzuzufügen, sodass Sie Ihre Nutzer:innen auf der Grundlage dieser Eigenschaften noch gezielter ansprechen können.

## Kauf-Events protokollieren {#log-purchase-events}

Sie können Käufe protokollieren, indem Sie ein [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object) über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) übergeben oder eine unserer SDK-Bibliotheken verwenden, die im folgenden Abschnitt aufgeführt sind.

{% alert note %}
Event-Eigenschaften von Kauf-Events verwenden dieselben Datentypen wie [angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events#expected-format).
{% endalert %}

Im Folgenden finden Sie die Methoden, die auf verschiedenen Plattformen zum Protokollieren von Käufen verwendet werden. Auf diesen Seiten finden Sie auch Dokumentation dazu, wie Sie Eigenschaften und Mengen zu Ihrem Kauf-Event hinzufügen können. Basierend auf diesen Eigenschaften können Sie Ihre Nutzer:innen noch gezielter ansprechen.

- [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=swift)
- [Internet]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=unity)
- [.NET MAUI (ehemals Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=roku)

## Kaufdaten anzeigen {#view-purchase-data}

Nachdem Sie Kauf-Events eingerichtet und mit der Protokollierung begonnen haben, können Sie diese Kaufdaten im Profil einer Nutzer:in auf dem [Tab „Übersicht“]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#overview-tab) einsehen.

## Kaufdaten verwenden {#use-purchase-data}

Es gibt verschiedene Möglichkeiten, Kaufdaten in Braze zu nutzen:

- **[Segmentierung](#purchase-event-segmentation):** Verwenden Sie Kaufdaten, um Segments von Nutzer:innen basierend auf ihrem Kaufverhalten zu erstellen.
- **[Personalisierung](#personalization):** Verwenden Sie Kaufdaten, um Nachrichten an Nutzer:innen zu personalisieren.
- **[Nachrichten triggern](#trigger-messages):** Richten Sie Nachrichten ein, die basierend auf Kauf-Events getriggert werden.
- **[Analytics](#analytics):** Analysieren Sie Ihre Kaufdaten, um Insights in das Nutzerverhalten und die Effektivität Ihrer Marketing-Campaigns zu gewinnen.

### Segmentierung {#purchase-event-segmentation}

Sie können beliebig viele oder verschiedene Arten von Folgekampagnen basierend auf protokollierten Kauf-Events triggern. Zum Beispiel können Sie ein Segment von Nutzer:innen erstellen, die in den letzten 30 Tagen einen Kauf getätigt haben, oder ein Segment von Nutzer:innen, die über einen bestimmten Betrag ausgegeben haben.

Die folgenden Segmentierungsfilter stehen beim Targeting von Nutzer:innen zur Verfügung:

- First Made Purchase
- First Purchase For App
- Last Purchased Product
- Money Spent
- Purchased Product
- Total Number of Purchases
- X Money Spent in Y Days
- X Product Purchased in Y Days
- X Purchase Property in Y Days
- X Purchases in Last Y Days

Für Details zu jedem Filter lesen Sie das Glossar der [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) und filtern Sie nach „Purchase behavior“.

![Filtern nach Nutzer:innen, die genau drei Käufe getätigt haben]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %}
Um nach der Anzahl der Käufe eines bestimmten Produkts zu segmentieren, erfassen Sie diesen Kauf einzeln als [inkrementierendes angepasstes Attribut]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview#custom-attribute-storage).
{% endalert %}

### Personalisierung {#personalization}

Wie bei jeder anderen Art von Daten, die Sie von Ihren Nutzer:innen erfassen, können Sie Kaufdaten nutzen, um Ihr Messaging über Liquid zu personalisieren. Zum Beispiel können Sie eine personalisierte E-Mail an Nutzer:innen senden, in der Sie Produkte empfehlen, die denen ähneln, die sie gerade gekauft haben.

Angenommen, Sie haben eine Kauf-Event-Eigenschaft namens `last_purchased_product`, die den Namen des letzten Produkts speichert, das ein:e Nutzer:in gekauft hat. Sie können diese Eigenschaft verwenden, um eine E-Mail-Nachricht wie folgt zu personalisieren:

{% raw %}

```liquid
{% if ${last_purchased_product} == "Running Shoes" %}
  We hope you're enjoying your new running shoes! Based on your recent purchase, you might also like these running shorts and water bottles.
{% elsif ${last_purchased_product} == "Yoga Mat" %}
  We hope you're enjoying your new yoga mat! Based on your recent purchase, you might also like these yoga blocks and straps.
{% else %}
  Thank you for your recent purchase! We hope you're enjoying your new item.
{% endif %}
```

{% endraw %}

In diesem Beispiel wird die Nachricht basierend auf der Eigenschaft `last_purchased_product` personalisiert. Wenn das letzte Produkt, das der/die Nutzer:in gekauft hat, „Running Shoes“ war, erhält er/sie eine Nachricht mit Empfehlungen für Laufshorts und Wasserflaschen. Wenn das letzte Produkt „Yoga Mat“ war, erhält er/sie eine Nachricht mit Empfehlungen für Yogablöcke und -gurte. Wenn `last_purchased_product` etwas anderes ist, erhält er/sie eine allgemeine Dankesnachricht.

### Nachrichten triggern {#trigger-messages}

Ein häufiger Anwendungsfall ist das automatische Senden einer Nachricht, z. B. einer E-Mail, wenn ein:e Nutzer:in einen Kauf tätigt. Zum Beispiel können Sie eine Dankesnachricht oder einen Rabattcode für einen zukünftigen Kauf senden.

Erstellen Sie dazu eine aktionsbasierte Campaign oder ein Canvas und setzen Sie die Trigger-Aktion auf **Make Purchase**. Sie können auch zusätzliche Bedingungen für den Trigger festlegen, wie das gekaufte Produkt oder den Kaufbetrag.

Sie können Ihre getriggerte Nachricht auch mit Liquid personalisieren. Im folgenden Beispiel ist `${purchase_product_name}` ein angepasstes Attribut, das Sie durch den tatsächlichen Attributnamen ersetzen würden, der den Namen des gekauften Produkts in Ihrem Braze-Setup speichert.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### Analytics {#analytics}

Zusätzlich zum Tracking von Kauf-Metriken für die Segmentierung erfasst Braze auch die Anzahl der Käufe für jedes Produkt und den im Laufe der Zeit generierten Umsatz. Dies kann hilfreich sein, um die beliebtesten Produkte zu identifizieren oder die Auswirkungen einer Werbeaktion auf den Umsatz zu messen.

Sie finden diese Daten auf der Seite [Umsatzbericht]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#exporting-revenue-data).

### Umsatzberechnungen {#revenue-calculations}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Umsatzberechnungen">
  <caption>Umsatzberechnungen</caption>
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

#### Währungsumrechnung {#currency-conversion}

Wenn Kauf-Events in einer Nicht-USD-Währung protokolliert werden, rechnet Braze den Betrag mithilfe von Wechselkursen von [Open Exchange Rates](http://openexchangerates.org) in USD um. Diese Kurse werden einmal alle 24 Stunden aktualisiert (ungefähr um 4 Uhr morgens ET). Da die Wechselkurse zwischengespeichert werden, kann es zu geringfügigen Abweichungen vom Echtzeit-Marktkurs kommen, insbesondere bei Währungen mit starken Schwankungen.

#### Berechnung des Lifetime-Umsatzes {#lifetime-revenue-calculation}

Braze verwendet Kauf-Events, um den Lifetime-Umsatz (auch Lifetime-Value oder LTV genannt) eines/einer Nutzer:in zu berechnen. Dies ist eine Prognose des Nettogewinns, der der gesamten zukünftigen Beziehung mit einem/einer Kund:in zugeordnet wird. Dies kann Ihnen helfen, fundierte Entscheidungen über Strategien zur Kundengewinnung und -bindung zu treffen.

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$

Es gibt zwei Hauptstellen in Braze, an denen Sie den LTV Ihrer Nutzer:innen einsehen können:

- Für Gesamtmetriken wie *Lifetime-Umsatz* und den *Lifetime-Value pro Nutzer:in* für jede App und Website lesen Sie Ihren [Umsatzbericht]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#exporting-revenue-data).
- Um den Lifetime-Umsatz eines/einer bestimmten Nutzer:in zu verstehen, sehen Sie sich das [Nutzerprofil]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#overview-tab) an.

##### Auswirkungen von Rückerstattungen auf den Lifetime-Umsatz {#impact-of-refunds-on-lifetime-revenue}

Wenn Sie Kauf-Events zum Tracking von Kaufdaten verwenden, sollten Sie Rückerstattungen erfassen, indem Sie ein Braze-Kauf-Event mit einer negativen `price`-Eigenschaft protokollieren. Dieser Ansatz sorgt für eine genaue Gesamtsumme des Lifetime-Umsatzes.

Beachten Sie jedoch, dass die Rückerstattung als zusätzliches Kauf-Event gezählt wird. Betrachten wir das folgende Beispiel: Sam tätigt seinen ersten Kauf über 12 $ und gibt einen Teil des Kaufs für eine Rückerstattung von 5 $ zurück. Sams Profil würde Folgendes protokollieren:

- 1 Kauf mit einem Preis von 12 $
- 1 Kauf mit einem Preis von -5 $
- Lifetime-Umsatz von 7 $

Obwohl Sam zwei Kauf-Events in seinem Profil hätte, hat er in Wirklichkeit nur einen Kauf getätigt. Dies ist wichtig zu berücksichtigen, wenn Sie Segmente oder Anwendungsfälle haben, die auf der Anzahl der Käufe eines/einer Nutzer:in basieren. Häufige Rückerstattungen erhöhen die Kaufanzahl im Profil des/der Nutzer:in.

## Kauf-Event-Eigenschaften {#purchase-properties}

Mit Kauf-Event-Eigenschaften können Sie Eigenschaften für Käufe festlegen, die verwendet werden können, um Trigger-Bedingungen weiter zu qualifizieren, die Personalisierung im Messaging zu verbessern und über den Rohdatenexport anspruchsvollere Analytics zu erstellen. Eigenschaftswerttypen (String, numerisch, Boolescher Wert, Datum) variieren je nach Plattform und werden häufig als Schlüssel-Wert-Paare zugewiesen.

{% alert warning %}
Die folgenden Schlüssel sind reserviert und können nicht als Namen für Kauf-Event-Eigenschaften verwendet werden: `time`, `product_id`, `quantity`, `event_name`, `price` und `currency`. Die Verwendung eines reservierten Schlüssels im `properties`-Objekt gibt den Fehler „Invalid 'properties' field“ zurück.
{% endalert %}

Wenn Sie beispielsweise eine E-Commerce-Anwendung haben und einer Nutzerin oder einem Nutzer nach einem Kauf eine Nachricht senden möchten, können Sie Ihre Zielgruppe zusätzlich verbessern und eine erhöhte Campaign-Personalisierung ermöglichen, indem Sie eine Kauf-Event-Eigenschaft `brand_name` hinzufügen.

**Beispiel für das Triggern basierend auf Kauf-Event-Eigenschaften:**

![Einstellungen für aktionsbasierte Zustellung, um eine Campaign an Nutzer:innen zu senden, die Kopfhörer mit einem Markennamen gleich HeadphoneMart kaufen]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

Weitere Informationen finden Sie unter [Kauf-Eigenschaften-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object#purchase-properties-object).

### Event-Eigenschafts-Segmentierung {#event-property-segmentation}

Die Event-Eigenschafts-Segmentierung ermöglicht es Ihnen, Nutzer:innen nicht nur basierend auf durchgeführten angepassten Events zu targeten, sondern auch basierend auf den mit diesen Events verknüpften Eigenschaften. Dies fügt zusätzliche Filteroptionen bei der Segmentierung von Kauf- und angepassten Events hinzu.

![Segmentierungsfilter für Kauf-Event-Eigenschaften, die Optionen zum Filtern von Nutzer:innen basierend auf bestimmten Kauf-Event-Eigenschaftswerten anzeigen, z. B. das Filtern nach Nutzer:innen, die ein Produkt mit einer bestimmten Eigenschaft innerhalb eines festgelegten Zeitraums gekauft haben.]({% image_buster /assets/img/purchase_event_property.png %}){: style="max-width:80%;margin-left:15px;"}

Diese Segmentierungsfilter umfassen:
- Hat das angepasste Event mit Eigenschaft Y mit Wert V X-mal in den letzten Y Tagen durchgeführt
- Hat Käufe mit Eigenschaft Y mit Wert V X-mal in den letzten Y Tagen getätigt
- Fügt eine 1-30-Tage-Segmentierung für alle Käufe, Events und Eigenschaften innerhalb von Käufen und Events hinzu

Im Gegensatz zu [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension) werden die verwendeten Segmente in Realtime aktualisiert, unterstützen eine unbegrenzte Anzahl von Segmenten, bieten einen Rückblickzeitraum von maximal 30 Tagen und verbrauchen Datenpunkte. Aufgrund der zusätzlichen Datenpunktkosten müssen Sie Ihren Braze-Customer-Success-Manager kontaktieren, um Event-Eigenschaften für Ihre angepassten Events aktivieren zu lassen.

Nach der Genehmigung können zusätzliche Eigenschaften im Dashboard unter **Dateneinstellungen** > **Angepasste Events** hinzugefügt werden, indem Sie **Eigenschaften verwalten** auswählen. Sie können diese Event-Eigenschaften dann im Zielgruppen-Schritt des Campaign- oder Canvas-Builders verwenden.

{% include data_activation/segmentable_purchase_properties_keys_note.md %}

### Canvas-Entry-Eigenschaften und Event-Eigenschaften {#canvas-entry-properties-and-event-properties}

{% multi_lang_include canvas/entry_event_properties.md %}

### Käufe auf Bestellebene protokollieren {#log-purchases-at-the-order-level}

Um Käufe auf Bestellebene statt auf Produktebene zu protokollieren, verwenden Sie den Bestellnamen oder die Bestellkategorie als `product_id`. Weitere Informationen finden Sie in unserer [Kauf-Objekt-Spezifikation]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions).

### Namenskonventionen für Produkt-IDs {#product-id-naming-conventions}

Bei Braze bieten wir einige allgemeine Namenskonventionen für die `product_id` des Kauf-Objekts an. Bei der Wahl der `product_id` empfiehlt Braze die Verwendung einfacher Namen wie Produktname oder Produktkategorie (anstelle von SKUs), mit dem Ziel, alle protokollierten Artikel nach dieser `product_id` zu gruppieren.

Dies macht Produkte für Segmentierung und Triggering leicht identifizierbar.

## Kauf-Events auf die Blocklist setzen {#blocklist-purchase-events}

Es kann vorkommen, dass Sie Kauf-Events identifizieren, die entweder zu viele Datenpunkte protokollieren, für Ihre Marketingstrategie nicht mehr nützlich sind oder versehentlich erfasst wurden. Um zu verhindern, dass diese Daten an Braze gesendet werden, können Sie das angepasste Datenobjekt auf die Blocklist setzen, während Ihr Entwicklerteam daran arbeitet, es aus dem Backend Ihrer App oder Website zu entfernen.

Im Braze-Dashboard können Sie die Blocklist unter **Dateneinstellungen** > **Produkte** verwalten. Weitere Informationen finden Sie unter [Angepasste Daten verwalten]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data).