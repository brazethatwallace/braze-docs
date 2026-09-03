---
nav_title: 방향 사용자 정의
article_title: iOS용 인앱 메시지 방향 사용자 정의
platform: iOS
page_order: 3
description: "이 참조 문서에서는 iOS 애플리케이션의 인앱 메시지 방향을 설정하는 방법을 다룹니다."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 방향 사용자 정의 {#customize-orientation}

## 모든 인앱 메시지의 방향 설정하기 {#setting-orientation-for-all-in-app-messages}

모든 인앱 메시지에 고정 방향을 설정하려면 `ABKInAppMessageUIController`에서 `supportedOrientationMask` 속성을 설정하면 됩니다. 앱에서 `startWithApiKey:inApplication:withLaunchOptions:`를 호출한 후 다음 코드를 추가합니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Set fixed in-app message orientation to portrait.
// Use UIInterfaceOrientationMaskLandscape to display in-app messages in landscape
id<ABKInAppMessageUIControlling> inAppMessageUIController = [Appboy sharedInstance].inAppMessageController.inAppMessageUIController;
((ABKInAppMessageUIController *)inAppMessageUIController).supportedOrientationMask = UIInterfaceOrientationMaskPortrait;
```

{% endtab %}
{% tab swift %}

```swift
// Set fixed in-app message orientation to portrait
// Use .landscape to display in-app messages in landscape
if let controller = Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController as? ABKInAppMessageUIController {
  controller.supportedOrientationMask = .portrait
}
```

{% endtab %}
{% endtabs %}

이렇게 하면 기기 방향에 관계없이 모든 인앱 메시지가 지원되는 방향으로 표시됩니다. 메시지가 표시되려면 기기 방향이 인앱 메시지의 `orientation` 속성에서도 지원되어야 합니다.

## 인앱 메시지별 방향 설정 {#setting-orientation-per-in-app-message}

또는 메시지별로 방향을 설정할 수도 있습니다. 이렇게 하려면 [인앱 메시지 델리게이트]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates)를 설정하세요. 그런 다음 `beforeInAppMessageDisplayed:` 델리게이트 메서드에서 `ABKInAppMessage`의 `orientation` 속성을 설정합니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to portrait
inAppMessage.orientation = ABKInAppMessageOrientationPortrait;

// Set inAppMessage orientation to landscape
inAppMessage.orientation = ABKInAppMessageOrientationLandscape;
```

{% endtab %}
{% tab swift %}

```swift
  // Set inAppMessage orientation to portrait
  inAppMessage.orientation = ABKInAppMessageOrientation.portrait

  // Set inAppMessage orientation to landscape
  inAppMessage.orientation = ABKInAppMessageOrientation.landscape
```

{% endtab %}
{% endtabs %}

기기 방향이 인앱 메시지의 `orientation` 속성과 일치하지 않으면 인앱 메시지가 표시되지 않습니다.

{% alert note %}
iPad의 경우 인앱 메시지는 실제 화면 방향과 관계없이 사용자가 선호하는 방향 스타일로 표시됩니다.
{% endalert %}

## 메서드 선언 {#method-declarations}

자세한 내용은 다음 헤더 파일을 참조하세요:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)