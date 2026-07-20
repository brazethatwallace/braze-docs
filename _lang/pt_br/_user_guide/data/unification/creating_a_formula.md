---
nav_title: Criar uma fórmula
article_title: Criar uma fórmula
page_order: 3
page_type: reference
description: "Este artigo de referência aborda a criação e o gerenciamento de fórmulas, que ajudam você a entender facilmente as relações complexas existentes em seus dados."
tool: Reports

---
# Criar uma fórmula {#create-a-formula}

> Ao visualizar a análise de dados na Braze, é possível combinar vários pontos de dados para obter insights valiosos sobre os dados de usuários. Esses recursos são chamados de fórmulas. Use fórmulas para normalizar os dados da série temporal com base no número total de usuários ativos mensais (MAU) e usuários ativos diários (DAU).

As fórmulas ajudam você a entender as relações complexas que existem em seus dados. Por exemplo, é possível comparar quantos eventos personalizados foram concluídos por usuários ativos diários que se qualificam para um determinado segmento em comparação com a população geral (ou com outro segmento).

## Casos de uso {#use-cases}

As fórmulas, especialmente quando combinadas com eventos personalizados, podem ajudar você a entender o comportamento do usuário em seu app. As fórmulas também podem fornecer insights mais profundos sobre os padrões de compra do segmento, mesmo que sua empresa use mídia paga em conjunto com a Braze, como o Google Ads ou a TV.

A seguir, alguns exemplos dos tipos de padrões de comportamento que podem ser detectados com o uso de fórmulas:

- **Apps de viagem por aplicativo:** Se você tiver um evento personalizado para quando o usuário cancelar uma viagem, poderá configurar uma função para Canceled Rides / DAU para descobrir se determinados segmentos de usuários tendem a cancelar mais viagens do que outros.
- **Apps de e-commerce:** Ao configurar uma função para compras de um determinado ID de produto / MAU, você pode comparar a popularidade de um produto promovido recentemente entre segmentos, mesmo que todas as promoções não possam ser rastreadas usando a Braze.
- **Apps de mídia que usam anúncios:** Se a experiência dos usuários for interrompida por anúncios entre clipes de vídeo ou áudio, registrar as saídas no meio do anúncio como um evento personalizado e calcular a proporção de saídas no meio do anúncio / DAU pode ajudar a encontrar os melhores segmentos para direcionamento com uma Campaign de inscrições premium sem anúncios.

## Criação de fórmulas {#creating-formulas}

As fórmulas podem ser acessadas nos painéis de estatísticas nas páginas [Página inicial]({{site.baseurl}}/user_guide/analytics/dashboards/home), [Relatório de receitas]({{site.baseurl}}/user_guide/analytics/reports/revenue_report) e [Relatório de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) no dashboard. Para visualizar esse painel, acesse o gráfico **Performance Over Time**, altere o menu suspenso **Statistics For** para **KPI Formulas** e selecione pelo menos uma fórmula de KPI para preencher o gráfico.

![Exibir estatísticas para fórmulas de KPI no dashboard da Braze]({% image_buster /assets/img_archive/kpi_forms.png %})

Para criar uma nova fórmula:

1. Acesse o dashboard apropriado (**Home**, **Revenue Report** ou **Custom Events Report**).
2. Selecione **Manage KPI Formulas**.
3. Digite um nome para sua fórmula.
4. Selecione os numeradores e denominadores relevantes.
5. Selecione **Save**.

## Numeradores e denominadores disponíveis {#available-numerators-and-denominators}

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

### Dashboard de visão geral {#overview-dashboard}

| Numeradores | Denominadores |
| --- | --- |
| DAU | MAU |
| Sessões | DAU |
| | Tamanho do segmento |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dashboard de visão geral" }

### Dashboard de receitas {#revenue-dashboard}

| Numeradores | Denominadores |
| --- | --- |
| Compras (todas) | DAU |
| Compras selecionadas (como um cartão-presente ou ID de produto) | MAU |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dashboard de receitas" }

### Dashboard de eventos personalizados {#custom-event-dashboard}

| Numeradores | Denominadores |
| --- | --- |
| Contagem de eventos personalizados | MAU |
|  | DAU |
|  | Tamanho do segmento (somente segmentos que tenham o [rastreamento de análise de dados]({{site.baseurl}}/viewing_and_understanding_segment_data) ativado podem ser usados) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dashboard de eventos personalizados" }