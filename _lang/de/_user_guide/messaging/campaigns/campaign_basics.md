---
nav_title: Kampagnen-Grundlagen
article_title: Kampagnen-Grundlagen
page_order: 0
page_type: reference
description: "Dieser Referenzartikel behandelt die Grundlagen von Kampagnen und geht auf verschiedene Fragen ein, die Sie sich beim Einrichten Ihrer ersten Kampagnen stellen sollten."
tool: Campaigns

---

# Kampagnen-Grundlagen {#campaigns-basics}

> Dieser Referenzartikel behandelt die Grundlagen von Kampagnen und geht auf verschiedene Fragen ein, die Sie sich beim Einrichten Ihrer ersten Kampagnen stellen sollten.

## Die Struktur von Kampagnen verstehen {#understanding-campaign-structure}

Bevor wir uns mit den Details der Kampagneneinrichtung befassen, lassen Sie uns die wichtigsten Aspekte identifizieren, um zu verstehen, wie Kampagnen über verschiedene Messaging-Kanäle hinweg funktionieren.

Kampagnen sind ein einzelner Nachrichtenschritt, um Ihre Nutzer:innen über Kanäle zu erreichen – häufig auch als Messaging-Kanäle bezeichnet. Zu diesen Messaging-Kanälen gehören Content Cards, E-Mail, In-App-Nachrichten, Push, SMS und MMS sowie Webhooks. Wenn Sie wissen, wo sich Ihre Kund:innen aufhalten, können Sie die passenden Messaging-Kanäle für die Kommunikation nutzen.

## Die geschäftskunden Journey gestalten {#building-the-customer-journey}

Da Kampagnen je nach Messaging-Kanal individuell aufgebaut werden können, können Sie die folgenden fünf W-Fragen der Visualisierung nutzen, um Ihre geschäftskunden-Engagement-Strategien und -Ziele zu identifizieren und zu konzipieren.

### Das „Was“: Benennen Sie Ihre Kampagne {#the-what-name-your-campaign}

*Was möchten Sie den Nutzer:innen helfen zu tun oder zu verstehen?*

Unterschätzen Sie niemals die Kraft des Namens. Braze ist auf Zusammenarbeit ausgelegt, daher ist dies ein hervorragender Zeitpunkt, um festzulegen, wie Sie Ziele mit Ihrem Team kommunizieren. Weitere Informationen zu geschäftskunden Journeys finden Sie in unserem Braze-Lernkurs [Mapping User Lifecycles](https://learning.braze.com/mapping-customer-lifecycles)!

### Das „Wann“: Startbedingungen erstellen {#the-when-create-starting-conditions}

*Wann wird ein:e geschäftskunden auf diese Kampagne stoßen?*

Nutzer:innen können Ihre Kampagne auf drei Arten betreten: bei einem festgelegten Datum und Zeitpunkt (geplant), wenn sie eine bestimmte Aktion ausführen (aktionsbasiert) oder wenn sie etwas tun, das einen API-Aufruf triggert (API-getriggert).

Geplante Zustellung bedeutet, dass Sie Ihre Kampagnen so einstellen, dass sie zu einem bestimmten Zeitpunkt und optional in einem festgelegten Rhythmus gesendet werden. Aktionsbasierte Kampagnen reagieren in Realtime auf bestimmtes Kundenverhalten. Dazu kann ein Kauf oder die Interaktion mit einer anderen Kampagne gehören. API-getriggerte Kampagnen können so eingerichtet werden, dass wichtige Kundenaktionen auf Ihrer Plattform definiert werden, die bei Erreichen einen API-Aufruf an Braze triggern und Ihre Kampagnen versenden.

### Das „Wer“: Eine Entry-Zielgruppe auswählen {#the-who-select-an-entry-audience}

*Wen möchten Sie erreichen?*

Sie können vordefinierte [Segmente]({{site.baseurl}}/user_guide/audience/segments) verwenden, um Nutzer:innen anhand ihrer demografischen, verhaltensbezogenen oder technischen Merkmale und Aktionen anzusprechen. Fügen Sie beim Erstellen Ihrer Kampagne weitere Filter hinzu, um Ihr Segment weiter anzupassen. Nur Nutzer:innen, die diesen Zielgruppenkriterien entsprechen, können die Journey betreten. In der folgenden Tabelle finden Sie eine kurze Übersicht der verfügbaren Filtertypen.

| Filter | Beschreibung |
|---|---|
| Angepasste Daten | Segmentieren Sie Nutzer:innen basierend auf Events und Attributen, die Sie definieren. Kann produktspezifische Features verwenden. |
| Nutzeraktivität | Segmentieren Sie Kund:innen basierend auf ihren Aktionen und Käufen. |
| Retargeting | Segmentieren Sie Kund:innen, denen vorherige Kampagnen gesendet wurden, die sie erhalten oder mit denen sie interagiert haben. |
| Marketing-Aktivität | Segmentieren Sie Kund:innen basierend auf allgemeinem Verhalten wie letztem Engagement oder erhaltenen Kampagnen. |
| Nutzerattribute | Segmentieren Sie Kund:innen nach ihren konstanten Attributen und Merkmalen. |
| Install-Attribution | Segmentieren Sie Kund:innen nach ihrer ersten Quelle, Anzeigengruppe, Kampagne oder Anzeige. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Das „Wer“: Eine Entry-Zielgruppe auswählen" }

### Das „Warum“: Konversions-Events identifizieren {#the-why-identify-conversion-events}

*Warum erstellen Sie diese Kampagne?*

Es ist immer wichtig, ein klar definiertes Ziel vor Augen zu haben, und Kampagnen helfen Ihnen zu verstehen, wie Sie bei KPIs wie Session-Engagement, Käufen und angepassten Events abschneiden. Die Auswahl mindestens eines [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) gibt Ihnen die Möglichkeit, die Performance Ihrer Kampagne zu verstehen.

### Das „Wo“: Meine Zielgruppe finden {#the-where-find-my-audience}

*Wo kann ich meine Zielgruppe am besten erreichen?*

Hier legen wir fest, welche Messaging-Kanäle für Ihre geschäftskunden Journey am sinnvollsten sind. Idealerweise möchten Sie Ihre Nutzer:innen dort erreichen, wo sie am aktivsten sind.

### Das „Wie“: Das Erlebnis gestalten {#the-how-build-the-experience}

*Wie baue ich meine Kampagne auf, nachdem ich die fünf W-Fragen identifiziert habe?*

Ziehen Sie in Betracht, Varianten und A/B-Tests einzurichten, wenn Sie mit dem Kampagnenaufbau vertrauter werden. Beachten Sie, dass Kampagnen bis zu acht Varianten mit einer Kontrollgruppe unterstützen. Nutzen Sie Ihre Kampagnen-Analytics, um fundierte Entscheidungen beim Aufbau Ihrer Kampagne zu treffen und alles von Ihrer segmentierten Zielgruppe bis hin zu Ihrem eigentlichen Nachrichteninhalt anzupassen.