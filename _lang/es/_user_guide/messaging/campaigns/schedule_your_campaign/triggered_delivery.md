---
nav_title: Entrega basada en acciones
article_title: Entrega basada en acciones
page_order: 1
page_type: reference
description: "Este artículo de referencia describe cómo desencadenar campañas para que se envíen después de que un usuario complete un evento determinado."
tool: Campaigns
local_redirect:
  use-cases: '/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#examples'

---

# Entrega basada en acciones {#action-based-delivery}

> Las campañas de entrega basada en acciones o campañas desencadenadas por eventos son muy eficaces para mensajes transaccionales o basados en logros. En lugar de enviar tu campaña en días determinados, puedes desencadenarlas para que se envíen después de que un usuario complete un evento determinado.

## Configuración de una campaña desencadenada {#setting-up-a-triggered-campaign}

### Paso 1: Selecciona un evento desencadenante {#step-1-select-a-trigger-event}

Selecciona un evento desencadenante. Los eventos están organizados por categoría y están disponibles en función de tu espacio de trabajo y los canales habilitados.

- **eCommerce**
    - **Place Order**
    - **Perform Cart Updated Event**
    - **Perform Checkout Started Event**
    - **Perform Checkout Completed Event**
    - **Make Purchase**
- **Actividad general**
    - **Interact With Campaign**
    - **Interact With Step**
    - **Interact with Landing Page**
    - **Perform Conversion Event**
    - **Perform Custom Event**
    - **Perform Exception Event For Campaign**
    - **Start Session**
- **Mensajería entrante**
    - **Send an servicio de mensajes cortos inbound message**
    - **Send a WhatsApp inbound message**
    - **Send a LINE inbound message**
- **Ubicación**
    - **Enter a Location**
    - **Trigger a Geofence**
- **Actualizaciones de perfil**
    - **Add an Email Address**
    - **Change Custom Attribute Value**
    - **Update Subscription Status**
    - **Update Subscription Group Status**

El grupo **eCommerce** también muestra eventos de eCommerce recomendados, como **Perform Product Viewed Event**, **Perform Order Cancelled Event** y **Perform Order Refunded Event**. Estas opciones utilizan **Perform Custom Event** con el nombre del evento ya rellenado.

Las campañas de mensajes dentro de la aplicación admiten un conjunto más reducido de desencadenantes: **Make Purchase**, **Place Order**, **Start Session**, **Perform Custom Event** e **Interact With Campaign**. Para las campañas de mensajes dentro de la aplicación, **Interact With Campaign** solo cubre la apertura de una push de cualquier campaña o de una campaña específica. No incluye la siguiente lista de interacciones de campaña.

Para campañas que no sean de mensajes dentro de la aplicación, cuando selecciones **Interact With Campaign**, **Interact With Step** o **Interact with Landing Page**, elige la interacción sobre la que desencadenar. Cada uno de estos desencadenantes ofrece sus propias interacciones, y las interacciones disponibles dependen de los canales que tengas habilitados.

{% details Interacciones para Interact With Campaign %}

- **Ver mensaje dentro de la aplicación**
- **Hacer clic en mensaje dentro de la aplicación**
- **Hacer clic en botón 1 de mensaje dentro de la aplicación**
- **Hacer clic en botón 2 de mensaje dentro de la aplicación**
- **Enviar cuestionario de mensaje dentro de la aplicación**
- **Hacer clic en correo electrónico**
- **Abrir correo electrónico**
- **Abrir correo electrónico (aperturas automáticas)**
- **Abrir correo electrónico (otras aperturas)**
- **Hacer clic en alias en correo electrónico**
- **Hacer clic en alias en cualquier campaña o paso en Canvas**
- **Abrir directamente notificación push**
- **Hacer clic en botón de notificación push**
- **Hacer clic en página de historias push**
- **Realizar evento de conversión**
- **Recibir correo electrónico**
- **Recibir notificación push**
- **Recibir webhook**
- **Recibir servicio de mensajes cortos**
- **Hacer clic en enlace acortado de servicio de mensajes cortos**
- **Ver tarjeta de contenido**
- **Hacer clic en tarjeta de contenido**
- **Descartar tarjeta de contenido**
- **Ver banner**
- **Hacer clic en banner**
- **Descartar banner**
- **Hacer clic en enlace rastreado de WhatsApp**
- **Hacer clic en enlace rastreado de LINE**
- **Hacer clic en enlace rastreado de KakaoTalk**
- **Estar inscrito en un grupo de control**

{% enddetails %}

{% details Interacciones para Interact With Step %}

- **Ver mensaje dentro de la aplicación**
- **Iniciar ventana de disponibilidad de mensaje dentro de la aplicación**
- **Enviar cuestionario de mensaje dentro de la aplicación**
- **Hacer clic en correo electrónico**
- **Abrir correo electrónico**
- **Abrir correo electrónico (aperturas automáticas)**
- **Abrir correo electrónico (otras aperturas)**
- **Hacer clic en alias en correo electrónico**
- **Hacer clic en alias en cualquier campaña o paso en Canvas**
- **Abrir directamente notificación push**
- **Hacer clic en botón de notificación push**
- **Hacer clic en página de historias push**
- **Recibir correo electrónico**
- **Recibir notificación push**
- **Recibir webhook**
- **Recibir servicio de mensajes cortos**
- **Hacer clic en enlace acortado de servicio de mensajes cortos**
- **Ver tarjeta de contenido**
- **Hacer clic en tarjeta de contenido**
- **Descartar tarjeta de contenido**
- **Ver banner**
- **Hacer clic en banner**
- **Descartar banner**
- **Hacer clic en enlace rastreado de WhatsApp**
- **Hacer clic en enlace rastreado de LINE**
- **Hacer clic en enlace rastreado de KakaoTalk**

{% enddetails %}

{% details Interacciones para Interact with Landing Page %}

- **Enviar formulario**
- **Enviar cuestionario**

{% enddetails %}

También puedes filtrar aún más los eventos desencadenantes mediante las [propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) de Braze, que permiten personalizar las propiedades de evento para eventos personalizados y compras dentro de la aplicación. Esta característica te permite acotar aún más qué usuarios reciben un mensaje en función de los atributos específicos del evento personalizado, lo que permite una mayor personalización de la campaña y una recopilación de datos más sofisticada.

Por ejemplo, supongamos que tenemos una campaña con un evento personalizado de carrito abandonado que se filtra adicionalmente por la propiedad "valor del carrito". Esta campaña solo alcanza a usuarios que hayan dejado entre $100 y $200 en productos en sus carritos.

![Campaña de carrito abandonado filtrada por una propiedad de evento personalizado para un valor de carrito entre $100 y $200.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
El evento desencadenante **Start Session** puede ser la primera apertura de la aplicación del usuario si el Segment de tu campaña aplica a usuarios nuevos (por ejemplo, si tu Segment está formado por aquellos sin sesiones).
{% endalert %}

Ten en cuenta que aún puedes enviar una campaña desencadenada a un Segment específico de usuarios, de modo que los usuarios que no formen parte del Segment no recibirán la campaña aunque completen el evento desencadenante.

Respecto al evento desencadenante de cuando un usuario añade una dirección de correo electrónico a su perfil, se aplican las siguientes reglas:

- El evento desencadenante se activa después de que el atributo del perfil de usuario se actualice. Esto significa que la evaluación de los Segments y filtros de la campaña ocurre después de cualquier actualización de atributos. Esto resulta beneficioso porque te permite configurar filtros como "la dirección de correo electrónico coincide con gmail.com" para crear una campaña desencadenada que solo envíe a usuarios de Gmail y se active en cuanto añadan su dirección de correo electrónico.
- El evento desencadenante se activa cuando se añade una dirección de correo electrónico a un perfil de usuario. Si tienes varios perfiles de usuario creados con la misma dirección de correo electrónico, la campaña puede activarse varias veces, una por cada perfil de usuario.

Además, los mensajes dentro de la aplicación desencadenados siguen respetando las reglas de entrega de mensajes dentro de la aplicación y aparecen al comienzo de una sesión de la aplicación.

### Paso 2: Selecciona la duración del retraso {#step-2-select-delay-length}

Selecciona cuánto tiempo esperar antes de enviar la campaña después de que se cumplan los criterios de desencadenamiento. Si la duración del retraso elegida es mayor que la duración del mensaje para su envío, ningún usuario recibirá la campaña.

Las campañas de mensajes dentro de la aplicación pueden retrasar la entrega después del evento desencadenante hasta dos horas (7200 segundos). Las opciones de retraso son **Inmediatamente** y **Después de un retraso**. Para una espera más larga, añade un paso de [Retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) antes de un paso de mensaje dentro de la aplicación en un Canvas.

{% alert important %}
Braze utiliza la marca de tiempo enviada con el evento personalizado para evaluar el retraso de una campaña basada en acciones. Si esa marca de tiempo tiene fecha retroactiva, Braze puede considerar que el retraso ya ha transcurrido y enviar el mensaje de inmediato o antes de lo esperado. Para evitar problemas con el momento de la entrega, envía la marca de tiempo del evento personalizado con la hora actual.
{% endalert %}

Además, los usuarios que completen el evento desencadenante después de que se lance tu campaña serán los primeros en recibir el mensaje una vez transcurrido el retraso. Los usuarios que completaron el evento desencadenante antes del lanzamiento de la campaña no califican para recibirla.

También puedes enviar la campaña en un día específico de la semana seleccionando **El siguiente día de la semana**, o un número determinado de días en el futuro seleccionando **Después de un número de días naturales**. Alternativamente, puedes enviar tu mensaje usando [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) en lugar de seleccionar manualmente una hora de entrega.

### Paso 3: Selecciona eventos de excepción {#step-3-select-exception-events}

Selecciona un evento de excepción que descalifique a los usuarios para recibir esta campaña. Solo puedes hacer esto si tu mensaje desencadenado se envía después de un retraso. Los [eventos de excepción]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) pueden ser realizar una compra, iniciar una sesión, realizar uno de los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) designados de una campaña o realizar un evento personalizado.

Si un usuario completa el evento desencadenante pero luego completa tu evento de excepción antes de que se envíe el mensaje debido al retraso, no recibirá la campaña. Los usuarios que no reciban la campaña debido al evento de excepción son automáticamente elegibles para recibirla en el futuro, la próxima vez que completen el evento desencadenante, incluso si no eliges que los usuarios vuelvan a ser [reelegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

Para más información sobre el uso de eventos de excepción, consulta [Ejemplos](#examples).

Si envías una campaña con un evento desencadenante que coincide con el evento de excepción, Braze cancela la campaña y reprograma automáticamente una nueva campaña basada en la hora de entrega del mensaje del evento de excepción. Por ejemplo, si tu primer evento desencadenante comienza a los cinco minutos y el evento de excepción comienza a los 10 minutos, te basarás en los 10 minutos del evento de excepción como la hora oficial de entrega del mensaje de la campaña.

{% alert note %}
No puedes hacer que "inicio de sesión" sea a la vez el evento desencadenante y el evento de excepción de una campaña. Sin embargo, siempre tienes la opción de seleccionar cualquier otro evento personalizado fuera de esta opción.
{% endalert %}

### Paso 4: Asigna la duración {#step-4-assign-duration}

Asigna la duración de la campaña especificando una hora de inicio y una hora de finalización opcional.

Si un usuario completa un evento desencadenante durante el periodo especificado pero califica para el mensaje fuera de ese periodo debido a un retraso programado, entonces no recibirá la campaña. Por lo tanto, si estableces un retraso mayor que el periodo del mensaje, ningún usuario recibirá tu campaña. Además, puedes elegir enviar el mensaje en las [zonas horarias locales]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) de los usuarios.

### Paso 5: Selecciona el periodo de tiempo {#step-5-select-time-frame}

Selecciona si el usuario recibe la campaña durante una porción específica del día. Si le das al mensaje un periodo de tiempo y el usuario completa el evento desencadenante fuera de ese periodo, o el retraso del mensaje hace que pierda el periodo, entonces, de forma predeterminada, el usuario no recibe tu mensaje.

En el caso de que un usuario complete el evento desencadenante dentro del periodo de tiempo, pero el retraso del mensaje haga que el usuario quede fuera del periodo, puedes seleccionar la casilla **Enviar en el siguiente horario disponible si el momento de entrega queda fuera de la porción del día especificada** para que estos usuarios sigan recibiendo la campaña.

Si un usuario no recibe el mensaje porque pierde el periodo de tiempo, seguirá siendo elegible para recibirlo la próxima vez que complete el evento desencadenante, incluso si no elegiste que los usuarios vuelvan a ser [reelegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility). Si eliges que los usuarios vuelvan a ser reelegibles, entonces los usuarios pueden recibir la campaña cada vez que completen el evento desencadenante, siempre que califiquen dentro del periodo de tiempo especificado.

Si también has asignado a la campaña una duración determinada, entonces el usuario debe calificar tanto dentro de la duración como dentro de la porción específica del día para recibir el mensaje.

### Paso 6: Determina la reelegibilidad {#step-6-determine-re-eligibility}

Determina si los usuarios pueden volver a ser [reelegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) para la campaña. Si permites que los usuarios vuelvan a ser reelegibles, puedes especificar un retraso antes de que el usuario pueda recibir la campaña nuevamente. Esto evita que tus campañas desencadenadas se vuelvan demasiado repetitivas.

## Ejemplos {#examples}

Las campañas desencadenadas son muy eficaces para mensajes transaccionales o basados en logros.

Las campañas transaccionales incluyen mensajes que se envían después de que el usuario completa una compra o añade un artículo a su carrito. Este último caso es un gran ejemplo de una campaña que se beneficia de un evento de excepción. Supón que tu campaña recuerda a los usuarios los artículos en su carrito que no han comprado. El evento de excepción, en este caso, es que el usuario compre los productos de su carrito. Para campañas basadas en logros, puedes enviar un mensaje cinco minutos después de que el usuario complete una conversión o supere un nivel de juego.

Además, al crear campañas de bienvenida, puedes desencadenar mensajes para que se envíen después de que el usuario se registre o configure una cuenta. Escalonar los mensajes para que se envíen en diferentes días tras el registro te permite crear un proceso de incorporación completo.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuál es el retraso máximo después de un desencadenante para campañas de mensajes dentro de la aplicación? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

Dos horas (7200 segundos). Para ver las opciones de retraso disponibles y cómo configurar una espera más larga, consulta [Paso 2: Seleccionar la duración del retraso](#step-2-select-delay-length).

### ¿Por qué un usuario no recibió mi Campaign desencadenada? {#why-did-a-user-not-receive-my-triggered-campaign}

Cualquiera de estas situaciones impide que un usuario que ha completado el evento desencadenante reciba la Campaign:

- El usuario completó el evento de excepción antes de que el tiempo de retraso transcurriera por completo.
- Se utilizó la [lógica de `abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) de Liquid y el mensaje fue abortado según la lógica o las reglas de `abort_message`.
- El tiempo de retraso provocó que el usuario se cualificara para recibir la Campaign después de que la duración hubiera finalizado.
- El tiempo de retraso provocó que el usuario se cualificara para recibir la Campaign fuera de la franja horaria especificada del día.
- El usuario ya recibió la Campaign (incluida la atribución a través de identificadores de canal compartidos, por ejemplo, si comparte un correo electrónico con alguien que lo recibió, abrió o hizo clic), y los usuarios no vuelven a ser elegibles.
- Aunque los usuarios son reelegibles para recibir la Campaign, solo pueden volver a desencadenarla después de cierto periodo de tiempo, y ese periodo aún no ha transcurrido.

[Segmentar]({{site.baseurl}}/user_guide/audience/segments) una Campaign desencadenada en función de datos de usuario registrados en el momento del evento puede provocar una [condición de carrera]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions). Esto ocurre cuando el atributo de usuario en el que se segmenta la Campaign se modifica, pero el cambio no se ha procesado para el usuario en el momento en que se envía la Campaign. Como las campañas comprueban la pertenencia a Segments en la entrada, esto puede provocar que el usuario no reciba la Campaign.

Por ejemplo, imagina que quieres enviar una Campaign desencadenada por un evento a usuarios masculinos que acaban de registrarse. Cuando el usuario se registra, registras un evento personalizado `registration` y simultáneamente estableces el atributo `gender` del usuario. El evento puede desencadenar la Campaign antes de que Braze haya procesado el género del usuario, lo que impide que reciba la Campaign.

Como práctica recomendada, asegúrate de que el atributo en el que se segmenta la Campaign se envíe a los servidores de Braze antes del evento. Si esto no es posible, la mejor manera de garantizar la entrega es usar [propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) para adjuntar las propiedades de usuario relevantes al evento y aplicar un filtro de propiedades para la propiedad del evento específica en lugar de un filtro de segmentación. Para nuestro ejemplo, agrega una propiedad `gender` al evento personalizado `registration` para que Braze tenga garantizados los datos que necesitas cuando se desencadene tu Campaign.

Además, si una Campaign se basa en acciones y tiene un retraso, puedes activar la opción **Reevaluar la pertenencia a Segments en el momento de envío** para asegurarte de que los usuarios sigan formando parte del público objetivo cuando se envíe el mensaje.

#### Evaluación de los criterios de audiencia {#audience-criteria-evaluation}

Para campañas que implican un retraso antes del envío (incluidos los límites de velocidad, la zona horaria local, la sincronización inteligente o una programación de desencadenante), el momento en que se reevalúa el Segment depende del tipo y la configuración de la Campaign.

En las campañas basadas en acciones con retraso, si seleccionas **Reevaluar la pertenencia a Segments en el momento de envío**, los usuarios se reevalúan antes de que se envíe el mensaje, por lo que solo los usuarios que aún cumplen los criterios del Segment en el momento del envío reciben el mensaje.

Si tu Campaign se desencadena con un evento personalizado específico y seleccionas un Segment como audiencia, los usuarios deben realizar el mismo evento personalizado para ser incluidos en el Segment. Esto significa que los usuarios necesitan formar parte de la audiencia antes de que una Campaign basada en acciones pueda desencadenarse. El flujo de trabajo general para una Campaign desencadenada es el siguiente:

1. **Unirse a la audiencia:** cuando un usuario realiza el evento personalizado, se añade al público objetivo de la Campaign.
2. **Desencadenar el correo electrónico:** el usuario debe realizar el evento personalizado de nuevo para desencadenar el correo electrónico, ya que necesita formar parte de la audiencia antes de que se pueda enviar el correo electrónico.

Recomendamos cambiar el público objetivo para incluir a todos los usuarios, o verificar que los usuarios que se espera que realicen el evento ya formen parte de la audiencia de la Campaign para que el mensaje pueda desencadenarse.

![Captura de pantalla relacionada con la evaluación de criterios de audiencia.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### Solución de problemas de eventos personalizados {#troubleshooting-custom-events}

Primero, confirma que el evento personalizado se está pasando a Braze. Ve a **Analytics** > **Informe de eventos personalizados** y selecciona el evento personalizado correspondiente y el rango de fechas. Si el evento no aparece, confirma que esté configurado correctamente y que el usuario haya realizado la acción correcta.

Si el evento personalizado aparece, continúa con la solución de problemas haciendo lo siguiente:

- Revisa la descarga del perfil de usuario para confirmar que hayan desencadenado el evento y cuándo lo hicieron. Si el evento se desencadenó, compara la marca de tiempo del momento en que se desencadenó el evento con la hora en que la Campaign se activó. El evento puede haberse desencadenado antes de que la Campaign estuviera activa.
- Revisa los registros de cambios de la Campaign y de los Segments utilizados en la segmentación para determinar si el usuario estaba en el Segment cuando se desencadenó su evento personalizado. Si no estaba en el Segment, no habría recibido la Campaign.
- Verifica si el usuario fue incluido en un grupo de control a través de la segmentación y, en consecuencia, se le impidió recibir la Campaign.
- Si hay un retraso programado, verifica si el evento personalizado del usuario se desencadenó antes del retraso. Si el evento se desencadenó antes del retraso, no habría recibido la Campaign.

{% alert note %}
Los mensajes dentro de la aplicación solo se pueden desencadenar mediante eventos enviados a través del SDK or kit de desarrollo de software, no a través de la REST or transferencia de estado representacional API.
{% endalert %}

### ¿Cuándo evalúan las campañas basadas en acciones la pertenencia a la audiencia? {#when-do-action-based-campaigns-evaluate-audience-membership}

Braze evalúa la pertenencia a la audiencia cuando procesa el evento desencadenante, antes de que se envíe el mensaje. De forma predeterminada, Braze verifica si el usuario coincide con el público objetivo en el momento de la puesta en cola. Si la Campaign tiene un retraso, puedes seleccionar **Reevaluar la pertenencia a Segments en el momento de envío** para verificar los criterios de audiencia nuevamente inmediatamente antes del envío, por ejemplo, cuando un usuario podría realizar la acción desencadenante y luego salir de la audiencia antes de que se complete el envío.

Para obtener más información, consulta [Evaluación de los criterios de audiencia](#audience-criteria-evaluation).