---
nav_title: "GET: Exportar sessões do app por tempo"
article_title: "GET: Exportar sessões do app por tempo"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Exportar análise de dados de sessões do app por tempo\"."

---
{% API or interface de programação do aplicativo (API) %}
# Exportar sessões do app por tempo {#export-app-session-by-time}
{% apimethod get %}
/sessions/data_series
{% endapimethod %}

> Use esse endpoint para recuperar uma série do número de sessões do seu app em um período de tempo designado.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#79efb6a9-62ec-4b8a-bf4a-e96313aa4be1 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `sessions.data_series`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| -------- | -------- | --------- | ----------- |
| `length` | Obrigatório | Inteiro | Número máximo de unidades (dias ou horas) antes de `ending_at` para incluir na série retornada. Deve estar entre 1 e 100 (inclusive). |
| `unit` | Opcional | String | Unidade de tempo entre os pontos de dados. Pode ser `day` ou `hour`, o padrão é `day`. |
| `ending_at` | Opcional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data em que a série de dados deve terminar. O padrão é a hora da solicitação. |
| `app_id` | Opcional | String | Identificador de API or interface de programação do aplicativo (API) do app recuperado da página [Chaves de API or interface de programação do aplicativo (API)]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) para limitar a análise de dados a um app específico. |
| `segment_id` | Opcional | String | Consulte [Identificador de API or interface de programação do aplicativo (API) do Segment or segmento or segmento]({{site.baseurl}}/api/identifier_types). ID do Segment or segmento or segmento que indica o Segment or segmento or segmento com análise de dados ativada para o qual as sessões devem ser retornadas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sessions/data_series?length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Resposta {#response}

```json
{
    "message": (string) returns 'success' when the request completes without errors,
    "data" : [
        {
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "sessions" : (int)
        },
        ...
    ]
}
```

{% alert tip %}
Para obter ajuda com exportações de CSV e API or interface de programação do aplicativo (API), acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}