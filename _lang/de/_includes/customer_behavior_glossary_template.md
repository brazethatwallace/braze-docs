---
nav_title: Kundenverhalten und Nutzer-Events
article_title: Kundenverhalten und Nutzer-Events
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "In diesem Glossar finden Sie eine Auflistung der verschiedenen Kundenverhaltens- und Nutzer-Events, die Braze mit Currents verfolgen und an ausgewählte Data Warehouses senden kann."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% details Schemabereich und zugehörige Ressourcen %}

Speicherschemata gelten für die Flat-File-Event-Daten, die wir an Data-Warehouse-Speicherpartner (Google Cloud Storage, Amazon S3 und Microsoft Azure Blob Storage) senden. Einige der hier aufgeführten Event- und Zielkombinationen sind noch nicht allgemein verfügbar. Informationen darüber, welche Events von verschiedenen Partnern unterstützt werden, finden Sie in unserer Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) und auf den jeweiligen Seiten.

{% alert tip %}
Diese Events sind auch als SQL-Tabellen im [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/), in [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/) und in der [Snowflake-Datenfreigabe]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) verfügbar. Informationen zu SQL-Tabellenschemata und Spaltendetails finden Sie in der [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/).
{% endalert %}

Kontaktieren Sie Ihre Braze-Vertretung oder öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/), wenn Sie Zugang zu zusätzlichen Event-Berechtigungen benötigen. Wenn Sie auf dieser Seite nicht finden, was Sie suchen, sehen Sie sich unsere [Bibliothek der Message-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) oder unsere [Currents-Beispieldaten](https://github.com/Appboy/currents-examples/tree/master/sample-data) an.

{% enddetails %}

{% details Erläuterung der Struktur von Kundenverhaltens- und Nutzer-Events sowie Plattformwerte %}

### Event-Struktur {#event-structure}

Diese Aufschlüsselung von Kundenverhalten und Nutzer-Events zeigt, welche Art von Informationen in der Regel in einem Kundenverhaltens- oder Nutzer-Event enthalten sind. Mit einem soliden Verständnis der Komponenten können Ihre Entwickler:innen und Ihr Business-Intelligence-Strategie-Team die eingehenden Currents-Event-Daten nutzen, um datengestützte Berichte und Charts zu erstellen und weitere wertvolle Metriken auszuwerten.

![Aufschlüsselung eines Nutzer-Events, das ein Kauf-Event mit den aufgeführten Eigenschaften zeigt, gruppiert nach nutzerspezifischen Eigenschaften, verhaltensspezifischen Eigenschaften und gerätespezifischen Eigenschaften]({% image_buster /assets/img/customer_engagement_event.png %})

Kundenverhaltens- und Nutzer-Events setzen sich aus **nutzerspezifischen** Eigenschaften, **verhaltensspezifischen** Eigenschaften und **gerätespezifischen** Eigenschaften zusammen.

### Plattformwerte {#platform-values}

Bestimmte Events geben einen `platform`-Wert zurück, der die Plattform des Nutzergeräts angibt.
<br>In der folgenden Tabelle finden Sie die möglichen Rückgabewerte:

| Nutzergerät | Plattformwert |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plattformwerte" }

{% enddetails %}

{% details Hinweise zu Kundenverhaltens- und Nutzer-Events %}

- Currents verwirft Events mit übermäßig großen Payloads von mehr als 900&nbsp;KB.
- Viele der Events in diesem Glossar werden vom SDK initiiert. Einige Events, wie z. B. `token_state_change`, können entweder vom SDK oder vom Backend initiiert werden (beispielsweise als Reaktion auf einen Push-Bounce). Die Felder `sdk_version`, `gender`, `language` und `country` werden nur bei SDK-initiierten Events gesetzt; bei Backend-initiierten Events oder wenn diese Informationen nicht verfügbar oder für die Nutzer:in nicht hinterlegt sind, können diese Felder `null` sein.

{% enddetails %}

</div>

<!--overview-end-->