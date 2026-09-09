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

Antes de lanzar un Canvas, hay varios detalles que puedes revisar para asegurarte de que tus mensajes y horarios de envío se alineen con las preferencias de tu audiencia. Los aspectos a considerar incluyen variaciones en las zonas horarias, la configuración de entrada y más. Utiliza esta lista de comprobación como guía para ajustar estas áreas según tu caso de uso y contribuir al éxito de tu Canvas.

### Revisar la configuración de zona horaria {#review-time-zone-settings}

Si estás ingresando usuarios según su zona horaria local mediante un calendario de entrada programado, deberías lanzar tu Canvas al menos 24 horas antes de cuando quieras que los usuarios entren a tu Canvas. Por ejemplo, aquí hay un Canvas que no dejó suficiente tiempo entre el lanzamiento y la hora de entrada programada. En este escenario, puede haber algunos usuarios que no entren a tu Canvas porque la hora de entrada programada ya pasó en ciertas zonas horarias.

{% alert tip %}
Verás una alerta si no has programado suficiente margen. Una solución rápida es ajustar la hora de envío para asegurar que los usuarios puedan permanecer en el segmento objetivo durante 24 horas completas.
{% endalert %}

![Un Canvas programado para ingresar usuarios a una hora, comenzando a las 10 am del 30 de abril de 2025, en su zona horaria local.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Considerar el uso de expresiones regulares para los filtros de audiencia {#consider-using-regular-expressions-for-audience-filters}

Después de configurar los detalles preliminares de cuándo tus usuarios deben entrar a un Canvas, se recomienda revisar tus segmentos o filtros en el paso **Público objetivo** de la creación de un Canvas. En este paso, también puedes revisar el resumen de **Población objetivo** para ver cómo se ha configurado tu público objetivo.

Aquí, considera usar una expresión regular para segmentos o filtros en los pasos de Rutas de Audiencia, la configuración de validación de entrega en los pasos de Mensaje y de división de decisiones. Una [expresión regular]({{site.baseurl}}/user_guide/audience/segments/regex) (también conocida como regex) es una cadena, lo que significa que reconoce patrones y tiene en cuenta los caracteres, en lugar de cosas como las mayúsculas. Esto significa que si estás usando "Es igual / No es igual", podrías estar limitando el tamaño de tu audiencia por simples errores de sintaxis.

Si notas que tu público objetivo es más pequeño de lo esperado, intenta usar "Coincide con Regex" o "No coincide con Regex" en lugar de "Es igual" o "No es igual". Esto puede incluir a esos usuarios faltantes y alcanzar a una audiencia más amplia.

### Identificar la configuración de entrada y las condiciones de carrera {#identify-entry-settings-and-race-conditions}

Una condición de carrera puede ocurrir cuando has utilizado los mismos criterios de entrada tanto en tu **Calendario de entrada** como en la configuración del **Público objetivo**.

Si estás usando una entrada basada en acciones, verifica que no hayas utilizado la misma acción desencadenante aquí que en tu público objetivo. Puede ocurrir una condición de carrera en la que el usuario no esté en la audiencia en el momento en que realiza el evento desencadenante, lo que significa que no entrará al Canvas.

{% alert tip %}
Consulta las [mejores prácticas]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#scenario-3-matching-action-based-triggers-and-audience-filters) para evitar esta condición de carrera al configurar un Canvas basado en acciones con el mismo desencadenante que el filtro de audiencia.
{% endalert %}

### Revisar las propiedades de entrada de Canvas y las propiedades del evento {#check-canvas-entry-properties-and-event-properties}

Aunque tienen nombres similares, las [propiedades de entrada de Canvas y las propiedades del evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) funcionan de manera diferente dentro de tus flujos de trabajo de Canvas. Las propiedades de entrada de Canvas están vinculadas a tu configuración de entrada y pueden referenciarse en cualquier componente de mensaje a lo largo de tu Canvas. Las propiedades de entrada de Canvas son propiedades del evento o la llamada a la API que desencadena la entrada de un usuario a un Canvas, usando configuraciones de entrada basadas en acciones o activadas por API.

Las propiedades del evento, por otro lado, solo pueden referenciarse en el primer paso de Mensaje que sigue a un paso de Rutas de Acción. Las propiedades del evento son propiedades de un evento personalizado o evento de compra que el usuario realizó durante la ventana de evaluación de un paso de Rutas de Acción, y que desencadena su avance por una de las rutas de acción definidas.

Revisa la vista previa de tu mensaje para cualquier paso de Mensaje que haga referencia a propiedades de entrada de Canvas o propiedades del evento.

### Revisar los pasos de Mensaje para el avance de usuarios {#review-message-steps-for-user-advancement}

De forma predeterminada, los usuarios avanzarán a través de todos los pasos de Mensaje independientemente de si recibieron el mensaje. Si quieres que avancen los usuarios que reciben un mensaje en particular, puedes hacerlo añadiendo un paso de división de decisiones directamente después de tu componente de Mensaje. Añade el filtro "Mensaje recibido del paso de Canvas" como filtro adicional, luego selecciona el Canvas y el paso de Mensaje.

Para los pasos de Mensaje con mensajes dentro de la aplicación, es posible que quieras usar un componente de Rutas de Acción en lugar del componente de división de decisiones. Esto te permitirá hacer avanzar a los usuarios según si han visto tu mensaje dentro de la aplicación. Define un grupo de acciones añadiendo el filtro "Interactuar con el paso" y selecciona **Ver mensaje dentro de la aplicación**. Luego, configura la ventana de evaluación del paso con la ventana de expiración del mensaje dentro de la aplicación.

Para un componente de Mensaje en mensajería multicanal, recomendamos lo siguiente:
* Incluir un paso de Retraso entre tus pasos de Mensaje y de división de decisiones, y configurar el retraso en al menos cinco segundos
* Si el componente incluye sincronización inteligente, configura el retraso en 24 horas
* Si el componente incluye límite de velocidad, divide tus mensajes en varios pasos de Mensaje de un solo canal y conéctalos entre sí. Luego, conecta el paso de división de decisiones directamente después del último paso de Mensaje para verificar si un usuario recibió alguno de los mensajes. También puedes usar este método como alternativa para un paso de Mensaje multicanal con sincronización inteligente.

## Aspectos a tener en cuenta después del lanzamiento {#things-to-consider-after-launch}

¡Has lanzado tu Canvas! Y ahora, ¿qué? Usa esta lista de comprobación para ver cómo puedes revisar y ajustar tu Canvas en caso de discrepancias después del lanzamiento según estos escenarios.

### Muchas entradas, pero pocos envíos {#many-entries-but-few-sends}

Por ejemplo, supongamos que has notado una disparidad entre el número de mensajes enviados y el total de entradas. Puedes identificar y descubrir áreas para ajustar tu Canvas comprobando estas áreas clave.

#### Público de entrada {#entry-audience}

Si estás utilizando una Campaign de envío programado, vuelve a comprobar tu público objetivo revisando tu población objetivo. ¿Cómo se ven los números en todos los canales y cómo se relacionan con los canales que has utilizado en tu Canvas? Si los números más bajos corresponden a los canales que has utilizado en tu Canvas, es posible que hayas encontrado el problema.

#### Primer componente del Canvas {#first-component-of-the-canvas}

Revisa cualquier filtro de audiencia, acción desencadenante o Segments utilizados en los componentes iniciales de tu Canvas. ¿Hay errores ortográficos o condiciones demasiado estrictas que impiden que tu Canvas arranque correctamente? ¿Estás usando "Equals" cuando deberías usar "Matches Regex"?

#### Grupo de control del Canvas {#canvas-control-group}

Revisa la distribución de usuarios entre tus variantes y tu grupo de control. ¿El grupo de control es más grande de lo que pretendías? Si es así, puedes editar esta configuración. Si **Optimize with BrazeAI<sup>TM</sup>** está activado y el grupo de control está ganando, considera detener tu Canvas e intentar un nuevo enfoque.

### Un público total vacío {#an-empty-total-audience}

Si no estás viendo ningún dato de entrada para tu Canvas, la razón por la que los usuarios pueden no estar entrando en tu Canvas puede deberse a condiciones de carrera y filtros de segmentación de audiencia restrictivos.

Si estás utilizando la entrada basada en acciones en tu programación de entrada, comprueba que no hayas utilizado la misma acción desencadenante aquí que en tu **público objetivo**. Puede ocurrir una condición de carrera en la que el usuario no esté en la audiencia en el momento en que realiza el evento desencadenante, lo que significa que no entrará en el Canvas.

Además, comprueba que el Segment seleccionado tenga usuarios revisando la tabla de **población objetivo** en la configuración del **público objetivo**. Si este número es bajo, revisa cómo puedes ajustar la configuración de entrada o revisa los Segments o filtros seleccionados en busca de errores.

### Caída inesperada entre pasos {#unexpected-drop-off-between-steps}

Otra forma evidente de identificar áreas de ajuste para tu Canvas puede ocurrir cuando hay una gran caída de un paso en Canvas al siguiente. En este caso, comprueba que tus filtros de audiencia y eventos de excepción no tengan errores ortográficos o de capitalización. Y como siempre, comprueba que tus filtros de audiencia no sean tan estrictos como para omitir a la mayoría de tus usuarios de la entrada al Canvas.

A continuación, es importante identificar estas configuraciones que pueden afectar cuándo y si los mensajes se envían a tus usuarios:
- [Sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)
- [Horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)
- Validaciones de entrega

En general, elige la sincronización inteligente o las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) para tu Canvas, no ambas. La misma sugerencia aplica para usar la sincronización inteligente o el [límite de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping), no ambos. Para más información sobre cómo aprovechar mejor la suite de inteligencia, lee nuestros [ejemplos de la suite de inteligencia]({{site.baseurl}}/user_guide/brazeai/intelligence_suite#use-cases).

### Volúmenes de envío sospechosos entre rutas {#suspicious-send-volumes-between-paths}

Cuando el volumen de envíos entre dos o más rutas (ya sean rutas de audiencia o Rutas de Acción) no es el que esperas, esta puede ser una oportunidad para comprobar tus Segments, filtros o acciones desencadenantes. Además, asegúrate de identificar y eliminar cualquier filtro superpuesto.