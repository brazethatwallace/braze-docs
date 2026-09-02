---
nav_title: Häufige Push-Fehlermeldungen
article_title: Häufige Push-Fehlermeldungen
page_order: 22
page_type: reference
description: "Dieser Artikel behandelt häufige Push-bezogene Fehlermeldungen für iOS und Android und führt Sie durch mögliche Lösungen."
channel: push
platform:
- iOS
- Android
---

# Häufige Push-Fehlermeldungen {#common-push-error-messages}

> Diese Seite behandelt häufige Fehlermeldungen für Push-Messaging.

{% tabs %}
{% tab Android %}
## Push-Bounce: MismatchSenderId {#push-bounced-mismatchsenderid}
`MismatchSenderId` weist auf einen Authentifizierungsfehler hin. Firebase Cloud Messaging (FCM) authentifiziert sich mit einigen wichtigen Daten: senderID und FCM-API-Schlüssel. Beide sollten auf Richtigkeit überprüft werden. Weitere Informationen finden Sie in der [Android-Dokumentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) zu diesem Thema.

Häufige Fehlerursachen können sein:
- Falsche [senderID]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android)
- Mehrfachregistrierung, wenn sich Nutzer:innen bei einem anderen Push-Dienst mit einer anderen senderID Registrierung or registrieren

### Push-Bounce: InvalidRegistration {#push-bounced-invalidregistration}
`InvalidRegistration` kann auftreten, wenn ein Push-Token / Textbaustein fehlerhaft ist. Häufige Fehlerursachen können sein:
- Nutzer:innen übergeben Braze-Registrierungstoken manuell, rufen aber nicht `getToken()` auf. Zum Beispiel übergeben sie möglicherweise die gesamte Instanz-ID. Das Token / Textbaustein in der Fehlermeldung sieht dann wie folgt aus: `&#124;ID&#124;1&#124;:[regular token]`.
- Nutzer:innen Registrierung or registrieren sich bei mehreren Diensten. Derzeit erwarten wir, dass Push-Registrierungs-Intents im alten Stil eintreffen. Wenn sich Nutzer:innen also an mehreren Stellen Registrierung or registrieren und wir Intents von anderen Diensten abfangen, können fehlerhafte Push-Token / Textbaustein entstehen.

### Push-Bounce: NotRegistered {#notregistered}

`NotRegistered` bedeutet in der Regel, dass die App vom Gerät gelöscht wurde (z. B. unser Signal für eine Deinstallation). Dies kann auch auftreten, wenn eine Mehrfachregistrierung stattfindet und eine zweite Registrierung das Push-Token / Textbaustein ungültig macht, das Braze erhalten hat.

### DEVICE_UNREGISTERED {#device-unregistered}

Dieser Fehler erscheint im Nachrichten-Aktivitätsprotokoll als: `Received 'Error: DEVICE_UNREGISTERED, ' sending to '[Token String]'`

Dies tritt typischerweise aus einem der folgenden Gründe auf:

- Die Nutzer:innen haben die App deinstalliert. Dies ist die häufigste Ursache. Wenn die App von einem Gerät entfernt wird, wird das Push-Token / Textbaustein ungültig.
- Die Push-Zugangsdaten wurden in der App aktualisiert. Wenn Ihr Team die FCM-Zugangsdaten oder Zertifikate geändert hat, die mit der App gebündelt sind, haben Nutzer:innen, die sich mit den vorherigen Zugangsdaten registriert haben, ungültige Token / Textbaustein, bis die App sie erneut registriert.
- Angepasste Logik meldet Nutzer:innen von Push ab. Dies ist selten, aber es ist technisch möglich, ein Gerät programmatisch über das [Firebase/Android-SDK or Software-Development-Kit](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#deleteToken()) von Push abzumelden.

{% alert note %}
Dieser Fehler bedeutet nicht, dass Push für die Nutzer:innen deaktiviert ist – nur, dass ein bestimmtes Token / Textbaustein aus ihrem Profil entfernt wurde. Dies ist häufig bei Nutzer:innen, die Funktionen testen und die App häufig installieren und deinstallieren. Um zu prüfen, ob die Nutzer:innen noch gültige Token / Textbaustein haben, gehen Sie zur **Nutzersuche** und überprüfen Sie den Abschnitt **Kontakteinstellungen** auf dem Tab **Engagement**.
{% endalert %}

### Angeforderte Entität wurde nicht gefunden {#requested-entity-was-not-found}

Dieser Fehler kann aus folgenden Gründen auftreten:

- Die Endnutzer:innen haben die App deinstalliert. Sie können deren Kundenprofil or Nutzerprofil überprüfen, um zu bestätigen, ob dies der Fall ist.
- Es liegt ein ungültiger Benachrichtigungskanal vor. Je nach Ihrer Integration können Geräte Push-Token / Textbaustein haben, die nur für bestimmte Benachrichtigungskanäle gültig sind. Beim Senden an einen ungültigen Kanal wird die Nachricht als Bounce zurückgewiesen.
- Die Payload-Größe ist zu groß.

Weitere Informationen finden Sie in [Googles Dokumentation](https://firebase.google.com/docs/cloud-messaging/manage-tokens#stale-and-expired-tokens) zu veralteten und abgelaufenen Registrierungstoken.

{% endtab %}
{% tab iOS %}

### Fehler beim Senden von Push, da die Payload ungültig war {#error-sending-push-because-the-payload-was-invalid}

Diese Nachricht kann im Kundenprofil or Nutzerprofil auf dem Tab **Engagement** unter **Kontakteinstellungen** > **Push-Changelog** erscheinen, wenn der Apple Push Notification Service (APNs) die Push-Anfrage aufgrund einer ungültigen Payload ablehnt.

In Braze kann diese Dashboard-Nachricht einem der folgenden APNs-Fehlergründe zugeordnet werden:

- `PayloadEmpty`: Die Payload enthielt nicht die erforderlichen Inhalte für den Typ des gesendeten Push.
- `PayloadTooLarge`: Die Payload hat die maximale Payload-Größe von APNs überschritten.

Häufige Ursachen sind:

- Angepasste Schlüssel (und deren Werte), die die Payload zu groß machen (dies kann unerwartet große, durch Liquid gerenderte Werte umfassen).
- Ein leerer oder fehlender Alert oder Body, wo dieser erforderlich ist (oder eine anderweitig fehlerhafte `aps`-Payload).

Nächste Schritte:

- Reduzieren Sie die Payload-Größe, indem Sie angepasste Schlüssel kürzen und große dynamische Werte verkleinern.
- Wenn Sie über die API senden, validieren Sie die endgültige JSON-Payload (einschließlich Größe) vor dem Senden.

### Push-Bounce: BadToken {#push-bounced-badtoken}

Der `BadToken`-Fehler kann aus verschiedenen Gründen auftreten:
- Das Push-Token / Textbaustein wird nicht korrekt an Braze gesendet (z. B. in `registerDeviceToken:` oder dem Äquivalent Ihrer Plattform).
	- Überprüfen Sie das Token / Textbaustein im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log). Es sollte in der Regel wie ein langer String aus Buchstaben und Zahlen aussehen (z. B. `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Wenn nicht, überprüfen Sie den Code, der das Push-Token / Textbaustein an Braze sendet.<br><br>
- Nicht übereinstimmende Bereitstellungsumgebung:
	- Wenn Sie sich mit einem Entwicklungszertifikat Registrierung or registrieren und versuchen, mit einem Produktionszertifikat zu senden, kann dieser Fehler auftreten.
	- Braze unterstützt nur universelle Zertifikate für Produktionsumgebungen. Das Testen von Push in Entwicklungsumgebungen mit einem universellen Zertifikat funktioniert nicht.
	- Diese Meldung zeigt Bounces in der Produktion, aber nicht in der Entwicklung an.<br><br>
- Nicht übereinstimmendes Bereitstellungsprofil:
	- Dies kann passieren, wenn Ihr Zertifikat nicht mit dem übereinstimmt, das zum Abrufen des Tokens verwendet wurde. Wenn dies vermutet wird, umfassen die nächsten Schritte:
		- Stellen Sie sicher, dass das Push-Zertifikat, das zum Senden von Push über das Braze-Dashboard verwendet wird, und das Bereitstellungsprofil korrekt konfiguriert sind.
		- Erstellen Sie die APNS-Zertifizierung neu und erstellen Sie dann das Bereitstellungsprofil neu, nachdem das APNS-Zertifikat für die `app_id` konfiguriert wurde. Dies kann manchmal einige offensichtlichere Probleme lösen.

### Bundle-ID nicht zulässig {#bundle-id-not-allowed}

Der `TopicDisallowed`-Fehler bedeutet, dass APNs den Push abgelehnt hat, weil das Topic (Bundle-ID) in der Anfrage für die verwendeten Authentifizierungsdaten nicht zulässig ist. Um dies zu beheben:

1. **Überprüfen Sie die Bundle-ID.** Bestätigen Sie, dass die in Ihren Braze-App-Einstellungen konfigurierte Bundle-ID genau mit der Bundle-ID Ihrer App übereinstimmt. Dies schließt alle Suffix-Variationen ein (z. B. `.debug`, `.staging`).
2. **Überprüfen Sie Ihre APNs-Authentifizierungseinrichtung.** Bestätigen Sie, dass Ihre App mit dem richtigen APNs-`.p8`-Schlüssel konfiguriert ist und dass der Schlüssel mit demselben Apple Developer Team verknüpft ist wie die App, an die Sie senden.
3. **Bestätigen Sie die App-Umgebung.** Wenn Sie separate App-IDs in Braze für Entwicklungs- und Produktions-Builds haben, überprüfen Sie, ob jede mit den richtigen Push-Zugangsdaten und der richtigen Umgebung konfiguriert ist.

### Unregistered {#ios-unregistered}

Dieser Fehler erscheint im Nachrichten-Aktivitätsprotokoll als:

`Received 'Unregistered' sending to '[Token String]'`

Dies ist das iOS-Äquivalent des Android-Fehlers [DEVICE_UNREGISTERED](#device-unregistered). Er tritt typischerweise aus einem der folgenden Gründe auf:

- Die Nutzer:innen haben die App deinstalliert. Dies ist die häufigste Ursache.
- Push-Zertifikate wurden aktualisiert. Wenn Ihr Team die APNs-Zertifikate geändert oder erneuert hat, haben Nutzer:innen, die sich mit den vorherigen Zertifikaten registriert haben, möglicherweise ungültige Token / Textbaustein, bis die App sie erneut registriert.
- Angepasste Logik meldet Nutzer:innen von Push ab. Dies ist selten, aber es ist technisch möglich, sich programmatisch über das iOS-SDK or Software-Development-Kit von Remote-Benachrichtigungen abzumelden.

{% alert note %}
Dieser Fehler bedeutet nicht, dass Push für die Nutzer:innen deaktiviert ist – nur, dass ein bestimmtes Token / Textbaustein aus ihrem Profil entfernt wurde. Um zu prüfen, ob die Nutzer:innen noch gültige Token / Textbaustein haben, gehen Sie zur **Nutzersuche** und überprüfen Sie den Abschnitt **Kontakteinstellungen** auf dem Tab **Engagement**.
{% endalert %}

### InvalidProviderToken

Der `InvalidProviderToken`-Fehler bedeutet, dass APNs die Anfrage abgelehnt hat, weil das Authentifizierungstoken (von einem `.p8`-Schlüssel) oder das Push-Zertifikat (`.p12`) nicht mit der Bundle-ID oder Team-ID der App übereinstimmt. Um dies zu beheben:

1. **Überprüfen Sie Ihre Team-ID und Key-ID:** Wenn Sie einen `.p8`-Authentifizierungsschlüssel verwenden, bestätigen Sie, dass die im Braze-Dashboard konfigurierte **Team-ID** und **Key-ID** (**Einstellungen** > **App-Einstellungen** > wählen Sie Ihre iOS-App aus) mit den Werten in Ihrem Apple Developer Account übereinstimmen.
2. **Überprüfen Sie die Bundle-ID:** Stellen Sie sicher, dass die in Braze registrierte Bundle-ID mit der Bundle-ID Ihrer App übereinstimmt. Eine Abweichung, wie z. B. eine andere Groß-/Kleinschreibung oder ein `.debug`-Suffix, verursacht diesen Fehler.
3. **Laden Sie den Schlüssel oder das Zertifikat erneut hoch:** Wenn der `.p8`-Schlüssel oder das `.p12`-Zertifikat kürzlich neu generiert oder widerrufen wurde, laden Sie den neuen Schlüssel in Braze hoch und entfernen Sie den alten.
4. **Bestätigen Sie die APNs-Umgebung:** Wenn Sie ein `.p12`-Zertifikat verwenden, überprüfen Sie, ob Sie beim Hochladen die richtige Umgebung (Entwicklung versus Produktion) ausgewählt haben. Für `.p8`-Schlüssel wird dies automatisch gehandhabt.

### Push-Bounce: APNS-Feedback-Service hat entfernt {#push-bounced-apns-feedback-service-removed}

Dies passiert in der Regel, wenn jemand die App deinstalliert. Braze fragt den APNS-Feedback-Service jede Nacht ab, um eine Liste ungültiger Token / Textbaustein zu erhalten. Weitere Informationen finden Sie in Apples Dokumentation [Communicating with APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).

{% endtab %}
{% endtabs %}