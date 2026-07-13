---
nav_title: Nachrichten
article_title: Messaging-Endpunkte
search_tag: Endpoint
page_order: 3
local_redirect: #app-group-rest-api-key #app-identifier #external-user-id #segment-identifier #campaign-identifier #canvas-identifier #trigger-properties #canvas-identifier #server-responses #fatal-errors #responses-for-tracked-send-ids #messaging-queued #canvas-entry-properties
  app-group-rest-api-key: '/docs/api/basics/#rest-api-key'
  app-identifier: '/docs/api/identifier_types/'
  external-user-id: '/docs/api/objects_filters/user_attributes_object/#braze-user-profile-fields'
  segment-identifier: '/docs/api/identifier_types/'
  campaign-identifier: '/docs/api/identifier_types/'
  canvas-identifier: '/docs/api/identifier_types/'
  send-identifier: '/docs/api/identifier_types/'
  trigger-properties: '/docs/api/objects_filters/trigger_properties_object'
  canvas-entry-properties: '/docs/api/objects_filters/canvas_entry_properties_object'
  server-responses: '/docs/api/errors/'
  messaging-queued: '/docs/api/errors/'
  responses-for-tracked-send-ids: '/docs/api/errors/'
  fatal-errors: '/docs/api/errors/'

layout: dev_guide

#Required
description: "Diese Landing-Page listet die Messaging-Endpunkte von Braze auf."
page_type: landing

guide_top_header: "Messaging-Endpunkte"
guide_top_text: "Die Braze Messaging API bietet Ihnen zwei verschiedene Optionen für den Versand von Nachrichten an Ihre Nutzer:innen. Sie können den Nachrichteninhalt und die Konfiguration in der API-Anfrage mit den Endpunkten <code class='highlighter-rouge'>/messages/send</code> und `/messages/schedule` angeben. Alternativ können Sie die Details Ihrer Nachricht mit einer API-getriggerten Kampagne im Braze-Dashboard verwalten und mit den Endpunkten `/campaigns/trigger/send` und `/campaigns/trigger/schedule` steuern, wann und an wen sie gesendet wird. In den folgenden Abschnitten wird die Anfragespezifikation für beide Methoden erläutert. <br> <br> Ähnlich wie bei anderen Kampagnen können Sie die Häufigkeit, mit der bestimmte Nutzer:innen eine Messaging-API-Kampagne erhalten können, einschränken, indem Sie die <a href='/docs/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery#re-eligibility-with-api-triggered-campaigns'>Einstellungen zur erneuten Berechtigung</a> im Braze-Dashboard konfigurieren. Braze stellt keine API-Nachrichten an Nutzer:innen zu, die sich nicht erneut für die Kampagne qualifiziert haben, unabhängig davon, wie viele API-Anfragen gesendet werden. <br> <br> Mit den Endpunkten zum Senden von Nachrichten können Sie sofortige Nachrichten an bestimmte Nutzer:innen senden. Wenn Sie ein Segment als Zielgruppe verwenden, wird eine Aufzeichnung Ihrer Anfrage im **Nachrichten-Aktivitätsprotokoll** gespeichert. Verwenden Sie die Endpunkte zum Planen von Nachrichten, um Nachrichten zu einem bestimmten Zeitpunkt zu versenden und bereits geplante Nachrichten zu ändern oder abzubrechen."

guide_featured_title: "Endpunkte zum Planen von Nachrichten"
guide_featured_list:
  - name: "GET: Anstehende geplante Kampagnen und Canvases auflisten"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Geplante Nachrichten löschen"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Geplante API-getriggerte Kampagnen löschen"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Geplante API-getriggerte Canvases löschen"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Nachrichten planen"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST: API-getriggerte Kampagnennachrichten planen"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: API-getriggerte Canvas-Nachrichten planen"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Geplante Nachrichten aktualisieren"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Geplante API-getriggerte Kampagnennachrichten aktualisieren"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Geplante API-getriggerte Canvas-Nachrichten aktualisieren"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "Endpunkte zum Senden von Nachrichten"
guide_menu_list:
  - name: "POST: Sende-IDs erstellen"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST: Nachrichten sofort senden"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST: API-getriggerte Kampagnennachrichten sofort senden"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST: API-getriggerte Canvas-Nachrichten sofort senden"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "Endpunkte zum Duplizieren von Nachrichten"
guide_menu_list2:
  - name: "POST: Kampagnen duplizieren"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns
    image: /assets/img/braze_icons/copy-04.svg
  - name: "POST: Canvases duplizieren"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases
    image: /assets/img/braze_icons/copy-04.svg

guide_menu_title3: "Live-Activity-Endpunkte"
guide_menu_list3:
  - name: "POST: Live Activity aktualisieren"
    link: /docs/api/endpoints/messaging/live_activity/update
    image: /assets/img/braze_icons/tablet-01.svg
---