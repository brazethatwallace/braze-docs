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

### Etapa 1: Selecione um evento de gatilho {#step-1-select-a-trigger-event}

Selecione um evento de gatilho. Ele pode incluir qualquer um dos seguintes:
- Realizar uma compra
- Iniciar uma sessão
- Realizar um evento personalizado
- Realizar o evento de conversão primária da campanha
- Adicionar um endereço de e-mail a um perfil de usuário
- Alterar o valor de um atributo personalizado
- Atualizar um status de inscrição
- Atualizar o status de um grupo de inscrições
- Interagir com outras campanhas
    - Visualizar mensagem no app
    - Clicar em mensagem no app
    - Clicar em botões de mensagem no app
    - Clicar em e-mail
    - Clicar em alias no e-mail
    - Clicar em alias em qualquer campanha ou etapa do Canvas
    - Abrir e-mail
    - Abrir e-mail (aberturas por máquina)
    - Abrir e-mail (outras aberturas)
    - Abrir diretamente a notificação por push
    - Clicar no botão da notificação por push
    - Clicar na página da story por push
    - Realizar evento de conversão
    - Receber e-mail
    - Receber SMS
    - Clicar em link encurtado de SMS
    - Receber notificação por push
    - Receber webhook
    - Ser inscrito no grupo de controle
    - Visualizar cartão de conteúdo
    - Clicar em cartão de conteúdo
    - Dispensar cartão de conteúdo
- Entrar em um local
- Realizar o evento de exceção de outra campanha
- Interagir com uma etapa do Canvas
- Disparar uma geofence
- Enviar uma mensagem SMS de entrada
- Enviar uma mensagem WhatsApp de entrada

Você também pode filtrar ainda mais os eventos de gatilho por meio das [propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) da Braze, permitindo propriedades de eventos customizáveis para eventos personalizados e compras no app. Esse recurso permite refinar ainda mais quais usuários recebem uma mensagem com base nos atributos específicos do evento personalizado, possibilitando maior personalização de campanhas e coleta de dados mais sofisticada.

Por exemplo, digamos que temos uma campanha com um evento personalizado de carrinho abandonado que é ainda mais direcionada pelo filtro de propriedade "valor do carrinho". Essa campanha alcançará apenas usuários que deixaram entre $100 e $200 em produtos nos seus carrinhos.

![Campanha de carrinho abandonado filtrada por uma propriedade de evento personalizado para valor do carrinho entre $100 e $200.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
O evento de gatilho "iniciar sessão" pode ser a primeira abertura do app pelo usuário se o segmento da sua campanha se aplicar a novos usuários (por exemplo, se o segmento consiste em usuários sem sessões).
{% endalert %}

Lembre-se de que você ainda pode enviar uma campanha disparada para um segmento específico de usuários. Portanto, usuários que não fazem parte do segmento não receberão a campanha, mesmo que completem o evento de gatilho.

Com relação ao evento de gatilho para quando um usuário adiciona um endereço de e-mail ao seu perfil, as seguintes regras se aplicam:

- O evento de gatilho será disparado após a atualização do atributo do perfil de usuário. Isso significa que a avaliação dos segmentos e filtros da campanha acontecerá após qualquer atualização de atributo. Isso é benéfico porque permite configurar filtros como "endereço de e-mail corresponde a gmail.com" para criar uma campanha disparada que envia apenas para usuários do Gmail e é disparada assim que eles adicionam seu endereço de e-mail.
- O evento de gatilho será disparado quando um endereço de e-mail for adicionado a um perfil de usuário. Se você tiver múltiplos perfis de usuário criados com o mesmo endereço de e-mail, a campanha pode ser disparada várias vezes, uma para cada perfil de usuário.

Além disso, mensagens no app disparadas ainda seguem as regras de entrega de mensagens no app e aparecem no início de uma sessão do app.

![Programação de entrega de campanha baseada em ação mostrando opções de configuração de evento de gatilho.]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### Etapa 2: Selecione a duração da postergação {#step-2-select-delay-length}

Selecione quanto tempo esperar antes de enviar a campanha após os critérios de gatilho serem atendidos. Se a duração da postergação escolhida for maior que a duração do envio da mensagem, nenhum usuário receberá a campanha.

{% alert important %}
A Braze usa o timestamp enviado com o evento personalizado para avaliar a postergação de uma campanha baseada em ação. Se esse timestamp estiver retroativo, a Braze pode tratar a postergação como já decorrida e enviar a mensagem imediatamente ou antes do esperado. Para evitar problemas no timing de entrega, envie o timestamp do evento personalizado com a hora atual.
{% endalert %}

Além disso, os usuários que completarem o evento de gatilho após o lançamento da campanha serão os primeiros a começar a receber a mensagem após a postergação ter passado. Usuários que completaram o evento de gatilho antes do lançamento da campanha não serão elegíveis para recebê-la.

![Captura de tela relacionada à etapa 2: selecionar a duração da postergação.]({% image_buster /assets/img_archive/schedule_triggered22.png %})

Você também pode optar por enviar a campanha em um dia específico da semana (escolhendo "no próximo" e selecionando um dia) ou um número específico de dias (selecionando "em") no futuro. Alternativamente, você pode escolher enviar sua mensagem usando o recurso [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) em vez de selecionar manualmente um horário de entrega.

![Você também pode optar por enviar a campanha em um dia específico da semana (escolhendo "no próximo" e selecionando um dia) ou um número específico de dias (selecionando "em") no futuro. Alternativamente, você pode escolher enviar sua mensagem usando o recurso Intelligent Timing em vez de selecionar manualmente um horário de entrega.]({% image_buster /assets/img_archive/schedule_triggered7.png %})
![Você também pode optar por enviar a campanha em um dia específico da semana (escolhendo "no próximo" e selecionando um dia) ou um número específico de dias (selecionando "em") no futuro. Alternativamente, você pode escolher enviar sua mensagem usando o recurso Intelligent Timing em vez de selecionar manualmente um horário de entrega.]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### Etapa 3: Selecione eventos de exceção {#step-3-select-exception-events}

Selecione um evento de exceção que desqualificará os usuários de receber esta campanha. Você só pode fazer isso se sua mensagem disparada for enviada após uma postergação. [Eventos de exceção]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) podem ser realizar uma compra, iniciar uma sessão, realizar um dos [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) designados da campanha ou realizar um evento personalizado. Se um usuário completar o evento de gatilho, mas depois completar o evento de exceção antes do envio da mensagem devido à postergação, ele não receberá a campanha. Usuários que não receberem a campanha devido ao evento de exceção serão automaticamente elegíveis para recebê-la no futuro, na próxima vez que completarem o evento de gatilho, mesmo que você não tenha optado por tornar os usuários [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

![Selecione um evento de exceção que desqualificará os usuários de receber esta campanha. Você só pode fazer isso se sua mensagem disparada for enviada após uma postergação. Eventos de exceção podem ser realizar uma compra, iniciar uma sessão, realizar um dos eventos de conversão designados da campanha ou realizar um evento personalizado. Se um usuário completar o evento de gatilho, mas depois completar o evento de exceção antes do envio da mensagem devido à postergação, ele não receberá a campanha. Usuários que não receberem a campanha devido ao evento de exceção serão automaticamente elegíveis para recebê-la no futuro, na próxima vez que completarem o evento de gatilho, mesmo que você não tenha optado por tornar os usuários reelegíveis.]({% image_buster /assets/img_archive/schedule_triggered32.png %})

Você pode ler mais sobre como utilizar eventos de exceção na nossa seção sobre [casos de uso]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#use-cases).

> Se você enviar uma campanha com um evento de gatilho que corresponda ao evento de exceção, a Braze cancelará a campanha e reagendará automaticamente uma nova campanha com base no horário de entrega da mensagem do evento de exceção. Por exemplo, se o primeiro evento de gatilho começa em cinco minutos e o evento de exceção começa em 10 minutos, o horário de entrega oficial da campanha será os 10 minutos do evento de exceção.

{% alert note %}
Você não pode definir "início de sessão" como evento de gatilho e evento de exceção ao mesmo tempo para uma campanha. No entanto, você sempre pode selecionar qualquer outro evento personalizado além dessa opção.
{% endalert %}

### Etapa 4: Atribua a duração {#step-4-assign-duration}

Atribua a duração da campanha especificando um horário de início e um horário de término opcional.

![Captura de tela relacionada à etapa 4: atribuir a duração.]({% image_buster /assets/img_archive/schedule_triggered43.png %})

Se um usuário completar um evento de gatilho durante o período especificado, mas se qualificar para a mensagem fora desse período devido a uma postergação programada, ele não receberá a campanha. Portanto, se você definir uma postergação maior que o período da mensagem, nenhum usuário receberá sua campanha. Além disso, você pode optar por enviar a mensagem nos [fusos horários locais]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) dos usuários.

### Etapa 5: Selecione o período do dia {#step-5-select-time-frame}

Selecione se o usuário receberá a campanha durante uma parte específica do dia. Se você definir um período para a mensagem e o usuário completar o evento de gatilho fora desse período, ou se a postergação da mensagem fizer com que ele perca o período, por padrão o usuário não receberá sua mensagem.

![Selecione se o usuário receberá a campanha durante uma parte específica do dia. Se você definir um período para a mensagem e o usuário completar o evento de gatilho fora desse período, ou se a postergação da mensagem fizer com que ele perca o período, por padrão o usuário não receberá sua mensagem.]({% image_buster /assets/img_archive/schedule_triggered5.png %})

No caso em que um usuário completar o evento de gatilho dentro do período, mas a postergação da mensagem fizer com que ele fique fora do período, você pode marcar a seguinte caixa para que esses usuários ainda recebam a campanha.

![Captura de tela relacionada à etapa 5: selecionar o período do dia.]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

Se um usuário não receber a mensagem porque perdeu o período, ele ainda será elegível para recebê-la na próxima vez que completar o evento de gatilho, mesmo que você não tenha optado por tornar os usuários [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility). Se você optar por tornar os usuários reelegíveis, eles poderão receber a campanha cada vez que completarem o evento de gatilho, desde que se qualifiquem durante o período especificado.

Se você também tiver atribuído uma duração à campanha, o usuário deve se qualificar tanto dentro da duração quanto na parte específica do dia para receber a mensagem.

### Etapa 6: Determine a reelegibilidade {#step-6-determine-re-eligibility}

Determine se os usuários podem se tornar [reelegíveis]({% image_buster /assets/img_archive/ReEligible.png %}) para a campanha. Se você permitir que os usuários se tornem reelegíveis, poderá especificar uma postergação antes que o usuário possa receber a campanha novamente. Isso evitará que suas campanhas disparadas se tornem "spam".

![Captura de tela relacionada à etapa 6: determinar a reelegibilidade.]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## Casos de uso {#use-cases}

Campanhas disparadas são muito eficazes para mensagens transacionais ou baseadas em conquistas.

Campanhas transacionais incluem mensagens enviadas após o usuário concluir uma compra ou adicionar um item ao carrinho. O último caso é um ótimo exemplo de campanha que se beneficiaria de um evento de exceção. Digamos que sua campanha lembra os usuários de itens no carrinho que eles não compraram. O evento de exceção, nesse caso, seria o usuário comprar os produtos do carrinho. Para campanhas baseadas em conquistas, você pode enviar uma mensagem 5 minutos após o usuário concluir uma conversão ou passar de fase em um jogo.

Além disso, ao criar campanhas de boas-vindas, você pode disparar mensagens para envio após o usuário se registrar ou configurar uma conta. Escalonar mensagens para serem enviadas em diferentes dias após o registro permite criar um processo de integração completo.

## Perguntas frequentes {#frequently-asked-questions}

### Por que um usuário não recebeu minha campanha disparada? {#why-did-a-user-not-receive-my-triggered-campaign}

Qualquer uma dessas situações impedirá que um usuário que completou o evento de gatilho receba a campanha:

- O usuário completou o evento de exceção antes que a postergação tivesse decorrido completamente.
- A [lógica `abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) do Liquid foi usada e a mensagem foi abortada com base na lógica ou regras de `abort_message`.
- A postergação fez com que o usuário se qualificasse para receber a campanha após o término da duração.
- A postergação fez com que o usuário se qualificasse para receber a campanha fora do período especificado do dia.
- O usuário já recebeu a campanha (incluindo atribuição por meio de identificadores de canal compartilhados — por exemplo, se ele compartilha um e-mail com alguém que recebeu, abriu ou clicou nele), e os usuários não se tornam reelegíveis.
- Embora os usuários sejam reelegíveis para receber a campanha, eles só podem redispará-la após um determinado período, e esse período ainda não decorreu.

[Segmentar]({{site.baseurl}}/user_guide/audience/segments) uma campanha disparada com base em dados de usuários registrados no momento do evento pode causar uma [condição de corrida]({{site.baseurl}}/help/best_practices/race_conditions#race-conditions). Isso acontece quando o atributo do usuário no qual a campanha é segmentada é alterado, mas a alteração ainda não foi processada para o usuário quando a campanha é enviada. Como as campanhas verificam a associação ao segmento na entrada, isso pode fazer com que o usuário não receba a campanha.

Por exemplo, imagine que você deseja enviar uma campanha disparada por evento para usuários masculinos que acabaram de se registrar. Quando o usuário se registra, você registra um evento personalizado `registration` e simultaneamente define o atributo `gender` do usuário. O evento pode disparar a campanha antes que a Braze tenha processado o gênero do usuário, impedindo-o de receber a campanha.

Como prática recomendada, certifique-se de que o atributo no qual a campanha é segmentada seja enviado aos servidores da Braze antes do evento. Se isso não for possível, a melhor maneira de garantir a entrega é usar [propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) para anexar as propriedades relevantes do usuário ao evento e aplicar um filtro de propriedade para a propriedade específica do evento em vez de um filtro de segmentação. No nosso exemplo, você adicionaria uma propriedade `gender` ao evento personalizado `registration` para que a Braze tenha garantidamente os dados necessários quando sua campanha for disparada.

Além disso, se uma campanha for baseada em ação e tiver uma postergação, você pode marcar a opção **Reavaliar associação ao segmento no momento do envio** para garantir que os usuários ainda façam parte do público-alvo quando a mensagem for enviada.

#### Avaliação dos critérios de público {#audience-criteria-evaluation}

Para campanhas que envolvem uma postergação antes do envio (incluindo limite de frequência, fuso horário local, Intelligent Timing ou um agendamento de gatilho), quando o segmento é reavaliado depende do tipo e das configurações da campanha.

Em campanhas baseadas em ação com postergação, se você selecionar **Reavaliar associação ao segmento no momento do envio**, os usuários serão reavaliados antes do envio da mensagem, de modo que apenas os usuários que ainda atendem aos critérios do segmento no momento do envio receberão a mensagem.

Se sua campanha for disparada por um evento personalizado específico e você selecionar um segmento como público, os usuários devem realizar o mesmo evento personalizado para serem incluídos no segmento. Isso significa que os usuários precisam fazer parte do público antes que uma campanha baseada em ação possa ser disparada. O fluxo geral de uma campanha disparada é o seguinte:

1. **Entrar no público:** Quando um usuário realiza o evento personalizado, ele é adicionado ao público-alvo da campanha.
2. **Disparar o e-mail:** O usuário deve realizar o evento personalizado novamente para disparar o e-mail, pois precisa fazer parte do público antes que o e-mail possa ser enviado.

Recomendamos alterar o público-alvo para incluir todos os usuários ou verificar se os usuários que devem realizar o evento já fazem parte do público da campanha para que a mensagem seja disparada.

![Captura de tela relacionada à avaliação dos critérios de público.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### Solução de problemas com eventos personalizados {#troubleshooting-custom-events}

Primeiro, confirme que o evento personalizado está sendo enviado para a Braze. Acesse **Analytics** > **Relatório de eventos personalizados** e selecione o respectivo evento personalizado e o intervalo de datas. Se o evento não aparecer, confirme que ele está configurado corretamente e que o usuário realizou a ação correta.

Se o evento personalizado aparecer, investigue mais fazendo o seguinte:

- Verifique o download do perfil do usuário para confirmar que ele disparou o evento e quando o fez. Se o evento foi disparado, compare o timestamp de quando o evento foi disparado com o horário em que a campanha entrou no ar. O evento pode ter sido disparado antes do lançamento da campanha.
- Revise os changelogs da campanha e de quaisquer segmentos usados no direcionamento para determinar se o usuário estava no segmento quando seu evento personalizado foi disparado. Se ele não estava no segmento, não teria recebido a campanha.
- Verifique se o usuário foi inserido em um grupo de controle por meio da segmentação e, consequentemente, impedido de receber a campanha.
- Se houver uma postergação programada, verifique se o evento personalizado do usuário foi disparado antes da postergação. Se o evento foi disparado antes da postergação, ele não teria recebido a campanha.

{% alert note %}
Mensagens no app só podem ser disparadas por eventos enviados pelo SDK, não pela REST API.
{% endalert %}

### Quando as campanhas baseadas em ação avaliam a associação ao público? {#when-do-action-based-campaigns-evaluate-audience-membership}

A Braze avalia a associação ao público quando processa o evento de gatilho, antes do envio da mensagem. Por padrão, a Braze verifica se o usuário corresponde ao público-alvo no momento do enfileiramento. Se a campanha tiver uma postergação, você pode selecionar **Reavaliar associação ao segmento no momento do envio** para verificar os critérios de público novamente imediatamente antes do envio — por exemplo, quando um usuário pode realizar a ação de gatilho e depois sair do público antes que o envio seja concluído.

Para saber mais, consulte [Avaliação dos critérios de público](#audience-criteria-evaluation).