---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre agentes
description: "Este artículo ofrece respuestas a las preguntas frecuentes sobre los agentes de Braze."
page_order: 10
toc_headers: h2
---

# Preguntas frecuentes sobre agentes {#agents-frequently-asked-questions}

> Este artículo responde a las preguntas frecuentes sobre los agentes de Braze.

## General {#general}

### ¿Cuál es la diferencia entre los agentes de paso en Canvas y los agentes de catálogo? {#what-is-the-difference-between-canvas-step-agents-and-catalog-agents}

Al crear un agente, especificas si quieres crear un agente de paso en Canvas o un agente de catálogo. Esto determina los tipos de instrucciones y opciones que el agente puede admitir. Los agentes de paso en Canvas procesan usuarios en tiempo real dentro de los recorridos, mientras que los agentes de catálogo enriquecen los datos del catálogo añadiendo o actualizando columnas con información procesada.

### ¿Cuáles son los beneficios de usar el modelo automático en comparación con traer tu propio modelo (BYO)? {#what-are-the-benefits-of-using-auto-model-versus-bring-your-own-byo-model}

Los beneficios de usar el modelo automático de Braze incluyen:

- No requiere la recuperación ni la introducción de claves de API ni la configuración de integraciones
- Enrutamiento automático de cada invocación al modelo más eficaz para realizar la tarea

### ¿Dónde puedo encontrar mi uso actual de agentes? {#where-can-i-find-my-current-agent-usage}

Ve a **Configuración** > **Facturación** > **Uso de créditos** > **Agent Console** para ver el consumo de créditos, los recuentos de invocaciones y las proporciones de créditos por agente. Consulta [Límites diarios de invocaciones y créditos]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits) para más detalles.

### ¿Puedo usar sentencias condicionales de Liquid en las instrucciones del agente? {#can-i-use-conditional-liquid-statements-in-agent-instructions}

No, intentar escribir bloques de Liquid como sentencias {% raw %}`{% if %}`{% endraw %} puede provocar un error de validación. En su lugar, los agentes pueden manejar diferentes escenarios a través de descripciones en lenguaje natural en el prompt.

### ¿Pueden los agentes acceder a datos de usuario más allá de los atributos Liquid específicos o el contexto de Canvas que les paso? {#can-agents-access-user-data-beyond-the-specific-liquid-attributes-or-canvas-context-that-i-pass-to-them}

No. Los agentes solo reciben los puntos de datos de usuario específicos que se pasan usando Liquid en las instrucciones, las selecciones de [+ Contexto del agente]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources), los [pasos de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) anteriores en Canvas, o el contexto adicional en el paso del agente. Los agentes no pueden buscar en los perfiles de usuario atributos que no hayas configurado para que reciban.

Los agentes tampoco pueden avisarte cuando faltan datos necesarios: proceden con lo que haya en el prompt. Trata la configuración del agente como un diseño deliberado de entrada a salida: pasa cada campo que el agente necesite y verifica las entradas en **Agent Console** > **Logs**. Para orientación, consulta [Qué datos reciben los agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

## Solución de problemas {#troubleshooting}

### ¿Por qué mi agente no siguió mis instrucciones o reglas? {#why-did-my-agent-not-follow-my-instructions-or-rules}

Considera usar [Operator]({{site.baseurl}}/user_guide/brazeai/operator) para investigar por qué tu agente no está siguiendo tus instrucciones. Operator puede proporcionar instrucciones paso a paso y explicaciones detalladas.

### ¿Por qué mi agente de catálogo omitió algunas filas? {#why-did-my-catalog-agent-skip-some-rows}

Los agentes de catálogo omiten una fila cuando una columna que marcaste como **obligatoria para ejecutar** está vacía o falta; por ejemplo, un campo `gender` que no se ha completado. Después de seleccionar las columnas de entrada, habilita el control de entrada obligatoria para el campo del catálogo y elige qué columnas deben contener valores antes de que el agente se ejecute; las columnas seleccionadas comienzan como obligatorias de forma predeterminada, pero puedes eliminar columnas que pueden estar vacías sin bloquear la invocación. Esto evita desperdiciar tokens en datos incompletos.

El agente también respeta las dependencias entre columnas. Si una columna de salida depende de otras columnas (por ejemplo, la columna D requiere valores en las columnas B y C), el agente no se ejecuta hasta que esas columnas previas estén completadas para esa fila.

Para más detalles, consulta [Mejores prácticas del agente de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

### ¿Las invocaciones fallidas del agente consumen créditos? {#do-failed-agent-invocations-consume-credits}

Depende del tipo de fallo:

| Fallo | ¿Consume créditos? |
| --- | --- |
| Error de límite de velocidad | No |
| Modelo no disponible | No |
| Límite diario de invocaciones alcanzado | No |
| Tiempo de espera agotado | Sí |
{: .reset-td-br-1 .reset-td-br-2 aria-label="¿Las invocaciones fallidas del agente consumen créditos?" }

Consulta [Cuándo se consumen los créditos]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed) para más detalles.

### Mi agente tiene dificultades con una tarea compleja. ¿Cómo puedo mejorar su rendimiento? {#subagent-approach}

Si notas que el agente tiene dificultades con las tareas que le pides, considera un enfoque de subagentes. Por ejemplo, podrías usar tres agentes para hacer lo siguiente:

- El agente 1 estandariza y transforma los datos no estructurados de contexto de Canvas entrantes.
- El agente 2 consulta un catálogo de detalles de artículos e identifica cuáles podrían ser relevantes.
- El agente 3 consulta un catálogo diferente que tiene una variedad de descripciones posibles para cada artículo e identifica la descripción del artículo más relevante para el usuario para incluirla en un correo electrónico.

### ¿Qué podría causar que un agente personalizado agote el tiempo de espera con frecuencia? {#what-might-cause-a-custom-agent-to-frequently-time-out}

Un agente personalizado puede agotar el tiempo de espera si:

- Las instrucciones del agente están incompletas o son contradictorias
- Las instrucciones del agente no cubren todos los escenarios ni incluyen una condición alternativa (como "Si todas las entradas están vacías, devolver 'No se pudo personalizar'")
- Las instrucciones del agente piden al agente que genere un formato de salida diferente al especificado en la pestaña **Output** (por ejemplo, si las instrucciones del agente piden una cadena, pero en la pestaña **Output** la salida está definida como un número)
- La tarea del agente es demasiado compleja y se beneficiaría de un [enfoque de subagentes](#subagent-approach) en su lugar

#### Cómo reducir los tiempos de espera agotados {#how-to-reduce-timeouts}

Si tu agente agota el tiempo de espera con frecuencia, prueba lo siguiente antes de contactar a tu director de cuentas sobre un límite de tiempo de espera más alto:

- **Elige un modelo más simple o de menor costo:** Los modelos más rápidos generalmente se completan dentro de la ventana de tiempo de espera predeterminada. Consulta [Determinar qué modelo usar]({{site.baseurl}}/user_guide/brazeai/agents/reference#determine-which-model-to-use).
- **Reduce el nivel de razonamiento (solo modelos BYO):** Comienza en **Minimal** y auméntalo solo si la calidad de la salida se ve afectada. Consulta [Niveles de razonamiento]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels).
- **Simplifica el prompt:** Elimina instrucciones redundantes, acorta los ejemplos y reduce el esquema de salida. Usa [Operator]({{site.baseurl}}/user_guide/brazeai/operator) para revisar y ajustar tus instrucciones.
- **Divide los flujos de trabajo complejos en múltiples agentes:** Si el caso de uso tiene varios subpasos (por ejemplo, clasificar la intención y luego generar el texto), usa agentes separados en secuencia en Canvas o en el catálogo en lugar de un solo agente que haga todo. Consulta [enfoque de subagentes](#subagent-approach).

{% alert note %}
Los tiempos de espera agotados consumen créditos de Braze incluso cuando el agente no devuelve una salida utilizable. Consulta [Cuándo se consumen los créditos]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).
{% endalert %}

Para los agentes de paso en Canvas, configura [valores alternativos]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) en Agent Console para que los usuarios sigan recibiendo una salida cuando una invocación falle.

### ¿Por qué mi agente funcionó bien en las pruebas pero no recibe datos específicos del usuario cuando lo lanzo en un Canvas? {#why-did-my-agent-do-fine-in-testing-but-isnt-getting-any-user-specific-data-when-i-launch-it-in-a-canvas}

Si tu agente funciona correctamente durante las pruebas pero no recibe datos específicos del usuario en un Canvas en vivo, prueba estos pasos de solución de problemas:

- Asegúrate de que los datos específicos del usuario que quieres que el agente reciba estén ingresados como variables Liquid en las instrucciones del agente.
- Si tienes datos importantes en el contexto de Canvas, usa la opción **Add all Canvas context** en la configuración del agente para asegurarte de que el agente reciba todo el contexto de Canvas.
- Asegúrate de que cualquier contexto de Canvas al que quieras que el agente acceda esté almacenado como contexto de Canvas. Usa un paso de contexto antes del paso del agente para almacenar estos datos.

## Cumplimiento normativo {#compliance}

### ¿Agent Console cumple con el RGPD/CCPA? {#is-agent-console-gdprccpa-compliant}

Sí. Cuando un cliente utiliza el modelo Braze Auto (impulsado por Gemini), Google actúa como subencargado del tratamiento de Braze, sujeto a los términos del Anexo de Tratamiento de Datos (DPA) entre el cliente y Braze.

### ¿Agent Console cumple con HIPAA? {#is-agent-console-hipaa-compliant}

Sí. Cuando se utiliza el modelo Braze Auto, contamos con un acuerdo específico de HIPAA, el Anexo de Asociado Comercial (BAA), con Google que cubre Gemini, el cual impulsa nuestro modelo Auto.

Nuestro BAA se aplica únicamente a los clientes que utilizan el modelo Braze Auto. Si los clientes usan su propia clave de LLM, Braze no envía información de salud protegida (PHI) sujeta a HIPAA a un LLM en su nombre; los clientes la envían directamente. En este caso, el BAA entre Braze y Google no aplica. El tratamiento de datos a través de su propia clave de LLM se rige por el contrato del cliente y cualquier BAA que tenga directamente con su proveedor de LLM.