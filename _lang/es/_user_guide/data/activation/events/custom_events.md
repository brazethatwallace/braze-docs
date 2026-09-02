---
nav_title: Eventos personalizados
article_title: Eventos personalizados
page_order: 1
page_type: reference
description: "En este artículo se describen los eventos y propiedades personalizados, la segmentación, el uso, las propiedades de entrada de Canvas, dónde ver los análisis relevantes y mucho más."
search_rank: 2
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"} Eventos personalizados {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> Este artículo describe los eventos personalizados y sus propiedades, el historial de eventos del perfil de usuario, los filtros de segmentación relacionados, las propiedades de entrada en Canvas, los análisis relevantes y mucho más. Para conocer los eventos de Braze en general, consulta [Eventos]({{site.baseurl}}/user_guide/data/activation/events).

Los eventos personalizados son acciones realizadas por tus usuarios o actualizaciones sobre ellos. Cuando se registran eventos personalizados, pueden desencadenar cualquier número y tipo de campañas de seguimiento. A continuación, puedes utilizar [filtros de segmentación](#segmentation-filters) para segmentar a los usuarios en función de lo recientes y frecuentes que hayan sido esos eventos personalizados. Esto hace que los eventos personalizados sean los más adecuados para el seguimiento de interacciones de usuario de alto valor dentro de tu aplicación.

## Ejemplos {#use-cases}

Algunos ejemplos comunes de eventos personalizados incluyen:

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## Gestión de eventos personalizados {#managing-custom-events}

Puedes gestionar, crear o bloquear eventos personalizados en el panel accediendo a **Configuración de datos** > **Eventos personalizados**.

### Solución de problemas con atributos personalizados o eventos duplicados {#troubleshooting-duplicate-custom-attributes-or-events}

{% multi_lang_include data_activation/troubleshooting_duplicate_custom_data_entries.md %}

Selecciona el menú junto a un evento personalizado para las siguientes acciones:

### Bloqueo {#blocklisting}

Puedes bloquear eventos personalizados individuales a través del menú de acciones, o seleccionar y bloquear hasta 100 eventos de forma masiva.

Cuando bloqueas un evento personalizado:

{% multi_lang_include data_activation/custom_event_block_effects.md %}

Además, si un evento personalizado bloqueado está siendo referenciado actualmente por filtros o desencadenadores en otras áreas de Braze, aparecerá un modal de advertencia explicando que todas las instancias de los filtros o desencadenadores que lo referencian serán eliminadas y archivadas.

Para más detalles sobre el bloqueo y la eliminación de datos personalizados, consulta [Bloquear datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data).

### Añadir descripciones {#adding-descriptions}

Puedes añadir una descripción a un evento personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases`. Selecciona **Editar descripción** para el evento personalizado e introduce lo que desees, como una nota para tu equipo.

### Añadir etiquetas {#adding-tags}

Puedes añadir etiquetas a un evento personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "Manage Events, Attributes, Purchases". Las etiquetas pueden utilizarse después para filtrar la lista de eventos.

### Exportar datos {#exporting-data}

Para exportar la lista de eventos personalizados como un archivo CSV, selecciona **Exportar todo** en la parte superior de la página. El archivo CSV se genera, y se te envía un enlace de descarga por correo electrónico.

{% alert note %}
No hay un límite fijo en el panel sobre cuántos **eventos personalizados** o **atributos personalizados** distintos puedes definir o almacenar en un perfil; los límites prácticos dependen de la forma de los datos, el volumen de ingesta y el rendimiento del espacio de trabajo. Si planeas hacer seguimiento de un catálogo muy grande de eventos o atributos, trabaja con tu equipo de cuenta de Braze en el modelado y la higiene de datos (por ejemplo, [bloquear]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data) datos sin uso).
{% endalert %}

## Ver informes de uso {#viewing-usage-reports}

El informe de uso muestra todos los Canvas, Campaigns y Segments que utilizan un evento personalizado específico. Esta lista no incluye los usos de Liquid.

Puedes ver hasta 100 informes de uso a la vez seleccionando las casillas de verificación junto a los eventos personalizados correspondientes y luego seleccionando **Ver informe de uso**.

## Registro de eventos personalizados {#logging-custom-events}

Los eventos personalizados requieren una configuración adicional. Consulta la siguiente documentación de la plataforma para conocer los métodos utilizados para registrar eventos personalizados y cómo añadir propiedades y cantidades a tus eventos personalizados.

{% details Ampliar para ver la documentación por plataforma %}

- [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/analytics#custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=unity)
- [.NET MAUI (anteriormente Xamarin)]({{site.baseurl}}/developer_guide/analytics?sdktab=xamarin#custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=roku)

{% enddetails %}

## Almacenamiento de eventos personalizados {#custom-event-storage}

Todos los datos almacenados en el **perfil de usuario**, incluidos los metadatos de eventos personalizados (primera o última ocurrencia, recuento total y X en Y durante 30 días), se conservan indefinidamente mientras cada perfil esté <a href="/docs/user_archival#active-users">activo</a>.

## Ver el historial de eventos de un usuario {#view-a-users-event-history}

Usa la pestaña **Historial de eventos** en el perfil de un usuario para ver sus eventos personalizados y compras recientes. Esto te ayuda a confirmar que tu integración está registrando eventos correctamente y a solucionar problemas a nivel de usuario directamente en el panel.

Para ver el historial de eventos de un usuario:

1. Ve a **Audiencia** > **Buscar usuarios** y selecciona un usuario para abrir su perfil.
2. Selecciona la pestaña **Historial de eventos**.

La pestaña muestra los eventos personalizados y las compras del usuario de los últimos 30 días, hasta sus 100 eventos más recientes, ordenados del más nuevo al más antiguo.

Cada evento incluye:

- **Tipo de evento:** Si el evento es un evento personalizado o una compra.
- **Nombre del evento:** El nombre del evento tal como fue registrado.
- **Hora:** Cuándo ocurrió el evento.
- **Propiedades:** Las propiedades completas del evento para esa ocurrencia, mostradas como JSON.

Los casos de uso comunes incluyen:

- Verificar que tu integración del SDK or kit de desarrollo de software o API está enviando eventos como se espera durante el desarrollo o después de un lanzamiento.
- Solucionar problemas sobre por qué un usuario entró o no entró en una Campaign o Canvas desencadenada por eventos.
- Investigar un problema de soporte para un usuario específico sin necesidad de configurar una exportación de datos.

{% alert note %}
Ver la pestaña **Historial de eventos** requiere los permisos de usuario **Buscar usuarios**, **Ver PII** y **Ver propiedades de eventos de usuario**, ya que las propiedades de eventos pueden contener datos personales. Para más información, consulta [Permisos de usuario de la empresa]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).
{% endalert %}

## Filtros de segmentación {#segmentation-filters}

La siguiente tabla muestra los filtros disponibles para segmentar usuarios por eventos personalizados.

| Opciones de segmentación | Filtro del menú desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprobar si el evento personalizado ha ocurrido **más de X veces** | **MÁS DE** | **NÚMERO** |
| Comprobar si el evento personalizado ha ocurrido **menos de X veces** | **MENOS DE** | **NÚMERO** |
| Comprobar si el evento personalizado ha ocurrido **exactamente X veces** | **EXACTAMENTE** | **NÚMERO** |
| Comprobar si el evento personalizado ocurrió por última vez **después de la fecha X** | **DESPUÉS DE** | **HORA** |
| Comprobar si el evento personalizado ocurrió por última vez **antes de la fecha X** | **ANTES DE** | **HORA** |
| Comprobar si el evento personalizado ocurrió por última vez **hace más de X días** | **MÁS DE** | **NÚMERO DE DÍAS ATRÁS** (número positivo) |
| Comprobar si el evento personalizado ocurrió por última vez **hace menos de X días** | **MENOS DE** | **NÚMERO DE DÍAS ATRÁS** (número positivo) |
| Comprobar si el evento personalizado ocurrió **más de X (máx. = 50) veces** | **MÁS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si el evento personalizado ocurrió **menos de X (máx. = 50) veces** | **MENOS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si el evento personalizado ocurrió **exactamente X (máx. = 50) veces** | **EXACTAMENTE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtros de segmentación" }

## Análisis {#analytics}

Braze registra el número de veces que se han producido eventos personalizados y la última vez que cada usuario los realizó para la segmentación. Para la configuración de informes, filtros y opciones de exportación, consulta [Informe de eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report).

En la página **Custom Events Report**, puedes ver de forma agregada con qué frecuencia se produce cada evento personalizado. Las líneas grises superpuestas en la serie temporal indican la última vez que se envió una Campaign, lo cual es útil para ver cómo tus Campaigns afectaron a la actividad de eventos personalizados.

![Gráfico de recuento de eventos personalizados en la página Custom Events del panel que muestra las tendencias de un evento personalizado]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

También puedes usar **Filters** para desglosar tus eventos personalizados por hora, usuarios activos mensuales (MAU or usuarios activos al mes), Segments o fórmulas de indicador clave de rendimiento.

![Filtros del gráfico de eventos personalizados]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Incrementar atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) te permite mantener un contador de una acción del usuario similar a un evento personalizado. Sin embargo, no puedes ver los datos de atributos personalizados en una serie temporal. Las acciones de los usuarios que no necesitan analizarse en una serie temporal deben registrarse con este método.
{% endalert %}

### Por qué no se muestran los análisis de eventos personalizados {#why-custom-events-analytics-arent-showing}

Los Segments creados con datos de eventos personalizados no pueden mostrar datos históricos anteriores a su creación.

## Propiedades de eventos personalizados {#custom-event-properties}

Las propiedades de eventos personalizados son metadatos o atributos de eventos personalizados que describen una ocurrencia específica de un evento. Estas propiedades pueden utilizarse para cualificar aún más las condiciones de desencadenamiento, aumentar la personalización en la mensajería, hacer seguimiento de conversiones y generar análisis más sofisticados a través de la exportación de datos en bruto.

Para obtener más información, consulta [Propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).