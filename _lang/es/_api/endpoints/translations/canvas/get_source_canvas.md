---
nav_title: "GET: Ver los valores de origen predeterminados de las etiquetas de traducción de Canvas"
article_title: "GET: Ver los valores de origen predeterminados de las etiquetas de traducción de Canvas"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el endpoint de origen de traducción de Canvas."
---

{% api %}
# Ver los valores de origen predeterminados de las etiquetas de traducción de un Canvas {#view-default-source-values-for-a-canvass-translation-tags}
{% apimethod get %}
/canvas/translations/source
{% endapimethod %}

> Utiliza este endpoint para ver todas las fuentes de traducción predeterminadas para las etiquetas de traducción de un Canvas. Estos son los valores con el {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para obtener más información sobre las características de traducción.

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `canvas.translations.get`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta {#query-parameters}

| Parámetro              | Obligatorio | Tipo de datos | Descripción                        |
|------------------------|----------|-----------|------------------------------------|
| `workflow_id`          | Obligatorio | Cadena    | El ID del Canvas.              |
| `step_id`              | Obligatorio | Cadena    | El ID de tu paso en Canvas.        |
| `message_variation_id` | Obligatorio | Cadena | El ID de tu variación de mensaje. |
| `locale_id`            | Opcional | Cadena    | El ID (UUID) de la configuración regional.              |
| `post_launch_draft_version` | Opcional | Booleano | Cuando es `true`, devuelve la última versión de borrador en lugar de la última versión publicada en vivo. El valor predeterminado es `false`, que devuelve la última versión en vivo.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de consulta" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la respuesta del endpoint GET.
{% endalert %}

## Ejemplo de solicitud {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/source?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

Hay cuatro respuestas de código de estado para este endpoint: `200`, `400`, `404` y `429`.

### Ejemplo de respuesta correcta {#example-success-response}

El código de estado `200` podría devolver el siguiente encabezado y cuerpo de respuesta.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Here's a Million Dollars",
           "id_1": "Hello World!"
       }
   },
   "message": "success"
}
```

### Ejemplo de respuesta de error {#example-error-response}

El código de estado `400` podría devolver el siguiente cuerpo de respuesta. Consulta [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puedes encontrar.

```json
{
	"errors": [
		{
			"message": "This message does not support multi-language."
		}
	]
}
```

{% endapi %}