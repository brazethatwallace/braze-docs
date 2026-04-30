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

### ¿Qué ocurre cuando varios usuarios inician sesión en un mismo dispositivo? {#what-happens-when-multiple-users-log-into-a-single-device}

Cuando un usuario cierra sesión en un dispositivo o sitio web, seguirá siendo alcanzable por push hasta que otro usuario inicie sesión. En ese momento, el token push se reasigna al nuevo usuario. Esto se debe a que cada dispositivo solo puede tener una suscripción push activa por aplicación o sitio web.

Cuando se reasigna un token push, el cambio se refleja en el **Push Changelog** del perfil de usuario. Puedes encontrarlo en la pestaña **Engagement** del perfil de usuario.

![El "Push Changelog" en la sección "Contact Settings".]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

### Cuando envío un push de prueba, ¿se envía a todos mis dispositivos? {#when-i-send-a-test-push-does-it-go-to-all-of-my-devices}

Sí. El push de prueba se envía a todos los dispositivos con push habilitado asociados al perfil de usuario seleccionado. Si tienes varios teléfonos o tabletas con la sesión iniciada con el mismo usuario, cada dispositivo con un token push válido recibe la notificación.

Para enviar el push de prueba a un solo dispositivo, puedes eliminar los tokens push de los demás dispositivos del perfil de usuario antes de la prueba. Alternativamente, si estás enviando con el [punto de conexión `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/), establece `send_to_most_recent_device_only` en `true` en el objeto `apple_push` o `android_push` para que solo el dispositivo activo más reciente reciba el push.

### ¿Qué significa "Error al enviar push porque la carga útil no era válida"? {#what-does-error-sending-push-because-the-payload-was-invalid-mean}

Este mensaje indica que APNs rechazó la solicitud push debido a una carga útil no válida (por ejemplo, una carga útil vacía o demasiado grande).

Para más detalles y próximos pasos, consulta [Mensajes de error push comunes]({{site.baseurl}}/user_guide/channels/push/push_error_codes/).

### ¿Por qué un usuario con suscripción activa no tiene un token push? {#why-doesnt-an-opted-in-user-have-a-push-token}

Esto puede ocurrir si el token push del usuario fue reasignado a otra persona que usó el mismo dispositivo.

1. Ve al **Push Changelog** en la pestaña **Engagement** del perfil del usuario afectado.
2. Busca un mensaje que indique que el token push fue trasladado a otro usuario.
3. Copia el token push y pégalo en la barra de búsqueda de usuarios.
4. Si el token push aún existe, serás dirigido al usuario que inició sesión más recientemente en el dispositivo.

Si deseas que el token push se reasigne al usuario original:

1. Haz que el usuario original inicie sesión en el perfil con el token push faltante.
2. Desencadena un nuevo envío push. Esto moverá el token de vuelta a la cuenta si el usuario aún tiene push habilitado a nivel de dispositivo.

### ¿Por qué "Abrir URL web dentro de la aplicación móvil" siempre abre la aplicación cuando estoy probando un borrador de campaña? {#why-does-open-web-url-inside-mobile-app-always-open-the-app-when-im-testing-a-draft-campaign}

Cuando una campaña aún está en estado **Draft** y envías un push de prueba, al tocar la notificación siempre se abre la aplicación primero, independientemente de si la opción **Open web URL inside mobile app** está seleccionada o no. Cuando la campaña está **Live**, el comportamiento al hacer clic funciona según la configuración.

Si seleccionaste **Open web URL** sin la opción **Inside App**, el enlace se abre directamente en el navegador predeterminado del dispositivo. Si seleccionaste **Open web URL inside mobile app**, el enlace se abre en una vista web dentro de la aplicación.

### ¿Cuál es la diferencia entre "Send to Production" y "Send to Development" para los certificados push de iOS? {#what-is-the-difference-between-send-to-production-and-send-to-development-for-ios-push-certificates}

Al añadir un certificado push de Apple en Braze, las opciones **Send to Production** y **Send to Development** determinan qué puerta de enlace de APNs (servicio de notificaciones push de Apple) utiliza Braze para entregar las notificaciones push:

- **Send to Development:** Selecciona esta opción si la aplicación fue compilada en modo de desarrollo en Xcode y firmada con un perfil de aprovisionamiento de desarrollo. Las notificaciones push se enrutan a través de la puerta de enlace de desarrollo (sandbox) de Apple.
- **Send to Production:** Selecciona esta opción si la aplicación se distribuye a través de TestFlight de Apple, App Store o distribución empresarial. Las notificaciones push se enrutan a través de la puerta de enlace de producción de Apple.

Si se selecciona la opción incorrecta, las notificaciones push fallan silenciosamente porque el tipo de token push no coincide con la puerta de enlace. Normalmente, las aplicaciones distribuidas a través de TestFlight o App Store deben usar **Send to Production**.

### ¿Cuál es la diferencia entre los filtros "Foreground Push Enabled" y "Background or Foreground Push Enabled"? {#what-is-the-difference-between-the-foreground-push-enabled-and-background-or-foreground-push-enabled-filters}

Estos filtros de segmentación verifican condiciones diferentes:

| Filtro | Qué verifica | Caso de uso |
|--------|-------------|-------------|
| **Foreground Push Enabled** | El usuario tiene un token push de primer plano válido **y** su estado de suscripción push es `Opted-In` o `Subscribed`. | Dirigirse a usuarios que pueden recibir notificaciones push visibles. |
| **Background or Foreground Push Enabled** | El usuario tiene cualquier token push (de primer plano o segundo plano) **y** su estado de suscripción push es `Opted-In` o `Subscribed`. Esto incluye a usuarios que han deshabilitado las notificaciones push visibles pero aún tienen un token push en segundo plano. | Se usa para [Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/), [notificaciones push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/) y geovallado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Un usuario puede tener `Background or Foreground Push Enabled` sin tener `Foreground Push Enabled`. Esto ocurre cuando el usuario ha deshabilitado las notificaciones push visibles en la configuración de su dispositivo, pero la aplicación aún conserva un token push en segundo plano. Para más detalles, consulta [Usuarios push y suscripciones]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#foreground-push-enabled).