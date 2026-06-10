---
nav_title: Cuestionarios
article_title: Cuestionarios de Braze
description: "Aprende a crear cuestionarios en mensajes dentro de la aplicación y páginas de inicio, revisar respuestas y reorientar usuarios durante la beta cerrada."
permalink: /braze_surveys/
hidden: true
---

# Cuestionarios de Braze {#braze-surveys}

> Los cuestionarios de Braze recopilan comentarios en mensajes dentro de la aplicación y páginas de inicio que puedes analizar y utilizar en mensajes de seguimiento.

{% alert important %}
Los cuestionarios de Braze están en beta cerrada. Envía tus comentarios sobre la beta a [surveys-feedback@braze.com](mailto:surveys-feedback@braze.com).
{% endalert %}

## Requisitos previos {#prerequisites}

Antes de crear un cuestionario, debes:

- Tener acceso a páginas de inicio, mensajes dentro de la aplicación, o ambos en tu espacio de trabajo de Braze
- Estar familiarizado con la [creación de páginas de inicio](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/)
- Estar familiarizado con la [creación de mensajes dentro de la aplicación de arrastrar y soltar](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/)

## Crear un cuestionario {#create-a-survey}

Durante la beta, los cuestionarios se crean dentro de tu flujo de composición de mensajes existente.

1. Ve a **Mensajería** > **Páginas de inicio**, o crea un [mensaje dentro de la aplicación](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/) en una Campaign o Canvas.
2. Crea un nuevo mensaje.
3. Selecciona **Survey** como tu tipo de mensaje.

## Redactar un cuestionario de mensaje dentro de la aplicación {#compose-an-in-app-message-survey}

Los cuestionarios de mensajes dentro de la aplicación contienen dos páginas de forma predeterminada:

- **Página 1**, donde los usuarios responden preguntas
- **Página de confirmación**, donde se envía el cuestionario

De forma predeterminada, los botones están vinculados a **Página siguiente**. Para cambiar este comportamiento, actualiza cada botón en el panel de **Acciones**.

![Flujo de páginas del cuestionario de mensaje dentro de la aplicación y configuración de acciones.]({% image_buster /assets/unlisted_docs/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

## Usar bloques de formulario de cuestionario {#use-survey-form-blocks}

Para controles de estilo y composición compartidos, consulta:

- [Bloques del editor de arrastrar y soltar de mensajes dentro de la aplicación](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/)
- [Bloques de formulario de páginas de inicio](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks)

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

La captura de texto largo es útil para comentarios cualitativos.

Puedes configurar:

- Recuentos mínimo y máximo de caracteres (hasta 1000)
- Si mostrar los límites de caracteres durante la composición
- Altura del área de texto (filas)
- Texto del marcador de posición

Durante la beta, las respuestas de texto largo están disponibles en informes y exportaciones, pero no se pueden registrar como atributos personalizados del perfil de usuario.

![Configuración del bloque de captura de texto largo.]({% image_buster /assets/unlisted_docs/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## Configurar campos obligatorios y atributos {#configure-required-fields-and-attributes}

Para cada bloque de formulario, introduce un **Identificador para informes** en el panel de configuración del lado derecho. Este identificador aparece en los informes de cuestionarios y las exportaciones CSV.

Durante la beta:

- Puedes registrar la mayoría de las respuestas de cuestionarios como atributos personalizados del perfil de usuario.
- Las respuestas de texto largo no se pueden registrar como atributos personalizados.
- Si decides no registrar una respuesta como atributo de usuario, no podrás segmentar usuarios por ese valor de respuesta.

![Configuración del identificador para informes y registro de atributos.]({% image_buster /assets/unlisted_docs/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Ver informes y análisis {#view-reporting-and-analytics}

Después del lanzamiento, revisa los resultados en:

- La pestaña **Respuestas** para cuestionarios de mensajes dentro de la aplicación
- La vista de análisis de páginas de inicio para cuestionarios de páginas de inicio

![Pestaña de análisis de páginas de inicio.]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-1.png %})

Los análisis de nivel superior incluyen:

- **Todas las respuestas:** total de respuestas completas e incompletas
- **Completadas:** usuarios que completaron todas las preguntas obligatorias
- **Parcialmente completadas:** usuarios que enviaron algunos datos, pero no completaron todas las preguntas obligatorias
- **Impresiones únicas:** total de vistas de página

{% alert note %}
Los cuestionarios de páginas de inicio no rastrean respuestas parcialmente completadas durante la beta.
{% endalert %}

También puedes revisar desgloses de respuestas por pregunta y exportar datos como CSV.

![Resumen de análisis del cuestionario y desglose a nivel de pregunta.]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-text.png %})

![Gráficos de barras del desglose a nivel de pregunta del cuestionario.]({% image_buster /assets/unlisted_docs/img/surveys/bar-charts-1.png %})

## Reorientar y desencadenar {#retarget-and-trigger}

Durante la beta, puedes:

- Segmentar usuarios por respuestas de cuestionarios que se registran como atributos de usuario.
- Segmentar usuarios por estado de finalización del cuestionario. <br><br>![Configuración de desencadenadores y filtros de segmentación para seguimiento de cuestionarios.]({% image_buster /assets/unlisted_docs/img/surveys/submit-survey-segment.png %})<br><br>
- Desencadenar Campaigns y Canvas cuando un usuario completa un cuestionario en una página de inicio o en una Campaign de mensaje dentro de la aplicación. <br><br>![Configuración de desencadenadores y filtro de segmentación para seguimiento de cuestionarios de páginas de inicio.]({% image_buster /assets/unlisted_docs/img/surveys/trigger_landing_page_survey.png %}) <br><br>![Configuración de desencadenadores y filtro de segmentación para seguimiento de cuestionarios de Campaigns de mensajes dentro de la aplicación.]({% image_buster /assets/unlisted_docs/img/surveys/interact-campaign-step.png %})

### Limitaciones {#limitations}

Durante la beta, tienes las siguientes restricciones:

- No puedes segmentar usuarios por respuestas de texto largo.
- El desencadenamiento por pregunta y respuesta que no depende de atributos de usuario registrados no está disponible.