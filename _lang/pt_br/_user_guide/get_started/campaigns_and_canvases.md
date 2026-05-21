---
nav_title: Campanhas e Canvas
article_title: "Primeiros passos: Campanhas e Canvas"
page_order: 3
page_type: reference
description: "Este artigo fornece uma visão geral das diferentes maneiras pelas quais você pode enviar mensagens com a Braze."

---

# Primeiros passos: Campanhas e Canvas {#get-started-campaigns-and-canvases}

> Este artigo fornece uma visão geral das diferentes maneiras pelas quais você pode enviar mensagens com a Braze. Na Braze, você pode enviar mensagens por meio de uma [campanha](#campaigns) ou de um [Canvas](#canvas).

- Para enviar uma única mensagem direcionada a um grupo de usuários, escolha uma campanha. Uma campanha é uma etapa de mensagem única para se conectar com seus usuários em vários canais de envio de mensagens.
- Para enviar uma série de mensagens contínuas em uma jornada abrangente do cliente, escolha o Canvas, nossa ferramenta de orquestração de jornadas. Embora as campanhas sejam boas para o envio de mensagens simples e direcionadas, é no Canvas que você leva o relacionamento com os clientes para o próximo nível.

## Campanhas {#campaigns}

Embora as campanhas possam ser criadas de forma exclusiva dependendo do canal, há quatro tipos principais de campanhas na Braze que você deve conhecer:

| Tipo de campanha | Descrição |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Regular | Esse é o tipo mais comum de campanha. Você pode direcionar um ou mais canais dependendo dos seus objetivos de envio de mensagens, e projetar, personalizar e testar seu conteúdo diretamente na Braze com nossos editores visuais. Saiba como [criar uma campanha]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/). |
| Testes A/B | Para campanhas direcionadas a um único canal, você pode enviar mais de uma versão da mesma campanha e ver qual delas tem o melhor desempenho. Você pode testar o texto, a personalização e muito mais em até oito versões diferentes com uma [campanha multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing/). |
| API | As [campanhas da API]({{site.baseurl}}/api/api_campaigns/) permitem que você envie mensagens oportunas o mais rápido possível. Diferentemente de outros tipos de campanha, você não especifica a mensagem, os destinatários ou a programação no dashboard da Braze. Em vez disso, passe esses identificadores em suas chamadas de API. Normalmente, são usadas para envio de mensagens transacionais em tempo real ou notícias de última hora. |
| E-mail de transação | Os [E-mails de transação]({{site.baseurl}}/user_guide/channels/email/) da Braze são criados especificamente para o envio de mensagens de e-mail automatizadas e não promocionais, facilitando uma transação acordada entre você e seus clientes. Eles enviam notificações críticas de negócios para um único usuário, onde a velocidade é de extrema importância. *Disponível para pacotes selecionados.* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns" }

{% alert note %}
As campanhas regulares e de testes A/B podem ser programadas (como informar uma lista de usuários sobre um evento futuro) ou automatizadas para envio em resposta a uma ação do usuário (como enviar um e-mail quando alguém se inscreve no seu boletim informativo). Saiba mais sobre o [agendamento de campanhas]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).
{% endalert %}

Independentemente do tipo de campanha que você criar, suas campanhas podem ouvir as necessidades do usuário e fornecer uma resposta atenciosa e personalizada. Depois de enviar sua campanha, use nossas [ferramentas integradas de análise de dados]({{site.baseurl}}/user_guide/analytics/reports/) para ver o desempenho e quantos usuários converteram com base nos seus [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/).

Confira estes recursos adicionais para saber mais sobre campanhas na Braze:

- Braze Learning: [Configuração de campanhas](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Criar uma campanha]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/)
- [Ideias e estratégias]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/)

## Canvas {#canvas}

Em vez de enviar mensagens esporádicas em várias campanhas, o Canvas cria uma conversa fluida e contínua com os usuários. Isso ocorre porque a jornada de um usuário por um Canvas pode se dividir em diferentes jornadas dependendo de suas ações (ou inação) com sua marca, permitindo que você avance automaticamente os usuários por um fluxo específico em tempo real.

![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

Dessa forma, o Canvas é ótimo para lançar uma rede e capturar os usuários que saíram da jornada de conversão, colocando-os nas iniciativas de alcance mais eficazes.

Ao criar um Canvas, você segue muitas das mesmas etapas da configuração de uma campanha: especificação de um público geral, condições de entrada e configurações de envio. Seu Canvas começa quando alguém corresponde à sua condição de disparo. Em seguida, essa pessoa se move por uma jornada no Canvas até atender às suas condições de saída.

Seu Canvas pode ter qualquer combinação de [mensagens]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/), [postergações]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/), [experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) e muito mais. Você pode enviar em qualquer canal de envio de mensagens compatível e até mesmo [integrar-se a plataformas sociais e de anúncios]({{site.baseurl}}/partners/canvas_audience_sync/overview/), como Facebook, Google ou TikTok.

Confira estes recursos adicionais para saber mais sobre o Canvas:

- Braze Learning: [Orquestração de jornadas com o Canvas Flow](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Criar um Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)
- [Modelos de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/canvas_outlines/)

## Canais de envio de mensagens {#messaging-channels}

Os canais de envio de mensagens são os vários canais de comunicação por meio dos quais você pode interagir com seus clientes e enviar mensagens direcionadas.

![]({% image_buster /assets/img/getting_started/channels.png %})

A tabela a seguir descreve nossos canais compatíveis.

| Canal | Descrição |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [E-mail]({{site.baseurl}}/user_guide/channels/email/) | Envie e-mails personalizados para as caixas de entrada dos seus usuários. |
| [Push móvel]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/) | Envie mensagens diretamente para os dispositivos móveis dos usuários como notificações. |
| [Push para a web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/) | Envie notificações para os navegadores dos usuários, mesmo quando eles não estiverem ativamente no seu site. |
| [Mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/) | Exiba mensagens no app móvel enquanto os usuários estiverem usando-o ativamente. |
| [SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/)* | Envie mensagens de texto para os celulares dos usuários. |
| [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/)* | Envie mensagens por meio da popular plataforma de envio de mensagens, o WhatsApp, para alcançar e interagir com seus usuários. |
| [Banners]({{site.baseurl}}/user_guide/channels/banners/)* | Incorpore mensagens diretamente no seu app ou site. |
| [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/)* | Forneça uma caixa de entrada no seu app ou site onde os usuários possam receber e interagir com mensagens, ou exiba mensagens em um carrossel, como um banner e muito mais. |
| [TV conectada]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/) | Interaja com usuários em plataformas de televisão conectadas. |
| [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks/) | Ative a comunicação e a integração em tempo real com sistemas externos por meio de retornos de chamada HTTP personalizados. |
| [LINE]({{site.baseurl}}/user_guide/channels/line/) | Interaja com os usuários no LINE, o app de mensagens mais popular no Japão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Messaging channels" }

<sup>*Disponível como recurso complementar.</sup>

{% alert tip %}
Para mensagens curtas e urgentes que podem ser comunicadas pela maioria dos canais (e-mail, SMS, push), aproveite o filtro [Intelligent Channel]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/) para enviar automaticamente a mensagem pelo melhor canal para cada usuário.
{% endalert %}