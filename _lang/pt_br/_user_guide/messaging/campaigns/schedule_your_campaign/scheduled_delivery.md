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

Se você optar por enviar uma mensagem assim que ela for lançada, o envio começará assim que você terminar de criar sua campanha.

![A seção "Entrega" com "Agendado" selecionado e a opção de agendamento com base em horário de enviar assim que a campanha for lançada.]({% image_buster /assets/img_archive/schedule_immediately.png %})

Esse tipo de agendamento é projetado para campanhas pontuais que você deseja enviar imediatamente, como mensagens sobre um evento atual. Um app de esportes, por exemplo, pode agendar notificações por push sobre atualizações de placar usando essa opção. Além disso, ao enviar mensagens de teste destinadas apenas a você ou à sua equipe, essa opção permite entregá-las imediatamente.

Se você planeja editar a campanha e reenviá-la após visualizar o teste, marque a caixa que torna os usuários [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/) para receber a campanha. Por padrão, a Braze envia uma campanha para um usuário apenas uma vez, a menos que essa caixa esteja marcada.

## Opção 2: Enviar em um horário designado {#option-2-send-at-a-designated-time}

Agendar uma campanha para um horário designado permite que você especifique os dias e horários em que sua campanha será enviada. Você pode enviar uma mensagem uma vez, diariamente, semanalmente ou mensalmente em um determinado horário do dia, além de especificar quando sua campanha deve começar e terminar. Essa data de término é inclusiva, o que significa que o último envio ocorre na data de término.

Se você selecionar um agendamento recorrente mensal, observe que alguns meses podem não ter o dia selecionado. Por exemplo, digamos que você configure uma campanha para enviar mensalmente no dia 31. Nesse cenário, a Braze envia no último dia daquele mês, como 30 de abril, porque 31 de abril não existe.

Se você selecionar **Entrega agendada** e não optar por enviar no horário local do usuário, sua campanha será enviada de acordo com o fuso horário especificado na página **Configurações da empresa**.

![As opções de agendamento com base em horário para enviar uma campanha em um horário designado.]({% image_buster /assets/img_archive/schedule_designated.png %})

### Campanhas com fuso horário local {#local-time-zone-campaigns}

Você pode entregar a mensagem no fuso horário local dos usuários para que membros do seu público internacional não recebam uma notificação em horários inconvenientes. Campanhas com fuso horário local precisam ser agendadas com 24 horas de antecedência para garantir que usuários elegíveis de todos os fusos horários possam recebê-las. Consulte as [Perguntas frequentes sobre Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign/) para entender como as campanhas com fuso horário local funcionam e as regras de entrega associadas.

Os segmentos direcionados com campanhas de fuso horário local devem incluir, no mínimo, uma janela de 2 dias para abranger usuários de todos os fusos horários. Por exemplo, se sua campanha está agendada para enviar à noite, mas tem apenas uma janela de 1 dia, alguns usuários podem ter saído do segmento quando seu fuso horário for alcançado. Exemplos de filtros que criam uma janela de 2 dias são "último uso há mais de 1 dia" e "último uso há menos de 3 dias", ou "primeira compra há mais de 7 dias" e "primeira compra há menos de 9 dias".

### Casos de uso {#use-cases}

Agendamentos com horário designado são mais adequados para mensagens agendadas com antecedência e campanhas recorrentes, como integração e retenção, que são executadas regularmente para todos os usuários qualificados.

## Opção 3: Intelligent Timing {#option-3-intelligent-timing}

O [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/) permite entregar uma campanha para cada usuário em um horário diferente. A Braze calcula o horário de cada indivíduo com base em quando esse usuário normalmente interage com seu app e suas notificações. Opcionalmente, você pode especificar que campanhas com Intelligent Timing sejam enviadas apenas durante uma determinada parte do dia. Por exemplo, se você está notificando os usuários sobre uma promoção que termina à meia-noite, pode querer que suas mensagens sejam enviadas até as 22h, no máximo.

![As opções de agendamento com base em horário para usar o Intelligent Timing e enviar uma campanha no horário mais popular de uso do app entre todos os usuários.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### Regras de entrega {#delivery-rules}

Como o horário ideal de um usuário pode ser qualquer momento ao longo de 24 horas, todas as campanhas com Intelligent Timing devem ser agendadas com 24 horas de antecedência. Além disso, assim como nas campanhas com horário designado, mensagens com uma janela de 1 dia perderão usuários que saírem do segmento antes que seu horário ideal no fuso horário seja alcançado. Os segmentos para campanhas com Intelligent Timing devem incorporar, no mínimo, uma janela de 3 dias para compensar isso.

Se o perfil de um usuário não tiver dados suficientes para calcular um horário ideal, você pode escolher um método de fallback para enviar no horário mais popular de uso do app entre todos os usuários ou em um horário de fallback personalizado definido.

### Casos de uso

Campanhas com Intelligent Timing funcionam melhor para mensagens pontuais e recorrentes em que há alguma flexibilidade em relação ao horário de entrega — ou seja, quando não são adequadas para notícias de última hora ou anúncios com horário definido.

## Avaliação de critérios de público com postergações {#audience-criteria-evaluation-with-delays}

Para campanhas que usam entrega agendada, os critérios de público são sempre avaliados no momento do envio agendado, não quando a campanha é lançada. Isso se aplica a qualquer postergação entre o agendamento e o envio — por exemplo, limite de taxa, fuso horário local, Intelligent Timing ou agendamento por gatilho.

## Solução de problemas {#troubleshooting}

### Por que minha campanha de e-mail agendada não alcançou todo o público estimado? {#why-didnt-my-scheduled-email-campaign-reach-the-entire-estimated-audience}

Os envios podem ser menores do que o público estimado quando os usuários não possuem um endereço de e-mail, não estão inscritos para receber e-mails ou são excluídos por filtros de entregabilidade no momento do envio. Uma alteração recente no endereço de e-mail de um usuário também pode afetar a elegibilidade quando os critérios de público são reavaliados no momento do envio. Para mais fatores, consulte [Por que os envios são menores do que o tamanho estimado do público?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#why-are-sends-lower-than-the-estimated-audience-size).

### Por que minha campanha foi enviada um dia antes do horário agendado? {#why-did-my-campaign-send-a-day-before-the-scheduled-time}

Se uma campanha for enviada antes do agendamento definido em **Configurações da empresa**, ative **Enviar no fuso horário local** ou adicione uma janela de horário de entrega para campanhas com Intelligent Timing. Sem essas configurações, a avaliação de fuso horário pode enfileirar envios para usuários em fusos horários anteriores antes do horário pretendido. Para saber mais, consulte [Campanhas com fuso horário local](#local-time-zone-campaigns) e [Quando a Braze avalia os usuários para entrega no fuso horário local?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#when-does-braze-evaluate-users-for-local-time-zone-delivery).