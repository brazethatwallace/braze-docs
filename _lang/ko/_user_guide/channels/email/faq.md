---
nav_title: FAQ
article_title: 이메일 FAQ
page_order: 30
description: "이 페이지에서는 이메일 메시징에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
channel: email

---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 문서에서는 이메일에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 이메일이 발송될 때 여러 프로필이 동일한 이메일 주소를 가지고 있으면 어떻게 되나요? {#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address}

일치하는 이메일 주소를 가진 여러 사용자가 Campaign을 수신할 Segment에 포함되어 있는 경우, 발송 시점에 해당 이메일 주소를 가진 단일 고객 프로필이 선택됩니다. 이렇게 하면 이메일이 한 번만 발송되고 중복이 제거되어 동일한 이메일 주소로 여러 번 도달하지 않습니다.

**고유 이메일 주소:** Braze는 프로필 간에 고유한 이메일 주소를 강제하지 않습니다. 이메일 주소와 프로필 간의 일대일 관계에 의존하는 경우, 사용자를 생성할 때 내부적으로 중복을 모니터링하세요.

**Liquid 이전 중복 제거:** Braze가 하나의 디스패치 내에서 이메일 주소별로 중복을 제거하는 발송(예: 동일한 주소를 가진 여러 Segment 멤버가 함께 처리되는 스케줄된 Campaign)의 경우, 해당 중복 제거는 해당 주소를 대표하도록 선택된 프로필에 대해 Liquid가 실행되기 전에 발생합니다. 해당 프로필에 대해 Liquid가 중단되면(예: [`abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) 사용 시), 해당 주소는 해당 디스패치에서 메시지를 수신하지 않습니다—중복 제거로 이미 건너뛴 프로필도 포함됩니다. 트리거된 발송에는 동일한 디스패치 내 주소 중복 제거가 적용되지 않습니다. 주소를 공유하는 여러 프로필이 하나의 배치에서 모두 적격 상태를 유지할 수 있으므로, 이 중단 동작은 동일한 방식으로 적용되지 않습니다(다음 단락 참조).

여러 프로필이 이메일 주소를 공유하고 하나의 프로필이 탈퇴하면, Braze는 해당 주소를 가진 다른 프로필(최대 100개)을 동일한 구독 상태로 업데이트합니다. 이는 탈퇴 및 글로벌 구독 상태와 개별 구독 그룹 상태 변경과 같은 기타 변경 사항에 적용됩니다.

**시드 그룹:** [시드 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups)이 있는 Campaign의 경우, 여러 프로필이 주소를 공유할 때 Braze는 기본 전달을 위해 하나의 프로필을 선택합니다. 해당 기본 수신자는 동일한 주소를 가진 다른 프로필이 시드 그룹에 있더라도 시드 그룹에 포함되지 않을 수 있습니다.

다음 시나리오에서는 사용자가 이메일을 두 번 받은 것처럼 보일 수 있습니다:

- **시드 목록 또는 테스트 수신자:** 시드 주소와 내부 테스트 수신자는 주요 오디언스 외에 추가로 발송을 수신할 수 있으며, 받은편지함이 프로필과 시드 항목 모두에 일치하는 경우 중복처럼 보일 수 있습니다.
- **Campaign 또는 Canvas 생성 중 오류가 발생한 경우:** 사용자가 문자 그대로 동일한 발송을 두 번 받지는 않을 수 있지만, 동일한 제목란을 가진 두 개의 별도 이메일을 받을 수 있습니다. Campaign이나 Canvas가 복제된 경우, 이미지나 제목란과 같은 이메일 구성 세부 정보를 확인하세요. 또한 체인지로그를 참조하여 Campaign이나 Canvas가 시작 후 수정되었는지 확인할 수 있습니다—복제본은 사용자가 수신했을 때 원본과 동일한 제목란을 공유할 수 있습니다.
- **여러 고객 프로필에 이메일 전달이 설정된 경우:** 사용자가 특정 앱에서 여러 계정을 가지고 있지만 하나의 계정이 메일을 전달하는 경우, 사용자는 받은편지함당 한 번 Campaign을 수신합니다. 메시지가 전달되는 받은편지함에서는 메일이 두 번 나타날 수 있습니다. 일부 공급자만 이메일이 다른 계정에서 전달되었음을 표시합니다.
- **수신자의 이메일 구성:** 일부 클라이언트는 받은편지함을 병합합니다("통합 받은편지함"). 동일한 Campaign이 하나의 받은편지함을 공유하는 여러 계정을 타겟팅하는 경우, 실제로는 두 개의 별개 프로필에 메시지가 전송되었지만 한 사람이 Campaign을 두 번 받은 것처럼 보일 수 있습니다. 수신자는 여러 계정이 하나의 받은편지함에 결합되어 있는지 확인할 수 있습니다.

이 중복 제거는 타겟팅된 사용자가 동일한 디스패치에 포함된 경우에 적용됩니다. 재적격성은 이메일 주소가 아닌 프로필 단위로 평가됩니다.

이메일 Campaign 및 캔버스 단계 재적격성은 받은편지함이 아닌 각 사용자의 프로필을 사용하므로, 해당 로직이 충족되는 동안 여러 프로필이 별도의 발송에 대해 자격을 얻을 수 있습니다. 트리거와 결합하면, 주소 수준에서 단일 비적격 기간을 준수하려는 경우에도 동일한 받은편지함에 두 개 이상의 메시지가 전달될 수 있습니다. 트리거된 Campaign(API 트리거 Campaign 제외)과 Canvases는 일치하는 이메일 주소를 가진 서로 다른 프로필이 서로 다른 시간에 트리거를 충족하는 경우 동일한 주소로 두 번 발송할 수도 있습니다—예를 들어, 사용자 A와 사용자 B가 `johndoe@example.com`을 공유하지만 서로 다른 시간대에 있고 전달이 현지 시간대를 사용하는 경우입니다.

사용자는 Canvas 진입 시 이메일로 중복 제거되지 않으므로, 속도 제한된 진입으로 인해 약간 다른 시간에 진행하는 경우 Canvas의 첫 번째 단계 이후에는 중복 제거되지 않을 수 있습니다. 특정 이메일 주소와 연결된 사용자가 이메일을 열거나 클릭하면, 해당 이메일 주소를 공유하는 모든 고객 프로필이 Campaign을 열었거나 클릭한 것으로 표시됩니다.

### 예외: API 트리거 Campaign {#exception-api-triggered-campaigns}

API 트리거 Campaign은 오디언스가 정의된 위치에 따라 중복을 제거하거나 중복 발송합니다. 중복 이메일이 여러 전달을 수신하려면 API 호출에서 별도의 `user_ids`를 사용하여 개별적으로 타겟팅해야 합니다. API 트리거 Campaign에 대한 세 가지 가능한 시나리오는 다음과 같습니다:

- **시나리오 1: 타겟 Segment의 중복 이메일:** 동일한 이메일이 API 트리거 Campaign의 대시보드 오디언스 필터에 그룹화된 여러 고객 프로필에 나타나는 경우, 프로필 중 하나만 이메일을 수신합니다.
- **시나리오 2: 수신자 오브젝트 내 서로 다른 `user_ids`의 중복 이메일:** 동일한 이메일이 `recipients` 오브젝트에서 참조하는 여러 `external_user_id` 값 내에 나타나는 경우, 이메일은 두 번 발송됩니다.
- **시나리오 3: 수신자 오브젝트 내 중복 `user_ids`로 인한 중복 이메일:** 동일한 고객 프로필을 두 번 추가하려고 하면, 프로필 중 하나만 이메일을 수신합니다.

{% alert important %}
API 호출을 통해 API Campaign을 발송하는 경우(API 트리거 Campaign 제외), Segment 오디언스에 동일한 이메일 주소를 가진 여러 사용자가 지정되어 있으면 호출에 나열된 횟수만큼 해당 주소로 발송됩니다. 이는 API 호출이 의도적으로 구성된 것으로 간주되기 때문입니다.
{% endalert %}

#### 중복 이메일 주소를 사용한 A/B 테스트 {#ab-testing-with-duplicate-email-addresses}

여러 프로필이 동일한 이메일 주소를 공유할 수 있는 경우 이메일에서 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing)를 사용하지 마세요. 배리언트는 프로필 단위로 할당되므로 동일한 받은편지함에 두 개 이상의 메시지가 전달될 수 있습니다. 해당 상황에서 테스트해야 하는 경우, **우승 배리언트** 단계를 [현지 시간대 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns)과 결합하여 우승자 선택을 지연시키는 방식으로 사용하지 마세요—이러한 옵션을 함께 사용하면 중복 발송 가능성이 높아질 수 있습니다.

#### Canvas와 중복 이메일 주소 {#canvas-and-duplicate-email-addresses}

Canvas 여정의 경우, 중복 이메일 주소가 한 번 발송을 수신하는지 또는 두 번 이상 수신하는지는 진입 배치, 단계 타이밍 및 기타 요인에 따라 달라질 수 있습니다. 여정에 대해 검증할 때까지 동작을 정의되지 않은 것으로 간주하세요. 가능하면 중복 프로필을 병합하거나 통합하세요. 제품 변경이 필요한 경우 Braze 팀을 통해 피드백을 제출하세요.

### 사용자의 이메일 주소가 다른 사용자가 공유하는 주소로 변경되면 구독 상태는 어떻게 되나요? {#what-happens-to-the-subscription-state-when-a-users-email-address-changes-to-one-shared-by-another-user}

사용자 A의 이메일 주소를 기존 사용자 B가 공유하는 다른 이메일 주소로 설정하거나 업데이트하면, **사용자가 이메일을 업데이트할 때 재구독** 설정이 켜져 있지 않는 한 사용자 A는 사용자 B에게 이미 존재하는 구독 상태를 상속받습니다.

### 발신 이메일 설정 업데이트가 소급 적용되나요? {#will-updates-to-my-outbound-email-settings-apply-retroactively}

아니요. 발신 이메일 설정에 대한 업데이트는 기존 발송에 소급 적용되지 않습니다. 예를 들어, 이메일 설정에서 기본 표시 이름을 변경해도 활성 Campaign이나 Canvases의 기존 기본 표시 이름이 자동으로 교체되지 않습니다.

### "좋은" 이메일 전달률이란 무엇인가요? {#what-is-a-good-email-delivery-rate}

일반적으로 "이상적인 수치"는 반송률이 3%를 넘지 않으면서 메시지의 약 98%가 전달되는 것입니다. 전달률이 이 수치 아래로 떨어지면 보통 우려할 만한 원인이 있습니다.

그러나 98% 이상의 비율에서도 전달 가능성 문제가 있을 수 있습니다. 예를 들어, 모든 반송이 단일 도메인에서 발생하는 경우 해당 공급자와의 평판 문제를 나타내는 명확한 신호입니다.

또한 메시지가 전달되었지만 스팸 폴더에 들어갈 수 있으며, 이는 잠재적으로 심각한 평판 문제를 나타냅니다. 전달되는 메시지 수뿐만 아니라 열람률과 클릭률도 모니터링하여 사용자가 실제로 받은편지함에서 메시지를 보고 있는지 확인하는 것이 중요합니다. 공급자는 보통 모든 스팸 인스턴스를 보고하지 않으므로, 1%의 스팸률도 우려의 원인이 될 수 있으며 추가 분석이 필요합니다.

마지막으로, 비즈니스와 발송하는 이메일 유형도 전달에 영향을 미칠 수 있습니다. 예를 들어, 주로 [트랜잭션 이메일]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign)을 발송하는 사람은 많은 마케팅 메시지를 발송하는 사람보다 더 나은 비율을 기대할 수 있습니다.

### 이메일 전달 측정기준이 합산하여 100%가 되지 않는 이유는 무엇인가요? {#why-are-my-email-delivery-metrics-not-adding-up-to-100}

이메일 전달 측정기준(전달, 반송, 스팸률)은 소프트바운스된 후 최대 72시간의 재시도 기간 후에도 전달되지 않은 이메일로 인해 합산하여 100%가 되지 않을 수 있습니다.

소프트바운스는 "사서함 가득 참", "서버 일시적으로 사용 불가" 등과 같은 일시적이거나 과도적인 문제로 인해 반송되는 이메일입니다. 소프트바운스된 이메일이 72시간 후에도 여전히 전달되지 않으면, 이 이메일은 Campaign 전달 측정기준에 포함되지 않습니다.

### 이메일 피드백 루프란 무엇인가요? {#what-is-an-email-feedback-loop}

이메일 피드백 루프(FBL)를 사용하면 발신자가 높은 불만 건수를 받는 Campaign을 식별하여 평판을 모니터링할 수 있습니다. Gmail 피드백 루프를 구현하는 단계는 [Google의 피드백 루프](https://support.google.com/a/answer/6254652) 문서를 참조하세요.

### 열람 추적 픽셀이란 무엇인가요? {#what-are-open-tracking-pixels}

[열람 추적 픽셀]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#changing-location-of-tracking-pixel)은 발신자의 이메일 클릭 추적 도메인을 활용하여 이메일 열람 이벤트를 추적합니다. 이 픽셀은 이메일의 HTML에 추가되는 이미지 태그입니다. 가장 일반적으로 body 태그 내의 마지막 HTML 요소입니다. 사용자가 이메일을 로드하면 브랜드 추적 도메인에서 이미지를 채우기 위한 요청이 이루어지며, 이를 통해 열람 이벤트가 기록됩니다.

### 이메일 Campaign이나 Canvas가 중지되면 어떻게 되나요? {#what-happens-when-an-email-campaign-or-canvas-is-stopped}

사용자는 Canvas에 진입할 수 없으며, 더 이상 메시지가 발송되지 않습니다.

이메일 Campaign과 Canvases의 경우, 중지 버튼은 발송을 즉시 중단하지 않습니다. 발송 요청이 전송되면 사용자에게 전달되는 것을 막을 수 없으며, 이는 약간의 지연 후에 발생할 수 있습니다.

Campaign이나 Canvas가 중지된 후에는 Braze가 더 이상 요청을 보내지 않지만, 이메일 서비스 공급자가 이미 진행 중인 요청을 처리하는 동안 분석 수치가 계속 증가할 수 있습니다.

### 이메일 분석에서 *총 클릭 수*가 *총 열람 수*보다 많은 이유는 무엇인가요? {#why-am-i-seeing-more-_total-clicks_-than-_total-opens_-in-my-email-analytics}

*총 열람 수*는 사용자가 이메일을 열어본 횟수이고, *총 클릭 수*는 사용자가 전달된 이메일 내에서 링크 클릭 등 모든 유형의 클릭을 포함하여 클릭한 횟수입니다. 다음과 같은 이유로 열람보다 클릭이 더 많을 수 있습니다:

- 사용자가 한 번의 열람 내에서 이메일 본문을 여러 번 클릭하는 경우.
- 사용자가 휴대폰의 미리보기 창에서 일부 이메일 링크를 클릭하는 경우. 이 경우 Braze는 이 이메일을 클릭된 것으로 기록하지만 열린 것으로는 기록하지 않습니다.
- 사용자가 이전에 미리 본 이메일을 다시 여는 경우.

### 이메일 열람 및 클릭이 0으로 표시되는 이유는 무엇인가요? {#why-am-i-seeing-zero-email-opens-and-clicks}

추적 도메인의 구성 오류가 있는 경우 이메일 열람이나 클릭이 표시되지 않을 수 있습니다. 이는 다음과 같은 이유 때문일 수 있습니다:
- 추적 URL이 `https` 대신 `http`인 SSL 문제가 있는 경우.
- 열람 이벤트, 클릭 이벤트 또는 둘 다에서 사용자 에이전트 문자열이 채워지지 않는 CDN 문제가 있는 경우.

### 서버 클릭을 트리거할 수 있는 잠재적 위험은 무엇인가요? {#what-are-the-potential-risks-of-triggering-server-clicks}

지나치게 긴 메시지나 너무 많은 느낌표와 같은 이메일 메시지의 특정 요소는 이메일 보안 응답을 트리거할 수 있습니다. 이러한 응답은 보고 및 IP 평판에 영향을 미치고 사용자가 탈퇴하게 만들 수 있습니다.

이러한 응답을 처리하는 모범 사례에 대해서는 [클릭률 증가 처리]({{site.baseurl}}/user_guide/channels/email/reporting)를 참조하세요.

### Braze가 "탈퇴" 측정기준에 포함되는 탈퇴 링크를 추적할 수 있나요? {#can-braze-track-unsubscribe-links-counted-toward-the-unsubscribe-metric}

Braze는 이메일 내에서 다음 Liquid가 사용되는 경우 탈퇴 링크를 추적합니다: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### 탈퇴 수와 탈퇴 링크 클릭 수가 다른 이유는 무엇인가요? {#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link}

*탈퇴* 수가 이메일 본문의 탈퇴 링크를 클릭한 사용자보다 많은 경우, [**List-unsubscribe**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe)가 그 차이를 설명하는 경우가 많습니다. List-unsubscribe는 이메일 헤더에 있는 추가 탈퇴 경로입니다(메시지 본문의 링크가 아님). 사용자가 이 방법으로 탈퇴하면 *탈퇴*로 집계되지만 본문의 추적된 탈퇴 URL 클릭으로는 집계되지 않습니다.

본문 탈퇴 링크의 총 클릭 수가 *탈퇴* 수보다 많은 경우, 사용자가 링크를 두 번 이상 클릭했을 수 있습니다—예를 들어, 탈퇴한 후 다시 가입하고 다시 탈퇴한 경우 이메일 분석의 클릭 분석에서 여러 번의 클릭이 기록될 수 있습니다.

사용자가 탈퇴 링크를 두 번 클릭한 경우(예: 탈퇴한 후 다시 가입하고 다시 탈퇴한 경우), 이메일 분석에서 두 번으로 집계됩니다.

### 이메일에 "브라우저에서 이 이메일 보기" 링크를 추가할 수 있나요? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

아니요. Braze는 이 기능을 제공하지 않습니다. 이는 점점 더 많은 이메일이 모바일 기기와 최신 이메일 클라이언트에서 열리고 있으며, 이러한 클라이언트는 이미지와 콘텐츠를 문제없이 렌더링하기 때문입니다.

**해결 방법:** 동일한 결과를 얻으려면 이메일 콘텐츠를 외부 랜딩 페이지(예: 웹사이트)에 호스팅한 다음, 이메일 본문을 편집할 때 **Link** 도구를 사용하여 구축 중인 이메일 Campaign에서 해당 페이지로 링크할 수 있습니다.

### Braze가 일반 텍스트 URL이나 "www." 텍스트를 자동으로 링크로 변환하나요? {#does-braze-automatically-turn-plain-text-urls-or-www-text-into-links}

아니요. Braze는 메시지를 스캔하여 `www.`로 시작하거나 URL처럼 보이는 일반 텍스트를 하이퍼링크로 변환하지 않습니다. HTML 앵커 태그(`<a href="...">`)로 정의한 링크만 Braze의 일반 렌더링 및 링크 기능을 통해 처리됩니다.

수신자가 일반 텍스트가 클릭 가능한 링크로 표시되는 것을 보는 경우, 이 동작은 보통 이메일 클라이언트(예: Gmail, Outlook 또는 Apple Mail)에서 발생합니다. 많은 클라이언트는 메시지가 전달된 후 URL과 유사한 문자열을 감지하여 수신자의 기기에서 링크로 변환합니다. Braze는 이 동작을 제어하지 않으며 수신자를 위해 이를 끌 수 없습니다.

예측 가능한 링크 표시, 추적 및 스타일링을 위해 일반 텍스트 URL 대신 명시적인 `<a href>` 태그를 사용하세요.

### 이메일 보안 소프트웨어에 의해 사용자가 자동으로 탈퇴되는 이유는 무엇인가요? {#why-are-my-users-being-auto-unsubscribed-by-email-security-software}

일부 기업 이메일 보안 도구(예: Barracuda, Proofpoint 및 유사 서비스)는 탈퇴 링크를 포함하여 수신 이메일의 모든 URL을 사전 가져오기하거나 스캔합니다. 이로 인해 보안 도구가 원클릭 list-unsubscribe 링크를 따라갈 때 의도하지 않은 탈퇴가 발생할 수 있습니다.

이를 완화하려면:

- **수신자에게 발송 도메인을 허용 목록에 추가하도록 권장하세요:** 영향을 받는 수신자의 IT 팀과 협력하여 발송 도메인과 Braze 추적 도메인을 이메일 보안 허용 목록에 추가하세요.
- **환경설정 센터를 사용하세요:** 직접 탈퇴 링크 대신 탈퇴 동작을 확인하기 위해 사용자 상호작용이 필요한 [환경설정 센터]({{site.baseurl}}/user_guide/channels/email/subscriptions)를 사용하세요. 보안 스캐너는 일반적으로 다단계 양식을 완료하지 않습니다.
- **탈퇴 로그를 검토하세요:** Currents 탈퇴 이벤트 데이터에서 `User-Agent` 헤더와 IP 주소를 확인하여 자동 스캔과 일치하는 패턴(예: 여러 탈퇴에 걸쳐 일관된 `User-Agent` 헤더)을 식별하세요.

서버 측 스캔이 이메일 측정기준에 미치는 영향에 대한 자세한 내용은 [클릭률 증가 처리]({{site.baseurl}}/user_guide/channels/email/reporting#handling-increases-in-click-rates)를 참조하세요.

### 머신 열람률이 예기치 않게 변경된 이유는 무엇인가요? {#why-has-my-machine-open-rate-changed-unexpectedly}

[머신 열람]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens)은 Apple Mail 개인정보 보호(MPP)와 같은 이메일 보안 기능에 의해 트리거되며, 사용자가 실제로 이메일을 열지 않아도 이메일 콘텐츠(추적 픽셀 포함)를 사전 로드합니다. 머신 열람률은 다음에 따라 변동할 수 있습니다:

- 오디언스 중 Apple Mail 또는 기타 개인정보 보호가 활성화된 이메일 클라이언트를 사용하는 비율의 변화.
- 이메일 공급자의 개인정보 보호 기능 또는 봇 감지 동작의 업데이트.
- 오디언스 세분화 또는 타겟팅의 변경.

머신 열람 비율은 실제 참여의 신뢰할 수 있는 척도가 아닙니다. 이메일 성과를 보다 정확하게 파악하려면 *기타 열람*(비머신 열람)과 *고유 클릭*에 집중하세요. [이메일 성과 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance)를 사용하여 시간에 따른 이러한 측정기준을 비교할 수도 있습니다.

### Gmail에서 딥링크가 작동하지 않는 이유는 무엇인가요? {#why-are-my-deep-links-not-working-in-gmail}

Gmail은 이메일 메시지에서 모든 비HTTP/HTTPS 링크를 제거합니다. 딥링크가 커스텀 스킴(예: `myapp://path/to/content`)을 사용하는 경우, Gmail이 이를 제거하며 Gmail에서 이메일을 읽는 수신자에게는 링크가 작동하지 않습니다. 이는 Braze의 제한이 아닌 Gmail의 제한입니다.

이를 해결하려면:

- **유니버설 링크(iOS) 또는 앱 링크(Android)를 사용하세요.** 이들은 앱이 설치된 경우 앱을 열고 그렇지 않으면 웹 페이지로 폴백하는 표준 `https://` URL을 사용합니다. 설정 방법은 [유니버설 링크 및 앱 링크]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links)를 참조하세요.
- **딥링킹 공급자를 사용하세요.** [Branch](https://www.branch.io/)와 같은 서비스는 Gmail을 포함한 이메일 클라이언트와 호환되는 HTTP 형식의 딥링크를 생성합니다.
- **리디렉트 엔드포인트를 설정하세요.** 서버에 앱의 커스텀 스킴 URL로 리디렉트하는 `https://` 엔드포인트를 호스팅하세요. 이메일 클라이언트는 `https://` 링크를 유지하며, 리디렉트가 앱 열기를 처리합니다.

### *고유 열람* 측정기준에 *머신 열람*이 포함되나요? {#does-the-unique-opens-metric-include-machine-opens}

네. *고유 열람*에는 *머신 열람*이 포함됩니다. **Campaign Analytics** 보기와 **보고서 빌더**에서 두 측정기준을 모두 확인할 수 있습니다.

### 이메일 전달량이 발송량과 일치하지 않는 이유는 무엇인가요? {#why-does-my-email-delivery-volume-not-match-my-send-volume}

이메일이 발송된 후, 수신자의 받은편지함이 전달 시점을 결정합니다. 사서함 가득 참, 특정 IP에서의 이메일 서비스 공급자 스로틀링 등의 이유로 메시지가 몇 시간 또는 며칠 동안 지연될 수 있습니다.

지연된 메시지가 발송일과 다른 날짜에 전달되면, 동일한 날짜 범위에서 _전달_이 _발송_을 초과할 수 있습니다. 많은 지연이 하루에 집중되면, 해당 범위에서 _발송_이 _전달_을 초과할 수 있습니다.

### 이메일에 이미 탈퇴 링크가 있는데 탈퇴 링크를 포함하라는 경고가 표시되는 이유는 무엇인가요? {#why-am-i-seeing-a-warning-to-include-an-unsubscribe-link-when-my-email-already-has-one}

이 경고는 탈퇴 링크가 없었던 Campaign에서 복제된 Campaign에서 지속될 수 있습니다. 이를 해결하려면:

- HTML 이메일의 경우, **Plaintext** 탭으로 이동한 다음 **Regenerate from HTML**을 선택하세요.
- 복제 후, 배리언트를 복제한 다음 원본 배리언트를 제거하세요. 원본 배리언트를 **선택하지 마세요**. 그렇지 않으면 경고가 이어질 수 있습니다.

### 사용자가 받지 말아야 할 이메일을 받은 이유는 무엇인가요? {#why-did-a-user-receive-an-email-they-shouldnt-have}

Braze가 구성된 대로 동작했더라도 전달이 잘못된 것처럼 보일 수 있습니다. 다음 사항을 확인하세요:

- 하나의 받은편지함을 공유하는 **중복 프로필**([이메일이 발송될 때 여러 프로필이 동일한 이메일 주소를 가지고 있으면 어떻게 되나요?](#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address) 참조).
- 오디언스에 포함되었거나 CC/BCC로 발송에 포함된 **시드 목록, 테스트 수신자 또는 내부 주소**.
- **Segment 또는 Canvas 타이밍:** Braze가 적격성을 평가할 때 사용자가 오디언스 또는 캔버스 단계에 일치했지만, 메시지를 읽기 전에 속성이나 구독 상태가 변경된 경우.
- **구독 그룹:** 글로벌 구독 상태가 달리 시사하더라도 메시지가 타겟팅한 그룹에 사용자가 옵트인 상태를 유지한 경우.
- **API 또는 파일 가져오기**로 세분화 이후 변경 사항이 적용될 것으로 예상하기 전에 사용자가 업데이트된 경우.

[메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), Campaign 또는 Canvas 체인지로그, Segment 정의를 검토하세요. 발송을 여전히 확인할 수 없는 경우, 사용자 식별자, `dispatch_id`(가능한 경우) 및 타임스탬프와 함께 Braze 고객지원에 문의하세요.

### 사용자가 이메일 메시지를 받지 못한 이유는 무엇인가요? {#why-hasnt-a-user-received-my-email-message}

사용자가 수신할 것으로 예상한 이메일을 받지 못하는 데에는 다음과 같은 여러 이유가 있습니다:

- 이메일을 수신할 자격이 없었습니다.
- 이메일 주소가 유효하지 않거나 존재하지 않습니다.
- 메시지를 놓쳤거나 삭제했을 수 있습니다.
- 메시지가 스팸 폴더에 있을 수 있습니다.

{% alert tip %}
Braze의 전달 이벤트는 이메일이 사서함 공급자의 서버에 의해 수락되었음을 의미합니다. 그러나 이것이 메시지가 사용자의 받은편지함에 나타나는 것을 보장하지는 않습니다. 사서함 공급자가 메시지를 스팸으로 라우팅하거나, 드문 경우 메시지 표시를 조용히 차단할 수 있습니다.
{% endalert %}

다음 표를 사용하여 원인을 좁혀보세요.

#### 이메일이 발송되지 않은 경우 {#the-email-wasnt-sent}

| 가능한 원인 | 확인 사항 |
|---|---|
| 사용자가 Campaign 또는 Canvas에 적격하지 않았습니다 | **Target Audiences**(Campaign의 경우) 또는 **Target Audience**(Canvas의 경우) [설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)을 확인하여 발송 시점에 사용자가 모든 오디언스 필터, Segment 기준 및 전달 규칙을 충족했는지 확인하세요. |
| 메시지가 중단되었습니다 | [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에서 Liquid 오류나 필수 필드 누락과 같은 중단 사유를 확인하세요. |
| 사용자의 이메일 주소가 유효하지 않거나 누락되었습니다 | **사용자 검색**에서 사용자의 프로필을 확인하여 발송 시점에 유효한 이메일 주소가 등록되어 있었는지 확인하세요. |
| 사용자의 이메일 주소가 이전에 하드바운스되었습니다 | 하드바운스는 이메일 주소를 유효하지 않은 것으로 표시하고 해당 주소로의 향후 발송을 차단합니다. 마찬가지로, 수신자가 이메일을 스팸으로 표시하면 Braze는 해당 사용자에게 표준 Campaign이 아닌 트랜잭션 이메일만 발송합니다. 사용자 프로필의 **참여** 탭을 확인하세요. 자세한 내용은 [탈퇴된 이메일 주소]({{site.baseurl}}/user_guide/channels/email/subscriptions#unsubscribed-email-addresses) 및 [반송 및 유효하지 않은 이메일]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails)을 참조하세요. |
| 사용자가 이메일을 탈퇴했습니다 | **참여** 탭의 **연락처 설정**에서 사용자의 구독 상태를 확인하세요. Braze는 탈퇴한 사용자에게 이메일을 발송하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이메일이 발송되지 않은 원인" }

#### 이메일이 발송되었지만 받은편지함에 도착하지 않은 경우 {#the-email-was-sent-but-didnt-arrive-in-their-inbox}

| 가능한 원인 | 확인 사항 |
|---|---|
| 사서함 공급자(MBP)에 접근할 수 없었습니다 | 일시적인 문제로 이메일이 수신자의 MBP에 도달하지 못했습니다. 이는 일반적으로 재시도를 통해 자체적으로 해결됩니다. 이메일 서비스 공급자는 최대 72시간 동안 소프트바운스를 재시도합니다. |
| MBP가 이메일을 반송했습니다 | 수신자의 메일 서버가 이메일을 거부했습니다. [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에서 반송 세부 정보를 확인하세요. |
| MBP가 이메일을 조용히 삭제했습니다 | MBP가 이메일을 수락했지만 사용자에게 표시하지 않았고 반송도 반환하지 않았습니다. 이는 Braze의 제어 범위 밖이며 Braze 로그에서 감지할 수 없습니다. |
| 이메일이 스팸 폴더로 이동했습니다 | MBP가 메시지를 스팸으로 식별하여 사용자의 스팸 또는 정크 폴더로 라우팅했습니다. 사용자에게 스팸 폴더를 확인하도록 요청하세요. |
| 수신자에게 커스텀 메일 필터링이 있습니다 | 사용자 또는 IT 관리자가 수신 메시지를 필터링, 리디렉트 또는 삭제하는 사서함 규칙을 구성했을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이메일이 받은편지함에 도착하지 않은 원인" }

### Outlook에서 이미지를 최적화하려면 어떻게 해야 하나요? {#how-can-i-optimize-images-in-outlook}

Outlook은 종종 Microsoft Word 스타일 렌더링을 사용하여 이미지 주위에 테두리를 추가할 수 있습니다. 표준 조건부 주석을 사용하여 Office 클라이언트에서 숨겨지도록 콘텐츠를 래핑할 수 있습니다. 예를 들어:

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### 이메일 메시지에 SVG 또는 WEBP 이미지를 사용할 수 있나요? {#can-i-use-svg-or-webp-images-in-my-email-messages}

SVG 이미지는 Gmail 웹 또는 Gmail iOS에서 렌더링되지 않습니다. WEBP는 클라이언트 간에 일관되게 지원되지 않습니다. 대신 PNG 또는 JPEG와 같이 널리 지원되는 형식을 사용하여 이미지가 안정적으로 렌더링되도록 하세요.

### 메시지 작성기의 한 부분에서 할당된 Liquid 변수를 다른 부분에서 사용할 수 있나요? {#can-liquid-variables-assigned-in-one-part-of-the-message-composer-be-used-in-another}

아니요. 이메일의 각 부분(제목, 본문, 헤더, 버튼 등)은 별도로 생성되므로, 한 필드에서 할당된 Liquid는 다른 필드에서 사용할 수 없습니다. 필요한 각 필드에서 변수를 할당하세요.

### 이메일 템플릿이 없습니다. 어디에 있나요? {#my-email-template-is-missing-where-is-it}

먼저 템플릿을 볼 수 있는 [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 있는지 확인하세요. 저장된 이메일 템플릿을 보려면 **콘텐츠** > **이메일**로 이동하세요. 상태 및 유형(HTML 또는 드래그 앤 드롭)별로 템플릿을 필터링할 수 있습니다.

### 릴레이 또는 마스킹된 이메일에 대해 도메인을 등록해야 하나요? {#do-i-need-to-register-domains-for-relay-or-masked-emails}

[Apple의 Private Email Relay]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO)는 반송을 방지하기 위해 Apple Developer Portal에 발송 도메인을 등록해야 합니다. Google Shielded Email은 수동 도메인 등록이나 허용 목록 프로세스가 필요하지 않습니다.

### 반송 사유 `unable to get mx info` 또는 `failed to get IPs from PTR record`는 무엇을 의미하나요? {#what-does-the-bounce-reason-unable-to-get-mx-info-or-failed-to-get-ips-from-ptr-record-mean}

[메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에서 다음과 유사한 반송 사유는 Braze 메시지 구성이 아닌 수신 도메인의 메일 설정(주소에서 `@` 뒤의 도메인)을 확인하는 데 문제가 있음을 나타냅니다:

일반적인 원인은 다음과 같습니다:

- 해당 도메인에 대한 **MX 레코드**가 누락되었거나, 잘못되었거나, 접근할 수 없는 경우
- 수신 인프라에서 기대하는 **PTR(역방향 DNS)** 검사에 실패하거나 확인할 수 없는 인바운드 메일 호스트 이름
- 이메일 주소의 유효하지 않거나 잘못 입력된 도메인

**다음 단계:**

- 주소와 도메인 철자를 확인하세요.
- 주소가 올바른 경우, 해당 도메인의 사서함 소유자 또는 IT 팀에 문의하세요.
- DNS 공급자를 통해 메일 서버의 PTR 레코드를 포함한 MX 및 관련 DNS 레코드를 점검하도록 요청하세요.

다른 수신자는 보통 영향을 받지 않습니다. 소프트바운스가 보고에 표시되는 방식에 대해서는 [소프트바운스]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce)를 참조하세요.