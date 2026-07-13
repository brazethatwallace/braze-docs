---
nav_title: Modelos de consulta
article_title: Modelos do Criador de consultas
page_order: 1
page_type: reference
toc_headers: h2
description: "Este artigo de referência lista os tipos de relatórios que você pode criar usando dados da Braze no Snowflake por meio do Criador de consultas."
tool: Reports
---

# Modelos do Criador de consultas {#query-builder-templates}

> Acesse os modelos do [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) selecionando **Query Template** ao criar um relatório. Todos os modelos exibem dados de até os últimos 60 dias, mas você pode editar esse e outros valores diretamente no editor.<br><br>Para ver as definições das métricas que podem aparecer nos seus relatórios do Criador de consultas, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary) e filtre pelo canal correspondente.

## Modelos de canal {#channel-templates}

<style>
table th:nth-child(1) {
    width: 30%;
}
table th:nth-child(2) {
    width: 70%;
}
table td {
    word-break: break-word;
}
</style>

| Nome da consulta | Descrição |
| --- | --- |
| Engajamento e receita por canal | Este relatório mostra, para cada canal, todas as métricas de engajamento (como aberturas e cliques), receita, número de transações e preço médio. {::nomarkdown} <ul> <li> <i>Número de transações:</i> Número de eventos de compra </li> <li> <i>Preço médio:</i> Receita dividida pelas transações </li> </ul> {:/} ![Captura de tela relacionada aos modelos de canal.]({% image_buster /assets/img_archive/channel_engagement_revenue.png %}) |
| Compras e receita por segmento | Este relatório mostra métricas das mensagens enviadas para um segmento específico. <br><br> As métricas de compra são únicas ao longo do período do relatório. Um usuário pode gerar no máximo uma compra. A receita leva em conta todas as compras do período do relatório. |
| Compras e receita por variantes ou etapas, por segmento | Este relatório mostra métricas das variantes ou etapas do Canvas das mensagens enviadas para cada segmento. <br><br> As métricas de compra são únicas ao longo do período do relatório. Um usuário pode gerar no máximo uma compra. A receita leva em conta todas as compras do período do relatório. |
| Melhores/piores mensagens para compras | Este relatório mostra métricas de compra para as melhores ou piores Campaigns, Canvas ou etapas do Canvas. Cada linha é uma Campaign, um Canvas ou uma etapa do Canvas. Você deve especificar se deseja exibir os melhores ou piores desempenhos e a métrica específica para executar essa análise (como *Compras únicas após recebimento*, *Receita após recebimento*, *Destinatários únicos*). <br><br> As linhas nos relatórios de melhores desempenhos serão ordenadas do melhor para o pior, enquanto as linhas nos relatórios de piores desempenhos serão ordenadas do pior para o melhor. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelos de canal" }

## Modelos de Campaign {#campaign-templates}

| Nome da consulta | Descrição |
| --- | --- |
| Receita de Campaign por país | Este relatório mostra a receita por país para uma Campaign específica. Para executar este relatório, você deve especificar o identificador de API de uma Campaign. Você pode encontrar o identificador de API de uma Campaign na parte inferior da página de detalhes dessa Campaign. <br><br> Este relatório mostra, para cada país, o valor da receita gerada, número de pedidos, número de devoluções, receita líquida e receita bruta.<br><br> {::nomarkdown} <ul> <li> <i>Pedidos:</i> Número de eventos de compra </li> <li><i> Devoluções:</i> Número de eventos de compra com valores de receita negativos </li> <li><i> Receita líquida:</i> Receita de todas as não devoluções </li> <li><i> Receita bruta:</i> Receita que inclui o valor das devoluções </li></ul>{:/} ![Captura de tela relacionada aos modelos de Campaign.]({% image_buster /assets/img_archive/campaign_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelos de Campaign" }

## Modelos de Canvas {#canvas-templates}

| Nome da consulta | Descrição |
| --- | --- |
| Receita de Canvas por país | Este relatório mostra a receita por país para um Canvas específico. Para executar este relatório, você deve especificar o identificador de API de um Canvas. Você pode encontrar o identificador de API do Canvas em **Analyze Variants**. <br><br> Este relatório mostra, para cada país, o valor da receita gerada, número de pedidos, número de devoluções, receita líquida e receita bruta.<br><br> {::nomarkdown} <ul> <li> <i>Pedidos:</i> Número de eventos de compra </li> <li><i> Devoluções:</i> Número de eventos de compra com valores de receita negativos </li> <li><i> Receita líquida:</i> Receita de todas as não devoluções </li> <li><i> Receita bruta:</i> Receita que inclui o valor das devoluções </li></ul>{:/} ![Captura de tela relacionada aos modelos de Canvas.]({% image_buster /assets/img_archive/canvas_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelos de Canvas" }

## Modelos de e-mail {#email-templates}

| Nome da consulta | Descrição |
| --- | --- |
| Bounces de e-mail por domínio | O número de bounces por domínio de e-mail, dividido em total de bounces, hard bounces e soft bounces. <br> ![Captura de tela relacionada aos modelos de e-mail.]({% image_buster /assets/img_archive/query_builder_q4.png %}){: style="max-width:60%;"} |
| Métricas de entrega de e-mail por dia | Este relatório mostra métricas das mensagens enviadas em cada dia, como quantos e-mails foram enviados, entregues, tiveram soft bounce e hard bounce. <br><br> Todas as métricas são únicas ao longo do período do relatório. Por exemplo, se um e-mail de boas-vindas teve soft bounce uma vez em 21 de novembro, duas vezes em 22 de novembro e nunca foi entregue: {::nomarkdown} <ul><li> A métrica de <i>Soft Bounces</i> de 21 de novembro aumenta em um.</li><li> A métrica de <i>Soft Bounces</i> de 22 de novembro não é afetada. </li></ul>{:/} ![Captura de tela relacionada aos modelos de e-mail.]({% image_buster /assets/img_archive/email_delivery_day.png %})|
| Métricas de engajamento de e-mail por segmento | Este relatório mostra métricas das mensagens enviadas para cada segmento, como quantos e-mails foram enviados, entregues, tiveram soft bounce e hard bounce. <br><br> Todas as métricas são únicas ao longo do período do relatório. Por exemplo, se um e-mail de boas-vindas teve soft bounce uma vez em 21 de novembro, duas vezes em 22 de novembro e nunca foi entregue: {::nomarkdown} <ul><li> A métrica de <i>Soft Bounces</i> de 21 de novembro aumenta em um. </li><li> A métrica de <i>Soft Bounces</i> de 22 de novembro não é afetada.</li></ul>{:/} ![Captura de tela relacionada aos modelos de e-mail.]({% image_buster /assets/img_archive/email_engagement_segment.png %}) |
| Métricas de engajamento de e-mail por variantes ou etapas, por segmento | Este relatório mostra métricas das variantes ou etapas do Canvas das mensagens enviadas para cada segmento. Essas métricas incluem quantos e-mails foram enviados, entregues, tiveram soft bounce e hard bounce. <br><br> Todas as métricas são únicas ao longo do período do relatório. Por exemplo, se um e-mail de boas-vindas teve soft bounce uma vez em 21 de novembro, duas vezes em 22 de novembro e nunca foi entregue: {::nomarkdown} <ul><li> A métrica de <i>Soft Bounces</i> de 21 de novembro aumenta em um. </li> <li> A métrica de <i>Soft Bounces</i> de 22 de novembro não é afetada.</li></ul> {:/} |
| Desempenho de e-mail por país | Este relatório mostra as seguintes métricas para cada país: envios, taxa de abertura indireta e taxa de abertura direta. O país é o país do usuário no momento do envio do e-mail. <br><br> ![Captura de tela relacionada aos modelos de e-mail.]({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| Registros de alteração de inscrição de e-mail | Este relatório mostra as métricas registradas sobre cada alteração de inscrição do usuário, como endereço de e-mail, status de inscrição, horário em que o status foi alterado e o Canvas ou a Campaign associada. |
| Opt-ins e opt-outs de grupo de inscrições de e-mail | Este relatório mostra o número de opt-ins e opt-outs de usuários únicos para qualquer grupo de inscrições de e-mail em cada semana. Você deve ter pelo menos um [grupo de inscrições de e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions) no espaço de trabalho para executar esta consulta. <br><br> ![Captura de tela relacionada aos modelos de e-mail.]({% image_buster /assets/img_archive/query_builder_q2.png %}){: style="max-width:70%;"} |
| URLs de e-mail clicadas | Este relatório mostra o número de cliques que cada link em um e-mail recebeu. Para executar este relatório, você precisará especificar o identificador de API de uma Campaign ou Canvas. Você pode encontrar o identificador de API de uma Campaign na parte inferior da página de detalhes dessa Campaign e o identificador de API do Canvas em **Analyze Variants**. <br><br> Este relatório mostra links despersonalizados e uma contagem de cliques para cada link. O download do CSV incluirá os IDs dos usuários que clicaram, o link em que clicaram e o registro de data e hora de quando clicaram. <br><br> *URLs despersonalizadas:* URLs das quais as tags Liquid foram removidas. <br><br> ![Captura de tela relacionada aos modelos de e-mail.]({% image_buster /assets/img_archive/query_builder_q5.png %}){: style="max-width:70%;"} |
| Melhores/piores mensagens para engajamento de e-mail | Este relatório mostra métricas de engajamento de e-mail para as melhores ou piores Campaigns, Canvas ou etapas do Canvas. Você deve especificar se deseja exibir os melhores ou piores desempenhos e a métrica específica para executar essa análise (como *Enviados*, *Soft Bounces* e *Aberturas únicas*). <br><br> As linhas nos relatórios de melhores desempenhos serão ordenadas do melhor para o pior, enquanto as linhas nos relatórios de piores desempenhos serão ordenadas do pior para o melhor. <br><br> ![Captura de tela relacionada aos modelos de e-mail.]({% image_buster /assets/img_archive/top-bottom-email.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelos de e-mail" }

## Modelos para dispositivos móveis {#mobile-templates}

| Nome da consulta | Descrição |
| --- | --- |
| Operadoras de dispositivos | O número de usuários por operadora de dispositivo, como Verizon e T-Mobile. <br><br> ![Captura de tela relacionada aos modelos para dispositivos móveis.]({% image_buster /assets/img_archive/device_carriers.png %}){: style="max-width:50%;"} |
| Modelos de dispositivos | O número de usuários por modelo de dispositivo, como iPhone 15 Pro e Pixel 7. <br><br> ![Captura de tela relacionada aos modelos para dispositivos móveis.]({% image_buster /assets/img_archive/device_models.png %}){: style="max-width:50%;"} |
| Sistemas operacionais de dispositivos | O número de usuários por sistema operacional, como 17.4 e Android 14. <br><br> ![Captura de tela relacionada aos modelos para dispositivos móveis.]({% image_buster /assets/img_archive/os_version.png %}){: style="max-width:50%;"} |
| Resoluções de tela de dispositivos | O número de usuários por resolução de tela do dispositivo, como 1179x2556 e 750x1334. <br><br> ![Captura de tela relacionada aos modelos para dispositivos móveis.]({% image_buster /assets/img_archive/device_screen_resolutions.png %}){: style="max-width:40%;"} |
| Códigos de erro de SMS | Este relatório mostra o tipo de erro e o número de erros para cada código de erro de SMS. <br><br>![Captura de tela relacionada aos modelos para dispositivos móveis.]({% image_buster /assets/img_archive/sms_errors.png %}){: style="max-width:50%;"} |
| Erros de provedor de SMS por usuário | Este relatório mostra os códigos de erro de SMS para um usuário específico. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelos para dispositivos móveis" }

## Modelos de push {#push-templates}

| Nome da consulta | Descrição |
| --- | --- |
| Desempenho de push por país | Este relatório mostra as seguintes métricas para cada país: entregas, taxa de abertura e taxa de cliques. O país é o país do usuário no momento do envio do e-mail. <br><br> ![Captura de tela relacionada aos modelos de push.]({% image_buster /assets/img_archive/query_builder_q7.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelos de push" }

## Detalhamento por segmento {#segment-breakdown}

| Nome da consulta | Descrição |
| -- | -- |
| Métricas de engajamento de e-mail por segmento | Este relatório mostra métricas de desempenho de e-mail detalhadas por segmento no nível de Campaign ou Canvas. |
| Compras e receita por segmento | Este relatório mostra métricas de compra e receita detalhadas por segmento para uma Campaign ou Canvas específico. |
| Melhores/piores mensagens para engajamento de e-mail | Este relatório mostra as Campaigns, Canvas ou etapas do Canvas que tiveram os melhores ou piores desempenhos para uma métrica de engajamento de e-mail especificada. |
| Melhores/piores mensagens para compras | Este relatório mostra as Campaigns, Canvas ou etapas do Canvas que tiveram os melhores ou piores desempenhos para uma métrica de compra ou receita especificada. |
| Desempenho de push por segmento | Este relatório mostra métricas de push detalhadas por segmento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalhamento por segmento" }