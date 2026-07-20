---
nav_title: "POST: Duplicar Campaigns"
article_title: "POST: Duplicar Campaigns"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint \"Duplicar Campaigns\"."

---
{% api %}
# Duplicar Campaigns usando a API {#duplicate-campaigns-using-the-api}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/duplicate
{% endapimethod %}

> Use esse endpoint para duplicar Campaigns. Esse endpoint da API é semelhante à [duplicação de Campaigns no dashboard da Braze]({{site.baseurl}}/user_guide/messaging/governance/duplicating).

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `campaigns.duplicate`.

## Limite de frequência {#rate-limit}

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
  "tag_names": (optional, array of strings) The tags of the resulting campaign,
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obrigatório | String | Consulte [identificador de Campaign]({{site.baseurl}}/api/identifier_types). |
| `name` | Obrigatório | String | O nome da Campaign resultante. |
| `description` | Opcional | String | O campo de descrição da Campaign resultante. |
| `tag_names` | Opcional | Array de strings | As tags da Campaign resultante. Elas devem ser tags já existentes. Se você adicionar novas tags na solicitação, elas substituirão quaisquer tags que estavam na Campaign original. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }


## Resposta {#response}

Esse endpoint retorna um código de status `202`, e a criação da Campaign ocorre de forma assíncrona. Você pode usar o [download de eventos de segurança]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report) para ver registros de quando as Campaigns foram duplicadas e por qual chave de API.

{% endapi %}