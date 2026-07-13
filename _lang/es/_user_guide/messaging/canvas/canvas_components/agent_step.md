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

Cuando un usuario llega a un paso de agente en un Canvas, Braze envía los datos de entrada que configuraste (contexto completo o campos seleccionados) al agente que elegiste. El agente procesa la entrada usando su modelo e instrucciones, y devuelve una salida. Esa salida se almacena en la variable de salida que definiste en el paso.

Puedes usar esta variable de tres formas principales:

- **Toma de decisiones:** Dirige a los usuarios por diferentes rutas de Canvas según la respuesta del agente. Por ejemplo, un agente de puntuación de leads podría devolver una categoría de lead como "Listo para ventas", "Calificado para marketing" o "Descalificado". Podrías usar esta asignación para activar una alerta de Slack o un mensaje automatizado para los leads "Listos para ventas", mientras eliminas del recorrido a los leads "Descalificados".
- **Personalización:** Inserta la respuesta del agente directamente en un mensaje. Por ejemplo, un agente podría analizar los comentarios de un cliente y generar un correo electrónico de seguimiento empático que haga referencia al comentario del cliente y sugiera una resolución.
- **Procesamiento de datos de usuario:** Analiza y estandariza tus datos de usuario, luego almacénalos en el perfil de usuario o envíalos mediante un webhook. Por ejemplo, un agente podría devolver una puntuación de sentimiento o una asignación de afinidad de producto. Puedes almacenar esos datos en un perfil de usuario para uso futuro.

## Crear un paso de agente {#creating-an-agent-step}

### Paso 1: Añadir un paso {#step-1-add-a-step}

Arrastra y suelta el componente **Agent** desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> de suma en la parte inferior de un paso y selecciona **Agent**.

### Paso 2: Elegir tu agente {#step-2-choose-your-agent}

Selecciona el agente que procesará los datos en este paso. Para orientación sobre la configuración, consulta [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents).

En la lista de agentes, cada agente está etiquetado con su [límite diario de invocaciones]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-3-set-up-details). Pasa el cursor sobre el límite para ver el progreso de hoy hacia ese límite, incluyendo el porcentaje utilizado y el número de invocaciones usadas hoy en comparación con el límite.

![El panel Configurar paso de agente mostrando el menú desplegable de agentes con dos agentes listados. Cada agente está etiquetado con su límite diario de invocaciones. Un tooltip en el primer agente muestra el porcentaje utilizado y las invocaciones usadas hoy.]({% image_buster /assets/img/ai_agent/configure_agent_step.png %})

### Paso 3: Configurar la salida de tu agente {#define-the-output-variable}

Las salidas del agente se llaman "variables de salida" y se almacenan en una [variable de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#context-variable-types) para un acceso fácil. Para definir la variable de salida, dale un nombre a la variable.

Ten en cuenta que el tipo de datos de la variable de salida se configura desde la [Consola de agente]({{site.baseurl}}/user_guide/brazeai/agents). Las salidas del agente se pueden guardar como cadenas, números, booleanos u objetos. Esto las hace flexibles tanto para la personalización de texto como para la lógica condicional en tu Canvas. Estos son algunos usos comunes para cada tipo:

| Tipo de datos | Usos comunes |
| --- | --- |
| Cadena | Personalización de mensajes (líneas del asunto, textos, respuestas) |
| Número | Puntuación, umbrales, enrutamiento en [rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) |
| Booleano | Ramificación Sí/No en [división de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) |
| Objeto | Aprovecha uno o más de los tipos de datos anteriores con una sola llamada LLM en una estructura de datos predecible |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Configurar la salida de tu agente" }

Puedes usar una variable de salida en todo el Canvas utilizando la misma sintaxis de plantilla que usarías con una variable de contexto. Usa el filtro de Segment **Context Variable**, o inserta las respuestas del agente directamente usando Liquid: {% raw %}`{{context.${response_variable_name}}}`{% endraw %}.

Para usar una propiedad específica de una variable de salida de tipo objeto, usa la notación de punto para acceder a esa propiedad usando Liquid: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Paso de agente para Body HTML Writer con un tipo de datos de objeto como salida para la variable "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Paso 4: Añadir contexto adicional (opcional) {#step-4-add-any-additional-context-optional}

Puedes decidir incluir valores de contexto adicionales para que el paso de agente los consulte cuando se ejecute. Puedes introducir cualquier valor con plantilla Liquid que normalmente usarías en un Canvas.

{% alert note %}
Ten en cuenta que el agente ya recibe automáticamente el contexto configurado en la sección **Instructions**. Las variables Liquid que ya se configuraron allí no necesitan volver a introducirse aquí.
{% endalert %}

![La opción de añadir contexto adicional a un paso de agente usando Liquid.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### Paso 5: Probar el agente {#step-5-test-the-agent}

Después de configurar tu paso de agente, puedes probar y previsualizar la salida de este paso.

![Previsualizar la salida del agente como un usuario aleatorio.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Manejo de errores {#error-handling}

Para saber cómo Braze gestiona los fallos de agentes, los errores de límite de velocidad y los controles de flujo de invocaciones, consulta [Manejo de errores y comportamiento alternativo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior) en Desplegar agentes y [Manejo de errores]({{site.baseurl}}/user_guide/brazeai/agents#error-handling) en Agentes de Braze.

- Si el modelo conectado devuelve un [error de límite de velocidad]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) del proveedor de LLM, Braze reintenta continuamente la solicitud usando retirada exponencial hasta que la llamada tenga éxito o Braze determine que no se puede completar; luego los usuarios proceden al siguiente paso en Canvas.
- Para otros fallos (como un error de tiempo de espera o una clave de API no válida), o cuando un agente alcanza su límite diario de invocaciones, la variable de salida se establece en `null` a menos que el agente tenga [valores alternativos configurados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) en la Consola de agente. Cuando los valores alternativos están configurados, Braze renderiza la alternativa con Liquid por usuario y almacena el resultado en la variable de salida, incluso cuando el límite diario bloquea una invocación.
- Si no configuras valores alternativos, usa [valores predeterminados de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) en los pasos de mensaje posteriores para manejar salidas nulas. Por ejemplo, en el modal **Add Personalization**, puedes introducir un valor predeterminado de Liquid como {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} o {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- Las respuestas se almacenan en caché para entradas idénticas y pueden reutilizarse para invocaciones idénticas repetidas en pocos minutos.
    - Las respuestas que usan valores en caché sí cuentan para el total de invocaciones y las invocaciones diarias.
- Los pasos de agente pueden tardar en procesar un lote grande de usuarios. Braze pone en cola las invocaciones de acuerdo con los [controles de flujo de invocaciones]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls), por lo que los usuarios pueden permanecer pendientes durante envíos de alto volumen. Revisa tus registros para verificar que las invocaciones se están realizando.

## Análisis {#analytics}

Consulta las siguientes métricas para rastrear el rendimiento de tus pasos de agente:

| Métrica | Descripción |
| --- | --- |
| _Entered_ | El número de veces que los usuarios ingresaron al paso de agente. |
| _Proceeded to Next Step_ | El número de usuarios que procedieron al siguiente paso en el flujo después de pasar por el paso de agente. |
| _Exited Canvas_ | El número de usuarios que salieron del Canvas después de pasar por el paso de agente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Análisis" }

## Mejores prácticas {#best-practices}

### Divide las tareas entre agentes para casos de uso complicados {#split-tasks-between-agents-for-complicated-use-cases}

Si descubres que un agente tiene dificultades con la complejidad de las tareas que le pides, divide el trabajo en más de un paso de agente. Cuando un solo prompt mezcla limpieza de datos, lógica de enrutamiento y redacción completa de mensajes, esos objetivos compiten entre sí y la calidad de la salida puede variar.

El siguiente patrón usa tres agentes para un ejemplo de viajes: alguien buscó en tu aplicación recientemente pero no reservó, y quieres crear textos de reorientación que lo impulsen hacia la compra.

- El agente 1 resume el contexto de Canvas. Lee campos como el nivel de fidelización, la última ciudad buscada y el comportamiento de búsqueda de alta intención, y devuelve un breve resumen estructurado como variable de salida que los pasos posteriores pueden reutilizar.
- El agente 2 devuelve un valor de enrutamiento sobre el cual tu Canvas puede ramificarse. Usa un número, booleano u objeto estructurado para que la salida coincida con la forma en que ramificas. Asigna ese valor a un paso de [rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) o [división de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split). Por ejemplo, considera rutas separadas para mensajería basada en fidelización frente a mensajería basada en ofertas.
- El agente 3 redacta el texto del mensaje generado solo en las ramas donde lo deseas. Pasa el resumen del agente 1 (y cualquier contexto específico de la rama) para que este agente se enfoque en el tono y los límites del canal en lugar de normalizar entradas y elegir estrategia en el mismo prompt.

### Usa el paso de recorrido de experimentos para probar recorridos agénticos a pequeña escala {#use-the-experiment-paths-step-to-test-agentic-journeys-at-small-scale}

Para probar el rendimiento y el consumo de créditos de tu agente frente a tus recorridos existentes, añade un paso de [recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que solo una parte de tu audiencia entre en la rama que contiene tu paso de agente.

Por ejemplo, puedes empezar enviando unos pocos miles de usuarios por día por una ruta con el agente y enviar el resto a una ruta de control o una ruta sin el agente. Recopila datos durante 1-2 semanas y compara los indicadores clave de rendimiento (KPI), las contramétricas y el consumo de créditos del agente entre las rutas. De esta forma, puedes generar confianza y demostrar el ROI antes de aumentar el tráfico hacia la rama habilitada con el agente, y limitar el consumo de invocaciones para hacerlo.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuándo debo usar un paso de agente? {#when-should-i-use-an-agent-step}

En general, recomendamos usar un paso de agente cuando quieras alimentar datos contextuales particulares a un LLM y hacer que asigne de forma agéntica una variable de contexto de Canvas de manera inteligente a una escala imposible para los humanos.

Supongamos que estás enviando un mensaje personalizado para recomendar un nuevo sabor de helado a un usuario que previamente pidió chocolate y fresa. Esta es la diferencia entre usar un paso de agente y recomendaciones de elementos de IA:

- **Paso de agente:** Usa LLMs para tomar una decisión cualitativa sobre lo que el usuario podría querer según las instrucciones y los puntos de datos de contexto proporcionados al agente. En este ejemplo, un paso de agente podría recomendar un nuevo sabor basándose en la posibilidad de que el usuario quiera probar sabores diferentes.
- **Recomendaciones de elementos de IA:** Usa modelos de aprendizaje automático para predecir los productos que un usuario tiene más probabilidades de querer según eventos pasados del usuario, como compras. En este ejemplo, las recomendaciones de elementos de IA sugerirían un sabor (vainilla) basándose en los dos pedidos anteriores del usuario (chocolate y fresa) y cómo se comparan con los comportamientos de otros usuarios en tu espacio de trabajo.

### ¿Cómo usan los pasos de agente los datos de entrada? {#how-do-agent-steps-use-input-data}

Un paso de agente analiza los datos de contexto que el agente está configurado para usar, así como cualquier contexto adicional que se [proporcione al agente](#step-4-add-any-additional-context-optional).

## Artículos relacionados {#related-articles}

- [Resumen de agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents)
- [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Desplegar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)
- [Referencia para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference)