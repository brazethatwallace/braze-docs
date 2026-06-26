{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

{% multi_lang_include video.html id="nv699nw706" source="wistia" %}

## Criando um conjunto de permissões {#creating-a-permission-set}

Use conjuntos de permissões para agrupar permissões relacionadas a áreas ou ações específicas. Você pode aplicar conjuntos de permissões a usuários do dashboard que precisam do mesmo acesso em diferentes espaços de trabalho. Para criar um conjunto de permissões, acesse **Configurações** > **Configurações de permissão** e selecione **Create permission set**. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
| Nome | Permissões |
|-----------|----------------|
| Desenvolvedores | "View API Keys", "Edit API Keys", "View Internal Groups", "Edit Internal Groups", "View Message Activity Log", "View Event User Log", "View API identifiers", "View API Usage Dashboard", "View API Limits", "View API Usage Alerts", "Edit API Usage Alerts", "View SDK Debugger", "Edit SDK Debugger". |
| Profissionais de marketing | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Frequency Capping Rules", "Edit Frequency Capping Rules", "View Message Prioritization", "Edit Message Prioritization", "View Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "Edit Global Control Group", "View IAM Templates", "Edit IAM Templates", "Archive IAM Templates", "View Email Templates", "Edit Email Templates", "Archive Email Templates", "View Webhook Templates", "Edit Webhook Templates", "Archive Webhook Templates", "View Email Link Templates", "Edit Email Link Templates", "View Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers", "Edit Dashboard Reports", "View Banner Templates", "View Localization Settings", "Use Operator", "View Decisioning Studio Agents". |
| Gerenciamento de usuários | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Criando um conjunto de permissões" }
{% endtab %}
{% endtabs %}

## Criando uma função {#creating-a-role}

As funções permitem mais estrutura ao agrupar suas permissões personalizadas individuais com os controles de acesso do espaço de trabalho. Isso é especialmente útil se você tiver muitas marcas ou espaços de trabalho regionais em um dashboard. Com funções, você pode adicionar usuários do dashboard aos espaços de trabalho certos e conceder diretamente as permissões associadas. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nome da função | Espaço de trabalho | Permissões
----------- | ----------- | ---------
| Profissional de marketing - Marcas de moda | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Profissional de marketing - Marcas de cuidados com a pele | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Gerenciamento de usuários - Todas as marcas | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Criando uma função" }
{% endtab %}
{% endtabs %}

## Como os conjuntos de permissões e funções diferem das equipes? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions.md content="Differences" %}

### Considerações para adicionar permissões de usuário às equipes {#considerations-for-adding-user-permissions-to-teams}

Você pode encontrar dificuldades ao tentar salvar permissões no dashboard da Braze, especialmente ao adicionar ou remover usuários de um espaço de trabalho, ou ao adicioná-los a uma equipe. O botão **Save/Update Users** pode ficar desativado se as permissões do usuário forem idênticas às que ele já possui no nível do espaço de trabalho. Essa restrição existe porque não há benefício em ter uma equipe se todos os usuários possuem as mesmas permissões que todo o espaço de trabalho.

Para adicionar um usuário a uma equipe com sucesso mantendo as mesmas permissões, não atribua nenhuma permissão no nível do espaço de trabalho. Em vez disso, atribua permissões exclusivamente no nível da equipe.

## Usuários limitados {#limited-users}

Usuários limitados têm permissões específicas que permitem gerenciar certos aspectos do dashboard da Braze, mas com restrições em comparação com administradores da empresa e administradores de espaço de trabalho.

| Escopo | Descrição |
| --- | --- |
| Permissões | Usuários limitados podem editar as permissões de outros usuários limitados se tiverem a permissão "Edit Dashboard Users". Eles também podem criar novos usuários limitados e modificar seus conjuntos de permissões. No entanto, não podem criar ou gerenciar contas de administrador da empresa. |
| Limitações de função | Se um usuário limitado tiver todas as permissões, exceto "Workspace Admin", ele ainda terá acesso a todas as outras permissões normalmente concedidas a um administrador do espaço de trabalho. |
| Visibilidade das permissões | Se um usuário limitado tiver a permissão "Edit Dashboard Users" para um espaço de trabalho (como Dev), mas não para outro (como Prod), ele não verá as permissões do espaço de trabalho Prod na página de detalhes dos usuários do dashboard. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Usuários limitados" }

### Comparando usuários limitados {#comparing-limited-users}

| Tipo de usuário limitado | Descrição |
| --- | --- |
| Administrador do espaço de trabalho | Os administradores do espaço de trabalho têm permissões específicas para gerenciar espaços de trabalho, mas não têm a mesma autoridade que os administradores da empresa. Usuários limitados podem herdar permissões semelhantes às dos administradores do espaço de trabalho se tiverem as permissões necessárias marcadas. |
| Administrador (administrador da empresa) | Os administradores da empresa têm permissões mais amplas, incluindo a capacidade de excluir usuários do dashboard. No entanto, eles não podem excluir suas próprias contas e devem entrar em contato com outro administrador da empresa para essa ação. |
| Acesso somente para visualização | Para acessar partes do dashboard, como a página de Campaigns, os usuários devem ter permissões de visualização atribuídas a eles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparando usuários limitados" }

### Erro de acesso limitado {#limited-access-error}

Os usuários podem encontrar mensagens como "You need 'View Landing Pages' permissions to access this page". Nesses casos, o usuário e o administrador da conta devem verificar se as permissões necessárias foram concedidas. Se sim, tente resolver o problema desativando e reativando as permissões do usuário.

{% alert note %}
Não é possível mesclar ou importar permissões de usuário de um usuário do dashboard para outro.
{% endalert %}

## Editando as permissões de um usuário {#editing-a-users-permissions}

Para editar as permissões atuais de administrador, empresa ou espaço de trabalho de um usuário, acesse **Configurações** > **Usuários da empresa** e selecione o nome dele.

![A página "Usuários da empresa" na Braze mostrando uma tabela de usuários do dashboard.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Administrador {#admin}

Os administradores têm acesso a todos os recursos e a capacidade de modificar qualquer configuração da empresa. Eles podem:

- Alterar [configurações de aprovação]({{site.baseurl}}/user_guide/messaging/governance/approvals/#turning-on-the-approval-workflow)
- Adicionar, editar, excluir, suspender ou reativar outros [usuários da Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/#adding-company-users)
- Exportar usuários da Braze como um arquivo CSV

Para conceder ou remover privilégios de administrador, selecione **This user is an admin** e depois selecione **Update user**.


{% alert warning %}
Se você remover os privilégios de administrador de um usuário, ele não poderá acessar a Braze até que você atribua a ele pelo menos uma [permissão em nível de empresa ou em nível de espaço de trabalho]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Company %}

### Empresa {#company}

Para gerenciar as seguintes permissões em nível de empresa para um usuário, marque ou desmarque a caixa ao lado da permissão. Quando terminar, selecione **Update user**.

| Nome da permissão | Descrição |
|----------|-----------|
| Gerenciar configurações da empresa | Permite que os usuários modifiquem as configurações de permissão e verificação do remetente. |
| Criar e excluir espaços de trabalho | Permite que os usuários criem e excluam espaços de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Empresa" }

{% endtab %}
{% tab Workspace %}

### Espaço de trabalho {#workspace}

Você pode dar a um usuário diferentes permissões para cada espaço de trabalho ao qual ele pertence na Braze. Para gerenciar as permissões em nível de espaço de trabalho, selecione **Select workspaces and permissions** e escolha as permissões manualmente ou atribua um [conjunto de permissões ou função]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) que você criou anteriormente. Se você precisar dar a um usuário permissões diferentes para diferentes espaços de trabalho, repita este processo quantas vezes forem necessárias. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Selecionar manualmente %}

Em **Workspaces**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Permissions**, selecione uma ou mais permissões. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou. Opcionalmente, você pode selecionar **Assign workspace admin access** se desejar dar a eles permissões completas para este espaço de trabalho.

Quando terminar, selecione **Update user**.

![Permissões em nível de espaço de trabalho sendo selecionadas manualmente na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Atribuir conjunto de permissões %}

Em **Workspaces**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Permission Sets**, escolha um conjunto de permissões. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou.

Quando terminar, selecione **Update user**.

![Permissões em nível de espaço de trabalho sendo atribuídas por meio de um conjunto de permissões na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Atribuir função %}

Em **Workspaces**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Role**, escolha uma função. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou.

Quando terminar, selecione **Update user**.

![Permissões em nível de espaço de trabalho sendo atribuídas por meio de uma função na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportando permissões de usuário {#exporting-user-permissions}

Para baixar uma lista dos seus usuários e suas permissões, acesse **Configurações** > **Usuários da empresa** e selecione **Export Users**. Um arquivo CSV será enviado para o seu endereço de e-mail em breve.

![A página "Usuários da empresa" na Braze com a opção "Export Users" em foco.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

Não é possível exportar uma matriz completa de permissões para todos os usuários do dashboard em massa a partir do dashboard da Braze. Se você precisar de mais detalhes do que o **Export Users** oferece, considere estas opções:

- Use o [provisionamento automatizado de usuários]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/) (SCIM) para gerenciar contas de usuários do dashboard. Por exemplo, você pode [pesquisar um usuário do dashboard por e-mail]({{site.baseurl}}/api/endpoints/scim/get_search_existing_dashboard_user/) ou obter detalhes do usuário por ID de recurso, conforme descrito em [Ver informações da conta do usuário]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information/).
- [Fale com o suporte da Braze]({{site.baseurl}}/braze_support/). Em algumas situações, o suporte pode fornecer uma lista de contas, mas não uma matriz completa de permissões.
- Filtre o [relatório de eventos de segurança]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report) da sua empresa, que registra eventos como **Added Account** e **Updated Permissions**, para auditar alterações de permissão fora do dashboard.

## Lista de permissões {#list-of-permissions}

### Envio de mensagens {#messaging}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Campaigns | View Campaigns | Ver Campaigns |
| Campaigns | Launch Campaigns | Iniciar, parar, pausar ou retomar Campaigns existentes |
| Campaigns | Archive Campaigns | Mover Campaigns para o arquivo |
| Campaigns | Edit Campaigns | Criar e atualizar Campaigns |
| Campaigns | Approve and Deny Campaigns | Aprovar ou negar Campaigns. O [fluxo de aprovação para Campaigns]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão se aplique. Esta configuração está atualmente em acesso antecipado. Entre em contato com seu gerente de conta se estiver interessado em participar do acesso antecipado. |
| Canvas | View Canvases | Ver Canvas |
| Canvas | Archive Canvases | Mover Canvas para o arquivo |
| Canvas | Edit Canvases | Criar e atualizar Canvas |
| Canvas | Launch Canvases | Iniciar, parar, pausar ou retomar Canvas existentes |
| Canvas | Approve and Deny Canvases | Aprovar ou negar Canvas. O [fluxo de aprovação para Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão se aplique. Esta configuração está atualmente em acesso antecipado. Entre em contato com seu gerente de conta se estiver interessado em participar do acesso antecipado. |
| Feature Flags | View Feature Flags | Ver Feature Flags |
| Feature Flags | Archive Feature Flags | Mover Feature Flags para o arquivo |
| Feature Flags | Edit Feature Flags | Criar e atualizar Feature Flags |
| Limites de frequência | View Frequency Capping Rules | Ver regras do limite de frequência |
| Limites de frequência | Edit Frequency Capping Rules | Criar e atualizar regras do limite de frequência |
| Landing pages | View Landing Pages | Ver landing pages |
| Landing pages | Publish Landing Pages | Tornar uma landing page em rascunho ativa |
| Landing pages | Edit Landing Page Drafts | Criar e salvar rascunhos de landing page |
| Configurações de arquivamento de mensagem | View Message Archiving Settings | Ver configurações de arquivamento de mensagem sem fazer alterações |
| Configurações de arquivamento de mensagem | Edit Message Archiving Settings | Criar e atualizar configurações de arquivamento de mensagem |
| Priorização de mensagens | View Message Prioritization | Ver configurações de priorização de mensagens sem fazer alterações |
| Priorização de mensagens | Edit Message Prioritization | Criar e atualizar configurações de priorização de mensagens |
| WhatsApp Flows | View WhatsApp Flows | Ver todos os WhatsApp Flows |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Envio de mensagens" }

### Público {#audience}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Grupo de controle global | View Global Control Group | Ver página de configuração do grupo de controle global |
| Grupo de controle global | Edit Global Control Group | Criar e salvar alterações no grupo de controle global. Os usuários com a permissão "Edit Global Control Group" também devem ter permissões para "Edit Campaigns" e "Edit Canvases". Os usuários com a permissão "Edit Global Control Group" também recebem a permissão "View Global Control Group". |
| Locais | Archive Locations | Mover locais para o arquivo |
| Locais | View Locations | Ver locais |
| Locais | Edit Locations | Criar e editar locais |
| Segments | View Segments | Ver Segments. Os usuários devem ter a permissão "View Segments" para ter a permissão "Edit Segments" ou "Archive Segments" |
| Segments | Archive Segments | Arquivar e desarquivar Segments. Os usuários com a permissão "Archive Segments" também devem ter a permissão "View Segments" |
| Segments | Edit Segments | Criar e atualizar Segments. Os usuários com a permissão "Edit Segments" também devem ter a permissão "View Segments" |
| Dados de usuários | View Import Users | Ver importações de usuários CSV sem fazer alterações |
| Dados de usuários | Import Users | Fazer upload de usuários para o dashboard |
| Dados de usuários | Edit User Data | Criar e atualizar dados de usuários |
| Dados de usuários | Export User Data | Baixar usuários do dashboard |
| Registros de exclusão de usuários | View User Merge Records | Ver uma lista de registros de mesclagem de usuários |
| Usuários | View User Profiles (PII Redacted) | Ver perfis de usuário de forma compatível com IPI |
| Usuários duplicados | Merge Duplicate Users | Combinar usuários duplicados em um único usuário. As duplicatas são removidas após a mesclagem |
| Usuários | Delete Users | Excluir permanentemente usuários do dashboard individualmente ou em massa |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Público" }

### Modelo {#template}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Modelos de banner | View Banner Templates | Ver modelos de banner |
| Modelos de banner | Archive Banner Templates | Mover modelos de banner para o arquivo |
| Modelos de banner | Edit Banner Templates | Criar e atualizar modelos de banner |
| Modelos de Canvas | View Canvas Templates | Ver Modelos de Canvas |
| Modelos de Canvas | Archive Canvas Templates | Mover Modelos de Canvas para o arquivo |
| Modelos de Canvas | Create and Edit Canvas Templates | Criar e atualizar Modelos de Canvas |
| Content Blocks | View Content Blocks | Ver Content Blocks |
| Content Blocks | Launch Content Blocks | Publicar Content Blocks em rascunho e editar, arquivar e desarquivar Content Blocks publicados |
| Content Blocks | Archive Content Blocks | Mover Content Blocks para o arquivo |
| Content Blocks | Edit Content Blocks | Criar Content Blocks e editar Content Blocks em rascunho |
| Modelos de link de e-mail | View Email Link Templates | Ver modelos de link sem fazer alterações |
| Modelos de link de e-mail | Edit Email Link Templates | Criar e atualizar modelos de link |
| Modelos de e-mail | View Email Templates | Ver modelos de e-mail |
| Modelos de e-mail | Archive Email Templates | Mover modelos de e-mail para o arquivo |
| Modelos de e-mail | Edit Email Templates | Criar e atualizar modelos de e-mail |
| Modelos IAM | View IAM Templates | Ver modelos de mensagem no app sem fazer alterações |
| Modelos IAM | Archive IAM Templates | Mover modelos IAM para o arquivo |
| Modelos IAM | Edit IAM Templates | Criar e atualizar modelos de mensagem no app |
| Modelos de landing page | View Landing Page Templates | Ver modelos de landing page |
| Modelos de landing page | Archive Landing Page Template | Mover modelos de landing page para o arquivo |
| Modelos de landing page | Edit Landing Page Templates | Criar e atualizar modelos de landing page |
| Modelos de webhook | View Webhook Templates | Ver modelos de webhook sem fazer alterações |
| Modelos de webhook | Archive Webhook Templates | Mover modelos de webhook para o arquivo |
| Modelos de webhook | Edit Webhook Templates | Criar e atualizar modelos de webhook |
| Modelos de mensagem do WhatsApp | View WhatsApp Message Templates | Permite que os usuários vejam [modelos de mensagem do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#step-2-compose-your-whatsapp-message) |
| Modelos de mensagem do WhatsApp | Edit WhatsApp Message Templates | Permite que os usuários criem modelos de mensagem do WhatsApp no construtor de modelos. Este recurso está atualmente em acesso antecipado. |
| Modelos de mensagem do WhatsApp do Meta | View WhatsApp Message Templates From Meta | Ver todos os modelos do WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Modelo" }

### Integrações de parceiros {#partner-integrations}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Integrações do Currents | View Currents Integration | Ver integrações do Currents |
| Integrações do Currents | Edit Currents Integrations | Criar, atualizar e excluir integrações do Currents |
| Parceiros de tecnologia | Edit Technology Partners | Criar e atualizar parceiros de tecnologia |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Integrações de parceiros" }

### Configurações de dados {#data-settings}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Catálogos | View Catalogs | Ver catálogos e seleções |
| Catálogos | Delete Catalogs | Excluir catálogos permanentemente |
| Catálogos | Export Catalogs | Baixar catálogos do dashboard |
| Catálogos | Edit Catalogs | Criar e atualizar catálogos e seleções |
| Ingestão de dados na nuvem | Edit Cloud Data Ingestion | Criar, atualizar e excluir fontes e sincronizações |
| Atributos personalizados | View Custom Attributes | Ver atributos personalizados e relatório de uso |
| Atributos personalizados | Export Custom Attributes | Baixar atributos personalizados do dashboard |
| Atributos personalizados | Delete Custom Attributes | Excluir atributos personalizados permanentemente |
| Atributos personalizados | Blocklist Custom Attributes | Adicionar atributos personalizados a uma lista de bloqueio que restringe o uso no dashboard |
| Atributos personalizados | Edit Custom Attributes | Criar e atualizar atributos personalizados |
| Segmentação de propriedades de eventos personalizados | Edit Custom Event Property Segmentation | Ativar e desativar a segmentação para propriedades de eventos personalizados |
| Eventos personalizados | View Custom Events | Ver eventos personalizados e relatório de uso, e adicionar eventos personalizados ao e-mail do relatório diário de análise de dados |
| Eventos personalizados | Export Custom Events | Baixar eventos personalizados do dashboard |
| IPI | View PII | Ver IPI |
| Eventos personalizados | Delete Custom Events | Excluir permanentemente eventos personalizados |
| Eventos personalizados | Blocklist Custom Events | Adicionar eventos personalizados a uma lista de bloqueio que restringe o uso no dashboard |
| Eventos personalizados | Edit Custom Events | Criar e atualizar eventos personalizados |
| Produtos | View Products | Ver produtos |
| Produtos | Blocklist Products | Adicionar produtos a uma lista de bloqueio que restringe o uso no dashboard |
| Produtos | Edit Products | Criar e atualizar produtos |
| Segmentação de propriedades de compra | Edit Purchase Property Segmentation | Ativar e desativar a segmentação para propriedades de eventos de compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Configurações de dados" }

### Configurações {#settings}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Identificadores de API | View API identifiers | Ver identificadores de API e outros identificadores |
| Chaves de API | View API Keys | Ver chaves de API |
| Chaves de API | Edit API Keys | Criar e atualizar chaves de API |
| Limites da API | View API Limits | Ver limites de taxa da API |
| Alertas de uso da API | View API Usage Alerts | Ver alertas de uso da API |
| Alertas de uso da API | Edit API Usage Alerts | Criar e atualizar alertas de uso da API |
| Dados de uso da API | View API Usage Dashboard | Ver o dashboard de uso da API |
| Configurações do app | Edit App Settings | Criar, editar e atualizar apps nas configurações do app |
| Configurações do app | View App Settings | Ver página de configurações do app |
| Configurações de Audience Sync | View Audience Sync Settings | Ver todas as configurações dos parceiros de Audience Sync conectados |
| Usuários do dashboard | Edit Dashboard Users | Ver, criar e editar usuários da empresa |
| Configurações de e-mail | View Email Settings | Ver preferências de e-mail |
| Configurações de e-mail | Edit Email Settings | Ativar e atualizar preferências de e-mail |
| Registro de usuários de eventos | View Event User Log | Ver registros de usuários de eventos |
| Grupos internos | View Internal User Groups | Ver grupos internos |
| Grupos internos | Delete Internal User Groups | Excluir grupos internos |
| Grupos internos | Edit Internal User Groups | Criar e atualizar grupos internos |
| Registro de atividade de mensagens | View Message Activity Log | Ver registros de atividade de mensagens |
| Configurações multilíngues | View Localization Settings | Ver página de configurações de localização multilíngue |
| Configurações multilíngues | Delete Localization Settings | Excluir localização multilíngue |
| Configurações multilíngues | Edit Localization Settings | Criar localizações multilíngues |
| Centrais de Preferências | View Preference Centers | Ver Centrais de Preferências |
| Centrais de Preferências | Edit Preference Centers | Criar e atualizar Centrais de Preferências |
| Centrais de Preferências | Launch Preference Centers | Tornar um rascunho da Central de Preferências ativo ou atualizar uma existente |
| Configurações de push | View Push Settings | Ver configurações de push |
| Configurações de push | Edit Push Settings | Criar e atualizar configurações de push |
| Depurador do SDK | View SDK Debugger | Ver Depurador do SDK ou sessões de depuração |
| Depurador do SDK | Edit SDK Debugger | Criar e baixar sessões do Depurador do SDK |
| Tags | View Tags | Ver tags |
| Tags | Delete Tags | Excluir tags permanentemente |
| Tags | Edit Tags | Criar e atualizar tags |
| Equipes | View Teams | Ver equipes |
| Equipes | Archive Teams | Mover equipes para o arquivo |
| Equipes | Edit Teams | Criar e atualizar equipes |
| Configurações do WhatsApp | View WhatsApp Settings | Ver todas as configurações do canal WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Configurações" }

### Decisioning Studio

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Agentes do Decisioning Studio | View Decisioning Studio Agent | Ver configuração dos agentes do Decisioning Studio sem fazer alterações |
| Público do Decisioning Studio | View Decisioning Studio Audience | Ver detalhes do público nos resumos de configuração dos agentes do Decisioning Studio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Decisioning Studio" }

### Outros {#other}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Uso do app | View Usage Data | Ver dados de uso |
| Faturamento | View Billing Details | Ver detalhes de faturamento |
| Agentes personalizados | View Agent Console AI Agents | Permite que os usuários vejam agentes de IA personalizados |
| Agentes personalizados | Archive Agent Console AI Agents | Permite que os usuários arquivem agentes de IA personalizados |
| Agentes personalizados | Edit Agent Console AI Agents | Permite que os usuários criem e atualizem agentes de IA personalizados |
| Atributos personalizados marcados como IPI | View Custom Attributes Marked as PII | Ver atributos personalizados marcados como IPI |
| Relatórios do dashboard | View Dashboard Reports | Ver relatórios sem fazer alterações |
| Relatórios do dashboard | Delete Dashboard Reports | Excluir relatórios permanentemente |
| Relatórios do dashboard | Edit Dashboard Reports | Criar e atualizar relatórios |
| Configurações de domínio | Edit Domain Settings | Adicionar domínios delegados e domínios personalizados em Domínios Verificados |
| Criptografia em nível de campo | Edit Identifier Field-Level Encryption | Ativar e atualizar configurações de criptografia em nível de campo |
| Ativos da biblioteca de mídia | View Media Library Assets | Ver ativos da biblioteca de mídia |
| Ativos da biblioteca de mídia | Delete Media Library Assets | Excluir permanentemente ativos da biblioteca de mídia |
| Ativos da biblioteca de mídia | Edit Media Library Assets | Criar e atualizar ativos da biblioteca de mídia |
| Limites de taxa de envio de mensagens | View Messaging Rate Limits | Ver limites de taxa de envio de mensagens no nível do espaço de trabalho |
| Limites de taxa de envio de mensagens | Edit Messaging Rate Limits | Configurar e editar limites de taxa de envio de mensagens no nível do espaço de trabalho |
| Operator | Use BrazeAI Operator<sup>TM</sup> | Acessar e usar o Braze Operator para responder perguntas, navegar pela configuração, solucionar problemas e gerar ideias |
| Posicionamentos | View Placements | Ver posicionamento de banner |
| Posicionamentos | Archive Placements | Mover posicionamentos de banner para o arquivo |
| Posicionamentos | Edit Placements | Ver posicionamentos de banner sem fazer alterações |
| Códigos de promoção | View Promotion Codes | Ver códigos promocionais |
| Códigos de promoção | Export Promotion Codes | Baixar uma lista de códigos promocionais do dashboard |
| Códigos de promoção | Edit Promotion Codes | Criar e atualizar códigos promocionais |
| Grupos de inscrições | Edit Subscriptions | Criar e atualizar grupos de inscrições |
| Transformações | Edit Data Transformation | Criar e atualizar transformações de dados |
| Transformações | View Data Transformation | Ver transformações de dados |
| Registros de exclusão de usuários | View User Deletion Records | Ver registros de exclusão de usuários |
| Tickets de suporte | Create Support Ticket | Criar e atualizar tickets de suporte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Outros" }