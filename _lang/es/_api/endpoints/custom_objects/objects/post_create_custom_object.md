---
nav_title: "POST: Crear objeto personalizado"
article_title: "POST: Crear objeto personalizado"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Crear objeto personalizado."
---
{% api %}
# Crear objeto personalizado {#create-custom-object}
{% apimethod post %}
/custom_objects/objects/{type_name}
{% endapimethod %}

> Utiliza este endpoint para crear un objeto personalizado para un tipo.

{% alert important %}
Los objetos personalizados se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos personalizados aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `custom_objects.create`.

## Límite de velocidad {#rate-limit}

Este endpoint está en el contenedor de escritura de objetos personalizados con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta para el endpoint `/custom_objects/objects/{type_name}`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta para crear objeto personalizado" }

## Parámetros de la solicitud {#request-parameters}

La siguiente tabla enumera y describe los parámetros del cuerpo de la solicitud JSON para el endpoint `/custom_objects/objects/{type_name}`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `external_id` | Obligatorio | Cadena | Identificador del objeto, único dentro del tipo |
| `attributes` | Obligatorio | Objeto | Valores con clave de nombre de campo validados contra el esquema del tipo |
| `display_name` | Opcional | Cadena | Etiqueta de visualización del objeto. Cuando el tipo tiene un campo de origen de nombre para mostrar, el valor de ese campo tiene prioridad. El valor predeterminado es `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de solicitud para crear objeto personalizado" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye una carga útil JSON de ejemplo y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

```json
{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo crea un registro `account` con el identificador `acct-new` y establece sus atributos `name` e `industry`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta exitosa y los campos de la respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `201` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-new",
    "attributes": { "name": "New Account", "industry": "software" }
  }
}
```

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `custom_object` | Obligatorio | Objeto | Registro de objeto personalizado creado |
| `custom_object.type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
| `custom_object.external_id` | Obligatorio | Cadena | Identificador del objeto personalizado |
| `custom_object.attributes` | Obligatorio | Objeto | Atributos del objeto almacenados con clave de nombre de campo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta para crear objeto personalizado" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes para este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | Campo de atributo desconocido o tipo de atributo no válido | Confirma que cada campo en `attributes` existe en el esquema del tipo y utiliza el tipo de datos correcto. |
| `404` | Tipo no encontrado (`custom-object-type-not-found`) | Confirma que `type_name` existe en el espacio de trabajo y coincide exactamente con el nombre de máquina. |
| `409` | Objeto duplicado (`duplicate-custom-object`) | Usa un `external_id` diferente, o usa `PUT` para reemplazar el objeto existente. |
| `422` | Límite de registros alcanzado (`custom-object-record-limit-exceeded`) | Reduce la cantidad de objetos para el tipo, o contacta con soporte de Braze acerca de los límites de tu espacio de trabajo. |
| `401` | Clave de API REST faltante o no válida | Verifica que el encabezado `Authorization` use `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API carece de permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tiene el permiso `custom_objects.create` y que tu IP de origen está en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de crear objeto personalizado" }
{% endapi %}