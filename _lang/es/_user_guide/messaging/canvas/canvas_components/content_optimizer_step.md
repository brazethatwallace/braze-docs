---
nav_title: Optimizador de contenidos
article_title: Paso del Optimizador de contenidos
alias: "/content_optimizer_step/"
page_order: 5
description: "El paso del Optimizador de contenidos te permite configurar y probar múltiples versiones de componentes de contenido dentro de un solo paso. Te ayuda a experimentar con variaciones de contenido y optimiza automáticamente hacia las combinaciones de mejor rendimiento a lo largo del tiempo."
page_type: reference

---

# Paso del Optimizador de contenidos {#content-optimizer-step}

> El paso del Optimizador de contenidos te permite configurar y probar múltiples versiones de componentes de contenido dentro de un solo paso. Te ayuda a experimentar con variaciones de contenido y optimiza automáticamente hacia las combinaciones de mejor rendimiento a lo largo del tiempo. Para una introducción, consulta [Optimizador de contenidos]({{site.baseurl}}/user_guide/brazeai/content_optimizer).

{% alert important %}
El Optimizador de contenidos está actualmente en beta. Para obtener ayuda para empezar, ponte en contacto con tu CSM or administrador de éxito de cliente or administrador de éxito de cliente.
{% endalert %}

## Crear un paso de Otimizador de Contenido {#create-a-content-optimizer-step}

Para obtener mejores resultados, usa el Otimizador de Contenido en Canvas donde los usuarios entren al paso gradualmente a lo largo del tiempo. Si todos los usuarios entran al paso a la vez, el Otimizador de Contenido no tendrá tiempo de aprender de los resultados iniciales.

### Paso 1: Añadir un paso {#step-1-add-a-step}

Arrastra y suelta el componente **Otimizador de Contenido** desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> de suma en la parte inferior de un paso y selecciona **Otimizador de Contenido**.

### Paso 2: Crear tu mensaje base {#step-2-create-your-base-message}

El mensaje base es el punto de partida para tu paso. Las variantes de cada componente de contenido se insertan dinámicamente en función de las combinaciones definidas en la pestaña **Configuración del Otimizador de Contenido**.

{% alert note %}
Durante el periodo beta, los canales compatibles son correo electrónico, notificaciones push y servicio de mensajes cortos/MMS/RCS.
{% endalert %}

{% tabs local %}
{% tab Correo electrónico %}

Desde la pestaña **Canales de mensajería**, selecciona **Correo electrónico** y crea tu mensaje de correo electrónico base. Consulta nuestra sección dedicada de [correo electrónico]({{site.baseurl}}/user_guide/channels/email) para obtener ayuda.

El Otimizador de Contenido utiliza la configuración de envío (como el dominio de correo electrónico y la dirección de respuesta) especificada en esta variante para enviar todos los mensajes. Puedes empezar con un nuevo diseño o seleccionar una plantilla existente para este mensaje. En este paso, considera qué componentes del mensaje deseas optimizar. Los defines en el [paso 4](#step-4).

Los componentes compatibles para optimizar incluyen:

- Asunto
- Encabezado del cuerpo
- Contenido del cuerpo
- CTA principal

{% endtab %}
{% tab Notificaciones push %}

Desde la pestaña **Canales de mensajería**, selecciona **Notificaciones push** y crea tu notificación push base. Consulta nuestra sección dedicada de [push]({{site.baseurl}}/user_guide/channels/push) para obtener ayuda.

El Otimizador de Contenido utiliza las plataformas push seleccionadas especificadas en esta variante para enviar todos los mensajes. Puedes empezar con un nuevo diseño o seleccionar una plantilla existente para este mensaje. En este paso, considera qué componentes del mensaje deseas optimizar. Los defines en el [paso 4](#step-4).

Los componentes compatibles para optimizar incluyen:

- Título
- Mensaje

{% endtab %}
{% tab servicio de mensajes cortos/MMS/RCS %}

Desde la pestaña **Canales de mensajería**, selecciona **servicio de mensajes cortos/MMS/RCS** y crea tu mensaje base. Consulta nuestra sección dedicada de [servicio de mensajes cortos/MMS/RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs) para obtener ayuda.

El Otimizador de Contenido utiliza los detalles de **Contenido** y **Mensaje** especificados en esta variante para enviar todos los mensajes. Puedes empezar con un nuevo diseño o seleccionar una plantilla existente para este mensaje. En este paso, considera qué componentes del mensaje deseas optimizar. Los defines en el [paso 4](#step-4).

Los componentes compatibles para optimizar incluyen:

- Gancho
- Cuerpo
- CTA

{% endtab %}
{% endtabs %}

### Paso 3: Especificar la configuración de entrega {#step-3-specify-delivery-settings}

En la pestaña **Configuración de entrega**, puedes especificar si el paso debe usar sincronización inteligente o validaciones de entrega. Para más detalles, consulta [Editar configuración de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings) en Paso de mensaje.

### Paso 4: Añadir componentes de contenido y variantes {#step-4}

Los componentes de contenido son los elementos individuales de tu mensaje que deseas probar, como diferentes líneas del asunto o títulos. Estos componentes te permiten generar múltiples versiones de un mensaje y optimizar automáticamente en función del rendimiento a lo largo del tiempo.

- **Correo electrónico:** puedes añadir hasta tres componentes de contenido por paso y hasta cinco variantes por componente, para un total de 125 combinaciones de contenido únicas.
- **Notificaciones push:** puedes añadir hasta dos componentes por paso y hasta cinco variantes por componente, para un total de 25 combinaciones de contenido únicas.
- **servicio de mensajes cortos/MMS/RCS:** puedes añadir hasta dos componentes de contenido por paso y hasta cinco variantes por componente, para un total de 25 combinaciones de contenido únicas.

Cuando usas **Generar sugerencias de IA**, Braze envía contenido a OpenAI para generar ideas de variantes. La asignación de tráfico en el momento del envío no utiliza OpenAI. Para obtener detalles sobre qué datos se envían y cómo se utilizan, consulta [OpenAI y Otimizador de Contenido]({{site.baseurl}}/user_guide/brazeai/content_optimizer#openai-and-content-optimizer).

![Opciones para añadir y configurar componentes de contenido en la interfaz del Otimizador de Contenido. La interfaz muestra componentes seleccionables como Asunto, Encabezado del cuerpo, Contenido del cuerpo y CTA principal, cada uno con campos para introducir diferentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Paso 4.1: Configurar componentes de contenido {#step-41-configure-content-components}

Para configurar los componentes, ve a la pestaña **Configuración del Otimizador de Contenido**.

{% tabs local %}
{% tab Correo electrónico %}

Elige qué componentes deseas optimizar para los mensajes de correo electrónico. Las opciones compatibles son:

- Asunto
- Encabezado del cuerpo
- Contenido del cuerpo
- CTA principal

Para cada componente seleccionado, define un conjunto de versiones alternativas de ese contenido (variantes). Usa variantes claras y distintas que difieran en tono, estructura o contenido. Esto ayuda al Otimizador de Contenido a identificar los de mejor rendimiento de manera más eficaz. Puedes:
  - Escribir tus propias variantes manualmente.
  - Usar sugerencias generadas por IA para explorar nuevas opciones rápidamente.

![Interfaz de configuración del Otimizador de Contenido que muestra opciones para añadir y configurar componentes de contenido para la optimización de correo electrónico. Cada componente tiene campos de entrada para introducir diferentes variantes. El texto visible incluye nombres de componentes y campos para introducir texto de variantes.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab Notificaciones push %}

Elige qué componentes deseas optimizar para las notificaciones push. Las opciones compatibles son:
- Título
- Mensaje

Para cada componente seleccionado, define un conjunto de versiones alternativas de ese contenido (variantes). Usa variantes claras y distintas que difieran en tono, estructura o contenido. Esto ayuda al Otimizador de Contenido a identificar los de mejor rendimiento de manera más eficaz. Puedes:
  - Escribir tus propias variantes manualmente.
  - Usar sugerencias generadas por IA para explorar nuevas opciones rápidamente.

![Configuración del Otimizador de Contenido que muestra opciones para añadir y configurar componentes de contenido para la optimización push.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% tab servicio de mensajes cortos/MMS/RCS %}

Después de seleccionar tu grupo de suscripción y tipo de mensaje (si corresponde), elige qué componentes deseas optimizar para servicio de mensajes cortos/MMS/RCS. Las opciones compatibles son:
- Gancho
- Cuerpo
- CTA
{% alert note %}
Después de que se lance un paso de Otimizador de Contenido para servicio de mensajes cortos/MMS/RCS, no puedes actualizar el grupo de suscripción ni el tipo de mensaje.
{% endalert %}
Para cada componente seleccionado, define un conjunto de versiones alternativas de ese contenido (variantes). Usa variantes claras y distintas que difieran en tono, estructura o contenido. Esto ayuda al Otimizador de Contenido a identificar los de mejor rendimiento de manera más eficaz. Puedes:
  - Escribir tus propias variantes manualmente.
  - Usar sugerencias generadas por IA para explorar nuevas opciones rápidamente.

![Configuración del Otimizador de Contenido que muestra opciones para añadir y configurar componentes de contenido para la optimización SMS/MMS/RCS.]({% image_buster /assets/img/content_optimizer/add_content_components_sms_rcs_mms.png %})

{% endtab %}
{% endtabs %}

#### Paso 4.2: Añadir Liquid a tu mensaje {#step-42-add-liquid-to-your-message}

Después de definir al menos dos variantes para cada componente, copia la etiqueta de Liquid asociada para cada uno y pégala en la ubicación correspondiente en tu mensaje base.

- Por ejemplo, si estás optimizando la línea del asunto, pega la etiqueta {% raw %}`{% message_component "Subject" %}`{% endraw %} en el campo de asunto del creador de correo electrónico.
- También puedes incluir etiquetas de componente dentro de texto más largo para probar solo una parte del componente. Por ejemplo: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Opciones para añadir y configurar componentes de contenido como Asunto, Encabezado del cuerpo, Contenido del cuerpo y CTA principal. Cada componente tiene campos para introducir diferentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Si no añades una etiqueta de Liquid para un componente de contenido seleccionado, verás una advertencia en la pestaña **Configuración del Otimizador de Contenido** y un error en la pestaña **Canales de mensajería**. El Canvas no puede lanzarse hasta que todos los componentes seleccionados se añadan correctamente a tu mensaje base.

A medida que el Canvas se ejecuta, el Otimizador de Contenido mezcla y combina variantes entre componentes para generar diferentes combinaciones de contenido. Con el tiempo, las combinaciones de mayor rendimiento se priorizan para la entrega, ayudándote a mejorar el rendimiento sin intervención manual.

#### Referencias de Liquid {#liquid-references}

| Canal | Componente | Fragmento de Liquid |
| --- | --- | --- |
| Correo electrónico | Asunto | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| Correo electrónico | Encabezado del cuerpo | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Correo electrónico | Contenido del cuerpo | {% raw %}`{% message_component "Body Content" %}`{% endraw %} |
| Correo electrónico | CTA principal | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} |
| Push | Título | {% raw %}`{% message_component "Title" %}`{% endraw %} |
| Push | Mensaje | {% raw %}`{% message_component "Message" %}`{% endraw %} |
| servicio de mensajes cortos/MMS/RCS | Gancho | {% raw %}`{% message_component "Hook" %}`{% endraw %} |
| servicio de mensajes cortos/MMS/RCS | Cuerpo | {% raw %}`{% message_component "Body" %}`{% endraw %} |
| servicio de mensajes cortos/MMS/RCS | CTA | {% raw %}`{% message_component "CTA" %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Referencias de Liquid" }

#### Token de combinación {#combination-token}

Usa el token de combinación para registrar qué combinación de variantes recibió un usuario. Añade la etiqueta de Liquid {% raw %}`{{component_combination_token}}`{% endraw %} a un enlace en tu mensaje base, y luego usa el valor en tus propias herramientas de análisis para atribuir el comportamiento posterior a una combinación específica.

Por ejemplo, añade el token a un enlace como parámetro UTM:

{% raw %}
```liquid
https://www.example.com/summer-sale?utm_content={{component_combination_token}}
```
{% endraw %}

La etiqueta genera una cadena de números separados por guiones bajos, como `3_2_8`:

- Cada posición corresponde a un componente de contenido, en el orden en que los componentes aparecen en la pestaña **Configuración del Otimizador de Contenido**.
- Cada número es el índice de la variante que el usuario recibió para ese componente. Los índices comienzan en 0, así que `0` es la primera variante creada para ese componente, `1` es la segunda, y así sucesivamente.

Braze asigna un índice a una variante cuando la creas y mantiene ese índice durante toda la vida del paso. Puedes desactivar una variante, pero no puedes eliminarla, y los índices nunca se reutilizan ni se renumeran. Un índice no refleja la posición de la variante entre las variantes actualmente activas.

Debido a esto, los índices pueden subir más allá de lo que sugiere el límite de cinco variantes por componente. Ese límite se aplica solo a las variantes activas, así que si desactivas varias variantes y añades nuevas, las nuevas variantes pueden tener índices como 5, 6, 7 y 8.

Por ejemplo, un paso de correo electrónico optimiza una línea del asunto y un CTA principal. El componente de asunto se lanzó con cinco variantes. Tres fueron desactivadas posteriormente y se añadieron tres nuevas:

| Variante de asunto | Índice | Estado |
| --- | --- | --- |
| Your summer sale starts now | 0 | Desactivada |
| Summer sale: 20% off | 1 | Desactivada |
| 20% off, this week only | 2 | Desactivada |
| Save 20% on summer picks | 3 | Activa |
| Your 20% off code is inside | 4 | Activa |
| Summer picks, 20% off | 5 | Activa |
| Don't miss 20% off | 6 | Activa |
| Last chance: 20% off summer | 7 | Activa |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Índices de variantes de asunto" }

El componente de CTA principal tiene dos variantes, con índices 0 y 1. En este paso, un token de `6_1` significa que el usuario recibió la variante de asunto con índice 6 ("Don't miss 20% off") y la variante de CTA principal con índice 1.

### Paso 5: Seleccionar el evento de optimización {#step-5-select-optimization-event}

El evento de optimización determina cómo el Otimizador de Contenido evalúa el rendimiento y asigna tráfico a las combinaciones de contenido a lo largo del tiempo.

Tu evento de optimización seleccionado se aplica a todos los componentes de contenido en este paso.

{% tabs local %}
{% tab Correo electrónico %}

Para correo electrónico, puedes optimizar para uno de los siguientes eventos. El Otimizador de Contenido utiliza las aperturas y los clics que se registran dentro de los 7 días posteriores al envío de un mensaje para redirigir la entrega hacia las combinaciones de contenido de mayor rendimiento.

| Evento | Descripción | Ejemplos |
| --- | --- | --- |
| Aperturas | Optimiza para combinaciones que logran que los destinatarios abran el correo electrónico. | Probar líneas del asunto o buscar aumentar la visibilidad |
| Clics | Optimiza para combinaciones que impulsan la participación con los enlaces. No incluye clics de bots ni clics de cancelación de suscripción reconocidos por Braze. | Generar tráfico, participación o conversión desde enlaces |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 5: Seleccionar el evento de optimización" }

#### Excluir enlaces de la optimización {#exclude-links-from-optimization}

Cuando optimizas para clics, puedes excluir uno o más enlaces de la optimización. Usa esto para enlaces que no indican participación con el contenido que estás probando, como un centro de preferencias o un localizador de tiendas.

Para excluir un enlace, ve a la pestaña **Configuración del Otimizador de Contenido** y añade la URL del enlace. Braze hace la coincidencia por prefijo, por lo que un clic en cualquier URL de tu mensaje que comience con la URL que especifiques se excluye.

Los clics excluidos no cuentan para el evento de optimización, por lo que no influyen en qué combinaciones favorece el Otimizador de Contenido. Aún se cuentan en el análisis total del paso, y no se cuentan en las tablas de [Rendimiento por componente](#performance-by-component) o [Rendimiento por combinación](#performance-by-combination).

{% endtab %}
{% tab Notificaciones push %}

Para notificaciones push, puedes optimizar **Aperturas**. Esto optimiza las combinaciones que logran que los destinatarios abran la notificación push. Puedes usar este evento de optimización para probar variaciones en el título o en el texto del mensaje.

{% endtab %}
{% tab servicio de mensajes cortos/MMS/RCS %}

Para mensajes servicio de mensajes cortos y MMS, puedes optimizar **Clics**. Para mensajes RCS, puedes optimizar **Lecturas** o **Clics**.

Para que el paso tenga un evento para optimizar:
- Los mensajes servicio de mensajes cortos y MMS deben contener un enlace.
- Los mensajes RCS deben contener un enlace o una respuesta sugerida.

{% alert note %}
En este momento, la mensajería RCS con el Otimizador de Contenido no admite alternativas de servicio de mensajes cortos.
{% endalert %}
{% endtab %}
{% endtabs %}

## Estados de los pasos {#step-states}

A medida que se ejecuta un paso del Otimizador de Conteúdo, Braze evalúa el rendimiento de las variantes de contenido y asigna al paso uno de tres estados, visibles en Canvas.

| Estado | Qué significa |
| --- | --- |
| Learning | Content Optimizer todavía está recopilando datos de rendimiento de tus variantes de contenido y aún no ha encontrado un ganador consistente y confiable. |
| Optimizing | Content Optimizer ha encontrado variantes que superan consistentemente a las demás y está desplazando la entrega hacia las combinaciones ganadoras. |
| Action Recommended | El paso se ha ejecutado durante un tiempo sin que surja un ganador claro. Revisa la configuración de tu paso para ayudar a Content Optimizer a encontrar uno. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de los pasos de Content Optimizer" }

### Acciones a considerar {#actions-to-consider}

Si tu paso entra en el estado Action Recommended, considera lo siguiente:

- Aumenta la cantidad de usuarios que ingresan al Canvas, si es posible. Más envíos le proporcionan a Content Optimizer más datos de los cuales aprender.
- En general, prueba más combinaciones en lugar de menos (consulta [Mejores prácticas](#best-practices)). Esto le da a Content Optimizer una señal más clara sobre qué está ganando. Si el volumen de tu audiencia es bajo (con un promedio inferior a aproximadamente 3,000 envíos por día), considera reducir ligeramente el número de variantes, ya que demasiadas combinaciones en relación con tu volumen pueden ralentizar el aprendizaje.
- Haz que tus variantes de contenido sean más claramente distintas entre sí en tono, estructura o contenido.
- Si no puedes aumentar tu audiencia y la cantidad de variantes y la diversidad de contenido ya se ven bien, es posible que tu paso simplemente necesite más tiempo para encontrar ganadoras.

## Editar un paso lanzado {#edit-a-launched-step}

Después de lanzar tu Canvas, puedes actualizar un paso del Otimizador de Contenido en ejecución abriéndolo en el editor de Canvas. Puedes:

{% multi_lang_include messaging/Canvas/content_optimizer_launched_step_actions.md %}

{% alert note %}
Braze asigna a cada usuario una combinación de contenido cuando entra en el paso del Optimizador de Contenido. Si su envío se retrasa por controles de entrega como los límites de velocidad, la sincronización inteligente o las horas tranquilas, es posible que aún reciba una variante que hayas desactivado. Para detener estos envíos de forma urgente, sigue los mismos pasos que para un paso de Mensaje. Para más información, consulta [Detener Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases).
{% endalert %}

Cuando publicas cambios, el optimizador se reinicia y comienza a redistribuir el tráfico desde cero entre todas las variantes y combinaciones activas. Evita actualizar variantes mientras el paso esté en estado de aprendizaje. Los datos históricos anteriores a la edición se conservan y se pueden ver en la pestaña **Content Analytics**.

Los siguientes ajustes no se pueden cambiar después del lanzamiento:

- El contenido de las variantes activas existentes
- Los componentes que se están probando
- El evento de optimización

Para pasos de servicio de mensajes cortos/MMS/RCS, el grupo de suscripción y el tipo de mensaje tampoco se pueden cambiar después del lanzamiento.

## Prácticas recomendadas {#best-practices}

- En general, prueba más componentes en lugar de menos para el paso del Otimizador de Contenido. Por ejemplo, en lugar de probar dos componentes para correo electrónico, prueba tres.
- Probar al menos 10 combinaciones totales generalmente produce mejores resultados.
- Para correo electrónico, los pasos que optimizan para clics tienden a superar a los pasos que optimizan para aperturas. Cuando los clics se ajusten a tu caso de uso, elige clics como tu evento de optimización.
- Si es la primera vez que usas el Otimizador de Contenido, considera usar un paso de [recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que solo parte de tu audiencia entre en la rama que contiene el paso del Otimizador de Contenido. Por ejemplo, podrías enviar a la mitad de tus usuarios por un recorrido con el paso del Otimizador de Contenido y enviar a la otra mitad por un recorrido de control que envíe el paso de mensaje con tu contenido habitual actual. Luego, recopila datos durante 2-3 semanas y compara cualquier indicador clave de rendimiento (indicador clave de rendimiento) o contramétrica antes de aumentar el tráfico a los recorridos con pasos del Otimizador de Contenido.
  - Para una comparación efectiva uno a uno, incluye tu contenido habitual como una de las variantes para cada componente en tu paso del Otimizador de Contenido.
- Cuando estés listo para actualizar después de que tu paso del Otimizador de Contenido haya estado en el estado de optimización durante algún tiempo, desactiva las variantes de bajo rendimiento y agrega nuevas que se basen en las características de tus mejores variantes.

## Consideraciones {#considerations}

- La configuración multilingüe no es compatible con los pasos del Optimizador de Contenido. En su lugar, usa un paso del Optimizador de Contenido por idioma y ramifica los recorridos individualmente.
- Las etiquetas de Liquid para los componentes del Optimizador de Contenido no son compatibles con los pasos de Mensaje, por lo que Liquid se interrumpe en los pasos de Mensaje.
- Una vez que se lanza un paso del Optimizador de Contenido, no puedes cambiar qué componentes se están probando, el contenido de las variantes activas existentes ni el evento de optimización. Para los pasos de servicio de mensajes cortos/MMS/RCS, el grupo de suscripción y el tipo de mensaje tampoco se pueden cambiar.

## Análisis {#analytics}

Para revisar el rendimiento, abre el panel de análisis a nivel de paso para ver las métricas por variante de contenido y el rendimiento general de la combinación. El paso del Optimizador de Contenido utiliza los [mismos análisis que el paso de Mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#analytics).

Si has actualizado el paso después del lanzamiento, el gráfico de asignación de envíos marca cuándo se produjo cada edición de contenido. Los datos de las variantes desactivadas se conservan y permanecen visibles en el panel de análisis, para que puedas comparar el rendimiento a lo largo de toda la vida útil del paso.

![Análisis del Optimizador de Contenido para tres botones y el porcentaje de asignación de envíos, con tendencia ascendente.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### Rendimiento por componente {#performance-by-component}

La sección **Rendimiento por componente** muestra el rendimiento de cada componente en el paso del Optimizador de Contenido. La columna **Componente** coincide con el componente de contenido que estás probando (por ejemplo, **Línea del asunto** o **CTA principal**). La columna **Identificador** coincide con el identificador de esta variante en la pestaña **Configuración del Optimizador de Contenido**.

Las aperturas únicas y los clics se capturan en un plazo de siete días desde el envío de un mensaje. Las columnas que ves dependen de tu canal y del evento de optimización seleccionado.

| Métrica | Descripción |
| --- | --- |
| Envíos | El número de envíos atribuidos a esta variante para ese componente en este paso, utilizando el mismo conteo de envíos a nivel de paso que [*Envíos*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends) en la tabla de [Rendimiento por combinación](#performance-by-combination). |
| Aperturas | Cuando esta columna aparece para tu canal, el número de aperturas **únicas** para esta variante dentro de los siete días posteriores al envío. Consulta [*Unique Opens*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Tarifa abierta | Cuando aparece esta columna, el porcentaje de envíos de esta variante que registraron al menos una apertura única válida dentro de los siete días. |
| Clics | El número de clics **únicos** para esta variante dentro de los siete días posteriores al envío. Consulta [*Total Clicks*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks), [*Unique Clicks*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks) y [Paso 5: Seleccionar evento de optimización](#step-5-select-optimization-event). |
| Tasa de clics | El porcentaje de envíos de esta variante que registraron al menos un clic único válido dentro de los siete días, utilizando la misma ventana de paso que la tabla de [Rendimiento por combinación](#performance-by-combination). Para más información, consulta [Por qué los análisis del paso difieren de los análisis generales](#why-step-analytics-differ-from-general-analytics). |
| Lecturas | Cuando aparece esta columna (por ejemplo, para RCS cuando optimizas por lecturas), cuenta cuándo un consumidor lee el mensaje con los acuses de lectura habilitados. Consulta [*Reads*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads). |
| Tasa de lectura | El porcentaje de envíos de esta variante que resultaron en una lectura entre los usuarios con los acuses de lectura activados. Consulta [*Read Rate*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de rendimiento por componente" }

![Análisis de rendimiento por componente del Optimizador de Contenido con tablas separadas por componente, que muestran envíos, clics y tasa de clics para cada variante.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_component.png %})

### Rendimiento por combinación {#performance-by-combination}

La sección **Rendimiento por combinación** muestra el rendimiento de cada combinación en el paso del Optimizador de Contenido. Las combinaciones son la mezcla de variantes que definen esta fila: una variante seleccionada de cada componente de contenido que estás probando (por ejemplo, una línea del asunto combinada con un CTA principal).

Las aperturas únicas y los clics se capturan en un plazo de siete días desde el envío de un mensaje. Las columnas que ves dependen de tu canal y del evento de optimización seleccionado.

| Métrica | Descripción |
| --- | --- |
| Envíos | El número total de mensajes enviados desde este paso con esta combinación. Los conteos siguen el mismo significado general que [*Envíos*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends), delimitados a cada combinación. |
| Aperturas | El número de aperturas únicas para esta combinación dentro de los siete días posteriores al envío. Para saber cómo se definen las aperturas únicas para correo electrónico, consulta [*Unique Opens*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Tarifa abierta | El porcentaje de envíos de esta combinación que registraron al menos una apertura única válida dentro de los siete días. |
| Clics | El número de clics únicos para esta combinación dentro de los siete días posteriores al envío. Para saber cómo Braze define los clics por canal, consulta [*Total Clicks*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks) y [*Unique Clicks*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks). |
| Tasa de clics | El porcentaje de envíos de esta combinación que registraron al menos un clic único válido dentro de los siete días. Dado que el Optimizador de Contenido utiliza los conteos deduplicados de siete días del paso, esta tasa puede no coincidir con las tasas de clics en los análisis generales de Campaign. Para más información, consulta [Por qué los análisis del paso difieren de los análisis generales](#why-step-analytics-differ-from-general-analytics). |
| [Lecturas]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads) | Cuando aparece esta columna (por ejemplo, para RCS cuando optimizas por lecturas), cuenta cuándo un consumidor lee el mensaje con los acuses de lectura habilitados. |
| [Tasa de lectura]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate) | Cuando aparece esta columna, el porcentaje de envíos de esta combinación que resultaron en una lectura entre los usuarios con los acuses de lectura activados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de rendimiento por combinación" }

![Tabla de análisis de rendimiento por combinación del Optimizador de Contenido con envíos, clics y tasa de clics para cada combinación de contenido.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_combination.png %})

### Por qué los análisis del paso difieren de los análisis generales {#why-step-analytics-differ-from-general-analytics}

Algunas razones por las que los análisis del paso del Optimizador de Contenido difieren de la sección **Analytics** incluyen:

- Los envíos push se deduplican para envíos al mismo usuario en diferentes dispositivos.
- En general, los clics y las aperturas se deduplican para ser únicos por cada usuario.
- Solo los clics y aperturas que ocurren dentro de los siete días posteriores al envío de un mensaje se cuentan en el paso del Optimizador de Contenido.
- Los clics en enlaces excluidos se cuentan en los análisis totales del paso, pero no se cuentan en las tablas de **Rendimiento por componente** ni de **Rendimiento por combinación**. Para más información, consulta [Excluir enlaces de la optimización](#exclude-links-from-optimization).

### Ver variantes en un perfil de usuario {#view-variants-on-a-user-profile}

Para ver qué variantes recibió un usuario individual, abre su perfil de usuario y ve a la pestaña **historial de mensajes**. En la fila del evento de envío de un paso del Optimizador de Contenido, la tabla muestra las variantes de componente que se enviaron a ese usuario. Para más información, consulta [Pestaña historial de mensajes]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab).

### Comparar pasos en el generador de informes {#compare-steps-in-report-builder}

Para comparar el rendimiento en más de un paso del Optimizador de Contenido, crea un informe y selecciona **Canvas Step with Canvas Optimizer**. El informe muestra el rendimiento del paso por componente y por combinación para los pasos que incluyas, ya sea que esos pasos estén en el mismo Canvas o en Canvas diferentes. Para más información, consulta [Generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

## Solución de problemas {#troubleshooting}

| Problema | Descripción | Solución |
| --- | --- | --- |
| Faltan etiquetas de Liquid | Si agregas un componente de contenido (como Asunto o CTA) pero no insertas la etiqueta de Liquid correspondiente en tu mensaje base, verás: <br>- Una advertencia en la pestaña **Content Optimizer Settings** <br>- Un error en la pestaña **Messaging Channels** | Copia el fragmento de código de Liquid que se muestra debajo de cada componente en la pestaña **Content Optimizer Settings** y pégalo en la parte correspondiente de tu mensaje. |
| Etiquetas de Liquid huérfanas | Si eliminas un componente de contenido pero dejas su etiqueta de Liquid en el mensaje base, es posible que el mensaje no se muestre como se espera cuando se envíe. | Elimina cualquier etiqueta `message_component` que no se use de tu mensaje base antes de lanzar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Solución de problemas" }