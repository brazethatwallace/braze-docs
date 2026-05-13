---
nav_title: Medir el tamaño del segmento
article_title: Medir el tamaño del segmento
page_order: 5
page_type: reference
tool:
- Segments
description: "Esta página explica cómo puedes monitorizar la membresía y el tamaño de tu segmento."
---

# Medir el tamaño del segmento {#measure-segment-size}

> Esta página explica cómo puedes monitorizar la membresía y el tamaño de tu segmento.

## Cálculo de la membresía del segmento {#segment-membership-calculation}

Braze actualiza la membresía del segmento del usuario a medida que los datos se envían de vuelta a nuestros servidores y se procesan, normalmente de forma instantánea. La membresía del segmento de un usuario no cambiará hasta que esa sesión haya sido procesada. Por ejemplo, un usuario que entra en un segmento de usuarios inactivos cuando la sesión comienza por primera vez será movido inmediatamente fuera del segmento de usuarios inactivos cuando la sesión sea procesada.

### Cálculo del total de usuarios alcanzables {#total-reachable-users-calculation}

Cada segmento muestra el número total de usuarios que son miembros de ese segmento. Al filtrar por **Users from all apps**, también muestra algunos de los canales de mensajería más utilizados (como notificación push web o correo electrónico) y el número de usuarios alcanzables para esos canales específicos.

Es posible que el número total de usuarios sea diferente del número de usuarios alcanzables por cada canal. Además, no todos los canales aparecen en la tabla de usuarios alcanzables. Por ejemplo, Content Cards, webhooks y WhatsApp no se muestran en el desglose. Esto significa que el recuento total de usuarios alcanzables podría ser mayor que la suma de los usuarios de cada canal mostrado.

![Una tabla que muestra el total de usuarios alcanzables desglosado por usuarios alcanzables por correo electrónico, push de iOS, push de Android, push web y push de Kindle.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Para que un usuario aparezca como alcanzable a través de un canal determinado, debe cumplir ambas condiciones:
* Tener una dirección de correo electrónico válida o un token de notificaciones push asociado a su perfil, y
* Haber optado por recibir o estar suscrito a tu aplicación.

Un solo usuario puede pertenecer a diferentes grupos de usuarios alcanzables. Por ejemplo, un usuario podría tener tanto una dirección de correo electrónico válida como un token de push de Android válido y haber optado por ambos, pero no tener un token de push de iOS asociado. La diferencia entre el total de usuarios alcanzables y la suma de los diferentes canales es el número de usuarios que calificaron para el segmento pero no son alcanzables a través de esos canales de comunicación.

## Estadísticas del tamaño del segmento {#statistics-for-segment-size}

Las estadísticas estimadas se aproximan muestreando solo una parte de tu segmento, por lo que debes esperar ver tamaños estimados que sean mayores o menores que el valor real, con espacios de trabajo más grandes que potencialmente presentan mayores márgenes de error. Para obtener un recuento preciso de los usuarios en tu segmento, selecciona **Calculate Exact Statistics**. La membresía exacta del segmento siempre se calculará antes de que un segmento se vea afectado por un mensaje enviado en una campaña o Canvas.

Braze proporciona las siguientes estadísticas sobre el tamaño del segmento.

### Estadísticas de filtros {#filter-statistics}

Para cada grupo de filtros, puedes ver los usuarios alcanzables estimados. Selecciona **Expand extra funnel statistics** para ver un desglose por canales.

![Un grupo de filtros con un filtro para usuarios que tuvieron exactamente un recuento de sesiones.]({% image_buster /assets/img_archive/segment_filter_stats.png %})

## Estimación de usuarios alcanzables {#reachable-users-estimate}

Puedes ver los usuarios alcanzables estimados de un segmento completo, incluyendo los recuentos estimados de usuarios para cada canal, en el panel lateral **Reachable users**. Esta **estimación** te muestra un rango aproximado para el tamaño de tu segmento, y una estimación de qué porcentaje de tu base de usuarios total cae en este segmento. Ten en cuenta que las estadísticas estimadas se almacenan en caché durante 15 minutos a menos que hagas ediciones a tu segmento, en cuyo caso las estadísticas estimadas se actualizarán automáticamente. También puedes ver un recuento exacto de usuarios alcanzables (tanto para el segmento en general como por canal) seleccionando **Calculate exact statistics**.

![El panel "Reachable users" indicando que hay entre 2,3M y 2,4M de usuarios estimados.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Consideraciones para los recuentos estimados {#considerations-for-estimate-counts}

Braze mide el número de usuarios estimados consultando un subconjunto de tus usuarios y luego extrapolando esos resultados a toda tu audiencia. Debido a que el subconjunto de usuarios que Braze consulta puede diferir cada vez que calculamos esta estimación, la estimación también puede cambiar en casos donde la membresía de tu audiencia técnicamente debería haber permanecido igual. Por ejemplo, si reordenas tus filtros o vuelves a verificar el mismo segmento en un momento diferente, es posible que el recuento estimado cambie (aunque **Calculate exact stats** revelaría los mismos resultados si tu segmento no cambió).

Si tienes una gran población de usuarios en tu espacio de trabajo, puedes ver más variación entre tus recuentos estimados en comparación con tus recuentos de cálculo exacto, especialmente en casos donde tu segmento es un porcentaje muy pequeño de la población total de tu espacio de trabajo. Esto se debe a que Braze mide la estimación consultando un subconjunto de tus usuarios y extrapolando los resultados a toda tu base de usuarios. Para bases de usuarios más grandes, se esperan mayores diferencias entre los recuentos estimados y exactos.

Los segmentos muy pequeños tendrán un rango estimado que incluye 0, lo que significa que el porcentaje del total de usuarios puede redondearse a 0. En estos casos, **Calculate exact stats** te ayudará a ver un recuento preciso del tamaño de tu segmento, que puede no ser realmente 0.

![El panel lateral "Reachable users" mostrando un recuento exacto de usuarios de "31".]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Usuarios alcanzables por canal {#reachable-users-by-channel}

Para ver el número de usuarios que son alcanzables para cada canal de mensajería, selecciona **Show breakdown** en el panel **Reachable users**. Esto muestra algunos de los canales de mensajería más utilizados (como notificación push web o correo electrónico) y el número de usuarios alcanzables para esos canales específicos.

La métrica _Total_ representa usuarios únicos. Por ejemplo, si un usuario tiene tanto push de Android como push de iOS, se contará en ambas filas, pero solo contará como 1 usuario en la fila _Total_.

Sin embargo, es posible que el número total de usuarios sea diferente de la suma de usuarios alcanzables por cada canal, ya que un solo usuario puede pertenecer a diferentes grupos de usuarios alcanzables. Por ejemplo, un usuario podría tener tanto una dirección de correo electrónico válida como un token de push de Android válido y haber optado por ambos, pero no tener un token de push de iOS asociado.

Ten en cuenta que no todos los canales aparecen en la tabla **Reachable users** (como Content Cards, webhooks y WhatsApp). Por ejemplo, si tienes usuarios que solo son alcanzables a través de WhatsApp, se reflejarán en el _Total_ pero no en ninguna de las filas específicas por canal. Esto significa que el recuento total de usuarios alcanzables puede ser diferente de la suma de los usuarios de cada canal mostrado.

En los casos en que el _Total_ es mayor que la suma de los canales, la diferencia representa el número de usuarios que calificaron para el segmento pero no son alcanzables a través de esos canales de comunicación.

Para que un usuario aparezca como alcanzable a través de un canal determinado, debe tener:
- Una dirección de correo electrónico válida o un token de notificaciones push asociado a su perfil, y
- Haber optado por recibir o estar suscrito a tu aplicación.

#### Filtros aplicados para usuarios alcanzables por canal específico {#applied-filters-for-channel-specific-reachable-users}

Los siguientes filtros se aplican para cada canal al determinar los usuarios alcanzables.

| Canal | Filtro |
| --- | --- |
| Correo electrónico | **Email Available** es verdadero. |
| Push | **Foreground Push Enabled** es verdadero. |
| SMS | **Subscription Group** es cualquier grupo de suscripción SMS. **Invalid Phone Number** es falso. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Filtros aplicados para usuarios alcanzables por canal específico" }

## Calcular estadísticas exactas {#calculating-exact-statistics}

Para ver un recuento preciso del número de usuarios en tu segmento, selecciona **Calculate exact stats** en el panel **Reachable users**.

Para actualizar las estadísticas de un cálculo que hayas ejecutado previamente, selecciona **Refresh exact statistics**. La fecha en que se ejecutó este cálculo por última vez se actualizará automáticamente.

Ten en cuenta que la precisión de un cálculo es solo del 99,999 % o superior. Por lo tanto, para segmentos grandes, puedes notar ligeras variaciones&#8212;incluso al calcular estadísticas exactas&#8212;lo cual es un comportamiento normal. Además, los resultados de las estadísticas exactas se almacenan en caché durante 24 horas a menos que hagas ediciones a tu segmento, en cuyo caso puedes volver a calcular las estadísticas exactas.

{% alert note %}
Los segmentos divididos equitativamente por [números de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) no tendrán el mismo tamaño. Por ejemplo, si creas un segmento con el filtro **Random Bucket # less than 5000** y un segmento con el filtro **Random Bucket # at least 5000**, es posible y esperado que los tamaños de los segmentos varíen hasta en unos pocos puntos porcentuales. Esto se debe a situaciones como la eliminación de usuarios inactivos y usuarios que no son alcanzables.
{% endalert %}

![Captura de pantalla del panel Reachable users mostrando estadísticas exactas y un menú de desglose expandido.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

Las estadísticas a nivel de filtro individual siempre serán estimadas, incluso si calculas estadísticas exactas. **Calculate exact stats** solo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros. Este cálculo puede tardar unos minutos en ejecutarse. Los espacios de trabajo más grandes en particular pueden requerir períodos más largos para completar los cálculos. Puedes seguir tu progreso en la barra de progreso del panel **Reachable users**. Cuando se espera que un cálculo tarde más de cinco minutos, Braze te enviará los resultados por correo electrónico.

Braze prioriza un cálculo a la vez por espacio de trabajo, por lo que ejecutar múltiples cálculos a la vez causará retrasos. Puedes seleccionar **View calculation queue** para ver qué segmentos están antes del tuyo, su progreso y quién los inició, y tener una idea de cuándo tu cálculo puede ser priorizado.

![Una cola de cálculos con un cálculo.]({% image_buster /assets/img_archive/calculation_queue.png %})

Puedes cancelar un cálculo de estadísticas exactas seleccionando **Cancel**. Esto puede ser beneficioso si hay múltiples cálculos en la cola y quieres priorizar otro cálculo primero.

![Un cálculo activo con la opción de cancelar]({% image_buster /assets/img_archive/cancel_calculation.png %}){: style="max-width:35%"}

## Ver el tamaño histórico de membresía del segmento {#viewing-historical-segment-membership-size}

Para todos los segmentos, puedes ver un gráfico de membresía histórica que muestra la membresía estimada del segmento para cada día. Este gráfico muestra cómo el tamaño de tu segmento cambió a lo largo del tiempo. Usa el menú desplegable para filtrar la membresía del segmento por rango de fechas.

![Usa el menú desplegable de membresía histórica para filtrar la membresía del segmento por rango de fechas.]({% image_buster /assets/img_archive/historical_membership2.png %})

Dado que el objetivo de este gráfico es darte una idea de las tendencias generales de membresía del segmento, el recuento diario es una estimación, similar a cómo el tamaño del segmento es una estimación antes de seleccionar **Calculate Exact Statistics**. Y dado que este gráfico muestra estimaciones, es posible que el tamaño de tu segmento aparezca como "0" en este gráfico, aunque su tamaño real (que se puede determinar después de seleccionar **Calculate Exact Stats**) no sea "0". Es especialmente probable que el gráfico muestre una estimación de "0" si tu segmento es muy pequeño en relación con el tamaño de la población de tu espacio de trabajo.

Por ejemplo, supongamos que tu espacio de trabajo contiene 100 millones de usuarios y tu segmento tiene aproximadamente 700 usuarios. Es posible que en algunos días ningún usuario esté en el segmento y ningún usuario caiga en el rango de contenedor aleatorio utilizado para la estimación de membresía histórica, lo que resulta en un recuento de membresía de un día de 0.

Braze estima el recuento de membresía del segmento consultando un subconjunto de tus usuarios y luego extrapolando esos resultados a toda tu audiencia. Esto significa que los resultados del gráfico proporcionan solo una estimación de lo que la membresía del segmento podría ser en ese día, y se espera que también fluctúe de un día a otro porque una muestra diferente de usuarios puede ser consultada para esta estimación cada día.

{% alert note %}
Todas las estimaciones pueden ser mayores o menores que el valor mostrado en aproximadamente un 1 % del tamaño total de la población de tu espacio de trabajo. Los espacios de trabajo más grandes con más usuarios tienen más probabilidades de tener estimaciones que pueden diferir de los cálculos exactos en una cantidad numérica mayor, incluso si la diferencia sigue siendo del 1 % de la población de usuarios del espacio de trabajo. Esto significa que se esperan mayores diferencias entre estimaciones y recuentos exactos en espacios de trabajo grandes.
{% endalert %}

### Razones de cambios significativos {#reasons-for-significant-changes}

El recuento de membresía puede cambiar significativamente por varias razones, como las que se muestran en esta tabla.

| Razón | Ejemplo |
| --- | --- |
| Comportamiento normal del usuario | Los usuarios se suscriben después de una campaña particularmente exitosa. |
| Los usuarios se importan por CSV | Se importó un archivo CSV de usuarios que aumentó significativamente la membresía del segmento. |
| Se modifican los criterios de audiencia del segmento | Las reglas de audiencia de un segmento existente (como los filtros) fueron cambiadas, causando cambios significativos en la membresía del segmento. |
| Los usuarios se eliminan | Se eliminó un número significativo de usuarios. |
| Una integración del socio se sincronizó con Braze | Un tercero envió datos a Braze que influyeron significativamente en la membresía del segmento. |
| Los usuarios inactivos se archivan | Se archivó un número significativo de perfiles inactivos. Por ejemplo, una gran cantidad de usuarios importados por CSV nunca registran actividad y se archivan al mismo tiempo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Razones de cambios significativos" }