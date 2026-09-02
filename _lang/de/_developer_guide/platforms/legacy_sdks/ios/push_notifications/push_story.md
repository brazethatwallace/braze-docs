---
nav_title: Push Stories
article_title: Push Stories für iOS
platform: iOS
page_order: 27
description: "Dieser Referenzartikel beschreibt, wie Sie Push Stories für Ihre iOS-Anwendung einrichten."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Push Story einrichten {#push-story-setup}

Die Push Story-Funktion erfordert das `UNNotification`-Framework und iOS 10. Das Feature ist erst ab iOS SDK or Software-Development-Kit Version 3.2.1 verfügbar.

## 1. Schritt: Push in Ihrer App aktivieren {#step-1-enable-push-in-your-app}

Folgen Sie der [Integration von Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration), um Push in Ihrer App zu aktivieren.

## 2. Schritt: Notification Content Extension-Ziel hinzufügen {#step-2-adding-the-notification-content-extension-target}

Wählen Sie in Ihrem App-Projekt das Menü **File > New > Target...** und fügen Sie ein neues `Notification Content Extension`-Ziel hinzu und aktivieren Sie es.

![Wählen Sie in Ihrem App-Projekt das Menü „File > New > Target...“ und fügen Sie ein neues Notification Content Extension-Ziel hinzu und aktivieren Sie es.]({% image_buster /assets/img/ios/push_story/add_content_extension.png %})

Xcode sollte ein neues Ziel generieren und automatisch folgende Dateien für Sie anlegen:

{% tabs %}
{% tab OBJECTIVE-C %}

- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

{% endtab %}
{% tab swift %}

- `NotificationViewController.swift`
- `MainInterface.storyboard`

{% endtab %}
{% endtabs %}

## 3. Schritt: Fähigkeiten aktivieren {#step-3-enable-capabilities}

Die Push Story-Funktion erfordert den Hintergrundmodus im Abschnitt **Capabilities** des Hauptziels der App. Nachdem Sie die Hintergrundmodi aktiviert haben, wählen Sie **Background fetch** und **Remote notifications**.

![Die Push Story-Funktion erfordert den Hintergrundmodus im Abschnitt „Capabilities“ des Hauptziels der App. Nachdem Sie die Hintergrundmodi aktiviert haben, wählen Sie „Background fetch“ und „Remote notifications“.]({% image_buster /assets/img/ios/push_story/enable_background_mode.png %})

### App-Gruppe hinzufügen {#adding-an-app-group}

Sie müssen außerdem `Capability App Groups` hinzufügen. Wenn Sie noch keine App-Gruppe in Ihrer App haben, gehen Sie zur **Capability** des Hauptziels der App, schalten Sie die `App Groups` ein und klicken Sie auf die Schaltfläche **+**. Verwenden Sie die Bundle-ID Ihrer App, um die App-Gruppe zu erstellen. Wenn die Bundle-ID Ihrer App beispielsweise `com.company.appname` lautet, können Sie die App-Gruppe `group.com.company.appname.xyz` nennen. Sie müssen `App Groups` sowohl für die Haupt-App als auch für die Ziele der Inhaltserweiterung aktivieren.

{% alert important %}
`App Groups` bezieht sich in diesem Zusammenhang auf die [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) von Apple und nicht auf Ihre Braze-Workspace-ID (früher App-Gruppe).
{% endalert %}

Wenn Sie Ihre App nicht zu einer App-Gruppe hinzufügen, kann es sein, dass Ihre App bestimmte Felder aus der Push-Nutzlast nicht ausfüllt und nicht vollständig wie erwartet funktioniert.

## 4. Schritt: Push Story-Framework zu Ihrer App hinzufügen {#step-4-adding-the-push-story-framework-to-your-app}

{% tabs local %}
{% tab Swift-Paketmanager %}

Nachdem Sie den [Leitfaden für die Integration des Swift-Paketmanagers]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager) befolgt haben, fügen Sie `AppboyPushStory` zur `Notification Content Extension` hinzu:

![Wählen Sie in Xcode unter „Frameworks und Bibliotheken“ das Symbol „+“, um ein Framework hinzuzufügen.]({% image_buster /assets/img/ios/push_story/spm1.png %})

![Nachdem Sie den Leitfaden für die Integration des Swift-Paketmanagers befolgt haben, fügen Sie AppboyPushStory zur Notification Content Extension hinzu.]({% image_buster /assets/img/ios/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Fügen Sie die folgende Zeile in Ihr Podfile ein:

```ruby
target 'YourContentExtensionTarget' do
  pod 'Appboy-Push-Story'
end
```

Navigieren Sie nach der Aktualisierung des Podfile in Ihrem Terminal zum Verzeichnis Ihres Xcode-App-Projekts und führen Sie `pod install` aus.

{% endtab %}
{% tab Manuell %}

Laden Sie die neueste Version der `AppboyPushStory.zip` von der [GitHub-Release-Seite](https://github.com/Appboy/appboy-ios-sdk/releases) herunter, extrahieren Sie sie und fügen Sie der `Notification Content Extension` Ihres Projekts die folgenden Dateien hinzu:
- `Resources/ABKPageView.nib`
- `AppboyPushStory.xcframework`

![Laden Sie die neueste AppboyPushStory.zip von der GitHub-Release-Seite herunter, extrahieren Sie sie und fügen Sie die folgenden Dateien zur Notification Content Extension Ihres Projekts hinzu.]({% image_buster /assets/img/ios/push_story/manual1.png %})

{% alert important %}
Stellen Sie sicher, dass unter der Spalte **Embed** die Option **Do Not Embed** für **AppboyPushStory.xcframework** ausgewählt ist.
{% endalert %}

Fügen Sie unter **Build Settings > Other Linker Flags** das Flag `-ObjC` zur `Notification Content Extension` Ihres Projekts hinzu.

{% endtab %}
{% endtabs %}

## 5. Schritt: View-Controller für Benachrichtigungen Update or aktualisieren or aktualisieren {#step-5-updating-your-notification-view-controller}

{% tabs %}
{% tab OBJECTIVE-C %}

Fügen Sie in Ihrer `NotificationViewController.h` die folgenden Zeilen hinzu, um neue Eigenschaften hinzuzufügen und die Header-Dateien zu importieren:

```objc
#import <AppboyPushStory/AppboyPushStory.h>
```

```objc
@property (nonatomic) IBOutlet ABKStoriesView *storiesView;
@property (nonatomic) ABKStoriesViewDataSource *dataSource;
```

Entfernen Sie in Ihrer `NotificationViewController.m` die Standardimplementierung und fügen Sie folgenden Code hinzu:

```objc
@implementation NotificationViewController

- (void)didReceiveNotification:(UNNotification *)notification {
  self.dataSource = [[ABKStoriesViewDataSource alloc] initWithNotification:notification
                                                               storiesView:self.storiesView
                                                                  appGroup:@"YOUR-APP-GROUP-IDENTIFIER"];
}

- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response
                     completionHandler:(void (^)(UNNotificationContentExtensionResponseOption option))completion {
  UNNotificationContentExtensionResponseOption option = [self.dataSource didReceiveNotificationResponse:response];
  completion(option);
}

- (void)viewWillDisappear:(BOOL)animated {
  [self.dataSource viewWillDisappear];
  [super viewWillDisappear:animated];
}

@end
```

{% endtab %}
{% tab swift %}

Fügen Sie in Ihrer `NotificationViewController.swift` die folgende Zeile hinzu, um die Header-Dateien zu importieren:

```swift
import AppboyPushStory
```

Entfernen Sie als Nächstes die Standardimplementierung und fügen Sie den folgenden Code hinzu:

```swift
class NotificationViewController: UIViewController, UNNotificationContentExtension {

  @IBOutlet weak var storiesView: ABKStoriesView!
  var dataSource: ABKStoriesViewDataSource?

  func didReceive(_ notification: UNNotification) {
    dataSource = ABKStoriesViewDataSource(notification: notification, storiesView: storiesView, appGroup: "YOUR-APP-GROUP-IDENTIFIER")
  }

  func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    if dataSource != nil {
      let option: UNNotificationContentExtensionResponseOption = dataSource!.didReceive(response)
      completion(option)
    }
  }

  override func viewWillDisappear(_ animated: Bool) {
    dataSource?.viewWillDisappear()
    super.viewWillDisappear(animated)
  }
}
```

{% endtab %}
{% endtabs %}

## 6. Schritt: Storyboard der Notification Content Extension festlegen {#step-6-set-the-notification-content-extension-storyboard}

Öffnen Sie das Storyboard der `Notification Content Extension` und platzieren Sie eine neue `UIView` im View-Controller für Benachrichtigungen. Benennen Sie die Klasse in `ABKStoriesView` um. Legen Sie Breite und Höhe der Ansicht so fest, dass sie automatisch an den Rahmen der Hauptansicht des View-Controllers für Benachrichtigungen angepasst werden.

![Öffnen Sie das Storyboard der Notification Content Extension und platzieren Sie eine neue UIView im View-Controller für Benachrichtigungen. Benennen Sie die Klasse in ABKStoriesView um. Legen Sie Breite und Höhe der Ansicht so fest, dass sie automatisch an den Rahmen der Hauptansicht angepasst werden.]({% image_buster /assets/img/ios/push_story/abkstoriesview_class.png %})

![Öffnen Sie das Storyboard der Notification Content Extension und platzieren Sie eine neue UIView im View-Controller für Benachrichtigungen. Benennen Sie die Klasse in ABKStoriesView um. Legen Sie Breite und Höhe der Ansicht so fest, dass sie automatisch an den Rahmen der Hauptansicht angepasst werden.]({% image_buster /assets/img/ios/push_story/abkstoriesview_size.png %})

Verknüpfen Sie als Nächstes das IBOutlet `storiesView` des View-Controllers für Benachrichtigungen mit der hinzugefügten `ABKStoriesView`.

![Screenshot zu Schritt 6: Storyboard der Notification Content Extension festlegen.]({% image_buster /assets/img/ios/push_story/abkstoriesview_outlet.png %})

## 7. Schritt: Plist-Datei der Notification Content Extension anpassen {#step-7-set-the-notification-content-extension-plist}

Öffnen Sie die Datei `Info.plist` der `Notification Content Extension` und fügen Sie unter `NSExtension \ NSExtensionAttributes` die folgenden Schlüssel hinzu und ändern Sie sie:

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2` (Typ `String`)
`UNNotificationExtensionDefaultContentHidden` = `YES` (Typ `Boolean`)
`UNNotificationExtensionInitialContentSizeRatio` = `0.65` (Typ `Number`)

![Screenshot zu Schritt 7: Plist-Datei der Notification Content Extension anpassen.]({% image_buster /assets/img/ios/push_story/notificationcontentextension_plist.png %})

## 8. Schritt: Braze-Integration in Ihrer Hauptanwendung Update or aktualisieren or aktualisieren {#step-8-updating-the-braze-integration-in-your-main-app}

### Option 1: Laufzeit {#option-1-runtime}

Fügen Sie in dem Wörterbuch `appboyOptions`, das zur Konfiguration Ihrer Braze-Instanz verwendet wird, den Eintrag `ABKPushStoryAppGroupKey` hinzu und legen Sie den Wert auf den API-Bezeichner Ihres Workspace fest.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKPushStoryAppGroupKey] = @"YOUR-APP-GROUP-IDENTIFIER";
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKPushStoryAppGroupKey : "YOUR-APP-GROUP-IDENTIFIER"
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endtab %}
{% endtabs %}

#### Option 2: Info.plist {#option-2-infoplist}

Um den Push Story-Workspace über Ihre Datei `Info.plist` zu konfigurieren, können Sie alternativ ein Wörterbuch mit dem Namen `Braze` zu Ihrer Datei `Info.plist` hinzufügen. Fügen Sie im Wörterbuch `Braze` den String-Untereintrag `PushStoryAppGroup` hinzu und legen Sie den Wert auf den Bezeichner Ihres Workspace fest. Beachten Sie, dass vor Braze iOS SDK or Software-Development-Kit v4.0.2 der Wörterbuchschlüssel `Appboy` anstelle von `Braze` verwendet werden muss.

## Nächste Schritte {#next-steps}

Sehen Sie sich als Nächstes die Schritte zur Integration von [Aktions-Buttons]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons) an, die erforderlich sind, damit Buttons in einer Push Story-Nachricht angezeigt werden.