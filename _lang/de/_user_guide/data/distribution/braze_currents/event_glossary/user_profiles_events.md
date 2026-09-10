---
nav_title: Nutzerprofile
layout: user_profiles_event_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Dieses Glossar listet die Nutzerprofil-Updates auf, die Braze verfolgen und über Currents an ausgewählte Data Warehouses senden kann."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% alert tip %}
Diese Events sind auch als SQL-Tabellen im [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder), in [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) und in der [Snowflake-Datenfreigabe]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) verfügbar. Informationen zu SQL-Tabellenschemata und Spaltendetails finden Sie in der [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). Informationen zu Snowflake-Datenfreigabe-Schemata für Nutzerprofil-Attribut-Views finden Sie unter [Nutzerprofilattribute]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes).
{% endalert %}

Wenden Sie sich an Ihre Braze-Vertretung oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support), wenn Sie Zugang zu zusätzlichen Event-Berechtigungen benötigen. Falls Sie auf dieser Seite nicht finden, was Sie suchen, sehen Sie sich die [Kundenverhalten-Events-Bibliothek]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), die [Nachrichten-Engagement-Events-Bibliothek]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) oder die [Currents-Beispieldaten](https://github.com/Appboy/currents-examples/tree/master/sample-data) an.

{% details Erläuterung der Struktur von Nutzerprofil-Update-Events %}

### Event-Struktur {#event-structure}

Diese Aufschlüsselung von Kundenverhalten- und Nutzer-Events zeigt, welche Art von Informationen in der Regel in einem Nutzerprofil-Update-Event enthalten sind. Mit einem soliden Verständnis der Komponenten können Ihre Entwickler:innen und Ihr Business-Intelligence-Strategie-Team die eingehenden Currents-Event-Daten nutzen, um datengestützte Berichte und Charts zu erstellen und weitere wertvolle Datenmetriken auszuwerten.

{% alert important %}
Speicherschemata gelten für Flat-File-Event-Daten, die an Data-Warehouse-Speicherpartner wie Google Cloud Storage, Amazon S3 und Microsoft Azure Blob Storage gesendet werden. Einige der hier aufgeführten Event- und Zielkombinationen sind noch nicht allgemein verfügbar. Informationen zu unterstützten Events nach Partner finden Sie unter [Verfügbare Partner]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) und auf den zugehörigen Partnerseiten.

Currents verwirft Events mit Payloads, die größer als 900 KB sind.
{% endalert %}

{% enddetails %}

</div>

<!--overview-end-->


{% api %}
## Events für Nutzerlöschanfragen {#user-delete-request-events}

{% apitags %}
User Delete Request
{% endapitags %}

Wenn ein:e Nutzer:in auf Kundenanfrage gelöscht wird

{% tabs %}
{% tab Cloud Storage %}
```json
// users.UserDeleteRequest

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.UserDeleteRequest

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Events für verwaiste Nutzer:innen {#user-orphan-events}

{% apitags %}
User Orphan
{% endapitags %}

Wenn ein:e Nutzer:in verwaist, d. h. das Nutzerprofil mit dem Profil eines/einer anderen Nutzer:in zusammengeführt wird

{% tabs %}
{% tab Cloud Storage %}
```json
// users.UserOrphan

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "orphaned_by_id" : "(required, string) BSON ID of the user whose profile was merged with the orphaned user's profile",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.UserOrphan

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "orphaned_by_id" : "(required, string) BSON ID of the user whose profile was merged with the orphaned user's profile"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "external_user_id" : "(optional, string) [PII] External ID of the user",
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Nutzerprofil-Update-Events {#user-profile-update-events}

{% apitags %}
Profile
{% endapitags %}

Dies stellt die Profil-Updates für ein:e Nutzer:in dar.

{% alert important %}
Das Nutzerprofil-Update-Event befindet sich in der Beta-Phase. Wenden Sie sich an Ihren Customer-Success-Manager oder Account Manager, um Zugang zu erhalten.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.profile.Update

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "archived" : "(optional, boolean) When set to True, indicates that this user was archived within Braze",
  "country" : "(optional, string) [PII] Country of the user",
  "custom_attributes" : "(optional, string) Valid JSON string of the updated custom attributes",
  "dob" : "(optional, string) [PII] Date of birth of the user in ISO-8601 format",
  "email_address" : "(optional, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "first_name" : "(optional, string) [PII] First name of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "home_city" : "(optional, string) [PII] Home city of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "last_name" : "(optional, string) [PII] Last name of the user",
  "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "time_ms" : "(required, long) Time in milliseconds when the update happened",
  "timezone" : "(optional, string) Time zone of the user",
  "update_source" : "(required, string) The source of this update",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Custom HTTP Connector %}
```json
// users.profile.Update

{
  "event_type" : "(required, string) The name of the event type",
  "id" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "archived" : "(optional, boolean) When set to True, indicates that this user was archived within Braze",
    "country" : "(optional, string) [PII] Country of the user",
    "custom_attributes" : "(optional, string) Valid JSON string of the updated custom attributes",
    "dob" : "(optional, string) [PII] Date of birth of the user in ISO-8601 format",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "first_name" : "(optional, string) [PII] First name of the user",
    "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
    "home_city" : "(optional, string) [PII] Home city of the user",
    "language" : "(optional, string) [PII] Language of the user",
    "last_name" : "(optional, string) [PII] Last name of the user",
    "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format",
    "time_ms" : "(required, long) Time in milliseconds when the update happened",
    "update_source" : "(required, string) The source of this update"
  },
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user" : {
    "external_user_id" : "(optional, string) [PII] External ID of the user",
    "timezone" : "(optional, string) Time zone of the user",
    "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
  }
}
```
{% endtab %}

{% tab Shopify %}
```json
// User Profile Update (users.profile.Update)

{
  "variables" : {
    "identifier" : {
      "customId" : {
        "key" : "user_id",
        "namespace" : "braze",
        "value" : "(required, string) [PII] Braze user ID of the user who performed this event"
      }
    },
    "input" : {
      "email" : "(optional, string) [PII] Email address of the user",
      "firstName" : "(optional, string) [PII] First name of the user",
      "lastName" : "(optional, string) [PII] Last name of the user",
      "locale" : "(optional, string) [PII] Language of the user",
      "phone" : "(optional, string) [PII] Phone number of the user in e.164 format"
    }
  }
}
```
{% endtab %}
{% endtabs %}

{% endapi %}