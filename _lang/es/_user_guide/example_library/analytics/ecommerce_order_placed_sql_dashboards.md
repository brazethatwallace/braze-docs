---
nav_title: Paneles SQL de Order Placed
article_title: Informes sobre eventos eCommerce Order Placed en el generador de paneles
page_order: 1
page_type: reference
description: "Usa SQL del generador de consultas sobre eventos ecommerce.order_placed para crear mosaicos de ingresos y pedidos en el generador de paneles para informes de eCommerce."
tool: Reports
---

# Informes sobre eventos eCommerce Order Placed en el generador de paneles {#report-on-ecommerce-order-placed-events-in-dashboard-builder}

> Crea gráficos personalizados de ingresos y pedidos a partir de eventos recomendados `ecommerce.order_placed` guardando consultas SQL en el generador de consultas y visualizando los resultados en el generador de paneles.

## Acerca de este ejemplo {#about-this-example}

Flash y Thread, una marca ficticia de comercio minorista de ropa, registra pedidos con [eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events). Su equipo de marketing quiere ingresos diarios, valor promedio de pedido (AOV) y volumen de pedidos en un solo panel, no solo la vista preconstruida de atribución de último toque.

Este patrón usa el generador de consultas para consultar `ecommerce.order_placed` desde las tablas de eventos compartidas de Snowflake, y luego agrega la consulta guardada como un mosaico de **Custom Queries** en el generador de paneles. Puedes repetir el flujo de trabajo para métricas adicionales (compradores nuevos frente a recurrentes, categorías de productos o ingresos a nivel de segmento).

Usa esto cuando los paneles de eCommerce integrados no cubran tu combinación de métricas. Para ingresos atribuidos por último toque, consulta el panel [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution).

## Consideraciones {#considerations}

- **Implementación de eventos:** `ecommerce.order_placed` debe estar implementado y enviando `total_value` (y datos de producto cuando sea necesario) antes de que las consultas devuelvan datos. Si usas el [conector de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), los eventos recomendados pueden estar ya disponibles.
- **Acceso al generador de consultas:** Necesitas el [permiso de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "View PII" para usar el generador de consultas.
- **Retención de datos:** El generador de consultas devuelve datos de los últimos 60 días de forma predeterminada. Con [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake), puedes consultar hasta dos años de datos retenidos. Consulta [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder).
- **Tiempos de espera:** Las consultas que se ejecutan durante más de seis minutos agotan el tiempo de espera. Reduce el rango de fechas, filtra por `TIME` o reduce el tamaño de la audiencia si un informe falla. Las tablas de eventos están agrupadas por `TIME`; es preferible filtrar por el momento en que ocurrió el evento.
- **Campo de ingresos:** Las consultas de ejemplo suman `total_value` de las `properties` del evento. Los ingresos estandarizados de eCommerce de Braze en los informes de producto a menudo se derivan del `price` y `quantity` de cada producto. Alinea `total_value` con tus líneas de producto, o ajusta el SQL para que coincida con tu esquema.
- **Etiquetas de columna:** Envuelve los nombres de columna de visualización entre comillas dobles (por ejemplo, `"Date"`, `"Total Revenue"`) para que el generador de paneles muestre encabezados de ejes y tablas legibles.
- **Pruebas:** El SQL de este artículo se proporciona como ejemplo. Valida las consultas en tu espacio de trabajo antes de compartir paneles ampliamente.

## Configuración {#setup}

### Paso 1: Crear una consulta SQL para ingresos diarios {#step-1-create-a-sql-query-for-daily-revenue}

1. Ve a **Analytics** > **Query Builder**.
2. Selecciona **Create SQL Query** y luego **SQL Editor**.
3. Asigna un nombre a la consulta (por ejemplo, `Flash Thread — daily eCommerce revenue`).
4. Pega y adapta la siguiente consulta para ingresos totales por día del calendario en los últimos 60 días:

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
5. Selecciona **Run Query** y luego selecciona **Save**.

Para más detalles sobre la configuración del generador de consultas, consulta [Ejecución de informes en el generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder#running-reports-in-the-query-builder).

### Paso 2: Agregar la consulta a un mosaico del generador de paneles {#step-2-add-the-query-to-a-dashboard-builder-tile}

1. Ve a **Analytics** > **Dashboard Builder**.
2. Selecciona **Create Dashboard** (o abre un panel existente).
3. Para el origen de datos, selecciona **Custom Queries**.
4. Selecciona **+ Add Tile** y luego elige la consulta que guardaste en el paso 1.
5. Selecciona el icono de lápiz para editar el mosaico:
   - Establece el tipo de gráfico en **Line graph**.
   - Establece el **eje X** en `Date`.
   - Establece el **eje Y** en `Total Revenue`.
6. Redimensiona el mosaico según sea necesario y luego selecciona **Save**.
7. Selecciona **View Dashboard** > **Run Dashboard**.

La generación del panel puede tardar unos minutos. Consulta [Creación de un panel personalizado]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#creating-a-custom-dashboard).

### Paso 3: Agregar métricas adicionales de _Order Placed_ (opcional) {#step-3-add-additional-_order-placed_-metrics-optional}

Crea consultas guardadas por separado y luego agrega cada una como su propio mosaico (hasta 10 mosaicos por panel).

#### Valor promedio de pedido y cantidad de pedidos por día {#average-order-value-and-order-count-per-day}

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

Usa un gráfico de líneas o barras con `Date` en el eje X y ambas métricas en el eje Y (deselecciona las columnas que no quieras mostrar).

#### Compradores nuevos frente a recurrentes por día {#new-versus-returning-purchasers-per-day}

Este patrón compara el primer día de `ecommerce.order_placed` de cada usuario con los días de compra posteriores. Es más preciso cuando la ventana del generador de consultas cubre el período de informe completo (por ejemplo, la ventana predeterminada de 60 días).

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

#### Categoría de producto a partir de líneas de pedido {#product-category-from-order-line-items}

Aplana el arreglo `products` y filtra por tu campo de categoría. Reemplaza `metadata.category` si usas una clave de metadatos de producto diferente.

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

#### Compras e ingresos por segmento (análisis de segmento) {#purchases-and-revenue-by-segment-segment-analytics}

Esto requiere [seguimiento de análisis de segmento]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) en los segmentos sobre los que informas. Usa [variables SQL]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables) para selectores de fecha.

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

### Otros informes de eCommerce integrados {#other-built-in-ecommerce-reporting}

| Informe | Cuándo usarlo |
| --- | --- |
| [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution) | Ingresos atribuidos por último toque por Campaign o Canvas |
| [Informe de eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) | Volumen y frecuencia de eventos para eventos recomendados |
| Conversiones de Campaign o Canvas | `ecommerce.order_placed` es el evento de conversión primaria |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Otros informes de eCommerce integrados" }

## Artículos relacionados {#related-articles}

- [Eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)
- [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder)
- [Variables SQL en el generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables)
- [Generador de paneles]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder)
- [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution)
- [Referencia de tablas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_BEHAVIORS_CUSTOMEVENT_SHARED)
- [Seguimiento de análisis de segmento]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)