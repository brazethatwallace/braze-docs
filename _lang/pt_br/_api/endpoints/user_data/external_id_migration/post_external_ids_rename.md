---
nav_title: "POST: Renomear ID externo"
article_title: "POST: Renomear ID externo"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Renomear IDs externos."

---
{% api %}
# Renomear ID externo {#rename-external-id}
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> Use esse endpoint para renomear os IDs externos dos seus usuários.

Você pode enviar até 50 objetos de renomeação por solicitação.

Esse endpoint define um novo `external_id` (primário) para o usuário e torna obsoleto o `external_id` existente. Isso significa que o usuário pode ser identificado por qualquer um dos `external_id` até que o obsoleto seja removido. Ter vários IDs externos permite um período de migração para que as versões legadas dos seus apps que usam o esquema de nomenclatura de ID externo anterior não sejam interrompidas.

Depois que o esquema de nomenclatura antigo não estiver mais em uso, é altamente recomendável remover IDs externos obsoletos usando o [endpoint `/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove).

{% alert warning %}
Remova os IDs externos obsoletos com o endpoint `/users/external_ids/remove` em vez de `/users/delete`. O envio de uma solicitação para `/users/delete` com o ID externo obsoleto exclui totalmente o perfil do usuário e não pode ser desfeito.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key) com a permissão `users.external_ids.rename`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | Obrigatória | Array de objetos de renomeação de identificador externo | Veja o exemplo de solicitação e as limitações a seguir para a estrutura do objeto de renomeação do identificador externo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

Observe o seguinte:

- O `current_external_id` deve ser o ID principal do usuário e não pode ser um ID obsoleto.
- O `new_external_id` não deve estar em uso como ID primário ou ID obsoleto.
- O `current_external_id` e o `new_external_id` não podem ser iguais.

## Exemplo de solicitação {#request-example}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## Resposta {#response}

A resposta confirmará todas as renomeações bem-sucedidas, bem como as malsucedidas com quaisquer erros associados. As mensagens de erro no campo `rename_errors` farão referência ao índice do objeto no array da solicitação original.

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

O campo `message` retornará `success` para qualquer solicitação válida. Erros mais específicos são capturados no array `rename_errors`. O campo `message` retorna um erro nos seguintes casos:

- Chave de API inválida
- Array `external_id_renames` vazio
- Array `external_id_renames` com mais de 50 objetos
- Limite de taxa atingido (mais de 1.000 solicitações por minuto)

## Perguntas frequentes {#frequently-asked-questions}

### Isso afeta o MAU? {#does-this-impact-mau}
Não, porque o número de usuários permanece o mesmo — eles apenas passam a ter um novo `external_id`.

### O comportamento do usuário muda historicamente? {#does-user-behavior-change-historically}
Não, porque o usuário ainda é o mesmo, e todo o seu comportamento histórico continua conectado a ele.

### Pode ser executado em espaços de trabalho de desenvolvimento ou de staging? {#can-it-be-run-on-development-or-staging-workspaces}
Sim. Na verdade, é altamente recomendável executar uma migração de teste em um espaço de trabalho de staging ou desenvolvimento e garantir que tudo ocorra bem antes de executar nos dados de produção.

### Isso registra pontos de dados? {#does-this-log-data-points}
Esse recurso não registra pontos de dados.

### Qual é o período de descontinuação recomendado? {#what-is-the-recommended-deprecation-period}
Não temos um limite rígido de quanto tempo você pode manter IDs externos obsoletos, mas é altamente recomendável removê-los quando não houver mais necessidade de fazer referência aos usuários pelo ID obsoleto.

{% endapi %}