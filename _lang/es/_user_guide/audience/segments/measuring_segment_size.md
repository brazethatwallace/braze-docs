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

## Cálculo de la pertenencia a un Segment {#segment-membership-calculation}

Braze actualiza la pertenencia de un usuario a un Segment a medida que los datos se envían de vuelta a nuestros servidores y se procesan, normalmente de forma instantánea. La pertenencia de un usuario a un Segment no cambiará hasta que esa sesión haya sido procesada. Por ejemplo, un usuario que pertenece a un Segment de usuarios inactivos cuando la sesión comienza por primera vez será movido inmediatamente fuera del Segment de usuarios inactivos cuando la sesión sea procesada.

### Cálculo del total de usuarios alcanzables {#total-reachable-users-calculation}

Cada Segment muestra el número total de usuarios que son miembros de ese Segment. Al filtrar por **Usuarios de todas las aplicaciones**, también se muestran algunos de los canales de mensajería más utilizados (como notificación push web o correo electrónico) y el número de usuarios alcanzables para esos canales específicos.

Es posible que el número total de usuarios sea diferente al número de usuarios alcanzables por cada canal. Además, no todos los canales aparecen en la tabla de usuarios alcanzables. Por ejemplo, Content Cards, webhooks y WhatsApp no se muestran en el desglose. Esto significa que el recuento total de usuarios alcanzables podría ser mayor que la suma de los usuarios de cada canal mostrado.

![Una tabla que muestra el total de usuarios alcanzables desglosados por usuarios alcanzables por correo electrónico, push en iOS, push en Android, push web y push en Kindle.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Para que un usuario aparezca como alcanzable a través de un canal determinado, debe cumplir ambas condiciones:
* Tener una dirección de correo electrónico válida o un token de notificaciones push asociado a su perfil, y
* Haber aceptado o estar suscrito a tu aplicación.

Un solo usuario puede pertenecer a diferentes grupos de usuarios alcanzables. Por ejemplo, un usuario podría tener tanto una dirección de correo electrónico válida como un token de notificaciones push de Android válido y haber aceptado ambos, pero no tener un token de notificaciones push de iOS asociado. La diferencia entre el total de usuarios alcanzables y la suma de los diferentes canales es el número de usuarios que cumplieron los criterios del Segment pero no son alcanzables a través de esos canales de comunicación.

{% alert note %}
**Total de usuarios alcanzables** incluye a todos los que coinciden con los filtros de tu Segment, incluso si ya no están suscritos a un canal. Las filas de canales como **iOS** cuentan a los usuarios que son alcanzables solo en ese canal según las reglas de [Usuarios alcanzables por canal](#reachable-users-by-channel). Para alinear los totales del Segment con los usuarios suscritos, añade filtros como **Push habilitado para iOS** es verdadero (o el equivalente para tu canal).
{% endalert %}

## Estadísticas del tamaño de un segmento {#statistics-for-segment-size}

Las estadísticas estimadas se aproximan muestreando solo una parte de tu segmento, por lo que debes esperar que los tamaños estimados sean mayores o menores que el valor real, y los espacios de trabajo más grandes pueden presentar márgenes de error potencialmente mayores. Para obtener un recuento preciso de los usuarios en tu segmento, selecciona **Calcular estadísticas exactas**. La pertenencia exacta al segmento siempre se calculará antes de que un segmento se vea afectado por un mensaje enviado en una Campaign o Canvas.

Braze proporciona las siguientes estadísticas sobre el tamaño de un segmento.

### Estadísticas de filtros {#filter-statistics}

Para cada grupo de filtros, puedes ver los usuarios alcanzables estimados. Selecciona **Expandir estadísticas adicionales del embudo** para ver un desglose por canales.

![Un grupo de filtros con un filtro para usuarios que tuvieron exactamente un recuento de sesión.]({% image_buster /assets/img_archive/segment_filter_stats.png %})

## Estimación de usuarios alcanzables {#reachable-users-estimate}

Puedes ver la estimación de usuarios alcanzables de un Segment completo, incluidos los recuentos estimados de usuarios para cada canal, en el panel lateral **Usuarios alcanzables**. Esta estimación te muestra un rango aproximado del tamaño de tu Segment y una estimación del porcentaje de tu base de usuarios total que pertenece a este Segment. Ten en cuenta que las estadísticas estimadas se almacenan en caché durante 15 minutos, a menos que realices cambios en tu Segment, en cuyo caso las estadísticas estimadas se actualizarán automáticamente. También puedes ver un recuento exacto de usuarios alcanzables (tanto para el Segment en general como por canal) seleccionando **Calcular estadísticas exactas**.

{% alert note %}
Los espacios de trabajo con más de 50 000 usuarios muestran **Usuarios estimados**; los espacios de trabajo más pequeños muestran **Usuarios exactos**.
{% endalert %}

![El panel "Usuarios alcanzables" que indica que hay entre 2,3 M y 2,4 M de usuarios estimados.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Consideraciones sobre los recuentos estimados {#considerations-for-estimate-counts}

Braze mide el número de usuarios estimados consultando un subconjunto de tus usuarios y luego extrapolando esos resultados a toda tu audiencia. Dado que el subconjunto de usuarios que Braze consulta puede variar cada vez que calculamos esta estimación, la estimación también puede cambiar en casos en los que la composición de tu audiencia técnicamente debería haber permanecido igual. Por ejemplo, si reordenas tus filtros o revisas el mismo Segment en un momento diferente, es posible que el recuento estimado cambie (aunque **Calcular estadísticas exactas** revelaría los mismos resultados si tu Segment no cambió).

Si tienes una gran población de usuarios en tu espacio de trabajo, es posible que veas más variación entre tus recuentos estimados en comparación con tus recuentos de cálculo exacto, especialmente en casos en los que tu Segment representa un porcentaje muy pequeño de la población total de tu espacio de trabajo. Esto se debe a que Braze mide la estimación consultando un subconjunto de tus usuarios y extrapolando los resultados a toda tu base de usuarios. Para bases de usuarios más grandes, es esperable que haya mayores diferencias entre los recuentos estimados y los exactos.

Los Segments muy pequeños tendrán un rango estimado que incluye 0, lo que significa que el porcentaje del total de usuarios puede redondearse a 0. En estos casos, **Calcular estadísticas exactas** te ayudará a ver un recuento preciso del tamaño de tu Segment, que puede no ser realmente 0.

![El panel lateral "Usuarios alcanzables" que muestra un recuento exacto de usuarios de "31".]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Usuarios alcanzables por canal {#reachable-users-by-channel}

Para ver el número de usuarios alcanzables para cada canal de mensajería, selecciona **Mostrar desglose** en el panel **Usuarios alcanzables**. Esto muestra algunos de los canales de mensajería más utilizados (como notificación push web o correo electrónico) y el número de usuarios alcanzables para esos canales específicos.

La métrica _Total_ representa usuarios únicos. Por ejemplo, si un usuario tiene tanto push en Android como push en iOS, se contará en ambas filas, pero solo contará como 1 usuario en la fila _Total_.

Sin embargo, es posible que el número total de usuarios sea diferente a la suma de usuarios alcanzables por cada canal, ya que un solo usuario puede pertenecer a diferentes grupos de usuarios alcanzables. Por ejemplo, un usuario podría tener tanto una dirección de correo electrónico válida como un token de notificaciones push de Android válido y estar suscrito a ambos, pero no tener un token de notificaciones push de iOS asociado.

Ten en cuenta que no todos los canales aparecen en la tabla **Usuarios alcanzables** (como Content Cards, webhooks y WhatsApp). Por ejemplo, si tienes usuarios que solo son alcanzables a través de WhatsApp, se reflejarán en el _Total_ pero no en ninguna de las filas específicas por canal. Esto significa que el recuento total de usuarios alcanzables puede ser diferente a la suma de los usuarios de cada canal mostrado.

En los casos en que el _Total_ sea mayor que la suma de los canales, la diferencia representa el número de usuarios que calificaron para el Segment pero no son alcanzables a través de esos canales de comunicación.

Para que un usuario aparezca como alcanzable a través de un canal determinado, el usuario debe tener:
- Una dirección de correo electrónico válida o un token de notificaciones push asociado a su perfil, y
- Haber aceptado o estar suscrito a tu aplicación.

#### Filtros aplicados para usuarios alcanzables específicos por canal {#applied-filters-for-channel-specific-reachable-users}

Los siguientes filtros se aplican para cada canal al determinar los usuarios alcanzables.

| Canal | Filtro |
| --- | --- |
| Correo electrónico | **Email Available** es verdadero. |
| Push | **Foreground Push Enabled** es verdadero. |
| servicio de mensajes cortos | **Subscription Group** es cualquier grupo de suscripción de servicio de mensajes cortos. **Invalid Phone Number** es falso. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Filtros aplicados para usuarios alcanzables específicos por canal" }

## Cálculo de estadísticas exactas {#calculating-exact-statistics}

Para ver un recuento preciso del número de usuarios en tu segmento, selecciona **Calcular estadísticas exactas** en el panel **Usuarios alcanzables**.

Para actualizar las estadísticas de un cálculo que hayas ejecutado previamente, selecciona **Actualizar estadísticas exactas**. La fecha en que se ejecutó este cálculo por última vez se actualizará automáticamente.

Ten en cuenta que la precisión de un cálculo es solo del 99,999 % o superior. Por lo tanto, para segmentos grandes, es posible que notes ligeras variaciones&#8212;incluso al calcular estadísticas exactas&#8212;lo cual es un comportamiento normal. Además, los resultados de las estadísticas exactas se almacenan en caché durante 24 horas, a menos que realices ediciones en tu segmento, en cuyo caso puedes volver a calcular las estadísticas exactas.

{% alert note %}
Los segmentos divididos equitativamente por [números de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) no tendrán el mismo tamaño. Por ejemplo, si creas un segmento con el filtro **Número de contenedor aleatorio menor que 5000** y un segmento con el filtro **Número de contenedor aleatorio de al menos 5000**, es posible y esperable que los tamaños de los segmentos varíen en unos pocos puntos porcentuales. Esto se debe a situaciones como la eliminación de usuarios inactivos y usuarios que no son alcanzables.
{% endalert %}

![Captura de pantalla del panel de usuarios alcanzables que muestra estadísticas exactas y un menú de desglose expandido.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

Las estadísticas a nivel de filtro individual siempre serán estimadas, incluso si calculas estadísticas exactas. **Calcular estadísticas exactas** solo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros. Este cálculo puede tardar unos minutos en ejecutarse. Los espacios de trabajo más grandes, en particular, pueden requerir períodos más largos para completar los cálculos. Puedes seguir tu progreso en la barra de progreso del panel **Usuarios alcanzables**. Cuando se espera que un cálculo tarde más de cinco minutos, Braze te enviará los resultados por correo electrónico.

Braze prioriza un cálculo a la vez por espacio de trabajo, por lo que ejecutar varios cálculos a la vez provocará retrasos. Puedes seleccionar **Ver cola de cálculos** para ver qué segmentos están antes que el tuyo, su progreso y quién los inició, y hacerte una idea de cuándo se priorizará tu cálculo.

![Una cola de cálculos con un cálculo.]({% image_buster /assets/img_archive/calculation_queue.png %})

Puedes cancelar un cálculo de estadísticas exactas seleccionando **Cancelar**. Esto puede ser útil si hay varios cálculos en la cola y deseas priorizar otro cálculo primero.

## Visualización del tamaño histórico de pertenencia a un segmento {#viewing-historical-segment-membership-size}

Para todos los segmentos, puedes ver un gráfico de pertenencia histórica que muestra la pertenencia estimada al segmento para cada día. Este gráfico muestra cómo el tamaño de tu segmento cambió a lo largo del tiempo. Usa el menú desplegable para filtrar la pertenencia al segmento por rango de fechas.

![Usa el menú desplegable de pertenencia histórica para filtrar la pertenencia al segmento por rango de fechas.]({% image_buster /assets/img_archive/historical_membership2.png %})

Dado que el objetivo de este gráfico es darte una idea de las tendencias generales de pertenencia al segmento, el recuento diario es una estimación, similar a cómo el tamaño del segmento es una estimación antes de seleccionar **Calculate Exact Statistics**. Y como este gráfico muestra estimaciones, es posible que el tamaño de tu segmento aparezca como "0" en este gráfico, aunque su tamaño real (que se puede determinar después de seleccionar **Calculate Exact Stats**) no sea "0". Es especialmente probable que el gráfico muestre una estimación de "0" si tu segmento es muy pequeño en relación con el tamaño de la población de tu espacio de trabajo.

Por ejemplo, supongamos que tu espacio de trabajo contiene 100 millones de usuarios y tu segmento tiene alrededor de 700 usuarios. Es posible que en algunos días, ningún usuario esté en el segmento y ningún usuario caiga en el rango de contenedor aleatorio utilizado para la estimación de pertenencia histórica, lo que resulta en un recuento de pertenencia de un día de 0.

Braze estima el recuento de pertenencia al segmento consultando un subconjunto de tus usuarios y luego extrapolando esos resultados a toda tu audiencia. Esto significa que los resultados del gráfico proporcionan solo una estimación de lo que podría ser la pertenencia al segmento en ese día, y se espera que también fluctúe de un día a otro porque cada día se puede consultar una muestra diferente de usuarios para esta estimación.

{% alert note %}
Todas las estimaciones pueden ser superiores o inferiores al valor mostrado en aproximadamente un 1 % del tamaño total de la población de tu espacio de trabajo. Los espacios de trabajo más grandes con más usuarios tienen más probabilidades de tener estimaciones que pueden diferir de los cálculos exactos en una cantidad numérica mayor, incluso si la diferencia sigue siendo del 1 % de la población de usuarios del espacio de trabajo. Esto significa que es esperable que haya diferencias mayores entre las estimaciones y los recuentos exactos en espacios de trabajo grandes.
{% endalert %}

### Razones de cambios significativos {#reasons-for-significant-changes}

El recuento de pertenencia puede cambiar significativamente por varias razones, como las que se muestran en esta tabla.

| Razón | Ejemplo |
| --- | --- |
| Comportamiento normal del usuario | Los usuarios se suscriben después de una Campaign particularmente exitosa. |
| Los usuarios se importan mediante CSV | Se importó un archivo CSV de usuarios que aumentó significativamente la pertenencia al segmento. |
| Se modifican los criterios de audiencia del segmento | Se cambiaron las reglas de audiencia de un segmento existente (como los filtros), lo que provocó cambios significativos en la pertenencia al segmento. |
| Se eliminan usuarios | Se eliminó un número significativo de usuarios. |
| Una integración del partner se sincronizó con Braze | Un tercero envió datos a Braze que influyeron significativamente en la pertenencia al segmento. |
| Se archivan usuarios inactivos | Se archivó un número significativo de perfiles inactivos. Por ejemplo, una gran cantidad de usuarios importados por CSV nunca registran actividad y se archivan al mismo tiempo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Razones de cambios significativos" }