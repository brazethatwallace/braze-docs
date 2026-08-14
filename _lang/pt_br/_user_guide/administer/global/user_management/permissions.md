---
nav_title: Permissões
article_title: Permissões de usuários da empresa
page_order: 1
page_type: reference
alias: /braze_permissions/
description: "Este artigo de referência aborda como as permissões de usuário funcionam na Braze. Aqui, você pode aprender a editar e definir permissões de usuário, escolhendo quem pode acessar seus apps no dashboard."
tool: Dashboard

---

# Permissões da Braze {#braze-permissions}

> Saiba como criar conjuntos de permissões, criar papéis, editar permissões de usuário e exportar permissões de usuário, para garantir que seus usuários acessem apenas os espaços de trabalho e recursos de que mais precisam.
>
> {% multi_lang_include video.html id="nv699nw706" source="wistia" %}

## Criar um conjunto de permissões {#create-a-permission-set}

Use conjuntos de permissões para agrupar permissões relacionadas a áreas de assunto ou ações específicas. Você pode aplicar conjuntos de permissões a usuários do dashboard que precisam do mesmo acesso em diferentes espaços de trabalho. Para criar um conjunto de permissões, acesse **Configurações** > **Gerenciamento de usuários** > **Conjuntos de permissões** e selecione **Criar conjunto de permissões**. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

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

## Criar um papel {#creating-a-role}

Os papéis permitem mais estrutura ao agrupar suas permissões personalizadas individuais com controles de acesso ao espaço de trabalho. Isso é especialmente útil se você tem muitas marcas ou espaços de trabalho regionais em um único dashboard. Com papéis, você pode adicionar usuários do dashboard aos espaços de trabalho corretos e conceder diretamente as permissões associadas. Para criar um papel, acesse **Configurações** > **Gerenciamento de usuários** > **Papéis** e selecione **Criar papel**. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab exemplos de papéis %}
| Nome do papel    | Espaço de trabalho | Permissões
----------- | ----------- | ---------
| Profissional de marketing - Marcas de moda | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Profissional de marketing - Marcas de skincare | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} |"View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers".|
| Gerenciamento de usuários - Todas as marcas | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams"|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Exemplos de papéis" }
{% endtab %}
{% endtabs %}

## Qual a diferença entre conjuntos de permissões, papéis e equipes? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions/differences.md content="Differences" %}

### Considerações ao adicionar permissões de usuário a equipes {#considerations-for-adding-user-permissions-to-teams}

Você pode encontrar dificuldades ao tentar salvar permissões no dashboard da Braze, especialmente ao adicionar ou remover usuários de um espaço de trabalho ou adicioná-los a uma equipe. O botão **Salvar/Atualizar usuários** pode ficar acinzentado se as permissões do usuário forem idênticas às que ele já possui no nível do espaço de trabalho. Essa restrição existe porque não há benefício em ter uma equipe se todos os usuários possuem as mesmas permissões de todo o espaço de trabalho.

Para adicionar um usuário a uma equipe com sucesso mantendo as mesmas permissões, não atribua nenhuma permissão no nível do espaço de trabalho. Em vez disso, atribua permissões exclusivamente no nível da equipe.

## Usuários limitados {#limited-users}

Usuários limitados têm permissões específicas que permitem gerenciar determinados aspectos do dashboard da Braze, mas com restrições em comparação com administradores da empresa e administradores do espaço de trabalho.

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
| Administrador (administrador da empresa) | Administradores da empresa têm permissões mais amplas, incluindo a capacidade de excluir usuários do dashboard. No entanto, eles não podem excluir suas próprias contas e devem entrar em contato com outro administrador da empresa para essa ação. |
| Acesso somente leitura | Para acessar partes do dashboard, como a página de Campaigns, os usuários devem ter permissões de visualização atribuídas a eles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparação de usuários limitados" }

### Erro de acesso limitado {#limited-access-error}

Os usuários podem encontrar mensagens como "Você precisa da permissão 'View Landing Pages' para acessar esta página". Nesses casos, o usuário e o administrador da conta devem verificar se as permissões necessárias foram concedidas. Se já estiverem, tente resolver o problema desativando e reativando as permissões do usuário.

{% alert note %}
Não é possível mesclar ou importar permissões de usuário de um usuário do dashboard para outro.
{% endalert %}

## Nuances das permissões de usuário {#nuances-of-user-permissions}

Tenha em mente os seguintes comportamentos ao atribuir acesso ao dashboard:

- **Administrador do espaço de trabalho versus administrador da empresa:** Administradores do espaço de trabalho gerenciam permissões dentro dos espaços de trabalho atribuídos. Administradores da empresa têm autoridade em toda a empresa, incluindo a exclusão de outros usuários do dashboard.
- **Usuários limitados:** Usuários limitados com a permissão "Edit Dashboard Users" podem gerenciar outros usuários limitados, mas não podem criar ou gerenciar contas de administrador da empresa.
- **Escopo de gerenciamento de usuários do dashboard:** Na página de detalhes do usuário, as permissões aparecem apenas para os espaços de trabalho que o editor pode acessar. Um usuário limitado que pode editar usuários em um espaço de trabalho pode não ver as caixas de seleção de permissões de outro espaço de trabalho.
- **Botão Atribuir permissões:** Ao editar um usuário que já possui permissões no nível do espaço de trabalho ou conjuntos de permissões para todos os espaços de trabalho que você pode gerenciar, o botão **Atribuir permissões** desaparece. Isso acontece porque não há espaços de trabalho adicionais para atribuir no nível do espaço de trabalho.
- **Exportar dados de usuários:** A exportação de dados de usuários requer acesso no nível do espaço de trabalho, além da permissão de exportação.
- **Permissões compostas:** Algumas áreas exigem múltiplas permissões. Por exemplo, configurar [parceiros de tecnologia]({{site.baseurl}}/partners) normalmente requer tanto o acesso ao parceiro quanto uma permissão básica de leitura para os recursos relacionados do espaço de trabalho.
- **Importar e atualizar dados de usuários:** Essa permissão inclui a capacidade de editar perfis de usuários do app por meio de fluxos de importação, não apenas registros de usuários do dashboard.

## Editar as permissões de um usuário {#edit-a-users-permissions}

Para editar as permissões atuais de administrador, empresa ou espaço de trabalho de um usuário, acesse **Configurações** > **Gerenciamento de usuários** > **Usuários da empresa** e selecione o nome dele.

![A página "Usuários da empresa" na Braze mostrando uma tabela de usuários do dashboard.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Administrador %}

### Administrador {#admin}

Administradores têm acesso a todos os recursos e a capacidade de modificar qualquer configuração da empresa. Eles podem:

- Alterar [configurações de aprovação]({{site.baseurl}}/user_guide/messaging/governance/approvals#turning-on-the-approval-workflow)
- Adicionar, editar, excluir, suspender ou reativar outros [usuários da Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#adding-company-users)
- Exportar usuários da Braze como CSV

Para conceder ou remover privilégios de administrador, selecione **Este usuário é um administrador** e depois selecione **Atualizar usuário**.

{% alert warning %}
Se você remover os privilégios de administrador de um usuário, ele não poderá acessar a Braze até que você atribua pelo menos uma [permissão no nível da empresa ou do espaço de trabalho]({{site.baseurl}}/user_guide/administer/global/user_management/permissions?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Empresa %}

### Empresa {#company}

Para gerenciar as seguintes permissões no nível da empresa para um usuário, marque ou desmarque a caixa ao lado da permissão. Quando terminar, selecione **Atualizar usuário**.

| Nome da permissão | Descrição |
|----------|-----------|
| Gerenciar configurações da empresa | Permite que os usuários modifiquem configurações de permissão e verificação de remetente. |
| Criar e excluir espaços de trabalho | Permite que os usuários criem e excluam espaços de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permissões no nível da empresa" }

{% endtab %}
{% tab Espaço de trabalho %}

### Espaço de trabalho {#workspace}

Você pode conceder a um usuário permissões diferentes para cada espaço de trabalho ao qual ele pertence na Braze. Para gerenciar as permissões no nível do espaço de trabalho, selecione **Selecionar espaços de trabalho e permissões** e escolha as permissões manualmente ou atribua um [conjunto de permissões ou papel]({{site.baseurl}}/user_guide/administer/global/user_management/permissions?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) que você criou anteriormente. Se precisar conceder a um usuário permissões diferentes para espaços de trabalho diferentes, repita esse processo quantas vezes for necessário. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

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

## Exportar permissões de usuário {#exporting-user-permissions}

Para baixar uma lista dos seus usuários e suas permissões, acesse **Configurações** > **Gerenciamento de usuários** > **Usuários da empresa** e selecione **Exportar usuários**. Um arquivo CSV será enviado para o seu endereço de e-mail em breve.

## Lista de permissões {#list-of-permissions}

### Envio de mensagens {#messaging}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Campaigns | View Campaigns | Visualizar Campaigns |
| Campaigns | Launch Campaigns | Iniciar, parar, pausar ou retomar Campaigns existentes |
| Campaigns | Archive Campaigns | Mover Campaigns para o arquivo |
| Campaigns | Edit Campaigns | Criar e atualizar Campaigns |
| Campaigns | Approve and Deny Campaigns | Aprovar ou rejeitar Campaigns. O [fluxo de aprovação para Campaigns]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals) deve estar ativado para que essa permissão se aplique. Essa configuração está atualmente em acesso antecipado. Entre em contato com seu gerente de conta se tiver interesse em participar do acesso antecipado. |
| Canvas | View Canvases | Visualizar Canvas |
| Canvas | Archive Canvases | Mover Canvas para o arquivo |
| Canvas | Edit Canvases | Criar e atualizar Canvas |
| Canvas | Launch Canvases | Iniciar, parar, pausar ou retomar Canvas existentes |
| Canvas | Approve and Deny Canvases | Aprovar ou rejeitar Canvas. O [fluxo de aprovação para Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals) deve estar ativado para que essa permissão se aplique. Essa configuração está atualmente em acesso antecipado. Entre em contato com seu gerente de conta se tiver interesse em participar do acesso antecipado. |
| Feature Flags | View Feature Flags | Visualizar Feature Flags |
| Feature Flags | Archive Feature Flags | Mover Feature Flags para o arquivo |
| Feature Flags | Edit Feature Flags | Criar e atualizar Feature Flags |
| Limites de frequência | View Frequency Capping Rules | Visualizar regras do limite de frequência |
| Limites de frequência | Edit Frequency Capping Rules | Criar e atualizar regras do limite de frequência |
| Landing pages | View Landing Pages | Visualizar landing pages |
| Landing pages | Publish Landing Pages | Tornar ativa uma landing page em rascunho |
| Landing pages | Edit Landing Page Drafts | Criar e salvar rascunhos de landing page |
| Configurações de arquivamento de mensagem | View Message Archiving Settings | Visualizar configurações de arquivamento de mensagem sem fazer alterações |
| Configurações de arquivamento de mensagem | Edit Message Archiving Settings | Criar e atualizar configurações de arquivamento de mensagem |
| Priorização de mensagens | View Message Prioritization | Visualizar configurações de priorização de mensagens sem fazer alterações |
| Priorização de mensagens | Edit Message Prioritization | Criar e atualizar configurações de priorização de mensagens |
| WhatsApp Flows | View WhatsApp Flows | Visualizar todos os WhatsApp Flows |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões de envio de mensagens" }

### Público {#audience}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Grupo de controle global | View Global Control Group | Visualizar a página de configuração do grupo de controle global |
| Grupo de controle global | Edit Global Control Group | Criar e salvar alterações no grupo de controle global. Usuários com a permissão "Edit Global Control Group" também devem ter as permissões "Edit Campaigns" e "Edit Canvases". Usuários com a permissão "Edit Global Control Group" também recebem a permissão "View Global Control Group". |
| Locais | Archive Locations | Mover locais para o arquivo |
| Locais | View Locations | Visualizar locais |
| Locais | Edit Locations | Criar e editar locais |
| Segments | View Segments | Visualizar Segments. Os usuários devem ter a permissão "View Segments" para ter a permissão "Edit Segments" ou "Archive Segments" |
| Segments | Archive Segments | Arquivar e desarquivar Segments. Usuários com a permissão "Archive Segments" também devem ter a permissão "View Segments" |
| Segments | Edit Segments | Criar e atualizar Segments. Usuários com a permissão "Edit Segments" também devem ter a permissão "View Segments" |
| Dados de usuários | View Import Users | Visualizar importações de usuários por CSV sem fazer alterações |
| Dados de usuários | Import Users | Fazer upload de usuários para o dashboard |
| Dados de usuários | Edit User Data | Criar e atualizar dados de usuários |
| Dados de usuários | Export User Data | Baixar usuários do dashboard |
| Usuários duplicados | View User Merge Records | Visualizar uma lista de registros de mesclagem de usuários |
| Usuários | View User Profiles (PII Redacted) | Visualizar perfis de usuário de maneira compatível com IPI. Usuários com essa permissão não podem salvar ou lançar Campaigns que referenciam atributos personalizados marcados como IPI, a menos que também tenham a permissão "View Custom Attributes Marked as PII".<br><br>A permissão "View User Profiles (PII Redacted)" deve ser ativada antes do uso. Entre em contato com seu gerente de sucesso do cliente para ativá-la no seu espaço de trabalho. |
| Usuários | View User Event Properties | Visualizar propriedades de eventos na guia **Histórico de eventos** nos perfis de usuário |
| Usuários duplicados | Merge Duplicate Users | Combinar usuários duplicados em um único usuário. Os duplicados são removidos após a mesclagem |
| Exclusão de usuários | View User Deletion Records | Visualizar uma lista de registros de exclusão de usuários |
| Exclusão de usuários | Delete Users | Excluir permanentemente usuários do dashboard individualmente ou em massa |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões de público" }

### Modelo {#template}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Modelos de banner | View Banner Templates | Visualizar modelos de banner |
| Modelos de banner | Archive Banner Templates | Mover modelos de banner para o arquivo |
| Modelos de banner | Edit Banner Templates | Criar e atualizar modelos de banner |
| Modelos de Canvas | View Canvas Templates | Visualizar modelos de Canvas |
| Modelos de Canvas | Archive Canvas Templates | Mover modelos de Canvas para o arquivo |
| Modelos de Canvas | Create and Edit Canvas Templates | Criar e atualizar modelos de Canvas |
| Content Blocks | View Content Blocks | Visualizar Content Blocks |
| Content Blocks | Launch Content Blocks | Publicar Content Blocks em rascunho e editar, arquivar e desarquivar Content Blocks publicados |
| Content Blocks | Archive Content Blocks | Mover Content Blocks para o arquivo |
| Content Blocks | Edit Content Blocks | Criar Content Blocks e editar Content Blocks em rascunho |
| Modelos de links de e-mail | View Email Link Templates | Visualizar modelos de links sem fazer alterações |
| Modelos de links de e-mail | Edit Email Link Templates | Criar e atualizar modelos de links |
| Modelos de e-mail | View Email Templates | Visualizar modelos de e-mail |
| Modelos de e-mail | Archive Email Templates | Mover modelos de e-mail para o arquivo |
| Modelos de e-mail | Edit Email Templates | Criar e atualizar modelos de e-mail |
| Modelos de mensagens no app | View IAM Templates | Visualizar modelos de mensagens no app sem fazer alterações |
| Modelos de mensagens no app | Archive IAM Templates | Mover modelos de mensagens no app para o arquivo |
| Modelos de mensagens no app | Edit IAM Templates | Criar e atualizar modelos de mensagens no app |
| Modelos de landing page | View Landing Page Templates | Visualizar modelos de landing page |
| Modelos de landing page | Archive Landing Page Template | Mover modelos de landing page para o arquivo |
| Modelos de landing page | Edit Landing Page Templates | Criar e atualizar modelos de landing page |
| Modelos de webhook | View Webhook Templates | Visualizar modelos de webhook sem fazer alterações |
| Modelos de webhook | Archive Webhook Templates | Mover modelos de webhook para o arquivo |
| Modelos de webhook | Edit Webhook Templates | Criar e atualizar modelos de webhook |
| Modelos de mensagens do WhatsApp | View WhatsApp Message Templates | Permite que os usuários visualizem [modelos de mensagens do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) |
| Modelos de mensagens do WhatsApp | Edit WhatsApp Message Templates | Permite que os usuários criem modelos de mensagens do WhatsApp no construtor de modelos. Esse recurso está atualmente em acesso antecipado. |
| Modelos de mensagens do WhatsApp do Meta | View WhatsApp Message Templates From Meta | Visualizar todos os modelos do WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões de modelos" }

### Integrações de parceiros {#partner-integrations}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Integrações do Currents | View Currents Integration | Visualizar integrações do Currents |
| Integrações do Currents | Edit Currents Integrations | Criar, atualizar e excluir integrações do Currents |
| Parceiros de tecnologia | Edit Technology Partners | Criar e atualizar parceiros de tecnologia |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões de integrações de parceiros" }

### Configurações de dados {#data-settings}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Catálogos | View Catalogs | Visualizar catálogos e seleções |
| Catálogos | Delete Catalogs | Excluir permanentemente catálogos |
| Catálogos | Export Catalogs | Baixar catálogos do dashboard |
| Catálogos | Edit Catalogs | Criar e atualizar catálogos e seleções |
| Ingestão de dados na nuvem | Edit Cloud Data Ingestion | Criar, atualizar e excluir fontes e sincronizações |
| Atributos personalizados | View Custom Attributes | Visualizar atributos personalizados e relatório de uso |
| Atributos personalizados | Export Custom Attributes | Baixar atributos personalizados do dashboard |
| Atributos personalizados | Delete Custom Attributes | Excluir permanentemente atributos personalizados |
| Atributos personalizados | Blocklist Custom Attributes | Adicionar atributos personalizados a uma lista de bloqueio que restringe o uso no dashboard |
| Atributos personalizados | Edit Custom Attributes | Criar e atualizar atributos personalizados |
| Segmentação por propriedade de evento personalizado | Edit Custom Event Property Segmentation | Ativar e desativar a segmentação por propriedades de eventos personalizados |
| Eventos personalizados | View Custom Events | Visualizar eventos personalizados e relatório de uso, e adicionar eventos personalizados ao e-mail de relatório de análise de dados diário |
| Eventos personalizados | Export Custom Events | Baixar eventos personalizados do dashboard |
| IPI | View PII | Visualizar IPI |
| Eventos personalizados | Delete Custom Events | Excluir permanentemente eventos personalizados |
| Eventos personalizados | Blocklist Custom Events | Adicionar eventos personalizados a uma lista de bloqueio que restringe o uso no dashboard |
| Eventos personalizados | Edit Custom Events | Criar e atualizar eventos personalizados |
| Produtos | View Products | Visualizar produtos |
| Produtos | Blocklist Products | Adicionar produtos a uma lista de bloqueio que restringe o uso no dashboard |
| Produtos | Edit Products | Criar e atualizar produtos |
| Segmentação por propriedade de compra | Edit Purchase Property Segmentation | Ativar e desativar a segmentação por propriedades de eventos de compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões de configurações de dados" }

### Configurações {#settings}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Identificadores de API | View API identifiers | Visualizar identificadores de API e outros identificadores |
| Chaves de API | View API Keys | Visualizar chaves de API |
| Chaves de API | Edit API Keys | Criar e atualizar chaves de API |
| Limites de API | View API Limits | Visualizar limites de taxa de API |
| Alertas de uso de API | View API Usage Alerts | Visualizar alertas de uso de API |
| Alertas de uso de API | Edit API Usage Alerts | Criar e atualizar alertas de uso de API |
| Dados de uso de API | View API Usage Dashboard | Visualizar o dashboard de uso de API |
| Configurações do app | Edit App Settings | Criar, editar e atualizar apps nas configurações do app |
| Configurações do app | View App Settings | Visualizar a página de configurações do app |
| Configurações de Audience Sync | View Audience Sync Settings | Visualizar todas as configurações dos parceiros de Audience Sync conectados |
| Usuários do dashboard | Edit Dashboard Users | Visualizar, criar e editar usuários da empresa |
| Configurações de e-mail | View Email Settings | Visualizar preferências de e-mail |
| Configurações de e-mail | Edit Email Settings | Ativar e atualizar preferências de e-mail |
| Registro de usuários de eventos | View Event User Log | Visualizar registros de usuários de eventos |
| Grupos internos | View Internal User Groups | Visualizar grupos internos |
| Grupos internos | Delete Internal User Groups | Excluir grupos internos |
| Grupos internos | Edit Internal User Groups | Criar e atualizar grupos internos |
| Registro de atividades de envio de mensagem | View Message Activity Log | Visualizar registros de atividades de envio de mensagem |
| Configurações de vários idiomas | View Localization Settings | Visualizar a página de configurações de localização de vários idiomas |
| Configurações de vários idiomas | Delete Localization Settings | Excluir localização de vários idiomas |
| Configurações de vários idiomas | Edit Localization Settings | Criar localizações de vários idiomas |
| Central de Preferências | View Preference Centers | Visualizar centrais de preferências |
| Central de Preferências | Edit Preference Centers | Criar e atualizar centrais de preferências |
| Central de Preferências | Launch Preference Centers | Tornar ativa uma Central de Preferências em rascunho ou atualizar uma existente |
| Configurações de push | View Push Settings | Visualizar configurações de push |
| Configurações de push | Edit Push Settings | Criar e atualizar configurações de push |
| Depurador do SDK | View SDK Debugger | Visualizar o depurador do SDK ou sessões de depuração |
| Depurador do SDK | Edit SDK Debugger | Criar e baixar sessões do depurador do SDK |
| Tags | View Tags | Visualizar tags |
| Tags | Delete Tags | Excluir permanentemente tags |
| Tags | Edit Tags | Criar e atualizar tags |
| Equipes | View Teams | Visualizar equipes |
| Equipes | Archive Teams | Mover equipes para o arquivo |
| Equipes | Edit Teams | Criar e atualizar equipes |
| Configurações do WhatsApp | View WhatsApp Settings | Visualizar todas as configurações do canal WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões de configurações" }

### Decisioning Studio

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Agentes do Decisioning Studio | View Decisioning Studio Agent | Visualizar a configuração dos agentes do Decisioning Studio sem fazer alterações |
| Público do Decisioning Studio | View Decisioning Studio Audience | Ver detalhes do público nos resumos de configuração dos agentes do Decisioning Studio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões do Decisioning Studio" }

### Outros {#other}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Uso do app | View Usage Data | Visualizar dados de uso |
| Faturamento | View Billing Details | Visualizar detalhes de faturamento |
| Agentes personalizados | View Agent Console AI Agents | Permite que os usuários visualizem agentes de IA personalizados |
| Agentes personalizados | Archive Agent Console AI Agents | Permite que os usuários arquivem agentes de IA personalizados |
| Agentes personalizados | Edit Agent Console AI Agents | Permite que os usuários criem e atualizem agentes de IA personalizados |
| Atributos personalizados marcados como IPI | View Custom Attributes Marked as PII | Visualizar atributos personalizados marcados como IPI |
| Relatórios do dashboard | View Dashboard Reports | Visualizar relatórios sem fazer alterações |
| Relatórios do dashboard | Delete Dashboard Reports | Excluir permanentemente relatórios |
| Relatórios do dashboard | Edit Dashboard Reports | Criar e atualizar relatórios |
| Configurações de domínio | Edit Domain Settings | Adicionar domínios delegados e domínios personalizados em domínios verificados |
| Criptografia em nível de campo | Edit Identifier Field-Level Encryption | Ativar e atualizar configurações de criptografia em nível de campo |
| Ativos da biblioteca de mídia | View Media Library Assets | Visualizar ativos da biblioteca de mídia |
| Ativos da biblioteca de mídia | Delete Media Library Assets | Remover ativos da biblioteca de mídia da interface. Ativos excluídos continuam hospedados pela Braze para evitar a quebra de mensagens que os referenciam. Para excluir permanentemente um ativo, entre em contato com o suporte da Braze. |
| Ativos da biblioteca de mídia | Edit Media Library Assets | Criar e atualizar ativos da biblioteca de mídia |
| Ativos da biblioteca de mídia | Replace Media Library Assets | Substituir o arquivo de um ativo existente da biblioteca de mídia mantendo a URL e o ID do ativo estáveis |
| Limites de taxa de envio de mensagens | View Messaging Rate Limits | Visualizar limites de taxa de envio de mensagens no nível do espaço de trabalho |
| Limites de taxa de envio de mensagens | Edit Messaging Rate Limits | Configurar e editar limites de taxa de envio de mensagens no nível do espaço de trabalho |
| Operator | Use BrazeAI Operator<sup>TM</sup> | Acessar e usar o BrazeAI Operator para responder perguntas, navegar pela configuração, solucionar problemas e gerar ideias |
| Posicionamentos | View Placements | Visualizar posicionamentos de banner |
| Posicionamentos | Archive Placements | Mover posicionamentos de banner para o arquivo |
| Posicionamentos | Edit Placements | Visualizar posicionamentos de banner sem fazer alterações |
| Códigos de promoção | View Promotion Codes | Visualizar códigos de promoção |
| Códigos de promoção | Export Promotion Codes | Baixar uma lista de códigos de promoção do dashboard |
| Códigos de promoção | Edit Promotion Codes | Criar e atualizar códigos de promoção |
| Grupos de inscrições | Edit Subscriptions | Criar e atualizar grupos de inscrições |
| Transformações | Edit Data Transformation | Criar e atualizar transformações de dados |
| Transformações | View Data Transformation | Visualizar transformações de dados |
| Tickets de suporte | Create Support Ticket | Criar e atualizar tickets de suporte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Outras permissões" }