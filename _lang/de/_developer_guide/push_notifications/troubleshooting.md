---
page_order: 10.9
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für Push-Benachrichtigungen im Braze SDK
channel:
  - push notifications
---

# Fehlerbehebung für Push-Benachrichtigungen {#troubleshoot-push-notifications}

> Erfahren Sie, wie Sie Probleme mit Push-Benachrichtigungen im Braze SDK beheben können.

{% sdktabs %}
{% sdktab web %}
## Fehlerbehebung {#troubleshooting}

Wenn nach der Einrichtung von Push-Benachrichtigungen Probleme auftreten, beachten Sie Folgendes:

- Web-Push-Benachrichtigungen erfordern, dass Ihre Website HTTPS verwendet.
- Nicht alle Browser können Push-Nachrichten empfangen. Stellen Sie sicher, dass `braze.isPushSupported()` im Browser `true` zurückgibt.
- Einige Browser, wie Firefox, zeigen keine Bilder in Push-Benachrichtigungen an. Details zur Browserunterstützung finden Sie in der [MDN-Dokumentation für Notification-Bilder](https://developer.mozilla.org/en-US/docs/Web/API/Notification/image).
- Wenn Nutzer:innen einer Website den Push-Zugriff verweigert haben, werden sie nicht erneut um Erlaubnis gebeten, es sei denn, sie entfernen den Ablehnungsstatus in ihren Browsereinstellungen.

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
## Den Braze/APNs-Workflow verstehen {#understanding-the-brazeapns-workflow}

Der Apple Push Notification Service (APNs) ist die Infrastruktur zum Senden von Push-Benachrichtigungen an Anwendungen, die auf Apple-Plattformen laufen. Hier ist die vereinfachte Struktur, wie Push-Benachrichtigungen für die Geräte Ihrer Nutzer:innen aktiviert werden und wie Braze Push-Benachrichtigungen an sie senden kann:

1. Sie konfigurieren das Push-Zertifikat und das Provisioning-Profil
2. Geräte registrieren sich bei APNs und stellen Braze Push-Token bereit
3. Sie starten eine Braze-Push-Campaign
4. Braze entfernt ungültige Token

### Schritt 1: Push-Zertifikat und Provisioning-Profil konfigurieren {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Um Ihre App zu entwickeln, erstellen Sie ein SSL-Zertifikat, um Push-Benachrichtigungen zu aktivieren. Dieses Zertifikat ist im Provisioning-Profil enthalten, mit dem Ihre App erstellt wird, und muss auch in das Braze-Dashboard hochgeladen werden. Das Zertifikat ermöglicht es Braze, APNs mitzuteilen, dass es autorisiert ist, Push-Benachrichtigungen in Ihrem Namen zu senden.

Es gibt zwei Arten von [Provisioning-Profilen](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) und Zertifikaten: Entwicklung und Distribution. Wir empfehlen, nur Distribution-Profile und -Zertifikate zu verwenden, um Verwechslungen zu vermeiden. Wenn Sie sich für unterschiedliche Profile und Zertifikate für Entwicklung und Distribution entscheiden, stellen Sie sicher, dass das im Dashboard hochgeladene Zertifikat mit dem Provisioning-Profil übereinstimmt, das Sie aktuell verwenden.

{% alert warning %}
Ändern Sie nicht die Push-Zertifikatsumgebung (Entwicklung versus Produktion). Das Ändern des Push-Zertifikats auf die falsche Umgebung kann dazu führen, dass Nutzer:innen versehentlich ihr Push-Token verlieren, wodurch sie per Push nicht mehr erreichbar sind.
{% endalert %}

### Schritt 2: Geräte registrieren sich bei APNs und stellen Braze Push-Token bereit {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Wenn Nutzer:innen Ihre App öffnen, werden sie aufgefordert, Push-Benachrichtigungen zu akzeptieren. Wenn sie diese Aufforderung akzeptieren, generiert APNs ein Push-Token für dieses bestimmte Gerät. Das Swift SDK sendet das Push-Token sofort und asynchron für Apps, die die standardmäßige [automatische Flush-Richtlinie]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) verwenden. Sobald wir ein Push-Token haben, das mit Nutzer:innen verknüpft ist, werden sie im Dashboard in ihrem Nutzerprofil unter dem Tab **Engagement** als „Push Registered“ angezeigt und sind berechtigt, Push-Benachrichtigungen von Braze-Campaigns zu erhalten.

{% alert note %}
Ab macOS 13 können Sie auf bestimmten Geräten Push-Benachrichtigungen in einem iOS-16-Simulator testen, der auf Xcode 14 läuft. Weitere Details finden Sie in den [Xcode 14 Release Notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Überlegungen zur Push-Token-Generierung {#considerations-for-push-token-generation}

- Wenn Nutzer:innen Ihre App auf einem anderen Gerät installieren, erstellt und erfasst Braze ein weiteres Token auf die gleiche Weise.
- Wenn Nutzer:innen Ihre App neu installieren, generiert das SDK ein neues Token und übergibt es an Braze. APNs und Braze können jedoch das ursprüngliche Token weiterhin als gültig protokollieren.
- Wenn Nutzer:innen Ihre App deinstallieren, erhält Braze nicht sofort eine Benachrichtigung, und das Token erscheint weiterhin als gültig, bis APNs es außer Betrieb nimmt.
- Irgendwann nimmt APNs alte Token außer Betrieb. Braze hat darüber keine Kontrolle und keinen Einblick.

### Schritt 3: Eine Braze-Push-Campaign starten {#step-3-launching-a-braze-push-campaign}

Wenn eine Push-Campaign gestartet wird, sendet Braze Anfragen an APNs, um Ihre Nachricht zuzustellen. Konkret werden die Anfragen für jedes aktuell gültige Push-Token an APNs weitergeleitet, es sei denn, **An das neueste Gerät der Nutzer:innen senden** ist ausgewählt. Nachdem Braze eine erfolgreiche Antwort von APNs erhalten hat, protokolliert Braze eine erfolgreiche Zustellung im Nutzerprofil, obwohl die Nutzer:innen die eigentliche Nachricht möglicherweise aus folgenden Gründen nicht erhalten haben:
- Ihr Gerät ist ausgeschaltet.
- Ihr Gerät ist nicht mit dem Internet verbunden (WLAN oder Mobilfunk).
- Sie haben die App kürzlich deinstalliert.

Braze verwendet das im Dashboard hochgeladene SSL-Push-Zertifikat, um sich zu authentifizieren und zu verifizieren, dass es autorisiert ist, Push-Benachrichtigungen an die bereitgestellten Push-Token zu senden. Wenn ein Gerät online ist, sollte die Benachrichtigung kurz nach dem Senden der Campaign empfangen werden. Beachten Sie, dass Braze das standardmäßige APNs-[Ablaufdatum](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) für Benachrichtigungen auf 30 Tage setzt.

### Schritt 4: Ungültige Token entfernen {#step-4-removing-invalid-tokens}

Wenn [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) uns mitteilt, dass eines der Push-Token, an die wir eine Nachricht zu senden versuchten, ungültig ist, entfernen wir diese Token aus den Nutzerprofilen, mit denen sie verknüpft waren.

{% alert note %}
Es ist normal, dass APNs zunächst einen Erfolgsstatus zurückgibt, auch wenn ein Token nicht mehr registriert ist, da APNs Token-Invalidierungsereignisse nicht sofort meldet. APNs verzögert absichtlich die Rückgabe eines `410`-Status für ungültige Token nach einem zufälligen Zeitplan, der den Datenschutz der Nutzer:innen schützen und das Tracking von App-Deinstallationen verhindern soll. Sie können weiterhin sicher Benachrichtigungen an ein nicht registriertes Token senden, bis APNs einen `410`-Status zurückgibt.
{% endalert %}

## Push-Fehlerprotokolle verwenden {#using-the-push-error-logs}

Das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab) ermöglicht es Ihnen, alle Nachrichten (insbesondere Fehlermeldungen) zu sehen, die mit Ihren Campaigns und Sendungen verbunden sind, einschließlich Push-Benachrichtigungsfehler. Dieses Fehlerprotokoll bietet eine Vielzahl von Warnungen, die sehr hilfreich sein können, um herauszufinden, warum Ihre Campaigns nicht wie erwartet funktionieren. Wenn Sie eine Fehlermeldung auswählen, werden Sie zur relevanten Dokumentation weitergeleitet, die Ihnen bei der Fehlerbehebung eines bestimmten Vorfalls hilft.

![Push-Fehlerprotokolle, die den Zeitpunkt des Fehlers, den App-Namen, den Kanal, den Fehlertyp und die Fehlermeldung anzeigen.]({% image_buster /assets/img_archive/message_activity_log.png %})

Häufige Fehler, die hier auftreten können, umfassen nutzerspezifische Benachrichtigungen, wie z. B. [„Received Unregistered Sending to Push Token“](#swift_received-unregistered-sending).

Darüber hinaus bietet Braze auch ein Push-Changelog im Nutzerprofil unter dem Tab **Engagement**. Dieses Changelog bietet Einblicke in das Push-Registrierungsverhalten, wie z. B. Token-Invalidierung, Push-Registrierungsfehler, Token, die zu neuen Nutzer:innen verschoben werden, usw.

![Braze-Nutzerprofil-Tab „Engagement“ mit dem Push-Registrierungs-Changelog.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Fehler im Nachrichtenaktivitätsprotokoll {#message-activity-log-errors}

#### „Received unregistered sending to push token“ {#received-unregistered-sending}

- Stellen Sie sicher, dass das Push-Token, das über die Methode `AppDelegate.braze?.notifications.register(deviceToken:)` an Braze gesendet wird, gültig ist. Sie können im **Nachrichtenaktivitätsprotokoll** das Push-Token einsehen. Es sollte ungefähr so aussehen: `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, ein langer String mit einer Mischung aus Buchstaben und Zahlen. Wenn Ihr Push-Token anders aussieht, überprüfen Sie Ihren [Code]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-32-register-push-tokens-with-braze) zum Senden der Push-Token an Braze.
- Stellen Sie sicher, dass Ihr Push-Provisioning-Profil mit der Umgebung übereinstimmt, in der Sie testen. Universelle Zertifikate können im Braze-Dashboard so konfiguriert werden, dass sie entweder an die Entwicklungs- oder Produktions-APNs-Umgebung senden. Die Verwendung eines Entwicklungszertifikats für eine Produktions-App oder eines Produktionszertifikats für eine Entwicklungs-App funktioniert nicht.
 - Überprüfen Sie, ob das Push-Token, das Sie bei Braze hochgeladen haben, mit dem Provisioning-Profil übereinstimmt, das zum Erstellen der App verwendet wurde, von der das Push-Token gesendet wurde.

#### DeviceTokenNotForTopic: Device-Token passt nicht zum Topic

APNs gibt `DeviceTokenNotForTopic` (HTTP-Status 400) zurück, wenn das Push-Token nicht zum konfigurierten Topic (Bundle-ID) für Ihre Zugangsdaten passt. Braze kann dies im **Nachrichtenaktivitätsprotokoll** oder in den Push-Zustellungsprotokollen als `DeviceTokenNotForTopic` anzeigen.

Um die Abweichung zu beheben:

1. Bestätigen Sie, dass die **Bundle-ID** der App mit der **App-Bundle-ID** in Braze übereinstimmt (**Einstellungen** > **App-Einstellungen** > **Push-Benachrichtigungseinstellungen**).
2. Überprüfen Sie, ob das Provisioning-Profil, das zum Erstellen der App verwendet wurde, die Push-Fähigkeit für diese Bundle-ID enthält.
3. Bestätigen Sie, dass die bei Braze hochgeladenen Push-Zugangsdaten mit der Umgebung der App übereinstimmen (Entwicklung versus Produktion).
4. Überprüfen Sie bei `.p8`-Schlüsseln, ob **Team-ID** und **Key-ID** in Braze mit Ihrem Apple-Developer-Konto übereinstimmen.
5. Laden Sie einen gültigen `.p8`-Schlüssel oder ein `.p12`-Zertifikat erneut hoch, wenn die Zugangsdaten rotiert oder widerrufen wurden.

Bevorzugen Sie `.p8`-Authentifizierungsschlüssel, wenn möglich. Informationen zu Zugangsdatentypen und Dashboard-Statusindikatoren finden Sie unter [Zu einem .p8-Authentifizierungsschlüssel migrieren]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key).

#### BadDeviceToken beim Senden an Push-Token {#baddevicetoken-sending-to-push-token}

`BadDeviceToken` ist ein APNs-Fehlercode und stammt nicht von Braze. Es kann verschiedene Gründe für diese Antwort geben, darunter:

- Die App hat ein Push-Token erhalten, das für die im Dashboard hochgeladenen Zugangsdaten ungültig war.
- Push war für diesen Workspace deaktiviert.
- Die Nutzer:innen haben sich von Push abgemeldet.
- Die App wurde deinstalliert.
- Apple hat das Push-Token aktualisiert, wodurch das alte Token ungültig wurde.
- Die App wurde für eine Produktionsumgebung erstellt, aber die bei Braze hochgeladenen Push-Zugangsdaten sind für eine Entwicklungsumgebung konfiguriert (oder umgekehrt).

## Probleme bei der Push-Registrierung {#push-registration-issues}

### Keine Push-Registrierungsaufforderung {#no-push-registration-prompt}

Wenn die Anwendung Sie nicht auffordert, sich für Push-Benachrichtigungen zu registrieren, liegt wahrscheinlich ein Problem mit Ihrer Push-Registrierungsintegration vor. Stellen Sie sicher, dass Sie unsere [Dokumentation]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) befolgt und unsere Push-Registrierung korrekt integriert haben. Sie können auch Breakpoints in Ihrem Code setzen, um sicherzustellen, dass der Push-Registrierungscode ausgeführt wird.

### Keine „Push Registered“-Nutzer:innen im Dashboard sichtbar (vor dem Senden von Nachrichten) {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

Stellen Sie sicher, dass Ihre App korrekt konfiguriert ist, um Push-Benachrichtigungen zuzulassen. Häufige Fehlerquellen, die Sie überprüfen sollten:

- Überprüfen Sie, ob Ihre App Sie auffordert, Push-Benachrichtigungen zuzulassen. Normalerweise erscheint diese Aufforderung beim ersten Öffnen der App, sie kann aber auch an anderer Stelle programmiert werden. Wenn sie nicht dort erscheint, wo sie sollte, liegt das Problem wahrscheinlich in der grundlegenden Konfiguration der Push-Fähigkeiten Ihrer App.
  - Überprüfen Sie, ob die Schritte für die [Push-Integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) erfolgreich abgeschlossen wurden.
  - Überprüfen Sie, ob das Provisioning-Profil, mit dem Ihre App erstellt wurde, Berechtigungen für Push enthält. Stellen Sie sicher, dass Sie alle verfügbaren Provisioning-Profile von Ihrem Apple-Developer-Konto abrufen. Um dies zu bestätigen, führen Sie die folgenden Schritte aus:
    1. Navigieren Sie in Xcode zu **Preferences > Accounts** (oder verwenden Sie die Tastenkombination <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Wählen Sie die Apple-ID aus, die Sie für Ihr Developer-Konto verwenden, und klicken Sie auf **View Details**.
    3. Klicken Sie auf der nächsten Seite auf **<i class="fas fa-redo-alt"></i> Refresh** und bestätigen Sie, dass Sie alle verfügbaren Provisioning-Profile abrufen.
- Überprüfen Sie, ob Sie die [Push-Fähigkeit korrekt aktiviert]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-2-enable-push-capabilities) haben.
- Überprüfen Sie, ob Ihr Push-Provisioning-Profil mit der Umgebung übereinstimmt, in der Sie testen. Universelle Zertifikate können im Braze-Dashboard so konfiguriert werden, dass sie entweder an die Entwicklungs- oder Produktions-APNs-Umgebung senden. Die Verwendung eines Entwicklungszertifikats für eine Produktions-App oder eines Produktionszertifikats für eine Entwicklungs-App funktioniert nicht.
- Überprüfen Sie, ob Sie unsere `registerPushToken`-Methode aufrufen, indem Sie einen Breakpoint in Ihrem Code setzen.
- Stellen Sie sicher, dass Sie mit einem Gerät testen (Push funktioniert nicht auf einem Simulator) und eine gute Netzwerkverbindung haben.

## Push-Benachrichtigungen gesendet, aber nicht auf Geräten der Nutzer:innen angezeigt {#push-notifications-sent-but-not-displayed-on-users-devices}

### „Push Registered“-Nutzer:innen nach dem Senden von Nachrichten nicht mehr aktiviert {#push-registered-users-no-longer-enabled-after-sending-messages}

Dies deutet wahrscheinlich darauf hin, dass die Nutzer:innen ein ungültiges Push-Token hatten. Dies kann aus mehreren Gründen passieren:

#### Abweichung zwischen Dashboard- und App-Zertifikat {#dashboard-and-app-certificate-mismatch}

Wenn das Push-Zertifikat, das Sie im Dashboard hochgeladen haben, nicht dasselbe ist wie im Provisioning-Profil, mit dem Ihre App erstellt wurde, lehnt APNs das Token ab. Überprüfen Sie, ob Sie das richtige Zertifikat hochgeladen haben, und schließen Sie eine weitere Sitzung in der App ab, bevor Sie eine weitere Testbenachrichtigung versuchen.

#### Anwendung wurde deinstalliert {#application-was-uninstalled}

Wenn Nutzer:innen Ihre Anwendung deinstalliert haben, wird ihr Push-Token ungültig und beim nächsten Senden entfernt.

#### Provisioning-Profil neu generieren {#regenerating-your-provisioning-profile}

Als letzten Ausweg können Sie von vorne beginnen und ein komplett neues Provisioning-Profil erstellen, um Konfigurationsfehler zu beheben, die durch die Arbeit mit mehreren Umgebungen, Profilen und Apps gleichzeitig entstehen. Es gibt viele „bewegliche Teile“ bei der Einrichtung von Push-Benachrichtigungen, daher ist es manchmal am besten, von vorne zu beginnen. Dies hilft auch, das Problem einzugrenzen, wenn Sie die Fehlerbehebung fortsetzen müssen.

### Nachrichten werden nicht an „Push Registered“-Nutzer:innen zugestellt {#messages-not-delivered-to-push-registered-users}

#### App ist im Vordergrund {#app-is-foregrounded}

Auf iOS-Versionen, die Push nicht über das `UserNotifications`-Framework integrieren, wird die Push-Nachricht nicht angezeigt, wenn die App im Vordergrund ist, wenn sie empfangen wird. Sie sollten die App auf Ihren Testgeräten in den Hintergrund versetzen, bevor Sie Testnachrichten senden.

#### Testbenachrichtigung falsch geplant {#test-notification-scheduled-incorrectly}

Überprüfen Sie den Zeitplan, den Sie für Ihre Testnachricht festgelegt haben. Wenn er auf Zustellung nach Ortszeit oder [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing) eingestellt ist, haben Sie die Nachricht möglicherweise einfach noch nicht erhalten (oder die App war im Vordergrund, als sie empfangen wurde).

### Nutzer:in nicht „Push Registered“ für die getestete App {#user-not-push-registered-for-the-app-being-tested}

Überprüfen Sie das Nutzerprofil der Nutzer:innen, an die Sie eine Testnachricht senden möchten. Unter dem Tab **Engagement** sollte eine Liste der „pushfähigen Apps“ vorhanden sein. Überprüfen Sie, ob die App, an die Sie Testnachrichten senden möchten, in dieser Liste enthalten ist. Nutzer:innen werden als „Push Registered“ angezeigt, wenn sie ein Push-Token für eine beliebige App in Ihrem Workspace haben, sodass dies ein falsch positives Ergebnis sein könnte.

Folgendes würde auf ein Problem mit der Push-Registrierung hinweisen oder darauf, dass das Token der Nutzer:innen nach dem Senden von APNs als ungültig an Braze zurückgegeben wurde:

![Ein Nutzerprofil, das die Kontakteinstellungen anzeigt. Unter Push wird „No Apps“ angezeigt.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Push-Klicks werden nicht protokolliert {#push-clicks-not-logged}

- Stellen Sie sicher, dass Sie die [Schritte zur Push-Integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling) befolgt haben.
- Braze verarbeitet keine Push-Benachrichtigungen, die im Vordergrund stillschweigend empfangen werden (standardmäßiges Vordergrund-Push-Verhalten vor dem `UserNotifications`-Framework). Das bedeutet, dass Links nicht geöffnet und Push-Klicks nicht protokolliert werden. Wenn Ihre Anwendung das `UserNotifications`-Framework noch nicht integriert hat, verarbeitet Braze keine Push-Benachrichtigungen, wenn der Anwendungsstatus `UIApplicationStateActive` ist. Stellen Sie sicher, dass Ihre App Aufrufe an [Push-Verarbeitungsmethoden]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling) nicht verzögert; andernfalls behandelt das Swift SDK Push-Benachrichtigungen möglicherweise als stille Vordergrund-Push-Ereignisse und verarbeitet sie nicht.

## Deeplinks funktionieren nicht {#deep-links-not-working}

Eine umfassende Fehlerbehebung über alle Kanäle hinweg – einschließlich Universal Links, angepasster Schemata, E-Mail und Drittanbieter wie Branch – finden Sie unter [Fehlerbehebung für Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

### Weblinks aus Push-Klicks werden nicht geöffnet {#web-links-from-push-clicks-not-opening}

Links in Push-Benachrichtigungen müssen ATS-konform sein, um in Webviews geöffnet zu werden. Stellen Sie sicher, dass Ihre Weblinks HTTPS verwenden. Weitere Informationen finden Sie unter [ATS-Konformität]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#app-transport-security-ats).

### Deeplinks aus Push-Klicks werden nicht geöffnet {#deep-links-from-push-clicks-not-opening}

Der Großteil des Codes, der Deeplinks verarbeitet, verarbeitet auch Push-Öffnungen. Stellen Sie zunächst sicher, dass Push-Öffnungen protokolliert werden. Wenn nicht, beheben Sie dieses Problem (da die Lösung oft auch die Link-Verarbeitung behebt).

Wenn Öffnungen protokolliert werden, prüfen Sie, ob es sich um ein Problem mit dem Deeplink im Allgemeinen oder mit der Deeplink-Verarbeitung bei Push-Klicks handelt. Testen Sie dazu, ob ein Deeplink aus einem In-App-Nachrichten-Klick funktioniert.

{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
## Fehlerbehebung

### Push erscheint nicht, nachdem die App über den Task-Switcher geschlossen wurde {#push-doesnt-appear-after-app-is-closed-from-task-switcher}

Wenn Sie feststellen, dass Push-Benachrichtigungen nicht mehr erscheinen, nachdem die App über den Task-Switcher geschlossen wurde, befindet sich Ihre App wahrscheinlich im Debug-Modus. .NET MAUI fügt im Debug-Modus Scaffolding hinzu, das verhindert, dass Apps Push empfangen, nachdem ihr Prozess beendet wurde. Wenn Sie Ihre App im Release-Modus ausführen, sollten Sie Push auch nach dem Schließen der App über den Task-Switcher sehen.

### Angepasste Notification-Factory wird nicht korrekt gesetzt {#custom-notification-factory-not-being-set-correctly}

Angepasste Notification-Factories (und alle Delegates) müssen [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) erweitern, um über die C#- und Java-Grenze hinweg korrekt zu funktionieren. Weitere Informationen finden Sie bei [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces) zur Implementierung von Java-Schnittstellen.

{% endsdktab %}
{% endsdktabs %}

## Zeilenumbrüche in Push-Benachrichtigungen {#push-linebreaks}

Beim Verfassen von Push-Benachrichtigungen mit Liquid-Tags werden Zeilenumbrüche neben Liquid-Tags automatisch entfernt, bevor die Nachricht gesendet wird. Im [Push-Benachrichtigungs-Composer]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message) werden diese Zeilenumbrüche wieder eingefügt, damit Ihre Nachricht beim Bearbeiten lesbar bleibt. Wenn Sie beim Speichern Ihrer Nachricht Zeilenumbrüche um Liquid-Tags herum bemerken, ist dies das erwartete Verhalten.