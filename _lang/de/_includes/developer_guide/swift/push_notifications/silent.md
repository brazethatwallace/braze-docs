{% multi_lang_include developer_guide/prerequisites/swift.md %} Sie müssen auch [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## iOS-Einschränkungen {#ios-limitations}

Das iOS-Betriebssystem kann Benachrichtigungen für einige Features einschränken. Sollten Sie Schwierigkeiten mit diesen Features haben, könnte das iOS-Gate für stille Benachrichtigungen die Ursache sein. Weitere Einzelheiten finden Sie in der Dokumentation zu Apples [Instanz-Methode](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) und [nicht empfangenen Benachrichtigungen](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23).

## Stille Push-Benachrichtigungen einrichten {#setting-up-silent-push-notifications}

Wenn Sie stille Push-Benachrichtigungen verwenden möchten, um Aufgaben im Hintergrund zu Trigger or triggern or triggern, müssen Sie Ihre App so konfigurieren, dass sie auch dann Benachrichtigungen erhält, wenn sie sich im Hintergrund befindet. Fügen Sie dazu die Funktion „Background Modes“ über den Bereich **Signing & Capabilities** zum Haupt-App-Target in Xcode hinzu. Aktivieren Sie das Kontrollkästchen **Remote notifications**.

![Xcode zeigt das Kontrollkästchen „Remote notifications“ unter „Capabilities“ an.]({% image_buster /assets/img_archive/background_mode.png %} "background mode enabled")

Auch wenn der Hintergrundmodus für Remote-Benachrichtigungen aktiviert ist, startet das System Ihre App nicht im Hintergrund, wenn Nutzer:innen das Beenden der Anwendung erzwungen haben. Nutzer:innen müssen die Anwendung explizit starten oder das Gerät neu starten, bevor die App vom System automatisch im Hintergrund gestartet werden kann.

Weitere Informationen finden Sie unter [Pushing Background Updates](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) und in der [Dokumentation](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:) zu `application:didReceiveRemoteNotification:fetchCompletionHandler:`.

## Stille Push-Benachrichtigungen senden {#sending-silent-push-notifications}

Um eine stille Push-Benachrichtigung zu senden, setzen Sie das Flag `content-available` in der Nutzlast einer Push-Benachrichtigung auf `1`.

{% alert note %}
Was Apple als Remote-Benachrichtigung bezeichnet, ist eine normale Push-Benachrichtigung, bei der das Flag `content-available` gesetzt ist.
{% endalert %}

Das `content-available`-Flag kann sowohl im Braze-Dashboard als auch in unserem [Apple-Push-Objekt]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) in der [Messaging-API]({{site.baseurl}}/api/endpoints/messaging/) gesetzt werden.

{% alert warning %}
Es wird davon abgeraten, sowohl einen Titel als auch einen Textkörper mit `content-available=1` anzuhängen, da dies zu undefiniertem Verhalten führen kann. Um sicherzustellen, dass eine Benachrichtigung wirklich still ist, schließen Sie sowohl den Titel als auch den Text aus, wenn Sie das `content-available`-Flag auf `1` setzen. Weitere Einzelheiten finden Sie in der offiziellen [Apple-Dokumentation über Hintergrundaktualisierungen](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).
{% endalert %}

![Das Braze-Dashboard zeigt das Kontrollkästchen „content-available“ im Tab „Einstellungen“ des Push-Composers.]({% image_buster /assets/img_archive/remote_notification.png %} "content available")

Wenn Sie eine stille Push-Benachrichtigung senden, möchten Sie vielleicht auch einige Daten in die Nutzlast der Benachrichtigung aufnehmen, damit Ihre Anwendung auf das Ereignis verweisen kann. Dies könnte Ihnen einige Netzwerkanfragen ersparen und die Reaktionsfähigkeit Ihrer App verbessern.

## Interne Push-Benachrichtigungen ignorieren {#ignoring-internal-push-notifications}

Braze verwendet stille Push-Benachrichtigungen, um bestimmte fortgeschrittene Features wie Uninstall-Tracking intern zu verwalten. Wenn Ihre App beim Starten der Anwendung oder bei Push-Nachrichten im Hintergrund automatische Aktionen ausführt, sollten Sie diese Aktivitäten so steuern, dass sie nicht durch interne Push-Benachrichtigungen ausgelöst werden.

Wenn Sie beispielsweise eine Logik haben, die Ihre Server bei jedem Hintergrund-Push oder Anwendungsstart nach neuen Inhalten fragt, möchten Sie vielleicht verhindern, dass die internen Pushs von Braze ausgelöst werden, um unnötigen Netzwerkverkehr zu vermeiden. Da Braze bestimmte Arten von internen Pushs an alle Nutzer:innen ungefähr zur gleichen Zeit sendet, kann es zu einer erheblichen Serverbelastung kommen, wenn die Netzwerkaufrufe beim Start von internen Pushs nicht eingeschränkt werden.

### 1. Schritt: Überprüfen Sie Ihre App auf automatische Aktionen {#step-1-check-your-app-for-automatic-actions}

Überprüfen Sie Ihre Anwendung an den folgenden Stellen auf automatische Aktionen und Update or aktualisieren or aktualisieren Sie Ihren Code, um die internen Pushs von Braze zu ignorieren:

1. **Push-Empfänger.** Push-Benachrichtigungen im Hintergrund rufen `application:didReceiveRemoteNotification:fetchCompletionHandler:` auf dem `UIApplicationDelegate` auf.
2. **Application Delegate.** Pushs im Hintergrund können [angehaltene](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) Apps im Hintergrund starten und dabei die Methoden `application:willFinishLaunchingWithOptions:` und `application:didFinishLaunchingWithOptions:` auf Ihrem `UIApplicationDelegate` Trigger or triggern or triggern. Überprüfen Sie die `launchOptions` dieser Methoden, um festzustellen, ob die Anwendung durch einen Push im Hintergrund gestartet wurde.

### 2. Schritt: Verwenden Sie die interne Push-Utility-Methode {#step-2-use-the-internal-push-utility-method}

Sie können die statische Utility-Methode in `Braze.Notifications` verwenden, um zu überprüfen, ob Ihre App einen internen Push von Braze erhalten hat oder von diesem gestartet wurde. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) liefert `true` für alle internen Push-Benachrichtigungen von Braze, einschließlich Uninstall-Tracking und [Feature-Flags]({{site.baseurl}}/user_guide/messaging/feature_flags/)-Synchronisierungsbenachrichtigungen.

Zum Beispiel:

{% tabs %}
{% tab swift %}


```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!Braze.Notifications.isInternalNotification(userInfo)) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}


```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![BRZNotifications isInternalNotification:userInfo]) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% endtabs %}