---
nav_title: Content Cards
article_title: Content Cards in Canvas
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt Features und Besonderheiten bei der Verwendung von Content Cards als Messaging-Kanal in Canvas."
tool: Canvas
channel: content cards

---

# Content Cards in Canvas {#content-cards-in-canvas}

> Content Cards können als Teil einer Canvas-Journey an Ihre Kund:innen gesendet werden. Dieser Artikel beschreibt Features und Besonderheiten bei der Verwendung von Content Cards als Messaging-Kanal in Canvas.

Wie bei anderen Canvas-Messaging-Kanälen werden Content Cards an das Gerät der Nutzer:innen gesendet, wenn diese die für den jeweiligen Schritt festgelegten Zielgruppen- und Targeting-Kriterien erfüllen. Nachdem die Content-Card gesendet wurde, ist sie im Feed der berechtigten Nutzer:innen verfügbar, sobald deren Card-Feed das nächste Mal aktualisiert wird.

![Content Cards als Messaging-Kanal für einen Nachrichtenschritt ausgewählt.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

Zwei Optionen, die das Verhalten des Content-Card-Schritts in Canvas beeinflussen, sind das [Ablaufdatum](#content-card-expiration) und die [Entfernung](#removal).

## Ablauf von Content Cards {#content-card-expiration}

Beim Erstellen einer neuen Content-Card können Sie festlegen, wann sie basierend auf dem Sendezeitpunkt aus dem Feed der Nutzer:innen ablaufen soll. Der Countdown für den Ablauf einer Content-Card beginnt, wenn die Nutzer:innen den Nachrichtenschritt im Canvas erreichen, in dem die Card gesendet wird. Die Card ist ab diesem Zeitpunkt im Feed der Nutzer:innen aktiv, bis sie abläuft. Eine Card kann bis zu 30 Tage im Feed der Nutzer:innen existieren.

![Ablaufeinstellungen für eine Content-Card in einem Nachrichtenschritt, die nach drei Stunden aus dem Feed der Nutzer:innen entfernt wird.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### Ablauftypen {#types-of-expiration}

Sie haben zwei Möglichkeiten festzulegen, wann eine Card aus dem Feed der Nutzer:innen verschwinden soll: ein relatives Datum oder ein absolutes Datum.

#### Relative Daten {#relative-dates}

Wenn Sie ein relatives Datum wählen, z. B. „Gesendete Cards nach 5 Tagen aus dem Feed der Nutzer:innen entfernen“, können Sie ein Ablaufdatum von bis zu 30 Tagen festlegen.

#### Absolute Daten {#absolute-dates}

Wenn Sie ein absolutes Datum wählen, z. B. „Gesendete Cards am 1. Dezember 2023 um 16 Uhr entfernen“, gibt es einige Besonderheiten zu beachten.

Obwohl Sie eine Ablaufdauer von mehr als 30 Tagen angeben können, existiert die Content-Card maximal 30 Tage im Feed der Nutzer:innen. Die Angabe einer Dauer von mehr als 30 Tagen ermöglicht es Ihnen, eventuelle Verzögerungen vor dem Auslösen des Nachrichtenschritts zu berücksichtigen, verlängert aber nicht die maximale Lebensdauer der Card im Feed der Nutzer:innen.

Seien Sie vorsichtig, wenn Sie ein Ablaufdatum festlegen, das mehr als 30 Tage nach dem Start des Canvas liegt. Wenn Nutzer:innen den Nachrichtenschritt mehr als 30 Tage vor dem angegebenen Ablaufdatum erreichen, wird die Card nicht gesendet.

#### Personalisierter Ablauf mit Liquid {#personalized-expiry-with-liquid}

Wenn Sie Liquid-Personalisierung verwenden, um die Ablaufdauer festzulegen (z. B. mithilfe angepasster Attribute oder Canvas-Eingangs-Eigenschaften), unterscheidet sich das Verhalten von absoluten oder relativen Daten:

- Wenn der personalisierte Ablauf eine Dauer von mehr als 30 Tagen ergibt, begrenzt Braze diese automatisch auf das Maximum von 30 Tagen.
- Die Content-Card wird dennoch mit der begrenzten Ablaufdauer an die Nutzer:innen gesendet.
- Die Nutzer:innen schreiten zum nächsten Schritt im Canvas fort.

Diese Begrenzung stellt sicher, dass Cards mit personalisiertem Ablauf auch dann zugestellt werden, wenn die aufgelöste Dauer das Plattformlimit überschreitet. Im Verarbeitungsprotokoll wird das Ergebnis als „Personalized expiration capped by max TTL“ angezeigt, mit Details wie `reason=capped_by_max_ttl` und `capped=true`.

### Ablaufverhalten {#expiration-behavior}

Die Content-Card bleibt im Feed der Nutzer:innen verfügbar, bis sie ihr Ablaufdatum erreicht – auch wenn die Nutzer:innen zu nachfolgenden Schritten in der Canvas-Journey fortschreiten. Wenn Sie nicht möchten, dass die Content-Card noch aktiv ist, wenn die nächsten Schritte im Canvas ausgeliefert werden, stellen Sie sicher, dass der Ablauf kürzer ist als die Verzögerung bei nachfolgenden Schritten.

Nach dem Ablauf einer Content-Card wird sie bei der nächsten Aktualisierung automatisch aus dem Feed der Nutzer:innen entfernt, auch wenn sie noch nicht angesehen wurde.

## Entfernung von Content Cards {#removal}

Content Cards können entfernt werden, wenn Nutzer:innen einen Kauf tätigen oder ein angepasstes Event ausführen. Sie können eines der folgenden Ereignisse als Entfernungsereignis auswählen: **Perform Custom Event** und **Place Order**. Wählen Sie dann **Add Trigger**.

![„Cards entfernen, wenn Nutzer:innen einen Kauf tätigen oder ein angepasstes Event ausführen“ ausgewählt, mit dem Trigger, Cards für Nutzer:innen zu entfernen, die eine bestimmte Bestellung aufgeben.]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## Berichte und Analytics {#reporting-and-analytics}

Nach dem Start eines Content-Card-Schritts in Canvas können Sie verschiedene Metriken für diesen Schritt analysieren. Dazu gehören die Anzahl der gesendeten Nachrichten, eindeutige tägliche Impressionen, Konversionsraten, Gesamtumsatz und mehr.

![Analytics für einen Nachrichtenschritt mit der Content-Card-Nachrichten-Performance.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

Weitere Informationen zu den verfügbaren Metriken und deren Definitionen finden Sie in unserem [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary/).

## Anwendungsfälle {#use-cases}

### Aktionsangebote {#promotional-offers}

Fügen Sie Cards zum Feed der Nutzer:innen hinzu, sobald diese sich für bestimmte Aktionen und Werbeangebote qualifizieren. Wenn Nutzer:innen beispielsweise nach einer Aktion oder einem Kauf für ein neues Angebot berechtigt werden, können Sie ihnen über Canvas eine Content-Card – zusätzlich zu anderen Messaging-Kanälen – senden, sodass das Angebot beim nächsten Öffnen der App verfügbar ist.

### Push-Benachrichtigungs-Posteingang {#push-notification-inbox}

Es gibt Situationen, in denen Nutzer:innen eine Push-Benachrichtigung verwerfen oder eine E-Mail löschen, Sie sie aber dennoch an das Angebot erinnern oder es bewerben möchten, falls sie es sich anders überlegen.

Mit Canvas können Sie eine Komponente hinzufügen, die sowohl eine Content-Card als auch eine Push-Benachrichtigung sendet, um Nutzer:innen einen persistenten „Posteingang“ mit Cards zu bieten, die zu den per Push gesendeten Aktionsnachrichten passen.

### Mehrere Feeds basierend auf Kategorien {#multiple-feeds-based-on-categories}

Sie können Ihre Content Cards in mehrere Feeds aufteilen, basierend auf Kategorien wie verschiedenen Themen, die Nutzer:innen durchsuchen können, oder transaktionalen und Marketing-Feeds. Weitere Informationen zum Erstellen mehrerer Feeds mithilfe von Schlüssel-Wert-Paaren finden Sie in unserem Leitfaden zum [Anpassen von Content-Card-Feeds]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).