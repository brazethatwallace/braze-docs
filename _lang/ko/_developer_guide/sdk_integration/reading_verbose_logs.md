---
page_order: 1.5
nav_title: 상세 로그 읽기
article_title: 상세 로그 읽기
description: "푸시 알림, 인앱 메시지, Content Cards, 딥링크에 대한 주요 항목을 포함하여 Braze SDK의 상세 로그 출력을 읽고 해석하는 방법을 알아봅니다."
---

# 상세 로그 읽기 {#reading-verbose-logs}

> 이 페이지에서는 Braze SDK의 상세 로그 출력을 해석하는 방법을 설명합니다. 각 메시징 채널에 대해 찾아야 할 주요 로그 항목, 그 의미, 주의해야 할 일반적인 문제를 확인할 수 있습니다.

시작하기 전에 [상세 로깅을 활성화]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)했는지, 그리고 플랫폼에서 로그를 수집하는 방법을 알고 있는지 확인하세요.

## 세션 {#sessions}

세션은 Braze 분석 및 메시지 전달의 기초입니다. 인앱 메시지 및 Content Cards를 포함한 많은 메시징 기능은 유효한 세션이 시작되어야 작동할 수 있습니다. 세션이 올바르게 기록되지 않으면 먼저 이를 조사하세요. 세션 추적 활성화에 대한 자세한 내용은 [5단계: 사용자 세션 추적 활성화]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_step-5-enable-user-session-tracking)를 참조하세요.

### 주요 로그 항목 {#key-log-entries}

{% tabs %}
{% tab Swift %}

**세션 시작:**

```
Started user session (id: <SESSION_ID>)
```

**세션 종료:**

```
Ended user session (id: <SESSION_ID>, duration: <DURATION>s)
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: sessionEnd(duration: <DURATION>)
```

{% endtab %}
{% tab Android %}

**세션 시작:**

다음 항목을 찾으세요:

```
New session created with ID: <SESSION_ID>
Session start event for new session received
Completed the openSession call
Opened session with activity: <ACTIVITY_NAME>
```

구성된 Braze 엔드포인트(예: sdk.iad-01.braze.com)에 대한 네트워크 요청을 필터링하여 세션 시작(`ss`) 이벤트를 확인하세요.

**세션 종료:**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### 확인할 사항 {#what-to-check}

- 앱이 시작될 때 세션 시작 로그가 나타나는지 확인하세요.
- 세션 시작이 보이지 않으면 SDK가 올바르게 초기화되었는지, `openSession`(Android)이 호출되고 있는지 확인하세요.
- Android에서 Braze 엔드포인트에 대한 네트워크 요청이 이루어지고 있는지 확인하세요. 보이지 않으면 API 키와 엔드포인트 구성을 확인하세요.

## 푸시 알림 {#push-notifications}

푸시 알림 로그는 기기 토큰이 등록되었는지, 알림이 전달되었는지, 클릭 이벤트가 추적되었는지 확인하는 데 도움이 됩니다.

### 토큰 등록 {#token-registration}

세션이 시작되면 SDK는 기기의 푸시 토큰을 Braze에 등록합니다.

{% tabs %}
{% tab Swift %}

```
Updated push notification authorization:
- authorization: authorized

Received remote notifications device token: <PUSH_TOKEN>
```

구성된 Braze 엔드포인트(예: sdk.iad-01.braze.com)에 대한 요청을 필터링하고 요청 본문 속성에서 `push_token`을 찾으세요:

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

기기 정보에 다음이 포함되어 있는지도 확인하세요:

```
"device": {
  "ios_push_auth": "authorized",
  "remote_notification_enabled": 1
}
```

{% endtab %}
{% tab Android %}

FCM 등록 로그를 찾으세요:

```
Registering for Firebase Cloud Messaging token using sender id: <SENDER_ID>
```

다음을 확인하세요:

- `com_braze_firebase_cloud_messaging_registration_enabled`이 `true`인지 확인합니다.
- FCM 발신자 ID가 Firebase 프로젝트와 일치하는지 확인합니다.

일반적인 오류는 `SENDER_ID_MISMATCH`이며, 이는 구성된 발신자 ID가 Firebase 프로젝트와 일치하지 않음을 의미합니다.

{% endtab %}
{% endtabs %}

### 확인할 사항

- 요청 본문에서 `push_token`이 누락된 경우 토큰이 캡처되지 않은 것입니다. 앱 구성에서 푸시 설정을 확인하세요.
- `ios_push_auth`가 `denied` 또는 `provisional`을 표시하면 사용자가 전체 푸시 권한을 부여하지 않은 것입니다.
- Android에서 `SENDER_ID_MISMATCH`가 보이면 FCM 발신자 ID를 Firebase 프로젝트와 일치하도록 업데이트하세요.

### 푸시 전달 및 클릭 {#push-delivery-and-click}

푸시 알림을 탭하면 SDK가 처리 및 클릭 이벤트를 기록합니다.

{% tabs %}
{% tab Swift %}

```
Processing push notification:
- date: <TIMESTAMP>
- silent: false
- userInfo: {
  "ab": { ... },
  "ab_uri": "<DEEP_LINK_OR_URL>",
  "aps": {
    "alert": {
      "body": "<MESSAGE_BODY>",
      "title": "<MESSAGE_TITLE>"
    }
  }
}
```

이어서 클릭 이벤트가 기록됩니다:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: pushClick(campaignId: ...)
```

푸시에 딥링크가 포함되어 있으면 다음도 볼 수 있습니다:

```
Opening '<URL>':
- channel: notification
- useWebView: false
- isUniversalLink: false
```

{% endtab %}
{% tab Android %}

```
BrazeFirebaseMessagingService: Got Remote Message from FCM
```

이어서 푸시 페이로드 및 표시 로그가 나타납니다. 딥링크의 경우 딥링크 대리자 또는 `UriAction` 항목을 찾으세요.

{% endtab %}
{% endtabs %}

### 확인할 사항

- 푸시 페이로드에 예상되는 `title`, `body` 및 딥링크(`ab_uri`)가 포함되어 있는지 확인하세요.
- 탭한 후 `pushClick` 이벤트가 기록되었는지 확인하세요.
- 클릭 이벤트가 누락된 경우 앱 대리자 또는 알림 핸들러가 푸시 이벤트를 Braze SDK에 올바르게 전달하고 있는지 확인하세요.

## 인앱 메시지 {#in-app-messages}

인앱 메시지 로그는 서버에서의 전달, 이벤트 기반 트리거, 표시, 노출 기록 및 클릭 추적의 전체 생애 주기를 보여줍니다.

### 메시지 전달 {#message-delivery}

사용자가 세션을 시작하고 인앱 메시지 수신 자격이 있을 때 SDK는 서버로부터 메시지 페이로드를 수신합니다.

{% tabs %}
{% tab Swift %}

구성된 Braze 엔드포인트(예: sdk.iad-01.braze.com)에서 인앱 메시지 데이터를 포함하는 응답을 필터링하세요.

응답 본문에는 다음을 포함한 메시지 페이로드가 포함되어 있습니다:

```
"templated_message": {
  "data": {
    "message": "...",
    "type": "HTML",
    "message_close": "SWIPE",
    "trigger_id": "<TRIGGER_ID>"
  },
  "type": "inapp"
}
```

{% endtab %}
{% tab Android %}

일치하는 트리거 이벤트 로그를 찾으세요:

```
Triggering action: <CAMPAIGN_BSON_ID>
```

이는 인앱 메시지가 트리거 이벤트와 일치했음을 확인합니다.

{% endtab %}
{% endtabs %}

### 메시지 표시 및 노출 {#message-display-and-impression}

{% tabs %}
{% tab Swift %}

```
In-app message ready for display:
- triggerId: (campaignId: <CAMPAIGN_ID>, ...)
- extras: { ... }
```

이어서 노출 로그가 나타납니다:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageImpression(triggerIds: [...])
```

{% endtab %}
{% tab Android %}

```
handleExistingInAppMessagesInStackWithDelegate:: Displaying in-app message
```

{% endtab %}
{% endtabs %}

### 클릭 및 버튼 이벤트 {#click-and-button-events}

사용자가 버튼을 탭하거나 메시지를 닫을 때:

{% tabs %}
{% tab Swift %}

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageButtonClick(triggerIds: [...], buttonId: "<BUTTON_ID>")
```

추가로 트리거된 메시지가 일치하지 않으면 다음도 볼 수 있습니다:

```
No matching trigger for event.
```

이것은 해당 이벤트에 대해 추가 인앱 메시지가 구성되지 않았을 때 예상되는 동작입니다.

{% endtab %}
{% tab Android %}

구성된 Braze 엔드포인트(예: sdk.iad-01.braze.com)에 대한 요청을 필터링하고 요청 본문에서 `sbc`(버튼 클릭) 또는 `si`(노출)라는 이름의 이벤트를 찾으세요.

{% endtab %}
{% endtabs %}

### 확인할 사항

- 인앱 메시지가 표시되지 않으면 먼저 세션 시작이 기록되었는지 확인하세요.
- 구성된 Braze 엔드포인트에서 응답을 필터링하여 메시지 페이로드가 전달되었는지 확인하세요.
- 노출 횟수가 기록되지 않으면 로깅을 억제하는 커스텀 `inAppMessageDisplay` 대리자를 구현하지 않았는지 확인하세요.
- "No matching trigger for event"가 나타나면 이는 정상이며, 해당 이벤트에 대해 추가 인앱 메시지가 구성되지 않았음을 나타냅니다.

## Content Cards

Content Cards 로그는 카드가 기기에 동기화되고, 사용자에게 표시되며, 상호작용(노출 횟수, 클릭, 해제)이 추적되고 있는지 확인하는 데 도움이 됩니다.

### 카드 동기화 {#card-sync}

Content Cards는 세션 시작 시 및 수동 새로고침 요청 시 동기화됩니다. 세션이 기록되지 않으면 Content Cards가 표시되지 않습니다.

{% tabs %}
{% tab Swift %}

구성된 Braze 엔드포인트(예: sdk.iad-01.braze.com)에서 카드 데이터를 포함하는 응답을 필터링하세요.

응답 본문에는 다음을 포함한 카드 데이터가 포함되어 있습니다:

```
"cards": [
  {
    "id": "<CARD_ID>",
    "tt": "<CARD_TITLE>",
    "ds": "<CARD_DESCRIPTION>",
    "tp": "short_news",
    "v": 0,
    "cl": 0,
    "p": 1
  }
]
```

주요 필드:
- `v` (조회됨): `0` = 조회되지 않음, `1` = 조회됨
- `cl` (클릭됨): `0` = 클릭되지 않음, `1` = 클릭됨
- `p` (고정됨): `0` = 고정되지 않음, `1` = 고정됨
- `tp` (유형): `short_news`, `captioned_image`, `classic` 등

{% endtab %}
{% tab Android %}

```
Requesting content cards sync.
```

이어서 사용자 및 기기 정보를 포함하는 구성된 Braze 엔드포인트(예: sdk.iad-01.braze.com)에 대한 POST 요청이 나타납니다.

{% endtab %}
{% endtabs %}

### 노출 횟수, 클릭 및 해제 {#impressions-clicks-and-dismissals}

{% tabs %}
{% tab Swift %}

**노출 횟수:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardImpression(cardIds: [...])
```

**클릭:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardClick(cardIds: [...])
```

카드에 URL이 있는 경우 다음도 볼 수 있습니다:

```
Opening '<URL>':
- channel: contentCard
- useWebView: true
```

**해제:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardDismissed(cardIds: [...])
```

{% endtab %}
{% tab Android %}

구성된 Braze 엔드포인트(예: sdk.iad-01.braze.com)에 대한 요청을 필터링하고 요청 본문에서 이벤트 이름을 찾으세요:
- `cci` — Content Cards 노출 횟수
- `ccc` — Content Cards 클릭
- `ccd` — Content Cards 해제됨

{% endtab %}
{% endtabs %}

### 확인할 사항

- **카드가 표시되지 않음**: 세션 시작이 기록되었는지 확인하세요. Content Cards는 동기화를 위해 활성 세션이 필요합니다.
- **새 사용자에게 카드가 누락됨**: 첫 세션의 새 사용자는 다음 세션까지 Content Cards를 보지 못할 수 있습니다. 이는 예상되는 동작입니다.
- **카드가 크기 제한을 초과함**: 2 KB를 초과하는 Content Cards는 표시되지 않으며 메시지가 중단됩니다.
- **Campaign 중지 후 카드가 지속됨**: Campaign이 중지된 후 동기화가 완료되었는지 확인하세요. Content Cards는 성공적인 동기화 후 기기에서 제거됩니다. Campaign을 중지할 때 사용자 피드에서 활성 카드를 제거하는 옵션이 선택되었는지 확인하세요.

## 딥링크 {#deep-links}

딥링크 로그는 푸시 알림, 인앱 메시지, Content Cards에 걸쳐 나타납니다. 로그 구조는 소스 채널에 관계없이 일관됩니다.

{% tabs %}
{% tab Swift %}

SDK가 딥링크를 처리할 때:

```
Opening '<DEEP_LINK_URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: false
- isUniversalLink: false
- extras: { ... }
```

여기서 `<SOURCE_CHANNEL>`은 `notification`, `inAppMessage` 또는 `contentCard` 중 하나입니다.

{% endtab %}
{% tab Android %}

딥링크의 경우 Logcat에서 **Deep Link Delegate** 또는 **UriAction** 항목을 찾으세요. 딥링크 해석을 독립적으로 테스트하려면 다음 명령을 실행하세요:

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

이를 통해 딥링크가 Braze SDK 외부에서 올바르게 해석되는지 확인할 수 있습니다.

{% endtab %}
{% endtabs %}

### 확인할 사항

- 딥링크 URL이 Campaign에서 구성한 내용과 일치하는지 확인하세요.
- 딥링크가 한 채널(예: 푸시)에서는 작동하지만 다른 채널(예: Content Cards)에서는 작동하지 않는 경우, 딥링크 처리 구현이 모든 채널을 지원하는지 확인하세요.
- iOS에서는 유니버설 링크에 추가 처리가 필요합니다. Braze 채널에서 유니버설 링크가 작동하지 않는 경우 앱이 URL 처리를 위해 `BrazeDelegate` 프로토콜을 구현했는지 확인하세요.
- Android에서는 커스텀 핸들러를 사용하는 경우 자동 딥링크 처리가 비활성화되어 있는지 확인하세요. 그렇지 않으면 기본 핸들러가 구현과 충돌할 수 있습니다.

## 사용자 식별 {#user-identification}

사용자가 `external_id`로 식별되면 SDK는 사용자 변경 이벤트를 기록합니다.

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

알아야 할 주요 사항:
- 사용자가 로그인하는 즉시 `changeUser`를 호출하세요. 빠를수록 좋습니다.
- 사용자가 로그아웃하면 `changeUser`를 호출하여 익명 사용자로 되돌릴 수 있는 방법이 없습니다.
- 익명 사용자를 원하지 않는 경우 세션 시작 또는 앱 시작 시 `changeUser`를 호출하세요.

{% endtab %}
{% tab Swift %}

구성된 Braze 엔드포인트(예: sdk.iad-01.braze.com)에 대한 요청을 필터링하고 요청 본문에서 사용자 식별을 찾으세요:

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## 네트워크 요청 {#network-requests}

상세 로그에는 Braze 서버와의 SDK 통신을 위한 전체 HTTP 요청 및 응답 세부 정보가 포함됩니다. 이는 연결 문제를 진단하는 데 유용합니다.

### 요청 구조 {#request-structure}

구성된 Braze 엔드포인트(예: sdk.iad-01.braze.com)에 대한 요청을 필터링하세요. 요청 구조에는 다음이 포함됩니다:

{% tabs %}
{% tab Swift %}

```
[http] request POST: <YOUR_BRAZE_ENDPOINT>
- Headers:
  - Content-Type: application/json
  - X-Braze-Api-Key: <REDACTED>
  - X-Braze-Req-Attempt: 1
  - X-Braze-Req-Tokens-Remaining: <COUNT>
- Body: { ... }
```

{% endtab %}
{% tab Android %}

```
Making request(id = <REQUEST_ID>) to <YOUR_BRAZE_ENDPOINT>
```

{% endtab %}
{% endtabs %}

### 확인할 사항

- **API 키**: `X-Braze-Api-Key`가 워크스페이스의 API 키와 일치하는지 확인하세요.
- **엔드포인트**: 요청 URL이 구성된 SDK 엔드포인트와 일치하는지 확인하세요.
- **재시도 횟수**: `X-Braze-Req-Attempt`가 1보다 크면 SDK가 실패한 요청을 재시도하고 있음을 나타내며, 이는 연결 문제를 의미할 수 있습니다.
- **사용량 제한**: `X-Braze-Req-Tokens-Remaining`은 남은 요청 토큰을 보여줍니다. 낮은 수치는 SDK가 사용량 제한에 접근하고 있음을 나타낼 수 있습니다.
- **누락된 요청**: Android에서 세션 시작 후 Braze 엔드포인트에 대한 요청이 보이지 않으면 API 키 및 엔드포인트 구성을 확인하세요.

## 일반 이벤트 약어 {#common-event-abbreviations}

상세 로그 페이로드에서 Braze는 약어 이벤트 이름을 사용합니다. 다음은 참조 목록입니다:

| 약어 | 이벤트 |
|---|---|
| `ss` | 세션 시작 |
| `se` | 세션 종료 |
| `si` | 인앱 메시지 노출 횟수 |
| `sbc` | 인앱 메시지 버튼 클릭 |
| `cci` | Content Cards 노출 횟수 |
| `ccc` | Content Cards 클릭 |
| `ccd` | Content Cards 해제됨 |
| `lr` | 위치 기록됨 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="일반 이벤트 약어" }

## 문제 해결 {#troubleshooting}

### 사용자 프로필에 세션이 0으로 기록되는 경우는 언제인가요? {#when-might-a-user-have-0-sessions-recorded-against-their-profile}

REST API([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)) 또는 CSV 가져오기를 통해 **첫 번째 세션** 또는 **마지막 세션** 필드 없이 사용자를 가져오면 사용자 프로필에 세션이 0으로 표시될 수 있습니다. 세션은 사용자가 SDK를 통해 앱과 상호작용할 때 기록됩니다. 자세한 내용은 [사용자 프로필에 세션이 0인 경우]({{site.baseurl}}/developer_guide/analytics/tracking_sessions#user-profile-has-0-sessions)를 참조하세요.

### SDK와 REST API를 함께 사용할 때 사용자 데이터 불일치 {#user-data-discrepancies-when-using-the-sdk-and-rest-api-together}

SDK와 REST API를 동시에 사용하면 경합 조건으로 인해 데이터 불일치가 발생할 수 있습니다. `changeUser()`를 호출한 후 중요한 REST API 호출을 하기 전에 SDK가 대기 중인 데이터를 플러시할 수 있도록 하고, 시간에 민감한 업데이트를 일괄 처리하지 않으며, SDK와 API 요청 사이에 짧은 지연을 추가하는 것을 고려하세요. `changeUser()` 동작에 대한 자세한 내용은 [changeUser() 작동 방식]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#how-changeuser-works)을 참조하세요.

### 데이터가 Braze에 도달하지 않는 경우 {#data-not-reaching-braze}

데이터가 Braze에 도달하지 않는 경우 방화벽이 Braze API 엔드포인트 및 CDN 공급자에 대한 아웃바운드 트래픽을 허용하는지 확인하세요. 문제가 발생하는 동안 MTR 테스트를 실행하고 [Fastly Debug](https://www.fastly-debug.com/)를 사용하세요. 허용 목록 및 연결 문제 해결에 대한 자세한 내용은 [API 네트워크 연결 문제]({{site.baseurl}}/api/network_connectivity_issues)를 참조하세요.