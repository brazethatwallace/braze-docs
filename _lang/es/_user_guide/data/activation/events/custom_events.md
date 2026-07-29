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

Algunos casos habituales de uso de eventos personalizados incluyen:

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## Administrar eventos personalizados {#managing-custom-events}

Puedes administrar, crear o bloquear eventos personalizados en el panel yendo a **Configuración de datos** > **Eventos personalizados**.

Selecciona el menú junto a un evento personalizado para las siguientes acciones:

### Bloqueo {#blocklisting}

Puedes bloquear eventos personalizados individuales a través del menú de acciones, o seleccionar y bloquear hasta 100 eventos de forma masiva.

Cuando bloqueas un evento personalizado:

{% multi_lang_include data_activation/custom_event_block_effects.md %}

Además, si un evento personalizado bloqueado está actualmente referenciado por filtros o desencadenadores en otras áreas de Braze, aparecerá un modal de advertencia explicando que todas las instancias de los filtros o desencadenadores que lo referencian serán eliminadas y archivadas.

Para más detalles sobre el bloqueo y la eliminación de datos personalizados, consulta [Bloquear datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data).

### Añadir descripciones {#adding-descriptions}

Puedes añadir una descripción a un evento personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases`. Selecciona **Editar descripción** para el evento personalizado e introduce lo que desees, como una nota para tu equipo.

### Añadir etiquetas {#adding-tags}

Puedes añadir etiquetas a un evento personalizado después de crearlo si tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "Manage Events, Attributes, Purchases". Las etiquetas se pueden usar para filtrar la lista de eventos.

### Exportar datos {#exporting-data}

Para exportar la lista de eventos personalizados como un archivo CSV, selecciona **Exportar todo** en la parte superior de la página. Se generará el archivo CSV y se te enviará un enlace de descarga por correo electrónico.

{% alert note %}
No existe un límite fijo en el panel sobre cuántos **eventos personalizados** o **atributos personalizados** distintos puedes definir o almacenar en un perfil; los límites prácticos dependen de la forma de los datos, el volumen de ingesta y el rendimiento del espacio de trabajo. Si planeas hacer seguimiento de un catálogo muy grande de eventos o atributos, trabaja con tu equipo de cuenta de Braze en el modelado y la higiene de datos (por ejemplo, [bloquear]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data) datos no utilizados).
{% endalert %}

## Ver informes de uso {#viewing-usage-reports}

El informe de uso enumera todos los Canvas, campañas y segmentos que utilizan un evento personalizado específico. Esta lista no incluye usos de Liquid.

Puedes ver hasta 100 informes de uso a la vez seleccionando las casillas de verificación junto a los eventos personalizados correspondientes y luego seleccionando **Ver informe de uso**.

## Registrar eventos personalizados {#logging-custom-events}

Los eventos personalizados requieren configuración adicional. Consulta la siguiente documentación por plataforma para conocer los métodos utilizados para registrar eventos personalizados y cómo añadir propiedades y cantidades a tus eventos personalizados.

{% details Expande para ver la documentación por plataforma %}

- [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=unity)
- [.NET MAUI (anteriormente Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=roku)

{% enddetails %}

## Almacenamiento de eventos personalizados {#custom-event-storage}

Todos los datos almacenados en el **perfil de usuario**, incluidos los metadatos de eventos personalizados (primera o última ocurrencia, recuento total y X en Y durante 30 días), se conservan indefinidamente mientras cada perfil esté <a href="/docs/user_archival#active-users">activo</a>.

## Ver el historial de eventos de un usuario {#view-a-users-event-history}

{% alert important %}
El historial de eventos se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si te interesa participar.
{% endalert %}

Usa la pestaña **Historial de eventos** en el perfil de un usuario para ver sus eventos personalizados y compras recientes. Esto te ayuda a confirmar que tu integración está registrando eventos correctamente y a solucionar problemas a nivel de usuario directamente en el panel.

Para ver el historial de eventos de un usuario:

1. Ve a **Audiencia** > **Buscar usuarios** y selecciona un usuario para abrir su perfil.
2. Selecciona la pestaña **Historial de eventos**.

La pestaña muestra los eventos personalizados y las compras del usuario de los últimos 30 días, hasta los 100 eventos más recientes, ordenados del más nuevo al más antiguo.

Cada evento incluye:

- **Tipo de evento:** si el evento es un evento personalizado o una compra.
- **Nombre del evento:** el nombre del evento tal como fue registrado.
- **Hora:** cuándo ocurrió el evento.
- **Propiedades:** las propiedades completas del evento para esa ocurrencia, mostradas como JSON.

Los casos de uso habituales incluyen:

- Verificar que tu integración de SDK o API está enviando eventos como se espera durante el desarrollo o después de un lanzamiento.
- Solucionar problemas sobre por qué un usuario entró o no entró en una campaña o Canvas desencadenados por eventos.
- Investigar un problema de soporte para un usuario específico sin necesidad de configurar una exportación de datos.

{% alert note %}
Ver la pestaña **Historial de eventos** requiere los permisos de usuario **Buscar usuarios**, **Ver PII** y **Ver propiedades de eventos de usuario**, ya que las propiedades de eventos pueden contener datos personales. Para más información, consulta [Permisos de usuario de la empresa]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).
{% endalert %}

## Filtros de segmentación {#segmentation-filters}

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtros de segmentación" }

## Análisis {#analytics}

Braze registra el número de veces que han ocurrido los eventos personalizados y la última vez que cada usuario los realizó para la segmentación. Consulta estos análisis yendo a **Analytics** > **Informe de eventos personalizados**.

En la página **Informe de eventos personalizados** del panel, puedes ver de forma agregada con qué frecuencia ocurre cada evento personalizado. Las líneas grises superpuestas en la serie temporal indican la última vez que se envió una campaña, lo cual es útil para ver cómo tus campañas afectaron la actividad de eventos personalizados.

![Gráfico de recuento de eventos personalizados en la página de eventos personalizados del panel que muestra tendencias para un evento personalizado]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

También puedes usar **Filtros** para desglosar tus eventos personalizados por hora, usuarios activos mensuales (MAU), segmentos o fórmulas de KPI.

![Filtros del gráfico de eventos personalizados]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Incrementa atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) para mantener un contador de una acción del usuario similar a un evento personalizado. Sin embargo, no puedes ver datos de atributos personalizados en una serie temporal. Las acciones de usuario que no necesitan ser analizadas en una serie temporal deben registrarse usando este método.
{% endalert %}

### Por qué no se muestran los análisis de eventos personalizados {#why-custom-events-analytics-arent-showing}

Los segmentos creados con datos de eventos personalizados no pueden mostrar datos históricos anteriores a su creación.

## Propiedades de eventos personalizados {#custom-event-properties}

Las propiedades de eventos personalizados son metadatos o atributos de eventos personalizados que describen una ocurrencia específica de un evento. Estas propiedades pueden utilizarse para cualificar aún más las condiciones de desencadenamiento, aumentar la personalización en la mensajería, hacer seguimiento de conversiones y generar análisis más sofisticados a través de la exportación de datos en bruto.

Para obtener más información, consulta [Propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).