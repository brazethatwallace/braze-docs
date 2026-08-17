---
nav_title: 이메일 애널리틱스 용어집
article_title: 이메일 애널리틱스 용어집
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "이 용어집에는 시작 후 이메일 Campaign 또는 Canvas의 분석 섹션에서 찾을 수 있는 용어가 포함되어 있습니다. 이 용어집에는 Currents 측정기준이 포함되어 있지 않습니다."
channel:
  - email
---

> 이 용어집은 이메일 Campaign 및 Canvases의 **Analytics** 탭에 있는 측정기준을 정의합니다. Braze는 호스팅된 "브라우저에서 이 이메일 보기" 페이지를 제공하지 않습니다. 해결 방법은 [이메일에 "브라우저에서 이 이메일 보기" 링크를 추가할 수 있나요?]({{site.baseurl}}/user_guide/channels/email/faq#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails)를 참조하세요. 여러 측정기준에 걸친 기타 문제 해결은 [이메일 FAQ]({{site.baseurl}}/user_guide/channels/email/faq)를 참조하세요.

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### 배리언트 {#variation}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 이메일 가능 {#emailable}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 오디언스 % {#audience}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">계산: (배리언트의 수신자 수) / (고유 수신자 수)</span>

{% endapi %}

{% api %}

### 고유 수신자 {#unique-recipients}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} 이 숫자는 Braze에서 수신됩니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 발송 수 {#sends}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  이 측정기준은 Braze에서 제공합니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 발송된 메시지 {#messages-sent}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  이 측정기준은 Braze에서 제공합니다.

<span class="calculation-line">계산: 카운트</span>

{% endapi %}

{% api %}

### 전달 수 {#deliveries}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} 이메일의 경우, *전달*은 이메일 수신이 가능한 대상에게 성공적으로 발송되어 수신된 총 메시지(발송) 수입니다.

<span class="calculation-line">계산: (발송) - (반송) </span>

{% alert note %}
사용자 수준의 **수신** 상태 및 관련 로직(예: 최대 게재빈도 설정)의 경우, Braze는 일반적으로 이메일 서비스 공급자(ESP)가 받은편지함으로의 최종 전달을 확인할 때가 아니라 발송이 처리되어 전달을 위해 넘겨질 때 사용자를 표시합니다. 이렇게 하면 ESP 확인과 제품 내 규칙 사이의 타이밍 차이를 방지할 수 있습니다. ESP 또는 서드파티 전달 보고서와 다를 수 있습니다.
{% endalert %}

{% endapi %}

{% api %}

### 전달률 %

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">계산: (발송 - 반송) / (발송) </span>

{% endapi %}

{% api %}

### 반송 {#bounces}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %}

이메일의 경우, *반송률 %* 또는 *반송률*은 발송 서비스에서 발송에 실패했거나 "반환" 또는 "수신 불가"로 지정된 메시지, 또는 의도한 이메일 수신 가능 사용자에게 수신되지 않은 메시지의 비율입니다.

SendGrid를 사용하는 고객의 이메일 반송은 하드바운스, 스팸(`spam_report_drops`), 유효하지 않은 주소로 발송된 이메일(`invalid_emails`)로 구성됩니다.

{% alert note %}
[Braze 커런츠]({{site.baseurl}}/user_guide/data/distribution/braze_currents)에서 일시적인 ESP 지연은 종종 소프트바운스로 표시됩니다. 전달 가능성 도구(예: 기본 SendGrid 보고 또는 Looker 모델)는 동일한 상황에 대해 지연을 사용할 수 있습니다. 지연은 일반적으로 일시적이며, 재시도 후 메일이 전달되는 경우가 많습니다. 장기간 재시도(Campaign 분석에서 소프트바운스의 경우 약 72시간까지) 후에도 ESP에 따라 메시지가 전달 불가로 처리될 수 있습니다. Currents 이메일 이벤트는 추가 전용이므로, 기록된 소프트바운스는 메시지가 최종적으로 전달되더라도 나중에 제거되지 않습니다.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>반송</i>:</b> 카운트</li>
        <li><b><i>반송 %</i> 또는 <i>반송률 %</i>:</b> (반송) / (발송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 하드바운스 {#hard-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

이메일이 하드바운스되거나 스팸으로 표시되면, Braze는 해당 이메일 주소를 유효하지 않은 것으로 표시하지만 사용자의 [구독 상태]({{site.baseurl}}/user_guide/channels/email/subscriptions)는 업데이트하지 않습니다. Braze는 해당 이메일 주소로의 향후 발송을 중단합니다. 하드바운스 목록에서 이메일 주소를 제거하려면 [하드바운스 이메일 제거 엔드포인트]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)를 사용하세요.

<span class="calculation-line">계산: 카운트 </span>

{% endapi %}

{% api %}

### 소프트바운스 {#soft-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 이메일이 소프트바운스되면 일반적으로 72시간 이내에 재시도하지만, 재시도 횟수는 수신자에 따라 다릅니다.

소프트바운스는 Campaign 분석에서 추적되지 않지만, [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에서 소프트바운스를 모니터링하거나 [소프트바운스 Segment 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced)를 사용하여 발송에서 해당 사용자를 제외할 수 있습니다. 메시지 활동 로그에서 소프트바운스의 원인을 확인하고 이메일 Campaign의 "발송"과 "전달" 간의 차이를 파악할 수도 있습니다.

<span class="calculation-line">계산: 카운트 </span>

{% endapi %}

{% api %}

### 스팸 {#spam}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>스팸</i>:</b> 카운트</li>
        <li><b><i>스팸 %</i> 또는 <i>스팸률 %</i>:</b> (스팸으로 표시됨) / (발송)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 고유 열람 {#unique-opens}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} 이메일의 경우, 이는 7일 동안 추적됩니다. 즉, 동일한 사용자가 7일 후에 같은 이메일을 다시 열면 새로운 고유 열람으로 집계됩니다. 따라서 대시보드의 고유 열람 수는 Currents 데이터에 대한 단순 `DISTINCT user_id` 쿼리보다 높을 수 있습니다. Currents에서 대시보드 수치와 일치시키려면 `is_unique`가 `true`인 이벤트를 필터링하세요.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>고유 열람</i>:</b> 카운트</li>
        <li><b><i>고유 열람 %</i> 또는 <i>고유 열람률</i>:</b> (고유 열람) / (전달)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 고유 클릭 {#unique-clicks}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} 이메일의 경우 7일 동안 추적되며 <a href='/docs/user_guide/messaging/messaging_fundamentals/dispatch_id'>dispatch_id</a>(단일 발송 시도) 단위로 측정됩니다. 여기에는 Braze에서 제공하는 탈퇴 링크 클릭도 포함됩니다. 추적되는 커스텀 구독취소 URL도 사용자가 링크를 선택하면 *고유 클릭*에 집계됩니다. 7일 후 동일한 사용자가 다시 클릭하면 새로운 고유 클릭으로 집계됩니다. *고유 클릭*을 포함한 대시보드 이메일 인게이지먼트 측정기준은 Braze에서 계산되며 ESP 집계 보고서와 조정되지 않습니다. Currents에서 대시보드 수치와 일치시키려면 `is_unique`가 `true`인 이벤트를 필터링하세요.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>고유 클릭</i>:</b> 카운트</li>
        <li><b><i>고유 클릭 %</i> 또는 <i>클릭률</i>:</b> (고유 클릭) / (전달)</li>
    </ul>
</span>
{:/}

#### 이메일 히트맵에서 예상치 못한 링크 {#unexpected-links-on-the-email-heatmap}

[이메일 히트맵]({{site.baseurl}}/user_guide/channels/email/reporting)에 예상치 못한 링크가 표시되면, 메시지 HTML에서 추적 URL을 생성하는 [콘텐츠 블록]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks) 또는 단어 사이의 간격을 확인하세요. 히트맵 보기에서 **총 클릭 수 기준 링크 테이블**을 사용하여 표시된 텍스트와 일치하지 않는 URL을 식별하세요.

Braze는 메시지 미리보기에서 Liquid 태그를 확장하지 않으므로, 히트맵 렌더러는 미리보기에서 클릭된 링크를 매칭할 수 없습니다. 이는 예상된 동작입니다. 히트맵 렌더러는 클릭된 URL을 메시지의 URL과 매칭하려고 시도합니다. 전체 URL이 이벤트 속성정보로 전달되는 경우처럼 URL이 크게 다르면, 히트맵이 이를 식별할 수 없습니다.

{% endapi %}

{% api %}

### 총 클릭 수 {#total-clicks}

{% apitags %}
Count, Percentage
{% endapitags %}

<i>총 클릭 수</i>는 사용자가 전달된 이메일의 링크를 클릭한 총 횟수이며, 동일한 사용자의 여러 번 클릭도 포함됩니다. 여기에는 Braze 탈퇴 링크 및 추적되는 커스텀 구독취소 URL 클릭도 포함됩니다.

*총 클릭 수*가 *고유 클릭*보다 훨씬 높은 경우, 보안 도구 또는 사서함 공급자가 사용자가 메시지를 열지 않은 상태에서 링크를 스캔하고 있을 수 있습니다. 내부적으로 참여를 평가할 때는 *고유 클릭*을 비교하세요.

{% endapi %}

{% api %}

### 구독취소 또는 가입 취소 {#unsubscribers-or-unsub}

{% apitags %}
Count, Percentage
{% endapitags %}

_구독취소_는 Braze의 표준 구독취소 링크를 반영합니다. 커스텀 구독취소 페이지는 API를 사용하여 사용자를 업데이트하지 않는 한 이 측정기준에 반영되지 않습니다. **구독 그룹 시계열**은 여전히 API 기반 변경 사항을 반영합니다.

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>구독취소</i> 또는 <i>가입 취소</i>:</b> 카운트</li>
        <li><b><i>구독취소 %</i> 또는 <i>가입 취소율</i>:</b> (구독취소) / (전달)</li>
    </ul>
</span>
{:/}

#### *구독취소*와 구독취소 링크 클릭 수가 다를 수 있는 이유 {#why-unsubscribes-and-unsubscribe-link-clicks-can-differ}

이메일 Campaign 또는 Canvas의 **Analytics** 페이지에서 **Total Clicks** 또는 **Unique Clicks**를 확장할 때 링크별 분석에서 Braze 구독취소 URL 클릭 수와 *구독취소* 수를 비교해 보세요. 두 수치는 대체로 일치하지만 차이가 발생할 수 있습니다.

- ***구독취소*가 본문 구독취소 URL 클릭 수보다 많은 경우:** [List-unsubscribe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe)는 이메일 헤더에 있는 추가 구독취소 경로입니다(메시지 본문의 링크가 아님). 사용자가 이 방법으로 구독을 취소하면 *구독취소*에는 집계되지만 본문의 추적된 구독취소 URL 클릭으로는 집계되지 않습니다.
- **본문 구독취소 URL 클릭 수가 *구독취소*보다 많은 경우:** 사용자가 해당 링크를 여러 번 선택할 수 있습니다. 구독을 취소한 후 다시 구독하고 다시 구독을 취소하면, 이메일 분석에서 클릭 분석에 여러 번의 클릭(예: 두 번)이 기록될 수 있습니다.

자세한 내용은 [구독취소 수와 구독취소 링크 클릭 수가 다른 이유는 무엇인가요?]({{site.baseurl}}/user_guide/channels/email/faq#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link)를 참조하세요.

{% endapi %}

{% api %}

### 매출 {#revenue}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">계산: 카운트 </span>

{% endapi %}

{% api %}

### 주요 전환 (A) 또는 주요 전환 이벤트 {#primary-conversions-a-or-primary-conversion-event}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 이메일, 푸시, 웹훅의 경우 최초 발송 후부터 전환을 추적하기 시작합니다.

{::nomarkdown}
<span class="calculation-line">
    계산:
    <ul>
        <li><b><i>주요 전환 (A)</i> 또는 <i>주요 전환 이벤트</i>:</b> 카운트</li>
        <li><b><i>주요 전환 (A) %</i> 또는 <i>주요 전환 이벤트 비율</i>:</b> (주요 전환) / (고유 수신자)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### 신뢰도 {#confidence}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### 머신 열람 {#machine-opens}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} 이 측정기준은 SendGrid의 경우 2021년 11월 11일부터, SparkPost의 경우 2021년 12월 2일부터 추적됩니다.

<span class="calculation-line">계산: 카운트 </span>

{% endapi %}

{% api %}

### 기타 열람 {#other-opens}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} 사용자는 *머신 열람* 횟수가 기록되기 전에 이메일을 열 수도 있습니다(이 경우 열람 횟수는 <i>기타 열람</i>에 포함됩니다). Apple Mail이 아닌 받은편지함에서 머신 열람 이벤트 이후 사용자가 이메일을 한 번(또는 그 이상) 열면, 사용자가 이메일을 연 횟수는 <i>기타 열람</i>에 집계되고 <i>고유 열람</i>에는 한 번만 집계됩니다.

<span class="calculation-line">계산: 카운트 </span>

{% endapi %}

{% api %}

### 추정 실제 열람 {#estimated-real-opens}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} Braze는 새로운 열람 및 클릭 데이터가 도착하면 이 추정치를 재계산합니다. 이 값은 일반적으로 발송 후 며칠 내에 안정화되지만, 새로운 적격 이벤트가 발생하면 계속 업데이트됩니다.

{% endapi %}

{% api %}

### 클릭 대비 열람률 {#click-to-open-rate}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">계산: (고유 클릭) / (고유 열람) (이메일의 경우)</span>

#### 메시지 열람 가능성 점수 (세분화) {#message-open-likelihood-scores-segmentation}

[`Message Open Likelihood`]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#message-open-likelihood) Segment 필터는 사용자가 이메일을 열 가능성을 0~100 척도로 점수화합니다. 해당 채널에 대한 충분한 발송 또는 열람 이력이 없는 사용자는 빈 값으로 표시됩니다. 이메일의 경우 머신 열람은 계산에서 제외되며, 해당 채널의 최근 메시지 이력을 사용합니다([개별 채널에 대한 메시지 열람 가능성 필터]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel#individual-channels) 참조).

{% endapi %}

## 이메일 리포팅 문제 해결 및 FAQ {#email-reporting-troubleshooting-and-faqs}

### 수신 거부 링크와 고유 클릭 {#unsubscribe-links-and-unique-clicks}

수신자가 수신 거부 링크를 클릭하면 해당 동작이 URL을 사용하기 때문에 Braze에서는 이를 클릭으로 집계합니다. 이는 Braze에서 제공하는 수신 거부 링크와 메시지 본문에 포함된 커스텀 수신 거부 링크 모두에 적용됩니다. 이러한 클릭은 다른 링크 클릭과 함께 *고유 클릭* 및 *총 클릭*에 포함됩니다. 측정기준 정의는 [고유 클릭](#unique-clicks) 및 [수신 거부 링크의 클릭 수와 수신 거부 수가 다르게 표시되는 이유는 무엇인가요?]({{site.baseurl}}/user_guide/channels/email/faq#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link)를 참조하세요.

### 브라우저에서 보기 {#view-in-browser}

Braze에는 "브라우저에서 이 이메일 보기" 기능이 기본 제공되지 않습니다. 이메일 콘텐츠를 외부 랜딩 페이지(예: 웹사이트)에 호스팅하고, 이메일 편집기의 **링크** 도구를 사용하여 메시지에서 해당 페이지로의 링크를 추가하세요. 자세한 내용은 ["브라우저에서 이 이메일 보기" 링크를 이메일에 추가할 수 있나요?]({{site.baseurl}}/user_guide/channels/email/faq#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails)를 참조하세요.

### 커스텀 수신 거부 페이지 업데이트 {#custom-unsubscribe-page-updates}

[커스텀 수신 거부 페이지]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences)에 대한 변경 사항은 몇 분 이내에 반영됩니다. 실시간 발송에서는 페이지의 단기 캐시를 사용하며, 변경 사항을 저장하면 캐시가 갱신됩니다.

### 용량 초과 및 사서함 가득 참 반송 {#over-quota-and-full-mailbox-bounces}

용량 초과 또는 사서함 가득 참 반송은 수신자의 사서함이 새 메일을 수신할 수 없음을 의미합니다. 유효하지 않거나 위험한 주소로 새로 가입한 사용자 또는 휴면 상태에서 받은편지함이 가득 찬 장기 비활성 프로필에서 이러한 주소를 확인할 수 있습니다.

Segment 및 소스별 반송률을 검토하고, 반복적으로 하드 반송되는 주소를 제거하거나 일몰 처리하며, 신규 구독자에게는 확인 또는 이중 옵트인을 사용하세요. 목록 위생 관리 방법에 대해서는 [전달 가능성 함정 및 스팸 트랩]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps) 및 [이메일 리포팅]({{site.baseurl}}/user_guide/channels/email/reporting#troubleshooting)을 참조하세요.

### 550 5.7.1 원치 않는 메일 {#550-571-unsolicited-mail}

`550 5.7.1` 응답(예: "Our system has detected that this message is likely unsolicited mail")은 평판이나 인게이지먼트 신호가 좋지 않을 때 엄격한 사서함 제공업체(예: Gmail)에서 주로 발생합니다. 일반적인 원인으로는 스팸 신고, 낮은 인게이지먼트, 구매 또는 임대한 목록, 갑작스러운 발송량 급증 등이 있습니다.

동의 기반 목록 성장에 집중하고, 비활성 구독자를 일몰 처리하며, 신고율과 반송률을 모니터링하세요. 자세한 내용은 [전달 가능성 함정 및 스팸 트랩]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps)을 참조하세요.

### 양호한 이메일 전달 가능성 비율 {#good-email-deliverability-rates}

**전달(Delivery)**은 수신 서버가 메시지를 수락하는지 여부를 의미하며, *전달 수* 및 반송률과 같은 측정기준으로 측정할 수 있습니다. **전달 가능성(Deliverability)**(받은편지함 도달)은 제공업체의 필터링에 따라 달라지며, Braze에서 단일 측정기준으로 표시되지 않습니다.

일반적인 가이드로, 전달률은 99%에 가깝게, 하드 반송은 약 1% 미만을 목표로 하고, 열람 및 클릭을 통해 인게이지먼트 추세를 관찰하세요. 정확한 목표는 업종과 발송 패턴에 따라 다릅니다. 평판을 지원하는 방법에 대해서는 [이메일 전달 가능성 개선]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) 및 [전달 가능성 함정 및 스팸 트랩]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps)을 참조하세요.

### "Campaign is already in delay window, so not enqueueing another"

[액션 기반 Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)의 메시지 활동 또는 진단 로그에서 이 처리 결과는 동일한 사용자에 대한 이전 트리거가 아직 Campaign의 전달 기간 내에 있는 동안 Braze가 중복 발송을 차단했음을 의미합니다. 디바운스 잠금이 동일한 트리거 버스트에 대한 다중 대기줄 등록을 방지합니다.

다음 중 하나라도 해당되면 Campaign이 **즉시 발송**으로 표시되어 있어도 이 결과가 나타날 수 있습니다:

- Campaign이 [예외 이벤트]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) 또는 타이밍에 영향을 미치는 발송 시간 지연을 사용합니다.
- 사용자에게 [재자격]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) 기간이 있어 해당 기간이 지나야 메시지를 다시 수신할 수 있습니다.
- 트리거가 겹칠 때 더 높은 우선순위를 가진 다른 Campaign 또는 Canvas 메시지 단계가 발송 슬롯을 소비했습니다.

사용자가 메시지를 수신했어야 하지만 수신하지 못한 경우, 동일한 트리거에 대한 이전 결과(예: 이메일 반송 또는 채널 미활성화)를 확인하세요. 동일한 워크플로의 다른 메시지가 이 발송을 방지했을 수 있습니다.

### Braze는 이메일의 고유 클릭을 어떻게 계산하나요? {#how-does-braze-calculate-unique-clicks-for-email}

Braze는 수신자별, [`dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id)별로 7일 기간 동안 *고유 클릭*을 집계합니다. 전체 정의, 수식, 수신 거부 링크 동작 및 Currents 정렬에 대해서는 [고유 클릭](#unique-clicks)을 참조하세요.