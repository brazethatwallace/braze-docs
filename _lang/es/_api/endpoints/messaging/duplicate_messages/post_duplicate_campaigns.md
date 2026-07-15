---
nav_title: "POST: Duplicar campañas"
article_title: "POST: Duplicar campañas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Duplicar campañas."

---
{% api %}
# Duplicar campañas utilizando la API {#duplicate-campaigns-using-the-api}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/duplicate
{% endapimethod %}

> Utiliza este endpoint para duplicar campañas. Este endpoint de la API es similar a la [duplicación de campañas en el panel de Braze]({{site.baseurl}}/user_guide/messaging/governance/duplicating).

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, deberás generar una clave de API con el permiso `campaigns.duplicate`.

## Límite de velocidad {#rate-limit}

Este endpoint está limitado a 100 llamadas a la API por minuto.

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) The campaign identifier,
  "name": (required, string) The name of the resulting campaign,
  "description": (optional, string) The description of the resulting campaign,
  "tag_names": (optional, array of strings) The tags of the resulting campaign,
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obligatorio | Cadena | Ver [identificador de campaña]({{site.baseurl}}/api/identifier_types). |
| `name` | Obligatorio | Cadena | El nombre de la campaña resultante. |
| `description` | Opcional | Cadena | El campo de descripción de la campaña resultante. |
| `tag_names` | Opcional | Matriz de cadenas | Las etiquetas de la campaña resultante. Deben ser etiquetas existentes. Si añades etiquetas nuevas en la solicitud, sobrescribirán cualquier etiqueta que existiera en la campaña original. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }


## Respuesta {#response}

Este endpoint devuelve un código de estado `202`, y la creación de la campaña se produce de forma asíncrona. Puedes utilizar la [descarga de eventos de seguridad]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report) para ver registros de cuándo se duplicaron las campañas y con qué clave de API.

{% endapi %}