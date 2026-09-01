---
nav_title: 대시보드 빌더
article_title: 대시보드 빌더
alias: "/dashboard_builder/"
description: "이 참조 문서에서는 대시보드 빌더를 사용하여 보고서 빌더 또는 쿼리 빌더에서 생성한 보고서를 활용해 대시보드와 시각화를 만드는 방법을 다룹니다."
page_type: reference
tool:
    - Reports
page_order: 6
---

# 대시보드 빌더 {#dashboard-builder}

> 대시보드 빌더를 사용하여 보고서 빌더 또는 쿼리 빌더에서 생성한 보고서를 활용해 대시보드와 시각화를 만들 수 있습니다.

대시보드 빌더를 사용하면 처음부터 또는 Braze에서 제공하는 대시보드를 기반으로 커스텀 분석 대시보드를 작성하고 시각화할 수 있습니다. 코드 없는 데이터 소스(보고서 빌더) 또는 SQL 데이터 소스(쿼리 빌더)를 사용하여 대시보드를 구동하거나, Braze에서 제공하는 다양한 대시보드 중 하나에서 시작할 수 있습니다.

## 커스텀 대시보드 만들기 {#creating-a-custom-dashboard}

1. **Analytics** > **대시보드 빌더**로 이동합니다.
2. **Create Dashboard**를 선택합니다.
3. 보고서를 구동할 데이터 소스를 선택합니다:
- 보고서 빌더에서 작성한 **Reports**
- 쿼리 빌더에서 생성한 **Custom Queries**<br><br>![대시보드의 데이터 소스를 선택하는 창.]({% image_buster /assets/img/select_data_source.png %})<br><br>

이제 데이터 소스에 따라 해당 단계를 따릅니다:

{% tabs %}
{% tab Reports %}

{: start="4"}
4. **+ Add Tile**을 선택한 다음, [보고서 빌더(신규)]({{site.baseurl}}/user_guide/analytics/reports/report_builder)에서 작성한 보고서 중 하나를 선택합니다.

{% alert important %}
보고서 빌더 보고서가 대시보드 빌더 타일에 추가된 후에는 해당 타일이 원본 보고서와 연결되지 않습니다. 보고서 빌더에서 원본 보고서를 수정하는 경우, 기존 대시보드 타일을 삭제하고 업데이트된 보고서를 데이터 소스로 사용하여 새 타일을 만들어야 합니다.
{% endalert %}

{: start="5"}
5. 연필 아이콘을 선택하여 타일에 표시되는 제목과 차트 유형을 변경합니다.
    - 차트 유형 컨트롤에서 다양한 차트 유형 간에 전환할 수 있습니다. 현재 옵션에는 막대 차트(가로 또는 세로)와 꺾은선 차트(보고서 빌더 설정에서 **Date**를 드릴다운 옵션으로 선택한 경우에만 사용 가능)가 있습니다.<br><br>![다양한 차트 유형 토글.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    - 측정기준 드롭다운을 사용하여 시각화에 포함할 측정기준을 선택합니다. 기본적으로 보고서의 첫 번째 열이 기본 표시 측정기준이 됩니다.
6. 원하는 대로 시각화를 변경한 후 **Save**를 선택합니다.
7. 나중에 대시보드를 쉽게 찾을 수 있도록 이름, 설명, 태그를 추가합니다.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4. **+ Add Tile**을 선택한 다음, 쿼리 빌더에서 실행한 쿼리를 선택합니다.
5. 타일에 쿼리 결과가 표시되는 방식을 편집하려면, 연필 아이콘을 선택하여 제목과 차트 유형을 변경합니다.
    - 차트 유형 컨트롤에서 다양한 차트 유형 간에 전환할 수 있습니다. 현재 옵션에는 테이블, 막대 차트(가로 또는 세로), 꺾은선 차트가 있습니다.<br><br>![다양한 차트 유형 토글.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        - 차트 옵션 중 하나를 선택한 경우, **X-axis** 드롭다운을 사용하여 쿼리 결과에서 X축으로 사용할 열을 하나 선택합니다.
        - **Y-axis** 드롭다운을 사용하여 시각화에 포함할 측정기준을 선택합니다. 기본적으로 쿼리 결과의 모든 열이 표시되므로, 보고 싶지 않은 열의 선택을 해제합니다.<br><br>![다양한 차트 유형 토글.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        - (선택 사항) **Grouping** 드롭다운을 사용하여 쿼리 결과를 그룹화할 수 있습니다. 예를 들어, Campaign ID가 열 결과에 포함되어 있고 해당 값을 가진 모든 행을 합산하려면 **Grouping** 드롭다운을 사용합니다.
        - (선택 사항) 표시되는 데이터를 편집하려면, 시각화에 연결된 쿼리를 선택하고 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder)에서 수정합니다.
6. 원하는 대로 시각화를 변경한 후 **Save**를 선택합니다.
7. 나중에 대시보드를 쉽게 찾을 수 있도록 이름, 설명, 태그를 추가합니다.
{% endtab %}
{% endtabs %}

{: start="8"}
8. 원하는 대시보드가 완성될 때까지 해당 방식에 맞게 4~7단계를 반복합니다.
9. **View Dashboard** > **Run Dashboard**를 선택합니다.

보고서 생성이 완료되기까지 몇 분이 소요될 수 있습니다.

{% alert note %}
대시보드에는 최대 10개의 타일을 추가할 수 있습니다.
{% endalert %}

## 대시보드 타일 관리 {#managing-dashboard-tiles}

### 타일 삭제 {#delete-tiles}

타일 하단의 **Delete Tile**을 선택하여 대시보드 타일을 삭제할 수 있습니다. **이 작업은 되돌릴 수 없습니다.**

### 타일 복제 {#duplicate-tiles}

타일 하단의 **Duplicate Tile**을 선택하여 타일의 사본을 만들 수 있습니다.

### 타일 크기 및 위치 조정 {#adjust-tile-size-and-position}

크기 조정 핸들을 드래그하여 타일 크기를 조정하고, 타일 핸들을 드래그하여 대시보드에서 타일 위치를 조정할 수 있습니다.

## 대시보드 실행하기 {#running-a-dashboard}

1. **Analytics** > **대시보드 빌더**로 이동합니다. 홈 페이지에는 워크스페이스 내의 모든 기존 대시보드가 나열되며, Braze가 만든 대시보드가 상단에 표시됩니다. 이러한 대시보드는 제목에 "(Braze)"로 표시됩니다.
2. 관심 있는 대시보드를 선택합니다.
3. **Run Dashboard**를 선택하여 해당 대시보드를 로드합니다.

### 사용 가능한 대시보드 {#available-dashboards}

Braze는 자주 사용되는 사용 사례를 위한 사전 빌드 대시보드를 제공합니다. 다음 표를 현재 문서화된 대시보드와 각 대시보드에 접근하는 방법에 대한 단일 참고 자료로 활용하세요.

| 대시보드 | 접근 경로 | 설명서 |
| --- | --- | --- |
| Revenue - Last Touch Attribution | **Analytics** > **대시보드 빌더** | [Revenue - Last Touch Attribution](#revenue---last-touch-attribution) |
| Devices and carriers | **Analytics** > **대시보드 빌더** | [Devices and carriers](#devices-and-carriers) |
| Segment Insights - Email | **Analytics** > **대시보드 빌더** | [Segment Insights - Email](#segment-insights---email) |
| Session Analytics | **Analytics** > **대시보드 빌더** | [Session Analytics](#session-analytics) |
| eCommerce Revenue - Last Touch Attribution | **Analytics** > **대시보드 빌더** | [eCommerce 매출 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/ecommerce_revenue_dashboard) |
| Messaging Diagnostics | **Analytics** > **대시보드 빌더** | [메시징 진단 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) |
| Industry Benchmarks | **Analytics** > **대시보드 빌더** | [업종 벤치마크 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/industry_benchmarks_dashboard) |
| Email performance | **Analytics** > **Email Performance** | [채널 성능 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#email-performance-dashboard) |
| SMS performance | **Analytics** > **SMS Performance** | [채널 성능 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#sms-performance-dashboard) |
| Push performance | **Analytics** > **대시보드 빌더** > **Push Channel Dashboard** | [채널 성능 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#push-performance-dashboard) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사용 가능한 대시보드" }

{% alert note %}
Braze가 만든 대시보드를 편집하는 기능은 아직 제공되지 않습니다. 추가 대시보드를 요청하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

#### Revenue - Last Touch Attribution {#revenue---last-touch-attribution}

**Revenue - Last Touch Attribution** 대시보드는 Campaigns, Canvases 및 채널 전반의 매출을 검토합니다. 모든 매출 데이터는 기여도 기간 내에 마지막으로 접촉한 메시지에 기여됩니다.

접촉에는 *이메일 클릭*(링크 클릭), *콘텐츠 카드 클릭*, *인앱 메시지 클릭*(닫기 버튼 제외), *푸시 열람*, *SMS 단축 링크 클릭*, *WhatsApp 읽음*, *웹훅 발송*이 포함됩니다.

| 측정기준 | 정의 |
| --- | --- |
| 총 라스트 터치 매출 | 선택한 날짜 범위 및 기여도 기간 내에 라스트 터치 이벤트가 있는 모든 Campaign 및 Canvas 매출 이벤트의 합계입니다. |
| 총 구매 전환 | 적격 라스트 터치 이벤트가 있는 모든 Campaign 및 Canvas 매출 이벤트의 수입니다. |
| 평균 전환 소요일 | 적격 라스트 터치 이벤트가 있는 모든 Campaign 및 Canvas 구매 이벤트 간의 평균 시간입니다. |
| 수신자당 매출 | 적격 매출 이벤트의 매출 합계를 날짜 범위 내에 메시지를 수신한 고유 사용자 수로 나눈 값입니다. |
| 고유 구매자 | 적격 매출 이벤트가 있는 고유 사용자 수입니다. |
| 국가별 매출 | 라스트 터치 이벤트가 있는 모든 Campaign 및 Canvas 매출 이벤트를 국가별로 그룹화한 합계입니다. |
| Campaign별 매출 | 적격 라스트 터치 이벤트가 있는 모든 Campaign 및 Canvas 매출 이벤트를 Campaign별로 그룹화한 합계입니다. |
| 캠페인 배리언트별 매출 | 적격 라스트 터치 이벤트가 있는 모든 Campaign 및 Canvas 매출 이벤트를 캠페인 배리언트별로 그룹화한 합계입니다. |
| Canvas별 매출 | 적격 라스트 터치 이벤트가 있는 모든 Campaign 및 Canvas 매출 이벤트를 Canvas별로 그룹화한 합계입니다. |
| 캔버스 배리언트별 매출 | 적격 라스트 터치 이벤트가 있는 모든 Campaign 및 Canvas 매출 이벤트를 캔버스 배리언트별로 그룹화한 합계입니다. |
| 제품별 구매 | 모든 구매를 제품별로 그룹화한 수입니다. |
| 채널별 매출 | 적격 라스트 터치 이벤트가 있는 모든 Campaign 및 Canvas 매출 이벤트를 채널별로 그룹화한 합계입니다. |
| 매출 시계열 | 적격 라스트 터치 이벤트가 있는 모든 Campaign 및 Canvas 매출 이벤트를 UTC 기준 일별로 그룹화한 합계입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Revenue - Last Touch Attribution" }

#### Devices and carriers {#devices-and-carriers}

| 측정기준 | 정의 |
| --- | --- |
| 기기 통신사 | 선택한 날짜 범위에서 푸시 알림을 열람한 사용자 수를 기기 통신사별로 그룹화한 수입니다. |
| 기기 모델 | 선택한 날짜 범위에서 푸시 알림을 열람한 사용자 수를 기기 모델별로 그룹화한 수입니다. |
| 기기 운영 체제 | 선택한 날짜 범위에서 푸시 알림을 열람한 사용자 수를 기기 운영 체제별로 그룹화한 수입니다. |
| 기기 화면 크기 | 선택한 날짜 범위에서 푸시 알림을 열람한 사용자 수를 기기 화면 해상도(크기)별로 그룹화한 수입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Devices and carriers" }

#### Segment Insights - Email {#segment-insights---email}

| 측정기준 | 정의 |
|---|---|
| 주간 이메일 측정기준(비율) | 이메일 참여율(전달율, 반송률, 열람률, 클릭률, 탈퇴율)을 Segment별로 그룹화하고 주간 시계열로 표시합니다. |
| 주간 이메일 측정기준(횟수) | 이메일 참여 횟수(발송, 전달, 반송, 열람, 클릭, 탈퇴)를 Segment별로 그룹화하고 주간 시계열로 표시합니다. |
| 주간 구매 측정기준(비율) | 이메일 열람 및 클릭에 따른 구매 전환율(수신자당 매출)을 Segment별로 그룹화하고 주간 시계열로 표시합니다. |
| 주간 구매 측정기준(횟수) | 이메일 열람 및 클릭에 따른 구매 횟수 및 매출 합계를 Segment별로 그룹화하고 주간 시계열로 표시합니다. |
| Segment별 이메일 참여 | 총 이메일 참여 측정기준(발송, 전달, 반송, 열람, 클릭, 탈퇴 및 해당 비율)을 Segment별로 집계한 요약 테이블입니다. |
| Segment별 구매 및 매출 | 이메일 열람 및 클릭에 따른 총 구매 측정기준(구매, 매출, 수신자당 매출)을 Segment별로 집계한 요약 테이블입니다. |
| 참여 측정기준 상위 10개 Campaigns | 가장 높은 이메일 참여 측정기준을 보유한 Campaigns의 순위 목록입니다(순위 측정기준 설정 가능). |
| 참여 측정기준 하위 10개 Campaigns | 가장 낮은 이메일 참여 측정기준을 보유한 Campaigns의 순위 목록입니다(순위 측정기준 설정 가능). |
| 참여 측정기준 상위 10개 Canvases | 가장 높은 이메일 참여 측정기준을 보유한 Canvases의 순위 목록입니다(순위 측정기준 설정 가능). |
| 참여 측정기준 하위 10개 Canvases | 가장 낮은 이메일 참여 측정기준을 보유한 Canvases의 순위 목록입니다(순위 측정기준 설정 가능). |
| 구매 측정기준 상위 10개 Campaigns | 이메일 참여에 따른 가장 높은 구매 전환 측정기준을 보유한 Campaigns의 순위 목록입니다(순위 측정기준 설정 가능). |
| 구매 측정기준 하위 10개 Campaigns | 이메일 참여에 따른 가장 낮은 구매 전환 측정기준을 보유한 Campaigns의 순위 목록입니다(순위 측정기준 설정 가능). |
| 구매 측정기준 상위 10개 Canvases | 이메일 참여에 따른 가장 높은 구매 전환 측정기준을 보유한 Canvases의 순위 목록입니다(순위 측정기준 설정 가능). |
| 구매 측정기준 하위 10개 Canvases | 이메일 참여에 따른 가장 낮은 구매 전환 측정기준을 보유한 Canvases의 순위 목록입니다(순위 측정기준 설정 가능). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment Insights - Email" }

#### Session Analytics {#session-analytics}

| 측정기준 | 정의 |
|---|---|
| 일별 세션 수(시계열) | 선택한 날짜 범위 내에서 일별로 그룹화한 고유 세션 수를 시계열로 표시합니다. |
| 사용자당 평균 세션 수 | 선택한 날짜 범위 내에서 총 세션 수를 고유 사용자 수로 나누어 계산한 사용자당 평균 세션 수입니다. |
| 세션으로 전환된 Campaigns | Campaign 전환과 동시에 발생한 고유 세션 수를 Campaign ID별로 그룹화하고 세션 수 기준으로 순위를 매긴 수입니다. |
| 세션으로 전환된 Canvases | Canvas 전환과 동시에 발생한 고유 세션 수를 Canvas ID별로 그룹화하고 세션 수 기준으로 순위를 매긴 수입니다. |
| 사용자당 총 세션 수 | 선택한 날짜 범위 내에서 총 세션 수 기준 상위 1,000명의 사용자 목록입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Session Analytics" }

## 피드백을 공유해 주세요 {#share-your-feedback-with-us}

{% multi_lang_include product_feedback_cta.md context="pain_point" channel="ux" feature="Dashboard Builder" %}