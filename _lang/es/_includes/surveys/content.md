{% comment %}
  Documentación compartida de cuestionarios de Braze.
  Parámetros:
  - channel (obligatorio): "in_app_message" o "landing_page"
{% endcomment %}

Para un resumen de los cuestionarios y las funcionalidades compartidas entre canales, consulta [Cuestionarios]({{site.baseurl}}/user_guide/messaging/surveys).

## Requisitos previos {#prerequisites}

Antes de crear un cuestionario, debes:

{% if include.channel == 'in_app_message' %}
- Tener acceso a los mensajes dentro de la aplicación en tu espacio de trabajo de Braze
- Estar familiarizado con la [creación de mensajes dentro de la aplicación en el editor de arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
{% elsif include.channel == 'landing_page' %}
- Tener acceso a las páginas de destino en tu espacio de trabajo de Braze
- Estar familiarizado con la [creación de páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% else %}
- Tener acceso a las páginas de destino, los mensajes dentro de la aplicación, o ambos en tu espacio de trabajo de Braze
- Estar familiarizado con la [creación de páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) y la [creación de mensajes dentro de la aplicación en el editor de arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
{% endif %}

## Crear un cuestionario {#create-a-survey}

Los cuestionarios se crean dentro de tu flujo de composición de mensajes existente.

{% if include.channel == 'in_app_message' %}
1. Crea un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) en una Campaign o Canvas.
2. Selecciona **Cuestionario** como tipo de mensaje.
{% elsif include.channel == 'landing_page' %}
1. Ve a **Mensajería** > **Páginas de destino**.
2. Crea una nueva página de destino.
3. Selecciona **Cuestionario** como tipo de mensaje.
{% else %}
1. Ve a **Mensajería** > **Páginas de destino**, o crea un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) en una Campaign o Canvas.
2. Crea un nuevo mensaje.
3. Selecciona **Cuestionario** como tipo de mensaje.
{% endif %}

{% if include.channel == 'in_app_message' %}

## Componer un cuestionario de mensaje dentro de la aplicación {#compose-an-in-app-message-survey}

Los cuestionarios de mensajes dentro de la aplicación contienen dos páginas de forma predeterminada:

- **Página 1**, donde los usuarios responden preguntas
- **Página de confirmación**, donde se envía el cuestionario

De forma predeterminada, los botones están vinculados a **Página siguiente**. Para cambiar este comportamiento, actualiza cada botón en el panel **Acciones**.

![Flujo de páginas del cuestionario de mensaje dentro de la aplicación y configuración de acciones.]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## Usa bloques de formulario de cuestionario {#use-survey-form-blocks}

Para controles compartidos de estilo y composición, consulta:

{% if include.channel == 'in_app_message' %}
- [Bloques de editor de arrastrar y soltar para mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
{% elsif include.channel == 'landing_page' %}
- [Bloques de formulario de página de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% else %}
- [Bloques de editor de arrastrar y soltar para mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [Bloques de formulario de página de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% endif %}

Puedes añadir los siguientes bloques de formulario a los cuestionarios:

- Captura de teléfono
- Captura de correo electrónico
- Grupo de botones de opción
- Captura de texto corto
- Captura de texto largo
- Desplegable
- Casilla de verificación individual
- Grupo de casillas de verificación
- Escala de valoración
- NPS

### Aleatorizar las opciones de respuesta {#randomize-answer-choices}

Los bloques de grupo de botones de opción, grupo de casillas de verificación y desplegable admiten opciones de respuesta aleatorizadas. Activa **Randomize choice order** para mezclar las opciones cada vez que se cargue el cuestionario. Para más información, consulta [Orden de opciones aleatorizado]({{site.baseurl}}/user_guide/messaging/surveys#randomized-choice-order).

### Captura de texto largo {#long-text-capture}

La captura de texto largo es útil para obtener comentarios cualitativos, con un máximo de 1000 caracteres. Para más información, consulta [Captura de texto en formato largo]({{site.baseurl}}/user_guide/messaging/surveys#long-form-text-capture).

### Escala de valoración {#rating-scale}

La escala de valoración (también llamada pregunta de escala numérica) es útil para capturar sentimiento, satisfacción o probabilidad de recomendación como un solo número. Para más información, consulta [Preguntas de escala numérica]({{site.baseurl}}/user_guide/messaging/surveys#number-scale-questions).

{% if include.channel == 'in_app_message' %}
![Escala de valoración para calificar tu experiencia en la tienda del 1 al 5.]({% image_buster /assets/img/surveys/iam_rating_scale_example.png %}){: style="max-width:40%;"}
{% elsif include.channel == 'landing_page' %}
![Escala de valoración para indicar la probabilidad de recomendar un producto a un amigo del 1 al 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% else %}
![Escala de valoración para indicar la probabilidad de recomendar un producto a un amigo del 1 al 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% endif %}

## Configura los campos y atributos obligatorios {#configure-required-fields-and-attributes}

Para cada bloque de formulario, introduce un **Identificador para informes** en el panel de configuración del lado derecho. Este identificador aparece en los informes de cuestionarios y en las exportaciones de CSV.

Ten en cuenta:

- Puedes registrar la mayoría de las respuestas de cuestionarios en atributos personalizados del perfil de usuario.
- Las respuestas de texto largo no se pueden registrar como atributos personalizados.
- Si decides no registrar una respuesta como atributo de usuario, no podrás segmentar a los usuarios por el valor de esa respuesta.

![Configuración del identificador para informes y del registro de atributos.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Ver informes y análisis {#view-reporting-and-analytics}

Después de lanzar, revisa los resultados en:

{% if include.channel == 'in_app_message' %}
- La pestaña **Responses** para cuestionarios de mensajes dentro de la aplicación
{% elsif include.channel == 'landing_page' %}
- La vista de análisis de página de destino para cuestionarios de página de destino
{% else %}
- La pestaña **Responses** para cuestionarios de mensajes dentro de la aplicación
- La vista de análisis de página de destino para cuestionarios de página de destino
{% endif %}

Para las definiciones de los análisis de nivel superior disponibles para cada cuestionario (todas las respuestas, completadas, parcialmente completadas e impresiones únicas), consulta [Análisis]({{site.baseurl}}/user_guide/messaging/surveys#analytics).

{% if include.channel == 'landing_page' %}
{% alert note %}
Los cuestionarios de página de destino rastrean las respuestas parcialmente completadas cuando el cuestionario utiliza [formularios de varios pasos]({{site.baseurl}}/user_guide/messaging/surveys#multi-step-landing-page-forms).
{% endalert %}
{% endif %}

También puedes revisar los desgloses de respuestas por pregunta, elegir entre tres tipos de gráficos y exportar los datos como CSV. Para más información, consulta [Tipos de gráficos]({{site.baseurl}}/user_guide/messaging/surveys#chart-types).

## Reorientar y desencadenar {#retarget-and-trigger}

Puedes:

- Segmentar usuarios por las respuestas del cuestionario que se registran como atributos de usuario.
- Segmentar usuarios por el estado de finalización del cuestionario.

{% if include.channel == 'in_app_message' %}

![Configuración de desencadenadores y filtros de segmentación para el seguimiento del cuestionario.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Desencadenar Campaigns y Canvas cuando un usuario completa un cuestionario en una Campaign de mensajes dentro de la aplicación.

![Configuración de desencadenadores y filtro de segmentación para el seguimiento de cuestionarios en Campaigns de mensajes dentro de la aplicación.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![Configuración de desencadenadores y filtro de segmentación para el seguimiento de cuestionarios en páginas de destino.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- Desencadenar Campaigns y Canvas cuando un usuario completa un cuestionario en una página de destino.

{% else %}

![Configuración de desencadenadores y filtros de segmentación para el seguimiento del cuestionario.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Desencadenar Campaigns y Canvas cuando un usuario completa un cuestionario en una página de destino o en una Campaign de mensajes dentro de la aplicación.

![Configuración de desencadenadores y filtro de segmentación para el seguimiento de cuestionarios en páginas de destino.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![Configuración de desencadenadores y filtro de segmentación para el seguimiento de cuestionarios en Campaigns de mensajes dentro de la aplicación.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### Limitaciones {#limitations}

Tienes las siguientes restricciones:

- No puedes segmentar usuarios por respuestas de texto largo.
- No está disponible el desencadenamiento por pregunta y respuesta que no dependa de atributos de usuario registrados.