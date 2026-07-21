---
nav_title: "PUT: Actualizar traducciones de una plantilla de correo electrónico"
article_title: "PUT: Actualizar traducciones de una plantilla de correo electrónico"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Actualizar traducciones de una plantilla de correo electrónico."
---

{% api %}
# Actualizar traducciones de una plantilla de correo electrónico {#update-translations-for-an-email-template}
{% apimethod put %}
/templates/email/translations/
{% endapimethod %}

> Usa este endpoint para actualizar las traducciones de una [plantilla de correo electrónico]({{site.baseurl}}/user_guide/messaging/templates/email_templates). Consulta [Configuraciones regionales en los mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para obtener más información sobre las características de traducción.

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `templates.translations.update`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de ruta {#path-parameters}

No hay parámetros de ruta para este endpoint.

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `template_id` | Obligatorio | Cadena | El ID de tu plantilla de correo electrónico. |
| `locale_id` | Obligatorio | Cadena | El ID de la configuración regional. |
| `translations_map` | Obligatorio | Cadena | El mapa de las traducciones de tu plantilla de correo electrónico. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la respuesta del endpoint GET.
{% endalert %}

## Ejemplo de solicitud {#example-request}

```json
{
    "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "Me llamo Jacky",
        "id_2": "¿Dónde está la biblioteca?"
    }
}
```

## Respuesta {#response}

Hay cuatro respuestas de código de estado para este endpoint: `200`, `400`, `404` y `429`.

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
			"id": "1234567-abc-123-012345678",
			"message": "The provided translations yielded errors when parsing. Please contact Braze for more information."
		}
	]
}
```

{% endapi %}