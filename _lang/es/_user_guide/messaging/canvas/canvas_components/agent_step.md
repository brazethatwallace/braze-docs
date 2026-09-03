---
nav_title: Agente
article_title: Paso de agente
alias: /agent_step/
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo usar el paso de agente en Canvas para generar contenido o tomar decisiones inteligentes en tiempo real."
tool: Canvas
toc_headers: h2
---

# Paso de agente {#agent-step}

> El paso de agente te permite añadir toma de decisiones y generación de contenido impulsadas por IA directamente en tu flujo de trabajo de Canvas. Para información más general, consulta [Agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents).

![Un paso de agente en un recorrido de usuario de Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Requisitos previos {#prerequisites}

Los pasos de agente utilizan [variables de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) para ingerir contexto relevante y generar una variable que se puede aprovechar en el Canvas.

## Cómo funciona {#how-it-works}

Cuando un usuario llega a un paso de agente en un Canvas, Braze envía los datos de entrada que has configurado (contexto completo o campos seleccionados) al agente que elegiste. Luego, el agente procesa la entrada utilizando su modelo e instrucciones, y devuelve una salida. Esa salida se almacena en la variable de salida que definiste en el paso.

Después puedes usar esta variable de tres formas principales:

- **Toma de decisiones:** Dirige a los usuarios por diferentes rutas de Canvas en función de la respuesta del agente. Por ejemplo, un agente de puntuación de leads podría devolver una categoría de lead como "Sales Ready", "Marketing Qualified" o "Disqualified". Podrías usar esta asignación para desencadenar una alerta de Slack o un mensaje automatizado para los leads "Sales Ready", mientras que los leads "Disqualified" se eliminan del recorrido.
- **Personalización:** Inserta la respuesta del agente directamente en un mensaje. Por ejemplo, un agente podría analizar los comentarios de los clientes y generar un correo electrónico de seguimiento empático que haga referencia al comentario del cliente y sugiera una resolución.
- **Procesamiento de datos de usuario:** Analiza y estandariza tus datos de usuario, y luego almacénalos en el perfil de usuario o envíalos mediante un webhook. Por ejemplo, un agente podría devolver una puntuación de sentimiento o una asignación de afinidad de producto. Puedes almacenar esos datos en un perfil de usuario para uso futuro.

## Crear un paso de agente {#creating-an-agent-step}

### Paso 1: Añadir un paso {#step-1-add-a-step}

Arrastra y suelta el componente **Agente** desde la barra lateral, o selecciona el botón de suma <i class="fas fa-plus-circle"></i> en la parte inferior de un paso y selecciona **Agente**.

### Paso 2: Elegir tu agente {#step-2-choose-your-agent}

Selecciona el agente que procesará los datos en este paso. Para obtener orientación sobre la configuración, consulta [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents).

En la lista de agentes, cada agente está etiquetado con su [límite de invocaciones diarias]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-3-set-up-details). Pasa el cursor sobre el límite para ver el progreso del día hacia ese límite, incluyendo el porcentaje utilizado y el número de invocaciones utilizadas hoy en comparación con el límite.

![El panel Configurar paso de agente mostrando el menú desplegable de agentes con dos agentes listados. Cada agente está etiquetado con su límite de invocaciones diarias. Un tooltip en el primer agente muestra el porcentaje utilizado y las invocaciones utilizadas hoy.]({% image_buster /assets/img/ai_agent/configure_agent_step.png %})

### Paso 3: Configurar la salida de tu agente {#define-the-output-variable}

Las salidas del agente se denominan "variables de salida" y se almacenan en una [variable de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#context-variable-filters) para facilitar el acceso. Para definir la variable de salida, dale un nombre a la variable.

Ten en cuenta que el tipo de datos de la variable de salida se configura desde la [Consola de agentes]({{site.baseurl}}/user_guide/brazeai/agents). Las salidas del agente se pueden guardar como cadenas, números, booleanos u objetos. Esto las hace flexibles tanto para la personalización de texto como para la lógica condicional en tu Canvas. Estos son algunos usos comunes para cada tipo:

| Tipo de datos | Usos comunes |
| --- | --- |
| Cadena | Personalización de mensajes (líneas del asunto, texto, respuestas) |
| Número | Puntuación, umbrales, enrutamiento en [rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) |
| Booleano | Ramificación Sí/No en [divisiones de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) |
| Objeto | Aprovecha uno o más de los tipos de datos mencionados anteriormente en esta sección con una sola llamada LLM en una estructura de datos predecible |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Configurar la salida de tu agente #define-the-output-variable" }

Puedes usar una variable de salida a lo largo del Canvas utilizando la misma sintaxis de plantilla que usarías con una variable de contexto. Usa el filtro de Segment **Variable de contexto**, o plantilla las respuestas del agente directamente usando Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Para usar una propiedad específica de una variable de salida de tipo objeto, usa la notación de punto para acceder a esa propiedad usando Liquid: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Paso de agente para Body HTML Writer con un tipo de datos objeto como salida para la variable "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Paso 4: Añadir instrucciones opcionales del paso {#step-4-add-optional-step-instructions}

Puedes incluir instrucciones opcionales del paso para cualquier cosa que tu agente necesite saber que sea específica de este paso y que no esté ya cubierta en las instrucciones principales del agente. Puedes introducir cualquier valor con plantilla Liquid que normalmente usarías en un Canvas.

### Paso 5: Probar el agente {#step-5-test-the-agent}

Puedes probar un paso de agente de dos formas:

**Vista previa en el paso (constructor de Canvas):** Después de configurar el paso, usa la vista previa del paso para ver la salida del agente para un usuario aleatorio, un usuario existente o un usuario personalizado. Esto prueba el paso de forma aislada sin recorrer la ruta completa del Canvas.

**Probar Canvas (recorrido completo):** Selecciona **Probar Canvas** en el pie de página del Canvas para previsualizar la ruta del usuario de extremo a extremo. Cuando la prueba llegue a tu paso de agente, Braze preguntará **¿Quieres ejecutar el agente "{agentName}"?**

- Selecciona **Sí** para añadir contexto opcionalmente, luego selecciona **Simular respuesta** para invocar al agente para el usuario de vista previa. Puedes describir entradas de ejemplo en lenguaje natural (por ejemplo, contenido del carrito o texto del mensaje) para complementar el perfil del usuario de prueba y cualquier contexto de Canvas ya establecido previamente.
- Selecciona **No** para omitir la invocación en vivo y usar la **salida alternativa** configurada del agente desde la Consola de agentes en su lugar.

Las invocaciones desde **Simular respuesta** cuentan para el límite de invocaciones diarias del agente y aparecen en **Consola de agentes** > **Registros**. Para ver el comportamiento completo de Probar Canvas, consulta [Previsualizar rutas de usuario]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths#agent-steps).

![Vista previa de la salida del agente como un usuario aleatorio.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Manejo de errores {#error-handling}

Para saber cómo Braze gestiona los fallos de agentes, los errores de límite de velocidad y los controles de flujo de invocaciones, consulta [Manejo de errores y comportamiento alternativo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior) en Desplegar agentes y [Manejo de errores]({{site.baseurl}}/user_guide/brazeai/agents#error-handling) en Agentes de Braze.

- Si el modelo conectado devuelve un [error de límite de velocidad]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) del proveedor de LLM, Braze reintenta continuamente la solicitud usando retirada exponencial hasta que la llamada tenga éxito o Braze determine que no se puede completar; luego los usuarios proceden al siguiente paso en Canvas.
- Para otros fallos (como un error de tiempo de espera o una clave de API no válida), o cuando un agente alcanza su límite diario de invocaciones, la variable de salida se establece en `null` a menos que el agente tenga [valores alternativos configurados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) en la Consola de agente. Cuando los valores alternativos están configurados, Braze renderiza la alternativa con Liquid por usuario y almacena el resultado en la variable de salida, incluso cuando el límite diario bloquea una invocación.
- Si no configuras valores alternativos, usa [valores predeterminados de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) en los pasos de mensaje posteriores para manejar salidas nulas. Por ejemplo, en el modal **Add Personalization**, puedes introducir un valor predeterminado de Liquid como {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} o {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- Las respuestas se almacenan en caché para entradas idénticas y pueden reutilizarse para invocaciones idénticas repetidas en pocos minutos.
    - Las respuestas que usan valores en caché sí cuentan para el total de invocaciones y las invocaciones diarias.
- Los pasos de agente pueden tardar en procesar un lote grande de usuarios. Braze pone en cola las invocaciones de acuerdo con los [controles de flujo de invocaciones]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls), por lo que los usuarios pueden permanecer pendientes durante envíos de alto volumen. Revisa tus registros para verificar que las invocaciones se están realizando.

## Análisis {#analytics}

Consulta las siguientes métricas para hacer seguimiento del rendimiento de tus pasos de agente:

| Métrica | Descripción |
| --- | --- |
| _Entrados_ | El número de veces que los usuarios entraron en el paso de agente. |
| _Procedieron al siguiente paso_ | El número de usuarios que procedieron al siguiente paso en el flujo después de pasar por el paso de agente. |
| _Salieron del Canvas_ | El número de usuarios que salieron del Canvas después de pasar por el paso de agente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Análisis" }

## Buenas prácticas {#best-practices}

### Divide las tareas entre agentes para casos de uso complicados {#split-tasks-between-agents-for-complicated-use-cases}

Si notas que un agente tiene dificultades con la complejidad de las tareas que le estás pidiendo, divide el trabajo en más de un paso de agente. Cuando un mismo prompt mezcla limpieza de datos, lógica de enrutamiento y redacción completa de mensajes, esos objetivos compiten entre sí y la calidad del resultado puede variar.

El siguiente patrón utiliza tres agentes para un ejemplo de viajes: alguien buscó recientemente en tu aplicación pero no reservó, y quieres un texto de reorientación que lo impulse hacia la compra.

- El agente 1 resume el contexto del Canvas. Lee campos como el nivel de fidelización, la última ciudad buscada y el comportamiento de búsqueda de alta intención, y devuelve un breve resumen estructurado como variable de salida que los pasos posteriores pueden reutilizar.
- El agente 2 devuelve un valor de enrutamiento sobre el que tu Canvas puede ramificarse. Usa un número, un booleano o un objeto estructurado para que la salida coincida con tu forma de ramificar. Asigna ese valor a un paso de [ruta de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) o de [división de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split). Por ejemplo, considera rutas separadas para mensajería enfocada en fidelización frente a mensajería enfocada en ofertas.
- El agente 3 redacta el texto del mensaje generado solo en las ramas donde lo necesites. Pasa el resumen del agente 1 (y cualquier contexto específico de la rama) para que este agente se enfoque en el tono y los límites del canal en lugar de normalizar entradas y elegir estrategia en el mismo prompt.

### Usa el paso de recorrido de experimentos para probar recorridos agénticos a pequeña escala {#use-the-experiment-paths-step-to-test-agentic-journeys-at-small-scale}

Para probar el rendimiento y el consumo de créditos de tu agente frente a tus recorridos existentes, añade un paso de [recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que solo una parte de tu audiencia entre en la rama que contiene tu paso de agente.

Por ejemplo, puedes empezar enviando unos cuantos miles de usuarios al día por una ruta con el agente y enviar el resto a una ruta de control o una ruta sin el agente. Recopila datos durante 1-2 semanas y compara los indicadores clave de rendimiento (indicador clave de rendimiento), las contramétricas y el consumo de créditos del agente entre las rutas. De esta forma, puedes generar confianza y demostrar el ROI antes de aumentar el tráfico hacia la rama habilitada con agente, y limitar el consumo de invocaciones para hacerlo.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuándo debo usar un paso de agente? {#when-should-i-use-an-agent-step}

En general, recomendamos usar un paso de agente cuando quieras alimentar un LLM con datos contextuales específicos y hacer que asigne de forma agéntica una variable de contexto de Canvas de manera inteligente a una escala imposible para los humanos.

Supongamos que estás enviando un mensaje personalizado para recomendar un nuevo sabor de helado a un usuario que anteriormente pidió chocolate y fresa. Esta es la diferencia entre usar un paso de agente y las recomendaciones de artículos con IA:

- **Paso de agente:** Usa LLM para tomar una decisión cualitativa sobre lo que el usuario podría querer, basándose en las instrucciones y los puntos de datos contextuales proporcionados al agente. En este ejemplo, un paso de agente podría recomendar un nuevo sabor basándose en la posibilidad de que el usuario quiera probar sabores diferentes.
- **Recomendaciones de artículos con IA:** Usa modelos de aprendizaje automático para predecir los productos que un usuario tiene más probabilidades de querer, basándose en eventos de usuario anteriores, como compras. En este ejemplo, las recomendaciones de artículos con IA sugerirían un sabor (vainilla) basándose en los dos pedidos anteriores del usuario (chocolate y fresa) y en cómo se comparan con los comportamientos de otros usuarios en tu espacio de trabajo.

### ¿Cómo usan los pasos de agente los datos de entrada? {#how-do-agent-steps-use-input-data}

Un paso de agente analiza los datos de contexto que el agente está configurado para usar, así como cualquier [instrucción opcional del paso](#step-4-add-optional-step-instructions) que agregues al paso.

## Artículos relacionados {#related-articles}

- [Resumen de Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents)
- [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Desplegar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)
- [Referencia para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference)