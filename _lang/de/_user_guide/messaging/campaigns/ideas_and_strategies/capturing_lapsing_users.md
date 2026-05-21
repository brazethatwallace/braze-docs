---
nav_title: Passive Nutzer:innen zurückgewinnen
article_title: Passive Nutzer:innen zurückgewinnen
page_order: 1
page_type: tutorial
description: "Dieser Artikel befasst sich mit dem Thema passiver Nutzer:innen und zeigt, wie Sie Braze-Kampagnen effektiv nutzen können, um diese Nutzer:innen erneut zu aktivieren."
tool:
  - Segments
  - Campaigns

---

# Passive Nutzer:innen zurückgewinnen

> Wenn Ihre Zielgruppe schrumpft, ist es entscheidend, sie zurückzugewinnen. Mit Braze können Sie automatisierte, wiederkehrende Kampagnen zur erneuten Interaktion einrichten, um passive Nutzer:innen zu erreichen. Sie können den Zeitrahmen und die Häufigkeit der erneuten Interaktion wählen, die am besten zu Ihrer App passen. Zur Veranschaulichung starten wir hier mit einem 14-tägigen Plan zur erneuten Interaktion.

Weitere Informationen zum Targeting von Nutzer:innen finden Sie in unserem [Braze-Lernkurs](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) zur Kampagneneinrichtung!

## 1. Schritt: Nutzer:innen segmentieren

Zunächst erstellen wir ein Segment, das Nutzer:innen anspricht, die Ihre App in den letzten zwei Wochen nicht genutzt haben. Dazu verwenden wir die folgenden Filter:

- **Last Used App** mehr als 2 Wochen her
- **Last Used App** weniger als 3 Wochen her

![]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Geben Sie dem Segment einen einprägsamen Namen, z. B. „Passive Nutzer:innen – 2 Wochen". Da wir die Kampagne so einrichten, dass sie wöchentlich wiederholt wird, möchten wir sicherstellen, dass mindestens eine Woche an Nutzer:innen im Segment erfasst wird. Deshalb haben wir Nutzer:innen ausgewählt, die die App zuletzt vor zwei bis drei Wochen genutzt haben.

## 2. Schritt: Kampagne erstellen

Klicken Sie als Nächstes auf **Kampagne erstellen** und wählen Sie den Kampagnentyp, den wir an dieses Segment senden möchten. In diesem Beispiel erstellen wir eine neue [Push-Kampagne]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/).

![]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Wir nennen die Kampagne „Nachricht an passive Nutzer:innen – 2 Wochen" und erstellen dann den Inhalt unserer Nachricht. In diesem Beispiel sprechen wir nur iOS-Nutzer:innen an, aber Sie können Braze sowohl für Android- als auch für iOS-Push-Benachrichtigungen verwenden.

Je kürzer die letzte Nutzung der App zurückliegt, desto wichtiger ist es, aktuell und relevant zu sein. Wenn Sie Nutzer:innen nach zwei Wochen ohne App-Nutzung kontaktieren, ist es wichtig, relevante Inhalte zu präsentieren und die Vorteile der App hervorzuheben.

![]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

Als Nächstes erstellen wir einen wiederkehrenden Zeitplan, um unsere wöchentliche Nachricht donnerstags um 17:45 Uhr zu senden – mit der [Zustellung nach Ortszeit]({{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer) unter **Zeitabhängige Planungsoptionen**. Wir empfehlen, Ihren Sitzungsgraphen zu analysieren, um Nutzer:innen kurz vor Zeiten mit hoher Nutzung anzusprechen. So stellen Sie sicher, dass Sie versuchen, Nutzer:innen dann erneut zu aktivieren, wenn sie die App am wahrscheinlichsten nutzen. Sie können dies später ändern und Ihre anfängliche Hypothese testen.

![]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## 3. Schritt: Kampagne starten

Jetzt sind Sie bereit, die Kampagne zu senden. Bestätigen Sie die Einstellungen auf der letzten Seite des Composers und klicken Sie auf **Kampagne starten**!