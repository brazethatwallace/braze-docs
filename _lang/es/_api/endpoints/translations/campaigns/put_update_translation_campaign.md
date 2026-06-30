---
nav_title: "PUT: Actualizar traducción en una campaña"
article_title: "PUT: Actualizar traducción en una campaña"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Actualizar traducción en una campaña."
---

{% api %}
# Actualizar traducción en una campaña {#update-translation-in-a-campaign}
{% apimethod put %}
/campaigns/translations
{% endapimethod %}

> Usa este punto de conexión para actualizar múltiples traducciones de una campaña. Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para obtener más información sobre las características de localización.

Si deseas actualizar las traducciones después de que se haya lanzado una campaña, primero deberás [guardar tu mensaje como borrador]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/change_your_campaign_after_launch).

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `campaigns.translations.update`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de ruta {#path-parameters}

No hay parámetros de ruta para este punto de conexión.

## Parámetros de solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obligatorio | Cadena | El ID de tu campaña. |
| `message_variation_id` | Obligatorio | Cadena | El ID de tu variación de mensaje. |
| `locale_id` | Obligatorio | Cadena | El ID (UUID) de la configuración regional. |
| `translation_map` | Obligatorio | Objeto | Objeto que contiene las nuevas traducciones. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de solicitud" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la respuesta del punto de conexión GET.
{% endalert %}

## Ejemplo de solicitud {#example-request}

```json
{
    "campaign_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "message_variation_id": "f14404b3-3626-4de0-bdec-06935f3aa0ad",
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