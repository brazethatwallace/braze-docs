---
nav_title: Carrito abandonado
article_title: Carrito abandonado
page_order: 1
page_type: reference
description: "Este artículo describe cómo utilizar una plantilla de Braze Canvas para interactuar con los usuarios en tiempo real y animarlos a completar sus compras."
tool: Canvas
---

# Carrito abandonado {#abandoned-cart}

> Interactúa con los usuarios en tiempo real para animarlos a completar sus compras. Usa esta plantilla para crear un recorrido de usuario que se centre en enviar mensajes oportunos y personalizados que recuerden a los usuarios sus carritos abandonados, destacando los beneficios del producto y ofreciendo incentivos, como códigos de descuento.

En este artículo, te guiaremos a través de un caso de uso de la plantilla **Abandoned Intent**, que está pensada para la etapa de consideración del ciclo de vida del usuario. Después de este artículo, habrás personalizado un recorrido de usuario que fomenta las compras de usuarios que no han realizado compras después de añadir artículos a sus carritos.

## Requisitos previos {#prerequisites}

Para utilizar esta plantilla con éxito, necesitarás lo siguiente:

- Un Canvas de recorrido de usuario posterior a la compra separado, ya que realizar una compra en este Canvas hará que los usuarios salgan del Canvas.
- Una [sincronización de audiencias de Braze]({{site.baseurl}}/partners/canvas_audience_sync/) configurada con los socios y audiencias que utilizas.

## Adaptar la plantilla a tus necesidades {#tailoring-the-template-to-your-needs}

Supongamos que trabajamos en Kitchenerie, una marca de comercio minorista especializada en utensilios de cocina, y nuestro objetivo es volver a captar a los usuarios que han añadido el último producto "Enormous Paper Plate" a sus carritos pero no han realizado sus compras.

Antes de crear el Canvas, configuramos la integración de [sincronización de audiencias de Braze con Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) para poder añadir datos de usuario de Braze a Facebook Audiences y enviar anuncios basados en desencadenantes de comportamiento, segmentación y más.

Para acceder a la plantilla de intención abandonada, al crear un nuevo Canvas, selecciona **Usar una plantilla de Canvas** > **Plantillas de Braze**. Luego, junto a **Abandoned Intent**, selecciona **Apply Template**. Ahora podemos revisar la plantilla para adaptarla a nuestras necesidades.

### Paso 1: Configura los detalles {#step-1-set-up-the-details}

Ajustemos los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Edit** junto al nombre de la plantilla.

![El título y la descripción actuales del Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2. Actualiza el nombre del Canvas para especificar que el Canvas está dirigido a usuarios con carritos abandonados.
3. Actualiza la descripción para especificar que el Canvas está destinado a animar a los usuarios a completar compras del último lanzamiento de temporada de utensilios de cocina.
4. Añade la etiqueta **Abandon Cart** para poder filtrar por ella en la página de inicio de Canvas.

![El nuevo nombre, descripción y etiqueta del Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### Paso 2: Asigna tus eventos de conversión {#step-2-assign-your-conversion-events}

A continuación, asignemos nuestro evento de conversión. Dado que nuestro enfoque está en nuestro producto "Enormous Paper Plate", haremos lo siguiente para el **evento de conversión primaria A**:

1. Para el **tipo de evento de conversión**, selecciona **Makes Purchase**.
2. Selecciona **Make a specific purchase**. Esto nos permite seleccionar un nombre de producto específico.
3. Selecciona **Enormous Paper Plate**.

![Evento de conversión primaria - A con el tipo de conversión "Makes Purchase" con el nombre de producto "Enormous Paper Plate". Hay un plazo de conversión de 3 días.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

### Paso 3: Establece un horario de entrada {#step-3-set-an-entry-schedule}

Aunque el horario de entrada de esta plantilla está configurado como **desencadenado por API**, nuestro caso de uso se beneficiará más de una entrada basada en acciones para este Canvas, ya que queremos centrarnos en los usuarios que han abandonado su carrito (lo cual es una acción).

1. Selecciona **Action-Based** como tipo de horario de entrada.
2. Selecciona **Abandoned Cart** como desencadenante.
3. Para la ventana de entrada, selecciona la fecha de hora de inicio.
4. Selecciona la opción para permitir que los usuarios entren en su zona horaria local. Esto puede mantener nuestros mensajes relevantes y generar mayor interacción si los mensajes se envían en momentos óptimos.

![Un Canvas basado en acciones que se dirige a usuarios que han abandonado su carrito, con la ventana de entrada del 15 de octubre de 2024 a las 3:20 pm en la zona horaria local de los usuarios.]({% image_buster /assets/img/canvas_templates/abandoned_intent2.png %})

### Paso 4: Determina quién entra en el Canvas {#step-4-determine-who-enters-the-canvas}

A continuación, definamos nuestra audiencia objetivo como usuarios que han comprado exclusivamente en línea con nosotros en los últimos 90 días. Esto nos ayuda a reducir nuestra audiencia a usuarios que sabemos que están interactuando con nuestros productos.

!["Online Shoppers Segment - 90 Days" como el segmento de usuarios objetivo para este Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

Dejaremos los controles de entrada tal como están, para que los usuarios no puedan volver a entrar en este Canvas y no haya límite en el número de personas que potencialmente pueden entrar en este Canvas.

Para los criterios de salida, los usuarios saldrán del Canvas si han comprado el "Enormous Paper Plate". De esta manera, no recibirán más mensajes sobre un artículo que ya han comprado.

![Criterios de salida que determinan que los usuarios que realicen una compra específica del Enormous Paper Plate saldrán del Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent4.png %})

### Paso 5: Selecciona tus ajustes de envío {#step-5-select-your-send-settings}

Mantendremos la configuración de suscripción predeterminada, de modo que solo enviemos a usuarios que se hayan suscrito u optado por recibir mensajes o notificaciones, y dejaremos el resto de la configuración tal como está.

### Paso 6: Personaliza tu Canvas {#step-6-customize-your-canvas}

Ahora, construiremos nuestro Canvas personalizando los pasos de la plantilla:

1. Selecciona el paso de Rutas de acción y luego selecciona el nombre del grupo de acciones **Made purchase**.
2. Para **Make Purchase**, selecciona **Make A Specific Purchase** y elige **Enormous Paper Plate** como producto. De manera similar a los criterios de salida, los usuarios que compren este producto saldrán del Canvas.

![Grupo de acciones "Made purchase" que hará que el usuario salga del Canvas si compra el Enormous Paper Plate.]({% image_buster /assets/img/canvas_templates/abandoned_intent5.png %})

{: start="3"}
3. Para el paso de mensaje, selecciona **Edit message** para personalizar el correo electrónico que se enviará a nuestros usuarios, notificándoles sobre los artículos en su carrito abandonado.
4. Mantén el paso de retraso tal como está.
5. En los pasos de mensaje posteriores al paso de ruta de audiencia, personalizaremos el correo electrónico y el mensaje SMS que recibirán nuestros usuarios. Aquí es donde queremos animar a nuestros usuarios a comprar productos con mensajes personalizados.

![Una vista previa del mensaje SMS que recibirán los usuarios: "Hi there, you left the enormous paper plate behind in your cart! Complete your purchase now and step up your hosting game. Use code MYPLATE at checkout for 20 percent off your order!"]({% image_buster /assets/img/canvas_templates/abandoned_intent6.png %})

{: start="6"}
6. En el siguiente paso de Rutas de acción, selecciona el grupo de acciones **Made purchase**. Luego, selecciona **Make a specific purchase** y elige **Enormous Paper Plate** como producto. Este paso reflejará el primer paso de Rutas de acción al hacer que los usuarios que hayan comprado nuestro producto salgan para que no reciban más mensajes.
7. Asegúrate de que nuestro paso de sincronización de audiencias esté configurado para sincronizar con Facebook. Esto ayudará aún más con la reorientación de anuncios.

{% alert tip %}
Puedes usar las [propiedades de entrada de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/) para personalizar los mensajes en tu Canvas según el producto al que te refieras.
{% endalert %}

### Paso 7: Prueba y lanza el Canvas {#step-7-test-and-launch-the-canvas}

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como se espera, selecciona **Launch Canvas** para lanzar el Canvas. ¡Ahora podemos dirigirnos de manera consciente a los usuarios con un recorrido de usuario personalizado para animarlos a completar la compra del producto que han añadido a sus carritos!

{% alert tip %}
Consulta nuestra [lista de verificación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para conocer las cosas a considerar antes y después de lanzar un Canvas.
{% endalert %}