---
nav_title: Capacidades
article_title: Qué puedes hacer con Operator
page_order: 1
page_type: reference
toc_headers: h2
description: "Este artículo de referencia cubre las tareas de IA disponibles a través de BrazeAI Operator™, incluyendo redacción de textos, Liquid, generación de imágenes, código de transformación de datos y revisión de contenido."
---

# Qué puedes hacer con Operator {#operator-capabilities}

> Las capacidades de IA que antes estaban disponibles como asistentes independientes ahora son accesibles a través de [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator). Dado que Operator está integrado en el dashboard y comprende tu espacio de trabajo (tus directrices de marca, atributos, Contenido conectado y la página en la que estás trabajando), el resultado es más consciente del contexto de lo que los asistentes anteriores podían producir.

En lugar de abrir una herramienta diferente para cada tarea, describe lo que quieres en lenguaje natural y Operator se encarga de ello en contexto. También puedes continuar la conversación, pidiendo un tono diferente, una versión más corta o una traducción, sin empezar de cero. Operator también puede proponer y ejecutar cambios directamente a través de [tarjetas de acción]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) que revisas antes de que surtan efecto.

## Requisitos previos {#prerequisites}

Operator tiene los mismos permisos que tú, por lo que ciertas acciones requieren el permiso correspondiente para esa superficie; por ejemplo, generar una imagen requiere *Edit Media Library Assets*. Si no ves un punto de entrada, verifica tus permisos con tu administrador. Para más información, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

## Qué está disponible a través de Operator {#whats-available-through-operator}

Todos los puntos de entrada existentes permanecen en su lugar, por lo que tus flujos de trabajo no se ven afectados. Estas experiencias ahora funcionan con Operator. La siguiente tabla relaciona cada asistente independiente anterior con dónde encontrarlo ahora.

| Asistente anterior | Qué hacía | Dónde encontrarlo ahora |
| --- | --- | --- |
| AI Copywriter | Generaba textos de marketing a partir de un nombre o descripción de producto | Un nuevo icono **Ask Operator** en los creadores de mensajes de SMS, push, correo electrónico HTML y Canvas |
| AI Liquid Assistant | Generaba Liquid para personalización | Un nuevo icono **Ask Operator** en los creadores de mensajes de SMS, push, correo electrónico HTML y Canvas |
| AI Image Generator | Generaba imágenes a partir de un prompt de texto para la biblioteca de medios | Un nuevo botón **Generate with Operator** en la biblioteca de medios |
| Data Transformations AI Copilot | Generaba código de transformación | El botón **Insert Code** en la página de Transformación de datos |
| Revisión de contenido | Verificaba el contenido en busca de errores ortográficos, gramaticales, de tono, lenguaje ofensivo y código suelto | Botón **Review with Operator** en la pestaña **Test** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Qué está disponible a través de Operator" }

## Aplicar directrices de marca {#apply-brand-guidelines}

Operator utiliza las directrices de marca configuradas en tu espacio de trabajo para que los textos, plantillas e imágenes generados coincidan con la voz, el tono y el estilo de tu marca. Para configurar las directrices de marca, ve a **Contenido** > **Directrices de marca**. Para más información, consulta [Directrices de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines). Para detalles sobre cómo aplicar directrices de marca para usar con Operator, consulta [Aplicar directrices de marca]({{site.baseurl}}/user_guide/brazeai/operator#apply-brand-guidelines).

## Generar textos {#generate-copy}

Puedes usar Operator para hacer lluvia de ideas o generar textos desde cualquier lugar, pero obtienes la mejor experiencia usándolo directamente en el creador de mensajes, donde puede trabajar junto a ti en el mensaje que estás construyendo. Describe tu producto o campaña, y Operator devuelve textos que puedes revisar e insertar.

Operator mejora al redactor independiente de varias maneras:

- Aplica tus [directrices de marca](#apply-brand-guidelines) automáticamente cuando están configuradas.
- Utiliza [contexto consciente de la página]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context), por lo que no tienes que volver a describir el canal o mensaje en el que estás trabajando. Como es consciente de la página, también puedes usarlo para editar o refinar un mensaje existente en lugar de generar uno desde cero.
- Puede buscar tus [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) y eventos, para que puedas pedirle que personalice las recomendaciones de texto con Liquid real.
- Puedes continuar la conversación e iterar. Por ejemplo, pide un tono diferente, una versión más corta o una traducción.

### Tonos {#generate-copy-tones}

El tono del texto generado está determinado por tu prompt. Describe el estilo que deseas —por ejemplo, formal, casual, urgente o llamativo— y Operator ajusta su resultado para que coincida. También puedes refinar el tono en prompts de seguimiento, como pedir una versión más relajada o más pulida. Cuando las [directrices de marca](#apply-brand-guidelines) están configuradas, Operator las aplica automáticamente para que el texto se mantenga consistente con la voz de tu marca.

### Prompts de ejemplo {#generate-copy-example-prompts}

{% include copy_block.html content="Write a short, eye-catching push notification announcing our summer sale." %}

{% include copy_block.html content="Rewrite this subject line in a more casual tone." %}

{% include copy_block.html content="Translate this copy into Spanish." %}

## Generar Liquid {#generate-liquid}

En cualquier creador de mensajes, abre Operator para generar y refinar Liquid para personalización. Operator comprende la [sintaxis de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), tus atributos estándar y [personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), y el [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), y puede explicar qué hace el código.

### Dónde puedes generar Liquid {#generate-liquid-supported-channels}

Al igual que con la redacción de textos, puedes pedirle a Operator que genere Liquid desde cualquier lugar, y funciona en todos los canales y creadores de mensajes. Obtienes los mejores resultados desde dentro de un creador de mensajes, donde Operator tiene el contexto completo del mensaje que estás construyendo.

### Capacidades de Liquid {#generate-liquid-attributes}

Operator es altamente capaz con Liquid. Puede generar lógica Liquid compleja basada en los datos de tu espacio de trabajo —incluyendo la búsqueda de datos de [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) para encontrar valores de ejemplo— y puede revisar y explicar el Liquid existente en tus Campaigns.

### Mejores prácticas {#generate-liquid-best-practices}

#### Usa lenguaje natural {#generate-liquid-use-natural-language}

Operator está entrenado para comprender el lenguaje natural. Conversa con él como lo harías con un compañero de trabajo al pedir ayuda. Esto ayuda a Operator a comprender tus necesidades y proporcionar asistencia precisa.

#### Da contexto {#generate-liquid-give-context}

Proporcionar contexto ayuda a Operator a comprender el panorama general de tu proyecto. Es útil incluir contexto como:

- El nombre de tu empresa y la industria
- Una campaña en la que estás trabajando, como Black Friday o ventas navideñas
- Tu objetivo, como aumentar tu tasa de click-through
- Atributos personalizados específicos que quieres incluir en tu mensaje

Incluir contexto en tu prompt ayuda a Operator a adaptar sus respuestas para que se ajusten mejor a tus necesidades. También puedes incluir detalles de tu campaña, resumen del mensaje o documento de lluvia de ideas para poner a Operator al día.

#### Sé específico {#generate-liquid-be-specific}

Operator puede hacer preguntas de seguimiento, pero proporcionar detalles por adelantado puede llevar a resultados más precisos más rápido. Considera incluir detalles como:

- Cualquier preferencia o requisito conocido para el mensaje
- Instrucciones sobre cómo manejar situaciones, como la falta de respuestas del destinatario del mensaje u opciones de mensaje alternativo
- Valores exactos o similares para los atributos personalizados que quieres usar, que ayudan a Operator a generar y probar lógica más precisa
- Al pedir Liquid que use Contenido conectado, documentación del punto de conexión de la API, una respuesta de API de ejemplo, o ambos

#### Sé creativo {#generate-liquid-get-creative}

Prueba diferentes prompts para ver cómo Operator puede mejorar tu mensajería. Experimenta con diferentes prompts e ideas, ya que la creatividad puede llevar a resultados más atractivos.

### Prompts de ejemplo {#generate-liquid-example-prompts}

{% tabs local %}
{% tab Sobre Liquid %}

{% include copy_block.html content="What is Liquid, and how can it help me enhance the personalization of my marketing campaigns within Braze?" %}

{% include copy_block.html content="What types of data can I use in Liquid to personalize my marketing messages, such as demographic information or past purchases?" %}

{% include copy_block.html content="Can you give me some examples of how Liquid is used in marketing campaigns to increase engagement and conversion rates?" %}

{% include copy_block.html content="What are some common use cases for Liquid in text messages for summer sales, such as abandoned cart reminders or personalized promotions?" %}

{% endtab %}
{% tab Personalización %}

{% include copy_block.html content="Add a countdown to this message that shows the time until the user's flight." %}

{% include copy_block.html content="Personalize this message with the user's first name, with a fallback if it's missing." %}

{% include copy_block.html content="Improve this Liquid so it's easier to read." %}

{% include copy_block.html content="Create a message that shows different content based on my customer's loyalty status. If we don't know about their loyalty status, send a fallback message." %}

{% include copy_block.html content="Write a dynamic message that includes a user's favorite product and their last purchase date. If there's no last purchase, abort the message." %}

{% include copy_block.html content="Write me Liquid to encourage someone to click my message that includes a countdown with how much time is left. If the offer has expired, abort the message." %}

{% include copy_block.html content="Help me write a message to encourage users to come back and check out if they have items remaining in their cart." %}

{% include copy_block.html content="Write Liquid to personalize a message based on a customer's country. I want to fill in the message with the country's name. If we don't have either of them, suggest they click on a link to update their profile." %}

{% include copy_block.html content="How can I personalize a welcome message with a user's first name and write different copy based on the user's gender?" %}

{% include copy_block.html content="Write Liquid to display different messages based on a custom attribute, \"CUSTOM_ATTRIBUTE_NAME\" and its value. There are six different options I could send. If there's no value for the custom attribute, I want to send a placeholder message." %}

{% endtab %}
{% endtabs %}

## Generar imágenes {#generate-images}

Operator genera imágenes usando [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/), un sistema de IA de OpenAI y un proveedor externo de Braze. Esto te permite crear imágenes realistas y arte a partir de una descripción en lenguaje natural.

En la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library), selecciona **Generate with Operator** en el panel **Upload Assets**. Describe la imagen que deseas, y Operator la genera y la guarda directamente en tu biblioteca de medios.

### Consejos para prompts {#generate-images-prompt-tips}

- Describe el tema, estilo, estado de ánimo y colores de forma específica. Cuanto más detalle incluyas, mejor será el resultado.
- Solo entrada de texto; no se admite la carga de una imagen de referencia.
- Cuando aplicas [directrices de marca](#apply-brand-guidelines) como contexto en tu prompt de Operator, Operator las aplica directamente a la imagen generada, de modo que el resultado refleja el estilo visual de tu marca.
- Las generaciones de imágenes cuentan para tu límite diario de uso de Operator. Para más información, consulta [Limitaciones]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting#limitations).

### Prompts de ejemplo {#generate-images-example-prompts}

{% include copy_block.html content="Generate a bright, summery banner image of a beach scene for an email header." %}

{% include copy_block.html content="Create a minimalist product background in our brand colors." %}

## Generar código de transformación de datos {#generate-data-transformation-code}

En el editor de [Transformación de datos]({{site.baseurl}}/user_guide/data/unification/data_transformation), selecciona **Insert Code** para generar código de transformación que convierte una carga útil de webhook entrante en solicitudes válidas de la API de Braze.

Para instrucciones paso a paso sobre cómo crear una transformación, consulta [Crear una transformación]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation).

### Prompts de ejemplo {#generate-data-transformation-example-prompts}

{% include copy_block.html content="Write transformation code that maps this survey webhook to a custom event on the user's profile." %}

{% include copy_block.html content="Update this transformation to identify users by email address instead of external ID." %}

## Revisar la calidad del contenido {#review-content-quality}

En la pestaña **Test** para SMS, push de Android, push de iOS y mensajes dentro de la aplicación tradicionales, selecciona **Review with Operator** para revisar tu contenido antes de enviarlo. De forma predeterminada, Operator revisa tu campaña en busca de errores ortográficos y gramaticales, tono inapropiado o fuera de marca, lenguaje ofensivo y cualquier código suelto, contenido de prueba o Liquid sin renderizar, y recomienda cómo corregir lo que encuentra. También puedes pedirle a Operator que adapte cómo revisa tu contenido directamente en tu prompt.

### Qué puedes pedirle a Operator que verifique {#review-content-quality-supported-features}

Más allá de su revisión predeterminada, puedes dirigir a Operator para que se enfoque en verificaciones específicas. Considera pedirle que revise cualquiera de los siguientes aspectos:

| Verificación | Qué pedir |
| --- | --- |
| Ortografía y gramática | Pide a Operator que revise errores ortográficos y gramaticales y sugiera correcciones que mejoren la precisión de tu contenido. |
| Tono | Pide a Operator que evalúe si el tono coincide con tu estilo de comunicación previsto y señale cualquier cosa que pueda malinterpretarse. |
| Lenguaje ofensivo | Pide a Operator que busque lenguaje potencialmente ofensivo o inapropiado para que puedas revisarlo y mantener tu mensajería respetuosa. |
| Contenido accidental | Pide a Operator que detecte código suelto, marcado o mensajes de prueba que agregaste involuntariamente, incluyendo Liquid que no se renderizó para un usuario de prueba. |
| Otros idiomas | Pide a Operator que revise contenido escrito en otro idioma. El soporte para contenido en idiomas distintos al inglés puede variar, así que revisa los resultados cuidadosamente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Qué puedes pedirle a Operator que verifique" }

### Mejores prácticas {#review-content-quality-best-practices}

Considera lo siguiente para aprovechar al máximo la revisión de contenido:

- **Revisa tu mensaje:** Aunque la revisión de contenido puede ayudar a identificar errores, sigue siendo esencial revisar tu contenido manualmente. Confía en las sugerencias generadas por IA como una guía útil, pero usa tu criterio para garantizar la precisión.
- **Comprende el análisis de tono:** Los resultados del análisis de tono son subjetivos y se basan en la comprensión del modelo de IA. Si bien pueden proporcionar información útil, considera tu tono previsto y el contexto de la conversación para hacer los ajustes apropiados.
- **Verifica el lenguaje ofensivo señalado:** La detección de lenguaje ofensivo está diseñada para ser robusta, pero ocasionalmente puede señalar falsos positivos. Revisa las secciones señaladas cuidadosamente y realiza los cambios apropiados según sea necesario.

### Prompts de ejemplo {#review-content-quality-example-prompts}

{% include copy_block.html content="Review this push notification for spelling, grammar, and tone, and flag any unrendered Liquid or leftover test content before I send it." %}

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Privacidad y seguridad de datos {#data-privacy-and-security}

Operator se integra con OpenAI para generar resultados. Para más información sobre qué información envía Braze a OpenAI, cómo se utilizan esos datos y tus derechos de propiedad intelectual, consulta [Cómo se utilizan los datos con OpenAI]({{site.baseurl}}/user_guide/brazeai/operator#how-data-is-used-with-openai).

## Próximos pasos {#next-steps}

- [Comenzar con Operator]({{site.baseurl}}/user_guide/brazeai/operator): accede y usa Operator
- [Revisar acciones]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): revisa y aprueba los cambios propuestos por Operator
- [Solución de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): consulta problemas comunes y soluciones