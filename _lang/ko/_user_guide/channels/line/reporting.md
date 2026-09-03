---
nav_title: 보고서
article_title: LINE 보고서
page_order: 21
description: "이 참조 문서에서는 Braze에서 사용되는 LINE 측정기준과 LINE Campaign에서 이를 확인하는 방법을 다룹니다."
page_type: reference
channel:
 - LINE
alias: /line/reporting/
---

# LINE 보고서 {#line-reporting}

> Campaign 또는 Canvas를 시작한 후 Campaign 세부 정보 페이지 또는 Canvas 분석에서 주요 측정기준을 확인할 수 있습니다. 이 문서에서는 해당 측정기준을 찾을 수 있는 위치와 각 측정기준이 나타내는 의미를 설명합니다.

{% alert tip %}
보고서에 사용되는 용어와 측정기준의 정의를 찾고 계신가요? [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/analytics/metrics_glossary)을 참조하세요.
{% endalert %}

## Campaign 분석 {#campaign-analytics}

**Campaign Analytics** 탭에서 일련의 패널로 보고서를 확인할 수 있습니다. 아래 섹션에 나열된 것보다 더 많거나 적은 패널이 표시될 수 있지만, 각 패널에는 고유한 목적이 있습니다.

{% alert note %}
LINE의 열람 및 클릭 관련 통계는 특정 날짜에 20명 이상의 사용자가 해당 이벤트를 수행한 경우에만 계산됩니다.
{% endalert %}

### Campaign 세부 정보 {#campaign-details}

**Campaign Details** 패널에는 LINE 메시지 성과에 대한 상위 수준 개요가 표시됩니다.

이 패널에서 수신자에게 발송된 메시지 수, 주요 전환율, 이 메시지로 발생한 총 매출 등의 전체 측정기준을 확인할 수 있습니다. 또한 이 페이지에서 전달, 오디언스 및 전환 설정을 검토할 수 있습니다.

#### 대조군 {#control-groups}

개별 LINE 메시지의 영향을 측정하려면 A/B 테스트에 [대조군]({{site.baseurl}}/user_guide/messaging/ab_testing)을 추가할 수 있습니다. 최상위 **Campaign Details** 패널에는 대조군 배리언트의 측정기준이 포함되지 않습니다.

### LINE 성과 {#line-performance}

**LINE Performance** 패널에는 메시지가 다양한 차원에서 얼마나 잘 수행되었는지가 표시됩니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트 실행 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **Preview** 아이콘을 클릭하면 각 배리언트 또는 채널에 대한 메시지를 확인할 수 있습니다.

![두 배리언트에 대한 측정기준을 보여주는 'LINE Performance' 패널.]({% image_buster /assets/img/line/line_performance.png %})

보기를 간소화하려면 **\+ Add/Remove Columns**를 선택하고 원하는 측정기준을 해제합니다. 기본값으로 모든 측정기준이 표시됩니다.

#### LINE 측정기준 {#line-metrics}

다음은 분석에서 확인할 수 있는 주요 LINE 측정기준입니다. Braze에서 사용되는 모든 LINE 측정기준의 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/analytics/metrics_glossary)을 참조하세요.

| 용어 | 정의 |
| --- | --- |
| 발송 수 | Braze와 LINE 간에 성공적으로 전달된 총 발송 수입니다. 이는 사용자가 메시지를 수신했음을 의미하지는 않습니다. |
| 고유 열람 수 | 하루 최소 20건의 메시지 임계값에 도달한 후 사용자가 열람한 LINE 메시지의 총 수입니다. |
| 총 열람 수 | 하루 최소 20건의 메시지 임계값에 도달한 후 사용자가 발송된 LINE 메시지를 열람한 총 횟수입니다. |
| 고유 클릭 수 | 하루 최소 20건의 메시지 임계값에 도달한 후 사용자가 클릭한 LINE 메시지의 총 수입니다. |
| 총 클릭 수 | 하루 최소 20건의 메시지 임계값에 도달한 후 사용자가 발송된 LINE 메시지를 클릭한 총 횟수입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE 측정기준" }

### 과거 성과 {#historical-performance}

**Historical Performance** 패널에서는 **Message Performance** 패널의 측정기준을 시간 경과에 따른 그래프로 확인할 수 있습니다. 패널 상단의 필터를 사용하여 그래프에 표시되는 통계와 채널을 수정할 수 있습니다. 이 그래프의 시간 범위는 항상 페이지 상단에 지정된 시간 범위와 동일합니다.

일별 분석을 확인하려면 <i class="fas fa-bars"></i> 햄버거 메뉴를 선택하고 **Download CSV**를 선택하여 보고서의 CSV 내보내기를 받을 수 있습니다.

### 전환 이벤트 세부 정보 {#conversion-event-details}

**Conversion Event Details** 패널에는 Campaign의 전환 이벤트 성과가 표시됩니다. 자세한 내용은 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/conversion_correlation)를 참조하세요.

### 전환 상관관계 {#conversion-correlation}

**Conversion Correlation** 패널에서는 어떤 사용자 속성과 동작이 Campaign에 설정한 성과에 도움이 되거나 방해가 되는지에 대한 인사이트를 제공합니다. 자세한 내용은 [전환 상관관계]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/conversion_correlation)를 참조하세요.