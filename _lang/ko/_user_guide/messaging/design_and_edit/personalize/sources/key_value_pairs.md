---
nav_title: 키-값 페어
article_title: 키-값 페어
page_order: 4
description: "이 참조 문서에서는 키-값 페어와 이를 사용하여 사용자 기기에 추가 데이터 페이로드를 전송하는 방법을 다룹니다."
channel:
  - push
  - in-app messages
  - content cards

---

# 키-값 페어 {#key-value-pairs}

> 이 페이지에서는 키-값 페어를 사용하여 사용자 기기에 추가 데이터 페이로드를 전송하는 방법을 다룹니다. 이 기능은 푸시, 인앱, 이메일 및 Content Cards 메시징 채널에서 사용할 수 있습니다.

키-값 페어를 사용하여 메시지에 구조화된 메타데이터를 추가할 수 있습니다. 이러한 추가 데이터 페이로드는 메시지가 렌더링되거나 처리되는 방식에 영향을 줄 수 있는 추가 상황별 정보로 메시지를 풍부하게 만들 수 있습니다.

키-값 페어는 메타데이터이므로 이 데이터가 반드시 수신자에게 표시되는 것은 아니지만, 연결된 시스템이나 프로세스에서 메시지 처리를 커스터마이즈하는 데 사용할 수 있습니다.

각 페어는 다음으로 구성됩니다:

- **키:** 식별자 (예: `utm_source`)
- **값:** 연결된 데이터 (예: `newsletter`)

## 사용 사례 {#use-cases}

키-값 페어를 사용하여 메타데이터를 추가하는 몇 가지 사용 사례는 다음과 같습니다:

1. **추적 매개변수:** 분석 목적으로 UTM 매개변수를 첨부합니다.
   - 키: `utm_campaign`
   - 값: `spring_sale`
2. **커스텀 태그:** 내부 라우팅 또는 분류를 위한 태그를 추가합니다.
   - 키: `priority`
   - 값: `high`
3. **동작 트리거:** 인앱 동작을 트리거하거나 커스터마이징하는 데 사용되는 메타데이터입니다.
   - 키: `deep_link`
   - 값: `app://promo-page`

## 푸시 알림 {#push-notifications}

키-값 페어는 Android, iOS 및 웹 푸시 알림에 추가할 수 있습니다. 키-값 페어를 사용하여 내부 측정기준 및 앱 콘텐츠를 업데이트하거나 알림 우선순위, 현지화, 사운드 등 푸시 알림 속성을 커스텀할 수 있습니다.

메시지 작성기에서 **설정** 탭을 선택하고 **새 페어 추가**를 선택한 다음 키-값 페어를 지정합니다.

메시지 작성기에서 키-값 페어를 추가하면 값이 문자열로 전송됩니다. iOS 푸시의 경우, **알림 옵션**을 통해 추가하는 예약된 Apple Push Notification service(APNs) 알림 키(현지화 인수에 사용되는 `loc-args` 등)는 페이로드에서 올바른 JSON 유형으로 포맷됩니다. 커스텀 키의 경우, 통합에서 파싱하지 않는 한 앱에서 문자열 값을 수신합니다.

### iOS

Apple Push Notification service(APNs)는 키-값 페어를 사용하여 알림 기본 설정을 지정하고 커스텀 데이터를 전송하는 기능을 지원합니다. APNs는 알림 속성을 제어하는 미리 정해진 키와 값을 포함하는 Apple 예약 `aps` 라이브러리를 사용합니다.

#### APS 라이브러리 {#aps-library}

| 키  | 값 유형  | 값 설명 |
|-------------------|-----------------------------|----------------------------------|
| alert             | 문자열 또는 사전 객체 | 문자열 입력의 경우, 해당 문자열을 메시지로 하여 닫기 및 보기 버튼이 있는 알림을 표시합니다. 문자열이 아닌 입력의 경우, 입력의 하위 속성에 따라 알림 또는 배너를 표시합니다. |
| badge             | 숫자                      | 앱 아이콘에 배지로 표시되는 숫자를 제어합니다.                                                                                                                              |
| sound             | 문자열                      | 알림으로 재생할 사운드 파일의 이름. 앱 번들 또는 `Library/Sounds` 폴더에 있어야 합니다.                                                                                    |
| content-available | 숫자                      | 값 1을 입력하면 앱 실행 또는 세션 재개 시 새 정보의 사용 가능 여부를 앱에 알립니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="APS 라이브러리" }


##### 알림 속성 라이브러리 {#alert-properties-library}

| 키            | 값 유형               | 값 설명                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| title         | 문자열                   | Apple Watch에서 알림의 일부로 잠시 표시되는 짧은 문자열                                                                    |
| body         | 문자열                   | 푸시 알림의 콘텐츠                                                                                                                  |
| title-loc-key  | 문자열 또는 null           | `Localizable.strings` 파일에서 현재 현지화의 제목 문자열을 설정하는 키                                          |
| title-loc-args | 문자열 배열 또는 null | title-loc-key의 제목 현지화 형식 지정자 자리에 표시될 수 있는 문자열 값                                           |
| action-loc-key | 문자열 배열 또는 null  | 지정된 경우, 해당 문자열이 닫기 및 보기 버튼의 현지화를 설정합니다.                                                         |
| loc-key        | 문자열 또는 null           | `Localizable.strings` 파일에서 현재 현지화의 알림 메시지를 설정하는 키                                  |
| loc-args       | 문자열 배열         | loc-key의 현지화 형식 지정자 자리에 표시될 수 있는 문자열 값                                                       |
| launch-image   | 문자열                  | 사용자가 실행 버튼을 탭하거나 실행 슬라이드를 이동할 때 시작 이미지로 사용할 앱 번들 내 이미지 파일의 이름 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="알림 속성 라이브러리" }

Braze 메시지 작성기는 **alert** 및 **해당 속성**, **content-available**, **sound**, **category** 키의 생성을 자동으로 처리합니다.

이 값들은 푸시 메시지를 작성할 때 **설정** 탭에서 입력할 수 있습니다. **알림 옵션**을 선택하고 알림 사전 키를 선택하면 새 키-값 항목에 해당 키가 자동으로 채워집니다.

![이 값들은 푸시 메시지를 작성할 때 설정 탭에서 입력할 수 있습니다. 알림 옵션을 선택하고 알림 사전 키를 선택하면 새 키-값 항목에 키가 자동으로 채워집니다.]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
Braze가 APNs에 푸시 알림을 전송하면 페이로드는 JSON으로 포맷됩니다.

**단순 페이로드**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**복잡한 페이로드**

```
{
    "aps" : {
        "alert" : {
            "body" : "Hi, welcome to our app!",
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "content-available" : 1
    },
}
```

{% endraw %}

##### 커스텀 키-값 페어 {#custom-key-value-pairs}

`aps` 라이브러리 페이로드 값 외에도 사용자의 기기에 커스텀 키-값 페어를 전송할 수 있습니다. 이 페어의 값은 사전(객체), 배열, 문자열, 숫자, 불리언 등 기본 유형으로 제한됩니다.

![커스텀 키-값 페어와 관련된 스크린샷.]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

커스텀 키-값 페어의 사용 사례에는 내부 측정기준 관리 및 사용자 인터페이스의 컨텍스트 설정이 포함되지만 이에 국한되지 않습니다. Braze에서는 [extras 키]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=swift#swift_settings)를 통해 애플리케이션에서 사용할 추가 키-값 페어를 푸시 알림과 함께 전송할 수 있습니다. 다른 키를 사용하려면 앱이 해당 커스텀 키를 처리할 수 있는지 확인하세요.

{% alert warning %}
애플리케이션에서 ab라는 최상위 키 또는 사전을 처리하지 않도록 해야 합니다.
{% endalert %}

Apple은 클라이언트에게 커스텀 페이로드 데이터로 고객 정보나 민감한 데이터를 포함하지 않을 것을 권고합니다. 또한 Apple은 알림 메시지와 관련된 모든 작업이 기기에서 데이터를 삭제하지 않을 것을 권장합니다.

{% alert warning %}
HTTP/2 제공자 API를 사용하는 경우, APNs에 전송하는 개별 페이로드는 4096바이트를 초과할 수 없습니다. 곧 지원이 중단될 레거시 바이너리 인터페이스는 2048바이트의 페이로드 크기만 지원합니다.
{% endalert %}

###### API 트리거 Campaigns {#api-triggered-campaigns}

Braze에서는 `extras`라고 하는 커스텀 정의된 문자열 키-값 페어를 전송할 수 있습니다. API 트리거 및 예약된 API 트리거 Campaigns에서 extras에 접근하려면 대시보드에서 키를 "example_key"로 설정하고 값을 {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}로 설정합니다. 이렇게 하면 개발자 콘솔 출력이 `"extras": { "test": { "foo": 1, "bar": 1 }`가 됩니다.

### Android

Braze에서는 키-값 페어를 사용하여 푸시 알림에 추가 데이터 페이로드를 전송할 수 있습니다.

#### 데이터 페이로드 {#data-payload}

iOS 푸시와 유사하게 사용자의 기기에 커스텀 키-값 페어를 전송할 수 있습니다.

커스텀 키-값 페어의 일부 사용 사례에는 내부 측정기준 관리 및 사용자 인터페이스의 컨텍스트 설정이 포함되지만, 원하는 어떤 용도로든 사용할 수 있습니다.

{% alert important %}
데이터 페이로드가 제대로 작동하려면 앱의 백엔드에서 커스텀 키-값 페어를 처리할 수 있어야 합니다.
{% endalert %}

##### API 트리거 Campaigns

Braze에서는 `extras`라고 하는 커스텀 정의된 문자열 키-값 페어를 전송할 수 있습니다. API 트리거 및 예약된 API 트리거 Campaigns에서 extras에 접근하려면 대시보드에서 키를 "example_key"로 설정하고 값을 {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}로 설정합니다. 이렇게 하면 개발자 콘솔 출력이 `"extras": { "test": { "foo": 1, "bar": 1 }`가 됩니다.

##### FCM 메시징 옵션 {#fcm-messaging-options}

Android 푸시 알림은 FCM 메시지 옵션으로 추가 커스텀이 가능합니다. 여기에는 [알림 우선순위]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings), [사운드]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings), 지연, 수명 및 축소 가능성이 포함됩니다. 이 값들은 푸시 메시지를 작성할 때 **설정** 탭에서 지정할 수 있습니다. Braze 메시지 작성기에서 이러한 옵션을 설정하는 방법에 대한 자세한 내용은 [고급 푸시 알림 설정]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings)을 참조하세요.

![FCM 메시징 옵션과 관련된 스크린샷.]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### 자동 푸시 알림 {#silent-push-notifications}

자동 푸시 알림은 알림 메시지나 사운드가 없는 푸시 알림으로, 백그라운드에서 앱의 인터페이스나 콘텐츠를 업데이트하는 데 사용됩니다. 이 알림은 키-값 페어를 사용하여 이러한 백그라운드 앱 작업을 트리거합니다. 자동 푸시 알림은 [제거 추적]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking) 기능도 지원합니다.

마케터는 자동 푸시 알림을 앱 사용자에게 전송하기 전에 예상되는 동작을 트리거하는지 테스트해야 합니다. [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift) 또는 [Android]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android) 자동 푸시 알림을 작성한 후, [외부 사용자 ID]({{site.baseurl}}/api/endpoints/messaging#external-user-id) 또는 [이메일 주소]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)로 필터링하여 테스트 사용자만 타겟팅해야 합니다.

Campaign 실행 시, 테스트 기기에서 눈에 보이는 푸시 알림을 수신하지 않았는지 확인해야 합니다.

{% alert note %}
iOS 자동 알림 게이팅으로 인해 다음과 같은 증상이 발생할 수 있습니다:

- iOS 사용자의 제거 추적 측정기준이 예상보다 낮게 나타남
- 자동 푸시 알림의 전달이 불일치하거나 지연됨
- 표시되지 않는 [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)
- 예상된 이미지, 비디오 또는 페이지 없이 도착하는 Push Stories

이는 Braze 문제가 아니라 Apple 플랫폼 제한 사항입니다. iOS는 제거 추적 및 Push Stories를 포함한 일부 Braze 기능에 대해 백그라운드 알림을 지연시키거나 삭제할 수 있습니다. iOS가 게이팅하는 항목과 시기에 대한 자세한 내용은 [iOS 제한 사항]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift#ios-limitations)을 참조하세요.
{% endalert %}

## 인앱 메시지 {#in-app-messages}

[기존 편집기]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)로 작성하는 인앱 메시지에 키-값 페어를 추가합니다.

1. Campaign 또는 Canvas에서 인앱 메시지를 만들거나 편집하고 기존 편집기(드래그 앤 드롭이 아님)를 선택합니다.
2. 메시지 작성기에서 **설정** 탭을 선택합니다.
3. **키-값 페어**에서 **새 페어 추가**를 선택합니다.
4. 각 페어에 대해 키와 값을 입력합니다. 페어를 추가하려면 **새 페어 추가**를 다시 선택합니다.

{% alert note %}
키-값 페어는 인앱 메시지의 드래그 앤 드롭 편집기에서는 사용할 수 없습니다. 키-값 페어를 추가하려면 기존 편집기를 사용하세요.
{% endalert %}

### API 트리거 Campaigns

Braze에서는 `extras`라고 하는 커스텀 정의 문자열 키-값 페어를 전송할 수 있습니다. API 트리거 및 예약된 API 트리거 Campaigns에서 extras에 액세스하려면, 대시보드에서 키를 "example_key"로 설정하고 값을 {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}로 설정합니다. 그러면 개발자 콘솔에 `"extras": { "test": { "foo": 1, "bar": 1 }`로 출력됩니다.

## 이메일 {#emails}

SparkPost와 SendGrid 모두 이메일에서 키-값 페어를 지원합니다. SendGrid를 사용하는 경우, 키-값 페어는 [고유 인수](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments)로 전송됩니다. SendGrid에서는 최대 10,000바이트의 데이터까지 무제한의 키-값 페어를 첨부할 수 있습니다. 이러한 키-값 페어는 SendGrid [이벤트 웹훅](https://sendgrid.com/docs/for-developers/tracking-events/event/)의 게시물에서 확인할 수 있습니다.

{% alert note %}
반송된 이메일은 SparkPost 또는 SendGrid에 키-값 페어를 전달하지 않습니다.
{% endalert %}

![Braze 이메일 메시지 작성기의 전송 정보 탭]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Content Cards

Content Cards에 키-값 페어를 추가하려면 Braze 메시지 작성기의 **설정** 탭으로 이동하여 **새 페어 추가**를 선택합니다.

![Content Cards에 키-값 페어 추가]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}

{% alert note %}
대조군 배리언트는 키-값 페어를 지원하지 않습니다. A/B 테스트에서 대조군에 대한 분석을 캡처해야 하는 경우, `control=true`와 같은 키-값 페어가 포함된 메시지 배리언트를 생성하고 노출 횟수를 기록하면서 앱 코드에서 숨기세요.
{% endalert %}