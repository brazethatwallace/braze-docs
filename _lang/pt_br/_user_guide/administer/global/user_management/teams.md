---
nav_title: Equipes
article_title: Equipes
page_order: 2
page_type: reference
alias: /teams/
description: "Este artigo de referência cobre como usar as Equipes da Braze no dashboard. Aqui, você pode aprender como criar Equipes, atribuir funções e atribuir tags e filtros."

---

# Equipes {#teams}

> Como administrador da Braze, você pode agrupar os usuários da sua empresa em Equipes com diferentes funções e permissões de usuário. Isso permite que você tenha múltiplos grupos não relacionados de usuários da empresa trabalhando juntos em um espaço de trabalho, separando os tipos de conteúdo que podem ser editados.

As Equipes podem ser configuradas com base no local da base de clientes, idioma e atributos personalizados, para que os membros da Equipe e os não membros tenham acesso diferente a recursos de envio de mensagens e dados de clientes. Filtros e tags de Equipe podem ser atribuídos em várias ferramentas de engajamento. Não há limite para quantas equipes você pode criar no seu espaço de trabalho.

As Equipes não estão disponíveis em todos os contratos da Braze. Para acessar esse recurso, entre em contato com seu gerente de conta da Braze ou [fale com a gente](mailto:success@braze.com) para uma consulta.

## Como as equipes diferem dos conjuntos de permissões e funções? {#how-do-teams-differ-from-permission-sets-and-roles}

{% multi_lang_include permissions/differences.md content="Differences" %}

## Criar Equipes {#creating-teams}

Acesse **Configurações** > **Equipes internas** e selecione <i class="fas fa-plus"></i> **Adicionar equipe**.

![Janela para adicionar uma nova Equipe.]({% image_buster /assets/img_archive/adding_a_team.png %})

Digite o **Nome da equipe**. Se desejado, use o campo **Definir Equipe (Opcional)** para selecionar um atributo personalizado, local ou idioma para definir melhor a quais dados de usuário a Equipe tem acesso. Por exemplo, um possível caso de uso é realizar [testes com Equipes](#test-with-teams) criando uma Equipe de desenvolvimento que só tem acesso a usuários teste, identificados por um atributo personalizado. Outro caso de uso é restringir a comunicação com usuários com base no produto.

Se uma Equipe for definida por um atributo personalizado, idioma ou país, você pode usar a Equipe para filtrar usuários finais em recursos como Campaigns, Canvas, Content Cards, Segments e muito mais. Para saber mais, consulte [Atribuir tags de Equipe](#tags-and-filters).

## Atribuir usuários a equipes {#assign-users-to-teams}

Administradores da Braze e usuários limitados com a permissão de nível de empresa "Can Manage Company Settings" podem atribuir permissões de nível de equipe a um usuário da empresa com acesso limitado. Quando atribuídos a uma equipe, os usuários da empresa ficam limitados a apenas ler ou gravar dados disponíveis para suas equipes específicas, como idioma do usuário, local ou atributo personalizado, conforme definido quando a equipe foi criada.

### Limitar permissões de usuário da empresa sem excluir um usuário {#limit-company-user-permissions-without-deleting-a-user}

Para impedir que um usuário da empresa faça login e ao mesmo tempo preservar sua conta, [suspenda o usuário]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#suspending-company-users). A suspensão coloca a conta em um estado inativo em que o usuário não consegue fazer login.

Se o usuário precisar continuar podendo fazer login com capacidades limitadas, acesse **Configurações** > **Usuários da empresa**, selecione o usuário e edite suas permissões. Remova as permissões de nível de espaço de trabalho para Campaigns, Canvas, Segments e dados de usuários, e deixe apenas o acesso mínimo — por exemplo, "View Media Library Assets". Para saber mais, consulte [Editar permissões de um usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions).

As permissões de equipe funcionam sobre as permissões do espaço de trabalho. Se você atribuir o usuário a uma equipe, conceda apenas as permissões mínimas de nível de equipe necessárias e não conceda permissões para Campaigns, Canvas, Segments ou perfis de usuário. Eles permanecem no espaço de trabalho e podem fazer login, mas não conseguem executar a maioria das ações de envio de mensagens ou de público.

Para atribuir um usuário a uma equipe, acesse **Configurações** > **Usuários da empresa** e selecione o usuário que você deseja adicionar à sua equipe.

Em seguida, execute as seguintes etapas:

1. Na seção **Permissões de nível de espaço de trabalho**, adicione o usuário ao espaço de trabalho apropriado, caso ele ainda não esteja incluído.

![Permissões de nível de espaço de trabalho com a permissão de modelo de banner definida.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2. Selecione **+ Adicionar permissões de nível de equipe** e, em seguida, selecione a **Equipe** à qual você deseja adicionar este usuário.
3. Atribua permissões específicas na seção de permissões da **Equipe**.

![Permissões de modelo de landing page de nível de equipe.]({% image_buster /assets/img/teams.png %})

### Permissões de nível de equipe disponíveis {#available-team-level-permissions}

A seguir estão todas as permissões disponíveis que você pode atribuir no nível de equipe. Quaisquer permissões não listadas aqui são concedidas apenas no nível do espaço de trabalho, e essas permissões aparecerão como "--" na coluna de permissões de **Equipes**.

- View Campaigns
- Edit Campaigns
- Archive Campaigns
- Launch Campaigns
- Approve Campaigns
- View Canvases
- Edit Canvases
- Archive Canvases
- Launch Canvases
- Approve Canvases
- View Content Blocks
- Edit Content Blocks
- Archive Content Blocks
- Launch Content Blocks
- View Segments
- Edit Segments
- Archive Segments
- View IAM Templates
- Edit IAM Templates
- Archive IAM Templates
- View Email Templates
- Edit Email Templates
- Archive Email Templates
- View Webhook Templates
- Edit Webhook Templates
- Archive Webhook Templates
- View Email Link Templates
- Edit Email Link Templates
- View Media Library Assets
- Edit Media Library Assets
- Delete Media Library Assets
- Export User Data
- View User Profiles (PII Redacted)
- View PII
- Edit Dashboard Users
- Edit Canvas Templates
- View Canvas Templates
- Archive Canvas Templates
- View Dashboard Reports
- Edit Dashboard Reports
- Delete Dashboard Reports

Para ver descrições do que cada permissão de usuário inclui e como usá-las, consulte nossa seção [Permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

## Atribuir tags de Equipe {#tags-and-filters}

Você pode atribuir uma Equipe a Canvas, Campaigns, Content Cards, Segments, modelos de e-mail, modelos de webhook, Content Blocks e ativos da biblioteca de mídia com o filtro **Adicionar equipe**.

Para Canvas, a Braze só verifica se os usuários correspondem aos critérios do filtro de equipe quando eles entram no Canvas. Depois que um usuário entra em um Canvas, ele continua recebendo mensagens de todas as etapas do Canvas, mesmo que seus atributos mudem e ele não corresponda mais aos critérios do filtro de equipe. Os filtros de equipe não se comportam como [validações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations), que reavaliam os usuários a cada envio de etapa de mensagem.

![Adicionando uma tag de Equipe a uma campanha.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Com base nas definições aplicadas quando a Equipe foi criada, quando um filtro de Equipe é atribuído, o público dessa ferramenta de engajamento é restrito a perfis de usuário que correspondem à definição.
- Com base nas permissões atribuídas, os membros da Equipe só poderão acessar ferramentas de engajamento do dashboard que tenham o filtro de Equipe deles configurado. Se tiverem permissões de espaço de trabalho limitadas ou nenhuma, eles devem adicionar um filtro de Equipe a determinados objetos antes de poder salvá-los ou lançá-los. Os membros da Equipe também podem filtrar Canvas, Campaigns, Content Cards e Segments por Equipe para identificar conteúdo relevante para eles.
- Usuários com permissões apenas de nível de Equipe não veem os filtros **Criado por** ou **Última edição por** nas páginas de Segments, Campaigns ou Canvas. A Braze oculta esses filtros para que usuários com acesso apenas de Equipe não possam navegar por todos os usuários da Braze a partir desses menus suspensos.

### Casos de uso {#use-cases}

Considere os dois cenários a seguir para uma profissional de marketing na Braze chamada Michelle. Michelle é membro de uma Equipe chamada "Development". Ela tem acesso a todas as permissões de nível de Equipe para a Equipe Development.

{% tabs %}
{% tab Cenário 1 - Apenas permissões de Equipe %}

Neste cenário, Michelle é uma usuária limitada que não tem permissões de nível de espaço de trabalho. Suas permissões se parecem com algo assim:

![Permissões personalizadas sem permissões de nível de espaço de trabalho e 16 permissões baseadas em equipe.]({% image_buster /assets/img_archive/scenario1.png %})

Com base nas permissões atribuídas a Michelle, sempre que ela criar uma campanha, ela só poderá atribuir a Equipe "Development" a essa campanha. Ela não pode lançar a campanha a menos que a Equipe esteja atribuída, e não pode visualizar ou acessar nenhuma outra tag de Equipe.

![Menu suspenso de tag de Equipe da campanha que exibe apenas a tag de Equipe "Development".]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Cenário 2 - Permissões de Equipe e de espaço de trabalho %}

Neste cenário, Michelle ainda é membro da Equipe Development, mas também tem uma permissão adicional de nível de espaço de trabalho.

![Permissões personalizadas com uma permissão de nível de espaço de trabalho e 15 permissões baseadas em equipe.]({% image_buster /assets/img_archive/scenario2.png %})

Como Michelle tem a permissão de nível de espaço de trabalho "Acessar Campaigns, Canvas, cartões, Content Blocks, Feature Flags, Segments, biblioteca de mídia e Central de Preferências", ela pode visualizar e atribuir outros filtros de Equipe à campanha que criar.

![Menu suspenso de tag de Equipe da campanha com múltiplas tags de Equipe.]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Assim como no primeiro cenário, Michelle deve adicionar a tag de Equipe Development à campanha antes de poder lançá-la.

{% endtab %}
{% endtabs %}

## Teste com equipes {#test-with-teams}

Um possível caso de uso para equipes é criar um sistema de aprovação baseado em equipes para testar e lançar conteúdo em um ambiente de produção.

Para isso, crie uma equipe "Desenvolvimento" que tenha acesso apenas a usuários teste. Você pode limitar uma equipe para acessar apenas usuários teste se seus usuários teste forem identificáveis por um atributo personalizado. Em seguida, adicione o atributo personalizado como definição ao criar ou editar a equipe (consulte a seção anterior [Criando equipes](#creating-Teams)). Seus aprovadores devem ter acesso a todos os usuários.

O processo geral seria o seguinte:

1. A equipe de Desenvolvimento cria uma Campaign e adiciona a tag de equipe "Desenvolvimento".
2. A equipe de Desenvolvimento lança a Campaign para usuários teste.
3. A equipe de Aprovação valida o design local da Campaign, promove e lança. Para lançar, a equipe de Aprovação altera a tag de equipe de "Desenvolvimento" para "[Todas as equipes]" e relança a Campaign.

Para alterações em Campaigns ativas:

1. A equipe de Desenvolvimento clona a Campaign em execução, adiciona a tag de equipe "Desenvolvimento" e salva.
2. A equipe de Desenvolvimento faz as edições e compartilha com a equipe de Aprovação.
3. A equipe de Aprovação remove a tag de equipe "Desenvolvimento", pausa a Campaign anterior e lança a nova Campaign.

## Arquivar uma equipe existente {#archive-an-existing-team}

Você pode arquivar equipes na página **Equipes internas**.

Selecione uma ou mais equipes para arquivar. Se a equipe não estiver associada a nenhum objeto na Braze, ela será arquivada imediatamente. Se a equipe estiver associada a um objeto, será apresentada uma opção para remover a equipe após o processo de arquivamento ou substituir a equipe.

![Arquivando uma equipe associada a um objeto na Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Os administradores da Braze podem desarquivar uma equipe selecionando a equipe arquivada e clicando em **Desarquivar**.