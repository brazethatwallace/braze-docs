---
nav_title: 매출 보고서
article_title: 매출 보고서
page_order: 7
page_type: reference
description: "이 페이지에서는 매출 보고서 페이지를 사용하여 특정 기간의 매출 데이터, 특정 제품 매출, 앱의 총 매출을 확인하는 방법을 설명합니다."
tool: Reports
---

# 매출 보고서 {#revenue-report}

> **매출 보고서** 페이지에서는 특정 기간의 매출 데이터, 특정 제품 매출, 앱의 총 매출을 확인할 수 있습니다.

대시보드에서 매출 보고서를 확인하려면 **Analytics** > **Revenue Report**로 이동합니다.

## 매출 보고서 커스터마이징 {#customizing-your-revenue-report}

날짜 범위, 보고할 앱, 파라미터를 선택하여 매출 보고서를 커스터마이징할 수 있습니다.

![파라미터가 'Revenue'로 설정된 'Performance Over Time' 그래프가 표시된 'Revenue Report' 페이지.]({% image_buster /assets/img/revenue_report.png %})

### 날짜 및 앱별 필터링 {#filtering-by-date-and-apps}

매출 보고서의 날짜 범위를 선택하고, 원하는 경우 특정 앱 또는 앱 조합을 선택합니다.

### 파라미터별 필터링 {#filtering-by-parameters}

**Performance Over Time** 그래프는 다양한 파라미터에 대한 데이터를 표시하며, **Statistics for** 드롭다운에서 선택할 수 있습니다. 선택적으로 **Breakdown** 드롭다운에서 특정 파라미터의 데이터를 세분화할 수 있습니다.

**Performance Over Time** 그래프에서 다음 데이터를 확인할 수 있습니다:
- KPI or 핵심 성과 지표(KPI) 수식
- 구매
    - (선택 사항) 제품별 구매
- 매출
    - (선택 사항) Segment별 매출
    - (선택 사항) 제품별 매출
- 시간당 매출
    - (선택 사항) Segment별 시간당 매출
- 사용자당 매출

## 매출 계산 이해하기 {#understanding-revenue-calculations}

{% alert note %}
환율이 없는 통화로 매출을 기록하면, Braze는 이를 미화 $0.00 구매로 기록합니다.
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="매출 계산 이해하기">
  <caption>매출 계산 이해하기</caption>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-revenue">생애주기 매출</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-value-per-user">사용자당 LTV or 생애주기 가치</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='LTV or LTV or 생애주기 가치 Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#average-daily-revenue">일평균 매출</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-purchases">일일 구매</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-revenue-per-user">사용자당 일일 매출</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## 제품 분류 보기 {#viewing-the-product-breakdown}

**Product Breakdown** 표에서 선택한 날짜 범위 동안 구매된 제품 목록, 각 제품의 구매 수량, 각 제품이 생성한 매출을 확인할 수 있습니다.

!['Product Name', 'Purchased', 'Revenue' 열이 표시된 'Product Breakdown' 표.]({% image_buster /assets/img/revenue_report_product_breakdown.png %})

## 매출 데이터 내보내기 {#exporting-revenue-data}

매출 데이터를 내보내려면 **Performance Over Time** 그래프에서 <i class="fas fa-bars" title="차트 컨텍스트 메뉴"></i> **차트 컨텍스트 메뉴**를 선택한 다음 내보내기 옵션을 선택합니다.

{% alert tip %}
매출 데이터를 얻는 더 많은 방법을 찾고 계신가요? Campaigns 또는 Canvases에 구매 행동(및 제품 구매)을 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)로 추가해 보세요.
{% endalert %}

[Campaign 분석]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) 또는 [Canvas 분석]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics) 페이지에서 개별 사례별로 매출 통계를 확인할 수도 있습니다.

{% alert tip %}
매출 보고서는 API를 통해 내보낼 수 없습니다. CSV 내보내기에 대한 도움이 필요하면 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)을 참조하세요.
{% endalert %}