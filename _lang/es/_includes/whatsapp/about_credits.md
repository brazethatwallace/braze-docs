A partir del 1 de julio de 2025, WhatsApp ahora cobra por mensaje. Las tarifas de los mensajes se basan tanto en el código de país del número de teléfono del destinatario como en el tipo de mensaje que estás enviando. El tipo de mensaje se determina a partir de la [plantilla de mensaje](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/) que envías para aprobación en WhatsApp Administrador.

{% alert note %}
Todas las conversaciones iniciadas por la empresa en la plataforma deben comenzar con un mensaje de plantilla aprobado.
{% endalert %}

{% if include.content == "h2" %}##{% else include.content == "h3" %}###{% endif %} Definiciones de plantillas de mensaje

Estas son las plantillas de mensaje que puedes enviar para aprobación en WhatsApp Administrador:

| Plantilla | Definición |
|----------|------------|
| **Plantilla de marketing**     | Esta plantilla te permite lograr una amplia gama de objetivos, desde generar conocimiento de marca hasta impulsar ventas y reorientar clientes. Los ejemplos incluyen anuncios de nuevos productos, servicios o características, promociones u ofertas dirigidas, y recordatorios de abandono del carrito de compras. |
| **Plantilla de utilidad**       | Esta plantilla te permite dar seguimiento a acciones o solicitudes de los usuarios, ya que estos mensajes suelen ser desencadenados por acciones del usuario. Los ejemplos incluyen confirmación de adhesión voluntaria, gestión de pedidos o entregas (como actualizaciones de entrega), actualizaciones o alertas de cuenta (como recordatorios de pago), o cuestionarios de retroalimentación.<br><br>A partir del 1 de julio de 2025:<br>• Las plantillas de utilidad deben ser no promocionales y sin ninguna intención persuasiva.<br>• Las plantillas de utilidad deben ser (1) específicas para el usuario o solicitadas por él, o (2) esenciales o críticas para el usuario. |
| **Plantilla de autenticación** | Esta plantilla te permite verificar la identidad de un usuario, potencialmente en varias etapas del recorrido del cliente (como verificación de cuenta, recuperación de cuenta y desafíos de integridad).<br><br>Las conversaciones de autenticación solo serán compatibles caso por caso y Braze no puede garantizar SLA específicos. Además, Braze no admite la generación de PIN. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% if include.content == "h2" %}##{% else include.content == "h3" %}###{% endif %} Tipos de mensajes gratuitos

Estos son algunos escenarios en los que tu mensaje de WhatsApp será gratuito:

| Mensaje | Detalles |
|-------|-------|
| Todas las conversaciones de servicio | _A partir del 1 de noviembre de 2024_<br><br>Cuando un usuario envía un mensaje a tu marca (iniciando la ventana de servicio al cliente de 24 horas), los mensajes de respuesta sin plantilla no se cobran. Nota: si tu marca responde al usuario con una plantilla, se te cobrará según el tipo de plantilla. |
| Plantillas de utilidad enviadas durante una ventana de servicio al cliente de 24 horas | _A partir del 1 de julio de 2025_<br><br>Se crea una ventana de servicio al cliente de 24 horas cuando un usuario final envía un mensaje a tu marca. Si tu marca responde con una plantilla de utilidad, será gratuito. Las plantillas de utilidad enviadas fuera de una ventana de servicio al cliente de 24 horas (por ejemplo, plantillas de utilidad enviadas proactivamente por tu marca para cosas como recordatorios de cuenta y actualizaciones de estado del pedido) seguirán siendo cobradas. |
| Conversaciones de punto de entrada gratuitas | Se abre una conversación de punto de entrada gratuita si 1) un usuario envía un mensaje a tu marca a través de un anuncio de clic a WhatsApp o un botón de llamada a la acción de una página de Facebook y 2) tu marca responde en un plazo de 24 horas. La conversación de punto de entrada gratuita se abre tan pronto como tu marca responde y dura 72 horas. Dentro de la ventana de 72 horas, tu marca puede enviar plantillas de mensaje a los usuarios de forma gratuita. Sin embargo, tu marca solo puede enviar mensajes sin plantilla si hay una ventana de servicio al cliente de 24 horas abierta. |
| Mensajes de respuesta | La mensajería de respuesta permite a tu marca enviar mensajes sin plantilla en respuesta a los mensajes de los usuarios. Los mensajes de respuesta se pueden enviar cuando hay una ventana de servicio al cliente de 24 horas abierta, como cuando un usuario envía un mensaje a tu marca en WhatsApp.<br><br>Ten en cuenta que el mensaje de plantilla que inicia la conversación seguirá siendo cobrado, pero los mensajes de respuesta posteriores serán gratuitos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}