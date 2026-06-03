---
nav_title: "GET: Ver traducciones de origen de una plantilla de correo electrónico"
article_title: "GET: Ver traducciones de origen de una plantilla de correo electrónico"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el punto de conexión Ver traducciones de origen de una plantilla de correo electrónico."
---

{% api %}
# Ver las traducciones de origen de una plantilla de correo electrónico {#view-the-source-translations-for-an-email-template}
{% apimethod get %}
/templates/email/translations/source
{% endapimethod %}

> Usa este punto de conexión para ver las traducciones de origen de una [plantilla de correo electrónico]({{site.baseurl}}/user_guide/messaging/templates/email_templates/). Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) para obtener más información sobre las características de traducción.

## Requisitos previos {#prerequisites}

Para usar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `templates.email.info`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta {#query-parameters}

| Parámetro     | Obligatorio | Tipo de datos | Descripción                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Obligatorio | Cadena    | El ID de tu plantilla de correo electrónico. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Query parameters" }

## Ejemplo de solicitud {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/source?template_id={template_id}'
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
---template_id: "6ad1507f-ca10-44c4-95bf-aj39fm10fm1ps"
```

## Respuesta {#response}

Hay cuatro respuestas de código de estado para este punto de conexión: `200`, `400`, `404` y `429`.

### Ejemplo de respuesta correcta {#example-success-response}

El código de estado `200` podría devolver el siguiente encabezado y cuerpo de respuesta.

```json
{
    "translations": {
        "translation_map": {
            "id_0": "Here's a limited time offer for your membership tier!",
            "id_1": "Welcome to a new fashion-forward season!"
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
            "message": "The provided locale code does not exist."
        }
    ]
}
```

{% endapi %}