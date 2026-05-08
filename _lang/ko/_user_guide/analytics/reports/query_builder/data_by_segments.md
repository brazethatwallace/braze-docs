---
nav_title: Segment별 측정기준
article_title: Segment별 측정기준
page_order: 3
page_type: reference
description: "이 페이지에서는 쿼리 빌더 보고서 템플릿을 사용하여 Campaigns, Canvas, 배리언트 및 단계의 성과 측정기준을 Segments별로 분류하는 방법을 설명합니다."
tool:
  - Segments
  - Reports

---

# Segment별 측정기준 {#metrics-by-segments}

> [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) 보고서 템플릿을 사용하여 Campaigns, Canvas, 배리언트 및 단계의 성과 측정기준을 Segments별로 분류합니다.

측정기준에 접근하려는 Segments에 대해 [분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/#segment-analytics-tracking)이 활성화되어 있어야 합니다.

이 보고서를 실행하려면 다음을 수행합니다:
1. **쿼리 빌더**에서 템플릿을 사용하여 새 SQL 보고서를 생성합니다.
2. 측정기준에 대해 **Segment 분류**를 선택하면 Segment별 분류가 포함된 측정기준 템플릿이 필터링됩니다. 해당 템플릿은 다음과 같습니다:
- Segment별 이메일 성과 측정기준
- Segment별 배리언트 또는 단계의 이메일 참여 측정기준
- Segment별 구매 및 매출
- Segment별 배리언트 또는 단계의 구매 및 매출
- Segment별 푸시 성과

![Segment 분류 페이지에는 SQL 편집기, 변수, 사용 가능한 데이터 테이블, 쿼리 기록 및 AI 쿼리 빌더 탭이 있는 사이드 패널, 그리고 결과 섹션이 포함되어 있습니다.]({% image_buster /assets/img_archive/segment_breakdown.png %})

## 보고서 템플릿 {#report-templates}

{% tabs %}
{% tab Segment별 이메일 참여 측정기준 %}

### Campaigns 또는 Canvases의 측정기준 보기 {#campaign-canvas-email}

Campaign 또는 Canvas 수준에서 Segment별로 분류된 이메일 성과 측정기준을 보려면 [변수](#variables) 탭을 사용하여 Campaigns 또는 Canvases와 데이터를 가져올 기간을 지정합니다. Campaigns 또는 Canvases를 지정하지 않으면 보고서에 지정된 기간 내 모든 Campaigns 및 Canvases의 이메일이 포함됩니다. 특정 태그가 있는 모든 Campaigns 및 Canvases를 볼 수도 있습니다.

이 보고서에서 사용할 수 있는 이메일 측정기준은 다음과 같습니다:
- 발송 수
- 전달 수
- 불만 수
- 고유 열람 수
- 고유 기계 열람 수
- 고유 비기계 열람 수
- 고유 클릭 수
- 탈퇴 수
- 반송 수
- 소프트바운스 수
- 지연 수

#### 결과 {#results}

선택한 Campaigns 또는 Canvases에 대한 Segment별 이메일 참여 측정기준이 결과에 표시됩니다. 특정 Campaigns 또는 Canvases를 선택하지 않은 경우, 보고서 기간 내 모든 이메일 Campaigns 및 Canvases에 대한 각 Segment의 이메일 측정기준이 표시됩니다.

- **행:** Segments
- **열:** 이메일 참여 측정기준

### 배리언트 또는 단계의 측정기준 보기 {#viewing-metrics-for-variants-or-steps}

캠페인 배리언트, 캔버스 배리언트 또는 캔버스 단계 수준에서 Segment별로 분류된 이메일 성과를 보려면 먼저 배리언트 또는 단계 수준 보고서(제목에 "배리언트 또는 단계별"이 포함된 보고서)를 선택한 다음 **변수** 탭을 사용하여 다음을 지정합니다:

- 특정 Campaign 또는 Canvas (배리언트 또는 단계 수준 보고서를 사용하는 경우 필수)
- 배리언트 (배리언트 또는 단계 수준 보고서를 사용하는 경우 필수)
- 캔버스 단계 (선택 사항)

측정기준은 [Campaign 또는 Canvas 수준](#campaign-canvas-email) 템플릿에서 제공되는 것과 동일합니다. 여러 배리언트를 선택하면 결과가 배리언트별로 그룹화됩니다.

#### 결과

선택한 배리언트 또는 단계에 대한 Segment별 이메일 참여 측정기준이 결과에 표시됩니다.

- **행:** Segments
- **열:** 이메일 참여 측정기준

{% endtab %}

{% tab Segment별 구매 및 매출 %}
### Campaigns 또는 Canvases의 측정기준 보기 {#viewing-metrics-for-campaigns-or-canvases}

특정 Campaign 또는 Canvas에 대해 Segment별로 분류된 구매 및 매출 측정기준을 보려면 [변수](#variables) 탭을 사용하여 다음을 지정합니다:

- 전환 기간 (이메일 수신 또는 클릭 후 Braze가 구매 또는 매출을 귀속시키는 일수)
- 특정 제품 (선택 사항)

또한 **변수** 탭을 사용하여 하나 이상의 Campaigns 또는 Canvases, 또는 하나 이상의 태그에 대해 보고서를 실행할지 지정합니다. Campaigns, Canvases 또는 태그를 선택하지 않으면 선택한 기간 동안 Campaigns 또는 Canvases의 모든 이메일에 대해 보고서가 실행됩니다.

현재 이 보고서는 이메일 채널의 측정기준만 가져옵니다. 이메일 이외의 채널에서 발생한 매출 또는 구매 데이터는 보고서에 반영되지 않습니다.

이메일에 사용할 수 있는 측정기준은 다음과 같습니다:

- 수신 후 고유 구매 수
- 수신 후 매출
- 클릭 후 고유 구매 수
- 클릭 후 매출
- 고유 수신자 수
- 고유 이메일 클릭 수

모든 비율 측정기준은 고유 이메일 수신자 수를 분모로 사용합니다.

#### 정의 {#definitions}

- "수신 후"는 사용자가 지정된 Campaigns 또는 Canvases를 수신한 후 지정된 전환 기간 내에 발생한 구매 이벤트 또는 매출을 의미합니다.
- "클릭 후"는 사용자가 지정된 Campaigns 또는 Canvases를 클릭한 후 지정된 전환 기간 내에 발생한 구매 이벤트 또는 매출을 의미합니다.

예를 들어, Segment에 10명의 사용자가 있고 그 중 5명이 이메일을 수신한 후 구매했다고 가정합니다. 그 5명 중 1명이 이메일을 클릭한 후 구매했다면, "수신 후 고유 구매율"은 50%이고 "클릭 후 고유 구매율"은 10%입니다.

![보고서에는 수신 후 고유 구매 수, 수신 후 매출, 클릭 후 고유 구매 수, 클릭 후 매출, 고유 수신자 수, 고유 이메일 클릭 수를 포함한 이메일 측정기준이 표시됩니다.]({% image_buster /assets/img_archive/segment_breakdown_results.png %})

#### 결과

선택한 Campaigns 또는 Canvases에 대한 Segment별 구매 측정기준이 결과에 표시됩니다. 특정 Campaigns 또는 Canvases를 선택하지 않은 경우, 보고서 기간 내 모든 이메일 Campaigns 또는 Canvases에 대한 각 Segment의 구매 측정기준이 표시됩니다.

- **행:** Segments
- **열:** 구매 측정기준


### 배리언트 또는 단계의 측정기준 보기

특정 캠페인 배리언트, 캔버스 배리언트 또는 캔버스 단계에 대해 Segment별로 분류된 구매 및 매출 측정기준을 보려면 [변수](#variables) 탭을 사용하여 다음을 지정합니다:

- 특정 Campaign 또는 Canvas
- 배리언트
- 캔버스 단계 (선택 사항)
- 기간
- 특정 제품 (선택 사항)

#### 결과

선택한 배리언트 또는 단계에 대한 Segment별 구매 측정기준이 결과에 표시됩니다.

- **행:** Segments
- **열:** 구매 측정기준

{% endtab %}
{% tab 이메일 참여 상위 또는 하위 메시징 %}

### 상위 또는 하위 성과의 측정기준 보기 {#viewing-metrics-for-the-top-or-bottom-performers}

이 보고서는 [변수](#variables) 탭에서 지정된 이메일 참여 측정기준에 대해 가장 높거나 낮은 성과를 보인 Campaigns, Canvases 또는 캔버스 단계를 표시합니다.

활용 사례는 다음과 같습니다:
- 고유 이메일 열람률이 가장 높은 상위 10개 Campaigns
- 이메일 탈퇴가 가장 많은 상위 25개 Canvases
- 고유 클릭 수가 가장 높은 상위 50개 캔버스 단계

이 보고서에서 사용할 수 있는 이메일 측정기준은 다음과 같습니다:
- 발송 수
- 전달 수
- 불만 수
- 고유 열람 수
- 고유 기계 열람 수
- 고유 비기계 열람 수
- 고유 클릭 수
- 탈퇴 수
- 반송 수
- 소프트바운스 수
- 불만 수

이 보고서를 보려면 **변수** 탭에서 다음 변수를 지정해야 합니다:
- **측정기준:** 결과를 순위 매길 측정기준 중 하나를 선택합니다
- **보고서 수:** 상위 또는 하위 결과와 결과 수를 선택합니다(예: 상위 10개 또는 하위 15개)
- **메시지 유형:** 결과가 Campaigns, Canvases 또는 캔버스 단계인지 지정합니다

#### 결과

선택한 상위(또는 하위) Campaigns, Canvases 또는 캔버스 단계가 결과에 표시됩니다. 예를 들어, 클릭률 상위 10개 Campaigns를 선택한 경우 클릭률이 가장 높은 순서에서 낮은 순서로 정렬된 상위 10개 Campaigns가 결과에 표시됩니다. 각 행(Campaigns, Canvases 또는 메시지 단계)에 대한 모든 이메일 참여 측정기준이 열에 표시됩니다.

{% endtab %}
{% tab 구매 상위 또는 하위 메시징 %}

### 상위 또는 하위 성과의 측정기준 보기

이 보고서는 [변수](#variables) 탭에서 지정된 구매 또는 매출 측정기준에 대해 가장 높거나 낮은 성과를 보인 Campaigns, Canvases 또는 캔버스 단계를 표시합니다.

활용 사례는 다음과 같습니다:
- 특정 제품에 대한 구매율이 가장 높은 상위 20개 Campaigns
- 매출이 가장 많이 발생한 상위 25개 Canvases
- 제품 구매율이 가장 낮은 하위 10개 캔버스 단계

이 보고서에서 사용할 수 있는 이메일 측정기준은 다음과 같습니다:
- 수신 후 고유 구매 수
- 수신 후 매출
- 클릭 후 고유 구매 수
- 클릭 후 매출
- 고유 수신자 수
- 고유 이메일 클릭 수

이 보고서를 보려면 **변수** 탭에서 다음 변수를 지정해야 합니다:
- **측정기준:** 결과를 순위 매길 측정기준 중 하나를 선택합니다
- **보고서 수:** 상위 또는 하위 결과와 결과 수를 선택합니다(예: 상위 10개 또는 하위 15개)
- **메시지 유형:** 결과가 Campaigns, Canvases 또는 캔버스 단계인지 지정합니다
- **전환 기간:** 이메일 수신 또는 클릭 후 Braze가 구매 또는 매출을 귀속시키는 일수

#### 정의

- "수신 후"는 사용자가 지정된 Campaigns 또는 Canvases를 수신한 후 지정된 전환 기간 내에 발생한 구매 이벤트 또는 매출을 의미합니다.
- "클릭 후"는 사용자가 지정된 Campaigns 또는 Canvases를 클릭한 후 지정된 전환 기간 내에 발생한 구매 이벤트 또는 매출을 의미합니다.

예를 들어, Segment에 10명의 사용자가 있고 그 중 5명이 이메일을 수신한 후 구매했다고 가정합니다. 그 5명 중 1명이 이메일을 클릭한 후 구매했다면, "수신 후 고유 구매율"은 50%이고 "클릭 후 고유 구매율"은 10%입니다.

#### 결과

선택한 상위(또는 하위) Campaigns, Canvases 또는 캔버스 단계가 결과에 표시됩니다. 예를 들어, "클릭 후 매출" 상위 10개 Campaigns를 선택한 경우 "클릭 후 매출"이 가장 높은 순서에서 낮은 순서로 정렬된 상위 10개 Campaigns가 결과에 표시됩니다. 각 행(Campaigns, Canvases 또는 메시지 단계)에 대한 모든 구매 측정기준이 열에 표시됩니다.

{% endtab %}
{% tab Segment별 푸시 성과 %}

### Segment별 푸시 측정기준 보기 {#viewing-push-metrics-for-segments}

이 보고서는 [변수](#variables) 탭에서 Segment별로 분류된 푸시 측정기준을 표시합니다.

**변수** 탭에서 측정기준을 볼 Campaigns 또는 Canvases와 데이터를 가져올 기간을 지정합니다. Campaigns 또는 Canvases를 선택하지 않으면 지정된 기간 내 모든 Campaigns 및 Canvases의 푸시가 보고서에 표시됩니다. 특정 태그가 있는 모든 Campaigns 및 Canvases를 볼 수도 있습니다.

이 보고서에서 사용할 수 있는 푸시 측정기준은 다음과 같습니다:

- 발송 수
- 반송 수
- 전달 수
- 직접 열람 수

#### 결과

보고서에 다음 결과가 표시됩니다:

- **행:** Segments
- **열:** 푸시 측정기준
{% endtab %}
{% endtabs %}