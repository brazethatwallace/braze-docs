---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für Push-Benachrichtigungen unter iOS
platform: iOS
page_order: 30
description: "Dieser Referenzartikel behandelt mögliche Themen zur Fehlerbehebung für Ihre iOS-Push-Implementierung."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Fehlerbehebung {#push-troubleshooting}

## Den Braze/APNs-Workflow verstehen {#understanding-the-brazeapns-workflow}

Der Apple Push Notification Service (APNs) ist Apples Infrastruktur für den Versand von Push-Benachrichtigungen an iOS- und OS-X-Anwendungen. Hier ist die vereinfachte Struktur, wie Push-Benachrichtigungen für die Geräte Ihrer Nutzer:innen aktiviert werden und wie Braze Push-Benachrichtigungen an diese senden kann:

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### Schritt 1: Push-Zertifikat und Bereitstellungsprofil konfigurieren {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Wenn Sie Ihre App entwickeln, erstellen Sie ein SSL-Zertifikat, um Push-Benachrichtigungen zu aktivieren. Dieses Zertifikat ist im Bereitstellungsprofil enthalten, mit dem Ihre App erstellt wird, und muss außerdem in das Braze-Dashboard hochgeladen werden. Das Zertifikat ermöglicht es Braze, APNs mitzuteilen, dass wir berechtigt sind, Push-Benachrichtigungen in Ihrem Namen zu senden.

Es gibt zwei Arten von [Bereitstellungsprofilen](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) und Zertifikaten: Entwicklung und Distribution. Wir empfehlen, ausschließlich Distributionsprofile und -zertifikate zu verwenden, um Verwechslungen zu vermeiden. Wenn Sie sich für unterschiedliche Profile und Zertifikate für Entwicklung und Distribution entscheiden, stellen Sie sicher, dass das im Dashboard hochgeladene Zertifikat mit dem aktuell verwendeten Bereitstellungsprofil übereinstimmt.

{% alert warning %}
Ändern Sie nicht die Umgebung des Push-Zertifikats (Entwicklung versus Produktion). Ein Wechsel des Push-Zertifikats auf die falsche Umgebung kann dazu führen, dass die Push-Token Ihrer Nutzer:innen versehentlich entfernt werden, wodurch diese per Push nicht mehr erreichbar sind.
{% endalert %}

#### Schritt 2: Geräte registrieren sich bei APNs und stellen Braze Push-Token bereit {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Wenn Nutzer:innen Ihre App öffnen, werden sie aufgefordert, Push-Benachrichtigungen zu akzeptieren. Wenn sie diese Aufforderung annehmen, generiert APNs ein Push-Token für das jeweilige Gerät. Das iOS SDK sendet das Push-Token sofort und asynchron für Apps, die die standardmäßige [automatische Flush-Richtlinie]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) verwenden. Sobald wir ein Push-Token mit einer/einem Nutzer:in verknüpft haben, wird diese Person im Dashboard in ihrem Nutzerprofil unter dem Tab **Engagement** als „Push Registered“ angezeigt und ist berechtigt, Push-Benachrichtigungen aus Braze Campaigns zu erhalten.

{% alert note %}
Ab Xcode 14 können Sie Remote-Push-Benachrichtigungen in einem iOS-Simulator testen.
{% endalert %}

#### Schritt 3: Eine Braze-Push-Campaign starten {#step-3-launching-a-braze-push-campaign}

Wenn eine Push-Campaign gestartet wird, sendet Braze Anfragen an APNs, um Ihre Nachricht zuzustellen. Braze verwendet das im Dashboard hochgeladene SSL-Push-Zertifikat zur Authentifizierung und Überprüfung, dass wir berechtigt sind, Push-Benachrichtigungen an die bereitgestellten Push-Token zu senden. Wenn ein Gerät online ist, sollte die Benachrichtigung kurz nach dem Versand der Campaign empfangen werden. Beachten Sie, dass Braze das standardmäßige APNs-[Ablaufdatum](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) für Benachrichtigungen auf 30 Tage setzt.

#### Schritt 4: Ungültige Token entfernen {#step-4-removing-invalid-tokens}

Wenn [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) uns mitteilt, dass Push-Token, an die wir eine Nachricht zu senden versucht haben, ungültig sind, entfernen wir diese Token aus den Nutzerprofilen, mit denen sie verknüpft waren.

## Push-Fehlerprotokolle nutzen {#utilizing-the-push-error-logs}

Braze stellt ein Protokoll der Push-Benachrichtigungsfehler im **Nachrichtenaktivitätsprotokoll** bereit. Dieses Fehlerprotokoll enthält eine Vielzahl von Warnungen, die sehr hilfreich sein können, um herauszufinden, warum Ihre Campaigns nicht wie erwartet funktionieren. Wenn Sie eine Fehlermeldung auswählen, werden Sie zur entsprechenden Dokumentation weitergeleitet, die Ihnen bei der Fehlerbehebung eines bestimmten Vorfalls hilft.

![Push-Fehlerprotokolle mit Zeitpunkt des Fehlers, App-Name, Kanal, Fehlertyp und Fehlermeldung.]({% image_buster /assets/img_archive/message_activity_log.png %})

Häufige Fehler, die hier auftreten können, umfassen nutzerspezifische Benachrichtigungen wie [„Received Unregistered Sending to Push Token“](#received-unregistered-sending).

Darüber hinaus stellt Braze auch ein Push-Changelog im Nutzerprofil unter dem Tab **Engagement** bereit. Dieses Changelog bietet Einblicke in das Push-Registrierungsverhalten, wie z. B. Token-Invalidierung, Push-Registrierungsfehler, Token, die neuen Nutzer:innen zugewiesen werden, usw.

![Beispiel für eine animierte Content-Card.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

## Probleme bei der Push-Registrierung {#push-registration-issues}

Um die Push-Registrierungslogik Ihrer Anwendung zu überprüfen, implementieren Sie [Push-Unit-Tests]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Keine Aufforderung zur Push-Registrierung {#no-push-registration-prompt}

Wenn die Anwendung Sie nicht zur Registrierung für Push-Benachrichtigungen auffordert, liegt wahrscheinlich ein Problem mit Ihrer Push-Registrierungsintegration vor. Stellen Sie sicher, dass Sie unsere [Dokumentation]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) befolgt und unsere Push-Registrierung korrekt integriert haben. Sie können auch Breakpoints in Ihrem Code setzen, um sicherzustellen, dass der Push-Registrierungscode ausgeführt wird.

#### Keine „push-registrierten“ Nutzer:innen im Dashboard sichtbar {#no-push-registered-users-showing-in-the-dashboard}

- Überprüfen Sie, ob Ihre App Sie auffordert, Push-Benachrichtigungen zuzulassen. In der Regel erscheint diese Aufforderung beim ersten Öffnen der App, sie kann aber auch an anderer Stelle programmiert werden. Wenn sie nicht dort erscheint, wo sie sollte, liegt das Problem wahrscheinlich in der grundlegenden Konfiguration der Push-Funktionen Ihrer App.
  - Überprüfen Sie, ob die Schritte für die [Push-Integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) erfolgreich abgeschlossen wurden.
  - Überprüfen Sie, ob das Bereitstellungsprofil, mit dem Ihre App erstellt wurde, Berechtigungen für Push enthält. Stellen Sie sicher, dass Sie alle verfügbaren Bereitstellungsprofile von Ihrem Apple-Entwicklerkonto abrufen. Um dies zu bestätigen, führen Sie die folgenden Schritte aus:
    1. Navigieren Sie in Xcode zu **Preferences > Accounts** (oder verwenden Sie die Tastenkombination <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Wählen Sie die Apple-ID aus, die Sie für Ihr Entwicklerkonto verwenden, und klicken Sie auf **View Details**.
    3. Klicken Sie auf der nächsten Seite auf **<i class="fas fa-redo-alt"></i> Refresh** und bestätigen Sie, dass Sie alle verfügbaren Bereitstellungsprofile abrufen.
- Überprüfen Sie, ob Sie die [Push-Funktion korrekt aktiviert]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-2-enable-push-capabilities) haben in Ihrer App.
- Überprüfen Sie, ob Ihr Push-Bereitstellungsprofil mit der Umgebung übereinstimmt, in der Sie testen. Universelle Zertifikate können im Braze-Dashboard so konfiguriert werden, dass sie entweder an die Entwicklungs- oder die Produktions-APNs-Umgebung senden. Die Verwendung eines Entwicklungszertifikats für eine Produktions-App oder eines Produktionszertifikats für eine Entwicklungs-App funktioniert nicht.
- Überprüfen Sie, ob Sie unsere `registerPushToken`-Methode aufrufen, indem Sie einen Breakpoint in Ihrem Code setzen.
- Überprüfen Sie, ob Sie ein Gerät verwenden (Push funktioniert nicht auf einem Simulator) und eine gute Netzwerkverbindung haben.

## Geräte empfangen keine Push-Benachrichtigungen {#devices-not-receiving-push-notifications}

### Nutzer:innen sind nach dem Senden einer Push-Benachrichtigung nicht mehr „push-registriert“ {#users-no-longer-push-registered-after-sending-a-push-notification}

Dies deutet wahrscheinlich darauf hin, dass die Nutzer:innen ein ungültiges Push-Token hatten. Dies kann verschiedene Ursachen haben:

#### Zertifikat im Dashboard und in der App stimmen nicht überein {#dashboard-and-app-certificate-mismatch}

Wenn das Push-Zertifikat, das Sie im Dashboard hochgeladen haben, nicht mit dem im Bereitstellungsprofil übereinstimmt, mit dem Ihre App erstellt wurde, lehnt APNs das Token ab. Überprüfen Sie, ob Sie das richtige Zertifikat hochgeladen und eine weitere Sitzung in der App abgeschlossen haben, bevor Sie eine weitere Testbenachrichtigung versuchen.

##### Deinstallationen {#uninstalls}

Wenn Nutzer:innen Ihre Anwendung deinstalliert haben, wird ihr Push-Token ungültig und beim nächsten Senden entfernt.

##### Bereitstellungsprofil neu generieren {#regenerating-your-provisioning-profile}

Als letzten Ausweg können Sie von vorne beginnen und ein komplett neues Bereitstellungsprofil erstellen, um Konfigurationsfehler zu beheben, die durch die gleichzeitige Arbeit mit mehreren Umgebungen, Profilen und Apps entstehen. Es gibt viele „bewegliche Teile“ beim Einrichten von Push-Benachrichtigungen für iOS-Apps, daher ist es manchmal am besten, von Anfang an neu zu beginnen. Dies hilft auch dabei, das Problem einzugrenzen, falls Sie die Fehlerbehebung fortsetzen müssen.

#### Nutzer:innen sind nach dem Senden einer Push-Benachrichtigung weiterhin „push-registriert“ {#users-still-push-registered-after-sending-a-push-notification}

##### App ist im Vordergrund {#app-is-foregrounded}

Bei iOS-Versionen, die Push nicht über das `UserNotifications`-Framework integrieren, wird die Push-Nachricht nicht angezeigt, wenn die App beim Empfang im Vordergrund ist. Sie sollten die App auf Ihren Testgeräten in den Hintergrund verschieben, bevor Sie Testnachrichten senden.

##### Testbenachrichtigung falsch geplant {#test-notification-scheduled-incorrectly}

Überprüfen Sie den Zeitplan, den Sie für Ihre Testnachricht festgelegt haben. Wenn die Zustellung auf Ortszeit oder [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) eingestellt ist, haben Sie die Nachricht möglicherweise noch nicht erhalten (oder die App war beim Empfang im Vordergrund).

#### Nutzer:in ist nicht „push-registriert“ für die getestete App {#user-not-push-registered-for-the-app-being-tested}

Überprüfen Sie das Nutzerprofil der Person, an die Sie eine Testnachricht senden möchten. Unter dem Tab **Engagement** sollte eine Liste der „pushfähigen Apps“ angezeigt werden. Überprüfen Sie, ob die App, an die Sie Testnachrichten senden möchten, in dieser Liste enthalten ist. Nutzer:innen werden als „Push Registered“ angezeigt, wenn sie ein Push-Token für eine beliebige App in Ihrem Workspace haben, sodass dies ein falsch positives Ergebnis sein könnte.

Folgendes würde auf ein Problem mit der Push-Registrierung hinweisen oder darauf, dass das Token der Nutzer:innen nach dem Senden von APNs als ungültig an Braze zurückgegeben wurde:

![Ein Nutzerprofil mit den Kontakteinstellungen. Hier können Sie sehen, für welche Apps Push registriert ist.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Push-Nachrichten werden nicht gesendet {#push-messages-not-sending}

Informationen zur Fehlerbehebung bei Push-Benachrichtigungen, die nicht gesendet werden, finden Sie unter [Fehlerbehebung für Push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

## Fehler im Nachrichtenaktivitätsprotokoll {#message-activity-log-errors}

### Nicht registriertes Senden an Push-Token empfangen {#received-unregistered-sending}

- Stellen Sie sicher, dass das Push-Token, das über die Methode `[[Appboy sharedInstance] registerPushToken:]` an Braze gesendet wird, gültig ist. Sie können im **Nachrichtenaktivitätsprotokoll** das Push-Token einsehen. Es sollte in etwa so aussehen: `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, ein langer String mit einer Mischung aus Buchstaben und Zahlen. Wenn Ihr Push-Token anders aussieht, überprüfen Sie Ihren [Code]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-4-register-push-tokens-with-braze) zum Senden der Push-Token an Braze.
- Stellen Sie sicher, dass Ihr Push-Bereitstellungsprofil mit der Umgebung übereinstimmt, in der Sie testen. Universelle Zertifikate können im Braze-Dashboard so konfiguriert werden, dass sie entweder an die Entwicklungs- oder die Produktions-APNs-Umgebung senden. Die Verwendung eines Entwicklungszertifikats für eine Produktions-App oder eines Produktionszertifikats für eine Entwicklungs-App funktioniert nicht.
 - Überprüfen Sie, ob das Push-Token, das Sie bei Braze hochgeladen haben, mit dem Bereitstellungsprofil übereinstimmt, das Sie zum Erstellen der App verwendet haben, von der das Push-Token gesendet wurde.

#### Geräte-Token nicht für das Thema {#device-token-not-for-topic}

Dieser Fehler weist darauf hin, dass das Push-Zertifikat Ihrer App und die Bundle-ID nicht übereinstimmen. Überprüfen Sie, ob das Push-Zertifikat, das Sie bei Braze hochgeladen haben, mit dem Bereitstellungsprofil übereinstimmt, das zum Erstellen der App verwendet wurde, von der das Push-Token gesendet wurde.

#### BadDeviceToken beim Senden an Push-Token {#baddevicetoken-sending-to-push-token}

`BadDeviceToken` ist ein APNs-Fehlercode und stammt nicht von Braze. Es kann verschiedene Gründe geben, warum diese Antwort zurückgegeben wird, unter anderem die folgenden:

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## Probleme nach der Push-Zustellung {#issues-after-push-delivery}

Um die Push-Verarbeitung Ihrer Anwendung zu überprüfen, implementieren Sie [Push-Unit-Tests]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Push-Klicks werden nicht protokolliert {#push-clicks-not-logged}

- Wenn dieses Problem nur unter iOS 10 auftritt, stellen Sie sicher, dass Sie die Schritte zur Push-Integration für [iOS 10]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling) befolgt haben.
- Braze verarbeitet keine Push-Benachrichtigungen, die im Vordergrund stillschweigend empfangen werden (z. B. das standardmäßige Vordergrund-Push-Verhalten vor dem `UserNotifications`-Framework). Das bedeutet, dass Links nicht geöffnet und Push-Klicks nicht protokolliert werden. Wenn Ihre Anwendung das `UserNotifications`-Framework noch nicht integriert hat, verarbeitet Braze keine Push-Benachrichtigungen, wenn der Anwendungsstatus `UIApplicationStateActive` ist. Stellen Sie sicher, dass Ihre App Aufrufe unserer [Push-Verarbeitungsmethoden]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling) nicht verzögert, da das iOS SDK Push-Benachrichtigungen andernfalls möglicherweise als stille Vordergrund-Push-Ereignisse behandelt und nicht weiterverarbeitet.

#### Web-Links aus Push-Klicks werden nicht geöffnet {#web-links-from-push-clicks-not-opening}

iOS 9+ erfordert, dass Links ATS-konform sind, um in Webansichten geöffnet zu werden. Stellen Sie sicher, dass Ihre Web-Links HTTPS verwenden. Weitere Informationen finden Sie in unserem Artikel zur [ATS-Konformität]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking#app-transport-security-ats).

#### Deeplinks aus Push-Klicks werden nicht geöffnet {#deep-links-from-push-clicks-not-opening}

Der Großteil des Codes, der Deeplinks verarbeitet, verarbeitet auch Push-Öffnungen. Stellen Sie zunächst sicher, dass Push-Öffnungen protokolliert werden. Falls nicht, [beheben Sie dieses Problem](#push-clicks-not-logged) (da die Lösung häufig auch die Link-Verarbeitung behebt).

Wenn Öffnungen protokolliert werden, prüfen Sie, ob es sich um ein allgemeines Problem mit dem Deeplink oder um ein Problem mit der Deeplink-Verarbeitung bei Push-Klicks handelt. Testen Sie dazu, ob ein Deeplink aus einem In-App-Nachrichten-Klick funktioniert.

#### Wenige oder keine direkten Öffnungen {#few-or-no-direct-opens}

Wenn mindestens ein:e Nutzer:in Ihre iOS-Push-Benachrichtigung öffnet, aber wenige oder keine *Direkten Öffnungen* in Braze protokolliert werden, liegt möglicherweise ein Problem mit Ihrer [SDK-Integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) vor. Beachten Sie, dass *Direkte Öffnungen* nicht für Testsendungen oder stille Push-Benachrichtigungen protokolliert werden.

- Stellen Sie sicher, dass die Nachrichten nicht als [stille Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications#sending-silent-push-notifications) gesendet werden. Die Nachricht muss Text im Titel oder im Textkörper enthalten, um nicht als still eingestuft zu werden.
- Überprüfen Sie die folgenden Schritte aus dem [Leitfaden zur Push-Integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration):
   - [Für Push registrieren]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-register-for-push-notifications-with-apns): Bei jedem einzelnen App-Start, vorzugsweise innerhalb von `application:didFinishLaunchingWithOptions:`, muss der Code aus Schritt 3 ausgeführt werden. Die Delegate-Eigenschaft von `UNUserNotificationCenter.current()` muss einem Objekt zugewiesen werden, das `UNUserNotificationCenterDelegate` implementiert und die Methode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` enthält.
   - [Push-Verarbeitung aktivieren]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling): Überprüfen Sie, dass die Methode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` implementiert wurde.