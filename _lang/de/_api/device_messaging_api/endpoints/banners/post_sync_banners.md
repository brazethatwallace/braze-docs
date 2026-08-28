---
nav_title: "POST: Banner für eine:n Nutzer:in abrufen"
article_title: "POST: Banner für eine:n Nutzer:in abrufen"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Verwenden Sie diesen Endpunkt, um berechtigte Banner für eine:n Nutzer:in abzurufen."
hidden: true
---

{% api %}
# Banner für eine:n Nutzer:in abrufen {#retrieve-banners-for-a-user}
{% apimethod post %}
/v1/device-messaging/banners/sync
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um das berechtigte Banner für jede angeforderte Platzierung für eine:n Nutzer:in abzurufen.

Die Antwort enthält strukturierte Banner-Eigenschaften, die Sie zum Erstellen einer benutzerdefinierten Oberfläche verwenden können. Sie enthält kein gerendertes HTML.

{% alert important %}
Diese Seite befindet sich in der Beta-Phase. Features und Dokumentation für die Device Messaging API können sich ändern. Wenden Sie sich an Ihren Braze Account Manager, um Zugang anzufordern.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie Folgendes:

- Einen Workspace mit aktivierten Bannern
- Einen [clientseitigen REST-API-Schlüssel]({{site.baseurl}}/api/device_messaging_api/authentication) mit der Berechtigung `banners.sync`
- Den [REST-Endpunkt]({{site.baseurl}}/api/basics#endpoints) für Ihre Braze-Instanz

Fügen Sie den clientseitigen REST-API-Schlüssel im `Authorization`-Header als Bearer-Token ein.

## Rate-Limits {#rate-limit}

Rate-Limits gelten pro Workspace. Wenn Sie das Rate-Limit überschreiten, gibt Braze den Statuscode `429` zurück. Verwenden Sie nach Möglichkeit die Antwort-Header `X-RateLimit-Limit`, `X-RateLimit-Remaining` und `X-RateLimit-Reset`, um Ihre Nutzung zu überwachen.

Weitere Informationen finden Sie unter [Rate-Limits der Device-Messaging-API]({{site.baseurl}}/api/device_messaging_api/rate_limits).

## Anfragekörper {#request-body}

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung | Beispiel |
|---|---|---|---|---|
| `external_user_id` | Erforderlich | String | Die externe ID der/des Nutzer:in. | `user_abc123` |
| `app_id` | Erforderlich | String | Der [App-API-Bezeichner]({{site.baseurl}}/api/identifier_types#app-identifier). Er muss eine App im authentifizierten Workspace identifizieren. | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | Erforderlich | String | Die Version der Host-App. Sie darf 255 Zeichen nicht überschreiten. | `1.0.0` |
| `placements` | Erforderlich | String-Array | Eine oder mehrere Platzierungs-IDs, für die Banner abgerufen werden sollen. Geben Sie mindestens eine Platzierungs-ID an. | `["home_hero", "sidebar_promo"]` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}

Ersetzen Sie *`YOUR_REST_API_URL`* durch den [REST-Endpunkt]({{site.baseurl}}/api/basics#endpoints) für Ihre Braze-Instanz.

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/sync' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}'
```

## Antwortparameter {#response-parameters}

| Parameter | Datentyp | Beschreibung |
|---|---|---|
| `banners` | Objekt | Eine Zuordnung jeder angeforderten Platzierungs-ID zu ihrem aufgelösten Banner. Der Wert ist `null`, wenn kein Banner für eine Platzierung berechtigt ist. |
| `banners.{placement_id}.id` | String | Der eindeutige Banner-Bezeichner. Verwenden Sie diesen Wert, um Impression- und Klick-Events zu melden. |
| `banners.{placement_id}.placement_id` | String | Die dem Banner zugeordnete Platzierungs-ID. |
| `banners.{placement_id}.is_control` | Boolean | Ob das Banner eine Kontrollgruppen-Variante ist. |
| `banners.{placement_id}.is_test_send` | Boolean | Ob das Banner aus einem Testversand stammt. Standardmäßig `false`. |
| `banners.{placement_id}.expires_at` | Integer | Der Unix-Zeitstempel in Sekunden, nach dem das Banner nicht mehr angezeigt werden sollte. Ein Wert von `-1` bedeutet, dass das Banner nicht abläuft. |
| `banners.{placement_id}.properties` | Objekt oder null | Vom Marketer definierte Eigenschaften für das Banner. Jede Eigenschaft enthält einen `type` und einen `value`. |
| `banners.{placement_id}.properties.{property}.type` | String | Der Typ der Eigenschaft. Mögliche Werte sind `number`, `string`, `boolean`, `image`, `jsonobject` und `datetime`. |
| `banners.{placement_id}.properties.{property}.value` | Number, String, Boolean oder Objekt | Der Wert der Eigenschaft. Der JSON-Typ entspricht dem `type`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Antwortparameter" }

## Beispielantwort {#example-response}

Eine erfolgreiche Anfrage gibt den Statuscode `200` und das aufgelöste Banner für jede angeforderte Platzierung zurück.

```json
{
  "banners": {
    "home_hero": {
      "id": "this_banner_is_a_stub_01",
      "placement_id": "home_hero",
      "is_control": false,
      "is_test_send": false,
      "expires_at": 1735689600,
      "properties": {
        "headline": {
          "type": "string",
          "value": "Level Up Your Game"
        },
        "cta_label": {
          "type": "string",
          "value": "Shop Now"
        }
      }
    },
    "sidebar_promo": null
  }
}
```

## Statuscodes {#status-codes}

| Statuscode | Beschreibung |
|---|---|
| `200` | Braze hat Banner-Daten für jede angeforderte Platzierung aufgelöst. |
| `400` | Die Anfrage enthält fehlende oder ungültige Parameter. |
| `401` | Der clientseitige REST-API-Schlüssel fehlt, ist ungültig oder verfügt nicht über die Berechtigung `banners.sync`. |
| `404` | Der Endpunkt ist nicht verfügbar. Diese Antwort unterscheidet nicht zwischen einem fehlenden oder ungültigen API-Schlüssel und einem deaktivierten Banner-Feature. |
| `429` | Der Workspace hat sein Rate-Limit überschritten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statuscodes" }

Weitere Informationen finden Sie unter [Fehlerbehandlung und Wiederholungsversuche der Device-Messaging-API]({{site.baseurl}}/api/device_messaging_api/error_handling).

{% endapi %}