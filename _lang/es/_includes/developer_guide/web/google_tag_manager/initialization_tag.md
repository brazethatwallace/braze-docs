### Requisitos previos {#prerequisites}

Antes de poder utilizar este método de integración, deberás [crear una cuenta y un contenedor para Google Tag Manager](https://support.google.com/tagmanager/answer/14842164).

### Paso 1: Abre la galería de plantillas de etiquetas {#step-1-open-the-tag-template-gallery}

En [Google Tag Manager](https://tagmanager.google.com/), elige tu espacio de trabajo y, a continuación, selecciona **Templates**. En el panel **Tag Template**, selecciona **Search Gallery**.

![La página de plantillas para un espacio de trabajo de ejemplo en Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### Paso 2: Añade la plantilla de etiqueta de inicialización {#step-2-add-the-initialization-tag-template}

En la galería de plantillas, busca `braze-inc` y selecciona **Braze Initialization Tag**.

![La galería de plantillas mostrando las distintas plantillas de "braze-inc".]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Selecciona **Add to workspace** > **Add**.

![La página "Braze Initialization Tag" en Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### Paso 3: Configura la etiqueta {#step-3-configure-the-tag}

En la sección **Templates**, selecciona la plantilla que acabas de añadir.

![La página "Templates" en Google Tag Manager mostrando la plantilla Braze Initialization Tag.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Selecciona el icono del lápiz para abrir el menú desplegable **Tag Configuration**.

![El mosaico Tag Configuration con el icono del "lápiz" mostrado.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Introduce la información mínima requerida:

| Campo | Descripción |
| ------------- | ----------- |
| **API Key** | Tu [clave de API de Braze]({{site.baseurl}}/api/basics#about-rest-api-keys), que se encuentra en el panel de Braze en **Settings** > **App Settings**. |
| **API Endpoint** | La URL de tu endpoint REST. Tu endpoint dependerá de la URL de Braze para [tu instancia]({{site.baseurl}}/api/basics#endpoints). |
| **SDK Version** | La versión `MAJOR.MINOR` más reciente del SDK Web de Braze que aparece en el [registro de cambios]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web). Por ejemplo, si la última versión es `4.1.2`, introduce `4.1`. Para más información, consulta [Acerca de la gestión de versiones del SDK]({{site.baseurl}}/developer_guide/sdk_integration/version_management). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 3: Configura la etiqueta" }

Para configuraciones de inicialización adicionales, selecciona **Braze Initialization Options** y elige las opciones que necesites.

![La lista de opciones de inicialización de Braze en "Tag Configuration".]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### Paso 4: Elige las opciones de inicialización {#step-4-choose-initialization-options}

La etiqueta de inicialización de Braze expone las siguientes opciones. La mayoría se mapean directamente a las [`InitializationOptions` del SDK Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions), y algunas corresponden a métodos del SDK Web que la etiqueta llamará durante la inicialización. Selecciona las opciones que se ajusten a tus necesidades de integración:

| Opción GTM | Configuración o método del SDK Web | Descripción |
| --- | --- | --- |
| **Allow HTML In-App Messages** | `allowUserSuppliedJavascript` | Habilita mensajes HTML dentro de la aplicación, banners y acciones de clic JavaScript proporcionadas por el usuario. Necesario para [mensajes HTML dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html) y [banners]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web) que utilizan HTML personalizado. Habilita esta opción solo si confías en el contenido HTML y JavaScript, ya que permite la ejecución de JavaScript proporcionado por el usuario. |
| **App Version Number** | `appVersion`, `appVersionNumber` | Versión de la aplicación para segmentación (por ejemplo, `1.2.3.4`). |
| **Automatically Open New Session** | `braze.openSession()` | Abre una nueva sesión después de que el SDK se inicialice llamando a este método por ti. |
| **Automatically show new in app messages** | `braze.automaticallyShowInAppMessages()` | Muestra automáticamente los nuevos mensajes dentro de la aplicación cuando llegan del servidor llamando a este método después de la inicialización. |
| **Disable Automatic Push Token Maintenance** | `disablePushTokenMaintenance` | Impide que el SDK sincronice los tokens de notificaciones push con el backend de Braze en las nuevas sesiones. |
| **Disable Automatic Service Worker Registration** | `manageServiceWorkerExternally` | Úsalo si tú mismo realizas el registro y controlas el prestador de servicios. |
| **Disable Cookies** | `noCookies` | Utiliza localStorage en lugar de cookies para los datos de usuario/sesión. Evita el reconocimiento entre subdominios. |
| **Disable Font Awesome** | `doNotLoadFontAwesome` | Evita que el SDK cargue Font Awesome desde el CDN. Úsalo si tu sitio tiene su propio Font Awesome. |
| **Enable SDK Authentication** | `enableSdkAuthentication` | Habilita la [autenticación SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication). |
| **Enable Web SDK Logging** | `enableLogging` | Habilita el registro en consola para depuración. Elimínalo antes de pasar a producción. |
| **Minimum Interval Between Triggered Messages** | `minimumIntervalBetweenTriggerActionsInSeconds` | Segundos mínimos entre acciones desencadenantes (predeterminado: 30). |
| **Open Cards in New Tab** | `openCardsInNewTab` | Abre los enlaces de las tarjetas de contenido en una nueva pestaña cuando se utiliza la interfaz de usuario predeterminada de la fuente. |
| **Service Worker Location** | `serviceWorkerLocation` | Ruta personalizada para el archivo del prestador de servicios (predeterminado: `/service-worker.js`). |
| **Session Timeout (seconds)** | `sessionTimeoutInSeconds` | Tiempo de espera de la sesión en segundos (predeterminado: 1800). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 4: Elige las opciones de inicialización" }

{% alert note %}
Para habilitar los [mensajes HTML personalizados dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html) cuando utilices la etiqueta de inicialización de Braze de Google Tag Manager, selecciona **Allow HTML In-App Messages** en **Braze Initialization Options**. Esta casilla de verificación se mapea con la opción de inicialización `allowUserSuppliedJavascript` en `braze.initialize()` y la establece en `true`. La etiqueta de inicialización de Braze de Google Tag Manager utiliza esta etiqueta en lugar del nombre de la opción.
{% endalert %}

Para las opciones que no aparecen en la plantilla GTM (como `contentSecurityNonce`, `localization` o `devicePropertyAllowlist`), utiliza la [inicialización en tiempo de ejecución]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web).

### Paso 5: Configura para desencadenar en *todas las páginas* {#step-5-set-to-trigger-on-all-pages}

La etiqueta de inicialización debe ejecutarse en todas las páginas de tu sitio web. Esto te permite utilizar los métodos del SDK de Braze y registrar análisis de notificaciones push web.

{% alert important %}
**Secuenciación de etiquetas:** La etiqueta de inicialización de Braze debe dispararse antes que cualquier otra etiqueta que llame a métodos del SDK de Braze (como `braze.getUser()` o `braze.logCustomEvent()`). Si los eventos personalizados, los atributos de usuario u otras llamadas a métodos de Braze se disparan antes de que el SDK se inicialice, puedes encontrar errores como `Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')`. Para garantizar la secuenciación correcta, configura tu etiqueta de inicialización de Braze como una etiqueta de configuración o utiliza la característica de secuenciación de etiquetas de GTM para garantizar que se dispare primero. Para más información, consulta [Secuenciación de etiquetas para etiquetas de acción de Braze]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/?sdktab=web#web_tag-sequencing-for-braze-action-tags).
{% endalert %}

### Paso 6: Verifica tu integración {#step-6-verify-your-integration}

Puedes verificar tu integración utilizando cualquiera de las siguientes opciones:

- **Opción 1:** Con la [herramienta de depuración](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager, puedes comprobar si la etiqueta de inicialización de Braze se desencadena correctamente en las páginas o eventos que has configurado.
- **Opción 2:** Comprueba si hay solicitudes de red realizadas a Braze desde tu página web. Además, la biblioteca global `window.braze` debería estar definida.