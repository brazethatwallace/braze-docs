---
nav_title: 업종 벤치마크 대시보드
article_title: 업종 벤치마크 대시보드
alias: "/industry_benchmarks_dashboard/"
page_order: 3
description: "이 문서에서는 업종 벤치마크 대시보드에 대한 개요를 제공합니다."
---

# 업종 벤치마크 대시보드 {#industry-benchmarks-dashboard}

> **업종 벤치마크** 대시보드는 워크스페이스의 인게이지먼트 성능을 각 업종의 동종 기업에서 집계된 개인정보 보호 기반 벤치마크와 비교합니다.

**업종 벤치마크** 대시보드를 사용하여 이메일, 푸시, Content Cards, SMS 성능을 업종 내 동종 기업과 비교하고, 최적화 기회가 있는 채널과 지역을 파악할 수 있습니다.

**업종 벤치마크** 대시보드를 보려면 **Analytics** > **대시보드 빌더**로 이동한 다음 **Industry Benchmarks**를 선택합니다. 대시보드에 데이터가 없는 경우 **Run Dashboard**를 선택하여 최신 결과를 생성합니다. 대시보드 상단의 필터를 사용하여 업종 분류 또는 기간별로 결과를 세분화할 수 있습니다.

## 대시보드 정보 {#about-the-dashboard}

대시보드는 **이메일**, **푸시 알림**, **Content Cards**, **SMS** 네 가지 채널 섹션으로 구성되어 있습니다.

| 섹션              | 설명                                                                                                                                             |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| KPI 카드            | 각 핵심 측정기준에 대한 워크스페이스의 비율과 업계 비율 대비 변화량을 보여줍니다. 녹색 위쪽 화살표는 워크스페이스가 업계 비율보다 높음을, 빨간색 아래쪽 화살표는 낮음을 나타냅니다. |
| 월별 추세 차트  | 시간 경과에 따른 워크스페이스 비율과 업계 비율을 비교하여 계절성 및 장기적 추세를 파악할 수 있습니다.                                   |
| 지역별 분석   | 지역별로 워크스페이스 비율과 업계 비율을 비교하여 지역 성능이 업계와 어디서 차이가 나는지 확인할 수 있습니다.         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="섹션" }

모든 차트에서 밝은 색상의 계열은 업계 벤치마크를 나타내고, 어두운 색상의 계열(**Workspace** 접두사 포함)은 자체 성능을 나타냅니다.

## 사용 가능한 측정기준 {#available-metrics}

각 채널 기반 측정기준은 두 가지 유형으로 제공됩니다.

| 측정기준 유형     | 설명                           | 예시                                              |
|----------|---------------------------------------|------------------------------------------------------|
| *합계*  | 모든 인게이지먼트 이벤트를 집계합니다.        | 사용자가 세 번 클릭하면 세 번의 클릭으로 집계됩니다. |
| *고유* | 고유 사용자를 집계합니다.                  | 사용자가 세 번 클릭하면 한 번의 클릭으로 집계됩니다.   |
{: .reset-td-br-1 .reset-td-br-2 aria-label="측정기준 유형" }

측정기준은 다음과 같은 산업, 지역, 하위 산업, 날짜의 조합으로 그룹화됩니다.

- 산업 + 날짜
- 산업 + 지역 + 날짜
- 산업 + 하위 산업 + 지역 + 날짜

각 채널의 측정기준을 보려면 탭을 선택하세요.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

{% tabs %}
{% tab 이메일 %}

<table aria-label="이메일 측정기준"><thead><tr><th>측정기준</th><th>설명</th><th>공식</th></tr></thead><tbody>
<tr><td class="no-split"><i>고유 열람율</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} 이 비율에는 기계 열람이 제외됩니다.</td><td class="no-split"><i>Unique Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>고유 클릭률</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>고유 클릭 대비 열람율</i></td><td class="no-split">이메일을 열람한 후 클릭한 사용자의 비율입니다.</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Opens</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="이메일 측정기준" }

![이메일 산업 벤치마크 측정기준이 꺾은선 그래프와 막대 그래프로 표시됩니다.]({% image_buster /assets/img/dashboards/email_industry.png %})

{% endtab %}
{% tab 푸시 %}

푸시 측정기준은 iOS, Android, 웹 및 모든 플랫폼 통합에 대해 사용할 수 있습니다.

<table aria-label="푸시 측정기준"><thead><tr><th>측정기준</th><th>설명</th><th>공식</th></tr></thead><tbody>
<tr><td class="no-split"><i>직접 열람율</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td><td class="no-split"><i>Direct Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>영향 열람율</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}</td><td class="no-split"><i>Influenced Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>총 열람율</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td><td class="no-split">(<i>Direct Opens</i> + <i>Influenced Opens</i>) / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="푸시 측정기준" }

![푸시 산업 벤치마크 측정기준이 꺾은선 그래프와 막대 그래프로 표시됩니다.]({% image_buster /assets/img/dashboards/push_industry.png %})

{% endtab %}
{% tab SMS %}

<table aria-label="SMS 측정기준"><thead><tr><th>측정기준</th><th>설명</th><th>공식</th></tr></thead><tbody>
<tr><td class="no-split"><i>전달율</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td><td class="no-split"><i>Deliveries</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>단축 링크 클릭률</i></td><td class="no-split">SMS를 수신한 후 단축 링크를 클릭한 사용자의 비율입니다.</td><td class="no-split"><i>Short Link Clicks</i> / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS 측정기준" }

![SMS 산업 벤치마크 측정기준이 꺾은선 그래프와 막대 그래프로 표시됩니다.]({% image_buster /assets/img/dashboards/sms_industry.png %})

{% endtab %}
{% tab Content Cards %}

<table aria-label="Content Cards 측정기준"><thead><tr><th>측정기준</th><th>설명</th><th>공식</th></tr></thead><tbody>
<tr><td class="no-split"><i>클릭률</i></td><td class="no-split">Content Cards를 수신한 후 링크를 클릭한 사용자의 비율입니다.</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Impressions</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content Cards 측정기준" }

![Content Cards 산업 벤치마크 측정기준이 꺾은선 그래프와 막대 그래프로 표시됩니다.]({% image_buster /assets/img/dashboards/content_card_industry.png %})

{% endtab %}
{% endtabs %}

## 방법론 {#methodology}

Braze 벤치마크는 안정적이고 표현 기반의 수치를 산출하기 위해 설계된 3단계 프로세스를 통해 계산됩니다.

### 1단계: 동적 샘플링 {#step-1-dynamic-sampling}

모든 데이터 포인트를 분석하는 대신, Braze는 표현 기반 샘플을 선택합니다. 이 샘플링 방법은 소규모 사용자 그룹을 과대 표집하여 적절한 대표성을 확보하고, 기업 규모에 따라 조정하여 소수의 대규모 기업이 전체 산업의 결과를 왜곡하지 않도록 합니다.

### 2단계: 이상값 제거 {#step-2-outlier-removal}

Braze는 통계적 이상값을 식별하고 제거합니다. 이를 통해 평균 성능 비율에 미치는 영향을 최소화하면서 데이터의 변동성을 크게 줄일 수 있으며, 기저 추세를 변경하지 않으면서 이상 항목을 제거합니다.

### 3단계: 사후 층화 가중치 적용 {#step-3-post-stratification-weighting}

샘플은 실제 모집단을 반영하도록 가중치가 적용됩니다. 샘플링 과정에서 남은 불균형을 보정하기 위해 하위 그룹에 가중치를 적용하여, 최종 벤치마크가 대표성 있고 편향되지 않도록 합니다.

## 데이터 거버넌스 {#data-governance}

- **갱신 주기:** 데이터는 매월 5일에 갱신되며, 직전 완료된 월까지의 데이터가 반영됩니다.
- **개인정보 보호:** 모든 벤치마크는 사용자 정보를 보호하기 위해 집계 및 비식별화 처리됩니다.