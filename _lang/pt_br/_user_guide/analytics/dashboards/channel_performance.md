---
nav_title: Performance do canal
article_title: Dashboards de performance do canal
page_order: 2
page_type: reference
description: "Este artigo de referência aborda o dashboard de performance do canal, que permite visualizar métricas de performance para canais inteiros em Campaigns e Canvas."
tool:
  - Reports
toc_headers: h2
---

# Dashboards de performance do canal {#channel-performance-dashboards}

> Os dashboards de performance do canal mostram métricas de performance agregadas para um canal inteiro, tanto de Campaigns quanto de Canvas. Atualmente, esses dashboards estão disponíveis para e-mail, push e SMS.

## Dashboards {#dashboards}

Selecione uma guia para ver os detalhes dos dashboards de desempenho de canal disponíveis.

{% tabs %}
{% tab Desempenho de e-mail %}

### Dashboard de desempenho de e-mail {#email-performance-dashboard}

Visualize o dashboard de desempenho de e-mail acessando **Analytics** > **Email Performance** e selecionando o período para o qual deseja visualizar os dados. O período pode abranger até um ano no passado.

{% alert note %}
Para visualizar o dashboard **Email Performance**, você precisa da permissão "View Usage Data" ou "View Dashboard Reports".
{% endalert %}

![Dashboard de desempenho de e-mail exibindo o engajamento do canal de e-mail nos últimos trinta dias.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![Exemplo de Campaign de e-mail com 335.630 envios, com média de 11.187,667 por dia.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Como as métricas são calculadas {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envios | Contagem | Número total de envios em cada dia do período selecionado |
| Taxa de entrega | Taxa | (Número total de entregas em cada dia do período) / (Número total de envios em cada dia do período) |
| Taxa de bounce | Taxa | (Número total de bounces em cada dia do período) / (Número total de envios em cada dia do período) |
| Taxa de cancelamento de inscrição | Taxa | (Número total de cancelamentos de inscrição únicos em cada dia do período) / (Número total de entregas no período)<br><br>Utiliza cancelamentos de inscrição únicos, que também são usados na análise de dados de Campaigns, visão geral e Report Builder. Esses cancelamentos de inscrição são registrados em todas as fontes (como a REST API, importações de CSV, e-mails e cancelamentos de inscrição por lista). As taxas de cancelamento de inscrição na análise de dados de Campaigns e Canvas são cancelamentos que ocorrem como resultado de um clique em cancelar inscrição em um e-mail entregue pela Braze. |
| Taxa de abertura única | Taxa | (Número total de aberturas únicas em cada dia do período) / (Número total de entregas no período) |
| Taxa de outras aberturas | Taxa | (Número total de outras aberturas em cada dia do período) / (Número total de entregas no período)<br><br>Outras aberturas incluem e-mails que não foram identificados como aberturas por máquina, como quando um usuário abre um e-mail. Essa métrica não é única e é uma submétrica do total de aberturas. |
| Taxa de cliques únicos | Taxa | (Número total de cliques únicos em cada dia do período) / (Número total de entregas no período) |
| Taxa de cliques por abertura única | Taxa | (Número total de cliques únicos em cada dia do período) / (Número total de aberturas únicas em cada dia do período) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como as métricas são calculadas" }

{% endtab %}
{% tab Insights de e-mail %}

### Dashboard de insights de e-mail {#email-insights-dashboard}

O dashboard de insights de e-mail rastreia onde e quando seus clientes estão interagindo com seus e-mails. Esses relatórios podem fornecer dados detalhados e granulares sobre como otimizar seus e-mails para gerar maior engajamento. O dashboard de insights de e-mail inclui até os últimos seis meses de dados. Para acessar o dashboard, vá para **Analytics** > **Email Performance** > **Email Insights**.

#### Engajamento por dispositivo {#engagement-by-device}

O relatório **Engagement by Device** fornece uma visão detalhada dos dispositivos que seus usuários estão usando para interagir com seus e-mails. Esses dados rastreiam o engajamento de e-mail em dispositivos móveis, desktop, tablet e outros tipos de dispositivo. Esses dados são baseados na string de user agent passada pelos dispositivos dos seus usuários.

{% alert note %}
Se você usar o CloudFront como sua CDN, certifique-se de que o user agent dos seus usuários seja repassado ao provedor de serviços de e-mail. Caso contrário, todos os user agents aparecerão como "Amazon Cloudfront".
{% endalert %}

A categoria "Other" inclui qualquer string de user agent que não possa ser identificada como desktop, mobile ou tablet. Por exemplo, televisão, carro, console de videogame, OTT (over-the-top ou streaming) e similares. Isso também pode incluir valores nulos ou vazios.

Para entender melhor o que está nessa categoria "Other", você pode extrair os user agents usando uma destas opções:

1. O [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) enviará a string exata de user agent que foi recuperada dos dispositivos dos seus usuários.
2. Use o [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) para utilizar SQL ou nosso [AI Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder#generating-sql-with-the-ai-query-builder) para visualizar os user agents.

![Relatório de engajamento por dispositivo mostrando o número de cliques para dispositivos móveis, desktop, tablet e outros. A maior quantidade de cliques ocorre em dispositivos móveis.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Para aberturas de e-mail, a Braze separa o Google Image Proxy, o Apple Image Proxy e o Yahoo Mail Proxy. Esses serviços armazenam em cache e carregam todas as imagens incorporadas em um e-mail antes que ele seja entregue ao destinatário. Como resultado, isso aciona uma abertura de e-mail dos servidores do provedor de caixa de e-mail em vez do servidor do destinatário, o que pode levar a aberturas de e-mail inflacionadas. Esses serviços são destinados a melhorar a privacidade, segurança, desempenho e eficiência ao carregar imagens. Isso também pode conter aberturas reais de destinatários, já que esses serviços de proxy mascaram o user agent, e a Braze categoriza os dados de proxy usando o user agent.

![Relatório de engajamento por dispositivo mostrando o número de cliques para Mobile, Desktop, Tablet, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy e Other. A maior quantidade de aberturas ocorre em dispositivos móveis.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### Engajamento por provedor de caixa de e-mail {#engagement-by-mailbox-provider}

O relatório **Engagement by Mailbox Provider** exibe os principais provedores de caixa de e-mail que contribuem para seus cliques ou aberturas. Você pode clicar em provedores de caixa de e-mail específicos para detalhar domínios de recebimento específicos. Por exemplo, se a Microsoft estiver listada neste relatório como uma das suas principais métricas de provedor de caixa de e-mail, você pode visualizar detalhes dos seus domínios de recebimento, como "outlook.com", "hotmail.com", "live.com" e outros.

![Exemplo de relatório de engajamento por provedor de caixa de e-mail com Google, Apple iCloud, Yahoo, Microsoft e Mail.Ru Group e seus números correspondentes de cliques.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### Horário de engajamento {#time-of-engagement}

O relatório **Time of Engagement** exibe dados sobre quando os usuários estão interagindo com seus e-mails. Isso pode ajudar a responder perguntas como qual dia da semana ou qual horário tem o maior engajamento dos seus clientes. Com esses insights, você pode experimentar o melhor dia ou horário para enviar suas mensagens e gerar maior engajamento. Esses horários são baseados no fuso horário da sua empresa.

O relatório de engajamento por **Day of the week** detalha aberturas ou cliques por dia da semana.

![Exemplo de relatório de engajamento por dia da semana com a maior quantidade de cliques na segunda e na quarta-feira.]({% image_buster /assets/img_archive/time_engagement.png %})

O relatório de engajamento por **Time of the day** detalha aberturas ou cliques por cada hora em uma janela de 24 horas.

![Exemplo de relatório de engajamento por horário do dia com aberturas ou cliques de 00h a 23h.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Para saber mais sobre a análise de dados dos seus e-mails, consulte [Relatórios de e-mail]({{site.baseurl}}/user_guide/channels/email/reporting).

{% endtab %}
{% tab Desempenho de SMS %}

### Dashboard de desempenho de SMS {#sms-performance-dashboard}

Para usar o dashboard de desempenho de SMS, vá para **Analytics** > **SMS Performance** e selecione o período para o qual deseja visualizar os dados. O período pode abranger até um ano no passado.

![Exemplo de Campaign de SMS com 335.630 envios, com média de 11.187,667 por dia.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Como as métricas são calculadas

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="SMS" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envios | Contagem | Número total de envios em cada dia do período selecionado |
| Taxa de entregas confirmadas | Taxa | (Número total de entregas em cada dia do período) / (Número total de envios em cada dia do período) |
| Taxa de falhas de entrega | Taxa | (Número total de falhas em cada dia do período) / (Número total de envios em cada dia do período) |
| Taxa de rejeições | Taxa | (Número total de rejeições em cada dia do período) / (Número total de envios em cada dia do período) |
| Taxa de cliques | Taxa | (Número total de cliques em cada dia do período) / (Número total de entregas em cada dia do período) |
| Total de aceitações | Taxa | Número total de aceitações de mensagens recebidas em cada dia do período |
| Total de cancelamentos | Taxa | Número total de cancelamentos de mensagens recebidas em cada dia do período |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como as métricas são calculadas" }

{% endtab %}
{% tab Desempenho de push %}

### Dashboard de desempenho de push {#push-performance-dashboard}

O dashboard **Push Performance** oferece uma visão em nível de canal do engajamento de push em todas as suas Campaigns e Canvas, para que você possa entender a integridade do canal sem precisar consolidar dados de mensagens individuais.

Para abrir o dashboard, vá para **Analytics** > **Push Performance** e selecione o período para o qual deseja visualizar os dados. O período pode abranger até um ano no passado.

![Dashboard de desempenho de push exibindo o engajamento do canal de push nos últimos trinta dias.]({% image_buster /assets/img_archive/push_performance_dashboard_performance_tab.png %})

#### Visão geral {#overview}

O banner de visão geral resume quatro métricas principais para o período selecionado: *Envios*, *Taxa de entrega*, *Taxa de abertura* e *Taxa de conversão*. Cada bloco exibe um valor principal, uma contagem de apoio e uma dica com detalhes estatísticos adicionais.

A taxa de conversão neste dashboard considera apenas o evento de conversão primária. Para analisar eventos de conversão secundários, use o [Report Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

#### Engajamento ao longo do tempo {#engagement-over-time}

Na seção de engajamento ao longo do tempo, cada métrica é plotada como um gráfico de linha no período selecionado:

- Envios
- Total de aberturas
- Aberturas Diretas
- Aberturas por Influência
- Taxa de Aberturas Diretas
- Taxa de conversão
- Bounces

Você pode ativar um benchmark do setor no gráfico de taxa de Aberturas Diretas. Os benchmarks estão desativados por padrão. Para saber mais, consulte [Benchmarking](#benchmarking).

#### Como as métricas são calculadas

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envios | Contagem | Número total de envios em cada dia do período selecionado |
| Taxa de entrega | Taxa | (Número total de entregas em cada dia do período) / (Número total de envios em cada dia do período) |
| Taxa de bounce | Taxa | (Número total de bounces em cada dia do período) / (Número total de envios em cada dia do período) |
| Taxa de Aberturas Diretas | Taxa | (Número total de Aberturas Diretas em cada dia do período) / (Número total de entregas em cada dia do período) |
| Taxa de Aberturas por Influência | Taxa | (Número total de Aberturas por Influência em cada dia do período) / (Número total de entregas em cada dia do período) |
| Taxa de abertura total | Taxa | (Número total de aberturas em cada dia do período) / (Número total de entregas em cada dia do período)<br><br>O total de aberturas inclui tanto Aberturas Diretas quanto Aberturas por Influência. |
| Taxa de conversão | Taxa | (Número total de conversões primárias em cada dia do período) / (Número total de destinatários em cada dia do período) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como as métricas são calculadas" }

{% endtab %}
{% tab Insights de push %}

### Dashboard de insights de push {#push-insights-dashboard}

O dashboard de insights de push revela padrões de como seu público responde às notificações por push, para que você possa ajustar o que envia e com que frequência. Para acessá-lo, vá para **Analytics** > **Push Performance** > **Insights**.

#### Frequência {#frequency}

O relatório de frequência mostra a relação entre quantas notificações por push um usuário recebe e sua taxa de abertura, para que você possa encontrar o ponto em que envios adicionais deixam de gerar engajamento. O gráfico destaca um volume de envio recomendado com base em dados de benchmark do seu setor.

{% alert important %}
Os relatórios de frequência e cadência utilizam uma janela de análise mínima de três meses. Se você selecionar um período mais curto, a Braze pode expandir a data de início para incluir até três meses de dados quando disponíveis. Esses relatórios não são afetados pelos filtros de tag, Campaign, Canvas ou plataforma — eles sempre refletem seu volume total de push para o período selecionado.
{% endalert %}

#### Cadência {#cadence}

Enquanto o relatório de frequência indica quantas mensagens enviar, o relatório de cadência indica como espaçá-las. Ele plota a taxa de abertura em relação à cadência de envio, para que você possa ver se concentrar seus envios — por exemplo, três pushes chegando em um fim de semana — prejudica o engajamento em comparação com distribuí-los ao longo da semana.

Use-o junto com o relatório de frequência: a frequência define sua meta de volume, a cadência define a distribuição.

#### Distribuição de desempenho de Campaigns {#campaign-performance-distribution}

Este relatório plota cada Campaign de push no seu período por taxa de abertura e taxa de conversão, para que você possa ver seus melhores e piores desempenhos lado a lado e identificar o que têm em comum.

No gráfico de distribuição de desempenho de Campaigns, clique no ícone de três pontos e selecione **View data table**, que exibe uma tabela classificável com as mesmas Campaigns. Você pode classificar por taxa de abertura ou taxa de conversão para ranquear os desempenhos e usá-la para abrir a análise de dados de uma Campaign individual.

{% endtab %}
{% tab Entregabilidade de push %}

### Dashboard de entregabilidade de push {#push-deliverability-dashboard}

O dashboard de entregabilidade de push rastreia a integridade do seu público de push ao longo do tempo, para que você possa ver como suas mensagens afetam sua base alcançável. Para acessá-lo, vá para **Analytics** > **Push Performance** > **Deliverability**.

Este dashboard é filtrado apenas por período, e cada métrica é detalhada por plataforma.

#### Taxa de bounce {#bounce-rate}

Bounces no período selecionado, detalhados por plataforma. Você pode ativar um benchmark do setor neste gráfico. Ele está desativado por padrão.

#### Taxa de desinstalação {#uninstall-rate}

Desinstalações no período selecionado, detalhadas por plataforma. Use isso para verificar se um período de envio intenso coincidiu com a perda de usuários. Os dados de desinstalação dependem da sua configuração de Uninstall Tracking. Consulte [Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking). O Uninstall Tracking é compatível com iOS, Android (excluindo Huawei) e Kindle. Se o Uninstall Tracking estiver desativado, os dados de taxa de desinstalação serão menos completos e podem ser menos precisos. Dependendo do sistema operacional, os relatórios de desinstalação podem chegar com atraso ou em lotes, então o gráfico pode não refletir a data exata de desinstalação.

#### Como as métricas são calculadas

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Taxa de desinstalação | Taxa | (Número total de dispositivos onde a Braze recebeu um sinal de desinstalação em cada dia do período) / (Número total de dispositivos com tokens válidos em cada dia do período) |
| Taxa de bounce | Taxa | (Número total de bounces em cada dia do período) / (Número total de envios em cada dia do período) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como as métricas são calculadas" }

{% endtab %}
{% endtabs %}

## Filtros do dashboard {#dashboard-filters}

Você pode filtrar os dados do seu dashboard usando as seguintes opções de filtro:

- **Tag:** Escolha uma tag. Quando aplicada, o dashboard mostrará métricas apenas para a tag selecionada. O dashboard de push é compatível com várias tags.
- **Plataformas:** (Somente dashboards de push) Escolha uma plataforma de push, como **All Push**, **Android**, **iOS**, **Mobile combined**, **Kindle** ou **Web**. Quando aplicada, o dashboard exibirá métricas apenas para a plataforma selecionada.
- **Canvas:** Escolha até 10 Canvas. Quando aplicado, o dashboard mostrará métricas apenas para os Canvas selecionados. Se você selecionar um filtro de tag primeiro, as opções de filtro de Canvas incluirão apenas os Canvas que possuem a tag selecionada.
- **Campaign:** Escolha até 10 Campaigns. Quando aplicado, o dashboard mostrará métricas apenas para as Campaigns selecionadas. Se você selecionar um filtro de tag primeiro, as opções de filtro de Campaign incluirão apenas as Campaigns que possuem a tag selecionada.

{% alert note %}
Os filtros se aplicam de forma diferente nos dashboards de push. O dashboard de performance de push é compatível com todos os filtros. O dashboard de entregabilidade de push é compatível apenas com intervalo de datas, com um detalhamento por plataforma exibido em cada gráfico. Os relatórios de frequência e cadência no dashboard de insights de push são compatíveis apenas com intervalo de datas.
{% endalert %}

![Opções de filtro no dashboard de performance do canal, onde é possível selecionar uma tag e uma lista de Canvas para filtrar.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Comparando períodos de tempo {#comparing-time-periods}

O dashboard de desempenho do canal compara automaticamente o período selecionado no intervalo de datas com o período anterior, totalizando o mesmo número de dias. Por exemplo, se você escolher "Últimos 7 dias" como intervalo de datas no dashboard, a comparação com o período anterior comparará as métricas dos últimos sete dias com os sete dias anteriores. Se você selecionar um intervalo de datas personalizado — digamos, de 10 a 15 de maio, que corresponde a seis dias de dados — o dashboard comparará as métricas desses dias com as métricas de 4 a 9 de maio.

A comparação é a variação percentual entre o período anterior e o atual, calculada pela diferença entre os dois períodos dividida pela métrica do período anterior.

### Visualizando mudanças em contagens totais e taxas {#viewing-changes-in-total-counts-and-rates}

Você pode alternar entre **Show Change in Totals** — que compara as contagens totais (como o número de e-mails entregues) entre os dois períodos — e **Show Change in Rates** — que compara as taxas (como a taxa de entrega).

![Botões de opção para alternar entre a exibição de mudanças em totais ou mudanças em taxas no dashboard de desempenho do canal.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Benchmarking {#benchmarking}

Nos dashboards de push, você pode comparar seu desempenho com dados agregados e anonimizados da Braze.

### Benchmarks disponíveis {#available-benchmarks}

| Benchmark | Onde aparece | Padrão |
| --- | --- | ---- |
| Taxa de abertura direta | Desempenho de push | Desativado |
| Taxa de bounce | Entregabilidade de push | Desativado |
| Frequência | Insights de push | Ativado |
| Cadência | Insights de push | Ativado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Benchmarks disponíveis" }

Os benchmarks de taxa de abertura direta e taxa de bounce são divididos por plataforma. Todos os benchmarks de push são medidos em relação à taxa de abertura, não à taxa de conversão.

### Comparação por verticais {#comparing-verticals}

Os dados de benchmark são divididos por vertical. Seu dashboard usa como padrão a vertical da sua conta, e você pode usar o menu suspenso para comparar com outra.

### Comparação por regiões {#comparing-regions}

Os dados de benchmark são divididos por região. Seu dashboard usa como padrão a região da sua conta, e você pode usar o menu suspenso para comparar com outra.

{% alert note %}
Se os dados de benchmark mais recentes não estiverem disponíveis para o período selecionado, a Braze exibe um benchmark previsto.

Os dados de benchmark são atualizados mensalmente.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### Por que meu dashboard está exibindo valores vazios? {#why-is-my-dashboard-displaying-empty-values}

Existem alguns cenários que podem levar a valores vazios para uma métrica:

- A Braze registrou zeros para essa métrica específica no período selecionado.
- Você não enviou nenhuma mensagem durante o período selecionado.
- Embora tenha havido métricas como aberturas, cliques ou cancelamentos de inscrição para o período selecionado, não houve entregas ou envios. Nesse caso, a Braze não calculará uma métrica de taxa.

Para ver mais métricas, tente expandir o período.

### Por que meu dashboard de e-mail exibe mais Outras Aberturas do que Aberturas Únicas? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

Para a métrica _Aberturas Únicas_, a Braze faz a deduplicação de quaisquer aberturas repetidas registradas por um determinado usuário (sejam elas _Aberturas por Máquina_ ou _Outras Aberturas_), de modo que apenas uma única _Abertura Única_ é incrementada quando um usuário abre várias vezes. Para _Outras Aberturas_, a Braze não faz a deduplicação.

### Por que meus relatórios de frequência e cadência estão vazios? {#why-are-my-frequency-and-cadence-reports-empty}

Esses relatórios usam uma janela de análise de três meses. Se o período selecionado for menor, a Braze poderá expandir o intervalo para incluir datas anteriores quando houver dados disponíveis.

Se o seu período for longo o suficiente e os relatórios ainda estiverem vazios, os dados de benchmark podem ainda não estar disponíveis para o seu espaço de trabalho. Entre em contato com o suporte da Braze se tiver alguma dúvida.

### Por que meus filtros não alteram os relatórios de frequência e cadência? {#why-dont-my-filters-change-the-frequency-and-cadence-reports}

Os relatórios de frequência e cadência sempre refletem o volume total de push, porque o valor deles está em medir a carga total de mensagens recebidas por um usuário. Filtrar por um subconjunto de Campaigns subestimaria quantas mensagens esse usuário realmente recebeu. Apenas o filtro de período é aplicável.
<!---Temporarily hidden until functionality is added

## Valores vazios nos seus dados {#empty-values-in-your-data}

### Se uma métrica exibe "0%" ou "0" {#if-a-metric-displays-0-or-0}

Isso significa que a Braze registrou zero para essa métrica específica durante o período selecionado.

#### Se uma métrica exibe "N/A" {#if-a-metric-displays-na}

Isso significa que, embora a Braze tenha registrado contagens positivas para uma métrica específica no período selecionado, o denominador para o cálculo da taxa (geralmente envios ou entregas) foi zero. Isso pode ocorrer quando e-mails são enviados em um dia e as aberturas e cliques são registrados nos dias seguintes, caso o período selecionado não inclua a data em que as mensagens foram enviadas.

#### Se uma métrica exibe "--" {#if-a-metric-displays}

Isso significa que a Braze não registrou nenhum dado para essa métrica durante o período selecionado. Se você ainda não configurou ou enviou nenhum e-mail, saiba mais sobre como fazer isso na nossa seção dedicada de [E-mail]({{site.baseurl}}/user_guide/channels/email).

--->