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

- [Permiso]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) para acceder a la **Agent Console** en tu espacio de trabajo. Consulta con tus administradores de Braze si no ves esta opción.
- Permiso para crear y editar agentes de IA personalizados.
- Una idea de lo que quieres que logre el agente. Los agentes de Braze pueden realizar las siguientes acciones:
   - **Mensajería personalizada:** Genera líneas del asunto, titulares, textos para productos u otro tipo de contenido.
   - **Enrutamiento de usuarios:** Dirige a los usuarios en Canvas en función de su comportamiento, preferencias o atributos personalizados.
   - **Gestión de datos:** Calcula valores, mejora las entradas del catálogo o actualiza los campos del perfil.

## Cómo funciona {#how-it-works}

Cuando creas un agente, defines su propósito y estableces las pautas sobre cómo debe comportarse. Una vez que esté en vivo, el agente se puede implementar en Braze para generar textos personalizados, tomar decisiones en tiempo real o actualizar campos del catálogo. Mientras construyes tu agente, puedes guardarlo como borrador, y puedes pausar o actualizar un agente en cualquier momento desde el panel. Cada vez que guardas se crea una nueva versión que puedes revisar en la pestaña [Historial de versiones]({{site.baseurl}}/user_guide/brazeai/agents/reference#version-history).

Los siguientes ejemplos muestran algunas formas de aprovechar los agentes personalizados.

| Caso de uso | Descripción |
| --- | --- |
| Gestión de los comentarios de los clientes | Transmite los comentarios de los usuarios a un agente para que analice el sentimiento y genere mensajes de seguimiento empáticos. Para los usuarios de alto valor, el agente podría escalar la respuesta o incluir ventajas adicionales. |
| Localización de contenido | Traduce el texto del catálogo a otro idioma para campañas globales o ajusta el tono y la longitud para canales específicos de cada región. Por ejemplo, traduce "Classic Clubmaster Sunglasses" al español como "Gafas de sol Classic Clubmaster" o acorta las descripciones para las campañas de SMS. |
| Resumen de reseñas o comentarios | Resume las opiniones o comentarios en un nuevo campo, por ejemplo, asignando puntuaciones de sentimiento como Positivo, Neutro o Negativo, o creando un breve resumen de texto como "La mayoría de los clientes mencionan que el producto se ajusta muy bien, pero señalan que el envío es lento". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cómo funciona" }

## Crear un agente {#create-an-agent}

### Paso 1: Elige un tipo de agente {#step-1-choose-an-agent-type}

Para crear un agente, primero elige el tipo de agente:

1. Ve a **Agent Console**.
2. Elige **Canvas Step Agents** o **Catalog Agents**.

### Paso 2: Elige cómo construir un agente {#step-2-choose-how-to-build-an-agent}

Selecciona **Create agent** y luego elige una de las siguientes opciones:

- **Custom agent** para construir un agente desde cero
- Una opción en **Create an agent with Operator** para usar [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) y aplicar una [plantilla inicial](#agent-templates-built-with-operator)

Si usas Operator, revisa y aprueba sus cambios en el chat antes de continuar con el siguiente paso.

### Paso 3: Configura los detalles {#step-3-set-up-details}

A continuación, configura los detalles de tu agente:

1. Introduce un nombre y una descripción para ayudar a tu equipo a comprender su finalidad.
2. (opcional) Añade etiquetas para filtrar tu agente.
3. Elige el [modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) que utilizará tu agente.
4. Si no estás utilizando el modelo **Braze Auto**, selecciona el [nivel de pensamiento]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels) del modelo. Puedes elegir entre mínimo, bajo, medio o alto. Te recomendamos que comiences con **Minimal** y pruebes las respuestas de tu agente, ajustándolo según sea necesario.
5. Establece un límite de invocaciones diario. De forma predeterminada, este valor está establecido en 250 000, pero puede aumentarse hasta 1 000 000. Si te interesa aumentar el límite por encima de 1 000 000, ponte en contacto con tu administrador de éxito de cliente para obtener más información.

El campo **Daily action credit cost limit** especifica el número máximo de créditos que este agente puede consumir por día. Braze lo calcula a partir de la proporción de créditos por invocación de tu espacio de trabajo para el modelo seleccionado (según tu contrato, que se muestra en la página [Credit Ratios]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage)) multiplicada por el límite de invocaciones diario. La estimación se actualiza cuando cambias el modelo o el límite de invocaciones.

Para gestionar el coste, reduce el límite de invocaciones diario. Para los modelos [trae tu propia clave (BYO)]({{site.baseurl}}/user_guide/brazeai/agents/reference#option-2-bring-your-own-api-key), también puedes cambiar a un modelo de menor coste o reducir el [nivel de pensamiento]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels). **Braze Auto** no permite ajustar el nivel de pensamiento. Consulta el uso real en **Settings** > **Billing** > **Credits Usage** > **Agent Console**.

![Interfaz de la Agent Console para crear un agente personalizado en Braze. La pantalla muestra campos para introducir el nombre y la descripción del agente, seleccionar un modelo y establecer un límite de invocaciones diario.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Paso 4: Escribe las instrucciones {#agent-instructions}

Dale instrucciones al agente. Si usaste una plantilla de Operator, revisa las instrucciones precargadas y edítalas según sea necesario.

Incluye instrucciones sobre lo que debe hacer el agente en situaciones inesperadas o ambiguas. Esto minimiza el riesgo de que la confusión del agente provoque errores. Por ejemplo, en lugar de pedirle al agente solo valores de sentimiento "positivos" o "negativos", pídele que devuelva "indeciso" si no puede decidir.

Consulta las [instrucciones de redacción]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) para conocer las mejores prácticas y los [ejemplos]({{site.baseurl}}/user_guide/brazeai/agents/reference#examples) para inspirarte sobre cómo dar instrucciones a tu agente.

#### Añadir contexto {#add-resources}

{% alert important %}
Los agentes solo reciben los datos que les pasas explícitamente; no buscan en los perfiles de usuario ni te avisan cuando faltan datos necesarios. Usa Liquid en tus instrucciones, selecciona **+ Agent context**, añade [pasos de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) previos en Canvas o pasa contexto adicional en el paso del agente. Para obtener una lista completa de orígenes de datos y orientación de diseño, consulta [Qué datos reciben los agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).
{% endalert %}

Selecciona **+ Agent context** para elegir lo que tu agente puede consultar. Esto incluye:

- [Campos del catálogo]({{site.baseurl}}/user_guide/brazeai/agents/reference#catalogs-and-fields): permite que el agente acceda a los datos de tu catálogo para obtener respuestas más precisas.
- [Fuentes de conocimiento]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources): permite que el agente acceda a los datos del catálogo a través de una fuente de conocimiento para una recuperación más precisa que adjuntar un catálogo directamente.
- [Pertenencia a segmentos]({{site.baseurl}}/user_guide/brazeai/agents/reference#segment-membership-context): permite que el agente personalice las respuestas en función de los segmentos a los que pertenezca el usuario. Puedes seleccionar hasta cinco segmentos.
- [Directrices de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines): consulta las directrices sobre el tono y el estilo de la marca que debe seguir el agente. Por ejemplo, si deseas que tu agente genere un texto SMS para animar a los usuarios a suscribirse a un gimnasio, puedes utilizar este campo para hacer referencia a tu directriz motivacional predefinida en negrita.
- [Todo el contexto de Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables): analiza todos los datos de contexto de Canvas de un usuario cuando se invoque este agente, incluidas las variables que no se mencionan en la sección **Instructions**.
- [Datos de interacción del usuario]({{site.baseurl}}/user_guide/brazeai/agents/reference#user-history): proporciona al agente los datos recientes de aperturas, clics y conversiones de Campaigns y Canvas de cada usuario.

{% alert tip %}
Para los agentes de Canvas, puedes utilizar Liquid en tus instrucciones para hacer referencia a atributos de los usuarios, como su nombre y apellidos, o atributos personalizados. Cualquier variable Liquid en las instrucciones del agente se pasa automáticamente al paso del agente cuando un usuario entra en el paso. Consulta [Qué datos reciben los agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive) para saber cómo pasar contexto de Canvas y datos de perfil de forma deliberada.
{% endalert %}

### Paso 5: Selecciona la salida {#select-output}

En la sección **Output**, puedes organizar y definir la [salida]({{site.baseurl}}/user_guide/brazeai/agents/reference#outputs) del agente mediante esquemas básicos o esquemas avanzados. Si usaste una plantilla de Operator, revisa el esquema de salida precargado y edítalo según sea necesario.

Para obtener los mejores resultados, asegúrate de que lo que especifiques en la sección **Output** coincida con las instrucciones del agente que introdujiste en el [paso 4](#agent-instructions). Por ejemplo, si en las instrucciones del agente mencionaste que deseas un objeto con dos cadenas, asegúrate de especificar un objeto con dos cadenas en la sección **Output**. Si las instrucciones del agente no coinciden con la salida especificada, el agente puede confundirse, agotar el tiempo de espera o generar resultados no deseados.

{% alert tip %}
Cuando utilices un [esquema de salida avanzado]({{site.baseurl}}/user_guide/brazeai/agents/reference#advanced-schemas), añade un campo de cadena llamado `explanation` si quieres que el agente devuelva su razonamiento además de sus otras salidas. Indica al agente en tus [instrucciones](#agent-instructions) que rellene `explanation` cuando eso te ayude a revisar o depurar las respuestas.
{% endalert %}

#### Configurar valores alternativos {#configure-fallback-values}

Los valores alternativos solo están disponibles para los agentes de paso en Canvas. En la sección **Output** de un agente de paso en Canvas, puedes definir valores que Braze utiliza cuando falla una invocación del agente, por ejemplo, cuando el LLM agota el tiempo de espera o devuelve un error de clave de API no válida. Los valores alternativos funcionan como valores predeterminados de personalización. Puedes establecer una línea del asunto estática o un mensaje breve que siga proporcionando una salida útil a los usuarios cuando el agente no pueda ejecutarse.

Los agentes de catálogo no admiten la configuración de valores alternativos en la Agent Console.

![Configuración de salida de la Agent Console que muestra el campo de salida alternativa para un esquema de tipo número.]({% image_buster /assets/img/ai_agent/fallback_output.png %}){: style="max-width:75%;"}

Para los agentes de Canvas, los valores alternativos admiten plantillas de [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) para que puedas hacer referencia a atributos de usuario o variables de contexto en el texto alternativo.

Los campos alternativos se adaptan al formato de salida de tu agente de paso en Canvas:

| Formato de salida | Configuración alternativa |
| --- | --- |
| Cadena, número o booleano | Introduce un único valor alternativo (compatible con Liquid). |
| Campos (esquema avanzado) | Introduce un valor alternativo para cada campo definido en la salida del agente. |
| Esquema JSON (esquema avanzado) | Braze lee tu esquema JSON y genera un campo de entrada para cada propiedad, de modo que puedas definir un valor alternativo por clave. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurar valores alternativos" }

Cuando un agente de paso en Canvas con valores alternativos se ejecuta en un [paso del agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step), Braze renderiza el valor alternativo por usuario y lo almacena en la variable de salida en lugar de `null`. Si no configuras valores alternativos, las invocaciones fallidas dejan la salida de Canvas sin establecer (`null`).

Para conocer el comportamiento en tiempo de ejecución, consulta [Gestión de errores y comportamiento alternativo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

### Paso 6: Prueba el agente {#step-6-test-the-agent}

El panel de **Preview** es una instancia del agente que aparece como un panel lateral dentro de la experiencia de configuración. Puedes utilizarlo para probar el agente mientras lo creas o actualizas, con el fin de experimentarlo de forma similar a como lo harían los usuarios finales. Este paso te ayuda a confirmar que funciona como esperabas y te da la oportunidad de realizar ajustes antes de que entre en funcionamiento.

1. En el campo **Test your agent**, introduce datos de clientes o respuestas de clientes de ejemplo, cualquier cosa que refleje situaciones reales que tu agente tendrá que gestionar.
2. Previsualiza la respuesta del agente para un usuario aleatorio, un usuario existente o un usuario personalizado.
3. Selecciona **Simulate response**. El agente se ejecutará según tu configuración y mostrará su respuesta.

{% alert note %}
Las ejecuciones de prueba cuentan para tu límite de invocaciones diario.
{% endalert %}

![Agent Console que muestra el panel de vista previa para probar un agente personalizado. La interfaz muestra un campo de entradas de muestra con datos de clientes de ejemplo, un botón para ejecutar la prueba y un área de respuesta donde aparece la salida del agente.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Revisa el resultado con ojo crítico. Considera las siguientes preguntas:

- ¿El texto se ajusta a la imagen de marca?
- ¿La lógica de decisión dirige a los clientes según lo previsto?
- ¿Son precisos los valores calculados?

Si algo no funciona correctamente, actualiza la configuración del agente y vuelve a realizar la prueba. Ejecuta varias entradas diferentes para ver cómo se adapta el agente a distintos escenarios, especialmente en casos extremos como la ausencia de datos o respuestas no válidas.

{% alert tip %}
Evita decirle al agente exactamente lo que no quieres que haga. Los LLM pueden seguir generando ese contenido si lo mencionas en las instrucciones.
{% endalert %}

### Paso 7: Utiliza tu agente {#step-7-use-your-agent}

¡Tu agente ya está listo para usar! Para obtener más información, consulta [Implementar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

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
- [Webinar de Braze sobre IA en acción: 3 nuevos ejemplos para la personalización 1:1](https://www.braze.com/resources/webinars-and-events/ai-in-action-use-cases)