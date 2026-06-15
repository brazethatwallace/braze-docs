---
article_title: Priorización de mensajes
permalink: /message_prioritization/
toc_headers: h2
description: "Este artículo de referencia describe la priorización de mensajes de nivel superior y cómo configurarla para tu espacio de trabajo."
---

# Priorización de mensajes {#message-prioritization}

> Utiliza la priorización de mensajes para asegurarte de que tus usuarios reciban las Campaigns que más importan.

{% alert important %}
La priorización de mensajes se encuentra actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si te interesa participar en esta beta.
{% endalert %}

Solo los administradores pueden configurar los ajustes de priorización de mensajes de nivel superior. Los usuarios con permisos limitados pueden ver cada página de esta sección, pero no pueden realizar cambios.

Para acceder a los ajustes de priorización de mensajes de nivel superior, ve a **Configuración** > **Priorización de mensajes**.

## Cómo funciona {#how-it-works}

La priorización de mensajes te permite crear [categorías](#categories) y [reglas de priorización](#prioritization-rules) para clasificar cómo se envían tus mensajes.

Supongamos que gestionas promociones por correo electrónico para asociaciones de pago y programas de fidelización de una marca de belleza. Con la priorización de mensajes, podrías crear dos categorías llamadas "Asociaciones de pago" y "Fidelización". Luego podrías clasificar estas categorías en función de cuál es más crítica para tu marca. Por ejemplo, durante la temporada navideña, podrías clasificar "Fidelización" por encima de "Asociaciones de pago" para priorizar a los clientes de tu marca que han formado parte de tu programa de membresía durante más de un año.

![Un ejemplo de reglas de priorización para dos categorías: Asociaciones de pago y Fidelización.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

## Categorías {#categories}

Las reglas de priorización se basan en una clasificación de categorías, que es una etiqueta que puedes asignar a una Campaign determinada (similar a una [etiqueta](https://www.braze.com/docs/user_guide/administrative/app_settings/tags)). Puedes crear hasta 20 categorías en un momento dado.

Para añadir una nueva categoría:

1. Ve a **Configuración** > **Priorización de mensajes** > **Categorías**.
2. Selecciona **Crear nueva categoría**.

![El botón "Crear nueva categoría" en la sección de priorización de mensajes.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Dale a la categoría un nombre y una descripción opcional.
4. Selecciona **Crear categoría**.

![Una categoría de ejemplo llamada "P3" con la descripción "Esta se convertirá en mi tercera categoría de mayor prioridad."]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

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

Para reordenar las reglas, selecciona y arrastra el icono <i class="fa-solid fa-grip-vertical"></i> en la parte superior izquierda de una regla. Para eliminar una regla, selecciona el menú <i class="fas fa-ellipsis-vertical"></i> y luego **Eliminar regla**.

Asegúrate de seleccionar **Guardar** para que se apliquen tus actualizaciones.

## Configuración a nivel de Campaign {#campaign-level-settings}

### Adhesión voluntaria {#opt-in}

{% alert important %}
Solo las Campaigns planificadas de un solo canal pueden adherirse a la priorización en este momento. Las Campaigns basadas en acciones, las desencadenadas por API y los Canvas no son compatibles.
{% endalert %}

Para adherir una Campaign a la priorización, selecciona la casilla **Adhesión voluntaria a la priorización de mensajes** en la página **Planificación de entrega** de la Campaign.

![La casilla de "Adhesión voluntaria a la priorización de mensajes".]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

A continuación, asigna la Campaign a una categoría seleccionando una del menú desplegable **Categoría**.

![La casilla de "Adhesión voluntaria a la priorización de mensajes".]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

Puedes adherir hasta 25 Campaigns activas en un momento dado. Las Campaigns en borrador, detenidas o archivadas no cuentan para este límite.

### Ventana de reintento {#retry-window}

Una ventana de reintento permite que las Campaigns adheridas reintenten durante un máximo de tres días si el primer intento no tiene una prioridad lo suficientemente alta para enviarse. En cada día posterior, a la misma hora en que el mensaje fue planificado originalmente, se intenta enviar el mensaje de nuevo. Después del último día en la ventana de reintento, si el mensaje aún no se ha enviado, no se reintenta más y se desprioriza permanentemente.

La ventana de reintento debe ser más corta que el tiempo entre envíos de esa Campaign. Si tienes una Campaign que se envía cada lunes y miércoles, el intento de reintento ocurre el martes. Esto significa que la ventana de reintento debe configurarse en un día.

![La configuración de "Ventana de reintento" establecida en 1 día.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

## Limitación de frecuencia {#frequency-caps}

### Para Campaigns {#for-campaigns}

Para ser elegible para la priorización de mensajes, una Campaign debe estar adherida a la limitación de frecuencia. Puedes confirmar que la Campaign está adherida dentro de la sección **Controles de entrega** de la página **Planificación de entrega**.

![Un ejemplo de la regla de limitación de frecuencia para cualquier canal aplicable y sin filtros adicionales.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

### Reglas de limitación de frecuencia {#frequency-capping-rules}

Optimizaremos la prioridad dentro de tus reglas de limitación de frecuencia existentes. Aunque no es obligatorio, recomendamos encarecidamente que configures al menos una regla de limitación de frecuencia que capture todos los mensajes independientemente del canal, la etiqueta o la categoría. Esta regla de limitación de frecuencia capturará cada mensaje adherido a la priorización de mensajes para que los mensajes priorizados se comparen entre sí, no solo con otros mensajes que comparten las mismas características.

Para configurar esto, ve a **Configuración** > **Reglas de limitación de frecuencia**. Crea una regla donde el canal sea **Cualquier canal aplicable** y los filtros adicionales sean **Ninguno**.

![Un ejemplo de la regla de limitación de frecuencia para cualquier canal aplicable y sin filtros adicionales.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization11.png %})

También puedes crear reglas de limitación de frecuencia por categoría. Esto te permite gestionar tus mensajes de marketing para evitar enviar demasiados mensajes de una categoría determinada solo porque está marcada como de alta prioridad. Selecciona **Categoría de priorización de mensajes** en **Filtros adicionales** y selecciona una categoría del menú desplegable.

![Un ejemplo de la regla de limitación de frecuencia con el menú desplegable del campo "Categoría" para seleccionar P2 o P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

Los mensajes fuera de la priorización de mensajes compartirán los límites de frecuencia con los mensajes priorizados, por lo que incluso un mensaje de alta prioridad puede ser cancelado debido a un mensaje fuera de la priorización de mensajes.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cómo se resuelven los empates entre mensajes de la misma categoría? {#how-are-ties-broken-between-messages-in-the-same-category}

Al priorizar dos mensajes de la misma categoría entre sí, daremos mayor prioridad al mensaje con la hora de envío más temprana. Para Campaigns recurrentes, la hora de envío se calcula como la próxima ocurrencia a partir de la medianoche de hoy en la hora de la empresa. Para Campaigns planificadas en hora local, asumiremos una hora de envío en la hora de la empresa.

### ¿Cuál es la relación entre la priorización de mensajes y la limitación de frecuencia? {#what-is-the-relationship-between-message-prioritization-and-frequency-capping}

En el momento del envío, compararemos el mensaje que se está enviando con otros mensajes que el usuario es elegible para recibir, que siguen la misma regla de limitación de frecuencia y están adheridos a la priorización de mensajes. El mensaje se enviará si:

1. La regla de limitación de frecuencia relevante aún no se ha alcanzado para ese usuario, y
2. Enviar este mensaje a este usuario no haría que se alcanzara un límite antes de que se envíe un mensaje posterior de mayor prioridad.

### ¿Cómo puedo asegurarme de que un mensaje siempre se envíe? {#how-can-i-make-sure-a-message-is-always-sent}

Puede haber algunos escenarios en los que quieras que un mensaje siempre se envíe, como en el caso de notificaciones transaccionales o legales. En este caso, debes excluir el mensaje de la limitación de frecuencia (lo que también lo hace no elegible para la priorización de mensajes). Esto enviará el mensaje siempre que esté planificado o desencadenado sin considerar qué más se está enviando.

### ¿Cuándo se priorizan realmente los mensajes? ¿Hay un horario? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Cada mensaje se prioriza en su propia hora de envío planificada. No hay un momento de evaluación universal para los mensajes priorizados.

### Mi mensaje estaba planificado para enviarse, pero aún no se ha enviado debido a límites de velocidad u otros retrasos. ¿Qué significa esto para la priorización de otras Campaigns? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

Asumiremos que tu mensaje se envió a la hora planificada originalmente si aún se está procesando. Usaremos esa suposición para determinar si enviar otros mensajes priorizados próximos. Cuando ese mensaje finalmente se envíe, usaremos la hora de envío real.

### Mi mensaje fue priorizado pero cancelado en el último momento. ¿Qué significa eso para la priorización? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Cuando un mensaje es priorizado, Braze asumirá que se envió a su hora planificada originalmente. En general, para la priorización de mensajes, no recomendamos usar cancelaciones de Liquid. Si un mensaje se cancela debido a la [lógica Liquid de `abort_message`](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages), asumiremos que se envió a ese usuario y priorizaremos las Campaigns futuras en consecuencia.

Supongamos que tienes dos mensajes: Mensaje 1 y Mensaje 2. Si el Mensaje 1 se cancela a favor de un futuro Mensaje 2 de mayor prioridad, esto no garantiza que el Mensaje 2 se envíe realmente. El Mensaje 2 aún puede cancelarse por cualquier motivo, incluyendo:

- Cancelaciones de Liquid
- El usuario ya no está en el Segment
- Limitación de frecuencia debido a un mensaje fuera de las reglas de priorización.

Si el Mensaje 2 se cancela, no habrá otro intento de enviar el Mensaje 1.

Ten en cuenta que un usuario podría recibir un mensaje de menor prioridad, pero no un mensaje de mayor prioridad para la misma regla de limitación de frecuencia por las siguientes razones:

- El mensaje de mayor prioridad fue limitado por frecuencia por una regla diferente.
- El mensaje de mayor prioridad entró en conflicto con otra Campaign futura de prioridad aún mayor para una regla diferente.
- En el momento del envío del mensaje de menor prioridad, el usuario no estaba en la audiencia del mensaje de mayor prioridad.
- Ambos mensajes deberían haberse podido enviar, pero un mensaje fuera de la configuración de priorización se envió antes de que el mensaje de mayor prioridad pudiera enviarse.

### ¿Puedo adherir Canvas a la priorización de mensajes? {#can-i-opt-canvases-into-message-prioritization}

No. En este momento, no puedes adherir Canvas a la priorización de mensajes.

### ¿Qué pasa con las Campaigns basadas en acciones o desencadenadas por API? {#what-about-action-based-or-api-triggered-campaigns}

En este momento, la priorización de mensajes no es compatible con las Campaigns basadas en acciones o desencadenadas por API.

### ¿Hay alguna funcionalidad de informes o análisis específica para la priorización de mensajes? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

En este momento, no hay funcionalidad de informes o análisis específica para esta característica. Te animamos a utilizar la [funcionalidad de informes de Braze](https://www.braze.com/docs/user_guide/analytics/reporting) existente para monitorear la salud y el rendimiento de tus Campaigns priorizadas.