---
nav_title: Abrechnungsrechner
article_title: Abrechnungsrechner
page_order: 5
description: "Dieser Referenzartikel behandelt, was ein SMS-Segment ist, wie Segmente für die Abrechnung gezählt werden und was beim Erstellen von SMS- und RCS-Nachrichtentexten zu beachten ist."
page_type: reference
alias: /sms_rcs_billing_calculators/
tool:
  - Testing Tools
channel:
  - SMS
  - MMS
  - RCS

---

# SMS- und RCS-Abrechnungsrechner {#sms-and-rcs-billing-calculators}

> Bei Braze werden SMS-Nachrichten pro Nachrichten-Segment abgerechnet, während RCS-Nachrichten pro Nachricht berechnet werden. Wenn Sie verstehen, was ein SMS-Segment ausmacht und welche verschiedenen RCS-Abrechnungstypen es gibt, können Sie besser nachvollziehen, wie Ihre Abrechnung erfolgt, und unbeabsichtigte Mehrkosten vermeiden.

## SMS-Nachrichtentext und Nachrichtensegment-Rechner {#sms-message-copy-and-segment-calculator}

SMS-Nachrichten werden pro Nachrichtensegment abgerechnet. Zu verstehen, wie SMS-Nachrichten aufgeteilt werden, ist entscheidend für das Verständnis Ihrer Abrechnung.

### Was ist ein SMS-Nachrichtensegment? {#what-is-an-sms-segment}

Der Short Messaging Service (SMS) ist ein standardisiertes Kommunikationsprotokoll, das es Geräten ermöglicht, kurze Textnachrichten zu senden und zu empfangen. Er wurde so konzipiert, dass er „zwischen“ andere Signalisierungsprotokolle passt, weshalb die SMS-Nachrichtenlänge auf 160 7-Bit-Zeichen begrenzt ist, also 1120 Bits oder 140 Bytes. SMS-Nachrichtensegmente sind die Zeichenpakete, die Mobilfunkanbieter zur Messung von Textnachrichten verwenden. Nachrichten werden pro Nachrichtensegment abgerechnet, sodass Clients, die SMS nutzen, erheblich davon profitieren, die Feinheiten der Nachrichtenaufteilung zu verstehen.

Wenn Sie eine SMS-Campaign oder ein Canvas mit Braze erstellen, sind die Nachrichten, die Sie im Nachrichten-Editor verfassen, repräsentativ für das, was Ihre Nutzer:innen sehen könnten, wenn die Nachricht auf ihrem Telefon zugestellt wird. **Dies ist jedoch kein Indikator dafür, wie Ihre Nachricht in Segmente aufgeteilt wird und wie Sie letztendlich abgerechnet werden.** Es liegt in Ihrer Verantwortung zu verstehen, wie viele Segmente gesendet werden, und sich der möglichen Mehrkosten bewusst zu sein. Wir stellen Ihnen jedoch einige Ressourcen zur Verfügung, um dies zu erleichtern. Nutzen Sie unseren internen [Nachrichtensegment-Rechner](#segment-calculator).

![Wenn Sie eine SMS-Campaign oder ein Canvas mit Braze erstellen, sind die Nachrichten im Nachrichten-Editor repräsentativ für das, was Ihre Nutzer:innen sehen könnten. Dies ist jedoch kein Indikator dafür, wie Ihre Nachricht in Segmente aufgeteilt und abgerechnet wird. Nutzen Sie unseren internen Nachrichtensegment-Rechner.]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

#### Aufschlüsselung der Segmente {#segment-breakdown}

Das Zeichenlimit für **ein einzelnes SMS-Nachrichtensegment** beträgt 160 Zeichen ([GSM-7](https://en.wikipedia.org/wiki/GSM_03.38)-Kodierung) oder 70 Zeichen ([UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)-Kodierung), je nach Kodierungstyp. Die meisten Telefone und Netzwerke unterstützen jedoch die Verkettung und ermöglichen so längere SMS-Nachrichten von bis zu 1530 Zeichen (GSM-7) oder 670 Zeichen (UCS-2). Auch wenn eine Nachricht mehrere Segmente umfassen kann, wird sie – sofern sie diese Verkettungslimits nicht überschreitet – als eine einzelne Nachricht angezeigt und auch so gemeldet.

Wichtig zu beachten: **Sobald Sie das Zeichenlimit Ihres ersten Segments überschreiten, führen zusätzliche Zeichen dazu, dass Ihre gesamte Nachricht basierend auf neuen Zeichenlimits aufgeteilt und segmentiert wird**:
- **GSM-7-Kodierung**
    - Nachrichten, die das Limit von 160 Zeichen überschreiten, werden in Segmente zu je 153 Zeichen aufgeteilt und einzeln gesendet, dann auf dem Gerät der Empfänger:in wieder zusammengesetzt. Beispielsweise wird eine Nachricht mit 161 Zeichen als zwei Nachrichten gesendet – eine mit 153 Zeichen und die zweite mit 8 Zeichen.
- **UCS-2-Kodierung**
    - Wenn Sie Nicht-GSM-Zeichen wie Emojis, chinesische, koreanische oder japanische Schriftzeichen in SMS-Nachrichten verwenden, müssen diese Nachrichten über UCS-2-Kodierung gesendet werden. Nachrichten, die das anfängliche Segmentlimit von 70 Zeichen überschreiten, werden in Nachrichtensegmente zu je 67 Zeichen verkettet. Beispielsweise wird eine Nachricht mit 71 Zeichen als zwei Nachrichten gesendet – eine mit 67 Zeichen und die zweite mit 4 Zeichen.

Unabhängig vom Kodierungstyp hat jede von Braze gesendete SMS-Nachricht ein Limit von bis zu 10 Segmenten und ist kompatibel mit [Liquid-Templating]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid), [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), Emojis und Links.

{% tabs %}
{% tab GSM-7-Kodierung %}
| Zeichenanzahl | Wie viele Segmente? |
| -------------------- | ----------------- |
| 0–160 Zeichen | 1 Segment |
| 161–306 Zeichen | 2 Segmente |
| 307–459 Zeichen | 3 Segmente |
| 460–612 Zeichen | 4 Segmente |
| 613–765 Zeichen | 5 Segmente |
| 766–918 Zeichen | 6 Segmente |
| 919–1071 Zeichen | 7 Segmente |
| 1072–1224 Zeichen | 8 Segmente |
| 1225–1377 Zeichen | 9 Segmente |
| 1378–1530 Zeichen | 10 Segmente |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aufschlüsselung der Segmente" }
{% endtab %}
{% tab UCS-2-Kodierung %}
| Zeichenanzahl | Wie viele Segmente? |
| -------------------- | ----------------- |
| 0–70 Zeichen | 1 Segment |
| 71–134 Zeichen | 2 Segmente |
| 135–201 Zeichen | 3 Segmente |
| 202–268 Zeichen | 4 Segmente |
| 269–335 Zeichen | 5 Segmente |
| 336–402 Zeichen | 6 Segmente |
| 403–469 Zeichen | 7 Segmente |
| 470–536 Zeichen | 8 Segmente |
| 537–603 Zeichen | 9 Segmente |
| 604–670 Zeichen | 10 Segmente |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aufschlüsselung der Segmente" }
{% endtab %}
{% endtabs %}

### Wichtige Hinweise für die Texterstellung {#things-to-keep-in-mind-as-you-create-your-copy}

- **Zeichenlimit pro Segment**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) hat ein Limit von 160 Zeichen für ein einzelnes SMS-Segment. Bei Nachrichten mit mehr als 160 Zeichen werden alle Nachrichten mit einem Limit von 153 Zeichen segmentiert.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) hat ein Limit von 70 Zeichen pro Nachrichtensegment. Bei Nachrichten mit mehr als 70 Zeichen werden alle Nachrichten mit einem Limit von 67 Zeichen segmentiert.<br><br>
- **Segmentlimit pro Nachricht**
    - Aufgrund der Einschränkungen des Mediums gibt es eine maximale Anzahl von Segmenten, die Sie senden können. In einer einzelnen Braze-SMS-Nachricht können nicht mehr als **10 Segmente** gesendet werden.
    - Diese 10 Segmente sind auf 1530 Zeichen (GSM-7-Kodierung) oder 670 Zeichen (UCS-2-Kodierung) begrenzt.<br><br>
- **Kompatibel mit Liquid-Templating, Connected Content, Emojis und Links**
    - Liquid-Templating und Connected Content können dazu führen, dass Ihre Nachricht das Zeichenlimit für Ihren Kodierungstyp überschreitet. Sie können den [truncate words-Filter](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) verwenden, um die Anzahl der Wörter zu begrenzen, die Liquid zu Ihrer Nachricht hinzufügen könnte.
    - Emojis haben keine standardisierte Zeichenanzahl über alle Emojis hinweg. Testen Sie daher immer, ob Ihre Nachrichten korrekt segmentiert und angezeigt werden.
    - Links können viele Zeichen beanspruchen, was zu mehr Nachrichtensegmenten als beabsichtigt führen kann. Obwohl die Verwendung von Link-Shortenern möglich ist, eignen sie sich am besten für Shortcodes. Weitere Informationen finden Sie in unseren [SMS-FAQ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs).<br><br>
- **Testen**
    - Testen Sie Ihre SMS-Nachrichten immer vor dem Versand, insbesondere bei Verwendung von Liquid und Connected Content, da das Überschreiten von Nachrichten- oder Textlimits zu zusätzlichen Kosten führen kann. Beachten Sie, dass Testnachrichten auf Ihre Nachrichtenlimits angerechnet werden.<br><br>
- **Automatische Antwortnachrichten**
    - Automatische Antwortnachrichten, die von Braze gesendet werden, wie z. B. Double-Opt-in-Bestätigungen und Antworten auf HELP-Schlüsselwörter, sind SMS-Sendungen, die als abrechenbare Segmente zählen. Die Anzahl der abrechenbaren Segmente hängt von der Textlänge und der Zeichenkodierung ab.

### SMS-Nachrichtensegment-Rechner {#segment-calculator}
---

{% multi_lang_include alerts/tip_alerts.md alert='SMS segment calculator' %}

## Abrechnung von RCS-Nachrichten {#rcs-message-billing}

RCS-Nachrichten werden basierend auf ihrem Inhalt und dem Land, in das die Nachricht zugestellt wird, abgerechnet. Um die Kosten genau abschätzen zu können, ist es wichtig, die verschiedenen Nachrichtentypen und deren Abrechnung zu verstehen.

### RCS-Abrechnungstypen {#rcs-billing-types}

Unsere Plattform unterstützt zwei primäre Abrechnungsmodelle: ein globales Modell und ein Modell für die Vereinigten Staaten.

#### Globales Modell (Nicht-US-Märkte) {#global-model-non-us-markets}

Nachrichten werden pro Nachricht abgerechnet und entweder als „Basic“ oder „Single“ klassifiziert.

{% tabs local %}
{% tab Basic %}

Basic-RCS-Nachrichten sind reine Textnachrichten mit bis zu 160 Zeichen und werden als einzelne Nachricht abgerechnet.

{% alert note %}
Das Hinzufügen von Buttons oder Rich-Elementen ändert den Nachrichtentyp zu einer Single-RCS-Nachricht.
{% endalert %}

{% endtab %}
{% tab Single %}

Single-RCS-Nachrichten sind Nachrichten, die über 160 Zeichen lang sind ODER Rich-Elemente wie Buttons oder Medien enthalten. Diese werden als einzelne Nachricht abgerechnet, unabhängig von der Nachrichtenlänge.

{% alert note %}
Das Senden einer Textnachricht und einer separaten Mediendatei wird dennoch als zwei separate Nachrichten abgerechnet.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Modell für die Vereinigten Staaten {#united-states-model}

Nachrichten werden entweder als „Rich“ oder „Rich Media“ kategorisiert.

{% tabs local %}
{% tab Rich-Nachrichten %}

Rich-Nachrichten sind reine Textnachrichten mit oder ohne Buttons. Sie werden pro Nachrichtensegment abgerechnet, wobei jedes Segment auf 160 UTF-8-Bytes begrenzt ist, was bedeutet, dass **die Anzahl der Zeichen pro Segment nicht festgelegt ist**. Eine Nachricht mit nur 160 einfachen englischen Zeichen ist ein Segment, aber eine Nachricht mit längerem Text und Emojis kann mehrere Segmente umfassen.

{% endtab %}
{% tab Rich-Media-Nachrichten %}

Rich-Media-Nachrichten enthalten eine Mediendatei (Bild, Video) oder eine Rich Card und werden als einzelne Nachricht abgerechnet.

{% endtab %}
{% endtabs %}

### Nachrichten-Editor und Credits-Usage-Dashboard {#message-composer-and-credits-usage-dashboard}

Während Sie Ihre Nachricht erstellen, zeigt der Nachrichten-Editor den Abrechnungstyp in Realtime über ein Label an (Basic RCS, Single RCS, Rich oder Rich Media), damit Sie die Kosten vor dem Versand im Blick behalten.

Ihr [Credits-Usage-Dashboard]({{site.baseurl}}/credits_usage_dashboard) spiegelt diese Abrechnungstypen wider und zeigt die Anzahl der verwendeten Segmente für US-Nachrichten an, sodass Sie einen transparenten Überblick über Ihren Nachrichtenkredit-Verbrauch erhalten.