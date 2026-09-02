---
nav_title: Entrega baseada em ação
article_title: Entrega baseada em ação
page_order: 1
page_type: reference
description: "Este artigo de referência descreve como disparar campanhas para envio após um usuário concluir um determinado evento."
tool: Campaigns
local_redirect:
  use-cases: '/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#examples'

---

# Entrega baseada em ação {#action-based-delivery}

> Campanhas de entrega baseada em ação ou campanhas disparadas por eventos são muito eficazes para mensagens transacionais ou baseadas em conquistas. Em vez de enviar sua campanha em dias específicos, você pode dispará-las para envio após um usuário concluir um determinado evento.

## Configurando uma campanha disparada {#setting-up-a-triggered-campaign}

### Etapa 1: Selecione um evento-gatilho {#step-1-select-a-trigger-event}

Selecione um evento-gatilho. Os eventos são organizados por categoria e ficam disponíveis conforme o seu espaço de trabalho e os canais ativados.

- **eCommerce**
    - **Place Order**
    - **Perform Cart Updated Event**
    - **Perform Checkout Started Event**
    - **Perform Checkout Completed Event**
    - **Make Purchase**
- **General activity**
    - **Interact With Campaign**
    - **Interact With Step**
    - **Interact with Landing Page**
    - **Perform Conversion Event**
    - **Perform Custom Event**
    - **Perform Exception Event For Campaign**
    - **Start Session**
- **Inbound messaging**
    - **Send an SMS inbound message**
    - **Send a WhatsApp inbound message**
    - **Send a LINE inbound message**
- **Location**
    - **Enter a Location**
    - **Trigger a Geofence**
- **Profile updates**
    - **Add an Email Address**
    - **Change Custom Attribute Value**
    - **Update Subscription Status**
    - **Update Subscription Group Status**

O grupo **eCommerce** também lista eventos de eCommerce recomendados, como **Perform Product Viewed Event**, **Perform Order Cancelled Event** e **Perform Order Refunded Event**. Essas opções usam **Perform Custom Event** com o nome do evento já preenchido.

Campaigns de mensagens no app aceitam um conjunto menor de gatilhos: **Make Purchase**, **Place Order**, **Start Session**, **Perform Custom Event** e **Interact With Campaign**. Para Campaigns de mensagens no app, **Interact With Campaign** cobre apenas a abertura de um push de qualquer Campaign ou de uma Campaign específica. Não inclui a lista de interações de Campaign a seguir.

Para Campaigns que não sejam de mensagens no app, ao selecionar **Interact With Campaign**, **Interact With Step** ou **Interact with Landing Page**, escolha a interação que deve atuar como gatilho. Cada um desses gatilhos oferece suas próprias interações, e as interações disponíveis dependem dos canais ativados.

{% details Interações de Interact With Campaign %}

- **View in-app message**
- **Click in-app message**
- **Click in-app message button 1**
- **Click in-app message button 2**
- **Submit in-app message survey**
- **Click email**
- **Open email**
- **Open email (machine opens)**
- **Open email (other opens)**
- **Click alias in email**
- **Clicked Alias in any campaign or canvas step**
- **Directly open push notification**
- **Click push notification button**
- **Click push story page**
- **Perform conversion event**
- **Receive email**
- **Receive push notification**
- **Receive webhook**
- **Receive SMS**
- **Click shortened SMS link**
- **View content card**
- **Click content card**
- **Dismiss content card**
- **View banner**
- **Click banner**
- **Dismiss banner**
- **Click tracked WhatsApp link**
- **Click tracked LINE link**
- **Click tracked KakaoTalk link**
- **Are enrolled in control group**

{% enddetails %}

{% details Interações de Interact With Step %}

- **View in-app message**
- **Start in-app message availability window**
- **Submit in-app message survey**
- **Click email**
- **Open email**
- **Open email (machine opens)**
- **Open email (other opens)**
- **Click alias in email**
- **Clicked Alias in any campaign or canvas step**
- **Directly open push notification**
- **Click push notification button**
- **Click push story page**
- **Receive email**
- **Receive push notification**
- **Receive webhook**
- **Receive SMS**
- **Click shortened SMS link**
- **View content card**
- **Click content card**
- **Dismiss content card**
- **View banner**
- **Click banner**
- **Dismiss banner**
- **Click tracked WhatsApp link**
- **Click tracked LINE link**
- **Click tracked KakaoTalk link**

{% enddetails %}

{% details Interações de Interact with Landing Page %}

- **Submit form**
- **Submit survey**

{% enddetails %}

Você também pode filtrar ainda mais os eventos-gatilho por meio das [propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) da Braze, permitindo propriedades de evento personalizáveis para eventos personalizados e compras no app. Esse recurso possibilita refinar quais usuários recebem uma mensagem com base em atributos específicos do evento personalizado, proporcionando maior personalização de Campaigns e coleta de dados mais sofisticada.

Por exemplo, imagine que temos uma Campaign com um evento personalizado de carrinho abandonado que é ainda mais direcionada pelo filtro de propriedade "valor do carrinho". Essa Campaign alcança apenas os usuários que deixaram entre $100 e $200 em produtos nos seus carrinhos.

![Campaign de carrinho abandonado filtrada por uma propriedade de evento personalizado para valor do carrinho entre $100 e $200.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
O evento-gatilho **Start Session** pode ser a primeira abertura do app pelo usuário se o Segment or segmento da sua Campaign se aplicar a novos usuários (por exemplo, se o seu Segment or segmento incluir aqueles sem sessões).
{% endalert %}

Lembre-se de que você ainda pode enviar uma Campaign disparada para um Segment or segmento específico de usuários, portanto usuários que não fazem parte do Segment or segmento não recebem a Campaign mesmo que completem o evento-gatilho.

Com relação ao evento-gatilho para quando um usuário adiciona um endereço de e-mail ao perfil, as seguintes regras se aplicam:

- O evento-gatilho é disparado depois que o atributo do perfil de usuário é atualizado. Isso significa que a avaliação dos Segments e filtros da Campaign acontece após qualquer atualização de atributo. Isso é útil porque permite configurar filtros como "endereço de e-mail corresponde a gmail.com" para criar uma Campaign disparada que envia apenas para usuários do Gmail assim que eles adicionam o endereço de e-mail.
- O evento-gatilho é disparado quando um endereço de e-mail é adicionado a um perfil de usuário. Se você tiver vários perfis de usuário criados com o mesmo endereço de e-mail, a Campaign pode ser disparada várias vezes, uma para cada perfil de usuário.

Além disso, mensagens no app disparadas ainda seguem as regras de entrega de mensagens no app e aparecem no início de uma sessão do app.

### Etapa 2: Selecione a duração da postergação {#step-2-select-delay-length}

Selecione quanto tempo esperar antes de enviar a Campaign após os critérios de gatilho serem atendidos. Se a duração da postergação for maior do que a duração de envio da mensagem, nenhum usuário receberá a Campaign.

Campaigns de mensagens no app podem postergar a entrega após o evento-gatilho em até duas horas (7.200 segundos). As opções de postergação são **Immediately** e **After a delay**. Para uma espera mais longa, adicione uma etapa de [postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) antes de uma etapa de mensagem no app em um Canvas.

{% alert important %}
A Braze usa o timestamp enviado com o evento personalizado para avaliar a postergação de uma Campaign baseada em ação. Se esse timestamp for antedatado, a Braze pode considerar a postergação como já expirada e enviar a mensagem imediatamente ou antes do esperado. Para evitar uma entrega fora do momento planejado, envie o timestamp do evento personalizado com a hora atual.
{% endalert %}

Além disso, os usuários que completam o evento-gatilho após o lançamento da sua Campaign são os primeiros a receber a mensagem depois que a postergação expirar. Os usuários que completaram o evento-gatilho antes do lançamento da Campaign não se qualificam para recebê-la.

Você também pode enviar a Campaign em um dia específico da semana selecionando **On the next day of the week**, ou um número definido de dias no futuro selecionando **After a number of calendar days**. Outra opção é enviar sua mensagem usando o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) em vez de selecionar manualmente um horário de entrega.

### Etapa 3: Selecione eventos de exceção {#step-3-select-exception-events}

Selecione um evento de exceção que desqualifica os usuários de receber essa Campaign. Você só pode fazer isso se a sua mensagem disparada for enviada após uma postergação. [Eventos de exceção]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) podem ser fazer uma compra, iniciar uma sessão, realizar um dos [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) designados da Campaign ou realizar um evento personalizado.

Se um usuário completar o evento-gatilho, mas em seguida completar o evento de exceção antes de a mensagem ser enviada por causa da postergação, ele não receberá a Campaign. Usuários que não recebem a Campaign devido ao evento de exceção são automaticamente elegíveis para recebê-la no futuro, na próxima vez que completarem o evento-gatilho, mesmo que você não tenha optado por tornar os usuários [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

Para saber mais sobre o uso de eventos de exceção, consulte [Exemplos](#examples).

Se você enviar uma Campaign com um evento-gatilho que corresponda ao evento de exceção, a Braze cancelará a Campaign e reagendará automaticamente uma nova Campaign com base no horário de entrega da mensagem do evento de exceção. Por exemplo, se o seu primeiro evento-gatilho começar aos cinco minutos e o evento de exceção aos 10 minutos, a Braze usará os 10 minutos do evento de exceção como o horário oficial de entrega da mensagem da Campaign.

{% alert note %}
Você não pode definir "início de sessão" como evento-gatilho e evento de exceção ao mesmo tempo para uma Campaign. No entanto, você sempre pode selecionar qualquer outro evento personalizado além dessa opção.
{% endalert %}

### Etapa 4: Defina a duração {#step-4-assign-duration}

Defina a duração da Campaign especificando um horário de início e, opcionalmente, um horário de término.

Se um usuário completar um evento-gatilho dentro do período especificado, mas se qualificar para a mensagem fora desse período devido a uma postergação agendada, ele não receberá a Campaign. Portanto, se você definir uma postergação maior do que o período da mensagem, nenhum usuário receberá a sua Campaign. Além disso, você pode optar por enviar a mensagem no [fuso local]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) dos usuários.

### Etapa 5: Selecione o período {#step-5-select-time-frame}

Selecione se o usuário receberá a Campaign durante uma parte específica do dia. Se você definir um período para a mensagem e o usuário completar o evento-gatilho fora desse período, ou se a postergação fizer com que ele perca o período, por padrão, o usuário não receberá a mensagem.

No caso em que um usuário completa o evento-gatilho dentro do período, mas a postergação faz com que ele fique fora do período, você pode marcar a caixa de seleção **Send at the next available time if the delivery time falls outside the specified portion of the day** para que esses usuários ainda recebam a Campaign.

Se um usuário não receber a mensagem porque perdeu o período, ele ainda é qualificado para recebê-la na próxima vez que completar o evento-gatilho, mesmo que você não tenha optado por tornar os usuários [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility). Se você optar por tornar os usuários reelegíveis, eles podem receber a Campaign cada vez que completarem o evento-gatilho, desde que se qualifiquem dentro do período especificado.

Se você também tiver definido uma duração para a Campaign, o usuário deve se qualificar tanto dentro da duração quanto dentro da parte específica do dia para receber a mensagem.

### Etapa 6: Determine a reelegibilidade {#step-6-determine-re-eligibility}

Determine se os usuários podem se tornar [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) para a Campaign. Se você permitir que os usuários se tornem reelegíveis, poderá especificar uma postergação antes que o usuário possa receber a Campaign novamente. Isso evita que suas Campaigns disparadas se tornem excessivas.

## Exemplos {#examples}

Campanhas disparadas são muito eficazes para mensagens transacionais ou baseadas em conquistas.

Campanhas transacionais incluem mensagens enviadas depois que o usuário conclui uma compra ou adiciona um item ao carrinho. O último caso é um ótimo exemplo de Campaign que se beneficia de um evento de exceção. Digamos que sua Campaign lembre os usuários sobre itens no carrinho que eles ainda não compraram. O evento de exceção, nesse caso, seria o usuário comprando os produtos do carrinho. Para campanhas baseadas em conquistas, você pode enviar uma mensagem cinco minutos depois que o usuário concluir uma conversão ou passar de fase em um jogo.

Além disso, ao criar campanhas de boas-vindas, você pode disparar mensagens para serem enviadas após o usuário se registrar ou configurar uma conta. Escalonar as mensagens para serem enviadas em diferentes dias após o registro permite criar um processo de integração completo.

## Perguntas frequentes {#frequently-asked-questions}

### Qual é o atraso máximo após um disparo para campanhas de mensagens no app? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

Duas horas (7.200 segundos). Para ver as opções de atraso disponíveis e como configurar uma espera mais longa, consulte [Etapa 2: Selecione a duração do atraso](#step-2-select-delay-length).

### Por que um usuário não recebeu minha Campaign disparada? {#why-did-a-user-not-receive-my-triggered-campaign}

Qualquer uma dessas situações impede que um usuário que completou o evento-gatilho receba a Campaign:

- O usuário completou o evento de exceção antes que o atraso tenha transcorrido completamente.
- A [lógica `abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) do Liquid foi usada e a mensagem foi interrompida com base na lógica ou regras de `abort_message`.
- O atraso fez com que o usuário se tornasse qualificado para receber a Campaign após o término da duração.
- O atraso fez com que o usuário se tornasse qualificado para receber a Campaign fora da porção especificada do dia.
- O usuário já recebeu a Campaign (incluindo atribuição por meio de identificadores de canal compartilhados — por exemplo, se ele compartilha um e-mail com alguém que recebeu, abriu ou clicou nele), e os usuários não se tornam reelegíveis.
- Embora os usuários sejam reelegíveis para receber a Campaign, eles só podem redispará-la após um determinado período, e esse período ainda não transcorreu.

[Segmentar]({{site.baseurl}}/user_guide/audience/segments) uma Campaign disparada com base em dados de usuários registrados no momento do evento pode causar uma [condição de corrida]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions). Isso acontece quando o atributo do usuário no qual a Campaign é segmentada é alterado, mas a alteração ainda não foi processada para o usuário quando a Campaign é enviada. Como as campanhas verificam a participação no Segment or segmento na entrada, isso pode fazer com que o usuário não receba a Campaign.

Por exemplo, imagine que você quer enviar uma Campaign disparada por evento para usuários masculinos que acabaram de se registrar. Quando o usuário se registra, você grava um evento personalizado `registration` e simultaneamente define o atributo `gender` do usuário. O evento pode disparar a Campaign antes que a Braze tenha processado o gênero do usuário, impedindo-o de receber a Campaign.

Como prática recomendada, garanta que o atributo no qual a Campaign é segmentada seja enviado aos servidores da Braze antes do evento. Se isso não for possível, a melhor forma de garantir a entrega é usar [propriedades de evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) para anexar as propriedades relevantes do usuário ao evento e aplicar um filtro de propriedade para a propriedade específica do evento em vez de um filtro de segmentação. No nosso exemplo, adicione uma propriedade `gender` ao evento personalizado `registration` para que a Braze tenha garantidamente os dados necessários quando sua Campaign for disparada.

Além disso, se uma Campaign é baseada em ação e tem um atraso, você pode marcar a opção **Reavaliar participação no Segment or segmento no momento do envio** para garantir que os usuários ainda façam parte do público-alvo quando a mensagem for enviada.

#### Avaliação dos critérios de público {#audience-criteria-evaluation}

Para campanhas que envolvem um atraso antes do envio (incluindo limite de frequência, fuso local, Intelligent Timing ou cronograma de disparo), o momento em que o Segment or segmento é reavaliado depende do tipo e das configurações da Campaign.

Em campanhas baseadas em ação com atraso, se você selecionar **Reavaliar participação no Segment or segmento no momento do envio**, os usuários serão reavaliados antes do envio da mensagem, de modo que apenas os usuários que ainda atendam aos critérios do Segment or segmento no momento do envio receberão a mensagem.

Se sua Campaign é disparada por um evento personalizado específico e você seleciona um Segment or segmento como público, os usuários precisam realizar o mesmo evento personalizado para serem incluídos no Segment or segmento. Isso significa que os usuários precisam fazer parte do público antes que uma Campaign baseada em ação possa ser disparada. O fluxo geral de uma Campaign disparada é o seguinte:

1. **Entrar no público:** Quando um usuário realiza o evento personalizado, ele é adicionado ao público-alvo da Campaign.
2. **Disparar o e-mail:** O usuário precisa realizar o evento personalizado novamente para disparar o e-mail, pois ele precisa fazer parte do público antes que o e-mail possa ser enviado.

Recomendamos alterar o público-alvo para incluir todos os usuários ou verificar se os usuários que devem realizar o evento já fazem parte do público da Campaign para que a mensagem seja disparada.

![Captura de tela relacionada à avaliação dos critérios de público.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### Solução de problemas de eventos personalizados {#troubleshooting-custom-events}

Primeiro, confirme que o evento personalizado está sendo enviado para a Braze. Acesse **Analytics** > **Custom Events Report** e selecione o respectivo evento personalizado e o intervalo de datas. Se o evento não aparecer, confirme que ele está configurado corretamente e que o usuário realizou a ação correta.

Se o evento personalizado aparecer, continue a solução de problemas fazendo o seguinte:

- Verifique o download do perfil do usuário para confirmar que ele disparou o evento e quando isso aconteceu. Se o evento foi disparado, compare o timestamp de quando o evento foi disparado com o momento em que a Campaign ficou ativa. O evento pode ter sido disparado antes da Campaign ficar ativa.
- Revise os changelogs da Campaign e de quaisquer Segments usados no direcionamento para determinar se o usuário estava no Segment or segmento quando o evento personalizado foi disparado. Se ele não estava no Segment or segmento, ele não teria recebido a Campaign.
- Verifique se o usuário foi inserido em um grupo de controle por meio de segmentação e, consequentemente, impedido de receber a Campaign.
- Se houver um atraso agendado, verifique se o evento personalizado do usuário foi disparado antes do atraso. Se o evento foi disparado antes do atraso, ele não teria recebido a Campaign.

{% alert note %}
Mensagens no app só podem ser disparadas por eventos enviados pelo SDK or kit de desenvolvimento de software, não pela REST or transferir estado representacional API or interface de programação do aplicativo (API).
{% endalert %}

### Quando as campanhas baseadas em ação avaliam a participação no público? {#when-do-action-based-campaigns-evaluate-audience-membership}

A Braze avalia a participação no público quando processa o evento-gatilho, antes do envio da mensagem. Por padrão, a Braze verifica se o usuário corresponde ao público-alvo no momento do enfileiramento. Se a Campaign tiver um atraso, você pode selecionar **Reavaliar participação no Segment or segmento no momento do envio** para verificar os critérios de público novamente imediatamente antes do envio — por exemplo, quando um usuário pode realizar a ação-gatilho e depois sair do público antes que o envio seja concluído.

Para saber mais, consulte [Avaliação dos critérios de público](#audience-criteria-evaluation).