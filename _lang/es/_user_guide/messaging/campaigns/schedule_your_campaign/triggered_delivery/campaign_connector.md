---
nav_title: Campaign Connector
article_title: Campaign Connector
page_order: 2
tool: Campaigns
page_type: tutorial
description: "Este artículo práctico explica qué es Campaign Connector y cómo usarlo para entregar contenido relevante y dirigido en el momento adecuado."

---
# Campaign Connector

> Campaign Connector te permite crear campañas que se desencadenan cuando los usuarios interactúan con campañas activas. Puedes entregar contenido relevante y dirigido en el momento adecuado.

## Cómo funciona {#how-it-works}

Esta característica te permite dirigirte a usuarios que completan las siguientes interacciones con campañas activas:

- Ver mensaje dentro de la aplicación
- Hacer clic en mensaje dentro de la aplicación
- Hacer clic en botones de mensaje dentro de la aplicación
- Hacer clic en correo electrónico
- Hacer clic en alias en correo electrónico
- Abrir correo electrónico
- Abrir directamente notificación push
- Hacer clic en botón de notificación push
- Hacer clic en página de historias push
- Realizar evento de conversión
- Recibir correo electrónico
- Recibir SMS
- Hacer clic en enlace acortado de SMS
- Recibir notificación push
- Recibir webhook
- Estar inscrito en un grupo de control
- Ver tarjeta de contenido
- Hacer clic en tarjeta de contenido
- Descartar tarjeta de contenido

{% alert important %}
Los desencadenadores de Campaign Connector no se pueden usar para desencadenar campañas de mensajes dentro de la aplicación. Los mensajes dentro de la aplicación solo se pueden desencadenar mediante eventos del SDK, como eventos personalizados o inicio de sesión. Para más información, consulta [Crear un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).
{% endalert %}

### Reglas de entrega {#delivery-rules}

Ten en cuenta que no puedes usar Campaign Connector para enviar un mensaje a un usuario después de que haya completado una interacción con una campaña. Por ejemplo, si estás ejecutando una campaña de marketing durante nueve semanas y configuras una campaña de seguimiento que usa Campaign Connector al inicio de la semana cuatro, la campaña de seguimiento solo entregará mensajes a los usuarios que interactuaron con la campaña de marketing después de que se publicó la campaña de seguimiento (semanas 4-9). Por lo tanto, para asegurarte de que tus campañas de seguimiento lleguen a todos los usuarios a los que te diriges, debes:

- Configurar tu campaña original como borrador
- Configurar y publicar tu campaña de seguimiento
- Publicar la campaña original

Estas reglas de entrega son particularmente relevantes si te diriges a usuarios que están inscritos en un grupo de control, reciben un correo electrónico o reciben una notificación push. Dado que los usuarios se inscribirán en el grupo de control tan pronto como publiques la campaña original, debes publicar la campaña de seguimiento antes de publicar la campaña original. De manera similar, si publicas la campaña original antes de la campaña de seguimiento, muchos usuarios pueden recibir tu correo electrónico y/o notificación push antes de que se publique la campaña de seguimiento.

## Usar Campaign Connector con tus campañas {#using-campaign-connector-with-your-campaigns}

### Paso 1: Crear una nueva campaña {#step-1-create-a-new-campaign}

Redacta los mensajes que deseas enviar a tus usuarios. Puedes seleccionar una campaña de un solo canal o una campaña multicanal, según tu caso de uso.

### Paso 2: Seleccionar la interacción y la campaña objetivo {#step-2-select-interaction-and-target-campaign}

1. Selecciona [**Entrega basada en acciones**]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) y añade el desencadenador "Interactuar con campaña" para dirigirte a usuarios que interactúan con una campaña activa.
2. Elige la interacción desencadenante.
3. A continuación, selecciona la campaña activa a la que deseas dirigirte.

![A continuación, selecciona la campaña activa a la que deseas dirigirte.]({% image_buster /assets/img_archive/Campaign_Connector1.png %})

### Paso 3: Establecer la demora de planificación y añadir excepciones (opcional) {#step-3-set-schedule-delay-and-add-exceptions-optional}

Si decides establecer una demora de planificación, puedes añadir una excepción a la acción desencadenante. Por ejemplo, es posible que quieras reenviar una campaña de correo electrónico a usuarios que no abrieron el correo electrónico original. En este escenario, puedes elegir "Recibió correo electrónico" como desencadenador y establecer una demora de planificación de una semana. Luego, puedes añadir "Abrir correo electrónico" como excepción. Ahora, reenviarás el correo electrónico a los usuarios que no abrieron el correo electrónico original en el plazo de una semana desde que lo recibieron.

![Si decides establecer una demora de planificación, puedes añadir una excepción a la acción desencadenante. Por ejemplo, es posible que quieras reenviar una campaña de correo electrónico a usuarios que no abrieron el correo electrónico original. En este escenario, puedes elegir "Recibió correo electrónico" como desencadenador y establecer una demora de planificación de una semana. Luego, puedes añadir "Abrir correo electrónico" como excepción. Ahora, reenviarás el correo electrónico a los usuarios que no abrieron el correo electrónico original en el plazo de una semana desde que lo recibieron.]({% image_buster /assets/img_archive/Campaign_Connector3.png %})

Los eventos de excepción solo se desencadenarán mientras un usuario esté esperando recibir el mensaje con el que está asociado. Si un usuario realiza la acción antes de esperar el mensaje, el evento de excepción no se desencadenará.

### Paso 4: Continuar con la creación de la campaña {#step-4-proceed-with-campaign-creation}

Continúa creando tu campaña como lo harías normalmente. Ten en cuenta que si quieres asegurarte de enviar un mensaje a todos los usuarios que van a interactuar con una campaña específica, lo mejor sería dirigirte a un segmento que contenga a todos los usuarios de tu aplicación.

## Casos de uso {#use-cases}

Puedes usar Campaign Connector para dirigirte a usuarios que interactúan o no interactúan con campañas activas.

Por ejemplo, podrías elegir dirigirte a usuarios que hicieron clic en un mensaje push promocional que anunciaba envío gratuito para enviarles un mensaje push promocional que ofrezca un 15 % de descuento en una compra.

Campaign Connector también puede dirigirse a usuarios que reciben una notificación push recordándoles que han abandonado su carrito. Por ejemplo, es posible que quieras reenviar la notificación a usuarios que no la abrieron directamente. Sin embargo, probablemente querrás excluir a los usuarios que hayan realizado una compra desde que enviaste la notificación original, incluso si no la abrieron directamente. Puedes lograr este caso de uso añadiendo un desencadenador "Recibió notificación push" para la campaña "Carrito abandonado", estableciendo una demora de planificación y añadiendo "Realiza compra" y "Abrió directamente notificaciones push" como excepciones.