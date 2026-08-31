---
nav_title: "POST: Recuperar Banners para un usuario"
article_title: "POST: Recuperar Banners para un usuario"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Usa este endpoint para recuperar los Banners elegibles para un usuario."
hidden: true
---

{% api %}
# Recuperar Banners para un usuario {#retrieve-banners-for-a-user}
{% apimethod post %}
/v1/device-messaging/banners/sync
{% endapimethod %}

> Usa este endpoint para recuperar el Banner elegible para cada ubicación solicitada para un usuario.

La respuesta contiene propiedades estructuradas del Banner que puedes utilizar para crear una interfaz personalizada. No contiene HTML renderizado.

{% alert important %}
Esta página está en fase beta. Las características y la documentación de la API de mensajería de dispositivos están sujetas a cambios. Ponte en contacto con tu director de cuentas de Braze para solicitar acceso.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitas lo siguiente:

- Un espacio de trabajo con Banners habilitados
- Una [clave de API REST del lado del cliente]({{site.baseurl}}/api/device_messaging_api/authentication) con el permiso `banners.sync`
- El [endpoint REST]({{site.baseurl}}/api/basics#endpoints) de tu instancia de Braze

Incluye la clave de API REST del lado del cliente en el encabezado `Authorization` como un token bearer.

## Límite de velocidad {#rate-limit}

Los límites de velocidad se aplican por espacio de trabajo. Si superas el límite de velocidad, Braze devuelve un código de estado `429`. Cuando estén disponibles, utiliza los encabezados de respuesta `X-RateLimit-Limit`, `X-RateLimit-Remaining` y `X-RateLimit-Reset` para monitorear tu uso.

Para más información, consulta [Límites de velocidad de la API de mensajería de dispositivos]({{site.baseurl}}/api/device_messaging_api/rate_limits).

## Cuerpo de la solicitud {#request-body}

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción | Ejemplo |
|---|---|---|---|---|
| `external_user_id` | Obligatorio | Cadena | El ID externo del usuario. | `user_abc123` |
| `app_id` | Obligatorio | Cadena | El [identificador de API de la aplicación]({{site.baseurl}}/api/identifier_types#app-identifier). Debe identificar una aplicación en el espacio de trabajo autenticado. | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | Obligatorio | Cadena | La versión de la aplicación anfitriona. No debe superar los 255 caracteres. | `1.0.0` |
| `placements` | Obligatorio | Matriz de cadenas | Uno o más ID de ubicación para los que recuperar Banners. Incluye al menos un ID de ubicación. | `["home_hero", "sidebar_promo"]` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}

Sustituye *`YOUR_REST_API_URL`* por el [endpoint REST]({{site.baseurl}}/api/basics#endpoints) de tu instancia de Braze.

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/sync' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}'
```

## Parámetros de respuesta {#response-parameters}

| Parámetro | Tipo de datos | Descripción |
|---|---|---|
| `banners` | Objeto | Un mapa de cada ID de ubicación solicitado a su Banner resuelto. El valor es `null` cuando ningún Banner es elegible para una ubicación. |
| `banners.{placement_id}.id` | Cadena | El identificador único del Banner. Usa este valor para reportar eventos de impresión y clic. |
| `banners.{placement_id}.placement_id` | Cadena | El ID de ubicación asociado al Banner. |
| `banners.{placement_id}.is_control` | Booleano | Si el Banner es una variante del grupo de control. |
| `banners.{placement_id}.is_test_send` | Booleano | Si el Banner proviene de un envío de prueba. El valor predeterminado es `false`. |
| `banners.{placement_id}.expires_at` | Entero | La marca de tiempo unix, en segundos, después de la cual no deberías mostrar el Banner. Un valor de `-1` significa que el Banner no expira. |
| `banners.{placement_id}.properties` | Objeto o null | Propiedades definidas por el especialista en marketing para el Banner. Cada propiedad contiene un `type` y un `value`. |
| `banners.{placement_id}.properties.{property}.type` | Cadena | El tipo de la propiedad. Los valores posibles son `number`, `string`, `boolean`, `image`, `jsonobject` y `datetime`. |
| `banners.{placement_id}.properties.{property}.value` | Número, cadena, booleano u objeto | El valor de la propiedad. Su tipo JSON corresponde a `type`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parámetros de respuesta" }

## Ejemplo de respuesta {#example-response}

Una solicitud exitosa devuelve un código de estado `200` y el Banner resuelto para cada ubicación solicitada.

```json
{
  "banners": {
    "home_hero": {
      "id": "this_banner_is_a_stub_01",
      "placement_id": "home_hero",
      "is_control": false,
      "is_test_send": false,
      "expires_at": 1735689600,
      "properties": {
        "headline": {
          "type": "string",
          "value": "Level Up Your Game"
        },
        "cta_label": {
          "type": "string",
          "value": "Shop Now"
        }
      }
    },
    "sidebar_promo": null
  }
}
```

## Códigos de estado {#status-codes}

| Código de estado | Descripción |
|---|---|
| `200` | Braze resolvió los datos del Banner para cada ubicación solicitada. |
| `400` | La solicitud contiene parámetros faltantes o no válidos. |
| `401` | La clave de API REST del lado del cliente falta, no es válida o no tiene el permiso `banners.sync`. |
| `404` | El endpoint no está disponible. Esta respuesta no distingue entre una clave de API faltante o no válida y una característica de Banners deshabilitada. |
| `429` | El espacio de trabajo superó su límite de velocidad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Códigos de estado" }

Para más información, consulta [Manejo de errores y reintentos de la API de mensajería de dispositivos]({{site.baseurl}}/api/device_messaging_api/error_handling).

{% endapi %}