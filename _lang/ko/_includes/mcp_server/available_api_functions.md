# Braze MCP 서버 기능 {#braze-mcp-server-functions}

> Braze MCP 서버는 특정 Braze REST API 엔드포인트에 매핑되는 API 기능 세트를 노출합니다. Claude 및 Cursor와 같은 MCP 클라이언트는 이러한 기능을 호출하여 비PII 데이터를 검색하고, 적절한 권한이 있는 경우 비PII 쓰기 동작을 수행할 수 있습니다. 더 일반적인 정보는 [Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}를 참조하세요.

{% multi_lang_include mcp_server/beta_alert.md %}

## 필수 조건 {#prerequisites}

이 기능을 사용하려면 먼저 [Braze MCP 서버를 설정]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}해야 합니다.

## 사용 가능한 Braze API 기능 {#available-braze-api-functions}

MCP 클라이언트는 다음 API 기능을 참조하여 Braze MCP 서버와 상호작용합니다.

### 일반 기능 {#general-functions}

이 기능들은 MCP 클라이언트가 사용 가능한 Braze API 기능을 검색하고 실행하는 데 도움을 줍니다.

| 기능 | 설명 |
|----------|-------------|
| `list_functions` | 설명 및 매개변수와 함께 사용 가능한 모든 Braze API 기능을 나열합니다. |
| `call_function` | 제공된 매개변수로 특정 읽기 전용 Braze API 기능을 호출합니다. |
| `call_write_function` | 제공된 매개변수로 특정 쓰기 가능 Braze API 기능을 호출합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="General functions" }

### Campaigns

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | 메타데이터와 함께 Campaign 목록을 내보냅니다. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | 특정 Campaign에 대한 상세 정보를 가져옵니다. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | Campaign에 대한 시계열 분석 데이터를 검색합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campaigns" }

### Canvases

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | 메타데이터와 함께 Canvases 목록을 내보냅니다. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | 특정 Canvas에 대한 상세 정보를 가져옵니다. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | Canvas 성과에 대한 요약 분석을 가져옵니다. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | Canvases에 대한 시계열 분석 데이터를 검색합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canvases" }

### 카탈로그 {#catalogs}

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | 워크스페이스의 카탈로그 목록을 반환합니다. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | 페이지네이션을 지원하여 여러 카탈로그 항목 및 해당 콘텐츠를 반환합니다. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | ID로 특정 카탈로그 항목 및 해당 콘텐츠를 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Catalogs" }

### 클라우드 데이터 수집 {#cloud-data-ingestion}

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) | 기존 CDI 통합 목록을 반환합니다. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/) | 지정된 CDI 통합에 대한 과거 동기화 상태를 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cloud Data Ingestion" }

### Content Blocks

`create_content_block` 및 `update_content_block` 기능은 쓰기 기능입니다. MCP 클라이언트는 `call_write_function`으로 이를 호출해야 하며, API 키에 해당하는 `content_blocks.create` 또는 `content_blocks.update` 권한이 있어야 합니다.

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | 사용 가능한 콘텐츠 블록을 나열합니다. |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | 콘텐츠 블록에 대한 정보를 가져옵니다. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | 콘텐츠 블록을 생성합니다. `name` 및 `content`가 필수입니다. 선택 필드로 `description`, `state`(`active` 또는 `draft`여야 함), `tags`가 있습니다. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | 기존 콘텐츠 블록을 업데이트합니다. `content_block_id`와 하나 이상의 업데이트 가능한 필드(`name`, `content`, `description`, `state`(`active` 또는 `draft`여야 함), `tags`)가 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content Blocks" }

### 커스텀 속성 {#custom-attributes}

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) | 앱에 기록된 커스텀 속성을 내보냅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Custom Attributes" }

### 이벤트 {#events}

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | 앱에 기록된 커스텀 이벤트 목록을 내보냅니다. |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | 커스텀 이벤트에 대한 시계열 데이터를 검색합니다. |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) | 페이지네이션을 지원하는 상세 이벤트 데이터를 가져옵니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Events" }

### KPI {#kpis}

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | 일일 신규 사용자 수 시리즈입니다. |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | 일일 활성 사용자 시계열 데이터입니다. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | 월간 활성 사용자 시계열 데이터입니다. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | 앱 삭제 시계열 데이터입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="KPIs" }

### 미디어 라이브러리 {#media-library}

`create_media_library_asset` 기능은 쓰기 기능입니다. MCP 클라이언트는 `call_write_function`으로 이를 호출해야 하며, API 키에 `media_library.create` 권한이 있어야 합니다.

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) | Braze 미디어 라이브러리에 자산을 업로드합니다. 공개적으로 접근 가능한 URL(`asset_url`) 또는 base64로 인코딩된 파일(`asset_file_base64`) 중 하나를 제공할 수 있지만, 둘 다 동시에 제공할 수는 없습니다. 이미지 크기 제한은 5MB입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Media Library" }

### 메시지 {#messages}

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | 예정된 Campaigns 및 Canvases 목록을 나열합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messages" }

### 환경설정 센터 {#preference-centers}

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | 사용 가능한 환경설정 센터를 나열합니다. |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) | HTML 콘텐츠 및 옵션을 포함한 특정 환경설정 센터의 세부 정보를 봅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Preference Centers" }

### 구매 {#purchases}

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | 페이지네이션된 제품 ID 목록을 내보냅니다. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | 매출 분석 시계열 데이터입니다. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | 구매 수량 시계열 데이터입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Purchases" }

### Segments

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | 분석 추적 상태가 포함된 Segment 목록을 내보냅니다. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | Segment에 대한 시계열 분석 데이터입니다. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | 특정 Segment에 대한 상세 정보입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Segments" }

### 전송 {#sends}

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | 추적된 Campaign 전송에 대한 일일 분석입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sends" }

### 세션 {#sessions}

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | 앱 세션 수에 대한 시계열 데이터입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sessions" }

### SDK 인증 키 {#sdk-authentication-keys}

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/) | 앱에 대한 모든 SDK 인증 키를 나열합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SDK Authentication Keys" }

### 구독 {#subscription}

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | 특정 사용자의 구독 그룹을 나열하고 가져옵니다. |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | 구독 그룹에서 사용자의 구독 상태를 가져옵니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Subscription" }

### 템플릿 {#templates}

`create_email_template` 및 `update_email_template` 기능은 쓰기 기능입니다. MCP 클라이언트는 `call_write_function`으로 이를 호출해야 하며, API 키에 해당하는 `templates.email.create` 또는 `templates.email.update` 권한이 있어야 합니다.

| 기능 | 엔드포인트 | 설명 |
|----------|----------|-------------|
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | 사용 가능한 이메일 템플릿을 나열합니다. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | 이메일 템플릿에 대한 정보를 가져옵니다. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | 이메일 템플릿을 생성합니다. `template_name`, `subject`, `body`가 필수입니다. 선택 필드로 `plaintext_body`, `preheader`, `tags`, `should_inline_css`가 있습니다. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | 기존 이메일 템플릿을 업데이트합니다. `email_template_id`와 하나 이상의 업데이트 가능한 필드(`template_name`, `subject`, `body`, `plaintext_body`, `preheader`, `tags`, `should_inline_css`)가 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Templates" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}