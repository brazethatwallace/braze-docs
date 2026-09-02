---
nav_title: "GET: Listar apps do espaço de trabalho"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "Este artigo descreve detalhes sobre o endpoint Listar apps do espaço de trabalho da Braze."
---
{% API or interface de programação do aplicativo (API) %}
# Listar apps do espaço de trabalho {#list-workspace-apps}
{% apimethod get %}
/app_group/apps
{% endapimethod %}

> Use este endpoint para listar o nome e o identificador exclusivo (`api_key`) dos apps em um espaço de trabalho.

Ao acessar este endpoint, é retornado um vetor de objeto chamado `apps`. Cada objeto em `apps` contém o nome e o identificador exclusivo do app.

{% apiref postman %}  {% endapiref %}

## Limite de taxa {#rate-limit}

Este endpoint tem um limite de taxa de 100 solicitações por dia (24 horas).

## Parâmetros de solicitação {#request-parameters}

Esta solicitação não aceita parâmetros.

## Exemplo de solicitação {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/apps' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Resposta {#response}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "apps": [
        {
          "name": "App Name",
          "api_key": 00000000-0000-0000-0000-000000000000
        }
    ],
    "message": "success"
}
```

### Solução de problemas {#troubleshooting}

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `401: Unauthorized` | A chave de API or interface de programação do aplicativo (API) não tem as permissões necessárias. Verifique se sua chave de API or interface de programação do aplicativo (API) tem permissões de `apps.get`. |
| `403: Forbidden` | O feature flipper não está ativado para esta empresa. Entre em contato com seu gerente de sucesso do cliente para obter assistência. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}