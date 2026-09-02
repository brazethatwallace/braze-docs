---
nav_title: Solución de problemas
article_title: Solución de problemas de push
page_order: 5
page_type: reference
description: "Diagnostica problemas de entrega push, comportamiento de clics y credenciales utilizando un índice de síntomas y una ruta de investigación estándar."
channel: push
---

# Solución de problemas de push {#troubleshoot-push}

> Usa esta página para solucionar problemas de entrega push, comportamiento de clics y credenciales. Para la configuración específica del SDK or kit de desarrollo de software, consulta [Solución de problemas de notificaciones push del SDK or kit de desarrollo de software de Braze]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting). Para códigos de error, consulta [Mensajes de error push comunes]({{site.baseurl}}/user_guide/channels/push/push_error_codes).

## Empieza aquí: identifica tu síntoma {#start-here-match-your-symptom}

| Síntoma | Ir a |
| --- | --- |
| El usuario no recibió una notificación push | [Notificaciones push faltantes](#missing-push-notifications) |
| Las notificaciones push llegan tarde | [Notificaciones push retrasadas](#delayed-push-notifications) |
| Los envíos push son más lentos de lo esperado | [Las notificaciones push se envían más lento de lo esperado](#push-notifications-are-sending-slower-than-expected) |
| Error `MismatchSenderID` (Android) | [Error: MismatchSenderID](#error-mismatch-sender-id) |
| Tocar una notificación push no abre la aplicación | [Al hacer clic en una notificación push no se abre la aplicación](#clicking-a-push-notification-does-not-open-the-app) |
| Los enlaces push se abren en la aplicación en lugar del navegador | [Los clics en push se abren inesperadamente en la aplicación](#push-clicks-unexpectedly-open-in-app) |
| Problemas de permisos o entrega de notificaciones push web | [Las notificaciones push web no se comportan como se esperaba](#web-push-notifications-are-not-behaving-as-expected) |
| Necesitas migrar de `.p12` a `.p8` (iOS) | [Migrar a una clave de autenticación .p8](#migrate-to-a-p8-authentication-key) |
| Código de error push específico en los registros | [Mensajes de error push](#push-error-messages) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma de push" }

## Ruta de investigación estándar {#standard-investigation-path}

Usa este flujo de trabajo cuando un usuario o dispositivo de prueba no haya recibido una notificación push. Empieza en el paso 1.

1. Confirma que el usuario tiene la suscripción push activa o ha dado su consentimiento y que tiene un token de notificaciones push válido en la pestaña **Engagement** de su perfil.
2. Confirma que el usuario está en el público objetivo de la Campaign o Canvas en el momento del envío (los Segments se actualizan en tiempo real).
3. Comprueba la limitación de frecuencia global, los límites de velocidad y la asignación al grupo de control de la Campaign o Canvas.
4. Confirma que estás usando el tipo de push correcto para el dispositivo (por ejemplo, Android, iOS o Kindle).
5. Para pruebas internas, confirma que la persona que está probando ha iniciado sesión en la aplicación correcta del dispositivo.
6. Si la entrega sigue fallando, revisa los [mensajes de error push comunes]({{site.baseurl}}/user_guide/channels/push/push_error_codes) o ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) con el ID de la Campaign o Canvas, el ID de usuario y la marca de tiempo con zona horaria.

## Notificaciones push faltantes {#missing-push-notifications}

**Síntoma:** Un usuario no recibió una notificación push esperada.

Si las notificaciones push no llegan como se espera, revisa las siguientes comprobaciones:

- [Estado de suscripción push](#push-subscription-status)
- [Segment](#segment)
- [Límites de notificaciones push](#push-notification-caps)
- [Límites de velocidad](#rate-limits)
- [Estado del grupo de control](#control-group-status)
- [Token de push válido](#valid-push-token)
- [Tipo de notificación push](#push-notification-type)
- [Aplicación actual](#current-app)

### Estado de suscripción push {#push-subscription-status}

Las notificaciones push solo pueden enviarse a usuarios suscritos u optados. En el **Perfil de usuario**, abre la pestaña [Interacción]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) y confirma que estás registrado activamente para push en el espacio de trabajo que estás probando. Si estás registrado en varias aplicaciones, aparecerán en **Push Registered For**:

![Push Registered For]({% image_buster /assets/img_archive/trouble1.png %})

También puedes exportar los perfiles de usuario con los endpoints de exportación de Braze:

- [Usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Usuarios por Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Cualquiera de los dos endpoints devuelve un objeto de token de push que incluye información de habilitación de push por dispositivo.

### Segment {#segment}

Confirma que perteneces al Segment al que te diriges (si se trata de una campaña en vivo y no de una prueba). En el **Perfil de usuario**, puedes ver a qué Segments pertenece actualmente el usuario. La pertenencia a Segments se actualiza en tiempo real.

![Lista de Segments]({% image_buster /assets/img_archive/trouble2.png %})

También puedes confirmar que el usuario forma parte del Segment utilizando **User Lookup** al crear un Segment. **User Lookup** solo acepta `external_id` o `braze_id`, no direcciones de correo electrónico ni números de teléfono. Para buscar por correo electrónico, teléfono, token de push o alias de usuario, consulta [**Buscar usuarios**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

![Sección de búsqueda de usuario con un campo de búsqueda.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

### Límites de notificaciones push {#push-notification-caps}

Comprueba los límites de frecuencia globales. Es posible que no hayas recibido la notificación push porque tu espacio de trabajo tiene limitación de frecuencia global activa y ya alcanzaste tu límite de notificaciones push para el período de tiempo especificado.

En la página de **Analytics** de la Campaign, busca un banner de limitación de frecuencia que muestre aproximadamente cuántos usuarios no recibieron la Campaign en los últimos 30 días. Para investigar envíos individuales, usa el [dashboard de diagnóstico de mensajería]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) y filtra por **Frequency capped**. Para revisar o cambiar las reglas, consulta [limitación de frecuencia global]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#freq-cap-feat-over).

![Detalles de Campaign]({% image_buster /assets/img_archive/trouble3.png %})

### Límites de velocidad {#rate-limits}

Si tienes un límite de velocidad configurado para tu Campaign o Canvas, es posible que dejes de recibir mensajes después de superar ese límite. Para más información, consulta [Límite de velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting).

### Estado del grupo de control {#control-group-status}

Si se trata de una Campaign de un solo canal o un Canvas con un grupo de control, es posible que estés en el grupo de control.

  1. Comprueba la [distribución de variantes]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-4-choose-a-segment-and-distribute-your-users-across-variants) para ver si hay un grupo de control.
  2. Si es así, crea un Segment que filtre por [en grupo de control de Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#in-campaign-control-group) y luego [exporta el Segment]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#segment-csv-export-details) y comprueba si tu ID de usuario está en la lista.

### Token de push válido {#valid-push-token}

Un token de push es un identificador que los remitentes utilizan para dirigirse a un dispositivo específico con una notificación push. Sin un token de push válido, Braze no puede enviar una notificación push a ese dispositivo.

Braze almacena hasta 20 dispositivos por perfil de usuario. Cuando un dispositivo número 21 se registra, el dispositivo más antiguo se elimina (primero en entrar, primero en salir, o FIFO). Llamar a [`changeUser()`]({{site.baseurl}}/developer_guide/analytics/setting_user_ids) en el SDK or kit de desarrollo de software vuelve a registrar el dispositivo actual en el perfil.

### Tipo de notificación push {#push-notification-type}

Usa el tipo de push que coincida con el dispositivo o la plataforma a la que te diriges. Por ejemplo, usa una notificación push de Kindle para Fire TV, no una campaña push de Android. Para dispositivos Android, usa una notificación push de Android en lugar de una campaña push de iOS.

Para flujos de trabajo de solución de problemas específicos por plataforma, consulta:

- [Solución de problemas de notificaciones push de Apple]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Solución de problemas de Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

### Aplicación actual {#current-app}

Al probar push con usuarios internos, confirma que el destinatario previsto haya iniciado sesión en la aplicación correcta. De lo contrario, podría no recibir la notificación push, o podría recibir una que no esperabas según la segmentación.

{% alert note %}
Si estás enviando mensajes push con imágenes en Android, FCM a veces puede descartar la imagen y solo mostrar el texto en el mensaje push. Este problema generalmente es causado por problemas de conectividad del servidor.
{% endalert %}

## Error: MismatchSenderID {#error-mismatch-sender-id}

**Síntoma:** La notificación push de Android falla con un error `MismatchSenderID`.

MismatchSenderID indica un fallo de autenticación con Firebase Cloud Messaging (FCM). Confirma que tu ID de remitente de Firebase y tu clave de API de FCM son correctos.

Para encontrar la clave de servidor de Firebase correcta y reemplazarla:

1. Ve a la consola de Firebase de tu aplicación.
2. En **Project Overview**, selecciona **Project Settings**.
3. En la pestaña **Cloud Messaging**, comprueba que el ID de remitente que aparece con las claves de API coincide con el de Braze (en **Configuración** > **Configuración de la aplicación** > **Cloud Messaging API Key**).

{% alert warning %}
No cambies tu ID de remitente en el panel de Braze. Hacerlo invalida los registros de push existentes. Si el ID de remitente no coincide, debes encontrar tu proyecto de Firebase con el ID de remitente correspondiente.
{% endalert %}

4. Copia la **Server Key** en **Project credentials**.
5. En Braze, ve a **Configuración** > **Configuración de la aplicación**, selecciona tu aplicación y pega la clave de servidor en el campo **Cloud Messaging API Key** (reemplazando la clave obsoleta).
6. Selecciona **Guardar**.
7. Para verificar, envía una notificación push de prueba a un dispositivo antes y después de cambiar la clave de API sin abrir la aplicación. Esto ayuda a confirmar que los usuarios siguen recibiendo notificaciones push sin necesidad de generar un nuevo ID de registro push (token de notificaciones push).

## Escenarios de solución de problemas {#troubleshooting-scenarios}

### Notificaciones push retrasadas {#delayed-push-notifications}

**Síntoma:** Las notificaciones push llegan más tarde de lo esperado.

Tus notificaciones push pueden retrasarse por las siguientes razones:

- Una conexión de datos débil en el dispositivo
- Código personalizado en la aplicación que puede suprimir las notificaciones push de Braze
- Preferencias del usuario para las notificaciones push en la configuración del dispositivo
- Prioridad del mensaje de la notificación push cuando se crea en la Campaign o Canvas
- Retrasos en el tráfico o problemas con los proveedores de servicios de notificaciones push (FCM y APNs)

### Las notificaciones push se envían más lento de lo esperado {#push-notifications-are-sending-slower-than-expected}

**Síntoma:** Los envíos push de Campaigns o Canvas tardan más de lo esperado en completarse.

Confirma que la configuración de tus notificaciones push sigue estas buenas prácticas:

- Si envías a audiencias grandes sin considerar el estado de habilitación de push, esto puede provocar una velocidad de envío más lenta. En su lugar, considera enviar solo a usuarios con push habilitado para reducir el tamaño de tu audiencia.
- Si es posible, intenta programar tus Campaigns con antelación en lugar de inmediatamente.
- Si estás enviando notificaciones push a un mayor número de usuarios en un Canvas, puedes anticipar que los pasos de mensaje posteriores en el Canvas requerirán tiempos de procesamiento diferentes a los de una Campaign que envía a los usuarios de inmediato. En este caso, las Campaigns normalmente terminarían de enviar antes que un Canvas, ya que el primer "paso" de un Canvas es verificar si los usuarios califican para el recorrido de usuario específico.

## Al hacer clic en una notificación push no se abre la aplicación {#clicking-a-push-notification-does-not-open-the-app}

**Síntoma:** Al tocar una notificación push no se abre la aplicación ni se navega según lo configurado.

Si al hacer clic en una notificación push no se abre tu aplicación, comprueba lo siguiente según tu plataforma.

### Android

1. **Verifica el comportamiento al hacer clic:** Confirma que la Campaign está configurada para abrir la aplicación al hacer clic.
2. **Comprueba la gestión de vínculos profundos:** En tu archivo `braze.xml`, comprueba si `com_braze_handle_push_deep_links_automatically` está configurado como `true` o `false`.
   - Si está configurado como `true`, el SDK or kit de desarrollo de software de Braze gestiona los vínculos profundos directamente y la aplicación debería abrirse como se espera.
   - Si está configurado como `false`, tu aplicación necesita un receptor de difusión para escuchar y gestionar los intents de push recibidos y abiertos. Verifica que este receptor esté implementado correctamente.
3. **Recopila registros detallados:** [Habilita el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduce el problema y proporciona los registros junto con tu `braze.xml` y `AndroidManifest.xml` a soporte de Braze.

### iOS

1. **Verifica el comportamiento al hacer clic:** Confirma que la Campaign está configurada para abrir la aplicación al hacer clic.
2. **Comprueba la integración push:** La vinculación en profundidad desde una notificación push hacia la aplicación se gestiona automáticamente mediante la [integración push estándar]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift) de Braze. Confirma que la integración esté implementada correctamente, incluyendo cualquier gestión de delegados personalizada.
3. **Recopila registros detallados:** [Habilita el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduce el problema y proporciona los registros a soporte de Braze.

## Los clics en push abren inesperadamente dentro de la aplicación {#push-clicks-unexpectedly-open-in-app}

**Síntoma:** Los enlaces en las notificaciones push se abren dentro de la aplicación en lugar del navegador web del dispositivo.

Si tienes problemas con enlaces en notificaciones push que se abren inesperadamente dentro de tu aplicación en lugar de en tu navegador web, puede haber un problema con la configuración de tu Campaign o la implementación del SDK or kit de desarrollo de software. Consulta estos pasos para obtener ayuda.

### Verifica el comportamiento al hacer clic {#verify-on-click-behavior}

En tu Campaign o paso en Canvas, verifica que **Open web URL inside mobile app** no esté seleccionado. Si lo está, desmarca la selección y vuelve a lanzar.

La interacción predeterminada para el comportamiento al hacer clic "Open web URL" difiere según la versión del SDK or kit de desarrollo de software. Para las versiones del SDK or kit de desarrollo de software iOS 2.29.0 y Android 2.0.0 y superiores, esta opción está seleccionada de forma predeterminada y las URL web se abren en una vista web dentro de la aplicación. Antes de estas versiones, esta opción está desmarcada de forma predeterminada y las URL web se abren en el navegador web predeterminado del dispositivo.

Si este no es el problema, puede haber un problema con tu implementación push.

### Verifica la integración push {#double-check-push-integration}

Si los enlaces en tus notificaciones push se abren inesperadamente en la aplicación, puede deberse a problemas con la integración de notificaciones push o la configuración de personalización. Sigue estos pasos para solucionar el problema:

1. **Revisa la implementación del delegado push:** Asegúrate de que el delegado push de Braze esté implementado correctamente. Para instrucciones detalladas, consulta la guía de integración de notificaciones push para tu [plataforma]({{site.baseurl}}/developer_guide/home).
2. **Inspecciona el manejo personalizado de enlaces:** Comprueba si la aplicación incluye un manejo personalizado para todos los enlaces `https://`. Las configuraciones personalizadas pueden anular los comportamientos predeterminados. Colabora con tu equipo de desarrollo para revisar y ajustar esta configuración si es necesario.
3. **Verifica el registro push en iOS:** Para iOS, revisa el paso 1 de la guía de integración push sobre [registrar notificaciones push con APN]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift). Asegúrate de que tu objeto delegado se asigne de forma sincrónica antes de que la aplicación termine de lanzarse. Este paso debe completarse en el método `application:didFinishLaunchingWithOptions:`.
4. **Prueba tu integración:** Después de realizar los ajustes, prueba el comportamiento de las notificaciones push en dispositivos iOS y Android para confirmar que el problema se ha resuelto.

### Vínculos profundos con la aplicación aún ejecutándose en segundo plano (iOS) {#deep-links-with-app-still-running-in-the-background-ios}

Si los vínculos profundos funcionan cuando la aplicación no está ejecutándose o cuando el enlace se usa directamente, pero no cuando la aplicación ya está ejecutándose en segundo plano, el problema puede estar relacionado con la forma en que la aplicación maneja el enlace. Comprueba si estás usando alguna biblioteca de terceros que utilice method swizzling. Recomendamos desactivar el swizzling, ya que puede causar problemas con las implementaciones de vínculos profundos.

## Migrar a una clave de autenticación .p8 {#migrate-to-a-p8-authentication-key}

**Síntoma:** Necesitas migrar las credenciales push de iOS de un certificado heredado a una clave `.p8`, o la entrega push falló después de un cambio de credencial.

Las claves de autenticación `.p8` de Apple son el enfoque requerido para push de APNs en Braze. A diferencia de los tipos de archivo de certificado heredados, las claves `.p8` no caducan y son compatibles con todas tus aplicaciones bajo una sola clave, eliminando la necesidad de renovaciones anuales de certificados y reduciendo el riesgo de fallos en la entrega push.

Si actualmente estás usando un certificado `.p12` o `.pem`, migra a una clave `.p8` lo antes posible. Para instrucciones sobre cómo crear y cargar una clave `.p8`, consulta [Cargar tu certificado push de APNs]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift). Para la guía de Apple sobre cómo generar una clave `.p8` desde tu cuenta de desarrollador, consulta [Comunicarse con APNs usando tokens de autenticación](https://developer.apple.com/help/account/capabilities/communicate-with-apns-using-authentication-tokens/).

### Claves .p8 frente a certificados .p12 {#p8-keys-versus-p12-certificates}

Usa la siguiente tabla para comparar tipos de credenciales, caducidad y cómo aparece cada uno en el panel.

| Credencial | Caducidad | Indicador de estado en el panel |
| --- | --- | --- |
| Clave de autenticación `.p8` | No caduca | Sin indicador de estado verde (esto es esperado) |
| Certificado push `.p12` | Caduca anualmente | Indicador verde cuando el certificado es válido |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Claves .p8 frente a certificados .p12" }

Cuando reemplazas un certificado `.p12` con una clave `.p8` (o cargas una nueva credencial), la entrega push puede pausarse brevemente mientras Braze procesa el cambio. Planifica las actualizaciones durante una ventana de mantenimiento cuando sea posible.

En **Settings** > **App Settings** > **Push Notification Settings**, confirma que **App Bundle ID**, **Team ID** y **Key ID** (para claves `.p8`) coincidan con los valores en tu cuenta de Apple Developer. Varios espacios de trabajo de Braze pueden usar la misma credencial push de Apple cuando el **bundle ID** de la aplicación iOS es idéntico; el entorno de la credencial (desarrollo frente a producción) debe coincidir con la forma en que se compiló la aplicación.

Las aplicaciones con [Braze Swift SDK or kit de desarrollo de software 10.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.0.0) o posterior pueden usar la [gestión dinámica de la puerta de enlace de APNs]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift#dynamic-apns-gateway-management), que enruta los tokens al entorno de APNs correcto automáticamente.

## Las notificaciones push web no se comportan como se espera {#web-push-notifications-are-not-behaving-as-expected}

**Síntoma:** Las notificaciones push del navegador no se muestran o los permisos del sitio parecen estar bloqueados.

Si tienes problemas con las notificaciones push en tu navegador, es posible que necesites restablecer los permisos de notificación de tu sitio y borrar el almacenamiento del sitio. Sigue los pasos a continuación para obtener ayuda.

{% tabs %}
{% tab Chrome %}

### Restablecer Chrome en escritorio {#reset-chrome-on-desktop}

1. Junto a tu URL en el navegador Chrome, selecciona el icono del control deslizante **View Site Information**.
2. En **Notifications**, selecciona **Reset permission**.
3. Abre Chrome DevTools. A continuación se muestran los atajos de teclado relevantes por sistema operativo.

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

Tus permisos de push se han restablecido. Abre una nueva pestaña con tu sitio y pruébalo.

### Restablecer Chrome en Android {#reset-chrome-on-android}

Si tienes una notificación de tu sitio visible en el cajón de notificaciones de Android:

1. Desde la notificación push, selecciona <i class="fas fa-cog" title="Configuración"></i> **Settings** y selecciona **Site settings**.
2. Desde **Site settings**, toca **Clear & Reset**.

Si no tienes una notificación de tu sitio abierta:

1. Abre Chrome en Android.
2. Toca el menú <i class="fas fa-ellipsis-vertical"></i>.
3. Ve a **Settings** > **Site Settings** > **Notifications**.
4. Verifica que las notificaciones estén configuradas como **Ask before sending (recommended)**.
5. Busca tu sitio en la lista.
6. Selecciona la entrada y toca **Clear and Reset**.

Tus permisos de push se han restablecido. Abre una nueva pestaña con tu sitio y pruébalo.

{% endtab %}
{% tab Firefox %}

### Restablecer Firefox en escritorio {#reset-firefox-on-desktop}

1. Junto a la URL de tu sitio, selecciona <i class="fa-solid fa-circle-info" alt="icono de información"></i> o <i class="fas fa-lock" alt="icono de candado"></i>.
2. En **Permissions**, junto a **Receive Notifications**, selecciona <i class="fa-solid fa-circle-xmark" title="Borrar este permiso y preguntar de nuevo"></i> **Clear permission** para borrar los permisos de notificación.
3. En el mismo menú, selecciona **Clear Cookies and Site Data**.
4. En el cuadro de diálogo para confirmar tu elección, selecciona **OK**.

Tus permisos de push se han restablecido. Abre una nueva pestaña con tu sitio y pruébalo.

### Restablecer Firefox en Android {#reset-firefox-on-android}

Para restablecer los permisos de push en Android, consulta [Clear your browsing history and other personal data](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser) en Mozilla Support.

{% endtab %}
{% tab Safari %}

### Restablecer Safari en macOS {#reset-safari-on-macos}

{% alert note %}
Estos pasos son solo para macOS, ya que Apple no es compatible con notificaciones push web para Safari en Windows.
{% endalert %}

1. Abre Safari.
2. Desde la [barra de menú en Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), ve a **Safari** > **Settings** > **Websites** > **Notifications**.
3. Selecciona tu sitio de la lista.
4. Selecciona **Remove** para eliminar los permisos de notificación del sitio.
5. Luego, ve a **Privacy** > **Manage Website Data**.
6. Selecciona tu sitio de la lista.
7. Selecciona **Remove**, o para eliminar todos los datos del sitio, selecciona **Remove All**.
8. Selecciona **Done**.

Tus permisos de push se han restablecido. Abre una nueva pestaña con tu sitio y pruébalo.

{% endtab %}
{% endtabs %}

## Métricas de apertura push {#push-open-metrics}

Braze registra una apertura directa cuando un usuario toca la notificación y tu aplicación inicia una sesión. Expandir una notificación push enriquecida sin abrir la aplicación no registra una apertura directa.

Si un usuario abre tu aplicación después de recibir una notificación push sin tocar la notificación, Braze puede registrar una Influenced Open en su lugar. Para definiciones e informes, consulta [Influenced Opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

## Mensajes de error de push {#push-error-messages}

**Síntoma:** Ves un código de error de push específico (por ejemplo, `DEVICE_UNREGISTERED`, `Unregistered` o `NotRegistered`).

Para definiciones de códigos de error push comunes (incluyendo `DEVICE_UNREGISTERED`, `NotRegistered` y `Unregistered`), consulta [Mensajes de error push comunes]({{site.baseurl}}/user_guide/channels/push/push_error_codes).

Cuando FCM devuelve errores como `DEVICE_UNREGISTERED` o `NotRegistered`, Braze normalmente elimina el token de notificaciones push afectado del perfil de usuario. Esa eliminación generalmente indica que la aplicación fue desinstalada o que el token ya no es válido. Las campañas de Uninstall Tracking utilizan la misma lógica de eliminación de tokens a escala.