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
description: "Erfahren Sie mehr über SMS, MMS und RCS in Braze, einschließlich Einrichtung, Compliance und Best Practices, um Nutzer:innen über ihre Telefonnummer zu erreichen."
---

# SMS, MMS und RCS {#sms-mms-and-rcs}

> SMS (Short Messaging Service), MMS (Multimedia Messaging Service) und RCS (Rich Communication Services) bieten einen direkten Weg, Ihre Nutzer:innen über ihre Telefonnummern in Echtzeit zu erreichen. SMS ist nach wie vor einer der weltweit am häufigsten genutzten Kanäle, weil der Kanal schnell, vertraut und effektiv für zeitkritische Informationen ist. Dieser Hub behandelt die Sender-Einrichtung, Compliance, das Erfassen von Opt-ins, die Nachrichtenerstellung und das Reporting für SMS, MMS und RCS in Braze. Lesen Sie [Gesetze und Vorschriften]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) und [Opt-ins von Nutzer:innen erfassen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins), bevor Sie Ihre erste Nachricht senden.

## Voraussetzungen {#prerequisites}

Die Verfügbarkeit von SMS, MMS und RCS hängt von Ihrem Braze-Paket ab. Wenden Sie sich an Ihren Account Manager oder Customer-Success-Manager, um loszulegen.

Bevor Sie beginnen, stellen Sie sicher, dass Sie Folgendes haben:

- Shortcodes, Langcodes oder alphanumerische Sender-IDs konfiguriert. Weitere Informationen finden Sie unter [Sender-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).
- Vertrautheit mit SMS-Gesetzen und -Vorschriften, einschließlich TCPA und Anforderungen der Mobilfunkanbieter. Weitere Informationen finden Sie unter [Gesetze und Vorschriften]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).
- Ausdrückliche Opt-in-Einwilligung der Nutzer:innen eingeholt. Weitere Informationen finden Sie unter [Opt-ins der Nutzer:innen erfassen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins).

## Anwendungsfälle {#use-cases}

| Anwendungsfall | Erklärung |
| --- | --- |
| Terminerinnerungen | Senden Sie rechtzeitige Erinnerungen vor geplanten Terminen, um Nichterscheinen zu reduzieren und Kund:innen auf dem Laufenden zu halten. |
| Bestellaktualisierungen | Benachrichtigen Sie Kund:innen in Echtzeit über Bestellbestätigungen, Versandstatus und Lieferaktualisierungen. |
| Zwei-Faktor-Authentifizierung | Übermitteln Sie Einmalcodes zur Verifizierung bei der Kontoanmeldung und Transaktionsbestätigung. |
| Aktionsangebote | Erreichen Sie Kund:innen mit zeitlich begrenzten Aktionen, Flash-Sales und personalisierten Rabatten direkt auf ihrem Telefon. |
| Kundensupport | Ermöglichen Sie bidirektionale Konversationen, um Kundenanfragen zu klären, Feedback zu sammeln oder Serviceanfragen zu bestätigen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

## SMS, MMS und RCS im Vergleich {#sms-mms-and-rcs-compared}

- **SMS** sendet reine Textnachrichten mit bis zu 160 Zeichen (oder 70 Zeichen bei Unicode). SMS wird universell auf allen Mobilgeräten und bei allen Mobilfunkanbietern unterstützt.
- **MMS** erweitert SMS um Unterstützung für Multimedia-Inhalte, darunter Bilder, GIFs und Audio. MMS erfordert Unterstützung durch den Mobilfunkanbieter und das Gerät.
- **RCS** ist die nächste Generation des Business-Messagings und bietet umfangreiche Features wie gebrandete Absenderprofile, vorgeschlagene Antworten, Karussells und Lesebestätigungen. Die Verfügbarkeit von RCS hängt von der Unterstützung durch den Mobilfunkanbieter und das Gerät ab.

### Warum RCS verwenden? {#why-use-rcs}

RCS (Rich Communication Services) baut auf SMS auf und bietet ein reichhaltigeres, App-ähnliches Erlebnis in der Standard-Messaging-App auf unterstützten Geräten. Marken nutzen RCS, um:

- Hochauflösende Bilder und Videos anstelle von reinem Text zu senden.
- Vorgeschlagene Antworten und Aktionen hinzuzufügen, damit Kund:innen mit einem Tippen antworten können.
- Ein verifiziertes Absenderprofil mit Branding anzuzeigen, damit Nachrichten leicht als vertrauenswürdig erkannt werden.
- Lesebestätigungen und Tipp-Indikatoren zu unterstützen, sofern der Mobilfunkanbieter dies erlaubt.

RCS eignet sich für Anwendungsfälle wie transaktionale Updates (Versand, Termine), Aktionen mit ansprechenden Kreativ-Inhalten, Kundensupport mit Schnellantwort-Pfaden sowie Onboarding oder Tutorials, die von Medien und strukturierten Aktionen profitieren. Informationen zur Einrichtung und Migration von SMS finden Sie unter [RCS-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Benötige ich eine Opt-in-Einwilligung, bevor ich SMS in Braze sende? {#do-i-need-opt-in-consent-before-sending-sms-in-braze}

Ja. Holen Sie eine ausdrückliche Opt-in-Einwilligung ein und halten Sie geltende Gesetze wie TCPA und Anforderungen der Mobilfunkanbieter ein. Weitere Informationen finden Sie unter [Opt-ins der Nutzer:innen erfassen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) und [Gesetze und Vorschriften]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### Was ist der Unterschied zwischen SMS, MMS und RCS? {#what-is-the-difference-between-sms-mms-and-rcs}

SMS sendet reine Textnachrichten, MMS ergänzt Multimedia-Inhalte wie Bilder, und RCS bietet erweiterte Features wie gebrandete Senderprofile und vorgeschlagene Antworten auf unterstützten Geräten. Siehe **SMS, MMS und RCS im Vergleich** weiter oben auf dieser Seite.

### Wie konfiguriere ich Sendernummern für SMS? {#how-do-i-configure-sender-numbers-for-sms}

Richten Sie Shortcodes, Langcodes oder alphanumerische Sender-IDs in Braze ein, bevor Sie Kampagnen starten. Weitere Informationen finden Sie unter [Sender-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Nächste Schritte {#next-steps}

{% article_tiles %}
- name: Nachrichteneinrichtung
  link: /docs/user_guide/channels/sms_mms_and_rcs/message_setup
  description: Konfigurieren Sie Absendernummern, Compliance-Einstellungen und Kanalvoraussetzungen, bevor Sie senden.
- name: Nachricht erstellen
  link: /docs/user_guide/channels/sms_mms_and_rcs/create
  description: Erstellen und starten Sie SMS-, MMS- oder RCS-Campaigns in Braze.
{% endarticle_tiles %}