---
nav_title: "GET: Listar alias de enlace para Canvas"
layout: api_page
page_type: reference
hidden: true
permalink: /get_canvas_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "Este artículo describe los detalles del punto de conexión Listar alias de enlace para Canvas."
---
{% api %}
# Listar alias de enlace para Canvas {#list-link-alias-for-canvas}
{% apimethod get %}
/canvas/url_info/details
{% endapimethod %}

> Utiliza este punto de conexión para listar el conjunto de alias de enlace en un paso en Canvas de correo electrónico específico.

{% apiref postman %}  {% endapiref %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `canvas_step_id` | Obligatoria | Cadena | Consulta [Identificador de API del paso en Canvas](https://www.braze.com/docs/api/identifier_types/#canvas-api-identifier). |
| `message_variation_id ` | Obligatoria | Cadena | Identificador de API de la variante del mensaje (para la variante del mensaje de correo electrónico en ese paso). Puedes encontrarlo haciendo clic en **Analizar variantes** en la página **Detalles de Canvas**. |
| `includes_link_id` | Opcional | Cadena | Un identificador de enlace específico (asignado por Braze) o `null`. Se utiliza para filtrar los resultados por un `link_id` específico. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Ejemplo de solicitud {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/canvas/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Respuesta {#response}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "channel": "email",
  "name": "Variant 1",
  "link_data": [
    {
      "link_URL": "https://www.braze.com?lid=014tk4e0kg97",
      "link_id": "014tk4e0kg97",
      "content_block_path_info": [],
      "link_alias": "link5"
    }
  ],
  "message": "success"
}
```

### Solución de problemas {#troubleshooting}

La siguiente tabla enumera los posibles errores devueltos y sus pasos de solución de problemas asociados.

| Error | Solución de problemas |
| --- | --- |
| `Missing/Invalid Canvas ID` | El ID de API de Canvas debe ser un identificador de API. Puedes encontrarlo utilizando el [punto de conexión Exportar lista de Canvas](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvases/) o iniciando sesión en el dashboard. |
| `Missing/Invalid Message Variant ID` | El ID de API de la variante del mensaje debe ser un identificador de API. Puedes encontrarlo utilizando el [punto de conexión Exportar detalles de Canvas](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_details/) o iniciando sesión en el dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}