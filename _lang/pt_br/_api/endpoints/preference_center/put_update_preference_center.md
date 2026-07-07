---
nav_title: "PUT: Atualizar a Central de Preferências"
article_title: "PUT: Atualizar a Central de Preferências"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Atualizar a Central de Preferências\"."

---
{% api %}
# Atualizar a Central de Preferências {#update-preference-center}
{% apimethod put %}
/preference_center/v1/{preferenceCenterExternalID}
{% endapimethod %}

> Use esse endpoint para atualizar uma Central de Preferências.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#bf1b43db-3f1b-461f-ad9a-2fbe35b804d7 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key) com a permissão `preference_center.update`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='post or put preference center' %}

## Parâmetros de caminho {#path-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `preferenceCenterExternalID` | Obrigatório | String | O ID da sua Central de Preferências. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de caminho" }


## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```
{
  "name": "preference_center_name",
  "preference_center_title": "string",
  "preference_center_page_html": "string",
  "confirmation_page_html": "string",
  "options": {
    "unknown macro": {links-tags}
  "options": {
    "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag,
    "links-tags": [
      {
        "rel": "string", (required) One of: "icon", "shortcut icon", or "apple-touch-icon",
        "type": "string", (optional) Valid values: "image/png", "image/svg", "image/gif", "image/x-icon", "image/svg+xml", "mask-icon",
        "sizes": "string", (optional),
        "color": "string", (optional) Use when type="mask-icon",
        "href": "string", (required)
      }
    ]
  }
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `preference_center_page_html` | Obrigatório | String | O HTML da página da Central de Preferências. |
| `preference_center_title` | Opcional | String | O título da Central de Preferências e das páginas de confirmação. Se um título não for especificado, o título das páginas será "Preference Center" por padrão. |
| `confirmation_page_html` | Obrigatório | String | O HTML da página de confirmação. |
| `state` | Opcional | String | Escolha `active` ou `draft`. |
| `options` | Opcional | Objeto | Atributos: <br>`meta-viewport-content`: Quando presente, uma meta tag `viewport` será adicionada à página com `content= <value of attribute>`.<br><br> `link-tags`: Defina um favicon para a página. Quando definido, uma tag `<link>` com um atributo rel é adicionada à página. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}

{% raw %}
```
curl --location --request POST 'https://rest.iad-01.braze.com/preference_center/v1/{preferenceCenterExternalId}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "name": "Example",
  "preference_center_title": "Example Preference Center Title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML here with a message to users here",
  "state": "active"
}
'
```
{% endraw %}

## Exemplo de resposta {#example-response}
{% raw %}
```
{
  "preference_center_api_id": "8efc52aa-935e-42b7-bd6b-98f43bb9b0f1",
  "created_at": "2022-09-22T18:28:07Z",
  "updated_at": "2022-09-22T18:32:07Z",
  "message": "success"
}
```
{% endraw %}

{% endapi %}