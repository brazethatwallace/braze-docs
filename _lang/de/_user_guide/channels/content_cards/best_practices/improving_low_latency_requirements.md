---
nav_title: Niedrige Latenz verbessern
article_title: Niedrige Latenz für Content Cards als Banner verbessern
page_order: 10
description: "Dieser Artikel behandelt Strategien, um sicherzustellen, dass die Anforderungen an niedrige Latenz bei Content Cards erfüllt werden."
channel:
  - content cards
---

# Latenz für Content Cards als Banner verbessern {#improve-latency-for-content-cards-as-banners}

> Wenn Sie bei Ihrer Content-Cards-Implementierung für kritische Anwendungsfälle wie Homepage-Banner Latenzprobleme feststellen, finden Sie auf dieser Seite Strategien und Tipps, die Ihnen helfen, das Rendering zu beschleunigen.

{% alert tip %}
Möchten Sie auffällige, angepasste Banner in Ihrer App oder auf Ihrer Website anzeigen? Probieren Sie den [Banner]({{site.baseurl}}/user_guide/channels/banners)-Kanal aus, der speziell für Banner-Anwendungsfälle mit niedriger Latenz entwickelt wurde.
{% endalert %}

## Verwenden Sie zeitgesteuerten Entry statt aktionsbasierten Entry {#use-scheduled-entry-instead-of-action-based-entry}

Aktionsbasierte Content-Cards in Campaigns und Canvases erfordern eine Hintergrundverarbeitung. Braze muss zunächst eine Benachrichtigung über die auslösende Aktion erhalten (z. B. einen erfolgten Kauf oder den Start einer Sitzung), bevor eine Card für eine:n Nutzer:in erstellt werden kann. Dadurch kommt es zu einer Verzögerung, bis diese Cards verfügbar sind.

Aktionsbasierte Cards bringen zusätzliche Komplexität in Ihre Anwendung, da Sie möglicherweise kontinuierlich abfragen und aktualisieren müssen, um darauf zu warten, dass die Card verfügbar wird. Konfigurieren Sie Ihre Card stattdessen als `Scheduled Entry`, was als Verfügbarkeitsfenster fungiert, sodass die Card für die angesprochene Zielgruppe immer verfügbar ist.

Wenn Sie Ihre Cards im Voraus planen, sind sie bereit und warten darauf, dass Nutzer:innen Ihre App öffnen und Cards abrufen.

## Verwenden Sie die Sendelogik „At First Impression“ {#use-at-first-impression-send-logic}

Zusammen mit geplanten Zustellungen vermeidet die Option `At First Impression` Latenz, da eine Content-Card schnell erstellt und in Braze gespeichert wird. Die Option `At Campaign Launch` erstellt alle Content-Cards für alle segmentierten Nutzer:innen im Voraus, was einige Zeit in Anspruch nehmen kann. Die Option `At First Impression` generiert eine Content-Card für Nutzer:innen erst dann, wenn sie zum ersten Mal angefordert wird – zum Beispiel, wenn Nutzer:innen Ihre App zum ersten Mal öffnen.

Das bedeutet, dass zusammen mit dem geplanten Entry die Content-Cards sofort verfügbar sind, sobald Sie sie benötigen – entweder zu Beginn der Sitzung oder innerhalb eines zeitbasierten Berechtigungsfensters.

## Bedenken Sie, dass der Canvas-Entry Voraussetzung für den Erhalt von Cards ist {#remember-that-canvas-entry-is-a-prerequisite-for-receiving-cards}

Wenn Sie Canvas verwenden, denken Sie daran, dass Nutzer:innen zunächst basierend auf Ihren konfigurierten Entry-Kriterien in den Canvas eintreten müssen und *dann* den Content-Card-Nachrichtenschritt durchlaufen müssen. Erst dann ist die Card für Ihre App oder Website verfügbar. Beachten Sie, dass es eine eingebaute Latenz gibt, bis die Card erstellt wird, nachdem Nutzer:innen den Schritt durchlaufen haben, was die Verfügbarkeit der Card verzögern kann.

## Content Cards nicht übermäßig aktualisieren {#dont-refresh-cards-excessively}

Content Cards werden vom SDK bei jedem neuen Sitzungsstart automatisch aktualisiert. Sie können auch jederzeit während einer aktiven Sitzung manuell eine Aktualisierung der Content Cards anfordern. Bei unterstützten SDK-Versionen sendet Braze Zustellungen und Entfernungen während der Sitzung per [Realtime-Zustellung]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#real-time-delivery) an das Gerät, wodurch die Notwendigkeit manueller Aktualisierungen reduziert wird.

Das Aufrufen der Methode `requestContentCardsRefresh` und zu häufiges Aktualisieren kann zu Rate-Limiting führen. Wenn Ihre App vorübergehend einem Rate-Limit unterliegt, können Sie Content Cards möglicherweise nicht aktualisieren, wenn Sie es benötigen oder zu einem kritischen Zeitpunkt im Engagement der Nutzer:innen mit Ihrer App.

Um dies zu vermeiden, rufen Sie diese Aktualisierungsmethode nur zu wichtigen Zeitpunkten im Lebenszyklus der Nutzer:innen auf, z. B. nachdem Nutzer:innen einen Kauf getätigt oder ihr Abo-Level upgegradet haben.

## Connected Content vermeiden {#avoid-including-connected-content}

Connected Content reichert Content Cards mit Daten aus eigenen oder Drittanbieter-APIs an. Wenn es jedoch in einer Content-Card-Nachricht enthalten ist, blockiert es die Verfügbarkeit der Karte, bis die Connected-Content-Netzwerkanfrage abgeschlossen werden kann. In einigen Fällen führt dies dazu, dass SDKs den Versuch einige Sekunden später wiederholen, um die Rendering-Logik Ihrer App nicht zu verzögern, die möglicherweise darauf wartet, dass das SDK seine Aktualisierungsaufgabe abschließt.

Wenn Sie Connected Content verwenden müssen, planen Sie diese Karten im Voraus und nutzen Sie die Option `At Campaign Launch`, damit die Karten erstellt werden, bevor die nächste Sitzung der Nutzer:innen beginnt. Beachten Sie, dass diese Karten nicht sofort verfügbar sind, da Braze alle Karten für alle berechtigten Nutzer:innen erstellt.