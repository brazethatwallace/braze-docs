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

## Configurar una campaña desencadenada {#setting-up-a-triggered-campaign}

### Paso 1: Seleccionar un evento desencadenante {#step-1-select-a-trigger-event}

Selecciona un evento desencadenante. Los eventos están organizados por categoría y están disponibles dependiendo de tu espacio de trabajo y los canales habilitados.

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
    - **Send an SMS inbound message**
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

El grupo **eCommerce** también muestra eventos de eCommerce recomendados, como **Perform Product Viewed Event**, **Perform Order Cancelled Event** y **Perform Order Refunded Event**. Estas opciones usan **Perform Custom Event** con el nombre del evento precargado.

Las campañas de mensajes dentro de la aplicación admiten un conjunto más reducido de desencadenantes: **Make Purchase**, **Place Order**, **Start Session**, **Perform Custom Event** e **Interact With Campaign**. Para las campañas de mensajes dentro de la aplicación, **Interact With Campaign** solo abarca la apertura de una notificación push de cualquier campaña o de una campaña específica. No incluye la siguiente lista de interacciones de campaña.

Para campañas que no sean de mensajes dentro de la aplicación, cuando selecciones **Interact With Campaign**, **Interact With Step** o **Interact with Landing Page**, elige la interacción que activará el desencadenante. Cada uno de estos desencadenantes ofrece sus propias interacciones, y las interacciones disponibles dependen de los canales que tengas habilitados.

{% details Interacciones para Interact With Campaign %}

- **Ver mensaje dentro de la aplicación**
- **Hacer clic en mensaje dentro de la aplicación**
- **Hacer clic en botón 1 de mensaje dentro de la aplicación**
- **Hacer clic en botón 2 de mensaje dentro de la aplicación**
- **Enviar cuestionario de mensaje dentro de la aplicación**
- **Hacer clic en correo electrónico**
- **Abrir correo electrónico**
- **Abrir correo electrónico (aperturas de máquina)**
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
- **Recibir SMS**
- **Hacer clic en enlace acortado de SMS**
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
- **Abrir correo electrónico (aperturas de máquina)**
- **Abrir correo electrónico (otras aperturas)**
- **Hacer clic en alias en correo electrónico**
- **Hacer clic en alias en cualquier campaña o paso en Canvas**
- **Abrir directamente notificación push**
- **Hacer clic en botón de notificación push**
- **Hacer clic en página de historias push**
- **Recibir correo electrónico**
- **Recibir notificación push**
- **Recibir webhook**
- **Recibir SMS**
- **Hacer clic en enlace acortado de SMS**
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

También puedes filtrar aún más los eventos desencadenantes a través de las [propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) de Braze, lo que permite propiedades de eventos personalizables para eventos personalizados y compras dentro de la aplicación. Esta característica te permite refinar qué usuarios reciben un mensaje en función de los atributos específicos del evento personalizado, lo que posibilita una mayor personalización de la campaña y una recopilación de datos más sofisticada.

Por ejemplo, supongamos que tenemos una campaña con un evento personalizado de carrito abandonado que se segmenta aún más con el filtro de propiedad "valor del carrito". Esta campaña solo llega a los usuarios que dejaron entre $100 y $200 en productos en sus carritos.

![Campaña de carrito abandonado filtrada por una propiedad de evento personalizado para un valor de carrito entre $100 y $200.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
El evento desencadenante **Start Session** puede ser la primera apertura de la aplicación del usuario si el Segment de tu campaña aplica a usuarios nuevos (por ejemplo, si tu Segment está compuesto por aquellos sin sesiones).
{% endalert %}

Ten en cuenta que aún puedes enviar una campaña desencadenada a un Segment específico de usuarios, de modo que los usuarios que no formen parte del Segment no reciban la campaña aunque completen el evento desencadenante.

Con respecto al evento desencadenante de cuando un usuario agrega una dirección de correo electrónico a su perfil, aplican las siguientes reglas:

- El evento desencadenante se activa después de que se actualiza el atributo del perfil de usuario. Esto significa que la evaluación de los Segments y filtros de la campaña ocurre después de cualquier actualización de atributos. Esto es beneficioso porque te permite configurar filtros como "la dirección de correo electrónico coincide con gmail.com" para crear una campaña desencadenada que solo envíe a usuarios de Gmail y se active tan pronto como agreguen su dirección de correo electrónico.
- El evento desencadenante se activa cuando se agrega una dirección de correo electrónico a un perfil de usuario. Si tienes varios perfiles de usuario que creaste con la misma dirección de correo electrónico, la campaña puede activarse varias veces, una vez por cada perfil de usuario.

Además, los mensajes dentro de la aplicación desencadenados siguen respetando las reglas de entrega de mensajes dentro de la aplicación y aparecen al comienzo de una sesión de la aplicación.

### Paso 2: Seleccionar la duración del retraso {#step-2-select-delay-length}

Selecciona cuánto tiempo esperar antes de enviar la campaña una vez que se cumplan los criterios del desencadenante. Si la duración del retraso elegida es mayor que la duración del mensaje para el envío, ningún usuario recibirá la campaña.

Las campañas de mensajes dentro de la aplicación pueden retrasar la entrega después del evento desencadenante hasta dos horas (7200 segundos). Las opciones de retraso son **Inmediatamente** y **Después de un retraso**. Para una espera más prolongada, agrega un paso de [Retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) antes de un paso de mensaje dentro de la aplicación en un Canvas.

{% alert important %}
Braze usa la marca de tiempo enviada con el evento personalizado para evaluar el retraso de una campaña basada en acciones. Si esa marca de tiempo está antedatada, Braze puede tratar el retraso como ya transcurrido y enviar el mensaje de inmediato o antes de lo esperado. Para evitar problemas de sincronización en la entrega, envía la marca de tiempo del evento personalizado con la hora actual.
{% endalert %}

Además, los usuarios que completen el evento desencadenante después de que se lance tu campaña serán los primeros en recibir el mensaje una vez transcurrido el retraso. Los usuarios que completaron el evento desencadenante antes del lanzamiento de la campaña no son elegibles para recibirla.

También puedes enviar la campaña en un día específico de la semana seleccionando **El siguiente día de la semana**, o un número determinado de días en el futuro seleccionando **Después de un número de días calendario**. Como alternativa, puedes enviar tu mensaje utilizando la [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) en lugar de seleccionar manualmente un horario de entrega.

### Paso 3: Seleccionar eventos de excepción {#step-3-select-exception-events}

Selecciona un evento de excepción que descalifique a los usuarios para recibir esta campaña. Solo puedes hacer esto si tu mensaje desencadenado se envía después de un retraso de tiempo. Los [eventos de excepción]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) pueden ser realizar una compra, iniciar una sesión, realizar uno de los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) designados de una campaña o realizar un evento personalizado.

Si un usuario completa el evento desencadenante pero luego completa tu evento de excepción antes de que se envíe el mensaje debido al retraso de tiempo, no recibirá la campaña. Los usuarios que no reciban la campaña debido al evento de excepción son automáticamente elegibles para recibirla en el futuro, la próxima vez que completen el evento desencadenante, incluso si no eliges que los usuarios vuelvan a ser [re-elegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

Para más información sobre el uso de eventos de excepción, consulta [Ejemplos](#examples).

Si envías una campaña con un evento desencadenante que coincide con el evento de excepción, Braze cancela la campaña y reprograma automáticamente una nueva campaña basándose en el tiempo de entrega del mensaje del evento de excepción. Por ejemplo, si tu primer evento desencadenante comienza a los cinco minutos y el evento de excepción comienza a los 10 minutos, te basas en los 10 minutos del evento de excepción como el tiempo oficial de entrega del mensaje de la campaña.

{% alert note %}
No puedes hacer que "inicio de sesión" sea tanto el evento desencadenante como el evento de excepción para una campaña. Sin embargo, siempre tienes la opción de seleccionar cualquier otro evento personalizado fuera de esta opción.
{% endalert %}

### Paso 4: Asignar duración {#step-4-assign-duration}

Asigna la duración de la campaña especificando una hora de inicio y una hora de finalización opcional.

Si un usuario completa un evento desencadenante durante el plazo especificado pero es elegible para el mensaje fuera del plazo debido a un retraso programado, entonces no recibirá la campaña. Por lo tanto, si estableces un retraso de tiempo mayor que el plazo del mensaje, ningún usuario recibirá tu campaña. Además, puedes elegir enviar el mensaje en las [zonas horarias locales]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) de los usuarios.

### Paso 5: Seleccionar franja horaria {#step-5-select-time-frame}

Selecciona si el usuario recibe la campaña durante una porción específica del día. Si le das al mensaje una franja horaria y el usuario completa el evento desencadenante fuera de la franja horaria o el retraso del mensaje hace que pierda la franja horaria, entonces, de forma predeterminada, el usuario no recibirá tu mensaje.

En el caso de que un usuario complete el evento desencadenante dentro de la franja horaria, pero el retraso del mensaje haga que el usuario quede fuera de la franja horaria, puedes seleccionar la casilla **Enviar en el próximo horario disponible si la hora de entrega queda fuera de la porción especificada del día** para que estos usuarios sigan recibiendo la campaña.

Si un usuario no recibe el mensaje porque perdió la franja horaria, sigue siendo elegible para recibirlo la próxima vez que complete el evento desencadenante, incluso si no elegiste que los usuarios vuelvan a ser [re-elegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility). Si eliges que los usuarios vuelvan a ser re-elegibles, entonces los usuarios pueden recibir la campaña cada vez que completen el evento desencadenante, siempre que cumplan los requisitos durante la franja horaria especificada.

Si también asignaste a la campaña una duración determinada, entonces el usuario debe cumplir los requisitos tanto dentro de la duración como de la porción específica del día para recibir el mensaje.

### Paso 6: Determinar la re-elegibilidad {#step-6-determine-re-eligibility}

Determina si los usuarios pueden volver a ser [re-elegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) para la campaña. Si permites que los usuarios vuelvan a ser re-elegibles, puedes especificar un retraso de tiempo antes de que el usuario pueda recibir la campaña de nuevo. Esto evita que tus campañas desencadenadas se vuelvan "spam".

## Ejemplos {#examples}

Las campañas desencadenadas son muy eficaces para mensajes transaccionales o basados en logros.

Las campañas transaccionales incluyen mensajes que se envían después de que el usuario completa una compra o añade un artículo a su carrito. Este último caso es un gran ejemplo de una campaña que se beneficia de un evento de excepción. Supongamos que tu campaña recuerda a los usuarios los artículos de su carrito que no han comprado. El evento de excepción, en este caso, es que el usuario compre los productos de su carrito. Para las campañas basadas en logros, puedes enviar un mensaje cinco minutos después de que el usuario complete una conversión o supere un nivel de juego.

Además, al crear campañas de bienvenida, puedes desencadenar mensajes para que se envíen después de que el usuario se registre o configure una cuenta. Escalonar los mensajes para que se envíen en diferentes días tras el registro te permite crear un proceso de incorporación completo.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuál es el retraso máximo después de un desencadenante para campañas de mensajes dentro de la aplicación? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

Dos horas (7200 segundos). Para conocer las opciones de retraso disponibles y cómo configurar una espera más larga, consulta [Paso 2: Seleccionar la duración del retraso](#step-2-select-delay-length).

### ¿Por qué un usuario no recibió mi Campaign desencadenada? {#why-did-a-user-not-receive-my-triggered-campaign}

Cualquiera de estos factores impide que un usuario que ha completado el evento desencadenante reciba la Campaign:

- El usuario completó el evento de excepción antes de que el retraso hubiera transcurrido por completo.
- Se usó la [lógica `abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) de Liquid y el mensaje fue cancelado en función de la lógica o las reglas de `abort_message`.
- El retraso provocó que el usuario fuera elegible para recibir la Campaign después de que la duración hubiera finalizado.
- El retraso provocó que el usuario fuera elegible para recibir la Campaign fuera de la parte del día especificada.
- El usuario ya ha recibido la Campaign (incluyendo la atribución a través de identificadores de canal compartidos, por ejemplo, si comparte un correo electrónico con alguien que lo recibió, abrió o hizo clic en él), y los usuarios no vuelven a ser elegibles.
- Aunque los usuarios son elegibles para volver a recibir la Campaign, solo pueden volver a desencadenarla después de un cierto período de tiempo, y ese período de tiempo aún no ha transcurrido.

La [segmentación]({{site.baseurl}}/user_guide/audience/segments) de una Campaign desencadenada basada en datos de usuario registrados en el momento del evento puede causar una [condición de carrera]({{site.baseurl}}/help/best_practices/race_conditions#race-conditions). Esto ocurre cuando el atributo de usuario en el que se segmenta la Campaign se cambia, pero el cambio no se ha procesado para el usuario cuando se envía la Campaign. Dado que las Campaigns comprueban la pertenencia al Segment en la entrada, esto puede provocar que el usuario no reciba la Campaign.

Por ejemplo, imagina que deseas enviar una Campaign desencadenada por evento a usuarios masculinos que acaban de registrarse. Cuando el usuario se registra, registras un evento personalizado `registration` y simultáneamente estableces el atributo `gender` del usuario. El evento puede desencadenar la Campaign antes de que Braze haya procesado el género del usuario, impidiendo que reciba la Campaign.

Como práctica recomendada, asegúrate de que el atributo en el que se segmenta la Campaign se envíe a los servidores de Braze antes del evento. Si esto no es posible, la mejor manera de garantizar la entrega es usar [propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) para adjuntar las propiedades de usuario relevantes al evento y aplicar un filtro de propiedad para la propiedad específica del evento en lugar de un filtro de segmentación. Para nuestro ejemplo, agrega una propiedad `gender` al evento personalizado `registration` para que Braze tenga garantizados los datos que necesitas cuando se desencadene tu Campaign.

Además, si una Campaign está basada en acciones y tiene un retraso, puedes marcar la opción de **Volver a evaluar la pertenencia al segmento en el momento del envío** para asegurarte de que los usuarios sigan siendo parte del público objetivo cuando se envíe el mensaje.

#### Evaluación de los criterios de audiencia {#audience-criteria-evaluation}

Para Campaigns que implican un retraso antes del envío (incluyendo el límite de velocidad, la zona horaria local, la sincronización inteligente o un programa de desencadenantes), el momento en que se vuelve a evaluar el Segment depende del tipo de Campaign y la configuración.

En Campaigns basadas en acciones con retraso, si seleccionas **Volver a evaluar la pertenencia al segmento en el momento del envío**, los usuarios se vuelven a evaluar antes de que se envíe el mensaje, de modo que solo los usuarios que aún cumplan con los criterios del Segment en el momento del envío reciban el mensaje.

Si tu Campaign se desencadena por un evento personalizado específico y seleccionas un Segment como audiencia, los usuarios deben realizar el mismo evento personalizado para ser incluidos en el Segment. Esto significa que los usuarios necesitan ser parte de la audiencia antes de que una Campaign basada en acciones pueda desencadenarse. El flujo de trabajo general para una Campaign desencadenada es el siguiente:

1. **Unirse a la audiencia:** cuando un usuario realiza el evento personalizado, se agrega al público objetivo de la Campaign.
2. **Desencadenar el correo electrónico:** un usuario debe realizar el evento personalizado de nuevo para desencadenar el correo electrónico, ya que necesita ser parte de la audiencia antes de que el correo electrónico pueda enviarse.

Recomendamos cambiar el público objetivo para incluir a todos los usuarios, o verificar que los usuarios que se espera que realicen el evento ya sean parte de la audiencia de la Campaign para que el mensaje se desencadene.

![Captura de pantalla relacionada con la evaluación de los criterios de audiencia.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### Solución de problemas con eventos personalizados {#troubleshooting-custom-events}

Primero, confirma que el evento personalizado se esté enviando a Braze. Ve a **Analytics** > **Informe de eventos personalizados** y luego selecciona el evento personalizado correspondiente y el rango de fechas. Si el evento no aparece, confirma que esté configurado correctamente y que el usuario haya realizado la acción correcta.

Si el evento personalizado aparece, soluciona el problema realizando lo siguiente:

- Revisa la descarga del perfil del usuario para confirmar que desencadenó el evento y cuándo lo hizo. Si el evento fue desencadenado, compara la marca de tiempo de cuándo se desencadenó el evento con el momento en que la Campaign se activó. El evento puede haberse desencadenado antes de que la Campaign estuviera activa.
- Revisa los registros de cambios de la Campaign y de cualquier Segment utilizado en la segmentación para determinar si el usuario estaba en el Segment cuando se desencadenó su evento personalizado. Si no estaba en el Segment, no habría recibido la Campaign.
- Verifica si el usuario fue incluido en un grupo de control a través de la segmentación y, en consecuencia, se le impidió recibir la Campaign.
- Si hay un retraso programado, verifica si el evento personalizado del usuario se desencadenó antes del retraso. Si el evento se desencadenó antes del retraso, no habría recibido la Campaign.

{% alert note %}
Los mensajes dentro de la aplicación solo pueden desencadenarse mediante eventos enviados a través del SDK, no de la REST API.
{% endalert %}

### ¿Cuándo evalúan las Campaigns basadas en acciones la pertenencia a la audiencia? {#when-do-action-based-campaigns-evaluate-audience-membership}

Braze evalúa la pertenencia a la audiencia cuando procesa el evento desencadenante, antes de que se envíe el mensaje. De forma predeterminada, Braze comprueba si el usuario coincide con el público objetivo en el momento de la puesta en cola. Si la Campaign tiene un retraso, puedes seleccionar **Volver a evaluar la pertenencia al segmento en el momento del envío** para comprobar los criterios de audiencia nuevamente justo antes del envío, por ejemplo, cuando un usuario podría realizar la acción desencadenante y luego salir de la audiencia antes de que se complete el envío.

Para más información, consulta [Evaluación de los criterios de audiencia](#audience-criteria-evaluation).