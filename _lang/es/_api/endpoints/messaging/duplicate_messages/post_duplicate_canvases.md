---
nav_title: "POST: Duplicar Canvas"
article_title: "POST: Duplicar Canvas"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el endpoint Duplicar Canvas."
---

{% api %}
# Duplicar Canvas utilizando la API {#duplicate-canvases-using-the-api}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/Canvas/duplicate
{% endapimethod %}

> Utiliza este endpoint para duplicar Canvas. Este endpoint de la API es similar a [duplicar Canvas en el panel de Braze]({{site.baseurl}}/user_guide/messaging/governance/duplicating).

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, deberás generar una clave de API con el permiso `canvas.duplicate`.

## Límite de velocidad {#rate-limit}

Este endpoint está limitado a 100 llamadas a la API por minuto.

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) The Canvas identifier,
  "name": (required, string) The name of the resulting Canvas,
  "description": (optional, string) The description of the resulting Canvas,
  "tag_names": (optional, array of strings) The tags of the resulting Canvas,
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Obligatorio | Cadena | Ver [identificador de Canvas]({{site.baseurl}}/api/identifier_types). |
| `name` | Obligatorio | Cadena | El nombre del Canvas resultante. |
| `description` | Opcional | Cadena | El campo de descripción del Canvas resultante. |
| `tag_names` | Opcional | Matriz de cadenas | Las etiquetas del Canvas resultante. Deben ser etiquetas existentes. Si añades nuevas etiquetas en la solicitud, sobrescribirán cualquier etiqueta que hubiera en el Canvas original. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Respuesta {#response}

Este endpoint devuelve un código de estado `202`, y la creación del Canvas se produce de forma asíncrona. Puedes utilizar la [descarga de eventos de seguridad]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report) para ver los registros de cuándo se duplicaron los Canvas y mediante qué clave de API.

{% endapi %}