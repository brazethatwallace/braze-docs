---
nav_title: Melhores práticas
article_title: Melhores práticas do Canvas
page_order: 1
description: "Este artigo apresenta algumas melhores práticas para criar e personalizar jornadas de usuários com o Canvas e o Canvas Flow."
tool: Canvas

---

# Melhores práticas do Canvas {#canvas-best-practices}

> Este artigo apresenta algumas melhores práticas para criar e personalizar jornadas de usuários com o Canvas e o Canvas Flow.

## Identifique seu objetivo {#identify-your-purpose}

Mergulhe no o quê, quem e por quê!
- O que você está tentando ajudar os usuários a realizar?
- Quem são os usuários que você quer alcançar?
- Por que você está criando este Canvas?

## Misture e combine {#mix-and-match}

Desbloqueie novas combinações de jornadas de usuários com os [componentes do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/).
- Divida seus usuários com a [Divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) e crie fluxos de trabalho diferentes.
- Espalhe suas jornadas de usuários com uma etapa de [Postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/).
- Adicione [mensagens independentes]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) em qualquer lugar que desejar no fluxo do seu Canvas.

{% alert note %}
As etapas do Canvas só podem mover os usuários para frente no fluxo. Não é possível configurar um Canvas para vincular uma etapa a uma etapa anterior, pois isso enviaria os usuários para trás. Essa validação garante que os usuários progridam em uma única direção pelo seu Canvas.
{% endalert %}

## Crie mensagens mais ricas {#create-richer-messages}

Atraia seus usuários com mensagens mais ricas.

- Crie [mensagens no app]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) para Canvas de integração e aproveite ao máximo a primeira impressão.
- Inclua [Content Cards]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/) em uma jornada do Canvas para ofertas promocionais e notificações por push.

## Teste suas jornadas de usuários {#test-your-user-journeys}

Determine o impacto do envio de mensagens do seu Canvas incorporando grupos de controle. Dessa forma, você pode entender como seu Canvas foi recebido!

- Nomeie cada etapa do seu Canvas para identificar sua jornada de usuário.
- Aproveite o componente [Jornadas do experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) na sua jornada de usuário para atribuir aleatoriamente os usuários a diferentes jornadas que você criar.
- Diversifique suas jornadas de usuários com etapas de Postergação e Mensagem para ajudar a descobrir qual jornada é mais eficaz.
- Confira a [análise de dados do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para ver o desempenho de cada componente na sua jornada de usuário.
- [Edite seu Canvas]({{site.baseurl}}/post-launch_edits/) após o lançamento inicial.

## Programando seus Canvas {#scheduling-your-canvases}

{% alert note %}
O Canvas impedirá que você use o envio agendado com um horário que já passou. No entanto, é possível lançar um Canvas durante o mesmo minuto exato em que a campanha está agendada (ou nos segundos anteriores). Isso pode fazer com que o Canvas perca o horário de entrada agendado e os usuários não entrem no Canvas. Recomendamos enviar os Canvas imediatamente caso alguma campanha seja editada poucos minutos antes do horário de envio agendado.
{% endalert %}

Para etapas do Canvas, considere os seguintes detalhes ao programar seu Canvas:

- As alterações de programação serão aplicadas apenas aos usuários que ainda não estão aguardando para receber a etapa.
- As alterações de público, por padrão, se aplicam a todos os usuários, a menos que você programe as alterações para serem aplicadas apenas aos usuários que não estão aguardando para receber a etapa.
- Editar um Canvas que está programado para ser enviado assim que implantado e selecionar **Atualizar** fará com que ele seja enviado imediatamente.

### Edições pós-lançamento {#post-launch-edits}

Se você parar um Canvas ativo enquanto um rascunho não salvo existir, a parada pode descartar esse rascunho. Salve, lance ou descarte o rascunho antes de parar, caso precise manter as edições em andamento.

#### Momento da avaliação do público {#audience-evaluation-timing}

A Braze avalia os públicos em diferentes pontos no criador do Canvas e nas etapas individuais. Para detalhes de configuração, consulte:

- [Defina seu público-alvo de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-13-set-your-target-entry-audience) e [Determine o cronograma de entrada do seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-12-determine-your-canvas-entry-schedule) ao criar um Canvas
- [Como o público-alvo e os critérios de entrada funcionam juntos]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/#how-target-audience-and-entry-criteria-work-together)
- [Editar configurações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) para etapas de Mensagem
- [Como os usuários são avaliados]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/#how-users-are-evaluated) para etapas de Jornadas do público

Se você editar um Canvas ativo próximo a uma janela de entrada ou envio agendado, os usuários já enfileirados para uma etapa de **Mensagem** podem não receber suas alterações. Para saber mais, consulte [Editar Canvas após o lançamento]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/).