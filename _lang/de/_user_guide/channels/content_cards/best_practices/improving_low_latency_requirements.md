---
nav_title: Niedrige Latenz verbessern
article_title: Niedrige Latenz für Content-Cards als Banner verbessern
page_order: 10
description: "Dieser Artikel behandelt Strategien, um sicherzustellen, dass die Anforderungen an niedrige Latenz bei Content-Cards erfüllt werden."
channel:
  - content cards
---

# Latenz für Content-Cards als Banner verbessern

> Wenn Sie bei Ihrer Content-Cards-Implementierung für kritische Anwendungsfälle wie Homepage-Banner Latenzprobleme feststellen, finden Sie auf dieser Seite Strategien und Tipps, die Ihnen helfen, das Rendering zu beschleunigen.

{% alert tip %}
Möchten Sie auffällige, angepasste Banner in Ihrer App oder auf Ihrer Website anzeigen? Probieren Sie [Banner]({{site.baseurl}}/user_guide/channels/banners/) aus, die speziell für Banner-Anwendungsfälle mit niedriger Latenz entwickelt wurden.
{% endalert %}

## Geplanten Eingang statt aktionsbasierten Eingang verwenden

Aktionsbasierte Cards in Kampagnen und Canvases erfordern eine Hintergrundverarbeitung. Braze muss zunächst eine Benachrichtigung über die auslösende Aktion erhalten (z. B. einen Kauf oder einen Sitzungsstart), bevor eine Card für eine:n Nutzer:in erstellt werden kann. Daher kommt es zu einer Verzögerung, bevor diese Cards verfügbar sind.

Aktionsbasierte Cards erhöhen die Komplexität Ihrer Anwendung, da Sie möglicherweise kontinuierlich abfragen und aktualisieren müssen, um auf die Verfügbarkeit der Card zu warten. Konfigurieren Sie Ihre Card stattdessen als `Scheduled Entry`, was als Verfügbarkeitsfenster dient, in dem die Card für die Zielgruppe immer verfügbar ist.

Wenn Sie Ihre Cards im Voraus planen, sind sie bereit und warten darauf, dass Nutzer:innen Ihre App öffnen und Cards anfordern.

## Sendelogik „At First Impression" verwenden

In Kombination mit geplanten Sendungen vermeidet die Option `At First Impression` Latenz, da die Card schnell in Braze erstellt und gespeichert wird. Die Option `At Campaign Launch` erstellt alle Cards für alle segmentierten Nutzer:innen im Voraus, was einige Zeit in Anspruch nehmen kann. Die Option `At First Impression` generiert eine Card für eine:n Nutzer:in erst dann, wenn sie zum ersten Mal angefordert wird – zum Beispiel, wenn eine Person Ihre App zum ersten Mal öffnet.

Das bedeutet, dass Cards in Kombination mit geplantem Eingang sofort verfügbar sind, sobald Sie sie benötigen – entweder beim Sitzungsstart oder für ein zeitbasiertes Berechtigungsfenster.

## Beachten Sie, dass der Canvas-Eingang Voraussetzung für den Empfang von Cards ist

Wenn Sie Canvas verwenden, denken Sie daran, dass Nutzer:innen zunächst basierend auf Ihren konfigurierten Eingangskriterien in den Canvas eintreten müssen und *dann* den Content-Card-Nachrichtenschritt durchlaufen müssen. Erst dann ist die Card für Ihre App oder Website verfügbar. Beachten Sie, dass es eine eingebaute Latenz für die Erstellung der Card gibt, sobald die Person den Schritt durchläuft, was die Verfügbarkeit der Card verzögern kann.

## Cards nicht übermäßig aktualisieren

Content-Cards werden vom SDK bei jedem neuen Sitzungsstart automatisch aktualisiert. Sie können auch jederzeit während einer aktiven Sitzung manuell eine Aktualisierung der Content-Cards anfordern.

Ein zu häufiger Aufruf der Methode `requestContentCardsRefresh` kann zu Rate-Limiting führen. Wenn Ihre App vorübergehend einem Rate-Limit unterliegt, können Sie Cards möglicherweise nicht aktualisieren, wenn Sie es brauchen oder zu einem kritischen Zeitpunkt im Engagement der Nutzer:innen mit Ihrer App.

Um dies zu vermeiden, rufen Sie diese Aktualisierungsmethode nur zu wichtigen Zeitpunkten im Lebenszyklus der Nutzer:innen auf, z. B. nach einem Kauf oder nach einem Abo-Upgrade.

## Connected-Content vermeiden

Connected-Content reichert Content-Cards mit Erst- oder Drittanbieter-API-Daten an. Wenn Connected-Content jedoch in einer Content-Card-Nachricht enthalten ist, blockiert es die Verfügbarkeit der Card, bis die Connected-Content-Netzwerkanfrage abgeschlossen werden kann. In einigen Fällen führt dies dazu, dass SDKs einige Sekunden später einen erneuten Versuch starten, um die Rendering-Logik Ihrer App nicht zu verzögern, die möglicherweise auf den Abschluss der SDK-Aktualisierung wartet.

Wenn Sie Connected-Content verwenden müssen, planen Sie diese Cards im Voraus und nutzen Sie die Option `At Campaign Launch`, damit die Cards vor der nächsten Sitzung der Nutzer:innen vorab erstellt werden. Beachten Sie, dass diese Cards nicht sofort verfügbar sind, da Braze alle Cards für alle berechtigten Nutzer:innen erstellt.