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

Messaging-Interaktionsdaten beschreiben, wie Nutzer:innen mit einer Campaign oder einem Canvas interagieren, die/den sie erhalten haben (zum Beispiel, wenn Nutzer:innen Campaign A öffnen oder Variante A erhalten). Diese Daten werden für Retargeting verwendet.

## Wann sind Messaging-Interaktionsdaten verfügbar? {#when-is-messaging-interaction-data-available}

Interaktionsdaten sind immer verfügbar. Für aktive Campaigns und Canvases sind Interaktionsdaten immer in Echtzeit verfügbar.

Für gestoppte Campaigns und Canvases verfallen deren Interaktionsdaten nach drei Monaten, es sei denn, sie werden in Retargeting-Filtern von aktiven Campaigns oder Canvases verwendet. Verfallene Interaktionsdaten werden in den Langzeitspeicher verschoben und stehen nicht zur Verfügung, sofern sie nicht mit dem unten beschriebenen Verfahren wiederhergestellt werden.

Verfallene Interaktionsdaten werden niemals gelöscht und können jederzeit wiederhergestellt werden.

### Features, die Interaktionsdaten verwenden {#features-that-use-interaction-data}

Die folgenden Features verwenden Messaging-Interaktionsdaten:

- Retargeting-Filter, die auf eine bestimmte Campaign oder ein bestimmtes Canvas abzielen
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
- Retargeting-Filter, die auf Campaigns oder Canvases mit einem bestimmten Tag abzielen
    - Received Message from Campaign or Canvas with Tag
    - Clicked/Opened Campaign or Canvas With Tag
    - Last Received Message from Campaign or Canvas With Tag
- Die Listen **Campaigns Received** und **Canvas Messages Received** im Nutzerprofil
- Der `/users/export`-Endpunkt
- **Nutzerdaten**-CSV-Exporte auf den Übersichtsseiten von Campaigns und Canvases

Diese Features enthalten keine verfallenen Interaktionsdaten in ihren Ergebnissen. Um verfallene Interaktionsdaten in die Ergebnisse dieser Features einzubeziehen, stellen Sie die Campaign oder das Canvas mit den verfallenen Daten wieder her.

Zum Beispiel können Canvases nicht gestartet werden, wenn die Interaktionsdaten verfallen sind, was bedeutet, dass eine Bearbeitung wie das Hinzufügen eines Teams zum Canvas nicht gespeichert werden kann.

### Features, die keine Interaktionsdaten verwenden {#features-that-dont-use-interaction-data}

Die folgenden Features verwenden **keine** Messaging-Interaktionsdaten, was bedeutet, dass diese Features vom Verfall der Messaging-Interaktionsdaten nicht betroffen sind:

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

## Wie stelle ich Messaging-Interaktionsdaten wieder her? {#how-do-i-restore-messaging-interaction-data}

Um Ihre Interaktionsdaten wiederherzustellen, führen Sie die folgenden Schritte aus:

1. Gehen Sie zur verfallenen Campaign oder zum verfallenen Canvas.
2. Wählen Sie oben auf der Übersichtsseite der Campaign oder des Canvas im Banner **Restore interaction data** aus.

Sie können auch Interaktionsdaten für mehrere Campaigns von der **Campaigns**-Seite aus wiederherstellen, indem Sie die Campaigns auswählen und dann **Restore interaction data** auswählen.

Die Dauer der Wiederherstellung von Interaktionsdaten kann variieren, aber in den meisten Fällen dauert dieser Vorgang zwischen 5 und 15 Minuten. Nach Abschluss der Wiederherstellung erhalten Sie eine E-Mail.

### Wiederherstellung nach Tag {#restoring-by-tag}

Sie können auch Interaktionsdaten für verfallene Campaigns oder Canvases mit einem bestimmten Tag wiederherstellen.

1. Gehen Sie zur **Campaigns**- oder **Canvas**-Seite und suchen Sie nach dem entsprechenden Tag.
2. Wählen Sie Ihre Campaigns oder Canvases aus.
3. Wählen Sie **Restore interaction data** aus, um die Daten für diese Campaigns oder Canvases wiederherzustellen.

Nach weiteren drei Monaten Inaktivität verfallen diese Campaigns oder Canvases erneut.

### Retargeting nach Tag {#retargeting-by-tag}

Campaigns, die Retargeting-Filter verwenden, die nach Tag retargeten, sind nicht von der Verfallsregelung ausgenommen. Retargeting-Filter, die nach Tag retargeten, umfassen:

- Received Message from Campaign or Canvas with Tag
- Clicked/Opened Campaign or Canvas With Tag
- Last Received Message from Campaign or Canvas With Tag

## Wann waren Messaging-Interaktionsdaten in der Vergangenheit verfügbar? {#when-was-messaging-interaction-data-available-in-the-past}

Zuvor wurden Messaging-Interaktionsdaten gelöscht, wenn eine Campaign oder ein Canvas:

- Seit 25 Kalendermonaten keine Nachrichten mehr gesendet hatte, UND
- Nicht für Retargeting in aktiven Campaigns, Canvases oder Content Cards verwendet wurde.

Campaigns und Canvases mit zuvor gelöschten Messaging-Interaktionsdaten können nicht in Retargeting-Filtern für Campaigns, Canvases und Segmente verwendet werden.

## Fehlerbehebung {#troubleshooting}

Beim Versuch, Campaigns, Canvases oder Content Cards mit verfallenen Interaktionsdaten fortzusetzen oder zu dearchivieren, können die folgenden Fehlermeldungen auftreten:

| Fehlermeldung | Wann sie erscheint | Fehlerbehebung |
| --- | --- | --- |
| „Can't resume Canvases because at least one Canvas is using filters or segments that have expired data. Remove these and try again.“ | Wenn Sie versuchen, ein oder mehrere Canvases (Massenaktion) fortzusetzen, die Filter oder Segmente mit verfallenen Interaktionsdaten verwenden | [Stellen Sie die Interaktionsdaten wieder her](#how-do-i-restore-messaging-interaction-data) für die in den Filtern referenzierten Campaigns oder Canvases, oder entfernen Sie die betroffenen Filter aus dem Canvas |
| „Can't resume {name} because it is using filters or segments that have expired data. Remove these and try again.“ | Wenn Sie versuchen, ein einzelnes Canvas fortzusetzen, das Filter oder Segmente mit verfallenen Interaktionsdaten verwendet | [Stellen Sie die Interaktionsdaten wieder her](#how-do-i-restore-messaging-interaction-data) für die in den Filtern referenzierten Campaigns oder Canvases, oder entfernen Sie die betroffenen Filter aus dem Canvas |
| „Resume is only available for stopped Canvases with available interaction data“ | Wenn Sie versuchen, ein Canvas über das Massenaktionsmenü fortzusetzen, das Canvas aber verfallene Interaktionsdaten hat | [Stellen Sie die Interaktionsdaten wieder her](#how-do-i-restore-messaging-interaction-data) für das Canvas |
| „You can't resume these Campaigns. One or more Campaigns include expired filters.“ | Wenn Sie versuchen, eine oder mehrere Campaigns fortzusetzen, die Filter mit verfallenen Interaktionsdaten verwenden | [Stellen Sie die Interaktionsdaten wieder her](#how-do-i-restore-messaging-interaction-data) für die in den Filtern referenzierten Campaigns oder Canvases, oder entfernen Sie die betroffenen Filter aus der Campaign |
| „You can't unarchive these Cards. One or more Cards include expired filters.“ | Wenn Sie versuchen, eine oder mehrere Content Cards zu dearchivieren, die Filter mit verfallenen Interaktionsdaten verwenden | [Stellen Sie die Interaktionsdaten wieder her](#how-do-i-restore-messaging-interaction-data) für die in den Filtern referenzierten Campaigns oder Canvases, oder entfernen Sie die betroffenen Filter aus der Card |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Häufige Fehlermeldungen" }