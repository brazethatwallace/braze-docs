---
nav_title: Mensajes
article_title: Endpoints de mensajería
search_tag: Endpoint
page_order: 3
local_redirect: #app-group-rest-api-key #app-identifier #external-user-id #segment-identifier #campaign-identifier #canvas-identifier #trigger-properties #canvas-identifier #server-responses #fatal-errors #responses-for-tracked-send-ids #messaging-queued #canvas-entry-properties
  app-group-rest-api-key: '/docs/api/basics/#rest-api-key-permissions'
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
description: "Esta página de inicio enumera los endpoints de mensajería de Braze."
page_type: landing

guide_top_header: "Endpoints de mensajería"
guide_top_text: "La API de mensajería de Braze te ofrece dos opciones distintas para enviar mensajes a tus usuarios. Puedes proporcionar el contenido y la configuración del mensaje en la solicitud de API con los endpoints <code class='highlighter-rouge'>/messages/send</code> y `/messages/schedule`. También puedes administrar los detalles de tu mensaje con una campaña activada por API en el panel de Braze y controlar cuándo y a quién se envía con los endpoints `/campaigns/trigger/send` y `/campaigns/trigger/schedule`. En las secciones siguientes se detallan las especificaciones de las solicitudes de ambos métodos. <br> <br> Al igual que en otras campañas, puedes limitar el número de veces que un usuario concreto puede recibir una campaña de la API de mensajería configurando los <a href='/docs/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery#re-eligibility-with-api-triggered-campaigns'>ajustes de reelegibilidad</a> en el panel de Braze. Braze no enviará mensajes de API a usuarios que no hayan vuelto a ser elegibles para la campaña, independientemente del número de solicitudes de API que se envíen. <br> <br> Los endpoints de envío de mensajes te permiten enviar mensajes inmediatos a usuarios designados. Si te diriges a un Segment, se guardará un registro de tu solicitud en el **Registro de actividad de mensajes**. Utiliza los endpoints de programación de mensajes para enviar mensajes a una hora determinada y modificar o cancelar mensajes que ya hayas programado."

guide_featured_title: "Endpoints de programación de mensajes"
guide_featured_list:
  - name: "GET: Enumerar próximas Campaigns y Canvas programados"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Eliminar mensajes programados"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Eliminar Campaigns programadas activadas por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Eliminar Canvas programados activados por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Programar mensajes"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST: Programar mensajes de Campaigns activadas por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Programar mensajes de Canvas activados por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Actualizar mensajes programados"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Actualizar mensajes de Campaigns programadas activadas por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Actualizar mensajes de Canvas programados activados por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "Endpoints de envío de mensajes"
guide_menu_list:
  - name: "POST: Crear ID de envío"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST: Enviar mensajes inmediatamente"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST: Enviar inmediatamente mensajes de Campaigns activadas por API"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST: Enviar inmediatamente mensajes de Canvas activados por API"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "Endpoints de duplicación de mensajes"
guide_menu_list2:
  - name: "POST: Duplicar Campaigns"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns
    image: /assets/img/braze_icons/copy-04.svg
  - name: "POST: Duplicar Canvas"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases
    image: /assets/img/braze_icons/copy-04.svg

guide_menu_title3: "Endpoints de Live Activity"
guide_menu_list3:
  - name: "POST: Actualizar Live Activity"
    link: /docs/api/endpoints/messaging/live_activity/update
    image: /assets/img/braze_icons/tablet-01.svg
---