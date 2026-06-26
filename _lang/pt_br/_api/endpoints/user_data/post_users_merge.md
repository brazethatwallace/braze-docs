---
nav_title: "POST: Mesclar usuários"
article_title: "POST: Mesclar usuários"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Mesclar usuários\"."

---
{% api %}
# Mesclar usuários {#merge-users}
{% apimethod post %}
/users/merge
{% endapimethod %}

> Use este endpoint para mesclar um usuário em outro usuário.

Até 50 mesclagens podem ser especificadas por solicitação. Este endpoint é assíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/api_key/) com a permissão `users.merge`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `merge_updates` | Obrigatória | Vetor | Um vetor de objetos. Cada objeto deve conter um objeto `identifier_to_merge` e um objeto `identifier_to_keep`, cada um dos quais deve fazer referência a um usuário por `external_id`, `user_alias`, `phone` ou `email`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação" }

### Comportamento de mesclagem {#merge-behavior}

O comportamento documentado abaixo é verdadeiro para todos os recursos da Braze que **não são** alimentados pelo Snowflake. As mesclagens de usuários não serão refletidas na guia **Histórico de mensagens**, Extensões de segmento, Criador de consultas e Currents.

{% alert important %}
O endpoint não garante a sequência de atualização dos objetos `merge_updates`.
{% endalert %}

Este endpoint mescla os seguintes campos se eles não forem encontrados no usuário alvo.

- Nome
- Sobrenome
- Endereços de e-mail (a menos que estejam [criptografados]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption/))
- Gênero
- Data de nascimento
- Número de telefone
- Fuso horário
- Cidade natal
- País
- Idioma
- Informações sobre o dispositivo
- Contagem de sessões (a soma das sessões de ambos os perfis)
- Data da primeira sessão (a Braze escolhe a data mais antiga das duas)
- Data da última sessão (a Braze escolhe a data mais recente das duas)
- Atributos personalizados (a Braze mantém os atributos personalizados existentes no perfil alvo e inclui atributos personalizados que não existiam no perfil alvo)
- Dados de eventos personalizados e de eventos de compra
- Propriedades de evento personalizado e de compra para segmentação "X vezes em Y dias" (onde X<=50 e Y<=30)
- Resumo dos eventos personalizados segmentáveis
  - Contagem de eventos (a soma de ambos os perfis)
  - O evento ocorreu pela primeira vez (a Braze escolhe a data mais antiga das duas)
  - O evento ocorreu pela última vez (a Braze escolhe a data mais recente das duas)
- Total de compras no app em centavos (a soma de ambos os perfis)
- Número total de compras (a soma de ambos os perfis)
- Data da primeira compra (a Braze escolhe a data mais antiga das duas)
- Data da última compra (a Braze escolhe a data mais recente das duas)
- Resumos do app
- Campos Last_X_at (a Braze atualiza os campos se os campos do perfil órfão forem mais recentes)
- Dados de interação de Campaign (a Braze escolhe os campos de data mais recentes)
- Resumos de fluxo de trabalho (a Braze escolhe os campos de data mais recentes)
- Histórico de mensagens e de engajamento com mensagens
- A Braze mescla dados de sessão apenas se o app existir em ambos os perfis de usuário.

{% alert note %}
Ao mesclar usuários, o uso do endpoint `/users/merge` funciona da mesma forma que o [método `changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
{% endalert %}

A Braze lida com três tipos de usuários de forma diferente ao mesclar: usuários marcados para exclusão, usuários teste e usuários do Grupo de controle global. Para saber mais, consulte [Comportamento de mesclagem de usuários]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior/).

#### Comportamento da data do evento personalizado e da data do evento de compra {#custom-event-date-and-purchase-event-date-behavior}

Esses campos mesclados atualizam filtros "para X eventos em Y dias". Para eventos de compra, esses filtros incluem "número de compras em Y dias" e "dinheiro gasto nos últimos Y dias".

### Mesclando usuários por e-mail ou número de telefone {#merging-users-by-email-or-phone-number}

Se um `email` ou `phone` for especificado como identificador, você deve incluir um valor adicional `prioritization` no identificador. O `prioritization` deve ser um vetor ordenado especificando qual usuário mesclar se múltiplos usuários forem encontrados. Isso significa que, se mais de um usuário corresponder a uma priorização, a mesclagem não ocorre.

Os valores permitidos para o vetor são:

- `identified`
- `unidentified`
- `most_recently_updated` (refere-se a priorizar o usuário atualizado mais recentemente)
- `least_recently_updated` (refere-se a priorizar o usuário atualizado menos recentemente)

Somente uma das opções a seguir pode existir no vetor de priorização por vez:

- `identified` refere-se à priorização de um usuário com um `external_id`
- `unidentified` refere-se à priorização de um usuário sem um `external_id`

{% alert important %}
Se ambos os perfis tiverem números de telefone inválidos, a Braze não os mescla. Números inválidos não são armazenados no formato E.164, e o processo de mesclagem não combina esses perfis. O endpoint ainda retorna `202 Accepted` com uma mensagem de sucesso, então a resposta HTTP não indica que a mesclagem foi ignorada. Corrija os números de telefone em um ou ambos os perfis antes de mesclar.
{% endalert %}

## Exemplos de solicitações {#example-requests}

### Solicitação básica {#basic-request}

Este é um corpo de solicitação básico para mostrar o padrão da solicitação.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "email": "user1@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

### Mesclando usuário não identificado {#merging-unidentified-user}

A seguinte solicitação mesclaria o usuário não identificado atualizado mais recentemente com o endereço de e-mail `john.smith@braze.com` no usuário com ID externo `john`. Neste exemplo, usar `most_recently_updated` filtra a consulta para um usuário não identificado. Portanto, se houvesse dois usuários não identificados com este endereço de e-mail, apenas um seria mesclado no usuário que tem o ID externo `john`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

### Mesclando usuário não identificado com usuário identificado {#merging-unidentified-user-into-identified-user}

Este próximo exemplo mescla o usuário não identificado atualizado mais recentemente com o endereço de e-mail `john.smith@braze.com` no usuário identificado atualizado mais recentemente com o endereço de e-mail `john.smith@braze.com`.

Usar `most_recently_updated` filtra as consultas para um usuário (um usuário não identificado para `identifier_to_merge` e um usuário identificado para `identifier_to_keep`).

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    }
  ]
}'
```

### Mesclando um usuário não identificado sem incluir a priorização most_recently_updated {#merging-an-unidentified-user-without-including-the-most_recently_updated-prioritization}

Se houver dois usuários não identificados com o endereço de e-mail `john.smith@braze.com`, este exemplo de solicitação não mescla nenhum usuário porque há dois usuários não identificados com esse endereço de e-mail. Esta solicitação só funciona se houver apenas um usuário não identificado com o endereço de e-mail `john.smith@braze.com`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

## Resposta {#response}

Existem dois códigos de status para este endpoint: `202` e `400`.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `202` poderia retornar o seguinte corpo de resposta.

```json
{
  "message": "success"
}
```

### Exemplo de resposta de erro {#example-error-response}

O código de status `400` poderia retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para saber mais sobre os erros que você pode encontrar.

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## Solução de problemas {#troubleshooting}

### Uma resposta de sucesso foi retornada, mas o usuário mesclado ainda pode ser encontrado {#a-success-response-was-returned-but-the-merged-user-is-still-searchable}

Uma resposta de sucesso confirma que a solicitação foi aceita, mas a operação de mesclagem envolve duas etapas: mesclar os perfis e depois remover o perfil de origem. Por causa disso, o perfil `identifier_to_merge` pode continuar pesquisável no dashboard por um curto período após uma resposta de sucesso. Esse é o comportamento esperado — aguarde alguns minutos e depois verifique se a mesclagem foi concluída.

Se o usuário mesclado ainda existir após vários minutos, verifique se os identificadores na sua solicitação estão corretos e pertencem a usuários no mesmo espaço de trabalho da chave de API usada na solicitação.

### Referência de erros {#error-reference}

A tabela a seguir lista as possíveis mensagens de erro que podem ocorrer.

| Erro | Solução de problemas |
| --- | --- |
| `'merge_updates' must be an array of objects` | Verifique se `merge_updates` é um vetor de objetos. |
| `a single request may not contain more than 50 merge updates` | Você só pode especificar até 50 atualizações de mesclagem em uma única solicitação. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string` | Verifique os identificadores na sua solicitação. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | Verifique se `merge_updates` contém apenas os dois objetos `identifier_to_merge` e `identifier_to_keep`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }

{% endapi %}