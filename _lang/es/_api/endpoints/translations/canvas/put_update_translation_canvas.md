---
nav_title: "PUT: Actualizar traducción en un Canvas"
article_title: "PUT: Actualizar traducción en un Canvas"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Actualizar traducción en un Canvas."
---

{% api %}
# Actualizar traducción en un Canvas {#update-translation-in-a-canvas}
{% apimethod put %}
/canvas/translations
{% endapimethod %}

> Usa este punto de conexión para actualizar múltiples traducciones de un Canvas. Consulta [Configuraciones regionales en los mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para obtener más información sobre las características de localización.

Si deseas actualizar las traducciones después de haber lanzado un Canvas, primero deberás [guardar tu mensaje como borrador]({{site.baseurl}}/post-launch_edits).

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `canvas.translations.update`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de ruta {#path-parameters}

No hay parámetros de ruta para este punto de conexión.

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `workflow_id` | Obligatorio | Cadena | El ID del Canvas. |
| `step_id` | Obligatorio | Cadena | El ID de tu paso en Canvas. |
| `message_variation_id` | Obligatorio | Cadena | El ID de tu variación de mensaje. |
| `locale_id` | Obligatorio | Cadena | El ID (UUID) de la configuración regional. |
| `translation_map` | Obligatorio | Objeto | Objeto que contiene las nuevas traducciones. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la respuesta del punto de conexión GET.
{% endalert %}

## Ejemplo de solicitud {#example-request}

```json
{
    "workflow_id": "a74404b3-3626-4de0-bdec-06935f3aa0ad",
    "step_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
    "message_variation_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_3": "Ein Absatz ohne Formatierung"
    }
}
```

## Respuesta {#response}

Hay cuatro respuestas de código de estado para este punto de conexión: `200`, `400`, `404` y `429`.

### Ejemplo de respuesta correcta {#example-success-response}

```json
{
	"message": "success"
}
```

### Ejemplo de respuesta de error {#example-error-response}

El código de estado `400` podría devolver el siguiente cuerpo de respuesta. Consulta [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puedes encontrar.

```json
{
	"errors": [
		{
			"message": "The provided locale code does not exist."
		}
	]
}
```

{% endapi %}