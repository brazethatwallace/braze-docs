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

## Como as Equipes diferem de conjuntos de permissões e funções? {#how-do-teams-differ-from-permission-sets-and-roles}

{% multi_lang_include permissions/differences.md content="Differences" %}

## Criar Equipes {#creating-teams}

Acesse **Configurações** > **Equipes internas** e selecione <i class="fas fa-plus"></i> **Adicionar equipe**.

![Janela para adicionar uma nova Equipe.]({% image_buster /assets/img_archive/adding_a_team.png %})

Digite o **Nome da equipe**. Se desejado, use o campo **Definir Equipe (Opcional)** para selecionar um atributo personalizado, local ou idioma para definir melhor a quais dados de usuário a Equipe tem acesso. Por exemplo, um possível caso de uso é realizar [testes com Equipes](#test-with-teams) criando uma Equipe de desenvolvimento que só tem acesso a usuários teste, identificados por um atributo personalizado. Outro caso de uso é restringir a comunicação com usuários com base no produto.

Se uma Equipe for definida por um atributo personalizado, idioma ou país, você pode usar a Equipe para filtrar usuários finais em recursos como Campaigns, Canvas, Content Cards, Segments e muito mais. Para saber mais, consulte [Atribuir tags de Equipe](#tags-and-filters).

## Atribuir usuários a Equipes {#assign-users-to-teams}

Administradores da Braze e usuários limitados com a permissão de nível de empresa "Pode gerenciar configurações da empresa" podem atribuir permissões de nível de Equipe a um usuário da empresa com acesso limitado. Quando atribuídos a uma Equipe, os usuários da empresa ficam limitados a apenas ler ou gravar dados disponíveis para suas Equipes específicas, como idioma do usuário, local ou atributo personalizado, conforme definido quando a Equipe foi criada.

### Limitar permissões de um usuário da empresa sem excluí-lo {#limit-company-user-permissions-without-deleting-a-user}

Para impedir que um usuário da empresa faça login sem excluir a conta dele, [suspenda o usuário]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#suspending-company-users). A suspensão coloca a conta em um estado inativo, impedindo o login.

Se o usuário precisar continuar com acesso limitado, acesse **Configurações** > **Usuários da empresa**, selecione o usuário e edite suas permissões. Remova as permissões de nível de espaço de trabalho para Campaigns, Canvas, Segments e dados de usuários, e deixe apenas o acesso mínimo — por exemplo, "View Media Library Assets". Para saber mais, consulte [Editar permissões de um usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions).

As permissões de Equipe funcionam em cima das permissões de espaço de trabalho. Se você atribuir o usuário a uma Equipe, conceda apenas as permissões mínimas de nível de equipe necessárias e não conceda permissões para Campaigns, Canvas, Segments ou perfis de usuário. Ele permanecerá no espaço de trabalho e poderá fazer login, mas não poderá executar a maioria das ações de envio de mensagens ou de público.

Para atribuir um usuário a uma Equipe, acesse **Configurações** > **Usuários da empresa** e selecione o usuário que deseja adicionar à sua Equipe.

Em seguida, siga estas etapas:

1. Na seção **Permissões de nível de espaço de trabalho**, adicione o usuário ao espaço de trabalho apropriado, caso ele ainda não esteja incluído.

![Permissões de nível de espaço de trabalho com o conjunto de permissões Banner Template.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2. Selecione **+ Adicionar permissões de nível de equipe** e, em seguida, selecione a **Equipe** à qual deseja adicionar este usuário.
3. Atribua permissões específicas na seção de permissões da **Equipe**.

![Permissões de modelo de landing page de nível de equipe.]({% image_buster /assets/img/teams.png %})

### Permissões de nível de Equipe disponíveis {#available-team-level-permissions}

A seguir estão todas as permissões disponíveis que você pode atribuir no nível de Equipe. Quaisquer permissões não listadas aqui são concedidas apenas no nível do espaço de trabalho, e essas permissões aparecerão como "--" na coluna de permissões de **Equipes**.

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

Você pode atribuir uma Equipe a Canvas, Campaigns, Content Cards, Segments, modelos de e-mail, modelos de webhook, Content Blocks e ativos da Biblioteca de mídia com o filtro **Adicionar equipe**.

![Adicionando uma tag de Equipe a uma campanha.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Com base nas *definições* aplicadas quando a Equipe foi criada, quando um filtro de Equipe é atribuído, o público dessa ferramenta de engajamento é restrito a perfis de usuário que correspondem à definição.
- Com base nas *permissões* atribuídas, os membros da Equipe só poderão acessar ferramentas de engajamento do dashboard que tenham o filtro de Equipe deles configurado. Se tiverem permissões de espaço de trabalho limitadas ou nenhuma, eles devem adicionar um filtro de Equipe a determinados objetos antes de poder salvá-los ou lançá-los. Os membros da Equipe também podem filtrar Canvas, Campaigns, Content Cards e Segments por Equipe para identificar conteúdo relevante para eles.

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

Como Michelle tem a permissão de nível de espaço de trabalho "Acessar Campaigns, Canvas, cartões, Content Blocks, Feature Flags, Segments, Biblioteca de mídia e Central de Preferências", ela pode visualizar e atribuir outros filtros de Equipe à campanha que criar.

![Menu suspenso de tag de Equipe da campanha com múltiplas tags de Equipe]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Assim como no primeiro cenário, Michelle deve adicionar a tag de Equipe Development à campanha antes de poder lançá-la.

{% endtab %}
{% endtabs %}

## Testar com Equipes {#test-with-teams}

Um possível caso de uso para Equipes é criar um sistema de aprovação baseado em Equipes para testar e lançar conteúdo em um ambiente de produção.

Para isso, crie uma Equipe "Development" que só tenha acesso a usuários teste. Você pode limitar uma Equipe a acessar apenas usuários teste se seus usuários teste forem identificáveis por um atributo personalizado. Em seguida, adicione o atributo personalizado como definição ao criar ou editar a Equipe (consulte a seção anterior [Criar Equipes](#creating-Teams)). Seus aprovadores devem ter acesso a todos os usuários.

O processo geral seria o seguinte:

1. A Equipe Development cria uma campanha e adiciona a tag de Equipe "Development".
2. A Equipe Development lança a campanha para usuários teste.
3. A Equipe de Aprovação valida o design local da campanha, promove e lança. Para lançar, a Equipe de Aprovação altera a tag de Equipe de "Development" para "[All Teams]" e relança a campanha.

Para alterações em campanhas ativas:

1. A Equipe Development clona a campanha em execução, adiciona a tag de Equipe "Development" e salva.
2. A Equipe Development faz as edições e compartilha com a Equipe de Aprovação.
3. A Equipe de Aprovação remove a tag de Equipe "Development", pausa a campanha anterior e lança a nova campanha.

## Arquivar uma Equipe existente {#archive-an-existing-team}

Você pode arquivar Equipes na página **Equipes internas**.

Selecione uma ou mais Equipes para arquivar. Se a Equipe não estiver associada a nenhum objeto na Braze, ela será arquivada imediatamente. Se a Equipe estiver associada a um objeto, será apresentada uma opção para remover a Equipe após o processo de arquivamento ou substituir a Equipe.

![Arquivando uma Equipe que está associada a um objeto na Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Administradores da Braze podem desarquivar uma Equipe selecionando a Equipe arquivada e selecionando **Desarquivar**.