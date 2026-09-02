---
nav_title: "Messaging-Interaktionsdaten"
article_title: "Messaging-Interaktionsdaten"
alias: "/messaging_interaction_data/"
page_order: 1
description: "Dieser Referenzartikel behandelt Interaktionsdaten von Campaigns und Canvases sowie deren Verfügbarkeit."
page_type: reference
---

# Über die Verfügbarkeit von Messaging-Interaktionsdaten {#about-messaging-interaction-data-availability}

> Erfahren Sie mehr über Messaging-Interaktionsdaten für Campaigns und Canvases, einschließlich der Aufbewahrungsdauer durch Braze und der Features, die sie für Retargeting verwenden.

## Was sind Messaging-Interaktionsdaten? {#what-is-messaging-interaction-data}

Messaging-Interaktionsdaten beziehen sich darauf, wie Nutzer:innen mit einer Campaign oder einem Canvas interagieren, die sie erhalten haben (zum Beispiel, wenn Nutzer:innen Campaign A öffnen oder Variante A erhalten). Diese Daten werden für Retargeting verwendet.

## Wann sind Interaktionsdaten für Nachrichten verfügbar? {#when-is-messaging-interaction-data-available}

Interaktionsdaten sind immer verfügbar. Für aktive Campaigns und Canvases sind Interaktionsdaten immer in Echtzeit verfügbar.

Für gestoppte Campaigns und Canvases laufen deren Interaktionsdaten nach drei Monaten ab, es sei denn, sie werden in Retargeting-Filtern von aktiven Campaigns oder Canvases verwendet. Abgelaufene Interaktionsdaten werden in den Langzeitspeicher verschoben und stehen nicht zur Verfügung, sofern sie nicht mit dem beschriebenen Verfahren wiederhergestellt werden.

Abgelaufene Interaktionsdaten werden niemals gelöscht und können jederzeit wiederhergestellt werden.

### Features, die Interaktionsdaten verwenden {#features-that-use-interaction-data}

Die folgenden Features verwenden Interaktionsdaten für Nachrichten:

- Retargeting-Filter, die auf eine bestimmte Campaign oder ein bestimmtes Canvas retargeten
    - Clicked Alias in Campaign
    - Clicked Alias in Canvas Step
    - Clicked/Opened Campaign
    - Clicked/Opened Step
    - Converted From Campaign
    - Converted From Canvas
    - Entered Canvas Variation
    - In Campaign Control Group
    - In Canvas Control Group
    - Last Received Message from Specific Campaign
    - Last Received Message from Specific Canvas Step
    - Received Campaign Variant
    - Received Message from Campaign
    - Received Message from Canvas Step
- Retargeting-Filter, die auf Campaigns oder Canvases mit einem bestimmten Tag retargeten
    - Received Message from Campaign or Canvas with Tag
    - Clicked/Opened Campaign or Canvas With Tag
    - Last Received Message from Campaign or Canvas With Tag
- Die Listen **Campaigns Received** und **Canvas Messages Received** im Nutzerprofil
- Der Endpunkt `/users/export`
- **Nutzerdaten**-CSV-Exporte auf den Zusammenfassungsseiten von Campaigns und Canvases

Diese Features enthalten keine abgelaufenen Interaktionsdaten in ihren Ergebnissen. Um abgelaufene Interaktionsdaten in die Ergebnisse dieser Features einzubeziehen, stellen Sie die Campaign oder das Canvas mit abgelaufenen Daten wieder her.

Zum Beispiel können Canvases nicht gestartet werden, wenn die Interaktionsdaten abgelaufen sind, was bedeutet, dass eine Bearbeitung wie das Hinzufügen eines Teams zum Canvas nicht gespeichert werden kann.

### Features, die keine Interaktionsdaten verwenden {#features-that-dont-use-interaction-data}

Die folgenden Features verwenden **keine** Interaktionsdaten für Nachrichten, d. h. diese Features sind vom Ablauf der Interaktionsdaten für Nachrichten nicht betroffen:

- Campaign- und Canvas-Einrichtung
- Campaign- und Canvas-Analytics
- Analytics-Berichte (wie Berichts-Builder, Query Builder und Engagement-Berichte)
- Currents
- Snowflake Data Share
- Segmenterweiterungen
- Datenpunkte
- Die folgenden Retargeting-Filter:
    - Clicked Alias in Any Campaign or Canvas Step
    - Feature Flags
    - Hard Bounced
    - Has Marked You As Spam
    - Has Never Received a Message from Campaign or Canvas Step
    - Invalid Phone Number
    - Last Engaged With Message
    - Last Enrolled in Any Control Group
    - Last In App Message Impression
    - Last Received Any Message
    - Last Received Email
    - Last Received Push
    - Last Received SMS
    - Last Received Webhook
    - Last Received WhatsApp
    - Last Sent Specific SMS Inbound Keyword Category
    - Last Viewed News Feed
    - News Feed View Count

## Wie stelle ich Interaktionsdaten für Nachrichten wieder her? {#how-do-i-restore-messaging-interaction-data}

Um Ihre Interaktionsdaten wiederherzustellen, führen Sie die folgenden Schritte aus:

1. Gehen Sie zur abgelaufenen Campaign oder zum abgelaufenen Canvas.
2. Wählen Sie oben auf der Landing-Page der Campaign oder des Canvas im Banner **Restore interaction data** aus.

Sie können auch Interaktionsdaten für mehrere Campaigns von der Seite **Campaigns** wiederherstellen, indem Sie die Campaigns auswählen und dann **Restore interaction data** auswählen.

Die Dauer der Wiederherstellung von Interaktionsdaten kann variieren, aber in den meisten Fällen dauert dieser Vorgang zwischen 5 und 15 Minuten. Nach Abschluss der Wiederherstellung erhalten Sie eine E-Mail.

### Wiederherstellung nach Tag {#restoring-by-tag}

Sie können auch Interaktionsdaten für abgelaufene Campaigns oder Canvases mit einem bestimmten Tag wiederherstellen.

1. Gehen Sie zur Seite **Campaigns** oder **Canvas** und suchen Sie nach dem entsprechenden Tag.
2. Wählen Sie Ihre Campaigns oder Canvases aus.
3. Wählen Sie **Restore interaction data** aus, um die Daten für diese Campaigns oder Canvases wiederherzustellen.

Nach weiteren drei Monaten Inaktivität laufen diese Campaigns oder Canvases erneut ab.

### Retargeting nach Tag {#retargeting-by-tag}

Campaigns, die Retargeting-Filter verwenden, die nach Tag retargeten, sind nicht von der Ablaufzeit ausgenommen. Retargeting-Filter, die nach Tag retargeten, umfassen:

- Received Message from Campaign or Canvas with Tag
- Clicked/Opened Campaign or Canvas With Tag
- Last Received Message from Campaign or Canvas With Tag

## Wann waren Messaging-Interaktionsdaten in der Vergangenheit verfügbar? {#when-was-messaging-interaction-data-available-in-the-past}

Zuvor wurden Messaging-Interaktionsdaten gelöscht, wenn eine Campaign oder ein Canvas:

- Seit 25 Kalendermonaten keine Nachrichten mehr gesendet hatte, UND
- In keiner aktiven Campaign, keinem Canvas und keinen Content Cards für Retargeting verwendet wurde.

Campaigns und Canvases mit zuvor gelöschten Messaging-Interaktionsdaten können nicht in Retargeting-Filtern für Campaigns, Canvases und Segments verwendet werden.

## Fehlerbehebung {#troubleshooting}

### Warum zeigt das Ablaufdatum einer Campaign oder eines Canvas immer „morgen“ an? {#why-does-a-campaign-or-canvas-expiration-date-keep-showing-tomorrow}

Wenn eine gestoppte Campaign oder ein gestopptes Canvas noch von einem aktiven Retargeting-Filter referenziert wird (zum Beispiel in einem aktiven Segment, einer Campaign, einem Canvas oder einer Content-Card), gibt Braze die zugehörigen Interaktionsdaten noch nicht frei.

In diesem Fall spiegelt das in der UI angezeigte Ablaufdatum den nächsten geplanten Bereinigungslauf wider, sodass es als „morgen“ erscheinen und sich weiter nach vorne verschieben kann, solange noch Referenzen bestehen.

Nachdem Sie alle aktiven Retargeting-Referenzen entfernt haben, werden die Interaktionsdaten im nächsten Bereinigungszyklus freigegeben (in der Regel am nächsten Tag).

Beim Versuch, Campaigns, Canvases oder Content Cards mit abgelaufenen Interaktionsdaten fortzusetzen oder aus dem Archiv zu holen, können die folgenden Fehlermeldungen auftreten:

| Fehlermeldung | Wann sie erscheint | Fehlerbehebung |
| --- | --- | --- |
| „Can't resume Canvases because at least one Canvas is using filters or segments that have expired data. Remove these and try again.“ | Wenn Sie versuchen, ein oder mehrere Canvases fortzusetzen (Massenaktion), die Filter oder Segments mit abgelaufenen Interaktionsdaten verwenden | [Interaktionsdaten wiederherstellen](#how-do-i-restore-messaging-interaction-data) für die in den Filtern referenzierten Campaigns oder Canvases, oder die betroffenen Filter aus dem Canvas entfernen |
| „Can't resume {name} because it is using filters or segments that have expired data. Remove these and try again.“ | Wenn Sie versuchen, ein einzelnes Canvas fortzusetzen, das Filter oder Segments mit abgelaufenen Interaktionsdaten verwendet | [Interaktionsdaten wiederherstellen](#how-do-i-restore-messaging-interaction-data) für die in den Filtern referenzierten Campaigns oder Canvases, oder die betroffenen Filter aus dem Canvas entfernen |
| „Resume is only available for stopped Canvases with available interaction data“ | Wenn Sie versuchen, ein Canvas über das Massenaktionsmenü fortzusetzen, dessen Interaktionsdaten jedoch abgelaufen sind | [Interaktionsdaten wiederherstellen](#how-do-i-restore-messaging-interaction-data) für das Canvas |
| „You can't resume these Campaigns. One or more Campaigns include expired filters.“ | Wenn Sie versuchen, eine oder mehrere Campaigns fortzusetzen, die Filter mit abgelaufenen Interaktionsdaten verwenden | [Interaktionsdaten wiederherstellen](#how-do-i-restore-messaging-interaction-data) für die in den Filtern referenzierten Campaigns oder Canvases, oder die betroffenen Filter aus der Campaign entfernen |
| „You can't unarchive these Cards. One or more Cards include expired filters.“ | Wenn Sie versuchen, eine oder mehrere Content Cards aus dem Archiv zu holen, die Filter mit abgelaufenen Interaktionsdaten verwenden | [Interaktionsdaten wiederherstellen](#how-do-i-restore-messaging-interaction-data) für die in den Filtern referenzierten Campaigns oder Canvases, oder die betroffenen Filter aus der Card entfernen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Häufige Fehlermeldungen" }