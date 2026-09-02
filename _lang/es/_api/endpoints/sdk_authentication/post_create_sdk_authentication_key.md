---
nav_title: "POST: Crear clave de autenticación SDK"
article_title: "POST: Crear clave de autenticación SDK"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el endpoint de Braze para crear una clave de autenticación SDK."
---

{% api %}
# Crear clave de autenticación SDK {#create-sdk-authentication-key}
{% apimethod post %}
/app_group/sdk_authentication/create
{% endapimethod %}

> Utiliza este endpoint para crear una nueva clave de autenticación SDK para tu aplicación.

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `sdk_authentication.create`.

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
  "rsa_public_key_str": "RSA public key string",
  "description": "description",
  "make_primary": false
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `app_id` | Obligatorio | Cadena | El identificador de API de la aplicación. |
| `rsa_public_key_str` | Obligatorio | Cadena | La cadena de clave pública RSA. Debe ser una clave pública RSA válida o devolverá un error. |
| `description` | Obligatorio | Cadena | Descripción de la clave de autenticación SDK. |
| `make_primary` | Opcional | Booleano | Si se establece en `true`, esta clave se convertirá en la clave de autenticación SDK principal cuando se cree. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/app_group/sdk_authentication/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "rsa_public_key_str": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
  "description": "SDK Authentication Key for iOS App",
  "make_primary": false
}'
```

## Respuesta {#response}
```json
{
  "id": "key id"
}
```

## Parámetros de respuesta {#response-parameters}

| Parámetro | Tipo de datos | Descripción |
| --------- | --------- | ----------- |
| `id` | Cadena | El ID de la clave de autenticación SDK recién creada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parámetros de respuesta" }

### Reglas de validación {#validation-rules}

Este endpoint tiene las siguientes reglas de validación:

- Puedes tener hasta 3 claves de autenticación SDK por aplicación.
- La cadena de clave pública RSA debe ser una clave pública RSA válida con el formato adecuado.
- El `app_id` debe ser un identificador de API de aplicación válido.
- La descripción no puede estar vacía.

{% endapi %}