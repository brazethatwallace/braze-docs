---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 1.3
description: "Este artículo ofrece un resumen de Intelligent Timing (antes Entrega Inteligente) y de cómo puedes aprovechar esta característica en tus Campaigns."
toc_headers: h2
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomintelligent-timing-stylefloatrightwidth120pxborder0-classnoimgborderintelligent-timing}

> Utiliza Intelligent Timing para entregar tu mensaje a cada usuario cuando Braze determine el momento óptimo de envío, que es cuando es más probable que el usuario interactúe (abra o haga clic). Esto te facilita comprobar que estás enviando mensajes a tus usuarios en el momento que prefieren y puede generar una mayor participación.

## Acerca de la sincronización inteligente {#about-intelligent-timing}

Braze calcula el momento óptimo de envío basándose en un análisis estadístico de las interacciones pasadas de tus usuarios con tu aplicación y sus interacciones con cada canal de mensajería. Se utilizan los siguientes datos de interacción:

- Tiempos de sesión
- Direct Opens de push
- Influenced Opens de push
- Clics en correo electrónico
- Aperturas de correo electrónico (excluyendo [aperturas automáticas]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens))
- Clics en servicio de mensajes cortos (solo si el [acortamiento de enlaces]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) y el seguimiento avanzado están habilitados)

Por ejemplo, Sam podría abrir tus correos electrónicos por la mañana de forma habitual, pero abrir tu aplicación e interactuar con las notificaciones por la noche. Esto significa que Sam recibiría una Campaign de correo electrónico con sincronización inteligente por la mañana, mientras que recibiría Campaigns con notificaciones push por la noche, cuando es más probable que interactúe.

Si un usuario no tiene datos de participación relevantes para que Braze calcule el momento óptimo de envío, puedes especificar una hora alternativa.

## Ejemplos {#examples}

- Enviar Campaigns recurrentes que no sean urgentes
- Automatizar Campaigns con usuarios de múltiples zonas horarias
- Al enviar mensajes a tus usuarios más participativos (tendrán la mayor cantidad de datos de participación)

## Uso de la sincronización inteligente {#using-intelligent-timing}

Esta sección describe cómo configurar la sincronización inteligente para tus Campaigns y Canvas.

{% tabs local %}
{% tab Campaign %}
### Paso 1: Añadir sincronización inteligente {#step-1-add-intelligent-timing}

1. Crea una Campaign y redacta tu mensaje.
2. Selecciona **Entrega programada** como tu tipo de entrega.
3. En **Opciones de programación basadas en el tiempo**, selecciona **Intelligent Timing**.
4. Establece la frecuencia de entrada. Para envíos únicos, selecciona **Once** y elige una fecha de envío. Para envíos recurrentes, selecciona **Daily**, **Weekly** o **Monthly** y configura las opciones de recurrencia. Consulta [Consideraciones](#considerations) para más orientación.
5. Opcionalmente, configura las [horas tranquilas](#quiet-hours).
6. Especifica una [hora alternativa](#campaign-fallback). Esta es la hora en que se envía el mensaje si el perfil de un usuario no tiene eventos relevantes para calcular un momento óptimo.

![Pantalla de programación de Campaign que muestra Intelligent Timing con hora alternativa y configuración de horas tranquilas]({% image_buster /assets/img/intelligent_timing/campaign_scheduling.png %})

#### Horas tranquilas {#quiet-hours}

Usa las horas tranquilas para evitar que se envíen mensajes durante horas específicas. Esto es útil cuando quieres evitar enviar mensajes durante las primeras horas de la mañana o durante la noche, mientras permites que la sincronización inteligente determine la mejor ventana de entrega.

{% alert note %}
Las horas tranquilas han sustituido a la configuración **Enviar solo dentro de horas específicas**. En lugar de elegir cuándo se pueden enviar mensajes, ahora eliges cuándo no se deben enviar. Por ejemplo, para enviar mensajes entre las 4 pm y las 6 pm, establece las horas tranquilas de 6 pm a 4 pm del día siguiente.
{% endalert %}

1. Selecciona **Enable Quiet Hours**.
2. Selecciona la hora de inicio y fin en la que **no** se deben enviar mensajes.

![Interruptor de horas tranquilas activado con hora de inicio y fin configuradas para bloquear la entrega de mensajes durante la noche]({% image_buster /assets/img/intelligent_timing/quiet_hours.png %})

Cuando las horas tranquilas están activadas, Braze no enviará mensajes durante el período tranquilo, incluso si ese momento coincide con el momento óptimo de envío de un usuario. Si el momento óptimo de un usuario cae dentro de la ventana tranquila, el mensaje se enviará en el borde más cercano de la ventana.

Por ejemplo, si las horas tranquilas están configuradas de 10:00 PM a 6:00 AM y el momento óptimo de un usuario es las 5:30 AM, Braze retendrá el mensaje y lo entregará a las 6:00 AM, el momento más cercano fuera de la ventana tranquila.

Para más información, consulta [Horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

#### Vista previa de los tiempos de entrega {#preview-delivery-times}

Para ver una estimación de cuántos usuarios recibirán el mensaje en cada hora del día, usa el gráfico de vista previa (solo para Campaigns).

1. Añade Segments o filtros en el paso de públicos objetivo.
2. En la sección **vista previa Delivery Times for** (que aparece tanto en los pasos de públicos objetivo como de entrega programada), selecciona tu canal.
3. Haz clic en **Refresh Data**.

![Gráfico de vista previa de entrega para push en Android que muestra el pico de participación entre las 12 y las 2 PM, y la hora más popular de la aplicación siendo las 2 PM.]({% image_buster /assets/img/intel-timing-preview.png %})

### Paso 2: Elegir una fecha de envío {#step-2-choose-a-send-date}

A continuación, selecciona una fecha de envío para tu Campaign. Ten en cuenta lo siguiente al programar Campaigns con sincronización inteligente:

#### Lanzar la Campaign con 48 horas de antelación {#launch-campaign-48-hours-in-advance}

Lanza tu Campaign al menos 48 horas antes de la fecha de envío programada. Esto se debe a las variaciones en las zonas horarias. Braze calcula el momento óptimo a medianoche en la hora de Samoa (UTC+13), una de las primeras zonas horarias del mundo. Un solo día abarca aproximadamente 48 horas en todo el mundo, lo que significa que si lanzas una Campaign dentro de ese margen de 48 horas, es posible que el momento óptimo de un usuario ya haya pasado en su zona horaria y el mensaje no se envíe.

{% alert important %}
Si se lanza una Campaign y el momento óptimo de un usuario fue hace menos de una hora, el mensaje se envía inmediatamente. Si el momento óptimo fue hace más de una hora, el mensaje no se envía en absoluto.
{% endalert %}

#### Ventana de 3 días para filtros de Segment {#3-day-window-for-segment-filters}

Si estás segmentando una audiencia que ha realizado una acción en un período de tiempo determinado, permite al menos una ventana de 3 días en tus filtros de Segment. Por ejemplo, en lugar de `First used app more than 1 day ago` y `First used app less than 3 days ago`, usa 1 día y 4 días.

![Filtros para el público objetivo donde la Campaign se dirige a usuarios que usaron la aplicación por primera vez entre hace 1 y 4 días.]({% image_buster /assets/img/intelligent_timing/first_used_app.png %})

Esto también se debe a las zonas horarias: seleccionar un período de menos de 3 días puede causar que algunos usuarios salgan del Segment antes de que se alcance su momento óptimo de envío.

Para más información, consulta [FAQ: Sincronización inteligente](#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

#### Programar el envío optimizado al menos 2 días después de la prueba A/B {#schedule-the-optimized-send-at-least-2-days-after-the-ab-test}

Si usas [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) para una Campaign de envío único, la sincronización inteligente puede afectar la duración y el tiempo de tu Campaign.

Al usar la sincronización inteligente, establece la duración del experimento de modo que el envío optimizado comience al menos dos días después de que comience la prueba A/B. Por ejemplo, si tu prueba comienza el 16 de abril a las 4:00 PM, configura el envío optimizado para que comience no antes del 18 de abril a las 4:00 PM. Esto le da a Braze suficiente tiempo para evaluar el comportamiento de los usuarios y enviar mensajes en el momento óptimo.

### Paso 3: Configurar horas tranquilas (opcional) {#step-3-configure-quiet-hours-optional}

Opcionalmente, puedes optar por limitar la ventana de entrega. Esto puede ser útil si tu Campaign se refiere a un evento, venta o promoción específicos, pero generalmente no se recomienda cuando se usa la sincronización inteligente. Para más información, consulta [Consideraciones](#considerations).

Las horas tranquilas actúan como una ventana de no envío. La sincronización inteligente sigue determinando el momento óptimo de envío de cada usuario, pero si ese momento cae dentro de las horas tranquilas, Braze retrasa el mensaje hasta el siguiente momento disponible fuera del período de horas tranquilas.

Para configurar las horas tranquilas:

1. Al configurar la sincronización inteligente, selecciona **Enable Quiet Hours**.
2. Introduce la hora de inicio y fin de la ventana de horas tranquilas.

### Paso 4: Elegir una hora alternativa {#campaign-fallback}

Elige una hora alternativa para usar si el perfil de un usuario no tiene eventos relevantes para calcular un momento óptimo de entrega.

![Programación de una Campaign con sincronización inteligente]({% image_buster /assets/img/intelligent_timing_1.png %})

{% multi_lang_include brazeai/intelligent_suite/fallback_time.md type="campaign" %}

### Paso 5: Vista previa de los tiempos de entrega {#step-5-preview-delivery-times}

Para ver una estimación de cuántos usuarios reciben el mensaje en cada hora del día, usa el gráfico de vista previa:

1. Añade Segments o filtros en el paso de **Target Audiences**.
2. En la sección **vista previa Delivery Times for** (que aparece tanto en los pasos de **Target Audiences** como de **Schedule Delivery**), selecciona tu canal.
3. Selecciona **Refresh Data**.

El gráfico de vista previa muestra cada hora del día usando tu hora local. Las etiquetas no están configuradas en una zona horaria global única.

![Ejemplo de vista previa de tiempos de entrega para push en Android.]({% image_buster /assets/img/intel-timing-preview.png %})

Cada vez que cambies alguna configuración sobre la sincronización inteligente o la audiencia de tu Campaign, actualiza los datos de nuevo para ver un gráfico actualizado.

El gráfico muestra en azul a los usuarios que tenían eventos relevantes para calcular un momento óptimo, y en rojo a los usuarios que usarán la hora alternativa. Usa los filtros de cálculo para ajustar la vista previa y obtener una visión más detallada de cualquiera de los dos grupos de usuarios.
{% endtab %}

{% tab Canvas %}

### Paso 1: Añadir sincronización inteligente

En tu Canvas, añade un [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), luego ve a **Configuración de entrega** y selecciona **Using Intelligent Timing**.

Los mensajes se enviarán a los usuarios que entraron en el paso ese día en su momento local óptimo. Sin embargo, si su momento óptimo ya pasó ese día, se entregará en el momento óptimo del día siguiente. Los pasos de mensaje que se dirigen a múltiples canales pueden enviar o intentar enviar mensajes en diferentes momentos para diferentes canales. Cuando el primer mensaje en un paso de mensaje intenta enviarse, todos los usuarios avanzan automáticamente.

### Paso 2: Elegir una hora alternativa {#step-2-choose-a-fallback-time}

Elige una hora alternativa para que el mensaje se envíe a los usuarios de tu audiencia que no tienen datos de participación relevantes para que Braze calcule un momento óptimo de envío. {% multi_lang_include brazeai/intelligent_suite/fallback_time.md %}

### Paso 4: Añadir un paso de retraso {#step-4-add-a-delay-step}

A diferencia de las Campaigns, no necesitas lanzar tu Canvas 48 horas antes de la fecha de envío porque la sincronización inteligente se configura a nivel de paso, no a nivel de Canvas.

En su lugar, añade un [paso de retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) de al menos dos días calendario entre la entrada del usuario al Canvas y el momento en que recibe el paso de sincronización inteligente.

#### Días calendario vs. días de 24 horas {#calendar-vs-24-hour-days}

Al usar la sincronización inteligente después de un paso de retraso, la fecha de entrega puede variar dependiendo de cómo calcules tu retraso. Esto solo aplica cuando tu retraso está configurado en **After a duration**, ya que hay una diferencia entre cómo se calculan los "días" y los "días calendario".

- **Días:** 1 día equivale a 24 horas, calculadas desde el momento en que el usuario entra en el paso de retraso.
- **Días calendario:** 1 día es el período desde que el usuario entra en el paso de retraso hasta la medianoche en su zona horaria. Esto significa que 1 día calendario podría ser de tan solo unos minutos.

Al usar la sincronización inteligente, recomendamos usar días calendario para los retrasos en lugar de días de 24 horas. Esto se debe a que con los días calendario, el mensaje se enviará en el último día del retraso, en el momento óptimo. Con un día de 24 horas, existe la posibilidad de que el momento óptimo del usuario sea antes de que entre en el paso, lo que significa que se añadirá un día adicional a su retraso.

Por ejemplo, supongamos que el momento óptimo de Luka es las 2:00 pm. Entra en el paso de retraso a las 2:01 pm el 1 de marzo, y el retraso está configurado en 2 días.

- El día 1 termina el 2 de marzo a las 2:01 pm
- El día 2 termina el 3 de marzo a las 2:01 pm

Sin embargo, la sincronización inteligente está configurada para entregar a las 2 pm, momento que ya pasó. Entonces Luka no recibirá el mensaje hasta el día siguiente: el 4 de marzo a las 2:00 pm.

![Gráfico que muestra la diferencia entre días y días calendario. Si el momento óptimo de un usuario es las 2 pm, pero entra en el paso de retraso a las 2:01 pm y el retraso está configurado en 2 días, los días entregan el mensaje 3 días después porque el usuario entró en el paso después de su momento óptimo, mientras que los días calendario entregan el mensaje 2 días después, en el último día del retraso.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}
{% endtab %}
{% endtabs %}

## Consideraciones {#considerations}

- Los mensajes dentro de la aplicación y los webhooks se entregan de inmediato y no reciben tiempos óptimos.
- La sincronización inteligente no está disponible para Campaigns basadas en acciones o activadas por API.
- La sincronización inteligente no debe usarse en los siguientes escenarios:
    - **Límite de velocidad:** Si se usan tanto el límite de velocidad como la sincronización inteligente, no hay garantía sobre cuándo se entregará el mensaje. Las Campaigns recurrentes diarias con sincronización inteligente no admiten con precisión un límite total de envío de mensajes.
    - **Campaigns de calentamiento de IP:** Algunos comportamientos de la sincronización inteligente pueden causar dificultades para alcanzar los volúmenes diarios necesarios cuando estás calentando tu IP por primera vez. Esto se debe a que la sincronización inteligente evalúa los Segments dos veces: una cuando se crea por primera vez la Campaign o el Canvas, y otra antes de enviar a los usuarios para verificar que aún deben estar en ese Segment. Esto puede hacer que los Segments cambien y varíen, lo que a menudo lleva a que algunos usuarios queden fuera del Segment en la segunda evaluación. Estos usuarios no se reemplazan, lo que afecta cuánto puedes acercarte al límite máximo de usuarios.

## Solución de problemas {#troubleshooting}

### El gráfico de vista previa muestra pocos usuarios con tiempos óptimos {#preview-chart-showing-few-users-with-optimal-times}

Si no hay eventos relevantes para un usuario (por ejemplo, usuarios nuevos con poca o ninguna participación), Braze utiliza la configuración de alternativa establecida, ya sea tu hora de alternativa personalizada o la hora más popular de uso de la aplicación entre todos los usuarios.

### Impacto de la zona horaria en la entrega con sincronización inteligente {#impact-of-time-zone-on-intelligent-timing-delivery}

La sincronización inteligente utiliza la zona horaria local de cada usuario y los días calendario para determinar la entrega óptima. Debido a esto, los usuarios en zonas horarias adelantadas o atrasadas respecto a la zona horaria de referencia de tu Campaign pueden recibir mensajes en un día calendario diferente al que podrías esperar.

Por ejemplo, si una Campaign está programada para el 15 de marzo y el tiempo óptimo de un usuario se calcula para esa fecha, un usuario en una zona horaria adelantada respecto al punto de referencia de la Campaign puede recibir el mensaje tarde el 14 de marzo en la zona horaria de referencia, mientras que un usuario en una zona horaria atrasada respecto al punto de referencia puede recibirlo el 16 de marzo.

Si los usuarios no reciben mensajes como se espera, verifica que el campo de zona horaria en su perfil esté completado correctamente. Si el campo de zona horaria está vacío, el usuario puede recibir mensajes que se alineen con la zona horaria de la empresa en lugar de su zona horaria local.

### Envío pasada la fecha programada {#sending-past-the-scheduled-date}

Tu Campaign con sincronización inteligente puede enviarse pasada la fecha programada si utilizas [Optimizar con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection). Para una Campaign de envío único, Braze envía la variante con mejor rendimiento a la audiencia restante después de la prueba inicial, lo que aumenta la duración de la Campaign.

Si utilizas sincronización inteligente, deja tiempo suficiente para que la prueba A/B termine y programa el envío optimizado para dos días después de la prueba inicial.

## Preguntas más frecuentes (FAQ) {#faq}

### General {#general}

#### ¿Qué predice Intelligent Timing? {#what-does-intelligent-timing-predict}

Intelligent Timing se centra en predecir cuándo es más probable que un usuario abra o haga clic en tus mensajes para garantizar que tus mensajes lleguen a los usuarios en los momentos óptimos de participación.

#### ¿Se calcula Intelligent Timing por separado para cada día de la semana? {#is-intelligent-timing-calculated-separately-for-each-day-of-the-week}

No, Intelligent Timing no está vinculado a días concretos. En su lugar, personaliza los tiempos de envío en función de los patrones de interacción únicos de cada usuario y del canal que estés utilizando, como el correo electrónico o las notificaciones push. Esto garantiza que tus mensajes lleguen a los usuarios cuando están más receptivos.

### Cálculos {#calculations}

#### ¿Qué datos se utilizan para calcular el tiempo óptimo para cada usuario? {#what-data-is-used-to-calculate-the-optimal-time-for-each-user}

Para calcular el tiempo óptimo, Intelligent Timing:

1. Analiza los datos de interacción de cada usuario registrados por el SDK or kit de desarrollo de software de Braze. Esto incluye lo siguiente:
  - Horario de las sesiones
  - Push Direct Opens
  - Push Influenced Opens
  - Clics en correos electrónicos
  - Aperturas de correo electrónico (excluyendo aperturas de máquina)
2. Agrupa estos eventos por hora, identificando la hora de envío óptima para cada usuario.

#### ¿Se incluyen las aperturas de máquina al calcular el tiempo óptimo? {#are-machine-opens-included-when-calculating-optimal-time}

No, las [aperturas de máquina]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) se excluyen de los cálculos del tiempo óptimo. Esto significa que los tiempos de envío se basan únicamente en la interacción real de los usuarios, lo que proporciona una sincronización más precisa para tus Campaigns.

#### ¿Cómo de preciso es el momento óptimo? {#how-precise-is-the-optimal-time}

Intelligent Timing programa mensajes durante la «hora de mayor interacción» de cada usuario, basándose en los eventos de inicio de sesión y apertura de mensajes. Dentro de esa hora, la hora del mensaje se redondea a los cinco minutos más próximos. Por ejemplo, si la hora óptima de un usuario se calcula a las 16:58, el mensaje se programará para las 17:00. Puede haber ligeros retrasos en la entrega debido a la actividad del sistema durante los periodos de mayor actividad.

#### ¿Cuáles son los cálculos alternativos si no hay eventos relevantes? {#what-are-the-fallback-calculations-if-there-are-no-relevant-events}

Si no hay eventos relevantes para un usuario, Intelligent Timing utiliza la configuración alternativa de los ajustes de tu mensaje, ya sea una hora alternativa personalizada o la hora más popular para utilizar la aplicación entre todos los usuarios.

### Campaigns {#campaigns}

#### ¿Con cuánta antelación debo lanzar una Campaign de Intelligent Timing para entregarla con éxito a todos los usuarios de todas las zonas horarias? {#how-far-in-advance-should-i-launch-an-intelligent-timing-campaign-to-successfully-deliver-it-to-all-users-in-all-time-zones}

Braze calcula la hora óptima a medianoche en la hora de Samoa, uno de los primeros husos horarios del mundo. En un solo día, abarca aproximadamente 48 horas. Por ejemplo, alguien cuya hora óptima son las 12:01 de la mañana y vive en Australia ya ha pasado su hora óptima, y es «demasiado tarde» para enviarle el mensaje. Por estas razones, necesitas programar con 48 horas de antelación para entregar con éxito a todas las personas del mundo que utilicen tu aplicación.

#### ¿Por qué mi Campaign de Intelligent Timing muestra pocos o ningún envío? {#why-is-my-intelligent-timing-campaign-showing-little-to-no-sends}

Si no hay eventos de interacción relevantes para un usuario (por ejemplo, usuarios nuevos con pocos o ningún clic o apertura), Intelligent Timing utiliza la configuración alternativa, ya sea tu hora alternativa personalizada o la hora más popular para utilizar la aplicación entre todos los usuarios.

#### ¿Por qué mi Campaign de Intelligent Timing se envía pasada la fecha programada? {#why-is-my-intelligent-timing-campaign-sending-past-the-scheduled-date}

Puede que tu Campaign de Intelligent Timing esté enviando más allá de la fecha programada cuando **Optimizar con BrazeAI<sup>TM</sup>** está activado. Para una Campaign de envío único, Braze envía la variante con mejor rendimiento a la audiencia restante una vez finalizada la prueba A/B, lo que aumenta la duración de la Campaign.

Deja suficiente tiempo para que finalice la prueba A/B y programa el envío optimizado para dos días después de la prueba inicial.

### Funcionalidad {#functionality}

#### ¿Cuándo comprueba Braze los criterios de elegibilidad de los filtros de Segment y audiencia? {#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters}

Braze realiza dos comprobaciones cuando se lanza una Campaign:

1. **Comprobación inicial:** A medianoche en la primera zona horaria del día de envío.
2. **Comprobación de la hora programada:** Justo antes de enviar a la hora que Intelligent Timing seleccionó para el usuario.

Ten cuidado al filtrar en función de otros envíos de Campaigns para evitar dirigirte a segmentos no elegibles. Por ejemplo, si enviaras dos Campaigns el mismo día a horas distintas y añades un filtro que solo permita a los usuarios recibir la segunda Campaign si han recibido la primera, los usuarios no recibirán la segunda Campaign. Esto se debe a que nadie era elegible cuando se creó la Campaign por primera vez y se formaron los segmentos.

#### ¿Puedo utilizar horas tranquilas en mi Campaign de Intelligent Timing? {#can-i-use-quiet-hours-in-my-intelligent-timing-campaign}

Las horas tranquilas pueden utilizarse en una Campaign que utilice Intelligent Timing. El algoritmo de Intelligent Timing evitará las horas tranquilas para seguir enviando el mensaje a todos los usuarios elegibles. Dicho esto, te recomendamos que desactives las horas tranquilas, a menos que haya implicaciones legales, de cumplimiento normativo o de otro tipo sobre cuándo se pueden enviar mensajes y cuándo no.

#### ¿Qué ocurre si la hora óptima para un usuario está dentro de las horas tranquilas? {#what-happens-if-the-optimal-time-for-a-user-is-within-the-quiet-hours}

Si la hora óptima determinada cae dentro de las horas tranquilas, Braze busca el límite más cercano de las horas tranquilas y programa el mensaje para la siguiente hora permitida antes o después de las horas tranquilas. El mensaje se pone en cola para enviarse en el límite más cercano de las horas tranquilas en relación con la hora óptima.

#### ¿Puedo utilizar Intelligent Timing y el límite de velocidad? {#can-i-use-intelligent-timing-and-rate-limiting}

El límite de velocidad puede utilizarse en una Campaign que utilice Intelligent Timing. Sin embargo, la naturaleza del límite de velocidad implica que algunos usuarios pueden recibir su mensaje en un momento menos que óptimo, especialmente si un gran número de usuarios en relación con el tamaño del límite de velocidad están programados en la hora alternativa porque no tienen eventos relevantes.

Recomendamos utilizar el límite de velocidad en una Campaign de Intelligent Timing solo cuando haya requisitos técnicos que deban cumplirse utilizando el límite de velocidad.

#### ¿Puedo utilizar Intelligent Timing durante el calentamiento de IP? {#can-i-use-intelligent-timing-while-ip-warming}

Braze no recomienda utilizar Intelligent Timing cuando los usuarios estén calentando IP por primera vez, ya que algunos de sus comportamientos pueden causar dificultades para alcanzar los volúmenes diarios. Esto se debe a que Intelligent Timing evalúa dos veces los segmentos de la Campaign. Una vez cuando se construye la Campaign por primera vez, y una segunda vez antes de enviarla a los usuarios para verificar que deben seguir estando en ese segmento.

Esto puede hacer que los segmentos se desplacen y cambien, lo que a menudo hace que algunos usuarios salgan del segmento en la segunda evaluación. Estos usuarios no se reemplazan, lo que afecta a lo cerca del tope máximo de usuarios que puedes llegar.

#### ¿Cómo se determina la hora más popular de la aplicación? {#how-is-the-most-popular-app-time-determined}

La hora más popular de la aplicación viene determinada por la hora media de inicio de sesión del espacio de trabajo (en hora local). Esta métrica se puede encontrar en el panel al previsualizar los tiempos de una Campaign, y se muestra en rojo.

#### ¿Tiene en cuenta Intelligent Timing las aperturas de máquina? {#does-intelligent-timing-account-for-machine-opens}

Sí, las aperturas de máquina son filtradas por Intelligent Timing, por lo que no influyen en su resultado.

#### ¿Cómo puedo asegurarme de que Intelligent Timing funciona lo mejor posible? {#how-can-i-make-sure-intelligent-timing-works-as-well-as-possible}

Intelligent Timing utiliza el historial individual de interacción con mensajes de cada usuario en cualquier momento en que haya recibido mensajes. Antes de utilizar Intelligent Timing, asegúrate de que has enviado mensajes a los usuarios a distintas horas del día. De ese modo, puedes «muestrear» cuándo puede ser el mejor momento para cada usuario. Un muestreo inadecuado de las distintas horas del día puede hacer que Intelligent Timing elija una hora de envío que no sea la óptima para un usuario.

#### ¿Cómo habilito Intelligent Timing en un paso en Canvas? {#how-do-i-enable-intelligent-timing-on-a-canvas-step}

En Canvas, añade o abre un [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), ve a **Configuración de entrega** y selecciona **Usar Intelligent Timing**. Según las indicaciones de configuración de Canvas en este artículo, incluye un [paso de retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) de al menos dos días naturales entre la entrada al Canvas y ese mensaje para que Intelligent Timing tenga un historial de interacción adecuado que evaluar.