---
nav_title: "GET: Listar grupos de inscrições de usuários"
article_title: "GET: Listar os grupos de inscrições do usuário"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para listar os grupos de inscrições do usuário."

---
{% api %}
# Listar os grupos de inscrições do usuário {#list-users-subscription-groups}
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> Use esse endpoint para listar e obter os grupos de inscrições com o histórico de um determinado usuário.

Se você quiser ver exemplos ou testar este endpoint para **grupos de inscrições para e-mail**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

Se você quiser ver exemplos ou testar este endpoint para **grupos de inscrições de SMS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

Se você quiser ver exemplos ou testar este endpoint para **grupos do WhatsApp**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `subscription.groups.get`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `external_id` | Obrigatório | String | O `external_id` do usuário (deve incluir no mínimo um e no máximo 50 `external_ids`). |
| `email` | Obrigatório* | String | O endereço de e-mail do usuário, que pode ser passado como uma matriz de strings. Deve incluir pelo menos um endereço de e-mail (com um máximo de 50). |
| `phone` | Obrigatório* | String no formato [E.164](https://en.wikipedia.org/wiki/E.164) | O número de telefone do usuário. Deve incluir pelo menos um número de telefone (com um máximo de 50). |
| `limit` | Opcional | Número inteiro | O limite do número máximo de resultados retornados. O `limit` padrão (e máximo) é 100. |
| `offset` | Opcional | Número inteiro | Número de modelos a serem ignorados antes de retornar o restante dos modelos que atendem aos critérios de pesquisa. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

{% alert tip %}
Se houver vários usuários (vários `external_ids`) que compartilham o mesmo endereço de e-mail, todos os usuários serão retornados como um usuário separado (mesmo que tenham o mesmo endereço de e-mail ou grupo de inscrições).
{% endalert %}

## Exemplo de solicitação {#example-request}

{% tabs %}
{% tab Múltiplos usuários %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS e WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab E-mail %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@example.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Exemplo de resposta {#example-response}

Somente os grupos de inscrições que tiveram uma atualização de status de inscrição no histórico de um usuário serão incluídos em uma resposta bem-sucedida. Isso significa que os grupos de inscrições recém-criados não serão listados.

```json
{
    "users": [
        {
            "email": "test@example.com",
            "phone": "+11112223333",
            "external_id": "external_identifier",
            "subscription_groups": [
                {
                  "id": "ec2fcc919fca",
                  "name": "ActivationGroup",
                  "channel": "email",
                  "status": "Subscribed"
                },
                {
                  "id": "7d7af9dd5556",
                  "name": "ReactivationGroup",
                  "channel": "email",
                  "status": "Subscribed"
                },
                {
                  "id": "a5e84fd16220",
                  "name": "MarketingGroup",
                  "channel": "sms",
                  "status": "Unsubscribed"
                },
                {
                  "id": "64d8cad9176c",
                  "name": "TransactionalGroup",
                  "channel": "sms",
                  "status": "Unsubscribed"
                },
                {
                  "id": "b2134cd63942",
                  "name": "BankerMarketingGroup",
                  "channel": "sms",
                  "status": "Subscribed"
                }
            ]
        }
    ],
    "total_count": 1,
    "message": "success"
}
```

{% endapi %}