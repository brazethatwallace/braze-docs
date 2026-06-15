---
nav_title: Databricks
article_title: Databricks
description: "이 문서에서는 Braze와의 Databricks Delta Sharing(비공개 베타)에 대해 설명하며, Databricks 계정에서 Braze 참여 및 Campaign 데이터에 액세스할 수 있는 방법을 안내합니다."
page_type: partner
search_tag: Partner
permalink: /databricks/
hidden: true
---

# Databricks


> [Databricks](https://www.databricks.com/)는 엔터프라이즈급 데이터, 분석 및 AI 솔루션을 대규모로 구축, 배포, 공유, 유지 관리하기 위한 통합 오픈 분석 플랫폼입니다. Databricks Data Intelligence Platform은 클라우드 계정의 클라우드 스토리지 및 보안과 통합되며, 클라우드 인프라를 관리하고 배포합니다.

{% alert important %}
Braze와의 Databricks Delta Sharing은 **비공개 베타** 상태입니다. 가용성, 지원 리전 및 제품 동작은 변경될 수 있습니다. 참여하거나 워크스페이스에서 이 기능이 활성화되어 있는지 확인하려면 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

## Delta Sharing(Braze에서 Databricks로) {#delta-sharing-braze-to-databricks}

Databricks [Delta Sharing](https://docs.databricks.com/en/delta-sharing/index.html)을 사용하면 데이터를 복사하거나 복제하지 않고도 클라우드 또는 리전 간에 사업부 및 자회사와 안전하게 데이터를 공유할 수 있습니다.

**Delta Sharing을 사용하면 다음과 같은 작업이 가능합니다:**
- Databricks SQL을 사용하여 Braze 이벤트 및 Campaign 데이터 쿼리
- 복잡한 보고서 생성 및 기여도 모델링 수행
- Braze 데이터를 Databricks 계정의 다른 데이터와 결합
- 채널, 산업 및 기기 플랫폼 전반에 걸쳐 참여 데이터 벤치마킹

설정 방법은 [Databricks Delta Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/databricks/delta_sharing/)을 참조하세요.

Databricks의 Delta Sharing에 대해 자세히 알아보려면 [Delta Sharing이란?](https://www.databricks.com/product/delta-sharing)을 참조하세요.

## 필수 조건 {#prerequisites}

이 기능을 사용하기 전에 다음 사항을 완료하세요.

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Braze 액세스 | Braze에서 이 기능에 액세스하려면 Braze 계정 매니저 또는 고객 성공 매니저에게 문의하세요. |
| Databricks 계정 | `admin` 권한이 있는 Databricks 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

공유를 구성하고 공유 데이터를 쿼리할 준비가 되면 [Databricks Delta Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/databricks/delta_sharing/)으로 이동하세요.