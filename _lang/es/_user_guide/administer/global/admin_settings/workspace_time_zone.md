---
nav_title: Zonas horarias del espacio de trabajo
article_title: Zonas horarias del espacio de trabajo
alias: /workspace_time_zones/
page_order: 3
description: "Este artículo de referencia explica cómo configurar diferentes zonas horarias para tus espacios de trabajo de Braze, lo que proporciona un mayor control sobre la programación de Campaigns y Canvas para equipos que operan en distintas ubicaciones geográficas."
toc_headers: h2
---

# Zonas horarias del espacio de trabajo {#workspace-time-zones}

> Las zonas horarias del espacio de trabajo permiten a los administradores definir zonas horarias específicas para cada espacio de trabajo individual. Esto hace que las Campaigns programadas y los Canvas (que no utilizan la hora local ni la sincronización inteligente) se envíen según la zona horaria designada por el espacio de trabajo, en lugar de la zona horaria general de la empresa.

{% alert important %}
Las zonas horarias del espacio de trabajo para el envío de mensajes se están implementando de forma gradual. Es posible que aún no veas esta configuración en tu panel.
{% endalert %}

De forma predeterminada, un nuevo espacio de trabajo hereda la zona horaria establecida para tu empresa. Los administradores pueden anular este valor predeterminado para uno o varios espacios de trabajo con zonas horarias de espacio de trabajo. Cuando se establece una zona horaria para un espacio de trabajo, las Campaigns programadas y los Canvas dentro de ese espacio de trabajo hacen referencia a esa nueva zona horaria para sus horas de envío.

Por ejemplo, si la zona horaria de un espacio de trabajo está configurada en PST y una Campaign dentro de ese espacio de trabajo está programada para enviarse a las 3 p. m. PST, se entregará a las 3 p. m. PST. Esto es así incluso si la zona horaria general de tu empresa es diferente (como la EST, donde las 3 p. m. PST serían las 6 p. m. EST).

## Gestionar zonas horarias del espacio de trabajo {#manage-workspace-time-zones}

Si eres administrador, puedes acceder y gestionar las zonas horarias del espacio de trabajo yendo a **Configuración** > **Configuración de administrador** > **Zonas horarias del espacio de trabajo**.

Aquí puedes ver una lista de todos tus espacios de trabajo, su zona horaria configurada y la última vez que se editó la zona horaria. Usa la barra de búsqueda para encontrar espacios de trabajo específicos por nombre.

### Configurar una zona horaria {#setting-a-time-zone}

{% alert note %}
Las actualizaciones de zona horaria pueden tardar unos minutos en surtir efecto.
{% endalert %}

{% tabs %}
{% tab Un solo espacio de trabajo %}
1. Localiza el espacio de trabajo deseado en la lista.
2. Selecciona el icono **Editar** junto al nombre del espacio de trabajo.

![Página "Zonas horarias del espacio de trabajo" con el icono "Editar" junto al nombre de un espacio de trabajo.]({% image_buster /assets/img/workspaces/time_zones/single_edit_icon.png %})

{: start="3"}
3. En el menú desplegable, selecciona la zona horaria deseada para ese espacio de trabajo.
4. Selecciona **Guardar**.

{% endtab %}
{% tab Varios espacios de trabajo %}

Puedes aplicar una zona horaria específica a varios espacios de trabajo a la vez haciendo lo siguiente:

1. Selecciona las casillas junto a todos los espacios de trabajo que deseas actualizar.
2. Selecciona **Editar zona horaria**.
3. En el menú desplegable, selecciona una zona horaria para aplicar a todos los espacios de trabajo seleccionados.

![Página "Zonas horarias del espacio de trabajo" con varios espacios de trabajo seleccionados y el menú desplegable "Editar zona horaria" abierto.]({% image_buster /assets/img/workspaces/time_zones/bulk_edit_workspace_time_zone.png %})

{: start="4"}
4. Selecciona **Guardar**.

{% endtab %}
{% endtabs %}

## Impacto en Campaigns y Canvas {#impact-on-campaigns-and-canvases}

{% alert important %}
Informa a los equipos y partes interesadas relevantes dentro de cada espacio de trabajo sobre cualquier cambio de zona horaria para evitar confusiones con los horarios de las Campaigns.
{% endalert %}

- **Campaigns y Canvas con hora local y sincronización inteligente:** Las Campaigns y los Canvas que utilizan la hora local del usuario o la [sincronización inteligente]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#option-3-intelligent-timing) para la entrega continúan funcionando como antes y no se ven afectados por las zonas horarias del espacio de trabajo.
- **Campaigns y Canvas programados:** Cualquier Campaign o Canvas programado que no utilice la hora local del usuario ni la sincronización inteligente para la entrega se envía según la zona horaria seleccionada del espacio de trabajo.
- **Campaigns programadas antes de un cambio de zona horaria:** Si programaste una Campaign o un Canvas antes de cambiar la zona horaria del espacio de trabajo, Braze mantiene la hora de envío original y no la reprograma. Por ejemplo, si una Campaign está configurada para enviarse a las 7 pm PST y la zona horaria del espacio de trabajo se cambia a EST, la Campaign se sigue enviando a las 7 pm PST (que ahora corresponde con las 10 pm EST). El sistema continúa haciendo referencia a la hora original, pero la interpreta a través de la nueva zona horaria del espacio de trabajo.

## Impacto en los filtros de audiencia basados en fechas {#impact-on-date-based-audience-filters}

Cuando se actualiza la zona horaria de un espacio de trabajo, los filtros de audiencia que utilizan criterios basados únicamente en fechas (donde no se proporciona una hora específica) se reevalúan en función de los límites de la nueva zona horaria.

Para filtros como "Last did custom event X after", Braze utiliza la zona horaria del espacio de trabajo para determinar el inicio y el final del día calendario. Cambiar esta configuración desplaza el punto de corte de las 11:59 pm para esa fecha específica.

### Ejemplo {#example}

Un espacio de trabajo actualiza su zona horaria de Eastern Time (EST) a Pacific Time (PST).

- **Hora de corte anterior:** 11:59 pm EST
- **Nueva hora de corte:** 11:59 pm PST (que equivale a las 2:59 am EST del día siguiente)

Tras este cambio, un usuario que realiza el evento personalizado a las 10 pm PST del 6 de marzo de 2026 (que equivale a la 1 am EST del 7 de marzo de 2026) ahora se incluye en la audiencia, ya que se encontraba dentro del límite del día calendario en PST para esa fecha.

## Impacto en los datos de rendimiento {#impact-on-performance-data}

Actualizar la zona horaria de tu espacio de trabajo afecta la forma en que los datos de rendimiento se agregan y se muestran en tu panel. Dado que los análisis de datos como los *usuarios activos diarios* (usuario activo diario) dependen de la zona horaria del espacio de trabajo para definir el inicio y el final de un día de 24 horas, un cambio en esta configuración desplaza esas ventanas de informes.

Cuando cambias la zona horaria, es posible que notes fluctuaciones o "desplazamientos" en tus datos históricos. Esto ocurre porque la ventana de 12 am a 11:59 pm se ha movido en relación con UTC.

Considera el siguiente ejemplo para un espacio de trabajo que cambia su zona horaria de UTC a PST (UTC-8):

- **Antes del cambio:** Un "día" para los informes se mide de 12 am UTC a 11:59 pm UTC.
- **Después del cambio:** Un "día" para los informes ahora se mide de 12 am PST a 11:59 pm PST.

Como resultado, un evento que ocurrió a la 1 am UTC del 1 de enero se habría contabilizado previamente en las estadísticas del 1 de enero. Después del cambio a PST, ese mismo evento (que ocurrió a las 5 pm PST del 31 de diciembre) se atribuiría a las métricas del día anterior en el informe actualizado.