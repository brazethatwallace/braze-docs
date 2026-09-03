---
page_order: 0
nav_title: Home
article_title: Braze API-Leitfaden
layout: api_glossary
glossary_top_header: "Braze API-Leitfaden"
glossary_top_text: "Braze bietet eine leistungsstarke REST API, mit der Sie Nutzer:innen verfolgen, Nachrichten versenden, Daten exportieren und Campaigns, Canvases, Kataloge und vieles mehr verwalten können. Verwenden Sie dieses Glossar, um Endpunkte nach Typ zu durchsuchen, Referenzartikel für Anfrage- und Antwortdetails zu öffnen und Links zu Authentifizierung, Rate-Limits und Objektdokumentation zu finden."
description: "Durchsuchen Sie die Braze REST API-Endpunkte nach Typ, mit Links zu Authentifizierung, Rate-Limits und Objektreferenz-Dokumentation."
page_type: glossary
glossary_tag_name: Endpunkttyp

glossary_filter_text: "Wählen Sie den Endpunkttyp aus, um das Glossar einzugrenzen:"

glossary_mid_text: "Endpunktsuche"
guide_featured_list:
  - name: API-Übersicht
    image: /assets/img/braze_icons/annotation-info.svg
    link: /docs/api/basics
  - name: API-Bezeichnertypen
    link: /docs/api/identifier_types
    image: /assets/img/braze_icons/clipboard-check.svg
  - name: Objekte und Filter
    link: /docs/api/objects_filters
    image: /assets/img/braze_icons/settings-01.svg
  - name: Fehler und Antworten
    link: /docs/api/errors
    image: /assets/img/braze_icons/list.svg
  - name: Datenaufbewahrung
    link: /docs/api/data_retention
    image: /assets/img/braze_icons/laptop-02.svg
  - name: Rate-Limits
    link: /docs/api/api_limits
    image: /assets/img/braze_icons/hand.svg

# channel to icon/fa or image mapping
glossary_tags:
  - name: Apps
  - name: Campaigns
  - name: Canvas
  - name: Catalogs
  - name: Content Blocks
  - name: Custom Events
  - name: Data Objects
  - name: Email List
  - name: Email Templates
  - name: Webhook Templates
  - name: KPI
  - name: Media Library
  - name: Device Messaging API
  - name: Purchases
  - name: Preference Center
  - name: Schedule Messages
  - name: SCIM
  - name: SDK Authentication
  - name: Segments
  - name: Send Messages
  - name: SMS
  - name: Subscription Groups
  - name: User Data
  - name: Live Activity
  - name: Cloud Data Ingestion

glossaries:
  - name: <a href='/docs/api/endpoints/apps/post_update_push_credential'>/apps/push_credential/update</a>
    description: Die Push-Zugangsdaten für eine einzelne App aktualisieren.
    tags:
      - Apps
  - name: <a href='/docs/api/endpoints/user_data/post_user_alias'>/users/alias/new</a>
    description: Neue Nutzer-Aliase für bestehende identifizierte Nutzer:innen hinzufügen oder neue nicht identifizierte Nutzer:innen erstellen.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_alias_update'>/users/alias/update</a>
    description: Bestehende Nutzer-Alias-Namen auf neue Nutzer-Alias-Namen aktualisieren.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_delete'>/users/delete</a>
    description: Ein beliebiges Nutzerprofil löschen, indem ein bekannter Nutzer-Bezeichner angegeben wird.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_global_control_group'>/users/export/global_control_group</a>
    description: Alle Nutzer:innen innerhalb einer globalen Kontrollgruppe exportieren.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_identifier'>/users/export/ids</a>
    description: Daten aus einem beliebigen Nutzerprofil exportieren, indem ein Nutzer-Bezeichner angegeben wird.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_segment'>/users/export/segment</a>
    description: Alle Nutzer:innen innerhalb eines Segments exportieren.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename'>/users/external_ids/rename</a>
    description: Die externen IDs Ihrer Nutzer:innen umbenennen.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove'>/users/external_ids/remove</a>
    description: Die alten, veralteten externen IDs Ihrer Nutzer:innen entfernen.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_identify'>/users/identify</a>
    description: Nicht identifizierte Nutzer:innen (nur Alias) identifizieren.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_track'>/users/track</a>
    description: Angepasste Events und Käufe erfassen sowie Nutzerprofilattribute aktualisieren.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_merge'>/users/merge</a>
    description: Ein Nutzerprofil mit einem anderen zusammenführen.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/data_objects'>/data_objects/*</a>
    description: Die vollständige Endpunktreferenz für Data Objects anzeigen, einschließlich Objekttypen, Objekten und Beziehungsendpunkten.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/types/get_list_data_object_types'>/data_objects/types</a>
    description: Data-Object-Typen im Workspace auflisten.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/types/get_data_object_type'>/data_objects/types/{type_name}</a>
    description: Einen Data-Object-Typ und seine Schema-Definition abrufen.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/types/get_list_user_relationship_types'>/data_objects/types/{type_name}/user_relationship_types</a>
    description: Nutzer-Beziehungsarten für einen Data-Object-Typ auflisten.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/types/get_list_object_relationship_types'>/data_objects/types/{type_name}/object_relationship_types</a>
    description: Objekt-Beziehungsarten für einen Data-Object-Typ auflisten.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/objects/get_list_data_objects'>/data_objects/objects/{type_name}</a>
    description: Data Objects für einen Typ auflisten.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/objects/get_data_object'>/data_objects/objects/{type_name}/{external_id}</a>
    description: Ein Data Object abrufen oder es ersetzen, aktualisieren und löschen.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/object_relationships/get_list_object_relationships'>/data_objects/objects/{type_name}/{external_id}/object_relationships</a>
    description: Objekt-zu-Objekt-Beziehungen auflisten, erstellen, ersetzen, aktualisieren und löschen.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/user_relationships/get_list_user_relationships'>/data_objects/objects/{type_name}/{external_id}/user_relationships</a>
    description: Nutzer-Beziehungen für ein Data Object auflisten.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/user_relationships/post_create_user_relationship'>/data_objects/objects/{type_name}/{external_id}/users</a>
    description: Nutzer-zu-Objekt-Beziehungen erstellen, ersetzen, aktualisieren und löschen.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns'>/campaigns/trigger/send</a>
    description: Sofortige, einmalige Nachrichten an bestimmte Nutzer:innen über API-getriggerte Zustellung senden.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases'>/canvas/trigger/send</a>
    description: Canvas-Nachrichten über API-getriggerte Zustellung senden.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_messages'>/messages/send</a>
    description: Sofortige, einmalige Nachrichten an bestimmte Nutzer:innen über die Braze-API senden.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids'>/sends/id/create</a>
    description: Sende-IDs erstellen, um Nachrichten zu versenden und die Performance der Nachrichten programmgesteuert zu verfolgen, ohne für jeden Versand eine Campaign erstellen zu müssen.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message'>/transactional/v1/campaigns/{CAMPAIGN_ID}/send</a>
    description: Sofortige, einmalige transaktionsbezogene Nachrichten an bestimmte Nutzer:innen senden.
    tags:
      - Send Messages
  - name: <a href='/docs/api/device_messaging_api/endpoints/banners/post_sync_banners'>/v1/device-messaging/banners/sync</a>
    description: Berechtigte Banner für Nutzer:innen und eine Reihe von Placements abrufen.
    tags:
      - Device Messaging API
  - name: <a href='/docs/api/device_messaging_api/endpoints/banners/post_track_banner_events'>/v1/device-messaging/banners/track</a>
    description: Impression- und Klick-Events für Banner aufzeichnen.
    tags:
      - Device Messaging API
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns'>/campaigns/trigger/schedule/create</a>
    description: Im Dashboard erstellte Campaign-Nachrichten über API-getriggerte Zustellung senden.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages'>/campaigns/trigger/schedule/delete</a>
    description: Zuvor geplante API-getriggerte Campaign-Nachrichten stornieren, bevor sie gesendet wurden.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns'>/campaigns/trigger/schedule/update</a>
    description: Im Dashboard erstellte geplante API-getriggerte Campaigns aktualisieren.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases'>/canvas/trigger/schedule/delete</a>
    description: Eine zuvor über API getriggerte geplante Canvas-Nachricht stornieren, bevor sie gesendet wurde.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases'>/canvas/trigger/schedule/create</a>
    description: Canvas-Nachrichten über API-getriggerte Zustellung planen.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages'>/messages/schedule/update</a>
    description: Geplante Nachrichten aktualisieren. Dieser Endpunkt akzeptiert Updates entweder für den <code>schedule</code>- oder <code>messages</code>-Parameter oder für beide.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages'>/messages/schedule/delete</a>
    description: Eine zuvor geplante Nachricht stornieren, bevor sie gesendet wurde.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages'>/messages/schedule/create</a>
    description: Eine Campaign, ein Canvas oder eine andere Nachricht planen, die zu einem bestimmten Zeitpunkt gesendet werden soll.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases'>/canvas/trigger/schedule/update</a>
    description: Im Dashboard erstellte geplante API-getriggerte Canvases aktualisieren.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled'>/messages/scheduled_broadcasts</a>
    description: Eine JSON-Liste mit Informationen über geplante Campaigns und Entry-Canvases zwischen jetzt und einer in der Anfrage angegebenen <code>end_time</code> zurückgeben.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/live_activity/update'>/messages/live_activity/update</a>
    description: Eine iOS-Live-Aktivität aktualisieren.
    tags:
      - Live Activity
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status'>/subscription/status/set</a>
    description: Den Abo-Status von bis zu 50 Nutzer:innen im Braze-Dashboard per Batch aktualisieren.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2'>/v2/subscription/status/set</a>
    description: Den Abo-Status von bis zu 50 Nutzer:innen im Braze-Dashboard per Batch aktualisieren.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status'>/subscription/status/get</a>
    description: Den Abo-Status von Nutzer:innen in einer Abo-Gruppe abrufen.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups'>/subscription/user/status</a>
    description: Die Abo-Gruppen bestimmter Nutzer:innen auflisten und abrufen.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/email/post_blacklist'>/email/blacklist</a>
    description: Nutzer:innen von E-Mails abmelden und als Hard Bounce markieren.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_remove_hard_bounces'>/email/bounce/remove</a>
    description: E-Mail-Adressen aus Ihrer Braze-Bounce-Liste entfernen.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_remove_spam'>/email/spam/remove</a>
    description: E-Mail-Adressen aus Ihrer Braze-Spam-Liste entfernen.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_email_subscription_status'>/email/status</a>
    description: Den E-Mail-Abo-Status für Ihre Nutzer:innen festlegen.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_create_email_template'>/templates/email/create</a>
    description: E-Mail-Templates im Braze-Dashboard erstellen.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_update_email_template'>/templates/email/update</a>
    description: E-Mail-Templates im Braze-Dashboard aktualisieren.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/email/get_list_hard_bounces'>/email/hard_bounces</a>
    description: Eine Liste der E-Mail-Adressen abrufen, die Ihre E-Mail-Nachrichten innerhalb eines bestimmten Zeitraums als Hard Bounce zurückgewiesen haben.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses'>/email/unsubscribes</a>
    description: E-Mails zurückgeben, die sich im Zeitraum von <code>start_date</code> bis <code>end_date</code> abgemeldet haben.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information'>/templates/email/info</a>
    description: Informationen zu Ihren E-Mail-Templates abrufen.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates'>/templates/email/list</a>
    description: Eine Liste der verfügbaren E-Mail-Templates in Ihrem Braze-Konto abrufen.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/translations/webhook_templates/get_view_source_webhook_template'>/templates/webhook/translations/source</a>
    description: Die Standard-Quellübersetzungen für ein Webhook-Template anzeigen.
    tags:
      - Webhook Templates
  - name: <a href='/docs/api/endpoints/translations/webhook_templates/get_view_translations_webhook_template'>/templates/webhook/translations</a>
    description: Übersetzungen für ein Webhook-Template anzeigen.
    tags:
      - Webhook Templates
  - name: <a href='/docs/api/endpoints/translations/webhook_templates/put_update_webhook_template'>/templates/webhook/translations</a>
    description: Übersetzungen für ein Webhook-Template aktualisieren.
    tags:
      - Webhook Templates
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics'>/campaigns/data_series</a>
    description: Eine tägliche Reihe verschiedener Statistiken für eine Campaign über einen Zeitraum abrufen.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_details'>/campaigns/details</a>
    description: Relevante Informationen zu einer bestimmten Campaign abrufen.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaigns'>/campaigns/list</a>
    description: Eine Liste von Campaigns exportieren, die jeweils den Namen, den Campaign-API-Bezeichner, die Angabe, ob es sich um eine API-Campaign handelt, sowie die zugehörigen Tags enthält.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_send_analytics'>/sends/data_series</a>
    description: Eine tägliche Reihe verschiedener Statistiken für eine getrackte <code>send_id</code> abrufen.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_analytics'>/canvas/data_series</a>
    description: Zeitreihendaten für ein Canvas exportieren.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary'>/canvas/data_summary</a>
    description: Rollups von Zeitreihendaten für ein Canvas exportieren und eine übersichtliche Zusammenfassung der Canvas-Ergebnisse bereitstellen.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_details'>/canvas/details</a>
    description: Metadaten zu einem Canvas exportieren, z. B. den Namen, den Erstellungszeitpunkt, den aktuellen Status und mehr.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvases'>/canvas/list</a>
    description: Eine Liste von Canvases exportieren, einschließlich des Namens, des Canvas-API-Bezeichners und der zugehörigen Tags.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_analytics'>/segments/data_series</a>
    description: Eine tägliche Reihe der geschätzten Größe eines Segments über einen Zeitraum abrufen.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_details'>/segments/details</a>
    description: Relevante Informationen zu einem Segment abrufen.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment'>/segments/list</a>
    description: Eine Liste von Segmenten exportieren, die jeweils den Namen, den Segment-API-Bezeichner und die Angabe enthalten, ob Analytics-Tracking aktiviert ist.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/post_cancel_export'>/export/segment/cancel</a>
    description: Exporte für die angegebene Segment-ID stornieren.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/sessions/get_sessions_analytics'>/sessions/data_series</a>
    description: Eine Reihe der Anzahl von Sitzungen für Ihre App über einen bestimmten Zeitraum abrufen.
    tags:
      - Sessions
  - name: <a href='/docs/api/endpoints/export/custom_attributes/get_custom_attributes'>/custom_attributes</a>
    description: Eine Liste angepasster Attribute exportieren, einschließlich Name, Beschreibung, Datentyp, Array-Länge (falls zutreffend), Status und zugehörige Tags.
    tags:
      - Custom Attributes
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics'>/events/data_series</a>
    description: Eine Reihe der Vorkommen eines angepassten Events in Ihrer App über einen bestimmten Zeitraum abrufen.
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events_data'>/events</a>
    description: Eine Liste angepasster Events exportieren, einschließlich Name, Beschreibung, Status, zugehörige Tags und Einbeziehung in Analytics-Berichte.
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events'>/events/list</a>
    description: Eine Liste der Namen angepasster Events exportieren, die für Ihre App aufgezeichnet wurden.
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block'>/content_blocks/create</a>
    description: Einen E-Mail-Content-Block erstellen.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block'>/content_blocks/update</a>
    description: Einen E-Mail-Content-Block aktualisieren.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information'>/content_blocks/info</a>
    description: Informationen zu Ihrem bestehenden E-Mail-Content-Block abrufen.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks'>/content_blocks/list</a>
    description: Informationen zu Ihren bestehenden Content Blocks auflisten.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date'>/kpi/dau/data_series</a>
    description: Eine tägliche Reihe der Gesamtzahl eindeutiger aktiver Nutzer:innen an jedem Datum abrufen.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days'>/kpi/mau/data_series</a>
    description: Eine tägliche Reihe der Gesamtzahl eindeutiger aktiver Nutzer:innen über ein rollierendes 30-Tage-Fenster abrufen.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date'>/kpi/new_users/data_series</a>
    description: Eine tägliche Reihe der Gesamtzahl neuer Nutzer:innen an jedem Datum abrufen.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date'>/kpi/uninstalls/data_series</a>
    description: Eine tägliche Reihe der Gesamtzahl der Deinstallationen an jedem Datum abrufen.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/sms/post_remove_invalid_numbers'>/sms/invalid_phone_numbers/remove</a>
    description: "„Ungültige“ Telefonnummern aus der Liste ungültiger Nummern in Braze entfernen. Verwenden Sie dies, um Telefonnummern erneut zu validieren, nachdem Braze sie als ungültig markiert hat."
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/sms/get_query_invalid_numbers'>/sms/invalid_phone_numbers</a>
    description: "Eine Liste der Telefonnummern abrufen, die Braze innerhalb eines bestimmten Zeitraums als „ungültig“ markiert hat."
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/export/purchases/get_list_product_id'>/purchases/product_list</a>
    description: Eine paginierte Liste von Produkt-IDs zurückgeben.
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/export/purchases/get_number_of_purchases'>/purchases/quantity_series</a>
    description: Die Gesamtzahl der Käufe in Ihrer App über einen Zeitraum zurückgeben.
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/export/purchases/get_revenue_series'>/purchases/revenue_series</a>
    description: Den Gesamtbetrag zurückgeben, der in Ihrer App über einen Zeitraum ausgegeben wurde.
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/preference_center/get_create_url_preference_center'>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</a>
    description: Eine URL für ein Präferenzzentrum erstellen.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/get_list_preference_center'>/preference_center/v1/list</a>
    description: Verfügbare Präferenzzentren auflisten.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/get_view_details_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>
    description: Die Details Ihres Präferenzzentrums anzeigen, einschließlich des Erstellungs- und Aktualisierungszeitpunkts.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/post_create_preference_center'>/preference_center/v1</a>
    description: Ein Präferenzzentrum erstellen, mit dem Nutzer:innen ihre Benachrichtigungspräferenzen für E-Mail-Campaigns verwalten können.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/put_update_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>
    description: Ein Präferenzzentrum aktualisieren.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: Mehrere Artikel in Ihrem Katalog löschen.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Einen Katalogartikel und seine Details auflisten.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: Mehrere Artikel in Ihrem Katalog bearbeiten.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: Mehrere Artikel in Ihrem Katalog erstellen.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog'>/catalogs/{catalog_name}</a>
    description: Einen Katalog löschen.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog'>/catalogs</a>
    description: Einen Katalog erstellen.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs'>/catalogs</a>
    description: Die Kataloge in einem Workspace auflisten.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Einen Artikel in einem Katalog erstellen.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Einen Artikel in einem Katalog bearbeiten.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk'>/catalogs/{catalog_name}/items</a>
    description: Mehrere Katalogartikel und deren Inhalt zurückgeben.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Einen Artikel in einem Katalog löschen.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Einen Artikel in einem Katalog ersetzen.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items'>/catalogs/{catalog_name}/items/</a>
    description: Mehrere Artikel in einem Katalog ersetzen.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields'>/catalogs/{catalog_name}/fields/</a>
    description: Mehrere Felder in einem Katalog erstellen.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field'>/catalogs/{catalog_name}/fields/{field_name}</a>
    description: Ein Feld aus einem Katalog löschen.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections'>/catalogs/{catalog_name}/selections</a>
    description: Eine Auswahl in einem Katalog erstellen.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection'>/catalogs/{catalog_name}/selections/{selection_name}</a>
    description: Eine Katalogauswahl löschen.
    tags:
      - Catalogs
  - name: <a href='/docs/post_create_user_account'>/scim/v2/Users</a>
    description: Ein neues Dashboard-Nutzer:innen-Konto erstellen, indem E-Mail, Vor- und Nachname sowie Berechtigungen (für die Festlegung von Berechtigungen auf Unternehmens-, Workspace- und Teamebene) angegeben werden.
    tags:
      - SCIM
  - name: <a href='/docs/get_see_user_account_information'>/scim/v2/Users/{id}</a>
    description: Ein bestehendes Dashboard-Nutzer:innen-Konto anhand der Ressourcen-ID nachschlagen.
    tags:
      - SCIM
  - name: <a href='/docs/post_update_existing_user_account'>/scim/v2/Users/{id}</a>
    description: Ein bestehendes Dashboard-Nutzer:innen-Konto aktualisieren, indem E-Mail, Vor- und Nachname sowie Berechtigungen (für die Festlegung von Berechtigungen auf Unternehmens-, Workspace- und Teamebene) angegeben werden.
    tags:
      - SCIM
  - name: <a href='/docs/delete_existing_dashboard_user'>/scim/v2/Users/{id}</a>
    description: Bestehende Dashboard-Nutzer:innen dauerhaft löschen.
    tags:
      - SCIM
  - name: <a href='/docs/get_search_existing_dashboard_user_email'>/scim/v2/Users?filter={userName@example.com}</a>
    description: Ein bestehendes Dashboard-Nutzer:innen-Konto anhand der E-Mail-Adresse nachschlagen.
    tags:
      - SCIM
  - name: <a href='/docs/api/endpoints/cdi/get_integration_list'>/cdi/integrations</a>
    description: Eine Liste vorhandener Integrationen zurückgeben.
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/cdi/post_job_sync'>/cdi/integrations/{integration_id}/sync</a>
    description: Eine Synchronisierung für eine bestimmte Integration triggern.
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/cdi/get_job_sync_status'>/cdi/integrations/{integration_id}/job_sync_status</a>
    description: Eine Liste der Synchronisierungsstatus zurückgeben.
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/sdk_authentication/post_create_sdk_authentication_key'>/app_group/sdk_authentication/create</a>
    description: Einen neuen SDK-Authentifizierungsschlüssel für Ihre App erstellen.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/get_sdk_authentication_keys'>/app_group/sdk_authentication/keys</a>
    description: SDK-Authentifizierungsschlüssel für Ihre App auflisten.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key'>/app_group/sdk_authentication/primary</a>
    description: Einen SDK-Authentifizierungsschlüssel als Primärschlüssel für Ihre App festlegen.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key'>/app_group/sdk_authentication/delete</a>
    description: Einen SDK-Authentifizierungsschlüssel für Ihre App löschen.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/media_library/manage_assets/create'>/media_library/create</a>
    description: Ein Asset in die Medienbibliothek hochladen.
    tags:
      - Media Library
---