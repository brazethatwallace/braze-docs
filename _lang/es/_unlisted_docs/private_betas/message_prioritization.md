---
article_title: Priorización de mensajes
permalink: /message_prioritization/
toc_headers: h2
description: "Este artículo de referencia describe la priorización de mensajes de nivel superior y cómo configurarla para tu espacio de trabajo."
---

# Priorización de mensajes {#message-prioritization}

> Utiliza la priorización de mensajes para asegurarte de que tus usuarios reciban las campañas que más importan.

{% alert important %}
La priorización de mensajes se encuentra actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si te interesa participar en esta beta.<br><br>Este artículo refleja la versión de la priorización de mensajes planificada para su lanzamiento en producción a finales de julio de 2026. Algunos comportamientos descritos aquí pueden no estar disponibles aún en todos los espacios de trabajo en beta.
{% endalert %}

Solo los administradores pueden configurar los ajustes de priorización de mensajes de nivel superior. Los usuarios con permisos limitados pueden ver cada página de esta sección, pero no pueden realizar cambios.

Para acceder a los ajustes de priorización de mensajes de nivel superior, ve a **Configuración** > **Priorización de mensajes**.

## Cómo funciona {#how-it-works}

Utiliza la priorización de mensajes para crear [categorías](#categories) y [reglas de priorización](#prioritization-rules) para clasificar cómo se envían tus mensajes.

Supongamos que una marca de belleza gestiona promociones por correo electrónico para asociaciones de pago y programas de fidelización. Con la priorización de mensajes, la marca crea dos categorías llamadas "Asociaciones de pago" y "Fidelización". La marca clasifica estas categorías en función de cuál es más crítica para el negocio. Durante la temporada navideña, la marca clasifica "Fidelización" por encima de "Asociaciones de pago" para priorizar a los clientes que han formado parte del programa de membresía durante más de un año.

![Un ejemplo de reglas de priorización para dos categorías: Asociaciones de pago y Fidelización.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

En el momento del envío, Braze compara el mensaje que se está enviando con otros mensajes que el usuario podría recibir y que están adheridos a la priorización, tienen una categoría de prioridad asignada y cuentan para la misma regla de limitación de frecuencia dentro de la misma ventana de limitación de frecuencia. Si enviar el mensaje actual impediría que un mensaje de mayor prioridad se envíe más tarde, Braze desprioriza el mensaje de menor prioridad. Dependiendo de la ventana de reintento configurada, ese mensaje de menor prioridad se reintenta más tarde o no se envía.

La priorización de mensajes puede evaluar:

- Campaigns planificadas
- Campaigns basadas en acciones
- Canvas

Braze utiliza su predicción de cuándo se espera que se envíe cada mensaje al evaluar si enviar un mensaje ahora podría impedir que un mensaje de mayor prioridad se envíe más tarde. Para más información sobre cómo Braze predice el momento de envío futuro para Campaigns y Canvas, consulta [¿Cómo predice Braze cuándo se enviará un mensaje futuro?](#how-does-braze-predict-when-a-future-message-sends)

### Tipos de mensajes compatibles {#supported-message-types}

La priorización de mensajes es compatible con los mismos canales que la limitación de frecuencia:

- Notificaciones push
- Correo electrónico
- SMS
- Webhooks
- WhatsApp
- LINE

Para la priorización y la limitación de frecuencia, las notificaciones push de iOS, Android, web y otras plataformas de notificaciones push se tratan como un único canal push compartido, no como canales separados.

## Categorías {#categories}

Las reglas de priorización se basan en una clasificación de categorías, que es una etiqueta que puedes asignar a una Campaign o Canvas determinado (similar a una [etiqueta]({{site.baseurl}}/user_guide/administrative/app_settings/tags)). Puedes crear hasta 20 categorías en un momento dado.

Para añadir una nueva categoría:

1. Ve a **Configuración** > **Priorización de mensajes** > **Categorías**.
2. Selecciona **Crear nueva categoría**.

![El botón "Crear nueva categoría" en la sección de priorización de mensajes.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Dale a la categoría un nombre y una descripción opcional.
4. Selecciona **Crear categoría**.

![Una categoría de ejemplo llamada "P3" con la descripción "Esta es mi tercera categoría de mayor prioridad."]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

Para editar o eliminar una categoría, selecciona el menú <i class="fas fa-ellipsis-vertical"></i>.

## Reglas de priorización {#prioritization-rules}

Una vez configuradas tus categorías, puedes clasificarlas en un conjunto de reglas de priorización. Las reglas se clasifican en orden descendente de prioridad. Puedes crear hasta 10 reglas de priorización en un momento dado.

1. Ve a **Configuración** > **Priorización de mensajes** > **Reglas de priorización** para configurar tus reglas.

![Sección "Reglas de priorización" sin prioridades configuradas aún.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. Selecciona **Añadir regla**.
3. Selecciona una categoría del menú desplegable.

![Regla de priorización "Prioridad 1" con P1 seleccionada como categoría.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. Continúa añadiendo reglas seleccionando **+ Añadir regla** debajo de tu última regla.

Para reordenar las reglas, selecciona y arrastra el icono <i class="fa-solid fa-grip-vertical"></i> de una regla. Para eliminar una regla, selecciona el menú <i class="fas fa-ellipsis-vertical"></i> y luego **Eliminar regla**.

Asegúrate de seleccionar **Guardar** para que se apliquen tus actualizaciones.

## Configuración a nivel de Campaign {#campaign-level-settings}

### Adhesión voluntaria {#opt-in}

Para adherir una Campaign a la priorización, selecciona la casilla **Adhesión voluntaria a la priorización de mensajes** en la configuración de entrega de la Campaign.

![La casilla de "Adhesión voluntaria a la priorización de mensajes".]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

A continuación, asigna la Campaign a una categoría seleccionando una del menú desplegable **Categoría**.

![El menú desplegable de categoría de priorización de mensajes en la configuración de entrega de una Campaign.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

La priorización de mensajes es compatible con Campaigns planificadas y Campaigns basadas en acciones.

### Sincronización inteligente {#intelligent-timing}

Para Campaigns que utilizan sincronización inteligente, la priorización de mensajes compara los mensajes utilizando la hora de envío que Braze selecciona para cada usuario en lugar de solo la programación original de la Campaign. Esto permite a Braze tener en cuenta el mensaje que tiene más probabilidades de enviarse primero a ese usuario.

Para Campaigns recurrentes con sincronización inteligente, Braze puede utilizar la hora de envío conocida seleccionada para la recurrencia actual al comparar esa Campaign con otros mensajes priorizados elegibles.

### Ventana de reintento {#retry-window}

Una ventana de reintento permite que los mensajes adheridos reintenten durante un máximo de tres días si el primer intento no tiene una prioridad lo suficientemente alta para enviarse. En cada día posterior, a la misma hora en que el mensaje fue planificado o desencadenado originalmente, se intenta enviar el mensaje de nuevo. Después del último día en la ventana de reintento, si el mensaje aún no se ha enviado, no se reintenta más y se desprioriza permanentemente.

Para Campaigns planificadas recurrentes, la ventana de reintento debe ser más corta que el tiempo mínimo entre envíos de esa Campaign. Los reintentos siempre ocurren un día a la vez desde la hora de envío original, incluso si la Campaign no está normalmente planificada para enviarse ese día. Por ejemplo, si tienes una Campaign que se envía cada lunes y miércoles, el intento de reintento ocurre el martes, por lo que la ventana de reintento debe configurarse en un día. Si tienes una Campaign que se envía cada lunes, miércoles y viernes, y el envío del viernes se reintenta con una ventana de reintento de un día, el intento de reintento ocurre el sábado, no el lunes.

![La configuración de "Ventana de reintento" establecida en 1 día.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

Para Campaigns basadas en acciones, los reintentos se basan en la hora en que se esperaba originalmente que se enviara el mensaje desencadenado.

Las Campaigns basadas en acciones que utilizan eventos de excepción no son compatibles con las ventanas de reintento.

Las ventanas de reintento para mensajes de Canvas se configuran a nivel de paso. Para los pasos de mensajería de Canvas compatibles, si un paso de mensaje de Canvas se desprioriza y tiene una ventana de reintento configurada, Braze puede reintentar ese paso más tarde dentro de su ventana de reintento.

## Configuración a nivel de Canvas {#canvas-level-settings}

Para adherir un Canvas a la priorización de mensajes, habilita la priorización de mensajes en la configuración del Canvas y asigna el Canvas a una categoría.

Cuando un usuario es elegible para múltiples mensajes priorizados, Braze evalúa las Campaigns adheridas y los pasos de mensaje de Canvas elegibles juntos en los canales compatibles.

Para Campaigns, esto incluye envíos planificados y basados en acciones elegibles.

Para Canvas, esto incluye:

- Canvas planificados futuros para los que el usuario es elegible de entrar
- Canvas en los que el usuario se encuentra actualmente

La priorización de Canvas no es todo o nada. Una Campaign de mayor prioridad puede hacer que un paso de Canvas se despriorice, mientras que pasos elegibles posteriores en ese mismo Canvas aún pueden enviarse, dependiendo de la clasificación de categorías, el momento de envío y las reglas de limitación de frecuencia.

### Cómo evalúa Braze los mensajes futuros {#how-braze-evaluates-future-messages}

Braze evalúa Campaigns y Canvas de manera diferente según el tipo de mensaje.

#### Campaigns

Braze compara cada mensaje de Campaign elegible utilizando la hora en que se espera que se envíe ese mensaje.

#### Canvas {#canvases}

Braze recorre el Canvas para determinar qué mensajes futuros podría recibir un usuario, comenzando desde:

- La entrada al Canvas, para Canvas planificados futuros
- El paso actual del usuario, si el usuario ya está en el Canvas

Luego, Braze evalúa los pasos de Canvas de las siguientes maneras.

##### Pasos de mensajería {#messaging-steps}

Estos pasos se cuentan para la priorización y se añaden al conjunto de mensajes elegibles cuando se envían en un canal compatible.

- Paso de mensaje
- Paso del optimizador de contenido

##### Pasos de continuación {#continuation-steps}

Estos pasos se ignoran para la priorización y no afectan la evaluación anticipada.

- Paso de actualización de contexto
- Paso de actualización de usuario
- Paso de sincronización de audiencia
- Paso de conmutador de características
- Paso de retraso con un retraso fijo

##### Pasos de límite {#boundary-steps}

Braze detiene la evaluación anticipada en estos pasos hasta que el usuario realmente avance a través de ellos en el Canvas.

- Paso de retraso con un retraso personalizado
- Paso de retraso que sigue a un paso de ramificación
- Paso de ruta de acción
- Paso de experimento

##### Pasos de ramificación {#branching-steps}

Estos pasos dividen el Canvas en múltiples rutas posibles.

- Paso de división de decisiones
- Paso de ruta de audiencia

Cuando una ruta de priorización contiene pasos de ramificación, Braze asume que todas las rutas son viables y considera todos los pasos de mensaje paralelos en canales compatibles para la priorización. Dado que las reglas de limitación de frecuencia pueden ser específicas por canal, los pasos de mensaje paralelos se deduplican por canal cuando es necesario.

Por ejemplo, si una rama puede enviar correo electrónico y otra rama también puede enviar correo electrónico, Braze los trata como un único envío de correo electrónico posible para la priorización anticipada. Si otra rama puede enviar push, Braze también considera ese posible envío push por separado.

Para pasos de mensaje de Canvas que utilizan sincronización inteligente, Braze predice el momento del envío con el mejor esfuerzo hasta que el usuario realmente llegue a ese paso. Una vez que el usuario entra en el paso de sincronización inteligente y Braze calcula la hora de envío por usuario, la priorización de mensajes utiliza esa hora de envío calculada para el paso actual. En rutas deterministas, Braze también refleja ese momento actualizado en los pasos de mensaje siguientes al determinar sus horas de envío esperadas.

Los pasos del optimizador de contenido se tratan como pasos de mensajería porque siempre envían en un canal especificado. Sin embargo, las ventanas de reintento no se aplican a los pasos del optimizador de contenido porque reintentar interferiría con el experimento. Otros pasos de mensajería de Canvas compatibles pueden utilizar ventanas de reintento. Los pasos de Canvas en canales no compatibles no participan en la priorización de mensajes.

## Limitación de frecuencia {#frequency-caps}

La priorización de mensajes funciona dentro de tus reglas de limitación de frecuencia existentes. Un mensaje priorizado solo puede enviarse si:

1. La regla de limitación de frecuencia relevante aún no se ha alcanzado para ese usuario, y
2. Enviar ese mensaje no haría que el usuario alcance un límite antes de que un mensaje posterior de mayor prioridad pueda enviarse.

Los mensajes que no están sujetos a la limitación de frecuencia no son elegibles para la priorización de mensajes. Si quieres que un mensaje siempre se envíe, exclúyelo de la limitación de frecuencia. Esto también lo elimina de la priorización de mensajes.

### Para Campaigns y pasos de Canvas compatibles {#for-supported-campaigns-and-canvas-steps}

Para ser elegible para la priorización de mensajes, la Campaign o el paso de Canvas debe utilizar un canal compatible y ser evaluado dentro de tu configuración de limitación de frecuencia.

![Un ejemplo de una regla de limitación de frecuencia.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

### Reglas de limitación de frecuencia {#frequency-capping-rules}

Braze optimiza la prioridad dentro de tus reglas de limitación de frecuencia existentes. Los mensajes priorizados solo se comparan cuando comparten la misma regla de limitación de frecuencia aplicable.

Por ejemplo, dos Campaigns de correo electrónico que cuentan para la misma regla de limitación de frecuencia de correo electrónico pueden priorizarse entre sí. Una Campaign de correo electrónico de menor prioridad no se desprioriza a favor de un mensaje SMS de mayor prioridad a menos que ambos mensajes cuenten para la misma regla de limitación de frecuencia.

Puedes utilizar reglas de limitación de frecuencia específicas por canal, reglas específicas por categoría, filtros de etiquetas o reglas que se apliquen a cualquier canal. La priorización de mensajes funciona con las reglas que se apliquen a tus mensajes adheridos.

Puedes crear reglas de limitación de frecuencia por categoría para gestionar cuántos mensajes recibe un usuario de una categoría determinada. Esto ayuda a evitar que una categoría de alta prioridad envíe demasiados mensajes. Selecciona **Categoría de priorización de mensajes** en **Filtros adicionales** y selecciona una categoría del menú desplegable.

![Un ejemplo de la regla de limitación de frecuencia con el menú desplegable del campo "Categoría" para seleccionar P2 o P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

Los mensajes fuera de la priorización de mensajes comparten los límites de frecuencia con los mensajes priorizados, por lo que incluso un mensaje de alta prioridad puede ser cancelado debido a un mensaje fuera de la priorización de mensajes.

## Ejemplos {#examples}

### Campaign de mayor prioridad frente a Campaign de menor prioridad {#higher-priority-campaign-versus-lower-priority-campaign}

Supongamos que un usuario es elegible para dos Campaigns de correo electrónico el mismo día, y ambas Campaigns cuentan para la misma regla de limitación de frecuencia. Si se espera que la Campaign de mayor prioridad se envíe más tarde ese día, Braze puede despriorizar la Campaign de menor prioridad para que la Campaign de mayor prioridad pueda enviarse en su lugar. Si la Campaign de menor prioridad tiene una ventana de reintento, Braze puede intentarla de nuevo más tarde.

### Campaign basada en acciones de mayor prioridad frente a mensaje de menor prioridad {#higher-priority-action-based-campaign-versus-lower-priority-message}

Supongamos que un usuario desencadena una Campaign basada en acciones de mayor prioridad que está configurada para enviarse dos horas después. Durante ese retraso, Braze puede considerar esa Campaign basada en acciones próxima al decidir si otro mensaje priorizado debería enviarse primero. Esto ayuda a evitar que un mensaje de menor prioridad se envíe ahora si se espera que la Campaign basada en acciones de mayor prioridad se envíe pronto.

### Canvas de mayor prioridad frente a Campaign de menor prioridad {#higher-priority-canvas-versus-lower-priority-campaign}

Supongamos que un usuario es elegible para una Campaign de menor prioridad, pero también se espera que reciba un mensaje de Canvas de mayor prioridad más tarde ese día. Si Braze ya puede evaluar ese mensaje futuro de Canvas, puede despriorizar la Campaign de menor prioridad para que el mensaje de Canvas de mayor prioridad pueda enviarse en su lugar.

### Canvas de mayor prioridad con un paso de límite frente a Campaign de menor prioridad {#higher-priority-canvas-with-a-boundary-step-versus-lower-priority-campaign}

Supongamos que un Canvas de mayor prioridad incluye un paso de ruta de acción, un experimento o un retraso personalizado antes de su siguiente paso de mensaje. Hasta que el usuario llegue y avance más allá de ese paso, Braze no evalúa anticipadamente el mensaje de Canvas de mayor prioridad que está más adelante. En ese caso, una Campaign de menor prioridad aún puede enviarse primero.

### Canvas de mayor prioridad con ramificación frente a mensaje de menor prioridad {#higher-priority-branching-canvas-versus-lower-priority-message}

Supongamos que un Canvas de mayor prioridad puede enviar diferentes mensajes dependiendo de la rama que siga un usuario. Braze evalúa esas posibles rutas futuras de manera conservadora al comparar mensajes. Esto ayuda a evitar que un mensaje de menor prioridad se envíe ahora si una rama de Canvas de mayor prioridad podría utilizar ese mismo límite de frecuencia más tarde.

### Paso de sincronización inteligente de Canvas y pasos posteriores {#canvas-intelligent-timing-step-and-downstream-steps}

Supongamos que un usuario entra en un paso de mensaje de Canvas de mayor prioridad que utiliza sincronización inteligente. Una vez que Braze calcula la hora de envío de ese usuario para el paso de sincronización inteligente, la priorización de mensajes utiliza esa hora de envío por usuario para el paso actual y para los pasos de mensaje posteriores en la misma ruta determinista. Esto ayuda a Braze a comparar los mensajes de Canvas posteriores con otros envíos priorizados utilizando el momento actualizado en lugar de solo la estimación de ruta anterior.

## Limitaciones {#limitations}

La priorización de mensajes tiene las siguientes limitaciones:

- Hasta 20 categorías por espacio de trabajo
- Hasta 10 reglas de priorización por espacio de trabajo
- Hasta 25 elementos planificados activos adheridos a la priorización a la vez
- Hasta 25 elementos basados en acciones activos adheridos a la priorización a la vez
- Ventanas de reintento de hasta 3 días

El límite de elementos planificados es un total combinado entre Campaigns planificadas y Canvas planificados adheridos. El límite de elementos basados en acciones es un total combinado entre Campaigns basadas en acciones y Canvas basados en acciones adheridos.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cómo se resuelven los empates entre mensajes de la misma categoría? {#how-are-ties-broken-between-messages-in-the-same-category}

Al priorizar dos Campaigns de la misma categoría entre sí, Braze da mayor prioridad a la que tiene la hora de envío más temprana. Si se configura una ventana de reintento, Braze utiliza el final de esa ventana de reintento al comparar Campaigns dentro de la misma regla de prioridad. Para Campaigns recurrentes, la hora de envío se calcula como la próxima ocurrencia a partir de la medianoche en la hora de la empresa. Para Campaigns planificadas en hora local, Braze asume una hora de envío en la hora de la empresa.

Para Canvas en la misma categoría, Braze utiliza el momento de entrada al Canvas como desempate para que todos los pasos en el mismo Canvas preserven la misma prioridad relativa frente a otras Campaigns y Canvas.

### ¿Cómo puedo asegurarme de que un mensaje siempre se envíe? {#how-can-i-make-sure-a-message-is-always-sent}

Puede haber algunos escenarios en los que quieras que un mensaje siempre se envíe, como en el caso de notificaciones transaccionales o legales. En este caso, debes excluir el mensaje de la limitación de frecuencia, lo que también lo hace no elegible para la priorización de mensajes. Esto envía el mensaje siempre que esté planificado o desencadenado sin considerar qué más se está enviando.

### ¿Cuándo se priorizan realmente los mensajes? ¿Hay un horario? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Cada mensaje se prioriza en función de cuándo se espera que se envíe. No hay un momento de evaluación universal para los mensajes priorizados.

### ¿Cómo predice Braze cuándo se enviará un mensaje futuro? {#how-does-braze-predict-when-a-future-message-sends}

Braze predice el momento de envío futuro de manera diferente para cada tipo de mensaje:

- **Campaigns planificadas:** Braze utiliza la hora en que se espera que se envíe cada Campaign. Para Campaigns planificadas que utilizan sincronización inteligente, Braze utiliza la hora de envío óptima de cada usuario para esa ocurrencia de la Campaign.
- **Campaigns basadas en acciones:** Braze utiliza la hora en que se espera que se envíe cada mensaje desencadenado, incluyendo cualquier retraso configurado entre el desencadenante y el envío.
- **Pasos de Canvas:** Braze utiliza la entrada del usuario al Canvas o la posición actual del usuario en el Canvas, más el momento de los pasos posteriores. Para pasos de mensaje de Canvas que utilizan sincronización inteligente, una vez que un usuario entra en ese paso, Braze utiliza la hora de envío por usuario que calcula para ese usuario. Para los pasos de mensaje siguientes en la misma ruta de priorización determinista, Braze utiliza esa hora de envío de sincronización inteligente al determinar el momento de envío esperado posterior. Antes de que un usuario llegue al paso de sincronización inteligente, la predicción se realiza con el mejor esfuerzo.

### Mi mensaje estaba planificado para enviarse, pero aún no se ha enviado debido a límites de velocidad u otros retrasos. ¿Qué significa esto para la priorización de otras campañas? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

Braze asume que tu mensaje se envió a la hora planificada originalmente si aún se está procesando, lo que determina si enviar otros mensajes priorizados próximos. Cuando ese mensaje finalmente se envíe, Braze utiliza la hora de envío real.

### Mi mensaje fue priorizado pero cancelado en el último momento. ¿Qué significa eso para la priorización? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Cuando un mensaje es priorizado, Braze asume que se envió a su hora planificada originalmente. En general, para la priorización de mensajes, no recomendamos usar cancelaciones de Liquid. Si un mensaje se cancela debido a la [lógica Liquid de `abort_message`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages), asumiremos que se envió a ese usuario y priorizaremos las Campaigns futuras en consecuencia.

Supongamos que tienes dos mensajes: Mensaje 1 y Mensaje 2. Si el Mensaje 1 se cancela a favor de un futuro Mensaje 2 de mayor prioridad, esto no garantiza que el Mensaje 2 se envíe realmente. El Mensaje 2 aún puede cancelarse por cualquier motivo, incluyendo:

- Cancelaciones de Liquid
- El usuario ya no está en el segmento
- Limitación de frecuencia debido a un mensaje fuera de las reglas de priorización.

Si el Mensaje 2 se cancela, no habrá otro intento de enviar el Mensaje 1.

Ten en cuenta que un usuario podría recibir un mensaje de menor prioridad, pero no un mensaje de mayor prioridad para la misma regla de limitación de frecuencia por las siguientes razones:

- El mensaje de mayor prioridad fue limitado por frecuencia por una regla diferente.
- El mensaje de mayor prioridad entró en conflicto con otra Campaign futura de prioridad aún mayor para una regla diferente.
- En el momento del envío del mensaje de menor prioridad, el usuario no estaba en la audiencia del mensaje de mayor prioridad.
- Ambos mensajes deberían haberse podido enviar, pero un mensaje fuera de la configuración de priorización se envió antes de que el mensaje de mayor prioridad pudiera enviarse.

### ¿Cómo afectan los pasos de límite a la priorización de Canvas? {#how-do-boundary-steps-affect-canvas-prioritization}

Los pasos de límite detienen la evaluación anticipada a través del Canvas hasta que el usuario realmente llegue o complete ese punto en el Canvas. Por ejemplo, si un mensaje de mayor prioridad se encuentra después de un paso de ruta de acción, un retraso personalizado o un paso de experimento, Braze no utiliza ese mensaje posterior para bloquear una Campaign de menor prioridad hasta que el usuario haya avanzado más allá de ese límite.

### ¿Cómo funciona la ramificación en la priorización de Canvas? {#how-does-branching-work-in-canvas-prioritization}

Cuando un Canvas contiene rutas de ramificación, Braze asume que cada ruta es viable y compara el mayor volumen de envío futuro posible por canal. Esto ayuda a evitar enviar un mensaje de menor prioridad ahora si una ruta de Canvas de mayor prioridad podría consumir ese mismo límite de frecuencia más tarde.

### ¿Qué sucede si un usuario tiene múltiples rutas a través de un Canvas priorizado al mismo tiempo? {#what-happens-if-a-user-has-multiple-paths-through-a-prioritized-canvas-at-the-same-time}

Braze trata cada ruta viable como una posible ruta futura y evalúa los pasos de mensaje elegibles en esas rutas de forma independiente. Cuando múltiples rutas pueden enviar en el mismo canal, Braze deduplica esos posibles envíos por canal cuando es necesario.

### ¿Cómo funciona la sincronización inteligente en la priorización de Canvas? {#how-does-intelligent-timing-work-in-canvas-prioritization}

Antes de que un usuario llegue a un paso de mensaje de Canvas con sincronización inteligente, Braze predice el momento de ese paso con el mejor esfuerzo. Una vez que el usuario entra en el paso y Braze calcula la hora de envío por usuario, la priorización de mensajes utiliza esa hora de envío calculada para el paso actual y para los pasos de mensaje siguientes en la misma ruta de priorización determinista.

### ¿Hay alguna funcionalidad de informes o análisis específica para la priorización de mensajes? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

Braze proporciona eventos relacionados con la priorización de mensajes en Currents y el uso compartido de datos para canales compatibles, incluyendo correo electrónico, LINE, notificaciones push, SMS, webhooks y WhatsApp. Estos incluyen eventos de despriorización y limitación de frecuencia, registrados en la tabla `users.messages.<channel>.abort`, así como eventos de reintento que muestran cuándo un mensaje fue reintentado más tarde dentro de la ventana de reintento configurada, registrados en la tabla `user_messages_<channel>_retry`.

Para Campaigns, también puedes utilizar el panel de diagnóstico de mensajería, las estadísticas diarias existentes de despriorización y reintento, y la [funcionalidad de informes de Braze]({{site.baseurl}}/user_guide/analytics/reporting) existente para monitorear la salud y el rendimiento de tus Campaigns y Canvas priorizados.