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

Los agentes personalizados se despliegan en diferentes partes de Braze según su tipo. Utiliza la siguiente tabla para encontrar la ruta de despliegue adecuada para tu agente.

| Tipo de agente | Se despliega en | Se ejecuta cuando | Sección |
| --- | --- | --- | --- |
| Agente de paso en Canvas | [Paso de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) en Canvas | Un usuario entra en el paso | [Usar agentes de paso en Canvas](#use-canvas-step-agents) |
| Agente de catálogo | Campo de catálogo | Se crea o actualiza una fila de catálogo | [Usar agentes de catálogo](#use-catalog-agents) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de agentes personalizados" }

Seleccionas el tipo de agente en **Agent Console** cuando creas el agente. Para los pasos de configuración, consulta [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-1-choose-an-agent-type).

## Buenas prácticas {#best-practices}

Apunta a casos de uso de alto valor donde los agentes puedan generar el mayor retorno de la inversión (ROI) y elige audiencias con probabilidad de responder. Una audiencia más pequeña y con alta oportunidad a menudo supera a una audiencia grande con baja oportunidad.

Para los agentes de paso en Canvas, comienza con usuarios que tengan señales fuertes, como búsquedas recientes, alta participación o datos de perfil enriquecidos, antes de expandirte a Segments más amplios. Para los agentes de catálogo, prioriza las filas donde las columnas de entrada que necesitas ya estén completadas, de modo que cada invocación tenga suficiente contexto para producir resultados útiles.

Para probar el ROI a pequeña escala antes de implementar un agente de forma amplia, usa un paso de [recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que solo una parte de tu audiencia entre en la rama que contiene tu paso de agente.

### Escalar después de una prueba exitosa {#scale-after-a-successful-test}

Después de que una prueba a pequeña escala (por ejemplo, una rama de [recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)) muestre calidad y ROI aceptables, planifica implementar el agente para toda tu audiencia objetivo (no solo el grupo de prueba) para que cada usuario elegible se beneficie.

Antes de escalar, ten en cuenta lo siguiente:

- Aumenta el límite diario de invocaciones del agente en Agent Console para que pueda manejar el volumen completo de tu audiencia. El valor predeterminado es 250 000; puedes aumentarlo hasta 1 000 000 (o más con tu administrador de éxito de cliente). Consulta [Límites diarios de invocaciones y créditos]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).
- Revisa la estimación del **Límite de costo de créditos de acción diaria** y confirma que tu espacio de trabajo tiene suficientes créditos para envíos a escala completa.
- Elimina o reconfigura el experimento para que toda la audiencia objetivo entre en el paso de agente (o promueve la variante ganadora a la ruta principal).

Escalar a la audiencia completa aumenta el consumo de créditos proporcionalmente. Monitorea el uso en **Configuración** > **Facturación** > **Uso de créditos** > **Agent Console** después del lanzamiento.

## Usar agentes de paso en Canvas {#use-canvas-step-agents}

Después de crear un agente de paso en Canvas, agrégalo a un Canvas como un paso de agente para personalizar mensajes o guiar la toma de decisiones en tiempo real.

### Cómo funciona {#how-it-works}

Cuando un usuario llega a un paso de agente en un Canvas, Braze envía los datos de entrada que configuraste a tu agente. El agente procesa la entrada usando su modelo e instrucciones, y luego devuelve una salida almacenada en la variable de salida que definiste en el paso. Puedes usar esa salida para la toma de decisiones, personalización o procesamiento posterior.

Los pasos de agente usan [variables de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) para ingerir contexto relevante y generar una variable que se puede usar en el Canvas. Para los requisitos previos y una referencia completa, consulta [Paso de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

### Agregar un paso de agente {#add-an-agent-step}

Para agregar un agente a tu Canvas:

1. Arrastra y suelta el componente **Agente** desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> de suma en la parte inferior de un paso y selecciona **Agente**.
2. Selecciona el agente que procesa los datos en este paso.
3. Define el nombre de la variable de salida. El tipo de datos de salida se configura en la [Consola de agentes]({{site.baseurl}}/user_guide/brazeai/agents).
4. (Opcional) Agrega valores de contexto adicionales para que el agente los consulte cuando se ejecute. Esto puede incluir variables Liquid adicionales o contexto de Canvas que no hayas vinculado previamente en la configuración del agente; por ejemplo, valores que solo quieras pasar en el momento del envío desde este paso.
5. Prueba el agente usando la vista previa del paso o [Probar Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths#agent-steps) para recorrer la ruta completa del usuario.

Para tipos de datos de salida, plantillas Liquid y capturas de pantalla, consulta [Paso de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

### Ejemplos {#use-cases}

| Ejemplo | Descripción |
| --- | --- |
| Puntuación y calificación de prospectos | Usa un paso de agente para evaluar prospectos entrantes en una escala (por ejemplo, 1-10). Dirige a los usuarios con una puntuación superior a un umbral hacia recorridos de nutrición, mientras descalificas a los prospectos de bajo ajuste. |
| Personalización dinámica de mensajes | Haz que un agente genere líneas del asunto, recomendaciones de productos o texto de mensajes basándose en atributos de usuario o comportamientos recientes. La respuesta se puede insertar directamente en un paso de mensaje. |
| Gestión de comentarios de clientes | Pasa los comentarios de los clientes a un agente para analizar el sentimiento y generar mensajes de seguimiento empáticos. Para usuarios de alto valor, el agente podría escalar la respuesta o incluir beneficios. |
| Enrutamiento inteligente | Usa las salidas del agente (booleanas o numéricas) para dividir a los usuarios en diferentes rutas de Canvas. Por ejemplo, clasifica a los usuarios como "en riesgo" o "saludables" y ajusta la cadencia de mensajería en consecuencia. |
| Interpretación de cuestionarios o respuestas | Permite que un agente analice respuestas abiertas de cuestionarios o campos de texto libre, devolviendo valores estructurados (por ejemplo, categorizando la intención o necesidad) que impulsen recorridos posteriores. |
| Razonamiento de múltiples pasos | Configura un agente para combinar campos de contexto y tomar decisiones complejas, como recomendar la siguiente mejor acción (correo electrónico, SMS o contacto humano) basándose en múltiples atributos de usuario. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplos" }

### Usar la salida del agente {#use-the-agent-output}

Después de que el agente se ejecute, usa la variable de salida en tu Canvas:

- **Enrutamiento del recorrido:** Dirige a los usuarios por diferentes rutas de Canvas según la respuesta del agente. Usa [rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) o [divisiones de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) con salidas numéricas, booleanas o estructuradas.
- **Personalización:** Inserta la respuesta del agente directamente en un paso de mensaje usando Liquid.
- **Procesamiento de datos de usuario:** Analiza y estandariza los datos de usuario, luego almacénalos en el perfil de usuario (por ejemplo, con un paso de [actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)) o envíalos usando un webhook.

Para ver ejemplos, consulta [Cómo funciona]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#how-it-works) en Paso de agente.

### Gestión de errores y comportamiento alternativo {#fallback-behavior}

Lo siguiente se aplica a los agentes de paso en Canvas en un [paso de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

- Si el modelo conectado devuelve un [error de límite de velocidad]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) del proveedor de LLM, Braze reintenta continuamente la solicitud usando retirada exponencial hasta que la llamada tenga éxito o Braze determine que no se puede completar; luego los usuarios avanzan al siguiente paso en Canvas.
- Para otros fallos (como un tiempo de espera agotado o una clave de API no válida), la variable de salida se establece en `null` a menos que el agente tenga [valores alternativos configurados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) en la Consola de agentes.
- Si un agente alcanza su límite diario de invocaciones, Braze también aplica los valores alternativos configurados cuando están presentes; de lo contrario, la variable de salida se establece en `null`.

Cuando se configuran valores alternativos, Braze los aplica para errores no reintentables y para fallos por límite diario. Braze renderiza el valor alternativo con Liquid por usuario y almacena el resultado en la variable de salida del paso de agente. Sin valores alternativos, esos fallos establecen la variable de salida en `null`. Si prefieres configurar valores predeterminados específicos del paso en los pasos de mensaje en lugar de valores alternativos en la Consola de agentes, puedes usar [valores predeterminados de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) en pasos posteriores. Para hacerlo, deja los valores alternativos en blanco en la sección **Salida** de la configuración del agente para que los valores predeterminados de Liquid se apliquen cuando el agente devuelva null.

Los errores de límite de velocidad, la indisponibilidad del modelo y los fallos por límite diario de invocaciones no consumen créditos de Braze. Los tiempos de espera agotados sí consumen créditos. Consulta [Cuándo se consumen los créditos]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).

- Las respuestas se almacenan en caché para entradas idénticas y pueden reutilizarse para invocaciones idénticas repetidas en unos pocos minutos. Las respuestas en caché aún cuentan para el total de invocaciones y las invocaciones diarias.
- Los pasos de agente pueden tardar en procesar un lote grande de usuarios. Braze pone en cola las invocaciones según los [controles de flujo de invocaciones]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls), por lo que los usuarios pueden permanecer pendientes durante envíos de alto volumen.

Para la configuración del paso de agente y los detalles de ejecución, consulta [Gestión de errores]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#error-handling) en Paso de agente. Para más detalles, consulta [Gestión de errores]({{site.baseurl}}/user_guide/brazeai/agents#error-handling) en Braze Agents.

## Uso de Catalog Agents {#use-catalog-agents}

Después de crear un Catalog Agent, aplícalo a un campo de catálogo para generar o calcular automáticamente valores para cada fila. El agente también se ejecuta en las nuevas filas que se añadan al catálogo en el futuro.

### Cómo funciona

Después del lanzamiento, el agente se ejecuta y evalúa cada fila, tomando las columnas seleccionadas en su contexto para producir una salida. Los agentes se ejecutan en todas las filas nuevas añadidas después de desplegar el agente. Si seleccionaste **Recalcular cuando se actualicen las filas del catálogo**, todos los valores de este campo se actualizan si cambian los campos de origen existentes.

Cuando configuras las columnas de entrada para un Catalog Agent, habilita el control del producto que marca qué columnas seleccionadas son obligatorias antes de que el agente se invoque (las etiquetas pueden variar ligeramente según el espacio de trabajo). Con ese control habilitado, elige el subconjunto de columnas que deben contener valores: las columnas seleccionadas comienzan como obligatorias de forma predeterminada, pero puedes eliminar columnas que pueden estar vacías sin bloquear al agente. El agente omite una fila solo cuando una columna que dejaste como obligatoria está en blanco o falta; por ejemplo, un campo `gender` que no se ha rellenado. Ejecutar sin el contexto obligatorio desperdicia tokens y puede producir resultados de baja calidad.

Los Catalog Agents también respetan las dependencias entre columnas. Si la columna D se genera a partir de las columnas B y C, el agente no se ejecuta en la columna D para una fila hasta que B y C contengan valores para esa fila.

Puedes actualizar y editar los campos de tu catálogo que usan agentes. Para eliminar un agente de una columna, deselecciona **Apply AI agent**. Esto revierte la columna a una columna no agéntica, y los campos conservan los últimos valores que el agente aplicó la última vez que se ejecutó en el catálogo.

Las referencias circulares en catálogos no son compatibles, lo que significa que el siguiente escenario no puede ocurrir:

- La columna agéntica 1 usa la columna agéntica 2 como entrada
- La columna agéntica 2 usa la columna agéntica 1 como entrada

### Añadir un agente a un campo de catálogo {#add-an-agent-to-a-catalog-field}

![Un paso de agente en un campo de catálogo.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Para añadir un agente a tu campo de catálogo:

1. En tu catálogo, añade un nuevo campo.
2. Selecciona **Apply AI agent**.
3. Asigna un agente a este campo.
4. Selecciona qué columnas deben pasarse como entrada. Si no se selecciona ninguna, el agente tiene acceso a todas las columnas del catálogo.
5. (Opcional) Habilita **Only run when required columns have values** para omitir filas en las que una o más columnas de entrada seleccionadas estén en blanco. Cuando esta opción está activada, selecciona cuáles de las columnas de entrada deben estar rellenadas para que el agente se ejecute: todas las columnas seleccionadas comienzan como obligatorias de forma predeterminada, pero puedes eliminar cualquiera que pueda estar vacía sin bloquear una ejecución.
6. Decide si el agente debe recalcular los campos cuando se actualicen las filas del catálogo. Si no seleccionas esta opción, el agente se ejecuta solo una vez por fila.
7. Selecciona **Add fields** para desplegar el agente y revisar las estimaciones de costos. El modal **Cost estimation** muestra cuántas veces se ejecutará el agente en este catálogo, aproximadamente igual al número total de filas. Para continuar, selecciona **Confirm**.

### Mejores prácticas de Catalog Agent {#catalog-agent-best-practices}

Planifica qué columnas necesita el agente antes de aplicarlo a un campo de catálogo. Después de habilitar los controles de entrada obligatoria para el campo, selecciona las columnas que contienen los datos que tu agente debe leer y luego desmarca cualquier columna que pueda permanecer vacía sin bloquear una ejecución. El agente omite una fila solo cuando una columna que dejaste marcada como obligatoria está en blanco.

No dejes una columna marcada como obligatoria si esperas que permanezca vacía para algunas filas y aún quieres que el agente se ejecute; en su lugar, elimínala del conjunto de obligatorias. Omitir filas incompletas evita el uso incorrecto de tokens y mantiene alta la calidad de la salida.

| Escenario | Qué sucede |
| --- | --- |
| Filas prerrellenadas con marcadores de posición | Si añades filas de catálogo con solo un ID y un nombre de fondo, y luego rellenas otras columnas más tarde, el agente omite esas filas hasta que las columnas de entrada obligatorias tengan valores. |
| Agente aplicado después de que existan filas | Cuando aplicas un agente a un campo en un catálogo que ya tiene filas, el agente evalúa cada fila pero solo se ejecuta donde las columnas de entrada obligatorias estén rellenadas. |
| Catálogo parcialmente completo | Por ejemplo, un catálogo con 100 filas donde `leader` está rellenado para las entradas de 2026 pero otras filas contienen solo un ID y nombre de fondo con campos en blanco en otros lugares. El agente se ejecuta en las filas con un valor de `leader` y omite las filas sin él cuando `leader` permanece como obligatorio. |
| Columnas dependientes | Si la columna 3 depende de las columnas 1 y 2, el agente no escribe en la columna 3 hasta que las columnas 1 y 2 tengan valores para esa fila. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mejores prácticas de Catalog Agent" }

### Ejemplos

| Ejemplo | Descripción |
| --- | --- |
| Generar descripciones de productos | Crea automáticamente textos de marketing breves para nuevas entradas de catálogo, por ejemplo, generando una descripción atractiva a partir de datos estructurados del producto como nombre, categoría y características. |
| Enriquecer atributos de productos | Rellena valores faltantes como familia de color, estilo o temporada basándose en el nombre y los detalles del producto. Por ejemplo, si el nombre de un producto es "Laguna Polarized Sunglasses", el agente podría asignar el estilo como "sport" y la familia de color como "blue". |
| Calcular campos derivados | Usa campos existentes para generar nuevos datos, como una "puntuación de ajuste" basada en atributos o una "etiqueta de popularidad" a partir de ventas y recuentos de reseñas. |
| Categorizar o etiquetar artículos | Asigna etiquetas para la lógica de recomendación de modo que los modelos de personalización puedan segmentar productos de manera más efectiva. Por ejemplo, etiquetar productos como "outdoor", "festival-ready" o "premium". |
| Localizar contenido | Traduce el texto del catálogo a otro idioma para campañas globales, o ajusta el tono y la longitud para canales específicos de cada región. Por ejemplo, traducir "Classic Clubmaster Sunglasses" al español como "Gafas de sol Classic Clubmaster", o acortar descripciones para campañas de SMS. |
| Resumir reseñas o comentarios | Resume el sentimiento o los comentarios en un nuevo campo, como asignar puntuaciones de sentimiento como Positivo, Neutro o Negativo, o crear un breve resumen de texto como "La mayoría de los clientes mencionan un gran ajuste, pero señalan envíos lentos". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplos" }

### Definir campos de respuesta {#define-response-fields}

Si tu agente usa [campos]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents?tab=fields#advanced-schemas) como formato de salida, puedes seleccionar el campo correspondiente del agente para **Response Field** y usarlo en el campo del catálogo.

Supongamos que tienes un agente que añade descripciones de productos a un catálogo con los siguientes campos para estructurar el formato de salida:

| Nombre del campo | Valor |
| --- | --- |
| **description** | Texto |
| **confidence_score_out_of_ten** | Número |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definir campos de respuesta" }

Puedes añadir un campo llamado **product_description** a un catálogo y seleccionar **description** como el **Response Field** para rellenar la columna con las descripciones del agente.

![Un campo "product_description" con el agente "Descriptor" aplicado. La salida "description" está seleccionada como campo de respuesta.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

También puedes sobrescribir manualmente la celda generada por el agente seleccionando **Edit Item** y actualizando la descripción generada por el agente con tus ediciones. Para volver a la descripción generada por el agente, selecciona el símbolo de actualización en la celda.

### Manejo de errores {#error-handling}

- Si el proveedor de LLM devuelve un [error de límite de velocidad]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors), Braze reintenta continuamente la solicitud usando retirada exponencial hasta que la llamada tenga éxito o Braze determine que no se puede completar.
- Para otros fallos (como un tiempo de espera agotado o una clave de API no válida), el valor del campo del catálogo no se actualiza. Los Catalog Agents no admiten la configuración de valores alternativos en Agent Console.
- Puedes revisar los registros del agente para obtener detalles sobre las ejecuciones fallidas.
- Los Catalog Agents están limitados a procesar valores de entrada de hasta 25 KB por fila.

## Monitoriza tu agente {#monitor-your-agent}

La monitorización funciona de la misma manera independientemente de si tu agente se ejecuta en Canvas o en catálogos.

En la sección **Uso** de tu agente, puedes consultar y navegar hasta donde el agente se está utilizando activamente en catálogos y Canvas.

![Sección de uso del agente que muestra dos agentes activos y un agente inactivo para Canvas.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

En la sección **Registros** de tu agente, puedes monitorizar las llamadas reales del agente que se producen en tus Canvas y catálogos. Puedes filtrar por información como el rango de fechas, el resultado (éxito o error) o la ubicación de la llamada. También puedes seleccionar **Exportar CSV** para exportar los registros que se muestran únicamente en la página actual.

{% alert tip %}
También puedes monitorizar los errores del límite de invocaciones diarias en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log).
{% endalert %}

![Registros de un agente AI Sentiment Score.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

Selecciona **Ver** para una llamada específica del agente y consulta la entrada, la salida y el ID de usuario.

![Panel de detalles de un agente Random Sports Assignment que muestra el prompt de entrada, la respuesta de salida y un ID de usuario asociado.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

Para los agentes de pasos en Canvas, los registros incluyen una sección **Alternativa** que muestra cualquier salida alternativa que se utilizó cuando la invocación generó un error.

### Usa Currents {#use-currents}

También puedes utilizar estos eventos de Currents para acceder a los esquemas de registros de Kafka:

- Eventos de ejecución del agente
- Eventos de invocación de herramientas

Consulta el [Glosario de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) para más detalles.

## Artículos relacionados {#related-articles}

- [Paso de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step)
- [Referencia para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference)
- [Preguntas frecuentes]({{site.baseurl}}/user_guide/brazeai/agents/faq)