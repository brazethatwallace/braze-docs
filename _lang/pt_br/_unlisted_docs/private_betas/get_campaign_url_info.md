---
nav_title: "GET: Listar alias de link para Campaigns"
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

description: "Este artigo descreve detalhes sobre o endpoint Listar alias de link da Braze."
---
{% api %}
# Listar alias de link para campaign {#list-link-alias-for-campaign}
{% apimethod get %}
/campaigns/url_info/details
{% endapimethod %}

> Use este endpoint para listar o conjunto de alias de link em uma variante de mensagem específica de uma campaign.

{% apiref postman %}  {% endapiref %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `campaign_id`  | Obrigatória | String | Consulte [identificador de API da campaign](https://www.braze.com/docs/api/identifier_types/#campaign-api-identifier). |
| `message_variation_id `  |  Obrigatória | String | Identificador de API da variante de mensagem. Você pode encontrá-lo na página de detalhes da campaign, na seção **API Identifier**. |
| `includes_link_id` | Opcional | String | Um identificador de link específico (conforme atribuído pela Braze) ou `null`. Usado para filtrar os resultados por um `link_id` específico. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemplo de solicitação {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/campaigns/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Resposta {#response}

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

### Solução de problemas {#troubleshooting}

A tabela a seguir lista possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `Missing/Invalid Campaign ID` | O ID de API da campaign deve ser um identificador de API. Você pode encontrá-lo usando o [endpoint Exportar lista de campaigns](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaigns/) ou fazendo login no dashboard. |
| `Missing/Invalid Message Variant ID` | O ID de API da variante de mensagem deve ser um identificador de API. Você pode encontrá-lo usando o [endpoint Exportar detalhes da campaign](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_details/) ou fazendo login no dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}