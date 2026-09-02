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

> As mensagens no app entregam conteúdo dentro do seu app ou website sem interromper os usuários com uma notificação por push. Mensagens no app personalizadas aprimoram a experiência do usuário e ajudam seu público a extrair mais valor do seu produto por meio de layouts, personalização e ferramentas de direcionamento. Este hub abrange tipos de mensagem, o editor de arrastar e soltar, pré-requisitos e casos de uso comuns, como integração e promoções. Integre o [SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) antes de criar sua primeira mensagem no app e, em seguida, escolha um layout padrão ou personalizado para sua Campaign.

## Pré-requisitos {#prerequisites}

Antes de enviar mensagens no app, você precisa integrar o [SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) no seu app ou website. Nenhuma configuração adicional é necessária.

Para versões mínimas do SDK or kit de desenvolvimento de software e requisitos específicos de recursos, consulte:
- [Editor de arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [Tipos de mensagem]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types)

## Casos de uso {#use-cases}

Com o rico nível de conteúdo oferecido pelas mensagens no app, você pode aproveitar esse canal para diversos casos de uso:

| Caso de uso | Explicação |
| --- | --- |
| Preparação para push | Execute uma campanha de [preparação para push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) usando uma mensagem no app avançada para mostrar aos seus clientes os benefícios de aceitar notificações por push do seu app ou site, e apresente a eles uma solicitação para conceder permissão de push. |
| Vendas e promoções | Use mensagens no app modais para receber os clientes com mídia visualmente atraente contendo códigos de promoção estáticos ou ofertas. Incentive-os a realizar compras ou conversões que, de outra forma, não fariam. |
| Incentivar a adoção de recursos | Incentive os clientes a usar outras partes do seu app ou aproveitar um serviço. |
| Campaigns altamente personalizadas | Posicione mensagens no app como a primeira coisa que seus clientes veem ao entrar no app ou site. Adicione alguns recursos de personalização da Braze, como [Conteúdo Conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), para motivar os usuários a agir e, assim, tornar sua comunicação mais eficaz. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

Outros casos de uso a considerar incluem:

- Novos recursos do app
- Gerenciamento do app
- Avaliações
- Upgrades ou atualizações do app
- Sorteios e concursos

## Tipos de mensagem padrão {#standard-message-types}

As guias a seguir mostram como seus usuários veem cada um dos tipos de mensagem no app padrão: slideup, modal e tela inteira.

{% tabs %}
{% tab Slideup %}

As mensagens slideup geralmente aparecem na parte superior ou inferior da tela do app (você pode definir isso ao criar sua mensagem). Elas são ótimas para alertar seus usuários sobre novos termos de serviço, cookies e outros snippets de informação.

![Mensagem no app do tipo slideup aparecendo na parte inferior da tela do app. O slideup inclui um ícone de imagem e uma breve mensagem.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

As mensagens modais aparecem no centro da tela do dispositivo com uma sobreposição que ajuda a destacá-las do app em segundo plano. São perfeitas para sugerir de forma direta que o usuário aproveite uma promoção ou sorteio.

![Mensagem no app do tipo modal aparecendo no centro de um app e website como uma caixa de diálogo. O modal inclui uma imagem, cabeçalho, corpo da mensagem e dois botões.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Tela inteira %}

As mensagens em tela inteira são exatamente o que você espera: elas ocupam toda a tela do dispositivo! Esse tipo de mensagem é ideal quando você realmente precisa da atenção do usuário, como para atualizações obrigatórias do app.

![Mensagem no app em tela inteira ocupando toda a tela do app. A mensagem em tela inteira inclui uma imagem grande, cabeçalho, corpo da mensagem e dois botões.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

Além desses modelos de mensagem padrão, você também pode personalizar ainda mais seu envio de mensagens usando mensagens no app em HTML personalizado, modais web com CSS ou formulários de captura de e-mail na web. Para saber mais, consulte [Personalizar]({{site.baseurl}}/user_guide/channels/in_app_messages/customize).

Para saber como a entrega por modelo no momento da exibição afeta o registro de **interrupção**, consulte [FAQ sobre mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

## Próximas etapas {#next-steps}

- [Criar uma mensagem no app com o editor de arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [Criar uma mensagem no app com o editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}