---
nav_title: "GET: Ver traducciones de origen para plantilla de webhook"
article_title: "GET: Ver traducciones de origen para plantilla de webhook"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint para ver las traducciones de origen de una plantilla de webhook."
---

{% api %}
# Ver traducciones de origen para una plantilla de webhook {#view-source-translations-for-a-webhook-template}
{% apimethod get %}
/templates/webhook/translations/source
{% endapimethod %}

> Utiliza este endpoint para ver las traducciones de origen predeterminadas de una [plantilla de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates). Para más información sobre las características de traducción, consulta [Mensajes multilingüe]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `templates.translations.get`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta {#query-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `template_id` | Obligatorio | Cadena | El ID de tu plantilla de webhook. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de consulta" }

## Ejemplo de solicitud {#example-request}

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations/source?template_id={TEMPLATE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

Sustituye *`TEMPLATE_ID`* por el ID de tu plantilla de webhook.

## Respuesta {#response}

Hay cinco códigos de estado de respuesta para este endpoint: `200`, `400`, `403`, `404` y `429`.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "translations": {
    "translation_map": {
      "id_0": "Hello!",
      "id_1": "Would you like to buy this?"
    }
  }
}
```

### Ejemplo de respuesta de error {#example-error-response}

El código de estado `400` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "message": "This template does not have multi-language setup"
}
```

{% endapi %}