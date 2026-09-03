---
nav_title: "SMS, MMS und RCS"
article_title: "SMS, MMS und RCS"
page_order: 8
page_type: landing
channel:
  - SMS
  - MMS
  - RCS
search_rank: 3
description: "Diese Landing-Page ist die Anlaufstelle für SMS (Short Messaging Service), MMS (Multimedia Messaging Service) und RCS (Rich Communication Services). Diese Dienste bieten einen direkteren Weg, Ihre Nutzer:innen zu erreichen, als die meisten anderen Messaging-Kanäle, da sie die Telefonnummer nutzen und so eine Realtime-Kommunikation ermöglichen."
---

# SMS, MMS und RCS {#sms-mms-and-rcs}

> SMS (Short Messaging Service), MMS (Multimedia Messaging Service) und RCS (Rich Communication Services) bieten einen direkten Weg, Ihre Nutzer:innen über ihre Telefonnummern in Echtzeit zu erreichen. SMS ist nach wie vor einer der weltweit am häufigsten genutzten Kanäle, weil der Kanal schnell, vertraut und effektiv für zeitkritische Informationen ist. Dieser Hub behandelt die Sender-Einrichtung, Compliance, das Erfassen von Opt-ins, die Nachrichtenerstellung und das Reporting für SMS, MMS und RCS in Braze. Lesen Sie [Gesetze und Vorschriften]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) und [Opt-ins von Nutzer:innen erfassen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins), bevor Sie Ihre erste Nachricht senden.

## Voraussetzungen {#prerequisites}

Die Verfügbarkeit von SMS, MMS und RCS hängt von Ihrem Braze-Paket ab. Wenden Sie sich an Ihren Account Manager oder Customer-Success-Manager, um loszulegen.

Bevor Sie beginnen, stellen Sie sicher, dass Folgendes vorhanden ist:

- Shortcodes, Langcodes oder alphanumerische Absender-IDs sind konfiguriert. Weitere Informationen finden Sie unter [Sender einrichten]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).
- Vertrautheit mit SMS-Gesetzen und -Vorschriften, einschließlich TCPA und Anforderungen der Mobilfunkanbieter. Weitere Informationen finden Sie unter [Gesetze und Vorschriften]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).
- Ausdrückliche Opt-in-Einwilligung der Nutzer:innen eingeholt. Weitere Informationen finden Sie unter [Opt-ins von Nutzer:innen erfassen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins).

## Anwendungsfälle {#use-cases}

| Anwendungsfall | Erklärung |
| --- | --- |
| Terminerinnerungen | Senden Sie rechtzeitig Erinnerungen vor geplanten Terminen, um Nichterscheinen zu reduzieren und Kund:innen auf dem Laufenden zu halten. |
| Bestellaktualisierungen | Benachrichtigen Sie Kund:innen in Echtzeit über Bestellbestätigungen, Versandstatus und Zustellungsupdates. |
| Zwei-Faktor-Authentifizierung | Stellen Sie Einmal-Verifizierungscodes für die Kontoanmeldung und Transaktionsbestätigung bereit. |
| Aktionsangebote | Erreichen Sie Kund:innen mit zeitlich begrenzten Aktionen, Flash-Sales und personalisierten Rabatten direkt auf ihrem Telefon. |
| Kundensupport | Ermöglichen Sie bidirektionale Konversationen, um Kundenanfragen zu lösen, Feedback zu sammeln oder Serviceanfragen zu bestätigen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

## SMS, MMS und RCS im Vergleich {#sms-mms-and-rcs-compared}

- **SMS** übermittelt reine Textnachrichten mit bis zu 160 Zeichen (oder 70 Zeichen mit Unicode). SMS wird von allen Mobilgeräten und Mobilfunkanbietern universell unterstützt.
- **MMS** erweitert SMS um Multimedia-Inhalte wie Bilder, GIFs und Audio. MMS erfordert Unterstützung durch den Mobilfunkanbieter und das Gerät.
- **RCS** ist die nächste Generation des Business-Messaging und bietet umfangreiche Features wie gebrandete Senderprofile, vorgeschlagene Antworten, Karussells und Lesebestätigungen. Die Verfügbarkeit von RCS hängt von der Unterstützung durch Mobilfunkanbieter und Gerät ab.

### Warum RCS verwenden? {#why-use-rcs}

RCS (Rich Communication Services) baut auf SMS auf und bietet ein reichhaltigeres, App-ähnliches Erlebnis in der Standard-Messaging-App auf unterstützten Geräten. Marken nutzen RCS, um:

- Hochauflösende Bilder und Videos statt reinem Text zu übermitteln.
- Vorgeschlagene Antworten und Aktionen hinzuzufügen, damit Kund:innen mit einem Tipp antworten können.
- Ein verifiziertes Senderprofil mit Branding anzuzeigen, damit Nachrichten leicht als vertrauenswürdig erkennbar sind.
- Lesebestätigungen und Tipp-Indikatoren zu unterstützen, wo Mobilfunkanbieter dies ermöglichen.

RCS eignet sich für Anwendungsfälle wie transaktionale Updates (Versand, Termine), Aktionen mit ansprechenden Creatives, Kundensupport mit Quick-Reply-Pfaden sowie Onboarding oder Tutorials, die von Medien und strukturierten Aktionen profitieren. Informationen zur Einrichtung und Migration von SMS finden Sie unter [RCS-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Brauche ich eine Opt-in-Einwilligung, bevor ich SMS in Braze sende? {#do-i-need-opt-in-consent-before-sending-sms-in-braze}

Ja. Holen Sie eine ausdrückliche Opt-in-Einwilligung ein und befolgen Sie geltende Gesetze wie den TCPA und die Anforderungen der Mobilfunkanbieter. Weitere Informationen finden Sie unter [Nutzer:innen-Opt-ins sammeln]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) und [Gesetze und Vorschriften]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### Was ist der Unterschied zwischen SMS, MMS und RCS? {#what-is-the-difference-between-sms-mms-and-rcs}

SMS versendet reine Textnachrichten, MMS fügt Multimedia wie Bilder hinzu und RCS bietet umfangreiche Features wie gebrandete Senderprofile und vorgeschlagene Antworten auf unterstützten Geräten. Weitere Informationen finden Sie im Abschnitt **SMS, MMS und RCS im Vergleich** weiter oben auf dieser Seite.

### Wie konfiguriere ich Sendernummern für SMS? {#how-do-i-configure-sender-numbers-for-sms}

Richten Sie Shortcodes, Langcodes oder alphanumerische Sender-IDs in Braze ein, bevor Sie Kampagnen starten. Weitere Informationen finden Sie unter [Sender-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Nächste Schritte {#next-steps}

- [Nachrichteneinrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup)
- [Eine Nachricht erstellen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)