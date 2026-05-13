---
nav_title: "Configuración avanzada de campañas push"
article_title: "Configuración avanzada de campañas push"
page_order: 5
page_layout: reference
description: "Este artículo de referencia cubre algunas configuraciones avanzadas de campañas push como prioridad, URL personalizadas, opciones de entrega y más."
platform: Android
channel:
  - push
tool:
  - Campaigns

---

# Configuración avanzada de campañas push {#advanced-push-campaign-settings}

> Hay muchas configuraciones avanzadas disponibles para las notificaciones push de Android y Fire OS enviadas a través del panel de Braze. Este artículo describirá estas características y cómo usarlas con éxito.

## ID de notificación {#notification-id}

Un ID de notificación es un identificador único para una categoría de mensaje de tu elección que indica al servicio de mensajería que solo respete el mensaje más reciente de ese ID. Establecer un ID de notificación te permite enviar solo el mensaje más reciente y relevante, en lugar de una pila de mensajes obsoletos e irrelevantes.

Para asignar un ID de notificación, navega a la página de composición del push al que deseas agregar el ID y selecciona la pestaña **Settings**. Ingresa un número entero en la sección **Notification ID**. Para actualizar esta notificación después de haberla emitido, envía otra notificación con el mismo ID que usaste anteriormente.

![Campo de ID de notificación.]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:60%;" }

## Tiempo de vida (TTL) {#ttl}

El campo **Time to Live** te permite establecer una duración personalizada para almacenar mensajes con el servicio de mensajería push. Si el dispositivo permanece sin conexión más allá del TTL, el mensaje expirará y no se entregará.

Para editar el tiempo de vida de tu push de Android, ve al compositor y selecciona la pestaña **Settings**. Encuentra el campo **Time to Live** e ingresa un valor en días, horas o segundos.

Los valores predeterminados para el tiempo de vida son definidos por tu administrador en la página de [Configuración de push]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings/). De forma predeterminada, Braze establece el TTL de push en el valor máximo para cada servicio de mensajería push. Aunque la configuración predeterminada del TTL se aplica globalmente, puedes anularla a nivel de mensaje durante la creación de la campaña. Esto es útil cuando diferentes campañas requieren distintos niveles de urgencia o ventanas de entrega.

Por ejemplo, supongamos que tu aplicación organiza un concurso de trivia semanal. Envías una notificación push una hora antes de que comience. Al establecer el TTL en 1 hora, te aseguras de que los usuarios que abran la aplicación después de que el concurso haya comenzado no reciban una notificación sobre un evento que ya ha iniciado.

{% details Mejores prácticas %}

#### Cuándo usar un TTL más corto {#when-to-use-shorter-ttl}

Los TTL más cortos aseguran que los usuarios reciban notificaciones oportunas para eventos o promociones que pierden relevancia rápidamente. Por ejemplo:

- **Comercio minorista:** Enviar un push para una venta relámpago que termina en 2 horas (TTL: 1-2 horas)
- **Entrega de comida:** Notificar a los usuarios cuando su pedido está cerca (TTL: 10-15 minutos)
- **Aplicaciones de transporte:** Compartir actualizaciones de llegada del viaje (TTL: unos pocos minutos)
- **Recordatorios de eventos:** Notificar a los usuarios cuando un seminario web está por comenzar (TTL: menos de 1 hora)

#### Cuándo evitar un TTL más corto {#when-to-avoid-shorter-ttl}

- Si el mensaje de tu campaña sigue siendo relevante durante varios días o semanas, como recordatorios de renovación de suscripción o promociones en curso.
- Cuando maximizar el alcance es más importante que la urgencia, como con anuncios de actualización de la aplicación o promociones de características.

{% enddetails %}

## Prioridad de entrega de Firebase Messaging {#fcm-priority}

El campo **Firebase Messaging Delivery Priority** te permite controlar si un push se envía con prioridad "normal" o "alta" a Firebase Cloud Messaging. Esta configuración determina la rapidez con la que se entregan los mensajes y cómo afectan la duración de la batería del dispositivo.

| Prioridad | Descripción | Ideal para |
|---------|-------------|----------|
| Normal | Entrega optimizada para la batería que puede retrasarse para conservar batería | Contenido no urgente, ofertas promocionales, actualizaciones de noticias |
| Alta | Entrega inmediata con mayor consumo de batería | Notificaciones urgentes, alertas críticas, actualizaciones de eventos en vivo, alertas de cuenta, noticias de última hora o recordatorios urgentes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Firebase messaging delivery priority #fcm-priority" }

#### Consideraciones {#considerations}

- **Configuración predeterminada**: Puedes establecer una prioridad FCM predeterminada para todas las campañas de Android en tu [Configuración de push]({{site.baseurl}}/user_guide/administer/global/workspace_settings/push_settings/). Esta configuración a nivel de campaña anulará la predeterminada si es necesario.
- **Reducción de prioridad**: Si FCM detecta que tu aplicación envía frecuentemente mensajes de alta prioridad que no resultan en notificaciones visibles para el usuario o en interacción del usuario, esos mensajes pueden ser automáticamente reducidos a prioridad normal.
- **Impacto en la batería**: Los mensajes de alta prioridad despiertan los dispositivos en reposo de manera más agresiva y consumen más batería. Usa esta prioridad con prudencia.

Para información más detallada sobre el manejo de mensajes y la reducción de prioridad, consulta la [documentación de FCM](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) y [Manejo de mensajes y reducción de prioridad en Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority#deprioritize).

## Texto de resumen {#summary-text}

El texto de resumen te permite establecer texto adicional en la vista expandida de la notificación. También sirve como pie de foto para notificaciones con imágenes.

![Un mensaje de Android con el título "Este es el título de la notificación." y texto de resumen "Este es el texto de resumen de la notificación."]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

El texto de resumen se mostrará debajo del cuerpo del mensaje en la vista expandida.

![Un mensaje de Android con el título "Este es el título de la notificación." y texto de resumen "Este es el texto de resumen de la notificación."]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Para las notificaciones push que incluyen imágenes, el texto del mensaje se mostrará en la vista contraída, mientras que el texto de resumen se mostrará como pie de foto de la imagen cuando la notificación se expanda.

## URI personalizadas {#custom-uris}

La característica **Custom URI** te permite especificar una URL web o un recurso de Android al que navegar cuando se hace clic en la notificación. Si no se especifica una URI personalizada, al hacer clic en la notificación se lleva a los usuarios a tu aplicación. Puedes usar la URI personalizada para crear enlaces profundos dentro de tu aplicación, así como dirigir a los usuarios a recursos que existen fuera de tu aplicación. Esto se puede especificar a través de nuestra [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) o en la pestaña **Compose** del compositor de push.

![Campo de URI personalizada.]({% image_buster /assets/img_archive/deep_link.png %}){: style="max-width:60%;"}

## Prioridad de visualización de notificaciones {#notification-display-priority}

{% multi_lang_include alerts/important_alerts.md alert='Android notification priority' %}

El nivel de prioridad de una notificación push afecta cómo se muestra tu notificación en la bandeja de notificaciones en relación con otras notificaciones. También puede afectar la velocidad y la forma de entrega, ya que los mensajes de prioridad normal e inferior pueden enviarse con una latencia ligeramente mayor o agrupados para preservar la duración de la batería, mientras que los mensajes de alta prioridad siempre se envían de inmediato.

Esta característica es útil para diferenciar tus mensajes según lo críticos o urgentes que sean. Por ejemplo, una notificación sobre condiciones peligrosas en la carretera sería una buena candidata para recibir una prioridad alta, mientras que una notificación sobre una venta en curso debería recibir una prioridad más baja. Deberías considerar si usar una prioridad disruptiva es realmente necesario para la notificación que estás enviando, ya que ocupar constantemente el primer lugar en el buzón de entrada de tus usuarios o interrumpir sus otras actividades puede tener un impacto negativo.

En Android O, la prioridad de notificación se convirtió en una propiedad de los canales de notificación. Necesitarás trabajar con tu desarrollador para definir la prioridad de un canal durante su configuración y luego usar el dashboard para seleccionar el canal adecuado al enviar los sonidos de tu notificación. Para dispositivos que ejecutan versiones de Android anteriores a O, es posible especificar un nivel de prioridad para las notificaciones de Android y Fire OS a través del panel de Braze y la API de mensajería.

Para enviar mensajes a toda tu base de usuarios con una prioridad específica, te recomendamos que especifiques la prioridad indirectamente a través de la [configuración de canales de notificación](https://developer.android.com/training/notify-user/channels#importance) (para dispositivos O+) y envíes la prioridad individual desde el dashboard (para dispositivos &#60;O).

Consulta la siguiente tabla para los niveles de prioridad que puedes establecer en las notificaciones push de Android o Fire OS:

| Prioridad | Descripción | Valor de `priority` (para mensajes de API) |
|------|-----------|----------------------------|
| Máxima | Mensajes urgentes o de tiempo crítico. | `2` |
| Alta | Comunicación importante, como un nuevo mensaje de un amigo. | `1` |
| Predeterminada | La mayoría de las notificaciones. Úsala si tu mensaje no cae explícitamente en ninguno de los otros tipos de prioridad. | `0` |
| Baja | Información que deseas que los usuarios conozcan pero que no requiere acción inmediata. | `-1`|
| Mínima | Información contextual o de fondo. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Notification display priority" }

Para más información, consulta la documentación de Google sobre [notificaciones de Android](http://developer.android.com/design/patterns/notifications.html).

## Categoría de push {#push-category}

Las notificaciones push de Android ofrecen la opción de especificar si tu notificación pertenece a una categoría predefinida. La interfaz del sistema Android puede usar esta categoría para tomar decisiones de clasificación o filtrado sobre dónde colocar la notificación en la bandeja de notificaciones del usuario.

![Pestaña de configuración con la categoría establecida en Ninguna, que es la configuración predeterminada.]({% image_buster /assets/img_archive/braze_category.png %}){: style="max-width:60%;"}

| Categoría | Descripción |
|---|-------|
| Ninguna | Opción predeterminada. |
| Alarma | Alarma o temporizador. |
| Llamada | Llamada entrante (voz o video) o solicitud de comunicación sincrónica similar. |
| Correo electrónico | Mensaje masivo asíncrono (correo electrónico). |
| Error | Error en una operación en segundo plano o estado de autenticación. |
| Evento | Evento de calendario. |
| Mensaje | Mensaje directo entrante (SMS, mensaje instantáneo, etc.). |
| Progreso | Progreso de una operación en segundo plano de larga duración. |
| Promoción | Promoción o anuncio. |
| Recomendación | Una recomendación específica y oportuna para un solo elemento. |
| Recordatorio | Recordatorio programado por el usuario. |
| Servicio | Indicación de servicio en segundo plano en ejecución. |
| Social | Actualización de red social o de uso compartido. |
| Estado | Información continua sobre el dispositivo o estado contextual. |
| Sistema | Actualización de estado del sistema o dispositivo. Reservado para uso del sistema. |
| Transporte | Control de transporte multimedia para reproducción. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push category" }

## Visibilidad de push {#push-visibility}

Las notificaciones push de Android proporcionan un campo opcional para determinar cómo aparece una notificación en la pantalla de bloqueo del usuario. Consulta la siguiente tabla para las opciones de visibilidad y sus descripciones.

| Visibilidad | Descripción |
|---|-----|
| Pública | La notificación aparece en la pantalla de bloqueo |
| Privada | La notificación se muestra con "Contenido oculto" como mensaje |
| Secreta | La notificación no se muestra en la pantalla de bloqueo |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push visibility" }

Además, los usuarios de Android pueden anular cómo aparecen las notificaciones push en su pantalla de bloqueo cambiando la configuración de privacidad de notificaciones en su dispositivo. Esta configuración anulará la visibilidad de la notificación push.

![Ubicación de la prioridad push en el dashboard con la opción Establecer visibilidad habilitada y configurada como Privada.]({% image_buster /assets/img_archive/braze_visibility.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Independientemente de la visibilidad, todas las notificaciones se mostrarán en la pantalla de bloqueo del usuario si la configuración de privacidad de notificaciones en su dispositivo es **Mostrar todo el contenido** (configuración predeterminada). Del mismo modo, las notificaciones no se mostrarán en su pantalla de bloqueo si su privacidad de notificaciones está configurada como **No mostrar notificaciones**. La visibilidad solo tiene efecto si su privacidad de notificaciones está configurada como **Ocultar contenido sensible**.

La visibilidad no tiene efecto en dispositivos anteriores a Android Lollipop 5.0.0, lo que significa que todas las notificaciones se mostrarán en estos dispositivos.

Consulta nuestra [documentación de Android](https://developer.android.com/guide/topics/ui/notifiers/notifications) para más información.

## Sonidos de notificación {#notification-sounds}

En Android O, los sonidos de notificación se convirtieron en una propiedad de los canales de notificación. Necesitarás trabajar con tu desarrollador para definir el sonido de un canal durante su configuración y luego usar el dashboard para seleccionar el canal adecuado al enviar tus notificaciones.

Para dispositivos que ejecutan versiones de Android anteriores a Android O, Braze te permite establecer el sonido de un mensaje push individual a través del compositor del dashboard. Puedes hacerlo especificando un recurso de sonido local en el dispositivo (por ejemplo, `android.resource://com.mycompany.myapp/raw/mysound`).

Seleccionar **Default** en este campo reproducirá el sonido de notificación predeterminado en el dispositivo. Esto se puede especificar a través de nuestra [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) o en **Settings** en el compositor de push.

![El campo "Sonido".]({% image_buster /assets/img_archive/sound_android.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

A continuación, ingresa la URI completa del recurso de sonido (por ejemplo, `android.resource://com.mycompany.myapp/raw/mysound`) en el campo del dashboard.

Para enviar mensajes a toda tu base de usuarios con un sonido específico, te recomendamos que especifiques el sonido indirectamente a través de la [configuración de canales de notificación](https://developer.android.com/training/notify-user/channels) (para dispositivos O+) y envíes el sonido individual desde el dashboard (para dispositivos &#60;O).