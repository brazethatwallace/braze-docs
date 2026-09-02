---
nav_title: FAQ
article_title: FAQ
page_order: 30
description: "Dieser Artikel behandelt einige der häufigsten Fragen, die bei der Einrichtung von Push-Campaigns auftreten."
page_type: FAQ
channel:
  - Push
---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zum Push-Kanal.

## Warum werden Push-Benachrichtigungen manchmal verzögert zugestellt? {#why-are-push-notifications-sometimes-delayed}

Die Zustellung durchläuft in der Regel drei Phasen: die **Verarbeitung** durch Braze (Segmentierung, Zeitplanung und Übergabe an den Anbieter), den Transport von Braze zu **APNs oder FCM** und die Zustellung vom Anbieter an das **Gerät**. Verzögerungen können in jeder Phase auftreten. Braze hat keinen Einblick in die Warteschlangen des Anbieters oder des Geräts. Verwenden Sie [Verbose Logging]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs) auf dem Client, wenn Sie geräteseitige Timing-Probleme eingrenzen müssen.

## Was passiert, wenn sich mehrere Nutzer:innen auf einem einzigen Gerät anmelden? {#what-happens-when-multiple-users-log-into-a-single-device}

Wenn sich ein:e Nutzer:in von einem Gerät oder einer Website abmeldet, bleibt er/sie per Push erreichbar, bis sich ein:e andere:r Nutzer:in anmeldet. Zu diesem Zeitpunkt wird das Push-Token dem/der neuen Nutzer:in zugewiesen. Das liegt daran, dass jedes Gerät nur ein aktives Push-Abo pro App oder Website haben kann.

Wenn ein Push-Token neu zugewiesen wird, wird die Änderung im **Push Changelog** des Nutzerprofils angezeigt. Sie finden dieses, indem Sie im Kundenprofil zum Tab **Engagement** navigieren.

![Das „Push Changelog“ im Abschnitt „Contact Settings“.]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

## Wird ein Test-Push an alle meine Geräte gesendet? {#when-i-send-a-test-push-does-it-go-to-all-of-my-devices}

Ja. Der Test-Push wird an jedes Push-fähige Gerät gesendet, das mit dem ausgewählten Kundenprofil verknüpft ist. Wenn Sie mehrere Telefone oder Tablets mit demselben/derselben Nutzer:in angemeldet haben, erhält jedes Gerät mit einem gültigen Push-Token die Benachrichtigung.

Um den Test-Push nur an ein Gerät zu senden, können Sie vor dem Testen die Push-Token für die anderen Geräte aus dem Kundenprofil entfernen. Alternativ können Sie beim Senden über den [`/messages/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) im `apple_push`- oder `android_push`-Objekt `send_to_most_recent_device_only` auf `true` setzen, sodass nur das zuletzt aktive Gerät den Push erhält.

## Was bedeutet „Error sending push because the payload was invalid“? {#what-does-error-sending-push-because-the-payload-was-invalid-mean}

Diese Meldung zeigt an, dass APNs die Push-Anfrage aufgrund eines ungültigen Payloads abgelehnt haben (zum Beispiel ein leerer Payload oder ein Payload, der zu groß ist).

Weitere Details und nächste Schritte finden Sie unter [Häufige Push-Fehlermeldungen]({{site.baseurl}}/user_guide/channels/push/push_error_codes).

## Warum hat ein:e Nutzer:in mit Opt-in kein Push-Token? {#why-doesnt-an-opted-in-user-have-a-push-token}

Das kann passieren, wenn das Push-Token des/der Nutzer:in einer anderen Person zugewiesen wurde, die dasselbe Gerät verwendet hat.

1. Navigieren Sie zum **Push Changelog** im Tab **Engagement** des betroffenen Nutzerprofils.
2. Suchen Sie nach einer Meldung, die besagt, dass das Push-Token zu einem/einer anderen Nutzer:in verschoben wurde.
3. Kopieren Sie das Push-Token und fügen Sie es in die Nutzersuche ein.
4. Wenn das Push-Token noch existiert, werden Sie zu dem/der Nutzer:in weitergeleitet, der/die sich zuletzt auf dem Gerät angemeldet hat.

Wenn Sie möchten, dass das Push-Token dem/der ursprünglichen Nutzer:in wieder zugewiesen wird:

1. Lassen Sie den/die ursprüngliche:n Nutzer:in sich in das Profil mit dem fehlenden Push-Token einloggen.
2. Lösen Sie einen neuen Push-Versand aus. Dadurch wird das Token zurück auf das Konto verschoben, sofern Push auf Geräteebene noch aktiviert ist.

## Warum öffnet „Open web URL inside mobile app“ beim Testen einer Entwurfs-Campaign immer die App? {#why-does-open-web-url-inside-mobile-app-always-open-the-app-when-im-testing-a-draft-campaign}

Wenn eine Campaign noch den Status **Entwurf** hat und Sie einen Test-Push senden, öffnet das Tippen auf die Benachrichtigung immer zuerst die App – unabhängig davon, ob die Option **Open web URL inside mobile app** ausgewählt oder deaktiviert ist. Wenn die Campaign **Live** ist, funktioniert das Klickverhalten wie konfiguriert.

Wenn Sie **Open web URL** ohne die Option **Inside App** ausgewählt haben, wird der Link direkt im Standardbrowser des Geräts geöffnet. Wenn Sie **Open web URL inside mobile app** ausgewählt haben, wird der Link in einer In-App-Webansicht geöffnet.

## Was ist der Unterschied zwischen „Send to Production“ und „Send to Development“ bei iOS-Push-Zertifikaten? {#what-is-the-difference-between-send-to-production-and-send-to-development-for-ios-push-certificates}

Beim Hinzufügen eines Apple-Push-Zertifikats in Braze bestimmen die Optionen **Send to Production** und **Send to Development**, welches APNs-Gateway (Apple Push Notification Service) Braze für die Zustellung von Push-Benachrichtigungen verwendet:

- **Send to Development:** Wählen Sie diese Option, wenn die App im Entwicklungsmodus in Xcode erstellt und mit einem Entwicklungs-Provisioning-Profil signiert wurde. Push-Benachrichtigungen werden über Apples Entwicklungs-Gateway (Sandbox) geroutet.
- **Send to Production:** Wählen Sie diese Option, wenn die App über Apples TestFlight, den App Store oder die Enterprise-Distribution verteilt wird. Push-Benachrichtigungen werden über Apples Produktions-Gateway geroutet.

Wenn die falsche Option ausgewählt wird, schlagen Push-Benachrichtigungen stillschweigend fehl, da der Push-Token-Typ nicht zum Gateway passt. In der Regel sollten Apps, die über TestFlight oder den App Store verteilt werden, **Send to Production** verwenden.

## Was ist der Unterschied zwischen den Filtern „Foreground Push Enabled“ und „Background or Foreground Push Enabled“? {#what-is-the-difference-between-the-foreground-push-enabled-and-background-or-foreground-push-enabled-filters}

Diese Segmentierungsfilter prüfen unterschiedliche Bedingungen:

| Filter | Was geprüft wird | Anwendungsfall |
|--------|------------------|----------------|
| **Foreground Push Enabled** | Der/die Nutzer:in hat ein gültiges Vordergrund-Push-Token **und** der Push-Abo-Status ist `Opted-In` oder `Subscribed`. | Nutzer:innen ansprechen, die sichtbare Push-Benachrichtigungen empfangen können. |
| **Background or Foreground Push Enabled** | Der/die Nutzer:in hat ein beliebiges Push-Token (Vordergrund oder Hintergrund) **und** der Push-Abo-Status ist `Opted-In` oder `Subscribed`. Dies schließt Nutzer:innen ein, die sichtbare Push-Benachrichtigungen deaktiviert haben, aber noch ein Hintergrund-Push-Token besitzen. | Wird für [Uninstall-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking), [stille Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/silent) und Geofencing verwendet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Was ist der Unterschied zwischen den Filtern „Foreground Push Enabled“ und „Background or Foreground Push Enabled“?" }

Ein:e Nutzer:in kann `Background or Foreground Push Enabled` sein, ohne `Foreground Push Enabled` zu sein. Das passiert, wenn der/die Nutzer:in sichtbare Push-Benachrichtigungen in den Geräteeinstellungen deaktiviert hat, die App aber noch ein Hintergrund-Push-Token besitzt. Weitere Details finden Sie unter [Push-Nutzer:innen und Abos]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled).

## Wie bestimmt Braze, wann eine Push-Nachricht erfolgreich gesendet wurde? {#how-does-braze-determine-when-a-push-message-is-sent-successfully}

Eine Nachricht wird als gesendet protokolliert, sobald sie vom Push-Dienstanbieter empfangen wurde. Das bedeutet nicht zwangsläufig, dass der/die Nutzer:in die Nachricht erhalten oder gesehen hat.

Für iOS ist der Push-Dienstanbieter der Apple Push Notification Service (APNs), und für Android ist es in der Regel Firebase Cloud Messaging (FCM). Der Push-Dienstanbieter antwortet sofort mit Erfolg oder Fehler. Ein Fehler kann einen Bounce oder einen erneuten Versuch bei Netzwerkproblemen umfassen.

Wenn eine Erfolgsmeldung zurückgegeben wird, protokolliert Braze den Versand, und der Push-Dienst versucht anschließend, die Nachricht an das Gerät zuzustellen. Wenn das Gerät nicht sofort erreichbar ist, versucht der Dienst es erneut – bis zur in Braze festgelegten Ablaufoption (**TTL** für Android, **Expiry** für iOS). Wenn die Nachricht das Zeitlimit überschreitet, verwirft der Push-Dienst den Push, dieser wird jedoch nicht als Bounce gewertet.

- Bei Push-Campaigns mit aktionsbasierter Zustellung wird der Nachrichtenversand protokolliert, sobald der/die Nutzer:in die Aktion ausgeführt hat, die die Campaign auslöst.
- Bei geplanten Campaigns ist der Sendezeitpunkt der Zeitpunkt, zu dem die Nachricht in die Warteschlange eingereiht und an den Push-Dienstanbieter übergeben wurde.
- Bei beiden Zustellungsarten wird die Nachricht in Braze und im Kundenprofil unter **Campaigns Received** als „gesendet“ markiert, auch wenn der/die Nutzer:in den Push möglicherweise noch nicht gesehen oder erhalten hat.

Die Metrik „Zustellungen“ für Push im Dashboard wird beim Laden der Seite als Anzahl der Sendungen abzüglich der Bounces berechnet.