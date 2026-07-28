---
nav_title: "POST: Eliminar los correos electrónicos de rebote duro"
article_title: "POST: Eliminar correos electrónicos de rebote duro"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Eliminar direcciones de correo electrónico de rebote duro de Braze."

---
{% api %}
# Eliminar los correos electrónicos de rebote duro {#remove-hard-bounced-emails}
{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

> Utiliza este endpoint para eliminar direcciones de correo electrónico de tu lista de rebotes de Braze y de la lista de rebotes mantenida por tu proveedor de correo electrónico.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `email.bounce.remove`.

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
| ----------|-----------| ---------|------ |
| `email` | Obligatorio | Cadena o matriz | Dirección de correo electrónico en forma de cadena a modificar, o una matriz de hasta 50 direcciones de correo electrónico a modificar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/bounce/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@example.com"
}'
```

{% endapi %}