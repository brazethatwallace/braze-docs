---
nav_title: Entrega basada en acciones
article_title: Entrega basada en acciones
page_order: 1
page_type: reference
description: "Este artículo de referencia describe cómo desencadenar campañas para que se envíen después de que un usuario complete un evento determinado."
tool: Campaigns

---

# Entrega basada en acciones {#action-based-delivery}

> Las campañas de entrega basada en acciones o campañas desencadenadas por eventos son muy eficaces para mensajes transaccionales o basados en logros. En lugar de enviar tu campaña en días determinados, puedes desencadenarlas para que se envíen después de que un usuario complete un evento determinado.

## Configuración de una campaña desencadenada {#setting-up-a-triggered-campaign}

### Paso 1: Selecciona un evento desencadenante {#step-1-select-a-trigger-event}

Selecciona un evento desencadenante. Puede incluir cualquiera de los siguientes:
- Realizar un pedido
- Iniciar una sesión
- Realizar un evento personalizado
- Realizar el evento de conversión primaria de la campaña
- Añadir una dirección de correo electrónico a un perfil de usuario
- Cambiar el valor de un atributo personalizado
- Actualizar un estado de suscripción
- Actualizar un estado del grupo de suscripción
- Interactuar con otras campañas
    - Ver mensaje dentro de la aplicación
    - Hacer clic en mensaje dentro de la aplicación
    - Hacer clic en botones de mensaje dentro de la aplicación
    - Hacer clic en correo electrónico
    - Hacer clic en alias en correo electrónico
    - Hacer clic en alias en cualquier Campaign o paso en Canvas
    - Abrir correo electrónico
    - Abrir correo electrónico (aperturas de máquina)
    - Abrir correo electrónico (otras aperturas)
    - Abrir directamente notificación push
    - Hacer clic en botón de notificación push
    - Hacer clic en página de historias push
    - Realizar evento de conversión
    - Recibir correo electrónico
    - Recibir SMS
    - Hacer clic en enlace acortado de SMS
    - Recibir notificación push
    - Recibir webhook
    - Estar inscrito en un grupo de control
    - Ver tarjeta de contenido
    - Hacer clic en tarjeta de contenido
    - Descartar tarjeta de contenido
- Entrar en una ubicación
- Realizar el evento de excepción de otra campaña
- Interactuar con un paso en Canvas
- Desencadenar una geovalla
- Enviar un mensaje SMS entrante
- Enviar un mensaje WhatsApp entrante

También puedes filtrar aún más los eventos desencadenantes a través de las [propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) de Braze, lo que permite propiedades de eventos personalizables para eventos personalizados y compras dentro de la aplicación. Esta característica te permite ajustar aún más qué usuarios reciben un mensaje en función de los atributos específicos del evento personalizado, lo que permite una mayor personalización de las campañas y una recopilación de datos más sofisticada.

Por ejemplo, supongamos que tenemos una campaña con un evento personalizado de carrito abandonado que se filtra aún más por la propiedad "valor del carrito". Esta campaña solo llegará a los usuarios que hayan dejado en su carrito productos con un valor de entre $100 y $200.

![Campaña de carrito abandonado filtrada por una propiedad de evento personalizado para un valor del carrito entre $100 y $200.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
El evento desencadenante "iniciar sesión" puede ser la primera apertura de la aplicación del usuario si el Segment de tu campaña aplica a usuarios nuevos (por ejemplo, si tu Segment incluye a usuarios sin sesiones).
{% endalert %}

Ten en cuenta que aún puedes enviar una campaña desencadenada a un Segment específico de usuarios, de modo que los usuarios que no formen parte del Segment no recibirán la campaña aunque completen el evento desencadenante.

Con respecto al evento desencadenante para cuando un usuario añade una dirección de correo electrónico a su perfil, se aplican las siguientes reglas:

- El evento desencadenante se activará después de que se actualice el atributo del perfil de usuario. Esto significa que la evaluación de los Segments y filtros de la campaña se realizará después de cualquier actualización de atributos. Esto es beneficioso porque te permite configurar filtros como "la dirección de correo electrónico coincide con gmail.com" para crear una campaña desencadenada que solo se envíe a usuarios de Gmail y se active tan pronto como añadan su dirección de correo electrónico.
- El evento desencadenante se activará cuando se añada una dirección de correo electrónico a un perfil de usuario. Si tienes varios perfiles de usuario creados con la misma dirección de correo electrónico, la campaña puede activarse varias veces, una por cada perfil de usuario.

Además, los mensajes dentro de la aplicación desencadenados siguen cumpliendo las reglas de entrega de mensajes dentro de la aplicación y aparecen al inicio de una sesión de la aplicación.

![Programación de entrega de campaña basada en acciones que muestra las opciones de configuración del evento desencadenante.]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### Paso 2: Selecciona la duración del retraso {#step-2-select-delay-length}

Selecciona cuánto tiempo esperar antes de enviar la campaña después de que se cumplan los criterios del desencadenante. Si la duración del retraso elegida es mayor que la duración del mensaje para el envío, ningún usuario recibirá la campaña.

Las campañas de mensajes dentro de la aplicación pueden retrasar la entrega después del evento desencadenante hasta dos horas (7200 segundos). Las opciones de retraso son **Inmediatamente** y **Después de un retraso**. Para una espera más larga, añade un paso de [Retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) antes de un paso de mensaje dentro de la aplicación en un Canvas.

{% alert important %}
Braze utiliza la marca de tiempo enviada con el evento personalizado para evaluar el retraso de una campaña basada en acciones. Si esa marca de tiempo está atrasada, Braze puede considerar que el retraso ya ha transcurrido y enviar el mensaje inmediatamente o antes de lo esperado. Para evitar problemas de sincronización en la entrega, envía la marca de tiempo del evento personalizado con la hora actual.
{% endalert %}

Además, los usuarios que completen el evento desencadenante después de que se lance tu campaña serán los primeros en recibir el mensaje una vez que haya pasado el retraso. Los usuarios que hayan completado el evento desencadenante antes del lanzamiento de la campaña no serán elegibles para recibirla.

![Captura de pantalla del paso 2: selección de la duración del retraso.]({% image_buster /assets/img_archive/schedule_triggered22.png %})

También puedes optar por enviar la campaña en un día específico de la semana (eligiendo "on the next" y seleccionando un día) o un número específico de días (seleccionando "in") en el futuro. Alternativamente, puedes elegir enviar tu mensaje usando la característica de [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) en lugar de seleccionar manualmente una hora de entrega.

![También puedes optar por enviar la campaña en un día específico de la semana o un número específico de días en el futuro. Alternativamente, puedes elegir enviar tu mensaje usando la característica de sincronización inteligente en lugar de seleccionar manualmente una hora de entrega.]({% image_buster /assets/img_archive/schedule_triggered7.png %})
![También puedes optar por enviar la campaña en un día específico de la semana o un número específico de días en el futuro. Alternativamente, puedes elegir enviar tu mensaje usando la característica de sincronización inteligente en lugar de seleccionar manualmente una hora de entrega.]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### Paso 3: Selecciona eventos de excepción {#step-3-select-exception-events}

Selecciona un evento de excepción que descalificará a los usuarios de recibir esta campaña. Solo puedes hacer esto si tu mensaje desencadenado se envía después de un retraso. Los [eventos de excepción]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) pueden ser realizar una compra, iniciar una sesión, realizar uno de los [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) designados de la campaña o realizar un evento personalizado. Si un usuario completa el evento desencadenante pero luego completa tu evento de excepción antes de que se envíe el mensaje debido al retraso, no recibirá la campaña. Los usuarios que no reciban la campaña debido al evento de excepción serán automáticamente elegibles para recibirla en el futuro, la próxima vez que completen el evento desencadenante, incluso si no eliges que los usuarios sean [re-elegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

![Selecciona un evento de excepción que descalificará a los usuarios de recibir esta campaña. Solo puedes hacer esto si tu mensaje desencadenado se envía después de un retraso. Los eventos de excepción pueden ser realizar una compra, iniciar una sesión, realizar uno de los eventos de conversión designados de la campaña o realizar un evento personalizado.]({% image_buster /assets/img_archive/schedule_triggered32.png %})

Puedes leer más sobre cómo utilizar los eventos de excepción en nuestra sección de [ejemplos]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#use-cases).

> Si envías una campaña con un evento desencadenante que coincide con el evento de excepción, Braze cancelará la campaña y reprogramará automáticamente una nueva campaña basada en la hora de entrega del mensaje del evento de excepción. Por ejemplo, si tu primer evento desencadenante comienza a los cinco minutos y el evento de excepción comienza a los 10 minutos, la hora de entrega oficial del mensaje de la campaña será los 10 minutos del evento de excepción.

{% alert note %}
No puedes hacer que "iniciar sesión" sea tanto el evento desencadenante como el evento de excepción de una campaña. Sin embargo, siempre tienes la opción de seleccionar cualquier otro evento personalizado aparte de esta opción.
{% endalert %}

### Paso 4: Asigna la duración {#step-4-assign-duration}

Asigna la duración de la campaña especificando una hora de inicio y una hora de finalización opcional.

![Captura de pantalla del paso 4: asignación de la duración.]({% image_buster /assets/img_archive/schedule_triggered43.png %})

Si un usuario completa un evento desencadenante durante el periodo de tiempo especificado, pero es elegible para el mensaje fuera del periodo debido a un retraso programado, entonces no recibirá la campaña. Por lo tanto, si configuras un retraso mayor que el periodo del mensaje, ningún usuario recibirá tu campaña. Además, puedes optar por enviar el mensaje en las [zonas horarias locales]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) de los usuarios.

### Paso 5: Selecciona el periodo de tiempo {#step-5-select-time-frame}

Selecciona si el usuario recibirá la campaña durante una parte específica del día. Si asignas un periodo de tiempo al mensaje y el usuario completa el evento desencadenante fuera de ese periodo o el retraso del mensaje hace que pierda el periodo, entonces, de forma predeterminada, el usuario no recibirá tu mensaje.

![Selecciona si el usuario recibirá la campaña durante una parte específica del día. Si asignas un periodo de tiempo al mensaje y el usuario completa el evento desencadenante fuera de ese periodo o el retraso del mensaje hace que pierda el periodo, entonces, de forma predeterminada, el usuario no recibirá tu mensaje.]({% image_buster /assets/img_archive/schedule_triggered5.png %})

En el caso en que un usuario complete el evento desencadenante dentro del periodo, pero el retraso del mensaje haga que quede fuera del periodo, puedes marcar la siguiente casilla para que estos usuarios aún reciban la campaña.

![Captura de pantalla del paso 5: selección del periodo de tiempo.]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

Si un usuario no recibe el mensaje porque pierde el periodo de tiempo, seguirá siendo elegible para recibirlo la próxima vez que complete el evento desencadenante, incluso si no elegiste que los usuarios sean [re-elegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility). Si eliges que los usuarios sean re-elegibles, entonces los usuarios pueden recibir la campaña cada vez que completen el evento desencadenante, siempre que sean elegibles durante el periodo de tiempo especificado.

Si también has asignado una duración determinada a la campaña, entonces el usuario debe ser elegible tanto dentro de la duración como de la parte específica del día para recibir el mensaje.

### Paso 6: Determina la re-elegibilidad {#step-6-determine-re-eligibility}

Determina si los usuarios pueden ser [re-elegibles]({% image_buster /assets/img_archive/ReEligible.png %}) para la campaña. Si permites que los usuarios sean re-elegibles, puedes especificar un retraso antes de que el usuario pueda recibir la campaña nuevamente. Esto evitará que tus campañas desencadenadas se vuelvan demasiado repetitivas.

![Captura de pantalla del paso 6: determinación de la re-elegibilidad.]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## Ejemplos {#use-cases}

Las campañas desencadenadas son muy eficaces para mensajes transaccionales o basados en logros.

Las campañas transaccionales incluyen mensajes enviados después de que el usuario completa una compra o añade un artículo a su carrito. Este último caso es un gran ejemplo de una campaña que se beneficiaría de un evento de excepción. Supongamos que tu campaña recuerda a los usuarios los artículos en su carrito que no han comprado. El evento de excepción, en este caso, sería que el usuario compre los productos de su carrito. Para las campañas basadas en logros, puedes enviar un mensaje 5 minutos después de que el usuario complete una conversión o supere un nivel de juego.

Además, al crear campañas de bienvenida, puedes desencadenar mensajes para que se envíen después de que el usuario se registre o configure una cuenta. Escalonar los mensajes para que se envíen en diferentes días tras el registro te permitirá crear un proceso de incorporación completo.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuál es el retraso máximo después de un desencadenante para campañas de mensajes dentro de la aplicación? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

Las campañas de mensajes dentro de la aplicación pueden retrasar la entrega después del evento desencadenante hasta dos horas (7200 segundos). Las opciones de retraso son **Inmediatamente** y **Después de un retraso**. Para una espera más larga, añade un paso de [Retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) antes de un paso de mensaje dentro de la aplicación en un Canvas.

### ¿Por qué un usuario no recibió mi campaña desencadenada? {#why-did-a-user-not-receive-my-triggered-campaign}

Cualquiera de estas situaciones impedirá que un usuario que haya completado el evento desencadenante reciba la campaña:

- El usuario completó el evento de excepción antes de que el tiempo de retraso haya transcurrido por completo.
- Se utilizó la [lógica `abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) de Liquid y el mensaje fue cancelado según la lógica o las reglas de `abort_message`.
- El tiempo de retraso causó que el usuario se volviera elegible para recibir la campaña después de que la duración haya finalizado.
- El tiempo de retraso causó que el usuario se volviera elegible para recibir la campaña fuera de la porción especificada del día.
- El usuario ya ha recibido la campaña (incluyendo la atribución a través de identificadores de canal compartidos; por ejemplo, si comparten un correo electrónico con alguien que lo recibió, abrió o hizo clic en él), y los usuarios no se vuelven elegibles de nuevo.
- Aunque los usuarios son elegibles de nuevo para recibir la campaña, solo pueden volver a desencadenarla después de un cierto periodo de tiempo, y ese periodo aún no ha transcurrido.

[Segmentar]({{site.baseurl}}/user_guide/audience/segments) una campaña desencadenada en función de datos de usuario registrados en el momento del evento puede causar una [condición de carrera]({{site.baseurl}}/help/best_practices/race_conditions#race-conditions). Esto sucede cuando el atributo de usuario en el que se segmenta la campaña cambia, pero el cambio no se ha procesado para el usuario cuando se envía la campaña. Dado que las campañas verifican la pertenencia al segmento en la entrada, esto puede hacer que el usuario no reciba la campaña.

Por ejemplo, imagina que quieres enviar una campaña desencadenada por un evento a usuarios masculinos que acaban de registrarse. Cuando el usuario se registra, registras un evento personalizado `registration` y simultáneamente configuras el atributo `gender` del usuario. El evento puede desencadenar la campaña antes de que Braze haya procesado el género del usuario, lo que impide que reciba la campaña.

Como práctica recomendada, asegúrate de que el atributo en el que se segmenta la campaña se envíe a los servidores de Braze antes que el evento. Si esto no es posible, la mejor manera de garantizar la entrega es usar [propiedades de evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) para adjuntar las propiedades de usuario relevantes al evento y aplicar un filtro de propiedad para la propiedad de evento específica en lugar de un filtro de segmentación. En nuestro ejemplo, añadirías una propiedad `gender` al evento personalizado `registration` para que Braze tenga garantizados los datos que necesitas cuando se desencadene tu campaña.

Además, si una campaña está basada en acciones y tiene un retraso, puedes marcar la opción de **Volver a evaluar la pertenencia al segmento en el momento del envío** para asegurarte de que los usuarios siguen formando parte del público objetivo cuando se envía el mensaje.

#### Evaluación de los criterios de audiencia {#audience-criteria-evaluation}

Para campañas que implican un retraso antes del envío (incluyendo límite de velocidad, zona horaria local, sincronización inteligente o un cronograma de desencadenamiento), el momento en que se vuelve a evaluar el segmento depende del tipo y la configuración de la campaña.

En campañas basadas en acciones con un retraso, si seleccionas **Volver a evaluar la pertenencia al segmento en el momento del envío**, los usuarios se vuelven a evaluar antes de que se envíe el mensaje, de modo que solo los usuarios que aún cumplen los criterios del segmento en el momento del envío reciben el mensaje.

Si tu campaña se desencadena por un evento personalizado específico y seleccionas un segmento como audiencia, los usuarios deben realizar el mismo evento personalizado para ser incluidos en el segmento. Esto significa que los usuarios necesitan formar parte de la audiencia antes de que se pueda desencadenar una campaña basada en acciones. El flujo de trabajo general para una campaña desencadenada es el siguiente:

1. **Unirse a la audiencia:** cuando un usuario realiza el evento personalizado, se añade al público objetivo de la campaña.
2. **Desencadenar el correo electrónico:** un usuario debe realizar el evento personalizado de nuevo para desencadenar el correo electrónico, ya que necesita formar parte de la audiencia antes de que se pueda enviar el correo electrónico.

Recomendamos cambiar el público objetivo para incluir a todos los usuarios o verificar que los usuarios que se espera que realicen el evento ya formen parte de la audiencia de la campaña para que el mensaje se desencadene.

![Captura de pantalla relacionada con la evaluación de criterios de audiencia.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### Solución de problemas con eventos personalizados {#troubleshooting-custom-events}

Primero, confirma que el evento personalizado se está enviando a Braze. Ve a **Analytics** > **Informe de eventos personalizados** y luego selecciona el evento personalizado y el rango de fechas correspondientes. Si el evento no aparece, confirma que esté configurado correctamente y que el usuario haya realizado la acción correcta.

Si el evento personalizado aparece, continúa la solución de problemas haciendo lo siguiente:

- Revisa la descarga del perfil del usuario para confirmar que desencadenó el evento y cuándo lo hizo. Si el evento se desencadenó, compara la marca de tiempo de cuándo se desencadenó con la hora en que la campaña se activó. Es posible que el evento se haya desencadenado antes de que la campaña estuviera activa.
- Revisa los registros de cambios de la campaña y de cualquier segmento utilizado en la segmentación para determinar si el usuario estaba en el segmento cuando se desencadenó su evento personalizado. Si no estaba en el segmento, no habría recibido la campaña.
- Verifica si el usuario fue incluido en un grupo de control a través de la segmentación y, en consecuencia, se le impidió recibir la campaña.
- Si hay un retraso programado, comprueba si el evento personalizado del usuario se desencadenó antes del retraso. Si el evento se desencadenó antes del retraso, no habría recibido la campaña.

{% alert note %}
Los mensajes dentro de la aplicación solo pueden ser desencadenados por eventos enviados a través del SDK, no a través de la REST API.
{% endalert %}

### ¿Cuándo evalúan las campañas basadas en acciones la pertenencia a la audiencia? {#when-do-action-based-campaigns-evaluate-audience-membership}

Braze evalúa la pertenencia a la audiencia cuando procesa el evento desencadenante, antes de que se envíe el mensaje. De forma predeterminada, Braze verifica si el usuario coincide con el público objetivo en el momento de poner en cola. Si la campaña tiene un retraso, puedes seleccionar **Volver a evaluar la pertenencia al segmento en el momento del envío** para verificar los criterios de audiencia nuevamente justo antes del envío; por ejemplo, cuando un usuario podría realizar la acción desencadenante y luego salir de la audiencia antes de que se complete el envío.

Para obtener más información, consulta [Evaluación de los criterios de audiencia](#audience-criteria-evaluation).