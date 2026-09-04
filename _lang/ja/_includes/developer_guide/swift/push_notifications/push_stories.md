{% multi_lang_include developer_guide/prerequisites/swift.md %} [プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)も必要です。これには`UNNotification`フレームワークの実装が含まれます。

Push Storiesを受信するには、以下の最小SDKバージョンが必要です。

{% sdk_min_versions swift:5.0.0 %}

## Push Storiesの設定 {#setting-up-push-stories}

### ステップ 1: 通知コンテンツ拡張ターゲットを追加する {#notification-content-extension}

アプリプロジェクトで、メニュー**File > New > Target**に移動し、新しい`Notification Content Extension`ターゲットを追加してアクティブにします。

![Push Stories用のNotification Content Extensionを作成するXcodeターゲットピッカー]({% image_buster /assets/img/swift/push_story/add_content_extension.png %})

Xcodeによって新しいターゲットが生成され、以下のファイルが自動的に作成されます。

- `NotificationViewController.swift`
- `MainInterface.storyboard`

### ステップ 2: 機能を有効にする {#enable-capabilities}

Xcodeで、メインアプリターゲットの**Signing & Capabilities**パネルを使用してBackground Modes機能を追加します。**Background fetch**と**Remote notifications**の両方のチェックボックスを選択します。

![]({% image_buster /assets/img/swift/push_story/enable_background_mode.png %})

#### アプリグループの追加 {#adding-an-app-group}

さらに、Xcodeの**Signing & Capabilities**パネルから、メインアプリターゲットと通知コンテンツ拡張ターゲットの両方にApp Groups機能を追加します。次に、**+**ボタンをクリックします。アプリのバンドルIDを使用してアプリグループを作成します。たとえば、アプリのバンドルIDが`com.company.appname`の場合、アプリグループに`group.com.company.appname.xyz`という名前を付けることができます。

{% alert important %}
ここでいうApp Groupsとは、Appleの[App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups)のことであり、Brazeのワークスペース（旧アプリグループ）IDのことではありません。
{% endalert %}

アプリをアプリグループに追加しないと、アプリがプッシュペイロードからの特定のフィールドの入力に失敗し、期待どおりに完全に動作しない可能性があります。

### ステップ 3: アプリにPush Storyフレームワークを追加する

{% tabs local %}
{% tab Swift Package マネージャー %}

[Swift Package マネージャーの統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/)に従って、`BrazePushStory`を`Notification Content Extension`に追加します。

![Xcodeで、フレームワークとライブラリの下にある「+」アイコンを選択してフレームワークを追加します。]({% image_buster /assets/img/swift/push_story/spm1.png %})

![通知コンテンツ拡張ターゲットにBrazePushStoryを追加するXcodeパッケージプロダクト選択画面]({% image_buster /assets/img/swift/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Podfileに次の行を追加します。

```ruby
target 'YourAppTarget' do
pod 'BrazeKit'
pod 'BrazeUI'
pod 'BrazeLocation'
end

target 'YourNotificationContentExtensionTarget' do
pod 'BrazePushStory'
end

# Only include the below if you want to also integrate Rich Push
target 'YourNotificationServiceExtensionTarget' do
pod 'BrazeNotificationService'
end
```

{% alert note %}
リッチプッシュの実装方法については、[リッチ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/?tab=swift%20package%20manager)を参照してください。
{% endalert %}

Podfileを更新したら、ターミナル内でXcodeアプリプロジェクトのディレクトリに移動し、`pod install`を実行します。

{% endtab %}
{% tab Manual %}

[GitHubリリースページ](https://github.com/braze-inc/braze-swift-sdk/releases)から最新の`BrazePushStory.zip`をダウンロードして展開し、`BrazePushStory.xcframework`をプロジェクトの`Notification Content Extension`に追加します。

![BrazePushStory.xcframeworkがDo Not Embed選択で追加されたXcodeフレームワーク設定]({% image_buster /assets/img/swift/push_story/manual1.png %})

{% alert important %}
**Embed**列の下で、**BrazePushStory.xcframework**に対して**Do Not Embed**が選択されていることを確認してください。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ 4: 通知ビューコントローラーを更新する

`NotificationViewController.swift`に以下の行を追加し、ヘッダーファイルをインポートします。

```swift
import BrazePushStory
```

次に、[`BrazePushStory.NotificationViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/)を継承してデフォルトの実装を置き換えます。

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

#### プッシュストーリーイベントのカスタム処理 {#custom-handling-push-story-events}

独自のカスタムロジックを実装してプッシュストーリー通知イベントを処理する場合は、上記のように`BrazePushStory.NotificationViewController`を継承し、以下の例のように[`didReceive`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/didreceive(_:))メソッドをオーバーライドします。

```swift
import BrazePushStory
import UserNotifications
import UserNotificationsUI

class NotificationViewController: BrazePushStory.NotificationViewController {
  override func didReceive(_ notification: UNNotification) {
    super.didReceive(notification)

    // Custom handling logic
  }

  override func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    super.didReceive(response, completionHandler: completion)

    // Custom handling logic
  }
}
```

### ステップ 5: 通知コンテンツ拡張plistを設定する

`Notification Content Extension`の`Info.plist`ファイルを開き、`NSExtension \ NSExtensionAttributes`の下に以下のキーを追加・変更します。

| キー                                              | タイプ    | 値                      |
|--------------------------------------------------|---------|------------------------|
| `UNNotificationExtensionCategory`                | 文字列  | `ab_cat_push_story_v2` |
| `UNNotificationExtensionDefaultContentHidden`    | ブール値 | `YES`                  |
| `UNNotificationExtensionInitialContentSizeRatio` | 数値    | `0.6`                  |
| `UNNotificationExtensionUserInteractionEnabled`  | ブール値 | `YES`                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ5: 通知コンテンツ拡張plistの設定" }

さらに、同じ`Info.plist`ファイルに以下の最上位`Braze`ディクショナリを追加します。`REPLACE_WITH_APPGROUP`を[ステップ2](#enable-capabilities)で作成したアプリグループに置き換えてください。

| キー              | タイプ   | 値                       |
|------------------|--------|--------------------------|
| `Braze.AppGroup` | 文字列 | `REPLACE_WITH_APPGROUP`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ5: 通知コンテンツ拡張plistの設定" }

`Info.plist`ファイルは以下の画像と一致するはずです。

![Brazeプッシュストーリーキーとアプリグループ設定が含まれたNotification Content ExtensionのInfo.plist]({% image_buster /assets/img/swift/push_story/notificationcontentextension_plist.png %})

### ステップ 6: メインアプリでのBraze統合を更新する {#update-braze}

Brazeを初期化する前に、アプリグループの名前をBraze設定の[`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup)プロパティに割り当てます。

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```
