{% multi_lang_include developer_guide/prerequisites/swift.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) 합니다.

{% alert note %}
이 구현 가이드는 Swift 구현을 중심으로 하지만 관심 있는 분을 위해 Objective-C 스니펫도 제공됩니다.
{% endalert %}

## 알림 콘텐츠 앱 확장 {#notification-content-app-extensions}

![나란히 표시된 두 개의 푸시 메시지. 왼쪽 메시지는 기본 UI로 표시되는 푸시의 모습을 보여줍니다. 오른쪽 메시지는 커스텀 푸시 UI를 구현하여 만든 커피 포인트 카드 푸시를 보여줍니다.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

알림 콘텐츠 앱 확장은 푸시 알림 커스터마이즈를 위한 훌륭한 옵션을 제공합니다. 알림 콘텐츠 앱 확장은 푸시 알림이 확장될 때 앱 알림에 대한 커스텀 인터페이스를 표시합니다.

푸시 알림은 세 가지 방법으로 확장할 수 있습니다:
- 푸시 배너를 길게 누르기
- 푸시 배너를 아래로 스와이프하기
- 배너를 가로로 스와이프한 후 "보기"를 선택하기

이러한 커스텀 뷰는 인터랙티브 알림, 사용자 데이터로 채워진 알림, 심지어 전화번호나 이메일과 같은 정보를 캡처할 수 있는 푸시 메시지 등 다양한 유형의 콘텐츠를 표시하여 고객 참여를 유도하는 스마트한 방법을 제공합니다. Braze의 잘 알려진 기능 중 하나인 [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)는 푸시 알림 콘텐츠 앱 확장이 어떤 모습일 수 있는지를 보여주는 대표적인 예입니다!

### 요구 사항 {#requirements}

![Xcode의 '새 타겟용 템플릿 선택' 화면에서 Application Extension 아래의 'Notification Content Extension'이 선택된 모습.]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- 앱에 [푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)이 성공적으로 통합되어 있어야 합니다
- 코딩 언어에 따라 Xcode에서 생성된 다음 파일이 필요합니다:

**SWIFT**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**OBJECTIVE-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## 인터랙티브 푸시 알림 {#interactive-push-notification}

푸시 알림은 콘텐츠 앱 확장 내에서 사용자 동작에 응답할 수 있습니다. iOS 12 이상을 실행하는 사용자의 경우, 푸시 알림을 완전한 인터랙티브 메시지로 전환할 수 있습니다! 이를 통해 프로모션과 애플리케이션에 상호작용성을 도입하는 흥미로운 옵션을 제공합니다. 예를 들어, 푸시 알림에 사용자가 플레이할 수 있는 게임, 할인을 위한 룰렛 휠, 또는 목록이나 노래를 저장하는 "좋아요" 버튼을 포함할 수 있습니다.

다음 예제는 사용자가 확장된 알림 내에서 매칭 게임을 플레이할 수 있는 푸시 알림을 보여줍니다.

![인터랙티브 푸시 알림의 각 단계가 어떻게 보일 수 있는지를 나타낸 다이어그램. 사용자가 푸시 알림을 눌러 인터랙티브 매칭 게임이 표시되는 과정을 보여줍니다.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### 대시보드 설정 {#dashboard-configuration}

인터랙티브 푸시 알림을 만들려면 대시보드에서 커스텀 뷰를 설정해야 합니다.

1. **Campaigns** 페이지에서 **Create Campaign**을 클릭하여 새 푸시 알림 Campaign을 시작합니다.
2. **Compose** 탭에서 **Notification Buttons**를 토글합니다.
3. **iOS Notification Category** 필드에 커스텀 iOS 카테고리를 입력합니다.
4. Notification Content Extension Target의 `.plist`에서 `UNNotificationExtensionCategory` 속성을 커스텀 iOS 카테고리로 설정합니다. 여기에 지정한 값은 Braze 대시보드의 **iOS Notification Category** 아래에 설정된 값과 일치해야 합니다.
5. `UNNotificationExtensionInteractionEnabled` 키를 `true`로 설정하여 푸시 알림에서 사용자 상호작용을 활성화합니다.

![푸시 메시지 작성기 설정에서 찾을 수 있는 알림 버튼 옵션.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![UNNotificationExtensionCategory가 "your_custom_category"로, UNNotificationExtensionDefaultContentHidden이 1로, UNNotificationExtensionInitialContentSizeRatio가 1로 설정된 NSExtension이 포함된 plist.]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## 개인화된 푸시 알림 {#personalized-push-notifications}

![두 대의 iPhone이 나란히 표시되어 있습니다. 첫 번째 iPhone은 푸시 메시지의 축소된 보기를 보여줍니다. 두 번째 iPhone은 푸시 메시지의 확장된 버전으로, 과정 진행률, 다음 세션 이름, 다음 세션 완료 기한을 보여줍니다.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

푸시 알림은 콘텐츠 확장 내에서 사용자별 정보를 표시할 수 있습니다. 이를 통해 다양한 플랫폼에서 진행 상황을 공유하는 옵션 추가, 잠금 해제된 업적 표시, 온보딩 체크리스트 표시 등 사용자 중심의 푸시 콘텐츠를 만들 수 있습니다. 이 예제는 사용자가 Braze 학습 과정에서 특정 작업을 완료한 후 표시되는 푸시 알림을 보여줍니다. 알림을 확장하면 학습 경로의 진행 상황을 확인할 수 있습니다. 여기서 제공되는 정보는 사용자별로 다르며, 세션이 완료되거나 특정 사용자 액션이 수행될 때 API 트리거를 활용하여 발송할 수 있습니다.

### 대시보드 설정

개인화된 푸시 알림을 만들려면 대시보드에서 커스텀 뷰를 설정해야 합니다.

1. **Campaigns** 페이지에서 **Create Campaign**을 클릭하여 새 푸시 알림 Campaign을 시작합니다.
2. **Compose** 탭에서 **Notification Buttons**를 토글하여 켭니다.
3. **iOS Notification Category** 필드에 커스텀 iOS 카테고리를 입력합니다.
4. **Settings** 탭에서 표준 Liquid를 사용하여 키-값 페어를 생성합니다. 메시지에 표시하려는 적절한 사용자 속성을 설정합니다. 이러한 뷰는 특정 고객 프로필의 특정 사용자 속성에 따라 개인화할 수 있습니다.
5. Notification Content Extension Target의 `.plist`에서 `UNNotificationExtensionCategory` 속성을 커스텀 iOS 카테고리로 설정합니다. 여기에 지정하는 값은 Braze 대시보드의 **iOS Notification Category**에서 설정한 값과 일치해야 합니다.

![네 세트의 키-값 페어로, "next_session_name"과 "next_session_complete_date"는 Liquid를 사용하여 API 트리거 속성으로 설정되고, "completed_session count"와 "total_session_count"는 Liquid를 사용하여 커스텀 사용자 속성으로 설정됩니다.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### 키-값 페어 처리 {#handling-key-value-pairs}

`didReceive` 메서드는 알림 콘텐츠 앱 확장이 알림을 수신했을 때 호출됩니다. 이 메서드는 `NotificationViewController` 내에서 찾을 수 있습니다. 대시보드에서 제공된 키-값 페어는 `userInfo` 사전을 통해 코드에서 표현됩니다.

#### 푸시 알림에서 키-값 페어 파싱 {#parsing-key-value-pairs-from-push-notifications}

{% tabs %}
{% tab Swift %}
``` swift
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo

  guard let value = userInfo["YOUR-KEY-VALUE-PAIR"] as? String,
        let otherValue = userInfo["YOUR-OTHER-KEY-VALUE-PAIR"] as? String,
  else { fatalError("Key-Value Pairs are incorrect.")}

  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;

  if (userInfo[@"YOUR-KEY-VALUE-PAIR"] && userInfo[@"YOUR-OTHER-KEY-VALUE-PAIR"]) {

  ...

  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```
{% endtab %}
{% endtabs %}

## 정보 수집 푸시 알림 {#information-capture-push-notification}

푸시 알림은 콘텐츠 앱 확장을 통해 사용자 정보를 수집하여 푸시로 가능한 범위를 넓힐 수 있습니다. 푸시 알림을 통해 사용자 입력을 요청하면 이름이나 이메일과 같은 기본 정보를 요청할 수 있을 뿐만 아니라, 사용자에게 피드백을 제출하거나 미완성된 사용자 프로필을 완성하도록 유도할 수도 있습니다.

{% alert tip %}
자세한 내용은 [푸시 알림 데이터 로깅]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications)을 참조하세요.
{% endalert %}

다음 플로우에서 커스텀 뷰는 상태 변경에 응답할 수 있습니다. 각 이미지에서 해당 상태 변경 구성 요소가 표현됩니다.

1. 사용자가 푸시 알림을 수신합니다.
2. 푸시를 엽니다. 확장된 후 푸시가 사용자에게 정보를 요청합니다. 이 예시에서는 사용자의 이메일 주소를 요청하지만, 어떤 종류의 정보든 요청할 수 있습니다.
3. 정보가 제공되고, 예상 형식에 맞으면 등록 버튼이 표시됩니다.
3. 확인 뷰가 표시되고 푸시가 닫힙니다.


### 대시보드 구성

정보 수집 푸시 알림을 생성하려면 대시보드에서 커스텀 뷰를 설정해야 합니다.

1. **Campaigns** 페이지에서 **Create Campaign**을 클릭하여 새로운 푸시 알림 Campaign을 시작합니다.
2. **Compose** 탭에서 **Notification Buttons**를 토글합니다.
3. **iOS Notification Category** 필드에 커스텀 iOS 카테고리를 입력합니다.
4. **Settings** 탭에서 표준 Liquid를 사용하여 키-값 페어를 생성합니다. 메시지에 표시하려는 적절한 사용자 속성을 설정합니다.
5. Notification Content Extension Target의 `.plist`에서 `UNNotificationExtensionCategory` 속성을 커스텀 iOS 카테고리로 설정합니다. 여기에 지정하는 값은 Braze 대시보드의 **iOS Notification Category** 아래에 설정된 것과 일치해야 합니다.

예시에서 볼 수 있듯이, 푸시 알림에 이미지를 포함할 수도 있습니다. 이를 위해서는 [리치 알림]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift)을 통합하고, Campaign에서 알림 스타일을 리치 알림으로 설정한 다음, 리치 푸시 이미지를 포함해야 합니다.

![세 가지 키-값 페어가 포함된 푸시 메시지. 1. Braze ID를 가져오기 위한 Liquid 호출로 설정된 "Braze_id". 2. "Braze Marketer Certification"으로 설정된 "cert_title". 3. "Certified Braze marketers drive..."로 설정된 "Cert_description".]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### 버튼 동작 처리 {#handling-button-actions}

각 실행 버튼은 고유하게 식별됩니다. 코드는 응답 식별자가 `actionIdentifier`와 같은지 확인하고, 같으면 사용자가 실행 버튼을 클릭했다는 것을 인식합니다.

**푸시 알림 실행 버튼 응답 처리**<br>

{% tabs %}
{% tab Swift %}
``` swift
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  if response.actionIdentifier == "YOUR-REGISTER-IDENTIFIER" {
    // do something
  } else {
    // do something else
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier isEqualToString:@"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }
}
```
{% endtab %}
{% endtabs %}

### 푸시 닫기 {#dismissing-pushes}

푸시 알림은 실행 버튼을 누르면 자동으로 닫을 수 있습니다. 권장하는 세 가지 기본 제공 푸시 닫기 옵션이 있습니다:

1. `completion(.dismiss)` - 알림을 닫습니다
2. `completion(.doNotDismiss)` - 알림이 열린 상태로 유지됩니다
3. `completion(.dismissAndForward)` - 푸시가 닫히고 사용자가 애플리케이션으로 이동합니다