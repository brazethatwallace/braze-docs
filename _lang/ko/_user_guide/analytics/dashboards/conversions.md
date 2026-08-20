---
nav_title: 전환
article_title: 전환 대시보드
alias: "/conversions_dashboard_v2/"
description: "전환 대시보드를 사용하면 다양한 기여도 방법을 사용하여 Campaigns, Canvases 및 채널 전반의 전환을 분석할 수 있습니다."
page_order: 3
page_type: reference
tool:
  - Reports
---

# 전환 대시보드 {#conversions-dashboard}

> 전환 대시보드는 다양한 [기여도 방법](#attribution-methods)을 사용하여 Campaigns, Canvases 및 채널 전반의 전환을 분석합니다. 전환을 측정할 때 기간, 전환 이벤트 및 전환 기간을 지정할 수 있습니다.

## 보고서 설정하기 {#setting-up-your-report}

전환 대시보드 보고서를 설정하려면 다음을 수행합니다.

1. **Analytics** > **전환**으로 이동합니다.
2. 보고서의 **날짜 범위**를 선택합니다(최대 90일).
3. 분석할 Campaigns 또는 Canvases(또는 둘 다)를 선택합니다.
   - (선택 사항) 태그를 선택하여 Campaigns와 Canvases를 필터링합니다.
4. 메시지를 분석할 **채널**을 선택합니다.
5. **분류 기준** 레이어를 선택하여 배리언트, 캔버스 단계, 국가 또는 언어별 등 다양한 데이터 차원을 확인합니다.
6. (선택 사항) Campaign 또는 Canvas에서 전환 이벤트로 설정되지 않은 이벤트의 전환을 계산하려면 [커스텀 이벤트 사용](#using-custom-events)을 켭니다.
7. 선택한 메시지를 분석할 [기여도 방법](#attribution-methods)을 선택합니다.

{% alert note %}
여러 채널의 전환을 분석하는 경우, **기여도 방법**은 기본적으로 **라스트 터치 기여도**로 설정됩니다.
{% endalert %}

{:start="8"}
8. **생성**을 선택하여 보고서를 실행합니다.

페이지가 로드되면 **전환 이벤트**를 선택하여 전환 데이터로 보고서를 필터링합니다. 사용 가능한 선택 항목에는 Canvases와 Campaigns에서 사전 구성된 이벤트가 포함됩니다. 보고서 설정 시 커스텀 이벤트를 선택한 경우(6단계), 이 옵션은 사용할 수 없습니다.

### 커스텀 이벤트 사용하기 {#using-custom-events}

커스텀 이벤트 측정기준이 전환 대시보드에 표시되려면, 페이지에서 지정한 날짜 범위 내에 전환 이벤트와 Canvas 진입 이벤트가 있어야 합니다.

Campaign 또는 Canvas에서 전환 이벤트로 설정되지 않은 이벤트의 전환을 계산하려면, 전환 이벤트로 사용할 특정 커스텀 이벤트를 선택합니다.

1. 보고서를 설정할 때 **커스텀 이벤트 사용**을 켭니다.
2. 전환 이벤트로 사용할 커스텀 이벤트를 선택합니다.
3. 해당 이벤트가 전환으로 집계되기 위해 발생해야 하는 전환 기간을 선택합니다.

{% alert note %}
커스텀 이벤트를 선택하면 페이지에 **전환 이벤트** 드롭다운이 표시되지 않으며, 다른 커스텀 이벤트의 전환을 확인하려면 보고서를 다시 실행해야 합니다.
{% endalert %}

### 고려 사항 {#considerations}

사용자가 보고서에 집계되려면 선택한 날짜 범위 내에서 다음 기준을 충족해야 합니다.
1. Canvas 또는 Campaign에 진입합니다.
2. [기여도 방법]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods)을 기록합니다.
3. 전환 이벤트를 수행합니다.

예를 들어, 사용자가 다음과 같은 행동을 했다고 가정합니다.
1. 9월 30일에 Canvas에 진입합니다.
2. 10월 1일에 기여도 방법을 기록합니다.
3. 10월 2일에 전환 이벤트를 수행합니다.

이 사용자는 날짜 범위가 10월 1일부터 10월 7일인 보고서에 **표시되지 않습니다**. 전환 이벤트가 정의된 날짜 범위 내에 발생했더라도, 사용자가 보고 기간 이전에 Canvas에 진입했기 때문입니다. 이 사용자가 보고서에 표시되려면 날짜 범위에 9월 30일이 포함되어야 합니다.

## 보고서 이해하기 {#understanding-your-report}

보고서는 세 가지 섹션으로 나뉩니다:

- [전환 세부 정보](#conversion-details)
- [전환 퍼널](#conversion-funnel)
- [시간별 전환](#conversions-over-time)

### 전환 세부 정보 {#conversion-details}

전환 세부 정보 테이블에는 항상 *수신자*와 *전환*(전환율 및 합계)에 대한 열이 표시됩니다. 나머지 두 개의 테이블 열은 보고서를 설정할 때 선택한 옵션에 따라 달라집니다.

![세 번째와 네 번째 열의 기여도 방법으로 터치포인트가 표시된 전환 세부 정보 테이블.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

다음 테이블은 가능한 측정기준을 설명합니다.

| 표시되는 측정기준 | 설명 |
| --- | --- |
| 수신자 | 보고서의 날짜 범위 내에서 선택한 채널을 통해 메시지를 수신한 사용자 수 |
| 전환율(수신자) | 계산 방식: (전환 수) / (수신자 수) |
| 기여도 방법 | 보고서를 설정할 때 선택한 [기여도 방법](#attribution-methods)에 의해 정의됩니다. 라스트 터치 기여도를 사용하거나 여러 채널을 선택한 경우 [터치포인트](#terms-to-know)로 표시됩니다. |
| 전환율(기여도 방법) | 보고서를 설정할 때 선택한 [기여도 방법](#attribution-methods)에 의해 정의됩니다. 여러 채널을 선택한 경우 기본적으로 라스트 터치 기여도가 적용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전환 세부 정보" }

[보고서를 설정](#setting-up-your-report)할 때(5단계) Campaigns 또는 Canvases에 대한 세부 분류를 선택한 경우, <i class="fas fa-angle-down"></i> **확장**을 선택하여 테이블을 확장할 수 있습니다.

### 전환 퍼널 {#conversion-funnel}

이 막대 그래프는 선택한 채널을 기준으로 각 [인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)의 절대 수를 보여줍니다. 전환 수는 선택한 기여도 방법에 따라 정의됩니다.

기본적으로 선택한 모든 Campaigns와 Canvases가 표시됩니다. Campaign 또는 Canvas를 선택 해제하려면 제외하려는 Campaign 또는 Canvas의 이름을 선택합니다. 인게이지먼트 이벤트에 대한 추가 세부 정보를 보려면 각 막대 위에 마우스를 올리면 됩니다.

시계열 데이터를 다운로드하려면 다운로드 옵션(PNG, JPEG, PDF, SVG 또는 CSV)을 선택합니다.

{% alert note %}
이 그래프는 한 번에 하나의 채널에 대한 데이터만 표시합니다. 차트의 **채널** 드롭다운을 사용하여 단일 채널을 선택하세요.
{% endalert %}

![이메일 전달, 이메일 열람, 이메일 클릭, 전환에 대해 유사한 결과를 보여주는 두 개의 이메일 Campaigns에 대한 전환 퍼널 막대 그래프.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### 시간별 전환 {#conversions-over-time}

이 시계열 그래프는 시간에 따른 Campaign 또는 Canvas별 전환을 나타냅니다. 기본적으로 선택한 모든 Campaigns와 Canvases가 표시됩니다. Campaign 또는 Canvas를 선택 해제하려면 제외하려는 Campaign 또는 Canvas의 이름을 클릭합니다.

시계열 데이터를 다운로드하려면 <i class="fas fa-bars" title="차트 컨텍스트 메뉴"></i> **차트 컨텍스트 메뉴**를 선택한 다음 다운로드 옵션을 선택합니다. 사용 가능한 옵션은 PNG, JPEG, PDF, SVG 또는 CSV입니다.

![일별 전환을 보여주는 두 개의 이메일 Campaigns에 대한 시간별 전환 시계열 그래프.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### 기여도 방법 {#attribution-methods}

| 기여도 방법 | 정의 | 비율 계산 | 채널별 옵션 |
| --- | --- | --- | --- |
| 수신 시 | 메시지 수신 후 발생한 총 전환 수 | (고유 수신 전환 수) / (고유 수신자 수)로 계산 | {::nomarkdown}<ul><li>이메일 전달 시</li><li>SMS 전달 시</li></ul>{:/} |
| 발송 시 | 메시지 발송 후 발생한 총 전환 수 | (고유 발송 전환 수) / (고유 수신자 수)로 계산 | {::nomarkdown}<ul><li>푸시 발송 시</li><li>콘텐츠 카드 발송 시</li><li>SMS 발송 시</li></ul>{:/} |
| 열람 시 | 메시지 열람 후 발생한 총 전환 수 | (고유 열람 전환 수) / (고유 수신자 수)로 계산 | {::nomarkdown}<ul><li>이메일 열람 시</li><li>푸시 열람 시</li></ul>{:/} |
| 클릭 시 | 메시지 클릭 후 발생한 총 전환 수 | (고유 클릭 전환 수) / (고유 수신자 수)로 계산 | {::nomarkdown}<ul><li>이메일 클릭 시</li><li>콘텐츠 카드 클릭 시</li><li>인앱 메시지 클릭 시</li></ul>{:/} |
| 노출 시 | 노출 후 발생한 총 전환 수 | (고유 노출 전환 수) / (고유 수신자 수)로 계산 | {::nomarkdown}<ul><li>인앱 메시지 노출 시</li><li>콘텐츠 카드 노출 시</li></ul>{:/} |
| 라스트 터치 시 | 전환 기간 동안 마지막으로 터치하거나 클릭한 메시지에 모든 기여도를 부여하는 전환입니다. | (터치포인트 수) / (고유 수신자 수)로 계산 | 보고서에 여러 채널이 추가된 경우 라스트 터치 기여도가 자동으로 선택됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="기여도 방법" }

## 알아야 할 용어 {#terms-to-know}

| 용어 | 정의 |
| --- | --- |
| 터치 | 메시지와의 물리적 상호작용 또는 터치포인트입니다.<br><br>터치에는 다음이 포함될 수 있습니다:<br>{::nomarkdown}<ul><li>이메일 클릭</li><li>푸시 열람</li><li>콘텐츠 카드 클릭</li><li>인앱 메시지 클릭</li><li>SMS 클릭</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="알아야 할 용어" }

## 문제 해결 {#troubleshooting}

### Campaign 또는 Canvas 전환이 낮은 이유는 무엇인가요? {#why-do-i-have-low-campaign-or-canvas-conversions}

이전 Campaigns나 기대치와 비교했을 때 전환이 예상만큼 높지 않을 수 있습니다. 전환은 이벤트 추적과 전환 마감 기한이라는 두 가지 핵심 기능에 따라 달라집니다.

문제를 해결하려면 이벤트 추적과 전환 마감 기한을 확인하세요.

#### 이벤트 추적 {#event-tracking}

Campaign이 세션 시작 또는 커스텀 이벤트를 트리거하는 경우, 이 이벤트 또는 세션이 메시지를 트리거할 만큼 충분히 자주 발생하는지 확인해야 합니다. [홈 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/home)에서 세션 데이터를 확인하거나 [커스텀 이벤트]({{site.baseurl}}/user_guide/analytics/reports/configure_reporting) 보고서를 확인하세요.

#### 전환 마감 기한 {#conversion-deadlines}

Campaign별로 선택하는 각 전환 이벤트에 대해 [마감 기한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#creating-a-campaign-with-conversion-tracking)을 설정합니다. 이는 각 Campaign에 대해 전환이 집계되기 위해 발생해야 하는 시간 제한을 설정하는 것입니다.

Campaign 측정기준을 이해하려면 [전환 추적 규칙]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules)에 대한 정보를 검토하세요. Canvas에서의 사용자 전환에 대해서는 [Canvas FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs#how-are-user-conversions-tracked-in-a-canvas)를 참조하세요.

### 이메일 열람 합계가 Campaign 분석과 일치하지 않는 이유는 무엇인가요? {#why-dont-email-open-totals-match-campaign-analytics}

**Campaign 분석**과 보고서 빌더는 *고유 열람*에 [머신 열람]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens)을 포함하여 집계합니다. 자세한 내용은 이메일 FAQ의 [*고유 열람* 측정기준에 *머신 열람*이 포함되나요?]({{site.baseurl}}/user_guide/channels/email/faq#does-the-unique-opens-metric-include-machine-opens)를 참조하세요.

**전환 대시보드**에서 **이메일 열람 시** 기여도는 사람의 열람만 집계합니다. [머신 열람]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens)은 해당 기여도 방식에 사용되는 열람 수에 포함되지 않습니다.

이러한 차이로 인해 Campaign 분석의 열람 합계가 동일한 Campaigns에 대한 전환 대시보드 기여도에서 사용되는 열람 수보다 높을 수 있습니다. 동일한 화면 내에서 측정기준을 비교하거나, 머신 열람 없이 사람의 인게이지먼트만 확인하려면 Campaign 분석에서 *기타 열람*을 사용하세요.