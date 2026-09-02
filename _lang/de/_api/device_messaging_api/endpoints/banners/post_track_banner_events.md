---
nav_title: "POST: Banner-Analytics-Ereignisse tracken"
article_title: "POST: Banner-Analytics-Ereignisse tracken"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Verwenden Sie diesen Endpunkt, um Impression-, Klick- und Dismissal-Ereignisse für Banner aufzuzeichnen."
hidden: true
---

{% api %}
# Banner-Analytics-Ereignisse tracken {#track-banner-analytics-events}
{% apimethod post %}
/v1/device-messaging/banners/track
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Impression-, Klick- und Dismissal-Ereignisse für Banner aufzuzeichnen.

Braze validiert jedes Ereignis einzeln. Wenn eine Anfrage sowohl gültige als auch ungültige Ereignisse enthält, verarbeitet Braze die gültigen Ereignisse und gibt Details zu übersprungenen Ereignissen im `errors`-Array zurück. Wenn keine Ereignisse gültig sind, gibt Braze den Statuscode `400` zurück.

{% alert important %}
Diese Seite befindet sich in der Beta-Phase. Features und Dokumentation für die Device Messaging API können sich ändern. Wenden Sie sich an Ihren Braze Account Manager:in, um Zugang anzufordern.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie Folgendes:

- Einen Workspace mit aktiviertem Banner-Feature
- Einen [clientseitigen Representational State Transfer-API-Schlüssel]({{site.baseurl}}/api/device_messaging_api/authentication) mit der Berechtigung `banners.track`
- Den [Representational State Transfer-Endpunkt]({{site.baseurl}}/api/basics#endpoints) für Ihre Braze-Instanz
- Eine Banner-`id`, die vom Endpunkt [Banner für eine:n Nutzer:in abrufen]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners) zurückgegeben wird

Fügen Sie den clientseitigen Representational State Transfer-API-Schlüssel im `Authorization`-Header als Bearer-Token / Textbaustein ein.

## Rate-Limits {#rate-limit}

Rate-Limits gelten pro Workspace. Wenn Sie das Rate-Limit überschreiten, gibt Braze den Statuscode `429` zurück. Verwenden Sie nach Möglichkeit die Antwort-Header `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` und `X-RateLimit-Retry-After`, um Ihre Nutzung zu überwachen und den richtigen Zeitpunkt für einen erneuten Versuch zu bestimmen.

Weitere Informationen finden Sie unter [Device Messaging API – Rate-Limits]({{site.baseurl}}/api/device_messaging_api/rate_limits).

## Banner schließen (Dismiss) {#dismissing-banners}

Das Tracking eines `dismiss`-Ereignisses schließt das Banner für die/den jeweilige:n Nutzer:in. Nachfolgende Banner-Synchronisierungen für diese:n Nutzer:in enthalten zuvor geschlossene Banner nicht mehr, es sei denn, in der Campaign ist eine erneute Berechtigung konfiguriert.

{% alert note %}
Dismissal-Ereignisse werden asynchron verarbeitet und spiegeln sich nicht sofort wider. In seltenen Fällen kann die Verarbeitung einige Minuten dauern. Vermeiden Sie es, den Endpunkt [Banner für eine:n Nutzer:in abrufen]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners) unmittelbar nach einem Dismissal aufzurufen, da das Banner während dieses Zeitfensters möglicherweise noch zurückgegeben wird.
{% endalert %}

Braze gleicht den Status des Banners in Ihrer UI nicht ab. Das Ausblenden des Banners nach einem Dismissal und das Beibehalten des ausgeblendeten Zustands, bis Braze das Ereignis verarbeitet hat, liegt in der Verantwortung Ihrer App.

## Anfragekörper {#request-body}

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "{BANNER_ID}",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    }
  ]
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung | Beispiel |
|---|---|---|---|---|
| `external_user_id` | Erforderlich | String | Die externe ID der/des Nutzer:in, die/der mit allen Ereignissen in der Anfrage verknüpft ist. Der UTF-8-kodierte Wert muss weniger als 987 Bytes umfassen. | `user_abc123` |
| `app_id` | Erforderlich | String | Der [App-API-Bezeichner]({{site.baseurl}}/api/identifier_types#app-identifier). Er muss eine App im authentifizierten Workspace identifizieren. | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | Erforderlich | String | Die Version der Host-App. Sie darf 255 Zeichen nicht überschreiten. | `1.0.0` |
| `events` | Erforderlich | Array von Objekten | Ein oder mehrere Banner-Analytics-Ereignisse, die aufgezeichnet werden sollen. | `[{"id":"bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E","event_type":"impression","timestamp":"2026-04-09T12:00:00Z"}]` |
| `events[].id` | Erforderlich | String | Die Banner-`id`, die vom Endpunkt „Banner für eine:n Nutzer:in abrufen“ zurückgegeben wird. Verwenden Sie die Banner-ID, nicht die `placement_id`, damit Braze das Ereignis der richtigen Campaign und Variante zuordnet. | `bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E` |
| `events[].event_type` | Erforderlich | String | Der Ereignistyp. Mögliche Werte sind `impression`, `click` und `dismiss`. | `impression` |
| `events[].timestamp` | Erforderlich | String | Datum und Uhrzeit des Ereignisses, formatiert als [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)-String. | `2026-04-09T12:00:00Z` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}

Ersetzen Sie *`YOUR_REST_API_URL`* durch den [Representational State Transfer-Endpunkt]({{site.baseurl}}/api/basics#endpoints) für Ihre Braze-Instanz.

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/track' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    },
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "click",
      "timestamp": "2026-04-09T12:00:05Z"
    }
  ]
}'
```

## Antwortparameter {#response-parameters}

| Parameter | Datentyp | Beschreibung |
|---|---|---|
| `events_processed` | Integer | Die Anzahl der Ereignisse, die Braze validiert und in die Warteschlange gestellt hat. |
| `message` | String | Der Status des akzeptierten Ereignis-Batches. |
| `errors` | Array von Objekten | Details zu Ereignissen, die Braze übersprungen hat. Dieses Array fehlt, wenn Braze alle Ereignisse verarbeitet. |
| `errors[].type` | String | Der Validierungsfehler für das übersprungene Ereignis. |
| `errors[].index` | Integer | Der nullbasierte Index des übersprungenen Ereignisses im `events`-Array der Anfrage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Antwortparameter" }

## Beispielantworten {#example-responses}

### Alle Ereignisse verarbeitet {#all-events-processed}

Wenn Braze alle Ereignisse akzeptiert, gibt es den Statuscode `202` zurück.

```json
{
  "events_processed": 2,
  "message": "success"
}
```

### Einige Ereignisse übersprungen {#some-events-skipped}

Braze gibt ebenfalls den Statuscode `202` zurück, wenn mindestens ein gültiges Ereignis akzeptiert wird. Die Antwort identifiziert alle übersprungenen Ereignisse.

```json
{
  "events_processed": 2,
  "message": "success",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click, dismiss.",
      "index": 2
    }
  ]
}
```

### Keine gültigen Ereignisse {#no-valid-events}

Wenn Braze keine Ereignisse verarbeiten kann, gibt es den Statuscode `400` zurück.

```json
{
  "message": "No valid events provided.",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click, dismiss.",
      "index": 0
    },
    {
      "type": "'timestamp' is required",
      "index": 1
    }
  ]
}
```

## Statuscodes {#status-codes}

| Statuscode | Beschreibung |
|---|---|
| `202` | Braze hat mindestens ein Ereignis akzeptiert. Die Antwort listet alle übersprungenen Ereignisse auf. |
| `400` | Die Anfrage ist fehlerhaft, erforderliche Felder sind ungültig oder es sind keine gültigen Ereignisse vorhanden. |
| `401` | Der clientseitige Representational State Transfer-API-Schlüssel fehlt oder ist ungültig. |
| `403` | Der clientseitige Representational State Transfer-API-Schlüssel verfügt nicht über die Berechtigung `banners.track`. |
| `404` | Das Banner-Feature ist für den Workspace nicht aktiviert. |
| `429` | Der Workspace hat sein Rate-Limit überschritten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statuscodes" }

Weitere Informationen finden Sie unter [Device Messaging API – Fehlerbehandlung und Wiederholungsversuche]({{site.baseurl}}/api/device_messaging_api/error_handling).

{% endapi %}