---
nav_title: SDK統合ガイド（任意）
article_title: iOS 用 Braze SDK 統合ガイド（オプション）
alias: "/ios_sdk/"
description: "この iOS 統合ガイドでは、iOS SDKとそのコアコンポーネントを初めてアプリケーションに統合する際のセットアップのベストプラクティスについて段階的に説明します。このガイドは、BrazeManager.swift ヘルパーファイルの作成に役立ちます。"
page_order: 10
platform: iOS

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Braze iOS SDK 統合ガイド {#braze-ios-sdk-integration-guide}

> このオプションのiOS統合ガイドでは、iOS SDKとそのコアコンポーネントを初めてアプリケーションに統合する際のセットアップのベストプラクティスについて段階的に説明します。このガイドは、`BrazeManager.swift` ヘルパーファイルを作成する際に役立ちます。このヘルパーファイルは、Braze iOS SDKへの依存関係をプロダクションコードの残りの部分から切り離し、アプリケーション全体で `import AppboyUI` を1か所だけにします。このアプローチにより、過剰なSDKインポートから発生する問題が軽減され、コードの追跡、デバッグ、および変更が容易になります。

{% alert important %}
このガイドでは、すでにXcodeプロジェクトに[SDKを追加]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview)していることを前提としています。
{% endalert %}

## 連携の概要 {#integration-overview}

以下の手順では、プロダクションコードが呼び出す `BrazeManager` ヘルパーファイルの構築方法について説明します。このヘルパーファイルは、以下の連携トピックに対応するさまざまなエクステンションを追加することで、Braze関連のすべての依存関係を処理します。各トピックには、SwiftとObjective-Cの両方の水平タブステップとコードスニペットが含まれています。Content Cardsとアプリ内メッセージのステップは、アプリケーションでこれらのチャネルを使用する予定がない場合、連携に必須ではありません。

- [BrazeManager.swiftの作成](#create-brazemanagerswift)
- [SDKの初期化](#initialize-the-sdk)
- [プッシュ通知](#push-notifications)
- [ユーザー変数とメソッドへのアクセス](#access-user-variables-and-methods)
- [分析のログ記録](#log-analytics)
- [アプリ内メッセージ（オプション）](#in-app-messages)
- [Content Cards（オプション）](#content-cards)
- [次のステップ](#next-steps)

### BrazeManager.swiftの作成 {#create-brazemanagerswift}

{% tabs local %}
{% tab Create BrazeManager swift %}

#### BrazeManager.swiftの作成
`BrazeManager.swift` ファイルを構築するには、プロジェクト内の任意の場所に _BrazeManager_ という名前の新しいSwiftファイルを作成して追加します。次に、`import Foundation` を SPMの場合は `import AppboyUI`（CocoaPodsの場合は `import Appboy_iOS_SDK`）に置き換え、すべてのBraze関連のメソッドと変数をホストする `BrazeManager` クラスを作成します。`Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager` は構造体ではなく `NSObject` クラスであるため、`ABKInAppMessageUIDelegate` などのABKデリゲートに準拠できます。
- `BrazeManager` は設計上シングルトンクラスであり、このクラスのインスタンスは1つだけ使用されます。これはオブジェクトへの統一されたアクセスポイントを提供するためです。
{% endalert %}

1. `BrazeManager` クラスを初期化する _shared_ という名前の静的変数を追加します。これは一度だけ遅延初期化されることが保証されています。
2. 次に、_apiKey_ という名前のプライベート定数変数を追加し、BrazeダッシュボードのワークスペースからAPIキー値として設定します。
3. SDKの設定値を格納する _appboyOptions_ という名前のプライベート算出変数を追加します。現時点では空になります。

{% subtabs global %}
{% subtab Swift %}

```swift
class BrazeManager: NSObject {
  // 1
  static let shared = BrazeManager()

  // 2
  private let apikey = "YOUR-API-KEY"

  // 3
  private var appboyOptions: [String:Any] {
    return [:]
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation BrazeManager

// 1
+ (instancetype)shared {
    static BrazeManager *shared = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        shared = [[BrazeManager alloc] init];
        // Do any other initialisation stuff here
    });
    return shared;
}

// 2
- (NSString *)apiKey {
  return @"YOUR-API-KEY";
}

// 3
- (NSDictionary *)appboyOptions {
  return [NSDictionary dictionary];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### SDKの初期化 {#initialize-the-sdk}

{% tabs local %}
{% tab Step 1: Initialize SDK from BrazeManager swift %}

#### BrazeManager.swiftからSDKを初期化する {#initialize-sdk-from-brazemanagerswift}
次に、SDKを初期化する必要があります。このガイドでは、すでにXcodeプロジェクトに[SDKを追加]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview)していることを前提としています。また、`Info.plist` ファイルまたは `appboyOptions` に[ワークスペースSDKエンドポイント]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration#step-2-specify-your-data-cluster)と[`LogLevel`]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#braze-log-level)が設定されている必要があります。

`AppDelegate.swift` ファイルの `didFinishLaunchingWithOptions` メソッドを、`BrazeManager.swift` ファイルに戻り値型なしで追加します。`BrazeManager.swift` ファイルに同様のメソッドを作成することで、`AppDelegate.swift` ファイルに `import AppboyUI` ステートメントが不要になります。

次に、新しく宣言した `apiKey` と `appboyOptions` 変数を使用してSDKを初期化します。

{% alert important %}
初期化はメインスレッドで行う必要があります。
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Step 2: Handle Appboy Initialization %}

##### AppDelegate.swiftでAppboyの初期化を処理する {#handle-appboy-initialization-in-the-appdelegateswift}
次に、`AppDelegate.swift` ファイルに戻り、AppDelegateの `didFinishLaunchingWithOptions` メソッドに以下のコードスニペットを追加して、`BrazeManager.swift` ヘルパーファイルからAppboyの初期化を処理します。`AppDelegate.swift` に `import AppboyUI` ステートメントを追加する必要はありません。

{% subtabs global %}
{% subtab Swift %}

```swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
  // Override point for customization after application launch

  BrazeManager.shared.application(application, didFinishLaunchingWithOptions: launchOptions)

  return true
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Override point for customization after application launch

  [[BrazeManager shared] application:application didFinishLaunchingWithOptions:launchOptions];

  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
コードをコンパイルし、アプリケーションを実行してください。<br><br>この時点で、SDKが起動して動作しているはずです。ダッシュボードでセッションがログ記録されていることを確認してから、先に進んでください。
{% endalert %}

### プッシュ通知 {#push-notifications}

{% tabs local %}
{% tab Step 1: Add Push Certificate %}

#### プッシュ証明書の追加 {#add-push-certificate}

Brazeダッシュボードの既存のワークスペースに移動します。**プッシュ通知設定**でプッシュ証明書ファイルをBrazeダッシュボードにアップロードし、保存します。

![APNsキーアップロードフィールドがあるBrazeダッシュボードのプッシュ通知設定。]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Step 2: Register for Notifications %}

{% alert important %}
このステップの最後にある専用のチェックポイントを見逃さないでください！
{% endalert %}

##### プッシュ通知の登録 {#register-for-push-notifications}

次に、プッシュ通知を登録します。このガイドでは、Apple開発者ポータルとXcodeプロジェクトで[プッシュ認証情報を正しく設定]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)していることを前提としています。

プッシュ通知を登録するコードは、`BrazeManager.swift` ファイルの `didFinishLaunching...` メソッドに追加されます。初期化コードは最終的に以下のようになります：

1. ユーザーとの対話のための認証リクエストの内容を設定します。これらのオプションは例として記載されています。
2. ユーザーにプッシュ通知を送信するための認証をリクエストします。ユーザーのプッシュ通知の許可または拒否の応答は `granted` 変数で追跡されます。
3. ユーザーが通知プロンプトに対話した後、プッシュ認証結果をBrazeに転送します。
4. APNsへの登録プロセスを開始します。これはメインスレッドで行う必要があります。登録が成功した場合、アプリは `AppDelegate` オブジェクトの `didRegisterForRemoteNotificationsWithDeviceToken` メソッドを呼び出します。

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey:Any]?) {
  Appboy.start(withAPIKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
  // 1
  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  // 2
  UNUserNotificationCenter.current().requestAuthorization(option: options) { (granted, error) in
  // 3
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }

  // 4
  UIApplications.shared.registerForRemoteNotificiations()
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];

  // 1
  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);

  // 2
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
  // 3
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];

  // 4
  [[UIApplication sharedApplication] registerForRemoteNotifications];
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert checkpoint %}
コードをコンパイルし、アプリケーションを実行してください。
- アプリでプッシュ通知のプロンプトが表示されていることを確認してから、先に進んでください。
- プロンプトが表示されない場合は、アプリを削除して再インストールし、プッシュ通知のプロンプトが以前に表示されていないことを確認してください。

先に進む前に、プッシュ通知のプロンプトが表示されていることを確認してください。
{% endalert %}

{% endtab %}
{% tab Step 3: Forward Methods %}

##### プッシュ通知メソッドの転送 {#forward-push-notification-methods}

次に、Braze iOS SDKで処理されるように、システムのプッシュ通知メソッドを `AppDelegate.swift` から `BrazeManager.swift` に転送します。

###### ステップ1: プッシュ通知コードのエクステンションを作成する {#step-1-create-extension-for-push-notification-code}

ヘルパーファイルで提供される目的がより整理された方法で読めるように、`BrazeManager.swift` ファイルにプッシュ通知コードのエクステンションを作成します：

1. `AppDelegate` に `import AppboyUI` ステートメントを含めないパターンに従い、`BrazeManager.swift` ファイルでプッシュ通知メソッドを処理します。ユーザーのデバイストークンは `didRegisterForRemote...` メソッドからBrazeに渡す必要があります。このメソッドはサイレントプッシュ通知の実装に必要です。次に、`AppDelegate` と同じメソッドを `BrazeManager` クラスに追加します。
2. メソッド内に以下の行を追加して、デバイストークンをBrazeに登録します。これはBrazeがトークンを現在のデバイスに関連付けるために必要です。

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK - Push Notifications
extension BrazeManager {
  // 1
  func application(
    _ application: UIApplication,
    didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
  ) {
    // 2
    Appboy.sharedInstance().?registerDeviceToken(deviceToken)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK - Push Notifications
// 1
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  // 2
  [[Appboy sharedInstance] registerDeviceToken:deviceToken];
}
```
{% endsubtab %}
{% endsubtabs %}

###### ステップ2: リモート通知のサポート {#step-2-support-remote-notifications}
**Signing & Capabilities** タブで、**Background Modes** サポートを追加し、**Remote notifications** を選択して、Brazeから発信されるリモートプッシュ通知のサポートを開始します。<br><br>![Signing & Capabilitiesの設定画面]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### ステップ3: リモート通知の処理 {#step-3-remote-notification-handling}
Braze SDKは、Brazeから発信されるリモートプッシュ通知を処理できます。リモート通知をBrazeに転送してください。SDKはBrazeから発信されていないプッシュ通知を自動的に無視します。プッシュ通知エクステンション内の `BrazeManager.swift` ファイルに以下のメソッドを追加します。

{% subtabs global %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication,
  didReceiveRemoteNotification userInfo: [AnyHashable : Any],
  fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
) {
  Appboy.sharedInstance()?.register(
    application,
    didReceiveRemoteNotification: userInfo,
    fetchCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application didReceiveRemoteNotification:userInfo fetchCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}

###### ステップ4: 通知レスポンスの転送 {#step-4-forward-notification-responses}

Braze SDKは、Brazeから発信されるプッシュ通知のレスポンスを処理できます。通知のレスポンスをBrazeに転送してください。SDKはBrazeから発信されていないプッシュ通知からのレスポンスを自動的に無視します。以下のメソッドを `BrazeManager.swift` ファイルに追加します：

{% subtabs global %}
{% subtab Swift %}

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  didReceive response: UNNotificationResponse,
  withCompletionHandler completionHandler: @escaping () -> Void
) {
  Appboy.sharedInstance()?.userNotificationCenter(
    center,
    didReceive: response,
    withCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response
         withCompletionHandler:(void (^)(void))completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center
                   didReceiveNotificationResponse:response
                            withCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
コードをコンパイルし、アプリケーションを実行してください。<br><br>Brazeダッシュボードから自分にプッシュ通知を送信し、先に進む前にプッシュ通知から分析がログ記録されていることを確認してください。
{% endalert %}

### ユーザー変数とメソッドへのアクセス {#access-user-variables-and-methods}

{% tabs local %}
{% tab Create User Variables and Methods %}

#### ユーザー変数とメソッドの作成 {#create-user-variables-and-methods}

次に、`ABKUser` の変数とメソッドに簡単にアクセスできるようにします。ヘルパーファイルで提供される目的がより整理された方法で読めるように、`BrazeManager.swift` ファイルにユーザーコードのエクステンションを作成します：

1. `ABKUser` オブジェクトは、iOSアプリケーション内の既知のまたは匿名のユーザーを表します。`ABKUser` を取得するための算出変数を追加します。この変数はユーザーに関する変数を取得するために再利用されます。
2. ユーザー変数をクエリして `userId` に簡単にアクセスします。`ABKUser` オブジェクトが担当する他の変数には（`firstName`、`lastName`、`phone`、`homeCity` など）があります。
3. 対応する `userId` で `changeUser()` を呼び出してユーザーを設定します。

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK: - User
extension BrazeManager {
  // 1
  var user: ABKUser? {
    return Appboy.sharedInstance()?.user
  }

  // 2
  var userId: String? {
    return user?.userID
  }

  // 3
  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - User
  // 1
- (ABKUser *)user {
  return [[Appboy sharedInstance] user];
}

   // 2
- (NSString *)userId {
  return [self user].userID;
}

  // 3
- (void)changeUser:(NSString *)userId {
  [[Appboy sharedInstance] changeUser:userId];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
コードをコンパイルし、アプリケーションを実行してください。<br><br>サインイン/サインアップの成功からユーザーを識別してみてください。適切なユーザー識別子とそうでないものについてしっかりと理解しておいてください。<br><br>ダッシュボードでユーザー識別子がログ記録されていることを確認してから、先に進んでください。
{% endalert %}

### 分析のログ記録 {#log-analytics}

{% tabs local %}
{% tab Step 1: Custom Events %}

#### カスタムイベントのログ記録メソッドの作成 {#create-log-custom-event-method}

以下のBraze SDKの `logCustomEvent` メソッドに基づいて、対応するメソッドを作成します。

**Brazeの `logCustomEvent` リファレンスメソッド**<br>
これは設計上、`BrazeManager.swift` ファイルのみがBraze iOS SDKのメソッドに直接アクセスできるためです。したがって、対応するメソッドを作成することで、プロダクションコードでBraze iOS SDKへの直接的な依存関係なしに同じ結果が得られます。

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**対応するメソッド**<br>
`Appboy` オブジェクトからBrazeにカスタムイベントをログ記録します。`Properties` はデフォルト値がnilのオプションパラメータです。カスタムイベントにはプロパティは必須ではありませんが、名前は必須です。

{% subtabs global %}
{% subtab Swift %}
```swift
func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
  Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(nullable NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:properties];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 2: Custom Attributes %}

##### カスタム属性のログ記録メソッドの作成 {#create-log-custom-attributes-method}

SDKはカスタム属性として多数の型をログ記録できます。設定可能な各値型のヘルパーメソッドを作成する必要はありません。代わりに、適切な値にフィルタリングできる1つのメソッドのみを公開します。

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

カスタム属性は `ABKUser` オブジェクトからログ記録されます。

属性に設定できるすべての利用可能な型を網羅する**1つのメソッド**を作成します。このメソッドを `BrazeManager.swift` ファイルの分析エクステンションに追加します。有効なカスタム属性型をフィルタリングし、一致する型に関連付けられたメソッドを呼び出すことで実現できます。

- パラメータ `value` は `Equatable` プロトコルに準拠するジェネリック型です。これは明示的に行われており、Braze iOS SDKが期待する型でない場合、コンパイル時エラーが発生します。
- パラメータ `key` と `value` はオプションパラメータであり、メソッド内で条件付きアンラップされます。これはnil以外の値がBraze iOS SDKに渡されることを保証する1つの方法です。

{% subtabs global %}
{% subtab Swift %}

```swift
func setCustomAttributeWithKey<T: Equatable>(_ key: String?, andValue value: T?) {
  guard let key = key, let value = value else { return }
  switch value.self {
  case let value as Date:
    user?.setCustomAttributeWithKey(key, andDateValue: value)
  case let value as Bool:
    user?.setCustomAttributeWithKey(key, andBOOLValue: value)
  case let value as String:
    user?.setCustomAttributeWithKey(key, andStringValue: value)
  case let value as Double:
    user?.setCustomAttributeWithKey(key, andDoubleValue: value)
  case let value as Int:
    user?.setCustomAttributeWithKey(key, andIntegerValue: value)
  default:
   return
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)setCustomAttributeWith:(NSString *)key andValue:(id)value {
  if ([value isKindOfClass:[NSDate class]]) {
    [[self user] setCustomAttributeWithKey:key andDateValue:value];
  } else if ([value isKindOfClass:[NSString class]]) {
    [[self user] setCustomAttributeWithKey:key andStringValue:value];
  } else if ([value isKindOfClass:[NSNumber class]]) {
    if (strcmp([value objCType], @encode(double)) == 0) {
      [[self user] setCustomAttributeWithKey:key andDoubleValue:[value doubleValue]];
    } else if (strcmp([value objCType], @encode(int)) == 0) {
      [[self user] setCustomAttributeWithKey:key andIntegerValue:[value integerValue]];
    } else if ([value boolValue]) {
      [[self user] setCustomAttributeWithKey:key andBOOLValue:[value boolValue]];
    }
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 3: Purchases %}

##### 購入のログ記録メソッドの作成 {#create-log-purchase-method}

次に、以下のBraze SDKの `logPurchase` メソッドに基づいて、対応するメソッドを作成します。

**Brazeの `logPurchase` リファレンスメソッド**<br>
これは設計上、`BrazeManager.swift` ファイルのみがBraze iOS SDKのメソッドに直接アクセスできるためです。したがって、対応するメソッドを作成することで、プロダクションコードでBraze iOS SDKへの直接的な依存関係なしに同じ結果が得られます。

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**対応するメソッド**<br>
`Appboy` オブジェクトからBrazeに購入をログ記録します。SDKには購入をログ記録するための複数のメソッドがあり、これはその一例です。このメソッドは `NSDecimal` と `UInt` オブジェクトの作成も処理します。その部分をどのように処理するかはお客様次第です。ここでは一例を示しています。

{% subtabs global %}
{% subtab Swift %}

```swift
func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price:
String, withQuantity quantity: Int) {

  Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quantity))

}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPurchase:(NSString *)productIdentifier inCurrency:(nonnull NSString *)currencyCode atPrice:(nonnull NSDecimalNumber *)price withQuantity:(NSUInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currencyCode atPrice:price withQuantity:quantity];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
コードをコンパイルし、アプリケーションを実行してください。<br><br>カスタムイベントのログ記録を試してみてください。<br><br>ダッシュボードでカスタムイベントがログ記録されていることを確認してから、先に進んでください。
{% endalert %}

### アプリ内メッセージ {#in-app-messages}

{% tabs local %}
{% tab Step 1: Conform to Delegate %}

{% alert important %}
以下のアプリ内メッセージのセクションは、アプリケーションでこのチャネルを使用する予定がない場合、連携に必須ではありません。
{% endalert %}

#### ABKInAppMessageUIDelegateへの準拠 {#conform-to-abkinappmessageuidelegate}

次に、`BrazeManager.swift` ファイルのコードが `ABKInAppMessageUIDelegate` に準拠するようにし、関連するメソッドを直接処理できるようにします。

デリゲートに準拠するコードは、`BrazeManager.swift` ファイルの `didFinishLaunching...` メソッドに追加されます。初期化コードは最終的に以下のようになります：

{% subtabs global %}
{% subtab swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()

  Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];

  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];

  [[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 2: Add Delegate Methods %}

##### デリゲートメソッドの追加 {#add-delegate-methods}
次に、`ABKInAppMessageUIDelegate` に準拠するエクステンションを作成します。

分析セクションに以下のスニペットを追加します。`BrazeManager.swift` オブジェクトがデリゲートとして設定されていることに注意してください。ここで `BrazeManager.swift` ファイルがすべての `ABKInAppMessageUIDelegate` メソッドを処理します。

{% alert important %}
`ABKInAppMessageUIDelegate` には必須メソッドはありませんが、以下はその一例です。
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - ABKInAppMessage UI Delegate
extension AppboyManager: ABKInAppMessageUIDelegate{
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return ABKInAppMessageSlideupViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageModal:
      return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageFull:
      return ABKInAppMessageFullViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - ABKInAppMessage UI Delegate
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [[ABKInAppMessageSlideupViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [[ABKInAppMessageFullViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  }
  return nil;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
コードをコンパイルし、アプリケーションを実行してください。<br><br>自分にアプリ内メッセージを送信してみてください。<br><br>`BrazeManager.swift` ファイルで、`ABKInAppMessageUIDelegate` メソッドの例のエントリにブレークポイントを設定します。自分にアプリ内メッセージを送信し、先に進む前にブレークポイントがヒットすることを確認してください。
{% endalert %}

### Content Cards {#content-cards}

{% tabs local %}
{% tab Create Content Card Variables and Methods %}

{% alert important %}
以下のContent Cardsセクションは、アプリケーションでこのチャネルを使用する予定がない場合、連携に必須ではありません。
{% endalert %}

#### Content Cardsの変数とメソッドの作成 {#create-content-card-variables-and-methods}

不要な `import AppboyUI` ステートメントなしでプロダクションコードがContent Cardsビューコントローラーを表示できるようにします。

ヘルパーファイルで提供される目的がより整理された方法で読めるように、`BrazeManager.swift` ファイルにContent Cardsコードのエクステンションを作成します：

1. `ABKContentCardsTableViewController` を表示します。ビューコントローラーをプレゼントまたはプッシュするために必要なのは、オプションの `navigationController` パラメータのみです。
2. `ABKContentCardsTableViewController` オブジェクトを初期化し、オプションでタイトルを変更します。また、初期化したビューコントローラーをナビゲーションスタックに追加する必要があります。

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - Content Cards
extension BrazeManager {

  // 1
  func displayContentCards(navigationController: UINavigationController?) {

    // 2
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "Content Cards"
    navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - Content Cards
  // 1
- (void)displayContentCards:(UINavigationController *)navigationController {
  // 2
  ABKContentCardsTableViewController *contentCardsVc = [[ABKContentCardsTableViewController alloc] init];
  contentCardsVc.title = @"Content Cards";
  [navigationController pushViewController:contentCardsVc animated:YES];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
コードをコンパイルし、アプリケーションを実行してください。<br><br>先に進む前に、アプリケーションで `ABKContentCardsTableViewController` の表示を試してください。
{% endalert %}

## 次のステップ {#next-steps}

おめでとうございます！このベストプラクティス統合ガイドを完了しました。`BrazeManager`ヘルパーファイルの例は[GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift)で確認できます。

Braze iOS SDKへの依存関係をプロダクションコードの他の部分から分離できたので、オプションの高度な実装ガイドをご確認ください：

{% article_tiles %}
- name: 高度なプッシュ通知実装ガイド
  link: /docs/developer_guide/platforms/legacy_sdks/ios/push_notifications/implementation_guide
  description: iOSアプリでプッシュ通知の動作をカスタマイズするためのオプションの高度なパターンです。
- name: 高度なアプリ内メッセージ実装ガイド
  link: /docs/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide
  description: アプリ内メッセージの配信と表示をカスタマイズするためのオプションの高度なパターンです。
- name: 高度なContent Cards実装ガイド
  link: /docs/developer_guide/platforms/legacy_sdks/ios/content_cards/implementation_guide
  description: Content Cardsフィードとユーザーインターフェースをカスタマイズするためのオプションの高度なパターンです。
{% endarticle_tiles %}