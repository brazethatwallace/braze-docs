---
nav_title: React Native SDK
article_title: React Native SDKリポジトリガイド
page_order: 7
description: "GitHubからミラーリングされたBraze React Native SDK READMEリファレンスです。"
---

<!-- BEGIN GENERATED README CONTENT -->
# React Native SDKリポジトリガイド {#react-native-sdk-repository-guide}

## Braze React Native SDKについて {#about-the-braze-react-native-sdk}

Braze React Native SDKは、iOSおよびAndroidアプリをBrazeに接続します。ユーザープロファイル、メッセージングサーフェス、分析、フィーチャーフラグに対応しています。ネイティブの[Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk)と[Braze Android SDK](https://github.com/braze-inc/braze-android-sdk)をJavaScript APIでラップしています。

**初期化はJavaScriptで行います。** ネイティブの設定（プッシュ、ログ、デリゲート）はAndroidリソースとiOSの`AppDelegate`で行い、JavaScriptから`Braze.initialize(apiKey, endpoint)`を呼び出してSDKを開始します。これにより、SDKの初期化タイミングと使用する認証情報を完全にコントロールできます。初期化後、必要に応じて他のSDKメソッド（例：`changeUser`、`logCustomEvent`）を呼び出します。

### できること {#what-you-can-do}

- **ユーザー管理**：ユーザーの識別、プロファイルフィールド、カスタム属性、エイリアス、購読グループの設定
- **アプリ内メッセージ**：デフォルトのBraze UIまたはサブスクリプションとログAPIによるカスタムハンドリング
- **Content Cards**：デフォルトのフィードUI、またはカードを取得して独自のUIを構築
- **バナー**：`BrazeBannerView`を含むプレースメントベースのHTMLバナー
- **プッシュ通知**：権限プロンプト、トークン登録、ペイロードリスナー（**プッシュ通知**を参照）
- **フィーチャーフラグ**：リフレッシュ、プロパティの読み取り、インプレッションの記録
- **分析**：カスタムイベント、購入、即時フラッシュ
- **SDKコントロール**：SDKの有効化/無効化、ローカルデータの消去、SDK認証署名

## 前提条件 {#prerequisites}

- Brazeアカウント（アプリAPIキーとSDKエンドポイントが必要）
- **React Native**開発環境（[React Native環境セットアップ](https://reactnative.dev/docs/set-up-your-environment)）
- **iOS**：Xcode、CocoaPods（`cd ios && pod install`）
- **Android**：Android Studio / Gradle、React Nativeテンプレートで必要なKotlin Gradleプラグイン
- **プッシュ**（使用する場合）：FCM（Android）およびAPNs（iOS）のセットアップ（[プッシュ通知のドキュメント](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/push_notifications/)を参照）

ダッシュボードでの認証情報の場所については、[統合の概要](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native)を参照してください。

## インストール {#installation}

``` bash
npm install @braze/react-native-sdk
# or:
# yarn add @braze/react-native-sdk
```

---

## クイックスタート {#quick-start}

このセクションでは、Braze React Native SDKを初期化するために必要な最小限の設定を説明します。

1. **インストール**からnpmパッケージをインストールします。
2. AndroidとiOSの**ネイティブセットアップ**を完了します（設定、権限、必要に応じてプッシュ）。
3. JavaScriptからSDKを初期化して使用を開始します：

``` typescript
import Braze from "@braze/react-native-sdk";

// Initialize the SDK — call early in your app lifecycle (e.g. in a useEffect).
// The API key and endpoint are passed from JavaScript; native configuration
// (push, logging, etc.) is applied automatically from your native setup.
Braze.initialize("<YOUR_API_KEY>", "<YOUR_SDK_ENDPOINT>");

Braze.changeUser("user-123");
Braze.logCustomEvent("button_clicked", { screen: "home" });
```

TypeScriptの型定義はパッケージに同梱されています（GitHubの`src/index.d.ts`）。

異なる認証情報で`Braze.initialize`を再度呼び出すと、現在のインスタンスが破棄されて再作成されるため、セッション中の再初期化がサポートされています。

---

## ネイティブセットアップ {#native-setup}

> **信頼できる情報源：** ステップごとの画面、Gradle/CocoaPodsの変更、およびAndroid XMLキーの完全なリストは、[Braze React Nativeデベロッパーガイド](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native)に記載されています。このセクションのスニペットは最小限の例です。

### Android

- テンプレートにまだ含まれていない場合は、ルートの`build.gradle`に**Kotlin Gradleプラグイン**を追加します（バージョンはReact Nativeのバージョンに依存します）。
- `res/values`に設定を含む`braze.xml`リソースファイルを追加します。遅延初期化を有効にして、SDKがJavaScriptからの`Braze.initialize()`を待ってから開始するようにします。その他の設定値（プッシュ、セッションタイムアウトなど）は引き続きこのファイルから読み取られ、初期化時に適用されます。
- `AndroidManifest.xml`に`INTERNET`や`ACCESS_NETWORK_STATE`などの基本的な権限があることを確認します。
- プッシュについては、FCM統合およびドキュメントに記載されているBraze固有の送信者ID/登録フラグを完了します。

``` xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- Enable delayed initialization so the SDK starts when
       Braze.initialize() is called from JavaScript. -->
  <bool name="com_braze_enable_delayed_initialization">true</bool>

  <!-- Additional native configuration (applied at initialization time) -->
  <bool name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">YOUR_SENDER_ID</string>
</resources>
```

{% alert note %}
** APIキーとエンドポイントは`braze.xml`では設定しなくなりました。JavaScriptから`Braze.initialize(apiKey, endpoint)`を介して渡されます。
{% endalert %}
### iOS

``` bash
cd ios && pod install
```

`AppDelegate`で`BrazeReactInitializer.configure`を使用して、ネイティブ設定を登録します。提供するクロージャは保存され、JavaScriptから`Braze.initialize(apiKey, endpoint)`が呼び出されたときに適用されます。

``` swift
import BrazeKit
import braze_react_native_sdk

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    // Register native configuration for when JS calls Braze.initialize().
    BrazeReactInitializer.configure { config in
      config.logger.level = .info
      config.push.automation = true
    } postInitialization: { braze in
      AppDelegate.braze = braze
    }

    // ... React Native setup
    return true
  }
}
```

- **`configure`クロージャ**：`Braze.Configuration`を受け取り、ネイティブ設定プロパティ（ロギング、プッシュ、セッションなど）を設定できます。APIキーとエンドポイントはJavaScriptから提供されるため、ここでは設定しません。
- **`postInitialization`クロージャ**（*オプション*）：作成後のライブ`Braze`インスタンスを受け取り、インスタンスが必要なセットアップ（参照の保存、デリゲートの設定など）に使用します。

{% alert note %}
** `BrazeReactInitializer.configure`は、非推奨の`BrazeReactBridge.initBraze(_:)`に代わるSwiftファーストAPIです。また、Objective-Cブリッジにおける`Braze.Configuration`のSwift型解決の問題も解決します。
{% endalert %}
---

## 設定リファレンス {#configuration-reference}

React Nativeでは、**設定はネイティブ**で行います。Androidは`res/values/braze.xml`を読み込み、iOSは**`BrazeReactInitializer.configure`**を通じて登録されたクロージャを使用します。どちらもJavaScriptから`Braze.initialize(apiKey, endpoint)`が呼び出されたときに適用されます。

### Android（`braze.xml`） {#android-brazexml}

デフォルト値はXMLに定義されています。[`BrazeConfig.Builder`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html)を使用して起動時にオーバーライドできます。キーと型の正式な一覧は、[Android SDK統合ガイド](https://www.braze.com/docs/developer_guide/platforms/android/sdk_integration/)および[`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html)に記載されています（各Kotlinプロパティはドキュメント化された`com_braze_*`リソースに対応しています）。

よく使用されるエントリ：

| キー | リソースタイプ | 説明 |
|-----|---------------|-------------|
| `com_braze_enable_delayed_initialization` | `bool` | **必須。** SDKがJavaScriptからの`Braze.initialize()`を待機するように`true`に設定します。 |
| `com_braze_api_key` | `string` | JavaScriptから`Braze.initialize()`を使用する場合は不要です（認証情報はJSから渡されます）。レガシーのネイティブファースト初期化の場合にのみ必要です。 |
| `com_braze_custom_endpoint` | `string` | JavaScriptから`Braze.initialize()`を使用する場合は不要です。レガシーのネイティブファースト初期化の場合にのみ必要です。 |
| `com_braze_server_target` | `string` | オプションのクラスター/環境セレクター（例：内部ビルドやステージングビルド）。Brazeの統合で特に指定がない限り、本番環境では`com_braze_custom_endpoint`を使用してください。 |
| `com_braze_firebase_cloud_messaging_registration_enabled` | `bool` | `true`の場合、BrazeがFCMに登録します（一般的なプッシュ設定）。 |
| `com_braze_firebase_cloud_messaging_sender_id` | `string` | 自動登録が有効な場合のFCM送信者ID。 |
| `com_braze_handle_push_deep_links_automatically` | `bool` | Brazeがプッシュのディープリンクを自動的に開くようにします。 |
| `com_braze_trigger_action_minimum_time_interval_seconds` | `integer` | アプリ内メッセージのトリガーアクション間の最小秒数。 |
| **その他** | *各種* | ここに記載されていない追加キー（セッションタイムアウト、ジオフェンス、ロケーション、通知のデフォルト、デバイス許可リスト、遅延初期化、SDK認証など）。[`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html)および[Android SDK統合ガイド](https://www.braze.com/docs/developer_guide/platforms/android/sdk_integration/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android (braze.xml)" }

### iOS（`Braze.Configuration`） {#ios-brazeconfiguration}

`BrazeReactInitializer.configure`に渡す`configure`クロージャ内でネイティブの設定プロパティを設定します。クロージャは`Braze.Configuration`インスタンスを受け取ります。APIキーとエンドポイントはJavaScriptの`Braze.initialize`呼び出しから自動的に設定されます。詳細：[`Braze.Configuration`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class)およびネストされた型 **`api`**、**`push`**、**`logger`**、**`location`**。

| 領域 | メンバー（代表的なもの） | 備考 |
|------|--------------------------|--------|
| **認証情報** | `api.key`、`api.endpoint` | JavaScriptの`Braze.initialize(apiKey, endpoint)`から自動的に設定されます。`configure`クロージャ内でこれらを設定しないでください。 |
| **ログ** | `logger.level` | 詳細ログは開発用です。本番環境ではノイズを減らしてください。 |
| **プッシュ** | `push.automation`、`push.appGroup`、… | オートメーションにより登録が簡素化されます。Push Stories/エクステンションを使用する場合は`appGroup`が必要です。 |
| **アプリ内メッセージ** | `triggerMinimumTimeInterval` | デフォルトはトリガー間**30**秒です。 |
| **セッション** | `sessionTimeout` | 新しいセッションが開始されるまでの非アクティブ時間（Brazeのセッションドキュメントを参照）。 |
| **プライバシー/データ** | `api.trackingPropertyAllowList`、`devicePropertyAllowList`、`api.sdkAuthentication` | [プライバシーマニフェスト](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/)およびSDK認証の製品設定に合わせてください。 |
| **ネットワーク** | `api.requestPolicy`、`api.flushInterval` | リクエストのリトライポリシーとフラッシュ間隔。 |
| **プッシュ購読** | `optInWhenPushAuthorized` | `true`の場合、ユーザーが通知を許可した後に購読ステータスがオプトインに移行できます。 |
| **IAM + ユーザー変更** | `preventInAppMessageDisplayForDifferentUser` | ユーザーIDが変更された場合のアプリ内メッセージの不一致を軽減します。 |
| **その他** | `forwardUniversalLinks`、`ephemeralEvents`、`useUUIDAsDeviceId`、… | 完全な動作についてはSwiftのドキュメントを参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOS (Braze.Configuration)" }

React Nativeブリッジは初期化時にReact固有の**`api.sdkFlavor`**/SDKメタデータを設定します。Brazeのドキュメントで指示されない限り、これらをオーバーライドしないでください。

---

## JavaScript / TypeScript API

パッケージのデフォルトエクスポートは、**静的**メソッド（例：`Braze.changeUser`、`Braze.logPurchase`）を持つ`Braze`クラスです。`Braze.Events`、`Braze.Genders`、`Braze.NotificationSubscriptionTypes`などの定数も同じエクスポートに含まれています。

---

## コア機能 {#core-features}

### ユーザー管理 {#user-management}

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.changeUser("user-123");
Braze.setEmail("user@example.com");
Braze.setCustomUserAttribute("plan", "premium");
Braze.addAlias("external_id", "marketing_id");
Braze.addToSubscriptionGroup("NEWSLETTER_GROUP_UUID");
```

オプションの**SDK認証**：ダッシュボードで有効にしている場合、`changeUser`の第2引数としてシグネチャを渡すか、`Braze.setSdkAuthenticationSignature(signature)`を呼び出します。

### アプリ内メッセージ {#in-app-messages}

- **デフォルトのBraze UI**を使用する場合は、[アプリ内メッセージのドキュメント](https://www.braze.com/docs/developer_guide/in_app_messages?sdktab=react%20native)に従ってください。デフォルトUIを表示するだけであれば、通常`subscribeToInAppMessage`を呼び出す必要は**ありません**。
- **カスタム**処理を行う場合は、`useBrazeUI: false`でサブスクライブし、必要に応じてインプレッション/クリックを記録します：

``` typescript
Braze.subscribeToInAppMessage(false, (event) => {
  const msg = event.inAppMessage;
  // Render your own UI from msg.message, msg.buttons, etc.
  Braze.logInAppMessageImpression(msg);
});
```

### Content Cards

``` typescript
const cards = await Braze.getCachedContentCards();
Braze.requestContentCardsRefresh();
Braze.launchContentCards(); // default Braze UI

Braze.logContentCardImpression(cardId);
Braze.logContentCardClicked(cardId);
```

`Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, ...)`で更新をリッスンできます。

### バナー {#banners}

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.requestBannersRefresh(["homepage_banner"]);
const banner = await Braze.getBanner("homepage_banner");

// Or use the native Banner view:
// <Braze.BrazeBannerView placementId="homepage_banner" />
```

### プッシュ通知 {#push-notifications}

``` typescript
Braze.requestPushPermission({
  alert: true,
  badge: true,
  sound: true,
});
// Token registration is usually handled natively; see docs for your setup.
Braze.registerPushToken(token);
```

- **`getInitialPushPayload`**：通知からアプリが開かれた際に、RNの`Linking`の競合を回避するために使用します。ネイティブフック（iOSでは`BrazeReactUtils`、Androidでは`BrazeReactUtils.populateInitialPushPayloadFromIntent`）が必要です。詳細はTypeScriptのドキュメントコメントとサンプルアプリを参照してください。
- **`Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, ...)`**は、公開型定義によると**Android専用**です。

### フィーチャーフラグ {#feature-flags}

``` typescript
const flag = await Braze.getFeatureFlag("new_checkout");
if (flag?.enabled) {
  const rollout = flag.getNumberProperty("rollout_percentage") ?? 0;
}
Braze.refreshFeatureFlags();
Braze.logFeatureFlagImpression("new_checkout");
```

### 分析と購入 {#analytics-and-purchases}

``` typescript
Braze.logCustomEvent("purchase_completed", { sku: "sku-1" });
Braze.logPurchase("sku-1", "29.99", "USD", 1, { source: "cart" });
Braze.requestImmediateDataFlush();
```

注：`logPurchase`は**価格を文字列として**受け取ります（型定義を参照）。

### データ管理とSDKの状態 {#data-management-and-sdk-state}

**`changeUser`**は、**新しい**アクティビティをどのユーザーIDに紐付けるかをBrazeに伝えるだけです。デバイス上のキャッシュされたSDKデータをクリアすることは**ありません**。個別の「ログアウト」APIは存在しません。従来のサインアウト（ローカルのBraze状態をクリアして、以前のユーザーのキャッシュされたプロファイル、メッセージ、トークンをこのインストールから削除する）が必要な場合は、通常**`wipeData()`**を使用します。これは完全なローカルリセットです。

``` typescript
Braze.wipeData();
Braze.disableSDK();
Braze.enableSDK();
```

**`wipeData()`** — このインストールのBrazeの**ローカル**データ（キャッシュされたユーザー/セッション/カードの状態、プッシュトークンの関連付けなど）をクリアします。以前のユーザーのBraze状態をデバイスに残してはならない場合の**サインアウトスタイル**の動作、**「このデバイスのデータを削除」**、再インストールなしの**QA**リセット、または厳格な**プライバシー**フローに使用します。**`changeUser`**だけではそのクリーンアップは実行されません。**新しい**イベントを受け取るユーザーIDを設定するだけです。**iOS**では、動作がAndroidと異なる場合があります（例：SDK無効状態との相互作用）。本番環境でこれを使用する場合は、Brazeのネイティブドキュメントを参照してください。

**`disableSDK()`** — SDKの動作を停止します（設定に基づくデータ収集/転送が行われなくなります）。**ユーザーのオプトアウト**トグル、**制限モード**（コンプライアンス、子供向け設定）、または依存関係を削除せずに行う**デバッグ**に使用します。

**`enableSDK()`** — **`disableSDK()`**の後にSDKを再度有効にします。**iOS**では、再有効化が**次のアプリ起動時**まで適用されない場合があります。即時の再有効化に依存する前に、Braze Swift/iOSのドキュメントで確認してください。

---

## イベント {#events}

`Braze.addListener(event, callback)` でイベントを購読します。この呼び出しはサブスクリプションオブジェクトを返します。リスニングを停止するには、そのオブジェクトの **`.remove()`** を呼び出します。

**リスナーの設定：**

``` typescript
import Braze from "@braze/react-native-sdk";

const subscription = Braze.addListener(
  Braze.Events.CONTENT_CARDS_UPDATED,
  (update) => {
    console.log("Content cards:", update.cards);
  }
);
```

**リスナーの削除：**

``` typescript
subscription.remove();
```

Reactコンポーネントでは、サブスクリプションを保存し、クリーンアップ時に `.remove()` を呼び出します（例：`useEffect` のreturn内）。

``` typescript
useEffect(() => {
  const sub = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
    setCards(update.cards);
  });
  return () => sub.remove();
}, []);
```

| イベント定数 | ペイロード（概要） |
|----------------|-------------------|
| `Braze.Events.CONTENT_CARDS_UPDATED` | 最新のContent Cards |
| `Braze.Events.BANNER_CARDS_UPDATED` | 最新のバナー |
| `Braze.Events.FEATURE_FLAGS_UPDATED` | フィーチャーフラグの配列 |
| `Braze.Events.IN_APP_MESSAGE_RECEIVED` | アプリ内メッセージイベント |
| `Braze.Events.SDK_AUTHENTICATION_ERROR` | SDK認証エラーの詳細 |
| `Braze.Events.PUSH_NOTIFICATION_EVENT` | プッシュペイロード（**Androidのみ**） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="イベント" }

---

## 統合に関する注意事項 {#integration-notes}

- **Expo**：可能な限り手動のネイティブ設定を避けるために、[Braze Expoプラグイン](https://github.com/braze-inc/braze-expo-plugin)を使用してください。
- **New Architecture / Turbo Modules**：最新のプラグインバージョンでサポートされています。移行する場合は、開発者ガイドおよびサンプルの`AppDelegate` / Gradle設定に従ってください。
- **プライバシー（iOS）**：`updateTrackingPropertyAllowList`などのメソッドは、プライバシーマニフェスト関連の設定をサポートしています。詳細については、[Swiftプライバシーマニフェスト](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/)を参照してください。

## - **Jest**: `react-native`のネイティブモジュールまたはBraze Turboモジュールをモックします（パターンについてはこのリポジトリの`__tests__/jest.setup.js`を参照してください）。 {#jest-mock-react-native-native-modules-or-the-braze-turbo-module-see-__tests__jestsetupjs-in-this-repo-for-patterns}

## バージョンサポート {#version-support}

{% alert note %}
このSDKはReact Nativeバージョン **0.85.3** でテストされています。
{% endalert %}
以下の表は、BrazeプラグインリリースごとにサポートされているReact Nativeバージョンを示しています。

| Brazeプラグイン | React Native | 新アーキテクチャ |
|--------------|--------------|------------------|
| 9.0.0+       | ≥ 0.71       | はい              |
| 6.0.0+       | ≥ 0.68       | はい (≥ 0.70.0)   |
| 2.0.0+       | ≥ 0.68       | はい              |
| ≤ 1.41.0     | ≤ 0.71       | いいえ               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="バージョンサポート" }

ネイティブSDKの要件も確認してください。

- [Android SDKバージョン情報](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
- [Swift SDKバージョン情報](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

---

## Braze Expoプラグイン {#braze-expo-plugin}

Expoマネージドワークフローについては、[Braze Expoプラグインリポジトリ](https://github.com/braze-inc/braze-expo-plugin)を参照してください。

---

## サンプルアプリ {#sample-app}

このリポジトリの`BrazeProject`は、完全なサンプル（ユーザー管理、Content Cards、フィーチャーフラグ、バナーなど）です。

``` bash
cd BrazeProject/
yarn install
npx react-native start
```

**iOS**（`BrazeProject`から）：

``` bash
cd ios && pod install && cd ..
npx react-native run-ios
```

レガシーアーキテクチャが必要な場合は、`RCT_NEW_ARCH_ENABLED=0 pod install`を使用してください。

**Android**（`BrazeProject`から）：

``` bash
npx react-native run-android
```

---

## デバッグとトラブルシューティング {#debugging-and-troubleshooting}

開発中はBrazeのログを**ネイティブ**設定で有効にして、SDKがシステムコンソール（Xcode / Android Logcat）に書き込むようにします。これにより、初期化、ユーザーの変更、イベント配信を確認できます。

- **iOS** — `BrazeReactInitializer.configure`に渡す`configure`クロージャ内で、`config.logger.level = .debug`（または`.info`）を設定します。本番環境ではログがユーザーに表示されないよう、レベルを下げるか無効にしてください。
- **Android** — `braze.xml`の`com_braze_logger_initial_log_level`リソースを使用するか、`BrazeConfig.Builder`で同等の設定を行います（[BrazeConfigurationProvider](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/logger-initial-log-level.html)を参照）。リリース前に冗長でないレベルに設定するか、オーバーライドを削除してください。

より詳細なトラブルシューティング（ネットワーク、セッション、キャンペーンの動作）については、[Braze React Native開発者ガイド](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native)およびネイティブSDKドキュメント（[Swift](https://github.com/braze-inc/braze-swift-sdk) · [Android](https://github.com/braze-inc/braze-android-sdk)）を参照してください。

---

## その他のリソース {#additional-resources}

- [Braze開発者ガイド — React Native](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native)
- [プッシュ通知 — React Native](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/push_notifications/)
- [GitHubリポジトリ](https://github.com/braze-inc/braze-react-native-sdk)
- [npmパッケージ](https://www.npmjs.com/package/@braze/react-native-sdk)

## お問い合わせ {#contact}

ご質問がある場合は、Brazeテクニカルサポートまでお問い合わせください。
<!-- END GENERATED README CONTENT -->

リポジトリの詳細とサンプルプロジェクトについては、[https://github.com/braze-inc/braze-react-native-sdk](https://github.com/braze-inc/braze-react-native-sdk)を参照してください。