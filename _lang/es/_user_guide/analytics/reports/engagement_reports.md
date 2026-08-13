---
nav_title: Informes de participación
article_title: Informes de participación
page_order: 5
local_redirect:
  report-glossary: '/docs/user_guide/analytics/metrics_glossary'
page_type: tutorial
description: "Este artículo te explica cómo crear, personalizar y programar informes de participación para Campaigns y Canvas."
tool:
  - Campaigns
  - Canvas
  - Reports
---

# Informes de participación {#engagement-reports}

> Los informes de participación te permiten obtener estadísticas de participación de mensajes específicos de Campaigns y Canvas para recibirlas por correo electrónico en el horario que prefieras.

{% alert note %}
Necesitas permisos de "Exportar datos de usuario" para ejecutar informes de participación.
{% endalert %}

Con los informes de participación, puedes seleccionar manualmente las Campaigns y Canvas que deseas incluir en tu informe por correo electrónico, o especificar reglas para seleccionar automáticamente las Campaigns y Canvas relevantes.

Independientemente del número de Campaigns o Canvas que selecciones, se generan hasta dos archivos CSV: uno para todos los datos de Campaign y otro para todos los datos de Canvas. Puedes acceder a estos archivos CSV desde el enlace incluido en el correo electrónico de tu informe. Los informes de participación no se guardan en el panel de Braze.

Ciertos datos se agregan a nivel de Campaign o Canvas en lugar de a nivel de variante de campaña individual o paso en Canvas. Si [eliminas un paso en Canvas después del lanzamiento]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#canvas-details), esto también eliminará los datos de los informes de participación.

{% alert tip %}
Puedes volver a ejecutar el informe para generar estadísticas actualizadas.
{% endalert %}

## Crear un informe nuevo {#creating-a-new-report}

### Paso 1: Crear un informe {#step-1-create-a-report}

En tu cuenta del panel, ve a **Analytics** > **Engagement reports**. Selecciona **+ Create New Report**.

### Paso 2: Añadir mensajes {#step-2-add-messages}

Añade las Campaigns y los mensajes de Canvas que deseas compilar en tu informe. Puedes seleccionar tus mensajes de dos formas:

- Seleccionar manualmente Campaigns y Canvas
- Seleccionar automáticamente Campaigns y Canvas según reglas específicas

![Selección de mensajes del informe de participación]({% image_buster /assets/img_archive/engagement_report_add_messages.png %})

#### Seleccionar manualmente Campaigns o Canvas {#manually-select-campaigns-or-canvases}

Esta opción te da la libertad de elegir las Campaigns o Canvas que desees incluir en este informe.

#### Seleccionar automáticamente Campaigns o Canvas {#automatically-select-campaigns-or-canvases}

Esta opción te permite incluir automáticamente todos los mensajes que contengan una [etiqueta]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) específica. Puedes dirigirte a mensajes que tengan una o todas las etiquetas listadas. Esta opción es útil si estás configurando informes recurrentes y etiquetas regularmente tus mensajes de participación.

{% alert important %}
Las etiquetas deben coincidir con al menos una Campaign o un Canvas para que se genere un informe. Si utilizas **Seleccionar automáticamente Campaigns y Canvas según reglas específicas** y ves un error, confirma que al menos una Campaign o un Canvas coincide con tus etiquetas y otros filtros (por ejemplo, cuando requieres todas las etiquetas listadas, cada mensaje coincidente debe tener todas las etiquetas).
{% endalert %}

### Paso 3: Añadir estadísticas {#add-statistics-to-your-reports}

El paso **Add Stats** te muestra las estadísticas para los tipos de Campaigns o Canvas que hayas seleccionado. Por ejemplo, si seleccionaste mensajes de correo electrónico, solo podrás ver las estadísticas relevantes de correo electrónico. Si elegiste una combinación de correo electrónico y push, podrás ver las estadísticas de esos dos canales.

![Añadir estadísticas al informe de participación]({% image_buster /assets/img_archive/engagement_report_add_stats.png %})

Los informes de participación agregan datos por Campaign o Canvas, no a nivel de espacio de trabajo. Para monitorear el volumen total de envíos o impresiones en todas las Campaigns y Canvas activos, como los envíos e impresiones por canal en todo un espacio de trabajo, utiliza el [generador de informes]({{site.baseurl}}/report_builder).

{% alert note %}
*Sends to Carrier* está obsoleto, pero seguirá siendo compatible para los usuarios que ya lo tienen.
{% endalert %}

| Canal | Estadísticas disponibles |
| ------| --------------|
| Correo electrónico | Sends, Opens, Unique Opens, Clicks, Unique Clicks, Click to Open, Unsubscribes, Bounces, Delivered, Reported Spam |
| Push  | Sends, Opens, Influenced Opens, Bounces, Body Clicks |
| Notificación push web | Sends, Opens, Bounces, Body Clicks |
| Mensaje dentro de la aplicación | Impressions, Clicks, First Button Clicks, Second Button Clicks |
| Webhook  |  Sends, Errors |
| SMS | Sends, Sends to Carrier, Confirmed Deliveries, Delivery Failures, Rejections |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Añadir estadísticas #add-statistics-to-your-reports" }

### Paso 4: Completar la configuración del informe {#step-4-complete-report-setup}

Dale un nombre a tu informe, elige cómo se formateará y selecciona a tus destinatarios. De forma predeterminada, los informes de participación se envían como un archivo ZIP donde los datos están delimitados por comas (donde cada dato está separado por una coma).

Puedes seleccionar entre las siguientes opciones de compresión y delimitador:

- **Compresión:** ZIP, sin comprimir o gzip
- **Delimitador:** Coma (`,`), dos puntos (`:`), punto y coma (`;`) o barra vertical (`|`)

{% alert note %}
Las estadísticas solo se recopilan para el rango de fechas especificado por el informe. Para recibir estadísticas precisas de tasa de aperturas y clics, selecciona un rango de fechas que incluya cuándo se realizaron los eventos de envío para tus Campaigns y Canvas.
{% endalert %}

#### Seleccionar período de tiempo {#select-time-frame}

De forma predeterminada, el rango de datos mostrado se basa en la zona horaria de tu empresa e irá desde el mensaje más antiguo seleccionado hasta la fecha actual. Puedes personalizar esto seleccionando el menú desplegable de fechas y usando la selección de rango personalizado O seleccionando el siguiente botón de opción y definiendo tu rango de fechas con las opciones desplegables disponibles.

#### Seleccionar visualización de datos {#select-data-display}

De forma predeterminada, los datos mostrados en los informes de participación son diarios (un día). Para ver estos datos en diferentes intervalos, elige un número explícito de días o semanas para agregar los datos del informe. Así, en lugar de ver métricas diarias, puedes ver tu participación por semana, mes, trimestre o similar. Si una agregación centrada en el tiempo no es suficiente, también puedes optar por exportar datos a nivel de Campaign o Canvas.

![Cobertura de datos del informe de participación]({% image_buster /assets/img_archive/engagement_report_datacoverage.png %})

##### Mostrar datos por Campaign o Canvas completo {#show-data-by-entire-campaign-or-canvas}

Cuando seleccionas **Show Data by Entire Campaign or Canvas**, Braze agrega las métricas en bloques de 1825 días (cinco años) a lo largo del rango de tiempo del informe.

Si el rango de tiempo abarca más de un bloque, es posible que veas varias filas para la misma Campaign o Canvas con diferentes fechas en la columna de fecha. Algunas filas pueden incluir solo métricas registradas más adelante en el rango (por ejemplo, cancelaciones de suscripción). Las fechas también pueden ser de años antes de que comenzaras a enviar en el espacio de trabajo, porque reflejan los límites de los bloques en la exportación, no solo tu primer envío.

Para alinear la columna de fecha con el momento en que tus Campaigns y Canvas seleccionados realmente enviaron, establece la [fecha de inicio del informe en **Seleccionar período de tiempo**](#select-time-frame) a la fecha más temprana que deseas en el archivo, generalmente cuando esos mensajes comenzaron a enviarse, en lugar de dejar el rango predeterminado que se remonta al mensaje seleccionado más antiguo.

En el CSV exportado, la primera columna es la fecha:

- **Mostrar datos por Campaign o Canvas completo:** La fecha es el inicio del rango de fechas del informe o un límite de bloque dentro de él, no la fecha de inicio de la Campaign o el Canvas.
- **Mostrar datos por cada X días o semanas:** La fecha de cada fila refleja cuándo ocurrieron los eventos en esa ventana de agregación.

#### Programar tu informe {#schedule-your-report}

Hay dos opciones al programar tu informe:

- **Enviar inmediatamente:** Después de que se lance el informe, Braze lo enviará de inmediato.
- **Enviar en un momento designado:** Esta opción te da la flexibilidad de elegir con qué frecuencia recibes este informe. Puedes elegir enviar este informe cada cierto número de días, semanas o meses. También puedes definir cuándo dejar de enviar el informe.

![Programación del informe de participación]({% image_buster /assets/img_archive/engagement_report_reportschedule.png %}){: style="max-width:65%;" }

### Paso 5: Revisar y lanzar {#step-5-review-and-launch}

El paso final de la configuración de tu informe muestra un resumen de solo lectura de las opciones configuradas. Revisa tu informe y, cuando estés satisfecho, selecciona **Launch Report**.

### Paso 6: Revisa tu correo electrónico {#step-6-check-your-email}

Recibirás un correo electrónico con enlaces a tus informes en el momento o la programación que hayas elegido. **Estos enlaces caducan 1 hora después de que se envió el informe.** Cuando selecciones los enlaces proporcionados, se descargará automáticamente un archivo ZIP que contiene tus archivos CSV, uno para todas las Campaigns.

El informe contiene todas las estadísticas seleccionadas en la sección [Add Stats](#add-statistics-to-your-reports) del proceso de configuración.

## Solución de problemas {#troubleshooting}

### Las métricas del informe de participación difieren del panel de rendimiento de correo electrónico {#engagement-report-metrics-differ-from-the-email-performance-dashboard}

Los informes de participación y el [panel de rendimiento de correo electrónico]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance) utilizan las mismas definiciones de métricas de correo electrónico. Ambos atribuyen las aperturas y los clics al día en que cada evento **ocurrió**, y ambos calculan *Unique Opens* y *Unique Clicks* como recuentos únicos de siete días por día que se suman a lo largo del rango de fechas seleccionado. Para ver las definiciones, consulta [Métricas de correo electrónico]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary) y [Cómo se calculan las métricas]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#how-metrics-are-calculated) en la página de paneles de rendimiento de canal.

Si los totales siguen siendo diferentes para las mismas Campaigns y el mismo período, comprueba lo siguiente:

| Verificación | Por qué es importante |
| --- | --- |
| Rango de fechas y zona horaria | Ambas superficies deben cubrir los mismos días calendario en la misma zona horaria. |
| Selección de Campaign o Canvas | El panel de rendimiento de correo electrónico agrega la actividad de correo electrónico en todo el espacio de trabajo. Un informe de participación incluye solo las Campaigns o Canvas que seleccionaste. |
| Filas diarias frente a totales del informe | Si **Data Display** divide la exportación en filas diarias, suma esas filas para compararlas con los totales del panel para el mismo rango. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verificaciones cuando las métricas de correo electrónico del informe de participación difieren del panel de rendimiento de correo electrónico" }

Las diferencias son más comunes cuando las cifras del informe de participación se comparan con los análisis de **Campaign** o **Canvas** en lugar del panel de rendimiento de correo electrónico. Las páginas de Campaign y Canvas pueden mostrar métricas de fecha de envío (por ejemplo, envíos o conversiones atribuidos a la fecha de envío) junto con aperturas y clics de fecha de evento. Consulta [El informe de participación no coincide con las métricas del Canvas o la Campaign](#engagement-report-doesnt-match-metrics-from-the-canvas-or-campaign).

### El informe de participación no coincide con las métricas del Canvas o la Campaign {#engagement-report-doesnt-match-metrics-from-the-canvas-or-campaign}

#### Rango de tiempo no coincidente {#mismatched-time-range}

Asegúrate de que las fechas en el informe de participación coincidan con las fechas en los análisis del Canvas o la Campaign (por ejemplo, que ambos cubran del 1 al 15 de diciembre), incluso si el Canvas solo se envió una vez. En la configuración del informe de participación, comprueba **Data Display** para confirmar que estás viendo el Canvas o la Campaign correctos. Si **Data Display** está configurado para mostrar datos cada *X* días, obtendrás una fila por fecha en la que se registraron métricas para cada paso.

Si los totales parecen incorrectos en una hoja de cálculo, elimina los filtros adicionales en la exportación. Puedes sumar las filas diarias para conciliarlas con los totales del Canvas o la Campaign para el mismo rango de tiempo.

{% alert note %}
Si deseas que las filas se agreguen por Campaign o Canvas completo en lugar de contenedores diarios, semanales u otros recurrentes, configura **Data Display** en **Show Data by Entire Campaign or Canvas**. Si los recuentos de filas o las fechas parecen incorrectos en el CSV, consulta [Show Data by Entire Campaign or Canvas](#show-data-by-entire-campaign-or-canvas).
{% endalert %}

#### Clics de botón duplicados en mensajes dentro de la aplicación HTML {#duplicate-button-clicks-in-html-in-app-messages}

Si utilizas mensajes dentro de la aplicación HTML y los **Body clicks** parecen altos en el informe de participación, es posible que estés registrando clics dos veces; por ejemplo, al llamar a `brazeBridge.logClick()` para un clic genérico en el cuerpo y también a `brazeBridge.logClick('body click')` (u otro ID) en la misma interacción. Busca `brazeBridge.logClick(` en tu código y alinea con un solo patrón por control. Para el uso recomendado, consulta [Seguimiento de botones]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#button-tracking-improvements).

#### Enlaces rotos en correos electrónicos de informes de participación {#broken-links-in-emailed-engagement-reports}

Si los enlaces en un correo electrónico de informe de participación programado no se abren correctamente en tu cliente de correo, prueba estos pasos:

1. Reenvía el informe a un buzón de Gmail y abre los enlaces en Google Chrome.
2. En la configuración del informe de participación, confirma que **Report Schedule** está configurado para enviarse cuando esperas (por ejemplo, inmediatamente después de que se genere el informe en lugar de en un horario diferido).