---
nav_title: JavaScript 브리지
article_title: 랜딩 페이지용 JavaScript 브리지
page_order: 5
page_type: reference
description: "brazeBridge JavaScript 브리지를 사용하여 랜딩 페이지의 커스텀 코드 블록에서 이벤트를 기록하고, 커스텀 속성을 설정하고, Braze 동작을 트리거하는 방법을 알아보세요."
---

# 랜딩 페이지용 JavaScript 브리지 {#javascript-bridge-for-landing-pages}

> 랜딩 페이지는 커스텀 코드(HTML, CSS, JavaScript)를 Braze SDK와 연결하기 위한 JavaScript "브리지"를 지원합니다.

커스텀 코드 블록에서 `brazeBridge`를 사용하여 브리지에 접근하면, 방문자가 랜딩 페이지와 상호작용할 때 이벤트를 기록하고, 커스텀 속성을 설정하고, 사용자를 식별하는 등의 작업을 수행할 수 있습니다.

## 작동 방식 {#how-it-works}

랜딩 페이지에서는 **커스텀 코드** 블록에 커스텀 HTML, CSS, JavaScript를 추가하여 페이지의 외관, 느낌, 동작을 더 세밀하게 제어할 수 있습니다. 커스텀 코드 블록은 [JavaScript 브리지](#supported-methods)를 사용하여 이벤트를 기록하고, 커스텀 속성을 설정하고, 사용자를 식별하는 등의 작업을 수행할 수 있습니다:
- 커스텀 이벤트 및 구매 기록
- 표준 및 커스텀 사용자 속성 설정
- 클릭 및 양식 제출 추적
- 사용자 식별

인앱 메시지 또는 배너에서 사용하던 `brazeBridge` 코드를 재사용하면 랜딩 페이지에서도 실행됩니다. 랜딩 페이지에 적용되지 않는 메서드는 무시되며, 오류를 발생시키는 대신 브라우저 콘솔에 경고를 기록합니다. 자세한 내용은 [랜딩 페이지에서 지원되지 않는 메서드](#methods-not-supported-on-landing-pages)를 참조하세요.

{% alert important %}
랜딩 페이지 브리지는 비동기식이며, 각 메서드는 Promise를 반환합니다. 이는 메서드가 즉시 반환되는 [커스텀 HTML 인앱 메시지 브리지]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge)와 다릅니다. 스크립트의 다음 단계가 브리지 호출 완료에 의존하는 경우(예: 페이지 리디렉션, 양식 제출, Braze로 데이터 전송), `await` 또는 `.then()`을 사용하고 호출이 동기적으로 완료되었다고 가정하지 마세요.
{% endalert %}

## 브리지 사용 가능 여부 {#bridge-availability}

방문자가 랜딩 페이지를 열면 **커스텀 코드** JavaScript에서 `brazeBridge`를 바로 사용할 수 있습니다. 랜딩 페이지에서는 브리지 메서드를 직접 호출하면 됩니다. 인앱 메시지에서 `ab.BridgeReady`를 사용하는 것처럼 별도의 준비 이벤트를 기다릴 필요가 없습니다.

브리지 객체를 사용할 수 있다고 해서 해당 방문자에 대해 Braze SDK가 초기화된 것은 아닙니다. SDK는 다음 두 가지 경우에 랜딩 페이지 방문 시 초기화됩니다:

- 방문자가 Braze 채널(이메일, 단문 메시지 서비스, 푸시 등)을 통해 전송된 [랜딩 페이지 Liquid 태그]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users)를 통해 페이지를 여는 경우. 페이지가 로드될 때 SDK가 자동으로 초기화됩니다.
- 방문자가 페이지의 양식을 제출하는 경우(예: 양식 데이터를 전송하는 **제출** 버튼 클릭). 여기에는 [커스텀 양식 블록]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks)의 `registerFormInput` 콜백 내에서 수행되는 `brazeBridge` 호출도 포함됩니다. 이러한 호출은 양식 제출의 일부로 실행되기 때문입니다.

방문자가 랜딩 페이지 Liquid 태그 없이 랜딩 페이지를 직접 열고 양식을 제출하지 않으면, 해당 페이지는 Braze에 익명으로 처리되며 브리지 메서드 호출은 효과가 없습니다.

{% alert note %}
`window.lpBridge`와 `window.appboyBridge`는 동일한 브리지 객체를 참조하지만, 둘 다 더 이상 사용되지 않습니다. `window.brazeBridge`를 사용하세요.
{% endalert %}

## 예시 {#example}

메서드가 비동기식이므로, 순서나 완료가 중요한 경우 async 핸들러와 `await`를 사용하세요:

```html
<button id="button">Set Favorite Color</button>
<script>
  document.querySelector("#button").onclick = async function () {
    // Track a click for analytics
    await brazeBridge.logClick("set-favorite-color");
    // Set the user's custom attribute
    await brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    await brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    await brazeBridge.requestImmediateDataFlush();
  };
</script>
```

## 지원되는 메서드 {#supported-methods}

다음 `brazeBridge` 메서드는 Promise를 반환하며 랜딩 페이지 **커스텀 코드** 블록에서 지원됩니다. 작업 순서를 지정하거나 완료를 보장해야 할 때 `await`를 사용하거나 `.then()`을 사용하세요.

### 최상위 메서드 {#top-level-methods}

| 메서드 | 설명 |
| --- | --- |
| `brazeBridge.changeUser(userId, signature?)` | 고유 ID로 사용자를 식별합니다. |
| `brazeBridge.logCustomEvent(eventName, eventProperties?)` | 커스텀 이벤트를 기록합니다. |
| `brazeBridge.logPurchase(productId, price, currencyCode?, quantity?, purchaseProperties?)` | 구매를 기록합니다. |
| `brazeBridge.requestImmediateDataFlush(callback?)` | 대기 중인 데이터를 Braze 서버로 플러시합니다. |
| `brazeBridge.logClick(trackingId)` | 지정된 추적 ID에 대한 랜딩 페이지 클릭 이벤트(`lp_c`)를 기록합니다. [클릭 추적](#click-tracking)을 참조하세요. |
| `brazeBridge.logSubmit()` | 랜딩 페이지 양식 제출(`lp_fs`)을 기록합니다. 랜딩 페이지 전용입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="최상위 메서드" }

### `getUser()` 메서드 {#getuser-methods}

{% alert note %}
`brazeBridge.getUser()`는 일반 객체를 동기적으로 반환하므로 `getUser()`에 `await`를 사용할 필요가 없습니다. 반환된 객체의 메서드(예: `getUser().setEmail(email)`)가 Promise를 반환합니다.
{% endalert %}

`getUser()`는 다음 사용자 메서드를 노출하는 객체를 반환합니다. 각 메서드는 Promise를 반환합니다.

| 메서드 | 설명 |
| --- | --- |
| `getUser().setFirstName(firstName)` | 사용자의 이름을 설정합니다. |
| `getUser().setLastName(lastName)` | 사용자의 성을 설정합니다. |
| `getUser().setEmail(email)` | 사용자의 이메일 주소를 설정합니다. |
| `getUser().setPhoneNumber(phoneNumber)` | 사용자의 전화번호를 설정합니다. |
| `getUser().setGender(gender: "m" \| "f" \| "o" \| "u" \| "n" \| "p")` | 사용자의 성별을 설정합니다: 각각 남성, 여성, 기타, 알 수 없음, 해당 없음, 밝히고 싶지 않음입니다. |
| `getUser().setDateOfBirth(year, month, day)` | 사용자의 생년월일을 설정합니다. |
| `getUser().setCountry(country)` | 사용자의 국가를 설정합니다. |
| `getUser().setHomeCity(city)` | 사용자의 거주 도시를 설정합니다. |
| `getUser().setLanguage(language)` | 사용자의 언어를 설정합니다. |
| `getUser().setCustomUserAttribute(key, value, merge?)` | 커스텀 사용자 속성을 설정합니다. |
| `getUser().addToCustomAttributeArray(key, value)` | 커스텀 속성 배열에 값을 추가합니다. |
| `getUser().removeFromCustomAttributeArray(key, value)` | 커스텀 속성 배열에서 값을 제거합니다. |
| `getUser().incrementCustomUserAttribute(key, incrementValue?)` | 숫자형 커스텀 속성을 증가시킵니다. |
| `getUser().setCustomLocationAttribute(key, latitude, longitude)` | 커스텀 위치 속성을 설정합니다. |
| `getUser().addToSubscriptionGroup(subscriptionGroupId)` | 사용자를 이메일 또는 단문 메시지 서비스 구독 그룹에 추가합니다. |
| `getUser().removeFromSubscriptionGroup(subscriptionGroupId)` | 사용자를 이메일 또는 단문 메시지 서비스 구독 그룹에서 제거합니다. |
| `getUser().setEmailNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | 이메일 알림 구독 상태를 설정합니다. |
| `getUser().setPushNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | 푸시 알림 구독 상태를 설정합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="getUser() 메서드" }

## 클릭 추적 {#click-tracking}

`brazeBridge.logClick(trackingId)`를 사용하여 랜딩 페이지에서 클릭을 추적합니다. 각 호출은 전달한 추적 ID로 태그된 랜딩 페이지 클릭 이벤트(`lp_c`)를 기록합니다:

```html
<a href="#" onclick="brazeBridge.logClick('cta-hero')">Get started</a>
```

{% alert note %}
랜딩 페이지 클릭 추적은 인앱 메시지와 다릅니다. 인앱 메시지에서는 "버튼 1"과 "버튼 2"의 관례적 ID로 `logClick('0')`과 `logClick('1')`을 사용합니다. 랜딩 페이지에는 이에 해당하는 특수 버튼 ID가 없습니다. 모든 `logClick(trackingId)` 호출은 사용자가 제공한 추적 ID로 키가 지정된 `lp_c` 이벤트를 기록합니다.
{% endalert %}

## 랜딩 페이지에서 지원되지 않는 메서드 {#methods-not-supported-on-landing-pages}

다음 메서드는 인앱 메시지와 배너에서는 작동하지만 랜딩 페이지에서는 지원되지 않습니다. 랜딩 페이지에서 이러한 메서드를 호출하면 Braze가 해당 호출을 무시합니다. 페이지는 계속 작동하지만, 브라우저의 개발자 콘솔에 경고가 표시될 수 있습니다.

| 메서드 | 참고 |
| --- | --- |
| `brazeBridge.closeMessage()` | 랜딩 페이지에는 닫을 메시지 UI가 없습니다. |
| `brazeBridge.requestPushPermission(successCallback?, deniedCallback?)` | 랜딩 페이지에서는 푸시 권한을 요청하지 않습니다. |
| `brazeBridge.web.registerAppboyPushMessages(successCallback?, deniedCallback?)` | 랜딩 페이지에서는 웹 푸시 등록을 사용할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="랜딩 페이지에서 지원되지 않는 메서드" }

## 관련 콘텐츠 {#related-content}

- [커스텀 양식 블록 만들기]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks)에서는 이 브리지의 고급 사용법인 완전한 커스텀 UI를 랜딩 페이지 양식에 연결하는 방법을 다룹니다.
- [랜딩 페이지 만들기]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)