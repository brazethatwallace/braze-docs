---
# This file is a template consumed by the external `braze-currents-generate-docs` tool
# (braze-agent-plugins / braze-currents plugin) to generate the Currents event glossary
# docs. It is not referenced from within braze-docs, so do not delete it as "unused".
nav_title: Kundenverhalten und Nutzer:innen-Events
article_title: Kundenverhalten und Nutzer:innen-Events
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Dieses Glossar listet die verschiedenen Kundenverhalten- und Nutzer:innen-Events auf, die Braze verfolgen und über Currents an ausgewählte Data Warehouses senden kann."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% details Schemabereich und zugehörige Ressourcen %}

Speicherschemata gelten für die Flat-File-Event-Daten, die wir an Data-Warehouse-Speicherpartner senden (Google Cloud Storage, Amazon S3 und Microsoft Azure Blob Storage). Einige der hier aufgeführten Event- und Zielkombinationen sind noch nicht allgemein verfügbar. Informationen darüber, welche Events von den verschiedenen Partnern unterstützt werden, finden Sie in unserer Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) und auf den jeweiligen Seiten.

{% alert tip %}
Diese Events sind auch als SQL-Tabellen im [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder), in [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) und im [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) verfügbar. Informationen zu SQL-Tabellenschemata und Spaltendetails finden Sie in der [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).
{% endalert %}

Wenden Sie sich an Ihre Braze-Vertretung oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support), wenn Sie Zugang zu zusätzlichen Event-Berechtigungen benötigen. Falls Sie auf dieser Seite nicht finden, was Sie suchen, sehen Sie sich unsere [Bibliothek der Message-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) oder unsere [Currents-Beispieldaten](https://github.com/Appboy/currents-examples/tree/master/sample-data) an.

{% enddetails %}

{% details Erläuterung der Struktur und Plattformwerte von Kundenverhalten- und Nutzer:innen-Events %}

## Event-Struktur {#event-structure}

Diese Aufschlüsselung der Kundenverhalten- und Nutzer:innen-Events zeigt, welche Art von Informationen in der Regel in einem Kundenverhalten- oder Nutzer:innen-Event enthalten sind. Mit einem soliden Verständnis der Komponenten können Ihre Entwickler:innen und Ihr Business-Intelligence-Strategie-Team die eingehenden Currents-Event-Daten nutzen, um datengestützte Berichte und Charts zu erstellen und andere wertvolle Datenmetriken auszuwerten.

![Aufschlüsselung eines Nutzer:innen-Events mit einem Kauf-Event und den aufgelisteten Eigenschaften, gruppiert nach nutzerspezifischen, verhaltensspezifischen und gerätespezifischen Eigenschaften]({% image_buster /assets/img/customer_engagement_event.png %})

Kundenverhalten- und Nutzer:innen-Events bestehen aus **nutzerspezifischen** Eigenschaften, **verhaltensspezifischen** Eigenschaften und **gerätespezifischen** Eigenschaften.

### Plattformwerte {#platform-values}

Bestimmte Events geben einen `platform`-Wert zurück, der die Plattform des Geräts der Nutzer:innen angibt.
<br>Die folgende Tabelle zeigt die möglichen zurückgegebenen Werte:

| Gerät der Nutzer:innen | Plattformwert |
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

{% details Hinweise zu Kundenverhalten- und Nutzer:innen-Events %}

- Currents verwirft Events mit übermäßig großen Payloads von mehr als 900&nbsp;KB.
- Viele der Events in diesem Glossar werden vom SDK initiiert. Einige Events, wie z. B. `token_state_change`, können entweder vom SDK oder vom Backend initiiert werden (zum Beispiel als Reaktion auf einen Push-Bounce). Die Felder `sdk_version`, `gender`, `language` und `country` werden nur für SDK-initiierte Events gesetzt; bei Backend-initiierten Events oder wenn diese Informationen nicht verfügbar oder für die Nutzer:innen nicht gesetzt sind, können diese Felder `null` sein.

{% enddetails %}

</div>

<!--overview-end-->