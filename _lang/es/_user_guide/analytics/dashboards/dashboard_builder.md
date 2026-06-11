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

El Generador de dashboards te permite redactar y visualizar dashboards de análisis personalizados desde cero y a partir de dashboards proporcionados por Braze. Puedes usar un origen de datos sin código (Generador de informes) o un origen de datos SQL (Generador de consultas) para alimentar tu dashboard, o empezar a partir de uno de los muchos dashboards proporcionados por Braze.

## Crear un dashboard personalizado {#creating-a-custom-dashboard}

1. Ve a **Analytics** > **Dashboard Builder**.
2. Selecciona **Create Dashboard**.
3. Selecciona qué origen de datos alimentará tus informes:
- **Reports** que se crearon en el Generador de informes
- **Custom Queries** que se crearon en el Generador de consultas<br><br>![Ventana para seleccionar tu origen de datos para tu dashboard.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Ahora, sigue los pasos correspondientes a tu origen de datos:

{% tabs %}
{% tab Reports %}

{: start="4"}
4. Selecciona **+ Add Tile** y luego elige uno de los informes que creaste en el [Generador de informes (nuevo)]({{site.baseurl}}/user_guide/analytics/reports/report_builder/).

{% alert important %}
Después de añadir un informe del Generador de informes a un mosaico del Generador de dashboards, el mosaico no está conectado al informe original. Si editas el informe original en el Generador de informes, debes eliminar el mosaico existente del dashboard y crear uno nuevo usando el informe actualizado como origen de datos.
{% endalert %}

{: start="5"}
5. Selecciona el icono de lápiz para cambiar cómo se muestran el título y el tipo de gráfico en el mosaico.
    - Puedes alternar entre diferentes tipos de gráficos debajo de la visualización predeterminada. Las opciones actuales incluyen gráficos de barras (horizontales o verticales) y gráficos de líneas (solo disponibles si seleccionaste **Date** como opción de desglose en la configuración del Generador de informes).<br><br>![Opciones para alternar entre diferentes tipos de gráficos.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    - Usa el menú desplegable de métricas para seleccionar qué métricas incluir en tu visualización. De forma predeterminada, la primera columna del informe será la métrica mostrada por defecto.
6. Selecciona **Save** después de haber cambiado la visualización a tu gusto.
7. Añade un nombre, una descripción y una etiqueta para que tu dashboard sea más fácil de encontrar después.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4. Selecciona **+ Add Tile** y luego elige una consulta que hayas ejecutado en el Generador de consultas.
5. Para editar cómo se muestran los resultados de la consulta en el mosaico, selecciona el icono de lápiz para cambiar el título y el tipo de gráfico.
    - Puedes alternar entre diferentes tipos de gráficos debajo de la visualización predeterminada. Las opciones actuales incluyen tablas, gráficos de barras (horizontales o verticales) y gráficos de líneas.<br><br>![Opciones para alternar entre diferentes tipos de gráficos.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        - Si eliges una de las opciones de gráfico, usa el menú desplegable **X-axis** para seleccionar una sola columna de los resultados de tu consulta para usarla como eje X.
        - Usa el menú desplegable **Y-axis** para seleccionar qué métricas incluir en tu visualización. De forma predeterminada, se mostrarán todas las columnas de los resultados de tu consulta, así que deselecciona las columnas que no te interese ver.<br><br>![Opciones para alternar entre diferentes tipos de gráficos.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        - (Opcional) Puedes usar el menú desplegable **Grouping** para agrupar los resultados de tu consulta. Por ejemplo, si tienes el ID de Campaign como resultado de columna y quieres sumar todas las filas con ese valor, usa el menú desplegable **Grouping**.
        - (Opcional) Para editar los datos que se muestran, selecciona la consulta que está vinculada al visual y haz tus ediciones en el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/).
6. Selecciona **Save** después de haber cambiado la visualización a tu gusto.
7. Añade un nombre, una descripción y una etiqueta para que tu dashboard sea más fácil de encontrar después.
{% endtab %}
{% endtabs %}

{: start="8"}
8. Repite los pasos 4 a 7 para tu método correspondiente hasta que crees el dashboard deseado.
9. Selecciona **View Dashboard** > selecciona **Run Dashboard**.

Tu dashboard puede tardar unos minutos en terminar de generar los informes.

{% alert note %}
Puedes añadir hasta 10 mosaicos a un dashboard.
{% endalert %}

## Administrar mosaicos del dashboard {#managing-dashboard-tiles}

### Eliminar mosaicos {#delete-tiles}

Elimina un mosaico del dashboard seleccionando **Delete Tile** en la parte inferior del mosaico. **Esta acción no se puede revertir.**

### Duplicar mosaicos {#duplicate-tiles}

Haz una copia de tu mosaico seleccionando **Duplicate Tile** en la parte inferior del mosaico.

### Ajustar el tamaño y la posición de los mosaicos {#adjust-tile-size-and-position}

Ajusta el tamaño del mosaico arrastrando la esquina inferior derecha del mosaico, y ajusta la posición del mosaico en el dashboard arrastrando el asa en la esquina superior derecha del mosaico.

## Ejecutar un dashboard {#running-a-dashboard}

1. Ve a **Analytics** > **Dashboard Builder**. La página de inicio muestra todos los dashboards existentes dentro de tu espacio de trabajo, con los dashboards creados por Braze en la parte superior. Estos se identifican con "(Braze)" en el título.
2. Selecciona el dashboard que te interese.
3. Selecciona **Run Dashboard** para cargar el dashboard correspondiente.

### Dashboards disponibles {#available-dashboards}

Braze proporciona dashboards preconstruidos para casos de uso frecuentes, como el análisis de ingresos usando atribución de último toque. Ten en cuenta que la capacidad de editar un dashboard aún no está disponible. Ponte en contacto con tu administrador del éxito del cliente si te gustaría ver cierto dashboard en el futuro.

#### Ingresos - Atribución de último toque {#revenue-last-touch-attribution}

El dashboard **Revenue - Last Touch Attribution** proporciona una revisión de los ingresos a través de Campaigns, Canvas y canales. Todos los datos de ingresos se atribuyen al último mensaje con el que se interactuó durante la ventana de atribución.

Los toques incluyen _clic en correo electrónico_ (clic en enlace), _clic en tarjeta de contenido_, _clic en mensaje dentro de la aplicación_ (excluyendo botones de cierre), _aperturas de push_, _clic en enlace corto de SMS_, _lectura de WhatsApp_ y _envío de webhook_.

| Métrica | Definición |
| --- | --- |
| Ingresos totales de último toque | Suma de todos los eventos de ingresos de Campaigns y Canvas con un evento de último toque dentro del rango de fechas y la ventana de atribución seleccionados. |
| Conversiones de compra totales | Recuento de todos los eventos de ingresos de Campaigns y Canvas con un evento de último toque que cumple los requisitos. |
| Promedio de días para convertir | El tiempo promedio entre todos los eventos de compra de Campaigns y Canvas con un evento de último toque que cumple los requisitos. |
| Ingresos por destinatario | Suma de los ingresos de eventos de ingresos que cumplen los requisitos dividida por el número de usuarios únicos que recibieron un mensaje dentro del rango de fechas. |
| Compradores únicos | Recuento de los usuarios únicos con un evento de ingresos que cumple los requisitos. |
| Ingresos por país | Suma de todos los eventos de ingresos de Campaigns y Canvas con un evento de último toque, agrupados por país. |
| Ingresos por Campaign | Suma de todos los eventos de ingresos de Campaigns y Canvas con un evento de último toque que cumple los requisitos, agrupados por Campaign. |
| Ingresos por variante de campaña | Suma de todos los eventos de ingresos de Campaigns y Canvas con un evento de último toque que cumple los requisitos, agrupados por variante de campaña. |
| Ingresos por Canvas | Suma de todos los eventos de ingresos de Campaigns y Canvas con un evento de último toque que cumple los requisitos, agrupados por Canvas. |
| Ingresos por variante en Canvas | Suma de todos los eventos de ingresos de Campaigns y Canvas con un evento de último toque que cumple los requisitos, agrupados por variante en Canvas. |
| Compras por producto | Recuento de todas las compras agrupadas por producto. |
| Ingresos por canal | Suma de todos los eventos de ingresos de Campaigns y Canvas con un evento de último toque que cumple los requisitos, agrupados por canal. |
| Serie temporal de ingresos | Suma de todos los eventos de ingresos de Campaigns y Canvas con un evento de último toque que cumple los requisitos, agrupados por día en UTC. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Revenue - Last Touch Attribution" }

#### Dispositivos y operadores {#devices-and-carriers}

| Métrica | Definición |
| --- | --- |
| Operadores de dispositivos | Recuento de usuarios en el rango de fechas seleccionado que abrieron una notificación push, agrupados por operador del dispositivo. |
| Modelo de dispositivo | Recuento de usuarios en el rango de fechas seleccionado que abrieron una notificación push, agrupados por modelo de dispositivo. |
| Sistema operativo del dispositivo | Recuento de usuarios en el rango de fechas seleccionado que abrieron una notificación push, agrupados por sistema operativo del dispositivo. |
| Tamaño de pantalla del dispositivo | Recuento de usuarios en el rango de fechas seleccionado que abrieron una notificación push, agrupados por resolución de pantalla (tamaño) del dispositivo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Devices and carriers" }

#### Información del segmento - Correo electrónico {#segment-insights-email}

| Métrica  | Definición  |
|---|---|
| Métricas semanales de correo electrónico (tasas) | Tasas de interacción de correo electrónico (entrega, rebote, apertura, clic, tasas de cancelación de suscripción) agrupadas por segmento y mostradas como serie temporal semanal.|
| Métricas semanales de correo electrónico (recuentos) | Recuentos de interacción de correo electrónico (enviados, entregados, rebotes, aperturas, clics, cancelaciones de suscripción) agrupados por segmento y mostrados como serie temporal semanal.|
| Métricas semanales de compras (tasas) | Tasas de conversión de compras (ingresos por destinatario) a partir de aperturas y clics de correo electrónico, agrupadas por segmento y mostradas como serie temporal semanal.|
| Métricas semanales de compras (recuentos) | Recuentos de compras y totales de ingresos a partir de aperturas y clics de correo electrónico, agrupados por segmento y mostrados como serie temporal semanal.|
| Interacción de correo electrónico por segmento | Tabla resumen que muestra las métricas totales de interacción de correo electrónico (enviados, entregados, rebotes, aperturas, clics, cancelaciones de suscripción y sus tasas) agregadas por segmento.|
| Compras e ingresos por segmento | Tabla resumen que muestra las métricas totales de compras (compras, ingresos e ingresos por destinatario) a partir de aperturas y clics de correo electrónico, agregadas por segmento.|
| Top 10 de Campaigns por métricas de interacción | Lista clasificada de las Campaigns con las métricas de interacción de correo electrónico más altas (métrica configurable para la clasificación).|
| 10 Campaigns con menor interacción | Lista clasificada de las Campaigns con las métricas de interacción de correo electrónico más bajas (métrica configurable para la clasificación).|
| Top 10 de Canvas por métricas de interacción | Lista clasificada de los Canvas con las métricas de interacción de correo electrónico más altas (métrica configurable para la clasificación).|
| 10 Canvas con menor interacción | Lista clasificada de los Canvas con las métricas de interacción de correo electrónico más bajas (métrica configurable para la clasificación).|
| Top 10 de Campaigns por métricas de compras | Lista clasificada de las Campaigns con las métricas de conversión de compras más altas a partir de la interacción de correo electrónico (métrica configurable para la clasificación).|
| 10 Campaigns con menores métricas de compras | Lista clasificada de las Campaigns con las métricas de conversión de compras más bajas a partir de la interacción de correo electrónico (métrica configurable para la clasificación).|
| Top 10 de Canvas por métricas de compras | Lista clasificada de los Canvas con las métricas de conversión de compras más altas a partir de la interacción de correo electrónico (métrica configurable para la clasificación).|
| 10 Canvas con menores métricas de compras | Lista clasificada de los Canvas con las métricas de conversión de compras más bajas a partir de la interacción de correo electrónico (métrica configurable para la clasificación).|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment Insights - Email" }

#### Análisis de sesiones {#session-analytics}

| Métrica | Definición  |
|---|---|
| N.º de sesiones por día (serie temporal) | Recuento de sesiones únicas agrupadas por día dentro del rango de fechas seleccionado, mostrado como serie temporal.|
| Promedio de sesiones por usuario | Número promedio de sesiones por usuario calculado como el total de sesiones dividido por usuarios únicos dentro del rango de fechas seleccionado.|
| Campaigns que convierten a sesiones | Recuento de sesiones únicas que ocurrieron al mismo tiempo que las conversiones de Campaigns, agrupadas por ID de Campaign y clasificadas por recuento de sesiones.|
| Canvas que convierten a sesiones | Recuento de sesiones únicas que ocurrieron al mismo tiempo que las conversiones de Canvas, agrupadas por ID de Canvas y clasificadas por recuento de sesiones.|
| N.º total de sesiones por usuario | Lista de los 1000 usuarios principales por su recuento total de sesiones dentro del rango de fechas seleccionado.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Session Analytics" }

## Comparte tus comentarios con nosotros {#share-your-feedback-with-us}

Selecciona el botón **Enviar comentarios** o ponte en contacto con tu administrador del éxito del cliente para compartir tus comentarios con nosotros.