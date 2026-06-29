---
nav_title: "POST: Añadir correos electrónicos a la lista negra"
article_title: "POST: Añadir correos electrónicos a la lista negra"
search_tag: Endpoint
page_order: 10
layout: api_page
page_type: reference
alias: /blacklist/
description: "En este artículo se describen los detalles del punto de conexión de Braze para añadir correos electrónicos a la lista negra."

---
{% api %}
# Añadir correos electrónicos a la lista negra {#blacklist-emails}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/email/blacklist
{% endapimethod %}

{% alert important %}
Braze ha lanzado el [punto de conexión `/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist) con la misma funcionalidad que el punto de conexión `/email/blacklist`. Te recomendamos que utilices el punto de conexión `/email/blocklist` en su lugar.
{% endalert %}

> Utiliza este punto de conexión para cancelar la suscripción de un usuario del correo electrónico y marcarlo como rebote duro.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `email.blacklist`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blacklist_email1","blacklist_email2"]
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| -----------|----------| --------|------- |
| `email` | Obligatorio | Cadena o matriz | Cadena de dirección de correo electrónico para añadir a la lista negra, o una matriz de hasta 50 direcciones de correo electrónico para añadir a la lista negra. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blacklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blacklist_email1","blacklist_email2"]
}'
```

{% endapi %}