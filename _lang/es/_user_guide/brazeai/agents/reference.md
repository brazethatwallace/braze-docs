---
nav_title: Referencia
article_title: Referencia para agentes
description: "Detalles clave de referencia sobre los agentes de Braze."
page_order: 3
---

# Referencia para agentes {#reference-for-agents}

> A medida que crees agentes personalizados, consulta este artículo para obtener más información sobre configuraciones clave, como instrucciones y esquemas de salida. Para una configuración paso a paso, consulta [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents). Para una introducción, consulta [Agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents) y [Preguntas frecuentes]({{site.baseurl}}/user_guide/brazeai/agents/faq).

## Modelos {#models}

Al configurar un agente, puedes elegir el modelo que utilizará para generar respuestas. Tienes dos opciones: utilizar un modelo con tecnología de Braze o traer tu propia clave de API.

{% alert important %}
El modelo **Auto** con tecnología de Braze está optimizado para modelos cuyas capacidades de razonamiento son suficientes para realizar tareas como la búsqueda en catálogos y la pertenencia a segmentos. Si utilizas otros modelos, te recomendamos que realices pruebas para confirmar que tu modelo funciona bien para tu caso de uso. Es posible que tengas que ajustar tus [instrucciones](#writing-instructions) para proporcionar diferentes niveles de detalle o razonamiento paso a paso a modelos con diferentes velocidades y capacidades.
{% endalert %}

### Opción 1: Utiliza un modelo con tecnología de Braze {#option-1-use-a-braze-powered-model}

Esta es la opción más sencilla, sin necesidad de configuración adicional. Braze proporciona acceso directo a modelos de lenguaje grandes (LLM). Para utilizar esta opción, selecciona **Auto**, que utiliza modelos Gemini.

{% alert important %}
Si no ves **Braze Auto** como opción en el menú desplegable **Model** al crear un agente, ponte en contacto con tu administrador de éxito de cliente para saber cómo puedes ser elegible para utilizar el modelo Braze Auto.
{% endalert %}

### Opción 2: Trae tu propia clave de API {#option-2-bring-your-own-api-key}

Con esta opción, puedes conectar tu cuenta de Braze con proveedores como OpenAI, Anthropic o Google Gemini. Si traes tu propia clave de API de un proveedor de LLM, los costes de los tokens se facturan directamente a través de tu proveedor, no a través de Braze.

Recomendamos probar periódicamente los modelos más recientes, ya que los modelos antiguos pueden descontinuarse o quedar obsoletos en unos meses. Asegúrate de tener créditos suficientes con tu proveedor para ejecutar tus agentes a escala. También puedes suscribirte a las notificaciones de la Consola de Agente en [Preferencias de notificación]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) para que te avisen cuando Braze detecte que un modelo ya no está disponible o encuentre problemas de facturación con tu proveedor de LLM.

Para configurarlo:

1. Ve a **Integraciones de socios** > **Socios tecnológicos** y busca tu proveedor.
2. Introduce la clave de API del proveedor.
3. Selecciona **Guardar**.

A continuación, puedes volver a tu agente y seleccionar tu modelo.

Cuando utilices un LLM proporcionado por Braze, los proveedores de dicho modelo actuarán como subencargados del tratamiento de Braze, con sujeción a los términos del Anexo de tratamiento de datos (DPA) entre tú y Braze. Si decides traer tu propia clave de API, el proveedor de tu suscripción a LLM se considerará un proveedor externo en virtud del contrato entre tú y Braze.

#### Niveles de razonamiento {#thinking-levels}

Algunos proveedores de LLM pueden permitirte ajustar el nivel de razonamiento de un modelo seleccionado. Los niveles de razonamiento definen el alcance del pensamiento que el modelo utiliza antes de responder, desde respuestas rápidas y directas hasta cadenas de razonamiento más largas. Esto afecta a la calidad de la respuesta, la latencia y el uso de tokens.

| Nivel | Cuándo usarlo |
|-------|-------------|
| **Mínimo** | Tareas sencillas y bien definidas (como búsqueda en catálogos, clasificación directa). Respuestas más rápidas y menor coste. |
| **Bajo** | Tareas que se benefician de un poco más de razonamiento pero no necesitan un análisis profundo. |
| **Medio** | Tareas de varios pasos o con matices (como analizar varias entradas para recomendar una acción). |
| **Alto** | Razonamiento complejo, casos extremos o cuando necesitas que el modelo trabaje los pasos antes de responder. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Niveles de razonamiento" }

Recomendamos empezar con **Mínimo** y probar las respuestas de tu agente. Luego, puedes ajustar el nivel de razonamiento a **Bajo** o **Medio** si encuentras que el agente tiene dificultades para proporcionar respuestas precisas. En casos excepcionales, puede ser necesario un nivel de razonamiento **Alto**, aunque usar este nivel puede resultar en altos costes de tokens y tiempos de respuesta más largos o mayor riesgo de errores de tiempo de espera. Si tu agente tiene dificultades para equilibrar el razonamiento de varios pasos con tiempos de respuesta razonables, considera dividir tu caso de uso en más de un agente que puedan trabajar juntos en un Canvas o catálogo.

Braze utiliza los mismos rangos de IP para las llamadas LLM salientes que para el contenido conectado. Los rangos se enumeran en la [lista de IP permitidas de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting). Si tu proveedor admite la lista de IP permitidas, puedes restringir la clave a esos rangos para que solo Braze pueda utilizarla.

{% alert important %}
Cuando utilices un LLM proporcionado por Braze, los proveedores de dicho modelo actuarán como subencargados del tratamiento de Braze, con sujeción a los términos del Anexo de tratamiento de datos (DPA) entre tú y Braze. Si decides traer tu propia clave de API, el proveedor de tu suscripción a LLM se considerará un proveedor externo en virtud del contrato entre tú y Braze.
{% endalert %}

#### Determinar qué modelo usar {#determine-which-model-to-use}

Cada proveedor de LLM tiene una combinación ligeramente diferente de capacidades de modelo, costes y niveles de razonamiento. A continuación se presentan algunas directrices generales y prácticas recomendadas:

- Para la eficiencia de costes, prioriza probar modelos con menor coste de tokens antes que modelos con mayor coste. Ajusta a modelos de mayor coste solo si los de menor coste tienen dificultades con el caso de uso o generan resultados inconsistentes o imprecisos.
- Para la eficiencia de velocidad y rendimiento, prioriza probar niveles de razonamiento más bajos antes que niveles más altos. Ajusta a niveles de razonamiento más altos solo si los niveles más bajos tienen dificultades con el caso de uso o generan resultados inconsistentes o imprecisos.
- Si los modelos de menor coste o los niveles de razonamiento más bajos tienen dificultades con el caso de uso o generan resultados inconsistentes o imprecisos, considera ajustar a modelos de mayor coste o niveles de razonamiento más altos.
- Durante las pruebas, asegúrate de equilibrar la fiabilidad y la precisión con el uso de tokens y la duración de la invocación.
- Cada caso de uso puede tener un modelo y nivel de razonamiento óptimos diferentes. Recomendamos realizar pruebas exhaustivas para verificar una calidad consistente sin tiempos de espera agotados.

### Controles de flujo de invocación {#invocation-flow-controls}

Los siguientes controles de flujo de invocación se aplican por espacio de trabajo:

- **Modelo con tecnología de Braze:** 5000 invocaciones por minuto
- **Trae tu propia clave de API:** 5000 invocaciones por minuto

Cuando muchos usuarios entran en un paso de agente a la vez, Braze pone en cola las invocaciones de acuerdo con estos límites, por lo que el procesamiento puede tardar más durante envíos de alto volumen.

### Límites diarios de invocación y créditos {#daily-invocation-and-credit-limits}

Cada agente tiene un límite diario de invocaciones (predeterminado 250 000; máximo 1 000 000 a menos que tu contrato permita un valor superior). Cada invocación, incluidas las vistas previas de la Consola de Agente y las ejecuciones de Canvas de prueba que utilizan **Simulate response**, cuenta para este límite.

En la Consola de Agente, el **Límite diario de coste de créditos de acción** estima los créditos máximos que un agente puede consumir por día. Braze multiplica la **proporción de créditos** por invocación de tu espacio de trabajo para el modelo seleccionado por el límite diario de invocaciones.

### Supervisar el uso de créditos {#monitor-credit-usage}

Ve a **Configuración** > **Facturación** > **Uso de créditos** > **Agent Console** para ver el consumo de créditos, los recuentos de invocaciones y las proporciones de créditos por agente.

Las proporciones de créditos provienen de tu contrato y aparecen en el panel de [Uso de créditos]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage) (pestaña **Credit Ratios** y pestaña **Agent Console**). La estimación se actualiza cuando cambias el modelo o el límite de invocaciones.

Para gestionar el gasto, reduce el límite diario de invocaciones. Para modelos [trae tu propia clave (BYO)](#option-2-bring-your-own-api-key), también puedes elegir un modelo de menor coste o reducir el [nivel de razonamiento](#thinking-levels) para disminuir los costes de tokens del proveedor. **Braze Auto** no admite el ajuste del nivel de razonamiento.

### Errores de límite de velocidad {#rate-limit-errors}

Si el proveedor de LLM devuelve un error de límite de velocidad durante un paso de agente de Canvas o una invocación de agente de catálogo, Braze reintenta continuamente la solicitud utilizando retirada exponencial hasta que la llamada se complete correctamente o Braze determine que no se puede completar.

Cuando se agotan los reintentos de Canvas o catálogo, el panel de detalles de **Logs** muestra **Error** y el mensaje del proveedor (como `Rate limit exceeded`) en **Output**. Los reintentos son visibles en los registros, incluida la primera invocación independientemente de su éxito o fallo final. Para un usuario determinado, si se necesitan cuatro reintentos para obtener finalmente un éxito, puedes buscar el ID de usuario y ver los cinco (el original más cuatro reintentos) en **Logs**, y el original más los tres primeros reintentos mostrarán **Error** con `Rate limit exceeded`.

![Detalles del registro de la Consola de Agente mostrando un error de límite de velocidad excedido en el campo Output.]({% image_buster /assets/img/ai_agent/rate_limit_error_log.png %}){: style="max-width:75%;"}

## Redacción de instrucciones {#writing-instructions}

Las instrucciones son las reglas o directrices que le das al agente (prompt del sistema). Definen cómo debe comportarse el agente cada vez que se ejecuta. Las instrucciones del sistema pueden tener un tamaño máximo de 25 KB.

Si creaste tu agente con [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) usando una [plantilla inicial]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), revisa las instrucciones precargadas y edítalas según sea necesario.

A continuación se incluyen algunas prácticas recomendadas generales para empezar con los prompts:

1. Empieza con el fin en mente. Primero, establece el objetivo.
2. Asigna al modelo un papel o una personalidad («Eres un/una...»).
3. Establece un contexto y unas limitaciones claras (audiencia, extensión, tono, formato).
4. Solicita estructura («Devuelve JSON/lista con viñetas/tabla...»).
5. Muestra, no cuentes. Incluye algunos ejemplos de alta calidad.
6. Divide las tareas complejas en pasos ordenados («Paso 1... Paso 2...»).
7. Anima a razonar («Piensa detenidamente los pasos a seguir y luego da una respuesta final concisa» o «explica brevemente tu decisión»).
8. Prueba, inspecciona e itera. Pequeños ajustes pueden suponer grandes mejoras en la calidad.
9. Maneja los casos extremos, añade barreras de protección e instrucciones de rechazo.
10. Mide y documenta lo que funciona internamente para reutilizarlo y escalarlo.

### Ejemplos {#examples}

Para configuraciones iniciales en la Consola de Agente, consulta [Plantillas de agentes creadas con Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

Para ejemplos completos de instrucciones que puedes copiar o adaptar, consulta la [biblioteca de casos de uso para agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents/examples).

| Ejemplo | Categoría | Tipo de agente | Qué hace |
| --- | --- | --- | --- |
| [Redactar mensajes personalizados basados en el contexto de un usuario]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-personalized-messaging-based-on-a-users-context) | Generación de contenido | Agente de paso en Canvas | Genera asunto/preencabezado de correo electrónico y título/cuerpo de push coordinados para usuarios que buscaron pero no reservaron. |
| [Analizar comentarios de usuarios para determinar los próximos pasos]({{site.baseurl}}/user_guide/brazeai/agents/examples#analyze-user-feedback-to-determine-next-steps) | Estandarización de datos | Agente de paso en Canvas | Clasifica la opinión y el tema de un cuestionario posterior al viaje, y luego recomienda un siguiente paso de CRM. |
| [Categorizar usuarios en contenedores de interés a partir de atributos existentes]({{site.baseurl}}/user_guide/brazeai/agents/examples#categorize-users-into-interest-buckets-from-existing-attributes) | Agente de afinidad | Agente de paso en Canvas | Clasifica a los usuarios en contenedores de interés a partir de atributos y señales de alta intención, y luego recomienda la mejor experiencia o artículo siguiente. |
| [Dirigir usuarios a la ruta de Canvas más relevante a partir de su comportamiento reciente]({{site.baseurl}}/user_guide/brazeai/agents/examples#route-users-to-the-most-relevant-canvas-path-from-recent-behavior) | Agente de afinidad | Agente de paso en Canvas | Infiere la motivación a partir del comportamiento reciente y devuelve la mejor clave de ruta para el siguiente paso en Canvas del usuario. |
| [Asignar usuarios a categorías de interés a partir de acciones de alta intención en tiempo real]({{site.baseurl}}/user_guide/brazeai/agents/examples#assign-users-to-interest-categories-from-real-time-high-intent-actions) | Agente de afinidad | Agente de paso en Canvas | Asigna categorías de interés a partir de acciones de alta intención y recomienda la mejor experiencia o artículo siguiente. |
| [Clasificar mensajes entrantes por intención de exclusión]({{site.baseurl}}/user_guide/brazeai/agents/examples#classify-inbound-messages-for-opt-out-intent) | Clasificación y enrutamiento | Agente de paso en Canvas | Devuelve un booleano estricto que indica si un mensaje es una solicitud de exclusión. |
| [Estandarizar mensajes entrantes en datos estructurados para automatización]({{site.baseurl}}/user_guide/brazeai/agents/examples#standardize-inbound-messages-into-structured-data-for-automation) | Estandarización de datos | Agente de paso en Canvas | Normaliza SMS o chat entrantes en intención estructurada, entidades e indicadores de cumplimiento para automatización posterior. |
| [Redactar descripciones de alta conversión alineadas con las directrices de marca]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-high-converting-descriptions-that-align-with-brand-guidelines) | Generación de contenido | Agente de catálogo | Genera descripciones breves y alineadas con la marca para cada fila del catálogo. |
| [Proporcionar traducciones basadas en el idioma utilizado por región]({{site.baseurl}}/user_guide/brazeai/agents/examples#provide-translations-based-on-language-used-by-region) | Enriquecimiento de catálogo | Agente de catálogo | Localiza cadenas de interfaz de usuario y marketing por configuración regional y límite de caracteres. |
| [Enriquecer elementos del catálogo con descripciones, categorías y etiquetas]({{site.baseurl}}/user_guide/brazeai/agents/examples#enrich-catalog-items-with-descriptions-categories-and-tags) | Enriquecimiento de catálogo | Agente de catálogo | Genera descripciones mejoradas, categorías y etiquetas a partir de los datos existentes de los elementos del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Resumen de ejemplos" }

### Utilizar Liquid {#using-liquid}

Incluir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) en las instrucciones de tu agente puede añadir un nivel adicional de personalización a su respuesta. Puedes especificar la variable Liquid exacta que obtiene el agente e incluirla en el contexto de tu prompt. Por ejemplo, en lugar de escribir explícitamente «nombre», puedes utilizar el fragmento de código Liquid {% raw %}`{{${first_name}}}`{% endraw %}:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

En la sección **Logs** de la **Consola de Agente**, puedes revisar los detalles de la entrada y salida del agente para comprender qué valor se obtiene de Liquid.

### Qué datos reciben los agentes {#what-data-agents-receive}

El contexto del agente no es una memoria conversacional abierta. A diferencia de un asistente de chat, un agente solo ve los datos que le pasas explícitamente en el momento de la invocación; no navega por perfiles de usuario, no infiere campos faltantes ni te avisa cuando falta información obligatoria.

Diseña cada agente como un pipeline deliberado de entrada a salida. Conecta cada dato que el agente necesita utilizando uno o más de los siguientes métodos:

1. **Liquid en las instrucciones:** Incluye atributos de usuario ({% raw %}`{{${first_name}}}`{% endraw %}) y [variables de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) ({% raw %}`{{context.${variable_name}}}`{% endraw %}) directamente en el prompt del agente.
2. **+ Contexto del agente:** Selecciona catálogos, pertenencia a segmentos, directrices de marca, **All Canvas Context** o datos de interacción del usuario en la Consola de Agente.
3. [Pasos de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context): Establece o actualiza variables `context.*` en pasos anteriores del Canvas antes de que se ejecute un paso de agente.
4. **Contexto adicional en el paso de agente:** Pasa cualquier valor adicional con plantilla Liquid que no se haya especificado con los otros métodos al agente en el momento del envío desde la configuración del paso.

Asegúrate de incluir estas variables de contexto como plantilla Liquid en las instrucciones del agente o de seleccionar **Add All Canvas Context**. Si un valor no se pasa a través de uno de estos canales, el agente no lo recibe. Enumera las entradas obligatorias en tus instrucciones o en los [requisitos previos del caso de uso]({{site.baseurl}}/user_guide/brazeai/agents/use_cases), y verifica las entradas en **Consola de Agente** > **Logs** después de las pruebas.

![Los detalles de un agente que tiene Liquid en sus instrucciones.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

Para los agentes de catálogo, utiliza **Fields** en la sección **Output** en lugar de esquema JSON; aun así puedes escribir instrucciones que soliciten al modelo una salida de clave-valor que coincida con esos nombres de campo.

Para obtener más información sobre las prácticas recomendadas para los prompts, consulta las guías de los siguientes proveedores de modelos:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Salidas {#outputs}

Si creaste tu agente con [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) usando una [plantilla inicial]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), revisa el esquema de salida precargado y edítalo según sea necesario.

### Esquemas básicos {#basic-schemas}

Los esquemas básicos son una salida simple que devuelve un agente. Puede ser una cadena, un número, un booleano, una matriz de cadenas o una matriz de números.

Por ejemplo, si deseas recopilar puntuaciones de opinión de los usuarios a partir de un cuestionario de comentarios sencillo para determinar el nivel de satisfacción de tus clientes después de recibir un producto, puedes seleccionar **Number** como esquema básico para estructurar el formato de salida.

{% alert important %}
Las matrices solo están disponibles para agentes de paso en Canvas, no para agentes de catálogo.
{% endalert %}

![Consola de Agente con número seleccionado como esquema básico.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### Esquemas avanzados {#advanced-schemas}

Las opciones de esquema avanzado incluyen la estructuración manual de campos o el uso de JSON.

- **Fields:** Una forma sin código de aplicar una salida de agente que puedes utilizar de manera consistente.
- **JSON:** Un enfoque con código para crear un formato de salida preciso, donde puedes anidar variables y objetos dentro del esquema JSON. Solo disponible para agentes de paso en Canvas, no para agentes de catálogo.

Recomendamos utilizar esquemas avanzados cuando quieras que el agente devuelva una estructura de datos con múltiples valores definidos de manera estructurada, en lugar de una salida de un solo valor. Esto permite que la salida tenga un mejor formato como variable de contexto consistente.

### Salida alternativa {#fallback-output}

Los valores alternativos están disponibles solo para agentes de paso en Canvas. En la sección **Output** de la Consola de Agente para un agente de paso en Canvas, puedes definir valores que Braze utiliza cuando una invocación falla.

Para esquemas **JSON**, Braze lee el esquema y genera un campo de entrada para cada propiedad, de modo que puedas establecer un valor alternativo por clave. Para esquemas **Fields**, introduces un valor alternativo para cada campo. Para esquemas básicos, introduces un único valor alternativo. Los agentes de paso en Canvas admiten Liquid en los valores alternativos.

Para los pasos de configuración, consulta [Configurar valores alternativos]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values). Para el comportamiento en tiempo de ejecución en Canvas, consulta [Gestión de errores y comportamiento alternativo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

Por ejemplo, puedes utilizar un formato de salida dentro de un agente destinado a crear un itinerario de viaje de muestra para un usuario basado en un formulario que envió. El formato de salida te permite definir que cada respuesta del agente debe incluir valores para `tripStartDate`, `tripEndDate` y `destination`. Cada uno de estos valores se puede extraer de las variables de contexto y colocar en un paso de mensaje para personalización usando Liquid.

{% tabs %}
{% tab Campos %}

Si deseas dar formato a las respuestas de un cuestionario de comentarios sencillo para determinar la probabilidad de que los encuestados recomienden el nuevo sabor de helado de tu restaurante, puedes configurar los siguientes campos para estructurar el formato de salida:

| Nombre del campo | Valor |
| --- | --- |
| **likelihood_score** | Número |
| **explanation** | Cadena |
| **confidence_score** | Número |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquemas avanzados" }

![Consola de Agente mostrando tres campos de salida para puntuación de probabilidad, explicación y puntuación de confianza.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab Esquema JSON %}

Si deseas recopilar comentarios de los usuarios sobre su experiencia gastronómica más reciente en tu cadena de restaurantes, puedes seleccionar **JSON Schema** como formato de salida e insertar el siguiente JSON para devolver un objeto de datos que incluya una variable de opinión y una variable de razonamiento.

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

Elige catálogos específicos para que un agente los consulte y proporciónale el contexto necesario para que comprenda tus productos y otros datos que no sean de usuario cuando sea pertinente. Los agentes utilizan herramientas para encontrar solo los elementos relevantes y los envían al LLM para minimizar el uso de tokens. Para una mejor recuperación del catálogo, crea una [fuente de conocimiento]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) y agrégala como contexto del agente en lugar de adjuntar el catálogo directamente.

![El catálogo «restaurants» y la columna «Loyalty_Program» seleccionados para que el agente realice la búsqueda.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

Cuando despliegas un agente de catálogo en un campo de catálogo, habilita el control de entrada obligatoria y elige qué columnas seleccionadas son obligatorias para ejecutarse antes de que el agente se invoque. El agente omite una fila solo cuando una de esas columnas obligatorias está vacía o falta; por ejemplo, un campo `gender` que aún no se ha completado. Las columnas seleccionadas comienzan como obligatorias de forma predeterminada, pero puedes quitar columnas que puedan estar vacías sin bloquear la ejecución. Esto evita el desperdicio de tokens en datos incompletos.

Los agentes de catálogo también respetan el orden de las columnas cuando los campos de entrada dependen unos de otros. Si la columna D debe generarse a partir de las columnas B y C, el agente no se ejecuta en la columna D hasta que B y C contengan valores para esa fila.

Para escenarios de despliegue y ejemplos, consulta [Usar agentes de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#use-catalog-agents) y [Prácticas recomendadas para agentes de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

## Contexto de pertenencia a segmentos {#segment-membership-context}

Puedes seleccionar hasta cinco segmentos para que el agente compare la pertenencia de cada usuario cuando se utiliza el agente en un Canvas. Supongamos que tu agente tiene seleccionada la pertenencia al segmento «Loyalty Users» y que el agente se utiliza en un Canvas. Cuando los usuarios entran en un paso de agente, este puede verificar si cada usuario es miembro de cada segmento que hayas especificado en la consola del agente y utilizar la pertenencia (o no pertenencia) de cada usuario como contexto para el LLM.

![El segmento «Loyalty Users» seleccionado para acceder a la pertenencia del agente.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Directrices de marca {#brand-guidelines}

Puedes seleccionar [directrices de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) que tu agente debe seguir en sus respuestas. Por ejemplo, si deseas que tu agente genere un texto SMS para animar a los usuarios a suscribirse a una membresía de gimnasio, puedes utilizar este campo para hacer referencia a tu directriz motivacional predefinida en negrita.

## Historial de interacción específico del usuario {#user-history}

Los datos de interacción de un usuario incluyen sus aperturas, clics y datos de conversión recientes de campañas y Canvas. Por ejemplo, puedes incluir este contexto para que un agente lo consulte cuando se evalúa en Canvas. El historial de interacción específico del usuario también puede ayudar a influir en un agente cuando su tarea es redactar textos de mensajes personalizados.

## Historial de versiones {#version-history}

La Consola de Agente registra una nueva versión cada vez que guardas cambios en el agente. La pestaña **Historial de versiones** enumera cada versión guardada y las ediciones entre guardados.

1. Abre el agente en la Consola de Agente.
2. Selecciona la pestaña **Historial de versiones**.
3. Selecciona una versión para revisar su configuración.

Para inspeccionar qué cambió en una versión, selecciona **Ver**. Braze muestra una diferencia en línea de estilo código que resalta las adiciones y eliminaciones. El contenido eliminado aparece con estilo de tachado en rojo.

Si necesitas restaurar instrucciones de una versión anterior, abre **Ver** para esa versión, copia el texto de las instrucciones y pégalo en tu campo **Instructions** actual.

{% alert tip %}
En la vista de diferencias en línea, presiona <kbd>⌘</kbd> + <kbd>A</kbd> (macOS) o <kbd>Ctrl</kbd> + <kbd>A</kbd> (Windows) para seleccionar todas las instrucciones sin el marcado de eliminación en rojo, de modo que puedas copiar y restaurar el texto limpio.
{% endalert %}

## Duplicar agentes {#duplicate-agents}

Duplica un agente para probar mejoras o iteraciones en paralelo con el original. Utiliza el [historial de versiones](#version-history) para revisar o restaurar configuraciones anteriores. Para duplicar un agente:

1. Coloca el cursor sobre la fila del agente y selecciona el menú <i class="fas fa-ellipsis-vertical" aria-label="Más opciones"></i>.
2. Selecciona **Duplicar**.

## Archivar agentes {#archive-agents}

A medida que crees más agentes personalizados, puedes organizar la página **Gestión de agentes** archivando los agentes que no se utilicen activamente. Para archivar un agente:

1. Coloca el cursor sobre la fila del agente y selecciona el menú <i class="fas fa-ellipsis-vertical" aria-label="Más opciones"></i>.
2. Selecciona **Archivar**.