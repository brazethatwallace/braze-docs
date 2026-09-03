---
nav_title: Nutzerprofile
layout: user_profiles_event_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Dieses Glossar listet die Nutzerprofil-Aktualisierungen auf, die Braze verfolgen und über Currents an ausgewählte Data Warehouses senden kann."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% alert tip %}
Diese Events sind auch als SQL-Tabellen im [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder), in [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) und im [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) verfügbar. SQL-Tabellenschemata und Spaltendetails finden Sie in der [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). Snowflake-Data-Sharing-Schemata für Nutzerprofil-Attributansichten finden Sie unter [Nutzerprofilattribute]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes).
{% endalert %}

Wenden Sie sich an Ihre Braze-Vertretung oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support), wenn Sie Zugang zu zusätzlichen Event-Berechtigungen benötigen. Falls Sie auf dieser Seite nicht finden, was Sie suchen, sehen Sie sich die [Kundenverhalten-Event-Bibliothek]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), die [Nachrichten-Engagement-Event-Bibliothek]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) oder die [Currents-Beispieldaten](https://github.com/Appboy/currents-examples/tree/master/sample-data) an.

{% details Erläuterung der Struktur von Nutzerprofil-Aktualisierungs-Events %}

### Event-Struktur {#event-structure}

Diese Aufschlüsselung von Kundenverhalten- und Nutzer:innen-Events zeigt, welche Art von Informationen in der Regel in einem Nutzerprofil-Aktualisierungs-Event enthalten sind. Mit einem soliden Verständnis der Komponenten können Ihre Entwickler:innen und Ihr Business-Intelligence-Strategie-Team die eingehenden Currents-Event-Daten nutzen, um datengestützte Berichte und Charts zu erstellen und weitere wertvolle Metriken auszuwerten.

{% alert important %}
Speicherschemata gelten für Flat-File-Event-Daten, die an Data-Warehouse-Speicherpartner wie Google Cloud Storage, Amazon S3 und Microsoft Azure Blob Storage gesendet werden. Einige der hier aufgeführten Event- und Zielkombinationen sind noch nicht allgemein verfügbar. Informationen zu unterstützten Events nach Partner finden Sie unter [Verfügbare Partner]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) und auf den zugehörigen Partnerseiten.

Currents verwirft Events mit Payloads, die größer als 900 KB sind.
{% endalert %}

{% enddetails %}

</div>

<!--overview-end-->