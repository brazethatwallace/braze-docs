---
nav_title: Eventos personalizados
article_title: Eventos personalizados
page_order: 1
page_type: reference
description: "Este artículo describe los eventos personalizados y sus propiedades, la segmentación, el uso, las propiedades de entrada de Canvas, dónde ver los análisis relevantes y más."
search_rank: 2
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Eventos personalizados

> Este artículo describe los eventos personalizados y sus propiedades, los filtros de segmentación relacionados, las propiedades de entrada de Canvas, los análisis relevantes y más. Para obtener más información sobre los eventos de Braze en general, consulta [Eventos]({{site.baseurl}}/user_guide/data/activation/events/).

Los eventos personalizados son acciones realizadas por tus usuarios o actualizaciones sobre ellos. Cuando se registran eventos personalizados, pueden desencadenar cualquier número y tipo de campañas de seguimiento. Luego puedes usar [filtros de segmentación](#segmentation-filters) para segmentar usuarios en función de cuán recientemente y con qué frecuencia ocurrieron esos eventos personalizados. Esto hace que los eventos personalizados sean ideales para rastrear interacciones de alto valor de los usuarios dentro de tu aplicación.

## Casos de uso

Algunos casos de uso comunes de eventos personalizados incluyen:

- Desencadenar una campaña o Canvas basándose en un evento personalizado mediante la [entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/)
- Segmentar usuarios por cuántas veces realizaron un evento personalizado, cuándo fue la última vez que ocurrió el evento, y similares
- Usar los [análisis de eventos personalizados](#analytics) del dashboard para ver un agregado de la frecuencia con la que ocurrió cada evento
- Encontrar análisis adicionales usando informes de [embudo]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports#step-2-select-events-for-funnel-steps) y [retención]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/)
- Aprovechar las [propiedades de entrada persistentes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/) para usar metadatos de tu evento personalizado para la personalización en tus pasos en Canvas
- Generar análisis más sofisticados con [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)
- Configurar [criterios de salida]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria/) para definir cuándo los usuarios deben salir de tu Canvas

## Administrar eventos personalizados

Puedes administrar, crear o bloquear eventos personalizados en el dashboard yendo a **Configuración de datos** > **Eventos personalizados**.

Selecciona el menú junto a un evento personalizado para las siguientes acciones:

### Bloqueo

Puedes bloquear eventos personalizados individuales a través del menú de acciones, o seleccionar y bloquear hasta 100 eventos de forma masiva.

Cuando bloqueas un evento personalizado:

- No se recopilarán datos futuros para ese evento.
- Los datos existentes no estarán disponibles a menos que se desbloquee ese evento.
- Ese evento no aparecerá en filtros ni gráficos.

Además, si un evento personalizado bloqueado está actualmente referenciado por filtros o desencadenadores en otras áreas de Braze, aparecerá un modal de advertencia explicando que todas las instancias de los filtros o desencadenadores que lo referencian serán eliminadas y archivadas.

Para más detalles sobre el bloqueo y la eliminación de datos personalizados, consulta [Bloquear datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).

### Marcar como información de identificación personal (PII)

Los administradores también pueden crear eventos personalizados y marcarlos como PII desde esta página. Estos eventos solo son visibles para administradores y usuarios del dashboard con el permiso "Ver atributos personalizados marcados como PII".

### Añadir descripciones

Puedes añadir una descripción a un evento personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) `Manage Events, Attributes, Purchases`. Selecciona **Editar descripción** para el evento personalizado e introduce lo que desees, como una nota para tu equipo.

### Añadir etiquetas

Puedes añadir etiquetas a un evento personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) "Manage Events, Attributes, Purchases". Las etiquetas se pueden usar para filtrar la lista de eventos.

### Exportar datos

Para exportar la lista de eventos personalizados como un archivo CSV, selecciona **Exportar todo** en la parte superior de la página. Se generará el archivo CSV y se te enviará un enlace de descarga por correo electrónico.

## Ver informes de uso

El informe de uso enumera todos los Canvas, campañas y segmentos que utilizan un evento personalizado específico. Esta lista no incluye usos de Liquid.

Puedes ver hasta 100 informes de uso a la vez seleccionando las casillas de verificación junto a los eventos personalizados correspondientes y luego seleccionando **Ver informe de uso**.

## Registrar eventos personalizados

Los eventos personalizados requieren configuración adicional. Consulta la lista a continuación para obtener documentación sobre cada plataforma, donde encontrarás información sobre los métodos utilizados para registrar eventos personalizados y cómo añadir propiedades y cantidades a tus eventos personalizados.

{% details Expande para ver la documentación por plataforma %}

- [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=unity)
- [.NET MAUI (anteriormente Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## Almacenamiento de eventos personalizados

Todos los datos almacenados en el **perfil de usuario**, incluidos los metadatos de eventos personalizados (primera o última ocurrencia, recuento total y X en Y durante 30 días), se conservan indefinidamente mientras cada perfil esté [activo]({{site.baseurl}}/user_archival#active-users).

## Filtros de segmentación

La siguiente tabla muestra los filtros disponibles para segmentar usuarios por eventos personalizados.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprobar si el evento personalizado ha ocurrido **más de X veces** | **MÁS DE** | **NÚMERO** |
| Comprobar si el evento personalizado ha ocurrido **menos de X veces** | **MENOS DE** | **NÚMERO** |
| Comprobar si el evento personalizado ha ocurrido **exactamente X veces** | **EXACTAMENTE** | **NÚMERO** |
| Comprobar si el evento personalizado ocurrió por última vez **después de la fecha X** | **DESPUÉS DE** | **FECHA** |
| Comprobar si el evento personalizado ocurrió por última vez **antes de la fecha X** | **ANTES DE** | **FECHA** |
| Comprobar si el evento personalizado ocurrió por última vez **hace más de X días** | **MÁS DE** | **NÚMERO DE DÍAS ATRÁS** (número positivo) |
| Comprobar si el evento personalizado ocurrió por última vez **hace menos de X días** | **MENOS DE** | **NÚMERO DE DÍAS ATRÁS** (número positivo) |
| Comprobar si el evento personalizado ocurrió **más de X (máx. = 50) veces** | **MÁS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si el evento personalizado ocurrió **menos de X (máx. = 50) veces** | **MENOS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si el evento personalizado ocurrió **exactamente X (máx. = 50) veces** | **EXACTAMENTE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Análisis

Braze registra el número de veces que han ocurrido los eventos personalizados y la última vez que cada usuario los realizó para la segmentación. Consulta estos análisis yendo a **Análisis** > **Informe de eventos personalizados**.

En la página **Informe de eventos personalizados** del dashboard, puedes ver de forma agregada con qué frecuencia ocurre cada evento personalizado. Las líneas grises superpuestas en la serie temporal indican la última vez que se envió una campaña, lo cual es útil para ver cómo tus campañas afectaron la actividad de eventos personalizados.

![Gráfico de recuento de eventos personalizados en la página de eventos personalizados del dashboard que muestra tendencias para un evento personalizado]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

También puedes usar **Filtros** para desglosar tus eventos personalizados por hora, usuarios activos mensuales (MAU), segmentos o fórmulas de KPI.

![Filtros del gráfico de eventos personalizados]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Incrementa atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#integers) para mantener un contador de una acción del usuario similar a un evento personalizado. Sin embargo, no puedes ver datos de atributos personalizados en una serie temporal. Las acciones de usuario que no necesitan ser analizadas en una serie temporal deben registrarse usando este método.
{% endalert %}

### Por qué no se muestran los análisis de eventos personalizados

Los segmentos creados con datos de eventos personalizados no pueden mostrar datos históricos anteriores a su creación.

## Propiedades de eventos personalizados

Las propiedades de eventos personalizados son metadatos o atributos de eventos personalizados que describen una ocurrencia específica de un evento. Estas propiedades se pueden usar para calificar aún más las condiciones de desencadenamiento, aumentar la personalización en la mensajería, rastrear conversiones y generar análisis más sofisticados a través de la exportación de datos sin procesar.

Para obtener más información, consulta [Propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/).