---
nav_title: "PUT: Reemplazar objeto de datos"
article_title: "PUT: Reemplazar objeto de datos"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Reemplazar objeto de datos."
---
{% api %}
# Reemplazar objeto de datos {#replace-data-object}
{% apimethod put %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Usa este endpoint para crear o reemplazar un objeto de datos con semántica de reemplazo completo de atributos.

{% alert important %}
Los objetos de datos se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos de datos aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `data_objects.update`.

## Límite de velocidad {#rate-limit}

Este endpoint está en el contenedor de escritura de objetos de datos con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta para el endpoint `/data_objects/objects/{type_name}/{external_id}`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | String | Nombre de máquina del tipo de objeto de datos |
| `external_id` | Obligatorio | String | Identificador del objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta para reemplazar objeto de datos" }

## Parámetros de solicitud {#request-parameters}

La siguiente tabla enumera y describe los parámetros del cuerpo de solicitud JSON para el endpoint `/data_objects/objects/{type_name}/{external_id}`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `attributes` | Obligatorio | Objeto | Atributos completos del objeto. Los campos omitidos se eliminan |
| `display_name` | Opcional | String | Etiqueta de visualización del objeto. Cuando el tipo tiene un campo de origen de nombre de visualización, el valor de ese campo tiene prioridad. El valor predeterminado es `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de solicitud para reemplazar objeto de datos" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye una carga útil JSON de ejemplo y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

```json
{
  "attributes": {
    "name": "Updated Account"
  }
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo reemplaza los atributos almacenados en `acct-123` con los de la carga útil. Si no existe ningún registro con ese identificador, esta solicitud lo crea.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "attributes": {
    "name": "Updated Account"
  }
}'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta exitosa y los campos de respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta. Este endpoint devuelve `200` tanto si la solicitud creó como si reemplazó el objeto.

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Updated Account" }
  }
}
```

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos de una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `data_object` | Obligatorio | Objeto | Registro de objeto de datos creado o reemplazado |
| `data_object.type_name` | Obligatorio | String | Nombre de máquina del tipo de objeto de datos |
| `data_object.external_id` | Obligatorio | String | Identificador del objeto de datos |
| `data_object.attributes` | Obligatorio | Objeto | Atributos del objeto almacenados indexados por nombre de campo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta para reemplazar objeto de datos" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | Error de validación | Confirma que cada campo en `attributes` existe en el esquema del tipo y usa el tipo de datos correcto. |
| `404` | Tipo no encontrado (`data-object-type-not-found`) | Confirma que `type_name` existe en el espacio de trabajo y coincide exactamente con el nombre de máquina. |
| `422` | Límite de registros alcanzado (`data-object-record-limit-exceeded`) cuando esta solicitud crearía un nuevo objeto | Reduce la cantidad de objetos del tipo o contacta con soporte de Braze sobre los límites de tu espacio de trabajo. |
| `401` | Clave de API REST or transferencia de estado representacional faltante o no válida | Verifica que el encabezado `Authorization` usa `Bearer YOUR_REST_API_KEY` y que la clave está activa. |
| `403` | La clave de API carece de permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tiene `data_objects.update` y que tu IP de origen está en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de reemplazar objeto de datos" }
{% endapi %}