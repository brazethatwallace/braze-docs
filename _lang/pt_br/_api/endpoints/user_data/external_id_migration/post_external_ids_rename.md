---
nav_title: "POST: Renomear ID externo"
article_title: "POST: Renomear ID externo"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Renomear IDs externos."
---
{% API or interface de programação do aplicativo (API) %}
# Renomear ID externo {#rename-external-id}
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> Use esse endpoint para renomear os IDs externos dos seus usuários.

Você pode enviar até 50 objetos de renomeação por solicitação.

Esse endpoint define um novo `external_id` (primário) para o usuário e torna obsoleto o `external_id` existente. Isso significa que o usuário pode ser identificado por qualquer um dos `external_id` até que o obsoleto seja removido. Ter vários IDs externos permite um período de migração para que as versões legadas dos seus apps que usam o esquema de nomenclatura de ID externo anterior não sejam interrompidas. O perfil permanece totalmente funcional com ambos os identificadores durante a janela de migração — o SDK or kit de desenvolvimento de software da Braze, a REST or transferir estado representacional API or interface de programação do aplicativo (API) e os pipelines de envio de mensagens podem continuar referenciando o usuário por qualquer um dos IDs até que o obsoleto seja explicitamente removido.

Depois que o esquema de nomenclatura antigo não estiver mais em uso, é altamente recomendável remover IDs externos obsoletos usando o [endpoint `/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove).

{% alert warning %}
Remova os IDs externos obsoletos com o endpoint `/users/external_ids/remove` em vez de `/users/delete`. O envio de uma solicitação para `/users/delete` com o ID externo obsoleto exclui totalmente o perfil do usuário e não pode ser desfeito.
{% endalert %}

## Como a renomeação funciona {#how-renaming-works}

Quando você chama esse endpoint, ele atribui um novo `external_id` primário a um perfil de usuário e, ao mesmo tempo, converte o `external_id` primário anterior em um ID externo obsoleto. Após uma renomeação bem-sucedida, o perfil de usuário contém exatamente um `external_id` primário (o novo valor) e um ID externo obsoleto (o valor antigo).

Chamadas de renomeação subsequentes no mesmo perfil são permitidas: cada renomeação cria um ID externo obsoleto adicional, de modo que um perfil pode acumular um `external_id` primário e vários IDs externos obsoletos ao longo do tempo. No entanto, o valor de `new_external_id` não pode já existir em nenhum perfil da Braze, seja como ID primário ou como ID externo obsoleto.

O endpoint não registra pontos de dados e não afeta as contagens de MAU. Todos os dados históricos do usuário — eventos, compras, atributos, engajamento com Campaigns — permanecem vinculados ao mesmo perfil.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics) com a permissão `users.external_ids.rename`.

## Limite de frequência {#rate-limit}

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

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | Obrigatório | Array de objetos de renomeação de identificador externo | Veja o exemplo de solicitação e as limitações a seguir para a estrutura do objeto de renomeação do identificador externo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

Observe o seguinte:

- O `current_external_id` deve ser o ID principal do usuário e não pode ser um ID obsoleto. Se o valor informado como `current_external_id` for um ID obsoleto no perfil, a chamada falhará. Antes de tentar novamente uma renomeação que falhou, use o [endpoint `/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) para confirmar qual ID é o primário no momento.
- O `new_external_id` não deve estar em uso como ID primário ou ID obsoleto. Tentar renomear para um ID que já está armazenado como ID obsoleto retorna o erro "new_external_id is already in use".
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

- Chave de API or interface de programação do aplicativo (API) inválida
- Array `external_id_renames` vazio
- Array `external_id_renames` com mais de 50 objetos
- Limite de frequência atingido (mais de 1.000 solicitações por minuto)

## Migrações em massa {#bulk-migrations}

Para migrações que envolvem grandes populações de usuários, agrupe os usuários em lotes de até 50 e envie cada lote como uma chamada de API or interface de programação do aplicativo (API) separada. O endpoint está sujeito a um limite de frequência de 1.000 solicitações por minuto. Com o tamanho máximo de lote (50 objetos por solicitação), isso permite até 50.000 renomeações de usuários por minuto.

Cada objeto de renomeação no lote é processado de forma independente. Uma falha em um objeto não bloqueia os demais na mesma solicitação. O corpo da resposta distingue renomeações bem-sucedidas (listadas no array `external_ids`) das que falharam (listadas no array `rename_errors` com uma referência de índice à posição do objeto com falha no array da solicitação).

Ao executar migrações em massa:

1. Itere pela população completa de usuários em lotes de até 50 pares.
2. Em cada resposta, inspecione tanto `external_ids` (sucesso) quanto `rename_errors` (falha) para identificar os usuários que precisam ser reprocessados.
3. Colete os objetos com falha e agende lotes de nova tentativa separadamente. Causas comuns de falha incluem o `new_external_id` já estar em uso ou o `current_external_id` ser um ID obsoleto em vez de um ID primário.
4. Registre os sucessos e as falhas nos seus próprios registros para que o estado da migração seja rastreado fora da Braze.

## Verificando o ID externo atual {#verifying-the-current-external-id}

Durante uma migração, pode ser necessário confirmar qual ID externo é o identificador primário ativo em um determinado perfil — por exemplo, ao verificar se um usuário específico já foi migrado ou ao solucionar problemas de uma renomeação que falhou. Use o [endpoint `/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) para esse fim.

O endpoint de exportação resolve tanto IDs externos primários quanto obsoletos para o mesmo perfil subjacente e sempre retorna o `external_id` primário atual na resposta. Isso significa que você pode consultar qualquer identificador conhecido de um usuário — antigo ou novo — e a resposta conterá o ID primário canônico. Essa é uma forma confiável de determinar o estado da migração.

Para verificar apenas o ID externo (em vez de obter o perfil completo), passe `fields_to_export` com apenas o campo `external_id`.

## Fluxo de trabalho de migração recomendado {#recommended-migration-workflow}

Para a maioria dos casos de uso de migração, a sequência recomendada é:

1. **Teste em staging** — Execute o fluxo completo de renomeação e verificação em um espaço de trabalho de desenvolvimento ou staging antes de alterar a produção.
2. **Renomeie em lotes** — Use o endpoint `/users/external_ids/rename` em lotes de até 50, tratando os `rename_errors` em cada resposta e enfileirando os pares com falha para nova tentativa.
3. **Verifique** — Após cada lote (ou ao final da migração), faça verificações pontuais nos perfis usando `/users/export/ids` para confirmar que o `external_id` primário esperado está definido.
4. **Mantenha a janela de descontinuação** — Mantenha os IDs externos obsoletos ativos pelo tempo necessário enquanto qualquer sistema (incluindo versões legadas do app em campo) ainda puder referenciar os IDs antigos. Não apresse essa etapa.
5. **Remova os IDs obsoletos** — Quando todos os sistemas estiverem confirmados como usando os novos IDs, use o endpoint [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) em lotes de até 50 para fazer a limpeza.

Se você também estiver migrando sua integração SDK or kit de desenvolvimento de software (por exemplo, alterando o valor passado para `changeUser`), coordene a renomeação via API or interface de programação do aplicativo (API) com o cronograma de lançamento do app para que o novo ID externo esteja em uso tanto no servidor quanto no cliente antes que os IDs obsoletos sejam removidos.

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
Não temos um limite rígido de quanto tempo você pode manter IDs externos obsoletos, mas é altamente recomendável removê-los quando não houver mais necessidade de referenciar os usuários pelo ID obsoleto.

### Quantos IDs externos obsoletos um perfil pode ter? {#how-many-deprecated-external-ids-can-a-profile-have}
Um perfil de usuário pode ter um `external_id` primário e qualquer quantidade de IDs externos obsoletos acumulados por meio de operações de renomeação sucessivas. Não há um limite documentado para o número de IDs obsoletos que um único perfil pode ter, mas a Braze recomenda removê-los assim que não forem mais necessários.

{% endapi %}