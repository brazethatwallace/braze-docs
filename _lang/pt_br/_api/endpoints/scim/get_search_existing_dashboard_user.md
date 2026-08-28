---
nav_title: "GET: Pesquisar conta de usuário existente do dashboard por e-mail"
article_title: "GET: Pesquisar conta de usuário existente do dashboard por e-mail"
alias: /get_search_existing_dashboard_user_email/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Pesquisar conta de usuário existente do dashboard por e-mail\"."
---

{% api %}
# Pesquisar conta de usuário existente do dashboard por e-mail {#search-existing-dashboard-user-account-by-email}
{% apimethod get %}
scim/v2/Users?filter=userName%20eq%20"user%40test.com"
{% endapimethod %}

> Use esse endpoint para procurar uma conta de usuário existente no dashboard especificando o e-mail no parâmetro de consulta do filtro.

Observe que, quando o parâmetro de consulta estiver codificado em URL, ele terá a seguinte leitura:

`/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22`

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de um token SCIM. Você usará a origem do seu serviço como o cabeçalho `X-Request-Origin`. Para saber mais, consulte [Provisionamento automatizado de usuários]({{site.baseurl}}/scim/automated_user_provisioning).

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='look up dashboard user email' %}

## Parâmetros de consulta {#query-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `filter` | Obrigatório | String | Expressão de filtro SCIM para pesquisar por e-mail. A Braze suporta apenas `userName eq "user@example.com"`. O valor do e-mail deve estar entre aspas duplas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de consulta" }

{% alert important %}
A Braze suporta apenas filtros de correspondência exata em `userName` usando o operador `eq`. Outros campos ou operadores de filtro SCIM retornam uma resposta `400`.
{% endalert %}

## Parâmetros de solicitação {#request-parameters}

```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

{% alert note %}
Se você receber uma resposta `401`, confirme se está usando um token SCIM (não uma chave da API REST), se o `X-Request-Origin` corresponde à origem do seu serviço e se o seu endereço IP está na lista de permissões SCIM. Para saber mais, consulte [Provisionamento automatizado de usuários]({{site.baseurl}}/scim/automated_user_provisioning).
{% endalert %}

## Exemplo de solicitação {#example-request}
```bash
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Resposta {#response}
```json
{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
    "totalResults": 1,
    "Resources": [
        {
            "userName": "user@example.com",
            "id": "dfa245b7-24195aec-887bb3ad-602b3340",
            "name": {
                "givenName": "Test",
                "familyName": "User"
            },
            "department": "finance",
            "createdAt": "2024 Nov 11, 4:20 PM",
            "lastSignInAt": "N/A",
            "permissions": {
                "companyPermissions": ["manage_company_settings"],
                "appGroup": [
                    {
                        "appGroupId": "241adcd25789fabcded",
                        "appGroupName": "Test Workspace",
                        "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                        "team": [
                            {
                                "teamId": "241adcd25789fabcded",
                                "teamName": "Test Team",
                                "teamPermissions": ["admin"]
                            }
                        ]
                    }
                ]
            }
        }
    ]
}
```

## Parâmetros de resposta {#response-parameters}

| Parâmetro | Tipo de dados | Descrição |
|---|---|---|
| `schemas` | Array de strings | Esquema de resposta de lista SCIM. |
| `totalResults` | Inteiro | Número de usuários do dashboard correspondentes (0 se não houver correspondência). |
| `Resources` | Array | Array de objetos de usuário. Cada objeto usa os mesmos campos que [GET: Consultar conta de usuário existente do dashboard]({{site.baseurl}}/get_see_user_account_information). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parâmetros de resposta" }

### Campos do objeto de usuário {#user-object-fields}

| Parâmetro | Tipo de dados | Descrição |
|---|---|---|
| `id` | String | O ID de recurso do usuário. |
| `userName` | String | O endereço de e-mail do usuário. |
| `name` | Objeto | Contém `givenName` e `familyName`. |
| `department` | String | O departamento do usuário, se definido. |
| `createdAt` | String | Quando a conta do usuário foi criada. Retorna `N/A` quando não definido; caso contrário, no formato `YYYY Mon DD, H:MM AM/PM`. |
| `lastSignInAt` | String | Quando o usuário fez login pela última vez. Retorna `N/A` se o usuário nunca fez login; caso contrário, no formato `YYYY Mon DD, H:MM AM/PM`. |
| `permissions` | Objeto | Permissões de empresa, espaço de trabalho, equipe e função. Consulte o [objeto de permissões]({{site.baseurl}}/scim_api_appendix). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos do objeto de usuário" }

### Estados de erro {#error-states}

Se o parâmetro `filter` estiver ausente ou malformado, o endpoint retornará:

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "status": 400,
  "detail": "Request is unparsable, syntactically incorrect, or violates schema."
}
```

{% endapi %}