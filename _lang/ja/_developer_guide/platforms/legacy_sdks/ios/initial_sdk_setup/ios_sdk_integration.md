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

## 統合の概要 {#integration-overview}

以下の手順は、プロダクションコードが呼び出す `BrazeManager` ヘルパーファイルの作成に役立ちます。このヘルパーファイルは、以下にリストされている統合トピックのさまざまなエクステンションを追加することで、Braze関連のすべての依存関係を処理します。各トピックには、SwiftとObjective-Cの両方の水平タブステップとコードスニペットが含まれます。アプリケーションでこれらのチャネルを使用する予定がない場合、Content Cardsとアプリ内メッセージのステップは統合に必要ありません。

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
`BrazeManager.swift` ファイルを作成するには、_BrazeManager_ という名前の新しいSwiftファイルを作成し、プロジェクトの任意の場所に追加します。次に、`import Foundation` をSPMの場合は `import AppboyUI` に（CocoaPodsの場合は `import Appboy_iOS_SDK` に）置き換え、すべてのBraze関連のメソッドと変数をホストするための `BrazeManager` クラスを作成します。`Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager` は構造体ではなく `NSObject` クラスであるため、`ABKInAppMessageUIDelegate` などのABKデリゲートに準拠できます。
- `BrazeManager` は設計上シングルトンクラスであり、このクラスのインスタンスは1つだけ使用されます。これは、オブジェクトへの統一されたアクセスポイントを提供するために行われます。
{% endalert %}

1. `BrazeManager` クラスを初期化する _shared_ という名前の静的変数を追加します。これは一度だけ遅延初期化されることが保証されています。
2. 次に、_apiKey_ という名前のプライベート定数変数を追加し、Brazeダッシュボードのワークスペースから取得したAPIキー値として設定します。
3. _appboyOptions_ という名前のプライベート計算変数を追加します。これにはSDKの設定値が格納されます。今のところ空です。

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
次に、SDKを初期化する必要があります。このガイドでは、すでにXcodeプロジェクトに[SDKを追加]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview)していることを前提としています。また、[ワークスペースSDKエンドポイント]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration#step-2-specify-your-data-cluster)および[`LogLevel`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations#braze-log-level)を `Info.plist` ファイルまたは `appboyOptions` に設定する必要があります。

`didFinishLaunchingWithOptions` メソッドを `AppDelegate.swift` ファイルから戻り値の型なしで `BrazeManager.swift` ファイルに追加します。`BrazeManager.swift` ファイルに同様のメソッドを作成することで、`AppDelegate.swift` ファイルに `import AppboyUI` ステートメントは不要になります。

次に、新しく宣言した `apiKey` および `appboyOptions` 変数を使用してSDKを初期化します。

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

##### AppDelegate.swiftでのAppboy初期化処理 {#handle-appboy-initialization-in-the-appdelegateswift}
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
コードをコンパイルしてアプリケーションを実行してください。<br><br>この時点で、SDKが稼働しているはずです。ダッシュボードでセッションがログに記録されていることを確認してから、次に進んでください。
{% endalert %}

### プッシュ通知 {#push-notifications}

{% tabs local %}
{% tab Step 1: Add Push Certificate %}

#### プッシュ証明書の追加 {#add-push-certificate}

Brazeダッシュボードで既存のワークスペースに移動します。**プッシュ通知の設定**で、プッシュ証明書ファイルをBrazeダッシュボードにアップロードして保存します。

![APNsキーのアップロードフィールドが表示されたBrazeダッシュボードのプッシュ通知設定。]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Step 2: Register for Notifications %}

{% alert important %}
このステップの最後にある専用チェックポイントを見逃さないでください！
{% endalert %}

##### プッシュ通知の登録 {#register-for-push-notifications}

次に、プッシュ通知を登録します。このガイドでは、Apple開発者ポータルおよびXcodeプロジェクトで[プッシュ認証情報を正しく設定]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)していることを前提としています。

プッシュ通知を登録するコードは、`BrazeManager.swift` ファイルの `didFinishLaunching...` メソッドに追加されます。初期化コードは最終的に次のようになります。

1. ユーザーとのインタラクションの許可を要求するためのコンテンツを設定します。これらのオプションは例としてリストされています。
2. ユーザーにプッシュ通知を送信する許可を要求します。プッシュ通知を許可または拒否するユーザーの応答は、`granted` 変数で追跡されます。
3. ユーザーが通知プロンプトを操作した後、プッシュ承認の結果をBrazeに転送します。
4. APNsで登録プロセスを開始します。これはメインスレッドで行う必要があります。登録が成功すると、アプリは `AppDelegate` オブジェクトの `didRegisterForRemoteNotificationsWithDeviceToken` メソッドを呼び出します。

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
コードをコンパイルしてアプリケーションを実行してください。
- アプリで、プッシュ通知の許可を求めるプロンプトが表示されていることを確認してから、先に進んでください。
- プロンプトが表示されない場合は、アプリを削除して再インストールし、プッシュ通知のプロンプトが以前に表示されていないことを確認してください。

プッシュ通知の許可を求めるプロンプトが表示されていることを確認してから、先に進んでください。
{% endalert %}

{% endtab %}
{% tab Step 3: Forward Methods %}

##### プッシュ通知メソッドの転送 {#forward-push-notification-methods}

次に、システムのプッシュ通知メソッドを `AppDelegate.swift` から `BrazeManager.swift` に転送し、Braze iOS SDKで処理されるようにします。

###### ステップ1: プッシュ通知コードのエクステンションを作成する {#step-1-create-extension-for-push-notification-code}

`BrazeManager.swift` ファイルにプッシュ通知コードのエクステンションを作成し、ヘルパーファイルでどのような目的が果たされているかをより整理された形で読み取れるようにします。以下に例を示します。

1. `AppDelegate` に `import AppboyUI` ステートメントを含めないパターンに従って、`BrazeManager.swift` ファイルでプッシュ通知メソッドを処理します。ユーザーのデバイストークンは、`didRegisterForRemote...` メソッドからBrazeに渡される必要があります。このメソッドは、サイレントプッシュ通知を実装するために必要です。次に、`BrazeManager` クラスに `AppDelegate` と同じメソッドを追加します。
2. 以下の行をメソッド内に追加して、デバイストークンをBrazeに登録します。これは、Brazeがトークンを現在のデバイスに関連付けるために必要です。

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
**Signing & Capabilities** タブで、**Background Modes** のサポートを追加し、**Remote notifications** を選択して、Brazeから発信されるリモートプッシュ通知のサポートを開始します。<br><br>![Signing & Capabilities]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### ステップ3: リモート通知の処理 {#step-3-remote-notification-handling}
Braze SDKは、Brazeから発信されるリモートプッシュ通知を処理できます。リモート通知をBrazeに転送してください。SDKはBrazeから発信されたものではないプッシュ通知を自動的に無視します。プッシュ通知エクステンション内の `BrazeManager.swift` ファイルに次のメソッドを追加します。

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

###### ステップ4: 通知応答の転送 {#step-4-forward-notification-responses}

Braze SDKは、Brazeから発信されるプッシュ通知の応答を処理できます。通知の応答をBrazeに転送してください。SDKは、Brazeから発信されていないプッシュ通知からの応答を自動的に無視します。以下のメソッドを `BrazeManager.swift` ファイルに追加します。

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
コードをコンパイルしてアプリケーションを実行してください。<br><br>Brazeダッシュボードからプッシュ通知を送信してみて、プッシュ通知から分析がログに記録されていることを確認してから、次に進んでください。
{% endalert %}

### ユーザー変数とメソッドへのアクセス {#access-user-variables-and-methods}

{% tabs local %}
{% tab Create User Variables and Methods %}

#### ユーザー変数とメソッドの作成 {#create-user-variables-and-methods}

次に、`ABKUser` の変数とメソッドに簡単にアクセスできるようにします。`BrazeManager.swift` ファイルにユーザーコードのエクステンションを作成し、ヘルパーファイルでどのような目的が果たされているかをより整理された形で読み取れるようにします。以下に例を示します。

1. `ABKUser` オブジェクトは、iOSアプリケーションの既知または匿名ユーザーを表します。`ABKUser` を取得するための計算変数を追加します。この変数は、ユーザーに関する変数を取得するために再利用されます。
2. `userId` に簡単にアクセスするには、ユーザー変数をクエリします。他の変数の中で、`ABKUser` オブジェクトは（`firstName`、`lastName`、`phone`、`homeCity` など）を管理します。
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
コードをコンパイルしてアプリケーションを実行してください。<br><br>サインイン/サインアップに成功したユーザーを識別してみてください。何が適切なユーザー識別子であり、何が適切でないかをしっかりと理解してください。<br><br>ダッシュボードで、ユーザー識別子がログに記録されていることを確認してから、先に進んでください。
{% endalert %}

### 分析のログ記録 {#log-analytics}

{% tabs local %}
{% tab Step 1: Custom Events %}

#### カスタムイベント記録メソッドの作成 {#create-log-custom-event-method}

以下のBraze SDKの `logCustomEvent` メソッドに基づいて、一致するメソッドを作成します。

**Braze `logCustomEvent` 参照メソッド**<br>
Braze iOS SDKのメソッドに直接アクセスできるのは `BrazeManager.swift` ファイルだけなので、これは仕様です。したがって、一致するメソッドを作成することで、結果は同じになり、プロダクションコード内でBraze iOS SDKに直接依存する必要がなくなります。

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**一致するメソッド**<br>
`Appboy` オブジェクトからBrazeにカスタムイベントを記録します。`Properties` はオプションのパラメータで、デフォルト値はnilです。カスタムイベントにはプロパティは必須ではありませんが、名前は必須です。

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

##### カスタム属性記録メソッドの作成 {#create-log-custom-attributes-method}

SDKは、カスタム属性として多数のタイプをログに記録できます。設定可能な値タイプごとにヘルパーメソッドを作成する必要はありません。代わりに、適切な値に絞り込むことができる1つのメソッドのみを公開します。

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

カスタム属性は、`ABKUser` オブジェクトからログに記録されます。

属性に設定可能なすべてのタイプを包含できる**1つのメソッド**を作成します。分析エクステンションの `BrazeManager.swift` ファイルにこのメソッドを追加します。これは、有効なカスタム属性タイプをフィルタリングして、一致するタイプに関連付けられたメソッドを呼び出すことによって行うことができます。

- パラメータ `value` は、`Equatable` プロトコルに準拠するジェネリック型です。これは明示的に行われるため、タイプがBraze iOS SDKの期待するものでない場合、コンパイル時エラーが発生します。
- パラメータ `key` および `value` はオプションのパラメータで、メソッド内で条件付きでアンラップされます。これは、nil以外の値がBraze iOS SDKに渡されるようにする1つの方法です。

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

##### 購入記録メソッドの作成 {#create-log-purchase-method}

次に、以下のBraze SDKの `logPurchase` メソッドに基づいて、一致するメソッドを作成します。

**Braze `logPurchase` 参照メソッド**<br>
Braze iOS SDKのメソッドに直接アクセスできるのは `BrazeManager.swift` ファイルだけなので、これは仕様です。したがって、一致するメソッドを作成することで、結果は同じになり、プロダクションコード内でBraze iOS SDKに直接依存する必要がなくなります。

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**一致するメソッド**<br>
`Appboy` オブジェクトからの購入をBrazeに記録します。SDKには購入を記録するための複数のメソッドがあり、これは1つの例にすぎません。このメソッドは、`NSDecimal` および `UInt` オブジェクトの作成も処理します。その部分をどのように処理するかはあなた次第ですが、以下はほんの一例です。

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
コードをコンパイルしてアプリケーションを実行してください。<br><br>カスタムイベントを記録してみてください。<br><br>ダッシュボードで、カスタムイベントがログに記録されていることを確認してから先に進んでください。
{% endalert %}

### アプリ内メッセージ {#in-app-messages}

{% tabs local %}
{% tab Step 1: Conform to Delegate %}

{% alert important %}
アプリケーションでこのチャネルを使用する予定がない場合、以下のアプリ内メッセージセクションは統合に必要ありません。
{% endalert %}

#### ABKInAppMessageUIDelegateに準拠する {#conform-to-abkinappmessageuidelegate}

次に、`BrazeManager.swift` ファイルのコードを `ABKInAppMessageUIDelegate` に準拠させ、関連付けられたメソッドを直接処理できるようにします。

デリゲートに準拠するコードは、`BrazeManager.swift` ファイルの `didFinishLaunching...` メソッドに追加されます。初期化コードは最終的に次のようになります。

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

次のスニペットを分析セクションに追加します。`BrazeManager.swift` オブジェクトがデリゲートとして設定されていることに注意してください。これは、`BrazeManager.swift` ファイルがすべての `ABKInAppMessageUIDelegate` メソッドを処理する場所です。

{% alert important %}
`ABKInAppMessageUIDelegate` には必須メソッドはありませんが、以下は1つの例です。
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
コードをコンパイルしてアプリケーションを実行してください。<br><br>アプリ内メッセージを送信してみてください。<br><br>`BrazeManager.swift` ファイルで、`ABKInAppMessageUIDelegate` メソッドの例のエントリにブレークポイントを設定します。アプリ内メッセージを送信し、ブレークポイントに到達したことを確認してから、さらに進んでください。
{% endalert %}

### Content Cards {#content-cards}

{% tabs local %}
{% tab Create Content Card Variables and Methods %}

{% alert important %}
アプリケーションでこのチャネルを使用する予定がない場合、以下のContent Cardsセクションは統合に必要ありません。
{% endalert %}

#### Content Cardsの変数とメソッドの作成 {#create-content-card-variables-and-methods}

不要な `import AppboyUI` ステートメントなしで、Content Cardsビューコントローラーを表示できるようにプロダクションコードを有効にします。

`BrazeManager.swift` ファイルにContent Cardsコードのエクステンションを作成し、ヘルパーファイルでどのような目的が果たされているかをより整理された形で読み取れるようにします。以下に例を示します。

1. `ABKContentCardsTableViewController` を表示します。オプションの `navigationController` は、ビューコントローラーを表示またはプッシュするために必要な唯一のパラメータです。
2. `ABKContentCardsTableViewController` オブジェクトを初期化し、オプションでタイトルを変更します。初期化されたビューコントローラーをナビゲーションスタックに追加する必要もあります。

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
コードをコンパイルしてアプリケーションを実行してください。<br><br>アプリケーションで `ABKContentCardsTableViewController` を表示してみてから先に進んでください。
{% endalert %}

## 次のステップ {#next-steps}

おめでとうございます！このベストプラクティス統合ガイドを完了しました！`BrazeManager` ヘルパーファイルの例は、[GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift)にあります。

これで、Braze iOS SDKへの依存関係をプロダクションコードの残りの部分から切り離すことができたので、オプションの高度な実装ガイドをいくつかご覧ください。
- [高度なプッシュ通知実装ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/implementation_guide)
- [高度なアプリ内メッセージ実装ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide)
- [高度なContent Cards実装ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/implementation_guide)