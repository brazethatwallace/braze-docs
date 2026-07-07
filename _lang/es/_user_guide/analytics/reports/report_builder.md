---
nav_title: Generador de informes
article_title: Generador de informes
alias: /report_builder/
page_type: reference
description: "Este artículo de referencia describe la característica del Generador de informes."
tool:
    - Reports
page_order: 3
---

# Generador de informes {#report-builder}

> Esta página explica cómo usar el Generador de informes para crear y ver informes detallados con datos de Braze, y cómo añadir informes a paneles.

El siguiente video ofrece un resumen de cómo crear y personalizar informes en el Generador de informes.

{% multi_lang_include video.html id="oi66kwwldv" source="wistia" %}

## Usar una plantilla de informe {#using-a-report-template}

1. Ve a **Analytics** > **Report Builder (New)**.
2. Selecciona la flecha de **Más opciones** junto al botón **Create New Report** y luego selecciona **Use a report template**.<br><br>![Desplegable del botón "Create New Report" con opciones para crear un informe personalizado o usar una plantilla.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Selecciona una de las plantillas de informe de la biblioteca de plantillas de Braze.
    - Usa los desplegables **Row items** y **Tags** para encontrar informes relevantes para tus casos de uso.<br><br>![Ventana "Plantillas de informe de Braze" con una lista de plantillas de Braze para seleccionar.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. Sigue desde el paso 3 en adelante en [Crear un informe](#creating-a-report) para personalizar aún más el informe según tu caso de uso.

## Crear un informe {#creating-a-report}

1. Ve a **Analytics** > **Report Builder (New)**.
2. Selecciona **Create New Report**.
3. En el desplegable **Rows**, selecciona sobre qué quieres generar el informe:
    - Campaigns
    - Canvas
    - Campaigns y Canvas
    - Canales
    - Etiquetas

    Ten en cuenta que tu selección de **Rows** afectará [las métricas que puedes ver](#metrics-availability). Por ejemplo, puedes ver métricas multivariantes solo si generas un informe sobre **Canvas** o **Campaigns** con un desglose por **Variant**. No puedes ver esas métricas cuando generas un informe sobre **Campaigns y Canvas**, incluso si esas Campaigns y Canvas tienen pruebas multivariantes.

![La sección "Filas y columnas" con campos para seleccionar las filas y agrupaciones de tu informe.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4. (Opcional) Selecciona **Add drilldown** para desglosar tus datos en vistas más detalladas:
    - Canales
    - Fecha
        - Usa esta opción para dividir tus datos en rangos de tiempo más pequeños. Por ejemplo, si te interesa cómo rindieron tus campañas por día, selecciona la siguiente configuración:
            - **Rows**: Campaigns
            - **Grouping:** Date
            - **Interval:** Days
    - Variantes
    - Campaigns y Canvas

{% alert tip %}
Prueba diferentes configuraciones de opciones de desglose para explorar las [muchas formas en que puedes desglosar tus datos](#metrics-availability).
{% endalert %}

{: start="5"}
5. En la sección **Columns**, selecciona **Customize Metrics**.

![La sección "Customize Metrics" con opciones para seleccionar múltiples métricas.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6. Examina las métricas por categoría y selecciona la casilla correspondiente para añadir una métrica a tu informe.
    - Reordena las métricas y columnas arrastrando el icono de puntos hacia arriba o hacia abajo.
7. En **Report content**, configura el rango de fechas para el cual deseas incluir datos en tu informe.
8. Luego, dependiendo de tus selecciones en el paso 3, elige añadir campañas, Canvas o ambos a tu informe de forma manual o automática.
    - **Añadir manualmente:** Elige cada campaña o Canvas que deseas incluir en el informe usando los filtros de fechas de **Last Sent** y etiquetas o canales, o buscando el nombre de la campaña o Canvas.<br><br>![La sección "Añadir manualmente campañas y Canvas" con una lista de campañas para seleccionar.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **Añadir automáticamente:** Establece reglas para determinar qué campañas o Canvas incluir en el informe. Solo necesitas seleccionar un campo en esta página.
        - Ten en cuenta que a medida que campañas o Canvas adicionales cumplan las condiciones que estableciste en esta pantalla, se añadirán automáticamente a futuras ejecuciones de tu informe.<br><br>![La sección "Añadir automáticamente campañas y Canvas" con campos para establecer reglas sobre qué campañas y Canvas deben añadirse al informe.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9. Ejecuta el informe seleccionando **Save & Run**.

{% alert note %}
El informe puede tardar hasta unos minutos en ejecutarse, dependiendo del rango de fechas y la cantidad de campañas o Canvas que seleccionaste en la etapa de configuración.
{% endalert %}

## Disponibilidad de métricas {#metrics-availability}

Tu selección de **Rows** afecta las métricas que puedes seleccionar.

{% alert tip %}
Si deseas generar un informe sobre variantes o pasos de Canvas, selecciona **Canvas** para las filas y deja el campo vacío o selecciona **Date** como desglose. Esto crea un desplegable **Canvas View** para ver métricas solo del Canvas, o agrupar métricas por variante, paso o mensaje.<br><br> Cuando agrupas por paso, la tabla de vista previa mientras configuras tu informe muestra un máximo de 50 filas. Ejecuta el informe o expórtalo como CSV para ver todas las filas.

![El desplegable "Canvas View" abierto.]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Métrica | Descripción |
| --- | --- |
| Métricas de conversión | Disponibles para Campaigns, Canvas, Campaigns y Canvas. |
| Entradas | Disponibles para Campaigns, Canvas, Campaigns y Canvas, etiquetas. |
| Fecha del último envío | Disponible para Campaigns, Canvas, Campaigns y Canvas. Solo se muestra para campañas programadas; no se completa para campañas basadas en acciones o desencadenadas por API. |
| Envíos | Disponibles para cada canal relevante. |
| Mensajes enviados | Disponibles para Campaigns, Canvas, Campaigns y Canvas, etiquetas. |
| Línea del asunto | Disponible para Campaigns de correo electrónico con desglose por **Variant**, Canvas y Canvas con desglose por **Variant**. |
| Ingresos totales | Disponibles para Campaigns, Canvas, Campaigns y Canvas, etiquetas. No disponible con desglose por **Channels**. |
| Impresiones únicas | Disponibles para Campaigns, Canvas, Campaigns y Canvas, etiquetas. |
| Destinatarios únicos | Disponibles para Campaigns, Canvas, Campaigns y Canvas, etiquetas. No disponible con desglose por **Channels**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disponibilidad de métricas" }

### Variantes de mensaje eliminadas {#deleted-message-variants}

Las estadísticas de variantes de mensaje eliminadas no se muestran cuando desglosas tu informe por campañas o Canvas. Sin embargo, los totales a nivel de canal incluyen todas las estadísticas independientemente de si la variante fue eliminada. Por ejemplo, _Envíos_ para correo electrónico incluye todos los envíos de correo electrónico, pero si desglosas esas estadísticas por campaña, los números pueden ser menores porque los envíos de variantes de mensaje eliminadas se filtran.

En el mismo informe, _Destinatarios únicos_ puede ser mayor que _Impresiones únicas_ cuando una variante de mensaje fue eliminada después del envío. Los _Destinatarios únicos_ a nivel de campaña aún pueden incluir usuarios que recibieron la variante eliminada, mientras que las _Impresiones únicas_ omiten las estadísticas de variantes eliminadas en las agregaciones a nivel de mensaje.

## Ver un informe {#viewing-a-report}

Después de ejecutar tu informe, puedes ver los resultados en formato de tabla en la página del informe.

![Una tabla con los datos del informe para las métricas de cada campaña.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### Crear un gráfico del informe {#creating-a-report-chart}

En la parte inferior de la página puedes crear un gráfico de tus datos seleccionando un **Chart type** y configurando las métricas del gráfico. De forma predeterminada, verás la primera métrica.

![Un gráfico de los datos del informe con opciones para configurar el eje x, el eje y, el tipo de gráfico y más.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
Para crear un gráfico de líneas, selecciona **Date** como opción de desglose al configurar el informe. Esto mostrará tendencias a lo largo del tiempo.
{% endalert %}

#### Descargar un gráfico del informe {#downloading-a-report-chart}

Para descargar una imagen del gráfico del informe, selecciona el icono de puntos y luego elige una opción de descarga.

![Un menú con opciones de descarga para diferentes formatos de archivo.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## Compartir un informe {#sharing-a-report}

Puedes compartir un enlace del panel al informe seleccionando **Share** y una de estas opciones:
- **Compartir un enlace:** Copia y comparte el enlace.

![Desplegable "Compartir un enlace" con un enlace al informe.]({% image_buster /assets/img/report_builder_2/share_this_report.png %}){: style="max-width:70%;"}

- **Enviar o programar un correo electrónico:** Envía un correo electrónico de inmediato o en un momento designado que contenga un enlace de descarga que caduca después de una hora. Puedes seleccionar destinatarios de los usuarios de la empresa listados en el desplegable **Email Recipients** o introducir cualquier otra dirección de correo electrónico.

![Ventana "Programar un correo electrónico" con campos para elegir el formato del informe, quién debe recibirlo y cuándo debe enviarse.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **Descargar CSV:** Descarga un CSV del informe.

## Añadir un informe a un panel {#adding-a-report-to-a-dashboard}

1. Selecciona el icono de puntos en la parte superior de la tabla del informe.
2. Selecciona **Add to dashboard**.
3. Selecciona si deseas crear un nuevo panel o añadirlo a un panel existente.<br><br>![Ventana con opciones para seleccionar si deseas añadir el informe a un panel nuevo o existente.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. Sigue los pasos en [Generador de paneles]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder) para aprender más sobre cómo construir un panel.

## Solución de problemas {#troubleshooting}

### El informe no muestra envíos para una campaña o Canvas {#report-shows-no-sends-for-a-campaign-or-canvas}

Una campaña o Canvas aparece en el informe cuando su fecha de **Last sent** se encuentra dentro de la ventana de **Last sent** que configuraste. **Envíos** y otras métricas solo se completan para la actividad dentro del rango de fechas de **Show data for**. Si el mensaje no se envió durante **Show data for**, la fila puede seguir mostrando la campaña o Canvas con cero envíos.

Por ejemplo, supongamos que **Last sent** es del 1 de enero de 2025 al 14 de abril de 2025, por lo que se incluye una campaña, pero **Show data for** es del 1 de diciembre de 2024 al 14 de enero de 2025. Si esa campaña no tuvo envíos en diciembre o enero, seguirá apareciendo en la tabla sin métricas de envío.

### El enlace de descarga ha caducado {#download-link-has-expired}

Los enlaces de descarga de informes caducan después de una hora. Si tu enlace ha caducado, genera un nuevo informe y descárgalo dentro de la hora. No hay forma de extender el tiempo de caducidad.

Si tienes un [contenedor de Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3) conectado en **Partner Integrations**, es posible que puedas recuperar datos de informes anteriores navegando directamente por tu contenedor de S3.