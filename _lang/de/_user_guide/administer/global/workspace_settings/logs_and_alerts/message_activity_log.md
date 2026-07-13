---
nav_title: Nachrichten-Aktivitätsprotokoll
article_title: Nachrichten-Aktivitätsprotokoll
page_order: 3
page_type: reference
description: "Dieser Referenzartikel beschreibt das Nachrichten-Aktivitätsprotokoll, das Ihnen Nachrichten anzeigt, die mit Ihren Kampagnen und Sendungen verknüpft sind. Hier finden Sie auch Informationen darüber, wie Sie Protokollnachrichten verstehen können."

---

# Nachrichten-Aktivitätsprotokoll {#dev-console-troubleshooting}

> Das **Nachrichten-Aktivitätsprotokoll** gibt Ihnen die Möglichkeit, alle Nachrichten (insbesondere Fehlermeldungen) einzusehen, die mit Ihren Kampagnen und Sendungen verknüpft sind.

Sie können API-Kampagnen-Transaktionen einsehen, Details zu fehlgeschlagenen Nachrichten analysieren und Insights gewinnen, wie Sie die Zustellung von Benachrichtigungen verbessern oder bestehende technische Probleme lösen können.

Um auf das Protokoll zuzugreifen, gehen Sie zu **Einstellungen** > **Nachrichten-Aktivitätsprotokoll**.

![Nachrichten-Aktivitätsprotokoll]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
Zusätzlich zu diesem Artikel empfehlen wir Ihnen auch unseren Braze-Lernkurs [Quality Assurance and Debugging Tools](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), der erklärt, wie Sie das Nachrichten-Aktivitätsprotokoll für Ihre eigene Fehlerbehebung und Ihr Debugging nutzen können.
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

Um zu bestimmen, was Ihre Nachrichten bedeuten, achten Sie auf den Wortlaut jeder Nachricht und die zugehörigen Spalten, da Ihnen dies bei der Fehlerbehebung durch Kontexthinweise helfen kann.

Wenn Sie beispielsweise einen Protokolleintrag haben, dessen Nachricht „empty-cart_app“ lautet und Sie sich nicht sicher sind, was das bedeutet, schauen Sie links in die Spalte **Typ**. Wenn Sie „Aborted Message Error“ sehen, können Sie davon ausgehen, dass die Nachricht als [Abbruchnachricht]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages#abort-messages) mit Liquid geschrieben wurde und dass die Nachricht abgebrochen wurde, weil die vorgesehene Empfänger:in einen leeren Warenkorb in Ihrer App hatte.

### Häufige Nachrichten {#common-messages}

Es gibt einige häufige Nachrichtentypen, die Sie möglicherweise sehen, und einige bieten sogar Links zur Fehlerbehebung, die Ihnen bei der Diagnose und Behebung von Problemen helfen.

Die folgenden Nachrichten dienen als Beispiele und stimmen möglicherweise nicht genau mit dem überein, was in der Spalte **Nachricht** Ihres Protokolls angezeigt wird.

| Nachrichtentyp | Mögliche Nachricht | Beschreibung |
|---|---|---|
| Soft Bounce | The email address same@example.com soft bounced. | Die E-Mail-Adresse war gültig und die E-Mail-Nachricht erreichte den Mailserver der Empfänger:in, wurde aber aufgrund eines „vorübergehenden“ Problems abgelehnt. <br><br>Häufige Gründe für Soft Bounces sind: {::nomarkdown} <ul> <li> Das Postfach war voll (die Nutzer:in hat ihr Kontingent überschritten) </li> <li> Der Server war nicht erreichbar </li> <li> Die Nachricht war zu groß für den Posteingang der Empfänger:in </li>  </ul> {:/} Wenn eine E-Mail einen Soft Bounce erhalten hat, versuchen wir in der Regel innerhalb von 72 Stunden erneut zuzustellen, aber die Anzahl der Wiederholungsversuche variiert je nach Empfänger:in. |
| Hard Bounce | The email account that you tried to reach does not exist. Try double-checking the recipient's email address for typos or unnecessary spaces. | Ihre Nachricht hat den Posteingang dieser Person nie erreicht, weil kein Posteingang vorhanden war. Wenn Sie tiefer nachforschen möchten, können solche Nachrichten manchmal Links in der Spalte **Details anzeigen** enthalten, über die Sie das Profil der vorgesehenen Empfänger:in einsehen können.|
| Block | Spam message is rejected because of anti-spam policy. | Ihre Nachricht wurde als Spam eingestuft. Dieser E-Mail-Fehler wird für eine Nutzer:in protokolliert, wenn wir ein Ereignis vom ESP erhalten haben, das anzeigt, dass die E-Mail verworfen wurde. Es könnte nur für diese bestimmte Empfänger:in gelten, aber wenn Sie diese Nachricht häufig sehen, sollten Sie Ihre Sendegewohnheiten oder den Inhalt Ihrer Nachricht überprüfen. Denken Sie auch zurück – haben Sie [Ihre IP aufgewärmt]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)? Falls nicht, kontaktieren Sie Braze für Ratschläge, wie Sie damit beginnen können.|
| Aborted Message Error | empty-cart_web | Wenn Sie eine App mit einem Warenkorb haben oder eine Sendung mit einer Abbruchnachricht in Liquid erstellen, können Sie anpassen, welche Nachricht an Sie zurückgegeben wird, wenn die Sendung abgebrochen wird. In diesem Fall lautet die zurückgegebene Nachricht empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Häufige Nachrichten" }

### Warum ist meine Nachricht hier nicht aufgeführt? {#why-isnt-my-message-listed-here}

Die Nachrichten im Nachrichten-Aktivitätsprotokoll können aus verschiedenen Quellen stammen: Braze, Ihren Apps oder Plattformen oder unseren Drittanbieter-Partnern. Das bedeutet, dass es eine unbegrenzte Anzahl von Nachrichten gibt, die möglicherweise in diesem Protokoll erscheinen können – wie Sie sich vorstellen können, können wir nicht alle auflisten!

Zum Beispiel könnten einige mögliche „Block“-Nachrichten, zusätzlich zu der in der obigen Tabelle aufgeführten, sein:

- Unfortunately, messages from [_IP_ADDRESS_] weren't sent. Please contact your Internet Service provider since part of their network is on our block list.
- Message rejected due to local policy.
- The message was blocked by the receiver as spam.
- Service unavailable, Client host [_IP_ADDRESS_] blocked using Spamhaus.

## Aufbewahrungszeitraum {#storage-retention-period}

Fehler der letzten 60 Stunden sind in den Nachrichten-Aktivitätsprotokollen verfügbar. Protokolle, die älter als 60 Stunden sind, werden bereinigt und sind nicht mehr zugänglich.

### Anzahl der gespeicherten Fehlerprotokolle {#number-of-error-logs-stored}

Die Anzahl der gespeicherten Protokolle wird von mehreren Bedingungen beeinflusst. Wenn beispielsweise eine geplante Kampagne an Tausende von Nutzer:innen gesendet wird, würden wir möglicherweise nur eine Stichprobe der Fehler im Nachrichten-Aktivitätsprotokoll sehen, anstatt alle Fehler. Im Folgenden finden Sie eine Übersicht der Bedingungen, die beeinflussen, wie viele Protokolle gespeichert werden:
- Bis zu 20 Fehlerprotokolle desselben Fehlertyps werden für dieselbe Kampagne oder denselben Canvas-Schritt innerhalb einer festen Uhrstunde für die folgenden Fehlertypen gespeichert:
    - Connected-Content-Fehler
    - Fehler bei abgebrochenen Nachrichten
    - Webhook-Fehler
    - SMS-Ablehnungsfehler
    - SMS-Zustellungsfehler
    - WhatsApp-Fehler
    - A/B-Test-Fehler
- Bis zu 20 Push-Benachrichtigungs-Fehlerprotokolle desselben Fehlertyps werden für dieselbe Kampagne oder denselben Canvas-Schritt und dieselbe App-Kombination für die folgenden Fehlertypen gespeichert:
    - Ungültige Push-Zugangsdaten
    - Ungültiges Push-Token
    - Keine Push-Zugangsdaten
    - Token-Fehler
    - Kontingent überschritten
    - Zeitüberschreitung bei Wiederholungsversuchen
    - Ungültige Payload
    - Unerwarteter Fehler
- Bis zu 100 Fehlerprotokolle desselben Fehlertyps werden für dieselbe App innerhalb einer festen Uhrstunde für die folgenden Fehlertypen gespeichert:
    - Live-Activity-Fehler (Keine Push-Zugangsdaten)
    - Live-Activity-Fehler (Ungültige Push-Zugangsdaten)
    - Andere Live-Activity-Fehler
    - APNs-Feedback-Fehler bei entferntem Token
- Bis zu 100 Fehlerprotokolle desselben Fehlertyps werden für dieselbe Kampagne oder denselben Canvas-Schritt innerhalb einer festen Uhrstunde für die folgenden Fehlertypen gespeichert:
    - E-Mail-Soft-Bounce-Fehler
    - E-Mail-Hard-Bounce-Fehler
    - E-Mail-Block-Fehler
- Bis zu 100 User-Aliasing-Fehlerprotokolle werden für denselben Workspace innerhalb einer festen Uhrstunde gespeichert.

## Testsendungen {#test-sends}

Das **Nachrichten-Aktivitätsprotokoll** zeigt Testprotokolle für diese Messaging-Kanäle an:

- SMS
- WhatsApp
- LINE
- KakaoTalk
- Webhook

Testsendungsprotokolle sind für die folgenden Kanäle nicht verfügbar: E-Mail, Content Cards, In-App-Nachrichten und Push.

Testsendungsprotokolle sind mit dem Präfix „[TEST SEND]“ versehen, aber es ist nicht garantiert, dass alle Testsendungsprotokolle dieses Präfix haben (zum Beispiel haben Connected-Content-Fehler dieses Präfix nicht).