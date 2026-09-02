---
nav_title: Melhores práticas
article_title: Melhores práticas para Campaigns
page_order: 0
description: "Este artigo apresenta melhores práticas para criar e personalizar suas campanhas."
tool: Campaign

---

# Melhores práticas para campanhas {#campaign-best-practices}

> Este artigo apresenta melhores práticas para criar e personalizar suas campanhas.

## Os quatro T's da Braze {#four-ts-of-braze}

A Braze recomenda que você envie apenas dados de clientes que pretende utilizar na plataforma. Considere a filosofia dos "Quatro T's da Braze" para garantir que você envie apenas dados que serão usados para:

- **Target (Direcionar)** seus públicos criando [segmentos de público]({{site.baseurl}}/user_guide/audience/segments).
- **Trigger (Disparar)** suas mensagens com entrega [baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) ou [disparada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery).
- **Template (Modelar)** e personalizar suas mensagens com [lógica condicional Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid).
- **Track (Rastrear)** a eficácia das suas campanhas com [rastreamento de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).

Isso permite otimizar os dados que você envia para a Braze e agilizar sua capacidade de enviar mensagens aos usuários, evitando o rastreamento de pontos de dados que sua equipe pode não considerar úteis a longo prazo.

## Direcionamento de usuários {#user-targeting}

À medida que você desenvolve suas campanhas ao longo do tempo, pode notar quedas no seu público. Nesse momento crucial, você pode direcionar seus [usuários inativos]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users) com uma campanha especializada usando segmentação.

### Identifique seu público {#identify-your-audience}

Aproveite segmentos e filtros a seu favor ao definir seu público. Considere quem sua campanha e mensagens estão direcionando. Com essa informação essencial, você pode criar [campanhas multicanal]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#create-a-multichannel-campaign) que oferecem a flexibilidade de construir suas mensagens em diferentes canais para atender às preferências de notificação do seu público.

Também é importante entender seus [usuários ativos]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/active_user_campaigns) para demonstrar apreço pelos seus usuários mais consistentes.

## Campanhas multicanal {#multichannel-campaigns}

### Divulgação de funcionalidades {#feature-awareness}

Se seu objetivo é atrair os usuários para uma nova funcionalidade ou versão do app, use uma estratégia multicanal com foco em canais no app. [Mensagens no app]({{site.baseurl}}/in-app_messages) e [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards) geralmente são menos intrusivos caso o usuário não queira atualizar imediatamente.

Certifique-se de incluir [deep links]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls) para a loja de apps apropriada.

Convencer os usuários a atualizar o app ou mudar a forma como usam seu app pode ser difícil. Portanto, informe-os sobre todos os benefícios da nova versão ou funcionalidades e como isso melhorará a experiência deles com o app.

### Momento do envio {#send-timing}

O momento certo é fundamental! Quando seu objetivo é convencer os usuários a atualizar o app, espere até que eles tenham uma experiência positiva dentro do app para fazer a solicitação. Para manter seu público engajado, evite mensagens repetitivas que possam parecer intrusivas.

Com o tempo, seus usuários podem esquecer certas funcionalidades ou não perceber novas funcionalidades. Quando novas funcionalidades forem adicionadas, avise seus usuários com [mensagens no app]({{site.baseurl}}/in-app_messages). Se os usuários não estão interagindo com funcionalidades importantes dentro do app, pode ser melhor lembrá-los quando estiverem usando o app e quando essa nova funcionalidade seria útil. Nosso artigo sobre [opt-in de dados]({{site.baseurl}}/user_guide/channels/content_cards) tem mais informações sobre como garantir que sua solicitação esteja alinhada com as expectativas de fluxo de trabalho dos usuários.

## Avaliações altas {#high-ratings}

Conseguir avaliações de cinco estrelas na loja de apps está na lista de desejos de todo profissional de marketing mobile. No entanto, alcançar avaliações positivas não é tarefa fácil, pois exige um esforço extra dos seus usuários. Aplicando nossas funcionalidades de maneiras inteligentes, podemos ajudar você a aumentar o engajamento dos seus clientes.

### Direcionando usuários avançados {#targeting-power-users}

Usuários avançados podem ser defensores do seu app. Geralmente, eles interagem com o app de forma consistente e podem fornecer feedback para melhorá-lo. Embora variem de app para app, os usuários avançados tendem a ter as seguintes características:

- Muitas sessões registradas
- Uso recente do app
- Gastos e compras realizadas

Para garantir avaliações mais altas, peça aos seus usuários avançados que avaliem seu app na loja de apps, pois eles têm mais chances de ter coisas boas a dizer. Por exemplo, você poderia criar um Segment chamado "Usuários avançados" com estes filtros:
- Usou estes apps mais de 10 vezes nos últimos 14 dias
- Gastou mais de 50 dólares

![Um exemplo de Segment que direciona usuários avançados de um app.]({% image_buster /assets/img_archive/ratings_power_users.png %})

Visitar a loja de apps demanda tempo dos seus usuários. Para maximizar a probabilidade de que eles façam esse esforço extra, solicite uma avaliação logo após uma experiência positiva com o app. Por exemplo, peça após eles passarem de fase em um jogo ou realizarem uma compra usando um código de desconto. Nosso artigo sobre [opt-in de dados]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) tem mais informações sobre formas de garantir que sua solicitação esteja alinhada com as expectativas de fluxo de trabalho dos usuários.

## Agendando suas campanhas {#scheduling-your-campaigns}

Ao editar agendamentos ou públicos de campanhas, observe as seguintes melhores práticas:

- **Campanhas com agendamento único:** você pode editar a campanha até o horário de envio agendado.
- **Campanhas com agendamento recorrente:** você pode editar a campanha até o horário de envio agendado.
- **Campanhas com horário de envio local:** não faça edições nas 24 horas anteriores ao horário de envio agendado.
- **Campanhas com horário de envio otimizado:** não faça edições nas 24 horas anteriores à meia-noite do dia em que a campanha está agendada para ser enviada.

Para detalhes sobre agendamento de Canvas (rascunhos, paradas e avaliação próxima ao horário de envio), consulte [Melhores práticas de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/best_practices#scheduling-your-canvases).

{% alert note %}
Editar uma campanha ativa e alterar a entrega para **Horário de Envio Local** fará com que um novo lote de mensagens seja enfileirado. Isso significa que seus usuários receberão a mensagem duas vezes, pois ela será enfileirada duas vezes. Para evitar isso, primeiro pare a campanha original e depois lance uma duplicata após atualizar o agendamento.
{% endalert %}