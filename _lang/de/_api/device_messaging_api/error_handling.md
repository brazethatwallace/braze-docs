---
nav_title: Fehlerbehandlung und Wiederholungsversuche
article_title: Fehlerbehandlung und Wiederholungsversuche der Device Messaging API
page_order: 2
page_type: reference
description: "Erfahren Sie, wie Sie mit Antworten, Fehlern und Wiederholungsversuchen der Device Messaging API umgehen."
hidden: true
---

# Fehlerbehandlung und Wiederholungsversuche der Device Messaging API {#device-messaging-api-error-handling-and-retries}

Die Antwortkörper und Erfolgssemantiken der Device Messaging API variieren je nach Endpunkt. Verwenden Sie das Antwortschema und die Statuscode-Tabelle des jeweiligen Endpunkts als verbindliche Referenz.

{% alert important %}
Diese Seite befindet sich in der Beta-Phase. Features und Dokumentation für die Device Messaging API können sich ändern. Wenden Sie sich an Ihren Braze Account Manager:in, um Zugang anzufordern.
{% endalert %}

## Erfolgreiche Antworten {#success-responses}

Die Banner-Endpunkte verwenden unterschiedliche Erfolgsantworten:

- `POST /v1/device-messaging/banners/sync` gibt einen `200`-Statuscode mit einem `banners`-Objekt zurück.
- `POST /v1/device-messaging/banners/track` gibt einen `202`-Statuscode mit `events_processed` und `message` zurück. Wenn Braze einzelne Events überspringt, enthält die Antwort zusätzlich ein `errors`-Array.

Eine `202`-Antwort vom Tracking-Endpunkt bedeutet, dass Braze mindestens ein gültiges Event akzeptiert hat. Überprüfen Sie das `errors`-Array, um übersprungene Events zu identifizieren.

## Fehlerantworten {#error-responses}

Die Felder für Fehlerantworten variieren ebenfalls:

- Fehler beim Abrufen von Bannern verwenden ein `error`-Feld.
- Fehler beim Banner-Tracking verwenden ein `message`-Feld und können ein indexiertes `errors`-Array enthalten.

Parsen Sie den Text von Fehlermeldungen nicht, um das Anwendungsverhalten zu bestimmen. Verwenden Sie stattdessen den HTTP-Statuscode und endpunktspezifische Felder.

## Anleitungen für Wiederholungsversuche {#retry-guidance}

Verwenden Sie die folgenden Hinweise, um zu entscheiden, ob ein Wiederholungsversuch sinnvoll ist:

| Statuscode | Anleitung für Wiederholungsversuche |
|---|---|
| `400` | Korrigieren Sie die Anfrage, bevor Sie es erneut versuchen. Korrigieren Sie beim Banner-Tracking übersprungene Events, bevor Sie diese erneut senden. |
| `401` oder `403` | Überprüfen Sie den clientseitigen Representational State Transfer-API-Schlüssel und seine Berechtigungen, bevor Sie es erneut versuchen. |
| `404` | Stellen Sie sicher, dass die Device Messaging API für den Workspace aktiviert ist und die Endpunkt-URL korrekt ist. |
| `429` | Reduzieren Sie die Anfragerate und versuchen Sie es mit exponentiellem Backoff erneut. Verwenden Sie die Rate-Limit-Antwort-Header, wenn verfügbar. |
| `5XX` | Versuchen Sie es mit exponentiellem Backoff und einer maximalen Anzahl von Versuchen erneut. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anleitungen für Wiederholungsversuche der Device Messaging API" }

Die genauen Antwortkörper und unterstützten Statuscodes finden Sie beim jeweiligen Endpunkt:

- [Banner für Nutzer:innen abrufen]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners)
- [Banner-Analytics-Ereignisse tracken]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_track_banner_events)