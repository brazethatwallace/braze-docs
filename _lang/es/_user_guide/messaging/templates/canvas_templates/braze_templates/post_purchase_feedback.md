---
nav_title: Comentarios posteriores a la compra
article_title: Comentarios posteriores a la compra
page_order: 6
page_type: reference
description: "Este artículo describe cómo utilizar una plantilla de BRAZE CANVAS para orquestar experiencias personalizadas que te permitan responder a los comentarios y construir una relación con tus usuarios."
tool: Canvas
---

# Comentarios posteriores a la compra {#post-purchase-feedback}

> Utiliza la plantilla de comentarios posteriores a la compra para obtener información crítica sobre cómo tus clientes interactúan con tu marca y asegurarte de que sigan teniendo experiencias positivas. Aprovechando la comunicación personalizada y un conjunto estructurado de mensajes, puedes seguir construyendo y fomentando las relaciones con tus clientes.

Este artículo te guiará a través de un caso de uso de la plantilla **Post-Purchase Feedback**, que está diseñada para la etapa de conversión del ciclo de vida del usuario. Cuando termines, habrás creado un Canvas que anima a los usuarios a proporcionar comentarios sobre tu aplicación.

## Requisitos previos {#prerequisites}

Para utilizar esta plantilla con éxito, necesitarás lo siguiente:

- Un [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes) como referencia para los resultados del cuestionario de comentarios.
- Una [sincronización de audiencia de Braze]({{site.baseurl}}/partners/canvas_audience_sync) configurada con los socios y audiencias que utilizas.

## Adaptar la plantilla a tus necesidades {#tailoring-the-template-to-your-needs}

Supongamos que trabajamos para Decorumsoft, un desarrollador de videojuegos para móviles. Utilizaremos la plantilla de comentarios posteriores a la compra para medir los comentarios sobre el lanzamiento de nuestro último videojuego, Proxy War 3: War of Thirst. Usando estos comentarios, informaremos nuestros planes de desarrollo para el paquete de expansión, Liquid Mirage.

Antes de crear el Canvas, configuramos la integración de [sincronización de audiencia de Braze con Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) para poder añadir datos de usuario de Braze a Google Audiences y enviar anuncios basados en desencadenantes de comportamiento, segmentación y más.

Para acceder a la plantilla de comentarios posteriores a la compra, al crear un nuevo Canvas, selecciona **Use a Canvas template** > **Braze templates**. Luego, junto a **Post-Purchase Feedback**, selecciona **Apply Template**. Ahora podemos recorrer la plantilla para adaptarla a nuestras necesidades.

### Paso 1: Configurar los detalles del Canvas {#step-1-set-up-canvas-details}

Ajustemos los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Edit** junto al nombre de la plantilla.

![El título y la descripción actuales del Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %}){: style="max-width:50%;"}

{:start="2"}
2. Actualiza el nombre del Canvas para especificar que está dirigido a usuarios recientes.
3. Actualiza la descripción para especificar que el Canvas es para animar a los usuarios a enviar comentarios.
4. Añade la etiqueta **Feedback** para filtrarlo en la página de inicio de Canvas.

![El nuevo nombre y descripción del Canvas. La nueva descripción dice: "Un Canvas de comentarios posteriores a la compra para medir el interés en la próxima expansión de PWD3, Liquid Mirage."]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %}){: style="max-width:50%;"}

### Paso 2: Asignar eventos de conversión {#step-2-assign-conversion-events}

A continuación, asignemos nuestros eventos de conversión. Actualiza el **conversión primaria Event - A** a **Make a specific purchase** y selecciona **Proxy War**.

![Sección "Assign Conversion Events" para el tipo de evento de conversión de compra del producto del juego Proxy War.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_conversion_event.png %}){: style="max-width:90%;"}

Mantendremos la fecha límite de conversión de tres días de la plantilla porque queremos dirigirnos a nuestros usuarios más recientes.

### Paso 3: Establecer un horario de entrada {#step-3-set-an-entry-schedule}

1. Mantén el tipo de horario de entrada como **Action-Based**.
2. Establece la **Start Time** de la ventana de entrada en la fecha de lanzamiento del juego.

### Paso 4: Determinar quién entra en el Canvas {#step-4-determine-who-enters-the-canvas}

Nuestra audiencia objetivo para los comentarios son los usuarios que han comprado recientemente Proxy War 3.

1. Selecciona nuestro segmento objetivo, "Purchased Proxy War 3", que consiste en usuarios que han comprado el juego.
2. Selecciona un filtro para incluir usuarios que han comprado "Proxy War 3" más de "0" veces.

![Un segmento llamado "Purchased Proxy War 3" que segmenta a los usuarios que han comprado el juego.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/entry_window_segment.png %}){: style="max-width:90%;"}

{: start="3"}
3. Actualiza los controles de entrada para no permitir que los usuarios vuelvan a entrar en el Canvas después de la duración máxima del Canvas.

### Paso 5: Seleccionar los ajustes de envío {#step-5-select-your-send-settings}

Mantendremos la configuración de suscripción predeterminada, de modo que solo enviemos a usuarios que se hayan suscrito u optado por recibir mensajes o notificaciones.

Dado que queremos ser cuidadosos con nuestros envíos, seleccionaremos **Enable Quiet Hours** para evitar solicitar comentarios entre las 11 pm y las 10 am en la zona horaria de nuestros usuarios y solo enviar en el siguiente horario disponible.

![Paso "Send Settings" dirigido a usuarios que están suscritos u optados. Las horas tranquilas están activadas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/send_settings_with_quiet_hours.png %}){: style="max-width:90%;"}

Para nuestro ejemplo, omitiremos las demás configuraciones (limitación de frecuencia y grupos semilla).

### Paso 6: Personalizar tu Canvas {#step-6-customize-your-canvas}

A continuación, construiremos nuestro Canvas personalizando los canales de mensajería y el contenido que se enviará a los usuarios. Dado que solo buscamos comentarios usando canales de correo electrónico, mensajes dentro de la aplicación y webhook, recorreremos la plantilla y eliminaremos las variantes de SMS de los pasos de mensaje.

Comenzaremos nuestra personalización recorriendo cada componente de mensajería para actualizar el contenido. Nuestro atributo personalizado de referencia es `Experience Feedback`.

1. En el constructor de Canvas, selecciona el primer paso de mensaje en el recorrido del usuario.
2. Selecciona la variante de **Email**.
3. Completa la **Sending info** con un asunto que anime a los usuarios a dar comentarios.
4. Selecciona **Edit message** para reemplazar el mensaje de correo electrónico de la plantilla con nuestro mensaje de cuestionario de comentarios. Esto incluye reemplazar los enlaces de cada llamada a la acción para capturar qué opción se selecciona, lo cual se referenciará en el paso de ruta de acción de nuestro recorrido del usuario.

{% alert tip %}
Puedes usar las [propiedades de entrada de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) para personalizar los mensajes en tu Canvas según el producto al que te refieras.
{% endalert %}

#### Configurar el cuestionario de comentarios {#set-up-feedback-survey}

A continuación, necesitaremos completar los detalles de la variante de **In-App Message**. Aquí es donde debemos especificar nuestro atributo personalizado `Experience Feedback` que indica el sentimiento de los comentarios de nuestros usuarios. (También lo referenciaremos en el paso de ruta de acción posterior.)

1. En el mismo primer paso de mensaje, selecciona la variante de **In-App Messages**. Mantendremos los controles del mensaje tal como están.
2. Para el encabezado y el cuerpo, usaremos un lenguaje que anime a los usuarios a ser honestos sobre su experiencia con Proxy War 3.
3. Dado que queremos que las respuestas del cuestionario se registren en sus perfiles, mantendremos el cuestionario como **Single-choice selection** y **Log attributes upon submission**.
4. Para cada una de las tres opciones del cuestionario, selecciona **Experience Feedback** como nuestro atributo personalizado.
5. Mantendremos los valores de atributo en el perfil de usuario tal como están, ya que estos valores se alinean con nuestro atributo personalizado.

![Un cuestionario que pregunta al usuario si disfrutó su compra reciente de Proxy War 3 con tres opciones: "Loved it", "It was OK" y "Not for me".]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/survey_example_iam.png %}){: style="max-width:90%;"}

#### Construir la ruta de acción {#build-out-the-action-path}

Usando nuestro atributo personalizado `Experience Feedback` y los valores de atributo de la sección anterior, actualizaremos la ruta de acción de la plantilla para que coincida con nuestro atributo y valores.

![El grupo "Good feedback" para el paso de ruta de acción que incluye a los usuarios que respondieron "Loved it" a nuestro cuestionario.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/action_path_good_example.png %}){: style="max-width:90%;"}

### Configurar la reorientación de anuncios {#set-up-ad-retargeting}

Nos aseguraremos de que nuestra sincronización de Google Audience esté configurada en nuestro paso de **Ad Retargeting**. Esto incluirá seleccionar nuestra cuenta de anuncios, una audiencia existente y la opción de añadir usuarios a la audiencia.

### Configurar casos de soporte con webhook {#set-up-webhook-support-cases}

A continuación, configuremos el webhook para desencadenar posibles casos de soporte. Esto puede ser especialmente útil en combinación con el análisis de los comentarios de nuestros usuarios.

Para el paso de mensaje llamado **Support Case Creation**, actualizaremos la plantilla para componer un webhook para los usuarios que no están satisfechos con su compra y quieren un reembolso.

![Un webhook que crea casos de soporte para clientes que tienen un sentimiento negativo y quieren un reembolso por su compra de Proxy War 3.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/webhook_example.png %}){: style="max-width:90%;"}

### Paso 7: Probar y lanzar el Canvas {#step-6-test-and-launch-the-canvas}

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como se espera, selecciona **Launch Canvas** para lanzar el Canvas. ¡Ahora podemos dirigirnos de manera cuidadosa a los usuarios con un recorrido de usuario personalizado para animarlos a responder a nuestro cuestionario de comentarios basado en su compra reciente de Proxy War 3!

{% alert tip %}
Consulta nuestra [lista de verificación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) para conocer las cosas a considerar antes y después de lanzar un Canvas.
{% endalert %}