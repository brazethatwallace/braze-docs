---
nav_title: Mensagens
article_title: Endpoints de envio de mensagens
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
description: "Essa landing page lista os endpoints de envio de mensagens da Braze."
page_type: landing

guide_top_header: "Endpoints de envio de mensagens"
guide_top_text: "A API or interface de programação do aplicativo (API) de envio de mensagens da Braze oferece duas opções distintas para o envio de mensagens aos seus usuários. Você pode fornecer o conteúdo e a configuração da mensagem na solicitação da API or interface de programação do aplicativo (API) com os endpoints <code class='highlighter-rouge'>/messages/send</code> e `/messages/schedule`. Alternativamente, você pode gerenciar os detalhes da sua mensagem com uma Campaign disparada por API or interface de programação do aplicativo (API) no dashboard da Braze e controlar quando e para quem ela é enviada com os endpoints `/campaigns/trigger/send` e `/campaigns/trigger/schedule`. As seções a seguir detalham a especificação da solicitação para ambos os métodos. <br> <br> Assim como em outras Campaigns, é possível limitar o número de vezes que um determinado usuário pode receber uma Campaign de envio de mensagens da API or interface de programação do aplicativo (API) configurando as <a href='/docs/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery#re-eligibility-with-API or interface de programação do aplicativo (API)-triggered-campaigns'>configurações de reelegibilidade</a> no dashboard da Braze. A Braze não enviará mensagens de API or interface de programação do aplicativo (API) para usuários que não se tornaram reelegíveis para a Campaign, independentemente de quantas solicitações de API or interface de programação do aplicativo (API) forem enviadas. <br> <br> Os endpoints de envio de mensagens permitem enviar mensagens imediatas a usuários designados. Se estiver direcionando para um Segment or segmento, um registro da sua solicitação será armazenado no **Message Activity Log**. Use os endpoints de agendamento de mensagens para enviar mensagens em um horário designado e modificar ou cancelar mensagens que já foram agendadas."

guide_featured_title: "Endpoints de agendamento de mensagens"
guide_featured_list:
  - name: "GET: Listar próximas Campaigns e Canvas agendados"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Excluir mensagens agendadas"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Excluir Campaigns agendadas disparadas por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Excluir Canvas agendados disparados por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Agendar mensagens"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST: Agendar mensagens de Campaign disparadas por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Agendar mensagens de Canvas disparadas por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Atualizar mensagens agendadas"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Atualizar mensagens de Campaign agendadas disparadas por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Atualizar mensagens de Canvas agendadas disparadas por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "Endpoints de envio de mensagens"
guide_menu_list:
  - name: "POST: Criar IDs de envio"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST: Enviar mensagens imediatamente"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST: Enviar mensagens de Campaign disparadas por API imediatamente"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST: Enviar mensagens de Canvas disparadas por API imediatamente"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "Endpoints de duplicação de mensagens"
guide_menu_list2:
  - name: "POST: Duplicar Campaigns"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns
    image: /assets/img/braze_icons/copy-04.svg
  - name: "POST: Duplicar Canvas"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases
    image: /assets/img/braze_icons/copy-04.svg

guide_menu_title3: "Endpoints de Live Activity"
guide_menu_list3:
  - name: "POST: Atualizar Live Activity"
    link: /docs/api/endpoints/messaging/live_activity/update
    image: /assets/img/braze_icons/tablet-01.svg
---