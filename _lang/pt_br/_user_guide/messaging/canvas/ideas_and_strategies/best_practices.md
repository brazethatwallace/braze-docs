---
nav_title: Práticas recomendadas
article_title: Práticas recomendadas do Canvas
page_order: 1
description: "Este artigo apresenta algumas práticas recomendadas para criar e personalizar jornadas de usuários com o Canvas e o Canvas Flow."
tool: Canvas

---

# Práticas recomendadas do Canvas

> Este artigo apresenta algumas práticas recomendadas para criar e personalizar jornadas de usuários com o Canvas e o Canvas Flow.

## Identifique seu objetivo

Mergulhe no o quê, quem e por quê!
- O que você está tentando ajudar os usuários a realizar?
- Quem são os usuários que você quer alcançar?
- Por que você está criando este Canvas?

## Misture e combine

Desbloqueie novas combinações de jornadas de usuários com os [componentes do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/).
- Divida seus usuários com a [Divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) e crie fluxos de trabalho diferentes.
- Espalhe suas jornadas de usuários com uma etapa de [Postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/).
- Adicione [mensagens independentes]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) em qualquer lugar que desejar no fluxo do seu Canvas.

{% alert note %}
As etapas do Canvas só podem mover os usuários para frente no fluxo. Não é possível configurar um Canvas para vincular uma etapa a uma etapa anterior, pois isso enviaria os usuários para trás. Essa validação garante que os usuários progridam em uma única direção pelo seu Canvas.
{% endalert %}

## Crie mensagens mais ricas

Atraia seus usuários com mensagens mais ricas.

- Crie [mensagens no app]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) para Canvas de integração e aproveite ao máximo a primeira impressão.
- Inclua [Cartões de conteúdo]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/) em uma jornada do Canvas para ofertas promocionais e notificações por push.

## Teste suas jornadas de usuários

Determine o impacto do envio de mensagens do seu Canvas incorporando grupos de controle. Dessa forma, você pode entender como seu Canvas foi recebido!

- Nomeie cada etapa do seu Canvas para identificar sua jornada de usuário.
- Aproveite o componente [Jornadas do experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) na sua jornada de usuário para atribuir aleatoriamente os usuários a diferentes jornadas que você criar.
- Diversifique suas jornadas de usuários com etapas de Postergação e Mensagem para ajudar a descobrir qual jornada é mais eficaz.
- Confira a [análise de dados do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para ver a performance de cada componente na sua jornada de usuário.
- [Edite seu Canvas]({{site.baseurl}}/post-launch_edits/) após o lançamento inicial.

## Programando seus Canvas

{% alert note %}
O Canvas impedirá que você use o envio agendado com um horário que já passou. No entanto, é possível lançar um Canvas durante o mesmo minuto exato em que a campanha está agendada (ou nos segundos anteriores). Isso pode fazer com que o Canvas perca o horário de entrada agendado e os usuários não entrem no Canvas. Recomendamos enviar os Canvas imediatamente caso alguma campanha seja editada poucos minutos antes do horário de envio agendado.
{% endalert %}

Para etapas do Canvas, considere os seguintes detalhes ao programar seu Canvas:

- As alterações de programação serão aplicadas apenas aos usuários que ainda não estão aguardando para receber a etapa.
- As alterações de público, por padrão, se aplicam a todos os usuários, a menos que você programe as alterações para serem aplicadas apenas aos usuários que não estão aguardando para receber a etapa.
- Editar um Canvas que está programado para ser enviado assim que implantado e selecionar **Atualizar** fará com que ele seja enviado imediatamente.