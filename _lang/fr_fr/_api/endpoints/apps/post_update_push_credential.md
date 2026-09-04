---
nav_title: "POST : Mettre à jour les identifiants push"
article_title: "POST : Mettre à jour les identifiants push"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Braze de mise à jour des identifiants push."
---

{% api %}
# Mettre à jour les identifiants push {#update-push-credentials}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/apps/push_credential/update
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour de manière programmatique les identifiants push d'une seule application, afin de gérer les identifiants sans passer par l'interface du tableau de bord.

Chaque requête met à jour les identifiants push pour une application et une plateforme push. Les fichiers d'identifiants, tels que la clé d'authentification iOS ou le compte de service Firebase, sont transmis sous forme de chaînes encodées en [Base64](https://en.wikipedia.org/wiki/Base64) dans le corps de la requête JSON.

Cet endpoint prend en charge les plateformes push suivantes :

| Plateforme | Identifiants |
|---|---|
| iOS (APNs) | Clé d'authentification `.p8` uniquement. Les certificats `.p12` et `.pem` ne sont pas pris en charge par cet endpoint. |
| Android (Firebase Cloud Messaging) | JSON du compte de service |
| Android (Huawei Mobile Services) | ID d'application et secret d'application |
| Kindle (Amazon Device Messaging) | ID client et secret client |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plateformes push prises en charge" }

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `apps.push_credential`.

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Incluez un seul objet de plateforme par requête : `apple`, `firebase`, `huawei` ou `kindle`.

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

## Paramètres de requête {#request-parameters}

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| [`app_id`]({{site.baseurl}}/api/identifier_types#app-identifier) | Obligatoire | String | La clé API d'identifiant d'application pour l'application que vous souhaitez mettre à jour. Vous la trouverez dans le tableau de bord sous **Paramètres** > **Paramètres de l'application**, à côté du champ **Clé API**. |
| `apple` | Obligatoire* | Objet | Les identifiants iOS (APNs). |
| `firebase` | Obligatoire* | Objet | Les identifiants Android (Firebase Cloud Messaging). |
| `huawei` | Obligatoire* | Objet | Les identifiants Android (Huawei Mobile Services). |
| `kindle` | Obligatoire* | Objet | Les identifiants Kindle (Amazon Device Messaging). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

\* Incluez exactement un objet de plateforme par requête.

### Paramètres iOS (APNs) {#ios-apns-parameters}

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `certificate` | Obligatoire | String | La clé d'authentification `.p8` encodée en Base64. Seules les clés d'authentification `.p8` sont prises en charge ; les certificats `.p12` et `.pem` ne sont pas pris en charge par cet endpoint. |
| `jwt_key_id` | Obligatoire | String | L'ID de clé pour la clé d'authentification `.p8`. |
| `jwt_team_id` | Obligatoire | String | Votre ID d'équipe Apple Developer. |
| `jwt_bundle_id` | Obligatoire | String | L'ID de bundle de votre application. |
| `apns_gateway` | Obligatoire | String | L'environnement APNs. Les valeurs disponibles sont `prod` et `dev`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres iOS (APNs)" }

### Paramètres Android (Firebase Cloud Messaging) {#android-firebase-cloud-messaging-parameters}

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `credential` | Obligatoire | String | Le JSON du compte de service Firebase encodé en Base64. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres Android (Firebase Cloud Messaging)" }

### Paramètres Android (Huawei Mobile Services) {#android-huawei-mobile-services-parameters}

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `app_id` | Obligatoire | String | Votre ID d'application Huawei. |
| `app_secret` | Obligatoire | String | Votre secret d'application Huawei. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres Android (Huawei Mobile Services)" }

### Paramètres Kindle (Amazon Device Messaging) {#kindle-amazon-device-messaging-parameters}

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `client_id` | Obligatoire | String | Votre ID client Amazon Device Messaging. |
| `client_secret` | Obligatoire | String | Votre secret client Amazon Device Messaging. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres Kindle (Amazon Device Messaging)" }

## Exemples de requêtes {#example-requests}

### iOS (APNs)

La valeur `apple.certificate` doit être encodée en Base64, et `apple.apns_gateway` doit être défini sur `prod` ou `dev`.

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

La valeur `firebase.credential` doit être encodée en Base64.

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

## Exemple de réponse {#example-response}

Si les identifiants sont mis à jour avec succès, vous recevrez une réponse avec le code de statut `201`.

```json
{
  "message": "success"
}
```

{% endapi %}