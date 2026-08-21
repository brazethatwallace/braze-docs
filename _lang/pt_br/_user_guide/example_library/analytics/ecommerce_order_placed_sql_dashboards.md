---
nav_title: Dashboards SQL de pedidos realizados
article_title: Relatório sobre eventos eCommerce Order Placed no Dashboard Builder
page_order: 1
page_type: reference
description: "Use SQL do Query Builder em eventos ecommerce.order_placed para criar blocos de receita e pedidos no Dashboard Builder para relatórios de eCommerce."
tool: Reports
---

# Relatório sobre eventos eCommerce Order Placed no Dashboard Builder {#report-on-ecommerce-order-placed-events-in-dashboard-builder}

> Crie gráficos personalizados de receita e pedidos a partir de eventos recomendados `ecommerce.order_placed` salvando consultas de SQL no Query Builder e visualizando os resultados no Dashboard Builder.

## Sobre este exemplo {#about-this-example}

Flash e Thread, uma marca fictícia de varejo de roupas, registra pedidos com [eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events). A equipe de marketing quer receita diária, valor médio do pedido (AOV) e volume de pedidos em um único dashboard — não apenas a visualização pré-construída de atribuição de último ponto de contato.

Esse padrão usa o Query Builder para consultar `ecommerce.order_placed` nas tabelas de eventos compartilhadas do Snowflake e, em seguida, adiciona a consulta salva como um bloco de **Custom Queries** no Dashboard Builder. Você pode repetir o fluxo de trabalho para métricas adicionais (compradores novos versus recorrentes, categorias de produtos ou receita por segmento).

Use isso quando os dashboards de eCommerce integrados não cobrirem sua combinação de métricas. Para receita atribuída por último ponto de contato, consulte o dashboard [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution).

## Considerações {#considerations}

- **Implementação do evento:** `ecommerce.order_placed` deve estar implementado e enviando `total_value` (e dados de produto quando necessário) antes que as consultas retornem dados. Se você usa o [conector Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), os eventos recomendados podem já estar disponíveis.
- **Acesso ao Query Builder:** Você precisa da [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "View PII" para usar o Query Builder.
- **Retenção de dados:** O Query Builder retorna dados dos últimos 60 dias por padrão. Com o [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake), você pode consultar até dois anos de dados retidos. Consulte [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder).
- **Timeouts:** Consultas que levam mais de seis minutos expiram. Reduza o intervalo de datas, filtre por `TIME` ou diminua o tamanho do público se um relatório falhar. As tabelas de eventos são clusterizadas em `TIME`; prefira filtrar pelo momento em que o evento ocorreu.
- **Campo de receita:** As consultas de exemplo somam `total_value` das `properties` do evento. A receita padronizada de eCommerce da Braze nos relatórios de produto geralmente é derivada do `price` e `quantity` de cada produto. Alinhe `total_value` com seus itens de linha de produto ou ajuste o SQL para corresponder ao seu esquema.
- **Rótulos de coluna:** Coloque os nomes de exibição das colunas entre aspas duplas (por exemplo, `"Date"`, `"Total Revenue"`) para que o Dashboard Builder mostre cabeçalhos de eixo e tabela legíveis.
- **Testes:** O SQL neste artigo é fornecido como exemplo. Valide as consultas no seu espaço de trabalho antes de compartilhar dashboards amplamente.

## Configuração {#setup}

### Etapa 1: Criar uma consulta SQL para receita diária {#step-1-create-a-sql-query-for-daily-revenue}

1. Acesse **Analytics** > **Query Builder**.
2. Selecione **Create SQL Query** e depois **SQL Editor**.
3. Nomeie a consulta (por exemplo, `Flash Thread — daily eCommerce revenue`).
4. Cole e adapte a seguinte consulta para receita total por dia nos últimos 60 dias:

{% raw %}
```sql
SELECT
  DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS "Date",
  SUM(PARSE_JSON(PROPERTIES):total_value::NUMBER(18, 2)) AS "Total Revenue"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE NAME = 'ecommerce.order_placed'
  AND TO_TIMESTAMP_NTZ(TIME) >= DATEADD(day, -60, CURRENT_TIMESTAMP())
  AND TO_TIMESTAMP_NTZ(TIME) <= CURRENT_TIMESTAMP()
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

{:start="5"}
5. Selecione **Run Query** e depois selecione **Save**.

Para detalhes sobre a configuração do Query Builder, consulte [Executando relatórios no Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder#running-reports-in-the-query-builder).

### Etapa 2: Adicionar a consulta a um bloco do Dashboard Builder {#step-2-add-the-query-to-a-dashboard-builder-tile}

1. Acesse **Analytics** > **Dashboard Builder**.
2. Selecione **Create Dashboard** (ou abra um dashboard existente).
3. Para a fonte de dados, selecione **Custom Queries**.
4. Selecione **+ Add Tile** e escolha a consulta que você salvou na Etapa 1.
5. Selecione o ícone de lápis para editar o bloco:
   - Defina o tipo de gráfico como **Line graph**.
   - Defina o **X-axis** como `Date`.
   - Defina o **Y-axis** como `Total Revenue`.
6. Redimensione o bloco conforme necessário e selecione **Save**.
7. Selecione **View Dashboard** > **Run Dashboard**.

A geração do dashboard pode levar alguns minutos. Consulte [Criando um dashboard personalizado]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#creating-a-custom-dashboard).

### Etapa 3: Adicionar métricas adicionais de _Order Placed_ (opcional) {#step-3-add-additional-_order-placed_-metrics-optional}

Crie consultas salvas separadas e adicione cada uma como seu próprio bloco (até 10 blocos por dashboard).

#### Valor médio do pedido e contagem de pedidos por dia {#average-order-value-and-order-count-per-day}

{% raw %}
```sql
SELECT
  DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS "Date",
  AVG(PARSE_JSON(PROPERTIES):total_value::NUMBER(18, 2)) AS "Average Order Value",
  COUNT(*) AS "No. of Orders"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE NAME = 'ecommerce.order_placed'
  AND TO_TIMESTAMP_NTZ(TIME) >= DATEADD(day, -60, CURRENT_TIMESTAMP())
  AND TO_TIMESTAMP_NTZ(TIME) <= CURRENT_TIMESTAMP()
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

Use um gráfico de linha ou barras com `Date` no eixo X e ambas as métricas no eixo Y (desmarque as colunas que você não deseja exibir).

#### Compradores novos versus recorrentes por dia {#new-versus-returning-purchasers-per-day}

Esse padrão compara o primeiro dia de `ecommerce.order_placed` de cada usuário com os dias de compra posteriores. Ele é mais preciso quando a janela do Query Builder cobre todo o período do relatório (por exemplo, a janela padrão de 60 dias).

{% raw %}
```sql
WITH order_days AS (
  SELECT DISTINCT
    USER_ID,
    DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS purchase_day
  FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
  WHERE NAME = 'ecommerce.order_placed'
),
first_purchase AS (
  SELECT
    USER_ID,
    MIN(purchase_day) AS first_day
  FROM order_days
  GROUP BY USER_ID
),
per_day_purchasers AS (
  SELECT DISTINCT
    USER_ID,
    purchase_day
  FROM order_days
)
SELECT
  p.purchase_day AS "Date",
  COUNT(DISTINCT CASE
    WHEN f.first_day = p.purchase_day THEN p.USER_ID
  END) AS "New Purchasers",
  COUNT(DISTINCT CASE
    WHEN f.first_day < p.purchase_day THEN p.USER_ID
  END) AS "Returning Purchasers"
FROM per_day_purchasers AS p
INNER JOIN first_purchase AS f
  ON p.USER_ID = f.USER_ID
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

#### Categoria de produto a partir dos itens de linha do pedido {#product-category-from-order-line-items}

Expanda o array `products` e filtre pelo campo de categoria. Substitua `metadata.category` se você usar uma chave de metadados de produto diferente.

{% raw %}
```sql
SELECT
  f.value:metadata:category::STRING AS "Product Category",
  COUNT(*) AS "Line Items"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED,
  LATERAL FLATTEN(INPUT => PARSE_JSON(PROPERTIES):products) f
WHERE NAME = 'ecommerce.order_placed'
  AND f.value:metadata:category::STRING IS NOT NULL
  AND TRIM(f.value:metadata:category::STRING) != ''
  AND LOWER(TRIM(f.value:metadata:category::STRING)) != 'undefined'
GROUP BY 1
ORDER BY 2 DESC;
```
{% endraw %}

#### Compras e receita por segmento (análise de segmento) {#purchases-and-revenue-by-segment-segment-analytics}

Isso requer [rastreamento de análise de segmento]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) nos segmentos sobre os quais você está gerando relatórios. Use [variáveis SQL]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables) para seletores de data.

{% raw %}
```sql
WITH event_conversions AS (
  SELECT
    user_id,
    time,
    TRY_CAST(GET_PATH(PARSE_JSON(PROPERTIES), 'total_value')::string AS FLOAT) AS price,
    id AS purchase_event_id,
    f.value::string AS user_segment_membership_id
  FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED,
    LATERAL FLATTEN(input => user_segment_membership_ids) AS f
  WHERE NAME = 'ecommerce.order_placed'
    AND time > {{start_date.${Start Date}}}
    AND time < {{end_date.${End Date}}}
)
SELECT
  user_segment_membership_id AS "Segment Analytics Id",
  COUNT(DISTINCT purchase_event_id) AS "Total Purchases",
  ROUND(SUM(price), 2) AS "Total Revenue"
FROM event_conversions
GROUP BY 1
ORDER BY 3 DESC;
```
{% endraw %}

### Outros relatórios de eCommerce integrados {#other-built-in-ecommerce-reporting}

| Relatório | Quando usar |
| --- | --- |
| [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution) | Receita atribuída por último ponto de contato por Campaign ou Canvas |
| [Relatório de eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) | Volume e frequência de eventos recomendados |
| Conversões de Campaign ou Canvas | `ecommerce.order_placed` é o evento de conversão primária |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Outros relatórios de eCommerce integrados" }

## Artigos relacionados {#related-articles}

- [Eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)
- [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder)
- [Variáveis SQL no Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables)
- [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder)
- [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution)
- [Referência de tabelas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_BEHAVIORS_CUSTOMEVENT_SHARED)
- [Rastreamento de análise de segmento]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)