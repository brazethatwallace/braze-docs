---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für Push
page_order: 5
page_type: reference
description: "Diagnostizieren Sie Probleme bei der Push-Zustellung, beim Klickverhalten und bei Zugangsdaten mithilfe eines Symptomindex und eines standardisierten Untersuchungspfads."
channel: push
---

# Fehlerbehebung für Push {#troubleshoot-push}

> Verwenden Sie diese Seite, um Probleme bei der Push-Zustellung, beim Klickverhalten und bei Zugangsdaten zu beheben. Informationen zur SDK or Software-Development-Kit-spezifischen Einrichtung finden Sie unter [Fehlerbehebung für Push-Benachrichtigungen im Braze SDK or Software-Development-Kit]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting). Fehlercodes finden Sie unter [Häufige Push-Fehlermeldungen]({{site.baseurl}}/user_guide/channels/push/push_error_codes).

## Hier starten: Symptom zuordnen {#start-here-match-your-symptom}

| Symptom | Gehe zu |
| --- | --- |
| Nutzer:in hat keine Push-Benachrichtigung erhalten | [Fehlende Push-Benachrichtigungen](#missing-push-notifications) |
| Push-Benachrichtigungen kommen verspätet an | [Verzögerte Push-Benachrichtigungen](#delayed-push-notifications) |
| Push-Versand ist langsamer als erwartet | [Push-Benachrichtigungen werden langsamer als erwartet gesendet](#push-notifications-are-sending-slower-than-expected) |
| `MismatchSenderID`-Fehler (Android) | [Fehler: MismatchSenderID](#error-mismatch-sender-id) |
| Tippen auf eine Push-Benachrichtigung öffnet die App nicht | [Klick auf eine Push-Benachrichtigung öffnet die App nicht](#clicking-a-push-notification-does-not-open-the-app) |
| Push-Links öffnen sich in der App statt im Browser | [Push-Klicks öffnen sich unerwartet in der App](#push-clicks-unexpectedly-open-in-app) |
| Probleme mit Web-Push-Berechtigungen oder -Zustellung | [Web-Push-Benachrichtigungen verhalten sich nicht wie erwartet](#web-push-notifications-are-not-behaving-as-expected) |
| Migration von `.p12` zu `.p8` erforderlich (iOS) | [Zu einem .p8-Authentifizierungsschlüssel migrieren](#migrate-to-a-p8-authentication-key) |
| Bestimmter Push-Fehlercode in den Protokollen | [Push-Fehlermeldungen](#push-error-messages) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push-Symptom" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow, wenn eine:r Nutzer:in oder ein Testgerät keine Push-Benachrichtigung erhalten hat. Beginnen Sie bei Schritt 1.

1. Bestätigen Sie, dass die:der Nutzer:in Push-abonniert oder opted-in ist und im Tab **Engagement** des Profils ein gültiges Push-Token / Textbaustein hat.
2. Bestätigen Sie, dass die:der Nutzer:in zum Sendezeitpunkt zur Zielgruppe der Campaign oder des Canvas gehört (Segmente werden in Echtzeit aktualisiert).
3. Prüfen Sie globales Frequency-Capping, Rate-Limits und Kontrollgruppen-Zuweisung für die Campaign oder den Canvas.
4. Bestätigen Sie, dass der korrekte Push-Typ für das Gerät verwendet wird (zum Beispiel Android, iOS oder Kindle).
5. Bestätigen Sie bei internen Tests, dass die Testperson in der richtigen App auf dem Gerät angemeldet ist.
6. Wenn die Zustellung weiterhin fehlschlägt, lesen Sie [Häufige Push-Fehlermeldungen]({{site.baseurl}}/user_guide/channels/push/push_error_codes) oder kontaktieren Sie den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) mit der Campaign- oder Canvas-ID, der Nutzer-ID und dem Zeitstempel mit Zeitzone.

## Fehlende Push-Benachrichtigungen {#missing-push-notifications}

**Symptom:** Ein:e Nutzer:in hat eine erwartete Push-Benachrichtigung nicht erhalten.

Wenn Push-Benachrichtigungen nicht wie erwartet ankommen, arbeiten Sie die folgenden Prüfungen durch:

- [Push-Abo-Status](#push-subscription-status)
- [Segment](#segment)
- [Obergrenzen für Push-Benachrichtigungen](#push-notification-caps)
- [Rate-Limits](#rate-limits)
- [Kontrollgruppen-Status](#control-group-status)
- [Gültiges Push-Token / Textbaustein](#valid-push-token)
- [Art der Push-Benachrichtigung](#push-notification-type)
- [Aktuelle App](#current-app)

### Push-Abo-Status {#push-subscription-status}

Push-Benachrichtigungen können nur an abonnierte oder angemeldete Nutzer:innen gesendet werden. Öffnen Sie im **Kundenprofil or Nutzerprofil** den Tab [Engagement]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) und bestätigen Sie, dass Sie aktiv für Push im Workspace registriert sind, den Sie testen. Wenn Sie für mehrere Apps registriert sind, werden diese unter **Push Registered For** aufgelistet:

![Für Push registriert]({% image_buster /assets/img_archive/trouble1.png %})

Sie können Nutzerprofile auch über die Braze-Export-Endpunkte exportieren:

- [Nutzer:innen nach Bezeichner]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Nutzer:innen nach Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Beide Endpunkte geben ein Push-Token / Textbaustein-Objekt zurück, das Informationen zur Push-Aktivierung pro Gerät enthält.

### Segment {#segment}

Bestätigen Sie, dass Sie in dem Segment sind, das Sie ansprechen (wenn es sich um eine Live-Campaign und nicht um einen Test handelt). Im **Kundenprofil or Nutzerprofil** können Sie sehen, welchen Segmenten die Nutzer:innen aktuell zugeordnet sind. Die Segmentzugehörigkeit wird in Echtzeit aktualisiert.

![Liste der Segmente]({% image_buster /assets/img_archive/trouble2.png %})

Sie können auch bestätigen, dass die Nutzer:innen Teil des Segments sind, indem Sie beim Erstellen eines Segments die **Nutzersuche** verwenden. Die **Nutzersuche** akzeptiert nur `external_id` oder `braze_id` – keine E-Mail-Adressen oder Telefonnummern. Um nach E-Mail, Telefon, Push-Token / Textbaustein oder Nutzer-Alias zu suchen, verwenden Sie [**Nutzer:innen suchen**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

![Abschnitt „Nutzersuche“ mit einem Suchfeld.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

### Obergrenzen für Push-Benachrichtigungen {#push-notification-caps}

Überprüfen Sie die globalen Frequency-Capping-Regeln. Möglicherweise haben Sie die Push-Benachrichtigung nicht erhalten, weil in Ihrem Workspace globales Frequency-Capping aktiv ist und Sie Ihre Obergrenze für Push-Benachrichtigungen im angegebenen Zeitraum bereits erreicht haben.

Prüfen Sie auf der **Analytics**-Seite der Campaign, ob ein Frequency-Capping-Banner angezeigt wird, das ungefähr angibt, wie viele Nutzer:innen die Campaign in den letzten 30 Tagen nicht erhalten haben. Um einzelne Sendungen zu untersuchen, verwenden Sie das [Messaging-Diagnostics-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) und filtern Sie nach **Frequency capped**. Um Regeln zu überprüfen oder zu ändern, lesen Sie [Globales Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#freq-cap-feat-over).

![Campaign-Details]({% image_buster /assets/img_archive/trouble3.png %})

### Rate-Limits {#rate-limits}

Wenn Sie ein Rate-Limit für Ihre Campaign oder Ihren Canvas festgelegt haben, kann es sein, dass Sie nach Überschreitung dieses Limits keine Nachrichten mehr erhalten. Weitere Informationen finden Sie unter [Rate-Limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting).

### Kontrollgruppen-Status {#control-group-status}

Wenn es sich um eine Einkanal-Campaign oder einen Canvas mit einer Kontrollgruppe handelt, befinden Sie sich möglicherweise in der Kontrollgruppe.

  1. Überprüfen Sie die [Variantenverteilung]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-4-choose-a-segment-and-distribute-your-users-across-variants), um festzustellen, ob es eine Kontrollgruppe gibt.
  2. Falls ja, erstellen Sie ein Segment, das nach [In Campaign-Kontrollgruppe]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#in-campaign-control-group) filtert, und [exportieren Sie das Segment]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#segment-csv-export-details), um zu prüfen, ob Ihre Nutzer-ID auf der Liste steht.

### Gültiges Push-Token / Textbaustein {#valid-push-token}

Ein Push-Token / Textbaustein ist ein Bezeichner, den Absender verwenden, um ein bestimmtes Gerät mit einer Push-Benachrichtigung anzusprechen. Ohne ein gültiges Push-Token / Textbaustein kann Braze keine Push-Benachrichtigung an dieses Gerät senden.

Braze speichert bis zu 20 Geräte pro Kundenprofil or Nutzerprofil. Wenn ein 21. Gerät registriert wird, wird das älteste Gerät entfernt (First-in-first-out, FIFO). Der Aufruf von [`changeUser()`]({{site.baseurl}}/developer_guide/analytics/setting_user_ids) im SDK or Software-Development-Kit registriert das aktuelle Gerät erneut im Profil.

### Art der Push-Benachrichtigung {#push-notification-type}

Verwenden Sie die Push-Art, die zum Gerät oder zur Plattform passt, die Sie ansprechen. Verwenden Sie beispielsweise eine Kindle-Push-Benachrichtigung für Fire TV, nicht eine Android-Push-Campaign. Für Android-Geräte verwenden Sie eine Android-Push-Benachrichtigung anstelle einer iOS-Push-Campaign.

Plattformspezifische Workflows zur Fehlerbehebung finden Sie unter:

- [Fehlerbehebung für Apple-Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Fehlerbehebung für Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

### Aktuelle App {#current-app}

Wenn Sie Push mit internen Nutzer:innen testen, bestätigen Sie, dass die vorgesehenen Empfänger:innen in der richtigen App angemeldet sind. Andernfalls erhalten sie möglicherweise die Push-Benachrichtigung nicht oder eine unerwartete Benachrichtigung basierend auf der Segmentierung.

{% alert note %}
Wenn Sie Push-Nachrichten mit Bildern auf Android senden, kann FCM das Bild manchmal verwerfen und nur den Text in der Push-Nachricht anzeigen. Dieses Problem wird in der Regel durch Probleme mit der Serververbindung verursacht.
{% endalert %}

## Fehler: MismatchSenderID {#error-mismatch-sender-id}

**Symptom:** Android-Push schlägt mit einem `MismatchSenderID`-Fehler fehl.

MismatchSenderID weist auf einen Authentifizierungsfehler bei Firebase Cloud Messaging (FCM) hin. Überprüfen Sie, ob Ihre Firebase-Sender-ID und Ihr FCM-API-Schlüssel korrekt sind.

So finden und ersetzen Sie den richtigen Firebase-Server-Key:

1. Öffnen Sie die Firebase-Konsole für Ihre App.
2. Wählen Sie unter **Projektübersicht** die Option **Projekteinstellungen** aus.
3. Überprüfen Sie auf dem Tab **Cloud Messaging**, ob die bei den API-Schlüsseln aufgeführte Sender-ID mit der in Braze übereinstimmt (unter **Einstellungen** > **App-Einstellungen** > **Cloud Messaging API Key**).

{% alert warning %}
Ändern Sie Ihre Sender-ID nicht im Braze-Dashboard. Dadurch werden bestehende Push-Registrierungen ungültig. Wenn die Sender-ID nicht übereinstimmt, müssen Sie Ihr Firebase-Projekt mit der passenden Sender-ID finden.
{% endalert %}

4. Kopieren Sie den **Server Key** unter **Project credentials**.
5. Gehen Sie in Braze zu **Einstellungen** > **App-Einstellungen**, wählen Sie Ihre App aus und fügen Sie den Server-Key in das Feld **Cloud Messaging API Key** ein (wobei der veraltete Schlüssel ersetzt wird).
6. Wählen Sie **Speichern**.
7. Senden Sie zur Überprüfung vor und nach der Änderung des API-Schlüssels eine Test-Push-Benachrichtigung an ein Gerät, ohne die Anwendung zu öffnen. So können Sie bestätigen, dass Nutzer:innen weiterhin Push-Benachrichtigungen erhalten, ohne dass eine neue Push-Registrierungs-ID (Push-Token / Textbaustein) generiert werden muss.

## Szenarien zur Fehlerbehebung {#troubleshooting-scenarios}

### Verzögerte Push-Benachrichtigungen {#delayed-push-notifications}

**Symptom:** Push-Benachrichtigungen kommen später als erwartet an.

Ihre Push-Benachrichtigungen können aus folgenden Gründen verzögert werden:

- Eine schwache Datenverbindung auf dem Gerät
- Benutzerdefinierter Code in der App, der Braze-Push-Benachrichtigungen unterdrücken kann
- Nutzer:innen-Einstellungen für Push-Benachrichtigungen in den Geräteeinstellungen
- Die Nachrichtenpriorität der Push-Benachrichtigung bei der Erstellung in der Campaign oder im Canvas
- Verkehrsverzögerungen oder Probleme mit den Push-Dienstanbietern (FCM und APNs)

### Push-Benachrichtigungen werden langsamer als erwartet gesendet {#push-notifications-are-sending-slower-than-expected}

**Symptom:** Campaign- oder Canvas-Push-Sendungen dauern länger als erwartet.

Stellen Sie sicher, dass Ihre Push-Benachrichtigungs-Einrichtung den folgenden Best Practices entspricht:

- Wenn Sie an große Zielgruppen senden, ohne den Push-Aktivierungsstatus zu berücksichtigen, kann dies zu einer langsameren Sendegeschwindigkeit führen. Erwägen Sie stattdessen, nur an Push-aktivierte Nutzer:innen zu senden, um die Größe Ihrer Zielgruppe zu reduzieren.
- Planen Sie Ihre Campaigns nach Möglichkeit im Voraus, anstatt sie sofort zu senden.
- Wenn Sie eine größere Anzahl von Nutzer:innen mit Push-Benachrichtigungen in einem Canvas ansprechen, können Sie davon ausgehen, dass nachfolgende Nachrichtenschritte im Canvas andere Verarbeitungszeiten erfordern als eine Campaign, die sofort an Nutzer:innen sendet. In diesem Fall würden Campaigns in der Regel vor einem Canvas fertig senden, da der erste „Schritt“ eines Canvas darin besteht, zu prüfen, ob Nutzer:innen für die jeweilige User Journey qualifiziert sind.

## Tippen auf eine Push-Benachrichtigung öffnet die App nicht {#clicking-a-push-notification-does-not-open-the-app}

**Symptom:** Das Tippen auf eine Push-Benachrichtigung öffnet die App nicht oder navigiert nicht wie konfiguriert.

Wenn das Tippen auf eine Push-Benachrichtigung Ihre App nicht öffnet, überprüfen Sie Folgendes je nach Plattform.

### Android

1. **Klickverhalten überprüfen:** Bestätigen Sie, dass die Campaign so konfiguriert ist, dass die App beim Klicken geöffnet wird.
2. **Deeplink-Verarbeitung prüfen:** Überprüfen Sie in Ihrer `braze.xml`-Datei, ob `com_braze_handle_push_deep_links_automatically` auf `true` oder `false` gesetzt ist.
   - Wenn auf `true` gesetzt, verarbeitet das Braze SDK or Software-Development-Kit Deeplinks direkt und die App sollte wie erwartet geöffnet werden.
   - Wenn auf `false` gesetzt, benötigt Ihre App einen Broadcast-Receiver, der Push-Empfangs- und Push-Öffnungs-Intents abhört und verarbeitet. Stellen Sie sicher, dass dieser Receiver korrekt implementiert ist.
3. **Ausführliche Logs erfassen:** [Aktivieren Sie die ausführliche Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduzieren Sie das Problem und stellen Sie die Logs zusammen mit Ihrer `braze.xml` und `AndroidManifest.xml` dem Braze-Support zur Verfügung.

### iOS

1. **Klickverhalten überprüfen:** Bestätigen Sie, dass die Campaign so konfiguriert ist, dass die App beim Klicken geöffnet wird.
2. **Push-Integration prüfen:** Deeplinking von einer Push-Benachrichtigung in die App wird automatisch durch die [Standard-Push-Integration]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift) von Braze verarbeitet. Bestätigen Sie, dass die Integration korrekt implementiert ist, einschließlich einer eventuellen benutzerdefinierten Delegate-Verarbeitung.
3. **Ausführliche Logs erfassen:** [Aktivieren Sie die ausführliche Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduzieren Sie das Problem und stellen Sie die Logs dem Braze-Support zur Verfügung.

## Push-Klicks öffnen unerwartet in der App {#push-clicks-unexpectedly-open-in-app}

**Symptom:** Links in Push-Benachrichtigungen öffnen sich innerhalb der App statt im Webbrowser des Geräts.

Wenn Links in Push-Benachrichtigungen unerwartet in Ihrer App statt in Ihrem Webbrowser geöffnet werden, liegt möglicherweise ein Problem mit Ihrer Campaign-Konfiguration oder SDK or Software-Development-Kit-Implementierung vor. Folgen Sie diesen Schritten zur Hilfe.

### Klickverhalten überprüfen {#verify-on-click-behavior}

Überprüfen Sie in Ihrer Campaign oder Ihrem Canvas-Schritt, ob **Open web URL inside mobile app** nicht ausgewählt ist. Falls doch, deaktivieren Sie die Auswahl und starten Sie erneut.

Die Standardinteraktion für das Klickverhalten „Open web URL“ unterscheidet sich je nach SDK or Software-Development-Kit-Version. Für SDK or Software-Development-Kit-Versionen iOS 2.29.0 und Android 2.0.0 und höher ist diese Option standardmäßig ausgewählt und Web-URLs werden in einer Webansicht innerhalb der App geöffnet. Vor diesen Versionen ist diese Option standardmäßig deaktiviert und Web-URLs werden im Standard-Webbrowser des Geräts geöffnet.

Wenn dies nicht das Problem ist, liegt möglicherweise ein Problem mit Ihrer Push-Implementierung vor.

### Push-Integration erneut prüfen {#double-check-push-integration}

Wenn Links in Ihren Push-Benachrichtigungen unerwartet in der App geöffnet werden, kann dies an Problemen mit Ihrer Push-Benachrichtigungs-Integration oder Anpassungseinstellungen liegen. Folgen Sie diesen Schritten zur Fehlerbehebung:

1. **Push-Delegate-Implementierung überprüfen:** Stellen Sie sicher, dass der Braze-Push-Delegate korrekt implementiert ist. Detaillierte Anweisungen finden Sie im Integrationsleitfaden für Push-Benachrichtigungen für Ihre [Plattform]({{site.baseurl}}/developer_guide/home).
2. **Angepasste Link-Behandlung prüfen:** Überprüfen Sie, ob die App eine angepasste Behandlung für alle `https://`-Links enthält. Angepasste Konfigurationen können Standardverhalten überschreiben. Arbeiten Sie mit Ihrem Entwicklungsteam zusammen, um diese Einstellungen bei Bedarf zu überprüfen und anzupassen.
3. **iOS-Push-Registrierung überprüfen:** Für iOS lesen Sie Schritt 1 des Push-Integrationsleitfadens zur [Registrierung von Push-Benachrichtigungen bei APNs]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift) erneut. Stellen Sie sicher, dass Ihr Delegate-Objekt synchron zugewiesen wird, bevor die App den Start abschließt. Dieser Schritt sollte in der Methode `application:didFinishLaunchingWithOptions:` abgeschlossen werden.
4. **Integration testen:** Testen Sie nach den Anpassungen das Push-Benachrichtigungsverhalten sowohl auf iOS- als auch auf Android-Geräten, um zu bestätigen, dass das Problem behoben ist.

### Deeplinks bei im Hintergrund laufender App (iOS) {#deep-links-with-app-still-running-in-the-background-ios}

Wenn Deeplinks funktionieren, wenn die App nicht läuft oder wenn der Link direkt verwendet wird, aber nicht, wenn die Anwendung bereits im Hintergrund läuft, hängt das Problem möglicherweise damit zusammen, wie die App den Link verarbeitet. Überprüfen Sie, ob Sie Drittanbieter-Bibliotheken verwenden, die Method-Swizzling nutzen. Wir empfehlen, Swizzling zu deaktivieren, da es Probleme mit Deeplink-Implementierungen verursachen kann.

## Zu einem .p8-Authentifizierungsschlüssel migrieren {#migrate-to-a-p8-authentication-key}

**Symptom:** Sie müssen iOS-Push-Zugangsdaten von einem älteren Zertifikat zu einem `.p8`-Schlüssel migrieren, oder die Push-Zustellung ist nach einer Änderung der Zugangsdaten fehlgeschlagen.

Apple `.p8`-Authentifizierungsschlüssel sind der erforderliche Ansatz für APNs-Push in Braze. Im Gegensatz zu älteren Zertifikatsdateitypen laufen `.p8`-Schlüssel nicht ab und unterstützen alle Ihre Apps unter einem einzigen Schlüssel, wodurch jährliche Zertifikatserneuerungen entfallen und das Risiko von Push-Zustellungsfehlern reduziert wird.

Wenn Sie derzeit ein `.p12`- oder `.pem`-Zertifikat verwenden, migrieren Sie so bald wie möglich zu einem `.p8`-Schlüssel. Anweisungen zum Erstellen und Hochladen eines `.p8`-Schlüssels finden Sie unter [APNs-Push-Zertifikat hochladen]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift). Apples Anleitung zum Generieren eines `.p8`-Schlüssels aus Ihrem Entwicklerkonto finden Sie unter [Mit APNs über Authentifizierungstoken kommunizieren](https://developer.apple.com/help/account/capabilities/communicate-with-apns-using-authentication-tokens/).

### .p8-Schlüssel im Vergleich zu .p12-Zertifikaten {#p8-keys-versus-p12-certificates}

Verwenden Sie die folgende Tabelle, um Zugangsdatentypen, Ablauf und Dashboard-Anzeige zu vergleichen.

| Zugangsdaten | Ablauf | Dashboard-Statusanzeige |
| --- | --- | --- |
| `.p8`-Authentifizierungsschlüssel | Läuft nicht ab | Keine grüne Statusanzeige (dies ist erwartet) |
| `.p12`-Push-Zertifikat | Läuft jährlich ab | Grüne Anzeige, wenn das Zertifikat gültig ist |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label=".p8-Schlüssel im Vergleich zu .p12-Zertifikaten" }

Wenn Sie ein `.p12`-Zertifikat durch einen `.p8`-Schlüssel ersetzen (oder neue Zugangsdaten hochladen), kann die Push-Zustellung kurzzeitig pausieren, während Braze die Änderung verarbeitet. Planen Sie Updates nach Möglichkeit während eines Wartungsfensters.

Bestätigen Sie unter **Einstellungen** > **App-Einstellungen** > **Push-Benachrichtigungseinstellungen**, dass **App Bundle ID**, **Team ID** und **Key ID** (für `.p8`-Schlüssel) mit den Werten in Ihrem Apple-Entwicklerkonto übereinstimmen. Mehrere Braze-Workspaces können dieselben Apple-Push-Zugangsdaten verwenden, wenn die iOS-App-**Bundle-ID** identisch ist; die Zugangsdaten-Umgebung (Entwicklung versus Produktion) muss mit der Art übereinstimmen, wie die App erstellt wurde.

Apps mit [Braze Swift SDK or Software-Development-Kit 10.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.0.0) oder höher können [Dynamisches APNs-Gateway-Management]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift#dynamic-apns-gateway-management) verwenden, das Token / Textbaustein automatisch an die richtige APNs-Umgebung weiterleitet.

## Web-Push-Benachrichtigungen verhalten sich nicht wie erwartet {#web-push-notifications-are-not-behaving-as-expected}

**Symptom:** Browser-Push-Benachrichtigungen werden nicht angezeigt oder die Website-Berechtigungen scheinen festzuhängen.

Wenn Sie Probleme mit Push-Benachrichtigungen in Ihrem Browser haben, müssen Sie möglicherweise die Benachrichtigungsberechtigungen Ihrer Website zurücksetzen und den Speicher Ihrer Website löschen. Verwenden Sie die folgenden Schritte als Hilfe.

{% tabs %}
{% tab Chrome %}

### Chrome auf dem Desktop zurücksetzen {#reset-chrome-on-desktop}

1. Wählen Sie neben Ihrer URL im Chrome-Browser das Schieberegler-Symbol **Website-Informationen anzeigen** aus.
2. Wählen Sie unter **Benachrichtigungen** die Option **Berechtigung zurücksetzen** aus.
3. Öffnen Sie die Chrome DevTools. Die folgenden Tastenkombinationen gelten je nach Betriebssystem.

<style>
table {
    max-width: 50%;
}
</style>

| Betriebssystem | Tastenkombinationen |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chrome auf dem Desktop zurücksetzen" }

{:start="4"}
4. Navigieren Sie in den DevTools zum Tab **Application**.
5. Wählen Sie in der Seitenleiste **Storage** aus.
6. Wählen Sie **Clear site data** aus.
7. Chrome fordert Sie auf, die Seite neu zu laden, um Ihre aktualisierten Einstellungen anzuwenden. Wählen Sie **Reload** aus.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab zu Ihrer Website und probieren Sie es aus.

### Chrome auf Android zurücksetzen {#reset-chrome-on-android}

Wenn eine Benachrichtigung von Ihrer Website in Ihrer Android-Benachrichtigungsleiste sichtbar ist:

1. Wählen Sie in der Push-Benachrichtigung <i class="fas fa-cog" title="Einstellungen"></i> **Einstellungen** und dann **Website-Einstellungen** aus.
2. Tippen Sie unter **Website-Einstellungen** auf **Löschen und zurücksetzen**.

Wenn Sie keine Benachrichtigung von Ihrer Website geöffnet haben:

1. Öffnen Sie Chrome auf Android.
2. Tippen Sie auf das <i class="fas fa-ellipsis-vertical"></i>-Menü.
3. Gehen Sie zu **Einstellungen** > **Website-Einstellungen** > **Benachrichtigungen**.
4. Überprüfen Sie, ob Benachrichtigungen auf **Vor dem Senden fragen (empfohlen)** eingestellt sind.
5. Suchen Sie Ihre Website in der Liste.
6. Wählen Sie den Eintrag aus und tippen Sie auf **Löschen und zurücksetzen**.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab zu Ihrer Website und probieren Sie es aus.

{% endtab %}
{% tab Firefox %}

### Firefox auf dem Desktop zurücksetzen {#reset-firefox-on-desktop}

1. Wählen Sie neben Ihrer Website-URL <i class="fa-solid fa-circle-info" alt="Info-Symbol"></i> oder <i class="fas fa-lock" alt="Schloss-Symbol"></i> aus.
2. Wählen Sie unter **Berechtigungen** neben **Benachrichtigungen empfangen** die Option <i class="fa-solid fa-circle-xmark" title="Diese Berechtigung löschen und erneut fragen"></i> **Berechtigung löschen** aus, um die Benachrichtigungsberechtigungen zu löschen.
3. Wählen Sie im selben Menü **Cookies und Website-Daten löschen** aus.
4. Wählen Sie im Bestätigungsdialog **OK** aus.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab zu Ihrer Website und probieren Sie es aus.

### Firefox auf Android zurücksetzen {#reset-firefox-on-android}

Um Push-Berechtigungen auf Android zurückzusetzen, lesen Sie [Browserverlauf und andere persönliche Daten löschen](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser) im Mozilla-Support.

{% endtab %}
{% tab Safari %}

### Safari auf macOS zurücksetzen {#reset-safari-on-macos}

{% alert note %}
Diese Schritte gelten nur für macOS, da Apple Web-Push für Safari unter Windows nicht unterstützt.
{% endalert %}

1. Öffnen Sie Safari.
2. Gehen Sie über die [Menüleiste auf dem Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac) zu **Safari** > **Einstellungen** > **Websites** > **Benachrichtigungen**.
3. Wählen Sie Ihre Website aus der Liste aus.
4. Wählen Sie **Entfernen** aus, um die Benachrichtigungsberechtigungen für die Website zu löschen.
5. Gehen Sie dann zu **Datenschutz** > **Websitedaten verwalten**.
6. Wählen Sie Ihre Website aus der Liste aus.
7. Wählen Sie **Entfernen** aus, oder um alle Website-Daten zu entfernen, wählen Sie **Alle entfernen** aus.
8. Wählen Sie **Fertig** aus.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab zu Ihrer Website und probieren Sie es aus.

{% endtab %}
{% endtabs %}

## Push-Öffnungsmetriken {#push-open-metrics}

Braze protokolliert eine direkte Öffnung, wenn Nutzer:innen auf die Benachrichtigung tippen und Ihre App eine Sitzung startet. Das Erweitern einer Rich-Push-Benachrichtigung ohne die App zu öffnen protokolliert keine direkte Öffnung.

Wenn Nutzer:innen Ihre App nach dem Empfang einer Push-Benachrichtigung öffnen, ohne auf die Benachrichtigung zu tippen, kann Braze stattdessen eine beeinflusste Öffnung protokollieren. Definitionen und Berichte finden Sie unter [Beeinflusste Öffnungen]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

## Push-Fehlermeldungen {#push-error-messages}

**Symptom:** Sie sehen einen bestimmten Push-Fehlercode (zum Beispiel `DEVICE_UNREGISTERED`, `Unregistered` oder `NotRegistered`).

Definitionen häufiger Push-Fehlercodes (einschließlich `DEVICE_UNREGISTERED`, `NotRegistered` und `Unregistered`) finden Sie unter [Häufige Push-Fehlermeldungen]({{site.baseurl}}/user_guide/channels/push/push_error_codes).

Wenn FCM Fehler wie `DEVICE_UNREGISTERED` oder `NotRegistered` zurückgibt, entfernt Braze in der Regel das betroffene Push-Token / Textbaustein aus dem Kundenprofil or Nutzerprofil. Diese Entfernung weist häufig darauf hin, dass die App deinstalliert wurde oder das Token / Textbaustein nicht mehr gültig ist. Uninstall-Tracking-Campaigns verwenden dieselbe Token / Textbaustein-Entfernungslogik im großen Maßstab.