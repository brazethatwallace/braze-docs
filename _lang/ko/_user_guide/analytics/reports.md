---
nav_title: 보고서
article_title: 보고서
page_order: 2
layout: dev_guide
guide_top_header: "보고서"
guide_top_text: "Braze는 캠페인 성과를 측정하고, 사용자 참여를 추적하며, 데이터 중심의 의사결정을 내릴 수 있도록 다양한 보고 옵션을 제공합니다. 어디서부터 시작해야 할지 모르겠다면 <a href='#choosing-a-report'>보고서 비교 표</a> 를 확인하여 목표에 맞는 보고서를 찾아보세요."

page_type: landing
description: "캠페인 분석, 보고서 빌더, 쿼리 빌더, 참여 보고서 등 Braze 보고 옵션을 살펴보세요."
tool: Reports
search_rank: 2
guide_featured_title: "섹션 문서"
guide_featured_list:
  - name: 캠페인 분석
    link: /docs/user_guide/analytics/reports/campaign_analytics
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: 보고서 빌더
    link: /docs/user_guide/analytics/reports/report_builder
    image: /assets/img/braze_icons/tool-01.svg
  - name: 쿼리 빌더
    link: /docs/user_guide/analytics/reports/query_builder
    image: /assets/img/braze_icons/code-02.svg
  - name: 참여 보고서
    link: /docs/user_guide/analytics/reports/engagement_reports
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: 매출 보고서
    link: /docs/user_guide/analytics/reports/revenue_report
    image: /assets/img/braze_icons/piggy-bank-02.svg
  - name: 사용자 지정 이벤트 보고서
    link: /docs/user_guide/analytics/reports/custom_events_report
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "추가 문서"
guide_menu_list:
  - name: Canvas 분석
    link: /docs/user_guide/analytics/reports/canvas_analytics
    image: /assets/img/braze_icons/line-chart-down-01.svg
  - name: 퍼널 보고서
    link: /docs/user_guide/analytics/reports/funnel_reports
    image: /assets/img/braze_icons/flag-02.svg
  - name: 리텐션 보고서
    link: /docs/user_guide/analytics/reports/retention_reports
    image: /assets/img/braze_icons/user-check-01.svg
  - name: 보고 설정
    link: /docs/user_guide/analytics/reports/configure_reporting
    image: /assets/img/braze_icons/settings-01.svg
---

## 보고서 선택하기 {#choosing-a-report}

| 보고서 | 적합한 용도 | 설명 |
| --- | --- | --- |
| [캠페인 분석]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) | 채널별 Campaign 결과 | 각 Campaign의 실시간 결과를 메시징 채널별로 확인합니다. |
| [Canvas 분석]({{site.baseurl}}/user_guide/analytics/reports/canvas_analytics) | Canvas 성과 | Canvas의 주요 통계, 배리언트 성과, 단계별 측정기준을 확인합니다. |
| [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reports/report_builder) | 크로스 캠페인 비교 | 여러 Campaigns 또는 Canvases의 결과를 커스텀 측정기준 및 드릴다운과 함께 단일 뷰에서 비교합니다. |
| [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder) | 커스텀 SQL 분석 | Snowflake에서 Braze 데이터에 대해 커스텀 SQL 쿼리를 작성하거나, 일반적인 분석을 위한 사전 구축 템플릿을 사용합니다. |
| [참여 보고서]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports) | 스케줄 이메일 내보내기 | 선택한 Campaigns 및 Canvases에 대한 참여 통계를 반복적으로 CSV로 내보내도록 설정합니다. |
| [사용자 지정 이벤트 보고서]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) | 커스텀 이벤트 트렌드 | 커스텀 이벤트 빈도를 시간 경과에 따라 Segment별 또는 KPI or 핵심 성과 지표(KPI) 공식으로 정규화하여 모니터링합니다. |
| [매출 보고서]({{site.baseurl}}/user_guide/analytics/reports/revenue_report) | 매출 및 구매 | 매출, 구매, 제품 분류를 시간 경과에 따라 추적하며, 선택적으로 Segment 필터를 적용할 수 있습니다. |
| [퍼널 보고서]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports) | 전환 퍼널 분석 | 고객이 Campaign 또는 Canvas를 수신한 후 거치는 여정을 이탈 지점을 포함하여 분석합니다. |
| [리텐션 보고서]({{site.baseurl}}/user_guide/analytics/reports/retention_reports) | 장기 리텐션 영향 | Campaign 또는 Canvas가 시간 경과에 따라(최대 30일) 사용자를 얼마나 효과적으로 재참여시키는지 측정합니다. |
| [보고 설정]({{site.baseurl}}/user_guide/analytics/reports/configure_reporting) | 주간 이메일 다이제스트 | 주간 분석 이메일을 구독하고 포함할 커스텀 이벤트를 선택합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="보고서 선택하기" }