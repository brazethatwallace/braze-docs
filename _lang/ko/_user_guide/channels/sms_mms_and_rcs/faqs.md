---
nav_title: FAQ
article_title: SMS, MMS, RCS FAQ
page_order: 30
description: "이 문서에서는 SMS, MMS, RCS 메시징에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
page_type: FAQ
alias: /sms_mms_rcs_faq/
channel:
  - SMS
  - MMS
  - RCS
---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 문서에서는 SMS, MMS, RCS 메시징에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 일반 {#general}

### SMS API 오브젝트에서 `app_id`란 무엇인가요? {#what-is-an-app_id-in-the-sms-api-object}

앱 식별자 API 키 또는 `app_id`는 워크스페이스 내 특정 앱에 활동을 연결하는 매개변수입니다. 워크스페이스 내에서 어떤 앱과 상호작용하는지를 지정합니다. 예를 들어, iOS 앱용 `app_id`, Android 앱용 `app_id`, 웹 통합용 `app_id`가 각각 있습니다.

**설정** > **앱 설정**으로 이동하여 **식별** 섹션에서 `app_id`를 확인할 수 있습니다.

### 여러 사용자가 동일한 전화번호를 사용하면 어떻게 되나요? {#what-happens-if-multiple-users-have-the-same-phone-number}

하나의 전화번호(SMS 활성화됨)를 공유하는 여러 사용자 프로필이 인바운드 SMS 이벤트에 의해 트리거되는 액션 기반 Campaign 또는 Canvas 구성요소에 동시에 적격한 경우, Braze는 Canvas 구성요소 수준에서 사용자를 중복 제거합니다. 이를 통해 여러 사용자가 동일한 전화번호를 공유하더라도 Canvas 구성요소당 두 개 이상의 SMS 문자를 수신하지 않습니다.

{% alert note %}
Braze는 스케줄된 Canvases에 대해서는 전화번호 기준으로 중복 제거를 수행하지 않습니다.
{% endalert %}

Braze는 다음 흐름에 따라 수신자 프로필을 결정합니다:
- 가장 최근에 SMS를 수신한 프로필을 확인합니다(최대 7일 전까지). 해당 프로필이 있으면 해당 사용자에게 전송합니다.
- 7일 이내에 SMS를 수신한 프로필이 없으면, 전화번호와 일치하는 "phone" 사용자 별칭이 있는 사용자에게 전송합니다.
- 해당하는 프로필이 없으면, 사용 가능한 프로필 중 무작위로 하나를 선택하여 전송합니다.

공유 전화번호에서 "START" 또는 "STOP" 키워드를 수신하면, 모든 사용자 프로필이 SMS에 가입 및 활성화되거나 구독 취소됩니다. 이는 API 상태 변경에도 적용됩니다. 예를 들어, 서로 다른 외부 ID를 가진 여러 프로필이 동일한 전화번호를 사용하는 경우, API를 통한 구독 그룹 상태 변경은 하나의 외부 ID만 지정하더라도 해당 전화번호를 가진 모든 프로필을 업데이트합니다.

{% alert important %}
사용자를 Canvas에 시차를 두고 진입시키고 각 Canvas 구성요소에 대해 서로 다른 스케줄 시간을 설정하면, 동일한 이메일 또는 전화번호를 가진 사용자에게 중복 메시지가 전송될 수 있습니다.
{% endalert %}

불필요하게 대규모 업데이트를 방지하기 위해, Braze는 구독 업데이트 시 식별자를 공유하는 최대 100개의 사용자 프로필을 업데이트합니다. 100개 이상의 사용자 프로필이 동일한 전화번호를 공유하는 경우, 모든 프로필이 업데이트되지는 않습니다.

### 공유 짧은 코드란 무엇인가요? {#what-are-shared-short-codes}

공유 짧은 코드를 사용하면, 어떤 비즈니스나 조직이 보내든 관계없이 모든 문자 메시지가 소비자의 모바일 기기에 동일한 5~6자리 전화번호로 도착합니다. 공유 짧은 코드는 비교적 저렴하고 즉시 사용할 수 있지만, 비즈니스에 전용 짧은 코드가 없다는 것을 의미합니다.

이 방식의 몇 가지 단점은 다음과 같습니다:

- 고객이 귀하와 짧은 코드를 공유하는 다른 비즈니스의 메시지를 수신 거부하면, 귀하의 메시지도 함께 수신 거부됩니다.
- 하나의 비즈니스가 규칙을 위반하면, 모든 비즈니스의 메시지가 중단됩니다.
- 보안 문제

## 청구 및 가격 {#billing-and-pricing}

### SMS 요금은 어떻게 청구되나요? {#how-will-i-be-billed-for-sms}

짧은 코드 및 긴 코드에 대한 요금 외에도, Braze는 다양한 국가에 대한 SMS 메시지 할당량을 제공합니다. 즉, 귀하와 협력하여 다양한 국가에 대한 특정 수의 메시지 세그먼트를 설정하며, 이를 사용하여 SMS Campaign을 전송합니다. 청구는 국가별로 전송된 메시지 세그먼트 수를 기준으로 이루어집니다. 메시지 세그먼트 계산 방법에 대한 자세한 내용은 [메시지 세그먼트 및 글자 수 제한]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) 가이드를 참조하세요. 계정 매니저가 최대 한도에 가까워지면 관련 보고서를 제공하여 연락드립니다. 초과 요금에 대한 추가 질문은 Braze 담당자에게 문의하세요.

### MMS와 SMS의 가격이 다른가요? {#does-mms-and-sms-pricing-differ}

MMS와 SMS는 비용이 다르며 볼륨에 따라 별도로 청구됩니다. 가격 정보는 Braze 온보딩 팀에 문의하세요.

### 초과 요금을 어떻게 방지할 수 있나요? {#how-can-i-avoid-overages}

가끔 초과가 발생하지 않을 것이라고 보장할 수는 없지만, 할당된 한도를 초과할 가능성을 줄이기 위해 다음 예방 조치를 따를 수 있습니다:

- SMS의 글자 수에 주의하세요. 의도치 않게 두 개 이상의 세그먼트를 전송하면 초과 요금이 발생할 수 있습니다. 자세한 내용은 [세그먼트 분석]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)을 참조하세요.
- Liquid 또는 연결된 콘텐츠를 고려하여 SMS 글자 수를 신중하게 계산하세요. 대시보드의 Braze SMS 작성기는 이러한 기능의 사용량을 추정하거나 반영하지 않습니다.
- 메시지가 사용하는 인코딩 유형을 고려하세요. 메시지가 GSM-7 인코딩을 사용하는 경우, 일반적으로 메시지 세그먼트당 128자로 메시지를 전송할 수 있습니다. 메시지가 [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) 인코딩을 사용하는 경우, 일반적으로 메시지 세그먼트당 67자로 메시지를 전송할 수 있습니다.
- 테스트, 테스트, 또 테스트하세요! 특히 Liquid 및 연결된 콘텐츠를 사용할 때는 항상 시작 전에 SMS 메시지를 테스트하세요.

### 유선 전화로 메시지를 보내면 SMS 전송 횟수에 포함되나요? {#if-a-message-is-sent-to-a-landline-will-the-message-still-count-toward-my-sms-send-count}

미국, 캐나다, 영국의 경우:
- SMS가 유선 전화로 전송되면 **미전달**로 표시됩니다. Twilio는 전달 시도에 대해 여전히 요금을 부과하므로, 메시지 로그에서 **전송됨**, **전달됨** 또는 **미전달**로 표시된 메시지에 대해 요금이 청구됩니다.
- 영국에서는 일부 통신사가 SMS를 음성 메일로 변환하여 메시지를 전달합니다.

기타 국가의 경우:
- Twilio가 오류를 반환하며, 시도된 SMS 메시지에 대해 요금이 청구되지 않습니다.

### 메시지가 160자(GSM-7) 또는 70자(UCS-2) 미만인데 Braze 대시보드에서 추가 메시지 세그먼트에 대해 요금이 부과될 수 있다고 경고하는 이유는 무엇인가요? {#why-is-the-braze-dashboard-warning-me-i-may-be-charged-for-additional-message-segments-when-my-message-is-under-160-gsm-7-or-70-ucs-2-characters}

메시지에 Liquid 개인화가 포함된 경우 추가 메시지 세그먼트에 대해 요금이 부과될 수 있습니다. 콘텐츠 블록 템플릿은 메시지가 전송 준비될 때까지 처리되지 않습니다. 콘텐츠 블록이 포함된 SMS를 편집할 때, Braze는 콘텐츠 블록에 포함될 내용을 알 수 없지만 대략적인 추정치를 제공합니다. 테스트 패널을 사용하여 메시지를 미리보기하여 예상되는 결과를 더 잘 이해하는 것을 권장합니다.

## 전송 및 전달 가능성 {#sending-and-deliverability}

### SMS에 링크를 포함할 수 있나요? {#can-you-include-links-in-an-sms}

원하는 SMS Campaign에 어떤 링크든 포함할 수 있습니다. 그러나 고려해야 할 몇 가지 사항이 있습니다:

- 링크는 SMS의 160자 제한 중 상당 부분을 차지할 수 있습니다. 링크와 텍스트를 포함하면 하나가 아닌 두 개의 SMS 메시지가 될 수 있습니다.
- 기업들은 링크의 글자 수 영향을 줄이기 위해 링크 단축기를 자주 사용합니다. 그러나 긴 코드를 통해 단축 링크를 전송하면, 통신사가 링크 리디렉션을 의심하여 메시지를 차단하거나 거부할 수 있습니다.
- [짧은 코드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)를 사용하는 것이 링크를 포함하기에 가장 안정적인 번호 유형입니다.

Braze에는 링크를 자동으로 단축하고 클릭률 분석을 제공하는 자체 링크 단축 기능도 있습니다. 자세한 내용은 [링크 단축]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening)을 참조하세요.

### SMS 메시지 전송 속도를 제한해야 하나요? {#do-you-need-to-rate-limit-how-fast-you-send-sms-messages}

기본 동시성 속도 및 처리량은 짧은 코드당 시간당 약 360,000개의 메시지를 전송할 수 있습니다. 추가 처리량을 위해서는 추가 짧은 코드가 필요합니다.

### SMS용 URL을 허용 목록에 추가하려면 어떻게 하나요? {#how-do-you-allowlist-urls-for-sms}

특정 국가(예: 스웨덴 또는 북유럽 국가)의 사용자에게 URL이 포함된 SMS 메시지를 보내기 전에, 해당 URL을 통신사에 등록해야 합니다. Braze 고객 서비스 매니저에게 문의하여 도움을 받으세요. 이 과정은 약 5일이 소요됩니다.

### SMS 스팸 감지를 방지하기 위한 모범 전송 사례는 무엇인가요? {#what-are-the-best-sending-practices-to-avoid-spam-detection-for-sms}

1. 옵트인 및 옵트아웃 안내가 명확한지 확인하세요.
2. 귀하(브랜드)가 고객과 관계가 있는지 확인하세요.
3. 콘텐츠가 관계 및 사용자가 수신에 동의한 내용과 관련이 있는지 확인하세요.

스팸 감지 방지에 대한 자세한 가이드라인은 [SMS 법률 및 규정 가이드라인]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)을 참조하세요.

### 이모지는 몇 글자를 사용하나요? {#how-many-characters-does-an-emoji-use}

이모지는 모든 이모지에 걸쳐 표준 글자 수가 없기 때문에 까다로울 수 있습니다. Braze 작성기에서 하나의 메시지로 표시되더라도 이모지가 글자 수 제한을 초과하여 SMS가 여러 메시지로 분할될 위험이 있습니다. 메시지를 테스트할 때 [세그먼트 계산기]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator)를 사용하여 메시지가 분할되는지 더 잘 확인할 수 있습니다.

## 구독 그룹 및 옵트인/옵트아웃 {#subscription-groups-and-opt-inopt-out}

### SMS에 대한 선택적 옵트인 로직을 만들어 사용자가 올바른 구독 그룹에 속하도록 하려면 어떻게 하나요? {#how-do-you-create-logic-for-selective-opt-ins-to-sms-so-users-are-in-the-right-subscription-group}

커스텀 키워드는 커스텀 이벤트로 작성되므로, 고객이 문자로 보낼 수 있는 키워드를 기반으로 Segments를 생성해야 합니다. 예를 들어, 사용자가 VIP 메시지에는 SMS를 옵트인하지만 알림에는 옵트인하지 않은 경우, VIP Segment와 알림 Segment를 생성한 다음 사용자를 적절한 Segment에 할당할 수 있습니다.

### 사용자가 짧은 코드에 "Stop"을 문자로 보내면 구독 그룹에서 구독 취소되나요? {#if-a-user-texts-stop-to-our-short-code-are-they-unsubscribed-from-the-subscription-group}

사용자 프로필에서는 어떻게 표시되나요? 구독 그룹은 2개의 대시(- -)로 되돌아가며, 가입 및 구독 취소에 대한 커스텀 이벤트가 생성됩니다.

### 사용자가 옵트아웃된 상태에서 짧은 코드 및 긴 코드로 키워드를 보내면, Braze에서 해당 키워드에 대해 구성한 응답을 받나요? {#if-a-user-is-opted-out-and-sends-a-keyword-to-our-short-and-long-code-do-they-receive-the-response-we-configured-for-that-keyword-in-braze}

사용자가 옵트아웃된 상태에서 [기본 키워드 카테고리]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout)의 키워드를 보내면, 해당 키워드에 대한 응답을 받습니다. 사용자가 옵트아웃된 상태에서 [커스텀 키워드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling)를 보내면, 해당 키워드에 대한 응답을 받지 않습니다.

### SMS 이벤트 속성은 문장 내의 키워드를 캡처하나요? {#will-sms-event-properties-capture-keywords-in-a-sentence}

문장 내에서 키워드가 인식되려면(예: "please stop texting me"), 특정 단어를 인식하기 위해 메시지에서 Liquid 구문을 사용해야 합니다. 이벤트 속성은 256자의 글자 수 제한이 있으며, 그 외에는 글자 수 제한이 없습니다.

## 테스트 {#testing}

### 테스트 문자 메시지도 한도에 포함되나요? {#do-test-text-messages-count-toward-limits}

네, 포함됩니다. 메시지를 테스트할 때 이 점을 유의하세요.

### SMS 테스트 메시지를 받으려면 사용자가 SMS 구독 그룹에 속해 있어야 하나요? {#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages}

네, 그렇습니다. 사용자는 유효한 전화번호를 가지고 있어야 하며, 테스트 전송에 사용되는 SMS 구독 그룹에 속해 있어야 하고, SMS의 **지역 권한**에서 하나 이상의 국가가 선택되어 있어야 합니다.

### 사용자 프로필에 별칭이 존재하는지 확인할 수 있는 방법이 있나요? {#is-there-a-way-to-see-if-an-alias-exists-on-a-user-profile}

별칭은 사용자 프로필에서 표시되지 않습니다. 별칭이 설정되었는지 확인하려면 [사용자 데이터 내보내기]({{site.baseurl}}/api/endpoints/export) 엔드포인트를 사용해야 합니다.

## MMS

### MMS를 전송할 때 Currents 데이터에 변경 사항이 있나요? {#are-there-any-changes-to-currents-data-when-sending-an-mms}

아니요, MMS 메시지를 전송할 때도 동일한 수준의 인사이트가 제공됩니다.

### MMS의 이미지와 메시지 본문의 전달 순서를 제어할 수 있나요? {#can-i-control-the-order-in-which-the-image-and-message-body-of-an-mms-are-delivered}

Braze는 MMS 메시지에 메시지 본문과 이미지가 모두 포함된 경우 표시 순서를 제어할 수 없습니다. 이는 다음을 포함하되 이에 국한되지 않는 여러 요인에 따라 달라집니다:

- 메시지를 수신하는 통신사
- 메시지를 수신하는 기기
- 메시지의 전체 크기

### MMS에는 별도의 온보딩 프로세스가 필요한가요? {#does-mms-require-a-separate-onboarding-process}

아니요. MMS는 이제 SMS 온보딩 프로세스에 포함되어 있습니다. 이미 온보딩을 완료한 기존 고객은 다음 단계를 완료한 후 MMS Campaign을 전송할 수 있습니다:

1. MMS를 구매합니다.
2. Braze 온보딩 팀에 연락하여 MMS 기능 활성화를 요청합니다. 이렇게 하면 MMS가 활성화되고 SMS/MMS 구독 그룹이 생성되거나 업데이트됩니다.

다음으로, Braze 온보딩 팀이 짧은 코드와 긴 코드가 MMS에 대해 활성화되었는지 확인합니다(미국 및 캐나다). 또한 MMS에 추가되거나 활성화된 현재 번호를 표시하도록 구독 그룹을 업데이트합니다. 이 단계가 완료되면 기본 SMS 작성기에서 바로 MMS 메시지를 전송할 수 있습니다.

### 기능이 활성화되었는데 대시보드에서 MMS를 찾을 수 없는 이유는 무엇인가요? {#why-cant-i-find-mms-on-my-dashboard-even-though-the-feature-is-enabled}

MMS는 구독 그룹이 "MMS 활성화"로 간주될 때만 Braze 대시보드에 표시됩니다. 이는 SMS/MMS 메시지 작성기에서 구독 그룹을 선택할 때 MMS 태그로 반영됩니다. 이는 구독 그룹 내 하나 이상의 번호가 MMS 메시지를 전송할 수 있음을 의미합니다.

또한, 원래 MMS가 활성화되지 않았던 짧은 코드의 활성화를 Twilio가 다시 승인해야 하는 특정 상황이 있습니다. 이 승인 프로세스는 몇 주가 걸릴 수 있습니다.

## RCS

### iOS 기기에서 RCS 메시지가 정확하게 렌더링되지 않는 이유는 무엇인가요? {#why-doesnt-my-rcs-message-render-accurately-on-ios-devices}

RCS 메시지는 운영체제 및 메시징 앱에 따라 iOS 기기에서 다르게 렌더링될 수 있습니다. iOS 기기에서는 다음과 같은 동작이 발생할 수 있습니다:

- 동일한 대화 스레드에 있는 서로 다른 RCS 메시지의 추천 동작이 함께 그룹화되어 잘못된 순서로 표시될 수 있습니다.
- 리치 카드 버튼 및 리치 카드 외부에 있는 추천 동작이 리치 카드 버튼이나 추천 동작을 탭한 후에도 계속 표시될 수 있습니다.

{% alert note %}
Braze는 작성한 RCS 페이로드를 전송하며, 메시징 클라이언트가 추천 동작의 순서, 그룹화 및 숨김을 제어합니다. 전송 전에 리치 카드와 추천 동작 또는 추천 답장을 사용하는 RCS 메시지를 Android 및 iOS 기기 모두에서 테스트하세요.
{% endalert %}

### RCS로 사전 녹음된 음성 메일을 보낼 수 있나요? {#can-i-send-pre-recorded-voicemails-with-rcs}

네, 미디어 메시지를 사용하여 오디오 파일을 지원할 수 있습니다.

### REST API SMS 옵트인이 SMS/MMS/RCS 성과의 **총 옵트인**과 일치하지 않는 이유는 무엇인가요? {#why-do-rest-api-sms-opt-ins-not-match-total-opt-ins-on-smsmmsrcs-performance}

[SMS/MMS/RCS 성과]({{site.baseurl}}/user_guide/analytics/dashboards) 대시보드의 **총 옵트인** 및 **총 옵트아웃**은 인바운드 SMS 키워드 처리에 의해 발생한 구독 변경을 집계합니다(예: 사용자가 짧은 코드로 옵트인 키워드를 문자로 보내는 경우). REST API, 대시보드 또는 기타 소스를 통해 이루어진 모든 구독 업데이트가 포함되는 것은 아닙니다.

소스별 옵트인 및 옵트아웃을 분석하려면 `USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED`에서 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder)를 사용하고 `STATE_CHANGE_SOURCE`(예: **Rest API** 대 **Inbound Message**)로 필터링하세요.