---
nav_title: 메시지
article_title: 메시징 엔드포인트
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
description: "이 랜딩 페이지에는 Braze 메시징 엔드포인트가 나열되어 있습니다."
page_type: landing

guide_top_header: "메시징 엔드포인트"
guide_top_text: "Braze 메시징 API는 사용자에게 메시지를 보낼 수 있는 두 가지 옵션을 제공합니다. <code class='highlighter-rouge'>/messages/send</code> 및 `/messages/schedule` 엔드포인트를 사용하여 API 요청에 메시지 내용과 구성을 직접 제공할 수 있습니다. 또는 Braze 대시보드에서 API 트리거 캠페인을 사용하여 메시지의 세부 사항을 관리하고, `/campaigns/trigger/send` 및 `/campaigns/trigger/schedule` 엔드포인트를 사용하여 전송 시점과 수신 대상을 제어할 수 있습니다. 다음 섹션에서는 두 가지 방법의 요청 사양에 대해 자세히 설명합니다. <br> <br> 다른 캠페인과 마찬가지로, Braze 대시보드에서 <a href='/docs/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/#re-eligibility-with-api-triggered-campaigns'>재자격 설정</a> 을 구성하여 특정 사용자가 메시징 API 캠페인을 받을 수 있는 횟수를 제한할 수 있습니다. Braze는 API 요청 횟수에 관계없이 캠페인에 대해 재자격을 얻지 못한 사용자에게는 API 메시지를 전달하지 않습니다. <br> <br> 메시지 전송 엔드포인트를 사용하면 지정된 사용자에게 즉시 메시지를 보낼 수 있습니다. Segment를 타겟팅하는 경우, 요청 기록이 **메시지 활동 로그**에 저장됩니다. 메시지 스케줄 엔드포인트를 사용하여 지정된 시간에 메시지를 보내고, 이미 예약한 메시지를 수정하거나 취소할 수 있습니다."

guide_featured_title: "메시지 스케줄 엔드포인트"
guide_featured_list:
  - name: "GET: 예정된 Campaigns 및 Canvases 목록 보기"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: 예약된 메시지 삭제"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: 예약된 API 트리거 Campaigns 삭제"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: 예약된 API 트리거 Canvases 삭제"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: 메시지 스케줄"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST: API 트리거 Campaign 메시지 스케줄"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: API 트리거 Canvas 메시지 스케줄"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: 예약된 메시지 업데이트"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: 예약된 API 트리거 Campaign 메시지 업데이트"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: 예약된 API 트리거 Canvas 메시지 업데이트"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "메시지 전송 엔드포인트"
guide_menu_list:
  - name: "POST: 전송 ID 생성"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids/
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST: 즉시 메시지 전송"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages/
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST: API 트리거 Campaign 메시지 즉시 전송"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST: API 트리거 Canvas 메시지 즉시 전송"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "메시지 복제 엔드포인트"
guide_menu_list2:
  - name: "POST: Campaigns 복제"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns/
    image: /assets/img/braze_icons/copy-04.svg
  - name: "POST: Canvases 복제"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases/
    image: /assets/img/braze_icons/copy-04.svg

guide_menu_title3: "Live Activity 엔드포인트"
guide_menu_list3:
  - name: "POST: Live Activity 업데이트"
    link: /docs/api/endpoints/messaging/live_activity/update/
    image: /assets/img/braze_icons/tablet-01.svg
---