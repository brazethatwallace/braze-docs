---
nav_title: Capacidades
article_title: Qué puedes hacer con Operator
page_order: 1
page_type: reference
toc_headers: h2
description: "Este artículo de referencia cubre lo que BrazeAI Operator™ puede hacer en todo el panel, incluyendo la creación de Campaigns, Segments y agentes; la generación de textos, mensajes, Liquid e imágenes; la transformación de datos; la revisión de la calidad del contenido; y la búsqueda de información."
---

# Qué puedes hacer con Operator {#operator-capabilities}

> [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator) es un asistente de IA integrado en el panel de Braze. Responde preguntas, redacta mensajes y actúa en las páginas compatibles: describe lo que quieres en lenguaje natural y Operator se encarga de ello en contexto.

Dado que Operator comprende tu espacio de trabajo —tus directrices de marca, atributos personalizados, contenido conectado y la página en la que estás trabajando—, su resultado es más consciente del contexto de lo que los asistentes independientes pueden producir. Cuando Operator propone un cambio en una Campaign, un Segment u otro objeto, muestra el cambio como una diferencia visual en una [tarjeta de acción]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) que revisas y apruebas antes de que se guarde nada.

Puedes continuar la conversación con seguimientos. Operator recuerda los mensajes anteriores hasta que borres tu historial de chat.

## Requisitos previos {#prerequisites}

Operator tiene los mismos permisos que tú, por lo que ciertas acciones requieren el permiso correspondiente para esa superficie. Por ejemplo, generar una imagen requiere *Editar activos de la biblioteca multimedia*. Si no ves un punto de entrada, comprueba tus permisos con tu administrador. Para más información, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

## Qué puede crear Operator {#what-operator-can-create}

Además de generar textos y Liquid, Operator puede ayudarte a crear varios otros objetos en todo el panel, incluyendo, entre otros:

- Campaigns
- Content Blocks
- Agentes personalizados
- Imágenes
- Mensajes y plantillas de mensajes (consulta [Generar mensajes](#generate-messages) y [Crear plantillas de mensajes](#create-message-templates))
- Segments
- Extensiones de segmento

{% alert note %}
Las capacidades de Operator en todo el panel se amplían regularmente. **Pregunta directamente a Operator** para obtener la respuesta más actualizada sobre lo que puede hacer.
{% endalert %}

## Campaigns y audiencias {#campaigns-and-audiences}

Operator puede ayudarte a pasar de una idea a un borrador de Campaign o audiencia, y refinar cualquiera de los dos una vez que exista. Cualquier cambio que Operator proponga a una Campaign o un Segment aparece como una tarjeta de acción que revisas antes de que se guarde.

Para empezar, busca la opción **Create with Operator** cuando crees una Campaign o un Segment.

![Los menús Crear Campaign y Crear Segment, cada uno mostrando la opción Create with Operator.]({% image_buster /assets/img/operator/operator_create_with_operator.png %}){:style="max-width:90%"}

- **Crear y editar Campaigns:** Cuando inicias una Campaign, Operator puede ayudarte a redactarla de principio a fin a partir de un solo resumen en lenguaje natural. Esto incluye audiencia, contenido y configuración de entrega. También puedes pedirle a Operator que te ayude a editar una Campaign existente, como ajustar la segmentación o actualizar el contenido del mensaje.
- **De resumen a Campaign:** Describe un resumen completo de Campaign, y Operator te ayuda a crear un borrador que incluye texto, imágenes, personalización, segmentación y recomendaciones de hora de envío. Revisa el borrador en el creador de Campaign y refínalo con prompts de seguimiento antes de lanzarlo.
- **Crear y editar Segments:** Cuando inicias un Segment, describe la audiencia que deseas y Operator te ayuda a construir la lógica de filtros, incluyendo condiciones de atributos, historial de eventos y búsquedas en catálogos. Operator también puede ayudarte a editar los filtros de un Segment existente cuando tu estrategia de segmentación necesita cambios.
- **Crear extensiones de segmento:** Operator puede ayudarte a crear una [extensión de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) definida por SQL escribiendo la consulta que la define. Describe la lógica de audiencia que deseas, y Operator redacta la consulta para que la revises antes de guardarla. Para más información sobre Operator y SQL, consulta [Escribir consultas SQL](#write-sql-queries).

## Agentes {#agents}

![El menú Crear agente, mostrando la opción de agente personalizado y las plantillas de agentes creadas con Operator.]({% image_buster /assets/img/operator/operator_create_agent.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

Operator puede ayudarte a crear y refinar agentes en [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents). Cualquier cambio que Operator proponga a un agente aparece como una tarjeta de acción que revisas antes de que se guarde.

- **Crear un agente desde cero:** Operator tiene acceso a todos los campos en Agent Console, así que puedes describir el agente que deseas y Operator te ayuda a configurarlo. Esto incluye instrucciones, configuración de salida y otros campos del agente.
- **Empezar desde una plantilla:** Agent Console ofrece una opción **Create agent with Operator** que carga un prompt preescrito para un caso de uso común, como redacción de textos, análisis de sentimiento, enrutamiento de recorridos o enriquecimiento de catálogos. Selecciona una categoría, y Operator te ayuda a redactar un agente que puedes refinar. Para la lista completa de plantillas, consulta [Plantillas de agentes creadas con Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).
- **Refinar un agente existente:** Cuando estás editando un agente, selecciona **Generate with Operator** o **Refine with Operator** cerca del campo de instrucciones del agente para obtener la ayuda de Operator al escribir o revisar el prompt y la configuración de salida del agente.

## Contenido y creatividad {#content-and-creative}

Operator puede generar y revisar el contenido de tus mensajes, incluyendo textos, HTML de mensajes, Liquid e imágenes, y aplica tus directrices de marca automáticamente donde estén configuradas.

### Aplicar directrices de marca {#apply-brand-guidelines}

Operator utiliza las directrices de marca configuradas en tu espacio de trabajo para que los textos, plantillas e imágenes generados coincidan con la voz, el tono y el estilo de tu marca. Para configurar las directrices de marca, ve a **Content** > **Brand Guidelines**. Para más información, consulta [Directrices de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) y [Aplicar directrices de marca]({{site.baseurl}}/user_guide/brazeai/operator#apply-brand-guidelines) en la guía de uso de Operator.

### Generar textos {#generate-copy}

Puedes usar Operator para hacer lluvia de ideas o generar textos desde cualquier lugar, pero obtienes la mejor experiencia usándolo directamente en el creador de mensajes, donde puede trabajar junto a ti en el mensaje que estás construyendo. Describe tu producto o Campaign, y Operator devuelve textos que puedes revisar e insertar.

Operator mejora respecto al redactor independiente de varias maneras:

- Aplica tus [directrices de marca](#apply-brand-guidelines) automáticamente cuando están configuradas.
- Utiliza [contexto consciente de la página]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context), por lo que no tienes que volver a describir el canal o mensaje en el que estás trabajando. Como es consciente de la página, también puedes usarlo para editar o refinar un mensaje existente en lugar de generar uno desde cero.
- Puede buscar tus [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) y eventos, para que puedas pedirle que personalice las recomendaciones de texto con Liquid real.
- Puedes continuar la conversación e iterar. Por ejemplo, pide un tono diferente, una versión más corta o una traducción.

#### Tonos {#generate-copy-tones}

El tono del texto generado está determinado por tu prompt. Describe el estilo que deseas y Operator ajusta su resultado para que coincida. Por ejemplo, pide un tono formal, casual, urgente o llamativo. También puedes refinar el tono en prompts de seguimiento, como pedir una versión más relajada o más pulida. Cuando las directrices de marca están configuradas, Operator las aplica automáticamente para que el texto se mantenga consistente con la voz de tu marca.

### Generar mensajes {#generate-messages}

Operator puede generar un diseño de mensaje completo para cualquier canal o editor con un modo HTML, incluyendo, entre otros:

- Correo electrónico
- SMS/MMS/RCS
- Mensaje dentro de la aplicación
- Tarjeta de contenido
- Banner
- Push
- Webhook

Los editores de arrastrar y soltar no admiten la generación directa de diseños, aunque Operator aún puede ayudar con textos u otro contenido que agregues manualmente. Describe el mensaje que deseas en lenguaje natural, revisa el resultado e insértalo en tu creador. Continúa la conversación para refinar el resultado. Por ejemplo, puedes pedir un diseño diferente, un texto más corto o un estilo de botón actualizado antes de insertar el HTML en el editor.

Obtienes los mejores resultados cuando usas Operator en el creador en el que estás trabajando, donde tiene [contexto consciente de la página]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context) para el canal y tipo de mensaje. Cuando las directrices de marca están configuradas, Operator las aplica automáticamente.

### Crear Content Blocks {#create-content-blocks}

Operator puede ayudarte a crear [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks), las piezas de contenido reutilizables que insertas en los mensajes. Describe el bloque que deseas, y Operator redacta su contenido para que lo revises antes de guardarlo. Como los Content Blocks son compartidos, actualizar uno actualiza cada mensaje que lo referencia.

Operator crea Content Blocks de uno en uno en el panel. Para crear Content Blocks de forma masiva, usa el endpoint [Crear bloque de contenido]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) con una clave de API que tenga el permiso `content_blocks.create`.

### Crear plantillas de mensajes {#create-message-templates}

Operator puede ayudarte a crear [plantillas de mensajes]({{site.baseurl}}/user_guide/messaging/templates) reutilizables que puedes aplicar en todas las Campaigns. Describe la plantilla que deseas, y Operator la redacta para que la revises antes de guardarla. Generar una plantilla funciona de manera muy similar a generar un mensaje, así que consulta [Generar mensajes](#generate-messages) para los canales y editores compatibles.

### Generar Liquid {#generate-liquid}

Operator es altamente capaz con la [sintaxis de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid). Puede generar lógica Liquid compleja basada en los datos de tu espacio de trabajo, incluyendo la búsqueda de datos de atributos, eventos y [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) para encontrar valores de ejemplo. También puede revisar y explicar el Liquid existente en tus Campaigns.

Al igual que con la redacción de textos, puedes pedirle a Operator que genere Liquid desde cualquier lugar, y funciona en todos los canales y creadores de mensajes. Obtienes los mejores resultados desde dentro de un creador de mensajes, donde Operator tiene el contexto completo del mensaje que estás construyendo.

{% details Mejores prácticas para prompts de Liquid %}

#### Da contexto {#generate-liquid-give-context}

Proporcionar contexto ayuda a Operator a comprender el panorama general de tu proyecto. Es útil incluir contexto como:

- El nombre de tu empresa y la industria
- Una Campaign en la que estás trabajando, como Black Friday o ventas navideñas
- Tu objetivo, como aumentar tu tasa de click-through
- Atributos personalizados específicos que quieres incluir en tu mensaje

Incluir contexto en tu prompt ayuda a Operator a adaptar sus respuestas para que se ajusten mejor a tus necesidades. También puedes incluir detalles de tu Campaign, resumen del mensaje o documento de lluvia de ideas para poner a Operator al día.

#### Sé específico {#generate-liquid-be-specific}

Operator puede hacer preguntas de seguimiento, pero proporcionar detalles por adelantado puede llevar a resultados más precisos más rápido. Considera incluir detalles como:

- Cualquier preferencia o requisito conocido para el mensaje
- Instrucciones sobre cómo manejar situaciones, como la falta de respuestas del destinatario del mensaje u opciones de mensaje alternativo
- Valores exactos o similares para los atributos personalizados que quieres usar, que ayudan a Operator a generar y probar lógica más precisa
- Al pedir Liquid que use contenido conectado, documentación del endpoint de la API, una respuesta de API de ejemplo, o ambos

#### Sé creativo {#generate-liquid-get-creative}

Prueba diferentes prompts para ver cómo Operator puede mejorar tu mensajería. Experimenta con diferentes prompts e ideas, ya que la creatividad puede llevar a resultados más atractivos.

{% enddetails %}

### Generar imágenes {#generate-images}

Operator genera imágenes usando [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/), un sistema de IA de OpenAI y un proveedor externo de Braze. Esto te permite crear imágenes realistas y arte a partir de una descripción en lenguaje natural.

En la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library), selecciona **Generate with Operator** en el panel **Upload Assets**. Describe la imagen que deseas, y Operator la genera y la guarda directamente en tu biblioteca de medios.

#### Consejos para prompts {#generate-images-prompt-tips}

- Describe el tema, estilo, estado de ánimo y colores de forma específica. Cuanto más detalle incluyas, mejor será el resultado. No se admite la carga de una imagen de referencia.
- Cuando aplicas [directrices de marca](#apply-brand-guidelines) como contexto en tu prompt de Operator, Operator las aplica directamente a la imagen generada, de modo que el resultado refleja el estilo visual de tu marca.
- Las generaciones de imágenes cuentan para tu límite diario de uso de Operator. Para más información, consulta [Limitaciones](#limitations).

### Revisar la calidad del contenido {#review-content-quality}

En la pestaña **Test** para SMS, push de Android, push de iOS y mensajes dentro de la aplicación tradicionales, selecciona **Review with Operator** para revisar tu contenido antes de enviarlo. De forma predeterminada, Operator revisa tu Campaign en busca de errores ortográficos y gramaticales, tono inapropiado o fuera de marca, lenguaje ofensivo y cualquier código suelto, contenido de prueba o Liquid sin renderizar, y recomienda cómo corregir lo que encuentra. También puedes pedirle a Operator que adapte cómo revisa tu contenido directamente en tu prompt.

Más allá de su revisión predeterminada, puedes dirigir a Operator para que se enfoque en verificaciones específicas. Considera pedirle que revise cualquiera de los siguientes aspectos:

- **Ortografía y gramática:** Revisa errores ortográficos y gramaticales y sugiere correcciones que mejoren la precisión de tu contenido.
- **Tono:** Evalúa si el tono coincide con tu estilo de comunicación previsto y señala cualquier cosa que pueda malinterpretarse.
- **Lenguaje ofensivo:** Busca lenguaje potencialmente ofensivo o inapropiado para que puedas revisarlo y mantener tu mensajería respetuosa.
- **Contenido accidental:** Detecta código suelto, marcado o mensajes de prueba que se agregaron involuntariamente, incluyendo Liquid que no se renderizó para un usuario de prueba.
- **Otros idiomas:** Revisa contenido escrito en otro idioma. El soporte para contenido en idiomas distintos al inglés puede variar, así que revisa los resultados cuidadosamente.

#### Mejores prácticas {#review-content-quality-best-practices}

Considera lo siguiente para aprovechar al máximo la revisión de contenido:

- **Revisa tu mensaje:** Aunque la revisión de contenido puede ayudar a identificar errores, sigue siendo esencial revisar tu contenido manualmente. Confía en las sugerencias generadas por IA como una guía útil, pero usa tu criterio para garantizar la precisión.
- **Comprende el análisis de tono:** Los resultados del análisis de tono son subjetivos y se basan en la comprensión del modelo de IA. Si bien pueden proporcionar información útil, considera tu tono previsto y el contexto de la conversación para hacer los ajustes apropiados.
- **Verifica el lenguaje ofensivo señalado:** La detección de lenguaje ofensivo está diseñada para ser robusta, pero ocasionalmente puede señalar falsos positivos. Revisa las secciones señaladas cuidadosamente y realiza los cambios apropiados según sea necesario.

## Automatización de datos y búsqueda {#data-automation-and-lookup}

Operator puede actuar como referencia para los datos de tu espacio de trabajo y la documentación de Braze, escribir SQL cuando necesites consultar esos datos directamente y generar el código que transforma los datos entrantes, como una carga útil de webhook, en un formato que Braze pueda usar.

### Qué puede buscar Operator {#what-operator-can-look-up}

Operator puede consultar lo siguiente para responder preguntas o fundamentar el contenido que genera, incluyendo, entre otros:

- Documentación de Braze
- [Segments]({{site.baseurl}}/user_guide/audience/segments)
- [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) y [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events)
- Datos de [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs)
- Configuración de [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns) y [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) existentes, como segmentación y configuración de entrega
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [Códigos promocionales]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)
- Respuestas de [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Agentes]({{site.baseurl}}/user_guide/brazeai/agents)

Pregunta directamente a Operator si no estás seguro de si puede buscar una información específica.

### Analizar datos de rendimiento {#analyze-performance-data}

Haz preguntas a Operator en lenguaje natural sobre el rendimiento de tus Campaigns y Canvas, y te devolverá gráficos, comparaciones e información breve extraída de los datos de tu espacio de trabajo. A diferencia de las funciones de Operator que dependen del contexto de la página en la que te encuentras, Analyze responde desde cualquier lugar del panel. Para más información, consulta [Operator Analyze]({{site.baseurl}}/user_guide/brazeai/operator/analyze).

### Escribir consultas SQL {#write-sql-queries}

Operator puede ayudarte a escribir SQL para [extensiones de segmento](#campaigns-and-audiences) y para [plantillas de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) del Query Builder. Describe la consulta que deseas en lenguaje natural, y Operator genera el SQL para que lo revises antes de ejecutarlo.

### Generar código de transformación de datos {#generate-data-transformation-code}

En el editor de [transformación de datos]({{site.baseurl}}/user_guide/data/unification/data_transformation), selecciona **Insert Code** para generar código de transformación que convierte una carga útil de webhook entrante en solicitudes válidas de la API de Braze. Para instrucciones paso a paso sobre cómo crear una transformación, consulta [Crear una transformación]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation).

## Configuración del espacio de trabajo {#workspace-settings}

Operator puede revisar y actualizar la configuración en varias páginas de configuración del espacio de trabajo. Describe el cambio que deseas y Operator lo propone como una tarjeta de acción que revisas antes de guardarlo. Las páginas de configuración compatibles incluyen, entre otras:

- [Horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)
- [Configuración de push]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings)
- [Límites de velocidad de mensajería]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits)
- [Flujos de trabajo de aprobación]({{site.baseurl}}/user_guide/messaging/governance/approvals), incluyendo [reglas de mensajería]({{site.baseurl}}/user_guide/messaging/governance/approvals/messaging_rules) y aprobación permanente
- [API e identificadores]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers), incluyendo [otros identificadores]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers#other-identifiers) y límites de API
- [Información de contacto de configuración de administrador]({{site.baseurl}}/user_guide/administer/global/admin_settings/contact_information)

{% alert note %}
La cobertura de Operator sobre las páginas de configuración se amplía regularmente. **Pregunta directamente a Operator** para obtener la respuesta más actualizada sobre lo que puede configurar.
{% endalert %}

## Limitaciones {#limitations}

{% alert note %}
La cobertura de Operator cambia con frecuencia. Si no estás seguro de si una pantalla o flujo de trabajo específico es compatible, pregunta directamente a Operator.
{% endalert %}

El soporte de Operator en el panel es amplio, pero tiene límites.

- **Canvas:** Operator no puede crear ni editar [Canvas]({{site.baseurl}}/user_guide/messaging/canvas), pero puede consultar la configuración de un Canvas existente, como la segmentación y la configuración de entrega, para responder preguntas y fundamentar su resultado.
- **Duplicación de Campaigns:** Operator no puede duplicar una Campaign existente desde la vista de lista de Campaigns. Para crear una Campaign similar, pide a Operator que cree una nueva desde cero, o duplica la Campaign manualmente desde el menú **Más acciones** de la vista de lista.
- **Editores de arrastrar y soltar:** Operator no puede generar ni insertar un diseño de mensaje directamente en un editor de arrastrar y soltar, como los de [correo electrónico]({{site.baseurl}}/user_guide/channels/email/drag_and_drop), [Banners]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner) y [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop). Cambia al editor HTML correspondiente para usar Operator, o pide a Operator que genere contenido, como texto, que puedas pegar manualmente. Consulta [Generar mensajes](#generate-messages) para ver los canales y editores compatibles.
- **Visibilidad de pantalla:** Operator utiliza contexto consciente de la página para comprender lo que estás viendo, incluido el contenido dentro de vistas previas y editores compatibles. Cuando parte de una página queda fuera de lo que Operator puede leer, te lo indica en lugar de adivinar, para que sepas que debes describir ese contenido tú mismo.
- **Límites de uso:** Operator tiene un límite de uso diario a nivel de empresa que se restablece cada 24 horas. Las generaciones de imágenes cuentan para este límite. Si se alcanza el límite, aparece un mensaje de "Límite de uso diario excedido" y no se pueden realizar más solicitudes hasta que se restablezca. Para pasos de solución de problemas, consulta [Solución de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting).

## Asistentes anteriores {#legacy-assistants}

Antes de Operator, varias funciones de IA existían como asistentes independientes: el AI Copywriter, el AI Liquid Assistant, el AI Image Generator, el AI SQL Generator, el Data Transformations AI Copilot y la revisión de contenido. Todos sus puntos de entrada permanecen en su lugar y redirigen a Operator, por lo que tus flujos de trabajo existentes no se ven afectados. Para saber qué hacen hoy, consulta [Contenido y creatividad](#content-and-creative) y [Automatización de datos y búsqueda](#data-automation-and-lookup).

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Privacidad y seguridad de datos {#data-privacy-and-security}

Operator se integra con OpenAI para generar resultados. Para más información sobre qué información envía Braze a OpenAI, cómo se utilizan esos datos y tus derechos de propiedad intelectual, consulta [Cómo se utilizan los datos con OpenAI]({{site.baseurl}}/user_guide/brazeai/operator#data-privacy-and-security).

## Próximos pasos {#next-steps}

- [Comenzar con Operator]({{site.baseurl}}/user_guide/brazeai/operator): accede y usa Operator
- [Biblioteca de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library): explora prompts de ejemplo listos para usar
- [Revisar acciones]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): revisa y aprueba los cambios propuestos por Operator
- [Solución de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): consulta problemas comunes y soluciones