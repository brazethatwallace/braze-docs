---
nav_title: "PUT: Actualizar traducciones para plantilla de webhook"
article_title: "PUT: Actualizar traducciones para plantilla de webhook"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint para actualizar traducciones de una plantilla de webhook."
---

{% api %}
# Actualizar traducciones para una plantilla de webhook {#update-translations-for-a-webhook-template}
{% apimethod put %}
/templates/webhook/translations
{% endapimethod %}

> Utiliza este endpoint para actualizar traducciones de una [plantilla de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates). Para más información sobre las características de traducción, consulta [Mensajes multilingüe]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `templates.translations.update`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de ruta {#path-parameters}

No hay parámetros de ruta para este endpoint.

## Parámetros de solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `template_id` | Obligatorio | Cadena | El ID de tu plantilla de webhook. |
| `locale_id` | Obligatorio | Cadena | El UUID de la configuración regional a actualizar. La configuración regional debe estar configurada para la plantilla de webhook. |
| `translation_map` | Obligatorio | Objeto | Un objeto que contiene las traducciones actualizadas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de solicitud" }

## Ejemplo de solicitud {#example-request}

```bash
curl --location --request PUT 'https://rest.iad-03.braze.com/templates/webhook/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
  "locale_id": "a14404b3-3626-4de0-bdec-06935f3aa0ad",
  "translation_map": {
    "id_0": "¡Hola!",
    "id_1": "¿Te gustaría comprar esto?"
  }
}'
```

## Respuesta {#response}

Hay cinco códigos de estado de respuesta para este endpoint: `200`, `400`, `403`, `404` y `429`.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` devuelve el siguiente cuerpo de respuesta vacío.

```json
{}
```

### Ejemplo de respuesta de error {#example-error-response}

El código de estado `400` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "message": "Locale not found"
}
```

{% endapi %}