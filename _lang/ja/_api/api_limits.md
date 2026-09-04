---
nav_title: レート制限
article_title: レート制限
page_order: 4.5
description: "この参考記事では、Braze APIインフラのAPIレート制限について説明します。"
page_type: reference
---

# レート制限 {#rate-limits}

> BrazeのAPIインフラは、顧客ベース全体で大量のデータを処理できるように設計されています。このため、ワークスペースごとにAPIレート制限を設けています。

レート制限とは、APIが一定時間内に受け取れるリクエスト数のことです。大規模システムにおける負荷ベースのサービス拒否インシデントの多くは、悪意のある攻撃ではなく、ソフトウェアや設定のエラーによって引き起こされる意図しないものです。レート制限は、このようなエラーによってBraze APIのリソースがお客様に提供できなくなることを防ぎます。一定時間内に多くのリクエストが送信された場合、ステータスコード`429`のエラー応答が返されることがあります。これは、レート制限に達したことを示します。

{% alert warning %}
APIレート制限は、システムの適切な使用状況に応じて変更される場合があります。損害や悪用を防ぐため、APIコールを行う際には適切な制限を設けることを推奨します。
{% endalert %}

## リクエストタイプ別のレート制限 {#rate-limits-by-request-type}

さまざまなリクエストタイプのデフォルト API レート制限については、以下を参照してください。これらのデフォルト制限は、リクエストに応じて引き上げることができます。詳細については、カスタマーサクセスマネージャーにお問い合わせください。

### 個別のレート制限を持つリクエスト {#requests-with-different-rate-limits}

| リクエストタイプ | デフォルト API レート制限 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)                                                                                                                                                                                                                                   | **リクエスト：**レート制限は契約内容に応じて異なります。料金体系にデータポイントが含まれるお客様には、Brazeは3秒あたり3,000リクエストのバースト制限を適用します。その他のすべてのお客様については、契約条件に基づいて制限が構成されます。ご自身の制限に関するご質問は、Brazeサポートまたはカスタマーサクセスマネージャーにお問い合わせください。<br><br>**バッチ処理：**1回のAPIリクエストあたり、`attributes`、`events`、`purchases`を合わせて最大75オブジェクトまで。レガシーレート制限のお客様は、各配列ごとに独立して最大75オブジェクトを含めることができます。詳細については、[ユーザートラックリクエストのバッチ処理](#batch-user-track)を参照してください。<br><br>**Monthly Active Users CY 24-25、Universal MAU、Web MAU、Mobile MAUの制限：**[Monthly Active Users CY 24-25の制限]({{site.baseurl}}/api/endpoints/user_data/post_user_track#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau)を参照してください。 |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)                                                                                                                                                                                                                              | **2024年8月22日以降にオンボーディングした場合：**1分あたり250リクエスト。<br><br> **2024年8月22日より前にオンボーディングした場合：**1分あたり2,500リクエスト。                                                                                                                                                                                                                               |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)<br>[`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias)<br>[`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update)<br>[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)<br>[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)                                                                                                                    | 1分あたり20,000リクエスト。エンドポイント間で共有されます。                                                                                                                                                                                                                                                                                                                                 |
| [`/users/external_id/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename)                                                                                                                                                                                                                      | 1分あたり1,000リクエスト。                                                                                                                                                                                                                                                                                                                                                                |
| [`/users/external_id/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove)                                                                                                                                                                                                                      | 1分あたり1,000リクエスト。                                                                                                                                                                                                                                                                                                                                                                |
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events)                                                                                                                                                                                                                                   | 1時間あたり1,000リクエスト。`/purchases/product_list`エンドポイントと共有されます。                                                                                                                                                                                                                                                                                                              |
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id)                                                                                                                                                                                                                        | 1時間あたり1,000リクエスト。`/events/list`エンドポイントと共有されます。                                                                                                                                                                                                                                                                                                                         |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)                                                                                                                                                                                                                       | 1分あたり50,000リクエスト。                                                                                                                                                                                                                                                                                                                                                               |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)<br>[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)<br>[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)<br>[`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)<br>[`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)                                                                                                                                                          | ブロードキャストコール（セグメント、フィルター、またはコネクテッドオーディエンスを広くターゲットとする場合）の場合、すべてのオーディエンスに対して1分あたり250リクエスト、および[ユニークオーディエンス]({{site.baseurl}}/api/api_limits#what-counts-as-the-same-unique-audience)ごとに1分あたり10リクエスト（いずれか先に到達した制限が適用されます）。<br><br>それ以外の場合、個別の受信者をターゲットとする際は、リクエストは1時間あたり250,000リクエストの[共有レート制限]({{site.baseurl}}/api/api_limits#requests-with-shared-rate-limits)に含まれます。                                                                                                                                                                                                                    |
| [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)                                                                                                                                                                                                                               | 1日あたり100リクエスト。                                                                                                                                                                                                                                                                                                                                                                     |
| [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)                                                                                                                                                                                                                       | 1分あたり5,000リクエスト。                                                                                                                                                                                                                                                                                                                                                                |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center)<br>[`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center)                                                                            | 1分あたり1,000リクエスト。                                                                                                                                                                                                                                                                                                                                                 |
| [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center)                                                                                                                                                            | 1分あたり10リクエスト。                                                                                                                                                                                                                                                                                                                                                    |
| [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)                                                                                                                                                                             | 1分あたり50リクエスト。エンドポイント間で共有されます。                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)                                                                                                                             | 1分あたり16,000リクエスト。エンドポイント間で共有されます。                                                                                                                                                                                                                                                                                                                                  |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item) | 1分あたり50リクエスト。エンドポイント間で共有されます。                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)<br>[`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)<br>[`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)<br>[`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | 1分あたり50リクエスト。エンドポイント間で共有されます。 |
| [`/scim/v2/Users/{id}`]({{site.baseurl}}/get_see_user_account_information)<br>[`/scim/v2/Users?filter={userName@example.com}`]({{site.baseurl}}/get_search_existing_dashboard_user_email)<br>[`/scim/v2/Users/{id}`]({{site.baseurl}}/post_update_existing_user_account)<br>[`/scim/v2/Users/{id}}`]({{site.baseurl}}/delete_existing_dashboard_user)<br>[`/scim/v2/Users/`]({{site.baseurl}}/post_create_user_account)                                                                          | 1日あたり5,000リクエスト（会社単位）。エンドポイント間で共有されます。                                                                                                                                                                                                                                                                                                                        |
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list)                                                                                                                                                                                                                              | 1分あたり50リクエスト。                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status)                                                                                                                                                                                                        | 1分あたり20リクエスト。                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync)                                                                                                                                                                                             | 1分あたり100リクエスト。                                                                                                                                                                                                                                                                                                                                                                  |
| [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | 1時間あたり100リクエスト。 |
| [`/media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file) | 1時間あたり100リクエスト。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="個別のレート制限を持つリクエスト" }

### 共有レート制限を持つリクエスト {#requests-with-shared-rate-limits}

以下のリクエストには、1時間あたり250,000リクエストの共有レート制限が適用されます。

- [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key)
- [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys)
- [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)（非ブロードキャストコール&#8212;`external_user_ids`または`aliases`を指定する場合のみ）
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)（非ブロードキャストコールのみ）
- [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages)
- [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns)
- [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)
- [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary)
- [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details)
- [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)（非ブロードキャストコールのみ）
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)（非ブロードキャストコールのみ）
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
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)（非ブロードキャストコールのみ）
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

### 同一ユニークオーディエンスとしてカウントされるもの {#what-counts-as-the-same-unique-audience}

これは以下のエンドポイントに適用されます：[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)、[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)、[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)、[`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)、および[`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)。

これらのエンドポイントでは、以下のすべてが一致する場合、ブロードキャストリクエストは同一ユニークオーディエンスをターゲットとしているとみなされます。

- トリガーされるキャンペーンまたはキャンバス（APIリクエスト内の`campaign_id`または`canvas_id`（指定されている場合））
- ターゲットとするオーディエンス（セグメントまたはフィルター、またはAPIキャンペーンの場合はAPIリクエスト内の`segment_id`）
- コネクテッドオーディエンスフィルター（APIリクエスト内の`audience`オブジェクト（指定されている場合））

これらの属性のユニークな組み合わせごとに個別のオーディエンスとしてカウントされるため、各ユニークオーディエンスに対する追加レート制限は、各組み合わせに対して独立して適用されます。

## APIリクエストのバッチ処理 {#batching-api-requests}

Braze APIはバッチ処理をサポートするように構築されています。バッチ処理を使用すると、Brazeは1回のAPI呼び出しでできるだけ多くのデータを取り込むことができるため、多数のAPI呼び出しを行う必要がありません。データを1回ずつ処理するよりも、バッチで処理する方がBrazeにとって効率的です。例えば、1,000件のバッチAPI呼び出しの処理は、75,000件の個別の呼び出しの処理よりもリソースが少なくて済みます。バッチ処理は、1時間あたり75,000回以上の呼び出しが必要になる可能性のあるアプリケーションにとって非常に重要です。

{% alert note %}
REST APIのレート制限の引き上げは、APIバッチ処理機能を活用しているお客様のニーズに基づいて検討されます。
{% endalert %}

### ユーザーの作成および更新エンドポイントのリクエストのバッチ処理 {#batch-user-track}

各`/users/track`リクエストには、`attributes`、`events`、`purchases`全体で合計最大75個のオブジェクトを含めることができます。各オブジェクトは1人のユーザーを更新できます。1つのユーザープロファイルは複数のオブジェクトで更新できます。

{% details レガシーレート制限 %}
レガシーレート制限が適用されるお客様の場合、各配列（`attributes`、`events`、`purchases`）にはそれぞれ独立して最大75個のオブジェクトを含めることができ、1リクエストあたりの合計最大数は225個になります。
{% enddetails %}

`/users/track`のレート制限の詳細については、[POST: ユーザーの作成と更新]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を参照してください。

このエンドポイントへのリクエストは、一般的に次の順序で処理が開始されます。

1. 属性
2. イベント
3. 購入

### メッセージングエンドポイントリクエストのバッチ処理 {#batching-messaging-endpoint-requests}

[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging)への1回のリクエストで、以下のいずれかに到達できます。

- 個別のメッセージパラメーターを持つ最大50件の特定の`external_ids`
- Brazeダッシュボードで作成された任意のサイズのセグメント（`segment_id`で指定）
- リクエスト内で[コネクテッドオーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience)オブジェクトとして定義された、任意のサイズの追加オーディエンスフィルターに一致するユーザー

### バッチリクエストの例 {#example-batch-request}

以下の例では、`external_id`を使用してメールとSMSに対して1回のAPI呼び出しを行います。

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

## レート制限の監視 {#monitoring-your-rate-limits}

Brazeに送信されるすべてのAPIリクエストは、レスポンスヘッダーに以下の情報を返します。

| ヘッダー名             | 説明                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | 指定された間隔で行うことができるリクエストの最大数（レート制限）。 |
| `X-RateLimit-Remaining` | 現在のレート制限ウィンドウで残っているリクエスト数。                          |
| `X-RateLimit-Reset`     | 現在のレート制限ウィンドウがリセットされる時刻（UTCエポック秒）。                |
{: .reset-td-br-1 .reset-td-br-2 aria-label="レート制限の監視" }

この情報は、Brazeダッシュボードではなく、APIリクエストへのレスポンスのヘッダーに意図的に含まれています。これにより、APIとやり取りする際にシステムがリアルタイムでより適切に対応できるようになります。たとえば、`X-RateLimit-Remaining`の値が特定のしきい値を下回った場合、すべてのトランザクションメールが確実に送信されるよう、送信速度を落とすことができます。また、値がゼロに達した場合は、`X-RateLimit-Reset`で指定された時刻が経過するまですべての送信を一時停止することもできます。

{% alert note %}
HTTPヘッダーはすべて小文字で返されます。この動作は、すべてのヘッダーフィールド名を小文字にすることを義務付けるHTTP/2プロトコルに準拠しています。これは、ヘッダー名が大文字小文字を区別しないものの、さまざまな大文字表記で記述されることが一般的だったHTTP/1.Xとは異なります。
{% endalert %}

APIの制限について質問がある場合は、カスタマーサクセスマネージャーに連絡するか、[サポートチケット]({{site.baseurl}}/user_guide/administer/personal/braze_support)を開いてください。

{% alert tip %}
[API使用状況ダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/api_usage)を使用して、レート制限に対する受信トラフィックを表示・比較できます。
{% endalert %}

### エンドポイント間の最適な遅延 {#optimal-delay-between-endpoints}

{% alert note %}
エラーを最小限に抑えるため、連続するエンドポイント呼び出しの間に5分間の遅延を設けることをお勧めします。
{% endalert %}

Braze APIに対して連続した呼び出しを行う際には、エンドポイント間の最適な遅延を理解することが重要です。エンドポイントが他のエンドポイントの正常な処理に依存している場合、早すぎるタイミングで呼び出すとエラーが発生する可能性があります。たとえば、`/user/alias/new`エンドポイントを通じてユーザーにエイリアスを割り当て、そのエイリアスを使って`/users/track`エンドポイントでカスタムイベントを送信する場合、どのくらい待つべきでしょうか。

通常の条件下では、データの結果整合性が発生するまでの時間は10〜100ミリ秒（1/10秒）です。ただし、整合性の確立に時間がかかる場合もあるため、エラーの発生確率を最小限に抑えるために、後続の呼び出しの間に5分間の遅延を設けることをお勧めします。

## ペイロードサイズ制限 {#payload-size-limits}

Braze APIリクエストには、レート制限とは別にペイロードサイズ制限が適用されます。ほとんどのエンドポイントは、最大4&nbsp;MBのリクエストボディを受け付けます。リクエストが該当する制限を超えた場合、Brazeはエンドポイントに応じてHTTP `413 Request Entity Too Large` またはHTTP `400 Bad Request` で拒否する場合があります。

[`/users/track/bulk`]({{site.baseurl}}/api/endpoints/user_data/post_user_track_bulk) エンドポイントには2&nbsp;MBのペイロード制限があり、リクエストボディがその制限を超えるとHTTP `400` を返します。エンドポイント固有の制限とエラーハンドリングについては、[ユーザーデータエンドポイント]({{site.baseurl}}/api/endpoints/user_data)を参照してください。

### レート制限のリセット {#rate-limit-reset}

レート制限はローリングウィンドウではなく、正時（時計の時刻）でリセットされます。たとえば、制限が1時間あたり250,000リクエストの場合、午後10時00分から午後10時59分の間に50,000リクエストを送信し、午後11時00分から午後11時59分の間にさらに250,000リクエストを送信できます。これはカウンターが各時間の正時にリセットされるためです。