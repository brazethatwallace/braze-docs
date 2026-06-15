{% comment %}
  Documentación compartida de cuestionarios de Braze.
  Parámetros:
  - channel (obligatorio): "in_app_message" o "landing_page"
{% endcomment %}

{% multi_lang_include early_access_beta_alert.md feature='Braze surveys' %}

## Requisitos previos {#prerequisites}

Antes de crear un cuestionario, debes:

{% if include.channel == 'in_app_message' %}
- Tener acceso a los mensajes dentro de la aplicación en tu espacio de trabajo de Braze
- Estar familiarizado con la [creación de mensajes dentro de la aplicación en el editor de arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
{% elsif include.channel == 'landing_page' %}
- Tener acceso a las páginas de inicio en tu espacio de trabajo de Braze
- Estar familiarizado con la [creación de páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/)
{% else %}
- Tener acceso a las páginas de inicio, los mensajes dentro de la aplicación, o ambos en tu espacio de trabajo de Braze
- Estar familiarizado con la [creación de páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/) y la [creación de mensajes dentro de la aplicación en el editor de arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
{% endif %}

## Crear un cuestionario {#create-a-survey}

Durante el acceso anticipado, los cuestionarios se crean dentro de tu flujo de composición de mensajes existente.

{% if include.channel == 'in_app_message' %}
1. Crea un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) en una Campaign o Canvas.
2. Selecciona **Survey** como tu tipo de mensaje.
{% elsif include.channel == 'landing_page' %}
1. Ve a **Mensajería** > **Páginas de inicio**.
2. Crea una nueva página de inicio.
3. Selecciona **Survey** como tu tipo de mensaje.
{% else %}
1. Ve a **Mensajería** > **Páginas de inicio**, o crea un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) en una Campaign o Canvas.
2. Crea un nuevo mensaje.
3. Selecciona **Survey** como tu tipo de mensaje.
{% endif %}

{% if include.channel == 'in_app_message' %}

## Redactar un cuestionario de mensaje dentro de la aplicación {#compose-an-in-app-message-survey}

Los cuestionarios de mensajes dentro de la aplicación contienen dos páginas de forma predeterminada:

- **Página 1**, donde los usuarios responden preguntas
- **Página de confirmación**, donde se envía el cuestionario

De forma predeterminada, los botones están vinculados a **Next page**. Para cambiar este comportamiento, actualiza cada botón en el panel de **Acciones**.

![Flujo de páginas del cuestionario de mensaje dentro de la aplicación y configuración de acciones.]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## Usar bloques de formulario de cuestionario {#use-survey-form-blocks}

Para controles compartidos de estilo y composición, consulta:

{% if include.channel == 'in_app_message' %}
- [Bloques del editor de arrastrar y soltar de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
{% elsif include.channel == 'landing_page' %}
- [Bloques de formulario de páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#form-blocks)
{% else %}
- [Bloques del editor de arrastrar y soltar de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [Bloques de formulario de páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#form-blocks)
{% endif %}

Puedes añadir los siguientes bloques de formulario a los cuestionarios:

- Captura de teléfono
- Captura de correo electrónico
- Grupo de botones de opción
- Captura de texto corto
- Captura de texto largo
- Desplegable
- Casilla de verificación única
- Grupo de casillas de verificación

### Captura de texto largo {#long-text-capture}

La captura de texto largo es útil para obtener comentarios cualitativos.

Puedes configurar:

- Recuentos mínimos y máximos de caracteres (hasta 1000)
- Si se muestran los límites de caracteres durante la composición
- Altura del área de texto (filas)
- Texto del marcador de posición

Durante el acceso anticipado, las respuestas de texto largo están disponibles en los informes y las exportaciones, pero no se pueden registrar como atributos personalizados del perfil de usuario.

![Configuración del bloque de captura de texto largo.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## Configurar campos obligatorios y atributos {#configure-required-fields-and-attributes}

Para cada bloque de formulario, introduce un **Identificador para informes** en el panel de configuración del lado derecho. Este identificador aparece en los informes de cuestionarios y en las exportaciones CSV.

Durante el acceso anticipado:

- Puedes registrar la mayoría de las respuestas de cuestionarios como atributos personalizados del perfil de usuario.
- Las respuestas de texto largo no se pueden registrar como atributos personalizados.
- Si decides no registrar una respuesta como atributo de usuario, no podrás segmentar usuarios por ese valor de respuesta.

![Configuración del identificador para informes y registro de atributos.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Ver informes y análisis {#view-reporting-and-analytics}

Después del lanzamiento, revisa los resultados en:

{% if include.channel == 'in_app_message' %}
- La pestaña **Responses** para cuestionarios de mensajes dentro de la aplicación
{% elsif include.channel == 'landing_page' %}
- La vista de análisis de la página de inicio para cuestionarios de páginas de inicio
{% else %}
- La pestaña **Responses** para cuestionarios de mensajes dentro de la aplicación
- La vista de análisis de la página de inicio para cuestionarios de páginas de inicio
{% endif %}

![Pestaña de análisis de la página de inicio.]({% image_buster /assets/img/surveys/survey-analytics-1.png %})

Los análisis de nivel superior incluyen:

- **Todas las respuestas:** Total de respuestas completas e incompletas
- **Completadas:** Usuarios que completaron todas las preguntas obligatorias
- **Parcialmente completadas:** Usuarios que enviaron algunos datos, pero no completaron todas las preguntas obligatorias
- **Impresiones únicas:** Total de vistas de página

{% if include.channel == 'landing_page' %}
{% alert note %}
Los cuestionarios de páginas de inicio no rastrean las respuestas parcialmente completadas durante el acceso anticipado.
{% endalert %}
{% endif %}

También puedes revisar los desgloses de respuestas por pregunta y exportar los datos como CSV.

### Elegir un tipo de gráfico {#choose-a-chart-type}

Para los bloques de formulario de botones de opción, desplegables y casillas de verificación, puedes elegir entre tres tipos de gráficos en la vista de análisis de cuestionarios. Esto te da más flexibilidad para interpretar y compartir información sin necesidad de exportar a una herramienta de terceros.

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

![Configuración de desencadenadores y filtros de segmentación para seguimiento de cuestionarios.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Desencadenar Campaigns y Canvas cuando un usuario completa un cuestionario en una Campaign de mensaje dentro de la aplicación.

![Configuración de desencadenadores y filtros de segmentación para seguimiento de cuestionarios de Campaigns de mensajes dentro de la aplicación.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![Configuración de desencadenadores y filtros de segmentación para seguimiento de cuestionarios de páginas de inicio.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- Desencadenar Campaigns y Canvas cuando un usuario completa un cuestionario en una página de inicio.

{% else %}

![Configuración de desencadenadores y filtros de segmentación para seguimiento de cuestionarios.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Desencadenar Campaigns y Canvas cuando un usuario completa un cuestionario en una página de inicio o en una Campaign de mensaje dentro de la aplicación.

![Configuración de desencadenadores y filtros de segmentación para seguimiento de cuestionarios de páginas de inicio.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![Configuración de desencadenadores y filtros de segmentación para seguimiento de cuestionarios de Campaigns de mensajes dentro de la aplicación.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### Limitaciones {#limitations}

Durante el acceso anticipado, tienes las siguientes restricciones:

- No puedes segmentar usuarios por respuestas de texto largo.
- La activación por pregunta y respuesta que no dependa de atributos de usuario registrados no está disponible.