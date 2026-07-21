---
nav_title: "GET: Ver valores fuente predeterminados para etiquetas de traducción de bloques de contenido"
article_title: "GET: Ver valores fuente predeterminados para etiquetas de traducción de bloques de contenido"
search_tag: Endpoint
page_order: 0

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el endpoint de fuente de traducción de bloques de contenido."
---

{% api %}
# Ver valores fuente predeterminados para las etiquetas de traducción de un bloque de contenido {#view-default-source-values-for-a-content-blocks-translation-tags}
{% apimethod get %}
/content_blocks/translations/source
{% endapimethod %}

> Usa este endpoint para ver todas las fuentes de traducción predeterminadas de las etiquetas de traducción de un bloque de contenido. Estos son los valores dentro de {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Consulta [Locales en mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para obtener más información sobre las características de traducción.

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `content_blocks.translations.get`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta {#query-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | Obligatorio | Cadena | El ID de tu bloque de contenido. |
| `locale_id` | Opcional | Cadena | Un UUID de configuración regional para filtrar las respuestas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de consulta" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la respuesta del endpoint GET.
{% endalert %}

## Ejemplo de solicitud {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/content_blocks/translations/source?content_block_id={content_block_id}&locale_id={locale_uuid}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

Hay cuatro códigos de estado de respuesta para este endpoint: `200`, `400`, `404` y `429`.

### Ejemplo de respuesta correcta {#example-success-response}

El código de estado `200` podría devolver el siguiente encabezado y cuerpo de respuesta.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Welcome!",
           "id_1": "Thank you for joining our program"
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