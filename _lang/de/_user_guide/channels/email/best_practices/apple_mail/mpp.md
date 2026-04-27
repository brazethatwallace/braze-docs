---
nav_title: Apple Mail-Datenschutz
article_title: Apple Mail Datenschutz für iOS 15
page_order: 1
description: "Dieser Referenzartikel behandelt das Update für den Apple Mail-Datenschutz, wer davon betroffen ist und wie Sie sich auf das Feature vorbereiten können."
channel:
  - email

---

# Apples Mail-Datenschutz

> Dieser Artikel behandelt Apples Mail Privacy Protection (MPP), wen es betrifft und wie Sie sich auf die Auswirkungen auf E-Mail-Zustellbarkeitsmetriken vorbereiten können.

## Was ist das Mail Privacy Protection Update von Apple?

Apples Mail Privacy Protection (MPP) ist ein Datenschutz-Update, das für Nutzer:innen der Apple Mail App auf iOS 15, iPadOS 15, macOS Monterey und watchOS 8 verfügbar ist und Mitte September 2021 veröffentlicht wurde. Für Nutzer:innen, die sich für MPP entscheiden (was unserer Einschätzung nach die meisten Nutzer:innen tun werden), werden E-Mails nun über Proxy-Server vorgeladen, wobei Bilder zwischengespeichert werden und die Möglichkeit eingeschränkt wird, Tracking-Pixel für Metriken wie [Öffnungs-Tracking]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#changing-location-of-tracking-pixel) zu nutzen.

Marken sollten damit rechnen, dass MPP zu Problemen bei E-Mail-Zustellbarkeitsmetriken sowie bei bestehenden Campaigns und Canvases führt, die auf Basis dieser Metriken getriggert werden. Um die Auswirkungen auf die E-Mail-Zustellbarkeit zu verstehen, lesen Sie den Abschnitt [E-Mail-Reporting]({{site.baseurl}}/user_guide/channels/email/reporting/).

### Wer ist davon betroffen?

Alle Empfänger:innen, die die native Apple Mail App verwenden auf:

- iOS 15
- iPadOS 15
- macOS Monterey
- watchOS 8

Dies gilt für alle Nutzer:innen, die ihr E-Mail-Konto mit der Apple Mail App verbunden und das Sicherheits-Feature aktiviert haben, unabhängig vom E-Mail-Dienst (Gmail, Outlook, Yahoo, AOL usw.). Diese Auswirkung beschränkt sich nicht auf Abonnent:innen, die E-Mails an Apple-/iCloud-/me.com-E-Mail-Adressen erhalten.

{% alert important %}
Obwohl diese Updates für die E-Mail-Zustellbarkeit bedeutsam sind, ändert MPP grundsätzlich keine der Regeln, die für E-Mail und Zustellbarkeit gelten. Stattdessen wird es beeinflussen, wie wir Erfolg messen und welche E-Mail-Tools und -Funktionen künftig genutzt werden können.
{% endalert %}

## Wie bereiten Sie sich auf MPP vor?

Für Marken, die gerade erst beginnen, über ihre Reaktion auf MPP und dessen potenzielle Auswirkungen auf ihr E-Mail-Marketing und ihr gesamtes Customer-Engagement nachzudenken, ist schnelles Handeln entscheidend. Wir empfehlen Nutzer:innen Folgendes:

- Bewerten Sie das Risiko, das MPP für Ihre Marketing-Aktivitäten darstellt.
- Erstellen Sie einen gezielten MPP-Reaktionsplan, der Automatisierungsanpassungen auf der Braze-Plattform berücksichtigt, Best Practices für die Zustellbarkeit stärkt und ein breiteres Set an Metriken zur Performance-Messung entwickelt.
- Setzen Sie diesen Reaktionsplan so schnell wie möglich um.

Für einen ausführlichen Überblick darüber, wie Sie sich auf Apples Mail Privacy Protection vorbereiten können, lesen Sie unseren [Blogbeitrag](https://www.braze.com/resources/articles/apple-mail-privacy-protection-how-to-prepare).