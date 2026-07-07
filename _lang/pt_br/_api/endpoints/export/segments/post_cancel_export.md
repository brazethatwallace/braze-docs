---
nav_title: "POST: Cancelar exportações por segmento"
article_title: "POST: Cancelar exportações por segmento"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para cancelar exportações por segmento."

---
{% api %}
# Cancelar exportações por segmento {#cancel-exports-by-segment}
{% apimethod post %}
/export/segment/cancel
{% endapimethod %}

> Use este endpoint para cancelar todas as exportações em andamento com um ID de segmento especificado.

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key) com a permissão `segments.list`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id": (required, string) the `segment_id` to locate and cancel its ongoing exports
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `segment_id` | Obrigatória | String | O `segment_id` para cancelar suas exportações em andamento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/export/segment/cancel' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id": "segment_identifier"
}'
```

{% endapi %}