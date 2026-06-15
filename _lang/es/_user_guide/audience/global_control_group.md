---
nav_title: Grupo de control global
article_title: Grupo de control global
alias: /global_control_group/
page_order: 6
page_type: reference
description: "Aprende a configurar y usar el Grupo de control global para medir el impacto general de tus esfuerzos de mensajería a lo largo del tiempo."
tool:
  - Reports
search_rank: 1
toc_headers: h2

---

# Grupo de control global {#global-control-group}

> Usa el Grupo de control global para especificar un porcentaje de todos los usuarios que no deben recibir ninguna campaña ni Canvas, lo que te permite analizar el impacto general de tus esfuerzos de mensajería a lo largo del tiempo.

Al comparar el comportamiento de los usuarios que reciben mensajes con los que no, puedes comprender mejor cómo tus campañas de marketing y Canvas contribuyen a un aumento en las sesiones y los eventos personalizados.

## Cómo funciona el Grupo de control global {#how-the-global-control-group-works}

Con el Grupo de control global, puedes establecer un porcentaje de todos los usuarios como grupo de control. Una vez guardado, los usuarios del grupo no reciben ninguna campaña ni Canvas.

{% alert important %}
Tu Grupo de control global se aplica a todos los canales, campañas y Canvas, excepto a las [campañas de API]({{site.baseurl}}/api/api_campaigns/). Esto significa que los usuarios de tu grupo de control seguirán recibiendo campañas de API. Sin embargo, esta excepción no se aplica a Content Cards. Si estás usando una campaña de Content Cards activada por API, los usuarios de tu grupo de control no las recibirán.
{% endalert %}

### Asignar usuarios aleatoriamente al Grupo de control global {#assign-users-randomly-to-the-global-control-group}

Braze selecciona aleatoriamente múltiples rangos de [números de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/#step-1-segment-your-users-by-the-random-bucket-attribute) e incluye a los usuarios de esos contenedores seleccionados. Si actualmente estás usando números de contenedor aleatorio para otros fines, consulta [Aspectos a tener en cuenta](#things-to-watch-for).

Cuando se genera tu Grupo de control global, todos los usuarios con números de contenedor aleatorio forman parte del grupo. Además, los nuevos usuarios que se unan después de este punto (los adquiridos después de que se generó el Grupo de control global) que tengan estos números de contenedor aleatorio también se añaden al Grupo de control global. De manera similar, si se eliminan muchos usuarios, puedes esperar que el tamaño de tu Grupo de control global se reduzca, ya que un porcentaje de esos usuarios eliminados pertenecía a este grupo. Esto mantiene el tamaño de tu grupo como un porcentaje constante en relación con tu base de usuarios total.

### Asignar usuarios aleatoriamente al grupo de tratamiento para informes {#assign-users-randomly-to-the-treatment-group-for-reporting}

Braze también crea un grupo de tratamiento para informar sobre el aumento. El grupo de tratamiento es un grupo de usuarios seleccionados aleatoriamente que no forman parte de tu Grupo de control global, y se genera usando el mismo método de números de contenedor aleatorio que el Grupo de control global.

Tu grupo de tratamiento tiene un tamaño similar al de tu Grupo de control global, pero es poco probable que sea exactamente del mismo tamaño. Para los [informes](#reporting), Braze mide los comportamientos de los usuarios en tu grupo de control y los usuarios en tu muestra de tratamiento. Cada espacio de trabajo tiene un máximo de un Grupo de control global y un grupo de muestra de tratamiento. El grupo de muestra de tratamiento es el mismo grupo de usuarios independientemente de cómo configures los informes de tu Control global.

### Excluir usuarios de los conmutadores de características {#exclude-users-from-feature-flags}

No puedes habilitar [conmutadores de características]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags/) para los usuarios de tu Grupo de control global. Esto significa que los usuarios de tu Grupo de control global tampoco pueden formar parte de experimentos de conmutadores de características.

### Excluir usuarios del Grupo de control global {#exclude-users-from-the-global-control-group}

No puedes eliminar usuarios específicos del Grupo de control global, pero puedes añadir [configuraciones de exclusión](#step-3-assign-exclusion-settings) para que las campañas y Canvas con etiquetas específicas **no** usen el Grupo de control global. También puedes desactivar y volver a activar tu Grupo de control global para reorganizar la membresía. La duración ideal para reorganizar usuarios varía según el tipo de prueba que estés ejecutando, pero intenta reorganizar no más de una vez al mes.

## Crear un Grupo de control global {#create-a-global-control-group}

### Paso 1: Navega a la configuración del Grupo de control global {#step-1-navigate-to-the-global-control-group-settings}

Desde el dashboard, ve a **Audience** > **Global Control Group**.

### Paso 2: Asigna un porcentaje de todos los usuarios a este grupo de control {#step-2-assign-a-percentage-of-all-users-to-this-control-group}

Introduce un porcentaje para tu grupo de control y selecciona **Save**. Una vez introducido, Braze te muestra una estimación de cuántos usuarios pertenecen a tu Control global, tratamiento y muestra de tratamiento. Ten en cuenta que cuantos más usuarios tengas en tu espacio de trabajo, más precisa será esta estimación.

El número de usuarios en tu Grupo de control global se actualiza automáticamente después de su configuración inicial para mantenerse proporcional a este porcentaje cuando se añaden más usuarios a tu espacio de trabajo. Además, los usuarios que se unan después de que se configure el Grupo de control global y que tengan números de contenedor aleatorio también se añaden al Grupo de control global. Si se añaden muchos usuarios, el tamaño de tu Grupo de control global crece para mantener un porcentaje constante en relación con tu base de usuarios total. Cuando el tamaño de tu Grupo de control global crece, los usuarios que ya estaban en el grupo permanecen en él (a menos que hagas cambios en tu grupo desactivándolo y creando uno nuevo).

Para directrices sobre porcentajes, consulta [Mejores prácticas de pruebas](#percentage-guidelines).

![La configuración del Grupo de control global con la configuración de audiencia establecida en "Asignar el cinco por ciento de todos los usuarios al Grupo de control global".]({% image_buster /assets/img/control_group/control_group4.png %})

### Paso 3: Asigna configuraciones de exclusión {#step-3-assign-exclusion-settings}

Usa etiquetas para añadir configuraciones de exclusión a tu Grupo de control global. Cualquier campaña o Canvas que use las etiquetas incluidas en las configuraciones de exclusión no usará tu Grupo de control global. Estas campañas y Canvas seguirán enviándose a todos los usuarios de la audiencia objetivo, incluidos los de tu Grupo de control global.

{% alert tip %}
Puede que quieras añadir configuraciones de exclusión si tienes mensajes transaccionales que deben enviarse a todos los usuarios.
{% endalert %}

![La sección para añadir o editar configuraciones de exclusión para tu Grupo de control global.]({% image_buster /assets/img/control_group/control_group5.png %})

### Paso 4: Guarda tu grupo de control {#step-4-save-your-control-group}

En este punto, Braze genera un grupo de usuarios seleccionados aleatoriamente que comprende el porcentaje seleccionado de tu base de usuarios total. Una vez guardado, todas las campañas y Canvas activas actualmente y futuras dejan de enviarse a los usuarios de este grupo, excepto las campañas o Canvas que contengan alguna de las etiquetas en tus configuraciones de exclusión.

## Realizar cambios en tu Grupo de control global {#making-changes-to-your-global-control-group}

Solo puedes realizar cambios en tu Grupo de control global desactivándolo y creando uno nuevo. Por ejemplo, si configuraste un Grupo de control global que es el 10 % de tu audiencia y quieres reducir su tamaño al 5 %, debes desactivar tu Grupo de control global actual y volver a activar un nuevo Grupo de control global.

Puedes desactivar tu Grupo de control global en cualquier momento desde la pestaña **Global Control Group Settings**, pero ten en cuenta que hacerlo hace que los usuarios de este grupo sean inmediatamente elegibles para campañas y Canvas.

Antes de desactivar tu grupo de control, [exporta](#export-group-members) un CSV de los usuarios de ese grupo en caso de que necesites consultarlo más adelante. Cuando desactivas un grupo de control, no hay forma de que Braze restaure el grupo o identifique qué usuarios estaban en él.

Después de desactivar tu grupo de control, puedes guardar uno nuevo. Cuando introduces un porcentaje y lo guardas, Braze genera un nuevo grupo de usuarios seleccionados aleatoriamente. Si introduces el mismo porcentaje que antes, Braze genera un nuevo grupo de usuarios para tus grupos de control y tratamiento.

![Un cuadro de diálogo titulado "Estás realizando cambios en la configuración global de mensajería" con texto advirtiendo que una vez que tu Grupo de control global se desactive, ya no se excluirá de ninguna campaña o Canvas nueva o activa.]({% image_buster /assets/img/control_group/control_group2.png %}){: style="max-width:60%" }

## Exportar los miembros de tu grupo de control {#export-group-members}

Si deseas ver qué usuarios están en tu Grupo de control global, puedes exportar los miembros de tu grupo mediante CSV o API.

Para ejecutar una exportación CSV, navega a la pestaña **Global Control Group Settings** y haz clic en <i class="fas fa-download" aria-label="Descargar"></i>&nbsp;**Export**. Para exportar mediante API, usa el [punto de conexión `/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).

{% alert important %}
Los grupos de control históricos no se conservan, por lo que solo puedes exportar los miembros de tu grupo actual. Asegúrate de exportar cualquier información necesaria antes de desactivar un grupo de control.
{% endalert %}

## Ver si un usuario está en un Grupo de control global {#view-whether-a-user-is-in-a-global-control-group}

Puedes ver la membresía del Grupo de control global yendo a la sección **Miscellaneous** en la pestaña **Engagement** del perfil de un usuario individual.

![Una sección "Miscellaneous" que informa que el usuario tiene un número de contenedor aleatorio de 6356 y no está en el Grupo de control global.]({% image_buster /assets/img/control_group/control_group1.png %}){: style="max-width:50%;"}

## Informes {#reporting}

El Informe del Grupo de control global te permite comparar tu grupo con una muestra de tratamiento. Tu muestra de tratamiento es una selección aleatoria de usuarios que no pertenecen al grupo de control, con aproximadamente el mismo número de usuarios que tu grupo de control, generada usando el método de números de contenedor aleatorio.

### Ver un informe {#viewing-a-report}

Para ver un informe de tu Grupo de control global desde el dashboard, ve a **Analytics** > **Global Control Group Report**.

A continuación, selecciona el parámetro con el que deseas ejecutar tu informe (sesiones o un evento personalizado en particular) y selecciona **Run Report**.

![]({% image_buster /assets/img/control_group/control_group6.png %})

### Configurar tu informe {#configuring-your-report}

Al generar tu informe, elige un evento (ya sea sesiones o cualquier evento personalizado) para comparar entre tus grupos de tratamiento y control. Luego elige un período de tiempo para el que deseas ver los datos. Ten en cuenta que si has guardado múltiples experimentos de grupo de control en diferentes períodos de tiempo, debes evitar incluir datos de más de un experimento en tu informe.

Ten en cuenta que las métricas de porcentaje en tu informe están redondeadas. Por ejemplo, en casos donde el número de conversiones es un porcentaje muy bajo de tu grupo de control o tratamiento general, la tasa de conversión puede redondearse a 0 %.

Este informe también muestra un porcentaje de [confianza]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/#understanding-confidence) para tu métrica de cambio respecto al control. En casos donde la tasa de conversión entre tu control y tratamiento son idénticas, se espera una confianza del 0 %, lo que indica que hay un 0 % de probabilidad de una diferencia en el rendimiento entre los dos grupos.

#### Tamaños de grupo {#group-sizes}

Antes de mayo de 2024, el Grupo de control global estaba excluido del archivado de usuarios, pero el grupo de muestra de tratamiento no. A partir de mayo de 2024, ambos grupos están excluidos del archivado de usuarios. Esto podría resultar en que tu grupo de muestra de tratamiento y tu Grupo de control global tengan tamaños significativamente diferentes. La próxima vez que restablezcas tu Grupo de control global, esta discrepancia se resolverá y verás tamaños de grupo similares.

{% alert note %}
Cada espacio de trabajo tiene un máximo de un Grupo de control global y un grupo de muestra de tratamiento. El grupo de muestra de tratamiento es el mismo grupo de usuarios independientemente de cómo configures los informes de tu Control global.
{% endalert %}

### Métricas del informe {#report-metrics}

| Métrica | Definición | Cálculo |
| -- | -- | -- |
| Cambio respecto al control | Calcula el aumento entre la tasa de conversión de tus grupos de tratamiento y control. | ((Tasa de conversión del tratamiento – tasa de conversión del control) ÷ tasa de conversión del control) * 100 |
| Aumento incremental | La diferencia en el total de eventos entre tus grupos de tratamiento y control. Esta métrica busca responder a la pregunta "¿Cuántos eventos de conversión más logró el grupo de tratamiento?". | Total de eventos del tratamiento – total de eventos del control |
| Porcentaje de aumento incremental | El porcentaje del total de eventos de tu tratamiento que puede atribuirse a tu tratamiento (frente al comportamiento natural del usuario). Se calcula dividiendo el aumento incremental (número) entre el número total de eventos de tu grupo de tratamiento. | Aumento incremental (número) ÷ Total de eventos del grupo de tratamiento |
| Tasa de conversión | El porcentaje estimado de usuarios en tu grupo de control o tratamiento que completan tu evento seleccionado durante el período de tiempo seleccionado. Se calcula sumando el número de eventos del período de tiempo y dividiéndolo entre la suma de usuarios dentro del grupo cada día. Esto solo puede aproximarse porque el tamaño del grupo fluctúa regularmente a medida que nuevos usuarios entran en tu Grupo de control global, y los eventos son totales, no únicos. Si el número de conversiones es muy pequeño y tus grupos de control o tratamiento son muy grandes, la tasa de conversión puede redondearse a 0 %. Si el número de eventos es muy alto (por ejemplo, en casos donde un usuario puede realizar más de un evento por día), la tasa de conversión puede superar el 100 %. | Suma del número de eventos para esos usuarios durante ese período de tiempo ÷ suma de usuarios en el grupo cada día |
| Tamaño estimado del grupo | El número estimado de usuarios en tus grupos de control y tratamiento durante el período de tiempo seleccionado. | El tamaño máximo de membresía que tus grupos de control y tratamiento alcanzaron durante el período de tiempo que elegiste para el informe. |
| Número total de eventos | El número total de veces que ocurrió el evento seleccionado durante el período de tiempo elegido. No es único (por ejemplo, si un usuario realiza un evento dos veces durante el período de tiempo, el evento se incrementa dos veces). | Suma del número de veces que ocurrió un evento cada día durante el período de tiempo elegido. |
| Eventos por usuario | El número promedio estimado de veces que los usuarios de cada grupo completaron tus eventos de conversión durante el período de tiempo seleccionado. | Total de eventos ÷ tamaño estimado del grupo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Solución de problemas {#troubleshooting}

A medida que configuras tus grupos de control globales y ves los informes, estos son los errores que puedes encontrar:

| Problema | Solución de problemas |
| --- | --- |
| No se puede guardar el porcentaje introducido al designar un Grupo de control global. | Este problema ocurre si introduces un número no entero o un entero que no está entre 1 y 15 (inclusive). |
| Error "Braze no puede actualizar tu Grupo de control global" en la página de configuración del Control global. | Esto generalmente indica que algún componente de esta página ha cambiado, probablemente debido a acciones realizadas por otro usuario en tu cuenta de Braze. En este caso, actualiza la página e inténtalo de nuevo. |
| El informe del Grupo de control global no tiene datos. | Si accedes al Informe del Grupo de control global sin haber guardado un Grupo de control global, no verás datos en el informe. Crea y guarda un Grupo de control global e inténtalo de nuevo. |
| Mi tasa de conversión es 0 % o no veo la gráfica, aunque hay más de cero eventos ocurriendo. | Si el número de conversiones es muy pequeño y tus grupos de control o tratamiento son muy grandes, la tasa de conversión puede redondearse a 0 % y, por lo tanto, no aparecer en la gráfica. Puedes verificar esto comprobando la métrica de Número total de eventos. Podrías comparar la efectividad de tus dos grupos usando la métrica de porcentaje de aumento incremental. |
| Mi tasa de conversión (u otras métricas) cambian drásticamente dependiendo del período de tiempo para el que estoy viendo los datos. | Si estás viendo datos en períodos de tiempo cortos, es posible que tus métricas fluctúen de un día a otro o de una semana a otra. Visualiza las métricas durante al menos un mes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Aspectos a tener en cuenta {#things-to-watch-for}

#### Números de contenedor aleatorio superpuestos {#overlapping-random-bucket-numbers}

Tu Grupo de control global se forma usando números de contenedor aleatorio, por lo que si estás ejecutando otras pruebas usando filtros de Segment con números de contenedor aleatorio, ten en cuenta que podría haber una superposición entre esos segmentos que creas y los usuarios de tu Grupo de control global.

#### Direcciones de correo electrónico duplicadas {#duplicate-email-addresses}

Si dos usuarios con diferentes ID de usuario externo tienen la misma dirección de correo electrónico, y uno de estos usuarios está en el grupo de control y el otro no, se seguirá enviando un correo electrónico a esa dirección cuando el usuario que no pertenece al grupo de control sea elegible para un correo electrónico. Cuando esto ocurre, ambos perfiles de usuario se marcan como habiendo recibido la campaña o Canvas que contiene ese correo electrónico.

#### Grupo de control global y grupos de control específicos de mensajes {#global-control-group-and-message-specific-control-groups}

Es posible tener tanto un Grupo de control global como usar un grupo de control específico de una campaña o Canvas. Tener un grupo de control específico de una campaña o Canvas te permite medir el impacto de un mensaje en particular.

Los usuarios de tu Grupo de control global no reciben ningún mensaje aparte de aquellos con excepciones de etiquetas, y si añades un control a una campaña o Canvas, Braze retiene una parte de tu grupo de tratamiento global de recibir esa campaña o Canvas en particular. Eso significa que si un miembro del Grupo de control global no es elegible para recibir una campaña o Canvas en particular, no estará presente en el grupo de control de esa campaña o Canvas en particular.

{% alert note %}
En resumen, los usuarios del Grupo de control global se filtran de la audiencia de la campaña o Canvas antes de la entrada. De los usuarios que entran en la campaña o Canvas, un porcentaje de ellos se asigna a la variante de control.
{% endalert %}

#### Segmentos del Grupo de control global en la consola para desarrolladores {#global-control-group-segments-on-the-developer-console}

Puedes ver múltiples segmentos de **Control global** en la sección **Additional API Identifiers** de la página [Claves de API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers/). Esto se debe a que cada vez que el Grupo de control global se activa o desactiva, se forma un nuevo Grupo de control global. Esto genera múltiples segmentos etiquetados como "Grupo de control global".

Solo uno de estos segmentos está activo y puede consultarse usando el [punto de conexión `/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/), o exportarse desde el dashboard. La exportación desde el dashboard indica específicamente qué subsegmentos componen este Grupo de control global.

## Mejores prácticas de pruebas {#testing-best-practices}

### Tamaño óptimo del grupo de control {#percentage-guidelines}

Dos reglas principales a tener en cuenta:
1. Tu grupo de control no debe tener menos de 1000 usuarios.
2. Tu grupo de control no debe ser más del 10 % de tu audiencia total.

Si tienes una audiencia total menor a 10 000, debes aumentar tu porcentaje para crear un grupo de más de 1000 usuarios; en este caso, no debes aumentar tu porcentaje por encima del 15 %. Ten en cuenta que cuanto menor sea el tamaño general de tu espacio de trabajo, más difícil será ejecutar una prueba estadísticamente rigurosa.

- Algunas compensaciones a considerar al pensar en el tamaño de tu grupo de control son que necesitas un número significativamente grande de clientes en tu grupo de control para que cualquier análisis de comportamiento creado sea confiable. Sin embargo, cuanto mayor sea tu grupo de control, menos clientes recibirán tus campañas, lo cual es una desventaja si estás usando tus campañas para impulsar la interacción y las conversiones.
- El porcentaje ideal de tu audiencia total depende de cuán grande sea tu audiencia total. Cuanto mayor sea tu audiencia total, menor puede ser tu porcentaje. Sin embargo, si tienes una audiencia pequeña, necesitas un porcentaje mayor para tu grupo de control.

### Duración del experimento {#experiment-duration}

#### Elige una duración ideal {#reshuffle}

Cuánto tiempo ejecutar tu experimento antes de reorganizar la membresía del grupo de control depende de lo que estés probando y cuáles sean los comportamientos base de tus usuarios. Si no estás seguro, un buen punto de partida es un trimestre (tres meses), pero no debes ir por debajo de un mes.

Para determinar la duración adecuada de tu experimento, considera qué preguntas esperas responder. Por ejemplo, ¿estás buscando ver si hay una diferencia en las sesiones? Si es así, piensa en con qué frecuencia tus usuarios tienen sesiones de forma orgánica. Las marcas cuyos usuarios tienen sesiones todos los días pueden ejecutar experimentos más cortos que las marcas cuyos usuarios solo tienen sesiones un par de veces al mes.

O puede que te interese un evento personalizado, por lo que tu experimento puede necesitar ejecutarse durante más tiempo que un experimento donde examinas sesiones, si es probable que tus usuarios desencadenen ese evento personalizado con menos frecuencia.

{% alert tip %}
Cuanto más tiempo mantengas el mismo grupo de control fuera, más divergen del grupo de tratamiento, lo que puede crear sesgo. Restablecer el Grupo de control global reequilibra la población.
{% endalert %}

#### Intenta limitar la finalización prematura de experimentos {#try-to-limit-ending-experiments-prematurely}

Decide cuánto tiempo ejecutar tu experimento antes de comenzarlo, y luego solo finaliza tu experimento y recopila los resultados finales después de alcanzar este punto predeterminado. Finalizar tu experimento antes de tiempo, o cuando veas datos prometedores, introduce sesgo.

#### Piensa en métricas valiosas {#think-about-valuable-metrics}

Considera cualquier comportamiento base para las métricas que más te interesen. ¿Te interesan las tasas de compra de planes de suscripción que se renuevan solo de forma anual? ¿O los clientes tienen un hábito semanal para el evento que deseas medir? Piensa en cuánto tiempo les toma a los usuarios alterar potencialmente sus comportamientos debido a tu mensajería. Después de decidir cuánto tiempo debe ejecutarse tu experimento, asegúrate de no finalizar tu experimento ni registrar los resultados finales antes de tiempo, o tus hallazgos pueden estar sesgados.