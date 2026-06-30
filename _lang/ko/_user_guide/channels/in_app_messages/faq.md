---
nav_title: FAQ
article_title: 인앱 메시지 FAQ
page_order: 30
description: "이 문서에서는 In-App Messages에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
tool: in-app messages

---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 문서에서는 인앱 메시지에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 인브라우저 메시지란 무엇이며 인앱 메시지와 어떻게 다른가요? {#what-is-an-in-browser-message-and-how-does-it-differ-from-an-in-app-message}

인브라우저 메시지는 웹 브라우저로 전송되는 인앱 메시지입니다. 인브라우저 메시지를 만들려면 인앱 메시지 Campaign 또는 Canvas를 생성할 때 **Send To** 필드에서 **Web Browser**를 선택하세요.

## 기기가 오프라인일 때 인앱 메시지가 표시되나요? {#does-an-in-app-message-display-if-a-device-is-offline}

경우에 따라 다릅니다. 인앱 메시지는 세션 시작 시 전달되므로, 기기가 오프라인 상태가 되기 전에 페이로드를 다운로드할 수 있었다면 오프라인 상태에서도 인앱 메시지가 표시될 수 있습니다. 페이로드가 다운로드되지 않은 경우에는 인앱 메시지가 표시되지 않습니다.

## 사용자의 기기에 이미 인앱 메시지 페이로드가 있고 메시지 만료가 변경된 경우, 기기에서 만료가 업데이트되나요? {#if-a-user-already-has-an-in-app-message-payload-on-their-device-and-the-message-expiration-is-changed-does-the-expiration-update-on-their-device}

사용자가 세션을 시작하면 Braze는 해당 사용자가 수신 자격이 있는 인앱 메시지에 변경 사항이 있는지 확인하고 그에 따라 업데이트합니다. 따라서 만료가 변경되고 사용자가 세션을 기록하면, 인앱 메시지가 업데이트된 정보와 함께 기기로 전송됩니다.

## 인앱 메시지 Campaign에 방해금지 시간을 어떻게 설정하나요? {#how-do-i-set-up-quiet-hours-for-an-in-app-message-campaign}

방해금지 시간 기능은 인앱 메시지 Campaign에서는 사용할 수 없습니다. 이 기능은 특정 시간대에 사용자에게 메시지가 전송되는 것을 방지하는 데 사용됩니다. 인앱 메시지 Campaign의 경우, 사용자가 앱 내에서 활성 상태일 때만 인앱 메시지를 수신합니다.

특정 시간에 인앱 메시지를 전송하기 위한 해결 방법으로 다음 Liquid 코드 샘플을 사용하세요. 이를 통해 지정된 시간대에서 오후 7시 59분 이후 또는 오전 8시 이전에 인앱 메시지가 표시되면 메시지가 중단됩니다.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

## 사용자가 인앱 메시지를 닫은 후 다시 수신할 수 있나요? {#can-users-receive-an-in-app-message-again-after-they-dismiss-it}

### Campaigns

인앱 메시지 Campaign의 경우, **전달 제어**에서 재적격성을 활성화하여(**사용자가 Campaign을 다시 수신할 수 있도록 허용**) 사용자가 Campaign을 다시 수신할 자격을 얻도록 할 수 있습니다. 다시 수신할 수 있는 시기는 설정한 재적격성 기간과 Braze가 이전 발송을 기록한 방식에 따라 달라집니다. Campaign 동작 및 재적격성과 메시지 수신의 관계에 대한 자세한 내용은 [Campaign 및 Canvas 재적격성]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility)을 참조하세요.

재적격성이 꺼져 있으면, 사용자가 Campaign을 수신한 후에는 일반적으로 자격 기준만으로는 동일한 Campaign을 다시 수신하지 않습니다.

### Canvases {#canvases}

Canvas에서 전송된 인앱 메시지의 경우, 사용자가 메시지를 다시 볼 수 있는지 여부는 Campaign 전달 제어뿐만 아니라 Canvas 진입 제어(예: 사용자가 Canvas에 다시 진입할 수 있도록 허용)와 단계 구성에 따라 달라집니다.

## 인앱 메시지의 적격성은 언제 계산되나요? {#when-is-eligibility-for-an-in-app-message-calculated}

인앱 메시지의 적격성은 전달 시점에 계산됩니다. 인앱 메시지가 오전 7시에 발송되도록 스케줄된 경우, 이 인앱 메시지에 대한 적격성은 오전 7시에 확인됩니다.

인앱 메시지가 표시되면, 적격성은 인앱 메시지가 다운로드되고 트리거된 시점에 따라 달라집니다.

## 아카이브된 인앱 메시지 Campaign이 여전히 인앱 메시지 노출 횟수를 전달하는 이유는 무엇인가요? {#why-is-my-archived-in-app-message-campaign-still-delivering-in-app-message-impressions}

이는 인앱 메시지 Campaign이 활성 상태일 때 Segment 기준을 충족한 사용자에게 발생할 수 있습니다.

이를 방지하려면 Campaign 설정 중에 **Re-evaluate campaign eligibility before displaying**을 선택하세요.

## 동일한 세션에서 여러 인앱 메시지가 표시될 수 있나요? {#can-multiple-in-app-messages-display-in-the-same-session}

예, 하지만 [트리거 이벤트]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create#choose-a-trigger) 발생당 하나의 인앱 메시지만 표시될 수 있습니다. 여러 인앱 메시지 Campaign이 동일한 트리거(예: 세션 시작)를 공유하는 경우, 해당 트리거가 발생할 때마다 가장 높은 우선순위의 메시지만 표시됩니다. 세션 시작 트리거의 경우, 세션당 하나의 메시지만 표시될 수 있으며, 다른 적격 메시지를 표시할 다음 기회는 다음 세션입니다.

여러 메시지가 동일한 우선순위 수준을 공유하는 경우, 가장 최근에 생성된 메시지가 먼저 표시됩니다. 세션 시작 트리거의 경우, 다음으로 최근에 생성된 메시지가 후속 세션에서 표시됩니다. 다른 트리거 유형의 경우, 다음으로 최근에 생성된 메시지가 해당 트리거 이벤트가 다음에 발생할 때 표시되며, 이는 동일한 세션 내이거나 이후 세션일 수 있습니다.

우선순위 버킷 내에서 표시 순서를 제어하려면 Campaign의 전달 설정으로 이동하여 **상세 우선순위 지정**을 선택한 다음, Campaign을 원하는 순서로 드래그 앤 드롭하세요. 자세한 내용은 [우선순위 선택]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create#choose-a-priority)을 참조하세요.

## Braze는 "1일 후" 만료로 설정된 인앱 메시지 만료를 어떻게 계산하나요? {#how-does-braze-calculate-an-in-app-message-expiration-set-to-after-1-days}

Braze는 1일의 만료 시간을 사용자가 메시지를 수신할 자격을 얻은 후 24시간으로 계산합니다.

## 템플릿 인앱 메시지란 무엇인가요? {#what-are-templated-in-app-messages}

인앱 메시지는 **Re-evaluate campaign eligibility before displaying**이 선택되었거나 메시지에 다음 Liquid 태그가 존재하는 경우 템플릿 인앱 메시지로 전달됩니다:

- `canvas_entry_properties`
- `connected_content`
- {% raw %}`{sms.${*}}`{% endraw %}와 같은 SMS 변수
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

이는 세션 시작 시 기기가 전체 메시지 대신 해당 인앱 메시지의 트리거를 수신한다는 것을 의미합니다. 사용자가 인앱 메시지를 트리거하면, 사용자의 기기가 실제 메시지를 가져오기 위해 네트워크 요청을 합니다.

{% alert note %}
기기가 인터넷에 접근할 수 없는 경우 메시지가 전달되지 않습니다. Liquid 로직을 해석하는 데 너무 오래 걸리면 메시지가 전달되지 않을 수 있습니다.
{% endalert %}

## 인앱 메시지의 중단 동작은 어떻게 작동하나요? {#how-does-abort-behavior-work-for-in-app-messages}

Braze에서 중단은 사용자가 메시지를 수신할 자격이 되는 동작을 수행했지만, Liquid 로직이 해당 사용자를 부적격으로 표시하여 메시지를 수신하지 못하는 경우에 발생합니다. 예를 들어:

1. Sam이 이메일 Campaign을 트리거해야 하는 동작을 수행합니다.
2. 이메일 본문에는 커스텀 속성 점수가 50 미만이면 이 이메일을 보내지 말라는 Liquid 로직이 포함되어 있습니다.
3. Sam의 커스텀 속성 점수는 20입니다.
4. Braze는 Sam이 이 이메일을 수신해서는 안 된다는 것을 인식하고, 이메일이 중단됩니다.
5. 중단 이벤트가 기록됩니다.

그러나 인앱 메시지는 풀(pull) 채널이므로, 중단이 약간 다르게 작동합니다.

### 표준 인앱 메시지 중단 동작 {#standard-in-app-message-abort-behavior}

인앱 메시지는 세션 시작 시 기기에 의해 풀(pull)되어 기기에 캐시되므로, 인터넷 연결 품질에 관계없이 메시지가 사용자에게 즉시 전달될 수 있습니다. 예를 들어, 사용자가 세션 내에서 5개의 인앱 메시지를 수신하면, 세션 시작 시 5개 모두를 수신합니다. 메시지는 로컬에 캐시되며 정의된 트리거 이벤트(세션 시작, 사용자가 커스텀 이벤트를 기록하는 버튼 클릭 등)가 발생할 때 나타납니다.

즉, 인앱 메시지를 중단해야 하는지 결정하는 로직은 트리거가 발생하기 **전에** 실행됩니다. 이를 설명하기 위해, 이메일 예시의 Sam이 푸시 알림을 구독하고 있다고 가정해 보겠습니다.

1. Sam이 Braze 기반 앱을 실행하여 세션을 시작합니다.
2. 워크스페이스의 활성 Campaign의 오디언스 기준에 따라, Sam은 5개의 서로 다른 Campaign에 적격할 수 있습니다. 5개 모두 Sam의 기기로 풀(pull)되어 캐시됩니다.
3. Sam은 이러한 메시지를 트리거할 동작을 아직 수행하지 **않았지만**, 세션 내에서 해당 메시지를 수신할 수 있습니다.
4. 두 개의 인앱 메시지의 Liquid에는 Sam이 메시지를 수신하지 못하도록 하는 규칙이 있습니다(예: 점수 커스텀 속성이 충분히 높지 않음).
5. Sam은 자신을 제외하는 두 개의 인앱 메시지를 수신하지 않지만, 나머지 세 개의 메시지는 수신합니다.
6. 중단 이벤트는 기록되지 않습니다.

Braze는 Sam의 경우 중단 이벤트를 기록하지 않습니다. 이는 중단의 정의를 충족하지 않기 때문입니다. Sam은 메시지를 트리거할 동작을 수행하지 **않았습니다**. 인앱 메시지의 경우, 사용자는 Braze가 메시지를 표시하지 않아야 한다고 결정하기 전에 실제로 트리거를 수행하지 않습니다.

### 템플릿 인앱 메시지 중단 동작 {#templated-in-app-message-abort-behavior}

[템플릿 인앱 메시지](#what-are-templated-in-app-messages)는 트리거 이벤트가 발생할 때 SDK가 메시지를 표시해야 하는지 재평가하도록 합니다. 이는 다른 중단 동작을 가집니다. 이를 설명하기 위해 다음 예시를 살펴보겠습니다:

1. Sam이 Braze 기반 앱을 실행하여 Braze 세션을 시작합니다.
2. 활성 Campaign의 오디언스 기준에 따르면 Sam은 템플릿 인앱 메시지에 적격할 수 있으므로, 메시지 페이로드 없이 트리거 정보가 기기로 전송됩니다.
3. Sam이 커스텀 이벤트를 기록하는 버튼을 선택하여 템플릿 인앱 메시지를 트리거합니다.
4. Sam의 기기가 인앱 메시지를 가져오기 위해 네트워크 요청을 합니다.
5. 메시지의 Liquid 로직이 중단으로 이어지므로, Braze는 이를 중단으로 기록합니다. Sam이 이 평가 전에 트리거 동작을 수행했기 때문입니다.

### 인앱 메시지 중단 동작 비교 {#comparing-in-app-message-abort-behavior}

이 표는 Sam이 경험한 인앱 메시지 흐름을 비교합니다:

| 인앱 메시지 | 중단 동작 |
| --- | --- |
| 표준 | Sam이 메시지를 트리거할 동작을 수행하지 않았기 때문에 중단 이벤트가 기록되지 않았습니다.<br><br>표준 인앱 메시지는 중단을 기록하지 않습니다. 중단의 정의가 "트리거 동작을 수행했음에도 메시지를 보지 못한 것"이기 때문입니다. 인앱 메시지는 트리거 동작이 발생하기 전에 기기로 전달되므로, Liquid 로직으로 인해 생략된 인앱 메시지를 중단으로 간주하는 것은 적절하지 않습니다. |
| 템플릿 | Sam이 템플릿 인앱 메시지를 트리거하기 위해 트리거 동작을 수행했지만 Liquid 템플릿에서 중단을 수신했기 때문에 중단 이벤트가 기록되었습니다.<br><br>템플릿 인앱 메시지는 Liquid 평가가 트리거 동작이 수행된 후에 발생하기 때문에 중단을 기록합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="인앱 메시지 중단 동작 비교" }

### 인앱 메시지에서 연결된 콘텐츠는 언제 실행되나요? {#when-does-connected-content-run-for-in-app-messages}

[템플릿 인앱 메시지](#what-are-templated-in-app-messages)의 경우, 연결된 콘텐츠 및 기타 Liquid 태그는 트리거 이벤트가 발생하고 기기가 메시지 페이로드를 요청할 때 해석됩니다. 사용자가 메시지 내부의 버튼을 클릭할 때가 아닙니다. 각 템플릿 가져오기에는 해당 표시를 위한 연결된 콘텐츠 호출이 포함될 수 있습니다.

HTML이 연결된 콘텐츠에서 반환된 REST 데이터를 참조하는 경우, 해당 데이터는 메시지가 템플릿된 세션에서 사용할 수 있습니다. 여러 버튼이 클릭 시 추가 호출을 트리거하지 않고 동일한 연결된 콘텐츠 응답을 참조할 수 있습니다.

### 인앱 메시지가 표시되기 전에 지연이 발생하는 이유는 무엇인가요? {#why-is-there-a-delay-before-my-in-app-message-displays}

표준 인앱 메시지는 트리거 이벤트 후 캐시된 페이로드가 준비되는 즉시 표시됩니다. Android 및 iOS에서는 메시지에 참조된 대용량 이미지 또는 기타 CDN 호스팅 자산이 다운로드를 완료하는 동안 인앱 메시지가 나타나기 전에 짧은 지연이 추가될 수 있습니다.

[템플릿 인앱 메시지](#what-are-templated-in-app-messages) 및 **Re-evaluate campaign eligibility before displaying**이 선택된 Campaign은 트리거 후 메시지가 나타나기 전에 추가 네트워크 요청이 필요합니다. 이로 인해 짧은 지연이 추가될 수 있습니다(안정적인 연결에서 일반적으로 100ms 미만). 자세한 내용은 [타겟 사용자 선택]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create#choose-users-to-target)을 참조하세요.

### 인앱 메시지가 대시보드 미리보기와 다르게 보이는 이유는 무엇인가요? {#why-does-my-in-app-message-look-different-from-the-dashboard-preview}

전달된 인앱 메시지는 다음과 같은 경우 대시보드 미리보기와 다를 수 있습니다:

- 통합에서 특정 플랫폼에 커스텀 스타일을 적용하거나 기본 인앱 메시지 UI를 재정의하는 경우
- 미리보기에서 수신자와 다른 속성을 가진 테스트 사용자 프로필을 사용하는 경우
- 템플릿 콘텐츠가 미리보기 모드와 발송 시점에서 다르게 해석되는 경우

외관을 검증할 때는 타겟 오디언스와 일치하는 프로필을 가진 테스트 사용자로 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message)를 사용하세요.

### 다중 페이지 인앱 메시지가 모든 페이지에서 동일한 배경을 사용하는 이유는 무엇인가요? {#why-does-a-multi-page-in-app-message-use-the-same-background-on-every-page}

다중 페이지 인앱 메시지의 한 페이지에서 **배경 이미지**가 활성화되면, 해당 배경이 메시지의 모든 페이지에 적용됩니다. 페이지별로 다른 배경을 사용하려면 JavaScript를 사용하여 페이지 간에 이미지를 전환하는 커스텀 HTML 블록을 사용하세요.

### 웹 인앱 메시지를 어떻게 테스트하나요? {#how-do-i-test-web-in-app-messages}

웹 인앱 메시지 테스트 발송은 테스트 기기에서 푸시가 활성화되어 있어야 합니다. 테스트 플로우가 앱 또는 사이트를 여는 푸시 알림을 전달하고, 그곳에서 인앱 메시지가 표시되기 때문입니다. 동일한 푸시 기반 테스트 경로는 Braze에서 푸시가 구성되지 않은 모든 플랫폼에 적용되지만, 많은 모바일 통합에서는 이미 푸시가 활성화되어 있으므로 웹에서 푸시 누락이 가장 자주 발생합니다. 대신 내부 테스트 Segment에 대한 라이브 Campaign을 사용하세요. 단계는 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message)를 참조하세요.

## Android에서 전체화면 HTML 인앱 메시지의 닫기 버튼이 숨겨지는 이유는 무엇인가요? {#why-is-the-close-button-hidden-on-full-screen-html-in-app-messages-on-android}

엣지 투 엣지 디스플레이가 있는 기기(Android 15 이상 포함)에서는 전체화면 HTML 인앱 메시지가 시스템 상태 표시줄 뒤에 그려져 레이아웃 상단의 닫기 컨트롤이 숨겨질 수 있습니다.

Braze Android SDK 버전 37.0.0 이상에서는 기본적으로 HTML 인앱 메시지에 윈도우 인셋을 적용하여 컨트롤이 안전 영역 내에 유지됩니다. 사용자에게 여전히 겹침이 보이는 경우 최신 Braze Android SDK로 업그레이드하세요.

이전 SDK 버전에서는 이 동작이 기본값이 되기 전에 개발자가 `BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled(true)`를 활성화할 수 있었습니다.

## 드래그 앤 드롭 인앱 메시지를 커스터마이징할 때 알아야 할 사항은 무엇인가요? {#what-should-i-know-when-customizing-drag-and-drop-in-app-messages}

[드래그 앤 드롭 에디터]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)는 모달 및 전체화면 표시 유형을 지원합니다. 이러한 컨테이너 내에서 편집기 블록을 사용하여 콘텐츠를 구축합니다.

다음 사항을 참고하세요:

- **링크 및 딥링크:** 각 클릭 시 동작에는 기본적으로 하나의 URL 필드가 있습니다. URL에 Liquid를 사용하여 기기, 앱 유형 또는 사용자 속성에 따라 링크를 다르게 설정할 수 있습니다. **메시지 컨테이너**에서 플랫폼별 클릭 시 동작을 활성화하여 플랫폼별로 다른 링크를 설정할 수도 있습니다.
- **불투명도 및 배경:** 메시지 컨테이너의 불투명도는 전체 메시지 배경에 영향을 줍니다. 개별 블록은 자체 배경색을 설정할 수 있습니다. 더 세밀한 제어를 위해 커스텀 코드 블록에서 커스텀 CSS를 추가하세요.
- **메시지 너비:** **메시지 컨테이너**의 최대 너비는 에디터에서 325px 미만으로 설정할 수 없으며, 이는 작은 화면에서도 콘텐츠를 읽을 수 있도록 유지합니다. 더 좁은 레이아웃이 필요한 경우 커스텀 CSS를 사용하세요.
- **플랫폼별 배경:** 단일 메시지는 웹과 모바일에서 동일한 배경 이미지와 색상을 사용합니다. 에디터에서 플랫폼별로 다른 배경을 설정할 수 없습니다.
- **다중 페이지 메시지:** 배경 이미지와 메시지 수준 클릭 시 동작은 다중 페이지 메시지의 모든 페이지에 적용됩니다. 각 페이지에서 다른 전체 이미지를 사용하려면 다음 페이지로 연결되는 버튼을 추가하세요.
- **메시지 수준 스타일:** 메시지 수준 스타일은 전체 메시지에 적용됩니다.
- **배경 이미지:** 배경 이미지는 모달에 맞게 늘어납니다.

에디터에 대한 추가 고려 사항은 [인앱 메시지 준비 가이드]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices/prep_guide#drag-and-drop-editor-considerations)를 참조하세요.

## Android SDK 로그에서 "Event was published, but no subscribers were found"는 무엇을 의미하나요? {#what-does-event-was-published-but-no-subscribers-were-found-mean-in-android-sdk-logs}

이 로그 라인은 일반적으로 오류가 아닙니다. Braze가 내부 이벤트(예: `NoMatchingTriggerEvent`)를 게시하고 해당 시점에 인앱 메시지 또는 Content Cards 리스너가 구독되어 있지 않을 때 자주 나타납니다.

커스텀 이벤트가 인앱 메시지를 트리거할 것으로 예상할 때 이 로그가 표시되면, 이벤트가 기록되었는지, 사용자가 Campaign 또는 Canvas 오디언스에 포함되어 있는지, 그리고 메시지가 Content Cards에 의존하는 경우 Content Cards가 동기화되었는지 확인하세요.