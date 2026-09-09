---
nav_title: "GET: Ver información sobre Content Blocks"
article_title: "GET: Ver información sobre Content Blocks"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint de Braze Ver información de Content Blocks."
---

{% api %}
# Ver información de Content Blocks {#see-content-block-information}
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> Utiliza este endpoint para consultar información de tus [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) existentes.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Requisitos previos {#prerequisites}
Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics) con el permiso `content_blocks.info`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `content_block_id` | Obligatorio | Cadena | El identificador del bloque de contenido. <br><br>Puedes encontrarlo listando la información de Content Blocks a través de una llamada a la API o yendo a la página [Claves de API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers), desplazándote hasta el final y buscando tu identificador de API de Content Blocks.|
| `include_inclusion_data` | Opcional | Booleano | Cuando se establece en `true`, la API devuelve el identificador de API de variación de mensajes de las Campaigns y los Canvas en los que se incluye este bloque de contenido, para utilizarlo en llamadas posteriores. Los resultados excluyen las Campaigns o los Canvas archivados o eliminados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Respuesta {#response}

```json
{
  "content_block_id": (string) the Content Block identifier,
  "name": (string) the name of the Content Block,
  "content": (string) the content in the Content Block,
  "description": (string) the Content Block description,
  "content_type": (string) the content type, html or text,
  "tags": (array) An array of tags formatted as strings,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "last_edited": (string) The time the Content Block was last edited in ISO 8601,
  "inclusion_count" : (integer) the inclusion count,
  "inclusion_data": (array) the inclusion data,
  "message": "success"
}
```

## Solución de problemas {#troubleshooting}

La siguiente tabla enumera los posibles errores devueltos y los pasos asociados para solucionarlos.

| Error | Solución de problemas |
| --- | --- |
| `Content Block ID cannot be blank` | Asegúrate de que en tu solicitud aparece un bloque de contenido y de que está encapsulado entre comillas (`""`). |
| `Content Block ID is invalid for this workspace` | Este bloque de contenido no existe o está en una cuenta de empresa o espacio de trabajo diferente. |
| `Content Block has been deleted—content not available` | Este bloque de contenido, aunque puede haber existido antes, ha sido eliminado. |
| `Include Inclusion Data—error` | Este parámetro solo acepta valores booleanos (true o false). Asegúrate de que el valor de `include_inclusion_data` no está encapsulado entre comillas (`""`), lo que hace que el valor se envíe como una cadena en lugar de un booleano. Consulta los [parámetros de la solicitud](#request-parameters) para más detalles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }


{% endapi %}