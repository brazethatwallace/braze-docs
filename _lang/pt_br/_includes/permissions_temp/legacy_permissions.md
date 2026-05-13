{% alert important %}
A Braze está introduzindo [permissões granulares]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions), uma forma mais flexível de gerenciar o acesso dos usuários. Consulte [Migrando para permissões granulares]({{site.baseurl}}/granular_permissions_migration/) para saber mais sobre o processo de migração, incluindo como as permissões legadas são mapeadas para permissões granulares.
{% endalert %}

## Criando um conjunto de permissões {#creating-a-permission-set}

Use conjuntos de permissões para agrupar permissões relacionadas a áreas ou ações específicas. Você pode aplicar conjuntos de permissões a usuários do dashboard que precisam do mesmo acesso em diferentes espaços de trabalho. Para criar um conjunto de permissões, acesse **Configurações** > **Configurações de Permissão** e selecione **Criar conjunto de permissões**. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% tabs local %}
{% tab conjuntos de permissões de exemplo %}
| Nome | Permissões |
|-----------|----------------|
| Desenvolvedores | "Access Dev Console" |
| Profissionais de marketing | "Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Centers" <br> "Manage Media Library Assets" |
| Gerenciamento de usuários | "Manage Dashboard Users" <br> "Manage Teams" |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Creating a permission set" }
{% endtab %}
{% endtabs %}

## Criando uma função {#creating-a-role}

As funções permitem mais estrutura ao agrupar suas permissões personalizadas individuais com os controles de acesso do espaço de trabalho. Isso é especialmente útil se você tiver muitas marcas ou espaços de trabalho regionais em um dashboard. Com funções, você pode adicionar usuários do dashboard aos espaços de trabalho certos e conceder diretamente as permissões associadas. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% tabs local %}
{% tab funções de exemplo %}
| Nome da função    | Espaço de trabalho | Permissões
----------- | ----------- | ---------
| Profissional de marketing - Marcas de moda | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Center"<br>"Manage Media Library Assets" |
| Profissional de marketing - Marcas de cuidados com a pele | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Centers" <br>"Manage Media Library Assets" |
| Gerenciamento de usuários - Todas as marcas | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Manage Dashboard Users"<br>"Manage Teams" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Creating a role" }
{% endtab %}
{% endtabs %}

## Como os conjuntos de permissões e funções diferem das equipes? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions.md content="Differences" %}

### Considerações para adicionar permissões de usuário às equipes {#considerations-for-adding-user-permissions-to-teams}

Você pode encontrar dificuldades ao tentar salvar permissões no dashboard da Braze, especialmente ao adicionar ou remover usuários de um espaço de trabalho, ou adicioná-los a uma equipe. O botão **Save/Update Users** pode ficar desativado se as permissões do usuário forem idênticas às que ele já possui no nível do espaço de trabalho. Essa restrição existe porque não há benefício em ter uma equipe se todos os usuários possuem as mesmas permissões que todo o espaço de trabalho.

Para adicionar um usuário a uma equipe com sucesso, mantendo as mesmas permissões, não atribua nenhuma permissão no nível do espaço de trabalho. Em vez disso, atribua permissões exclusivamente no nível da equipe.

## Usuários limitados {#limited-users}

Usuários limitados têm permissões específicas que permitem gerenciar certos aspectos do dashboard da Braze, mas com restrições em comparação com administradores da empresa e administradores de espaço de trabalho.

| Permissões | Usuários limitados podem editar as permissões de outros usuários limitados se tiverem a permissão "Manage Dashboard Users" marcada. Eles também podem criar novos usuários limitados e modificar seus conjuntos de permissões. No entanto, eles não podem criar ou gerenciar contas de administradores da empresa. |
| Limitações de função | Se um usuário limitado tiver todas as permissões, exceto "App Group Admin", ainda terá acesso a todas as outras permissões normalmente concedidas a um administrador de espaço de trabalho. |
| Visibilidade das permissões | Se um usuário limitado tiver "Manage Dashboard Users" marcado para um grupo de app (como Dev), mas não para outro (como Prod), ele não verá as permissões do grupo de app Prod em seu perfil "Manage Users". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limited users" }

### Comparando usuários limitados {#comparing-limited-users}

| Tipo de usuário limitado | Descrição |
| --- | --- |
| Administrador do grupo de app | Os administradores do grupo de app têm permissões específicas para gerenciar grupos de app, mas não têm a mesma autoridade que os administradores da empresa. Usuários limitados podem herdar permissões semelhantes às dos administradores do grupo de app se tiverem as permissões necessárias marcadas. |
| Administrador da empresa | Os administradores da empresa têm permissões mais amplas, incluindo a capacidade de excluir usuários do dashboard. No entanto, eles não podem excluir suas próprias contas e devem entrar em contato com outro administrador da empresa para essa ação. |
| Permissão básica somente leitura | Para acessar certas partes do dashboard, como a página de Parceiros de Tecnologia, os usuários devem ter uma permissão básica somente leitura. Isso inclui ter "Manage External Integrations" ativado, juntamente com permissões para Access Campaigns, Canvases, Cards, Segments e Media Library. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparing limited users" }

### Erro de acesso limitado {#limited-access-error}

Os usuários podem encontrar mensagens como "Limited Access. You do not have permissions to access this Page." Nesses casos, o administrador da conta deve verificar se pode resolver o problema desativando e reativando as permissões do usuário.

{% alert note %}
Não é possível mesclar ou importar permissões de usuário de um usuário do dashboard para outro.
{% endalert %}

## Editando as permissões de um usuário {#editing-a-users-permissions}

Para editar as permissões atuais de administrador, empresa ou espaço de trabalho de um usuário, acesse **Configurações** > **Usuários da Empresa** e selecione o nome dele.

![A página "Usuários da Empresa" na Braze com um usuário listado nos resultados.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Administrador %}

### Administrador {#admin}

Os administradores têm acesso a todos os recursos e a capacidade de modificar qualquer configuração da empresa. Eles podem:

- Alterar [configurações de aprovação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Adicionar, editar, excluir, suspender ou reativar outros [usuários da Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)
- Exportar usuários da Braze como um CSV

Para conceder ou remover privilégios de administrador, selecione **This user is an admin** e depois selecione **Update user**.

![Os detalhes do usuário selecionado com a caixa de seleção de administrador em foco.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Se você remover os privilégios de administrador de um usuário, ele não poderá acessar a Braze até que você atribua a ele pelo menos uma permissão [de nível de empresa ou de nível de espaço de trabalho]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions&tab=company#legacypermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Empresa %}

### Empresa {#company}

Para gerenciar as seguintes permissões de nível de empresa para um usuário, marque ou desmarque a caixa ao lado dessa permissão. Quando terminar, selecione **Update user**.

| Nome da permissão | Descrição |
|----------|-----------|
| Manage company settings | Permite que os usuários modifiquem qualquer configuração da empresa. |
| Create and delete workspaces | Permite que os usuários criem e excluam espaços de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Company" }

{% endtab %}
{% tab Espaço de trabalho %}

### Espaço de trabalho {#workspace}

Você pode dar a um usuário diferentes permissões para cada espaço de trabalho ao qual ele pertence na Braze. Para gerenciar as permissões de nível de espaço de trabalho, selecione **Select workspaces and permissions** e escolha suas permissões manualmente para selecionar ou atribuir um conjunto de permissões [que você criou anteriormente]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_creating-a-permission-set).

Se você precisar dar a um usuário permissões diferentes para diferentes espaços de trabalho, repita este processo quantas vezes forem necessárias. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% subtabs %}
{% subtab Selecionar manualmente %}

Em **Workspaces**, escolha um ou mais espaços de trabalho no menu suspenso. Depois, em **Permissions**, escolha uma ou mais permissões no menu suspenso. A Braze atribui essas permissões apenas para os espaços de trabalho que você selecionou. Opcionalmente, você pode selecionar **Enable Admin Access** se quiser conceder permissões totais para esse espaço de trabalho.

Quando terminar, selecione **Update user**.

![Permissões de nível de espaço de trabalho sendo selecionadas manualmente na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual_legacy.png %})

{% endsubtab %}
{% subtab Atribuir conjunto de permissões %}

Em **Workspaces**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Permission Sets**, escolha um conjunto de permissões. A Braze atribui essas permissões apenas para os espaços de trabalho que você selecionou.

Quando terminar, selecione **Update user**.

![Permissões de nível de espaço de trabalho sendo atribuídas por meio de um conjunto de permissões na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set_legacy.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportando permissões de usuário {#exporting-user-permissions}

Para baixar uma lista dos seus usuários e suas permissões, acesse **Configurações** > **Usuários da Empresa** e selecione **Export Users**. Um arquivo CSV será enviado para o seu endereço de e-mail em breve.

![A página "Usuários da Empresa" na Braze com a opção "Export Users" em foco.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Lista de permissões {#list-of-permissions}

| Nível | Nome | Definição |
|---|---|---|
| Administrador | Admin | Permite que os usuários acessem todos os recursos disponíveis. Esta é a configuração padrão para todos os novos usuários. Pode atualizar as configurações da empresa (nome da empresa e fuso horário), o que os usuários limitados não podem fazer. |
| Empresa | Create and delete workspaces | Permite que os usuários criem e excluam espaços de trabalho. |
| Empresa | Manage company settings | Permite que os usuários modifiquem qualquer configuração da empresa. |
| Espaço de trabalho | Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers | Permite que os usuários visualizem métricas de desempenho de Campaigns e Canvas, criem e dupliquem rascunhos de Campaigns e Canvas, editem rascunhos e modelos de Campaigns e Canvas, visualizem rascunhos de Segments, modelos e mídias, criem modelos, façam upload de mídias, criem ou atualizem listas de códigos promocionais, visualizem relatórios de engajamento e visualizem configurações de mensagens globais no dashboard. No entanto, os usuários com essa permissão não podem pausar ou editar conteúdo ativo existente.<br><br> Quando essa permissão é configurada como uma [permissão de equipe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), se quaisquer Campaigns ou Canvas no [relatório de engajamento]({{site.baseurl}}/user_guide/analytics/reporting/engagement_reports/) estiverem fora das equipes atribuídas ao usuário ou não tiverem equipes atribuídas, o relatório ficará oculto para o usuário. |
| Espaço de trabalho | Access Dev Console | Permite acesso total às seguintes configurações e registros:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>Chaves de API</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Grupos internos</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Registro de atividades de envio de mensagem</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Registro de usuários de eventos</a></li></ul>{:/} |
| Espaço de trabalho | Approve and Deny Campaigns | Permite que os usuários aprovem ou rejeitem Campaigns. O [fluxo de trabalho de aprovação para Campaigns]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão se aplique. Esta configuração está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta se quiser participar do acesso antecipado. |
| Espaço de trabalho | Approve and Deny Canvases | Permite que os usuários aprovem ou rejeitem Canvas. O [fluxo de trabalho de aprovação para Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão se aplique. |
| Espaço de trabalho | Edit Currents Integrations | Permite que os usuários modifiquem uma conexão Currents, incluindo credenciais. Por padrão, os usuários atribuídos à permissão "External Integrations" também recebem essa permissão. |
| Espaço de trabalho | Edit Segments | Permite que os usuários criem e editem Segments. Você ainda pode criar Campaigns com Segments e filtros existentes sem essa permissão. Você precisa dessa permissão para gerar um segmento a partir de usuários em um CSV ou redirecionar o grupo de usuários no CSV. |
| Espaço de trabalho | Export User Data | Permite que os usuários exportem seus dados de usuários de Segments, Campaigns e Canvas. Essa permissão inclui informações confidenciais do usuário, como nomes, endereços de e-mail e outras informações de identificação pessoal (IPI) coletadas. Para exportar CSVs do dashboard, você deve ter esta permissão e a permissão "View PII". |
| Espaço de trabalho | Import and Update User Data | Permite que os usuários importem arquivos CSV e atualizem arquivos de usuários do app, bem como visualizem a página de importação de usuário. Isso também permite que você edite o status de inscrição de um usuário e suas regras de aceitação/recusa de grupo de inscrições. |
| Espaço de trabalho | Launch and Manage Content Blocks | Permite que os usuários lancem e gerenciem [Content Blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/). |
| Espaço de trabalho | Launch Preference Centers | Permite que os usuários lancem [Centrais de Preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/). |
| Espaço de trabalho | Manage Apps | Permite que os usuários editem **App Settings**. |
| Espaço de trabalho | Manage Catalogs Dashboard Permission | Permite que os usuários criem e gerenciem catálogos. |
| Espaço de trabalho | Manage Dashboard Users | Permite que os não administradores visualizem, editem e gerenciem a página **Company Users** e gerenciem os usuários do dashboard em seu espaço de trabalho, modificando as permissões de qualquer usuário, inclusive eles próprios. Os usuários com essa permissão não podem excluir usuários (somente os administradores podem excluir usuários).<br><br>Isso corresponde à permissão legada `MANAGE_DEVELOPERS_AND_PERMISSIONS`. |
| Espaço de trabalho | Manage Email Settings | Permite que os usuários salvem as alterações de configuração de e-mail (**Settings** > **Email Preferences**). |
| Espaço de trabalho | Manage Events, Attributes, Purchases | Permite que os usuários editem atributos personalizados (usuários sem essa capacidade ainda podem visualizar atributos personalizados), editem e visualizem propriedades de eventos personalizados e editem e visualizem propriedades de produtos em **Data Settings**. |
| Espaço de trabalho | Manage External Integrations | Permite acesso a todas as guias em **Technology Partners**, capacidade de sincronizar a Braze com outras plataformas e acesso para gerenciar [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/). |
| Espaço de trabalho | Manage Feature Flags | Permite que os usuários criem ou editem [Feature Flags]({{site.baseurl}}/developer_guide/feature_flags/). |
| Espaço de trabalho | Manage Media Library Assets | Permite que os usuários adicionem, editem e excluam ativos da biblioteca de mídia. |
| Espaço de trabalho | Manage Subscription Groups | Permite que os usuários criem e gerenciem grupos de inscrições. |
| Espaço de trabalho | Manage Tags | Permite que os usuários editem ou excluam tags (em **Tag Management**). Você não precisa dessa permissão para adicionar tags a Campaigns ou Segments. |
| Espaço de trabalho | Manage Teams | Permite que os usuários gerenciem **Internal Teams**. A capacidade de selecionar esta permissão depende do seu contrato com a Braze.<br><br>Isso corresponde à permissão legada `MANAGE_TERRITORIES`. |
| Espaço de trabalho | Manage Transformations | Permite que os usuários criem e gerenciem Transformações de Dados. |
| Espaço de trabalho | Send Campaigns, Canvases | Permite que os usuários editem, arquivem e interrompam Campaigns e Canvas, criem Campaigns e lancem Canvas. |
| Espaço de trabalho | View Billing Details | Permite que os usuários visualizem inscrições e faturamento. |
| Espaço de trabalho | View Currents Integration | Permite que os usuários visualizem todas as informações sobre uma conexão Currents, excluindo credenciais. Por padrão, os usuários atribuídos à permissão "Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers" também recebem essa permissão. |
| Espaço de trabalho | View Custom Attributes Marked as PII | Permite que usuários não administradores visualizem atributos personalizados que contenham informações confidenciais e estejam marcados como informações de identificação pessoal (IPI). |
| Espaço de trabalho | View PII | Permite que os usuários visualizem os campos de informações de identificação pessoal (IPI) conforme definido pela sua empresa no dashboard. Os usuários também podem visualizar os campos de IPI na guia **Preview as a User** das prévias de mensagens.<br><br>Você precisa desta permissão para usar o [Criador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), pois permite acesso direto a alguns dados de clientes. Para exportar CSVs do dashboard, os usuários precisam tanto desta permissão quanto da permissão "Export User Data". |
| Espaço de trabalho | View User Profiles PII Compliant | Permite que os usuários visualizem perfis de usuários que contenham campos que sua empresa definiu como informações de identificação pessoal (IPI), mas os campos de IPI são ocultados.<br><br>Você precisa desta permissão para usar a ferramenta de busca de usuários. |
| Espaço de trabalho | View Transformations | Permite que os usuários visualizem [Transformações de Dados da Braze]({{site.baseurl}}/user_guide/data/data_transformation/overview/). |
| Espaço de trabalho | View Usage Data | Permite que os usuários visualizem o uso do app, incluindo os painéis de desempenho do canal. |
| Espaço de trabalho | Merge Duplicate Users | Permite que os usuários mesclem perfis de usuário duplicados. |
| Espaço de trabalho | Preview Duplicate Users | Permite que os usuários vejam uma prévia de quais perfis de usuário estão duplicados. |
| Espaço de trabalho | Create and Edit Canvas Templates | Permite que os usuários criem e editem modelos de Canvas. |
| Espaço de trabalho | View Canvas Templates | Permite que os usuários visualizem os modelos de Canvas. |
| Espaço de trabalho | Archive Canvas Templates | Permite que os usuários arquivem modelos de Canvas. |
| Espaço de trabalho | Manage Custom Event Property Segmentation | Permite que os usuários criem segmentos com base na recência e na frequência da propriedade do evento. |
| Espaço de trabalho | Publish Landing Pages | Permite que os usuários publiquem [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/). |
| Espaço de trabalho | Create Landing Page Drafts | Permite que os usuários criem e salvem rascunhos de landing pages. |
| Espaço de trabalho | Access Landing Pages | Permite que os usuários acessem a página **Landing Pages**. |
| Espaço de trabalho | Create and Edit Landing Page Templates | Permite que os usuários criem e editem modelos de landing page. |
| Espaço de trabalho | View Landing Page Templates | Permite que os usuários visualizem modelos de landing page. |
| Espaço de trabalho | Archive Landing Page Templates | Permite que os usuários arquivem modelos de landing page. |
| Espaço de trabalho | View Custom AI Agents | Permite que os usuários visualizem [agentes de IA personalizados]({{site.baseurl}}/user_guide/brazeai/agents/). Esse recurso está em beta. |
| Espaço de trabalho | Create Custom AI Agents | Permite que os usuários criem agentes de IA personalizados. Esse recurso está em beta. |
| Espaço de trabalho | Edit Custom AI Agents | Permite que os usuários editem agentes de IA personalizados. Esse recurso está em beta. |
| Espaço de trabalho | Support Tickets | Create Support Ticket | Cria e atualiza tickets de suporte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="List of permissions" }