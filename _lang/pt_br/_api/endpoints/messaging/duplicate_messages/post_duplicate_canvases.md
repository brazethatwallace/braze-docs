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

> Use esse endpoint para duplicar Canvas. Esse endpoint da API é semelhante à [duplicação de Canvas no dashboard da Braze]({{site.baseurl}}/user_guide/messaging/governance/duplicating).

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará gerar uma chave de API com a permissão `canvas.duplicate`.

## Limite de frequência {#rate-limit}

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
  "tag_names": (optional, array of strings) The tags of the resulting Canvas,
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Obrigatório | String | Consulte [Identificador do Canvas]({{site.baseurl}}/api/identifier_types). |
| `name` | Obrigatório | String | O nome do Canvas resultante. |
| `description` | Opcional | String | O campo de descrição do Canvas resultante. |
| `tag_names` | Opcional | Array de strings | As tags do Canvas resultante. Essas devem ser tags existentes. Se você adicionar novas tags na solicitação, elas substituirão todas as tags que estavam no Canvas original. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Resposta {#response}

Esse endpoint retorna um código de status `202`, e a criação do Canvas ocorre de forma assíncrona. Você pode usar o [download de evento de segurança]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report) para ver os registros de quando os Canvas foram duplicados e por qual chave de API.

{% endapi %}