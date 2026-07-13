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

### MMS-Absender-Anforderungen {#mms-sender-requirements}

> MMS und SMS sind beide an den Braze-SMS-Kanal gebunden. Um MMS in Ihrem Konto nutzen zu können, ist der Kauf von SMS erforderlich, sofern Sie noch keinen Zugang erworben haben. Bestehende SMS-Kund:innen können nach dem Kauf auf MMS zugreifen.

MMS wird derzeit für US-Shortcodes (5–6-stellige Nummern), US- und CA-Langcodes (10-stellige Nummern) sowie US- und kanadische Kundennummern unterstützt. MMS wird bei bestimmten Dienstanbietern auch für gebührenfreie Nummern unterstützt.

Der Versand von MMS an Nummern außerhalb der USA und Kanadas ist möglich, allerdings werden MMS-Nachrichten in eine SMS-Nachricht mit einem Link zum Medien-Asset umgewandelt.

### MMS-Shortcodes {#mms-short-codes}

Einige Nutzer:innen verwenden möglicherweise keine MMS-Shortcodes, diese stehen jedoch bei Bedarf zu einem späteren Zeitpunkt zur Verfügung.

Für Nutzer:innen, die ihre Shortcodes vor der MMS-Unterstützung durch Braze erhalten haben: Alle bestehenden Kund:innen mit US-Shortcodes können MMS sofort aktivieren. Kontaktieren Sie Ihren Customer-Success-Manager, wenn dies auf Sie zutrifft und Sie MMS aktivieren möchten.

{% alert important %}
Wenn MMS für Shortcodes aktiviert wird, die zuvor kein MMS unterstützten, müssen die Shortcodes möglicherweise in einem Genehmigungsverfahren erneut genehmigt werden, das Wochen dauern kann. Es ist wichtig, diesen Zeitrahmen bei der Entscheidung zur MMS-Aktivierung zu berücksichtigen.
{% endalert %}

#### Best Practices für MMS-Shortcodes {#mms-short-code-best-practices}

- Bei Braze empfehlen wir dringend, Transaktions- und Aktionsnachrichten getrennt zu halten, jeweils mit unterschiedlichen Shortcodes. Da MMS an den SMS-Kanal gebunden ist und der SMS-Kanal stark reguliert wird, können Kund:innen bei Missbrauch des Kanals zu einer Geldstrafe verpflichtet werden und ihren Shortcode gesperrt bekommen (was nicht rückgängig gemacht werden kann). Die Trennung von Transaktions- und Aktionsnachrichten auf verschiedene Shortcodes schützt die Transaktionsnachrichten.
- Wenn Kund:innen bereits einen Shortcode für Aktionsnachrichten haben und dieser MMS-fähig ist, benötigen sie keinen separaten Shortcode für MMS.

### MMS-Langcodes {#mms-long-codes}

Kund:innen können MMS mit Langcodes versenden. Dazu müssen Sie sicherstellen, dass Ihre Langcodes MMS-fähig sind. Dies kann bei der Ersteinrichtung oder später innerhalb Ihres Kontos erfolgen.

MMS-Nachrichten können nicht mit einer alphanumerischen Absender-ID versendet werden.

### MMS-Nachrichtenlimits und Durchsatz {#mms-message-limits-and-throughput}

Der MMS-Durchsatz beträgt ein Segment pro Sekunde über einen Langcode.

Mobilfunkanbieter legen eigene Dateigrößenlimits fest, die den Erfolg von MMS-Sendungen bestimmen. Diese Limits können je nach Geografie und Anbieter variieren, daher empfiehlt Braze, 600&nbsp;KB für Ihr Multimedia-Asset nicht zu überschreiten und gleichzeitig einen Nachrichtentext einzufügen. Wir empfehlen außerdem, zu testen, ob Ihre Medien über die Anbieter Ihrer Nutzer:innen zugestellt werden können.

#### Dateigrößenlimits der Anbieter {#carrier-file-size-limits}

| Datei&nbsp;größe | Handhabung durch den Anbieter |
| --- | --- |
| 300&nbsp;KB | Alle Anbieter sollten MMS-Nachrichten dieser Größe zuverlässig verarbeiten können. |
| 600&nbsp;KB | Dies gilt als die standardmäßige maximale Dateigröße für MMS bei den meisten Anbietern. |
| 1&nbsp;MB | Die meisten US-amerikanischen und kanadischen Anbieter können MMS-Nachrichten dieser Größe verarbeiten, wobei dies je nach Anbieter variieren kann. Einige Anbieter erlauben möglicherweise größere Dateien. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dateigrößenlimits der Anbieter" }

#### Akzeptierte Dateitypen {#accepted-file-types}

Braze akzeptiert JPEG-, GIF-, PNG- und VCF-Dateien und ermöglicht es Ihnen, ein einzelnes Multimedia-Asset an Ihre MMS-Nachricht anzuhängen.