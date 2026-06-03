---
nav_title: 세그먼트 분석 추적
article_title: 세그먼트 분석 추적
page_order: 3
page_type: reference
description: "이 참조 문서에서는 세그먼트 분석 추적과 시간별 매출 및 구매, 시간별 세션, 시간별 커스텀 이벤트를 보는 방법에 대해 설명합니다."
tool:
  - Segments
  - Reports
---

# Segment 분석 추적 {#segment-analytics-tracking}

> Segment에 대해 분석 추적이 켜져 있으면 해당 Segment의 세션, 커스텀 이벤트, 시간 경과에 따른 매출을 확인할 수 있습니다.

Segment에 대해 분석 추적을 켜지 않더라도 해당 Segment의 [실시간 통계]({{site.baseurl}}/user_guide/audience/segments/segment_data/#segment-statistics)에 액세스하고 Campaigns로 해당 사용자를 타겟팅할 수 있습니다. 유일한 차이점은 이 페이지에서 언급된 특정 분석 도구에 액세스할 수 있는지 여부입니다.

## Segment 분석 켜기 {#turning-on-segment-analytics}

Segment 페이지의 **Segment Details** 섹션에서 **Analytics Tracking**을 켭니다.

![Segment에 대한 분석 추적 토글]({% image_buster /assets/img_archive/A_Tracking_2.png %})

앱은 최대 25개의 Segments에 대해 추적을 설정할 수 있습니다. Braze는 Campaigns이 세션, 매출, 구매에 미치는 영향을 파악할 때 분석해야 할 중요한 Segments를 추적할 것을 권장합니다.

{% alert note %}
분석 추적을 활성화한 후 Segment 데이터가 채워질 때까지 지연이 발생할 수 있습니다. 24시간 이내에 데이터가 채워지지 않으면 [고객지원에 문의]({{site.baseurl}}/braze_support/)하세요.
{% endalert %}

## 시간 경과에 따른 매출 및 구매 보기 {#viewing-revenue-and-purchases-over-time}

**Analytics** > **매출 보고서**로 이동하여 [이 Segment의 시간 경과에 따른 매출 및 구매]({{site.baseurl}}/user_guide/analytics/reports/revenue_report/) 데이터를 확인합니다.

매출 및 구매 차트는 해당 Segment에 대해 분석 추적이 켜진 이후에 기록된 활동을 반영합니다. 추적을 켜더라도 이전 구매가 해당 보고서에 소급 적용되지는 않습니다. Segments를 비교할 때는 선택한 각 Segment에 대해 추적이 활성화된 시간 범위만 사용하세요.

![Segment별 매출 데이터]({% image_buster /assets/img_archive/Revenue.png %})

커스텀 시간 범위에 대한 Segment 데이터를 시각적으로 비교하려면 그래프에서 Segments를 추가하거나 제거합니다. **Breakdown** 드롭다운에서 **By Segment**를 선택한 다음 **Breakdown values**에서 Segments를 선택합니다.

그래프 위의 Segment 이름을 선택하여 해당 Segment의 측정기준 표시 여부를 켜거나 끌 수 있습니다.

![여러 Segment에 대한 매출]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## 시간별 세션 {#sessions-over-time}

마찬가지로 **Home** 페이지에서 [이 특정 Segment의 시간 경과에 따른 세션]({{site.baseurl}}/user_guide/analytics/dashboards/home/#exporting-app-usage-data) 데이터를 확인할 수 있습니다.

![Segment별 세션 데이터]({% image_buster /assets/img_archive/events_over_time2.png %})

## 시간 경과에 따른 커스텀 이벤트 보기 {#view-custom-events-over-time}

**Analytics** > **사용자 지정 이벤트 보고서**로 이동하여 [Segments의 시간 경과에 따른 커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events/#analytics) 데이터를 확인합니다.

## 쿼리 빌더 템플릿 사용 {#using-query-builder-templates}

분석 추적이 켜져 있으면 쿼리 빌더 보고서 템플릿을 사용하여 Campaigns, Canvas, 배리언트 및 단계에 대한 성과 측정기준을 Segments별로 세분화할 수 있습니다. 자세히 알아보려면 [Segment 데이터]({{site.baseurl}}/user_guide/audience/segments/segment_data/#performance-data-by-segment)를 확인하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### 분석 추적이 잘못되었거나 비어 있는 경우 무엇을 확인해야 하나요? {#what-should-i-check-if-analytics-tracking-looks-wrong-or-empty}

**Segment Details**에서 **Analytics Tracking**이 여전히 활성화되어 있는지 확인하고, 앱당 한도(추적이 설정된 Segments 25개)를 초과하지 않았는지 확인하세요. 추적을 처음 활성화한 후 데이터가 채워지기까지 최대 24시간이 소요될 수 있습니다. 문제가 계속되면 Segment 정의와 보고서 날짜 범위를 확인한 후 [고객지원에 문의]({{site.baseurl}}/braze_support/)하세요.