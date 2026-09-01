---
nav_title: "GET: Obtener objeto personalizado"
article_title: "GET: Obtener objeto personalizado"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Obtener objeto personalizado."
---
{% api %}
# Obtener objeto personalizado {#get-custom-object}
{% apimethod get %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Utiliza este endpoint para devolver un objeto personalizado.

{% alert important %}
Los objetos personalizados se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos personalizados aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `custom_objects.read`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de lectura de objetos personalizados con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta del endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
| `external_id` | Obligatorio | Cadena | Identificador del objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta de obtener objeto personalizado" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye una carga útil de ejemplo con parámetros de ruta y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

Utiliza este objeto JSON como referencia para los parámetros de ruta en esta solicitud.

```json
{
  "type_name": "account",
  "external_id": "acct-123"
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo recupera el registro de cuenta `acct-123` y sus atributos almacenados.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta exitosa y los campos de la respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "industry": "software" }
  }
}
```

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos de una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `custom_object` | Obligatorio | Objeto | Registro de objeto personalizado devuelto |
| `custom_object.type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
| `custom_object.external_id` | Obligatorio | Cadena | Identificador del objeto personalizado |
| `custom_object.attributes` | Obligatorio | Objeto | Atributos del objeto indexados por nombre de campo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta de obtener objeto personalizado" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `404` | Tipo no encontrado (`custom-object-type-not-found`) u objeto no encontrado (`custom-object-not-found`) | Confirma que tanto `type_name` como `external_id` existen en el espacio de trabajo. |
| `401` | Clave de API REST ausente o no válida | Verifica que el encabezado `Authorization` utilice `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API carece de permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tiene el permiso `custom_objects.read` y que tu IP de origen está en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de obtener objeto personalizado" }
{% endapi %}