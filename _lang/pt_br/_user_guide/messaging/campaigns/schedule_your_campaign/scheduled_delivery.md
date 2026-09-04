---
nav_title: Entrega agendada
article_title: Entrega agendada
page_order: 0
page_type: reference
description: "Este artigo de referência descreve as diferenças entre as opções de agendamento com base em horário para entrega de campanhas."
tool: Campaigns

---

# Entrega agendada {#scheduled-delivery}

> Campanhas enviadas usando entrega agendada com base em horário são entregues em dias específicos.

## Opção 1: Enviar assim que a campanha for lançada {#option-1-send-as-soon-as-the-campaign-is-launched}

Se você optar por enviar uma mensagem assim que ela for lançada, sua mensagem começará a ser enviada assim que você terminar de criar sua campaign.

![A seção "Entrega" com "Agendado" selecionado e a opção de agendamento baseado em tempo para enviar assim que a campaign for lançada.]({% image_buster /assets/img_archive/schedule_immediately.png %})

Esse tipo de agendamento é projetado para campaigns pontuais que você deseja enviar imediatamente, como mensagens sobre um evento atual. Um app de esportes, por exemplo, pode agendar notificações por push sobre atualizações de placar usando essa opção. Além disso, ao enviar mensagens de teste destinadas apenas a você ou à sua equipe, essa opção permite entregá-las imediatamente.

Se você planeja editar a campaign e reenviá-la após visualizar o teste, marque a caixa que torna os usuários [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) para receber a campaign. Por padrão, a Braze envia uma campaign para um usuário apenas uma vez, a menos que essa caixa esteja marcada.

## Opção 2: Enviar em um horário designado {#option-2-send-at-a-designated-time}

Agendar uma campaign para um horário designado permite que você especifique os dias e horários em que sua campaign será enviada. Você pode enviar uma mensagem uma vez, diariamente, semanalmente ou mensalmente em um determinado horário do dia, além de especificar quando sua campaign deve começar e terminar. Essa data de término é inclusiva, o que significa que o último envio ocorre na data de término.

Se você selecionar um cronograma recorrente mensal, observe que alguns meses podem não ter o dia selecionado. Por exemplo, digamos que você configure uma campaign para enviar mensalmente no dia 31. Nesse cenário, a Braze envia no último dia daquele mês, como 30 de abril, porque 31 de abril não existe.

Se você selecionar **Scheduled Delivery** e não optar por enviar no fuso local do usuário, sua campaign será enviada de acordo com o fuso horário especificado na página **Company Settings**.

![As opções de agendamento baseadas em tempo para enviar uma campaign em um horário designado.]({% image_buster /assets/img_archive/schedule_designated.png %})

### Campaigns com fuso local {#local-time-zone-campaigns}

Você pode entregar a mensagem no fuso local dos usuários para que membros do seu público internacional não recebam uma notificação em horários inconvenientes. Campaigns com fuso local precisam ser agendadas com 24 horas de antecedência para garantir que usuários elegíveis de todos os fusos horários possam recebê-las. Consulte as [Perguntas frequentes sobre Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign) para entender como Campaigns com fuso local funcionam e as regras de entrega associadas.

Segments direcionados com Campaigns de fuso local devem incluir, no mínimo, uma janela de 2 dias para abranger usuários de todos os fusos horários. Por exemplo, se sua campaign está agendada para enviar à noite, mas tem apenas uma janela de 1 dia, alguns usuários podem ter saído do Segment quando seu fuso horário for alcançado. Exemplos de filtros que criam uma janela de 2 dias são "usado pela última vez há mais de 1 dia" e "usado pela última vez há menos de 3 dias", ou "primeira compra há mais de 7 dias" e "primeira compra há menos de 9 dias".

### Casos de uso {#use-cases}

Cronogramas com horário designado são mais adequados para mensagens agendadas com antecedência e Campaigns recorrentes, como integração e retenção, que são executadas regularmente para todos os usuários qualificados.

## Opção 3: Intelligent Timing {#option-3-intelligent-timing}

O [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) permite entregar uma campanha a cada usuário em um horário diferente. A Braze calcula o horário de cada pessoa com base em quando esse usuário normalmente interage com o seu app e suas notificações. Opcionalmente, você pode especificar que as campanhas com Intelligent Timing sejam enviadas apenas durante uma determinada parte do dia. Por exemplo, se você está notificando os usuários sobre uma promoção que termina à meia-noite, pode querer que suas mensagens sejam enviadas até as 22h, no máximo.

![As opções de agendamento baseado em horário para usar o Intelligent Timing e enviar uma campanha no horário mais popular de uso do app entre todos os usuários.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### Regras de entrega {#delivery-rules}

Como o horário ideal de um usuário pode ser qualquer momento ao longo de 24 horas em todos os fusos horários globais, todas as campanhas com Intelligent Timing devem ser agendadas com 48 horas de antecedência. Agendar com 48 horas de antecedência garante a entrega a todos os usuários no mundo todo, já que um único dia abrange aproximadamente 48 horas em todos os fusos horários. Além disso, de forma semelhante às campanhas com horário designado, mensagens com uma janela de 1 dia perdem os usuários que saem do Segment antes que o horário ideal no fuso horário deles seja alcançado. Os Segments para campanhas com Intelligent Timing devem incorporar uma janela de pelo menos 3 dias para compensar isso.

Se o perfil de um usuário não tiver dados suficientes para calcular um horário ideal, você pode escolher um método de fallback para enviar no horário mais popular de uso do app entre todos os usuários ou em um horário de fallback personalizado definido.

### Casos de uso

As campanhas com Intelligent Timing funcionam melhor para mensagens únicas e recorrentes em que há alguma flexibilidade em relação ao horário de entrega, como quando não são adequadas para notícias de última hora ou anúncios com horário definido.

## Avaliação de critérios de público com postergações {#audience-criteria-evaluation-with-delays}

Para Campaigns que usam entrega agendada, os critérios de público são sempre avaliados no momento do envio agendado, não quando a Campaign é lançada. Isso se aplica a qualquer postergação entre o agendamento e o envio — por exemplo, limite de frequência, fuso local, Intelligent Timing ou um cronograma de disparo.

### Momento das alterações de Segment {#timing-of-segment-changes}

Se você modificar um Segment usado como público de uma Campaign agendada, as alterações feitas próximas ao horário de envio agendado geralmente são incluídas quando o público é avaliado. O ponto de corte exato varia, mas as alterações são incluídas se terminarem de ser processadas antes da Braze montar o público para aquele envio.

Por exemplo, se você atualizar um Segment às 15h50 para uma Campaign agendada para envio às 16h, a Braze usa os critérios atualizados do Segment ao avaliar o público, desde que as alterações terminem de ser processadas antes do início da execução da Campaign.

#### Práticas recomendadas {#best-practices}

Para dar tempo às alterações de Segment de serem processadas antes do envio das suas Campaigns agendadas:

- **Planeje com antecedência:** Faça alterações no Segment bem antes do horário de envio agendado para que elas tenham tempo de serem processadas.
- **Teste primeiro:** Quando possível, teste as alterações em uma Campaign menor antes de aplicá-las a Campaigns maiores e mais críticas.

Para saber mais sobre opções de entrega agendada, consulte [Tipos de entrega e entrada]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#time-based-options).

## Solução de problemas {#troubleshooting}

### Por que minha campanha de e-mail agendada não alcançou todo o público estimado? {#why-didnt-my-scheduled-email-campaign-reach-the-entire-estimated-audience}

Os envios podem ser menores do que o público estimado quando os usuários não têm um endereço de e-mail, não estão inscritos para receber e-mails ou são excluídos por filtros de entregabilidade no momento do envio. Uma alteração recente no endereço de e-mail de um usuário também pode afetar a elegibilidade quando os critérios de público são reavaliados no momento do envio. Para saber mais sobre outros fatores, consulte [Por que os envios são menores do que o tamanho estimado do público?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size).

### Por que minha campanha foi enviada um dia antes do horário agendado? {#why-did-my-campaign-send-a-day-before-the-scheduled-time}

Se uma campanha é enviada antes do cronograma definido em **Company Settings**, ative **Send in local time zone** ou adicione uma janela de horário de entrega para campanhas com Intelligent Timing. Sem essas configurações, a avaliação de fuso horário pode enfileirar envios para usuários em fusos horários anteriores antes do horário pretendido. Para saber mais, consulte [Campanhas no fuso local](#local-time-zone-campaigns) e [Quando a Braze avalia os usuários para entrega no fuso local?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery).