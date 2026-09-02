---
nav_title: Passive Nutzer:innen zurückgewinnen
article_title: Passive Nutzer:innen zurückgewinnen
page_order: 1
page_type: tutorial
description: "Dieser Artikel befasst sich mit dem Thema passiver Nutzer:innen und zeigt, wie Sie Braze Campaigns effektiv nutzen können, um diese Nutzer:innen erneut zu aktivieren."
tool:
  - Segments
  - Campaigns

---

# Passive Nutzer:innen zurückgewinnen {#capture-lapsing-users}

> Wenn Ihre Zielgruppe schrumpft, ist es entscheidend, sie zurückzugewinnen. Mit Braze können Sie automatisierte, wiederkehrende Campaigns zur erneuten Interaktion einrichten, um passive Nutzer:innen zu erreichen. Sie können den Zeitrahmen und die Häufigkeit der erneuten Interaktion wählen, die am besten zu Ihrer App passen. Zur Veranschaulichung starten wir hier mit einem 14-tägigen Plan zur erneuten Interaktion.

Weitere Informationen zum Targeting von Nutzer:innen finden Sie in unserem [Braze-Lernkurs](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) zur Kampagneneinrichtung!

## Schritt 1: Nutzer:innen segmentieren {#step-1-segment-users}

Zunächst erstellen wir ein Segment, um Nutzer:innen anzusprechen, die Ihre App in den letzten zwei Wochen nicht verwendet haben. Dazu nutzen wir die folgenden Filter:

- **Letzte App-Nutzung** vor mehr als 2 Wochen
- **Letzte App-Nutzung** vor weniger als 3 Wochen

![Screenshot zu Schritt 1: Nutzer:innen segmentieren.]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Geben Sie dem Segment einen einprägsamen Namen, z. B. „Passive Nutzer:innen – 2 Wochen“. Da wir die Campaign so einrichten, dass sie wöchentlich wiederholt wird, möchten wir sicherstellen, dass mindestens eine Woche an Nutzer:innen im Segment erfasst wird. Aus diesem Grund haben wir Nutzer:innen ausgewählt, die die App zuletzt vor zwei bis drei Wochen verwendet haben.

## Schritt 2: Campaign erstellen {#step-2-create-a-campaign}

Klicken Sie als Nächstes auf **Create Campaign** und wählen Sie den Campaign-Typ aus, den wir an dieses Segment senden werden. In diesem Beispiel erstellen wir eine neue [Push-Campaign]({{site.baseurl}}/user_guide/channels/push/create_a_push_message).

![Klicken Sie als Nächstes auf „Create Campaign“ und wählen Sie den Campaign-Typ aus, den wir an dieses Segment senden werden. In diesem Beispiel erstellen wir eine neue Push-Campaign.]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Wir nennen die Campaign „Message to Lapsed Users - 2 Weeks“ und erstellen dann den Inhalt unserer Nachricht. In diesem Beispiel werden wir nur iOS-Nutzer:innen ansprechen, aber Sie können Braze sowohl für Android- als auch für iOS-Push-Benachrichtigungen nutzen.

Je kürzer die letzte Nutzung der App zurückliegt, desto wichtiger ist es, aktuell und relevant zu sein. Wenn Sie Nutzer:innen nach zwei Wochen ohne App-Nutzung kontaktieren, ist es wichtig, relevante Inhalte zu präsentieren und die Vorteile der App hervorzuheben.

![Screenshot zu Schritt 2: Campaign erstellen.]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

Als Nächstes erstellen wir einen wiederkehrenden Zeitplan, um unsere wöchentliche Nachricht donnerstags um 17:45 Uhr mit [Zustellung nach Ortszeit]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer) unter **Time-Based Scheduling Options** zu senden. Wir empfehlen, Ihren Sitzungsgraphen zu analysieren, um Nutzer:innen kurz vor Zeiten mit hoher Nutzung anzusprechen. So stellen Sie sicher, dass Sie versuchen, Personen dann erneut zu aktivieren, wenn sie die App am wahrscheinlichsten nutzen. Sie können dies später ändern und Ihre anfängliche Hypothese testen.

![Als Nächstes erstellen wir einen wiederkehrenden Zeitplan, um unsere wöchentliche Nachricht donnerstags um 17:45 Uhr mit Zustellung nach Ortszeit unter „Time-Based Scheduling Options“ zu senden. Wir empfehlen, Ihren Sitzungsgraphen zu analysieren, um Nutzer:innen kurz vor Zeiten mit hoher Nutzung anzusprechen. So stellen Sie sicher, dass Sie versuchen, Personen dann erneut zu aktivieren, wenn sie die App am wahrscheinlichsten nutzen. Sie können dies später ändern und Ihre anfängliche Hypothese testen.]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## Schritt 3: Campaign starten {#step-3-launch-the-campaign}

Jetzt können Sie die Campaign absenden. Bestätigen Sie die Einstellungen auf der letzten Seite des Composers und klicken Sie auf **Launch Campaign**!