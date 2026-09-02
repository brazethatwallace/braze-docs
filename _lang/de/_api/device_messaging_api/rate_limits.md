---
nav_title: Rate-Limits
article_title: Rate-Limits der Device Messaging API
page_order: 3
page_type: reference
description: "Erfahren Sie, wie Rate-Limits und Antwort-Header der Device Messaging API funktionieren."
hidden: true
---

# Rate-Limits der Device Messaging API {#device-messaging-api-rate-limits}

Braze wendet Rate-Limits der Device Messaging API pro Workspace an. Wenn ein Workspace ein Limit überschreitet, gibt Braze den Statuscode `429 Too Many Requests` zurück.

Die Rate-Limits der Device Messaging API sind von den standardmäßigen Limits getrennt, die für andere Braze-Representational State Transfer-API-Endpunkte dokumentiert sind. Gehen Sie nicht davon aus, dass ein Limit, ein Zeitfenster, eine Payload-Größe oder ein Reset-Zeitplan, der für einen anderen Endpunkt dokumentiert ist, auch für die Device Messaging API gilt.

{% alert important %}
Diese Seite befindet sich in der Beta-Phase. Features und Dokumentation für die Device Messaging API können sich ändern. Wenden Sie sich an Ihren Braze Account Manager:in, um Zugang anzufordern.
{% endalert %}

## Rate-Limit-Header {#rate-limit-headers}

Wenn Rate-Limit-Informationen verfügbar sind, enthält eine Antwort die folgenden Header:

| Header | Beschreibung |
|---|---|
| `X-RateLimit-Limit` | Die maximale Anzahl zulässiger Anfragen im aktuellen Intervall. |
| `X-RateLimit-Remaining` | Die Anzahl der verbleibenden Anfragen im aktuellen Rate-Limit-Fenster. |
| `X-RateLimit-Reset` | Die UTC-Epochenzeit, zu der das aktuelle Rate-Limit-Fenster zurückgesetzt wird. |
| `X-RateLimit-Retry-After` | Die Anzahl der Sekunden, die vor einem erneuten Versuch einer ratenbegrenzten Anfrage gewartet werden soll. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rate-Limit-Header der Device Messaging API" }

Verwenden Sie diese Header, um Anfragen zu reduzieren oder zu pausieren, bevor ein Limit erreicht wird. Header sind möglicherweise nicht in jeder Antwort enthalten.

## Umgang mit Rate-Limits {#handling-rate-limits}

Wenn Sie eine `429`-Antwort erhalten:

1. Stoppen oder reduzieren Sie Anfragen für den betroffenen Workspace.
2. Verwenden Sie `X-RateLimit-Retry-After`, sofern vorhanden, um die Wartezeit zu bestimmen. Andernfalls verwenden Sie `X-RateLimit-Reset`, sofern verfügbar, um den Zeitpunkt für die Wiederaufnahme zu ermitteln.
3. Wiederholen Sie die Anfrage mit exponentiellem Backoff und einer maximalen Anzahl von Versuchen.