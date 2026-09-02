---
nav_title: "POST: Criar nova conta de usuário do dashboard"
article_title: "POST: Criar nova conta de usuário do dashboard"
alias: /post_create_user_account/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Criar nova conta de usuário do dashboard da Braze."
---

{% api %}
# Criar nova conta de usuário do dashboard {#create-new-dashboard-user-account}
{% apimethod post %}
/scim/v2/Users
{% endapimethod %}

> Use esse endpoint para criar uma nova conta de usuário do dashboard especificando e-mail, nome e sobrenome, permissões (para definir permissões no nível da empresa, do espaço de trabalho e da equipe).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#768a3c9d-ce1d-44fc-a0e4-d556b09f7aa3 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de um token SCIM. Você usará a origin do seu serviço como o cabeçalho `X-Request-Origin`. Para saber mais, consulte [Provisionamento automatizado de usuários]({{site.baseurl}}/scim/automated_user_provisioning).

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='create dashboard user' %}

## Corpo da solicitação {#request-body}
```
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-KEY
```
```
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "user@example.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role"
            },
            {
                "roleId": "2519dafcdba238ae7"
            }
        ],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",
                         "teamPermissions": ["basic_access","export_user_data"]
                    }
                ]
            },
            {
                "appGroupName": "Other Test Workspace",
                "appGroupPermissionSets": [
                    {
                        "appGroupPermissionSetName":  "Test Permission Set"
                    }
                ]
            }
        ]
    }
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `schemas` | Obrigatório | Array de strings | Nome do esquema SCIM 2.0 esperado para o objeto do usuário. |
| `userName` | Obrigatório | String | O endereço de e-mail do usuário. |
| `name` | Obrigatório | Objeto JSON | Esse objeto contém o nome e o sobrenome do usuário. |
| `department` | Obrigatório | String | String de departamento válida da [documentação de string de departamento]({{site.baseurl}}/api/objects_filters/scim_api_appendix). |
| `permissions` | Opcional | Objeto JSON | Objeto de permissões, conforme descrito na [documentação do objeto de permissões]({{site.baseurl}}/api/objects_filters/scim_api_appendix). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
```bash
curl --location --request POST 'https://rest.iad-01.braze.com/scim/v2/Users' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM–TOKEN-HERE' \
--data raw '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "user@example.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role"
            },
            {
                "roleId": "2519dafcdba238ae7"
            }
        ],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",
                         "teamPermissions": ["basic_access","export_user_data"]
                    }
                ]
            }
        ]
    }
}'
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
    "lastSignInAt": "Thursday, January 1, 1970 12:00:00 AM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role",
                "roleId": "519dafcdba23dfaae7",
                "appGroup": [
                    {
                        "appGroupId": "241adcd25789fabcded",
                        "appGroupName": "Some Workspace",
                        "appGroupPermissions": ["basic_access", "publish_cards"],
                        "team": [
                            {
                                "teamId": "2519dafcdba238ae7",
                                "teamName": "Some Team",
                                "teamPermissions": ["export_user_data"]
                            }
                        ]
                    }
                ]
            },
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
                         "teamId": "2519dafcdba238ae7",
                         "teamName": "Test Team",
                         "teamPermissions": ["basic_access","export_user_data"]
                    }
                ]
            },
            {
                "appGroupName": "Other Test Workspace",
                "appGroupPermissionSets": [
                    {
                        "appGroupPermissionSetName":  "Test Permission Set"
                    }
                ]
            }
        ]
    }
}
```

## Parâmetros de resposta {#response-parameters}

| Parâmetro | Tipo de dados | Descrição |
| --------- | --------- | ----------- |
| `schemas` | Array de strings | Nome do esquema SCIM 2.0 esperado para o objeto do usuário. |
| `userName` | String | O endereço de e-mail do usuário. |
| `name` | Objeto JSON | Esse objeto contém o nome e o sobrenome do usuário. |
| `department` | String | String de departamento válida da [documentação de string de departamento]({{site.baseurl}}/api/objects_filters/scim_api_appendix). |
| `permissions` | Objeto JSON | Objeto de permissões, conforme descrito na [documentação do objeto de permissões]({{site.baseurl}}/api/objects_filters/scim_api_appendix). |
| `id` | String | ID gerado pela Braze usado para pesquisar e gerenciar contas de usuário. |
| `lastSignInAt` | String | Data do último login bem-sucedido, em UTC. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parâmetros de resposta" }

### Estados de erro {#error-states}

Se um usuário com esse `userName` ou endereço de e-mail já existir na Braze, o endpoint responderá com:

```http
HTTP/1.1 409 Conflict
Date: Tue, 10 Sep 2019 02:22:30 GMT
Content-Type: text/json;charset=UTF-8

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "detail": "User already exists in the database.",
  "status": 409
}
```

{% endapi %}