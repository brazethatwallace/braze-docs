## Swift SDKの統合 {#integrating-the-swift-sdk}

Braze Swift SDKは、Swift Package マネージャー（SPM）、CocoaPods、または手動での統合方法を使って統合しカスタマイズできます。各種SDKシンボルに関する詳細情報は、[Braze Swiftリファレンスドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/)を参照してください。

### 前提条件 {#prerequisites}

始める前に、[最新のBraze Swift SDKバージョン](https://github.com/braze-inc/braze-swift-sdk#version-information)がお使いの環境をサポートしていることを確認してください。

### ステップ1：Braze Swift SDKをインストールする {#step-1-install-the-braze-swift-sdk}

Braze Swift SDKのインストールには、[Swift Package マネージャー（SwiftPM）](https://swift.org/package-manager/)または[CocoaPods](http://cocoapods.org/)の使用を推奨します。あるいは、SDKを手動でインストールすることもできます。

{% tabs local %}
{% tab Swift Package マネージャー %}
#### ステップ1.1：SDKバージョンのインポート {#step-11-import-sdk-version}

プロジェクトを開き、プロジェクトの設定に移動します。**Swift Packages**タブを選択し、パッケージリストの下にある<i class="fas fa-plus"></i>追加ボタンをクリックします。

![Swift Packagesタブとパッケージ追加ボタンが表示されたXcodeプロジェクト設定。]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
バージョン7.4.0以降、Braze Swift SDKには[静的XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static)および[動的XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)としての追加の配布チャネルがあります。これらの形式のいずれかを使用したい場合は、それぞれのリポジトリのインストール手順に従ってください。
{% endalert %}

iOS Swift SDKリポジトリのURL `https://github.com/braze-inc/braze-swift-sdk` をテキストフィールドに入力します。**Dependency Rule**セクションで、SDKバージョンを選択します。最後に、**Add Package**をクリックします。

![Braze Swift SDKリポジトリURLが入力されたXcodeのAdd Packageダイアログ。]({% image_buster /assets/img/importsdk_example.png %})

#### ステップ1.2：パッケージを選択する {#step-12-select-your-packages}

Braze Swift SDKは、開発者がどの機能をプロジェクトにインポートするかをより詳細にコントロールできるように、機能をスタンドアロンライブラリーに分離しています。

| パッケージ | 詳細 |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BrazeKit` | 分析とプッシュ通知をサポートするメインSDKライブラリー。 |
| `BrazeLocation` | 位置情報分析とジオフェンス監視をサポートする位置情報ライブラリー。 |
| `BrazeUI` | アプリ内メッセージ、Content Cards、バナー用のBraze提供ユーザーインターフェイスライブラリー。デフォルトのUIコンポーネントを使用する場合は、このライブラリーをインポートしてください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ1.2：パッケージを選択する" }

{: .ws-td-nw-1}

##### 拡張ライブラリーについて {#about-extension-libraries}

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)と[BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)は追加機能を提供する拡張モジュールであり、メインアプリケーションターゲットに直接追加しないでください。代わりにリンクされたガイドに従って、それぞれのターゲット拡張機能に個別に統合してください。
{% endalert %}

| パッケージ | 詳細 |
| -------------------------- | ------------------------------------------------------------------------------------- |
| `BrazeNotificationService` | リッチプッシュ通知をサポートする通知サービス拡張ライブラリー。 |
| `BrazePushStory` | Push Storiesをサポートする通知コンテンツ拡張ライブラリー。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="拡張ライブラリーについて" }

{: .ws-td-nw-1}

ご自身のニーズに最も適したパッケージを選択し、**Add Package**をクリックしてください。必ず最低でも`BrazeKit`を選択してください。

![パッケージ追加前にBrazeKitが選択されたXcodeパッケージプロダクトリスト。]({% image_buster /assets/img/add_package.png %})
{% endtab %}

{% tab CocoaPods %}
#### ステップ1.1：CocoaPodsをインストールする {#step-11-install-cocoapods}

完全な手順については、CocoaPodsの[入門ガイド](https://guides.cocoapods.org/using/getting-started.html)を参照してください。そうでなければ、以下のコマンドを実行すればすぐに始められます：

```bash
$ sudo gem install cocoapods
```

行き詰まった場合は、CocoaPodsの[トラブルシューティングガイド](http://guides.cocoapods.org/using/troubleshooting.html)を確認してください。

#### ステップ1.2：Podfileの構築 {#step-12-constructing-the-podfile}

次に、Xcodeプロジェクトディレクトリ内に`Podfile`という名前のファイルを作成します。

{% alert note %}
バージョン7.4.0以降、Braze Swift SDKには[静的XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static)および[動的XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)としての追加の配布チャネルがあります。これらの形式のいずれかを使用したい場合は、それぞれのリポジトリのインストール手順に従ってください。
{% endalert %}

次の行をPodfileに追加します：

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit`にはメインSDKライブラリーが含まれており、分析とプッシュ通知のサポートが提供されています。

ポッドの更新がマイナーバージョンの更新よりも小さいものを自動的に取得するように、Brazeをバージョン管理することを推奨します。これは`pod 'BrazeKit' ~> Major.Minor.Build`のようになります。大きな変更があっても、Braze SDKの最新バージョンを自動的に統合したい場合は、Podfileで`pod 'BrazeKit'`を使用できます。

##### 追加ライブラリーについて {#about-additional-libraries}

Braze Swift SDKは、開発者がどの機能をプロジェクトにインポートするかをより詳細にコントロールできるように、機能をスタンドアロンライブラリーに分離しています。`BrazeKit`に加えて、以下のライブラリーをPodfileに追加できます：

| ライブラリー | 詳細 |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pod 'BrazeLocation'` | 位置情報分析とジオフェンス監視をサポートする位置情報ライブラリー。 |
| `pod 'BrazeUI'` | アプリ内メッセージ、Content Cards、バナー用のBraze提供ユーザーインターフェイスライブラリー。デフォルトのUIコンポーネントを使用する場合は、このライブラリーをインポートしてください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="追加ライブラリーについて" }

{: .ws-td-nw-1}

###### 拡張ライブラリー {#extension-libraries}

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)と[BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)は、追加機能を提供する拡張モジュールであり、メインアプリケーションターゲットに直接追加すべきではありません。代わりに、これらのモジュールごとに個別の拡張ターゲットを作成し、対応するターゲットにBrazeモジュールをインポートする必要があります。

| ライブラリー | 詳細 |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `pod 'BrazeNotificationService'` | リッチプッシュ通知をサポートする通知サービス拡張ライブラリー。 |
| `pod 'BrazePushStory'` | Push Storiesをサポートする通知コンテンツ拡張ライブラリー。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="拡張ライブラリー" }

{: .ws-td-nw-1}

#### ステップ1.3：SDKをインストールする {#step-13-install-the-sdk}

Braze SDK CocoaPodをインストールするには、ターミナル内でXcodeアプリプロジェクトのディレクトリに移動し、次のコマンドを実行します：
```
pod install
```

この時点で、CocoaPodsによって作成された新しいXcodeプロジェクトワークスペースを開くことができるはずです。Xcodeプロジェクトの代わりに、必ずこのXcodeワークスペースを使用してください。

![Brazeのサンプルフォルダが展開され、新しい`BrazeExample.workspace`が表示されている。]({% image_buster /assets/img/braze_example_workspace.png %})

#### CocoaPodsを使ってSDKを更新する {#updating-the-sdk-using-cocoapods}

CocoaPodを更新するには、プロジェクトディレクトリ内で以下のコマンドを実行するだけです：

```
pod update
```
{% endtab %}

{% tab Manual %}
#### ステップ1.1：Braze SDKをダウンロードする {#step-11-download-the-braze-sdk}

[GitHubのBraze SDKリリースページ](https://github.com/braze-inc/braze-swift-sdk/releases)に移動し、`braze-swift-sdk-prebuilt.zip`をダウンロードします。

![GitHub上のBraze SDKリリースページ。]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

#### ステップ1.2：フレームワークを選択する {#step-12-choose-your-frameworks}

Braze Swift SDKにはさまざまなスタンドアロンのXCFrameworkが含まれており、すべてを統合する必要はなく、必要な機能を自由に統合できます。次の表を参照して、XCFrameworksを選択してください：

| パッケージ | 必須 | 説明 |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit` | はい | 分析とプッシュ通知をサポートするメインSDKライブラリー。 |
| `BrazeLocation` | いいえ | 位置情報分析とジオフェンス監視をサポートする位置情報ライブラリー。 |
| `BrazeUI` | いいえ | アプリ内メッセージ、Content Cards、バナー用のBraze提供ユーザーインターフェイスライブラリー。デフォルトのUIコンポーネントを使用する場合は、このライブラリーをインポートしてください。 |
| `BrazeNotificationService` | いいえ | リッチプッシュ通知をサポートする通知サービス拡張ライブラリー。このライブラリーを直接メインアプリケーションターゲットに追加しないでください。代わりに[`BrazeNotificationService`ライブラリーを個別に追加してください](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)。 |
| `BrazePushStory` | いいえ | Push Storiesをサポートする通知コンテンツ拡張ライブラリー。このライブラリーを直接メインアプリケーションターゲットに追加しないでください。代わりに[`BrazePushStory`ライブラリーを個別に追加してください](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)。 |
| `BrazeKitCompat` | いいえ | `Appboy-iOS-SDK`バージョン4.X.Xで使用可能だったすべての`Appboy`および`ABK*`クラスとメソッドを含む互換性ライブラリー。使用の詳細については、[移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)の最小限の移行シナリオを参照してください。 |
| `BrazeUICompat` | いいえ | `Appboy-iOS-SDK`バージョン4.X.Xの`AppboyUI`ライブラリーで使用可能だったすべての`ABK*`クラスとメソッドを含む互換性ライブラリー。使用の詳細については、[移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)の最小限の移行シナリオを参照してください。 |
| `SDWebImage` | いいえ | 最小限の移行シナリオで`BrazeUICompat`によってのみ使用される依存関係。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ1.2：フレームワークを選択する" }

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 aria-label="ステップ1.2：フレームワークを選択する" }

#### ステップ1.3：ファイルを準備する {#step-13-prepare-your-files}

**静的**XCFrameworksまたは**動的**XCFrameworksのどちらを使用するかを決定してから、ファイルを準備します：

1. XCFrameworks用の一時ディレクトリを作成します。
2. `braze-swift-sdk-prebuilt`で、`dynamic`ディレクトリを開き、`BrazeKit.xcframework`を自分のディレクトリに移動します。ディレクトリは次のようになります：
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. [選択した各XCFramework](#swift_step-2-choose-your-frameworks)を一時ディレクトリに移動します。ディレクトリは次のようになります：
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```

#### ステップ1.4：フレームワークを統合する {#step-14-integrate-your-frameworks}

次に、[以前に準備した](#swift_step-3-prepare-your-files)**動的**または**静的**XCFrameworksを統合します：

Xcodeプロジェクトでビルドターゲットを選択し、次に**General**を選択します。**Frameworks, Libraries, and Embedded Content**の下に、[以前に準備したファイル](#swift_step-3-prepare-your-files)をドラッグ＆ドロップします。

![各Brazeライブラリーが「Embed & Sign」に設定されたXcodeプロジェクトの例。]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert note %}
Swift SDK 12.0.0以降では、静的および動的の両方のバリアントにおいて、Braze XCFrameworksに対して常に**Embed & Sign**を選択してください。これにより、フレームワークのリソースがアプリバンドルに適切に組み込まれます。
{% endalert %}

{% alert tip %}
GIFサポートを有効にするには、`braze-swift-sdk-prebuilt/static`または`braze-swift-sdk-prebuilt/dynamic`にある`SDWebImage.xcframework`を追加してください。
{% endalert %}

#### Objective-Cプロジェクトの一般的なエラー {#common-errors-for-objective-c-projects}

XcodeプロジェクトにObjective-Cファイルのみが含まれている場合、プロジェクトのビルドを試みると「missing symbol」エラーが発生することがあります。これらのエラーを修正するには、プロジェクトを開き、ファイルツリーに空のSwiftファイルを追加します。これにより、ビルドツールチェーンが[Swiftランタイム](https://support.apple.com/kb/dl1998)を埋め込み、ビルド時に適切なフレームワークにリンクするようになります。

```bash
FILE_NAME.swift
```

`FILE_NAME`を任意のスペースのない文字列に置き換えます。ファイルは次のようになります：

```bash
empty_swift_file.swift
```
{% endtab %}
{% endtabs local %}

### ステップ2：遅延初期化を設定する（任意） {#step-2-set-up-delayed-initialization-optional}

Braze Swift SDKの初期化を遅らせることができます。これは、アプリが設定を読み込む必要がある場合や、SDKを開始する前にユーザーの同意を待つ必要がある場合に便利です。遅延初期化により、SDK初期化前に受信したBrazeプッシュ通知とプッシュトークンは、SDKが初期化された時点でキューに入れられ処理されます。

遅延初期化を使用するには、最低限のBraze SDKバージョンが必要です：
{% sdk_min_versions swift:11.2.0 %}

#### ステップ2.1：遅延初期化の準備 {#step-21-prepare-for-delayed-initialization}

アプリのライフサイクルにおいて、できるだけ早い段階で`Braze.prepareForDelayedInitialization()`を呼び出してください。理想的には`application(_:didFinishLaunchingWithOptions:)`内またはそれ以前に呼び出します。これにより、SDKが初期化される前に受信したプッシュ通知が確実にキャプチャされ、後で適切に処理されます。

{% alert note %}
これはBrazeからのプッシュ通知にのみ適用されます。その他のプッシュ通知は、システムデリゲートによって通常通り処理されます。
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];

  // ... Additional non-Braze setup code

  return YES;
}
```
{% endtab %}
{% endtabs %}

遅延初期化を使用する場合、プッシュ通知のオートメーションは暗黙的に有効になります。`pushAutomation`パラメータを渡すことで、[プッシュオートメーションの設定をカスタマイズ](#swift_step-23-customize-push-automation-optional)できます。

#### ステップ2.2：プッシュ分析の動作を設定する（任意） {#step-22-configure-push-analytics-behavior-optional}

遅延初期化が有効な場合、プッシュ分析はデフォルトでキューに格納されます。ただし、プッシュ分析を明示的にキューに入れるか破棄するかを選択することもできます。

##### 明示的にキューに入れる {#explicitly-queue}

プッシュ分析を明示的にキューに入れるには（デフォルト動作）、`analyticsBehavior`パラメータに`.queue`を渡します。初期化前にキューに追加されたプッシュ分析イベントは、初期化時に処理されサーバーに送信されます。

{% tabs local %}
{% tab Swift %}
```swift
Braze.prepareForDelayedInitialization(analyticsBehavior: .queue)
```
{% endtab %}
{% tab Objective-C %}
```objc
[Braze prepareForDelayedInitializationWithAnalyticsBehavior:BRZPushEnqueueBehaviorQueue];
```
{% endtab %}
{% endtabs %}

##### 破棄する {#drop}

SDK初期化前に受信したプッシュ分析を破棄するには、`analyticsBehavior`パラメータに`.drop`を渡します。このオプションでは、SDKが初期化されていない間に発生したプッシュ分析イベントはすべて無視されます。

{% tabs local %}
{% tab Swift %}
```swift
Braze.prepareForDelayedInitialization(analyticsBehavior: .drop)
```
{% endtab %}
{% tab Objective-C %}
```objc
[Braze prepareForDelayedInitializationWithAnalyticsBehavior:BRZPushEnqueueBehaviorDrop];
```
{% endtab %}
{% endtabs %}

#### ステップ2.3：プッシュオートメーションをカスタマイズする（任意） {#swift_step-23-customize-push-automation-optional}

`pushAutomation`パラメータを渡すことで、プッシュオートメーションの設定をカスタマイズできます。デフォルトでは、`requestAuthorizationAtLaunch`を除くすべてのオートメーション機能が有効になっています。

{% tabs local %}
{% tab SWIFT %}
```swift
// Enable all push automation
featuresBraze.prepareForDelayedInitialization(pushAutomation: true)

// Or customize specific automation options
let automation = Braze.Configuration.Push.Automation()
automation.automaticSetup = true
automation.requestAuthorizationAtLaunch = false
Braze.prepareForDelayedInitialization(pushAutomation: automation)
```
{% endtab %}

{% tab OBJECTIVE-C %}
```objc
// Enable all push automation features
[Braze prepareForDelayedInitializationWithPushAutomation:[[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES]];

// Or customize specific automation options
BRZConfigurationPushAutomation *automation = [[BRZConfigurationPushAutomation alloc] init];
automation.automaticSetup = YES;
automation.requestAuthorizationAtLaunch = NO;
[Braze prepareForDelayedInitializationWithPushAutomation:automation analyticsBehavior:BRZPushEnqueueBehaviorQueue];
```
{% endtab %}
{% endtabs %}

#### ステップ2.4：SDKを初期化する {#swift_step-24-initialize-the-sdk}

選択した遅延期間の後（例えば、サーバーから設定を取得した後やユーザーの同意を得た後）、通常通りSDKを初期化します：

{% tabs local %}
{% tab SWIFT %}
```swift
func initializeBraze() {
  let configuration = Braze.Configuration(apiKey: "YOUR-API-KEY", endpoint: "YOUR-ENDPOINT")

  // Enable push automation to match the delayed initialization configuration
  configuration.push.automation = true
  let braze = Braze(configuration: configuration)

  // Store the Braze instance for later use
  AppDelegate.braze = braze
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (void)initializeBraze {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"YOUR-API-KEY" endpoint:@"YOUR-ENDPOINT"];

  // Enable push automation to match the delayed initialization configuration
  configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES];
  Braze *braze = [[Braze alloc] initWithConfiguration:configuration];

  // Store the Braze instance for later use
  AppDelegate.braze = braze;
}
```
{% endtab %}
{% endtabs %}

{% alert note %}
SDKが初期化されると、キューに蓄積されたプッシュ通知、プッシュトークン、ディープリンクは自動的に処理されます。
{% endalert %}

### ステップ3：アプリデリゲートを更新する {#step-3-update-your-app-delegate}

{% alert important %}
以下は、プロジェクトに既に`AppDelegate`を追加済み（デフォルトでは生成されません）であり、遅延初期化機能を使用していないことを前提としています。`AppDelegate`を使用する予定がない場合は、アプリの起動時など、できるだけ早い段階でBraze SDKを初期化してください。遅延初期化機能を使用している場合は、SDKの初期化については[ステップ2.4](#swift_step-24-initialize-the-sdk)を参照し、このステップは無視してください。
{% endalert %}

{% subtabs local %}
{% subtab swift %}
`AppDelegate.swift`ファイルに以下のコード行を追加して、Braze Swift SDKに含まれる機能をインポートします：

```swift
import BrazeKit
```

次に、`AppDelegate`クラスにstaticプロパティを追加し、アプリケーションのライフタイムを通してBrazeインスタンスへの強い参照を保持します：

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

SDKでは、アプリケーションが使用期間を通してBrazeインスタンスへの強い参照を保持する必要があります。予期しない副作用を防ぐため、Brazeインスタンスのプロパティやメソッドにアクセスまたは変更する前に、その参照を完全にキャプチャしていることを確認してください。

最後に、`AppDelegate.swift`で、`application:didFinishLaunchingWithOptions:`メソッドに次のスニペットを追加します：

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

**アプリ設定**ページから、`YOUR-APP-IDENTIFIER-API-KEY`と`YOUR-BRAZE-ENDPOINT`を正しい値に更新してください。アプリ識別子APIキーの場所については、[API識別子の種類]({{site.baseurl}}/api/identifier_types/?tab=app%20ids)を参照してください。

{% endsubtab %}
{% subtab OBJECTIVE-C %}

次のコード行を`AppDelegate.m`ファイルに追加します：

```objc
@import BrazeKit;
```

次に、`AppDelegate.m`ファイルに静的変数を追加して、アプリケーションのライフタイムを通してBrazeインスタンスへの参照を保持します：

```objc
static Braze *_braze;

@implementation AppDelegate
+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
@end
```

SDKでは、アプリケーションが使用期間を通してBrazeインスタンスへの強い参照を保持する必要があります。予期しない副作用を防ぐため、Brazeインスタンスのプロパティやメソッドにアクセスまたは変更する前に、その参照を完全にキャプチャしていることを確認してください。

最後に、`AppDelegate.m`ファイル内で、`application:didFinishLaunchingWithOptions:`メソッド内に以下のスニペットを追加します：

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:"YOUR-APP-IDENTIFIER-API-KEY"
                                                                  endpoint:"YOUR-BRAZE-ENDPOINT"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

**設定の管理**ページから、`YOUR-APP-IDENTIFIER-API-KEY`と`YOUR-BRAZE-ENDPOINT`を正しい値で更新してください。アプリ識別子APIキーの場所について詳しくは、[APIドキュメント]({{site.baseurl}}/api/api_key#the-app-identifier-api-key)をご覧ください。

{% endsubtab %}
{% endsubtabs local %}

{% alert note %}
`Braze.init`は呼び出しスレッド上で即座に返されます。SDKは内部キューで起動処理を行います。`init`の直後にメインスレッドで`braze.deviceId`などの同期プロパティを読み取ると、SDKが初期化後の処理を完了するまで呼び出しスレッドがブロックされます。メインスレッドやレイテンシに敏感なコンテキストでは、ブロックせずに値を読み取るために`braze.getDeviceId(_:)`（Swift）または`[braze getDeviceIdWithCompletion:^(NSString *deviceId) { ... }]`（Objective-C）を使用してください。
{% endalert %}

## オプション設定 {#optional-configurations}

### ロギング {#logging}

すべてのプラットフォームにわたる一元的な概要については、[詳細ログ]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)を参照してください。ログ出力の解釈方法については、[詳細ログの読み方]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs)を参照してください。

#### ログレベル {#log-levels}

Braze Swift SDKのデフォルトのログレベルは`.error`です。これはログが有効な場合にサポートされる最低レベルでもあります。以下がログレベルの一覧です：

| Swift | Objective-C | 説明 |
| ----------- | ------------------------ | ------------------------------------------------------------ |
| `.debug` | `BRZLoggerLevelDebug` | デバッグ情報 + `.info` + `.error`を記録します。 |
| `.info` | `BRZLoggerLevelInfo` | 一般的なSDK情報（ユーザーの変更など）+ `.error`を記録します。 |
| `.error` | `BRZLoggerLevelError` | エラーを記録します。 |
| `.disabled` | `BRZLoggerLevelDisabled` | ロギングは行われません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ログレベル" }

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ログレベル" }

#### ログレベルの設定 {#setting-the-log-level}

実行時に`Braze.Configuration`オブジェクト内でログレベルを割り当てることができます。完全な使用方法の詳細については、[`Braze.Configuration.Logger`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class)を参照してください。

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}