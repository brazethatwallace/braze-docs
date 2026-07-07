---
nav_title: O dashboard
article_title: O dashboard da Braze
page_order: 1
page_type: reference
description: "O dashboard da Braze é seu espaço de trabalho central para criar, gerenciar e analisar o engajamento com clientes. Ele reúne ferramentas de envio de mensagens, insights de público, segmentação e dados de desempenho em tempo real em um só lugar."

---

# O dashboard da Braze {#the-braze-dashboard}

> O dashboard da Braze é seu espaço de trabalho central para criar, gerenciar e analisar o engajamento com clientes. Acesse em [dashboard.braze.com](https://dashboard.braze.com/) ou [dashboard.braze.eu](https://dashboard.braze.eu/).

Use o dashboard da Braze para planejar campanhas, lançar e gerenciar mensagens, explorar insights de público, ajustar a segmentação e revisar métricas de desempenho e engajamento em tempo real a partir de uma única interface.

## Visão geral do dashboard {#dashboard-overview}

Ao fazer login, o dashboard oferece uma visão centralizada das suas ferramentas de engajamento e dados:

- **Página inicial:** Mostra seu [conteúdo editado recentemente](#pick-up-where-you-left-off) e métricas de desempenho principais em um relance
- **Navegação lateral:** Organiza as ferramentas por função (envio de mensagens, público, análise de dados, configurações)
- **Cabeçalho global:** Oferece acesso rápido a pesquisa, suporte, configurações de idioma, notificações e sua conta

Sua experiência no dashboard é organizada por [espaços de trabalho]({{site.baseurl}}/user_guide/get_started/workspaces), que ajudam a gerenciar conteúdo para diferentes marcas, regiões ou equipes. Você pode [alternar entre espaços de trabalho](#workspace-switcher) a qualquer momento pela navegação lateral.

## Acessar seu dashboard {#access-your-dashboard}

Para começar, [faça login na sua conta da Braze]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account). Seu acesso às páginas do dashboard e a permissão para realizar determinadas ações são baseados nas suas [permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) atribuídas. Se precisar de ajuda com suas permissões, entre em contato com os administradores da Braze.

## Navegar na Braze {#navigate-braze}

A navegação da Braze foi projetada para ajudar você a acessar recursos e conteúdo de forma eficiente em diferentes dispositivos. Existem dois níveis de navegação no dashboard da Braze: cabeçalho global e navegação lateral.

O cabeçalho global está quase sempre visível na parte superior da tela. Ele oferece acesso rápido a ferramentas e configurações essenciais, incluindo:

- [Pesquisa](#search-your-dashboard)
- Links de suporte e comunidade
- [Idioma do dashboard]({{site.baseurl}}/user_guide/administer/personal/language_settings)
- Notificações
- Configurações da conta
- [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator)

### Usar a navegação lateral {#use-the-side-navigation}

O menu vertical à esquerda organiza as ferramentas da Braze por função e mantém os itens mais usados ao seu alcance. Selecione um item do menu principal para revelar suas opções em um layout vertical empilhado.

![Seletor de espaço de trabalho no dashboard da Braze]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### Seletor de espaço de trabalho {#workspace-switcher}

Localizado no topo da navegação lateral, o seletor de espaço de trabalho permite alternar entre diferentes espaços de trabalho na sua instância da Braze. O espaço de trabalho ativo fica destacado.

[Espaços de trabalho]({{site.baseurl}}/user_guide/get_started/workspaces) ajudam a organizar conteúdo por marca, região, linha de produto ou equipe. Cada espaço de trabalho inclui seus próprios dados, Campaigns e configurações. Seu acesso pode variar entre espaços de trabalho. Por exemplo, você pode ter acesso de edição em um espaço de trabalho e acesso somente leitura em outro.

Para alternar entre espaços de trabalho, selecione o menu suspenso de espaço de trabalho no topo da navegação lateral e escolha o espaço de trabalho que deseja acessar. Você também pode [adicionar espaços de trabalho favoritos](#favorite-workspaces) para acesso mais rápido aos que usa com mais frequência.

#### Minimizar a navegação lateral {#minimize-the-side-navigation}

Para reduzir a poluição visual, especialmente durante tarefas como projetar um Canvas, você pode minimizar o painel de navegação lateral. Pressione **Minimizar menu** para recolhê-lo. Mesmo minimizado, passe o mouse sobre qualquer ícone para ver dicas com os nomes dos itens do menu. Isso ajuda você a alternar rapidamente entre ferramentas mantendo seu espaço de trabalho limpo.

![Ícones de minimizar e maximizar menu]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### Navegação responsiva {#responsive-navigation}

A navegação se adapta perfeitamente a diferentes tamanhos de tela. Em telas menores, a navegação lateral é recolhida automaticamente. Pressione <i class="fa-solid fa-bars" aria-label="Abrir menu de navegação"></i> para abrir o menu quando necessário.

![Em telas menores, a navegação lateral é recolhida automaticamente. Tocar no ícone de menu abre as opções de navegação.]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## Pesquisar no dashboard {#search-your-dashboard}

A barra de pesquisa global, localizada no cabeçalho, é a maneira mais rápida de encontrar conteúdo no dashboard da Braze. Selecione para abrir a interface de pesquisa e ir diretamente ao que você precisa.

![Pesquisa global aberta sem termos de pesquisa inseridos, mostrando páginas abertas recentemente.]({% image_buster /assets/img/navigation/search_recently_opened.png %})

Seu conteúdo aberto recentemente aparece abaixo da barra de pesquisa. Isso inclui qualquer Campaign, Canvas, modelo ou página com a qual você interagiu recentemente, facilitando o retorno ao seu trabalho.

### O que você pode pesquisar? {#what-can-you-search-for}

Você pode pesquisar os seguintes itens e ações:

- Nomes de Campaigns
- Nomes de Canvas
- Content Blocks
- Nomes de Segments
- Nomes de modelos de e-mail
- Páginas na Braze (incluindo sinônimos)

{% alert tip %}
Para pesquisar texto exato, coloque o termo de pesquisa entre aspas (""). Por exemplo, pesquisar ["all users"] retornará todos os itens que contêm a frase exata "all users" no nome.
{% endalert %}

### Tags de tipo de conteúdo e status {#content-type-and-status-tags}

Cada resultado é identificado com uma tag indicando seu tipo de conteúdo — como Campaign, Canvas ou Segment — e seu status (ativo, arquivado, parado).

### Filtrar por conteúdo ativo e rascunho {#filter-for-active-and-draft-content}

Por padrão, a pesquisa inclui itens ativos, rascunhos e arquivados. Use o botão **Show active and draft only** para refinar seus resultados.

![O botão "Show active and draft only".]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### Atalhos de teclado {#keyboard-shortcuts}

Você pode navegar pelos resultados da pesquisa usando o teclado.

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| Ação                              | Atalho de teclado                                                             |
| --------------------------------- | ----------------------------------------------------------------------------- |
| Abrir o menu de pesquisa          | {::nomarkdown} <ul> <li> Mac: <kbd>⌘</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> <li>Windows: <kbd>Ctrl</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> </ul> {:/}  |
| Mover entre resultados da pesquisa | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| Selecionar um resultado da pesquisa | <kbd>Enter</kbd>    |
| Fechar o menu de pesquisa         | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Atalhos de teclado" }

## Recursos de produtividade {#productivity-features}

O dashboard da Braze inclui vários recursos para ajudar você a trabalhar de forma mais eficiente e acessar rapidamente as ferramentas e o conteúdo que mais usa.

### BrazeAI Operator

BrazeAI Operator™ é um assistente com tecnologia de IA integrado ao dashboard. Use-o para obter respostas, acompanhar configurações, solucionar problemas e gerar ideias. Abra-o em **BrazeAI Operator™** no cabeçalho global ao lado do seu perfil. Para saber mais, consulte [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator).

### Continue de onde parou {#pick-up-where-you-left-off}

Na página **Inicial**, o dashboard exibe suas Campaigns, Canvas e Segments editados ou criados recentemente. Isso facilita o retorno a trabalhos em andamento sem precisar pesquisar. Cada item inclui tags mostrando o tipo de conteúdo e o status (como rascunho, ativo ou parado).

![Um rascunho de Canvas, um Segment ativo e um rascunho de Campaign na seção "Continue de onde parou".]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

Para saber mais, consulte [Dashboard inicial]({{site.baseurl}}/user_guide/analytics/dashboards/home#pick-up-where-you-left-off).

### Espaços de trabalho favoritos {#favorite-workspaces}

Se você trabalha em vários espaços de trabalho, pode marcar os mais usados como favoritos. Os espaços de trabalho favoritos aparecem no topo do seletor de espaço de trabalho para acesso mais rápido.

Para adicionar espaços de trabalho favoritos:

1. [Acesse as configurações do seu perfil](#access-your-profile-settings).
2. Na seção **Perfil da conta**, localize o campo **Espaços de trabalho favoritos**.
3. Selecione os espaços de trabalho que deseja favoritar.

### Acessar as configurações do seu perfil {#access-your-profile-settings}

Para gerenciar as configurações da sua conta, preferências de notificação e informações pessoais:

1. Selecione o ícone do seu perfil no cabeçalho global.
2. Selecione **Gerenciar sua conta** para acessar a página do seu perfil.

Na página do seu perfil, você pode atualizar suas configurações de e-mail, configurar a autenticação de dois fatores, visualizar suas chaves de API e gerenciar outros detalhes da conta.

## Acessibilidade no dashboard {#accessibility-in-the-dashboard}

O dashboard da Braze usa cores da marca que atendem aos padrões WCAG AA de contraste de cores. Isso proporciona uma experiência inclusiva para todos os usuários e está alinhado com as melhores práticas de acessibilidade.

## Compartilhar feedback {#sharing-feedback}

Quer nos dizer o que pensa? Você pode compartilhar feedback sobre navegação, acessibilidade, usabilidade, design visual e muito mais. Abra o menu **Suporte** no cabeçalho global e selecione **Compartilhar feedback**. Revisamos todos os feedbacks para ajudar a melhorar sua experiência com a Braze.

## Recursos relacionados {#related-resources}

### Tarefas administrativas {#administrative-tasks}

- [Criar e gerenciar espaços de trabalho]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces)
- [Gerenciar usuários da Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users)
- [Permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)
- [Equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams)

### Tarefas principais e próximos passos {#key-tasks-and-next-steps}

- **Criar Campaigns**: [Criar uma Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign)
- **Criar jornadas**: [Criar um Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)
- **Definir públicos**: [Criar um Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)
- **Revisar desempenho**: [Visão geral de análise de dados]({{site.baseurl}}/user_guide/analytics/dashboards/home)
- **Definir configurações**: [Configurações do app]({{site.baseurl}}/user_guide/administer/global/workspace_settings)