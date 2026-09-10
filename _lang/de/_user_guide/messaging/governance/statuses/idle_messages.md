---
nav_title: Inaktive Campaigns und Canvases
article_title: Inaktive Campaigns und Canvases
page_order: 1
page_type: reference
alias: /idle_campaigns/
description: "Dieser Referenzartikel behandelt den Inaktiv-Status für Campaigns und Canvases, einschließlich der Kriterien für das automatische Stoppen und häufig gestellter Fragen."
toc_headers: h2
---

# Inaktive Campaigns und Canvases {#idle-campaigns-and-canvases}

> Campaigns und Canvases werden inaktiv, wenn sie für einen bestimmten Zeitraum keine Nachrichten mehr senden oder keine Nutzer:innen mehr aufnehmen.

Braze stoppt inaktive Campaigns und Canvases automatisch zu den zugehörigen Stoppzeitpunkten. Sie bleiben aktiv, bis Braze sie stoppt. Einmalige Sendungen und Nachrichten mit Enddatum werden inaktiv, wenn dieses Datum verstrichen ist, und werden nach sieben Tagen automatisch gestoppt. Nachrichten ohne Enddatum werden nach 11 Monaten ohne Aktivität inaktiv und werden nach einem Jahr automatisch gestoppt.

## Inaktive Campaigns {#idle-campaigns}

Braze stoppt inaktive Campaigns, die eines der folgenden Kriterien erfüllen:

- Ein geplanter einmaliger Versand liegt mehr als sieben Tage nach dem Sendedatum
- Eine geplante oder aktionsbasierte Campaign mit einem Enddatum liegt mehr als sieben Tage nach dem Enddatum
- Eine Campaign ohne Enddatum hat seit einem Jahr keine Nachricht gesendet, keine Nutzer:innen in eine Kontrollgruppe aufgenommen und wurde nicht bearbeitet

Bei Campaigns ohne Enddatum setzt ein Versand, eine Kontrollgruppenaufnahme oder eine Bearbeitung den Einjahres-Countdown zurück. Wenn Braze Campaigns stoppt, werden Unternehmensnutzer:innen im Dashboard und per E-Mail benachrichtigt.

Braze stoppt Campaigns zum späteren Zeitpunkt aus dem Standard-Stoppdatum und einem Tag nach der letzten Konversionsfrist. Versendungen einer Gewinnervariante oder personalisierten Variante werden als geplante Versendungen behandelt, und Braze stoppt sie sieben Tage nach dem Versand dieser Variante. Campaigns werden täglich um 4 Uhr UTC gestoppt.

Content Cards werden erst nach Ablauf ihres Ablaufdatums gestoppt und unterliegen ebenfalls den Stoppkriterien für inaktive Campaigns sowie der Konversionsfrist-Regel. Weitere Informationen finden Sie unter [Wie funktioniert das Stoppen von Content Cards?](#how-does-stopping-content-cards-work).

Verwenden Sie diese Tabelle, um eine inaktive Campaign aktiv zu halten. Inaktivstatus und automatisches Stoppen verwenden unterschiedliche Zeitfenster: Eine Campaign ohne Enddatum wird nach 11 Monaten ohne Aktivität inaktiv, und Braze stoppt sie automatisch nach einem Jahr.

| Grund für den Inaktivstatus | Schritte, um die Campaign wieder aktiv zu machen |
|---|---|
| Geplanter einmaliger Versand liegt nach dem Sendedatum | Planen Sie einen zukünftigen Versand |
| Geplante oder aktionsbasierte Campaign hat ein abgelaufenes Enddatum | Verlängern Sie das Enddatum |
| Campaign ohne Enddatum hat seit 11 Monaten keine Nachricht gesendet, keine Nutzer:innen in eine Kontrollgruppe aufgenommen und wurde nicht bearbeitet | Senden Sie eine Nachricht oder bearbeiten Sie die Campaign |
{: .reset-td-br-1 .reset-td-br-2 aria-label="So halten Sie eine inaktive Campaign aktiv" }

Feature-Flag-Campaigns und Feature-Flag-Experimente werden nicht inaktiv und nicht automatisch gestoppt.

### In-App-Nachricht-Campaigns {#in-app-message-campaigns}

Aktionsbasierte In-App-Nachricht-Campaigns werden nach 30 Tagen ohne Versand, Kontrollgruppenaufnahme oder Bearbeitung inaktiv. Eine inaktive In-App-Nachricht-Campaign wird weiterhin gemäß ihrer Konfiguration ausgeliefert. Je nach Workspace kann Braze sie als [vorlagisierte In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages) ausliefern.

Ein Versand, eine Kontrollgruppenaufnahme oder eine Bearbeitung setzt die Campaign wieder auf den aktiven Status zurück und startet das 30-Tage-Fenster neu. Das automatische Stoppen folgt weiterhin den Sieben-Tage- und Einjahres-Regeln unter [Inaktive Campaigns](#idle-campaigns) und nicht dem 30-Tage-Inaktivfenster.

## Inaktive Canvases {#idle-canvases}

Braze stoppt inaktive Canvases, die eines dieser Kriterien erfüllen:

- Ein geplanter Einmalversand liegt mehr als sieben Tage nach seinem Sendedatum und seiner [maximalen Dauer]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#maximum-duration)
- Ein geplantes oder aktionsbasiertes Canvas mit einem Enddatum liegt mehr als sieben Tage nach seinem Enddatum und seiner maximalen Dauer
- Ein Canvas ohne Enddatum hat seit mehr als 12 Monaten plus seiner maximalen Dauer keine Nutzer:innen aufgenommen und wurde nicht bearbeitet

Bei Canvases ohne Enddatum setzt ein Nutzereintritt oder eine Bearbeitung den Einjahres-Countdown zurück. Wenn Braze Canvases stoppt, werden Unternehmensnutzer:innen im Dashboard und per E-Mail benachrichtigt.

Die maximale Dauer eines Canvas ist die längstmögliche Zeit, die Nutzer:innen benötigen können, um dieses Canvas abzuschließen. Diese Dauer umfasst Ablaufzeiten für Content Cards und In-App-Nachrichten. Wenn Ihr Canvas Schritte mit Rate-Limits enthält, fügt Braze der maximalen Dauer zusätzlich sieben Tage hinzu, um mögliche Rate-Limit-Warteschlangen zu berücksichtigen.

Verwenden Sie diese Tabelle, um ein inaktives Canvas aktiv zu halten. Inaktivitätsstatus und automatisches Stoppen verwenden unterschiedliche Zeitfenster: Ein Canvas ohne Enddatum wird nach 11 Monaten plus seiner maximalen Dauer ohne Aktivität inaktiv, und Braze stoppt es automatisch nach 12 Monaten plus seiner maximalen Dauer.

| Grund für den Inaktivitätsstatus | Schritte, um das Canvas wieder zu aktivieren |
|---|---|
| Der geplante Einmalversand liegt nach dem Sendedatum und der maximalen Dauer | Planen Sie einen zukünftigen Versand |
| Ein geplantes oder aktionsbasiertes Canvas hat ein Enddatum und eine maximale Dauer, die überschritten wurden | Verlängern Sie das Enddatum |
| Ein Canvas ohne Enddatum hat seit 11 Monaten plus seiner maximalen Dauer keine Nutzer:innen aufgenommen und wurde nicht bearbeitet | Nehmen Sie Nutzer:innen auf oder bearbeiten Sie das Canvas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="So halten Sie ein inaktives Canvas aktiv" }

Canvases mit Feature-Flag-Schritten werden nicht inaktiv und nicht automatisch gestoppt.

Informationen zu Messaging-Interaktionsdaten bei gestoppten Campaigns und Canvases finden Sie unter [Über die Verfügbarkeit von Messaging-Interaktionsdaten]({{site.baseurl}}/messaging_interaction_data).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Für welche Campaigns oder Canvases gilt das? {#what-campaigns-or-canvases-does-this-apply-to}

Dies gilt für Campaigns und Canvases, die bereits die in diesem Artikel genannten Kriterien erfüllen, sowie für solche, die die Kriterien zu einem späteren Zeitpunkt erfüllen.

### Wie erkenne ich, ob eine Campaign oder ein Canvas inaktiv ist? {#how-do-i-know-if-a-campaign-or-canvas-is-idle}

Um inaktive Campaigns und Canvases zu finden, gehen Sie zur Seite **Campaigns** oder **Canvas** und filtern Sie nach **Idle**. Das Datum, an dem Braze die Campaign oder das Canvas stoppt, wird als Spalte in der Liste angezeigt.

![Der Filter „Idle“ auf der Campaigns-Seite.]({% image_buster /assets/img/idle_filter.png %}){: style="max-width:80%;"}

### Was passiert, wenn eine inaktive Campaign oder ein inaktives Canvas aktualisiert wird? {#what-happens-if-an-idle-campaign-or-canvas-is-updated}

Wenn Sie eine Campaign aktualisieren, die keine Nachricht gesendet hat, oder ein Canvas, in das keine Nutzer:innen eingetreten sind, wird der Countdown zurückgesetzt.

### Was passiert mit Campaigns, die seit einem Jahr keine Nachricht gesendet haben (oder Canvases, in die seit einem Jahr keine Nutzer:innen eingetreten sind), aber ein Enddatum in der Zukunft haben? {#what-happens-to-campaigns-that-havent-sent-a-message-in-one-year-or-canvases-that-havent-entered-users-in-one-year-but-have-an-end-date-in-the-future}

Braze stoppt diese Campaigns und Canvases sieben Tage nach dem Enddatum um 4 Uhr UTC.

### Kann ich verhindern, dass Campaigns automatisch gestoppt werden? {#can-i-prevent-campaigns-from-auto-stopping}

Nein. Das automatische Stoppen sorgt dafür, dass nur die notwendigen Campaigns aktiv bleiben, was das Dashboard übersichtlicher macht und die Performance verbessert. Wenn Sie eine Liste aller automatisch gestoppten Campaigns benötigen, [reichen Sie ein Support-Ticket ein]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Wer erhält E-Mail-Benachrichtigungen über gestoppte Campaigns und Canvases? {#who-receives-email-notifications-about-stopped-campaigns-and-canvases}

Standardmäßig erhalten alle Nutzer:innen mit Administratorberechtigungen E-Mail-Benachrichtigungen über automatisch gestoppte Campaigns und Canvases. Die Person, die die Campaign oder das Canvas erstellt hat, wird immer benachrichtigt, wenn diese gestoppt werden. Um Empfänger:innen zu verwalten, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Benachrichtigungseinstellungen** und fügen Sie Empfänger:innen unter **Campaign Automatically Stopped** und **Canvas Automatically Stopped** hinzu oder entfernen Sie sie.

### Wie funktioniert das Stoppen von Content Cards? {#how-does-stopping-content-cards-work}

Content Cards in Campaigns werden erst nach Ablauf ihres Verfallsdatums und der entsprechenden Pufferzeit gestoppt. Braze stoppt sie zum späteren Zeitpunkt aus Pufferzeit (einmaliger Versand, Enddatum oder kein Enddatum) und Verfallsdatum.

Wenn eine Content Card beispielsweise am 1. April abläuft, einmalig versendet wird und eine Konversions-Frist von 10 Tagen hat, stoppt Braze sie am 12. April (10 Tage nach der Konversions-Frist plus ein Tag). Wenn eine Content Card am 1. April abläuft, API-getriggert ist und seit dem 15. März keine Nachrichten mehr gesendet hat, läuft sie am 15. März des folgenden Jahres ab.

Canvases werden erst gestoppt, nachdem ihre Content Cards gestoppt wurden, d. h. nachdem ihre maximale Dauer abgelaufen ist.

### Ich habe ein Feature-Flag-Experiment in meinem Canvas. Bleibt das Canvas aktiv, nachdem mein Feature-Flag gesetzt wurde? {#i-have-a-feature-flag-experiment-in-my-canvas-after-my-feature-flag-is-set-does-the-canvas-remain-active}

Ja. Canvases mit Feature-Flag-Schritten werden nicht automatisch gestoppt und werden nicht als inaktiv eingestuft. Feature-Flag-Campaigns und Feature-Flag-Experimente folgen derselben Ausnahme.

### Warum erscheinen inaktive Campaigns, wenn ich die Campaign-Liste nur nach aktiven filtere? {#why-do-idle-campaigns-appear-when-i-filter-the-campaign-list-to-active-only}

Inaktive Campaigns gelten als aktiv, bis sie gestoppt werden.

### Ist eine Campaign inaktiv, wenn sie noch Push-Benachrichtigungen sendet? {#is-a-campaign-idle-if-its-still-sending-push-notifications}

Nein. Eine Campaign wird als inaktiv aufgeführt, wenn sie nicht mehr aktiv Nachrichten sendet.