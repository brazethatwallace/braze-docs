---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Aprende a acceder y utilizar BrazeAI Operator<sup>TM</sup>, un asistente basado en inteligencia artificial integrado en el panel de Braze, incluidas sus características y mejores prácticas."
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup> es un asistente basado en inteligencia artificial integrado en el panel. Operator te ayuda a construir —redactando Campaigns, Canvas, Segments y contenido— y te ayuda a avanzar, desde responder preguntas y solucionar problemas hasta generar ideas.

## Acceder a Operator {#access-operator}

Abre Operator desde cualquier página en el panel de Braze.

1. Selecciona **BrazeAI Operator<sup>TM</sup>** junto a tu perfil de usuario.
2. El panel de chat de Operator se abre en un panel lateral.

![El panel de chat de Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximiza para expandir el panel y facilitar la lectura, o minimiza para mantener Operator disponible mientras trabajas.
{% endalert %}

## Usar Operator {#use-operator}

Describe lo que intentas lograr usando lenguaje natural. Los prompts claros y específicos generan respuestas más útiles. Los prompts pueden ir desde una simple pregunta hasta una solicitud de construcción completa:

- **Haz una pregunta:** ¿Por qué no se está renderizando mi Liquid?
- **Construye algo:** Crea un borrador de un Segment de usuarios que abandonaron su carrito en los últimos 7 días.

Operator puede proporcionar instrucciones paso a paso, enlaces a la documentación de Braze, explicaciones en lenguaje natural y borradores de Campaigns, Canvas, Segments y contenido que puedes revisar e insertar directamente en tu trabajo. Para saber cómo Operator propone y aplica cambios, consulta [Tomar acción con Operator](#take-action-with-operator).

Operator utiliza [GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra), que es adecuado para tareas complejas y de múltiples pasos. Para conocer toda la gama de lo que Operator puede ayudarte a construir, consulta [Qué puedes hacer con Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). Para ejemplos listos para usar, consulta la [biblioteca de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

Mira este video para ver un ejemplo de lo que Operator puede hacer.

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## Mejores prácticas {#best-practices}

Trata a Operator como una conversación, no como un motor de búsqueda. Los prompts cortos y naturales funcionan mejor.

- **Sé específico:** En lugar de "Cuéntame sobre Canvas", prueba "¿Cómo uso las Rutas de Acción en Canvas?".
- **Haz preguntas de seguimiento:** Si la primera respuesta no aborda tu necesidad, pide aclaraciones o detalles adicionales. Operator recuerda los mensajes anteriores en la conversación hasta que borres tu historial de chat.
- **Aprovecha el contexto de la página:** Operator comprende tu ubicación en Braze. Abre Operator mientras visualizas la página relevante para obtener los resultados más precisos.

## Personaliza tu experiencia {#customize-your-experience}

### Aplica las directrices de marca {#apply-brand-guidelines}

Añade directrices de marca como contexto a las consultas de Operator para que las respuestas coincidan con la voz, el tono y la personalidad de tu marca. Operator utiliza las directrices de marca configuradas en tu espacio de trabajo, lo que ayuda a garantizar una mensajería coherente cuando sugiere textos o explica características.

Para configurar las directrices de marca, ve a **Contenido** > **Directrices de marca**. Para más información, consulta [Directrices de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines).

![Selección de directrices de marca en el panel de chat de Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Aprovecha el contexto de la página {#leverage-page-aware-context}

Operator entiende automáticamente tu ubicación en Braze y adapta las respuestas en función de ese contexto. Por ejemplo, cuando abres Operator mientras construyes un Canvas, puede sugerirte pasos relevantes o proporcionarte orientación sobre las características de Canvas sin que tengas que explicar en qué parte de tu flujo de trabajo te encuentras.

Esta consciencia del contexto significa que puedes usar prompts cortos y naturales para interactuar con Operator, como "Actualiza la configuración de mi editor para que coincida con mis directrices de marca." Cuando tu solicitud necesita una parte diferente del panel, Operator puede [llevarte allí]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard) directamente.

Para ideas de prompts listas para usar, consulta la [biblioteca de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

## Trabajar con las respuestas de Operator {#work-with-operator-responses}

### Comienza con prompts sugeridos {#get-started-with-suggested-prompts}

Cuando abres una conversación con Operator, aparecen prompts sugeridos basados en tareas comunes y la página en la que te encuentras. Selecciona uno para comenzar rápidamente o escribe tu propia pregunta personalizada.

### Comprende cómo piensa Operator {#understand-how-operator-thinks}

Operator muestra sus pasos de razonamiento en secciones contraíbles etiquetadas como **Reasoned**. Selecciona el desplegable para expandir estas secciones y ver cómo Operator determinó una respuesta. Esto es útil cuando quieres entender la lógica detrás de una sugerencia o verificar el enfoque.

![El desplegable "Reasoned" contraído en una respuesta de Operator.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Toma acción con Operator {#take-action-with-operator}

Operator puede proponer y ejecutar cambios directamente en el panel de Braze, como rellenar campos de formulario, actualizar configuraciones, generar contenido o navegar a una página diferente para completar tu solicitud. Cada cambio propuesto se presenta como una tarjeta de acción para que la revises y apruebes antes de que surta efecto. Para más información sobre cómo funciona, consulta [Revisar acciones]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions).

### Copia las respuestas a otras herramientas {#copy-responses-to-other-tools}

Las respuestas de Operator están formateadas en Markdown. Cuando hayas recibido una respuesta, selecciona **Copy** en la barra de herramientas que aparece para copiar la respuesta completa a tu portapapeles. La mayoría de las herramientas renderizan Markdown de forma nativa o lo aceptan con ajustes menores. Selecciona una pestaña según tu destino:

{% tabs %}
{% tab Google Docs %}

Primero, ve a **Tools** > **Preferences** y selecciona **Automatically detect Markdown**. Luego, para pegar Markdown, ve a **Edit** > **Paste from Markdown**. También puedes hacer clic derecho y seleccionar **Paste from Markdown**.

{% endtab %}
{% tab Microsoft Word and Outlook %}

Word y Outlook no renderizan Markdown de forma nativa. Pega la respuesta en un previsualizador de Markdown basado en web, luego copia la salida renderizada y pégala en Word o Outlook con **Keep Source Formatting**. Alternativamente, pega como texto sin formato y formatea manualmente.

{% endtab %}
{% tab Confluence and Notion %}

Pega directamente. Ambas plataformas renderizan Markdown automáticamente.

{% endtab %}
{% tab Slack %}

Pega directamente. Slack renderiza negritas, código en línea, bloques de código, citas y listas con viñetas, pero no renderiza encabezados Markdown ni la sintaxis de enlaces.

{% endtab %}
{% tab Otras herramientas %}

Si quieres trabajar en un archivo o usar herramientas de conversión, también puedes:

- Abrir un editor de texto como [VS Code](https://code.visualstudio.com/) y crear un nuevo archivo de texto, luego pegar el Markdown y previsualizar para revisar el formato antes de convertirlo o pegarlo en otro lugar.
- Usar [Pandoc](https://pandoc.org/) para convertir Markdown en un documento de Word, HTML o PDF cuando necesites una estructura predecible en Word o Outlook sin pegar desde un navegador.

{% endtab %}
{% endtabs %}

## Gestiona tu sesión {#manage-your-session}

### Detener una respuesta {#stop-a-response}

Mientras Operator está generando una respuesta, el botón **Enviar** se convierte en un botón **Detener**. Selecciona **Detener** para finalizar la respuesta anticipadamente si necesitas reformular tu pregunta o si la respuesta va en la dirección equivocada.

### Borrar tu historial {#clear-your-history}

Para empezar de nuevo o eliminar información sensible de la conversación, selecciona **Borrar historial de chat**. Esto elimina todo el contenido actual y restablece el contexto de la conversación.

### Enviar comentarios {#provide-feedback}

En la parte inferior de cada respuesta, usa los botones de pulgar arriba o pulgar abajo para enviar comentarios rápidos. Tus comentarios ayudan a mejorar las respuestas de Operator con el tiempo.

## Privacidad y seguridad de datos {#data-privacy-and-security}

BrazeAI Operator<sup>TM</sup> se integra con OpenAI, que actúa como subprocesador de Braze sujeto al Anexo de procesamiento de datos (DPA) entre tú y Braze. Los datos enviados a OpenAI a través de Braze no se utilizan para entrenar ni mejorar los modelos de OpenAI. Para más información sobre el cumplimiento de HIPAA, la retención de datos, el tratamiento de PII y la gobernanza, consulta [Privacidad y seguridad de datos]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).

## Próximos pasos {#next-steps}

- [Qué puedes hacer con Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities): Explora las capacidades de Operator en todo el panel
- [Biblioteca de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library): Examina ejemplos de prompts organizados por página del panel
- [Revisar acciones]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Aprende a revisar y aprobar los cambios propuestos por Operator
- [Enviar tickets de soporte]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets): Envía tickets de soporte directamente desde Operator
- [Solución de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): Consulta problemas comunes y soluciones
- [Privacidad y seguridad de datos]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security): Revisa el cumplimiento de HIPAA, la retención de datos y las directrices de minimización de PII