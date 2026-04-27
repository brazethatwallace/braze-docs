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

# Paso de agente  

> El paso de agente te permite añadir toma de decisiones y generación de contenido impulsadas por IA directamente en tu flujo de trabajo de Canvas. Para información más general, consulta [Agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents/). 

![Un paso de agente en un recorrido de usuario de Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Requisitos previos

Los pasos de agente utilizan [variables de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/) para ingerir contexto relevante y generar una variable que se puede aprovechar en el Canvas.

## Cómo funciona

Cuando un usuario llega a un paso de agente en un Canvas, Braze envía los datos de entrada que configuraste (contexto completo o campos seleccionados) al agente que elegiste. El agente procesa la entrada usando su modelo e instrucciones, y devuelve una salida. Esa salida se almacena en la variable de salida que definiste en el paso.

Puedes usar esta variable de tres formas principales:

- **Toma de decisiones:** Dirige a los usuarios por diferentes rutas de Canvas según la respuesta del agente. Por ejemplo, un agente de puntuación de leads podría devolver un número entre 1 y 10. Puedes usar esta puntuación para decidir si continuar enviando mensajes a un usuario o eliminarlo del recorrido.
- **Personalización:** Inserta la respuesta del agente directamente en un mensaje. Por ejemplo, un agente podría analizar los comentarios de un cliente y generar un correo electrónico de seguimiento empático que haga referencia al comentario del cliente y sugiera una resolución.
- **Procesamiento de datos de usuario:** Analiza y estandariza tus datos de usuario, luego almacénalos en el perfil de usuario o envíalos mediante un webhook. Por ejemplo, un agente podría devolver una puntuación de sentimiento o una asignación de afinidad de producto. Puedes almacenar esos datos en un perfil de usuario para uso futuro.

## Crear un paso de agente

### Paso 1: Añadir un paso

Arrastra y suelta el componente **Agente** desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> de suma en la parte inferior de un paso y selecciona **Agente**.  

### Paso 2: Elegir tu agente  

Selecciona el agente que procesará los datos en este paso. Elige un agente existente. Para orientación sobre la configuración, consulta [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Paso 3: Configurar la salida de tu agente {#define-the-output-variable}

Las salidas del agente se llaman "variables de salida" y se almacenan en una [variable de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#context-variable-types) para un acceso fácil. Para definir la variable de salida, dale un nombre a la variable.

Ten en cuenta que el tipo de datos de la variable de salida se configura desde la [Consola de Agente]({{site.baseurl}}/user_guide/brazeai/agents). Las salidas del agente se pueden guardar como cadenas, números, booleanos u objetos. Esto las hace flexibles tanto para la personalización de texto como para la lógica condicional en tu Canvas. Estos son algunos usos comunes para cada tipo:

| Tipo de datos | Usos comunes |
| --- | --- |
| Cadena | Personalización de mensajes (líneas del asunto, textos, respuestas) |
| Número | Puntuación, umbrales, enrutamiento en [Rutas de audiencia]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) |
| Booleano | Ramificación Sí/No en [División de decisiones]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) |
| Objeto | Aprovecha uno o más de los tipos de datos anteriores con una sola llamada LLM en una estructura de datos predecible |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Puedes usar una variable de salida en todo el Canvas utilizando la misma sintaxis de plantilla que usarías con una variable de contexto. Usa el filtro de segmento **Variable de contexto**, o inserta las respuestas del agente directamente usando Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Para usar una propiedad específica de una variable de salida de tipo objeto, usa la notación de punto para acceder a esa propiedad usando Liquid: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Paso de agente para Body HTML Writer con un tipo de datos de objeto como salida para la variable "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Paso 4: Añadir contexto adicional (opcional)

Puedes decidir incluir valores de contexto adicionales para que el paso de agente los consulte cuando se ejecute. Puedes introducir cualquier valor con plantilla Liquid que normalmente usarías en un Canvas.

{% alert note %}
Ten en cuenta que el agente ya recibe automáticamente el contexto configurado en la sección **Instrucciones**. Las variables Liquid que ya se configuraron allí no necesitan volver a introducirse aquí.
{% endalert %}

![La opción de añadir contexto adicional a un paso de agente usando Liquid.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### Paso 5: Probar el agente

Después de configurar tu paso de agente, puedes probar y previsualizar la salida de este paso.

![Previsualizar la salida del agente como un usuario aleatorio.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Manejo de errores  

- Si el modelo conectado devuelve un error de límite de velocidad, Braze reintenta hasta cinco veces con retirada exponencial.  
- Si el agente falla por cualquier otra razón (como un error de tiempo de espera o una clave de API no válida), la variable de salida se establece en `null`.
    - Si un agente alcanza su límite diario de invocaciones, la variable de salida se establece en `null`. 
- Usa [valores predeterminados de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/) para protegerte contra errores. Por ejemplo, en el modal **Añadir personalización**, puedes introducir un valor predeterminado de Liquid como {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} o {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- Las respuestas se almacenan en caché para entradas idénticas y pueden reutilizarse para invocaciones idénticas repetidas en pocos minutos.
    - Las respuestas que usan valores en caché sí cuentan para el total de invocaciones y las invocaciones diarias.
- Los pasos de agente pueden tardar en procesar un lote grande de usuarios. Si ves usuarios que aún están pendientes en este paso, revisa tus registros para verificar que las invocaciones se están realizando.

## Análisis  

Consulta las siguientes métricas para rastrear el rendimiento de tus pasos de agente:  

| Métrica | Descripción |
| --- | --- |
| _Ingresaron_ | El número de veces que los usuarios ingresaron al paso de agente. |
| _Procedieron al siguiente paso_ | El número de usuarios que procedieron al siguiente paso en el flujo después de pasar por el paso de agente. |
| _Salieron del Canvas_ | El número de usuarios que salieron del Canvas después de pasar por el paso de agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Preguntas frecuentes

### ¿Cuándo debo usar un paso de agente?

En general, recomendamos usar un paso de agente cuando quieras alimentar datos contextuales particulares a un LLM y hacer que asigne de forma agéntica una variable de contexto de Canvas de manera inteligente a una escala imposible para los humanos.

Supongamos que estás enviando un mensaje personalizado para recomendar un nuevo sabor de helado a un usuario que previamente pidió chocolate y fresa. Esta es la diferencia entre usar un paso de agente y Recomendaciones de elementos de IA:

- **Paso de agente:** Usa LLMs para tomar una decisión cualitativa sobre lo que el usuario podría querer según las instrucciones y los puntos de datos de contexto proporcionados al agente. En este ejemplo, un paso de agente podría recomendar un nuevo sabor basándose en la posibilidad de que el usuario quiera probar sabores diferentes.
- **Recomendaciones de elementos de IA:** Usa modelos de aprendizaje automático para predecir los productos que un usuario tiene más probabilidades de querer según eventos pasados del usuario, como compras. En este ejemplo, Recomendaciones de elementos de IA sugeriría un sabor (vainilla) basándose en los dos pedidos anteriores del usuario (chocolate y fresa) y cómo se comparan con los comportamientos de otros usuarios en tu espacio de trabajo.

### ¿Cómo usan los pasos de agente los datos de entrada?

Un paso de agente analiza los datos de contexto que el agente está configurado para usar, así como cualquier contexto adicional que se [proporcione al agente](#step-4-add-any-additional-context-optional).

## Artículos relacionados  

- [Resumen de agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Desplegar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
- [Referencia para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference/)