---
nav_title: "GET: Ver todas las traducciones de un bloque de contenido"
article_title: "GET: Ver todas las traducciones de un bloque de contenido"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el endpoint Ver todas las traducciones de un bloque de contenido."
---

{% api %}
# Ver todas las traducciones de un bloque de contenido {#view-all-translations-for-a-content-block}
{% apimethod get %}
/content_blocks/translations
{% endapimethod %}

> Usa este endpoint para ver todas las traducciones de un [bloque de contenido]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Consulta [Locales en los mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para obtener más información sobre las características de traducción.

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `content_blocks.translations.get`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parámetros de consulta {#query-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | Obligatorio | Cadena | El ID de tu bloque de contenido. |
| `locale_id` | Opcional | Cadena | Un UUID de locale para filtrar las respuestas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de consulta" }

{% alert note %}
Todos los ID de traducción se consideran identificadores únicos universales (UUID), que se pueden encontrar en la respuesta del endpoint GET.
{% endalert %}

## Ejemplo de solicitud {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/content_blocks/translations?content_block_id={content_block_id}&locale_id={locale_uuid}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

Hay cuatro respuestas de código de estado para este endpoint: `200`, `400`, `404` y `429`.

### Ejemplo de respuesta correcta {#example-success-response}

El código de estado `200` podría devolver el siguiente encabezado y cuerpo de respuesta.

```json
{
    "translations": [
        {
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            },
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            }
        },
        {
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
            },
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
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
	"errors": [
		{
			"message": "This message does not support multi-language."
		}
	]
}
```


{% endapi %}