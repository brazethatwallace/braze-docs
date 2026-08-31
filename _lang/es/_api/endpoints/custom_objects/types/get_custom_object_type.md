---
nav_title: "GET: Obtener tipo de objeto personalizado"
article_title: "GET: Obtener tipo de objeto personalizado"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Obtener tipo de objeto personalizado."
---
{% api %}
# Obtener tipo de objeto personalizado {#get-custom-object-type}
{% apimethod get %}
/custom_objects/types/{type_name}
{% endapimethod %}

> Utiliza este endpoint para devolver un tipo de objeto personalizado y su definición de esquema.

{% alert important %}
Los objetos personalizados se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos personalizados aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `custom_objects.read`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de lectura de objetos personalizados con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta del endpoint `/custom_objects/types/{type_name}`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta de obtener tipo de objeto personalizado" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye una carga útil de ejemplo de parámetro de ruta y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

Utiliza este objeto JSON como referencia para el parámetro de ruta en esta solicitud.

```json
{
  "type_name": "account"
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo recupera la definición del tipo de objeto personalizado `account`.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta exitosa y los campos de respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "custom_object_type": {
    "type_name": "account",
    "metadata": { "display_name_source": "name" },
    "schema_def": {
      "type": "object",
      "properties": {
        "name": { "type": "string", "title": "Name" },
        "industry": { "type": "string", "title": "Industry" },
        "renewal_date": { "type": "string", "format": "date-time", "title": "Renewal date" }
      },
      "required": ["name"]
    }
  }
}
```

`schema_def` describe los campos de objeto permitidos. Las escrituras siguen rechazando campos no declarados aunque este esquema de respuesta sea descriptivo.

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `custom_object_type` | Obligatorio | Objeto | Registro del tipo de objeto personalizado devuelto |
| `custom_object_type.type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
| `custom_object_type.metadata` | Obligatorio | Objeto | Objeto de metadatos del tipo |
| `custom_object_type.schema_def` | Obligatorio | Objeto | Definición del esquema JSON para los atributos del objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta de obtener tipo de objeto personalizado" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `404` | Tipo no encontrado (`custom-object-type-not-found`) | Confirma que `type_name` existe en el espacio de trabajo y coincide exactamente con el nombre de máquina. |
| `401` | Clave de API REST ausente o no válida | Verifica que el encabezado `Authorization` utilice `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tiene el permiso `custom_objects.read` y que tu IP de origen está en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de obtener tipo de objeto personalizado" }
{% endapi %}