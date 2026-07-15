---
nav_title: "GET: Ver la traducción y la configuración regional específicas para la plantilla de correo electrónico"
article_title: "GET: Ver traducción específica y configuración regional para la plantilla de correo electrónico"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el punto de conexión para ver la traducción y la configuración regional específicas de una plantilla de correo electrónico."
---

{% api %}
# Ver una traducción y configuración regional específicas para el punto de conexión de plantilla de correo electrónico {#view-a-specific-translation-and-locale-for-email-template-endpoint}
{% apimethod get %}
/templates/translations/email
{% endapimethod %}

> Utiliza este punto de conexión para ver una traducción y una configuración regional específicas para una [plantilla de correo electrónico]({{site.baseurl}}/user_guide/messaging/templates/email_templates). Consulta [Configuraciones regionales en los mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para obtener más información sobre las características de traducción.

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `templates.translations.get`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta {#query-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Obligatorio | Cadena | El ID de tu plantilla de correo electrónico. |
| `locale_id` | Opcional | Cadena | El ID (UUID) de la configuración regional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de consulta" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la respuesta del punto de conexión GET.
{% endalert %}

## Ejemplo de solicitud {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/translations/email?locale_id={locale_uuid}&template_id={template_id}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

Hay cuatro respuestas de código de estado para este punto de conexión: `200`, `400`, `404` y `429`.

### Ejemplo de respuesta correcta {#example-success-response}

El código de estado `200` podría devolver el siguiente encabezado y cuerpo de respuesta.

```json
{
    "translations": [
        {
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            },
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
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