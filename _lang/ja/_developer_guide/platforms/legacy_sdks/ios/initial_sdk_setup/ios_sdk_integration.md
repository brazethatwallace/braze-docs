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

以下の手順は、本番コードから呼び出す `BrazeManager` ヘルパーファイルの構築方法を説明します。このヘルパーファイルは、以下の連携トピックに関するさまざまなエクステンションを追加することで、Braze 関連のすべての依存関係を処理します。各トピックには、SwiftとObjective-Cの両方の水平タブステップとコードスニペットが含まれます。Content Cardsとアプリ内メッセージのステップは、アプリケーションでこれらのチャネルを使用する予定がない場合、連携に必須ではありません。

- [BrazeManager.swiftの作成](#create-brazemanagerswift)
- [SDKの初期化](#initialize-the-sdk)
- [プッシュ通知](#push-notifications)
- [ユーザー変数およびメソッドへのアクセス](#access-user-variables-and-methods)
- [分析のログ記録](#log-analytics)
- [アプリ内メッセージ（オプション）](#in-app-messages)
- [Content Cards（オプション）](#content-cards)
- [次のステップ](#next-steps)

### BrazeManager.swiftの作成 {#create-brazemanagerswift}

{% tabs local %}
{% tab Create BrazeManager swift %}

#### BrazeManager.swiftの作成
`BrazeManager.swift` ファイルを作成するには、_BrazeManager_ という名前の新しい Swift ファイルを作成し、プロジェクト内の任意の場所に追加します。次に、`import Foundation` を SPM の場合は `import AppboyUI`（CocoaPods の場合は `import Appboy_iOS_SDK`）に置き換え、Braze 関連のすべてのメソッドと変数をホストする `BrazeManager` クラスを作成します。`Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager` は構造体ではなく `NSObject` クラスであり、`ABKInAppMessageUIDelegate` などの ABK デリゲートに準拠できます。
- `BrazeManager` は設計上シングルトンクラスであり、このクラスのインスタンスは1つだけ使用されます。これは、オブジェクトへの統一されたアクセスポイントを提供するためです。
{% endalert %}

1. `BrazeManager` クラスを初期化する _shared_ という名前の静的変数を追加します。これは、一度だけ遅延初期化されることが保証されています。
2. 次に、_apiKey_ という名前のプライベート定数変数を追加し、BrazeダッシュボードのワークスペースからAPI キー値として設定します。
3. _appboyOptions_ という名前のプライベートコンピューテッド変数を追加します。これはSDKの設定値を格納します。現時点では空のままです。

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
次に、SDKを初期化する必要があります。このガイドでは、すでにXcodeプロジェクトに[SDKを追加している]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview)ことを前提としています。また、`Info.plist`ファイルまたは`appboyOptions`で[ワークスペースSDKエンドポイント]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration#step-2-specify-your-data-cluster)と[`LogLevel`]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#braze-log-level)が設定されている必要があります。

`AppDelegate.swift`ファイルの`didFinishLaunchingWithOptions`メソッドを、戻り値の型なしで`BrazeManager.swift`ファイルに追加します。`BrazeManager.swift`ファイルに同様のメソッドを作成することで、`AppDelegate.swift`ファイルに`import AppboyUI`文が不要になります。

次に、新しく宣言した`apiKey`変数と`appboyOptions`変数を使用してSDKを初期化します。

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
次に、`AppDelegate.swift`ファイルに戻り、`BrazeManager.swift`ヘルパーファイルからAppboyの初期化を処理するために、AppDelegateの`didFinishLaunchingWithOptions`メソッドに以下のコードスニペットを追加します。`AppDelegate.swift`に`import AppboyUI`文を追加する必要はありません。

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
コードをコンパイルしてアプリケーションを実行してください。<br><br>この時点で、SDKが正常に動作しているはずです。ダッシュボードでセッションがログ記録されていることを確認してから、次のステップに進んでください。
{% endalert %}

### プッシュ通知 {#push-notifications}

{% tabs local %}
{% tab Step 1: Add Push Certificate %}

#### プッシュ証明書の追加 {#add-push-certificate}

Brazeダッシュボードで既存のワークスペースに移動します。**プッシュ通知設定**で、プッシュ証明書ファイルをBrazeダッシュボードにアップロードして保存します。

![APNsキーのアップロードフィールドが表示されたBrazeダッシュボードのプッシュ通知設定。]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Step 2: Register for Notifications %}

{% alert important %}
このステップの最後にある専用チェックポイントを見逃さないでください！
{% endalert %}

##### プッシュ通知の登録 {#register-for-push-notifications}

次に、プッシュ通知の登録を行います。このガイドでは、Apple開発者ポータルおよびXcodeプロジェクトで[プッシュの認証情報が正しく設定されている]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)ことを前提としています。

プッシュ通知の登録コードは、`BrazeManager.swift`ファイルの`didFinishLaunching...`メソッドに追加します。最終的な初期化コードは以下のようになります：

1. ユーザーとのインタラクションの許可をリクエストするためのコンテンツを構成します。これらのオプションは例として記載されています。
2. プッシュ通知をユーザーに送信する許可をリクエストします。プッシュ通知を許可または拒否するユーザーのレスポンスは、`granted`変数で追跡されます。
3. ユーザーが通知プロンプトに対してインタラクションした後、プッシュ許可の結果をBrazeに転送します。
4. APNsへの登録プロセスを開始します。これはメインスレッドで行う必要があります。登録が成功すると、アプリは`AppDelegate`オブジェクトの`didRegisterForRemoteNotificationsWithDeviceToken`メソッドを呼び出します。

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
- アプリで、次に進む前にプッシュ通知の許可を求めるプロンプトが表示されることを確認してください。
- プロンプトが表示されない場合は、アプリを削除して再インストールし、プッシュ通知のプロンプトが以前に表示されていないことを確認してください。

次に進む前に、プッシュ通知のプロンプトが表示されていることを確認してください。
{% endalert %}

{% endtab %}
{% tab Step 3: Forward Methods %}

##### プッシュ通知メソッドの転送 {#forward-push-notification-methods}

次に、`AppDelegate.swift`からシステムのプッシュ通知メソッドを`BrazeManager.swift`に転送し、Braze iOS SDKで処理されるようにします。

###### ステップ1: プッシュ通知コード用のエクステンションを作成する {#step-1-create-extension-for-push-notification-code}

`BrazeManager.swift`ファイルにプッシュ通知コード用のエクステンションを作成し、ヘルパーファイルでどのような目的が果たされているかがより整理された形で読めるようにします。以下のようになります：

1. `AppDelegate`に`import AppboyUI`文を含めないパターンに従い、プッシュ通知メソッドは`BrazeManager.swift`ファイルで処理します。ユーザーのデバイストークンは、`didRegisterForRemote...`メソッドからBrazeに渡す必要があります。このメソッドはサイレントプッシュ通知の実装に必要です。次に、`AppDelegate`と同じメソッドを`BrazeManager`クラスに追加します。
2. メソッド内に、デバイストークンをBrazeに登録する以下の行を追加します。これは、Brazeがトークンを現在のデバイスに関連付けるために必要です。

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
**Signing & Capabilities** タブで、**Background Modes** サポートを追加し、**Remote notifications** を選択して、Brazeからのリモートプッシュ通知のサポートを開始します。<br><br>![Signing & Capabilitiesの設定画面]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### ステップ3: リモート通知のハンドリング {#step-3-remote-notification-handling}
Braze SDKは、Brazeから発信されたリモートプッシュ通知を処理できます。リモート通知をBrazeに転送してください。SDKはBraze以外から発信されたプッシュ通知を自動的に無視します。プッシュ通知エクステンション内の`BrazeManager.swift`ファイルに以下のメソッドを追加してください。

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

Braze SDKは、Brazeから発信されたプッシュ通知のレスポンスを処理できます。通知のレスポンスをBrazeに転送してください。SDKはBraze以外から発信されたプッシュ通知のレスポンスを自動的に無視します。`BrazeManager.swift`ファイルに以下のメソッドを追加してください：

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
コードをコンパイルしてアプリケーションを実行してください。<br><br>Brazeダッシュボードから自分自身にプッシュ通知を送信し、次に進む前にプッシュ通知から分析がログ記録されていることを確認してください。
{% endalert %}

### ユーザー変数およびメソッドへのアクセス {#access-user-variables-and-methods}

{% tabs local %}
{% tab Create User Variables and Methods %}

#### ユーザー変数およびメソッドの作成 {#create-user-variables-and-methods}

次に、`ABKUser`の変数とメソッドに簡単にアクセスできるようにします。`BrazeManager.swift`ファイルにユーザーコード用のエクステンションを作成し、ヘルパーファイルでどのような目的が果たされているかがより整理された形で読めるようにします。以下のようになります：

1. `ABKUser`オブジェクトは、iOSアプリケーションの既知のユーザーまたは匿名ユーザーを表します。`ABKUser`を取得するコンピューテッド変数を追加します。この変数はユーザーに関する変数を取得するために再利用されます。
2. `userId`に簡単にアクセスするためにユーザー変数をクエリします。その他の変数として、`ABKUser`オブジェクトは（`firstName`、`lastName`、`phone`、`homeCity`など）を管理します。
3. 対応する`userId`で`changeUser()`を呼び出してユーザーを設定します。

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
コードをコンパイルしてアプリケーションを実行してください。<br><br>サインイン/サインアップの成功時にユーザーを識別してみてください。適切なユーザー識別子とは何か、そうでないものは何かをしっかり理解しておいてください。<br><br>ダッシュボードでユーザー識別子がログ記録されていることを確認してから、次のステップに進んでください。
{% endalert %}

### 分析のログ記録 {#log-analytics}

{% tabs local %}
{% tab Step 1: Custom Events %}

#### カスタムイベントのログ記録メソッドの作成 {#create-log-custom-event-method}

以下のBraze SDKの`logCustomEvent`メソッドに基づいて、対応するメソッドを作成します。

**Brazeの`logCustomEvent`参照メソッド**<br>
これは設計上、`BrazeManager.swift`ファイルのみがBraze iOS SDKメソッドに直接アクセスできるようにするためです。したがって、対応するメソッドを作成することで、結果は同じであり、本番コードでBraze iOS SDKへの直接的な依存関係なしに実現できます。

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**対応するメソッド**<br>
`Appboy`オブジェクトからBrazeにカスタムイベントをログ記録します。`Properties`はデフォルト値がnilのオプションパラメータです。カスタムイベントにはプロパティは必須ではありませんが、名前は必須です。

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
{% tab Step 2: カスタム属性 %}

##### カスタム属性のログ記録メソッドの作成 {#create-log-custom-attributes-method}

SDKはカスタム属性として多数の型をログ記録できます。設定可能な各値型に対してヘルパーメソッドを作成する必要はありません。代わりに、適切な値にフィルタリングできるメソッドを1つだけ公開します。

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

カスタム属性は`ABKUser`オブジェクトからログ記録されます。

属性に設定できるすべての利用可能な型を包括する**1つのメソッド**を作成します。このメソッドを`BrazeManager.swift`ファイルの分析エクステンションに追加します。これは、有効なカスタム属性タイプをフィルタリングし、一致するタイプに関連するメソッドを呼び出すことで実現できます。

- パラメータ`value`は、`Equatable`プロトコルに準拠するジェネリック型です。これは明示的に行われており、Braze iOS SDKが期待する型でない場合、コンパイル時エラーが発生します。
- パラメータ`key`と`value`はオプションパラメータであり、メソッド内で条件付きでアンラップされます。これは、nil以外の値がBraze iOS SDKに渡されることを保証する一つの方法です。

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

##### 購入ログ記録メソッドの作成 {#create-log-purchase-method}

次に、以下のBraze SDKの`logPurchase`メソッドに基づいて、対応するメソッドを作成します。

**Brazeの`logPurchase`参照メソッド**<br>
これは設計上、`BrazeManager.swift`ファイルのみがBraze iOS SDKメソッドに直接アクセスできるようにするためです。したがって、対応するメソッドを作成することで、結果は同じであり、本番コードでBraze iOS SDKへの直接的な依存関係なしに実現できます。

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**対応するメソッド**<br>
`Appboy`オブジェクトからBrazeに購入をログ記録します。SDKには購入をログ記録するための複数のメソッドがあり、これはその一例です。このメソッドは`NSDecimal`と`UInt`オブジェクトの作成も処理します。その部分をどのように処理するかはあなた次第であり、ここでは一例を示しています。

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
コードをコンパイルしてアプリケーションを実行してください。<br><br>カスタムイベントのログ記録を試してください。<br><br>ダッシュボードでカスタムイベントがログ記録されていることを確認してから、次のステップに進んでください。
{% endalert %}

### アプリ内メッセージ {#in-app-messages}

{% tabs local %}
{% tab Step 1: Conform to Delegate %}

{% alert important %}
以下のアプリ内メッセージセクションは、アプリケーションでこのチャネルを使用する予定がない場合、連携に必須ではありません。
{% endalert %}

#### ABKInAppMessageUIDelegateへの準拠 {#conform-to-abkinappmessageuidelegate}

次に、`BrazeManager.swift`ファイルのコードが`ABKInAppMessageUIDelegate`に準拠し、関連するメソッドを直接処理できるようにします。

デリゲートへの準拠コードは、`BrazeManager.swift`ファイルの`didFinishLaunching...`メソッドに追加されます。最終的な初期化コードは以下のようになります：

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
次に、`ABKInAppMessageUIDelegate`に準拠するエクステンションを作成します。

分析セクションに以下のスニペットを追加します。`BrazeManager.swift`オブジェクトがデリゲートとして設定されていることに注意してください。ここが`BrazeManager.swift`ファイルがすべての`ABKInAppMessageUIDelegate`メソッドを処理する場所になります。

{% alert important %}
`ABKInAppMessageUIDelegate`には必須メソッドはありませんが、以下はその一例です。
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
コードをコンパイルしてアプリケーションを実行してください。<br><br>自分自身にアプリ内メッセージを送信してみてください。<br><br>`BrazeManager.swift`ファイルで、`ABKInAppMessageUIDelegate`メソッドの例のエントリにブレークポイントを設定してください。アプリ内メッセージを自分に送信し、ブレークポイントがヒットすることを確認してから次のステップに進んでください。
{% endalert %}

### Content Cards {#content-cards}

{% tabs local %}
{% tab Create Content カード Variables and Methods %}

{% alert important %}
以下のContent Cardsセクションは、アプリケーションでこのチャネルを使用する予定がない場合、連携に必須ではありません。
{% endalert %}

#### Content Cardsの変数とメソッドの作成 {#create-content-card-variables-and-methods}

不要な`import AppboyUI`文なしで、本番コードからContent Cardsビューコントローラーを表示できるようにします。

`BrazeManager.swift`ファイルにContent Cardsコード用のエクステンションを作成し、ヘルパーファイルでどのような目的が果たされているかがより整理された形で読めるようにします。以下のようになります：

1. `ABKContentCardsTableViewController`を表示します。ビューコントローラーを表示またはプッシュするために必要な唯一のパラメータは、オプションの`navigationController`です。
2. `ABKContentCardsTableViewController`オブジェクトを初期化し、オプションでタイトルを変更します。また、初期化されたビューコントローラーをナビゲーションスタックに追加する必要があります。

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
コードをコンパイルしてアプリケーションを実行してください。<br><br>次に進む前に、アプリケーションで`ABKContentCardsTableViewController`の表示を試してください。
{% endalert %}

## 次のステップ {#next-steps}

おめでとうございます！このベストプラクティス統合ガイドを完了しました。`BrazeManager` ヘルパーファイルの例は [GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift) で確認できます。

Braze iOS SDKへの依存関係をプロダクションコードの残りの部分から分離できたので、オプションの高度な実装ガイドをご確認ください：
- [高度なプッシュ通知実装ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/implementation_guide)
- [高度なアプリ内メッセージ実装ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide)
- [高度なContent Cards実装ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/implementation_guide)