---
nav_title: Integration
article_title: Push-Integration für iOS
platform: iOS
page_order: 0
description: "Dieser Referenzartikel beschreibt, wie Sie Push-Benachrichtigungen in Ihre iOS-Anwendung integrieren."
channel:
  - push
search_rank: 5

local_redirect:
  ios-10-rich-notifications: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/'
local_redirect:
  creating-a-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-service-extension'
local_redirect:
  setting-up-the-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#setting-up-the-service-extension'
local_redirect:
  creating-a-rich-notification-in-your-dashboard: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-rich-notification-in-your-dashboard'
local_redirect:
  push-action-buttons-integration: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/'
local_redirect:
  step-1-adding-braze-default-push-categories: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-1-adding-braze-default-push-categories'
local_redirect:
  step-2-enable-interactive-push-handling: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-2-enable-interactive-push-handling'

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Push-Integration {#push-integration}

## 1. Schritt: Laden Sie Ihr APNs-Token / Textbaustein hoch {#step-1-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

## 2. Schritt: Push-Funktionen aktivieren {#step-2-enable-push-capabilities}

Stellen Sie in Ihren Projekteinstellungen sicher, dass unter dem Tab **Capabilities** die Funktion **Push Notifications** aktiviert ist.

![Stellen Sie in Ihren Projekteinstellungen sicher, dass unter dem Tab „Capabilities“ die Funktion „Push Notifications“ aktiviert ist.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

Wenn Sie separate Push-Zertifikate für Entwicklung und Produktion verwenden, deaktivieren Sie das Kontrollkästchen **Automatically manage signing** im Tab **General**. So können Sie für jede Build-Konfiguration unterschiedliche Provisioning-Profile auswählen, da die automatische Code-Signing-Funktion von Xcode nur für die Entwicklungssignierung vorgesehen ist.

![Xcode-Projekteinstellungen mit dem Tab „General“. In diesem Tab ist die Option „Automatically manage signing“ deaktiviert.]({% image_buster /assets/img_archive/xcode8_auto_signing.png %})

## 3. Schritt: Für Push-Benachrichtigungen Registrierung {#step-3-register-for-push-notifications}

Das entsprechende Codebeispiel muss in die `application:didFinishLaunchingWithOptions:`-Delegate-Methode Ihrer App eingebunden werden, damit die Geräte Ihrer Nutzer:innen sich bei APNs Registrierung können. Stellen Sie sicher, dass Sie den gesamten Push-Integrationscode im Hauptthread Ihrer Anwendung aufrufen.

Braze bietet außerdem Standard-Push-Kategorien für die Unterstützung von Push-Action-Buttons, die manuell zu Ihrem Push-Registrierungscode hinzugefügt werden müssen. Weitere Integrationsschritte finden Sie unter [Push-Action-Buttons]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons).

{% alert warning %}
Wenn Sie eine angepasste Push-Aufforderung implementiert haben, wie in unseren [Push-Best-Practices]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/troubleshooting) beschrieben, stellen Sie sicher, dass Sie den folgenden Code **bei jedem App-Start** aufrufen, nachdem Push-Berechtigungen für Ihre App erteilt wurden. **Apps müssen sich erneut bei APNs Registrierung, da [Geräte-Token / Textbaustein sich willkürlich ändern können](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html).**
{% endalert %}

### Verwendung des UserNotification-Frameworks (iOS 10+) {#using-usernotification-framework-ios-10}

Wenn Sie das in iOS 10 eingeführte `UserNotifications`-Framework verwenden (empfohlen), fügen Sie den folgenden Code zur `application:didFinishLaunchingWithOptions:`-Methode Ihres App-Delegates hinzu.

{% alert important %}
Das folgende Codebeispiel enthält die Integration für die vorläufige Push-Authentifizierung (Zeilen 5 und 6). Wenn Sie nicht planen, die vorläufige Autorisierung in Ihrer App zu verwenden, können Sie die Codezeilen entfernen, die `UNAuthorizationOptionProvisional` zu den `requestAuthorization`-Optionen hinzufügen.<br>Besuchen Sie [iOS-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options), um mehr über die vorläufige Push-Authentifizierung zu erfahren.
{% endalert %}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_9_x_Max) {
  UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
  center.delegate = self;
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
  }
  [center requestAuthorizationWithOptions:options
                        completionHandler:^(BOOL granted, NSError * _Nullable error) {
                          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
} else {
  UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
  [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
}
```

{% endtab %}
{% tab swift %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.delegate = self as? UNUserNotificationCenterDelegate
  var options: UNAuthorizationOptions = [.alert, .sound, .badge]
  if #available(iOS 12.0, *) {
    options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
  }
  center.requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
} else {
  let types : UIUserNotificationType = [.alert, .badge, .sound]
  let setting : UIUserNotificationSettings = UIUserNotificationSettings(types:types, categories:nil)
  UIApplication.shared.registerUserNotificationSettings(setting)
  UIApplication.shared.registerForRemoteNotifications()
}
```

{% endtab %}
{% endtabs %}


{% alert warning %}
Sie müssen Ihr Delegate-Objekt mit `center.delegate = self` synchron zuweisen, bevor Ihre App den Start abgeschlossen hat, vorzugsweise in `application:didFinishLaunchingWithOptions:`. Andernfalls kann es passieren, dass Ihre App eingehende Push-Benachrichtigungen verpasst. Besuchen Sie die Apple-Dokumentation zu [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate), um mehr zu erfahren.
{% endalert %}

### Ohne UserNotifications-Framework {#without-usernotifications-framework}

Wenn Sie das `UserNotifications`-Framework nicht verwenden, fügen Sie den folgenden Code zur `application:didFinishLaunchingWithOptions:`-Methode Ihres App-Delegates hinzu:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
[[UIApplication sharedApplication] registerForRemoteNotifications];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
let types : UIUserNotificationType = UIUserNotificationType.Badge | UIUserNotificationType.Sound | UIUserNotificationType.Alert
var setting : UIUserNotificationSettings = UIUserNotificationSettings(forTypes: types, categories: nil)
UIApplication.shared.registerUserNotificationSettings(setting)
UIApplication.shared.registerForRemoteNotifications()
```

{% endtab %}
{% endtabs %}

## 4. Schritt: Push-Token / Textbaustein bei Braze Registrierung {#step-4-register-push-tokens-with-braze}

Sobald die APNs-Registrierung abgeschlossen ist, muss die folgende Methode angepasst werden, um das resultierende `deviceToken` an Braze zu übergeben, damit Push-Benachrichtigungen für die Nutzer:innen aktiviert werden:

{% tabs %}
{% tab OBJECTIVE-C %}

Fügen Sie den folgenden Code zu Ihrer `application:didRegisterForRemoteNotificationsWithDeviceToken:`-Methode hinzu:

```objc
[[Appboy sharedInstance] registerDeviceToken:deviceToken];
```

{% endtab %}
{% tab swift %}

Fügen Sie den folgenden Code zur `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`-Methode Ihrer App hinzu:

```swift
Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Die Delegate-Methode `application:didRegisterForRemoteNotificationsWithDeviceToken:` wird jedes Mal aufgerufen, nachdem `[[UIApplication sharedApplication] registerForRemoteNotifications]` aufgerufen wurde. Wenn Sie von einem anderen Push-Dienst zu Braze migrieren und das Gerät Ihrer Nutzer:innen bereits bei APNs registriert ist, erfasst diese Methode die Token / Textbaustein aus bestehenden Registrierungen beim nächsten Aufruf, und die Nutzer:innen müssen sich nicht erneut für Push anmelden.
{% endalert %}

## 5. Schritt: Push-Handling aktivieren {#step-5-enable-push-handling}

Der folgende Code leitet empfangene Push-Benachrichtigungen an Braze weiter und ist für das Logging von Push-Analytics und die Link-Verarbeitung erforderlich. Stellen Sie sicher, dass Sie den gesamten Push-Integrationscode im Main-Thread Ihrer Anwendung aufrufen.

### iOS 10+

Wenn Sie für iOS 10+ bauen, empfehlen wir Ihnen, das `UserNotifications`-Framework zu integrieren und Folgendes zu tun:

{% tabs %}
{% tab OBJECTIVE-C %}

Fügen Sie den folgenden Code zur Methode `application:didReceiveRemoteNotification:fetchCompletionHandler:` Ihrer Anwendung hinzu:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Fügen Sie anschließend den folgenden Code zur Methode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` Ihrer App hinzu:

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                 didReceiveNotificationResponse:response
                          withCompletionHandler:completionHandler];
```

**Push-Handling im Vordergrund**

Um eine Push-Benachrichtigung anzuzeigen, während die App im Vordergrund ist, implementieren Sie `userNotificationCenter:willPresentNotification:withCompletionHandler:`:

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```

Wenn die Vordergrund-Benachrichtigung angeklickt wird, wird der iOS-10-Push-Delegate `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` aufgerufen, und Braze protokolliert ein Push-Klick-Ereignis.

{% endtab %}
{% tab swift %}

Fügen Sie den folgenden Code zur Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` Ihrer App hinzu:

```swift
Appboy.sharedInstance()?.register(application,
                                            didReceiveRemoteNotification: userInfo,
                                            fetchCompletionHandler: completionHandler)
```

Fügen Sie anschließend den folgenden Code zur Methode `userNotificationCenter(_:didReceive:withCompletionHandler:)` Ihrer App hinzu:

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                               didReceive: response,
                                               withCompletionHandler: completionHandler)
```

**Push-Handling im Vordergrund**

Um eine Push-Benachrichtigung anzuzeigen, während die App im Vordergrund ist, implementieren Sie `userNotificationCenter(_:willPresent:withCompletionHandler:)`:

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                              willPresent notification: UNNotification,
                              withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner]);
  } else {
    completionHandler([.alert]);
  }
}
```

Wenn die Vordergrund-Benachrichtigung angeklickt wird, wird der iOS-10-Push-Delegate `userNotificationCenter(_:didReceive:withCompletionHandler:)` aufgerufen, und Braze protokolliert ein Push-Klick-Ereignis.

{% endtab %}
{% endtabs %}

### Vor iOS 10 {#pre-ios-10}

iOS 10 hat das Verhalten so geändert, dass `application:didReceiveRemoteNotification:fetchCompletionHandler:` nicht mehr aufgerufen wird, wenn eine Push-Benachrichtigung angeklickt wird. Aus diesem Grund müssen Sie, wenn Sie nicht auf iOS 10+ aktualisieren und das `UserNotifications`-Framework verwenden, Braze über beide alten Delegates aufrufen, was eine Abweichung von unserer bisherigen Integration darstellt.

Für Apps, die gegen SDKs < iOS 10 gebaut werden, verwenden Sie die folgenden Anweisungen:

{% tabs %}
{% tab OBJECTIVE-C %}

Um das Open-Tracking für Push-Benachrichtigungen zu aktivieren, fügen Sie den folgenden Code zur Methode `application:didReceiveRemoteNotification:fetchCompletionHandler:` Ihrer App hinzu:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Um Push-Analytics unter iOS 10 zu unterstützen, müssen Sie außerdem den folgenden Code zur Delegate-Methode `application:didReceiveRemoteNotification:` Ihrer App hinzufügen:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo];
```

{% endtab %}
{% tab swift %}

Um das Open-Tracking für Push-Benachrichtigungen zu aktivieren, fügen Sie den folgenden Code zur Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` Ihrer App hinzu:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo,
  fetchCompletionHandler: completionHandler)
```

Um Push-Analytics unter iOS 10 zu unterstützen, müssen Sie außerdem den folgenden Code zur Delegate-Methode `application(_:didReceiveRemoteNotification:)` Ihrer App hinzufügen:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo)
```

{% endtab %}
{% endtabs %}

## 6. Schritt: Deeplinking {#step-6-deep-linking}

Deeplinking von einer Push-Benachrichtigung in die App wird automatisch über unsere Standard-Push-Integrationsdokumentation gehandhabt. Wenn Sie mehr darüber erfahren möchten, wie Sie Deeplinks zu bestimmten Stellen in Ihrer App hinzufügen, lesen Sie unsere [fortgeschrittenen Anwendungsfälle]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#linking-handling-customization).

## 7. Schritt: Unit-Tests (optional) {#step-7-unit-tests-optional}

Um die gerade durchgeführten Integrationsschritte mit Tests abzudecken, implementieren Sie [Push-Unit-Tests]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).