---
nav_title: "POST: Eliminar números de teléfono no válidos"
article_title: "POST: Eliminar números de teléfono no válidos"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Eliminar números de teléfono no válidos de Braze."

---
{% api %}
# Eliminar números de teléfono no válidos {#remove-invalid-phone-numbers}

{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

> Usa este endpoint para eliminar números de teléfono "no válidos" de nuestra lista de no válidos.

Se puede utilizar para volver a validar números de teléfono después de haberlos marcado como no válidos.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76495aac-8c2d-4e1a-8cac-12e3856ab1d3 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `sms.invalid_phone_numbers.remove`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| ----------|-----------| ---------|------ |
| `phone_numbers` | Obligatorio | Matriz de cadenas en formato e.164 | Una matriz de hasta 50 números de teléfono para modificar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```

{% endapi %}