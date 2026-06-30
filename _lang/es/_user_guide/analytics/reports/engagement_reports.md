---
nav_title: Informes de interacción
article_title: Informes de interacción
page_order: 5
local_redirect:
  report-glossary: '/docs/user_guide/analytics/metrics_glossary'
page_type: tutorial
description: "Este artículo te explica cómo crear, personalizar y planificar informes de interacción para campañas y Canvas."
tool:
  - Campaigns
  - Canvas
  - Reports
---

# Informes de interacción {#engagement-reports}

> Los informes de interacción te permiten obtener estadísticas de interacción de mensajes específicos de campañas y Canvas para recibirlas por correo electrónico en el horario que prefieras.

{% alert note %}
Necesitas permisos de "Exportar datos de usuario" para ejecutar informes de interacción.
{% endalert %}

Con los informes de interacción, puedes seleccionar manualmente las campañas y Canvas que deseas incluir en tu informe por correo electrónico, o especificar reglas para seleccionar automáticamente las campañas y Canvas relevantes.

Independientemente del número de campañas o Canvas que selecciones, se generan hasta dos archivos CSV: uno para todos los datos de campaña y otro para todos los datos de Canvas. Puedes acceder a estos archivos CSV desde el enlace incluido en el correo electrónico de tu informe. Los informes de interacción no se guardan en el panel de Braze.

Ciertos datos se agregan a nivel de campaña o Canvas en lugar de a nivel de variante de campaña individual o paso en Canvas. Si [eliminas un paso en Canvas después del lanzamiento]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#canvas-details), esto también eliminará los datos de los informes de interacción.

{% alert tip %}
Puedes volver a ejecutar el informe para generar estadísticas actualizadas.
{% endalert %}

## Crear un nuevo informe {#creating-a-new-report}

### Paso 1: Crear un informe {#step-1-create-a-report}

En tu cuenta del dashboard, ve a **Analytics** > **Engagement Reports**. Selecciona **+ Create New Report**.

### Paso 2: Añadir mensajes {#step-2-add-messages}

Añade las campañas y los mensajes de Canvas que deseas compilar en tu informe. Puedes seleccionar tus mensajes de dos formas:

- Seleccionar manualmente campañas y Canvas
- Seleccionar automáticamente campañas y Canvas en función de reglas específicas

![engagement_reports_message_selection]({% image_buster /assets/img_archive/engagement_report_add_messages.png %})

#### Seleccionar manualmente campañas o Canvas {#manually-select-campaigns-or-canvases}

Esta opción te da la libertad de elegir las campañas o Canvas que desees para este informe.

#### Seleccionar automáticamente campañas o Canvas {#automatically-select-campaigns-or-canvases}

Esta opción te permite incluir automáticamente todos los mensajes que contengan una [etiqueta]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) específica. Puedes dirigirte a mensajes que tengan una o todas las etiquetas listadas. Esta opción es útil si estás configurando informes recurrentes y etiquetas regularmente tus mensajes de interacción.

{% alert important %}
Las etiquetas deben coincidir con al menos una campaña o Canvas para que se genere un informe. Si utilizas **Automatically select campaigns and Canvases based on specific rules** y ves un error, confirma que al menos una campaña o Canvas coincide con tus etiquetas y otros filtros (por ejemplo, cuando requieres todas las etiquetas listadas, cada mensaje coincidente debe tener todas las etiquetas).
{% endalert %}

### Paso 3: Añadir estadísticas {#add-statistics-to-your-reports}

El paso **Add Stats** te muestra las estadísticas para los tipos de campañas o Canvas que hayas seleccionado. Por ejemplo, si seleccionaste mensajes de correo electrónico, solo podrás ver las estadísticas relevantes de correo electrónico. Si elegiste una combinación de correo electrónico y push, podrás ver las estadísticas de esos dos canales.

![engagement_report_add_stats]({% image_buster /assets/img_archive/engagement_report_add_stats.png %})

Los informes de interacción agregan datos por campaña o Canvas, no a nivel de espacio de trabajo. Para monitorear el volumen total de envíos o impresiones en todas las campañas y Canvas activos, como los envíos e impresiones por canal en todo un espacio de trabajo, usa el [Generador de informes]({{site.baseurl}}/report_builder).

{% alert note %}
*Envíos al operador* está obsoleto, pero seguirá siendo compatible para los usuarios que ya lo tienen.
{% endalert %}

| Canal | Estadísticas disponibles |
| ------| --------------|
| Correo electrónico | Envíos, Aperturas, Aperturas únicas, Clics, Clics únicos, Clic a apertura, Cancelaciones de suscripción, Rebotes, Entregados, Correo no deseado reportado |
| Push  | Envíos, Aperturas, Influenced Opens, Rebotes, Clics en el cuerpo |
| Notificación push web | Envíos, Aperturas, Rebotes, Clics en el cuerpo |
| Mensaje dentro de la aplicación | Impresiones, Clics, Clics en el primer botón, Clics en el segundo botón |
| Webhook  |  Envíos, Errores |
| SMS | Envíos, Envíos al operador, Entregas confirmadas, Fallos de entrega, Rechazos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Añadir estadísticas #add-statistics-to-your-reports" }

### Paso 4: Completar la configuración del informe {#step-4-complete-report-setup}

Dale un nombre a tu informe, elige cómo se formateará y selecciona tus destinatarios. De forma predeterminada, los informes de interacción se envían como un archivo ZIP donde los datos están delimitados por comas (donde cada dato está separado por una coma).

Puedes seleccionar entre las siguientes opciones de compresión y delimitador:

- **Compresión:** ZIP, sin comprimir o gzip
- **Delimitador:** Coma (`,`), dos puntos (`:`), punto y coma (`;`) o barra vertical (`|`)

{% alert note %}
Las estadísticas solo se recopilan para el rango de fechas especificado por el informe. Para recibir estadísticas precisas de tasa de apertura y clics, selecciona un rango de fechas que incluya cuándo se realizaron los eventos de envío para tus campañas y Canvas.
{% endalert %}

#### Seleccionar periodo de tiempo {#select-time-frame}

De forma predeterminada, el rango de datos mostrado se basa en la zona horaria de tu empresa e irá desde el mensaje más antiguo seleccionado hasta la fecha actual. Puedes personalizar esto seleccionando el menú desplegable de fecha y usando la selección de rango personalizado O seleccionando el siguiente botón de opción y definiendo tu rango de fechas con las opciones desplegables disponibles.

#### Seleccionar visualización de datos {#select-data-display}

De forma predeterminada, los datos mostrados en los informes de interacción son diarios (un día). Para ver estos datos en diferentes intervalos, elige un número explícito de días o semanas para agregar los datos del informe. Así, en lugar de ver métricas diarias, puedes ver tu interacción por semana, mes, trimestre o similar. Si una agregación centrada en el tiempo no es suficiente, también puedes optar por exportar datos a nivel de campaña o Canvas.

![engagement_reports_data_coverage]({% image_buster /assets/img_archive/engagement_report_datacoverage.png %})

##### Mostrar datos por campaña o Canvas completo {#show-data-by-entire-campaign-or-canvas}

Cuando seleccionas **Show Data by Entire Campaign or Canvas**, Braze agrega las métricas en bloques de 1825 días (cinco años) a lo largo del rango de tiempo del informe.

Si el rango de tiempo abarca más de un bloque, es posible que veas varias filas para la misma campaña o Canvas con diferentes fechas en la columna de fecha. Algunas filas pueden incluir solo métricas registradas más adelante en el rango (por ejemplo, cancelaciones de suscripción). Las fechas también pueden ser anteriores a cuando comenzaste a enviar en el espacio de trabajo, porque reflejan los límites de los bloques en la exportación, no solo tu primer envío.

Para alinear la columna de fecha con el momento en que tus campañas y Canvas seleccionados realmente enviaron, establece la [fecha de inicio del informe en **Seleccionar periodo de tiempo**](#select-time-frame) a la fecha más temprana que deseas en el archivo, generalmente cuando esos mensajes comenzaron a enviarse, en lugar de dejar el rango predeterminado que se remonta al mensaje seleccionado más antiguo.

#### Planificar tu informe {#schedule-your-report}

Hay dos opciones al planificar tu informe:

- **Enviar inmediatamente:** Después de lanzar el informe, Braze lo enviará de inmediato.
- **Enviar en un horario designado:** Esta opción te da la flexibilidad de elegir con qué frecuencia recibes este informe. Puedes elegir enviar este informe cada cierto número de días, semanas o meses. También puedes definir cuándo dejar de enviar el informe.

![engagement_reports_schedule_report]({% image_buster /assets/img_archive/engagement_report_reportschedule.png %}){: style="max-width:65%;" }

### Paso 5: Revisar y lanzar {#step-5-review-and-launch}

El paso final de la configuración de tu informe muestra un resumen de solo lectura de las opciones configuradas. Revisa tu informe y, cuando estés satisfecho, selecciona **Launch Report**.

### Paso 6: Revisa tu correo electrónico {#step-6-check-your-email}

Recibirás un correo electrónico con enlaces a tus informes en el horario o planificación elegidos. **Estos enlaces caducan 1 hora después de que se envió el informe.** Cuando selecciones los enlaces proporcionados, se descargará automáticamente un archivo ZIP que contiene tus archivos CSV, uno para todas las campañas.

El informe contiene todas las estadísticas seleccionadas en la sección [Añadir estadísticas](#add-statistics-to-your-reports) del proceso de configuración.

## Solución de problemas {#troubleshooting}

### El informe de interacción no coincide con las métricas del Canvas o la campaña {#engagement-report-doesnt-match-metrics-from-the-canvas-or-campaign}

#### Rango de tiempo no coincidente {#mismatched-time-range}

Asegúrate de que las fechas en el informe de interacción coincidan con las fechas en los análisis del Canvas o la campaña (por ejemplo, que ambos cubran del 1 al 15 de diciembre), incluso si el Canvas solo envió una vez. En la configuración del informe de interacción, revisa **Data Display** para confirmar que estás viendo el Canvas o la campaña correctos. Si **Data Display** está configurado para mostrar datos cada *X* días, obtendrás una fila por fecha cuando se registraron métricas para cada paso.

Si los totales parecen incorrectos en una hoja de cálculo, limpia los filtros adicionales en la exportación. Puedes sumar las filas diarias para conciliarlas con los totales del Canvas o la campaña para el mismo rango de tiempo.

{% alert note %}
Si deseas filas agregadas por campaña o Canvas completo en lugar de contenedores diarios, semanales u otros recurrentes, configura **Data Display** en **Show Data by Entire Campaign or Canvas**. Si los recuentos de filas o las fechas parecen incorrectos en el CSV, consulta [Mostrar datos por campaña o Canvas completo](#show-data-by-entire-campaign-or-canvas).
{% endalert %}

#### Clics de botón duplicados en mensajes dentro de la aplicación HTML {#duplicate-button-clicks-in-html-in-app-messages}

Si utilizas mensajes dentro de la aplicación HTML y los **clics en el cuerpo** parecen altos en el informe de interacción, es posible que estés registrando clics dos veces, por ejemplo, al llamar a `brazeBridge.logClick()` para un clic genérico en el cuerpo y también `brazeBridge.logClick('body click')` (u otro ID) en la misma interacción. Busca en tu código `brazeBridge.logClick(` y alinea con un patrón por control. Para el uso recomendado, consulta [Seguimiento de botones]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#button-tracking-improvements).

#### Enlaces rotos en los correos electrónicos de informes de interacción {#broken-links-in-emailed-engagement-reports}

Si los enlaces en un correo electrónico de informe de interacción planificado no se abren correctamente en tu cliente de correo, prueba estos pasos:

1. Reenvía el informe a una bandeja de entrada de Gmail y abre los enlaces en Google Chrome.
2. En la configuración del informe de interacción, confirma que **Report Schedule** está configurado para enviar cuando esperas (por ejemplo, inmediatamente después de que se genere el informe en lugar de en una planificación diferida).