---
nav_title: Lista de verificación previa y posterior al lanzamiento
article_title: Lista de verificación previa y posterior al lanzamiento
page_order: 2
description: "Este artículo proporciona una guía de aspectos a verificar antes y después de lanzar un Canvas."
tool: Canvas

---

# Lista de verificación previa y posterior al lanzamiento {#pre-and-post-launch-checklist}

> Este artículo proporciona una guía de aspectos a verificar antes y después de lanzar un Canvas.

## Aspectos a considerar antes del lanzamiento {#things-to-consider-before-launch}

Antes de lanzar un Canvas, hay varios detalles que puedes verificar para asegurarte de que tu mensajería y los horarios de envío se alineen con las preferencias de tu audiencia. Los aspectos a considerar incluyen variaciones en zonas horarias, configuración de entrada y más. Usando esta lista de verificación como guía, ajusta estas áreas según tu caso de uso para contribuir al éxito de tu Canvas.

### Revisa la configuración de zona horaria {#review-time-zone-settings}

Si estás ingresando usuarios según su zona horaria local usando un horario de entrada planificado, deberías lanzar tu Canvas al menos 24 horas antes de cuando quieras que los usuarios entren a tu Canvas. Por ejemplo, aquí hay un Canvas que no ha dejado suficiente tiempo entre el lanzamiento y el horario de entrada planificado. En este escenario, puede haber algunos usuarios que no entren a tu Canvas porque el horario de entrada planificado ya ha pasado en ciertas zonas horarias.

{% alert tip %}
Verás una alerta si no has planificado suficiente margen de tiempo. Una solución rápida es ajustar el horario de envío para asegurar que los usuarios puedan permanecer en el segmento objetivo durante 24 horas completas.
{% endalert %}

![Un Canvas planificado para ingresar usuarios a una hora específica comenzando a las 10 am del 30 de abril de 2025, en su hora local.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Considera usar expresiones regulares para los filtros de audiencia {#consider-using-regular-expressions-for-audience-filters}

Después de configurar los detalles preliminares de cuándo tus usuarios deben entrar a un Canvas, se recomienda revisar tus segmentos o filtros en el paso **Público objetivo** de la creación de un Canvas. En este paso, también puedes revisar el resumen de **Población objetivo** para ver cómo se ha configurado tu audiencia objetivo.

Aquí, considera usar una expresión regular para segmentos o filtros en los pasos de Rutas de audiencia, así como en la configuración de validación de entrega en los pasos de Mensaje y División de decisiones. Una [expresión regular]({{site.baseurl}}/user_guide/audience/segments/regex/) (también conocida como regex) es una cadena, lo que significa que reconoce patrones y tiene en cuenta los caracteres, en lugar de cosas como las mayúsculas. Esto significa que si estás usando "Equals / Does Not Equal", podrías estar limitando el tamaño de tu audiencia debido a simples errores de sintaxis.

Si notas que tu audiencia objetivo es más pequeña de lo esperado, intenta usar "Matches Regex" o "Does Not Match Regex" en lugar de "Equals" o "Does Not Equal". Esto puede tener en cuenta a esos usuarios faltantes y dirigirse a una audiencia más amplia.

### Identifica la configuración de entrada y las condiciones de carrera {#identify-entry-settings-and-race-conditions}

Una condición de carrera puede ocurrir cuando has usado los mismos criterios de entrada tanto en tu **Horario de entrada** como en la configuración de **Público objetivo**.

Si estás usando una entrada basada en acciones, verifica que no hayas usado la misma acción desencadenante aquí que en tu audiencia objetivo. Puede ocurrir una condición de carrera en la que el usuario no está en la audiencia en el momento en que realiza el evento desencadenante, lo que significa que no entrará al Canvas.

{% alert tip %}
Consulta las [mejores prácticas]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions/#scenario-3-matching-action-based-triggers-and-audience-filters) para evitar esta condición de carrera al configurar un Canvas basado en acciones con el mismo desencadenante que el filtro de audiencia.
{% endalert %}

### Verifica las propiedades de entrada de Canvas y las propiedades del evento {#check-canvas-entry-properties-and-event-properties}

Aunque tienen nombres similares, las [propiedades de entrada de Canvas y las propiedades del evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/) funcionan de manera diferente dentro de tus flujos de trabajo de Canvas. Las propiedades de entrada de Canvas están vinculadas a tu configuración de entrada y pueden referenciarse en cualquier componente de mensaje a lo largo de tu Canvas. Las propiedades de entrada de Canvas son propiedades del evento o la llamada a la API que desencadena la entrada de un usuario a un Canvas, usando configuraciones de entrada basadas en acciones o desencadenadas por API.

Las propiedades del evento, por otro lado, solo pueden referenciarse en el primer paso de Mensaje que sigue a un paso de Rutas de acción. Las propiedades del evento son propiedades de un evento personalizado o evento de compra que el usuario realizó durante la ventana de evaluación de un paso de Rutas de acción, y que desencadena su progresión por una de las rutas de acción definidas.

Revisa la vista previa de tu mensaje para cualquier paso de Mensaje que haga referencia a propiedades de entrada de Canvas o propiedades del evento.

### Revisa los pasos de Mensaje para el avance de usuarios {#review-message-steps-for-user-advancement}

De forma predeterminada, los usuarios avanzarán a través de todos los pasos de Mensaje independientemente de si recibieron el mensaje. Si quieres que avancen los usuarios que reciben un mensaje en particular, puedes hacerlo agregando un paso de División de decisiones directamente después de tu componente de Mensaje. Agrega el filtro "Received Message from Canvas Step" como filtro adicional, luego selecciona el Canvas y el paso de Mensaje.

Para los pasos de Mensaje con mensajes dentro de la aplicación, es posible que quieras usar un componente de Rutas de acción en lugar del componente de División de decisiones. Esto te permitirá avanzar a los usuarios según si han visto tu mensaje dentro de la aplicación. Define un grupo de acciones agregando el filtro "Interact with Step" y selecciona **View in app message**. Luego, establece la ventana de evaluación del paso en la ventana de expiración del mensaje dentro de la aplicación.

Para un componente de Mensaje en mensajería multicanal, recomendamos lo siguiente:
* Incluir un paso de Retraso entre tus pasos de Mensaje y División de decisiones, y establecer el retraso en al menos cinco segundos
* Si el componente incluye Intelligent Timing, establece el retraso en 24 horas
* Si el componente incluye límite de velocidad, divide tus mensajes en varios pasos de Mensaje de un solo canal y conéctalos entre sí. Luego, conecta el paso de División de decisiones directamente después del último paso de Mensaje para verificar si un usuario recibió alguno de los mensajes. También puedes usar este método como alternativa para un paso de Mensaje multicanal con Intelligent Timing.

## Aspectos a considerar después del lanzamiento {#things-to-consider-after-launch}

¡Has lanzado tu Canvas! Y ahora, ¿qué sigue? Usa esta lista de verificación para ver cómo puedes revisar y ajustar tu Canvas en caso de discrepancias después del lanzamiento según estos escenarios.

### Muchas entradas, pero pocos envíos {#many-entries-but-few-sends}

Por ejemplo, supongamos que has notado una disparidad entre tu número de mensajes enviados y el total de entradas. Puedes identificar y descubrir áreas para ajustar tu Canvas revisando estas áreas clave.

#### Audiencia de entrada {#entry-audience}

Si estás usando una campaña de envío planificado, verifica tu audiencia objetivo revisando tu población objetivo. ¿Cómo se ven los números a través de los canales, y cómo se relaciona eso con los canales que has usado en tu Canvas? Si los números más bajos corresponden con los canales que has usado en tu Canvas, es posible que hayas encontrado el problema.

#### Primer componente del Canvas {#first-component-of-the-canvas}

Revisa cualquier filtro de audiencia, desencadenante de acción o segmento usado en los componentes iniciales de tu Canvas. ¿Hay errores ortográficos o condiciones demasiado estrictas que impiden que tu Canvas comience correctamente? ¿Estás usando "Equals" cuando deberías estar usando "Matches Regex"?

#### Grupo de control del Canvas {#canvas-control-group}

Revisa la distribución de usuarios entre tus variantes y tu grupo de control. ¿El grupo de control es más grande de lo que pretendías? Si es así, puedes editar esta configuración. Si tienes **Intelligent Selection** activado y el grupo de control está ganando, considera detener tu Canvas e intentar un nuevo enfoque.

### Una audiencia total vacía {#an-empty-total-audience}

Si no estás viendo datos de entrada para tu Canvas, la razón por la que los usuarios pueden no estar entrando a tu Canvas puede deberse a condiciones de carrera y filtros de segmentación de audiencia restrictivos.

Si estás usando una entrada basada en acciones en tu horario de entrada, verifica que no hayas usado la misma acción desencadenante aquí que en tu **Público objetivo**. Puede ocurrir una condición de carrera en la que el usuario no está en la audiencia en el momento en que realiza el evento desencadenante, lo que significa que no entrará al Canvas.

Además, verifica que el segmento seleccionado tenga usuarios revisando la tabla de **Población objetivo** en la configuración de **Público objetivo**. Si este número es bajo, revisa cómo puedes ajustar tu configuración de entrada o revisa tus segmentos o filtros seleccionados en busca de errores.

### Caída inesperada entre pasos {#unexpected-drop-off-between-steps}

Otra forma evidente de identificar áreas de ajuste para tu Canvas puede ocurrir cuando hay una gran caída de un paso en Canvas al siguiente. En este caso, verifica que tus filtros de audiencia y eventos de excepción no tengan errores ortográficos o de mayúsculas. Y como siempre, verifica que tus filtros de audiencia no sean tan estrictos como para omitir a la mayoría de tus usuarios de la entrada al Canvas.

A continuación, es importante identificar estas configuraciones que pueden afectar cuándo y si los mensajes se envían a tus usuarios:
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/)
- [Horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/)
- Validaciones de entrega

En general, elige Intelligent Timing o [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/) para tu Canvas, no ambos. La misma sugerencia aplica para usar Intelligent Timing o [límite de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/), no ambos. Para más información sobre cómo usar mejor Intelligence Suite, lee nuestros [casos de uso de Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/#use-cases).

### Volúmenes de envío sospechosos entre rutas {#suspicious-send-volumes-between-paths}

Cuando el volumen de envíos entre dos o más rutas (ya sean Rutas de audiencia o Rutas de acción) no es lo que esperas, esta puede ser una oportunidad para revisar tus segmentos, filtros o acciones desencadenantes. Además, asegúrate de identificar y eliminar cualquier filtro superpuesto.