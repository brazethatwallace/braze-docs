---
nav_title: "Segmentos RFM"
article_title: Extensões de segmento SQL RFM
page_order: 1
page_type: reference
alias: "/rfm_segments/"
description: "Este artigo descreve como criar extensões de segmento RFM, que identificam seus melhores usuários medindo seus hábitos de compra."
tool: Segments
---

# Segmentos SQL RFM {#rfm-sql-segments}

> Você pode criar uma extensão de segmento RFM (recência, frequência, valor monetário) para segmentar seus melhores usuários medindo seus hábitos de compra.

A análise RFM é uma técnica de marketing que identifica seus melhores usuários pontuando-os em uma escala de 0 a 3 para cada categoria (recência, frequência, valor monetário), onde 3 é a melhor pontuação e 0 é a pior. Os valores de recência, frequência e monetário são todos baseados em dados de um intervalo de tempo específico de sua escolha.

## Categorias RFM {#rfm-categories}

| Categoria | Definição |
| --- | --- |
| Recência | Quão recentemente um cliente fez uma compra. Uma pontuação mais alta significa compras mais recentes. |
| Frequência | Com que frequência um cliente fez uma compra. Uma pontuação mais alta significa maior frequência. |
| Valor monetário | Valor total gasto por um cliente. Uma pontuação mais alta significa maior gasto. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Categorias RFM" }

{% alert note %}
Os eventos de compra devem estar ativados para usar segmentos SQL RFM, pois o valor monetário dos seus usuários é determinado pela receita gerada por meio dos eventos de compra da Braze.
{% endalert %}

## Criando um segmento RFM {#creating-an-rfm-segment}

1. Acesse **Audience** > **Segment Extensions**.
2. Selecione **New Extension** e, em seguida, selecione **Recency, frequency, and monetary value (RFM) segment**.

![Modal com a opção de criar um segmento de catálogo para eventos, compras ou segmentos RFM.]({% image_buster /assets/img/segment/select_rfm_segment.png %}){: style="max-width:80%" }

{: start="3"}
3. No painel **Variables**, selecione seu **Time Range** para especificar o período de dados de compra a ser analisado. Você pode especificar até os últimos 60 dias. O intervalo de tempo selecionado é o período do qual os dados de comportamento do usuário são extraídos e depende dos objetivos da sua campanha.

| Campo de intervalo de tempo | Descrição | Caso de uso |
| --- | --- | --- |
| Relativo | Especifica a atividade nos últimos X dias | Analisar o comportamento mais recente do usuário com uma janela móvel. |
| Data de início | Especifica um ponto de partida fixo para sua análise | Analisar a atividade do usuário a partir de uma data específica, como após o lançamento de uma campanha. |
| Data de término | Especifica um ponto final fixo para sua análise | Analisar a atividade do usuário até uma data específica, como antes de uma atualização de produto. |
| Intervalo de datas | Especifica uma data de início e término para um período personalizado | Analisar o comportamento do usuário durante um período definido, como um evento promocional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Criando um segmento RFM" }

{: start="4"}
4. Selecione os [grupos RFM](#rfm-groups) gerados para incluir no seu segmento. Se você selecionar múltiplos grupos, seu segmento incluirá usuários que fazem parte de qualquer um dos grupos selecionados.

![Painel de variáveis com os grupos RFM "Champions" e "Loyal Users" selecionados.]({% image_buster /assets/img/segment/rfm_groups.png %})

{: start="5"}
5. Execute uma prévia e salve seu segmento.

{% alert note %}
Você não precisa editar o código SQL no modelo para criar um segmento RFM. Você pode usar exclusivamente o painel **Variables** para personalizar seu segmento.
{% endalert %}

### Grupos RFM {#rfm-groups}

Os segmentos RFM são avaliados em uma ordem específica. Os usuários são atribuídos ao primeiro segmento cujos critérios eles atendem, de cima para baixo na lista de priorização. Por exemplo, um usuário que se qualifica tanto para "Champions" quanto para "Loyal Users" é atribuído ao segmento "Champions" porque ele tem uma prioridade mais alta.

| Grupo RFM          | Descrição do segmento                                                                 | Classificação de recência (R) | Classificação de frequência (F) | Classificação monetária (M) |
|--------------------|-------------------------------------------------------------------------------------|------------------|--------------------|-------------------|
| Champions          | O segmento de usuários mais valioso, com as melhores pontuações em todas as categorias.                   | 3                | 2-3                | 2-3               |
| Loyal Users        | Usuários com alta recência e alta frequência. Podem ter valor monetário menor que os Champions. | 2-3              | 2-3                | 1-3               |
| Potential Loyalists| Usuários que compraram recentemente com frequência e valor monetário moderados.   | 3                | 1-3                | 1-3               |
| Promising          | Usuários que fizeram uma compra inicial recente e de alto valor, mas ainda não estabeleceram uma alta frequência de compra. | 3                | 0-3                | 1-3               |
| New Customer       | Usuários que fizeram sua primeira compra muito recentemente.                             | 3                | 0-3                | 0-3               |
| Needing Attention  | Usuários com recência acima da média, mas cuja frequência de compra ou valor monetário estão abaixo da média. | 2-3              | 0-3                | 0-3               |
| Cannot lose them   | Usuários que anteriormente tinham alto valor com boas pontuações de frequência e monetárias, mas não compram há muito tempo. | 0-1              | 2-3                | 2-3               |
| At Risk            | Usuários que historicamente tinham pontuações moderadas de frequência e monetárias, mas não compram há muito tempo. | 0-1              | 1-3                | 1-3               |
| About to Sleep     | Usuários com pontuações baixas em todas as métricas.                                       | 1                | 0-3                | 0-3               |
| Hibernating        | Usuários com frequência moderada, mas que estão inativos há um período prolongado.    | 0                | 0-2                | 0-3               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Grupos RFM" }