---
nav_title: Inaktive Campaigns und Canvase
article_title: Inaktive Campaigns und Canvase
page_order: 1
page_type: reference
alias: /idle_campaigns/
description: "Dieser Referenzartikel behandelt den Inaktiv-Status für Campaigns und Canvase, einschließlich der Kriterien für das automatische Stoppen und häufig gestellter Fragen."
toc_headers: h2
---

# Inaktive Campaigns und Canvase {#idle-campaigns-and-canvases}

> Campaigns und Canvase werden inaktiv, wenn sie für einen bestimmten Zeitraum keine Nachrichten mehr senden oder keine Nutzer:innen mehr aufnehmen.

Braze stoppt inaktive Campaigns und Canvase automatisch zu den zugehörigen Stoppzeitpunkten. Sie bleiben aktiv, bis Braze sie stoppt. Einmalige Sendungen und Nachrichten mit Enddatum werden inaktiv, wenn dieses Datum verstrichen ist, und werden nach sieben Tagen automatisch gestoppt. Nachrichten ohne Enddatum werden nach 11 Monaten ohne Aktivität inaktiv und werden nach einem Jahr automatisch gestoppt.

## Inaktive Campaigns {#idle-campaigns}

Braze stoppt inaktive Campaigns, die eines der folgenden Kriterien erfüllen:

- Eine geplante einmalige Sendung liegt sieben Tage hinter dem Sendedatum
- Eine geplante oder aktionsbasierte Campaign mit Enddatum liegt sieben Tage hinter dem Enddatum
- Eine Campaign ohne Enddatum hat seit einem Jahr keine Nachricht gesendet, keine:n Nutzer:in in eine Kontrollgruppe aufgenommen und wurde nicht bearbeitet

Bei Campaigns ohne Enddatum setzt eine Sendung, eine Kontrollgruppen-Aufnahme oder eine Bearbeitung den Countdown von einem Jahr zurück. Wenn Braze Campaigns stoppt, benachrichtigt es die Unternehmensnutzer:innen im Dashboard und per E-Mail.

Braze stoppt Campaigns zum späteren der beiden Zeitpunkte: dem Standard-Stoppzeitpunkt oder einem Tag nach der letzten Konversions-Frist. Sendungen einer Gewinnervariante oder personalisierten Variante werden als geplante Sendungen behandelt, und Braze stoppt sie sieben Tage nach dem Versand dieser Variante. Campaigns werden täglich um 4 Uhr UTC gestoppt.

Content Cards werden erst nach Ablauf ihrer Gültigkeitsfrist gestoppt und unterliegen ebenfalls den Stoppkriterien für inaktive Campaigns sowie der Konversions-Frist-Regel. Einzelheiten finden Sie unter [Wie funktioniert das Stoppen von Content Cards?](#how-does-stopping-content-cards-work).

Verwenden Sie diese Tabelle, um eine inaktive Campaign aktiv zu halten. Inaktiv-Status und automatisches Stoppen verwenden unterschiedliche Zeitfenster: Eine Campaign ohne Enddatum wird nach 11 Monaten ohne Aktivität inaktiv, und Braze stoppt sie nach einem Jahr automatisch.

| Grund für den Inaktiv-Status | Schritte, um die Campaign wieder zu aktivieren |
|---|---|
| Eine geplante einmalige Sendung liegt hinter dem Sendedatum | Planen Sie eine zukünftige Sendung |
| Eine geplante oder aktionsbasierte Campaign hat ein Enddatum, das verstrichen ist | Verlängern Sie das Enddatum |
| Eine Campaign ohne Enddatum hat seit 11 Monaten keine Nachricht gesendet, keine:n Nutzer:in in eine Kontrollgruppe aufgenommen und wurde nicht bearbeitet | Senden Sie eine Nachricht oder bearbeiten Sie die Campaign |
{: .reset-td-br-1 .reset-td-br-2 aria-label="So halten Sie eine inaktive Campaign aktiv" }

Feature-Flag-Campaigns und Feature-Flag-Experimente werden nicht inaktiv und werden nicht automatisch gestoppt.

### In-App-Nachricht-Campaigns {#in-app-message-campaigns}

Aktionsbasierte In-App-Nachricht-Campaigns werden nach 30 Tagen ohne Sendung, Kontrollgruppen-Aufnahme oder Bearbeitung inaktiv. Eine inaktive In-App-Nachricht-Campaign wird weiterhin gemäß ihrer Konfiguration zugestellt. Je nach Ihrem Workspace kann Braze sie als [vorlagenbasierte In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages) zustellen.

Eine Sendung, Kontrollgruppen-Aufnahme oder Bearbeitung versetzt die Campaign wieder in den aktiven Status und setzt das 30-Tage-Fenster zurück. Das automatische Stoppen folgt weiterhin den Sieben-Tage- und Ein-Jahres-Regeln unter [Inaktive Campaigns](#idle-campaigns), nicht dem 30-Tage-Inaktivitätsfenster.

## Inaktive Canvase {#idle-canvases}

Braze stoppt inaktive Canvase, die eines der folgenden Kriterien erfüllen:

- Eine geplante einmalige Sendung liegt mehr als sieben Tage hinter ihrem Sendedatum und ihrer [maximalen Dauer]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#maximum-duration)
- Ein geplanter oder aktionsbasierter Canvas mit Enddatum liegt mehr als sieben Tage hinter seinem Enddatum und seiner maximalen Dauer
- Ein Canvas ohne Enddatum hat seit mehr als 12 Monaten zuzüglich seiner maximalen Dauer keine Nutzer:innen aufgenommen und wurde nicht bearbeitet

Bei Canvase ohne Enddatum setzt eine Nutzeraufnahme oder Bearbeitung den Countdown von einem Jahr zurück. Wenn Braze Canvase stoppt, benachrichtigt es die Unternehmensnutzer:innen im Dashboard und per E-Mail.

Die maximale Dauer eines Canvas ist die längste mögliche Zeit, die Nutzer:innen benötigen können, um diesen Canvas abzuschließen. Diese Dauer umfasst die Gültigkeitsfristen für Content Cards und In-App-Nachrichten.

Verwenden Sie diese Tabelle, um einen inaktiven Canvas aktiv zu halten. Inaktiv-Status und automatisches Stoppen verwenden unterschiedliche Zeitfenster: Ein Canvas ohne Enddatum wird nach 11 Monaten zuzüglich seiner maximalen Dauer ohne Aktivität inaktiv, und Braze stoppt ihn nach 12 Monaten zuzüglich seiner maximalen Dauer automatisch.

| Grund für den Inaktiv-Status | Schritte, um den Canvas wieder zu aktivieren |
|---|---|
| Eine geplante einmalige Sendung liegt hinter dem Sendedatum und der maximalen Dauer | Planen Sie eine zukünftige Sendung |
| Ein geplanter oder aktionsbasierter Canvas hat ein Enddatum und eine maximale Dauer, die verstrichen sind | Verlängern Sie das Enddatum |
| Ein Canvas ohne Enddatum hat seit 11 Monaten zuzüglich seiner maximalen Dauer keine Nutzer:innen aufgenommen und wurde nicht bearbeitet | Nehmen Sie eine:n Nutzer:in auf oder bearbeiten Sie den Canvas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="So halten Sie einen inaktiven Canvas aktiv" }

Canvase mit Feature-Flag-Schritten werden nicht inaktiv und werden nicht automatisch gestoppt.

Informationen zu Messaging-Interaktionsdaten bei gestoppten Campaigns und Canvase finden Sie unter [Informationen zur Verfügbarkeit von Messaging-Interaktionsdaten]({{site.baseurl}}/messaging_interaction_data).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Für welche Campaigns oder Canvase gilt das? {#what-campaigns-or-canvases-does-this-apply-to}

Dies gilt für Campaigns und Canvase, die die in diesem Artikel genannten Kriterien bereits erfüllen, und für solche, die sie später erfüllen.

### Wie erkenne ich, ob eine Campaign oder ein Canvas inaktiv ist? {#how-do-i-know-if-a-campaign-or-canvas-is-idle}

Um inaktive Campaigns und Canvase zu finden, gehen Sie zur Seite **Campaigns** oder **Canvas** und filtern Sie nach **Idle**. Das Datum, an dem Braze die Campaign oder den Canvas stoppt, wird als Spalte in der Liste angezeigt.

![Der Filter „Idle“ auf der Campaigns-Seite.]({% image_buster /assets/img/idle_filter.png %}){: style="max-width:80%;"}

### Was passiert, wenn eine inaktive Campaign oder ein inaktiver Canvas aktualisiert wird? {#what-happens-if-an-idle-campaign-or-canvas-is-updated}

Wenn Sie eine Campaign Update or aktualisieren or aktualisieren, die keine Nachricht gesendet hat, oder einen Canvas, der keine Nutzer:innen aufgenommen hat, wird der Countdown zurückgesetzt.

### Was passiert mit Campaigns, die seit einem Jahr keine Nachricht gesendet haben (oder Canvase, die seit einem Jahr keine Nutzer:innen aufgenommen haben), aber ein Enddatum in der Zukunft haben? {#what-happens-to-campaigns-that-havent-sent-a-message-in-one-year-or-canvases-that-havent-entered-users-in-one-year-but-have-an-end-date-in-the-future}

Braze stoppt diese Campaigns und Canvase sieben Tage nach dem Enddatum um 4 Uhr UTC.

### Kann ich verhindern, dass Campaigns automatisch gestoppt werden? {#can-i-prevent-campaigns-from-auto-stopping}

Nein. Das automatische Stoppen sorgt dafür, dass nur die notwendigen Campaigns aktiv bleiben, was das Dashboard übersichtlicher macht und die Performance verbessert. Wenn Sie eine Liste aller automatisch gestoppten Campaigns benötigen, [reichen Sie ein Support-Ticket ein]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Wer erhält E-Mail-Benachrichtigungen über gestoppte Campaigns und Canvase? {#who-receives-email-notifications-about-stopped-campaigns-and-canvases}

Standardmäßig sind alle Nutzer:innen mit Administratorberechtigungen für E-Mail-Benachrichtigungen über automatisch gestoppte Campaigns und Canvase angemeldet. Die Erstellerin oder der Ersteller der Campaign oder des Canvas wird immer benachrichtigt, wenn diese:r gestoppt wird. Um die Empfänger:innen zu verwalten, gehen Sie zu **Einstellungen** > **Administratoreinstellungen** > **Benachrichtigungseinstellungen** und fügen Sie Empfänger:innen zu **Campaign Automatically Stopped** und **Canvas Automatically Stopped** hinzu oder entfernen Sie sie.

### Wie funktioniert das Stoppen von Content Cards? {#how-does-stopping-content-cards-work}

Content Cards in Campaigns werden erst nach Ablauf ihrer Gültigkeitsfrist und der entsprechenden Pufferfrist gestoppt. Braze stoppt sie zum späteren der beiden Zeitpunkte: der Pufferfrist (einmalige Sendung, Enddatum oder ohne Enddatum) und der Gültigkeitsfrist.

Beispiel: Wenn eine Content Card am 1. April abläuft, eine einmalige Sendung ist und eine Konversions-Frist von 10 Tagen hat, stoppt Braze sie am 12. April (10 Tage nach der Konversions-Frist, plus ein Tag). Wenn eine Content Card am 1. April abläuft, API-getriggert ist und seit dem 15. März keine Nachrichten gesendet hat, läuft sie am 15. März des folgenden Jahres ab.

Canvase werden erst gestoppt, nachdem ihre Content Cards gestoppt wurden, das heißt, nachdem ihre maximale Dauer verstrichen ist.

### Ich habe ein Feature-Flag-Experiment in meinem Canvas. Bleibt der Canvas aktiv, nachdem mein Feature-Flag gesetzt wurde? {#i-have-a-feature-flag-experiment-in-my-canvas-after-my-feature-flag-is-set-does-the-canvas-remain-active}

Ja. Canvase mit Feature-Flag-Schritten werden nicht automatisch gestoppt und werden nicht inaktiv. Feature-Flag-Campaigns und Feature-Flag-Experimente unterliegen derselben Ausnahme.

### Warum erscheinen inaktive Campaigns, wenn ich die Campaign-Liste nur nach aktiven filtere? {#why-do-idle-campaigns-appear-when-i-filter-the-campaign-list-to-active-only}

Inaktive Campaigns gelten als aktiv, bis sie gestoppt werden.

### Ist eine Campaign inaktiv, wenn sie noch Push-Benachrichtigungen sendet? {#is-a-campaign-idle-if-its-still-sending-push-notifications}

Nein. Eine Campaign wird als inaktiv aufgeführt, wenn sie nicht mehr aktiv Nachrichten sendet.