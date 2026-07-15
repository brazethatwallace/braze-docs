---
nav_title: "POST: Actualizar credenciales push"
article_title: "POST: Actualizar credenciales push"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint de Braze Actualizar credenciales push."
---

{% api %}
# Actualizar credenciales push {#update-push-credentials}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/apps/push_credential/update
{% endapimethod %}

> Utiliza este endpoint para actualizar de forma programática las credenciales push de una sola aplicación, de modo que puedas gestionar las credenciales sin usar la interfaz del panel.

Cada solicitud actualiza las credenciales push de una aplicación y una plataforma push. Los archivos de credenciales, como la clave de autenticación de iOS o la cuenta de servicio de Firebase, se pasan como cadenas codificadas en [Base64](https://en.wikipedia.org/wiki/Base64) dentro del cuerpo de la solicitud JSON.

Este endpoint es compatible con las siguientes plataformas push:

| Plataforma | Credenciales |
|---|---|
| iOS (APNs) | Solo clave de autenticación `.p8`. Los certificados `.p12` y `.pem` no son compatibles con este endpoint. |
| Android (Firebase Cloud Messaging) | JSON de cuenta de servicio |
| Android (Huawei Mobile Services) | ID de aplicación y secreto de aplicación |
| Kindle (Amazon Device Messaging) | ID de cliente y secreto de cliente |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plataformas push compatibles" }

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `apps.push_credential`.

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Incluye un objeto de plataforma por solicitud: `apple`, `firebase`, `huawei` o `kindle`.

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

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| [`app_id`]({{site.baseurl}}/api/identifier_types#app-identifier) | Obligatorio | Cadena | La clave de API del identificador de la aplicación que deseas actualizar. Encuéntrala en el panel en **Configuración** > **Configuración de la aplicación**, junto al campo **Clave de API**. |
| `apple` | Obligatorio* | Objeto | Las credenciales de iOS (APNs). |
| `firebase` | Obligatorio* | Objeto | Las credenciales de Android (Firebase Cloud Messaging). |
| `huawei` | Obligatorio* | Objeto | Las credenciales de Android (Huawei Mobile Services). |
| `kindle` | Obligatorio* | Objeto | Las credenciales de Kindle (Amazon Device Messaging). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de la solicitud" }

\* Incluye exactamente un objeto de plataforma por solicitud.

### Parámetros de iOS (APNs) {#ios-apns-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `certificate` | Obligatorio | Cadena | La clave de autenticación `.p8` codificada en Base64. Solo se admiten claves de autenticación `.p8`; los certificados `.p12` y `.pem` no son compatibles con este endpoint. |
| `jwt_key_id` | Obligatorio | Cadena | El ID de clave para la clave de autenticación `.p8`. |
| `jwt_team_id` | Obligatorio | Cadena | Tu ID de equipo de Apple Developer. |
| `jwt_bundle_id` | Obligatorio | Cadena | El ID de paquete de tu aplicación. |
| `apns_gateway` | Obligatorio | Cadena | El entorno de APNs. Los valores disponibles son `prod` y `dev`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de iOS (APNs)" }

### Parámetros de Android (Firebase Cloud Messaging) {#android-firebase-cloud-messaging-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `credential` | Obligatorio | Cadena | El JSON de cuenta de servicio de Firebase codificado en Base64. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de Android (Firebase Cloud Messaging)" }

### Parámetros de Android (Huawei Mobile Services) {#android-huawei-mobile-services-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `app_id` | Obligatorio | Cadena | Tu ID de aplicación de Huawei. |
| `app_secret` | Obligatorio | Cadena | Tu secreto de aplicación de Huawei. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de Android (Huawei Mobile Services)" }

### Parámetros de Kindle (Amazon Device Messaging) {#kindle-amazon-device-messaging-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `client_id` | Obligatorio | Cadena | Tu ID de cliente de Amazon Device Messaging. |
| `client_secret` | Obligatorio | Cadena | Tu secreto de cliente de Amazon Device Messaging. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de Kindle (Amazon Device Messaging)" }

## Ejemplos de solicitudes {#example-requests}

### iOS (APNs)

El valor de `apple.certificate` debe estar codificado en Base64, y `apple.apns_gateway` debe establecerse en `prod` o `dev`.

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

El valor de `firebase.credential` debe estar codificado en Base64.

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

## Ejemplo de respuesta {#example-response}

Si las credenciales se actualizan correctamente, recibirás una respuesta con el código de estado `201`.

```json
{
  "message": "success"
}
```

{% endapi %}