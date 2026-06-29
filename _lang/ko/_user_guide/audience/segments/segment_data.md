---
nav_title: Segment 데이터
article_title: Segment 데이터
page_order: 4
page_type: reference
description: "이 페이지에서는 Braze 대시보드의 Segments 섹션에 대해 설명하며, 제공되는 통계 요약을 포함합니다."
alias: /viewing_and_understanding_segment_data/
tool:
  - Segments
  - Reports

---
# Segment 데이터 {#segment-data}

> 이 페이지에서는 Braze 대시보드의 Segments 섹션에 대해 설명하며, 제공되는 통계 요약을 포함합니다.

## Segments 및 멤버십 데이터에 접근하기 {#accessing-data-about-your-segments-and-membership}

Braze 대시보드의 **Segments** 페이지에는 모든 Segments의 요약이 포함되어 있으며, 각 Segment에 대한 상세 데이터를 확인할 수 있습니다. 이 페이지에서 Segment 이름을 검색하고 선택하여 데이터를 편집하고 확인할 수 있습니다. Segment를 생성하는 방법을 알아보려면 [Segment 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#creating-a-segment)을 확인하세요.

![Segments 페이지]({% image_buster /assets/img_archive/segments.png %})

Segment 이름을 선택하면 Segment 통계와 필터를 확인하고, 필터를 추가하거나 삭제하여 Segment를 편집할 수 있습니다. 변경 사항을 반드시 저장하세요!

Segment에 대해 [분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)을 활성화하면, 해당 Segment의 세션, 커스텀 이벤트, 매출을 시간에 따라 확인할 수 있습니다.

![Segment의 분석 추적 토글]({% image_buster /assets/img_archive/A_Tracking_2.png %})

### Segment 통계 {#segment-statistics}

필터를 추가하거나 삭제할 때 실시간으로 업데이트되는 다음 Segment 통계를 확인할 수 있습니다:

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Segment 통계">
  <caption>Segment 통계</caption>
    <thead>
        <tr>
            <th>통계</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">총 사용자</td>
            <td class="no-split">앱의 전체 사용자 수입니다.</td>
        </tr>
        <tr>
            <td class="no-split">선택된 사용자</td>
            <td class="no-split">Segment에 포함된 사용자 수와 전체 사용자 기반에서 차지하는 비율입니다.</td>
        </tr>
        <tr>
            <td class="no-split">LTV (유료 사용자)</td>
            <td class="no-split">이 Segment의 사용자당 생애주기 가치(LTV)와 유료 사용자당 생애주기 가치입니다. LTV는 생애주기 매출을 생애주기 사용자 수로 나누어 계산합니다.</td>
        </tr>
        <tr>
            <td class="no-split">이메일 수신 가능 (옵트인)</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Emailable' %} <a href="/docs/help/best_practices/spam_regulations#spam-regulationsspam regulations">스팸 규정</a> 으로 인해 사용자에게 초기 확인 이메일의 링크를 클릭하도록 하는 더블 옵트인 정책을 구현하여 명시적으로 옵트인하도록 요청하는 것이 좋습니다. 더 많은 사용자가 옵트인하도록 유도하려면 <a href="/docs/user_guide/channels/email/subscriptions#segmenting-by-user-subscriptions">옵트인도 옵트아웃도 하지 않은 사용자</a> 를 대상으로 메시지를 보낼 수 있습니다.</td>
        </tr>
        <tr>
            <td class="no-split">푸시 활성화 (옵트인)</td>
            <td class="no-split">푸시 활성화는 하나 이상의 푸시 토큰을 가진 사용자 수를 의미합니다. 일부 사용자는 여러 개의 푸시 토큰을 가질 수 있으므로(예: iPhone과 iPad를 모두 소유한 경우), 이 Segment에 보내는 푸시 알림 수가 "푸시 활성화" 사용자 수보다 많을 수 있습니다. "옵트인"은 푸시 알림에 명시적으로 옵트인한 사용자 수를 의미합니다. 사용자에게 푸시를 보내려면 항상 명시적으로 옵트인해야 합니다.</td>
        </tr>
    </tbody>
</table>

### 세그먼트 인사이트 {#segment-insights}

대시보드의 [세그먼트 인사이트]({{site.baseurl}}/user_guide/audience/segments/segment_insights) 페이지를 방문하여 사전 선택된 KPI 세트에 대해 하나의 Segment가 다른 Segment와 비교하여 어떻게 성과를 내고 있는지 확인할 수 있습니다.

### 메시징 사용 {#messaging-use}
**메시징 사용** 섹션에서는 현재 활성화된 Campaigns와 현재 활성화된 Canvases 중 어떤 것이 해당 Segment를 타겟팅하고 있는지 확인할 수 있습니다.

### 과거 멤버십 {#historical-membership}

**과거 멤버십** 섹션에서는 Segment의 크기가 시간에 따라 어떻게 변화했는지 확인할 수 있습니다. 드롭다운을 사용하여 날짜 범위별로 Segment 멤버십을 필터링하세요.

Segment의 멤버십과 크기를 모니터링하는 방법에 대해 자세히 알아보려면 [Segment 크기 측정]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size)을 참조하세요.

### 사용자 미리보기 {#user-preview}

Segments에 대한 상세한 사용자별 정보를 확인하려면 **User Data**를 클릭하고 **User Preview**를 선택하세요.

이 페이지에서는 성별, 나이, 세션 수, 푸시 및 이메일 옵트인 여부 등 다양한 사용자별 속성을 확인할 수 있습니다.

워크스페이스 크기에 비해 Segment가 매우 작은 경우, 사용자 미리보기에서 사용자가 0명으로 표시될 수 있습니다. 이것이 반드시 Segment에 사용자가 0명이라는 의미는 아닙니다. Segment의 정확한 크기를 확인하려면 [정확한 통계 계산]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#statistics-for-segment-size)을 실행하세요.

![사용자 미리보기]({% image_buster /assets/img_archive/user_preview.png %})

## Segment별 성과 데이터 확인하기 {#viewing-performance-data-by-segment}

[쿼리 빌더 보고서 템플릿]({{site.baseurl}}/user_guide/analytics/reports/query_builder/data_by_segments)을 사용하여 Campaigns, Canvas, 배리언트 및 단계의 성과 측정기준을 Segments별로 분류할 수 있습니다.

## 쿼리 빌더를 사용하여 Segment 분류 보고서 생성하기 {#creating-a-segment-breakdown-report-using-query-builder}

[쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder) 템플릿에서 보고서를 생성하려면 **쿼리 빌더**로 이동하여 다음을 수행하세요:

1. **Create SQL Query** > **Query Template**을 선택합니다.
2. "segment breakdowns"를 포함하는 측정기준이 있는 템플릿을 필터링합니다.
3. 사용할 템플릿을 선택합니다.
4. [변수](#variables) 탭에서 SQL 템플릿의 변수를 입력합니다.
5. (선택 사항) 템플릿의 SQL을 직접 편집합니다.
6. **Run Query**를 선택합니다. 결과가 테이블에 표시됩니다.

## 변수 {#variables}

보고서를 생성하기 전에 **변수** 탭으로 이동하여 보고서 빌더 템플릿에 필요한 정보를 입력하세요. 여기에는 보고서에 따라 달라지는 필수 변수가 포함됩니다.

변수에는 다음이 포함됩니다:

- **Campaign 또는 Canvas:** 하나 또는 여러 개의 Campaigns 또는 Canvases를 포함할 수 있습니다(지정할 수 있는 Campaigns 또는 Canvases 수에 제한이 없습니다). Campaigns 또는 Canvases를 지정하지 않으면 보고서에 선택한 기간의 모든 Campaigns 또는 Canvases가 포함됩니다.
- **배리언트:** 배리언트 수준 분류를 제공하는 템플릿을 사용하는 경우, Campaign 또는 Canvas를 선택한 후 해당 Campaign 또는 Canvas 내의 배리언트를 선택할 수 있습니다. 여러 배리언트를 선택하면 결과가 배리언트별로 그룹화됩니다.
- **단계:** 캔버스 배리언트를 선택한 경우 캔버스 단계를 선택할 수 있습니다. 캔버스 배리언트를 먼저 선택하지 않으면 단계를 선택할 수 없습니다.
- **기간:** 데이터를 가져올 기간을 지정합니다. 기간을 지정하지 않으면 기본값으로 최근 30일이 적용됩니다.
- **제품명:** 구매 데이터에 대한 보고서를 실행하는 경우, 데이터를 가져올 특정 제품을 지정할 수 있습니다.
- **전환 기간:** 매출 및 구매 데이터가 포함된 보고서에 항상 필수입니다. 이메일 수신 또는 클릭 후 Braze가 구매 또는 매출을 귀속시키는 일수입니다.
- **Segments:** 데이터를 분류할 Segments를 지정합니다. 지정하지 않으면 분석 추적이 활성화된 모든 Segments에 대해 보고서가 실행됩니다.
- **태그:** **변수**에서 태그를 지정하여 특정 태그가 있는 모든 Campaigns 또는 Canvases에 대해 보고서를 실행할 수 있습니다. 여러 태그를 포함할 수 있습니다. 태그와 특정 Campaigns 또는 Canvases를 모두 보고서에 추가하면, 보고서에 태그의 데이터와 지정된 Campaigns 또는 Canvases의 데이터가 모두 포함됩니다.

## 데이터 가용성 {#data-availability}

다음 두 가지 조건이 모두 충족되는 기간에 대해 데이터를 사용할 수 있습니다:

1. 데이터를 확인하려는 Segments에 대해 [Segment 분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)이 활성화되어 있어야 합니다.
2. Segment별 성과 데이터 기능이 활성화되어 있어야 합니다.

이 기능이 회사에 활성화되기 이전 기간의 데이터에는 접근할 수 없습니다. 예를 들어, Segment A에 대한 분석 추적이 10월 1일에 활성화되고 이 기능이 회사에 10월 2일에 활성화된 경우, 10월 2일 이후에 측정기준을 기록한 Campaigns 및 Canvases에 대한 Segment A 데이터만 확인할 수 있습니다.

회사에서 이 기능을 10월 2일에 활성화하고 Segment B에 대한 분석 추적을 10월 3일에 활성화한 경우, 10월 3일 이후에 측정기준을 기록한 Campaigns 및 Canvases에 대한 Segment B 데이터만 확인할 수 있습니다.