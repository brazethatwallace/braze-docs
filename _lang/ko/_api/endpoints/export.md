---
nav_title: 내보내기
article_title: 내보내기 엔드포인트
search_tag: Endpoint
page_order: 2
description: "이 참조 문서에서는 필수 조건, 내보낼 수 있는 항목, 데이터 전달 방식, 전체 엔드포인트 목록을 포함하여 Braze 내보내기 엔드포인트에 대해 설명합니다."
page_type: reference
---

# 내보내기 엔드포인트 {#export-endpoints}

이 엔드포인트 모음을 사용하면 핵심 성과 지표(KPI), 앱 세션, 사용자, Segments, Campaigns, Canvases에 대한 다양한 수준의 세부 정보에 액세스하고 내보낼 수 있습니다. 매개변수 및 요청 본문을 작성할 때 [Braze 인스턴스]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints), [API 키]({{site.baseurl}}/api/basics), [API 식별자]({{site.baseurl}}/api/identifier_types)를 알고 있어야 합니다.

## 필수 조건 {#prerequisites}

시작하기 전에 다음 사항을 준비했는지 확인하세요:

| 요구 사항 | 설명 |
| --- | --- |
| Braze REST API 키 | 호출하려는 엔드포인트에 적합한 내보내기 권한이 있는 REST API 키입니다. API 키는 특정 엔드포인트로 범위가 지정되며, 생성 후에는 권한을 변경할 수 없습니다. 자세한 내용은 [REST API 키]({{site.baseurl}}/api/basics#about-rest-api-keys)를 참조하세요. |
| 관련 식별자 | 내보내려는 데이터의 식별자(예: Campaign ID, Segment ID 또는 Canvas ID)입니다. Braze 대시보드에서 확인할 수 있습니다. 전체 목록은 [API 식별자 유형]({{site.baseurl}}/api/identifier_types)을 참조하세요. |
| 클라우드 스토리지 자격 증명(선택 사항) | 대용량 데이터셋을 내보내는 경우, [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3), [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) 또는 [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents) 버킷을 연결하여 내보내기 파일을 스토리지에 직접 저장할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

{% alert note %}
API 액세스 권한이 없는 마케터 또는 팀원인 경우, 조직 내 개발자 또는 관리자에게 API 키 및 통합 설정을 요청하세요.
{% endalert %}

## 내보낼 수 있는 항목 {#what-you-can-export}

다음 표에서는 내보내기 API를 통해 사용할 수 있는 데이터 카테고리를 요약합니다.

| 카테고리 | 포함 항목 | API 참고 자료 |
| --- | --- | --- |
| Campaigns | 성능 분석, Campaign 세부 정보, Campaign 목록 및 발송 분석 | [Campaign 엔드포인트]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) |
| Canvases | 데이터 시계열 분석, 분석 요약, Canvas 세부 정보 및 Canvas 목록 | [Canvas 엔드포인트]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) |
| Segments | Segment 목록, Segment 분석 및 Segment 세부 정보 | [Segment 엔드포인트]({{site.baseurl}}/api/endpoints/export/segments/get_segment) |
| 사용자 데이터 | 식별자 또는 Segment별 전체 고객 프로필 및 글로벌 컨트롤 그룹별 사용자 | [사용자 데이터 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) |
| 핵심 성과 지표(KPI) | 일일 활성 사용자, 월간 활성 사용자, 일일 신규 사용자 및 날짜별 삭제 수 | [KPI 엔드포인트]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) |
| 세션 | 앱 세션 시계열 데이터 | [세션 엔드포인트]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) |
| 커스텀 이벤트 | 이벤트 이름, 이벤트 목록 및 시간에 따른 이벤트 분석 | [커스텀 이벤트 엔드포인트]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) |
| 커스텀 속성 | 속성 이름 | [커스텀 속성 엔드포인트]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) |
| 구매 | 시간별 매출 데이터, 제품 ID 목록 및 구매 횟수 | [구매 엔드포인트]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="내보낼 수 있는 항목" }

## 내보내기 데이터 전달 방식 {#how-export-data-is-delivered}

API 내보내기는 대시보드에서 다운로드하는 CSV 파일과 달리 JSON 형식으로 데이터를 반환합니다. 전달 방식은 클라우드 스토리지 연결 여부에 따라 달라집니다.

- **클라우드 스토리지 미연결 시:** Braze는 내보내기 파일을 자체 S3 버킷에 저장하고 API 응답에 임시 다운로드 URL을 포함합니다. 이 URL은 4시간 후에 만료되며, 내보내기는 JSON 파일이 포함된 압축 아카이브(ZIP 또는 GZIP, `output_format` 매개변수에 따라 다름)로 패키징됩니다. JSON 파일의 각 줄은 하나의 데이터 객체를 나타냅니다.
- **클라우드 스토리지 연결 시:** Braze는 내보내기 파일을 구성된 버킷에 직접 저장합니다. API 응답에 다운로드 URL이 포함되지 않습니다. 파일은 자체 보존 정책을 따르며, 일반적으로 대규모 내보내기에 더 안정적입니다.

{% alert tip %}
"클라우드 스토리지"란 자체 스토리지 버킷(예: Amazon S3, Microsoft Azure Blob Storage 또는 Google Cloud Storage)을 의미합니다. **파트너 통합** > **기술 파트너**에서 버킷을 연결하면 Braze가 내보내기 파일을 해당 버킷에 직접 저장할 수 있습니다.
{% endalert %}

내보내기 전달 및 문제 해결에 대한 자세한 내용은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)을 참조하세요.

## 내보내기 엔드포인트

다음 표에는 사용 가능한 모든 내보내기 API가 나와 있습니다.

| 카테고리 | 메서드 | 엔드포인트 |
| --- | --- | --- |
| Campaigns | GET | [Campaign 분석]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) |
| Campaigns | GET | [Campaign 세부 정보]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) |
| Campaigns | GET | [Campaigns 목록]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) |
| Campaigns | GET | [발송 분석]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) |
| Canvases | GET | [Canvas 데이터 시리즈 분석]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) |
| Canvases | GET | [Canvas 분석 요약]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) |
| Canvases | GET | [Canvas 세부 정보]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) |
| Canvases | GET | [Canvas 목록]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) |
| 커스텀 이벤트 | GET | [커스텀 이벤트]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) |
| 커스텀 이벤트 | GET | [커스텀 이벤트 목록]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) |
| 커스텀 이벤트 | GET | [커스텀 이벤트 분석]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) |
| 커스텀 속성 | GET | [커스텀 속성]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) |
| 핵심 성과 지표(KPI) | GET | [날짜별 일일 신규 사용자 KPI]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) |
| 핵심 성과 지표(KPI) | GET | [날짜별 일일 활성 사용자 KPI]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) |
| 핵심 성과 지표(KPI) | GET | [최근 30일간 월간 활성 사용자 KPI]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) |
| 핵심 성과 지표(KPI) | GET | [날짜별 앱 삭제 KPI]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) |
| 구매 | GET | [제품 ID 목록]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) |
| 구매 | GET | [구매 횟수]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) |
| 구매 | GET | [기간별 매출 데이터]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) |
| Segments | GET | [Segment 목록]({{site.baseurl}}/api/endpoints/export/segments/get_segment) |
| Segments | GET | [Segment 분석]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) |
| Segments | GET | [Segment 세부 정보]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) |
| 세션 | GET | [앱 세션 시계열 데이터]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) |
| 사용자 데이터 | POST | [식별자별 사용자 데이터]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) |
| 사용자 데이터 | POST | [Segment별 사용자 데이터]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) |
| 사용자 데이터 | POST | [글로벌 컨트롤 그룹별 사용자 데이터]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="내보내기 엔드포인트" }

## 관련 문서 {#related-articles}

대시보드에서 일회성 내보내기를 수행하려면 다음 문서를 참조하세요:

- [Campaign 데이터 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data)
- [Canvas 데이터 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data)
- [Segment 데이터를 CSV로 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv)