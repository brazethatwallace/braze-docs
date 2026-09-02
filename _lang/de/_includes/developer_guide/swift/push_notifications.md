## Rate-Limits

Push-Benachrichtigungen unterliegen Rate-Limits – senden Sie also ruhig so viele, wie Ihre Anwendung benötigt. iOS und die Apple-Push-Notification-Service-Server (APNs) steuern, wie oft sie zugestellt werden, und Sie bekommen keine Probleme, wenn Sie zu viele senden. Wenn Ihre Push-Benachrichtigungen gedrosselt werden, werden sie möglicherweise verzögert, bis das Gerät das nächste Mal ein Keep-Alive-Paket sendet oder eine andere Benachrichtigung empfängt.

## Push-Benachrichtigungen einrichten {#setting-up-push-notifications}

### Schritt 1: APNs-Token / Textbaustein hochladen {#step-1-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

### Schritt 2: Push-Funktionen aktivieren {#step-2-enable-push-capabilities}

Gehen Sie in Xcode zum Abschnitt **Signing & Capabilities** des Haupt-App-Targets und fügen Sie die Funktion für Push-Benachrichtigungen hinzu.

![Der Abschnitt „Signing & Capabilities“ in einem Xcode-Projekt.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

### Schritt 3: Push-Verarbeitung einrichten {#step-3-set-up-push-handling}

Sie können das Swift SDK or Software-Development-Kit verwenden, um die Verarbeitung von Remote-Benachrichtigungen, die von Braze empfangen werden, zu automatisieren. Dies ist der einfachste Weg, Push-Benachrichtigungen zu verarbeiten, und die empfohlene Methode.

{% tabs local %}
{% tab Automatisch %}
#### Schritt 3.1: Automatisierung in der Push-Eigenschaft aktivieren {#step-31-enable-automation-in-the-push-property}

Um die automatische Push-Integration zu aktivieren, setzen Sie die `automation`-Eigenschaft der `push`-Konfiguration auf `true`:

{% subtabs %}
{% subtab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endsubtab %}
{% endsubtabs %}

Dies weist das SDK or Software-Development-Kit an:
- Ihre Anwendung für Push-Benachrichtigungen im System zu Registrierung or registrieren.
- Bei der Initialisierung die Autorisierung/Berechtigung für Push-Benachrichtigungen anzufordern.
- Dynamisch Implementierungen für die systembezogenen Delegate-Methoden für Push-Benachrichtigungen bereitzustellen.

{% alert note %}
Die vom SDK or Software-Development-Kit durchgeführten Automatisierungsschritte sind mit bestehenden Push-Benachrichtigungs-Integrationen in Ihrer Codebasis kompatibel. Das SDK or Software-Development-Kit automatisiert nur die Verarbeitung von Remote-Benachrichtigungen, die von Braze empfangen werden. Alle System-Handler, die zur Verarbeitung Ihrer eigenen oder von einem Drittanbieter-SDK or Software-Development-Kit stammenden Remote-Benachrichtigungen implementiert wurden, funktionieren weiterhin, wenn `automation` aktiviert ist.
{% endalert %}

{% alert warning %}
Das SDK or Software-Development-Kit muss im Main-Thread initialisiert werden, um die Automatisierung von Push-Benachrichtigungen zu aktivieren. Die SDK or Software-Development-Kit-Initialisierung muss erfolgen, bevor die Anwendung den Start abgeschlossen hat, oder in Ihrer AppDelegate-Implementierung von [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application).
Wenn Ihre Anwendung vor der Initialisierung des SDK or Software-Development-Kit eine zusätzliche Einrichtung erfordert, lesen Sie bitte die Dokumentationsseite zur [verzögerten Initialisierung]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#step-2-set-up-delayed-initialization-optional).
{% endalert %}

#### Schritt 3.2: Einzelne Konfigurationen überschreiben (optional) {#step-32-override-individual-configurations-optional}

Für eine detailliertere Kontrolle kann jeder Automatisierungsschritt einzeln aktiviert oder deaktiviert werden:

{% subtabs %}
{% subtab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endsubtab %}
{% endsubtabs %}

Unter [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) finden Sie alle verfügbaren Optionen und unter [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) weitere Informationen zum Automatisierungsverhalten.
{% endtab %}

{% tab Manuell %}
{% alert note %}
Wenn Sie auf Push-Benachrichtigungen für zusätzliches, app-spezifisches Verhalten angewiesen sind, können Sie möglicherweise trotzdem die automatische Push-Integration anstelle der manuellen Push-Benachrichtigungs-Integration verwenden. Die Methode [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) bietet die Möglichkeit, über von Braze verarbeitete Remote-Benachrichtigungen benachrichtigt zu werden.
{% endalert %}

#### Schritt 3.1: Für Push-Benachrichtigungen bei APNs Registrierung or registrieren {#step-31-register-for-push-notifications-with-apns}

Fügen Sie das entsprechende Codebeispiel in die [`application:didFinishLaunchingWithOptions:`-Delegate-Methode](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) Ihrer App ein, damit sich die Geräte Ihrer Nutzer:innen bei APNs Registrierung or registrieren können. Stellen Sie sicher, dass Sie den gesamten Push-Integrationscode im Main-Thread Ihrer Anwendung aufrufen.

Braze bietet auch standardmäßige Push-Kategorien zur Unterstützung von Push-Action-Buttons, die manuell zu Ihrem Push-Registrierungscode hinzugefügt werden müssen. Weitere Integrationsschritte finden Sie unter [Push-Action-Buttons]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories).

Fügen Sie den folgenden Code zur Methode `application:didFinishLaunchingWithOptions:` Ihres App-Delegates hinzu.

{% alert note %}
Das folgende Codebeispiel enthält die Integration für die vorläufige Push-Authentifizierung (Zeilen 5 und 6). Wenn Sie keine vorläufige Autorisierung in Ihrer App verwenden möchten, können Sie die Codezeilen entfernen, die `UNAuthorizationOptionProvisional` zu den `requestAuthorization`-Optionen hinzufügen.<br>Besuchen Sie [iOS-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options), um mehr über die vorläufige Push-Authentifizierung zu erfahren.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

```swift
application.registerForRemoteNotifications()
let center = UNUserNotificationCenter.current()
center.setNotificationCategories(Braze.Notifications.categories)
center.delegate = self
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
center.requestAuthorization(options: options) { granted, error in
  print("Notification authorization, granted: \(granted), error: \(String(describing: error))")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
[application registerForRemoteNotifications];
UNUserNotificationCenter *center = UNUserNotificationCenter.currentNotificationCenter;
[center setNotificationCategories:BRZNotifications.categories];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
}
[center requestAuthorizationWithOptions:options
                      completionHandler:^(BOOL granted, NSError *_Nullable error) {
                        NSLog(@"Notification authorization, granted: %d, "
                              @"error: %@)",
                              granted, error);
}];
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
Sie müssen Ihr Delegate-Objekt mit `center.delegate = self` synchron zuweisen, bevor Ihre App den Start abgeschlossen hat, vorzugsweise in `application:didFinishLaunchingWithOptions:`. Andernfalls kann es passieren, dass Ihre App eingehende Push-Benachrichtigungen verpasst. Besuchen Sie Apples [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate)-Dokumentation, um mehr zu erfahren.
Wenn Ihre App `wipeData()` aufruft und später das Braze SDK or Software-Development-Kit im selben App-Lauf erneut aktiviert, müssen Sie `registerForRemoteNotifications()` erneut aufrufen, um das vom SDK or Software-Development-Kit verwendete Geräte-Token / Textbaustein wiederherzustellen.
{% endalert %}

#### Schritt 3.2: Push-Token / Textbaustein bei Braze Registrierung or registrieren {#step-32-register-push-tokens-with-braze}

Sobald die APNs-Registrierung abgeschlossen ist, übergeben Sie das resultierende `deviceToken` an Braze, um Push-Benachrichtigungen für die Nutzer:innen zu aktivieren.

{% subtabs %}
{% subtab Swift %}

Fügen Sie den folgenden Code zur Methode `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` Ihrer App hinzu:

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Fügen Sie den folgenden Code zur Methode `application:didRegisterForRemoteNotificationsWithDeviceToken:` Ihrer App hinzu:

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Die Delegate-Methode `application:didRegisterForRemoteNotificationsWithDeviceToken:` wird jedes Mal aufgerufen, nachdem `application.registerForRemoteNotifications()` aufgerufen wurde. <br><br>Wenn Sie von einem anderen Push-Dienst zu Braze migrieren und das Gerät Ihrer Nutzer:innen bereits bei APNs registriert ist, sammelt diese Methode Token / Textbaustein aus bestehenden Registrierungen beim nächsten Aufruf, und die Nutzer:innen müssen sich nicht erneut für Push anmelden.
{% endalert %}

#### Schritt 3.3: Push-Verarbeitung aktivieren {#step-33-enable-push-handling}

Leiten Sie anschließend die empfangenen Push-Benachrichtigungen an Braze weiter. Dieser Schritt ist notwendig für die Protokollierung von Push-Analytics und die Link-Verarbeitung. Stellen Sie sicher, dass Sie den gesamten Push-Integrationscode im Main-Thread Ihrer Anwendung aufrufen.

##### Standard-Push-Verarbeitung {#default-push-handling}

{% subtabs %}
{% subtab Swift %}
Um die Standard-Push-Verarbeitung von Braze zu aktivieren, fügen Sie den folgenden Code zur Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` Ihrer App hinzu:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

Fügen Sie als Nächstes den folgenden Code zur Methode `userNotificationCenter(_:didReceive:withCompletionHandler:)` Ihrer App hinzu:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
Um die Standard-Push-Verarbeitung von Braze zu aktivieren, fügen Sie den folgenden Code zur Methode `application:didReceiveRemoteNotification:fetchCompletionHandler:` Ihrer Anwendung hinzu:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleBackgroundNotificationWithUserInfo:userInfo
                                                                                                       fetchCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler(UIBackgroundFetchResultNoData);
```

Fügen Sie als Nächstes den folgenden Code zur Methode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` Ihrer App hinzu:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                                                                                  withCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler();
```
{% endsubtab %}
{% endsubtabs %}

##### Vordergrund-Push-Verarbeitung {#foreground-push-handling}

{% subtabs %}
{% subtab Swift %}
Um Vordergrund-Push-Benachrichtigungen zu aktivieren und Braze zu ermöglichen, diese beim Empfang zu erkennen, implementieren Sie `UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)`. Wenn Nutzer:innen auf Ihre Vordergrund-Benachrichtigung tippen, wird der Push-Delegate `userNotificationCenter(_:didReceive:withCompletionHandler:)` aufgerufen und Braze protokolliert das Push-Klick-Ereignis.

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  willPresent notification: UNNotification,
  withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions
) -> Void) {
  if let braze = AppDelegate.braze {
    // Forward notification payload to Braze for processing.
    braze.notifications.handleForegroundNotification(notification: notification)
  }

  // Configure application's foreground notification display options.
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner])
  } else {
    completionHandler([.alert])
  }
}
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
Um Vordergrund-Push-Benachrichtigungen zu aktivieren und Braze zu ermöglichen, diese beim Empfang zu erkennen, implementieren Sie `userNotificationCenter:willPresentNotification:withCompletionHandler:`. Wenn Nutzer:innen auf Ihre Vordergrund-Benachrichtigung tippen, wird der Push-Delegate `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` aufgerufen und Braze protokolliert das Push-Klick-Ereignis.

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (AppDelegate.braze != nil) {
    // Forward notification payload to Braze for processing.
    [AppDelegate.braze.notifications handleForegroundNotificationWithNotification:notification];
  }

  // Configure application's foreground notification display options.
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Benachrichtigungen testen {#push-testing}

Wenn Sie In-App- und Push-Benachrichtigungen über die Befehlszeile testen möchten, können Sie über CURL und die [Messaging-API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) eine einzelne Benachrichtigung über das Terminal senden. Sie müssen die folgenden Felder durch die richtigen Werte für Ihren Testfall ersetzen:

- `YOUR_API_KEY` – verfügbar unter **Einstellungen** > **API-Schlüssel**.
- `YOUR_EXTERNAL_USER_ID` – verfügbar auf der Seite **Nutzer:innen suchen**. Weitere Informationen finden Sie unter [Nutzer-IDs zuweisen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#assigning-a-user-id).
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

Im folgenden Beispiel wird die Instanz `US-01` verwendet. Wenn Sie sich nicht auf dieser Instanz befinden, sehen Sie in unserer [API-Dokumentation]({{site.baseurl}}/api/basics) nach, an welchen Endpunkt Sie Anfragen stellen müssen.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## Updates für Push-Benachrichtigungen abonnieren {#subscribing-to-push-notifications-updates}

Um auf die von Braze verarbeiteten Push-Benachrichtigungs-Payloads zuzugreifen, verwenden Sie die Methode [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/).

Mit dem Parameter `payloadTypes` können Sie festlegen, ob Sie Benachrichtigungen über Push-Öffnungsereignisse, Push-Empfangsereignisse oder beides abonnieren möchten.

{% tabs %}
{% tab Swift %}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.notifications.subscribeToUpdates(payloadTypes: [.open, .received]) { payload in
  print("Braze processed notification with title '\(payload.title)' and body '\(payload.body)'")
}
```

{% alert important %}
Beachten Sie, dass Push-Empfangsereignisse nur für Vordergrund-Benachrichtigungen und `content-available`-Hintergrund-Benachrichtigungen ausgelöst werden. Sie werden nicht für Benachrichtigungen ausgelöst, die im beendeten Zustand empfangen werden, oder für Hintergrund-Benachrichtigungen ohne das Feld `content-available`.
{% endalert %}

{% endtab %}

{% tab OBJECTIVE-C %}

```objc
NSInteger filtersValue = BRZNotificationsPayloadTypeFilter.opened.rawValue | BRZNotificationsPayloadTypeFilter.received.rawValue;
BRZNotificationsPayloadTypeFilter *filters = [[BRZNotificationsPayloadTypeFilter alloc] initWithRawValue: filtersValue];
BRZCancellable *cancellable = [notifications subscribeToUpdatesWithPayloadTypes:filters update:^(BRZNotificationsPayload * _Nonnull payload) {
  NSLog(@"Braze processed notification with title '%@' and body '%@'", payload.title, payload.body);
}];
```

{% alert important %}
Beachten Sie, dass Push-Empfangsereignisse nur für Vordergrund-Benachrichtigungen und `content-available`-Hintergrund-Benachrichtigungen ausgelöst werden. Sie werden nicht für Benachrichtigungen ausgelöst, die im beendeten Zustand empfangen werden, oder für Hintergrund-Benachrichtigungen ohne das Feld `content-available`.
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
Bei Verwendung der automatischen Push-Integration ist `subscribeToUpdates(_:)` die einzige Möglichkeit, über von Braze verarbeitete Remote-Benachrichtigungen informiert zu werden. Die Systemmethoden `UIAppDelegate` und `UNUserNotificationCenterDelegate` werden nicht aufgerufen, wenn die Benachrichtigung automatisch von Braze verarbeitet wird.
{% endalert %}

{% alert tip %}
Erstellen Sie Ihr Push-Benachrichtigungs-Abonnement in `application(_:didFinishLaunchingWithOptions:)`, um sicherzustellen, dass Ihr Abonnement ausgelöst wird, nachdem Endnutzer:innen auf eine Benachrichtigung tippen, während sich Ihre App im beendeten Zustand befindet.
{% endalert %}

## Vordergrund-Benachrichtigungen verarbeiten {#handling-foreground-notifications}

Standardmäßig zeigt iOS eine Push-Benachrichtigung nicht automatisch an, wenn sie eintrifft, während Ihre App im Vordergrund ist. Um Push-Benachrichtigungen im Vordergrund anzuzeigen und sie mit Braze Analytics zu tracken, rufen Sie die Methode `handleForegroundNotification(notification:)` innerhalb Ihrer `UNUserNotificationCenterDelegate.userNotificationCenter(_:willPresent:withCompletionHandler:)`-Implementierung auf.

### So funktioniert es {#how-it-works}

Wenn Sie `handleForegroundNotification(notification:)` aufrufen, verarbeitet Braze den Benachrichtigungs-Payload, um Analytics zu protokollieren und Deeplinks oder Button-Aktionen zu verarbeiten. Das tatsächliche Anzeigeverhalten wird durch die `UNNotificationPresentationOptions` gesteuert, die Sie an den Completion-Handler übergeben.

```swift
import BrazeKit
import UserNotifications

extension AppDelegate: UNUserNotificationCenterDelegate {
  func userNotificationCenter(
    _ center: UNUserNotificationCenter,
    willPresent notification: UNNotification,
    withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void
  ) {
    // Let Braze process the notification payload
    if let braze = AppDelegate.braze {
      braze.notifications.handleForegroundNotification(notification: notification)
    }

    // Control how the notification appears in the foreground
    if #available(iOS 14.0, *) {
      completionHandler([.banner, .list, .sound])
    } else {
      completionHandler([.alert, .sound])
    }
  }
}
```

Ein vollständiges Beispiel finden Sie im [Beispiel zur manuellen Integration von Push-Benachrichtigungen](https://github.com/braze-inc/braze-swift-sdk/blob/e31907eaa0dbd151dc2e6826de66cc494242ba60/Examples/Swift/Sources/PushNotifications-Manual/AppDelegate.swift#L1-L120) im Braze Swift SDK or Software-Development-Kit-Repository.

## Push-Primer {#push-primers}

Push-Primer-Campaigns ermutigen Ihre Nutzer:innen, Push-Benachrichtigungen auf ihrem Gerät für Ihre App zu aktivieren. Dies kann ohne SDK or Software-Development-Kit-Anpassung mit unserem [No-Code-Push-Primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) umgesetzt werden.

## Dynamisches APNs-Gateway-Management {#dynamic-apns-gateway-management}

Dynamisches Apple Push Notification Service (APNs)-Gateway-Management verbessert die Zuverlässigkeit und Effizienz von iOS-Push-Benachrichtigungen, indem es die korrekte APNs-Umgebung automatisch erkennt. Zuvor mussten Sie APNs-Umgebungen (Entwicklung oder Produktion) für Ihre Push-Benachrichtigungen manuell auswählen, was manchmal zu fehlerhaften Gateway-Konfigurationen, Zustellungsfehlern und `BadDeviceToken`-Fehlern führte.

Mit dynamischem APNs-Gateway-Management profitieren Sie von:

- **Verbesserte Zuverlässigkeit:** Benachrichtigungen werden immer an die korrekte APNs-Umgebung zugestellt, was fehlgeschlagene Zustellungen reduziert.
- **Vereinfachte Konfiguration:** Sie müssen APNs-Gateway-Einstellungen nicht mehr manuell verwalten.
- **Fehlerresilienz:** Ungültige oder fehlende Gateway-Werte werden ordnungsgemäß behandelt und gewährleisten einen unterbrechungsfreien Dienst.

### Voraussetzungen {#prerequisites}

Braze unterstützt dynamisches APNs-Gateway-Management für Push-Benachrichtigungen auf iOS mit der folgenden SDK or Software-Development-Kit-Versionsanforderung:

{% sdk_min_versions swift:10.0.0 %}

### Funktionsweise

Wenn eine iOS-App mit dem Braze Swift SDK or Software-Development-Kit integriert wird, sendet sie gerätebezogene Daten, einschließlich [`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment), an die Braze SDK or Software-Development-Kit API, sofern verfügbar. Der `apns_gateway`-Wert gibt an, ob die App die Entwicklungs- (`dev`) oder Produktions- (`prod`) APNs-Umgebung verwendet.

Braze speichert außerdem den gemeldeten Gateway-Wert für jedes Gerät. Wenn ein neuer, gültiger Gateway-Wert empfangen wird, aktualisiert Braze den gespeicherten Wert automatisch.

Wenn Braze eine Push-Benachrichtigung sendet:

- Wenn ein gültiger Gateway-Wert (dev oder prod) für das Gerät gespeichert ist, verwendet Braze diesen, um die korrekte APNs-Umgebung zu bestimmen.
- Wenn kein Gateway-Wert gespeichert ist, verwendet Braze standardmäßig die APNs-Umgebung, die auf der Seite **App-Einstellungen** konfiguriert ist.

### Häufig gestellte Fragen {#frequently-asked-questions}

#### Warum wurde dieses Feature eingeführt? {#why-was-this-feature-introduced}

Mit dynamischem APNs-Gateway-Management wird die korrekte Umgebung automatisch ausgewählt. Zuvor mussten Sie das APNs-Gateway manuell konfigurieren, was zu `BadDeviceToken`-Fehlern, Token / Textbaustein-Invalidierung und potenziellen APNs-Rate-Limiting-Problemen führen konnte.

#### Wie wirkt sich dies auf die Push-Zustellungs-Performance aus? {#how-does-this-impact-push-delivery-performance}

Dieses Feature verbessert die Zustellungsraten, indem Push-Token / Textbaustein immer an die korrekte APNs-Umgebung weitergeleitet werden und Fehler durch falsch konfigurierte Gateways vermieden werden.

#### Kann ich dieses Feature deaktivieren? {#can-i-disable-this-feature}

Dynamisches APNs-Gateway-Management ist standardmäßig aktiviert und bietet Verbesserungen der Zuverlässigkeit. Wenn Sie spezifische Anwendungsfälle haben, die eine manuelle Gateway-Auswahl erfordern, wenden Sie sich an den [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).