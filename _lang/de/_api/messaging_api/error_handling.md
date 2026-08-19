---
nav_title: Fehlerbehandlung und Wiederholungsversuche
article_title: Fehlerbehandlung und Wiederholungsversuche der Messaging API
page_order: 2
page_type: reference
description: "Erfahren Sie, wie Sie mit Messaging-API-Antworten, Fehlern und Wiederholungsversuchen umgehen."
hidden: true
---

# Fehlerbehandlung und Wiederholungsversuche der Messaging API {#messaging-api-error-handling-and-retries}

{% alert important %}
Diese Seite befindet sich in der Betaphase. Features und Dokumentation für die Messaging API können sich ändern.
{% endalert %}

Die Antwortkörper und Erfolgssemantiken der Messaging API variieren je nach Endpunkt. Verwenden Sie das Antwortschema und die Statuscode-Tabelle des jeweiligen Endpunkts als verbindliche Referenz.

## Erfolgsantworten {#success-responses}

Die Banner-Endpunkte verwenden unterschiedliche Erfolgsantworten:

- `POST /v1/device-messaging/banners/sync` gibt einen `200`-Statuscode mit einem `banners`-Objekt zurück.
- `POST /v1/device-messaging/banners/track` gibt einen `202`-Statuscode mit `events_processed` und `message` zurück. Wenn Braze einzelne Ereignisse überspringt, enthält die Antwort zusätzlich ein `errors`-Array.

Eine `202`-Antwort vom Tracking-Endpunkt bedeutet, dass Braze mindestens ein gültiges Ereignis akzeptiert hat. Überprüfen Sie das `errors`-Array, um übersprungene Ereignisse zu identifizieren.

## Fehlerantworten {#error-responses}

Auch die Felder der Fehlerantworten variieren:

- Fehler beim Banner-Abruf verwenden ein `error`-Feld.
- Fehler beim Banner-Tracking verwenden ein `message`-Feld und können ein indiziertes `errors`-Array enthalten.

Parsen Sie nicht den Text der Fehlermeldung, um das Anwendungsverhalten zu bestimmen. Verwenden Sie stattdessen den HTTP-Statuscode und die endpunktspezifischen Felder.

## Hinweise zu Wiederholungsversuchen {#retry-guidance}

Verwenden Sie die folgenden Hinweise, um zu entscheiden, ob ein Wiederholungsversuch sinnvoll ist:

| Statuscode | Hinweise zu Wiederholungsversuchen |
|---|---|
| `400` | Korrigieren Sie die Anfrage, bevor Sie es erneut versuchen. Korrigieren Sie beim Banner-Tracking übersprungene Ereignisse, bevor Sie diese erneut senden. |
| `401` oder `403` | Überprüfen Sie den clientseitigen REST-API-Schlüssel und seine Berechtigungen, bevor Sie es erneut versuchen. |
| `404` | Stellen Sie sicher, dass die Messaging API für den Workspace aktiviert ist und die Endpunkt-URL korrekt ist. |
| `429` | Reduzieren Sie die Anfragerate und versuchen Sie es mit exponentiellem Backoff erneut. Verwenden Sie die Rate-Limit-Antwort-Header, sofern verfügbar. |
| `5XX` | Versuchen Sie es mit exponentiellem Backoff und einer maximalen Anzahl von Versuchen erneut. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Hinweise zu Wiederholungsversuchen der Messaging API" }

Die genauen Antwortkörper und unterstützten Statuscodes finden Sie beim jeweiligen Endpunkt:

- [Banner für Nutzer:innen abrufen]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_sync_banners)
- [Banner-Analytics-Ereignisse tracken]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_track_banner_events)