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

Como buena práctica, Braze recomienda mantener cada línea de texto tanto del título opcional como del cuerpo del mensaje en aproximadamente 30-40 caracteres en una notificación push móvil. Ten en cuenta que el contador de caracteres del creador no tiene en cuenta los caracteres de Liquid. Esto significa que el recuento final de caracteres de un mensaje depende de cómo se renderice Liquid para cada usuario. En caso de duda, sé breve y conciso.

## Reduce el tamaño de la carga útil de las notificaciones push {#reduce-push-notification-payload-size}

El tamaño máximo de la carga útil depende de la plataforma.

| Plataforma | Tamaño máximo de la carga útil |
| --- | --- |
| Web | 3807 bytes |
| Android | 3930 bytes |
| iOS | 3960 bytes |
| Kindle | 5985 bytes |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reducir el tamaño de la carga útil de las notificaciones push" }

Si tu push supera el tamaño máximo de la carga útil, es posible que el mensaje no se envíe. Como buena práctica, mantén tu carga útil en unos pocos cientos de bytes.

### ¿Qué es una carga útil push? {#what-is-a-push-payload}

Los proveedores de servicios push calculan si tu notificación push puede mostrarse a un usuario observando el tamaño en bytes de toda la carga útil push. La carga útil está limitada a **4 KB (4096 bytes)** para la mayoría de los servicios push, incluyendo:

- Servicio de notificaciones push de Apple (APN)
- Firebase Cloud Messaging (FCM) de Android
- Notificación push web
- Push de Huawei

Estos servicios push rechazarán cualquier notificación que supere este límite.

Braze reserva una parte de la carga útil push para fines de integración y análisis. Dado esto, nuestro tamaño máximo de carga útil es de **3807 bytes**. Si tu push supera este tamaño, es posible que el mensaje no se envíe. Como buena práctica, mantén tu carga útil en unos pocos cientos de bytes.

Los siguientes elementos de tu push componen tu carga útil push:

- Texto, como el título y el cuerpo del mensaje
- Renderizado final de cualquier personalización con Liquid
- URLs de imágenes (pero no el tamaño de la imagen en sí)
- URLs de destinos de clic
- Nombres de botones
- Pares clave-valor

### Consejos para reducir el tamaño de la carga útil {#tips-to-reduce-payload-size}

Para reducir el tamaño de la carga útil:

- Mantén tu mensaje breve. Una buena pauta general es hacerlo accionable y beneficioso en menos de 40 caracteres.
- Omite espacios en blanco y saltos de línea de tu texto.
- Considera cómo se renderizará Liquid al enviar. Dado que el renderizado final de cualquier personalización con Liquid varía de un usuario a otro, Braze no puede determinar si una carga útil push superará el límite de tamaño cuando se incluye Liquid. Si tu Liquid renderiza un mensaje más corto, puede que no haya problema. Sin embargo, si tu Liquid resulta en un mensaje más largo, tu push puede superar el límite de tamaño de la carga útil. Siempre prueba tu mensaje push en un dispositivo real antes de enviarlo a los usuarios.
- Considera acortar las URLs usando un acortador de URLs.

## Optimiza la segmentación {#optimize-targeting}

### Recopila datos de usuario relevantes {#collect-relevant-user-data}

Las notificaciones push deben tratarse con cuidado para dirigirse a los usuarios con notificaciones oportunas y relevantes. Braze recopilará información útil del dispositivo y de uso que puede utilizarse para segmentar audiencias relevantes. Esta información debe complementarse con eventos personalizados y atributos específicos de tu aplicación. Usando esos datos, puedes dirigir cuidadosamente los mensajes para aumentar las tasas de apertura y disminuir los casos en que los usuarios desactivan las notificaciones push.

### Crea una página de configuración de notificaciones {#create-a-notification-settings-page}

Puedes crear una página de configuración en tu aplicación que permita a los usuarios indicar qué notificaciones desean recibir. Un enfoque común es crear un atributo personalizado booleano en Braze que corresponda al estado de configuración de la aplicación. Por ejemplo, una aplicación de noticias podría tener configuraciones de suscripción para noticias de última hora, deportes o política.

Cuando la aplicación de noticias quiere crear una Campaign dirigida solo a usuarios interesados en política, añade el filtro de atributo `Subscribes to Politics` al segmento. Cuando se establece como verdadero, solo los usuarios que se suscriban a las notificaciones las recibirán.

Para más información sobre cómo establecer atributos personalizados, consulta los siguientes artículos para [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes#setting-custom-attributes) o [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data#user-attributes-object-specification).

## Aumenta las adhesiones voluntarias y la relevancia {#increase-opt-ins-and-relevance}

### Obtén el permiso del usuario {#obtain-user-permission}

Las estadísticas generales de push habilitado se relacionan con si el usuario ha aprobado las notificaciones con su sistema operativo. Si los usuarios desactivan las notificaciones en iOS, se eliminarán automáticamente de nuestro sistema, ya que Apple no permitirá que se envíe el token de notificaciones push.

Android 13 y versiones posteriores requieren obtener permiso antes de que se puedan mostrar las notificaciones push. Las versiones anteriores de Android suscriben a los usuarios a las notificaciones de forma predeterminada.

### Prepara a los usuarios para las notificaciones push {#prime-users-for-push}

Solo tienes una oportunidad de pedir permiso de push a un usuario, y después de que lo rechace, es muy difícil convencerlo de volver a habilitar las notificaciones push en la configuración de su dispositivo. Por esta razón, debes preparar a los usuarios para las notificaciones push usando un mensaje dentro de la aplicación antes de mostrar el aviso del sistema. Consulta [Mensajes dentro de la aplicación de preparación para push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) para obtener más información sobre cómo aumentar las adhesiones voluntarias.

### Añade controles de suscripción push {#add-push-subscription-controls}

Para evitar que los usuarios desactiven las notificaciones a nivel de dispositivo, lo que elimina completamente su token de notificaciones push en primer plano, permite que los usuarios controlen su suscripción push directamente dentro de tu aplicación. Consulta [Actualización de los estados de suscripción push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states) para más detalles.

### Usa la planificación avanzada o añade retrasos {#use-advanced-scheduling-or-add-delays}

Dependiendo del tamaño de tu audiencia y de con cuánta anticipación se planifique tu mensaje push, puede haber retrasos en la entrega de las notificaciones push. El tiempo que tarda en enviar las notificaciones push depende de la capacidad de procesamiento asignada. Por ejemplo, si tu mensaje push utiliza varias llamadas de contenido conectado, esto puede aumentar la complejidad de la plantilla del mensaje push y puede resultar en velocidades limitadas por la rapidez con la que las APIs de terceros devuelven datos.

Una carga útil push más pequeña y una prioridad de notificación más alta pueden ayudar a reducir los retrasos y escalar tus mensajes. Puedes añadir `Push Enabled = true` en tu filtro de audiencia para reducir el tamaño de la audiencia de modo que solo se procesen los usuarios con push habilitado para el envío de la Campaign.

También recomendamos minimizar el número de llamadas a la API optimizando los datos que necesitas. Si es posible, intenta obtener todos los datos que necesitas en una sola llamada a la API en lugar de hacer múltiples llamadas.

### Comprende los estados de suscripción push {#understand-push-subscription-states}

El estado de suscripción push no garantiza que se entregue una notificación push; los usuarios también deben tener push habilitado para recibir notificaciones. Esto se debe a que un perfil de usuario puede tener múltiples dispositivos con diferentes permisos de push en primer plano, pero solo un único estado de suscripción push.

Si un usuario no tiene un token de notificaciones push en primer plano válido para una aplicación (es decir, desactiva los tokens de notificaciones push a nivel de dispositivo a través de la configuración, optando por no recibir notificaciones), su estado de suscripción aún puede considerarse `subscribed` a push. Sin embargo, este usuario no estaría como `Foreground Push Enabled for App` en Braze, ya que el token de notificaciones push en primer plano no es válido.

Además, si un perfil de usuario no tiene un token de notificaciones push válido o registrado para ninguna otra aplicación, su filtro `Foreground Push Enabled` en la segmentación también será falso.

## Implementa una política de desactivación para usuarios que no responden {#implement-a-sunset-policy-for-unresponsive-users}

Incluso cuando envías solo notificaciones push relevantes y oportunas, algunos usuarios pueden seguir sin responder a ellas y considerarlas correo no deseado. Supongamos que un usuario muestra un historial de ignorar repetidamente tus notificaciones push. En ese caso, es buena idea dejar de enviarle notificaciones push antes de que se moleste con las comunicaciones de tu aplicación o la desinstale por completo.

Para hacer esto, crea una [política de desactivación]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) que eventualmente deje de enviar notificaciones push a los usuarios que no hayan tenido una apertura directa o influenciada durante mucho tiempo.

1. Identifica a los usuarios que no responden basándote en las aperturas directas o influenciadas.
2. Deja de enviar gradualmente notificaciones push a esos usuarios.
3. Antes de eliminar las notificaciones push por completo, envía una última notificación explicando por qué ya no las recibirán. Esto les da a los usuarios la oportunidad de demostrar su interés en seguir recibiendo notificaciones push abriendo esa notificación.
4. Después de que la política de desactivación entre en vigor, usa un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages) para recordar a estos usuarios que, aunque ya no recibirán notificaciones push, los canales de mensajería dentro de la aplicación seguirán entregando información interesante y útil.

Aunque puedas ser reticente a dejar de enviar notificaciones push a usuarios que originalmente optaron por recibirlas, recuerda que otros canales de mensajería pueden llegar a estos usuarios de manera más efectiva, especialmente si han ignorado previamente tus notificaciones push. Si el usuario abre tus correos electrónicos, las campañas de correo electrónico son una buena forma de llegar a ellos fuera de tu aplicación. Si no, los mensajes dentro de la aplicación son la mejor manera de entregar contenido sin arriesgarte a que el usuario desinstale tu aplicación.

## Establece eventos de conversión para aperturas de la aplicación {#set-conversion-events-for-app-opens}

Al asignar [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) a una Campaign push, puedes rastrear las aperturas de la aplicación durante un cierto período después de que se reciba la Campaign. Establecer un evento de conversión para aperturas de la aplicación proporciona una perspectiva diferente de las estadísticas de resultados que normalmente recibes después de una Campaign push.

Mientras que todos los resultados de las Campaigns push desglosan las aperturas directas y las aperturas de un mensaje (que incluyen tanto las aperturas directas como las [aperturas influenciadas]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens)), el seguimiento de conversiones rastreará cualquier tipo de apertura, ya sea directa o influenciada.

Además, al usar el evento de conversión "abre la aplicación", estás rastreando las aperturas de la aplicación que ocurren antes de esa fecha límite de conversión (por ejemplo, tres días). Esto difiere de una apertura influenciada en que el tiempo que tiene un usuario para registrar una apertura influenciada puede variar de persona a persona, dependiendo del comportamiento de interacción pasado de cada usuario.

## Regulaciones de mensajes push {#push-message-regulations}

Dado que los mensajes push son un tipo de mensajería intrusiva que va directamente al teléfono o navegador de tu cliente, existen directrices para enviar mensajes push a través de aplicaciones y sitios.

### Regulaciones de push móvil para aplicaciones {#mobile-push-regulations-for-apps}

| Políticas de la App Store de Apple |
| --- |
| [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) Inaceptable: (i) Crear una interfaz para mostrar aplicaciones, extensiones o complementos de terceros similar a la App Store o como una colección de interés general. |
| [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) Las notificaciones push no deben ser necesarias para que la aplicación funcione, y no deben usarse para enviar información personal sensible o confidencial. Las notificaciones push no deben usarse con fines de promoción o marketing directo a menos que los clientes hayan optado explícitamente por recibirlas mediante un lenguaje de consentimiento mostrado en la interfaz de usuario de tu aplicación, y proporciones un método en tu aplicación para que el usuario deje de recibir dichos mensajes. |
| [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) No puedes monetizar las capacidades integradas proporcionadas por el hardware o el sistema operativo, como las notificaciones push, la cámara o el giroscopio; ni los servicios y tecnologías de Apple, como el acceso a Apple Music, el almacenamiento en iCloud o las APIs de Screen Time. |
{: .reset-td-br-1 aria-label="Regulaciones de push móvil para aplicaciones" }

| Política de Google Play Store |
| --- |
| [Uso no autorizado o imitación de funcionalidad del sistema](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) No permitimos aplicaciones o anuncios que imiten o interfieran con la funcionalidad del sistema, como notificaciones o advertencias. Las notificaciones a nivel del sistema solo pueden usarse para las características integrales de una aplicación, como una aplicación de aerolínea que notifica a los usuarios sobre ofertas especiales, o un juego que notifica a los usuarios sobre promociones dentro del juego. |
{: .reset-td-br-1 aria-label="Regulaciones de push móvil para aplicaciones" }

## Artículos relacionados {#related-articles}

¿No encontraste lo que buscabas? Consulta estos artículos adicionales de buenas prácticas:

- [Formatos de mensajes e imágenes push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)
- [Mensajes dentro de la aplicación de preparación para push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)
- [Capacidad de entrega para dispositivos Android chinos]({{site.baseurl}}/user_guide/channels/push/best_practices/chinese_push_deliverability)
- [Lo que debes saber antes de enviar: canales]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send)