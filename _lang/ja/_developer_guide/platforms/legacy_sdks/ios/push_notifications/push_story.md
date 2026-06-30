---
nav_title: プッシュ通知ストーリー
article_title: iOS版 Push Stories
platform: iOS
page_order: 27
description: "この参照記事では、iOSアプリケーション向けにPush Storiesを設定する方法を紹介しています。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Push Storyのセットアップ {#push-story-setup}

Push Story機能を使用するには、`UNNotification` フレームワークとiOS 10が必要です。この機能はiOS SDKバージョン3.2.1以降でのみ利用可能です。

## ステップ 1:アプリでプッシュを有効にする {#step-1-enable-push-in-your-app}

[プッシュ通知統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)に従って、アプリでプッシュを有効にします。

## ステップ 2:通知コンテンツ拡張ターゲットを追加する {#step-2-adding-the-notification-content-extension-target}

アプリプロジェクトで、メニュー **[File] > [New] > [Target...]** を選択し、新しい `Notification Content Extension` ターゲットを追加してアクティブ化します。

![アプリプロジェクトで、メニューの「File」>「New」>「Target...」を選択し、新しい Notification Content Extension ターゲットを追加してアクティブ化します。]({% image_buster /assets/img/ios/push_story/add_content_extension.png %})

Xcodeによって新しいターゲットが生成され、次のようなファイルが自動的に作成されます。

{% tabs %}
{% tab OBJECTIVE-C %}

- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

{% endtab %}
{% tab swift %}

- `NotificationViewController.swift`
- `MainInterface.storyboard`

{% endtab %}
{% endtabs %}

## ステップ 3:機能を有効にする {#step-3-enable-capabilities}

Push Story機能では、メインアプリターゲットの **[Capabilities]** セクションのバックグラウンドモードが必要です。バックグラウンドモードをオンにしたら、**[Background fetch]** と **[Remote notifications]** を選択します。

![Push Story機能では、メインアプリターゲットの「Capabilities」セクションのバックグラウンドモードが必要です。バックグラウンドモードをオンにしたら、「Background fetch」と「Remote notifications」を選択します。]({% image_buster /assets/img/ios/push_story/enable_background_mode.png %})

### アプリグループの追加 {#adding-an-app-group}

`Capability App Groups` も追加する必要があります。アプリにアプリグループがない場合は、メインアプリターゲットの **[Capability]** に移動し、`App Groups` をオンにして **[+]** ボタンをクリックします。アプリのバンドルIDを使用してアプリグループを作成します。たとえば、アプリのバンドルIDが `com.company.appname` の場合、アプリグループに `group.com.company.appname.xyz` という名前を付けることができます。メインアプリとコンテンツ拡張ターゲットの両方で `App Groups` をオンにする必要があります。

{% alert important %}
この場合の `App Groups` は、Appleの[App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups)を指し、Brazeワークスペース（以前のアプリグループ）のIDではありません。
{% endalert %}

アプリをアプリグループに追加しないと、アプリがプッシュペイロードからの特定のフィールドの入力に失敗し、期待したとおりに完全に動作しない可能性があります。

## ステップ 4:Push Storyフレームワークをアプリに追加する {#step-4-adding-the-push-story-framework-to-your-app}

{% tabs local %}
{% tab Swift Package Manager %}

[Swift Package Managerの統合ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager)に従って、`AppboyPushStory` を `Notification Content Extension` に追加します。

![Xcodeで、フレームワークとライブラリーの下にある「+」アイコンを選択してフレームワークを追加します。]({% image_buster /assets/img/ios/push_story/spm1.png %})

![Swift Package Managerの統合ガイドに従って、AppboyPushStoryをNotification Content Extensionに追加します。]({% image_buster /assets/img/ios/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

次の行をPodfileに追加します。

```ruby
target 'YourContentExtensionTarget' do
  pod 'Appboy-Push-Story'
end
```

Podfileを更新したら、ターミナル内でXcodeアプリプロジェクトのディレクトリーに移動し、`pod install` を実行します。

{% endtab %}
{% tab Manual %}

[GitHubリリースページ](https://github.com/Appboy/appboy-ios-sdk/releases)から最新の `AppboyPushStory.zip` をダウンロードして展開し、以下のファイルをプロジェクトの `Notification Content Extension` に追加します。
- `Resources/ABKPageView.nib`
- `AppboyPushStory.xcframework`

![GitHubリリースページから最新のAppboyPushStory.zipをダウンロードして展開し、ファイルをプロジェクトのNotification Content Extensionに追加します。]({% image_buster /assets/img/ios/push_story/manual1.png %})

{% alert important %}
**Embed** 列の下で、**AppboyPushStory.xcframework** に対して **Do Not Embed** が選択されていることを確認します。
{% endalert %}

**Build Settings** > **Other Linker Flags** でプロジェクトの `Notification Content Extension` に `-ObjC` フラグを追加します。

{% endtab %}
{% endtabs %}

## ステップ 5:通知ビューコントローラーを更新する {#step-5-updating-your-notification-view-controller}

{% tabs %}
{% tab OBJECTIVE-C %}

`NotificationViewController.h` で、次の行を追加して新しいプロパティを追加し、ヘッダーファイルをインポートします。

```objc
#import <AppboyPushStory/AppboyPushStory.h>
```

```objc
@property (nonatomic) IBOutlet ABKStoriesView *storiesView;
@property (nonatomic) ABKStoriesViewDataSource *dataSource;
```

`NotificationViewController.m` では、デフォルトの実装を削除し、次のコードを追加します。

```objc
@implementation NotificationViewController

- (void)didReceiveNotification:(UNNotification *)notification {
  self.dataSource = [[ABKStoriesViewDataSource alloc] initWithNotification:notification
                                                               storiesView:self.storiesView
                                                                  appGroup:@"YOUR-APP-GROUP-IDENTIFIER"];
}

- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response
                     completionHandler:(void (^)(UNNotificationContentExtensionResponseOption option))completion {
  UNNotificationContentExtensionResponseOption option = [self.dataSource didReceiveNotificationResponse:response];
  completion(option);
}

- (void)viewWillDisappear:(BOOL)animated {
  [self.dataSource viewWillDisappear];
  [super viewWillDisappear:animated];
}

@end
```

{% endtab %}
{% tab swift %}

`NotificationViewController.swift` で、次の行を追加してヘッダーファイルをインポートします。

```swift
import AppboyPushStory
```

次に、デフォルトの実装を削除し、次のコードを追加します。

```swift
class NotificationViewController: UIViewController, UNNotificationContentExtension {

  @IBOutlet weak var storiesView: ABKStoriesView!
  var dataSource: ABKStoriesViewDataSource?

  func didReceive(_ notification: UNNotification) {
    dataSource = ABKStoriesViewDataSource(notification: notification, storiesView: storiesView, appGroup: "YOUR-APP-GROUP-IDENTIFIER")
  }

  func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    if dataSource != nil {
      let option: UNNotificationContentExtensionResponseOption = dataSource!.didReceive(response)
      completion(option)
    }
  }

  override func viewWillDisappear(_ animated: Bool) {
    dataSource?.viewWillDisappear()
    super.viewWillDisappear(animated)
  }
}
```

{% endtab %}
{% endtabs %}

## ステップ 6:通知コンテンツ拡張ストーリーボードを設定する {#step-6-set-the-notification-content-extension-storyboard}

`Notification Content Extension` ストーリーボードを開き、通知ビューコントローラーに新しい `UIView` を配置します。クラスの名前を `ABKStoriesView` に変更します。通知ビューコントローラーのメインビューフレームに合わせて、ビューの幅と高さを自動サイズ変更可能にします。

![Notification Content Extensionストーリーボードを開き、通知ビューコントローラーに新しいUIViewを配置します。クラスの名前をABKStoriesViewに変更します。]({% image_buster /assets/img/ios/push_story/abkstoriesview_class.png %})

![通知ビューコントローラーのメインビューフレームに合わせて、ビューの幅と高さを自動サイズ変更可能にします。]({% image_buster /assets/img/ios/push_story/abkstoriesview_size.png %})

次に、追加された `ABKStoriesView` に通知ビューコントローラーの `storiesView` IBOutletをリンクします。

![ステップ6に関連するスクリーンショット：通知コンテンツ拡張ストーリーボードを設定します。]({% image_buster /assets/img/ios/push_story/abkstoriesview_outlet.png %})

## ステップ 7:通知コンテンツ拡張plistを設定する {#step-7-set-the-notification-content-extension-plist}

`Notification Content Extension` の `Info.plist` ファイルを開き、`NSExtension \ NSExtensionAttributes` で以下のキーを追加および変更します。

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2`（`String` タイプ）
`UNNotificationExtensionDefaultContentHidden` = `YES`（`Boolean` タイプ）
`UNNotificationExtensionInitialContentSizeRatio` = `0.65`（`Number` タイプ）

![ステップ7に関連するスクリーンショット：通知コンテンツ拡張plistを設定します。]({% image_buster /assets/img/ios/push_story/notificationcontentextension_plist.png %})

## ステップ 8:メインアプリでのBraze統合のアップデート {#step-8-updating-the-braze-integration-in-your-main-app}

### オプション 1:ランタイム {#option-1-runtime}

Brazeインスタンスの設定に使用する `appboyOptions` 辞書で、`ABKPushStoryAppGroupKey` エントリを追加し、値をワークスペースAPI識別子に設定します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKPushStoryAppGroupKey] = @"YOUR-APP-GROUP-IDENTIFIER";
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKPushStoryAppGroupKey : "YOUR-APP-GROUP-IDENTIFIER"
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endtab %}
{% endtabs %}

#### オプション 2:Info.plist {#option-2-infoplist}

または、`Info.plist` ファイルからPush Storyワークスペースを構成するには、`Braze` という名前の辞書を `Info.plist` ファイルに追加します。`Braze` 辞書内で、文字列型の `PushStoryAppGroup` サブエントリを追加し、値をワークスペース識別子に設定します。なお、Braze iOS SDK v4.0.2より前のバージョンでは、`Braze` の代わりに辞書キー `Appboy` を使用する必要があります。

## 次のステップ {#next-steps}

次に、[アクションボタン]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons)を統合する手順を参照してください。これはPush Storiesメッセージにボタンを表示するために必要です。