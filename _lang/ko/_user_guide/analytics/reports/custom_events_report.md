---
nav_title: 사용자 지정 이벤트 보고서
article_title: 사용자 지정 이벤트 보고서
page_order: 6
page_type: reference
description: "이 페이지에서는 사용자 지정 이벤트 보고서를 사용하여 Segment별로 분류된 커스텀 이벤트의 발생 추이를 확인하는 방법을 설명합니다."
tool: Reports
---

# 사용자 지정 이벤트 보고서 {#custom-events-report}

> 사용자 지정 이벤트 보고서를 사용하면 하나 이상의 커스텀 이벤트가 시간에 따라 발생한 추이를 확인할 수 있습니다. Segment별로 결과를 분류하고, KPI 수식을 적용하며, 추가 분석을 위해 데이터를 내보낼 수 있습니다.

## 보고서 보기 {#viewing-a-report}

대시보드에서 이 보고서를 보려면 **분석** > **사용자 지정 이벤트 보고서**로 이동합니다. 분석하려는 커스텀 이벤트를 선택한 다음 **Apply**를 선택하여 그래프를 생성합니다.

![커스텀 이벤트]({% image_buster /assets/img_archive/Export_events.png %})

## 보고서 구성하기 {#configuring-your-report}

다음 옵션을 사용하여 **Performance Over Time** 그래프에 표시되는 데이터를 커스터마이즈할 수 있습니다.

| 옵션 | 설명 |
| --- | --- |
| Apps | 기본적으로 보고서에는 모든 앱의 데이터가 포함됩니다. 이 드롭다운을 사용하여 보고서를 특정 앱으로 좁힐 수 있습니다. |
| Breakdown custom events by | 선택한 커스텀 이벤트의 시계열이 그룹화되는 방식을 제어합니다. 기본적으로 차트는 날짜별 전체 집계 추세를 표시합니다. **Custom Events by Hour**로 전환하면 일중 패턴을 확인할 수 있고, **Custom Events per MAU**로 전환하면 월간 활성 사용자 수 대비 이벤트 볼륨을 정규화할 수 있습니다. |
| Filter by Segments | 이 옵션을 토글하면 하나 이상의 Segment별로 이벤트 수를 분류할 수 있습니다. 활성화하면 비교하려는 Segments를 선택합니다. 그래프에는 각 Segment에서 커스텀 이벤트를 수행한 사용자 수가 표시됩니다. |
| KPI formula | 원시 이벤트 수를 분자(예: 커스텀 이벤트 수)와 분모(예: DAU, MAU 또는 분석이 활성화된 Segment 크기)로 구성된 계산 측정기준으로 대체합니다. 하나 이상의 수식을 선택하면 차트에 선택한 기간 동안 각 수식의 값이 표시되어 총 이벤트 볼륨 대신 정규화된 성과(예: "활성 사용자당 이벤트")를 비교할 수 있습니다. 선택한 기간과 수식에 대해 사용 가능한 데이터가 없는 경우 Braze는 "데이터 없음" 메시지를 표시합니다. 기간을 넓히거나 다른 수식을 선택해 보세요. **Manage KPI formulas**를 선택하여 수식을 생성하거나 편집할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 데이터 내보내기 {#exporting-data}

커스텀 이벤트 데이터를 내보내려면 **Performance Over Time** 그래프에서 <i class="fas fa-bars" title="Chart context menu"></i>를 선택한 다음 내보내기 옵션을 선택합니다.

{% alert tip %}
CSV 및 API 내보내기에 대한 도움이 필요하면 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}