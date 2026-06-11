---
nav_title: Crear agentes
article_title: Crear agentes personalizados
description: "Aprende a crear agentes, qué preparar antes de empezar y cómo ponerlos a trabajar en mensajería, toma de decisiones y gestión de datos."
page_order: 1
alias: /creating-agents/
---

# Crear agentes personalizados {#create-custom-agents}

> Aprende a crear agentes personalizados, qué preparar antes de empezar y cómo ponerlos en funcionamiento en mensajería, toma de decisiones y gestión de datos. Para obtener más información general, consulta [Agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents/).

## Requisitos previos {#prerequisites}

Antes de empezar, necesitarás lo siguiente:

- [Permiso]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions) para acceder a la **Consola de Agente** en tu espacio de trabajo. Consulta con tus administradores de Braze si no ves esta opción.
- Permiso para crear y editar agentes de IA personalizados.
- Una idea de lo que quieres que logre el agente. Los agentes de Braze pueden realizar las siguientes acciones:
   - **Mensajería personalizada:** Genera líneas del asunto, titulares, textos para productos u otro tipo de contenido.
   - **Enrutamiento de usuarios:** Dirige a los usuarios en Canvas en función de su comportamiento, preferencias o atributos personalizados.
   - **Gestión de datos:** Calcula valores, mejora las entradas del catálogo o actualiza los campos del perfil.

## Cómo funciona {#how-it-works}

Cuando creas un agente, defines su propósito y estableces las pautas sobre cómo debe comportarse. Una vez que esté en vivo, el agente se puede implementar en Braze para generar textos personalizados, tomar decisiones en tiempo real o actualizar campos del catálogo. Mientras construyes tu agente, puedes guardarlo como borrador, y puedes pausar o actualizar un agente en cualquier momento desde el dashboard.

Los siguientes casos de uso muestran algunas formas de aprovechar los agentes personalizados.

| Caso de uso | Descripción |
| --- | --- |
| Gestión de los comentarios de los clientes | Transmite los comentarios de los usuarios a un agente para que analice el sentimiento y genere mensajes de seguimiento empáticos. Para los usuarios de alto valor, el agente podría escalar la respuesta o incluir ventajas adicionales. |
| Localización de contenido | Traduce el texto del catálogo a otro idioma para campañas globales o ajusta el tono y la longitud para canales específicos de cada región. Por ejemplo, traduce "Classic Clubmaster Sunglasses" al español como "Gafas de sol Classic Clubmaster" o acorta las descripciones para las campañas de SMS. |
| Resumen de reseñas o comentarios | Resume las opiniones o comentarios en un nuevo campo, por ejemplo, asignando puntuaciones como Positivo, Neutro o Negativo, o creando un breve resumen de texto como "La mayoría de los clientes mencionan que el producto se ajusta muy bien, pero señalan que el envío es lento". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cómo funciona" }

## Crear un agente {#create-an-agent}

### Paso 1: Elige un tipo de agente {#step-1-choose-an-agent-type}

Para crear tu agente personalizado:

1. Ve a **Consola de Agente** > **Gestión de agentes** en el dashboard de Braze.
2. Selecciona **Crear agente**.
3. Elige entre crear un agente de Canvas o un agente de catálogo.

### Paso 2: Configura los detalles {#step-2-set-up-details}

A continuación, configura los detalles de tu agente:

1. Introduce un nombre y una descripción para ayudar a tu equipo a comprender su finalidad.
2. (opcional) Añade etiquetas para filtrar tu agente.
3. Elige el [modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) que utilizará tu agente.
4. Si no estás utilizando el modelo **Braze Auto**, selecciona el [nivel de pensamiento]({{site.baseurl}}/user_guide/brazeai/agents/reference/#thinking-levels) del modelo. Puedes elegir entre mínimo, bajo, medio o alto. Te recomendamos que comiences con **Mínimo** y pruebes las respuestas de tu agente, ajustándolo según sea necesario.
5. Establece un límite de invocaciones diario. De forma predeterminada, este valor está establecido en 250 000, pero puede aumentarse hasta 1 000 000. Si te interesa aumentar el límite por encima de 1 000 000, ponte en contacto con tu administrador del éxito del cliente para obtener más información.

![Interfaz de la Consola de Agente para crear un agente personalizado en Braze. La pantalla muestra campos para introducir el nombre y la descripción del agente, seleccionar un modelo y establecer un límite de invocaciones diario.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Paso 3: Escribe las instrucciones {#agent-instructions}

Dale instrucciones al agente. Recomendamos incluir instrucciones sobre lo que debe hacer el agente en situaciones inesperadas o ambiguas. Esto minimiza el riesgo de que la confusión del agente provoque errores. Por ejemplo, en lugar de pedirle al agente solo valores de sentimiento "positivos" o "negativos", pídele que devuelva "indeciso" si no puede decidir.

Consulta las [instrucciones de redacción]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) para conocer las mejores prácticas y los [ejemplos]({{site.baseurl}}/user_guide/brazeai/agents/reference/#examples) para inspirarte sobre cómo dar instrucciones a tu agente.

{% alert tip %}
Para los agentes de Canvas, puedes utilizar Liquid en tus instrucciones para hacer referencia a atributos de los usuarios, como su nombre y apellidos, o atributos personalizados. Cualquier variable Liquid en las instrucciones del agente se pasa automáticamente al paso del agente cuando un usuario entra en el paso.
{% endalert %}

#### Añadir contexto {#add-resources}

Selecciona **+ Contexto del agente** para elegir lo que tu agente puede consultar. Esto incluye lo siguiente:

- [Campos del catálogo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields): Permite que el agente acceda a los datos de tu catálogo para obtener respuestas más precisas.
- [Pertenencia a segmentos]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context): Permite que el agente personalice las respuestas en función de los segmentos a los que pertenezca el usuario. Puedes seleccionar hasta cinco segmentos.
- [Directrices de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/): Consulta las directrices sobre el tono y el estilo de la marca que debe seguir el agente. Por ejemplo, si deseas que tu agente genere un texto SMS para animar a los usuarios a inscribirse en un gimnasio, puedes utilizar este campo para hacer referencia a tu directriz motivacional predefinida en negrita.
- [Todo el contexto de Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/): Analiza todos los datos de contexto de Canvas de un usuario cuando se invoque este agente, incluidas las variables que no se mencionan en la sección **Instrucciones**.
- [Datos de interacción del usuario]({{site.baseurl}}/user_guide/brazeai/agents/reference/#user-history): Proporciona al agente los datos recientes de aperturas, clics y conversiones de Campaign y Canvas de cada usuario.

### Paso 4: Selecciona la salida {#select-output}

En la sección **Salida**, puedes organizar y definir la [salida]({{site.baseurl}}/user_guide/brazeai/agents/reference/#outputs) del agente mediante esquemas básicos o esquemas avanzados.

Para obtener los mejores resultados, asegúrate de que lo que especifiques en la sección **Salida** coincida con las instrucciones del agente que introdujiste en el [paso 3](#agent-instructions). Por ejemplo, si en las instrucciones del agente mencionaste que deseas un objeto con dos cadenas, asegúrate de especificar un objeto con dos cadenas en la sección **Salida**. Si las instrucciones del agente no coinciden con la salida especificada, el agente puede confundirse, agotar el tiempo de espera o generar resultados no deseados.

{% alert tip %}
Cuando utilices un [esquema de salida avanzado]({{site.baseurl}}/user_guide/brazeai/agents/reference/#advanced-schemas), añade un campo de cadena llamado `explanation` si quieres que el agente devuelva su razonamiento además de sus otras salidas. Indica al agente en tus [instrucciones](#agent-instructions) que rellene `explanation` cuando eso te ayude a revisar o depurar las respuestas.
{% endalert %}

### Paso 5: Prueba y crea el agente {#step-5-test-and-create-the-agent}

El panel de **vista previa** es una instancia del agente que aparece como un panel lateral dentro de la experiencia de configuración. Puedes utilizarlo para probar el agente mientras lo creas o actualizas, con el fin de experimentarlo de forma similar a como lo harían los usuarios finales. Este paso te ayuda a confirmar que funciona como esperabas y te da la oportunidad de realizar ajustes antes de que entre en funcionamiento.

1. En el campo **Prueba tu agente**, introduce datos de clientes o respuestas de clientes de ejemplo, cualquier cosa que refleje situaciones reales que tu agente tendrá que gestionar.
2. Previsualiza la respuesta del agente para un usuario aleatorio, un usuario existente o un usuario personalizado.
3. Selecciona **Simular respuesta**. El agente se ejecutará según tu configuración y mostrará su respuesta.

{% alert note %}
Las ejecuciones de prueba cuentan para tu límite de invocaciones diario.
{% endalert %}

![Consola de Agente que muestra el panel de vista previa para probar un agente personalizado. La interfaz muestra un campo de entradas de muestra con datos de clientes de ejemplo, un botón Ejecutar prueba y un área de respuesta donde aparece la salida del agente.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Revisa el resultado con ojo crítico. Considera las siguientes preguntas:

- ¿El texto se ajusta a la imagen de marca?
- ¿La lógica de decisión dirige a los clientes según lo previsto?
- ¿Son precisos los valores calculados?

Si algo no funciona correctamente, actualiza la configuración del agente y vuelve a realizar la prueba. Ejecuta varias entradas diferentes para ver cómo se adapta el agente a distintos escenarios, especialmente en casos extremos como la ausencia de datos o respuestas no válidas.

{% alert tip %}
Evita decirle al agente exactamente lo que no quieres que haga. Los LLM pueden seguir generando ese contenido si lo mencionas en las instrucciones.
{% endalert %}

### Paso 6: Utiliza tu agente {#step-6-use-your-agent}

¡Tu agente ya está listo para usar! Para obtener más información, consulta [Implementar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Recursos relacionados {#related-resources}

- [Referencia para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
- [Preguntas frecuentes]({{site.baseurl}}/user_guide/brazeai/agents/faq/)
- [Seminario web de Braze sobre IA en acción: 3 nuevos casos de uso para la personalización 1:1](https://www.braze.com/resources/webinars-and-events/ai-in-action-use-cases)