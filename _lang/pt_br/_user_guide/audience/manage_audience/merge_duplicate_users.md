---
nav_title: Mesclar usuários duplicados
article_title: Mesclar usuários duplicados
description: "Saiba como encontrar e mesclar usuários duplicados no dashboard da Braze."
page_order: 4
---

# Mesclar usuários duplicados {#merge-duplicate-users}

> Saiba como encontrar e mesclar usuários duplicados para maximizar a eficácia das suas Campaigns e Canvas.

## REST API: identificar e mesclar usuários {#rest-api-identify-and-merge-users}

As ferramentas nesta página mesclam perfis duplicados no dashboard. Você também pode combinar ou redirecionar perfis por meio dos [endpoints de dados de usuários]({{site.baseurl}}/api/endpoints/user_data) da Braze:

- [POST: Identificar usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) (`/users/identify`): Combina um perfil somente com alias, somente com e-mail ou somente com número de telefone com um perfil que tenha um `external_id`.
- [POST: Mesclar usuários]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) (`/users/merge`): Mescla um perfil de usuário em outro, inclusive quando ambos os perfis já possuem um `external_id`. Revise os [Pré-requisitos]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#prerequisites) e o [Comportamento de mesclagem]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) antes de chamar esse endpoint.

Quando um perfil anônimo é associado a um perfil identificado existente (por exemplo, por meio de uma chamada `changeUser()` do SDK ou `/users/identify`), a Braze descarta o perfil anônimo e copia apenas determinados campos para o perfil identificado. Para saber mais, consulte [O que acontece quando você identifica usuários anônimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).

Mesclagens de usuários são difíceis de desfazer. Se você está planejando uma mesclagem complexa envolvendo múltiplos valores de `external_id` ou grandes migrações de perfis, entre em contato com seu CSM da Braze para orientação antes de usar `/users/merge`.

A Braze trata três tipos de usuários de forma diferente ao mesclar: usuários marcados para exclusão, usuários teste e usuários do Grupo de controle global. Para mais informações, consulte [Comportamento de mesclagem de usuários]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior).

## Mesclagem individual {#individual-merging}

Se uma pesquisa de usuários retornar perfis duplicados, você pode mesclar cada perfil individualmente a partir do perfil do usuário no dashboard da Braze.

### Etapa 1: Pesquisar um perfil duplicado {#step-1-search-for-a-duplicate-profile}

Na Braze, selecione **Audience** > **User Search**.

![O bloco "User Search" destacado no menu de navegação.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

Insira um identificador único, como um endereço de e-mail ou número de telefone, para o perfil duplicado e selecione **Search**.

![A página "User Search" no dashboard da Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### Etapa 2: Mesclar duplicados {#step-2-merge-duplicates}

Para iniciar o processo de mesclagem, selecione **Merge duplicates**.

![Um dos perfis de usuário duplicados.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

Escolha qual perfil de usuário manter e qual mesclar e selecione **Merge profiles**. Repita esse processo até que todos os perfis duplicados tenham sido mesclados.


{% alert warning %}
Perfis de usuários duplicados não podem ser recuperados após a mesclagem.
{% endalert %}

## Mesclagem em massa {#bulk-merging}

Quando você mescla usuários duplicados em massa, a Braze encontra perfis com identificadores correspondentes (como um endereço de e-mail) e mantém um perfil. A Braze primeiro prioriza perfis com um `external_id` e, em seguida, aplica suas configurações de **Resolving ties**: **Resolve ties using** e **Prioritization**. Se não houver perfis com um `external_id`, a Braze usa **Resolve ties using** e **Prioritization** entre perfis sem um `external_id`. A Braze só mescla usuários quando essas configurações identificam um perfil a ser mantido. Por exemplo, se **Resolve ties using** for **Updated date** e ambos os perfis tiverem o mesmo timestamp de última atualização, a Braze não consegue resolver o empate, então esses usuários não são mesclados.

### Etapa 1: Acessar Gerenciar público {#step-1-go-to-manage-audience}

No dashboard da Braze, selecione **Audience** > **Manage Audience**.

![O bloco "Manage Audience" destacado no menu de navegação.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### Etapa 2: Pré-visualizar os resultados (opcional) {#step-2-preview-the-results-optional}

Para pré-visualizar os resultados antes de mesclar os duplicados, selecione **Generate list of duplicates**.

![A página "Manage Audience" com "Generate list of duplicates" destacado.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

A Braze gerará a pré-visualização e a enviará para o seu endereço de e-mail como um arquivo CSV.

O arquivo CSV inclui uma coluna **Created from** que mostra como cada perfil foi criado inicialmente (por exemplo, por meio do [SDK]({{site.baseurl}}/developer_guide/sdk_integration), da [REST API]({{site.baseurl}}/api/basics) ou de uma [importação CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)). Isso ajuda a entender a origem do perfil antes de mesclar duplicados.

Ao revisar as linhas duplicadas, compare **Created from** com identificadores como `external_id`, endereço de e-mail e número de telefone. Use esse contexto para decidir qual perfil deve ser mantido como perfil principal antes de selecionar **Merge all duplicates**.

O campo **Created from** é especialmente útil quando perfis duplicados contêm valores semelhantes, mas vêm de caminhos de ingestão diferentes. Ele fornece mais contexto para decisões de mesclagem e ajuda a reduzir mesclagens acidentais de perfis que você preferiria manter separados até uma análise mais detalhada.


No exemplo a seguir, a Braze usa o ID externo do usuário para sinalizar perfis duplicados e identificar qual deve ser mantido. Se esses perfis forem mesclados em massa, a Braze usará o perfil com um ID externo como o novo perfil principal do usuário.

{% tabs local %}
{% tab example csv file %}
| Email Address    | External ID | Phone Number   | Braze ID              | Identifier for rule | Created from | Profile to keep | Profile to merge |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | ------------ | --------------- | ---------------- |
| jane.doe@example.com   | 123-external-id | 555 123-4567 | example-id-12345 | email               | sdk          | TRUE            | FALSE            |
| john.doe@example.com   |                 | 555 123-4567 | example-id-12346 | email               | rest         | FALSE           | TRUE             |
| jordan.doe@example.com |                 | 555 123-4567 | example-id-12347 | email               | csv          | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 2: Pré-visualizar os resultados (opcional)" }
{% endtab %}
{% endtabs %}

#### Comportamento de mesclagem {#merge-behavior}

A Braze preencherá os campos vazios no perfil mantido com valores do perfil mesclado. Para ver a lista de campos que serão preenchidos, consulte [Comportamento de mesclagem]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

### Etapa 3: Mesclar os duplicados {#step-3-merge-your-duplicates}

Se estiver satisfeito com os resultados da pré-visualização, selecione **Merge all duplicates**.

{% alert warning %}
Perfis de usuários duplicados não podem ser recuperados após a mesclagem.
{% endalert %}


## Mesclagem baseada em regras {#rules-based-merging}

Você pode usar regras para controlar como os perfis duplicados são resolvidos ao executar uma mesclagem, garantindo que o perfil de usuário mais relevante seja mantido. Quando as regras são definidas, a Braze manterá os perfis que correspondem aos seus critérios.

### Etapa 1: Definir suas regras {#step-1-define-your-rules}

1. Acesse **Audience** > **Manage Audience** > **Edit rules**.
2. Na seção **Profile to keep** do painel **Edit rules**, selecione o **Identifier** para os perfis que serão mantidos ao mesclar duplicados. Pode ser o endereço de e-mail ou o número de telefone.
3. Na seção **Resolving ties**, selecione os critérios para determinar como resolver empates entre perfis com critérios correspondentes de **Profile to keep**. Você pode selecionar o seguinte:<br>
- **Resolve ties using**: Created date, Updated date, Last session
- **Prioritization**: Newest, Oldest

![O painel "Edit rules" com seções para selecionar opções de "Profile to keep" e "Resolving ties".]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

Por exemplo, você pode manter o perfil que tem um número de telefone. Se vários usuários tiverem o mesmo número de telefone, você pode resolver empates usando o campo **Updated date** e priorizar o usuário atualizado mais recentemente.

### Etapa 2: Pré-visualizar os resultados (opcional)

Após salvar suas regras, você pode pré-visualizar como elas funcionarão selecionando **Generate a list of duplicates**. A Braze gerará a pré-visualização e a enviará para o seu endereço de e-mail como um arquivo CSV que mostra quais usuários seriam mantidos e mesclados se suas regras fossem aplicadas.

### Etapa 3: Mesclar duplicados {#step-3-merge-duplicates}

Se estiver satisfeito com os resultados da pré-visualização, volte à página **Manage Audience** e selecione **Merge all duplicates**.

{% alert warning %}
Perfis de usuários duplicados não podem ser recuperados após a mesclagem.
{% endalert %}

## Mesclagem programada {#scheduled-merging}

Semelhante à mesclagem baseada em regras, a mesclagem programada permite automatizar a mesclagem de perfis de usuários diariamente usando regras pré-configuradas.

![A página "Manage Audience" com o botão "schedule".]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

Após a ativação do recurso, a Braze atribuirá automaticamente um horário para executar o processo de mesclagem diariamente, por volta das 0h no fuso horário da empresa do usuário. Você pode desativar a mesclagem programada a qualquer momento. A Braze notificará os administradores do seu espaço de trabalho 24 horas antes da mesclagem programada, fornecendo um lembrete e tempo para revisar a configuração.

{% alert warning %}
Perfis de usuários duplicados não podem ser recuperados após a mesclagem.
{% endalert %}

## Por que vários perfis de usuário estão associados ao mesmo endereço de e-mail? {#why-are-multiple-user-profiles-associated-with-the-same-email-address}

A Braze armazena vários perfis de usuário que compartilham o mesmo endereço de e-mail quando os perfis são criados por meio de diferentes identificadores, importações ou sessões anônimas antes da identificação. Esse é o comportamento esperado quando os usuários não compartilham um único `external_id`.

Antes de mesclar duplicados, use o [endpoint Exportar perfil de usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) para confirmar quais perfis existem para um endereço de e-mail e quais campos cada perfil contém. Você também pode pesquisar por e-mail em **Audience** > **User Search** para revisar duplicados no dashboard.

## Artigos relacionados {#related-articles}

- [Comportamento de mesclagem de usuários]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior)
- [POST: Mesclar usuários]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)
- [Excluir usuários]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users)