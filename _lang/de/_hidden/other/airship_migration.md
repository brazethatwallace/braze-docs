---
nav_title: SDK or Software-Development-Kit-Migration von Airship zu Braze
permalink: /sdk_migration_guide_airship/
hidden: true
page_type: reference
---

# Migration der SDKs von Airship zu Braze (iOS) {#migrate-sdks-from-airship-to-braze-ios}

> Wir bei Braze wissen, dass der Wechsel zu einer völlig neuen Plattform und einem neuen SDK or Software-Development-Kit entmutigend sein kann. Aber mit dem folgenden Migrationsleitfaden, den einfachen Beispielen auf Code-Ebene und dem beeindruckenden Funktionsumfang der Braze-Plattform wird Ihnen das sicher nichts ausmachen. In diesem Artikel finden Sie das Braze-Äquivalent zu vielen wichtigen Features von Airship sowie Code-Snippets für das SDK or Software-Development-Kit, die die Verwendung von Airship ersetzen und Ihre Migration schnell, einfach und schmerzlos machen.

## Über den Code hinaus {#beyond-the-code}
### Token / Textbaustein-Verwaltung {#token-management}
Braze verwendet Apples Geräte-Token / Textbaustein für iOS.

| **Braze-Perspektive:**<br>Wir stellen sicher, dass Kund:innen während der Migration von Airship zu Braze kontinuierlich mit ihren Nutzer:innen kommunizieren können (z. B. Push-Benachrichtigungen), unabhängig davon, ob es sich um eine vollständige Umstellung auf 100 % Braze oder einen schrittweisen Übergang wie 50 % Airship und 50 % Braze handelt. |
{: .reset-td-br-1 aria-label="Token / Textbaustein-Verwaltung" }

#### Migration von Push-Token / Textbaustein {#push-token-migration}

Es ist erforderlich, [Push-Token / Textbaustein über die API zu migrieren]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens). Die verlinkte Dokumentation enthält spezifische Schritte sowie ein Beispiel-Payload. Der Gesamtprozess sieht wie folgt aus:

1. Importieren Sie die Token / Textbaustein über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Für große Batch-Importe stehen Ressourcen zur Verfügung, die den Prozess beschleunigen können. Wenden Sie sich an Ihre:n COM oder SA für weitere Details!
2. Wenn das Token / Textbaustein bereits in Braze vorhanden ist, wird es ignoriert. Andernfalls wird ein anonymes Profil erstellt.
3. Führen Sie eine Qualitätssicherung der Push-Integration durch. Stellen Sie sicher, dass die Schritte zur [Konfiguration von Push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) abgeschlossen wurden.

Wenn Ihre Nutzerprofile und Push-Token / Textbaustein zufällig an verschiedenen Orten gespeichert sind, empfehlen wir, Push-Token / Textbaustein zunächst anonym zu importieren und anschließend eine separate Migration Ihrer bestehenden Nutzerprofile durchzuführen. Es ist nicht notwendig, sie miteinander zu verknüpfen, da das Braze iOS SDK or Software-Development-Kit die Token / Textbaustein-Auflösung bei erfolgreicher Integration automatisch übernimmt.

- Wir empfehlen die Migration von Nutzer:innen über die API. Falls jedoch eine statische Nutzerliste importiert werden muss, kann dies per CSV erfolgen. Beachten Sie, dass **Push-Token / Textbaustein nicht per CSV importiert werden können**, da das „push_token“-Objekt in der CSV nicht angegeben werden kann. Um ein Import-Template anzuzeigen und mehr über den Datenimport in das Dashboard zu erfahren, lesen Sie unsere [CSV-Dokumentation]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#braze-csv-import).

{% alert note %}
Push-Token / Textbaustein werden im Braze-Dashboard möglicherweise als `subscribed` angezeigt, ändern sich jedoch zu `opted-in`, sobald die Nutzer:innen eine Sitzung mit dem Braze SDK or Software-Development-Kit starten.
{% endalert %}

#### Mehrere Push-Token / Textbaustein {#multiple-push-tokens}

Bei Braze können Nutzer:innen mehrere Push-Token / Textbaustein besitzen (eines pro Gerät). Durch das Targeting aller gültigen Push-Token / Textbaustein können Sie Benachrichtigungen an mehrere Geräte senden. Es ist außerdem möglich, Campaigns so zu konfigurieren, dass sie nur an das zuletzt verwendete Gerät der Nutzer:innen gesendet werden.

## Campaign-Konfiguration {#campaign-configuration}
Auf einer übergeordneten Ebene ist Braze ein wirklich einzigartiges Tool im Bereich Customer-Engagement. Aufgrund unserer umfangreichen Anpassungsoptionen und des wachsenden Feature-Sets profitieren Campaigns, die zu Braze migriert werden, häufig von einer Neuplanung, um die Vorteile dieser Tools zu nutzen. Unser Framework für die Campaign-Planung (wenden Sie sich für weitere Details an Ihren COM oder SA) wurde genau dafür entwickelt.

### Zusammenstellung {#composition}
#### Push-Benachrichtigungen {#push-notifications}
Braze erfordert separate Kanäle für Push (einen für iOS, einen für Android).

| **Braze-Perspektive:**<br>Wir ermöglichen es unseren Kund:innen, die Vorteile beider Plattformen zu nutzen, anstatt Kompromisse eingehen zu müssen. Die Möglichkeit, den jeweiligen Kanal voll auszuschöpfen, bietet mehr Flexibilität für den Marketer und eine verbesserte Nutzererfahrung. So können wir die neuesten Features jedes Betriebssystems übernehmen – beispielsweise unterstützte Android Rich-Benachrichtigungen bereits vor iOS. |
{: .reset-td-br-1 aria-label="Push-Benachrichtigungen" }

Braze kann Push-Benachrichtigungen an Nutzer:innen senden, die ihre App mit dem installierten Braze SDK or Software-Development-Kit nicht Update or aktualisieren or aktualisieren. Sofern Braze über ein gültiges Push-Token / Textbaustein verfügt, kann Braze die Push-Benachrichtigung ohne das Braze SDK or Software-Development-Kit senden, da APNs den Representational State Transfer übernehmen. Es ist wichtig zu beachten, dass Push-Nachrichten-**Analytics für Builds ohne das Braze SDK or Software-Development-Kit nicht verfügbar sind**.

##### Tokens teilen {#sharing-tokens}

Im Fall von Lifecycle-spezifischen Campaigns, die während Ihres Migrationsprozesses zum Braze SDK or Software-Development-Kit fortgesetzt werden müssen, können Nutzer:innen möglicherweise Benachrichtigungen sowohl von Braze als auch von Airship erhalten, sofern Braze ein gültiges Push-Token / Textbaustein erhalten hat.

#### Nachrichtencenter {#message-center}
Um die Nachrichtencenter-Campaign-Funktionalität von Airship zu ersetzen, empfehlen wir die Erstellung einer Multichannel-Campaign, die aus einer Push-Benachrichtigung und einer [Content Card]({{site.baseurl}}/user_guide/channels/content_cards) besteht. Um mehr darüber zu erfahren, wie Sie Content Cards in einem Nachrichtencenter-Format verwenden können, lesen Sie unseren [iOS Content-Card-Implementierungsleitfaden]({{site.baseurl}}/developer_guide/content_cards/creating_cards#message-inbox).

### Segmentierung {#segmentation}
Braze bietet mehrere [Segmentierungs]({{site.baseurl}}/user_guide/audience/segments)-Filter, um Ihren Kund:innen ein umfangreiches Nutzererlebnis zu bieten.

| **Braze-Perspektive:**<br>Segments in Braze sind vollständig dynamisch, sodass Nutzer:innen das Segment betreten und verlassen, wenn sich die definierten Bedingungen ändern. |
{: .reset-td-br-1 aria-label="Segmentierung" }

#### Migration von Nutzer-Segments {#user-segment-migration}

Um ein statisches Airship-Segment direkt in Braze nachzubilden, gibt es zwei Optionen:
- **Import über API – Angepasstes Attribut zuweisen** (Empfohlen)<br>
Wir empfehlen, Nutzer:innen über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) zu importieren und dabei den importierten Nutzer:innen ein angepasstes Attribut zuzuweisen. Sie könnten beispielsweise ein Segment von Nutzer:innen erstellen, die jeweils ein angepasstes Attribut `Segment_Group_1` haben, das auf `true` gesetzt ist. Um diese Nutzer:innen später zu segmentieren, würden Sie [ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), das alle Nutzer:innen enthält, bei denen `Segment_Group_1` den Wert `true` hat.<br><br>
- **Filter basierend auf CSV-Nutzerimport**<br>
In Braze gibt es die Option, gezielt Nutzer:innen zu filtern, die in einem bestimmten CSV-Import enthalten sind. Diese Filteroption finden Sie während des Schritts „Zielgruppe zusammenstellen“ unserer Engagement-Tools unter „Nutzer:innen filtern nach `Updated/Imported via CSV`“.
![CSV-Import-Filter]({% image_buster /assets/img/csv_filter.png %}){: style="max-width:90%;border:0;"}
Beachten Sie, dass für CSV-Importe eine externe ID für alle importierten Nutzer:innen erforderlich ist und **Segments mit anonymen oder nur Alias-Nutzer:innen nicht importiert werden können**. Um ein Import-Template anzuzeigen und mehr über das Importieren von Daten in das Dashboard zu erfahren, lesen Sie unsere [CSV-Dokumentation]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#braze-csv-import).

## SDK or Software-Development-Kit-Code-Snippets ersetzen {#replace-sdk-code-snippets}
Um die Migration zu vereinfachen, haben wir die folgenden Airship-SDK or Software-Development-Kit-Snippets hervorgehoben, die in Ihrem Code vorhanden sind, und die entsprechenden Braze-SDK or Software-Development-Kit-Snippets bereitgestellt, die als Ersatz notwendig sind. Besuchen Sie die folgenden Themen, um loszulegen:
- [Installation](#installation)
- [Nutzer-ID abrufen und setzen](#userid)
- [Push-Benachrichtigungen verarbeiten](#pushnotifications)
- [Analytics](#analytics)
- [In-App-Nachrichten verarbeiten](#iammessages)
- [Content Cards und Nachrichtencenter](#messagecenter)

### Installation {#installation}
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

### Nutzer-ID abrufen und setzen {#userid}
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

### Push-Benachrichtigungen verarbeiten {#pushnotifications}
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

### Analytics {#analytics}
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

### In-App-Nachrichten verarbeiten {#iammessages}
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

### Content Cards und Nachrichtencenter {#messagecenter}
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