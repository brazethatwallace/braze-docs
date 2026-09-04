---
nav_title: Messages
article_title: Endpoints d'envoi de messages
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
description: "Cette page d'accueil liste les endpoints Braze d'envoi de messages."
page_type: landing

guide_top_header: "Endpoints d'envoi de messages"
guide_top_text: "L'API d'envoi de messages de Braze vous offre deux options distinctes pour envoyer des messages à vos utilisateurs. Vous pouvez fournir le contenu et la configuration du message dans la requête API à l'aide des endpoints <code class='highlighter-rouge'>/messages/send</code> et `/messages/schedule`. Vous pouvez également gérer les détails de votre message via une campagne déclenchée par API dans le tableau de bord de Braze et contrôler quand et à qui il est envoyé à l'aide des endpoints `/campaigns/trigger/send` et `/campaigns/trigger/schedule`. Les sections suivantes détaillent la spécification de requête pour les deux méthodes. <br> <br> Comme pour les autres campagnes, vous pouvez limiter le nombre de fois qu'un utilisateur donné peut recevoir une campagne API d'envoi de messages en configurant les <a href='/docs/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery#re-eligibility-with-api-triggered-campaigns'>paramètres de rééligibilité</a> dans le tableau de bord de Braze. Braze ne distribuera pas de messages API aux utilisateurs qui ne sont pas redevenus éligibles pour la campagne, quel que soit le nombre de requêtes API envoyées. <br> <br> Les endpoints d'envoi de messages vous permettent d'envoyer des messages immédiats à des utilisateurs désignés. Si vous ciblez un segment, un enregistrement de votre requête sera stocké dans le **Journal d'activité des messages**. Utilisez les endpoints de planification de messages pour envoyer des messages à une heure donnée, et pour modifier ou annuler des messages que vous avez déjà planifiés."

guide_featured_title: "Endpoints de planification de messages"
guide_featured_list:
  - name: "GET : Lister les Campaigns et Canvas planifiés à venir"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST : Supprimer les messages planifiés"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST : Supprimer des Campaigns planifiées déclenchées par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST : Supprimer des Canvas planifiés déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST : Planifier des messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST : Planifier des messages de Campaign déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST : Planifier des messages Canvas déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST : Mettre à jour les messages planifiés"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST : Mettre à jour les messages de Campaign planifiés déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST : Mettre à jour les messages Canvas planifiés déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "Endpoints d'envoi de messages"
guide_menu_list:
  - name: "POST : Créer des ID d'envoi"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST : Envoyer des messages immédiatement"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST : Envoyer immédiatement des messages de Campaign déclenchés par API"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST : Envoyer immédiatement des messages Canvas déclenchés par API"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "Endpoints de duplication de messages"
guide_menu_list2:
  - name: "POST : Dupliquer des Campaigns"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns
    image: /assets/img/braze_icons/copy-04.svg
  - name: "POST : Dupliquer des Canvas"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases
    image: /assets/img/braze_icons/copy-04.svg

guide_menu_title3: "Endpoints Live Activity"
guide_menu_list3:
  - name: "POST : Mettre à jour une Live Activity"
    link: /docs/api/endpoints/messaging/live_activity/update
    image: /assets/img/braze_icons/tablet-01.svg
---