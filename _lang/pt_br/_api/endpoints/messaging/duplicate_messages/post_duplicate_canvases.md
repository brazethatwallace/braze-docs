---
nav_title: "POST: Duplicar Canvas"
article_title: "POST: Duplicar Canvas"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint de duplicação de Canvas."
---

{% api %}
# Duplicar Canvas usando a API {#duplicate-canvases-using-the-api}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/canvas/duplicate
{% endapimethod %}

> Use esse endpoint para duplicar Canvas. Esse endpoint da API é semelhante à [duplicação de Canvas no dashboard da Braze][1].

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `canvas.duplicate`.

## Limite de taxa {#rate-limit}

Esse endpoint está limitado a 100 chamadas de API por minuto.

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) The Canvas identifier,
  "name": (required, string) The name of the resulting Canvas,
  "description": (optional, string) The description of the resulting Canvas,
  "tag_names": (optional, string) The tags of the resulting Canvas,
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Obrigatória | String | Consulte [Identificador do Canvas]({{site.baseurl}}/api/identifier_types). |
| `name` | Obrigatória | String | O nome do Canvas resultante. |
| `description` | Opcional | String | O campo de descrição do Canvas resultante. |
| `tag_names` | Opcional | String | As tags do Canvas resultante. Essas devem ser tags existentes. Se você adicionar novas tags na solicitação, elas substituirão todas as tags que estavam no Canvas original. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Resposta {#response}

Esse endpoint retorna um código de status `202`, e a criação do Canvas ocorre de forma assíncrona. Você pode usar o [download de evento de segurança][2] para ver os registros de quando os Canvas foram duplicados e por qual chave de API.

[1]: {{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings

{% endapi %}