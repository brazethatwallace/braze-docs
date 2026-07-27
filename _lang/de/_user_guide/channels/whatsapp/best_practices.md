---
nav_title: Best Practices
article_title: Best Practices
page_order: 22
description: "Dieser Artikel beschreibt empfohlene Best Practices für die Nutzung des WhatsApp-Messaging-Kanals, einschließlich der Aufrechterhaltung einer hohen Telefonqualitätsbewertung und der Vermeidung einer hohen Rate an Blockierungen und Meldungen."
page_type: reference
channel:
  - WhatsApp


---
# WhatsApp-Best-Practices {#whatsapp-best-practices}

> Bevor Sie Ihre WhatsApp-Nachrichten versenden, lesen Sie diese empfohlenen Best Practices, um eine hohe Telefonqualitätsbewertung aufrechtzuerhalten, Blockierungen und Meldungen zu vermeiden und Nutzer:innen für Opt-in und Opt-out zu verwalten.

## Eine hohe Telefonqualitätsbewertung aufrechterhalten {#maintain-a-high-phone-quality-rating}

WhatsApp basiert seine [Telefonqualitätsbewertung](https://www.facebook.com/business/help/896873687365001) auf Aktionen, die von Nutzer:innen durchgeführt werden, die Ihre Nachrichten erhalten, wie z. B. das Blockieren oder Melden Ihres Unternehmens. Es ist wichtig, eine hohe Qualitätsbewertung aufrechtzuerhalten, denn wenn sie niedrig ist und sich über einen bestimmten Zeitraum nicht verbessert, kann Ihr Messaging-Limit sinken.

Wenn Sie eine:n Nutzer:in zum ersten Mal in WhatsApp anschreiben, werden diese Optionen im Nachrichtenverlauf angezeigt.

![WhatsApp-Nachrichtenverlauf mit Optionen zum Blockieren oder Melden eines Unternehmens]({% image_buster /assets/img/whatsapp/whatsapp_block_report.png %}){: style="max-width:30%;"}

{% alert note %}
Für Metriken zu Ihren Blockierungen und Meldungen stellen Sie sicher, dass der [Insights-Tab](https://www.facebook.com/business/help/683499390267496) in Ihrem WhatsApp Manager aktiviert ist.
{% endalert %}

Um hohe Blockierungs- und Meldungsraten zu vermeiden, empfiehlt Braze die folgenden Best Practices, um eine hohe Telefonqualitätsbewertung und stabile Messaging-Limits aufrechtzuerhalten.

### WhatsApp-Opt-in-Anforderungen und -Richtlinien befolgen {#follow-whatsapp-opt-in-requirements-and-guidelines}

Stellen Sie sicher, dass alle Nutzer:innen aktiv dem Empfang von WhatsApp-Nachrichten zugestimmt haben, bevor Sie mit ihnen über WhatsApp kommunizieren. Wenn Sie Nutzer:innen um ein Opt-in bitten, sollten sie darüber informiert werden, dass sie ausdrücklich dem Empfang von Nachrichten Ihres Unternehmens über WhatsApp zustimmen.

{% alert note %}
Informationen zu Opt-in-Anforderungen und hilfreiche Tipps finden Sie unter [Get Opt-in for WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/).
{% endalert %}

### Messaging-Best-Practices befolgen {#follow-messaging-best-practices}

- Gestalten Sie Ihren Kanalnamen so, dass er Ihre Marke widerspiegelt, damit Nutzer:innen erkennen, dass die Nachricht von Ihnen stammt und kein Spam ist.
- Senden Sie Nutzer:innen eine Bestätigungsnachricht, nachdem Sie deren Opt-in-Zustimmung erhalten haben.
- Senden Sie Nachrichten zu angemessenen Zeiten.

### Kund:innen die Möglichkeit zum Opt-out geben {#give-customers-the-option-to-opt-out}

Opt-outs wirken sich nicht auf Ihre Telefonqualitätsbewertung aus, daher ist es besser, wenn sich Nutzer:innen vom Empfang von WhatsApp-Kommunikation abmelden, anstatt Sie zu blockieren oder zu melden.

Eine empfohlene Best Practice ist es, in der Fußzeile der ersten Nachricht, die Sie an Nutzer:innen senden, Anweisungen zum Abmelden bereitzustellen. Sie könnten beispielsweise angeben, dass sich Nutzer:innen von Ihrem WhatsApp-Kanal abmelden können, indem sie mit Ihrem Opt-out-Schlüsselwort antworten. Sie könnten die Opt-out-Fußzeile auch regelmäßig in zukünftige Campaigns einbinden. Informationen zur Einrichtung finden Sie unter [Opt-in und Opt-out]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs).

![WhatsApp-Nachricht mit einer Fußzeile, die besagt, dass man mit STOP antworten soll, um sich vom Kanal abzumelden]({% image_buster /assets/img/whatsapp/whatsapp_unsubscribe.png %}){: style="max-width:35%;"}

### Antwortlatenz bei bidirektionalen Abläufen minimieren {#minimize-response-latency-for-two-way-flows}

Für interaktive Canvas-Abläufe, die mit [Antwortnachrichten]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#response-messages) reagieren:

- Platzieren Sie den Antwortnachricht-Schritt unmittelbar nach dem eingehenden Trigger oder der Aktionspfad-Auswertung.
- Verwenden Sie [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) anstelle von Nutzer:innen-Aktualisierungsschritten, wenn vor der Antwort keine Abo-Änderungen erforderlich sind.
- Vermeiden Sie lange Verzögerungen oder mehrtägige Wartezeiten zwischen eingehenden Nachrichten und dem Versand von Antworten; das WhatsApp-Kundenservice-Fenster beträgt 24 Stunden pro eingehender Nachricht.