---
nav_title: FAQ
article_title: FAQ zu Rate-Limiting und Frequency-Capping
page_order: 0
page_type: FAQ
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Rate-Limiting und Frequency-Capping."
tool: Campaigns

---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu Rate-Limiting und Frequency-Capping.

## Wenn ich eine Sendedrosselung in einem aktiven Canvas ändere, wirkt sich das auf Nutzer:innen aus, die sich bereits im Canvas befinden? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Ja. Wenn Sie ein Canvas-Rate-Limit erhöhen oder verringern, gilt das aktualisierte Limit für neue Nachrichten. Es kann eine kurze Verzögerung geben, bevor die Änderung im gesamten Canvas wirksam wird.

### Was passiert, wenn ein:e Nutzer:in einen Canvas-Nachrichtenschritt erreicht, aber das globale Frequency-Capping überschritten hat? {#what-happens-if-a-user-reaches-a-canvas-message-step-but-is-over-the-global-frequency-cap}

Die:der Nutzer:in erhält den Versand für den begrenzten Kanal nicht, folgt aber weiterhin den Fortschrittsregeln Ihres Nachrichtenschritts. Nachrichtenschritte bringen Nutzer:innen voran, wenn eine Nachricht aufgrund des globalen Frequency-Cappings nicht gesendet wird, sodass sie zum nächsten Canvas-Schritt weitergeleitet werden. Die vollständige Liste der Fortschrittsfälle finden Sie unter [Wie Nutzer:innen vorankommen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance).

### Wie kann ich Nutzer:innen identifizieren, die in einem Canvas durch Frequency-Capping begrenzt wurden? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Nutzer:innen, die durch Frequency-Capping begrenzt werden, erzeugen kein Sendeereignis für diesen Schritt. Um diese Nutzer:innen zu identifizieren, können Sie [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) verwenden, um abgebrochene Nachrichtenereignisse zu verfolgen, bei denen `abort_type` den Wert `frequency_capped` hat. Alternativ können Sie eine [Segmenterweiterung]({{site.baseurl}}/user_guide/audience/segments/segment_extension) erstellen, um Nutzer:innen zu analysieren, die den Canvas betreten haben, aber die erwartete Nachricht nicht erhalten haben.

### Wie werden Kalendertage und Zeitzonen für globale Frequency-Caps „pro Tag“ verwendet? {#how-are-calendar-days-and-time-zones-used-for-per-day-global-frequency-caps}

Das globale Frequency-Capping verwendet die Zeitzone der:des Nutzer:in und zählt nach Kalendertagen, nicht nach rollierenden 24-Stunden-Zeiträumen. Ein Beispiel finden Sie unter [Zustellungsregeln]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-rules).

### Gilt das globale Frequency-Capping für getriggerte In-App-Nachrichten? {#does-global-frequency-capping-apply-to-triggered-in-app-messages}

Nein, das globale Frequency-Capping gilt nur für Push-, E-Mail-, Kurzmitteilungsdienst or SMS-, Webhook-, WhatsApp- und LINE-Nachrichten.

### Begrenzt Frequency-Capping die empfangenen Kampagnen oder einzelne Nachrichten innerhalb eines Versands? {#does-frequency-capping-limit-campaigns-received-or-individual-messages-inside-a-send}

Frequency-Capping wird pro Versand angewendet – jeder Campaign- oder Canvas-Schritt-Versand zählt für Ihre Limits, nicht jede Variante oder Plattform innerhalb eines Versands. Weitere Informationen finden Sie unter [Zustellungsregeln]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-rules).

### Wenn mehrere Nachrichten gleichzeitig infrage kommen und nur einige unter das Limit passen, welche Nachrichten werden gesendet? {#if-several-messages-are-eligible-at-the-same-time-and-only-some-fit-under-the-cap-which-messages-send}

Braze sendet bis zum Limit. Wenn mehrere Versendungen im selben Zeitfenster konkurrieren, werden die Nachrichten, die zuerst verarbeitet werden, auf das Limit angerechnet. Verbleibende Versendungen in diesem Zeitfenster werden durch das Capping begrenzt.

### Zählen fehlgeschlagene Webhooks für das globale Frequency-Capping? {#do-failed-webhooks-count-toward-the-global-frequency-cap}

Nein. Ein Webhook zählt für das Limit, wenn Braze eine erfolgreiche Zustellung verzeichnet. Nicht erfolgreiche Webhook-Antworten (z. B. `4xx`- oder `5xx`-Statuscodes) zählen nicht für das Limit.