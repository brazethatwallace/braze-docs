---
nav_title: Optimizador de contenidos
article_title: Paso del agente Optimizador de contenidos
alias: "/content_optimizer_step/"
page_order: 5
description: "El paso del agente Optimizador de contenidos te permite configurar y probar múltiples versiones de componentes de contenido dentro de un solo paso. Te ayuda a experimentar con variaciones de contenido y optimiza automáticamente hacia las combinaciones de mejor rendimiento a lo largo del tiempo."
page_type: reference

---

# Paso del agente Optimizador de contenidos {#content-optimizer-agent-step}

> El paso del agente Optimizador de contenidos te permite configurar y probar múltiples versiones de componentes de contenido dentro de un solo paso. Te ayuda a experimentar con variaciones de contenido y optimiza automáticamente hacia las combinaciones de mejor rendimiento a lo largo del tiempo. Para una introducción, consulta [Optimizador de contenidos]({{site.baseurl}}/user_guide/brazeai/content_optimizer).

{% alert important %}
El Optimizador de contenidos está actualmente en beta. Para obtener ayuda para empezar, ponte en contacto con tu administrador de éxito de cliente.
{% endalert %}

## Crear un paso del Optimizador de contenidos {#create-a-content-optimizer-step}

Para obtener mejores resultados, utiliza el agente Optimizador de contenidos en Canvas donde los usuarios entren al paso gradualmente a lo largo del tiempo. Si todos los usuarios entran al paso a la vez, el agente no tendrá tiempo de aprender de los primeros resultados.

### Paso 1: Añadir un paso {#step-1-add-a-step}

Arrastra y suelta el componente **Content Optimizer** desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> de signo más en la parte inferior de un paso y selecciona **Content Optimizer**.

### Paso 2: Crear tu mensaje base {#step-2-create-your-base-message}

El mensaje base es el punto de partida para tu paso. Las variantes para cada componente de contenido se insertan dinámicamente en función de las combinaciones definidas en la pestaña **Content Optimizer Settings**.

{% alert note %}
Durante el periodo beta, los canales compatibles son correo electrónico, notificaciones push y SMS/MMS/RCS.
{% endalert %}

{% tabs local %}
{% tab Correo electrónico %}

Desde la pestaña **Messaging Channels**, selecciona **Email** y crea tu mensaje de correo electrónico base. Consulta nuestra sección dedicada de [correo electrónico]({{site.baseurl}}/user_guide/channels/email) para obtener ayuda.

El agente Optimizador de contenidos utiliza los ajustes de envío (como el dominio de correo electrónico y la dirección de responder a) especificados en esta variante para enviar todos los mensajes. Puedes empezar con un nuevo diseño o seleccionar una plantilla existente para este mensaje. En este paso, considera qué componentes del mensaje quieres optimizar. Los defines en el [paso 4](#step-4).

Los componentes compatibles para optimizar incluyen:

- Subject
- Body Header
- Body Content
- Primary CTA

{% endtab %}
{% tab Notificaciones push %}

Desde la pestaña **Messaging Channels**, selecciona **Push notifications** y crea tu notificación push base. Consulta nuestra sección dedicada de [push]({{site.baseurl}}/user_guide/channels/push) para obtener ayuda.

El agente Optimizador de contenidos utiliza las plataformas push seleccionadas especificadas en esta variante para enviar todos los mensajes. Puedes empezar con un nuevo diseño o seleccionar una plantilla existente para este mensaje. En este paso, considera qué componentes del mensaje quieres optimizar. Los defines en el [paso 4](#step-4).

Los componentes compatibles para optimizar incluyen:

- Title
- Message

{% endtab %}
{% tab SMS/MMS/RCS %}

Desde la pestaña **Messaging Channels**, selecciona **SMS/MMS/RCS** y crea tu mensaje base. Consulta nuestra sección dedicada de [SMS/MMS/RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs) para obtener ayuda.

El agente Optimizador de contenidos utiliza los detalles de **Content** y **Message** especificados en esta variante para enviar todos los mensajes. Puedes empezar con un nuevo diseño o seleccionar una plantilla existente para este mensaje. En este paso, considera qué componentes del mensaje quieres optimizar. Los defines en el [paso 4](#step-4).

Los componentes compatibles para optimizar incluyen:

- Hook
- Body
- CTA

{% endtab %}
{% endtabs %}

### Paso 3: Especificar los ajustes de entrega {#step-3-specify-delivery-settings}

En la pestaña **Delivery Settings**, puedes especificar si el paso debe usar sincronización inteligente o validaciones de entrega. Para más detalles, consulta [Editar ajustes de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings) en el paso de mensaje.

### Paso 4: Añadir componentes de contenido y variantes {#step-4}

Los componentes de contenido son los elementos individuales de tu mensaje que quieres probar, como diferentes líneas del asunto o títulos. Estos componentes te permiten generar múltiples versiones de un mensaje y optimizar automáticamente en función del rendimiento a lo largo del tiempo.

- **Correo electrónico:** Puedes añadir hasta tres componentes de contenido por paso y hasta cinco variantes por componente, para un total de 125 combinaciones de contenido únicas.
- **Notificaciones push:** Puedes añadir hasta dos componentes por paso y hasta cinco variantes por componente, para un total de 25 combinaciones de contenido únicas.
- **SMS/MMS/RCS:** Puedes añadir hasta dos componentes de contenido por paso y hasta cinco variantes por componente, para un total de 25 combinaciones de contenido únicas.

Cuando usas **Generate AI suggestions**, Braze envía contenido a OpenAI para generar ideas de variantes. La asignación de tráfico en el momento del envío no utiliza OpenAI. Para más detalles sobre qué datos se envían y cómo se utilizan, consulta [OpenAI y el Optimizador de contenidos]({{site.baseurl}}/user_guide/brazeai/content_optimizer#openai-and-content-optimizer).

![Opciones para añadir y configurar componentes de contenido en la interfaz del Optimizador de contenidos. La interfaz muestra componentes seleccionables como Subject, Body Header, Body Content y Primary CTA, cada uno con campos para introducir diferentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Paso 4.1: Configurar componentes de contenido {#step-41-configure-content-components}

Para configurar componentes, ve a la pestaña **Content Optimizer Settings**.

{% tabs local %}
{% tab Correo electrónico %}

Elige qué componentes quieres optimizar para mensajes de correo electrónico. Las opciones compatibles son:

- Subject
- Body Header
- Body Content
- Primary CTA

Para cada componente seleccionado, define un conjunto de versiones alternativas de ese contenido (variantes). Usa variantes claras y diferenciadas que difieran en tono, estructura o contenido. Esto ayuda al Optimizador de contenidos a identificar las de mejor rendimiento de forma más efectiva. Puedes:
  - Escribir tus propias variantes manualmente.
  - Usar sugerencias generadas por IA para explorar nuevas opciones rápidamente.

![Interfaz de Content Optimizer Settings que muestra opciones para añadir y configurar componentes de contenido para la optimización de correo electrónico. Cada componente tiene campos de entrada para introducir diferentes variantes. El texto visible incluye nombres de componentes y campos para introducir texto de variantes.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab Notificaciones push %}

Elige qué componentes quieres optimizar para notificaciones push. Las opciones compatibles son:
- Title
- Message

Para cada componente seleccionado, define un conjunto de versiones alternativas de ese contenido (variantes). Usa variantes claras y diferenciadas que difieran en tono, estructura o contenido. Esto ayuda al Optimizador de contenidos a identificar las de mejor rendimiento de forma más efectiva. Puedes:
  - Escribir tus propias variantes manualmente.
  - Usar sugerencias generadas por IA para explorar nuevas opciones rápidamente.

![Ajustes del Optimizador de contenidos que muestran opciones para añadir y configurar componentes de contenido para la optimización push.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% tab SMS/MMS/RCS %}

Después de seleccionar tu grupo de suscripción y tipo de mensaje (si corresponde), elige qué componentes quieres optimizar para SMS/MMS/RCS. Las opciones compatibles son:
- Hook
- Body
- CTA
{% alert note %}
Después de que se lance un paso del Optimizador de contenidos de SMS/MMS/RCS, no puedes actualizar el grupo de suscripción ni el tipo de mensaje.
{% endalert %}
Para cada componente seleccionado, define un conjunto de versiones alternativas de ese contenido (variantes). Usa variantes claras y diferenciadas que difieran en tono, estructura o contenido. Esto ayuda al Optimizador de contenidos a identificar las de mejor rendimiento de forma más efectiva. Puedes:
  - Escribir tus propias variantes manualmente.
  - Usar sugerencias generadas por IA para explorar nuevas opciones rápidamente.

![Ajustes del Optimizador de contenidos que muestran opciones para añadir y configurar componentes de contenido para la optimización de SMS/MMS/RCS.]({% image_buster /assets/img/content_optimizer/add_content_components_sms_rcs_mms.png %})

{% endtab %}
{% endtabs %}

#### Paso 4.2: Añadir Liquid a tu mensaje {#step-42-add-liquid-to-your-message}

Después de definir al menos dos variantes para cada componente, copia la etiqueta de Liquid asociada para cada uno y pégala en la ubicación correspondiente de tu mensaje base.

- Por ejemplo, si estás optimizando la línea del asunto, pega la etiqueta {% raw %}`{% message_component "Subject" %}`{% endraw %} en el campo de asunto del creador de correo electrónico.
- También puedes incluir etiquetas de componentes dentro de texto más largo para probar solo una parte del componente. Por ejemplo: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Opciones para añadir y configurar componentes de contenido como Subject, Body Header, Body Content y Primary CTA. Cada componente tiene campos para introducir diferentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Si no añades una etiqueta de Liquid para un componente de contenido seleccionado, verás una advertencia en la pestaña **Content Optimizer Settings** y un error en la pestaña **Messaging Channels**. El Canvas no se puede lanzar hasta que todos los componentes seleccionados se hayan añadido correctamente a tu mensaje base.

A medida que el Canvas se ejecuta, el agente mezcla y combina variantes entre componentes para generar diferentes combinaciones de contenido. Con el tiempo, las combinaciones de mayor rendimiento se priorizan para la entrega, ayudándote a mejorar el rendimiento sin intervención manual.

#### Referencias de Liquid {#liquid-references}

| Canal | Componente | Fragmento de código Liquid |
| --- | --- | --- |
| Correo electrónico | Subject | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| Correo electrónico | Body Header | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Correo electrónico | Body Content | {% raw %}`{% message_component "Body Content" %}`{% endraw %} |
| Correo electrónico | Primary CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} |
| Push | Title | {% raw %}`{% message_component "Title" %}`{% endraw %} |
| Push | Message | {% raw %}`{% message_component "Message" %}`{% endraw %} |
| SMS/MMS/RCS | Hook | {% raw %}`{% message_component "Hook" %}`{% endraw %} |
| SMS/MMS/RCS | Body | {% raw %}`{% message_component "Body" %}`{% endraw %} |
| SMS/MMS/RCS | CTA | {% raw %}`{% message_component "CTA" %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Referencias de Liquid" }

### Paso 5: Seleccionar el evento de optimización {#step-5-select-optimization-event}

El evento de optimización determina cómo el agente Optimizador de contenidos evalúa el rendimiento y asigna tráfico a las combinaciones de contenido a lo largo del tiempo.

El evento de optimización seleccionado se aplica a todos los componentes de contenido en este paso.

{% tabs local %}
{% tab Correo electrónico %}

Para correo electrónico, puedes optimizar para uno de los siguientes eventos. El agente utiliza las aperturas y los clics que se registran dentro de los 7 días posteriores al envío de un mensaje para dirigir la entrega hacia las combinaciones de contenido de mayor rendimiento.

| Evento | Descripción | Ejemplos |
| --- | --- | --- |
| Aperturas | Optimiza para combinaciones que logran que los destinatarios abran el correo electrónico. | Probar líneas del asunto o buscar aumentar la visibilidad |
| Clics | Optimiza para combinaciones que impulsan la interacción con enlaces. No incluye clics de bots ni clics de cancelar suscripción reconocidos por Braze. | Impulsar tráfico, interacción o conversión desde enlaces |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 5: Seleccionar el evento de optimización" }

{% endtab %}
{% tab Notificaciones push %}

Para notificaciones push, puedes optimizar **Aperturas**. Esto optimiza las combinaciones que logran que los destinatarios abran la notificación push. Puedes usar este evento de optimización para probar variaciones en el título o el texto del mensaje.

{% endtab %}
{% tab SMS/MMS/RCS %}

Para mensajes SMS y MMS, puedes optimizar **Clics**. Para mensajes RCS, puedes optimizar **Lecturas** o **Clics**.

Para que el paso tenga un evento hacia el cual optimizar:
- Los mensajes SMS y MMS deben contener un enlace.
- Los mensajes RCS deben contener un enlace o una respuesta sugerida.

{% alert note %}
En este momento, la mensajería RCS con el Optimizador de contenidos no admite alternativas de SMS.
{% endalert %}
{% endtab %}
{% endtabs %}

## Estados del paso {#step-states}

A medida que un paso del Optimizador de contenidos se ejecuta, Braze evalúa el rendimiento de las variantes de contenido y asigna al paso uno de tres estados, visibles en el Canvas.

| Estado | Qué significa |
| --- | --- |
| Aprendiendo | El agente aún está recopilando datos de rendimiento de tus variantes de contenido y no ha encontrado un ganador consistente y fiable todavía. |
| Optimizando | El agente ha encontrado variantes que superan consistentemente a las demás y está dirigiendo la entrega hacia las combinaciones ganadoras. |
| Acción recomendada | El paso ha estado ejecutándose durante un tiempo sin que surja un ganador claro. Revisa la configuración de tu paso para ayudar al agente a encontrar uno. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados del paso del Optimizador de contenidos" }

### Acciones a considerar {#actions-to-consider}

Si tu paso entra en el estado Acción recomendada, considera lo siguiente:

- Aumenta la cantidad de usuarios que entran al Canvas, si es posible. Más envíos le dan al agente más datos de los que aprender.
- En general, prueba más combinaciones en lugar de menos (consulta [Buenas prácticas](#best-practices)). Esto le da al agente una señal más clara sobre qué está ganando. Si el volumen de tu audiencia es bajo (un promedio inferior a aproximadamente 3000 envíos por día), considera reducir ligeramente el número de variantes, ya que demasiadas combinaciones en relación con tu volumen pueden ralentizar el aprendizaje.
- Haz que tus variantes de contenido sean más claramente distintas entre sí en tono, estructura o contenido.
- Si no puedes aumentar tu audiencia y la cantidad de variantes y la diversidad de contenido ya se ven bien, es posible que tu paso simplemente necesite más tiempo para encontrar ganadoras.

## Editar un paso lanzado {#edit-a-launched-step}

Después de que tu Canvas se lance, puedes actualizar un paso del Optimizador de contenidos en ejecución abriéndolo en el editor de Canvas. Puedes:

- Añadir nuevas variantes a cualquier componente existente, ya sea manualmente o usando sugerencias generadas por IA, hasta el límite de cinco variantes por componente.
- Desactivar variantes para dejar de enviarlas a los usuarios.
- Reactivar variantes previamente desactivadas, siempre que hacerlo mantenga el componente en o por debajo del límite de cinco variantes.

Cuando publicas los cambios, el optimizador se reinicia y comienza a reasignar tráfico desde cero entre todas las variantes y combinaciones activas. Evita actualizar variantes mientras el paso está en el estado Aprendiendo. Los datos históricos anteriores a la edición se conservan y se pueden consultar en la pestaña **Content Analytics**.

Los siguientes ajustes no se pueden cambiar después del lanzamiento:

- El contenido de las variantes activas existentes
- Qué componentes se están probando
- El evento de optimización

Para los pasos de SMS/MMS/RCS, el grupo de suscripción y el tipo de mensaje tampoco se pueden cambiar después del lanzamiento.

## Buenas prácticas {#best-practices}

- En general, prueba más componentes en lugar de menos para el paso del Optimizador de contenidos. Por ejemplo, en lugar de probar dos componentes para correo electrónico, prueba tres.
- Probar al menos 10 combinaciones totales generalmente produce mejores resultados.
- Si es la primera vez que usas el Optimizador de contenidos, considera usar un paso de [recorrido de experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que solo una parte de tu audiencia entre en la rama que contiene el paso del Optimizador de contenidos. Por ejemplo, podrías enviar a la mitad de tus usuarios por un recorrido con el paso del Optimizador de contenidos y enviar a la otra mitad por un recorrido de control que envíe el paso de mensaje con tu contenido habitual. Luego, recopila datos durante 2-3 semanas y compara cualquier indicador clave de rendimiento (KPI) o contraindicador antes de aumentar el tráfico hacia los recorridos con pasos del Optimizador de contenidos.
  - Para una comparación efectiva uno a uno, incluye tu contenido habitual como una de las variantes para cada componente en tu paso del Optimizador de contenidos.
- Cuando estés listo para actualizar después de que tu paso del Optimizador de contenidos haya estado en el estado Optimizando durante un tiempo, desactiva las variantes de bajo rendimiento y añade nuevas que se basen en las características de tus mejores variantes.

## Consideraciones {#considerations}

- La configuración multilingüe no es compatible con los pasos del Optimizador de contenidos. En su lugar, usa un paso del Optimizador de contenidos por idioma y ramifica los recorridos individualmente.
- Las etiquetas de Liquid para componentes del Optimizador de contenidos no son compatibles con los pasos de mensaje, por lo que Liquid se interrumpe en los pasos de mensaje.
- Después de que se lance un paso del Optimizador de contenidos, no puedes cambiar qué componentes se están probando, el contenido de las variantes activas existentes ni el evento de optimización. Para los pasos de SMS/MMS/RCS, el grupo de suscripción y el tipo de mensaje tampoco se pueden cambiar.

## Análisis {#analytics}

Para revisar el rendimiento, abre el panel de análisis a nivel de paso para ver métricas por variante de contenido y rendimiento general de combinaciones. El paso del Optimizador de contenidos utiliza los [mismos análisis que el paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#analytics).

Si has actualizado el paso después del lanzamiento, el gráfico de asignación de envíos marca cuándo ocurrió cada edición de contenido. Los datos de las variantes desactivadas se conservan y se pueden consultar en el panel de análisis, para que puedas comparar el rendimiento a lo largo de toda la vida del paso.

![Análisis del Optimizador de contenidos para tres botones y el porcentaje de asignación de envíos, que tiende al alza.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### Rendimiento por componente {#performance-by-component}

La sección **Rendimiento por componente** muestra el rendimiento de cada componente en el paso del Optimizador de contenidos. La columna **Componente** coincide con el componente de contenido que estás probando (por ejemplo, **Subject line** o **Primary CTA**). La columna **Identificador** coincide con el identificador de esta variante en la pestaña **Content Optimizer Settings**.

Las aperturas únicas y los clics se capturan dentro de los siete días posteriores al envío de un mensaje. Las columnas que ves dependen de tu canal y del evento de optimización seleccionado.

| Métrica | Descripción |
| --- | --- |
| Envíos | El número de envíos atribuidos a esta variante para ese componente en este paso, utilizando el mismo conteo de envíos a nivel de paso que [*Envíos*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends) en la tabla [Rendimiento por combinación](#performance-by-combination). |
| Aperturas | Cuando esta columna aparece para tu canal, el número de aperturas **únicas** para esta variante dentro de los siete días posteriores al envío. Consulta [*Unique Opens*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Tasa de apertura | Cuando esta columna aparece, el porcentaje de envíos para esta variante que registraron al menos una apertura única cualificada dentro de los siete días. |
| Clics | El número de clics **únicos** para esta variante dentro de los siete días posteriores al envío. Consulta [*Clics totales*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks), [*Clics únicos*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks) y [Paso 5: Seleccionar el evento de optimización](#step-5-select-optimization-event). |
| Tasa de clics | El porcentaje de envíos para esta variante que registraron al menos un clic único cualificado dentro de los siete días, utilizando la misma ventana de paso que la tabla [Rendimiento por combinación](#performance-by-combination). Para más información, consulta [Por qué los análisis del paso difieren de los análisis generales](#why-step-analytics-differ-from-general-analytics). |
| Lecturas | Cuando esta columna aparece (por ejemplo, para RCS cuando optimizas para lecturas), cuenta cuando un consumidor lee el mensaje con los acuses de lectura habilitados. Consulta [*Lecturas*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads). |
| Tasa de lectura | El porcentaje de envíos para esta variante que resultaron en una lectura entre los usuarios con acuses de lectura activados. Consulta [*Tasa de lectura*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de rendimiento por componente" }

![Análisis de rendimiento por componente del Optimizador de contenidos con tablas separadas por componente, que muestran envíos, clics y tasa de clics para cada variante.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_component.png %})

### Rendimiento por combinación {#performance-by-combination}

La sección **Rendimiento por combinación** muestra el rendimiento de cada combinación en el paso del Optimizador de contenidos. Las combinaciones son la mezcla de variantes que definen esta fila: una variante seleccionada de cada componente de contenido que estás probando (por ejemplo, una línea del asunto emparejada con un CTA principal).

Las aperturas únicas y los clics se capturan dentro de los siete días posteriores al envío de un mensaje. Las columnas que ves dependen de tu canal y del evento de optimización seleccionado.

| Métrica | Descripción |
| --- | --- |
| Envíos | El número total de mensajes enviados desde este paso utilizando esta combinación. Los conteos siguen el mismo significado general que [*Envíos*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends), limitados a cada combinación. |
| Aperturas | El número de aperturas únicas para esta combinación dentro de los siete días posteriores al envío. Para saber cómo se definen las aperturas únicas para correo electrónico, consulta [*Unique Opens*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens). |
| Tasa de apertura | El porcentaje de envíos para esta combinación que registraron al menos una apertura única cualificada dentro de los siete días. |
| Clics | El número de clics únicos para esta combinación dentro de los siete días posteriores al envío. Para saber cómo Braze define los clics por canal, consulta [*Clics totales*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks) y [*Clics únicos*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks). |
| Tasa de clics | El porcentaje de envíos para esta combinación que registraron al menos un clic único cualificado dentro de los siete días. Dado que el Optimizador de contenidos utiliza los conteos deduplicados de siete días del paso, esta tasa puede no coincidir con las tasas de clics en los análisis generales de Campaign. Para más información, consulta [Por qué los análisis del paso difieren de los análisis generales](#why-step-analytics-differ-from-general-analytics). |
| [Lecturas]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads) | Cuando esta columna aparece (por ejemplo, para RCS cuando optimizas para lecturas), cuenta cuando un consumidor lee el mensaje con los acuses de lectura habilitados. |
| [Tasa de lectura]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate) | Cuando esta columna aparece, el porcentaje de envíos para esta combinación que resultaron en una lectura entre los usuarios con acuses de lectura activados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de rendimiento por combinación" }

![Tabla de análisis de rendimiento por combinación del Optimizador de contenidos con envíos, clics y tasa de clics para cada combinación de contenido.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_combination.png %})

### Por qué los análisis del paso difieren de los análisis generales {#why-step-analytics-differ-from-general-analytics}

Las razones por las que los análisis en el paso del Optimizador de contenidos difieren de la sección de **Analytics** incluyen:

- Los envíos push se deduplican para envíos al mismo usuario en diferentes dispositivos.
- En general, los clics y las aperturas se deduplican para ser únicos por cada usuario.
- Solo los clics y las aperturas que ocurren dentro de los siete días posteriores al envío de un mensaje se cuentan en el paso del Optimizador de contenidos.

## Solución de problemas {#troubleshooting}

| Problema | Descripción | Solución |
| --- | --- | --- |
| Etiquetas de Liquid faltantes | Si añades un componente de contenido (como Subject o CTA) pero no insertas la etiqueta de Liquid correspondiente en tu mensaje base, verás: <br>- Una advertencia en la pestaña **Content Optimizer Settings** <br>- Un error en la pestaña **Messaging Channels** | Copia el fragmento de código Liquid que se muestra debajo de cada componente en la pestaña **Content Optimizer Settings** y pégalo en la parte correspondiente de tu mensaje. |
| Etiquetas de Liquid huérfanas | Si eliminas un componente de contenido pero dejas su etiqueta de Liquid en el mensaje base, es posible que el mensaje no se renderice como se espera al enviarse. | Elimina cualquier etiqueta `message_component` no utilizada de tu mensaje base antes de lanzar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Solución de problemas" }