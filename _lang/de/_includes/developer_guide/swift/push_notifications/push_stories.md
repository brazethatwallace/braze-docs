{% multi_lang_include developer_guide/prerequisites/swift.md %} Sie müssen außerdem [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift), was die Implementierung des `UNNotification`-Frameworks beinhaltet.

Die folgende Mindestversion des SDK ist erforderlich, um Push-Storys zu empfangen:

{% sdk_min_versions swift:5.0.0 %}

## Einrichten von Push-Storys {#setting-up-push-stories}

### 1. Schritt: Hinzufügen des Ziels für die Erweiterung für Benachrichtigungsinhalte {#notification-content-extension}

Wählen Sie in Ihrem App-Projekt das Menü **File > New > Target** und fügen Sie ein neues `Notification Content Extension`-Ziel hinzu und aktivieren Sie es.

![]({% image_buster /assets/img/swift/push_story/add_content_extension.png %})

Xcode sollte ein neues Ziel generieren und automatisch folgende Dateien für Sie anlegen:

- `NotificationViewController.swift`
- `MainInterface.storyboard`

### 2. Schritt: Funktionen aktivieren {#enable-capabilities}

Fügen Sie in Xcode die Funktion „Hintergrundmodi“ über den Bereich **Signing & Capabilities** zum Hauptziel der App hinzu. Aktivieren Sie die Kontrollkästchen **Background fetch** und **Remote notifications**.

![]({% image_buster /assets/img/swift/push_story/enable_background_mode.png %})

#### Hinzufügen einer App-Gruppe {#adding-an-app-group}

Fügen Sie außerdem im Bereich **Signing & Capabilities** in Xcode die Funktion „App-Gruppen“ zu Ihrem Haupt-App-Ziel sowie zu den Zielen der Notification Content Extension hinzu. Klicken Sie dann auf die Schaltfläche **+**. Verwenden Sie die Bundle-ID Ihrer App, um die App-Gruppe zu erstellen. Wenn die Bundle-ID Ihrer App beispielsweise `com.company.appname` lautet, können Sie die App-Gruppe `group.com.company.appname.xyz` nennen.

{% alert important %}
App-Gruppen beziehen sich in diesem Zusammenhang auf die [App-Gruppen-Berechtigung](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) von Apple und nicht auf die ID Ihres Braze Workspace (früher App-Gruppe).
{% endalert %}

Wenn Sie Ihre App nicht zu einer App-Gruppe hinzufügen, kann es sein, dass Ihre App bestimmte Felder aus der Push-Nutzlast nicht ausfüllt und nicht vollständig wie erwartet funktioniert.

### 3. Schritt: Hinzufügen des Push-Story-Frameworks zu Ihrer App

{% tabs local %}
{% tab Swift-Paketmanager %}

Nachdem Sie den [Leitfaden für die Integration des Swift-Paketmanagers]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/) befolgt haben, fügen Sie `BrazePushStory` zur `Notification Content Extension` hinzu:

![Wählen Sie in Xcode unter „Frameworks und Bibliotheken“ das Symbol „+“, um ein Framework hinzuzufügen.]({% image_buster /assets/img/swift/push_story/spm1.png %})

![]({% image_buster /assets/img/swift/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Fügen Sie die folgende Zeile in Ihr Podfile ein:

```ruby
target 'YourAppTarget' do
pod 'BrazeKit'
pod 'BrazeUI'
pod 'BrazeLocation'
end

target 'YourNotificationContentExtensionTarget' do
pod 'BrazePushStory'
end

# Only include the below if you want to also integrate Rich Push
target 'YourNotificationServiceExtensionTarget' do
pod 'BrazeNotificationService'
end
```

{% alert note %}
Eine Anleitung zur Implementierung von Rich Push finden Sie unter [Rich-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/?tab=swift%20package%20manager).
{% endalert %}

Nachdem Sie das Podfile aktualisiert haben, wechseln Sie in Ihrem Terminal in das Verzeichnis Ihres Xcode-App-Projekts und führen Sie `pod install` aus.

{% endtab %}
{% tab Manuell %}

Laden Sie die neueste Version der `BrazePushStory.zip` von der [GitHub-Release-Seite](https://github.com/braze-inc/braze-swift-sdk/releases) herunter, extrahieren Sie sie und fügen Sie `BrazePushStory.xcframework` zur `Notification Content Extension` Ihres Projekts hinzu.

![]({% image_buster /assets/img/swift/push_story/manual1.png %})

{% alert important %}
Stellen Sie sicher, dass unter der Spalte **Embed** die Option **Do Not Embed** für **BrazePushStory.xcframework** ausgewählt ist.
{% endalert %}

{% endtab %}
{% endtabs %}

### 4. Schritt: View-Controller für Benachrichtigungen aktualisieren

Fügen Sie in `NotificationViewController.swift` die folgende Zeile hinzu, um die Header-Dateien zu importieren:

```swift
import BrazePushStory
```

Ersetzen Sie als Nächstes die Standard-Implementierung durch die Vererbung von [`BrazePushStory.NotificationViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/):

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

#### Benutzerdefinierte Handhabung von Push-Story-Ereignissen {#custom-handling-push-story-events}

Wenn Sie Ihre eigene angepasste Logik zur Verarbeitung von Push-Story-Benachrichtigungs-Events implementieren möchten, vererben Sie `BrazePushStory.NotificationViewController` wie oben beschrieben und überschreiben Sie die [`didReceive`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/didreceive(_:))-Methoden wie folgt:

```swift
import BrazePushStory
import UserNotifications
import UserNotificationsUI

class NotificationViewController: BrazePushStory.NotificationViewController {
  override func didReceive(_ notification: UNNotification) {
    super.didReceive(notification)

    // Custom handling logic
  }

  override func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    super.didReceive(response, completionHandler: completion)

    // Custom handling logic
  }
}
```

### 5. Schritt: Plist-Datei der Erweiterung für Benachrichtigungsinhalte anpassen

Öffnen Sie die Datei `Info.plist` der `Notification Content Extension`, fügen Sie dann unter `NSExtension \ NSExtensionAttributes` die folgenden Schlüssel hinzu und ändern Sie sie:

| Schlüssel                                        | Typ      | Wert                   |
|--------------------------------------------------|----------|------------------------|
| `UNNotificationExtensionCategory`                | String   | `ab_cat_push_story_v2` |
| `UNNotificationExtensionDefaultContentHidden`    | Boolesch | `YES`                  |
| `UNNotificationExtensionInitialContentSizeRatio` | Zahl     | `0.6`                  |
| `UNNotificationExtensionUserInteractionEnabled`  | Boolesch | `YES`                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="5. Schritt: Plist-Datei der Erweiterung für Benachrichtigungsinhalte anpassen" }

Fügen Sie zusätzlich das folgende `Braze`-Wörterbuch der obersten Ebene in dieselbe `Info.plist`-Datei ein und ersetzen Sie dabei `REPLACE_WITH_APPGROUP` durch die in [Schritt 2](#enable-capabilities) erstellte App-Gruppe:

| Schlüssel        | Typ    | Wert                   |
|------------------|--------|------------------------|
| `Braze.AppGroup` | String | `REPLACE_WITH_APPGROUP`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="5. Schritt: Plist-Datei der Erweiterung für Benachrichtigungsinhalte anpassen" }

Ihre `Info.plist`-Datei sollte dem folgenden Bild entsprechen:

![]({% image_buster /assets/img/swift/push_story/notificationcontentextension_plist.png %})

### 6. Schritt: Braze-Integration in der Haupt-App aktualisieren {#update-braze}

Weisen Sie vor der Initialisierung von Braze der Eigenschaft [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) der Braze-Konfiguration den Namen Ihrer App-Gruppe zu.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```
