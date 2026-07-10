## React Native Braze SDKについて {#about-the-react-native-braze-sdk}

React Native Braze SDKを統合すると、基本的な分析機能を利用できます。さらに、iOSとAndroidの両プラットフォーム向けに、単一のコードベースでアプリ内メッセージとContent Cardsを導入できます。

## 新しいアーキテクチャの互換性 {#new-architecture-compatibility}

以下の最小SDKバージョンは、[React Nativeの新しいアーキテクチャ](https://reactnative.dev/docs/the-new-architecture/landing-page)を使用するすべてのアプリと互換性があります。

{% sdk_min_versions reactnative:2.0.1 %}

SDKバージョン6.0.0以降、BrazeはReact Native Turbo Moduleを採用しています。これは新アーキテクチャと従来のブリッジアーキテクチャの両方と互換性があるため、追加の設定は不要です。

{% alert warning %}
iOSアプリが`RCTAppDelegate`に準拠し、以前の`AppDelegate`設定手順に従っている場合、Turbo Moduleでイベントを購読する際のクラッシュを防ぐため、[完全なネイティブ設定](#reactnative_step-2-complete-native-setup)のサンプルを確認してください。
{% endalert %}

## ReactとReact Nativeのバージョン要件 {#react-and-react-native-version-requirements}

Brazeは、React Native SDKがサポートする範囲を超えて、個別のReact最小バージョンを公開していません。SDKを統合するには、React Nativeバージョン0.71以降を使用してください。サポートされているReact Nativeバージョンの完全なリストについては、[React Native SDK GitHubリポジトリ](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support)を参照してください。

React、React Native、またはBraze SDKをアップグレードする際は、デプロイ前にSDKの[CHANGELOG](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)で破壊的変更を確認してください。

## React Native SDKの統合 {#integrating-the-react-native-sdk}

### 前提条件 {#prerequisites}

サポートされているReact Nativeバージョンとアップグレードガイダンスについては、[ReactとReact Nativeのバージョン要件](#react-and-react-native-version-requirements)を参照してください。

### ステップ 1: Brazeライブラリーの統合 {#step-1-integrate-the-braze-library}

{% tabs local %}
{% tab npm %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab yarn %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

<a id="step-2-choose-a-setup-option"></a>
<a id="reactnative_step-2-complete-native-setup"></a>
### ステップ 2: ネイティブ設定の完了 {#step-2-complete-native-setup}

アプリがExpoを使用している場合は、[Expoプラグインの使用](#reactnative-using-the-expo-plugin)を参照してください。アプリがピュアReact Nativeを使用している場合は、[React Native CLIの使用](#reactnative-using-react-native-cli)を参照してください。
各バージョンタブで、ExpoプラグインまたはReact Native CLIのいずれかの設定方法を選択してください。

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

#### 方法 1: Expoプラグインの使用 {#reactnative-using-the-expo-plugin}

##### 2.1 Braze Expoプラグインのインストール {#21-install-the-braze-expo-plugin}

Braze Expoプラグインのバージョンが4.1.0以上であることを確認してください。サポートされているバージョンの完全なリストについては、[Braze Expoプラグインリポジトリ](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support)を参照してください。

以下のコードスニペットは、Braze Expoプラグインをインストールするコマンドです。

```bash
npx expo install @braze/expo-plugin
```

##### 2.2 app.jsonにプラグインを追加する {#22-add-the-plugin-to-your-appjson}

`app.json`で、Braze Expoプラグインを追加します。APIキーとエンドポイントはここでは設定しません。JavaScriptから`Braze.initialize()`を使用してランタイムで提供します。実装のニーズに応じて、以下のオプション設定パラメーターを追加してください。

| 方法                                        | タイプ    | 説明                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enableBrazeIosPush`                          | boolean | iOSのみ。iOSでのプッシュ通知の処理にBrazeを使用するかどうか。                       |
| `enableFirebaseCloudMessaging`                | boolean | Androidのみ。プッシュ通知にFirebase Cloud Messagingを使用するかどうか。             |
| `firebaseCloudMessagingSenderId`              | string  | Androidのみ。Firebase Cloud Messagingの送信者ID。                                    |
| `sessionTimeout`                              | integer | アプリケーションのBrazeセッションタイムアウト（秒単位）。                                                                                               |
| `enableSdkAuthentication`                     | boolean | [SDK認証]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/#sdk-authentication)機能を有効にするかどうか。      |
| `logLevel`                                    | integer | アプリケーションのログレベル。デフォルトのログレベルは8で、最低限の情報を記録します。デバッグのために詳細ログを有効にするには、ログレベル0を使用してください。    |
| `minimumTriggerIntervalInSeconds`             | integer | トリガー間の最小時間間隔（秒単位）。デフォルトは30秒です。                                                                           |
| `enableAutomaticLocationCollection`           | boolean | 自動位置情報収集が有効かどうか（ユーザーが許可した場合）。                                                                                  |
| `enableGeofence`                              | boolean | ジオフェンスを有効にするかどうか。                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | ジオフェンスリクエストを自動で行うかどうか。                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | iOSのみ。ユーザーがアプリ内メッセージの外側をクリックした時に、モーダルなアプリ内メッセージが閉じられるかどうか。                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Androidのみ。Braze SDKが自動的にプッシュディープリンクを処理するかどうか。                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Androidのみ。`android.text.Html.fromHtml`を使って、プッシュ通知のテキストコンテンツをHTMLとして解釈し、レンダリングするかどうかを設定します。        |
| `androidNotificationAccentColor`              | string  | Androidのみ。Android通知のアクセントカラーを設定します。                                                                                                |
| `androidNotificationLargeIcon`                | string  | Androidのみ。Android通知の大アイコンを設定します。                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Androidのみ。Android通知の小アイコンを設定します。                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | iOSのみ。アプリの起動時にユーザーにプッシュ許可を自動的に求めるかどうか。                                                          |
| `enableBrazeIosRichPush`                      | boolean | iOSのみ。iOSのリッチプッシュ機能を有効にするかどうか。                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | iOSのみ。iOSのBraze Push Storiesを有効にするかどうか。                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | iOSのみ。iOS Push Storiesに使用されるアプリグループ。                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | iOSのみ。デバイスIDがランダムに生成されたUUIDを使用するかどうか。                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | iOSのみ。SDKがユニバーサルリンクを自動的に認識し、システムメソッドに転送するかどうかを指定します（デフォルト：`false`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="app.jsonにプラグインを追加する" }

以下のコードスニペットは、`app.json`の設定例です。

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ]
    ]
  }
}
```

###### Androidプッシュ通知アイコンの設定 {#android-push-icons}

`androidNotificationLargeIcon`と`androidNotificationSmallIcon`を使用する際は、アイコンを正しく表示するために以下のベストプラクティスに従ってください。

**アイコンの配置と形式**

Braze Expoプラグインでカスタムプッシュ通知アイコンを使用するには：

1. 以下のアイコン要件に従ってアイコンファイルを作成します。
2. プロジェクトのAndroidネイティブディレクトリ`android/app/src/main/res/drawable-<density>/`に配置します。
   例えば、`android/app/src/main/res/drawable-mdpi/`や`android/app/src/main/res/drawable-hdpi/`を使用します。
3. あるいは、React Nativeディレクトリ内でアセットを管理している場合、Expoの[app.jsonアイコン設定](https://docs.expo.dev/versions/latest/config/app/#icon)を使用するか、[Expo設定プラグイン](https://docs.expo.dev/config-plugins/introduction/)を作成して、プリビルド時にアイコンをAndroidのdrawableフォルダにコピーできます。

Braze Expoプラグインは、Androidのdrawableリソースシステムを使ってこれらのアイコンを参照します。

**アイコンの要件**

- **小アイコン：** 透明なバックグラウンドに白いシルエットでなければなりません（これはAndroidプラットフォームの要件です）
- **大アイコン：** フルカラーの画像を使用できます。
- **形式：** PNG形式が推奨されます。
- **命名：** 小文字、数字、アンダースコアのみを使用してください（例：`my_large_icon.png`）

**app.jsonでの設定**

以下のコードスニペットは、`app.json`で`@drawable/`プレフィックスを使用してAndroid通知アイコンを参照する方法です。

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
アイコンを参照する際には、相対パス（例：`src/assets/images/icon.png`）を使用したり、ファイル拡張子を含めたりしないでください。Expoプラグインは、プリビルド処理後にAndroidネイティブフォルダ内でアイコンを正しく見つけられるように、`@drawable/`プレフィックスが必要です。
{% endalert %}

**仕組み**

Braze Expoプラグインは、Androidの`drawable`ディレクトリからアイコンファイルを参照します。`npx expo prebuild`を実行すると、ExpoはネイティブのAndroidプロジェクト構造を生成します。ビルドプロセス前に、アイコンはAndroidの`drawable`フォルダ内に存在しなければなりません（手動で配置するか、設定プラグイン経由でコピーするかのいずれか）。プラグインはその後、これらのdrawableリソースを名前（パスや拡張子なし）で利用するようBraze SDKを設定します。これが設定で`@drawable/`プレフィックスが必要な理由です。

Android通知アイコンの詳細については、[Androidの通知アイコンガイドライン](https://developer.android.com/develop/ui/views/notifications#icon)を参照してください。

##### 2.3 アプリケーションのビルドおよび実行 {#23-build-and-run-your-application}

アプリケーションをプリビルドすると、Braze Expoプラグインが動作するために必要なネイティブファイルが生成されます。

以下のコードスニペットは、アプリケーションをプリビルドするコマンドです。

```bash
npx expo prebuild
```

[Expoドキュメント](https://docs.expo.dev/workflow/customizing/)の指定に従い、アプリケーションを実行します。設定オプションを変更した場合は、アプリケーションを再度プリビルドして実行してください。

#### 方法 2: React Native CLIの使用 {#reactnative-using-react-native-cli}

##### Androidの設定 {#set-up-android}

**2.1 Kotlin Gradleプラグインの追加**

以下のコードスニペットは、最上位プロジェクトの`build.gradle`の`buildscript` > `dependencies`にKotlin Gradleプラグインを追加する方法です。

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

これでプロジェクトにKotlinが追加されます。

**2.2 Braze SDKの設定**

プロジェクトの`res/values`フォルダに`braze.xml`ファイルを作成します。APIキーとエンドポイントはJavaScriptからランタイムで提供されるため、このファイルでは不要です。以下のコードスニペットは、`com_braze_enable_delayed_initialization`で遅延初期化を有効にする方法です。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
</resources>
```

{% alert note %}
`braze.xml`には他のネイティブ設定値（プッシュ、セッションタイムアウト、ログ設定など）を追加することもできます。これらはJavaScriptから`Braze.initialize()`が呼び出された際に自動的に適用されます。
{% endalert %}

以下のコードスニペットは、`AndroidManifest.xml`ファイルに必要な権限です。

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
Braze Android SDKバージョン12.2.0以降では、`gradle.properties`ファイルに`importBrazeLocationLibrary=true`を設定することで、android-sdk-locationライブラリーを自動的にプルインできます。
{% endalert %}

**2.3 ユーザーセッショントラッキングの実装**

`openSession()`および`closeSession()`への呼び出しは自動的に処理されます。
以下のコードスニペットは、`MainApplication`クラスの`onCreate()`メソッドに追加する内容です。

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**2.4 インテント更新の処理**

MainActivityで`android:launchMode`が`singleTask`に設定されている場合、以下のコードスニペットを`MainActivity`クラスに追加してください。

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### iOSの設定 {#set-up-ios}

**2.5（オプション）ダイナミックXCFrameworkに関するPodfileの設定**

特定のBrazeライブラリー（例：BrazeUI）をObjective-C++ファイルにインポートするには、`#import`構文を使用する必要があります。Braze Swift SDKのバージョン`7.4.0`以降、バイナリにはこの構文と互換性のある[ダイナミックXCFrameworkとしてのオプションの配布チャネル](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)があります。

この配布チャネルを使用する場合は、PodfileでCocoaPodsのソースの場所を手動で上書きしてください。以下のサンプルを参照し、`{your-version}`をインポートする関連バージョンに置き換えてください。

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**2.6 Podのインストール**

React Nativeではライブラリーがネイティブプラットフォームに自動でリンクされるため、CocoaPodsを使用してSDKをインストールできます。

以下のコードスニペットは、プロジェクトのルートフォルダからPodをインストールする方法です。

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**2.7 Braze SDKの設定**

`BrazeReactInitializer.configure`を`AppDelegate`で使用して、ネイティブ設定を登録します。提供したクロージャは保存され、JavaScriptから`Braze.initialize(apiKey, endpoint)`が呼び出された際に適用されます。

{% subtabs local %}
{% subtab SWIFT %}

以下のコードスニペットは、`AppDelegate.swift`ファイルの先頭でBraze SDKをインポートする方法です。

```swift
import BrazeKit
import braze_react_native_sdk
```

`application(_:didFinishLaunchingWithOptions:)`メソッドで、`BrazeReactInitializer.configure`を使用してネイティブ設定を登録します。ここではAPIキーやエンドポイントを設定しないでください。これらはJavaScriptの`Braze.initialize()`から提供されます。

- **`configure`クロージャ**：`Braze.Configuration`を受け取り、ネイティブ設定プロパティ（ログ、プッシュ、セッションなど）を設定できます。
- **`postInitialization`クロージャ**（オプション）：作成後のライブ`Braze`インスタンスを受け取り、インスタンスが必要なセットアップ（例：参照の保存やデリゲートの設定）に使用します。

以下のコードスニペットは、`BrazeReactInitializer.configure`を使用した`AppDelegate.swift`の実装例です。

```swift
@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    BrazeReactInitializer.configure { configuration in
      configuration.logger.level = .info
      configuration.push.automation = true
    } postInitialization: { braze in
      AppDelegate.braze = braze
    }

    // ... React Native setup

    return true
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

以下のコードスニペットは、`AppDelegate.m`ファイルの先頭でBraze SDKをインポートする方法です。

```objc
@import BrazeKit;
@import braze_react_native_sdk;
```

`application:didFinishLaunchingWithOptions:`メソッドで、`BrazeReactInitializer`を使用してネイティブ設定を登録します。ここではAPIキーやエンドポイントを設定しないでください。これらはJavaScriptの`Braze.initialize()`から提供されます。

以下のコードスニペットは、`BrazeReactInitializer`を使用した`AppDelegate.m`の実装例です。

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [BrazeReactInitializer configure:^(BRZConfiguration *configuration) {
    configuration.logger.level = BRZLoggerLevelInfo;
    configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES];
  } postInitialization:^(Braze *braze) {
    // Store the Braze instance for later use.
  }];

  /* Other configuration */

  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`BrazeReactInitializer.configure()`は設定を保存するだけです。JavaScriptから`Braze.initialize()`が呼び出されるまでBrazeインスタンスは存在しないため、`configure()`の後にAppDelegateでBraze SDKメソッドを呼び出さないでください。
`Braze.initialize()`を再度呼び出すと、同じ`configure`および`postInitialization`ブロックが新しいBrazeインスタンスに適用されます。
{% endalert %}

{% endtab %}
{% tab React Native SDK 19.1.0以前 %}

#### 方法 1: Expoプラグインの使用 {#method-1-using-the-expo-plugin}

##### ステップ 2.1: Braze Expoプラグインのインストール {#step-21-install-the-braze-expo-plugin}

Braze React Native SDKのバージョンが1.37.0以上であることを確認してください。サポートされているバージョンの完全なリストについては、[Braze React Nativeリポジトリ](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support)を参照してください。

以下のコードスニペットは、Braze Expoプラグインをインストールするコマンドです。

```bash
npx expo install @braze/expo-plugin
```

##### ステップ 2.2: app.jsonにプラグインを追加する {#step-22-add-the-plugin-to-your-appjson}

`app.json`で、Braze Expoプラグインを追加します。以下の設定オプションを指定できます。

| 方法                                        | タイプ    | 説明                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | string  | 必須。Brazeダッシュボードの**設定の管理**にあるAndroidアプリケーションの[APIキー]({{site.baseurl}}/api/identifier_types/)。 |
| `iosApiKey`                                   | string  | 必須。Brazeダッシュボードの**設定の管理**にあるiOSアプリケーションの[APIキー]({{site.baseurl}}/api/identifier_types/)。     |
| `baseUrl`                                     | string  | 必須。Brazeダッシュボードの**設定の管理**にあるアプリケーションの[SDKエンドポイント]({{site.baseurl}}/api/basics/#endpoints)。    |
| `enableBrazeIosPush`                          | boolean | iOSのみ。iOSでのプッシュ通知の処理にBrazeを使用するかどうか。React Native SDK v1.38.0およびExpo Plugin v0.4.0で導入されました。                       |
| `enableFirebaseCloudMessaging`                | boolean | Androidのみ。プッシュ通知にFirebase Cloud Messagingを使用するかどうか。React Native SDK v1.38.0およびExpo Plugin v0.4.0で導入されました。             |
| `firebaseCloudMessagingSenderId`              | string  | Androidのみ。Firebase Cloud Messagingの送信者ID。React Native SDK v1.38.0およびExpo Plugin v0.4.0で導入されました。                                    |
| `sessionTimeout`                              | integer | アプリケーションのBrazeセッションタイムアウト（秒単位）。                                                                                               |
| `enableSdkAuthentication`                     | boolean | [SDK認証]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/#sdk-authentication)機能を有効にするかどうか。      |
| `logLevel`                                    | integer | アプリケーションのログレベル。デフォルトのログレベルは8で、最低限の情報を記録します。デバッグのために詳細ログを有効にするには、ログレベル0を使用してください。    |
| `minimumTriggerIntervalInSeconds`             | integer | トリガー間の最小時間間隔（秒単位）。デフォルトは30秒です。                                                                           |
| `enableAutomaticLocationCollection`           | boolean | 自動位置情報収集が有効かどうか（ユーザーが許可した場合）。                                                                                  |
| `enableGeofence`                              | boolean | ジオフェンスを有効にするかどうか。                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | ジオフェンスリクエストを自動で行うかどうか。                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | iOSのみ。ユーザーがアプリ内メッセージの外側をクリックした時に、モーダルなアプリ内メッセージが閉じられるかどうか。                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Androidのみ。Braze SDKが自動的にプッシュディープリンクを処理するかどうか。                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Androidのみ。`android.text.Html.fromHtml`を使って、プッシュ通知のテキストコンテンツをHTMLとして解釈し、レンダリングするかどうかを設定します。        |
| `androidNotificationAccentColor`              | string  | Androidのみ。Android通知のアクセントカラーを設定します。                                                                                                |
| `androidNotificationLargeIcon`                | string  | Androidのみ。Android通知の大アイコンを設定します。                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Androidのみ。Android通知の小アイコンを設定します。                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | iOSのみ。アプリの起動時にユーザーにプッシュ許可を自動的に求めるかどうか。                                                          |
| `enableBrazeIosRichPush`                      | boolean | iOSのみ。iOSのリッチプッシュ機能を有効にするかどうか。                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | iOSのみ。iOSのBraze Push Storiesを有効にするかどうか。                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | iOSのみ。iOS Push Storiesに使用されるアプリグループ。                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | iOSのみ。デバイスIDがランダムに生成されたUUIDを使用するかどうか。                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | iOSのみ。SDKがユニバーサルリンクを自動的に認識し、システムメソッドに転送するかどうかを指定します（デフォルト：`false`）。有効にすると、SDKは[アプリでのユニバーサルリンクのサポート](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/)で定義されたシステムメソッドにユニバーサルリンクを自動的に転送します。React Native SDK v11.1.0およびExpo Plugin v3.2.0で導入されました。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="app.jsonにプラグインを追加する" }

以下のコードスニペットは、`app.json`の設定例です。

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ],
    ]
  }
}
```

###### Androidプッシュ通知アイコンの設定 {#configuring-android-push-notification-icons}

`androidNotificationLargeIcon`と`androidNotificationSmallIcon`を使用する際は、アイコンを正しく表示するために以下のベストプラクティスに従ってください。

**アイコンの配置と形式**

Braze Expoプラグインでカスタムプッシュ通知アイコンを使用するには：

1. 以下のアイコン要件に従ってアイコンファイルを作成します。
2. プロジェクトのAndroidネイティブディレクトリ`android/app/src/main/res/drawable-<density>/`に配置します（例：`android/app/src/main/res/drawable-mdpi/`、`drawable-hdpi/`など）。
3. あるいは、React Nativeディレクトリ内でアセットを管理している場合、Expoの[app.jsonアイコン設定](https://docs.expo.dev/versions/latest/config/app/#icon)を使用するか、[Expo設定プラグイン](https://docs.expo.dev/config-plugins/introduction/)を作成して、プリビルド時にアイコンをAndroidのdrawableフォルダにコピーできます。

Braze Expoプラグインは、Androidのdrawableリソースシステムを使ってこれらのアイコンを参照します。

**アイコンの要件**

- **小アイコン：** 透明なバックグラウンドに白いシルエットでなければなりません（これはAndroidプラットフォームの要件です）
- **大アイコン：** フルカラーの画像を使用できます。
- **形式：** PNG形式が推奨されます。
- **命名：** 小文字、数字、アンダースコアのみを使用してください（例：`my_large_icon.png`）

**app.jsonでの設定**

以下のコードスニペットは、`app.json`で`@drawable/`プレフィックスを使用してAndroid通知アイコンを参照する方法です。

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
アイコンを参照する際には、相対パス（例：`src/assets/images/icon.png`）を使用したり、ファイル拡張子を含めたりしないでください。Expoプラグインは、プリビルド処理後にAndroidネイティブフォルダ内でアイコンを正しく見つけられるように、`@drawable/`プレフィックスが必要です。
{% endalert %}

**仕組み**

Braze Expoプラグインは、Androidの`drawable`ディレクトリからアイコンファイルを参照します。`npx expo prebuild`を実行すると、ExpoはネイティブのAndroidプロジェクト構造を生成します。ビルドプロセス前に、アイコンはAndroidの`drawable`フォルダ内に存在しなければなりません（手動で配置するか、設定プラグイン経由でコピーするかのいずれか）。プラグインはその後、これらのdrawableリソースを名前（パスや拡張子なし）で利用するようBraze SDKを設定します。これが設定で`@drawable/`プレフィックスが必要な理由です。

Android通知アイコンの詳細については、[Androidの通知アイコンガイドライン](https://developer.android.com/develop/ui/views/notifications#icon)を参照してください。

##### ステップ 2.3: アプリケーションのビルドおよび実行 {#step-23-build-and-run-your-application}

アプリケーションをプリビルドすると、Braze Expoプラグインが動作するために必要なネイティブファイルが生成されます。

以下のコードスニペットは、アプリケーションをプリビルドするコマンドです。

```bash
npx expo prebuild
```

[Expoドキュメント](https://docs.expo.dev/workflow/customizing/)の指定に従い、アプリケーションを実行します。設定オプションを変更した場合は、アプリケーションを再度プリビルドして実行する必要があります。

#### 方法 2: React Native CLIの使用 {#method-2-using-react-native-cli}

##### Androidの設定

**ステップ 2.1: Kotlin Gradleプラグインの追加**

以下のコードスニペットは、最上位プロジェクトの`build.gradle`の`buildscript` > `dependencies`にKotlin Gradleプラグインを追加する方法です。

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

これでプロジェクトにKotlinが追加されます。

**ステップ 2.2: Braze SDKの設定**

Brazeサーバーに接続するには、プロジェクトの`res/values`フォルダに`braze.xml`ファイルを作成します。以下のコードスニペットは`braze.xml`の設定例です。API[キー]({{site.baseurl}}/api/identifier_types/)と[エンドポイント]({{site.baseurl}}/api/basics/#endpoints)を実際の値に置き換えてください。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

以下のコードスニペットは、`AndroidManifest.xml`ファイルに必要な権限です。

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
Braze Android SDKバージョン12.2.0以降では、`gradle.properties`ファイルに`importBrazeLocationLibrary=true`を設定することで、android-sdk-locationライブラリーを自動的にプルインできます。
{% endalert %}

**ステップ 2.3: ユーザーセッショントラッキングの実装**

`openSession()`および`closeSession()`への呼び出しは自動的に処理されます。
以下のコードスニペットは、`MainApplication`クラスの`onCreate()`メソッドに追加する内容です。

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**ステップ 2.4: インテント更新の処理**

MainActivityで`android:launchMode`が`singleTask`に設定されている場合、以下のコードスニペットを`MainActivity`クラスに追加してください。

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### iOSの設定

**ステップ 2.5:（オプション）ダイナミックXCFrameworkに関するPodfileの設定**

特定のBrazeライブラリー（例：BrazeUI）をObjective-C++ファイルにインポートするには、`#import`構文を使用する必要があります。Braze Swift SDKのバージョン`7.4.0`以降、バイナリにはこの構文と互換性のある[ダイナミックXCFrameworkとしてのオプションの配布チャネル](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)があります。

この配布チャネルを使用する場合は、PodfileでCocoaPodsのソースの場所を手動で上書きしてください。以下のコードスニペットはサンプルの上書きです。`{your-version}`をインポートする関連バージョンに置き換えてください。

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**ステップ 2.6: Podのインストール**

React Nativeではライブラリーがネイティブプラットフォームに自動でリンクされるため、CocoaPodsを使用してSDKをインストールできます。

以下のコードスニペットは、プロジェクトのルートフォルダからPodをインストールする方法です。

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**ステップ 2.7: Braze SDKの設定**

{% subtabs local %}
{% subtab SWIFT %}

以下のコードスニペットは、`AppDelegate.swift`ファイルの先頭でBraze SDKをインポートする方法です。
```swift
import BrazeKit
import braze_react_native_sdk
```

`application(_:didFinishLaunchingWithOptions:)`メソッドで、API[キー]({{site.baseurl}}/api/identifier_types/)と[エンドポイント]({{site.baseurl}}/api/basics/#endpoints)をアプリの値に置き換えます。次に、設定を使用してBrazeインスタンスを作成し、簡単にアクセスできるよう`AppDelegate`で静的プロパティを作成します。

{% alert note %}
この例では、React Native設定で多くの抽象化を提供する[RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h)の実装を前提としています。アプリに別の設定を使用している場合は、必要に応じて実装を調整してください。
{% endalert %}

以下のコードスニペットは、`AppDelegate.swift`の設定例です。

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

以下のコードスニペットは、`AppDelegate.m`ファイルの先頭でBraze SDKをインポートする方法です。
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

`application:didFinishLaunchingWithOptions:`メソッドで、API[キー]({{site.baseurl}}/api/identifier_types/)と[エンドポイント]({{site.baseurl}}/api/basics/#endpoints)をアプリの値に置き換えます。次に、設定を使用してBrazeインスタンスを作成し、簡単にアクセスできるよう`AppDelegate`で静的プロパティを作成します。

{% alert note %}
この例では、React Native設定で多くの抽象化を提供する[RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h)の実装を前提としています。アプリに別の設定を使用している場合は、必要に応じて実装を調整してください。
{% endalert %}

以下のコードスニペットは、`AppDelegate.m`の設定例です。

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### ステップ 3: SDKの初期化 {#step-3-initialize-the-sdk}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

以下のコードスニペットは、React Nativeコードでライブラリーをインポートする方法です。

```javascript
import Braze from "@braze/react-native-sdk";
```

次に、アプリ識別子APIキーとSDKエンドポイントを指定して`Braze.initialize()`を呼び出し、Brazeインスタンスを作成します。アプリ内でこのメソッドを呼び出す場所については、以下のオプションを参照してください。

#### 標準初期化 {#standard-initialization}

以下のコードスニペットは、`useEffect`内で`Braze.initialize()`を呼び出してアプリ起動時にSDKを初期化する方法です。

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
  }, []);

  return (
    // Your app components
  );
};
```

#### 遅延初期化 {#delayed-initialization}

以下のコードスニペットは、セッション中の後のタイミングまでSDKの初期化を遅延させる方法です。例えば、ユーザーが同意を付与した後やログインを完了した後に初期化できます。

```javascript
function onUserConsent() {
  Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
}
```

{% alert warning %}
iOSでは、`Braze.initialize()`の前に受信したプッシュ通知はキューに入れられ、初期化後に処理されます。Androidでは、SDKの初期化待ち中にプッシュ通知からのディープリンクは解決されません。アプリが起動時の即時ディープリンク処理に依存している場合は、代わりに[標準初期化](#standard-initialization)を使用してください。
{% endalert %}

#### プラットフォーム固有のAPIキー {#platform-specific-api-keys}

以下のコードスニペットは、AndroidとiOSのアプリで異なるAPIキーを使用する場合のプラットフォーム検出の方法です。

```javascript
import { Platform } from "react-native";
import Braze from "@braze/react-native-sdk";

const apiKey = Platform.select({
  android: "YOUR-ANDROID-API-KEY",
  ios: "YOUR-IOS-API-KEY",
}) ?? "";

Braze.initialize(apiKey, "YOUR-SDK-ENDPOINT");
```

#### 再初期化 {#re-initialization}

セッション中に異なるAPIキーとエンドポイントでSDKを再初期化するために、`Braze.initialize()`を複数回呼び出すことができます。呼び出すたびに、前のBrazeインスタンスが破棄され、新しいインスタンスが作成されます。

{% alert important %}
iOSでは、`Braze.initialize()`の前に行われたすべてのSDKメソッド呼び出しは無視されるため、他のBrazeメソッドを使用する前に`Braze.initialize()`を呼び出してください。
{% endalert %}

{% endtab %}
{% tab React Native SDK 19.1.0以前 %}

React Native SDK 19.1.0以前では、ネイティブの初期化はステップ2で行われます。Brazeメソッドを呼び出すには、React Nativeコードでライブラリーをインポートしてください。詳細については、[サンプルプロジェクト](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject)を参照してください。

```javascript
import Braze from "@braze/react-native-sdk";
```

{% endtab %}
{% endtabs %}

### ステップ 4: 統合のテスト（オプション） {#step-4-test-the-integration-optional}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

ダッシュボードでセッション統計を確認することで、SDKが統合されていることを検証できます。いずれかのプラットフォームでアプリケーションを実行すると、ダッシュボード（**Overview**セクション）に新しいセッションが表示されます。

以下のコードスニペットは、アプリ内で特定のユーザーのセッションを開始する方法です。

```javascript
import Braze from "@braze/react-native-sdk";

Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
Braze.changeUser("{some-user-id}");
```

ダッシュボードの**オーディエンス** > **ユーザーを検索**で`{some-user-id}`のユーザーを検索してください。そこで、セッションとデバイスデータが記録されたことを確認できます。

{% endtab %}
{% tab React Native SDK 19.1.0以前 %}

SDKの統合をテストするには、以下のコードスニペットでいずれかのプラットフォームでユーザーの新しいセッションを開始します。

```javascript
Braze.changeUser("userId");
```

以下のコードスニペットは、アプリ起動時にユーザーIDを割り当てる例です。

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

Brazeダッシュボードで[ユーザー検索]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#using-user-search)に移動し、`some-user-id`と一致するIDのユーザーを検索してください。そこで、セッションとデバイスデータが記録されたことを確認できます。

{% endtab %}
{% endtabs %}

## 次のステップ {#next-steps}

Braze SDKを統合した後、一般的なメッセージング機能の実装を開始できます。

- [プッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/)：ユーザーにプッシュ通知を設定して送信します。
- [アプリ内メッセージ]({{site.baseurl}}/developer_guide/in_app_messages/)：アプリ内で状況に即したメッセージを表示します。
- [バナー]({{site.baseurl}}/developer_guide/banners/)：アプリのインターフェイスに常時表示されるバナーを表示します。