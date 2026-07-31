---
page_order: 10.9
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für Push-Benachrichtigungen im Braze SDK
description: "Diagnostizieren Sie Probleme bei der Zustellung und Anzeige von Push-Benachrichtigungen mithilfe eines Symptomindex, eines standardisierten Untersuchungspfads und plattformspezifischer SDK-Prüfungen."
channel:
  - push notifications
---

# Fehlerbehebung für Push-Benachrichtigungen {#troubleshoot-push-notifications}

> Verwenden Sie diese Seite, um Probleme bei der Zustellung und Anzeige von Push-Benachrichtigungen auf einem Gerät zu diagnostizieren. Informationen zu Dashboard-seitigen Zustellungsprüfungen (Abo-Status, Segmente, Obergrenzen) finden Sie unter [Fehlerbehebung für Push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

Bevor Sie mit dem Debugging beginnen, fügen Sie sich als [Testnutzer:in]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) hinzu und lesen Sie [Testnachrichten senden]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages).

## Hier starten: Symptom zuordnen {#start-here-match-your-symptom}

Finden Sie das Verhalten, das Sie beobachten, in der Tabelle und folgen Sie dann den Schritten des jeweiligen Abschnitts. Wenn Sie sich nicht sicher sind, welcher Abschnitt zutrifft, verwenden Sie den [standardisierten Untersuchungspfad](#standard-investigation-path).

| Symptom | Gehe zu |
| --- | --- |
| Push wird auf einer Plattform nicht empfangen | Wählen Sie Ihren SDK-Tab unter [Plattformspezifische Fehlerbehebung](#platform-specific-troubleshooting) |
| Zeilenumbrüche um Liquid-Tags sehen beim Speichern falsch aus | [Zeilenumbrüche in Push-Benachrichtigungen](#push-linebreaks) |
| Dashboard-Zustellungsprüfungen (Abo, Segment, Obergrenzen) | [Fehlerbehebung für Push]({{site.baseurl}}/user_guide/channels/push/troubleshooting) |
| Deeplink aus Push öffnet sich nicht korrekt | [Fehlerbehebung für Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting) |
| Häufige Push-Fehlercodes | [Häufige Push-Fehlermeldungen]({{site.baseurl}}/user_guide/channels/push/push_error_codes) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push-SDK-Symptom" }

## Standardisierter Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow für jeden Push-Benachrichtigungsvorfall. Beginnen Sie bei Schritt 1.

1. Bestätigen Sie, dass das Gerät ein gültiges Push-Token hat und die Push-Berechtigung in den Geräteeinstellungen erteilt wurde.
2. Bestätigen Sie im Dashboard, dass die/der Testnutzer:in dem Campaign- oder Canvas-[Segment]({{site.baseurl}}/user_guide/channels/push/troubleshooting#segment) entspricht und sich nicht in der [Kontrollgruppe]({{site.baseurl}}/user_guide/channels/push/troubleshooting#control-group-status) befindet.
3. Senden Sie einen [Test-Push]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages) an das Testgerät.
4. [Aktivieren Sie die ausführliche Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduzieren Sie das Problem und lesen Sie die plattformspezifischen Hinweise in Ihrem [SDK-Tab](#platform-specific-troubleshooting).
5. Wenn das Problem weiterhin besteht, kontaktieren Sie den [Braze-Support]({{site.baseurl}}/braze_support) mit ausführlichen Protokollen, Plattform, SDK-Version und Campaign- oder Canvas-ID.

## Plattformspezifische Fehlerbehebung {#platform-specific-troubleshooting}

Wählen Sie Ihren SDK-Tab für plattformspezifische Einrichtungs- und Anzeigeprüfungen.

{% sdktabs %}
{% sdktab web %}
## Fehlerbehebung {#troubleshooting}

Wenn nach der Einrichtung von Push-Benachrichtigungen Probleme auftreten, beachten Sie Folgendes:

- Web-Push-Benachrichtigungen erfordern, dass Ihre Website HTTPS verwendet.
- Nicht alle Browser können Push-Nachrichten empfangen. Stellen Sie sicher, dass `braze.isPushSupported()` im Browser `true` zurückgibt.
- Einige Browser, wie z. B. Firefox, zeigen keine Bilder in Push-Benachrichtigungen an. Einzelheiten zur Browserunterstützung finden Sie in der [MDN-Dokumentation für Notification-Bilder](https://developer.mozilla.org/en-US/docs/Web/API/Notification/image).
- Wenn Nutzer:innen einer Website den Push-Zugriff verweigert haben, werden sie nicht erneut um Erlaubnis gebeten, es sei denn, sie entfernen den Ablehnungsstatus in ihren Browsereinstellungen.

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
## Den Braze/APNs-Workflow verstehen {#understanding-the-brazeapns-workflow}

Der Apple Push Notification Service (APNs) ist die Infrastruktur zum Senden von Push-Benachrichtigungen an Anwendungen, die auf Apple-Plattformen laufen. Hier ist die vereinfachte Struktur, wie Push-Benachrichtigungen für die Geräte Ihrer Nutzer:innen aktiviert werden und wie Braze Push-Benachrichtigungen an sie senden kann:

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### Schritt 1: Push-Zertifikat und Bereitstellungsprofil konfigurieren {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Um Ihre App zu entwickeln, erstellen Sie ein SSL-Zertifikat, um Push-Benachrichtigungen zu aktivieren. Dieses Zertifikat ist im Bereitstellungsprofil enthalten, mit dem Ihre App erstellt wird, und muss auch in das Braze-Dashboard hochgeladen werden. Das Zertifikat ermöglicht es Braze, APNs mitzuteilen, dass es autorisiert ist, Push-Benachrichtigungen in Ihrem Namen zu senden.

Es gibt zwei Arten von [Bereitstellungsprofilen](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) und Zertifikaten: Entwicklung und Distribution. Wir empfehlen, nur Distributionsprofile und -zertifikate zu verwenden, um Verwechslungen zu vermeiden. Wenn Sie sich für unterschiedliche Profile und Zertifikate für Entwicklung und Distribution entscheiden, stellen Sie sicher, dass das in das Dashboard hochgeladene Zertifikat mit dem Bereitstellungsprofil übereinstimmt, das Sie derzeit verwenden.

{% alert warning %}
Ändern Sie nicht die Umgebung des Push-Zertifikats (Entwicklung versus Produktion). Ein Wechsel des Push-Zertifikats zur falschen Umgebung kann dazu führen, dass das Push-Token Ihrer Nutzer:innen versehentlich entfernt wird, sodass sie per Push nicht mehr erreichbar sind.
{% endalert %}

### Schritt 2: Geräte registrieren sich bei APNs und stellen Braze Push-Token bereit {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Wenn Nutzer:innen Ihre App öffnen, werden sie aufgefordert, Push-Benachrichtigungen zu akzeptieren. Wenn sie diese Aufforderung akzeptieren, generiert APNs ein Push-Token für dieses bestimmte Gerät. Das Swift SDK sendet das Push-Token sofort und asynchron für Apps, die die standardmäßige [automatische Flush-Richtlinie]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) verwenden. Sobald wir ein Push-Token haben, das mit einer/einem Nutzer:in verknüpft ist, wird diese Person im Dashboard in ihrem Nutzerprofil unter dem Tab **Engagement** als „Push Registered“ angezeigt und ist berechtigt, Push-Benachrichtigungen von Braze Campaigns zu erhalten.

{% alert note %}
Ab macOS 13 können Sie auf bestimmten Geräten Push-Benachrichtigungen in einem iOS-16-Simulator testen, der auf Xcode 14 läuft. Weitere Details finden Sie in den [Xcode 14 Release Notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Überlegungen zur Push-Token-Generierung {#considerations-for-push-token-generation}

- Wenn Nutzer:innen Ihre App auf einem anderen Gerät installieren, erstellt und erfasst Braze auf die gleiche Weise ein weiteres Token.
- Wenn Nutzer:innen Ihre App neu installieren, generiert das SDK ein neues Token und übergibt es an Braze. APNs und Braze können jedoch das ursprüngliche Token weiterhin als gültig protokollieren.
- Wenn Nutzer:innen Ihre App deinstallieren, erhält Braze nicht sofort eine Benachrichtigung, und das Token erscheint weiterhin als gültig, bis APNs es außer Betrieb nimmt.
- Irgendwann nimmt APNs alte Token außer Betrieb. Braze hat darüber keine Kontrolle und keinen Einblick.

### Schritt 3: Eine Braze-Push-Campaign starten {#step-3-launching-a-braze-push-campaign}

Wenn eine Push-Campaign gestartet wird, sendet Braze Anfragen an APNs, um Ihre Nachricht zuzustellen. Konkret werden die Anfragen für jedes aktuell gültige Push-Token an APNs weitergeleitet, es sei denn, **An das neueste Gerät der/des Nutzer:in senden** ist ausgewählt. Nachdem Braze eine erfolgreiche Antwort von APNs erhalten hat, protokolliert Braze eine erfolgreiche Zustellung im Nutzerprofil, obwohl die/der Nutzer:in die eigentliche Nachricht möglicherweise aus folgenden Gründen nicht erhalten hat:
- Das Gerät ist ausgeschaltet.
- Das Gerät ist nicht mit dem Internet verbunden (WLAN oder Mobilfunk).
- Die App wurde kürzlich deinstalliert.

Braze verwendet das im Dashboard hochgeladene SSL-Push-Zertifikat, um sich zu authentifizieren und zu verifizieren, dass es autorisiert ist, Push-Benachrichtigungen an die bereitgestellten Push-Token zu senden. Wenn ein Gerät online ist, sollte die Benachrichtigung kurz nach dem Versand der Campaign empfangen werden. Beachten Sie, dass Braze das standardmäßige APNs-[Ablaufdatum](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) für Benachrichtigungen auf 30 Tage setzt.

### Schritt 4: Ungültige Token entfernen {#step-4-removing-invalid-tokens}

Wenn [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) uns mitteilt, dass eines der Push-Token, an die wir eine Nachricht zu senden versuchten, ungültig ist, entfernen wir diese Token aus den Nutzerprofilen, mit denen sie verknüpft waren.

{% alert note %}
Es ist normal, dass APNs zunächst einen Erfolgsstatus zurückgibt, auch wenn ein Token nicht mehr registriert ist, da APNs Ereignisse zur Token-Ungültigmachung nicht sofort meldet. APNs verzögert absichtlich die Rückgabe eines `410`-Status für ungültige Token nach einem zufälligen Zeitplan, der den Schutz der Privatsphäre der Nutzer:innen gewährleisten und das Tracking von App-Deinstallationen verhindern soll. Sie können weiterhin sicher Benachrichtigungen an ein nicht registriertes Token senden, bis APNs einen `410`-Status zurückgibt.
{% endalert %}

## Push-Fehlerprotokolle verwenden {#using-the-push-error-logs}

Das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab) zeigt Ihnen alle Nachrichten (insbesondere Fehlermeldungen), die mit Ihren Campaigns und Sendungen verbunden sind, einschließlich Push-Benachrichtigungsfehler. Dieses Fehlerprotokoll bietet eine Vielzahl von Warnungen, die sehr hilfreich sein können, um herauszufinden, warum Ihre Campaigns nicht wie erwartet funktionieren. Wenn Sie eine Fehlermeldung auswählen, werden Sie zur entsprechenden Dokumentation weitergeleitet, die Ihnen bei der Fehlerbehebung eines bestimmten Vorfalls hilft.

![Push-Fehlerprotokolle mit dem Zeitpunkt des Fehlers, dem App-Namen, dem Kanal, dem Fehlertyp und der Fehlermeldung.]({% image_buster /assets/img_archive/message_activity_log.png %})

Häufige Fehler, die hier auftreten können, sind nutzerspezifische Benachrichtigungen wie [„Received Unregistered Sending to Push Token“](#swift_received-unregistered-sending).

Darüber hinaus bietet Braze auch ein Push-Changelog im Nutzerprofil unter dem Tab **Engagement**. Dieses Changelog gibt Einblick in das Push-Registrierungsverhalten, wie z. B. Token-Invalidierung, Push-Registrierungsfehler, Token, die zu neuen Nutzer:innen verschoben werden, usw.

![Tab „Engagement“ im Braze-Nutzerprofil mit dem Push-Registrierungs-Changelog.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Fehler im Nachrichtenaktivitätsprotokoll {#message-activity-log-errors}

#### Received Unregistered Sending to Push Token {#received-unregistered-sending}

- Stellen Sie sicher, dass das Push-Token, das über die Methode `AppDelegate.braze?.notifications.register(deviceToken:)` an Braze gesendet wird, gültig ist. Sie können im **Nachrichtenaktivitätsprotokoll** das Push-Token einsehen. Es sollte in etwa so aussehen: `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6` – ein langer String aus Buchstaben und Zahlen. Wenn Ihr Push-Token anders aussieht, überprüfen Sie Ihren [Code]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-32-register-push-tokens-with-braze) zum Senden der Push-Token an Braze.
- Stellen Sie sicher, dass Ihr Push-Provisioning-Profil mit der Umgebung übereinstimmt, in der Sie testen. Universelle Zertifikate können im Braze-Dashboard so konfiguriert werden, dass sie entweder an die Entwicklungs- oder die Produktions-APNs-Umgebung senden. Die Verwendung eines Entwicklungszertifikats für eine Produktions-App oder eines Produktionszertifikats für eine Entwicklungs-App funktioniert nicht.
 - Überprüfen Sie, ob das Push-Token, das Sie bei Braze hochgeladen haben, mit dem Provisioning-Profil übereinstimmt, das Sie zum Erstellen der App verwendet haben, von der das Push-Token gesendet wurde.

#### Device Token not for topic {#device-token-not-for-topic}

APNs gibt `DeviceTokenNotForTopic` (HTTP-Status 400) zurück, wenn das Push-Token nicht zum konfigurierten Topic (Bundle-ID) Ihrer Zugangsdaten passt. Braze kann dies im **Nachrichtenaktivitätsprotokoll** oder in den Push-Zustellungsprotokollen als `DeviceTokenNotForTopic` anzeigen.

So beheben Sie die Abweichung:

1. Bestätigen Sie, dass die **Bundle-ID** der App mit der **App Bundle ID** in Braze übereinstimmt (**Einstellungen** > **App-Einstellungen** > **Push-Benachrichtigungseinstellungen**).
2. Überprüfen Sie, ob das Provisioning-Profil, das zum Erstellen der App verwendet wurde, die Push-Fähigkeit für diese Bundle-ID enthält.
3. Bestätigen Sie, dass die bei Braze hochgeladenen Push-Zugangsdaten mit der Umgebung der App übereinstimmen (Entwicklung versus Produktion).
4. Überprüfen Sie bei `.p8`-Schlüsseln, ob **Team ID** und **Key ID** in Braze mit Ihrem Apple-Developer-Konto übereinstimmen.
5. Laden Sie einen gültigen `.p8`-Schlüssel oder ein `.p12`-Zertifikat erneut hoch, wenn die Zugangsdaten rotiert oder widerrufen wurden.

Bevorzugen Sie nach Möglichkeit `.p8`-Authentifizierungsschlüssel. Informationen zu Zugangsdatentypen und Dashboard-Statusanzeigen finden Sie unter [Zu einem .p8-Authentifizierungsschlüssel migrieren]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key).

#### BadDeviceToken beim Senden an Push-Token {#baddevicetoken-sending-to-push-token}

`BadDeviceToken` ist ein APNs-Fehlercode und stammt nicht von Braze. Es kann verschiedene Gründe geben, warum diese Antwort zurückgegeben wird, darunter die folgenden:

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## Probleme bei der Push-Registrierung {#push-registration-issues}

### Keine Aufforderung zur Push-Registrierung {#no-push-registration-prompt}

Wenn die Anwendung Sie nicht zur Registrierung für Push-Benachrichtigungen auffordert, liegt wahrscheinlich ein Problem mit Ihrer Push-Registrierungsintegration vor. Stellen Sie sicher, dass Sie unsere [Dokumentation]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) befolgt und unsere Push-Registrierung korrekt integriert haben. Sie können auch Breakpoints in Ihrem Code setzen, um sicherzustellen, dass der Push-Registrierungscode ausgeführt wird.

### Keine „push-registrierten“ Nutzer:innen im Dashboard sichtbar (vor dem Senden von Nachrichten) {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

Stellen Sie sicher, dass Ihre App korrekt konfiguriert ist, um Push-Benachrichtigungen zuzulassen. Häufige Fehlerquellen, die Sie überprüfen sollten:

- Prüfen Sie, ob Ihre App Sie auffordert, Push-Benachrichtigungen zuzulassen. In der Regel erscheint diese Aufforderung beim ersten Öffnen der App, sie kann aber auch an anderer Stelle programmiert werden. Wenn sie nicht dort erscheint, wo sie erscheinen sollte, liegt das Problem wahrscheinlich in der grundlegenden Konfiguration der Push-Funktionen Ihrer App.
  - Überprüfen Sie, ob die Schritte für die [Push-Integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) erfolgreich abgeschlossen wurden.
  - Prüfen Sie, ob das Provisioning-Profil, mit dem Ihre App erstellt wurde, Berechtigungen für Push enthält. Stellen Sie sicher, dass Sie alle verfügbaren Provisioning-Profile von Ihrem Apple-Entwicklerkonto abrufen. Um dies zu bestätigen, führen Sie die folgenden Schritte aus:
    1. Navigieren Sie in Xcode zu **Preferences > Accounts** (oder verwenden Sie die Tastenkombination <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Wählen Sie die Apple-ID aus, die Sie für Ihr Entwicklerkonto verwenden, und klicken Sie auf **View Details**.
    3. Klicken Sie auf der nächsten Seite auf **<i class="fas fa-redo-alt"></i> Refresh** und bestätigen Sie, dass Sie alle verfügbaren Provisioning-Profile abrufen.
- Prüfen Sie, ob Sie die [Push-Funktion korrekt aktiviert]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-2-enable-push-capabilities) haben in Ihrer App.
- Prüfen Sie, ob Ihr Push-Provisioning-Profil mit der Umgebung übereinstimmt, in der Sie testen. Universelle Zertifikate können im Braze-Dashboard so konfiguriert werden, dass sie entweder an die Entwicklungs- oder die Produktions-APNs-Umgebung senden. Die Verwendung eines Entwicklungszertifikats für eine Produktions-App oder eines Produktionszertifikats für eine Entwicklungs-App funktioniert nicht.
- Stellen Sie sicher, dass Sie unsere `registerPushToken`-Methode aufrufen, indem Sie einen Breakpoint in Ihrem Code setzen.
- Stellen Sie sicher, dass Sie mit einem Gerät testen (Push funktioniert nicht auf einem Simulator) und eine gute Netzwerkverbindung haben.

## Push-Benachrichtigungen gesendet, aber nicht auf den Geräten der Nutzer:innen angezeigt {#push-notifications-sent-but-not-displayed-on-users-devices}

### „Push-registrierte“ Nutzer:innen nach dem Senden von Nachrichten nicht mehr aktiviert {#push-registered-users-no-longer-enabled-after-sending-messages}

Dies deutet wahrscheinlich darauf hin, dass die Nutzer:innen ein ungültiges Push-Token hatten. Dies kann aus mehreren Gründen passieren:

#### Dashboard- und App-Zertifikat stimmen nicht überein {#dashboard-and-app-certificate-mismatch}

Wenn das Push-Zertifikat, das Sie im Dashboard hochgeladen haben, nicht mit dem im Bereitstellungsprofil übereinstimmt, mit dem Ihre App erstellt wurde, wird APNs das Token ablehnen. Überprüfen Sie, ob Sie das richtige Zertifikat hochgeladen und eine weitere Sitzung in der App abgeschlossen haben, bevor Sie eine weitere Testbenachrichtigung versuchen.

#### Anwendung wurde deinstalliert {#application-was-uninstalled}

Wenn Nutzer:innen Ihre Anwendung deinstalliert haben, wird ihr Push-Token ungültig und beim nächsten Senden entfernt.

#### Bereitstellungsprofil neu generieren {#regenerating-your-provisioning-profile}

Als letzten Ausweg können Sie von vorne beginnen und ein komplett neues Bereitstellungsprofil erstellen, um Konfigurationsfehler zu beheben, die durch die Arbeit mit mehreren Umgebungen, Profilen und Apps gleichzeitig entstehen. Es gibt viele „bewegliche Teile“ bei der Einrichtung von Push-Benachrichtigungen, daher ist es manchmal am besten, von Anfang an neu zu beginnen. Dies hilft auch dabei, das Problem einzugrenzen, falls Sie die Fehlerbehebung fortsetzen müssen.

### Nachrichten werden nicht an „push-registrierte“ Nutzer:innen zugestellt {#messages-not-delivered-to-push-registered-users}

#### App ist im Vordergrund {#app-is-foregrounded}

Auf iOS-Versionen, die Push nicht über das `UserNotifications`-Framework integrieren, wird die Push-Nachricht nicht angezeigt, wenn die App im Vordergrund ist, wenn die Nachricht empfangen wird. Sie sollten die App auf Ihren Testgeräten in den Hintergrund versetzen, bevor Sie Testnachrichten senden.

#### Testbenachrichtigung falsch geplant {#test-notification-scheduled-incorrectly}

Überprüfen Sie den Zeitplan, den Sie für Ihre Testnachricht festgelegt haben. Wenn die Zustellung auf Ortszeit oder [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing) eingestellt ist, haben Sie die Nachricht möglicherweise noch nicht erhalten (oder die App war im Vordergrund, als sie empfangen wurde).

### Nutzer:in nicht „push-registriert“ für die getestete App {#user-not-push-registered-for-the-app-being-tested}

Überprüfen Sie das Nutzerprofil der Person, an die Sie eine Testnachricht senden möchten. Unter dem Tab **Engagement** sollte eine Liste der „push-fähigen Apps“ angezeigt werden. Überprüfen Sie, ob die App, an die Sie Testnachrichten senden möchten, in dieser Liste enthalten ist. Nutzer:innen werden als „Push-registriert“ angezeigt, wenn sie ein Push-Token für eine beliebige App in Ihrem Workspace haben, sodass dies ein falsch positives Ergebnis sein könnte.

Folgendes würde auf ein Problem mit der Push-Registrierung hinweisen oder darauf, dass das Token der Nutzer:innen nach dem Senden von APNs als ungültig an Braze zurückgegeben wurde:

![Ein Nutzerprofil, das die Kontakteinstellungen anzeigt. Unter Push wird „No Apps“ angezeigt.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Push-Klicks werden nicht protokolliert {#push-clicks-not-logged}

- Stellen Sie sicher, dass Sie die [Schritte zur Push-Integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling) befolgt haben.
- Braze verarbeitet keine Push-Benachrichtigungen, die im Vordergrund stillschweigend empfangen werden (standardmäßiges Vordergrund-Push-Verhalten vor dem `UserNotifications`-Framework). Das bedeutet, dass Links nicht geöffnet und Push-Klicks nicht protokolliert werden. Wenn Ihre Anwendung das `UserNotifications`-Framework noch nicht integriert hat, verarbeitet Braze keine Push-Benachrichtigungen, wenn der Anwendungsstatus `UIApplicationStateActive` ist. Stellen Sie sicher, dass Ihre App Aufrufe an [Push-Verarbeitungsmethoden]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling) nicht verzögert; andernfalls behandelt das Swift SDK Push-Benachrichtigungen möglicherweise als stille Vordergrund-Push-Ereignisse und verarbeitet sie nicht.

## Deeplinks funktionieren nicht {#deep-links-not-working}

Für eine umfassende Fehlerbehebung über alle Kanäle hinweg – einschließlich Universal Links, benutzerdefinierter Schemata, E-Mail und Drittanbieter wie Branch – siehe [Fehlerbehebung für Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

### Web-Links aus Push-Klicks öffnen sich nicht {#web-links-from-push-clicks-not-opening}

Links in Push-Benachrichtigungen müssen ATS-konform sein, um in Web-Views geöffnet zu werden. Stellen Sie sicher, dass Ihre Web-Links HTTPS verwenden. Weitere Informationen finden Sie unter [ATS-Konformität]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#app-transport-security-ats).

### Deeplinks aus Push-Klicks öffnen sich nicht {#deep-links-from-push-clicks-not-opening}

Der Großteil des Codes, der Deeplinks verarbeitet, verarbeitet auch Push-Öffnungen. Stellen Sie zunächst sicher, dass Push-Öffnungen protokolliert werden. Falls nicht, beheben Sie dieses Problem (da die Lösung häufig auch die Link-Verarbeitung behebt).

Wenn Öffnungen protokolliert werden, prüfen Sie, ob es sich um ein allgemeines Problem mit dem Deeplink handelt oder um ein Problem mit der Deeplink-Verarbeitung bei Push-Klicks. Testen Sie dazu, ob ein Deeplink aus einem In-App-Nachrichten-Klick funktioniert.

{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
## Fehlerbehebung

### Push wird nach dem Schließen der App über den Task-Switcher nicht angezeigt {#push-doesnt-appear-after-app-is-closed-from-task-switcher}

Wenn Sie feststellen, dass Push-Benachrichtigungen nach dem Schließen der App über den Task-Switcher nicht mehr angezeigt werden, befindet sich Ihre App wahrscheinlich im Debug-Modus. .NET MAUI fügt im Debug-Modus ein Grundgerüst hinzu, das verhindert, dass Apps Push-Benachrichtigungen empfangen, nachdem ihr Prozess beendet wurde. Wenn Sie Ihre App im Release-Modus ausführen, sollten Sie Push-Benachrichtigungen auch nach dem Schließen der App über den Task-Switcher sehen.

### Angepasste Notification Factory wird nicht korrekt gesetzt {#custom-notification-factory-not-being-set-correctly}

Angepasste Notification Factories (und alle Delegates) müssen [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) erweitern, um über die C#- und Java-Grenze hinweg korrekt zu funktionieren. Weitere Informationen zur Implementierung von Java-Schnittstellen finden Sie unter [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces).

{% endsdktab %}
{% endsdktabs %}

## Zeilenumbrüche in Push-Benachrichtigungen {#push-linebreaks}

Beim Verfassen von Push-Benachrichtigungen mit Liquid-Tags werden Zeilenumbrüche neben Liquid-Tags automatisch entfernt, bevor die Nachricht gesendet wird. Im [Push-Benachrichtigungs-Composer]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message) werden diese Zeilenumbrüche wieder eingefügt, damit Ihre Nachricht beim Bearbeiten lesbar bleibt. Wenn Sie beim Speichern Ihrer Nachricht Zeilenumbrüche um Liquid-Tags herum bemerken, ist dies das erwartete Verhalten.