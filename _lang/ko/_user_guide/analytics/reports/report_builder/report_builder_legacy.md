---
nav_title: 보고서 빌더 (레거시)
article_title: 보고서 빌더 (레거시)
alias: /report_builder_legacy/
page_order: 1
page_type: reference
description: "이 페이지에서는 레거시 보고서 빌더를 사용하여 Campaign 및 Canvas 비교 보고서 생성, 보고서 및 차트 작성 등 보고서를 실행하는 방법을 다룹니다."
tool:
  - Reports

---

# 보고서 빌더 (레거시) {#report-builder-legacy}

> 보고서 빌더를 사용하면 여러 Campaign 또는 Canvases의 결과를 단일 뷰에서 비교할 수 있으므로, 어떤 참여 전략이 핵심 측정기준에 가장 큰 영향을 미쳤는지 쉽게 파악할 수 있습니다. Campaign과 Canvases 모두에서 데이터를 내보내고 보고서를 저장하여 나중에 확인할 수 있습니다.<br><br>보고서에서 확인할 수 있는 측정기준의 상세 목록은 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/analytics/metrics_glossary)을 참조하세요.

![Campaign 비교 예시]({% image_buster /assets/img/campaign_comparison/campaign_main.png %}){: style="max-width:80%;"}

이 보고서를 사용하여 다음과 같은 주요 참여 관련 질문에 답할 수 있습니다:

- 특정 태그 또는 채널에서 가장 성과가 좋은 Campaign 또는 Canvases는 무엇이었나요?
- 다변량 Campaign의 어떤 배리언트가 대조군 대비 가장 높은 상승 효과를 보였나요?
- 어떤 시즌 프로모션 Campaign이 더 높은 구매율을 이끌었나요—여름 세일, 가을 세일, 겨울 세일 중 어느 것인가요?
- 이 Canvas 내에서 어떤 푸시 알림이 가장 높은 열람률을 기록했나요?
- 이 Canvases 그룹에서 어떤 단계가 가장 많은 전환을 이끌었나요?
- 환영 이메일 버전 1과 버전 2 중 어느 것이 더 높은 참여와 전환을 이끌었나요? 변경 사항이 효과가 있었나요?
- 서로 다른 전달 방법(예: 3개의 스케줄된 푸시, 3개의 액션 기반 푸시, 3개의 API 트리거 푸시)이 열람률, 전환율 또는 구매율에 어떤 영향을 미치나요?
- 이탈 위험 사용자 메시지에 대한 지속적인 개선이 시간이 지남에 따라 KPI에 긍정적인 영향을 미쳤나요?

{% alert tip %}
비교하려는 Campaign과 Canvases 전체에서 전환 A, B 등에 동일한 전환 이벤트를 사용해 보세요. 그러면 보고서 빌더 보고서에서 이러한 전환을 정렬할 수 있습니다.
{% endalert %}

## 보고서 실행 {#running-a-report}

### 1단계: 새 보고서 생성 {#step-1-create-a-new-report}

대시보드에서 **Analytics** > **보고서 빌더**로 이동합니다.

**새 보고서 생성**을 선택하고 Campaign 비교 보고서 또는 Canvas 비교 보고서 중 하나를 선택합니다.

Campaign에 대한 보고서를 실행하려면 **수동** 또는 **자동** 보고서 중에서 선택할 수 있습니다. 보고서에는 Campaign 또는 Canvases 중 하나만 포함할 수 있으며, 둘을 함께 포함할 수는 없습니다. 지난 12개월 이내에 마지막으로 메시지를 보낸 모든 Campaign과 Canvases가 보고서에 포함될 수 있습니다.

![Campaign 대시보드]({% image_buster /assets/img/campaign_comparison/create_report.png %}){: style="max-width:80%;"}

다음은 두 옵션의 차이점입니다:

| **동작** | **수동** | **자동** |
| ---- | ---------- | ------------- |
| **보고서 작성** | 필터를 사용하여 Campaign 목록을 좁힌 다음 특정 Campaign을 선택할 수 있습니다. | 필터 옵션을 사용하여 Campaign 목록을 좁혀 보고서를 작성합니다. |
| **보고서 저장 및 보기** | 보고서를 저장할 수 있습니다. 다음에 볼 때 이전에 추가한 동일한 Campaign을 볼 수 있으며, 이는 해당 Campaign이 여전히 "마지막 발송" 필터에 해당하기 때문입니다. | 보고서를 저장할 수 있습니다. 다음에 볼 때 보고서가 현재 필터와 일치하는 모든 Campaign을 포함하도록 자동으로 업데이트됩니다. |
| **보고서 편집** | **보고서 편집**을 선택하여 보고서에서 Campaign을 추가하거나 삭제할 수 있습니다. | 필터 기준을 조정하여 보고서를 편집할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="1단계: 새 보고서 생성" }

{% alert note %}
**수동** 및 **자동** 보고서 모두 하나의 보고서에 최대 250개의 Campaign을 포함할 수 있습니다.
{% endalert %}

Canvas 보고서는 수동 Campaign 보고서와 유사하게 작동하며, Canvas 선택 및 보고서 업데이트도 수동으로 수행해야 합니다. 하나의 보고서에 최대 5개의 Canvases를 포함할 수 있습니다.

### 2단계: 측정기준 선택 {#step-2-choose-your-metrics}

보고서를 생성하면 각 행에 Campaign이 포함된 빈 테이블이 표시됩니다. **열 편집**을 선택하고 추가할 측정기준을 선택하면 테이블이 채워집니다.

![Campaign 옵션]({% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}){: style="max-width:80%;"}

선택한 측정기준으로 테이블이 채워집니다. 이러한 측정기준의 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/analytics/metrics_glossary)을 참조하세요. 일부 측정기준은 Campaign 비교 보고서에서만 사용할 수 있습니다.

또한 모든 비율 또는 수치 측정기준의 **평균** 계산과 모든 수치 측정기준의 **합계** 계산을 토글할 수 있습니다.

### 3단계: 기간 선택 {#step-3-choose-a-time-period}

특정 기간을 선택하여 보고서 데이터를 확인할 수 있습니다. 특정 Campaign, Canvas, 캔버스 배리언트 또는 Canvas 구성요소에 선택한 기간에 대한 데이터가 없는 경우 해당 행의 결과는 비어 있습니다.

![Campaign 수치 측정기준]({% image_buster /assets/img/campaign_comparison/metric.png %}){: style="max-width:60%;"}

### 4단계: 보고서 이름 지정 및 저장 {#step-4-name-and-save-your-report}

저장하기 전에 보고서 이름을 지정하세요. 이름을 지정하지 않고 보고서를 저장하면 Braze에서 "Campaign Comparison Report"라는 기본 이름이 적용됩니다.

![Campaign 메모]({% image_buster /assets/img/campaign_comparison/comparison_name.png %}){: style="max-width:60%;"}

준비가 되면 **저장**을 선택합니다. 저장된 보고서는 나중에 **보고서 빌더** 페이지에서 확인할 수 있습니다.

## 다변량 Campaign의 Campaign 비교 보고서 {#campaign-comparison-report-with-multivariate-campaigns}

다변량 Campaign의 경우 Campaign 이름 옆의 화살표를 클릭하면 배리언트 및 대조군별로 분류된 측정기준을 확인할 수 있습니다. 배리언트가 포함된 행에는 해당 배리언트의 성과 결과가 표시되고, 대조군이 포함된 행에는 전환 이벤트 결과만 표시됩니다.

![Campaign 메모]({% image_buster /assets/img/campaign_comparison/compare_note.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

전체 Campaign 행에 표시되는 측정기준은 배리언트의 성과를 반영하지만 대조군의 성과는 포함하지 않습니다. 예를 들어, 전체 Campaign의 주요 전환 이벤트 A는 배리언트의 주요 전환 이벤트 A의 합계이며, 대조군의 주요 전환 이벤트 A는 포함되지 않습니다.

{% alert important %}
다변량 Campaign에서 배리언트를 삭제하면 해당 배리언트의 데이터는 향후 보고서에서 사용할 수 없습니다.
{% endalert %}

## Canvas 비교 보고서 분석 {#canvas-comparison-report-breakdown}

Canvas 보고서 내에서 배리언트, 단계 또는 메시지별로 Canvases를 분류하여 확인할 수 있습니다.

### 배리언트 {#variant}

**배리언트별 분류**를 선택하면 전체 Canvases의 상위 수준 통계와 각 배리언트의 통계를 확인할 수 있으며, Canvas 이름 옆의 화살표를 선택하여 확장할 수 있습니다.

![배리언트]({% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}){: style="max-width:90%;"}

### 단계 {#steps}

**단계별 분류**를 선택하면 단계 수준의 측정기준을 확인할 수 있으며, 보고서의 각 행에 단계가 표시됩니다.

![단계]({% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}){: style="max-width:90%;"}

### 메시지 {#message}

단계 수준 분류와 유사하게, **메시지별 분류**를 선택하면 각 행에 단계 이름이 표시됩니다. 그러나 **열 편집** 내에서 이메일 클릭 수 및 푸시 열람 수와 같은 채널별 통계 등 메시지 수준 측정기준에 접근할 수 있습니다.

![보고서]({% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}){: style="max-width:90%;"}

Braze 대시보드에서는 Canvas 보고서의 처음 50개 행을 미리 볼 수 있습니다. CSV를 내보내면 전체 보고서에 접근할 수 있습니다.

## 저장된 보고서 접근 {#accessing-saved-reports}

저장된 **수동 보고서**에 접근하면 이전에 추가한 동일한 Campaign을 볼 수 있으며, 이는 해당 Campaign이 여전히 "마지막 발송" 필터에 해당하기 때문입니다.

저장된 **자동 보고서**에 접근하면 보고서가 현재 필터와 일치하는 모든 Campaign을 포함하도록 자동으로 업데이트됩니다. 예를 들어, 보고서가 "프로모션" 태그가 있는 Campaign을 필터링한 경우, 이 보고서를 볼 때마다 보고서를 만든 후에 생성된 Campaign이라도 "프로모션" 태그가 있는 모든 Campaign을 확인할 수 있습니다.

## 보고서 편집 {#editing-reports}

**수동 보고서**에서는 **편집**을 선택하여 보고서를 편집할 수 있습니다. 여기에서 보고서에 포함할 Campaign을 선택하거나 선택 해제할 수 있습니다.

**자동 보고서**에서는 필터를 토글하여 보고서의 결과를 좁힐 수 있습니다.

## 보고서 내보내기 {#exporting-reports}

**내보내기**를 선택하여 보고서를 CSV로 다운로드할 수도 있습니다.

보고서에 다변량 Campaign이 포함된 경우 내보내기에는 두 개의 CSV 파일이 포함됩니다:

- 각 Campaign의 상위 수준 측정기준만 포함하는 파일
- 배리언트 수준 측정기준을 포함하는 파일

배리언트 측정기준이 포함된 파일의 이름 앞에는 `variant_`가 추가됩니다. 자동 보고서를 처음 내보낼 때 여러 파일 다운로드 권한을 요청하는 팝업이 표시됩니다. **허용**을 클릭하세요.

![Campaign 다운로드]({% image_buster /assets/img/campaign_comparison/download.png %}){: style="max-width:60%;"}

### Canvas 비교 보고서 내보내기 {#exporting-canvas-comparison-reports}

CSV 내보내기는 **내보내기**를 선택했을 때 보고 있던 분류 뷰를 반영합니다. 예를 들어, 단계 수준 분류 뷰에 있었다면 내보내기에는 단계 측정기준에 대한 데이터가 포함됩니다. 다른 분류의 데이터를 내보내려면 먼저 해당 분류로 이동한 다음 거기에서 **내보내기**를 선택해야 합니다.

배리언트 분류 Canvas 보고서를 다운로드하면 두 개의 CSV 파일을 받게 됩니다:

- 각 Canvas의 상위 수준 측정기준만 포함하는 파일
- 배리언트 수준 측정기준을 포함하는 파일

## 차트 작성 {#building-charts}

차트를 사용하여 보고서에서 선택한 측정기준을 시각화할 수 있습니다. 차트는 Campaign이 포함되어 있고 열에 하나 이상의 측정기준이 추가된 보고서에서 사용할 수 있습니다.

![메시지 발송 측정기준이 선택된 Campaign 성과 차트]({% image_buster /assets/img/campaign_comparison/report_builder_charts.png %})

기본적으로 각 보고서의 차트는 보고서 첫 번째 열의 측정기준을 표시합니다. 그래프에 표시할 다른 측정기준을 선택하려면 드롭다운에서 측정기준을 선택하세요. 보고서 테이블의 모든 측정기준을 차트에 표시할 수 있습니다.

최대 3개의 측정기준을 그래프로 표시할 수 있습니다. 모든 측정기준의 단위는 동일해야 합니다. 예를 들어, 첫 번째 드롭다운에서 비율을 선택하면 두 번째 드롭다운에서도 비율만 선택할 수 있습니다.

차트에 하나의 측정기준만 포함된 경우 선택한 측정기준을 기준으로 내림차순으로 최대 30개의 Campaign이 표시됩니다. 예를 들어, 차트의 측정기준이 이메일 클릭 수인 경우 차트에는 클릭 수가 가장 많은 30개의 이메일 Campaign이 가장 많은 것부터 가장 적은 순서로 표시됩니다. 보고서에 30개 이상의 Campaign이 포함된 경우 상위 30개만 차트에 표시됩니다. 두 개 이상의 측정기준을 선택하면 첫 번째로 선택한 측정기준을 기준으로 상위 5개 Campaign만 그래프에 표시됩니다.

현재 보고서를 저장할 때 차트는 저장되지 않습니다.