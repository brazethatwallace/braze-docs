---
nav_title: "GET: Procurar uma conta de usuário de dashboard existente"
article_title: "GET: Procurar uma conta de usuário de dashboard existente"
alias: /get_see_user_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para procurar o ID de recurso de uma conta de usuário existente no dashboard."
---

{% api %}
# Procurar uma conta de usuário existente no dashboard por ID de recurso {#look-up-an-existing-dashboard-user-account-by-resource-id}
{% apimethod get %}
/scim/v2/Users/{id}
{% endapimethod %}

> Use este endpoint para procurar uma conta de usuário do dashboard existente especificando o recurso `id` retornado pelo método SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#3df40764-8f74-4532-aed3-ab8a6cb92122 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de um token SCIM. Você usará a Origin do seu serviço como o cabeçalho `X-Request-Origin`. Para saber mais, consulte [Provisionamento automatizado de usuários]({{site.baseurl}}/scim/automated_user_provisioning).

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='look up dashboard user' %}

## Parâmetros de caminho {#path-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `id` | Obrigatório | String | O ID do recurso do usuário. Esse parâmetro é retornado pelos métodos `POST` `/scim/v2/Users/` ou `GET` `/scim/v2/Users?filter=userName eq "user@example.com"`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## Parâmetros de solicitação {#request-parameters}

```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

{% alert note %}
Se você receber uma resposta `401`, confirme que está usando um token SCIM (e não uma chave da API REST), que o `X-Request-Origin` corresponde à Origin do seu serviço e que seu endereço IP está na lista de permissões do SCIM. Para saber mais, consulte [Provisionamento automatizado de usuários]({{site.baseurl}}/scim/automated_user_provisioning).
{% endalert %}

## Exemplo de solicitação {#example-request}
```bash
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Resposta {#response}
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "dfa245b7-24195aec-887bb3ad-602b3340",
    "userName": "user@example.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "lastSignInAt": "2024 Nov 11, 4:20 PM",
    "createdAt": "2024 Nov 11, 4:20 PM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Another Test Role",
                "roleId": "23125dad23dfaae7",
                "appGroup": [
                    {
                        "appGroupId": "241adcd25adfabcded",
                        "appGroupName": "Production Workspace",
                        "appGroupPermissionSets": [
                            {
                                "appGroupPermissionSetName": "A Permission Set",
                                "appGroupPermissionSetId": "dfa385109bc38",
                                "permissions": ["basic_access","publish_cards"]
                            }
                        ]
                    }
                ]
            }
        ],
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
```

## Parâmetros de resposta {#response-parameters}

| Parâmetro | Tipo de dados | Descrição |
|---|---|---|
| `schemas` | Matriz de strings | Esquema de usuário SCIM. |
| `id` | String | O ID do recurso do usuário. |
| `userName` | String | O endereço de e-mail do usuário. |
| `name` | Objeto | Contém `givenName` e `familyName`. |
| `department` | String | O departamento do usuário, se definido. |
| `createdAt` | String | Quando a conta do usuário foi criada. Retorna `N/A` quando não definido; caso contrário, formatado como `YYYY Mon DD, H:MM AM/PM`. |
| `lastSignInAt` | String | Quando o usuário fez login pela última vez. Retorna `N/A` se o usuário nunca fez login; caso contrário, formatado como `YYYY Mon DD, H:MM AM/PM`. |
| `permissions` | Objeto | Permissões de empresa, espaço de trabalho, equipe e função do usuário. Consulte o [objeto de permissões]({{site.baseurl}}/scim_api_appendix). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Response parameters" }

### Estados de erro {#error-states}

Se nenhum usuário existir para o `id` de recurso fornecido, o endpoint retornará:

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "status": 404,
  "detail": "Resource not found"
}
```

{% endapi %}