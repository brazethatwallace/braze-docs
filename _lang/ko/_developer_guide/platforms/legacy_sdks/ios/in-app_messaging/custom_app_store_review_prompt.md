---
nav_title: 커스텀 앱 스토어 리뷰 프롬프트
article_title: 커스텀 App Store 리뷰 프롬프트
platform: iOS
page_order: 4
description: "이 참조 문서에서는 커스텀 iOS App Store 리뷰 프롬프트를 설정하는 방법을 보여줍니다."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 커스텀 App Store 리뷰 프롬프트 {#custom-app-store-review-prompt}

{% alert note %}
이 프롬프트를 구현하면 Braze는 자동으로 노출 횟수 추적을 중지하며, 직접 [분석]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/handling_in_app_display#logging-impressions-and-clicks)을 기록해야 합니다.
{% endalert %}

사용자에게 App Store 리뷰를 요청하는 Campaign(캠페인)을 생성하는 것은 인앱 메시지의 대표적인 활용 사례입니다.

먼저 앱에서 [인앱 메시지 델리게이트](#in-app-message-controller-delegate)를 설정합니다. 그런 다음, 기본 App Store 리뷰 메시지를 비활성화하기 위해 다음 델리게이트 메서드를 구현합니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  if (inAppMessage.extras != nil && inAppMessage.extras[@"Appstore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:inAppMessage.uri options:@{} completionHandler:nil];
    return ABKDiscardInAppMessage;
  } else {
    return ABKDisplayInAppMessageNow;
  }
}
```

{% endtab %}
{% tab swift %}

```swift
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
  if inAppMessage.extras?["Appstore Review"] != nil && inAppMessage.uri != nil {
    UIApplication.shared.open(inAppMessage.uri!, options: [:], completionHandler: nil)
    return ABKInAppMessageDisplayChoice.discardInAppMessage
  } else {
    return ABKInAppMessageDisplayChoice.displayInAppMessageNow
  }
}
```

{% endtab %}
{% endtabs %}

딥링크 처리 코드에서 `{YOUR-APP-SCHEME}:appstore-review` 딥링크를 처리하기 위해 다음 코드를 추가합니다. `SKStoreReviewController`를 사용하려면 `StoreKit`를 가져와야 합니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:appstore-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:appstore-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

다음으로 아래 내용을 포함하여 인앱 메시징 Campaign을 생성합니다:

- 키-값 페어 `"Appstore Review" : "true"`
- 클릭 시 동작을 "앱으로 딥링크"로 설정하고, 딥링크 `{YOUR-APP-SCHEME}:appstore-review`를 사용합니다.

{% endraw %}

{% alert tip %}
Apple은 사용자당 연간 최대 3회로 App Store 리뷰 프롬프트를 제한하므로, Campaign도 사용자당 연간 3회로 [빈도 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)을 설정해야 합니다.<br><br>사용자는 App Store 리뷰 프롬프트를 끌 수 있습니다. 따라서 커스텀 리뷰 프롬프트는 네이티브 App Store 리뷰 프롬프트가 표시될 것이라고 약속하거나 직접적으로 리뷰를 요청해서는 안 됩니다.
{% endalert %}