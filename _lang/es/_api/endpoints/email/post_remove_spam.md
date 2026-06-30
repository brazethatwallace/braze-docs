---
nav_title: "POST: Eliminar direcciones de correo electrónico de la lista de correo no deseado"
article_title: "POST: Eliminar direcciones de correo electrónico de la lista de correo no deseado"
search_tag: Endpoint
page_order: 7
layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el punto de conexión de Braze Eliminar direcciones de correo electrónico de la lista de correo no deseado."

---
{% api %}
# Eliminar direcciones de correo electrónico de la lista de correo no deseado {#remove-email-addresses-from-spam-list}
{% apimethod post %}
/email/spam/remove
{% endapimethod %}

> Utiliza este punto de conexión para eliminar direcciones de correo electrónico de tu lista de correo no deseado de Braze y de la lista de correo no deseado mantenida por tu proveedor de correo electrónico.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `email.spam.remove`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud {#request-body}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@example.com"
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| ----------|-----------| --------|------- |
| `email` | Obligatorio | Cadena o matriz | Dirección de correo electrónico en forma de cadena a modificar, o una matriz de hasta 50 direcciones de correo electrónico a modificar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@example.com"
}'
```
{% endapi %}