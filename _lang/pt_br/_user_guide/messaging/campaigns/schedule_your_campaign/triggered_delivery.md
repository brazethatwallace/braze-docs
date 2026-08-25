---
nav_title: Entrega baseada em ação
article_title: Entrega baseada em ação
page_order: 1
page_type: reference
description: "Este artigo de referência descreve como disparar campanhas para envio após um usuário concluir um determinado evento."
tool: Campaigns

---

# Entrega baseada em ação {#action-based-delivery}

> Campanhas de entrega baseada em ação ou campanhas disparadas por eventos são muito eficazes para mensagens transacionais ou baseadas em conquistas. Em vez de enviar sua campanha em dias específicos, você pode dispará-las para envio após um usuário concluir um determinado evento.

## Configurando uma campanha disparada {#setting-up-a-triggered-campaign}

### Etapa 1: Selecionar um evento-gatilho {#step-1-select-a-trigger-event}

Selecione um evento-gatilho. Ele pode incluir qualquer um dos seguintes:
- Fazer um pedido
- Iniciar uma sessão
- Realizar um evento personalizado
- Realizar o evento de conversão primária da campanha
- Adicionar um endereço de e-mail ao perfil de usuário
- Alterar o valor de um atributo personalizado
- Atualizar o status de inscrição
- Atualizar o status de um grupo de inscrições
- Interagir com outras campanhas
    - Visualizar mensagem no app
    - Clicar em mensagem no app
    - Clicar em botões de mensagem no app
    - Clicar em e-mail
    - Clicar em alias no e-mail
    - Clicar em alias em qualquer Campaign ou etapa do Canvas
    - Abrir e-mail
    - Abrir e-mail (aberturas por máquina)
    - Abrir e-mail (outras aberturas)
    - Abrir diretamente notificação por push
    - Clicar em botão de notificação por push
    - Clicar em página de story por push
    - Realizar evento de conversão
    - Receber e-mail
    - Receber SMS
    - Clicar em link encurtado de SMS
    - Receber notificação por push
    - Receber webhook
    - Ser inscrito em um grupo de controle
    - Visualizar cartão de conteúdo
    - Clicar em cartão de conteúdo
    - Dispensar cartão de conteúdo
- Entrar em um local
- Realizar o evento de exceção de outra campanha
- Interagir com uma etapa do Canvas
- Disparar uma geofence
- Enviar uma mensagem SMS de entrada
- Enviar uma mensagem WhatsApp de entrada

Você também pode filtrar ainda mais os eventos-gatilho por meio das [propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) da Braze, permitindo propriedades de eventos configuráveis para eventos personalizados e compras in-app. Esse recurso permite refinar ainda mais quais usuários recebem uma mensagem com base nos atributos específicos do evento personalizado, possibilitando uma personalização maior das campanhas e uma coleta de dados mais sofisticada.

Por exemplo, digamos que temos uma campanha com um evento personalizado de carrinho abandonado, que é adicionalmente direcionada pelo filtro de propriedade "valor do carrinho". Essa campanha alcançará apenas usuários que deixaram entre US$ 100 e US$ 200 em produtos nos carrinhos.

![Campanha de carrinho abandonado filtrada por uma propriedade de evento personalizado para valor do carrinho entre US$ 100 e US$ 200.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
O evento-gatilho "iniciar sessão" pode ser a primeira abertura do app pelo usuário se o Segment da sua campanha se aplicar a novos usuários (por exemplo, se seu Segment consiste em usuários sem sessões).
{% endalert %}

Tenha em mente que você ainda pode enviar uma campanha disparada para um Segment específico de usuários, de modo que usuários que não fazem parte do Segment não receberão a campanha, mesmo que completem o evento-gatilho.

Quanto ao evento-gatilho de quando um usuário adiciona um endereço de e-mail ao perfil, as seguintes regras se aplicam:

- O evento-gatilho será disparado após a atualização do atributo do perfil de usuário. Isso significa que a avaliação dos Segments e filtros da campanha acontecerá após as atualizações de atributos. Isso é vantajoso porque permite configurar filtros como "endereço de e-mail corresponde a gmail.com" para criar uma campanha disparada que envia apenas para usuários do Gmail e é disparada assim que eles adicionam seu endereço de e-mail.
- O evento-gatilho será disparado quando um endereço de e-mail for adicionado a um perfil de usuário. Se você tiver múltiplos perfis de usuário criados com o mesmo endereço de e-mail, a campanha poderá ser disparada várias vezes, uma para cada perfil de usuário.

Além disso, In-App Messages disparadas ainda seguem as regras de entrega de mensagens no app e aparecem no início de uma sessão do app.

![Cronograma de entrega de campanha baseada em ação mostrando as opções de configuração de eventos-gatilho.]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### Etapa 2: Selecionar a duração da postergação {#step-2-select-delay-length}

Selecione quanto tempo aguardar antes de enviar a campanha após o cumprimento dos critérios de gatilho. Se a duração da postergação escolhida for maior que a duração do envio da mensagem, nenhum usuário receberá a campanha.

Campanhas de mensagens no app podem postergar a entrega após o evento-gatilho em até duas horas (7.200 segundos). As opções de postergação são **Imediatamente** e **Após uma postergação**. Para uma espera mais longa, adicione uma etapa de [Postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) antes de uma etapa de mensagem no app em um Canvas.

{% alert important %}
A Braze usa o timestamp enviado com o evento personalizado para avaliar a postergação de uma campanha baseada em ação. Se esse timestamp estiver retroativo, a Braze poderá tratar a postergação como já decorrida e enviar a mensagem imediatamente ou antes do esperado. Para evitar problemas de entrega, envie o timestamp do evento personalizado com a hora atual.
{% endalert %}

Além disso, os usuários que completarem o evento-gatilho após o lançamento da campanha serão os primeiros a começar a receber a mensagem depois que a postergação tiver passado. Usuários que completaram o evento-gatilho antes do lançamento da campanha não se qualificarão para recebê-la.

![Captura de tela relacionada à etapa 2: selecionar a duração da postergação.]({% image_buster /assets/img_archive/schedule_triggered22.png %})

Você também pode optar por enviar a campanha em um dia específico da semana (escolhendo "no próximo" e selecionando um dia) ou em um número específico de dias (selecionando "em") no futuro. Alternativamente, você pode enviar sua mensagem usando o recurso [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) em vez de selecionar manualmente um horário de entrega.

![Você também pode optar por enviar a campanha em um dia específico da semana (escolhendo "no próximo" e selecionando um dia) ou em um número específico de dias (selecionando "em") no futuro. Alternativamente, você pode enviar sua mensagem usando o recurso Intelligent Timing em vez de selecionar manualmente um horário de entrega.]({% image_buster /assets/img_archive/schedule_triggered7.png %})
![Você também pode optar por enviar a campanha em um dia específico da semana (escolhendo "no próximo" e selecionando um dia) ou em um número específico de dias (selecionando "em") no futuro. Alternativamente, você pode enviar sua mensagem usando o recurso Intelligent Timing em vez de selecionar manualmente um horário de entrega.]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### Etapa 3: Selecionar eventos de exceção {#step-3-select-exception-events}

Selecione um evento de exceção que desqualificará os usuários de receber esta campanha. Você só pode fazer isso se sua mensagem disparada for enviada após uma postergação. [Eventos de exceção]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) podem ser fazer uma compra, iniciar uma sessão, realizar um dos [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) designados da campanha ou realizar um evento personalizado. Se um usuário completar o evento-gatilho, mas depois completar o evento de exceção antes que a mensagem seja enviada (devido à postergação), ele não receberá a campanha. Usuários que não receberem a campanha por causa do evento de exceção serão automaticamente elegíveis para recebê-la no futuro, na próxima vez que completarem o evento-gatilho, mesmo que você não tenha optado por tornar os usuários [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

![Selecione um evento de exceção que desqualificará os usuários de receber esta campanha. Você só pode fazer isso se sua mensagem disparada for enviada após uma postergação. Eventos de exceção podem ser fazer uma compra, iniciar uma sessão, realizar um dos eventos de conversão designados da campanha ou realizar um evento personalizado.]({% image_buster /assets/img_archive/schedule_triggered32.png %})

Você pode ler mais sobre como utilizar eventos de exceção na nossa seção de [casos de uso]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#use-cases).

> Se você enviar uma campanha com um evento-gatilho que corresponda ao evento de exceção, a Braze cancelará a campanha e reagendará automaticamente uma nova campanha com base no horário de entrega da mensagem do evento de exceção. Por exemplo, se o primeiro evento-gatilho começa em cinco minutos e o evento de exceção começa em 10 minutos, você dependeria dos 10 minutos do evento de exceção como o horário oficial de entrega da mensagem da campanha.

{% alert note %}
Você não pode fazer "início de sessão" ser tanto o evento-gatilho quanto o evento de exceção de uma campanha. No entanto, você sempre tem a opção de selecionar qualquer outro evento personalizado fora dessa opção.
{% endalert %}

### Etapa 4: Definir a duração {#step-4-assign-duration}

Defina a duração da campanha especificando um horário de início e um horário de término opcional.

![Captura de tela relacionada à etapa 4: definir a duração.]({% image_buster /assets/img_archive/schedule_triggered43.png %})

Se um usuário completar um evento-gatilho durante o período especificado, mas se qualificar para a mensagem fora do período devido a uma postergação programada, ele não receberá a campanha. Portanto, se você definir uma postergação maior que o período da mensagem, nenhum usuário receberá sua campanha. Além disso, você pode optar por enviar a mensagem no [fuso local]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) dos usuários.

### Etapa 5: Selecionar o período {#step-5-select-time-frame}

Selecione se o usuário receberá a campanha durante uma parte específica do dia. Se você definir um período para a mensagem e o usuário completar o evento-gatilho fora desse período, ou se a postergação da mensagem fizer com que ele perca o período, por padrão o usuário não receberá sua mensagem.

![Selecione se o usuário receberá a campanha durante uma parte específica do dia. Se você definir um período para a mensagem e o usuário completar o evento-gatilho fora desse período, ou se a postergação da mensagem fizer com que ele perca o período, por padrão o usuário não receberá sua mensagem.]({% image_buster /assets/img_archive/schedule_triggered5.png %})

No caso de o usuário completar o evento-gatilho dentro do período, mas a postergação da mensagem fizer com que ele fique fora do período, você pode marcar a caixa a seguir para que esses usuários ainda recebam a campanha.

![Captura de tela relacionada à etapa 5: selecionar o período.]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

Se um usuário não receber a mensagem porque perdeu o período, ele ainda será qualificado para recebê-la na próxima vez que completar o evento-gatilho, mesmo que você não tenha optado por tornar os usuários [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility). Se você optar por tornar os usuários reelegíveis, eles poderão receber a campanha cada vez que completarem o evento-gatilho, desde que se qualifiquem dentro do período especificado.

Se você também tiver definido uma duração para a campanha, o usuário deverá se qualificar tanto dentro da duração quanto da parte específica do dia para receber a mensagem.

### Etapa 6: Determinar a reelegibilidade {#step-6-determine-re-eligibility}

Determine se os usuários podem se tornar [reelegíveis]({% image_buster /assets/img_archive/ReEligible.png %}) para a campanha. Se você permitir que os usuários se tornem reelegíveis, poderá especificar uma postergação antes que o usuário possa receber a campanha novamente. Isso impedirá que suas campanhas disparadas se tornem "spammy".

![Captura de tela relacionada à etapa 6: determinar a reelegibilidade.]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## Casos de uso {#use-cases}

Campanhas disparadas são muito eficazes para mensagens transacionais ou baseadas em conquistas.

Campanhas transacionais incluem mensagens enviadas após o usuário concluir uma compra ou adicionar um item ao carrinho. Este último caso é um ótimo exemplo de Campaign que se beneficiaria de um evento de exceção. Digamos que sua Campaign lembra os usuários de itens no carrinho que eles ainda não compraram. O evento de exceção, nesse caso, seria o usuário comprando os produtos do carrinho. Para campanhas baseadas em conquistas, você pode enviar uma mensagem 5 minutos após o usuário concluir uma conversão ou passar de fase em um jogo.

Além disso, ao criar campanhas de boas-vindas, você pode disparar mensagens para envio após o usuário se registrar ou configurar uma conta. Escalonar mensagens para serem enviadas em dias diferentes após o registro permite criar um processo de integração completo.

## Perguntas frequentes {#frequently-asked-questions}

### Qual é o atraso máximo após um disparo para campanhas de mensagem no app? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

Campanhas de mensagem no app podem atrasar a entrega após o evento-gatilho em até duas horas (7.200 segundos). As opções de atraso são **Imediatamente** e **Após um atraso**. Para uma espera mais longa, adicione uma etapa de [postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) antes de uma etapa de mensagem no app em um Canvas.

### Por que um usuário não recebeu minha Campaign disparada? {#why-did-a-user-not-receive-my-triggered-campaign}

Qualquer uma dessas situações impedirá que um usuário que completou o evento-gatilho receba a Campaign:

- O usuário completou o evento de exceção antes que o tempo de atraso tivesse se esgotado completamente.
- A [lógica `abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) do Liquid foi usada e a mensagem foi interrompida com base na lógica ou nas regras de `abort_message`.
- O tempo de atraso fez com que o usuário se tornasse qualificado para receber a Campaign após a duração ter encerrado.
- O tempo de atraso fez com que o usuário se tornasse qualificado para receber a Campaign fora da porção especificada do dia.
- O usuário já recebeu a Campaign (incluindo atribuição por meio de identificadores de canal compartilhados — por exemplo, se compartilhou um e-mail com alguém que recebeu, abriu ou clicou nele), e os usuários não se tornam reelegíveis.
- Embora os usuários sejam reelegíveis para receber a Campaign, eles só podem redispará-la após um determinado período de tempo, e esse período ainda não se esgotou.

[Segmentar]({{site.baseurl}}/user_guide/audience/segments) uma Campaign disparada com base em dados do usuário registrados no momento do evento pode causar uma [condição de corrida]({{site.baseurl}}/help/best_practices/race_conditions#race-conditions). Isso acontece quando o atributo do usuário no qual a Campaign é segmentada é alterado, mas a alteração ainda não foi processada para o usuário quando a Campaign é enviada. Como as campanhas verificam a associação ao Segment na entrada, isso pode fazer com que o usuário não receba a Campaign.

Por exemplo, imagine que você deseja enviar uma Campaign disparada por evento para usuários masculinos que acabaram de se registrar. Quando o usuário se registra, você grava um evento personalizado `registration` e simultaneamente define o atributo `gender` do usuário. O evento pode disparar a Campaign antes que a Braze tenha processado o gênero do usuário, impedindo-o de receber a Campaign.

Como prática recomendada, garanta que o atributo no qual a Campaign é segmentada seja enviado aos servidores da Braze antes do evento. Se isso não for possível, a melhor maneira de garantir a entrega é usar [propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) para anexar as propriedades relevantes do usuário ao evento e aplicar um filtro de propriedade para a propriedade específica do evento em vez de um filtro de segmentação. No nosso exemplo, você adicionaria uma propriedade `gender` ao evento personalizado `registration` para que a Braze tenha garantidamente os dados necessários quando sua Campaign for disparada.

Além disso, se uma Campaign é baseada em ação e tem um atraso, você pode marcar a opção **Reavaliar associação ao Segment no momento do envio** para garantir que os usuários ainda façam parte do público-alvo quando a mensagem for enviada.

#### Avaliação dos critérios de público {#audience-criteria-evaluation}

Para campanhas que envolvem um atraso antes do envio (incluindo limite de frequência, fuso local, Intelligent Timing ou um cronograma de disparo), quando o Segment é reavaliado depende do tipo da Campaign e das configurações.

Em campanhas baseadas em ação com atraso, se você selecionar **Reavaliar associação ao Segment no momento do envio**, os usuários serão reavaliados antes que a mensagem seja enviada, de modo que apenas os usuários que ainda atendem aos critérios do Segment no momento do envio recebam a mensagem.

Se sua Campaign for disparada por um evento personalizado específico e você selecionar um Segment como público, os usuários devem realizar o mesmo evento personalizado para serem incluídos no Segment. Isso significa que os usuários precisam fazer parte do público antes que uma Campaign baseada em ação possa ser disparada. O fluxo geral de uma Campaign disparada é o seguinte:

1. **Entrar no público:** Quando um usuário realiza o evento personalizado, ele é adicionado ao público-alvo da Campaign.
2. **Disparar o e-mail:** Um usuário deve realizar o evento personalizado novamente para disparar o e-mail, pois ele precisa fazer parte do público antes que o e-mail possa ser enviado.

Recomendamos alterar o público-alvo para incluir todos os usuários ou verificar se os usuários que devem realizar o evento já fazem parte do público da Campaign para que a mensagem seja disparada.

![Captura de tela relacionada à avaliação de critérios de público.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### Solução de problemas com eventos personalizados {#troubleshooting-custom-events}

Primeiro, confirme que o evento personalizado está sendo enviado para a Braze. Acesse **Analytics** > **Relatório de eventos personalizados** e selecione o respectivo evento personalizado e o intervalo de datas. Se o evento não aparecer, confirme que ele está configurado corretamente e que o usuário realizou a ação correta.

Se o evento personalizado aparecer, faça a seguinte solução de problemas:

- Verifique o download do perfil do usuário para confirmar que ele disparou o evento e quando o fez. Se o evento foi disparado, compare o timestamp de quando o evento foi disparado com o horário em que a Campaign entrou no ar. O evento pode ter sido disparado antes de a Campaign estar ativa.
- Revise os changelogs da Campaign e de quaisquer Segments usados no direcionamento para determinar se o usuário estava no Segment quando o evento personalizado foi disparado. Se não estava no Segment, ele não teria recebido a Campaign.
- Verifique se o usuário foi inserido em um grupo de controle por meio de segmentação e, consequentemente, impedido de receber a Campaign.
- Se houver um atraso agendado, verifique se o evento personalizado do usuário foi disparado antes do atraso. Se o evento foi disparado antes do atraso, ele não teria recebido a Campaign.

{% alert note %}
Mensagens no app só podem ser disparadas por eventos enviados pelo SDK, não pela REST API.
{% endalert %}

### Quando as campanhas baseadas em ação avaliam a associação ao público? {#when-do-action-based-campaigns-evaluate-audience-membership}

A Braze avalia a associação ao público quando processa o evento-gatilho, antes de a mensagem ser enviada. Por padrão, a Braze verifica se o usuário corresponde ao público-alvo no momento do enfileiramento. Se a Campaign tiver um atraso, você pode selecionar **Reavaliar associação ao Segment no momento do envio** para verificar os critérios de público novamente imediatamente antes do envio — por exemplo, quando um usuário pode realizar a ação-gatilho e depois sair do público antes que o envio seja concluído.

Para saber mais, consulte [Avaliação dos critérios de público](#audience-criteria-evaluation).