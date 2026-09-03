---
nav_title: Segment 보고
article_title: 보고서 빌더의 Segment 보고
permalink: /segment_reporting_report_builder/
description: "이 참고 문서에서는 보고서 빌더에서 Segment를 보고 차원으로 사용하는 방법, Segment별 보고 방법, Segment별 세분화 방법, 지원되는 조합에 대해 설명합니다."
hidden: true
noindex: true
page_type: reference
---

# 보고서 빌더의 Segment 보고 {#segment-reporting-in-report-builder}

> 이 문서에서는 보고서 빌더에서 Segment를 보고 차원으로 사용하는 방법, Segment별 보고 방법, Segment별 세분화 방법, 지원되는 조합에 대해 설명합니다.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Segment reporting' contact='customer success 매니저' %}

보고서 빌더는 행 및 드릴다운 옵션으로 **Segments**를 지원하므로, Segment의 성능을 확인하고 Campaign 또는 Canvas 성능을 Segment 멤버십별로 세분화할 수 있습니다. **행** 또는 **드릴다운** 드롭다운에 **Segments**가 표시되지 않는 경우, 해당 기능이 계정에 활성화되지 않은 것입니다.

다음과 같은 질문에 답할 수 있습니다:

- 특정 Segment가 시간에 따라 어떤 성능을 보이고 있는가?
- 어떤 Campaigns와 Canvases가 특정 Segment를 타겟팅하고 있으며, 각각의 성능은 어떠한가?
- 단일 Campaign 또는 Canvas에 대해 Segment 간 인게이지먼트를 어떻게 비교할 수 있는가?

{% alert note %}
Segment 보고는 [분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)이 활성화된 Segment에서만 사용할 수 있습니다. **행** 드롭다운에서 **Segments**를 선택하려면 워크스페이스 수준의 ["대시보드 보고서 보기" 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 필요합니다.
{% endalert %}

## Segment별 보고 {#report-on-segments}

Segment를 직접 보고하려면 다음을 수행합니다:

1. **Analytics** > **보고서 빌더(신규)**로 이동합니다.
2. **새 보고서 생성**을 클릭합니다.
3. **행** 드롭다운에서 **Segments**를 선택합니다.
4. (선택 사항) **드릴다운 추가**를 선택하여 Segment 데이터를 더 세분화합니다:
   - **Campaigns 및 Canvases:** 해당 Segment를 타겟팅한 Campaigns와 Canvases, 그리고 각각의 성능을 확인합니다.
   - **날짜:** Segment의 크기 또는 성능 추이를 시간에 따라 확인합니다. 꺾은선형 차트와 함께 사용하면 추이를 시각화할 수 있습니다.
5. **보고서 콘텐츠**에서 **Segments** 드롭다운을 열고 보고서에 추가할 Segment를 선택합니다.
6. **열** > **측정기준 커스터마이즈**에서 측정기준을 선택한 다음, **보고서 콘텐츠**에서 날짜 범위를 설정합니다.
7. **Campaigns 및 Canvases** 드릴다운을 추가한 경우, 보고서에 포함할 Campaigns와 Canvases를 추가합니다.
8. **저장 및 실행**을 클릭합니다.

전체 보고서 빌더 워크플로는 [보고서 생성]({{site.baseurl}}/user_guide/analytics/reports/report_builder#creating-a-report)을 참조하세요.

## Segment별 드릴다운 {#drill-down-by-segment}

Campaign, Canvas 또는 채널 보고서를 Segment별로 드릴다운하려면 다음을 수행합니다:

1. **행** 드롭다운에서 **Campaigns**, **Canvases** 또는 **Campaigns 및 Canvases**를 선택합니다.
2. **드릴다운 추가**를 선택하고 **Segment**를 선택합니다.
3. **보고서 콘텐츠**에서 **Segments** 드롭다운을 열고 보고서에 추가할 Segment를 선택합니다.
4. **열** > **측정기준 커스터마이즈**에서 측정기준을 선택한 다음, **보고서 콘텐츠**에서 날짜 범위를 설정합니다.
5. 보고서에 포함할 Campaigns 또는 Canvases를 추가합니다.
6. **저장 및 실행**을 클릭하면 Campaigns 또는 Canvases가 타겟팅한 각 Segment별로 세분화된 성능을 확인할 수 있습니다.

이 기능은 동일한 Campaign 또는 Canvas를 여러 Segment에 발송하는 워크스페이스에 특히 유용합니다. Segment 멤버십과 Campaign 성능을 수동으로 교차 참조하지 않고도 각 Segment가 어떻게 반응했는지 확인할 수 있습니다.

## 지원되는 조합 {#supported-combinations}

Segment 보고에 지원되는 **행** 및 **드릴다운** 조합은 다음과 같습니다:

| 행 | 드릴다운 |
| ----- | ----- |
| Segment | Campaigns 및 Canvases |
| Segment | 날짜 |
| Campaign | Segment |
| Campaign | 배리언트 |
| Canvas | Segment |
| Campaigns 및 Canvases | Segment |
{: .reset-td-br-1 .reset-td-br-2 aria-label="지원되는 행 및 드릴다운 조합"}

{% alert note %}
보고서 빌더는 한 번에 하나의 드릴다운만 지원합니다. **행** 드롭다운에서 **Campaigns**를 선택한 경우, **배리언트** 또는 **Segment**로 드릴다운할 수 있지만 동일한 보고서에서 두 가지를 동시에 사용할 수는 없습니다.
{% endalert %}

## 측정기준 사용 가능 여부 {#metrics-availability}

Segment별 보고 시 모든 보고서 빌더 측정기준을 사용할 수 있는 것은 아닙니다. 선택할 수 있는 측정기준은 **Segments**가 **행**에 있는지 **드릴다운**에 있는지, 그리고 보고서에 Campaign 또는 Canvas 차원이 포함되어 있는지에 따라 달라집니다.

| 측정기준 | 사용 가능 여부 |
| ----- | ----- |
| 채널 및 일반 메시징 측정기준 | 지원되는 행 및 드릴다운 조합에서 사용 가능합니다. |
| 전환 횟수(전환 A–D) 및 전환 이벤트 이름 | Segment와 Campaign 또는 Canvas 차원이 함께 표시될 때 사용 가능합니다. **Segments**를 행에 배치하고 **Campaigns 및 Canvases** 드릴다운을 사용하거나, **Campaigns**, **Canvases** 또는 **Campaigns 및 Canvases**를 행에 배치하고 **Segment** 드릴다운을 사용합니다. |
| 매출 및 전환율 | Segment 차원 보고서에서는 사용할 수 없습니다. |
| Segment 구매 매출 및 횟수 | **Segments**가 행에 있을 때만 사용 가능합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment 보고 측정기준 사용 가능 여부"}

행 및 드릴다운 선택이 측정기준에 미치는 영향에 대한 자세한 내용은 보고서 빌더의 [측정기준 사용 가능 여부]({{site.baseurl}}/user_guide/analytics/reports/report_builder#metrics-availability)를 참조하세요.