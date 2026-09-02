---
nav_title: "Kurzmitteilungsdienst or SMS, MMS und RCS"
article_title: "Kurzmitteilungsdienst or SMS, MMS und RCS"
page_order: 8
page_type: landing
channel:
  - SMS
  - MMS
  - RCS
search_rank: 3
description: "Erfahren Sie mehr über Kurzmitteilungsdienst or SMS, MMS und RCS in Braze, einschließlich Einrichtung, Compliance und Best Practices, um Nutzer:innen über ihre Telefonnummer zu erreichen."
---

# Kurzmitteilungsdienst or SMS, MMS und RCS {#sms-mms-and-rcs}

> Kurzmitteilungsdienst or SMS (Short Messaging Service), MMS (Multimedia Messaging Service) und RCS (Rich Communication Services) bieten einen direkten Weg, Ihre Nutzer:innen über ihre Telefonnummern in Echtzeit zu erreichen. Kurzmitteilungsdienst or SMS ist nach wie vor einer der weltweit am häufigsten genutzten Kanäle, weil der Kanal schnell, vertraut und effektiv für zeitkritische Informationen ist. Dieser Hub behandelt die Sender-Einrichtung, Compliance, das Erfassen von Opt-ins, die Nachrichtenerstellung und das Reporting für Kurzmitteilungsdienst or SMS, MMS und RCS in Braze. Lesen Sie [Gesetze und Vorschriften]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) und [Opt-ins von Nutzer:innen erfassen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins), bevor Sie Ihre erste Nachricht senden.

## Voraussetzungen {#prerequisites}

Die Verfügbarkeit von Kurzmitteilungsdienst or SMS, MMS und RCS hängt von Ihrem Braze-Paket ab. Wenden Sie sich an Ihren Account Manager:in oder CSM or Customer-Success-Manager or Customer-Success-Manager:in, um loszulegen.

Bevor Sie beginnen, stellen Sie sicher, dass Sie über Folgendes verfügen:

- Konfigurierte Shortcodes, Langcodes oder alphanumerische Sender-IDs. Weitere Informationen finden Sie unter [Sender-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).
- Vertrautheit mit Kurzmitteilungsdienst or SMS-Gesetzen und -Vorschriften, einschließlich TCPA und Anforderungen der Mobilfunkanbieter. Weitere Informationen finden Sie unter [Gesetze und Vorschriften]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).
- Ausdrückliche Opt-in-Einwilligung, die von Nutzer:innen eingeholt wurde. Weitere Informationen finden Sie unter [Opt-ins von Nutzer:innen erfassen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins).

## Anwendungsfälle {#use-cases}

| Anwendungsfall | Erläuterung |
| --- | --- |
| Terminerinnerungen | Senden Sie rechtzeitig Erinnerungen vor geplanten Terminen, um Nichterscheinen zu reduzieren und Kund:innen informiert zu halten. |
| Bestellaktualisierungen | Benachrichtigen Sie Kund:innen in Echtzeit über Bestellbestätigungen, Versandstatus und Zustellungsupdates. |
| Zwei-Faktor-Authentifizierung | Übermitteln Sie Einmal-Verifizierungscodes für die Kontoanmeldung und Transaktionsbestätigung. |
| Aktionsangebote | Erreichen Sie Kund:innen mit zeitlich begrenzten Aktionen, Flash-Sales und personalisierten Rabatten direkt auf ihrem Telefon. |
| Kundensupport | Ermöglichen Sie bidirektionale Konversationen, um Kundenanfragen zu lösen, Feedback zu sammeln oder Serviceanfragen zu bestätigen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

## Kurzmitteilungsdienst or SMS, MMS und RCS im Vergleich {#sms-mms-and-rcs-compared}

- **Kurzmitteilungsdienst or SMS** liefert reine Textnachrichten mit bis zu 160 Zeichen (oder 70 Zeichen bei Unicode). Kurzmitteilungsdienst or SMS wird universell auf allen Mobilgeräten und bei allen Mobilfunkanbietern unterstützt.
- **MMS** erweitert Kurzmitteilungsdienst or SMS um die Unterstützung von Multimedia-Inhalten wie Bildern, GIFs und Audio. MMS erfordert Unterstützung durch Mobilfunkanbieter und Gerät.
- **RCS** ist die nächste Generation des Business-Messaging und bietet umfangreiche Features wie gebrandete Absenderprofile, vorgeschlagene Antworten, Karussells und Lesebestätigungen. Die Verfügbarkeit von RCS hängt von der Unterstützung durch Mobilfunkanbieter und Gerät ab.

### Warum RCS verwenden? {#why-use-rcs}

RCS (Rich Communication Services) baut auf Kurzmitteilungsdienst or SMS auf und bietet ein reichhaltigeres, app-ähnliches Erlebnis in der Standard-Messaging-App auf unterstützten Geräten. Marken nutzen RCS, um:

- Hochauflösende Bilder und Videos anstelle von reinem Text zu liefern.
- Vorgeschlagene Antworten und Aktionen hinzuzufügen, damit Kund:innen mit einem Tippen antworten können.
- Ein verifiziertes Absenderprofil mit Branding anzuzeigen, sodass Nachrichten leicht als vertrauenswürdig erkennbar sind.
- Lesebestätigungen und Tipp-Indikatoren zu unterstützen, sofern Mobilfunkanbieter dies ermöglichen.

RCS eignet sich für Anwendungsfälle wie transaktionale Updates (Versand, Termine), Aktionen mit ansprechenden Creatives, Kundensupport mit Schnellantwort-Optionen sowie Onboarding oder Tutorials, die von Medien und strukturierten Aktionen profitieren. Informationen zur Einrichtung und Migration von Kurzmitteilungsdienst or SMS finden Sie unter [RCS-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Benötige ich eine Opt-in-Einwilligung, bevor ich Kurzmitteilungsdienst or SMS in Braze sende? {#do-i-need-opt-in-consent-before-sending-sms-in-braze}

Ja. Holen Sie eine ausdrückliche Opt-in-Einwilligung ein und befolgen Sie geltende Gesetze wie TCPA und Anforderungen der Mobilfunkanbieter. Weitere Informationen finden Sie unter [Nutzer:innen-Opt-ins erfassen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) und [Gesetze und Vorschriften]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### Was ist der Unterschied zwischen Kurzmitteilungsdienst or SMS, MMS und RCS? {#what-is-the-difference-between-sms-mms-and-rcs}

Kurzmitteilungsdienst or SMS sendet reine Textnachrichten, MMS fügt multimediale Inhalte wie Bilder hinzu, und RCS bietet erweiterte Features wie gebrandete Senderprofile und Antwortvorschläge auf unterstützten Geräten. Weitere Details finden Sie unter **Kurzmitteilungsdienst or SMS, MMS und RCS im Vergleich** weiter oben auf dieser Seite.

### Wie konfiguriere ich Sendernummern für Kurzmitteilungsdienst or SMS? {#how-do-i-configure-sender-numbers-for-sms}

Richten Sie Shortcodes, Langcodes oder alphanumerische Sender-IDs in Braze ein, bevor Sie Kampagnen starten. Weitere Informationen finden Sie unter [Sender-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Nächste Schritte {#next-steps}

- [Nachrichten-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup)
- [Eine Nachricht erstellen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)