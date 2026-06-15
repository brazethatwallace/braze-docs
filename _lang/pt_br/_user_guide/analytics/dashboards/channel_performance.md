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

Selecione uma guia para ver os detalhes dos dashboards de performance de canal disponíveis.

{% tabs %}
{% tab Email performance %}

### Dashboard de performance de e-mail {#email-performance-dashboard}

Visualize seu dashboard de performance de e-mail acessando **Analytics** > **Email Performance** e selecionando o intervalo de datas do período que deseja visualizar. O intervalo de datas pode ser de até um ano no passado.

![Dashboard de performance de e-mail exibindo o engajamento do canal de e-mail nos últimos trinta dias.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![Um exemplo de Campaign de e-mail com 335.630 envios, com uma média de 11.187,667 por dia.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Como as métricas são calculadas {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envios | Contagem | Número total de envios em cada dia do intervalo de datas |
| Taxa de entrega | Taxa | (Número total de entregas em cada dia do intervalo de datas) / (Número total de envios em cada dia do intervalo de datas) |
| Taxa de bounce | Taxa | (Número total de bounces em cada dia do intervalo de datas) / (Número total de envios em cada dia do intervalo de datas) |
| Taxa de cancelamento de inscrição | Taxa | (Número total de cancelamentos de inscrição únicos em cada dia do intervalo de datas) / (Número total de entregas no intervalo de datas)<br><br>Essa métrica usa cancelamentos de inscrição únicos, que também são usados na análise de dados de Campaigns, Visão geral e Criador de relatórios. Esses cancelamentos de inscrição são registrados em todas as fontes (como a REST API, importações CSV, e-mails e cancelamentos de inscrição por lista). As taxas de cancelamento de inscrição nas análises de dados de Campaigns e Canvas referem-se aos cancelamentos que ocorrem como resultado de um clique de cancelamento de inscrição em um e-mail enviado pela Braze. |
| Taxa de abertura única | Taxa | (Número total de aberturas únicas em cada dia do intervalo de datas) / (Número total de entregas no intervalo de datas) |
| Taxa de outras aberturas | Taxa | (Número total de outras aberturas em cada dia do intervalo de datas) / (Número total de entregas no intervalo de datas)<br><br>Outras aberturas incluem e-mails que não foram identificados como aberturas por máquina, como quando um usuário abre um e-mail. Essa métrica não é única e é uma sub-métrica do total de aberturas. |
| Taxa de cliques únicos | Taxa | (Número total de cliques únicos em cada dia do intervalo de datas) / (Número total de entregas no intervalo de datas) |
| Taxa de cliques por abertura única | Taxa | (Número total de cliques únicos em cada dia do intervalo de datas) / (Número total de aberturas únicas em cada dia do intervalo de datas) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como as métricas são calculadas" }

{% endtab %}
{% tab Email insights %}

### Dashboard de insights de e-mail {#email-insights-dashboard}

O dashboard de insights de e-mail rastreia onde e quando seus clientes estão interagindo com seus e-mails. Esses relatórios podem fornecer dados detalhados e granulares sobre como otimizar seus e-mails para gerar maior engajamento. O dashboard de insights de e-mail inclui dados de até os últimos seis meses. Para acessar o dashboard, vá para **Analytics** > **Email Performance** > **Email Insights**.

#### Engajamento por dispositivo {#engagement-by-device}

O relatório **Engagement by Device** fornece um detalhamento de quais dispositivos seus usuários estão usando para interagir com seus e-mails. Esses dados rastreiam o engajamento de e-mail em celular, desktop, tablet e outros tipos de dispositivos. Esses dados são baseados na string de user agent transmitida pelos dispositivos dos seus usuários.

{% alert note %}
Se você usa o CloudFront como CDN, certifique-se de que o user agent dos seus usuários seja transmitido ao ESP. Caso contrário, todos os user agents aparecerão como "Amazon Cloudfront".
{% endalert %}

A categoria "Other" inclui qualquer string de user agent que não pode ser identificada como desktop, celular ou tablet. Por exemplo, televisão, carro, console de videogame, OTT (over-the-top ou streaming) e similares. Isso também pode incluir valores nulos ou vazios.

Para entender melhor o que está nessa categoria "Other", você pode extrair os user agents usando uma destas opções:

1. O [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) enviará a string exata de user agent que foi obtida dos dispositivos dos seus usuários.
2. Use nosso [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) com SQL ou nosso [Criador de consultas com IA]({{site.baseurl}}/user_guide/analytics/reports/query_builder/#generating-sql-with-the-ai-query-builder) para visualizar os user agents.

![Relatório de engajamento por dispositivo que mostra o número de cliques para celular, desktop, tablet e outros dispositivos. O maior número de cliques ocorre em dispositivos móveis.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Para aberturas de e-mail, a Braze separa o Google Image Proxy, o Apple Image Proxy e o Yahoo Mail Proxy. Esses serviços armazenam em cache e carregam todas as imagens incorporadas em um e-mail antes de ele ser entregue ao destinatário. Como resultado, isso aciona uma abertura de e-mail a partir dos servidores do provedor de caixa de e-mail, e não do servidor do destinatário, o que pode levar a aberturas de e-mail inflacionadas. Esses serviços têm como objetivo melhorar a privacidade, segurança, performance e eficiência ao carregar imagens. Isso também pode conter aberturas reais de destinatários, pois esses serviços de proxy mascaram o user agent, e a Braze categoriza os dados de proxy usando o user agent.

![Relatório de engajamento por dispositivo que mostra o número de cliques para celular, desktop, tablet, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy e outros. O maior número de aberturas ocorre em dispositivos móveis.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### Engajamento por provedor de caixa de e-mail {#engagement-by-mailbox-provider}

O relatório **Engagement by Mailbox Provider** exibe os principais provedores de caixa de e-mail que contribuem para seus cliques ou aberturas. Você pode clicar em provedores de caixa de e-mail específicos para detalhar domínios de recebimento específicos. Por exemplo, se a Microsoft estiver listada neste relatório como uma das suas principais métricas de provedor de caixa de e-mail, você pode visualizar detalhes dos domínios de recebimento, como "outlook.com", "hotmail.com", "live.com" e outros.

![Um exemplo de relatório de engajamento por provedor de caixa de e-mail com Google, Apple iCloud, Yahoo, Microsoft e Mail.Ru Group e seus respectivos números de cliques.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### Horário de engajamento {#time-of-engagement}

O relatório **Time of Engagement** exibe dados sobre quando os usuários estão interagindo com seus e-mails. Isso pode ajudar a responder perguntas como qual dia da semana ou horário tem o maior engajamento dos seus clientes. Com esses insights, você pode experimentar o melhor dia ou horário para enviar suas mensagens e gerar maior engajamento. Esses horários são baseados no fuso horário da sua empresa.

O relatório de engajamento por **Day of the week** detalha aberturas ou cliques por dia da semana.

![Um exemplo de relatório de engajamento por dia da semana com o maior número de cliques na segunda-feira e quarta-feira.]({% image_buster /assets/img_archive/time_engagement.png %})

O relatório de engajamento por **Time of the day** detalha aberturas ou cliques por cada hora em uma janela de 24 horas.

![Um exemplo de relatório de engajamento por horário do dia com aberturas ou cliques das 0h às 23h.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Para saber mais sobre a análise de dados dos seus e-mails, confira [Relatórios de e-mail]({{site.baseurl}}/user_guide/channels/email/reporting/).

{% endtab %}
{% tab SMS performance %}

### Dashboard de performance de SMS {#sms-performance-dashboard}

Para usar seu dashboard de performance de SMS, acesse **Analytics** > **SMS Performance** e selecione o intervalo de datas do período que deseja visualizar. O intervalo de datas pode ser de até um ano no passado.

![Um exemplo de Campaign de SMS com 335.630 envios, com uma média de 11.187,667 por dia.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Como as métricas são calculadas

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="SMS" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envios | Contagem | Número total de envios em cada dia do intervalo de datas |
| Taxa de entregas confirmadas | Taxa | (Número total de entregas em cada dia do intervalo de datas) / (Número total de envios em cada dia do intervalo de datas) |
| Taxa de falhas de entrega | Taxa | (Número total de falhas em cada dia do intervalo de datas) / (Número total de envios em cada dia do intervalo de datas) |
| Taxa de rejeições | Taxa | (Número total de rejeições em cada dia do intervalo de datas) / (Número total de envios em cada dia do intervalo de datas) |
| Taxa de cliques | Taxa | (Número total de cliques em cada dia do intervalo de datas) / (Número total de entregas em cada dia do intervalo de datas) |
| Total de opt-ins | Taxa | Número total de opt-ins de mensagens recebidas em cada dia do intervalo de datas |
| Total de descadastramentos | Taxa | Número total de descadastramentos de mensagens recebidas em cada dia do intervalo de datas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como as métricas são calculadas" }

{% endtab %}
{% tab Push performance %}

### Dashboard de performance de push {#push-performance-dashboard}

O dashboard **Push Performance** oferece uma visão única no nível do canal sobre o engajamento de push, incluindo envios, bounces, entregas e taxas de aberturas diretas, por influência e totais em um período configurável. Use-o para entender a integridade geral do seu canal de push sem precisar consolidar dados de Campaigns ou Canvas individuais.

Para abrir o dashboard, acesse **Analytics** > **Dashboard Builder** e selecione **Push Channel Dashboard**. O intervalo de datas pode ser de até um ano no passado.

![Um exemplo de Campaign de push com mais de 63 milhões de envios.]({% image_buster /assets/img_archive/push_performance_dashboard.png %})

#### Como as métricas são calculadas

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envios | Contagem | Número total de envios em cada dia do intervalo de datas |
| Taxa de bounce | Taxa | (Número total de bounces em cada dia do intervalo de datas) / (Número total de envios em cada dia do intervalo de datas) |
| Taxa de entrega | Taxa | (Número total de entregas em cada dia do intervalo de datas) / (Número total de envios em cada dia do intervalo de datas) |
| Taxa de aberturas diretas | Taxa | (Número total de aberturas diretas em cada dia do intervalo de datas) / (Número total de entregas em cada dia do intervalo de datas) |
| Taxa de aberturas por influência | Taxa | (Número total de aberturas por influência em cada dia do intervalo de datas) / (Número total de entregas em cada dia do intervalo de datas) |
| Taxa de aberturas totais | Taxa | (Número total de aberturas totais em cada dia do intervalo de datas) / (Número total de entregas em cada dia do intervalo de datas)<br><br>As aberturas totais incluem tanto aberturas diretas quanto aberturas por influência. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como as métricas são calculadas" }

{% endtab %}
{% endtabs %}

## Filtros do dashboard {#dashboard-filters}

Você pode filtrar os dados do seu dashboard usando as seguintes opções de filtro:

- **Tag:** Escolha uma tag. Quando aplicado, seu dashboard mostrará métricas apenas para a tag selecionada.
- **Plataformas:** (Somente no dashboard de performance de push) Escolha uma plataforma de push, como **All Push**, **Android**, **iOS**, **Mobile combined**, **Kindle** ou **Web**. Quando aplicado, seu dashboard exibirá métricas apenas para a plataforma selecionada.
- **Canvas:** Escolha até 10 Canvas. Quando aplicado, seu dashboard mostrará métricas apenas para os Canvas selecionados. Se você selecionar um filtro de tag primeiro, as opções de filtro de Canvas incluirão apenas os Canvas que possuem a tag selecionada.
- **Campaign:** Escolha até 10 Campaigns. Quando aplicado, seu dashboard mostrará métricas apenas para as Campaigns selecionadas. Se você selecionar um filtro de tag primeiro, as opções de filtro de Campaign incluirão apenas as Campaigns que possuem a tag selecionada.

![Opções de filtro no dashboard de performance do canal onde você pode selecionar uma tag e uma lista de Canvas para filtrar.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Comparação de períodos {#comparing-time-periods}

O dashboard de performance do canal compara automaticamente o período selecionado no intervalo de datas com o período anterior, totalizando o mesmo número de dias. Por exemplo, se você escolher "Últimos 7 dias" como intervalo de datas no dashboard, a comparação com o período anterior comparará as métricas dos últimos sete dias com os sete dias anteriores. Se você selecionar um intervalo de datas personalizado — digamos, de 10 a 15 de maio, que corresponde a seis dias de dados — o dashboard comparará as métricas desses dias com as métricas de 4 a 9 de maio.

A comparação é a variação percentual entre o período anterior e o atual, calculada pela diferença entre os dois períodos dividida pela métrica do período anterior.

### Visualizando mudanças em contagens totais e taxas {#viewing-changes-in-total-counts-and-rates}

Você pode alternar entre **Show Change in Totals** — que compara as contagens totais (como o número de e-mails entregues) entre os dois períodos — e **Show Change in Rates** — que compara as taxas (como a taxa de entrega).

![Botões de opção para alternar entre mostrar mudança em totais ou mudança em taxas no dashboard de performance do canal.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Perguntas frequentes {#frequently-asked-questions}

### Por que meu dashboard exibe valores vazios? {#why-is-my-dashboard-displaying-empty-values}

Existem alguns cenários que podem levar a valores vazios para uma métrica:

- A Braze registrou zeros para essa métrica específica no intervalo de datas selecionado.
- Você não enviou nenhuma mensagem durante o intervalo de datas selecionado.
- Embora tenha havido métricas como aberturas, cliques ou cancelamentos de inscrição para o intervalo de datas selecionado, não houve entregas ou envios. Nesse caso, a Braze não calculará uma métrica de taxa.

Para ver mais métricas, tente expandir o intervalo de datas.

### Por que meu dashboard de e-mail exibe mais Outras Aberturas do que Aberturas Únicas? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

Para a métrica _Aberturas Únicas_, a Braze deduplica quaisquer aberturas repetidas registradas por um determinado usuário (sejam elas _Aberturas por Máquina_ ou _Outras Aberturas_), de modo que apenas uma única _Abertura Única_ é contabilizada se um usuário abrir várias vezes. Para _Outras Aberturas_, a Braze não faz deduplicação.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--"

This means Braze hasn't recorded any data for that metric during the time you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/channels/email/) section.

--->