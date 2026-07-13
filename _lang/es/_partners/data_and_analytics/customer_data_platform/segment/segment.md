---
nav_title: Segment
article_title: Segment
page_order: 1
alias: /partners/segment/
description: "Este artículo de referencia describe la asociación entre Braze y Segment, una plataforma de datos de clientes que recopila y redirige información entre fuentes de tu stack de marketing."
page_type: partner
search_tag: Partner

---

# Segment

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment](https://segment.com) es una plataforma de datos de clientes que te ayuda a recopilar, limpiar y activar los datos de tus clientes.

La integración de Braze y Segment te permite realizar un seguimiento de tus usuarios y enviar datos a varios proveedores de análisis de usuarios. Segment te permite:

- Sincronizar [Segment Engage]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_engage) con Braze para utilizarlo en la segmentación de Campaign y Canvas de Braze.
- [Importar datos entre las dos plataformas](#integration-options). Ofrecemos una integración en paralelo de SDK para tus aplicaciones Android, iOS y web, y una integración de servidor a servidor para sincronizar tus datos con las REST API de Braze.
- [Conectar datos a Segment a través de Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents).

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Segment | Se necesita una [cuenta de Segment](https://app.segment.com/login) para beneficiarse de esta asociación. |
| Fuente instalada y [bibliotecas](https://segment.com/docs/sources/) de fuentes de Segment | El origen de cualquier dato enviado a Segment, como aplicaciones móviles, sitios web o servidores backend.<br><br>Debes instalar las bibliotecas en tu aplicación, sitio o servidor antes de poder configurar correctamente el flujo `Source > Destination`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para integrar Braze y Segment, debes configurar [Braze como destino](#connection-settings) de acuerdo con [el tipo de integración elegido](#integration-options) (modo de conexión). Si eres un cliente nuevo de Braze, puedes transmitir datos históricos a Braze mediante [repeticiones de Segment](#segment-replays). A continuación, debes configurar [los mapeados](#methods) y [probar tu integración](#step-4-test-your-integration) para garantizar un flujo de datos fluido entre Braze y Segment.

### Paso 1: Crear un destino Braze {#connection-settings}

Después de configurar correctamente tus fuentes, tendrás que configurar Braze como [destino](https://segment.com/docs/destinations/) para cada fuente (iOS, Android, web, etc.). Tendrás muchas opciones para personalizar el flujo de datos entre Braze y Segment mediante la configuración de la conexión.

### Paso 2: Elige el marco de destino y el tipo de conexión {#integration-options}

En Segment, ve a **Destinations** > **Braze** > **Configure Braze** > **Select your Source** > **Setup**.

![La página de configuración de la fuente. Esta página incluye configuraciones para establecer el marco de destino como "actions" o "classic" y establecer el modo de conexión como "cloud mode" o "device mode".]({% image_buster /assets/img/segment/setup.png %})

Puedes integrar la fuente web de Segment (Analytics.js) y las bibliotecas nativas del lado del cliente con Braze utilizando una integración en paralelo (modo dispositivo) o una integración de servidor a servidor (modo nube).

Tu elección del modo de conexión vendrá determinada por el tipo de fuente para el que esté configurado el destino.

| Integración | Detalles |
| ----------- | ------- |
| [En paralelo<br>(modo dispositivo)](#side-by-side-sdk-integration) | Utiliza el SDK de Segment para traducir eventos en llamadas nativas de Braze, lo que permite acceder a características más profundas y a un uso más completo de Braze que la integración de servidor a servidor.<br><br>Ten en cuenta que Segment no admite todos los métodos de Braze (por ejemplo, Content Cards). Para utilizar un método de Braze que no esté mapeado mediante un mapeado correspondiente, tendrás que invocar el método añadiendo código nativo de Braze a tu código base. |
| [De servidor a servidor<br>(modo nube)](#server-to-server-integration) | Reenvía los datos de Segment a los endpoints de la REST API de Braze.<br><br>No es compatible con las características de la interfaz de usuario de Braze, como la mensajería dentro de la aplicación, Content Cards o las notificaciones push. También existen datos capturados automáticamente, como los campos a nivel de dispositivo, que no están disponibles mediante este método.<br><br>Considera una integración en paralelo si deseas utilizar estas características. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Elige el marco de destino y el tipo de conexión" }

{% alert note %}
Visita [Segment](https://segment.com/docs/destinations/#connection-modes) para obtener más información sobre las dos opciones de integración (modos de conexión), incluidas las ventajas de cada una.
{% endalert %}

#### Integración en paralelo de SDK {#side-by-side-sdk-integration}

También llamada modo dispositivo, esta integración mapea el SDK y los [métodos](#methods) de Segment al SDK de Braze, permitiendo el acceso a todas las características que proporciona nuestro SDK, como push, mensajería dentro de la aplicación y otros métodos nativos de Braze.

{% alert note %}
Cuando utilices el modo dispositivo de Segment, no necesitas integrar directamente el SDK de Braze. Al añadir Braze como destino del modo dispositivo para Segment, el SDK de Segment inicializará el SDK de Braze y llamará a los métodos de Braze mapeados pertinentes.
{% endalert %}

{% alert important %}
Para las integraciones en modo dispositivo en móvil, debes añadir el complemento de destino de Braze a tu aplicación, además de configurar el destino en el panel de Segment. El SDK de Segment no incluye el complemento de Braze de forma predeterminada; sin él, el SDK de Segment no puede reenviar datos ni llamadas a métodos mapeados a Braze, y características como push, mensajes dentro de la aplicación y Content Cards no funcionarán. Consulta las pestañas específicas de cada plataforma en esta sección para obtener instrucciones de instalación.
{% endalert %}

Cuando se utiliza una conexión en modo dispositivo, de forma similar a la integración del SDK de Braze de forma nativa, el SDK de Braze asignará un `device_id` y un identificador de backend, `braze_id`, a cada usuario. Esto permite a Braze capturar la actividad anónima del dispositivo haciendo coincidir esos identificadores en lugar de `userId`.

{% alert note %}
Si utilizas [filtros de destino](https://segment.com/docs/connections/destinations/destination-filters/) con destinos en modo dispositivo (Kotlin o Swift), debes configurar el complemento de destino con el soporte de filtros habilitado. Consulta la [documentación de filtros de destino](https://segment.com/docs/connections/destinations/destination-filters/) de Segment para obtener detalles sobre las versiones de complementos compatibles.
{% endalert %}

{% tabs local %}
{% tab Android %}

{% alert important %}
Braze mantiene el código fuente de la integración del modo dispositivo Android y lo actualiza periódicamente para reflejar las nuevas versiones del SDK de Braze.

<br>
El SDK de Braze que utilices dependerá del SDK de Segment que utilices:

| | SDK de Segment | SDK de Braze |
| - | ----------- | --------- |
| Preferido | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| Legado | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze Segment Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integración en paralelo de SDK" }


{% endalert %}

Para configurar Braze como destino en modo dispositivo para tu fuente Android, elige **Actions** como **Destination framework** y, a continuación, selecciona **Save**.

Para completar la integración en paralelo, debes añadir el [complemento de destino Braze Kotlin](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/) a tu aplicación Android. Este complemento conecta el SDK de Segment y el SDK de Braze, permitiendo que los datos en modo dispositivo fluyan hacia Braze. Sigue las instrucciones de instalación de Segment para añadir la dependencia del complemento e inicializarlo con tu instancia de análisis de Segment.

Braze mantiene el código fuente de la integración [del modo dispositivo Android](https://github.com/braze-inc/braze-segment-kotlin) y lo actualiza regularmente para reflejar las nuevas versiones del SDK de Braze.

{% endtab %}
{% tab iOS %}

{% alert important %}
Braze mantiene el código fuente de la integración del modo dispositivo iOS y lo actualiza regularmente para reflejar las nuevas versiones del SDK de Braze.

<br>
El SDK de Braze que utilices dependerá del SDK de Segment que utilices:

| | SDK de Segment | SDK de Braze |
| - | ----------- | --------- |
| Preferido | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| Legado | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integración en paralelo de SDK" }
{% endalert %}

Para configurar Braze como destino en modo dispositivo para tu fuente iOS, elige **Actions** como **Destination framework** y, a continuación, selecciona **Save**.

Para completar la integración en paralelo, debes añadir el [complemento de destino Braze Swift](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/) a tu aplicación iOS. Este complemento conecta el SDK de Segment y el SDK de Braze, permitiendo que los datos en modo dispositivo fluyan hacia Braze. Sigue las instrucciones de instalación de Segment para añadir la dependencia del complemento (a través de Swift Package Manager o CocoaPods) e inicializarlo con tu instancia de análisis de Segment.

Braze mantiene el código fuente de la integración [del modo dispositivo iOS](https://github.com/braze-inc/braze-segment-swift) y lo actualiza regularmente para reflejar las nuevas versiones del SDK de Braze.

{% endtab %}
{% tab Web o JavaScript %}

Se recomienda el marco Braze Web Mode (Actions) de Segment para configurar Braze como destino del modo dispositivo para tu fuente web.

En Segment, selecciona **Actions** como marco de destino y **Device Mode** como modo de conexión.

![Configuración del destino de Segment mostrando el marco Actions y Device Mode seleccionados.]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
Segment mantiene el código fuente del [complemento Braze para React Native](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze) y lo actualiza periódicamente para reflejar las nuevas versiones del SDK de Braze.

Al conectar una fuente de React Native de Segment a Braze, debes configurar una fuente y un destino por sistema operativo. Por ejemplo, configurar un destino iOS y un destino Android.

Dentro de la base de código de tu aplicación, inicializa condicionalmente el SDK de Segment por tipo de dispositivo, utilizando la respectiva clave de escritura de origen asociada a cada aplicación.

Cuando se registra un token de notificaciones push desde un dispositivo y se envía a Braze, se asocia al identificador de la aplicación utilizado al inicializar el SDK. La inicialización condicional del tipo de dispositivo ayuda a confirmar que cualquier token de notificaciones push enviado a Braze está asociado a la aplicación correspondiente.

{% alert important %}
Si la aplicación React Native inicializa Braze con el mismo identificador de aplicación de Braze para todos los dispositivos, todos los usuarios de React Native se considerarán usuarios de Android o iOS en Braze, y todos los tokens de notificaciones push estarán asociados a ese sistema operativo.
{% endalert %}

Para configurar Braze como destino en modo dispositivo para cada fuente, elige **Actions** como **Destination framework** y, a continuación, selecciona **Save**.

{% endtab %}
{% endtabs %}

#### Integración de servidor a servidor {#server-to-server-integration}

También llamada modo nube, esta integración reenvía datos de Segment a las REST API de Braze. Utiliza el marco [Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) de Segment para configurar un destino en modo nube para cualquiera de tus fuentes.

A diferencia de la integración en paralelo, la integración de servidor a servidor no es compatible con las características de la interfaz de usuario de Braze, como la mensajería dentro de la aplicación, Content Cards o el registro automático de tokens de notificaciones push. También existen datos [capturados automáticamente]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection#user-data-collection) (como usuarios anónimos y campos a nivel de dispositivo) que no están disponibles a través del modo nube.

Si deseas utilizar estos datos y estas características, considera la posibilidad de utilizar la integración en paralelo (modo dispositivo) del SDK.

El código fuente del [destino Braze Cloud Mode (Actions)](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) lo mantiene Segment.

### Paso 3: Configuración {#step-3-settings}

Define la configuración de tu destino. No todas las configuraciones se aplicarán a todos los tipos de destino.

{% tabs local %}
{% tab Mobile Device-Mode %}

| Configuración | Descripción |
| ------- | ----------- |
| Identificador de la aplicación | El identificador de la aplicación utilizado para hacer referencia a la aplicación específica. Esto se puede encontrar en el panel de Braze en **Administrar configuración**. |
| Punto final personalizado de la API<br>(punto final SDK) | Tu punto final SDK de Braze que corresponde a tu instancia (como `sdk.iad-01.braze.com`). |
| Región del punto final | Tu instancia de Braze (como US 01, US 02, EU 01, etc.). |
| Habilitar el registro automático de mensajes dentro de la aplicación | Desactívalo si quieres registrar manualmente los mensajes dentro de la aplicación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Configuración" }

{% endtab %}
{% tab Web Device-Mode %}

| Configuración | Descripción |
| ------- | ----------- |
| Identificador de la aplicación | El identificador de la aplicación utilizado para hacer referencia a la aplicación específica. Esto se puede encontrar en el panel de Braze en **Administrar configuración**. |
| Punto final personalizado de la API<br>(punto final SDK) | Tu punto final SDK de Braze que corresponde a tu instancia (como `sdk.iad-01.braze.com`). |
| ID push del sitio web de Safari | Si eres compatible con la notificación push de Safari, debes especificar esta opción con el ID de sitio web push que proporcionaste a Apple al crear tu certificado push de Safari (empieza por `web`, por ejemplo, `web.com.example.domain`). |
| Versión del SDK Web de Braze | La versión del SDK Web de Braze que deseas utilizar. |
| Enviar automáticamente mensajes dentro de la aplicación | De forma predeterminada, todos los mensajes dentro de la aplicación para los que un usuario es elegible se entregan automáticamente al usuario. Desactívalo si quieres mostrar manualmente mensajes dentro de la aplicación. |
| No cargar Font Awesome | Braze utiliza Font Awesome para los iconos de mensajes dentro de la aplicación. De forma predeterminada, Braze cargará automáticamente FontAwesome desde el CDN de FontAwesome. Para desactivar este comportamiento (por ejemplo, porque tu sitio utiliza una versión personalizada de FontAwesome), establece esta opción en `TRUE`. Ten en cuenta que si haces esto, eres responsable de asegurarte de que FontAwesome está cargado en tu sitio; de lo contrario, es posible que los mensajes dentro de la aplicación no se muestren correctamente. |
| Habilitar mensajes HTML dentro de la aplicación | Habilitar esta opción permitirá a los usuarios del panel de Braze utilizar mensajes HTML dentro de la aplicación. |
| Abrir mensajes dentro de la aplicación en una pestaña nueva | De forma predeterminada, los enlaces de los clics de mensajes dentro de la aplicación se cargan en la pestaña actual o en una nueva pestaña, según se especifique en el panel, mensaje a mensaje. Configura esta opción en `TRUE` para forzar que todos los enlaces de los clics de mensajes dentro de la aplicación se abran en una nueva pestaña o ventana. |
| Índice z de mensajes dentro de la aplicación | Introduce un valor en esta opción para anular los índices z predeterminados de Braze. |
| Exigir la eliminación explícita de mensajes dentro de la aplicación | De forma predeterminada, cuando se muestra un mensaje dentro de la aplicación, al pulsar el botón de escape o hacer clic en el fondo gris de la página se descartará el mensaje. Establece esta opción como verdadera para evitar este comportamiento y requerir un clic explícito en el botón para descartar los mensajes. |
| Intervalo mínimo entre acciones desencadenantes en segundos | Predeterminado a 30.<br>De forma predeterminada, una acción desencadenante solo se activará si han transcurrido al menos 30 segundos desde la última acción desencadenante. Proporciona un valor a esta opción de configuración para anular ese valor predeterminado con un valor propio. No recomendamos que este valor sea inferior a 10 para evitar el envío excesivo de notificaciones al usuario. |
| Ubicación del prestador de servicios | De forma predeterminada, al registrar usuarios para notificaciones push web, Braze buscará el archivo del prestador de servicios necesario en el directorio raíz de tu servidor web en `/service-worker.js`. Si quieres alojar tu prestador de servicios en una ruta diferente en ese servidor, proporciona un valor para esta opción que sea la ruta absoluta al archivo (por ejemplo, `/mycustompath/my-worker.js`). Ten en cuenta que establecer un valor aquí limita el alcance de las notificaciones push en tu sitio. Por ejemplo, en el ejemplo anterior, como el archivo del prestador de servicios se encuentra en el directorio `/mycustompath/`, solamente se puede llamar a `requestPushPermission` desde páginas web que empiecen por `http://yoursite.com/mycustompath/`. |
| Desactivar el mantenimiento de token de notificaciones push | De forma predeterminada, los usuarios que ya hayan concedido permiso push web sincronizarán su token de notificaciones push con el backend de Braze automáticamente en las nuevas sesiones para garantizar la capacidad de entrega. Para desactivar este comportamiento, configura esta opción en `FALSE`. |
| Gestionar externamente al prestador de servicios | Si tienes tu propio prestador de servicios que registras y cuyo ciclo de vida controlas, establece esta opción en `TRUE`, y el SDK de Braze no registrará ni dará de baja a ningún prestador de servicios. Si configuras esta opción en `TRUE`, para que push funcione correctamente, debes registrar tú mismo el prestador de servicios antes de llamar a `requestPushPermission` y asegurarte de que contiene el código del prestador de servicios de Braze, bien con `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` o incluyendo directamente el contenido de ese archivo. Cuando esta opción es `TRUE`, la opción `serviceWorkerLocation` es irrelevante y se ignora. |
| Nonce de seguridad del contenido | Si proporcionas un valor para esta opción, el SDK de Braze añadirá el atributo nonce a todos los elementos `<script>` y `<style>` creados por el SDK. Esto permite que el SDK de Braze funcione con la política de seguridad de contenidos de tu sitio web. Además de configurar este nonce, es posible que también tengas que permitir que se cargue FontAwesome, lo que puedes hacer añadiendo `use.fontawesome.com` a la lista de permitidos de tu política de seguridad de contenidos o utilizando la opción `doNotLoadFontAwesome` y cargándolo manualmente. |
| Permitir actividad de rastreo | De forma predeterminada, el SDK Web de Braze ignora la actividad de arañas o rastreadores web conocidos, como Google, basándose en la cadena del agente de usuario. Esto ahorra puntos de datos, hace que los análisis sean más precisos y puede mejorar la clasificación de la página. Sin embargo, si quieres que Braze registre la actividad de estos rastreadores, puedes configurar esta opción en `TRUE`. |
| Habilitar registro | Establécelo en `TRUE` para habilitar el registro de forma predeterminada. Ten en cuenta que esto hará que Braze se registre en la consola JavaScript, que es visible para todos los usuarios. Antes de poner tu página en producción, debes eliminarlo o proporcionar un registrador alternativo con `setLogger`. |
| Permitir JavaScript proporcionado por el usuario | De forma predeterminada, el SDK Web de Braze no permite acciones de clic en JavaScript proporcionadas por el usuario, ya que permite a los usuarios del panel de Braze ejecutar JavaScript en tu sitio. Para indicar que confías en que los usuarios del panel de Braze escriban acciones de clic en JavaScript no maliciosas, establece esta propiedad en `TRUE`. Si `enableHtmlInAppMessages` es `TRUE`, esta opción también se establecerá en `TRUE`. |
| Versión de la aplicación | Si proporcionas un valor para esta opción, los eventos de usuario enviados a Braze se asociarán con la versión dada, que puede utilizarse para la segmentación de usuarios. |
| Tiempo de espera de la sesión en segundos | Predeterminado a 30.<br>De forma predeterminada, las sesiones caducan tras 30 minutos de inactividad. Proporciona un valor a esta opción de configuración para anular ese valor predeterminado con un valor propio. |
| Lista permitida de propiedades del dispositivo | De forma predeterminada, el SDK de Braze detecta y recopila automáticamente todas las propiedades del dispositivo en `DeviceProperties`. Para anular este comportamiento, proporciona una matriz de `DeviceProperties`. Ten en cuenta que, sin algunas propiedades, no todas las funciones funcionarán correctamente. Por ejemplo, la entrega según la zona horaria local no funcionará sin la zona horaria. |
| Localización | De forma predeterminada, cualquier mensaje visible para el usuario generado por el SDK se mostrará en el idioma del navegador del usuario. Proporciona un valor a esta opción para anular ese comportamiento y forzar un idioma específico. El valor de esta opción debe ser un código de idioma ISO 639-1. |
| Sin cookies | De forma predeterminada, el SDK de Braze almacenará pequeñas cantidades de datos (ID de usuario, ID de sesión) en cookies. Esto se hace para permitir a Braze reconocer usuarios y sesiones en diferentes subdominios de tu sitio. Si esto te supone un problema, pasa `TRUE` para esta opción para desactivar el almacenamiento de cookies y confiar totalmente en HTML 5 localStorage para identificar usuarios y sesiones. |
| Seguimiento de todas las páginas | **Solo destino clásico en modo dispositivo web (mantenimiento)**<br><br>Segment recomienda migrar al destino del marco de Web Actions, donde esta configuración puede [habilitarse mediante mapeados](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Esto enviará todas las [llamadas de página](https://segment.com/docs/spec/page/) a Braze como un evento "Loaded/Viewed a Page". |
| Seguir solo las páginas con nombre | **Solo destino clásico en modo dispositivo web (mantenimiento)**<br><br>Segment recomienda migrar al destino del marco de Web Actions, donde esta configuración puede [habilitarse mediante mapeados](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Esto solo enviará a Braze las llamadas a páginas que tengan un nombre asociado. |
| Registrar la compra cuando haya ingresos | **Solo destino clásico en modo dispositivo web (mantenimiento)**<br><br>Segment recomienda migrar al destino del marco de Web Actions, donde esta configuración puede [habilitarse mediante mapeados](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Cuando esta opción está habilitada, todas las llamadas de seguimiento con la propiedad de ingresos desencadenarán un evento de compra. |
| Seguir solo a usuarios conocidos | **Solo destino clásico en modo dispositivo web (mantenimiento)**<br><br>Segment recomienda migrar al destino del marco de Web Actions, donde esta configuración puede habilitarse mediante mapeados.<br><br>Si se habilita, esta nueva configuración retrasa la llamada de `window.braze.initialize` hasta que haya un `userId` válido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Configuración" }

{% endtab %}
{% tab Cloud-Mode %}

| Configuración | Descripción |
| ------- | ----------- |
| Identificador de la aplicación | El identificador de la aplicación utilizado para hacer referencia a la aplicación específica. Esto se puede encontrar en el panel de Braze en **Administrar configuración**. |
| Clave de API REST | Puedes encontrarla en tu panel de Braze, en **Configuración** > **Claves de API**. |
| Punto final personalizado de la REST API | Tu punto final REST de Braze que corresponde a tu instancia (como rest.iad-01.braze.com). |
| Actualizar solo usuarios existentes | **Solo destino clásico en modo nube (mantenimiento)**<br><br>Segment recomienda migrar al destino del marco de Cloud Actions, donde esta configuración puede [habilitarse mediante mapeados](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Determina si se actualizan solo los usuarios existentes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Configuración" }

{% endtab %}
{% endtabs %}

### Paso 4: Métodos de mapeado {#methods}

Braze admite los métodos de Segment [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify](https://segment.com/docs/spec/identify/) y [Track](https://segment.com/docs/spec/track/). Los tipos de identificadores utilizados en estos métodos dependerán de si los datos se envían a través de una integración de servidor a servidor (modo nube) o en paralelo (modo dispositivo). En los destinos Braze Web Mode Actions y Cloud Mode Actions, también puedes elegir configurar un mapeado para una [llamada de alias de Segment](https://segment.com/docs/connections/spec/alias/).

{% alert note %}
Aunque los alias de usuario se admiten como identificador en el destino Braze Cloud Mode (Actions), hay que tener en cuenta que la llamada de alias de Segment no está directamente relacionada con los alias de usuario de Braze.
{% endalert %}

| Tipo de identificador | Destino admitido |
| --------------- | --------------------- |
| `userId` (`external_id`) | Todos |
| Usuario anónimo | Destinos en modo dispositivo |
| Alias de usuario | Destinos en modo nube |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 4: Métodos de mapeado" }

El destino Cloud Mode (Actions) ofrece una [acción Crear alias](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias) que puede utilizarse para crear un usuario de solo alias o añadir un alias a un perfil existente de `external_id`. La acción [Identificar usuario](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user) puede utilizarse junto con la acción Crear alias para fusionar un usuario de solo alias con un `external_id` después de que haya uno disponible para el usuario.

También es posible ingeniárselas y utilizar `braze_id` para enviar datos de usuario anónimos en modo nube. Esto requiere incluir manualmente el `braze_id` del usuario en todas tus llamadas a la API de Segment. Puedes obtener más información sobre cómo configurar esta solución en [la documentación de Segment](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users).

Los datos de destino enviados a Braze se pueden procesar por lotes dentro de Cloud Mode Actions. El tamaño de los lotes está limitado a 75 eventos, y estos lotes se acumularán durante un periodo de 30 segundos antes de ser enviados. El procesamiento por lotes de solicitudes se realiza por acción. Por ejemplo, las llamadas Identify (atributos) se agruparán en una solicitud y las llamadas Track (eventos personalizados) se agruparán en una segunda solicitud. Braze recomienda habilitar esta característica, ya que reducirá el número de solicitudes que se envían desde Segment a Braze. A su vez, esto reducirá el riesgo de que el destino alcance los límites de velocidad de Braze y reintente las solicitudes.

Puedes activar el procesamiento por lotes de una acción navegando a tu destino Braze > **Mappings**. Desde ahí, haz clic en el icono de 3 puntos situado a la derecha del mapeado y selecciona **Edit Mapping**. Desplázate hasta la parte inferior de la sección **Select mappings** y asegúrate de que **Batch Data to Braze** está establecido en **Yes**.


{% tabs local %}
{% tab Identify %}
#### Identify

La llamada [Identify](https://segment.com/docs/spec/identify/) te permite vincular a un usuario a sus acciones y registrar atributos sobre él.

Algunos rasgos especiales de Segment están mapeados en campos de perfil de atributo estándar en Braze:

| Rasgos especiales de Segment | Atributos estándar de Braze |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identify" }

Otros campos reservados del perfil de Braze, como `email_subscribe` y `push_subscribe`, pueden enviarse utilizando la convención de nomenclatura de Braze para estos campos y pasándolos como rasgos dentro de una llamada Identify.

##### Añadir un usuario a un grupo de suscripción {#adding-a-user-to-a-subscription-group}

También puedes suscribir o cancelar la suscripción de un usuario de un determinado grupo de suscripción utilizando los siguientes campos del parámetro de rasgos.

Utiliza el campo reservado del perfil de Braze llamado `braze_subscription_groups`, que puede asociarse a una matriz de objetos. Cada objeto de la matriz debe tener dos claves reservadas:

1. `subscription_group_state`: indica si el usuario está `"subscribed"` o `"unsubscribed"` en un grupo de suscripción específico.
2. `subscription_group_id`: representa el ID único del grupo de suscripción. Puedes encontrar este ID en el panel de Braze, en **Administración del grupo de suscripción**.

{% subtabs %}
{% subtab Swift %}
```swift
analytics.identify(
  userId: "{your-user}",
  traits: [
    "braze_subscription_groups": [
      [
        "subscription_group_id": "{your-group-id}",
        "subscription_group_state": "subscribed"
      ],
      [
        "subscription_group_id", "{your-group-id}",
        "subscription_group_state": "unsubscribed"
      ]
    ]
  ]
)
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
analytics.identify(
  "{your-user}",
  buildJsonObject {
    put("braze_subscription_groups", buildJsonArray {
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "subscribed")
          }
        )
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "unsubscribed")
          }
        )
      }
    )
  }
)
```
{% endsubtab %}
{% subtab TypeScript %}
```typescript
analytics.identify(
  "{your-user}",
  {
    braze_subscription_groups: [
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "subscribed"
      },
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "unsubscribed"
      }
    ]
  }
)
```
{% endsubtab %}
{% endsubtabs %}

##### Atributos personalizados {#custom-attributes}

Todos los demás rasgos se registrarán como [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).

| Método de Segment | Método de Braze | Ejemplo |
|---|---|---|
| Identify con ID de usuario | Configurar ID externo | Segment:  `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| Identify con rasgos reservados | Establecer atributos del usuario | Segment: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| Identify con rasgos personalizados | Establecer atributos personalizados | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| Identify con ID de usuario y rasgos | Segment: establecer ID externo y atributo | Combina los métodos anteriores. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atributos personalizados" }

En los destinos [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) y [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile), los mapeados anteriores pueden establecerse mediante la acción Actualizar perfil de usuario.

{% alert important %}
Cuando pases datos de atributos de usuario, comprueba que solo pasas valores de atributos que hayan cambiado desde la última actualización. Así te asegurarás de no registrar innecesariamente puntos de datos. Para las fuentes del lado del cliente, utiliza la herramienta [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) de código abierto de Segment para optimizar tu integración y limitar el uso de puntos de datos eliminando las llamadas duplicadas a `identify()` desde Segment.

{% endalert %}
{% endtab %}

{% tab Track %}
#### Track

Cuando realices el seguimiento de un evento, registraremos ese evento como un [evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events) utilizando el nombre proporcionado.

Los metadatos enviados dentro del objeto de propiedades de la llamada Track se registrarán en Braze como propiedades del evento personalizado para el evento asociado. Se admiten todos los [tipos de datos de propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).

En los destinos [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) y [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event), los mapeados anteriores pueden establecerse mediante la acción Track Event.

| Método de Segment | Método de Braze | Ejemplo |
|---|---|---|
| [Track](https://segment.com/docs/spec/track/) | Registrado como [evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events). | Segment: `analytics.track("played_game");` <br>Braze: `Braze.logCustomEvent("played_game");`|
| [Track con propiedades](https://segment.com/docs/spec/track/) | Registrado como [propiedad del evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties). | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Track con producto](https://segment.com/docs/spec/track/) | Registrado como [evento de compra]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web). | Segment: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Track" }

##### Pedido completado {#order-completed}

Cuando realices el seguimiento de un evento con el nombre `Order Completed` utilizando el formato descrito en la [API de comercio electrónico](https://segment.com/docs/spec/ecommerce/v2/) de Segment, registraremos los productos que hayas indicado como [compras]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data).

En los destinos [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) y [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase), el mapeado predeterminado puede personalizarse a través de la acción Track Purchase.

{% endtab %}

{% tab Page %}
#### Page {#page}

La llamada [Page](https://segment.com/docs/spec/page/) te permite registrar cada vez que un usuario ve una página de tu sitio web, junto con cualquier propiedad opcional sobre la página.

Este tipo de evento puede utilizarse como desencadenante en los destinos Web Mode Actions y Cloud Actions para registrar un evento personalizado en Braze.
{% endtab %}

{% endtabs %}

### Paso 5: Prueba tu integración {#step-5-test-your-integration}

Al utilizar la integración en paralelo (modo dispositivo), tus métricas de [resumen]({{site.baseurl}}/user_guide/analytics/dashboards/home) (sesiones de toda la vida, MAU, DAU, adherencia, sesiones diarias y sesiones diarias por MAU) pueden utilizarse para garantizar que Braze está recibiendo datos de Segment.

Puedes ver tus datos en las páginas de [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data#custom-event-data) o de [ingresos]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data), o [creando un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment). La página **Eventos personalizados** del panel te permite ver los recuentos de eventos personalizados a lo largo del tiempo. Ten en cuenta que no podrás utilizar [fórmulas]({{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula#creating-a-formula) que incluyan estadísticas de MAU y DAU cuando utilices una integración de servidor a servidor (modo nube).

Si envías datos de compra a Braze (consulta pedido completado en la pestaña **Track** del [Paso 3](#methods)), la página de [ingresos]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data) te permite ver datos sobre ingresos o compras durante periodos específicos o los ingresos totales de tu aplicación.

[Crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment) te permite filtrar a tus usuarios en función de los datos de eventos y atributos personalizados.

{% alert important %}
Si utilizas una integración de servidor a servidor (modo nube), los filtros relacionados con los datos de sesión recopilados automáticamente (como "primera aplicación utilizada" y "última aplicación utilizada") no funcionarán. Utiliza una integración en paralelo (modo dispositivo) si quieres utilizarlos en tu integración de Segment y Braze.
{% endalert %}

## Eliminación y supresión de usuarios {#user-deletion-and-suppression}

Si necesitas eliminar o suprimir usuarios, ten en cuenta que [la característica de eliminación de usuarios de Segment](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **está** mapeada en el [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) de Braze. Ten en cuenta que la verificación de estas eliminaciones puede tardar hasta 30 días.

Debes asegurarte de que seleccionas un identificador de usuario común entre Braze y Segment (como `external_id`). Después de haber iniciado una solicitud de eliminación con Segment, puedes ver el estado en la pestaña de solicitudes de eliminación de tu panel de Segment.

## Repeticiones de Segment {#segment-replays}

Segment proporciona un servicio a los clientes para "reproducir" todos los datos históricos a un nuevo partner tecnológico. Los nuevos clientes de Braze que deseen importar todos los datos históricos relevantes pueden hacerlo a través de Segment. Habla con tu representante de Segment si esto te interesa.

Segment se conectará a nuestro [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para importar datos de usuario a Braze en tu nombre.

{% alert important %}
Todos los identificadores admitidos en el destino Cloud Mode Actions son compatibles como parte de las repeticiones de Segment.
{% endalert %}

## Buenas prácticas {#best-practices}

{% details Revisa los casos de uso para evitar excedentes de datos. %}

Segment **no** limita el número de elementos de datos que le envían los clientes. Segment te permite enviar todos o decidir qué eventos enviarás a Braze. En lugar de enviar todos tus eventos utilizando Segment, te sugerimos que revises los casos de uso con tus equipos de marketing y editorial para determinar qué eventos enviarás a Braze para evitar excedentes de datos.

{% enddetails %}

{% details Comprende la diferencia entre el punto final personalizado de la API y el punto final personalizado de la REST API en la configuración del destino en modo dispositivo móvil. %}

| Terminología de Braze | Equivalente de Segment |
| ----------------- | ------------------ |
| Punto final SDK de Braze | Punto final personalizado de la API |
| Punto final REST de Braze | Punto final personalizado de la REST API |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Buenas prácticas" }

Tu punto final API de Braze (llamado "punto final personalizado de la API" en Segment) es el punto final SDK que Braze configura para tu SDK (por ejemplo, `sdk.iad-03.braze.com`). Tu punto final de la REST API de Braze (llamado "punto final personalizado de la REST API" en Segment) es el punto final de la REST API (por ejemplo, `https://rest.iad-03.braze.com`).
{% enddetails %}

{% details Asegúrate de que tu punto final personalizado de la API esté correctamente introducido en la configuración del destino en modo dispositivo móvil. %}

| Terminología de Braze | Equivalente de Segment |
| ----------------- | ------------------ |
| Punto final SDK de Braze | Punto final personalizado de la API |
| Punto final REST de Braze | Punto final personalizado de la REST API |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Buenas prácticas" }

Debes seguir el formato adecuado para asegurarte de que introduces correctamente tu punto final SDK de Braze. Tu punto final SDK de Braze no debe incluir `https://` (por ejemplo, `sdk.iad-03.braze.com`), o la integración de Braze se romperá. Esto es necesario porque Segment antepone automáticamente `https://` a tu punto final, lo que provoca que Braze se inicialice con un punto final no válido `https://https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Matices del mapeado de datos. %}

Escenarios en los que los datos no pasarán como se espera:

1. Atributos personalizados anidados
  - Aunque [los atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support) pueden enviarse técnicamente a Braze a través de Segment, cada vez se enviará la **carga útil completa**. Esto incurrirá en [puntos de datos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#data-points) por clave pasada en el objeto anidado cada vez que se envíe la carga útil.<br><br> Para gastar solo un subconjunto de puntos de datos cuando se envía la carga útil, puedes utilizar la característica de [funciones de destino](https://segment.com/docs/connections/functions/destination-functions/) personalizadas, propiedad de Segment. Esta característica de la plataforma Segment te permite personalizar cómo se envían los datos a los destinos posteriores.

  {% alert note %}
  Las funciones de destino personalizadas se controlan dentro de Segment, y Braze tiene información limitada sobre las funciones que se han configurado externamente.
  {% endalert %}

{: start="2"}
2. Pasar datos anónimos de servidor a servidor.
  - Los clientes pueden utilizar las bibliotecas de servidor a servidor de Segment para canalizar datos anónimos a otros sistemas. Consulta la sección de métodos de mapeado para obtener más información sobre el envío de usuarios sin `external_id` a Braze mediante una integración de servidor a servidor (modo nube).

{% enddetails %}

{% details Personalización de la inicialización de Braze. %}

Hay varias formas diferentes de personalizar Braze: push, mensajes dentro de la aplicación, Content Cards e inicialización. Con una integración en paralelo, puedes seguir personalizando push, mensajes dentro de la aplicación y Content Cards como lo harías con una integración directa de Braze.

Sin embargo, personalizar cuándo se integra el SDK de Braze o especificar las configuraciones de inicialización puede ser difícil y, a veces, imposible. Esto se debe a que Segment inicializará el SDK de Braze por ti cuando se produzca la inicialización de Segment.

{% enddetails %}

{% details Envío de deltas a Braze. %}

Cuando pases datos de atributos de usuario, comprueba que solo pasas valores de atributos que hayan cambiado desde la última actualización. Esto evitará el registro de puntos de datos innecesarios. Para las fuentes del lado del cliente, utiliza la herramienta [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) de código abierto de Segment para optimizar tu integración y limitar el uso de puntos de datos eliminando las llamadas duplicadas a `identify()` desde Segment.

{% enddetails %}

{% details Utiliza el centro de datos de Braze correcto. %}

Segment utiliza tu centro de datos de Braze para obtener el punto final REST de Braze adecuado (como `https://rest.iad-01.braze.com`) para realizar llamadas de servidor a servidor.

{% enddetails %}

{% details Elimina el punto final personalizado de la REST API cuando utilices el Event Tester de Segment. %}

El Event Tester de Segment envía eventos al endpoint de la REST API `/users/track` de Braze y genera un error `401 Invalid API Key` si se ha establecido un punto final personalizado de la REST API en la configuración del destino de Braze, incluso cuando ese punto final es correcto. Elimina el valor del punto final personalizado de la REST API en Segment para que el Event Tester funcione correctamente.

{% enddetails %}

{% details Permite tiempo para las actualizaciones después de configurar una nueva fuente. %}

Segment mantiene la configuración en caché durante mucho tiempo, por lo que al configurar una nueva fuente (como cambiar de modo nube a modo dispositivo), es posible que tu aplicación no muestre el nuevo comportamiento o datos hasta que se renueve la caché. Ten en cuenta este retraso al planificar la adición de una fuente.

{% enddetails %}