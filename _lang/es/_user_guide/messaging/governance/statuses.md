---
nav_title: Estados
article_title: Estados
page_order: 6
description: "Conoce los estados de las Campaigns y los Canvas y cómo usarlos en el panel."
tool:
    - Campaigns
    - Canvas
---

# Estados de Campaign y Canvas {#campaign-and-canvas-statuses}

> Conoce los estados de las Campaigns y los Canvas y cómo puedes usarlos en el panel.

## Filtrar por estado {#filtering-by-status}

Para filtrar tus Campaigns o Canvas por estado, selecciona **All Statuses** y luego elige un estado.

![El desplegable "All Statuses" en el panel de Braze.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Cambiar el estado {#changing-the-status}

Para cambiar el estado de una Campaign o Canvas, selecciona el menú <i class="fas fa-ellipsis-vertical"></i> y luego elige un estado.

![Una lista de Canvas en el panel de Braze, con el menú abierto para uno de los Canvas.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Estados disponibles {#available-statuses}

Estos son los estados disponibles para Campaigns y Canvas:

| Estado | Descripción |
| --- | --- |
| Activo | Las Campaigns y Canvas activos están en proceso de envío. De forma predeterminada, verás las Campaigns y Canvas activos en sus páginas respectivas. |
| Borrador | Los borradores de Campaigns y Canvas están guardados pero no se han lanzado. Para continuar editando y comenzar a enviar, puedes seleccionar el borrador yendo a **Mensajería** en el panel de Braze y seleccionando **Canvas** o **Campaigns**. |
| Archivado | Las Campaigns y Canvas archivados son mensajes que ya no se están enviando. Estas Campaigns y Canvas también se eliminan de los gráficos de estadísticas en las páginas [**Inicio**]({{site.baseurl}}/user_guide/analytics/dashboards/home) e [**Ingresos**]({{site.baseurl}}/user_guide/analytics/reports/revenue_report). |
| Detenido | Las Campaigns y Canvas detenidos están en pausa, pero aún puedes editarlos. Para reanudar un Canvas, ve al paso **Resumen** del creador de Canvas y selecciona **Reanudar Canvas**. Para Campaigns, selecciona el menú <i class="fas fa-ellipsis-vertical" aria-label="Más opciones"></i> y luego **Reanudar**. Para más información, consulta [Comportamiento de Canvas detenido](#stopped-canvas-behavior). |
| Inactivo | Cuando una Campaign o un Canvas ya no está enviando mensajes, Braze le asignará un estado inactivo para ayudar a ordenar y gestionar tu lista de Campaigns y Canvas. Puedes ver qué Campaigns o Canvas se detendrán automáticamente y la fecha de detención asociada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados disponibles" }

### Comportamiento de Canvas detenido {#stopped-canvas-behavior}

Cuando un Canvas se detiene, ocurre lo siguiente:

- **Mensajes programados:** Tus mensajes programados no se enviarán, independientemente de la posición del usuario en el Canvas. Esto también incluye a los usuarios que estaban en cola debido a límites de velocidad.
- **Envíos de correo electrónico:** Los envíos de correo electrónico pueden no detenerse de inmediato, ya que tu proveedor de servicios de correo electrónico (ESP) puede seguir procesando tus solicitudes existentes.
- **Pasos de retraso:** Los usuarios en un [paso de retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) permanecerán allí con normalidad, pero saldrán del Canvas cuando finalice el período establecido.
- **Cambios en borrador:** Cualquier cambio en borrador del Canvas se descartará cuando el Canvas se detenga.

Para reanudar el Canvas, ve al paso **Resumen** del creador de Canvas y selecciona **Reanudar Canvas**. Cuando se reactive, cualquier mensaje previamente detenido se enviará según lo programado&#8212;siempre que el horario programado no haya pasado ya.

## Buenas prácticas {#best-practices}

### Monitorea tus mensajes por estado {#monitor-your-messages-by-status}

Puedes monitorear tus mensajes por estado para revisar los detalles de rendimiento. Por ejemplo, si tienes una serie de Campaigns activas, puedes evaluar el rendimiento de cada Campaign con sus métricas de participación y hacer ajustes según sea necesario. Si, en cambio, tienes algunos Canvas detenidos, puedes considerar si deberían reanudarse para mensajería o archivarse por completo.

{% alert tip %}
¿Buscas más formas de mantenerte organizado? Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/messaging/governance/tags) para proporcionar más contexto de un vistazo.
{% endalert %}

### Audita tus mensajes activos {#audit-your-active-messages}

Al realizar auditorías de tus Campaigns y Canvas activos, puedes evaluar la relevancia y el rendimiento, y eliminar o actualizar cualquier Campaign o Canvas obsoleto para mantener tu mensajería actualizada.