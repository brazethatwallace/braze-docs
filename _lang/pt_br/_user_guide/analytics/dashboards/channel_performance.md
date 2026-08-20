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

Visualize seu dashboard de desempenho de e-mail acessando **Analytics** > **Email Performance** e selecionando o período para o qual deseja visualizar os dados. O período pode ser de até um ano no passado.

{% alert note %}
Para visualizar o dashboard **Email Performance**, você precisa da permissão "View Usage Data" ou "View Dashboard Reports".
{% endalert %}

![Dashboard de desempenho de e-mail exibindo o engajamento do canal de e-mail nos últimos trinta dias.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![Um exemplo de Campaign de e-mail com 335.630 envios, com uma média de 11.187,667 por dia.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Como as métricas são calculadas {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envios | Contagem | Número total de envios em cada dia no período |
| Taxa de entrega | Taxa | (Número total de entregas em cada dia no período) / (Número total de envios em cada dia no período) |
| Taxa de bounce | Taxa | (Número total de bounces em cada dia no período) / (Número total de envios em cada dia no período) |
| Taxa de cancelamento de inscrição | Taxa | (Número total de cancelamentos de inscrição únicos em cada dia no período) / (Número total de entregas no período)<br><br>Isso usa cancelamentos de inscrição únicos, que também são usados em Campaign Analytics, Visão Geral e Report Builder. Esses cancelamentos de inscrição são registrados em todas as fontes (como o dashboard, REST API, importações de CSV, e-mails e cancelamentos de inscrição por lista). As taxas de cancelamento de inscrição em análises de Campaign e Canvas são cancelamentos que ocorrem como resultado de um clique de cancelamento de inscrição em um e-mail entregue pela Braze. |
| Taxa de abertura única | Taxa | (Número total de aberturas únicas em cada dia no período) / (Número total de entregas no período) |
| Taxa de outras aberturas | Taxa | (Número total de outras aberturas em cada dia no período) / (Número total de entregas no período)<br><br>Outras aberturas incluem e-mails que não foram identificados como aberturas por máquina, como quando um usuário abre um e-mail. Essa métrica não é única e é uma submétrica do total de aberturas. |
| Taxa de cliques únicos | Taxa | (Número total de cliques únicos em cada dia no período) / (Número total de entregas no período) |
| Taxa de cliques por abertura única | Taxa | (Número total de cliques únicos em cada dia no período) / (Número total de aberturas únicas em cada dia no período) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como as métricas são calculadas" }

{% endtab %}
{% tab Insights de e-mail %}

### Dashboard de insights de e-mail {#email-insights-dashboard}

O dashboard de insights de e-mail rastreia onde e quando seus clientes estão interagindo com seus e-mails. Esses relatórios podem fornecer dados ricos e detalhados sobre como otimizar seus e-mails para gerar maior engajamento. O dashboard de insights de e-mail inclui até os últimos seis meses de dados. Para acessar o dashboard, vá para **Analytics** > **Email Performance** > **Email Insights**.

#### Engajamento por dispositivo {#engagement-by-device}

O relatório **Engagement by Device** fornece um detalhamento de quais dispositivos seus usuários estão usando para interagir com seus e-mails. Esses dados rastreiam o engajamento de e-mail em dispositivos móveis, desktop, tablet e outros tipos de dispositivos. Esses dados são baseados na string de user agent passada pelos dispositivos dos seus usuários.

{% alert note %}
Se você usa o CloudFront como sua CDN, certifique-se de que o user agent dos seus usuários seja passado para o provedor de serviços de e-mail. Caso contrário, todo user agent será "Amazon Cloudfront".
{% endalert %}

A categoria "Other" inclui qualquer string de user agent que não pode ser identificada como desktop, móvel ou tablet. Por exemplo, televisão, carro, console de videogame, OTT (over-the-top ou streaming) e similares. Isso também pode incluir valores nulos ou vazios.

Para entender melhor o que está nessa categoria "Other", você pode extrair os user agents usando qualquer uma destas opções:

1. O [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) enviará a string exata de user agent que foi recuperada dos dispositivos dos seus usuários.
2. Use o [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) para utilizar SQL ou o [AI Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder#generating-sql-with-the-ai-query-builder) para visualizar os user agents.

![Relatório de engajamento por dispositivo mostrando o número de cliques para dispositivos móveis, desktop, tablet e outros. O maior número de cliques ocorre em dispositivos móveis.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Para aberturas de e-mail, a Braze separa o Google Image Proxy, o Apple Image Proxy e o Yahoo Mail Proxy. Esses serviços armazenam em cache e carregam todas as imagens incorporadas em um e-mail antes de ele ser entregue ao destinatário. Como resultado, isso dispara uma abertura de e-mail a partir dos servidores do provedor de caixa de entrada, em vez do servidor do destinatário, o que pode levar a aberturas de e-mail inflacionadas. Esses serviços são destinados a melhorar a privacidade, segurança, desempenho e eficiência ao carregar imagens. Isso também pode conter aberturas reais de destinatários, pois esses serviços de proxy mascaram o user agent, e a Braze categoriza os dados de proxy usando o user agent.

![Relatório de engajamento por dispositivo mostrando o número de cliques para dispositivos móveis, desktop, tablet, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy e outros. O maior número de aberturas ocorre em dispositivos móveis.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### Engajamento por provedor de caixa de entrada {#engagement-by-mailbox-provider}

O relatório **Engagement by Mailbox Provider** exibe os principais provedores de caixa de entrada que contribuem para seus cliques ou aberturas. Você pode clicar em provedores de caixa de entrada específicos para detalhar domínios de recebimento específicos. Por exemplo, se a Microsoft estiver listada neste relatório como uma das suas principais métricas de provedor de caixa de entrada, você pode visualizar mais detalhes sobre seus domínios de recebimento, como "outlook.com", "hotmail.com", "live.com" e outros.

![Um exemplo de relatório de engajamento por provedor de caixa de entrada com Google, Apple iCloud, Yahoo, Microsoft e Mail.Ru Group e seus respectivos números de cliques.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### Horário de engajamento {#time-of-engagement}

O relatório **Time of Engagement** exibe dados sobre quando os usuários estão interagindo com seus e-mails. Isso pode ajudar a responder perguntas como qual dia da semana ou qual horário tem o maior engajamento dos seus clientes. Com esses insights, você pode experimentar o melhor dia ou horário para enviar suas mensagens e gerar maior engajamento. Esses horários são baseados no fuso horário da sua empresa.

O relatório de engajamento **Day of the week** detalha aberturas ou cliques por dia da semana.

![Um exemplo de relatório de engajamento por dia da semana com o maior número de cliques na segunda-feira e na quarta-feira.]({% image_buster /assets/img_archive/time_engagement.png %})

O relatório de engajamento **Time of the day** detalha aberturas ou cliques por cada hora em uma janela de 24 horas.

![Um exemplo de relatório de engajamento por hora do dia com aberturas ou cliques das 0h às 23h.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Para saber mais sobre análise de dados dos seus e-mails, confira [Relatórios de e-mail]({{site.baseurl}}/user_guide/channels/email/reporting).

{% endtab %}
{% tab Desempenho de SMS %}

### Dashboard de desempenho de SMS {#sms-performance-dashboard}

Para usar seu dashboard de desempenho de SMS, acesse **Analytics** > **SMS Performance** e selecione o período para o qual deseja visualizar os dados. O período pode ser de até um ano no passado.

![Um exemplo de Campaign de SMS com 335.630 envios, com uma média de 11.187,667 por dia.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Como as métricas são calculadas

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="SMS" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envios | Contagem | Número total de envios em cada dia no período |
| Taxa de entregas confirmadas | Taxa | (Número total de entregas em cada dia no período) / (Número total de envios em cada dia no período) |
| Taxa de falhas de entrega | Taxa | (Número total de falhas em cada dia no período) / (Número total de envios em cada dia no período) |
| Taxa de rejeições | Taxa | (Número total de rejeições em cada dia no período) / (Número total de envios em cada dia no período) |
| Taxa de cliques | Taxa | (Número total de cliques em cada dia no período) / (Número total de entregas em cada dia no período) |
| Total de aceitações | Taxa | Número total de aceitações de mensagens recebidas em cada dia no período |
| Total de cancelamentos | Taxa | Número total de cancelamentos de mensagens recebidas em cada dia no período |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como as métricas são calculadas" }

{% endtab %}
{% tab Desempenho de push %}

### Dashboard de desempenho de push {#push-performance-dashboard}

O dashboard **Push Performance** oferece uma visão única em nível de canal do engajamento de push, incluindo envios, bounces, entregas e taxas de Aberturas Diretas, Aberturas por Influência e aberturas totais em uma janela de tempo configurável. Use-o para entender a integridade geral do seu canal de push sem precisar consolidar dados de Campaigns ou Canvas individuais.

Para abrir o dashboard, acesse **Analytics** > **Dashboard Builder** e selecione **Push Channel Dashboard**. O período pode ser de até um ano no passado.

![Um exemplo de Campaign de push com mais de 63 milhões de envios.]({% image_buster /assets/img_archive/push_performance_dashboard.png %})

#### Como as métricas são calculadas

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envios | Contagem | Número total de envios em cada dia no período |
| Taxa de bounce | Taxa | (Número total de bounces em cada dia no período) / (Número total de envios em cada dia no período) |
| Taxa de entrega | Taxa | (Número total de entregas em cada dia no período) / (Número total de envios em cada dia no período) |
| Taxa de Aberturas Diretas | Taxa | (Número total de Aberturas Diretas em cada dia no período) / (Número total de entregas em cada dia no período) |
| Taxa de Aberturas por Influência | Taxa | (Número total de Aberturas por Influência em cada dia no período) / (Número total de entregas em cada dia no período) |
| Taxa de aberturas totais | Taxa | (Número total de aberturas totais em cada dia no período) / (Número total de entregas em cada dia no período)<br><br>O total de aberturas inclui tanto Aberturas Diretas quanto Aberturas por Influência. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como as métricas são calculadas" }

{% endtab %}
{% endtabs %}

## Filtros do dashboard {#dashboard-filters}

Você pode filtrar os dados do seu dashboard usando as seguintes opções de filtro:

- **Tag:** Escolha uma tag. Quando aplicada, o dashboard mostrará métricas apenas para a tag selecionada.
- **Platforms:** (Somente no dashboard de desempenho de push) Escolha uma plataforma de push, como **All Push**, **Android**, **iOS**, **Mobile combined**, **Kindle** ou **Web**. Quando aplicada, o dashboard exibirá métricas apenas para a plataforma selecionada.
- **Canvas:** Escolha até 10 Canvas. Quando aplicado, o dashboard mostrará métricas apenas para os Canvas selecionados. Se você selecionar um filtro de tag primeiro, as opções de filtro de Canvas incluirão apenas os Canvas que possuem a tag selecionada.
- **Campaign:** Escolha até 10 Campaigns. Quando aplicado, o dashboard mostrará métricas apenas para as Campaigns selecionadas. Se você selecionar um filtro de tag primeiro, as opções de filtro de Campaign incluirão apenas as Campaigns que possuem a tag selecionada.

![Opções de filtro no dashboard de desempenho de canal, onde você pode selecionar uma tag e uma lista de Canvas para filtrar.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Comparação de períodos {#comparing-time-periods}

O dashboard de desempenho do canal compara automaticamente o período selecionado no intervalo de datas com o período anterior, totalizando o mesmo número de dias. Por exemplo, se você escolher "Últimos 7 dias" como intervalo de datas no dashboard, a comparação com o período anterior comparará as métricas dos últimos sete dias com os sete dias anteriores. Se você selecionar um intervalo de datas personalizado — digamos, de 10 a 15 de maio, o que equivale a seis dias de dados — o dashboard comparará as métricas desses dias com as métricas de 4 a 9 de maio.

A comparação é a variação percentual entre o período anterior e o atual, calculada pela diferença entre os dois períodos dividida pela métrica do período anterior.

### Visualização de alterações em contagens totais e taxas {#viewing-changes-in-total-counts-and-rates}

Você pode alternar entre **Show Change in Totals** — que compara as contagens totais (como o número de e-mails entregues) entre os dois períodos — e **Show Change in Rates** — que compara as taxas (como a taxa de entrega).

![Botões de opção para alternar entre a exibição de alterações em totais ou alterações em taxas no dashboard de desempenho do canal.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Perguntas frequentes {#frequently-asked-questions}

### Por que meu dashboard está exibindo valores vazios? {#why-is-my-dashboard-displaying-empty-values}

Existem alguns cenários que podem levar a valores vazios para uma métrica:

- A Braze registrou zeros para essa métrica específica no período selecionado.
- Você não enviou nenhuma mensagem durante o período selecionado.
- Embora tenha havido métricas como aberturas, cliques ou cancelamentos de inscrição em um período selecionado, não houve entregas ou envios. Nesse caso, a Braze não calculará uma métrica de taxa.

Para ver mais métricas, tente expandir o período.

### Por que meu dashboard de e-mail exibe mais Outras Aberturas do que Aberturas Únicas? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

Para a métrica _Aberturas Únicas_, a Braze faz a deduplicação de quaisquer aberturas repetidas registradas por um determinado usuário (sejam elas _Aberturas por Máquina_ ou _Outras Aberturas_), de modo que apenas uma única _Abertura Única_ é contabilizada se um usuário abrir várias vezes. Para _Outras Aberturas_, a Braze não faz deduplicação.

<!---Temporarily hidden until functionality is added

## Valores vazios nos seus dados {#empty-values-in-your-data}

### Se uma métrica exibe "0%" ou "0" {#if-a-metric-displays-0-or-0}

Isso significa que a Braze registrou zero para essa métrica específica durante o período selecionado.

#### Se uma métrica exibe "N/A" {#if-a-metric-displays-na}

Isso significa que, embora a Braze tenha registrado contagens positivas para uma métrica específica no período selecionado, o denominador para o cálculo da taxa (envios ou entregas, na maioria dos casos) foi zero. Isso pode ocorrer quando e-mails são enviados em um dia e as aberturas e cliques são registrados nos dias seguintes, caso o período selecionado não inclua a data em que as mensagens foram enviadas.

#### Se uma métrica exibe "--" {#if-a-metric-displays}

Isso significa que a Braze não registrou nenhum dado para essa métrica durante o período selecionado. Se você ainda não configurou ou enviou nenhum e-mail, saiba mais sobre como fazer isso na nossa seção dedicada de [E-mail]({{site.baseurl}}/user_guide/channels/email).

--->