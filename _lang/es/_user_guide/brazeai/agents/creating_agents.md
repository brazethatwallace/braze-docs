---
nav_title: Crear agentes
article_title: Crear agentes personalizados
description: "Aprende a crear agentes, qué preparar antes de empezar y cómo ponerlos a trabajar en mensajería, toma de decisiones y gestión de datos."
page_order: 1
alias: /creating-agents/
---

# Crear agentes personalizados {#create-custom-agents}

> Aprende a crear agentes personalizados, qué preparar antes de empezar y cómo ponerlos a trabajar en mensajería, toma de decisiones y gestión de datos. Para obtener más información general, consulta [Agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents).

## Requisitos previos {#prerequisites}

Antes de empezar, necesitarás lo siguiente:

- [Permiso]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) para acceder a la **Consola de agentes** en tu espacio de trabajo. Consulta con los administradores de Braze si no ves esta opción.
- Permiso para crear y editar agentes de IA personalizados.
- Una idea de lo que quieres que el agente logre. Los agentes de Braze pueden realizar las siguientes acciones:
   - **Mensajería personalizada:** genera líneas del asunto, encabezados, textos dentro del producto u otro contenido.
   - **Enrutamiento de usuarios:** enruta a los usuarios en Canvas según su comportamiento, preferencias o atributos personalizados.
   - **Gestión de datos:** calcula valores, enriquece entradas de catálogo o actualiza campos de perfil.

## Cómo funciona {#how-it-works}

Cuando creas un agente, defines su propósito y estableces las directrices para su comportamiento. Una vez en vivo, el agente puede desplegarse en Braze para generar textos personalizados, tomar decisiones en tiempo real o actualizar campos del catálogo. Mientras construyes tu agente, puedes guardarlo como borrador y actualizarlo en cualquier momento desde el panel. Cada guardado crea una nueva versión que puedes revisar en la pestaña [Historial de versiones]({{site.baseurl}}/user_guide/brazeai/agents/reference#version-history).

Los siguientes ejemplos muestran algunas formas de aprovechar los agentes personalizados.

| Ejemplo | Descripción |
| --- | --- |
| Gestión de comentarios de clientes | Envía los comentarios de los usuarios a un agente para analizar el sentimiento y generar mensajes de seguimiento empáticos. Para usuarios de alto valor, el agente puede escalar la respuesta o incluir beneficios. |
| Localizar contenido | Traduce texto del catálogo a otro idioma para campañas globales, o ajusta el tono y la extensión para canales específicos de cada región. Por ejemplo, traduce "Classic Clubmaster Sunglasses" al español como "Gafas de sol Classic Clubmaster", o acorta las descripciones para campañas de SMS. |
| Resumir reseñas o comentarios | Resume el sentimiento o los comentarios en un nuevo campo, como asignar puntuaciones de sentimiento tales como Positivo, Neutral o Negativo, o crear un breve resumen de texto como "La mayoría de los clientes mencionan un gran ajuste, pero señalan envíos lentos." |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cómo funciona" }

## Crear un agente {#create-an-agent}

### Paso 1: Elige un tipo de agente {#step-1-choose-an-agent-type}

Para crear un agente, primero elige tu tipo de agente:

1. Ve a **Agent Console**.
2. Elige **Canvas Step Agents** o **Catalog Agents**.

### Paso 2: Elige cómo construir un agente {#step-2-choose-how-to-build-an-agent}

Selecciona **Create agent** y luego elige una de las siguientes opciones:

- **Custom agent** para construir un agente desde cero
- Una opción en **Create an agent with Operator** para usar [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) y aplicar una [plantilla inicial](#agent-templates-built-with-operator)

Si usas Operator, revisa y aprueba sus cambios en el chat antes de continuar con el siguiente paso.

### Paso 3: Configura los detalles {#step-3-set-up-details}

A continuación, configura los detalles de tu agente:

1. Ingresa un nombre y una descripción para ayudar a tu equipo a entender su propósito.
2. (opcional) Añade etiquetas para filtrar tu agente.
3. Elige el [modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) que usará tu agente.
4. Si no estás usando el modelo **Braze Auto**, selecciona el [nivel de razonamiento]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels) del modelo. Puedes elegir entre mínimo, bajo, medio o alto. Recomendamos comenzar con **Minimal** y probar las respuestas de tu agente, ajustando según sea necesario.
5. Establece un límite diario de invocaciones. De forma predeterminada, este valor está establecido en 250.000, pero puede elevarse a 1.000.000. Si te interesa aumentar el límite por encima de 1.000.000, contacta a tu administrador de éxito de cliente para obtener más información. Establece el límite lo suficientemente alto para el tamaño de audiencia planificado después de las pruebas. Un límite demasiado bajo causa fallos por límite diario (que no consumen créditos pero sí aplican valores alternativos o dejan la salida como `null`).

El campo **Daily action credit cost limit** especifica el número máximo de créditos que este agente puede consumir por día. Braze lo calcula a partir de la proporción de créditos por invocación de tu espacio de trabajo para el modelo seleccionado (según tu contrato, que se muestra en la página [Credit Ratios]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage)) multiplicado por el límite diario de invocaciones. La estimación se actualiza cuando cambias el modelo o el límite de invocaciones.

Para gestionar el costo, reduce el límite diario de invocaciones. Para los modelos [bring-your-own (BYO)]({{site.baseurl}}/user_guide/brazeai/agents/reference#option-2-bring-your-own-api-key), también puedes cambiar a un modelo de menor costo o reducir el [nivel de razonamiento]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels). **Braze Auto** no permite ajustar el nivel de razonamiento. Realiza el seguimiento del uso real en **Settings** > **Billing** > **Credits Usage** > **Agent Console**.

![Interfaz de Agent Console para crear un agente personalizado en Braze. La pantalla muestra campos para ingresar el nombre y la descripción del agente, seleccionar un modelo y establecer un límite diario de invocaciones.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Paso 4: Escribe las instrucciones {#agent-instructions}

Dale instrucciones al agente. Si usaste una plantilla de Operator, revisa las instrucciones precargadas y edítalas según sea necesario.

Incluye instrucciones sobre lo que el agente debe hacer en escenarios inesperados o ambiguos. Esto minimiza el riesgo de que la confusión del agente genere errores. Por ejemplo, en lugar de pedirle al agente solo valores de sentimiento "positivo" o "negativo", pídele que devuelva "unsure" si no puede decidir.

Consulta las [instrucciones de escritura]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) para conocer las mejores prácticas y los [ejemplos]({{site.baseurl}}/user_guide/brazeai/agents/reference#examples) para inspirarte sobre cómo formular las indicaciones de tu agente.

#### Agregar contexto {#add-resources}

{% alert important %}
Los agentes solo reciben datos que les pasas explícitamente: no buscan en los perfiles de usuario ni te advierten cuando faltan datos necesarios. Usa Liquid en tus instrucciones, selecciona **+ Agent context**, añade [pasos de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) anteriores en Canvas, o pasa contexto adicional en el paso del agente. Para ver la lista completa de orígenes de datos y orientación de diseño, consulta [Qué datos reciben los agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).
{% endalert %}

Selecciona **+ Agent context** para elegir qué puede referenciar tu agente. Esto incluye:

- [Campos de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/reference#catalogs-and-fields): Dale al agente acceso a los datos de tu catálogo para obtener respuestas más precisas.
- [Fuentes de conocimiento]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources): Dale al agente acceso a los datos del catálogo a través de una fuente de conocimiento para una recuperación más precisa que adjuntar un catálogo directamente.
- [Pertenencia a Segments]({{site.baseurl}}/user_guide/brazeai/agents/reference#segment-membership-context): Permite que el agente personalice las respuestas según a qué Segments pertenece un usuario. Puedes seleccionar hasta cinco Segments.
- [Directrices de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines): Referencia la voz y las directrices de estilo de la marca que el agente debe seguir. Por ejemplo, si quieres que tu agente genere texto de SMS para animar a los usuarios a suscribirse a una membresía de gimnasio, puedes usar este campo para referenciar tu directriz predefinida de tono motivacional y audaz.
- [Todo el contexto de Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables): Analiza todos los datos de contexto de Canvas para un usuario cuando se invoca este agente, incluyendo cualquier variable que no esté referenciada en la sección **Instructions**.
- [Datos de interacción del usuario]({{site.baseurl}}/user_guide/brazeai/agents/reference#user-history): Proporciona al agente los datos recientes de aperturas, clics y conversiones de Campaigns y Canvas de cada usuario.

{% alert tip %}
Para los agentes de Canvas, puedes usar Liquid en tus instrucciones para referenciar atributos de usuario, como su nombre y apellido, o atributos personalizados. Cualquier variable Liquid en las instrucciones del agente se pasa automáticamente al paso del agente cuando un usuario entra en el paso. Consulta [Qué datos reciben los agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive) para saber cómo pasar contexto de Canvas y datos de perfil de forma deliberada.
{% endalert %}

### Paso 5: Selecciona la salida {#select-output}

En la sección **Output**, puedes organizar y definir la [salida]({{site.baseurl}}/user_guide/brazeai/agents/reference#outputs) del agente mediante esquemas básicos o esquemas avanzados. Si usaste una plantilla de Operator, revisa el esquema de salida precargado y edítalo según sea necesario.

Para obtener los mejores resultados, asegúrate de que lo que especificas en la sección **Output** coincida con las instrucciones del agente que ingresaste en el [Paso 4](#agent-instructions). Por ejemplo, si mencionaste en las instrucciones del agente que deseas un objeto con dos cadenas, asegúrate de especificar un objeto con dos cadenas en la sección **Output**. Si las instrucciones de tu agente no se alinean con la salida especificada, el agente puede confundirse, agotar el tiempo de espera o generar salidas no deseadas.

{% alert tip %}
Cuando uses un [esquema de salida avanzado]({{site.baseurl}}/user_guide/brazeai/agents/reference#advanced-schemas), añade un campo de tipo cadena llamado `explanation` si quieres que el agente devuelva su razonamiento además de las otras salidas. Indica al agente en tus [instrucciones](#agent-instructions) que complete `explanation` cuando esto te ayude a revisar o depurar las respuestas.
{% endalert %}

#### Configurar valores alternativos {#configure-fallback-values}

Los valores alternativos solo están disponibles para los agentes de paso en Canvas. En la sección **Output** de un agente de paso en Canvas, puedes definir valores que Braze utiliza cuando falla una invocación del agente, por ejemplo, cuando el LLM agota el tiempo de espera o devuelve un error de clave de API no válida. Los valores alternativos funcionan como valores predeterminados de personalización. Podrías configurar una línea del asunto estática o un mensaje corto que aún proporcione a los usuarios una salida útil cuando el agente no pueda ejecutarse.

Los agentes de catálogo no permiten configurar valores alternativos en Agent Console.

![Configuración de salida de Agent Console que muestra el campo de salida alternativa para un esquema de tipo numérico.]({% image_buster /assets/img/ai_agent/fallback_output.png %}){: style="max-width:75%;"}

Para los agentes de Canvas, los valores alternativos son compatibles con plantillas de [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) para que puedas referenciar atributos de usuario o variables de contexto en el texto alternativo.

Los campos alternativos se adaptan al formato de salida de tu agente de paso en Canvas:

| Formato de salida | Configuración alternativa |
| --- | --- |
| Cadena, número o booleano | Ingresa un solo valor alternativo (compatible con Liquid). |
| Campos (esquema avanzado) | Ingresa un valor alternativo para cada campo definido en la salida del agente. |
| Esquema JSON (esquema avanzado) | Braze lee tu esquema JSON y genera un campo de entrada para cada propiedad, para que puedas definir un valor alternativo por clave. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurar valores alternativos" }

Cuando un agente de paso en Canvas con valores alternativos se ejecuta en un [paso de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step), Braze renderiza el valor alternativo por usuario y lo almacena en la variable de salida en lugar de `null`. Si no configuras valores alternativos, las invocaciones fallidas dejan la salida de Canvas sin establecer (`null`).

Para el comportamiento en tiempo de ejecución, consulta [Manejo de errores y comportamiento alternativo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

### Paso 6: Prueba el agente {#step-6-test-the-agent}

El panel **Preview** es una instancia del agente que aparece como un panel lateral dentro de la experiencia de configuración. Puedes usar esta sección para probar el agente mientras lo creas o actualizas, experimentándolo de una forma similar a los usuarios finales. Este paso te ayuda a confirmar que se está comportando como esperas y te da la oportunidad de afinar antes de que entre en vivo.

1. En el campo **Test your agent**, ingresa datos de clientes de ejemplo o respuestas de clientes, cualquier cosa que refleje escenarios reales que tu agente manejará.
2. Previsualiza la respuesta del agente para un usuario aleatorio, un usuario existente o un usuario personalizado.
3. Selecciona **Simulate response**. El agente se ejecutará según tu configuración y mostrará su respuesta.

{% alert note %}
Las ejecuciones de prueba cuentan para tu límite diario de invocaciones.
{% endalert %}

![Agent Console mostrando el panel de vista previa para probar un agente personalizado. La interfaz muestra un campo de entradas de muestra con datos de clientes de ejemplo, un botón para ejecutar la prueba y un área de respuesta donde aparece la salida del agente.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Revisa la salida con ojo crítico. Considera las siguientes preguntas:

- ¿El texto se siente acorde con la marca?
- ¿La lógica de decisión dirige a los clientes como se pretende?
- ¿Los valores calculados son precisos?

Si algo no se siente bien, actualiza la configuración del agente y prueba de nuevo. Ejecuta algunas entradas diferentes para ver cómo se adapta el agente en distintos escenarios, especialmente en casos límite como la ausencia de datos o respuestas no válidas.

{% alert tip %}
Evita decirle al agente exactamente lo que no quieres que haga. Los LLM aún pueden generar ese contenido si lo mencionas en las instrucciones.
{% endalert %}

### Paso 7: Usa tu agente {#step-7-use-your-agent}

¡Tu agente ya está listo para usar! Para más detalles, consulta [Desplegar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

## Plantillas de agentes creadas con Operator {#agent-templates-built-with-operator}

Operator puede preconfigurar instrucciones, campos de salida y contexto para las siguientes plantillas iniciales de la Agent Console. Elige una plantilla en Operator o pídele a Operator que aplique una por nombre.

### Plantillas de agentes de paso en Canvas {#canvas-step-agent-templates}

| Plantilla | Descripción | Ejemplo de salida |
| --- | --- | --- |
| Redactor personalizado | Genera textos de mensajes específicos para cada canal a partir de atributos de usuario, contexto de Canvas y directrices de marca | Línea del asunto y preencabezado del correo electrónico; título y cuerpo del push |
| Analista de comentarios | Analiza comentarios abiertos de cuestionarios o soporte y los convierte en campos estructurados para la ramificación en Canvas | Sentimiento, tema, siguiente acción recomendada |
| Enrutador de recorridos | Dirige a cada usuario a la ruta de Canvas más relevante en función de su perfil y el contexto del recorrido | Nombre de la ruta o booleano para pasos de división de decisiones |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Plantillas de agentes de paso en Canvas" }

### Plantillas de agentes de catálogo {#catalog-agent-templates}

| Plantilla | Descripción | Ejemplo de salida |
| --- | --- | --- |
| Redactor de descripciones | Escribe descripciones de marketing breves a partir de columnas existentes del catálogo | Descripción de producto o destino |
| Categorizador de elementos | Asigna categorías o etiquetas a partir de los datos de las filas | Etiquetas de categoría para filtrado y recomendaciones |
| Traductor de localización | Traduce cadenas del catálogo a los idiomas de destino dentro de los límites de caracteres | Texto localizado por idioma |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Plantillas de agentes de catálogo" }

## Recursos relacionados {#related-resources}

- [Referencia para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference)
- [Preguntas frecuentes]({{site.baseurl}}/user_guide/brazeai/agents/faq)
- [Webinar de Braze sobre IA en acción: 3 nuevos ejemplos de personalización 1:1](https://www.braze.com/resources/webinars-and-events/ai-in-action-use-cases)