---
nav_title: Sender-Einrichtung
article_title: SMS-, MMS- und RCS-Absender
page_order: 2
description: "Dieser Artikel bietet eine Übersicht über die Codes und Absender, die für den Versand von SMS-, MMS- und RCS-Nachrichten verfügbar sind."
page_type: reference
alias: /sending_phone_numbers/
channel:
  - SMS
  - MMS
  - RCS
---

{% multi_lang_include channels/sms/short_and_long_codes.md %}

## MMS-spezifische Anforderungen {#mms-specific-requirements}

### MMS-Absenderanforderungen {#mms-sender-requirements}

> MMS und SMS sind beide an den Braze-SMS-Kanal gebunden. Um MMS in Ihrem Konto nutzen zu können, ist der Kauf von SMS erforderlich, sofern Sie noch keinen Zugang erworben haben. Bestehende SMS-Kund:innen können nach dem Kauf auf MMS zugreifen.

MMS wird derzeit für US-Shortcodes (5–6-stellige Nummern), US- und CA-Langcodes (10-stellige Nummern) sowie US- und Kanada-Kundennummern unterstützt. MMS wird für gebührenfreie Nummern von bestimmten Dienstanbietern unterstützt.

Das Senden von MMS an Nummern außerhalb der USA und Kanadas ist möglich, allerdings werden MMS-Nachrichten in eine SMS-Nachricht mit einem Link zum Medien-Asset umgewandelt.

### MMS-Shortcodes {#mms-short-codes}

Einige Nutzer:innen implementieren oder verwenden möglicherweise keine MMS-Shortcodes, diese stehen jedoch bei Bedarf zu einem späteren Zeitpunkt zur Verfügung.

Für Nutzer:innen, die ihre Shortcodes erhalten haben, bevor Braze MMS unterstützte, sind alle bestehenden Kund:innen mit US-Shortcodes berechtigt, MMS sofort zu aktivieren. Wenden Sie sich an Ihren Customer-Success-Manager, wenn diese Situation auf Sie zutrifft und Sie MMS aktivieren möchten.

{% alert important %}
Beim Aktivieren von MMS für Shortcodes, bei denen MMS zuvor nicht aktiviert war, müssen die Shortcodes möglicherweise in einem Genehmigungsverfahren erneut genehmigt werden, das Wochen dauern kann. Es ist wichtig, diesen Zeitrahmen bei der Entscheidung zur Aktivierung von MMS zu berücksichtigen.
{% endalert %}

#### Best Practices für MMS-Shortcodes {#mms-short-code-best-practices}

- Bei Braze empfehlen wir dringend, transaktionsbezogenes und werbliches Messaging getrennt zu halten, jeweils mit unterschiedlichen Shortcodes. Da MMS an den SMS-Kanal gebunden ist und der SMS-Kanal stark reguliert ist, können Kund:innen bei Missbrauch des Kanals zu einer Geldstrafe verpflichtet werden und ihren Shortcode gesperrt bekommen (was nicht rückgängig gemacht werden kann). Die Trennung von transaktionsbezogenem und werblichem Messaging über verschiedene Shortcodes schützt das transaktionsbezogene Messaging.
- Wenn Kund:innen bereits einen Shortcode für werbliches Messaging haben und dieser MMS-fähig ist, benötigen sie keinen separaten Shortcode für MMS.

### MMS-Langcodes {#mms-long-codes}

Kund:innen können MMS mit Langcodes senden. Dazu müssen Sie sicherstellen, dass Ihre Langcodes MMS-fähig sind. Dies kann bei der Ersteinrichtung oder später innerhalb Ihres Kontos erfolgen.

MMS-Nachrichten können nicht mit einer alphanumerischen Absender-ID gesendet werden.

### MMS-Nachrichtenlimits und Durchsatz {#mms-message-limits-and-throughput}

Der MMS-Durchsatz beträgt ein Segment pro Sekunde über einen Langcode.

Mobilfunkanbieter legen ihre eigenen Dateigrößenlimits fest, die den Erfolg von MMS-Sendungen bestimmen. Diese Limits können je nach Geografie und Anbieter variieren, daher empfiehlt Braze, 600&nbsp;KB für Ihr Multimedia-Asset nicht zu überschreiten und gleichzeitig einen Nachrichtentext einzufügen. Im Braze-SMS- oder MMS-Composer werden Uploads über 1&nbsp;MB blockiert. Die Fehlermeldung empfiehlt, eine Datei von 600&nbsp;KB oder weniger hochzuladen. Wir empfehlen außerdem, zu testen, ob Ihre Medien über die Mobilfunkanbieter Ihrer Nutzer:innen zugestellt werden können.

#### Dateigrößenlimits der Mobilfunkanbieter {#carrier-file-size-limits}

| Datei&nbsp;größe | Handhabung durch den Anbieter |
| --- | --- |
| 300&nbsp;KB | Alle Anbieter sollten MMS-Nachrichten dieser Größe zuverlässig verarbeiten. |
| 600&nbsp;KB | Dies gilt als die standardmäßige maximale Dateigröße für MMS bei den meisten Anbietern. |
| 1&nbsp;MB | Die meisten US- und kanadischen Anbieter können MMS-Nachrichten dieser Größe verarbeiten, wobei dies je nach Anbieter variieren kann. Einige Anbieter erlauben möglicherweise größere Dateien. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dateigrößenlimits der Mobilfunkanbieter" }

#### Akzeptierte Dateitypen {#accepted-file-types}

Braze akzeptiert JPEG-, GIF-, PNG- und VCF-Dateien und ermöglicht es Ihnen, ein einzelnes Multimedia-Asset an Ihre MMS-Nachricht anzuhängen.