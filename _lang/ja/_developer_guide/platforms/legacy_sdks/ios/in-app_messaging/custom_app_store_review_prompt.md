---
nav_title: カスタムアプリストアのレビュー依頼
article_title: カスタム App Store レビュープロンプト
platform: iOS
page_order: 4
description: "このリファレンス記事では、iOS App Store のカスタムレビュープロンプトを設定する方法について説明します。"
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# カスタム App Store レビュープロンプト {#custom-app-store-review-prompt}

{% alert note %}
このプロンプトを実装すると、Brazeはインプレッションの自動トラッキングを停止するため、独自の[分析]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/handing_in_app_display/#logging-impressions-and-clicks)を記録する必要があります。
{% endalert %}

アプリ内メッセージの一般的な用途として、ユーザーにApp Storeでのレビューを依頼するキャンペーンの作成があります。

まず、アプリで[アプリ内メッセージのデリゲート](#in-app-message-controller-delegate)を設定します。次に、以下のデリゲートメソッドを実装して、デフォルトのApp Storeレビューメッセージを無効にします。

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

`````````swift
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

ディープリンク処理コードで、以下のコードを追加して `{YOUR-APP-SCHEME}:appstore-review` ディープリンクを処理します。`SKStoreReviewController`を使用するには `StoreKit` をインポートする必要があることに注意してください。

{% tabs %}
{% tab OBJECTIVE-C %}

`````````objc
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

`````````swift
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

次に、以下の内容でアプリ内メッセージングキャンペーンを作成します。

- キーと値のペア `"Appstore Review" : "true"`
- ディープリンク `{YOUR-APP-SCHEME}:appstore-review` を使用して、クリック時の動作を「アプリにディープリンクする」に設定します。

{% endraw %}

{% alert tip %}
Appleは、App Storeのレビュープロンプトをユーザーごとに年間最大3回に制限しているため、キャンペーンの[レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/)をユーザーごとに年間3回に設定する必要があります。<br><br>ユーザーはApp Storeのレビュープロンプトをオフにできます。そのため、カスタムレビュープロンプトでは、App Storeのネイティブレビュープロンプトが表示されることを約束したり、直接レビューを求めたりしないでください。
{% endalert %}