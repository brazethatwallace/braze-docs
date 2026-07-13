---
nav_title: 수식 만들기
article_title: 수식 만들기
page_order: 3
page_type: reference
description: "이 참조 문서에서는 데이터에 존재하는 복잡한 관계를 쉽게 이해할 수 있도록 도와주는 수식을 만들고 관리하는 방법에 대해 설명합니다."
tool: Reports

---
# 수식 만들기 {#create-a-formula}

> Braze에서 분석을 볼 때 여러 데이터 포인트를 결합하여 사용자 데이터에 대한 가치 있는 인사이트를 얻을 수 있습니다. 이를 수식이라고 합니다. 수식을 사용하여 총 월간 활성 사용자 수(MAU) 및 일일 활성 사용자 수(DAU)를 기준으로 시계열 데이터를 정규화할 수 있습니다.

수식은 데이터에 존재하는 복잡한 관계를 이해하는 데 도움이 됩니다. 예를 들어 특정 Segment에 해당하는 일일 활성 사용자가 완료한 커스텀 이벤트의 수를 일반 모집단과 비교하거나 다른 Segment와 비교할 수 있습니다.

## 활용 사례 {#use-cases}

특히 커스텀 이벤트와 결합된 수식을 사용하면 앱 내에서 사용자 동작을 이해하는 데 도움이 될 수 있습니다. 또한 수식은 Google Ads나 TV와 같은 유료 미디어를 Braze와 함께 사용하는 경우에도 Segment 구매 패턴에 대한 심층적인 인사이트를 제공할 수 있습니다.

다음은 수식을 사용하여 감지할 수 있는 동작 패턴의 몇 가지 예입니다:

- **차량 공유 앱:** 사용자가 차량 서비스를 취소하는 시점에 대한 커스텀 이벤트가 있는 경우, 취소된 차량 서비스 / DAU에 대한 함수를 구성하여 특정 사용자 Segments가 다른 사용자보다 차량 서비스를 더 많이 취소하는 경향이 있는지 확인할 수 있습니다.
- **이커머스 앱:** 특정 제품 ID / MAU의 구매에 대한 함수를 설정하면, Braze를 사용하여 모든 프로모션을 추적할 수 없더라도 최근 프로모션한 제품의 Segments 간 인기도를 비교할 수 있습니다.
- **광고를 사용하는 미디어 앱:** 동영상 또는 오디오 클립 사이에 광고로 인해 사용자 경험이 중단되는 경우, 광고 중간 이탈을 커스텀 이벤트로 기록하고 광고 중간 이탈 / DAU 비율을 계산하면 광고 없는 프리미엄 구독 Campaign으로 타겟팅할 최적의 Segments를 찾는 데 도움이 될 수 있습니다.

## 수식 만들기 {#creating-formulas}

수식은 대시보드의 [홈]({{site.baseurl}}/user_guide/analytics/dashboards/home), [매출 보고서]({{site.baseurl}}/user_guide/analytics/reports/revenue_report), [사용자 지정 이벤트 보고서]({{site.baseurl}}/user_guide/data/activation/events/custom_events) 페이지에 있는 통계 패널에서 접근할 수 있습니다. 이 패널을 보려면 **Performance Over Time** 차트로 이동하여 **Statistics For** 드롭다운을 **KPI Formulas**로 변경한 다음 하나 이상의 KPI 수식을 선택하여 차트를 채웁니다.

![Braze 대시보드에서 KPI 수식에 대한 통계 보기]({% image_buster /assets/img_archive/kpi_forms.png %})

새 수식을 만들려면 다음과 같이 하세요:

1. 해당 대시보드(**홈**, **매출 보고서** 또는 **사용자 지정 이벤트 보고서**)로 이동합니다.
2. **KPI 수식 관리**를 선택합니다.
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
| DAU | MAU |
| 세션 | DAU |
| | Segment 크기 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="개요 대시보드" }

### 매출 대시보드 {#revenue-dashboard}

| 분자 | 분모 |
| --- | --- |
| 구매(전체) | DAU |
| 선택 구매(예: 기프트 카드 또는 제품 ID) | MAU |
{: .reset-td-br-1 .reset-td-br-2 aria-label="매출 대시보드" }

### 커스텀 이벤트 대시보드 {#custom-event-dashboard}

| 분자 | 분모 |
| --- | --- |
| 커스텀 이벤트 수 | MAU |
|  | DAU |
|  | Segment 크기([분석 추적]({{site.baseurl}}/viewing_and_understanding_segment_data)이 활성화된 Segments만 사용할 수 있습니다) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 이벤트 대시보드" }