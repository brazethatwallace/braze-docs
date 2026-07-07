---
nav_title: Braze Pilot
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze Pilot"
guide_top_text: "O Braze Pilot é um app móvel projetado para se conectar perfeitamente ao seu dashboard da Braze. Com ele, você pode lançar Campaigns e Canvas para o app, dando vida às mensagens da Braze no seu próprio telefone. O Braze Pilot inclui uma biblioteca de simulações de apps para marcas fictícias que representam diferentes setores, permitindo que você veja como suas mensagens podem parecer do ponto de vista dos seus clientes."
description: "Confira as diferentes maneiras de usar a Braze para enviar mensagens do dashboard da Braze para o seu telefone."

guide_featured_title: "Artigos da seção"
guide_featured_list:
  - name: Comece com o Braze Pilot
    link: /docs/user_guide/get_started/braze_pilot/getting_started
    image: /assets/img/braze_icons/brush-02.svg
  - name: Dicionário de dados
    link: /docs/user_guide/get_started/braze_pilot/data_dictionary
    image: /assets/img/braze_icons/book-closed.svg
  - name: Deep links de navegação
    link: /docs/user_guide/get_started/braze_pilot/deep_links
    image: /assets/img/braze_icons/link-03.svg

---

## Simulações de apps do Pilot {#pilot-app-simulations}

O núcleo do Braze Pilot é sua biblioteca de simulações de apps. Cada app é uma simulação realista de uma marca fictícia de um setor específico, instrumentada para registrar uma rica variedade de eventos e atributos que criam oportunidades infinitas para impulsionar casos de uso comuns da Braze.

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppington é um app de fitness com treinos, metas de exercícios e um serviço premium Steppington+. Ele oferece vários locais para demonstrar [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards), uma seção que pode ser revelada com [Feature Flags]({{site.baseurl}}/developer_guide/feature_flags) e uma robusta biblioteca de registro de eventos personalizados que possibilita ilustrar muitas jornadas de clientes para esse setor.

![A página inicial do Steppington com ícones para treinamento de maratona, yoga, ciclismo e musculação.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### PantsLabyrinth

PantsLabyrinth é um app de eCommerce que vende (você adivinhou) calças! O app PantsLabyrinth inclui uma experiência completa de checkout de carrinho de compras, um recurso opcional de lista de desejos que pode ser ativado com uma Feature Flag e muitas oportunidades para piadas sutis com amigos do Reino Unido.

![Uma página de produto do PantsLabyrinth com opções para adicionar jeans ao carrinho.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon

MovieCanon é um serviço de streaming perfeitamente projetado para ilustrar casos de uso comuns da Braze relacionados ao engajamento de conteúdo.

![O app MovieCanon com diferentes thrillers para assistir.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Como o Pilot se conecta ao seu dashboard da Braze {#how-pilot-connects-with-your-braze-dashboard}

O SDK da Braze é um pacote de código que coleta dados dos seus usuários depois de integrado ao seu app ou site. Quando você conecta o Pilot ao seu dashboard, você inicializa essa conexão entre o app Pilot no seu telefone e o SDK da Braze, além de estabelecer uma conexão única com sua instância da Braze ao fornecer ao Pilot o identificador da sua chave de API do dashboard.

![A primeira etapa para configurar o Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Depois que o Pilot se conecta ao seu dashboard da Braze, o SDK da Braze funciona no app exatamente como funcionará quando você integrar o SDK ao seu próprio app ou site. Isso significa que a Braze irá:

- Armazenar dados sobre a atividade do usuário no Pilot, incluindo dados personalizados específicos das marcas fictícias no app.
- Coletar automaticamente dados de sessão, informações do dispositivo e tokens por push.
- Alimentar notificações por push, mensagens no app e canais de envio de mensagens de Content Cards que exigem integração de SDK para funcionar.

Para saber mais sobre o SDK da Braze, confira [Integração]({{site.baseurl}}/user_guide/get_started/integrations).

![A pilha de engajamento do cliente da Braze, que inclui integrações, APIs, SDKs para ingestão de dados, classificação, orquestração, personalização e ação com canais de envio de mensagens para um ciclo de feedback interativo com seus clientes.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Perfis de usuário na Braze {#user-profiles-in-braze}

Cada dado enviado à Braze é armazenado em um perfil de usuário dedicado a um usuário específico do seu app ou site. Depois que você conecta o Pilot ao seu dashboard da Braze, a Braze começa a registrar dados sobre você como usuário do Pilot. Existem dois tipos de usuários que podem ser criados para você por meio dessa conexão: anônimo e identificado.

### Anônimo {#anonymous}

Esse status de conexão representa a experiência de um visitante do seu app ou site que ainda não fez login. Se você inicializar o Pilot como um usuário anônimo, a Braze cria um [perfil de usuário anônimo]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) para você e registra dados sobre sua atividade nele. Usuários anônimos ainda podem ser segmentados em Campaigns, mas você não poderá consultar o perfil de usuário deles diretamente no seu dashboard da Braze.

### Identificado {#identified}

Esse status de conexão significa que a Braze reconhece seu perfil de usuário por meio de um identificador único atribuído a você, conhecido como identificador externo. Você pode pesquisar esse identificador externo na página **Pesquisa de usuários** do seu dashboard para localizar seu perfil de usuário, que armazena todos os atributos e eventos do usuário registrados a partir do Pilot com base na sua atividade no app. No dashboard da Braze, acesse **Público** > **Pesquisa de usuários**, insira seu **ID externo** do Pilot e abra o perfil para inspecionar atributos e eventos.

### Tipo de conexão {#connection-type}

Para verificar que tipo de conexão você tem, confira o indicador de status de conexão no canto superior direito do app Pilot.

{% tabs local %}
{% tab Anonymous user  %}

**Anônimo** indica que você está registrando dados como um usuário anônimo. A área de status mostra o rótulo **Anônimo** (por exemplo, um ícone de máscara ou de navegação anônima).

{% endtab %}
{% tab Identified user %}

Se você estiver registrando dados como um usuário identificado, a área de status mostra **Usuário identificado** e seu ID externo.

{% endtab %}
{% tab Not connected %}

**Não conectado** indica que você ainda não inicializou a conexão do SDK da Braze com o Pilot. A área de status indica que o Pilot ainda não está conectado ao seu espaço de trabalho da Braze.

{% endtab %}
{% endtabs %}

## Campaigns e Canvas {#campaigns-and-canvases}

Campaigns e Canvas são a forma como você envia mensagens aos seus usuários.

- Campaigns são ideais para mensagens individuais enviadas a um segmento específico de público em vários canais.
- Canvas são fluxos de trabalho avançados de Campaigns que permitem automatizar e orquestrar jornadas personalizadas de clientes em múltiplos canais. Em um Canvas, você pode configurar lógica de ramificação, postergações, pontos de decisão e eventos de conversão para guiar os clientes por uma série de interações. Canvas ajudam a garantir uma comunicação consistente e fluida em diferentes pontos de contato, aumentando as chances de engajamento e conversão do cliente.

## Canais de envio de mensagens suportados {#supported-messaging-channels}

O Braze Pilot atualmente suporta [mensagens no app]({{site.baseurl}}/in-app_messages), que aparecem no seu app, entregando mensagens oportunas enquanto o usuário está ativamente engajado.

![Uma mensagem no app no MovieCanon "Curtindo o MovieCanon? Indique seus amigos!" com uma opção para inserir seu endereço de e-mail para enviar uma indicação.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}