---
nav_title: AirshipからBrazeへのSDK移行
permalink: /sdk_migration_guide_airship/
hidden: true
page_type: reference
---

# SDKをAirshipからBraze（iOS）に移行する {#migrate-sdks-from-airship-to-braze-ios}

> Brazeでは、まったく新しいプラットフォームやSDKへの移行が大変なことだと理解しています。しかし、以下の移行ガイド、わかりやすいコードレベルの例、そしてBrazeプラットフォームがもたらす優れた機能セットがあれば、きっとスムーズに進められるはずです。この記事では、Airshipの主要機能の多くに相当するBrazeの機能と、Airshipの使用を置き換えて移行を迅速かつ簡単に行うためのSDKコードスニペットを紹介します。

## コードの向こう側 {#beyond-the-code}
### トークン管理 {#token-management}
Brazeは、iOSのAppleデバイストークンを使用します。

| **Brazeの観点:**<br>AirshipからBrazeへの移行プロセスにおいて（Brazeへの100%一括切り替えでも、Airship 50%・Braze 50%のような段階的な移行でも）、顧客がユーザーとの継続的なコミュニケーション（プッシュ通知など）を維持できるようにします。 |
{: .reset-td-br-1 aria-label="トークン管理" }

#### プッシュトークンの移行 {#push-token-migration}

[APIを介したプッシュトークンの移行]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens)が必要です。リンク先のドキュメントには具体的な手順とペイロードの例が記載されていますが、全体的なプロセスは以下のとおりです。

1. [`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を介してトークンをインポートします。大規模なバッチインポートの場合、プロセスを迅速化するためのリソースをご用意しています。詳細については、COMまたはSAにお問い合わせください。
2. トークンがすでにBrazeに存在する場合は無視されます。存在しない場合は、匿名プロファイルが生成されます。
3. プッシュ統合の品質保証を実施します。[プッシュの設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)手順が完了していることを確認してください。

ユーザープロファイルとプッシュトークンが別々の場所に保存されている場合は、まずプッシュトークンを匿名でインポートし、その後既存のユーザープロファイルを移行することをお勧めします。Braze iOS SDKが統合の成功時にトークンの解決を処理するため、両者をマッピングする必要はありません。

- ユーザーの移行はAPIを介して行うことをお勧めしますが、静的なユーザーリストをインポートする必要がある場合は、CSVで行うことができます。ただし、CSVでは「push_token」オブジェクトを指定できないため、**プッシュトークンをCSVでインポートすることはできません**。インポートテンプレートの確認やダッシュボードへのデータインポートの詳細については、[CSVドキュメント]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#braze-csv-import)をご覧ください。

{% alert note %}
プッシュトークンはBrazeダッシュボードで`subscribed`として表示されることがありますが、ユーザーがBraze SDKでセッションを開始すると`opted-in`に変更されます。
{% endalert %}

#### 複数のプッシュトークン {#multiple-push-tokens}

Brazeでは、ユーザーは複数のプッシュトークン（デバイスごとに1つ）を持つことができ、すべての有効なプッシュトークンをターゲットにすることで、複数のユーザーデバイスに通知を送信できます。また、ユーザーの最新のデバイスにのみ送信するようにキャンペーンを設定することも可能です。

## キャンペーンの設定 {#campaign-configuration}
大まかに言えば、Brazeはカスタマーエンゲージメント分野において真にユニークなツールです。豊富なカスタマイズオプションと拡大し続ける機能セットにより、Brazeに移行されたキャンペーンは、これらのツールのメリットを活用するために再計画することで多くの恩恵を受けることができます。当社のキャンペーン計画フレームワーク（詳細についてはCOMまたはSAにお問い合わせください）は、まさにそのために構築されています。

### 構成 {#composition}
#### プッシュ通知 {#push-notifications}
Brazeではプッシュに個別のチャネルが必要です（iOSとAndroidでそれぞれ1つずつ）。

| **Brazeの見解:**<br>Brazeでは、妥協を強いられることなく、両方のメリットを活用できます。各チャネルをフルに活用できることで、マーケターにとってはより高い柔軟性を、ユーザーにとってはより良い体験を提供します。これにより、各OSの最新機能を取り入れることが可能になります。例えば、AndroidはiOSよりも先にリッチプッシュ通知をサポートしていました。 |
{: .reset-td-br-1 aria-label="プッシュ通知" }

Brazeは、Braze SDKがインストールされたアプリケーションを更新していないユーザーにもプッシュ通知を送信できます。Brazeが有効なプッシュトークンを持っている場合、APNsが残りの処理を行うため、Braze SDKなしでもプッシュ通知を送信できます。ただし、**Braze SDKが含まれていないビルドではプッシュメッセージの分析を利用できない**ことに注意することが重要です。

##### トークンの共有 {#sharing-tokens}

Braze SDKへの移行プロセス中も継続する必要があるライフサイクル固有のキャンペーンの場合、Brazeが有効なプッシュトークンを受信していれば、ユーザーはBrazeとAirshipの両方から通知を受け取る資格がある場合があります。

#### メッセージセンター {#message-center}
Airshipのメッセージセンターキャンペーン機能を置き換えるには、プッシュ通知と[Content Card]({{site.baseurl}}/user_guide/channels/content_cards)で構成されるマルチチャネルキャンペーンを作成することをお勧めします。メッセージセンター形式でContent Cardsを使用する方法の詳細については、[iOS Content Cards実装ガイド]({{site.baseurl}}/developer_guide/content_cards/creating_cards#message-inbox)をご覧ください。

### セグメンテーション {#segmentation}
Brazeは、顧客に充実したユーザー体験を提供するために、複数の[セグメンテーション]({{site.baseurl}}/user_guide/audience/segments)フィルターを提供しています。

| **Brazeの見解**:<br>Brazeのセグメントは完全にダイナミックであるため、定義された条件が変更されるとユーザーはセグメントに出入りします。 |
{: .reset-td-br-1 aria-label="セグメンテーション" }

#### ユーザーセグメントの移行 {#user-segment-migration}

Airshipの静的セグメントをBrazeで直接再作成するには、2つの方法があります：
- **API経由でインポート - カスタム属性の割り当て**（推奨）<br>
[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を介してユーザーをインポートし、その際にインポートされたユーザーにカスタム属性を割り当てることをお勧めします。例えば、`Segment_Group_1`というカスタム属性が`true`に設定されたユーザーのセグメントを作成できます。後でこれらのユーザーをセグメント化するには、`Segment_Group_1`が`true`であるすべてのユーザーの[セグメントを作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)します。<br><br>
- **CSVユーザーインポートに基づくフィルター**<br>
Brazeには、特定のCSVインポートに含まれるユーザーを特定してフィルタリングするオプションがあります。このフィルタリングオプションは、エンゲージメントツールのターゲットユーザーステップで「`Updated/Imported via CSV`でユーザーをフィルター」の下にあります。
![CSVインポートフィルター]({% image_buster /assets/img/csv_filter.png %}){: style="max-width:90%;border:0;"}
CSVインポートでは、インポートされる各ユーザーにexternal IDが必要であり、**匿名ユーザーまたはエイリアスのみのユーザーのセグメントはインポートできない**ことに注意してください。インポートテンプレートの確認やダッシュボードへのデータインポートの詳細については、[CSVドキュメント]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#braze-csv-import)をご覧ください。

## SDKコードスニペットの置き換え {#replace-sdk-code-snippets}
移行を簡素化するため、コード内に存在する以下のAirship SDKスニペットを強調表示し、置き換えに必要な対応するBraze SDKスニペットを提供しています。以下のトピックにアクセスして始めましょう:
- [インストール](#installation)
- [ユーザーIDの取得と設定](#userid)
- [プッシュ通知の処理](#pushnotifications)
- [分析](#analytics)
- [アプリ内メッセージの処理](#iammessages)
- [Content Cardsとメッセージセンター](#messagecenter)

### インストール {#installation}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {

    UAirship.takeOff(UAConfig.default())

    UALocation.shared()?.isLocationUpdatesEnabled = true
    UALocation.shared().isBackgroundLocationUpdatesAllowed = true

    UAirship.push()?.notificationOptions = [.alert, .badge, .sound]
    UAirship.push()?.userPushNotificationsEnabled = true
    UAirship.push()?.pushNotificationDelegate = self

    UAInAppAutomation.shared()?.inAppMessageManager.delegate = self
    UAInAppAutomation.shared()?.inAppMessageManager.displayInterval = 30
}
```
**Braze**
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {

    Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

    locationManager.requestAlwaysAuthorization() // locationManager is a CLLocationManager property variable

    // Push Notifications
    let options: UNAuthorizationOptions = [.alert, .sound, .badge]
    UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
      Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
    }
    UIApplication.shared.registerForRemoteNotifications()

    // In-App Messages
    Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endtab %}
{% tab Objective-C %}
**Airship**
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

  [UAirship takeOff:[UAConfig defaultConfig]];

  [[UALocation shared] setLocationUpdatesEnabled:YES];
  [[UALocation shared] setBackgroundLocationUpdatesAllowed:YES];

  [UAirship push].notificationOptions = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  [[UAirship push] setUserPushNotificationsEnabled:YES];
  [[UAirship push] setPushNotificationDelegate:self];

  [UAInAppAutomation shared].inAppMessageManager.delegate = self;
  [UAInAppAutomation shared].inAppMessageManager.displayInterval = 30;

  return YES;
}
```
**Braze**
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

  [Appboy startWithApiKey:self.apiKey inApplication:application withLaunchOptions:launchOptions withAppboyOptions:self.appboyOptions];

  [self.locationManager requestAlwaysAuthorization]; // locationManager is a CLLocationManager property variable

  // Push Notifications
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options
                          completionHandler:^(BOOL granted, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];

  // In-App Messages
  [[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];

  return YES;
}
```

{% endtab %}
{% endtabs %}

### ユーザーIDの取得と設定 {#userid}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
extension AirshipManager {
  var userId: String? {
    return UAirship.namedUser()?.identifier
   }

  func setUser(_ userId: String) {
    UAirship.namedUser()?.identifier = userId
  }
}
```
**Braze**
```swift
extension AppboyManager {
  var userId: String? {
     return Appboy.sharedInstance()?.user.userID
  }

  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Airship**
```objc

- (NSString *)userId {
  return [UAirship namedUser].identifier
}

- (void)setUser:(NSString *)userId {
  [[UAirship namedUser] setIdentifier:userId];
}
```
**Braze**
```objc
- (NSString *)userId {
  return [Appboy sharedInstance].user.userID;
}

- (void)changeUser:(NSString *)userId {
  [[Appboy sharedInstance] changeUser: userId];
}
```
{% endtab %}
{% endtabs %}

### プッシュ通知の処理 {#pushnotifications}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
extension AirshipManager: UAPushNotificationDelegate {
  func receivedBackgroundNotification(_ notificationContent: UANotificationContent, completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    completionHandler(.noData)
  }

  func receivedForegroundNotification(_ notificationContent: UANotificationContent, completionHandler: @escaping () -> Void) {
    completionHandler()
  }

  func receivedNotificationResponse(_ notificationResponse: UANotificationResponse, completionHandler: @escaping () -> Void) {
    completionHandler()
  }
}
```
**Braze**
```swift
extension AppboyManager {
  func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
  }

  func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    Appboy.sharedInstance()?.register(application, didReceiveRemoteNotification: userInfo, fetchCompletionHandler: completionHandler)
  }

  func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
    Appboy.sharedInstance()?.userNotificationCenter(center, didReceive: response, withCompletionHandler: completionHandler)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Airship**
```objc
- (void)receivedBackgroundNotification:(UANotificationContent *)notificationContent completionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  completionHandler(UIBackgroundFetchResultNoData);
}

- (void)receivedForegroundNotification:(UANotificationContent *)notificationContent completionHandler:(void (^)(void))completionHandler {
  completionHandler();
}

- (void)receivedNotificationResponse:(UANotificationResponse *)notificationResponse completionHandler:(void (^)(void))completionHandler {
  completionHandler();
}
```
**Braze**
```objc
- (void)application:(UIApplication *)application didRegisterForRemoteNotifications
  func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
  }

- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  [[Appboy sharedInstance] registerDeviceToken:deviceToken];
}

- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
}

- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response
         withCompletionHandler:(void (^)(void))completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center didReceiveNotificationResponse:response withCompletionHandler:completionHandler];
}
```
{% endtab %}
{% endtabs %}

### 分析 {#analytics}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
extension AirshipManager {
  func trackEvent(with name: String, value: NSDecimalNumber? = nil, eventProperties: [String: Any]? = nil) {
    let event = UACustomEvent(name: name, value: value)

    if let eventProperties = eventProperties {
      event.properties = eventProperties
    }

    event.track()
  }

  func applyMutationsWithValue(_ value: String, forAttribute attribute: String) {
    let mutations = UAAttributeMutations()
    mutations.setString(value, forAttribute: attribute)
    UAirship.namedUser().apply(mutations)
  }
}
```
**Braze**
```swift
extension AppboyManager {
  func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
    Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
  }

  func setCustomAttributeWithKey(_ key: String, andStringValue value: String) {
    Appboy.sharedInstance()?.user.setCustomAttributeWithKey(key, andStringValue: value)
  }

  func logPurchase(productIdentifier: String, inCurrency currency: String, atPrice price: String, withQuanitity quanity: Int) {
    Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quanity))
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Airship**
```objc
- (void)trackEventWith:(NSString *)name value:(NSDecimalNumber *)value eventProperties:(NSDictionary *)eventProperties {
  UACustomEvent *event = [[UACustomEvent alloc] init];
  event.eventName = name;
  event.eventValue = value;
  event.properties = eventProperties;

  [event track];
}

- (void)applyMutationWith:(NSString *)value forAttribute:(NSString *)attribute {
  UAAttributeMutations* mutations = [[UAAttributeMutations alloc] init];
  [mutations setString:value forAttribute:attribute];
  [[UAirship namedUser] applyAttributeMutations:mutations];
}
```
**Braze**
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties: properties];
}

- (void)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value {
  [[Appboy sharedInstance].user setCustomAttributeWithKey:key andStringValue:value];
}

- (void)logPurchase:(NSString *)productIdentifier inCurrency:(NSString *)currency atPrice:(NSString *)price withQuantity:(NSInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currency atPrice:[[NSDecimalNumber alloc] initWithString:price] withQuantity:quantity];
}
```
{% endtab %}
{% endtabs %}

### アプリ内メッセージの処理 {#iammessages}
{% tabs %}
{% tab Swift %}
**Airship**
```swift

extension AirshipManager: UAInAppMessagingDelegate {
  func extend(_ message: UAInAppMessage) -> UAInAppMessage {
      return message
  }

  func messageWillBeDisplayed(_ message: UAInAppMessage, scheduleID: String) {
  }

  func messageFinishedDisplaying(_ message: UAInAppMessage, scheduleID: String, resolution: UAInAppMessageResolution) {
  }
}
```
**Braze**
```swift
extension AppboyManager: ABKInAppMessageControllerDelegate {
  func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
    // This delegate method defines whether the in-app message will be displayed now, displayed later, or discarded.
    return .displayInAppMessageNow
  }

  func beforeControlMessageImpressionLogged(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
    // This delegate method defines the timing of when the control in-app message impression event should be logged: now, later, or discarded.
    return .displayInAppMessageNow
  }
}

extension AppboyManager: ABKInAppMessageUIDelegate {
  func on(inAppMessageDismissed inAppMessage: ABKInAppMessage) {
    // Use this method to perform any custom logic that should execute after the in-app message has been dismissed
  }

  func on(inAppMessageClicked inAppMessage: ABKInAppMessage) -> Bool {
    // This delegate method is fired when the user clicks on a slide-up in-app message or a modal/full in-app message without button(s) on it.
    return true
  }

  func on(inAppMessageButtonClicked inAppMessage: ABKInAppMessageImmersive, button: ABKInAppMessageButton) -> Bool {
    // This delegate method is fired whenever the user clicks a button on the in-app message.
    return true
  }

  func on(inAppMessageHTMLButtonClicked inAppMessage: ABKInAppMessageHTMLBase, clickedURL: URL?, buttonID buttonId: String) -> Bool {
    // This delegate method is fired whenever the user clicks a link on the HTML in-app message.
    return true
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Airship**
```objc
- (UAInAppMessage *)extendMessage:(UAInAppMessage *)message {

  return message;
}

- (void)messageWillBeDisplayed:(UAInAppMessage *)message scheduleID:(NSString *)scheduleID {

}

- (void)messageFinishedDisplaying:(UAInAppMessage *)message scheduleID:(NSString *)scheduleID resolution:(UAInAppMessageResolution *)resolution {

}
```
**Braze**
```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  return ABKDisplayInAppMessageNow;
}

- (ABKInAppMessageDisplayChoice) beforeControlMessageImpressionLogged:(ABKInAppMessage *)inAppMessage {
  return ABKDisplayInAppMessageNow;
}

- (void)onInAppMessageDismissed:(ABKInAppMessage *)inAppMessage {
  // Use this method to perform any custom logic that should execute after the in-app message has been dismissed
}

- (BOOL)onInAppMessageClicked: (ABKInAppMessage *)inAppMessage {
  // This delegate method is fired when the user clicks on a slide-up in-app message or a modal/full in-app message without button(s) on it.
  return YES;
}

- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button {
  return YES;
}

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID {
  return YES;
}
```
{% endtab %}
{% endtabs %}

### Content Cardsとメッセージセンター {#messagecenter}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
extension AirshipManager {
  func displayMessageCenter() {
    UAMessageCenter.shared()?.defaultUI.title = "My Message Center"

    let style = UAMessageCenterStyle()
    style.navigationBarColor = .black
    style.titleColor = .white
    style.tintColor = .white

    UAMessageCenter.shared()?.defaultUI.messageCenterStyle = style
    UAMessageCenter.shared()?.display()
  }
}
```
**Braze**
```swift
extension AppboyManager {
  func displayContentCards(navigationController: UINavigationController?) {
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "My Message Center"
    contentCardsVc.disableUnreadIndicator = true
    navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Airship**
```objc
- (void)displayMessageCenter {
  [UAMessageCenter shared].defaultUI.title = @"My Message Center";
  [[UAMessageCenter shared] display];
}
```
**Braze**
```objc
- (void)displayContentCards:(UINavigationController *)navigationController {
  ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
  contentCards.title = @"My Message Center";
  [self.navigationController pushViewController:contentCards animated:YES];
}
```
{% endtab %}
{% endtabs %}