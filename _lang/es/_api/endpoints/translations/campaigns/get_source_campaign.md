---
nav_title: "GET: Ver los valores de fuente predeterminados para las etiquetas de traducción de Campaign"
article_title: "GET: Ver los valores de fuente predeterminados para las etiquetas de traducción de Campaign"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el punto de conexión de fuente de traducción de Campaign."
---

{% api %}
# Ver los valores de fuente predeterminados para las etiquetas de traducción de una Campaign {#view-default-source-values-for-a-campaigns-translation-tags}
{% apimethod get %}
/campaigns/translations/source
{% endapimethod %}

> Usa este punto de conexión para ver todas las fuentes de traducción predeterminadas para las etiquetas de traducción de una Campaign. Estos son los valores dentro de {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) para obtener más información sobre las características de traducción.

## Requisitos previos {#prerequisites}

Para usar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `campaigns.translations.get`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta {#query-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obligatorio | Cadena | El ID de tu Campaign. |
| `message_variation_id` | Obligatorio | Cadena | El ID de tu variación de mensaje. |
| `locale_id` | Opcional | Cadena | Un UUID de locale para filtrar las respuestas. |
| `post_launch_draft_version` | Opcional | Booleano | Cuando es `true`, devuelve la última versión de borrador en lugar de la última versión publicada en vivo. El valor predeterminado es `false`, que devuelve la última versión en vivo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Query parameters" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la respuesta del punto de conexión GET.
{% endalert %}

## Ejemplo de solicitud {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/source?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

Hay cuatro respuestas de código de estado para este punto de conexión: `200`, `400`, `404` y `429`.

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