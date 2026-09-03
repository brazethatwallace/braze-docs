---
nav_title: Airship에서 Braze로의 SDK 마이그레이션
permalink: /sdk_migration_guide_airship/
hidden: true
page_type: reference
---

# Airship에서 Braze로 SDK 마이그레이션(iOS) {#migrate-sdks-from-airship-to-braze-ios}

> Braze는 완전히 새로운 플랫폼과 SDK로 이전하는 것이 부담스러울 수 있다는 점을 잘 알고 있습니다. 하지만 다음 마이그레이션 가이드와 간단한 코드 수준의 예제, 그리고 Braze 플랫폼이 제공하는 인상적인 기능 세트를 활용하면 걱정하지 않으셔도 됩니다. 이 문서에서는 많은 주요 Airship 기능에 해당하는 Braze 기능과 함께 Airship 사용을 대체하여 마이그레이션을 빠르고 간단하며 손쉽게 진행할 수 있는 SDK 코드 스니펫을 소개합니다.

## 코드 이상의 것들 {#beyond-the-code}
### 토큰 관리 {#token-management}
Braze는 iOS용 Apple의 기기 토큰을 사용합니다.

| **Braze 관점:**<br>Airship에서 Braze로 마이그레이션하는 과정에서 고객이 사용자와 지속적으로 커뮤니케이션(예: 푸시 알림)할 수 있도록 보장합니다. (100% Braze로의 전면 전환이든, 50% Airship 50% Braze와 같은 단계적 전환이든 모두 해당합니다.) |
{: .reset-td-br-1 aria-label="토큰 관리" }

#### 푸시 토큰 마이그레이션 {#push-token-migration}

[API를 통해 푸시 토큰을 마이그레이션]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens)하는 것이 필수입니다. 연결된 설명서에는 구체적인 단계와 예제 페이로드가 포함되어 있으며, 전체 프로세스는 다음과 같습니다:

1. [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 통해 토큰을 가져옵니다. 대량 일괄 가져오기의 경우 프로세스를 신속하게 진행할 수 있는 리소스가 준비되어 있습니다. 자세한 내용은 COM 또는 SA에 문의하세요!
2. 토큰이 Braze에 이미 존재하는 경우 무시되며, 그렇지 않으면 익명 프로필이 생성됩니다.
3. 푸시 통합에 대한 품질 보증을 수행합니다. [푸시 구성]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) 단계가 완료되었는지 확인하세요.

고객 프로필과 푸시 토큰이 별도의 위치에 저장되어 있는 경우, 먼저 푸시 토큰을 익명으로 가져온 후 기존 고객 프로필을 후속으로 마이그레이션하는 것을 권장합니다. Braze iOS SDK가 성공적으로 통합되면 토큰 확인을 자동으로 처리하므로, 이를 함께 매핑할 필요는 없습니다.

- API를 통해 사용자를 마이그레이션하는 것을 권장하지만, 정적 사용자 목록을 가져와야 하는 경우 CSV를 통해 수행할 수 있습니다. 단, CSV에서는 "push_token" 객체를 지정할 수 없으므로 **푸시 토큰은 CSV를 통해 가져올 수 없습니다**. 가져오기 템플릿을 확인하고 대시보드로 데이터를 가져오는 방법에 대해 자세히 알아보려면 [CSV 설명서]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#braze-csv-import)를 참조하세요.

{% alert note %}
푸시 토큰은 Braze 대시보드에서 `subscribed`로 표시될 수 있지만, 사용자가 Braze SDK로 세션을 시작하면 `opted-in`으로 변경됩니다.
{% endalert %}

#### 다중 푸시 토큰 {#multiple-push-tokens}

Braze에서는 사용자가 여러 개의 푸시 토큰(각 기기당 하나)을 가질 수 있으며, 모든 유효한 푸시 토큰을 타겟팅하여 여러 사용자 기기에 알림을 보낼 수 있습니다. 또한 사용자의 가장 최근 기기에만 전송하도록 Campaigns을 구성하는 것도 가능합니다.

## Campaign 구성 {#campaign-configuration}
높은 수준에서 Braze는 고객 참여 분야에서 진정으로 고유한 툴입니다. 광범위한 커스터마이징 옵션과 지속적으로 성장하는 기능 세트 덕분에 Braze로 마이그레이션된 Campaign은 이러한 툴의 이점을 활용하기 위해 재계획하는 것이 유리한 경우가 많으며, Braze의 Campaign 계획 프레임워크(자세한 내용은 담당 COM 또는 SA에 문의하세요)가 바로 이를 위해 설계되었습니다.

### 구성 {#composition}
#### 푸시 알림 {#push-notifications}
Braze는 푸시를 위해 별도의 채널(iOS용 하나, Android용 하나)이 필요합니다.

| **Braze 관점:**<br>Braze는 고객이 양보할 필요 없이 두 가지의 이점을 모두 누릴 수 있도록 합니다. 개별 채널을 최대한 활용할 수 있어 마케터에게는 더 많은 유연성을, 사용자에게는 향상된 경험을 제공합니다. 이를 통해 각 OS의 최신 기능을 채택할 수 있습니다. 예를 들어, Android는 iOS보다 먼저 리치 알림을 지원했습니다. |
{: .reset-td-br-1 aria-label="푸시 알림" }

Braze는 Braze SDK가 설치된 애플리케이션을 업데이트하지 않은 사용자에게도 푸시 알림을 보낼 수 있습니다. Braze에 유효한 푸시 토큰이 있으면 APN이 나머지를 처리하므로 Braze SDK 없이도 푸시 알림을 보낼 수 있습니다. 중요한 점은 **Braze SDK가 없는 빌드에서는 푸시 메시지 분석을 사용할 수 없다**는 것입니다.

##### 토큰 공유 {#sharing-tokens}

Braze SDK로의 마이그레이션 과정 중 계속 진행해야 하는 라이프사이클 관련 Campaign의 경우, Braze가 유효한 푸시 토큰을 수신한 경우 사용자는 Braze와 Airship 모두에서 알림을 받을 수 있습니다.

#### 메시지 센터 {#message-center}
Airship의 메시지 센터 Campaign 기능을 대체하려면 푸시 알림과 [Content Card]({{site.baseurl}}/user_guide/channels/content_cards)로 구성된 멀티채널 Campaign을 만드는 것이 좋습니다. Content Cards를 메시지 센터 형식으로 사용하는 방법에 대한 자세한 내용은 [iOS Content Card 구현 가이드]({{site.baseurl}}/developer_guide/content_cards/creating_cards#message-inbox)를 참조하세요.

### 세분화 {#segmentation}
Braze는 고객에게 풍부한 사용자 경험을 제공하기 위해 다양한 [세분화]({{site.baseurl}}/user_guide/audience/segments) 필터를 제공합니다.

| **Braze 관점**:<br>Braze의 Segments는 완전히 동적이므로 정의된 조건이 변경됨에 따라 사용자가 Segment에 진입하거나 이탈합니다. |
{: .reset-td-br-1 aria-label="세분화" }

#### 사용자 Segment 마이그레이션 {#user-segment-migration}

Braze에서 정적 Airship Segment를 직접 재생성하려면 두 가지 옵션이 있습니다:
- **API를 통한 가져오기 - 커스텀 속성 할당** (권장)<br>
[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 통해 사용자를 가져오면서 해당 사용자에게 커스텀 속성을 할당하는 것을 권장합니다. 예를 들어, 각 사용자에게 `Segment_Group_1`이라는 커스텀 속성을 `true`로 설정한 Segment를 만들 수 있습니다. 이후 해당 사용자를 세분화하려면 `Segment_Group_1`이 `true`인 모든 사용자의 [Segment를 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)하면 됩니다.<br><br>
- **CSV 사용자 가져오기 기반 필터**<br>
Braze에는 특정 CSV 가져오기에 포함된 사용자만 필터링하는 옵션이 있습니다. 이 필터링 옵션은 참여 툴의 타겟 사용자 단계에서 "`Updated/Imported via CSV`로 사용자 필터"에서 확인할 수 있습니다.
![CSV 가져오기 필터]({% image_buster /assets/img/csv_filter.png %}){: style="max-width:90%;border:0;"}
CSV 가져오기의 경우 가져온 각 사용자에 대해 외부 ID가 필요하며 **익명 또는 별칭 전용 사용자로 구성된 Segments는 가져올 수 없습니다**. 가져오기 템플릿을 확인하고 대시보드로 데이터를 가져오는 방법에 대해 자세히 알아보려면 [CSV 설명서]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#braze-csv-import)를 참조하세요.

## SDK 코드 스니펫 교체 {#replace-sdk-code-snippets}
마이그레이션을 간소화하기 위해, 코드에 존재하는 Airship SDK 스니펫과 이를 대체하는 데 필요한 해당 Braze SDK 스니펫을 아래에 정리했습니다. 다음 항목을 방문하여 시작하세요:
- [설치](#installation)
- [사용자 ID 가져오기 및 설정](#userid)
- [푸시 알림 처리](#pushnotifications)
- [분석](#analytics)
- [인앱 메시지 처리](#iammessages)
- [Content Cards 및 메시지 센터](#messagecenter)

### 설치 {#installation}
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

### 사용자 ID 가져오기 및 설정 {#userid}
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

### 푸시 알림 처리 {#pushnotifications}
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

### 분석 {#analytics}
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

### 인앱 메시지 처리 {#iammessages}
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

### Content Cards 및 메시지 센터 {#messagecenter}
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