---
nav_title: "PUT: Establecer la clave de autenticación SDK or kit de desarrollo de software principal"
article_title: "PUT: Establecer la clave de autenticación SDK or kit de desarrollo de software principal"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el endpoint de Braze para establecer la clave de autenticación SDK or kit de desarrollo de software principal."
---

{% api %}
# Establecer la clave de autenticación SDK or kit de desarrollo de software principal {#set-primary-sdk-authentication-key}
{% apimethod put %}
/app_group/sdk_authentication/primary
{% endapimethod %}

> Utiliza este endpoint para establecer una clave de autenticación SDK or kit de desarrollo de software como clave principal para tu aplicación.

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `sdk_authentication.primary`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud {#request-body}
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

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `app_id` | Obligatorio | Cadena | El identificador de API de la aplicación. |
| `key_id` | Obligatorio | Cadena | El ID de la clave de autenticación SDK or kit de desarrollo de software que se va a marcar como principal. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/app_group/sdk_authentication/primary' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "abcdef12-3456-7890-abcd-ef1234567890"
}'
```

## Respuesta {#response}
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

## Parámetros de respuesta {#response-parameters}

| Parámetro | Tipo de datos | Descripción |
| --------- | --------- | ----------- |
| `keys` | Matriz | Matriz de todos los objetos de clave de autenticación SDK or kit de desarrollo de software. |
| `keys[].id` | Cadena | El ID de la clave de autenticación SDK or kit de desarrollo de software. |
| `keys[].rsa_public_key` | Cadena | La cadena de clave pública RSA. |
| `keys[].description` | Cadena | Descripción de la clave de autenticación SDK or kit de desarrollo de software. |
| `keys[].is_primary` | Booleano | Si esta clave es la clave de autenticación SDK or kit de desarrollo de software principal. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parámetros de respuesta" }

### Reglas de validación {#validation-rules}

Este endpoint tiene las siguientes reglas de validación:

- El `key_id` debe ser un ID de clave de autenticación SDK or kit de desarrollo de software válido.
- El `app_id` debe ser un identificador de API de aplicación válido.
- La clave de autenticación SDK or kit de desarrollo de software debe existir para la aplicación especificada.

{% endapi %}