---
nav_title: "DELETE: Eliminar clave de autenticación SDK"
article_title: "DELETE: Eliminar clave de autenticación SDK"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint de Braze para eliminar una clave de autenticación SDK."
---

{% api %}
# Eliminar clave de autenticación SDK {#delete-sdk-authentication-key}
{% apimethod delete %}
/app_group/sdk_authentication/delete
{% endapimethod %}

> Utiliza este endpoint para eliminar una clave de autenticación SDK de tu aplicación.

{% alert important %}
La clave principal no se puede eliminar. Si intentas eliminar la clave principal, este endpoint devolverá un error.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `sdk_authentication.delete`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud {#request-body}
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

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `app_id` | Obligatorio | Cadena | El identificador de API de la aplicación. |
| `key_id` | Obligatorio | Cadena | El ID de la clave de autenticación SDK que se va a eliminar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/app_group/sdk_authentication/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "fedcba98-7654-3210-fedc-ba9876543210"
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
    }
  ]
}
```

## Parámetros de respuesta {#response-parameters}

| Parámetro | Tipo de datos | Descripción |
| --------- | --------- | ----------- |
| `keys` | Matriz | Matriz de objetos de clave de autenticación SDK restantes. |
| `keys[].id` | Cadena | El ID de la clave de autenticación SDK. |
| `keys[].rsa_public_key` | Cadena | La cadena de clave pública RSA. |
| `keys[].description` | Cadena | Descripción de la clave de autenticación SDK. |
| `keys[].is_primary` | Booleano | Si esta clave es la clave de autenticación SDK principal. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parámetros de respuesta" }

### Reglas de validación {#validation-rules}

Este endpoint tiene las siguientes reglas de validación:

- El `key_id` debe ser un ID de clave de autenticación SDK válido.
- El `app_id` debe ser un identificador de API de aplicación válido.
- La clave de autenticación SDK debe existir para la aplicación especificada.
- La clave de autenticación SDK principal no se puede eliminar.

{% endapi %}