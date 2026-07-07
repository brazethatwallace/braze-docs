---
nav_title: アクションボタン
article_title: iOS 用プッシュアクションボタン
platform: iOS
page_order: 1
description: "この参考記事では、iOS プッシュ通知にアクションボタンを実装する方法について説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# アクションボタン {#push-action-buttons-integration}

Braze iOS SDKは、各プッシュアクションボタンのURL処理サポートなど、デフォルトのプッシュカテゴリーをサポートしています。現在、デフォルトカテゴリーには、`Accept`/`Decline`、`Yes`/`No`、`Confirm`/`Cancel`、および`More`の4セットのプッシュアクションボタンがあります。

![カスタマイズ可能な2つのアクションボタンを表示するためにプルダウンされているプッシュメッセージのGIF。]({% image_buster /assets/img_archive/iOS8Action.gif %})

デフォルトのプッシュカテゴリーを登録するには、統合手順に従ってください。

## ステップ 1:Brazeのデフォルトプッシュカテゴリーの追加 {#step-1-adding-braze-default-push-categories}

以下のコードを使用して、[プッシュ登録]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-4-register-push-tokens-with-braze)時にデフォルトのプッシュカテゴリーに登録します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// For UserNotification.framework (iOS 10+ only)
NSSet *appboyCategories = [ABKPushUtils getAppboyUNNotificationCategorySet];
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:appboyCategories];

// For UIUserNotificationSettings (before iOS 10)
NSSet *appboyCategories = [ABKPushUtils getAppboyUIUserNotificationCategorySet];
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeBadge
                                                                         categories:appboyCategories];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
// For UserNotification.framework (iOS 10+ only)
let appboyCategories = ABKPushUtils.getAppboyUNNotificationCategorySet()
UNUserNotificationCenter.current().setNotificationCategories(appboyCategories)

// For UIUserNotificationSettings (before iOS 10)
let appboyCategories = ABKPushUtils.getAppboyUIUserNotificationCategorySet()
let settings = UIUserNotificationSettings.init(types: .badge, categories: appboyCategories)
UIApplication.shared.registerUserNotificationSettings(settings)
```

{% endtab %}
{% endtabs %}

バックグラウンドアクティベーションモードでプッシュアクションボタンをクリックすると、通知が閉じられるだけで、アプリは開きません。ユーザーが次回アプリを開くと、これらのアクションのボタンクリック分析がサーバーにフラッシュされます。

独自のカスタム通知カテゴリーを作成する場合は、[アクションボタンのカスタマイズ]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons#push-category-customization)を参照してください。

## ステップ 2:インタラクティブなプッシュ処理を有効にする {#step-2-enable-interactive-push-handling}

`UNNotification`フレームワークを使用しており、Brazeの[デリゲート]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling)を実装している場合は、このメソッドがすでに統合されているはずです。

クリック分析やURLルーティングを含むプッシュアクションボタンの処理を有効にするには、アプリの`(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`デリゲートメソッドに次のコードを追加します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                           didReceiveNotificationResponse:response
                               withCompletionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                                didReceive: response,
                                                withCompletionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

UNNotificationフレームワークを使用していない場合は、プッシュアクションボタンの処理を有効にするために、アプリの`application:handleActionWithIdentifier:forRemoteNotification:completionHandler:`に次のコードを追加する必要があります。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] getActionWithIdentifier:identifier
                           forRemoteNotification:userInfo
                               completionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.getActionWithIdentifier(identifier,
                                                 forRemoteNotification: userInfo,,
                                                 completionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

{% alert important %}
`handleActionWithIdentifier`を使用している方は、`UNNotification`フレームワークの使用を開始することを強くお勧めします。[`handleActionWithIdentifier`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc)が非推奨になったため、これをお勧めします。
{% endalert %}

## プッシュカテゴリーのカスタマイズ {#push-category-customization}

Brazeは、[デフォルトのプッシュカテゴリー]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons)のセットを提供するだけでなく、カスタムの通知カテゴリーやアクションもサポートしています。アプリケーションにカテゴリーを登録すると、Brazeダッシュボードを使用して通知カテゴリーをユーザーに送信できます。

`UserNotifications`フレームワークを使用していない場合は、[代替カテゴリー](https://developer.apple.com/documentation/usernotifications/unnotificationcategory)のドキュメントを参照してください。

その後、これらのカテゴリーをダッシュボードからプッシュ通知に割り当てて、デザインのアクションボタン構成をトリガーできます。デバイスに表示される`LIKE_CATEGORY`を活用する例を次に示します。

![「いいねを取り消す」と「いいね」の2つのプッシュアクションボタンを表示するプッシュメッセージ。]({% image_buster /assets/img_archive/push_example_category.png %})