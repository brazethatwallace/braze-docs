---
nav_title: Generador de informes (heredado)
article_title: Generador de informes (heredado)
alias: /report_builder_legacy/
page_order: 1
page_type: reference
description: "Esta página explica cómo ejecutar un informe con el generador de informes heredado, incluyendo la creación de informes comparativos de Campaigns y Canvas, y la creación de informes y gráficos."
tool:
  - Reports

---

# Generador de informes (heredado) {#report-builder-legacy}

> El Generador de informes te permite comparar los resultados de múltiples Campaigns o Canvas en una sola vista, para que puedas determinar fácilmente qué estrategias de interacción tuvieron mayor impacto en tus métricas clave. Tanto para Campaigns como para Canvas, puedes exportar tus datos y guardar tu informe para consultarlo en el futuro.<br><br>Para una lista descriptiva de las métricas que encontrarás en tus informes, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

![Ejemplo de comparación de Campaigns]({% image_buster /assets/img/campaign_comparison/campaign_main.png %}){: style="max-width:80%;"}

Usa este informe para responder preguntas clave sobre interacción, por ejemplo:

- ¿Cuáles fueron las Campaigns o Canvas con mejor rendimiento para una etiqueta o canal específico?
- ¿Qué variantes de Campaigns multivariantes tuvieron mayor mejora respecto al grupo de control?
- ¿Qué campaña de promoción estacional generó una mayor tasa de compra: la oferta de verano, la de otoño o la de invierno?
- ¿Qué notificaciones push dentro de este Canvas tuvieron las tasas de apertura más altas?
- ¿Qué pasos en este grupo de Canvas tuvieron más conversiones?
- ¿La versión 1 de un correo electrónico de bienvenida o la versión 2 generaron mayor interacción y conversión? ¿Funcionaron los cambios?
- ¿Cómo impactan los diferentes métodos de entrega (por ejemplo, 3 push planificados, 3 push basados en acciones y 3 push activados por API) en tus tasas de apertura, tasas de conversión o tasas de compra?
- ¿Las mejoras continuas en los mensajes para usuarios inactivos han impactado positivamente tus KPI a lo largo del tiempo?

{% alert tip %}
Intenta usar los mismos eventos de conversión para la conversión A, B, etc., en las Campaigns y Canvas que desees comparar, para que puedas alinear estas conversiones en tus informes del Generador de informes.
{% endalert %}

## Ejecutar un informe {#running-a-report}

### Paso 1: Crear un informe nuevo {#step-1-create-a-new-report}

Dentro del dashboard, navega a **Analytics** > **Report Builder**.

Selecciona **Crear informe nuevo** y elige un informe comparativo de Campaigns o un informe comparativo de Canvas.

Si eliges ejecutar un informe sobre Campaigns, puedes seleccionar entre un informe **Manual** o **Automatizado**. Los informes pueden contener Campaigns o Canvas, pero no ambos juntos. Cualquier Campaign o Canvas que haya enviado mensajes por última vez en los últimos 12 meses será elegible para un informe.

![Dashboard de Campaigns]({% image_buster /assets/img/campaign_comparison/create_report.png %}){: style="max-width:80%;"}

Las siguientes son las diferencias entre estas dos opciones:

| **Acción** | **Manual** | **Automatizado** |
| ---- | ---------- | ------------- |
| **Creación del informe** | Podrás reducir tu lista de Campaigns usando filtros y luego marcar Campaigns específicas. | Crearás tu informe usando las opciones de filtro para reducir tu lista de Campaigns. |
| **Guardar y ver el informe** | Puedes guardar tu informe. La próxima vez que lo veas, podrás ver las mismas Campaigns que añadiste previamente, ya que estas aún cumplen con tu filtro de "Último envío". | Puedes guardar tu informe. La próxima vez que lo veas, el informe se actualizará automáticamente para incluir todas las Campaigns que actualmente coincidan con tus filtros. |
| **Editar el informe** | Puedes seleccionar **Editar informe** para añadir o eliminar Campaigns de tu informe. | Puedes editar tu informe ajustando tus criterios de filtro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 1: Crear un informe nuevo" }

{% alert note %}
Tanto los informes **manuales** como los **automatizados** pueden incluir un máximo de 250 Campaigns en un informe.
{% endalert %}

Los informes de Canvas funcionan de manera similar a un informe manual de Campaigns, ya que las selecciones de Canvas y las actualizaciones del informe también deben hacerse manualmente. Puedes incluir como máximo cinco Canvas en un informe.

### Paso 2: Elegir tus métricas {#step-2-choose-your-metrics}

Después de crear tu informe, encontrarás una tabla vacía con Campaigns en cada fila. La tabla se completará después de que selecciones **Editar columnas** y elijas las métricas que deseas añadir.

![Opciones de Campaign]({% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}){: style="max-width:80%;"}

Tu tabla se completará con las métricas que elijas. Para las definiciones de estas métricas, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary). Algunas métricas solo están disponibles para informes comparativos de Campaigns.

También puedes alternar los cálculos del **Promedio** de cualquier tasa o métrica numérica y el **Total** de cualquier métrica numérica.

### Paso 3: Elegir un período de tiempo {#step-3-choose-a-time-period}

Puedes seleccionar un período de tiempo específico para ver los datos de tu informe. Si una Campaign, Canvas, variante en Canvas o componente de Canvas en particular no tiene datos para el período de tiempo seleccionado, los resultados de esa fila estarán vacíos.

![Métrica numérica de Campaign]({% image_buster /assets/img/campaign_comparison/metric.png %}){: style="max-width:60%;"}

### Paso 4: Nombrar y guardar tu informe {#step-4-name-and-save-your-report}

Nombra tu informe antes de guardarlo. Si un informe se guarda sin nombre, Braze aplicará un nombre predeterminado de "Campaign Comparison Report".

![Nota de Campaign]({% image_buster /assets/img/campaign_comparison/comparison_name.png %}){: style="max-width:60%;"}

Cuando estés listo, selecciona **Guardar**. Los informes guardados se pueden consultar más adelante en la página del **Generador de informes**.

## Informe comparativo de Campaigns con Campaigns multivariantes {#campaign-comparison-report-with-multivariate-campaigns}

Para cualquier Campaign multivariante, puedes ver estas métricas desglosadas por tus variantes y grupo de control haciendo clic en la flecha junto al nombre de la Campaign. Las filas que contienen tus variantes incluirán los resultados de rendimiento de esa variante, y la fila que contiene tu grupo de control incluirá solo los resultados de tus eventos de conversión.

![Nota de Campaign]({% image_buster /assets/img/campaign_comparison/compare_note.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Las métricas que completan la fila de tu Campaign general reflejarán el rendimiento de sus variantes, pero no incluirán el rendimiento del grupo de control. Por ejemplo, el evento de conversión primaria A de tu Campaign general será la suma del evento de conversión primaria A de tus variantes, y esto no incluirá el evento de conversión primaria A de tu grupo de control.

{% alert important %}
Si eliminas una variante de una Campaign multivariante, los datos de esa variante no estarán disponibles para su uso en un informe futuro.
{% endalert %}

## Desglose del informe comparativo de Canvas {#canvas-comparison-report-breakdown}

Dentro de un informe de Canvas, puedes ver tus Canvas desglosados por variante, pasos o mensaje.

### Variante {#variant}

Seleccionar **desglose por variante** te permite ver las estadísticas de alto nivel de tus Canvas generales, así como las estadísticas de cada variante, que se pueden expandir seleccionando la flecha junto al nombre del Canvas.

![Variantes]({% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}){: style="max-width:90%;"}

### Pasos {#steps}

Seleccionar **desglose por pasos** te permite ver métricas a nivel de paso, con cada fila del informe conteniendo la fila de un paso.

![Pasos]({% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}){: style="max-width:90%;"}

### Mensaje {#message}

Similar a un desglose a nivel de paso, seleccionar **desglose por mensaje** muestra el nombre de los pasos en cada fila. Sin embargo, dentro de **Editar columnas**, tendrás acceso a métricas a nivel de mensaje, como estadísticas específicas del canal, como clics de correo electrónico y aperturas de push.

![Informe]({% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}){: style="max-width:90%;"}

Ten en cuenta que dentro del dashboard de Braze puedes previsualizar las primeras 50 filas de tu informe de Canvas. Puedes acceder al informe completo cuando exportes un CSV.

## Acceder a informes guardados {#accessing-saved-reports}

Cuando accedes a un **informe manual** guardado, puedes ver las mismas Campaigns que añadiste previamente, ya que estas aún cumplen con tu filtro de "Último envío".

Cuando accedes a un **informe automatizado** guardado, el informe se actualizará automáticamente para incluir todas las Campaigns que actualmente coincidan con tus filtros. Por ejemplo, si tu informe filtraba Campaigns con la etiqueta "Promoción", cada vez que veas este informe, podrás ver todas las Campaigns con la etiqueta "Promoción", incluso si estas Campaigns fueron creadas después de que hiciste este informe.

## Editar informes {#editing-reports}

En un **informe manual**, puedes editar un informe seleccionando **Editar**. Desde ahí, puedes seleccionar o deseleccionar Campaigns para incluir en tu informe.

En un **informe automatizado**, alterna tus filtros para reducir los resultados en tu informe.

## Exportar informes {#exporting-reports}

También puedes seleccionar **Exportar** para descargar tu informe en CSV.

Si tu informe contiene Campaigns multivariantes, tu exportación incluirá dos archivos CSV:

- Un archivo que contiene solo las métricas de nivel superior de cada Campaign
- Un archivo que contiene métricas a nivel de variante

El archivo que contiene métricas de variante tendrá `variant_` añadido al inicio de su nombre. La primera vez que exportes un informe automatizado, recibirás una ventana emergente pidiéndote que concedas permiso para descargar múltiples archivos; haz clic en **Permitir**.

![Descarga de Campaign]({% image_buster /assets/img/campaign_comparison/download.png %}){: style="max-width:60%;"}

### Exportar informes comparativos de Canvas {#exporting-canvas-comparison-reports}

Tu exportación CSV reflejará la vista de desglose en la que te encontrabas cuando seleccionaste **Exportar**. Por ejemplo, si estabas en la vista de desglose a nivel de paso, tu exportación contendrá datos sobre tus métricas de paso. Para exportar datos de un desglose diferente, primero deberás navegar a ese desglose y seleccionar **Exportar** desde ahí.

Si descargas un informe de Canvas con desglose por variante, recibirás dos archivos CSV:

- Un archivo que contiene solo las métricas de nivel superior de cada Canvas
- Un archivo que contiene métricas a nivel de variante

## Crear gráficos {#building-charts}

Usa gráficos para visualizar una métrica seleccionada en tu informe. Los gráficos están disponibles para informes que incluyen Campaigns y tienen al menos una métrica añadida a sus columnas.

![Gráfico de rendimiento de Campaign con la métrica Mensajes enviados seleccionada]({% image_buster /assets/img/campaign_comparison/report_builder_charts.png %})

De forma predeterminada, el gráfico de cada informe mostrará la métrica de la primera columna del informe. Para seleccionar una métrica diferente para graficar, elige tu métrica del menú desplegable. Cualquier métrica en la tabla de tu informe estará disponible para mostrar en tu gráfico.

Puedes graficar como máximo tres métricas. Las unidades de todas las métricas deben ser las mismas; por ejemplo, si eliges una tasa en el primer menú desplegable, solo las tasas estarán disponibles para selección en el segundo menú desplegable.

Si tu gráfico contiene solo una métrica, mostrará hasta 30 Campaigns en orden descendente según la métrica que hayas seleccionado. Por ejemplo, si la métrica de tu gráfico es clics de correo electrónico, tu gráfico mostrará las 30 Campaigns de correo electrónico con más clics, ordenadas de mayor a menor cantidad de clics. Si tu informe contiene más de 30 Campaigns, solo las 30 principales se mostrarán en el gráfico. Si seleccionas más de una métrica, tu gráfico solo mostrará las cinco principales Campaigns según la primera métrica seleccionada.

Actualmente, los gráficos no se guardan cuando guardas tu informe.