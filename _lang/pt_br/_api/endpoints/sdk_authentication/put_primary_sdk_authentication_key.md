---
nav_title: "PUT: Definir a chave primária de autenticação do SDK or kit de desenvolvimento de software"
article_title: "PUT: Definir a chave primária de autenticação do SDK or kit de desenvolvimento de software"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para definir a chave primária de autenticação do SDK or kit de desenvolvimento de software."
---

{% API or interface de programação do aplicativo (API) %}
# Definir a chave primária de autenticação do SDK or kit de desenvolvimento de software {#set-primary-sdk-authentication-key}
{% apimethod put %}
/app_group/sdk_authentication/primary
{% endapimethod %}

> Use este endpoint para definir uma chave de autenticação do SDK or kit de desenvolvimento de software como a chave primária para seu app.

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `sdk_authentication.primary`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação {#request-body}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API identifier",
  "key_id": "key id"
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | É necessário informar | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `app_id` | É necessário informar | String | O identificador de API or interface de programação do aplicativo (API) do app. |
| `key_id` | É necessário informar | String | O ID da chave de autenticação do SDK or kit de desenvolvimento de software a ser marcada como primária. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/app_group/sdk_authentication/primary' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "abcdef12-3456-7890-abcd-ef1234567890"
}'
```

## Resposta {#response}
```json
{
  "keys": [
    {
      "id": "abcdef12-3456-7890-abcd-ef1234567890",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for iOS App",
      "is_primary": true
    },
    {
      "id": "fedcba98-7654-3210-fedc-ba9876543210",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nqWGfHOAiIwVzC/bTxwQZQQVzm/3ktgdNXRUDm5aIwVzCtxbNm5aIxOAiIwVzVHOA...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for Android App",
      "is_primary": false
    }
  ]
}
```

## Parâmetros de resposta {#response-parameters}

| Parâmetro | Tipo de dados | Descrição |
| --------- | --------- | ----------- |
| `keys` | Array | Array de todos os objetos de chave de autenticação do SDK or kit de desenvolvimento de software. |
| `keys[].id` | String | O ID da chave de autenticação do SDK or kit de desenvolvimento de software. |
| `keys[].rsa_public_key` | String | A string da chave pública RSA. |
| `keys[].description` | String | Descrição da chave de autenticação do SDK or kit de desenvolvimento de software. |
| `keys[].is_primary` | Boolean | Se esta chave é a chave primária de autenticação do SDK or kit de desenvolvimento de software. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parâmetros de resposta" }

### Regras de validação {#validation-rules}

Este endpoint possui as seguintes regras de validação:

- O `key_id` deve ser um ID de chave de autenticação do SDK or kit de desenvolvimento de software válido.
- O `app_id` deve ser um identificador de API or interface de programação do aplicativo (API) de app válido.
- A chave de autenticação do SDK or kit de desenvolvimento de software deve existir para o app especificado.

{% endapi %}