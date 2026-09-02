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
- [Importar datos entre las dos plataformas](#integration-options). Ofrecemos una integración en paralelo de SDK or kit de desarrollo de software para tus aplicaciones Android, iOS y web, y una integración de servidor a servidor para sincronizar tus datos con las REST or transferencia de estado representacional API de Braze.
- [Conectar datos a Segment a través de Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents).

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Segment | Se necesita una [cuenta de Segment](https://app.segment.com/login) para beneficiarse de esta asociación. |
| Fuente instalada y [bibliotecas](https://segment.com/docs/sources/) de fuente de Segment | El origen de cualquier dato enviado a Segment, como aplicaciones móviles, sitios web o servidores backend.<br><br>Debes instalar las bibliotecas en tu aplicación, sitio o servidor antes de poder configurar un flujo `Source > Destination` con éxito. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para integrar Braze y Segment, debes configurar [Braze como destino](#connection-settings) de acuerdo con [el tipo de integración que hayas elegido](#integration-options) (modo de conexión). Si eres un cliente nuevo de Braze, puedes retransmitir datos históricos a Braze utilizando [las repeticiones de Segment](#segment-replays). A continuación, debes configurar los [mapeados](#methods) y [probar tu integración](#step-4-test-your-integration) para garantizar un flujo de datos fluido entre Braze y Segment.

### Paso 1: Crear un destino Braze {#connection-settings}

Tras configurar correctamente tus fuentes, tendrás que configurar Braze como [destino](https://segment.com/docs/destinations/) para cada fuente (iOS, Android, web, etc.). Tendrás muchas opciones para personalizar el flujo de datos entre Braze y Segment mediante la configuración de conexión.

### Paso 2: Elegir el framework de destino y el tipo de conexión {#integration-options}

En Segment, ve a **Destinations** > **Braze** > **Configure Braze** > **Select your Source** > **Setup**.

![La página de configuración de la fuente. Esta página incluye ajustes para establecer el framework de destino como "actions" o "classic" y configurar el modo de conexión como "cloud mode" o "device mode".]({% image_buster /assets/img/segment/setup.png %})

Puedes integrar la fuente web de Segment (Analytics.js) y las bibliotecas nativas del lado del cliente con Braze utilizando una integración en paralelo (device-mode) o una integración servidor a servidor (cloud-mode).

Tu elección del modo de conexión estará determinada por el tipo de fuente para la que esté configurado el destino.

| Integración | Detalles |
| ----------- | ------- |
| [En paralelo<br>(device-mode)](#side-by-side-sdk-integration) | Utiliza el SDK or kit de desarrollo de software de Segment para traducir eventos en llamadas nativas de Braze, lo que permite acceder a características más profundas y un uso más completo de Braze que la integración servidor a servidor.<br><br>Ten en cuenta que Segment no es compatible con todos los métodos de Braze (por ejemplo, Content Cards). Para utilizar un método de Braze que no esté mapeado a través de un mapeado correspondiente, tendrás que invocar el método añadiendo código nativo de Braze a tu código base. |
| [Servidor a servidor<br>(cloud-mode)](#server-to-server-integration) | Reenvía datos desde Segment a los endpoints de la REST or transferencia de estado representacional API de Braze.<br><br>No es compatible con las características de la interfaz de Braze, como mensajes dentro de la aplicación, Content Cards o notificaciones push. También existen datos capturados automáticamente, como campos a nivel de dispositivo, que no están disponibles a través de este método.<br><br>Considera una integración en paralelo si deseas utilizar estas características. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Elegir el framework de destino y el tipo de conexión" }

{% alert note %}
Visita [Segment](https://segment.com/docs/destinations/#connection-modes) para obtener más información sobre las dos opciones de integración (modos de conexión), incluidas las ventajas de cada una.
{% endalert %}

#### Integración en paralelo del SDK or kit de desarrollo de software {#side-by-side-sdk-integration}

También llamada device-mode, esta integración mapea el SDK or kit de desarrollo de software de Segment y los [métodos](#methods) al SDK or kit de desarrollo de software de Braze, lo que permite acceder a todas las características que proporciona nuestro SDK or kit de desarrollo de software, como push, mensajes dentro de la aplicación y otros métodos nativos de Braze.

{% alert note %}
Cuando utilices el device-mode de Segment, deja que Segment inicialice Braze. No inicialices también el SDK or kit de desarrollo de software de Braze en tu aplicación. El plugin de destino configura Braze y abre sesiones; una segunda inicialización nativa puede registrar sesiones duplicadas. Utiliza `identify` de Segment para establecer el ID de usuario. El plugin mapea esa llamada a `changeUser()`.
{% endalert %}

{% alert important %}
Para integraciones en device-mode en móvil, debes añadir el plugin de destino de Braze a tu aplicación además de configurar el destino en el panel de Segment. El SDK or kit de desarrollo de software de Segment no incluye el plugin de Braze por defecto; sin él, el SDK or kit de desarrollo de software de Segment no puede reenviar datos ni llamadas de métodos mapeados a Braze, y características como push, mensajes dentro de la aplicación y Content Cards no funcionarán. Consulta las pestañas específicas de plataforma en esta sección para obtener instrucciones de instalación.
{% endalert %}

Al utilizar una conexión en device-mode, de forma similar a la integración nativa del SDK or kit de desarrollo de software de Braze, el SDK or kit de desarrollo de software de Braze asignará un `device_id` y un identificador de backend, `braze_id`, a cada usuario. Esto permite a Braze capturar la actividad anónima del dispositivo al hacer coincidir esos identificadores en lugar de `userId`.

{% alert note %}
Si utilizas [filtros de destino](https://segment.com/docs/connections/destinations/destination-filters/) con destinos en device-mode (Kotlin o Swift), debes configurar el plugin de destino con el soporte de filtros habilitado. Consulta la [documentación de filtros de destino](https://segment.com/docs/connections/destinations/destination-filters/) de Segment para obtener detalles sobre las versiones de plugin compatibles.
{% endalert %}

{% tabs local %}
{% tab Android %}

{% alert important %}
El código fuente de la integración en device-mode para Android es mantenido por Braze y se actualiza regularmente para reflejar las nuevas versiones del SDK or kit de desarrollo de software de Braze.

<br>
El SDK or kit de desarrollo de software de Braze que utilices dependerá del SDK or kit de desarrollo de software de Segment que uses:

| | SDK or kit de desarrollo de software de Segment | SDK or kit de desarrollo de software de Braze |
| - | ----------- | --------- |
| Preferido | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| Heredado | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze Segment Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integración en paralelo del SDK or kit de desarrollo de software" }


{% endalert %}

Para configurar Braze como destino en device-mode para tu fuente de Android, elige **Actions** como **Destination framework** y después selecciona **Save**.

Para completar la integración en paralelo, debes añadir el [plugin de destino Braze Kotlin](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/) a tu aplicación Android. Este plugin conecta el SDK or kit de desarrollo de software de Segment con el SDK or kit de desarrollo de software de Braze, permitiendo que los datos en device-mode fluyan hacia Braze. Sigue las instrucciones de instalación de Segment para añadir la dependencia del plugin e inicializarlo con tu instancia de análisis de Segment.

El código fuente de la integración en [device-mode para Android](https://github.com/braze-inc/braze-segment-kotlin) es mantenido por Braze y se actualiza regularmente para reflejar las nuevas versiones del SDK or kit de desarrollo de software de Braze.

{% endtab %}
{% tab iOS %}

{% alert important %}
El código fuente de la integración en device-mode para iOS es mantenido por Braze y se actualiza regularmente para reflejar las nuevas versiones del SDK or kit de desarrollo de software de Braze.

<br>
El SDK or kit de desarrollo de software de Braze que utilices dependerá del SDK or kit de desarrollo de software de Segment que uses:

| | SDK or kit de desarrollo de software de Segment | SDK or kit de desarrollo de software de Braze |
| - | ----------- | --------- |
| Preferido | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| Heredado | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integración en paralelo del SDK or kit de desarrollo de software" }
{% endalert %}

Para configurar Braze como destino en device-mode para tu fuente de iOS, elige **Actions** como **Destination framework** y después selecciona **Save**.

Para completar la integración en paralelo, debes añadir el [plugin de destino Braze Swift](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/) a tu aplicación iOS. Este plugin conecta el SDK or kit de desarrollo de software de Segment con el SDK or kit de desarrollo de software de Braze, permitiendo que los datos en device-mode fluyan hacia Braze. Sigue las instrucciones de instalación de Segment para añadir la dependencia del plugin (a través de Swift Package Administrador o CocoaPods) e inicializarlo con tu instancia de análisis de Segment.

El código fuente de la integración en [device-mode para iOS](https://github.com/braze-inc/braze-segment-swift) es mantenido por Braze y se actualiza regularmente para reflejar las nuevas versiones del SDK or kit de desarrollo de software de Braze.

{% endtab %}
{% tab Web o JavaScript %}

El framework Braze Web Mode (Actions) de Segment es recomendado para configurar Braze como destino en device-mode para tu fuente web.

En Segment, selecciona **Actions** como tu framework de destino y **Device Mode** como tu modo de conexión.

![Configuración de destino de Segment mostrando el framework Actions y Device Mode seleccionados.]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
El código fuente del [plugin React Native de Braze](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze) es mantenido por Segment y se actualiza regularmente para reflejar las nuevas versiones del SDK or kit de desarrollo de software de Braze.

Al conectar una fuente React Native de Segment con Braze, debes configurar una fuente y un destino por sistema operativo. Por ejemplo, configurar un destino iOS y un destino Android.

Dentro del código de tu aplicación, inicializa condicionalmente el SDK or kit de desarrollo de software de Segment por tipo de dispositivo, utilizando la clave de escritura de la fuente respectiva asociada con cada aplicación.

Cuando se registra un token de push desde un dispositivo y se envía a Braze, se asocia con el identificador de la aplicación utilizado al inicializar el SDK or kit de desarrollo de software. La inicialización condicional por tipo de dispositivo ayuda a confirmar que cualquier token de push enviado a Braze esté asociado con la aplicación correspondiente.

{% alert important %}
Si la aplicación React Native inicializa Braze con el mismo identificador de aplicación de Braze para todos los dispositivos, entonces todos los usuarios de React Native serán considerados usuarios de Android o iOS en Braze, y todos los tokens de push se asociarán con ese sistema operativo.
{% endalert %}

Para configurar Braze como destino en device-mode para cada fuente, elige **Actions** como **Destination framework** y después selecciona **Save**.

{% endtab %}
{% endtabs %}

#### Integración servidor a servidor {#server-to-server-integration}

También llamada cloud-mode, esta integración reenvía datos desde Segment a las REST or transferencia de estado representacional APIs de Braze. Utiliza el framework [Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) de Segment para configurar un destino en cloud-mode para cualquiera de tus fuentes.

A diferencia de la integración en paralelo, la integración servidor a servidor no es compatible con las características de la interfaz de Braze, como mensajes dentro de la aplicación, Content Cards o el registro automático de tokens de push. También existen datos [capturados automáticamente]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection#user-data-collection) (como usuarios anónimos y campos a nivel de dispositivo) que no están disponibles a través de cloud-mode.

Si deseas utilizar estos datos y estas características, considera usar la integración en paralelo (device-mode) del SDK or kit de desarrollo de software.

El código fuente del [destino Braze Cloud Mode (Actions)](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) es mantenido por Segment.

### Paso 3: Configuración {#step-3-settings}

Define la configuración de tu destino. No todas las configuraciones se aplicarán a todos los tipos de destino.

{% tabs local %}
{% tab Device-Mode móvil %}

| Configuración | Descripción |
| ------- | ----------- |
| Identificador de aplicación | El identificador de aplicación utilizado para hacer referencia a la aplicación específica. Se puede encontrar en el panel de Braze en **Manage Settings** |
| Endpoint de API personalizado<br>(endpoint del SDK or kit de desarrollo de software) | Tu endpoint del SDK or kit de desarrollo de software de Braze que corresponde a tu instancia (como `sdk.iad-01.braze.com`) |
| Región del endpoint | Tu instancia de Braze (como US 01, US 02, EU 01, etc.) |
| Habilitar registro automático de mensajes dentro de la aplicación | Deshabilita esta opción si deseas registrar manualmente los mensajes dentro de la aplicación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Configuración" }

{% endtab %}
{% tab Device-Mode web %}

| Configuración | Descripción |
| ------- | ----------- |
| Identificador de aplicación | El identificador de aplicación utilizado para hacer referencia a la aplicación específica. Se puede encontrar en el panel de Braze en **Manage Settings** |
| Endpoint de API personalizado<br>(endpoint del SDK or kit de desarrollo de software) | Tu endpoint del SDK or kit de desarrollo de software de Braze que corresponde a tu instancia (como `sdk.iad-01.braze.com`) |
| ID de push del sitio web en Safari | Si admites push en Safari, debes especificar esta opción con el ID de push del sitio web que proporcionaste a Apple al crear tu certificado de push de Safari (comienza con `web`, por ejemplo, `web.com.example.domain`). |
| Versión del SDK or kit de desarrollo de software web de Braze | La versión del SDK or kit de desarrollo de software web de Braze que deseas utilizar |
| Enviar automáticamente mensajes dentro de la aplicación | De forma predeterminada, todos los mensajes dentro de la aplicación para los que un usuario es elegible se entregan automáticamente al usuario. Deshabilita esta opción si deseas mostrar manualmente los mensajes dentro de la aplicación. |
| No cargar Font Awesome | Braze utiliza Font Awesome para los iconos de los mensajes dentro de la aplicación. De forma predeterminada, Braze cargará automáticamente FontAwesome desde el CDN de FontAwesome. Para deshabilitar este comportamiento (por ejemplo, porque tu sitio utiliza una versión personalizada de FontAwesome), establece esta opción en `TRUE`. Ten en cuenta que si haces esto, eres responsable de asegurar que FontAwesome esté cargado en tu sitio; de lo contrario, los mensajes dentro de la aplicación podrían no mostrarse correctamente. |
| Habilitar mensajes HTML dentro de la aplicación | Habilitar esta opción permitirá a los usuarios del panel de Braze utilizar mensajes HTML dentro de la aplicación. |
| Abrir mensajes dentro de la aplicación en una nueva pestaña | De forma predeterminada, los enlaces de los clics en mensajes dentro de la aplicación se cargan en la pestaña actual o en una nueva pestaña según se especifique en el panel para cada mensaje. Establece esta opción en `TRUE` para forzar que todos los enlaces de los clics en mensajes dentro de la aplicación se abran en una nueva pestaña o ventana. |
| Índice z de mensajes dentro de la aplicación | Proporciona un valor para esta opción para anular los índices z predeterminados de Braze. |
| Requerir descarte explícito de mensajes dentro de la aplicación | De forma predeterminada, cuando se muestra un mensaje dentro de la aplicación, al presionar la tecla de escape o hacer clic en el fondo gris de la página se descarta el mensaje. Establece esta opción en true para evitar este comportamiento y requerir un clic explícito en un botón para descartar los mensajes. |
| Intervalo mínimo entre acciones desencadenantes en segundos | El valor predeterminado es 30.<br>De forma predeterminada, una acción desencadenante solo se ejecutará si han transcurrido al menos 30 segundos desde la última acción desencadenante. Proporciona un valor para esta opción de configuración para anular ese valor predeterminado con uno propio. No recomendamos que este valor sea menor a 10 para evitar enviar notificaciones excesivas al usuario. |
| Ubicación del prestador de servicios | De forma predeterminada, al registrar usuarios para notificaciones push web, Braze buscará el archivo de prestador de servicios requerido en el directorio raíz de tu servidor web en `/service-worker.js`. Si deseas alojar tu prestador de servicios en una ruta diferente en ese servidor, proporciona un valor para esta opción que sea la ruta absoluta al archivo (por ejemplo, `/mycustompath/my-worker.js`). Ten en cuenta que establecer un valor aquí limita el alcance de las notificaciones push en tu sitio. Por ejemplo, en este caso, debido a que el archivo del prestador de servicios se encuentra dentro del directorio `/mycustompath/`, `requestPushPermission` solo puede llamarse desde páginas web que comiencen con `http://yoursite.com/mycustompath/`. |
| Deshabilitar mantenimiento de tokens de push | De forma predeterminada, los usuarios que ya han otorgado permisos de push web sincronizarán su token de push con el backend de Braze automáticamente en nuevas sesiones para asegurar la capacidad de entrega. Para deshabilitar este comportamiento, establece esta opción en `FALSE`. |
| Administrar prestador de servicios externamente | Si tienes tu propio prestador de servicios que registras y controlas su ciclo de vida, establece esta opción en `TRUE`, y el SDK or kit de desarrollo de software de Braze no registrará ni cancelará el registro de un prestador de servicios. Si estableces esta opción en `TRUE`, para que el push funcione correctamente, debes registrar el prestador de servicios tú mismo antes de llamar a `requestPushPermission` y asegurar que contenga el código del prestador de servicios de Braze, ya sea con `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` o incluyendo el contenido de ese archivo directamente. Cuando esta opción es `TRUE`, la opción `serviceWorkerLocation` es irrelevante y se ignora. |
| Nonce de seguridad de contenido | Si proporcionas un valor para esta opción, el SDK or kit de desarrollo de software de Braze añadirá el nonce a cualquier elemento `<script>` y `<style>` creado por el SDK or kit de desarrollo de software. Esto permite que el SDK or kit de desarrollo de software de Braze funcione con la política de seguridad de contenido de tu sitio web. Además de configurar este nonce, es posible que también necesites permitir la carga de FontAwesome, lo cual puedes hacer añadiendo `use.fontawesome.com` a la lista de permitidos de tu política de seguridad de contenido o utilizando la opción `doNotLoadFontAwesome` y cargándolo manualmente. |
| Permitir actividad de rastreadores | De forma predeterminada, el SDK or kit de desarrollo de software web de Braze ignora la actividad de arañas o rastreadores web conocidos, como Google, según la cadena del agente de usuario. Esto ahorra puntos de datos, hace que los análisis sean más precisos y puede mejorar el posicionamiento en páginas. Sin embargo, si deseas que Braze registre la actividad de estos rastreadores, puedes establecer esta opción en `TRUE`. |
| Habilitar registro | Establece en `TRUE` para habilitar el registro de forma predeterminada. Ten en cuenta que esto hará que Braze registre en la consola de JavaScript, que es visible para todos los usuarios. Antes de publicar tu página en producción, deberías eliminar esto o proporcionar un logger alternativo con `setLogger`. |
| Permitir JavaScript proporcionado por el usuario | De forma predeterminada, el SDK or kit de desarrollo de software web de Braze no permite acciones de clic en JavaScript proporcionadas por el usuario, ya que permite a los usuarios del panel de Braze ejecutar JavaScript en tu sitio. Para indicar que confías en los usuarios del panel de Braze para escribir acciones de clic en JavaScript no maliciosas, establece esta propiedad en `TRUE`. Si `enableHtmlInAppMessages` es `TRUE`, esta opción también se establecerá en `TRUE`. |
| Versión de la aplicación | Si proporcionas un valor para esta opción, los eventos de usuario enviados a Braze se asociarán con la versión dada, que se puede utilizar para la segmentación de usuarios. |
| Tiempo de espera de sesión en segundos | El valor predeterminado es 30.<br>De forma predeterminada, las sesiones expiran después de 30 minutos de inactividad. Proporciona un valor para esta opción de configuración para anular ese valor predeterminado con uno propio. |
| Lista de propiedades de dispositivo permitidas | De forma predeterminada, el SDK or kit de desarrollo de software de Braze detecta y recopila automáticamente todas las propiedades del dispositivo en `DeviceProperties`. Para anular este comportamiento, proporciona un array de `DeviceProperties`. Ten en cuenta que sin algunas propiedades, no todas las características funcionarán correctamente. Por ejemplo, la entrega por zona horaria local no funcionará sin la zona horaria. |
| Localización | De forma predeterminada, cualquier mensaje generado por el SDK or kit de desarrollo de software visible para el usuario se mostrará en el idioma del navegador del usuario. Proporciona un valor para esta opción para anular ese comportamiento y forzar un idioma específico. El valor para esta opción debe ser un código de idioma ISO 639-1. |
| Sin cookies | De forma predeterminada, el SDK or kit de desarrollo de software de Braze almacenará pequeñas cantidades de datos (IDs de usuario, IDs de sesión) en cookies. Esto se hace para permitir que Braze reconozca usuarios y sesiones en diferentes subdominios de tu sitio. Si esto te causa problemas, pasa `TRUE` para esta opción para deshabilitar el almacenamiento de cookies y depender completamente de HTML 5 localStorage para identificar usuarios y sesiones. |
| Rastrear todas las páginas | **Solo para destino clásico Web Device-Mode (mantenimiento)**<br><br>Segment recomienda migrar al destino del framework Web Actions donde esta configuración puede [habilitarse a través de mapeados](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Esto enviará todas las [llamadas de página](https://segment.com/docs/spec/page/) a Braze como un evento "Loaded/Viewed a Page". |
| Rastrear solo páginas con nombre | **Solo para destino clásico Web Device-Mode (mantenimiento)**<br><br>Segment recomienda migrar al destino del framework Web Actions donde esta configuración puede [habilitarse a través de mapeados](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Esto solo enviará llamadas de página a Braze que tengan un nombre asociado. |
| Registrar compra cuando hay ingresos presentes | **Solo para destino clásico Web Device-Mode (mantenimiento)**<br><br>Segment recomienda migrar al destino del framework Web Actions donde esta configuración puede [habilitarse a través de mapeados](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Cuando esta opción está habilitada, todas las llamadas Track con la propiedad de ingresos activarán un evento de compra. |
| Solo rastrear usuarios conocidos | **Solo para destino clásico Web Device-Mode (mantenimiento)**<br><br>Segment recomienda migrar al destino del framework Web Actions donde esta configuración puede habilitarse a través de mapeados.<br><br>Si se habilita, esta nueva configuración retrasará la llamada a `window.braze.initialize` hasta que haya un `userId` válido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Configuración" }

{% endtab %}
{% tab Cloud-Mode %}

| Configuración | Descripción |
| ------- | ----------- |
| Identificador de aplicación | El identificador de aplicación utilizado para hacer referencia a la aplicación específica. Se puede encontrar en el panel de Braze en **Manage Settings** |
| Clave de API REST or transferencia de estado representacional | Se puede encontrar en tu panel de Braze en **Settings** > **API Keys**. |
| Endpoint personalizado de la REST or transferencia de estado representacional API | Tu endpoint REST or transferencia de estado representacional de Braze que corresponde a tu instancia (como REST or transferencia de estado representacional.iad-01.braze.com). |
| Actualizar solo usuarios existentes | **Solo para destino clásico Cloud-Mode (mantenimiento)**<br><br>Segment recomienda migrar al destino del framework Cloud Actions donde esta configuración puede [habilitarse a través de mapeados](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Determina si solo se actualizan los usuarios existentes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Configuración" }

{% endtab %}
{% endtabs %}

### Paso 4: Mapear métodos {#methods}

Braze es compatible con los métodos [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify](https://segment.com/docs/spec/identify/) y [Track](https://segment.com/docs/spec/track/) de Segment. Los tipos de identificadores utilizados dentro de estos métodos dependerán de si los datos se envían a través de una integración servidor a servidor (cloud-mode) o en paralelo (device-mode). En los destinos Braze Web Mode Actions y Cloud Mode Actions, también puedes elegir configurar un mapeado para una [llamada de alias de Segment](https://segment.com/docs/connections/spec/alias/).

{% alert note %}
Aunque los alias de usuario son compatibles como identificador en el destino Braze Cloud Mode (Actions), se debe tener en cuenta que la llamada de alias de Segment no está directamente relacionada con los alias de usuario de Braze.
{% endalert %}

| Tipo de identificador | Destino compatible |
| --------------- | --------------------- |
| `userId` (`external_id`) | Todos |
| Usuario anónimo | Destinos en device-mode |
| Alias de usuario | Destinos en cloud-mode |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 4: Mapear métodos" }

El destino Cloud Mode (Actions) ofrece una [acción Crear alias](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias) que puede utilizarse para crear un usuario solo con alias o añadir un alias a un perfil `external_id` existente. La [acción Identificar usuario](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user) puede utilizarse junto con la acción Crear alias para fusionar un usuario solo con alias con un `external_id` una vez que esté disponible para el usuario.

También es posible diseñar una solución alternativa y utilizar `braze_id` para enviar datos de usuarios anónimos en cloud-mode. Esto requiere incluir manualmente el `braze_id` del usuario en todas tus llamadas a la API de Segment. Puedes obtener más información sobre cómo configurar esta solución alternativa en la [documentación de Segment](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users).

Los datos de destinos enviados a Braze se pueden agrupar en lotes dentro de Cloud Mode Actions. Los tamaños de lote están limitados a 75 eventos, y estos lotes se acumularán durante un periodo de 30 segundos antes de enviarse. El agrupamiento de solicitudes en lotes se realiza por acción. Por ejemplo, las llamadas Identify (atributos) se agruparán en una solicitud y las llamadas Track (eventos personalizados) se agruparán en una segunda solicitud. Braze recomienda habilitar esta característica ya que reducirá el número de solicitudes enviadas desde Segment a Braze. A su vez, esto reducirá el riesgo de que el destino alcance los límites de velocidad de Braze y necesite reintentar solicitudes.

Puedes activar el agrupamiento en lotes para una acción navegando a tu destino Braze > **Mappings**. Desde ahí, haz clic en el icono de los 3 puntos junto al mapeado y selecciona **Edit Mapping**. Desplázate hasta la parte inferior de la sección **Select mappings** y asegúrate de que **Batch Data to Braze** esté configurado en **Yes**.


{% tabs local %}
{% tab Identify %}
#### Identify

La llamada [Identify](https://segment.com/docs/spec/identify/) te permite vincular a un usuario con sus acciones y registrar atributos sobre él.

Ciertos traits especiales de Segment se mapean a campos de atributos estándar del perfil en Braze:

| Traits especiales de Segment | Atributos estándar de Braze |
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

Otros campos de perfil reservados de Braze como `email_subscribe` y `push_subscribe` pueden enviarse utilizando la convención de nombres de Braze para estos campos y pasándolos como traits dentro de una llamada identify.

##### Añadir un usuario a un grupo de suscripción {#adding-a-user-to-a-subscription-group}

También puedes suscribir o cancelar la suscripción de un usuario a un grupo de suscripción determinado utilizando los siguientes campos en el parámetro traits.

Utiliza el campo de perfil reservado de Braze llamado `braze_subscription_groups`, que puede asociarse con un array de objetos. Cada objeto en el array debe tener dos claves reservadas:

1. `subscription_group_state`: Indica si el usuario está `"subscribed"` o `"unsubscribed"` de un grupo de suscripción específico.
2. `subscription_group_id`: Representa el ID único del grupo de suscripción. Puedes encontrar este ID en el panel de Braze en **Subscription Group Management**.

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

Todos los demás traits se registrarán como [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).

| Método de Segment | Método de Braze | Ejemplo |
|---|---|---|
| Identify con ID de usuario | Establecer ID externo | Segment:  `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| Identify con traits reservados | Establecer atributos de usuario | Segment: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| Identify con traits personalizados | Establecer atributos personalizados | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| Identify con ID de usuario y traits | Segment: Establecer ID externo y atributo | Combina los métodos anteriores. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atributos personalizados" }

En los destinos [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) y [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile), estos mapeados pueden configurarse utilizando la acción Actualizar perfil de usuario.

{% alert important %}
Al pasar datos de atributos de usuario, verifica que solo pases valores para atributos que hayan cambiado desde la última actualización. Esto garantizará que no registres puntos de datos innecesariamente. Para fuentes del lado del cliente, utiliza la herramienta de código abierto [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) de Segment para optimizar tu integración y limitar el uso de puntos de datos eliminando llamadas `identify()` duplicadas de Segment.

{% endalert %}
{% endtab %}

{% tab Track %}
#### Track

Cuando rastreas un evento, registraremos ese evento como un [evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events) utilizando el nombre proporcionado.

Los metadatos enviados dentro del objeto de propiedades de la llamada track se registrarán en Braze como las propiedades del evento personalizado para el evento asociado. Todos los [tipos de datos de propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) son compatibles.

En los destinos [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) y [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event), estos mapeados pueden configurarse utilizando la acción Track Event.

| Método de Segment | Método de Braze | Ejemplo |
|---|---|---|
| [Track](https://segment.com/docs/spec/track/) | Registrado como un [evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events). | Segment: `analytics.track("played_game");` <br>Braze: `Braze.logCustomEvent("played_game");`|
| [Track con propiedades](https://segment.com/docs/spec/track/) | Registrado como [propiedad del evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties). | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Track con producto](https://segment.com/docs/spec/track/) | Registrado como un [evento de compra]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web). | Segment: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Track" }

##### Pedido completado {#order-completed}

Cuando rastreas un evento con el nombre `Order Completed` utilizando el formato descrito en la [API de eCommerce](https://segment.com/docs/spec/ecommerce/v2/) de Segment, registraremos los productos que hayas incluido como [compras]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data).

En los destinos [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) y [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase), el mapeado predeterminado puede personalizarse a través de la acción Track Purchase.

{% endtab %}

{% tab Page %}
#### Page {#page}

La llamada [Page](https://segment.com/docs/spec/page/) te permite registrar cada vez que un usuario ve una página de tu sitio web, junto con cualquier propiedad opcional sobre la página.

Este tipo de evento puede utilizarse como desencadenante en los destinos Web Mode Actions y Cloud Actions para registrar un evento personalizado en Braze.
{% endtab %}

{% endtabs %}

### Paso 5: Probar tu integración {#step-5-test-your-integration}

Al utilizar la integración en paralelo (device-mode), tus métricas del [resumen]({{site.baseurl}}/user_guide/analytics/dashboards/home) (sesiones de por vida, MAU or usuarios activos al mes, usuario activo diario, adherencia, sesiones diarias y sesiones diarias por MAU or usuarios activos al mes) pueden utilizarse para asegurar que Braze está recibiendo datos de Segment.

Puedes ver tus datos en las páginas de [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data#custom-event-data) o [ingresos]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data), o [creando un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment). La página **Custom Events** del panel te permite ver los recuentos de eventos personalizados a lo largo del tiempo. Ten en cuenta que no podrás utilizar [fórmulas]({{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula#creating-a-formula) que incluyan estadísticas de MAU or usuarios activos al mes y usuario activo diario cuando utilices una integración servidor a servidor (cloud-mode).

Si estás enviando datos de compras a Braze (consulta pedido completado en la pestaña **Track** del [Paso 3](#methods)), la página de [ingresos]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data) te permite ver datos sobre ingresos o compras durante periodos específicos o los ingresos totales de tu aplicación.

[Crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment) te permite filtrar tus usuarios según los datos de eventos personalizados y atributos.

{% alert important %}
Si utilizas una integración servidor a servidor (cloud-mode), los filtros relacionados con los datos de sesión capturados automáticamente (como "primera vez que usó la aplicación" y "última vez que usó la aplicación") no funcionarán. Utiliza una integración en paralelo (device-mode) si deseas usar estos filtros en tu integración de Segment y Braze.
{% endalert %}

## Eliminación y supresión de usuarios {#user-deletion-and-suppression}

Si necesitas eliminar o suprimir usuarios, ten en cuenta que la [función de eliminación de usuarios de Segment](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **está** mapeada al [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) de Braze. Ten en cuenta que la verificación de estas eliminaciones podría tardar hasta 30 días.

Debes asegurarte de seleccionar un identificador de usuario común entre Braze y Segment (como `external_id`). Una vez que hayas iniciado una solicitud de eliminación con Segment, puedes ver el estado en la pestaña de solicitudes de eliminación de tu panel de Segment.

## Repeticiones de Segment {#segment-replays}

Segment ofrece un servicio a los clientes para "repetir" todos los datos históricos hacia un nuevo partner tecnológico. Los nuevos clientes de Braze que deseen importar todos los datos históricos relevantes pueden hacerlo a través de Segment. Habla con tu representante de Segment si esto te interesa.

Segment se conectará a nuestro [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para importar datos de usuario en Braze en tu nombre.

{% alert important %}
Todos los identificadores compatibles con el destino en modo nube (Cloud Mode Actions) son compatibles como parte de las repeticiones de Segment.
{% endalert %}

## Prácticas recomendadas {#best-practices}

{% details Revisa los ejemplos para evitar excedentes de datos. %}

Segment **no** limita el número de elementos de datos que los clientes envían. Segment te permite enviar todos los eventos o decidir cuáles enviarás a Braze. En lugar de enviar todos tus eventos a través de Segment, te sugerimos que revises los ejemplos con tus equipos de marketing y editorial para determinar qué eventos enviarás a Braze y así evitar excedentes de datos.

{% enddetails %}

{% details Comprende la diferencia entre el endpoint de API personalizado y el endpoint de API REST or transferencia de estado representacional personalizado en la configuración del destino en modo dispositivo móvil. %}

| Terminología de Braze | Equivalente en Segment |
| ----------------- | ------------------ |
| Endpoint de SDK or kit de desarrollo de software de Braze | Endpoint de API personalizado |
| Endpoint REST or transferencia de estado representacional de Braze | Endpoint de API REST or transferencia de estado representacional personalizado |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prácticas recomendadas" }

Tu endpoint de API de Braze (llamado "Custom API Endpoint" en Segment) es el endpoint de SDK or kit de desarrollo de software que Braze configura para tu SDK or kit de desarrollo de software (por ejemplo, `sdk.iad-03.braze.com`). Tu endpoint de API REST or transferencia de estado representacional de Braze (llamado "Custom REST or transferencia de estado representacional API Endpoint" en Segment) es el endpoint de REST or transferencia de estado representacional API (por ejemplo, `https://rest.iad-03.braze.com`).
{% enddetails %}

{% details Asegúrate de que tu endpoint de API personalizado esté correctamente introducido en la configuración del destino en modo dispositivo móvil. %}

| Terminología de Braze | Equivalente en Segment |
| ----------------- | ------------------ |
| Endpoint de SDK or kit de desarrollo de software de Braze | Endpoint de API personalizado |
| Endpoint REST or transferencia de estado representacional de Braze | Endpoint de API REST or transferencia de estado representacional personalizado |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prácticas recomendadas" }

Debes seguir el formato adecuado para asegurarte de introducir correctamente tu endpoint de SDK or kit de desarrollo de software de Braze. Tu endpoint de SDK or kit de desarrollo de software de Braze no debe incluir `https://` (por ejemplo, `SDK or kit de desarrollo de software.iad-03.braze.com`), ya que de lo contrario la integración de Braze dejará de funcionar. Esto se debe a que Segment antepone automáticamente `https://` a tu endpoint, lo que provoca que Braze se inicialice con un endpoint no válido: `https://https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Matices del mapeado de datos. %}

Escenarios en los que los datos no se pasarán según lo esperado:

1. Atributos personalizados anidados
  - Aunque los [atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support) técnicamente pueden enviarse a Braze a través de Segment, la **carga útil completa** se enviará cada vez. Esto generará [puntos de datos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#data-points) por cada clave pasada en el objeto anidado cada vez que se envíe la carga útil.<br><br> Para utilizar solo un subconjunto de puntos de datos cuando se envíe la carga útil, puedes usar la característica de [funciones de destino](https://segment.com/docs/connections/functions/destination-functions/) personalizadas de Segment. Esta característica de la plataforma de Segment te permite personalizar cómo se envían los datos a los destinos posteriores.

  {% alert note %}
  Las funciones de destino personalizadas se controlan dentro de Segment, y Braze tiene una visibilidad limitada sobre las funciones que se hayan configurado externamente.
  {% endalert %}

{: start="2"}
2. Pasar datos anónimos de servidor a servidor.
  - Los clientes pueden usar las bibliotecas de servidor a servidor de Segment para canalizar datos anónimos a otros sistemas. Consulta la sección de métodos de mapeado para obtener más información sobre cómo enviar usuarios sin un `external_id` a Braze a través de una integración de servidor a servidor (modo nube).

{% enddetails %}

{% details Personalización de la inicialización de Braze. %}

Existen varias formas de personalizar Braze: push, mensajes dentro de la aplicación, Content Cards e inicialización. Con una integración en paralelo, puedes seguir personalizando push, mensajes dentro de la aplicación y Content Cards como lo harías con una integración directa de Braze.

Sin embargo, personalizar cuándo se integra el SDK or kit de desarrollo de software de Braze o especificar configuraciones de inicialización puede ser difícil y, a veces, no ser posible. Esto se debe a que Segment inicializará el SDK or kit de desarrollo de software de Braze por ti cuando se produzca la inicialización de Segment.

{% enddetails %}

{% details Enviar solo los cambios (deltas) a Braze. %}

Al pasar datos de atributos de usuario, comprueba que solo pasas valores para los atributos que hayan cambiado desde la última actualización. Esto evitará el registro de puntos de datos innecesarios. Para fuentes del lado del cliente, utiliza la herramienta de código abierto [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) de Segment para optimizar tu integración y limitar el uso de puntos de datos mediante la eliminación de llamadas `identify()` duplicadas de Segment.

{% enddetails %}

{% details Utiliza el centro de datos de Braze correcto. %}

Segment utiliza tu centro de datos de Braze para obtener el endpoint REST or transferencia de estado representacional de Braze adecuado (como `https://rest.iad-01.braze.com`) para realizar llamadas de servidor a servidor.

{% enddetails %}

{% details Elimina el endpoint de API REST or transferencia de estado representacional personalizado al usar el Event Tester de Segment. %}

El Event Tester de Segment envía eventos al endpoint de REST or transferencia de estado representacional API `/users/track` de Braze y genera un error `401 Invalid API Key` si se ha configurado un endpoint de API REST or transferencia de estado representacional personalizado en la configuración del destino de Braze, incluso cuando ese endpoint es correcto. Elimina el valor del endpoint de API REST or transferencia de estado representacional personalizado en Segment para que el Event Tester funcione correctamente.

{% enddetails %}

{% details Espera a que se apliquen las actualizaciones después de configurar una nueva fuente. %}

Segment mantiene la configuración en la caché durante mucho tiempo, por lo que al configurar una nueva fuente (como cambiar del modo nube al modo dispositivo) es posible que tu aplicación no muestre el nuevo comportamiento o los nuevos datos hasta que se renueve la caché. Ten en cuenta este retraso cuando planifiques añadir una fuente.

{% enddetails %}