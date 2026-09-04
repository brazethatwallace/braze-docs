---
page_order: 22
nav_title: Buenas prácticas
article_title: Buenas prácticas de push
description: "Esta página contiene buenas prácticas y casos de uso de push para asegurarte de que tus mensajes push inspiren interacción en lugar de molestia."
channel: push
---

# Buenas prácticas de push {#push-best-practices}

> Esta página contiene buenas prácticas y casos de uso de push para asegurarte de que tus mensajes push inspiren interacción en lugar de molestia.

Las notificaciones push son herramientas poderosas para interactuar con los usuarios de tu aplicación, pero deben usarse con cuidado para garantizar que entreguen mensajes oportunos y relevantes. Antes de enviar tu mensaje push, consulta las siguientes buenas prácticas sobre lo que debes saber y verificar.

{% alert important %}
Tus mensajes push deben cumplir con las directrices de la App Store de Apple y las políticas de Google Play Store, especialmente en lo que respecta al uso de mensajes push como anuncios, correo no deseado, promociones y más. En esta página, consulta [Regulaciones de mensajes push](#push-message-regulations).
{% endalert %}

## Redacta tu mensaje push {#compose-your-push-message}

Como buena práctica, Braze recomienda mantener cada línea de texto, tanto del título opcional como del cuerpo del mensaje, en aproximadamente 30-40 caracteres en una notificación push móvil. Ten en cuenta que el contador de caracteres del creador no tiene en cuenta los caracteres de Liquid. Esto significa que el recuento final de caracteres de un mensaje depende de cómo Liquid se renderiza para cada usuario. En caso de duda, sé breve y conciso.

## Reducir el tamaño de la carga útil de las notificaciones push {#reduce-push-notification-payload-size}

El tamaño máximo de la carga útil depende de la plataforma.

| Plataforma | Tamaño máximo de la carga útil |
| --- | --- |
| Web | 3807 bytes |
| Android | 3930 bytes |
| iOS | 3960 bytes |
| Kindle | 5985 bytes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reducir el tamaño de la carga útil de las notificaciones push" }

Si tu notificación push supera el tamaño máximo de la carga útil, es posible que el mensaje no se envíe. Como buena práctica, mantén tu carga útil en unos pocos cientos de bytes.

### ¿Qué es una carga útil push? {#what-is-a-push-payload}

Los proveedores de servicios de notificaciones push calculan si tu notificación push puede mostrarse a un usuario observando el tamaño en bytes de toda la carga útil push. La carga útil está limitada a **4 KB (4096 bytes)** en la mayoría de los servicios push, incluidos:

- El servicio de notificaciones push de Apple (APN)
- Firebase Cloud Messaging (FCM) de Android
- Notificación push web
- Notificación push de Huawei

Estos servicios push rechazarán cualquier notificación que supere este límite.

Braze reserva una parte de la carga útil push con fines de integración y análisis. Dado esto, nuestro tamaño máximo de carga útil es de **3807 bytes**. Si tu notificación push supera este tamaño, es posible que el mensaje no se envíe. Como buena práctica, mantén tu carga útil en unos pocos cientos de bytes.

Los siguientes elementos de tu notificación push componen la carga útil push:

- Texto, como el título y el cuerpo del mensaje
- El resultado final de cualquier personalización con Liquid
- URL de las imágenes (pero no el tamaño de la imagen en sí)
- URL de los destinos de clic
- Nombres de los botones
- Pares clave-valor

### Consejos para reducir el tamaño de la carga útil {#tips-to-reduce-payload-size}

Para reducir el tamaño de la carga útil:

- Mantén tu mensaje breve. Una buena pauta general es hacerlo accionable y útil en menos de 40 caracteres.
- Omite los espacios en blanco y los saltos de línea de tu texto.
- Considera cómo se renderizará Liquid en el envío. Dado que el resultado final de cualquier personalización con Liquid varía de un usuario a otro, Braze no puede determinar si la carga útil push superará el límite de tamaño cuando se incluye Liquid. Si tu Liquid produce un mensaje más corto, es posible que no haya problema. Sin embargo, si tu Liquid genera un mensaje más largo, tu notificación push podría superar el límite de tamaño de la carga útil. Siempre prueba tu mensaje push en un dispositivo real antes de enviarlo a los usuarios.
- Considera acortar las URL utilizando un acortador de URL.

## Optimizar la segmentación {#optimize-targeting}

### Recopilar datos de usuario relevantes {#collect-relevant-user-data}

Las notificaciones push deben tratarse con cuidado para dirigirse a los usuarios con notificaciones oportunas y relevantes. Braze recopilará información útil sobre el dispositivo y el uso, que puede utilizarse para segmentar audiencias relevantes. Esta información debe complementarse con eventos personalizados y atributos específicos de tu aplicación. Con esos datos, puedes dirigir los mensajes cuidadosamente para aumentar las tasas de apertura y reducir los casos en que los usuarios desactivan las notificaciones push.

### Crear una página de configuración de notificaciones {#create-a-notification-settings-page}

Puedes crear una página de configuración en tu aplicación que permita a los usuarios indicar qué notificaciones desean recibir. Un enfoque común es crear un atributo personalizado booleano en Braze que corresponda al estado de la configuración de la aplicación. Por ejemplo, una aplicación de noticias podría tener configuraciones de suscripción para noticias de última hora, deportes o política.

Cuando la aplicación de noticias quiera crear una Campaign dirigida solo a usuarios interesados en política, se añade el filtro de atributo `Subscribes to Politics` al Segment. Cuando se establece como verdadero, solo los usuarios que se suscriban a las notificaciones las recibirán.

Para obtener más información sobre cómo configurar atributos personalizados, consulta los siguientes artículos para [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android) o [REST API]({{site.baseurl}}/api/objects_filters/user_attributes_object).

## Aumenta las adhesiones voluntarias y la relevancia {#increase-opt-ins-and-relevance}

### Obtén el permiso del usuario {#obtain-user-permission}

Las estadísticas generales de push habilitado se relacionan con si el usuario aprobó las notificaciones con su sistema operativo. Si los usuarios desactivan las notificaciones en iOS, se eliminarán automáticamente de nuestro sistema, ya que Apple no permitirá que se envíe el token de notificaciones push.

Android 13 y versiones posteriores requieren obtener permiso antes de que se puedan mostrar las notificaciones push. Las versiones anteriores de Android suscriben a los usuarios a las notificaciones de forma predeterminada.

### Prepara a los usuarios para push {#prime-users-for-push}

Solo tienes una oportunidad de pedirle a un usuario permiso para push, y una vez que lo rechaza, es muy difícil convencerlo de volver a habilitar push en la configuración de su dispositivo. Por esta razón, deberías preparar a los usuarios para push usando un mensaje dentro de la aplicación antes de mostrar la solicitud del sistema. Consulta [Mensajes dentro de la aplicación de preparación para push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) para obtener más información sobre cómo aumentar las adhesiones voluntarias.

### Agrega controles de suscripción push {#add-push-subscription-controls}

Para evitar que los usuarios desactiven las notificaciones a nivel de dispositivo, lo que elimina por completo su token de push en primer plano, permite que los usuarios controlen su suscripción push directamente dentro de tu aplicación. Consulta [Actualización de los estados de suscripción push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states) para obtener más detalles.

### Usa la programación avanzada o agrega retrasos {#use-advanced-scheduling-or-add-delays}

Dependiendo del tamaño de tu audiencia y con cuánta antelación esté programado tu mensaje push, puede haber retrasos en la entrega de push. El tiempo que se tarda en enviar los push depende de la potencia de procesamiento asignada. Por ejemplo, si tu mensaje push utiliza varias llamadas de contenido conectado, esto puede aumentar la complejidad de la creación de la plantilla del mensaje push y puede dar como resultado velocidades limitadas por la rapidez con la que las API de terceros devuelven los datos.

Una carga útil de push más pequeña y una mayor prioridad de notificación pueden ayudar a reducir los retrasos y escalar tus mensajes. Puedes agregar `Push Enabled = true` en tu filtro de audiencia para reducir el tamaño de la audiencia, de modo que solo se procesen los usuarios con push habilitado para el envío de la Campaign.

También recomendamos minimizar el número de llamadas a la API optimizando los datos que necesitas. Si es posible, intenta obtener todos los datos que necesitas en una sola llamada a la API en lugar de realizar múltiples llamadas.

### Comprende los estados de suscripción push {#understand-push-subscription-states}

El estado de suscripción push no garantiza que se entregue un push: los usuarios también deben tener push habilitado para recibir notificaciones. Esto se debe a que un perfil de usuario puede tener varios dispositivos con diferentes permisos de push en primer plano, pero solo un estado de suscripción push único.

Si un usuario no tiene un token de push en primer plano válido para una aplicación (es decir, desactiva los tokens de push a nivel de dispositivo a través de la configuración, optando por no recibir notificaciones), su estado de suscripción aún puede considerarse `subscribed` a push. Sin embargo, este usuario no estaría `Foreground Push Enabled for App` en Braze, ya que el token de push en primer plano no es válido.

Además, si un perfil de usuario no tiene un token de push válido o registrado para ninguna otra aplicación, su filtro `Foreground Push Enabled` en la segmentación también será falso.

## Implementa una política de extinción para usuarios no receptivos {#implement-a-sunset-policy-for-unresponsive-users}

Incluso cuando envías solo notificaciones push relevantes y oportunas, algunos usuarios pueden seguir sin responder a ellas y considerarlas correo no deseado. Supón que un usuario muestra un historial de ignorar repetidamente tus notificaciones push. En ese caso, es buena idea dejar de enviarle notificaciones push antes de que se moleste con las comunicaciones de tu aplicación o la desinstale por completo.

Para ello, crea una [política de extinción]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) que con el tiempo deje de enviar notificaciones push a los usuarios que no hayan tenido un Direct Opens o un Influenced Opens durante mucho tiempo.

1. Identifica a los usuarios no receptivos en función de los Direct Opens o Influenced Opens.
2. Deja de enviar notificaciones push a esos usuarios de forma gradual.
3. Antes de eliminar las notificaciones push por completo, envía una última notificación explicando por qué ya no las recibirán. Esto les da la oportunidad de demostrar su interés en seguir recibiendo notificaciones push abriendo esa notificación.
4. Una vez que la política de extinción entre en vigor, utiliza un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages) para recordar a estos usuarios que, aunque ya no recibirán notificaciones push, los canales de mensajería dentro de la aplicación seguirán proporcionándoles información interesante y útil.

Aunque puedas ser reacio a dejar de enviar notificaciones push a usuarios que originalmente se suscribieron, recuerda que otros canales de mensajería pueden llegar a estos usuarios de manera más efectiva, especialmente si previamente han ignorado tus notificaciones push. Si el usuario abre tus correos electrónicos, las campañas de correo electrónico son una buena forma de llegar a él fuera de tu aplicación. Si no, los mensajes dentro de la aplicación son la mejor manera de entregar contenido sin arriesgarte a que el usuario desinstale tu aplicación.

## Establecer eventos de conversión para aperturas de la aplicación {#set-conversion-events-for-app-opens}

Al asignar [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) a una Campaign push, puedes hacer seguimiento de las aperturas de la aplicación durante un periodo determinado después de que se reciba la Campaign. Establecer un evento de conversión para aperturas de la aplicación proporciona información diferente a las estadísticas de resultados que normalmente recibes después de una Campaign push.

Aunque todos los resultados de una Campaign push desglosan las aperturas directas y las aperturas de un mensaje (que incluyen tanto las aperturas directas como las [Influenced Opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens)), el seguimiento de conversiones rastreará cualquier tipo de apertura, ya sea directa o influenciada.

Además, al utilizar el evento de conversión "abre la aplicación", estás rastreando las aperturas de la aplicación que ocurren antes de la fecha límite de conversión (por ejemplo, tres días). Esto difiere de una apertura influenciada en que el tiempo que tiene un usuario para registrar una apertura influenciada puede variar de persona a persona, dependiendo del comportamiento de participación anterior de cada usuario.

## Regulaciones de mensajes push {#push-message-regulations}

Dado que los mensajes push son un tipo de mensajería intrusiva que llega directamente al teléfono o navegador de tu cliente, existen directrices para enviar mensajes push a través de aplicaciones y sitios.

### Regulaciones de push para dispositivos móviles en aplicaciones {#mobile-push-regulations-for-apps}

| Políticas del Apple App Store |
| --- |
| [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Inaceptable: (i) Crear una interfaz para mostrar aplicaciones, extensiones o complementos de terceros similar al App Store o como una colección de interés general. |
| [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) Las notificaciones push no deben ser necesarias para que la aplicación funcione y no deben utilizarse para enviar información personal sensible o confidencial. Las notificaciones push no deben utilizarse con fines promocionales o de marketing directo, a menos que los clientes hayan dado su consentimiento explícito para recibirlas mediante un texto de consentimiento mostrado en la interfaz de tu aplicación, y proporciones un método en tu aplicación para que el usuario pueda dejar de recibir dichos mensajes. |
| [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) No puedes monetizar capacidades integradas proporcionadas por el hardware o el sistema operativo, como las notificaciones push, la cámara o el giroscopio; ni servicios y tecnologías de Apple, como el acceso a Apple Music, el almacenamiento en iCloud o las API de Screen Time. |
{: .reset-td-br-1 aria-label="Regulaciones de push para dispositivos móviles en aplicaciones" }

| Política de Google Play Store |
| --- |
| [Uso no autorizado o imitación de funciones del sistema](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) No permitimos aplicaciones ni anuncios que imiten o interfieran con funciones del sistema, como notificaciones o advertencias. Las notificaciones a nivel de sistema solo pueden utilizarse para funciones esenciales de una aplicación, como una aplicación de aerolínea que notifica a los usuarios sobre ofertas especiales, o un juego que notifica a los usuarios sobre promociones dentro del juego. |
{: .reset-td-br-1 aria-label="Regulaciones de push para dispositivos móviles en aplicaciones" }

## Artículos relacionados {#related-articles}

¿No encontraste lo que buscabas? Consulta estos artículos adicionales sobre buenas prácticas:

- [Formatos de mensajes e imágenes push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)
- [Mensajes push primer dentro de la aplicación]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)
- [Capacidad de entrega para dispositivos Android en China]({{site.baseurl}}/user_guide/channels/push/best_practices/chinese_push_deliverability)
- [Lo que debes saber antes de enviar: canales]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send)