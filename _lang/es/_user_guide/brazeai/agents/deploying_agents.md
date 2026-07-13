---
nav_title: Implementar agentes
article_title: Implementar agentes personalizados
description: "Aprende a utilizar los agentes personalizados en Braze después de crearlos."
alias: /deploying-agents/
page_order: 2
---

# Implementar agentes personalizados {#deploy-custom-agents}

> Después de [crear un agente]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents), utiliza esta página para saber dónde y cómo implementarlo en Braze. El tipo de agente que elijas en el momento de la creación —agente de Canvas o agente de catálogo— determina dónde puede ejecutarse el agente. Para obtener una introducción, consulta [Agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents).

## Tipos de agentes personalizados {#types-of-custom-agents}

Los agentes personalizados se implementan en diferentes partes de Braze según su tipo. Utiliza la tabla siguiente para encontrar la ruta de implementación adecuada para tu agente.

| Tipo de agente | Se implementa en | Se ejecuta cuando | Sección |
| --- | --- | --- | --- |
| Agente de paso en Canvas | [Paso Agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) en Canvas | Un usuario entra en el paso | [Usar agentes de paso en Canvas](#use-canvas-step-agents) |
| Agente de catálogo | Campo de catálogo | Se crea o actualiza una fila del catálogo | [Usar agentes de catálogo](#use-catalog-agents) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de agentes personalizados" }

Seleccionas el tipo de agente en **Agent Console** cuando creas el agente. Para conocer los pasos de configuración, consulta [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-1-choose-an-agent-type).

## Buenas prácticas {#best-practices}

Apunta a casos de uso de alto valor en los que los agentes puedan generar el mayor retorno de la inversión (ROI), y elige audiencias con probabilidades de responder. Una audiencia más pequeña y con grandes oportunidades suele superar a una audiencia grande con pocas oportunidades.

Para los agentes de Canvas, empieza con usuarios que tengan señales fuertes —como búsquedas recientes, alta participación o datos de perfil enriquecidos— antes de expandirte a segmentos más amplios. Para los agentes de catálogo, prioriza las filas en las que las columnas de entrada que necesitas ya estén rellenadas, de modo que cada invocación tenga suficiente contexto para producir resultados útiles.

Para probar el ROI a pequeña escala antes de desplegar un agente de forma amplia, utiliza un paso de [Recorridos de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que solo una parte de tu audiencia entre en la rama que contiene tu paso Agente.

## Usar agentes de paso en Canvas {#use-canvas-step-agents}

Después de crear un agente de Canvas, añádelo a un Canvas como paso Agente para personalizar mensajes u orientar la toma de decisiones en tiempo real.

### Cómo funciona {#how-it-works}

Cuando un usuario llega a un paso Agente en un Canvas, Braze envía los datos de entrada que configuraste a tu agente. El agente procesa la entrada utilizando su modelo e instrucciones, y luego devuelve un resultado almacenado en la variable de salida que definiste en el paso. Puedes utilizar esa salida para la toma de decisiones, la personalización o el procesamiento posterior.

Los pasos Agente utilizan [variables de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) para incorporar el contexto relevante y generar una variable que puede utilizarse en el Canvas. Para conocer los requisitos previos y una referencia completa, consulta [Paso Agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

### Añadir un paso Agente {#add-an-agent-step}

Para añadir un agente a tu Canvas:

1. Arrastra y suelta el componente **Agente** desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> en la parte inferior de un paso y selecciona **Agente**.
2. Selecciona el agente que procesará los datos en este paso.
3. Define el nombre de la variable de salida. El tipo de datos de salida se configura en [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents).
4. (Opcional) Añade valores de contexto adicionales para que el agente los consulte cuando se ejecute. Esto puede incluir variables Liquid adicionales o contexto de Canvas que no hayas vinculado previamente en la configuración del agente, por ejemplo, valores que solo quieras pasar en el momento del envío desde este paso.
5. Prueba y previsualiza la salida del agente en la vista previa del paso.

Para conocer los tipos de datos de salida, la creación de plantillas con Liquid y las capturas de pantalla, consulta [Paso Agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

### Ejemplos {#use-cases}

| Caso de uso | Descripción |
| --- | --- |
| Puntuación y calificación de clientes potenciales | Utiliza un paso Agente para evaluar los clientes potenciales entrantes en una escala (por ejemplo, del 1 al 10). Dirige a los usuarios con una puntuación superior a un umbral a rutas de captación, mientras descartas a los clientes potenciales menos adecuados. |
| Personalización dinámica de mensajes | Haz que un agente genere líneas del asunto, recomendaciones de productos o textos de mensajes basados en los atributos de los usuarios o en sus comportamientos recientes. La respuesta se puede insertar directamente en un paso de mensaje. |
| Gestión de los comentarios de los clientes | Transmite los comentarios de los clientes a un agente para analizar el sentimiento y generar mensajes de seguimiento empáticos. Para los usuarios de alto valor, el agente podría escalar la respuesta o incluir ventajas adicionales. |
| Enrutamiento inteligente | Utiliza los resultados del agente (booleanos o numéricos) para dividir a los usuarios en diferentes rutas de Canvas. Por ejemplo, clasifica a los usuarios como «en riesgo» o «sanos» y ajusta la frecuencia de la mensajería en consecuencia. |
| Interpretación de cuestionarios o respuestas | Deja que un agente analice las respuestas abiertas de los cuestionarios o los campos de texto libre, y devuelva valores estructurados (por ejemplo, categorizando la intención o la necesidad) que impulsen las rutas posteriores. |
| Razonamiento en varios pasos | Configura un agente para combinar campos de contexto y tomar decisiones complejas, como recomendar la siguiente mejor acción (correo electrónico, SMS o contacto humano) en función de múltiples atributos del usuario. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplos" }

### Usar la salida del agente {#use-the-agent-output}

Después de que el agente se ejecute, utiliza la variable de salida en tu Canvas:

- **Enrutamiento del recorrido:** Dirige a los usuarios por diferentes rutas de Canvas en función de la respuesta del agente. Utiliza [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) o [División de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) con salidas numéricas, booleanas o estructuradas.
- **Personalización:** Inserta la respuesta del agente directamente en un paso de mensaje utilizando Liquid.
- **Procesamiento de datos de usuario:** Analiza y estandariza los datos de usuario, y luego almacénalos en el perfil de usuario (por ejemplo, con un paso de [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)) o envíalos mediante un webhook.

Para ver ejemplos, consulta [Cómo funciona]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#how-it-works) en Paso Agente.

### Gestión de errores y comportamiento alternativo {#fallback-behavior}

Lo siguiente se aplica a los **agentes de paso en Canvas** en un [paso Agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

- Si el modelo conectado devuelve un [error de límite de velocidad]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) del proveedor del LLM, Braze reintenta continuamente la solicitud utilizando retirada exponencial hasta que la llamada se complete correctamente o Braze determine que no puede completarse; a continuación, los usuarios avanzan al siguiente paso en Canvas.
- Para otros fallos (como un tiempo de espera agotado o una clave de API no válida), la variable de salida se establece en `null` a menos que el agente tenga [valores alternativos configurados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) en Agent Console.
- Si un agente alcanza su límite de invocaciones diarias, Braze también aplica los valores alternativos configurados cuando están presentes; de lo contrario, la variable de salida se establece en `null`.

Cuando se configuran valores alternativos, Braze los aplica para errores no reintentables y para fallos por límite diario. Braze renderiza la alternativa con Liquid por usuario y almacena el resultado en la variable de salida del paso Agente. Sin valores alternativos, esos fallos establecen la variable de salida en `null`. Si prefieres configurar valores predeterminados específicos del paso en los pasos de mensaje en lugar de las alternativas de Agent Console, puedes utilizar [valores predeterminados de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) en pasos posteriores. Para ello, deja las alternativas en blanco en la sección **Output** de la configuración del agente para que los valores predeterminados de Liquid puedan aplicarse cuando el agente devuelva null.

- Las respuestas se almacenan en caché para entradas idénticas y pueden reutilizarse para invocaciones idénticas repetidas en unos pocos minutos. Las respuestas en caché siguen contando para el total de invocaciones y las invocaciones diarias.
- Los pasos Agente pueden tardar en procesar un lote grande de usuarios. Braze pone en cola las invocaciones según los [controles de flujo de invocaciones]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls), por lo que los usuarios pueden permanecer pendientes durante envíos de alto volumen.

Para conocer la configuración del paso Agente y los detalles del tiempo de ejecución, consulta [Gestión de errores]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#error-handling) en Paso Agente. Para más detalles, consulta [Gestión de errores]({{site.baseurl}}/user_guide/brazeai/agents#error-handling) en Agentes de Braze.

## Usar agentes de catálogo {#use-catalog-agents}

Después de crear un agente de catálogo, aplícalo a un campo de catálogo para generar o calcular automáticamente los valores de cada fila. El agente también se ejecuta en las nuevas filas que se añadan al catálogo en el futuro.

### Cómo funciona

Tras su inicio, el agente se ejecuta y evalúa cada fila, tomando las columnas seleccionadas en su contexto para generar un resultado. Los agentes se ejecutan en todas las filas nuevas añadidas después de implementar el agente. Si seleccionaste **Recalculate when catalog rows update**, todos los valores de este campo se actualizarán si cambian los campos de origen existentes.

Cuando configuras las columnas de entrada para un agente de catálogo, habilita el control del producto que marca qué columnas seleccionadas son **obligatorias para la ejecución** antes de que el agente se invoque (las etiquetas pueden variar ligeramente según el espacio de trabajo). Con ese control habilitado, elige el subconjunto de columnas que deben contener valores: las columnas seleccionadas comienzan como obligatorias de forma predeterminada, pero puedes quitar las columnas que pueden estar vacías sin bloquear al agente. El agente omite una fila solo cuando una columna que dejaste como obligatoria está en blanco o falta, por ejemplo, un campo `gender` que no se ha rellenado. Ejecutar sin el contexto obligatorio desperdicia tokens y puede producir resultados de baja calidad.

Los agentes de catálogo también respetan las dependencias entre columnas. Si la columna D se genera a partir de las columnas B y C, el agente no se ejecuta en la columna D para una fila hasta que B y C contengan valores para esa fila.

Puedes actualizar y editar los campos de tu catálogo que utilizan agentes. Para eliminar un agente de una columna, desmarca **Apply AI agent**. Esto revierte la columna a una columna no agéntica, y los campos conservan los últimos valores que el agente aplicó la última vez que se ejecutó en el catálogo.

Las referencias circulares en los catálogos no son compatibles, lo que significa que no puede darse la siguiente situación:

- La columna agéntica 1 utiliza la columna agéntica 2 como entrada
- La columna agéntica 2 utiliza la columna agéntica 1 como entrada

### Añadir un agente a un campo de catálogo {#add-an-agent-to-a-catalog-field}

![Un paso Agente en un campo de catálogo.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Para añadir un agente al campo de tu catálogo:

1. En tu catálogo, añade un nuevo campo.
2. Selecciona **Apply AI agent**.
3. Asigna un agente a este campo.
4. Selecciona las columnas que deben pasarse como entrada. Si no se selecciona ninguna, el agente tendrá acceso a todas las columnas del catálogo.
5. (Opcional) Habilita **Only run when required columns have values** para omitir las filas en las que una o más columnas de entrada seleccionadas estén vacías. Cuando esta opción está activada, selecciona cuáles de las columnas de entrada deben estar rellenadas para que el agente se ejecute: todas las columnas seleccionadas comienzan como obligatorias de forma predeterminada, pero puedes quitar las que pueden estar vacías sin bloquear la ejecución.
6. Decide si el agente debe volver a calcular los campos cuando se actualicen las filas del catálogo. Si no seleccionas esta opción, el agente solo se ejecutará una vez por fila.
7. Selecciona **Add fields** para implementar el agente y revisar las estimaciones de costes. El modal **Cost estimation** muestra cuántas veces se ejecutará el agente en este catálogo, lo que equivale aproximadamente al número total de filas. Para continuar, selecciona **Confirm**.

### Buenas prácticas para agentes de catálogo {#catalog-agent-best-practices}

Planifica qué columnas necesita el agente antes de aplicarlo a un campo de catálogo. Después de habilitar los controles de entrada obligatoria para el campo, selecciona las columnas que contienen los datos que tu agente debe leer y luego desmarca cualquier columna que pueda permanecer vacía sin bloquear la ejecución. El agente omite una fila solo cuando una columna que dejaste marcada como obligatoria está en blanco.

No dejes una columna marcada como obligatoria si esperas que permanezca vacía para algunas filas y aun así quieres que el agente se ejecute; quítala del conjunto de obligatorias. Omitir las filas incompletas evita el uso incorrecto de tokens y mantiene alta la calidad de los resultados.

| Escenario | Qué sucede |
| --- | --- |
| Filas prerrellenadas con marcadores de posición | Si añades filas al catálogo con solo un ID y un nombre de fondo, y luego rellenas otras columnas más tarde, el agente omite esas filas hasta que las columnas de entrada obligatorias tengan valores. |
| Agente aplicado después de que existan filas | Cuando aplicas un agente a un campo en un catálogo que ya tiene filas, el agente evalúa cada fila pero solo se ejecuta donde las columnas de entrada obligatorias estén rellenadas. |
| Catálogo parcialmente completo | Por ejemplo, un catálogo con 100 filas donde `leader` está rellenado para las entradas de 2026 pero otras filas contienen solo un ID y un nombre de fondo con campos vacíos en otros lugares. El agente se ejecuta en las filas con un valor de `leader` y omite las filas sin él cuando `leader` sigue siendo obligatorio. |
| Columnas dependientes | Si la columna 3 depende de las columnas 1 y 2, el agente no escribe en la columna 3 hasta que las columnas 1 y 2 tengan valores para esa fila. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Buenas prácticas para agentes de catálogo" }

### Ejemplos

| Caso de uso | Descripción |
| --- | --- |
| Generar descripciones de productos | Crea automáticamente textos de marketing breves para las nuevas entradas del catálogo, por ejemplo, generando una descripción atractiva a partir de datos estructurados del producto, como el nombre, la categoría y las características. |
| Enriquecer atributos del producto | Rellena los valores que falten, como la familia de colores, el estilo o la temporada, basándote en el nombre y los detalles del producto. Por ejemplo, si el nombre de un producto es «Gafas de sol polarizadas Laguna», el agente podría asignar el estilo como «deportivo» y la familia de colores como «azul». |
| Calcular campos derivados | Utiliza los campos existentes para generar nuevos datos, como una «puntuación de adecuación» basada en atributos o una «etiqueta de popularidad» a partir de las ventas y el número de reseñas. |
| Clasificar o etiquetar elementos | Asigna etiquetas para la lógica de recomendación, de modo que los modelos de personalización puedan segmentar productos de forma más eficaz. Por ejemplo, etiqueta los productos como «para exterior», «para festivales» o «premium». |
| Localizar contenido | Traduce el texto del catálogo a otro idioma para campañas globales o ajusta el tono y la longitud para canales específicos de cada región. Por ejemplo, traduce «Classic Clubmaster Sunglasses» al español como «Gafas de sol Classic Clubmaster» o acorta las descripciones para las campañas de SMS. |
| Resumir reseñas o comentarios | Resume las opiniones o comentarios en un nuevo campo, por ejemplo, asignando puntuaciones de sentimiento como Positivo, Neutro o Negativo, o creando un breve resumen de texto como «La mayoría de los clientes mencionan que el producto se ajusta muy bien, pero señalan que el envío es lento». |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplos" }

### Definir campos de respuesta {#define-response-fields}

Si tu agente utiliza [campos]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents?tab=fields#advanced-schemas) como formato de salida, puedes seleccionar el campo correspondiente del agente en **Response Field** para utilizarlo en el campo del catálogo.

Supongamos que tienes un agente que añade descripciones de productos a un catálogo con los siguientes campos para estructurar el formato de salida:

| Nombre del campo | Valor |
| --- | --- |
| **description** | Texto |
| **confidence_score_out_of_ten** | Número |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definir campos de respuesta" }

Puedes añadir un campo llamado **product_description** a un catálogo y seleccionar **description** como **Response Field** para rellenar la columna con las descripciones del agente.

![Un campo «product_description» con el agente «Descriptor» aplicado. La salida «description» se selecciona como campo de respuesta.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

También puedes anular manualmente la celda generada por el agente seleccionando **Edit Item** y actualizando la descripción generada por el agente con tus modificaciones. Para volver a la descripción generada por el agente, selecciona el símbolo de actualización en la celda.

### Gestión de errores {#error-handling}

- Las invocaciones de catálogo fallidas no se reintentan, incluidos los [errores de límite de velocidad]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) del proveedor del LLM.
- Si la llamada a la API del proveedor del modelo fundacional devuelve algún otro error, como un error de clave de API no válida, el valor del campo no se actualiza. Los agentes de catálogo no admiten la configuración de valores alternativos en Agent Console.
- Puedes revisar los registros del agente para obtener detalles sobre las ejecuciones fallidas.
- Los agentes de catálogo solo pueden procesar valores de entrada de hasta 25 KB por fila.

## Supervisa tu agente {#monitor-your-agent}

La supervisión funciona de la misma manera independientemente de si tu agente se ejecuta en Canvas o en catálogos.

En la sección **Usage** de tu agente, puedes consultar y navegar hasta los lugares en los que el agente se utiliza activamente en catálogos y Canvas.

![Sección de uso del agente que muestra dos agentes activos y un agente inactivo para Canvas.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

En la sección **Logs** de tu agente, puedes supervisar las llamadas reales de los agentes que se producen en tus Canvas y catálogos. Puedes filtrar por información como el intervalo de fechas, el resultado (correcto o fallido) o la ubicación de la llamada. También puedes seleccionar **Export CSV** para exportar solo los registros que se muestran en la página actual.

{% alert tip %}
También puedes supervisar los errores de límite de invocaciones diarias en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log).
{% endalert %}

![Registros para la puntuación de sentimiento de IA de un agente.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

Selecciona **View** para una llamada de agente específica y verás la entrada, la salida y el ID de usuario.

![El panel de detalles de un agente de asignación deportiva aleatoria que muestra la solicitud de entrada, la respuesta de salida y un ID de usuario asociado.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

### Usar Currents {#use-currents}

También puedes utilizar estos eventos de Currents para acceder a los esquemas de registros de Kafka:

- Eventos ejecutados por el agente
- Eventos de invocación de herramientas

Consulta el [glosario de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) para obtener más detalles.

## Artículos relacionados {#related-articles}

- [Paso Agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step)
- [Referencia para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference)
- [Preguntas frecuentes]({{site.baseurl}}/user_guide/brazeai/agents/faq)