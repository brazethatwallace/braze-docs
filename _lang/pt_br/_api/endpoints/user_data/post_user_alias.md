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

Você pode enviar Campaigns disparadas por API para usuários por `user_alias` usando o endpoint [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

## Quando `alias_label` e `alias_name` já existem {#when-alias_label-and-alias_name-already-exist}

A combinação de `alias_label` e `alias_name` deve ser única em toda a sua base de usuários. Para saber mais, consulte [Aliases de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases).

Se você enviar uma solicitação em que o par `alias_label` e `alias_name` já existe para qualquer usuário (seja no mesmo usuário ou em outro), o endpoint ainda retornará uma resposta de sucesso (por exemplo, `"aliases_processed": 1`, `"message": "success"`). Nesse caso, nenhum novo alias é adicionado ao usuário na solicitação. Como o par `alias_label` e `alias_name` já está em uso, a solicitação não faz nenhuma alteração, e pode parecer que o alias nunca foi adicionado ao usuário em questão.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics) com a permissão `users.alias.new`.

## Limite de frequência {#rate-limit}

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
| `user_aliases` | Obrigatório | Vetor de objetos de novos aliases de usuário | Consulte o [objeto de alias de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object).<br><br> Para saber mais sobre `alias_name` e `alias_label`, consulte nossa documentação sobre [aliases de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

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

## Solução de problemas {#troubleshooting}

### Por que meus atributos não estão sendo atualizados depois que eu crio um alias de usuário usando esse endpoint? {#why-are-my-attributes-not-updating-after-i-create-a-user-alias-using-this-endpoint}

Isso geralmente acontece quando `/users/alias/new` é seguido por uma solicitação separada de `/users/track` que tenta atualizar atributos por alias. A solicitação de rastreamento pode ser processada antes que a Braze consiga resolver de forma consistente o novo par `alias_label` e `alias_name` para um perfil, de modo que os atributos não são aplicados ao usuário esperado.

**Abordagem recomendada:** Use uma única chamada [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) somente quando quiser criar um perfil somente de alias ou atualizar um perfil por um alias que já existe. No vetor `attributes`, coloque `user_alias` e os campos do perfil no mesmo [objeto de atributos de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object) para que a Braze resolva o usuário e aplique a atualização em uma única etapa.

Defina `_update_existing_only` como `false` quando for necessário criar um perfil somente de alias a partir desse objeto. Se você omitir esse campo ao usar `user_alias`, a Braze assume o comportamento de somente atualização e não cria o perfil somente de alias. Se o alias já existir em um usuário no seu espaço de trabalho, a mesma solicitação atualizará esse perfil com os novos atributos.

Não é possível usar `/users/track` para adicionar um novo alias a um usuário existente identificado por `external_id`. Em um objeto de atributos de usuário, `external_id` e `user_alias` são mutuamente exclusivos. Para adicionar um alias a um usuário identificado, primeiro chame `/users/alias/new`. Depois que o alias estiver vinculado, você poderá atualizar esse perfil com `/users/track` usando o `external_id` ou o alias existente.

Por exemplo, o corpo de `/users/track` a seguir cria um perfil somente de alias se o alias ainda não existir, ou atualiza o perfil existente que já possui esse alias:
```json
{
  "attributes": [
    {
      "user_alias": {
        "alias_name": "example@example.com",
        "alias_label": "email"
      },
      "_update_existing_only": false,
      "string_attribute": "test_alias_only_update"
    }
  ]
}
```

{% endapi %}