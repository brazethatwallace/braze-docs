## 푸시 구독 상태 {#push-sub-states}

Braze의 "푸시 구독 상태"는 푸시 알림 수신에 대한 **사용자의** 글로벌 선호도를 식별합니다. 구독 상태는 사용자 기반이므로 개별 앱에 한정되지 않습니다. 구독 상태는 푸시 알림을 타겟팅할 사용자를 결정할 때 유용한 플래그가 됩니다.

{% alert note %}
사용자의 푸시 구독 상태는 사용자의 모든 기기를 포함한 전체 고객 프로필에 적용됩니다.
{% endalert %}

다음 구독 상태 옵션이 있습니다: `Subscribed`, `Opted-In`, 및 `Unsubscribed`.

기본적으로 사용자가 푸시를 통해 메시지를 받으려면 푸시 구독 상태가 `Subscribed` 또는 `Opted-In`이어야 하며, 포그라운드 푸시가 활성화되어 있어야 합니다. 메시지를 작성할 때 필요한 경우 이 설정을 재정의할 수 있습니다.

| 옵트인 상태 | 설명 |
|---|---|
| `Subscribed` | Braze에서 고객 프로필을 생성할 때의 기본 푸시 구독 상태입니다. |
| `Opted-In` | 사용자가 푸시 알림 수신을 명시적으로 선호한다고 밝혔습니다. Braze는 사용자가 OS 수준의 푸시 프롬프트를 수락하면 사용자의 옵트인 상태를 자동으로 `Opted-In`으로 변경합니다.<br><br>Android 12 이하 사용자에게는 적용되지 않습니다. |
| `Unsubscribed` | 사용자가 애플리케이션 또는 브랜드가 제공하는 기타 방법을 통해 푸시 수신을 명시적으로 취소한 경우입니다. 기본적으로 Braze 푸시 Campaigns는 푸시에 대해 `Subscribed` 또는 `Opted-in`인 사용자만을 대상으로 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="푸시 구독 상태" }

{% alert important %}
Braze는 사용자의 푸시 구독 상태를 `Unsubscribed`로 자동 변경하지 않습니다. 사용자의 푸시 구독 상태가 `Unsubscribed`인 경우 세분화에서 해당 사용자의 `Foreground Push Enabled` 필터는 `false`임을 기억하세요.
{% endalert %}

### 푸시 등록 및 도달 가능 사용자 {#push-registration-and-reachable-users}

푸시 구독 상태는 사용자의 선호도를 반영하지만, 대시보드에서 푸시에 대해 **도달 가능**으로 집계되는지 여부는 [푸시 등록]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle), 즉 프로필에 유효한 포그라운드 푸시 토큰이 있는지에 따라 달라집니다. Braze가 채널 수준 수치를 계산하는 방법은 [Segment 크기 측정]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size)을 참조하세요.

- **푸시 Campaigns 및 Canvases:** 푸시에 등록되지 않은 사용자는 푸시 구독 상태가 `Subscribed` 또는 `Opted-In`이더라도 오디언스 통계에서 Android 푸시 또는 iOS 푸시의 **도달 가능 사용자**에 포함되지 않습니다.
- **기타 채널:** 동일한 사용자라도 자격을 갖춘 다른 채널(예: 이메일 또는 인앱 메시지)에서는 도달 가능으로 집계될 수 있습니다.
- **Segments:** Segment 멤버십은 필터를 따릅니다. 푸시에 등록되지 않은 사용자도 필터가 제외하지 않는 한(예: **Foreground Push Enabled**) Segment에 남아 있습니다. 전체 Segment 멤버십은 푸시 전용 **도달 가능 사용자** 행에 표시되는 사용자 수의 합보다 클 수 있습니다.

고객 프로필에 푸시 구독 상태가 `Subscribed`로 표시되더라도 푸시 토큰이 할당되지 않은 경우가 있습니다. 이러한 사용자는 Braze가 유효한 토큰을 기록할 때까지 Android 푸시 또는 iOS 푸시의 **도달 가능 사용자**에 집계되지 않습니다.

필터 정의에 대해서는 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 참조하세요.

### 푸시 구독 상태 업데이트하기 {#update-push-subscription-state}

사용자의 푸시 구독 상태를 업데이트하는 다음 방법을 검토하세요:

#### 자동 옵트인(기본값) {#automatic-opt-in-default}

기본적으로 Braze는 사용자가 앱에 대한 푸시 알림을 처음 승인할 때 사용자의 푸시 구독 상태를 `Opted-In`으로 설정합니다. 또한 사용자가 이전에 푸시 권한을 비활성화했다가 시스템 설정에서 다시 활성화하는 경우에도 Braze는 이 작업을 수행합니다.

{% tabs local %}
{% tab android %}
이 기본 동작을 비활성화하려면 Android Studio 프로젝트의 `braze.xml` 파일에 다음 속성을 추가하세요:

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
iOS에서 새로 설치하면 일반적으로 사용자가 알림을 허용할 때까지 푸시 구독 상태가 **`Subscribed`**로 표시됩니다. 사용자가 OS 프롬프트에서 **허용**을 선택하면, 자동 옵트인이 활성화된 경우 Braze가 상태를 **`Opted-In`**으로 설정합니다. 사용자가 **허용 안 함**을 선택한 후 나중에 iOS 설정에서 푸시를 켜면, 설정을 변경하는 시점이 아니라 사용자가 세션을 기록한 후에 상태가 업데이트됩니다.

[Braze Swift SDK 버전 7.5.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0)부터는 Xcode 프로젝트의 `AppDelegate.swift` 파일에 `optInWhenPushAuthorized` 구성을 추가하여 이 동작을 비활성화하거나 추가로 커스텀할 수 있습니다:

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### SDK 통합 {#sdk-integration}

[웹](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) 또는 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:))에서 `setPushNotificationSubscriptionType` 메서드를 사용하여 Braze SDK로 사용자의 구독 상태를 업데이트할 수 있습니다. 예를 들어, 이 메서드를 사용하여 앱에서 사용자가 수동으로 푸시 알림을 활성화하거나 비활성화할 수 있는 설정 페이지를 만들 수 있습니다.

#### REST API

Braze REST API의 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 사용하여 사용자의 [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) 속성을 업데이트함으로써 구독 상태를 변경할 수 있습니다.

### 푸시 활성화와 푸시 구독 상태의 차이 {#differences-between-push-enablement-and-push-subscription-status}

푸시 활성화는 사용자가 특정 기기에서 알림을 수신하기 위해 OS 또는 브라우저 수준의 권한을 부여했는지 여부를 나타냅니다. 푸시 구독 상태는 Braze 수준의 설정으로, 프로필 전체에서 푸시 수신에 대한 사용자의 글로벌 선호도를 나타냅니다.

자동 옵트인이 활성화된 경우(기본값), Braze는 사용자가 앱에 대한 푸시 알림을 승인하거나 시스템 설정에서 권한을 다시 활성화할 때(예: iOS, Android 13+, 지원되는 웹 브라우저) 사용자의 푸시 구독 상태를 `Opted-In`으로 업데이트합니다. 그렇지 않으면 SDK 메서드 또는 REST API 호출을 사용하여 명시적으로 변경할 때까지 사용자의 푸시 구독 상태는 `Subscribed`로 유지됩니다.

Braze는 사용자가 OS, 브라우저 또는 앱 수준에서 알림을 옵트아웃할 때 사용자의 푸시 구독 상태를 `Unsubscribed`로 자동 변경하지 않습니다. 사용자의 푸시 구독 상태를 업데이트하려면 Braze에서 직접 업데이트해야 합니다. 예를 들어, 사용자가 인앱 환경설정 센터에서 푸시를 비활성화하면 Braze에서 푸시 구독 상태를 `Unsubscribed`로 업데이트하세요. Braze는 환경설정 센터를 기반으로 고객 프로필을 자동 업데이트하지 않습니다. 구독 상태를 사용자의 인앱 환경설정과 일치시키려면 SDK(iOS 또는 Android) 또는 REST API를 사용하여 적절한 메서드를 호출하세요. 자세한 내용은 [푸시 구독 상태 업데이트하기]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#update-push-subscription-state)를 참조하세요.

### 가져온 푸시 토큰(iOS) {#imported-push-tokens-ios}

`push_token_import`를 사용하여 [iOS 푸시 토큰을 가져올]({{site.baseurl}}/api/objects_filters/user_attributes_object#push-token-import) 때, 사용자의 푸시 구독 상태는 일반적으로 Braze 통합 앱에서 세션을 기록할 때까지 **`Subscribed`**입니다. 첫 번째 세션 이후, [자동 옵트인](#automatic-opt-in-default)이 적용되는 경우(예: 사용자가 iOS에서 푸시를 승인하고 `optInWhenPushAuthorized`가 활성화된 경우) Braze가 상태를 **`Opted-In`**으로 업데이트할 수 있습니다.

가져오기 후와 사용자의 첫 인앱 세션 이후에 고객 프로필의 **연락처 설정**을 확인하여 예상 상태를 확인하세요.

### 푸시 구독 상태 확인 {#checking-push-subscription-state}

![푸시 구독 상태가 Subscribed로 설정된 John Doe의 고객 프로필.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Braze를 사용하여 사용자의 푸시 구독 상태를 확인할 수 있는 방법은 다음과 같습니다:

* **고객 프로필:** Braze 대시보드의 **[사용자 검색]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)** 페이지에서 개별 고객 프로필에 접근할 수 있습니다. 이메일 주소, 전화번호 또는 외부 사용자 ID를 통해 사용자의 프로필을 찾은 후 **인게이지먼트** 탭을 선택하여 사용자의 구독 상태를 확인하고 수동으로 조정할 수 있습니다.
* **REST API 내보내기:** [Segment별 사용자]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) 또는 [식별자별 사용자]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) 내보내기 엔드포인트를 사용하여 개별 고객 프로필을 JSON 형식으로 내보낼 수 있습니다. Braze는 각 기기에 대한 푸시 활성화 정보를 포함하는 푸시 토큰 오브젝트를 반환합니다.