---
nav_title: Nachrichten-Aktivitätsprotokoll
article_title: "Nachrichten-Aktivitätsprotokoll {#dev-console-troubleshooting}"
page_order: 3
page_type: reference
description: "Dieser Referenzartikel beschreibt das Nachrichten-Aktivitätsprotokoll, das Ihnen Nachrichten anzeigt, die mit Ihren Campaigns und Sendungen verknüpft sind. Hier finden Sie auch weitere Informationen."
---

# Nachrichten-Aktivitätsprotokoll {#dev-console-troubleshooting}

> Das **Nachrichten-Aktivitätsprotokoll** gibt Ihnen die Möglichkeit, alle Nachrichten (insbesondere Fehlermeldungen) einzusehen, die mit Ihren Campaigns und Sendungen verknüpft sind.

Sie können API-Campaign-Transaktionen einsehen, Details zu fehlgeschlagenen Nachrichten analysieren und Insights gewinnen, wie Sie die Zustellung von Benachrichtigungen verbessern oder bestehende technische Probleme lösen können.

Um auf das Protokoll zuzugreifen, gehen Sie zu **Einstellungen** > **Einrichtung und Tests** > **Nachrichten-Aktivitätsprotokoll**.

![Nachrichten-Aktivitätsprotokoll]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
Zusätzlich zu diesem Artikel empfehlen wir Ihnen auch unseren Braze-Lernkurs [Qualitätssicherung und Debugging-Tools](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), der erklärt, wie Sie das Nachrichten-Aktivitätsprotokoll für Ihre eigene Fehlerbehebung und Ihr Debugging nutzen können.
{% endalert %}

Sie können nach den folgenden Inhalten filtern, die im **Nachrichten-Aktivitätsprotokoll** protokolliert werden:

- Push-Benachrichtigungsfehler
- Fehler bei abgebrochenen In-App-Nachrichten-Templates
- Webhook-Fehler
- E-Mail-Fehler
- API-Nachrichtendatensätze
- Connected-Content-Fehler
- REST-API-Connected-Audience-Fehler
- User-Aliasing-Fehler
- A/B-Test-Fehler
- SMS/MMS-Fehler
- WhatsApp-Fehler
- Live-Activity-Fehler
- Fehler bei fehlerhaften Nutzer-Triggern
- Braze-Agents-Fehler bei [täglichem Aufruf-Limit]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#monitor-your-agent)
- Braze-Agents-Fehler bei nicht verfügbarem [Modell]({{site.baseurl}}/user_guide/brazeai/agents/reference#models)

Diese Nachrichten können von unserem eigenen System, Ihren Apps oder Plattformen oder von unseren Drittanbieter-Partnern stammen. Dies kann zu einer unbegrenzten Anzahl von Nachrichten führen, die in diesem Protokoll erscheinen können.

## Protokollnachrichten verstehen {#understanding-log-messages}

Um zu ermitteln, was Ihre Nachrichten bedeuten, achten Sie auf die Formulierung jeder einzelnen Nachricht und die zugehörigen Spalten, da sie Ihnen bei der Fehlerbehebung anhand von Kontexthinweisen helfen können.

Zum Beispiel können Einträge vom Typ **Aborted Message Error** aus vielen Gründen auftreten, nicht nur durch [Liquid-Abbruchnachrichten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages). Lesen Sie die Spalte **Message**, um den konkreten Grund zu erfahren:

- Wenn der Versand durch ein Liquid-Tag `abort_message` abgebrochen wurde, zeigt die Spalte **Message** das genaue Liquid-Snippet an, das aufgerufen wurde, zum Beispiel {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %}.
- Bei anderen Abbruchgründen erklärt die Spalte **Message**, warum der Versand abgebrochen wurde.

### API-Campaign-Payloads {#api-campaign-payloads}

Das Message Activity Log zeichnet je nach Typ der API-Campaign unterschiedliche Informationen auf. Der [`/messages/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) protokolliert den Nachrichtentext (messages) in den API-Nachrichteneinträgen, während der [`/campaigns/trigger/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) den Request-Payload oder `api_trigger_properties` nicht im Message Activity Log protokolliert.

### Häufige Nachrichten {#common-messages}

Es gibt einige häufige Nachrichtentypen, die Sie möglicherweise sehen, und einige bieten sogar Links zur Fehlerbehebung, die Ihnen bei der Diagnose und Behebung von Problemen helfen können.

Die folgenden Nachrichten dienen als Beispiele und stimmen möglicherweise nicht exakt mit den Einträgen in der Spalte **Message** Ihres Logs überein.

| Nachrichtentyp | Mögliche Nachricht | Beschreibung |
|---|---|---|
| Soft Bounce | The email address same@example.com soft bounced. | Die E-Mail-Adresse war gültig und die E-Mail-Nachricht erreichte den Mailserver des Empfängers, wurde jedoch wegen eines „vorübergehenden“ Problems abgelehnt. <br><br>Häufige Gründe für einen Soft Bounce sind: {::nomarkdown} <ul> <li> Das Postfach war voll (die Nutzer:innen haben ihr Kontingent überschritten) </li> <li> Der Server war nicht erreichbar </li> <li> Die Nachricht war zu groß für den Posteingang des Empfängers </li>  </ul> {:/} Wenn eine E-Mail einen Soft Bounce erhalten hat, wird in der Regel innerhalb von 72 Stunden ein erneuter Zustellversuch unternommen, aber die Anzahl der Wiederholungsversuche variiert je nach Empfänger. |
| Hard Bounce | The email account that you tried to reach does not exist. Try double-checking the recipient's email address for typos or unnecessary spaces. | Ihre Nachricht hat den Posteingang dieser Person nie erreicht, da kein Posteingang vorhanden war. Wenn Sie tiefer nachforschen möchten, können solche Nachrichten manchmal Links in der Spalte **View Details** enthalten, über die Sie das Profil des beabsichtigten Empfängers einsehen können. |
| Block | Spam message is rejected because of anti-spam policy. | Ihre Nachricht wurde als Spam eingestuft. Dieser E-Mail-Fehler wird für Nutzer:innen protokolliert, wenn wir vom E-Mail-Anbieter ein Ereignis erhalten haben, das darauf hinweist, dass die E-Mail verworfen wurde. Es könnte sich nur auf die beabsichtigten Empfänger:innen beziehen, aber wenn Sie diese Nachricht häufig sehen, sollten Sie Ihre Versandgewohnheiten oder den Inhalt Ihrer Nachricht überdenken. Denken Sie auch daran – haben Sie Ihre [IP aufgewärmt]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)? Falls nicht, kontaktieren Sie Braze für eine Beratung, um dies in Gang zu bringen. |
| Aborted Message Error | {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %} | Wenn ein Versand durch ein Liquid-Tag `abort_message` abgebrochen wird, zeigt die Spalte **Message** das genaue Liquid-Snippet an, das aufgerufen wurde. Andere **Aborted Message Error**-Einträge können unterschiedliche Nachrichten enthalten, die den Abbruchgrund beschreiben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Häufige Nachrichten" }

### Warum ist meine Nachricht hier nicht aufgeführt? {#why-isnt-my-message-listed-here}

Die Nachrichten im Message Activity Log können aus verschiedenen Quellen stammen: von Braze, Ihren Apps oder Plattformen oder von unseren Drittanbieter-Partnern. Das bedeutet, dass eine unendliche Anzahl von Nachrichten in diesem Log erscheinen kann – wie Sie sich vorstellen können, können wir nicht alle aufführen!

Einige mögliche „Block“-Nachrichten könnten zum Beispiel zusätzlich zu der in der obigen Tabelle aufgeführten sein:

- Unfortunately, messages from [_IP_ADDRESS_] weren't sent. Please contact your ISP since part of their network is on our block list.
- Message rejected due to local policy.
- The message was blocked by the receiver as spam.
- Service unavailable, Client host [_IP_ADDRESS_] blocked using Spamhaus.

## Aufbewahrungsdauer {#storage-retention-period}

Fehler der letzten 60 Stunden sind in den Nachrichtenaktivitätsprotokollen verfügbar. Protokolle, die älter als 60 Stunden sind, werden bereinigt und sind nicht mehr zugänglich.

### Anzahl der gespeicherten Fehlerprotokolle {#number-of-error-logs-stored}

Die Anzahl der gespeicherten Protokolle wird von mehreren Bedingungen beeinflusst. Wenn beispielsweise eine geplante Campaign an Tausende von Nutzer:innen gesendet wird, würden wir möglicherweise nur eine Stichprobe der Fehler im Nachrichtenaktivitätsprotokoll sehen, anstatt alle Fehler. Im Folgenden finden Sie eine Übersicht der Bedingungen, die beeinflussen, wie viele Protokolle gespeichert werden:
- Bis zu 20 Fehlerprotokolle desselben Fehlertyps werden für dieselbe Campaign oder denselben Canvas-Schritt innerhalb einer festen Taktungsstunde für die folgenden Fehlertypen gespeichert:
    - Connected-Content-Fehler
    - Abort-Message-Fehler
    - Webhook-Fehler
    - SMS-Ablehnungsfehler
    - SMS-Zustellungsfehler
    - WhatsApp-Fehler
    - A/B-Test-Fehler
- Bis zu 20 Push-Benachrichtigungs-Fehlerprotokolle desselben Fehlertyps werden für dieselbe Campaign oder denselben Canvas-Schritt und dieselbe App-Kombination für die folgenden Fehlertypen gespeichert:
    - Ungültige Push-Anmeldedaten
    - Ungültiges Push-Token
    - Keine Push-Anmeldedaten
    - Token-Fehler
    - Kontingent überschritten
    - Zeitüberschreitung bei Wiederholungsversuchen
    - Ungültige Nutzlast
    - Unerwarteter Fehler
- Bis zu 100 Fehlerprotokolle desselben Fehlertyps werden für dieselbe App innerhalb einer festen Taktungsstunde für die folgenden Fehlertypen gespeichert:
    - Live-Activity-Fehler (Keine Push-Anmeldedaten)
    - Live-Activity-Fehler (Ungültige Push-Anmeldedaten)
    - Sonstige Live-Activity-Fehler
    - APNS-Feedback-Removed-Token-Fehler
- Bis zu 100 Fehlerprotokolle desselben Fehlertyps werden für dieselbe Campaign oder denselben Canvas-Schritt innerhalb einer festen Taktungsstunde für die folgenden Fehlertypen gespeichert:
    - E-Mail-Soft-Bounce-Fehler
    - E-Mail-Hard-Bounce-Fehler
    - E-Mail-Block-Fehler
- Bis zu 100 User-Aliasing-Fehlerprotokolle werden für denselben Workspace innerhalb einer festen Taktungsstunde gespeichert.

## Testversand {#test-sends}

Das **Nachrichtenaktivitätsprotokoll** zeigt Testprotokolle für diese Messaging-Kanäle:

- SMS
- WhatsApp
- LINE
- KakaoTalk
- Webhook

Testversandprotokolle sind für die folgenden Kanäle nicht verfügbar: E-Mail, Content Cards, In-App Messages und Push.

Testversandprotokolle erhalten das Präfix „[TEST SEND]“, aber es ist nicht garantiert, dass alle Testversandprotokolle dieses Präfix haben (z. B. haben Connected-Content-Fehler das Präfix nicht).