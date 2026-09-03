---
nav_title: Seguimiento de sesiones
article_title: Seguimiento de sesiones
page_order: 3.3
description: "Aprende a realizar el seguimiento de las sesiones a través del SDK de Braze."
---

# Seguimiento de sesiones {#track-sessions}

> Aprende a realizar el seguimiento de las sesiones a través del SDK de Braze.

{% alert note %}
Para los SDK envolventes que no aparecen en la lista, utiliza el método nativo de Android o Swift correspondiente.
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Definición de la inactividad {#defining-inactivity}

Entender cómo se define y mide la inactividad es clave para gestionar eficazmente los ciclos de vida de las sesiones en el SDK Web. La inactividad se refiere a un periodo durante el cual el SDK Web de Braze no detecta ningún evento rastreado por parte del usuario.

### Cómo se mide la inactividad {#how-inactivity-is-measured}

El SDK Web rastrea la inactividad en función de los [eventos rastreados por el SDK]({{site.baseurl}}/user_guide/data/activation/events/events_overview). El SDK mantiene un temporizador interno que se reinicia cada vez que se envía un evento rastreado. Si no se producen eventos rastreados por el SDK dentro del periodo de tiempo de espera configurado, la sesión se considera inactiva y finaliza.

Para más información sobre cómo se implementa el ciclo de vida de la sesión en el SDK Web, consulta el código fuente de gestión de sesiones en el [repositorio de GitHub del SDK Web de Braze](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts).

**Qué cuenta como actividad de forma predeterminada:**
- Abrir o actualizar la aplicación web
- Interactuar con elementos de la interfaz impulsados por Braze (como [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages) o [Content Cards]({{site.baseurl}}/developer_guide/content_cards))
- Llamar a métodos del SDK que envían eventos rastreados (como [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events) o [actualizaciones de atributos de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes))

**Qué no cuenta como actividad de forma predeterminada:**
- Cambiar a una pestaña diferente del navegador
- Minimizar la ventana del navegador
- Eventos de enfoque o desenfoque del navegador
- Desplazamiento o movimientos del ratón en la página

{% alert note %}
El SDK Web no rastrea automáticamente los cambios de visibilidad del navegador, el cambio de pestañas ni el enfoque del usuario. Sin embargo, puedes rastrear estas interacciones a nivel de navegador implementando listeners de eventos personalizados mediante la [API de visibilidad de página](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) del navegador y enviando [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web) a Braze. Para ver un ejemplo de implementación, consulta [Seguimiento de inactividad personalizada](#tracking-custom-inactivity).
{% endalert %}

### Configuración del tiempo de espera de la sesión {#session-timeout-configuration}

De forma predeterminada, el SDK Web considera una sesión inactiva después de 30 minutos sin ningún evento rastreado. Puedes personalizar este umbral al inicializar el SDK utilizando el parámetro `sessionTimeoutInSeconds`. Para más información sobre cómo configurar este parámetro, incluidos ejemplos de código, consulta [Cambiar el tiempo de espera predeterminado de la sesión](#changing-the-default-session-timeout).

### Ejemplo: comprensión de los escenarios de inactividad {#example-understanding-inactivity-scenarios}

Considera el siguiente escenario:

1. Un usuario abre tu sitio web y el SDK inicia una sesión llamando a [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession).
2. El usuario cambia a una pestaña diferente del navegador para ver otro sitio web durante 30 minutos.
3. Durante este tiempo, no se producen eventos rastreados por el SDK en tu sitio web.
4. Después de 30 minutos de inactividad, la sesión finaliza automáticamente.
5. Cuando el usuario vuelve a la pestaña de tu sitio web y desencadena un evento del SDK (como ver una página o interactuar con el contenido), comienza una nueva sesión.

### Seguimiento de inactividad personalizada {#tracking-custom-inactivity}

Si necesitas rastrear la inactividad basándote en la visibilidad del navegador o en el cambio de pestañas, implementa listeners de eventos personalizados en tu código JavaScript. Utiliza eventos del navegador como `visibilitychange` para detectar cuándo los usuarios abandonan tu página, y envía manualmente [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events) a Braze o llama a [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession) cuando sea apropiado.

```javascript
// Example: Track when user switches away from tab
document.addEventListener('visibilitychange', function() {
  if (document.hidden) {
    // User switched away - optionally log a custom event
    braze.logCustomEvent('tab_hidden');
  } else {
    // User returned - optionally start a new session and/or log an event
    // braze.openSession();
    braze.logCustomEvent('tab_visible');
  }
});
```

Para más información sobre cómo registrar eventos personalizados, consulta [Registrar eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events). Para más detalles sobre el ciclo de vida de la sesión y la configuración del tiempo de espera, consulta [Cambiar el tiempo de espera predeterminado de la sesión](#change-session-timeout).

## Suscripción a actualizaciones de sesión {#subscribing-to-session-updates}

### Paso 1: Suscríbete a las actualizaciones {#step-1-subscribe-to-updates}

Para suscribirte a las actualizaciones de sesión, utiliza el método `subscribeToSessionUpdates()`.

{% tabs %}
{% tab web %}
Actualmente, la suscripción a actualizaciones de sesión no es compatible con el SDK de Braze para Web.
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message.getEventType() == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
      // A session has just been started
    }
  }
});
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
Si registras una devolución de llamada de fin de sesión, se activa cuando la aplicación vuelve al primer plano. La duración de la sesión se mide desde que la aplicación se abre o pasa al primer plano, hasta que se cierra o pasa a segundo plano.

{% subtabs %}
{% subtab swift %}
```swift
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.subscribeToSessionUpdates { event in
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```

Para suscribirte a un flujo asíncrono, puedes utilizar [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) en su lugar.

```swift
for await event in braze.sessionUpdatesStream {
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
BRZCancellable *cancellable = [AppDelegate.braze subscribeToSessionUpdates:^(BRZSessionEvent * _Nonnull event) {
  switch (event.state) {
    case BRZSessionStateStarted:
      NSLog(@"Session %@ has started", event.sessionId);
      break;
    case BRZSessionStateEnded:
      NSLog(@"Session %@ has ended", event.sessionId);
      break;
    default:
      break;
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
El SDK de React Native no expone un método para suscribirse directamente a las actualizaciones de sesión. El ciclo de vida de la sesión es gestionado por el SDK nativo subyacente, por lo que para suscribirte a las actualizaciones, utiliza el enfoque de la plataforma nativa en la pestaña **Android** o **Swift**.
{% endtab %}
{% endtabs %}

### Paso 2: Probar el seguimiento de sesiones (opcional) {#step-2-test-session-tracking-optional}

Para probar el seguimiento de sesiones, inicia una sesión en tu dispositivo y luego abre el panel de Braze y busca al usuario correspondiente. En su perfil de usuario, selecciona **Sessions Overview**. Si las métricas se actualizan como se espera, el seguimiento de sesiones funciona correctamente.

![La sección de resumen de sesiones de un perfil de usuario que muestra el número de sesiones, la fecha de último uso y la fecha de primer uso.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
Los detalles específicos de la aplicación solo se muestran para los usuarios que han utilizado más de una aplicación.
{% endalert %}

## Cambiar el tiempo de espera predeterminado de la sesión {#change-session-timeout}

Puedes cambiar el tiempo que transcurre antes de que una sesión caduque automáticamente.

{% tabs %}
{% tab web %}
De forma predeterminada, el tiempo de espera de la sesión está establecido en `30` minutos. Para cambiarlo, pasa la opción `sessionTimeoutInSeconds` a tu función [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize). Se puede establecer en cualquier número entero mayor o igual que `1`.

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

{% tab android %}
De forma predeterminada, el tiempo de espera de la sesión está establecido en `10` segundos. Para cambiarlo, abre tu archivo `braze.xml` y añade el parámetro `com_braze_session_timeout`. Se puede establecer en cualquier número entero mayor o igual que `1`.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
De forma predeterminada, el tiempo de espera de la sesión está establecido en `10` segundos. Para cambiarlo, configura `sessionTimeout` en el objeto `configuration` que se pasa a [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class). Se puede establecer en cualquier número entero mayor o igual que `1`.

{% subtabs %}
{% subtab swift %}
```swift
// Sets the session timeout to 60 seconds
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.sessionTimeout = 60;
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endsubtab %}
{% subtab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
El SDK de React Native depende de los SDK nativos para gestionar las sesiones. Para cambiar el tiempo de espera predeterminado de la sesión, configúralo en la capa nativa:

- **Android:** Configura `com_braze_session_timeout` en tu archivo `braze.xml`. Para obtener más información, selecciona la pestaña **Android**.
- **iOS:** Configura `sessionTimeout` en tu objeto `Braze.Configuration`. Para obtener más información, selecciona la pestaña **Swift**.
{% endtab %}
{% endtabs %}

{% alert note %}
Si estableces un tiempo de espera para la sesión, toda la semántica de la sesión se ampliará automáticamente hasta el tiempo de espera establecido.
{% endalert %}

## Solución de problemas {#troubleshooting}

### El perfil de usuario tiene 0 sesiones {#user-profile-has-0-sessions}

Un perfil de usuario puede tener 0 sesiones si el usuario fue creado fuera del SDK:

- **Creado por REST API:** Si un usuario se crea a través del endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) con un `app_id` en la solicitud, el perfil aparece asociado con esa aplicación pero no tiene datos de sesión porque el SDK nunca se inicializó para ese usuario.
- **Creado por importación CSV:** Si un usuario se importa a través de [CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) sin valores para los campos de primera o última sesión, el perfil existe con 0 sesiones.

### Algunos usuarios no están registrando sesiones {#some-users-are-not-logging-sessions}

Dado que las sesiones solo se rastrean después de que el SDK se inicializa, los usuarios que no activan la inicialización del SDK no registran ninguna sesión. Esto suele ocurrir cuando tu aplicación utiliza lógica condicional antes de inicializar el SDK, como retrasar la inicialización detrás de un flujo de inicio de sesión, una solicitud de consentimiento o un conmutador de características. Para obtener orientación sobre la implementación, consulta [Inicialización retardada]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift#step-2-set-up-delayed-initialization-optional). En estos casos, cualquier usuario que no cumpla la condición nunca inicia una sesión.

Si algunos usuarios están registrando sesiones y otros no, verifica lo siguiente:

- **Comprueba tu lógica de inicialización.** Confirma que el SDK se inicializa para todos los usuarios y puntos de entrada de la aplicación, no solo para algunos.
- **Busca cambios recientes en la aplicación.** Nueva lógica condicional alrededor de la inicialización del SDK puede causar una caída repentina en el recuento de sesiones.
- **Compara usuarios afectados y no afectados.** Identifica diferencias en la versión de la aplicación, tipo de dispositivo o flujo de usuario que puedan explicar por qué se omite la inicialización para ciertos usuarios.

Si el problema persiste después de verificar tu implementación, reproduce el problema y recopila la siguiente información antes de contactar con soporte:

- Pasos para reproducir el problema
- La versión de la aplicación afectada
- [Registros detallados del SDK]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), capturados mientras ocurre el problema (o por plataforma: [Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_enabling-logs), [Swift]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift#swift_setting-the-log-level), [Web]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web#web_logging))
- El fragmento de código para la inicialización del SDK
- Un resumen de cualquier lógica condicional aplicada antes de la inicialización