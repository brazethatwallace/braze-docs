---
nav_title: "Mensagens no app"
article_title: "Mensagens no app"
page_order: 5
page_type: landing
alias: /in-app_messages/
description: "Engaje usuários com mensagens no app personalizadas que aprimoram a experiência do usuário usando uma variedade de layouts e ferramentas de personalização na Braze."
channel:
  - in-app messages
search_rank: 5
---

# Mensagens no app {#in-app-messages}

> As mensagens no app ajudam você a entregar conteúdo aos seus usuários sem interromper o dia deles com uma notificação por push. Mensagens no app personalizadas e sob medida aprimoram a experiência do usuário e ajudam seu público a extrair o máximo valor do seu app. Com uma variedade de layouts e ferramentas de personalização para escolher, as mensagens no app engajam seus usuários mais do que nunca.

## Pré-requisitos {#prerequisites}

Antes de enviar mensagens no app, você precisa integrar o [SDK da Braze]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) ao seu app ou site. Nenhuma configuração adicional é necessária.

Para versões mínimas do SDK e requisitos específicos de funcionalidades, consulte:
- [Editor de arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
- [Tipos de mensagem]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/)

## Casos de uso {#use-cases}

Com o rico nível de conteúdo oferecido pelas mensagens no app, você pode aproveitar esse canal para uma variedade de casos de uso:

| Caso de uso | Explicação |
| --- | --- |
| Preparação para push | Execute uma Campaign de [preparação para push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/) usando uma mensagem no app rica para mostrar aos seus clientes o benefício de aceitar notificações por push do seu app ou site, e apresente a eles uma solicitação para conceder permissão de push.
| Vendas e promoções | Use mensagens no app modais para receber os clientes com mídia visualmente atraente contendo códigos de promoção estáticos ou ofertas. Incentive-os a fazer compras ou conversões quando, de outra forma, não fariam. |
| Incentivar a adoção de funcionalidades | Incentive os clientes a usar outras partes do seu app ou aproveitar um serviço. |
| Campaigns altamente personalizadas | Posicione mensagens no app como a primeira coisa que seus clientes veem ao entrar no seu app ou site. Adicione alguns recursos de personalização da Braze, como [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), para motivar os usuários a agir e, assim, tornar sua comunicação mais eficaz.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

Outros casos de uso a considerar incluem:

- Novas funcionalidades do app
- Gerenciamento do app
- Avaliações
- Atualizações do app
- Sorteios e promoções

## Tipos de mensagem padrão {#standard-message-types}

As guias a seguir mostram como seus usuários veem cada um dos nossos tipos padrão de mensagem no app — slideup, modal e mensagens no app em tela cheia.

{% tabs %}
{% tab Slideup %}

As mensagens slideup geralmente aparecem na parte superior e inferior da tela do app (você pode definir isso ao criar sua mensagem). Elas são ótimas para alertar seus usuários sobre novos termos de serviço, cookies e outros trechos de informação.

![Mensagem no app slideup aparecendo na parte inferior da tela do app. O slideup inclui um ícone de imagem e uma breve mensagem.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

As modais aparecem no centro da tela do dispositivo com uma sobreposição de tela que ajuda a destacá-las do seu app em segundo plano. São perfeitas para sugerir de forma evidente que seu usuário aproveite uma promoção ou sorteio.

![Mensagem no app modal aparecendo no centro de um app e site como uma caixa de diálogo. A modal inclui uma imagem, cabeçalho, corpo da mensagem e dois botões.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Tela cheia %}

As mensagens em tela cheia são exatamente o que você espera — elas ocupam toda a tela do dispositivo! Esse tipo de mensagem é ótimo quando você realmente precisa da atenção do seu usuário, como para atualizações obrigatórias do app.

![Mensagem no app em tela cheia ocupando a tela de um app. A mensagem em tela cheia inclui uma imagem grande, cabeçalho, corpo da mensagem e dois botões.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

Além desses modelos de mensagem padrão, você também pode personalizar ainda mais suas mensagens usando mensagens no app com HTML personalizado, modais web com CSS ou formulários de captura de e-mail web. Para saber mais, consulte [Personalizar]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/).

Para saber como a entrega com modelo no momento da exibição afeta o registro de **abort**, consulte [FAQ sobre mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/faq/).

## Próximos passos {#next-steps}

- [Crie uma mensagem no app com o editor de arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
- [Crie uma mensagem no app com o editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}