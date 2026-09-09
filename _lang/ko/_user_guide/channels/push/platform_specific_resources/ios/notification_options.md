---
nav_title: "알림 옵션"
article_title: iOS 알림 옵션
page_order: 2
page_layout: reference
description: "이 참조 문서에서는 중요 알림, 조용한 알림, 임시 푸시 알림 등 iOS 알림 옵션에 대해 설명합니다."

platform: iOS
channel:
  - push
---

# 알림 옵션 {#notification-options}

> Apple의 iOS 12 출시와 함께 Braze는 [알림 그룹](#notification-groups), [조용한 알림/임시 승인](#provisional-push-authentication--quiet-notifications), [중요 알림](#critical-alerts) 등 여러 기능을 지원합니다.

## 알림 그룹 {#notification-groups}

메시지를 분류하고 사용자의 알림 트레이에서 그룹화하려면 Braze를 통해 iOS의 알림 그룹 기능을 활용할 수 있습니다.

iOS 푸시 Campaign을 생성한 다음, **설정** 탭으로 이동하여 **알림 그룹** 드롭다운을 여세요.

![알림 그룹 드롭다운에서 'Coupons' 값이 선택된 설정 탭.]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

드롭다운에서 알림 그룹을 선택하세요. 알림 그룹 설정에 오류가 발생하거나 드롭다운에서 **None**을 선택한 경우, 메시지는 워크스페이스에 정의된 모든 사용자에게 일반적으로 자동 전송됩니다.

여기에 알림 그룹이 나열되지 않은 경우, iOS Thread ID를 사용하여 추가할 수 있습니다. 추가하려는 각 알림 그룹마다 하나의 iOS Thread ID가 필요합니다. 그런 다음 드롭다운에서 **Manage Notification Groups**를 클릭하고 나타나는 **Manage iOS Push Notification Groups** 창에서 필수 필드를 입력하여 알림 그룹에 추가하세요.

![iOS 푸시 알림 그룹 관리 창.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

iOS 푸시 Campaign을 생성한 다음, 작성기 상단을 확인하세요. **Notification Groups**라는 레이블이 지정된 드롭다운이 표시됩니다.

### 요약 인수 {#summary-arguments}

Thread ID별로 알림을 그룹화하는 것 외에도, Apple에서는 알림이 그룹화될 때 표시되는 요약을 편집할 수 있습니다. Braze 사용자는 푸시 Campaign을 작성할 때 Braze 도구를 사용하여 요약 카테고리, 요약 개수, 요약 인수를 지정할 수 있습니다.

{% alert tip %}
동일한 Thread ID를 가진 알림이 알림 트레이에서 어떻게 그룹화되는지는 OS가 제어합니다. iOS는 최적이라고 판단되는 방식에 따라 동일한 Thread ID를 가진 알림을 개별적으로 또는 그룹으로 표시할 수 있습니다.
{% endalert %}

**푸시 작성기**에서 **Alert Options** 체크박스를 선택하세요.

그런 다음 `summary-arg`와 `summary-arg-count`를 키로 선택하고 해당 열에 값을 입력하세요. `summary-arg`에 값을 설정하지 않으면 기본값 1이 적용됩니다.

### 요약 카테고리 {#summary-categories}

요약 카테고리를 사용하면 알림이 그룹화될 때 표시되는 전체 요약을 커스텀할 수 있습니다. 여러 카테고리를 생성하고 적용할 수 있습니다.

메시지에서 카테고리를 사용하려면, 다음 예시를 참고하여 개발자와 협력하여 구현하세요:

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
이 작업에는 SDK 업데이트가 필요하지 않습니다.
{% endalert %}

{% alert tip %}
`%u`와 `%@`는 각각 요약 개수와 요약 인수에 대한 형식 문자열입니다. 요약이 표시되면, 이 입력 안내가 `summary-count`와 `summary-arg`의 값으로 대체됩니다.
{% endalert %}

앱에서 설정을 완료한 후, **Notification Buttons** 체크박스를 선택하고 **Enter Pre-registered iOS Category**를 선택하여 요약 카테고리를 사용하세요.

그런 다음 앱에서 설정한 요약 카테고리 식별자를 입력하세요.

### 임시 푸시 인증 및 조용한 알림 {#provisional-push}

Apple은 사용자가 공식적으로 명시적 옵트인하기 전에 사용자의 알림 센터에 조용한 푸시 알림을 보낼 수 있는 옵션을 브랜드에 제공하여 메시지의 가치를 일찍 보여줄 기회를 줍니다. 앱에서 [임시 푸시 알림을 설정](#set-up-provisional-push-notifications)하기만 하면, 임시 푸시 토큰을 가진 모든 사용자가 메시지를 수신합니다.

기존 iOS 푸시 토큰과 달리, 임시 푸시 토큰은 "체험 패스"로 작동하여 브랜드가 사용자가 Apple의 기본 푸시 옵트인 안내를 보고 클릭하기 전에 새로운 사용자에게 도달할 수 있게 합니다. 이 기능을 사용하면 푸시 알림이 신규 사용자의 알림 트레이에 직접 전달되며, 향후 알림을 "유지"하거나 "끄기" 옵션이 함께 제공됩니다. "옵트인" 여정을 경험하는 대신, 사용자는 "옵트아웃" 여정에 더 가까운 경험을 하게 됩니다.

{% alert tip %}
임시 인증은 옵트인 비율을 극적으로 높일 수 있는 잠재력이 있지만, 사용자가 메시지에서 가치를 느끼는 경우에만 가능합니다. [사용자 세분화]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), [위치 타겟팅]({{site.baseurl}}/user_guide/audience/locations_and_geofences), [개인화]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) 기능을 활용하여 적절한 사용자가 적절한 시점에 이러한 "체험" 알림을 받을 수 있도록 하세요. 그러면 사용자 경험에 가치를 더한다는 것을 알고 사용자가 푸시 알림에 완전히 옵트인하도록 유도할 수 있습니다.
{% endalert %}

사용자가 어떤 옵션을 선택하든 고객 프로필의 **인게이지먼트** 탭 아래 [연락처 설정]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab)에 적절한 토큰 또는 [구독 상태]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states)가 추가됩니다.

![푸시 구독 상태가 표시된 연락처 설정.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

[세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 사용하여 사용자가 임시 인증되었는지 여부에 따라 사용자를 타겟팅할 수 있습니다.

![사용자를 타겟팅하기 위한 세분화 필터 예시로 'iOS Stopwatch (iOS)에서 임시 인증됨이 참'이 설정된 Segment 세부 정보 패널.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
사용자가 임시 푸시를 "끄기"로 선택하면, 더 이상 임시 푸시 메시지를 받지 않습니다. 이 기능을 사용하여 전송하는 메시지 콘텐츠와 빈도를 신중하게 고려하세요!
{% endalert %}

{% alert important %}
추가 푸시 안내 또는 [인앱 푸시 프라이머](https://www.braze.com/resources/glossary/priming-for-push/)(사용자에게 푸시 알림 옵트인을 권장하는 인앱 메시지)를 사용하는 경우, Braze 담당자에게 추가 안내를 문의하세요.
{% endalert %}

#### 임시 푸시 알림 설정 {#set-up-provisional-push-notifications}

Braze를 사용하면 다음 코드 스니펫을 예시로 참고하여 Braze iOS SDK 구현의 토큰 등록 스니펫에서 코드를 업데이트함으로써 임시 인증에 등록할 수 있습니다(이를 개발자에게 전달하거나 [통합 프로세스 중에 임시 푸시 인증을 구현]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)하도록 하세요).

{% alert warning %}
임시 푸시 인증 구현은 iOS 12 이상만 지원하며, 배포 대상이 그 이전 버전인 경우 오류가 발생합니다. 이에 대한 자세한 내용은 [상세 구현 설명서]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)에서 확인할 수 있습니다.
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**Swift**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

**Objective-C**

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### 중단 수준 (iOS 15 이상) {#interruption-level}

iOS 15의 새로운 집중 모드를 통해 사용자는 앱 알림이 소리나 진동으로 "방해"할 수 있는 시기를 더 잘 제어할 수 있습니다.

![알림이 즉시 전달로 활성화되고 시간에 민감한 알림이 활성화된 iOS 알림 설정 페이지.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

앱은 긴급도에 따라 알림에 포함해야 하는 중단 수준을 지정할 수 있습니다.

iOS 푸시 알림의 중단 수준을 변경하려면, **설정** 탭을 선택하고 **Interruption Level** 드롭다운 메뉴에서 원하는 수준을 선택하세요.

![중단 수준 선택을 위한 드롭다운.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

이 기능은 최소 SDK 버전 요구 사항이 없지만, iOS 15 이상을 실행하는 기기에만 적용됩니다.

사용자가 궁극적으로 집중 모드를 제어한다는 점을 유의하세요. 시간에 민감한 알림이 전달되더라도, 사용자가 어떤 앱이 집중 모드를 방해할 수 없는지 지정할 수 있습니다.

중단 수준과 그 설명은 다음 표를 참조하세요.

| 중단 수준 | 설명 | 사용 시기 | 집중 모드 무시 여부 |
|--|--|--|--|
| [Passive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive) | 소리, 진동 또는 화면 켜기 없이 알림을 전송합니다. | 즉각적인 주의가 필요하지 않은 알림. | 아니요 |
| [Active](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (기본값) | 사용자가 집중 모드를 사용하지 않는 경우에만 소리, 진동을 울리고 화면을 켭니다. | 즉각적인 주의가 필요하지만, 사용자가 집중 모드를 활성화한 경우는 제외되는 알림. | 아니요 |
| [Time Sensitive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive) | 집중 모드 중에도 소리, 진동을 울리고 화면을 켭니다. 이를 위해 Xcode에서 앱에 **Time Sensitive Notifications capability**를 추가해야 합니다. | 라이드쉐어나 배달 알림과 같이 사용자의 집중 모드와 관계없이 방해해야 하는 시기적절한 알림. | 예 |
| [Critical](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical) | 휴대폰의 **방해 금지** 스위치가 활성화되어 있어도 소리, 진동을 울리고 화면을 켭니다. 이를 위해서는 [Apple의 명시적 승인](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/)이 필요합니다. | 심각한 기상 또는 안전 경보와 같은 긴급 상황. | 예 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="중단 수준 (iOS 15 이상)" }

### 관련성 점수 (iOS 15 이상) {#relevance-score}

!['저녁 요약'이라는 제목의 iOS 알림 요약으로 세 개의 알림이 표시되어 있습니다.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15는 또한 하루 종일 지정된 시간에 여러 알림의 다이제스트 그룹을 선택적으로 예약할 수 있는 새로운 방법을 사용자에게 도입했습니다. 이는 즉각적인 주의가 필요하지 않은 알림으로 인한 하루 종일의 지속적인 방해를 방지하기 위한 것입니다.

앱은 **관련성 점수**를 설정하여 어떤 푸시 알림이 가장 관련성이 높은지 지정할 수 있습니다. Apple은 이 점수를 사용하여 예약된 알림 요약에 표시할 알림을 결정하고, 나머지 알림은 사용자가 요약을 클릭할 때 확인할 수 있도록 합니다.

모든 알림은 여전히 사용자의 알림 센터에서 접근할 수 있습니다.

iOS 알림의 관련성 점수를 설정하려면, **설정** 탭에서 `0.0`과 `1.0` 사이의 값을 입력하세요. 예를 들어, 가장 중요한 메시지는 `1.0`으로, 중간 정도 중요도의 메시지는 `0.5`로 전송해야 합니다.

![관련성 점수 '0.5'.]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

이 기능은 최소 SDK 버전 요구 사항이 없지만, iOS 15 이상을 실행하는 기기에만 적용됩니다.

다양한 메시지 유형의 최대 메시지 길이에 대한 자세한 내용은 다음 리소스를 참조하세요:

- [이미지 및 텍스트 사양]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)
- [iOS 글자 수 가이드라인]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications#character-count)