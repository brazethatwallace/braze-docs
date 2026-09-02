---
nav_title: "POST: Atualizar credenciais de push"
article_title: "POST: Atualizar credenciais de push"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Atualizar credenciais de push da Braze."
---

{% API or interface de programação do aplicativo (API) %}
# Atualizar credenciais de push {#update-push-credentials}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/apps/push_credential/update
{% endapimethod %}

> Use este endpoint para atualizar programaticamente as credenciais de push de um único app, permitindo gerenciar credenciais sem usar a interface do dashboard.

Cada solicitação atualiza as credenciais de push de um app e uma plataforma de push. Arquivos de credenciais, como a chave de autenticação do iOS ou a conta de serviço do Firebase, são passados como strings codificadas em [Base64](https://en.wikipedia.org/wiki/Base64) dentro do corpo da solicitação JSON.

Este endpoint é compatível com as seguintes plataformas de push:

| Plataforma | Credenciais |
|---|---|
| iOS (APNs) | Somente chave de autenticação `.p8`. Certificados `.p12` e `.pem` não são compatíveis com este endpoint. |
| Android (Firebase Cloud Messaging) | JSON da conta de serviço |
| Android (Huawei Mobile Services) | ID do app e segredo do app |
| Kindle (Amazon Device Messaging) | ID do cliente e segredo do cliente |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plataformas de push compatíveis" }

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `apps.push_credential`.

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Inclua um objeto de plataforma por solicitação: `apple`, `firebase`, `huawei` ou `kindle`.

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

## Parâmetros da solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| [`app_id`]({{site.baseurl}}/api/identifier_types#app-identifier) | Obrigatório | String | A chave de API or interface de programação do aplicativo (API) do identificador do app que você deseja atualizar. Encontre-a no dashboard em **Configurações** > **Configurações do app**, ao lado do campo **Chave de API or interface de programação do aplicativo (API)**. |
| `apple` | Obrigatório* | Objeto | As credenciais do iOS (APNs). |
| `firebase` | Obrigatório* | Objeto | As credenciais do Android (Firebase Cloud Messaging). |
| `huawei` | Obrigatório* | Objeto | As credenciais do Android (Huawei Mobile Services). |
| `kindle` | Obrigatório* | Objeto | As credenciais do Kindle (Amazon Device Messaging). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros da solicitação" }

\* Inclua exatamente um objeto de plataforma por solicitação.

### Parâmetros do iOS (APNs) {#ios-apns-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `certificate` | Obrigatório | String | A chave de autenticação `.p8` codificada em Base64. Somente chaves de autenticação `.p8` são compatíveis; certificados `.p12` e `.pem` não são compatíveis com este endpoint. |
| `jwt_key_id` | Obrigatório | String | O ID da chave de autenticação `.p8`. |
| `jwt_team_id` | Obrigatório | String | O ID da equipe do Apple Developer. |
| `jwt_bundle_id` | Obrigatório | String | O bundle ID do seu app. |
| `apns_gateway` | Obrigatório | String | O ambiente APNs. Os valores disponíveis são `prod` e `dev`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros do iOS (APNs)" }

### Parâmetros do Android (Firebase Cloud Messaging) {#android-firebase-cloud-messaging-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `credential` | Obrigatório | String | O JSON da conta de serviço do Firebase codificado em Base64. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros do Android (Firebase Cloud Messaging)" }

### Parâmetros do Android (Huawei Mobile Services) {#android-huawei-mobile-services-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `app_id` | Obrigatório | String | O ID do app Huawei. |
| `app_secret` | Obrigatório | String | O segredo do app Huawei. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros do Android (Huawei Mobile Services)" }

### Parâmetros do Kindle (Amazon Device Messaging) {#kindle-amazon-device-messaging-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `client_id` | Obrigatório | String | O ID do cliente do Amazon Device Messaging. |
| `client_secret` | Obrigatório | String | O segredo do cliente do Amazon Device Messaging. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros do Kindle (Amazon Device Messaging)" }

## Exemplos de solicitação {#example-requests}

### iOS (APNs)

O valor de `apple.certificate` deve ser codificado em Base64, e `apple.apns_gateway` deve ser definido como `prod` ou `dev`.

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

O valor de `firebase.credential` deve ser codificado em Base64.

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

## Exemplo de resposta {#example-response}

Se as credenciais forem atualizadas com sucesso, você receberá uma resposta com o código de status `201`.

```json
{
  "message": "success"
}
```

{% endapi %}