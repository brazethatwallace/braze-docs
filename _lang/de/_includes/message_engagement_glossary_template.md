---
# This file is a template consumed by the external `braze-currents-generate-docs` tool
# (braze-agent-plugins / braze-currents plugin) to generate the Currents event glossary
# docs. It is not referenced from within braze-docs, so do not delete it as "unused".
nav_title: Nachrichten-Engagement-Events
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Dieses Glossar listet die verschiedenen Nachrichten-Engagement-Events auf, die Braze verfolgen und mithilfe von Currents an ausgewählte Data Warehouses senden kann."
tool: Currents
search_rank: 6
lazy_partner_tabs: true
---

<div class="api-glossary-preamble" markdown="1">

{% details Schemabereich und zugehörige Ressourcen %}

Speicherschemata gelten für die Flat-File-Eventdaten, die wir an Data-Warehouse-Speicherpartner senden (Google Cloud Storage, Amazon S3 und Microsoft Azure Blob Storage). Für Schemata, die für andere Partner gelten, lesen Sie unsere Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) und besuchen Sie die jeweiligen Seiten.

{% alert tip %}
Diese Events sind auch als SQL-Tabellen im [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder), in [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) und im [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) verfügbar. Für SQL-Tabellenschemata und Spaltendetails lesen Sie die [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).
{% endalert %}

Wenden Sie sich an Ihren Account Manager:in oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support), wenn Sie Zugriff auf zusätzliche Event-Berechtigungen benötigen. Falls Sie in diesem Artikel nicht finden, was Sie suchen, besuchen Sie unsere [Kundenverhalten-Event-Bibliothek]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) oder unsere [Currents-Beispieldaten](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% enddetails %}

{% details Erläuterung der Struktur und Plattformwerte von Nachrichten-Engagement-Events %}

## Eventstruktur {#event-structure}

Diese Aufschlüsselung zeigt, welche Art von Informationen in der Regel in einem Nachrichten-Engagement-Event enthalten sind. Mit einem soliden Verständnis der Komponenten können Ihre Entwickler:innen und Ihr Business-Intelligence-Strategie-Team die eingehenden Currents-Eventdaten nutzen, um datengestützte Berichte und Charts zu erstellen und weitere wertvolle Datenmetriken auszuwerten.

![Aufschlüsselung eines Nachrichten-Engagement-Events, das ein E-Mail-Abmelde-Event mit den aufgelisteten Eigenschaften zeigt, gruppiert nach nutzerspezifischen Eigenschaften, Campaign- oder Canvas-Tracking-Eigenschaften und eventspezifischen Eigenschaften]({% image_buster /assets/img/message_engagement_event.png %}){: width="2300" height="770" style="max-width:100%;height:auto;"}

Nachrichten-Engagement-Events bestehen aus **nutzerspezifischen** Eigenschaften, **Campaign-/Canvas-Tracking**-Eigenschaften und **eventspezifischen** Eigenschaften.

### Nutzer:innen-ID-Schema {#user-id-schema}

Beachten Sie die Namenskonventionen für Nutzer:innen-IDs.

| Braze-Schema | Currents-Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Der eindeutige Bezeichner, der automatisch von Braze zugewiesen wird. |
| `external_id` | `"EXTERNAL_USER_ID"` | Der eindeutige Bezeichner eines Nutzerprofils, der von der Kund:in festgelegt wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer:innen-ID-Schema" }

### Plattformwerte {#platform-values}

Bestimmte Events geben einen `platform`-Wert zurück, der die Plattform des Geräts der Nutzer:in angibt.
<br>Die folgende Tabelle zeigt die möglichen zurückgegebenen Werte:

| Gerät der Nutzer:in | Plattformwert |
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

{% details Hinweise zu Nachrichten-Engagement-Events %}

- Currents verwirft Events mit Payloads, die größer als 900&nbsp;KB sind.
- Objekte im Zusammenhang mit Canvas Flow haben IDs, die Sie zum Gruppieren verwenden und über den [Endpunkt „Canvas-Details exportieren“]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) in lesbare Namen übersetzen können.
- Bestimmte Felder zeigen möglicherweise nicht sofort ihren aktuellsten Status an, nachdem Sie eine Campaign oder ein Canvas aktualisiert haben:
  - `campaign_name`
  - `canvas_name`
  - `canvas_step_name`
  - `conversion_behavior`
  - `canvas_variation_name`
  - `experiment_split_name`
  - `message_variation_name`
- Wenn Sie vollständige Konsistenz für diese Felder benötigen, warten Sie eine Stunde nach der letzten Aktualisierung, bevor Sie Nachrichten an Ihre Nutzer:innen senden.

{% enddetails %}

</div>

<!--overview-end-->