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

Los cuestionarios están disponibles en dos canales. Cada página de canal cubre el flujo de creación, la composición y la ubicación de los informes específicos del canal, mientras que esta página cubre los conceptos y las funcionalidades que aplican a ambos.

| Canal | Crea cuestionarios en |
| --- | --- |
| Páginas de inicio | [Cuestionarios en páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) |
| Mensajes dentro de la aplicación | [Cuestionarios de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disponibilidad de canales de cuestionarios" }

## Página de cuestionarios {#surveys-page}

Ve a **Mensajería** > **Cuestionarios** para encontrar cuestionarios en páginas de inicio, Campaigns y Canvas en un solo lugar. Úsalo como tu punto de entrada para revisar el rendimiento de cuestionarios en todos los canales.

{% alert note %}
Si no ves **Cuestionarios** en **Mensajería**, contacta a tu director de cuentas de Braze.
{% endalert %}

## Análisis {#analytics}

Cada tipo de pregunta de cuestionario incluye informes mejorados de forma predeterminada, para que puedas revisar los datos de respuestas de un vistazo sin necesidad de crear un segmento o exportar a una herramienta separada primero.

Los análisis de nivel superior incluyen:

- **Todas las respuestas:** total de respuestas completas e incompletas
- **Completadas:** usuarios que completaron todas las preguntas obligatorias
- **Parcialmente completas:** usuarios que enviaron algunos datos, pero no completaron todas las preguntas obligatorias
- **Impresiones únicas:** total de vistas de página

![Página de respuestas de cuestionarios que muestra análisis de puntuación NPS con porcentajes de promotores, pasivos y detractores, y un gráfico de barras horizontal de distribución de puntuaciones.]({% image_buster /assets/img/surveys/survey_responses.png %})

### Tipos de gráficos {#chart-types}

Para los bloques de formulario de botón de opción, menú desplegable y casilla de verificación, puedes elegir entre tres tipos de gráficos en la vista de análisis de cuestionarios. Esto te da más flexibilidad para interpretar y compartir información sin exportar a una herramienta de terceros.

| Tipo de gráfico | Ideal para |
| --- | --- |
| **Gráfico de barras** | La vista horizontal predeterminada de conteos y porcentajes de respuestas. |
| **Gráfico de columnas** | Una vista vertical de conteos y porcentajes de respuestas. Usa este gráfico para comparar respuestas lado a lado, especialmente para preguntas de selección múltiple o preguntas con más opciones de respuesta. |
| **Gráfico circular** | Un desglose proporcional de las respuestas. Usa este gráfico para preguntas de selección única cuando quieras ver cómo se distribuyen las respuestas entre las opciones. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de gráficos de cuestionarios" }

Cada gráfico muestra datos en tiempo real a medida que llegan las respuestas. Puedes cambiar de tipo de gráfico en cualquier momento sin afectar los datos subyacentes.

![Desglose a nivel de pregunta del cuestionario utilizando un gráfico de barras.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Formularios de páginas de inicio con múltiples pasos {#multi-step-landing-page-forms}

Crea un cuestionario como una sola página de inicio con múltiples pasos que se vinculan automáticamente entre sí, en lugar de crear múltiples páginas de inicio independientes y vincularlas manualmente. Por ejemplo, puedes definir pasos separados para cada pregunta del cuestionario, más un paso de confirmación al final.

Esta funcionalidad es específica del canal de páginas de inicio. Los cuestionarios de mensajes dentro de la aplicación también admiten un administrador de páginas para moverse entre pasos; consulta [Componer un cuestionario de mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#compose-an-in-app-message-survey) para más detalles.

![Editor de página de inicio con una vista previa de formulario de múltiples pasos y el panel de propiedades del formulario que lista los pasos y un paso de confirmación bloqueado.]({% image_buster /assets/img/surveys/multi_step.png %})

## Bloques de preguntas y formularios {#question-and-form-blocks}

Las páginas de inicio y los mensajes dentro de la aplicación admiten todos sus bloques de formulario estándar en cuestionarios también, incluyendo grupo de botones de opción, casilla de verificación, grupo de casillas de verificación, menú desplegable, captura de teléfono, captura de correo electrónico y captura de texto corto. Esta sección destaca los tres bloques de formulario con informes diseñados específicamente para cuestionarios: NPS, escala numérica y texto largo.

{% tabs local %}
{% tab NPS %}
### Bloque NPS independiente {#standalone-nps-block}

El bloque **NPS** es un bloque de formulario separado del bloque **Calificación** (escala numérica), no una opción de configuración dentro de él. Agrégalo a un cuestionario para hacer la pregunta estándar de Net Promoter Score (0–10) y obtener informes diseñados específicamente para ese caso de uso.

El bloque **NPS** te ofrece mejores informes en el panel que una pregunta de calificación simple usada para el mismo propósito. En lugar de un conteo plano de respuestas por número, Braze agrupa automáticamente las respuestas en promotores (9–10), pasivos (7–8) y detractores (0–6) y muestra esos segmentos, junto con la puntuación NPS resultante, directamente en la vista de análisis del cuestionario.

Currents exporta la puntuación numérica (y, si se agrega, el campo de comentarios de texto libre) en el evento **Survey Response**. Los segmentos de promotores, pasivos y detractores no son campos separados de Currents.

![Un cuestionario NPS en móvil junto al panel de respuestas del cuestionario, que muestra una puntuación NPS con desgloses de promotores, pasivos y detractores, y un gráfico de distribución de respuestas.]({% image_buster /assets/img/surveys/survey_and_chart.png %})
{% endtab %}

{% tab Escala numérica %}
### Preguntas de escala numérica {#number-scale-questions}

También llamada escala de calificación en las páginas de canal; ambos términos se refieren al mismo bloque de formulario **Calificación**. Captura preguntas de escala numérica de 1–5, 1–10 o 0–10 para adaptarse a diferentes necesidades de cuestionarios e informes, desde calificaciones simples de satisfacción hasta puntuaciones de probabilidad de recomendación. Para capturas de pantalla de composición específicas del canal, consulta la sección de escala de calificación en la página de [cuestionarios en páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) o [cuestionarios de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale).

Puedes recopilar una calificación como respuesta de cuestionario, registrarla como atributo personalizado de tipo entero, o ambos. Combina una pregunta de escala numérica con un bloque de [captura de texto largo](#long-form-text-capture) para recopilar una puntuación numérica junto con comentarios cualitativos en el mismo cuestionario.

![Editor de cuestionario de página de inicio con una pregunta de calificación 1–5 seleccionada y el panel de propiedades de calificación abierto a la derecha.]({% image_buster /assets/img/surveys/rating_block.png %})
{% endtab %}

{% tab Texto largo %}
### Captura de texto largo {#long-form-text-capture}

La captura de texto largo es útil para comentarios cualitativos. Puedes configurar el conteo mínimo y máximo de caracteres (hasta 1000 caracteres), si se muestra el límite de caracteres durante la composición, la altura del área de texto y el texto del marcador de posición.

![Configuración del bloque de captura de texto largo.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

Las respuestas de texto largo están disponibles en informes y exportaciones, pero no pueden registrarse como atributos personalizados del perfil de usuario, por lo que no puedes segmentar usuarios por un valor de respuesta de texto largo directamente. Consulta [Limitaciones]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#limitations) en cualquiera de las páginas de canal para más detalles.

En Currents, las respuestas de texto largo usan `answer_type = 'free_form_text'` con el texto en `answer_long_string`.
{% endtab %}
{% endtabs %}

## Orden aleatorio de opciones {#randomized-choice-order}

Los bloques de grupo de botones de opción, grupo de casillas de verificación y menú desplegable admiten opciones de respuesta aleatorias. Activa **Aleatorizar orden de opciones** para mezclar las opciones cada vez que se carga el cuestionario, lo que reduce el sesgo de orden cuando la misma primera opción podría de otra manera sesgar las respuestas.

La aleatorización cambia solo el orden de visualización para cada encuestado. Las etiquetas y valores de los informes permanecen mapeados a las opciones que configuraste, por lo que los análisis, las exportaciones CSV y la segmentación usan los mismos datos de respuesta independientemente del orden que un usuario determinado vio.

## Plantillas de cuestionarios {#survey-templates}

Guarda un cuestionario como plantilla desde la biblioteca de plantillas de páginas de inicio o mensajes dentro de la aplicación para que los creadores puedan comenzar desde ella en lugar de recrear las mismas preguntas y bloques de formulario cada vez. Cuando las plantillas de cuestionarios están habilitadas para tu espacio de trabajo, filtra la biblioteca por **Cuestionario** para encontrar y reutilizar estructuras de cuestionarios guardadas en Campaigns, Canvas y páginas de inicio.

## Eventos de respuesta de cuestionarios {#survey-response-events}

Las respuestas de cuestionarios fluyen hacia [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para que puedas exportar datos de cuestionarios a tu almacén de datos o una herramienta de BI de terceros para análisis posteriores, uniones con otros datos de participación e informes personalizados que van más allá de los análisis integrados del panel.

Braze exporta respuestas individuales de cuestionarios a Currents a través del evento **Survey Response** (`users.messages.survey.Response`). Cada evento representa la respuesta de un encuestado a una pregunta del cuestionario. Para la referencia completa de campos, consulta [Eventos de respuesta de cuestionarios]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#survey-response-events) en el glosario de eventos de Currents.

## Embudo de participación en páginas de inicio {#landing-page-engagement-funnel}

Los cuestionarios de páginas de inicio también generan eventos **Landing Page Impression** y **Landing Page Click** para vistas de página y clics rastreados. Completar un cuestionario de página de inicio registra un evento **Survey Response**; no dispara también el evento genérico **Landing Page Form Submission**, que es para formularios estándar (no de cuestionario) de páginas de inicio. Para la referencia completa de campos de estos eventos, consulta el [glosario de eventos de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

## Artículos relacionados {#related-articles}

- [Cuestionarios en páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys): flujo de creación, composición e informes para el canal de páginas de inicio
- [Cuestionarios de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys): flujo de creación, composición e informes para el canal de mensajes dentro de la aplicación
- [Bloques de editor de arrastrar y soltar]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks): referencia completa de los bloques de formulario que puedes agregar a un cuestionario
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents): configura la exportación de datos a tu almacén de datos o herramienta de BI