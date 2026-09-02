---
nav_title: FAQ
article_title: FAQ do Canvas
page_order: 8
alias: "/canvas_v2_101/"
description: "Este artigo fornece respostas para perguntas frequentes sobre o Canvas."
tool: Canvas
toc_headers: h2
---

# Perguntas frequentes {#frequently-asked-questions}

> Este artigo fornece respostas para algumas perguntas frequentes sobre o Canvas.

## Criação e edição de Canvas {#building-and-editing-canvas}

### Quantas etapas posso incluir em um Canvas? {#how-many-steps-i-can-include-in-a-canvas}

Você pode adicionar até 200 etapas em um Canvas.

### Existem limites de tamanho para as propriedades de entrada do Canvas? {#are-there-size-limits-for-canvas-entry-properties}

Sim. O [objeto de contexto do Canvas]({{site.baseurl}}/api/objects_filters/context_object) (propriedades de entrada do Canvas) tem um tamanho máximo de 50&nbsp;KB. Mantenha as cargas úteis o menor possível dentro desse limite. Para entender como as propriedades de entrada e de evento funcionam no Canvas, consulte [Propriedades de contexto e evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties).

### Por que vejo o erro "Too many Canvas branches"? {#why-do-i-see-a-too-many-canvas-branches-error}

Esse erro aparece quando a combinação de ramificações de etapas e o tamanho do público de entrada pode causar problemas de desempenho no cluster, impedindo o envio de mensagens. Para ver as etapas de resolução — incluindo o uso de [jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), redução de ramificações ou do tamanho do público e reconstrução no Canvas Flow — consulte [Erro "Too many Canvas branches"]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#too-many-canvas-branches-error).

### Posso usar o recurso Otimizar com BrazeAI<sup>TM</sup> com reelegibilidade em um Canvas? {#can-i-use-optimize-with-brazeai-with-re-eligibility-in-a-canvas}

Sim. Os Canvas podem usar [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai) quando a reelegibilidade está ativada. A Braze não pode garantir a mesma variante ao reentrar, pois a alocação muda ao longo do tempo. As Campaigns exigem uma janela de reelegibilidade de 24 horas ou mais quando **Otimizar com BrazeAI<sup>TM</sup>** está ativado.

### Qual é a diferença entre um componente e uma etapa? {#whats-the-difference-between-a-component-and-a-step}

Um [componente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about) é uma parte individual do seu Canvas que você pode usar para determinar a eficácia do seu Canvas. Os componentes podem incluir ações como dividir a jornada do usuário, adicionar uma postergação e até testar múltiplas jornadas do Canvas. Uma etapa no Canvas refere-se à jornada personalizada do usuário nas ramificações do seu Canvas. Essencialmente, seu Canvas é composto de componentes individuais que criam etapas para a jornada do usuário.

### Posso lançar um Canvas com etapas desconectadas? {#can-i-launch-a-canvas-with-disconnected-steps}

Sim. Você também pode salvar Canvas após o lançamento com etapas desconectadas.

### Para onde os usuários vão quando chegam a uma etapa desconectada? {#where-do-users-go-when-theyve-reached-a-disconnected-step}

Se um usuário estiver em uma etapa desconectada do seu fluxo de trabalho do Canvas, ele avançará para a etapa subsequente, se houver uma, e a configuração da etapa determinará como o usuário deve avançar. Isso é intencional para permitir que os usuários façam alterações nas etapas sem precisar conectá-las diretamente ao restante do Canvas. Isso também oferece espaço para testes antes de entrar em operação imediatamente, permitindo efetivamente salvar um rascunho.

Recomendamos verificar a visualização de análise de dados para usuários pendentes em uma etapa do Canvas antes de desconectar uma etapa.

### O que acontece se o público e o horário de envio forem idênticos para um Canvas com uma variante, mas com múltiplas ramificações? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

Enfileiramos um job para cada etapa — eles são executados aproximadamente ao mesmo tempo, e um deles "vence". Na prática, isso pode ser distribuído de forma relativamente uniforme, mas é provável que haja pelo menos uma pequena tendência para a etapa que foi criada primeiro.

Além disso, não podemos garantir exatamente como essa distribuição será. Se você quiser uma divisão uniforme, adicione um filtro de [números de bucket aleatórios]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers).

### Como os públicos do Canvas são avaliados? {#how-are-canvas-audiences-evaluated}

Por padrão, os filtros e Segments para etapas completas no Canvas são verificados no momento do envio. A etapa de divisão de decisão realiza uma avaliação logo após receber uma etapa anterior (ou antes de uma postergação).

### Quando um evento de exceção é disparado? {#when-does-an-exception-event-trigger}

Os eventos de exceção só são disparados enquanto o usuário está aguardando para receber o componente do Canvas ao qual ele está associado. Se um usuário realizar uma ação antecipadamente, o evento de exceção não será disparado. Se você quiser excluir usuários que já realizaram determinado evento, use [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Como a edição de um Canvas afeta os usuários que já estão no Canvas? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

Se você editar algumas das etapas de um Canvas com múltiplas etapas, os usuários que já estavam no público, mas que ainda não receberam as etapas, receberão a versão atualizada da mensagem. Isso só acontecerá se eles ainda não tiverem sido avaliados para a etapa.

Para saber mais sobre o que você pode editar após o lançamento, consulte [Alterando seu Canvas após o lançamento]({{site.baseurl}}/post-launch_edits).

### O que acontece quando você interrompe um Canvas? {#what-happens-when-you-stop-a-canvas}

Quando você interrompe um Canvas, o seguinte se aplica:

- Os usuários serão impedidos de entrar no Canvas.
- Nenhuma mensagem adicional será enviada, independentemente de onde o usuário esteja no fluxo.
- **Exceção:** Canvas com e-mails não serão interrompidos imediatamente. Depois que as solicitações de envio chegam ao SendGrid, não há como impedir que sejam entregues ao usuário.

### Devo criar um único Canvas ou Canvas separados por ciclo de vida do usuário? {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

Dependendo do que você deseja alcançar com o seu Canvas, pode ser necessário adotar abordagens diferentes na forma como você constrói a jornada do usuário. A flexibilidade do Canvas permite que você mapeie jornadas de usuários para qualquer estágio do ciclo de vida. Confira nossos [modelos de Canvas da Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) para vários exemplos de abordagens simplificadas para criar jornadas de usuário eficazes.

## Mensagens e entrega {#messages-and-delivery}

### Quando as mensagens no app em um Canvas são enviadas? {#when-are-in-app-messages-in-canvas-sent}

As mensagens no app são enviadas no início da próxima sessão. Isso significa que, se o usuário entrar na etapa do Canvas antes de o Canvas ser interrompido, ele ainda receberá a mensagem no app no próximo início de sessão, desde que a mensagem no app ainda não tenha expirado.

É possível que um usuário inicie uma sessão antes de o Canvas ser interrompido, mas não veja a mensagem no app imediatamente. Isso pode acontecer se a mensagem no app for disparada por um evento personalizado ou estiver com atraso. Ou seja, é possível que um usuário registre uma impressão de mensagem no app e "receba" a mensagem no app após o Canvas ser interrompido. No entanto, o usuário precisaria ter iniciado a sessão antes de o Canvas ser interrompido, mas **depois** de ter recebido a etapa do Canvas.

{% alert note %}
Interromper um Canvas não fará com que os usuários que estão aguardando para receber mensagens saiam da jornada do usuário. Se você reativar o Canvas e os usuários ainda estiverem aguardando a mensagem, eles a receberão (a menos que o horário em que a mensagem deveria ter sido enviada já tenha passado — nesse caso, eles não a receberão).
{% endalert %}

### Por que um Canvas pode mostrar zero envios mesmo quando há impressões registradas? {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

Se _Mensagens enviadas_ for sempre zero para um Canvas que contém uma etapa de mensagem no app, isso acontece porque a entrega de mensagens no app funciona de forma diferente dos outros canais de envio de mensagens.

As mensagens no app são "puxadas" pelo SDK, em vez de serem "enviadas" pela Braze. As mensagens no app para usuários elegíveis são entregues automaticamente no início da sessão e "aguardam" o evento-gatilho antes de serem exibidas. Como os usuários elegíveis recebem a mensagem quando iniciam uma sessão, a Braze não registra isso como um evento de envio. Quando os usuários executam o evento-gatilho, a mensagem é exibida e a Braze registra uma impressão e marca a etapa do Canvas (ou Campaign) como recebida no perfil do usuário. Consequentemente, o total de _Envios_ é zero para mensagens no app.

### Por que os usuários não receberam minha mensagem no app após uma postergação longa ou ramificação? {#why-didnt-users-receive-my-in-app-message-after-a-long-delay-or-branch}

Após a conclusão de etapas de [Postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) upstream e verificações de público, os usuários se tornam elegíveis para uma mensagem no app apenas quando alcançam a etapa de Mensagem. Se a mensagem expirar em uma data do calendário ou em uma janela curta de **duração após a etapa estar disponível**, os usuários em ramificações mais lentas podem chegar após a expiração e nunca ver a mensagem. Alinhe a expiração com os atrasos mais longos e realistas do caminho. Para saber mais e ver exemplos, consulte [Expiração de mensagens no app]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#in-app-message-expiration).

### Por que vejo "Canvas Entry Properties may not be used in In-App Messages."? {#why-do-i-see-canvas-entry-properties-may-not-be-used-in-in-app-messages}

Essa mensagem aparece quando a personalização faz referência a campos que as mensagens no app não conseguem resolver no Canvas. Use o objeto `context` conforme descrito em [Propriedades de contexto e evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) e [Etapa de mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step). O namespace Liquid legado `canvas_entry_properties` tem restrições diferentes do `context`. Se você precisar que os valores persistam em várias etapas, revise as [propriedades persistentes no editor de Canvas original]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties) com a sua equipe da Braze. Os valores armazenados são apagados quando um usuário sai do Canvas antes de o dispositivo baixar a carga útil da mensagem no app.

### Onde posso encontrar os cliques de botão para mensagens no app de arrastar e soltar no Canvas? {#where-can-i-find-button-clicks-for-drag-and-drop-in-app-messages-in-canvas}

As métricas de nível de botão para mensagens no app de arrastar e soltar aparecem no cartão de análise de dados da etapa **Mensagem** em **Detalhes do Canvas**, e não apenas no resumo de alto nível do Canvas. Abra o Canvas, selecione a etapa de Mensagem e analise o engajamento da mensagem no app ali. Para conceitos de relatórios, consulte [Medir e testar com análise de dados do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

### Posso agendar horários de envio diferentes para cada variante na mesma etapa de Mensagem do Canvas ou envio multivariante? {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

Não. As variantes na mesma configuração multivariante ou etapa de Mensagem compartilham um único cronograma de entrega. Não é possível atribuir uma variante para envio às 18h e outra às 19h para o mesmo envio agendado.

Para escalonar envios ou usar horários diferentes por jornada, experimente os seguintes métodos:

- Separar etapas de Mensagem com etapas de Postergação entre elas para que cada mensagem tenha seu próprio cronograma.
- Usar ramificações ou uma etapa de [jornada experimental]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que os usuários sigam jornadas com horários diferentes.
- Separar em Campaigns se o caso de uso não precisar permanecer dentro de um único Canvas.

Para conceitos de testes multivariantes e A/B em Campaigns, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

### O que acontece se um usuário estiver com limite de frequência global em uma etapa de Mensagem do Canvas? {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

Ele não recebe aquele envio para o canal limitado, mas as etapas de Mensagem ainda avançam os usuários quando uma mensagem não é enviada por causa do limite de frequência global. Para os casos de avanço passo a passo, consulte [Como os usuários avançam]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance). O limite de frequência global sozinho não faz com que os usuários saiam de um Canvas; esse comportamento é separado das **Validações de entrega** em uma etapa de Mensagem. Para saber mais, consulte [Limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Por que os envios são menores do que o tamanho estimado do público? {#why-are-sends-lower-than-the-estimated-audience-size}

Os envios podem ser menores do que o **Público estimado** por muitas das mesmas razões que em [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size), incluindo limites de frequência, filtros rigorosos de dispositivo ou navegador, janelas de reelegibilidade, limitação de taxa e exclusões no nível do canal (por exemplo, alcançabilidade de push ou verificações de inscrição e entregabilidade de e-mail).

Fatores específicos do Canvas também se aplicam:

- **Entrada baseada em ação ou disparada por API:** Os usuários só entram (e recebem etapas) após executarem o comportamento de entrada, portanto os envios realizados ficam atrás da estimativa inicial até que essas ações ocorram.
- **Jornadas do público:** Os usuários são direcionados para a ramificação de maior prioridade para a qual se qualificam, então ramificações posteriores podem receber menos usuários do que uma contagem simples de Segment sugere.
- **Verificações de público e horário de envio:** Etapas completas reavaliam os filtros no momento do envio, a menos que você configure de outra forma. Usuários que se qualificaram quando o Canvas foi criado podem sair antes de uma mensagem ser enviada.
- **Grupos de controle:** Grupos de controle globais ou do Canvas retêm uma parcela dos entrantes do envio de mensagens.
- **Horário de silêncio e postergações:** As mensagens podem ser retidas ou reagendadas, deslocando os envios para fora da janela de relatório que você está visualizando.
- **Limites máximos de entrada ou público:** Limites de entrada ou envio interrompem usuários adicionais mesmo quando o Segment subjacente é maior.
- **Janela de relatório:** O intervalo de análise de dados pode não incluir todos os envios que você está comparando com a estimativa.

### Por que o público estimado e a contagem de usuários do Canvas não coincidem? {#why-dont-estimated-audience-and-canvas-user-counts-match}

O **Público estimado** reflete quem corresponde ao seu Segment e filtros de entrada no momento em que a estimativa é executada. Após esse momento, entradas com postergação ou baseadas em ação, reelegibilidade, disparos por API ou roteamento de ramificações podem aumentar o número de perfis que passam pela jornada em comparação com o snapshot. Os usuários também podem sair quando os filtros no momento do envio falham, o que reduz as entradas ou envios realizados. Compare os horários, limites e configurações de avaliação junto com [Por que os envios são menores do que o tamanho estimado do público?](#why-are-sends-lower-than-the-estimated-audience-size).

### Por que _Destinatários únicos_ é maior do que o número de usuários que eu direcionei? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

_Destinatários únicos_ pode ser maior do que o público esperado porque a Braze rastreia **destinatários únicos diários** para relatórios de Canvas e Campaign. Isso possibilita uma atribuição de conversão precisa a cada vez que um usuário recebe uma mensagem na jornada.

Por exemplo, se um usuário recebe uma etapa do Canvas na segunda-feira e novamente na sexta-feira e converte após cada envio, a Braze pode contar duas linhas de destinatários e duas conversões no escopo. Com entradas recorrentes ou reelegibilidade, o mesmo pequeno conjunto de perfis pode produzir múltiplos _Destinatários únicos_ ao longo de vários dias.

### Por que meu Canvas está com taxas de envio mais baixas? {#why-is-my-canvas-experiencing-lower-send-rates}

Se você perceber que o seu Canvas agendado diário envia para menos usuários ao longo do tempo, verifique o seguinte:

- **Verifique se a reelegibilidade está ativada:** Sem reelegibilidade, a Braze insere cada usuário no Canvas apenas uma vez. Em Canvas agendados diários, apenas os usuários que correspondem ao público e ainda não entraram no Canvas são elegíveis para cada entrada. À medida que mais usuários entram, cada entrada posterior tem menos usuários elegíveis, então o volume de entradas diminui.
- **Verifique se o público tem membros fixos:** Públicos construídos a partir de uma lista fixa de usuários (como uma [importação de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) usada como filtro de Segment) não ganham novos membros automaticamente. Sem novos entrantes, o volume de entradas não consegue se recuperar à medida que os usuários entram no Canvas.

Para [limites de taxa de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) e outros fatores que reduzem os envios para uma única ocorrência, consulte [Por que os envios são menores do que o tamanho estimado do público?](#why-are-sends-lower-than-the-estimated-audience-size).

### Por que um Segment pequeno de grupo de controle mostra mudanças no histórico de membros? {#why-does-a-small-control-group-segment-show-changes-in-historical-membership}

Os gráficos de histórico de membros usam amostras estimadas, então Segments pequenos — incluindo Segments de [grupo de controle global]({{site.baseurl}}/user_guide/audience/global_control_group) — podem mostrar variações diárias mesmo quando o público subjacente está estável. Para saber como as estimativas funcionam e por que os gráficos podem flutuar, consulte [Visualizar o tamanho histórico de membros do Segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#viewing-historical-segment-membership-size).

## Análise de dados e conversões {#analytics-and-conversions}

### Como o dashboard de conversões atribui conversões de Canvas? {#how-does-the-conversions-dashboard-attribute-canvas-conversions}

O [dashboard de conversões]({{site.baseurl}}/user_guide/analytics/dashboards/conversions) atribui conversões de Canvas com base no [método de atribuição]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods) que você seleciona (por exemplo, **Upon Receipt**, **Upon Send**, **Upon Open** ou **Upon Click**). Para que um usuário apareça no relatório, ele precisa entrar no Canvas ou Campaign, registrar o método de atribuição selecionado e realizar o evento de conversão dentro das configurações do seu relatório.

Para regras de conversão no nível de etapa e no nível de variante na análise de Canvas, consulte [Como as conversões de usuários são rastreadas em um Canvas?](#how-are-user-conversions-tracked-in-a-canvas).

### Como as conversões de usuários são rastreadas em um Canvas? {#how-are-user-conversions-tracked-in-a-canvas}

Um usuário só pode converter uma vez por entrada no Canvas. As conversões são atribuídas à mensagem mais recente recebida pelo usuário naquela entrada. O bloco de resumo no início de um Canvas reflete todas as conversões realizadas pelos usuários naquela jornada, independentemente de terem recebido uma mensagem ou não. Cada etapa subsequente mostrará apenas as conversões que ocorreram enquanto aquela era a etapa mais recente que o usuário recebeu.

{% alert note %}
Quando um usuário reentra em um Canvas, os eventos de conversão são rastreados apenas para a entrada mais recente. Os eventos de conversão não são registrados para entradas anteriores, mesmo que o evento de conversão seja preenchido retroativamente.
{% endalert %}

{% details Expandir para ver exemplos %}

**Exemplo 1**

Há uma jornada de Canvas com 10 notificações por push e o evento de conversão é "início de sessão" ("Abre o app"):

- O Usuário A abre o app após entrar, mas antes de receber a primeira mensagem.
- O Usuário B abre o app após cada notificação por push.

**Resultado:** O resumo mostrará duas conversões, enquanto as etapas individuais mostrarão uma conversão na primeira etapa e zero em todas as etapas subsequentes.

{% alert note %}
Se o horário de silêncio estiver ativo quando o evento de conversão ocorrer, as mesmas regras se aplicam.
{% endalert %}

**Exemplo 2**

Há um Canvas de uma única etapa com horário de silêncio ativado:

1. O usuário entra no Canvas.
2. A primeira etapa não tem postergação, mas está dentro do horário de silêncio configurado, então a mensagem é suprimida.
3. O usuário realiza o evento de conversão.

**Resultado:** O usuário será contado como convertido na variante geral do Canvas, mas não na etapa, pois não recebeu a etapa.

{% enddetails %}

### Qual é a diferença entre os diferentes tipos de taxa de conversão? {#whats-the-difference-between-the-different-conversion-rate-types}

- O total de conversões do Canvas reflete quantos usuários únicos completaram um evento de conversão, não quantas conversões cada um completou.
- A taxa de conversão da variante ou o bloco de resumo no início de um Canvas reflete todas as conversões realizadas pelos usuários naquela jornada, independentemente de terem recebido uma mensagem ou não, como um total agregado.
- A taxa de conversão da etapa reflete quantos indivíduos receberam aquela etapa de mensagem e completaram qualquer um dos eventos de conversão definidos.

### Por que a taxa de conversão da minha etapa de Canvas não é igual à taxa de conversão total da variante do Canvas? {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

É comum que o total de conversões de uma variante de Canvas seja maior que a soma dos totais de suas etapas. Isso ocorre porque um usuário pode realizar um evento de conversão para uma variante assim que entra nela. No entanto, esse mesmo evento de conversão não conta para uma etapa de Canvas. Portanto, qualquer usuário que entre no Canvas e realize o evento de conversão antes de receber a primeira etapa do Canvas é contado no total de conversão da variante, mas não no total da etapa. O mesmo vale para um usuário que entra no Canvas, mas sai antes de receber qualquer etapa.

Observe que também é possível que um usuário entre em uma variante, não receba nenhuma mensagem de uma etapa e, mesmo assim, converta. Nesse caso, a conversão não é registrada no nível da etapa. No entanto, como o usuário tecnicamente converteu, a conversão é registrada no nível do Canvas.

### Como posso confirmar se meus usuários receberam um Canvas disparado por API? {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

Você pode [criar um Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) usando um filtro de Canvas para confirmar se os usuários entraram no Canvas ou receberam uma etapa específica do Canvas. Por exemplo, use um filtro de entrada no Canvas se quiser confirmar que os usuários entraram no Canvas disparado por API, ou um filtro de etapa recebida se quiser confirmar que receberam uma mensagem do Canvas. Depois, use o [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) para exportar os usuários desse Segment.

### Posso excluir um Canvas? {#can-i-delete-a-canvas}

Não, mas você pode [arquivar um Canvas]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Como posso retomar um Canvas ou Campaign arquivado? {#how-do-i-resume-an-archived-canvas-or-campaign}

Mensagens arquivadas não são enviadas até que você as retorne para um estado editável. [Desarquive]({{site.baseurl}}/user_guide/messaging/governance/archiving#unarchiving) o Campaign ou Canvas, defina o cronograma de entrada ou horário de envio para uma janela futura (ou duplique a jornada se precisar de uma cópia limpa) e, em seguida, selecione **Retomar** ou lance conforme necessário. Consulte [Arquivar Campaigns e Canvas]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Por que meu Canvas não salva quando nenhum erro aparece? {#why-doesnt-my-canvas-save-when-no-error-appears}

Filtros de **Atributo personalizado** vazios no público ou nos filtros de nível de etapa podem bloquear o salvamento sem uma mensagem de validação detalhada. Abra cada cartão de filtro, remova regras de atributo personalizado incompletas ou insira o nome e o valor do atributo e, em seguida, selecione **Salvar** novamente.

### Por que uma tag desapareceu do meu Canvas ou Campaign? {#why-did-a-tag-disappear-from-my-canvas-or-campaign}

Quando uma [tag]({{site.baseurl}}/user_guide/messaging/governance/tags) é excluída do seu espaço de trabalho, a Braze a remove de todos os Campaigns e Canvas que faziam referência a ela. Essa limpeza nem sempre gera uma linha própria no registro de alterações do Canvas.

### Como posso visualizar a análise de dados de cada um dos meus componentes de Canvas? {#how-can-i-view-analytics-for-each-of-my-canvas-components}

Para visualizar a análise de dados de um componente de Canvas, acesse seu Canvas e role a página **Canvas Details** para baixo. Aqui, você pode ver a análise de dados de cada componente. Confira [Análise de dados do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics) para mais detalhes.

### Quando o engajamento de uma etapa de Canvas fica visível no perfil de um usuário? {#when-is-engagement-from-a-canvas-step-visible-on-a-user-profile}

Filtros como `Received Message from Canvas Step` são atualizados após a Braze registrar o evento correspondente de envio, recebimento ou engajamento para aquela etapa. In-App Messages podem registrar impressões separadamente das métricas do tipo envio. Consulte [Por que um Canvas pode mostrar zero envios mesmo quando impressões são registradas?](#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged). Esses mesmos eventos aparecem nas métricas da etapa em **Canvas Details**.

### Ao analisar o número de usuários únicos, a análise de dados do Canvas ou o segmentador é mais preciso? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

O segmentador é uma estatística mais precisa para dados de usuários únicos em comparação com as estatísticas de Canvas ou Campaign. Isso ocorre porque as estatísticas de Canvas e Campaign são números que a Braze incrementa quando algo acontece, o que significa que há variáveis que podem resultar em um número diferente do segmentador. Por exemplo, os usuários podem converter mais de uma vez em um Canvas ou Campaign.

### Por que o número de usuários que entram em um Canvas não corresponde ao número esperado? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

O número de usuários que entram em um Canvas pode diferir do número esperado por causa de como os públicos e gatilhos são avaliados. Na Braze, o público é avaliado antes do gatilho (a menos que se use um gatilho de [alteração de atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Isso faz com que os usuários saiam do Canvas se não fizerem parte do público selecionado antes que quaisquer ações de gatilho sejam avaliadas.

### O que acontece com usuários anônimos durante a jornada deles no Canvas? {#what-happens-to-anonymous-users-during-their-canvas-journey}

Embora usuários anônimos possam entrar e sair de Canvas, as ações deles não estão associadas a um perfil de usuário específico até que sejam identificados, então as interações podem não ser totalmente rastreadas na sua análise de dados. Você pode usar o [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) para gerar um relatório dessas métricas.

{% alert tip %}
Para obter mais assistência com a solução de problemas do Canvas, entre em contato com o suporte da Braze dentro de 30 dias após a ocorrência do problema, pois temos apenas os últimos 30 dias de registros de diagnóstico.
{% endalert %}

### Posso excluir de um Campaign ou Segment os usuários que estão atualmente em uma jornada de Canvas? {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

Use [filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) como `Entered Canvas Variation`, `In Canvas Control Group` ou `Received Message from Canvas Step` para direcionar usuários com base na entrada no Canvas, atribuição de variante ou engajamento com etapas. Esses filtros avaliam o histórico de entrada e as interações — eles não indicam se um usuário ainda está progredindo por uma jornada ativa.

Para incluir ou excluir usuários com base na participação ativa no Canvas, adicione etapas de [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) na entrada e na saída do Canvas para definir e limpar atributos personalizados e, em seguida, filtre por esses atributos em Campaigns ou Segments.

## Segmentação {#segmentation}

### Qual é a diferença entre "Has not entered Canvas variation" e "Is not in Canvas control group"? {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

Consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) para ver as definições completas dos filtros.

#### Has not entered Canvas variation {#has-not-entered-canvas-variation}

O usuário nunca entrou em uma jornada de variante de um Canvas específico. Todos os usuários que não estão no grupo de controle são incluídos, independentemente de terem entrado no Canvas. Isso inclui usuários que entraram em outra variante e usuários que não entraram em nenhuma variante.

#### Is not in Canvas control group {#is-not-in-canvas-control-group}

O usuário entrou no Canvas, mas não está no grupo de controle e, consequentemente, recebeu uma variante. Isso inclui apenas os usuários que entraram no Canvas.

A atribuição de variante ocorre na entrada do Canvas. Se um usuário não tiver entrado em um Canvas, ele não será atribuído a nenhuma variante. Em outras palavras, ele não estará no grupo de controle nem em uma variante.

## Editor original do Canvas {#original-canvas-editor}

{% details Expandir para ver as perguntas frequentes do editor original do Canvas %}

### Como converto um Canvas existente do editor original para o editor atual? {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

Você pode [clonar seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases). Isso cria uma cópia do seu Canvas original no fluxo de trabalho mais atual do Canvas.

### Quais são as principais diferenças entre os editores atual e original do Canvas? {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### Barra de ferramentas de componentes do Canvas {#canvas-component-toolbar}

Anteriormente, com o editor original do Canvas, uma etapa completa era adicionada por padrão sempre que você criava qualquer etapa na jornada do usuário. Essas etapas completas foram substituídas por diferentes componentes do Canvas, o que oferece o benefício de maior visibilidade e personalização na sua experiência de edição. Você pode ver imediatamente todos os componentes do Canvas na barra de ferramentas de etapas do Canvas.

#### Comportamento das etapas {#step-behavior}

Anteriormente, cada etapa completa incluía informações como configurações de postergação e agendamento, eventos de exceção, filtros de público, configuração de mensagem e opções de avanço de mensagem, tudo em um único componente. No editor atual, essas são configurações separadas para tornar sua experiência de criação do Canvas mais personalizável, e isso introduz algumas diferenças na funcionalidade.

#### Avanço do componente de mensagem {#message-component-advancement}

Os [componentes de mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) avançam todos os usuários que entram na etapa. Não há necessidade de especificar o comportamento de avanço da mensagem, o que torna a configuração da etapa geral mais simples. Se você quiser implementar a opção **Avançar quando a mensagem for enviada**, adicione um componente separado de jornadas do público para filtrar os usuários que não receberam a etapa anterior.

#### Comportamento de postergação "em" {#delay-in-behavior}

Os [componentes de postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) aguardam todo o tempo de postergação antes de prosseguir para a próxima etapa.

Digamos que em 12 de abril temos um componente de postergação em que a postergação está configurada para enviar o usuário à próxima etapa em um dia às 14h. Um usuário entra no componente às 14h01 do dia 13 de abril.
- No fluxo de trabalho original, o usuário prosseguiria para a próxima etapa às 14h do dia 14 de abril, o que é menos de um dia a partir do horário de entrada.
- No editor atual, o usuário prosseguiria para a próxima etapa às 14h do dia 15 de abril. Note que é o mesmo horário, mas mais de um dia a partir do horário de entrada.

#### Comportamento do Intelligent Timing {#intelligent-timing-behavior}

Como o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) é armazenado no componente de mensagem, as postergações serão aplicadas antes dos cálculos do Intelligent Timing. Isso significa que, dependendo de quando um usuário entra no componente, ele pode receber a mensagem mais tarde do que receberia em um Canvas criado com o fluxo de trabalho original do Canvas.

Digamos que sua postergação está configurada para 2 dias, o Intelligent Timing está ativado e determinou que o melhor horário para enviar sua mensagem é às 14h. Um usuário entra na etapa de postergação às 14h01.
- **Fluxo de trabalho atual:** Serão necessárias 48 horas para a postergação passar, então o usuário recebe a mensagem no terceiro dia às 14h.
- **Fluxo de trabalho original:** O usuário recebe a mensagem no segundo dia às 14h.

Note que, se o Intelligent Timing estiver ativado, a mensagem será enviada dentro de 24 horas após o usuário entrar no componente de mensagem, no horário inteligente identificado (mesmo que nenhum componente de postergação esteja envolvido).

#### Eventos de exceção {#exception-events}

##### Horário de silêncio {#quiet-hours}

O evento de exceção é aplicado usando jornadas de ação, que são separadas das etapas de mensagem. O horário de silêncio é aplicado no componente de mensagem. Isso significa que, se um usuário já passou pela jornada de ação (e não foi excluído pelo evento de exceção), e então encontra o horário de silêncio ao chegar ao componente de mensagem, e o Canvas foi configurado para reenviar a mensagem após o período de horário de silêncio, o evento de exceção não será mais aplicado. Note que esse caso de uso não é comum.

Para Segments e filtros, a etapa de mensagem tem validações de entrega que permitem aos usuários configurar Segments e filtros adicionais que são validados no momento do envio. Isso evita o caso extremo mencionado do horário de silêncio.

##### Configuração de agendamento "em" ou "no próximo" {#in-or-on-the-next-schedule-setting}

Eventos de exceção são criados usando jornadas de ação. As jornadas de ação suportam apenas "após uma janela de tempo de X" e não "em X tempo" ou "no próximo X tempo".

{% enddetails %}

### O que devo incluir ao enviar um ticket de suporte para um erro "Request Timed Out"? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Se você encontrar um erro "Request Timed Out" ao editar um Canvas e precisar entrar em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support), inclua as seguintes informações para ajudar a acelerar a resolução:

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='canvas' %}

## Entrega e solução de problemas do Canvas {#canvas-delivery-and-troubleshooting}

### Usuários órfãos são elegíveis para receber mensagens do Canvas? {#are-orphaned-users-eligible-to-receive-canvas-messages}

Não. [Usuários órfãos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users) não são elegíveis para receber mensagens. Se um perfil é órfão enquanto um usuário está em uma jornada do Canvas, ele sai silenciosamente do fluxo. A análise de dados nem sempre mostra um evento **Exited** para essa saída, e o resumo do fluxo de trabalho pode incluir um `partial_update_token` sem `exited_date` ou `exit_reason`.

Para saber mais sobre mesclagens e perfis órfãos, consulte [Mesclar usuários duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

### Se eu parar um Canvas ou uma Campaign ativa, as mensagens já enviadas ao provedor de serviços de e-mail ainda serão entregues? {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

Sim. Depois que a Braze envia uma solicitação ao seu provedor de serviços de e-mail (ESP), a Braze não pode cancelar esse envio. Parar um Canvas ou uma Campaign impede novas solicitações de envio, mas as mensagens já entregues ao ESP ainda podem ser enviadas e incrementar as contagens de envio conforme o ESP as processa.

Esse é o mesmo comportamento descrito em [parar um Canvas](#what-happens-when-you-stop-a-canvas): envios de e-mail em andamento não são interrompidos imediatamente.

### Como posso confirmar que uma etapa de webhook do Canvas foi disparada sem conteúdo visível ao usuário? {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

A Braze rastreia **Envios** de webhook e os resultados de entrega relacionados para etapas de [Webhook]({{site.baseurl}}/user_guide/channels/webhooks) em Campaigns e Canvas. Use a análise de dados da etapa, o [Relatório de webhooks]({{site.baseurl}}/user_guide/channels/webhooks/reporting) ou eventos de webhook do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para confirmar que a etapa foi executada. Os logs de solicitação do seu endpoint fornecem confirmação adicional quando você precisa de prova de recebimento no lado do servidor.

A Braze não inclui um pixel de rastreamento invisível nativo para etapas de webhook. Use as métricas de webhook da Braze e os logs do seu endpoint em vez de solicitações de imagem de um pixel personalizadas.

### Por que minha etapa de webhook não tem campo de corpo? {#why-does-my-webhook-step-have-no-body-field}

Etapas de webhook usam um corpo de solicitação para `POST`, `PUT`, `PATCH` e `DELETE`. Se você alternar o método para `GET`, a Braze remove o campo de corpo porque solicitações GET não suportam corpo de solicitação. Volte para um método que suporte corpo se precisar enviar JSON ou dados de formulário. Para saber mais sobre métodos, consulte [Criar um webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#http-method).

### Como uso o spacer.gif em uma etapa de webhook? {#how-do-i-use-spacergif-in-a-webhook-step}

A Braze hospeda uma imagem de espaço reservado `spacer.gif` em `cdn.braze.com` e `braze-images.com`. Algumas equipes apontam a URL de um webhook para essa imagem quando uma etapa precisa ser disparada sem chamar um endpoint externo. Etapas padrão de webhook devem chamar um endpoint real. Use o [relatório de webhooks]({{site.baseurl}}/user_guide/channels/webhooks/reporting) e os logs do seu endpoint para confirmar a entrega, conforme descrito em [Como posso confirmar que uma etapa de webhook do Canvas foi disparada sem conteúdo visível ao usuário?](#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content).

### Por que meu Canvas não carrega com o erro "invalid next-step-id"? {#why-wont-my-canvas-load-with-an-invalid-next-step-id-error}

Esse erro no console significa que pelo menos uma etapa aponta para uma próxima etapa ausente ou inválida — por exemplo, após uma exclusão parcial, clonagem ou importação. Abra o Canvas no editor, reconecte as etapas órfãs ou remova etapas que não têm mais um caminho válido adiante. Se o Canvas ainda não carregar, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) informando o ID do Canvas e uma captura de tela do erro no console.

### Por que o timestamp de conversão de um Canvas no Currents difere da minha análise de dados do Canvas? {#why-does-a-canvas-conversion-timestamp-in-currents-differ-from-my-canvas-analytics}

O Currents registra conversões do Canvas como eventos [`users.canvas.Conversion`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-conversion-events). O `time` do evento é quando o evento de conversão ocorreu. O campo `conversion_behavior` nesse evento descreve a definição de conversão (tipo e janela). A análise de dados do Canvas também pode agregar conversões em relação à entrada no Canvas dentro da janela de conversão. Ao reconciliar exportações, compare o `time` do Currents com o timestamp do evento de conversão e as configurações da janela de conversão do seu Canvas.

### Por que `canvas_step_name` é nulo no Currents? {#why-is-canvas_step_name-null-in-currents}

Campos de nome de Campaign e Canvas, como `canvas_step_name`, podem ser `null` quando um evento do Currents é enviado antes que a Braze termine de propagar os metadados da etapa — por exemplo, após criar ou renomear uma etapa. Para saber mais, consulte [Por que o nome da campanha ou da etapa do Canvas é `NULL` nos meus dados do Currents?]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data).

### Por que minha array não está atualizando em uma etapa de Atualização de Usuário? {#why-isnt-my-array-updating-in-a-user-update-step}

Verifique o JSON na sua etapa de [Atualização de Usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Atualizações de arrays e atributos aninhados precisam de caminhos e valores válidos para o atributo que você está alterando. Não inclua campos que a etapa fornece automaticamente, como o ID de usuário externo. Use a guia **Preview and test** da etapa para confirmar a carga útil antes do lançamento.

### Posso enviar mensagens do Canvas para usuários sem `external_id`? {#can-i-send-canvas-messages-to-users-without-an-external_id}

Sim, se já existir um perfil de usuário na Braze. Usuários sem `external_id` são [usuários anônimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles) e podem ser referenciados com um `braze_id` ou [alias de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases). Crie ou atualize o perfil com o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou seu SDK antes da entrada no Canvas, e então use [entrada baseada em ação ou disparada por API]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule). O direcionamento padrão do Canvas ainda exige um perfil de usuário na Braze — não é possível enviar mensagens do Canvas apenas para um endereço de e-mail sem perfil.

### Por que um usuário entrou no Canvas menos vezes do que realizou o evento-gatilho? {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

Para Canvas baseados em ação e disparados por API, a Braze deduplica eventos-gatilho para que um usuário possa entrar no máximo **uma vez por segundo** para o mesmo Canvas. Se um usuário executa o mesmo gatilho várias vezes dentro de um segundo, apenas uma entrada é processada.

Para permitir múltiplas entradas no mesmo segundo, espaçe os eventos-gatilho em pelo menos 1,1 segundo (por exemplo, quando você controla o timing dos eventos a partir do seu servidor). Para um comportamento estilo Campaign que permita múltiplos gatilhos no mesmo segundo, compare seu caso de uso com [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns) com agendamento e configurações de reelegibilidade apropriados.

### Quando os usuários são deduplicados em Canvas disparados por API? {#when-are-users-de-duplicated-in-api-triggered-canvases}

Se um usuário reentrar em um Canvas disparado por API e chegar a uma etapa de postergação onde já está enfileirado de uma entrada anterior para uma mensagem idêntica, a Braze deduplica o usuário para evitar envios duplicados. A segunda instância do Canvas é encerrada, então o número de entradas pode exceder o número de envios.

### Por que um push de teste vai para o app errado, mas os envios reais parecem corretos? {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

O **push de teste** em um perfil de usuário é entregue a todos os dispositivos habilitados para push daquele perfil. Quando vários apps estão instalados em um dispositivo, o sistema operacional geralmente entrega a notificação de teste para o primeiro app disponível, que pode não ser o app que você deseja validar.

Para confirmar o direcionamento específico do app, envie uma mensagem real ou de teste por meio de uma Campaign ou Canvas com um público restrito (por exemplo, filtrando por `external_id`) em vez de depender apenas do **push de teste** do perfil.

Para etapas de mensagem do **Canvas** com vários apps, ative **Validate audience at message send** na etapa de mensagem para que as verificações de Segment e filtro sejam executadas no momento do envio. Para saber mais, consulte [Etapa de mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

Para o comportamento geral do push de teste, consulte [Envio de mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) e [FAQ de push]({{site.baseurl}}/user_guide/channels/push/faqs).

### Como depuro Push Stories no iOS e Android? {#how-do-i-debug-push-stories-on-ios-and-android}

Comece com [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) para requisitos de configuração e criativo. Para implementação e tratamento de notificações Rich, consulte [Notificações Rich]({{site.baseurl}}/developer_guide/push_notifications/rich) e [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories) no Guia do Desenvolvedor.

### Quem recebe o e-mail "Canvas Messages Delayed 24+ Hours"? {#who-receives-the-canvas-messages-delayed-24-hours-email}

A Braze envia essa notificação quando mensagens do Canvas são atrasadas por limite de frequência por 24 horas ou mais. O e-mail é enviado para os usuários do dashboard que fizeram alterações anteriormente no Canvas afetado (com base nos logs de alteração do Canvas). Se a Braze não conseguir determinar esses destinatários, o e-mail é enviado para os **administradores da empresa** do espaço de trabalho.

### Quando um usuário para de receber mensagens após um evento de exceção? {#when-does-a-user-stop-receiving-messages-after-an-exception-event}

A Braze registra a saída assim que o evento de exceção ocorre, mas os usuários podem permanecer dentro de uma etapa até que os temporizadores terminem — mais visivelmente em etapas de postergação. O comportamento também difere entre etapas agendadas e etapas disparadas por evento. Para linhas do tempo, exemplos e nuances de análise de dados, consulte [Critérios de saída]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria).

### Por que minha etapa de jornadas de ação mostra um erro quando seleciono uma interação de alias de link? {#why-does-my-action-paths-step-show-an-error-when-i-select-a-link-alias-interaction}

Grupos de ação que usam gatilhos de interatividade de e-mail (por exemplo, **Click alias in email** ou **Clicked alias in any campaign or Canvas step**) precisam de uma etapa de mensagem que já tenha enviado a mensagem contendo aquele link. Adicione ou reordene as etapas para que o e-mail seja enviado antes que a etapa de jornadas de ação avalie o clique, ou escolha uma interação que corresponda a uma mensagem que o usuário já recebeu neste Canvas. Para a lista completa de gatilhos de interação, consulte [Entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

### Como timestamps históricos de eventos personalizados afetam Canvas e Campaigns baseados em ação? {#how-do-historical-custom-event-timestamps-affect-action-based-canvases-and-campaigns}

A Braze avalia jornadas baseadas em ação quando eventos qualificados são ingeridos e o usuário atende às suas regras de público. Se um evento é registrado no perfil fora da janela em que seu Canvas ou Campaign estava ativo, ou antes de o usuário corresponder ao seu público, a entrada ou envios subsequentes podem não ocorrer como esperado. Compare os timestamps dos eventos com os horários de ativação e a associação ao Segment usando o log de atividade do perfil de usuário e as etapas de solução de problemas em [Solução de problemas de eventos personalizados]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#troubleshooting-custom-events). Se o comportamento ainda não corresponder às expectativas, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).