---
nav_title: Intención abandonada
article_title: Intención abandonada
page_order: 1
page_type: reference
description: "Este artículo describe cómo utilizar una plantilla de BRAZE CANVAS para interactuar con los usuarios en tiempo real y animarlos a completar sus compras."
tool: Canvas
---

# Intención abandonada {#abandoned-intent}

> Interactúa con los usuarios en tiempo real para animarlos a completar sus compras mientras los productos aún están frescos en su mente. Esta plantilla activada por API registra a los usuarios de inmediato cuando abandonan un carrito, envía recordatorios oportunos en el canal óptimo (correo electrónico, SMS o mensaje dentro de la aplicación), verifica la finalización de la compra en dos puntos del recorrido y sincroniza a los usuarios que no convierten con audiencias publicitarias para reorientación.

En este artículo, te guiaremos a través de un caso de uso de la plantilla **Abandoned Intent**, que está pensada para la etapa de consideración del ciclo de vida del usuario. Después de este artículo, habrás personalizado un recorrido de usuario que fomenta las compras de usuarios que no han realizado compras después de añadir artículos a sus carritos.

{% alert tip %}
Usa [BrazeAI Operator<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/operator) para configurar y personalizar esta plantilla. Selecciona **BrazeAI Operator<sup>TM</sup>** junto a tu perfil de usuario mientras creas o editas tu Canvas. Luego, describe tu objetivo, como "Ayúdame a configurar la plantilla Abandoned Intent para volver a captar a los usuarios que abandonaron su carrito".
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar esta plantilla con éxito, necesitarás lo siguiente:

- Un Canvas de recorrido de usuario posterior a la compra separado, ya que realizar una compra en este Canvas hará que los usuarios salgan del Canvas.
- Una [sincronización de audiencias de Braze]({{site.baseurl}}/partners/canvas_audience_sync) configurada con los socios y audiencias que utilizas.

## Adaptar la plantilla a tus necesidades {#tailoring-the-template-to-your-needs}

Supongamos que trabajamos en Kitchenerie, una marca de comercio minorista especializada en utensilios de cocina, y nuestro objetivo es volver a captar a los usuarios que han añadido el último producto "Enormous Paper Plate" a sus carritos pero no han realizado sus compras.

Antes de crear el Canvas, configuramos la integración de [sincronización de audiencias de Braze con Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) para poder añadir datos de usuario de Braze a Facebook Audiences y enviar anuncios basados en desencadenantes de comportamiento, segmentación y más.

La plantilla **Abandoned Intent** sigue este flujo: verificar la compra, enviar un recordatorio inmediato, esperar, dirigir al canal óptimo, hacer seguimiento, verificar de nuevo y reorientar a los que no convierten. Incluye los siguientes pasos:

| Paso en Canvas | Nombre del paso en la plantilla | Propósito |
|---|---|---|
| Rutas de acción | Made purchase? | Primera verificación de finalización; los usuarios que ya compraron salen del Canvas. |
| Mensaje | Itemized Reminder | Recordatorio inmediato del carrito enviado justo después de la entrada. |
| Retraso | Delay | Espera de 30 minutos para que el seguimiento llegue mientras el producto aún está fresco en la mente. |
| Rutas de audiencia | Intelligent Channel split | Dirige a los usuarios a correo electrónico o SMS según la clasificación de [canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel). |
| Mensaje | Abandoned Cart Email, Abandoned Cart SMS y Abandoned Cart In-App Message | Seguimientos específicos por canal. El canal inteligente selecciona entre correo electrónico y SMS; el mensaje dentro de la aplicación se envía en una ruta separada en la plantilla. |
| Rutas de acción | Made purchase? (2) | Segunda verificación de finalización antes de la reorientación. |
| Sincronización de audiencias | Ad Retargeting | Sincroniza a los que no convierten con audiencias publicitarias (como Facebook) para reorientación fuera del canal. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pasos de la plantilla Abandoned Intent" }

### Paso 1: Configura los detalles {#step-1-set-up-the-details}

Apliquemos la plantilla de Canvas y actualicemos los detalles para reflejar nuestro objetivo.

1. Ve a **Mensajería** > **Canvas**.
2. Selecciona **Crear Canvas** > **Usar una plantilla de Canvas**.
3. Selecciona la pestaña **Plantillas de Braze** y luego selecciona **Aplicar plantilla** junto a **Abandoned Intent**.
4. Actualiza la descripción para especificar que el Canvas está destinado a animar a los usuarios a completar compras del último lanzamiento de temporada de utensilios de cocina.
5. Añade la etiqueta **Intent** para poder filtrar por ella en la página de inicio de Canvas.

![El nuevo nombre, descripción y etiqueta del Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### Paso 2: Asigna tus eventos de conversión {#step-2-assign-your-conversion-events}

La plantilla establece el **Evento de conversión primaria - A** como **Makes Purchase (Legacy)** con **Make any purchase (Legacy)** seleccionado de forma predeterminada. Dado que nuestro enfoque está en nuestro producto "Enormous Paper Plate", personalizamos el evento de conversión de la siguiente manera:

1. Selecciona **Make a specific purchase (Legacy)**.
2. En **Product name**, introduce **Enormous Paper Plate**.

![Evento de conversión primaria - A con el tipo de conversión "Makes Purchase" con el nombre de producto "Enormous Paper Plate". Hay un plazo de conversión de 3 días.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

{% alert note %}
Si tu espacio de trabajo utiliza el evento de conversión **Places order**, las opciones relacionadas con compras pueden aparecer con **(Legacy)** en la etiqueta. Los pasos de este artículo utilizan el flujo de conversión de compra legacy.
{% endalert %}

### Paso 3: Establece un horario de entrada {#step-3-set-an-entry-schedule}

La plantilla **Abandoned Intent** utiliza un horario de entrada **desencadenado por API** para que puedas registrar a los usuarios en el Canvas tan pronto como abandonen su carrito. Esto se ajusta a nuestro caso de uso porque queremos responder mientras el producto aún está fresco en su mente.

1. Mantén **Desencadenado por API** como tipo de horario de entrada.
2. Toma nota del ID del Canvas y usa el [punto de conexión `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) para añadir usuarios cuando tu aplicación o sitio web detecte un carrito abandonado.
3. Opcionalmente, puedes pasar [variables de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) (como el nombre del producto o los detalles del carrito) para personalizar los mensajes posteriores.

Si prefieres una entrada basada en acciones, selecciona **Basado en acciones** y elige un desencadenante que coincida con la forma en que tu marca rastrea los carritos abandonados, por ejemplo, **Realizar evento personalizado** para un evento `abandoned_cart` registrado.

### Paso 4: Determina quién entra en el Canvas {#step-4-determine-who-enters-the-canvas}

A continuación, definamos nuestra audiencia objetivo como usuarios que han comprado exclusivamente en línea con nosotros en los últimos 90 días. Esto nos ayuda a reducir nuestra audiencia a usuarios que sabemos que están interactuando con nuestros productos.

!["Online Shoppers Segment - 90 Days" como el segmento de usuarios objetivo para este Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

Dejaremos los controles de entrada tal como están, para que los usuarios no puedan volver a entrar en este Canvas y no haya límite en el número de personas que potencialmente pueden entrar en este Canvas.

La plantilla no establece criterios de salida globales de forma predeterminada. En su lugar, los usuarios salen cuando realizan una compra en los pasos de Rutas de acción **Made purchase?**, que personalizaremos en el paso 6.

### Paso 5: Selecciona tus ajustes de envío {#step-5-select-your-send-settings}

Mantendremos la configuración de suscripción predeterminada, de modo que solo enviemos a usuarios que se hayan suscrito u optado por recibir mensajes o notificaciones, y dejaremos el resto de la configuración tal como está.

### Paso 6: Personaliza tu Canvas {#step-6-customize-your-canvas}

Personaliza los pasos del Canvas en el orden en que los usuarios los experimentan:

#### Verificar la compra en la entrada {#check-for-purchase-at-entry}

1. Selecciona el paso de Rutas de acción **Made purchase?** y luego selecciona el grupo de acciones **Made purchase**.
2. En **Make Purchase**, selecciona **Make a specific purchase (Legacy)** y elige **Enormous Paper Plate** como producto. Los usuarios que compren este producto saldrán del Canvas.

#### Enviar el recordatorio inmediato {#send-the-immediate-reminder}

1. Selecciona el paso de mensaje **Itemized Reminder** y luego selecciona **Edit message** para personalizar el primer correo electrónico de recordatorio. Este mensaje se envía inmediatamente después de la entrada, antes del retraso.
2. Mantén el paso de **Retraso** tal como está. La plantilla utiliza un retraso de 30 minutos antes de que se envíen los mensajes de seguimiento, dando a los usuarios tiempo para completar la compra mientras el producto aún está fresco en su mente.

{% alert tip %}
Puedes usar las [propiedades de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) para personalizar los mensajes en tu Canvas según el producto al que te refieras.
{% endalert %}

#### Dirigir al canal óptimo {#route-to-the-optimal-channel}

1. Revisa el paso de Rutas de audiencia **Intelligent Channel split**. Este dirige a los usuarios a **Abandoned Cart Email** o **Abandoned Cart SMS** según la clasificación de [canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel). Ajusta las rutas si es necesario.
2. Personaliza los pasos **Abandoned Cart Email**, **Abandoned Cart SMS** y **Abandoned Cart In-App Message**. Selecciona **Edit message** en cada paso para actualizar el texto y el mensaje de ese canal. El mensaje dentro de la aplicación se ejecuta en una ruta separada de la división de canal inteligente y no es seleccionado por la clasificación de canal inteligente.

#### Reorientar a los que no convierten {#retarget-non-converters}

1. Selecciona el paso de Rutas de acción **Made purchase? (2)** y luego selecciona el grupo de acciones **Made purchase**.
2. Selecciona **Make a specific purchase (Legacy)** y elige **Enormous Paper Plate** como producto. Los usuarios que compren aquí salen del Canvas antes de llegar a la reorientación.
3. Selecciona el paso de sincronización de audiencias **Ad Retargeting** y configúralo para sincronizar con Facebook. Los usuarios que lleguen a este paso no han comprado: sincronízalos con tu audiencia publicitaria para reorientación fuera del canal.

### Paso 7: Prueba y lanza el Canvas {#step-7-test-and-launch-the-canvas}

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como se espera, selecciona **Launch Canvas** para lanzar el Canvas. ¡Ahora podemos dirigirnos de manera consciente a los usuarios con un recorrido de usuario personalizado para animarlos a completar la compra del producto que han añadido a sus carritos!

{% alert tip %}
Consulta nuestra [lista de verificación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) para conocer las cosas a considerar antes y después de lanzar un Canvas.
{% endalert %}