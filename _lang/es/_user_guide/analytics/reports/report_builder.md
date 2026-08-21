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

## Uso de una plantilla de informe {#using-a-report-template}

1. Ve a **Analytics** > **Generador de informes (nuevo)**.
2. Selecciona la flecha de **Más opciones** junto al botón **Crear informe nuevo** y, a continuación, selecciona **Usar una plantilla de informe**.<br><br>![Desplegable del botón "Crear informe nuevo" con opciones para crear un informe personalizado o usar una plantilla.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Selecciona una de las plantillas de informe de la biblioteca de plantillas de Braze.
    - Usa los desplegables **Elementos de fila** y **Etiquetas** para encontrar informes relevantes para tus ejemplos.<br><br>![Ventana "Plantillas de informe de Braze" con una lista de plantillas de Braze para seleccionar.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. Sigue desde el paso 3 en adelante en [Creación de un informe](#creating-a-report) para personalizar aún más el informe y adaptarlo a tu caso de uso.

## Crear un informe {#creating-a-report}

1. Ve a **Analytics** > **Generador de informes (nuevo)**.
2. Selecciona **Crear informe nuevo**.
3. En el desplegable **Filas**, selecciona sobre qué te gustaría generar el informe:
    - Campaigns
    - Canvas
    - Campaigns y Canvas
    - Canales
    - Etiquetas

    Ten en cuenta que tu selección de **Filas** afecta a [las métricas que puedes ver](#metrics-availability). Por ejemplo, puedes ver métricas multivariantes solo si generas un informe sobre **Canvas** o **Campaigns** con un desglose por **Variante**. No puedes ver esas métricas cuando generas un informe sobre **Campaigns y Canvas**, aunque esas Campaigns y Canvas tengan pruebas multivariantes.

![La sección "Filas y columnas" con campos para seleccionar las filas y agrupaciones de tu informe.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4. (Opcional) Selecciona **Añadir desglose** para dividir tus datos en vistas más detalladas:
    - Canales
    - Fecha
        - Usa esta opción para dividir tus datos en intervalos de tiempo más pequeños. Por ejemplo, si te interesa saber cómo rindieron tus Campaigns por día, selecciona la siguiente configuración:
            - **Filas**: Campaigns
            - **Agrupación:** Fecha
            - **Intervalo:** Días
    - Variantes
    - Campaigns y Canvas

{% alert tip %}
Prueba diferentes configuraciones de opciones de desglose para explorar las [muchas formas en que puedes dividir tus datos](#metrics-availability).
{% endalert %}

{: start="5"}
5. En la sección **Columnas**, selecciona **Personalizar métricas**.

![La sección "Personalizar métricas" con opciones para seleccionar múltiples métricas.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6. Explora las métricas por categoría y selecciona la casilla correspondiente para añadir una métrica a tu informe.
    - Reordena las métricas y columnas arrastrando el icono de puntos hacia arriba o hacia abajo.
7. En **Contenido del informe**, configura el intervalo de fechas para el que deseas incluir datos en tu informe.
8. Luego, dependiendo de tus selecciones en el paso 3, elige añadir Campaigns, Canvas o ambos a tu informe de forma manual o automática.
    - **Añadir manualmente:** Elige cada Campaign o Canvas que deseas incluir en el informe usando los filtros de fechas de **Último envío** y etiquetas o canales, o buscando el nombre de la Campaign o Canvas.<br><br>![La sección "Añadir manualmente Campaigns y Canvas" con una lista de Campaigns para seleccionar.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **Añadir automáticamente:** Establece reglas para determinar qué Campaigns o Canvas incluir en el informe. Solo es necesario que selecciones un campo en esta página.
        - Ten en cuenta que a medida que Campaigns o Canvas adicionales cumplan las condiciones que establezcas en esta pantalla, se añadirán automáticamente a futuras ejecuciones de tu informe.
        - Banners no es una opción en el desplegable **Canal**, por lo que no puedes usar reglas de canal para añadir automáticamente Campaigns o Canvas de Banner. Aun así, puedes incluir KPI de Banner en las métricas de tu informe.<br><br>![La sección "Añadir automáticamente Campaigns y Canvas" con campos para establecer reglas sobre qué Campaigns y Canvas deben añadirse al informe.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9. Ejecuta el informe seleccionando **Guardar y ejecutar**.

{% alert note %}
El informe puede tardar unos minutos en ejecutarse, dependiendo del intervalo de fechas y la cantidad de Campaigns o Canvas que hayas seleccionado en la etapa de configuración.
{% endalert %}

## Disponibilidad de métricas {#metrics-availability}

Tu selección de **Filas** afecta las métricas que puedes seleccionar.

{% alert tip %}
Si deseas generar informes sobre variantes o pasos de Canvas, selecciona **Canvas** para las filas y deja el campo vacío o selecciona **Fecha** como desglose. Después de ejecutar el informe, aparece un desplegable **Vista de Canvas** en la página de resultados para ver las métricas solo del Canvas, o agrupar las métricas por variante, paso o mensaje.<br><br> Al editar tu informe, la tabla de vista previa muestra un máximo de 50 filas. Ejecuta el informe para ver todas las filas en la página de resultados con paginación (100 filas por página) o exporta el conjunto de datos completo como CSV.

![El desplegable "Vista de Canvas" abierto.]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Métrica | Descripción |
| --- | --- |
| Métricas de conversión | Disponible para Campaigns, Canvas, Campaigns y Canvas. |
| Entradas | Disponible para Campaigns, Canvas, Campaigns y Canvas, etiquetas. |
| Fecha del último envío | Disponible para Campaigns, Canvas, Campaigns y Canvas. Solo se muestra para campañas programadas; no se completa para campañas basadas en acciones o activadas por API. |
| Envíos | Disponible para cada canal relevante. |
| Mensajes enviados | Disponible para Campaigns, Canvas, Campaigns y Canvas, etiquetas. |
| Línea del asunto | Disponible para Campaigns de correo electrónico con desglose por **Variante**, Canvas y Canvas con desglose por **Variante**. |
| Ingresos totales | Disponible para Campaigns, Canvas, Campaigns y Canvas, etiquetas. No disponible con desglose por **Canales**. |
| Impresiones únicas | Disponible para Campaigns, Canvas, Campaigns y Canvas, etiquetas. |
| Destinatarios únicos | Disponible para Campaigns, Canvas, Campaigns y Canvas, etiquetas. No disponible con desglose por **Canales**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disponibilidad de métricas" }

### Variantes de mensaje eliminadas {#deleted-message-variants}

Las estadísticas de las variantes de mensaje eliminadas no se muestran cuando desglosas tu informe por campañas o Canvas. Sin embargo, los totales a nivel de canal incluyen todas las estadísticas independientemente de si la variante fue eliminada. Por ejemplo, los _Envíos_ de correo electrónico incluyen todos los envíos de correo electrónico, pero si desglosas esas estadísticas por campaña, los números pueden ser menores porque los envíos de las variantes de mensaje eliminadas se filtran.

En el mismo informe, los _Destinatarios únicos_ pueden ser mayores que las _Impresiones únicas_ cuando una variante de mensaje fue eliminada después del envío. Los _Destinatarios únicos_ a nivel de campaña aún pueden incluir usuarios que recibieron la variante eliminada, mientras que las _Impresiones únicas_ omiten las estadísticas de las variantes eliminadas en las agregaciones a nivel de mensaje.

## Visualización de un informe {#viewing-a-report}

Después de ejecutar tu informe, puedes ver los resultados en formato de tabla en la página de resultados del informe.

![Una tabla con los datos del informe para las métricas de cada Campaign.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### Creación de un gráfico del informe {#creating-a-report-chart}

En la parte inferior de la página, puedes crear un gráfico de tus datos seleccionando un **Tipo de gráfico** y configurando las métricas del gráfico. De forma predeterminada, verás la primera métrica.

![Un gráfico de los datos del informe con opciones para configurar el eje X, el eje Y, el tipo de gráfico y más.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
Para crear un gráfico de líneas, selecciona **Date** como opción de desglose al configurar el informe. Esto muestra las tendencias a lo largo del tiempo.
{% endalert %}

#### Descarga de un gráfico del informe {#downloading-a-report-chart}

Para descargar una imagen del gráfico del informe, selecciona el icono de puntos y luego elige una opción de descarga.

![Un menú con opciones de descarga para diferentes formatos de archivo.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## Compartir un informe {#sharing-a-report}

Puedes compartir un enlace del panel al informe seleccionando **Compartir** y una de estas opciones:
- **Compartir un enlace:** Copia y comparte el enlace.
- **Enviar o programar un correo electrónico:** Envía un correo electrónico de inmediato o a una hora designada que contenga un enlace de descarga que caduca después de una hora. Puedes seleccionar destinatarios de los usuarios de la empresa que aparecen en el desplegable **Email Recipients** o introducir cualquier otra dirección de correo electrónico.

{% alert note %}
El desplegable **Email Recipients** solo muestra usuarios de la empresa en Braze y guarda sus direcciones de correo electrónico en las programaciones de informes. Las direcciones de correo electrónico externas deben introducirse manualmente cada vez que crees una nueva programación de informe. Si envías informes con frecuencia a destinatarios externos, como un contacto de un partner, considera añadirlos como usuario de la empresa con los permisos adecuados para que su dirección aparezca en el desplegable.
{% endalert %}

![Ventana "Programar un correo electrónico" con campos para elegir el formato del informe, quién debe recibirlo y cuándo debe enviarse.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **Descargar CSV:** Descarga un CSV del informe.

## Añadir un informe a un panel {#adding-a-report-to-a-dashboard}

1. Selecciona el icono de puntos en la parte superior de la tabla del informe.
2. Selecciona **Añadir al panel**.
3. Selecciona si deseas crear un panel nuevo o añadirlo a un panel existente.<br><br>![Ventana con opciones para seleccionar si deseas añadir el informe a un panel nuevo o existente.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. Sigue los pasos en [Generador de paneles]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder) para obtener más información sobre cómo crear un panel.

## Permisos de equipo {#team-permissions}

Los informes del generador de informes no admiten la [asignación de equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) como las Campaigns o los Canvas. No puedes limitar un informe guardado a un equipo específico cuando lo creas.

Los usuarios con permiso ["Ver informes del panel"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) a nivel de equipo (en lugar de a nivel de espacio de trabajo) pueden seguir usando el generador de informes, pero la visibilidad de los informes es limitada:

- Estos usuarios solo ven informes en los que cada Campaign y Canvas seleccionado está asignado a sus equipos.
- Los informes con **Canales** como filas están ocultos.
- Los informes que usan la selección automática para añadir Campaigns o Canvas están ocultos, porque Braze no puede verificar el acceso del equipo para los mensajes que podrían añadirse cuando se ejecuta el informe.

El [Generador de informes (heredado)]({{site.baseurl}}/report_builder_legacy) limita por equipo qué Campaigns y Canvas puedes añadir a un informe, pero los informes guardados no se filtran de la lista de la misma manera que en el generador de informes (nuevo). Para la configuración de permisos, consulta [Configuración de permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) y [Equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams).

## Solución de problemas {#troubleshooting}

### El informe no muestra envíos para una Campaign o Canvas {#report-shows-no-sends-for-a-campaign-or-canvas}

Una Campaign o Canvas aparece en el informe cuando su fecha de **Último envío** se encuentra dentro de la ventana de **Último envío** que configuraste. Los **Envíos** y otras métricas solo se completan para la actividad dentro del rango de fechas de **Mostrar datos para**. Si el mensaje no se envió durante **Mostrar datos para**, la fila puede seguir mostrando la Campaign o Canvas con cero envíos.

Por ejemplo, supongamos que **Último envío** es del 1 de enero de 2025 al 14 de abril de 2025, por lo que se incluye una Campaign, pero **Mostrar datos para** es del 1 de diciembre de 2024 al 14 de enero de 2025. Si esa Campaign no tuvo envíos en diciembre o enero, seguirá apareciendo en la tabla sin métricas de envío.

### El enlace de descarga ha caducado {#download-link-has-expired}

Los enlaces de descarga de informes caducan después de una hora. Si tu enlace ha caducado, genera un nuevo informe y descárgalo dentro de la hora. No hay forma de extender el tiempo de caducidad.

Si tienes un [contenedor de Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3) conectado en **Integraciones de partners**, es posible que puedas recuperar datos de informes anteriores navegando directamente por tu contenedor de S3.