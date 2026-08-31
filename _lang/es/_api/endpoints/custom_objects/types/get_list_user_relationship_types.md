---
nav_title: "GET: Listar tipos de relación de usuario"
article_title: "GET: Listar tipos de relación de usuario"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Listar tipos de relación de usuario."
---
{% api %}
# Listar tipos de relación de usuario {#list-user-relationship-types}
{% apimethod get %}
/custom_objects/types/{type_name}/user_relationship_types
{% endapimethod %}

> Utiliza este endpoint para listar los valores válidos de `rel_kind` para las relaciones de usuario en un tipo de objeto personalizado.

{% alert important %}
Los objetos personalizados se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos personalizados aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `custom_objects.read`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de lectura de objetos personalizados con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta del endpoint `/custom_objects/types/{type_name}/user_relationship_types`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta para listar tipos de relación de usuario" }

## Parámetros de consulta {#query-parameters}

La siguiente tabla enumera y describe los parámetros de consulta del endpoint `/custom_objects/types/{type_name}/user_relationship_types`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `limit` | Opcional | Entero | Tamaño de página. Predeterminado `100`. Se limita de `1` a `250` |
| `offset` | Opcional | Entero | Desplazamiento. Predeterminado `0`. Los valores negativos se redondean a `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de consulta para listar tipos de relación de usuario" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye una carga útil de parámetros de ejemplo y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

Utiliza este objeto JSON como referencia para los parámetros de solicitud.

```json
{
  "type_name": "account",
  "limit": 100,
  "offset": 0
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo enumera los tipos de relación de usuario que puedes utilizar para vincular usuarios a registros de `account`.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types/account/user_relationship_types?limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta correcta y los campos de la respuesta.

### Ejemplo de respuesta correcta {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "items": [
    { "rel_kind": "account_user", "display_name": "account_user" }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`display_name` actualmente coincide con `rel_kind`.

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos de una respuesta correcta.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `items` | Obligatorio | Matriz | Lista de tipos de relación de usuario disponibles |
| `items[].rel_kind` | Obligatorio | Cadena | Valor del tipo de relación de usuario |
| `items[].display_name` | Obligatorio | Cadena | Etiqueta de visualización del tipo de relación |
| `total_count` | Obligatorio | Entero | Número total de registros que coinciden |
| `has_more` | Obligatorio | Booleano | Si hay otra página de resultados disponible |
| `next_offset` | Opcional | Entero | Desplazamiento para la siguiente página cuando `has_more` es `true` |
| `offset` | Obligatorio | Entero | Desplazamiento de la página actual |
| `limit` | Obligatorio | Entero | Tamaño de página utilizado por la solicitud |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta para listar tipos de relación de usuario" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `404` | Tipo no encontrado (`custom-object-type-not-found`) | Confirma que `type_name` existe en el espacio de trabajo y coincide exactamente con el nombre de máquina. |
| `401` | Clave de API REST faltante o no válida | Verifica que el encabezado `Authorization` utilice `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tiene el permiso `custom_objects.read` y que tu IP de origen está en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de listar tipos de relación de usuario" }
{% endapi %}