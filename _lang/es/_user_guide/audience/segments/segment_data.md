---
nav_title: Datos de Segment
article_title: Datos de Segment
page_order: 4
page_type: reference
description: "Esta página explica la sección de Segments de tu panel de Braze e incluye un resumen de las estadísticas proporcionadas."
alias: /viewing_and_understanding_segment_data/
tool:
  - Segments
  - Reports

---
# Datos de Segment {#segment-data}

> Esta página explica la sección de Segments de tu panel de Braze e incluye un resumen de las estadísticas proporcionadas.

## Acceder a los datos de tus Segments y membresía {#accessing-data-about-your-segments-and-membership}

La página **Segments** de tu panel de Braze contiene un resumen de todos tus Segments y te permite examinar datos detallados de cada uno. En esta página, busca y selecciona el nombre de un Segment para editarlo y ver sus datos. Para aprender a crear un Segment, consulta [Crear un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#creating-a-segment).

![Página de Segments]({% image_buster /assets/img_archive/segments.png %})

Después de seleccionar el nombre de un Segment, puedes ver las estadísticas y filtros del Segment, y editarlo añadiendo o eliminando filtros. ¡Asegúrate de guardar cualquier cambio!

Cuando activas el [seguimiento de análisis para un Segment]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/), puedes ver sesiones, eventos personalizados e ingresos a lo largo del tiempo para este Segment.

![Alternancia de seguimiento de análisis para un Segment]({% image_buster /assets/img_archive/A_Tracking_2.png %})

### Estadísticas de Segment {#segment-statistics}

Puedes ver las siguientes estadísticas de Segment, que se actualizan en tiempo real a medida que añades o eliminas filtros:

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Estadísticas de Segment">
  <caption>Estadísticas de Segment</caption>
    <thead>
        <tr>
            <th>Estadística</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Usuarios totales</td>
            <td class="no-split">Cuántos usuarios tiene tu aplicación en total.</td>
        </tr>
        <tr>
            <td class="no-split">Usuarios seleccionados</td>
            <td class="no-split">Cuántos usuarios hay en tu Segment y qué porcentaje de tu base de usuarios total representan.</td>
        </tr>
        <tr>
            <td class="no-split">LTV (usuarios de pago)</td>
            <td class="no-split">El valor de duración del ciclo de vida por usuario (LTV) en este Segment y el valor de duración del ciclo de vida por usuario de pago en este Segment. El LTV se calcula dividiendo tus ingresos de duración del ciclo de vida entre los usuarios de duración del ciclo de vida.</td>
        </tr>
        <tr>
            <td class="no-split">Contactable por correo electrónico (adhesión voluntaria)</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Emailable' %} Debido a las <a href="/docs/help/best_practices/spam_regulations/#spam-regulationsspam regulations">regulaciones de correo no deseado</a>, es una buena idea pedir a tus usuarios que opten explícitamente por la adhesión voluntaria implementando una política de doble adhesión voluntaria en la que los usuarios deben hacer clic en un enlace en un correo electrónico de confirmación inicial. Para animar a más usuarios a optar por la adhesión voluntaria, puedes dirigir un mensaje a <a href="/docs/user_guide/channels/email/subscriptions#segmenting-by-user-subscriptions">aquellos que no han optado ni por la adhesión ni por la exclusión</a>.</td>
        </tr>
        <tr>
            <td class="no-split">Push habilitado (adhesión voluntaria)</td>
            <td class="no-split">Push habilitado se refiere al número de usuarios con al menos un token de notificaciones push. Algunos usuarios pueden tener múltiples tokens de notificaciones push (por ejemplo, si tienen un iPhone y un iPad), por lo que el número de notificaciones push que envíes a este Segment puede ser mayor que el número de usuarios con "push habilitado". "Adhesión voluntaria" se refiere al número de usuarios que han optado explícitamente por recibir notificaciones push. Los usuarios siempre deben optar explícitamente por la adhesión voluntaria para que puedas enviarles notificaciones push.</td>
        </tr>
    </tbody>
</table>

### Información del segmento {#segment-insights}

Puedes ver cómo se desempeña un Segment en comparación con otro a través de un conjunto de KPI preseleccionados visitando la página [Información del segmento]({{site.baseurl}}/user_guide/audience/segments/segment_insights/) de tu dashboard.

### Uso de mensajería {#messaging-use}
La sección **Messaging Use** muestra qué Segments, Campaigns actualmente habilitadas y Canvas actualmente habilitados están dirigidos a tu Segment.

### Membresía histórica {#historical-membership}

La sección **Historical Membership** muestra cómo cambió el tamaño de tu Segment a lo largo del tiempo. Usa el menú desplegable para filtrar la membresía del Segment por rango de fechas.

Para obtener más información sobre cómo monitorear la membresía y el tamaño de tu Segment, consulta [Medir el tamaño del Segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size/).

### Vista previa de usuario {#user-preview}

Para ver información detallada y específica del usuario sobre tus Segments, haz clic en **User Data** y selecciona **User Preview**.

En esta página, puedes ver una serie de atributos específicos del usuario, como género, edad, número de sesiones y si han optado por la adhesión voluntaria a push y correo electrónico.

Ten en cuenta que en los casos en que tu Segment sea muy pequeño en relación con el tamaño de tu espacio de trabajo, es posible que la vista previa de usuario devuelva cero usuarios. Esto no significa necesariamente que haya cero usuarios en tu Segment; ejecuta [Calculate Exact Stats]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size/#statistics-for-segment-size) para determinar el tamaño exacto de tu Segment.

![Vista previa de usuario]({% image_buster /assets/img_archive/user_preview.png %})

## Ver datos de rendimiento por Segment {#viewing-performance-data-by-segment}

Usa las [plantillas de informes del Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/data_by_segments/) para desglosar las métricas de rendimiento de Campaigns, Canvas, variantes y pasos por Segments.

## Crear un informe de desglose por Segment usando el Generador de consultas {#creating-a-segment-breakdown-report-using-query-builder}

Para crear un informe a partir de una plantilla del [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/), ve a **Query Builder** y haz lo siguiente:

1. Selecciona **Create SQL Query** > **Query Template**.
2. Filtra las plantillas por aquellas que tengan métricas que incluyan "segment breakdowns".
3. Selecciona la plantilla que deseas usar.
4. Completa las variables en tu plantilla SQL en la pestaña [Variables](#variables).
5. (Opcional) Edita directamente el SQL en la plantilla.
6. Selecciona **Run Query**. Tus resultados se mostrarán en una tabla.

## Variables {#variables}

Antes de generar tu informe, ve a la pestaña **Variables** para proporcionar información para la plantilla del Generador de informes, incluidas las variables obligatorias que variarán según el informe.

Las variables incluyen:

- **Campaña o Canvas:** puedes incluir una o varias campañas o Canvas (no hay un máximo para cuántas campañas o Canvas puedes especificar). Si no especificas ninguna campaña o Canvas, el informe incluirá todas las campañas o Canvas de tu período de tiempo elegido.
- **Variante:** si usas una plantilla que ofrece desgloses a nivel de variante, después de seleccionar una campaña o Canvas, puedes seleccionar variantes dentro de esa campaña o Canvas. Si seleccionas múltiples variantes, tus resultados se agruparán por variante.
- **Paso:** si seleccionas una variante en Canvas, puedes seleccionar un paso en Canvas. No puedes seleccionar un paso sin antes seleccionar una variante en Canvas.
- **Rango de tiempo:** identifica el período de tiempo del que deseas extraer datos. Si no se especifica un rango de tiempo, el rango de tiempo será por defecto los últimos 30 días.
- **Nombre del producto:** si ejecutas un informe para datos de compras, puedes identificar un producto específico del que extraer datos.
- **Ventana de conversión:** siempre obligatoria para informes con datos de ingresos y compras. El número de días después de la recepción o clic del correo electrónico en los que Braze debe atribuir compras o ingresos.
- **Segments:** identifica los Segments por los que deseas desglosar los datos. Si no se especifica, el informe se ejecutará para todos los Segments que tengan activado el seguimiento de análisis.
- **Etiquetas:** especifica etiquetas en **Variables** para ejecutar tu informe para todas las campañas o Canvas con ciertas etiquetas. Puedes incluir múltiples etiquetas. Si añades tanto etiquetas como campañas o Canvas específicos a un informe, tu informe incluirá datos de tus etiquetas y las campañas o Canvas especificados.

## Disponibilidad de datos {#data-availability}

Los datos están disponibles para períodos de tiempo en los que se cumplen ambas condiciones:

1. El [seguimiento de análisis de Segment]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) está activado para los Segments de los que deseas ver datos.
2. La función de datos de rendimiento por Segment está activada.

No puedes acceder a datos de períodos de tiempo anteriores a cuando esta función se activó para tu empresa. Por ejemplo, si el seguimiento de análisis se activa para el Segment A el 1 de octubre y esta función se activa para tu empresa el 2 de octubre, entonces solo puedes ver datos del Segment A para las campañas y Canvas que registraron métricas después del 2 de octubre.

Si tu empresa activó esta función el 2 de octubre y activó el seguimiento de análisis para el Segment B el 3 de octubre, entonces solo puedes ver datos del Segment B para las campañas y Canvas que registraron métricas después del 3 de octubre.