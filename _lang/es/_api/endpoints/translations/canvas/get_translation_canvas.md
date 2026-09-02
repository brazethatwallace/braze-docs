---
nav_title: "GET: Ver la traducción de un Canvas"
article_title: "GET: Ver la traducción de un Canvas"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Ver la traducción de un Canvas."
---

{% api %}
# Ver la traducción de un Canvas {#view-translation-for-a-canvas}
{% apimethod get %}
/canvas/translations
{% endapimethod %}

> Utiliza este endpoint para obtener una vista previa de un mensaje traducido para un Canvas. Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para obtener más información sobre las características de traducción.

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `canvas.translations.get`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta {#query-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|------------------------|----------|-----------|------------------------------------|
| `workflow_id` | Obligatorio | Cadena | El ID del Canvas. |
| `step_id` | Obligatorio | Cadena | El ID de tu paso en Canvas. |
| `message_variation_id` | Obligatorio | Cadena | El ID de tu variación de mensaje. |
| `locale_id` | Opcional | Cadena | El ID (UUID) de la configuración regional. |
| `post_launch_draft_version` | Opcional | Booleano | Cuando es `true`, devuelve la última versión de borrador en lugar de la última versión publicada en vivo. El valor predeterminado es `false`, que devuelve la última versión en vivo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de consulta" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la respuesta del endpoint GET.
{% endalert %}

## Ejemplo de solicitud {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

Hay cuatro respuestas de código de estado para este endpoint: `200`, `400`, `404` y `429`.

### Ejemplo de respuesta correcta {#example-success-response}

El código de estado `200` podría devolver el siguiente encabezado y cuerpo de respuesta.

```json
{
    "translations": [
        {
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            },
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            }
        }
    ]
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