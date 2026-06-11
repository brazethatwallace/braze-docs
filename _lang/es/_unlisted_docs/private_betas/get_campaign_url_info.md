---
nav_title: "GET: Listar alias de enlace para Campaigns"
layout: api_page
page_type: reference
hidden: true
permalink: /get_campaign_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "Este artículo describe los detalles del punto de conexión de Braze para listar alias de enlace."
---
{% api %}
# Listar alias de enlace para Campaign {#list-link-alias-for-campaign}
{% apimethod get %}
/campaigns/url_info/details
{% endapimethod %}

> Usa este punto de conexión para listar el alias de enlace configurado en una variante de mensaje específica de una Campaign.

{% apiref postman %}  {% endapiref %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `campaign_id` | Obligatoria | Cadena | Consulta [identificador de API de Campaign](https://www.braze.com/docs/api/identifier_types/#campaign-api-identifier). |
| `message_variation_id ` | Obligatoria | Cadena | Identificador de API de la variante de mensaje. Puedes encontrarlo en la página de detalles de la Campaign, en la sección **Identificador de API**. |
| `includes_link_id` | Opcional | Cadena | Un identificador de enlace específico (asignado por Braze) o `null`. Se utiliza para filtrar los resultados por un `link_id` específico. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/campaigns/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
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

La siguiente tabla enumera los posibles errores devueltos y los pasos de solución de problemas asociados.

| Error | Solución de problemas |
| --- | --- |
| `Missing/Invalid Campaign ID` | El ID de API de la Campaign debe ser un identificador de API. Puedes encontrarlo usando el [punto de conexión Exportar lista de Campaigns](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaigns/) o iniciando sesión en el dashboard. |
| `Missing/Invalid Message Variant ID` | El ID de API de la variante de mensaje debe ser un identificador de API. Puedes encontrarlo usando el [punto de conexión Exportar detalles de Campaign](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_details/) o iniciando sesión en el dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}