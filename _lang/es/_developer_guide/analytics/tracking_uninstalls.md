---
nav_title: Seguir las desinstalaciones
article_title: Seguir las desinstalaciones a través del SDK de Braze
page_order: 3.5
description: "Aprende a seguir las desinstalaciones a través del SDK de Braze."

---

# Seguir las desinstalaciones {#track-uninstalls}

> Aprende a configurar el seguimiento de Uninstall Tracking a través del SDK de Braze. Para obtener información general, consulta [Guía del usuario: Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

{% sdktabs %}
{% sdktab android %}
## Configuración de Uninstall Tracking {#setting-up-uninstall-tracking}

### Paso 1: Configurar el FCM {#step-1-set-up-fcm}

El SDK de Android Braze utiliza Firebase Cloud Messaging (FCM) para enviar notificaciones push silenciosas, que se utilizan para recopilar análisis de seguimiento de desinstalaciones. Si aún no lo has hecho, [configura]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#android_setting-up-push-notifications) o [migra a]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) la API de mensajería en la nube de Firebase para las notificaciones push.

### Paso 2: Detectar manualmente el seguimiento de Uninstall Tracking (opcional) {#step-2-manually-detect-uninstall-tracking-optional}

De forma predeterminada, el SDK de Android Braze detecta e ignora automáticamente las notificaciones push silenciosas relacionadas con el Uninstall Tracking. Sin embargo, puedes elegir detectar manualmente el seguimiento de la desinstalación mediante el método [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html).

{% alert important %}
Como las notificaciones silenciosas para el seguimiento de desinstalación no se reenvían a ninguna devolución de llamada push de Braze, solo puedes utilizar este método antes de pasar una notificación push a Braze.
{% endalert %}

### Paso 3: Eliminar los pings automáticos del servidor {#step-3-remove-automatic-server-pings}

Una notificación push silenciosa activa tu aplicación e instancia el componente `Application` si la aplicación no se está ejecutando. Por lo tanto, si tienes una subclase personalizada de [`Application`](https://developer.android.com/reference/android/app/Application), elimina cualquier lógica que haga pings automáticos a tus servidores durante el método de ciclo de vida [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()).

### Paso 4: Habilitar Uninstall Tracking {#step-4-enable-uninstall-tracking}

Por último, habilita Uninstall Tracking en Braze. Para un recorrido completo, consulta [Activar Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking#turning-on-uninstall-tracking).

{% alert important %}
El seguimiento de desinstalaciones puede ser impreciso. Las métricas que ves en Braze pueden estar retrasadas o ser inexactas.
{% endalert %}

{% endsdktab %}

{% sdktab swift %}
## Configuración de Uninstall Tracking

### Paso 1: Habilitar el push en segundo plano {#step-1-enable-background-push}

En tu proyecto de Xcode, ve a **Capacidades** y asegúrate de que tienes habilitados **los Modos de Fondo**. Para más información, consulta [Notificación push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Paso 2: Ignorar notificaciones push internas {#step-2-ignore-internal-push-notifications}

El SDK de Swift Braze utiliza notificaciones push en segundo plano para recopilar análisis de seguimiento de desinstalaciones. Asegúrate de que tu aplicación [ignore las notificaciones push internas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications) para que no realice acciones no deseadas cuando se envíen.

### Paso 3: Enviar un push de prueba (opcional) {#step-3-send-a-test-push-optional}

A continuación, envíate una notificación push de prueba desde el panel de Braze (no te preocupes&#8212;no actualizará tu perfil de usuario).

1. Ve a **Mensajería** > **Campañas** y crea una campaña de notificación push utilizando la plataforma correspondiente.
2. Ve a **Configuración** > **Configuración de la aplicación** y añade la clave `appboy_uninstall_tracking` con el valor `true` correspondiente, luego marca **Añadir indicador de contenido disponible**.
3. Utiliza la página **Vista previa** para enviarte un push de seguimiento de desinstalación de prueba.
4. Comprueba que tu aplicación no realiza ninguna acción automática no deseada cuando recibe una notificación push.

{% alert note %}
Se envía un número de señal junto con la notificación push de prueba&#8212;sin embargo, un push real de Uninstall Tracking no envía ningún número de señal.
{% endalert %}

### Paso 4: Habilitar Uninstall Tracking

Por último, habilita Uninstall Tracking en Braze. Para un recorrido completo, consulta [Activar Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking#turning-on-uninstall-tracking).

{% alert important %}
El seguimiento de desinstalaciones puede ser impreciso. Las métricas que ves en Braze pueden estar retrasadas o ser inexactas.
{% endalert %}

{% endsdktab %}
{% endsdktabs %}