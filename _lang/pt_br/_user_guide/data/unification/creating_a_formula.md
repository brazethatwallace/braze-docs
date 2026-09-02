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

As fórmulas ajudam você a entender as relações complexas que existem em seus dados. Por exemplo, é possível comparar quantos eventos personalizados foram concluídos por usuários ativos diários que se qualificam para um determinado Segment or segmento or segmento em comparação com a população geral (ou com outro Segment or segmento or segmento).

## Casos de uso {#use-cases}

As fórmulas, especialmente quando combinadas com eventos personalizados, podem ajudar a entender os comportamentos dos usuários dentro do seu app. As fórmulas também podem oferecer insights mais profundos sobre padrões de compra de segmentos, mesmo que sua empresa use mídia paga em conjunto com a Braze, como Google Ads ou TV.

A seguir estão alguns exemplos dos tipos de padrões de comportamento que podem ser detectados usando fórmulas:

- **Viagem por aplicativo:** Se você tem um evento personalizado para quando o usuário cancela uma corrida, é possível configurar uma função para Corridas Canceladas / usuário ativo diário para descobrir se determinados segmentos de usuários tendem a cancelar mais corridas do que outros.
- **Apps de eCommerce:** Ao configurar uma função para compras de um determinado ID de produto / MAU, você pode comparar a popularidade de um produto recentemente promovido entre segmentos, mesmo que todas as promoções não pudessem ser rastreadas usando a Braze.
- **Apps de mídia que usam anúncios:** Se a experiência dos usuários é interrompida por anúncios entre clipes de vídeo ou áudio, registrar saídas no meio do anúncio como um evento personalizado e calcular a proporção de saídas no meio do anúncio / usuário ativo diário pode ajudar a encontrar os melhores segmentos para direcionar com uma Campaign de inscrições premium sem anúncios.

## Criando fórmulas {#creating-formulas}

As fórmulas podem ser acessadas nas páginas [Início]({{site.baseurl}}/user_guide/analytics/dashboards/home), [Relatório de receita]({{site.baseurl}}/user_guide/analytics/reports/revenue_report) e [Relatório de eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) no dashboard. Em **Início** e **Relatório de receita**, abra o gráfico **Performance Over Time**, defina **Statistics For** como **KPI Formulas** e selecione pelo menos uma fórmula. Na página **Relatório de eventos personalizados**, abra **Filters**, selecione uma ou mais opções de **KPI formula** e selecione **Apply**.

![Visualizar estatísticas de fórmulas de KPI no dashboard da Braze]({% image_buster /assets/img_archive/kpi_forms.png %})

Para criar uma nova fórmula:

1. Acesse o dashboard apropriado (**Início**, **Relatório de receita** ou **Relatório de eventos personalizados**).
2. Selecione **Manage KPI Formulas**.
3. Insira um nome para sua fórmula.
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
| | Tamanho do Segment or segmento |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dashboard de visão geral" }

### Dashboard de receita {#revenue-dashboard}

| Numeradores | Denominadores |
| --- | --- |
| Compras (todas) | DAU |
| Compras selecionadas (como um cartão-presente ou ID de produto) | MAU |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dashboard de receita" }

### Dashboard de eventos personalizados {#custom-event-dashboard}

| Numeradores | Denominadores |
| --- | --- |
| Contagem de eventos personalizados | MAU |
|  | DAU |
|  | Tamanho do Segment or segmento (somente Segments que têm o [rastreamento de análise de dados]({{site.baseurl}}/viewing_and_understanding_segment_data) ativado podem ser usados) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dashboard de eventos personalizados" }