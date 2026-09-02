---
nav_title: "POST: Push-Zugangsdaten Update or aktualisieren or aktualisieren"
article_title: "POST: Push-Zugangsdaten Update or aktualisieren or aktualisieren"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Braze-Endpunkt zum Update or aktualisieren or aktualisieren von Push-Zugangsdaten."
---

{% api %}
# Push-Zugangsdaten Update or aktualisieren or aktualisieren {#update-push-credentials}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/apps/push_credential/Update or aktualisieren
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die Push-Zugangsdaten für eine einzelne App programmatisch zu Update or aktualisieren or aktualisieren, sodass Sie Zugangsdaten verwalten können, ohne die Dashboard-UI zu verwenden.

Jede Anfrage aktualisiert die Push-Zugangsdaten für eine App und eine Push-Plattform. Zugangsdaten-Dateien, wie der iOS-Authentifizierungsschlüssel oder das Firebase-Dienstkonto, werden als [Base64](https://en.wikipedia.org/wiki/Base64)-kodierte Strings im JSON-Anfragekörper übergeben.

Dieser Endpunkt unterstützt die folgenden Push-Plattformen:

| Plattform | Zugangsdaten |
|---|---|
| iOS (APNs) | Nur `.p8`-Authentifizierungsschlüssel. `.p12`- und `.pem`-Zertifikate werden von diesem Endpunkt nicht unterstützt. |
| Android (Firebase Cloud Messaging) | Dienstkonto-JSON |
| Android (Huawei Mobile Services) | App-ID und App-Secret |
| Kindle (Amazon Device Messaging) | Client-ID und Client-Secret |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unterstützte Push-Plattformen" }

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `apps.push_credential`.

## Anfragekörper {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Fügen Sie pro Anfrage ein Plattform-Objekt ein: `apple`, `firebase`, `huawei` oder `kindle`.

{% tabs %}
{% tab iOS (APNs) %}
```json
{
  "app_id": (required, string) the app identifier API key found under Settings > App Settings,
  "apple": {
    "certificate": (required, string) the Base64-encoded .p8 authentication key,
    "jwt_key_id": (required, string) the key ID for the .p8 authentication key,
    "jwt_team_id": (required, string) your Apple Developer team ID,
    "jwt_bundle_id": (required, string) your app's bundle ID,
    "apns_gateway": (required, string) either "prod" or "dev"
  }
}
```
{% endtab %}
{% tab Android (Firebase Cloud Messaging) %}
```json
{
  "app_id": (required, string) the app identifier API key found under Settings > App Settings,
  "firebase": {
    "credential": (required, string) the Base64-encoded Firebase service account JSON
  }
}
```
{% endtab %}
{% tab Android (Huawei Mobile Services) %}
```json
{
  "app_id": (required, string) the app identifier API key found under Settings > App Settings,
  "huawei": {
    "app_id": (required, string) your Huawei app ID,
    "app_secret": (required, string) your Huawei app secret
  }
}
```
{% endtab %}
{% tab Kindle (Amazon Device Messaging) %}
```json
{
  "app_id": (required, string) the app identifier API key found under Settings > App Settings,
  "kindle": {
    "client_id": (required, string) your Amazon Device Messaging client ID,
    "client_secret": (required, string) your Amazon Device Messaging client secret
  }
}
```
{% endtab %}
{% endtabs %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| [`app_id`]({{site.baseurl}}/api/identifier_types#app-identifier) | Erforderlich | String | Der App-Bezeichner-API-Schlüssel für die App, die Sie Update or aktualisieren or aktualisieren möchten. Sie finden ihn im Dashboard unter **Einstellungen** > **App-Einstellungen** neben dem Feld **API-Schlüssel**. |
| `apple` | Erforderlich* | Objekt | Die iOS (APNs)-Zugangsdaten. |
| `firebase` | Erforderlich* | Objekt | Die Android (Firebase Cloud Messaging)-Zugangsdaten. |
| `huawei` | Erforderlich* | Objekt | Die Android (Huawei Mobile Services)-Zugangsdaten. |
| `kindle` | Erforderlich* | Objekt | Die Kindle (Amazon Device Messaging)-Zugangsdaten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter" }

\* Fügen Sie pro Anfrage genau ein Plattform-Objekt ein.

### iOS (APNs)-Parameter {#ios-apns-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `certificate` | Erforderlich | String | Der Base64-kodierte `.p8`-Authentifizierungsschlüssel. Es werden nur `.p8`-Authentifizierungsschlüssel unterstützt; `.p12`- und `.pem`-Zertifikate werden von diesem Endpunkt nicht unterstützt. |
| `jwt_key_id` | Erforderlich | String | Die Schlüssel-ID für den `.p8`-Authentifizierungsschlüssel. |
| `jwt_team_id` | Erforderlich | String | Ihre Apple Developer Team-ID. |
| `jwt_bundle_id` | Erforderlich | String | Die Bundle-ID Ihrer App. |
| `apns_gateway` | Erforderlich | String | Die APNs-Umgebung. Verfügbare Werte sind `prod` und `dev`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="iOS (APNs)-Parameter" }

### Android (Firebase Cloud Messaging)-Parameter {#android-firebase-cloud-messaging-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `credential` | Erforderlich | String | Das Base64-kodierte Firebase-Dienstkonto-JSON. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Android (Firebase Cloud Messaging)-Parameter" }

### Android (Huawei Mobile Services)-Parameter {#android-huawei-mobile-services-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `app_id` | Erforderlich | String | Ihre Huawei-App-ID. |
| `app_secret` | Erforderlich | String | Ihr Huawei-App-Secret. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Android (Huawei Mobile Services)-Parameter" }

### Kindle (Amazon Device Messaging)-Parameter {#kindle-amazon-device-messaging-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `client_id` | Erforderlich | String | Ihre Amazon Device Messaging Client-ID. |
| `client_secret` | Erforderlich | String | Ihr Amazon Device Messaging Client-Secret. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Kindle (Amazon Device Messaging)-Parameter" }

## Beispielanfragen {#example-requests}

### iOS (APNs)

Der Wert `apple.certificate` muss Base64-kodiert sein, und `apple.apns_gateway` muss auf `prod` oder `dev` gesetzt werden.

```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "apple": {
    "certificate": "{BASE64_ENCODED_STRING}",
    "jwt_key_id": "{YOUR_KEY_ID}",
    "jwt_team_id": "{YOUR_TEAM_ID}",
    "jwt_bundle_id": "{YOUR_BUNDLE_ID}",
    "apns_gateway": "prod"
  }
}'
```

### Android (Firebase Cloud Messaging)

Der Wert `firebase.credential` muss Base64-kodiert sein.

```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "firebase": {
    "credential": "{BASE64_ENCODED_STRING}"
  }
}'
```

### Android (Huawei Mobile Services)

```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "huawei": {
    "app_id": "{YOUR_HUAWEI_APP_ID}",
    "app_secret": "{YOUR_HUAWEI_APP_SECRET}"
  }
}'
```

### Kindle (Amazon Device Messaging)

```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "kindle": {
    "client_id": "{YOUR_ADM_CLIENT_ID}",
    "client_secret": "{YOUR_ADM_CLIENT_SECRET}"
  }
}'
```

## Beispielantwort {#example-response}

Wenn die Zugangsdaten erfolgreich aktualisiert wurden, erhalten Sie eine Antwort mit dem Statuscode `201`.

```json
{
  "message": "success"
}
```

{% endapi %}