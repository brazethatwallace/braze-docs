---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 1.3
description: "Este artigo fornece uma visão geral do Intelligent Timing (anteriormente Entrega Inteligente) e como você pode aproveitar esse recurso em suas campanhas."
toc_headers: h2
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomintelligent-timing-stylefloatrightwidth120pxborder0-classnoimgborderintelligent-timing}

> Use o Intelligent Timing para enviar sua mensagem a cada usuário quando a Braze determinar o horário ideal de envio, que é quando o usuário tem mais chances de interagir (abrir ou clicar). Isso facilita garantir que você está enviando mensagens aos usuários no horário preferido deles, o que pode levar a um maior engajamento.

## Sobre o Intelligent Timing {#about-intelligent-timing}

A Braze calcula o horário ideal de envio com base em uma análise estatística das interações anteriores dos seus usuários com o app e com cada canal de envio de mensagens. Os seguintes dados de interação são usados:

- Horários de sessão
- Aberturas Diretas de push
- Aberturas por Influência de push
- Cliques em e-mail
- Aberturas de e-mail (excluindo [Aberturas por Máquina]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens))
- Cliques em SMS (somente se o [encurtamento de links]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) e o rastreamento avançado estiverem ativados)

Por exemplo, Sam pode abrir seus e-mails regularmente pela manhã, mas abrir o app e interagir com notificações à noite. Isso significa que Sam receberia uma Campaign de e-mail com Intelligent Timing pela manhã, enquanto receberia Campaigns com notificações por push à noite, quando é mais provável que ela interaja.

Se um usuário não tiver dados de engajamento relevantes para a Braze calcular o horário ideal de envio, você pode especificar um horário de fallback.

## Exemplos {#examples}

- Enviar Campaigns recorrentes que não sejam sensíveis ao tempo
- Automatizar Campaigns com usuários de múltiplos fusos horários
- Ao enviar mensagens para seus usuários mais engajados (eles terão mais dados de engajamento)

## Usando o Intelligent Timing {#using-intelligent-timing}

Esta seção descreve como configurar o Intelligent Timing para suas Campaigns e Canvas.

{% tabs local %}
{% tab Campaign %}
### Etapa 1: Adicionar o Intelligent Timing {#step-1-add-intelligent-timing}

1. Crie uma Campaign e componha sua mensagem.
2. Selecione **Scheduled Delivery** como tipo de entrega.
3. Em **Time-Based Scheduling Options**, selecione **Intelligent Timing**.
4. Defina a frequência de entrada. Para envios únicos, selecione **Once** e escolha uma data de envio. Para envios recorrentes, selecione **Daily**, **Weekly** ou **Monthly** e configure as opções de recorrência. Consulte [Considerações](#considerations) para mais orientações.
5. Opcionalmente, configure o [horário de silêncio](#quiet-hours).
6. Especifique um [horário de fallback](#campaign-fallback). Este é o horário em que a mensagem será enviada caso o perfil do usuário não tenha eventos relevantes para calcular um horário ideal.

![Tela de agendamento de Campaign mostrando o Intelligent Timing com horário de fallback e configurações de horário de silêncio]({% image_buster /assets/img/intelligent_timing/campaign_scheduling.png %})

#### Horário de silêncio {#quiet-hours}

Use o horário de silêncio para evitar que mensagens sejam enviadas durante horários específicos. Isso é útil quando você quer evitar enviar mensagens nas primeiras horas da manhã ou durante a madrugada, mas ainda permitir que o Intelligent Timing determine a melhor janela de entrega.

{% alert note %}
O horário de silêncio substituiu a configuração **Only send within specific hours**. Em vez de escolher quando as mensagens podem ser enviadas, agora você escolhe quando elas não devem ser enviadas. Por exemplo, para enviar mensagens entre 16h e 18h, defina o horário de silêncio das 18h às 16h do dia seguinte.
{% endalert %}

1. Selecione **Enable Quiet Hours**.
2. Selecione o horário de início e término em que as mensagens **não** devem ser enviadas.

![Alternância de horário de silêncio ativada com horário de início e término definido para bloquear a entrega de mensagens durante a noite]({% image_buster /assets/img/intelligent_timing/quiet_hours.png %})

Quando o horário de silêncio está ativado, a Braze não enviará mensagens durante o período de silêncio, mesmo que esse horário corresponda ao horário ideal de envio do usuário. Se o horário ideal do usuário estiver dentro da janela de silêncio, a mensagem será enviada na borda mais próxima da janela.

Por exemplo, se o horário de silêncio estiver definido das 22h às 6h e o horário ideal do usuário for 5h30, a Braze reterá a mensagem e a entregará às 6h — o horário mais próximo fora da janela de silêncio.

Para saber mais, consulte [Horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

#### Prévia dos horários de entrega {#preview-delivery-times}

Para ver uma estimativa de quantos usuários receberão a mensagem em cada hora do dia, use o gráfico de prévia (somente para Campaigns).

1. Adicione Segments ou filtros na etapa de públicos-alvo.
2. Na seção **Preview Delivery Times for** (que aparece tanto na etapa de públicos-alvo quanto na etapa de agendamento de entrega), selecione seu canal.
3. Clique em **Refresh Data**.

![Gráfico de prévia de entrega para push no Android mostrando o pico de engajamento entre 12h e 14h, e o horário mais popular do app sendo 14h.]({% image_buster /assets/img/intel-timing-preview.png %})

### Etapa 2: Escolher uma data de envio {#step-2-choose-a-send-date}

Em seguida, selecione uma data de envio para sua Campaign. Tenha em mente o seguinte ao agendar Campaigns com Intelligent Timing:

#### Lançar a Campaign com 48 horas de antecedência {#launch-campaign-48-hours-in-advance}

Lance sua Campaign pelo menos 48 horas antes da data de envio agendada. Isso se deve às variações de fuso horário. A Braze calcula o horário ideal à meia-noite no horário de Samoa (UTC+13), um dos primeiros fusos horários do mundo. Um único dia abrange cerca de 48 horas ao redor do globo, o que significa que, se você lançar uma Campaign dentro desse intervalo de 48 horas, é possível que o horário ideal do usuário já tenha passado no fuso horário dele, e a mensagem não será enviada.

{% alert important %}
Se uma Campaign for lançada e o horário ideal do usuário tiver passado há menos de uma hora, a mensagem será enviada imediatamente. Se o horário ideal tiver passado há mais de uma hora, a mensagem não será enviada.
{% endalert %}

#### Janela de 3 dias para filtros de Segment {#3-day-window-for-segment-filters}

Se você estiver direcionando um público que realizou uma ação em um determinado período de tempo, permita pelo menos uma janela de 3 dias nos seus filtros de Segment. Por exemplo, em vez de `First used app more than 1 day ago` e `First used app less than 3 days ago`, use 1 dia e 4 dias.

![Filtros para o público-alvo em que a Campaign direciona usuários que usaram o app pela primeira vez entre 1 e 4 dias atrás.]({% image_buster /assets/img/intelligent_timing/first_used_app.png %})

Isso também se deve aos fusos horários — selecionar um período menor que 3 dias pode fazer com que alguns usuários saiam do Segment antes que o horário ideal de envio seja alcançado.

Para saber mais, consulte [FAQ: Intelligent Timing](#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

#### Agendar o envio otimizado pelo menos 2 dias após o teste A/B {#schedule-the-optimized-send-at-least-2-days-after-the-ab-test}

Se você usar [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) para uma Campaign de envio único, o Intelligent Timing pode afetar a duração e o momento da sua Campaign.

Ao usar o Intelligent Timing, defina a duração do experimento para que o envio otimizado comece pelo menos dois dias após o início do teste A/B. Por exemplo, se o teste começar em 16 de abril às 16h, configure o envio otimizado para começar no mínimo em 18 de abril às 16h. Isso dá à Braze tempo suficiente para avaliar o comportamento dos usuários e enviar mensagens no horário ideal.

### Etapa 3: Configurar horário de silêncio (opcional) {#step-3-configure-quiet-hours-optional}

Opcionalmente, você pode optar por limitar a janela de entrega. Isso pode ser útil se sua Campaign se refere a um evento, promoção ou venda específica, mas geralmente não é recomendado ao usar o Intelligent Timing. Para saber mais, consulte [Considerações](#considerations).

O horário de silêncio funciona como uma janela de não envio. O Intelligent Timing ainda determina o horário ideal de envio de cada usuário, mas se esse horário estiver dentro do horário de silêncio, a Braze adiará a mensagem até o próximo horário disponível fora do período de silêncio.

Para configurar o horário de silêncio:

1. Ao configurar o Intelligent Timing, selecione **Enable Quiet Hours**.
2. Insira o horário de início e término da janela de silêncio.

### Etapa 4: Escolher um horário de fallback {#campaign-fallback}

Escolha um horário de fallback para usar caso o perfil do usuário não tenha eventos relevantes para calcular um horário ideal de entrega.

![Agendando uma Campaign com Intelligent Timing]({% image_buster /assets/img/intelligent_timing_1.png %})

{% multi_lang_include brazeai/intelligent_suite/fallback_time.md type="campaign" %}

### Etapa 5: Prévia dos horários de entrega {#step-5-preview-delivery-times}

Para ver uma estimativa de quantos usuários receberão a mensagem em cada hora do dia, use o gráfico de prévia:

1. Adicione Segments ou filtros na etapa **Target Audiences**.
2. Na seção **Preview Delivery Times for** (que aparece tanto na etapa **Target Audiences** quanto na etapa **Schedule Delivery**), selecione seu canal.
3. Selecione **Refresh Data**.

O gráfico de prévia mostra cada hora do dia usando seu fuso local. Os rótulos não estão definidos em um fuso horário global único.

![Exemplo de prévia dos horários de entrega para push no Android.]({% image_buster /assets/img/intel-timing-preview.png %})

Sempre que você alterar qualquer configuração do Intelligent Timing ou do público da sua Campaign, atualize os dados novamente para visualizar um gráfico atualizado.

O gráfico mostra em azul os usuários que tiveram eventos relevantes para calcular um horário ideal e em vermelho os usuários que usarão o horário de fallback. Use os filtros de cálculo para ajustar a visualização da prévia e ter uma visão mais detalhada de cada grupo de usuários.
{% endtab %}

{% tab Canvas %}

### Etapa 1: Adicionar o Intelligent Timing

No seu Canvas, adicione uma [etapa de Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), depois vá para **Delivery Settings** e selecione **Using Intelligent Timing**.

As mensagens serão enviadas aos usuários que entraram na etapa naquele dia no horário local ideal deles. No entanto, se o horário ideal já tiver passado naquele dia, a mensagem será entregue no horário ideal do dia seguinte. Etapas de mensagem que direcionam múltiplos canais podem enviar ou tentar enviar mensagens em horários diferentes para canais diferentes. Quando a primeira mensagem em uma etapa de Mensagem tenta ser enviada, todos os usuários avançam automaticamente.

### Etapa 2: Escolher um horário de fallback {#step-2-choose-a-fallback-time}

Escolha um horário de fallback para enviar a mensagem aos usuários do seu público que não têm dados de engajamento relevantes para que a Braze calcule um horário ideal de envio. {% multi_lang_include brazeai/intelligent_suite/fallback_time.md %}

### Etapa 4: Adicionar uma etapa de postergação {#step-4-add-a-delay-step}

Diferente das Campaigns, você não precisa lançar o Canvas 48 horas antes da data de envio, pois o Intelligent Timing é definido no nível da etapa, não no nível do Canvas.

Em vez disso, adicione uma [etapa de postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) de pelo menos dois dias corridos entre a entrada do usuário no Canvas e o momento em que ele recebe a etapa com Intelligent Timing.

#### Dias corridos vs. dias de 24 horas {#calendar-vs-24-hour-days}

Ao usar o Intelligent Timing após uma etapa de postergação, a data de entrega pode variar dependendo de como você calcula a postergação. Isso se aplica apenas quando a postergação está definida como **After a duration**, pois há uma diferença entre como "dias" e "dias corridos" são calculados.

- **Dias:** 1 dia equivale a 24 horas, calculadas a partir do momento em que o usuário entra na etapa de postergação.
- **Dias corridos:** 1 dia é o período desde quando o usuário entra na etapa de postergação até a meia-noite no fuso horário dele. Isso significa que 1 dia corrido pode durar apenas alguns minutos.

Ao usar o Intelligent Timing, recomendamos usar dias corridos para postergações em vez de dias de 24 horas. Isso porque, com dias corridos, a mensagem será enviada no último dia da postergação, no horário ideal. Com um dia de 24 horas, há a possibilidade de o horário ideal do usuário ser anterior à entrada dele na etapa, o que significa que um dia extra será adicionado à postergação.

Por exemplo, digamos que o horário ideal do Luka é 14h. Ele entra na etapa de postergação às 14h01 do dia 1º de março, e a postergação está definida como 2 dias.

- O dia 1 termina em 2 de março às 14h01
- O dia 2 termina em 3 de março às 14h01

No entanto, o Intelligent Timing está configurado para entregar às 14h, horário que já passou. Então Luka não receberá a mensagem até o dia seguinte: 4 de março às 14h.

![Gráfico ilustrando a diferença entre dias e dias corridos: se o horário ideal do usuário é 14h, mas ele entra na etapa de postergação às 14h01, e a postergação está definida como 2 dias, a opção de dias entrega a mensagem 3 dias depois porque o usuário entrou na etapa após o horário ideal, enquanto dias corridos entrega a mensagem 2 dias depois, no último dia da postergação.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}
{% endtab %}
{% endtabs %}

## Considerações {#considerations}

- Mensagens no app e webhooks são entregues imediatamente e não recebem horários otimizados.
- O Intelligent Timing não está disponível para Campaigns baseadas em ação ou disparadas por API.
- O Intelligent Timing não deve ser usado nos seguintes cenários:
    - **Limite de frequência:** se tanto o limite de frequência quanto o Intelligent Timing forem usados, não há garantia de quando a mensagem será entregue. Campaigns recorrentes diárias com Intelligent Timing não suportam com precisão um limite total de envio de mensagens.
    - **Campaigns de aquecimento de IP:** alguns comportamentos do Intelligent Timing podem causar dificuldades para atingir os volumes diários necessários quando você está começando a aquecer seu IP. Isso acontece porque o Intelligent Timing avalia os Segments duas vezes: uma quando a Campaign ou o Canvas é criado pela primeira vez, e outra antes do envio aos usuários para verificar se eles ainda devem estar naquele Segment. Isso pode fazer com que os Segments mudem e se alterem, frequentemente levando alguns usuários a saírem do Segment na segunda avaliação. Esses usuários não são substituídos, impactando o quão próximo do limite máximo de usuários você consegue alcançar.

## Solução de problemas {#troubleshooting}

### Gráfico de prévia mostrando poucos usuários com horários ideais {#preview-chart-showing-few-users-with-optimal-times}

Se não houver eventos relevantes para um usuário (por exemplo, novos usuários com pouco ou nenhum engajamento), a Braze usa a configuração de fallback definida — seja o horário de fallback personalizado ou o horário mais popular de uso do app entre todos os usuários.

### Impacto do fuso horário na entrega com Intelligent Timing {#impact-of-time-zone-on-intelligent-timing-delivery}

O Intelligent Timing usa o fuso horário local de cada usuário e os dias do calendário para determinar a entrega ideal. Por isso, usuários em fusos horários à frente ou atrás do fuso horário de referência da sua Campaign podem receber mensagens em um dia diferente do esperado.

Por exemplo, se uma Campaign está agendada para 15 de março e o horário ideal de um usuário é calculado para essa data, um usuário em um fuso horário à frente do ponto de referência da Campaign pode receber a mensagem no final do dia 14 de março no fuso horário de referência, enquanto um usuário em um fuso horário atrás do ponto de referência pode recebê-la no dia 16 de março.

Se os usuários não receberem as mensagens como esperado, verifique se o campo de fuso horário no perfil deles está preenchido corretamente. Se o campo de fuso horário estiver vazio, o usuário pode receber mensagens alinhadas ao fuso horário da empresa em vez do fuso local.

### Envio após a data agendada {#sending-past-the-scheduled-date}

Sua Campaign com Intelligent Timing pode enviar após a data agendada se você usar [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection). Para uma Campaign de envio único, a Braze envia a variante com melhor desempenho para o público restante após o teste inicial, o que aumenta a duração da Campaign.

Se você usar Intelligent Timing, deixe tempo suficiente para que o teste A/B termine e agende o envio otimizado para dois dias após o teste inicial.

## Perguntas frequentes (FAQ) {#faq}

### Geral {#general}

#### O que o Intelligent Timing prevê? {#what-does-intelligent-timing-predict}

O Intelligent Timing se concentra em prever quando um usuário tem mais chances de abrir ou clicar nas suas mensagens, garantindo que elas cheguem aos usuários nos momentos de maior engajamento.

#### O Intelligent Timing é calculado separadamente para cada dia da semana? {#is-intelligent-timing-calculated-separately-for-each-day-of-the-week}

Não, o Intelligent Timing não está vinculado a dias específicos. Em vez disso, ele personaliza os horários de envio com base nos padrões de engajamento únicos de cada usuário e no canal que você está usando, como e-mail ou notificações por push. Isso garante que suas mensagens cheguem aos usuários quando eles estão mais receptivos.

### Cálculos {#calculations}

#### Quais dados são usados para calcular o horário ideal para cada usuário? {#what-data-is-used-to-calculate-the-optimal-time-for-each-user}

Para calcular o horário ideal, o Intelligent Timing:

1. Analisa os dados de interação de cada usuário registrados pelo SDK da Braze. Isso inclui:
  - Horários de sessão
  - Aberturas Diretas de push
  - Aberturas por Influência de push
  - Cliques em e-mail
  - Aberturas de e-mail (excluindo aberturas por máquina)
2. Agrupa esses eventos por horário, identificando o momento ideal de envio para cada usuário.

#### As aberturas por máquina são incluídas no cálculo do horário ideal? {#are-machine-opens-included-when-calculating-optimal-time}

Não, as [aberturas por máquina]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) são excluídas dos cálculos do horário ideal. Isso significa que os horários de envio são baseados exclusivamente no engajamento genuíno do usuário, proporcionando um timing mais preciso para suas campanhas.

#### Quão preciso é o horário ideal? {#how-precise-is-the-optimal-time}

O Intelligent Timing programa mensagens durante a "hora de maior engajamento" de cada usuário, com base nos inícios de sessão e eventos de abertura de mensagens. Dentro dessa hora, o horário da mensagem é arredondado para os cinco minutos mais próximos. Por exemplo, se o horário ideal de um usuário for calculado como 16h58, a mensagem será programada para 17h. Pode haver pequenos atrasos na entrega devido à atividade do sistema durante períodos de alta demanda.

#### Quais são os cálculos de fallback se não houver eventos relevantes? {#what-are-the-fallback-calculations-if-there-are-no-relevant-events}

Se não houver eventos relevantes para um usuário, o Intelligent Timing usa a configuração de fallback definida nas configurações da mensagem — seja um horário de fallback personalizado ou o horário mais popular para usar o app entre todos os usuários.

### Campanhas {#campaigns}

#### Com quanto tempo de antecedência devo lançar uma campanha com Intelligent Timing para entregá-la com sucesso a todos os usuários em todos os fusos horários? {#how-far-in-advance-should-i-launch-an-intelligent-timing-campaign-to-successfully-deliver-it-to-all-users-in-all-time-zones}

A Braze calcula o horário ideal à meia-noite no horário de Samoa, um dos primeiros fusos horários do mundo. Em um único dia, isso abrange aproximadamente 48 horas. Por exemplo, uma pessoa cujo horário ideal é 0h01 e que mora na Austrália já teve seu horário ideal ultrapassado, e é "tarde demais" para enviar para ela. Por essas razões, você precisa programar com 48 horas de antecedência para entregar com sucesso a todos no mundo que usam seu app.

#### Por que minha campanha com Intelligent Timing está mostrando pouco ou nenhum envio? {#why-is-my-intelligent-timing-campaign-showing-little-to-no-sends}

Se não houver eventos de engajamento relevantes para um usuário (por exemplo, novos usuários com poucos ou nenhum clique ou abertura), o Intelligent Timing usa a configuração de fallback definida — seja o seu horário de fallback personalizado ou o horário mais popular para usar o app entre todos os usuários.

#### Por que minha campanha com Intelligent Timing está sendo enviada após a data programada? {#why-is-my-intelligent-timing-campaign-sending-past-the-scheduled-date}

Sua campanha com Intelligent Timing pode estar sendo enviada após a data programada quando a opção **Optimize with BrazeAI<sup>TM</sup>** está ativada. Em uma campanha de envio único, a Braze envia a variante com melhor desempenho para o público restante após o término do teste A/B, o que aumenta a duração da campanha.

Deixe tempo suficiente para o teste A/B terminar e programe o envio otimizado para dois dias após o teste inicial.

### Funcionalidade {#functionality}

#### Quando a Braze verifica os critérios de elegibilidade para os filtros de segmento e público? {#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters}

A Braze realiza duas verificações quando uma campanha é lançada:

1. **Verificação inicial:** À meia-noite no primeiro fuso horário no dia do envio.
2. **Verificação no horário programado:** Logo antes do envio, no horário que o Intelligent Timing selecionou para o usuário.

Tenha cuidado ao filtrar com base em outros envios de campanha para evitar direcionar segmentos inelegíveis. Por exemplo, se você enviar duas campanhas no mesmo dia em horários diferentes e adicionar um filtro que permite que os usuários recebam a segunda campanha apenas se tiverem recebido a primeira, os usuários não receberão a segunda campanha. Isso ocorre porque ninguém era elegível quando a campanha foi criada pela primeira vez e os segmentos foram formados.

#### Posso usar o horário de silêncio na minha campanha com Intelligent Timing? {#can-i-use-quiet-hours-in-my-intelligent-timing-campaign}

O horário de silêncio pode ser usado em uma campanha que utiliza o Intelligent Timing. O algoritmo do Intelligent Timing evitará o horário de silêncio para que ainda envie a mensagem a todos os usuários elegíveis. Dito isso, recomendamos desativar o horário de silêncio, a menos que haja implicações de política, conformidade ou outras questões legais sobre quando as mensagens podem ou não ser enviadas.

#### O que acontece se o horário ideal de um usuário estiver dentro do horário de silêncio? {#what-happens-if-the-optimal-time-for-a-user-is-within-the-quiet-hours}

Se o horário ideal determinado cair dentro do horário de silêncio, a Braze encontra o limite mais próximo do horário de silêncio e programa a mensagem para o próximo horário permitido antes ou depois do período de silêncio. A mensagem é enfileirada para envio no limite mais próximo do horário de silêncio em relação ao horário ideal.

#### Posso usar o Intelligent Timing com limite de frequência? {#can-i-use-intelligent-timing-and-rate-limiting}

O limite de frequência pode ser usado em uma campanha que utiliza o Intelligent Timing. No entanto, a natureza do limite de frequência significa que alguns usuários podem receber suas mensagens em um momento menos ideal, especialmente se um grande número de usuários em relação ao tamanho do limite de frequência estiver programado para o horário de fallback por não terem eventos relevantes.

Recomendamos usar o limite de frequência em uma campanha com Intelligent Timing apenas quando houver requisitos técnicos que precisem ser atendidos com o limite de frequência.

#### Posso usar o Intelligent Timing durante o aquecimento de IP? {#can-i-use-intelligent-timing-while-ip-warming}

A Braze não recomenda usar o Intelligent Timing quando os usuários estão começando o aquecimento de IP, pois alguns de seus comportamentos podem causar dificuldades em atingir os volumes diários necessários. Isso ocorre porque o Intelligent Timing avalia os segmentos de campanha duas vezes: uma vez quando a campanha é criada pela primeira vez, e uma segunda vez antes de enviar aos usuários para verificar se eles ainda devem estar nesse segmento.

Isso pode fazer com que os segmentos mudem, muitas vezes levando alguns usuários a saírem do segmento na segunda avaliação. Esses usuários não são substituídos, impactando o quão próximo do limite máximo de usuários você consegue alcançar.

#### Como é determinado o horário mais popular do app? {#how-is-the-most-popular-app-time-determined}

O horário mais popular do app é determinado pelo horário médio de início de sessão do espaço de trabalho (no fuso local). Essa métrica pode ser encontrada no dashboard ao visualizar a prévia dos horários de uma campanha, mostrada em vermelho.

#### O Intelligent Timing leva em conta as aberturas por máquina? {#does-intelligent-timing-account-for-machine-opens}

Sim, as aberturas por máquina são filtradas pelo Intelligent Timing, de modo que não influenciam o resultado.

#### Como posso garantir que o Intelligent Timing funcione da melhor forma possível? {#how-can-i-make-sure-intelligent-timing-works-as-well-as-possible}

O Intelligent Timing usa o histórico individual de engajamento com mensagens de cada usuário, considerando os horários em que eles receberam mensagens. Antes de usar o Intelligent Timing, certifique-se de ter enviado mensagens aos usuários em diferentes horários do dia. Dessa forma, você consegue "amostrar" qual pode ser o melhor horário para cada usuário. Uma amostragem inadequada de diferentes horários do dia pode fazer com que o Intelligent Timing escolha um horário de envio abaixo do ideal para um usuário.

#### Como ativo o Intelligent Timing em uma etapa do Canvas? {#how-do-i-enable-intelligent-timing-on-a-canvas-step}

No Canvas, adicione ou abra uma [etapa de Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), acesse **Delivery Settings** e selecione **Using Intelligent Timing**. Conforme as orientações de configuração do Canvas neste artigo, inclua uma [etapa de postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) de pelo menos dois dias corridos entre a entrada no Canvas e essa mensagem, para que o Intelligent Timing tenha um histórico de engajamento adequado para avaliar.