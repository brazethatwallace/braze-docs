---
nav_title: Dashboard de diagnóstico de envio de mensagens
article_title: Dashboard de diagnóstico de envio de mensagens
description: "Este artigo de referência aborda o dashboard de diagnóstico de envio de mensagens, que ajuda a entender por que as mensagens de suas campanhas ou Canvas podem não ter sido enviadas conforme o esperado."
alias: /ccdd/
page_order: 2
toc_headers: h2
---

# Dashboard de diagnóstico de envio de mensagens {#messaging-diagnostics-dashboard}

> O dashboard **Messaging Diagnostics** oferece uma visão geral dos resultados de envio de mensagens, permitindo que você identifique tendências e diagnostique possíveis problemas na sua configuração de envio de mensagens. Esse dashboard pode ajudar a entender por que as mensagens de suas campanhas ou Canvas podem não ter sido enviadas conforme o esperado.

{% alert important %}
O dashboard **Messaging Diagnostics** está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar do acesso antecipado.
{% endalert %}

## Conceitos principais {#key-concepts}

### Enviado e entregue {#sent-and-delivered}

É fundamental entender que esse dashboard relata como a Braze processou internamente uma mensagem, e não o status final de entrega da mensagem.

Uma mensagem marcada como "enviada" nesse dashboard significa que a Braze processou e despachou a mensagem com sucesso. Para a maioria dos canais, isso significa que a Braze encaminhou a mensagem ao parceiro de envio terceirizado relevante. No entanto, isso não garante a entrega final ao dispositivo do usuário.

Quando a Braze "envia" uma mensagem, a entrega final pode depender de serviços externos. Considere os exemplos a seguir para cada canal.

| Canal | Exemplo de entrega final |
| --- | --- |
| Content Cards | O cartão foi enviado e está elegível para visualização. |
| E-mail | A Braze encaminha a mensagem a um provedor de serviços de e-mail (ESP). O ESP é então responsável pela entrega final. Esse ESP, por exemplo, pode reportar um "bounce" se o endereço de e-mail for inválido ou a caixa de entrada estiver cheia. |
| Mensagens no app | A mensagem foi exibida ao usuário. |
| LINE | A mensagem foi encaminhada com sucesso a um parceiro de envio. |
| Push | A Braze encaminha a mensagem ao serviço de notificação por push apropriado (como o serviço de Notificações por Push da Apple para iOS ou o Firebase Cloud Messaging para Android). Esse serviço é responsável pela entrega final da notificação ao dispositivo. |
| SMS/MMS/RCS | A Braze encaminha a mensagem a um gateway de SMS (como o Twilio). Esse gateway é responsável pela entrega final à operadora de celular. |
| Webhooks | A solicitação de webhook foi feita com sucesso, retornando uma resposta `2xx`. |
| WhatsApp | A mensagem foi encaminhada com sucesso a um parceiro de envio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enviado e entregue" }

### Atualização dos dados {#data-freshness}

A frequência com que os dados nesse dashboard são atualizados pode variar com base na carga do sistema. Embora a frequência de atualização não seja garantida, na maioria dos casos ela é inferior a uma hora.

## Configurando o dashboard {#configuring-the-dashboard}

Você pode acessar o dashboard de diagnóstico em **Analytics** > **Dashboard Builder** e selecionando **Messaging Diagnostics** na lista de dashboards criados pela Braze.

Para executar o dashboard e visualizar seus dados:

1. Escolha **Campaigns** ou **Canvas** como a origem dos relatórios do seu dashboard.
2. Selecione uma ou mais campanhas ou Canvas.
3. Selecione **Run Dashboard** para carregar os dados dos filtros selecionados.

![Exemplo de diagnóstico de Campaign e Canvas de 25 a 31 de maio de 2025 para uma campanha de série de boas-vindas.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Exemplo de diagnóstico de Campaign e Canvas com gráfico ao passar o mouse de 25 a 31 de maio de 2025 para uma campanha de série de boas-vindas.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

## Interpretando os dados {#interpreting-the-data}

{% alert note %}
O dashboard exibe apenas os dados dos últimos sete dias. Todos os horários são exibidos no fuso horário do seu espaço de trabalho.
{% endalert %}

### Blocos de resumo {#summary-tiles}

No topo da página, há blocos de resumo com as principais métricas do período selecionado:

- **Sent:** A contagem total de mensagens que a Braze processou e enviou com sucesso.
  - **E-mail, SMS/MMS/RCS, WhatsApp, LINE e push:** A mensagem foi encaminhada com sucesso a um parceiro de envio.
  - **Webhooks:** A solicitação de webhook foi feita com sucesso, retornando uma resposta `2xx`.
  - **Content Cards:** O cartão foi enviado e está elegível para visualização.
  - **Mensagens no app:** A mensagem foi exibida ao usuário.
- **Not Sent:** A contagem total de mensagens que foram abortadas. Isso inclui membros do público do Canvas que não entraram no Canvas ou saíram dele porque tiveram uma falha em uma etapa ou atenderam aos critérios de saída ao realizar um evento de saída.

### Resultados de mensagens ao longo do tempo {#message-outcomes-over-time}

Este gráfico de série temporal mostra um detalhamento por hora dos motivos pelos quais uma mensagem foi abortada ou um usuário foi removido de um Canvas. Os rótulos de resultado neste gráfico são rótulos normalizados do dashboard, não valores brutos do payload de eventos. Este gráfico não exibe o número de envios.

### Registro granular de resultados de mensagens {#message-outcomes-granular-log}

O dashboard exibe uma tabela granular de resultados individuais de mensagens para os filtros e o período selecionados. Use essa tabela para revisar registros específicos, incluindo o horário, o ID do usuário, a etapa do Canvas, o resultado, os detalhes e o canal.

Você pode filtrar a tabela para focar em registros específicos:

- **Filtrar por resultado:** Selecione um resultado no filtro de resultados para exibir apenas as linhas com esse resultado (por exemplo, `Frequency capped` ou `User not eligible for channel`).
- **Pesquisar por ID do usuário:** Insira um ID de usuário no campo de pesquisa para exibir as linhas desse usuário específico.

Quando você aplica ambos os filtros, a tabela retorna as linhas que correspondem tanto ao resultado selecionado quanto ao ID do usuário inserido.

Selecione uma linha na tabela para abrir o painel de detalhes. O painel de detalhes fornece contexto adicional sobre o resultado, e o Ask Operator oferece orientações de correção para ajudar a solucionar o problema subjacente.

![Registro granular de resultados do Messaging Diagnostics com uma linha selecionada e acesso ao painel de detalhes.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Painel de detalhes do Messaging Diagnostics expandido com contexto do resultado e orientações de correção.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

{% alert note %}
Os filtros de canal se aplicam a resultados vinculados a um canal de envio de mensagens específico. Alguns resultados são independentes de canal, então ainda podem aparecer em visualizações agregadas mesmo quando você aplica um filtro de canal.
{% endalert %}

### Resultados de interrupção {#abort-outcomes}

As definições a seguir explicam os resultados de interrupção exibidos no dashboard. Os resultados são agrupados por categoria para facilitar a localização do que você está investigando.

{% alert note %}
Os resultados de interrupção no Messaging Diagnostics são rótulos legíveis do dashboard. Nos [eventos de engajamento com mensagem do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), as informações de interrupção são representadas com campos como `abort_type` e `abort_log`. Como esses conjuntos de dados têm representações e caminhos de processamento diferentes, as contagens ou nomenclaturas podem diferir entre o Currents e o Messaging Diagnostics.
{% endalert %}

#### Conteúdo e renderização {#content-and-rendering}

| Resultado de interrupção | Explicação |
| ---- | ---- |
| Content Card expired | O cartão de conteúdo expirou antes que o usuário o visse. |
| Content Card invalid | O cartão de conteúdo continha erros e não foi enviado ao usuário. Alguns motivos comuns incluem: {::nomarkdown}<ul><li> Tamanho máximo excedido (2 KB) </li><li> Data de expiração inválida </li><li> A mensagem contém caracteres inválidos </li></ul>{:/} |
| Connected Content failed | A Braze tentou enviar a mensagem, mas o Connected Content falhou após o número máximo de tentativas (o padrão é cinco). **Nota:** Essa contagem representa o número de mensagens abortadas por atingir o número máximo de tentativas, não o número total de solicitações de Connected Content que falharam. |
| In-app-message rendering timeout | Após múltiplas tentativas, o Liquid não pôde ser renderizado e atingiu o tempo limite. |
| Liquid abort | A Liquid tag [abort_message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) foi chamada, então o envio foi cancelado. |
| Liquid rendering timeout | A renderização do modelo Liquid demorou demais. Isso ocorre com mais frequência em Banners, mensagens no app e e-mail. |
| Liquid syntax error | O modelo Liquid continha um erro de análise, então a mensagem foi cancelada. |
| Media URL failure | A Braze não conseguiu processar a URL de mídia na mensagem. Isso pode acontecer quando a URL está bloqueada, é inválida, atinge o tempo limite, retorna um status HTTP inválido ou falha na validação SSL. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conteúdo e renderização" }

#### Estado da campanha e do Canvas {#campaign-and-canvas-state}

| Resultado de interrupção | Explicação |
| ---- | ---- |
| Delay step failure | A [etapa de postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays) falhou, fazendo o usuário sair do Canvas. Essa falha pode ocorrer quando: {::nomarkdown}<ul><li> A variável fornecida à etapa de postergação personalizada estava vazia ou era de um tipo inválido </li><li> A postergação ultrapassa a duração máxima permitida no Canvas</li></ul>{:/} |
| Exception or exit event | O usuário era anteriormente elegível para receber a mensagem, mas: {::nomarkdown}<ul><li> realizou um <a href="/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-3-select-exception-events">evento de exceção</a> para uma campanha baseada em ação, então a mensagem foi abortada, ou </li><li> atendeu aos <a href="/docs/user_guide/messaging/canvas/create_a_canvas#setting-exit-criteria">critérios de saída</a> do Canvas e foi removido no meio da jornada.</li></ul>{:/} |
| Inactive campaign | A campanha foi interrompida enquanto a mensagem estava em trânsito, então foi abortada. |
| Inactive Canvas | O Canvas foi interrompido antes que o usuário entrasse na jornada. |
| Inactive Canvas step | Isso pode ocorrer no Canvas se: {::nomarkdown}<ul><li> A etapa do Canvas foi excluída </li> <li>O Canvas foi interrompido, fazendo com que todas as etapas se tornassem inativas </li></ul>{:/} |
| Volume limited | A campanha atingiu o limite de volume de envios definido, então o envio foi cancelado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estado da campanha e do Canvas" }

#### Limite de frequência e temporização {#rate-limiting-and-timing}

| Resultado de interrupção | Explicação |
| ---- | ---- |
| Frequency capped | O usuário já recebeu o número máximo de mensagens permitido pelas regras de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping) do seu espaço de trabalho, então o envio foi cancelado. |
| Quiet Hours abort | O horário de silêncio estava ativado para a campanha ou etapa do Canvas com o fallback definido como **Abort message**. O usuário disparou a campanha ou entrou na etapa de mensagem do Canvas durante o horário de silêncio, então a mensagem foi abortada. No entanto, isso não remove o usuário do Canvas. |
| Rate limited over 72 hours | A mensagem foi limitada por mais de 72 horas devido aos [limites de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting), então o envio foi abortado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limite de frequência e temporização" }

#### Elegibilidade e perfil do usuário {#user-eligibility-and-profile}

| Resultado de interrupção | Explicação |
| ---- | ---- |
| Duplicate user identifier | Múltiplos usuários com um identificador correspondente (como ID externo, endereço de e-mail, número de telefone) eram elegíveis para receber esta mensagem. Para evitar envios duplicados ao mesmo usuário, esta mensagem foi abortada. |
| User failed pre-check for Message step | A Braze executa um primeiro conjunto de pré-verificações básicas de elegibilidade de público, reelegibilidade e elegibilidade de canal antes das validações completas de entrega para uma etapa de mensagem do Canvas. Esse resultado significa que o usuário ou a mensagem falhou em uma dessas verificações, então a mensagem foi abortada para essa etapa. |
| User failed pre-check for triggered message | A Braze executa um primeiro conjunto de pré-verificações básicas de elegibilidade de público, reelegibilidade e elegibilidade de canal antes de criar uma mensagem para enviar a partir desse gatilho. Esse resultado significa que o usuário ou a mensagem falhou em uma dessas verificações, então a mensagem foi abortada. |
| User no longer eligible | O usuário estava inicialmente no público-alvo, mas deixou de atender aos critérios do público antes que a Braze enviasse a mensagem ou inserisse o usuário no Canvas. O intervalo entre o usuário atender inicialmente aos critérios do público e deixar de atendê-los pode ser causado por atrasos de: {::nomarkdown}<ul><li>Intelligent Timing</li><li>Horário de silêncio</li><li>Fuso local</li><li>Limites de velocidade de entrega (não aplicável para entrada no Canvas)</li><li>Atrasos no pipeline de envio de mensagens</li></ul>{:/} |
| User not eligible for step | O usuário não atendeu às [validações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) definidas para a etapa de mensagem ou fazia parte de uma [lista de supressão]({{site.baseurl}}/user_guide/audience/suppression_lists). Dependendo das configurações de **Delivery validations**, o usuário pode ter saído do Canvas ou avançado para a próxima etapa. |
| User not re-eligible | O usuário era elegível para receber a mensagem ou entrar no Canvas, mas o envio foi cancelado devido às configurações de reelegibilidade ou reentrada. Isso pode acontecer se o usuário já recebeu a campanha ou entrou no Canvas recentemente, se outro envio da mesma campanha já está em andamento para esse usuário, ou se a reelegibilidade ou reentrada está desativada. |
| User profile not found | O usuário nunca existiu ou não existe mais na Braze. Alguns casos comuns incluem: {::nomarkdown}<ul><li> O usuário foi direcionado usando envio de mensagens por API, mas nunca existiu na Braze. </li><li>O usuário foi excluído antes que a mensagem fosse enviada ou a etapa do Canvas fosse executada. </li><li>O usuário foi mesclado com outro perfil antes que a mensagem fosse enviada.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Elegibilidade e perfil do usuário" }

#### Canal e entrega {#channel-and-delivery}

| Resultado de interrupção | Explicação |
| ---- | ---- |
| Partner delivery error | A Braze tentou enviar esta mensagem ao seu parceiro de entrega por 24 horas, mas o parceiro retornou erros temporários durante todo o período. |
| Push credentials invalid | As [credenciais de push]({{site.baseurl}}/user_guide/channels/push/faqs#valid-push-token) para este app estão ausentes ou inválidas, então o envio foi cancelado. Atualize suas credenciais em **Configurações do app**. |
| Subscription group failure | A mensagem não pôde ser enviada devido a problemas de configuração do grupo de inscrições ou do serviço de envio de mensagens. Motivos comuns incluem números de envio ausentes para SMS ou WhatsApp, ou MMS não suportado no serviço de envio de mensagens configurado. |
| User not eligible for channel | O usuário não é elegível para receber esta mensagem no canal selecionado. Motivos comuns incluem identificadores de canal ausentes ou inválidos, nenhum token por push elegível, restrições de estado de inscrição, capacidade de canal não suportada ou países bloqueados para canais baseados em telefone. |
| Webhook failed | O webhook recebeu um código de resposta malsucedido (não `2xx`). Consulte o [Registro de atividades de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log#dev-console-troubleshooting) para mais detalhes. Registros com mais de 60 horas são limpos e não estão mais acessíveis; erros de webhook são amostrados em até 20 registros por hora. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canal e entrega" }

## Perguntas frequentes {#frequently-asked-questions}

### O que significa uma falha de "pré-verificação"? {#what-does-a-pre-check-failure-mean}

Uma "pré-verificação" é uma verificação de validação rápida e agrupada que é executada no início de uma etapa do pipeline (como uma mensagem sendo disparada ou o envio de uma etapa de mensagem do Canvas). Pense nisso como uma saída antecipada projetada para máxima velocidade. Em vez de executar muitas verificações separadas e que consomem muitos recursos (como validar cada detalhe do perfil de um usuário), a Braze agrupa várias validações básicas em uma única "primeira passagem".

Se um usuário falhar nessa verificação agrupada, ele é removido imediatamente. Essa abordagem agrupada permite que a Braze processe volumes massivos de mensagens em alta velocidade e pode contribuir para um desempenho mais rápido e estável das suas campanhas e Canvas, reduzindo a latência de processamento de cada mensagem.

### O que significa um resultado de interrupção "other"? {#what-does-an-other-abort-outcome-mean}

São interrupções que não se enquadram nas categorias existentes do dashboard. Se você notar uma grande proporção de interrupções com "Other", entre em contato com o [suporte da Braze]({{site.baseurl}}/braze_support) para obter mais assistência.

### Por que a soma de _Not Sent_ e _Sent_ é menor que o tamanho esperado do meu público? {#why-is-the-sum-of-_not-sent_-and-_sent_-lower-than-my-expected-audience-size}

Isso pode acontecer por vários motivos:

- **Critérios de público:** Menos usuários do que o esperado podem ter atendido aos critérios de público (por exemplo, não estavam no segmento ou não tinham os atributos necessários) quando a campanha ou o Canvas foi lançado.
- **Processamento em andamento:** As mensagens ainda podem estar sendo processadas. Os usuários podem ainda estar em etapas anteriores do Canvas e não ter chegado a nenhuma etapa de mensagem.
- **Atualização dos dados:** Os dados do dashboard são atualizados aproximadamente a cada 15 minutos, mas isso não é garantido. Os dados mais recentes desta campanha ou Canvas podem ainda não ter chegado ao dashboard.
- **Casos extremos:** Há uma pequena chance de você estar encontrando um caso extremo que não é capturado neste dashboard no momento. Se você suspeitar que esse é o caso, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Por que a soma de _Not Sent_ e _Sent_ é maior que o público de uma campanha e Canvas? {#why-is-the-sum-of-_not-sent_-and-_sent_-greater-than-the-audience-for-a-campaign-and-canvas}

Isso pode ocorrer pelos seguintes motivos:

- **Mensagens multicanal:** A campanha ou etapa do Canvas foi configurada para enviar em múltiplos canais (como SMS e e-mail). Um único usuário pode receber um resultado de "enviado" para um canal (como e-mail) e um resultado de "interrupção" para outro (como "User not eligible for channel"). Nesse caso, esse único usuário seria contado duas vezes no gráfico: uma vez como "enviado" e uma vez como "interrupção".
  - **Exemplo:** Você envia uma campanha de push para 100 usuários, direcionando tanto iOS quanto Android. Se um usuário tem apenas um dispositivo iOS, ele recebe o push iOS ("enviado"), mas também dispara uma interrupção para o push Android ("User not eligible for channel").
- **Múltiplas etapas de mensagem (apenas Canvas):** Seu Canvas pode ter mais de uma etapa de mensagem em uma determinada jornada. Este dashboard agrega todos os resultados, então um único usuário pode ser contado múltiplas vezes se passar por múltiplas etapas de mensagem dentro do período selecionado.
- **Mensagens de teste:** O envio de testes (que é contabilizado no dashboard) está fazendo com que as contagens totais sejam maiores que o tamanho do público.