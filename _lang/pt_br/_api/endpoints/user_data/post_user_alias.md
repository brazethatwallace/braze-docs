---
nav_title: "POST: Criar novo alias de usuário"
article_title: "POST: Criar novo alias de usuário"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Criar novo alias de usuário da Braze."

---
{% api %}
# Criar novo alias de usuário {#create-new-user-alias}
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> Use esse endpoint para adicionar novos aliases de usuário para usuários identificados existentes ou para criar novos usuários não identificados.

Podem ser especificados até 50 aliases de usuário por solicitação.

**A adição de um alias de usuário para um usuário existente** requer que um `external_id` seja incluído no novo objeto de alias de usuário. Se o `external_id` estiver presente no objeto, mas não houver nenhum usuário com esse `external_id`, o alias não será adicionado a nenhum usuário. Se um `external_id` não estiver presente, um usuário ainda será criado, mas precisará ser identificado posteriormente. Você pode fazer isso usando o endpoint "Identificação de usuários" e o endpoint `users/identify`.

**A criação de um novo usuário somente de alias** exige que o `external_id` seja omitido no novo objeto de alias de usuário. Depois que o usuário for criado, use o endpoint `/users/track` para associar o usuário somente de alias a atributos, eventos e compras, e o endpoint `/users/identify` para identificar o usuário com um `external_id`.

## Quando `alias_label` e `alias_name` já existem {#when-alias_label-and-alias_name-already-exist}

A combinação de `alias_label` e `alias_name` deve ser única em toda a sua base de usuários. Para saber mais, consulte [Aliases de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).

Se você enviar uma solicitação em que o par `alias_label` e `alias_name` já existe para qualquer usuário (seja no mesmo usuário ou em outro), o endpoint ainda retornará uma resposta de sucesso (por exemplo, `"aliases_processed": 1`, `"message": "success"`). Nesse caso, nenhum novo alias é adicionado ao usuário na solicitação. Como o par `alias_label` e `alias_name` já está em uso, a solicitação não faz nenhuma alteração, e pode parecer que o alias nunca foi adicionado ao usuário em questão.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.alias.new`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | Obrigatório | Vetor de objetos de novos aliases de usuário | Consulte o [objeto de alias de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/).<br><br> Para saber mais sobre `alias_name` e `alias_label`, consulte nossa documentação sobre [aliases de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

### Corpo da solicitação do endpoint com a especificação do novo objeto de alias de usuário {#endpoint-request-body-with-new-user-alias-object-specification}

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## Exemplo de solicitação {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "user_aliases" :[
    {
      "external_id": "external_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
```

## Resposta {#response}

Quando um alias é ignorado porque o mesmo `alias_label` e `alias_name` já existem para um usuário, o corpo da resposta ainda pode indicar sucesso. Consulte [Quando `alias_label` e `alias_name` já existem](#when-the-alias-label-and-name-already-exist) para mais detalhes.

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```


{% endapi %}