---
nav_title: Abo-Status
article_title: Abo-Status
page_order: 0
page_type: reference
description: "Erfahren Sie, wie Braze den Abo-Status über E-Mail, LINE, Kurzmitteilungsdienst or SMS, RCS und WhatsApp hinweg verfolgt und wie der Status die Nachrichtenzustellung steuert."

---

# Abo-Status {#subscription-status}

> Erfahren Sie, wie Braze den Abo-Status über Messaging-Kanäle hinweg verfolgt, wie globaler Status und Abo-Gruppenstatus zusammenwirken und wo kanalspezifische Regeln gelten.

Der Abo-Status teilt Braze mit, ob eine Nutzer:in berechtigt ist, Nachrichten auf einem Kanal zu empfangen. Der Status kann das Targeting von Campaigns und Canvase, Segment-Filter und die Zustellung durch Braze steuern.

## So funktioniert der Abo-Status in Braze {#how-subscription-status-works-in-braze}

Braze verfolgt den Abo-Status auf zwei Ebenen:

| Ebene | Was sie steuert | Kanäle |
| ----- | --------------- | ------ |
| Globaler Abo-Status | Ob eine Nutzer:in überhaupt Nachrichten auf diesem Kanal empfangen kann | E-Mail, Push |
| Abo-Gruppenstatus | Ob eine Nutzer:in für eine bestimmte Gruppe innerhalb eines Kanals angemeldet ist | E-Mail, Kurzmitteilungsdienst or SMS, MMS, RCS, WhatsApp, LINE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="So funktioniert der Abo-Status in Braze" }

Globaler Status und Abo-Gruppenstatus wirken zusammen. Bei E-Mail erhält eine Nutzer:in, die global abgemeldet ist, keine E-Mails – selbst wenn sie einer Abo-Gruppe zugeordnet ist. Bei Kurzmitteilungsdienst or SMS, RCS, WhatsApp und LINE müssen Nutzer:innen der entsprechenden Abo-Gruppe zugeordnet sein, um Nachrichten von dieser Gruppe zu erhalten.

Sie können den Abo-Status im Profil einer Nutzer:in unter **Engagement** > **Kontakteinstellungen** einsehen und Update or aktualisieren or aktualisieren – über die Representational State Transfer API, das SDK or Software-Development-Kit, einen CSV-Import, Präferenzcenter und kanalspezifische Opt-in-Abläufe. Braze zählt Änderungen des Abo-Status nicht als Datenpunkte.

{% alert note %}
Abo-Gruppen ermöglichen ein granulares Opt-in innerhalb eines Kanals (zum Beispiel Werbe- versus Transaktions-Kurzmitteilungsdienst or SMS). Der globale E-Mail-Status und die Abo-Gruppenmitgliedschaft wirken bei der Entscheidung, wer erreichbar ist, zusammen.
{% endalert %}

## E-Mail {#email}

Braze hat drei globale Abo-Status für E-Mail. Diese Status steuern, ob Nutzer:innen Nachrichten erhalten, die an abonnierte oder angemeldete Zielgruppen gerichtet sind. Nutzer:innen im Status `unsubscribed` erhalten beispielsweise keine Nachrichten, die an `subscribed`- oder `opted-in`-Nutzer:innen gerichtet sind.

| Status | Definition |
| ------ | ---------- |
| Opted-in | Eine Nutzer:in hat ausdrücklich bestätigt, dass sie E-Mails erhalten möchte. Braze empfiehlt einen expliziten Opt-in-Prozess, um die Zustimmung der Nutzer:innen zum E-Mail-Versand einzuholen. |
| Subscribed | Eine Nutzer:in hat sich weder abgemeldet noch ausdrücklich für den E-Mail-Empfang angemeldet. Dies ist der Standard-Abo-Status bei der Erstellung eines Nutzerprofils. |
| Unsubscribed | Eine Nutzer:in hat sich ausdrücklich von Ihren E-Mails abgemeldet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="E-Mail-Abo-Status" }

### E-Mail-spezifisches Verhalten {#email-specific-behavior}

- **Abmeldungen und Spam-Berichte:** Braze meldet Nutzer:innen automatisch ab, die sich über eine [benutzerdefinierte Fußzeile]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer) abmelden. Wenn eine Nutzer:in eine E-Mail als Spam markiert, sendet Braze nur noch Transaktions-E-Mails (Nachrichten, die mit **An alle Nutzer:innen senden, einschließlich abgemeldeter Nutzer:innen** versendet werden).
- **Hard Bounces:** Wenn eine E-Mail-Adresse einen Hard Bounce verursacht, setzt Braze den Abo-Status der Nutzer:in nicht automatisch auf `unsubscribed`. Braze markiert die Adresse als ungültig und stellt den Versand ein, bis die Nutzer:in ihre E-Mail-Adresse aktualisiert.
- **Gemeinsam genutzte E-Mail-Adressen:** Wenn sich der globale E-Mail-Abo-Status einer Nutzer:in ändert, überträgt Braze diesen Status auf andere Profile mit derselben E-Mail-Adresse – bis zu 100 Profile pro Änderung.
- **Aktualisierung der E-Mail-Adresse:** Wenn eine Nutzer:in ihre E-Mail-Adresse aktualisiert, wird ihr Abo-Status auf `subscribed` gesetzt, es sei denn, die aktualisierte Adresse existiert bereits in einem anderen Profil – in diesem Fall übernimmt die Nutzer:in den Status dieses Profils.

Informationen zum Update or aktualisieren or aktualisieren des Abo-Status, zur Statusprüfung, zu Präferenzcentern und zum Campaign-Targeting finden Sie unter [E-Mail-Abos]({{site.baseurl}}/user_guide/channels/email/subscriptions).

## LINE {#line}

LINE ist die maßgebliche Quelle für den LINE-Abo-Status. Selbst wenn ein Kundenprofil or Nutzerprofil eine `native_line_id` hat, stellt Braze keine LINE-Nachrichten zu, sofern die Nutzer:in nicht Ihrem LINE-Kanal folgt.

Der LINE-Abo-Status wird anhand der `native_line_id` verfolgt, nicht anhand der `external_id`. Wenn mehrere Profile dieselbe `native_line_id` teilen, übernehmen sie denselben LINE-Abo-Status.

| Status | Definition |
| ------ | ---------- |
| Subscribed | Die Nutzer:in folgt Ihrem LINE-Kanal über ihre LINE-App. |
| Unsubscribed | Die Nutzer:in folgt Ihrem LINE-Kanal nicht oder hat das Folgen explizit aufgehoben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE-Abo-Status" }

### Abo-Synchronisierungstool {#subscription-sync-tool}

Nach einer erfolgreichen LINE-Kanalintegration stellt Braze ein Abo-Synchronisierungstool bereit, um bestehende Braze-Profile mit den LINE-Follower-Daten abzugleichen:

- Profile mit einer `native_line_id`, die Ihrem Kanal folgen, werden auf `subscribed` aktualisiert.
- Follower ohne ein passendes Braze-Profil erhalten ein anonymes Profil mit `native_line_id`, einem `line_id`-Nutzer-Alias und dem Status `subscribed`.

Sie können den LINE-Abo-Gruppenstatus während der Integration nicht manuell festlegen – LINE steuert den Status, und Braze synchronisiert ihn.

### Aktualisierungen durch Follow- und Unfollow-Ereignisse {#follow-and-unfollow-event-updates}

Wenn Braze LINE-Webhook-Ereignisse für Ihren integrierten Kanal empfängt:

- **Follow:** Alle Profile mit einer passenden `native_line_id` werden auf `subscribed` gesetzt. Wenn kein Profil existiert, [erstellt Braze eine anonyme Nutzer:in]({{site.baseurl}}/user_guide/channels/line/message_users/user_management).
- **Unfollow:** Alle Profile mit einer passenden `native_line_id` werden auf `unsubscribed` gesetzt.

Informationen zu Einrichtungsschritten, Nutzerabgleich und Anwendungsfällen finden Sie unter [LINE-Einrichtung]({{site.baseurl}}/user_guide/channels/line/line_setup#user-setup) und [LINE-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups).

## Kurzmitteilungsdienst or SMS und RCS {#sms-and-rcs}

Kurzmitteilungsdienst or SMS und RCS verwenden den Abo-Gruppenstatus, keinen separaten globalen Kanalstatus. Eine Nutzer:in kann gleichzeitig bei einer Transaktionsgruppe `subscribed` und bei einer Werbegruppe `unsubscribed` sein.

| Status | Definition |
| ------ | ---------- |
| Subscribed | Die Nutzer:in ist für den Empfang von Kurzmitteilungsdienst or SMS und RCS einer bestimmten Abo-Gruppe angemeldet – entweder über die Braze-Abo-API, ein Opt-in-Schlüsselwort oder eine andere unterstützte Methode. Wenn [Double-Opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) aktiviert ist, müssen Nutzer:innen das Opt-in bestätigen, bevor der Status auf `Subscribed` aktualisiert wird. |
| Unsubscribed | Die Nutzer:in hat sich von dieser Abo-Gruppe abgemeldet, indem sie ein Opt-out-Schlüsselwort gesendet hat oder über die [Braze-Abo-API]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kurzmitteilungsdienst or SMS- und RCS-Abo-Status" }

### Kurzmitteilungsdienst or SMS- und RCS-spezifisches Verhalten {#sms-and-rcs-specific-behavior}

- **Übernahme der Telefonnummer:** Wenn eine Telefonnummer einem Profil hinzugefügt oder aktualisiert wird, übernimmt die Nummer den Abo-Gruppenstatus vom Profil oder von einem bestehenden Profil, das diese Nummer bereits verwendet.
- **Schlüsselwortverarbeitung:** Nutzer:innen können sich durch das Senden von Standard- oder benutzerdefinierten [Schlüsselwörtern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) an- oder abmelden. Braze aktualisiert den Abo-Status automatisch.
- **Compliance:** Braze sendet niemals Kurzmitteilungsdienst or SMS oder RCS an Nutzer:innen, die nicht bei der ausgewählten Abo-Gruppe angemeldet sind.

Informationen zur Einrichtung, zum Versand und zur Verwaltung von Abo-Gruppen finden Sie unter [Kurzmitteilungsdienst or SMS-, MMS- und RCS-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups).

## WhatsApp {#whatsapp}

WhatsApp verwendet ebenfalls den Abo-Gruppenstatus. Meta verlangt eine ausdrückliche [Opt-in-Zustimmung](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/), bevor Sie Marketing-Nachrichten senden.

| Status | Definition |
| ------ | ---------- |
| Subscribed | Die Nutzer:in hat ausdrücklich bestätigt, dass sie WhatsApp-Nachrichten von Ihrem Unternehmen erhalten möchte – über einen Opt-in-Ablauf oder die Braze-Abo-API. |
| Unsubscribed | Die Nutzer:in hat kein Opt-in erteilt oder ihr Opt-in wurde entfernt. Abgemeldete Nutzer:innen erhalten keine Nachrichten von Telefonnummern in dieser Abo-Gruppe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="WhatsApp-Abo-Status" }

### Opt-in-Anforderungen {#opt-in-requirements}

Um Nutzer:innen über WhatsApp zu kontaktieren, stellen Sie Braze eine `external_id`, eine [Telefonnummer]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) und einen aktualisierten Abo-Status für jede Nutzer:in bereit. Sammeln Sie Opt-ins auf Ihrer Website, in Ihrer App, per Kurzmitteilungsdienst or SMS, über In-App-Nachrichten, eingehende WhatsApp-Threads oder durch einen CSV-Import von Nutzer:innen, die sich bereits anderweitig angemeldet haben.

### Opt-out-Methoden {#opt-out-methods}

Nutzer:innen können sich auf folgende Weise abmelden:

- **Eingehende Schlüsselwort-Workflows:** Canvase oder Campaigns, die durch Opt-out-Schlüsselwörter (zum Beispiel „STOP“) ausgelöst werden, mit einem Folgeschritt, der den Abo-Status aktualisiert.
- **Marketing-Opt-out-Schnellantworten:** Nachrichtenvorlagen mit Metas Marketing-Opt-out-Button, kombiniert mit einem Abo-Gruppen-Aktualisierungsschritt in Ihrem Canvas.
- **Blockierungen und Meldungen:** Wenn eine Nutzer:in Ihr Unternehmen blockiert, werden nachfolgende Nachrichten nicht zugestellt und nicht berechnet, aber der Braze-Abo-Status wird nicht aktualisiert. Nutzermeldungen ändern den Abo-Status ebenfalls nicht.

### WhatsApp-Schalter „Angebote und Ankündigungen“ {#whatsapp-offers-and-announcements-toggle}

Der native WhatsApp-Schalter **Angebote und Ankündigungen** ist von den Braze-Abo-Gruppen getrennt. Wenn eine Nutzer:in ihn in WhatsApp deaktiviert, blockiert Meta die Marketing-Zustellung, selbst wenn Braze `subscribed` anzeigt. Die beiden Ebenen synchronisieren sich nicht automatisch.

Schritt-für-Schritt-Anleitungen für Opt-in- und Opt-out-Workflows finden Sie unter [WhatsApp-Opt-ins und -Opt-outs]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) und [WhatsApp-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

## Segmentierung und Targeting nach Abo-Status {#segment-and-target-by-subscription-status}

Verwenden Sie Abo-Status-Filter im Segment-Builder, um Zielgruppen nach Kanal gezielt anzusprechen oder auszuschließen – zum Beispiel die Filter **Email Subscription Status**, **Push Subscription Status** und **Subscription Group**.

Beim Erstellen von Campaigns und Canvase können Sie über die Optionen **Sendeeinstellungen** und **Zielgruppe** nur an Nutzer:innen mit einem bestimmten Abo-Status senden (zum Beispiel „subscribed“ und „opted-in“). Definitionen der E-Mail- und Push-Filter finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).