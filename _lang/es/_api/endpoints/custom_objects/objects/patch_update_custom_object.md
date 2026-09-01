---
nav_title: "PATCH: Actualizar objeto personalizado"
article_title: "PATCH: Actualizar objeto personalizado"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Actualizar objeto personalizado."
---
{% api %}
# Actualizar objeto personalizado {#update-custom-object}
{% apimethod patch %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Usa este endpoint para fusionar atributos en un objeto personalizado existente.

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta de actualizar objeto personalizado" }

## Parámetros de solicitud {#request-parameters}

La siguiente tabla enumera y describe los parámetros del cuerpo de solicitud JSON del endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `attributes` | Obligatorio | Objeto | Campos de nivel superior para fusionar |
| `display_name` | Opcional | Cadena | Etiqueta de visualización del objeto. Cuando el tipo tiene un campo de origen de nombre de visualización, el valor de ese campo tiene prioridad. Cuando se omite, se conserva el nombre de visualización existente |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de solicitud de actualizar objeto personalizado" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye un ejemplo de carga útil JSON y un ejemplo de solicitud cURL.

### Ejemplo de carga útil de solicitud {#sample-request-payload}

```json
{
  "attributes": {
    "credits": 750
  }
}
```

### Ejemplo de solicitud cURL {#sample-curl-request}

Este ejemplo actualiza el atributo `credits` en `acct-123` y deja sin cambios los demás atributos del registro.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{ "attributes": { "credits": 750 } }'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta exitosa y los campos de la respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta. El objeto `attributes` refleja el resultado de la fusión.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "credits": 750 }
  }
}
```

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `custom_object` | Obligatorio | Objeto | Registro del objeto personalizado actualizado |
| `custom_object.type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
| `custom_object.external_id` | Obligatorio | Cadena | Identificador del objeto personalizado |
| `custom_object.attributes` | Obligatorio | Objeto | Atributos del objeto después de la fusión |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta de actualizar objeto personalizado" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | Error de validación | Confirma que cada campo en `attributes` existe en el esquema del tipo y utiliza el tipo de datos correcto. |
| `404` | Tipo no encontrado u objeto no encontrado | Confirma que tanto `type_name` como `external_id` existen en el espacio de trabajo. |
| `401` | Clave de API REST faltante o no válida | Verifica que el encabezado `Authorization` utilice `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tiene el permiso `custom_objects.update` y que tu IP de origen está en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de actualizar objeto personalizado" }
{% endapi %}