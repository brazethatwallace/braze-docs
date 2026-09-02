---
nav_title: "DELETE: Remover chave de autenticação do SDK"
article_title: "DELETE: Remover chave de autenticação do SDK"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para excluir a chave de autenticação do SDK."
---

{% api %}
# Excluir chave de autenticação do SDK {#delete-sdk-authentication-key}
{% apimethod delete %}
/app_group/sdk_authentication/delete
{% endapimethod %}

> Use este endpoint para excluir uma chave de autenticação do SDK para seu app.

{% alert important %}
A chave primária não pode ser excluída. Se você tentar excluir a chave primária, este endpoint retornará um erro.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `sdk_authentication.delete`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação {#request-body}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API Identifier",
  "key_id": "key id"
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `app_id` | Obrigatório | String | O identificador de API do app. |
| `key_id` | Obrigatório | String | O ID da chave de autenticação do SDK a ser excluída. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/app_group/sdk_authentication/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "fedcba98-7654-3210-fedc-ba9876543210"
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
    }
  ]
}
```

## Parâmetros de resposta {#response-parameters}

| Parâmetro | Tipo de dados | Descrição |
| --------- | --------- | ----------- |
| `keys` | Array | Array de objetos de chaves de autenticação do SDK restantes. |
| `keys[].id` | String | O ID da chave de autenticação do SDK. |
| `keys[].rsa_public_key` | String | A string da chave pública RSA. |
| `keys[].description` | String | Descrição da chave de autenticação do SDK. |
| `keys[].is_primary` | Boolean | Se esta chave é a chave primária de autenticação do SDK. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parâmetros de resposta" }

### Regras de validação {#validation-rules}

Este endpoint possui as seguintes regras de validação:

- O `key_id` deve ser um ID válido de chave de autenticação do SDK.
- O `app_id` deve ser um identificador de API de app válido.
- A chave de autenticação do SDK deve existir para o app especificado.
- A chave primária de autenticação do SDK não pode ser excluída.

{% endapi %}