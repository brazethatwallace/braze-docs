---
nav_title: "GET: Exportar detalhes do segmento"
article_title: "GET: Exportar detalhes do segmento"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para exportar detalhes do segmento."

---
{% api %}
# Exportar detalhes do segmento {#export-segment-details}
{% apimethod get %}
/segments/details
{% endapimethod %}

> Use esse endpoint para recuperar informações relevantes sobre um segmento, que pode ser identificado pelo `segment_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key) com a permissão `segments.details`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro    | Obrigatória | Tipo de dados | Descrição            |
| ------------ | -------- | --------- | ---------------------- |
| `segment_id` | Obrigatória | String | Consulte [Identificador de API do segmento]({{site.baseurl}}/api/identifier_types).<br><br> O `segment_id` de um determinado segmento pode ser encontrado na página [Chaves de API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) na sua conta da Braze, ou você pode usar o [endpoint Exportar lista de segmentos]({{site.baseurl}}/api/endpoints/export/segments/get_segment).  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Resposta {#response}

```json
{
      "message": (required, string) the status of the export, returns 'success' when completed without errors,
      "created_at" : (string) the date created as ISO 8601 date,
      "updated_at" : (string) the date last updated as ISO 8601 date,
      "name" : (string) the segment name,
      "description" : (string) a human-readable description of filters,
      "text_description" : (string) the segment description,
      "tags" : (array) the tag names associated with the segment formatted as strings,
      "teams" : (array) the names of the Teams associated with the campaign
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}