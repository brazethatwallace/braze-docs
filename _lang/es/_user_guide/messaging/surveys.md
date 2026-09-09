---
nav_title: Cuestionarios
article_title: Cuestionarios
page_order: 9
page_type: reference
channel:
  - landing pages
  - in-app messages
description: "Aprende cómo los cuestionarios de Braze te permiten recopilar comentarios de primera parte en páginas de inicio y mensajes dentro de la aplicación, incluyendo análisis, bloques de formulario y exportación con Currents."
---

# Cuestionarios {#surveys}

> Los cuestionarios de Braze te permiten recopilar comentarios de primera parte directamente de tus usuarios y actuar sobre ellos en mensajería de seguimiento, sin salir del panel de Braze. Usa los cuestionarios para entender el sentimiento de los usuarios, capturar preferencias y crear segmentos y desencadenantes a partir de las respuestas que recopiles.

## Disponibilidad de canales {#channel-availability}

Los cuestionarios están disponibles en dos canales. Cada página de canal cubre el flujo de creación, la composición y la ubicación de los informes específicos del canal, mientras que esta página cubre los conceptos y las capacidades que se aplican a ambos.

| Canal | Crea cuestionarios en |
| --- | --- |
| Páginas de destino | [Cuestionarios en páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) |
| In-App Messages | [Cuestionarios de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disponibilidad de canales de cuestionarios" }

## Página de cuestionarios {#surveys-page}

Ve a **Mensajería** > **Cuestionarios** para encontrar cuestionarios de páginas de destino, Campaigns y Canvas en un solo lugar. Úsala como punto de entrada para revisar el rendimiento de los cuestionarios en todos los canales.

{% alert note %}
Si no ves **Cuestionarios** en **Mensajería**, contacta a tu director de cuentas de Braze.
{% endalert %}

## Análisis {#analytics}

Cada tipo de pregunta de cuestionario incluye informes mejorados de forma predeterminada, de modo que puedes revisar los datos de respuesta de un vistazo sin necesidad de crear un segmento ni exportar a una herramienta independiente.

Los análisis de nivel superior incluyen:

- **Todas las respuestas:** Total de respuestas completas e incompletas
- **Completadas:** Usuarios que completaron todas las preguntas obligatorias
- **Parcialmente completadas:** Usuarios que enviaron algunos datos, pero no completaron todas las preguntas obligatorias
- **Impresiones únicas:** Total de visualizaciones de página

![Página de respuestas del cuestionario que muestra análisis de puntuación NPS con porcentajes de promotores, pasivos y detractores y un gráfico de barras horizontales de distribución de puntuaciones.]({% image_buster /assets/img/surveys/survey_responses.png %})

### Tipos de gráficos {#chart-types}

Para los bloques de formulario de botón de selección, menú desplegable y casilla de verificación, puedes elegir entre tres tipos de gráficos en la vista de análisis del cuestionario. Esto te da más flexibilidad para interpretar y compartir información sin necesidad de exportar a una herramienta de terceros.

| Tipo de gráfico | Ideal para |
| --- | --- |
| **Gráfico de barras** | La vista horizontal predeterminada de recuentos y porcentajes de respuestas. |
| **Gráfico de columnas** | Una vista vertical de recuentos y porcentajes de respuestas. Usa este gráfico para comparar respuestas lado a lado, especialmente para preguntas de selección múltiple o preguntas con más opciones de respuesta. |
| **Gráfico circular** | Un desglose proporcional de las respuestas. Usa este gráfico para preguntas de selección única cuando quieras ver cómo se distribuyen las respuestas entre las opciones. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de gráficos de cuestionarios" }

Cada gráfico muestra datos en tiempo real a medida que llegan las respuestas. Puedes cambiar de tipo de gráfico en cualquier momento sin afectar los datos subyacentes.

![Desglose a nivel de pregunta del cuestionario usando un gráfico de barras.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Formularios de página de destino con varios pasos {#multi-step-landing-page-forms}

Crea un cuestionario como una sola página de destino con varios pasos que se vinculan automáticamente entre sí, en lugar de crear varias páginas de destino independientes y vincularlas manualmente. Por ejemplo, puedes definir pasos separados para cada pregunta del cuestionario, además de un paso de confirmación al final.

Esta función es específica del canal de páginas de destino. Los cuestionarios de mensajes dentro de la aplicación también admiten un administrador de páginas para desplazarse entre pasos; consulta [Redactar un cuestionario de mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#compose-an-in-app-message-survey) para más detalles.

![Editor de página de destino con una vista previa de formulario con varios pasos y el panel de propiedades del formulario con una lista de pasos y un paso de confirmación bloqueado.]({% image_buster /assets/img/surveys/multi_step.png %})

## Bloques de preguntas y formularios {#question-and-form-blocks}

Las páginas de destino y los mensajes dentro de la aplicación admiten todos sus bloques de formulario estándar también en cuestionarios, incluidos grupo de botones de radio, casilla de verificación, grupo de casillas de verificación, desplegable, captura de teléfono, captura de correo electrónico y captura de texto corto. Esta sección destaca los tres bloques de formulario con reportes diseñados específicamente para cuestionarios: NPS, escala numérica y texto largo.

{% tabs local %}
{% tab NPS %}
### Bloque NPS independiente {#standalone-nps-block}

El bloque **NPS** es un bloque de formulario separado del bloque **Calificación** (escala numérica), no una opción de configuración dentro de él. Agrégalo a un cuestionario para formular la pregunta estándar de Net Promoter Score (0–10) y obtener reportes diseñados específicamente para ese caso de uso.

El bloque **NPS** te ofrece mejores reportes en el panel que una pregunta de calificación simple utilizada para el mismo propósito. En lugar de un conteo plano de respuestas por número, Braze agrupa automáticamente las respuestas en promotores (9–10), pasivos (7–8) y detractores (0–6) y muestra esos segmentos —y la puntuación NPS resultante— directamente en la vista de análisis del cuestionario.

Currents exporta la puntuación numérica (y, si se agregó, el campo de comentarios de texto libre) en el evento **Survey Response**. Los segmentos de promotores, pasivos y detractores no son campos separados de Currents.

![Un cuestionario NPS móvil junto al panel de respuestas del cuestionario, que muestra una puntuación NPS con desgloses de promotores, pasivos y detractores y un gráfico de distribución de respuestas.]({% image_buster /assets/img/surveys/survey_and_chart.png %})
{% endtab %}

{% tab Escala numérica %}
### Preguntas de escala numérica {#number-scale-questions}

También llamada escala de calificación en las páginas del canal; ambos términos se refieren al mismo bloque de formulario **Calificación**. Captura preguntas de escala numérica de 1–5, 1–10 o 0–10 para adaptarte a diferentes necesidades de cuestionarios y reportes, desde calificaciones de satisfacción simples hasta puntuaciones de probabilidad de recomendación. Para capturas de pantalla de composición específicas del canal, consulta la sección de escala de calificación en la página de [cuestionarios en páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) o [cuestionarios de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale).

Puedes recopilar una calificación como respuesta de cuestionario, registrarla como un atributo personalizado de tipo entero, o ambas opciones. Combina una pregunta de escala numérica con un bloque de [captura de texto largo](#long-form-text-capture) para recopilar una puntuación numérica junto con comentarios cualitativos en el mismo cuestionario.

![Editor de cuestionarios de página de destino con una pregunta de calificación de 1–5 seleccionada y el panel de propiedades de Calificación abierto a la derecha.]({% image_buster /assets/img/surveys/rating_block.png %})
{% endtab %}

{% tab Texto largo %}
### Captura de texto largo {#long-form-text-capture}

La captura de texto largo es útil para comentarios cualitativos. Puedes configurar el número mínimo y máximo de caracteres (hasta 1000 caracteres), si mostrar el límite de caracteres durante la composición, la altura del área de texto y el texto del marcador de posición.

![Configuración del bloque de captura de texto largo.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

{% alert important %}
Los campos de texto largo en cuestionarios de mensajes dentro de la aplicación en iOS están temporalmente limitados a 250 caracteres. Esta limitación se abordará en una futura actualización del SDK de iOS. Por ahora, considera mantener tu número máximo de caracteres en 250 o menos para cuestionarios mostrados a usuarios de iOS.
{% endalert %}

Las respuestas de texto largo están disponibles en reportes y exportaciones, pero no se pueden registrar como atributos personalizados del perfil de usuario, por lo que no puedes segmentar usuarios directamente por un valor de respuesta de texto largo. Consulta [Limitaciones]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#limitations) en cualquiera de las páginas del canal para más detalles.

En Currents, las respuestas de texto largo usan `answer_type = 'free_form_text'` con el texto en `answer_long_string`.
{% endtab %}
{% endtabs %}

## Orden aleatorio de las opciones {#randomized-choice-order}

Los bloques de grupo de botones de radio, grupo de casillas de verificación y menús desplegables admiten opciones de respuesta aleatorias. Activa **Aleatorizar orden de las opciones** para mezclar las opciones cada vez que se carga el cuestionario, lo que reduce el sesgo de orden cuando la misma primera opción podría influir en las respuestas.

La aleatorización solo cambia el orden de visualización para cada encuestado del cuestionario. Las etiquetas y los valores de los informes permanecen vinculados a las opciones que configuraste, de modo que los análisis, las exportaciones CSV y la segmentación utilizan los mismos datos de respuesta independientemente del orden en que los vio un usuario determinado.

## Plantillas de cuestionarios {#survey-templates}

Guarda un cuestionario como plantilla desde la página de destino o la biblioteca de plantillas de mensajes dentro de la aplicación para que los creadores puedan partir de ella en lugar de recrear las mismas preguntas y bloques de formulario cada vez. Cuando las plantillas de cuestionarios están habilitadas para tu espacio de trabajo, filtra la biblioteca por **Survey** para encontrar y reutilizar estructuras de cuestionarios guardadas en Campaigns, Canvas y páginas de destino.

## Eventos de respuesta de cuestionarios {#survey-response-events}

Las respuestas de los cuestionarios fluyen hacia [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para que puedas exportar los datos de los cuestionarios a tu almacén de datos o a una herramienta de BI de terceros para análisis posteriores, combinaciones con otros datos de participación e informes personalizados que van más allá de los análisis integrados del panel.

Braze exporta las respuestas individuales de los cuestionarios a Currents a través del evento **Survey Response** (`users.messages.survey.Response`). Cada evento representa la respuesta de un encuestado a una pregunta del cuestionario. Para la referencia completa de campos, consulta [Eventos de respuesta de cuestionarios]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#survey-response-events) en el glosario de eventos de Currents.

## Embudo de participación en páginas de destino {#landing-page-engagement-funnel}

Los cuestionarios en páginas de destino también generan eventos de **Impresión de página de destino** y **Clic en página de destino** para las vistas de página y los clics rastreados. Completar un cuestionario en una página de destino registra un evento de **Respuesta de cuestionario**; no desencadena también el evento genérico de **Envío de formulario de página de destino**, que es para formularios de páginas de destino estándar (no cuestionarios). Para la referencia completa de campos de estos eventos, consulta el [glosario de eventos de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

## Artículos relacionados {#related-articles}

- [Cuestionarios en páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys): Flujo de creación, composición e informes para el canal de páginas de destino
- [Cuestionarios de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys): Flujo de creación, composición e informes para el canal de In-App Messages
- [Bloques de editor de arrastrar y soltar]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks): Referencia completa de los bloques de formulario que puedes añadir a un cuestionario
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents): Configura la exportación de datos a tu almacén de datos o herramienta de BI