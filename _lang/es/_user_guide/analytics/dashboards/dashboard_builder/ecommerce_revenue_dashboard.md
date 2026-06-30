---
nav_title: Dashboard de ingresos de comercio electrónico
article_title: Dashboard de ingresos de comercio electrónico
alias: "/ecommerce_revenue_dashboard/"
page_order: 1
description: "Este artículo ofrece un resumen del dashboard de ingresos de comercio electrónico con atribución de último toque."
---

# Dashboard de ingresos de comercio electrónico {#ecommerce-revenue-dashboard}

> El dashboard **eCommerce Revenue - Last Touch Attribution** realiza un seguimiento de los ingresos atribuidos por último toque para Campaigns y Canvas mediante [eventos recomendados de comercio electrónico]({{site.baseurl}}/ecommerce_events). Usa este dashboard para entender qué mensajes generan ingresos y para monitorear el rendimiento general de comercio electrónico a lo largo del tiempo.

{% alert note %}
Si estás usando el nuevo [conector de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores?tab=shopify%20connector), los eventos recomendados de comercio electrónico estarán disponibles automáticamente a través de la integración. De lo contrario, estos eventos deben implementarse antes de que los datos aparezcan en este dashboard.
{% endalert %}

Para ver tu dashboard de ingresos de comercio electrónico, ve a **Analytics** > **Generador de dashboards** y selecciona **eCommerce Revenue - Last Touch Attribution**. Este dashboard informa sobre los ingresos atribuidos a la última campaña o Canvas con la que un usuario interactuó antes de realizar un pedido, dentro de la ventana de conversión seleccionada.

![Dashboard eCommerce Revenue - Last Touch Attribution que muestra estadísticas de ingresos de comercio electrónico, pedidos diarios realizados e ingresos diarios promedio de comercio electrónico, y un gráfico de ingresos de comercio electrónico a lo largo del tiempo.]({% image_buster /assets/img/ecommerce/ecommerce_revenue_dashboard.png %})

## Métricas disponibles {#available-metrics}

| Métrica | Definición |
| --- | --- |
| Ingresos de comercio electrónico | Ingresos totales atribuidos por último toque según el rango de fechas y la ventana de conversión seleccionados. |
| Pedidos diarios realizados | El número promedio de pedidos distintos realizados por día. |
| Ingresos diarios promedio de comercio electrónico | Ingresos promedio atribuidos por día para el período de tiempo seleccionado. |
| Ingresos de comercio electrónico a lo largo del tiempo | Una serie temporal de ingresos atribuidos en el rango de fechas seleccionado. |
| Ingresos de comercio electrónico por Campaign | Ingresos atribuidos desglosados por Campaign. |
| Ingresos de comercio electrónico por Canvas | Ingresos atribuidos desglosados por Canvas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas disponibles" }

![Gráficos de ingresos de comercio electrónico por Campaign e ingresos de comercio electrónico por Canvas.]({% image_buster /assets/img/ecommerce/ecommerce_revenue_charts.png %})

## Modelo de atribución {#attribution-model}

El dashboard **eCommerce Revenue - Last Touch Attribution** utiliza la atribución de último toque. Esto significa que los ingresos se atribuyen a la Campaign o Canvas de Braze más reciente con la que un usuario interactuó antes de realizar un pedido.

Las siguientes interacciones con mensajes califican como eventos de toque para la atribución:

- Clic en correo electrónico
- Apertura de push
- Clic en tarjeta de contenido
- Clic en mensaje dentro de la aplicación
- Clic en enlace corto de SMS
- Clic en enlace corto de WhatsApp

{% alert important %}
Las interacciones con mensajes deben haber ocurrido dentro de la ventana de conversión seleccionada. Los pedidos sin una interacción elegible con un mensaje dentro de la ventana de conversión no se atribuyen.
{% endalert %}

## Datos incluidos {#included-data}

El dashboard **eCommerce Revenue - Last Touch Attribution** obtiene datos de los eventos recomendados de comercio electrónico:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

{% alert note %}
Para que los datos se muestren en el dashboard **eCommerce Revenue - Last Touch Attribution**, los valores de `total_value`, `product.price` y `product.quantity` del evento `ecommerce.order_placed` deben ser `0` o superiores.
{% endalert %}

Los ingresos y los recuentos de pedidos utilizan los cálculos estandarizados de Braze.

| Métrica | Cálculo |
| --- | --- |
| Ingresos totales | Suma de valores de pedidos realizados − Suma de valores reembolsados |
| Pedidos totales | Pedidos distintos realizados − Pedidos distintos cancelados |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Datos incluidos" }

### Datos excluidos {#excluded-data}

Las compras registradas mediante el evento de compra heredado no se incluyen. El dashboard **eCommerce Revenue - Last Touch Attribution** actualmente no es compatible con características vinculadas a eventos de compra heredados, como LTV o informes de ingresos dentro de Campaigns o Canvas.

## Manejo de divisas {#currency-handling}

Todos los ingresos se muestran en USD. Las divisas que no sean USD se convierten a USD utilizando el tipo de cambio de la fecha en que se reportó el evento. Para evitar la conversión, establece la divisa como `USD` de forma fija al enviar eventos.