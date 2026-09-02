## Den Braze/APNs-Workflow verstehen {#understanding-the-brazeapns-workflow}

Der Apple Push Notification service (APNs) ist die Infrastruktur zum Senden von Push-Benachrichtigungen an Anwendungen, die auf Apple-Plattformen laufen. Hier ist die vereinfachte Struktur, wie Push-Benachrichtigungen für die Geräte Ihrer Nutzer:innen aktiviert werden und wie Braze Push-Benachrichtigungen an sie senden kann:

1. Sie konfigurieren das Push-Zertifikat und das Provisioning-Profil
2. Geräte registrieren sich bei APNs und stellen Braze Push-Token bereit
3. Sie starten eine Braze-Push-Campaign
4. Braze entfernt ungültige Token

### Schritt 1: Push-Zertifikat und Provisioning-Profil konfigurieren {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Bei der Entwicklung Ihrer App müssen Sie ein SSL-Zertifikat erstellen, um Push-Benachrichtigungen zu aktivieren. Dieses Zertifikat wird in das Provisioning-Profil aufgenommen, mit dem Ihre App erstellt wird, und muss außerdem in das Braze-Dashboard hochgeladen werden. Das Zertifikat ermöglicht es Braze, APNs mitzuteilen, dass wir berechtigt sind, Push-Benachrichtigungen in Ihrem Namen zu senden.

Es gibt zwei Arten von [Provisioning-Profilen](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) und Zertifikaten: Entwicklung und Distribution. Wir empfehlen, nur Distribution-Profile und -Zertifikate zu verwenden, um Verwechslungen zu vermeiden. Wenn Sie sich für unterschiedliche Profile und Zertifikate für Entwicklung und Distribution entscheiden, stellen Sie sicher, dass das im Dashboard hochgeladene Zertifikat mit dem Provisioning-Profil übereinstimmt, das Sie derzeit verwenden.

{% alert warning %}
Ändern Sie nicht die Umgebung des Push-Zertifikats (Entwicklung versus Produktion). Ein Wechsel des Push-Zertifikats auf die falsche Umgebung kann dazu führen, dass die Push-Token Ihrer Nutzer:innen versehentlich entfernt werden, sodass sie per Push nicht mehr erreichbar sind.
{% endalert %}

### Schritt 2: Geräte registrieren sich bei APNs und stellen Braze Push-Token bereit {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Wenn Nutzer:innen Ihre App öffnen, werden sie aufgefordert, Push-Benachrichtigungen zu akzeptieren. Wenn sie diese Aufforderung annehmen, generiert APNs ein Push-Token für das jeweilige Gerät. Das Swift SDK sendet das Push-Token sofort und asynchron für Apps, die die standardmäßige [automatische Flush-Richtlinie]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) verwenden. Sobald wir ein Push-Token mit einer/einem Nutzer:in verknüpft haben, wird diese:r im Dashboard auf dem Kundenprofil unter dem Tab **Engagement** als „Push Registered“ angezeigt und ist berechtigt, Push-Benachrichtigungen von Braze-Campaigns zu erhalten.

{% alert note %}
Ab macOS 13 können Sie auf bestimmten Geräten Push-Benachrichtigungen in einem iOS-16-Simulator unter Xcode 14 testen. Weitere Details finden Sie in den [Xcode 14 Release Notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Überlegungen zur Push-Token-Generierung {#considerations-for-push-token-generation}

- Wenn Nutzer:innen Ihre App auf einem anderen Gerät installieren, wird ein weiteres Token auf die gleiche Weise erstellt und erfasst.
- Wenn Nutzer:innen Ihre App neu installieren, wird ein neues Token generiert und an Braze weitergegeben. Das ursprüngliche Token kann jedoch weiterhin von APNs und Braze als gültig protokolliert sein.
- Wenn Nutzer:innen Ihre App deinstallieren, wird Braze nicht sofort darüber benachrichtigt, und das Token erscheint weiterhin als gültig, bis es von APNs außer Betrieb genommen wird.
- Irgendwann wird APNs alte Token außer Betrieb nehmen. Braze hat darauf weder Einfluss noch Einblick.

### Schritt 3: Eine Braze-Push-Campaign starten {#step-3-launching-a-braze-push-campaign}

Wenn eine Push-Campaign gestartet wird, sendet Braze Anfragen an APNs, um Ihre Nachricht zuzustellen. Konkret werden die Anfragen für jedes derzeit gültige Push-Token an APNs übermittelt, es sei denn, **An das neueste Gerät des Nutzers/der Nutzerin senden** ist ausgewählt. Nachdem Braze eine erfolgreiche Antwort von APNs erhalten hat, protokollieren wir eine erfolgreiche Zustellung im Kundenprofil, obwohl die/der Nutzer:in die eigentliche Nachricht möglicherweise aus folgenden Gründen nicht erhalten hat:
- Das Gerät ist ausgeschaltet.
- Das Gerät ist nicht mit dem Internet verbunden (WLAN oder Mobilfunk).
- Die App wurde kürzlich deinstalliert.

Braze verwendet das im Dashboard hochgeladene SSL-Push-Zertifikat, um sich zu authentifizieren und zu bestätigen, dass wir berechtigt sind, Push-Benachrichtigungen an die bereitgestellten Push-Token zu senden. Wenn ein Gerät online ist, sollte die Benachrichtigung kurz nach dem Versand der Campaign empfangen werden. Beachten Sie, dass Braze das standardmäßige APNs-[Ablaufdatum](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) für Benachrichtigungen auf 30 Tage festlegt.

### Schritt 4: Ungültige Token entfernen {#step-4-removing-invalid-tokens}

Wenn [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) uns darüber informiert, dass Push-Token, an die wir eine Nachricht senden wollten, ungültig sind, entfernen wir diese Token aus den Nutzerprofilen, mit denen sie verknüpft waren.

{% alert note %}
Es ist normal, dass APNs zunächst einen Erfolgsstatus zurückgibt, auch wenn ein Token abgemeldet wurde, da APNs Token-Ungültigkeitsereignisse nicht sofort meldet. APNs verzögert absichtlich die Rückgabe eines `410`-Status für ungültige Token nach einem zufälligen Zeitplan, der dem Schutz der Privatsphäre der Nutzer:innen dient und das Tracking von App-Deinstallationen verhindert. Sie können weiterhin Benachrichtigungen an ein abgemeldetes Token senden, bis APNs einen `410`-Status zurückgibt.
{% endalert %}

## Push-Fehlerprotokolle verwenden {#using-the-push-error-logs}

Das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) bietet Ihnen die Möglichkeit, alle Nachrichten (insbesondere Fehlermeldungen) einzusehen, die mit Ihren Campaigns und Sendungen zusammenhängen, einschließlich Push-Benachrichtigungsfehler. Dieses Fehlerprotokoll liefert eine Vielzahl von Warnungen, die sehr hilfreich sein können, um herauszufinden, warum Ihre Campaigns nicht wie erwartet funktionieren. Wenn Sie auf eine Fehlermeldung klicken, werden Sie zur entsprechenden Dokumentation weitergeleitet, die Ihnen bei der Fehlerbehebung eines bestimmten Vorfalls hilft.

![Push-Fehlerprotokolle mit Zeitpunkt des Fehlers, App-Name, Kanal, Fehlertyp und Fehlermeldung.]({% image_buster /assets/img_archive/message_activity_log.png %})

Häufige Fehler, die hier auftreten können, sind nutzerspezifische Benachrichtigungen wie [„Received Unregistered Sending to Push-Token“](#swift_received-unregistered-sending).

Darüber hinaus stellt Braze auch ein Push-Changelog im Kundenprofil unter dem Tab **Engagement** bereit. Dieses Changelog gibt Einblick in das Push-Registrierungsverhalten, wie z. B. Token-Invalidierung, Push-Registrierungsfehler, Token, die zu neuen Nutzer:innen verschoben werden usw.

![Tab „Engagement“ im Braze-Kundenprofil mit dem Push-Registrierungs-Changelog.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Fehler im Nachrichtenaktivitätsprotokoll {#message-activity-log-errors}

#### Received Unregistered Sending to Push-Token {#received-unregistered-sending}

- Stellen Sie sicher, dass das Push-Token, das über die Methode `AppDelegate.braze?.notifications.register(deviceToken:)` an Braze gesendet wird, gültig ist. Sie können im **Nachrichtenaktivitätsprotokoll** das Push-Token einsehen. Es sollte in etwa so aussehen: `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6` – ein langer String aus einer Mischung von Buchstaben und Zahlen. Falls Ihr Push-Token anders aussieht, überprüfen Sie Ihren [Code]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-4-register-push-tokens-with-braze) zum Senden der Push-Token an Braze.
- Stellen Sie sicher, dass Ihr Push-Provisioning-Profil mit der Umgebung übereinstimmt, in der Sie testen. Universelle Zertifikate können im Braze-Dashboard so konfiguriert werden, dass sie entweder an die Entwicklungs- oder die Produktions-APNs-Umgebung senden. Ein Entwicklungszertifikat für eine Produktions-App oder ein Produktionszertifikat für eine Entwicklungs-App funktioniert nicht.
 - Überprüfen Sie, ob das Push-Token, das Sie bei Braze hochgeladen haben, mit dem Provisioning-Profil übereinstimmt, das Sie zum Erstellen der App verwendet haben, von der das Push-Token gesendet wurde.

#### Device Token Not for Topic

APNs gibt `DeviceTokenNotForTopic` (HTTP-Status 400) zurück, wenn das Push-Token nicht zum konfigurierten Topic (Bundle-ID) Ihrer Zugangsdaten passt. Braze kann dies im **Nachrichtenaktivitätsprotokoll** oder in den Push-Zustellungsprotokollen als `DeviceTokenNotForTopic` anzeigen.

So beheben Sie die Abweichung:

1. Bestätigen Sie, dass die **Bundle-ID** der App mit der **App Bundle ID** in Braze übereinstimmt (**Einstellungen** > **App-Einstellungen** > **Push-Benachrichtigungseinstellungen**).
2. Überprüfen Sie, ob das Provisioning-Profil, mit dem die App erstellt wurde, die Push-Fähigkeit für diese Bundle-ID enthält.
3. Bestätigen Sie, dass die bei Braze hochgeladenen Push-Zugangsdaten mit der Umgebung der App übereinstimmen (Entwicklung versus Produktion).
4. Überprüfen Sie bei `.p8`-Schlüsseln, ob **Team ID** und **Key ID** in Braze mit Ihrem Apple Developer-Konto übereinstimmen.
5. Laden Sie einen gültigen `.p8`-Schlüssel oder ein `.p12`-Zertifikat erneut hoch, falls Zugangsdaten rotiert oder widerrufen wurden.

Bevorzugen Sie `.p8`-Authentifizierungsschlüssel, wenn möglich. Informationen zu Zugangsdatentypen und Dashboard-Statusindikatoren finden Sie unter [Migration zu einem .p8-Authentifizierungsschlüssel]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key).

#### BadDeviceToken beim Senden an Push-Token {#baddevicetoken-sending-to-push-token}

`BadDeviceToken` ist ein APNs-Fehlercode und stammt nicht von Braze. Es kann verschiedene Gründe geben, warum diese Antwort zurückgegeben wird, darunter:

- Die App hat ein Push-Token erhalten, das für die im Dashboard hochgeladenen Zugangsdaten ungültig war.
- Push war für diesen Workspace deaktiviert.
- Die Nutzer:innen haben Push abgelehnt.
- Die App wurde deinstalliert.
- Apple hat das Push-Token aktualisiert, wodurch das alte Token ungültig wurde.
- Die App wurde für eine Produktionsumgebung erstellt, aber die bei Braze hochgeladenen Push-Zugangsdaten sind für eine Entwicklungsumgebung konfiguriert (oder umgekehrt).

## Probleme bei der Push-Registrierung {#push-registration-issues}

### Keine Aufforderung zur Push-Registrierung {#no-push-registration-prompt}

Wenn die Anwendung Sie nicht zur Registrierung für Push-Benachrichtigungen auffordert, liegt wahrscheinlich ein Problem mit Ihrer Push-Registrierungsintegration vor. Stellen Sie sicher, dass Sie unsere [Dokumentation]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) befolgt und unsere Push-Registrierung korrekt integriert haben. Sie können auch Haltepunkte in Ihrem Code setzen, um sicherzustellen, dass der Push-Registrierungscode ausgeführt wird.

### Keine „push-registrierten“ Nutzer:innen im Dashboard angezeigt (vor dem Senden von Nachrichten) {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

Stellen Sie sicher, dass Ihre App korrekt konfiguriert ist, um Push-Benachrichtigungen zu erlauben. Häufige Fehlerquellen, die überprüft werden sollten:

- Überprüfen Sie, ob Ihre App Sie auffordert, Push-Benachrichtigungen zu erlauben. In der Regel erscheint diese Aufforderung beim ersten Öffnen der App, kann aber auch an anderer Stelle programmiert werden. Wenn sie nicht dort erscheint, wo sie erscheinen sollte, liegt das Problem wahrscheinlich in der grundlegenden Konfiguration der Push-Funktionen Ihrer App.
  - Überprüfen Sie, ob die Schritte für die [Push-Integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) erfolgreich abgeschlossen wurden.
  - Überprüfen Sie, ob das Provisioning-Profil, mit dem Ihre App erstellt wurde, Berechtigungen für Push enthält. Stellen Sie sicher, dass Sie alle verfügbaren Provisioning-Profile von Ihrem Apple-Entwicklerkonto abrufen. Führen Sie dazu die folgenden Schritte aus:
    1. Navigieren Sie in Xcode zu **Preferences > Accounts** (oder verwenden Sie das Tastaturkürzel <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Wählen Sie die Apple-ID aus, die Sie für Ihr Entwicklerkonto verwenden, und klicken Sie auf **View Details**.
    3. Klicken Sie auf der nächsten Seite auf **<i class="fas fa-redo-alt"></i> Refresh** und bestätigen Sie, dass Sie alle verfügbaren Provisioning-Profile abrufen.
- Überprüfen Sie, ob Sie die [Push-Funktionalität korrekt aktiviert]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-2-enable-push-capabilities) haben in Ihrer App.
- Überprüfen Sie, ob Ihr Push-Provisioning-Profil mit der Umgebung übereinstimmt, in der Sie testen. Universelle Zertifikate können im Braze-Dashboard so konfiguriert werden, dass sie entweder an die Entwicklungs- oder Produktions-APNs-Umgebung senden. Die Verwendung eines Entwicklungszertifikats für eine Produktions-App oder eines Produktionszertifikats für eine Entwicklungs-App funktioniert nicht.
- Stellen Sie sicher, dass Sie unsere `registerPushToken`-Methode aufrufen, indem Sie einen Haltepunkt in Ihrem Code setzen.
- Stellen Sie sicher, dass Sie mit einem Gerät testen (Push funktioniert nicht auf einem Simulator) und eine gute Netzwerkverbindung haben.

## Push-Benachrichtigungen gesendet, aber nicht auf Geräten der Nutzer:innen angezeigt {#push-notifications-sent-but-not-displayed-on-users-devices}

### „Push registrierte“ Nutzer:innen nach dem Senden von Nachrichten nicht mehr aktiviert {#push-registered-users-no-longer-enabled-after-sending-messages}

Dies deutet wahrscheinlich darauf hin, dass die:der Nutzer:in ein ungültiges Push-Token hatte. Dies kann aus mehreren Gründen passieren:

#### Dashboard- und App-Zertifikat stimmen nicht überein {#dashboard-and-app-certificate-mismatch}

Wenn das Push-Zertifikat, das Sie im Dashboard hochgeladen haben, nicht mit dem im Bereitstellungsprofil übereinstimmt, mit dem Ihre App erstellt wurde, lehnt APNs das Token ab. Überprüfen Sie, ob Sie das richtige Zertifikat hochgeladen und eine weitere Sitzung in der App abgeschlossen haben, bevor Sie eine weitere Test-Benachrichtigung versuchen.

#### Anwendung wurde deinstalliert {#application-was-uninstalled}

Wenn eine:r Nutzer:in Ihre Anwendung deinstalliert hat, wird das Push-Token ungültig und beim nächsten Versand entfernt.

#### Bereitstellungsprofil neu generieren {#regenerating-your-provisioning-profile}

Als letzten Ausweg können Sie von vorne beginnen und ein völlig neues Bereitstellungsprofil erstellen, um Konfigurationsfehler zu beheben, die durch die gleichzeitige Arbeit mit mehreren Umgebungen, Profilen und Apps entstehen. Es gibt viele „bewegliche Teile“ bei der Einrichtung von Push-Benachrichtigungen, sodass es manchmal am besten ist, von vorne zu beginnen. Dies hilft auch, das Problem zu isolieren, wenn Sie weiter Fehler beheben müssen.

### Nachrichten werden nicht an „Push registrierte“ Nutzer:innen zugestellt {#messages-not-delivered-to-push-registered-users}

#### App ist im Vordergrund {#app-is-foregrounded}

Auf iOS-Versionen, die Push nicht über das `UserNotifications`-Framework integrieren, wird die Push-Nachricht nicht angezeigt, wenn die App im Vordergrund ist, wenn sie empfangen wird. Sie sollten die App auf Ihren Testgeräten in den Hintergrund versetzen, bevor Sie Testnachrichten senden.

#### Testbenachrichtigung falsch geplant {#test-notification-scheduled-incorrectly}

Überprüfen Sie den Zeitplan, den Sie für Ihre Testnachricht festgelegt haben. Wenn die Zustellung auf Ortszeit oder [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) eingestellt ist, haben Sie die Nachricht möglicherweise einfach noch nicht erhalten (oder die App war im Vordergrund, als sie empfangen wurde).

### Nutzer:in ist nicht „Push registriert“ für die getestete App {#user-not-push-registered-for-the-app-being-tested}

Überprüfen Sie das Kundenprofil der:des Nutzer:in, an die:den Sie eine Testnachricht senden möchten. Unter dem Tab **Engagement** sollte eine Liste der „push-fähigen Apps“ angezeigt werden. Überprüfen Sie, ob die App, an die Sie Testnachrichten senden möchten, in dieser Liste enthalten ist. Nutzer:innen werden als „Push registriert“ angezeigt, wenn sie ein Push-Token für eine beliebige App in Ihrem Workspace haben, sodass dies ein falsch positives Ergebnis sein könnte.

Das Folgende würde auf ein Problem mit der Push-Registrierung hindeuten oder darauf, dass das Token der:des Nutzer:in nach dem Push von APNs als ungültig an Braze zurückgegeben wurde:

![Ein Kundenprofil, das die Kontakteinstellungen einer:eines Nutzer:in anzeigt. Unter Push wird „No Apps“ angezeigt.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Nicht protokollierte Push-Klicks {#push-clicks-not-logged}

- Stellen Sie sicher, dass Sie die [Schritte zur Push-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling) durchgeführt haben.
- Braze verarbeitet keine Push-Benachrichtigungen, die still im Vordergrund empfangen werden (Standardverhalten von Push im Vordergrund vor dem Framework `UserNotifications`). Das bedeutet, dass Links nicht geöffnet werden und Push-Klicks nicht protokolliert werden. Wenn das Framework `UserNotifications` noch nicht in Ihrer Anwendung integriert ist, verarbeitet Braze keine Push-Benachrichtigungen, wenn der Anwendungsstatus `UIApplicationStateActive` lautet. Stellen Sie sicher, dass Ihre App die Aufrufe von [Push-Verarbeitungsmethoden]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling) nicht verzögert. Andernfalls kann es sein, dass das Swift SDK Push-Benachrichtigungen als stille Push-Ereignisse im Vordergrund behandelt und sie nicht verarbeitet.

## Deeplinks funktionieren nicht {#deep-links-not-working}

Für eine umfassende Fehlerbehebung über alle Kanäle hinweg – einschließlich Universal Links, benutzerdefinierter Schemes, E-Mail und Drittanbieter wie Branch – siehe [Fehlerbehebung für Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

### Web-Links aus Push-Klicks öffnen sich nicht {#web-links-from-push-clicks-not-opening}

Links in Push-Benachrichtigungen müssen ATS-konform sein, um in Webviews geöffnet zu werden. Stellen Sie sicher, dass Ihre Web-Links HTTPS verwenden. Weitere Informationen finden Sie unter [ATS-Konformität]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking#app-transport-security-ats).

### Deeplinks aus Push-Klicks öffnen sich nicht {#deep-links-from-push-clicks-not-opening}

Der Großteil des Codes, der Deeplinks verarbeitet, verarbeitet auch Push-Öffnungen. Stellen Sie zunächst sicher, dass Push-Öffnungen protokolliert werden. Falls nicht, beheben Sie dieses Problem (da die Behebung oft auch die Link-Verarbeitung korrigiert).

Wenn Öffnungen protokolliert werden, prüfen Sie, ob es sich um ein generelles Problem mit dem Deeplink handelt oder um ein Problem mit der Verarbeitung von Deeplinks bei Push-Klicks. Testen Sie dazu, ob ein Deeplink aus einem In-App-Nachrichten-Klick funktioniert.