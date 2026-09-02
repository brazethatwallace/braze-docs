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
O dashboard **Messaging Diagnostics** está disponível de forma geral. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em obter acesso ao recurso.
{% endalert %}

{% alert note %}
Para acessar o dashboard **Messaging Diagnostics**, você precisa da [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "View Dashboard Reports" no seu espaço de trabalho.
{% endalert %}

## Conceitos principais {#key-concepts}

### Enviado e entregue {#sent-and-delivered}

É fundamental entender que esse dashboard informa como a Braze processou internamente uma mensagem, e não o status final de entrega da mensagem.

Uma mensagem marcada como "enviada" nesse dashboard significa que a Braze processou e despachou a mensagem com sucesso. Para a maioria dos canais, isso significa que a Braze entregou a mensagem ao parceiro de envio terceirizado relevante. No entanto, isso não garante a entrega final ao dispositivo do usuário.

Quando a Braze "envia" uma mensagem, a entrega final pode depender de serviços externos. Considere os exemplos a seguir para cada canal.

| Canal | Exemplo de entrega final |
| --- | --- |
| Content Cards | O cartão foi enviado e está elegível para visualização. |
| E-mail | A Braze entrega a mensagem a um provedor de serviços de e-mail (ESP). O ESP é então responsável pela entrega final. Esse ESP, por exemplo, pode relatar um "bounce" se o endereço de e-mail for inválido ou a caixa de entrada estiver cheia. |
| In-App Messages | A mensagem foi visualizada pelo usuário e uma impressão foi registrada. |
| LINE | A mensagem foi entregue com sucesso a um parceiro de envio. |
| Push | A Braze entrega a mensagem ao serviço de notificação por push apropriado (como o Apple Push Notification service para iOS ou o Firebase Cloud Messaging para Android). Esse serviço é responsável pela entrega final da notificação ao dispositivo. |
| SMS/MMS/RCS | A Braze entrega a mensagem a um gateway de SMS (como o Twilio). Esse gateway é responsável pela entrega final à operadora de celular. |
| Webhooks | A solicitação do webhook foi feita com sucesso, retornando uma resposta `2xx`. |
| WhatsApp | A mensagem foi entregue com sucesso a um parceiro de envio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enviado e entregue" }

### Atualização dos dados {#data-freshness}

A frequência com que os dados nesse dashboard são atualizados pode variar com base na carga do sistema. Embora a frequência de atualização não seja garantida, na maioria dos casos ela é inferior a uma hora.

## Configurando o dashboard {#configuring-the-dashboard}

Você pode acessar o dashboard de diagnósticos acessando **Analytics** > **Dashboard Builder** e selecionando **Messaging Diagnostics** na lista de dashboards criados pela Braze.

Para executar o dashboard e visualizar seus dados:

1. Escolha **Campaigns** ou **Canvas** como a fonte dos relatórios do seu dashboard.
2. Selecione uma ou mais Campaigns ou Canvas.
3. Selecione **Run Dashboard** para carregar os dados dos filtros selecionados.

![Exemplo de diagnósticos de Campaign e Canvas de 25 a 31 de maio de 2025 para uma campanha de série de boas-vindas.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Exemplo de diagnósticos de Campaign e Canvas com gráfico ao passar o mouse de 25 a 31 de maio de 2025 para uma campanha de série de boas-vindas.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

## Interpretando os dados {#interpreting-the-data}

{% alert note %}
O dashboard exibe no máximo os últimos sete dias de dados. Todos os timestamps são exibidos no fuso horário do seu espaço de trabalho.
{% endalert %}

### Blocos de resumo {#summary-tiles}

No topo da página, há blocos de resumo com as principais métricas do período selecionado que mostram:

- **Enviadas:** O total de mensagens que a Braze processou e enviou com sucesso.
  - **E-mail, SMS/MMS/RCS, WhatsApp, LINE e push:** A mensagem foi entregue com sucesso a um parceiro de envio.
  - **Webhooks:** A requisição do webhook foi feita com sucesso, retornando uma resposta `2xx`.
  - **Content Cards:** O cartão foi enviado e está elegível para visualização.
  - **In-App Messages:** A mensagem foi exibida ao usuário.
- **Não enviadas:** O total de mensagens que foram interrompidas. Isso inclui membros do público do Canvas que não entraram no Canvas ou saíram do Canvas porque encontraram uma falha em uma etapa ou atenderam aos critérios de saída ao realizar um evento de saída.

### Resultados de mensagens ao longo do tempo {#message-outcomes-over-time}

Este gráfico de série temporal mostra um detalhamento por hora dos motivos pelos quais uma mensagem foi interrompida ou um usuário foi removido de um Canvas. Os rótulos de resultados neste gráfico são rótulos normalizados do dashboard, não valores brutos do payload do evento. Este gráfico não exibe o número de envios.

### Log granular de resultados de mensagens {#message-outcomes-granular-log}

O dashboard exibe uma tabela granular de resultados individuais de mensagens para os filtros e o período selecionados. Use esta tabela para revisar registros específicos, incluindo o timestamp, ID do usuário, etapa do Canvas, resultado, detalhes e canal.

Você pode filtrar a tabela para focar em registros específicos:

- **Filtrar por resultado:** Selecione um resultado no filtro de resultados para exibir apenas as linhas com aquele resultado (por exemplo, `Frequency capped` ou `User not eligible for channel`).
- **Buscar por ID do usuário:** Insira um ID de usuário no campo de busca para exibir as linhas daquele usuário específico.

Quando você aplica ambos os filtros, a tabela retorna as linhas que correspondem tanto ao resultado selecionado quanto ao ID de usuário informado.

Selecione uma linha na tabela para abrir o painel de detalhes. O painel de detalhes fornece contexto adicional sobre aquele resultado, e o Ask Operator oferece orientações de remediação para ajudar você a solucionar o problema subjacente.

![Log granular de resultados do Messaging Diagnostics com uma linha selecionada e acesso ao painel de detalhes.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Painel de detalhes do Messaging Diagnostics expandido com contexto do resultado e orientações de remediação.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

{% alert note %}
Os filtros de canal se aplicam a resultados vinculados a um canal de envio de mensagens específico. Alguns resultados são agnósticos de canal, então ainda podem aparecer em visualizações agregadas mesmo quando você aplica um filtro de canal.
{% endalert %}

### Resultados de interrupção {#abort-outcomes}

As definições a seguir explicam os resultados de interrupção exibidos no dashboard. Os resultados são agrupados por categoria para facilitar a localização daquele que você está investigando.

{% alert note %}
Os resultados de interrupção no Messaging Diagnostics são rótulos legíveis do dashboard. Nos [eventos de engajamento com mensagem do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), as informações de interrupção são representadas com campos como `abort_type` e `abort_log`. Como esses conjuntos de dados têm representações e fluxos de processamento diferentes, as contagens ou nomenclaturas podem divergir entre o Currents e o Messaging Diagnostics.
{% endalert %}

#### Conteúdo e renderização {#content-and-rendering}

| Resultado da interrupção | Explicação |
| ---- | ---- |
| Content Card expirado | O Content Card expirou antes que o usuário o visualizasse. |
| Content Card inválido | O Content Card continha erros e não foi enviado ao usuário. Alguns motivos comuns incluem: {::nomarkdown}<ul><li> Tamanho máximo excedido (2 KB) </li><li> Data de expiração inválida </li><li> A mensagem contém caracteres inválidos </li></ul>{:/} |
| Falha no Connected Content | A Braze tentou enviar a mensagem, mas o Connected Content falhou após o número máximo de tentativas (o padrão é cinco). **Nota:** Essa contagem representa o número de mensagens interrompidas por atingir o número máximo de tentativas, não o total de requisições de Connected Content que falharam. |
| Timeout na renderização da mensagem no app | Após várias tentativas, o Liquid não pôde ser renderizado e atingiu o tempo limite. |
| Interrupção via Liquid | A tag Liquid [abort_message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) foi chamada, então o envio foi cancelado. |
| Timeout na renderização do Liquid | A renderização do template Liquid demorou demais. Mais provável de ocorrer em Banners, mensagens no app e e-mail. |
| Erro de sintaxe do Liquid | O template Liquid continha um erro de análise, então a mensagem foi cancelada. |
| Falha na URL de mídia | A Braze não conseguiu processar a URL de mídia na mensagem. Isso pode acontecer quando a URL está bloqueada, inválida, atinge o tempo limite, retorna um status HTTP inválido ou falha na validação SSL. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conteúdo e renderização" }

#### Estado da Campaign e do Canvas {#campaign-and-canvas-state}

| Resultado da interrupção | Explicação |
| ---- | ---- |
| Falha na etapa de postergação | A [etapa de postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays) falhou, fazendo com que o usuário saísse do Canvas. Essa falha pode acontecer quando: {::nomarkdown}<ul><li> A variável fornecida para a etapa de postergação personalizada estava vazia ou era de um tipo inválido </li><li> A postergação excede a duração máxima permitida dentro do Canvas</li></ul>{:/} |
| Evento de exceção ou saída | O usuário era anteriormente elegível para receber a mensagem, mas {::nomarkdown}<ul><li> realizou um <a href="/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-3-select-exception-events">evento de exceção</a> para uma campanha baseada em ação, então a mensagem foi interrompida, ou </li><li> atendeu aos <a href="/docs/user_guide/messaging/canvas/create_a_canvas#setting-exit-criteria">critérios de saída</a> do Canvas, sendo removido durante a jornada.</li></ul>{:/} |
| Campaign inativa | A Campaign foi interrompida enquanto a mensagem estava em trânsito, então foi cancelada. |
| Canvas inativo | O Canvas foi interrompido antes que o usuário entrasse na jornada. |
| Etapa do Canvas inativa | Isso pode ocorrer no Canvas se: {::nomarkdown}<ul><li> A etapa do Canvas foi excluída </li> <li>O Canvas foi interrompido, fazendo com que todas as etapas se tornassem inativas </li></ul>{:/} |
| Limite de volume atingido | A Campaign atingiu o limite de volume de envios configurado, então o envio foi cancelado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estado da Campaign e do Canvas" }

#### Limite de frequência e timing {#rate-limiting-and-timing}

| Resultado da interrupção | Explicação |
| ---- | ---- |
| Limite de frequência atingido | O usuário já recebeu o número máximo de mensagens permitido pelas regras de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping) do seu espaço de trabalho, então o envio foi cancelado. |
| Interrupção por horário de silêncio | O horário de silêncio estava ativado para a Campaign ou etapa do Canvas com o fallback configurado como **Interromper mensagem**. O usuário disparou a Campaign ou entrou na etapa de mensagem do Canvas durante o horário de silêncio, então a mensagem foi interrompida. No entanto, isso não remove o usuário do Canvas. |
| Limite de frequência excedido por mais de 72 horas | A mensagem foi limitada por mais de 72 horas devido aos [limites de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting), então o envio foi cancelado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limite de frequência e timing" }

#### Elegibilidade e perfil do usuário {#user-eligibility-and-profile}

| Resultado da interrupção | Explicação |
| ---- | ---- |
| Identificador de usuário duplicado | Vários usuários com um identificador correspondente (como ID externo, endereço de e-mail ou número de telefone) eram elegíveis para receber esta mensagem. Para evitar envios duplicados ao mesmo usuário, esta mensagem foi interrompida. |
| Falha na pré-verificação do usuário para etapa de mensagem | A Braze executa um conjunto inicial de pré-verificações básicas de elegibilidade de público, reelegibilidade e elegibilidade de canal antes das validações completas de entrega para uma etapa de mensagem do Canvas. Esse resultado significa que o usuário ou a mensagem falhou em uma dessas verificações, então a mensagem foi interrompida para aquela etapa. |
| Falha na pré-verificação do usuário para mensagem disparada | A Braze executa um conjunto inicial de pré-verificações básicas de elegibilidade de público, reelegibilidade e elegibilidade de canal antes de criar uma mensagem para envio a partir deste disparo. Esse resultado significa que o usuário ou a mensagem falhou em uma dessas verificações, então a mensagem foi interrompida. |
| Usuário não é mais elegível | O usuário estava inicialmente no público-alvo, mas deixou de corresponder aos critérios do público antes que a Braze enviasse a mensagem ou inserisse o usuário no Canvas. O intervalo entre o usuário atender inicialmente aos critérios de público e deixar de atendê-los pode ser causado por atrasos de: {::nomarkdown}<ul><li>Intelligent Timing</li><li>Horário de silêncio</li><li>Fuso local</li><li>Limites de velocidade de entrega (não aplicável para entrada no Canvas)</li><li>Atrasos no pipeline de envio de mensagens</li></ul>{:/} |
| Usuário não elegível para a etapa | O usuário não atendeu às [validações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) configuradas para a etapa de mensagem ou fazia parte de uma [lista de supressão]({{site.baseurl}}/user_guide/audience/suppression_lists). Dependendo das configurações de **Validações de entrega**, o usuário pode ter saído do Canvas ou seguido para a próxima etapa. |
| Usuário não reelegível | O usuário era elegível para receber a mensagem ou entrar no Canvas, mas o envio foi cancelado devido às configurações de reelegibilidade ou reentrada. Isso pode acontecer se o usuário já recebeu a Campaign ou entrou no Canvas muito recentemente, se outro envio da mesma Campaign já está em andamento para este usuário, ou se a reelegibilidade ou reentrada está desativada. |
| Perfil de usuário não encontrado | O usuário nunca existiu ou não existe mais na Braze. Alguns casos comuns incluem: {::nomarkdown}<ul><li> O usuário foi direcionado usando envio de mensagens via API, mas nunca existiu na Braze. </li><li>O usuário foi excluído antes que a mensagem fosse enviada ou a etapa do Canvas fosse executada. </li><li>O usuário foi mesclado com outro perfil antes que a mensagem fosse enviada.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Elegibilidade e perfil do usuário" }

#### Canal e entrega {#channel-and-delivery}

| Resultado da interrupção | Explicação |
| ---- | ---- |
| Erro de entrega do parceiro | A Braze tentou enviar esta mensagem ao seu parceiro de entrega por 24 horas, mas o parceiro retornou erros temporários durante toda a janela. |
| Credenciais de push inválidas | As [credenciais de push]({{site.baseurl}}/user_guide/channels/push/faqs#why-doesnt-an-opted-in-user-have-a-push-token) para este app estão ausentes ou inválidas, então o envio foi cancelado. Atualize suas credenciais em **Configurações do app**. |
| Falha no grupo de inscrições | A mensagem não pôde ser enviada devido a problemas de configuração do grupo de inscrições ou do serviço de envio de mensagens. Motivos comuns incluem números de envio ausentes para SMS ou WhatsApp, ou MMS não suportado no serviço de envio de mensagens configurado. |
| Usuário não elegível para o canal | O usuário não é elegível para receber esta mensagem no canal selecionado. Motivos comuns incluem identificadores de canal ausentes ou inválidos, nenhum token de push elegível, restrições de estado de inscrição, capacidade de canal não suportada ou países bloqueados para canais baseados em telefone. |
| Falha no webhook | O webhook recebeu um código de resposta sem sucesso (não `2xx`). Códigos de erro comuns podem ser erros de cliente `4XX`, erros de servidor ou timeout `5XX`, ou `598 Host Unhealthy` ou requisições interrompidas brevemente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canal e entrega" }

## Perguntas frequentes {#frequently-asked-questions}

### O que significa uma falha de "pré-verificação"? {#what-does-a-pre-check-failure-mean}

Uma "pré-verificação" é uma validação rápida e agrupada que ocorre logo no início de uma etapa do pipeline (como o disparo de uma mensagem ou o envio de uma etapa de mensagem do Canvas). Pense nisso como uma saída antecipada projetada para máxima velocidade. Em vez de executar diversas verificações separadas e intensivas em recursos (como validar cada detalhe do perfil de um usuário), a Braze agrupa várias validações básicas em uma única "primeira passagem".

Se um usuário não passar nessa verificação agrupada, ele é descartado imediatamente. Essa abordagem permite que a Braze processe volumes massivos de mensagens em alta velocidade e pode contribuir para um desempenho mais rápido e estável das suas Campaigns e Canvas, reduzindo a latência de processamento de cada mensagem.

### O que significa um resultado de interrupção "outro"? {#what-does-an-other-abort-outcome-mean}

São interrupções que não se enquadram nas categorias existentes do dashboard. Se você ainda notar uma grande proporção de interrupções com "Outro", entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) para obter mais assistência.

### Por que a soma de _Não enviadas_ e _Enviadas_ é menor do que o tamanho esperado do público? {#why-is-the-sum-of-_not-sent_-and-_sent_-lower-than-my-expected-audience-size}

Isso pode acontecer por vários motivos:

- **Critérios de público:** Menos usuários do que o esperado podem ter atendido aos critérios de público (por exemplo, não estavam no Segment ou não tinham os atributos necessários) quando a Campaign ou o Canvas foi lançado.
- **Processamento em andamento:** As mensagens podem ainda estar sendo processadas. Os usuários podem ainda estar em etapas anteriores do Canvas e ainda não terem chegado a nenhuma etapa de mensagem.
- **Atualização dos dados:** Os dados do dashboard são atualizados aproximadamente a cada 15 minutos, mas isso não é garantido. Os dados mais recentes dessa Campaign ou Canvas podem ainda não ter chegado ao dashboard.
- **Casos extremos:** Há uma pequena chance de você estar encontrando um caso extremo que não é capturado nesse dashboard no momento. Se você suspeitar que esse é o caso, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Por que a soma de _Não enviadas_ e _Enviadas_ é maior do que o público de uma Campaign e Canvas? {#why-is-the-sum-of-_not-sent_-and-_sent_-greater-than-the-audience-for-a-campaign-and-canvas}

Isso pode ocorrer pelos seguintes motivos:

- **Mensagens multicanal:** A Campaign ou etapa do Canvas foi configurada para enviar em múltiplos canais (como SMS e e-mail). Um único usuário pode receber um resultado de "enviado" para um canal (como e-mail) e um resultado de "interrupção" para outro (como "Usuário não elegível para o canal"). Nesse caso, esse usuário seria contado duas vezes no gráfico: uma vez como "enviado" e uma vez como "interrupção".
  - **Exemplo:** Você envia uma Campaign de push para 100 usuários, direcionando tanto iOS quanto Android. Se um usuário tem apenas um dispositivo iOS, ele recebe o push do iOS ("enviado"), mas também dispara uma interrupção para o push do Android ("Usuário não elegível para o canal").
- **Múltiplas etapas de mensagem (somente Canvas):** Seu Canvas pode ter mais de uma etapa de mensagem em uma determinada jornada. Esse dashboard agrega todos os resultados, então um único usuário pode ser contado múltiplas vezes se ele passar por várias etapas de mensagem dentro do intervalo de tempo selecionado.
- **Mensagens de teste:** O envio de testes (que é contabilizado no dashboard) faz com que os totais sejam maiores do que o tamanho do público.