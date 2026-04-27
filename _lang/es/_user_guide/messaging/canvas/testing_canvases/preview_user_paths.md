---
nav_title: Vista previa de recorridos de usuario
article_title: Vista previa de recorridos de usuario
page_order: 0.3
alias: /preview_user_paths/
description: "Esta página explica cómo puedes previsualizar los recorridos de usuario en Canvas."
tool:
  - Canvas
---

# Vista previa de recorridos de usuario en Canvas

> Experimenta el recorrido en Canvas que has creado para tus usuarios. Esto incluye previsualizar los tiempos y los mensajes que reciben tus usuarios. Estas ejecuciones de prueba funcionan como control de calidad para asegurar que tus mensajes se envían a la audiencia correcta, todo antes de enviar tu Canvas.

## Crear una ejecución de prueba

Sigue estos pasos para previsualizar el recorrido de tu usuario:

1. Ve al creador de Canvas. Guarda los cambios no guardados y resuelve cualquier error.
2. Selecciona **Probar Canvas** en el pie de página.
3. Selecciona un usuario de prueba.
4. (Opcional) Selecciona un destinatario para la prueba.
5. Selecciona **Ejecutar prueba**.

Puedes ejecutar una vista previa aunque no tengas permiso para editar un Canvas, pero esta vista previa se ejecuta con los cambios no guardados si los hay.

### Pasos compatibles

Los siguientes pasos son compatibles:
- Mensaje
- Ruta de audiencia
- División de decisiones
- Retraso
- Ruta de acción
- Recorrido de experimentos
- Actualización de usuario (solo en el editor de interfaz, lo que significa que los pasos que usan el editor JSON se omiten)

Si la prueba coincide con un tipo de paso que no está en la lista anterior, el paso no compatible se omite y el usuario de prueba continúa al siguiente paso compatible.

### Detalles del paso en Canvas

Para ver más detalles sobre los criterios de entrada, selecciona **Ver más**. Los pasos con segmentación muestran los criterios cumplidos o no cumplidos. Los mensajes también muestran esto para las validaciones de entrega y la elegibilidad del canal. Los pasos de mensaje muestran qué canales se enviaron y cuáles no.

### Liquid

Braze procesa la lógica de Liquid durante una ejecución de prueba, incluso si no estás enviando un mensaje de prueba real. Esto significa que la [lógica de cancelación de mensajes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/#abort-messages) y otra lógica de Liquid se reflejan y podrían afectar el recorrido del usuario en Canvas.

Si tu vista previa envía el último paso del recorrido de tu usuario en lugar de cancelar, es posible que la vista previa esté usando la hora actual como la hora evaluada para Liquid, no la hora real en la que el usuario estaría en el paso según la hora de entrada al Canvas.

## Vistas previas de tiempos

Para Canvas planificados, el usuario de prueba entra en el siguiente horario de entrada planificado. Para Canvas basados en acciones con fechas de inicio, el usuario de prueba entra en la fecha y hora de inicio.

Aunque los horarios de inicio predeterminados siguen aplicándose, la hora de entrada es configurable en todos los casos, lo que significa que puedes simular una fecha en el pasado o en el futuro. Sin embargo, no puedes probar antes de la fecha de inicio ni después de la fecha de finalización del Canvas.

Los pasos de mensaje y retraso muestran la hora a la que un usuario avanzaría o recibiría el mensaje sin necesidad de reconfigurar los retrasos. Ten en cuenta que, aunque los pasos indican si se usa Intelligent Timing, esta vista previa del recorrido del usuario no calcula una estimación para un usuario de prueba.

Para Canvas con un desencadenador de acción como "cambio en el valor de un atributo personalizado", Braze intenta simular el cambio estableciendo temporalmente el atributo del usuario en el desencadenador como vacío **solo para la ejecución de prueba del Canvas** (esto no afecta al perfil de usuario). Esto está pensado para probar que el atributo cambia desde su valor actual.

## Cuándo los usuarios entran y salen

Los usuarios de prueba entran en la vista previa incluso si no son elegibles en la vida real. Si no son elegibles, puedes ver por qué no han cumplido los criterios. Cuando un usuario de prueba entra en la vista previa, asumimos que ha cumplido los criterios de audiencia objetivo y ha realizado los criterios del desencadenador de acción. Por ejemplo, para un Canvas que usa eventos personalizados en los criterios de entrada, se asume que el usuario de prueba ha realizado el evento personalizado como se esperaba en los criterios de entrada. Sin embargo, si el mismo evento personalizado se usa en otra parte del Canvas (como en los criterios de salida), considera cómo esto podría afectar el recorrido de tu usuario.

Los eventos, desencadenadores de API, atributos personalizados y propiedades de entrada de Canvas que se asumen para permitir que un usuario de prueba entre al Canvas no se actualizan en el perfil de usuario real y no persisten más allá de la ejecución de prueba. Por ejemplo, durante las pruebas, cuando un atributo personalizado se usa como desencadenador de Canvas, los criterios del desencadenador se aplican a la vista previa del usuario **como si** hubiera desencadenado el cambio de atributo personalizado.

### Consideración

Si pruebas una ruta de acción con acciones que corresponden a criterios de salida (incluidas las propiedades del evento), los criterios de salida se activan y la ejecución de prueba finaliza. Si pruebas un paso de mensaje que corresponde a criterios de salida, los criterios de salida se activan y la ejecución de prueba finaliza.

En este momento, no puedes seleccionar un evento o propiedad específica dentro de una ruta de acción para activar los criterios de salida (solo la ruta en su conjunto). Si un usuario pudiera cumplir potencialmente múltiples criterios de salida, se muestra como resultado el primero que se procesa y que cumple.

## Recorridos de experimentos y variantes en Canvas

- Para Canvas con variantes de nivel superior, selecciona una variante al inicio de la prueba.
- Para recorridos de experimentos, selecciona la variante por la que avanza el usuario cuando el usuario de prueba encuentra el paso.
- Para recorridos de experimentos que usan recorrido personalizado o variante ganadora, aunque hay un período de retraso durante el cual el usuario de prueba espera en un paso de mensaje, este retraso no se tiene en cuenta ya que Braze asume que el usuario avanzó por la variante seleccionada inmediatamente.

## Envíos de prueba

Puedes optar por enviar mensajes de prueba a un grupo de prueba interno o a un usuario individual a medida que se completa la ejecución de prueba. Esto significa que solo se envían los mensajes que el usuario encuentra a lo largo del recorrido de prueba. Los destinatarios reciben mensajes con sus atributos de forma predeterminada, pero puedes anularlos con los atributos del usuario de prueba.

Para enviar todos los mensajes de prueba en un Canvas a la vez, independientemente del recorrido, y sin previsualizar el recorrido, puedes seleccionar **Enviar todos los mensajes de prueba** en la pestaña **Envíos de prueba**.

## Capacidad de respuesta

Los pasos en Canvas responden a los tiempos al previsualizar los recorridos de usuario. Las actualizaciones realizadas a través del paso de Actualización de usuario se reflejan en los pasos posteriores del flujo, pero no se aplican al perfil de usuario real. Los efectos de que un usuario entre en una variante se reflejan en los pasos futuros de una vista previa.

De manera similar, los filtros reconocen las acciones que ocurrieron como resultado de la interacción del usuario de prueba con otros pasos en el Canvas. Por ejemplo, este modo de vista previa reconoce que un usuario encontró un paso de mensaje que fue "enviado" anteriormente en el Canvas, y reconoce que el usuario de prueba "realizó una acción" para avanzar a través de una ruta de acción.

Consulta [Criterios de salida]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria/) para más detalles sobre el comportamiento de respuesta.

## Contenido conectado

El Contenido conectado se ejecuta si está incluido en el Canvas. Esto significa que si pruebas un Canvas que tiene llamadas de Contenido conectado o Bloques de contenido que contienen Contenido conectado, el Canvas puede enviar las llamadas de Contenido conectado, lo que modificaría los datos referenciados en otras campañas o Canvas.

Al previsualizar los recorridos de usuario, considera eliminar el Contenido conectado que altera los perfiles de usuario o los datos referenciados en otros Canvas o campañas.

## Webhooks

Los webhooks se ejecutan cuando se envían mensajes de prueba, pero no durante la ejecución de prueba. De manera similar al Contenido conectado, considera eliminar los webhooks que alteran los perfiles de usuario o los datos referenciados en otros Canvas o campañas.

## Variables de contexto y grupos semilla

Para un paso de mensaje con correo electrónico como canal de mensajería, los grupos semilla envían copias semilla de los correos electrónicos cuando un usuario llega a este paso en el Canvas. Estas copias semilla no se envían como parte de los recorridos propios en Canvas de los destinatarios del grupo semilla, por lo que Braze no ejecuta [pasos de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) ni evalúa las variables de contexto para esos destinatarios. Si el contenido de tu correo electrónico hace referencia a variables de contexto, los destinatarios del grupo semilla reciben una copia semilla sin esos datos completados. Para probar mensajes que dependen de datos de variables de contexto, usa la vista previa de **Probar Canvas** con envíos de prueba en lugar de grupos semilla.

## Caso de uso

En este escenario, el Canvas está configurado para dirigirse a usuarios que no han tenido una sesión en una aplicación. Este recorrido incluye un paso de mensaje con un correo electrónico de bienvenida, un paso de retraso configurado para un día y un paso de rutas de audiencia que se divide en dos recorridos: usuarios con al menos una sesión y el resto. Dependiendo de la ruta de audiencia en la que caiga un usuario, se envía el paso de mensaje correspondiente.

![Un ejemplo de un Canvas con un paso de mensaje, un paso de retraso, un paso de rutas de audiencia y dos pasos de mensaje.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Dado que nuestro usuario de prueba cumple los criterios de entrada del Canvas, puede entrar al Canvas y recorrer el recorrido del usuario. Sin embargo, como nuestro usuario de prueba no ha abierto la aplicación en el último día calendario, continúa por el recorrido "El resto" y recibe una notificación push que dice: "¡Última oportunidad! Completa tu primera tarea para obtener un bono exclusivo."

![La sección "Resultados de la prueba" muestra que el usuario de prueba ha cumplido los criterios de entrada y proporciona un resumen de su recorrido, incluyendo qué pasos se le enviaron.]({% image_buster /assets/img/preview_user_path_results_example.png %})