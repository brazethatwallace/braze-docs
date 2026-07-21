---
nav_title: AirshipからBrazeへのSDK移行
permalink: /sdk_migration_guide_airship/
hidden: true
page_type: reference
---

# SDKをAirshipからBraze（iOS）に移行する {#migrate-sdks-from-airship-to-braze-ios}

> Brazeでは、まったく新しいプラットフォームやSDKへの移行が大変なことだと理解しています。しかし、以下の移行ガイド、わかりやすいコードレベルの例、そしてBrazeプラットフォームがもたらす優れた機能セットがあれば、きっとスムーズに進められるはずです。この記事では、Airshipの主要機能の多くに相当するBrazeの機能と、Airshipの使用を置き換えて移行を迅速かつ簡単に行うためのSDKコードスニペットを紹介します。

## コードを超えて {#beyond-the-code}
### トークン管理 {#token-management}
BrazeはAppleのiOS用デバイストークンを使用します。

| **Brazeの観点:**<br>AirshipからBrazeへの移行プロセスにおいて、顧客がユーザーと継続的にコミュニケーション（プッシュ通知など）できるようにします（100% Brazeへのハードカットオーバーであっても、50% Airship・50% Brazeなどのきめ細かい移行であっても同様です）。 |
{: .reset-td-br-1 aria-label="Token management" }

#### プッシュトークンの移行 {#push-token-migration}

[APIを通じてプッシュトークンを移行する]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens)必要があります。リンク先のドキュメントには具体的な手順とペイロードの例が記載されていますが、全体的な流れは以下のとおりです。

1. [`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)経由でトークンをインポートします。大規模なバッチインポートについては、プロセスを迅速化するためのリソースをご用意しています。詳細はCOMまたはSAにお問い合わせください！
2. トークンがすでにBrazeに存在する場合は無視され、存在しない場合は匿名プロファイルが生成されます。
3. プッシュ統合の品質保証を行います。[プッシュを設定する]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)手順が完了していることを確認してください。

ユーザープロファイルとプッシュトークンが別々の場所に保存されている場合は、プッシュトークンを匿名でインポートし、その後で既存のユーザープロファイルを移行することをお勧めします。Braze iOS SDKが統合成功時にトークンの解決を処理するため、これらを一緒にマッピングする必要はありません。

- API経由でユーザーを移行することをお勧めしますが、静的なユーザーリストをインポートする必要がある場合はCSV経由で行うことができます。なお、**プッシュトークンはCSVではインポートできません**。「push_token」オブジェクトをCSVで指定できないためです。インポートテンプレートやダッシュボードへのデータインポートの詳細については、[CSVドキュメント]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv)を参照してください。

{% alert note %}
プッシュトークンはBrazeのダッシュボードでは`subscribed`と表示される場合がありますが、ユーザーがBraze SDKでセッションを開始すると`opted-in`に変わります。
{% endalert %}

#### 複数のプッシュトークン {#multiple-push-tokens}

Brazeでは、ユーザーは複数のプッシュトークン（各デバイスに1つずつ）を持つことができ、有効なプッシュトークンすべてをターゲットにすることで、複数のユーザーデバイスに通知を送信できます。また、ユーザーの最新のデバイスにのみ送信するようにキャンペーンを設定することも可能です。

## キャンペーンの設定 {#campaign-configuration}
高いレベルで言えば、Brazeはカスタマーエンゲージメントの分野において実にユニークなツールです。豊富なカスタマイズオプションと成長し続ける機能セットにより、Brazeに移行されたキャンペーンは、これらのツールのメリットを活用するために再計画することで大きな恩恵を受けることが多いです。当社のキャンペーンプランニングフレームワーク（詳細はCOMまたはSAにお問い合わせください）は、まさにそのために設計されています。

### 構成 {#composition}
#### プッシュ通知 {#push-notifications}
Brazeはプッシュのために別々のチャネルを必要とします（iOS用とAndroid用）。

| **Brazeの観点:**<br>当社は、顧客が妥協することなく両方のメリットを得られるようにしています。個々のチャネルをフルに活用できることで、マーケターにとっては柔軟性が増し、ユーザーエクスペリエンスも向上します。これにより、各OSの最新機能を採用することができます。例えば、AndroidはiOSより先にリッチ通知をサポートしていました。 |
{: .reset-td-br-1 aria-label="Push notifications" }

Brazeは、Braze SDKがインストールされたアプリケーションを更新していないユーザーにもプッシュ通知を送信できます。Brazeに有効なプッシュトークンがある場合、APNsが残りを処理するため、Braze SDKなしでプッシュ通知を送信できます。プッシュメッセージの**分析はBraze SDKを使用しないビルドでは利用できない**ことに注意してください。

##### トークンの共有 {#sharing-tokens}

Braze SDKへの移行プロセス中も継続する必要があるライフサイクル固有のキャンペーンの場合、Brazeが有効なプッシュトークンを受け取っていれば、ユーザーはBrazeとAirshipの両方から通知を受け取ることができます。

#### メッセージセンター {#message-center}
Airshipのメッセージセンターキャンペーン機能を置き換えるには、プッシュ通知と[Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)で構成されるマルチチャネルキャンペーンを作成することをお勧めします。Content Cardsをメッセージセンター形式で使用する方法については、[iOS Content Cards実装ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/implementation_guide#content-cards-in-a-message-center)を参照してください。

### セグメンテーション {#segmentation}
Brazeは、顧客に豊かなユーザー体験を提供するために、複数の[セグメンテーション]({{site.baseurl}}/user_guide/audience/segments)フィルターを提供しています。

| **Brazeの観点**:<br>Brazeのセグメントは完全に動的であるため、定義された条件の変化に応じてユーザーはセグメントに入ったり出たりします。 |
{: .reset-td-br-1 aria-label="Segmentation" }

#### ユーザーセグメントの移行 {#user-segment-migration}

静的なAirshipのセグメントをBrazeで直接再現するには、2つの選択肢があります。
- **API経由でインポートする - カスタム属性を割り当てる**（推奨）<br>
[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)経由でユーザーをインポートし、同時にそのインポートしたユーザーにカスタム属性を割り当てることをお勧めします。例えば、`true`に設定されたカスタム属性`Segment_Group_1`をそれぞれ持つユーザーのセグメントを作成できます。これらのユーザーを後でセグメント化するには、`Segment_Group_1`が`true`であるすべてのユーザーの[セグメントを作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)します。<br><br>
- **CSVユーザーインポートに基づくフィルタリング**<br>
Brazeには、特定のCSVインポートに含まれるユーザーを具体的にフィルターするオプションがあります。このフィルターオプションは、エンゲージメントツールのターゲットユーザーステップの「ユーザーを`Updated/Imported via CSV`でフィルターする」の下にあります。
![CSVインポートフィルター]({% image_buster /assets/img/csv_filter.png %}){: style="max-width:90%;border:0;"}
CSVインポートでは、インポートされる各ユーザーにexternal IDが必要であり、**匿名またはエイリアスのみのユーザーを持つセグメントはインポートできない**ことに注意してください。インポートテンプレートやダッシュボードへのデータインポートの詳細については、[CSVドキュメント]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv)を参照してください。

## SDKコードスニペットを置き換える {#replace-sdk-code-snippets}
移行を簡単にするために、コード内に存在する以下のAirship SDKスニペットを強調表示し、それらを置き換えるために必要な対応するBraze SDKスニペットを提供しています。以下のトピックから始めてください。
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