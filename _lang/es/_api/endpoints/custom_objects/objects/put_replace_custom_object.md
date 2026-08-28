---
nav_title: "PUT: Reemplazar objeto personalizado"
article_title: "PUT: Reemplazar objeto personalizado"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Reemplazar objeto personalizado."
---
{% api %}
# Reemplazar objeto personalizado {#replace-custom-object}
{% apimethod put %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Utiliza este endpoint para crear o reemplazar un objeto personalizado con semántica de reemplazo completo de atributos.

{% alert important %}
Los objetos personalizados se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos personalizados aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `custom_objects.update`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de escritura de objetos personalizados con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta del endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
| `external_id` | Obligatorio | Cadena | Identificador del objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta para reemplazar objeto personalizado" }

## Parámetros de solicitud {#request-parameters}

La siguiente tabla enumera y describe los parámetros del cuerpo de solicitud JSON del endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `attributes` | Obligatorio | Objeto | Atributos completos del objeto. Los campos omitidos se eliminan |
| `display_name` | Opcional | Cadena | Etiqueta de visualización del objeto. Cuando el tipo tiene un campo de origen para el nombre de visualización, el valor de ese campo tiene prioridad. El valor predeterminado es `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de solicitud para reemplazar objeto personalizado" }

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
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "attributes": {
    "name": "Updated Account"
  }
}'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta exitosa y los campos de la respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta. Este endpoint devuelve `200` tanto si la solicitud creó como si reemplazó el objeto.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Updated Account" }
  }
}
```

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `custom_object` | Obligatorio | Objeto | Registro de objeto personalizado creado o reemplazado |
| `custom_object.type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
| `custom_object.external_id` | Obligatorio | Cadena | Identificador del objeto personalizado |
| `custom_object.attributes` | Obligatorio | Objeto | Atributos del objeto almacenados, indexados por nombre de campo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta para reemplazar objeto personalizado" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | Error de validación | Confirma que cada campo en `attributes` existe en el esquema del tipo y utiliza el tipo de datos correcto. |
| `404` | Tipo no encontrado (`custom-object-type-not-found`) | Confirma que `type_name` existe en el espacio de trabajo y coincide exactamente con el nombre de máquina. |
| `422` | Límite de registros alcanzado (`custom-object-record-limit-exceeded`) cuando esta solicitud crearía un nuevo objeto | Reduce la cantidad de objetos del tipo o contacta con soporte de Braze para consultar los límites de tu espacio de trabajo. |
| `401` | Clave de API REST ausente o no válida | Verifica que el encabezado `Authorization` utilice `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tiene `custom_objects.update` y que tu IP de origen está en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Vuelve a intentar después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de reemplazar objeto personalizado" }
{% endapi %}