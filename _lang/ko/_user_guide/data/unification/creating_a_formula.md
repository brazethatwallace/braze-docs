---
nav_title: 수식 만들기
article_title: 수식 만들기
page_order: 3
page_type: reference
description: "이 참조 문서에서는 데이터에 존재하는 복잡한 관계를 쉽게 이해할 수 있도록 도와주는 수식을 만들고 관리하는 방법에 대해 설명합니다."
tool: Reports

---
# 수식 만들기 {#create-a-formula}

> Braze에서 분석을 볼 때 여러 데이터 포인트를 결합하여 사용자 데이터에 대한 가치 있는 인사이트를 얻을 수 있습니다. 이를 수식이라고 합니다. 수식을 사용하여 총 월간 활성 사용자 수(MAU) 및 일일 활성 사용자 수(일일 활성 사용자)를 기준으로 시계열 데이터를 정규화할 수 있습니다.

수식은 데이터에 존재하는 복잡한 관계를 이해하는 데 도움이 됩니다. 예를 들어 특정 Segment에 해당하는 일일 활성 사용자가 완료한 커스텀 이벤트의 수를 일반 모집단과 비교하거나 다른 Segment와 비교할 수 있습니다.

## 사용 사례 {#use-cases}

수식은 특히 커스텀 이벤트와 결합할 때 앱 내 사용자 행동을 이해하는 데 도움이 됩니다. 또한 수식은 Google Ads나 TV 광고와 같은 유료 미디어를 Braze와 함께 사용하는 경우에도 Segment 구매 패턴에 대한 더 깊은 인사이트를 제공할 수 있습니다.

다음은 수식을 사용하여 감지할 수 있는 행동 패턴의 몇 가지 예시입니다:

- **차량 공유 앱:** 사용자가 탑승을 취소할 때의 커스텀 이벤트가 있는 경우, 취소된 탑승 / 일일 활성 사용자(일일 활성 사용자) 함수를 구성하여 특정 사용자 Segment가 다른 Segment보다 더 많이 탑승을 취소하는 경향이 있는지 확인할 수 있습니다.
- **이커머스 앱:** 특정 제품 ID의 구매 / 월간 활성 사용자(MAU) 함수를 구성하면, 모든 프로모션을 Braze를 통해 추적할 수 없는 경우에도 최근 프로모션된 제품의 인기도를 Segment 간에 비교할 수 있습니다.
- **광고를 사용하는 미디어 앱:** 비디오 또는 오디오 클립 사이에 광고로 인해 사용자 경험이 중단되는 경우, 광고 중간 이탈을 커스텀 이벤트로 기록하고 광고 중간 이탈 / 일일 활성 사용자(일일 활성 사용자) 비율을 계산하면 광고 없는 프리미엄 가입 Campaign의 타겟으로 가장 적합한 Segment를 찾는 데 도움이 됩니다.

## 수식 만들기 {#creating-formulas}

수식은 대시보드의 [홈]({{site.baseurl}}/user_guide/analytics/dashboards/home), [매출 보고서]({{site.baseurl}}/user_guide/analytics/reports/revenue_report), [커스텀 이벤트 보고서]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) 페이지에서 사용할 수 있습니다. **홈** 및 **매출 보고서**에서 **시간별 성능** 차트를 열고, **통계 대상**을 **KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or 핵심 성과 지표(KPI or 핵심 성과 지표(KPI)) 수식**으로 설정한 다음, 하나 이상의 수식을 선택합니다. **커스텀 이벤트 보고서** 페이지에서는 **필터**를 열고, 하나 이상의 **KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or 핵심 성과 지표(KPI or 핵심 성과 지표(KPI)) 수식** 옵션을 선택한 후 **적용**을 선택합니다.

![Braze 대시보드에서 KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or 핵심 성과 지표(KPI or 핵심 성과 지표(KPI)) 수식에 대한 통계 보기]({% image_buster /assets/img_archive/kpi_forms.png %})

새 수식을 만들려면 다음을 수행합니다.

1. 해당 대시보드(**홈**, **매출 보고서** 또는 **커스텀 이벤트 보고서**)로 이동합니다.
2. **KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or 핵심 성과 지표(KPI or 핵심 성과 지표(KPI)) 수식 관리**를 선택합니다.
3. 수식의 이름을 입력합니다.
4. 관련 분자와 분모를 선택합니다.
5. **저장**을 선택합니다.

## 사용 가능한 분자 및 분모 {#available-numerators-and-denominators}

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

### 개요 대시보드 {#overview-dashboard}

| 분자 | 분모 |
| --- | --- |
| 일일 활성 사용자 | MAU |
| 세션 | 일일 활성 사용자 |
| | Segment 크기 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="개요 대시보드" }

### 매출 대시보드 {#revenue-dashboard}

| 분자 | 분모 |
| --- | --- |
| 구매(전체) | 일일 활성 사용자 |
| 특정 구매(예: 기프트 카드 또는 제품 ID) | MAU |
{: .reset-td-br-1 .reset-td-br-2 aria-label="매출 대시보드" }

### 커스텀 이벤트 대시보드 {#custom-event-dashboard}

| 분자 | 분모 |
| --- | --- |
| 커스텀 이벤트 수 | MAU |
|  | 일일 활성 사용자 |
|  | Segment 크기([분석 추적]({{site.baseurl}}/viewing_and_understanding_segment_data)이 활성화된 Segments만 사용할 수 있습니다) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 이벤트 대시보드" }