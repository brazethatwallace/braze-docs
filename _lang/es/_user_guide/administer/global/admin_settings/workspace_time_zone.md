---
nav_title: Zonas horarias del espacio de trabajo
article_title: Zonas horarias del espacio de trabajo
alias: /workspace_time_zones/
page_order: 3
description: "Este artículo de referencia explica cómo configurar diferentes zonas horarias para tus espacios de trabajo de Braze, lo que proporciona un mayor control sobre la programación de campañas y Canvas para equipos que operan en distintas ubicaciones geográficas."
toc_headers: h2
---

# Zonas horarias del espacio de trabajo {#workspace-time-zones}

> Las zonas horarias del espacio de trabajo permiten a los administradores definir zonas horarias específicas para cada espacio de trabajo individual. Esto hace que las campañas programadas y los Canvas (que no utilizan la hora local ni Intelligent Timing) se envíen según la zona horaria designada por el espacio de trabajo, en lugar de la zona horaria general de la empresa.

{% alert important %}
Las zonas horarias del espacio de trabajo para el envío de mensajes se están implementando de forma gradual. Es posible que aún no veas esta configuración en tu dashboard.
{% endalert %}

De forma predeterminada, un nuevo espacio de trabajo hereda la zona horaria establecida para tu empresa. Los administradores pueden anular este valor predeterminado para uno o varios espacios de trabajo con zonas horarias de espacio de trabajo. Cuando se establece una zona horaria para un espacio de trabajo, las campañas programadas y los Canvas dentro de ese espacio de trabajo hacen referencia a esa nueva zona horaria para sus horas de envío.

Por ejemplo, si la zona horaria de un espacio de trabajo está configurada en PST y una campaña dentro de ese espacio de trabajo está programada para enviarse a las 3 p. m. PST, se entregará a las 3 p. m. PST. Esto es así incluso si la zona horaria general de tu empresa es diferente (como la EST, donde las 3 p. m. PST serían las 6 p. m. EST).

## Administración de las zonas horarias del espacio de trabajo {#manage-workspace-time-zones}

Si eres administrador, puedes acceder y administrar las zonas horarias del espacio de trabajo yendo a **Settings** > **Admin Settings** > **Workspace Time Zones**.

Aquí puedes ver una lista de todos tus espacios de trabajo, su zona horaria configurada y la última vez que se editó la zona horaria. Usa la barra de búsqueda para encontrar espacios de trabajo específicos por nombre.

![Página "Workspace Time Zones" con una lista de espacios de trabajo, sus respectivas zonas horarias y cuándo se editaron por última vez.]({% image_buster /assets/img/workspaces/time_zones/workspace_time_zones_page.png %})

### Configurar una zona horaria {#setting-a-time-zone}

{% alert note %}
Las actualizaciones de zona horaria pueden tardar unos minutos en surtir efecto.
{% endalert %}

{% tabs %}
{% tab Espacio de trabajo único %}
1. Localiza el espacio de trabajo deseado en la lista.
2. Selecciona el icono **Edit** junto al nombre del espacio de trabajo.

![Botón "Edit" junto al nombre de un espacio de trabajo.]({% image_buster /assets/img/workspaces/time_zones/single_edit_icon.png %})

{: start="3"}
3. En el menú desplegable, selecciona la zona horaria deseada para ese espacio de trabajo.
4. Selecciona **Save**.

![Menú desplegable con la zona horaria GMT seleccionada.]({% image_buster /assets/img/workspaces/time_zones/edit_single_workspace.png %})
{% endtab %}
{% tab Múltiples espacios de trabajo %}

Puedes aplicar una zona horaria específica a varios espacios de trabajo a la vez haciendo lo siguiente:

1. Selecciona las casillas junto a todos los espacios de trabajo que deseas actualizar.
2. Selecciona **Edit time zone**.
3. En el menú desplegable, selecciona una zona horaria para aplicar a todos los espacios de trabajo seleccionados.

![Página "Workspace Time Zones" con varios espacios de trabajo seleccionados y un botón "Edit time zone".]({% image_buster /assets/img/workspaces/time_zones/bulk_edit_workspace_time_zone.png %})

{: start="4"}
4. Selecciona **Save**.

{% endtab %}
{% endtabs %}

## Impacto en campañas y Canvas {#impact-on-campaigns-and-canvases}

{% alert important %}
Informa a los equipos y partes interesadas relevantes dentro de cada espacio de trabajo sobre cualquier cambio de zona horaria para evitar confusiones con los horarios de las campañas.
{% endalert %}

- **Campañas con hora local e Intelligent Timing:** Las campañas y los Canvas que utilizan la hora local del usuario o [Intelligent Timing]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery/#option-3-intelligent-timing) para la entrega seguirán funcionando como antes y no se verán afectados por las zonas horarias del espacio de trabajo.
- **Campañas y Canvas programados:** Cualquier campaña o Canvas programado que no utilice la hora local del usuario ni Intelligent Timing para la entrega ahora se enviará según la zona horaria seleccionada del espacio de trabajo.
- **Campañas programadas antes de un cambio de zona horaria:** Si programaste una campaña o Canvas antes de cambiar la zona horaria del espacio de trabajo, Braze mantiene la hora de envío original y no la reprograma. Por ejemplo, si una campaña está configurada para enviarse a las 7 p. m. PST y la zona horaria del espacio de trabajo se cambia a EST, la campaña se sigue enviando a las 7 p. m. PST (que ahora corresponde con las 10 p. m. EST). El sistema seguirá haciendo referencia a la hora original, pero la interpretará a través de la nueva zona horaria del espacio de trabajo.

## Impacto en los filtros de audiencia basados en fechas {#impact-on-date-based-audience-filters}

Cuando se actualiza la zona horaria de un espacio de trabajo, los filtros de audiencia que utilizan criterios basados solo en fechas (donde no se proporciona una hora específica) se reevalúan según los límites de la nueva zona horaria.

Para filtros como "Realizó por última vez el evento personalizado X después de", Braze utiliza la zona horaria del espacio de trabajo para determinar el inicio y el fin del día calendario. Cambiar esta configuración desplaza el punto de corte de las 11:59 p. m. para esa fecha específica.

### Ejemplo {#example}

Un espacio de trabajo actualiza su zona horaria de hora del este (EST) a hora del Pacífico (PST).

- **Hora de corte anterior:** 11:59 p. m. EST
- **Nueva hora de corte:** 11:59 p. m. PST (que es las 2:59 a. m. EST del día siguiente)

Tras este cambio, un usuario que realiza el evento personalizado a las 10 p. m. PST del 6 de marzo de 2026 (que es la 1 a. m. EST del 7 de marzo de 2026) ahora se incluye en la audiencia, ya que se encontraba dentro del límite del día calendario en PST para esa fecha.

## Impacto en los datos de rendimiento {#impact-on-performance-data}

Actualizar la zona horaria de tu espacio de trabajo afecta la forma en que se agregan y muestran los datos de rendimiento en tu dashboard. Dado que los análisis de datos como *usuarios activos diarios* (DAU) dependen de la zona horaria del espacio de trabajo para definir el inicio y el fin de un día de 24 horas, un cambio en esta configuración desplaza esas ventanas de informes.

Cuando cambias la zona horaria, es posible que notes fluctuaciones o "desplazamientos" en tus datos históricos. Esto ocurre porque la ventana de 12 a. m. a 11:59 p. m. se ha movido en relación con UTC.

Considera el siguiente ejemplo para un espacio de trabajo que cambia su zona horaria de UTC a PST (UTC-8):

- **Antes del cambio:** Un "día" para los informes se mide de 12 a. m. UTC a 11:59 p. m. UTC.
- **Después del cambio:** Un "día" para los informes ahora se mide de 12 a. m. PST a 11:59 p. m. PST.

Como resultado, un evento que ocurrió a la 1 a. m. UTC del 1 de enero se habría contabilizado previamente en las estadísticas del 1 de enero. Después del cambio a PST, ese mismo evento (que ocurrió a las 5 p. m. PST del 31 de diciembre) se atribuiría a las métricas del día anterior en el informe actualizado.