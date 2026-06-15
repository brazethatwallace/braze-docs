---
nav_title: Kubit
article_title: Kubit
description: "이 참조 문서에서는 노코드 셀프서비스 분석 플랫폼인 Kubit과 Braze 간의 파트너십을 설명합니다. Kubit은 즉각적인 제품 인사이트를 제공하며, Kubit 사용자 코호트를 가져와 Braze 메시징에서 타겟팅할 수 있습니다."
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# Kubit

> [Kubit](https://kubit.ai/)은 즉각적인 제품 인사이트를 제공하는 노코드 셀프서비스 분석 플랫폼입니다.

Braze와 Kubit 통합을 통해 [Kubit 사용자 코호트를 가져와]({{site.baseurl}}/partners/data_and_analytics/cohort_import/kubit/) Braze 메시징에서 타겟팅할 수 있습니다. 또한 [Snowflake 보안 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)를 활용하여 Braze의 원시 캠페인 및 노출 횟수 데이터를 Kubit 제품 분석과 통합하여 이러한 캠페인의 영향을 실시간으로 측정할 수 있습니다. 이 접근 방식은 엔지니어링 작업 없이도 사용자의 전체 라이프사이클에 대한 인사이트를 제공합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Kubit 엔터프라이즈 계정 | 이 파트너십을 활용하려면 Kubit 엔터프라이즈 계정이 필요합니다. |
| 일치하는 사용자 ID | Kubit과 Braze의 고객 데이터는 두 플랫폼에서 일치하는 사용자 ID를 가지고 있어야 합니다. 여기에는 익명 UUID도 포함됩니다. Braze에서 사용자 ID를 설정하는 방법에 대해서는 [설명서]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Kubit에서 Braze 데이터 분석하기 {#analyzing-braze-data-in-kubit}

[Snowflake 보안 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)를 활용하여 Braze의 원시 캠페인 및 노출 횟수 데이터를 Kubit과 공유하고, 이를 Kubit의 셀프서비스 분석에 통합하여 사용자 라이프사이클의 전체 그림을 확인할 수 있습니다.

참고로, Kubit 분석에 통합할 수 있는 모든 [Braze 필드]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2)가 여기에 나와 있습니다. 이 단계의 세부 사항은 고객마다 다르며 특별한 구성이 필요합니다. 자세한 내용은 Kubit 계정 매니저 또는 [support@kubit.ai](support@kubit.ai)에 문의하세요.