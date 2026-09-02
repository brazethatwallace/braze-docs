---
nav_title: Sunsetting-Richtlinien
article_title: Sunset-Richtlinien für E-Mail
page_order: 8
page_type: reference
description: "Dieser Artikel befasst sich mit bewährten Sunsetting-Richtlinien und mit der Frage, wann es besser ist, Nachrichten an desinteressierte Nutzer:innen einzustellen."
channel: email

---

# Sunset-Richtlinien {#sunset-policies}

> Auch wenn es verlockend sein mag, Campaigns an so viele Nutzer:innen wie möglich zu senden, gibt es Situationen, in denen es tatsächlich vorteilhaft ist, Nachrichten an uninteressierte Nutzer:innen einzustellen.

Bei E-Mails fließen die Reputation Ihrer Sende-IP und Ihrer Domain in Engagement, Spam-Berichte, Blocklisten und mehr ein. Wenn die Reputation dauerhaft niedrig bleibt, können ISP or Internet-Provider- und Mailbox-Filter Ihre E-Mails für alle Empfänger:innen in den Spam- oder niedrig priorisierten Ordner sortieren – nicht nur für inaktive. Sunset-Richtlinien begrenzen den fortlaufenden Versand an uninteressierte Nutzer:innen und schützen so Ihre Reputation. Kombinieren Sie sie mit regelmäßigem Monitoring, damit Sie Probleme frühzeitig erkennen können.

## IP- und Domain-Gesundheit überwachen {#monitor-ip-and-domain-health}

Nutzen Sie das [Deliverability Center]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center), um nachzuverfolgen, wie Mailbox-Anbieter Ihren Versand bewerten:

- **Google Postmaster Tools** (nachdem Sie Ihr Konto verbunden haben): IP-Reputation, Domain-Reputation, Zustellfehler, Authentifizierung (SPF, DKIM, DMARC) und Verschlüsselungsmetriken für Gmail-bezogene Einblicke.
- **Microsoft Smart Network Data Services (SNDS)** (wenn für Ihre IPs konfiguriert): IP-Gesundheit für Outlook und Microsoft-Mailboxen, einschließlich Filterergebnissen, Beschwerdequoten und Spam-Trap-Treffern.

Weitere Informationen zur Versandhygiene finden Sie unter [E-Mail-Zustellbarkeit verbessern]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) und [Zustellbarkeitsfallen und Spam-Traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps).

Sie können auch externe Tools wie [Sender Score](https://www.senderscore.org/) oder [Outlook Smart Network Data Services](https://postmaster.live.com/snds/) außerhalb von Braze für zusätzliche Signale nutzen.

## Unterdrückungslisten verwenden {#use-suppression-lists}

[Unterdrückungslisten]({{site.baseurl}}/user_guide/audience/suppression_lists) sind Gruppen von Nutzer:innen, die mit Segmentfiltern definiert werden und standardmäßig keine Campaigns oder Canvase erhalten, selbst wenn sie im Zielsegment erscheinen. Für inaktive oder uninteressierte Empfänger:innen fungiert eine Unterdrückungsliste als Workspace-weite Schutzmaßnahme. Wenn Nutzer:innen Ihre Inaktivitätskriterien erfüllen, erhalten sie die meisten Nachrichten nicht mehr, ohne dass Sie jedes Segment oder jede Campaign einzeln bearbeiten müssen.

Um die Unterdrückungsliste an eine Sunset-Richtlinie anzupassen, erstellen Sie sie mit Filtern, die Nutzer:innen erfassen, die keine laufenden Werbe-E-Mails mehr erhalten sollen (z. B. `Last Engaged With Message` oder andere Filter unter **Retargeting**). Verwenden Sie dabei dasselbe Rückblickfenster und dieselbe Kanalauswahl wie in Ihrer Richtlinie für „unengagierte“ Nutzer:innen. Die Mitgliedschaft ist dynamisch – Nutzer:innen werden aufgenommen, wenn sie die Filterkriterien erfüllen, und wieder entfernt, wenn sie erneut interagieren.

Wenn bestimmte Sendungen inaktive Nutzer:innen dennoch erreichen sollen, z. B. eine letzte Rückgewinnungs-E-Mail oder genehmigte transaktionale Journeys, konfigurieren Sie Ausnahme-Tags in der Unterdrückungsliste, damit Campaigns oder Canvase mit diesen Tags weiterhin zugestellt werden, wenn Nutzer:innen in der Zielgruppe sind. Unterdrückungslisten arbeiten zusammen mit der Segmentierung, die festlegt, wen Sie in einen Versand einschließen. Informationen zu Einrichtungsschritten, Berechtigungen und Limits finden Sie unter [Unterdrückungslisten einrichten]({{site.baseurl}}/user_guide/audience/suppression_lists#setup).

## Segmentierungsfilter verwenden {#use-segmentation-filters}

Mit Segmentierungsfiltern können Sie verhindern, dass Ihre Nachrichten wie Spam wirken, indem Sie ganz einfach Sunset-Richtlinien für E-Mails, Push- und In-App-Benachrichtigungen implementieren. Hier sind einige Punkte, die Sie bei der Erstellung einer Sunset-Richtlinie berücksichtigen sollten:

- Was gilt als „unengagierte:r“ Nutzer:in?
- Wird Engagement durch Klicks, Käufe, App-Nutzung oder eine Kombination dieser Verhaltensweisen definiert?
- Wie lange muss das Engagement ausbleiben, bevor Sie den Nachrichtenversand einstellen?
- Werden Sie spezielle Campaigns an Nutzer:innen senden, bevor Sie sie aus Ihren Segmenten ausschließen?
- Für welche Messaging-Kanäle soll Ihre Sunset-Richtlinie gelten?

Wenn Sie beispielsweise Nutzer:innen haben, die sich für [Apples E-Mail-Datenschutz or E-Mail-Datenschutz or MPP (E-Mail-Datenschutz or MPP)]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp) entschieden haben, sollten Sie berücksichtigen, wie sich dies auf Ihre E-Mail-Campaigns und Zustellbarkeitsmetriken auswirken kann, und bestimmen, wie Sie Ihre Sunset-Richtlinie am besten strukturieren.

Um Sunset-Richtlinien in Ihre Campaigns einzubinden, erstellen Sie ein [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), das automatisch Nutzer:innen ausschließt, die Ihre E-Mails als Spam markiert haben oder über einen bestimmten Zeitraum nicht mit Ihren Nachrichten interagiert haben.

Um diese Segmente einzurichten, wählen Sie die Filter `Has Marked You As Spam` und `Last Engaged With Message` im Abschnitt **Retargeting** im Filter-Dropdown aus.

Wenn Sie den Filter `Last Engaged With Message` anwenden, geben Sie die Art des Messaging (Push, E-Mail oder In-App-Benachrichtigung) an, mit der die Nutzer:innen interagiert oder nicht interagiert haben, sowie die Anzahl der Tage seit der letzten Interaktion. Nachdem Sie ein Segment erstellt haben, können Sie dieses Segment über jeden [Messaging-Kanal]({{site.baseurl}}/user_guide/channels) ansprechen.

![Seite „Segmentdetails“ mit dem ausgewählten Filter „Last Engaged with Message“.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Obwohl Braze automatisch den E-Mail-Versand an Nutzer:innen einstellt, die Sie als Spam markiert haben, ermöglicht Ihnen der Filter `Has Marked You As Spam`, diesen Nutzer:innen auch gezielte Push-Nachrichten und In-App-Benachrichtigungen zu senden. Dieser Filter ist nützlich für [Retargeting-Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns). Sie können beispielsweise unengagierten Nutzer:innen Nachrichten senden, die sie an die Features und Angebote erinnern, die ihnen entgehen, wenn sie Ihre E-Mails nicht öffnen.

Sunset-Richtlinien können besonders hilfreich bei E-Mail-Campaigns sein, die sich an passive Nutzer:innen richten. Obwohl sich diese Campaigns auf Segmente konzentrieren, die über einen bestimmten Zeitraum nicht mit Ihrer App interagiert haben, können sie die Zustellbarkeit Ihrer E-Mails gefährden, wenn sie wiederholt unengagierte Empfänger:innen einschließen. Sunset-Richtlinien ermöglichen es Ihnen, passive Nutzer:innen anzusprechen, ohne im Spam-Ordner zu landen.