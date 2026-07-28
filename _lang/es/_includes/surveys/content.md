{% comment %}
  Documentación compartida de cuestionarios de Braze.
  Parámetros:
  - channel (obligatorio): "in_app_message" o "landing_page"
{% endcomment %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='Braze surveys' %}

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

Durante el acceso anticipado, los cuestionarios se crean dentro de tu flujo de composición de mensajes existente.

{% if include.channel == 'in_app_message' %}
1. Crea un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) en una Campaign o Canvas.
2. Selecciona **Survey** como tu tipo de mensaje.
{% elsif include.channel == 'landing_page' %}
1. Ve a **Mensajería** > **Landing Pages**.
2. Crea una nueva landing page.
3. Selecciona **Survey** como tu tipo de mensaje.
{% else %}
1. Ve a **Mensajería** > **Landing Pages**, o crea un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) en una Campaign o Canvas.
2. Crea un nuevo mensaje.
3. Selecciona **Survey** como tu tipo de mensaje.
{% endif %}

{% if include.channel == 'in_app_message' %}

## Componer un cuestionario de mensaje dentro de la aplicación {#compose-an-in-app-message-survey}

Los cuestionarios de mensajes dentro de la aplicación contienen dos páginas de forma predeterminada:

- **Página 1**, donde los usuarios responden preguntas
- **Página de confirmación**, donde se envía el cuestionario

De forma predeterminada, los botones están vinculados a **Next page**. Para cambiar este comportamiento, actualiza cada botón en el panel **Actions**.

![Flujo de páginas del cuestionario de mensaje dentro de la aplicación y configuración de acciones.]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## Usar bloques de formulario de cuestionario {#use-survey-form-blocks}

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

### Aleatorizar opciones de respuesta {#randomize-answer-choices}

Los bloques de grupo de botones de opción, grupo de casillas de verificación y desplegable admiten opciones de respuesta aleatorizadas. Activa **Aleatorizar orden de opciones** para mezclar las opciones cada vez que se cargue el cuestionario. Usa esta configuración para reducir el sesgo de orden cuando la misma primera opción podría distorsionar las respuestas.

La aleatorización solo cambia el orden de visualización para cada encuestado. Las etiquetas y los valores de los informes permanecen asignados a las opciones que configuraste, por lo que los análisis, las exportaciones CSV y la segmentación utilizan los mismos datos de respuesta.

### Captura de texto largo {#long-text-capture}

La captura de texto largo es útil para obtener comentarios cualitativos.

Puedes configurar:

- Recuentos mínimo y máximo de caracteres (hasta 1000)
- Si se muestran los límites de caracteres durante la composición
- Altura del área de texto (filas)
- Texto del marcador de posición

Durante el acceso anticipado, las respuestas de texto largo están disponibles en informes y exportaciones, pero no se pueden registrar como atributos personalizados del perfil de usuario.

![Configuración del bloque de captura de texto largo.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

### Escala de valoración {#rating-scale}

La escala de valoración es útil para capturar sentimiento, satisfacción o probabilidad de recomendación como un solo número.

En el panel de configuración, selecciona una escala del desplegable:

- **1–10**
- **1–5**
- **0–10** (rango estándar de NPS)

Puedes recopilar una valoración como respuesta del cuestionario, registrarla como un atributo personalizado de tipo entero, o ambas cosas. Combina un bloque de escala de valoración con un bloque de [captura de texto largo](#long-text-capture) para recopilar una puntuación numérica junto con comentarios cualitativos en el mismo cuestionario.

{% if include.channel == 'in_app_message' %}
![Escala de valoración para calificar tu experiencia en la tienda del 1 al 5.]({% image_buster /assets/img/surveys/iam_rating_scale_example.png %}){: style="max-width:40%;"}
{% elsif include.channel == 'landing_page' %}
![Escala de valoración para indicar la probabilidad de recomendar un producto a un amigo del 1 al 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% else %}
![Escala de valoración para indicar la probabilidad de recomendar un producto a un amigo del 1 al 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% endif %}

## Configura los campos y atributos obligatorios {#configure-required-fields-and-attributes}

Para cada bloque de formulario, introduce un **Identificador para informes** en el panel de configuración del lado derecho. Este identificador aparece en los informes de cuestionarios y en las exportaciones CSV.

Durante el acceso anticipado:

- Puedes registrar la mayoría de las respuestas de cuestionarios en atributos personalizados del perfil de usuario.
- Las respuestas de texto largo no se pueden registrar como atributos personalizados.
- Si decides no registrar una respuesta como atributo de usuario, no podrás segmentar usuarios por ese valor de respuesta.

![Configuración del identificador para informes y del registro de atributos.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Ver informes y análisis {#view-reporting-and-analytics}

Después del lanzamiento, revisa los resultados en:

{% if include.channel == 'in_app_message' %}
- La pestaña **Responses** para cuestionarios de mensajes dentro de la aplicación
{% elsif include.channel == 'landing_page' %}
- La vista de análisis de la página de destino para cuestionarios de páginas de destino
{% else %}
- La pestaña **Responses** para cuestionarios de mensajes dentro de la aplicación
- La vista de análisis de la página de destino para cuestionarios de páginas de destino
{% endif %}

Los análisis de nivel superior incluyen:

- **All responses:** Total de respuestas completas e incompletas
- **Completed:** Usuarios que completaron todas las preguntas obligatorias
- **Partially complete:** Usuarios que enviaron algunos datos, pero no completaron todas las preguntas obligatorias
- **Unique impressions:** Total de vistas de página

{% if include.channel == 'landing_page' %}
{% alert note %}
Los cuestionarios de páginas de destino no rastrean las respuestas parcialmente completadas durante el acceso anticipado.
{% endalert %}
{% endif %}

También puedes revisar los desgloses de respuestas por pregunta y exportar los datos como CSV.

### Elegir un tipo de gráfico {#choose-a-chart-type}

Para los bloques de formulario de botón de opción, menú desplegable y casilla de verificación, puedes elegir entre tres tipos de gráficos en la vista de análisis del cuestionario. Esto te da más flexibilidad para interpretar y compartir información sin necesidad de exportar a una herramienta de terceros.

| Tipo de gráfico | Ideal para |
| --- | --- |
| Gráfico de barras | La vista horizontal predeterminada de recuentos y porcentajes de respuestas. |
| Gráfico de columnas | Una vista vertical de recuentos y porcentajes de respuestas. Usa este gráfico para comparar respuestas lado a lado, especialmente para preguntas de selección múltiple o preguntas con más opciones de respuesta. |
| Gráfico circular | Un desglose proporcional de las respuestas. Usa este gráfico para preguntas de selección única cuando quieras ver cómo se distribuyen las respuestas entre las opciones. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de gráficos de cuestionarios" }

Cada gráfico se actualiza en tiempo real a medida que llegan las respuestas. Puedes cambiar de tipo de gráfico en cualquier momento sin afectar los datos subyacentes.

![Desglose a nivel de pregunta del cuestionario usando un gráfico de barras.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Reorientar y desencadenar {#retarget-and-trigger}

Durante el acceso anticipado, puedes:

- Segmentar usuarios por respuestas de cuestionarios que se registran como atributos de usuario.
- Segmentar usuarios por estado de finalización del cuestionario.

{% if include.channel == 'in_app_message' %}

![Configuración de desencadenadores y filtros de segmentación para el seguimiento de cuestionarios.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Desencadenar Campaigns y Canvas cuando un usuario completa un cuestionario en una Campaign de mensaje dentro de la aplicación.

![Configuración de desencadenadores y filtro de segmentación para el seguimiento de cuestionarios de Campaigns de mensajes dentro de la aplicación.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![Configuración de desencadenadores y filtro de segmentación para el seguimiento de cuestionarios de páginas de destino.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- Desencadenar Campaigns y Canvas cuando un usuario completa un cuestionario en una página de destino.

{% else %}

![Configuración de desencadenadores y filtros de segmentación para el seguimiento de cuestionarios.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Desencadenar Campaigns y Canvas cuando un usuario completa un cuestionario en una página de destino o en una Campaign de mensaje dentro de la aplicación.

![Configuración de desencadenadores y filtro de segmentación para el seguimiento de cuestionarios de páginas de destino.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![Configuración de desencadenadores y filtro de segmentación para el seguimiento de cuestionarios de Campaigns de mensajes dentro de la aplicación.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### Limitaciones {#limitations}

Durante el acceso anticipado, tienes las siguientes restricciones:

- No puedes segmentar usuarios por respuestas de texto largo.
- No está disponible el desencadenamiento por pregunta y respuesta que no dependa de atributos de usuario registrados.