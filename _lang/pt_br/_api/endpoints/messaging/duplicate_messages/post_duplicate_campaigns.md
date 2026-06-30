---
nav_title: "POST: Duplicar campaigns"
article_title: "POST: Duplicar campaigns"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint \"Duplicar campaigns\"."

---
{% api %}
# Duplicar campaigns usando a API {#duplicate-campaigns-using-the-api}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/duplicate
{% endapimethod %}

> Use esse endpoint para duplicar campaigns. Esse endpoint da API é semelhante à [duplicação de campaigns no dashboard da Braze][1].

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `campaigns.duplicate`.

## Limite de taxa {#rate-limit}

Esse endpoint está limitado a 100 chamadas de API por minuto.

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) The campaign identifier,
  "name": (required, string) The name of the resulting campaign,
  "description": (optional, string) The description of the resulting campaign,
  "tag_names": (optional, string) The tags of the resulting campaign,
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obrigatória | String | Consulte [identificador de campaign]({{site.baseurl}}/api/identifier_types). |
| `name` | Obrigatória | String | O nome da campaign resultante. |
| `description` | Opcional | String | O campo de descrição da campaign resultante. |
| `tag_names` | Opcional | String | As tags da campaign resultante. Elas devem ser tags já existentes. Se você adicionar novas tags na solicitação, elas substituirão quaisquer tags que estavam na campaign original. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }


## Resposta {#response}

Esse endpoint retornará um código de status `202` e a criação da campaign ocorrerá de forma assíncrona. Você pode usar o [download de eventos de segurança][2] para ver registros de quando as campaigns foram duplicadas e por qual chave de API.


[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report

{% endapi %}