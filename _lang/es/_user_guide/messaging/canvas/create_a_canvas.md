---
nav_title: Crear un Canvas
article_title: Crear un Canvas
page_order: 1
description: "Aprende a crear y lanzar un Canvas: configura los aspectos básicos, el horario de entrada, la audiencia objetivo, los ajustes de envío, construye tu recorrido y más."
tool: Canvas
search_rank: 1
---

# Crear un Canvas {#create-a-canvas}

> Este artículo de referencia cubre los pasos necesarios para crear, mantener y probar un Canvas. Sigue esta guía o consulta nuestro [curso de Braze Learning sobre Canvas](https://learning.braze.com/quick-overview-canvas-setup). También puedes empezar desde una [plantilla de Braze Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) para acelerar tu configuración. Para más información, consulta [Plantillas de Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates).

{% details Expande para ver los detalles del editor original de Canvas %}
Ya no puedes crear ni duplicar Canvas usando la experiencia original de Canvas. Braze recomienda [clonar tus Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) al editor más reciente.
{% enddetails %}

## Paso 1: Configura un nuevo Canvas {#step-1-set-up-a-new-canvas}

Primero, ve a **Mensajería** > **Canvas** y selecciona **Crear Canvas**.

El creador de Canvas te guiará paso a paso a través de la configuración de tu Canvas, desde ponerle nombre hasta establecer eventos de conversión y llevar a los usuarios previstos a su recorrido del cliente. Selecciona cada una de las siguientes pestañas para ver qué configuraciones puedes ajustar en cada paso del creador.

{% tabs local %}
  {% tab Aspectos básicos %}
    Aquí configurarás los aspectos básicos de tu Canvas:
    - Nombra tu Canvas
    - Añade equipos
    - Añade etiquetas
    - Asigna eventos de conversión y elige sus tipos de evento y plazos

    Más información sobre el [paso Aspectos básicos](#step-11-start-with-your-canvas-basics).
  {% endtab %}
  {% tab Programación de entrada %}
    Aquí decidirás cómo y cuándo tus usuarios entrarán en tu Canvas:
    - Programada: Esta es una entrada en Canvas basada en el tiempo
    - Basada en acciones: Tu usuario entrará en tu Canvas después de realizar una acción definida
    - Activada por API: Usa una solicitud de API para que los usuarios entren en tu Canvas

    Más información sobre el [paso Programación de entrada](#step-12-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Público objetivo %}
    Aquí seleccionarás tu público objetivo:
    - Crea tu audiencia añadiendo segmentos y filtros
    - Ajusta la reentrada en Canvas y los límites de entrada
    - Consulta un resumen de tu público objetivo

    Más información sobre el [paso Público objetivo](#step-13-set-your-target-entry-audience).
  {% endtab %}
  {% tab Configuración de envío %}
    Aquí seleccionarás la configuración de envío de tu Canvas:
    - Selecciona tu configuración de suscripción
    - Establece un límite de velocidad de envío para los mensajes de tu Canvas
    - Habilita y configura las horas tranquilas

    Más información sobre el [paso Configuración de envío](#step-14-select-your-send-settings).
  {% endtab %}
  {% tab Crear Canvas %}
    Aquí crearás tu Canvas.

    Aprende cómo [crear tu Canvas](#step-2-build-your-canvas) usando el creador de Canvas.
  {% endtab %}
  {% tab Resumen %}
    Aquí encontrarás el resumen de los detalles de tu Canvas. Si tienes activado el [flujo de trabajo de aprobación de Canvas]({{site.baseurl}}/user_guide/messaging/governance/approvals), puedes aprobar los detalles del Canvas listados antes de lanzarlo.

  {% endtab %}
{% endtabs %}

### Paso 1.1: Comienza con los aspectos básicos de tu Canvas {#step-11-start-with-your-canvas-basics}

Aquí nombrarás tu Canvas, asignarás [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y crearás o añadirás [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags). También puedes asignar eventos de conversión para el Canvas.

{% alert tip %}
Etiqueta tus Canvas para que sean fáciles de encontrar y para crear informes a partir de ellos. Por ejemplo, al usar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder), puedes filtrar por etiquetas específicas.
{% endalert %}

![La página de detalles del Canvas, con campos para el nombre del Canvas, descripción, ubicación y etiquetas.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

#### Elige los eventos de conversión {#choose-conversion-events}

Elige tu tipo de evento de conversión y luego selecciona las conversiones que deseas registrar. Estos [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) medirán la eficiencia de tu Canvas.

![Evento de conversión primaria A con el tipo de evento de conversión Realiza una compra para registrar conversaciones de usuarios que realizan cualquier compra dentro de un plazo de conversión de tres días.]({% image_buster /assets/img/add_canvas_conversions.png %})

Si tu Canvas tiene múltiples variantes o un grupo de control, Braze usará este evento de conversión para determinar la mejor variación para lograr este objetivo de conversión. Usando la misma lógica, puedes crear múltiples eventos de conversión.

### Paso 1.2: Determina la programación de entrada de tu Canvas {#step-12-determine-your-canvas-entry-schedule}

Puedes elegir una de tres formas en las que los usuarios pueden entrar en tu Canvas.

#### Tipos de programación de entrada {#entry-schedule-types}

{% tabs local %}
{% tab Entrega programada %}
Con la entrega programada, los usuarios entrarán según un horario, de manera similar a como programarías una Campaign. Puedes inscribir usuarios en un Canvas tan pronto como se lance, hacerlos entrar en tu recorrido en algún momento en el futuro, o de forma recurrente (diaria, semanal o mensual).

Si seleccionas una programación recurrente mensual, ten en cuenta que algunos meses pueden no tener el día seleccionado. Por ejemplo, supongamos que configuras un Canvas para enviarse mensualmente el día 31. En este escenario, Braze envía el último día de ese mes, como el 30 de abril, porque el 31 de abril no existe.

En este ejemplo, basándose en las opciones de tiempo, los usuarios entran en este Canvas cada martes a las 12 pm en su zona horaria local cada semana, comenzando el 14 de noviembre de 2025 hasta el 31 de diciembre de 2025.

![La página "Programación de entrada" con el tipo configurado como "Programada". Debido a la selección, se muestran opciones basadas en el tiempo, incluyendo frecuencia, hora de inicio, recurrencia, días y más.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})

Al usar la entrega en zona horaria local, Braze evalúa la elegibilidad de entrada dos veces: primero en la hora de Samoa (UTC+13) en el día programado, y nuevamente en la zona horaria local del usuario. Un usuario debe ser elegible en ambas comprobaciones para entrar en el Canvas. Si tus filtros de entrada usan ventanas de tiempo relativas (por ejemplo, "hace más de 2 días"), es posible que el período de 24 horas no haya transcurrido en el momento de la primera comprobación, lo que hace que los usuarios entren un día tarde. Para evitar esto, usa una ventana de tiempo más amplia, como al menos dos días. Para más detalles, consulta [¿Cuándo evalúa Braze a los usuarios para la entrega en zona horaria local?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery)
{% endtab %}
{% tab Entrega basada en acciones %}
Con la entrega basada en acciones, los usuarios entrarán en el Canvas y comenzarán a recibir mensajes cuando realicen acciones particulares, como abrir tu aplicación, realizar una compra o activar un evento personalizado.

Puedes controlar otros aspectos del comportamiento del Canvas desde la ventana **Público de entrada**, incluyendo reglas de reelegibilidad y configuración de limitación de frecuencia. Ten en cuenta que la entrega basada en acciones no está disponible para componentes de Canvas con mensajes dentro de la aplicación.

![Un ejemplo de entrega basada en acciones. Los usuarios entrarán en el Canvas si realizan una compra con una ventana de entrada que comienza a la 1:30 pm el 10 de junio de 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

{% alert note %}
**Interactuar con paso de Canvas** no está disponible como desencadenante de entrada basado en acciones para Canvas. Solo puede usarse como desencadenante para Campaigns. Para activar un Canvas desde otro, usa el componente de Canvas [Enviar a destino]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination), o crea un [webhook de Braze a Braze]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook#trigger-a-second-canvas-from-an-initial-canvas) que llame al endpoint `/canvas/trigger/send`.
{% endalert %}

{% alert important %}
Si tu Canvas basado en acciones envía mensajes antes de lo esperado, verifica que la marca de tiempo de tu evento personalizado se envíe con la hora actual en lugar de una hora retroactiva. Por ejemplo, si un Canvas basado en acciones tiene un retraso de tres horas después de que un usuario realiza un evento personalizado, Braze usa la marca de tiempo enviada con el evento personalizado para evaluar ese retraso. Si la marca de tiempo está retroactiva por más de tres horas, Braze trata el retraso como ya transcurrido y envía el mensaje inmediatamente.
{% endalert %}
{% endtab %}
{% tab Entrega activada por API %}
Con la entrega activada por API, los usuarios entrarán en tu Canvas y comenzarán a recibir mensajes después de haber sido añadidos usando el [endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) a través de la API. En el panel, puedes encontrar un ejemplo de solicitud cURL que hace esto, así como asignar [`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) opcional usando el [objeto de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context).

![Un ejemplo de entrega activada por API con un ID de Canvas y un ejemplo de solicitud cURL.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

Puedes usar los siguientes endpoints para la entrega activada por API:
- [POST: Enviar mensajes de Canvas mediante entrega activada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [POST: Programar Canvas activados por API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [POST: Actualizar Canvas programados activados por API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases)
{% endtab %}
{% endtabs %}

Después de seleccionar tu método de entrega, ajusta la configuración para que coincida con tu caso de uso y luego continúa configurando tu público objetivo.

{% details Comportamiento de deduplicación para Canvas que usan el editor original %}
Si la ventana de reelegibilidad es menor que la duración máxima del Canvas, se permitirá que un usuario vuelva a entrar y reciba los mensajes de más de un componente. En el caso límite en que la reentrada de un usuario alcance el mismo componente que su entrada anterior, Braze deduplicará los mensajes de ese componente.

Si un usuario vuelve a entrar en el Canvas, alcanza el mismo componente que su entrada anterior y es elegible para un mensaje dentro de la aplicación en cada entrada, el usuario recibirá el mensaje dos veces (dependiendo de la prioridad de los mensajes dentro de la aplicación) siempre que vuelva a abrir una sesión dos veces.
{% enddetails %}

### Paso 1.3: Configura tu público de entrada objetivo {#step-13-set-your-target-entry-audience}

Solo los usuarios que coincidan con tus criterios definidos podrán entrar en el recorrido en el paso **Público objetivo**, lo que significa que Braze evalúa la elegibilidad del público objetivo primero **antes** de que los usuarios entren en el recorrido del Canvas. Por ejemplo, si quieres dirigirte a usuarios nuevos, puedes seleccionar un segmento de usuarios que usaron tu aplicación por primera vez hace menos de una semana.

{% alert important %}
En espacios de trabajo con múltiples aplicaciones, la elegibilidad del público de entrada del Canvas (incluyendo segmentos y filtros) se evalúa solo cuando los usuarios entran en el Canvas, no en los pasos de mensaje individuales. Si tu espacio de trabajo tiene múltiples aplicaciones y necesitas asegurarte de que los pasos de mensaje se dirijan solo a usuarios de una aplicación específica, usa uno de los siguientes enfoques en cada paso de mensaje:
- Activa **Validar audiencia al enviar el mensaje** en las [validaciones de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) del paso de mensaje y añade segmentos o filtros específicos de la aplicación.
- Usa Liquid para verificar el dispositivo o la aplicación objetivo en el momento del envío.

Sin estas medidas de seguridad, los usuarios que calificaron para el recorrido en una aplicación pueden recibir mensajes destinados a otra aplicación si también usan otras aplicaciones en tu espacio de trabajo.
{% endalert %}

En **Controles de entrada**, puedes limitar el número de usuarios cada vez que el Canvas está programado para ejecutarse. Para Canvas basados en activación por API y basados en acciones, este límite se aplica cada hora UTC.

{% multi_lang_include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

#### Prueba tu audiencia {#testing-your-audience}

Después de añadir segmentos y filtros a tu público objetivo, puedes probar si tu audiencia está configurada como se espera [buscando un usuario]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para confirmar si coincide con los criterios de la audiencia.

![El campo "Búsqueda de usuario", que te permite buscar por ID de usuario externo o ID de Braze.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Selección de controles de entrada {#selecting-entry-controls}

Los controles de entrada determinan si los usuarios pueden volver a entrar en un Canvas. También puedes limitar el número de personas que potencialmente entrarían en este Canvas según una cadencia seleccionada dependiendo de tu tipo de programación de entrada:

- **Programada:** Duración del Canvas o cada vez que el Canvas está programado
- **Basada en acciones:** Por hora, diariamente o durante la duración del Canvas
- **Activada por API:** Por hora, diariamente o durante la duración del Canvas

Por ejemplo, si tienes un Canvas programado y seleccionas **Limitar volumen de entrada** y configuras el campo **Entradas máximas** a 500.000 usuarios con **Cada vez que el Canvas está programado** como cadencia de límite, entonces el Canvas solo envía a 500.000 usuarios por envío programado.

![La página "Controles de entrada" mostrando casillas de verificación para "Permitir a los usuarios volver a entrar en el Canvas" y "Limitar volumen de entrada".]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze no recomienda seleccionar **Cada vez que el Canvas está programado** para el calentamiento de IP, ya que esto puede llevar a un aumento en los volúmenes de envío.
{% endalert %}

#### Configuración de criterios de salida {#setting-exit-criteria}

Configurar los [criterios de salida]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) determina qué usuarios deseas que salgan de un Canvas. Si un usuario realiza el evento de excepción o coincide con los segmentos y filtros, no recibirá más mensajes.

#### Cálculo de la población objetivo {#calculating-target-population}

En la sección **Población objetivo**, puedes ver un resumen de tu audiencia, como tus segmentos seleccionados y filtros adicionales, y un desglose de cuántos usuarios son alcanzables por canal de mensajería. Para calcular el número exacto de usuarios alcanzables en tu público objetivo en lugar de la estimación predeterminada, selecciona [Calcular estadísticas exactas]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics).

Ten en cuenta que:

- Calcular estadísticas exactas puede tardar unos minutos en ejecutarse. Esta función solo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros.
- Mientras se cargan las estadísticas exactas, puede aparecer una estimación redondeada. La cifra exacta aparece en la sección **Usuarios alcanzables** cuando se carga. Puedes seleccionar **Mostrar estadísticas adicionales** para un desglose detallado.
- Para segmentos grandes, es normal ver ligeras variaciones incluso al calcular estadísticas exactas. Se espera que la precisión de esta función sea del 99,999 % o superior.

Para ver estadísticas adicionales, como los ingresos promedio de por vida de los usuarios objetivo, selecciona **Mostrar estadísticas adicionales**.

![Desglose de la población objetivo con opción para calcular estadísticas exactas.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

#### Por qué el recuento del público objetivo podría diferir del recuento de usuarios alcanzables {#why-the-target-audience-count-could-differ-from-the-reachable-users-count}

{% multi_lang_include audience/segments.md section='Differing audience size' %}

### Paso 1.4: Selecciona tu configuración de envío {#step-14-select-your-send-settings}

Selecciona **Configuración de envío** para editar tu configuración de suscripción, activar la limitación de velocidad y activar las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours). Al activar la [limitación de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting) o la [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping), puedes aliviar la presión de marketing sobre tus usuarios y asegurarte de que no les envías demasiados mensajes.

Para Canvas dirigidos a canales de correo electrónico y push, es posible que desees limitar tu Canvas para que solo los usuarios que hayan optado explícitamente por la adhesión voluntaria reciban el mensaje (excluyendo a los usuarios suscritos o que cancelaron su suscripción). Por ejemplo, supongamos que tienes tres usuarios con diferentes estados de adhesión voluntaria:

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

Para hacerlo, configura los **Ajustes de suscripción** para enviar este Canvas a "solo usuarios con adhesión voluntaria". Esta opción asegurará que solo los usuarios con adhesión voluntaria reciban tu correo electrónico, y Braze solo enviará tu push a los usuarios que tengan push habilitado de forma predeterminada.

Estos ajustes de suscripción se aplican paso a paso, lo que significa que no tienen efecto en el público de entrada. Por lo tanto, este ajuste se usa para evaluar la elegibilidad de un usuario para recibir cada paso del Canvas.

{% alert important %}
Con esta configuración, no incluyas ningún filtro en el paso **Público objetivo** que limite la audiencia a un solo canal (por ejemplo, `Foreground Push Enabled = True` o `Email Subscription = Opted-In`).
{% endalert %}

Puedes optar por especificar [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) (el tiempo durante el cual tus mensajes no se envían) para tu Canvas. Marca **Habilitar horas tranquilas** en tu **Configuración de envío**. Luego, selecciona tus horas tranquilas en la zona horaria local de tu usuario y si el mensaje debe cancelarse o enviarse en el siguiente horario disponible.

Cuando se selecciona **Enviar en el siguiente horario disponible**, las horas tranquilas suprimen el mensaje y lo envían en el siguiente horario disponible fuera de las horas tranquilas. Por ejemplo, supongamos que las horas tranquilas están configuradas para evitar que se envíen mensajes entre las 11:30 am y las 2:30 pm en la zona horaria local del usuario, y un usuario entra en un paso de mensaje a las 11:35 am. Debido a que esta hora está dentro de las horas tranquilas, el mensaje no se envía aún, y el usuario recibe el paso de mensaje a las 2:30 pm, que es después de las horas tranquilas.

![La página "Horas tranquilas" mostrando una casilla de verificación para habilitar las horas tranquilas. Si se habilita, se pueden configurar la hora de inicio, la hora de fin y el comportamiento alternativo.]({% image_buster /assets/img/quiet_hours.png %})

## Paso 2: Construye tu Canvas {#step-2-build-your-canvas}

{% alert tip %}
Ahorra tiempo y agiliza la creación de tu Canvas utilizando las [plantillas de Braze Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates). Explora nuestra biblioteca de plantillas prediseñadas para encontrar una que se ajuste a tu caso de uso y personalízala para satisfacer tus necesidades específicas. Para más información, consulta [Plantillas de Canvas]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates).
{% endalert %}

### Paso 2.1: Añade una variante {#step-21-add-a-variant}

![El botón "Añadir variante" seleccionado mostrando un menú contextual con la opción "Añadir variante".]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Selecciona **Añadir variante** y luego añade una nueva variante a tu Canvas. Las variantes representan un recorrido que seguirán tus usuarios y pueden contener múltiples pasos y ramas.

Puedes añadir variantes adicionales seleccionando el botón de suma <i class="fas fa-plus-circle"></i>. Cuando añadas nuevas variantes, podrás ajustar cómo se distribuirán tus usuarios entre ellas para que puedas comparar y analizar la eficacia de diferentes estrategias de participación.

![Dos variantes de ejemplo en un Braze Canvas.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
De forma predeterminada, la asignación de variantes en Canvas se determina mediante un hash determinista del ID de usuario y el ID de Canvas (no el [número de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) del usuario), lo que significa que un usuario dado se asigna de forma consistente a la misma variante al reingresar, siempre que los porcentajes de distribución de variantes permanezcan sin cambios. Si ajustas la distribución de variantes después del lanzamiento, los usuarios pueden ser asignados a variantes diferentes cuando reingresen al Canvas. <br><br>Si necesitas una asignación que permanezca fija cuando cambien los porcentajes de distribución, utiliza una sola variante en Canvas y dirige a los usuarios con un paso de [Rutas de Audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths). Al inicio del recorrido, utiliza un paso de [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) para almacenar un número aleatorio en un atributo personalizado y luego filtra por ese atributo en las Rutas de Audiencia.

{% details Expandir para ver los pasos %}

1. Crea un atributo personalizado de tipo **Número** para almacenar tu número aleatorio. Nómbralo con algo fácil de localizar, como `lottery_number` o `random_assignment`. En tu panel, ve a **Configuración de datos** > **Atributos personalizados**.<br><br>
2. Utiliza una sola variante en Canvas (o añade el mismo paso de Actualización de usuario a cada variante). Añade un paso de [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) al inicio del recorrido. Este paso genera y almacena el número aleatorio antes de que los usuarios lleguen a tu paso de Rutas de Audiencia.<br><br>
3. En el paso de Actualización de usuario, selecciona el [Editor JSON avanzado]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor). Utiliza la etiqueta {% raw %}{% random %}{% endraw %} para generar el número. Para más detalles, consulta [Enviar mensajes con un número aleatorio]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#send-messages-with-a-random-number). Por ejemplo, {% raw %}`{% random 10 %}`{% endraw %} devuelve un entero del 0 al 9. Establece el atributo personalizado del paso 1 usando JSON como este:<br><br>{% raw %}
```json
{% if {{custom_attribute.${lottery_number}}} == blank %}
{% capture lottery_number_str %}{% random 10 %}{% endcapture %}
{
  "attributes": [
    {
      "lottery_number": {{ lottery_number_str | plus: 0 }}
    }
  ]
}
{% endif %}
```
{% endraw %}
<br><br>
El bloque {% raw %}`{% if %}`{% endraw %} establece el número solo cuando el atributo está vacío, de modo que los usuarios mantienen la misma asignación cuando reingresan al Canvas.<br><br>

{: start="4"}
4. Añade un paso de [Rutas de Audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) después del paso de Actualización de usuario. En cada grupo de audiencia, añade filtros basados en tu atributo personalizado en lugar de usar porcentajes de distribución de variantes.<br><br>Por ejemplo, si usaste {% raw %}`{% random 10 %}`{% endraw %}, un grupo podría usar `lottery_number` **es menor que 4**, otro **es mayor que 3 y menor que 7**, y un tercero **es mayor que 6 y menor que 10**.

{% enddetails %}
{% endalert %}

### Paso 2.2: Añade pasos en Canvas {#step-22-add-canvas-steps}

Puedes añadir más pasos a tu flujo de trabajo en Canvas arrastrando y soltando componentes desde la barra lateral de **Componentes**. O selecciona el botón de suma <i class="fas fa-plus-circle"></i> para añadir un componente con el menú emergente.

{% alert tip %}
A medida que añadas más pasos, puedes cambiar el nivel de zoom para enfocarte en los detalles o ver el recorrido completo del usuario. Acerca con <kbd>Shift</kbd> + <kbd>+</kbd> o aleja con <kbd>Shift</kbd> + <kbd>-</kbd>.
{% endalert %}

![La ventana de búsqueda de componentes añadiendo un paso de demora al Braze Canvas.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Puedes añadir hasta 200 pasos en un Canvas. Si tu Canvas supera los 200 pasos, pueden ocurrir problemas de carga.
{% endalert %}

#### Duración máxima {#maximum-duration}

A medida que tu recorrido en Canvas aumenta en pasos, la duración máxima es el tiempo más largo posible que un usuario puede tardar en completar este Canvas. Se calcula sumando las demoras y las ventanas de activación de cada paso para cada variante en la ruta más larga. Por ejemplo, si tu Canvas tiene un paso de Demora con una demora de 3 días y un paso de Mensaje, la duración máxima de tu Canvas será de 3 días.

#### Editar un paso {#editing-a-step}

¿Quieres editar un paso en el recorrido de tu usuario? Consulta cómo hacerlo dependiendo de tu flujo de trabajo en Canvas.

Puedes editar cualquier paso en tu flujo de trabajo en Canvas seleccionando cualquiera de los componentes. Por ejemplo, supongamos que quieres editar tu primer paso, un componente de [Demora]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), en tu flujo de trabajo para un día específico. Selecciona el paso para ver su configuración y ajusta tu demora al 1 de marzo. Esto significa que el 1 de marzo, tus usuarios avanzarán al siguiente paso en tu Canvas.

![Un ejemplo de paso "Demora" con la demora configurada en "Hasta un día específico".]({% image_buster /assets/img_archive/edit_delay_flow.png %})

O puedes editar y ajustar rápidamente la **Configuración de acción** de tu paso de [Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) para mantener a los usuarios durante un período de tiempo. Esto prioriza su siguiente ruta en función de las acciones durante este período de evaluación.

![El segundo paso en el Canvas, "Configuración de acción", con una ventana de evaluación configurada en 1 día.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Los componentes ligeros en Canvas permiten una experiencia de edición sencilla, por lo que ajustar los detalles más específicos de tu Canvas es más fácil.

#### Mensajes en Canvas {#messages-in-canvas}

Edita los mensajes en un componente de Canvas para controlar los mensajes que un paso en particular enviará. Canvas puede enviar correos electrónicos, mensajes push para móvil y web, y webhooks para integrarse con otros sistemas. De forma similar a Campaigns, puedes usar ciertas plantillas de [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) para personalizar tus mensajes.

{% alert tip %}
¿Sabías que puedes incluir nombres de componentes de Canvas en tus mensajes y plantillas de enlaces?<br>
Usa la etiqueta de Liquid `campaign.${name}` en Canvas para mostrar el nombre del componente de Canvas actual.
{% endalert %}

El componente de Mensaje gestiona los mensajes enviados a los usuarios. Puedes seleccionar tus **Canales de mensajería** y ajustar la **Configuración de entrega** para optimizar la mensajería de tu Canvas. Para más detalles sobre este componente, consulta [Mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

![El paso "Configurar mensajes", con "Canales de mensajería" seleccionado, que muestra la lista de canales de mensajería disponibles, como push de Android, Content Cards, correo electrónico y más.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Selecciona **Listo** después de haber terminado de configurar tu componente de Canvas.

{% tabs local %}
{% tab Propiedades de entrada de Canvas %}

El [objeto `context`]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) se configura en el paso de **Programación de entrada** al crear un Canvas e indica el desencadenante que hace que un usuario ingrese a un Canvas. Estas propiedades también pueden acceder a las propiedades de las cargas útiles de entrada en Canvas activados por API. Ten en cuenta que el objeto `context` puede tener hasta 50 KB.

Usa el siguiente Liquid cuando hagas referencia a estas propiedades creadas al ingresar al Canvas: {% raw %} ``context.${property_name}`` {% endraw %}. Ten en cuenta que los eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta manera.

{% raw %}
Por ejemplo, considera la siguiente solicitud: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`. Podrías añadir la palabra "shoes" a un mensaje con este Liquid ``{{context.${product_name}}}``.
{% endraw %}

{% endtab %}

{% tab Propiedades de evento %}
Las propiedades de evento son las propiedades que tú estableces en eventos personalizados y compras. Estas `event_properties` pueden usarse en Campaigns con entrega basada en acciones, así como en Canvas.

En Canvas, las propiedades de eventos personalizados y eventos de compra pueden usarse en Liquid en cualquier paso de Mensaje que siga a un paso de Rutas de Acción. Usa este Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} cuando hagas referencia a estas `event_properties`. Estos eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta manera en el componente de Mensaje.

En el primer paso de Mensaje que sigue a una Ruta de Acción, puedes usar `event_properties` relacionadas con el evento referenciado en esa Ruta de Acción. Puedes tener otros pasos (que no sean otro paso de Rutas de Acción o de Mensaje) entre este paso de Rutas de Acción y el paso de Mensaje. Ten en cuenta que solo tendrás acceso a `event_properties` si tu paso de Mensaje puede rastrearse hasta una ruta que no sea la de Todos los demás en un paso de Ruta de Acción.

{% endtab %}
{% endtabs %}

### Paso 2.3: Edita las conexiones {#step-23-edit-connections}

Para mover una conexión entre pasos, selecciona la flecha que conecta los dos componentes y selecciona un componente diferente. Para eliminar la conexión, selecciona la flecha seguida de **Cancelar conexión** en el pie del creador de Canvas.

Si una sola variante tiene múltiples ramas con la misma audiencia y hora de envío, Braze no garantiza una división equitativa entre esas ramas. La distribución puede favorecer la rama que se creó primero. Para una división equitativa, usa filtros de [Número de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) en cada rama. Para más información, consulta [¿Qué sucede si la audiencia y la hora de envío son idénticas para un Canvas que tiene una variante, pero múltiples ramas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches).

## Paso 3: Añadir un grupo de control {#step-3-add-a-control-group}

Puedes añadir un grupo de control a tu Canvas seleccionando el botón <i class="fas fa-plus-circle"></i> de más para añadir una nueva variante.

Braze realizará un seguimiento de las conversiones de los usuarios que se coloquen en el grupo de control, aunque no recibirán ningún mensaje. Para preservar una prueba precisa, realizaremos un seguimiento del número de conversiones de tus variantes y del grupo de control durante exactamente la misma cantidad de tiempo, como se muestra en la pantalla de selección de eventos de conversión.

Puedes ajustar la distribución entre tus mensajes haciendo doble clic en los encabezados de **Nombre de variante**.

En este ejemplo, tenemos nuestro Canvas dividido en dos variantes. La variante 1 tiene el 70% de los usuarios. La segunda variante es un grupo de control con el 30% restante de los usuarios.

![Un ejemplo de variante en un Canvas de Braze, donde el 70% va a la "Variante 1", que tiene una demora de 1 día en el primer paso y luego envía un mensaje en el segundo paso. El otro 30% va a un "Control" que no tiene pasos de seguimiento.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

### Selección inteligente para Canvas {#intelligent-selection-for-canvas}

Las capacidades de selección inteligente están ahora disponibles dentro de Canvas multivariantes. De forma similar a la característica de [selección inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) para Campaigns multivariantes, la selección inteligente para Canvas analiza el rendimiento de cada variante en Canvas y ajusta el porcentaje de usuarios que se canalizan a través de cada variante. Esta distribución se basa en las métricas de rendimiento de cada variante para maximizar el número total esperado de conversiones.

Ten en cuenta que los Canvas multivariantes te permiten probar no solo el texto, sino también el momento y los canales. A través de la selección inteligente, puedes probar Canvas de manera más eficiente y tener la confianza de que tus usuarios serán enviados por el mejor recorrido posible en Canvas.

![La opción "Selección inteligente" está habilitada en la página "Editar distribución de variantes". A medida que analiza y optimiza el Canvas, muestra una barra horizontal a lo largo de la página dividida en varias secciones, cada una con diferente color y tamaño. Esto es solo una representación visual y no se correlaciona con ningún análisis específico.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

La selección inteligente para Canvas optimiza los resultados de tu Canvas realizando ajustes graduales en tiempo real a la distribución de usuarios asignados a cada variante. Cuando el algoritmo estadístico determina un ganador decisivo entre tus variantes, descartará las variantes con bajo rendimiento y asignará a todos los futuros destinatarios elegibles del Canvas a las variantes ganadoras.

Por esta razón, la selección inteligente funciona mejor en Canvas que tienen nuevos usuarios entrando con frecuencia.

## Paso 4: Guardar y lanzar {#step-4-save-and-launch}

Cuando hayas terminado de crear tu Canvas, selecciona **Lanzar Canvas** para guardar y lanzar tu Canvas. Después de lanzar tu Canvas, podrás ver los análisis de tu recorrido a medida que lleguen en la página **Detalles de Canvas**.

También puedes guardar tu Canvas como borrador si necesitas volver a él.

![Un ejemplo de Canvas en Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
¿Necesitas hacer cambios en tu Canvas después del lanzamiento? ¡Puedes hacerlo! Consulta [Editar Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits) para más información.
{% endalert %}