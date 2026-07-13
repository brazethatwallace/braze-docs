---
nav_title: "Push Primer"
article_title: Push Primer für iOS
page_order: 6
page_type: reference
description: "Dieser Referenzartikel beschreibt die Integration von iOS-Push-Primern."
platform: iOS
channel:
  - push
noindex: true
alias: /push_primer/
---

{% multi_lang_include deprecations/objective-c.md %}

# Push-Primer-Integration {#push-primer-integration}

Push-Primer-Campaigns ermutigen Ihre Nutzer:innen, Push auf ihrem Gerät für Ihre App zu aktivieren. Die Erlaubnis von Nutzer:innen einzuholen, um Nachrichten direkt an ihre Geräte zu senden, kann komplex sein, aber unsere Anleitungen können Ihnen dabei helfen! Dieser Leitfaden beschreibt die Schritte, die Entwickler:innen für die Integration von Push Priming durchführen müssen.

## 1. Schritt: Snippet in die Datei AppDelegate.m einfügen {#step-1-add-snippet-in-appdelegatem-file}

Fügen Sie die folgende Codezeile anstelle der Standardintegration in Ihre `AppDelegate.m`-Datei ein:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
...
if (@available(iOS 10.0, *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [center getNotificationSettingsWithCompletionHandler:^(UNNotificationSettings * _Nonnull settings) {
      if (settings.authorizationStatus != UNAuthorizationStatusNotDetermined) {
        // authorization has already been requested, need to follow usual steps
        [center requestAuthorizationWithOptions:(UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge) completionHandler:^(BOOL granted, NSError * _Nullable error) {
          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
        }];
        center.delegate = self;
        [center setNotificationCategories:[ABKPushUtils getAppboyUNNotificationCategorySet]];
        [[UIApplication sharedApplication] registerForRemoteNotifications];
      }
    }];
  } else {
    UIApplication *sharedApplication = [UIApplication sharedApplication];
    UIUserNotificationSettings *notificationSettings = [sharedApplication currentUserNotificationSettings];
    if (notificationSettings.types) {
      UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:[ABKPushUtils getAppboyUIUserNotificationCategorySet]];
      [sharedApplication registerUserNotificationSettings:settings];
      [sharedApplication registerForRemoteNotifications];
    }
  }
```
{% endtab %}
{% tab swift %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.getNotificationSettings(completionHandler: { (settings) in
    if settings.authorizationStatus != .notDetermined {
      // authorization has already been requested, need to follow usual steps
      center.requestAuthorization(options: [.alert, .sound, .badge]) { (granted, error) in
      Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
      }
      center.delegate = self as? UNUserNotificationCenterDelegate
      center.setNotificationCategories(ABKPushUtils.getAppboyUNNotificationCategorySet())
      UIApplication.shared.registerForRemoteNotifications()
    }
  })
} else {
  let notificationSettiings = UIApplication.shared.currentUserNotificationSettings
  if notificationSettiings?.types != nil {
    let setting = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories:nil)
    UIApplication.shared.registerUserNotificationSettings(setting)
    UIApplication.shared.registerForRemoteNotifications()
  }
}
```
{% endtab %}
{% endtabs %}

## 2. Schritt: Prüfung für angepasste Events an die Datei AppDelegate.m anhängen {#step-2-append-custom-event-checker-to-appdelegatem-file}

Das folgende Code-Snippet prüft, ob ein angepasstes Event ausgelöst werden muss. Fügen Sie die folgende Codezeile in Ihre `AppDelegate.m`-Datei ein.

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
if (@available(iOS 10.0, *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [center getNotificationSettingsWithCompletionHandler:^(UNNotificationSettings * _Nonnull settings) {
      if (settings.authorizationStatus == UNAuthorizationStatusNotDetermined) {
        // ...
        // fire custom event
        // ...
      }
    }];
  } else {
    UIUserNotificationSettings *notificationSettings = [[UIApplication sharedApplication] currentUserNotificationSettings];
    if (!notificationSettings.types) {
        // …
        // fire custom event
        // ...
    }
  }
```
{% endtab %}
{% tab swift %}
```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.getNotificationSettings(completionHandler: { (settings) in
    if settings.authorizationStatus == .notDetermined {
      // ...
      // fire custom event
      // ...
    }
  })
} else {
let notificationSettiings = UIApplication.shared.currentUserNotificationSettings
  if notificationSettiings?.types != nil {
    // ...
    // fire custom event
    // ...
  }
}
```
{% endtab %}
{% endtabs %}

## 3. Schritt: Deeplink-Handler einrichten {#step-3-set-up-a-deep-link-handler}

Platzieren Sie das folgende Code-Snippet in Ihrem Deeplink-Handling-Code. Sie sollten diesen Deeplinking-Code nur für Ihre Push-Primer-In-App-Nachricht ausführen.

Weitere Informationen über Deeplinking finden Sie unter [Anpassung der Linkbehandlung]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking#linking-handling-customization).

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
  // ...
  // check that this deep link relates to the push prompt
  // ...
  if (@available(iOS 10.0, *)) {
    UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
    [center requestAuthorizationWithOptions:(UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge) completionHandler:^(BOOL granted, NSError * _Nullable error) {
      [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
    }];
    center.delegate = self;
    [center setNotificationCategories:[ABKPushUtils getAppboyUNNotificationCategorySet]];
    [[UIApplication sharedApplication] registerForRemoteNotifications];
  } else {
    UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:[ABKPushUtils getAppboyUIUserNotificationCategorySet]];
      UIApplication *sharedApplication = [UIApplication sharedApplication];
      [sharedApplication registerUserNotificationSettings:settings];
      [sharedApplication registerForRemoteNotifications];
  }
```
{% endtab %}
{% tab swift %}

```swift
  // ...
  // check that this deep link relates to the push prompt
  // ...
  if #available(iOS 10, *) {
    let center = UNUserNotificationCenter.current()
    center.delegate = self as? UNUserNotificationCenterDelegate
    center.requestAuthorization(options: [.alert, .sound, .badge]) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
  } else {
    let setting = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories:nil)
    UIApplication.shared.registerUserNotificationSettings(setting)
    UIApplication.shared.registerForRemoteNotifications()
  }
```
{% endtab %}
{% endtabs %}