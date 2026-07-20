---
nav_title: Status
article_title: Status
page_order: 5
description: "Saiba mais sobre os status de Campaigns e Canvas e como usá-los no dashboard."
tool:
    - Campaigns
    - Canvas
---

# Status de Campaigns e Canvas {#campaign-and-canvas-statuses}

> Saiba mais sobre os status de Campaigns e Canvas e como você pode usá-los no dashboard.

## Filtrando por status {#filtering-by-status}

Para filtrar suas Campaigns ou Canvas por status, selecione **Todos os status** e escolha um status.

![O menu suspenso "Todos os status" no dashboard da Braze.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Alterando o status {#changing-the-status}

Para alterar o status de uma Campaign ou Canvas, selecione o menu <i class="fas fa-ellipsis-vertical"></i> e escolha um status.

![Uma lista de Canvas no dashboard da Braze, com o menu aberto para um dos Canvas.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Status disponíveis {#available-statuses}

Estes são os status disponíveis para Campaigns e Canvas:

| Status | Descrição |
| --- | --- |
| Ativo | Campaigns e Canvas ativos estão em processo de envio. Por padrão, você verá Campaigns e Canvas ativos nas respectivas páginas. |
| Rascunho | Rascunhos de Campaigns e Canvas são salvos, mas não lançados. Para continuar editando e começar a enviar, você pode selecionar o rascunho acessando **Messaging** no dashboard da Braze e selecionando **Canvas** ou **Campaigns**. |
| Arquivado | Campaigns e Canvas arquivados são mensagens que não estão mais sendo enviadas. Essas Campaigns e Canvas também são removidos dos gráficos estatísticos nas páginas [**Início**]({{site.baseurl}}/user_guide/analytics/dashboards/home) e [**Receita**]({{site.baseurl}}/user_guide/analytics/reports/revenue_report). |
| Parado | Campaigns e Canvas parados estão pausados, mas você ainda pode editá-los. Para retomar um Canvas, acesse a etapa **Summary** do criador de Canvas e selecione **Resume Canvas**. Para Campaigns, selecione o menu <i class="fas fa-ellipsis-vertical"></i> e depois **Resume**. Para saber mais, consulte [Comportamento de Canvas parado](#stopped-canvas-behavior). |
| Sem atividades | Quando uma Campaign ou Canvas não está mais enviando mensagens, a Braze atribuirá um status de sem atividades para ajudar a organizar e gerenciar sua lista de Campaigns e Canvas. Você pode visualizar quais Campaigns ou Canvas serão automaticamente parados e a data de parada associada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Status disponíveis" }

### Comportamento de Canvas parado {#stopped-canvas-behavior}

Quando um Canvas é parado, o seguinte ocorre:

- **Mensagens agendadas:** Suas mensagens agendadas não serão enviadas, independentemente da posição do usuário no Canvas. Isso também inclui usuários que estavam na fila devido a limite de taxa.
- **Envios de e-mail:** Os envios de e-mail podem não parar imediatamente, pois seu prestador de serviço de e-mail (ESP) pode continuar processando suas solicitações existentes.
- **Etapas de postergação:** Usuários em uma [etapa de postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) permanecerão nela normalmente, mas sairão do Canvas quando o período definido terminar.
- **Alterações de rascunho:** Quaisquer alterações de rascunho no Canvas serão descartadas quando o Canvas for parado.

Para retomar o Canvas, acesse a etapa **Summary** do criador de Canvas e selecione **Resume Canvas**. Quando reativado, quaisquer mensagens previamente paradas serão enviadas conforme agendado&#8212;desde que o horário agendado ainda não tenha passado.

## Práticas recomendadas {#best-practices}

### Monitore suas mensagens por status {#monitor-your-messages-by-status}

Você pode monitorar suas mensagens por status para revisar os detalhes de desempenho. Por exemplo, se você tem uma série de Campaigns ativas, pode avaliar o desempenho de cada Campaign com suas métricas de engajamento e fazer ajustes conforme necessário. Se, em vez disso, você tem alguns Canvas parados, pode considerar se eles devem ser retomados para envio de mensagens ou arquivados completamente.

{% alert tip %}
Procurando mais formas de se organizar? Adicione [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [tags]({{site.baseurl}}/user_guide/messaging/governance/tags) para fornecer mais contexto em uma visão rápida.
{% endalert %}

### Audite suas mensagens ativas {#audit-your-active-messages}

Ao realizar auditorias de suas Campaigns e Canvas ativos, você pode avaliar a relevância e o desempenho, além de remover ou atualizar quaisquer Campaigns e Canvas desatualizados para manter seu envio de mensagens sempre atualizado.