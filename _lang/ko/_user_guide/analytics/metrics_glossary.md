---
nav_title: 측정기준 용어집
article_title: 측정기준 용어집
layout: report_metrics
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "이 용어집은 Braze 계정의 보고서에서 확인할 수 있는 용어를 정의합니다."
tool: Reports
---

<style>
  .calculation-line {
    color: #5B6B75;
    font-size: 14px;
  }
</style>

{% api %}

## AMP 클릭 수 {#amp-clicks}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

## AMP 열람 수 {#amp-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

## 오디언스 {#audience}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">계산: (배리언트 내 수신자 수) / (고유 수신자 수)</span>

{% endapi %}

{% api %}

## 반송 {#bounces}

{% apitags %}
Email, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 유효한 푸시 토큰이 없거나, Campaign 시작 후 사용자가 구독을 취소했거나, 이메일 주소가 부정확하거나 비활성화된 경우 발생할 수 있습니다.

| 채널 | 추가 정보 |
|-------|-----------------------|
| 이메일 | SendGrid를 사용하는 고객의 이메일 반송은 하드바운스, 스팸(`spam_report_drops`), 잘못된 주소로 발송된 이메일(`invalid_emails`)로 구성됩니다.<br><br>이메일의 경우, *반송 %* 또는 *반송률*은 발송 서비스에서 발송에 실패했거나 "반환됨" 또는 "수신되지 않음"으로 지정된 메시지, 또는 대상 이메일 사용자에게 수신되지 않은 메시지의 비율입니다.|
| 푸시 | 이 사용자들은 향후 모든 푸시 알림에서 자동으로 구독 취소됩니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="반송" }

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>반송</i>: 횟수</li>
        <li><i>반송 %</i> 또는 <i>반송률 %</i>: (반송) / (발송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 본문 클릭 {#body-click}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">계산: (본문 클릭 수) / (노출 횟수)</span>

{% endapi %}

{% api %}

## 본문 클릭 수 {#body-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}

<span class="calculation-line">계산: (본문 클릭 수) / (노출 횟수)</span>

{% endapi %}

{% api %}

## 버튼 1 클릭 수 {#button-1-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} _버튼 1 클릭 수_ 리포팅은 인앱 메시지에서 **Identifier for Reporting**을 "0"으로 지정한 경우에만 작동합니다.

<span class="calculation-line">계산: (버튼 1 클릭 수) / (노출 횟수)</span>

{% endapi %}

{% api %}

## 버튼 2 클릭 수 {#button-2-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} _버튼 2 클릭 수_ 리포팅은 인앱 메시지에서 **Identifier for Reporting**을 "1"로 지정한 경우에만 작동합니다.

<span class="calculation-line">계산: (버튼 2 클릭 수) / (노출 횟수)</span>

{% endapi %}

{% api %}

## Campaign 분석 {#campaign-analytics}

{% apitags %}
Feature Flags
{% endapitags %}

다양한 채널에 걸친 메시지의 성능입니다. 표시되는 측정기준은 선택한 메시징 채널과 [피처 플래그 실험]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments#campaign-analytics)이 다변량 테스트인지 여부에 따라 달라집니다.

{% endapi %}

{% api %}

## 제출된 선택 항목 {#choices-submitted}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

## 클릭 대비 열람률 {#click-to-open-rate}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">계산: (고유 클릭 수) / (고유 열람 수) (이메일의 경우)</span>

{% endapi %}

{% api %}

## RCS 확인된 전달 또는 SMS 확인된 전달 {#rcs-confirmed-deliveries-or-sms-confirmed-deliveries}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Braze 고객의 경우, 전달은 SMS 할당량에 대해 과금됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>확인된 전달</i>: 횟수</li>
        <li><i>확인된 전달률</i>: (확인된 전달) / (발송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 신뢰도 {#confidence}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

## 확인 페이지 버튼 {#confirmation-page-button}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

## 확인 페이지 닫기 {#confirmation-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

## 전환 (B, C, D) {#conversions-b-c-d}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} 이 정의된 이벤트는 Campaign을 구축할 때 사용자가 결정합니다.

| 채널 | 추가 정보 |
|-------|-----------------------|
| 이메일, 푸시, 웹훅 | 전환은 최초 발송 이후 추적됩니다.|
| Content Cards | 전환은 사용자가 Content Cards를 처음 조회할 때 집계됩니다.|
| 인앱 메시지 | 전환은 사용자가 인앱 메시지 Campaign을 수신하고 조회한 후, 메시지를 클릭했는지 여부와 관계없이 정의된 전환 기간 내에 특정 전환 이벤트를 수행하면 집계됩니다.<br><br>전환은 가장 최근에 수신한 메시지에 귀속됩니다. 재자격이 활성화된 경우, 전환은 정의된 전환 기간 내에 발생하는 한 가장 최근에 수신한 인앱 메시지에 할당됩니다. 그러나 인앱 메시지에 이미 전환이 할당된 경우, 해당 특정 메시지에 대해 새로운 전환을 기록할 수 없습니다. 즉, 각 인앱 메시지 전달은 하나의 전환에만 연결됩니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="전환 (B, C, D)" }

{% endapi %}

{% api %}

## 총 전환 수 {#total-conversions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

사용자가 인앱 메시지 Campaign을 한 번만 조회한 경우, 이후 전환 이벤트를 여러 번 수행하더라도 전환은 한 번만 집계됩니다. 그러나 재자격이 활성화되어 사용자가 인앱 메시지 Campaign을 여러 번 조회한 경우, 사용자가 인앱 메시지 Campaign의 새 인스턴스에 대해 노출을 기록할 때마다 *총 전환 수*가 증가할 수 있습니다.

예를 들어, 사용자가 인앱 메시지를 두 번 트리거하고 각 인앱 메시지 노출 후 전환한 경우(전환 2회), *총 전환 수*는 2만큼 증가합니다. 그러나 인앱 메시지 노출이 한 번만 있고 그 후 전환 이벤트가 두 번 발생한 경우, 전환은 한 번만 기록되며 *총 전환 수*는 1만큼 증가합니다.

{% endapi %}

{% api %}

## 메시지 닫기 {#close-message}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

## 전환율 {#conversion-rate}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

| 채널 | 추가 정보 |
|-------|-----------------------|
| 인앱 메시지 | 일일 총 <i>고유 노출 횟수</i> 측정기준은 인앱 메시지의 <i>전환율</i>을 계산하는 데 사용됩니다.<br><br>인앱 메시지의 <i>고유 노출 횟수</i>는 워크스페이스 시간대 기준으로 하루에 한 번만 집계될 수 있습니다. 사용자가 원하는 동작("전환")을 완료하는 횟수는 같은 날 내에 증가할 수 있습니다. 전환은 하루에 여러 번 발생할 수 있지만, <i>고유 노출 횟수</i>는 그렇지 않습니다. 따라서 사용자가 하루 내에 전환을 여러 번 완료하면 <i>전환율</i>은 그에 따라 증가할 수 있지만, <i>고유 노출 횟수</i>는 해당 날에 한 번만 집계됩니다. 자세한 내용은 <a href="/docs/user_guide/channels/in_app_messages/reporting">인앱 메시지 리포팅</a> 을 참조하세요.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="전환율" }

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>인앱 메시지</b>: (주요 전환) / (고유 노출 횟수)</li>
        <li><b>기타 채널</b>: (주요 전환) / (고유 수신자 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 전환 기간 {#conversion-window}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

## 전달 {#deliveries}

{% apitags %}
Email, Web Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

| 채널 | 추가 정보 |
|-------|-----------------------|
| 이메일 | 이메일 수신이 가능한 대상에게 성공적으로 발송되고 수신된 총 메시지 수(발송)를 의미합니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="전달" }

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>전달</i>: 횟수</li>
        <li><i>전달 %</i>: (발송 - 반송) / (발송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## RCS 전달 실패 또는 SMS 전달 실패 {#rcs-delivery-failures-or-sms-delivery-failures}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

전달 실패 원인을 파악하려면 <a href="/docs/braze_support">Braze 고객지원</a> 에 문의하세요.

<span class="calculation-line">계산: (발송) - (통신사 전송)</span>

{% endapi %}

{% api %}

## 전달 실패 {#delivery-failures}

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

전달 실패 원인을 파악하려면 <a href="/docs/braze_support">Braze 고객지원</a> 에 문의하세요.

<span class="calculation-line">계산: (발송) - (통신사 전송)</span>

{% endapi %}

{% api %}

## 전달 실패율 {#failed-delivery-rate}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

전달 실패 원인을 파악하려면 <a href="/docs/braze_support">Braze 고객지원</a> 에 문의하세요.

<span class="calculation-line">계산: (전달 실패) / (발송)</span>

{% endapi %}

{% api %}

## 직접 열람 수 {#direct-opens}

{% apitags %}
iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">계산: (직접 열람 수) / (전달)</span>

{% endapi %}

{% api %}

## 이메일 수신 가능 {#emailable}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">계산: 횟수</span>

{% endapi %}

{% api %}

## 오류 수 {#errors}

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} 오류 수는 <i>발송</i> 횟수에 포함되지만 <i>고유 수신자 수</i>에는 포함되지 않습니다.

{% endapi %}

{% api %}

## 추정 실제 열람 수 {#estimated-real-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

## 실패 {#failures}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} 실패는 <i>발송</i> 횟수에 포함되지만 <i>전달</i> 횟수에는 포함되지 않습니다.</td>

<span class="calculation-line">계산 (<i>실패율</i>): (실패) / (발송)</span>

{% endapi %}

{% api %}

## 피처 플래그 실험 성과 {#feature-flag-experiment-performance}

{% apitags %}
Feature Flags
{% endapitags %}

피처 플래그 실험에서 메시지의 성과 측정기준입니다. 표시되는 구체적인 측정기준은 메시징 채널과 실험이 다변량 테스트인지 여부에 따라 달라집니다.

{% endapi %}

{% api %}

## 하드바운스 {#hard-bounce}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

이 경우 Braze는 해당 이메일 주소를 유효하지 않은 것으로 표시하지만 사용자의 [구독 상태]({{site.baseurl}}/user_guide/channels/email/subscriptions)는 업데이트하지 않습니다. 이메일이 하드바운스를 수신하면 Braze는 해당 이메일 주소로의 향후 요청을 중단합니다.

{% endapi %}

{% api %}

## 도움말 {#help}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} 사용자 응답은 메시지를 수신한 후 4시간 이내에 인바운드 메시지를 보낼 때마다 측정됩니다.

{% endapi %}

{% api %}

## 영향받은 열람 수 {#influenced-opens}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">계산: (영향받은 열람 수) / (전달)</span>

{% endapi %}

{% api %}

## 생애주기 매출 {#lifetime-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

## 사용자당 생애주기 가치 {#lifetime-value-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

## 일평균 매출 {#average-daily-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

## 일일 구매 수 {#daily-purchases}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

## 사용자당 일일 매출 {#daily-revenue-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

## 머신 열람 수 {#machine-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} 이 측정기준은 SendGrid의 경우 2021년 11월 11일부터, SparkPost의 경우 2021년 12월 2일부터 추적됩니다. Amazon SES의 경우, 분석은 _열람 수_로 표시됩니다. 그러나 클릭에 대한 봇 필터링은 지원됩니다.

{% endapi %}

{% api %}

## 열람 수 {#opens}

{% apitags %}
Web Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

## 수신 거부 {#opt-out}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} 사용자 응답은 메시지를 수신한 후 4시간 이내에 인바운드 메시지를 보낼 때마다 측정됩니다.

{% endapi %}

{% api %}

## 기타 열람 수 {#other-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} 사용자는 머신 열람 수가 기록되기 전에 이메일을 열 수도 있습니다(이 경우 열람 횟수는 기타 열람 수에 포함됩니다). Apple Mail이 아닌 받은편지함에서 머신 열람 이벤트 이후 사용자가 이메일을 한 번(또는 그 이상) 열면, 사용자가 이메일을 연 횟수는 기타 열람 수에 포함되고 고유 열람 수에는 한 번만 포함됩니다.

{% endapi %}

{% api %}

## 재시도 대기 중 {#pending-retry}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

## 주요 전환 (A) 또는 주요 전환 이벤트 {#primary-conversions-a-or-primary-conversion-event}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}

| 채널 | 추가 정보 |
|-------|-----------------------|
| 이메일, 푸시, 웹훅 | 최초 발송 이후.|
| Content Cards, 인앱 메시지 | 사용자가 Content Cards 또는 메시지를 처음 조회할 때.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="주요 전환 (A) 또는 주요 전환 이벤트" }

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>주요 전환 (A) 또는 주요 전환 이벤트</i>: 횟수</li>
        <li><i>주요 전환 (A) %</i> 또는 <i>주요 전환 이벤트율</i>: (주요 전환) / (고유 수신자 수)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 읽음 {#reads}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

## 읽음률 {#read-rate}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">계산: (읽음 확인이 있는 읽음 수) / (발송)</span>

{% endapi %}

{% api %}

## 수신 {#received}

{% apitags %}
Email, Content Cards, In-App Message, Web Push, iOS Push, Android Push, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %}

| 채널 | 추가 정보 |
|-------|-------|
| Content Cards | 사용자가 앱에서 카드를 조회할 때 수신됩니다.|
| 푸시 | Braze 서버에서 푸시 제공업체로 메시지가 전송될 때 수신됩니다.|
| 이메일 | Braze 서버에서 이메일 서비스 제공업체로 메시지가 전송될 때 수신됩니다.|
| SMS/MMS | SMS 제공업체가 상위 통신사 및 대상 기기로부터 확인을 받은 후 "전달됨"으로 처리됩니다.|
| 인앱 메시지 | 정의된 트리거 동작에 따라 표시 시점에 수신됩니다.|
| WhatsApp | 정의된 트리거 동작에 따라 표시 시점에 수신됩니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="수신" }

{% endapi %}

{% api %}

## RCS 거부 또는 SMS 거부 {#rcs-rejections-or-sms-rejections}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} Braze 고객의 경우, 거부는 SMS 할당량에 대해 과금됩니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>거부</i>: 횟수</li>
        <li><i>거부율</i>: (거부) / (발송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 매출 {#revenue}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

## 발송됨 {#sent}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">계산: 횟수</span>

{% endapi %}

{% api %}

## 발송 {#sends}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} 이 측정기준은 Braze에서 제공합니다. 예약된 Campaign을 시작하면 이 측정기준에는 사용량 제한으로 인해 아직 발송되지 않은 메시지를 포함하여 발송된 모든 메시지가 포함됩니다.

{% alert tip %}
Content Cards의 경우, 이 측정기준은 [카드 생성]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation)에서 선택한 항목에 따라 다르게 계산됩니다.

- **시작 또는 단계 진입 시:** 생성되어 조회 가능한 카드 수입니다. 사용자가 카드를 조회했는지 여부는 포함되지 않습니다.
- **첫 노출 시:** 사용자에게 표시된 카드 수입니다.
{% endalert %}

<span class="calculation-line">계산: 횟수</span>

{% endapi %}

{% api %}

## 발송된 메시지 {#messages-sent}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} 이 측정기준은 Braze에서 제공합니다. 예약된 Campaign을 시작하면 이 측정기준에는 사용량 제한으로 인해 아직 발송되지 않은 메시지를 포함하여 발송된 모든 메시지가 포함됩니다.

{% alert tip %}
Content Cards의 경우, 이 측정기준은 [카드 생성]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation)에서 선택한 항목에 따라 다르게 계산됩니다.

- **시작 또는 단계 진입 시:** 생성되어 조회 가능한 카드 수입니다. 사용자가 카드를 조회했는지 여부는 포함되지 않습니다.
- **첫 노출 시:** 사용자에게 표시된 카드 수입니다.
{% endalert %}

<span class="calculation-line">계산: 횟수</span>

{% endapi %}

{% api %}

## 통신사 전송 {#sends-to-carrier}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>통신사 전송</i>: 횟수</li>
        <li><i>통신사 전송률</i>: (통신사 전송) / (발송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 소프트바운스 {#soft-bounce}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 이메일이 소프트바운스를 수신하면 일반적으로 72시간 이내에 재시도하지만, 재시도 횟수는 수신자에 따라 다릅니다.

_소프트바운스_는 _지연_과 다릅니다. 이 재시도 기간 동안 이메일이 성공적으로 전달되지 않으면, Braze는 시도된 Campaign 발송당 하나의 소프트바운스 이벤트를 전송합니다. 2025년 2월 25일 이전에는 이러한 재시도가 하나의 Campaign 발송에 대해 여러 소프트바운스로 집계되었습니다.

소프트바운스는 Campaign 분석에서 추적되지 않지만, [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에서 모니터링할 수 있습니다. 또한 이러한 사용자를 발송에서 제외하거나 [소프트바운스 Segment 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced)를 사용하여 최근 30일간의 소프트바운스 수를 확인할 수 있습니다. 메시지 활동 로그에서 소프트바운스의 원인을 확인하고 이메일 Campaign의 "발송"과 "전달" 간의 차이를 파악할 수도 있습니다.

{% endapi %}

{% api %}

## 스팸 {#spam}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
스팸 신고는 이메일 서비스 제공업체에서 직접 처리한 후 피드백 루프를 통해 Braze에 전달됩니다. 대부분의 피드백 루프는 실제 신고의 일부만 보고하므로, _스팸_ 측정기준은 실제 총 수의 일부를 나타내는 경우가 많습니다. 이메일 서비스 제공업체만이 스팸 신고의 실제 규모를 확인할 수 있으므로, _스팸_은 포괄적인 측정기준이 아닌 참고용 측정기준으로 봐야 합니다.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>스팸</i>: 횟수</li>
        <li><i>스팸 %</i> 또는 <i>스팸률 %</i>: (스팸으로 표시됨) / (발송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 설문조사 페이지 닫기 {#survey-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

## 설문조사 제출 {#survey-submissions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

## 총 클릭 수 {#total-clicks}

{% apitags %}
Email, Content Cards, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

| 채널 | 추가 정보 |
|-------|-------|
| LINE | 하루 최소 20개 메시지 임계값에 도달한 후 추적됩니다. AMP 이메일에는 HTML 및 일반 텍스트 버전 모두에서 기록된 클릭이 포함됩니다. 이 수치는 스팸 방지 도구에 의해 인위적으로 부풀려질 수 있습니다.|
| 배너 | 동일한 사용자가 여러 번 클릭했는지 여부와 관계없이, 전달된 메시지 내에서 클릭한 총 사용자 수(및 비율)입니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="총 클릭 수" }

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>이메일:</b> (총 클릭 수) / (전달)</li>
        <li><b>Content Cards:</b> (총 클릭 수) / (총 노출 횟수)</li>
        <li><b>SMS:</b> (클릭 열람) / (전달)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 총 닫기 수 {#total-dismissals}

{% apitags %}
Content Cards, Banners
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Content Cards의 경우, 사용자가 동일한 Campaign에서 두 개의 다른 카드를 수신하고 둘 다 닫으면, 이 횟수는 2만큼 증가합니다. 재자격을 사용하면 사용자가 카드를 수신할 때마다 _총 닫기 수_를 한 번씩 증가시킬 수 있으며, 각 카드는 별도의 메시지입니다. 배너의 경우, 닫기 동작이 활성화되어 있을 때 각 닫기를 집계합니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>총 닫기 수:</i> 횟수</li>
        <li><i>총 닫기율:</i> 총 닫기 수 / 총 노출 횟수</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 총 노출 횟수 {#total-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} 이 수치는 Braze가 SDK로부터 수신한 노출 이벤트 수의 합계입니다.

| 채널 | 추가 정보 |
|-------|-----------------------|
| Content Cards | 특정 Content Cards에 대해 기록된 총 노출 횟수입니다. 동일한 사용자에 대해 여러 번 증가할 수 있습니다.|
| 인앱 메시지 | 여러 기기가 있고 재자격이 꺼져 있는 경우, 사용자는 인앱 메시지를 한 번만 볼 수 있습니다. 사용자가 여러 기기를 사용하더라도 타겟팅된 첫 번째 기기에서만 볼 수 있습니다. 이는 프로필에 통합된 기기가 있고 사용자가 여러 기기에서 하나의 사용자 ID로 로그인한 것을 전제로 합니다. 재자격이 켜져 있으면 사용자가 인앱 메시지를 볼 때마다 노출이 기록됩니다. 자세한 내용은 <a href="/docs/user_guide/channels/in_app_messages/reporting">인앱 메시지 리포팅</a> 을 참조하세요.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="총 노출 횟수" }

<span class="calculation-line">계산: 횟수</span>

{% endapi %}

{% api %}

## 총 열람 수 {#total-opens}

{% apitags %}
Email, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

| 채널 | 추가 정보 |
|-------|-----------------------|
| LINE | 하루 최소 20개 메시지 임계값에 도달한 후 추적됩니다.|
| AMP 이메일 | HTML 및 일반 텍스트 버전의 총 열람 수입니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="총 열람 수" }

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b>이메일 <i>총 열람 수</i>:</b> 횟수</li>
        <li><b>이메일 <i>총 열람률</i>:</b> (열람 수) / (전달)</li>
        <li><b>웹 푸시 <i>총 열람 수</i>:</b> <i>직접 열람 수</i> 횟수</li>
        <li><b>웹 푸시 <i>총 열람률</i>:</b> (총 열람 수) / (전달)</li>
        <li><b>iOS, Android 및 Kindle 푸시 <i>총 열람 수</i>:</b> (직접 열람 수) + (영향받은 열람 수)</li>
        <li><b>iOS, Android 및 Kindle 푸시 <i>총 열람률</i>:</b> (총 열람 수) / (전달)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 총 매출 {#total-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} 이 측정기준은 <a href='/docs/user_guide/analytics/reports/report_builder'>보고서 빌더</a> 를 통한 Campaign 비교 보고서에서만 사용할 수 있습니다.

{% endapi %}

{% api %}

## 고유 클릭 수 {#unique-clicks}

{% apitags %}
Email, Content Cards, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

여기에는 Braze에서 제공하는 구독 취소 링크 클릭이 포함됩니다.

| 채널 | 추가 정보 |
|-------|-----------------------|
| 이메일 | 7일 동안 추적됩니다.|
| LINE | 하루 최소 20개 메시지 임계값에 도달한 후 추적됩니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="고유 클릭 수" }

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>고유 클릭 수</i>: 횟수</li>
        <li><b>Content Cards</b> <i>고유 클릭 %</i> 또는 <i>고유 클릭률</i>: (고유 클릭 수) / (고유 노출 횟수)</li>
        <li><b>이메일</b> <i>고유 클릭 %</i> 또는 <i>고유 클릭률</i>: (고유 클릭 수) / (전달)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 고유 닫기 수 {#unique-dismissals}

{% apitags %}
Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">계산: (고유 닫기 수) / (고유 노출 횟수)</span>

{% endapi %}

{% api %}

## 일일 고유 노출 횟수 {#unique-daily-impressions}

{% apitags %}
Content Cards, Banners
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %}

이 수치는 Braze에서 수신되며 `user_id`를 기반으로 합니다. 일일 고유 노출 횟수는 Campaign 또는 캔버스 단계 수준에서 집계됩니다.

<span class="calculation-line">계산: 횟수</span>

{% endapi %}

{% api %}

## 고유 노출 횟수 {#unique-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}

| 채널 | 추가 정보 |
|-------|-----------------------|
| 인앱 메시지 | 재자격이 켜져 있고 사용자가 트리거 동작을 수행하면, 워크스페이스 시간대 기준으로 새로운 날에 고유 노출 횟수가 다시 증가할 수 있습니다. 재자격이 켜져 있으면 <i>고유 노출 횟수</i> = <i>고유 수신자 수</i>입니다. 자세한 내용은 <a href="/docs/user_guide/channels/in_app_messages/reporting">인앱 메시지 리포팅</a> 을 참조하세요.|
| Content Cards | 사용자가 카드를 두 번째로 조회할 때는 횟수가 증가하지 않습니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="고유 노출 횟수" }

<span class="calculation-line">계산: 횟수</span>

{% endapi %}

{% api %}

## 고유 열람 수 {#unique-opens}

{% apitags %}
Email, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} 특정 기간을 평가할 때, <i>고유 열람 수</i>가 같은 기간의 <i>발송</i>보다 높게 나타날 수 있습니다. 이는 사용자가 해당 기간 외에 발송된 메시지에 대해 여전히 열람 이벤트를 기록할 수 있기 때문입니다. 전체 Campaign 기간 동안 <i>고유 열람 수</i>는 항상 총 <i>발송</i>보다 낮습니다.

| 채널 | 추가 정보 |
|-------|-----------------------|
| 이메일 | 7일 동안 추적됩니다.|
| LINE | 하루 최소 20개 메시지 임계값에 도달한 후 추적됩니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="고유 열람 수" }

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>고유 열람 수</i>: 횟수</li>
        <li><i>고유 열람 %</i> 또는 <i>고유 열람률</i>: (고유 열람 수) / (전달)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 고유 수신자 수 {#unique-recipients}

{% apitags %}
Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

조회자는 매일 고유 수신자가 될 수 있으므로, 이 수치는 <i>고유 노출 횟수</i>보다 높을 수 있습니다. 이 수치는 Braze에서 수신되며 `user_id`를 기반으로 합니다. 고유 수신자 수는 <a href='{{ site.homeurl }}{{ site.baseurl }}/api/identifier_types/#send-identifier'>발송 식별자</a> 수준이 아닌 Campaign 또는 캔버스 단계 수준에서 집계됩니다.

반송된 사용자도 Braze가 해당 발송일에 수신자로 집계하므로 <i>고유 수신자 수</i>에 포함됩니다. <i>고유 수신자 수</i>는 성공적인 전달만이 아니라 Braze가 해당 날짜에 메시지를 타겟팅한 사용자를 기반으로 합니다.

<span class="calculation-line">계산: 횟수</span>

{% endapi %}

{% api %}

## 구독 취소자 또는 구독 취소 {#unsubscribers-or-unsub}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><i>구독 취소자</i> 또는 <i>구독 취소</i>: 횟수</li>
        <li><i>구독 취소자 %</i> 또는 <i>구독 취소율</i>: (구독 취소) / (전달)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## 구독 취소 수 {#unsubscribes}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">계산: (구독 취소 수) / (전달)</span>

{% endapi %}

{% api %}

## 배리언트 {#variation}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">계산: 횟수</span>

{% endapi %}