---
nav_title: 10월
page_order: 4
noindex: true
page_type: update
description: "이 문서에는 2018년 10월의 릴리스 노트가 포함되어 있습니다."
---
# 2018년 10월 {#october-2018}

{% comment %}
  나중에 추가할 수 있습니다...
  지능형 선택 대조군 토글
  이제 지능형 선택 상자에 [대조군 사용을 켜거나 끌]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing#including-a-control-group) 수 있는 확인란이 생겼습니다. 이 기능을 켜면 대조군은 대상 규모의 20%가 되며 지능형 선택 기능이 배리언트 오디언스 규모별로 최적화함에 따라 변경됩니다.
  캔버스 항목 설정 마법사(베타)
  작업 누락과 그로 인한 오류를 방지하기 위해 캔버스 UI가 간소화됩니다. 특히 캔버스 구성은 이제 캠페인 마법사의 디자인과 유사하게 마법사에 표시됩니다. 이 기능은 점진적으로 배포 중이므로 현재 설명서에는 반영되어 있지 않습니다. 자세한 내용은 곧 다시 확인해 주세요!
  구독 그룹 API (숨김)
  Braze는 외부 ID 또는 이메일 주소를 기반으로 요청할 수 있는 새로운 GET 호출 기능을 추가했습니다. 그러면 해당 사용자와 연결된 모든 구독 그룹이 제공됩니다.
{% endcomment %}

## Campaign의 정확한 오디언스 통계 계산 {#calculate-exact-audience-stats-for-campaigns}

이제 **Campaign Analytics**로 이동하여 오디언스의 정확한 통계를 계산할 수 있습니다. **Target Audiences** 섹션 하단에서 **Calculate Exact Stats**를 클릭하면 정확한 오디언스 통계가 표시됩니다. 계산하기 전에 Campaign을 저장해야 하며, 임시저장 상태의 Campaign은 임시저장본으로 저장됩니다.

## Windows 8 지원 중단 {#windows-8-deprecation}

Braze는 2018년 10월 10일부로 Windows 8에 대한 지원을 종료했습니다.

## 파트너십 허브 {#partnerships-hub}

이제 Braze 플랫폼의 **Integrations**에서 통합 목록과 통합 키 및 안내 사항을 확인할 수 있습니다.

## 이메일 분석 계산 {#email-analytics-calculations}

Braze는 이제 이메일 분석의 정확성을 크게 향상시키기 위해 이메일 서비스 공급자(ESP)의 이벤트 데이터를 사용하여 모든 이메일 분석을 계산하고 있습니다. 이 솔루션은 데이터 무결성을 보장하기 위해 오픈 소스 데이터베이스 솔루션인 Postgres를 활용합니다.

{% alert important %}
고유 열람 및 고유 클릭은 현재 이메일 서비스 공급자가 제공하는 집계 데이터에 의존하고 있습니다. 이번 릴리스에서 도입된 동일한 인프라를 사용하여 이러한 고유성 통계를 계산하기 위한 작업이 진행 중입니다.
{% endalert %}

## 메시지 작성기 패널 컨트롤 {#composer-panel-controls}

메시지 작성기 컨트롤이 업데이트되어 아이콘과 관련된 텍스트가 포함되었으며, 이를 통해 사용성과 탐색이 향상되었습니다.

## Currents용 Azure {#azure-for-currents}

Currents를 사용하는 Braze 고객은 이제 [Azure]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)를 잠재적 통합으로 확인할 수 있습니다.

## 입력 필드 확장 {#input-field-expansions}

이제 이메일 제목란과 푸시 제목의 입력란을 확장할 수 있습니다.