---
nav_title: Permissões
article_title: "Permissões da Braze"
page_order: 1
page_type: reference
alias: /braze_permissions/
description: "Este artigo de referência aborda como as permissões de usuário funcionam na Braze. Aqui, você pode aprender a editar e definir permissões de usuário, escolhendo quem pode acessar."
tool: Dashboard
---

# Permissões da Braze {#braze-permissions}

> Saiba como criar conjuntos de permissões, criar papéis, editar permissões de usuário e exportar permissões de usuário, para garantir que seus usuários acessem apenas os espaços de trabalho e recursos de que mais precisam.
>
> {% multi_lang_include video.html id="nv699nw706" source="wistia" %}

## Criar um conjunto de permissões {#create-a-permission-set}

Use conjuntos de permissões para agrupar permissões relacionadas a áreas de assunto ou ações específicas. Você pode aplicar conjuntos de permissões a usuários do dashboard que precisam do mesmo acesso em diferentes espaços de trabalho. Para criar um conjunto de permissões, acesse **Configurações** > **Gerenciamento de Usuários** > **Conjuntos de Permissões** e selecione **Criar conjunto de permissões**. Para ver a descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab exemplos de conjuntos de permissões %}
| Nome | Permissões |
|-----------|----------------|
| Desenvolvedores | "View API Keys", "Edit API Keys", "View Internal Groups", "Edit Internal Groups", "View Message Activity Log", "View Event User Log", "View API identifiers", "View API Usage Dashboard", "View API Limits", "View API Usage Alerts", "Edit API Usage Alerts", "View SDK Debugger", "Edit SDK Debugger". |
| Profissionais de marketing | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Frequency Capping Rules", "Edit Frequency Capping Rules", "View Message Prioritization", "Edit Message Prioritization", "View Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "Edit Global Control Group", "View IAM Templates", "Edit IAM Templates", "Archive IAM Templates", "View Email Templates", "Edit Email Templates", "Archive Email Templates", "View Webhook Templates", "Edit Webhook Templates", "Archive Webhook Templates", "View Email Link Templates", "Edit Email Link Templates", "View Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers", "Edit Dashboard Reports", "View Banner Templates", "View Localization Settings", "Use Operator", "View Decisioning Studio Agents". |
| Gerenciamento de usuários | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemplo de conjunto de permissões" }
{% endtab %}
{% endtabs %}

## Criando um papel {#creating-a-role}

Os papéis permitem mais estrutura ao agrupar suas permissões personalizadas individuais com controles de acesso ao espaço de trabalho. Isso é especialmente útil quando você tem muitas marcas ou espaços de trabalho regionais em um único dashboard. Com os papéis, você pode adicionar usuários do dashboard aos espaços de trabalho apropriados e conceder diretamente as permissões associadas. Para criar um papel, acesse **Configurações** > **Gerenciamento de Usuários** > **Papéis** e selecione **Criar papel**. Para ver a descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab exemplos de papéis %}
| Nome do papel | Espaço de trabalho | Permissões |
| ----------- | ----------- | --------- |
| Profissional de marketing - Marcas de moda | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Profissional de marketing - Marcas de skincare | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Gerenciamento de usuários - Todas as marcas | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Exemplos de papéis" }
{% endtab %}
{% endtabs %}

## Como os conjuntos de permissões e os papéis diferem das Equipes? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions/differences.md content="Differences" %}

### Considerações ao adicionar permissões de usuário a Equipes {#considerations-for-adding-user-permissions-to-teams}

Você pode encontrar dificuldades ao tentar salvar permissões no dashboard da Braze, especialmente ao adicionar ou remover usuários de um espaço de trabalho ou ao adicioná-los a uma Equipe. O botão **Save/Update Users** pode ficar esmaecido se as permissões do usuário forem idênticas às que ele já possui no nível do espaço de trabalho. Essa restrição existe porque não há benefício em ter uma Equipe se todos os usuários possuem as mesmas permissões de todo o espaço de trabalho.

Para adicionar um usuário a uma Equipe com sucesso e manter as mesmas permissões, não atribua nenhuma permissão no nível do espaço de trabalho. Em vez disso, atribua permissões exclusivamente no nível da equipe.

## Usuários limitados {#limited-users}

Usuários limitados têm permissões específicas que permitem gerenciar determinados aspectos do dashboard da Braze, mas com restrições em comparação aos administradores da empresa e administradores do espaço de trabalho.

| Escopo | Descrição |
| --- | --- |
| Permissões | Usuários limitados podem editar as permissões de outros usuários limitados se tiverem a permissão "Edit Dashboard Users". Eles também podem criar novos usuários limitados e modificar seus conjuntos de permissões. No entanto, não podem criar ou gerenciar contas de administrador da empresa. |
| Limitações de papéis | Se um usuário limitado tiver todas as permissões, exceto "Workspace Admin", ele ainda terá acesso a todas as outras permissões normalmente concedidas a um administrador do espaço de trabalho. |
| Visibilidade de permissões | Se um usuário limitado tiver a permissão "Edit Dashboard Users" para um espaço de trabalho (como Dev), mas não para outro (como Prod), ele não verá as permissões do espaço de trabalho Prod na página de detalhes dos usuários do dashboard. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permissões para usuários limitados" }

### Comparar usuários limitados {#compare-limited-users}

| Tipo de usuário limitado | Descrição |
| --- | --- |
| Administrador do espaço de trabalho | Administradores do espaço de trabalho têm permissões específicas para gerenciar espaços de trabalho, mas não possuem a mesma autoridade que administradores da empresa. Usuários limitados podem herdar permissões semelhantes às de administradores do espaço de trabalho se tiverem as permissões necessárias marcadas. |
| Administrador (Administrador da empresa) | Administradores da empresa têm permissões mais amplas, incluindo a capacidade de excluir usuários do dashboard. No entanto, eles não podem excluir suas próprias contas e devem entrar em contato com outro administrador da empresa para essa ação. |
| Acesso somente leitura | Para acessar partes do dashboard, como a página de Campaigns, os usuários devem ter permissões de visualização atribuídas a eles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparação de usuários limitados" }

### Erro de acesso limitado {#limited-access-error}

Os usuários podem encontrar mensagens como "You need 'View Landing Pages' permissions to access this page". Nesses casos, o usuário e o administrador da conta devem verificar se as permissões necessárias foram concedidas. Se já estiverem, tente resolver o problema desativando e depois reativando as permissões do usuário.

{% alert note %}
Não é possível mesclar ou importar permissões de usuário de um usuário do dashboard para outro.
{% endalert %}

## Nuances das permissões de usuário {#nuances-of-user-permissions}

Tenha em mente os seguintes comportamentos ao atribuir acesso ao dashboard:

- **Administrador do espaço de trabalho versus Administrador da empresa:** Os Administradores de espaço de trabalho gerenciam permissões dentro dos espaços de trabalho atribuídos. Os Administradores da empresa têm autoridade em toda a empresa, incluindo a exclusão de outros usuários do dashboard.
- **Usuários limitados:** Usuários limitados com a permissão "Editar usuários do dashboard" podem gerenciar outros usuários limitados, mas não podem criar ou gerenciar contas de Administrador da empresa.
- **Escopo de Gerenciar usuários do dashboard:** Na página de detalhes do usuário, as permissões aparecem apenas para os espaços de trabalho aos quais o editor tem acesso. Um usuário limitado que pode editar usuários em um espaço de trabalho pode não visualizar as caixas de seleção de permissões de outro espaço de trabalho.
- **Botão Atribuir permissões:** Ao editar um usuário que já possui permissões no nível do espaço de trabalho ou conjuntos de permissões para todos os espaços de trabalho que você pode gerenciar, o botão **Atribuir permissões** desaparece. Isso acontece porque não há espaços de trabalho adicionais para atribuir no nível do espaço de trabalho.
- **Exportar dados de usuários:** Exportar dados de usuários requer acesso no nível do espaço de trabalho, além da permissão de exportação.
- **Permissões compostas:** Algumas áreas exigem múltiplas permissões. Por exemplo, configurar [parceiros de tecnologia]({{site.baseurl}}/partners) normalmente requer tanto o acesso ao parceiro quanto uma permissão básica de leitura para os recursos relacionados do espaço de trabalho.
- **Importar e atualizar dados de usuários:** Essa permissão inclui a capacidade de editar perfis de usuários do app por meio de fluxos de importação, e não apenas registros de usuários do dashboard.

## Editar permissões de um usuário {#edit-a-users-permissions}

Para editar as permissões atuais de administrador, empresa ou espaço de trabalho de um usuário, acesse **Configurações** > **Gerenciamento de Usuários** > **Usuários da Empresa** e selecione o nome do usuário.

![A página "Usuários da Empresa" na Braze mostrando uma tabela de usuários do dashboard.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Administrador %}

### Administrador {#admin}

Os administradores têm acesso a todos os recursos e a capacidade de modificar qualquer configuração da empresa. Eles podem:

- Alterar [configurações de aprovação]({{site.baseurl}}/user_guide/messaging/governance/approvals#turning-on-the-approval-workflow)
- Adicionar, editar, excluir, suspender ou reativar outros [usuários da Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#adding-company-users)
- Exportar usuários da Braze como um arquivo CSV

Para conceder ou remover privilégios de administrador, selecione **Este usuário é um administrador** e, em seguida, selecione **Atualizar usuário**.

{% alert warning %}
Se você remover os privilégios de administrador de um usuário, ele não poderá acessar a Braze até que você atribua a ele pelo menos uma [permissão no nível da empresa ou do espaço de trabalho]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Empresa %}

### Empresa {#company}

Para gerenciar as permissões no nível da empresa de um usuário, marque ou desmarque a caixa ao lado da permissão correspondente. Quando terminar, selecione **Atualizar usuário**.

|Nome da permissão|Descrição|
|----------|-----------|
|Gerenciar configurações da empresa|Permite que os usuários modifiquem configurações de permissão e verificação de remetente.|
|Criar e excluir espaços de trabalho|Permite que os usuários criem e excluam espaços de trabalho.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permissões no nível da empresa" }

{% endtab %}
{% tab Espaço de trabalho %}

### Espaço de trabalho {#workspace}

Você pode conceder a um usuário permissões diferentes para cada espaço de trabalho ao qual ele pertence na Braze. Para gerenciar as permissões no nível do espaço de trabalho, selecione **Selecionar espaços de trabalho e permissões** e escolha as permissões manualmente ou atribua um [conjunto de permissões ou papel]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#create-a-permission-set) criado anteriormente. Se precisar conceder a um usuário permissões diferentes para espaços de trabalho distintos, repita esse processo quantas vezes for necessário. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% subtabs %}
{% subtab Selecionar manualmente %}

Em **Espaços de trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Permissões**, selecione uma ou mais permissões. Elas serão atribuídas apenas para os espaços de trabalho que você selecionou. Opcionalmente, você pode selecionar **Atribuir acesso de administrador do espaço de trabalho** se quiser conceder permissões completas para esse espaço de trabalho.

Quando terminar, selecione **Atualizar usuário**.

![Permissões no nível do espaço de trabalho sendo selecionadas manualmente na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Atribuir conjunto de permissões %}

Em **Espaços de trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Conjuntos de permissões**, escolha um conjunto de permissões. Elas serão atribuídas apenas para os espaços de trabalho que você selecionou.

Quando terminar, selecione **Atualizar usuário**.

![Permissões no nível do espaço de trabalho sendo atribuídas por meio de um conjunto de permissões na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Atribuir papel %}

Em **Espaços de trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Papel**, escolha um papel. Elas serão atribuídas apenas para os espaços de trabalho que você selecionou.

Quando terminar, selecione **Atualizar usuário**.

![Permissões no nível do espaço de trabalho sendo atribuídas por meio de um papel na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportando permissões de usuários {#exporting-user-permissions}

Para baixar uma lista dos seus usuários e suas permissões, acesse **Configurações** > **Gerenciamento de Usuários** > **Usuários da Empresa** e selecione **Exportar Usuários**. Um arquivo CSV será enviado para o seu endereço de e-mail em breve.

## Lista de permissões {#list-of-permissions}

### Envio de mensagens {#messaging}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Campaigns | Ver Campaigns | Ver Campaigns |
| Campaigns | Lançar Campaigns | Iniciar, parar, pausar ou retomar Campaigns existentes |
| Campaigns | Arquivar Campaigns | Mover Campaigns para o arquivo |
| Campaigns | Editar Campaigns | Criar e atualizar Campaigns |
| Campaigns | Aprovar e rejeitar Campaigns | Aprovar ou rejeitar Campaigns. O [fluxo de trabalho de aprovação para Campaigns]({{site.baseurl}}/user_guide/messaging/governance/approvals) deve estar ativado para que essa permissão seja aplicada. |
| Canvas | Ver Canvas | Ver Canvas |
| Canvas | Arquivar Canvas | Mover Canvas para o arquivo |
| Canvas | Editar Canvas | Criar e atualizar Canvas |
| Canvas | Lançar Canvas | Iniciar, parar, pausar ou retomar Canvas existentes |
| Canvas | Aprovar e rejeitar Canvas | Aprovar ou rejeitar Canvas. O [fluxo de trabalho de aprovação para Canvas]({{site.baseurl}}/user_guide/messaging/governance/approvals) deve estar ativado para que essa permissão seja aplicada. |
| Feature Flags | Ver Feature Flags | Ver Feature Flags |
| Feature Flags | Arquivar Feature Flags | Mover Feature Flags para o arquivo |
| Feature Flags | Editar Feature Flags | Criar e atualizar Feature Flags |
| Limites de frequência | Ver regras de limite de frequência | Ver regras de limite de frequência |
| Limites de frequência | Editar regras de limite de frequência | Criar e atualizar regras de limite de frequência |
| Landing pages | Ver landing pages | Ver landing pages |
| Landing pages | Publicar landing pages | Tornar ativa uma landing page em rascunho |
| Landing pages | Editar rascunhos de landing page | Criar e salvar rascunhos de landing page |
| Configurações de arquivamento de mensagens | Ver configurações de arquivamento de mensagens | Ver configurações de arquivamento de mensagens sem fazer alterações |
| Configurações de arquivamento de mensagens | Editar configurações de arquivamento de mensagens | Criar e atualizar configurações de arquivamento de mensagens |
| Priorização de mensagens | Ver priorização de mensagens | Ver configurações de priorização de mensagens sem fazer alterações |
| Priorização de mensagens | Editar priorização de mensagens | Criar e atualizar configurações de priorização de mensagens |
| WhatsApp Flows | Ver WhatsApp Flows | Ver todos os WhatsApp Flows |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões de envio de mensagens" }

### Público {#audience}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Grupo de controle global | Ver grupo de controle global | Ver a página de configuração do grupo de controle global |
| Grupo de controle global | Editar grupo de controle global | Criar e salvar alterações no grupo de controle global. Usuários com a permissão "Editar grupo de controle global" também devem ter as permissões "Editar Campaigns" e "Editar Canvas". Usuários com a permissão "Editar grupo de controle global" também recebem a permissão "Ver grupo de controle global". |
| Locais | Arquivar locais | Mover locais para o arquivo |
| Locais | Ver locais | Ver locais |
| Locais | Editar locais | Criar e editar locais |
| Segments | Ver Segments | Ver Segments. Os usuários devem ter a permissão "Ver Segments" para ter a permissão "Editar Segments" ou "Arquivar Segments" |
| Segments | Arquivar Segments | Arquivar e desarquivar Segments. Usuários com a permissão "Arquivar Segments" também devem ter a permissão "Ver Segments" |
| Segments | Editar Segments | Criar e atualizar Segments. Usuários com a permissão "Editar Segments" também devem ter a permissão "Ver Segments" |
| Dados de usuários | Ver importação de usuários | Ver importações de usuários via CSV sem fazer alterações |
| Dados de usuários | Importar usuários | Fazer upload de usuários para o dashboard |
| Dados de usuários | Editar dados de usuários | Criar e atualizar dados de usuários |
| Dados de usuários | Exportar dados de usuários | Baixar usuários do dashboard |
| Usuários duplicados | Ver registros de mesclagem de usuários | Ver uma lista de registros de mesclagem de usuários |
| Usuários | Ver perfis de usuário (IPI ocultas) | Ver perfis de usuário em conformidade com IPI. Usuários com essa permissão não podem salvar ou lançar Campaigns que fazem referência a atributos personalizados marcados como IPI, a menos que também tenham a permissão "Ver atributos personalizados marcados como IPI".<br><br>A permissão "Ver perfis de usuário (IPI ocultas)" deve ser ativada antes do uso. Entre em contato com o seu gerente de sucesso do cliente para ativá-la no seu espaço de trabalho. |
| Usuários | Ver propriedades de eventos do usuário | Ver propriedades de eventos na guia **Histórico de eventos** nos perfis de usuário |
| Usuários duplicados | Mesclar usuários duplicados | Combinar usuários duplicados em um único usuário. Os duplicados são removidos após a mesclagem |
| Excluir usuários | Ver registros de exclusão de usuários | Ver uma lista de registros de exclusão de usuários |
| Excluir usuários | Excluir usuários | Excluir permanentemente usuários do dashboard individualmente ou em massa |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões de público" }

### Modelo {#template}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Modelos de banner | Ver modelos de banner | Ver modelos de banner |
| Modelos de banner | Arquivar modelos de banner | Mover modelos de banner para o arquivo |
| Modelos de banner | Editar modelos de banner | Criar e atualizar modelos de banner |
| Modelos de Canvas | Ver modelos de Canvas | Ver modelos de Canvas |
| Modelos de Canvas | Arquivar modelos de Canvas | Mover modelos de Canvas para o arquivo |
| Modelos de Canvas | Criar e editar modelos de Canvas | Criar e atualizar modelos de Canvas |
| Content Blocks | Ver Content Blocks | Ver Content Blocks |
| Content Blocks | Lançar Content Blocks | Publicar Content Blocks em rascunho, além de editar, arquivar e desarquivar Content Blocks publicados |
| Content Blocks | Arquivar Content Blocks | Mover Content Blocks para o arquivo |
| Content Blocks | Editar Content Blocks | Criar Content Blocks e editar Content Blocks em rascunho |
| Modelos de links de e-mail | Ver modelos de links de e-mail | Ver modelos de links sem fazer alterações |
| Modelos de links de e-mail | Editar modelos de links de e-mail | Criar e atualizar modelos de links |
| Modelos de e-mail | Ver modelos de e-mail | Ver modelos de e-mail |
| Modelos de e-mail | Arquivar modelos de e-mail | Mover modelos de e-mail para o arquivo |
| Modelos de e-mail | Editar modelos de e-mail | Criar e atualizar modelos de e-mail |
| Modelos de mensagem no app | Ver modelos de mensagem no app | Ver modelos de mensagem no app sem fazer alterações |
| Modelos de mensagem no app | Arquivar modelos de mensagem no app | Mover modelos de mensagem no app para o arquivo |
| Modelos de mensagem no app | Editar modelos de mensagem no app | Criar e atualizar modelos de mensagem no app |
| Modelos de landing page | Ver modelos de landing page | Ver modelos de landing page |
| Modelos de landing page | Arquivar modelos de landing page | Mover modelos de landing page para o arquivo |
| Modelos de landing page | Editar modelos de landing page | Criar e atualizar modelos de landing page |
| Modelos de webhook | Ver modelos de webhook | Ver modelos de webhook sem fazer alterações |
| Modelos de webhook | Arquivar modelos de webhook | Mover modelos de webhook para o arquivo |
| Modelos de webhook | Editar modelos de webhook | Criar e atualizar modelos de webhook |
| Modelos de mensagem do WhatsApp | Ver modelos de mensagem do WhatsApp | Permite que os usuários vejam [modelos de mensagem do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) |
| Modelos de mensagem do WhatsApp | Editar modelos de mensagem do WhatsApp | Permite que os usuários criem modelos de mensagem do WhatsApp no construtor de modelos. Esse recurso está atualmente em acesso antecipado. |
| Modelos de mensagem do WhatsApp do Meta | Ver modelos de mensagem do WhatsApp do Meta | Ver todos os modelos do WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões de modelo" }

### Integrações com parceiros {#partner-integrations}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Integrações com Currents | Ver integrações com Currents | Ver integrações com Currents e compartilhamento de dados (Snowflake Data Sharing e Databricks Delta Sharing) |
| Integrações com Currents | Editar integrações com Currents | Criar, atualizar e excluir integrações com Currents e compartilhamentos de dados |
| Parceiros de tecnologia | Editar parceiros de tecnologia | Criar e atualizar parceiros de tecnologia |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões de integrações com parceiros" }

### Configurações de dados {#data-settings}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Catálogos | Ver catálogos | Ver catálogos e seleções |
| Catálogos | Excluir catálogos | Excluir permanentemente catálogos |
| Catálogos | Exportar catálogos | Baixar catálogos do dashboard |
| Catálogos | Editar catálogos | Criar e atualizar catálogos e seleções |
| Ingestão de dados na nuvem | Editar ingestão de dados na nuvem | Criar, atualizar e excluir fontes e sincronizações |
| Atributos personalizados | Ver atributos personalizados | Ver atributos personalizados e relatório de uso |
| Atributos personalizados | Exportar atributos personalizados | Baixar atributos personalizados do dashboard |
| Atributos personalizados | Excluir atributos personalizados | Excluir permanentemente atributos personalizados |
| Atributos personalizados | Bloquear atributos personalizados | Adicionar atributos personalizados a uma lista de bloqueio que restringe o uso no dashboard |
| Atributos personalizados | Editar atributos personalizados | Criar e atualizar atributos personalizados |
| Segmentação por propriedade de evento personalizado | Editar segmentação por propriedade de evento personalizado | Ativar e desativar a segmentação para propriedades de eventos personalizados |
| Eventos personalizados | Ver eventos personalizados | Ver eventos personalizados e relatório de uso, além de adicionar eventos personalizados ao e-mail de relatório de análise de dados diário |
| Eventos personalizados | Exportar eventos personalizados | Baixar eventos personalizados do dashboard |
| IPI | Ver IPI | Ver IPI |
| Eventos personalizados | Excluir eventos personalizados | Excluir permanentemente eventos personalizados |
| Eventos personalizados | Bloquear eventos personalizados | Adicionar eventos personalizados a uma lista de bloqueio que restringe o uso no dashboard |
| Eventos personalizados | Editar eventos personalizados | Criar e atualizar eventos personalizados |
| Produtos | Ver produtos | Ver produtos |
| Produtos | Bloquear produtos | Adicionar produtos a uma lista de bloqueio que restringe o uso no dashboard |
| Produtos | Editar produtos | Criar e atualizar produtos |
| Segmentação por propriedade de compra | Editar segmentação por propriedade de compra | Ativar e desativar a segmentação para propriedades de eventos de compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões de configurações de dados" }

### Configurações {#settings}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Identificadores de API | Ver identificadores de API | Ver identificadores de API e outros identificadores |
| Chaves de API | Ver chaves de API | Ver chaves de API |
| Chaves de API | Editar chaves de API | Criar e atualizar chaves de API |
| Limites de API | Ver limites de API | Ver limites de taxa da API |
| Alertas de uso de API | Ver alertas de uso de API | Ver alertas de uso de API |
| Alertas de uso de API | Editar alertas de uso de API | Criar e atualizar alertas de uso de API |
| Dados de uso de API | Ver dashboard de uso de API | Ver o dashboard de uso de API |
| Configurações de app | Editar configurações de app | Criar, editar e atualizar apps dentro das configurações de app |
| Configurações de app | Ver configurações de app | Ver a página de configurações de app |
| Configurações de Audience Sync | Ver configurações de Audience Sync | Ver todas as configurações dos parceiros conectados de Audience Sync |
| Usuários do dashboard | Editar usuários do dashboard | Ver, criar e editar usuários da empresa |
| Configurações de e-mail | Ver configurações de e-mail | Ver preferências de e-mail |
| Configurações de e-mail | Editar configurações de e-mail | Ativar e atualizar preferências de e-mail |
| Registro de usuários de eventos | Ver registro de usuários de eventos | Ver registros de usuários de eventos |
| Grupos internos | Ver grupos internos de usuários | Ver grupos internos |
| Grupos internos | Excluir grupos internos de usuários | Excluir grupos internos |
| Grupos internos | Editar grupos internos de usuários | Criar e atualizar grupos internos |
| Registro de atividade de mensagens | Ver registro de atividade de mensagens | Ver registros de atividade de mensagens |
| Configurações de múltiplos idiomas | Ver configurações de localização | Ver a página de configurações de localidades de múltiplos idiomas |
| Configurações de múltiplos idiomas | Excluir configurações de localização | Excluir localidade de múltiplos idiomas |
| Configurações de múltiplos idiomas | Editar configurações de localização | Criar localidades de múltiplos idiomas |
| Centrais de Preferências | Ver Centrais de Preferências | Ver Centrais de Preferências |
| Centrais de Preferências | Editar Centrais de Preferências | Criar e atualizar Centrais de Preferências |
| Centrais de Preferências | Lançar Centrais de Preferências | Tornar ativa uma Central de Preferências em rascunho ou atualizar uma existente |
| Configurações de push | Ver configurações de push | Ver configurações de push |
| Configurações de push | Editar configurações de push | Criar e atualizar configurações de push |
| SDK Debugger | Ver SDK Debugger | Ver o SDK Debugger ou sessões de depuração |
| SDK Debugger | Editar SDK Debugger | Criar e baixar sessões do SDK Debugger |
| Tags | Ver tags | Ver tags |
| Tags | Excluir tags | Excluir permanentemente tags |
| Tags | Editar tags | Criar e atualizar tags |
| Equipes | Ver equipes | Ver equipes |
| Equipes | Arquivar equipes | Mover equipes para o arquivo |
| Equipes | Editar equipes | Criar e atualizar equipes |
| Configurações do WhatsApp | Ver configurações do WhatsApp | Ver todas as configurações do canal WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões de configurações" }

### Decisioning Studio

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Agentes do Decisioning Studio | Ver agente do Decisioning Studio | Ver a configuração dos agentes do Decisioning Studio sem fazer alterações |
| Público do Decisioning Studio | Ver público do Decisioning Studio | Ver detalhes de público nos resumos de configuração dos agentes do Decisioning Studio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões do Decisioning Studio" }

### Outros {#other}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Uso do app | Ver dados de uso | Ver dados de uso |
| Faturamento | Ver detalhes de faturamento | Ver detalhes de faturamento |
| Agentes personalizados | Ver agentes de IA do console de agentes | Permite que os usuários vejam agentes de IA personalizados |
| Agentes personalizados | Arquivar agentes de IA do console de agentes | Permite que os usuários arquivem agentes de IA personalizados |
| Agentes personalizados | Editar agentes de IA do console de agentes | Permite que os usuários criem e atualizem agentes de IA personalizados |
| Atributos personalizados marcados como IPI | Ver atributos personalizados marcados como IPI | Ver atributos personalizados marcados como IPI |
| Relatórios do dashboard | Ver relatórios do dashboard | Ver relatórios sem fazer alterações |
| Relatórios do dashboard | Excluir relatórios do dashboard | Excluir permanentemente relatórios |
| Relatórios do dashboard | Editar relatórios do dashboard | Criar e atualizar relatórios |
| Configurações de domínio | Editar configurações de domínio | Adicionar domínios delegados e domínios personalizados em Domínios verificados |
| Criptografia em nível de campo | Editar criptografia em nível de campo de identificador | Ativar e atualizar configurações de criptografia em nível de campo |
| Ativos da biblioteca de mídia | Ver ativos da biblioteca de mídia | Ver ativos da biblioteca de mídia |
| Ativos da biblioteca de mídia | Excluir ativos da biblioteca de mídia | Remover ativos da biblioteca de mídia da interface. Os ativos excluídos permanecem hospedados pela Braze para evitar que mensagens que os referenciam sejam afetadas. Para excluir permanentemente um ativo, entre em contato com o suporte da Braze. |
| Ativos da biblioteca de mídia | Editar ativos da biblioteca de mídia | Criar e atualizar ativos da biblioteca de mídia |
| Ativos da biblioteca de mídia | Substituir ativos da biblioteca de mídia | Substituir o arquivo de um ativo existente da biblioteca de mídia mantendo sua URL e ID de ativo estáveis |
| Limites de taxa de envio de mensagens | Ver limites de taxa de envio de mensagens | Ver limites de taxa de envio de mensagens no nível do espaço de trabalho |
| Limites de taxa de envio de mensagens | Editar limites de taxa de envio de mensagens | Configurar e editar limites de taxa de envio de mensagens no nível do espaço de trabalho |
| Operator | Usar BrazeAI Operator<sup>TM</sup> | Acessar e usar o Braze Operator para responder perguntas, orientar configurações, solucionar problemas e gerar ideias |
| Posicionamentos | Ver posicionamentos | Ver posicionamentos de banner |
| Posicionamentos | Arquivar posicionamentos | Mover posicionamentos de banner para o arquivo |
| Posicionamentos | Editar posicionamentos | Criar e atualizar posicionamentos de banner |
| Códigos de promoção | Ver códigos de promoção | Ver códigos de promoção |
| Códigos de promoção | Exportar códigos de promoção | Baixar uma lista de códigos de promoção do dashboard |
| Códigos de promoção | Editar códigos de promoção | Criar e atualizar códigos de promoção |
| Grupos de inscrições | Editar inscrições | Criar e atualizar grupos de inscrições |
| Transformações | Editar transformação de dados | Criar e atualizar transformações de dados |
| Transformações | Ver transformação de dados | Ver transformações de dados |
| Tickets de suporte | Criar ticket de suporte | Criar e atualizar tickets de suporte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Outras permissões" }