---
nav_title: Comportamento de mesclagem
article_title: Comportamento de mesclagem de usuários
page_order: 1
page_type: reference
description: "Saiba como a Braze lida com a mesclagem de usuários marcados para exclusão, usuários teste e usuários do Grupo de controle global."
---

# Comportamento de mesclagem de usuários {#user-merge-behavior}

> Saiba como a Braze lida com a mesclagem de usuários, incluindo os três tipos de usuários em que o comportamento padrão não se aplica: usuários marcados para exclusão, usuários teste e usuários do Grupo de controle global.

Esse comportamento se aplica a todas as mesclagens, seja usando [mesclagem individual]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users#individual-merging), [mesclagem em massa]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users#bulk-merging) ou o [endpoint da API Merge users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge).

## Comportamento geral de mesclagem {#general-merge-behavior}

Quando você mescla dois perfis de usuário, a Braze preenche os campos vazios no perfil a ser mantido com os valores do perfil a ser mesclado. Se um campo tiver um valor em ambos os perfis, a Braze preserva o valor do perfil a ser mantido.

Por exemplo, se um valor existe apenas em um dos perfis, a Braze o mantém:

| Campo | Perfil a ser mesclado | Perfil a ser mantido | Perfil resultante |
|---|---|---|---|
| `first_name` | Alex | (vazio) | Alex |
| `last_name` | (vazio) | Sterling | Sterling |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

Se ambos os perfis tiverem um valor para o mesmo campo, a Braze mantém o valor do perfil a ser mantido:

| Campo | Perfil a ser mesclado | Perfil a ser mantido | Perfil resultante |
|---|---|---|---|
| `first_name` | Alex | Al | Al |
| `last_name` | (vazio) | Sterling | Sterling |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

Esse comportamento funciona bem para atributos padrão e personalizados. No entanto, a Braze lida com os seguintes tipos de usuários de forma diferente.

## Resumo do comportamento {#behavior-summary}

| Tipo de usuário | Comportamento | Motivo |
|---|---|---|
| Usuários marcados para exclusão | Não mesclar | Perfis marcados para exclusão são excluídos em até 7 dias, então seus dados não precisam ser preservados. |
| Usuários teste | Mesclar, com o status de usuário teste preservado | Manter o status de usuário teste ajuda a preservar uma população de testes utilizável após a mesclagem. |
| Usuários do Grupo de controle global | Não mesclar | A mesclagem alteraria os números de bucket aleatórios, o que afetaria experimentos e relatórios. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Usuários marcados para exclusão {#users-marked-for-deletion}

Quando você usa a [ferramenta de exclusão de usuários em massa]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users) para excluir um Segment, a Braze marca esses perfis de usuário para exclusão nos próximos 7 dias. A Braze não mescla perfis marcados para exclusão, seja o perfil a ser mantido ou o perfil a ser mesclado.

Se você precisar mesclar um perfil marcado para exclusão, primeiro [cancele a exclusão do Segment]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users#cancel) ou remova o usuário da exclusão para que o perfil não esteja mais marcado.

## Usuários teste {#test-users}

A Braze permite que perfis de usuários teste sejam mesclados e preserva o status de usuário teste no perfil resultante. Isso difere do [comportamento geral de mesclagem](#general-merge-behavior), que normalmente manteria o valor do perfil a ser mantido.

A tabela a seguir mostra o status de usuário teste resultante para cada combinação:

| Perfil a ser mesclado | Perfil a ser mantido | Perfil resultante |
|---|---|---|
| Não é usuário teste | Não é usuário teste | Não é usuário teste |
| Usuário teste | Usuário teste | Usuário teste |
| Usuário teste | Não é usuário teste | Usuário teste |
| Não é usuário teste | Usuário teste | Usuário teste |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para saber mais sobre usuários teste, consulte [Grupos internos]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups).

## Usuários do Grupo de controle global {#global-control-group-users}

A Braze não mescla perfis de usuário em um [Grupo de controle global]({{site.baseurl}}/user_guide/audience/global_control_group), seja o perfil a ser mantido ou o perfil a ser mesclado.

A participação no Grupo de controle global é determinada pelo [número de bucket aleatório]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) do usuário. A mesclagem alteraria quais usuários pertencem ao grupo, o que afetaria seus experimentos e relatórios.

## Artigos relacionados {#related-articles}

- [Mesclar usuários duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)
- [POST: Merge users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)
- [Excluir usuários]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users)
- [Grupo de controle global]({{site.baseurl}}/user_guide/audience/global_control_group)
- [Números de bucket aleatórios]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)
- [Grupos internos]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups)