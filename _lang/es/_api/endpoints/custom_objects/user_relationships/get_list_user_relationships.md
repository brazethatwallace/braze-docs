---
nav_title: "GET: Listar relaciones de usuario"
article_title: "GET: Listar relaciones de usuario"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Listar relaciones de usuario."
---
{% api %}
# Listar relaciones de usuario {#list-user-relationships}
{% apimethod get %}
/custom_objects/objects/{type_name}/{external_id}/user_relationships
{% endapimethod %}

> Utiliza este endpoint para listar los usuarios vinculados a un objeto personalizado.

{% alert important %}
Los objetos personalizados se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos personalizados aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `custom_objects.user_relationships.read`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de lectura de objetos personalizados con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta del endpoint `/custom_objects/objects/{type_name}/{external_id}/user_relationships`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Tipo de objeto |
| `external_id` | Obligatorio | Cadena | Identificador del objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta para listar relaciones de usuario" }

## Parámetros de consulta {#query-parameters}

La siguiente tabla enumera y describe los parámetros de consulta del endpoint `/custom_objects/objects/{type_name}/{external_id}/user_relationships`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `rel_kind` | Opcional | Cadena | Filtrar por tipo de relación |
| `limit` | Opcional | Entero | Tamaño de página. Predeterminado `100`. Limitado de `1` a `250` |
| `offset` | Opcional | Entero | Desplazamiento. Predeterminado `0`. Los valores negativos se redondean a `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de consulta para listar relaciones de usuario" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye una carga útil de parámetros de ejemplo y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

Utiliza este objeto JSON como referencia para los parámetros de solicitud.

```json
{
  "type_name": "account",
  "external_id": "acct-123",
  "rel_kind": "account_user",
  "limit": 100,
  "offset": 0
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo lista los usuarios vinculados a `acct-123` a través de la relación `account_user`.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/user_relationships?rel_kind=account_user&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta exitosa y los campos de respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "items": [
    {
      "type_name": "account",
      "external_id": "acct-123",
      "rel_kind": "account_user",
      "user": { "braze_id": "507f1f77bcf86cd799439011" },
      "attributes": { "role": "admin" }
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

La carga útil de `user` contiene solo `braze_id`.

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `items` | Obligatorio | Array | Lista de registros de relaciones de usuario |
| `items[].type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
| `items[].external_id` | Obligatorio | Cadena | Identificador del objeto personalizado |
| `items[].rel_kind` | Obligatorio | Cadena | Valor del tipo de relación |
| `items[].user` | Obligatorio | Objeto | Objeto de usuario vinculado |
| `items[].user.braze_id` | Obligatorio | Cadena | Identificador de usuario de Braze |
| `items[].attributes` | Obligatorio | Objeto | Atributos de la relación |
| `total_count` | Obligatorio | Entero | Número total de registros coincidentes |
| `has_more` | Obligatorio | Booleano | Si hay otra página de resultados disponible |
| `next_offset` | Opcional | Entero | Desplazamiento para la siguiente página cuando `has_more` es `true` |
| `offset` | Obligatorio | Entero | Desplazamiento de la página actual |
| `limit` | Obligatorio | Entero | Tamaño de página utilizado por la solicitud |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta para listar relaciones de usuario" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `404` | Tipo u objeto no encontrado | Confirma que tanto `type_name` como `external_id` existan en el espacio de trabajo. |
| `401` | Clave de API REST faltante o no válida | Verifica que el encabezado `Authorization` utilice `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene el permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tenga el permiso `custom_objects.user_relationships.read` y que tu IP de origen esté en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Vuelve a intentarlo después de `X-RateLimit-Reset` y reduce la frecuencia de las solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de listar relaciones de usuario" }
{% endapi %}