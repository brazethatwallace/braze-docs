---
nav_title: "API 개요"
article_title: "API 개요"
page_order: 2.1
description: "이 참조 문서에서는 REST API가 무엇인지, 용어, API 키에 대한 개요를 포함하여 API 기본 사항을 다룹니다."
page_type: reference
alias: /api/api_key/
---

# API 개요 {#api-overview}

> 이 참조 문서는 API 기본 사항, 일반 용어 및 REST API 키, 권한 및 이를 안전하게 유지하는 방법에 대한 개요를 다룹니다.

## Braze REST API 컬렉션 {#braze-rest-api-collection}

| 컬렉션                                                                     | 용도                                                                                   |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [카탈로그]({{site.baseurl}}/api/endpoints/catalogs)                       | Braze Campaigns에서 참조할 카탈로그 및 카탈로그 항목을 생성하고 관리합니다.    |
| [클라우드 데이터 수집]({{site.baseurl}}/api/endpoints/cdi)                | 데이터 웨어하우스 통합 및 동기화를 관리합니다.                                    |
| [이메일 목록 및 주소]({{site.baseurl}}/api/endpoints/email)         | Braze와 이메일 시스템 간의 양방향 동기화를 설정하고 관리합니다.           |
| [내보내기]({{site.baseurl}}/api/endpoints/export)                           | Campaigns, Canvases, 핵심 성과 지표(KPI) 등의 다양한 세부 정보에 액세스하고 내보냅니다.        |
| [미디어 라이브러리]({{site.baseurl}}/api/endpoints/media_library)             | Braze 내 에셋을 관리합니다.                                                           |
| [메시지]({{site.baseurl}}/api/endpoints/messaging)                      | Campaigns와 Canvases를 예약하고 전송하며 관리합니다.                               |
| [환경설정 센터]({{site.baseurl}}/api/endpoints/preference_center)     | 환경설정 센터를 구축하고 스타일을 업데이트합니다.                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim)                               | 클라우드 기반 애플리케이션 및 서비스에서 사용자 ID를 관리합니다.                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms)                                 | 구독 그룹 내 사용자의 전화번호를 관리합니다.                         |
| [구독 그룹]({{site.baseurl}}/api/endpoints/subscription_groups) | Braze 대시보드에 저장된 SMS 및 이메일 구독 그룹을 조회하고 업데이트합니다. |
| [템플릿]({{site.baseurl}}/api/endpoints/templates)                     | 이메일 메시징 및 Content Blocks용 템플릿을 생성하고 업데이트합니다.                   |
| [사용자 데이터]({{site.baseurl}}/api/endpoints/user_data)                     | 사용자를 식별하고 추적하며 관리합니다.                                               |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze REST API 컬렉션" }

## API 정의 {#api-definitions}

다음은 Braze REST API 설명서에서 볼 수 있는 용어에 대한 개요입니다.

### 엔드포인트 {#endpoints}

Braze는 대시보드와 REST 엔드포인트를 위해 여러 인스턴스를 관리합니다. 계정이 프로비저닝되면 다음 URL 중 하나에 로그인하게 됩니다. 프로비저닝된 인스턴스에 맞는 올바른 REST 엔드포인트를 사용하세요. 확실하지 않은 경우 [지원 티켓]({{site.baseurl}}/user_guide/administer/personal/braze_support)을 열거나 다음 표를 참조하여 사용 중인 대시보드 URL에 맞는 올바른 REST 엔드포인트를 확인하세요.

Braze에서 REST 엔드포인트를 확인하는 방법:

1. Braze에 로그인하고 **설정** > **API 및 식별자** > **API 키**로 이동합니다.
2. 기존 API 키를 선택하거나 **API 키 생성**을 선택하여 새 키를 만듭니다.
3. 이 탭에 표시된 REST 엔드포인트를 복사하여 API 요청에 사용합니다.

{% alert important %}
API 호출에 엔드포인트를 사용할 때는 REST 엔드포인트를 사용하세요.

SDK 통합의 경우 REST 엔드포인트가 아닌 [SDK 엔드포인트]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)를 사용하세요.
{% endalert %}

{% multi_lang_include administer/data_centers.md datacenters='instances' %}

### API 사용량 제한 {#api-limits}

대부분의 API에 대해 Braze는 시간당 250,000건의 기본 사용량 제한을 적용합니다. 그러나 특정 요청 유형에는 고객 기반 전체에서 대량의 데이터를 더 효과적으로 처리하기 위해 자체 사용량 제한이 적용됩니다. 자세한 내용은 [API 사용량 제한]({{site.baseurl}}/api/api_limits)을 참조하세요.

### 사용자 ID {#user-ids}

- **외부 사용자 ID**: `external_id`는 데이터를 제출하는 대상 사용자의 고유 식별자 역할을 합니다. 이 식별자는 동일한 사용자에 대해 여러 프로필이 생성되는 것을 방지하기 위해 Braze SDK에서 설정한 것과 동일해야 합니다.
- **Braze 사용자 ID**: `braze_id`는 Braze에서 설정하는 고유 사용자 식별자 역할을 합니다. 이 식별자를 사용하여 external_ids 외에도 REST API를 통해 사용자를 삭제할 수 있습니다.

자세한 내용은 플랫폼에 따른 다음 문서를 참조하세요: [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [웹]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).

## REST API 키 소개 {#about-rest-api-keys}

REST API(Application Programming Interface) 키는 API에 전달하여 API 호출을 인증하고 호출 애플리케이션 또는 사용자를 식별하는 고유 코드입니다. 회사의 REST API 엔드포인트에 대한 HTTPS 웹 요청을 사용하여 API에 접근합니다. REST API 키는 앱 식별자 키와 함께 작동하여 데이터를 추적, 접근, 전송, 내보내기 및 분석하여 모든 것이 원활하게 실행되도록 합니다.

워크스페이스와 API 키는 Braze에서 밀접하게 연결되어 있습니다. 워크스페이스는 여러 플랫폼에 걸쳐 동일한 애플리케이션의 버전을 수용하도록 설계되었습니다. 많은 고객이 동일한 플랫폼에서 무료 및 프리미엄 버전의 애플리케이션을 포함하기 위해 워크스페이스를 사용하기도 합니다. 이러한 워크스페이스도 REST API를 활용하며 자체 REST API 키를 가지고 있습니다. 이러한 키는 API의 특정 엔드포인트에 대한 접근을 포함하도록 개별적으로 범위를 지정할 수 있습니다. API에 대한 각 호출에는 해당 엔드포인트에 대한 접근 권한이 있는 키가 포함되어야 합니다.

REST API 키와 워크스페이스 API 키를 모두 `api_key`라고 합니다. `api_key`는 각 요청에 요청 헤더로 포함되며, REST API를 사용할 수 있도록 인증 키 역할을 합니다. 이러한 REST API는 사용자 추적, 메시지 전송, 사용자 데이터 내보내기 등에 사용됩니다. 새 REST API 키를 생성할 때 특정 엔드포인트에 대한 접근 권한을 부여해야 합니다. API 키에 특정 권한을 할당하면 API 키가 인증할 수 있는 호출을 정확하게 제한할 수 있습니다.

![API Keys 탭의 REST API 키 패널.]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
REST API 키 외에도 API에서 앱, 템플릿, Canvases, Campaigns, Content Cards, Segments 같은 특정 항목을 참조하는 데 사용할 수 있는 식별자 키라는 유형의 키도 있습니다. 자세한 내용은 [API 식별자 유형]({{site.baseurl}}/api/identifier_types)을 참조하세요.
{% endalert %}

### REST API 키 생성 {#creating-rest-api-keys}

새 REST API 키를 생성하려면 다음 단계를 따르세요.

1. **설정** > **API 및 식별자**로 이동합니다.
2. **API 키 생성**을 선택합니다.
3. 한눈에 식별할 수 있도록 새 키에 이름을 지정합니다.
4. 새 키에 대한 [허용 IP 주소](#api-ip-allowlisting)와 서브넷을 지정합니다.
5. 새 키에 연결할 [권한](#rest-api-key-permissions)을 선택합니다.

{% alert important %}
새 API 키를 생성한 후에는 권한 범위나 허용 IP를 편집할 수 없습니다. 이 제한은 보안상의 이유로 적용됩니다. 키의 범위를 변경해야 하는 경우 업데이트된 권한으로 새 키를 생성하고 기존 키 대신 해당 키를 구현하세요. 구현이 완료되면 이전 키를 삭제할 수 있습니다.
{% endalert %}

### REST API 키 권한 {#rest-api-key-permissions}

API 키 권한은 사용자 또는 그룹에 할당하여 특정 API 호출에 대한 접근을 제한할 수 있는 권한입니다. API 키 권한 목록을 보려면 **설정** > **API 및 식별자**로 이동하여 API 키를 선택하세요.

{% tabs %}
{% tab 사용자 데이터 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | 사용자 속성, 커스텀 이벤트, 구매를 기록합니다. |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) | 모든 사용자를 삭제합니다. |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias) | 기존 사용자에 대한 새 별칭을 생성합니다. |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) | 외부 ID로 별칭 전용 사용자를 식별합니다. |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | 사용자 ID로 고객 프로필 정보를 쿼리합니다. |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) | Segment별로 고객 프로필 정보를 쿼리합니다. |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) | 두 기존 사용자를 하나로 병합합니다. |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename) | 기존 사용자의 외부 ID를 변경합니다. |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) | 기존 사용자의 외부 ID를 제거합니다. |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update) | 기존 사용자의 별칭을 업데이트합니다. |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group) | 글로벌 컨트롤 그룹의 고객 프로필 정보를 쿼리합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

 {% endtab %}
 {% tab 이메일 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses) | 탈퇴한 이메일 주소를 쿼리합니다. |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status) | 이메일 주소 상태를 변경합니다. |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces) | 하드 바운스된 이메일 주소를 쿼리합니다. |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces) | 하드 바운스 목록에서 이메일 주소를 제거합니다. |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam) | 스팸 목록에서 이메일 주소를 제거합니다. |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist) | 이메일 주소를 차단 목록에 추가합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab 메시지 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | 특정 사용자에게 즉시 메시지를 보냅니다. |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages) | 특정 시간에 보낼 메시지를 예약합니다. |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages) | 예약된 메시지를 업데이트합니다. |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages) | 예약된 메시지를 삭제합니다. |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | 모든 예약된 브로드캐스트 메시지를 쿼리합니다. |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) | iOS 라이브 액티비티를 업데이트합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab Campaigns %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) | 기존 Campaign의 발송을 트리거합니다. |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) | API 트리거 전송으로 Campaign 발송을 예약합니다. |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns) | API 트리거 전송으로 예약된 Campaign을 업데이트합니다. |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages) | API 트리거 전송으로 예약된 Campaign을 삭제합니다. |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | Campaign 목록을 쿼리합니다. |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | 특정 기간 동안의 Campaign 분석 데이터를 쿼리합니다. |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | 특정 Campaign의 세부 정보를 쿼리합니다. |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | 특정 기간 동안의 메시지 전송 분석 데이터를 쿼리합니다. |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids) | 메시지 대량 발송 추적을 위한 전송 ID를 생성합니다. |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | Campaign 내 특정 메시지 배리언트의 URL 세부 정보를 쿼리합니다. |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) | 트랜잭션 메시징 엔드포인트를 사용하여 트랜잭션 메시지를 보낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab Canvas %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) | 기존 Canvas의 발송을 트리거합니다. |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) | API 트리거 전송으로 Canvas 발송을 예약합니다. |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases) | API 트리거 전송으로 예약된 Canvas를 업데이트합니다. |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases) | API 트리거 전송으로 예약된 Canvas를 삭제합니다. |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | Canvases 목록을 쿼리합니다. |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | 특정 기간 동안의 Canvas 분석 데이터를 쿼리합니다. |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | 특정 Canvas의 세부 정보를 쿼리합니다. |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | 특정 기간 동안의 Canvas 분석 데이터 요약을 쿼리합니다. |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias) | 캔버스 단계 내 특정 메시지 배리언트의 URL 세부 정보를 쿼리합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab Segments %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Segments 목록을 쿼리합니다. |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | 특정 기간 동안의 Segment 분석 데이터를 쿼리합니다. |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | 특정 Segment의 세부 정보를 쿼리합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab 구매 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | 앱에서 구매된 제품 목록을 쿼리합니다. |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | 특정 기간 동안 앱에서 일별 총 지출 금액을 쿼리합니다. |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | 특정 기간 동안 앱에서 일별 총 구매 수를 쿼리합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab 이벤트 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | 커스텀 이벤트 목록을 쿼리합니다. |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | 특정 기간 동안의 커스텀 이벤트 발생 횟수를 쿼리합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab 세션 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | 특정 기간 동안의 일별 세션 수를 쿼리합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab 핵심 성과 지표(KPI) %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | 특정 기간 동안의 일별 고유 활성 사용자 수를 쿼리합니다. |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | 특정 기간 동안 30일 롤링 윈도우 기준 총 고유 활성 사용자 수를 쿼리합니다. |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | 특정 기간 동안의 일별 신규 사용자 수를 쿼리합니다. |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | 특정 기간 동안의 일별 앱 제거 수를 쿼리합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab 템플릿 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | 대시보드에 새 이메일 템플릿을 생성합니다. |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | 특정 템플릿의 정보를 쿼리합니다. |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | 이메일 템플릿 목록을 쿼리합니다. |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | 대시보드에 저장된 이메일 템플릿을 업데이트합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab SSO %}

| 권한 | 설명 |
| --- | --- |
| `sso.saml.login` | ID 제공자 시작 로그인을 설정합니다. 자세한 내용은 [서비스 제공자(SP) 시작 로그인]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="REST API 키 권한" }

{% endtab %}
{% tab Content Blocks %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | 특정 템플릿의 정보를 쿼리합니다. |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | Content Blocks 목록을 쿼리합니다. |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | 대시보드에 새 콘텐츠 블록을 생성합니다. |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | 대시보드의 기존 콘텐츠 블록을 업데이트합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab 환경 설정 센터 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | 환경 설정 센터를 가져옵니다. |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | 환경 설정 센터 목록을 조회합니다. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center) | 환경 설정 센터를 생성하거나 업데이트합니다. |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | 사용자의 환경 설정 센터 링크를 가져옵니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab 구독 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) | 구독 그룹 상태를 설정합니다. |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | 구독 그룹 상태를 가져옵니다. |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | 특정 사용자가 명시적으로 가입 및 탈퇴한 구독 그룹의 상태를 가져옵니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab SMS %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers) | 유효하지 않은 전화번호를 쿼리합니다. |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers) | 사용자로부터 유효하지 않은 전화번호 플래그를 제거합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab 카탈로그 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | 기존 카탈로그에 여러 항목을 추가합니다. |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | 기존 카탈로그의 여러 항목을 업데이트합니다. |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | 기존 카탈로그에서 여러 항목을 삭제합니다. |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | 기존 카탈로그에서 단일 항목을 가져옵니다. |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item) | 기존 카탈로그의 단일 항목을 업데이트합니다. |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item) | 기존 카탈로그에 단일 항목을 생성합니다. |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item) | 기존 카탈로그에서 단일 항목을 삭제합니다. |
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item) | 기존 카탈로그의 단일 항목을 교체합니다. |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | 카탈로그를 생성합니다. |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | 카탈로그 목록을 가져옵니다. |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | 카탈로그를 삭제합니다. |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | 기존 카탈로그에서 항목 미리보기를 가져옵니다. |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | 기존 카탈로그의 항목을 교체합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% tab SDK 인증 %}

| 권한 | 엔드포인트 | 설명 |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | 앱에 대한 새 SDK 인증 키를 생성합니다. |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key) | SDK 인증 키를 앱의 기본 키로 지정합니다. |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | 앱의 SDK 인증 키를 삭제합니다. |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | 앱의 모든 SDK 인증 키를 가져옵니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키 권한" }

{% endtab %}
{% endtabs %}

### REST API 키 관리 {#managing-rest-api-keys}

**설정** > **API 및 식별자** > **API 키** 탭에서 기존 REST API 키의 세부 정보를 보거나 삭제할 수 있습니다. REST API 키는 생성 후 편집할 수 없습니다.

**API 키** 탭에는 각 키에 대해 다음 정보가 포함됩니다.

| 필드 | 설명 |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| API 키 이름 | 생성 시 키에 지정된 이름입니다. |
| 식별자 | API 키입니다. |
| 생성자 | 키를 생성한 사용자의 이메일 주소입니다. 2023년 6월 이전에 생성된 키의 경우 이 필드에 "N/A"로 표시됩니다. |
| 생성일 | 이 키가 생성된 날짜입니다. |
| 마지막 확인 | 이 키가 마지막으로 사용된 날짜입니다. 한 번도 사용되지 않은 키의 경우 이 필드에 "N/A"로 표시됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="REST API 키 관리" }

API 키의 세부 정보를 보려면 키 위에 마우스를 올리고 <i class="fa-solid fa-eye" alt="보기"></i> **보기**를 선택합니다. 여기에는 이 키가 가진 모든 권한, 화이트리스트에 등록된 IP(있는 경우), 이 키가 Braze IP 화이트리스팅에 옵트인되었는지 여부가 포함됩니다.

![Braze 대시보드의 API 키 권한 목록.]({% image_buster /assets/img_archive/view-api-key.png %})

[사용자를 삭제]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users)해도 Braze는 해당 사용자가 생성한 관련 API 키를 삭제하지 않습니다. 키를 삭제하려면 키 위에 마우스를 올리고 <i class="fa-solid fa-trash-can" alt="삭제"></i> **삭제**를 선택합니다.

![휴지통 아이콘이 강조 표시된 'Last Seen'이라는 이름의 API 키로, '삭제'가 표시됩니다.]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### REST API 키 보안 {#rest-api-key-security}

API 키는 API 호출을 인증하는 데 사용됩니다. 새 REST API 키를 생성할 때 특정 엔드포인트에 대한 접근 권한을 부여해야 합니다. API 키에 특정 권한을 할당하면 API 키가 인증할 수 있는 호출을 정확하게 제한할 수 있습니다.

REST API 키는 민감할 수 있는 REST API 엔드포인트에 대한 접근을 허용하므로, 이러한 키를 안전하게 보관하고 신뢰할 수 있는 파트너에게만 공유하세요. 키는 절대 공개적으로 노출되어서는 안 됩니다. 예를 들어, 웹사이트에서 AJAX 호출을 하거나 다른 공개적인 방식으로 이 키를 노출하지 마세요.

좋은 보안 관행은 사용자에게 업무 수행에 필요한 만큼만 접근 권한을 부여하는 것입니다. 이 원칙은 각 키에 권한을 할당하여 API 키에도 적용할 수 있습니다. 이러한 권한은 계정의 다양한 영역에 대한 더 나은 보안과 제어를 제공합니다.

{% alert warning %}
REST API 키는 민감할 수 있는 REST API 엔드포인트에 대한 접근을 허용하므로, 안전하게 저장하고 사용해야 합니다. 예를 들어, 웹사이트에서 AJAX 호출을 하거나 다른 공개적인 방식으로 이 키를 노출하지 마세요.
{% endalert %}

실수로 키가 노출된 경우 개발자 콘솔에서 삭제할 수 있습니다. 이 과정에 대한 도움이 필요하면 [지원 티켓]({{site.baseurl}}/user_guide/administer/personal/braze_support)을 생성하세요.

### REST API 키와 SDK API 키의 보안 {#security-of-rest-api-keys-and-sdk-api-keys}

REST API 키와 SDK API 키는 보안 프로필이 다릅니다.

| | REST API 키 | SDK API 키 |
|---|---|---|
| 용도 | REST API에 대한 서버 측 인증(메시지 전송, 데이터 내보내기, 사용자 관리) | Braze SDK에 대한 클라이언트 측 식별(데이터 수집, In-App Messages, Content Cards) |
| 공개 범위 | **비공개로 유지해야 합니다**. 클라이언트 측 코드, 공개 리포지토리 또는 사용자 애플리케이션에 절대 노출하지 마세요. | 공개적으로 사용하도록 설계되었습니다. 앱 바이너리에 번들되거나 웹 브라우저 JavaScript에서 볼 수 있으며, Google Analytics 추적 ID와 유사합니다. |
| 노출 시 조치 | 즉시 키를 폐기하고 **설정** > **API 및 식별자** > **API 키**에서 대체 키를 생성하세요. 노출된 REST API 키는 메시지 전송, 사용자 데이터 내보내기 또는 계정 설정 수정에 사용될 수 있습니다. | 조치가 필요하지 않습니다. SDK API 키는 데이터 수집과 클라이언트 측 메시징(예: In-App Messages 및 Content Cards) 검색만 가능합니다. 사용자 데이터를 내보내거나, 메시지를 대신 보내거나, Campaign을 수정할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST API 키와 SDK API 키의 보안" }

### API IP 허용 목록 {#api-ip-allowlisting}

추가 보안을 위해 특정 REST API 키에 대해 REST API 요청을 허용할 IP 주소와 서브넷 목록을 지정할 수 있습니다. 이를 허용 목록 또는 화이트리스트라고 합니다. 특정 IP 주소 또는 서브넷을 허용하려면 새 REST API 키를 생성할 때 **Whitelist IPs** 섹션에 추가하세요.

![새 API 키 생성 시 IP 허용 목록 옵션.]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

아무것도 지정하지 않으면 모든 IP 주소에서 요청을 보낼 수 있습니다.

{% alert tip %}
Braze 간 웹훅을 만들면서 허용 목록을 사용하는 경우 [화이트리스트에 추가할 IP]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) 목록을 확인하세요.
{% endalert %}

## API 인증 및 보안 {#api-authentication-and-security}

### Bearer 토큰 인증 {#bearer-token-authentication}

Braze는 `Authorization` 요청 헤더에 Bearer 토큰으로 전달되는 REST API 키를 사용하여 REST API 요청을 인증합니다. 요청을 보낼 때 다음 형식으로 API 키를 포함하세요:

```bash
Authorization: Bearer YOUR_REST_API_KEY
```

각 요청에 대해 Braze는 다음과 같은 서버 측 유효성 검사를 수행합니다:

1. **토큰 유효성:** REST API 키가 Braze에 존재하며 활성 상태인지(예: 해지되거나 비활성화되지 않았는지) 확인합니다.
2. **토큰 권한:** API 키가 요청된 엔드포인트에 대해 필요한 권한을 가지고 있는지 확인합니다.

인증이 실패하면 API는 HTTP 상태 코드와 함께 오류 응답을 반환합니다. 예를 들어, `401 Unauthorized`는 유효하지 않거나 누락된 키를 나타내고, `403 Forbidden`은 해당 키가 요청된 엔드포인트에 대한 권한이 없음을 나타냅니다. 자세한 내용은 [API 오류]({{site.baseurl}}/api/errors)를 참조하세요.

### 요청 헤더 대소문자 {#header-casing}

HTTP 헤더 이름은 대소문자를 구분하지 않으므로 `Authorization`과 `authorization`은 동일하게 취급됩니다. `Content-Type`과 같은 다른 표준 요청 헤더도 마찬가지입니다. HTTP 클라이언트가 생성하는 대소문자 형식을 그대로 전송하면 됩니다.

Braze는 `Bearer` 스킴의 모든 대소문자 표기(`Bearer`, `bearer`, 또는 `BEARER`)를 허용합니다. REST API 키 자체는 발급된 그대로 정확히 전송하세요.

### 네트워크 수준 보안 {#network-level-security}

Braze에 대한 REST API 요청은 전체 요청 경로에 걸쳐 TLS(Transport Layer Security) 암호화로 보호됩니다. 다음 표는 서버에서 Braze로의 API 요청에 대한 네트워크 흐름을 설명합니다:

| 단계 | 구성 요소 | 설명 |
| --- | --- | --- |
| 1 | 사용자 서버 | TLS 암호화를 사용하여 HTTPS 요청을 시작합니다. |
| 2 | Cloudflare | 클라이언트 TLS 연결을 종료하고 네트워크 수준 보호를 적용합니다. |
| 3 | 네트워크 로드 밸런서(NLB) | 패킷을 애플리케이션 인프라로 전달합니다. NLB는 Layer 4에서 동작하므로 Layer 7 프록시가 없습니다. 패킷은 HTTP 수준의 검사나 수정 없이 전달됩니다. |
| 4 | NGINX 인그레스 | 내부 TLS 연결을 종료하고 요청을 라우팅합니다. |
| 5 | Unicorn(애플리케이션 서버) | 인증된 요청을 처리합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="네트워크 수준 보안" }

TLS 암호화는 체인의 모든 구간을 보호합니다. 사용자 서버는 TLS를 통해 Cloudflare에 연결되고, Cloudflare는 NLB를 거쳐 NGINX 인그레스까지 별도의 TLS 연결을 수립하므로 API 키와 요청 데이터는 전송 중에 암호화된 상태를 유지합니다.

## 추가 리소스 {#additional-resources}

### Ruby 클라이언트 라이브러리 {#ruby-client-library}

Ruby를 사용하여 Braze를 구현하는 경우, [Ruby 클라이언트 라이브러리](https://github.com/braze-inc/braze-api-client-ruby)를 사용하여 데이터 가져오기 시간을 줄일 수 있습니다. 클라이언트 라이브러리는 특정 프로그래밍 언어(이 경우 Ruby)에 특화된 코드 모음으로, API를 더 쉽게 사용할 수 있도록 도와줍니다.

Ruby 클라이언트 라이브러리는 [사용자 엔드포인트]({{site.baseurl}}/api/endpoints/user_data)를 지원합니다.

{% alert important %}
이 클라이언트 라이브러리는 베타 버전입니다. 이 라이브러리를 개선하는 데 도움이 되도록, [smb-product@braze.com](mailto:smb-product@braze.com)으로 피드백을 보내주세요.
{% endalert %}