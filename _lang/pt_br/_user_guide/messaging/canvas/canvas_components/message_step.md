---
nav_title: Mensagem
article_title: Mensagem
alias: "/message_step/"
page_order: 11
page_type: reference
description: "Este artigo de referência aborda como criar uma mensagem independente usando a etapa de Mensagem."
tool: Canvas

---

# Mensagem {#message}

> As etapas de Mensagem permitem adicionar uma mensagem independente onde você quiser no seu Canvas.

![Uma etapa de Mensagem chamada "Lunch promo" usando o canal de push.]({% image_buster /assets/img/canvas_components/message_step1.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

## Criar uma mensagem {#create-a-message}

Para criar um componente de Mensagem, primeiro adicione uma etapa ao seu Canvas. Arraste e solte o componente da barra lateral ou selecione o botão de mais <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Message**.

### Etapa 1: Selecione seu canal de envio de mensagens {#step-1-select-your-messaging-channel}

Você pode selecionar entre os seguintes canais de envio de mensagens:
- Banners
- Content Cards
- E-mail
- LINE
- Notificações por push
- SMS/MMS/RCS
- Mensagens no app
- Webhook
- WhatsApp

![Uma lista de canais de envio de mensagens disponíveis para selecionar na etapa de Mensagem.]({% image_buster /assets/img/canvas_components/message_step2.png %})

### Etapa 2: Edite as configurações de entrega {#step-2-edit-delivery-settings}

Em seguida, você pode editar as configurações de Intelligent Delivery, substituições de horário de silêncio e validação de entrega.

#### Intelligent Timing {#intelligent-timing}

Você pode ativar o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/) com uma opção de fallback quando o perfil de um usuário não tiver dados suficientes para calcular um horário ideal. Recomendamos ativar o Intelligent Timing e o [limite de taxa]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#rate-limiting-and-frequency-capping/) como uma verificação adicional para quaisquer atrasos entre a entrada dos usuários na etapa de Mensagem e o envio real da mensagem.

Selecione **Using Intelligent Timing** na guia **Delivery Settings**. Aqui, você pode selecionar o horário mais popular ou um horário de fallback específico. Se o horário de silêncio estiver ativado, a etapa de Mensagem também permite substituir essa configuração.

![A guia Delivery Settings para as configurações do componente de Mensagem. O horário de silêncio está ativado e a caixa de seleção Using Intelligent Timing está marcada para entregar a mensagem no horário ideal.]({% image_buster /assets/img/canvas_components/message_step4.png %}){: style="max-width:90%;"}

#### Validações de entrega {#delivery-validations}

As validações de entrega fornecem uma verificação adicional no momento do envio da mensagem para confirmar que seu público ainda atende aos seus critérios. Recomendamos usá-las quando o horário de silêncio, o Intelligent Timing ou o limite de taxa estiverem ativados. Selecione **Validate audience at message send** e adicione um Segment ou filtros adicionais. Se um usuário não atender às validações, escolha se ele sai do Canvas ou avança para a próxima etapa.

As validações de entrega avaliam os critérios do perfil do usuário no momento do envio. Filtros relacionados a apps verificam se um usuário usou recentemente ou já usou um app específico, mas não confirmam qual app o usuário está usando na sessão atual.

Se o seu espaço de trabalho tiver vários apps e uma etapa de Mensagem precisar direcionar um app específico, use uma das seguintes abordagens:

- Ao compor a mensagem, [especifique suas plataformas de entrega]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/#step-2-specify-delivery-platforms), como **Mobile Apps** ou **Web Browsers**.
- Use Liquid para verificar o dispositivo ou app direcionado no momento do envio:
  - {% raw %}`{{targeted_device.${platform}}}`{% endraw %} avalia a plataforma da sessão atual do usuário. Para saber mais, consulte [Informações do dispositivo direcionado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/#targeted-device-information).
  - {% raw %}`{{app.${api_id}}}`{% endraw %} avalia qual app está solicitando a mensagem. Combine essa tag com `abort_message()` para evitar envios para o app errado. Para saber mais, consulte [Informações do app direcionado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/#targeted-app-information).

![As validações de entrega estão ativadas para validar o público no momento do envio da mensagem. O comportamento de avanço das validações de entrega está configurado para avançar o usuário para a próxima etapa do Canvas se as validações de entrega não forem atendidas.]({% image_buster /assets/img/canvas_components/message_step5.png %}){: style="max-width:90%;"}

## Como os usuários avançam {#how-users-advance}

Todos os usuários que entram na etapa de Mensagem avançam para a próxima etapa quando qualquer uma das seguintes condições for atendida:

- Qualquer mensagem é enviada
- Uma mensagem tem limite de frequência e não é enviada
- Uma mensagem é cancelada
- Um usuário não é alcançável pelo canal, então a mensagem não é enviada
- Um usuário não atende aos critérios em **Delivery validations**

{% raw %}
Se um Canvas baseado em ação for disparado por uma mensagem SMS recebida, você pode referenciar as propriedades do SMS na primeira etapa (etapa de Mensagem) ou em uma etapa de Mensagem aninhada em uma etapa de Jornadas de ação. Por exemplo, na etapa de Mensagem, você pode usar `{{sms.${inbound_message_body}}}` ou `{{sms.${inbound_media_urls}}}`.
{% endraw %}

## Referenciar propriedades de contexto {#reference-context-properties}

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

As propriedades de entrada são configuradas na etapa **Entry Schedule** ao criar um Canvas e indicam o gatilho que faz um usuário entrar em um Canvas. Essas propriedades também podem acessar as propriedades das cargas úteis de entrada em Canvas disparados por API. Observe que o objeto `context` tem um limite máximo de tamanho de 50 KB.

As propriedades de entrada podem ser usadas em Liquid em qualquer etapa de Mensagem. Use o seguinte Liquid ao referenciar essas propriedades de entrada: {% raw %}``{context.${property_name}}``{% endraw %}. Os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

{% alert note %}
Especificamente para canais de mensagens no app, `context` só pode ser referenciado no Canvas.
{% endalert %}

Use o seguinte Liquid ao referenciar essas propriedades de entrada: {% raw %}``context.${property_name}``{% endraw %}. Observe que os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

{% raw %}
Por exemplo, considere a seguinte requisição: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`. Você pode adicionar a palavra "shoes" a uma mensagem com o Liquid `{{context.${product_name}}}`.
{% endraw %}

Você também pode aproveitar as [propriedades de entrada persistentes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/) em qualquer etapa de Mensagem para guiar seus usuários por etapas personalizadas ao longo do fluxo de trabalho do seu Canvas.

### Propriedades de evento {#event-properties}

As propriedades de evento referem-se às propriedades que você define para eventos personalizados e eventos de compra. Essas propriedades de evento podem ser usadas em Campaigns com entrega baseada em ação, bem como em Canvas.

No Canvas, as propriedades de eventos personalizados e de compra podem ser usadas em Liquid em qualquer etapa de Mensagem que siga uma etapa de [Jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/). Por exemplo, ao referenciar `event_properties`, use este trecho de Liquid: {% raw %}``{{event_properties.${property_name}}}``{% endraw %}

{% alert important %}
`event_properties` não pode ser usado independentemente das etapas de Jornadas de ação.
{% endalert %}

Na primeira etapa de Mensagem após uma Jornada de ação, você pode usar `event_properties` relacionadas ao evento referenciado nessa Jornada de ação. Você pode ter outras etapas (que não sejam outra Jornada de ação ou etapa de Mensagem) entre essa etapa de Jornadas de ação e a etapa de Mensagem. Observe que você só terá acesso a `event_properties` se sua etapa de Mensagem puder ser rastreada até uma jornada que não seja Restante do público em uma etapa de Jornada de ação.

{% alert important %}
Você não pode usar `event_properties` na etapa de Mensagem principal. Em vez disso, você deve usar `context` ou adicionar uma etapa de Jornadas de ação com o evento correspondente antes da etapa de Mensagem que inclui `event_properties`.
{% endalert %}

{% details Expandir para o editor original do Canvas %}

Não é mais possível criar ou duplicar Canvas usando o editor original. Esta seção está disponível apenas para referência.

- `event_properties` não pode ser usado em etapas completas agendadas. No entanto, você pode usar `event_properties` na primeira etapa completa de um Canvas baseado em ação, mesmo que a etapa completa seja agendada.
- `context` pode ser referenciado apenas na primeira etapa completa de um Canvas.
- Especificamente para canais de mensagens no app, `context` pode ser referenciado no editor original do Canvas se você tiver as propriedades de entrada persistentes ativadas como parte do acesso antecipado anterior.

{% enddetails %}

## Análise de dados {#analytics}

Consulte a tabela a seguir para as definições das métricas do componente de Mensagem:

| Métrica | Descrição |
| --- | --- |
| _Entradas_ | O número de vezes que a etapa foi acessada. Se o seu Canvas tiver reelegibilidade e um usuário entrar em uma etapa de Mensagem duas vezes, duas entradas serão registradas. |
| _Avançou para a próxima etapa_ | O número de entradas que avançaram para a próxima etapa no Canvas. |
| _Envios_ | O número total de mensagens que a etapa enviou. Se o seu Canvas tiver reelegibilidade e um usuário entrar em uma etapa de Mensagem duas vezes, duas entradas serão registradas. |
| _Destinatários únicos_ | O número de usuários que receberam mensagens desta etapa. |
| _Evento de conversão primária_ | O número de vezes que um evento definido ocorreu após interagir com ou visualizar uma mensagem recebida de uma Campaign da Braze. Você define esse evento ao criar a Campaign. |
| _Receita_ | A receita total em dólares dos destinatários da Campaign dentro da janela de conversão primária definida. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }