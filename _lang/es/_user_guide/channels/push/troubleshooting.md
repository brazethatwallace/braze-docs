---
nav_title: Solución de problemas
article_title: Solución de problemas de push
page_order: 5
page_type: reference
description: "Esta página contiene pasos de solución de problemas para diversos problemas relacionados con el canal de mensajería push."
channel: push
---

# Solución de problemas de push {#troubleshoot-push}

> Usa esta página para solucionar problemas con el canal de mensajería push.

## Notificaciones push faltantes {#missing-push-notifications}

¿Tienes problemas con la entrega de notificaciones push? Hay una serie de pasos que puedes seguir para solucionar este problema comprobando lo siguiente:

- [Estado de suscripción push](#push-subscription-status)
- [Segment](#segment)
- [Límites de notificaciones push](#push-notification-caps)
- [Límites de velocidad](#rate-limits)
- [Estado del grupo de control](#control-group-status)
- [Token de push válido](#valid-push-token)
- [Tipo de notificación push](#push-notification-type)
- [Aplicación actual](#current-app)

#### Estado de suscripción push {#push-subscription-status}

Las notificaciones push solo pueden enviarse a usuarios suscritos u optados. Comprueba tu perfil de usuario en la pestaña [Interacción]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#engagement-tab) en la sección **User Profile** para confirmar si estás registrado activamente para push en el espacio de trabajo que estás probando. Si estás registrado en varias aplicaciones, las encontrarás en el campo **Push Registered For**:

![Push Registered For]({% image_buster /assets/img_archive/trouble1.png %})

También puedes exportar los perfiles de usuario utilizando los puntos de conexión de exportación de Braze:
- [Usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)
- [Usuarios por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)

Cualquiera de los dos puntos de conexión devolverá un objeto de token de push que incluye información de habilitación de push por dispositivo.

#### Segment {#segment}

Asegúrate de que perteneces al segmento al que te diriges (si se trata de una campaña en vivo y no de una prueba). En el **User Profile**, verás una lista de segmentos a los que pertenece actualmente el usuario. Recuerda que esta es una variable en constante cambio, ya que la segmentación se actualiza en tiempo real.

![List of Segments]({% image_buster /assets/img_archive/trouble2.png %})

También puedes confirmar que el usuario forma parte del segmento utilizando **User Lookup** al crear un segmento. **User Lookup** solo acepta `external_id` o `braze_id`, no direcciones de correo electrónico ni números de teléfono. Para buscar por correo electrónico, teléfono, token de push o alias de usuario, usa [**Buscar usuarios**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/).

![Sección de búsqueda de usuario con un campo de búsqueda.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Límites de notificaciones push {#push-notification-caps}

Comprueba los límites de frecuencia globales. Es posible que no hayas recibido la notificación push porque tu espacio de trabajo tiene una limitación de frecuencia global activa y ya has alcanzado tu límite de notificaciones push para el período de tiempo especificado.

Puedes hacerlo comprobando la [limitación de frecuencia global]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#freq-cap-feat-over) en el dashboard. Si la campaña está configurada para respetar las reglas de limitación de frecuencia, habrá un número de usuarios afectados por esta configuración.

![Campaign Details]({% image_buster /assets/img_archive/trouble3.png %})

#### Límites de velocidad {#rate-limits}

Si tienes un límite de velocidad configurado para tu campaña o Canvas, es posible que no estés recibiendo mensajes porque has superado este límite. Para más información, consulta [Límite de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#rate-limiting).

#### Estado del grupo de control {#control-group-status}

Si se trata de una campaña de un solo canal o un Canvas con un grupo de control, es posible que estés cayendo en el grupo de control.

  1. Comprueba la [distribución de variantes]({{site.baseurl}}/user_guide/messaging/ab_testing/#step-5-distribute-users-among-your-variants) para ver si hay un grupo de control.
  2. Si es así, crea un segmento filtrando por [en grupo de control de Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter) y luego [exporta el segmento]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/#exporting-to-csv) y comprueba si tu ID de usuario está en esta lista.

#### Token de push válido {#valid-push-token}
Un token de push es un identificador que los remitentes utilizan para dirigirse a dispositivos específicos con una notificación push. Por lo tanto, si el dispositivo no tiene un token de push válido, no hay forma de enviarle una notificación push.

#### Tipo de notificación push {#push-notification-type}

Comprueba que estás utilizando el tipo correcto de notificación push. Por ejemplo, si quieres dirigirte a un FireTV, usarías una notificación push de Kindle, no una campaña push de Android. Del mismo modo, si quieres dirigirte a un Android, usa una notificación push de Android y no una campaña push de iOS. Consulta los siguientes artículos para más información sobre cómo entender el flujo de trabajo de Braze para:
- [Apple Push Notification]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### Aplicación actual {#current-app}

Al probar envíos push con usuarios internos, asegúrate de que el usuario que deseas que reciba la notificación push esté actualmente conectado en la aplicación correspondiente. Esto puede provocar que el usuario no reciba una notificación push o que reciba una push para la que crees que no está segmentado.

{% alert note %}
Si estás enviando mensajes push con imágenes en Android, FCM a veces puede descartar la imagen y solo mostrar el texto en el mensaje push. Este problema generalmente es causado por problemas de conectividad del servidor.
{% endalert %}

## Error: MismatchSenderID {#error-mismatchsenderid}

MismatchSenderID indica un fallo de autenticación con Firebase Cloud Messaging (FCM). Confirma que tu Firebase sender ID y la clave de API de FCM sean correctos.

Para encontrar la clave de servidor de Firebase correcta y reemplazarla:

1. Ve a la consola de Firebase para tu aplicación.
2. En **Project Overview**, selecciona **Project Settings**.
3. En la pestaña **Cloud Messaging**, comprueba que el Sender ID debajo de las claves de API coincida con el de Braze (en **Settings** > **App Settings** > **Cloud Messaging API Key**).

{% alert warning %}
No cambies tu Sender ID en tu dashboard de Braze. Hacerlo provocará que los registros push existentes se invaliden. Si el Sender ID no coincide, debes encontrar tu proyecto de Firebase con el Sender ID correspondiente.
{% endalert %}

{:start="4"}
4. Copia la **Server Key** en **Project credentials**.
5. En Braze, ve a **Settings** > **App Settings**, selecciona tu aplicación y pega la clave del servidor en el campo **Cloud Messaging API Key** (reemplazando la clave obsoleta).
6. Selecciona **Save**.
7. Para verificar, envía una notificación push de prueba a un dispositivo antes y después de cambiar la clave de API sin abrir la aplicación. Esto ayuda a confirmar que los usuarios continúan recibiendo notificaciones push sin necesidad de generar un nuevo ID de registro push (token de push).

## Escenarios de solución de problemas {#troubleshooting-scenarios}

### Notificaciones push retrasadas {#delayed-push-notifications}

Tus notificaciones push pueden retrasarse por estas razones:

- Una conexión de datos débil en el dispositivo
- Código personalizado en la aplicación que puede suprimir las notificaciones push de Braze
- Preferencias del usuario para notificaciones push en la configuración del dispositivo
- Prioridad del mensaje de la notificación push cuando se crea en la campaña o Canvas
- Retrasos de tráfico o problemas con los proveedores de servicios push (FCM y APNs)

### Las notificaciones push se envían más lento de lo esperado {#push-notifications-are-sending-slower-than-expected}

Asegúrate de que la configuración de tus notificaciones push siga estas mejores prácticas:

- Si estás enviando a audiencias grandes sin considerar el estado de habilitación push, esto puede provocar una velocidad de envío más lenta. En su lugar, considera enviar solo a usuarios con push habilitado para reducir el tamaño de tu audiencia.
- Si es posible, intenta programar tus campañas con anticipación en lugar de inmediatamente.
- Si estás dirigiendo notificaciones push a un mayor número de usuarios en un Canvas, puedes anticipar que los pasos de mensaje posteriores en el Canvas requerirán tiempos de procesamiento diferentes a los de una campaña que envía a los usuarios inmediatamente. En este caso, las campañas normalmente terminarían de enviar antes que un Canvas, ya que el primer "paso" de un Canvas es verificar si los usuarios califican para el recorrido de usuario específico.

## Al hacer clic en una notificación push no se abre la aplicación {#clicking-a-push-notification-doesnt-open-the-app}

Si al hacer clic en una notificación push no se abre tu aplicación, comprueba lo siguiente según tu plataforma.

### Android

1. **Verifica el comportamiento al hacer clic:** Confirma que la campaña está configurada para abrir la aplicación al hacer clic.
2. **Comprueba el manejo de vínculos profundos:** En tu archivo `braze.xml`, comprueba si `com_braze_handle_push_deep_links_automatically` está configurado como `true` o `false`.
   - Si está configurado como `true`, el SDK de Braze maneja los vínculos profundos directamente y la aplicación debería abrirse como se espera.
   - Si está configurado como `false`, tu aplicación necesita un receptor de difusión para escuchar y manejar las intenciones de push recibidas y abiertas. Verifica que este receptor esté implementado correctamente.
3. **Recopila registros detallados:** [Habilita el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/), reproduce el problema y proporciona los registros junto con tu `braze.xml` y `AndroidManifest.xml` al soporte de Braze.

### iOS

1. **Verifica el comportamiento al hacer clic:** Confirma que la campaña está configurada para abrir la aplicación al hacer clic.
2. **Comprueba la integración push:** La vinculación en profundidad desde una notificación push hacia la aplicación se maneja automáticamente mediante la [integración push estándar]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) de Braze. Confirma que la integración está implementada correctamente, incluyendo cualquier manejo de delegado personalizado.
3. **Recopila registros detallados:** [Habilita el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/), reproduce el problema y proporciona los registros al soporte de Braze.

## Los clics en push abren inesperadamente dentro de la aplicación {#push-clicks-unexpectedly-open-in-app}

Si tienes problemas con enlaces en notificaciones push que se abren inesperadamente dentro de tu aplicación en lugar de en tu navegador web, puede haber un problema con la configuración de tu campaña o la implementación del SDK. Consulta estos pasos para obtener ayuda.

### Verifica el comportamiento al hacer clic {#verify-on-click-behavior}

En tu campaña o paso en Canvas, verifica que **Open web URL inside mobile app** no esté seleccionado. Si lo está, desmarca la selección y vuelve a lanzar.

![Campo "Comportamiento al hacer clic" de la configuración de una notificación push establecido en "Open web URL" con "Open web URL inside mobile app" desmarcado.]({% image_buster /assets/img/push_on_click.png %})

La interacción predeterminada para el comportamiento al hacer clic "Open web URL" difiere según la versión del SDK. Para las versiones del SDK iOS 2.29.0 y Android 2.0.0 y superiores, esta opción está seleccionada de forma predeterminada y las URL web se abrirán en una vista web dentro de la aplicación. Antes de estas versiones, esta opción está desmarcada de forma predeterminada y las URL web se abren en el navegador web predeterminado del dispositivo.

Si este no es el problema, puede haber un problema con tu implementación push.

### Verifica la integración push {#double-check-push-integration}

Si los enlaces en tus notificaciones push se abren inesperadamente en la aplicación, puede deberse a problemas con la integración de notificaciones push o la configuración de personalización. Sigue estos pasos para solucionar el problema:

1. **Revisa la implementación del delegado push:** Asegúrate de que el delegado push de Braze esté implementado correctamente. Para instrucciones detalladas, consulta la guía de integración de notificaciones push para tu [plataforma]({{site.baseurl}}/developer_guide/home/).
2. **Inspecciona el manejo personalizado de enlaces:** Comprueba si la aplicación incluye un manejo personalizado para todos los enlaces `https://`. Las configuraciones personalizadas pueden anular los comportamientos predeterminados. Colabora con tu equipo de desarrollo para revisar y ajustar esta configuración si es necesario.
3. **Verifica el registro push en iOS:** Para iOS, revisa el paso 1 de la guía de integración push sobre [registrar notificaciones push con APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). Asegúrate de que tu objeto delegado se asigne de forma sincrónica antes de que la aplicación termine de lanzarse. Este paso debe completarse en el método `application:didFinishLaunchingWithOptions:`.
4. **Prueba tu integración:** Después de realizar los ajustes, prueba el comportamiento de las notificaciones push en dispositivos iOS y Android para confirmar que el problema se ha resuelto.

### Vínculos profundos con la aplicación aún ejecutándose en segundo plano (iOS) {#deep-links-with-app-still-running-in-the-background-ios}

Si los vínculos profundos funcionan cuando la aplicación no está ejecutándose o cuando el enlace se usa directamente, pero no cuando la aplicación ya está ejecutándose en segundo plano, el problema puede estar relacionado con la forma en que la aplicación maneja el enlace. Comprueba si estás usando alguna biblioteca de terceros que utilice method swizzling. Recomendamos desactivar el swizzling, ya que puede causar problemas con las implementaciones de vínculos profundos.

## Migrar a una clave de autenticación .p8 {#migrate-to-a-p8-authentication-key}

Las claves de autenticación `.p8` de Apple son el enfoque requerido para push de APNs en Braze. A diferencia de los tipos de archivo de certificado heredados, las claves `.p8` no caducan y son compatibles con todas tus aplicaciones bajo una sola clave, eliminando la necesidad de renovaciones anuales de certificados y reduciendo el riesgo de fallos en la entrega push.

Si actualmente estás usando un certificado `.p12` o `.pem`, migra a una clave `.p8` lo antes posible. Para instrucciones sobre cómo crear y cargar una clave `.p8`, consulta [Cargar tu certificado push de APNs]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift). Para la guía de Apple sobre cómo generar una clave `.p8` desde tu cuenta de desarrollador, consulta [Comunicarse con APNs usando tokens de autenticación](https://developer.apple.com/help/account/capabilities/communicate-with-apns-using-authentication-tokens/).

### Claves .p8 frente a certificados .p12 {#p8-keys-versus-p12-certificates}

| Credencial | Caducidad | Indicador de estado en el dashboard |
| --- | --- | --- |
| Clave de autenticación `.p8` | No caduca | Sin indicador de estado verde (esto es esperado) |
| Certificado push `.p12` | Caduca anualmente | Indicador verde cuando el certificado es válido |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Claves .p8 frente a certificados .p12" }

Cuando reemplazas un certificado `.p12` con una clave `.p8` (o cargas una nueva credencial), la entrega push puede pausarse brevemente mientras Braze procesa el cambio. Planifica las actualizaciones durante una ventana de mantenimiento cuando sea posible.

En **Settings** > **App Settings** > **Push Notification Settings**, confirma que **App Bundle ID**, **Team ID** y **Key ID** (para claves `.p8`) coincidan con los valores en tu cuenta de Apple Developer. Varios espacios de trabajo de Braze pueden usar la misma credencial push de Apple cuando el **bundle ID** de la aplicación iOS es idéntico; el entorno de la credencial (desarrollo frente a producción) debe coincidir con la forma en que se compiló la aplicación.

Las aplicaciones con [Braze Swift SDK 10.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.0.0) o posterior pueden usar la [gestión dinámica de la puerta de enlace de APNs]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#dynamic-apns-gateway-management), que enruta los tokens al entorno de APNs correcto automáticamente.

## Las notificaciones push web no se comportan como se espera {#web-push-notifications-arent-behaving-as-expected}

Si tienes problemas con las notificaciones push en tu navegador, es posible que necesites restablecer los permisos de notificación de tu sitio y borrar el almacenamiento de tu sitio. Consulta estos pasos para obtener ayuda.

{% tabs %}
{% tab Chrome %}

### Restablecer Chrome en escritorio {#reset-chrome-on-desktop}

1. Junto a tu URL en el navegador Chrome, selecciona el icono deslizante **View Site Information**.
2. En **Notifications**, selecciona **Reset permission**.
3. Abre Chrome DevTools. Los siguientes son los atajos relevantes por sistema operativo.

<style>
table {
    max-width: 50%;
}
</style>

| SO      | Atajos de teclado                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Restablecer Chrome en escritorio" }

{:start="4"}
4. En DevTools, navega a la pestaña **Application**.
5. En la barra lateral, selecciona **Storage**.
6. Selecciona **Clear site data**.
7. Chrome te pedirá que recargues la página para aplicar la configuración actualizada. Selecciona **Reload**.

Tus permisos push se han restablecido. Abre una nueva pestaña en tu sitio y pruébalo.

### Restablecer Chrome en Android {#reset-chrome-on-android}

Si tienes una notificación de tu sitio visible en el cajón de notificaciones de Android:

1. Desde la notificación push, toca <i class="fas fa-cog" title="Configuración"></i> **Configuración** y selecciona **Site settings**.
2. Desde **Site settings**, toca **Clear & Reset**.

Si no tienes una notificación de tu sitio abierta:

1. Abre Chrome en Android.
2. Toca el menú <i class="fas fa-ellipsis-vertical"></i>.
3. Ve a **Settings** > **Site Settings** > **Notifications**.
4. Verifica que las notificaciones estén configuradas como **Ask before sending (recommended)**.
5. Encuentra tu sitio en la lista.
6. Selecciona la entrada y toca **Clear and Reset**.

Tus permisos push se han restablecido. Abre una nueva pestaña en tu sitio y pruébalo.

{% endtab %}
{% tab Firefox %}

### Restablecer Firefox en escritorio {#reset-firefox-on-desktop}

1. Junto a la URL de tu sitio, selecciona <i class="fa-solid fa-circle-info" alt="icono de información"></i> o <i class="fas fa-lock" alt="icono de candado"></i>.
2. En **Permissions**, junto a **Receive Notifications**, selecciona <i class="fa-solid fa-circle-xmark" title="Borrar este permiso y preguntar de nuevo"></i> **Borrar permiso** para borrar los permisos de notificación.
3. En el mismo menú, selecciona **Clear Cookies and Site Data**.
4. En el diálogo para confirmar tu elección, selecciona **OK**.

Tus permisos push se han restablecido. Abre una nueva pestaña en tu sitio y pruébalo.

### Restablecer Firefox en Android {#reset-firefox-on-android}

Para restablecer los permisos push en Android, consulta este [artículo de soporte de Mozilla](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

{% endtab %}
{% tab Safari %}

### Restablecer Safari en macOS {#reset-safari-on-macos}

{% alert note %}
Estos pasos son solo para macOS, ya que Apple no es compatible con Web Push para Safari en Windows.
{% endalert %}

1. Abre Safari.
2. Desde la [barra de menú en Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), ve a **Safari** > **Settings** > **Websites** > **Notifications**.
3. Selecciona tu sitio de la lista.
4. Selecciona **Remove** para borrar los permisos de notificación del sitio.
5. Luego, ve a **Privacy** > **Manage Website Data**.
6. Selecciona tu sitio de la lista.
7. Selecciona **Remove**, o para eliminar todos los datos del sitio, selecciona **Remove All**.
8. Selecciona **Done**.

Tus permisos push se han restablecido. Abre una nueva pestaña en tu sitio y pruébalo.

{% endtab %}
{% endtabs %}

## Mensajes de error de push {#push-error-messages}

Para información detallada sobre mensajes de error push comunes (como `DEVICE_UNREGISTERED`, `Unregistered`, `NotRegistered` y otros), consulta [Mensajes de error push comunes]({{site.baseurl}}/user_guide/channels/push/push_error_codes/).

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).