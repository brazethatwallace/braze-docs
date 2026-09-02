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

## 보고서 보기 {#view-a-report}

대시보드에서 이 보고서를 보려면 **Analytics** > **Custom Events Report**로 이동하세요. 분석하려는 커스텀 이벤트를 선택합니다. 이벤트를 선택하면 그래프가 자동으로 렌더링됩니다.

![커스텀 이벤트]({% image_buster /assets/img_archive/Export_events.png %})

### API 커스텀 이벤트 및 앱 필터 {#api-custom-events-and-app-filters}

[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트를 통해 전송된 커스텀 이벤트에는 선택적으로 `app_id`를 포함할 수 있습니다. SDK를 통해 기록된 이벤트와 달리, API 이벤트는 자동으로 앱에 연결되지 않습니다. `app_id`가 없으면 이벤트는 기록되지만, 앱 필터가 적용된 경우 커스텀 이벤트 그래프에 표시되지 않습니다.

## 보고서 구성하기 {#configure-your-report}

다음 옵션을 사용하여 커스텀 이벤트 그래프에 표시되는 데이터를 맞춤 설정할 수 있습니다.

| 옵션 | 설명 |
| --- | --- |
| 앱 | 기본적으로 보고서에는 모든 앱의 데이터가 포함됩니다. 이 드롭다운을 사용하여 보고서를 특정 앱으로 좁힐 수 있습니다. |
| 커스텀 이벤트 분류 기준 | 선택한 커스텀 이벤트의 시계열 데이터가 그룹화되는 방식을 제어합니다. 기본적으로 차트는 날짜별 전체 집계 추세를 표시합니다. **Custom Events by Hour**로 전환하면 일중 패턴을 확인할 수 있고, **Custom Events per MAU**로 전환하면 이벤트 볼륨을 월간 활성 사용자(MAU) 수 대비 정규화하여 볼 수 있습니다. |
| Segments별 필터 | 이 옵션을 토글하면 이벤트 수를 하나 이상의 Segment별로 분류할 수 있습니다. 활성화하면 비교할 Segments를 선택합니다. 그래프에는 각 Segment에서 해당 커스텀 이벤트를 수행한 사용자 수가 표시됩니다. |
| KPI 공식 | 원시 이벤트 수를 분자(예: 커스텀 이벤트 수)와 분모(예: 일일 활성 사용자, MAU 또는 분석이 활성화된 Segment 크기)로 구성된 계산 지표로 대체합니다. 하나 이상의 공식을 선택하면 차트에 선택한 날짜 범위에 걸쳐 각 공식의 값이 표시되므로, 총 이벤트 볼륨 대신 정규화된 성능(예: "활성 사용자당 이벤트 수")을 비교할 수 있습니다. 선택한 시간 범위와 공식에 대해 사용 가능한 데이터가 없는 경우, Braze는 "데이터 없음" 메시지를 표시합니다. 시간 범위를 넓히거나 다른 공식을 선택하세요. **Manage KPI formulas**를 선택하여 공식을 생성하거나 편집할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="보고서 구성하기" }

## 데이터 내보내기 {#export-data}

커스텀 이벤트 데이터를 내보내려면 커스텀 이벤트 그래프에서 <i class="fas fa-bars" title="차트 컨텍스트 메뉴"></i> **차트 컨텍스트 메뉴**를 선택한 다음 내보내기 옵션을 선택합니다.

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)을 참조하세요.
{% endalert %}

## 문제 해결 {#troubleshooting}

### Segment 분석이 워크스페이스 전체 합계와 일치하지 않는 경우 {#segment-breakdown-doesnt-match-workspace-totals}

**Segments별 필터링**을 사용하거나 **앱** 드롭다운으로 보고서 범위를 좁히면, 차트는 워크스페이스 전체의 모든 커스텀 이벤트 발생 건수가 아니라 선택한 Segment(또는 앱)에서 해당 커스텀 이벤트를 수행한 사용자를 집계합니다.

Segment 라인을 필터가 적용되지 않은 보기(또는 **모든 앱**)와 비교하면 합계가 다른 경우가 많은데, 그 이유는 다음과 같습니다.

- **모든 앱**에는 워크스페이스 내 모든 앱의 사용자와 이벤트가 포함될 수 있습니다.
- 단일 앱 필터는 해당 앱에 연결된 프로필만 포함합니다.
- Segment 필터는 쿼리 시점에 Segment 정의와 일치하는 사용자를 집계하므로, Segment 기준 밖에서 이벤트를 수행한 사용자는 제외될 수 있습니다.

동일한 기준으로 비교하려면, 비교하는 각 시리즈에 동일한 앱 필터와 Segment 선택을 적용하거나, 데이터를 내보내어 분석 도구에서 수치를 대조하세요.