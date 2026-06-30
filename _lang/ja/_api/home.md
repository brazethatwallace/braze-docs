---
page_order: 0
nav_title: ホーム
article_title: Braze API ガイド
layout: api_glossary
glossary_top_header: "Braze API ガイド"
glossary_top_text: "Brazeは、ユーザーのトラッキング、メッセージの送信、データのエクスポートなどを可能にする高パフォーマンスなREST APIを提供しています。このページでは、利用可能なBraze APIエンドポイントとその用途を紹介します。"
page_type: glossary
description: "このランディングページでは、利用可能なBraze APIエンドポイントとその用途を紹介します。"
glossary_tag_name: Endpoint Type

glossary_filter_text: "Select endpoint type to narrow the glossary:"

glossary_mid_text: "Endpoint Search"
guide_featured_list:
  - name: APIの概要
    image: /assets/img/braze_icons/annotation-info.svg
    link: /docs/api/basics
  - name: API識別子の種類
    link: /docs/api/identifier_types
    image: /assets/img/braze_icons/clipboard-check.svg
  - name: オブジェクトとフィルター
    link: /docs/api/objects_filters
    image: /assets/img/braze_icons/settings-01.svg
  - name: エラーとレスポンス
    link: /docs/api/errors
    image: /assets/img/braze_icons/list.svg
  - name: データ保持
    link: /docs/api/data_retention
    image: /assets/img/braze_icons/laptop-02.svg
  - name: レート制限
    link: /docs/api/api_limits
    image: /assets/img/braze_icons/hand.svg

# channel to icon/fa or image mapping
glossary_tags:
  - name: Campaigns
  - name: Canvas
  - name: Catalogs
  - name: Content Blocks
  - name: Custom Events
  - name: Email List
  - name: Email Templates
  - name: KPI
  - name: Media Library
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
  - name: <a href='/docs/api/endpoints/user_data/post_user_alias'>/users/alias/new</a>
    description: 識別された既存のユーザーに新しいユーザーエイリアスを追加するか、未識別の新規ユーザーを作成します。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_alias_update'>/users/alias/update</a>
    description: 既存のユーザーエイリアス名を新しいユーザーエイリアス名に更新します。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_delete'>/users/delete</a>
    description: 既知のユーザー識別子を指定して、任意のユーザープロファイルを削除します。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_global_control_group'>/users/export/global_control_group</a>
    description: グローバルコントロールグループ内のすべてのユーザーをエクスポートします。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_identifier'>/users/export/ids</a>
    description: ユーザー識別子を指定して、任意のユーザープロファイルからデータをエクスポートします。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_segment'>/users/export/segment</a>
    description: Segment内のすべてのユーザーをエクスポートします。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename'>/users/external_ids/rename</a>
    description: ユーザーのexternal IDの名前を変更します。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove'>/users/external_ids/remove</a>
    description: ユーザーの古い非推奨external IDを削除します。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_identify'>/users/identify</a>
    description: 未識別（エイリアスのみ）のユーザーを識別します。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_track'>/users/track</a>
    description: カスタムイベント、購入を記録し、ユーザープロファイル属性を更新します。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_merge'>/users/merge</a>
    description: ユーザープロファイルを別のユーザーにマージします。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns'>/campaigns/trigger/send</a>
    description: APIトリガー配信を使用して、指定したユーザーに即時の1回限りのメッセージを送信します。
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases'>/canvas/trigger/send</a>
    description: APIトリガー配信でCanvasメッセージを送信します。
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_messages'>/messages/send</a>
    description: Braze APIを使用して、指定したユーザーに即時の1回限りのメッセージを送信します。
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids'>/sends/id/create</a>
    description: 送信ごとにCampaignを作成せずに、メッセージの送信およびメッセージパフォーマンスのトラッキングに使用する送信IDをプログラムで作成します。
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message'>/transactional/v1/campaigns/{CAMPAIGN_ID}/send</a>
    description: 指定したユーザーに即時の1回限りのトランザクションメッセージを送信します。
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns'>/campaigns/trigger/schedule/create</a>
    description: ダッシュボードで作成したCampaignメッセージをAPIトリガー配信で送信します。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages'>/campaigns/trigger/schedule/delete</a>
    description: 以前にスケジュールしたAPIトリガーCampaignメッセージを送信前にキャンセルします。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns'>/campaigns/trigger/schedule/update</a>
    description: ダッシュボードで作成したスケジュール済みのAPIトリガーCampaignを更新します。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases'>/canvas/trigger/schedule/delete</a>
    description: 以前にAPIトリガーでスケジュールしたCanvasメッセージを送信前にキャンセルします。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases'>/canvas/trigger/schedule/create</a>
    description: APIトリガー配信でCanvasメッセージをスケジュールします。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages'>/messages/schedule/update</a>
    description: スケジュール済みメッセージを更新します。このエンドポイントは、<code>schedule</code>パラメータまたは<code>messages</code>パラメータ、あるいはその両方の更新を受け付けます。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages'>/messages/schedule/delete</a>
    description: 以前にスケジュールしたメッセージを送信前にキャンセルします。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages'>/messages/schedule/create</a>
    description: Campaign、Canvas、またはその他のメッセージを指定した時間に送信するようスケジュールします。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases'>/canvas/trigger/schedule/update</a>
    description: ダッシュボードで作成したスケジュール済みのAPIトリガーCanvasを更新します。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled'>/messages/scheduled_broadcasts</a>
    description: 現在からリクエストで指定した<code>end_time</code>までの間にスケジュールされたCampaignおよびエントリCanvasに関する情報のJSONリストを返します。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/live_activity/update'>/messages/live_activity/update</a>
    description: iOSのライブアクティビティを更新します。
    tags:
      - Live Activity
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status'>/subscription/status/set</a>
    description: Brazeダッシュボード上で最大50ユーザーのサブスクリプション状態を一括更新します。
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2'>/v2/subscription/status/set</a>
    description: Brazeダッシュボード上で最大50ユーザーのサブスクリプション状態を一括更新します。
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status'>/subscription/status/get</a>
    description: サブスクリプショングループ内のユーザーのサブスクリプション状態を取得します。
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups'>/subscription/user/status</a>
    description: 特定のユーザーのサブスクリプショングループをリストアップして取得します。
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/email/post_blacklist'>/email/blacklist</a>
    description: ユーザーのメール配信を停止し、ハードバウンスとしてマークします。
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_remove_hard_bounces'>/email/bounce/remove</a>
    description: Brazeのバウンスリストからメールアドレスを削除します。
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_remove_spam'>/email/spam/remove</a>
    description: Brazeのスパムリストからメールアドレスを削除します。
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_email_subscription_status'>/email/status</a>
    description: ユーザーのメールサブスクリプション状態を設定します。
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_create_email_template'>/templates/email/create</a>
    description: Brazeダッシュボードでメールテンプレートを作成します。
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_update_email_template'>/templates/email/update</a>
    description: Brazeダッシュボードでメールテンプレートを更新します。
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/email/get_list_hard_bounces'>/email/hard_bounces</a>
    description: 一定期間内にメールメッセージを「ハードバウンス」したメールアドレスのリストを取得します。
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses'>/email/unsubscribes</a>
    description: <code>start_date</code>から<code>end_date</code>までの期間に配信停止したメールアドレスを返します。
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information'>/templates/email/info</a>
    description: メールテンプレートの情報を取得します。
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates'>/templates/email/list</a>
    description: Brazeアカウントで利用可能なメールテンプレートのリストを取得します。
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics'>/campaigns/data_series</a>
    description: Campaignに関するさまざまな統計の日次データを取得します。
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_details'>/campaigns/details</a>
    description: 指定したCampaignの関連情報を取得します。
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaigns'>/campaigns/list</a>
    description: Campaignのリストをエクスポートします。各Campaignには、名前、Campaign API識別子、APIキャンペーンかどうか、およびCampaignに関連付けられたタグが含まれます。
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_send_analytics'>/sends/data_series</a>
    description: トラッキング対象の<code>send_id</code>に関するさまざまな統計の日次データを取得します。
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_analytics'>/canvas/data_series</a>
    description: Canvasの時系列データをエクスポートします。
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary'>/canvas/data_summary</a>
    description: Canvasの時系列データのロールアップをエクスポートし、Canvasの結果の簡潔なサマリーを提供します。
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_details'>/canvas/details</a>
    description: 名前、作成日時、現在のステータスなど、Canvasに関するメタデータをエクスポートします。
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvases'>/canvas/list</a>
    description: 名前、Canvas API識別子、関連タグを含むCanvasのリストをエクスポートします。
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_analytics'>/segments/data_series</a>
    description: Segmentの推定サイズの日次データを時系列で取得します。
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_details'>/segments/details</a>
    description: Segmentの関連情報を取得します。
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment'>/segments/list</a>
    description: Segmentのリストをエクスポートします。各Segmentには、名前、セグメントAPI識別子、および分析トラッキングが有効かどうかが含まれます。
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/post_cancel_export'>/export/segment/cancel</a>
    description: 指定されたセグメントIDのエクスポートをキャンセルします。
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/sessions/get_sessions_analytics'>/sessions/data_series</a>
    description: 指定した期間におけるアプリのセッション数の時系列データを取得します。
    tags:
      - Sessions
  - name: <a href='/docs/api/endpoints/export/custom_attributes/get_custom_attributes'>/custom_attributes</a>
    description: 名前、説明、データタイプ、配列長（該当する場合）、ステータス、関連タグを含むカスタム属性のリストをエクスポートします。
    tags:
      - Custom Attributes
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics'>/events/data_series</a>
    description: 指定した期間におけるアプリ内のカスタムイベント発生回数の時系列データを取得します。
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events_data'>/events</a>
    description: 名前、説明、ステータス、関連タグ、分析レポートへの含有状況を含むカスタムイベントのリストをエクスポートします。
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events'>/events/list</a>
    description: アプリに記録されたカスタムイベント名のリストをエクスポートします。
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block'>/content_blocks/create</a>
    description: メールのContent Blocksを作成します。
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block'>/content_blocks/update</a>
    description: メールのContent Blocksを更新します。
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information'>/content_blocks/info</a>
    description: 既存のメールContent Blocksの情報を取得します。
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks'>/content_blocks/list</a>
    description: 既存のContent Blocksの情報をリストアップします。
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date'>/kpi/dau/data_series</a>
    description: 各日付のユニークアクティブユーザー総数の日次データを取得します。
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days'>/kpi/mau/data_series</a>
    description: 30日間のローリングウィンドウにおけるユニークアクティブユーザー総数の日次データを取得します。
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date'>/kpi/new_users/data_series</a>
    description: 各日付の新規ユーザー総数の日次データを取得します。
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date'>/kpi/uninstalls/data_series</a>
    description: 各日付のアンインストール総数の日次データを取得します。
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/sms/post_remove_invalid_numbers'>/sms/invalid_phone_numbers/remove</a>
    description: Brazeの無効リストから「無効」な電話番号を削除します。Brazeが無効とマークした電話番号を再検証する場合に使用します。
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/sms/get_query_invalid_numbers'>/sms/invalid_phone_numbers</a>
    description: 一定期間内にBrazeが「無効」とマークした電話番号のリストを取得します。
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/export/purchases/get_list_product_id'>/purchases/product_list</a>
    description: ページ分割された製品IDのリストを返します。
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/export/purchases/get_number_of_purchases'>/purchases/quantity_series</a>
    description: 指定した期間におけるアプリの購入総数を返します。
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/export/purchases/get_revenue_series'>/purchases/revenue_series</a>
    description: 指定した期間におけるアプリの総支出額を返します。
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/preference_center/get_create_url_preference_center'>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</a>
    description: ユーザー設定センターのURLを作成します。
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/get_list_preference_center'>/preference_center/v1/list</a>
    description: 利用可能なユーザー設定センターをリストアップします。
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/get_view_details_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>
    description: ユーザー設定センターの作成日時や更新日時などの詳細を表示します。
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/post_create_preference_center'>/preference_center/v1</a>
    description: ユーザー設定センターを作成し、ユーザーがメールCampaignの通知設定を管理できるようにします。
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/put_update_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>
    description: ユーザー設定センターを更新します。
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: カタログ内の複数のアイテムを削除します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: カタログアイテムとその詳細をリストアップします。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: カタログ内の複数のアイテムを編集します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: カタログ内に複数のアイテムを作成します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog'>/catalogs/{catalog_name}</a>
    description: カタログを削除します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog'>/catalogs</a>
    description: カタログを作成します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs'>/catalogs</a>
    description: ワークスペース内のカタログをリストアップします。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: カタログにアイテムを作成します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: カタログのアイテムを編集します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk'>/catalogs/{catalog_name}/items</a>
    description: 複数のカタログアイテムとその内容を返します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: カタログのアイテムを削除します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: カタログのアイテムを置換します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items'>/catalogs/{catalog_name}/items/</a>
    description: カタログの複数のアイテムを置換します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields'>/catalogs/{catalog_name}/fields/</a>
    description: カタログに複数のフィールドを作成します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field'>/catalogs/{catalog_name}/fields/{field_name}</a>
    description: カタログからフィールドを削除します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections'>/catalogs/{catalog_name}/selections</a>
    description: カタログにセレクションを作成します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection'>/catalogs/{catalog_name}/selections/{selection_name}</a>
    description: カタログセレクションを削除します。
    tags:
      - Catalogs
  - name: <a href='/docs/post_create_user_account'>/scim/v2/Users</a>
    description: メール、姓名、権限（会社、ワークスペース、チームレベルでの権限設定）を指定して、新しいダッシュボードユーザーアカウントを作成します。
    tags:
      - SCIM
  - name: <a href='/docs/get_see_user_account_information'>/scim/v2/Users/{id}</a>
    description: リソースIDを指定して、既存のダッシュボードユーザーアカウントを検索します。
    tags:
      - SCIM
  - name: <a href='/docs/post_update_existing_user_account'>/scim/v2/Users/{id}</a>
    description: メール、姓名、権限（会社、ワークスペース、チームレベルでの権限設定）を指定して、既存のダッシュボードユーザーアカウントを更新します。
    tags:
      - SCIM
  - name: <a href='/docs/delete_existing_dashboard_user'>/scim/v2/Users/{id}</a>
    description: 既存のダッシュボードユーザーを完全に削除します。
    tags:
      - SCIM
  - name: <a href='/docs/get_search_existing_dashboard_user_email'>/scim/v2/Users?filter={userName@example.com}</a>
    description: メールアドレスを指定して、既存のダッシュボードユーザーアカウントを検索します。
    tags:
      - SCIM
  - name: <a href='/docs/api/endpoints/cdi/get_integration_list'>/cdi/integrations</a>
    description: 既存の統合のリストを返します。
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/cdi/post_job_sync'>/cdi/integrations/{integration_id}/sync</a>
    description: 指定した統合の同期をトリガーします。
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/cdi/get_job_sync_status'>/cdi/integrations/{integration_id}/job_sync_status</a>
    description: 同期ステータスのリストを返します。
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/sdk_authentication/post_create_sdk_authentication_key'>/app_group/sdk_authentication/create</a>
    description: アプリ用に新しいSDK認証キーを作成します。
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/get_sdk_authentication_keys'>/app_group/sdk_authentication/keys</a>
    description: アプリのSDK認証キーをリストアップします。
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key'>/app_group/sdk_authentication/primary</a>
    description: SDK認証キーをアプリのプライマリキーとして設定します。
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key'>/app_group/sdk_authentication/delete</a>
    description: アプリのSDK認証キーを削除します。
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/media_library/manage_assets/create'>/media_library/create</a>
    description: メディアライブラリにアセットをアップロードします。
    tags:
      - Media Library
---