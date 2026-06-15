---
nav_title: Adopción de características
article_title: Adopción de características
page_order: 3
page_type: reference
description: "Este artículo describe cómo usar una plantilla de Canvas de Braze para entregar mensajes personalizados oportunos que destaquen los beneficios y consejos de uso."
tool: Canvas
---

# Adopción de características {#feature-adoption}

> Esta plantilla está diseñada para impulsar el uso de tus nuevas características, productos existentes, ofertas adicionales o cualquier otra área que quieras que tus clientes experimenten. Al aprovechar la comunicación personalizada y un conjunto estructurado de mensajes, puedes introducir fácilmente nuevas características a los usuarios y obtener comentarios valiosos de ellos.

En este artículo, te guiaremos a través de un caso de uso para la plantilla **Feature Adoption**, que está pensada para las etapas de retención y fidelización del ciclo de vida del usuario. Después de este artículo, habrás personalizado un recorrido de usuario que anima a los usuarios a usar nuevas características y recopila el sentimiento de los usuarios.

## Requisitos previos {#prerequisites}

Para usar esta plantilla con éxito, necesitarás un [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) que haga referencia a cuándo los usuarios han usado la característica.

## Adaptar la plantilla a tus necesidades {#tailoring-the-template-to-your-needs}

Supongamos que trabajas en Calorie Rocket, una aplicación de entrega de comida, que recientemente lanzó Cruise Control, una característica para programar entregas de comida recurrentes, y quieres animar a más usuarios a adoptar esta nueva característica. En nuestro ejemplo, usaremos el evento personalizado `scheduled_delivery` para rastrear cuándo los usuarios han probado la característica Cruise Control.

Para acceder a la plantilla de vuelta en stock, al crear un nuevo Canvas, selecciona **Usar una plantilla de Canvas** > **Plantillas de Braze**. Luego, junto a **Feature Adoption**, selecciona **Aplicar plantilla**. Ahora, podemos revisar la plantilla para adaptarla a nuestras necesidades.

### Paso 1: Configurar los detalles {#step-1-set-up-the-details}

Ajustemos los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Edit** junto al nombre de la plantilla.

![El título y la descripción actuales del Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %}){: style="max-width:60%;"}

{:start="2"}
2. Actualiza el nombre del Canvas para especificar que el Canvas está dirigido a usuarios para recopilar comentarios de los usuarios.
3. Actualiza la descripción para especificar que el Canvas es para animar a los usuarios a enviar comentarios y rastrear el sentimiento de los usuarios sobre la nueva característica Cruise Control.
4. Añade la etiqueta **Feature adoption** para que podamos filtrarla en la página de inicio de Canvas.

![El nuevo nombre y descripción del Canvas. La nueva descripción dice: 'Un Canvas de adopción de características para rastrear la adopción y el sentimiento de los usuarios sobre Cruise Control, una característica para programar entregas de comida recurrentes.']({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### Paso 2: Asignar un evento de conversión {#step-2-assign-a-conversion-event}

A continuación, añadamos un evento de conversión para nuestro Canvas que señale la adopción de la característica. Esto nos permitirá adaptar la ruta de experimentos en nuestro recorrido de usuario más adelante.

1. En **Assign Conversion Events**, selecciona **Add Conversion Event**.
2. En **Primary Conversion Event - A**, selecciona **Performs Custom Event** como el **Conversion event type**.
3. Selecciona nuestro evento personalizado `scheduled_delivery`.
4. Mantendremos la fecha límite de conversión en tres días.

![La ventana de evento de conversión en el Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/assign_conversion_event_cruise_control.png %}){: style="max-width:90%;"}

### Paso 3: Adaptar el horario de entrada {#step-3-tailor-the-entry-schedule}

Nuestro objetivo es animar a nuestros usuarios a adoptar Cruise Control, pero no queremos que nuestros mensajes sean demasiado frecuentes. Así que mantendremos este Canvas como una entrega planificada y haremos los siguientes ajustes en la sección **Time-Based Options**.

1. Actualiza la **Entry Frequency** a **Weekly**.
2. Mantén la recurrencia tal como está.
3. Selecciona **Mon** para dirigirte a los usuarios al comienzo de la semana.
4. Selecciona la hora de inicio para nuestro Canvas.
5. Actualiza los **Ending parameters** para terminar el Canvas el último día del año.

Mantendremos la opción de permitir que los usuarios entren al Canvas en su zona horaria local.

### Paso 4: Seleccionar la audiencia objetivo {#step-4-select-the-target-audience}

Ahora, configuremos nuestra audiencia objetivo actualizando los siguientes detalles en la plantilla:

1. Selecciona el segmento **All Users**.
2. Elimina los filtros adicionales de la plantilla.
3. Crea este filtro usando nuestro evento personalizado: `Has scheduled_delivery for exactly 0 times`. Esto nos permite excluir a los usuarios que ya han usado la característica de entrar en nuestro Canvas.

![El segmento para todos los usuarios que no han usado Cruise Control.]({% image_buster /assets/img/canvas_templates/feature_adoption/cruise_control_segment.png %}){: style="max-width:90%;"}

{: start="4"}
4. Teniendo en cuenta que Calorie Rocket previamente permitió a algunos usuarios probar en beta la nueva característica Cruise Control, actualizaremos los criterios de salida para excluir a estos usuarios de entrar en el Canvas.

### Paso 5: Seleccionar los ajustes de envío {#step-5-select-your-send-settings}

Mantendremos la configuración de suscripción predeterminada, así que solo enviaremos a usuarios que se hayan suscrito u optado por recibir mensajes o notificaciones, y omitiremos los demás ajustes (limitación de frecuencia, horas tranquilas y grupos semilla).

### Paso 6: Personalizar tu Canvas {#step-6-customize-your-canvas}

#### Construir la ruta de acción {#build-out-the-action-path}

A continuación, construyamos el primer paso de ruta de acción, que está destinado a indicar si nuestros usuarios tienen interés en la nueva característica. Haremos los siguientes ajustes a la plantilla:

1. Dado que la característica Cruise Control solo está disponible después de que se haya añadido un pedido al carrito, nombraremos el primer grupo de acción **Added to cart** y seleccionaremos `added_to_cart` para el evento personalizado.

![El nombre del grupo de acción configurado como "Added to cart" y "Perform Custom Event" configurado como "added_to_cart".]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %}){: style="max-width:60%;"}

{: start="2"}
2. Mantén el segundo grupo de acción **Taken Tour** tal como está, ya que queremos evaluar si los usuarios han realizado un recorrido por la aplicación, y si lo han hecho, avanzarán a la segunda ruta.
3. Para la ruta de acción posterior llamada **Assess Usage**, reemplaza **Used Feature >3x** con **Viewed Cruise Control settings**.
4. Selecciona el desplegable **Perform Custom Event**, luego selecciona `scheduled_delivery` para el evento personalizado.

![El nombre del grupo de acción configurado como 'Used Feature >3x' y 'Perform Custom Event' configurado como 'scheduled_delivery'.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %}){: style="max-width:60%;"}

#### Configurar el cuestionario de comentarios {#set-up-feedback-survey}

A continuación, iremos al paso de mensaje llamado **Feedback Survey** para incluir nuestro cuestionario de comentarios para que nuestros usuarios lo completen después de usar Cruise Control por primera vez. Las opciones de respuesta del cuestionario para nuestros usuarios son:

- **Loved it!**
- **Not for me.**

1. Para las dos opciones del cuestionario, selecciona **Experience Feedback** como nuestro atributo personalizado para capturar y rastrear los comentarios sobre Cruise Control. Este atributo personalizado tendrá dos valores para representar las respuestas del cuestionario (`good` y `bad`).
2. Actualiza los valores de los atributos para que coincidan con las opciones del cuestionario. Esto nos permitirá rastrear la respuesta de un usuario.

### Paso 7: Probar y lanzar tu Canvas {#step-7-test-and-launch-your-canvas}

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como se espera, selecciona **Launch Canvas** para lanzar el Canvas. Ahora, podemos dirigirnos a los usuarios con un recorrido de usuario personalizado para animarlos a adoptar nuestra nueva característica Cruise Control.

{% alert tip %}
Consulta nuestra [Lista de verificación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para conocer las cosas a considerar antes y después de lanzar un Canvas.
{% endalert %}