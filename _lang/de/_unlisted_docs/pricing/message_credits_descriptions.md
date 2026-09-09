---
nav_title: Beschreibungen der Braze Action Credits
permalink: "/message_credits_descriptions/"
hidden: true
noindex: true
hide_toc: true
---

# Beschreibungen der Braze Action Credits {#braze-action-credits-descriptions}

> Action Credits bieten eine flexible Struktur, mit der Sie problemlos auf Multi-Channel-Messaging und fortschrittliche KI-Produkte zugreifen und gleichzeitig Ihr Marketingbudget optimal nutzen können. Beginnen Sie mit dem Engagement auf einem einzelnen Kanal oder in einer Region und erweitern Sie Ihren Mix nahtlos um KI-Agenten, wenn sich Ihr Geschäftsmodell, Ihre Kundenbasis und Ihre Engagement-Strategien weiterentwickeln.

Action Credits können auf alle auf dieser Seite aufgeführten Kanäle und Features angewendet werden.

Beachten Sie, dass das auf dieser Seite referenzierte „Credit-Verhältnis“ als die genaue Anzahl von Action Credits definiert ist, die für die Durchführung der angegebenen Aktion erforderlich sind.

## Inhaltsverzeichnis {#table-of-contents}

- [E-Mail-Kanaldetails](#email-channel-details)
- [SMS-, MMS- und RCS-Kanaldetails](#sms-mms-and-rcs-channel-details)
  - [SMS-Nachrichtensegmente](#sms-segments)
  - [MMS-Nachrichten](#mms-messages)
  - [RCS-Typen](#rcs-types)
- [WhatsApp-Kanaldetails](#whatsapp-channel-details)
  - [Aufschlüsselung nach Abrechnungsregion](#billing-region-breakdown)
- [Agent Console-Details](#agent-console-details)
- [Weitere Kanaldetails](#additional-channel-details)
  - [LINE](#line)
  - [KakaoTalk](#kakaotalk)
  - [Content Cards](#content-cards)
  - [Banner](#banners)
  - [Audience Sync](#audience-sync)
  - [Nachrichtenarchivierung](#message-archiving)
  - [Webhooks](#webhooks)

## Details zum E-Mail-Kanal {#email-channel-details}

E-Mail-Guthabenverhältnisse werden in Schritten von eintausend gesendeten E-Mails (CPM) von der Braze-Plattform berechnet.

{% alert note %}
Weitere Informationen zu unserem E-Mail-Kanal finden Sie in unserer [E-Mail-Dokumentation]({{site.baseurl}}/user_guide/channels/email).
{% endalert %}

## SMS-, MMS- und RCS-Kanaldetails {#sms-mms-and-rcs-channel-details}

Die Anrechnungsverhältnisse für SMS- und MMS-Credits werden in Schritten gesendeter Nachrichtensegmente über die Braze-Plattform berechnet. Die Anrechnungsverhältnisse für RCS-Credits werden in Schritten von Basic- und Rich-Media-Typen oder Single- und Rich-Media-Typen berechnet, die über die Braze-Plattform zugestellt werden. Sowohl eingehende als auch ausgehende Typen werden abgerechnet.

{% alert note %}
Sofern für diese Kanäle zutreffend, werden Mobilfunkanbieter-Gebühren separat (nachträglich) in Rechnung gestellt und nicht als Teil der Action Credits betrachtet.
{% endalert %}

### SMS-Nachrichtensegmente {#sms-segments}

In der SMS-Branche werden Nachrichten in SMS-Nachrichtensegmenten gezählt. Ein Nachrichtensegment ist eine Gruppierung von bis zu einer festgelegten Zeichenanzahl (160 für GSM-7-Kodierung; 67 für UCS-2-Kodierung), die in einem einzelnen SMS-Versand gesendet wird. Wenn Sie eine SMS mit 161 Zeichen in GSM-7-Kodierung versenden, werden zwei (2) Nachrichtensegmente gesendet. Das Senden mehrerer Nachrichtensegmente führt zu zusätzlichen Kosten.

### MMS-Nachrichten {#mms-messages}

Für MMS liegt das Nachrichtenlimit bei 5 MB (dies umfasst sowohl die Multimedia-Datei als auch die Größe des Nachrichtentexts). Um auf der sicheren Seite zu sein, empfiehlt Braze, 600 KB für Ihre Multimedia-Datei nicht zu überschreiten und gleichzeitig einen Nachrichtentext einzubeziehen.

### RCS-Typen {#rcs-types}

RCS ist die nächste Generation von SMS und MMS. Es bietet die Vorteile eines direkten Kanals mit hohem Engagement wie SMS – mit umfangreicheren Funktionen, die moderne Verbraucher:innen heute erwarten, wie Rich Content (Bilder, Videos, Dokumente), verifizierter und gebrandeter Versand, interaktive Features wie vorgeschlagene Antworten und Aktionen und mehr.

{% multi_lang_include pricing/rcs_billing_message_types.md %}

{% alert note %}
Weitere Informationen zu unserem SMS-Angebot finden Sie in unserer [SMS- und MMS-Dokumentation]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs).
{% endalert %}

## Details zum WhatsApp-Kanal {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

## Aufschlüsselung nach Abrechnungsregion {#billing-region-breakdown}

### Nordamerika {#north-america}

Vereinigte Staaten, Kanada

### Übriges Afrika {#rest-of-africa}

Algerien, Angola, Benin, Botswana, Burkina Faso, Burundi, Kamerun, Tschad, Kongo, Eritrea, Äthiopien, Gabun, Gambia, Ghana, Guinea-Bissau, Elfenbeinküste, Kenia, Lesotho, Liberia, Libyen, Madagaskar, Malawi, Mali, Mauretanien, Marokko, Mosambik, Namibia, Niger, Ruanda, Senegal, Sierra Leone, Somalia, Südsudan, Sudan, Eswatini, Tansania, Togo, Tunesien, Uganda, Sambia

### Übriger asiatisch-pazifischer Raum {#rest-of-asia-pacific}

Afghanistan, Australien, Bangladesch, Kambodscha, China, Japan, Laos, Mongolei, Nepal, Neuseeland, Papua-Neuguinea, Philippinen, Sri Lanka, Taiwan, Tadschikistan, Thailand, Turkmenistan, Usbekistan, Vietnam

### Übriges Mittel- und Osteuropa {#rest-of-central-eastern-europe}

Albanien, Armenien, Aserbaidschan, Belarus, Bulgarien, Kroatien, Tschechische Republik, Georgien, Griechenland, Lettland, Litauen, Nordmazedonien, Moldawien, Serbien, Slowakei, Slowenien, Ukraine

### Übriges Lateinamerika {#rest-of-latin-america}

Bolivien, Costa Rica, Dominikanische Republik, Ecuador, El Salvador, Guatemala, Haiti, Honduras, Jamaika, Nicaragua, Panama, Paraguay, Puerto Rico, Uruguay, Venezuela

### Übriger Naher Osten {#rest-of-middle-east}

Bahrain, Irak, Jordanien, Kuwait, Libanon, Oman, Jemen

### Übriges Westeuropa {#rest-of-western-europe}

Österreich, Belgien, Dänemark, Finnland, Irland, Norwegen, Portugal, Schweden, Schweiz

{% alert note %}
Weitere Informationen zu unseren WhatsApp-Angeboten finden Sie in unserer [WhatsApp-Dokumentation]({{site.baseurl}}/user_guide/channels/whatsapp).
{% endalert %}

## Agent Console – Details {#agent-console-details}

Die Guthabenverhältnisse der Agent Console werden in Schritten von eintausend (1.000) Invocations berechnet, die über die Braze-Plattform ausgeführt werden. Eine Invocation wird protokolliert, wenn ein Agent einen Aufruf an ein LLM initiiert. Standardmäßig enthält Ihr Vertrag ein Kontingent an Invocations, wie in Ihrer Platform Edition für jeden Zeitraum Ihrer Abonnementlaufzeit festgelegt. Zusätzliche Invocations werden gemäß Ihrem Bestellformular berechnet.

{% alert note %}
Weitere Informationen zur Agent Console finden Sie in unserer [Braze Agents-Dokumentation]({{site.baseurl}}/user_guide/brazeai/agents).
{% endalert %}

## Weitere Kanal-Details {#additional-channel-details}

### LINE {#line}

LINE-Credit-Verhältnisse werden in Schritten von über die Braze-Plattform gesendeten LINE-Nachrichten berechnet.

{% alert note %}
Weitere Informationen zur Nutzung von LINE mit Braze finden Sie in unserer [LINE-Dokumentation]({{site.baseurl}}/user_guide/channels/line).
{% endalert %}

### KakaoTalk {#kakaotalk}

KakaoTalk-Credit-Verhältnisse werden in Schritten von über die Braze-Plattform gesendeten KakaoTalk-Nachrichten berechnet.

{% alert note %}
Weitere Informationen zur Nutzung von KakaoTalk mit Braze finden Sie in unserer [KakaoTalk-Dokumentation]({{site.baseurl}}/kakaotalk).
{% endalert %}

### Content Cards {#content-cards}

Content-Cards-Credit-Verhältnisse werden in Schritten von eintausend täglichen eindeutigen Impressionen berechnet.

Braze behält sich das Recht vor, Credits für Content Cards auf Basis der Anzahl gesendeter Content Cards zu berechnen, wenn die Kundin oder der Kunde Content Cards nicht so einrichtet, dass eindeutige Impressionen gemäß den Braze-Richtlinien erfasst werden. Dies gilt als zutreffend, wenn die Kundin oder der Kunde innerhalb von sechs (6) Monaten nach dem ersten Versand von Content Cards:
- Mehr als fünf Millionen (5.000.000) Content Cards gesendet hat, UND ENTWEDER
    - Null (0) Impressionen erfasst wurden
    - Das Verhältnis von Sendungen zu täglichen eindeutigen Impressionen größer als einhundert (100) ist

{% alert note %}
Weitere Informationen zu Braze Content Cards finden Sie in unserer [Content-Cards-Dokumentation]({{site.baseurl}}/user_guide/channels/content_cards).
{% endalert %}

### Banner {#banners}

Banner-Credit-Verhältnisse werden in Schritten von eintausend täglichen eindeutigen Impressionen berechnet.

{% alert note %}
Weitere Informationen zu Braze-Bannern finden Sie in unserer [Banner-Dokumentation]({{site.baseurl}}/developer_guide/banners).
{% endalert %}

### Audience Sync {#audience-sync}

Audience-Sync-Credit-Verhältnisse werden in Schritten von eintausend synchronisierten Nutzer:innen insgesamt berechnet. Standardmäßig umfasst Ihr Vertrag fünf Millionen Nutzer:innen-Synchronisierungen pro Zeitraum Ihrer Abonnementlaufzeit. Zusätzliche Nutzer:innen-Synchronisierungen werden gemäß Ihrem Bestellformular berechnet.

{% alert note %}
Weitere Informationen zu Canvas Audience Sync und verfügbaren Partnern finden Sie in unserer [Canvas-Dokumentation]({{site.baseurl}}/partners/canvas_audience_sync).
{% endalert %}

### Nachrichtenarchivierung {#message-archiving}

Credit-Verhältnisse für die Nachrichtenarchivierung werden in Schritten von eintausend erfolgreich archivierten Nachrichten über die Kanäle Push, E-Mail, SMS/MMS und In-App Messages berechnet.

{% alert note %}
Ab dem 2. September 2026 werden fehlgeschlagene Archivierungsversuche von der Nutzungsabrechnung ausgeschlossen; nur erfolgreiche Archivierungen verbrauchen Action Credits. Diese Änderung betrifft keine vor dem 2. September 2026 abgerechnete Nutzung.
{% endalert %}

{% alert note %}
Weitere Informationen zur Nachrichtenarchivierung finden Sie in unserer [Dokumentation zur Nachrichtenarchivierung]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving).
{% endalert %}

### Webhooks {#webhooks}

Webhook-Credit-Verhältnisse werden in Schritten von eintausend erfolgreich über die Braze-Plattform gesendeten Webhooks berechnet. Standardmäßig umfasst Ihr Vertrag einhunderttausend Webhooks pro Zeitraum Ihrer Abonnementlaufzeit. Zusätzliche Webhooks werden gemäß Ihrem Bestellformular berechnet.

{% multi_lang_include pricing/webhook_failed_requests_billing.md credit_name='Action Credits' %}

{% alert note %}
Weitere Informationen zu Braze Webhooks finden Sie in unserer [Webhook-Dokumentation]({{site.baseurl}}/user_guide/channels/webhooks).
{% endalert %}