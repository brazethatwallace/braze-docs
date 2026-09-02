---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes
page_order: 30
description: "Este artículo aborda algunas de las preguntas más frecuentes que surgen al configurar campañas push."
page_type: FAQ
channel:
  - Push
---

# Preguntas frecuentes {#frequently-asked-questions}

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre el canal push.

## ¿Por qué las notificaciones push a veces se retrasan? {#why-are-push-notifications-sometimes-delayed}

La entrega generalmente sigue tres etapas: **procesamiento** de Braze (segmentación, planificación y transferencia al proveedor), transporte de Braze a **APNs o FCM**, y entrega del proveedor al **dispositivo**. Los retrasos pueden ocurrir en cualquier etapa. Braze no tiene visibilidad sobre las colas del proveedor o del dispositivo; usa el [registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs) en el cliente cuando necesites identificar los tiempos del lado del dispositivo.

## ¿Qué ocurre cuando varios usuarios inician sesión en un mismo dispositivo? {#what-happens-when-multiple-users-log-into-a-single-device}

Cuando un usuario cierra sesión en un dispositivo o sitio web, seguirá siendo alcanzable por push hasta que otro usuario inicie sesión. En ese momento, el token de notificaciones push se reasigna al nuevo usuario. Esto se debe a que cada dispositivo solo puede tener una suscripción push activa por aplicación o sitio web.

Cuando se reasigna un token de notificaciones push, el cambio se refleja en el **Push Registro de cambios** del perfil de usuario. En el perfil de usuario, ve a la pestaña **Engagement**.

![El "Push Changelog" en la sección "Contact Settings".]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

## Cuando envío un push de prueba, ¿se envía a todos mis dispositivos? {#when-i-send-a-test-push-does-it-go-to-all-of-my-devices}

Sí. El push de prueba se envía a todos los dispositivos con push habilitado asociados al perfil de usuario seleccionado. Si tienes varios teléfonos o tabletas con la sesión iniciada con el mismo usuario, cada dispositivo con un token de notificaciones push válido recibe la notificación.

Para enviar el push de prueba a un solo dispositivo, puedes eliminar los tokens de notificaciones push de los demás dispositivos del perfil de usuario antes de la prueba. Alternativamente, si estás enviando con el [punto de conexión `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages), establece `send_to_most_recent_device_only` en `true` en el objeto `apple_push` o `android_push` para que solo el dispositivo activo más reciente reciba el push.

## ¿Qué significa "Error al enviar push porque la carga útil no era válida"? {#what-does-error-sending-push-because-the-payload-was-invalid-mean}

Este mensaje indica que APNs rechazó la solicitud push debido a una carga útil no válida (por ejemplo, una carga útil vacía o demasiado grande).

Para más detalles y próximos pasos, consulta [Mensajes de error push comunes]({{site.baseurl}}/user_guide/channels/push/push_error_codes).

## ¿Por qué un usuario con suscripción activa no tiene un token de notificaciones push? {#why-doesnt-an-opted-in-user-have-a-push-token}

Esto puede ocurrir si el token de notificaciones push del usuario fue reasignado a otra persona que usó el mismo dispositivo.

1. Ve al **Push Registro de cambios** en la pestaña **Engagement** del perfil del usuario afectado.
2. Busca un mensaje que indique que el token de notificaciones push fue trasladado a otro usuario.
3. Copia el token de notificaciones push y pégalo en la barra de búsqueda de usuarios.
4. Si el token de notificaciones push aún existe, serás dirigido al usuario que inició sesión más recientemente en el dispositivo.

Si deseas que el token de notificaciones push se reasigne al usuario original:

1. Haz que el usuario original inicie sesión en el perfil con el token de notificaciones push faltante.
2. Desencadena un nuevo envío push. Esto moverá el token de vuelta a la cuenta si el usuario aún tiene push habilitado a nivel de dispositivo.

## ¿Por qué "Abrir URL web dentro de la aplicación móvil" siempre abre la aplicación cuando estoy probando un borrador de Campaign? {#why-does-open-web-url-inside-mobile-app-always-open-the-app-when-im-testing-a-draft-campaign}

Cuando una Campaign aún está en estado **Draft** y envías un push de prueba, al tocar la notificación siempre se abre la aplicación primero, independientemente de si la opción **Open web URL inside mobile app** está seleccionada o no. Cuando la Campaign está en estado **Live**, el comportamiento al hacer clic funciona según la configuración.

Si seleccionaste **Open web URL** sin la opción **Inside App**, el enlace se abre directamente en el navegador predeterminado del dispositivo. Si seleccionaste **Open web URL inside mobile app**, el enlace se abre en una vista web dentro de la aplicación.

## ¿Cuál es la diferencia entre "Send to Production" y "Send to Development" para los certificados push de iOS? {#what-is-the-difference-between-send-to-production-and-send-to-development-for-ios-push-certificates}

Al añadir un certificado push de Apple en Braze, las opciones **Send to Production** y **Send to Development** determinan qué puerta de enlace de APNs (servicio de notificaciones push de Apple) utiliza Braze para entregar las notificaciones push:

- **Send to Development:** Selecciona esta opción si la aplicación fue compilada en modo de desarrollo en Xcode y firmada con un perfil de aprovisionamiento de desarrollo. Las notificaciones push se enrutan a través de la puerta de enlace de desarrollo (sandbox) de Apple.
- **Send to Production:** Selecciona esta opción si la aplicación se distribuye a través de TestFlight de Apple, App Store o distribución empresarial. Las notificaciones push se enrutan a través de la puerta de enlace de producción de Apple.

Si se selecciona la opción incorrecta, las notificaciones push fallan silenciosamente porque el tipo de token de notificaciones push no coincide con la puerta de enlace. Normalmente, las aplicaciones distribuidas a través de TestFlight o App Store deben usar **Send to Production**.

## ¿Cuál es la diferencia entre los filtros "Foreground Push Enabled" y "Background or Foreground Push Enabled"? {#what-is-the-difference-between-the-foreground-push-enabled-and-background-or-foreground-push-enabled-filters}

Estos filtros de segmentación verifican condiciones diferentes:

| Filtro | Qué verifica | Caso de uso |
|--------|-------------|-------------|
| **Foreground Push Enabled** | El usuario tiene un token de notificaciones push de primer plano válido **y** su estado de suscripción push es `Opted-In` o `Subscribed`. | Dirigirse a usuarios que pueden recibir notificaciones push visibles. |
| **Background or Foreground Push Enabled** | El usuario tiene cualquier token de notificaciones push (de primer plano o segundo plano) **y** su estado de suscripción push es `Opted-In` o `Subscribed`. Esto incluye a usuarios que han deshabilitado las notificaciones push visibles pero aún tienen un token de notificaciones push en segundo plano. | Se usa para [Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking), [notificaciones push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent) y geovallado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Diferencia entre los filtros Foreground Push Enabled y Background or Foreground Push Enabled" }

Un usuario puede tener `Background or Foreground Push Enabled` sin tener `Foreground Push Enabled`. Esto ocurre cuando el usuario ha deshabilitado las notificaciones push visibles en la configuración de su dispositivo, pero la aplicación aún conserva un token de notificaciones push en segundo plano. Para más detalles, consulta [Usuarios push y suscripciones]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled).

## ¿Cómo determina Braze cuándo un mensaje push se envió correctamente? {#how-does-braze-determine-when-a-push-message-is-sent-successfully}

Un mensaje se registra como enviado en cuanto el proveedor de servicios de notificaciones push lo recibe. Esto no significa necesariamente que el usuario haya recibido o visto el mensaje.

Para iOS, el proveedor de servicios de notificaciones push es el servicio de notificaciones push de Apple (APNs), y para Android, normalmente es Firebase Cloud Messaging (FCM). El proveedor de servicios de notificaciones push responde de inmediato con éxito o fallo. Un fallo podría incluir un rebote o un reintento por fallo de red.

Si se devuelve un mensaje de éxito, el envío se registra en Braze y, a continuación, el servicio push intenta entregar al dispositivo. Si no se puede contactar con el dispositivo de inmediato, el servicio reintenta hasta que se alcanza la opción de caducidad configurada en Braze (**TTL** para Android, **Expiry** para iOS). Si el mensaje caduca, el servicio push lo descarta, pero no se considera un rebote.

- Para Campaigns push con entrega basada en acciones, el envío del mensaje se registra en cuanto el usuario realiza la acción que desencadena la Campaign.
- Para Campaigns planificadas, la hora de envío es el momento en que el mensaje se puso en cola y se pasó al proveedor de servicios de notificaciones push.
- Para ambos tipos de entrega, el mensaje se marca como "enviado" en Braze y en el perfil de usuario en **Campaigns Received**, aunque el usuario aún no haya visto ni recibido el push.

La métrica de "entregas" para push en el dashboard se calcula al cargar la página como el número de envíos menos los rebotes.