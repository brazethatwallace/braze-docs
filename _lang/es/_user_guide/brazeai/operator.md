---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Aprende a acceder y utilizar BrazeAI Operator<sup>TM</sup>, un asistente basado en inteligencia artificial integrado en el panel de Braze, incluidas sus características y mejores prácticas."
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup> es un asistente basado en inteligencia artificial integrado en el dashboard. Operator te ayuda a realizar tareas: responde preguntas, guía en la configuración, realiza la solución de problemas y aporta ideas.

## Acceder a Operator {#access-operator}

Abre Operator desde cualquier página del panel de Braze.

1. Selecciona **BrazeAI Operator<sup>TM</sup>** junto a tu perfil de usuario.

![El icono de BrazeAI Operator junto a un perfil de usuario.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. El panel de chat de Operator se abre en la parte derecha de la pantalla.

![El panel de chat de Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximiza para ampliar el panel y facilitar la lectura, o minimiza para mantener Operator disponible mientras trabajas.
{% endalert %}

Mira este video para ver un ejemplo de lo que Operator puede hacer.

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## Utilizar Operator {#use-operator}

Describe lo que intentas lograr utilizando lenguaje natural. Los prompts pueden variar desde preguntas sencillas hasta solicitudes complejas:

- **Simple:** ¿Por qué no se renderiza Liquid?
- **Complejo:** ¿Cómo puedo hacer que la etiqueta `abort_message` de mi mensaje incluya el atributo de usuario que provocó la interrupción?

Operator puede proporcionar instrucciones paso a paso, enlaces a la documentación de Braze y explicaciones en lenguaje sencillo. Las preguntas claras y específicas dan lugar a respuestas más útiles. Operator utiliza [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), que ofrece un razonamiento sólido y es adecuado para tareas complejas de varios pasos. Para ver ejemplos listos para usar, consulta la [biblioteca de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

## Mejores prácticas {#best-practices}

Trata a Operator como una conversación, no como un motor de búsqueda. Los prompts breves y naturales son los que mejor funcionan.

- **Sé específico:** En lugar de «Cuéntame sobre Canvas», prueba con «¿Cómo utilizo las Rutas de acción en Canvas?».
- **Haz preguntas de seguimiento:** Si la primera respuesta no satisface tus necesidades, solicita aclaraciones o detalles adicionales.
- **Utiliza el contexto consciente de la página:** Operator conoce tu ubicación en Braze. Abre Operator mientras visualizas la página correspondiente para obtener resultados más precisos.

## Personaliza tu experiencia {#customize-your-experience}

### Aplicar las directrices de marca {#apply-brand-guidelines}

Añade directrices de marca como contexto a las consultas de Operator para que las respuestas coincidan con la voz, el tono y la personalidad de tu marca. Operator utiliza las directrices de marca configuradas en tu espacio de trabajo, lo que ayuda a garantizar la coherencia de la mensajería cuando sugiere textos o explica características.

Para configurar las directrices de marca, ve a **Configuración** > **Directrices de marca**. Para más información, consulta [Directrices de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines).

![Seleccionar las directrices de marca en el panel de chat de Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Aprovechar el contexto consciente de la página {#leverage-page-aware-context}

Operator comprende automáticamente tu ubicación en Braze y adapta las respuestas en función de ese contexto. Por ejemplo, cuando abres Operator mientras creas un Canvas, puede sugerirte pasos relevantes u ofrecerte orientación sobre las características de Canvas sin que tengas que explicar en qué punto del flujo de trabajo te encuentras.

Esta conciencia del contexto significa que puedes formular preguntas más cortas y naturales, como «¿Cómo añado un retraso?», en lugar de «¿Cómo añado un paso de retraso en un flujo de trabajo de Canvas?». Para ver prompts listos para usar organizados por página del dashboard, consulta la [biblioteca de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

## Trabajar con las respuestas de Operator {#work-with-operator-responses}

### Empieza con los prompts sugeridos {#get-started-with-suggested-prompts}

Al abrir una conversación con Operator, aparecen prompts sugeridos basados en tareas comunes y en la página en la que te encuentras. Selecciona uno para empezar rápidamente o escribe tu propia pregunta personalizada.

### Comprender cómo piensa Operator {#understand-how-operator-thinks}

Operator muestra sus pasos de razonamiento en secciones plegables etiquetadas como **Reasoned**. Selecciona el menú desplegable para ampliar estas secciones y ver cómo Operator determinó una respuesta. Esto resulta útil cuando quieres comprender la lógica que hay detrás de una sugerencia o verificar el enfoque.

![El menú desplegable «Reasoned» colapsado en una respuesta de Operator.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Actúa con Operator {#take-action-with-operator}

Operator puede proponer y ejecutar cambios directamente en el panel de Braze, como rellenar campos de formularios, actualizar la configuración o generar contenido. Cada cambio propuesto se presenta como una tarjeta de acción para que lo revises y apruebes antes de que entre en vigor. Para obtener más información sobre cómo funciona esto, consulta [Revisión de las acciones]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions).

### Copiar respuestas a otras herramientas {#copy-responses-to-other-tools}

Las respuestas de Operator están formateadas en Markdown. Cuando recibas una respuesta, selecciona **Copy** en la barra de herramientas que aparece para copiar la respuesta completa al portapapeles. La mayoría de las herramientas renderizan Markdown de forma nativa o lo aceptan con ajustes menores. Selecciona una pestaña según tu destino:

{% tabs %}
{% tab Google Docs %}

Primero, ve a **Tools** > **Preferences** y selecciona **Automatically detect Markdown**. Luego, para pegar Markdown, ve a **Edit** > **Paste from Markdown**. También puedes hacer clic derecho y seleccionar **Paste from Markdown**.

{% endtab %}
{% tab Microsoft Word y Outlook %}

Word y Outlook no renderizan Markdown de forma nativa. Pega la respuesta en un previsualizador de Markdown basado en web, luego copia la salida renderizada y pégala en Word o Outlook con **Keep Source Formatting**. Alternativamente, pega como texto sin formato y formatea manualmente.

{% endtab %}
{% tab Confluence y Notion %}

Pega directamente. Ambas plataformas renderizan Markdown automáticamente.

{% endtab %}
{% tab Slack %}

Pega directamente. Slack renderiza negrita, código en línea, bloques de código, citas y listas con viñetas, pero no renderiza encabezados Markdown ni sintaxis de enlaces.

{% endtab %}
{% tab Otras herramientas %}

Si quieres trabajar en un archivo o usar herramientas de conversión, también puedes:

- Abrir un editor de texto como [VS Code](https://code.visualstudio.com/) y crear un nuevo archivo de texto, luego pegar el Markdown y previsualizar para revisar el formato antes de convertirlo o pegarlo en otro lugar.
- Usar [Pandoc](https://pandoc.org/) para convertir Markdown en un documento de Word, HTML o PDF cuando necesites una estructura predecible en Word o Outlook sin pegar desde un navegador.

{% endtab %}
{% endtabs %}

## Gestiona tu sesión {#manage-your-session}

### Detener una respuesta {#stop-a-response}

Mientras Operator genera una respuesta, el botón **Send** se convierte en un botón **Stop**. Selecciona **Stop** para finalizar la respuesta antes de tiempo si necesitas reformular tu pregunta o si la respuesta va por mal camino.

### Borrar tu historial {#clear-your-history}

Para empezar de cero o eliminar información confidencial de la conversación, selecciona **Clear chat history**. Esto elimina todo el contenido actual y restablece el contexto de la conversación.

### Enviar comentarios {#provide-feedback}

En la parte inferior de cada respuesta, utiliza los botones de pulgar hacia arriba o pulgar hacia abajo para proporcionar comentarios rápidos. Tus comentarios ayudan a mejorar las respuestas de Operator con el tiempo.

## Privacidad y seguridad de datos {#data-privacy-and-security}

BrazeAI Operator<sup>TM</sup> tiene integración con OpenAI, que actúa como subencargado del tratamiento de Braze con sujeción al Anexo de tratamiento de datos (DPA) entre tú y Braze. Los datos enviados a OpenAI a través de Braze no se utilizan para entrenar o mejorar los modelos de OpenAI. Para obtener detalles sobre el cumplimiento de HIPAA, la retención de datos, el manejo de PII y la gobernanza, consulta [Privacidad y seguridad de datos]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).

## Próximos pasos {#next-steps}

- [Biblioteca de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library): Examina ejemplos de prompts organizados por página del dashboard
- [Revisar acciones]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Aprende a revisar y aprobar los cambios propuestos por Operator
- [Tickets de soporte]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets): Envía tickets de soporte directamente desde Operator
- [Solución de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): Consulta problemas comunes y soluciones
- [Privacidad y seguridad de datos]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security): Revisa el cumplimiento de HIPAA, la retención de datos y las directrices de minimización de PII