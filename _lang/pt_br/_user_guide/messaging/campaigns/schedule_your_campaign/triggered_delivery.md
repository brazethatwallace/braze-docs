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

Selecione um evento-gatilho. Os eventos são organizados por categoria e estão disponíveis dependendo do seu espaço de trabalho e dos canais ativados.

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

O grupo **eCommerce** também lista eventos recomendados de eCommerce, como **Perform Product Viewed Event**, **Perform Order Cancelled Event** e **Perform Order Refunded Event**. Essas opções usam **Perform Custom Event** com o nome do evento pré-preenchido.

Campaigns de mensagens no app suportam um conjunto menor de gatilhos: **Make Purchase**, **Place Order**, **Start Session**, **Perform Custom Event** e **Interact With Campaign**. Para Campaigns de mensagens no app, **Interact With Campaign** abrange apenas a abertura de um push de qualquer Campaign ou de uma Campaign específica. Não inclui a lista de interações de Campaign a seguir.

Para Campaigns que não são de mensagens no app, ao selecionar **Interact With Campaign**, **Interact With Step** ou **Interact with Landing Page**, escolha a interação que será o gatilho. Cada um desses gatilhos oferece suas próprias interações, e as interações disponíveis dependem dos seus canais ativados.

{% details Interações para Interact With Campaign %}

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

{% details Interações para Interact With Step %}

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

{% details Interações para Interact with Landing Page %}

- **Submit form**
- **Submit survey**

{% enddetails %}

Você também pode filtrar ainda mais os eventos-gatilho por meio das [propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) da Braze, permitindo propriedades de eventos personalizáveis para eventos personalizados e compras no app. Esse recurso permite definir com mais precisão quais usuários recebem uma mensagem com base nos atributos específicos do evento personalizado, possibilitando maior personalização de Campaigns e uma coleta de dados mais sofisticada.

Por exemplo, digamos que temos uma Campaign com um evento personalizado de carrinho abandonado que é ainda mais direcionada pelo filtro de propriedade "valor do carrinho". Essa Campaign alcança apenas usuários que deixaram entre $100 e $200 em produtos nos seus carrinhos.

![Campaign de carrinho abandonado filtrada por uma propriedade de evento personalizado para valor do carrinho entre $100 e $200.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
O evento-gatilho **Start Session** pode ser a primeira abertura do app do usuário se o Segment da sua Campaign se aplicar a novos usuários (por exemplo, se o seu Segment é composto por aqueles que não têm sessões).
{% endalert %}

Lembre-se de que você ainda pode enviar uma Campaign disparada para um Segment específico de usuários. Portanto, os usuários que não fazem parte do Segment não recebem a Campaign, mesmo que completem o evento-gatilho.

Em relação ao evento-gatilho de quando um usuário adiciona um endereço de e-mail ao seu perfil, as seguintes regras se aplicam:

- O evento-gatilho é disparado após a atualização do atributo do perfil de usuário. Isso significa que a avaliação dos Segments e filtros da Campaign acontece depois de qualquer atualização de atributo. Isso é vantajoso porque permite configurar filtros como "endereço de e-mail corresponde a gmail.com" para criar uma Campaign disparada que envia apenas para usuários do Gmail e é disparada assim que eles adicionam seu endereço de e-mail.
- O evento-gatilho é disparado quando um endereço de e-mail é adicionado a um perfil de usuário. Se você tiver múltiplos perfis de usuário criados com o mesmo endereço de e-mail, a Campaign pode ser disparada várias vezes, uma para cada perfil de usuário.

Além disso, mensagens no app disparadas ainda seguem as regras de entrega de mensagens no app e aparecem no início de uma sessão do app.

### Etapa 2: Selecione a duração da postergação {#step-2-select-delay-length}

Selecione quanto tempo esperar antes de enviar a Campaign após os critérios de gatilho serem atendidos. Se a duração da postergação escolhida for maior do que a duração de envio da mensagem, nenhum usuário receberá a Campaign.

Campaigns de mensagens no app podem postergar a entrega após o evento-gatilho por até duas horas (7.200 segundos). As opções de postergação são **Imediatamente** e **Após uma postergação**. Para uma espera mais longa, adicione uma etapa de [Postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) antes de uma etapa de mensagem no app em um Canvas.

{% alert important %}
A Braze usa o timestamp enviado com o evento personalizado para avaliar a postergação de uma Campaign baseada em ação. Se esse timestamp for retroativo, a Braze pode tratar a postergação como já tendo expirado e enviar a mensagem imediatamente ou antes do esperado. Para evitar problemas de timing na entrega, envie o timestamp do evento personalizado com a hora atual.
{% endalert %}

Além disso, os usuários que completam o evento-gatilho após o lançamento da sua Campaign são os primeiros a receber a mensagem depois que a postergação tiver passado. Os usuários que completaram o evento-gatilho antes do lançamento da Campaign não se qualificam para receber a Campaign.

Você também pode enviar a Campaign em um dia específico da semana selecionando **No próximo dia da semana**, ou um número definido de dias no futuro selecionando **Após um número de dias corridos**. Como alternativa, você pode enviar sua mensagem usando o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) em vez de selecionar manualmente um horário de entrega.

### Etapa 3: Selecione eventos de exceção {#step-3-select-exception-events}

Selecione um evento de exceção que desqualifica os usuários de receber esta Campaign. Você só pode fazer isso se sua mensagem disparada for enviada após uma postergação. [Eventos de exceção]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) podem ser realizar uma compra, iniciar uma sessão, realizar um dos [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) designados da Campaign ou realizar um evento personalizado.

Se um usuário completar o evento-gatilho, mas depois completar seu evento de exceção antes do envio da mensagem devido à postergação, ele não receberá a Campaign. Os usuários que não recebem a Campaign devido ao evento de exceção são automaticamente elegíveis para recebê-la no futuro, na próxima vez que completarem o evento-gatilho, mesmo que você não tenha optado por tornar os usuários [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

Para saber mais sobre o uso de eventos de exceção, consulte [Exemplos](#examples).

Se você enviar uma Campaign com um evento-gatilho que corresponda ao evento de exceção, a Braze cancela a Campaign e automaticamente reagenda uma nova Campaign com base no horário de entrega da mensagem do evento de exceção. Por exemplo, se o seu primeiro evento-gatilho começa em cinco minutos e o evento de exceção começa em 10 minutos, o horário de entrega da mensagem oficial da Campaign será os 10 minutos do evento de exceção.

{% alert note %}
Você não pode definir um "início de sessão" como evento-gatilho e evento de exceção ao mesmo tempo para uma Campaign. No entanto, você sempre pode selecionar qualquer outro evento personalizado fora dessa opção.
{% endalert %}

### Etapa 4: Atribua a duração {#step-4-assign-duration}

Atribua a duração da Campaign especificando um horário de início e um horário de término opcional.

Se um usuário completar um evento-gatilho durante o período especificado, mas se qualificar para a mensagem fora do período devido a uma postergação agendada, ele não receberá a Campaign. Portanto, se você definir uma postergação maior do que o período da mensagem, nenhum usuário receberá sua Campaign. Além disso, você pode optar por enviar a mensagem no [fuso local]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) dos usuários.

### Etapa 5: Selecione o período {#step-5-select-time-frame}

Selecione se o usuário receberá a Campaign durante uma parte específica do dia. Se você definir um período para a mensagem e o usuário completar o evento-gatilho fora desse período, ou se a postergação da mensagem fizer com que ele perca o período, por padrão o usuário não receberá sua mensagem.

No caso em que um usuário completa o evento-gatilho dentro do período, mas a postergação da mensagem faz com que ele saia do período, você pode selecionar a opção **Enviar no próximo horário disponível se o horário de entrega cair fora da parte especificada do dia** para que esses usuários ainda recebam a Campaign.

Se um usuário não receber a mensagem porque perdeu o período, ele ainda se qualifica para recebê-la na próxima vez que completar o evento-gatilho, mesmo que você não tenha optado por tornar os usuários [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility). Se você optar por tornar os usuários reelegíveis, eles poderão receber a Campaign cada vez que completarem o evento-gatilho, desde que se qualifiquem dentro do período especificado.

Se você também tiver atribuído à Campaign uma duração específica, o usuário deve se qualificar tanto dentro da duração quanto da parte específica do dia para receber a mensagem.

### Etapa 6: Determine a reelegibilidade {#step-6-determine-re-eligibility}

Determine se os usuários podem se tornar [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) para a Campaign. Se você permitir que os usuários se tornem reelegíveis, poderá especificar uma postergação antes que o usuário possa receber a Campaign novamente. Isso evita que suas Campaigns disparadas se tornem "spammy".

## Exemplos {#examples}

Campanhas disparadas são muito eficazes para mensagens transacionais ou baseadas em conquistas.

Campanhas transacionais incluem mensagens enviadas após o usuário concluir uma compra ou adicionar um item ao carrinho. Este último caso é um ótimo exemplo de Campaign que se beneficia de um evento de exceção. Digamos que sua Campaign lembra os usuários de itens no carrinho que eles ainda não compraram. O evento de exceção, nesse caso, é o usuário comprar os produtos do carrinho. Para campanhas baseadas em conquistas, você pode enviar uma mensagem cinco minutos após o usuário concluir uma conversão ou passar de fase em um jogo.

Além disso, ao criar campanhas de boas-vindas, você pode disparar mensagens para envio após o usuário se registrar ou configurar uma conta. Escalonar mensagens para serem enviadas em dias diferentes após o registro permite criar um processo de integração completo.

## Perguntas frequentes {#frequently-asked-questions}

### Qual é a postergação máxima após um disparo para campanhas de mensagem no app? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

Duas horas (7.200 segundos). Para ver as opções de postergação disponíveis e como definir uma espera mais longa, consulte [Etapa 2: Selecionar a duração da postergação](#step-2-select-delay-length).

### Por que um usuário não recebeu minha Campaign disparada? {#why-did-a-user-not-receive-my-triggered-campaign}

Qualquer uma dessas situações impede que um usuário que completou o evento-gatilho receba a Campaign:

- O usuário completou o evento de exceção antes de o tempo de postergação ter decorrido completamente.
- A [lógica de `abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) do Liquid foi usada e a mensagem foi interrompida com base na lógica ou nas regras de `abort_message`.
- A postergação fez com que o usuário se tornasse elegível para receber a Campaign após o término da duração.
- A postergação fez com que o usuário se tornasse elegível para receber a Campaign fora do período especificado do dia.
- O usuário já recebeu a Campaign (incluindo atribuição por meio de identificadores de canal compartilhados — por exemplo, se ele compartilha um e-mail com alguém que recebeu, abriu ou clicou nele) e os usuários não se tornam reelegíveis.
- Embora os usuários sejam reelegíveis para receber a Campaign, eles só podem redispará-la após um determinado período, e esse período ainda não decorreu.

A [segmentação]({{site.baseurl}}/user_guide/audience/segments) de uma Campaign disparada com base em dados de usuário registrados no momento do evento pode causar uma [condição de corrida]({{site.baseurl}}/help/best_practices/race_conditions#race-conditions). Isso acontece quando o atributo do usuário no qual a Campaign é segmentada é alterado, mas a alteração ainda não foi processada para o usuário quando a Campaign é enviada. Como as Campaigns verificam a associação ao Segment na entrada, isso pode fazer com que o usuário não receba a Campaign.

Por exemplo, imagine que você deseja enviar uma Campaign disparada por evento para usuários do sexo masculino que acabaram de se registrar. Quando o usuário se registra, você grava um evento personalizado `registration` e define simultaneamente o atributo `gender` do usuário. O evento pode disparar a Campaign antes que a Braze tenha processado o gênero do usuário, impedindo que ele receba a Campaign.

Como prática recomendada, assegure-se de que o atributo no qual a Campaign é segmentada seja enviado aos servidores da Braze antes do evento. Se isso não for possível, a melhor forma de garantir a entrega é usar [propriedades de evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) para anexar as propriedades relevantes do usuário ao evento e aplicar um filtro de propriedade para a propriedade específica do evento em vez de um filtro de segmentação. No nosso exemplo, adicione uma propriedade `gender` ao evento personalizado `registration` para que a Braze tenha garantidamente os dados necessários quando sua Campaign for disparada.

Além disso, se uma Campaign é baseada em ação e tem uma postergação, você pode marcar a opção **Re-evaluate segment membership at send-time** para garantir que os usuários ainda façam parte do público-alvo quando a mensagem for enviada.

#### Avaliação dos critérios de público {#audience-criteria-evaluation}

Para Campaigns que envolvem uma postergação antes do envio (incluindo limite de frequência, fuso local, Intelligent Timing ou um cronograma de disparo), quando o Segment é reavaliado depende do tipo e das configurações da Campaign.

Em Campaigns baseadas em ação com postergação, se você selecionar **Re-evaluate segment membership at send-time**, os usuários serão reavaliados antes de a mensagem ser enviada, de modo que apenas os usuários que ainda atendem aos critérios do Segment no momento do envio receberão a mensagem.

Se sua Campaign é disparada por um evento personalizado específico e você seleciona um Segment como público, os usuários devem realizar o mesmo evento personalizado para serem incluídos no Segment. Isso significa que os usuários precisam fazer parte do público antes que uma Campaign baseada em ação possa ser disparada. O fluxo de trabalho geral para uma Campaign disparada é o seguinte:

1. **Entrar no público:** quando um usuário realiza o evento personalizado, ele é adicionado ao público-alvo da Campaign.
2. **Disparar o e-mail:** o usuário deve realizar o evento personalizado novamente para disparar o e-mail, pois ele precisa fazer parte do público antes que o e-mail possa ser enviado.

Recomendamos alterar o público-alvo para incluir todos os usuários ou verificar se os usuários que devem realizar o evento já fazem parte do público da Campaign para que a mensagem seja disparada.

![Captura de tela relacionada à avaliação de critérios de público.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### Solução de problemas com eventos personalizados {#troubleshooting-custom-events}

Primeiro, confirme se o evento personalizado está sendo enviado para a Braze. Acesse **Analytics** > **Custom Events Report** e selecione o evento personalizado e o intervalo de datas correspondentes. Se o evento não aparecer, confirme se ele está configurado corretamente e se o usuário realizou a ação correta.

Se o evento personalizado aparecer, investigue mais fazendo o seguinte:

- Verifique o download do perfil do usuário para confirmar que ele disparou o evento e quando isso aconteceu. Se o evento foi disparado, compare o timestamp de quando o evento foi disparado com o horário em que a Campaign entrou em operação. O evento pode ter sido disparado antes de a Campaign entrar em operação.
- Revise os changelogs da Campaign e de quaisquer Segments usados no direcionamento para determinar se o usuário estava no Segment quando seu evento personalizado foi disparado. Se ele não estava no Segment, não teria recebido a Campaign.
- Verifique se o usuário foi inserido em um grupo de controle por meio de segmentação e, consequentemente, impedido de receber a Campaign.
- Se houver uma postergação agendada, verifique se o evento personalizado do usuário foi disparado antes da postergação. Se o evento foi disparado antes da postergação, ele não teria recebido a Campaign.

{% alert note %}
Mensagens no app só podem ser disparadas por eventos enviados pelo SDK, não pela REST API.
{% endalert %}

### Quando as Campaigns baseadas em ação avaliam a associação ao público? {#when-do-action-based-campaigns-evaluate-audience-membership}

A Braze avalia a associação ao público quando processa o evento-gatilho, antes de a mensagem ser enviada. Por padrão, a Braze verifica se o usuário corresponde ao público-alvo no momento do enfileiramento. Se a Campaign tiver uma postergação, você pode selecionar **Re-evaluate segment membership at send-time** para verificar os critérios de público novamente imediatamente antes do envio — por exemplo, quando um usuário pode realizar a ação-gatilho e depois sair do público antes de o envio ser concluído.

Para saber mais, consulte [Avaliação dos critérios de público](#audience-criteria-evaluation).