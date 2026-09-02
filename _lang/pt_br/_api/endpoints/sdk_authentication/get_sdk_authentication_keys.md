---
nav_title: "GET: Listar chaves de autenticação do SDK or kit de desenvolvimento de software"
article_title: "GET: Listar chaves de autenticação do SDK or kit de desenvolvimento de software"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para listar chaves de autenticação do SDK or kit de desenvolvimento de software."
---

{% API or interface de programação do aplicativo (API) %}
# Listar chaves de autenticação do SDK or kit de desenvolvimento de software {#list-sdk-authentication-keys}
{% apimethod get %}
/app_group/sdk_authentication/keys
{% endapimethod %}

> Use este endpoint para recuperar todas as chaves de autenticação do SDK or kit de desenvolvimento de software do seu app.

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `sdk_authentication.keys`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `app_id` | Obrigatório | String | O identificador de API or interface de programação do aplicativo (API) do app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/sdk_authentication/keys?app_id=01234567-89ab-cdef-0123-456789abcdef' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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
| `keys` | Array | Array de objetos de chaves de autenticação do SDK or kit de desenvolvimento de software. |
| `keys[].id` | String | O ID da chave de autenticação do SDK or kit de desenvolvimento de software. |
| `keys[].rsa_public_key` | String | A string da chave pública RSA. |
| `keys[].description` | String | Descrição da chave de autenticação do SDK or kit de desenvolvimento de software. |
| `keys[].is_primary` | Boolean | Se esta chave é a chave principal de autenticação do SDK or kit de desenvolvimento de software. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parâmetros de resposta" }

### Regras de validação {#validation-rules}

Este endpoint possui as seguintes regras de validação:

- O parâmetro `app_id` deve ser um identificador de API or interface de programação do aplicativo (API) de app válido.
- O app deve existir no seu espaço de trabalho.

{% endapi %}