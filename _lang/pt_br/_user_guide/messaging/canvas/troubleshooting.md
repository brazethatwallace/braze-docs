---
nav_title: Solução de problemas
article_title: Solução de problemas do Canvas
page_order: 7
page_type: reference
description: "Diagnostique problemas de entrada, envio e análise de dados do Canvas usando um caminho de investigação padrão, índice de sintomas e links para o Histórico de mensagens e o dashboard de Diagnóstico de mensagens."
tool: Canvas
---

# Solução de problemas do Canvas {#troubleshoot-canvases}

> Use esta página para diagnosticar problemas de entrada, envio e análise de dados do Canvas. Para definições e aprofundamentos, consulte as [Perguntas frequentes do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs).

{% alert note %}
Os registros do **Histórico de mensagens** e do **Diagnóstico de mensagens** ficam disponíveis por até **30 dias** a partir do evento. Entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) dentro desse período se precisar de ajuda para investigar um incidente específico.
{% endalert %}

## Comece aqui: identifique seu sintoma {#start-here-match-your-symptom}

| Sintoma | Acesse |
| --- | --- |
| Um usuário não entrou no Canvas | [O usuário não entrou no Canvas](#user-didnt-enter-the-canvas) |
| Um usuário entrou, mas não recebeu uma mensagem ou etapa | [O usuário não recebeu uma mensagem ou etapa do Canvas](#user-didnt-receive-a-canvas-message-or-step) |
| Ninguém ou menos usuários do que o esperado entraram | [Entradas no Canvas baixas ou zero](#low-or-zero-canvas-entries) |
| Envios ou entregas estão abaixo do público estimado | [Menos envios do que o esperado](#lower-sends-than-expected) |
| A análise de dados do Canvas parece incorreta (grupo de controle, conversões, zero envios) | [Divergências na análise de dados do Canvas](#canvas-analytics-mismatches) |
| A análise de dados mostra muito mais envios do que entradas ou mais saídas do que entradas | [A filtragem por intervalo de datas pode exibir números inesperados](#date-range-filtering-can-show-unexpected-numbers) |
| O Canvas não salva ou o editor congela | [Problemas com o editor e salvamento](#editor-and-save-issues) |
| Não é possível excluir uma variante do Canvas | [Não é possível excluir uma variante do Canvas por causa de um Segment or segmento arquivado](#cant-delete-a-canvas-variant-because-of-an-archived-segment) |
| Parei o Canvas, mas as mensagens continuaram sendo enviadas | [Comportamento do Canvas interrompido](#stopped-canvas-behavior) |
| Erro "Too many Canvas branches" ao lançar | [Erro "Too many Canvas branches"](#too-many-canvas-branches-error) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sintoma do Canvas" }

## Caminho de investigação padrão {#standard-investigation-path}

Use este fluxo de trabalho para investigar um usuário específico ou um problema de envio agregado. Comece pela etapa 1 para cada incidente.

1. Confirme se o Canvas está ativo (não é rascunho, parado ou arquivado).
2. Confirme se o cronograma de entrada (janela agendada, fuso horário, gatilho baseado em ação ou entrada disparada por API or interface de programação do aplicativo (API)) corresponde ao momento em que você espera que os usuários entrem.
3. Verifique o registro de mensagens de um usuário acessando **Público** > **Pesquisar usuários**, abrindo o perfil e selecionando **Histórico de mensagens** (últimos 30 dias).
   - Se não houver registro para o horário de envio esperado, o problema é com a entrada, não com a mensagem. Acesse [Usuário não entrou no Canvas](#user-didnt-enter-the-canvas).
4. Verifique o **Changelog** do Canvas e os changelogs de quaisquer Segments usados no direcionamento. Confirme se o público, as etapas ou as configurações de envio não foram alterados durante o incidente.
5. Verifique os resultados agregados na página de análise de dados do Canvas abrindo o [dashboard de Diagnóstico de mensagens]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) e revisando os motivos de interrupção e descarte.
   - Se você encontrar um resultado que não reconhece, consulte [Resultados de interrupção]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes) na documentação de diagnóstico.
   - Se uma etapa mostrar zero entradas (não zero envios), verifique o tipo da etapa anterior ([Jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), [Postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), [Jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) ou [Divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)).
6. Se você ainda estiver bloqueado, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) dentro de 30 dias com o ID do Canvas, IDs dos usuários afetados, timestamps (com fuso horário) e capturas de tela do histórico de mensagens ou do Diagnóstico de mensagens.

Antes do lançamento, use [Enviar Canvas de teste]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) e [Prévia de jornadas de usuários]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) para validar sua configuração.

## O usuário não entrou no Canvas {#user-didnt-enter-the-canvas}

**Sintoma:** Um usuário não entrou no Canvas quando você esperava, ou menos usuários entraram do que os eventos-gatilho indicam.

Os usuários devem corresponder ao **público-alvo** antes que a Braze avalie o gatilho de entrada (exceto para gatilhos de [alteração de atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Um gatilho por si só não garante a entrada se o usuário não estava no público no momento da avaliação.

Reelegibilidade e reentrada são controles separados em [Selecionando controles de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls):

- **Reelegibilidade:** Determina se um usuário pode entrar novamente no Canvas após sair (janela de tempo e configuração **Permitir que os usuários reentrem no Canvas**).
- **Reentrada:** Determina se um usuário que está atualmente dentro do Canvas pode entrar em uma jornada concorrente.

Um usuário pode ser reelegível, mas estar bloqueado porque ainda está no Canvas, ou pode ter saído, mas ainda estar fora da janela de reelegibilidade. Verifique ambas as configurações quando um usuário não conseguir reentrar em um Canvas.

Verifique o seguinte:

- **Cronograma de entrada e fuso horário:** Confirme se o Canvas estava ativo e se o usuário realizou o gatilho durante a [janela de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule).
- **Público-alvo no momento da avaliação:** Revise os changelogs de Segments e filtros. [User Lookup]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) pode apresentar um falso positivo para alguns tipos de filtro (por exemplo, atributos de data em formato de string).
- **Limites de entrada:** [Máximo de entradas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) ou limites de público podem ter sido atingidos.
- **Grupo de controle global:** Usuários no [grupo de controle global]({{site.baseurl}}/user_guide/audience/global_control_group) não entram em Canvas de envio de mensagens.
- **Grupo de controle do Canvas:** Usuários atribuídos ao grupo de controle do Canvas na entrada não recebem mensagens de variante. A atribuição de variante acontece na entrada, não por meio de filtros de Segment or segmento. Consulte [Divergências na análise de dados do Canvas](#canvas-analytics-mismatches).
- **Critérios de saída:** O usuário pode ter correspondido aos [critérios de saída]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) antes ou durante a entrada. Se a entrada e a saída usam o mesmo evento, consulte [Correspondência entre critérios de entrada e saída]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria).
- **Entrada disparada por API or interface de programação do aplicativo (API):** Confirme se o usuário foi adicionado com o [endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Você pode [criar um Segment or segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) com um filtro de entrada do Canvas e exportar usuários com [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

### A contagem de eventos-gatilho é maior do que as entradas no Canvas {#trigger-event-count-is-higher-than-canvas-entries}

**Sintoma:** O volume de eventos-gatilho é maior do que a contagem de entradas no Canvas.

A Braze faz a deduplicação de múltiplas tentativas de entrada que ocorrem no mesmo instante, então você pode ver menos entradas no Canvas do que eventos-gatilho. Para testar múltiplas entradas, espaçe os eventos-gatilho em pelo menos um segundo de intervalo.

Se um usuário realiza o mesmo gatilho múltiplas vezes dentro de um segundo, a Braze processa apenas uma entrada. Verifique o Messaging Diagnostics para resultados como **User not re-eligible** quando regras de reentrada ou reelegibilidade se aplicam.

{% details Horário de verão e Canvas agendados diariamente %}

Em dias de transição do horário de verão, Canvas agendados diariamente podem ser executados até uma hora antes ou depois do habitual. Se seus critérios de entrada dependem de atributos personalizados ou eventos com timestamps que se enquadram dentro de uma hora do horário de entrada agendado, os usuários podem ainda não se qualificar no dia da mudança de horário porque o atributo ou evento ainda não foi registrado.

Por exemplo, suponha que os usuários normalmente recebem uma atualização de atributo personalizado às 15h no fuso horário do seu Canvas e seu Canvas é executado diariamente às 15h30 nesse mesmo fuso horário. Em um dia de adiantamento do horário de verão, o Canvas pode avaliar os usuários até uma hora antes do habitual em relação a essa atualização de atributo — antes que o atributo tenha sido registrado. Se a reelegibilidade estiver desativada, os usuários que entraram em dias anteriores não podem reentrar, resultando em zero entradas nesse dia.

Para evitar isso, garanta que suas atualizações de atributos personalizados ou eventos ocorram mais de uma hora antes do horário de entrada agendado do Canvas.

{% enddetails %}

## O usuário não recebeu uma mensagem ou etapa do Canvas {#user-didnt-receive-a-canvas-message-or-step}

**Sintoma:** Um usuário entrou no Canvas mas não recebeu a mensagem ou etapa esperada.

Verifique o [**histórico de mensagens**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab) do usuário para a etapa do Canvas e o registro de data/hora. Se não houver registro, retorne a [O usuário não entrou no Canvas](#user-didnt-enter-the-canvas).

Em seguida, verifique o seguinte por tipo de gatilho ou etapa:

- **Gatilhos de evento personalizado ou compra:** Confirme se o evento aparece em **Analytics** > **Custom Events Report** (ou **Revenue** para compras). Compare o registro de data/hora do evento com o momento em que o Canvas foi ativado e com qualquer postergação programada na etapa.
- **Entrada disparada por API or interface de programação do aplicativo (API):** Confirme a entrada com um filtro de Segment or segmento do Canvas e exportação, conforme descrito em [O usuário não entrou no Canvas](#user-didnt-enter-the-canvas).
- **Gatilhos de jornadas de ação ou etapa de mensagem:** Confirme se o usuário realizou o evento pré-requisito e se as [propriedades do evento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#event-properties) estão disponíveis na etapa.
- **Etapas de mensagem no app:** As mensagens no app são enviadas no próximo início de sessão após o usuário entrar na etapa, e apenas a partir de eventos do SDK or kit de desenvolvimento de software (não da REST or transferir estado representacional API or interface de programação do aplicativo (API)). Consulte [Quando as mensagens no app do Canvas são enviadas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent) nas Perguntas frequentes do Canvas.
- **Grupo de controle do Canvas:** Verifique se o usuário não foi atribuído ao grupo de controle do Canvas na entrada.
- **Elegibilidade do canal e configurações de envio:** Confirme o status de inscrição, o estado de push ativado e as [configurações de envio]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) por etapa (por exemplo, **Subscription Settings** definido apenas para usuários com opt-in). Não adicione filtros de canal único ao **Target Audience** em Canvas multicanal.
- **Validações de entrega:** Se você ativou **Validate audience at message send** em uma etapa de mensagem, os usuários que não correspondem mais aos filtros no momento do envio não recebem a mensagem. Consulte [Validações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
- **Horário de silêncio, Intelligent Timing, limite de frequência e limites de frequência:** Esses recursos podem adiar, suprimir ou interromper envios. Os usuários podem permanecer no Canvas mesmo após uma interrupção por horário de silêncio.
- **Condições de corrida:** Se o usuário disparou múltiplas ações ao mesmo tempo, consulte [Condições de corrida]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions).

{% alert important %}
Quando uma etapa de mensagem do Canvas interrompe um envio, o usuário ainda avança para a próxima etapa. O Canvas avança na interrupção para que etapas posteriores de postergação e jornadas de ação não fiquem permanentemente bloqueadas. Consulte [Como os usuários avançam]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) e [Resultados de interrupção]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes).
{% endalert %}

Para filtros em nível de etapa, conflitos entre ramificações e comportamento de Branch or ramificação or ramificação de mensagens no app, consulte [Lançar com Canvas Flow — Solução de problemas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#troubleshooting) e as [Perguntas frequentes do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery).

{% alert important %}
Se o seu Canvas baseado em ação está enviando mensagens antes do esperado, verifique se o registro de data/hora do seu evento personalizado usa a hora atual, e não uma hora retroativa. A Braze avalia as postergações a partir do registro de data/hora enviado com o evento. Consulte [Entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule).
{% endalert %}

## Entradas do Canvas baixas ou zeradas {#low-or-zero-canvas-entries}

**Sintoma:** Nenhum ou menos usuários do que o esperado entraram no Canvas.

Comece com o [Checklist de lançamento com Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#launch-checklist) e depois confirme:

- O Canvas está ativo e o horário atual está dentro da janela de entrada agendada.
- As [configurações de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) (reelegibilidade, máximo de entradas e limites de entrada) permitem que os usuários esperados entrem.
- O público-alvo e os filtros de Segment or segmento ainda correspondem aos usuários esperados após o lançamento.
- As porcentagens do grupo de controle global e do Canvas mostram qual proporção de usuários entra em cada jornada versus recebe mensagens.
- Os limites de frequência do espaço de trabalho ou filas de entrada devem adicionar atrasos entre o momento em que os usuários se qualificam e quando entram ou avançam para uma etapa.

Para um único usuário, siga o [caminho de investigação padrão](#standard-investigation-path). Para entradas zeradas relacionadas ao horário de verão, consulte a seção recolhível em [Usuário não entrou no Canvas](#user-didnt-enter-the-canvas).

## Envios menores que o esperado {#lower-sends-than-expected}

**Sintoma:** Os envios ou entregas são menores do que o público estimado em uma etapa do Canvas.

As causas comuns incluem a reavaliação do público no momento do envio, elegibilidade do canal, grupos de controle, horário de silêncio, Intelligent Timing, limites de frequência e o comportamento de entrega de mensagens no app (zero _Envios_ com impressões é esperado para mensagens no app).

Se uma etapa de Mensagem mostra muitos usuários que entraram, mas poucos envios, verifique se o Liquid `abort_message()` cancelou o envio. Para verificações no Registro de Atividade de Mensagens, atributos ausentes e envios de teste, consulte [Solução de problemas de altas taxas de interrupção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages#troubleshooting-high-abort-rates).

Para uma lista detalhada, consulte [Por que os envios são menores do que o tamanho estimado do público?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#why-are-sends-lower-than-the-estimated-audience-size) nas perguntas frequentes do Canvas e [Por que os envios são menores do que o tamanho estimado do público?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size) para Campaigns.

Use o [dashboard de Diagnósticos de Envio de Mensagens]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) para ver os motivos de interrupção e descarte no nível da etapa.

## Divergências na análise de dados do Canvas {#canvas-analytics-mismatches}

**Sintoma:** A análise de dados do Canvas parece incorreta (divisões de grupo de controle, conversões ou zero envios).

A atribuição do grupo de controle e da variante acontece na entrada do Canvas com base nas porcentagens definidas no builder, e não por meio de filtros de Segment or segmento. Usuários que não podem receber um canal específico ainda podem entrar em uma variante. Use as [Configurações de envio]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) por etapa para limitar quem recebe cada tipo de mensagem, em vez de restringir o **Público-alvo** com filtros de canal.

Diferencie o grupo de controle do Canvas do [grupo de controle global]({{site.baseurl}}/user_guide/audience/global_control_group). Para definições de filtros, consulte [Qual é a diferença entre "Has not entered Canvas variation" e "Is not in Canvas control group"?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group) nas Perguntas frequentes do Canvas.

{% details Por que os envios de uma variante podem ser menores do que a porcentagem da variante %}

Imagine o seguinte cenário:

- Um Canvas tem uma única variante e um grupo de controle.
- A primeira etapa da variante é uma notificação por push.
- 90% dos usuários foram selecionados para entrar na variante e 10% para entrar no grupo de controle.

![Exemplo de Canvas com 90% de variante e 10% de grupo de controle.]({% image_buster /assets/img_archive/trouble15.png %})

Nesse cenário, 90% dos usuários que entram no Canvas entram na variante.

Ao analisar o Segment or segmento de usuários ativos, você verá que, embora ele contenha 29,8 mil usuários, apenas 64% deles estão com push ativado:

![Segment or segmento com o filtro "Push Enabled" definido como "true" e estimativa de 29,8 mil usuários.]({% image_buster /assets/img_archive/trouble16.png %})

Isso significa que, embora você tenha especificado que 90% dos usuários entrariam na variante, nem todos eles podem receber uma notificação por push. Usuários que não podem receber push ainda entram na variante — a contagem de envios reflete a elegibilidade do canal na etapa, e não a atribuição da variante na entrada.

{% enddetails %}

### A filtragem por intervalo de datas pode exibir números inesperados {#date-range-filtering-can-show-unexpected-numbers}

**Sintoma:** A análise de dados do Canvas ou da etapa mostra números inesperados ou improváveis, como muito mais envios do que entradas, ou mais usuários saindo de uma etapa do que entrando.

Isso pode acontecer quando você usa o filtro de calendário de intervalo de datas no topo da página de análise de dados do Canvas. Se você selecionar um intervalo que exclua algumas ações dos usuários, as métricas exibidas podem mostrar apenas parte da jornada de cada usuário.

Por exemplo:
- Você pode ver 100 entradas com 8.000 envios se o intervalo de datas começar depois que a maioria dos usuários entrou, mas incluir o período em que eles receberam as mensagens.
- Você pode ver mais usuários avançando para a próxima etapa do que entrando na etapa anterior se o intervalo capturar apenas as saídas, mas não as entradas anteriores.

Para resolver isso, ajuste o intervalo de datas para incluir todas as datas desde o lançamento do Canvas até o presente, ou selecione um intervalo que cubra todo o período relevante para as métricas que você precisa.

Para definições de taxa de conversão e análise de dados no nível da etapa, consulte [Análise de dados e conversões]({{site.baseurl}}/user_guide/messaging/canvas/faqs#analytics-and-conversions) nas Perguntas frequentes do Canvas.

## Problemas de edição e salvamento {#editor-and-save-issues}

**Sintoma:** O editor de Canvas não carrega, congela ou não salva suas alterações.

| Sintoma | Causa mais provável |
| --- | --- |
| O botão de salvar gira indefinidamente sem erro | Filtro de atributo personalizado vazio ou incompleto no público do Canvas ou em um filtro de etapa — remova o filtro ou selecione um atributo válido |
| Erro "Request Timed Out" ao editar | Interferência de extensão do navegador, bloqueadores de anúncios ou sessão expirada — tente uma janela anônima ou outro navegador |
| Não é possível salvar após arquivar uma variante | Uma variante arquivada ainda é referenciada adiante; revise as conexões entre etapas e restaure ou substitua a variante |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sintoma do editor" }

Se o editor congelar em um Canvas grande ou complexo, tente o seguinte:

- Limpe o cache e os cookies do navegador e recarregue a página. Bloqueadores de anúncios corporativos ou extensões do navegador podem interferir na plataforma da Braze.
- Use os controles de zoom do Canvas para reduzir a visualização para 25% ou 10%, diminuindo a quantidade de UI que o navegador precisa renderizar.
- Tente um navegador de internet or navegador web diferente.

Se o Canvas não carregar e não avançar, uma versão anterior não foi salva corretamente e pode conter etapas inválidas. Duplique o Canvas pelo dashboard. Se o problema persistir, abra um [ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

Para tickets de suporte sobre "Request Timed Out", inclua uma gravação de tela, carimbo de data/hora e fuso horário, navegador e versão, etapas para reproduzir e, opcionalmente, um log HAR das ferramentas de desenvolvedor do navegador. Consulte [O que devo incluir ao enviar um ticket de suporte para um erro "Request Timed Out"?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error) nas Perguntas frequentes sobre Canvas.

{% multi_lang_include audience/segments.md section='Canvas variant archived Segment or segmento' %}

## Comportamento de Canvas interrompido {#stopped-canvas-behavior}

**Sintoma:** Você interrompeu o Canvas, mas os usuários ainda receberam mensagens.

Quando você interrompe um Canvas, os usuários não podem entrar e nenhuma mensagem adicional é enviada pelo fluxo do Canvas. Envios de e-mail já entregues ao seu provedor de serviços de e-mail não podem ser recuperados.

Os usuários que estão aguardando em uma etapa de postergação ou jornada de ação não são removidos automaticamente da jornada quando você interrompe o Canvas. Se você reativar o Canvas antes que o horário de envio agendado passe, eles ainda poderão receber as etapas pendentes.

Para mais detalhes, consulte [O que acontece quando você interrompe um Canvas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas) nas perguntas frequentes do Canvas.

## Erro "Too many Canvas branches" {#too-many-canvas-branches-error}

**Sintoma:** Você vê o erro "Too many Canvas branches" ao lançar um Canvas agendado.

Esse erro aparece quando a combinação de ramificações de etapas e o tamanho do público de entrada pode causar problemas de desempenho no cluster, impedindo o envio de mensagens. A Braze exibe essa mensagem quando você lança um Canvas com uma entrada agendada — ela não aparece ao salvar um rascunho.

Para resolver:

- Reduza as ramificações de etapas no Canvas.
- Reduza o tamanho do público de entrada.
- Use [jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) para consolidar ramificações em vez de usar muitas jornadas paralelas.
- Se o seu Canvas usa o editor original, [clone-o para o Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) e reconstrua usando os componentes do Canvas.

Se ainda assim você precisar lançar o Canvas sem alterações e não conseguir migrar para o Canvas Flow, entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact).

## Quando entrar em contato com o suporte {#when-to-contact-support}

Entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) dentro de 30 dias após o problema, caso tenha concluído o [caminho de investigação padrão](#standard-investigation-path) e ainda precise de ajuda.

Inclua:

- ID do Canvas e IDs dos usuários afetados (ID externo ou ID da Braze)
- Timestamps com fuso horário
- Capturas de tela ou exportações do **histórico de mensagens** ou **Diagnóstico de mensagens**
- Para erros de "Request Timed Out" no editor, os detalhes listados em [Problemas no editor e ao salvar](#editor-and-save-issues)