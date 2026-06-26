{% if include.metric == "AMP Clicks" %}
<i>Clics AMP</i> es el número total de clics en tu correo electrónico AMP HTML, acumulado de las versiones HTML, texto sin formato y AMP HTML del correo electrónico.
{% endif %}

{% if include.metric == "AMP Opens" %}
<i>Aperturas AMP</i> es el recuento total de aperturas en tu correo electrónico AMP HTML y en las versiones AMP HTML del correo electrónico.
{% endif %}

{% if include.metric == "Audience" %}
La <i>audiencia</i> es el porcentaje de usuarios que recibieron un mensaje concreto. Este número se recibe de Braze.
{% endif %}

{% if include.metric == "Bounces" %}
<i>Rebotes</i> es el número total de mensajes que no se entregaron correctamente a los destinatarios previstos.
{% endif %}

{% if include.metric == "Estimated Real Opens" %}
Las <i>aperturas reales estimadas</i> son una estimación de cuántas aperturas únicas habría si no existieran las aperturas por máquina, y son el resultado de un modelo estadístico propio de Braze.
{% endif %}

{% if include.metric == "Help" %}
<i>Ayuda</i> es cuando un usuario respondió a tu mensaje con una <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">palabra clave AYUDA</a> y se le envió una respuesta automática de AYUDA.
{% endif %}

{% if include.metric == "Hard Bounce" %}
Un <i>rebote duro</i> es cuando un correo electrónico no se entrega al destinatario debido a un error de entrega permanente. Un rebote duro puede producirse porque el nombre de dominio no existe o porque el destinatario es desconocido.
{% endif %}

{% if include.metric == "Soft Bounce" %}
Un <i>rebote blando</i> es cuando un correo electrónico no se entrega al destinatario debido a un error temporal de entrega, aunque la dirección de correo electrónico del destinatario sea válida. Un rebote blando puede producirse porque el buzón de entrada del destinatario está lleno, el servidor no funcionaba o el mensaje era demasiado grande para el buzón de entrada del destinatario.
{% endif %}

{% if include.metric == "Deferral" %}
Un <i>aplazamiento</i> es cuando un correo electrónico no se entregó inmediatamente, pero Braze reintenta el correo electrónico hasta 72 horas después de este fallo de entrega temporal para maximizar las posibilidades de éxito en la entrega antes de que se detengan los intentos para esa Campaign específica.
{% endif %}

{% if include.metric == "Body Click" %}
Las notificaciones de historias push registran un <i>clic en el cuerpo</i> cuando se hace clic en la notificación. No se registrará cuando se expanda un mensaje ni para los clics en los botones de acción.
{% endif %}

{% if include.metric == "Body Clicks" %}
Los <i>clics en el cuerpo</i> se producen cuando un usuario hace clic en un mensaje que no tiene botones (Botón 1, Botón 2) y que se creó con el editor tradicional, y cuando un mensaje creado con el editor HTML o el editor de arrastrar y soltar utiliza <code>brazeBridge.logClick()</code> sin argumentos.
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>Clics en el botón 1</i> es el número total de clics en el botón 1 del mensaje.
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>Clics en el botón 2</i> es el número total de clics en el botón 2 del mensaje.
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>Opciones enviadas</i> es el número total de opciones seleccionadas cuando el usuario hace clic en el botón enviar de la página de preguntas de un <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>cuestionario simple</a>.
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
La <i>tasa de clics sobre aperturas</i> es el porcentaje de correos electrónicos abiertos en los que un usuario o una máquina ha hecho clic al menos una vez, y solo está disponible en el <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/data_and_analytics/reporting/report_builder/'>generador de informes</a>.
{% endif %}

{% if include.metric == "Close Message" %}
<i>Cerrar mensaje</i> es el número total de clics en el botón de cierre del mensaje. Esto solo existe para los mensajes dentro de la aplicación creados en el editor de arrastrar y soltar, no en el editor tradicional.
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
Las <i>entregas confirmadas</i> se producen cuando el operador ha confirmado que el mensaje se ha entregado en el número de teléfono de destino.
{% endif %}

{% if include.metric == "Confidence" %}
La <i>confianza</i> es el porcentaje de confianza en que una determinada variante de un mensaje supera al grupo de control.
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>Botón de página de confirmación</i> es el total de clics en el botón de llamada a la acción de la página de confirmación de un <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>cuestionario simple</a>.
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
Los <i>descartes de la página de confirmación</i> son el total de clics en el botón de cierre (x) de la página de confirmación de un <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>cuestionario simple</a>.
{% endif %}

{% if include.metric == "Conversion Rate" %}
La <i>tasa de conversión</i> es el porcentaje de veces que se ha producido un evento definido en comparación con todos los destinatarios de un mensaje. Este evento definido se determina cuando construyes la Campaign.
{% endif %}

{% if include.metric == "Conversion Window" %}
La <i>ventana de conversión</i> es el número de días después de recibir el mensaje durante los cuales se hace un seguimiento de las acciones del usuario y se atribuyen a un evento de conversión. Las conversiones que ocurren después de esta ventana no se atribuyen al evento de conversión.
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
Las <i>conversiones (B, C, D)</i> son eventos de conversión adicionales añadidos después del evento de conversión primaria. Es el número de veces que se produjo un evento definido después de interactuar con o ver un mensaje recibido de una Campaign de Braze.
{% endif %}

{% if include.metric == "Total Conversions" %}
<i>Conversiones totales</i> es el número total de veces que un usuario completa un evento de conversión específico después de ver una Campaign de mensajes dentro de la aplicación.
{% endif %}

{% if include.metric == "Deliveries" %}
<i>Entregas</i> es el número total (o porcentaje) de solicitudes de mensajes aceptadas por el servidor receptor. Esto no significa que el mensaje se haya entregado a un dispositivo, solo que el servidor ha aceptado el mensaje.
{% endif %}

{% if include.metric == "Deliveries %" %}
El <i>% de entregas</i> es el porcentaje del número total de mensajes (envíos) enviados y recibidos con éxito por las partes que pueden recibir correos electrónicos.
{% endif %}

{% if include.metric == "Delivery Failures" %}
Los <i>fallos de entrega</i> se producen cuando el SMS no se ha podido enviar porque se han desbordado las colas (envío de SMS a una tasa superior a la que pueden soportar tus códigos largo o abreviado).
{% endif %}

{% if include.metric == "Delivery Failures RCS" %}
Los <i>fallos de entrega</i> se producen cuando no se puede enviar el RCS debido al desbordamiento de las colas (envío de RCS a una tasa superior a la que puede gestionar tu remitente verificado por RCS).
{% endif %}

{% if include.metric == "Failed Delivery Rate" %}
La <i>tasa de entregas fallidas</i> es el porcentaje de envíos que fallaron porque no se pudo enviar el mensaje. Esto puede ocurrir por varias razones, como el desbordamiento de la cola, la suspensión de la cuenta y errores de medios en el caso de los MMS.
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>Direct Opens</i> es el número total (o porcentaje) de usuarios que abrieron tu aplicación o sitio web pulsando directamente la notificación.
{% endif %}

{% if include.metric == "Emailable" %}
<i>Con correo electrónico</i> es el número total de usuarios que tienen registrada una dirección de correo electrónico y han optado explícitamente por la adhesión voluntaria o se han suscrito.
{% endif %}

{% if include.metric == "Errors" %}
<i>Errores</i> es el número de errores devueltos por los eventos webhook (se incrementa durante el proceso de envío).
{% endif %}

{% if include.metric == "Failures" %}
Los <i>fallos</i> se producen cuando el mensaje de WhatsApp no se ha podido enviar porque el proveedor de servicios de Internet ha devuelto un rebote duro. Un rebote duro significa un fallo permanente en la capacidad de entrega.
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>Influenced Opens</i> es el número total (o porcentaje) de usuarios que abrieron la aplicación tras el envío de la notificación push, sin abrir directamente el push.
{% endif %}

{% if include.metric == "Lifetime Revenue" %}
Los <i>ingresos de toda la vida</i> son el valor total del precio de <code>PurchaseEvents</code> (en USD) recibido desde el inicio.
{% endif %}

{% if include.metric == "Lifetime Value Per User" %}
El <i>valor de duración del ciclo de vida por usuario</i> son los <i>ingresos de toda la vida</i> divididos por el total de tus <i>usuarios</i> (ubicados en tu página de inicio).
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
Los <i>ingresos medios diarios</i> son la media de la suma de los ingresos de la Campaign y de Canvas de un día determinado.
{% endif %}

{% if include.metric == "Daily Purchases" %}
<i>Compras diarias</i> es la media del total de <code>PurchaseEvents</code> únicos a lo largo del periodo de tiempo.
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
Los <i>ingresos diarios por usuario</i> son los ingresos medios diarios por usuario activo diario.
{% endif %}

{% if include.metric == "Machine Opens" %}
<i>Aperturas de máquina</i> incluye la proporción de «aperturas» que se ven afectadas por la protección de la privacidad en los correos electrónicos (MPP) de Apple para iOS 15. Por ejemplo, si un usuario abre un correo electrónico utilizando la aplicación Mail en un dispositivo Apple, esto se registrará como una <i>apertura de máquina</i>.
{% endif %}

{% if include.metric == "Other Opens" %}
<i>Otras aperturas</i> incluye correos electrónicos que no han sido identificados como <i>aperturas de máquina</i>. Por ejemplo, cuando un usuario abre un correo electrónico en otra plataforma (como la aplicación de Gmail en un teléfono, Gmail en un navegador de escritorio), esto se registrará como <i>otras aperturas</i>.
{% endif %}

{% if include.metric == "Opens" %}
Las <i>aperturas</i> son instancias que incluyen tanto <i>Direct Opens</i> como <i>Influenced Opens</i> en las que el SDK de Braze ha determinado, mediante un algoritmo propio, que una notificación push ha provocado que un usuario abra la aplicación.
{% endif %}

{% if include.metric == "Opt-Out" %}
La <i>exclusión voluntaria</i> se produce cuando un usuario responde a tu mensaje con una <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">palabra clave de exclusión voluntaria</a> y cancela la suscripción a tu programa SMS o RCS.
{% endif %}

{% if include.metric == "Pending Retry" %}
El <i>reintento pendiente</i> es el número de solicitudes que fueron rechazadas temporalmente por el servidor receptor, pero que el proveedor de servicios de correo electrónico (ESP) intentó volver a entregar. El ESP reintentará la entrega hasta que se alcance un tiempo de espera (normalmente después de 72 horas).
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>Conversiones primarias (A)</i> o <i>evento de conversión primaria</i> es el número de veces que se ha producido un evento definido tras interactuar con o ver un mensaje recibido de una Campaign de Braze. Este evento definido lo determinas tú al crear la Campaign.
{% endif %}

{% if include.metric == "Reads" %}
Las <i>lecturas</i> se producen cuando el usuario lee el mensaje. Los recibos de lectura del usuario deben estar «Activados» para que Braze realice un seguimiento de las lecturas.
{% endif %}

{% if include.metric == "Read Rate" %}
La <i>tasa de lectura</i> es el porcentaje de envíos que dieron lugar a una lectura. Solo se proporciona para los usuarios que tienen activados los recibos de lectura.
{% endif %}

{% if include.metric == "Received" %}
<i>Recibido</i> se define de forma diferente según el canal, y puede ser cuando los usuarios ven el mensaje, los usuarios realizan una acción desencadenante definida o el mensaje se envía al proveedor de mensajes.
{% endif %}

{% if include.metric == "Rejections" %}
Los <i>rechazos</i> se producen cuando el SMS o RCS ha sido rechazado por el operador. Esto puede ocurrir por varias razones, como el filtrado de contenidos del operador, la disponibilidad del dispositivo de destino, que el número de teléfono ya no esté en servicio, y similares.
{% endif %}

{% if include.metric == "Revenue" %}
Los <i>ingresos</i> son los ingresos totales en dólares de los destinatarios de la Campaign dentro de la <a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>ventana de conversión primaria</a> establecida.
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>Mensajes enviados</i> es el número total de mensajes enviados en una Campaign. Tras lanzar una Campaign programada, esta métrica incluirá todos los mensajes enviados, independientemente de si se han enviado ya debido a la limitación de tasa. Esto no significa que el mensaje se haya recibido o entregado a un dispositivo, solo que el mensaje se ha enviado.
{% endif %}

{% if include.metric == "Sent" %}
Se <i>envía</i> cada vez que se inicia o se desencadena una Campaign o un paso en Canvas, y se envía un SMS o RCS desde Braze. Es posible que el SMS o RCS no haya llegado al dispositivo del usuario debido a errores.
{% endif %}

{% if include.metric == "Sends" %}
<i>Envíos</i> es el número total de mensajes enviados en una Campaign. Tras lanzar una Campaign programada, esta métrica incluirá todos los mensajes enviados, independientemente de si se han enviado ya debido a la limitación de tasa. Esto no significa que el mensaje se haya recibido o entregado a un dispositivo, solo que el mensaje se ha enviado.
{% endif %}

{% if include.metric == "Sends to Carrier" %}
<i>Envíos al operador</i> está obsoleto, pero seguirá siendo compatible para los usuarios que ya lo tengan. Es la suma de las <i>entregas confirmadas</i>, los <i>rechazos</i> y los <i>envíos</i> cuya entrega o rechazo no fue confirmado por el operador. Esto incluye las instancias en las que los operadores no proporcionan la confirmación de entrega o rechazo, ya que algunos operadores no proporcionan esta confirmación o no pueden hacerlo en el momento del envío.
{% endif %}

{% if include.metric == "Sends to Carrier Rate" %}
La <i>tasa de envíos al operador</i> es el porcentaje del total de mensajes enviados que se clasificaron como <i>envíos al operador</i>. Esto incluye las instancias en las que los operadores no proporcionan confirmación de entrega o rechazo, ya que algunos operadores no proporcionan esta confirmación o no pueden hacerlo en el momento del envío. Esta métrica está obsoleta, pero seguirá siendo compatible para los usuarios que ya la tengan.
{% endif %}

{% if include.metric == "Spam" %}
El <i>correo no deseado</i> es el número total de correos electrónicos entregados que han sido marcados como «correo no deseado» por el destinatario. Aunque Braze no cambia el estado de suscripción de estos usuarios, estos quedarán automáticamente excluidos de futuros correos electrónicos, a menos que envíes un correo electrónico transaccional, que está configurado para «enviar a todos los usuarios, incluidos los que han cancelado la suscripción».
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
Los <i>descartes de la página del cuestionario</i> son el total de clics en el botón cerrar (x) de la página de preguntas de un <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>cuestionario simple</a>.
{% endif %}

{% if include.metric == "Survey Submissions" %}
Los <i>envíos de cuestionarios</i> son el total de clics en el botón de envío de un <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>cuestionario simple</a>.
{% endif %}

{% if include.metric == "Total Clicks" %}
El <i>total de clics</i> es el número (o porcentaje) de destinatarios únicos que han hecho clic en un enlace del mensaje entregado.
{% endif %}

{% if include.metric == "Total Dismissals" %}
El <i>total de descartes</i> es el número de veces que los usuarios descartaron un mensaje de una Campaign. Para Content Cards, esto cuenta cada descarte de tarjeta. Para los Banners, esto cuenta cada vez que un usuario descartó el Banner cuando el comportamiento de descarte está habilitado.
{% endif %}

{% if include.metric == "Total Impressions" %}
Las <i>impresiones totales</i> son el número de veces que se ve un mensaje. Braze registra una impresión solo cuando el mensaje se hace visible para el usuario en su pantalla. Por ejemplo, si un mensaje se coloca en la parte inferior de una página, la impresión no se registra hasta que el usuario se desplaza hacia abajo y el mensaje queda a la vista. Si a un usuario se le muestra el mismo mensaje dos veces, contará como dos impresiones.
{% endif %}

{% if include.metric == "Total Opens" %}
<i>Aperturas totales</i> es el número total de mensajes que se abrieron.
{% endif %}

{% if include.metric == "Total Revenue" %}
Los <i>ingresos totales</i> son los ingresos totales en dólares de los destinatarios de la Campaign dentro de la ventana de conversión primaria establecida.
{% endif %}

{% if include.metric == "Unique Clicks" %}
Los <i>clics únicos</i> son el número diferenciado de destinatarios que han hecho clic en un enlace dentro de un mensaje al menos una vez y se miden mediante <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/messaging/messaging_fundamentals/dispatch_id/'>dispatch_id</a>.
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>Descartes únicos</i> es el número de destinatarios únicos que descartaron una Content Card de una Campaign. Un usuario que descarta varias veces una Content Card de una Campaign representa un único descarte.
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
Las <i>impresiones únicas</i> son el número total de usuarios que han visto un mensaje de una Campaign determinada. Una impresión solo se registra cuando el mensaje se hace visible en la pantalla de un usuario.
{% endif %}

{% if include.metric == "Unique Daily Impressions" %}
Las <i>impresiones diarias únicas</i> son el número de usuarios únicos que vieron el mensaje en un día determinado. Este recuento se restablece cada día natural, por lo que un usuario que ve el mismo mensaje en dos días diferentes se cuenta dos veces. Esta métrica se alinea con la métrica de facturación del mismo nombre.
{% endif %}

{% if include.metric == "Unique Recipients" %}
Los <i>destinatarios únicos</i> son el número de destinatarios únicos diarios, o usuarios que recibieron un nuevo mensaje en un día. Para que este recuento se incremente más de una vez para un usuario, este debe recibir un nuevo mensaje en un día diferente.
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>Aperturas únicas</i> es el número total (o porcentaje) de mensajes entregados que han sido abiertos por un único usuario al menos una vez y que son objeto de seguimiento durante un periodo de siete días.
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>Cancelaciones de suscripción</i> o <i>Desuscritos</i> es el número de mensajes que dan lugar a una cancelación de suscripción. Las cancelaciones de suscripción se producen cuando Braze procesa una cancelación de suscripción desde la URL de cancelación de suscripción de Braze en el cuerpo del mensaje o desde el encabezado list-unsubscribe cuando esa ruta es gestionada por Braze.
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>Cancelaciones de suscripción</i> es el número de destinatarios cuyo estado de suscripción cambió a cancelado desde una ruta de cancelación de suscripción gestionada por Braze, incluida la URL de cancelación de suscripción de Braze en el cuerpo del mensaje y list-unsubscribe cuando Braze procesa la solicitud.
{% endif %}

{% if include.metric == "Variation" %}
<i>Variación</i> es el número de variaciones de una Campaign, diferentes según las defina el creador.
{% endif %}