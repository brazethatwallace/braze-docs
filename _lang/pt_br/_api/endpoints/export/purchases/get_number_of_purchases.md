---
nav_title: "GET: Exportar número de compras"
article_title: "GET: Exportar número de compras"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para exportar o número de compras."

---
{% api %}
# Exportar número de compras {#export-number-of-purchases}
{% apimethod get %}
/purchases/quantity_series
{% endapimethod %}

> Use esse endpoint para retornar o número total de compras no seu app em um intervalo de tempo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6ac59282-d231-4317-88df-f7f12169b94e{% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `purchases.quantity_series`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `ending_at` | Opcional | Datetime (string [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Data em que a exportação de dados deve terminar. O padrão é o momento da solicitação. |
| `length` | Obrigatório | Inteiro | Número máximo de dias antes de `ending_at` para incluir na série retornada. Deve estar entre 1 e 100 (inclusive). |
| `unit` | Opcional | String | Unidade de tempo entre os pontos de dados. Pode ser dia ou hora; o padrão é dia. |
| `app_id` | Opcional | String | Identificador de API do app recuperado da página [Chaves de API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Se excluído, serão retornados os resultados de todos os apps em um espaço de trabalho. |
| `product` | Opcional | String | Nome do produto para filtrar a resposta. Se excluído, os resultados de todos os apps serão retornados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/quantity_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta {#response}

```json
{
  "message": (string) returns 'success' when the request completes without errors,
  "data" : [
    {
      "time" : (string) the date as ISO 8601 date,
      "purchase_quantity" : (int) the number of items purchased in the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}