---
nav_title: Generador de dashboards
article_title: Generador de dashboards
alias: "/dashboard_builder/"
description: "Este artículo de referencia explica cómo usar el Generador de dashboards para crear dashboards y visualizaciones utilizando informes creados en el Generador de consultas."
page_type: reference
tool:
    - Reports
page_order: 6
---

# Generador de dashboards {#dashboard-builder}

> Usa el Generador de dashboards para crear dashboards y visualizaciones utilizando informes creados en el Generador de informes o el Generador de consultas.

El Generador de dashboards te permite componer y visualizar dashboards de análisis personalizados desde cero y a partir de dashboards proporcionados por Braze. Puedes usar un origen de datos sin código (Generador de informes) o un origen de datos SQL (Generador de consultas) para alimentar tu dashboard, o empezar a partir de uno de los muchos dashboards proporcionados por Braze.

## Creación de un dashboard personalizado {#creating-a-custom-dashboard}

1. Ve a **Analytics** > **Generador de dashboards**.
2. Selecciona **Crear dashboard**.
3. Selecciona qué origen de datos alimentará tus informes:
- **Informes** que se crearon en el generador de informes
- **Consultas personalizadas** que se crearon en el generador de consultas<br><br>![Ventana para seleccionar el origen de datos de tu dashboard.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Ahora, sigue los pasos correspondientes a tu origen de datos:

{% tabs %}
{% tab Informes %}

{: start="4"}
4. Selecciona **+ Agregar mosaico** y luego elige uno de los informes que creaste en el [generador de informes (nuevo)]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

{% alert important %}
Después de que un informe del generador de informes se agrega a un mosaico del generador de dashboards, el mosaico no está conectado al informe original. Si editas el informe original en el generador de informes, debes eliminar el mosaico existente del dashboard y crear uno nuevo utilizando el informe actualizado como origen de datos.
{% endalert %}

{: start="5"}
5. Selecciona el icono de lápiz para cambiar cómo se muestran el título y el tipo de gráfico en el mosaico.
    - Puedes alternar entre diferentes tipos de gráfico en los controles de tipo de gráfico. Las opciones actuales incluyen gráficos de barras (horizontales o verticales) y gráficos de líneas (solo disponibles si seleccionaste **Fecha** como opción de desglose en la configuración del generador de informes).<br><br>![Controles para alternar entre diferentes tipos de gráfico.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    - Usa el menú desplegable de métricas para seleccionar qué métricas incluir en tu visualización. De forma predeterminada, la primera columna del informe será la métrica mostrada por defecto.
6. Selecciona **Guardar** después de haber cambiado la visualización a tu gusto.
7. Agrega un nombre, una descripción y una etiqueta para que tu dashboard sea más fácil de encontrar después.
{% endtab %}
{% tab Consultas personalizadas %}
{: start="4"}
4. Selecciona **+ Agregar mosaico** y luego elige una consulta que hayas ejecutado en el generador de consultas.
5. Para editar cómo se muestran los resultados de la consulta en el mosaico, selecciona el icono de lápiz para cambiar el título y el tipo de gráfico.
    - Puedes alternar entre diferentes tipos de gráfico en los controles de tipo de gráfico. Las opciones actuales incluyen tablas, gráficos de barras (horizontales o verticales) y gráficos de líneas.<br><br>![Controles para alternar entre diferentes tipos de gráfico.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        - Si eliges una de las opciones de gráfico, usa el menú desplegable del **eje X** para seleccionar una sola columna de los resultados de tu consulta como eje X.
        - Usa el menú desplegable del **eje Y** para seleccionar qué métricas incluir en tu visualización. De forma predeterminada, se mostrarán todas las columnas de los resultados de tu consulta, así que deselecciona las columnas que no te interese ver.<br><br>![Controles para alternar entre diferentes tipos de gráfico.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        - (Opcional) Puedes usar el menú desplegable de **Agrupación** para agrupar los resultados de tu consulta. Por ejemplo, si tienes el ID de Campaign como resultado de columna y quieres sumar todas las filas con ese valor, usa el menú desplegable de **Agrupación**.
        - (Opcional) Para editar los datos que se muestran, selecciona la consulta que está asociada al visual y realiza tus ediciones en el [generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder).
6. Selecciona **Guardar** después de haber cambiado la visualización a tu gusto.
7. Agrega un nombre, una descripción y una etiqueta para que tu dashboard sea más fácil de encontrar después.
{% endtab %}
{% endtabs %}

{: start="8"}
8. Repite los pasos 4-7 para tu método respectivo hasta que crees el dashboard deseado.
9. Selecciona **Ver dashboard** > selecciona **Ejecutar dashboard**.

Tu dashboard puede tardar hasta unos minutos en terminar de generar los informes.

{% alert note %}
Puedes agregar hasta 10 mosaicos a un dashboard.
{% endalert %}

## Gestión de mosaicos del dashboard {#managing-dashboard-tiles}

### Eliminar mosaicos {#delete-tiles}

Elimina un mosaico del dashboard seleccionando **Eliminar mosaico** en la parte inferior del mosaico. **Esta acción no se puede revertir.**

### Duplicar mosaicos {#duplicate-tiles}

Haz una copia de tu mosaico seleccionando **Duplicar mosaico** en la parte inferior del mosaico.

### Ajustar el tamaño y la posición de los mosaicos {#adjust-tile-size-and-position}

Ajusta el tamaño del mosaico arrastrando el controlador de redimensionamiento, y ajusta la posición del mosaico en el dashboard arrastrando el controlador del mosaico.

## Ejecutar un dashboard {#running-a-dashboard}

1. Ve a **Analytics** > **Generador de dashboards**. La página de inicio muestra todos los dashboards existentes en tu espacio de trabajo, con los dashboards creados por Braze en la parte superior. Estos se identifican con "(Braze)" en el título.
2. Selecciona el dashboard que te interese.
3. Selecciona **Run Dashboard** para cargar el dashboard correspondiente.

### Dashboards disponibles {#available-dashboards}

Braze proporciona dashboards prediseñados para casos de uso frecuentes. Usa la siguiente tabla como referencia única para los dashboards documentados actualmente y dónde acceder a cada uno.

| Dashboard | Ruta de acceso | Documentación |
| --- | --- | --- |
| Revenue - Last Touch Attribution | **Analytics** > **Generador de dashboards** | [Revenue - Last Touch Attribution](#revenue---last-touch-attribution) |
| Devices and carriers | **Analytics** > **Generador de dashboards** | [Dispositivos y operadores](#devices-and-carriers) |
| Segment Insights - Email | **Analytics** > **Generador de dashboards** | [Segment Insights - Email](#segment-insights---email) |
| Session Analytics | **Analytics** > **Generador de dashboards** | [Session Analytics](#session-analytics) |
| eCommerce Revenue - Last Touch Attribution | **Analytics** > **Generador de dashboards** | [Dashboard de ingresos de comercio electrónico]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/ecommerce_revenue_dashboard) |
| Messaging Diagnostics | **Analytics** > **Generador de dashboards** | [Dashboard de diagnóstico de mensajería]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) |
| Industry Benchmarks | **Analytics** > **Generador de dashboards** | [Dashboard de referencias del sector]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/industry_benchmarks_dashboard) |
| Email performance | **Analytics** > **Email Performance** | [Dashboards de rendimiento de canal]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#email-performance-dashboard) |
| SMS performance | **Analytics** > **SMS Performance** | [Dashboards de rendimiento de canal]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#sms-performance-dashboard) |
| Push performance | **Analytics** > **Generador de dashboards** > **Push Channel Dashboard** | [Dashboards de rendimiento de canal]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#push-performance-dashboard) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dashboards disponibles" }

{% alert note %}
La posibilidad de editar los dashboards creados por Braze aún no está disponible. Ponte en contacto con tu CSM si deseas solicitar dashboards adicionales.
{% endalert %}

#### Revenue - Last Touch Attribution {#revenue---last-touch-attribution}

El dashboard **Revenue - Last Touch Attribution** proporciona una revisión de los ingresos en Campaigns, Canvas y canales. Todos los datos de ingresos se atribuyen al último mensaje con el que se interactuó durante la ventana de atribución.

Las interacciones incluyen _clic en correo electrónico_ (clic en enlace), _clic en tarjeta de contenido_, _clic en mensaje dentro de la aplicación_ (excluyendo botones de cierre), _aperturas de push_, _clic en enlace corto de SMS_, _lectura de WhatsApp_ y _envío de webhook_.

| Métrica | Definición |
| --- | --- |
| Ingresos totales por último toque | Suma de todos los eventos de ingresos de Campaign y Canvas con un evento de último toque dentro del rango de fechas y ventana de atribución seleccionados. |
| Conversiones de compra totales | Recuento de todos los eventos de ingresos de Campaign y Canvas con un evento de último toque que cumple los requisitos. |
| Promedio de días para convertir | El tiempo promedio entre todos los eventos de compra de Campaign y Canvas con un evento de último toque que cumple los requisitos. |
| Ingresos por destinatario | Suma de los ingresos de eventos de ingresos que cumplen los requisitos dividida entre el número de usuarios únicos que recibieron un mensaje dentro del rango de fechas. |
| Compradores únicos | Recuento de los usuarios únicos con un evento de ingresos que cumple los requisitos. |
| Ingresos por país | Suma de todos los eventos de ingresos de Campaign y Canvas con un evento de último toque, agrupados por país. |
| Ingresos por Campaign | Suma de todos los eventos de ingresos de Campaign y Canvas con un evento de último toque que cumple los requisitos, agrupados por Campaign. |
| Ingresos por variante de campaña | Suma de todos los eventos de ingresos de Campaign y Canvas con un evento de último toque que cumple los requisitos, agrupados por variante de campaña. |
| Ingresos por Canvas | Suma de todos los eventos de ingresos de Campaign y Canvas con un evento de último toque que cumple los requisitos, agrupados por Canvas. |
| Ingresos por variante en Canvas | Suma de todos los eventos de ingresos de Campaign y Canvas con un evento de último toque que cumple los requisitos, agrupados por variante en Canvas. |
| Compras por producto | Recuento de todas las compras agrupadas por producto. |
| Ingresos por canal | Suma de todos los eventos de ingresos de Campaign y Canvas con un evento de último toque que cumple los requisitos, agrupados por canal. |
| Serie temporal de ingresos | Suma de todos los eventos de ingresos de Campaign y Canvas con un evento de último toque que cumple los requisitos, agrupados por día en UTC. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Revenue - Last Touch Attribution" }

#### Dispositivos y operadores {#devices-and-carriers}

| Métrica | Definición |
| --- | --- |
| Operadores de dispositivos | Recuento de usuarios en el rango de fechas seleccionado que abrieron una notificación push, agrupados por operador del dispositivo. |
| Modelo de dispositivo | Recuento de usuarios en el rango de fechas seleccionado que abrieron una notificación push, agrupados por modelo de dispositivo. |
| Sistema operativo del dispositivo | Recuento de usuarios en el rango de fechas seleccionado que abrieron una notificación push, agrupados por sistema operativo del dispositivo. |
| Tamaño de pantalla del dispositivo | Recuento de usuarios en el rango de fechas seleccionado que abrieron una notificación push, agrupados por resolución de pantalla del dispositivo (tamaño). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dispositivos y operadores" }

#### Segment Insights - Email {#segment-insights---email}

| Métrica | Definición |
|---|---|
| Métricas semanales de correo electrónico (tasas) | Tasas de participación de correo electrónico (entrega, rebote, apertura, clic, cancelación de suscripción) agrupadas por segmento y mostradas como serie temporal semanal. |
| Métricas semanales de correo electrónico (recuentos) | Recuentos de participación de correo electrónico (enviados, entregados, rebotes, aperturas, clics, cancelaciones de suscripción) agrupados por segmento y mostrados como serie temporal semanal. |
| Métricas semanales de compras (tasas) | Tasas de conversión de compras (ingresos por destinatario) a partir de aperturas y clics de correo electrónico, agrupadas por segmento y mostradas como serie temporal semanal. |
| Métricas semanales de compras (recuentos) | Recuentos de compras y totales de ingresos a partir de aperturas y clics de correo electrónico, agrupados por segmento y mostrados como serie temporal semanal. |
| Participación de correo electrónico por Segment | Tabla resumen que muestra las métricas totales de participación de correo electrónico (enviados, entregados, rebotes, aperturas, clics, cancelaciones de suscripción y sus tasas) agregadas por segmento. |
| Compras e ingresos por Segment | Tabla resumen que muestra las métricas totales de compras (compras, ingresos e ingresos por destinatario) a partir de aperturas y clics de correo electrónico, agregadas por segmento. |
| Top 10 de Campaigns para métricas de participación | Lista clasificada de Campaigns con las métricas de participación de correo electrónico más altas (métrica configurable para la clasificación). |
| Últimas 10 Campaigns para métricas de participación | Lista clasificada de Campaigns con las métricas de participación de correo electrónico más bajas (métrica configurable para la clasificación). |
| Top 10 de Canvas para métricas de participación | Lista clasificada de Canvas con las métricas de participación de correo electrónico más altas (métrica configurable para la clasificación). |
| Últimos 10 Canvas para métricas de participación | Lista clasificada de Canvas con las métricas de participación de correo electrónico más bajas (métrica configurable para la clasificación). |
| Top 10 de Campaigns para métricas de compras | Lista clasificada de Campaigns con las métricas de conversión de compras más altas a partir de participación de correo electrónico (métrica configurable para la clasificación). |
| Últimas 10 Campaigns para métricas de compras | Lista clasificada de Campaigns con las métricas de conversión de compras más bajas a partir de participación de correo electrónico (métrica configurable para la clasificación). |
| Top 10 de Canvas para métricas de compras | Lista clasificada de Canvas con las métricas de conversión de compras más altas a partir de participación de correo electrónico (métrica configurable para la clasificación). |
| Últimos 10 Canvas para métricas de compras | Lista clasificada de Canvas con las métricas de conversión de compras más bajas a partir de participación de correo electrónico (métrica configurable para la clasificación). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment Insights - Email" }

#### Session Analytics {#session-analytics}

| Métrica | Definición |
|---|---|
| N.º de sesiones por día (serie temporal) | Recuento de sesiones únicas agrupadas por día dentro del rango de fechas seleccionado, mostrado como serie temporal. |
| Promedio de sesiones por usuario | Número promedio de sesiones por usuario calculado como el total de sesiones dividido entre los usuarios únicos dentro del rango de fechas seleccionado. |
| Campaigns que convierten en sesiones | Recuento de sesiones únicas que ocurrieron al mismo tiempo que las conversiones de Campaign, agrupadas por ID de Campaign y clasificadas por recuento de sesiones. |
| Canvas que convierten en sesiones | Recuento de sesiones únicas que ocurrieron al mismo tiempo que las conversiones de Canvas, agrupadas por ID de Canvas y clasificadas por recuento de sesiones. |
| N.º total de sesiones por usuario | Lista de los 1,000 usuarios principales por su recuento total de sesiones dentro del rango de fechas seleccionado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Session Analytics" }

## Comparte tus comentarios con nosotros {#share-your-feedback-with-us}

{% multi_lang_include product_feedback_cta.md context="pain_point" channel="ux" feature="Dashboard Builder" %}