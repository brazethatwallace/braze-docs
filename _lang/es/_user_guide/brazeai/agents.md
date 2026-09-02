---
nav_title: Consola de Agente
article_title: "Agentes de Braze en la Consola de Agente"
page_order: 1
description: "Los agentes de Braze pueden generar contenido, tomar decisiones inteligentes y enriquecer tus datos para que puedas entregar experiencias del cliente más personalizadas."
---

# Agentes de Braze en la Consola de Agente {#braze-agents-in-agent-console}

> Los agentes de Braze son asistentes basados en inteligencia artificial que puedes crear dentro de Braze. Los agentes pueden generar contenido, tomar decisiones inteligentes y enriquecer tus datos para que puedas entregar experiencias del cliente más personalizadas.

{% alert important %}
Se necesitan créditos de mensajes o de acciones para acceder y utilizar los agentes de Braze. Si actualmente no tienes créditos de acciones y quieres utilizar los agentes de Braze, ponte en contacto con tu director de cuentas para conocer los pasos a seguir.
{% endalert %}

Mira este video para obtener un resumen de los agentes de Braze en la Consola de Agente.

{% multi_lang_include video.html id="afd0hp0vrh" source="wistia" title="Braze Agents in Agent Console overview" %}

## ¿Por qué usar Braze Agents? {#why-use-braze-agents}

Braze Agents ayudan a tu equipo a ofrecer experiencias más inteligentes y personalizadas, sin añadir trabajo extra. Actúan como agentes autónomos que no solo responden a indicaciones, sino que comprenden el contexto, toman decisiones y ejecutan acciones orientadas a un objetivo.

En la práctica, los agentes pueden crear automáticamente el texto de los mensajes —como líneas del asunto o textos dentro del producto— para que cada cliente reciba una comunicación que se sienta personalizada. También pueden adaptarse en tiempo real, dirigiendo a las personas por diferentes recorridos en Canvas según sus preferencias, comportamientos u otros datos.

Más allá de la mensajería, los agentes pueden enriquecer tus catálogos calculando o generando valores de campos de producto y perfil, manteniendo tus datos actualizados y dinámicos. Al encargarse de tareas repetitivas o complejas, liberan a tu equipo para que se concentre en la estrategia y la creatividad en lugar de la configuración manual. Braze Agents actúan más como colaboradores que como procesos en segundo plano, ayudándote a resolver problemas y generar impacto a escala.

### Cuándo usar Braze Agents en lugar de otras características de BrazeAI {#when-to-use-braze-agents-versus-other-brazeai-features}

Usa agentes para personalizar contenido sobre la marcha utilizando el contexto específico de un usuario. Por ejemplo, si un agente sabe que el sabor de helado favorito de un usuario en particular es chocolate y su topping favorito son los ositos de goma, puede generar un texto push específico para esa combinación para ese usuario a medida que avanza por el Canvas.

Sin embargo, el agente no aprende por ensayo y error, y no tiene noción de un objetivo de marketing final que busque medir y maximizar. Aunque le indiques que en general escriba textos que impulsen las conversiones, no cuenta con un mecanismo para "monitorear" el impacto en conversiones de su escritura agéntica e integrar esos datos en futuras llamadas agénticas. Puedes pensar en esto como toma de decisiones "por intuición", no como toma de decisiones de IA basada en recompensas.

En cambio, otras herramientas de BrazeAI están diseñadas para maximizar las métricas que miden. Por ejemplo, los agentes son muy buenos evaluando cualitativamente cómo las características de un usuario influyen en su probabilidad o propensión a realizar un determinado evento o preferir un determinado producto. Sin embargo, como el agente no aprende por ensayo y error, no tiene forma de medir la precisión de sus predicciones de probabilidad ni de mejorar la señal con el tiempo. Por ello, usar Predictive Suite supera al paso de agente cuando se juzga en función de la precisión de sus predicciones y las mejoras a lo largo del tiempo.

## Características {#features}

Las características de Braze Agents incluyen:

- **Configuración flexible:** Usa un LLM proporcionado por Braze o conecta tus propios [proveedores de modelos de IA]({{site.baseurl}}/partners/ai_model_providers) (como OpenAI, Anthropic, Google Gemini o Databricks Mosaic).
- **Integración fluida:** Implementa agentes directamente en pasos en Canvas o campos de catálogo.
- **Pruebas, registros e historial de versiones:** Previsualiza la salida de tu agente probándolo con entradas de ejemplo antes de lanzarlo. Consulta los registros de cada vez que se ejecuta el agente, incluidos la entrada y la salida de esa ejecución. Usa la pestaña **Version history** para revisar versiones anteriores y las diferencias en línea de los cambios en las instrucciones.
- **Controles de uso:** Los límites diarios ayudan a gestionar el rendimiento y los costos.

## Acerca de Braze Agents {#about-braze-agents}

Los agentes se configuran con instrucciones (indicaciones del sistema) que definen cómo se comportan. Cuando un agente se ejecuta, utiliza tus instrucciones junto con los datos que le proporcionas explícitamente para generar una respuesta. No pueden acceder a datos de usuario más allá de lo que configures: variables Liquid, selecciones de contexto del agente, variables de contexto de Canvas y valores del paso de contexto. Los agentes no buscan perfiles ni advierten cuando faltan datos. Consulta [Qué datos reciben los agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

### Conceptos clave {#key-concepts}

| Término | Definición |
| --- | --- |
| [Modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) | El "cerebro" del agente, en este caso un modelo grande de lenguaje (LLM). Interpreta entradas, genera respuestas y realiza razonamiento. Un modelo más potente (entrenado con datos más relevantes) hace que el agente sea más capaz y versátil. |
| [Instrucciones]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) | Las reglas o directrices que le proporcionas al agente (indicación del sistema). Definen cómo debe comportarse el agente cada vez que se ejecuta. Unas instrucciones claras hacen que el agente sea más fiable y predecible. |
| Contexto | Datos proporcionados al agente en tiempo de ejecución, en cualquier lugar donde esté implementado, como campos de perfil de usuario o filas de catálogo. Esta entrada proporciona la información que el agente utiliza para generar resultados. |
| [Variables de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#how-context-variables-work) | Datos temporales que puedes crear y utilizar dentro del recorrido de un usuario a través de un Canvas específico. |
| [Variable de salida]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#define-the-output-variable) | La salida que produce el agente cuando se utiliza en pasos en Canvas. Las variables de salida almacenan el resultado del agente para personalizar contenido o guiar los recorridos del flujo de trabajo. Las variables de salida pueden ser de tipo cadena, número o booleano. |
| [Invocación](#limitations) | Una sola ejecución del agente. Esto cuenta contra tus límites diarios. |
| [Formato de salida]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#select-output) | La estructura de datos predefinida de la respuesta del agente. |
| [Fuentes de conocimiento]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) | Un tipo de contexto de agente utilizado para recuperar datos de un catálogo con mayor precisión que si se hace referencia al catálogo directamente en las instrucciones del agente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conceptos clave" }

## Limitaciones {#limitations}

Se aplican las siguientes limitaciones:

- Cada agente tiene un límite diario predeterminado de 250,000 ejecuciones, que puede aumentarse hasta un máximo de 1,000,000 ejecuciones por día. Ponte en contacto con tu CSM si te interesa aumentar este límite.
- La Consola de Agente muestra un **Límite diario de coste de créditos de acción** para cada agente: el máximo estimado de créditos por día basado en la proporción de créditos por invocación de tu modelo y el límite diario de invocaciones. Consulta [Límites diarios de invocaciones y créditos]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).
- De forma predeterminada, cada ejecución debe completarse en 20 segundos. Después de 20 segundos, el agente devuelve una respuesta `null` donde se utiliza.
    - Si tus agentes agotan el tiempo de espera de forma constante, ponte en contacto con tu director de cuentas de Braze para aumentar este límite.
- Los datos de entrada están limitados a 25 KB por solicitud. Las entradas más largas se truncan.

## Buenas prácticas {#best-practices}

Orienta los casos de uso de alto valor en los que los agentes puedan generar el mayor ROI (ROI), y elige audiencias con probabilidades de responder. Una audiencia más pequeña y de alta oportunidad suele superar a una audiencia grande con baja oportunidad; por ejemplo, reorientar a usuarios que buscaron recientemente pero no convirtieron, en lugar de enviar textos generados por agentes a toda tu base de usuarios.

Para validar el ROI antes de escalar, usa un paso de [recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para enviar solo una parte de tu audiencia a través de un paso de agente. Cuando una prueba a pequeña escala dé buenos resultados, escala el agente a tu público objetivo completo y aumenta el [límite diario de invocaciones]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits) para que las invocaciones no se detengan a mitad del envío. Confirma que te sientes cómodo con el consumo estimado de créditos antes de escalar a tu audiencia completa. Para más orientación sobre el despliegue, consulta [Implementar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

## Gestión de errores {#error-handling}

Si el modelo conectado devuelve un [error de límite de velocidad]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) del proveedor del LLM durante una invocación de un agente de paso en Canvas o un agente de catálogo, Braze reintenta continuamente la solicitud utilizando retirada exponencial.

Para otros fallos (como un tiempo de espera agotado o una clave de API no válida), la salida del agente de paso en Canvas se establece en `null`, a menos que el agente tenga [valores de alternativa configurados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) en la Consola de Agente (solo agentes de paso en Canvas). Los agentes de catálogo no reintentan fallos que no sean de límite de velocidad. Si un agente alcanza su límite diario de invocaciones, Braze aplica los valores de alternativa configurados cuando están presentes; de lo contrario, la salida se establece en `null`.

Los errores de límite de velocidad, la indisponibilidad del modelo y los fallos por límite diario de invocaciones no consumen créditos de Braze. Los tiempos de espera agotados sí consumen créditos. Consulta [Cuándo se consumen créditos]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).

Cuando muchos usuarios entran en un paso de agente a la vez, el procesamiento puede tardar más debido a los [controles de flujo de invocación]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls). Configura valores de alternativa en la Consola de Agente para los agentes de paso en Canvas, de modo que los usuarios sigan recibiendo una salida cuando falle una invocación, o utiliza [valores predeterminados de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) en los pasos de mensaje posteriores.

## ¿Cómo se usan mis datos y cómo se envían a los LLM proporcionados por Braze? {#how-is-my-data-used-and-sent-to-braze-provided-llms}

Para generar resultados de IA a través de las características de IA de Braze que Braze identifica como que aprovechan los LLM proporcionados por Braze ("Resultados"), Braze enviará tu prompt del sistema o cualquier otra entrada, según corresponda ("Entrada") al LLM proporcionado por Braze. Los datos enviados al LLM proporcionado por Braze correspondiente no se utilizan para entrenar ni mejorar el LLM proporcionado por Braze. Entre tú y Braze, los Resultados son tu propiedad intelectual. Braze no reclamará ningún derecho de propiedad de copyright sobre dichos Resultados. Braze no ofrece ninguna garantía de ningún tipo con respecto a cualquier contenido generado por IA en general, incluidos los Resultados.

El LLM proporcionado por Braze para Braze Agents, identificado como "Auto", utiliza modelos de Google Gemini. Google retiene las Entradas y los Resultados enviados a través de Braze durante 55 días, tras los cuales los datos se eliminan.

## Próximos pasos {#next-steps}

Ahora que conoces los agentes de Braze, estás listo para los próximos pasos:

- [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Implementar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)