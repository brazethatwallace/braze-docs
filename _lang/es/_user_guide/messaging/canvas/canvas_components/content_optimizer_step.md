---
nav_title: Optimizador de contenidos
article_title: Paso del agente Optimizador de contenidos
alias: "/content_optimizer_step/"
page_order: 5
description: "El paso del agente Optimizador de contenidos te permite configurar y probar múltiples versiones de componentes de contenido dentro de un solo paso. Te ayuda a experimentar con variaciones de contenido y optimiza automáticamente hacia las combinaciones de mejor rendimiento a lo largo del tiempo."
page_type: reference

---

# Paso del agente Optimizador de contenidos

> El paso del agente Optimizador de contenidos te permite configurar y probar múltiples versiones de componentes de contenido dentro de un solo paso. Te ayuda a experimentar con variaciones de contenido y optimiza automáticamente hacia las combinaciones de mejor rendimiento a lo largo del tiempo. Para una introducción, consulta [Optimizador de contenidos]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
El Optimizador de contenidos está actualmente en beta. Para obtener ayuda para empezar, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Crear un paso del Optimizador de contenidos

Para obtener mejores resultados, utiliza el agente Optimizador de contenidos en Canvas donde los usuarios entren al paso gradualmente a lo largo del tiempo. Si todos los usuarios entran al paso a la vez, el agente no tendrá tiempo de aprender de los primeros resultados.

### Paso 1: Añadir un paso

Arrastra y suelta el componente **Optimizador de contenidos** desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> de signo más en la parte inferior de un paso y selecciona **Optimizador de contenidos**.

### Paso 2: Crear tu mensaje base

El mensaje base es el punto de partida para tu paso. Las variantes para cada componente de contenido se insertan dinámicamente en función de las combinaciones definidas en la pestaña **Configuración del Optimizador de contenidos**.

{% alert note %}
Durante el periodo beta, los canales compatibles son correo electrónico y notificaciones push.
{% endalert %}

{% tabs local %}
{% tab Correo electrónico %}

Desde la pestaña **Canales de mensajería**, selecciona **Correo electrónico** y crea tu mensaje de correo electrónico base. Consulta nuestra sección dedicada de [Correo electrónico]({{site.baseurl}}/user_guide/channels/email) para obtener ayuda.

El agente Optimizador de contenidos utiliza los ajustes de envío (como el dominio de correo electrónico y la dirección de responder a) especificados en esta variante para enviar todos los mensajes. Puedes empezar con un nuevo diseño o seleccionar una plantilla existente para este mensaje. En este paso, considera qué componentes del mensaje quieres optimizar. Los defines en el [paso 4](#step-4).

Los componentes compatibles para optimizar incluyen:

- Asunto
- Encabezado del cuerpo
- Contenido del cuerpo
- CTA principal

{% endtab %}
{% tab Notificaciones push %}

Desde la pestaña **Canales de mensajería**, selecciona **Notificaciones push** y crea tu notificación push base. Consulta nuestra sección dedicada de [Push]({{site.baseurl}}/user_guide/channels/push) para obtener ayuda.

El agente Optimizador de contenidos utiliza las plataformas push seleccionadas especificadas en esta variante para enviar todos los mensajes. Puedes empezar con un nuevo diseño o seleccionar una plantilla existente para este mensaje. En este paso, considera qué componentes del mensaje quieres optimizar. Los defines en el [paso 4](#step-4).

Los componentes compatibles para optimizar incluyen:

- Título
- Mensaje

{% endtab %}
{% endtabs %}

### Paso 3: Especificar los ajustes de entrega

En la pestaña **Ajustes de entrega**, puedes especificar si el paso debe usar Intelligent Timing o validaciones de entrega. Para más detalles, consulta [Editar ajustes de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) en el paso de mensaje.

### Paso 4: Añadir componentes de contenido y variantes {#step-4}

Los componentes de contenido son los elementos individuales de tu mensaje que quieres probar, como diferentes líneas del asunto o títulos. Estos componentes te permiten generar múltiples versiones de un mensaje y optimizar automáticamente en función del rendimiento a lo largo del tiempo.

- **Correo electrónico:** Puedes añadir hasta tres componentes de contenido por paso y hasta cinco variantes por componente, para un total de 125 combinaciones de contenido únicas.
- **Notificaciones push:** Puedes añadir hasta dos componentes por paso y hasta cinco variantes por componente, para un total de 25 combinaciones de contenido únicas.

![Opciones para añadir y configurar componentes de contenido en la interfaz del Optimizador de contenidos. La interfaz muestra componentes seleccionables como Asunto, Encabezado del cuerpo, Contenido del cuerpo y CTA principal, cada uno con campos para introducir diferentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Paso 4.1: Configurar componentes de contenido

Para configurar componentes, ve a la pestaña **Configuración del Optimizador de contenidos**.

{% tabs local %}
{% tab Correo electrónico %}

Elige qué componentes quieres optimizar para mensajes de correo electrónico. Las opciones compatibles son:

- Asunto
- Encabezado del cuerpo
- Contenido del cuerpo
- CTA principal

Para cada componente seleccionado, define un conjunto de versiones alternativas de ese contenido (variantes). Usa variantes claras y diferenciadas que difieran en tono, estructura o contenido. Esto ayuda al Optimizador de contenidos a identificar las de mejor rendimiento de forma más efectiva. Puedes:
  - Escribir tus propias variantes manualmente.
  - Usar sugerencias generadas por IA para explorar nuevas opciones rápidamente.

![Interfaz de configuración del Optimizador de contenidos que muestra opciones para añadir y configurar componentes de contenido para la optimización de correo electrónico. Cada componente tiene campos de entrada para introducir diferentes variantes. El texto visible incluye nombres de componentes y campos para introducir texto de variantes.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab Notificaciones push %}

Elige qué componentes quieres optimizar para notificaciones push. Las opciones compatibles son:
- Título
- Mensaje

Para cada componente seleccionado, define un conjunto de versiones alternativas de ese contenido (variantes). Usa variantes claras y diferenciadas que difieran en tono, estructura o contenido. Esto ayuda al Optimizador de contenidos a identificar las de mejor rendimiento de forma más efectiva. Puedes:
  - Escribir tus propias variantes manualmente.
  - Usar sugerencias generadas por IA para explorar nuevas opciones rápidamente.

![Configuración del Optimizador de contenidos que muestra opciones para añadir y configurar componentes de contenido para la optimización push.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% endtabs %}

#### Paso 4.2: Añadir Liquid a tu mensaje

Después de definir al menos dos variantes para cada componente, copia la etiqueta de Liquid asociada para cada uno y pégala en la ubicación correspondiente de tu mensaje base.

- Por ejemplo, si estás optimizando la línea del asunto, pega la etiqueta {% raw %}`{% message_component "Subject" %}`{% endraw %} en el campo de asunto del compositor de correo electrónico.
- También puedes incluir etiquetas de componentes dentro de texto más largo para probar solo una parte del componente. Por ejemplo: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Opciones para añadir y configurar componentes de contenido como Asunto, Encabezado del cuerpo, Contenido del cuerpo y CTA principal. Cada componente tiene campos para introducir diferentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Si no añades una etiqueta de Liquid para un componente de contenido seleccionado, verás una advertencia en la pestaña **Configuración del Optimizador de contenidos** y un error en la pestaña **Canales de mensajería**. El Canvas no se puede lanzar hasta que todos los componentes seleccionados se hayan añadido correctamente a tu mensaje base.

A medida que el Canvas se ejecuta, el agente mezcla y combina variantes entre componentes para generar diferentes combinaciones de contenido. Con el tiempo, las combinaciones de mayor rendimiento se priorizan para la entrega, ayudándote a mejorar el rendimiento sin intervención manual.

#### Referencias de Liquid

| Canal | Componente | Fragmento de código Liquid |
| --- | --- | --- |
| Correo electrónico | Asunto | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| Correo electrónico | Encabezado del cuerpo | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Correo electrónico | Contenido del cuerpo | {% raw %}`{% message_component "Body Content" %}`{% endraw %} | 
| Correo electrónico | CTA principal | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} | 
| Push | Título | {% raw %}`{% message_component "Title" %}`{% endraw %} | 
| Push | Mensaje | {% raw %}`{% message_component "Message" %}`{% endraw %} | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 5: Seleccionar el evento de optimización

El evento de optimización determina cómo el agente Optimizador de contenidos evalúa el rendimiento y asigna tráfico a las combinaciones de contenido a lo largo del tiempo.

El evento de optimización seleccionado se aplica a todos los componentes de contenido en este paso.

{% tabs local %}
{% tab Correo electrónico %}

Para correo electrónico, puedes optimizar para uno de los siguientes eventos. El agente utiliza las aperturas y los clics que se registran dentro de los 7 días posteriores al envío de un mensaje para dirigir la entrega hacia las combinaciones de contenido de mayor rendimiento.

| Evento | Descripción | Casos de uso |
| --- | --- | --- |
| Aperturas | Optimiza para combinaciones que logran que los destinatarios abran el correo electrónico. | Probar líneas del asunto o buscar aumentar la visibilidad |
| Clics | Optimiza para combinaciones que impulsan la interacción con enlaces. No incluye clics de bots ni clics de cancelar suscripción reconocidos por Braze. | Impulsar tráfico, interacción o conversión desde enlaces |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Notificaciones push %}

Para notificaciones push, puedes optimizar **Aperturas**. Esto optimiza las combinaciones que logran que los destinatarios abran la notificación push. Puedes usar este evento de optimización para probar variaciones en el título o el texto del mensaje.

{% endtab %}
{% endtabs %}

## Buenas prácticas

- En general, recomendamos probar más de un componente para el paso del Optimizador de contenidos.
- Si estás optimizando para clics, incluye líneas del asunto en tus pruebas, ya que líneas del asunto más efectivas pueden contribuir a un aumento de aperturas y crear más oportunidades para clics.
- Si estás optimizando para aperturas, mantén tus pruebas enfocadas en la línea del asunto.

## Análisis

Para revisar el rendimiento, abre el panel de análisis a nivel de paso para ver métricas por variante de contenido y rendimiento general de combinaciones. El paso del Optimizador de contenidos utiliza los [mismos análisis que el paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#analytics).

![Análisis del Optimizador de contenidos para tres botones y el porcentaje de asignación de envíos, que tiende al alza.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### Por qué los análisis del paso difieren de los análisis generales

Las razones por las que los análisis en el paso del Optimizador de contenidos difieren de la sección de **Análisis** incluyen:

- Los envíos push se deduplican para envíos al mismo usuario en diferentes dispositivos.
- En general, los clics y las aperturas se deduplican para ser únicos por cada usuario.
- Solo los clics y las aperturas que ocurren dentro de los siete días posteriores al envío de un mensaje se cuentan en el paso del Optimizador de contenidos.

## Solución de problemas

| Problema | Descripción | Solución |
| --- | --- | --- |
| Etiquetas de Liquid faltantes | Si añades un componente de contenido (como Asunto o CTA) pero no insertas la etiqueta de Liquid correspondiente en tu mensaje base, verás: <br>- Una advertencia en la pestaña **Configuración del Optimizador de contenidos** <br>- Un error en la pestaña **Canales de mensajería** | Copia el fragmento de código Liquid que se muestra debajo de cada componente en la pestaña **Configuración del Optimizador de contenidos** y pégalo en la parte correspondiente de tu mensaje. |
| Etiquetas de Liquid huérfanas | Si eliminas un componente de contenido pero dejas su etiqueta de Liquid en el mensaje base, es posible que el mensaje no se renderice como se espera al enviarse. | Elimina cualquier etiqueta `message_component` no utilizada de tu mensaje base antes de lanzar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }