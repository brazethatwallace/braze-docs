---
nav_title: Status
article_title: Status
page_order: 6
description: "Saiba mais sobre os status de Campaigns e Canvas e como usá-los no dashboard."
tool:
    - Campaigns
    - Canvas
---

# Status de Campaigns e Canvas {#campaign-and-canvas-statuses}

> Saiba mais sobre os status de Campaigns e Canvas e como você pode usá-los no dashboard.

## Filtrando por status {#filtering-by-status}

Para filtrar suas Campaigns ou Canvas por status, selecione **All Statuses** e escolha um status.

![O menu suspenso "All Statuses" no dashboard da Braze.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Alterando o status {#changing-the-status}

Para alterar o status de uma Campaign ou Canvas, selecione o menu <i class="fas fa-ellipsis-vertical"></i> e escolha um status.

![Uma lista de Canvas no dashboard da Braze, com o menu aberto para um dos Canvas.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Status disponíveis {#available-statuses}

Estes são os status disponíveis para Campaigns e Canvas:

| Status | Descrição |
| --- | --- |
| Ativo | Campaigns e Canvas ativos estão em processo de envio. Por padrão, você verá Campaigns e Canvas ativos nas respectivas páginas. |
| Rascunho | Rascunhos de Campaigns e Canvas são salvos, mas não lançados. Para continuar editando e começar a enviar, você pode selecionar o rascunho acessando **Messaging** no dashboard da Braze e selecionando **Canvas** ou **Campaigns**. |
| Arquivado | Campaigns e Canvas arquivados são mensagens que não estão mais sendo enviadas. Essas Campaigns e Canvas também são removidos dos gráficos de estatísticas nas páginas [**Home**]({{site.baseurl}}/user_guide/analytics/dashboards/home) e [**Revenue**]({{site.baseurl}}/user_guide/analytics/reports/revenue_report). |
| Parado | Campaigns e Canvas parados estão pausados, mas você ainda pode editá-los. Para retomar um Canvas, acesse a etapa **Summary** do criador de Canvas e selecione **Resume Canvas**. Para Campaigns, selecione o menu <i class="fas fa-ellipsis-vertical" aria-label="Mais opções"></i> e depois **Resume**. Para saber mais, consulte [Comportamento de Canvas parado](#stopped-canvas-behavior). |
| Sem atividades | Quando uma Campaign ou Canvas não está mais enviando mensagens, a Braze atribuirá um status sem atividades para ajudar a classificar e gerenciar sua lista de Campaigns e Canvas. Você pode visualizar quais Campaigns ou Canvas serão automaticamente parados e a data de parada associada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Status disponíveis" }

### Comportamento de Canvas parado {#stopped-canvas-behavior}

Quando um Canvas é parado, o seguinte ocorre:

- **Mensagens agendadas:** Suas mensagens agendadas não serão enviadas, independentemente da posição do usuário no Canvas. Isso também inclui usuários que estavam na fila devido ao limite de frequência.
- **Envios de e-mail:** Os envios de e-mail podem não parar imediatamente, pois seu provedor de serviços de e-mail (ESP) pode continuar processando suas solicitações existentes.
- **Etapas de postergação:** Usuários em uma [etapa de postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) permanecerão nela normalmente, mas sairão do Canvas quando o período definido terminar.
- **Alterações de rascunho:** Quaisquer alterações de rascunho no Canvas serão descartadas quando o Canvas for parado.

#### Quando você retoma um Canvas {#when-you-resume-a-canvas}

Para retomar o Canvas, acesse a etapa **Summary** do criador de Canvas e selecione **Resume Canvas**. Quando você retoma um Canvas, os usuários continuam sua jornada de onde pararam:

- Usuários em etapas de postergação: Usuários que estavam aguardando em uma etapa de postergação quando o Canvas foi parado continuam aguardando pelo período de postergação restante. Por exemplo, se um usuário estava há 2 horas em uma postergação de 24 horas quando o Canvas foi parado por 3 dias, ele aguardará mais 22 horas após o Canvas ser retomado antes de avançar.
- Usuários aguardando mensagens: Quaisquer mensagens agendadas que estavam pendentes quando o Canvas foi parado são enviadas conforme agendado quando você retoma o Canvas — desde que o horário agendado ainda não tenha passado.
- Usuários que saíram: Usuários que saíram do Canvas durante o período de parada (por exemplo, usuários que estavam em etapas de postergação e chegaram ao final de sua postergação) não reentrarão no Canvas quando você retomá-lo.

#### Comportamento de fuso local {#local-time-zone-behavior}

Se o seu Canvas está configurado para **Inserir usuários neste Canvas no fuso local deles**, tenha estas considerações em mente ao parar e retomar:

- Janelas de entrada: Quando você retoma o Canvas, os usuários entram com base no fuso local conforme originalmente configurado. A Braze continua avaliando a elegibilidade de entrada de acordo com o fuso de cada usuário.
- Janelas de entrada perdidas: Se o Canvas foi parado durante uma janela de entrada agendada para usuários em determinados fusos, esses usuários não entrarão retroativamente quando o Canvas for retomado. A avaliação de entrada é retomada dali em diante.

#### Cenários comuns {#common-scenarios}

**Cenário 1: Erro no conteúdo da mensagem**
Você lança um Canvas, mas percebe um erro de digitação em uma das mensagens. Pare o Canvas, edite a mensagem no modo de rascunho e depois retome. Usuários que ainda não receberam a mensagem receberão a versão corrigida. Usuários que já a receberam não a receberão novamente.

**Cenário 2: Problema de direcionamento**
Você percebe que o Canvas está direcionando o Segment errado. Pare o Canvas imediatamente para evitar que mais usuários entrem. Quaisquer usuários atualmente em etapas de postergação sairão quando o período de postergação terminar. Você pode então criar um novo Canvas com o direcionamento correto.

**Cenário 3: Cenário de postergação estendida**
Você tem um Canvas com uma etapa de postergação de sete dias. Você para o Canvas após três dias. Usuários que estavam na etapa de postergação continuam aguardando, mas quando o período de postergação termina enquanto o Canvas ainda está parado, eles saem do Canvas. Se você retomar o Canvas antes que a postergação deles termine, eles continuam pela jornada.

## Práticas recomendadas {#best-practices}

### Monitore suas mensagens por status {#monitor-your-messages-by-status}

Você pode monitorar suas mensagens por status para analisar os detalhes de desempenho. Por exemplo, se você tem uma série de Campaigns ativas, pode avaliar o desempenho de cada Campaign com suas métricas de engajamento e fazer ajustes conforme necessário. Se, por outro lado, você tem alguns Canvas parados, pode considerar se eles devem ser retomados para envio de mensagens ou arquivados completamente.

{% alert tip %}
Procurando mais formas de se manter organizado? Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [tags]({{site.baseurl}}/user_guide/messaging/governance/tags) para fornecer mais contexto de forma rápida.
{% endalert %}

### Faça auditorias nas suas mensagens ativas {#audit-your-active-messages}

Ao realizar auditorias nas suas Campaigns e Canvas ativos, você pode avaliar a relevância e o desempenho, além de remover ou atualizar quaisquer Campaigns e Canvas desatualizados para manter seu envio de mensagens sempre atualizado.