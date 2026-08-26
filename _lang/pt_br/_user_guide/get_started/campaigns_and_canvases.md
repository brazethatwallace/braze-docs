---
nav_title: Campaigns e Canvas
article_title: "Primeiros passos: Campaigns e Canvas"
page_order: 3
page_type: reference
description: "Este artigo fornece uma visão geral das diferentes maneiras pelas quais você pode enviar mensagens com a Braze."
---

# Primeiros passos: Campaigns e Canvas {#get-started-campaigns-and-canvases}

> Este artigo fornece uma visão geral das diferentes maneiras pelas quais você pode enviar mensagens com a Braze. Na Braze, você pode enviar mensagens por meio de uma [Campaign](#campaigns) ou de um [Canvas](#canvas).

- Para enviar uma única mensagem direcionada a um grupo de usuários, escolha uma Campaign. Uma Campaign é uma etapa de mensagem única para se conectar com seus usuários em vários canais de envio de mensagens.
- Para enviar uma série de mensagens contínuas em uma jornada abrangente do cliente, escolha o Canvas, nossa ferramenta de orquestração de jornadas. Embora as Campaigns sejam boas para o envio de mensagens simples e direcionadas, é no Canvas que você leva o relacionamento com os clientes para o próximo nível.

## Campaigns {#campaigns}

Embora as Campaigns possam ser criadas de forma única dependendo do canal, existem quatro tipos principais de Campaigns na Braze que você deve conhecer:

| Tipo de Campaign | Descrição |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Regular | Este é o tipo mais comum de Campaign. Você pode direcionar um ou mais canais dependendo dos seus objetivos de envio de mensagens e projetar, personalizar e testar seu conteúdo diretamente na Braze com nossos editores visuais. Saiba como [criar uma Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign). |
| Testes A/B | Para Campaigns direcionadas a um único canal, você pode enviar mais de uma versão da mesma Campaign e ver qual delas se sai melhor. Você pode testar o texto, a personalização e muito mais para até oito versões diferentes com uma [Campaign multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing). |
| API | [Campaigns de API]({{site.baseurl}}/api/api_campaigns) permitem que você envie mensagens oportunas o mais rápido possível. Diferentemente de outros tipos de Campaign, você não especifica a mensagem, os destinatários ou o cronograma no dashboard da Braze. Em vez disso, você passa esses identificadores nas suas chamadas de API. Elas são normalmente usadas para envio de mensagens de transação em tempo real ou notícias urgentes. |
| E-mails de transação | Os [e-mails de transação]({{site.baseurl}}/user_guide/channels/email) da Braze são desenvolvidos especificamente para enviar mensagens de e-mail automatizadas e não promocionais para facilitar uma transação acordada entre você e seus clientes. Eles enviam notificações críticas para o negócio a um único usuário, onde a velocidade é de extrema importância. *Disponível para pacotes selecionados.* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns" }

{% alert note %}
Campaigns regulares e de testes A/B podem ser agendadas (como informar uma lista de usuários sobre um evento futuro) ou automatizadas para envio em resposta a uma ação do usuário (como enviar um e-mail quando alguém se inscreve na sua newsletter). Saiba mais sobre [agendar Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).
{% endalert %}

Independentemente do tipo de Campaign que você cria, suas Campaigns podem ouvir as necessidades dos seus usuários e entregar uma resposta atenciosa e personalizada. Depois de enviar sua Campaign, use nossas [ferramentas de análise de dados integradas]({{site.baseurl}}/user_guide/analytics/reports) para ver o desempenho e quantos usuários converteram com base nos seus [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).

Confira estes recursos adicionais para saber mais sobre Campaigns na Braze:

- Braze Learning: [Configuração de Campaign](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Criar uma Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign)
- [Ideias e estratégias]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies)

## Canvas {#canvas}

Em vez de enviar mensagens esporádicas em várias Campaigns, o Canvas cria uma conversa contínua e fluida com os usuários. Isso acontece porque a jornada de um usuário pelo Canvas pode se dividir em diferentes caminhos, dependendo das ações (ou inações) dele com a sua marca, permitindo que você avance automaticamente os usuários por um fluxo específico em tempo real.

![Diagrama de fluxo do processo descrito.]({% image_buster /assets/img/getting_started/canvas_flow.png %})

Dessa forma, o Canvas é ótimo para lançar uma rede e capturar os usuários que saíram do caminho da conversão, colocando-os nas iniciativas de alcance mais eficazes.

Ao criar um Canvas, você segue muitas das mesmas etapas da configuração de uma Campaign: especificar um público geral, condições de entrada e configurações de envio. Seu Canvas começa quando alguém atende à sua condição de disparo. Em seguida, essa pessoa percorre uma jornada no Canvas até atender às suas condições de saída.

Seu Canvas pode ter qualquer combinação de [mensagens]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), [postergações]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), [experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) e muito mais. Você pode enviar por qualquer canal de envio de mensagens compatível e até mesmo [integrar com plataformas sociais e de anúncios]({{site.baseurl}}/partners/canvas_audience_sync/overview), como Facebook, Google ou TikTok.

Confira estes recursos adicionais para saber mais sobre o Canvas:

- Braze Learning: [Orquestração de jornadas com Canvas Flow](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Criar um Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)
- [Esboços de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/canvas_outlines)

## Canais de envio de mensagens {#messaging-channels}

Os canais de envio de mensagens são os diversos canais de comunicação por meio dos quais você pode interagir com seus clientes e entregar mensagens direcionadas.

![Diagrama dos canais de envio de mensagens disponíveis na Braze por meio do SDK.]({% image_buster /assets/img/getting_started/channels.png %})

A tabela a seguir descreve nossos canais compatíveis.

| Canal                                                                                              | Descrição                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [E-mail]({{site.baseurl}}/user_guide/channels/email)                        | Envie e-mails personalizados para a caixa de entrada dos seus usuários.                                                                                                       |
| [Push para dispositivos móveis]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)                   | Entregue mensagens diretamente nos dispositivos móveis dos usuários como notificações.                                                                                   |
| [Web push]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web)                         | Entregue notificações nos navegadores web dos usuários, mesmo quando eles não estão ativamente no seu website.                                                         |
| [In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages)    | Exiba mensagens dentro do seu app enquanto os usuários o estão usando ativamente.                                                                             |
| [SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)*                   | Envie mensagens de texto para os celulares dos usuários.                                                                                                            |
| [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)*              | Envie mensagens pela popular plataforma de mensagens WhatsApp para alcançar e interagir com seus usuários.                                                   |
| [Banners]({{site.baseurl}}/user_guide/channels/banners)*       | Incorpore mensagens diretamente no seu app ou website. |
| [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)*       | Forneça uma caixa de entrada dentro do seu app ou website onde os usuários podem receber e interagir com mensagens, ou exiba mensagens em um carrossel, como um banner e muito mais. |
| [TV conectada]({{site.baseurl}}/developer_guide/platforms/tv_and_ott)                           | Interaja com os usuários em plataformas de televisão conectada.                                                                                                   |
| [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks) | Ative a comunicação em tempo real e a integração com sistemas externos por meio de retornos de chamada HTTP personalizados.                                                    |
| [LINE]({{site.baseurl}}/user_guide/channels/line) | Interaja com os usuários no LINE, o app de mensagens mais popular do Japão.                                                    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canais de envio de mensagens" }

<sup>Disponível como recurso adicional.</sup>

{% alert tip %}
Para mensagens curtas e urgentes que podem ser comunicadas pela maioria dos canais (e-mail, SMS, push), aproveite o filtro de [canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel) para enviar automaticamente a mensagem pelo melhor canal para cada usuário.
{% endalert %}