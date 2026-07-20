---
nav_title: Editar Canvas después del lanzamiento
article_title: Editar Canvas después del lanzamiento
page_order: 0
description: "Este artículo de referencia cubre los diferentes aspectos de un Canvas que se pueden cambiar después del lanzamiento inicial."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Editar Canvas después del lanzamiento {#edit-canvases-after-launch}

> Este artículo de referencia cubre lo que se puede cambiar en un Canvas después del lanzamiento inicial.

Puedes editar tus Canvas después del lanzamiento de las siguientes maneras:

* Insertando nuevos pasos en Canvas en el recorrido del usuario
* Añadiendo nuevas variantes y conexiones
* Ajustando la distribución de variantes
* Deteniendo o reanudando todos los pasos en Canvas

{% alert note %}
La distribución de la variante de control solo puede disminuirse después del lanzamiento.
{% endalert %}

Puedes eliminar cualquiera de los siguientes elementos en tu recorrido del usuario:

- [Pasos en Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about)
- Variantes en Canvas
- Conexiones entre pasos en Canvas

Si deseas editar o añadir más pasos al recorrido del usuario en tu Canvas, se aplican los siguientes detalles:

- Los usuarios que aún no han entrado en el Canvas son elegibles para cualquier paso recién creado.
- Si la configuración de entrada de tu Canvas permite a los usuarios volver a entrar en los pasos, los usuarios que ya han pasado por los pasos recién creados son elegibles para volver a entrar.
- Los usuarios que actualmente están en un Canvas lanzado, pero no han alcanzado los puntos del recorrido del usuario donde se añadieron nuevos pasos, son elegibles para recibir esos pasos recién añadidos.

Si eliminas un paso de [Retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) o de [Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), puedes opcionalmente redirigir a los usuarios que actualmente están esperando en el paso hacia otro paso en Canvas. Para los retrasos, los usuarios permanecen en el paso hasta el final del período de retraso. Para las Rutas de Acción, los usuarios permanecen en el paso hasta el final de la ventana de evaluación.

Ten en cuenta que cuando lanzas un Canvas inicialmente, Braze pone en cola a los usuarios para el paso de mensaje en el que se encuentran, no todos los mensajes posteriores en el Canvas. Si realizas una edición en el Canvas después del lanzamiento, es posible que algunos usuarios ya estén en cola y no reciban los cambios. Si detienes el Canvas, lo duplicas, luego lo cambias y lanzas esta nueva versión, el Canvas vuelve a evaluar a todos los usuarios de nuevo, no solo a los usuarios que aún no han sido puestos en cola.

Consulta la sección de [Mejores prácticas](#best-practices) para casos de uso específicos de edición. En general, es una buena práctica evitar editar Canvas en vivo, ya que puede haber comportamientos inesperados.

{% details Expandir para ver detalles del editor de Canvas original %}

Ten en cuenta las siguientes ediciones permitidas después del lanzamiento de Canvas, dependiendo del flujo de trabajo con el que se creó tu Canvas. Si tu Canvas utiliza el flujo de trabajo original de Canvas, necesitarás clonarlo a Canvas Flow primero para realizar ediciones después del lanzamiento.

No puedes editar ni eliminar conexiones existentes, y no puedes insertar un paso entre pasos ya conectados. Si deseas editar o añadir más pasos al recorrido del usuario en tu Canvas, se aplican los siguientes detalles:

- Los usuarios que aún no han entrado en el Canvas son elegibles para cualquier paso recién creado.
- Si la configuración de entrada de tu Canvas permite a los usuarios volver a entrar en los pasos, los usuarios que ya han pasado por los pasos recién creados son elegibles para volver a entrar.
- Los usuarios que actualmente están en un Canvas lanzado, pero no han alcanzado los pasos recién añadidos en el recorrido del usuario, son elegibles para recibir esos pasos recién añadidos.
- Si un paso de retraso es el último paso en el Canvas, los usuarios que llegan a ese paso avanzan automáticamente fuera del Canvas y no recibirán ningún paso recién creado.

{% alert important %}
Si actualizas la configuración de **Retraso** o **Ventana** para un paso en Canvas, los usuarios que actualmente están en ese paso en el momento de la actualización se rigen por el tiempo de retraso que se les asignó cuando entraron originalmente. Solo los nuevos usuarios que entran en el Canvas y aquellos que aún no han sido puestos en cola para ese paso reciben el mensaje en el tiempo actualizado.
{% endalert %}

Detener un Canvas no hace salir a los usuarios que están esperando recibir un mensaje. Si vuelves a habilitar el Canvas y los usuarios aún están esperando el mensaje, lo reciben (a menos que el momento en que debería haberse enviado el mensaje ya haya pasado, en cuyo caso no lo reciben).

{% enddetails %}

## Detalles de Canvas {#canvas-details}

Puedes editar la siguiente configuración y detalles después de lanzar un Canvas:

* Nombre y descripción del Canvas
* Equipos y etiquetas
* Tipo de entrada, horario y controles
* Estado de suscripción
* Límite de velocidad
* Limitación de frecuencia
* Horas tranquilas
* Público objetivo

Después de que un Canvas ha sido lanzado:

- Los eventos de conversión no se pueden editar.
- Los siguientes pasos no se pueden añadir ni eliminar, y no se pueden reordenar para ajustar la clasificación: [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), [Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) y [Recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step).
  - **Solución alternativa 1:** Crea una nueva ruta de audiencia, Ruta de Acción o recorrido de experimentos y reconfigura las rutas hacia ese nuevo paso.
  - **Solución alternativa 2:** Duplica el Canvas para hacer tus ediciones.

### Pasos individuales {#individual-steps}

Para pasos individuales en Canvas, puedes editar los siguientes detalles después del lanzamiento:

* Nombre
* Contenido del mensaje
* Desencadenantes
* Audiencia
* Eventos de excepción
* Retrasos (solo para pasos de retraso)

Sin embargo, el tipo de planificación del paso y los porcentajes de control no son editables después del lanzamiento. Para los pasos de Rutas de Acción y rutas de audiencia, las clasificaciones y las ventanas de evaluación no son editables después del lanzamiento.

#### Paso Enviar a destino {#send-to-destination-step}

Al editar el paso [Enviar a destino]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) en un Canvas en vivo, se aplican los siguientes comportamientos:

- **Cambiar el Canvas de destino:** Editar el paso Enviar a destino para apuntar a un Canvas de destino diferente sigue las mismas reglas generales de edición después del lanzamiento. Los cambios solo afectan a los usuarios que aún no han alcanzado el paso Enviar a destino.
  - Los usuarios que ya pasaron por el paso permanecen en el Canvas de destino original; no se redirigen.
  - Los usuarios actualmente en cola en pasos anteriores (por ejemplo, esperando en un paso de retraso antes del paso Enviar a destino) se evalúan según los criterios de entrada y audiencia del nuevo Canvas de destino cuando alcanzan el paso. Los usuarios elegibles se envían al nuevo Canvas de destino.
- **Canvas de destino detenido:** Si el Canvas de destino se detiene mientras tu Canvas de origen sigue activo, los usuarios que alcanzan el paso Enviar a destino no se envían al Canvas de destino. Esto causa una pérdida de usuarios en la transferencia, no una pausa mientras el destino está detenido.
  - Los usuarios que no pueden entrar en el Canvas de destino detenido continúan en el Canvas de origen si hay más pasos después del paso Enviar a destino. Para más información sobre el comportamiento de avance, consulta [Enviar a destino]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination#how-does-advancement-behavior-work-for-send-to-destination-steps).
  - No puedes lanzar un Canvas de origen con un paso Enviar a destino que apunte a un destino detenido. Este comportamiento se aplica cuando un Canvas de destino se detiene después de que el Canvas de origen ya está en vivo.

### Porcentajes de variantes en Canvas {#canvas-variant-percentages}

Después de lanzar un Canvas, solo puedes disminuir los porcentajes de la variante de control. Si se modifica un porcentaje de variante en Canvas, encontrarás que tus usuarios pueden ser redistribuidos a otras variantes.

Inicialmente, estos usuarios se asignan aleatoriamente a una variante particular antes de recibir una campaña por primera vez. A partir de entonces, cada vez sucesiva que se recibe la campaña (o el usuario vuelve a entrar en una variante en Canvas), reciben la misma variante a menos que se modifiquen los porcentajes de variante.

Si los porcentajes de variante cambian, los usuarios pueden ser redistribuidos a otras variantes. Los usuarios permanecen en estas variantes hasta que los porcentajes se modifiquen de nuevo. Ten en cuenta que para Canvas que utilizan ramificación con filtros `NOT` con números de contenedor aleatorio, es posible que los usuarios no reciban la misma rama cada vez en su recorrido del usuario cuando vuelven a entrar en el Canvas.

#### Grupos de control {#control-groups}

Los grupos de control permanecen consistentes si el porcentaje de variante no cambia. Si el porcentaje de un grupo de control se disminuye o aumenta, los usuarios que previamente recibieron mensajes no podrían entrar en el grupo de control en un envío posterior, ni ningún usuario en el grupo de control recibiría jamás un mensaje.

### Hora de envío local {#local-send-time}

Los Canvas programados para lanzarse a una hora de envío local pueden editarse hasta 24 horas antes de la hora de envío programada. Esta ventana se llama la "zona segura".

{% alert tip %}
Si tienes la intención de hacer ediciones más grandes que lleven a crear una copia completamente nueva del Canvas, recuerda excluir a los usuarios que recibieron el primer Canvas y reajustar los horarios de planificación del Canvas para permitir el envío por zona horaria.
{% endalert %}

Cuando un horario de entrada está configurado para que los usuarios entren inmediatamente al lanzar, el Canvas se lanza a la hora más cercana en incrementos de 5 minutos. Por ejemplo, si actualizas un Canvas para que los usuarios entren inmediatamente a las 8:31 am PST, la hora de lanzamiento se establece a las 8:30 am PST y en la zona horaria de la empresa.

### Eliminar variantes {#deleting-variants}

Cuando se eliminan variantes de un Canvas, ocurre lo siguiente:

- Los pasos dentro de la variante (incluidos los compartidos por otras variantes) se eliminan.
- Los análisis del paso y los análisis de nivel superior del Canvas, como *Entradas totales*, *Salidas totales* y *Tasa de conversión*, se eliminan.
- Los usuarios en variantes eliminadas salen de los pasos, y cualquier mensaje posterior no se envía.

### Propiedades de entrada de Canvas {#canvas-entry-properties}

Las propiedades de entrada de Canvas no se aplican como plantilla en los pasos cuando se envían. Esto significa que cuando las propiedades de entrada de Canvas se editan después de que un Canvas ha sido lanzado, estos cambios solo se aplican a los nuevos usuarios que entran en el Canvas. Si tu Canvas permite a los usuarios volver a entrar en el Canvas, cualquier usuario que vuelva a entrar se determina por las propiedades de entrada de Canvas actualizadas.

## Mejores prácticas {#best-practices}

Consulta estas mejores prácticas a tener en cuenta al editar o añadir elementos a tu Canvas después de que ha sido lanzado.

{% alert important %}
En general, evita hacer cambios mientras el Canvas está activo y poniendo usuarios en cola.
{% endalert %}

### Pasos desconectados {#disconnected-steps}

Puedes lanzar tu Canvas con pasos desconectados y también guardar estos Canvas después del lanzamiento. Antes de desconectar un paso de tu flujo de trabajo, te recomendamos verificar la vista de análisis de los pasos para usuarios pendientes.

Supongamos que un usuario está en un paso desconectado de tu flujo de trabajo de Canvas. Este usuario avanza al paso posterior si hay uno. La configuración del paso determina cómo debe avanzar el usuario.

Al crear o editar pasos desconectados, puedes hacer cambios en estos pasos independientes sin tener que conectarlos directamente al resto de tu Canvas. Esto ayuda a probar tus pasos antes de lanzar tu Canvas de nuevo.

### Paso de recorrido de experimentos {#experiment-path-step}

Si tu Canvas tiene un experimento de ruta ganadora o ruta personalizada activo o en progreso y actualizas el Canvas activo (independientemente de si actualizas el paso de recorrido de experimentos en sí), el experimento en progreso finaliza y el paso de recorridos de experimentos no determina una ruta ganadora ni rutas personalizadas. Para reiniciar el experimento, puedes desconectar el recorrido de experimentos existente y lanzar uno nuevo, o duplicar el Canvas y lanzar un nuevo Canvas. De lo contrario, los usuarios fluyen a través del recorrido de experimentos como si no se hubiera seleccionado ningún método de optimización.

### Retrasos de tiempo {#time-delays}

Editar Canvas con retrasos de tiempo puede ser un poco complicado, así que ten en cuenta los siguientes detalles mientras realizas ediciones en tus Canvas:

- Si actualizas el retraso en un paso de retraso, solo los nuevos usuarios que entran en el Canvas y los usuarios que no han sido puestos en cola para ese paso reciben el mensaje con el retraso de tiempo actualizado.
- Si eliminas un paso con un retraso de tiempo (como retraso o Rutas de Acción) y decides redirigir a esos usuarios a otro paso en Canvas, los usuarios solo son redirigidos después de que el retraso de tiempo del paso se haya completado. Por ejemplo, supongamos que eliminas un paso de retraso con un retraso de un día y rediriges a esos usuarios a un paso de mensaje. En este caso, los usuarios solo son redirigidos después de que el retraso de un día se haya completado.
- Si tu Canvas tiene uno o más pasos de recorridos de experimentos, eliminar pasos podría invalidar los resultados de este paso.

### Detener Canvas {#stopping-canvases}

Detener un Canvas no hace salir a los usuarios que están esperando en un paso. Si vuelves a habilitar el Canvas y los usuarios aún están esperando, completan el paso y avanzan al siguiente paso. Sin embargo, si el momento en que el usuario debería haber avanzado al siguiente paso ya ha pasado, en su lugar sale del Canvas.

Por ejemplo, supongamos que tienes un Canvas creado usando el flujo de trabajo de Canvas Flow configurado para lanzarse a las 2 pm con una variante con dos pasos: un paso de retraso con un retraso de una hora que lleva a un paso de mensaje.

Un usuario entra en este Canvas a las 2:01 pm y entra en el paso de retraso al mismo tiempo. Esto significa que el usuario está programado para avanzar al siguiente paso del recorrido del usuario (el paso de mensaje) a las 3:01 pm. Si detienes el Canvas a las 2:30 pm y vuelves a habilitar el Canvas a las 3:30 pm, el usuario sale del Canvas ya que es después de las 3:01 pm. Sin embargo, si vuelves a habilitar el Canvas a las 2:40 pm, el usuario avanza al paso de mensaje como se esperaba a las 3:01 pm.

## Cosas que debes saber {#things-to-know}

Los siguientes problemas comunes pueden desencadenarse al editar o añadir más componentes a cualquier otro componente en un Canvas después del lanzamiento.

{% alert important %}
Los siguientes problemas son evitables. Si necesitas hacer ediciones a un Canvas después de que ha sido lanzado, te recomendamos primero confirmar que todos los usuarios que ya han entrado en el Canvas hayan completado su recorrido del usuario. Además, sugerimos que no elimines pasos que ya hayan sido procesados por al menos un usuario.
{% endalert %}

- Datos de informes faltantes (cuando las variantes de mensaje se eliminan y se vuelven a añadir)
- Los usuarios no siguen la ruta esperada
- Los mensajes se envían en momentos inesperados
- Las ediciones no sobrescriben los datos de Currents, por lo que puedes notar discrepancias entre los pasos en Canvas (como `canvas_step_ids` que no existen en el Canvas debido a la eliminación)
- Los usuarios pueden recibir el mismo mensaje dos veces
- Los usuarios no recibirán mensajes debido al límite de velocidad existente
  - Cuando actualizas el límite de velocidad en un Canvas activo, el nuevo límite de velocidad se aplica solo a los usuarios que pasan por el paso de mensaje después del cambio de límite de velocidad. Los usuarios que ya están en cola para un paso de mensaje conservan el límite de velocidad original que estaba vigente cuando fueron puestos en cola. Para aplicar un nuevo límite de velocidad a todos los usuarios, detén el Canvas, duplícalo con el límite de velocidad actualizado y lanza el nuevo Canvas. Usa un filtro para evitar que los usuarios que recibieron mensajes del Canvas original entren en el duplicado.
- Cuando un Canvas se [detiene automáticamente]({{site.baseurl}}/user_guide/messaging/governance/statuses#available-statuses), los borradores posteriores al lanzamiento del Canvas también se eliminan.