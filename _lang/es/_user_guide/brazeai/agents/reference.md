---
nav_title: Referencia
article_title: Referencia para agentes
description: "Detalles clave de referencia sobre los agentes de Braze."
page_order: 3
---

# Referencia para agentes {#reference-for-agents}

> A medida que crees agentes personalizados, consulta este artículo para obtener más información sobre configuraciones clave, como instrucciones y esquemas de salida. Para una configuración paso a paso, consulta [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents). Para una introducción, consulta [Agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents) y [Preguntas frecuentes]({{site.baseurl}}/user_guide/brazeai/agents/faq).

## Modelos {#models}

Cuando configuras un agente, puedes elegir el modelo que utiliza para generar respuestas. Tienes dos opciones: usar un modelo con tecnología de Braze o aportar tu propia clave de API.

{% alert important %}
El modelo **Auto** con tecnología de Braze está optimizado para modelos cuyas capacidades de razonamiento son suficientes para realizar tareas como búsqueda en catálogos y pertenencia a Segments. Cuando uses otros modelos, te recomendamos realizar pruebas para confirmar que tu modelo funciona bien para tu caso de uso. Es posible que necesites ajustar tus [instrucciones](#writing-instructions) para dar diferentes niveles de detalle o razonamiento paso a paso a modelos con diferentes velocidades y capacidades.
{% endalert %}

### Opción 1: Usar un modelo con tecnología de Braze {#option-1-use-a-braze-powered-model}

Esta es la opción más sencilla, sin necesidad de configuración adicional. Braze proporciona acceso a modelos de lenguaje grande (LLM) directamente. Para usar esta opción, selecciona **Auto**, que utiliza modelos Gemini.

{% alert important %}
Si no ves **Braze Auto** como opción en el menú desplegable **Model** al crear un agente, ponte en contacto con tu administrador de éxito de cliente para saber cómo ser elegible para usar el modelo Braze Auto.
{% endalert %}

### Opción 2: Aportar tu propia clave de API {#option-2-bring-your-own-api-key}

Con esta opción, puedes conectar tu cuenta de Braze con proveedores como OpenAI, Anthropic o Google Gemini. Si aportas tu propia clave de API de un proveedor de LLM, los costes de tokens se facturan directamente a través de tu proveedor, no a través de Braze.

Te recomendamos probar regularmente los modelos más recientes, ya que los modelos antiguos pueden ser descontinuados o quedar obsoletos después de unos meses. Asegúrate de tener créditos suficientes con tu proveedor para ejecutar tus agentes a escala. También puedes suscribirte a las notificaciones de Agent Console en [Preferencias de notificación]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) para recibir alertas cuando Braze detecte que un modelo ya no está disponible o encuentre problemas de facturación con tu proveedor de LLM.

Para configurar esto:

1. Ve a **Partner Integrations** > **Technology Partners** y busca tu proveedor.
2. Introduce tu clave de API del proveedor.
3. Selecciona **Save**.

Luego, puedes volver a tu agente y seleccionar tu modelo.

Cuando usas un LLM proporcionado por Braze, los proveedores de dicho modelo actúan como subprocesadores de Braze, sujetos a los términos del Acuerdo de Procesamiento de Datos (DPA) entre tú y Braze. Si decides aportar tu propia clave de API, el proveedor de tu suscripción de LLM se considera un proveedor externo según el contrato entre tú y Braze.

#### Niveles de razonamiento {#thinking-levels}

Algunos proveedores de LLM pueden permitirte ajustar el nivel de razonamiento de un modelo seleccionado. Los niveles de razonamiento definen el rango de pensamiento que el modelo utiliza antes de responder, desde respuestas rápidas y directas hasta cadenas de razonamiento más largas. Esto afecta la calidad de la respuesta, la latencia y el uso de tokens.

| Nivel | Cuándo usarlo |
|-------|---------------|
| **Mínimo** | Tareas sencillas y bien definidas (como búsqueda en catálogos, clasificación directa). Respuestas más rápidas y menor coste. |
| **Bajo** | Tareas que se benefician de un poco más de razonamiento pero no necesitan un análisis profundo. |
| **Medio** | Tareas de varios pasos o con matices (como analizar varias entradas para recomendar una acción). |
| **Alto** | Razonamiento complejo, casos extremos o cuando necesitas que el modelo trabaje paso a paso antes de responder. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Niveles de razonamiento" }

Recomendamos empezar con **Mínimo** y probar las respuestas de tu agente. Luego, puedes ajustar el nivel de razonamiento a **Bajo** o **Medio** si observas que el agente tiene dificultades para proporcionar respuestas precisas. En casos excepcionales, puede ser necesario un nivel de razonamiento **Alto**, aunque usar este nivel puede resultar en costes elevados de tokens y tiempos de respuesta más largos o mayor riesgo de [errores de tiempo de espera agotado]({{site.baseurl}}/user_guide/brazeai/agents/faq#what-might-cause-a-custom-agent-to-frequently-time-out). Si tu agente tiene dificultades para equilibrar el razonamiento de varios pasos con tiempos de respuesta razonables, considera dividir tu caso de uso en más de un agente que puedan trabajar juntos en un Canvas o catálogo.

Braze utiliza los mismos rangos de IP para las llamadas salientes de LLM que para el contenido conectado. Los rangos se enumeran en la [lista de direcciones IP permitidas para contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting). Si tu proveedor admite listas de direcciones IP permitidas, puedes restringir la clave a esos rangos para que solo Braze pueda usarla.

{% alert important %}
Cuando usas un LLM proporcionado por Braze, los proveedores de dicho modelo actúan como subprocesadores de Braze, sujetos a los términos del Acuerdo de Procesamiento de Datos (DPA) entre tú y Braze. Si decides aportar tu propia clave de API, el proveedor de tu suscripción de LLM se considera un proveedor externo según el contrato entre tú y Braze.
{% endalert %}

#### Determinar qué modelo usar {#determine-which-model-to-use}

Cada proveedor de LLM tiene una combinación ligeramente diferente de capacidades de modelo, costes y niveles de razonamiento. A continuación, se presentan algunas directrices generales y prácticas recomendadas:

- Para la eficiencia de costes, prioriza probar modelos con menor coste de tokens sobre modelos con mayor coste. Ajusta a modelos de mayor coste solo si los modelos de menor coste tienen dificultades con el caso de uso o generan resultados inconsistentes o imprecisos.
- Para la eficiencia de velocidad y rendimiento, prioriza probar niveles de razonamiento más bajos sobre niveles de razonamiento más altos. Ajusta a niveles de razonamiento más altos solo si los niveles más bajos tienen dificultades con el caso de uso o generan resultados inconsistentes o imprecisos.
- Si los modelos de menor coste o los niveles de razonamiento más bajos tienen dificultades con el caso de uso o generan resultados inconsistentes o imprecisos, considera ajustar a modelos de mayor coste o niveles de razonamiento más altos.
- Durante las pruebas, asegúrate de equilibrar la fiabilidad y precisión con el uso de tokens y la duración de la invocación.
- Cada caso de uso puede tener un modelo y nivel de razonamiento óptimos diferentes. Recomendamos realizar pruebas exhaustivas para verificar una calidad consistente sin tiempos de espera agotados.

### Controles de flujo de invocaciones {#invocation-flow-controls}

Los siguientes controles de flujo de invocaciones se aplican por espacio de trabajo:

- **Modelo con tecnología de Braze:** 5000 invocaciones por minuto
- **Aportar tu propia clave de API:** 5000 invocaciones por minuto

Cuando muchos usuarios entran en un paso de agente al mismo tiempo, Braze pone las invocaciones en cola según estos límites, por lo que el procesamiento puede tardar más durante los envíos de alto volumen.

### Límites diarios de invocaciones y créditos {#daily-invocation-and-credit-limits}

Cada agente tiene un límite diario de invocaciones (predeterminado 250 000; máximo 1 000 000 a menos que tu contrato permita más). Cada invocación (incluidas las vistas previas de Agent Console y las ejecuciones de prueba de Canvas que usan **Simulate response**) cuenta para este límite.

En Agent Console, el **Daily action credit cost limit** estima los créditos máximos que un agente puede consumir por día. Braze multiplica la proporción de créditos por invocación de tu espacio de trabajo para el modelo seleccionado por el límite diario de invocaciones.

### Cuándo se consumen los créditos {#when-credits-are-consumed}

Braze cobra créditos solo por las invocaciones que completan el procesamiento. No se consumen créditos cuando una invocación falla debido a:

- Un [error de límite de velocidad](#rate-limit-errors) del proveedor de LLM (incluidos los reintentos que finalmente fallan)
- El modelo seleccionado no está disponible
- El agente alcanzó su límite diario de invocaciones

Los créditos se consumen cuando una invocación agota el tiempo de espera, aunque el agente no devuelva un resultado utilizable.

### Supervisar el uso de créditos {#monitor-credit-usage}

Ve a **Settings** > **Billing** > **Credits Usage** > **Agent Console** para ver el consumo de créditos, los recuentos de invocaciones y las proporciones de créditos por agente.

Las proporciones de créditos provienen de tu contrato y aparecen en el panel de [uso de créditos]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage) (pestaña **Credit Ratios** y pestaña **Agent Console**). La estimación se actualiza cuando cambias el modelo o el límite de invocaciones.

Para gestionar el gasto, reduce el límite diario de invocaciones. Para modelos de [clave propia (BYO)](#option-2-bring-your-own-api-key), también puedes elegir un modelo de menor coste o reducir el [nivel de razonamiento](#thinking-levels) para disminuir los costes de tokens del proveedor. Braze Auto no admite el ajuste del nivel de razonamiento.

### Errores de límite de velocidad {#rate-limit-errors}

Si el proveedor de LLM devuelve un error de límite de velocidad durante una invocación de un paso de agente en Canvas o un agente de catálogo, Braze reintenta continuamente la solicitud mediante retirada exponencial hasta que la llamada se completa correctamente o Braze determina que no se puede completar.

Cuando se agotan los reintentos de Canvas o catálogo, el panel de detalles de **Logs** muestra **Error** y el mensaje del proveedor (como `Rate limit exceeded`) en **Output**. Los reintentos son visibles en los registros, incluida la primera invocación independientemente de su éxito o fallo final. Para un usuario dado, si se necesitan cuatro reintentos para finalmente obtener un éxito, puedes buscar el ID de usuario y ver los cinco (el original más cuatro reintentos) en los **Logs**, y el original más los tres primeros reintentos mostrarán **Error** con `Rate limit exceeded`.

Los errores de límite de velocidad no consumen créditos de Braze, incluidos los reintentos fallidos que se muestran en **Logs**.

![Detalles de registro de Agent Console que muestran un error de límite de velocidad excedido en el campo Output.]({% image_buster /assets/img/ai_agent/rate_limit_error_log.png %}){: style="max-width:75%;"}

## Instrucciones de escritura {#writing-instructions}

Las instrucciones son las reglas o directrices que le das al agente (indicación del sistema). Definen cómo debe comportarse el agente cada vez que se ejecuta. Las instrucciones del sistema pueden tener hasta 25 KB.

Si creaste tu agente con [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) usando una [plantilla de inicio]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), revisa las instrucciones precargadas y edítalas según sea necesario.

Estas son algunas buenas prácticas generales para comenzar con las indicaciones:

1. Comienza con el objetivo en mente. Establece la meta primero.
2. Dale al modelo un rol o persona ("Eres un ...").
3. Define un contexto y restricciones claros (audiencia, extensión, tono, formato).
4. Pide estructura ("Devuelve JSON/lista con viñetas/tabla...").
5. Muestra, no cuentes. Incluye algunos ejemplos de alta calidad.
6. Divide las tareas complejas en pasos ordenados ("Paso 1... Paso 2...").
7. Fomenta el razonamiento ("Piensa en los pasos internamente y luego proporciona una respuesta final concisa" o "explica brevemente tu decisión").
8. Prueba, inspecciona e itera. Pequeños ajustes pueden generar grandes mejoras en la calidad.
9. Gestiona los casos límite, añade barreras de seguridad e incluye instrucciones de rechazo.
10. Mide y documenta lo que funciona internamente para su reutilización y escalado.

### Ejemplos {#examples}

Para configuraciones iniciales en Agent Console, consulta [Plantillas de agente creadas con Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

Para ejemplos completos de instrucciones que puedes copiar o adaptar, consulta la [biblioteca de casos de uso para Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/examples).

| Ejemplo | Categoría | Tipo de agente | Qué hace |
| --- | --- | --- | --- |
| [Escribir mensajes personalizados basados en el contexto de un usuario]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-personalized-messaging-based-on-a-users-context) | Generación de contenido | Canvas Step Agent | Genera asunto/preencabezado de correo electrónico y título/cuerpo de push coordinados para usuarios que buscaron pero no reservaron. |
| [Analizar comentarios de usuarios para determinar los próximos pasos]({{site.baseurl}}/user_guide/brazeai/agents/examples#analyze-user-feedback-to-determine-next-steps) | Estandarización de datos | Canvas Step Agent | Clasifica el sentimiento y el tema de encuestas posteriores al viaje, luego recomienda un siguiente paso de CRM. |
| [Categorizar usuarios en contenedores de interés a partir de atributos existentes]({{site.baseurl}}/user_guide/brazeai/agents/examples#categorize-users-into-interest-buckets-from-existing-attributes) | Agente de afinidad | Canvas Step Agent | Clasifica usuarios en contenedores de interés a partir de atributos y señales de alta intención, luego recomienda la mejor siguiente experiencia o artículo. |
| [Dirigir usuarios a la ruta de Canvas más relevante a partir del comportamiento reciente]({{site.baseurl}}/user_guide/brazeai/agents/examples#route-users-to-the-most-relevant-canvas-path-from-recent-behavior) | Agente de afinidad | Canvas Step Agent | Infiere la motivación a partir del comportamiento reciente y devuelve la mejor clave de ruta para el siguiente paso en Canvas del usuario. |
| [Asignar usuarios a categorías de interés a partir de acciones de alta intención en tiempo real]({{site.baseurl}}/user_guide/brazeai/agents/examples#assign-users-to-interest-categories-from-real-time-high-intent-actions) | Agente de afinidad | Canvas Step Agent | Asigna categorías de interés a partir de acciones de alta intención y recomienda la mejor siguiente experiencia o artículo. |
| [Clasificar mensajes entrantes por intención de exclusión]({{site.baseurl}}/user_guide/brazeai/agents/examples#classify-inbound-messages-for-opt-out-intent) | Clasificación y enrutamiento | Canvas Step Agent | Devuelve un valor booleano estricto que indica si un mensaje es una solicitud de exclusión. |
| [Estandarizar mensajes entrantes en datos estructurados para automatización]({{site.baseurl}}/user_guide/brazeai/agents/examples#standardize-inbound-messages-into-structured-data-for-automation) | Estandarización de datos | Canvas Step Agent | Normaliza SMS o chat entrantes en intención estructurada, entidades y marcadores de cumplimiento para automatización posterior. |
| [Escribir descripciones de alta conversión alineadas con las directrices de marca]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-high-converting-descriptions-that-align-with-brand-guidelines) | Generación de contenido | Catalog Agent | Genera descripciones cortas y alineadas con la marca para cada fila del catálogo. |
| [Proporcionar traducciones basadas en el idioma utilizado por región]({{site.baseurl}}/user_guide/brazeai/agents/examples#provide-translations-based-on-language-used-by-region) | Enriquecimiento de catálogo | Catalog Agent | Localiza cadenas de UI y marketing por configuración regional y límite de caracteres. |
| [Enriquecer elementos de catálogo con descripciones, categorías y etiquetas]({{site.baseurl}}/user_guide/brazeai/agents/examples#enrich-catalog-items-with-descriptions-categories-and-tags) | Enriquecimiento de catálogo | Catalog Agent | Genera descripciones mejoradas, categorías y etiquetas a partir de datos existentes de elementos del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Resumen de ejemplos" }

### Uso de Liquid {#using-liquid}

Incluir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) en las instrucciones de tu agente puede añadir una capa extra de personalización en su respuesta. Puedes especificar la variable Liquid exacta que recibe el agente e incluirla en el contexto de tu indicación. Por ejemplo, en lugar de escribir explícitamente "nombre", puedes usar el fragmento de Liquid {% raw %}`{{${first_name}}}`{% endraw %}:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

En la sección **Logs** de **Agent Console**, puedes revisar los detalles de entrada y salida del agente para entender qué valor se renderiza desde el Liquid.

### Qué datos reciben los agentes {#what-data-agents-receive}

El contexto de un agente no es una memoria conversacional abierta. A diferencia de un asistente de chat, un agente solo ve los datos que le pasas explícitamente en el momento de la invocación; no explora perfiles de usuario, no infiere campos faltantes ni te avisa cuando la información requerida está ausente.

Diseña cada agente como un pipeline deliberado de entrada a salida. Conecta cada punto de datos que el agente necesita usando uno o más de los siguientes métodos:

1. **Liquid en las instrucciones:** Usa plantillas de atributos de usuario ({% raw %}`{{${first_name}}}`{% endraw %}) y [variables de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) ({% raw %}`{{context.${variable_name}}}`{% endraw %}) directamente en la indicación del agente.
2. **+ Agent context:** Selecciona catálogos, pertenencia a Segments, directrices de marca, **All Canvas Context** o datos de interacción de usuarios en Agent Console.
3. [Pasos de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context): Establece o actualiza variables `context.*` en pasos anteriores del Canvas antes de que se ejecute un paso de agente.
4. **Contexto adicional en el paso de agente:** Pasa cualquier valor adicional con plantilla Liquid que no esté especificado en los otros métodos al agente en el momento del envío desde la configuración del paso.

Asegúrate de incluir estas variables de contexto como plantilla Liquid en las instrucciones del agente o de seleccionar **Add All Canvas Context**. Si un valor no se pasa a través de uno de estos canales, el agente no lo recibe. Enumera las entradas requeridas en tus instrucciones o en los [requisitos previos del caso de uso]({{site.baseurl}}/user_guide/brazeai/agents/examples), y verifica las entradas en **Agent Console** > **Logs** después de probar.

![Detalles de un agente que tiene Liquid en sus instrucciones.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

Para Catalog Agents, usa **Fields** en la sección **Output** en lugar de esquema JSON; aun así puedes escribir instrucciones que le pidan al modelo una salida de clave-valor que coincida con esos nombres de campo.

Para más detalles sobre las mejores prácticas de indicaciones, consulta las guías de los siguientes proveedores de modelos:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Salidas {#outputs}

Si creaste tu agente con [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) usando una [plantilla inicial]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), revisa el esquema de salida prerrellenado y edítalo según sea necesario.

### Esquemas básicos {#basic-schemas}

Los esquemas básicos son una salida simple que devuelve un agente. Puede ser una cadena, un número, un booleano, una matriz de cadenas o una matriz de números.

Por ejemplo, si deseas recopilar puntuaciones de sentimiento de los usuarios a partir de un cuestionario de feedback sencillo para determinar qué tan satisfechos están tus clientes después de recibir un producto, puedes seleccionar **Number** como esquema básico para estructurar el formato de salida.

{% alert important %}
Las matrices solo están disponibles para agentes de paso en Canvas, no para agentes de catálogo.
{% endalert %}

![Consola de agente con número seleccionado como esquema básico.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### Esquemas avanzados {#advanced-schemas}

Las opciones de esquema avanzado incluyen la estructuración manual de campos o el uso de JSON.

- **Fields:** Una forma sin código de definir una salida de agente que puedes usar de manera consistente.
- **JSON:** Un enfoque basado en código para crear un formato de salida preciso, donde puedes anidar variables y objetos dentro del esquema JSON. Solo está disponible para agentes de paso en Canvas, no para agentes de catálogo.

Recomendamos usar esquemas avanzados cuando quieras que el agente devuelva una estructura de datos con múltiples valores definidos de forma estructurada, en lugar de una salida de un solo valor. Esto permite que la salida tenga un mejor formato como variable de contexto consistente.

### Salida alternativa {#fallback-output}

Los valores alternativos solo están disponibles para agentes de paso en Canvas. En la sección **Output** de la consola de agente para un agente de paso en Canvas, puedes definir valores que Braze utiliza cuando una invocación falla.

Para esquemas **JSON**, Braze lee el esquema y genera un campo de entrada para cada propiedad de modo que puedas establecer un valor alternativo por clave. Para esquemas de **Fields**, introduces un valor alternativo para cada campo. Para esquemas básicos, introduces un único valor alternativo. Los agentes de paso en Canvas admiten Liquid en los valores alternativos.

Para los pasos de configuración, consulta [Configurar valores alternativos]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values). Para el comportamiento en tiempo de ejecución en Canvas, consulta [Gestión de errores y comportamiento alternativo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

Por ejemplo, puedes usar un formato de salida dentro de un agente diseñado para crear un itinerario de viaje de ejemplo para un usuario basado en un formulario que envió. El formato de salida te permite definir que cada respuesta del agente debe incluir valores para `tripStartDate`, `tripEndDate` y `destination`. Cada uno de estos valores puede extraerse de variables de contexto y colocarse en un paso de mensaje para personalización usando Liquid.

{% tabs %}
{% tab Fields %}

Si deseas dar formato a las respuestas de un cuestionario de feedback sencillo para determinar qué tan probable es que los encuestados recomienden el nuevo sabor de helado de tu restaurante, puedes configurar los siguientes campos para estructurar el formato de salida:

| Nombre del campo | Valor |
| --- | --- |
| **likelihood_score** | Number |
| **explanation** | String |
| **confidence_score** | Number |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquemas avanzados" }

![Consola de agente mostrando tres campos de salida para puntuación de probabilidad, explicación y puntuación de confianza.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

Si deseas recopilar feedback de los usuarios sobre su experiencia gastronómica más reciente en tu cadena de restaurantes, puedes seleccionar **JSON Schema** como formato de salida e insertar el siguiente JSON para devolver un objeto de datos que incluya una variable de sentimiento y una variable de razonamiento.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

{% endtab %}
{% endtabs %}

## Catálogos y campos {#catalogs-and-fields}

Elige catálogos específicos para que un agente los consulte y dale el contexto que necesita para comprender tus productos y otros datos no relacionados con usuarios cuando sea relevante. Los agentes usan herramientas para encontrar solo los elementos relevantes y enviarlos al LLM para minimizar el uso de tokens. Para una mejor recuperación del catálogo, crea una [fuente de conocimiento]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) y agrégala como contexto del agente en lugar de adjuntar el catálogo directamente.

![El catálogo "restaurants" y la columna "Loyalty_Program" seleccionados para que el agente realice búsquedas.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

Cuando implementas un agente de catálogo en un campo de catálogo, habilita el control de entrada obligatoria y elige qué columnas seleccionadas son obligatorias para ejecutarse antes de que el agente se invoque. El agente omite una fila solo cuando una de esas columnas obligatorias está vacía o no existe; por ejemplo, un campo `gender` que aún no se ha rellenado. Las columnas seleccionadas comienzan como obligatorias de forma predeterminada, pero puedes eliminar columnas que pueden estar vacías sin bloquear la ejecución. Esto evita el desperdicio de tokens en datos incompletos.

Los agentes de catálogo también respetan el orden de las columnas cuando los campos de entrada dependen entre sí. Si la columna D debe generarse a partir de las columnas B y C, el agente no se ejecuta en la columna D hasta que B y C contengan valores para esa fila.

Para escenarios de implementación y ejemplos, consulta [Usar agentes de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#use-catalog-agents) y [Mejores prácticas de agentes de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

## Contexto de pertenencia a Segment {#segment-membership-context}

Puedes seleccionar hasta cinco Segments para que el agente haga una referencia cruzada de la pertenencia de cada usuario a un Segment cuando se utilice en un Canvas. Supongamos que tu agente tiene seleccionada la pertenencia al Segment "Loyalty Users" y se usa en un Canvas. Cuando los usuarios entran en un paso de agente, el agente puede verificar de forma cruzada si cada usuario es miembro de cada Segment que especificaste en la consola del agente, y utilizar la pertenencia (o no pertenencia) de cada usuario como contexto para el LLM.

![El Segment "Loyalty Users" seleccionado para el acceso de pertenencia del agente.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Directrices de marca {#brand-guidelines}

Puedes seleccionar [directrices de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) que tu agente debe seguir en sus respuestas. Por ejemplo, si quieres que tu agente genere textos de SMS para animar a los usuarios a suscribirse a una membresía de gimnasio, puedes usar este campo para hacer referencia a tu directriz predefinida de tono audaz y motivacional.

## Historial de interacción específico del usuario {#user-history}

Los datos de interacción de un usuario incluyen sus aperturas, clics y datos de conversión recientes de campañas y Canvas. Por ejemplo, puedes incluir este contexto para que un agente lo consulte cuando se evalúa en Canvas. El historial de interacción específico del usuario también puede ayudar a influir en un agente cuando su tarea es redactar textos de mensajes personalizados.

## Historial de versiones {#version-history}

La Consola de Agente registra una nueva versión cada vez que guardas cambios en el agente. La pestaña **Historial de versiones** enumera cada versión guardada y las ediciones entre guardados.

1. Abre el agente en la Consola de Agente.
2. Selecciona la pestaña **Historial de versiones**.
3. Selecciona una versión para revisar su configuración.

Para inspeccionar qué cambió en una versión, selecciona **Ver**. Braze muestra una diferencia en línea de estilo código que resalta las adiciones y eliminaciones. El contenido eliminado aparece con estilo de tachado en rojo.

![Historial de versiones de la Consola de Agente con el panel de diferencias respecto a la versión anterior abierto, mostrando adiciones en línea en verde y eliminaciones en rojo para las instrucciones del agente.]({% image_buster /assets/img/ai_agent/instruction_differences.png %}){: style="max-width:75%;"}

Si necesitas restaurar instrucciones de una versión anterior, abre **Ver** para esa versión, copia el texto de las instrucciones y pégalo en tu campo **Instrucciones** actual.

{% alert tip %}
En la vista de diferencias en línea, presiona <kbd>⌘</kbd> + <kbd>A</kbd> (macOS) o <kbd>Ctrl</kbd> + <kbd>A</kbd> (Windows) para seleccionar todas las instrucciones sin el marcado de eliminación en rojo, de modo que puedas copiar y restaurar el texto limpio.
{% endalert %}

## Duplicar agentes {#duplicate-agents}

Duplica un agente para probar mejoras o iteraciones en paralelo con el original. Usa el [historial de versiones](#version-history) para revisar o restaurar configuraciones anteriores. Para duplicar un agente:

1. Pasa el cursor sobre la fila del agente y selecciona el menú <i class="fas fa-ellipsis-vertical"></i>.
2. Selecciona **Duplicar**.

## Archivar agentes {#archive-agents}

A medida que crees más agentes personalizados, puedes organizar la página **Agent Management** archivando los agentes que no se estén utilizando activamente. Para archivar un agente:

1. Pasa el cursor sobre la fila del agente y selecciona el menú <i class="fas fa-ellipsis-vertical"></i>.
2. Selecciona **Archive**.