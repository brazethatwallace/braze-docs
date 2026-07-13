---
nav_title: 푸시 프라이머 인앱 메시지
article_title: 푸시 프라이머 인앱 메시지
page_order: 1
page_type: reference
description: "이 문서에서는 푸시 프라이머 인앱 메시지의 필수 조건과 설정 방법을 다룹니다."
channel: push

---

# 푸시 프라이머 인앱 메시지 {#push-primer-in-app-messages}

> 사용자에게 푸시 권한을 요청할 기회는 한 번뿐이므로, 푸시 등록을 최적화하는 것이 푸시 메시지의 도달 범위를 극대화하는 데 매우 중요합니다. 인앱 메시지를 사용하여 네이티브 푸시 프롬프트를 표시하기 전에, 사용자가 옵트인할 경우 어떤 유형의 메시지를 받게 되는지 설명하세요. 이를 푸시 프라이머라고 합니다.

![스트리밍 앱의 푸시 프라이머 인앱 메시지. 알림에 "Movie Cannon에서 푸시 알림을 받으시겠습니까? 알림에는 새 영화, TV 프로그램 또는 기타 공지가 포함될 수 있으며 언제든지 끌 수 있습니다."라고 표시됩니다.]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

Braze에서 푸시 프라이머 인앱 메시지를 생성하려면, iOS, Android 또는 웹용 인앱 메시지를 만들 때 버튼 클릭 시 동작으로 "Request Push Permission"을 사용할 수 있습니다.

## 필수 조건 {#prerequisites}

이 기능에는 [버튼 클릭 시 동작](#button-actions)이 필요하며, 다음 최소 버전 이상에서 지원됩니다:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

또한 다음 플랫폼별 세부 사항을 참고하세요:

{% tabs local %}
{% tab android %}
| OS 버전 | 추가 정보 |
|----------|----------------------|
| **Android 12 이하** | 푸시가 기본적으로 옵트인되어 있으므로 푸시 프라이머 구현은 권장되지 않습니다. |
| **Android 13+** | 사용자가 푸시 권한 프롬프트를 두 번 거부하면, Android는 Braze 푸시 프라이머 메시지를 포함한 추가 프롬프트를 차단합니다. 이후 권한을 부여하려면 사용자가 기기 설정에서 앱의 푸시를 수동으로 활성화해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }
{% endtab %}

{% tab swift %}
### 일반 정보 {#general-information}

- 푸시 프롬프트는 설치당 한 번만 표시할 수 있으며, 이는 운영체제에 의해 적용됩니다.
- 앱의 푸시 설정이 명시적으로 켜져 있거나 꺼져 있으면 프롬프트가 표시되지 않습니다. [임시 승인](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375)이 있는 사용자에게만 표시됩니다.
  - **앱의 푸시 설정이 켜져 있는 경우:** 사용자가 이미 옵트인했으므로 Braze는 인앱 메시지를 표시하지 않습니다.
  - **앱의 푸시 설정이 꺼져 있는 경우:** 기기 설정 내 앱의 푸시 알림 설정으로 사용자를 리디렉션해야 합니다.
- **거부 후 재테스트:** 사용자가 네이티브 프롬프트를 거부하면, iOS는 해당 앱 설치에 대해 다시 표시하지 않습니다. 푸시 프라이머 흐름을 재테스트하려면 일반적으로 앱을 삭제하고 다시 설치하거나, **설정**에서 앱의 알림 권한을 변경해야 합니다.

### 수동 코드 제거 {#manual-code-removal}

이 튜토리얼을 사용하여 설정한 인앱 메시지는 사용자가 인앱 메시지 버튼을 클릭할 때 네이티브 푸시 프롬프트 코드를 자동으로 호출합니다. 푸시 알림 권한을 두 번 요청하거나 잘못된 시점에 요청하는 것을 방지하려면, 개발자가 기존에 구현한 푸시 알림 통합을 수정하여 인앱 메시지가 사용자에게 표시되는 첫 번째 푸시 알림 프라이머가 되도록 해야 합니다.

개발팀은 앱 또는 사이트의 푸시 알림 구현을 검토하고 푸시 권한을 요청하는 코드를 수동으로 제거해야 합니다. 예를 들어, 다음 코드에 대한 참조를 제거하세요:

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
requestAuthorizationWithOptions
```
{% endsubtab %}
{% subtab swift %}
```swift
requestAuthorization
```
{% endsubtab %}
{% subtab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endsubtab %}
{% subtab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 1단계: 인앱 메시지 생성 {#step-1-create-an-in-app-message}

먼저 [인앱 메시지를 생성]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)한 다음, 메시지 유형과 레이아웃을 선택합니다.

메시지와 버튼 모두를 위한 충분한 공간을 확보하려면 전체화면 또는 모달 메시지 레이아웃을 사용하세요. 전체화면을 선택하는 경우 이미지가 필수입니다.

## 2단계: 메시지 작성 {#step-2-build-your-message}

이제 문구를 추가할 차례입니다! 푸시 프라이머는 사용자가 푸시 알림을 켜도록 유도하기 위한 것임을 기억하세요. 메시지 본문에서 사용자가 푸시 알림을 켜야 하는 이유를 강조하는 것이 좋습니다. 어떤 유형의 알림을 보낼 것인지, 그리고 어떤 가치를 제공할 수 있는지 구체적으로 설명하세요.

예를 들어, 뉴스 앱은 다음과 같은 푸시 프라이머를 사용할 수 있습니다:

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

스트리밍 앱은 다음과 같이 사용할 수 있습니다:

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

모범 사례 및 추가 리소스는 [커스텀 옵트인 프롬프트 생성]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)을 참조하세요.

## 3단계: 버튼 동작 지정 {#button-actions}

인앱 메시지에 버튼을 추가하려면 두 개의 **Button** 블록을 메시지에 드래그하세요. 이 블록은 인앱 메시지의 기본 버튼과 보조 버튼 역할을 합니다. 또한 행을 메시지에 드래그한 다음 버튼을 행 안에 드래그하여 버튼이 (서로 위아래로 쌓이는 대신) 같은 가로 행에 배치되도록 할 수도 있습니다. 시작 버튼으로 "Allow notifications"와 "Not now"를 권장하지만, 다양한 버튼 프롬프트를 할당할 수 있습니다.

버튼 문구를 추가한 후 각 버튼의 클릭 시 동작을 지정합니다:

- **Button 1:** "Close Message"로 설정합니다. 이것은 보조 버튼, 즉 "Not now" 옵션입니다.
- **Button 2:** "Request Push Permission"으로 설정합니다. 이것은 기본 버튼, 즉 "Allow notifications" 옵션입니다.

![두 개의 버튼이 있는 인앱 메시지 작성기: "Allow notifications"와 "Not now".]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## 4단계: 전달 스케줄 {#step-4-schedule-delivery}

푸시 프라이머가 적절한 시점에 전송되도록 설정하려면, 인앱 메시지를 **Perform Custom Event**를 트리거 동작으로 하는 실행 기반 메시지로 스케줄해야 합니다.

이상적인 시점은 다양하지만, Braze는 사용자가 앱이나 사이트에서 가치를 느끼기 시작했음을 나타내는 일종의 [고가치 행동](https://www.braze.com/resources/videos/mapping-high-value-actions)을 완료한 후, 또는 푸시 알림이 해결할 수 있는 긴급한 필요가 있을 때(예: 주문 후 배송 추적 정보를 제공하려는 경우) 대기하는 것을 권장합니다. 이렇게 하면 프롬프트가 브랜드만을 위한 것이 아니라 고객에게도 유익합니다.

![커스텀 이벤트 "Add to Watch List"를 수행한 사용자에게 전송하는 실행 기반 전달 설정.]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## 5단계: 사용자 타겟팅 {#step-5-target-users}

푸시 프라이머 Campaign의 목표는 아직 푸시 권한을 부여하지 않은 모든 기기의 사용자에게 프롬프트를 표시하는 것입니다. 여기에는 처음 사용하는 사용자 또는 새 기기를 사용하거나 앱을 재설치한 기존 사용자가 포함될 수 있습니다.

{% alert important %}
**노코드 푸시 프라이머를 사용한 자동 억제**: 노코드 푸시 프라이머("Request Push Permission" 버튼 동작)를 사용하는 경우, 세분화에 푸시 구독 필터를 추가할 필요가 없습니다. SDK는 사용자의 다른 기기에서의 푸시 상태와 관계없이, 이미 활성 푸시 토큰이 있는 기기에서 인앱 메시지를 자동으로 억제합니다. 여러 기기를 가진 사용자 타겟팅에 대한 자세한 내용은 [여러 기기를 가진 사용자 타겟팅](#targeting-users-with-multiple-devices)을 참조하세요.
{% endalert %}

노코드 푸시 프라이머를 사용하지 않는 경우, `Foreground Push Enabled For App is false` 필터를 추가하세요. 이 필터는 아직 포그라운드 푸시 알림에 옵트인하지 않은 개별 앱 설치를 식별합니다.

{% alert important %}
`Push Subscription Status is not Opted In`과 같은 사용자 수준 필터를 사용하면, 다른 기기에서 이미 옵트인한 사용자가 제외되어 새 기기에서 프롬프트를 받지 못하게 됩니다.
{% endalert %}

그 외에도 가장 적절하다고 생각되는 추가 Segment를 결정할 수 있습니다. 예를 들어, 두 번째 구매를 완료한 사용자, 회원 가입을 막 한 사용자, 또는 주 2회 이상 앱을 방문하는 사용자를 타겟팅할 수 있습니다. 이러한 핵심 Segment의 사용자를 타겟팅하면 사용자가 옵트인하고 푸시가 활성화될 가능성이 높아집니다.

### 여러 기기를 가진 사용자 타겟팅 {#targeting-users-with-multiple-devices}

Braze는 기기 수준이 아닌 프로필 수준에서 사용자 데이터를 수집하므로, 여러 기기를 소유한 사용자를 타겟팅하는 것은 어려울 수 있습니다. 세분화의 푸시 구독 필터는 특정 타겟 기기의 구독 상태가 아닌 단일 기기의 구독 상태를 기반으로 사용자를 포함하거나 제외합니다. 또한 iOS의 임시 상태는 이러한 기기가 기술적으로 포그라운드 푸시 토큰을 가지고 있지만 사용자가 명시적으로 옵트인하지 않았기 때문에 복잡성을 더합니다.

#### 푸시 구독 필터의 문제점 {#the-problem-with-push-subscription-filters}

사용자가 서로 다른 푸시 구독 상태를 가진 여러 기기를 보유한 경우, 세분화의 푸시 구독 필터가 일부 기기를 타겟팅하지 못할 수 있습니다. 다음 시나리오를 고려하세요:

{% details 시나리오 1: 사용자가 서로 다른 플랫폼의 두 기기를 보유 %}

**사용자가 두 기기를 보유:**
- 기기 A: Android, 푸시 옵트인
- 기기 B: iOS, 푸시 옵트인하지 않음

**작동하지 않는 Segment 필터:**
- `Push enabled = false` - 사용자가 Android 기기에서 푸시가 활성화되어 있으므로 Segment에 포함되지 않습니다. Segment에 iOS 기기가 포함되지 않습니다.
- `Push subscription status is not opted in` - 사용자가 Android 기기에서 푸시가 활성화되어 있으므로 Segment에 포함되지 않습니다. Segment에 iOS 기기가 포함되지 않습니다.

**작동하는 Segment 필터:**
- `Push enabled for iOS = false` - 사용자가 Android 기기에서 푸시가 활성화되어 있지만, iOS 기기만 타겟팅하므로 사용자가 Segment에 포함됩니다. Segment에 iOS 기기가 포함됩니다.

{% enddetails %}

{% details 시나리오 2: 사용자가 서로 다른 상태의 두 iOS 기기를 보유 %}

**사용자가 두 iOS 기기를 보유:**
- 기기 A: 푸시 옵트인
- 기기 B: 임시 활성화되었지만 옵트인하지 않음

**작동하지 않는 Segment 필터:**
- `Push enabled = false` - 기기 A가 푸시에 옵트인되어 있으므로 사용자가 Segment에 포함되지 않습니다. Segment에 기기 B가 포함되지 않습니다.
- `Provisionally opted in = true` - 기기 A가 완전히 옵트인되어 있어 임시 상태가 아닙니다. 사용자가 Segment에 포함되지 않습니다. Segment에 기기 B가 포함되지 않습니다.
- `Push enabled for app > iOS = false` - 기기 A가 iOS에서 푸시에 옵트인되어 있으므로 사용자가 Segment에 포함되지 않습니다. Segment에 기기 B가 포함되지 않습니다.
- `Push subscription status is not opted in` - 기기 A가 푸시에 옵트인되어 있으므로 사용자가 Segment에 포함되지 않습니다. Segment에 기기 B가 포함되지 않습니다.

**결과:** 이러한 푸시 필터의 어떤 조합을 사용하더라도 Segment에서 최소 하나의 기기가 제외됩니다.

{% enddetails %}

{% details 시나리오 3: 사용자가 동일 OS의 세 개 이상 기기를 보유 %}

**사용자가 세 기기를 보유:**
- 기기 A: 푸시 옵트인
- 기기 B: 푸시 옵트인하지 않음
- 기기 C: 푸시 옵트인하지 않음

**작동하지 않는 Segment 필터:**
- `Push enabled = false` - 기기 A가 푸시에 옵트인되어 있으므로 사용자가 Segment에 포함되지 않습니다. Segment에 기기 B와 C가 포함되지 않습니다.
- `Push enabled for app > X = false` - 기기 A가 지정된 앱에서 푸시에 옵트인되어 있으므로 사용자가 Segment에 포함되지 않습니다. Segment에 기기 B와 C가 포함되지 않습니다.
- `Push subscription status is not opted in` - 기기 A가 푸시에 옵트인되어 있으므로 사용자가 Segment에 포함되지 않습니다. Segment에 기기 B와 C가 포함되지 않습니다.

**결과:** 이러한 푸시 필터의 어떤 조합을 사용하더라도 최소 하나의 기기가 타겟팅되지 않습니다.

{% enddetails %}

#### 해결 방법: 노코드 푸시 프라이머 사용 {#solution-use-the-no-code-push-primer}

권장 해결 방법은 추가 푸시 상태 세분화 필터 없이 노코드 푸시 프라이머("Request Push Permission" 버튼 동작)를 사용하는 것입니다.

{% alert important %}
**자동 억제**: 노코드 푸시 프라이머는 이미 활성 푸시 토큰이 있는 기기에서 자동으로 억제됩니다. SDK는 특정 기기에서 사용자가 이미 푸시 토큰을 가지고 있는지 확인합니다. SDK가 사용자가 이미 옵트인했음을 감지하면(예: 이전 요청 또는 기기 설정을 통해), 추가 세분화 필터 없이도 인앱 메시지를 자동으로 억제합니다. 프라이머는 사용자가 임시로 푸시에 옵트인한 경우를 포함하여 다른 모든 시나리오에서 표시됩니다.
{% endalert %}

노코드 푸시 프라이머를 사용하는 이점은 이 기능이 Braze SDK에서 지원된다는 것입니다. SDK가 메시지를 표시하는 특정 기기의 푸시 토큰 상태를 감지할 수 있으므로, 여러 기기를 가진 사용자를 제외할 수 있는 프로필 수준 세분화 필터에 의존할 필요가 없습니다.

#### 고려 사항 {#considerations}

**노코드 푸시 프라이머 필수**: 자동 억제가 작동하려면 노코드 푸시 프라이머를 사용해야 합니다. "Request Push Permission" 버튼 동작 대신 커스텀 로직이나 딥링크를 설정하면, SDK가 푸시 프라이머를 표시하려는 것임을 식별할 수 없습니다. 이 경우 해당 기기의 구독 상태와 관계없이 메시지가 표시됩니다.

**옵트아웃한 사용자에 대한 억제**: 명시적으로 푸시를 옵트아웃한 사용자(예: 네이티브 요청 또는 기기 설정에서)에 대해 인앱 메시지를 억제하고, 해당 사용자를 별도의 육성 Campaign으로 리타겟팅하고 싶을 수 있습니다. 이를 위해 노코드 프라이머와 함께 다음 Liquid 로직을 사용하세요:

{% raw %}
```liquid
{% if targeted_device.${foreground_push_enabled} == false %}
{% abort_message('user turned off push notifications') %}
{% endif %}
- message goes here -
```
{% endraw %}

`targeted_device` Liquid 필터는 사용자 프로필이 아닌 메시지가 표시되는 기기만을 확인합니다. 해당 기기에서 `foreground_push_enabled`는 활성 포그라운드 푸시 토큰이 있을 때 `true`로 설정되고, 운영체제가 푸시 알림이 비활성화되었다고 보고할 때(예: 사용자가 명시적으로 끈 경우) `false`로 설정됩니다. 아직 푸시 권한 상태에 응답하지 않은 완전히 새로운 기기의 경우, `foreground_push_enabled`는 설정되지 않으며 값이 없습니다. Liquid 조건이 {% raw %}`false`{% endraw %}를 구체적으로 확인하므로, 명시적으로 옵트아웃한 기기에서만 프라이머를 억제하고, 이 알 수 없는 상태의 기기는 여전히 자격이 있어 푸시 프라이머를 받을 수 있습니다.

## 6단계: 전환 이벤트 {#step-6-conversion-events}

Braze는 전환에 대한 기본 설정을 제안하지만, 푸시 프라이머와 관련된 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)를 설정할 수도 있습니다.