---
nav_title: Editar sua campanha após o lançamento
article_title: Editar sua campanha após o lançamento
page_order: 1
tool: Campaigns
page_type: reference
description: "Este artigo de referência oferece uma visão geral dos resultados de editar determinados aspectos de uma campanha após o lançamento."

---

# Editar sua campanha após o lançamento {#edit-your-campaign-after-launch}

> Este artigo oferece uma visão geral dos resultados de editar determinados aspectos de uma campanha após o lançamento.

## Interromper sua campanha {#stopping-your-campaign}

Para interromper uma campanha, abra a página **Campaign Details** e selecione **Interromper campanha**. Quando uma campanha é interrompida:

- As mensagens programadas para envio serão canceladas.
- Os testes A/B cujo teste inicial já foi enviado serão cancelados permanentemente.
- Os eventos de mensagens que já foram enviadas (por exemplo, cliques de abertura) continuarão sendo rastreados.

Para reiniciar sua campanha, selecione **Resume**. Sua campanha continuará enviando mensagens e testes A/B, mas as mensagens perdidas não serão reenviadas ou reprogramadas.

### Interromper sua campanha durante o envio {#stopping-your-campaign-during-sending}

Para campanhas com um público maior e limites de taxa, a Braze particiona e programa lotes de mensagens para envio em horários diferentes. Quando uma campanha é interrompida, os envios não são cancelados imediatamente. Em vez disso, eles são cancelados quando começam a ser executados e detectam que a campanha foi interrompida.

Por exemplo, se você iniciar uma campanha de e-mail com limite de taxa, pausá-la por algumas horas e depois retomá-la, todas as mensagens que estavam programadas para envio durante as horas de pausa serão canceladas e nunca serão enviadas. Quaisquer mensagens restantes programadas após a retomada da campanha continuarão sendo enviadas. Se a reelegibilidade estiver ativada para a campanha, os usuários poderão se tornar elegíveis para receber a campanha novamente, além de quaisquer mensagens que já estavam na fila antes da campanha ser interrompida.

## Campanhas disparadas {#triggered-campaigns}

Todas as alterações em campanhas de entrega baseada em ação e campanhas de entrega disparadas por API entram em vigor imediatamente para envios futuros.

Se essas campanhas foram disparadas, mas ainda não foram enviadas (por exemplo, uma campanha de entrega baseada em ação com uma postergação de 1 dia é editada durante o período de postergação de 1 dia), consulte as orientações a seguir para campanhas agendadas.

### Campanhas agendadas {#scheduled-campaigns}

Se você precisar fazer alterações em uma campanha após o lançamento, observe os itens a seguir ao editar sua campanha para garantir que suas alterações tenham os efeitos desejados.

### Conteúdo da mensagem {#message-content}

Qualquer alteração no conteúdo da mensagem (incluindo títulos, corpos e imagens) entra em vigor imediatamente ao salvar para todos os envios de mensagens futuros. Não é possível alterar o conteúdo de mensagens que já foram enviadas.

### Programação e público {#scheduling-and-audience}

Se você editar o horário de envio programado ou o público da sua campanha, essas alterações serão refletidas na campanha imediatamente.

#### Considerações {#considerations}

Se sua campanha usa Intelligent Timing ou entrega por fuso horário local, as edições no horário de envio programado não serão refletidas se a edição for feita dentro de 24 horas do horário de envio original. Isso acontece porque:

- **Intelligent Timing:** a Braze começa a calcular o horário ideal de envio à meia-noite no horário de Samoa. Se esse horário já passou, a mensagem já terá começado a ser processada. Para saber mais, consulte [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/).
- **Entrega por fuso horário local:** editar uma campanha de fuso horário local que está programada para menos de 24 horas não alterará a programação da mensagem. Para saber mais, consulte [Como programar uma campanha de fuso horário local?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign).

### Taxa de envio {#send-rate}

Ao usar um limite de taxa de envio, a Braze "programa" suas mensagens em intervalos de tempo com granularidade de minutos. Portanto, se você quiser alterar a taxa de envio de mensagens, siga o processo abaixo para fazer alterações imediatas.

#### Pausar campanhas com limite de velocidade de entrega {#pausing-campaigns-with-delivery-speed-rate-limiting}

Quando você pausa uma campanha que usa [limite de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting), a Braze distribui os envios em intervalos baseados em minutos. **Resume** não reenvia mensagens de intervalos que foram cancelados enquanto a campanha estava pausada.

Mensagens com limite de taxa são canceladas somente se a campanha ainda estiver pausada quando o horário de envio programado chegar. Se uma mensagem será enviada após a retomada depende de quando você pausou a campanha e por quanto tempo ela ficou pausada.

Por exemplo:

1. Você pausa a campanha às 13h.
2. Uma mensagem com limite de taxa está programada para envio às 13h05.
   - Se você retomar antes das 13h05, a mensagem será enviada.
   - Se você retomar após as 13h05, a mensagem será cancelada durante a pausa e não será enviada.

Se alguns usuários não receberam mensagens porque a campanha estava pausada durante o intervalo programado deles, duplique a campanha e direcione apenas esses usuários, em vez de depender de **Resume** para entregar as mensagens perdidas.

## Fazer alterações imediatas {#making-immediate-changes}

Se você precisar que as alterações entrem em vigor imediatamente, faça o seguinte:

1. Interrompa a campanha afetada.
2. Duplique a campanha.
3. Faça as edições na campanha duplicada.

{% alert important %}
Isso redefine a elegibilidade para pessoas que já receberam a campanha original. Portanto, pode ser necessário filtrar a campanha duplicada para pessoas que não receberam a original.
{% endalert %}

## Salvar rascunhos de campanhas ativas {#campaign-drafts}

Os rascunhos são ótimos para fazer alterações em grande escala em campanhas ativas. Ao criar um rascunho, você pode testar as alterações planejadas antes do próximo lançamento.

{% alert note %}
Uma campanha só pode ter um rascunho por vez. Além disso, a análise de dados não está disponível, pois as alterações do rascunho ainda não foram lançadas.
{% endalert %}

Para criar um rascunho, faça o seguinte:

1. Acesse sua campanha ativa.
2. Faça suas alterações.
3. Selecione **Salvar como rascunho**. Observe que, após criar um rascunho, você não poderá editar a campanha ativa até lançar ou descartar o rascunho.

![Um rascunho de uma campanha ativa com a opção de visualizar a campanha ativa.]({% image_buster /assets/img/campaign_draft.png %})

Enquanto faz edições no rascunho, você também pode consultar a campanha ativa no cabeçalho do rascunho da campanha ou no rodapé da análise de dados da campanha.

Para voltar a uma campanha ativa, selecione **Editar rascunho** na visualização de análise de dados ou na visualização da campanha ativa.

### Priorização de mensagens no app {#in-app-message-prioritization}

A prioridade de mensagens no app será atualizada imediatamente (antes do lançamento do rascunho) quando você selecionar **Definir prioridade exata** e especificar a prioridade em relação a outras campanhas ou Canvas.