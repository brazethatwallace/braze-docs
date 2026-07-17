---
nav_title: Consola de Agente
article_title: Agentes de Braze
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

## ¿Por qué utilizar los agentes de Braze? {#why-use-braze-agents}

Los agentes de Braze ayudan a tu equipo a entregar experiencias más inteligentes y personalizadas, sin añadir trabajo adicional. Actúan como agentes autónomos que no solo responden a indicaciones, sino que comprenden el contexto, toman decisiones y actúan para alcanzar un objetivo.

En la práctica, los agentes pueden crear automáticamente textos de mensajes, como líneas del asunto o texto dentro del producto, para que cada cliente reciba una comunicación que parezca personalizada. También pueden adaptarse en tiempo real, dirigiendo a las personas por diferentes rutas de Canvas en función de sus preferencias, comportamientos u otros datos.

Más allá de la mensajería, los agentes pueden enriquecer tus catálogos calculando o generando valores de campos de productos y perfiles, lo que mantiene tus datos actualizados y dinámicos. Al encargarse de tareas repetitivas o complejas, liberan a tu equipo para que pueda centrarse en la estrategia y la creatividad, en lugar de en la configuración manual. Los agentes de Braze actúan más como colaboradores que como procesos en segundo plano, ayudándote a resolver problemas y a generar impacto a gran escala.

### Cuándo utilizar los agentes de Braze frente a otras características de BrazeAI {#when-to-use-braze-agents-versus-other-brazeai-features}

Utiliza agentes para personalizar contenido sobre la marcha usando el contexto específico del usuario. Por ejemplo, si un agente sabe que el sabor de helado favorito de un usuario en particular es el chocolate y que su topping favorito son las gominolas, puede crear un texto push específico para esa combinación para ese usuario cuando pase por el Canvas.

Sin embargo, el agente no aprende mediante ensayo y error, y no tiene idea del objetivo de marketing final que busca medir y maximizar. Aunque le indiques que, en general, redacte textos que impulsen las conversiones, no dispone de ningún mecanismo para «supervisar» el impacto de sus textos en las conversiones e integrar esos datos en futuras llamadas. Puedes pensar en esto como una toma de decisiones basada en «vibraciones», no como toma de decisiones con IA basada en recompensas.

Por el contrario, otras herramientas de BrazeAI están diseñadas para maximizar las métricas que miden. Por ejemplo, los agentes son muy buenos a la hora de evaluar cualitativamente cómo las características de un usuario influyen en su probabilidad o propensión a realizar una determinada acción o a preferir un determinado producto. Sin embargo, dado que el agente no aprende mediante ensayo y error, no tiene idea de cómo medir su precisión a la hora de predecir probabilidades y mejorar la señal con el tiempo. Por lo tanto, el uso de Predictive Suite supera al paso del agente cuando se evalúa la precisión de sus predicciones y las mejoras a lo largo del tiempo.

## Características {#features}

Las características de los agentes de Braze incluyen:

- **Configuración flexible:** Utiliza un LLM proporcionado por Braze o conecta tus propios [proveedores de modelos de IA]({{site.baseurl}}/partners/ai_model_providers) (como OpenAI, Anthropic, Google Gemini o Databricks Mosaic).
- **Integración fluida:** Implementa agentes directamente en los pasos en Canvas o en los campos del catálogo.
- **Pruebas, registros e historial de versiones:** Obtén una vista previa del resultado de tu agente probando con entradas de muestra antes de lanzarlo. Consulta los registros de cada vez que se ejecuta el agente, incluyendo la entrada y salida de esa ejecución. Utiliza la pestaña **Historial de versiones** para revisar versiones anteriores y las diferencias en línea de los cambios en las instrucciones.
- **Controles de uso:** Los límites diarios ayudan a administrar el rendimiento y los costes.

## Acerca de los agentes de Braze {#about-braze-agents}

Los agentes se configuran con instrucciones (indicaciones del sistema) que definen cómo deben comportarse. Cuando un agente se ejecuta, utiliza tus instrucciones junto con los datos que le pasas explícitamente para generar una respuesta. No pueden acceder a datos de usuario más allá de lo que configures: variables de Liquid, selecciones de contexto del agente, variables de contexto de Canvas y valores de pasos de contexto. Los agentes no buscan en los perfiles ni advierten cuando faltan datos. Consulta [Qué datos reciben los agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

### Conceptos clave {#key-concepts}

| Término | Definición |
| --- | --- |
| [Modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) | El «cerebro» del agente, en este caso un modelo de lenguaje grande (LLM). Interpreta las entradas, genera respuestas y realiza razonamientos. Un modelo más sólido (entrenado con datos más relevantes) hace que el agente sea más capaz y versátil. |
| [Instrucciones]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) | Las reglas o directrices que le das al agente (indicación del sistema). Definen cómo debe comportarse el agente cada vez que se ejecuta. Las instrucciones claras hacen que el agente sea más fiable y predecible. |
| Contexto | Datos que se transmiten al agente en tiempo de ejecución, independientemente de dónde se implemente, como campos del perfil de usuario o filas del catálogo. Esta entrada proporciona la información que el agente utiliza para generar resultados. |
| [Variables de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#how-context-variables-work) | Datos temporales que puedes crear y utilizar dentro del recorrido de un usuario a través de un Canvas específico. |
| [Variable de salida]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#define-the-output-variable) | El resultado que produce el agente cuando se utiliza en los pasos en Canvas. Las variables de salida almacenan el resultado del agente para personalizar contenido o guiar las rutas del flujo de trabajo. Las variables de salida pueden ser de tipo cadena, número o booleano. |
| [Invocación](#limitations) | Una sola ejecución del agente. Esto cuenta para tus límites diarios. |
| [Formato de salida]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#select-output) | La estructura de datos predefinida de la respuesta del agente. |
| [Fuentes de conocimiento]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) | Un tipo de contexto del agente que se utiliza para recuperar datos de un catálogo con mayor precisión que si se hace referencia al catálogo directamente en las instrucciones del agente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conceptos clave" }

## Limitaciones {#limitations}

Se aplican las siguientes limitaciones:

- Cada agente tiene un límite de invocación diario predeterminado de 250 000 ejecuciones, que se puede aumentar hasta un máximo de 1 000 000 de ejecuciones por día. Ponte en contacto con tu administrador de éxito de cliente si te interesa aumentar este límite.
- La Consola de Agente muestra un **Límite diario de coste de créditos de acción** para cada agente: el máximo estimado de créditos por día en función de la proporción de créditos por invocación de tu modelo y el límite de invocación diario. Consulta [Límites diarios de invocación y créditos]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).
- De forma predeterminada, cada ejecución debe completarse en un plazo de 20 segundos. Después de 20 segundos, el agente devuelve una respuesta `null` donde se utiliza.
    - Si tus agentes agotan constantemente el tiempo de espera, ponte en contacto con tu director de cuentas de Braze para aumentar este límite.
- Los datos de entrada están limitados a 25 KB por solicitud. Las entradas más largas se truncan.

## Buenas prácticas {#best-practices}

Apunta a casos de uso de alto valor donde los agentes puedan generar el mayor retorno de la inversión (ROI), y elige audiencias que tengan probabilidades de responder. Una audiencia más pequeña y con alta oportunidad a menudo supera a una audiencia grande con baja oportunidad; por ejemplo, reorientar a usuarios que buscaron recientemente pero no convirtieron, en lugar de enviar textos generados por agentes a toda tu base de usuarios.

Para validar el ROI antes de escalar, utiliza un paso de [recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para enviar solo una parte de tu audiencia a través de un paso de agente. Para obtener más orientación sobre la implementación, consulta [Implementar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

## Gestión de errores {#error-handling}

Si el modelo conectado devuelve un [error de límite de velocidad]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) del proveedor del LLM durante la invocación de un agente de paso en Canvas o de un agente de catálogo, Braze reintenta continuamente la solicitud utilizando retirada exponencial.

Para otros fallos (como un tiempo de espera agotado o una clave de API no válida), la salida del agente de paso en Canvas se establece en `null` a menos que el agente tenga [valores alternativos configurados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) en la Consola de Agente (solo agentes de paso en Canvas). Los agentes de catálogo no reintentan los fallos que no son de límite de velocidad. Si un agente alcanza su límite de invocación diario, Braze aplica los valores alternativos configurados cuando están presentes; de lo contrario, la salida se establece en `null`.

Cuando muchos usuarios entran en un paso de agente a la vez, el procesamiento puede tardar más debido a los [controles de flujo de invocación]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls). Configura valores alternativos en la Consola de Agente para los agentes de paso en Canvas de modo que los usuarios sigan recibiendo resultados cuando una invocación falle, o utiliza [valores predeterminados de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) en los pasos de mensaje posteriores.

## ¿Cómo se utilizan mis datos y cómo se envían a los LLM proporcionados por Braze? {#how-is-my-data-used-and-sent-to-braze-provided-llms}

Con el fin de generar resultados de IA a través de las características de IA de Braze que Braze identifica como que aprovechan los LLM proporcionados por Braze («Resultado»), Braze enviará tu indicación del sistema o cualquier otra entrada, según corresponda («Entrada»), al LLM proporcionado por Braze. Los datos enviados al LLM proporcionado por Braze aplicable no se utilizan para entrenar o mejorar el LLM proporcionado por Braze. Entre tú y Braze, el Resultado es tu propiedad intelectual. Braze no reclamará ningún derecho de propiedad intelectual sobre dicho Resultado. Braze no ofrece garantía alguna con respecto a cualquier contenido generado por IA en general, incluido el Resultado.

El LLM proporcionado por Braze para los agentes de Braze, identificado como «Auto», utiliza modelos Google Gemini. Google conserva las Entradas y los Resultados enviados a través de Braze durante 55 días, tras los cuales los datos se eliminan.

## Próximos pasos {#next-steps}

Ahora que ya conoces los agentes de Braze, estás listo para los siguientes pasos:

- [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Implementar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)