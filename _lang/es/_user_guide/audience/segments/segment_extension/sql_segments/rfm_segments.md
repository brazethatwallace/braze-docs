---
nav_title: "Segmentos RFM"
article_title: Extensiones de segmento SQL RFM
page_order: 1
page_type: reference
alias: "/rfm_segments/"
description: "Este artículo describe cómo crear extensiones de segmento RFM, que identifican a tus mejores usuarios midiendo sus hábitos de compra."
tool: Segments
---

# Segmentos RFM SQL {#rfm-sql-segments}

> Puedes crear una extensión de segmento RFM (recencia, frecuencia, valor monetario) para dirigirte a tus mejores usuarios midiendo sus hábitos de compra.

El análisis RFM es una técnica de marketing que identifica a tus mejores usuarios puntuándolos en una escala de 0 a 3 para cada categoría (recencia, frecuencia, valor monetario), donde 3 es la mejor puntuación y 0 es la peor. Los valores de recencia, frecuencia y valor monetario se basan en datos de un rango de tiempo específico que tú elijas.

## Categorías RFM {#rfm-categories}

| Categoría | Definición |
| --- | --- |
| Recencia | Qué tan recientemente un cliente realizó una compra. Una puntuación más alta significa compras más recientes. |
| Frecuencia | Con qué frecuencia un cliente realizó una compra. Una puntuación más alta significa mayor frecuencia. |
| Valor monetario | Cantidad total de dinero que un cliente gastó. Una puntuación más alta significa mayor gasto. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="RFM categories" }

{% alert note %}
Los eventos de compra deben estar habilitados para usar segmentos RFM SQL, ya que el valor monetario de tus usuarios se determina por los ingresos que han generado a través de los eventos de compra de Braze.
{% endalert %}

## Crear un segmento RFM {#creating-an-rfm-segment}

1. Ve a **Audience** > **Segment Extensions**.
2. Selecciona **New Extension** y luego selecciona **Recency, frequency, and monetary value (RFM) segment**.

![Modal con la opción de crear un segmento de catálogo para eventos, compras o segmentos RFM.]({% image_buster /assets/img/segment/select_rfm_segment.png %}){: style="max-width:80%" }

{: start="3"}
3. En el panel **Variables**, selecciona tu **Time Range** para especificar el período de datos de compra a analizar. Puedes especificar hasta los últimos 60 días. El rango de tiempo que selecciones es el rango del que se extraen los datos de comportamiento del usuario y depende de los objetivos de tu campaña.

| Campo de rango de tiempo | Descripción | Caso de uso |
| --- | --- | --- |
| Relativo | Especifica la actividad dentro de los últimos X días | Analizar el comportamiento más reciente del usuario con una ventana móvil. |
| Fecha de inicio | Especifica un punto de inicio fijo para tu análisis | Analizar la actividad del usuario a partir de una fecha específica, como después del lanzamiento de una campaña. |
| Fecha de fin | Especifica un punto de fin fijo para tu análisis | Analizar la actividad del usuario hasta una fecha específica, como antes de una actualización de producto. |
| Rango de fechas | Especifica tanto una fecha de inicio como de fin para un período personalizado | Analizar el comportamiento del usuario durante un período definido, como un evento promocional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Creating an RFM segment" }

{: start="4"}
4. Selecciona los [grupos RFM](#rfm-groups) generados para incluir en tu segmento. Si seleccionas múltiples grupos, tu segmento incluye a los usuarios que forman parte de cualquiera de los grupos seleccionados.

![Panel de variables con los grupos RFM "Champions" y "Loyal Users" seleccionados.]({% image_buster /assets/img/segment/rfm_groups.png %})

{: start="5"}
5. Ejecuta una vista previa y luego guarda tu segmento.

{% alert note %}
No necesitas editar el código SQL en la plantilla para crear un segmento RFM. Puedes usar exclusivamente el panel **Variables** para personalizar tu segmento.
{% endalert %}

### Grupos RFM {#rfm-groups}

Los segmentos RFM se evalúan en un orden específico. Los usuarios se asignan al primer segmento cuyos criterios cumplan, desde la parte superior de la lista de priorización hacia abajo. Por ejemplo, un usuario que califica tanto para "Champions" como para "Loyal Users" se asigna al segmento "Champions" porque tiene una prioridad más alta.

| Grupo RFM          | Descripción del segmento                                                                 | Rango de recencia (R) | Rango de frecuencia (F) | Rango monetario (M) |
|--------------------|-------------------------------------------------------------------------------------|------------------|--------------------|-------------------|
| Champions          | El segmento de usuarios más valioso con las puntuaciones más altas en todas las categorías.                   | 3                | 2-3                | 2-3               |
| Loyal Users        | Usuarios con alta recencia y alta frecuencia. Pueden tener un valor monetario menor que los Champions. | 2-3              | 2-3                | 1-3               |
| Potential Loyalists| Usuarios que compraron recientemente con frecuencia moderada y valor monetario moderado.   | 3                | 1-3                | 1-3               |
| Promising          | Usuarios que realizaron una compra inicial reciente de alto valor pero aún no han establecido una alta frecuencia de compra. | 3                | 0-3                | 1-3               |
| New Customer       | Usuarios que realizaron su primera compra muy recientemente.                             | 3                | 0-3                | 0-3               |
| Needing Attention  | Usuarios con recencia por encima del promedio, pero cuya frecuencia de compra o valor monetario están por debajo del promedio. | 2-3              | 0-3                | 0-3               |
| Cannot lose them   | Usuarios que anteriormente eran de alto valor con buenas puntuaciones de frecuencia y valor monetario, pero que no han comprado en mucho tiempo. | 0-1              | 2-3                | 2-3               |
| At Risk            | Usuarios que históricamente han tenido puntuaciones moderadas de frecuencia y valor monetario, pero que no han comprado en mucho tiempo. | 0-1              | 1-3                | 1-3               |
| About to Sleep     | Usuarios que tienen puntuaciones bajas en todas las métricas.                                       | 1                | 0-3                | 0-3               |
| Hibernating        | Usuarios con frecuencia moderada pero que han estado inactivos durante un período prolongado.    | 0                | 0-2                | 0-3               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="RFM groups" }