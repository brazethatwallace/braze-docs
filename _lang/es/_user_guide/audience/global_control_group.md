---
nav_title: Grupo de control global
article_title: Grupo de control global
alias: /global_control_group/
page_order: 6
page_type: reference
description: "Aprende a configurar y usar el grupo de control global para medir el impacto general de tus esfuerzos de mensajería a lo largo del tiempo."
tool:
  - Reports
search_rank: 1
toc_headers: h2

---

# Grupo de control global {#global-control-group}

> Usa el grupo de control global para especificar un porcentaje de todos los usuarios que no deben recibir ninguna campaña ni Canvas, lo que te permite analizar el impacto general de tus esfuerzos de mensajería a lo largo del tiempo.

Al comparar el comportamiento de los usuarios que reciben mensajes con los que no, puedes comprender mejor cómo tus campañas de marketing y Canvas contribuyen a un aumento en las sesiones y los eventos personalizados.

## Cómo funciona el grupo de control global {#how-the-global-control-group-works}

Con el grupo de control global, puedes establecer un porcentaje de todos los usuarios como grupo de control. Cuando se guarda, los usuarios del grupo no reciben ninguna Campaign ni Canvas.

{% alert important %}
Tu grupo de control global se aplica a todos los canales, Campaigns y Canvas, excepto a las [Campaigns de API]({{site.baseurl}}/api/api_campaigns). Esto significa que los usuarios de tu grupo de control seguirán recibiendo Campaigns de API. Sin embargo, esta excepción no se aplica a Content Cards. Si estás utilizando una campaña de tarjeta de contenido activada por API, los usuarios de tu grupo de control no las recibirán.
{% endalert %}

### Asignar usuarios aleatoriamente al grupo de control global {#assign-users-randomly-to-the-global-control-group}

Braze selecciona aleatoriamente múltiples rangos de [números de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers#create-segments-using-random-bucket-numbers) e incluye a los usuarios de esos contenedores seleccionados. Si actualmente estás utilizando números de contenedor aleatorio para cualquier otro propósito, consulta [Aspectos a tener en cuenta](#things-to-watch-for).

Cuando se genera tu grupo de control global, todos los usuarios con números de contenedor aleatorio forman parte del grupo. Además, los nuevos usuarios que se unan después de este punto (aquellos adquiridos después de que se generó el grupo de control global) que tengan estos números de contenedor aleatorio también se añaden al grupo de control global. De manera similar, si se eliminan muchos usuarios, puedes esperar que el tamaño de tu grupo de control global se reduzca, ya que un porcentaje de esos usuarios eliminados ha caído en este grupo. Esto mantiene el tamaño de tu grupo como un porcentaje constante en relación con toda tu base de usuarios.

### Asignar usuarios aleatoriamente al grupo de tratamiento para informes {#assign-users-randomly-to-the-treatment-group-for-reporting}

Braze también crea un grupo de tratamiento para informar sobre el incremento. El grupo de tratamiento es un grupo de usuarios seleccionados aleatoriamente que no forman parte de tu grupo de control global, y se genera utilizando el mismo método de números de contenedor aleatorio que el grupo de control global.

Tu grupo de tratamiento es similar en tamaño a tu grupo de control global, pero es poco probable que tenga exactamente el mismo tamaño. Para los [informes](#reporting), Braze mide los comportamientos de los usuarios en tu grupo de control y los usuarios en tu muestra de tratamiento. Cada espacio de trabajo tiene un máximo de un grupo de control global y un grupo de muestra de tratamiento. El grupo de muestra de tratamiento es el mismo grupo de usuarios independientemente de cómo configures los informes de tu control global.

### Excluir usuarios de los conmutadores de características {#exclude-users-from-feature-flags}

No puedes habilitar [conmutadores de características]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags) para los usuarios de tu grupo de control global. Esto significa que los usuarios de tu grupo de control global tampoco pueden formar parte de experimentos de conmutadores de características.

### Excluir usuarios del grupo de control global {#exclude-users-from-the-global-control-group}

No puedes eliminar usuarios específicos del grupo de control global, pero puedes añadir [configuración de exclusión](#step-3-assign-exclusion-settings) para que las Campaigns y Canvas con etiquetas específicas **no** utilicen el grupo de control global. También puedes desactivar y volver a activar tu grupo de control global para reorganizar la membresía. La duración ideal para reorganizar usuarios varía según el tipo de prueba que estés ejecutando, pero intenta reorganizar no más de una vez al mes.

## Crear un grupo de control global {#create-a-global-control-group}

### Paso 1: Navega a la configuración del grupo de control global {#step-1-navigate-to-the-global-control-group-settings}

Desde el panel, ve a **Audiencia** > **Grupo de control global**.

### Paso 2: Asigna un porcentaje de todos los usuarios a este grupo de control {#step-2-assign-a-percentage-of-all-users-to-this-control-group}

Introduce un porcentaje para tu grupo de control y selecciona **Guardar**. Una vez introducido, Braze te muestra una estimación de cuántos usuarios forman parte de tu control global, tratamiento y muestra de tratamiento. Ten en cuenta que cuantos más usuarios tengas en tu espacio de trabajo, más precisa será esta estimación.

El número de usuarios en tu grupo de control global se actualiza automáticamente después de su configuración inicial para mantenerse proporcionado a este porcentaje cuando se añaden más usuarios a tu espacio de trabajo. Además, los usuarios que se unen después de que se configure el grupo de control global y que tienen números de contenedor aleatorio también se añaden al grupo de control global. Si se añaden muchos usuarios, el tamaño de tu grupo de control global crece para mantener un porcentaje constante en relación con toda tu base de usuarios. Cuando el tamaño de tu grupo de control global crece, los usuarios que ya estaban en el grupo siguen permaneciendo en él (a menos que hagas cambios en tu grupo deshabilitándolo y creando uno nuevo).

Para directrices sobre porcentajes, consulta [Mejores prácticas de pruebas](#percentage-guidelines).

![La configuración del grupo de control global con los ajustes de audiencia establecidos en "Asignar el cinco por ciento de todos los usuarios al grupo de control global".]({% image_buster /assets/img/control_group/control_group4.png %})

### Paso 3: Asigna ajustes de exclusión {#step-3-assign-exclusion-settings}

Usa etiquetas para añadir ajustes de exclusión a tu grupo de control global. Cualquier Campaign o Canvas que use las etiquetas incluidas en los ajustes de exclusión no utilizará tu grupo de control global. Estas Campaigns y Canvas seguirán enviándose a todos los usuarios del público objetivo, incluidos los que están en tu grupo de control global.

Ten en cuenta que el menú desplegable de etiquetas solo muestra las etiquetas que actualmente están aplicadas a al menos una Campaign o Canvas activo. Si creas una nueva etiqueta y quieres usarla en los ajustes de exclusión, aplícala primero a una Campaign o Canvas.

{% alert tip %}
Puede que quieras añadir ajustes de exclusión si tienes mensajes transaccionales que deben enviarse a todos los usuarios.
{% endalert %}

![La sección para añadir o editar ajustes de exclusión para tu grupo de control global.]({% image_buster /assets/img/control_group/control_group5.png %})

### Paso 4: Guarda tu grupo de control {#step-4-save-your-control-group}

En este punto, Braze genera un grupo de usuarios seleccionados aleatoriamente que comprende el porcentaje seleccionado de tu base de usuarios total. Una vez guardado, todas las Campaigns y Canvas activos actualmente y futuros dejarán de enviarse a los usuarios de este grupo, excepto las Campaigns o Canvas que contengan alguna de las etiquetas en tus ajustes de exclusión.

## Hacer cambios en tu grupo de control global {#making-changes-to-your-global-control-group}

Solo puedes hacer cambios en tu grupo de control global deshabilitándolo y creando uno nuevo. Por ejemplo, si configuraste un grupo de control global que representa el 10 % de tu audiencia y quieres reducir su tamaño al 5 %, debes deshabilitar tu grupo de control global actual y volver a habilitar un nuevo grupo de control global.

Puedes deshabilitar tu grupo de control global en cualquier momento desde la pestaña **Global Control Group Settings**, pero ten en cuenta que hacerlo provoca que los usuarios de este grupo sean inmediatamente elegibles para Campaigns y Canvas.

Antes de deshabilitar tu grupo de control, [exporta](#export-group-members) un CSV de los usuarios de ese grupo en caso de que necesites consultarlo más adelante. Cuando deshabilitas un grupo de control, Braze no puede restaurar el grupo ni identificar qué usuarios formaban parte de él.

Después de deshabilitar tu grupo de control, puedes guardar uno nuevo. Cuando introduzcas un porcentaje y lo guardes, Braze generará un nuevo grupo de usuarios seleccionados aleatoriamente. Si introduces el mismo porcentaje que antes, Braze generará un nuevo grupo de usuarios para tus grupos de control y tratamiento.

![Un cuadro de diálogo titulado "You are making changes to Global Messaging Settings" con un texto que advierte que, una vez deshabilitado tu grupo de control global, ya no se excluirá de ninguna Campaign o Canvas nueva o activa.]({% image_buster /assets/img/control_group/control_group2.png %}){: style="max-width:60%" }

## Exportar los miembros de tu grupo de control {#export-group-members}

Si deseas ver qué usuarios están en tu grupo de control global, puedes exportar los miembros de tu grupo mediante CSV o API.

Para ejecutar una exportación CSV, navega a la pestaña **Global Control Group Settings** y haz clic en <i class="fas fa-download" aria-label="Descargar"></i>&nbsp;**Export**. Para exportar mediante API, usa el [endpoint `/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group).

{% alert important %}
Los grupos de control históricos no se conservan, por lo que solo puedes exportar los miembros de tu grupo actual. Asegúrate de exportar cualquier información necesaria antes de desactivar un grupo de control.
{% endalert %}

## Ver si un usuario está en un grupo de control global {#view-whether-a-user-is-in-a-global-control-group}

Puedes ver la pertenencia al grupo de control global yendo a la sección **Miscellaneous** en la pestaña **Engagement** del perfil de un usuario individual.

![Una sección "Miscellaneous" que informa que el usuario tiene un número de contenedor aleatorio de 6356 y no está en el grupo de control global.]({% image_buster /assets/img/control_group/control_group1.png %}){: style="max-width:50%;"}

## Informes {#reporting}

El informe del grupo de control global te permite comparar tu grupo con una muestra de tratamiento. Tu muestra de tratamiento es una selección aleatoria de usuarios que no pertenecen al grupo de control, con aproximadamente el mismo número de usuarios que tu grupo de control, generada mediante el método de número de contenedor aleatorio.

### Ver un informe {#viewing-a-report}

Para ver un informe de tu grupo de control global desde el panel, ve a **Analytics** > **Informe del grupo de control global**.

A continuación, selecciona el parámetro con el que quieres ejecutar tu informe (sesiones o un evento personalizado en particular) y selecciona **Ejecutar informe**.

![Selecciona el parámetro con el que quieres ejecutar tu informe (sesiones o un evento personalizado en particular) y selecciona Ejecutar informe.]({% image_buster /assets/img/control_group/control_group6.png %})

### Configurar tu informe {#configuring-your-report}

Al generar tu informe, elige un evento (ya sean sesiones o cualquier evento personalizado) para comparar entre tus grupos de tratamiento y de control. Luego elige un periodo de tiempo para el que deseas ver los datos. Ten en cuenta que si has guardado varios experimentos de grupo de control en diferentes periodos de tiempo, debes evitar incluir datos de más de un experimento en tu informe.

Ten en cuenta que las métricas de porcentaje en tu informe están redondeadas. Por ejemplo, en los casos en que el número de conversiones es un porcentaje muy bajo de tu grupo de control o tratamiento general, la tasa de conversión puede redondearse a 0%.

Este informe también muestra un porcentaje de [confianza]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#understanding-confidence) para tu métrica de cambio respecto al control. En los casos en que la tasa de conversión entre tu grupo de control y de tratamiento sea idéntica, se espera una confianza del 0%, lo que indica que hay un 0% de probabilidad de que exista una diferencia en el rendimiento entre los dos grupos.

#### Tamaños de los grupos {#group-sizes}

Antes de mayo de 2024, el grupo de control global estaba excluido del archivado de usuarios, pero la muestra de tratamiento no lo estaba. A partir de mayo de 2024, ambos grupos están excluidos del archivado de usuarios. Esto podría hacer que tu muestra de tratamiento y tu grupo de control global tengan tamaños significativamente diferentes. La próxima vez que restablezcas tu grupo de control global, esta discrepancia se resolverá y verás tamaños de grupo similares.

{% alert note %}
Cada espacio de trabajo tiene un máximo de un grupo de control global y un grupo de muestra de tratamiento. El grupo de muestra de tratamiento es el mismo grupo de usuarios independientemente de cómo configures los informes de control global.
{% endalert %}

### Métricas del informe {#report-metrics}

| Métrica | Definición | Cálculo |
| -- | -- | -- |
| Cambio respecto al control | Calcula el incremento entre la tasa de conversión de tus grupos de tratamiento y de control. | ((Tasa de conversión del tratamiento – tasa de conversión del control) ÷ tasa de conversión del control) \* 100 |
| Incremento incremental | La diferencia en el total de eventos entre tus grupos de tratamiento y de control. Esta métrica busca responder a la pregunta "¿Cuántos eventos de conversión más logró el grupo de tratamiento?". | Total de eventos del tratamiento – total de eventos del control |
| Porcentaje de incremento incremental | El porcentaje del total de eventos de tu tratamiento que puede atribuirse a tu tratamiento (frente al comportamiento natural del usuario). Se calcula dividiendo el incremento incremental (número) entre el número total de eventos de tu grupo de tratamiento. | Incremento incremental (número) ÷ total de eventos del grupo de tratamiento |
| Tasa de conversión | El porcentaje estimado de usuarios en tu grupo de control o tratamiento que completan el evento seleccionado durante el periodo de tiempo elegido. Se calcula sumando el número de eventos del periodo de tiempo y dividiéndolo entre la suma de usuarios dentro del grupo cada día. Esto solo puede aproximarse porque el tamaño del grupo fluctúa regularmente a medida que nuevos usuarios entran en tu grupo de control global, y los eventos son totales, no únicos. Si el número de conversiones es muy pequeño y tus grupos de control o tratamiento son muy grandes, la tasa de conversión puede redondearse a 0%. Si el número de eventos es muy alto (por ejemplo, en casos en que un usuario puede realizar más de un evento por día), la tasa de conversión puede superar el 100%. | Suma del número de eventos de esos usuarios durante ese periodo de tiempo ÷ suma de usuarios en el grupo cada día |
| Tamaño estimado del grupo | El número estimado de usuarios en tus grupos de control y tratamiento durante el periodo de tiempo seleccionado. | El tamaño máximo de membresía que tus grupos de control y tratamiento alcanzaron durante el periodo de tiempo que elegiste para el informe. |
| Número total de eventos | El número total de veces que el evento seleccionado ocurrió durante el periodo de tiempo elegido. No es único (por ejemplo, si un usuario realiza un evento dos veces durante el periodo de tiempo, el evento se incrementa dos veces). | Suma del número de veces que un evento ocurrió cada día durante el periodo de tiempo elegido. |
| Eventos por usuario | El número promedio estimado de veces que los usuarios de cada grupo completaron tus eventos de conversión durante el periodo de tiempo seleccionado. | Total de eventos ÷ tamaño estimado del grupo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Métricas del informe" }

## Solución de problemas {#troubleshooting}

A medida que configuras tus grupos de control global y consultas los informes, estos son los errores con los que puedes encontrarte:

| Problema | Solución de problemas |
| --- | --- |
| No se puede guardar el porcentaje introducido al designar un grupo de control global. | Este problema ocurre si introduces un valor que no es un número entero o un número entero que no está entre 1 y 15 (inclusive). |
| Error "Braze is not able to update your Global Control Group" en la página de configuración del control global. | Esto suele indicar que algún componente de esta página ha cambiado, probablemente debido a acciones realizadas por otro usuario en tu cuenta de Braze. En este caso, actualiza la página y vuelve a intentarlo. |
| El informe del grupo de control global no tiene datos. | Si accedes al informe del grupo de control global sin haber guardado un grupo de control global, no verás datos en el informe. Crea y guarda un grupo de control global e inténtalo de nuevo. |
| Mi tasa de conversión es del 0 % o no veo la gráfica, aunque hay más de cero eventos ocurriendo. | Si el número de conversiones es muy pequeño y tus grupos de control o tratamiento son muy grandes, la tasa de conversión puede redondearse al 0 % y, por lo tanto, no aparecer en la gráfica. Puedes verificarlo comprobando la métrica de número total de eventos. Podrías comparar la eficacia de tus dos grupos utilizando la métrica de porcentaje de incremento. |
| Mi tasa de conversión (u otras métricas) cambian drásticamente dependiendo del período de tiempo para el que estoy viendo los datos. | Si estás viendo datos en períodos de tiempo cortos, es posible que tus métricas fluctúen de un día a otro o de una semana a otra. Consulta las métricas durante al menos un mes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }

### Aspectos a tener en cuenta {#things-to-watch-for}

#### Números de contenedor aleatorio superpuestos {#overlapping-random-bucket-numbers}

Tu grupo de control global se forma utilizando números de contenedor aleatorio, por lo que, si estás ejecutando otras pruebas con filtros de Segment de números de contenedor aleatorio, ten en cuenta que podría haber una superposición entre los Segments que crees y los usuarios de tu grupo de control global.

#### Direcciones de correo electrónico duplicadas {#duplicate-email-addresses}

Si dos usuarios con diferentes ID de usuario externo tienen la misma dirección de correo electrónico, y uno de ellos está en el grupo de control y el otro no, se enviará un correo electrónico a esa dirección cuando el usuario que no pertenece al grupo de control sea elegible para recibir un correo electrónico. Cuando esto ocurre, ambos perfiles de usuario se marcan como si hubieran recibido la Campaign o el Canvas que contiene ese correo electrónico.

#### Grupo de control global y grupos de control específicos de mensaje {#global-control-group-and-message-specific-control-groups}

Es posible tener un grupo de control global y también utilizar un grupo de control específico de Campaign o de Canvas. Tener un grupo de control específico de Campaign o de Canvas te permite medir el impacto de un mensaje en particular.

Los usuarios de tu grupo de control global no reciben ningún mensaje salvo aquellos con excepciones de etiqueta, y si añades un control a una Campaign o Canvas, Braze retiene a una parte de tu grupo de tratamiento global de recibir esa Campaign o Canvas en particular. Esto significa que si un miembro del grupo de control global no es elegible para recibir una Campaign o Canvas en particular, no estará presente en el grupo de control de esa Campaign o Canvas en particular.

{% alert note %}
En resumen, los usuarios del grupo de control global se filtran de la audiencia de la Campaign o Canvas antes de la entrada. De los usuarios que entran en la Campaign o Canvas, un porcentaje de ellos se asigna a la variante de control.
{% endalert %}

#### Segments de grupo de control global en la consola para desarrolladores {#global-control-group-segments-on-the-developer-console}

Es posible que veas múltiples Segments de **control global** en la sección **Identificadores de API adicionales** de la página [Claves de API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Esto se debe a que cada vez que se habilita o deshabilita el grupo de control global, se forma un nuevo grupo de control global. Esto genera múltiples Segments etiquetados como "Global Control Group".

Solo uno de estos Segments está activo y se puede consultar mediante el [endpoint `/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group), o exportar desde el panel. La exportación desde el panel indica específicamente qué subsegmentos componen este grupo de control global.

## Mejores prácticas de pruebas {#testing-best-practices}

### Tamaño óptimo del grupo de control {#percentage-guidelines}

Dos reglas principales a tener en cuenta:
1. Tu grupo de control no debe tener menos de 1000 usuarios.
2. Tu grupo de control no debe superar el 10 % de tu audiencia total.

Si tu audiencia total es menor de 10 000, deberías aumentar tu porcentaje para crear un grupo de más de 1000 usuarios; en este caso, no deberías aumentar tu porcentaje por encima del 15 %. Ten en cuenta que cuanto menor sea el tamaño general de tu espacio de trabajo, más difícil será ejecutar una prueba estadísticamente rigurosa.

- Algunas compensaciones a considerar al pensar en el tamaño de tu grupo de control son que necesitas un número significativamente grande de clientes en tu grupo de control para que cualquier análisis de comportamiento creado sea confiable. Sin embargo, cuanto mayor sea tu grupo de control, menos clientes recibirán tus Campaigns, lo cual es una desventaja si estás utilizando tus Campaigns para impulsar la participación y las conversiones.
- El porcentaje ideal de tu audiencia total depende de lo grande que sea tu audiencia total. Cuanto mayor sea tu audiencia total, menor puede ser tu porcentaje. Sin embargo, si tienes una audiencia pequeña, necesitas un porcentaje mayor para tu grupo de control.

### Duración del experimento {#experiment-duration}

#### Elige una duración ideal {#reshuffle}

El tiempo que debes ejecutar tu experimento antes de reorganizar la membresía del grupo de control depende de lo que estés probando y de cuáles sean los comportamientos de referencia de tus usuarios. Si no estás seguro, un buen punto de partida es un trimestre (tres meses), pero no deberías bajar de un mes.

Para determinar la duración adecuada de tu experimento, considera qué preguntas esperas responder. Por ejemplo, ¿buscas ver si hay una diferencia en las sesiones? Si es así, piensa en la frecuencia con la que tus usuarios tienen sesiones de forma orgánica. Las marcas cuyos usuarios tienen sesiones todos los días pueden ejecutar experimentos más cortos que las marcas cuyos usuarios tienen sesiones solo un par de veces al mes.

O quizás te interese un evento personalizado, por lo que tu experimento puede necesitar ejecutarse durante más tiempo que un experimento en el que examinas sesiones, si es probable que tus usuarios desencadenen ese evento personalizado con menos frecuencia.

{% alert tip %}
Cuanto más tiempo mantengas el mismo grupo de control fuera, más divergen del grupo de tratamiento, lo que puede crear sesgo. Restablecer el grupo de control global reequilibra la población.
{% endalert %}

#### Intenta limitar la finalización prematura de los experimentos {#try-to-limit-ending-experiments-prematurely}

Decide cuánto tiempo ejecutar tu experimento antes de comenzarlo, y luego solo finaliza tu experimento y recopila los resultados finales después de alcanzar este punto predeterminado. Finalizar tu experimento antes de tiempo, o cada vez que veas datos prometedores, introduce sesgo.

#### Piensa en las métricas valiosas {#think-about-valuable-metrics}

Considera cualquier comportamiento de referencia para las métricas que más te interesen. ¿Te interesan las tasas de compra de planes de suscripción que se renuevan solo de forma anual? ¿O los clientes tienen un hábito semanal para el evento que te gustaría medir? Piensa en cuánto tiempo tardan los usuarios en alterar potencialmente sus comportamientos debido a tu mensajería. Después de decidir cuánto tiempo debe ejecutarse tu experimento, asegúrate de no finalizar tu experimento ni registrar los resultados finales antes de tiempo, o tus hallazgos podrían estar sesgados.