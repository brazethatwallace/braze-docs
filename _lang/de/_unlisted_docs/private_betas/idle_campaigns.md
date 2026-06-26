---
nav_title: "Inaktive Campaigns und Canvases"
permalink: "/idle_campaigns_canvases/"
hidden: true
---

# Inaktive Campaigns und Canvases {#idle-campaigns-and-canvases}

> Dieser Referenzartikel erklärt den Inaktiv-Status für Campaigns und Canvases und beantwortet häufig gestellte Fragen.

{% alert note %}
Ab 2024 werden Canvases als **Inaktiv** markiert und gestoppt, ähnlich wie Campaigns. Wenn Canvases inaktiv oder gestoppt sind, folgen sie der in diesem Dokument beschriebenen Logik.
{% endalert %}

Campaigns und Canvases erhalten den Status „Inaktiv“, wenn sie seit einiger Zeit keine Nachrichten gesendet oder keine Nutzer:innen aufgenommen haben. Diese Campaigns und Canvases werden automatisch zu ihrem zugehörigen Stoppdatum gestoppt. Sie können nach inaktiven Campaigns und Canvases filtern, um Ihre Liste von Campaigns und Canvases zu sortieren und zu verwalten.

Campaigns und Canvases mit Enddaten und einmaligen Sendungen sind 7 Tage lang inaktiv, bevor sie automatisch gestoppt werden. Campaigns und Canvases, die seit 11 Monaten keine Nachricht gesendet haben, sind 1 Monat lang inaktiv, bevor sie automatisch gestoppt werden.

## Inaktive Campaigns {#idle-campaigns}

Fortlaufend werden inaktive Campaigns, die die folgenden Kriterien erfüllen, gestoppt:

- Eine geplante einmalige Sendung liegt mehr als sieben Tage nach ihrem Sendedatum
- Eine geplante oder aktionsbasierte Campaign mit einem Enddatum liegt mehr als sieben Tage nach ihrem Enddatum
- Eine Campaign ohne Enddatum, die seit einem Jahr keine Nachrichten gesendet hat

Bei Campaigns ohne Enddaten wird der Einjahres-Countdown zum Stoppen der Campaign zurückgesetzt, wenn eine Nachricht gesendet oder die Campaign aktualisiert wird. Wenn Campaigns gestoppt werden, benachrichtigt Braze die Kund:innen in ihrem Dashboard und per E-Mail.

Campaigns werden zum späteren der beiden folgenden Zeitpunkte gestoppt: dem Standard-Stoppdatum oder einem Tag nach ihrer letzten Conversion-Frist. Sendungen, die aus einer Gewinnervariante oder personalisierten Variante resultieren, werden als geplante Sendungen behandelt und sieben Tage nach dem Versand der Gewinnervariante oder personalisierten Variante gestoppt. Alle Campaigns werden täglich um 4 Uhr UTC für alle Braze-Nutzer:innen gestoppt.

Content Cards werden erst nach Ablauf ihrer Gültigkeitsfrist gestoppt und unterliegen ebenfalls den oben genannten Kriterien sowie der Conversion-Frist-Regel.

In dieser Tabelle erfahren Sie, wie Sie eine inaktive Campaign aktiv halten:

| Grund für den Inaktiv-Status                                                                              | Schritte, um die Campaign zu aktivieren                     |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Campaigns mit geplanten einmaligen Sendungen, deren Sendedatum überschritten ist                 | Planen Sie eine zukünftige Sendung                            |
| Campaigns, die geplant oder aktionsbasiert sind, Enddaten haben und deren Enddatum überschritten ist | Verlängern Sie das Enddatum                               |
| Campaigns ohne Enddatum, die seit einem Jahr keine Nachrichten gesendet haben                                | Senden Sie eine Nachricht oder nehmen Sie eine beliebige Änderung an der Campaign vor |
| Campaigns mit Enddaten und einmaligen Sendungen | Planen Sie eine zukünftige Sendung |
| Campaigns, die seit 11 Monaten keine Nachricht gesendet haben | Senden Sie eine Nachricht oder nehmen Sie eine beliebige Änderung an der Campaign vor |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### In-App-Nachricht-Campaigns {#in-app-message-campaigns}

Wenn eine In-App-Nachricht-Campaign keine Impressionen hat und seit über 30 Tagen nicht bearbeitet wurde, wird sie zu einer inaktiven Campaign. Eine inaktive In-App-Nachricht-Campaign wird weiterhin gemäß ihrer Konfiguration ausgeliefert, aber die In-App-Nachricht wird zu einer vorlagenbasierten In-App-Nachricht.

Wenn Ihre Nutzer:innen ein Impressions-Ereignis auslösen oder der Marketer die Campaign bearbeitet, wird die Campaign wieder in den aktiven Status versetzt und der 30-Tage-Zähler wird zurückgesetzt.

## Inaktive Canvases {#idle-canvases}

Fortlaufend werden inaktive Canvases, die die folgenden Kriterien erfüllen, gestoppt:

- Eine geplante einmalige Sendung liegt mehr als 7 Tage nach ihrem Sendedatum und ihrer maximalen Dauer
- Ein geplanter oder aktionsbasierter Canvas mit einem Enddatum liegt mehr als 7 Tage nach seinem Enddatum und seiner maximalen Dauer
- Ein Canvas ohne Enddatum hat seit über 12 Monaten keine Nutzer:innen aufgenommen oder wurde nicht bearbeitet, und seine maximale Dauer ist abgelaufen

Bei Canvases ohne Enddaten wird der Einjahres-Countdown zum Stoppen des Canvas zurückgesetzt, wenn ein:e Nutzer:in aufgenommen wird oder der Canvas aktualisiert wird. Wenn Canvases gestoppt werden, benachrichtigt Braze die Kund:innen in ihrem Dashboard und per E-Mail.

Die [maximale Dauer]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) eines Canvas ist die längstmögliche Zeit, die ein:e Nutzer:in benötigen kann, um einen bestimmten Canvas abzuschließen. Diese Dauer umfasst Ablauffristen für Content Cards und In-App-Nachrichten.

In dieser Tabelle erfahren Sie, wie Sie einen inaktiven Canvas aktiv halten:

| Grund für den Inaktiv-Status                                                                                                  | Schritte, um den Canvas zu aktivieren                     |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Canvases mit geplanten einmaligen Sendungen, deren maximale Dauer nach dem Sendedatum überschritten ist                 | Planen Sie eine zukünftige Sendung                          |
| Canvases, die geplant oder aktionsbasiert sind, Enddaten haben und deren maximale Dauer nach dem Enddatum überschritten ist | Verlängern Sie das Enddatum                             |
| Canvases ohne Enddaten, die seit einem Jahr keine Nachrichten gesendet haben                                                      | Senden Sie eine Nachricht oder nehmen Sie eine beliebige Änderung am Canvas vor |
| Canvases mit Enddaten und einmaligen Sendungen | Planen Sie eine zukünftige Sendung |
| Canvases, die seit 11 Monaten keine Nachricht gesendet haben | Senden Sie eine Nachricht oder nehmen Sie eine beliebige Änderung am Canvas vor |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn es keine Option zur Wiederherstellung von Interaktionsdaten gibt, kann dies folgende Gründe haben:

- Die Wiederherstellung oder eine andere Operation im Zusammenhang mit Interaktionsdaten ist derzeit in Bearbeitung.
- Für diesen Canvas existierten keine Interaktionsdaten.
- Wenn der Canvas vor 2021 erstellt wurde, wurden die Daten möglicherweise gemäß der vorherigen Richtlinie dauerhaft gelöscht.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Für welche Campaigns oder Canvases gilt dies? {#what-campaigns-or-canvases-does-this-apply-to}

Dies gilt für Campaigns und Canvases, die die zuvor aufgeführten Kriterien bereits erfüllen, sowie für Campaigns und Canvases, die die Kriterien in Zukunft erfüllen werden.

### Wie erkenne ich, ob eine Campaign oder ein Canvas inaktiv ist? {#how-do-i-know-if-a-campaign-or-canvas-is-idle}

Inaktive Campaigns und Canvases werden auf den Listenseiten für Campaigns und Canvases unter der Kategorie **Inaktiv** angezeigt. Das Datum, an dem die Campaign oder der Canvas gestoppt wird, wird als Spalte in der Liste aufgeführt.

![Der Filter „Inaktiv“ auf der Seite „Campaigns“.][1]{: style="max-width:60%;"}

### Was passiert, wenn eine inaktive Campaign oder ein inaktiver Canvas aktualisiert wird? {#what-happens-if-an-idle-campaign-or-canvas-is-updated}

Wenn eine Campaign, die keine Nachricht gesendet hat, oder ein Canvas, der keine Nutzer:innen aufgenommen hat, aktualisiert wird, wird der Countdown zurückgesetzt.

### Was passiert mit Campaigns, die seit einem Jahr keine Nachricht gesendet haben (oder Canvases, die seit einem Jahr keine Nutzer:innen aufgenommen haben), aber ein Enddatum in der Zukunft haben? {#what-happens-to-campaigns-that-havent-sent-a-message-in-one-year-or-canvases-that-havent-entered-users-in-one-year-but-have-an-end-date-in-the-future}

Wir stoppen diese Campaigns und Canvases sieben Tage nach dem Enddatum um 4 Uhr UTC.

#### Kann ich verhindern, dass Campaigns automatisch gestoppt werden? {#can-i-stop-campaigns-from-automatically-stopping}

Nein. Dies hilft dabei, nur die notwendigen Campaigns aktiv zu halten, um Dashboards übersichtlicher zu gestalten und die Performance zu verbessern. Wenn Sie eine Liste aller automatisch gestoppten Campaigns wünschen, [reichen Sie ein Support-Ticket ein]({{site.baseurl}}/help/support/), um eine solche zu erhalten.

### Wer erhält E-Mail-Benachrichtigungen über gestoppte Campaigns und Canvases? {#who-will-receive-email-notifications-about-stopped-campaigns-and-canvases}

Standardmäßig sind alle Nutzer:innen mit Administratorberechtigungen für E-Mail-Benachrichtigungen über automatisch gestoppte Campaigns und Canvases angemeldet. Der/die Ersteller:in der Campaign oder des Canvas wird immer benachrichtigt, wenn diese/r gestoppt wird. Nutzer:innen können ihre Präferenzen für E-Mail-Benachrichtigungen verwalten, indem sie zu **Unternehmenseinstellungen** > **Präferenzen für Benachrichtigungen** navigieren und dann Empfänger:innen zur Benachrichtigung **Campaign Automatically Stopped** und zur Benachrichtigung **Canvas Automatically Stopped** hinzufügen oder entfernen.

### Wie funktioniert das Stoppen von Content Cards? {#how-does-stopping-content-cards-work}

Content Cards in Campaigns werden erst nach Ablauf ihrer Gültigkeitsfrist und der entsprechenden Pufferzeit gestoppt. Sie werden zum späteren der beiden folgenden Zeitpunkte gestoppt: der Pufferzeit (je nachdem, ob die Campaign eine einmalige Sendung ist, ein Enddatum hat oder kein Enddatum hat) und der Gültigkeitsfrist.

Wenn beispielsweise eine Content Card am 1. April abläuft, eine einmalige Sendung ist und eine Conversion-Frist von 10 Tagen hat, wird sie am 12. April gestoppt (10 Tage nach der Conversion-Frist plus ein Tag). Wenn eine Content Card am 1. April abläuft, API-getriggert ist und seit dem 15. März keine Nachrichten gesendet hat, läuft sie am 15. März des nächsten Jahres ab.

Canvases werden erst gestoppt, nachdem die Content Cards gestoppt wurden, d. h. ihre maximale Dauer abgelaufen ist.

### Ich habe ein Feature-Flag-Experiment in meinem Canvas. Bleibt der Canvas aktiv, nachdem mein Feature-Flag gesetzt wurde? {#i-have-a-feature-flag-experiment-in-my-canvas-after-my-feature-flag-is-set-will-the-canvas-remain-active}

Canvases mit Feature-Flag-Schritten werden nicht automatisch gestoppt und werden nicht inaktiv.

### Warum sehe ich inaktive Campaigns in meiner Campaign-Liste, obwohl ich einen Filter angewendet habe, um nur aktive Campaigns anzuzeigen? {#why-am-i-seeing-idle-campaigns-displayed-in-my-campaigns-list-when-i-applied-a-filter-to-show-active-campaigns-only}

Inaktive Campaigns gelten als aktiv, bis sie gestoppt werden.

### Wird eine Campaign als inaktiv aufgeführt, wenn sie noch Push-Benachrichtigungen sendet? {#would-a-campaign-be-listed-as-idle-when-its-still-sending-push-notifications}

Nein. Eine Campaign wird als inaktiv aufgeführt, wenn sie nicht mehr aktiv Nachrichten sendet.

[1]: {% image_buster /assets/unlisted_docs/img/idle_filter.png %}