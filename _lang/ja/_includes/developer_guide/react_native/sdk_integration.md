## React Native Braze SDKについて {#about-the-react-native-braze-sdk}

React Native Braze SDKを統合すると、基本的な分析機能が提供され、1つのコードベースでiOSとAndroid両方のアプリ内メッセージとContent Cardsを統合できます。

## New Architectureの互換性 {#new-architecture-compatibility}

以下の最小SDKバージョンは、[React NativeのNew Architecture](https://reactnative.dev/docs/the-new-architecture/landing-page)を使用するすべてのアプリと互換性があります。

{% sdk_min_versions reactnative:2.0.1 %}

SDKバージョン6.0.0以降、BrazeはReact Native Turbo Moduleを使用しており、New Architectureとレガシーブリッジアーキテクチャの両方に対応しています。そのため、追加の設定は不要です。

{% alert warning %}
iOSアプリが`RCTAppDelegate`に準拠しており、以前の`AppDelegate`設定に従っている場合は、Turbo Moduleでイベントをサブスクライブする際のクラッシュを防ぐため、[ネイティブ設定を完了する](#reactnative_step-2-complete-native-setup)のサンプルを確認してください。
{% endalert %}

## ReactおよびReact Nativeのバージョン要件 {#react-and-react-native-version-requirements}

BrazeはReact Native SDKがサポートする範囲を超えて、個別のReact最小バージョンを公開していません。SDKを統合するには、React Nativeバージョン0.71以降を使用してください。サポートされているReact Nativeバージョンの完全なリストについては、[React Native SDK GitHubリポジトリ](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support)を参照してください。

React、React Native、またはBraze SDKをアップグレードする際は、デプロイ前にSDKの[CHANGELOG](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)で破壊的変更を確認してください。

## React Native SDKの統合 {#integrating-the-react-native-sdk}

### 前提条件 {#prerequisites}

サポートされているReact Nativeのバージョンとアップグレードガイダンスについては、[ReactおよびReact Nativeのバージョン要件](#react-and-react-native-version-requirements)を参照してください。

### ステップ1：Brazeライブラリを統合する {#step-1-integrate-the-braze-library}

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
### ステップ2：ネイティブセットアップを完了する {#step-2-complete-native-setup}

アプリがExpoを使用している場合は、[Expoプラグインを使用する](#reactnative-using-the-expo-plugin)を参照してください。アプリがピュアReact Nativeを使用している場合は、[React Native CLIを使用する](#reactnative-using-react-native-cli)を参照してください。
各バージョンタブで、Expoプラグインまたは React Native CLIのいずれかのセットアップ方法を選択してください。

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

#### 方法1：Expoプラグインを使用する {#reactnative-using-the-expo-plugin}

##### 2.1 Braze Expoプラグインをインストールする {#21-install-the-braze-expo-plugin}

Braze Expoプラグインのバージョンが4.1.0以上であることを確認してください。サポートされているバージョンの完全なリストについては、[Braze Expoプラグインリポジトリ](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support)を参照してください。

以下のコードスニペットは、Braze Expoプラグインをインストールするコマンドを示しています：

```bash
npx expo install @braze/expo-plugin
```

##### 2.2 プラグインをapp.jsonに追加する {#22-add-the-plugin-to-your-appjson}

`app.json`にBraze Expoプラグインを追加します。APIキーとエンドポイントはここでは設定しません。JavaScriptから`Braze.initialize()`を通じてランタイム時に提供します。実装のニーズに基づいて、以下のオプション設定パラメーターを追加してください：

| メソッド | 型 | 説明 |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enableBrazeIosPush`                          | boolean | iOSのみ。Brazeを使用してiOSでプッシュ通知を処理するかどうか。                       |
| `enableFirebaseCloudMessaging`                | boolean | Androidのみ。プッシュ通知にFirebase Cloud Messagingを使用するかどうか。             |
| `firebaseCloudMessagingSenderId`              | string  | Androidのみ。Firebase Cloud MessagingのセンダーID。                                    |
| `sessionTimeout`                              | integer | アプリケーションのBrazeセッションタイムアウト（秒単位）。                                                                                               |
| `enableSdkAuthentication`                     | boolean | [SDK認証]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication)機能を有効にするかどうか。      |
| `logLevel`                                    | integer | アプリケーションのログレベル。デフォルトのログレベルは8で、最小限の情報をログに記録します。デバッグ用の詳細ログを有効にするには、ログレベル0を使用します。    |
| `minimumTriggerIntervalInSeconds`             | integer | トリガー間の最小時間間隔（秒単位）。デフォルトは30秒です。                                                                           |
| `enableAutomaticLocationCollection`           | boolean | 自動位置情報収集を有効にするかどうか（ユーザーが許可した場合）。                                                                                  |
| `enableGeofence`                              | boolean | ジオフェンスを有効にするかどうか。                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | ジオフェンスリクエストを自動的に行うかどうか。                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | iOSのみ。ユーザーがアプリ内メッセージの外側をクリックした場合にモーダルアプリ内メッセージを閉じるかどうか。                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Androidのみ。Braze SDKがプッシュディープリンクを自動的に処理するかどうか。                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Androidのみ。プッシュ通知のテキストコンテンツを`android.text.Html.fromHtml`を使用してHTMLとして解釈・レンダリングするかどうかを設定します。        |
| `androidNotificationAccentColor`              | string  | Androidのみ。Android通知のアクセントカラーを設定します。                                                                                                |
| `androidNotificationLargeIcon`                | string  | Androidのみ。Android通知のラージアイコンを設定します。                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Androidのみ。Android通知のスモールアイコンを設定します。                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | iOSのみ。アプリ起動時にプッシュ権限のプロンプトを自動的に表示するかどうか。                                                          |
| `enableBrazeIosRichPush`                      | boolean | iOSのみ。iOS向けのリッチプッシュ機能を有効にするかどうか。                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | iOSのみ。iOS向けのBraze Push Storiesを有効にするかどうか。                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | iOSのみ。iOS Push Storiesに使用するアプリグループ。                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | iOSのみ。デバイスIDにランダムに生成されたUUIDを使用するかどうか。                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | iOSのみ。SDKがユニバーサルリンクを自動的に認識してシステムメソッドに転送するかどうかを指定します（デフォルト：`false`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2.2 プラグインをapp.jsonに追加する" }

以下のコードスニペットは、`app.json`の設定例を示しています：

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

`androidNotificationLargeIcon`と`androidNotificationSmallIcon`を使用する場合は、アイコンを適切に表示するために以下のベストプラクティスに従ってください：

**アイコンの配置とフォーマット**

Braze Expoプラグインでカスタムプッシュ通知アイコンを使用するには：

1. 「アイコン要件」に記載されている要件に従ってアイコンファイルを作成します。
2. プロジェクトのAndroidネイティブディレクトリ`android/app/src/main/res/drawable-<density>/`に配置します。
   たとえば、`android/app/src/main/res/drawable-mdpi/`や`android/app/src/main/res/drawable-hdpi/`を使用します。
3. あるいは、React Nativeディレクトリでアセットを管理している場合は、Expoの[app.jsonアイコン設定](https://docs.expo.dev/versions/latest/config/app/#icon)を使用するか、[Expo設定プラグイン](https://docs.expo.dev/config-plugins/introduction/)を作成してプレビルド時にアイコンをAndroid drawableフォルダーにコピーできます。

Braze Expoプラグインは、Androidのdrawableリソースシステムを使用してこれらのアイコンを参照します。

**アイコン要件**

- **スモールアイコン：** 透明な背景に白いシルエットである必要があります（これはAndroidプラットフォームの要件です）
- **ラージアイコン：** フルカラー画像を使用できます。
- **フォーマット：** PNG形式を推奨します。
- **命名規則：** 小文字、数字、アンダースコアのみを使用してください（例：`my_large_icon.png`）

**app.jsonでの設定**

以下のコードスニペットは、`@drawable/`プレフィックスを使用して`app.json`でAndroid通知アイコンを参照する方法を示しています：

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
アイコンを参照する際に、相対ファイルパス（`src/assets/images/icon.png`など）を使用したり、ファイル拡張子を含めたりしないでください。Expoプラグインでは、プレビルドプロセス後にAndroidネイティブフォルダー内のアイコンを正しく見つけるために`@drawable/`プレフィックスが必要です。
{% endalert %}

**仕組み**

Braze Expoプラグインは、Androidの`drawable`ディレクトリからアイコンファイルを参照します。`npx expo prebuild`を実行すると、Expoはネイティブのandroidプロジェクト構造を生成します。アイコンは、ビルドプロセスの前にAndroidの`drawable`フォルダー内に存在する必要があります（手動で配置するか、設定プラグインを通じてコピーします）。プラグインはその後、これらのdrawableリソースを名前（パスや拡張子なし）で使用するようにBraze SDKを設定します。これが、設定で`@drawable/`プレフィックスが必要な理由です。

Android通知アイコンの詳細については、[Androidの通知アイコンガイドライン](https://developer.android.com/develop/ui/views/notifications#icon)を参照してください。

##### 2.3 アプリケーションをビルドして実行する {#23-build-and-run-your-application}

アプリケーションをプレビルドすると、Braze Expoプラグインが動作するために必要なネイティブファイルが生成されます。

以下のコードスニペットは、アプリケーションをプレビルドするコマンドを示しています：

```bash
npx expo prebuild
```

[Expoドキュメント](https://docs.expo.dev/workflow/customizing/)の指定に従ってアプリケーションを実行します。設定オプションを変更した場合は、アプリケーションを再度プレビルドして実行してください。

#### 方法2：React Native CLIを使用する {#reactnative-using-react-native-cli}

##### Androidのセットアップ {#set-up-android}

**2.1 Kotlin Gradleプラグインを追加する**

以下のコードスニペットは、トップレベルプロジェクトの`build.gradle`の`buildscript` > `dependencies`にKotlin Gradleプラグインを追加する方法を示しています：

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

これによりプロジェクトにKotlinが追加されます。

**2.2 Braze SDKを設定する**

プロジェクトの`res/values`フォルダーに`braze.xml`ファイルを作成します。APIキーとエンドポイントはJavaScriptからランタイム時に提供されるため、このファイルでは不要です。以下のコードスニペットは、`com_braze_enable_delayed_initialization`を使用して遅延初期化を有効にする方法を示しています：

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
</resources>
```

{% alert note %}
`braze.xml`にその他のネイティブ設定値（プッシュ、セッションタイムアウト、ログ設定など）を追加することもできます。これらはJavaScriptから`Braze.initialize()`が呼び出されると自動的に適用されます。
{% endalert %}

以下のコードスニペットは、`AndroidManifest.xml`ファイルに必要な権限を示しています：

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
Braze Android SDKバージョン12.2.0以降では、`gradle.properties`ファイルで`importBrazeLocationLibrary=true`を設定することで、android-sdk-locationライブラリを自動的に取り込むことができます。
{% endalert %}

**2.3 ユーザーセッショントラッキングを実装する**

`openSession()`と`closeSession()`の呼び出しは自動的に処理されます。
以下のコードスニペットは、`MainApplication`クラスの`onCreate()`メソッドに追加する内容を示しています：

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

**2.4 インテントの更新を処理する**

MainActivityの`android:launchMode`が`singleTask`に設定されている場合、以下のコードスニペットは`MainActivity`クラスに追加する内容を示しています：

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

##### iOSのセットアップ {#set-up-ios}

**2.5（オプション）動的XCFrameworks用にPodfileを設定する**

BrazeUIなどの特定のBrazeライブラリをObjective-C++ファイルにインポートするには、`#import`構文を使用する必要があります。Braze Swift SDKのバージョン`7.4.0`以降、バイナリには[動的XCFrameworksとしてのオプションの配布チャネル](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)があり、この構文と互換性があります。

この配布チャネルを使用する場合は、PodfileでCocoaPodsのソースロケーションを手動でオーバーライドしてください。以下のサンプルを参照し、`{your-version}`をインポートしたい関連バージョンに置き換えてください：

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**2.6 Podをインストールする**

React Nativeはライブラリをネイティブプラットフォームに自動的にリンクするため、CocoaPodsを使用してSDKをインストールできます。

以下のコードスニペットは、プロジェクトのルートフォルダーからPodをインストールする方法を示しています：

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**2.7 Braze SDKを設定する**

`AppDelegate`で`BrazeReactInitializer.configure`を使用してネイティブ設定を登録します。提供するクロージャーは保存され、JavaScriptから`Braze.initialize(apiKey, endpoint)`が呼び出されたときに適用されます。

{% subtabs local %}
{% subtab SWIFT %}

以下のコードスニペットは、`AppDelegate.swift`ファイルの先頭でBraze SDKをインポートする方法を示しています：

```swift
import BrazeKit
import braze_react_native_sdk
```

`application(_:didFinishLaunchingWithOptions:)`メソッドで、`BrazeReactInitializer.configure`を使用してネイティブ設定を登録します。ここではAPIキーやエンドポイントを設定しないでください。それらはJavaScriptから`Braze.initialize()`を通じて提供されます。

- **`configure`クロージャー**：`Braze.Configuration`を受け取り、ネイティブ設定プロパティ（ログ、プッシュ、セッションなど）を設定できます。
- **`postInitialization`クロージャー**（オプション）：作成後のライブBrazeインスタンスを受け取り、インスタンスを必要とするセットアップ（参照の保存やデリゲートの設定など）に使用します。

以下のコードスニペットは、`BrazeReactInitializer.configure`を使用した`AppDelegate.swift`の実装例を示しています：

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

以下のコードスニペットは、`AppDelegate.m`ファイルの先頭でBraze SDKをインポートする方法を示しています：

```objc
@import BrazeKit;
@import braze_react_native_sdk;
```

`application:didFinishLaunchingWithOptions:`メソッドで、`BrazeReactInitializer`を使用してネイティブ設定を登録します。ここではAPIキーやエンドポイントを設定しないでください。それらはJavaScriptから`Braze.initialize()`を通じて提供されます。

以下のコードスニペットは、`BrazeReactInitializer`を使用した`AppDelegate.m`の実装例を示しています：

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
`Braze.initialize()`を再度呼び出すと、同じ`configure`と`postInitialization`ブロックが新しいBrazeインスタンスに適用されます。
{% endalert %}

{% endtab %}
{% tab React Native SDK 19.1.0以前 %}

#### 方法1：Expoプラグインを使用する {#method-1-using-the-expo-plugin}

##### ステップ2.1：Braze Expoプラグインをインストールする {#step-21-install-the-braze-expo-plugin}

Braze React Native SDKのバージョンが1.37.0以上であることを確認してください。サポートされているバージョンの完全なリストについては、[Braze React Nativeリポジトリ](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support)を参照してください。

以下のコードスニペットは、Braze Expoプラグインをインストールするコマンドを示しています：

```bash
npx expo install @braze/expo-plugin
```

##### ステップ2.2：プラグインをapp.jsonに追加する {#step-22-add-the-plugin-to-your-appjson}

`app.json`にBraze Expoプラグインを追加します。以下の設定オプションを指定できます：

| メソッド | 型 | 説明 |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | string  | 必須。Androidアプリケーションの[APIキー]({{site.baseurl}}/api/identifier_types)。Brazeダッシュボードの**設定の管理**に配置されています。 |
| `iosApiKey`                                   | string  | 必須。iOSアプリケーションの[APIキー]({{site.baseurl}}/api/identifier_types)。Brazeダッシュボードの**設定の管理**に配置されています。     |
| `baseUrl`                                     | string  | 必須。アプリケーションの[SDKエンドポイント]({{site.baseurl}}/api/basics#endpoints)。Brazeダッシュボードの**設定の管理**に配置されています。    |
| `enableBrazeIosPush`                          | boolean | iOSのみ。Brazeを使用してiOSでプッシュ通知を処理するかどうか。React Native SDK v1.38.0およびExpo Plugin v0.4.0で導入されました。                       |
| `enableFirebaseCloudMessaging`                | boolean | Androidのみ。プッシュ通知にFirebase Cloud Messagingを使用するかどうか。React Native SDK v1.38.0およびExpo Plugin v0.4.0で導入されました。             |
| `firebaseCloudMessagingSenderId`              | string  | Androidのみ。Firebase Cloud MessagingのセンダーID。React Native SDK v1.38.0およびExpo Plugin v0.4.0で導入されました。                                    |
| `sessionTimeout`                              | integer | アプリケーションのBrazeセッションタイムアウト（秒単位）。                                                                                               |
| `enableSdkAuthentication`                     | boolean | [SDK認証]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication)機能を有効にするかどうか。      |
| `logLevel`                                    | integer | アプリケーションのログレベル。デフォルトのログレベルは8で、最小限の情報をログに記録します。デバッグ用の詳細ログを有効にするには、ログレベル0を使用します。    |
| `minimumTriggerIntervalInSeconds`             | integer | トリガー間の最小時間間隔（秒単位）。デフォルトは30秒です。                                                                           |
| `enableAutomaticLocationCollection`           | boolean | 自動位置情報収集を有効にするかどうか（ユーザーが許可した場合）。                                                                                  |
| `enableGeofence`                              | boolean | ジオフェンスを有効にするかどうか。                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | ジオフェンスリクエストを自動的に行うかどうか。                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | iOSのみ。ユーザーがアプリ内メッセージの外側をクリックした場合にモーダルアプリ内メッセージを閉じるかどうか。                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Androidのみ。Braze SDKがプッシュディープリンクを自動的に処理するかどうか。                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Androidのみ。プッシュ通知のテキストコンテンツを`android.text.Html.fromHtml`を使用してHTMLとして解釈・レンダリングするかどうかを設定します。        |
| `androidNotificationAccentColor`              | string  | Androidのみ。Android通知のアクセントカラーを設定します。                                                                                                |
| `androidNotificationLargeIcon`                | string  | Androidのみ。Android通知のラージアイコンを設定します。                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Androidのみ。Android通知のスモールアイコンを設定します。                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | iOSのみ。アプリ起動時にプッシュ権限のプロンプトを自動的に表示するかどうか。                                                          |
| `enableBrazeIosRichPush`                      | boolean | iOSのみ。iOS向けのリッチプッシュ機能を有効にするかどうか。                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | iOSのみ。iOS向けのBraze Push Storiesを有効にするかどうか。                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | iOSのみ。iOS Push Storiesに使用するアプリグループ。                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | iOSのみ。デバイスIDにランダムに生成されたUUIDを使用するかどうか。                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | iOSのみ。SDKがユニバーサルリンクを自動的に認識してシステムメソッドに転送するかどうかを指定します（デフォルト：`false`）。有効にすると、SDKは[アプリでのユニバーサルリンクのサポート](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/)で定義されたシステムメソッドにユニバーサルリンクを自動的に転送します。React Native SDK v11.1.0およびExpo Plugin v3.2.0で導入されました。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2.2：プラグインをapp.jsonに追加する" }

以下のコードスニペットは、`app.json`の設定例を示しています：

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

`androidNotificationLargeIcon`と`androidNotificationSmallIcon`を使用する場合は、アイコンを適切に表示するために以下のベストプラクティスに従ってください：

**アイコンの配置とフォーマット**

Braze Expoプラグインでカスタムプッシュ通知アイコンを使用するには：

1. 「アイコン要件」に記載されている要件に従ってアイコンファイルを作成します。
2. プロジェクトのAndroidネイティブディレクトリ`android/app/src/main/res/drawable-<density>/`に配置します（例：`android/app/src/main/res/drawable-mdpi/`、`drawable-hdpi/`など）。
3. あるいは、React Nativeディレクトリでアセットを管理している場合は、Expoの[app.jsonアイコン設定](https://docs.expo.dev/versions/latest/config/app/#icon)を使用するか、[Expo設定プラグイン](https://docs.expo.dev/config-plugins/introduction/)を作成してプレビルド時にアイコンをAndroid drawableフォルダーにコピーできます。

Braze Expoプラグインは、Androidのdrawableリソースシステムを使用してこれらのアイコンを参照します。

**アイコン要件**

- **スモールアイコン：** 透明な背景に白いシルエットである必要があります（これはAndroidプラットフォームの要件です）
- **ラージアイコン：** フルカラー画像を使用できます。
- **フォーマット：** PNG形式を推奨します。
- **命名規則：** 小文字、数字、アンダースコアのみを使用してください（例：`my_large_icon.png`）

**app.jsonでの設定**

以下のコードスニペットは、`@drawable/`プレフィックスを使用して`app.json`でAndroid通知アイコンを参照する方法を示しています：

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
アイコンを参照する際に、相対ファイルパス（`src/assets/images/icon.png`など）を使用したり、ファイル拡張子を含めたりしないでください。Expoプラグインでは、プレビルドプロセス後にAndroidネイティブフォルダー内のアイコンを正しく見つけるために`@drawable/`プレフィックスが必要です。
{% endalert %}

**仕組み**

Braze Expoプラグインは、Androidの`drawable`ディレクトリからアイコンファイルを参照します。`npx expo prebuild`を実行すると、Expoはネイティブのandroidプロジェクト構造を生成します。アイコンは、ビルドプロセスの前にAndroidの`drawable`フォルダー内に存在する必要があります（手動で配置するか、設定プラグインを通じてコピーします）。プラグインはその後、これらのdrawableリソースを名前（パスや拡張子なし）で使用するようにBraze SDKを設定します。これが、設定で`@drawable/`プレフィックスが必要な理由です。

Android通知アイコンの詳細については、[Androidの通知アイコンガイドライン](https://developer.android.com/develop/ui/views/notifications#icon)を参照してください。

##### ステップ2.3：アプリケーションをビルドして実行する {#step-23-build-and-run-your-application}

アプリケーションをプレビルドすると、Braze Expoプラグインが動作するために必要なネイティブファイルが生成されます。

以下のコードスニペットは、アプリケーションをプレビルドするコマンドを示しています：

```bash
npx expo prebuild
```

[Expoドキュメント](https://docs.expo.dev/workflow/customizing/)の指定に従ってアプリケーションを実行します。設定オプションを変更した場合は、アプリケーションを再度プレビルドして実行する必要があります。

#### 方法2：React Native CLIを使用する {#method-2-using-react-native-cli}

##### Androidのセットアップ

**ステップ2.1：Kotlin Gradleプラグインを追加する**

以下のコードスニペットは、トップレベルプロジェクトの`build.gradle`の`buildscript` > `dependencies`にKotlin Gradleプラグインを追加する方法を示しています：

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

これによりプロジェクトにKotlinが追加されます。

**ステップ2.2：Braze SDKを設定する**

Brazeサーバーに接続するには、プロジェクトの`res/values`フォルダーに`braze.xml`ファイルを作成します。以下のコードスニペットは、`braze.xml`の設定例を示しています。API[キー]({{site.baseurl}}/api/identifier_types)と[エンドポイント]({{site.baseurl}}/api/basics#endpoints)をご自身の値に置き換えてください：

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

以下のコードスニペットは、`AndroidManifest.xml`ファイルに必要な権限を示しています：

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
Braze Android SDKバージョン12.2.0以降では、`gradle.properties`ファイルで`importBrazeLocationLibrary=true`を設定することで、android-sdk-locationライブラリを自動的に取り込むことができます。
{% endalert %}

**ステップ2.3：ユーザーセッショントラッキングを実装する**

`openSession()`と`closeSession()`の呼び出しは自動的に処理されます。
以下のコードスニペットは、`MainApplication`クラスの`onCreate()`メソッドに追加する内容を示しています：

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

**ステップ2.4：インテントの更新を処理する**

MainActivityの`android:launchMode`が`singleTask`に設定されている場合、以下のコードスニペットは`MainActivity`クラスに追加する内容を示しています：

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

##### iOSのセットアップ

**ステップ2.5：（オプション）動的XCFrameworks用にPodfileを設定する**

BrazeUIなどの特定のBrazeライブラリをObjective-C++ファイルにインポートするには、`#import`構文を使用する必要があります。Braze Swift SDKのバージョン`7.4.0`以降、バイナリには[動的XCFrameworksとしてのオプションの配布チャネル](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)があり、この構文と互換性があります。

この配布チャネルを使用する場合は、PodfileでCocoaPodsのソースロケーションを手動でオーバーライドしてください。以下のコードスニペットはサンプルのオーバーライドを示しています。`{your-version}`をインポートしたい関連バージョンに置き換えてください：

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**ステップ2.6：Podをインストールする**

React Nativeはライブラリをネイティブプラットフォームに自動的にリンクするため、CocoaPodsを使用してSDKをインストールできます。

以下のコードスニペットは、プロジェクトのルートフォルダーからPodをインストールする方法を示しています：

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**ステップ2.7：Braze SDKを設定する**

{% subtabs local %}
{% subtab SWIFT %}

以下のコードスニペットは、`AppDelegate.swift`ファイルの先頭でBraze SDKをインポートする方法を示しています：
```swift
import BrazeKit
import braze_react_native_sdk
```

`application(_:didFinishLaunchingWithOptions:)`メソッドで、API[キー]({{site.baseurl}}/api/identifier_types)と[エンドポイント]({{site.baseurl}}/api/basics#endpoints)をアプリの値に置き換えます。次に、設定を使用してBrazeインスタンスを作成し、`AppDelegate`にスタティックプロパティを作成してアクセスしやすくします。

{% alert note %}
この例では、React Nativeのセットアップで多くの抽象化を提供する[RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h)の実装を前提としています。アプリで異なるセットアップを使用している場合は、必要に応じて実装を調整してください。
{% endalert %}

以下のコードスニペットは、`AppDelegate.swift`のセットアップ例を示しています：

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

以下のコードスニペットは、`AppDelegate.m`ファイルの先頭でBraze SDKをインポートする方法を示しています：
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

`application:didFinishLaunchingWithOptions:`メソッドで、API[キー]({{site.baseurl}}/api/identifier_types)と[エンドポイント]({{site.baseurl}}/api/basics#endpoints)をアプリの値に置き換えます。次に、設定を使用してBrazeインスタンスを作成し、`AppDelegate`にスタティックプロパティを作成してアクセスしやすくします。

{% alert note %}
この例では、React Nativeのセットアップで多くの抽象化を提供する[RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h)の実装を前提としています。アプリで異なるセットアップを使用している場合は、必要に応じて実装を調整してください。
{% endalert %}

以下のコードスニペットは、`AppDelegate.m`のセットアップ例を示しています：

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

### ステップ3：SDKを初期化する {#step-3-initialize-the-sdk}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

以下のコードスニペットは、React Nativeコードでライブラリをインポートする方法を示しています：

```javascript
import Braze from "@braze/react-native-sdk";
```

{% alert note %}
React Native SDK 19.2.0以降では、React NativeレイヤーまたはネイティブのiOS・Androidレイヤーから Brazeを初期化できます。React Nativeレイヤーから初期化することで[遅延初期化](#delayed-initialization)を使用でき、同意やログインなどのイベント後にSDKを開始できます。アプリが現在ネイティブレイヤーでBrazeを初期化している場合は、アップグレード時にそのセットアップを維持できます。各セットアップで通知がどのように動作するかを確認するには、[コールドスタート時のプッシュ通知](#push-notifications-on-cold-start)を参照してください。
{% endalert %}

次に、アプリ識別子APIキーとSDKエンドポイントを使用して`Braze.initialize()`を呼び出し、Brazeインスタンスを作成します。アプリフローのどこでこのメソッドを呼び出すかについては、以下のオプションを参照してください。

#### 標準的な初期化 {#standard-initialization}

以下のコードスニペットは、`useEffect`で`Braze.initialize()`を呼び出してアプリ起動時にSDKを初期化する方法を示しています：

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

以下のコードスニペットは、SDK初期化をセッションの後半まで遅延する方法を示しています。たとえば、ユーザーが同意を付与するかログインを完了した後に初期化します：

```javascript
function onUserConsent() {
  Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
}
```

{% alert warning %}
iOSでは、`Braze.initialize()`の前に受信したプッシュ通知はキューに入れられ、初期化後に処理されます。Androidでは、SDKが初期化を待機している間、Brazeはプッシュ通知からのディープリンクを解決しません。通知がアプリを起動する場合に通知を動作させ続けるには、[コールドスタート時のプッシュ通知](#push-notifications-on-cold-start)を参照してください。
{% endalert %}

#### プラットフォーム固有のAPIキー {#platform-specific-api-keys}

以下のコードスニペットは、AndroidアプリとiOSアプリで異なるAPIキーを使用する場合のプラットフォーム検出方法を示しています：

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

`Braze.initialize()`を複数回呼び出して、セッション中に異なるAPIキーとエンドポイントでSDKを再初期化できます。各呼び出しは前のBrazeインスタンスを破棄し、新しいインスタンスを作成します。

{% alert important %}
`Braze.initialize()`の前に行われたすべてのSDKメソッド呼び出しはiOSでは無視されるため、他のBrazeメソッドを使用する前に`Braze.initialize()`を呼び出してください。
{% endalert %}

#### コールドスタート時のプッシュ通知 {#push-notifications-on-cold-start}

通知がアプリを終了状態から起動する場合、Brazeは React Nativeが読み込まれる前にネイティブレイヤーに通知ペイロードを保存します。このため、React Nativeレイヤーからの初期化は、ペイロードがアプリに届くかどうかには影響しません。これらの通知を処理するには、ネイティブフックを追加し、React Nativeコードでペイロードを読み取ります。

Androidでは、`MainActivity`クラスの`onCreate()`メソッドで`BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)`を呼び出します：

```kotlin
import com.braze.reactbridge.BrazeReactUtils

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)
}
```

iOSでは、`AppDelegate`の`application(_:didFinishLaunchingWithOptions:)`メソッドで`populateInitialPayload(fromLaunchOptions:)`を呼び出します：

```swift
if let launchOptions {
  BrazeReactUtils.sharedInstance().populateInitialPayload(fromLaunchOptions: launchOptions)
}
```

次に、React Nativeコードでペイロードを読み取ります：

```javascript
Braze.getInitialPushPayload((pushPayload) => {
  if (pushPayload) {
    // Handle the notification, such as navigating to the pushPayload.url value
  }
});
```

{% alert important %}
Androidで遅延初期化が有効な場合、Brazeは通知内のディープリンクを解決する代わりにメインアクティビティを開き、通知データをそのアクティビティに渡します。`Braze.getInitialPushPayload()`からの`url`値を使用して、React Nativeコードでナビゲーションを処理してください。
{% endalert %}

プッシュ登録設定は、両方の初期化ロケーションのネイティブ設定に残り、`Braze.initialize()`の実行時にBrazeが適用します：

- Androidでは、`braze.xml`で`com_braze_firebase_cloud_messaging_registration_enabled`と`com_braze_firebase_cloud_messaging_sender_id`を設定します。
- iOSでは、`BrazeReactInitializer.configure`に渡す`configure`クロージャー内の設定オブジェクトで`push`プロパティを設定します。

アプリが終了状態から通知で起動された際のディープリンクに依存している場合は、React Native SDK 21.1.0以降を使用してください。これらのバージョンには、Androidでの初期プッシュペイロードのキャプチャとプッシュディープリンクの解決に関する修正が含まれています。変更の完全なリストについては、[React Native SDKの変更ログ](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)を参照してください。

{% endtab %}
{% tab React Native SDK 19.1.0以前 %}

React Native SDK 19.1.0以前では、ネイティブ初期化はステップ2で行われます。BrazeメソッドをＲeact Nativeコードでインポートして呼び出します。詳細については、[サンプルプロジェクト](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject)を確認してください。

```javascript
import Braze from "@braze/react-native-sdk";
```

{% endtab %}
{% endtabs %}

### ステップ4：統合をテストする（オプション） {#step-4-test-the-integration-optional}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

ダッシュボードでセッション統計を確認することで、SDKが統合されていることを検証できます。いずれかのプラットフォームでアプリケーションを実行すると、ダッシュボード（**概要**セクション）に新しいセッションが表示されるはずです。

以下のコードスニペットは、アプリで特定のユーザーのセッションを開く方法を示しています：

```javascript
import Braze from "@braze/react-native-sdk";

Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
Braze.changeUser("{some-user-id}");
```

ダッシュボードの**オーディエンス** > **ユーザー検索**で`{some-user-id}`のユーザーを検索します。そこで、セッションおよびデバイスデータがログに記録されていることを確認できます。

{% endtab %}
{% tab React Native SDK 19.1.0以前 %}

SDK統合をテストするために、以下のコードスニペットは、いずれかのプラットフォームでユーザーの新しいセッションを開始する方法を示しています。

```javascript
Braze.changeUser("userId");
```

以下のコードスニペットは、アプリ起動時にユーザーIDを割り当てる例を示しています：

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

Brazeダッシュボードで、[ユーザー検索]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search)に移動し、`some-user-id`に一致するIDのユーザーを検索します。そこで、セッションおよびデバイスデータがログに記録されていることを確認できます。

{% endtab %}
{% endtabs %}

## Jestを使用したテスト {#testing-with-jest}

Braze SDKをインポートするReact Nativeのユニットテストでは、ネイティブモジュールとBraze Turbo Moduleのモックが必要です。[Braze React Native SDKリポジトリ](https://github.com/braze-inc/braze-react-native-sdk)では、[`__tests__/jest.setup.js`](https://github.com/braze-inc/braze-react-native-sdk/blob/master/__tests__/jest.setup.js)にリファレンスとなるJestセットアップが含まれています。このファイル（または適宜調整したコピー）をJest設定の`setupFiles`に追加することで、Braze APIを呼び出すコンポーネントのテスト時に`NativeEventEmitter`、`TurboModuleRegistry`、および`BrazeReactBridge`がモックされます。

## 次のステップ {#next-steps}

Braze SDKを統合した後、一般的なメッセージング機能の実装を開始できます。

- [プッシュ通知]({{site.baseurl}}/developer_guide/push_notifications)：ユーザーにプッシュ通知を設定して送信します。
- [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages)：アプリ内に文脈に応じたメッセージを表示します。
- [バナー]({{site.baseurl}}/developer_guide/banners)：アプリのインターフェイスに常駐バナーを表示します。