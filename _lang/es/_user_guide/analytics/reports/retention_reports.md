---
nav_title: Informes de retención
article_title: Informes de retención para Campaigns y Canvas
page_order: 9
tool: Reports
page_type: reference
description: "Esta página explica cómo medir la retención de usuarios que realizaron un evento de retención seleccionado en una Campaign o Canvas específico."
---

# Informes de retención {#retention-reports}

> La retención de usuarios es una de las métricas más importantes para cualquier especialista en marketing. Mantener a los usuarios comprometidos regresando por más indica que el negocio está saludable. Braze te permite medir la retención de usuarios directamente en la página de **Analytics** de tu Campaign o Canvas.

{% alert important %}
Los informes de retención no están disponibles para Campaigns activadas por API.
{% endalert %}

## Ejecutar un informe de retención {#running-a-retention-report}

### Paso 1: Seleccionar un rango de fechas {#step-1-select-a-date-range}

![Fecha del informe]({% image_buster /assets/img/date_select_retention.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para empezar, visita cualquier Campaign o Canvas en tu panel de Braze y selecciona un rango de fechas para tu informe. Seleccionar un rango de fechas adecuado es crucial debido a la forma en que afecta a los informes de retención.

Este informe incluirá a todos los usuarios que entraron inicialmente en la Campaign o Canvas durante esta ventana, y de esos usuarios, los datos de aquellos que realizaron su evento de retención durante el rango de fechas aparecerán en el informe.

Para seleccionar un rango de fechas, navega a la página de **Analytics** de la Campaign o Canvas y selecciona varios rangos o establece un rango personalizado para tu informe.

### Paso 2: Seleccionar un evento de retención {#step-2-select-a-retention-event}

{% tabs %}
{% tab Campaign %}

A continuación, ve a la sección **Campaign Retention**. La retención de Campaign te muestra la tasa a la que cualquier usuario que haya recibido esta Campaign específica ha realizado un evento de retención (especificado por ti en el informe de retención) durante los 30 días desde el momento en que recibió la Campaign.

{% endtab %}
{% tab Canvas %}

A continuación, selecciona **Analyze Variants**. Desde aquí, puedes analizar tus variantes, consultar tu informe de embudo y ver tu informe de retención. La retención de Canvas te muestra la tasa a la que cualquier usuario que haya recibido este Canvas específico ha realizado un evento de retención (especificado por ti en el informe de retención) durante los 30 días desde el momento en que recibió el Canvas.

{% endtab %}
{% endtabs %}

![Seleccionar un evento de retención]({% image_buster /assets/img/retention_1.png %}){: style="max-width:80%"}

### Paso 3: Generar el informe {#step-3-generate-the-report}

Después de haber seleccionado un evento de retención, selecciona **Run Report** para iniciar la consulta.

![Ejecutar informe]({% image_buster /assets/img/retention_2.png %}){: style="max-width:80%"}

Esta consulta puede tardar unos minutos en ejecutarse, dependiendo de la cantidad de datos que necesiten recuperarse para generar los resultados. Si tarda demasiado, verás una notificación pidiéndote que intentes cargar el informe de nuevo. Es posible que debas esperar hasta cinco minutos antes de que el informe se cargue.

Una vez generado el informe, no se puede volver a ejecutar con el mismo evento de retención durante 24 horas. Siempre verás una marca de tiempo de cuándo se generó el informe por última vez y una opción para regenerarlo si ha pasado más de un día. Sin embargo, puedes cambiar el evento de retención y volver a ejecutar el informe para analizar el impacto de la Campaign en diferentes KPI.

El informe solo mostrará los días en los que la Campaign o Canvas estuvo enviando mensajes. Para algunas Campaigns y Canvas, eso puede significar que el informe solo muestre un día si solo se envió una vez. Si es recurrente o se desencadena automáticamente, es posible que veas múltiples días en la tabla.

{% tabs %}
{% tab Campaign %}

![Informe completo]({% image_buster /assets/img/campaign_retention3.png %})

{% endtab %}
{% tab Canvas %}

![Informe completo]({% image_buster /assets/img/canvas_retention_report.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

## Explicación del informe {#report-explanation}

El informe de retención ofrece tanto una fórmula de retención progresiva como una de retención por rango. Para ver tu informe de Campaign o Canvas con uno de estos tipos de retención, selecciona **Rolling Retention** o **Range Retention** en **Type of Retention**.

### Retención progresiva {#rolling-retention}

La retención progresiva mide cuántos usuarios regresan y realizan el evento de retención en o después de cualquiera de los días listados en la parte superior del informe. Así, si un usuario inició una sesión entre el día tres y el siete, el usuario se contará como retenido en las columnas "3 días", "1 día" y "0 días". Cualquier usuario que se cuente como retenido después de la marca de 30 días desde que se envió la Campaign o Canvas se contará en la columna "30 días" de esa fila.

Un usuario que completa el evento múltiples veces durante una ventana de más de 30 días se contará como parte de múltiples marcos temporales. Por ejemplo, un usuario que completa una sesión después de un día se incrementará en las columnas para >0 y >1. Si luego completa el evento después de tres días, se incrementará nuevamente en las columnas anteriores (>0 y >1), lo que podría resultar en que la tasa de retención supere el 100%.

#### Cómo leer los informes de retención progresiva {#how-to-read-rolling-retention-reports}

La forma de leer el gráfico del informe de retención para una columna de día tres sería: Y% o Y número de usuarios (según las unidades elegidas) realizaron el evento tres o más días después de recibir la Campaign en el día Z.

![Informe progresivo]({% image_buster /assets/img/campaign_retention3.png %})

Como otro ejemplo, haciendo referencia a la tabla en la imagen anterior, el 25 de marzo, un total de 38 usuarios realizaron el evento de retención. La retención del día cero fue del 68,42%, lo que significa que el 68,42% de los usuarios realizaron el evento de retención cero o más días (en el día cero o después) después de recibir la Campaign. La retención del día siete fue del 57,89%, lo que significa que el 57,89% de los usuarios realizaron el evento siete o más días (en el día siete o después) después de recibir la Campaign.

Esta información puede ser útil si quieres conocer el porcentaje de usuarios que han utilizado y no han utilizado tu producto más de 30 días después del primer uso. Un valor de porcentaje o número en la columna del día 30 te indica el porcentaje de usuarios que regresaron en el día 30 o después.

### Retención por rango {#range-retention}

La retención por rango mide cuántos usuarios regresan en el rango de días listado en la parte superior del informe. Así, si un usuario inició una sesión entre los días tres y siete y luego nuevamente en el día 13, se contaría como retenido tanto en el rango "Día 3-7" como en el rango "Día 7-14".

#### Cómo leer los informes de retención por rango {#how-to-read-range-retention-reports}

Los informes de rango son algunos de los informes más intuitivos de leer. Indican claramente, de todos los usuarios en una cohorte, qué porcentaje de esos usuarios realizó el evento de retención dentro de un rango de fechas determinado. Por ejemplo, en la siguiente imagen, haciendo referencia a la cohorte de todos los usuarios, en el rango de fechas "Día 0 (0-24hrs)", el 35,71% de la cohorte realizó el evento de retención. Si un usuario realiza múltiples eventos de retención dentro de múltiples rangos de fechas, se contará como retenido para cada rango.

![Informe de retención]({% image_buster /assets/img/range_retention.png %})

### Componentes del informe de retención {#retention-report-components}

- **Columna de usuarios**: El valor mostrado es el número de usuarios únicos que realizaron la acción de inicio dentro del marco temporal seleccionado; el recuento de usuarios del día actual se excluirá ya que se está calculando.
- **Filas de cohorte Z**: Muestran los días en los que la Campaign o Canvas estuvo enviando mensajes.
- **Columnas de día X**: Días que abarcan entre 0 y 30 días en varios incrementos.
- **Fila de todos los usuarios**: También conocida como la fila de resumen del informe, resume los datos de retención para todo el período de tiempo. Ten en cuenta que si un usuario ha recibido la Campaign o Canvas en múltiples cohortes, sus resultados se contarán dos veces aquí.
- **Porcentajes/Números**: Muestra el porcentaje o número de usuarios que realizaron el evento X o más días después de recibir la Campaign o Canvas en el día Z. Estos porcentajes son los promedios ponderados. Los valores incompletos se indicarán con un asterisco.
- **Rango de fechas**: Establecido en la página de **Details** de la Campaign o Canvas, el rango de fechas incluye a todos los usuarios que recibieron la Campaign o Canvas durante esta ventana, y de esos usuarios, los datos de aquellos que realizaron su evento de retención durante el rango de fechas aparecerán en el informe.
- **Unidades**: Puedes ajustar las unidades entre el porcentaje de usuarios y el número de usuarios desde los controles del gráfico; unidades específicas pueden resultar más significativas al evaluar el impacto de una Campaign o Canvas.
- **Mapa de colores**: En tu informe de retención, los porcentajes o números de usuarios más altos se asignan a tonos más oscuros de azul. Los porcentajes o números de usuarios más bajos se asignan a tonos más claros de azul. Esto se hace para ayudar a los usuarios a visualizar estos datos.
- **Gráfico del informe de retención**: Este gráfico resume los resultados de todas las cohortes para el rango de fechas seleccionado.

### Rendimiento por variante {#performance-by-variant}

Ver tu informe de retención por variante te permite comparar la retención progresiva para cada variante o variación de mensaje durante el período de tiempo seleccionado, así como el grupo de control. Este informe se puede ver alternando **Show Performance For** a **By Variant**.

Algunos ejemplos de uso del rendimiento por variante:

- ¿Tienes algunas variantes o experimentos en los que los resultados parecen un esfuerzo desperdiciado o no tienen significancia estadística? Echa otro vistazo y comprueba si una u otra tuvo un impacto a más largo plazo.
- Observa cómo se ve la retención si no enviaste un mensaje analizando los datos de retención del grupo de control.

{% tabs %}
{% tab Campaign %}

![Ver por variante]({% image_buster /assets/img/variant_view.png %})

{% endtab %}
{% tab Canvas %}

![Ver por variante]({% image_buster /assets/img/variant_view_canvas.png %})

{% endtab %}
{% endtabs %}

#### Componentes del informe de retención por variante {#retention-report-by-variant-components}

- **Rango de fechas**: Establecido en la página de **Details** de la Campaign o Canvas, el rango de fechas incluye a todos los usuarios que recibieron la Campaign o Canvas durante esta ventana, y de esos usuarios, los datos de aquellos que realizaron su evento de retención durante el rango de fechas aparecerán en el informe. Cada día se miden la tasa de retención, el cambio porcentual respecto al grupo de control y la confianza.
- **Tasa de retención**: Muestra la tasa de retención por variante. La tasa de retención es equivalente al número de usuarios que realizaron el evento de retención dividido por el total de usuarios que recibieron la Campaign o Canvas.
- **Cambio porcentual respecto al control**: Cuantifica el cambio porcentual por variante respecto al grupo de control.
- **Confianza**: {% multi_lang_include analytics/metrics.md metric='Confidence' %} Braze compara la tasa de conversión de cada variante con la tasa de conversión del control mediante un procedimiento estadístico llamado prueba Z para calcular un porcentaje de [confianza]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#understanding-confidence).
- **Unidades**: Puedes ajustar las unidades entre el porcentaje de usuarios y el número de usuarios desde los controles del gráfico; unidades específicas pueden resultar más significativas al evaluar el impacto de una Campaign o Canvas.
- **Gráfico de variantes**: Este gráfico resume los resultados por variante para el rango de fechas seleccionado.

## Qué buscar en tus informes de retención {#things-to-look-for-in-your-retention-reports}

Los informes de retención son sencillos de generar, pero difíciles de interpretar y de actuar en consecuencia. Los siguientes temas y preguntas pueden ayudarte a sacar más provecho de tus informes de retención.

- Considera las tendencias por día de la semana para Campaigns recurrentes (por ejemplo, ¿las cohortes del lunes tienen mejor rendimiento que las cohortes del sábado?).
- ¿Dónde empieza a disminuir el impacto? Esto podría ser una señal de que se necesita una nueva Campaign o Canvas que se dirija a los usuarios en ese momento como otro impulso a la retención.
- ¿Estás observando fatiga de mensajería?
- ¿Una optimización específica que hiciste a una Campaign o Canvas hace X días tuvo un impacto positivo?