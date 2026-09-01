---
nav_title: Criador de dashboard
article_title: Criador de dashboard
alias: "/dashboard_builder/"
description: "Este artigo de referência aborda como usar o Criador de dashboard para criar dashboards e visualizações usando relatórios criados no Criador de consultas."
page_type: reference
tool:
    - Reports
page_order: 6
---

# Criador de dashboard {#dashboard-builder}

> Use o Criador de dashboard para criar dashboards e visualizações usando relatórios criados no Criador de relatórios ou no Criador de consultas.

O Criador de dashboard permite que você componha e visualize dashboards de análise de dados personalizados do zero ou a partir de dashboards fornecidos pela Braze. Você pode usar uma fonte de dados sem código (Criador de relatórios) ou uma fonte de dados SQL (Criador de consultas) para alimentar seu dashboard, ou começar a partir de um dos vários dashboards fornecidos pela Braze.

## Criando um dashboard personalizado {#creating-a-custom-dashboard}

1. Acesse **Analytics** > **Dashboard Builder**.
2. Selecione **Create Dashboard**.
3. Selecione qual fonte de dados alimentará seus relatórios:
- **Reports** que foram criados no Report Builder
- **Custom Queries** que foram criadas no Query Builder<br><br>![Janela para selecionar a fonte de dados do seu dashboard.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Agora, siga as etapas correspondentes à sua fonte de dados:

{% tabs %}
{% tab Reports %}

{: start="4"}
4. Selecione **+ Add Tile** e escolha um dos relatórios que você criou no [Report Builder (New)]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

{% alert important %}
Após um relatório do Report Builder ser adicionado a um tile do Dashboard Builder, o tile não fica conectado ao relatório original. Se você editar o relatório original no Report Builder, será necessário excluir o tile existente do dashboard e criar um novo usando o relatório atualizado como fonte de dados.
{% endalert %}

{: start="5"}
5. Selecione o ícone de lápis para alterar como o título e o tipo de gráfico são exibidos no tile.
    - Você pode alternar entre diferentes tipos de gráfico nos controles de tipo de gráfico. As opções atuais incluem gráficos de barras (horizontais ou verticais) e gráficos de linhas (disponíveis apenas se você selecionou **Date** como opção de detalhamento na configuração do Report Builder).<br><br>![Controles para diferentes tipos de gráfico.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    - Use o menu suspenso de métricas para selecionar quais métricas incluir na sua visualização. Por padrão, a primeira coluna do relatório será a métrica exibida.
6. Selecione **Save** após ajustar a visualização conforme desejado.
7. Adicione um nome, uma descrição e uma tag para facilitar a localização do seu dashboard posteriormente.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4. Selecione **+ Add Tile** e escolha uma consulta que você executou no Query Builder.
5. Para editar como os resultados da consulta são exibidos no tile, selecione o ícone de lápis para alterar o título e o tipo de gráfico.
    - Você pode alternar entre diferentes tipos de gráfico nos controles de tipo de gráfico. As opções atuais incluem tabelas, gráficos de barras (horizontais ou verticais) e gráficos de linhas.<br><br>![Controles para diferentes tipos de gráfico.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        - Se você escolher uma das opções de gráfico, use o menu suspenso **X-axis** para selecionar uma única coluna dos resultados da consulta como eixo X.
        - Use o menu suspenso **Y-axis** para selecionar quais métricas incluir na sua visualização. Por padrão, todas as colunas dos resultados da consulta serão exibidas, então desmarque as colunas que você não deseja visualizar.<br><br>![Controles para diferentes tipos de gráfico.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        - (Opcional) Você pode usar o menu suspenso **Grouping** para agrupar os resultados da consulta. Por exemplo, se você tem o ID de Campaign como resultado de coluna e deseja somar todas as linhas com esse valor, use o menu suspenso **Grouping**.
        - (Opcional) Para editar os dados exibidos, selecione a consulta vinculada ao visual e faça suas edições no [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder).
6. Selecione **Save** após ajustar a visualização conforme desejado.
7. Adicione um nome, uma descrição e uma tag para facilitar a localização do seu dashboard posteriormente.
{% endtab %}
{% endtabs %}

{: start="8"}
8. Repita as etapas 4 a 7 do respectivo método até criar o dashboard desejado.
9. Selecione **View Dashboard** > selecione **Run Dashboard**.

Seu dashboard pode levar alguns minutos para concluir a geração dos relatórios.

{% alert note %}
Você pode adicionar até 10 tiles a um dashboard.
{% endalert %}

## Gerenciando blocos do dashboard {#managing-dashboard-tiles}

### Excluir blocos {#delete-tiles}

Exclua um bloco do dashboard selecionando **Delete Tile** na parte inferior do bloco. **Essa ação não pode ser revertida.**

### Duplicar blocos {#duplicate-tiles}

Faça uma cópia do seu bloco selecionando **Duplicate Tile** na parte inferior do bloco.

### Ajustar tamanho e posição do bloco {#adjust-tile-size-and-position}

Ajuste o tamanho do bloco arrastando a alça de redimensionamento e ajuste a posição do bloco no dashboard arrastando a alça do bloco.

## Executando um dashboard {#running-a-dashboard}

1. Acesse **Analytics** > **Dashboard Builder**. A página inicial lista todos os dashboards existentes no seu espaço de trabalho, com os dashboards criados pela Braze no topo. Eles são identificados com "(Braze)" no título.
2. Selecione o dashboard desejado.
3. Selecione **Run Dashboard** para carregar o respectivo dashboard.

### Dashboards disponíveis {#available-dashboards}

A Braze oferece dashboards pré-criados para casos de uso frequentes. Use a tabela a seguir como referência única para os dashboards documentados atualmente e como acessar cada um.

| Dashboard | Caminho de acesso | Documentação |
| --- | --- | --- |
| Revenue - Last Touch Attribution | **Analytics** > **Dashboard Builder** | [Revenue - Last Touch Attribution](#revenue---last-touch-attribution) |
| Devices and carriers | **Analytics** > **Dashboard Builder** | [Devices and carriers](#devices-and-carriers) |
| Segment Insights - Email | **Analytics** > **Dashboard Builder** | [Segment Insights - Email](#segment-insights---email) |
| Session Analytics | **Analytics** > **Dashboard Builder** | [Session Analytics](#session-analytics) |
| eCommerce Revenue - Last Touch Attribution | **Analytics** > **Dashboard Builder** | [Dashboard de receita de eCommerce]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/ecommerce_revenue_dashboard) |
| Messaging Diagnostics | **Analytics** > **Dashboard Builder** | [Dashboard de diagnóstico de envio de mensagens]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) |
| Industry Benchmarks | **Analytics** > **Dashboard Builder** | [Dashboard de benchmarks do setor]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/industry_benchmarks_dashboard) |
| Email performance | **Analytics** > **Email Performance** | [Dashboards de desempenho de canal]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#email-performance-dashboard) |
| SMS performance | **Analytics** > **SMS Performance** | [Dashboards de desempenho de canal]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#sms-performance-dashboard) |
| Push performance | **Analytics** > **Dashboard Builder** > **Push Channel Dashboard** | [Dashboards de desempenho de canal]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#push-performance-dashboard) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dashboards disponíveis" }

{% alert note %}
A opção de editar dashboards criados pela Braze ainda não está disponível. Entre em contato com seu gerente de sucesso do cliente se desejar solicitar dashboards adicionais.
{% endalert %}

#### Revenue - Last Touch Attribution {#revenue---last-touch-attribution}

O dashboard **Revenue - Last Touch Attribution** oferece uma visão geral da receita em Campaigns, Canvas e canais. Todos os dados de receita são atribuídos à última mensagem com a qual o usuário interagiu dentro da janela de atribuição.

As interações incluem _Email Click_ (clique em link), _Content Card Click_, _In-App Message Click_ (excluindo botões de fechar), _Push Opens_, _SMS Short Link Click_, _WhatsApp Read_ e _Webhook Send_.

| Métrica | Definição |
| --- | --- |
| Receita total de último ponto de contato | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato dentro do intervalo de datas e janela de atribuição selecionados. |
| Total de conversões de compra | Contagem de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado. |
| Média de dias para conversão | Tempo médio entre todos os eventos de compra de Campaigns e Canvas com um evento de último ponto de contato qualificado. |
| Receita por destinatário | Soma da receita de eventos de receita qualificados dividida pelo número de usuários únicos que receberam uma mensagem dentro do intervalo de datas. |
| Compradores únicos | Contagem de usuários únicos com um evento de receita qualificado. |
| Receita por país | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato, agrupada por país. |
| Receita por Campaign | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado, agrupada por Campaign. |
| Receita por variante de Campaign | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado, agrupada por variante de campanha. |
| Receita por Canvas | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado, agrupada por Canvas. |
| Receita por variante de Canvas | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado, agrupada por variante de Canvas. |
| Compras por produto | Contagem de todas as compras agrupadas por produto. |
| Receita por canal | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado, agrupada por canal. |
| Série temporal de receita | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado, agrupada por dia em UTC. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Revenue - Last Touch Attribution" }

#### Devices and carriers {#devices-and-carriers}

| Métrica | Definição |
| --- | --- |
| Operadoras de dispositivos | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupada por operadora do dispositivo. |
| Modelo do dispositivo | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupada por modelo do dispositivo. |
| Sistema operacional do dispositivo | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupada por sistema operacional do dispositivo. |
| Tamanho da tela do dispositivo | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupada por resolução (tamanho) da tela do dispositivo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Devices and carriers" }

#### Segment Insights - Email {#segment-insights---email}

| Métrica | Definição |
|---|---|
| Métricas semanais de e-mail (taxas) | Taxas de engajamento de e-mail (entrega, bounce, abertura, clique, cancelamento de inscrição) agrupadas por segmento e exibidas como série temporal semanal. |
| Métricas semanais de e-mail (contagens) | Contagens de engajamento de e-mail (enviados, entregues, bounces, aberturas, cliques, cancelamentos de inscrição) agrupadas por segmento e exibidas como série temporal semanal. |
| Métricas semanais de compra (taxas) | Taxas de conversão de compra (receita por destinatário) a partir de aberturas e cliques de e-mail, agrupadas por segmento e exibidas como série temporal semanal. |
| Métricas semanais de compra (contagens) | Contagens de compras e totais de receita a partir de aberturas e cliques de e-mail, agrupados por segmento e exibidos como série temporal semanal. |
| Engajamento de e-mail por segmento | Tabela resumida mostrando métricas totais de engajamento de e-mail (enviados, entregues, bounces, aberturas, cliques, cancelamentos de inscrição e suas taxas) agregadas por segmento. |
| Compras e receita por segmento | Tabela resumida mostrando métricas totais de compra (compras, receita e receita por destinatário) a partir de aberturas e cliques de e-mail, agregadas por segmento. |
| Top 10 Campaigns por métricas de engajamento | Lista classificada de Campaigns com as maiores métricas de engajamento de e-mail (métrica configurável para classificação). |
| 10 piores Campaigns por métricas de engajamento | Lista classificada de Campaigns com as menores métricas de engajamento de e-mail (métrica configurável para classificação). |
| Top 10 Canvas por métricas de engajamento | Lista classificada de Canvas com as maiores métricas de engajamento de e-mail (métrica configurável para classificação). |
| 10 piores Canvas por métricas de engajamento | Lista classificada de Canvas com as menores métricas de engajamento de e-mail (métrica configurável para classificação). |
| Top 10 Campaigns por métricas de compra | Lista classificada de Campaigns com as maiores métricas de conversão de compra a partir de engajamento de e-mail (métrica configurável para classificação). |
| 10 piores Campaigns por métricas de compra | Lista classificada de Campaigns com as menores métricas de conversão de compra a partir de engajamento de e-mail (métrica configurável para classificação). |
| Top 10 Canvas por métricas de compra | Lista classificada de Canvas com as maiores métricas de conversão de compra a partir de engajamento de e-mail (métrica configurável para classificação). |
| 10 piores Canvas por métricas de compra | Lista classificada de Canvas com as menores métricas de conversão de compra a partir de engajamento de e-mail (métrica configurável para classificação). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment Insights - Email" }

#### Session Analytics {#session-analytics}

| Métrica | Definição |
|---|---|
| Nº de sessões por dia (série temporal) | Contagem de sessões únicas agrupadas por dia dentro do intervalo de datas selecionado, exibida como série temporal. |
| Média de sessões por usuário | Número médio de sessões por usuário, calculado como total de sessões dividido por usuários únicos dentro do intervalo de datas selecionado. |
| Campaigns que convertem em sessões | Contagem de sessões únicas que ocorreram ao mesmo tempo que conversões de Campaign, agrupadas por ID de Campaign e classificadas por contagem de sessões. |
| Canvas que convertem em sessões | Contagem de sessões únicas que ocorreram ao mesmo tempo que conversões de Canvas, agrupadas por ID de Canvas e classificadas por contagem de sessões. |
| Total de sessões por usuário | Lista dos 1.000 principais usuários por contagem total de sessões dentro do intervalo de datas selecionado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Session Analytics" }

## Compartilhe seu feedback conosco {#share-your-feedback-with-us}

{% multi_lang_include product_feedback_cta.md context="pain_point" channel="ux" feature="Dashboard Builder" %}