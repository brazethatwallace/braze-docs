---
nav_title: Nachrichtenengagement-Events
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Dieses Glossar listet die verschiedenen Nachrichtenengagement-Events auf, die Braze mit Currents tracken und an ausgewählte Data Warehouses senden kann."
tool: Currents
search_rank: 6
---

Speicherschemata gelten für die Flat-File-Eventdaten, die wir an Data-Warehouse-Speicherpartner (Google Cloud Storage, Amazon S3 und Microsoft Azure Blob Storage) senden. Für Schemata, die für andere Partner gelten, lesen Sie unsere Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) und besuchen Sie die jeweiligen Seiten.

{% alert tip %}
Diese Events sind auch als SQL-Tabellen im [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/), in [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/) und in der [Snowflake-Datenfreigabe]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) verfügbar. Für SQL-Tabellenschemata und Spaltendetails lesen Sie die [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/).
{% endalert %}

Kontaktieren Sie Ihren Account Manager oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/), wenn Sie Zugang zu zusätzlichen Event-Berechtigungen benötigen. Wenn Sie in diesem Artikel nicht finden, was Sie suchen, sehen Sie sich unsere [Bibliothek für Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) oder unsere [Currents-Beispieldaten](https://github.com/Appboy/currents-examples/tree/master/sample-data) an.

{% details Erläuterung der Struktur von Nachrichtenengagement-Events und Plattformwerte %}

### Event-Struktur

Diese Aufschlüsselung zeigt, welche Art von Informationen in der Regel in einem Nachrichtenengagement-Event enthalten sind. Mit einem soliden Verständnis der Komponenten können Ihre Entwickler:innen und Ihr Business-Intelligence-Strategie-Team die eingehenden Currents-Eventdaten nutzen, um datengestützte Berichte und Charts zu erstellen und weitere wertvolle Metriken auszuwerten.

![Aufschlüsselung eines Nachrichtenengagement-Events, das ein E-Mail-Abmelde-Event mit den aufgeführten Eigenschaften zeigt, gruppiert nach nutzerspezifischen Eigenschaften, Kampagnen- oder Canvas-Tracking-Eigenschaften und eventspezifischen Eigenschaften]({% image_buster /assets/img/message_engagement_event.png %})

Nachrichtenengagement-Events bestehen aus **nutzerspezifischen** Eigenschaften, **Kampagnen-/Canvas-Tracking**-Eigenschaften und **eventspezifischen** Eigenschaften.

### Nutzer-ID-Schema

Beachten Sie die Namenskonventionen für Nutzer-IDs.

| Braze-Schema | Currents-Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Der eindeutige Bezeichner, der automatisch von Braze zugewiesen wird. |
| `external_id` | `"EXTERNAL_USER_ID"` | Der eindeutige Bezeichner eines Nutzerprofils, der von der Kundschaft festgelegt wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Plattformwerte

Bestimmte Events geben einen `platform`-Wert zurück, der die Plattform des Nutzergeräts angibt.
<br>Die folgende Tabelle zeigt die möglichen Rückgabewerte:

| Nutzergerät | Plattformwert |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
Currents verwirft Events mit übermäßig großen Nutzdaten von mehr als 900&nbsp;KB.
{% endalert %}

{% alert note %}
Objekte, die sich auf Canvas Flow beziehen, haben IDs, die zur Gruppierung verwendet und über den [Endpunkt „Canvas-Details exportieren"]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) in menschenlesbare Namen übersetzt werden können.
{% endalert %}

{% alert note %}
Bei bestimmten Feldern kann es länger dauern, bis der neueste Stand angezeigt wird, nachdem eine Kampagne oder ein Canvas aktualisiert wurde. Diese Felder sind:
<ul>
  <li>"campaign_name"</li>
  <li>"canvas_name"</li>
  <li>"canvas_step_name"</li>
  <li>"conversion_behavior"</li>
  <li>"canvas_variation_name"</li>
  <li>"experiment_split_name"</li>
  <li>"message_variation_name"</li>
</ul>
Wenn vollständige Konsistenz erforderlich ist, empfehlen wir, nach dem letzten Update dieser Felder eine Stunde zu warten, bevor Sie Ihre Nachrichten an Ihre Nutzer:innen versenden.
{% endalert %}