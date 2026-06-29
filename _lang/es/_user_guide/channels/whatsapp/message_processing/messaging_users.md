---
nav_title: "Mensajes de usuario"
article_title: "Mensajes de usuario de WhatsApp"
description: "Este artículo de referencia cubre cómo Braze gestiona los mensajes de los usuarios."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /whatsapp_quick_replies/

---

# Mensajes de usuario {#user-messages}

> WhatsApp es un canal de comunicación bidireccional. Tu marca no solo puede enviar mensajes a los usuarios, sino que ellos también pueden participar en conversaciones utilizando Campaigns y Canvas con plantillas. Hay varias formas de hacerlo, incluyendo respuestas rápidas de WhatsApp, mensajes de lista y palabras desencadenantes. Las llamadas a la acción (CTA) de respuestas rápidas y mensajes de lista son una excelente manera de fomentar la interacción de los usuarios con tu mensajería de WhatsApp.

## Desencadenantes basados en acciones {#action-based-triggers}

Tanto las campañas como los Canvas pueden iniciarse, ramificarse y tener cambios a mitad del recorrido a partir de un mensaje entrante de WhatsApp (un usuario que envía un mensaje a tu WhatsApp), como una palabra desencadenante.

Asegúrate de que tu palabra desencadenante coincida con lo que esperas de los usuarios.

**Cosas que debes saber:**
- Cada letra de tu palabra desencadenante debe estar en mayúsculas cuando se configura. Braze no requiere que las palabras desencadenantes entrantes enviadas por los usuarios estén en mayúsculas. Por ejemplo, enviar "jOin2023" seguirá desencadenando el Canvas o la campaña.
- Si no se especifica ninguna palabra desencadenante en el desencadenante basado en acciones del horario de entrada, la campaña o el Canvas se ejecutará para TODOS los mensajes entrantes de WhatsApp. Esto incluye mensajes que coincidan con frases en campañas y Canvas activos, en cuyo caso el usuario recibirá dos mensajes de WhatsApp.

{% tabs %}
{% tab Campaign %}

![Opciones de planificación de Campaign basada en acciones.]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

{% endtab %}
{% tab Canvas %}

![Opciones de planificación de Canvas basado en acciones.]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

{% endtab %}
{% endtabs %}

## Respuestas no reconocidas {#unrecognized-responses}

Recomendamos que incluyas una opción para respuestas no reconocidas en Canvas interactivos. Esto guía a los usuarios para que comprendan cuáles son las indicaciones disponibles y establece expectativas para el canal. La gestión de expectativas puede ser especialmente útil si tienes canales de WhatsApp con chat de agente en vivo.
- En el paso de acción, después de crear los grupos de acción para las frases de filtro personalizadas, agrega un grupo de acción adicional para "Enviar mensaje de WhatsApp", pero **no marques Where the message body**. Esto capturará todas las respuestas de usuario no reconocidas, similar a una cláusula "else".
- Recomendamos hacer un seguimiento con un mensaje de WhatsApp informando al usuario que este canal no está atendido y guiándolo a un canal de soporte si es necesario.

## Respuestas rápidas {#quick-replies}

![Pantalla de teléfono que muestra que un botón de llamada a la acción responderá con el texto del botón seleccionado.]({% image_buster /assets/img/whatsapp/whatsapp11.png %}){: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

Las respuestas rápidas aparecen como opciones de botones clicables dentro de la conversación, pero actúan como si un usuario hubiera respondido con texto. Braze luego procesa estos como mensajes entrantes y puede enviar respuestas configuradas según el botón seleccionado. Usa el paso de acción "Inbound WhatsApp message action" al crear y filtrar respuestas de tus usuarios.

![Un mensaje de WhatsApp que muestra texto y tres botones de llamada a la acción.]({% image_buster /assets/img/whatsapp/whatsapp13.png %}){: style="max-width:50%;"}

### Configurar la experiencia de respuesta rápida en Canvas {#configure-the-quick-reply-experience-in-canvas}

#### Paso 1: Crear los CTA {#step-1-build-out-ctas}

Primero, crea tus CTA de respuesta rápida en el [Administrador de plantillas de mensajes de WhatsApp](https://business.facebook.com/wa/manage/message-templates/) dentro de una plantilla de mensaje.

![La interfaz del administrador de plantillas de mensajes de WhatsApp que muestra cómo crear un botón CTA, proporcionando el tipo de botón (personalizado) y el texto del botón.]({% image_buster /assets/img/whatsapp/whatsapp12.png %}){: style="max-width:80%;"}

Una vez que tu plantilla haya sido enviada y aprobada por WhatsApp, puedes usarla para crear un Canvas dentro de Braze.

{% alert tip %}
Puedes crear el Canvas antes de recibir la aprobación de tu plantilla de mensaje.
{% endalert %}

#### Paso 2: Crear tu Canvas {#step-2-build-your-canvas}

A continuación, crea un Canvas con un paso de mensaje que incluya tu plantilla creada.

![Creador de mensajes del paso de WhatsApp con una plantilla de respuesta rápida completada.]({% image_buster /assets/img/whatsapp/whatsapp14.png %})

Crea un paso de acción que siga al paso de mensaje. Crea un grupo por cada opción de respuesta rápida en este paso de acción.

![Un Canvas donde la acción de evaluación es "enviar un mensaje entrante de WhatsApp".]({% image_buster /assets/img/whatsapp/whatsapp15.png %})

Para cada grupo de opciones de respuesta rápida, especifica el texto exacto del botón que estás emparejando. Ten en cuenta que las palabras clave deben estar en mayúsculas.

![Un paso de Canvas donde la acción "enviar un mensaje entrante de WhatsApp" está configurada para enviarse cuando se recibe un cuerpo de mensaje específico.]({% image_buster /assets/img/whatsapp/whatsapp16.png %})

Si deseas una respuesta predeterminada para los usuarios que responden al mensaje con texto en lugar de respuestas rápidas, crea un grupo adicional sin cuerpo de mensaje coincidente.

Continúa construyendo el Canvas como lo harías normalmente a partir de este punto.

### Respuestas {#responses}

Lo más probable es que quieras un mensaje de respuesta para cada respuesta. Recomendamos tener una opción general para respuestas fuera del alcance de las respuestas rápidas (como para clientes que responden con un mensaje general en lugar de una indicación predeterminada). Por ejemplo, "Lo sentimos, no reconocimos tu respuesta. Para problemas de soporte, por favor envía un mensaje a <canal de soporte>."

![Un Canvas construido que muestra las respuestas para cada botón de llamada a la acción.]({% image_buster /assets/img/whatsapp/whatsapp18.png %})

Ten en cuenta que puedes usar cualquier acción posterior que ofrece Braze Canvas, como mensajes en respuesta, actualizaciones de perfil de usuario o webhooks de Braze a Braze.

## Mensajes de lista {#list-messages}

Los mensajes de lista aparecen como un mensaje de cuerpo con una lista de opciones clicables. Cada lista puede tener múltiples secciones, y cada lista puede tener hasta 10 filas.

![Ejemplo de un mensaje de lista de WhatsApp con filas para diferentes estilos de moda.]({% image_buster /assets/img/whatsapp/list_message_example.png %}){: style="max-width:40%;"}

### Configurar la experiencia de mensaje de lista en Canvas {#configure-the-list-message-experience-in-canvas}

#### Paso 1: Crear o editar un Canvas basado en acciones existente {#step-1-create-or-edit-an-existing-action-based-canvases}

Solo puedes agregar mensajes de lista de WhatsApp a Canvas que estén basados en acciones, ya que necesitan ser en respuesta a un mensaje de usuario.

#### Paso 2: Crear un paso de mensaje de WhatsApp {#step-2-create-a-whatsapp-message-step}

Agrega un [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) de WhatsApp y luego selecciona el diseño de mensaje de respuesta de **List Message**.

![Una colección seleccionable de los diferentes tipos de mensajes de respuesta de WhatsApp que puedes crear, incluyendo "List Message".]({% image_buster /assets/img/whatsapp/list_message_option.png %}){: style="max-width:70%;"}

Agrega un nombre de **List button** que los usuarios seleccionarán para mostrar tu lista. Luego, usa los campos en **List content** para crear tu lista:

- **Section:** Agrega hasta 10 secciones para agrupar y organizar los elementos de tu lista. Por ejemplo, un minorista de ropa podría usar secciones para organizar por estilos de temporada (como primavera, verano, otoño e invierno) o artículos de ropa (como tops, pantalones y zapatos).
- **Row:** Agrega hasta 10 filas, o elementos de lista, en todas las secciones.
- **Row description (optional):** Agrega una descripción opcional a todas las filas (elementos de lista).

![La sección "List content" completada con dos secciones, y varias filas y descripciones de filas.]({% image_buster /assets/img/whatsapp/list_content.png %}){: style="max-width:60%;"}

Cambia el orden de las secciones y filas seleccionando y arrastrando el icono junto a sus nombres.

![Arrastrando una sección de lista a una nueva ubicación.]({% image_buster /assets/img/whatsapp/drag_list_order.png %}){: style="max-width:60%;"}

De vuelta en el creador de Canvas, agrega una [ruta de acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) después del paso de mensaje que tenga un grupo para cada respuesta de lista. En cada grupo:

1. Agrega un desencadenante para **Sent inbound WhatsApp subscription group** y selecciona el grupo de suscripción de WhatsApp correspondiente.
2. Marca la casilla **Where the message body**.
3. Especifica el contenido de una fila (o elemento de lista).

![Creador de una ruta de acción con grupos para diferentes estilos de ropa.]({% image_buster /assets/img/whatsapp/action_path_list_message.png %})

Continúa construyendo tu Canvas.

### Crear rutas de acción para descripciones largas {#creating-actions-paths-for-long-descriptions}

Si tienes descripciones de filas, debes usar **Matches regex** para especificar una fila. Por ejemplo, si quieres especificar una fila con la descripción "Nuestro nuevo estilo que se ajusta sobre tu par favorito de botines", podrías usar [regex]({{site.baseurl}}/user_guide/audience/segments/regex) con "botines".

![Un desencadenante de WhatsApp que usa el filtro "Matches regex" para capturar mensajes de respuesta con "ankle boots".]({% image_buster /assets/img/whatsapp/regex_list_message.png %})

## Consideraciones {#considerations}

### Requisitos de tiempo para mensajes de respuesta {#timing-requirements-for-response-messages}

Los mensajes de respuesta deben enviarse dentro de las 24 horas posteriores a la recepción del mensaje de un usuario. Para ayudar a crear experiencias exitosas, Braze verifica la lógica del mensaje para confirmar que hay un mensaje entrante del usuario anterior que desbloquea el mensaje de respuesta.

Los siguientes eventos desbloquean los mensajes de respuesta:

- Mensaje entrante
  - [Ruta de acción]({{site.baseurl}}/action_paths) o [entrada basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) con el desencadenante **Send a WhatsApp inbound message**.

![Un paso de entrada basado en acciones con el desencadenante "Send a WhatsApp inbound message".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message_trigger.png %})

- [Entrada desencadenada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)
- Mensaje de producto entrante
  - Evento [`ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events?tab=ecommerce.cart_updated)

![Una ruta de acción con el desencadenante de un evento personalizado realizado `ecommerce.cart_updated`.]({% image_buster /assets/img/whatsapp/ecommerce_cart_updated.png %})

### Filtrar por un atributo de tiempo personalizado {#filtering-by-a-custom-time-attribute}

Si la audiencia de tu Campaign o Canvas de WhatsApp basado en acciones depende de un atributo de tiempo personalizado que cae dentro de una ventana relativa (por ejemplo, entre ahora y las próximas 24 horas), combina dos filtros como se describe en [Tiempo]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes#time).

### Almacenamiento de medios entrantes y expiración de URL {#inbound-media-storage-and-url-expiration}

Cuando un usuario envía un mensaje de WhatsApp que contiene medios (como una imagen, un archivo de audio o un documento), Braze almacena esos medios en Amazon S3 durante 30 días a partir del momento en que se recibe el mensaje.

Sin embargo, el campo Liquid `inbound_media_urls`, que hace referencia a la URL de esos medios, es válido durante siete días a partir del momento en que Braze recibe el mensaje entrante. Dado que la URL se genera una sola vez en el momento de la recepción y no se regenera, la ventana de siete días aplica independientemente de cuándo accedas al campo. El límite más corto de los dos es el que aplica, por lo que en la práctica, `inbound_media_urls` debe considerarse válido por un máximo de siete días.

{% alert note %}
Si guardas un valor de `inbound_media_urls` en un atributo personalizado de usuario para usarlo más adelante, ten en cuenta esta expiración de siete días. Intentar acceder a la URL después de que haya expirado resultará en un enlace roto.
{% endalert %}