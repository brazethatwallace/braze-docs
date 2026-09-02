---
nav_title: Clarisights
article_title: Clarisights
description: "Este artigo de referência descreve a parceria entre a Braze e a Clarisights, uma plataforma de relatórios de marketing de performance de autoatendimento, permitindo que você importe dados de Campaigns e Canvas da Braze para ajudar a obter uma interface unificada de relatórios de marketing de performance e CRM/retenção."
alias: /partners/clarisights/
page_type: partner
search_tag: Partner

---

# Clarisights

> A [Clarisights](https://clarisights.com) é uma plataforma de relatórios de marketing de performance de autoatendimento para organizações orientadas por dados. Ela integra, processa e visualiza automaticamente todos os seus dados de fontes de marketing, analíticas e de atribuição.

_Esta integração é mantida pela Clarisights._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Clarisights permite que você importe dados de Campaigns e Canvas da Braze para ajudar a obter uma interface unificada de relatórios de marketing de performance e CRM/retenção.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Clarisights | É necessário ter um espaço de trabalho da Clarisights para usar a parceria |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com as seguintes permissões:  <br> - `campaigns.list` <br>  - `campaigns.details`<br> - `campaigns.data_series` <br> - `canvas.details`<br> - `canvas.list` <br>  - `canvas.data_series` <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint REST or transferir estado representacional da Braze | [Sua URL de endpoint REST or transferir estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
| Nome do espaço de trabalho da Braze | O nome do espaço de trabalho associado à chave de API or interface de programação do aplicativo (API) da Braze. Esse nome será usado para identificar a integração do espaço de trabalho na Clarisights. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso {#use-cases}

Com a integração da Braze e da Clarisights, os usuários podem criar diferentes visualizações e tabelas para obter insights das campanhas que criaram. Os casos de uso populares incluem:

{% tabs %}
{% tab Better visibility %}
Melhor visibilidade do desempenho geral de Campaigns e Canvas.

![Um gráfico que mostra um exemplo de melhor visibilidade na plataforma da Clarisights. Esse gráfico inclui estatísticas de aberturas de Campaigns e Canvas, cliques, envios, conversões etc.]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab Granular reporting %}
Relatórios granulares para Campaigns e Canvas.

![Um gráfico que mostra relatórios granulares, como "total enviado por canal de envio" e "taxa de conversão".]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab Unified dashboards %}
Dashboards unificados para CMOs e CXOs.

![Um gráfico que mostra um exemplo de dashboards unificados.]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## Integração {#integration}

Para sincronizar os dados da Braze com a Clarisights, crie um conector da Braze e conecte os espaços de trabalho da Braze.

1. Na Clarisights, navegue até a página **Integrations**, localize o conector **Braze** e selecione **+ Connect**.<br>![Uma lista de conectores disponíveis no marketplace de integrações da Clarisights.]({{site.baseurl}}/assets/img/clarisights/integrations.png)<br><br>
2. Em seguida, usando o fluxo de integração, conecte sua conta da Clarisights à Braze. Isso pode ser feito fornecendo sua chave da API REST da Braze, o nome do espaço de trabalho da Braze e o endpoint REST da Braze.<br>![Conector de espaço de trabalho da Braze na plataforma da Clarisights. Esta página tem campos para o nome do espaço de trabalho da Braze, a chave da API REST da Braze e o endpoint REST da Braze.]({{site.baseurl}}/assets/img/clarisights/braze_flow.png)<br><br>Antes da integração bem-sucedida, os usuários verão os espaços de trabalho conectados na mesma página.<br>![Em "Braze Accounts", você encontrará uma lista de espaços de trabalho conectados.]({{site.baseurl}}/assets/img/clarisights/connected.png)<br><br>

## Usando essa integração {#using-this-integration}

Para incluir a Braze como uma fonte de dados em seus relatórios da Clarisights, navegue até **Create New Report**. Dê um nome ao seu relatório e selecione **Braze** como fonte de dados no prompt que aparece. Você também pode escolher as métricas e dimensões a serem incluídas no relatório. Quando concluído, selecione **Create Report**.

Os dados da Braze começarão a fluir a partir do momento da próxima importação de dados programada. Entre em contato com seu gerente de sucesso do cliente da Clarisights para solicitar backfills por períodos mais longos.

![Configurações de relatório da Clarisights mostrando campos para nome e fonte de dados. Para este exemplo, a Braze é selecionada como a fonte de dados.]({{site.baseurl}}/assets/img/clarisights/braze_report.png)

Visite a Clarisights para saber mais sobre as [métricas e dimensões](https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions) disponíveis ou sobre [a criação de relatórios](https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights).