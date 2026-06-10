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

- [Beschreibungen der Braze Action Credits](#braze-action-credits-descriptions)
  - [Details zum E-Mail-Kanal](#email-channel-details)
  - [Details zu SMS-, MMS- und RCS-Kanälen](#sms-mms-and-rcs-channel-details)
    - [SMS-Segmente](#sms-segments)
    - [MMS-Nachrichten](#mms-messages)
    - [RCS-Typen](#rcs-types)
  - [Details zum WhatsApp-Kanal](#whatsapp-channel-details)
    - [Aufschlüsselung nach Abrechnungsregion](#billing-region-breakdown)
  - [Details zur Agentenkonsole](#agent-console-details)
  - [Details zu weiteren Kanälen](#additional-channel-details)
    - [LINE](#line)
    - [KakaoTalk](#kakaotalk)
    - [Content Cards](#content-cards)
    - [Banner](#banners)
    - [Audience Sync](#audience-sync)
    - [Nachrichtenarchivierung](#message-archiving)
    - [Webhooks](#webhooks)

## Details zum E-Mail-Kanal {#email-channel-details}

Die Credit-Verhältnisse für E-Mails werden in Schritten von eintausend über die Braze-Plattform gesendeten E-Mails (CPM) berechnet.

{% alert note %}
Weitere Informationen zu unserem E-Mail-Kanal finden Sie in unserer [E-Mail-Dokumentation](https://www.braze.com/docs/user_guide/message_building_by_channel/email).
{% endalert %}

## Details zu SMS-, MMS- und RCS-Kanälen {#sms-mms-and-rcs-channel-details}

Die Credit-Verhältnisse für SMS und MMS werden in Schritten von eingehenden oder ausgehenden Segmenten berechnet, die über die Braze-Plattform gesendet werden. Die Credit-Verhältnisse für RCS werden in Schritten von Basic- oder Single-Typen berechnet, die über die Braze-Plattform gesendet werden.

{% alert note %}
Sofern für diese Kanäle zutreffend, werden Carrier-Gebühren separat (nachträglich) in Rechnung gestellt und sind nicht Bestandteil der Action Credits.
{% endalert %}

### SMS-Segmente {#sms-segments}

In der SMS-Branche werden Nachrichten in SMS-Nachrichten-Segmenten gezählt. Ein Nachrichten-Segment ist eine Gruppierung von bis zu einer definierten Anzahl von Zeichen (160 für GSM-7-Kodierung; 67 für UCS-2-Kodierung), die in einem einzelnen SMS-Versand gesendet wird. Wenn Sie eine SMS mit 161 Zeichen unter Verwendung der GSM-7-Kodierung versenden, werden zwei (2) Nachrichten-Segmente gesendet. Das Senden mehrerer Nachrichten-Segmente führt zu zusätzlichen Kosten.

### MMS-Nachrichten {#mms-messages}

Für MMS beträgt das Nachrichtenlimit 5 MB (dies umfasst das Multimedia-Asset und die Größe des Nachrichtentexts). Um auf der sicheren Seite zu sein, empfiehlt Braze, 600 KB für Ihr Multimedia-Asset nicht zu überschreiten und gleichzeitig einen Nachrichtentext einzuschließen.

### RCS-Typen {#rcs-types}

RCS ist die nächste Generation von SMS und MMS. Es bietet die Vorteile eines direkten Kanals mit hohem Engagement wie SMS – mit umfangreicheren Funktionen, die moderne Verbraucher:innen erwarten, wie Rich Content (Bilder, Videos, Dokumente), verifizierter und gebrandeter Versand, interaktive Features wie vorgeschlagene Antworten und Aktionen und mehr.

- Die RCS-Abrechnung basiert auf zwei verschiedenen Nachrichtentypen (mit Unterscheidungen für die USA):
    - **Basic RCS:** Nur Text, bis zu 160 Zeichen
    - **Single RCS:** Nachrichten mit Rich Content oder reine Textnachrichten mit mehr als 160 Zeichen
    - **Rich RCS (nur USA):** Nur Text, kann eingeschränkte Vorschläge/Buttons enthalten (quickReply, dialPhone, openURL ohne Webview), segmentiert pro 160 UTF-8-Bytes
    - **Rich Media RCS (nur USA):** Beliebige Medien ODER Text mit umfangreicheren Vorschlägen/Buttons (Webview, Standort, Kalender usw.), wird als eine Nachricht gezählt

{% alert note %}
Weitere Informationen zu unseren SMS-Angeboten finden Sie in unserer [SMS- und MMS-Dokumentation](https://www.braze.com/docs/user_guide/message_building_by_channel/sms).
{% endalert %}

## Details zum WhatsApp-Kanal {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

### Aufschlüsselung nach Abrechnungsregion {#billing-region-breakdown}

#### Nordamerika {#north-america}

Vereinigte Staaten, Kanada

#### Übriges Afrika {#rest-of-africa}

Algerien, Angola, Benin, Botswana, Burkina Faso, Burundi, Kamerun, Tschad, Kongo, Eritrea, Äthiopien, Gabun, Gambia, Ghana, Guinea-Bissau, Elfenbeinküste, Kenia, Lesotho, Liberia, Libyen, Madagaskar, Malawi, Mali, Mauretanien, Marokko, Mosambik, Namibia, Niger, Ruanda, Senegal, Sierra Leone, Somalia, Südsudan, Sudan, Swasiland, Tansania, Togo, Tunesien, Uganda, Sambia

#### Übriger asiatisch-pazifischer Raum {#rest-of-asia-pacific}

Afghanistan, Australien, Bangladesch, Kambodscha, China, Hongkong, Japan, Laos, Mongolei, Nepal, Neuseeland, Papua-Neuguinea, Philippinen, Singapur, Sri Lanka, Taiwan, Tadschikistan, Thailand, Turkmenistan, Usbekistan, Vietnam

#### Übriges Mittel- und Osteuropa {#rest-of-central-eastern-europe}

Albanien, Armenien, Aserbaidschan, Belarus, Bulgarien, Kroatien, Tschechische Republik, Georgien, Griechenland, Ungarn, Lettland, Litauen, Mazedonien, Moldawien, Polen, Rumänien, Serbien, Slowakei, Slowenien, Ukraine

#### Übriges Lateinamerika {#rest-of-latin-america}

Bolivien, Costa Rica, Dominikanische Republik, Ecuador, El Salvador, Guatemala, Haiti, Honduras, Jamaika, Nicaragua, Panama, Paraguay, Puerto Rico, Uruguay, Venezuela

#### Übriger Naher Osten {#rest-of-middle-east}

Bahrain, Irak, Jordanien, Kuwait, Libanon, Oman, Katar, Jemen

#### Übriges Westeuropa {#rest-of-western-europe}

Österreich, Belgien, Dänemark, Finnland, Irland, Norwegen, Portugal, Schweden, Schweiz

{% alert note %}
Weitere Informationen zu unseren WhatsApp-Angeboten finden Sie in unserer [WhatsApp-Dokumentation](https://www.braze.com/docs/user_guide/message_building_by_channel/whatsapp).
{% endalert %}

## Details zur Agentenkonsole {#agent-console-details}

Die Credit-Verhältnisse für die Agentenkonsole werden in Schritten von eintausend (1.000) über die Braze-Plattform durchgeführten Invocations berechnet. Eine Invocation wird protokolliert, wenn ein Agent einen Aufruf an ein LLM initiiert. Standardmäßig enthält Ihr Vertrag ein Kontingent an Invocations, wie in Ihrer Platform Edition für jeden Zeitraum Ihrer Abo-Laufzeit festgelegt. Zusätzliche Invocations werden gemäß Ihrem Bestellformular berechnet.

{% alert note %}
Weitere Informationen zur Agentenkonsole finden Sie in unserer [Braze-Agents-Dokumentation](https://www.braze.com/docs/user_guide/brazeai/agents).
{% endalert %}

## Details zu weiteren Kanälen {#additional-channel-details}

### LINE {#line}

Die Credit-Verhältnisse für LINE werden in Schritten von über die Braze-Plattform gesendeten LINE-Nachrichten berechnet.

{% alert note %}
Weitere Informationen zur Verwendung von LINE mit Braze finden Sie in unserer [LINE-Dokumentation](https://www.braze.com/docs/user_guide/message_building_by_channel/line).
{% endalert %}

### KakaoTalk {#kakaotalk}

Die Credit-Verhältnisse für KakaoTalk werden in Schritten von über die Braze-Plattform gesendeten KakaoTalk-Nachrichten berechnet.

{% alert note %}
Weitere Informationen zur Verwendung von KakaoTalk mit Braze finden Sie in unserer [KakaoTalk-Dokumentation](https://braze.com/docs/kakaotalk/).
{% endalert %}

### Content Cards {#content-cards}

Die Credit-Verhältnisse für Content Cards werden in Schritten von eintausend täglichen eindeutigen Impressionen berechnet.

Braze behält sich das Recht vor, Credits für Content Cards basierend auf der Anzahl der gesendeten Content Cards zu berechnen, wenn die Kundin oder der Kunde Content Cards nicht so einrichtet, dass eindeutige Impressionen gemäß den Richtlinien von Braze protokolliert werden. Dies gilt als zutreffend, wenn die Kundin oder der Kunde innerhalb von sechs (6) Monaten nach dem ersten Versand von Content Cards:
- Mehr als fünf Millionen (5.000.000) Content Cards gesendet hat, UND ENTWEDER
    - Null (0) Impressionen aufgezeichnet wurden
    - Das Verhältnis von Sendungen zu täglichen eindeutigen Impressionen größer als einhundert (100) ist

{% alert note %}
Weitere Informationen zu Braze Content Cards finden Sie in unserer [Content-Cards-Dokumentation](https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards).
{% endalert %}

### Banner {#banners}

Die Credit-Verhältnisse für Banner werden in Schritten von eintausend täglichen eindeutigen Impressionen berechnet.

{% alert note %}
Weitere Informationen zu Braze-Bannern finden Sie in unserer [Banner-Dokumentation](https://braze.com/docs/developer_guide/banner_cards).
{% endalert %}

### Audience Sync {#audience-sync}

Die Credit-Verhältnisse für Audience Sync werden in Schritten von eintausend synchronisierten Nutzer:innen insgesamt berechnet. Standardmäßig enthält Ihr Vertrag fünf Millionen Nutzer:innen-Synchronisierungen pro Zeitraum Ihrer Abo-Laufzeit. Zusätzliche Nutzer:innen-Synchronisierungen werden gemäß Ihrem Bestellformular berechnet.

{% alert note %}
Weitere Informationen zu Canvas Audience Sync und verfügbaren Partnern finden Sie in unserer [Canvas-Dokumentation](https://www.braze.com/docs/partners/canvas_steps).
{% endalert %}

### Nachrichtenarchivierung {#message-archiving}

Die Credit-Verhältnisse für die Nachrichtenarchivierung werden in Schritten von eintausend archivierten Nachrichten über Push-, E-Mail- und SMS/MMS-Kanäle berechnet.

{% alert note %}
Weitere Informationen zur Nachrichtenarchivierung finden Sie in unserer [Dokumentation zur Nachrichtenarchivierung](https://www.braze.com/docs/user_guide/data/export_braze_data/message_archiving#message-archiving).
{% endalert %}

### Webhooks {#webhooks}

Die Credit-Verhältnisse für Webhooks werden in Schritten von eintausend über die Braze-Plattform gesendeten Webhooks berechnet. Standardmäßig enthält Ihr Vertrag einhunderttausend Webhooks pro Zeitraum Ihrer Abo-Laufzeit. Zusätzliche Webhooks werden gemäß Ihrem Bestellformular berechnet.

{% alert note %}
Weitere Informationen zu Braze-Webhooks finden Sie in unserer [Webhooks-Dokumentation](https://www.braze.com/docs/user_guide/message_building_by_channel/webhooks).
{% endalert %}