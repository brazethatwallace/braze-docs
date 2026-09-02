---
nav_title: 사용량 제한
article_title: 사용량 제한
page_order: 4.5
description: "이 참조 문서는 Braze API 인프라에 대한 API 사용량 제한을 다룹니다."
page_type: reference
---

# 사용량 제한 {#rate-limits}

> Braze API 인프라는 고객 기반 전체에서 대량의 데이터를 처리하도록 설계되었습니다. 이를 위해 워크스페이스별로 API 사용량 제한을 적용합니다.

사용량 제한은 API가 주어진 시간 동안 수신할 수 있는 요청의 수입니다. 대규모 시스템에서 발생하는 부하 기반 서비스 거부 사고의 대부분은 악의적인 공격이 아닌 소프트웨어 또는 구성 오류로 인해 의도치 않게 발생합니다. 사용량 제한은 이러한 오류로 인해 고객이 Braze API 리소스를 사용하지 못하는 상황을 방지합니다. 지정된 시간 프레임 내에 너무 많은 요청이 전송되면, `429` 상태 코드와 함께 오류 응답이 표시될 수 있으며, 이는 사용량 제한에 도달했음을 나타냅니다.

{% alert warning %}
API 사용량 제한은 시스템의 적절한 사용에 따라 변경될 수 있습니다. 손상이나 오용을 방지하기 위해 API 호출 시 합리적인 제한을 두는 것이 좋습니다.
{% endalert %}

## 요청 유형별 사용량 제한 {#rate-limits-by-request-type}

다양한 요청 유형의 기본 API 사용량 제한에 대해서는 아래를 참고하세요. 이러한 기본 제한은 요청 시 증가할 수 있습니다. 자세한 내용은 고객 성공 매니저에게 문의하세요.

### 개별 사용량 제한이 적용되는 요청 {#requests-with-different-rate-limits}

| 요청 유형 | 기본 API 사용량 제한 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | **요청:** 사용량 제한은 계약에 따라 다릅니다. 가격 책정에 데이터 포인트가 포함된 고객의 경우, Braze는 3초당 3,000건의 버스트 제한을 적용합니다. 그 외 모든 고객의 경우, 계약 조건에 따라 제한이 설정됩니다. 제한에 대한 질문은 Braze 지원팀 또는 고객 성공 매니저에게 문의하세요.<br><br>**일괄 처리:** API 요청당 `attributes`, `events`, `purchases` 전체에서 최대 75개의 오브젝트를 결합할 수 있습니다. 레거시 사용량 제한을 적용받는 고객은 배열별로 최대 75개의 오브젝트를 독립적으로 포함할 수 있습니다. 자세한 내용은 [User Track 요청 일괄 처리](#batch-user-track)를 참고하세요.<br><br>**월간 활성 사용자 CY 24-25, 유니버설 MAU, 웹 MAU, 모바일 MAU 제한:** [월간 활성 사용자 CY 24-25 제한]({{site.baseurl}}/api/endpoints/user_data/post_user_track#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau)을 참고하세요. |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | **2024년 8월 22일 이후에 온보딩한 경우:** 분당 250건의 요청. <br><br> **2024년 8월 22일 이전에 온보딩한 경우:** 분당 2,500건의 요청. |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)<br>[`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias)<br>[`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update)<br>[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)<br>[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) | 분당 20,000건의 요청이며, 엔드포인트 간에 공유됩니다. |
| [`/users/external_id/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename) | 분당 1,000건의 요청. |
| [`/users/external_id/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) | 분당 1,000건의 요청. |
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | 시간당 1,000건의 요청이며, `/purchases/product_list` 엔드포인트와 공유됩니다. |
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | 시간당 1,000건의 요청이며, `/events/list` 엔드포인트와 공유됩니다. |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | 분당 50,000건의 요청. |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)<br>[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)<br>[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)<br>[`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)<br>[`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) | 브로드캐스트 호출(Segments, 필터 또는 연결된 오디언스를 광범위하게 타겟팅하는 경우)의 경우, 전체 오디언스에 걸쳐 분당 250건의 요청, 그리고 [고유 오디언스]({{site.baseurl}}/api/api_limits#what-counts-as-the-same-unique-audience)당 분당 10건의 요청(둘 중 먼저 도달하는 제한이 적용됩니다).<br><br>그 외 개별 수신자를 타겟팅하는 경우, 해당 요청은 시간당 250,000건의 [공유 사용량 제한]({{site.baseurl}}/api/api_limits#requests-with-shared-rate-limits)에 포함됩니다. |
| [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids) | 일당 100건의 요청. |
| [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) | 분당 5,000건의 요청. |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center)<br>[`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | 분당 1,000건의 요청. |
| [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center) | 분당 10건의 요청. |
| [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | 분당 50건의 요청이며, 엔드포인트 간에 공유됩니다. |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | 분당 16,000건의 요청이며, 엔드포인트 간에 공유됩니다. |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item) | 분당 50건의 요청이며, 엔드포인트 간에 공유됩니다. |
| [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)<br>[`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)<br>[`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)<br>[`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | 분당 50건의 요청이며, 엔드포인트 간에 공유됩니다. |
| [`/scim/v2/Users/{id}`]({{site.baseurl}}/get_see_user_account_information)<br>[`/scim/v2/Users?filter={userName@example.com}`]({{site.baseurl}}/get_search_existing_dashboard_user_email)<br>[`/scim/v2/Users/{id}`]({{site.baseurl}}/post_update_existing_user_account)<br>[`/scim/v2/Users/{id}}`]({{site.baseurl}}/delete_existing_dashboard_user)<br>[`/scim/v2/Users/`]({{site.baseurl}}/post_create_user_account) | 일당 회사당 5,000건의 요청이며, 엔드포인트 간에 공유됩니다. |
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | 분당 50건의 요청. |
| [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | 분당 20건의 요청. |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) | 분당 100건의 요청. |
| [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | 시간당 100건의 요청. |
| [`/media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file) | 시간당 100건의 요청. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="개별 사용량 제한이 적용되는 요청" }

### 공유 사용량 제한이 적용되는 요청 {#requests-with-shared-rate-limits}

다음 요청에는 시간당 250,000건의 사용량 제한이 적용되며, 엔드포인트 간에 공유됩니다.

- [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key)
- [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys)
- [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) (비브로드캐스트 호출에만 해당&#8212;`external_user_ids` 또는 `aliases`를 지정하는 경우)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) (비브로드캐스트 호출에만 해당)
- [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages)
- [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns)
- [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)
- [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary)
- [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details)
- [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) (비브로드캐스트 호출에만 해당)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) (비브로드캐스트 호출에만 해당)
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
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) (비브로드캐스트 호출에만 해당)
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

### 동일한 고유 오디언스로 간주되는 기준 {#what-counts-as-the-same-unique-audience}

이 내용은 다음 엔드포인트에 적용됩니다: [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages), [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns), [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases), [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns), [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases).

이러한 엔드포인트에서 브로드캐스트 요청은 다음 항목이 모두 일치하는 경우 동일한 고유 오디언스를 타겟팅하는 것으로 간주됩니다:

- 트리거되는 Campaign 또는 Canvas(API 요청의 `campaign_id` 또는 `canvas_id`(지정된 경우))
- 타겟팅되는 오디언스(Segments 또는 필터, 또는 API Campaign의 경우 API 요청의 `segment_id`)
- 연결된 오디언스 필터(API 요청의 `audience` 오브젝트(지정된 경우))

이러한 속성의 각 고유 조합은 별도의 오디언스로 간주되므로, 각 고유 오디언스에 대한 추가 사용량 제한은 각 조합에 독립적으로 적용됩니다.

## API 요청 일괄 처리 {#batching-api-requests}

Braze API는 일괄 처리(배칭)를 지원하도록 설계되었습니다. 일괄 처리를 사용하면 Braze가 단일 API 호출에서 가능한 한 많은 데이터를 수집할 수 있으므로 많은 API 호출을 수행할 필요가 없습니다. Braze는 한 번에 하나의 호출씩 데이터를 처리하는 것보다 일괄적으로 데이터를 처리하는 것이 더 효율적입니다. 예를 들어, 1,000건의 일괄 API 호출을 처리하는 것이 75,000건의 개별 호출을 처리하는 것보다 리소스를 훨씬 적게 소모합니다. 일괄 처리는 시간당 75,000건 이상의 호출이 필요할 수 있는 모든 애플리케이션에 매우 중요합니다.

{% alert note %}
REST API 사용량 제한 증가는 API 일괄 처리 기능을 활용하는 고객의 필요에 따라 검토됩니다.
{% endalert %}

### 사용자 생성 및 업데이트 엔드포인트에 대한 일괄 요청 {#batch-user-track}

각 `/users/track` 요청에는 `attributes`, `events`, `purchases` 전체를 합산하여 최대 75개의 객체를 포함할 수 있습니다. 각 객체는 한 명의 사용자를 업데이트할 수 있습니다. 단일 고객 프로필은 여러 객체에 의해 업데이트될 수 있습니다.

{% details 레거시 사용량 제한 %}
레거시 사용량 제한이 적용되는 고객의 경우, 각 배열(`attributes`, `events`, `purchases`)에 독립적으로 최대 75개의 객체를 포함할 수 있으며, 요청당 최대 225개의 객체를 합산하여 포함할 수 있습니다.
{% enddetails %}

`/users/track` 사용량 제한에 대한 자세한 내용은 [POST: 사용자 생성 및 업데이트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 참조하세요.

이 엔드포인트에 대한 요청은 일반적으로 다음 순서로 처리되기 시작합니다:

1. 속성
2. 이벤트
3. 구매

### 메시징 엔드포인트 요청 일괄 처리 {#batching-messaging-endpoint-requests}

[메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging)에 대한 단일 요청으로 다음 중 하나에 도달할 수 있습니다:

- 각각 개별 메시지 파라미터를 가진 최대 50개의 특정 `external_ids`
- Braze 대시보드에서 생성된 모든 크기의 Segment(`segment_id`로 지정)
- 요청에서 [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience) 객체로 정의된 모든 크기의 추가 오디언스 필터와 일치하는 사용자

### 일괄 요청 예시 {#example-batch-request}

다음 예시에서는 `external_id`를 사용하여 이메일과 단문 메시지 서비스에 대해 하나의 API 호출을 수행합니다.

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

## 사용량 제한 모니터링 {#monitoring-your-rate-limits}

Braze로 전송되는 모든 API 요청은 응답 헤더에 다음 정보를 반환합니다.

| 헤더 이름             | 설명                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | 지정된 간격 내에서 수행할 수 있는 최대 요청 수(사용량 제한)입니다. |
| `X-RateLimit-Remaining` | 현재 사용량 제한 윈도우에 남아 있는 요청 수입니다.                          |
| `X-RateLimit-Reset`     | 현재 사용량 제한 윈도우가 초기화되는 시간(UTC 에포크 초 단위)입니다.                |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용량 제한 모니터링" }

이 정보는 Braze 대시보드가 아닌 API 요청에 대한 응답 헤더에 의도적으로 포함됩니다. 이를 통해 API와 상호작용하는 동안 시스템이 실시간으로 더 잘 반응할 수 있습니다. 예를 들어, `X-RateLimit-Remaining` 값이 특정 임계값 아래로 떨어지면 모든 트랜잭션 이메일이 전송되도록 발송 속도를 늦출 수 있습니다. 또는 값이 0에 도달하면 `X-RateLimit-Reset`에 지정된 시간이 경과할 때까지 모든 발송을 일시 중지할 수 있습니다.

{% alert note %}
HTTP 헤더는 모두 소문자로 반환됩니다. 이 동작은 모든 헤더 필드 이름이 소문자여야 한다고 규정하는 HTTP/2 프로토콜에 부합합니다. 이는 헤더 이름이 대소문자를 구분하지 않았지만 다양한 대소문자 표기로 작성되던 HTTP/1.X와 다릅니다.
{% endalert %}

API 제한에 대한 질문이 있으시면 고객 성공 매니저에게 문의하거나 [지원 티켓]({{site.baseurl}}/user_guide/administer/personal/braze_support)을 제출하세요.

{% alert tip %}
[API 사용 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/api_usage)를 사용하여 수신 트래픽을 사용량 제한과 비교하고 확인할 수 있습니다.
{% endalert %}

### 엔드포인트 간 최적 지연 시간 {#optimal-delay-between-endpoints}

{% alert note %}
오류를 최소화하기 위해 연속 엔드포인트 호출 사이에 5분의 지연을 두는 것을 권장합니다.
{% endalert %}

Braze API에 연속 호출을 수행할 때 엔드포인트 간 최적 지연 시간을 이해하는 것이 중요합니다. 엔드포인트가 다른 엔드포인트의 성공적인 처리에 의존하는 경우, 너무 빨리 호출하면 오류가 발생할 수 있습니다. 예를 들어, `/user/alias/new` 엔드포인트를 통해 사용자에게 별칭을 할당한 다음, `/users/track` 엔드포인트를 통해 해당 별칭으로 커스텀 이벤트를 전송하는 경우 얼마나 기다려야 할까요?

정상적인 조건에서 데이터의 최종 일관성이 달성되는 시간은 10~100ms(1/10초)입니다. 그러나 일관성이 달성되는 데 더 오래 걸리는 경우도 있으므로, 오류 가능성을 최소화하기 위해 후속 호출 사이에 5분의 지연을 두는 것을 권장합니다.

## 페이로드 크기 제한 {#payload-size-limits}

Braze API 요청에는 사용량 제한과는 별도로 페이로드 크기 제한이 적용됩니다. 대부분의 엔드포인트는 최대 4&nbsp;MB의 요청 본문을 허용합니다. 요청이 해당 제한을 초과하면 엔드포인트에 따라 Braze에서 HTTP `413 Request Entity Too Large` 또는 HTTP `400 Bad Request`로 거부할 수 있습니다.

[`/users/track/bulk`]({{site.baseurl}}/api/endpoints/user_data/post_user_track_bulk) 엔드포인트는 2&nbsp;MB 페이로드 제한이 적용되며, 요청 본문이 해당 제한을 초과하면 HTTP `400`을 반환합니다. 엔드포인트별 제한 및 오류 처리에 대한 자세한 내용은 [사용자 데이터 엔드포인트]({{site.baseurl}}/api/endpoints/user_data)를 참조하세요.

### 사용량 제한 초기화 {#rate-limit-reset}

사용량 제한은 롤링 윈도우가 아닌 정시 기준으로 초기화됩니다. 예를 들어, 시간당 250,000건의 요청 제한이 있는 경우, 오후 10:00부터 오후 10:59 사이에 50,000건의 요청을 보내고, 오후 11:00부터 오후 11:59 사이에 다시 250,000건의 요청을 보낼 수 있습니다. 이는 매 정시에 카운터가 초기화되기 때문입니다.