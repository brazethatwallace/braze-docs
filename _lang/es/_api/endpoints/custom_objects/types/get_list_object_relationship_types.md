---
nav_title: "GET: Listar tipos de relación de objetos"
article_title: "GET: Listar tipos de relación de objetos"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Listar tipos de relación de objetos."
---
{% api %}
# Listar tipos de relación de objetos {#list-object-relationship-types}
{% apimethod get %}
/custom_objects/types/{type_name}/object_relationship_types
{% endapimethod %}

> Usa este endpoint para listar los tipos de relaciones disponibles para vínculos de objeto a objeto en una dirección de anclaje determinada.

{% alert important %}
Los objetos personalizados se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos personalizados aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `custom_objects.read`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de lectura de objetos personalizados con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta del endpoint `/custom_objects/types/{type_name}/object_relationship_types`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta para listar tipos de relación de objetos" }

## Parámetros de consulta {#query-parameters}

La siguiente tabla enumera y describe los parámetros de consulta del endpoint `/custom_objects/types/{type_name}/object_relationship_types`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `anchor` | Opcional | Cadena | `source` (predeterminado) o `target` |
| `limit` | Opcional | Entero | Tamaño de página. Predeterminado `100`. Limitado de `1` a `250` |
| `offset` | Opcional | Entero | Desplazamiento. Predeterminado `0`. Los valores negativos se redondean a `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de consulta para listar tipos de relación de objetos" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye una carga útil de parámetros de ejemplo y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

Usa este objeto JSON como referencia para los parámetros de solicitud.

```json
{
  "type_name": "account",
  "anchor": "source",
  "limit": 10,
  "offset": 0
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo enumera los tipos de relación de objetos disponibles para el tipo `account` cuando `account` es el origen de la relación.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types/account/object_relationship_types?anchor=source&limit=10&offset=0' \
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
      "from_type_name": "account",
      "to_type_name": "account",
      "rel_kind": "subaccount",
      "display_name": "subaccount",
      "related_type_name": "account"
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 10
}
```

`related_type_name` es el tipo en el otro extremo de la relación para el `anchor` seleccionado.

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `items` | Obligatorio | Array | Lista de tipos de relación de objetos disponibles |
| `items[].from_type_name` | Obligatorio | Cadena | Nombre del tipo de objeto personalizado de origen |
| `items[].to_type_name` | Obligatorio | Cadena | Nombre del tipo de objeto personalizado de destino |
| `items[].rel_kind` | Obligatorio | Cadena | Valor del tipo de relación |
| `items[].display_name` | Obligatorio | Cadena | Etiqueta de visualización del tipo de relación |
| `items[].related_type_name` | Obligatorio | Cadena | Tipo del lado opuesto para el `anchor` solicitado |
| `total_count` | Obligatorio | Entero | Número total de registros coincidentes |
| `has_more` | Obligatorio | Booleano | Si hay otra página de resultados disponible |
| `next_offset` | Opcional | Entero | Desplazamiento para la siguiente página cuando `has_more` es `true` |
| `offset` | Obligatorio | Entero | Desplazamiento de la página actual |
| `limit` | Obligatorio | Entero | Tamaño de página utilizado en la solicitud |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta para listar tipos de relación de objetos" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | `anchor` no válido | Usa `source` o `target` para `anchor`. |
| `404` | Tipo no encontrado (`custom-object-type-not-found`) | Confirma que `type_name` existe en el espacio de trabajo y coincide exactamente con el nombre de máquina. |
| `401` | Clave de API REST faltante o no válida | Verifica que el encabezado `Authorization` use `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tiene el permiso `custom_objects.read` y que tu IP de origen está en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de listar tipos de relación de objetos" }
{% endapi %}