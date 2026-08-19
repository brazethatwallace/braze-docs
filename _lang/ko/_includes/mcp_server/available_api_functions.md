# Braze MCP 서버 기능 {#braze-mcp-server-functions}

> Braze MCP 서버는 특정 Braze REST API 엔드포인트에 매핑되는 읽기 및 쓰기 도구를 노출합니다. 자세한 내용은 [Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}를 참조하세요.

{% multi_lang_include mcp_server/beta_alert.md %}

## 사전 요구 사항 {#prerequisites}

이 기능을 사용하려면 먼저 [Braze MCP 서버를 설정]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}해야 합니다.

## 사용 가능한 Braze API 기능 {#available-braze-api-functions}

MCP 클라이언트는 이러한 도구를 참조하여 Braze MCP 서버와 상호작용합니다.

### 워크스페이스 {#workspaces}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | 읽기 | 현재 OAuth 액세스 토큰으로 접근할 수 있는 Braze 워크스페이스를 확인합니다. 이 도구를 먼저 호출하세요. 반환된 각 워크스페이스 `id`가 다른 모든 도구에서 필요한 `app_group_id`입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="워크스페이스" }

### Campaigns

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | 읽기 | 이름, Campaign API 식별자, API Campaign 플래그, 태그가 포함된 Campaign 목록을 내보냅니다. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | 읽기 | `campaign_id`로 지정된 Campaign의 관련 정보를 조회합니다. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | 읽기 | 시간 경과에 따른 Campaign 통계의 일별 시리즈(채널별 발송, 열람, 클릭, 전환)를 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaigns" }

### Canvases

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | 읽기 | 이름, Canvas API 식별자, 태그가 포함된 Canvas 목록을 내보냅니다. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | 읽기 | Canvas 메타데이터(이름, 생성 시간, 현재 상태 등)를 내보냅니다. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | 읽기 | Canvas의 시계열 데이터를 내보냅니다. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | 읽기 | Canvas 시계열 데이터의 요약 집계를 내보냅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvases" }

### 카탈로그 {#catalogs}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | 읽기 | 워크스페이스의 카탈로그 목록을 조회합니다. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | 읽기 | 여러 카탈로그 항목과 해당 콘텐츠를 반환합니다. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | 읽기 | 단일 카탈로그 항목과 해당 콘텐츠를 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="카탈로그" }

### 커스텀 속성 {#custom-attributes}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | 읽기 | 앱에 기록된 커스텀 속성을 알파벳순으로 50개씩 내보냅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="커스텀 속성" }

### 커스텀 이벤트 {#custom-events}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | 읽기 | 앱에 기록된 커스텀 이벤트를 알파벳순으로 50개씩 내보냅니다(커서 페이지네이션). |
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | 읽기 | 커스텀 이벤트 이름을 알파벳순으로 250개씩 내보냅니다(페이지 페이지네이션). |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | 읽기 | 지정된 기간 동안의 커스텀 이벤트 발생 횟수를 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="커스텀 이벤트" }

### CDI 통합 {#cdi-integrations}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | 읽기 | 기존 클라우드 데이터 수집 통합 목록을 호출당 10개씩 조회합니다. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | 읽기 | 지정된 CDI 통합의 과거 동기화 상태를 호출당 10개씩 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="CDI 통합" }

### 핵심 성과 지표(KPI)

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | 읽기 | 날짜별 고유 활성 사용자의 일별 시리즈를 조회합니다. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | 읽기 | 30일 롤링 윈도우 기준 고유 활성 사용자의 일별 시리즈를 조회합니다. |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | 읽기 | 날짜별 총 신규 사용자의 일별 시리즈를 조회합니다. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | 읽기 | 날짜별 총 앱 삭제 수의 일별 시리즈를 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="핵심 성과 지표(KPI)" }

### 미디어 라이브러리 {#media-library}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | 생성 | 외부 URL 또는 base64 파일 콘텐츠를 통해 Braze 미디어 라이브러리에 에셋을 업로드합니다. 업로드 모드는 정확히 하나만 제공해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="미디어 라이브러리" }

### 구매 {#purchases}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | 읽기 | 페이지네이션된 제품 ID 목록을 조회합니다. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | 읽기 | 지정된 기간 동안 앱의 총 구매 수를 조회합니다. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | 읽기 | 지정된 기간 동안 앱에서 발생한 총 매출을 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="구매" }

### Segments

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | 읽기 | 이름, Segment API 식별자, 분석 추적 플래그가 포함된 Segment를 내보냅니다. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | 읽기 | `segment_id`로 Segment의 관련 정보를 조회합니다. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | 읽기 | 시간 경과에 따른 Segment의 예상 크기 일별 시리즈를 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Segments" }

### 발송 {#sends}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | 읽기 | 추적된 `send_id`(API Campaign)의 일별 통계를 조회합니다. Braze는 발송 후 14일 동안 발송 분석 데이터를 저장합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="발송" }

### 세션 {#sessions}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | 읽기 | 지정된 기간 동안 앱의 세션 수를 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="세션" }

### 구독 그룹 {#subscription-groups}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | 읽기 | 구독 그룹 내 사용자의 구독 상태를 조회합니다. |
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | 읽기 | 사용자의 구독 그룹 목록을 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="구독 그룹" }

### 템플릿 {#templates}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | 읽기 | Braze 계정에서 사용 가능한 이메일 템플릿 목록을 조회합니다. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | 읽기 | 특정 이메일 템플릿의 정보를 조회합니다. 드래그 앤 드롭 편집기 템플릿은 지원되지 않습니다. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | 생성 | Braze 대시보드에서 이메일 템플릿을 생성합니다. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | 업데이트 | 기존 이메일 템플릿을 업데이트합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="템플릿" }

### Content Blocks

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | 읽기 | 기존 콘텐츠 블록 정보 목록을 조회합니다. |
| `get_content_block_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | 읽기 | 기존 콘텐츠 블록의 정보를 조회하며, 선택적으로 Campaign 또는 Canvas 포함 데이터를 함께 확인할 수 있습니다. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | 생성 | 콘텐츠 블록을 생성합니다. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | 업데이트 | 콘텐츠 블록을 업데이트합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Content Blocks" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}