---
nav_title: "PUT: Actualizar traducción en un bloque de contenido"
article_title: "PUT: Actualizar traducción en un bloque de contenido"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el punto de conexión Actualizar traducción en un bloque de contenido."
---

{% api %}
# Actualizar traducción en un bloque de contenido {#update-translation-in-a-content-block}
{% apimethod put %}
/content_blocks/translations
{% endapimethod %}

> Utiliza este punto de conexión para actualizar múltiples traducciones de un [bloque de contenido]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para obtener más información sobre las características de traducción.

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `content_blocks.translations.update`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de ruta {#path-parameters}

No hay parámetros de ruta para este punto de conexión.

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | Obligatorio | Cadena | El ID de tu bloque de contenido. |
| `locale_id` | Obligatorio | Cadena | El ID (UUID) de la configuración regional. |
| `translation_map` | Obligatorio | Objeto | Objeto que contiene las nuevas traducciones. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de solicitud" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la respuesta del punto de conexión GET.
{% endalert %}

## Ejemplo de solicitud {#example-request}

```json
{
    "content_block_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
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