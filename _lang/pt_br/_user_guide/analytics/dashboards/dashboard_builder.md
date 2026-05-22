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

1. Acesse **Analytics** > **Criador de dashboard**.
2. Selecione **Create Dashboard**.
3. Selecione qual fonte de dados alimentará seus relatórios:
- **Reports** que foram criados no Criador de relatórios
- **Custom Queries** que foram criadas no Criador de consultas<br><br>![Janela para selecionar a fonte de dados do seu dashboard.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Agora, siga as etapas correspondentes à sua fonte de dados:

{% tabs %}
{% tab Reports %}

{: start="4"}
4. Selecione **+ Add Tile** e escolha um dos relatórios que você criou no [Criador de relatórios (Novo)]({{site.baseurl}}/user_guide/analytics/reports/report_builder/).

{% alert important %}
Depois que um relatório do Criador de relatórios é adicionado a um bloco do Criador de dashboard, o bloco não fica conectado ao relatório original. Se você editar o relatório original no Criador de relatórios, será necessário excluir o bloco existente do dashboard e criar um novo usando o relatório atualizado como fonte de dados.
{% endalert %}

{: start="5"}
5. Selecione o ícone de lápis para alterar como o título e o tipo de gráfico são exibidos no bloco.
    - Você pode alternar entre diferentes tipos de gráfico abaixo da visualização padrão. As opções atuais incluem gráficos de barras (horizontais ou verticais) e gráficos de linhas (disponíveis apenas se você selecionou **Date** como opção de detalhamento na configuração do Criador de relatórios).<br><br>![Alternadores para diferentes tipos de gráfico.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    - Use o menu suspenso de métricas para selecionar quais métricas incluir na sua visualização. Por padrão, a primeira coluna do relatório será a métrica exibida.
6. Selecione **Save** depois de ajustar a visualização conforme desejado.
7. Adicione um nome, uma descrição e uma tag para facilitar a localização do seu dashboard posteriormente.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4. Selecione **+ Add Tile** e escolha uma consulta que você executou no Criador de consultas.
5. Para editar como os resultados da consulta são exibidos no bloco, selecione o ícone de lápis para alterar o título e o tipo de gráfico.
    - Você pode alternar entre diferentes tipos de gráfico abaixo da visualização padrão. As opções atuais incluem tabelas, gráficos de barras (horizontais ou verticais) e gráficos de linhas.<br><br>![Alternadores para diferentes tipos de gráfico.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        - Se você escolher uma das opções de gráfico, use o menu suspenso **X-axis** para selecionar uma única coluna dos resultados da consulta para usar como eixo X.
        - Use o menu suspenso **Y-axis** para selecionar quais métricas incluir na sua visualização. Por padrão, todas as colunas dos resultados da consulta serão exibidas, então desmarque as colunas que você não deseja visualizar.<br><br>![Alternadores para diferentes tipos de gráfico.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        - (Opcional) Você pode usar o menu suspenso **Grouping** para agrupar os resultados da consulta. Por exemplo, se você tem o ID da campanha como resultado de coluna e deseja somar todas as linhas com esse valor, use o menu suspenso **Grouping**.
        - (Opcional) Para editar os dados exibidos, selecione a consulta vinculada ao visual e faça suas edições no [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/).
6. Selecione **Save** depois de ajustar a visualização conforme desejado.
7. Adicione um nome, uma descrição e uma tag para facilitar a localização do seu dashboard posteriormente.
{% endtab %}
{% endtabs %}

{: start="8"}
8. Repita as etapas 4 a 7 para o método correspondente até criar o dashboard desejado.
9. Selecione **View Dashboard** > selecione **Run Dashboard**.

Seu dashboard pode levar alguns minutos para concluir a geração dos relatórios.

{% alert note %}
Você pode adicionar até 10 blocos a um dashboard.
{% endalert %}

## Gerenciando blocos do dashboard {#managing-dashboard-tiles}

### Excluir blocos {#delete-tiles}

Exclua um bloco do dashboard selecionando **Delete Tile** na parte inferior do bloco. **Essa ação não pode ser revertida.**

### Duplicar blocos {#duplicate-tiles}

Faça uma cópia do seu bloco selecionando **Duplicate Tile** na parte inferior do bloco.

### Ajustar tamanho e posição dos blocos {#adjust-tile-size-and-position}

Ajuste o tamanho do bloco arrastando o canto inferior direito do bloco e ajuste a posição do bloco no dashboard arrastando a alça no canto superior direito do bloco.

## Executando um dashboard {#running-a-dashboard}

1. Acesse **Analytics** > **Criador de dashboard**. A página inicial lista todos os dashboards existentes no seu espaço de trabalho, com os dashboards criados pela Braze no topo. Eles são identificados com "(Braze)" no título.
2. Selecione o dashboard desejado.
3. Selecione **Run Dashboard** para carregar o dashboard correspondente.

### Dashboards disponíveis {#available-dashboards}

A Braze fornece dashboards pré-criados para casos de uso frequentes, como análise de receita usando atribuição de último ponto de contato. A capacidade de editar um dashboard ainda não está disponível. Fale com seu gerente de sucesso do cliente se quiser ver determinado dashboard no futuro.

#### Receita - Atribuição de último ponto de contato {#revenue-last-touch-attribution}

O dashboard **Revenue - Last Touch Attribution** fornece uma revisão da receita em Campaigns, Canvas e canais. Todos os dados de receita são atribuídos à última mensagem tocada durante o período de atribuição.

Os pontos de contato incluem _Clique em e-mail_ (clique em link), _Clique em cartão de conteúdo_, _Clique em mensagem no app_ (excluindo botões de fechar), _Aberturas de push_, _Clique em link curto de SMS_, _Leitura de WhatsApp_ e _Envio de Webhook_.

| Métrica | Definição |
| --- | --- |
| Receita total de último ponto de contato | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato dentro do intervalo de datas e período de atribuição selecionados. |
| Total de conversões de compra | Contagem de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado. |
| Média de dias para conversão | Tempo médio entre todos os eventos de compra de Campaigns e Canvas com um evento de último ponto de contato qualificado. |
| Receita por destinatário | Soma da receita de eventos de receita qualificados dividida pelo número de usuários únicos que receberam uma mensagem dentro do intervalo de datas. |
| Compradores únicos | Contagem de usuários únicos com um evento de receita qualificado. |
| Receita por país | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato, agrupados por país. |
| Receita por Campaign | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado, agrupados por Campaign. |
| Receita por variante de Campaign | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado, agrupados por variante de Campaign. |
| Receita por Canvas | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado, agrupados por Canvas. |
| Receita por variante de Canvas | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado, agrupados por variante de Canvas. |
| Compras por produto | Contagem de todas as compras agrupadas por produto. |
| Receita por canal | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado, agrupados por canal. |
| Série temporal de receita | Soma de todos os eventos de receita de Campaigns e Canvas com um evento de último ponto de contato qualificado, agrupados por dia em UTC. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Revenue - Last Touch Attribution" }

#### Dispositivos e operadoras {#devices-and-carriers}

| Métrica | Definição |
| --- | --- |
| Operadoras de dispositivos | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados por operadora do dispositivo. |
| Modelo do dispositivo | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados por modelo do dispositivo. |
| Sistema operacional do dispositivo | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados por sistema operacional do dispositivo. |
| Tamanho da tela do dispositivo | Contagem de usuários no intervalo de datas selecionado que abriram uma notificação por push, agrupados por resolução de tela (tamanho) do dispositivo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Devices and carriers" }

#### Insights de segmento - E-mail {#segment-insights-email}

| Métrica  | Definição  |
|---|---|
| Métricas semanais de e-mail (taxas) | Taxas de engajamento de e-mail (entrega, bounce, abertura, clique, taxas de cancelamento de inscrição) agrupadas por segmento e exibidas como série temporal semanal.|
| Métricas semanais de e-mail (contagens) | Contagens de engajamento de e-mail (enviados, entregues, bounces, aberturas, cliques, cancelamentos de inscrição) agrupadas por segmento e exibidas como série temporal semanal.|
| Métricas semanais de compra (taxas) | Taxas de conversão de compra (receita por destinatário) a partir de aberturas e cliques de e-mail, agrupadas por segmento e exibidas como série temporal semanal.|
| Métricas semanais de compra (contagens) | Contagens de compras e totais de receita a partir de aberturas e cliques de e-mail, agrupados por segmento e exibidos como série temporal semanal.|
| Engajamento de e-mail por segmento | Tabela resumida mostrando métricas totais de engajamento de e-mail (enviados, entregues, bounces, aberturas, cliques, cancelamentos de inscrição e suas taxas) agregadas por segmento.|
| Compras e receita por segmento | Tabela resumida mostrando métricas totais de compra (compras, receita e receita por destinatário) a partir de aberturas e cliques de e-mail, agregadas por segmento.|
| Top 10 Campaigns para métricas de engajamento | Lista classificada de Campaigns com as maiores métricas de engajamento de e-mail (métrica configurável para classificação).|
| 10 piores Campaigns para métricas de engajamento | Lista classificada de Campaigns com as menores métricas de engajamento de e-mail (métrica configurável para classificação).|
| Top 10 Canvas para métricas de engajamento | Lista classificada de Canvas com as maiores métricas de engajamento de e-mail (métrica configurável para classificação).|
| 10 piores Canvas para métricas de engajamento | Lista classificada de Canvas com as menores métricas de engajamento de e-mail (métrica configurável para classificação).|
| Top 10 Campaigns para métricas de compra | Lista classificada de Campaigns com as maiores métricas de conversão de compra a partir de engajamento de e-mail (métrica configurável para classificação).|
| 10 piores Campaigns para métricas de compra | Lista classificada de Campaigns com as menores métricas de conversão de compra a partir de engajamento de e-mail (métrica configurável para classificação).|
| Top 10 Canvas para métricas de compra | Lista classificada de Canvas com as maiores métricas de conversão de compra a partir de engajamento de e-mail (métrica configurável para classificação).|
| 10 piores Canvas para métricas de compra | Lista classificada de Canvas com as menores métricas de conversão de compra a partir de engajamento de e-mail (métrica configurável para classificação).|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment Insights - Email" }

#### Análise de sessões {#session-analytics}

| Métrica | Definição  |
|---|---|
| Nº de sessões por dia (série temporal) | Contagem de sessões únicas agrupadas por dia dentro do intervalo de datas selecionado, exibidas como série temporal.|
| Média de sessões por usuário | Número médio de sessões por usuário, calculado como total de sessões dividido por usuários únicos dentro do intervalo de datas selecionado.|
| Campaigns que convertem em sessões | Contagem de sessões únicas que ocorreram ao mesmo tempo que conversões de Campaign, agrupadas por ID de Campaign e classificadas por contagem de sessões.|
| Canvas que convertem em sessões | Contagem de sessões únicas que ocorreram ao mesmo tempo que conversões de Canvas, agrupadas por ID de Canvas e classificadas por contagem de sessões.|
| Nº total de sessões por usuário | Lista dos 1.000 principais usuários por contagem total de sessões dentro do intervalo de datas selecionado.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Session Analytics" }

## Compartilhe seu feedback conosco {#share-your-feedback-with-us}

Selecione o botão **Enviar feedback** ou fale com seu gerente de sucesso do cliente para compartilhar seu feedback conosco.