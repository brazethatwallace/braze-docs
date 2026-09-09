---
nav_title: SDK-Integrationshandbuch (optional)
article_title: Braze SDK-Integrationsanleitung für iOS (optional)
alias: "/ios_sdk/"
description: "Dieser Leitfaden zur iOS-Integration führt Sie Schritt für Schritt durch die bewährten Verfahren bei der ersten Integration des iOS SDK und seiner Kernkomponenten in Ihre Anwendung. Diese Anleitung hilft Ihnen, eine BrazeManager.swift-Hilfsdatei zu erstellen."
page_order: 10
platform: iOS

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Braze iOS SDK-Integrationsanleitung {#braze-ios-sdk-integration-guide}

> Dieser optionale Leitfaden zur iOS-Integration führt Sie Schritt für Schritt durch die bewährten Verfahren bei der ersten Integration des iOS SDK und seiner Kernkomponenten in Ihre Anwendung. Diese Anleitung hilft Ihnen bei der Erstellung einer `BrazeManager.swift`-Hilfsdatei, die alle Abhängigkeiten vom Braze iOS SDK vom Rest Ihres produktiven Codes entkoppelt, was zu einem einzigen `import AppboyUI` in Ihrer gesamten Anwendung führt. Dieser Ansatz vermeidet Probleme, die durch übermäßige SDK-Importe entstehen, und erleichtert das Tracking, Debugging und Ändern von Code.

{% alert important %}
Diese Anleitung geht davon aus, dass Sie das [SDK bereits zu Ihrem Xcode-Projekt hinzugefügt]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) haben.
{% endalert %}

## Integrationsübersicht {#integration-overview}

Die folgenden Schritte helfen Ihnen, eine `BrazeManager`-Hilfsdatei zu erstellen, die Ihr Produktionscode aufruft. Diese Hilfsdatei behandelt alle Braze-bezogenen Abhängigkeiten, indem sie verschiedene Erweiterungen für die folgenden aufgelisteten Integrationsthemen hinzufügt. Jedes Thema enthält horizontale Tab-Schritte und Code-Snippets sowohl in Swift als auch in Objective-C. Beachten Sie, dass die Schritte für Content Cards und In-App-Nachrichten für die Integration nicht erforderlich sind, wenn Sie diese Kanäle in Ihrer Anwendung nicht nutzen möchten.

- [BrazeManager.swift erstellen](#create-brazemanagerswift)
- [SDK initialisieren](#initialize-the-sdk)
- [Push-Benachrichtigungen](#push-notifications)
- [Auf Nutzervariablen und -methoden zugreifen](#access-user-variables-and-methods)
- [Analytics protokollieren](#log-analytics)
- [In-App-Nachrichten (optional)](#in-app-messages)
- [Content Cards (optional)](#content-cards)
- [Nächste Schritte](#next-steps)

### BrazeManager.swift erstellen {#create-brazemanagerswift}

{% tabs local %}
{% tab Create BrazeManager swift %}

#### BrazeManager.swift erstellen
Um Ihre `BrazeManager.swift`-Datei aufzubauen, erstellen Sie eine neue Swift-Datei namens _BrazeManager_, die Sie an der gewünschten Stelle zu Ihrem Projekt hinzufügen. Ersetzen Sie anschließend `import Foundation` durch `import AppboyUI` für SPM (`import Appboy_iOS_SDK` für CocoaPods) und erstellen Sie dann eine `BrazeManager`-Klasse, die alle Braze-bezogenen Methoden und Variablen beherbergt. `Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager` ist eine `NSObject`-Klasse und kein Struct, damit sie ABK-Delegates wie dem `ABKInAppMessageUIDelegate` entsprechen kann.
- `BrazeManager` ist designbedingt eine Singleton-Klasse, sodass nur eine Instanz dieser Klasse verwendet wird. Dies bietet einen einheitlichen Zugriffspunkt auf das Objekt.
{% endalert %}

1. Fügen Sie eine statische Variable namens _shared_ hinzu, die die `BrazeManager`-Klasse initialisiert. Es ist garantiert, dass diese nur einmal lazily initialisiert wird.
2. Fügen Sie als Nächstes eine private Konstantenvariable namens _apiKey_ hinzu und setzen Sie sie als API-Schlüsselwert aus Ihrem Workspace im Braze-Dashboard.
3. Fügen Sie eine private berechnete Variable namens _appboyOptions_ hinzu, die Konfigurationswerte für das SDK speichert. Sie wird vorerst leer sein.

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

### SDK initialisieren {#initialize-the-sdk}

{% tabs local %}
{% tab Step 1: Initialize SDK from BrazeManager swift %}

#### SDK über BrazeManager.swift initialisieren {#initialize-sdk-from-brazemanagerswift}
Als Nächstes müssen Sie das SDK initialisieren. Dieser Leitfaden geht davon aus, dass Sie das [SDK bereits hinzugefügt]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) haben. Außerdem müssen Sie Ihren [Workspace-SDK-Endpunkt]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration#step-2-specify-your-data-cluster) und das [`LogLevel`]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#braze-log-level) in Ihrer `Info.plist`-Datei oder in `appboyOptions` festgelegt haben.

Fügen Sie die Methode `didFinishLaunchingWithOptions` aus der `AppDelegate.swift`-Datei ohne Rückgabetyp in Ihre `BrazeManager.swift`-Datei ein. Durch das Erstellen einer ähnlichen Methode in der `BrazeManager.swift`-Datei wird kein `import AppboyUI`-Statement in Ihrer `AppDelegate.swift`-Datei benötigt.

Initialisieren Sie als Nächstes das SDK mit Ihren neu deklarierten Variablen `apiKey` und `appboyOptions`.

{% alert important %}
Die Initialisierung sollte im Haupt-Thread erfolgen.
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

##### Appboy-Initialisierung in AppDelegate.swift handhaben {#handle-appboy-initialization-in-the-appdelegateswift}
Navigieren Sie als Nächstes zurück zur `AppDelegate.swift`-Datei und fügen Sie das folgende Code-Snippet in die `didFinishLaunchingWithOptions`-Methode des AppDelegate ein, um die Appboy-Initialisierung aus der `BrazeManager.swift`-Hilfsdatei zu handhaben. Denken Sie daran, dass kein `import AppboyUI`-Statement in der `AppDelegate.swift` erforderlich ist.

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
Fahren Sie mit dem Kompilieren Ihres Codes fort und starten Sie Ihre Anwendung.<br><br>An diesem Punkt sollte das SDK laufen. Überprüfen Sie in Ihrem Dashboard, dass Sitzungen protokolliert werden, bevor Sie fortfahren.
{% endalert %}

### Push-Benachrichtigungen {#push-notifications}

{% tabs local %}
{% tab Step 1: Add Push Certificate %}

#### Push-Zertifikat hinzufügen {#add-push-certificate}

Navigieren Sie zu Ihrem bestehenden Workspace im Braze-Dashboard. Laden Sie unter **Push Notification Settings** Ihre Push-Zertifikatsdatei in Ihr Braze-Dashboard hoch und speichern Sie sie.

![Braze-Dashboard Push Notification Settings mit APNs-Schlüssel-Upload-Feldern.]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Step 2: Register for Notifications %}

{% alert important %}
Überspringen Sie nicht den dedizierten Checkpoint am Ende dieses Schritts!
{% endalert %}

##### Für Push-Benachrichtigungen registrieren {#register-for-push-notifications}

Registrieren Sie sich als Nächstes für Push-Benachrichtigungen. Dieser Leitfaden geht davon aus, dass Sie Ihre [Push-Zugangsdaten korrekt eingerichtet]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) haben — sowohl in Ihrem Apple Developer Portal als auch in Ihrem Xcode-Projekt.

Der Code zur Registrierung von Push-Benachrichtigungen wird in der Methode `didFinishLaunching...` in der `BrazeManager.swift`-Datei hinzugefügt. Ihr Initialisierungscode sollte am Ende wie folgt aussehen:

1. Konfigurieren Sie die Inhalte für die Anfrage zur Autorisierung der Interaktion mit Nutzer:innen. Diese Optionen sind als Beispiel aufgeführt.
2. Fordern Sie die Autorisierung an, um Ihren Nutzer:innen Push-Benachrichtigungen zu senden. Die Antwort der Nutzer:innen, Push-Benachrichtigungen zuzulassen oder abzulehnen, wird in der Variable `granted` gespeichert.
3. Leiten Sie die Push-Autorisierungsergebnisse an Braze weiter, nachdem Nutzer:innen mit der Benachrichtigungsaufforderung interagiert haben.
4. Starten Sie den Registrierungsprozess bei APNs; dies sollte im Haupt-Thread erfolgen. Bei erfolgreicher Registrierung ruft die App die Methode `didRegisterForRemoteNotificationsWithDeviceToken` Ihres `AppDelegate`-Objekts auf.

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
Fahren Sie mit dem Kompilieren Ihres Codes fort und starten Sie Ihre Anwendung.
- Bestätigen Sie in Ihrer App, dass Sie zur Erlaubnis von Push-Benachrichtigungen aufgefordert werden, bevor Sie fortfahren.
- Wenn Sie nicht aufgefordert werden, versuchen Sie, die App zu löschen und neu zu installieren, um sicherzustellen, dass die Push-Benachrichtigungsaufforderung nicht bereits zuvor angezeigt wurde.

Stellen Sie sicher, dass Sie zur Erlaubnis von Push-Benachrichtigungen aufgefordert werden, bevor Sie fortfahren.
{% endalert %}

{% endtab %}
{% tab Step 3: Forward Methods %}

##### Push-Benachrichtigungsmethoden weiterleiten {#forward-push-notification-methods}

Leiten Sie als Nächstes die System-Push-Benachrichtigungsmethoden von `AppDelegate.swift` an `BrazeManager.swift` weiter, damit sie vom Braze iOS SDK verarbeitet werden.

###### Schritt 1: Erweiterung für Push-Benachrichtigungscode erstellen {#step-1-create-extension-for-push-notification-code}

Erstellen Sie eine Erweiterung für Ihren Push-Benachrichtigungscode in Ihrer `BrazeManager.swift`-Datei, damit er übersichtlicher lesbar ist und der Zweck in der Hilfsdatei klar erkennbar wird:

1. Nach dem Muster, kein `import AppboyUI`-Statement in Ihrem `AppDelegate` einzufügen, werden die Push-Benachrichtigungsmethoden in der `BrazeManager.swift`-Datei behandelt. Die Device-Tokens der Nutzer:innen müssen über die Methode `didRegisterForRemote...` an Braze übergeben werden. Diese Methode wird benötigt, um Silent-Push-Benachrichtigungen zu implementieren. Fügen Sie anschließend dieselbe Methode aus dem `AppDelegate` in Ihre `BrazeManager`-Klasse ein.
2. Fügen Sie die folgende Zeile innerhalb der Methode hinzu, um das Device-Token bei Braze zu registrieren. Dies ist notwendig, damit Braze das Token mit dem aktuellen Gerät verknüpfen kann.

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

###### Schritt 2: Remote-Benachrichtigungen unterstützen {#step-2-support-remote-notifications}
Fügen Sie im Tab **Signing & Capabilities** die Unterstützung für **Background Modes** hinzu und wählen Sie **Remote notifications**, um mit der Unterstützung von Remote-Push-Benachrichtigungen zu beginnen, die von Braze stammen.<br><br>![Signing & Capabilities]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### Schritt 3: Remote-Benachrichtigungsbehandlung {#step-3-remote-notification-handling}
Das Braze SDK kann Remote-Push-Benachrichtigungen verarbeiten, die von Braze stammen. Leiten Sie Remote-Benachrichtigungen an Braze weiter; das SDK ignoriert automatisch Push-Benachrichtigungen, die nicht von Braze stammen. Fügen Sie die folgende Methode in Ihrer `BrazeManager.swift`-Datei in der Push-Benachrichtigungserweiterung hinzu.

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

###### Schritt 4: Benachrichtigungsantworten weiterleiten {#step-4-forward-notification-responses}

Das Braze SDK kann die Antwort auf Push-Benachrichtigungen verarbeiten, die von Braze stammen. Leiten Sie die Antwort der Benachrichtigungen an Braze weiter; das SDK ignoriert automatisch Antworten auf Push-Benachrichtigungen, die nicht von Braze stammen. Fügen Sie die folgende Methode in Ihrer `BrazeManager.swift`-Datei hinzu:

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
Fahren Sie mit dem Kompilieren Ihres Codes fort und starten Sie Ihre Anwendung. <br><br>Versuchen Sie, sich selbst eine Push-Benachrichtigung über das Braze-Dashboard zu senden, und stellen Sie sicher, dass Analytics aus Push-Benachrichtigungen protokolliert werden, bevor Sie fortfahren.
{% endalert %}

### Auf Nutzervariablen und -methoden zugreifen {#access-user-variables-and-methods}

{% tabs local %}
{% tab Create User Variables and Methods %}

#### Nutzervariablen und -methoden erstellen {#create-user-variables-and-methods}

Als Nächstes möchten Sie einen einfachen Zugriff auf die `ABKUser`-Variablen und -Methoden. Erstellen Sie eine Erweiterung für Ihren Nutzercode in der `BrazeManager.swift`-Datei, damit er übersichtlicher lesbar ist und der Zweck in der Hilfsdatei klar erkennbar wird:

1. Ein `ABKUser`-Objekt repräsentiert eine:n bekannte:n oder anonyme:n Nutzer:in in Ihrer iOS-Anwendung. Fügen Sie eine berechnete Variable hinzu, um das `ABKUser`-Objekt abzurufen; diese Variable wird wiederverwendet, um Variablen über die:den Nutzer:in abzurufen.
2. Fragen Sie die Nutzervariable ab, um einfach auf die `userId` zuzugreifen. Neben den anderen Variablen ist das `ABKUser`-Objekt verantwortlich für (`firstName`, `lastName`, `phone`, `homeCity` usw.)
3. Setzen Sie die:den Nutzer:in, indem Sie `changeUser()` mit einer entsprechenden `userId` aufrufen.

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
Fahren Sie mit dem Kompilieren Ihres Codes fort und starten Sie Ihre Anwendung.<br><br>Versuchen Sie, Nutzer:innen über einen erfolgreichen Anmelde-/Registrierungsvorgang zu identifizieren. Stellen Sie sicher, dass Sie ein solides Verständnis davon haben, was ein geeigneter Nutzerbezeichner ist und was nicht. <br><br>Überprüfen Sie in Ihrem Dashboard, dass der Nutzerbezeichner protokolliert wird, bevor Sie fortfahren.
{% endalert %}

### Analytics protokollieren {#log-analytics}

{% tabs local %}
{% tab Step 1: Custom Events %}

#### Methode zum Protokollieren angepasster Events erstellen {#create-log-custom-event-method}

Erstellen Sie basierend auf der folgenden Braze SDK-Methode `logCustomEvent` eine entsprechende Methode.

**Braze `logCustomEvent`-Referenzmethode**<br>
Dies ist designbedingt so, da nur die `BrazeManager.swift`-Datei direkt auf die Methoden des Braze iOS SDK zugreifen kann. Durch das Erstellen einer entsprechenden Methode ist das Ergebnis dasselbe und es werden keine direkten Abhängigkeiten zum Braze iOS SDK in Ihrem Produktionscode benötigt.

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**Entsprechende Methode**<br>
Protokollieren Sie angepasste Events vom `Appboy`-Objekt zu Braze. `Properties` ist ein optionaler Parameter mit dem Standardwert nil. Angepasste Events benötigen nicht zwingend Properties, müssen aber einen Namen haben.

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

##### Methode zum Protokollieren angepasster Attribute erstellen {#create-log-custom-attributes-method}

Das SDK kann zahlreiche Typen als angepasste Attribute protokollieren. Es ist nicht notwendig, Hilfsmethoden für jeden Wertetyp zu erstellen, der gesetzt werden kann. Stattdessen wird nur eine Methode bereitgestellt, die zum passenden Wert filtern kann.

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

Angepasste Attribute werden über das `ABKUser`-Objekt protokolliert.

Erstellen Sie **eine Methode**, die alle verfügbaren Typen abdecken kann, die für ein Attribut gesetzt werden können. Fügen Sie diese Methode in Ihrer `BrazeManager.swift`-Datei in der Analytics-Erweiterung hinzu. Dies kann durch Filtern der gültigen angepassten Attributtypen und Aufrufen der Methode erreicht werden, die dem passenden Typ zugeordnet ist.

- Der Parameter `value` ist ein generischer Typ, der dem `Equatable`-Protokoll entspricht. Dies ist explizit so gemacht, damit bei einem Typ, der nicht dem entspricht, was das Braze iOS SDK erwartet, ein Kompilierungsfehler auftritt.
- Die Parameter `key` und `value` sind optionale Parameter, die innerhalb der Methode bedingt entpackt werden. Dies ist nur eine Möglichkeit, sicherzustellen, dass keine nil-Werte an das Braze iOS SDK übergeben werden.

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

##### Methode zum Protokollieren von Käufen erstellen {#create-log-purchase-method}

Erstellen Sie als Nächstes basierend auf der folgenden Braze SDK-Methode `logPurchase` eine entsprechende Methode.

**Braze `logPurchase`-Referenzmethode**<br>
Dies ist designbedingt so, da nur die `BrazeManager.swift`-Datei direkt auf die Methoden des Braze iOS SDK zugreifen kann. Durch das Erstellen einer entsprechenden Methode ist das Ergebnis dasselbe und es werden keine direkten Abhängigkeiten zum Braze iOS SDK in Ihrem Produktionscode benötigt.

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**Entsprechende Methode**<br>
Protokollieren Sie Käufe vom `Appboy`-Objekt zu Braze. Das SDK bietet mehrere Methoden zum Protokollieren von Käufen, und dies ist nur ein Beispiel. Diese Methode übernimmt auch das Erstellen der `NSDecimal`- und `UInt`-Objekte. Wie Sie diesen Teil handhaben möchten, bleibt Ihnen überlassen; hier wird nur ein Beispiel gezeigt.

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
Fahren Sie mit dem Kompilieren Ihres Codes fort und starten Sie Ihre Anwendung. <br><br>Versuchen Sie, angepasste Events zu protokollieren.<br><br>Überprüfen Sie in Ihrem Dashboard, dass die angepassten Events protokolliert werden, bevor Sie fortfahren.
{% endalert %}

### In-App-Nachrichten {#in-app-messages}

{% tabs local %}
{% tab Step 1: Conform to Delegate %}

{% alert important %}
Der folgende Abschnitt zu In-App-Nachrichten ist für die Integration nicht erforderlich, wenn Sie diesen Kanal in Ihrer Anwendung nicht nutzen möchten.
{% endalert %}

#### Dem ABKInAppMessageUIDelegate entsprechen {#conform-to-abkinappmessageuidelegate}

Aktivieren Sie als Nächstes Ihren `BrazeManager.swift`-Dateicode, damit er dem `ABKInAppMessageUIDelegate` entspricht und die zugehörigen Methoden direkt verarbeiten kann.

Der Code für die Delegate-Konformität wird in den `didFinishLaunching...`-Methoden in der `BrazeManager.swift`-Datei hinzugefügt. Ihr Initialisierungscode sollte am Ende wie folgt aussehen:

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

##### Delegate-Methoden hinzufügen {#add-delegate-methods}
Erstellen Sie als Nächstes eine Erweiterung, die dem `ABKInAppMessageUIDelegate` entspricht.

Fügen Sie das folgende Snippet im Analytics-Abschnitt hinzu. Beachten Sie, dass das `BrazeManager.swift`-Objekt als Delegate gesetzt ist; hier werden alle `ABKInAppMessageUIDelegate`-Methoden von der `BrazeManager.swift`-Datei verarbeitet.

{% alert important %}
Der `ABKInAppMessageUIDelegate` enthält keine Pflichtmethoden, aber das Folgende ist ein Beispiel für eine solche.
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
Fahren Sie mit dem Kompilieren Ihres Codes fort und starten Sie Ihre Anwendung. <br><br>Versuchen Sie, sich selbst eine In-App-Nachricht zu senden. <br><br>Setzen Sie in der `BrazeManager.swift`-Datei einen Breakpoint am Einstiegspunkt der `ABKInAppMessageUIDelegate`-Beispielmethode. Senden Sie sich selbst eine In-App-Nachricht und bestätigen Sie, dass der Breakpoint erreicht wird, bevor Sie fortfahren.
{% endalert %}

### Content Cards {#content-cards}

{% tabs local %}
{% tab Create Content Card Variables and Methods %}

{% alert important %}
Der folgende Abschnitt zu Content Cards ist für die Integration nicht erforderlich, wenn Sie diesen Kanal in Ihrer Anwendung nicht nutzen möchten.
{% endalert %}

#### Content-Card-Variablen und -Methoden erstellen {#create-content-card-variables-and-methods}

Ermöglichen Sie es Ihrem Produktionscode, den Content-Cards-View-Controller ohne unnötige `import AppboyUI`-Statements anzuzeigen.

Erstellen Sie eine Erweiterung für Ihren Content-Cards-Code in Ihrer `BrazeManager.swift`-Datei, damit er übersichtlicher lesbar ist und der Zweck in der Hilfsdatei klar erkennbar wird:

1. Zeigen Sie den `ABKContentCardsTableViewController` an. Ein optionaler `navigationController` ist der einzige benötigte Parameter, um unseren View-Controller zu präsentieren oder zu pushen.
2. Initialisieren Sie ein `ABKContentCardsTableViewController`-Objekt und ändern Sie optional den Titel. Sie müssen außerdem den initialisierten View-Controller zum Navigation-Stack hinzufügen.

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
Fahren Sie mit dem Kompilieren Ihres Codes fort und starten Sie Ihre Anwendung.<br><br>Versuchen Sie, den `ABKContentCardsTableViewController` in Ihrer Anwendung anzuzeigen, bevor Sie fortfahren.
{% endalert %}

## Nächste Schritte {#next-steps}

Herzlichen Glückwunsch! Sie haben diesen Leitfaden zur Best-Practice-Integration abgeschlossen! Eine Beispieldatei für den `BrazeManager`-Helper finden Sie auf [GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift).

Nachdem Sie alle Abhängigkeiten vom Braze iOS SDK vom Rest Ihres Produktionscodes entkoppelt haben, sehen Sie sich einige unserer optionalen erweiterten Implementierungsleitfäden an:

{% article_tiles %}
- name: Erweiterter Implementierungsleitfaden für Push-Benachrichtigungen
  link: /docs/developer_guide/platforms/legacy_sdks/ios/push_notifications/implementation_guide
  description: Optionale erweiterte Muster zur Anpassung des Verhaltens von Push-Benachrichtigungen in Ihrer iOS-App.
- name: Erweiterter Implementierungsleitfaden für In-App-Nachrichten
  link: /docs/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide
  description: Optionale erweiterte Muster zur Anpassung der Zustellung und Anzeige von In-App-Nachrichten.
- name: Erweiterter Implementierungsleitfaden für Content Cards
  link: /docs/developer_guide/platforms/legacy_sdks/ios/content_cards/implementation_guide
  description: Optionale erweiterte Muster zur Anpassung von Content-Card-Feeds und der UI.
{% endarticle_tiles %}