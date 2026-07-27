---
nav_title: Sunset-Richtlinien
article_title: Sunset-Richtlinien für E-Mail
page_order: 8
page_type: reference
description: "Dieser Artikel behandelt Best Practices rund um Sunset-Richtlinien und hilft Ihnen zu verstehen, wann es besser ist, Nachrichten an uninteressierte Nutzer:innen einzustellen."
channel: email

---

# Sunset-Richtlinien {#sunset-policies}

> Auch wenn es verlockend sein mag, Campaigns an so viele Nutzer:innen wie möglich zu senden, gibt es Situationen, in denen es tatsächlich vorteilhaft ist, Nachrichten an uninteressierte Nutzer:innen einzustellen.

Bei E-Mails fließen die Reputation Ihrer Sende-IP und Ihrer Domain in Engagement, Spam-Berichte, Blocklisten und mehr ein. Bleibt die Reputation dauerhaft niedrig, können ISP- und Mailbox-Filter Ihre E-Mails für alle Empfänger:innen in den Spam- oder niedrig priorisierten Ordner sortieren – nicht nur für inaktive. Sunset-Richtlinien begrenzen den fortlaufenden Versand an uninteressierte Nutzer:innen und schützen so Ihre Reputation. Kombinieren Sie sie mit regelmäßigem Monitoring, damit Sie Probleme frühzeitig erkennen können.

## IP- und Domain-Gesundheit überwachen {#monitor-ip-and-domain-health}

Verwenden Sie das [Deliverability Center]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center), um nachzuverfolgen, wie Postfachanbieter Ihren Versand bewerten:

- **Google Postmaster Tools** (nach Verknüpfung Ihres Kontos): IP-Reputation, Domain-Reputation, Zustellfehler, Authentifizierung (SPF, DKIM, DMARC) und Verschlüsselungsmetriken für Gmail-bezogene Einblicke.
- **Microsoft Smart Network Data Services (SNDS)** (wenn für Ihre IPs konfiguriert): IP-Gesundheit bei Outlook und Microsoft-Postfächern, einschließlich Filterergebnissen, Beschwerdequoten und Spam-Trap-Treffern.

Für eine umfassendere Versandhygiene lesen Sie [E-Mail-Zustellbarkeit verbessern]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) und [Zustellbarkeitsfallen und Spam-Traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps).

Sie können auch externe Tools wie [Sender Score](https://www.senderscore.org/) oder [Outlook Smart Network Data Services](https://postmaster.live.com/snds/) außerhalb von Braze für zusätzliche Signale nutzen.

## Unterdrückungslisten verwenden {#use-suppression-lists}

[Unterdrückungslisten]({{site.baseurl}}/user_guide/audience/suppression_lists) sind Gruppen von Nutzer:innen, die mit Segment-Filtern definiert werden und standardmäßig keine Campaigns oder Canvases erhalten, selbst wenn sie im Zielsegment erscheinen. Für inaktive oder nicht engagierte Empfänger:innen fungiert eine Unterdrückungsliste als Workspace-weite Schutzmaßnahme. Wenn Nutzer:innen Ihre Inaktivitätskriterien erfüllen, erhalten sie die meisten Nachrichten nicht mehr, ohne dass Sie jedes Segment oder jede Campaign einzeln bearbeiten müssen.

Um die Liste an eine Sunset-Richtlinie anzupassen, erstellen Sie die Unterdrückungsliste mit Filtern, die Nutzer:innen erfassen, die keine laufenden Werbe-E-Mails mehr erhalten sollen (zum Beispiel `Last Engaged With Message` oder andere Filter unter **Retargeting**). Verwenden Sie dabei dasselbe Rückblickfenster und dieselben Kanaloptionen, die Sie in Ihrer Richtlinie für „nicht engagiert“ nutzen. Die Zugehörigkeit ist dynamisch – Nutzer:innen werden aufgenommen, wenn sie die Filterkriterien erfüllen, und wieder entfernt, wenn sie erneut interagieren.

Wenn bestimmte Sendungen trotzdem inaktive Nutzer:innen erreichen sollen, etwa eine letzte Rückgewinnungs-Nachricht oder genehmigte transaktionale Journeys, konfigurieren Sie Ausnahme-Tags in der Unterdrückungsliste, damit Campaigns oder Canvases mit diesen Tags weiterhin zugestellt werden, wenn Nutzer:innen in der Zielgruppe sind. Unterdrückungslisten arbeiten zusammen mit der Segmentierung, die festlegt, wen Sie in eine Sendung einschließen. Informationen zu Einrichtungsschritten, Berechtigungen und Limits finden Sie unter [Unterdrückungslisten einrichten]({{site.baseurl}}/user_guide/audience/suppression_lists#setup).

## Segmentierungsfilter verwenden {#use-segmentation-filters}

Segmentierungsfilter helfen dabei, zu verhindern, dass Ihre Nachrichten wie Spam wirken, indem sie Ihnen ermöglichen, Sunset-Richtlinien für E-Mails, Push und In-App-Benachrichtigungen einfach umzusetzen. Hier sind einige Punkte, die Sie bei der Erstellung einer Sunset-Richtlinie berücksichtigen sollten:

- Was zählt als „nicht engagierte:r“ Nutzer:in?
- Wird Engagement durch Klicks, Käufe, App-Nutzung oder eine Kombination dieser Verhaltensweisen definiert?
- Wie lange muss die Engagement-Pause andauern, bevor Sie aufhören, Nachrichten zu senden?
- Werden Sie spezielle Campaigns an Nutzer:innen senden, bevor Sie sie aus Ihren Segments ausschließen?
- Für welche Messaging-Kanäle soll Ihre Sunset-Richtlinie gelten?

Wenn Sie beispielsweise Nutzer:innen haben, die sich für [Apples E-Mail-Datenschutz (MPP)]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp) entschieden haben, überlegen Sie, wie sich dies auf Ihre E-Mail-Campaigns und Zustellbarkeits-Metriken auswirken kann, und bestimmen Sie, wie Sie Ihre Sunset-Richtlinie am besten strukturieren.

Um Sunset-Richtlinien in Ihre Campaigns zu integrieren, erstellen Sie ein [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), das automatisch Nutzer:innen ausschließt, die Ihre E-Mails als Spam markiert haben oder über einen bestimmten Zeitraum nicht mit Ihren Nachrichten interagiert haben.

Um diese Segments einzurichten, wählen Sie die Filter `Has Marked You As Spam` und `Last Engaged With Message` im Bereich **Retargeting** im Filter-Dropdown aus.

Wenn Sie den Filter `Last Engaged With Message` anwenden, geben Sie die Art des Messaging (Push, E-Mail oder In-App-Benachrichtigung) an, mit der die Nutzer:innen interagiert oder nicht interagiert haben, sowie die Anzahl der Tage seit der letzten Interaktion. Nachdem Sie ein Segment erstellt haben, können Sie dieses Segment mit jedem [Messaging-Kanal]({{site.baseurl}}/user_guide/channels) ansprechen.

![Seite „Segment-Details“ mit dem ausgewählten Filter „Last Engaged with Message“.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Obwohl Braze automatisch aufhört, E-Mails an Nutzer:innen zu senden, die Sie als Spam markiert haben, ermöglicht Ihnen der Filter `Has Marked You As Spam`, diesen Nutzer:innen auch gezielte Push-Nachrichten und In-App-Benachrichtigungen zu senden. Dieser Filter ist nützlich für [Retargeting-Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns). Sie können beispielsweise nicht engagierten Nutzer:innen Nachrichten senden, die sie an die Features und Angebote erinnern, die ihnen entgehen, wenn sie Ihre E-Mails nicht öffnen.

Sunset-Richtlinien können besonders hilfreich bei E-Mail-Campaigns sein, die auf passive Nutzer:innen abzielen. Während sich diese Campaigns auf Segments konzentrieren, die über einen bestimmten Zeitraum nicht mit Ihrer App interagiert haben, können sie die Zustellbarkeit Ihrer E-Mails gefährden, wenn sie wiederholt nicht engagierte Empfänger:innen einschließen. Sunset-Richtlinien ermöglichen es Ihnen, passive Nutzer:innen anzusprechen, ohne im Spam-Ordner zu landen.