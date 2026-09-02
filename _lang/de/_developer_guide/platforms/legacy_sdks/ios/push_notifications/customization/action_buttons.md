---
nav_title: Aktions-Buttons
article_title: Push-Action-Buttons für iOS
platform: iOS
page_order: 1
description: "In diesem Referenzartikel erfahren Sie, wie Sie Aktions-Buttons in Ihren iOS Push-Benachrichtigungen implementieren."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Aktions-Buttons {#push-action-buttons-integration}

Das Braze iOS SDK or Software-Development-Kit unterstützt die standardmäßigen Push-Kategorien, einschließlich URL-Handling für jeden Push-Action-Button. Die Standard-Kategorien verfügen derzeit über vier Sets von Push-Action-Buttons: `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel` und `More`.

![Ein GIF, das eine Push-Nachricht zeigt, die nach unten gezogen wird, um zwei anpassbare Aktions-Buttons anzuzeigen.]({% image_buster /assets/img_archive/iOS8Action.gif %})

Um unsere Standard-Push-Kategorien zu Registrierung or registrieren, folgen Sie den Anweisungen zur Integration:

## Schritt 1: Standard-Push-Kategorien von Braze hinzufügen {#step-1-adding-braze-default-push-categories}

Verwenden Sie den folgenden Code, um sich für unsere Standard-Push-Kategorien zu Registrierung or registrieren, wenn Sie sich [für Push Registrierung or registrieren]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-4-register-push-tokens-with-braze):

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// For UserNotification.framework (iOS 10+ only)
NSSet *appboyCategories = [ABKPushUtils getAppboyUNNotificationCategorySet];
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:appboyCategories];

// For UIUserNotificationSettings (before iOS 10)
NSSet *appboyCategories = [ABKPushUtils getAppboyUIUserNotificationCategorySet];
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeBadge
                                                                         categories:appboyCategories];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
// For UserNotification.framework (iOS 10+ only)
let appboyCategories = ABKPushUtils.getAppboyUNNotificationCategorySet()
UNUserNotificationCenter.current().setNotificationCategories(appboyCategories)

// For UIUserNotificationSettings (before iOS 10)
let appboyCategories = ABKPushUtils.getAppboyUIUserNotificationCategorySet()
let settings = UIUserNotificationSettings.init(types: .badge, categories: appboyCategories)
UIApplication.shared.registerUserNotificationSettings(settings)
```

{% endtab %}
{% endtabs %}

Das Tippen auf Push-Action-Buttons mit Hintergrundaktivierungsmodus schließt lediglich die Benachrichtigung und öffnet nicht die App. Wenn Nutzer:innen die App das nächste Mal öffnen, werden die Klick-Analytics für diese Aktionen an den Server übermittelt.

Wenn Sie Ihre eigenen angepassten Benachrichtigungskategorien erstellen möchten, lesen Sie den Abschnitt [Anpassung von Aktions-Buttons]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons#push-category-customization).

## Schritt 2: Interaktive Push-Behandlung aktivieren {#step-2-enable-interactive-push-handling}

Wenn Sie das `UNNotification`-Framework verwenden und Braze-[Delegates]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling) implementiert haben, sollten Sie diese Methode bereits integriert haben.

Um unsere Behandlung von Push-Action-Buttons zu aktivieren, einschließlich Klick-Analytics und URL-Routing, fügen Sie den folgenden Code zur Delegate-Methode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` Ihrer App hinzu:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                           didReceiveNotificationResponse:response
                               withCompletionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                                didReceive: response,
                                                withCompletionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

Wenn Sie das UNNotification-Framework nicht verwenden, müssen Sie den folgenden Code zu `application:handleActionWithIdentifier:forRemoteNotification:completionHandler:` Ihrer App hinzufügen, um unsere Behandlung von Push-Action-Buttons zu aktivieren:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] getActionWithIdentifier:identifier
                           forRemoteNotification:userInfo
                               completionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.getActionWithIdentifier(identifier,
                                                 forRemoteNotification: userInfo,,
                                                 completionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Wir empfehlen dringend, dass Nutzer:innen, die `handleActionWithIdentifier` verwenden, auf das `UNNotification`-Framework umsteigen. Wir empfehlen dies aufgrund der Einstellung von [`handleActionWithIdentifier`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc).
{% endalert %}

## Anpassung der Push-Kategorie {#push-category-customization}

Zusätzlich zu einem Satz von [Standard-Push-Kategorien]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons) unterstützt Braze angepasste Benachrichtigungskategorien und -aktionen. Nachdem Sie Kategorien in Ihrer App registriert haben, können Sie das Braze-Dashboard verwenden, um Benachrichtigungskategorien an Ihre Nutzer:innen zu senden.

Wenn Sie das `UserNotifications`-Framework nicht verwenden, lesen Sie die Dokumentation zu [alternativen Kategorien](https://developer.apple.com/documentation/usernotifications/unnotificationcategory).

Diese Kategorien können dann über unser Dashboard Push-Benachrichtigungen zugewiesen werden, um die Aktions-Button-Konfigurationen Ihres Designs auszulösen. Hier ist ein Beispiel, das die auf dem Gerät angezeigte `LIKE_CATEGORY` nutzt:

![Eine Push-Nachricht mit zwei Push-Action-Buttons „unlike“ und „like“.]({% image_buster /assets/img_archive/push_example_category.png %})