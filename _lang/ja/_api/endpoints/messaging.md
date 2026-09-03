---
nav_title: メッセージ
article_title: メッセージングエンドポイント
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
description: "このランディングページには、Brazeのメッセージングエンドポイントが一覧表示されています。"
page_type: landing

guide_top_header: "メッセージングエンドポイント"
guide_top_text: "BrazeメッセージングAPIでは、ユーザーにメッセージを送信するための2つの方法が用意されています。<code class='highlighter-rouge'>/messages/send</code> および `/messages/schedule` エンドポイントを使用して、APIリクエストでメッセージの内容と設定を指定できます。または、BrazeダッシュボードでAPIトリガーキャンペーンを使用してメッセージの詳細を管理し、`/campaigns/trigger/send` と `/campaigns/trigger/schedule` エンドポイントで送信のタイミングと送信先をコントロールできます。以下のセクションでは、両方の方法のリクエスト仕様について詳しく説明します。 <br> <br> 他のキャンペーンと同様に、Brazeダッシュボードで<a href='/docs/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery#re-eligibility-with-api-triggered-campaigns'>再適格性設定</a> を構成することで、特定のユーザーがメッセージングAPIキャンペーンを受信できる回数を制限できます。Brazeは、送信されたAPIリクエスト数に関係なく、キャンペーンの再適格性を満たしていないユーザーにはAPIメッセージを配信しません。 <br> <br> 「メッセージを送信」エンドポイントでは、指定したユーザーに即時メッセージを送信できます。セグメントをターゲットにしている場合、リクエストの記録は**メッセージアクティビティログ**に保存されます。「メッセージをスケジュール」エンドポイントを使用して、指定した時間にメッセージを送信したり、すでにスケジュールしたメッセージを変更またはキャンセルしたりできます。"

guide_featured_title: "メッセージスケジュールエンドポイント"
guide_featured_list:
  - name: "GET: 今後スケジュールされているキャンペーンとキャンバスを一覧表示"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: スケジュールされたメッセージを削除"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: スケジュールされたAPIトリガーキャンペーンを削除"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: スケジュールされたAPIトリガーキャンバスを削除"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: メッセージをスケジュール"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST: APIトリガーキャンペーンメッセージをスケジュール"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: APIトリガーキャンバスメッセージをスケジュール"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: スケジュールされたメッセージを更新"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: スケジュールされたAPIトリガーキャンペーンメッセージを更新"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: スケジュールされたAPIトリガーキャンバスメッセージを更新"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "メッセージ送信エンドポイント"
guide_menu_list:
  - name: "POST: 送信IDを作成"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST: メッセージを即時送信"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST: APIトリガーキャンペーンメッセージを即時送信"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST: APIトリガーキャンバスメッセージを即時送信"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "メッセージ複製エンドポイント"
guide_menu_list2:
  - name: "POST: キャンペーンを複製"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns
    image: /assets/img/braze_icons/copy-04.svg
  - name: "POST: キャンバスを複製"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases
    image: /assets/img/braze_icons/copy-04.svg

guide_menu_title3: "ライブアクティビティエンドポイント"
guide_menu_list3:
  - name: "POST: ライブアクティビティを更新"
    link: /docs/api/endpoints/messaging/live_activity/update
    image: /assets/img/braze_icons/tablet-01.svg
---