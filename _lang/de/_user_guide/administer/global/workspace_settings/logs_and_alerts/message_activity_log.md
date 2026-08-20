---
nav_title: Nachrichten-Aktivitätsprotokoll
article_title: Nachrichten-Aktivitätsprotokoll
page_order: 3
page_type: reference
description: "Dieser Referenzartikel beschreibt das Nachrichten-Aktivitätsprotokoll, das Ihnen Nachrichten anzeigt, die mit Ihren Campaigns und Sendungen verknüpft sind. Hier finden Sie auch Informationen darüber, wie Sie Protokollnachrichten verstehen können."

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

Um zu verstehen, was Ihre Nachrichten bedeuten, achten Sie auf den Wortlaut jeder Nachricht und die zugehörigen Spalten, da diese Ihnen bei der Fehlerbehebung mithilfe von Kontexthinweisen helfen können.

Zum Beispiel können Einträge vom Typ **Aborted Message Error** aus vielen Gründen auftreten, nicht nur aufgrund von [Liquid-Abbruchnachrichten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages). Lesen Sie die Spalte **Message**, um den konkreten Grund zu erfahren:

- Wenn der Versand durch ein Liquid-Tag `abort_message` abgebrochen wurde, zeigt die Spalte **Message** das genaue Liquid-Snippet an, das aufgerufen wurde, zum Beispiel {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %}.
- Bei anderen Abbruchgründen erklärt die Spalte **Message**, warum der Versand abgebrochen wurde.

### API-Campaign-Payloads {#api-campaign-payloads}

Das Nachrichtenaktivitätsprotokoll zeichnet je nach Art der API-Campaign unterschiedliche Informationen auf. Der [`/messages/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) protokolliert den Nachrichtentext (Nachrichten) in API-Nachrichtendatensätzen, während der [`/campaigns/trigger/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) den Anfrage-Payload oder `api_trigger_properties` nicht im Nachrichtenaktivitätsprotokoll erfasst.

### Häufige Nachrichten {#common-messages}

Es gibt einige häufige Nachrichtentypen, die Sie möglicherweise sehen, und einige davon bieten sogar Links zur Fehlerbehebung, die Ihnen bei der Diagnose und Behebung von Problemen helfen können.

Die folgenden Nachrichten dienen als Beispiele und stimmen möglicherweise nicht genau mit dem überein, was in der Spalte **Message** Ihres Protokolls angezeigt wird.

| Nachrichtentyp | Mögliche Nachricht | Beschreibung |
|---|---|---|
| Soft Bounce | The email address same@example.com soft bounced. | Die E-Mail-Adresse war gültig und die E-Mail-Nachricht hat den Mailserver der Empfänger:in erreicht, wurde aber aufgrund eines „temporären“ Problems abgelehnt. <br><br>Häufige Gründe für Soft Bounces sind: {::nomarkdown} <ul> <li> Das Postfach war voll (die Nutzer:in hat ihr Kontingent überschritten) </li> <li> Der Server war nicht erreichbar </li> <li> Die Nachricht war zu groß für den Posteingang der Empfänger:in </li>  </ul> {:/} Wenn eine E-Mail einen Soft Bounce erhalten hat, wird in der Regel innerhalb von 72 Stunden ein erneuter Zustellversuch unternommen, wobei die Anzahl der Wiederholungsversuche je nach Empfänger variiert. |
| Hard Bounce | The email account that you tried to reach does not exist. Try double-checking the recipient's email address for typos or unnecessary spaces. | Ihre Nachricht hat den Posteingang dieser Person nie erreicht, da kein Posteingang vorhanden war. Wenn Sie tiefer nachforschen möchten, können Nachrichten wie diese manchmal Links in der Spalte **View Details** enthalten, über die Sie das Profil der vorgesehenen Empfänger:in einsehen können. |
| Block | Spam message is rejected because of anti-spam policy. | Ihre Nachricht wurde als Spam eingestuft. Dieser E-Mail-Fehler wird für eine Nutzer:in protokolliert, wenn wir ein Ereignis vom ESP erhalten haben, das anzeigt, dass die E-Mail verworfen wurde. Es könnte nur für diese bestimmte Empfänger:in gelten, aber wenn Sie diese Nachricht häufig sehen, sollten Sie Ihre Versandgewohnheiten oder den Inhalt Ihrer Nachricht überprüfen. Denken Sie auch daran: Haben Sie Ihre [IP aufgewärmt]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)? Falls nicht, wenden Sie sich an Braze, um Unterstützung bei der Einrichtung zu erhalten. |
| Aborted Message Error | {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %} | Wenn ein Versand durch ein Liquid-Tag `abort_message` abgebrochen wird, zeigt die Spalte **Message** das genaue Liquid-Snippet an, das aufgerufen wurde. Andere **Aborted Message Error**-Einträge können unterschiedliche Nachrichten enthalten, die den Abbruchgrund beschreiben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Häufige Nachrichten" }

### Warum wird meine Nachricht hier nicht aufgeführt? {#why-isnt-my-message-listed-here}

Die Nachrichten im Nachrichtenaktivitätsprotokoll können aus verschiedenen Quellen stammen: Braze, Ihren Apps oder Plattformen oder unseren Drittanbieter-Partnern. Das bedeutet, dass eine unendliche Anzahl von Nachrichten in diesem Protokoll erscheinen kann – wie Sie sich vorstellen können, können wir nicht alle auflisten!

Zum Beispiel könnten einige mögliche „Block“-Nachrichten, zusätzlich zu der in der obigen Tabelle aufgeführten, folgende sein:

- Unfortunately, messages from [_IP_ADDRESS_] weren't sent. Please contact your Internet Service provider since part of their network is on our block list.
- Message rejected due to local policy.
- The message was blocked by the receiver as spam.
- Service unavailable, Client host [_IP_ADDRESS_] blocked using Spamhaus.

## Aufbewahrungszeitraum {#storage-retention-period}

Fehler der letzten 60 Stunden sind in den Nachrichtenaktivitätsprotokollen verfügbar. Protokolle, die älter als 60 Stunden sind, werden bereinigt und sind nicht mehr zugänglich.

### Anzahl der gespeicherten Fehlerprotokolle {#number-of-error-logs-stored}

Die Anzahl der gespeicherten Protokolle wird von mehreren Bedingungen beeinflusst. Wenn beispielsweise eine geplante Campaign an Tausende von Nutzer:innen gesendet wird, wird möglicherweise nur eine Stichprobe der Fehler im Nachrichtenaktivitätsprotokoll angezeigt, anstatt alle Fehler. Im Folgenden finden Sie eine Übersicht der Bedingungen, die beeinflussen, wie viele Protokolle gespeichert werden:
- Bis zu 20 Fehlerprotokolle desselben Fehlertyps werden für dieselbe Campaign oder denselben Canvas-Schritt innerhalb einer festen Taktungsstunde für die folgenden Fehlertypen gespeichert:
    - Connected-Content-Fehler
    - Nachrichtenabbruch-Fehler
    - Webhook-Fehler
    - SMS-Ablehnungsfehler
    - SMS-Zustellungsfehler
    - WhatsApp-Fehler
    - A/B-Test-Fehler
- Bis zu 20 Push-Benachrichtigungs-Fehlerprotokolle desselben Fehlertyps werden für dieselbe Campaign oder denselben Canvas-Schritt und dieselbe App-Kombination für die folgenden Fehlertypen gespeichert:
    - Invalid Push Credential
    - Invalid Push Token
    - No Push Credential
    - Token Errors
    - Quota Exceeded
    - Retries Timed Out
    - Invalid Payload
    - Unexpected Error
- Bis zu 100 Fehlerprotokolle desselben Fehlertyps werden für dieselbe App innerhalb einer festen Taktungsstunde für die folgenden Fehlertypen gespeichert:
    - Live-Activity-Fehler (No push credential)
    - Live-Activity-Fehler (Invalid push credential)
    - Andere Live-Activity-Fehler
    - APNS Feedback Removed Token-Fehler
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

Testversandprotokolle sind mit dem Präfix „[TEST SEND]“ versehen, es ist jedoch nicht garantiert, dass alle Testversandprotokolle dieses Präfix enthalten (z. B. haben Connected-Content-Fehler das Präfix nicht).