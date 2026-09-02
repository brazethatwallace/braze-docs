---
nav_title: Rate-Limits
article_title: Rate-Limits
page_order: 4.5
description: "Dieser Referenzartikel behandelt die API Rate-Limits für die Braze API-Infrastruktur."
page_type: reference
---

# Rate-Limits

> Die API-Infrastruktur von Braze ist darauf ausgelegt, große Datenmengen für unsere Kund:innen zu verarbeiten. Zu diesem Zweck setzen wir API Rate-Limits pro Workspace durch.

Ein Rate-Limit ist die Anzahl der Anfragen, die die API in einem bestimmten Zeitraum empfangen kann. Viele lastbasierte Denial-of-Service-Vorfälle in großen Systemen sind unbeabsichtigt – sie werden durch Fehler in Software oder Konfigurationen verursacht und nicht durch böswillige Angriffe. Rate-Limits stellen sicher, dass unseren Kund:innen durch solche Fehler keine Braze API-Ressourcen vorenthalten werden. Wenn in einem bestimmten Zeitrahmen zu viele Anfragen gesendet werden, erhalten Sie möglicherweise Fehlerantworten mit dem Statuscode `429`, der anzeigt, dass das Rate-Limit erreicht wurde.

{% alert warning %}
API Rate-Limits können sich je nach ordnungsgemäßer Nutzung unseres Systems ändern. Wir empfehlen vernünftige Grenzen bei API-Aufrufen, um Schäden oder Missbrauch zu vermeiden.
{% endalert %}

## Rate-Limits nach Anfragetyp {#rate-limits-by-request-type}

In der folgenden Übersicht finden Sie die standardmäßigen API-Rate-Limits für verschiedene Anfragetypen. Diese Standardlimits können auf Anfrage erhöht werden. Wenden Sie sich für weitere Informationen an Ihren Customer-Success-Manager.

### Anfragen mit unterschiedlichen Rate-Limits {#requests-with-different-rate-limits}

| Anfragetyp | Standard-API-Rate-Limit |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | **Anfragen:** Die Rate-Limits variieren je nach Vertrag. Für Kund:innen, deren Preismodell Datenpunkte umfasst, wendet Braze ein Burst-Limit von 3.000 Anfragen pro drei Sekunden an. Für alle anderen Kund:innen werden die Limits gemäß Ihren Vertragsbedingungen konfiguriert. Kontaktieren Sie den Braze-Support oder Ihren Customer-Success-Manager bei Fragen zu Ihren Limits.<br><br>**Batching:** Bis zu 75 Objekte insgesamt, kombiniert aus `attributes`, `events` und `purchases`, pro API-Anfrage. Kund:innen mit Legacy-Rate-Limits können bis zu 75 Objekte pro Array unabhängig voneinander einschließen. Weitere Informationen finden Sie unter [Batching von User-Track-Anfragen](#batch-user-track).<br><br>**Limits für Monthly Active Users CY 24-25, Universal MAU, Web MAU und Mobile MAU:** Siehe [Limits für Monthly Active Users CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau). |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | **Bei Onboarding am oder nach dem 22. August 2024:** 250 Anfragen pro Minute. <br><br> **Bei Onboarding vor dem 22. August 2024:** 2.500 Anfragen pro Minute. |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)<br>[`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias)<br>[`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update)<br>[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)<br>[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) | 20.000 Anfragen pro Minute, geteilt zwischen den Endpunkten. |
| [`/users/external_id/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename) | 1.000 Anfragen pro Minute. |
| [`/users/external_id/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) | 1.000 Anfragen pro Minute. |
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | 1.000 Anfragen pro Stunde, geteilt mit dem `/purchases/product_list`-Endpunkt. |
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | 1.000 Anfragen pro Stunde, geteilt mit dem `/events/list`-Endpunkt. |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | 50.000 Anfragen pro Minute. |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)<br>[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)<br>[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)<br>[`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)<br>[`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) | Für Broadcast-Aufrufe (bei breit angelegtem Targeting von Segmenten, Filtern oder einer Connected Audience) gelten 250 Anfragen pro Minute über alle Zielgruppen hinweg und 10 Anfragen pro Minute pro [eindeutige Zielgruppe]({{site.baseurl}}/api/api_limits#what-counts-as-the-same-unique-audience) (es gilt das zuerst erreichte Limit).<br><br>Andernfalls, wenn einzelne Empfänger:innen angesprochen werden, wird die Anfrage in das [gemeinsame Rate-Limit]({{site.baseurl}}/api/api_limits#requests-with-shared-rate-limits) von 250.000 Anfragen pro Stunde einbezogen. |
| [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids) | 100 Anfragen pro Tag. |
| [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) | 5.000 Anfragen pro Minute. |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center)<br>[`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | 1.000 Anfragen pro Minute. |
| [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center) | 10 Anfragen pro Minute. |
| [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | 50 Anfragen pro Minute, geteilt zwischen den Endpunkten. |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | 16.000 Anfragen pro Minute, geteilt zwischen den Endpunkten. |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item) | 50 Anfragen pro Minute, geteilt zwischen den Endpunkten. |
| [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)<br>[`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)<br>[`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)<br>[`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | 50 Anfragen pro Minute, geteilt zwischen den Endpunkten. |
| [`/scim/v2/Users/{id}`]({{site.baseurl}}/get_see_user_account_information)<br>[`/scim/v2/Users?filter={userName@example.com}`]({{site.baseurl}}/get_search_existing_dashboard_user_email)<br>[`/scim/v2/Users/{id}`]({{site.baseurl}}/post_update_existing_user_account)<br>[`/scim/v2/Users/{id}}`]({{site.baseurl}}/delete_existing_dashboard_user)<br>[`/scim/v2/Users/`]({{site.baseurl}}/post_create_user_account) | 5.000 Anfragen pro Tag, pro Unternehmen, geteilt zwischen den Endpunkten. |
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | 50 Anfragen pro Minute. |
| [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | 20 Anfragen pro Minute. |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) | 100 Anfragen pro Minute. |
| [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | 100 Anfragen pro Stunde. |
| [`/media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file) | 100 Anfragen pro Stunde. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anfragen mit unterschiedlichen Rate-Limits" }

### Anfragen mit gemeinsamen Rate-Limits {#requests-with-shared-rate-limits}

Für die folgenden Anfragen gilt ein gemeinsames Rate-Limit von 250.000 Anfragen pro Stunde.

- [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key)
- [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys)
- [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) (nur für Nicht-Broadcast-Aufrufe – solche, die `external_user_ids` oder `aliases` angeben)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) (nur für Nicht-Broadcast-Aufrufe)
- [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages)
- [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns)
- [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)
- [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary)
- [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details)
- [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) (nur für Nicht-Broadcast-Aufrufe)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) (nur für Nicht-Broadcast-Aufrufe)
- [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases)
- [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases)
- [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)
- [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information)
- [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks)
- [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)
- [`/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist)
- [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist)
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)
- [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)
- [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses)
- [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics)
- [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date)
- [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days)
- [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date)
- [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)
- [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) (nur für Nicht-Broadcast-Aufrufe)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)
- [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages)
- [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages)
- [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled)
- [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics)
- [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details)
- [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment)
- [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics)
- [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics)
- [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers)
- [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers)
- [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)
- [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups)
- [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)
- [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information)
- [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates)
- [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group)
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

### Was zählt als dieselbe eindeutige Zielgruppe? {#what-counts-as-the-same-unique-audience}

Dies gilt für die folgenden Endpunkte: [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages), [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns), [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases), [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) und [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases).

Bei diesen Endpunkten gelten Broadcast-Anfragen als an dieselbe eindeutige Zielgruppe gerichtet, wenn alle folgenden Kriterien übereinstimmen:

- Die getriggerte Campaign oder das Canvas (die `campaign_id` oder `canvas_id` in Ihrer API-Anfrage, falls angegeben)
- Die angesprochene Zielgruppe (die Segmente oder Filter, oder bei API-Campaigns die `segment_id` in Ihrer API-Anfrage)
- Die Connected-Audience-Filter (das `audience`-Objekt in Ihrer API-Anfrage, falls angegeben)

Jede eindeutige Kombination dieser Attribute zählt als separate Zielgruppe, sodass das zusätzliche Rate-Limit pro eindeutiger Zielgruppe für jede Kombination unabhängig gilt.

## API-Anfragen bündeln {#batching-api-requests}

Braze-APIs unterstützen das Bündeln (Batching) von Anfragen. Durch das Bündeln kann Braze so viele Daten wie möglich in einem einzigen API-Aufruf verarbeiten, sodass Sie nicht viele einzelne API-Aufrufe durchführen müssen. Es ist für Braze effizienter, Daten in Stapeln zu verarbeiten als einen Aufruf nach dem anderen. Zum Beispiel erfordert die Verarbeitung von 1.000 gebündelten API-Aufrufen weniger Ressourcen als die Verarbeitung von 75.000 einzelnen Aufrufen. Das Bündeln ist äußerst wichtig für jede Anwendung, die möglicherweise mehr als 75.000 Aufrufe pro Stunde benötigt.

{% alert note %}
Erhöhungen des REST-API-Rate-Limits werden bedarfsabhängig für Kund:innen geprüft, die die API-Batching-Funktionen nutzen.
{% endalert %}

### Anfragen für den Endpunkt „Nutzer:innen erstellen und aktualisieren“ bündeln {#batch-user-track}

Jede `/users/track`-Anfrage kann insgesamt bis zu 75 Objekte enthalten, die über `attributes`, `events` und `purchases` verteilt sind. Jedes Objekt kann eine:n Nutzer:in aktualisieren. Ein einzelnes Nutzerprofil kann durch mehrere Objekte aktualisiert werden.

{% details Ältere Rate-Limits %}
Für Kund:innen mit älteren Rate-Limits kann jedes Array (`attributes`, `events` und `purchases`) unabhängig bis zu 75 Objekte enthalten, was ein kombiniertes Maximum von bis zu 225 Objekten pro Anfrage ergibt.
{% enddetails %}

Weitere Informationen zu den Rate-Limits für `/users/track` finden Sie unter [POST: Nutzer:innen erstellen und aktualisieren]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

Anfragen an diesen Endpunkt werden in der Regel in folgender Reihenfolge verarbeitet:

1. Attribute
2. Events
3. Purchases

### Messaging-Endpunkt-Anfragen bündeln {#batching-messaging-endpoint-requests}

Eine einzelne Anfrage an die [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) kann Folgendes erreichen:

- Bis zu 50 spezifische `external_ids`, jeweils mit individuellen Nachrichtenparametern
- Ein Segment beliebiger Größe, das im Braze-Dashboard erstellt wurde und durch seine `segment_id` angegeben wird
- Nutzer:innen, die zusätzlichen Zielgruppenfiltern beliebiger Größe entsprechen, die in der Anfrage als [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience)-Objekt definiert sind

### Beispiel für eine gebündelte Anfrage {#example-batch-request}

Das folgende Beispiel verwendet `external_id`, um einen einzelnen API-Aufruf für E-Mail und SMS durchzuführen.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@example.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@example.com"]
    }
  ]
}
```

## Überwachung Ihrer Rate-Limits {#monitoring-your-rate-limits}

Jede einzelne an Braze gesendete API-Anfrage gibt die folgenden Informationen in den Antwort-Headern zurück:

| Header-Name             | Beschreibung                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | Die maximale Anzahl von Anfragen, die Sie in einem bestimmten Intervall stellen können (Ihr Rate-Limit). |
| `X-RateLimit-Remaining` | Die Anzahl der verbleibenden Anfragen im aktuellen Rate-Limit-Fenster.                          |
| `X-RateLimit-Reset`     | Der Zeitpunkt, zu dem das aktuelle Rate-Limit-Fenster zurückgesetzt wird, in UTC-Epoch-Sekunden.                |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Überwachung Ihrer Rate-Limits" }

Diese Informationen sind absichtlich im Header der Antwort auf die API-Anfrage enthalten und nicht im Braze-Dashboard. Dadurch kann Ihr System in Echtzeit besser reagieren, während Sie mit unserer API interagieren. Wenn beispielsweise der Wert von `X-RateLimit-Remaining` unter einen bestimmten Schwellenwert fällt, möchten Sie möglicherweise den Versand verlangsamen, um sicherzustellen, dass alle Transaktions-E-Mails zugestellt werden. Oder wenn der Wert Null erreicht, möchten Sie möglicherweise den gesamten Versand pausieren, bis die in `X-RateLimit-Reset` angegebene Zeit abgelaufen ist.

{% alert note %}
HTTP-Header werden ausschließlich in Kleinbuchstaben zurückgegeben. Dieses Verhalten entspricht dem HTTP/2-Protokoll, das vorschreibt, dass alle Header-Feldnamen in Kleinbuchstaben geschrieben sein müssen. Dies unterscheidet sich von HTTP/1.X, wo Header-Namen nicht zwischen Groß- und Kleinschreibung unterschieden, aber häufig in verschiedenen Schreibweisen verwendet wurden.
{% endalert %}

Wenn Sie Fragen zu API-Limits haben, wenden Sie sich an Ihren Customer-Success-Manager oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support).

{% alert tip %}
Sie können das [API-Nutzungs-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/api_usage) verwenden, um eingehenden Datenverkehr anzuzeigen und mit Ihren Rate-Limits zu vergleichen.
{% endalert %}

### Optimale Verzögerung zwischen Endpunkten {#optimal-delay-between-endpoints}

{% alert note %}
Wir empfehlen, eine Verzögerung von 5 Minuten zwischen aufeinanderfolgenden Endpunkt-Aufrufen einzuplanen, um Fehler zu minimieren.
{% endalert %}

Das Verständnis der optimalen Verzögerung zwischen Endpunkten ist entscheidend, wenn Sie aufeinanderfolgende Aufrufe an die Braze-API durchführen. Probleme entstehen, wenn Endpunkte von der erfolgreichen Verarbeitung anderer Endpunkte abhängen und bei zu frühem Aufruf Fehler auftreten könnten. Wenn Sie beispielsweise Nutzer:innen über unseren Endpunkt `/user/alias/new` einen Alias zuweisen und dann diesen Alias verwenden, um über unseren Endpunkt `/users/track` ein angepasstes Event zu senden – wie lange sollten Sie warten?

Unter normalen Bedingungen beträgt die Zeit für die Eventual Consistency unserer Daten 10–100 ms (1/10 Sekunde). Es kann jedoch Fälle geben, in denen diese Konsistenz länger dauert. Daher empfehlen wir, eine Verzögerung von 5 Minuten zwischen aufeinanderfolgenden Aufrufen einzuplanen, um die Fehlerwahrscheinlichkeit zu minimieren.

## Begrenzungen der Payload-Größe {#payload-size-limits}

Braze-API-Anfragen unterliegen Begrenzungen der Payload-Größe, die von den Rate-Limits getrennt sind. Die meisten Endpunkte akzeptieren Anfragekörper mit bis zu 4&nbsp;MB. Wenn eine Anfrage das geltende Limit überschreitet, kann Braze sie mit HTTP `413 Request Entity Too Large` oder HTTP `400 Bad Request` ablehnen, je nach Endpunkt.

Der Endpunkt [`/users/track/bulk`]({{site.baseurl}}/api/endpoints/user_data/post_user_track_bulk) hat ein Payload-Limit von 2&nbsp;MB und gibt HTTP `400` zurück, wenn der Anfragekörper dieses Limit überschreitet. Informationen zu endpunktspezifischen Limits und zur Fehlerbehandlung finden Sie unter [Nutzerdaten-Endpunkte]({{site.baseurl}}/api/endpoints/user_data).

### Zurücksetzen der Rate-Limits {#rate-limit-reset}

Rate-Limits werden zur vollen Stunde zurückgesetzt, nicht auf Basis eines gleitenden Zeitfensters. Wenn das Limit beispielsweise bei 250.000 Anfragen pro Stunde liegt, könnten Sie 50.000 Anfragen zwischen 22:00 und 22:59 Uhr und weitere 250.000 Anfragen zwischen 23:00 und 23:59 Uhr senden, da der Zähler zu Beginn jeder vollen Stunde zurückgesetzt wird.