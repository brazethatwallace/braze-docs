# Braze MCP 서버 기능 {#braze-mcp-server-functions}

> Braze MCP 서버는 특정 Braze REST API 엔드포인트에 매핑되는 읽기 및 쓰기 도구를 노출합니다. 자세한 내용은 [Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}를 참조하세요.

{% multi_lang_include mcp_server/beta_alert.md %}

{% alert note %}
Braze MCP 서버에는 베타 프로그램에 참여 중인 고객만 사용할 수 있는 도구가 포함되어 있습니다. 베타 프로그램에 포함된 도구에 접근하려 할 때 계정에 해당 기능이 활성화되어 있지 않으면 오류 응답을 받을 수 있습니다. 베타 프로그램에 참여하려면 계정 매니저에게 문의하세요.
{% endalert %}

## 사전 요구 사항 {#prerequisites}

이 기능을 사용하려면 먼저 [Braze MCP 서버를 설정]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}해야 합니다.

## 사용 가능한 Braze API 기능 {#available-braze-api-functions}

MCP 클라이언트는 이러한 도구를 참조하여 Braze MCP 서버와 상호 작용합니다.

### 워크스페이스 {#workspaces}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | read | 현재 OAuth 액세스 토큰으로 접근할 수 있는 Braze 워크스페이스를 확인합니다. 먼저 이 도구를 호출하세요. 반환된 각 워크스페이스 `id`는 다른 모든 도구에서 필요한 `app_group_id`입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="워크스페이스" }

### Campaigns

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | read | 이름, Campaign API 식별자, API Campaign 플래그 및 태그가 포함된 Campaign 목록을 내보냅니다. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | read | `campaign_id`를 기준으로 지정된 Campaign의 관련 정보를 조회합니다. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | read | 시간 경과에 따른 Campaign 통계의 일별 시리즈(채널별 발송, 열람, 클릭, 전환)를 조회합니다. |
| `duplicate_campaign` | [`/campaigns/duplicate`]({{site.baseurl}}/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns) | create | 기존 Campaign을 복제합니다. |
| `create_campaign`<sup>*</sup> | N/A | create | 새 Campaign을 생성합니다. |
| `edit_campaign`<sup>*</sup> | N/A | update | 기존 Campaign을 편집합니다. |
| `launch_campaign`<sup>*</sup> | N/A | update | Campaign을 시작합니다. |
| `stop_campaign`<sup>*</sup> | N/A | update | 실행 중인 Campaign을 중지합니다. |
| `archive_campaign`<sup>*</sup> | N/A | update | Campaign을 보관합니다. |
| `unarchive_campaign`<sup>*</sup> | N/A | update | Campaign 보관을 해제합니다. |
| `get_campaign_draft`<sup>*</sup> | N/A | read | 임시 저장된 Campaign 세부 정보를 조회합니다. |
| `get_campaign_live_details`<sup>*</sup> | N/A | read | 라이브 Campaign 세부 정보를 조회합니다. |
| `create_campaign_message`<sup>*</sup> | N/A | create | Campaign 내에 메시지를 생성합니다. |
| `update_campaign_message`<sup>*</sup> | N/A | update | Campaign 메시지를 업데이트합니다. |
| `delete_campaign_message`<sup>*</sup> | N/A | delete | Campaign 메시지를 삭제합니다. |
| `create_campaign_message_variation`<sup>*</sup> | N/A | create | Campaign 내에 메시지 배리에이션을 생성합니다. |
| `update_campaign_message_variation`<sup>*</sup> | N/A | update | Campaign 메시지 배리에이션을 업데이트합니다. |
| `delete_campaign_message_variation`<sup>*</sup> | N/A | delete | Campaign 메시지 배리에이션을 삭제합니다. |
| `update_campaign_distribution`<sup>*</sup> | N/A | update | Campaign 배포 설정을 업데이트합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaigns" }

<sup>*</sup> 이 도구는 Campaign API 베타 프로그램에 참여 중인 고객만 사용할 수 있습니다. 계정에 이 기능이 활성화되어 있지 않으면, 사용하려고 할 때 오류가 발생할 수 있습니다. 베타 프로그램에 참여하려면 계정 매니저에게 문의하세요.
{: .reset-td-br-1 }

### Canvases

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | read | 이름, Canvas API 식별자 및 태그가 포함된 Canvas 목록을 내보냅니다. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | read | Canvas 메타데이터(이름, 생성 시간, 현재 상태 등)를 내보냅니다. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | read | Canvas의 시계열 데이터를 내보냅니다. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | read | 간결한 결과 요약을 위해 Canvas 시계열 데이터의 집계값을 내보냅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvases" }

### 카탈로그 {#catalogs}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | read | 워크스페이스 내 카탈로그 목록을 조회합니다. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | read | 여러 카탈로그 항목과 해당 콘텐츠를 반환합니다. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | read | 단일 카탈로그 항목과 해당 콘텐츠를 반환합니다. |
| `create_catalog` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | create | 카탈로그를 생성합니다. |
| `delete_catalog` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | delete | 카탈로그를 삭제합니다. |
| `create_catalog_fields` | [`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields) | create | 카탈로그에 여러 필드를 생성합니다. |
| `delete_catalog_field` | [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field) | delete | 카탈로그 필드를 삭제합니다. |
| `create_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | create | 카탈로그에 여러 항목을 생성합니다. 요청당 최대 50개 항목. |
| `edit_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | update | 카탈로그의 기존 항목 여러 개를 편집합니다. 요청당 최대 50개 항목. |
| `replace_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | update | 카탈로그의 여러 항목을 교체합니다. 항목이 존재하지 않으면 생성합니다. 요청당 최대 50개 항목. |
| `delete_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | delete | 카탈로그의 여러 항목을 삭제합니다. 요청당 최대 50개 항목. |
| `create_catalog_selection` | [`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | create | 카탈로그에 선택 항목을 생성합니다. |
| `delete_catalog_selection` | [`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection) | delete | 카탈로그 선택 항목을 삭제합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="카탈로그" }

### 커스텀 속성 {#custom-attributes}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | read | 앱에 기록된 커스텀 속성을 알파벳순으로 50개씩 내보냅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="커스텀 속성" }

### 커스텀 이벤트 {#custom-events}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | read | 앱에 기록된 커스텀 이벤트를 알파벳순으로 50개씩 내보냅니다(커서 페이지네이션). |
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | read | 커스텀 이벤트 이름을 알파벳순으로 250개씩 내보냅니다(페이지 페이지네이션). |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | read | 지정된 기간 동안의 커스텀 이벤트 발생 횟수를 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="커스텀 이벤트" }

### CDI 통합 {#cdi-integrations}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | read | 기존 클라우드 데이터 수집(CDI) 통합 목록을 호출당 10개씩 조회합니다. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | read | 특정 CDI 통합의 이전 동기화 상태를 호출당 10개씩 조회합니다. |
| `trigger_integration_sync` | [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) | write | 특정 CDI 통합에 대한 동기화를 트리거합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="CDI 통합" }

### 핵심 성과 지표(KPI)

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | read | 날짜별 일일 고유 활성 사용자 수 시리즈를 조회합니다. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | read | 30일 롤링 윈도우 기준 일별 고유 활성 사용자 수 시리즈를 조회합니다. |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | read | 날짜별 총 신규 사용자 수의 일별 시리즈를 조회합니다. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | read | 날짜별 총 앱 삭제 건수의 일별 시리즈를 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="핵심 성과 지표(KPI)" }

### 미디어 라이브러리 {#media-library}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | create | 외부 URL 또는 base64 파일 콘텐츠를 통해 Braze 미디어 라이브러리에 에셋을 업로드합니다. 정확히 하나의 업로드 방식만 제공해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="미디어 라이브러리" }

### 구매 {#purchases}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | read | 페이지네이션된 제품 ID 목록을 조회합니다. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | read | 특정 기간 동안 앱 내 총 구매 건수를 조회합니다. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | read | 특정 기간 동안 앱 내 총 매출을 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="구매" }

### Segments

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | read | 이름, Segment API 식별자 및 분석 추적 플래그가 포함된 Segment 목록을 내보냅니다. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | read | `segment_id`를 기준으로 Segment의 관련 정보를 조회합니다. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | read | 시간 경과에 따른 Segment의 예상 크기에 대한 일별 시리즈를 조회합니다. |
| `get_segment_filters`<sup>*</sup> | N/A | read | Segment 필터 정의를 조회합니다. |
| `create_segment`<sup>*</sup> | N/A | create | 새 Segment를 생성합니다. |
| `edit_segment`<sup>*</sup> | N/A | update | 기존 Segment를 편집합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Segments" }

<sup>*</sup> 이 도구는 Segment API 베타 프로그램에 참여 중인 고객만 사용할 수 있습니다. 계정에 이 기능이 활성화되어 있지 않으면, 사용하려고 할 때 오류가 발생할 수 있습니다. 베타 프로그램에 참여하려면 계정 매니저에게 문의하세요.
{: .reset-td-br-1 }

### 발송 {#sends}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | read | 추적된 `send_id`(API Campaign)에 대한 일별 통계를 조회합니다. Braze는 발송 분석 데이터를 발송 후 14일간 보관합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="발송" }

### 세션 {#sessions}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | read | 지정된 기간 동안 앱의 세션 수를 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="세션" }

### 템플릿 {#templates}

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | read | Braze 계정에서 사용 가능한 이메일 템플릿 목록을 조회합니다. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | read | 특정 이메일 템플릿에 대한 정보를 조회합니다. 드래그 앤 드롭 편집기 템플릿은 지원되지 않습니다. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | create | Braze 대시보드에서 이메일 템플릿을 생성합니다. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | update | 기존 이메일 템플릿을 업데이트합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="템플릿" }

### Content Blocks

| 도구 | API 엔드포인트 | 접근 | 설명 |
| --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | read | 기존 콘텐츠 블록 정보 목록을 조회합니다. |
| `get_content_block_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | read | 기존 콘텐츠 블록의 정보를 조회합니다. 선택적으로 Campaign 또는 Canvas 포함 데이터를 함께 조회할 수 있습니다. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | create | 콘텐츠 블록을 생성합니다. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | update | 콘텐츠 블록을 업데이트합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Content Blocks" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}