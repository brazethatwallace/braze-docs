---
nav_title: Excluir usuários
article_title: Excluir usuários
page_order: 6
toc_headers: h2
description: "Saiba como excluir um usuário individual ou um segmento de usuários diretamente pelo dashboard da Braze."
alias: /delete_users/
---

# Excluir usuários {#delete-users}

> Saiba como excluir um usuário individual ou um segmento de usuários diretamente pelo dashboard da Braze.

{% alert important %}
A exclusão de usuários está atualmente em acesso antecipado. Fale com seu gerente de sucesso do cliente se tiver interesse em participar.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para excluir usuários, você precisa ser administrador ou ter a permissão **Delete Users**. Para visualizar registros de exclusão de usuários, você precisa ser administrador ou ter a permissão **View User Deletion Records**. As seguintes permissões controlam a exclusão de usuários e os registros de exclusão:

| Permissão | Descrição |
|------------|-------------|
| Delete Users | Exclui permanentemente usuários de forma individual ou em massa. |
| View User Deletion Records | Visualiza registros de exclusão de usuários. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Sobre a exclusão de usuários {#about-user-deletion}

A exclusão de usuários permite gerenciar seu banco de dados removendo perfis que não são mais necessários, foram criados por engano ou precisam ser excluídos por conformidade (como GDPR ou CCPA).

| Consideração | Informações |
|---------------|---------|
| Tamanho máximo | Você pode excluir até 100 milhões de perfis de usuários ao excluir um segmento. |
| Período de espera | Todas as exclusões de segmentos exigem um período de espera de 7 dias, mais o tempo necessário para processar as exclusões. |
| Limite de tarefas | Apenas um segmento pode ser excluído por vez, o que inclui o período de espera de 7 dias. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sobre a exclusão de usuários" }

## Excluindo usuários {#deleting-users}

Você pode excluir um [usuário individual](#delete-individual) ou um [segmento de usuários](#delete-segment) pelo dashboard da Braze:

### Excluindo um usuário individual {#delete-individual}

Para excluir um usuário individual da Braze, acesse **Audience** > **Search Users** e pesquise e selecione um usuário. Se você estiver excluindo um perfil de usuário duplicado, verifique se selecionou o correto.

![A página "Search Users" na Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Exclusões de usuários individuais são permanentes — os perfis não podem ser recuperados após a exclusão.
{% endalert %}

Na página do perfil, selecione <i class="fa-solid fa-ellipsis-vertical"></i> **Show options** > **Delete User**. Lembre-se de que pode levar alguns minutos para que o usuário seja totalmente excluído na Braze.

![Um usuário na Braze com o menu de reticências verticais aberto, mostrando a opção de excluir o usuário.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Excluindo um segmento {#delete-segment}

Se ainda não fez isso, [crie um segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/) contendo os perfis de usuários que você deseja excluir. Certifique-se de incluir todos os perfis de usuários se estiver excluindo usuários duplicados.

Na Braze, acesse **Audience** > **Manage Audience** e selecione a guia **Delete Users**.

![A guia "Delete Users" na seção "Manage Audience" do dashboard da Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Selecione **Delete users**, escolha o segmento que deseja excluir e selecione **Next**.

![Uma janela pop-up com um segmento escolhido para exclusão.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Digite **DELETE** para confirmar sua solicitação e selecione **Delete users**.

![A página de confirmação com "DELETE" digitado na caixa de confirmação.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Os usuários neste segmento não serão excluídos imediatamente. Em vez disso, serão marcados como pendentes de exclusão pelos próximos 7 dias. Após esse período, eles serão excluídos e enviaremos um e-mail para informá-lo.

{% alert tip %}
Para garantir que exatamente esses usuários sejam excluídos independentemente de alterações no segmento, um filtro de segmento chamado **Pending Deletion** é criado automaticamente. Você pode [usar esse filtro]({{site.baseurl}}/user_guide/audience/segments/managing_segments/#filters) para verificar o status das exclusões pendentes.
{% endalert %}

## Confirmando exclusões de segmentos {#confirming-segment-deletions}

A Braze envia um e-mail de confirmação com o número de perfis pendentes de exclusão.

Para prosseguir com a exclusão, faça login na Braze e confirme a solicitação de exclusão.

Se você não confirmar dentro do prazo indicado no e-mail, a solicitação de exclusão expira e não é processada.

## Cancelando exclusões de segmentos {#cancel}

Você tem 7 dias para cancelar exclusões de segmentos pendentes. Para cancelar, acesse **Audience** > **Manage Audience** e selecione a guia **Delete Users**.

![A guia "Delete Users" na seção "Manage Audience" do dashboard da Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Ao lado de uma exclusão de segmento pendente, selecione <i class="fa-solid fa-eye"></i> **Ver informações** para abrir os detalhes do registro de exclusão.

![Uma exclusão de segmento pendente na guia "Delete Users".]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

Nos detalhes do registro de exclusão, selecione **Cancel deletion**.

![A janela "Deletion Record Details" na guia "Delete Users".]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Quando a exclusão em massa de usuários está em andamento, você pode cancelá-la a qualquer momento. No entanto, os usuários já excluídos antes do cancelamento não podem ser restaurados.
{% endalert %}

## Verificando o status da exclusão {#status}

Você pode verificar o status de uma exclusão usando [filtros de segmento](#segment-filters), a página [Gerenciar público](#manage-audience) ou [relatórios de eventos de segurança](#security-event-report).

### Filtros de segmento {#segment-filters}

Quando você solicita a exclusão de um segmento de usuários, um [filtro de segmento]({{site.baseurl}}/user_guide/audience/segments/managing_segments/#filters) chamado **Pending Deletion** é criado automaticamente. Você pode usá-lo para:

- Ver o conjunto exato de usuários vinculados a uma data de execução de exclusão específica.
- Excluir esses usuários de Campaigns para que não recebam mensagens antes da remoção.
- Exportar a lista caso precise para conformidade ou manutenção de registros.

### Gerenciar público {#manage-audience}

{% alert note %}
Para obter a lista exata de usuários que serão excluídos, use o [filtro de segmento Pending Deletion](#segment-filters).
{% endalert %}

Acesse **Audience** > **Manage Audience** e selecione a guia **Delete Users**.

![A guia "Delete Users" na seção "Manage Audience" do dashboard da Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Nesta página, você encontra as seguintes informações gerais para todas as exclusões atuais e pendentes:

| Campo | Descrição |
|-------|-------------|
| Data da solicitação | A data em que a solicitação foi feita originalmente. Use-a com o filtro **Pending Deletion** para obter a lista de perfis pendentes de exclusão. |
| Solicitante | O usuário que iniciou a solicitação de exclusão. |
| Nome do segmento | O nome do segmento usado para selecionar os usuários pendentes de exclusão. |
| Status | Indica se a solicitação de exclusão está pendente, em andamento ou concluída. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gerenciar público" }

Para mais detalhes sobre uma solicitação específica, selecione <i class="fa-solid fa-eye"></i> **Ver informações** para exibir os detalhes do registro de exclusão. Aqui você também pode [cancelar exclusões de segmentos pendentes](#cancel).

![Uma exclusão de segmento pendente na guia "Delete Users".]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Relatório de eventos de segurança {#security-event-report}

Você também pode verificar o status de exclusões anteriores baixando um relatório de eventos de segurança. Para saber mais, consulte [Configurações de segurança]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report).

## Perguntas frequentes {#faq}

### Posso excluir segmentos com mais de 100 milhões de usuários? {#can-i-delete-segments-with-more-than-100-million-users}

Não. Você não pode excluir segmentos com mais de 100 milhões de usuários. Se precisar de ajuda para excluir um segmento desse tamanho, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support/).

### Parece que não consigo excluir 100 milhões de usuários e estou limitado a excluir apenas 10 milhões. Isso é um bug? {#it-looks-like-i-am-not-able-to-delete-100-million-users-and-am-limited-to-deleting-only-10-million-is-this-a-bug}

Não, isso não é um bug. Alguns clientes têm um limite no número de usuários que podem excluir durante o programa de acesso antecipado (EA).

À medida que o programa de EA avança, essa capacidade é projetada para aumentar até que todos os clientes possam excluir até 100 milhões de usuários.

Se quiser aumentar essa capacidade, entre em contato com seu gerente de conta da Braze. As solicitações são concedidas a critério da equipe de produto.

### A mesclagem automatizada de usuários afeta a exclusão de usuários? {#does-automated-user-merging-affect-user-deletion}

Se uma mesclagem agendada incluir perfis de usuários pendentes de exclusão, a Braze ignora esses perfis e não os mescla. Para mesclar esses perfis, você precisa removê-los da exclusão.

### O que acontece com os dados enviados para usuários pendentes de exclusão? {#what-happens-to-data-sent-to-users-pending-deletion}

Os dados enviados por sistemas externos ou SDKs ainda são aceitos, mas os usuários serão excluídos conforme programado, independentemente da atividade.

### Canvas e Campaigns são disparados para usuários pendentes de exclusão? {#do-canvases-and-campaigns-trigger-for-users-pending-deletion}

Sim. No entanto, você pode adicionar um filtro de inclusão de segmento para excluir todos os usuários com o [filtro de segmento](#segment-filters) **Pending Deletion**.

### Posso recuperar perfis de usuários excluídos? {#can-i-recover-deleted-user-profiles}

Exclusões de usuários individuais são permanentes.

Você pode [cancelar exclusões de segmentos](#cancel) dentro dos primeiros 7 dias. No entanto, os usuários já excluídos antes do cancelamento não podem ser restaurados.

### Posso excluir usuários pela API em vez do dashboard? {#can-i-delete-users-with-the-api-instead-of-the-dashboard}

Sim. Para lotes menores, você pode usar o [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/), que aceita até 50 identificadores por solicitação e está sujeito ao [limite de taxa]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/#rate-limit) desse endpoint. A exclusão de segmentos pelo dashboard é mais adequada para públicos muito grandes, mas inclui o [período de espera de 7 dias](#about-user-deletion).