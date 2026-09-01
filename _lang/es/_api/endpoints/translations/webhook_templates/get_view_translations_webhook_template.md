---
nav_title: "GET: Ver traducciones para plantilla de webhook"
article_title: "GET: Ver traducciones para plantilla de webhook"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint para ver traducciones de una plantilla de webhook."
---

{% api %}
# Ver traducciones para una plantilla de webhook {#view-translations-for-a-webhook-template}
{% apimethod get %}
/templates/webhook/translations
{% endapimethod %}

> Utiliza este endpoint para ver las traducciones de una [plantilla de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates). Puedes devolver todos los locales configurados o filtrar la respuesta por locale. Para más información sobre las características de traducción, consulta [Mensajes multilingües]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `templates.translations.get`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta {#query-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `template_id` | Obligatorio | Cadena | El ID de tu plantilla de webhook. |
| `locale_id` | Opcional | Cadena | El UUID del locale a devolver. Si se omite, la respuesta incluye todos los locales configurados para la plantilla de webhook. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de consulta" }

## Ejemplo de solicitud {#example-request}

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations?template_id={TEMPLATE_ID}&locale_id={LOCALE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

Sustituye *`TEMPLATE_ID`* por el ID de tu plantilla de webhook y *`LOCALE_ID`* por el UUID del locale que deseas devolver. Omite `locale_id` para devolver todos los locales configurados.

## Respuesta {#response}

Existen cinco códigos de estado de respuesta para este endpoint: `200`, `400`, `403`, `404` y `429`.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "translations": [
    {
      "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "¿Te gustaría comprar esto?"
      },
      "locale": {
        "uuid": "c7c12345-de35-1234-5678-abcdefa99a3f",
        "name": "es-MX",
        "country": "MX",
        "language": "es",
        "locale_key": "es-mx"
      }
    },
    {
      "translation_map": {
        "id_0": "你好！",
        "id_1": "你想買這個嗎？"
      },
      "locale": {
        "uuid": "a1b12345-cd35-1234-5678-abcdefa99a3f",
        "name": "zh-HK",
        "country": "HK",
        "language": "zh",
        "locale_key": "zh-hk"
      }
    }
  ]
}
```

### Ejemplo de respuesta de error {#example-error-response}

El código de estado `400` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "message": "Invalid locale ID"
}
```

{% endapi %}