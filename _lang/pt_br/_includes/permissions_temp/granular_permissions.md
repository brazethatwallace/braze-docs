{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

## Criando um conjunto de permissões {#creating-a-permission-set}

Use conjuntos de permissões para agrupar permissões relacionadas a áreas ou ações específicas. Você pode aplicar conjuntos de permissões a usuários do dashboard que precisam do mesmo acesso em diferentes espaços de trabalho. Para criar um conjunto de permissões, acesse **Configurações** > **Configurações de Permissão** e selecione **Criar conjunto de permissões**. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nome|Permissões|
|-----------|----------------|
|Desenvolvedores|"Ver Chaves de API", "Editar Chaves de API", "Ver Grupos Internos", "Editar Grupos Internos", "Ver Registro de Atividade de Mensagens", "Ver Registro de Usuários de Eventos", "Ver identificadores de API", "Ver Dashboard de Uso da API", "Ver Limites da API", "Ver Alertas de Uso da API", "Editar Alertas de Uso da API", "Ver Depurador do SDK", "Editar Depurador do SDK".|
|Profissionais de Marketing|"Ver Campaigns", "Editar Campaigns", "Arquivar Campaigns", "Ver Canvas", "Editar Canvas", "Arquivar Canvas", "Ver Regras de Limitação de Frequência", "Editar Regras de Limitação de Frequência", "Ver Priorização de Mensagens", "Editar Priorização de Mensagens", "Ver Content Blocks", "Ver Feature Flags", "Editar Feature Flags", "Arquivar Feature Flags", "Ver Segments", "Editar Segments", "Editar Grupo de Controle Global", "Ver Modelos IAM", "Editar Modelos IAM", "Arquivar Modelos IAM", "Ver Modelos de E-mail", "Editar Modelos de E-mail", "Arquivar Modelos de E-mail", "Ver Modelos de Webhook", "Editar Modelos de Webhook", "Arquivar Modelos de Webhook", "Ver Modelos de Link de E-mail", "Editar Modelos de Link de E-mail", "Ver Ativos da Biblioteca de Mídia", "Ver Locais", "Editar Locais", "Arquivar Locais", "Ver Códigos de Promoção", "Editar Códigos de Promoção", "Exportar Códigos de Promoção", "Ver Centrais de Preferências", "Editar Centrais de Preferências", "Editar Relatórios do Dashboard", "Ver Modelos de Banner", "Ver Configurações de Localização", "Usar Operator", "Ver Agentes do Decisioning Studio".|
|Gerenciamento de Usuários|"Editar Usuários do Dashboard", "Ver Equipes", "Editar Equipes", "Arquivar Equipes".|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Criando uma função {#creating-a-role}

As funções permitem mais estrutura ao agrupar suas permissões personalizadas individuais com os controles de acesso do espaço de trabalho. Isso é especialmente útil se você tiver muitas marcas ou espaços de trabalho regionais em um dashboard. Com funções, você pode adicionar usuários do dashboard aos espaços de trabalho certos e conceder diretamente as permissões associadas. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nome da Função    | Espaço de trabalho | Permissões
----------- | ----------- | ---------
| Profissional de Marketing - Marcas de Moda | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "Ver Campaigns", "Editar Campaigns", "Arquivar Campaigns", "Ver Canvas", "Editar Canvas", "Arquivar Canvas", "Ver Content Blocks", "Editar Content Blocks", "Arquivar Content Blocks", "Lançar Content Blocks", "Ver Feature Flags", "Editar Feature Flags", "Arquivar Feature Flags", "Ver Segments", "Editar Segments", "Ver Modelos de Banner", "Editar Modelos de Banner", "Ver Modelos de E-mail", "Editar Modelos de E-mail", "Ver Ativos da Biblioteca de Mídia", "Editar Ativos da Biblioteca de Mídia", "Excluir Ativos da Biblioteca de Mídia", "Ver Locais", "Editar Locais", "Arquivar Locais", "Ver Códigos de Promoção", "Editar Códigos de Promoção", "Exportar Códigos de Promoção", "Ver Centrais de Preferências", "Editar Centrais de Preferências". |
| Profissional de Marketing - Marcas de Cuidados com a Pele | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} |"Ver Campaigns", "Editar Campaigns", "Arquivar Campaigns", "Ver Canvas", "Editar Canvas", "Arquivar Canvas", "Ver Content Blocks", "Editar Content Blocks", "Arquivar Content Blocks", "Lançar Content Blocks", "Ver Feature Flags", "Editar Feature Flags", "Arquivar Feature Flags", "Ver Segments", "Editar Segments", "Ver Modelos de Banner", "Editar Modelos de Banner", "Ver Modelos de E-mail", "Editar Modelos de E-mail", "Ver Ativos da Biblioteca de Mídia", "Editar Ativos da Biblioteca de Mídia", "Excluir Ativos da Biblioteca de Mídia", "Ver Locais", "Editar Locais", "Arquivar Locais", "Ver Códigos de Promoção", "Editar Códigos de Promoção", "Exportar Códigos de Promoção", "Ver Centrais de Preferências", "Editar Centrais de Preferências".|
| Gerenciamento de Usuários - Todas as Marcas | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Editar Usuários do Dashboard", "Ver Equipes", "Editar Equipes", "Arquivar Equipes"|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## Como os conjuntos de permissões e funções diferem das Equipes? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions.md content="Differences" %}

### Considerações para adicionar permissões de usuário às Equipes {#considerations-for-adding-user-permissions-to-teams}

Você pode encontrar dificuldades ao tentar salvar permissões no dashboard da Braze, especialmente ao adicionar ou remover usuários de um espaço de trabalho, ou ao adicioná-los a uma Equipe. O botão **Salvar/Atualizar Usuários** pode ficar desativado se as permissões do usuário forem idênticas às que ele já possui no nível do espaço de trabalho. Essa restrição existe porque não há benefício em ter uma Equipe se todos os usuários possuem as mesmas permissões que todo o espaço de trabalho.

Para adicionar um usuário a uma Equipe com sucesso mantendo as mesmas permissões, não atribua nenhuma permissão no nível do espaço de trabalho. Em vez disso, atribua permissões exclusivamente no nível da equipe.

## Usuários limitados {#limited-users}

Usuários limitados têm permissões específicas que permitem gerenciar certos aspectos do dashboard da Braze, mas com restrições em comparação com administradores da empresa e administradores de espaço de trabalho.

| Escopo | Descrição |
| --- | --- |
| Permissões | Usuários limitados podem editar as permissões de outros usuários limitados se tiverem a permissão "Editar Usuários do Dashboard". Eles também podem criar novos usuários limitados e modificar seus conjuntos de permissões. No entanto, não podem criar ou gerenciar contas de administrador da empresa. |
| Limitações de função | Se um usuário limitado tiver todas as permissões, exceto "Administrador do Espaço de Trabalho", ele ainda terá acesso a todas as outras permissões normalmente concedidas a um administrador do espaço de trabalho. |
| Visibilidade das permissões | Se um usuário limitado tiver a permissão "Editar Usuários do Dashboard" para um espaço de trabalho (como Dev), mas não para outro (como Prod), ele não verá as permissões do espaço de trabalho Prod na página de detalhes dos usuários do dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparando usuários limitados {#comparing-limited-users}

| Tipo de usuário limitado | Descrição |
| --- | --- |
| Administrador do Espaço de Trabalho | Os Administradores do Espaço de Trabalho têm permissões específicas para gerenciar espaços de trabalho, mas não têm a mesma autoridade que os Administradores da Empresa. Usuários limitados podem herdar permissões semelhantes às dos Administradores do Espaço de Trabalho se tiverem as permissões necessárias marcadas. |
| Administrador (Administrador da Empresa) | Os Administradores da Empresa têm permissões mais amplas, incluindo a capacidade de excluir usuários do dashboard. No entanto, eles não podem excluir suas próprias contas e devem entrar em contato com outro Administrador da Empresa para essa ação. |
| Acesso somente para visualização | Para acessar partes do dashboard, como a página de Campaigns, os usuários devem ter permissões de visualização atribuídas a eles.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erro de acesso limitado {#limited-access-error}

Os usuários podem encontrar mensagens como "Você precisa de permissões de 'Ver Landing Pages' para acessar esta página". Nesses casos, o usuário e o administrador da conta devem verificar se as permissões necessárias foram concedidas. Se sim, tente resolver o problema desativando e reativando as permissões do usuário.

{% alert note %}
Não é possível mesclar ou importar permissões de usuário de um usuário do dashboard para outro.
{% endalert %}

## Editando as permissões de um usuário {#editing-a-users-permissions}

Para editar as permissões atuais de administrador, empresa ou espaço de trabalho de um usuário, acesse **Configurações** > **Usuários da Empresa** e selecione o nome dele.

![A página "Usuários da Empresa" na Braze mostrando uma tabela de usuários do dashboard.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Administrador {#admin}

Os administradores têm acesso a todos os recursos e a capacidade de modificar qualquer configuração da empresa. Eles podem:

- Alterar [configurações de aprovação]({{site.baseurl}}/user_guide/messaging/governance/approvals/#turning-on-the-approval-workflow)
- Adicionar, editar, excluir, suspender ou reativar outros [usuários da Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/#adding-company-users)
- Exportar usuários da Braze como um arquivo CSV

Para conceder ou remover privilégios de administrador, selecione **Este usuário é um administrador** e depois selecione **Atualizar usuário**.

![Os detalhes do usuário selecionado com a caixa de seleção de administrador em foco.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Se você remover os privilégios de administrador de um usuário, ele não poderá acessar a Braze até que você atribua a ele pelo menos uma [permissão em nível de empresa ou em nível de espaço de trabalho]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Company %}

### Empresa {#company}

Para gerenciar as seguintes permissões em nível de empresa para um usuário, marque ou desmarque a caixa ao lado da permissão. Quando terminar, selecione **Atualizar usuário**.

|Nome da permissão|Descrição|
|----------|-----------|
|Gerenciar configurações da empresa|Permite que os usuários modifiquem as configurações de permissão e verificação do remetente.|
|Criar e excluir espaços de trabalho|Permite que os usuários criem e excluam espaços de trabalho.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espaço de trabalho {#workspace}

Você pode dar a um usuário diferentes permissões para cada espaço de trabalho ao qual ele pertence na Braze. Para gerenciar as permissões em nível de espaço de trabalho, selecione **Selecionar espaços de trabalho e permissões** e escolha as permissões manualmente ou atribua um [conjunto de permissões ou função]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) que você criou anteriormente. Se você precisar dar a um usuário permissões diferentes para diferentes espaços de trabalho, repita este processo quantas vezes forem necessárias. Para uma descrição de cada permissão, consulte [Lista de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Permissões**, selecione uma ou mais permissões. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou. Opcionalmente, você pode selecionar **Atribuir acesso de administrador do espaço de trabalho** se desejar dar a eles permissões completas para este espaço de trabalho.

Quando terminar, selecione **Atualizar usuário**.

![Permissões em nível de espaço de trabalho sendo selecionadas manualmente na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Conjuntos de permissão**, escolha um conjunto de permissões. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou.

Quando terminar, selecione **Atualizar usuário**.

![Permissões em nível de espaço de trabalho sendo atribuídas por meio de um conjunto de permissões na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Assign role %}

Em **Espaços de Trabalho**, escolha um ou mais espaços de trabalho no menu suspenso. Em seguida, em **Função**, escolha uma função. Os usuários receberão essas permissões apenas nos espaços de trabalho que você selecionou.

Quando terminar, selecione **Atualizar usuário**.

![Permissões em nível de espaço de trabalho sendo atribuídas por meio de uma função na Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportando permissões de usuário {#exporting-user-permissions}

Para baixar uma lista dos seus usuários e suas permissões, acesse **Configurações** > **Usuários da Empresa** e selecione **Exportar Usuários**. Um arquivo CSV será enviado para o seu endereço de e-mail em breve.

![A página "Usuários da Empresa" na Braze com a opção "Exportar Usuários" em foco.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Lista de permissões {#list-of-permissions}

### Envio de mensagens {#messaging}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Campaigns | Ver Campaigns | Ver Campaigns |
| Campaigns | Lançar Campaigns | Iniciar, parar, pausar ou retomar Campaigns existentes |
| Campaigns | Arquivar Campaigns | Mover Campaigns para o arquivo |
| Campaigns | Editar Campaigns | Criar e atualizar Campaigns |
| Campaigns | Aprovar e negar Campaigns | Aprovar ou negar Campaigns. O [fluxo de aprovação para Campaigns]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão se aplique. Esta configuração está atualmente em acesso antecipado. Entre em contato com seu gerente de conta se estiver interessado em participar do acesso antecipado. |
| Canvas | Ver Canvas | Ver Canvas |
| Canvas | Arquivar Canvas | Mover Canvas para o arquivo |
| Canvas | Editar Canvas | Criar e atualizar Canvas |
| Canvas | Lançar Canvas | Iniciar, parar, pausar ou retomar Canvas existentes |
| Canvas | Aprovar e negar Canvas | Aprovar ou negar Canvas. O [fluxo de aprovação para Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) deve estar ativado para que essa permissão se aplique. Esta configuração está atualmente em acesso antecipado. Entre em contato com seu gerente de conta se estiver interessado em participar do acesso antecipado. |
| Feature Flags | Ver Feature Flags | Ver Feature Flags |
| Feature Flags | Arquivar Feature Flags | Mover Feature Flags para o arquivo |
| Feature Flags | Editar Feature Flags | Criar e atualizar Feature Flags |
| Limites de frequência | Ver regras de limitação de frequência | Ver regras de limitação de frequência |
| Limites de frequência | Editar regras de limitação de frequência | Criar e atualizar regras de limitação de frequência |
| Landing pages | Ver landing pages | Ver landing pages |
| Landing pages | Publicar landing pages | Tornar uma landing page em rascunho ativa |
| Landing pages | Editar rascunhos de landing page | Criar e salvar rascunhos de landing page |
| Configurações de arquivamento de mensagem | Ver configurações de arquivamento de mensagem | Ver configurações de arquivamento de mensagem sem fazer alterações |
| Configurações de arquivamento de mensagem | Editar configurações de arquivamento de mensagem | Criar e atualizar configurações de arquivamento de mensagem |
| Priorização de mensagens | Ver priorização de mensagens | Ver configurações de priorização de mensagens sem fazer alterações |
| Priorização de mensagens | Editar priorização de mensagens | Criar e atualizar configurações de priorização de mensagens |
| WhatsApp Flows | Ver WhatsApp Flows | Ver todos os WhatsApp Flows |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Público {#audience}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Grupo de Controle Global | Ver Grupo de Controle Global | Ver página de configuração do Grupo de Controle Global |
| Grupo de Controle Global | Editar Grupo de Controle Global | Criar e salvar alterações no Grupo de Controle Global. Os usuários com a permissão "Editar Grupo de Controle Global" também devem ter permissões para "Editar Campaigns" e "Editar Canvas". Os usuários com a permissão "Editar Grupo de Controle Global" também recebem a permissão "Ver Grupo de Controle Global". |
| Locais | Arquivar locais | Mover locais para o arquivo |
| Locais | Ver locais | Ver locais |
| Locais | Editar locais | Criar e editar locais |
| Segments | Ver Segments | Ver Segments. Os usuários devem ter a permissão "Ver Segments" para ter a permissão "Editar Segments" ou "Arquivar Segments" |
| Segments | Arquivar Segments | Arquivar e desarquivar Segments. Os usuários com a permissão "Arquivar Segments" também devem ter a permissão "Ver Segments" |
| Segments | Editar Segments | Criar e atualizar Segments. Os usuários com a permissão "Editar Segments" também devem ter a permissão "Ver Segments" |
| Dados de usuários | Ver importação de usuários | Ver importações de usuários CSV sem fazer alterações |
| Dados de usuários | Importar usuários | Fazer upload de usuários para o dashboard |
| Dados de usuários | Editar dados de usuários | Criar e atualizar dados de usuários |
| Dados de usuários | Exportar dados de usuários | Baixar usuários do dashboard |
| Registros de exclusão de usuários | Ver registros de mesclagem de usuários | Ver uma lista de registros de mesclagem de usuários |
| Usuários | Ver perfis de usuário (IPI ocultada) | Ver perfis de usuário de forma compatível com IPI |
| Usuários duplicados | Mesclar usuários duplicados | Combinar usuários duplicados em um único usuário. As duplicatas são removidas após a mesclagem |
| Usuários | Excluir usuários | Excluir permanentemente usuários do dashboard individualmente ou em massa |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Modelo {#template}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Modelos de banner | Ver modelos de banner | Ver modelos de banner |
| Modelos de banner | Arquivar modelos de banner | Mover modelos de banner para o arquivo |
| Modelos de banner | Editar modelos de banner | Criar e atualizar modelos de banner |
| Modelos de Canvas | Ver Modelos de Canvas | Ver Modelos de Canvas |
| Modelos de Canvas | Arquivar Modelos de Canvas | Mover Modelos de Canvas para o arquivo |
| Modelos de Canvas | Criar e editar Modelos de Canvas | Criar e atualizar Modelos de Canvas |
| Content Blocks | Ver Content Blocks | Ver Content Blocks |
| Content Blocks | Lançar Content Blocks | Lançar Content Blocks |
| Content Blocks | Arquivar Content Blocks | Mover Content Blocks para o arquivo |
| Content Blocks | Editar Content Blocks | Criar e atualizar Content Blocks |
| Modelos de link de e-mail | Ver modelos de link de e-mail | Ver modelos de link sem fazer alterações |
| Modelos de link de e-mail | Editar modelos de link de e-mail | Criar e atualizar modelos de link |
| Modelos de e-mail | Ver modelos de e-mail | Ver modelos de e-mail |
| Modelos de e-mail | Arquivar modelos de e-mail | Mover modelos de e-mail para o arquivo |
| Modelos de e-mail | Editar modelos de e-mail | Criar e atualizar modelos de e-mail |
| Modelos IAM | Ver modelos IAM | Ver modelos de mensagem no app sem fazer alterações |
| Modelos IAM | Arquivar modelos IAM | Mover modelos IAM para o arquivo |
| Modelos IAM | Editar modelos IAM | Criar e atualizar modelos de mensagem no app |
| Modelos de landing page | Ver modelos de landing page | Ver modelos de landing page |
| Modelos de landing page | Arquivar modelos de landing page | Mover modelos de landing page para o arquivo |
| Modelos de landing page | Editar modelos de landing page | Criar e atualizar modelos de landing page |
| Modelos de webhook | Ver modelos de webhook | Ver modelos de webhook sem fazer alterações |
| Modelos de webhook | Arquivar modelos de webhook | Mover modelos de webhook para o arquivo |
| Modelos de webhook | Editar modelos de webhook | Criar e atualizar modelos de webhook |
| Modelos de mensagem do WhatsApp | Ver modelos de mensagem do WhatsApp | Permite que os usuários vejam [modelos de mensagem do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#step-2-compose-your-whatsapp-message) |
| Modelos de mensagem do WhatsApp | Editar modelos de mensagem do WhatsApp | Permite que os usuários criem modelos de mensagem do WhatsApp no construtor de modelos. Este recurso está atualmente em acesso antecipado. |
| Modelos de mensagem do WhatsApp do Meta | Ver modelos de mensagem do WhatsApp do Meta | Ver todos os modelos do WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Integrações de parceiros {#partner-integrations}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Integrações do Currents | Ver integrações do Currents | Ver integrações do Currents |
| Integrações do Currents | Editar integrações do Currents | Criar, atualizar e excluir integrações do Currents |
| Parceiros de tecnologia | Editar parceiros de tecnologia | Criar e atualizar parceiros de tecnologia |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Configurações de dados {#data-settings}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Catálogos | Ver catálogos | Ver catálogos e seleções |
| Catálogos | Excluir catálogos | Excluir catálogos permanentemente |
| Catálogos | Exportar catálogos | Baixar catálogos do dashboard |
| Catálogos | Editar catálogos | Criar e atualizar catálogos e seleções |
| Ingestão de dados na nuvem | Editar ingestão de dados na nuvem | Criar, atualizar e excluir fontes e sincronizações |
| Atributos personalizados | Ver atributos personalizados | Ver atributos personalizados e relatório de uso |
| Atributos personalizados | Exportar atributos personalizados | Baixar atributos personalizados do dashboard |
| Atributos personalizados | Excluir atributos personalizados | Excluir atributos personalizados permanentemente |
| Atributos personalizados | Bloquear atributos personalizados | Adicionar atributos personalizados a uma lista de bloqueio que restringe o uso no dashboard |
| Atributos personalizados | Editar atributos personalizados | Criar e atualizar atributos personalizados |
| Segmentação de propriedades de eventos personalizados | Editar segmentação de propriedades de eventos personalizados | Ativar e desativar a segmentação para propriedades de eventos personalizados |
| Eventos personalizados | Ver eventos personalizados | Ver eventos personalizados e relatório de uso, e adicionar eventos personalizados ao e-mail do relatório diário de análise de dados |
| Eventos personalizados | Exportar eventos personalizados | Baixar eventos personalizados do dashboard |
| IPI | Ver IPI | Ver IPI |
| Eventos personalizados | Excluir eventos personalizados | Excluir permanentemente eventos personalizados |
| Eventos personalizados | Bloquear eventos personalizados | Adicionar eventos personalizados a uma lista de bloqueio que restringe o uso no dashboard |
| Eventos personalizados | Editar eventos personalizados | Criar e atualizar eventos personalizados |
| Produtos | Ver produtos | Ver produtos |
| Produtos | Bloquear produtos | Adicionar produtos a uma lista de bloqueio que restringe o uso no dashboard |
| Produtos | Editar produtos | Criar e atualizar produtos |
| Segmentação de propriedades de compra | Editar segmentação de propriedades de compra | Ativar e desativar a segmentação para propriedades de eventos de compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Configurações {#settings}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Identificadores de API | Ver identificadores de API | Ver identificadores de API e outros identificadores |
| Chaves de API | Ver chaves de API | Ver chaves de API |
| Chaves de API | Editar chaves de API | Criar e atualizar chaves de API |
| Limites da API | Ver limites da API | Ver limites de taxa da API |
| Alertas de uso da API | Ver alertas de uso da API | Ver alertas de uso da API |
| Alertas de uso da API | Editar alertas de uso da API | Criar e atualizar alertas de uso da API |
| Dados de uso da API | Ver dashboard de uso da API | Ver o dashboard de uso da API |
| Configurações do app | Editar configurações do app | Criar, editar e atualizar apps nas configurações do app |
| Configurações do app | Ver configurações do app | Ver página de configurações do app |
| Configurações de Audience Sync | Ver configurações de Audience Sync | Ver todas as configurações dos parceiros de Audience Sync conectados |
| Usuários do dashboard | Editar usuários do dashboard | Ver, criar e editar usuários da empresa |
| Configurações de e-mail | Ver configurações de e-mail | Ver preferências de e-mail |
| Configurações de e-mail | Editar configurações de e-mail | Ativar e atualizar preferências de e-mail |
| Registro de usuários de eventos | Ver registro de usuários de eventos | Ver registros de usuários de eventos |
| Grupos internos | Ver grupos internos | Ver grupos internos |
| Grupos internos | Excluir grupos internos | Excluir grupos internos |
| Grupos internos | Editar grupos internos | Criar e atualizar grupos internos |
| Registro de atividade de mensagens | Ver registro de atividade de mensagens | Ver registros de atividade de mensagens |
| Configurações multilíngues | Ver configurações de localização | Ver página de configurações de localização multilíngue |
| Configurações multilíngues | Excluir configurações de localização | Excluir localização multilíngue |
| Configurações multilíngues | Editar configurações de localização | Criar localizações multilíngues |
| Centrais de Preferências | Ver Centrais de Preferências | Ver Centrais de Preferências |
| Centrais de Preferências | Editar Centrais de Preferências | Criar e atualizar Centrais de Preferências |
| Centrais de Preferências | Lançar Centrais de Preferências | Tornar um rascunho da Central de Preferências ativo ou atualizar uma existente |
| Configurações de push | Ver configurações de push | Ver configurações de push |
| Configurações de push | Editar configurações de push | Criar e atualizar configurações de push |
| Depurador do SDK | Ver Depurador do SDK | Ver Depurador do SDK ou sessões de depuração |
| Depurador do SDK | Editar Depurador do SDK | Criar e baixar sessões do Depurador do SDK |
| Tags | Ver tags | Ver tags |
| Tags | Excluir tags | Excluir tags permanentemente |
| Tags | Editar tags | Criar e atualizar tags |
| Equipes | Ver equipes | Ver equipes |
| Equipes | Arquivar equipes | Mover equipes para o arquivo |
| Equipes | Editar equipes | Criar e atualizar equipes |
| Configurações do WhatsApp | Ver configurações do WhatsApp | Ver todas as configurações do canal WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Decisioning Studio {#decisioning-studio}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Agentes do Decisioning Studio | Ver agente do Decisioning Studio | Ver configuração dos agentes do Decisioning Studio sem fazer alterações |
| Público do Decisioning Studio | Ver público do Decisioning Studio | Ver detalhes do público nos resumos de configuração dos agentes do Decisioning Studio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Outros {#other}

| Área do produto | Permissão | Definição |
| --- | --- | --- |
| Uso do app | Ver dados de uso | Ver dados de uso |
| Faturamento | Ver detalhes de faturamento | Ver detalhes de faturamento |
| Agentes personalizados | Ver agentes de IA do Console do agente | Permite que os usuários vejam agentes de IA personalizados |
| Agentes personalizados | Arquivar agentes de IA do Console do agente | Permite que os usuários arquivem agentes de IA personalizados |
| Agentes personalizados | Editar agentes de IA do Console do agente | Permite que os usuários criem e atualizem agentes de IA personalizados |
| Atributos personalizados marcados como IPI | Ver atributos personalizados marcados como IPI | Ver atributos personalizados marcados como IPI |
| Relatórios do dashboard | Ver relatórios do dashboard | Ver relatórios sem fazer alterações |
| Relatórios do dashboard | Excluir relatórios do dashboard | Excluir relatórios permanentemente |
| Relatórios do dashboard | Editar relatórios do dashboard | Criar e atualizar relatórios |
| Configurações de domínio | Editar configurações de domínio | Adicionar domínios delegados e domínios personalizados em Domínios Verificados |
| Criptografia em nível de campo | Editar criptografia em nível de campo do identificador | Ativar e atualizar configurações de criptografia em nível de campo |
| Ativos da biblioteca de mídia | Ver ativos da biblioteca de mídia | Ver ativos da biblioteca de mídia |
| Ativos da biblioteca de mídia | Excluir ativos da biblioteca de mídia | Excluir permanentemente ativos da biblioteca de mídia |
| Ativos da biblioteca de mídia | Editar ativos da biblioteca de mídia | Criar e atualizar ativos da biblioteca de mídia |
| Limites de taxa de envio de mensagens | Ver limites de taxa de envio de mensagens | Ver limites de taxa de envio de mensagens no nível do espaço de trabalho |
| Limites de taxa de envio de mensagens | Editar limites de taxa de envio de mensagens | Configurar e editar limites de taxa de envio de mensagens no nível do espaço de trabalho |
| Operator | Usar BrazeAI Operator<sup>TM</sup> | Acessar e usar o Braze Operator para responder perguntas, navegar pela configuração, solucionar problemas e gerar ideias |
| Posicionamentos | Ver posicionamentos | Ver posicionamento de banner |
| Posicionamentos | Arquivar posicionamentos | Mover posicionamentos de banner para o arquivo |
| Posicionamentos | Editar posicionamentos | Ver posicionamentos de banner sem fazer alterações |
| Códigos de promoção | Ver códigos de promoção | Ver códigos promocionais |
| Códigos de promoção | Exportar códigos de promoção | Baixar uma lista de códigos promocionais do dashboard |
| Códigos de promoção | Editar códigos de promoção | Criar e atualizar códigos promocionais |
| Grupos de inscrições | Editar inscrições | Criar e atualizar grupos de inscrições |
| Transformações | Editar Transformação de dados | Criar e atualizar transformações de dados |
| Transformações | Ver Transformação de dados | Ver transformações de dados |
| Registros de exclusão de usuários | Ver registros de exclusão de usuários | Ver registros de exclusão de usuários |
| Tickets de suporte | Criar ticket de suporte | Criar e atualizar tickets de suporte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }