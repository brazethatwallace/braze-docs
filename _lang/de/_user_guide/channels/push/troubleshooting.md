---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für Push
page_order: 5
page_type: reference
description: "Schritte zur Fehlerbehebung bei Problemen mit dem Push-Messaging-Kanal."
channel: push
---

# Fehlerbehebung für Push {#troubleshoot-push}

> Verwenden Sie diese Seite, um Probleme mit dem Push-Messaging-Kanal zu beheben.

## Fehlende Push-Benachrichtigungen {#missing-push-notifications}

Wenn Push-Benachrichtigungen nicht wie erwartet ankommen, arbeiten Sie die folgenden Prüfungen durch:

- [Push-Abo-Status](#push-subscription-status)
- [Segment](#segment)
- [Obergrenzen für Push-Benachrichtigungen](#push-notification-caps)
- [Rate-Limits](#rate-limits)
- [Kontrollgruppen-Status](#control-group-status)
- [Gültiges Push-Token](#valid-push-token)
- [Art der Push-Benachrichtigung](#push-notification-type)
- [Aktuelle App](#current-app)

### Push-Abo-Status {#push-subscription-status}

Push-Benachrichtigungen können nur an abonnierte oder angemeldete Nutzer:innen gesendet werden. Öffnen Sie im **Nutzerprofil** den Tab [Engagement]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) und bestätigen Sie, dass Sie aktiv für Push im Workspace registriert sind, den Sie testen. Wenn Sie für mehrere Apps registriert sind, werden diese unter **Push Registered For** aufgelistet:

![Für Push registriert]({% image_buster /assets/img_archive/trouble1.png %})

Sie können Nutzerprofile auch über die Braze-Export-Endpunkte exportieren:

- [Nutzer:innen nach Bezeichner]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Nutzer:innen nach Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Beide Endpunkte geben ein Push-Token-Objekt zurück, das Informationen zur Push-Aktivierung pro Gerät enthält.

### Segment {#segment}

Bestätigen Sie, dass Sie in dem Segment sind, das Sie ansprechen (wenn es sich um eine Live-Campaign und nicht um einen Test handelt). Im **Nutzerprofil** können Sie sehen, welchen Segmenten die Nutzer:innen aktuell zugeordnet sind. Die Segmentzugehörigkeit wird in Echtzeit aktualisiert.

![Liste der Segmente]({% image_buster /assets/img_archive/trouble2.png %})

Sie können auch bestätigen, dass die Nutzer:innen Teil des Segments sind, indem Sie beim Erstellen eines Segments die **Nutzersuche** verwenden. Die **Nutzersuche** akzeptiert nur `external_id` oder `braze_id` – keine E-Mail-Adressen oder Telefonnummern. Um nach E-Mail, Telefon, Push-Token oder Nutzer-Alias zu suchen, verwenden Sie [**Nutzer:innen suchen**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

![Abschnitt „Nutzersuche“ mit einem Suchfeld.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

### Obergrenzen für Push-Benachrichtigungen {#push-notification-caps}

Wenn in Ihrem Workspace globales Frequency-Capping aktiv ist, haben Sie möglicherweise Ihre Obergrenze für den Zeitraum bereits erreicht und erhalten die Push-Benachrichtigung nicht. Prüfen Sie im Dashboard das [globale Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#freq-cap-feat-over) und Ihre Limits. Wenn die Campaign die Frequency-Capping-Regeln einhält, zeigen die Campaign-Details an, wie viele Nutzer:innen betroffen waren.

![Campaign-Details]({% image_buster /assets/img_archive/trouble3.png %})

### Rate-Limits {#rate-limits}

Wenn Sie ein Rate-Limit für Ihre Campaign oder Ihren Canvas festgelegt haben, kann es sein, dass Sie nach Überschreitung dieses Limits keine Nachrichten mehr erhalten. Weitere Informationen finden Sie unter [Rate-Limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#rate-limiting).

### Kontrollgruppen-Status {#control-group-status}

Wenn es sich um eine Einkanal-Campaign oder einen Canvas mit einer Kontrollgruppe handelt, befinden Sie sich möglicherweise in der Kontrollgruppe.

  1. Überprüfen Sie die [Variantenverteilung]({{site.baseurl}}/user_guide/messaging/ab_testing#step-5-distribute-users-among-your-variants), um festzustellen, ob es eine Kontrollgruppe gibt.
  2. Falls ja, erstellen Sie ein Segment, das nach [In Campaign-Kontrollgruppe]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#in-campaign-control-group-filter) filtert, und [exportieren Sie das Segment]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#exporting-to-csv), um zu prüfen, ob Ihre Nutzer-ID auf der Liste steht.

### Gültiges Push-Token {#valid-push-token}

Ein Push-Token ist ein Bezeichner, den Absender verwenden, um ein bestimmtes Gerät mit einer Push-Benachrichtigung anzusprechen. Ohne ein gültiges Push-Token kann Braze keine Push-Benachrichtigung an dieses Gerät senden.

Braze speichert bis zu 20 Geräte pro Nutzerprofil. Wenn ein 21. Gerät registriert wird, wird das älteste Gerät entfernt (First-in-first-out, FIFO). Der Aufruf von [`changeUser()`]({{site.baseurl}}/developer_guide/analytics/setting_user_ids) im SDK registriert das aktuelle Gerät erneut im Profil.

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

## Fehler: MismatchSenderID {#error-mismatchsenderid}

MismatchSenderID weist auf einen Authentifizierungsfehler bei Firebase Cloud Messaging (FCM) hin. Bestätigen Sie, dass Ihre Firebase-Sender-ID und Ihr FCM-API-Schlüssel korrekt sind.

So finden Sie den richtigen Firebase-Server-Key und ersetzen ihn:

1. Gehen Sie zur Firebase-Konsole für Ihre App.
2. Wählen Sie unter **Project Overview** die Option **Project Settings**.
3. Überprüfen Sie im Tab **Cloud Messaging**, ob die Sender-ID unter den API-Schlüsseln mit der in Braze übereinstimmt (unter **Settings** > **App Settings** > **Cloud Messaging API Key**).

{% alert warning %}
Ändern Sie Ihre Sender-ID nicht in Ihrem Braze-Dashboard. Dadurch werden bestehende Push-Registrierungen ungültig. Wenn die Sender-ID nicht übereinstimmt, müssen Sie Ihr Firebase-Projekt mit der passenden Sender-ID finden.
{% endalert %}

{:start="4"}
4. Kopieren Sie den **Server Key** unter **Project credentials**.
5. Gehen Sie in Braze zu **Settings** > **App Settings**, wählen Sie Ihre App aus und fügen Sie den Server-Key in das Feld **Cloud Messaging API Key** ein (und ersetzen Sie den veralteten Schlüssel).
6. Wählen Sie **Save**.
7. Senden Sie zur Überprüfung eine Test-Push-Benachrichtigung an ein Gerät, bevor und nachdem Sie den API-Schlüssel geändert haben, ohne die Anwendung zu öffnen. So wird bestätigt, dass Nutzer:innen weiterhin Push-Benachrichtigungen erhalten, ohne dass eine neue Push-Registrierungs-ID (Push-Token) generiert werden muss.

## Fehlerbehebungsszenarien {#troubleshooting-scenarios}

### Verzögerte Push-Benachrichtigungen {#delayed-push-notifications}

Ihre Push-Benachrichtigungen können aus folgenden Gründen verzögert werden:

- Eine schwache Datenverbindung auf dem Gerät
- Angepasster Code in der App, der Braze-Push-Benachrichtigungen unterdrücken kann
- Nutzereinstellungen für Push-Benachrichtigungen in den Geräteeinstellungen
- Nachrichtenpriorität der Push-Benachrichtigung bei der Erstellung in der Campaign oder im Canvas
- Verkehrsverzögerungen oder Probleme bei den Push-Dienstanbietern (FCM und APNs)

### Push-Benachrichtigungen werden langsamer als erwartet gesendet {#push-notifications-are-sending-slower-than-expected}

Stellen Sie sicher, dass Ihr Push-Benachrichtigungs-Setup diesen Best Practices folgt:

- Wenn Sie an große Zielgruppen senden, ohne den Push-Aktivierungsstatus zu berücksichtigen, kann dies zu einer langsameren Sendegeschwindigkeit führen. Erwägen Sie stattdessen, nur an Push-aktivierte Nutzer:innen zu senden, um die Größe Ihrer Zielgruppe zu reduzieren.
- Versuchen Sie nach Möglichkeit, Ihre Campaigns im Voraus zu planen, anstatt sie sofort zu senden.
- Wenn Sie eine größere Anzahl von Nutzer:innen mit Push-Benachrichtigungen in einem Canvas ansprechen, können Sie davon ausgehen, dass nachfolgende Nachrichtenschritte im Canvas andere Verarbeitungszeiten erfordern als eine Campaign, die sofort an Nutzer:innen sendet. In diesem Fall würden Campaigns in der Regel schneller fertig senden als ein Canvas, da der erste „Schritt“ eines Canvas darin besteht, zu prüfen, ob Nutzer:innen für die spezifische User-Journey qualifiziert sind.

## Tippen auf eine Push-Benachrichtigung öffnet die App nicht {#clicking-a-push-notification-doesnt-open-the-app}

Wenn das Tippen auf eine Push-Benachrichtigung Ihre App nicht öffnet, überprüfen Sie je nach Plattform Folgendes.

### Android

1. **Klickverhalten überprüfen:** Bestätigen Sie, dass die Campaign so konfiguriert ist, dass die App beim Klicken geöffnet wird.
2. **Deeplink-Behandlung prüfen:** Überprüfen Sie in Ihrer `braze.xml`-Datei, ob `com_braze_handle_push_deep_links_automatically` auf `true` oder `false` gesetzt ist.
   - Wenn auf `true` gesetzt, behandelt das Braze SDK Deeplinks direkt und die App sollte wie erwartet geöffnet werden.
   - Wenn auf `false` gesetzt, benötigt Ihre App einen Broadcast-Receiver, der Push-Empfangs- und Öffnungs-Intents abhört und verarbeitet. Überprüfen Sie, ob dieser Receiver korrekt implementiert ist.
3. **Ausführliche Logs erfassen:** [Aktivieren Sie ausführliches Logging]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduzieren Sie das Problem und stellen Sie die Logs zusammen mit Ihrer `braze.xml` und `AndroidManifest.xml` dem Braze-Support zur Verfügung.

### iOS

1. **Klickverhalten überprüfen:** Bestätigen Sie, dass die Campaign so konfiguriert ist, dass die App beim Klicken geöffnet wird.
2. **Push-Integration prüfen:** Deeplinking von einer Push-Benachrichtigung in die App wird automatisch durch die Braze [Standard-Push-Integration]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift) behandelt. Bestätigen Sie, dass die Integration korrekt implementiert ist, einschließlich aller angepassten Delegate-Behandlungen.
3. **Ausführliche Logs erfassen:** [Aktivieren Sie ausführliches Logging]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduzieren Sie das Problem und stellen Sie die Logs dem Braze-Support zur Verfügung.

## Push-Klicks öffnen unerwartet in der App {#push-clicks-unexpectedly-open-in-app}

Wenn Links in Push-Benachrichtigungen unerwartet in Ihrer App statt in Ihrem Webbrowser geöffnet werden, liegt möglicherweise ein Problem mit Ihrer Campaign-Konfiguration oder SDK-Implementierung vor. Folgen Sie diesen Schritten zur Hilfe.

### Klickverhalten überprüfen {#verify-on-click-behavior}

Überprüfen Sie in Ihrer Campaign oder Ihrem Canvas-Schritt, ob **Open web URL inside mobile app** nicht ausgewählt ist. Falls doch, deaktivieren Sie die Auswahl und starten Sie erneut.

![Feld „Klickverhalten“ bei der Konfiguration einer Push-Benachrichtigung, eingestellt auf „Open web URL“ mit deaktiviertem „Open web URL inside mobile app“.]({% image_buster /assets/img/push_on_click.png %})

Die Standardinteraktion für das Klickverhalten „Open web URL“ unterscheidet sich je nach SDK-Version. Für SDK-Versionen iOS 2.29.0 und Android 2.0.0 und höher ist diese Option standardmäßig ausgewählt und Web-URLs werden in einer Webansicht innerhalb der App geöffnet. Vor diesen Versionen ist diese Option standardmäßig deaktiviert und Web-URLs werden im Standard-Webbrowser des Geräts geöffnet.

Wenn dies nicht das Problem ist, liegt möglicherweise ein Problem mit Ihrer Push-Implementierung vor.

### Push-Integration erneut prüfen {#double-check-push-integration}

Wenn Links in Ihren Push-Benachrichtigungen unerwartet in der App geöffnet werden, kann dies an Problemen mit Ihrer Push-Benachrichtigungs-Integration oder Anpassungseinstellungen liegen. Folgen Sie diesen Schritten zur Fehlerbehebung:

1. **Push-Delegate-Implementierung überprüfen:** Stellen Sie sicher, dass der Braze-Push-Delegate korrekt implementiert ist. Detaillierte Anweisungen finden Sie im Integrationsleitfaden für Push-Benachrichtigungen für Ihre [Plattform]({{site.baseurl}}/developer_guide/home).
2. **Angepasste Link-Behandlung prüfen:** Überprüfen Sie, ob die App eine angepasste Behandlung für alle `https://`-Links enthält. Angepasste Konfigurationen können Standardverhalten überschreiben. Arbeiten Sie mit Ihrem Entwicklungsteam zusammen, um diese Einstellungen bei Bedarf zu überprüfen und anzupassen.
3. **iOS-Push-Registrierung überprüfen:** Für iOS lesen Sie Schritt 1 des Push-Integrationsleitfadens zur [Registrierung von Push-Benachrichtigungen bei APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-register-for-push-notifications-with-apns) erneut. Stellen Sie sicher, dass Ihr Delegate-Objekt synchron zugewiesen wird, bevor die App den Start abschließt. Dieser Schritt sollte in der Methode `application:didFinishLaunchingWithOptions:` abgeschlossen werden.
4. **Integration testen:** Testen Sie nach den Anpassungen das Push-Benachrichtigungsverhalten sowohl auf iOS- als auch auf Android-Geräten, um zu bestätigen, dass das Problem behoben ist.

### Deeplinks bei im Hintergrund laufender App (iOS) {#deep-links-with-app-still-running-in-the-background-ios}

Wenn Deeplinks funktionieren, wenn die App nicht läuft oder wenn der Link direkt verwendet wird, aber nicht, wenn die Anwendung bereits im Hintergrund läuft, hängt das Problem möglicherweise damit zusammen, wie die App den Link verarbeitet. Überprüfen Sie, ob Sie Drittanbieter-Bibliotheken verwenden, die Method-Swizzling nutzen. Wir empfehlen, Swizzling zu deaktivieren, da es Probleme mit Deeplink-Implementierungen verursachen kann.

## Zu einem .p8-Authentifizierungsschlüssel migrieren {#migrate-to-a-p8-authentication-key}

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

Bestätigen Sie unter **Settings** > **App Settings** > **Push Notification Settings**, dass **App Bundle ID**, **Team ID** und **Key ID** (für `.p8`-Schlüssel) mit den Werten in Ihrem Apple-Entwicklerkonto übereinstimmen. Mehrere Braze-Workspaces können dieselben Apple-Push-Zugangsdaten verwenden, wenn die iOS-App-**Bundle-ID** identisch ist; die Zugangsdaten-Umgebung (Entwicklung versus Produktion) muss mit der Art übereinstimmen, wie die App erstellt wurde.

Apps mit [Braze Swift SDK 10.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.0.0) oder höher können [Dynamic APNs gateway management]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift#dynamic-apns-gateway-management) verwenden, das Token automatisch an die richtige APNs-Umgebung weiterleitet.

## Web-Push-Benachrichtigungen verhalten sich nicht wie erwartet {#web-push-notifications-arent-behaving-as-expected}

Wenn Sie Probleme mit Push-Benachrichtigungen in Ihrem Browser haben, müssen Sie möglicherweise die Benachrichtigungsberechtigungen Ihrer Website zurücksetzen und den Speicher Ihrer Website löschen. Folgen Sie diesen Schritten zur Hilfe.

{% tabs %}
{% tab Chrome %}

### Chrome auf dem Desktop zurücksetzen {#reset-chrome-on-desktop}

1. Wählen Sie neben Ihrer URL im Chrome-Browser das Schieberegler-Symbol **View Site Information** aus.
2. Wählen Sie unter **Notifications** die Option **Reset permission**.
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
6. Wählen Sie **Clear site data**.
7. Chrome fordert Sie auf, die Seite neu zu laden, um Ihre aktualisierten Einstellungen anzuwenden. Wählen Sie **Reload**.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab zu Ihrer Website und probieren Sie es aus.

### Chrome auf Android zurücksetzen {#reset-chrome-on-android}

Wenn Sie eine Benachrichtigung von Ihrer Website in Ihrer Android-Benachrichtigungsleiste sehen:

1. Tippen Sie in der Push-Benachrichtigung auf <i class="fas fa-cog" title="Einstellungen"></i> **Einstellungen** und wählen Sie **Site settings**.
2. Tippen Sie unter **Site settings** auf **Clear & Reset**.

Wenn Sie keine Benachrichtigung von Ihrer Website geöffnet haben:

1. Öffnen Sie Chrome auf Android.
2. Tippen Sie auf das Menü <i class="fas fa-ellipsis-vertical"></i>.
3. Gehen Sie zu **Settings** > **Site Settings** > **Notifications**.
4. Überprüfen Sie, ob Benachrichtigungen auf **Ask before sending (recommended)** eingestellt sind.
5. Suchen Sie Ihre Website in der Liste.
6. Wählen Sie den Eintrag aus und tippen Sie auf **Clear and Reset**.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab zu Ihrer Website und probieren Sie es aus.

{% endtab %}
{% tab Firefox %}

### Firefox auf dem Desktop zurücksetzen {#reset-firefox-on-desktop}

1. Wählen Sie neben Ihrer Website-URL <i class="fa-solid fa-circle-info" alt="Info-Symbol"></i> oder <i class="fas fa-lock" alt="Schloss-Symbol"></i> aus.
2. Wählen Sie unter **Permissions** neben **Receive Notifications** das Symbol <i class="fa-solid fa-circle-xmark" title="Diese Berechtigung löschen und erneut fragen"></i> **Berechtigung löschen**, um die Benachrichtigungsberechtigungen zu löschen.
3. Wählen Sie im selben Menü **Clear Cookies and Site Data**.
4. Wählen Sie im Bestätigungsdialog **OK**.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab zu Ihrer Website und probieren Sie es aus.

### Firefox auf Android zurücksetzen {#reset-firefox-on-android}

Um Push-Berechtigungen auf Android zurückzusetzen, lesen Sie [Ihren Browserverlauf und andere persönliche Daten löschen](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser) im Mozilla-Support.

{% endtab %}
{% tab Safari %}

### Safari auf macOS zurücksetzen {#reset-safari-on-macos}

{% alert note %}
Diese Schritte gelten nur für macOS, da Apple Web-Push für Safari unter Windows nicht unterstützt.
{% endalert %}

1. Öffnen Sie Safari.
2. Gehen Sie in der [Menüleiste auf dem Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac) zu **Safari** > **Settings** > **Websites** > **Notifications**.
3. Wählen Sie Ihre Website aus der Liste aus.
4. Wählen Sie **Remove**, um die Benachrichtigungsberechtigungen für die Website zu löschen.
5. Gehen Sie dann zu **Privacy** > **Manage Website Data**.
6. Wählen Sie Ihre Website aus der Liste aus.
7. Wählen Sie **Remove** oder, um alle Website-Daten zu entfernen, wählen Sie **Remove All**.
8. Wählen Sie **Done**.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab zu Ihrer Website und probieren Sie es aus.

{% endtab %}
{% endtabs %}

## Push-Open-Metriken {#push-open-metrics}

Braze protokolliert einen Direct Open, wenn Nutzer:innen auf die Benachrichtigung tippen und Ihre App eine Sitzung startet. Das Erweitern einer Rich-Push-Benachrichtigung ohne Öffnen der App protokolliert keinen Direct Open.

Wenn Nutzer:innen Ihre App nach dem Empfang einer Push-Benachrichtigung öffnen, ohne auf die Benachrichtigung zu tippen, kann Braze stattdessen einen Influenced Open protokollieren. Definitionen und Berichte finden Sie unter [Influenced Opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

## Push-Fehlermeldungen {#push-error-messages}

Definitionen häufiger Push-Fehlercodes (einschließlich `DEVICE_UNREGISTERED`, `NotRegistered` und `Unregistered`) finden Sie unter [Häufige Push-Fehlermeldungen]({{site.baseurl}}/user_guide/channels/push/push_error_codes).

Wenn FCM Fehler wie `DEVICE_UNREGISTERED` oder `NotRegistered` zurückgibt, entfernt Braze in der Regel das betroffene Push-Token aus dem Nutzerprofil. Diese Entfernung weist häufig darauf hin, dass die App deinstalliert wurde oder das Token nicht mehr gültig ist. Uninstall-Tracking-Campaigns verwenden dieselbe Token-Entfernungslogik im großen Maßstab.

Benötigen Sie weitere Hilfe? Eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support).