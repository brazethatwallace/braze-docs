---
nav_title: Sunset-Richtlinien
article_title: Sunset-Richtlinien für E-Mail
page_order: 8
page_type: reference
description: "Dieser Artikel behandelt Best Practices rund um Sunset-Richtlinien und hilft Ihnen zu verstehen, wann es besser ist, Nachrichten an inaktive Nutzer:innen einzustellen."
channel: email

---

# Sunset-Richtlinien

> Auch wenn es verlockend sein mag, Kampagnen an so viele Nutzer:innen wie möglich zu senden, gibt es Situationen, in denen es tatsächlich vorteilhaft ist, Nachrichten an inaktive Nutzer:innen einzustellen.

Bei E-Mails hat Ihre Sende-IP einen Reputationswert, der Engagement, Spam-Berichte, Blocklisting und mehr berücksichtigt. Sie können Tools wie [Sender Score](https://www.senderscore.org/) oder [Outlooks Smart Network Data Service](https://postmaster.live.com/snds/) verwenden, um Ihren Reputationswert zu überwachen. Wenn Ihr Reputationswert dauerhaft niedrig ist, können ISP- und Postfach-Filter Ihre E-Mails automatisch in einen Spam- oder niedrig priorisierten Ordner für alle Empfänger:innen sortieren – auch für aktive. Das Erstellen einer Sunset-Richtlinie hilft dabei, Ihre E-Mails nur an aktive Empfänger:innen zuzustellen.

Segmentierungsfilter helfen zu verhindern, dass Ihre Nachrichten wie Spam wirken, indem sie Ihnen ermöglichen, Sunset-Richtlinien für E-Mails, Push und In-App-Benachrichtigungen einfach umzusetzen. Hier sind einige Punkte, die Sie bei der Erstellung einer Sunset-Richtlinie berücksichtigen sollten:

- Was zählt als „inaktive:r" Nutzer:in?
- Wird Engagement durch Klicks, Käufe, App-Nutzung oder eine Kombination dieser Verhaltensweisen definiert?
- Wie lange muss die Inaktivitätsphase andauern, bevor Sie den Nachrichtenversand einstellen?
- Werden Sie spezielle Kampagnen an Nutzer:innen senden, bevor Sie sie aus Ihren Segmenten ausschließen?
- Für welche Messaging-Kanäle soll Ihre Sunset-Richtlinie gelten?

Wenn Sie beispielsweise Nutzer:innen haben, die sich für [Apples E-Mail-Datenschutz (MPP)]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp/) entschieden haben, sollten Sie berücksichtigen, wie sich dies auf Ihre E-Mail-Kampagnen und Zustellbarkeitsmetriken auswirken kann, und bestimmen, wie Sie Ihre Sunset-Richtlinie am besten strukturieren.

Um Sunset-Richtlinien in Ihre Kampagnen einzubinden, erstellen Sie ein [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#creating-a-segment), das automatisch Nutzer:innen ausschließt, die Ihre E-Mails als Spam markiert haben oder über einen bestimmten Zeitraum nicht mit Ihren Nachrichten interagiert haben.

Um diese Segmente einzurichten, wählen Sie die Filter `Has Marked You As Spam` und `Last Engaged With Message` im Abschnitt **Retargeting** im Filter-Dropdown aus.

Wenn Sie den Filter `Last Engaged With Message` anwenden, geben Sie die Art des Messaging (Push, E-Mail oder In-App-Benachrichtigung) an, mit der die Nutzer:innen interagiert oder nicht interagiert haben, sowie die Anzahl der Tage seit der letzten Interaktion. Nachdem Sie ein Segment erstellt haben, können Sie dieses Segment über jeden [Messaging-Kanal]({{site.baseurl}}/user_guide/channels/) ansprechen.

![Seite „Segmentdetails" mit dem ausgewählten Filter „Last Engaged with Message".]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Obwohl Braze automatisch den E-Mail-Versand an Nutzer:innen einstellt, die Sie als Spam markiert haben, ermöglicht Ihnen der Filter `Has Marked You As Spam`, diesen Nutzer:innen auch gezielte Push-Nachrichten und In-App-Benachrichtigungen zu senden. Dieser Filter ist nützlich für [Retargeting-Kampagnen]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns/#retarget-campaigns). Sie können beispielsweise inaktiven Nutzer:innen Nachrichten senden, die sie an die Features und Angebote erinnern, die ihnen entgehen, wenn sie Ihre E-Mails nicht öffnen.

Sunset-Richtlinien können besonders hilfreich bei E-Mail-Kampagnen sein, die sich an passive Nutzer:innen richten. Obwohl sich diese Kampagnen auf Segmente konzentrieren, die über einen bestimmten Zeitraum nicht mit Ihrer App interagiert haben, können sie die Zustellbarkeit Ihrer E-Mails gefährden, wenn sie wiederholt inaktive Empfänger:innen einschließen. Sunset-Richtlinien ermöglichen es Ihnen, passive Nutzer:innen anzusprechen, ohne im Spam-Ordner zu landen.