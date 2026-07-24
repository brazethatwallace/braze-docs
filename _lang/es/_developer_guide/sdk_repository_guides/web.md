---
nav_title: SDK web
article_title: Guía del repositorio del SDK web
page_order: 1
description: "Referencia del README del SDK web de Braze reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guía del repositorio del SDK web {#web-sdk-repository-guide}

## Acerca del SDK web de Braze {#about-the-braze-web-sdk}

El SDK web de Braze te permite integrar la plataforma de interacción con los clientes de Braze directamente en tus aplicaciones web. Creado con TypeScript y diseñado para el desarrollo web moderno, este SDK proporciona herramientas completas para la gestión de usuarios, mensajería, análisis y conmutadores de características.

### Lo que puedes hacer {#what-you-can-do}

- **Gestión de usuarios**: rastrea y gestiona identidades de usuarios, atributos y comportamiento en tu aplicación web
- **In-App Messages**: muestra mensajes y notificaciones dirigidos a los usuarios mientras están usando activamente tu sitio
- **Content Cards**: muestra feeds de contenido personalizados y tarjetas promocionales que se actualizan en tiempo real
- **Banners**: muestra mensajes de banner en ubicaciones específicas dentro de tu sitio
- **Notificaciones push**: envía notificaciones push web para interactuar con los usuarios incluso cuando no están en tu sitio
- **Conmutadores de características**: controla el despliegue de características y las pruebas A/B con la gestión de conmutadores de características del lado del servidor
- **Análisis**: rastrea eventos personalizados, interacciones de usuarios y métricas de conversión
- **Gestión de sesiones**: monitoriza las sesiones de los usuarios y los patrones de interacción

Ya sea que estés creando una aplicación de página única, un sitio de comercio electrónico o una plataforma de contenido, el SDK web de Braze proporciona las herramientas que necesitas para crear experiencias de usuario personalizadas y atractivas que impulsen el crecimiento y la retención.

## Requisitos previos {#prerequisites}

Antes de integrar el SDK web de Braze, necesitarás:

{% multi_lang_include developer_guide/sdk_api_prerequisites.md %}

### Obtener tus credenciales {#getting-your-credentials}

1. **Clave de API**: se encuentra en tu panel de Braze en **Configuración** > **Claves de API**
2. **Punto final de SDK**: se encuentra en **Configuración** > **Autenticación SDK** > **Puntos finales**
3. **Service worker**: necesario para las notificaciones push (consulta la sección de notificaciones push)

## Instalación {#installation}

``` bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

## Inicio rápido {#quick-start}

El siguiente fragmento muestra la configuración mínima necesaria para inicializar el SDK web de Braze.

``` typescript
import * as braze from "@braze/web-sdk";

// Initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
});

braze.changeUser('Jane Doe');
```

## Referencia de configuración {#configuration-reference}

### Opciones de inicialización {#initialization-options}

La función `initialize` acepta un objeto de opciones con las siguientes propiedades:

| Opción | Tipo | Predeterminado | Descripción |
|--------|------|----------------|-------------|
| `baseUrl` | `string` | **Obligatorio** | Esta opción es obligatoria para configurar el SDK web de Braze para que utilice el endpoint adecuado para tu integración; por ejemplo: `braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'sdk.iad-03.braze.com' })` |
| `enableLogging` | `boolean` | `false` | Establécelo en true para habilitar el registro de forma predeterminada. Ten en cuenta que esto hará que Braze registre en la consola de JavaScript, que es visible para todos los usuarios. Probablemente deberías eliminar esto o proporcionar un registrador alternativo con setLogger antes de publicar tu página en producción. |
| `allowUserSuppliedJavascript` | `boolean` | `false` | De forma predeterminada, el SDK web de Braze no permite acciones de clic de JavaScript proporcionadas por el usuario, ni habilita mensajes dentro de la aplicación HTML ni Banners, ya que permiten a los usuarios del panel de Braze ejecutar JavaScript en tu sitio. Para indicar que confías en los usuarios del panel de Braze para escribir acciones de clic de JavaScript no maliciosas, establece esta propiedad en true. |
| `doNotLoadFontAwesome` | `boolean` | `false` | Braze utiliza Font Awesome para los iconos de los mensajes dentro de la aplicación. De forma predeterminada, Braze cargará automáticamente FontAwesome 4.7.0 desde el CDN de FontAwesome. Para deshabilitar este comportamiento (por ejemplo, porque tu sitio utiliza una versión personalizada de FontAwesome), establece esta opción en `true`. Ten en cuenta que si haces esto, eres responsable de asegurar que FontAwesome esté cargado en tu sitio; de lo contrario, los mensajes dentro de la aplicación podrían no renderizarse correctamente. |
| `inAppMessageZIndex` | `number` | `999999` | De forma predeterminada, el SDK de Braze mostrará In-App Messages con un z-index de 999999. Proporciona un valor para esta opción para anular ese valor predeterminado. |
| `sessionTimeoutInSeconds` | `number` | `30` | De forma predeterminada, una sesión expira después de 30 segundos de inactividad. Proporciona un valor para esta opción para anular ese valor predeterminado. |
| `deviceId` | `string` | Autogenerado | De forma predeterminada, Braze asignará un guid aleatorio como ID de dispositivo. Proporciona un valor para esta opción de configuración para anular ese valor predeterminado con un valor propio. |
| `appVersion` | `string` | `undefined` | Si proporcionas un valor para esta opción, los eventos de usuario enviados a Braze se asociarán con la versión dada, que puede utilizarse para la segmentación de usuarios. |
| `appVersionNumber` | `string` | `undefined` | Un valor numérico de versión de la aplicación que puede utilizarse para la segmentación de usuarios. Este valor debe enviarse con cuatro campos, como "1.2.3.4"; de lo contrario, se ignorará. Nota: `appVersion` también debe establecerse, ya sea con el mismo valor o con un nombre único para esta versión. |
| `contentSecurityNonce` | `string` | `undefined` | Si proporcionas un valor para esta opción, el SDK de Braze añadirá el nonce a cualquier elemento `<script>` y `<style>` creado por el SDK. Esto puede utilizarse para permitir que el SDK de Braze funcione con la Política de Seguridad de Contenido de tu sitio web. Ten en cuenta que, además de establecer este nonce, también puede ser necesario permitir que FontAwesome se cargue, lo cual puedes hacer añadiendo `use.fontawesome.com` a la lista de permitidos de tu Política de Seguridad de Contenido o utilizando la opción `doNotLoadFontAwesome` y cargándolo manualmente. |
| `noCookies` | `boolean` | `false` | De forma predeterminada, el SDK web de Braze utiliza cookies. Para deshabilitar el uso de cookies, establece esta opción en true. Ten en cuenta que deshabilitar las cookies puede afectar la capacidad del SDK para recordar las identidades de los usuarios entre sesiones. |
| `allowCrawlerActivity` | `boolean` | `false` | De forma predeterminada, el SDK web de Braze ignora la actividad de arañas web o rastreadores conocidos, como Google, basándose en la cadena de agente de usuario. Esto ahorra puntos de datos, hace que los análisis sean más precisos y puede mejorar el posicionamiento en buscadores. Sin embargo, si deseas que Braze registre la actividad de estos rastreadores, puedes establecer esta opción en true. |
| `disablePushTokenMaintenance` | `boolean` | `false` | De forma predeterminada, los usuarios que ya han concedido permiso de push web (por ejemplo, a través de requestPushPermission o de un proveedor de push anterior) sincronizarán su token de push con el backend de Braze automáticamente en cada nueva sesión para garantizar la capacidad de entrega. Para deshabilitar este comportamiento, establece esta opción en true. |
| `enableSdkAuthentication` | `boolean` | `false` | Establécelo en true para habilitar la característica de autenticación SDK. Para más información sobre la autenticación SDK, consulta nuestra documentación del producto. |
| `manageServiceWorkerExternally` | `boolean` | `false` | De forma predeterminada, el SDK web de Braze gestiona su propio service worker para las notificaciones push. Si ya estás gestionando un service worker en tu aplicación y deseas incorporar la funcionalidad del service worker de Braze en él, establece esta opción en true e incluye el código del service worker de Braze en tu archivo de service worker. |
| `minimumIntervalBetweenTriggerActionsInSeconds` | `number` | `30` | De forma predeterminada, las acciones desencadenantes (por ejemplo, mostrar un mensaje dentro de la aplicación) pueden activarse como máximo una vez cada 30 segundos por usuario. Proporciona un valor para esta opción para anular ese valor predeterminado. |
| `serviceWorkerLocation` | `string` | `undefined` | De forma predeterminada, el SDK web de Braze buscará su archivo de service worker en la raíz de tu dominio. Proporciona un valor para esta opción para anular ese valor predeterminado y especificar una ubicación personalizada para el archivo del service worker. |
| `safariWebsitePushId` | `string` | `undefined` | Obligatorio para las notificaciones push de Safari. Este valor se puede encontrar en tu cuenta de Apple Developer. Para más información sobre la configuración de las notificaciones push de Safari, consulta nuestra documentación del producto. |
| `localization` | `string` | `undefined` | Si proporcionas un valor para esta opción, el SDK de Braze intentará mostrar los mensajes dentro de la aplicación y las Content Cards en ese idioma. |
| `openInAppMessagesInNewTab` | `boolean` | `false` | De forma predeterminada, los enlaces en los mensajes dentro de la aplicación se abren en la misma pestaña. Establece esta opción en true para que se abran en una nueva pestaña. |
| `openCardsInNewTab` | `boolean` | `false` | De forma predeterminada, los enlaces en las Content Cards se abren en la misma pestaña. Establece esta opción en true para que se abran en una nueva pestaña. |
| `requireExplicitInAppMessageDismissal` | `boolean` | `false` | De forma predeterminada, los mensajes dentro de la aplicación pueden descartarse haciendo clic fuera de ellos o presionando la tecla Escape. Establece esta opción en true para requerir que los usuarios hagan clic explícitamente en un botón de descarte o en un botón de acción para descartar el mensaje. |
| `devicePropertyAllowlist` | `string[]` | `undefined` | De forma predeterminada, el SDK de Braze detecta y recopila automáticamente todas las propiedades del dispositivo en DeviceProperties. Para anular este comportamiento, proporciona un array de DeviceProperties. Para deshabilitar el envío de todas las propiedades a los servidores de Braze, proporciona un array vacío. Ten en cuenta que sin algunas propiedades, no todas las características funcionarán correctamente. Por ejemplo, sin la zona horaria, la entrega en zona horaria local no funcionará. |
| `serviceWorkerScope` | `string` | `undefined` | De forma predeterminada, el SDK web de Braze registrará su service worker con el alcance predeterminado (el directorio del service worker). Proporciona un valor para esta opción para anular ese valor predeterminado y especificar un alcance personalizado para el service worker. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Opciones de inicialización" }

---

## Características principales {#core-features}

### Inicialización y configuración {#initialization-setup}

#### Inicialización básica {#basic-initialization}

``` typescript
import * as braze from "@braze/web-sdk";

// Initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: 'YOUR-SDK-ENDPOINT-HERE',
    enableLogging: true // Remove in production
});

// Start a session
braze.openSession();
```

#### Opciones de inicialización avanzadas {#advanced-initialization-options}

``` typescript
import * as braze from "@braze/web-sdk";

braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: 'YOUR-SDK-ENDPOINT-HERE',
    enableLogging: true,
    allowUserSuppliedJavascript: true,
    doNotLoadFontAwesome: false,
    inAppMessageZIndex: 999999,
    sessionTimeoutInSeconds: 30,
    deviceId: 'custom-device-id',
    appVersion: '1.0.0',
    contentSecurityNonce: 'your-nonce-here'
});
```

### Gestión de usuarios {#user-management}

#### Cambiar usuario {#change-user}

``` typescript
import { changeUser } from "@braze/web-sdk";

// Change to a new user
changeUser('user-123');
```

#### Establecer atributos de usuario {#set-user-attributes}

``` typescript
import { getUser } from "@braze/web-sdk";

const user = getUser();
if (user) {
    user.setEmail('user@example.com');
    user.setFirstName('John');
    user.setLastName('Doe');
    user.setCustomUserAttribute('subscription_tier', 'premium');
    user.setCustomUserAttribute('last_login', new Date());
}
```

#### Establecer ubicación del usuario {#set-user-location}

``` typescript
import { getUser } from "@braze/web-sdk";

const user = getUser();
if (user) {
    user.setCountry('US');
    user.setHomeCity('San Francisco');
    user.setLanguage('en');
    user.setCustomLocationAttribute('latitude', 37.7749);
    user.setCustomLocationAttribute('longitude', -122.4194);
}
```

#### Alias de usuario y grupos de suscripción {#user-aliases-and-subscription-groups}

``` typescript
import { getUser } from "@braze/web-sdk";

const user = getUser();
if (user) {
    // Add alias
    user.addAlias('external_id', '12345');

    // Add to subscription group
    user.addToSubscriptionGroup('newsletter_subscribers');

    // Remove from subscription group
    user.removeFromSubscriptionGroup('old_subscribers');
}
```

#### Cierre de sesión del usuario {#user-logout}

``` typescript
import { wipeData } from "@braze/web-sdk";

// There is no explicit method to logout. To "forget" the current users entirely, use wipeData().
// This is a complete data wipe (use with caution, this wipes things such as device ID)
wipeData();
```

### In-App Messages

#### Visualización automática {#automatic-display}

``` typescript
import { automaticallyShowInAppMessages } from "@braze/web-sdk";

// Automatically show in-app messages
automaticallyShowInAppMessages();
```

#### Visualización manual {#manual-display}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

// Subscribe to in-app messages
subscribeToInAppMessage((inAppMessage) => {
    // Show the message
    showInAppMessage(inAppMessage);
});
```

#### Gestión personalizada de In-App Messages {#custom-in-app-message-handling}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

subscribeToInAppMessage((inAppMessage) => {
    // Custom logic before showing
    if (inAppMessage.getExtras()['priority'] === 'high') {
        showInAppMessage(inAppMessage);
    }
});
```

#### Registrar interacciones de In-App Messages {#log-in-app-message-interactions}

``` typescript
import {
    logInAppMessageClick,
    logInAppMessageImpression,
    logInAppMessageButtonClick
} from "@braze/web-sdk";

// Log when user sees the message
logInAppMessageImpression(inAppMessage);

// Log when user clicks the message
logInAppMessageClick(inAppMessage);

// Log when user clicks a button in the message
logInAppMessageButtonClick(inAppMessage, button);
```

#### In-App Messages HTML personalizados {#custom-html-in-app-messages}

``` typescript
import { subscribeToInAppMessage, logInAppMessageImpression, logInAppMessageClick } from "@braze/web-sdk";

// Don't call automaticallyShowInAppMessages() when using custom rendering
// braze.automaticallyShowInAppMessages(); // Comment this out

subscribeToInAppMessage((inAppMessage) => {
    // Extract message data
    const messageData = {
        title: inAppMessage.getMessage(),
        body: inAppMessage.getBody(),
        imageUrl: inAppMessage.getImageUrl(),
        buttons: inAppMessage.getButtons(),
        deepLink: inAppMessage.getExtras()['deep_link_url']
    };

    // Define your own HTML structure, using messageData
    const customHTML = ` <!-- Add your custom styling and structure -->`;

    /* Render the In-App Message here */

    // Here we naively log an impression once the message is rendered.
    // Be precise about exactly when you want to log an impression (ie. only the first time it enters the view port).
    logInAppMessageImpression(inAppMessage);
});

// Handle button clicks and deep linking
const handleButtonClick = (button, inAppMessage) => {
    logInAppMessageClick(inAppMessage);
    // Handle additional click actions (ie. deep linking)
};
```

### Content Cards

#### Mostrar Content Cards {#display-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show content cards in default location
showContentCards();

// Show in specific container
const container = document.getElementById('content-cards-container');
showContentCards(container);
```

#### Suscribirse a actualizaciones de Content Cards {#subscribe-to-content-cards-updates}

``` typescript
import { subscribeToContentCardsUpdates } from "@braze/web-sdk";

subscribeToContentCardsUpdates((cards) => {
    console.log('Content cards updated:', cards);
    // Display cards or update UI
});
```

#### Registrar interacciones de Content Cards {#log-content-card-interactions}

``` typescript
import {
    logContentCardClick,
    logContentCardImpressions,
    logCardDismissal
} from "@braze/web-sdk";

// Log card impressions
logContentCardImpressions(cards);

// Log card clicks
logContentCardClick(card);

// Log card dismissals
logCardDismissal(card);
```

#### Filtrar Content Cards {#filter-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show only pinned cards
// You can also provide a parent element instead of null
showContentCards(null, (cards) => {
    return cards.filter(card => card.getIsPinned());
});
```

#### Solicitar actualización de Content Cards {#request-content-cards-refresh}

``` typescript
import { requestContentCardsRefresh } from "@braze/web-sdk";

requestContentCardsRefresh(
    () => console.log('Content cards refreshed'),
    () => console.log('Failed to refresh content cards')
);
```

#### Content Cards personalizadas {#custom-content-cards}

``` typescript
import { subscribeToContentCardsUpdates, logContentCardClick, logContentCardImpressions, requestContentCardsRefresh } from "@braze/web-sdk";

// State for impression de-duping
const loggedImpressions = new Set();
const idToCard = new Map();

subscribeToContentCardsUpdates((cards) => {
    // Build cards one by one
    cards.getCards().forEach(card => {
        // Skip control cards
        if (card.getIsControl()) return;

        // Extract card data
        const cardData = {
            id: card.getId(),
            title: card.getTitle(),
            description: card.getDescription(),
            imageUrl: card.getImageUrl(),
            url: card.getUrl(),
            extras: card.getExtras()
        };

        // Define your own HTML structure, using cardData
        const customHTML = ` <!-- Add your custom styling and structure -->`;

        /* Render each card here */

        // Basic observer for impression logging.
        // Be precise about exactly when you want to log an impression (ie. only the first time it enters the view port).
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    logContentCardImpressions([card]);
                }
            });
        });

        // Observe card element when rendered
        // observer.observe(cardElement);
    });
});

// Handle card clicks
const handleCardClick = (card) => {
    logContentCardClick(card);
    // Handle additional click actions (ie. navigation)
};

```

### Notificaciones push {#push-notifications}

#### Solicitar permiso de push {#request-push-permission}

``` typescript
import { requestPushPermission } from "@braze/web-sdk";

requestPushPermission(
    () => console.log('Push permission granted'),
    () => console.log('Push permission denied')
);
```

#### Comprobar compatibilidad con push {#check-push-support}

``` typescript
import { isPushSupported, isPushPermissionGranted } from "@braze/web-sdk";

if (isPushSupported()) {
    if (isPushPermissionGranted()) {
        console.log('Push notifications are enabled');
    } else {
        console.log('Push permission not granted');
    }
}
```

#### Cancelar registro de push {#unregister-push}

``` typescript
import { unregisterPush } from "@braze/web-sdk";

unregisterPush(
    () => console.log('Successfully unregistered'),
    () => console.log('Failed to unregister')
);
```

### Conmutadores de características {#feature-flags}

#### Obtener un conmutador de características {#get-feature-flag}

``` typescript
import { getFeatureFlag } from "@braze/web-sdk";

const featureFlag = getFeatureFlag('new_checkout_flow');
if (featureFlag) {
    const isEnabled = featureFlag.getBooleanProperty('enabled', false);
    const rolloutPercentage = featureFlag.getNumberProperty('rollout_percentage', 0);

    if (isEnabled) {
        // Enable new checkout flow
    }
}
```

#### Suscribirse a actualizaciones de conmutadores de características {#subscribe-to-feature-flag-updates}

``` typescript
import { subscribeToFeatureFlagsUpdates } from "@braze/web-sdk";

subscribeToFeatureFlagsUpdates((featureFlags) => {
    featureFlags.forEach(flag => {
        console.log(`Feature flag ${flag.getId()}: ${flag.getBooleanProperty('enabled')}`);
    });
});
```

#### Registrar impresiones de conmutadores de características {#log-feature-flag-impressions}

``` typescript
import { logFeatureFlagImpression } from "@braze/web-sdk";

const featureFlag = getFeatureFlag('new_feature');
if (featureFlag) {
    logFeatureFlagImpression(featureFlag);
}
```

#### Solicitar actualización de conmutadores de características {#request-feature-flags-refresh}

``` typescript
import { refreshFeatureFlags } from "@braze/web-sdk";

refreshFeatureFlags(
    () => console.log('Feature flags refreshed'),
    () => console.log('Failed to refresh feature flags')
);
```

### Banners {#banners}

#### Obtener y mostrar banners {#get-and-display-banners}

``` typescript
import { getBanner, insertBanner } from "@braze/web-sdk";

const banner = getBanner('homepage_banner');
if (banner) {
    // Insert banner into specific element
    const container = document.getElementById('banner-container');
    insertBanner(banner, container);
}
```

#### Suscribirse a actualizaciones de banners {#subscribe-to-banner-updates}

``` typescript
import { insertBanner, subscribeToBannersUpdates } from "@braze/web-sdk";

subscribeToBannersUpdates((banners) => {
    Object.entries(banners).forEach(([placementId, banner]) => {
        if (banner) {
            console.log(`Banner for ${placementId}:`, banner);

            // Insert banner into specific element
            const container = document.getElementById(`banner-container-${placementId}`);
            insertBanner(banner, container);
        }
    });
});
```

#### Descartar banners en una interfaz personalizada {#dismiss-banners-in-a-custom-ui}

``` typescript
import { dismissBanner, getBanner, subscribeToBannersUpdates } from "@braze/web-sdk";

subscribeToBannersUpdates((banners) => {
    const banner = getBanner("homepage_banner");
    const container = document.getElementById("custom-banner-container");
    if (!container) {
        return;
    }

    if (!banner) {
        container.replaceChildren();
        return;
    }

    banner.subscribeToDismissedEvent(() => {
        console.log("Dismissed banner:", banner);
    });

    const closeButton = document.createElement("button");
    closeButton.textContent = "Close";
    closeButton.addEventListener("click", () => {
        dismissBanner(banner);
    });

    // Render your custom UI here and include the close button.
});
```

Cuando llamas a `dismissBanner(banner)`, el SDK gestiona el estado de descarte del banner, lo elimina de las actualizaciones activas de banners, notifica a los suscriptores del evento de descarte del banner y sincroniza el descarte con Braze. Las interfaces personalizadas deben usar `subscribeToBannersUpdates` para reaccionar a la eliminación del banner descartado, en lugar de tratar `dismissBanner` solo como un cambio local de la interfaz o solo como un método de registro de análisis.

#### Solicitar actualización de banners {#request-banner-refresh}

``` typescript
import { requestBannersRefresh } from "@braze/web-sdk";

requestBannersRefresh(
    ["placement_1", "placement_2"],
    () => console.log('Banners refreshed'),
    () => console.log('Failed to refresh banners')
);
```

### Análisis y eventos {#analytics-events}

#### Registrar eventos personalizados {#log-custom-events}

``` typescript
import { logCustomEvent } from "@braze/web-sdk";

// Simple event
logCustomEvent('button_clicked');

// Event with properties
logCustomEvent('purchase', {
    product_id: '123',
    price: 29.99,
    currency: 'USD'
});
```

#### Registrar compras {#log-purchases}

``` typescript
import { logPurchase } from "@braze/web-sdk";

logPurchase('product-123', 29.99, 'USD', 1, {
    category: 'electronics',
    brand: 'Apple'
});
```

#### Solicitar envío inmediato de datos {#request-data-flush}

``` typescript
import { requestImmediateDataFlush } from "@braze/web-sdk";

// Force immediate data send
requestImmediateDataFlush();
```

### Gestión de sesiones {#session-management}

#### Abrir sesión {#open-session}

``` typescript
import { openSession } from "@braze/web-sdk";

// Start a new session
openSession();
```

#### Comprobar el estado del SDK {#check-sdk-status}

``` typescript
import { isInitialized, isDisabled } from "@braze/web-sdk";

if (isInitialized()) {
    console.log('SDK is initialized');

    if (isDisabled()) {
        console.log('SDK is disabled');
    }
}
```

#### Habilitar/deshabilitar el SDK {#enabledisable-sdk}

``` typescript
import { enableSDK, disableSDK } from "@braze/web-sdk";

// Disable SDK
disableSDK();

// Re-enable SDK
enableSDK();
```

### Gestión de datos {#data-management}

#### Borrar datos {#wipe-data}

``` typescript
import { wipeData } from "@braze/web-sdk";

// Remove all locally stored data
wipeData();
```

#### Destruir el SDK {#destroy-sdk}

``` typescript
import { destroy } from "@braze/web-sdk";

// Clean up SDK resources
destroy();
```

#### Obtener el ID de dispositivo {#get-device-id}

``` typescript
import { getDeviceId } from "@braze/web-sdk";

const deviceId = getDeviceId();
console.log('Device ID:', deviceId);
```

#### Autenticación SDK {#sdk-authentication}

``` typescript
import { setSdkAuthenticationSignature } from "@braze/web-sdk";

// Set authentication signature
setSdkAuthenticationSignature('your-signature-here');
```

#### Suscribirse a fallos de autenticación {#subscribe-to-authentication-failures}

``` typescript
import { subscribeToSdkAuthenticationFailures } from "@braze/web-sdk";

subscribeToSdkAuthenticationFailures((error) => {
    console.log('Authentication failed:', error);
    // Provide new signature
    setSdkAuthenticationSignature('new-signature');
});
```

---

## Patrones de integración {#integration-patterns}

### Frameworks SSR {#ssr-frameworks}

Si utilizas un framework de renderizado del lado del servidor (SSR) como Next.js, es posible que encuentres errores porque el SDK está diseñado para ejecutarse en un entorno de navegador. Puedes resolver estos problemas importando el SDK de forma dinámica.

Puedes conservar los beneficios del tree-shaking al hacerlo exportando las partes del SDK que necesitas en un archivo separado y luego importando dinámicamente ese archivo en tu componente.

``` javascript
// MyComponent/braze-exports.js
// export the parts of the SDK you need here
export { initialize, openSession } from "@braze/web-sdk";

// MyComponent/MyComponent.js
// import the functions you need from the braze exports file
useEffect(() => {
    import("./braze-exports.js").then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

Alternativamente, si utilizas webpack para empaquetar tu aplicación, puedes aprovechar sus comentarios mágicos para importar dinámicamente solo las partes del SDK que necesitas.

``` javascript
// MyComponent.js
useEffect(() => {
    import(
        /* webpackExports: ["initialize", "openSession"] */
        "@braze/web-sdk"
    ).then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

### Vite

Si utilizas Vite y ves una advertencia sobre dependencias circulares o `Uncaught TypeError: Class extends value undefined is not a constructor or null`, es posible que necesites excluir el SDK de Braze de su descubrimiento de dependencias:

``` javascript
export default {
    optimizeDeps: {
        exclude: ['@braze/web-sdk']
    }
}
```

### Framework Jest {#jest-framework}

Al usar Jest, es posible que veas un error similar a `SyntaxError: Unexpected token 'export'`. Para solucionarlo, ajusta tu configuración en `package.json` para ignorar el SDK de Braze:

``` json
{
  "jest": {
    "transformIgnorePatterns": [
      "/node_modules/(?!@braze)"
    ]
  }
}
```

### Definición de módulo asíncrono (AMD) {#asynchronous-module-definition-amd}

#### Deshabilitar la compatibilidad con AMD {#disable-amd-support}

Si tu sitio utiliza RequireJS u otro cargador de módulos AMD, pero prefieres cargar el SDK web de Braze a través del CDN, puedes cargar una versión de la biblioteca que no incluye compatibilidad con AMD. Esta versión de la biblioteca se puede cargar desde la ubicación del CDN: `https://js.appboycdn.com/web-sdk/6.3/braze.no-amd.min.js`

#### Cargador de módulos {#module-loader}

Si utilizas RequireJS u otros cargadores de módulos AMD, te recomendamos alojar una copia de nuestra biblioteca y referenciarla como lo harías con otros recursos:

``` javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Páginas móviles aceleradas (AMP) {#accelerated-mobile-pages-amp}

Para la integración con AMP, necesitarás:

1. **Incluir el script de push web de AMP**: añade la etiqueta de script asíncrono a tu head
2. **Añadir widgets de suscripción**: añade widgets para permitir que los usuarios se suscriban o cancelen su suscripción
3. **Añadir archivos auxiliares**: incluye `helper-iframe.html` y `permission-dialog.html`
4. **Crear un service worker**: añade el archivo de service worker de Braze
5. **Configurar el elemento de push web de AMP**: añade el elemento `amp-web-push` con tu clave de API y URL base como parámetros de consulta

Para instrucciones detalladas de integración con AMP, consulta la [Guía para desarrolladores de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web#amp).

### Electron

Electron no es compatible oficialmente con las notificaciones push web (consulta: este [issue de GitHub](https://github.com/electron/electron/issues/6697)). Existen otras [soluciones alternativas de código abierto](https://github.com/MatthieuLemoine/electron-push-receiver) que puedes probar y que no han sido probadas por Braze.

### Integración por CDN {#cdn-integration}

- **Carga de scripts**: inicializa después de que se cargue la etiqueta de script colocando el código de inicialización después de la etiqueta de script, o utiliza el controlador de eventos `onload` de la etiqueta de script
- **Acceso global**: el SDK está disponible como `window.braze` cuando se carga a través del CDN

### Service worker (notificaciones push) {#service-worker-push-notifications}

- **Obligatorio**: debes incluir el service worker de Braze para que las notificaciones push funcionen
- **Registro predeterminado**: de forma predeterminada, el SDK web de Braze registra y gestiona tu service worker automáticamente cuando se llama a `requestPushPermission()`, así como al inicio de cada nueva sesión para los usuarios que ya han concedido permiso de push. Aún necesitas alojar un archivo de service worker en la ubicación esperada que contenga el código del service worker de Braze.
- **Gestionar tu propio service worker**: si ya gestionas un service worker en tu aplicación, establece la opción de inicialización `manageServiceWorkerExternally` en `true`, añade el código del service worker de Braze a tu archivo de service worker y regístralo tú mismo usando `navigator.serviceWorker.register()`
- **Permisos de push**: llama a `braze.requestPushPermission()` en respuesta a interacciones del usuario (por ejemplo, clics en botones). Utiliza indicaciones de push suaves (interfaz personalizada) antes de solicitar el permiso del navegador

### Gestores de etiquetas {#tag-managers}

#### Tealium iQ

Tealium iQ ofrece una integración básica llave en mano con Braze. Para configurar la integración, busca Braze en la interfaz de gestión de etiquetas de Tealium y proporciona la clave de API del SDK web desde tu panel. Para más detalles o soporte de configuración avanzada de Tealium, consulta nuestra [documentación de integración](https://www.braze.com/docs/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) o ponte en contacto con tu director de cuentas de Tealium.

#### Google Tag Manager

El SDK web puede inicializarse y llamarse desde una etiqueta HTML personalizada en tu contenedor de Google Tag Manager. Consulta nuestra [aplicación de ejemplo de Google Tag Manager](https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/google-tag-manager) para ver un ejemplo de envío de eventos a Braze a través de GTM, o consulta nuestra [documentación de integración](https://www.braze.com/docs/developer_guide/sdk_integration/google_tag_manager) para más detalles.

#### Otros gestores de etiquetas {#other-tag-managers}

Braze también puede ser compatible con otras soluciones de gestión de etiquetas siguiendo nuestras instrucciones de integración dentro de una etiqueta HTML personalizada. Ponte en contacto con un representante de Braze si necesitas ayuda para evaluar estas soluciones.

---

## Bibliotecas {#libraries}

La siguiente tabla describe las distribuciones disponibles del SDK web de Braze.

| Nombre | Descripción | npm | URL del CDN |
| ---- | ----------- | --- | ------- |
| Full | SDK completo con interfaz de usuario. Al usar la versión npm, los empaquetadores de JavaScript eliminan el código no utilizado, incluido el código de la interfaz de usuario. | `@braze/web-sdk` | https://js.appboycdn.com/web-sdk/6.10/braze.min.js |
| Core | Contiene el SDK sin interfaz de usuario. Implementa tu propia interfaz de usuario para In-App Messages y Content Cards al usar esta versión del SDK. Utiliza la biblioteca completa para la mayoría de las integraciones, ya que proporciona elementos de interfaz de usuario personalizables a través de CSS. | N/A | https://js.appboycdn.com/web-sdk/6.10/braze.core.min.js |
| No-AMD | Contiene el SDK completo sin compatibilidad con AMD. Esto es útil si tu sitio utiliza RequireJS u otro cargador de módulos AMD, pero prefieres cargar el SDK a través del CDN. | N/A | https://js.appboycdn.com/web-sdk/6.10/braze.no-amd.min.js |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Bibliotecas" }

## Navegadores compatibles {#supported-browsers}

- Navegadores modernos basados en Chromium (Chrome, Edge, Opera)
- Firefox
- Safari

## Depuración y solución de problemas {#debugging-troubleshooting}

Pasa la opción `enableLogging: true` a la función de inicialización (`braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT', enableLogging: true });`) para que Braze registre en la consola de JavaScript. Esto es valioso para el desarrollo, pero es visible para todos los usuarios, así que elimina esta opción o [proporciona un registrador alternativo](https://js.appboycdn.com/web-sdk/6.10/doc/modules/braze.html#setlogger) antes de publicar tu página en producción.

## Font Awesome

Braze utiliza [Font Awesome](http://fortawesome.github.io/Font-Awesome/) 4.7.0 para los iconos de los mensajes dentro de la aplicación. Para deshabilitar la carga de Font Awesome, utiliza la opción de inicialización `doNotLoadFontAwesome`. Consulta la [hoja de referencia](http://fortawesome.github.io/Font-Awesome/cheatsheet/) para explorar los iconos disponibles.

## Recursos adicionales {#additional-resources}

- [Guía para desarrolladores de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web)
- [Documentación del SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)
- [Compilaciones de ejemplo](https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/)

## Contacto {#contact}

Si tienes preguntas, ponte en contacto con el soporte técnico de Braze para obtener asistencia.
<!-- END GENERATED README CONTENT -->

Para detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-web-sdk](https://github.com/braze-inc/braze-web-sdk).