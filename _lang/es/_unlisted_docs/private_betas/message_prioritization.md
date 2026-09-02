---
article_title: Priorización de mensajes
permalink: /message_prioritization/
toc_headers: h2
description: "Este artículo de referencia describe la priorización de mensajes de nivel superior y cómo configurarla para tu espacio de trabajo."
---

# Priorización de mensajes {#message-prioritization}

> Utiliza la priorización de mensajes para asegurarte de que los usuarios reciban los mensajes que más importan para tu negocio, no solo los que se envían primero.

{% alert important %}
La priorización de mensajes se encuentra actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si te interesa participar en esta beta.<br><br>Este artículo refleja la versión de la priorización de mensajes planificada para su lanzamiento en producción a finales de julio de 2026. Algunos comportamientos descritos aquí pueden no estar disponibles aún en todos los espacios de trabajo en beta.
{% endalert %}

## ¿Por qué usar la priorización de mensajes? {#why-use-message-prioritization}

Los usuarios solo pueden recibir cierta cantidad de mensajes antes de que el volumen se convierta en un problema. Los mensajes que les llegan deberían ser los que más importan para tu negocio. La priorización de mensajes ayuda a garantizar que tus mensajes de mayor valor ganen ese espacio limitado, en lugar de dejarlo al azar.

La mayoría de los equipos controlan el volumen de mensajes con la limitación de frecuencia. Por sí sola, la limitación de frecuencia es un instrumento poco preciso. Una vez que un usuario alcanza su límite, el momento del envío decide qué mensajes se entregan, no la importancia para el negocio.

Una promoción de bajo valor que se dispara primero puede ocupar un espacio que una recompensa de fidelización o un mensaje urgente habría utilizado más tarde ese día. Los equipos suelen sortear esto con reglas de límite separadas, programación manual y filtros ad hoc. Estos enfoques requieren mantenimiento constante. Se vuelven más difíciles de gestionar a medida que las Campaigns y los Canvas cambian. Y aun así no pueden garantizar que el mensaje correcto gane.

La priorización de mensajes cambia la asignación de la limitación de frecuencia de **primero en llegar, primero en servirse** a **consciente de la prioridad del negocio**: tú defines lo que importa, y Braze toma las decisiones de envío por ti.

La priorización de mensajes ofrece varios beneficios:

- **Define lo que importa una sola vez:** Usa categorías y reglas ordenadas para codificar tus prioridades, por ejemplo, "Fidelización" sobre "Asociaciones pagadas". Cada envío con adhesión voluntaria respeta esas clasificaciones automáticamente.
- **Decisiones con visión de futuro:** Braze predice lo que un usuario puede recibir más adelante. Puede retener un mensaje de menor prioridad para preservar espacio del límite para uno de mayor prioridad.
- **Funciona en distintos tipos de mensajes y canales:** Campaigns programadas, Campaigns basadas en acciones y pasos en Canvas compiten en un único grupo ordenado dentro de tus límites de frecuencia compartidos.
- **Ventanas de reintento:** Un mensaje despriorizado puede reintentarse si se libera capacidad. Esto mejora la combinación de mensajes sin descartar por completo los envíos de menor prioridad.

El resultado es el mismo volumen de envío limitado, asignado automáticamente a los mensajes que más importan.

La priorización de mensajes es más valiosa para remitentes de alto volumen que alcanzan regularmente los límites de frecuencia. Funciona mejor cuando el valor de los mensajes está claramente diferenciado, por ejemplo, mensajes de fidelización o generadores de ingresos frente a promociones rutinarias.

## Cómo funciona {#how-it-works}

Usa la priorización de mensajes para crear [categorías](#categories) y [reglas de priorización](#prioritization-rules) que clasifiquen cómo se envían tus mensajes.

Para gestionar estos ajustes, ve a **Configuración** > **Priorización de mensajes**. Solo los administradores pueden configurar los ajustes de nivel superior de priorización de mensajes. Los usuarios necesitan el permiso "View Message Prioritization" para ver los ajustes de esta sección y el permiso "Edit Message Prioritization" para editarlos.

Por ejemplo, una marca de belleza que gestiona promociones por correo electrónico para asociaciones de pago y programas de fidelización usa la priorización de mensajes para crear dos categorías: "Paid Partnerships" y "Loyalty". La marca clasifica estas categorías por importancia empresarial. Durante la temporada navideña, clasifica "Loyalty" en primer lugar y "Paid Partnerships" en segundo para priorizar a los miembros a largo plazo.

![Un ejemplo de reglas de priorización para dos categorías: Paid Partnerships y Loyalty.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

En el momento del envío, Braze compara el mensaje que se está enviando con otros mensajes que el usuario podría recibir y que estén incluidos en la priorización, tengan una categoría de prioridad configurada y cuenten para la misma regla de limitación de frecuencia dentro de la misma ventana de limitación de frecuencia. Si enviar el mensaje actual impediría que un mensaje de mayor prioridad se envíe más adelante, Braze resta prioridad al mensaje de menor prioridad. Dependiendo de la ventana de reintentos configurada, ese mensaje de menor prioridad se reintenta más tarde o no se envía.

La priorización de mensajes puede evaluar:

- Campaigns programadas
- Campaigns basadas en acciones
- Canvas

Actualmente, las Campaigns activadas por API o los Canvas no son compatibles con la priorización de mensajes y no participarán en la priorización.

Braze utiliza su predicción de cuándo se espera que se envíe cada mensaje al evaluar si enviar un mensaje ahora podría impedir que un mensaje de mayor prioridad se envíe más adelante. Para más información sobre cómo Braze predice la sincronización de envío futuro para Campaigns y Canvas, consulta [¿Cómo predice Braze cuándo se envía un mensaje futuro?](#how-does-braze-predict-when-a-future-message-sends)

### Canales de mensajes compatibles {#supported-message-channels}

La priorización de mensajes es compatible con los mismos canales que la limitación de frecuencia:

- Notificaciones push
- Correo electrónico
- SMS
- Webhooks
- WhatsApp
- LINE

Para la priorización y la limitación de frecuencia, las notificaciones push de iOS, Android, web y otras plataformas de notificaciones push se tratan como un único canal push compartido, no como canales separados.

Estos canales no son elegibles para la priorización de mensajes porque no están sujetos a la limitación de frecuencia:

- Content Cards
- Mensajes dentro de la aplicación
- Banners

Los mensajes dentro de la aplicación y los Banners usan sus propios ajustes de prioridad para decidir qué mensaje se muestra cuando varios mensajes compiten por el mismo desencadenante o ubicación. Para mensajes dentro de la aplicación, consulta [Elegir una prioridad]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority). Para Banners, consulta [Prioridad de Banner]({{site.baseurl}}/user_guide/channels/banners#priority).

Si una Campaign o un paso en Canvas utiliza solo canales no elegibles, no participará en la priorización.

## Categorías {#categories}

Las reglas de priorización se basan en una clasificación de categorías, que son etiquetas que puedes asignar a una Campaign o Canvas determinada (similar a una [etiqueta]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)). Hay un límite en la cantidad de categorías que puedes crear en un momento dado; habla con tu director de cuentas si deseas un límite más alto.

Para añadir una nueva categoría:

1. Ve a **Configuración** > **Priorización de mensajes** > **Categorías**.
2. Selecciona **Crear nueva categoría**.

![El botón "Crear nueva categoría" en la sección Priorización de mensajes.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Dale a la categoría un nombre y una descripción opcional.
4. Selecciona **Crear categoría**.

![Una categoría de ejemplo llamada "P3" con la descripción "Esta es mi tercera categoría de mayor prioridad."]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

Para editar o eliminar una categoría, selecciona el menú <i class="fas fa-ellipsis-vertical" aria-label="Más opciones"></i>.

## Reglas de priorización {#prioritization-rules}

Una vez que tus categorías estén configuradas, puedes clasificarlas en un conjunto de reglas de priorización. Las reglas se clasifican en orden descendente de prioridad. Hay un límite en la cantidad de reglas de priorización que puedes crear en un momento determinado; habla con tu director de cuentas si deseas un límite más alto.

1. Ve a **Configuración** > **Priorización de mensajes** > **Reglas de priorización** para configurar tus reglas.

![Sección "Reglas de priorización" sin prioridades configuradas aún.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. Selecciona **Agregar regla**.
3. Selecciona una categoría en el menú desplegable.

![Regla de priorización "Prioridad 1" con P1 seleccionada como categoría.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. Continúa agregando reglas seleccionando **+ Agregar regla** debajo de tu última regla.

Para reordenar las reglas, selecciona y arrastra el icono <i class="fa-solid fa-grip-vertical" aria-label="Arrastrar para reordenar"></i> de una regla. Para eliminar una regla, selecciona el menú <i class="fas fa-ellipsis-vertical" aria-label="Más opciones"></i> y luego **Eliminar regla**.

Asegúrate de seleccionar **Guardar** para que se apliquen tus actualizaciones.

## Límites de frecuencia {#frequency-caps}

La priorización de mensajes funciona dentro de tus reglas de limitación de frecuencia existentes. Para ser elegible para la priorización, una Campaign o un paso en Canvas debe usar un canal compatible y estar sujeta a tu configuración de limitación de frecuencia. Los mensajes que no están sujetos a la limitación de frecuencia no son elegibles para la priorización de mensajes. Si quieres que un mensaje se envíe siempre, exclúyelo de la limitación de frecuencia. Esto también lo elimina de la priorización de mensajes.

Un mensaje priorizado solo puede enviarse si:

1. La regla de limitación de frecuencia correspondiente aún no se ha alcanzado para ese usuario, y
2. El envío de ese mensaje no haría que el usuario alcanzara un límite antes de que pueda enviarse un mensaje posterior de mayor prioridad.

![Un ejemplo de una regla de limitación de frecuencia.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

Puedes usar reglas de limitación de frecuencia específicas por canal, reglas específicas por categoría, filtros de etiquetas o reglas que se apliquen a cualquier canal. La priorización de mensajes funciona con las reglas que apliquen a tus mensajes incluidos.

También puedes crear reglas de limitación de frecuencia por categoría para gestionar cuántos mensajes recibe un usuario de una categoría determinada. Esto ayuda a evitar que una categoría de alta prioridad envíe demasiados mensajes. Selecciona **Message prioritization category** en **Additional filters** y selecciona una categoría en el menú desplegable.

![Un ejemplo de la regla de limitación de frecuencia con el menú desplegable del campo "Category" para seleccionar P2 o P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

## Adhesión voluntaria {#opting-in}

### Adhesión voluntaria de Campaign {#campaign-opt-in}

Para que una Campaign se adhiera a la priorización, selecciona la casilla **Opt-in to Message Prioritization** en la configuración de entrega de la Campaign.

![La casilla "Opt-in to Message Prioritization".]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

A continuación, asigna la Campaign a una categoría seleccionando una en el desplegable **Category**.

![El desplegable de categoría de priorización de mensajes en la configuración de entrega de una Campaign.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

La priorización de mensajes es compatible con Campaigns programadas y Campaigns basadas en acciones. Las Campaigns activadas por API no son compatibles.

### Adhesión voluntaria de Canvas {#canvas-opt-in}

La adhesión voluntaria de Canvas funciona de forma similar a la de Campaigns. Para que un Canvas se adhiera a la priorización de mensajes, habilita la priorización de mensajes en la configuración del Canvas y asigna el Canvas a una categoría. Todos los pasos en el Canvas comparten esa categoría y el mismo nivel de prioridad, lo que significa que no puedes establecer la prioridad de forma individual por paso.

La priorización de mensajes es compatible con Canvas programados y Canvas basados en acciones. Los Canvas activados por API no son compatibles.

## Sincronización inteligente {#intelligent-timing}

Con la sincronización inteligente, Braze envía un mensaje en el momento óptimo de envío de cada usuario, por lo que la misma Campaign o paso de mensaje en Canvas puede llegar a diferentes usuarios en diferentes momentos. La priorización de mensajes tiene esto en cuenta: en lugar de asumir que el mensaje se envía a todos en su hora programada, clasifica los mensajes en competencia de un usuario utilizando el momento óptimo de envío de ese usuario.

Para Campaigns y pasos de mensaje en Canvas que utilizan la sincronización inteligente, Braze predice el momento de envío con el mejor esfuerzo posible hasta que calcula el momento de envío por usuario para cada usuario. Para Campaigns, la priorización de mensajes utiliza el momento óptimo de envío de ese usuario para la ocurrencia actual al comparar la Campaign con los otros mensajes priorizados elegibles del usuario. Para Campaigns recurrentes con sincronización inteligente, Braze utiliza el momento óptimo de envío elegido para esa ocurrencia.

Para pasos de mensaje en Canvas, Braze actualiza esta predicción una vez que el usuario entra en el paso y Braze calcula el momento óptimo de envío de ese usuario para el paso. La priorización de mensajes utiliza ese momento de envío calculado para el paso actual. En rutas deterministas (rutas sin ramificación, donde la secuencia de pasos es fija), Braze también refleja esa sincronización actualizada en los pasos de mensaje siguientes al determinar sus momentos de envío esperados.

## Ventanas de reintento {#retry-windows}

Una ventana de reintento permite que los mensajes con adhesión voluntaria se reintenten durante un número limitado de días si el primer intento no tiene la prioridad suficiente para enviarse. La duración máxima de la ventana de reintento depende de tu edición de la plataforma Braze. Cada día subsiguiente, a la misma hora en que el mensaje fue originalmente programado o desencadenado para enviarse, se intenta enviar el mensaje de nuevo. Después del último día en la ventana de reintento, si el mensaje aún no se ha enviado, no se reintenta más y se desprioriza permanentemente.

Para Campaigns programadas recurrentes, la ventana de reintento debe ser más corta que el tiempo mínimo entre envíos de esa Campaign. Los reintentos siempre ocurren un día a la vez desde la hora de envío original, incluso si la Campaign no está normalmente programada para enviarse ese día. Por ejemplo, si tienes una Campaign que se envía cada lunes y miércoles, el intento de reintento ocurre el martes, por lo que la ventana de reintento debe establecerse en un día. Si tienes una Campaign que se envía cada lunes, miércoles y viernes, y el envío del viernes se reintenta con una ventana de reintento de un día, el intento de reintento ocurre el sábado, no el lunes.

![La configuración "Ventana de reintento" establecida en 1 día.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

Para Campaigns basadas en acciones, los reintentos se basan en la hora en que se esperaba originalmente que se enviara el mensaje desencadenado.

Las Campaigns basadas en acciones que utilizan eventos de excepción no admiten ventanas de reintento.

Las ventanas de reintento para los mensajes de Canvas se configuran a nivel de paso. Para los pasos de mensajería de Canvas compatibles, si un paso de mensaje de Canvas se desprioriza y tiene una ventana de reintento configurada, Braze puede reintentar ese paso más tarde dentro de su ventana de reintento.

## Cómo evalúa Braze los mensajes {#how-braze-evaluates-messages}

{% alert tip %}
No necesitas entender todo en esta sección para usar la priorización de mensajes. Una vez que configures tus categorías y reglas y habilites tus mensajes, Braze evalúa y prioriza los mensajes automáticamente y hace todo lo posible por enviar los que más importan. Los detalles aquí son para cuando quieras entender cómo se toman esas decisiones.
{% endalert %}

Cuando un usuario es elegible para múltiples mensajes priorizados, Braze evalúa conjuntamente las Campaigns habilitadas y los pasos de mensaje de Canvas elegibles en los canales compatibles.

Para Campaigns, esto incluye los envíos programados y basados en acciones que sean elegibles.

Para Canvas, esto incluye:

- Canvas programados futuros para los que el usuario es elegible
- Canvas en los que el usuario se encuentra actualmente

La priorización de Canvas no es de todo o nada. Una Campaign de mayor prioridad puede provocar que un paso de Canvas se despriorice, mientras que pasos elegibles posteriores en ese mismo Canvas aún pueden enviarse, dependiendo de la clasificación de categoría, el momento del envío y las reglas de limitación de frecuencia.

Braze compara los mensajes priorizados solo cuando comparten la misma regla de limitación de frecuencia aplicable. Por ejemplo, dos Campaigns de correo electrónico que cuentan para la misma regla de limitación de frecuencia de correo electrónico pueden priorizarse entre sí, pero una Campaign de correo electrónico de menor prioridad no se desprioriza a favor de un mensaje SMS de mayor prioridad a menos que ambos cuenten para la misma regla. Los mensajes fuera de la priorización de mensajes también comparten estos límites de frecuencia, por lo que incluso un mensaje de alta prioridad puede cancelarse debido a un mensaje fuera de la priorización de mensajes.

Braze evalúa Campaigns y Canvas de manera diferente, porque un Canvas puede ramificarse y desarrollarse con el tiempo.

### Evaluar Campaigns {#evaluating-campaigns}

Braze compara cada mensaje de Campaign elegible utilizando la hora en la que se espera que se envíe ese mensaje.

### Evaluar Canvas {#evaluating-canvases}

Para evaluar un Canvas, Braze realiza una **anticipación**: recorre el Canvas desde un punto de partida para predecir qué mensajes futuros puede recibir un usuario, y cuándo. La anticipación comienza desde:

- La entrada al Canvas, para Canvas programados futuros
- El paso actual del usuario, si el usuario ya está en el Canvas

A medida que avanza, Braze trata cada tipo de paso en Canvas de manera diferente. El tipo de paso determina si la anticipación lo cuenta, lo omite, se detiene en él o se divide en múltiples rutas:

| Categoría de paso | Efecto en la anticipación |
|---|---|
| Pasos de mensajería | Se cuentan como mensajes elegibles para la priorización |
| Pasos de continuación | Se omiten; la anticipación pasa a través de ellos |
| Pasos de límite | La anticipación se detiene hasta que el usuario supera el paso |
| Pasos de ramificación | La anticipación sigue todas las rutas posibles |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Evaluación de Canvas" }

#### Pasos de mensajería {#messaging-steps}

Estos pasos se cuentan para la priorización y se agregan al conjunto de mensajes elegibles cuando envían en un canal compatible.

- Paso de mensaje
- Paso de Content Optimizer

#### Pasos de continuación {#continuation-steps}

Estos pasos se ignoran para la priorización y no afectan la anticipación.

- Paso de actualización de contexto
- Paso de actualización de usuario
- Paso de Audience Sync
- Paso de conmutador de características
- Paso de retraso con un retraso fijo

#### Pasos de límite {#boundary-steps}

Braze detiene la anticipación en estos pasos hasta que el usuario realmente avanza a través de ellos en el Canvas.

- Paso de retraso con un retraso personalizado
- Paso de retraso que sigue a un paso de ramificación
- Paso de ruta de acción
- Paso de experimento

#### Pasos de ramificación {#branching-steps}

Estos pasos dividen el Canvas en múltiples rutas posibles.

- Paso de división de decisiones
- Paso de ruta de audiencia

Cuando una ruta de priorización contiene pasos de ramificación, Braze asume que todas las rutas son viables y considera todos los pasos de mensaje paralelos en canales compatibles para la priorización. Dado que las reglas de limitación de frecuencia pueden ser específicas de un canal, los pasos de mensaje paralelos se desduplican por canal cuando es necesario.

Por ejemplo, si una rama puede enviar correo electrónico y otra rama también puede enviar correo electrónico, Braze los trata como un único posible envío de correo electrónico durante la anticipación. Si otra rama puede enviar push, Braze también considera ese posible envío push por separado.

Para los pasos de mensaje en Canvas que usan sincronización inteligente, Braze utiliza la hora de envío calculada de cada usuario una vez que el usuario alcanza el paso. Para más detalles, consulta [Sincronización inteligente](#intelligent-timing).

Los pasos de Content Optimizer se tratan como pasos de mensajería porque siempre envían en un canal especificado. Sin embargo, las ventanas de reintento no se aplican a los pasos de Content Optimizer porque reintentar interferiría con el experimento. Otros pasos de mensajería de Canvas compatibles pueden usar ventanas de reintento. Los pasos en Canvas en canales no compatibles no participan en la priorización de mensajes.

## Ejemplos {#examples}

### Campaign de mayor prioridad frente a Campaign de menor prioridad {#higher-priority-campaign-versus-lower-priority-campaign}

Supongamos que un usuario es elegible para dos Campaigns de correo electrónico el mismo día, y ambas Campaigns cuentan para la misma regla de limitación de frecuencia. Si se espera que la Campaign de mayor prioridad se envíe más tarde ese día, Braze puede reducir la prioridad de la Campaign de menor prioridad para que la Campaign de mayor prioridad pueda enviarse en su lugar. Si la Campaign de menor prioridad tiene una ventana de reintento, Braze puede intentarlo de nuevo más tarde.

### Campaign basada en acciones de mayor prioridad frente a mensaje de menor prioridad {#higher-priority-action-based-campaign-versus-lower-priority-message}

Supongamos que un usuario desencadena una Campaign basada en acciones de mayor prioridad que está configurada para enviarse dos horas después. Durante ese retraso, Braze puede considerar esa próxima Campaign basada en acciones al decidir si otro mensaje priorizado debe enviarse primero. Esto ayuda a evitar que un mensaje de menor prioridad se envíe ahora si se espera que la Campaign basada en acciones de mayor prioridad se envíe pronto.

### Canvas de mayor prioridad frente a Campaign de menor prioridad {#higher-priority-canvas-versus-lower-priority-campaign}

Supongamos que un usuario es elegible para una Campaign de menor prioridad, pero también se espera que reciba un mensaje de Canvas de mayor prioridad más tarde ese día. Si Braze ya puede evaluar ese futuro mensaje de Canvas, puede reducir la prioridad de la Campaign de menor prioridad para que el mensaje de Canvas de mayor prioridad pueda enviarse en su lugar.

### Canvas de mayor prioridad con un paso de límite frente a Campaign de menor prioridad {#higher-priority-canvas-with-a-boundary-step-versus-lower-priority-campaign}

Supongamos que un Canvas de mayor prioridad incluye un paso de ruta de acción, un experimento o un retraso personalizado antes de su siguiente paso de mensaje. Hasta que el usuario alcance y supere ese paso, Braze no anticipa el mensaje del Canvas de mayor prioridad que está más adelante en el flujo. En ese caso, una Campaign de menor prioridad aún puede enviarse primero.

### Canvas de mayor prioridad con ramificación frente a mensaje de menor prioridad {#higher-priority-branching-canvas-versus-lower-priority-message}

Supongamos que un Canvas de mayor prioridad puede enviar diferentes mensajes dependiendo de la rama que siga un usuario. Braze evalúa esas posibles rutas futuras de manera conservadora al comparar mensajes. Esto ayuda a evitar que un mensaje de menor prioridad se envíe ahora si una rama del Canvas de mayor prioridad podría usar esa misma limitación de frecuencia más tarde.

### Paso en Canvas con sincronización inteligente y pasos posteriores {#canvas-step-with-intelligent-timing-and-downstream-steps}

Supongamos que un usuario entra en un paso de mensaje de Canvas de mayor prioridad que utiliza sincronización inteligente. Una vez que Braze calcula la hora de envío de ese usuario para el paso con sincronización inteligente, la priorización de mensajes utiliza esa hora de envío por usuario para el paso actual y para los pasos de mensaje posteriores en la misma ruta determinista. Esto ayuda a Braze a comparar los mensajes del Canvas que están más adelante en el flujo con otros envíos priorizados utilizando la sincronización actualizada en lugar de solo la estimación de ruta anterior.

## Limitaciones {#limitations}

La priorización de mensajes tiene los siguientes límites de característica. Los límites específicos dependen de tu edición de la plataforma Braze; contacta a tu director de cuentas de Braze para más detalles.

- Un límite en el número de Campaigns y Canvas programados activos con adhesión voluntaria (combinados)
- Un límite en el número de Campaigns y Canvas activos basados en acciones con adhesión voluntaria (combinados)
- Un límite en el número de decisiones de priorización por mes
- Un límite en el número de categorías por espacio de trabajo
- Un límite en el número de reglas de priorización por espacio de trabajo
- Una duración máxima de la ventana de reintento

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cómo se desempatan los mensajes con la misma prioridad dentro de la misma categoría? {#how-are-ties-in-priority-broken-between-messages-in-the-same-category}

Al priorizar dos Campaigns en la misma categoría entre sí, Braze da mayor prioridad a la que tiene la hora de envío más temprana. Si se configura una ventana de reintento, Braze utiliza el final de esa ventana de reintento al comparar Campaigns dentro de la misma regla de prioridad. Para Campaigns recurrentes, la hora de envío se calcula como la siguiente ocurrencia a partir de la medianoche en la hora de la empresa. Para Campaigns programadas en hora local, Braze asume una hora de envío en la hora de la empresa.

Para Canvas en la misma categoría, Braze utiliza el momento de entrada al Canvas como criterio de desempate, de modo que todos los pasos del mismo Canvas conserven la misma prioridad relativa frente a otros Campaigns y Canvas.

### ¿Cómo puedo asegurarme de que un mensaje siempre se envíe? {#how-can-i-make-sure-a-message-is-always-sent}

Puede haber algunos escenarios en los que quieras que un mensaje se envíe siempre, como en el caso de notificaciones transaccionales o legales. En este caso, debes excluir el mensaje de la limitación de frecuencia, lo que también lo hace inelegible para la priorización de mensajes. Esto envía el mensaje siempre que esté programado o se desencadene, sin considerar qué más se está enviando.

### ¿Cuándo se priorizan realmente los mensajes? ¿Hay un horario? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Cada mensaje se prioriza en función de cuándo se espera que se envíe. No hay un momento de evaluación universal para los mensajes priorizados.

### ¿Cómo predice Braze cuándo se envía un mensaje futuro? {#how-does-braze-predict-when-a-future-message-sends}

Braze predice el momento de envío futuro de forma diferente para cada tipo de mensaje:

- **Campaigns programadas:** Braze utiliza la hora en que se espera que se envíe cada Campaign. Para Campaigns programadas que usan sincronización inteligente, Braze utiliza la hora óptima de envío de cada usuario para esa ocurrencia de Campaign.
- **Campaigns basadas en acciones:** Braze utiliza la hora en que se espera que se envíe cada mensaje desencadenado, incluyendo cualquier retraso configurado entre el desencadenante y el envío.
- **Pasos en Canvas:** Braze utiliza la entrada del usuario al Canvas o la posición actual en el Canvas, más el momento de los pasos posteriores. Para los pasos de mensaje en Canvas que usan sincronización inteligente, una vez que un usuario ingresa a ese paso, Braze utiliza la hora de envío por usuario que calcula para ese usuario. Para los pasos de mensaje siguientes en la misma ruta determinista, Braze utiliza esa hora de envío de sincronización inteligente al determinar la hora de envío esperada posterior. Antes de que un usuario llegue al paso con sincronización inteligente, la predicción se realiza con el mejor esfuerzo posible.

### Mi mensaje ya estaba programado para enviarse, pero aún no se ha enviado por límites de velocidad u otros retrasos. ¿Qué significa esto para la priorización de otros Campaigns? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

Braze asume que tu mensaje se envió a la hora programada originalmente si aún está en procesamiento, lo que determina si se envían otros mensajes priorizados próximos. Cuando ese mensaje finalmente se envíe, Braze utiliza la hora de envío real.

### Mi mensaje fue priorizado pero se canceló en el último momento. ¿Qué significa eso para la priorización? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Cuando un mensaje se prioriza, Braze asume que se envió a la hora programada originalmente. En general, para la priorización de mensajes, no recomendamos usar cancelaciones de Liquid. Si un mensaje se cancela debido a la [lógica Liquid `abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages), asumimos que se envió a ese usuario y priorizamos los Campaigns futuros en consecuencia.

Supongamos que tienes dos mensajes: Mensaje 1 y Mensaje 2. Si el Mensaje 1 se cancela en favor de un Mensaje 2 de mayor prioridad futuro, esto no garantiza que el Mensaje 2 realmente se envíe. El Mensaje 2 aún puede cancelarse por cualquier razón, incluyendo:

- Mensajes de cancelación de Liquid
- El usuario ya no está en el Segment
- Limitación de frecuencia debido a un mensaje fuera de las reglas de priorización.

Si el Mensaje 2 se cancela, no hay otro intento de enviar el Mensaje 1.

Ten en cuenta que un usuario podría recibir un mensaje de menor prioridad, pero no un mensaje de mayor prioridad para la misma regla de limitación de frecuencia por las siguientes razones:

- El mensaje de mayor prioridad fue limitado por frecuencia por una regla diferente.
- El mensaje de mayor prioridad entró en conflicto con otro Campaign futuro de prioridad aún mayor para una regla diferente.
- En el momento del envío del mensaje de menor prioridad, el usuario no estaba en la audiencia del mensaje de mayor prioridad.
- Ambos mensajes deberían haberse podido enviar, pero un mensaje fuera de la configuración de priorización se envió antes de que el mensaje de mayor prioridad pudiera enviarse.

### ¿Cómo funciona la sincronización inteligente con la priorización de mensajes? {#how-does-intelligent-timing-work-with-message-prioritization}

Para Campaigns, la priorización de mensajes utiliza la hora óptima de envío de cada usuario para la ocurrencia actual. Para los pasos de mensaje en Canvas, Braze utiliza la hora de envío calculada de cada usuario una vez que el usuario llega al paso, y refleja ese momento en los pasos de mensaje siguientes en la misma ruta determinista. Para más detalles, consulta [Sincronización inteligente](#intelligent-timing).

### ¿Hay alguna funcionalidad de informes o análisis específica para la priorización de mensajes? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

Braze proporciona eventos relacionados con la priorización de mensajes en Currents y compartición de datos para los canales compatibles, incluyendo correo electrónico, LINE, notificaciones push, SMS, webhooks y WhatsApp. Estos incluyen eventos de despriorización y limitación de frecuencia, registrados como el evento `users.messages.<channel>.Abort`, así como eventos de reintento que muestran cuándo un mensaje fue reintentado posteriormente dentro de la ventana de reintento configurada, registrados como el evento `users.messages.<channel>.Retry`.

También puedes usar el panel de diagnóstico de mensajería, las estadísticas diarias existentes de mensajes despriorizados y reintentados, y la [funcionalidad de informes de Braze]({{site.baseurl}}/user_guide/analytics/reports) existente para monitorear el estado y el rendimiento de tus Campaigns y Canvas priorizados.