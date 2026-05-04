---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für Push
page_order: 5
page_type: reference
description: "Diese Seite enthält Schritte zur Fehlerbehebung für verschiedene Probleme im Zusammenhang mit dem Push-Messaging-Kanal."
channel: push
---

# Fehlerbehebung für Push {#troubleshoot-push}

> Verwenden Sie diese Seite, um Probleme mit dem Push-Messaging-Kanal zu beheben.

## Fehlende Push-Benachrichtigungen {#missing-push-notifications}

Haben Sie Probleme mit der Zustellung von Push-Benachrichtigungen? Es gibt eine Reihe von Schritten, die Sie zur Fehlerbehebung unternehmen können, indem Sie Folgendes überprüfen:

- [Push-Abo-Status](#push-subscription-status)
- [Segment](#segment)
- [Obergrenzen für Push-Benachrichtigungen](#push-notification-caps)
- [Rate-Limits](#rate-limits)
- [Kontrollgruppen-Status](#control-group-status)
- [Gültiges Push-Token](#valid-push-token)
- [Art der Push-Benachrichtigung](#push-notification-type)
- [Aktuelle App](#current-app)

#### Push-Abo-Status {#push-subscription-status}

Push-Benachrichtigungen können nur an abonnierte oder angemeldete Nutzer:innen gesendet werden. Überprüfen Sie Ihr Nutzerprofil im Tab [Engagement]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#engagement-tab) im Abschnitt **Nutzerprofil**, um zu bestätigen, dass Sie aktiv für Push im Workspace registriert sind, den Sie testen. Wenn Sie für mehrere Apps registriert sind, finden Sie diese im Feld **Push Registered For**:

![Push Registered For]({% image_buster /assets/img_archive/trouble1.png %})

Sie können die Nutzerprofile auch über die Braze-Export-Endpunkte exportieren:
- [Nutzer:innen nach Bezeichner]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)
- [Nutzer:innen nach Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)

Beide Endpunkte geben ein Push-Token-Objekt zurück, das Informationen zur Push-Aktivierung pro Gerät enthält.

#### Segment {#segment}

Stellen Sie sicher, dass Sie in das Segment fallen, das Sie ansprechen (wenn es sich um eine Live-Campaign und nicht um einen Test handelt). Im **Nutzerprofil** sehen Sie eine Liste der Segmente, in denen sich die Nutzer:innen aktuell befinden. Beachten Sie, dass dies eine sich ständig ändernde Variable ist, da die Segmentierung in Echtzeit aktualisiert wird.

![Liste der Segmente]({% image_buster /assets/img_archive/trouble2.png %})

Sie können auch bestätigen, dass die Nutzer:innen Teil des Segments sind, indem Sie beim Erstellen eines Segments die **Nutzersuche** verwenden.

![Abschnitt „Nutzersuche“ mit einem Suchfeld.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Obergrenzen für Push-Benachrichtigungen {#push-notification-caps}

Überprüfen Sie die globalen Frequency-Capping-Regeln. Es ist möglich, dass Sie die Push-Benachrichtigung nicht erhalten haben, weil in Ihrem Workspace globales Frequency-Capping aktiv ist und Sie Ihre Push-Benachrichtigungs-Obergrenze für den angegebenen Zeitraum bereits erreicht haben.

Sie können dies überprüfen, indem Sie das [globale Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#freq-cap-feat-over) im Dashboard prüfen. Wenn die Campaign so eingestellt ist, dass sie die Frequency-Capping-Regeln einhält, wird eine Anzahl von Nutzer:innen angezeigt, die von diesen Einstellungen betroffen sind.

![Campaign-Details]({% image_buster /assets/img_archive/trouble3.png %})

#### Rate-Limits {#rate-limits}

Wenn Sie ein Rate-Limit für Ihre Campaign oder Ihren Canvas festgelegt haben, kann es sein, dass Sie aufgrund der Überschreitung dieses Limits keine Nachrichten erhalten. Weitere Informationen finden Sie unter [Rate-Limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#rate-limiting).

#### Kontrollgruppen-Status {#control-group-status}

Wenn es sich um eine Einkanal-Campaign oder einen Canvas mit einer Kontrollgruppe handelt, ist es möglich, dass Sie in die Kontrollgruppe fallen.

  1. Überprüfen Sie die [Variantenverteilung]({{site.baseurl}}/user_guide/messaging/ab_testing/#step-5-distribute-users-among-your-variants), um festzustellen, ob es eine Kontrollgruppe gibt.
  2. Falls ja, erstellen Sie ein Segment, das nach [In Campaign-Kontrollgruppe]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter) filtert, und [exportieren Sie das Segment]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/#exporting-to-csv), um zu prüfen, ob Ihre Nutzer-ID auf dieser Liste steht.

#### Gültiges Push-Token {#valid-push-token}
Ein Push-Token ist ein Bezeichner, den Absender verwenden, um bestimmte Geräte mit einer Push-Benachrichtigung anzusprechen. Wenn das Gerät kein gültiges Push-Token hat, gibt es keine Möglichkeit, eine Push-Benachrichtigung an dieses Gerät zu senden.

#### Art der Push-Benachrichtigung {#push-notification-type}

Überprüfen Sie, ob Sie die richtige Art von Push-Benachrichtigung verwenden. Wenn Sie beispielsweise ein FireTV ansprechen möchten, würden Sie eine Kindle-Push-Benachrichtigung verwenden, nicht eine Android-Push-Campaign. Ebenso sollten Sie für Android eine Android-Push-Benachrichtigung verwenden und nicht eine iOS-Push-Campaign. Lesen Sie die folgenden Artikel für weitere Informationen zum Verständnis des Braze-Workflows für:
- [Apple Push Notification]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### Aktuelle App {#current-app}

Stellen Sie beim Testen von Push-Sendungen mit internen Nutzer:innen sicher, dass die Person, die die Push-Benachrichtigung erhalten soll, aktuell in der entsprechenden App angemeldet ist. Dies kann dazu führen, dass Nutzer:innen entweder keine Push-Benachrichtigung erhalten oder eine Push-Benachrichtigung erhalten, für die sie Ihrer Meinung nach nicht segmentiert sind.

## Tippen auf eine Push-Benachrichtigung öffnet die App nicht {#clicking-a-push-notification-doesnt-open-the-app}

Wenn das Tippen auf eine Push-Benachrichtigung Ihre App nicht öffnet, überprüfen Sie je nach Plattform Folgendes.

### Android

1. **Klickverhalten überprüfen:** Bestätigen Sie, dass die Campaign so konfiguriert ist, dass die App beim Klicken geöffnet wird.
2. **Deeplink-Behandlung prüfen:** Überprüfen Sie in Ihrer `braze.xml`-Datei, ob `com_braze_handle_push_deep_links_automatically` auf `true` oder `false` gesetzt ist.
   - Wenn auf `true` gesetzt, behandelt das Braze SDK Deeplinks direkt und die App sollte wie erwartet geöffnet werden.
   - Wenn auf `false` gesetzt, benötigt Ihre App einen Broadcast-Receiver, der Push-Empfangs- und Öffnungs-Intents abhört und verarbeitet. Überprüfen Sie, ob dieser Receiver korrekt implementiert ist.
3. **Ausführliche Logs erfassen:** [Aktivieren Sie ausführliches Logging]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/), reproduzieren Sie das Problem und stellen Sie die Logs zusammen mit Ihrer `braze.xml` und `AndroidManifest.xml` dem Braze-Support zur Verfügung.

### iOS

1. **Klickverhalten überprüfen:** Bestätigen Sie, dass die Campaign so konfiguriert ist, dass die App beim Klicken geöffnet wird.
2. **Push-Integration prüfen:** Deeplinking von einer Push-Benachrichtigung in die App wird automatisch durch die Braze [Standard-Push-Integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) behandelt. Bestätigen Sie, dass die Integration korrekt implementiert ist, einschließlich aller angepassten Delegate-Behandlungen.
3. **Ausführliche Logs erfassen:** [Aktivieren Sie ausführliches Logging]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/), reproduzieren Sie das Problem und stellen Sie die Logs dem Braze-Support zur Verfügung.

## Push-Klicks öffnen unerwartet in der App {#push-clicks-unexpectedly-open-in-app}

Wenn Links in Push-Benachrichtigungen unerwartet in Ihrer App statt in Ihrem Webbrowser geöffnet werden, liegt möglicherweise ein Problem mit Ihrer Campaign-Konfiguration oder SDK-Implementierung vor. Folgen Sie diesen Schritten zur Hilfe.

### Klickverhalten überprüfen {#verify-on-click-behavior}

Überprüfen Sie in Ihrer Campaign oder Ihrem Canvas-Schritt, ob **Web-URL in mobiler App öffnen** nicht ausgewählt ist. Falls doch, deaktivieren Sie die Auswahl und starten Sie erneut.

![Feld „Klickverhalten“ bei der Konfiguration einer Push-Benachrichtigung, eingestellt auf „Web-URL öffnen“ mit deaktiviertem „Web-URL in mobiler App öffnen“.]({% image_buster /assets/img/push_on_click.png %})

Die Standardinteraktion für das Klickverhalten „Web-URL öffnen“ unterscheidet sich je nach SDK-Version. Für SDK-Versionen iOS 2.29.0 und Android 2.0.0 und höher ist diese Option standardmäßig ausgewählt und Web-URLs werden in einer Webansicht innerhalb der App geöffnet. Vor diesen Versionen ist diese Option standardmäßig deaktiviert und Web-URLs werden im Standard-Webbrowser des Geräts geöffnet.

Wenn dies nicht das Problem ist, liegt möglicherweise ein Problem mit Ihrer Push-Implementierung vor.

### Push-Integration erneut prüfen {#double-check-push-integration}

Wenn Links in Ihren Push-Benachrichtigungen unerwartet in der App geöffnet werden, kann dies an Problemen mit Ihrer Push-Benachrichtigungs-Integration oder Anpassungseinstellungen liegen. Folgen Sie diesen Schritten zur Fehlerbehebung:

1. **Push-Delegate-Implementierung überprüfen:** Stellen Sie sicher, dass der Braze-Push-Delegate korrekt implementiert ist. Detaillierte Anweisungen finden Sie im Integrationsleitfaden für Push-Benachrichtigungen für Ihre [Plattform]({{site.baseurl}}/developer_guide/home/).
2. **Angepasste Link-Behandlung prüfen:** Überprüfen Sie, ob die App eine angepasste Behandlung für alle `https://`-Links enthält. Angepasste Konfigurationen können Standardverhalten überschreiben. Arbeiten Sie mit Ihrem Entwicklungsteam zusammen, um diese Einstellungen bei Bedarf zu überprüfen und anzupassen.
3. **iOS-Push-Registrierung überprüfen:** Für iOS lesen Sie Schritt 1 des Push-Integrationsleitfadens zur [Registrierung von Push-Benachrichtigungen bei APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns) erneut. Stellen Sie sicher, dass Ihr Delegate-Objekt synchron zugewiesen wird, bevor die App den Start abschließt. Dieser Schritt sollte in der Methode `application:didFinishLaunchingWithOptions:` abgeschlossen werden.
4. **Integration testen:** Testen Sie nach den Anpassungen das Push-Benachrichtigungsverhalten sowohl auf iOS- als auch auf Android-Geräten, um zu bestätigen, dass das Problem behoben ist.

## Zu einem .p8-Authentifizierungsschlüssel migrieren {#migrate-to-a-p8-authentication-key}

Apple `.p8`-Authentifizierungsschlüssel sind der erforderliche Ansatz für APNs-Push in Braze. Im Gegensatz zu älteren Zertifikatsdateitypen laufen `.p8`-Schlüssel nicht ab und unterstützen alle Ihre Apps unter einem einzigen Schlüssel, wodurch jährliche Zertifikatserneuerungen entfallen und das Risiko von Push-Zustellungsfehlern reduziert wird.

Wenn Sie derzeit ein `.p12`- oder `.pem`-Zertifikat verwenden, migrieren Sie so bald wie möglich zu einem `.p8`-Schlüssel. Anweisungen zum Erstellen und Hochladen eines `.p8`-Schlüssels finden Sie unter [APNs-Push-Zertifikat hochladen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift). Apples Anleitung zum Generieren eines `.p8`-Schlüssels aus Ihrem Entwicklerkonto finden Sie unter [Communicate with APNs using authentication tokens](https://developer.apple.com/help/account/capabilities/communicate-with-apns-using-authentication-tokens/).

## Web-Push-Benachrichtigungen verhalten sich nicht wie erwartet {#web-push-notifications-arent-behaving-as-expected}

Wenn Sie Probleme mit Push-Benachrichtigungen in Ihrem Browser haben, müssen Sie möglicherweise die Benachrichtigungsberechtigungen Ihrer Website zurücksetzen und den Speicher Ihrer Website löschen. Folgen Sie diesen Schritten zur Hilfe.

{% tabs %}
{% tab Chrome %}

### Chrome auf dem Desktop zurücksetzen {#reset-chrome-on-desktop}

1. Wählen Sie neben Ihrer URL im Chrome-Browser das Schieberegler-Symbol **Website-Informationen anzeigen** aus.
2. Wählen Sie unter **Benachrichtigungen** die Option **Berechtigung zurücksetzen**.
3. Öffnen Sie die Chrome DevTools. Die folgenden Tastenkombinationen gelten je nach Betriebssystem.

<style>
table {
    max-width: 50%;
}
</style>

| Betriebssystem | Tastenkombinationen                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4. Navigieren Sie in den DevTools zum Tab **Application**.
5. Wählen Sie in der Seitenleiste **Storage** aus.
6. Wählen Sie **Clear site data**.
7. Chrome fordert Sie auf, die Seite neu zu laden, um Ihre aktualisierten Einstellungen anzuwenden. Wählen Sie **Reload**.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab zu Ihrer Website und probieren Sie es aus.

### Chrome auf Android zurücksetzen {#reset-chrome-on-android}

Wenn Sie eine Benachrichtigung von Ihrer Website in Ihrer Android-Benachrichtigungsleiste sehen:

1. Tippen Sie in der Push-Benachrichtigung auf <i class="fas fa-cog" title="Einstellungen"></i> und wählen Sie **Website-Einstellungen**.
2. Tippen Sie unter **Website-Einstellungen** auf **Löschen und zurücksetzen**.

Wenn Sie keine Benachrichtigung von Ihrer Website geöffnet haben:

1. Öffnen Sie Chrome auf Android.
2. Tippen Sie auf das Menü <i class="fas fa-ellipsis-vertical"></i>.
3. Gehen Sie zu **Einstellungen** > **Website-Einstellungen** > **Benachrichtigungen**.
4. Überprüfen Sie, ob Benachrichtigungen auf **Vor dem Senden fragen (empfohlen)** eingestellt sind.
5. Suchen Sie Ihre Website in der Liste.
6. Wählen Sie den Eintrag aus und tippen Sie auf **Löschen und zurücksetzen**.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab zu Ihrer Website und probieren Sie es aus.

{% endtab %}
{% tab Firefox %}

### Firefox auf dem Desktop zurücksetzen {#reset-firefox-on-desktop}

1. Wählen Sie neben Ihrer Website-URL <i class="fa-solid fa-circle-info" alt="Info-Symbol"></i> oder <i class="fas fa-lock" alt="Schloss-Symbol"></i> aus.
2. Wählen Sie unter **Berechtigungen** neben **Benachrichtigungen empfangen** das Symbol <i class="fa-solid fa-circle-xmark" title="Diese Berechtigung löschen und erneut fragen"></i>, um die Benachrichtigungsberechtigungen zu löschen.
3. Wählen Sie im selben Menü **Cookies und Website-Daten löschen**.
4. Wählen Sie im Bestätigungsdialog **OK**.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab zu Ihrer Website und probieren Sie es aus.

### Firefox auf Android zurücksetzen {#reset-firefox-on-android}

Um Push-Berechtigungen auf Android zurückzusetzen, lesen Sie diesen [Mozilla-Support-Artikel](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

{% endtab %}
{% tab Safari %}

### Safari auf macOS zurücksetzen {#reset-safari-on-macos}

{% alert note %}
Diese Schritte gelten nur für macOS, da Apple Web-Push für Safari unter Windows nicht unterstützt.
{% endalert %}

1. Öffnen Sie Safari.
2. Gehen Sie in der [Menüleiste auf dem Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac) zu **Safari** > **Einstellungen** > **Websites** > **Benachrichtigungen**.
3. Wählen Sie Ihre Website aus der Liste aus.
4. Wählen Sie **Entfernen**, um die Benachrichtigungsberechtigungen für die Website zu löschen.
5. Gehen Sie dann zu **Datenschutz** > **Website-Daten verwalten**.
6. Wählen Sie Ihre Website aus der Liste aus.
7. Wählen Sie **Entfernen** oder, um alle Website-Daten zu entfernen, wählen Sie **Alle entfernen**.
8. Wählen Sie **Fertig**.

Ihre Push-Berechtigungen sind jetzt zurückgesetzt. Öffnen Sie einen neuen Tab zu Ihrer Website und probieren Sie es aus.

{% endtab %}
{% endtabs %}

## Push-Fehlermeldungen {#push-error-messages}

Detaillierte Informationen zu häufigen Push-Fehlermeldungen (wie `DEVICE_UNREGISTERED`, `Unregistered`, `NotRegistered` und andere) finden Sie unter [Häufige Push-Fehlermeldungen]({{site.baseurl}}/user_guide/channels/push/push_error_codes/).

Benötigen Sie weitere Hilfe? Eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).