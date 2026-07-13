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

## Den Arbeitsablauf von Braze/APNs verstehen {#understanding-the-brazeapns-workflow}

Der Apple Push Notification Service (APNs) ist Apples Infrastruktur für den Versand von Push-Benachrichtigungen an iOS- und OS X-Anwendungen. Hier ist die vereinfachte Struktur, wie Push-Benachrichtigungen für die Geräte Ihrer Nutzer:innen aktiviert werden und wie Braze Push-Benachrichtigungen an sie senden kann:

1. Sie konfigurieren das Push-Zertifikat und das Bereitstellungsprofil
2. Geräte registrieren sich für APNs und versorgen Braze mit Push-Token
3. Sie starten eine Braze-Push-Campaign
4. Braze entfernt ungültige Token

### 1. Schritt: Konfigurieren des Push-Zertifikats und des Bereitstellungsprofils {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Bei der Entwicklung Ihrer App müssen Sie ein SSL-Zertifikat erstellen, um Push-Benachrichtigungen zu aktivieren. Dieses Zertifikat wird in das Bereitstellungsprofil Ihrer App aufgenommen und muss außerdem in das Braze-Dashboard hochgeladen werden. Das Zertifikat ermöglicht es Braze, APNs mitzuteilen, dass wir in Ihrem Namen Push-Benachrichtigungen senden dürfen.

Es gibt zwei Arten von [Bereitstellungsprofilen](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) und Zertifikaten: Entwicklung und Verteilung. Um Unklarheiten zu vermeiden, empfehlen wir, nur Verteilungsprofile und -zertifikate zu verwenden. Wenn Sie unterschiedliche Profile und Zertifikate für die Entwicklung und Verteilung verwenden möchten, stellen Sie sicher, dass das in das Dashboard hochgeladene Zertifikat mit dem derzeit verwendeten Bereitstellungsprofil übereinstimmt.

{% alert warning %}
Ändern Sie nicht die Push-Zertifikat-Umgebung (Entwicklung oder Produktion). Wenn Sie das Push-Zertifikat in die falsche Umgebung ändern, kann dies dazu führen, dass Ihren Nutzer:innen versehentlich ihr Push-Token entzogen wird, sodass sie nicht mehr per Push erreichbar sind.
{% endalert %}

#### 2. Schritt: Geräte registrieren sich für APNs und versorgen Braze mit Push-Token {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Wenn Nutzer:innen Ihre App öffnen, werden sie aufgefordert, Push-Benachrichtigungen zu akzeptieren. Stimmen sie der Aufforderung zu, generieren die APNs ein Push-Token für das betreffende Gerät. Das iOS SDK sendet das Push-Token für Apps, die die standardmäßige [Auto-Flush-Richtlinie]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) verwenden, sofort und asynchron. Nachdem wir ein Push-Token mit einer Nutzer:in verknüpft haben, wird diese im Dashboard auf ihrem Nutzerprofil unter dem Tab **Engagement** als „Push registriert“ angezeigt und ist berechtigt, Push-Benachrichtigungen von Braze-Campaigns zu erhalten.

{% alert note %}
Ab Xcode 14 können Sie Remote-Push-Benachrichtigungen auf einem iOS-Simulator testen.
{% endalert %}

#### 3. Schritt: Starten einer Braze-Push-Campaign {#step-3-launching-a-braze-push-campaign}

Beim Starten einer Push-Campaign stellt Braze Anfragen an APNs, um Ihre Nachricht zuzustellen. Braze verwendet das im Dashboard hochgeladene SSL-Push-Zertifikat, um sich zu authentifizieren und zu überprüfen, ob wir Push-Benachrichtigungen an die angegebenen Push-Token senden dürfen. Wenn ein Gerät online ist, sollte die Benachrichtigung kurz nach dem Senden der Campaign empfangen werden. Beachten Sie, dass Braze das standardmäßige APNs-[Ablaufdatum](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) für Benachrichtigungen auf 30 Tage festlegt.

#### 4. Schritt: Entfernen ungültiger Token {#step-4-removing-invalid-tokens}

Wenn [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) uns informiert, dass eines der Push-Token, an das wir eine Nachricht senden wollten, ungültig ist, entfernen wir diese Token aus den Nutzerprofilen, mit denen sie verknüpft waren.

## Verwendung der Push-Fehlerprotokolle {#utilizing-the-push-error-logs}

Braze bietet ein Protokoll der Push-Benachrichtigungsfehler im **Nachrichten-Aktivitätsprotokoll**. Dieses Fehlerprotokoll enthält eine Reihe von Warnungen, die sehr hilfreich sein können, um festzustellen, warum Ihre Campaigns nicht wie erwartet funktionieren. Wenn Sie auf eine Fehlermeldung klicken, werden Sie zur entsprechenden Dokumentation weitergeleitet, die Sie bei der Fehlerbehebung unterstützt.

![Push-Fehlerprotokolle, die den Zeitpunkt des Auftretens des Fehlers, den Namen der App, den Kanal, den Fehlertyp und die Fehlermeldung anzeigen.]({% image_buster /assets/img_archive/message_activity_log.png %})

Zu den häufigen Fehlern, die Ihnen hier angezeigt werden, gehören nutzerspezifische Benachrichtigungen wie [„Nicht registrierte Sendung an Push-Token empfangen“](#received-unregistered-sending).

Darüber hinaus stellt Braze unter dem Tab **Engagement** ein Push-Changelog für das Nutzerprofil bereit. Dieses Changelog enthält Insights zum Verhalten bei der Push-Registrierung, z. B. Token-Invalidierung, Fehler bei der Push-Registrierung, zu neuen Nutzer:innen verschobene Token usw.

![Animiertes Beispiel für Content-Cards.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

## Probleme bei der Push-Registrierung {#push-registration-issues}

Um die Logik der Push-Registrierung für Ihre Anwendung zu verifizieren, implementieren Sie [Push-Unit-Tests]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Keine Push-Registrierungsaufforderung {#no-push-registration-prompt}

Wenn die Anwendung Sie nicht auffordert, sich für Push-Benachrichtigungen zu registrieren, liegt wahrscheinlich ein Problem mit der Integration der Push-Registrierung vor. Stellen Sie sicher, dass Sie unsere [Dokumentation]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) befolgt und unsere Push-Registrierung korrekt integriert haben. Sie können auch Haltepunkte in Ihrem Code setzen, um sicherzustellen, dass der Code für die Push-Registrierung ausgeführt wird.

#### Keine „push-registrierten“ Nutzer:innen im Dashboard sichtbar {#no-push-registered-users-showing-in-the-dashboard}

- Überprüfen Sie, ob Sie von Ihrer App aufgefordert werden, Push-Benachrichtigungen zuzulassen. Normalerweise erscheint diese Aufforderung beim ersten Öffnen der App, aber sie kann auch so programmiert werden, dass sie an anderen Stellen erscheint. Wenn sie nicht dort erscheint, wo sie sein sollte, liegt das Problem wahrscheinlich bei der Grundkonfiguration der Push-Funktionen Ihrer App.
  - Überprüfen Sie, ob die Schritte für die [Push-Integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) erfolgreich abgeschlossen wurden.
  - Vergewissern Sie sich, dass das Bereitstellungsprofil Ihrer App Berechtigungen für Push enthält. Stellen Sie sicher, dass Sie alle verfügbaren Bereitstellungsprofile aus Ihrem Apple-Entwicklerkonto abrufen. Um dies zu bestätigen, führen Sie die folgenden Schritte aus:
    1. Navigieren Sie in Xcode zu **Preferences > Accounts** (oder verwenden Sie die Tastenkombination <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Wählen Sie die Apple ID, die Sie für Ihr Entwicklerkonto verwenden, und klicken Sie auf **View Details**.
    3. Klicken Sie auf der nächsten Seite auf **<i class="fas fa-redo-alt"></i> Refresh** und bestätigen Sie, dass Sie alle verfügbaren Bereitstellungsprofile abrufen.
- Überprüfen Sie, ob die [Push-Funktion in Ihrer App korrekt aktiviert ist]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-2-enable-push-capabilities).
- Stellen Sie sicher, dass das Push-Bereitstellungsprofil mit der Umgebung übereinstimmt, in der Sie testen. Universelle Zertifikate können im Braze-Dashboard so konfiguriert werden, dass sie entweder an die APNs-Entwicklungs- oder die Produktionsumgebung gesendet werden. Die Verwendung eines Entwicklungszertifikats für eine Produktionsanwendung oder eines Produktionszertifikats für eine Entwicklungsanwendung wird nicht funktionieren.
- Überprüfen Sie, ob unsere Methode `registerPushToken` aufgerufen wird, indem Sie einen Haltepunkt in Ihrem Code setzen.
- Stellen Sie sicher, dass Sie sich auf einem Gerät befinden (Push funktioniert nicht auf einem Simulator) und eine gute Netzwerkverbindung haben.

## Geräte erhalten keine Push-Benachrichtigungen {#devices-not-receiving-push-notifications}

### Nutzer:innen sind nach dem Senden einer Push-Benachrichtigung nicht mehr „push-registriert“ {#users-no-longer-push-registered-after-sending-a-push-notification}

Dies deutet wahrscheinlich darauf hin, dass das Push-Token der Nutzer:in ungültig war. Dafür kann es mehrere Gründe geben:

#### Dashboard und App-Zertifikat stimmen nicht überein {#dashboard-and-app-certificate-mismatch}

Wenn das Push-Zertifikat, das Sie im Dashboard hochgeladen haben, nicht dasselbe ist wie das im Bereitstellungsprofil, mit dem Ihre App erstellt wurde, lehnen die APNs das Token ab. Vergewissern Sie sich, dass Sie das richtige Zertifikat hochgeladen und eine weitere Sitzung in der App abgeschlossen haben, bevor Sie eine weitere Testbenachrichtigung versuchen.

##### Deinstallationen {#uninstalls}

Wenn eine Nutzer:in Ihre Anwendung deinstalliert hat, ist ihr Push-Token ungültig und wird beim nächsten Senden entfernt.

##### Ihr Bereitstellungsprofil neu generieren {#regenerating-your-provisioning-profile}

Als letzten Ausweg können Sie von vorne beginnen und ein völlig neues Bereitstellungsprofil erstellen, um Konfigurationsfehler zu beheben, die durch die gleichzeitige Arbeit mit mehreren Umgebungen, Profilen und Anwendungen entstehen. Bei der Einrichtung von Push-Benachrichtigungen für iOS-Apps gibt es viele „bewegliche Teile“. Daher ist es mitunter sinnvoll, noch einmal von vorn zu beginnen. Diese Vorgehensweise ist auch hilfreich, um das Problem einzugrenzen, wenn Sie die Fehlerbehebung fortsetzen müssen.

#### Nutzer:innen sind nach dem Senden einer Push-Benachrichtigung weiterhin „push-registriert“ {#users-still-push-registered-after-sending-a-push-notification}

##### App befindet sich im Vordergrund {#app-is-foregrounded}

Bei iOS-Versionen, die Push nicht über das Framework `UserNotifications` integrieren, wird die Nachricht nicht angezeigt, wenn sich die App beim Empfang der Push-Nachricht im Vordergrund befindet. Vor dem Senden von Testnachrichten sollten Sie die App auf Ihren Testgeräten in den Hintergrund versetzen.

##### Testbenachrichtigung falsch geplant {#test-notification-scheduled-incorrectly}

Überprüfen Sie den Zeitplan, den Sie für Ihre Testnachricht festgelegt haben. Wenn sie auf Zustellung in der lokalen Zeitzone oder [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) eingestellt ist, haben Sie die Nachricht möglicherweise noch nicht erhalten (oder die App war im Vordergrund, als sie empfangen wurde).

#### Nutzer:in ist für die zu testende App nicht „push-registriert“ {#user-not-push-registered-for-the-app-being-tested}

Überprüfen Sie das Nutzerprofil der Nutzer:in, an die Sie eine Testnachricht senden möchten. Unter dem Tab **Engagement** sollte eine Liste der „pushbaren Apps“ angezeigt werden. Vergewissern Sie sich, dass die App, an die Sie Testnachrichten senden möchten, in dieser Liste enthalten ist. Nutzer:innen werden als „Push registriert“ angezeigt, wenn sie ein Push-Token für eine beliebige App in Ihrem Workspace haben, es könnte sich also um ein falsches Positiv handeln.

Das Folgende deutet auf ein Problem mit der Push-Registrierung hin oder darauf, dass das Token der Nutzer:in von den APNs nach dem Push-Vorgang als ungültig an Braze zurückgegeben wurde:

![Ein Nutzerprofil, das die Kontakteinstellungen einer Nutzer:in anzeigt. Hier können Sie sehen, für welche Apps Push registriert ist.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Push-Nachrichten werden nicht gesendet {#push-messages-not-sending}

Zur Fehlerbehebung bei Push-Benachrichtigungen, die nicht gesendet werden, lesen Sie [Fehlerbehebung für Push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

## Fehler im Nachrichten-Aktivitätsprotokoll {#message-activity-log-errors}

### Nicht registrierte Sendung an Push-Token empfangen {#received-unregistered-sending}

- Stellen Sie sicher, dass das Push-Token, das über die Methode `[[Appboy sharedInstance] registerPushToken:]` an Braze gesendet wird, gültig ist. Im **Nachrichten-Aktivitätsprotokoll** können Sie das Push-Token einsehen. Es sollte etwa so aussehen wie `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, eine lange Zeichenkette mit einer Mischung aus Buchstaben und Zahlen. Wenn Ihr Push-Token anders aussieht, überprüfen Sie Ihren [Code]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-4-register-push-tokens-with-braze) zum Senden der Push-Token an Braze.
- Vergewissern Sie sich, dass das Push-Bereitstellungsprofil mit der Umgebung übereinstimmt, in der Sie testen. Universelle Zertifikate können im Braze-Dashboard so konfiguriert werden, dass sie entweder an die APNs-Entwicklungs- oder die Produktionsumgebung gesendet werden. Die Verwendung eines Entwicklungszertifikats für eine Produktionsanwendung oder eines Produktionszertifikats für eine Entwicklungsanwendung wird nicht funktionieren.
 - Überprüfen Sie, ob das Push-Token, das Sie auf Braze hochgeladen haben, mit dem Bereitstellungsprofil übereinstimmt, das Sie zum Erstellen der App verwendet haben, von der Sie das Push-Token gesendet haben.

#### Geräte-Token nicht zum Thema {#device-token-not-for-topic}

Dieser Fehler zeigt an, dass das Push-Zertifikat Ihrer App und die Bundle-ID nicht übereinstimmen. Überprüfen Sie, ob das Push-Zertifikat, das Sie auf Braze hochgeladen haben, mit dem Bereitstellungsprofil übereinstimmt, das zur Erstellung der App verwendet wurde, von der das Push-Token gesendet wurde.

#### BadDeviceToken beim Senden an Push-Token {#baddevicetoken-sending-to-push-token}

`BadDeviceToken` ist ein APNs-Fehlercode und stammt nicht von Braze. Es kann eine Reihe von Gründen dafür geben, dass diese Antwort zurückgegeben wird, wie beispielsweise:

- Die App hat ein Push-Token empfangen, das für die im Dashboard hochgeladenen Zugangsdaten ungültig war.
- Push wurde für diesen Workspace deaktiviert.
- Die Nutzer:in hat die Push-Funktion abbestellt.
- Die App wurde deinstalliert.
- Apple hat das Push-Token erneuert, wodurch das alte Token ungültig wurde.
- Die App wurde für eine Produktionsumgebung erstellt, aber die auf Braze hochgeladenen Push-Zugangsdaten sind für eine Entwicklungsumgebung eingestellt (oder umgekehrt).

## Probleme nach der Push-Zustellung {#issues-after-push-delivery}

Um die Push-Verarbeitung Ihrer Anwendung zu verifizieren, implementieren Sie [Push-Unit-Tests]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Nicht protokollierte Push-Klicks {#push-clicks-not-logged}

- Wenn dieses Problem nur unter iOS 10 auftritt, stellen Sie sicher, dass Sie die Schritte zur Push-Integration für [iOS 10]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling) befolgt haben.
- Braze verarbeitet keine Push-Benachrichtigungen, die still im Vordergrund empfangen werden (z. B. Standardverhalten von Push im Vordergrund vor dem Framework `UserNotifications`). Das bedeutet, dass Links nicht geöffnet werden und Push-Klicks nicht protokolliert werden. Wenn das Framework `UserNotifications` noch nicht in Ihrer Anwendung integriert ist, verarbeitet Braze keine Push-Benachrichtigungen, wenn der Anwendungsstatus `UIApplicationStateActive` lautet. Sie sollten sicherstellen, dass Ihre App die Aufrufe unserer [Push-Verarbeitungsmethoden]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling) nicht verzögert. Andernfalls kann es sein, dass das iOS SDK Push-Benachrichtigungen als stille Vordergrund-Push-Ereignisse behandelt und sie nicht weitergibt.

#### Weblinks von Push-Klicks werden nicht geöffnet {#web-links-from-push-clicks-not-opening}

Unter iOS 9+ müssen Links ATS-konform sein, damit sie in Webansichten geöffnet werden können. Stellen Sie sicher, dass Ihre Weblinks HTTPS verwenden. Weitere Informationen finden Sie in unserem Artikel zur [ATS-Konformität]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking#app-transport-security-ats).

#### Deeplinks von Push-Klicks werden nicht geöffnet {#deep-links-from-push-clicks-not-opening}

Der Großteil des Codes, der Deeplinks verarbeitet, verarbeitet auch Push-Öffnungen. Stellen Sie zunächst sicher, dass Push-Öffnungen protokolliert werden. Wenn nicht, [beheben Sie das Problem](#push-clicks-not-logged) (hierdurch wird oftmals auch die Linkverarbeitung korrigiert).

Wenn Öffnungen protokolliert werden, prüfen Sie, ob es sich um ein Problem mit Deeplinks im Allgemeinen oder nur mit Deeplinks bei der Verarbeitung von Push-Klicks handelt. Um dies herauszufinden, testen Sie per Klick auf eine In-App-Nachricht, ob ein Deeplink funktioniert.

#### Wenige oder keine direkten Öffnungen {#few-or-no-direct-opens}

Wenn mindestens eine Nutzer:in Ihre iOS-Push-Benachrichtigung öffnet, aber nur wenige oder keine _direkten Öffnungen_ in Braze protokolliert werden, gibt es möglicherweise ein Problem mit Ihrer [SDK-Integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview). Denken Sie daran, dass _direkte Öffnungen_ nicht für Testsendungen oder stille Push-Benachrichtigungen protokolliert werden.

- Stellen Sie sicher, dass die Nachrichten nicht als [stille Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications#sending-silent-push-notifications) gesendet werden. Die Nachricht muss Text im Titel oder Textkörper enthalten, um nicht als stille Nachricht zu gelten.
- Überprüfen Sie die folgenden Schritte im [Leitfaden zur Push-Integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration):
   - [Push-Registrierung]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-register-for-push-notifications-with-apns): Bei jedem einzelnen App-Start, vorzugsweise innerhalb von `application:didFinishLaunchingWithOptions:`, muss der Code aus Schritt 3 ausgeführt werden. Die Eigenschaft „delegate“ von `UNUserNotificationCenter.current()` muss einem Objekt zugewiesen sein, das `UNUserNotificationCenterDelegate` implementiert und die Methode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` enthält.
   - [Push-Verarbeitung aktivieren]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling): Überprüfen Sie, ob die Methode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` implementiert wurde.