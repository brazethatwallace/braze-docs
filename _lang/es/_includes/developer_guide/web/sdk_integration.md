## Acerca del SDK Web de Braze {#about-the-web-braze-sdk}

El SDK Web de Braze te permite recopilar datos de análisis y mostrar mensajes enriquecidos dentro de la aplicación, mensajes push y mensajes de Content Cards a tus usuarios web. Para obtener más información, consulta [la documentación de referencia de Braze JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% multi_lang_include archive/web-v4-rename.md %}

## Integrar el SDK Web {#integrate-the-web-sdk}

Puedes integrar el SDK Web de Braze utilizando los siguientes métodos. Para ver opciones adicionales, consulta [otros métodos de integración](#web_other-integration-methods).

- **Integración basada en código:** Integra el SDK Web de Braze directamente en tu código base utilizando tu administrador de paquetes preferido o el CDN de Braze. Esto te permite controlar totalmente cómo se carga y configura el SDK.
- **Google Tag Manager:** Una solución sin código que te permite integrar el SDK Web de Braze sin modificar el código de tu sitio web. Para obtener más información, consulta [Google Tag Manager con el SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager).

{% alert important %}
Recomendamos utilizar el [método de integración NPM]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web). Las ventajas incluyen el almacenamiento local de las bibliotecas del SDK en tu sitio web, la inmunidad frente a las extensiones de bloqueo de anuncios y la contribución a tiempos de carga más rápidos como parte de la compatibilidad con el empaquetador.
{% endalert %}

{% tabs local %}
{% tab code-based integration %}
### Paso 1: Instala la biblioteca Braze {#step-1-install-the-braze-library}

Puedes instalar la biblioteca Braze utilizando uno de los siguientes métodos. Sin embargo, si tu sitio web utiliza un `Content-Security-Policy`, revisa la [Política de seguridad de contenidos]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy) antes de continuar.

{% alert important %}
Aunque la mayoría de los bloqueadores de anuncios no bloquean el SDK Web de Braze, se sabe que algunos bloqueadores de anuncios más restrictivos causan problemas.
{% endalert %}

{% subtabs %}
{% subtab package manager %}
Si tu sitio utiliza los administradores de paquetes NPM o Yarn, puedes añadir el [paquete NPM de Braze](https://www.npmjs.com/package/@braze/web-sdk) como dependencia.

A partir de la versión 3.0.0, se incluyen definiciones de Typescript. Para obtener notas sobre la actualización de 2.x a 3.x, consulta nuestro [registro de cambios](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

Una vez instalado, puedes `import` o `require` la biblioteca de la forma típica:

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endsubtab %}

{% subtab braze cdn %}
Añade el SDK Web de Braze directamente a tu HTML haciendo referencia a nuestro script alojado en CDN, que carga la biblioteca de forma asíncrona.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
La configuración predeterminada **Prevenir el seguimiento entre sitios** en Safari puede impedir que se muestren tipos de mensajes dentro de la aplicación, como banners y Content Cards, cuando utilizas el método de integración CDN. Para evitar este problema, utiliza el método de integración NPM, de modo que Safari no clasifique estos mensajes como tráfico entre sitios y tus usuarios web puedan verlos en todos los navegadores compatibles.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### Paso 2: Inicializar el SDK {#step-2-initialize-the-sdk}

Una vez añadido el SDK Web de Braze a tu sitio web, inicializa la biblioteca con la clave de API y [la URL del endpoint del SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) que se encuentran en **Configuración** > **Configuración de la aplicación** dentro de tu panel de Braze. Para obtener una lista completa de opciones para `braze.initialize()`, junto con nuestros otros métodos JavaScript, consulta [la documentación de Braze JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

{% alert note %}
**No se admiten dominios personalizados para solicitudes del SDK Web**: El `baseUrl` del SDK Web debe ser un endpoint del SDK de Braze (por ejemplo, `sdk.iad-05.braze.com`). Braze no admite el enrutamiento del tráfico del SDK Web a través de un dominio propiedad del cliente mediante registros CNAME. Si necesitas que las solicitudes del SDK Web se originen desde tu propio dominio, ponte en contacto con el soporte de Braze.
{% endalert %}

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
    enableLogging: false, // set to `true` for debugging
    allowUserSuppliedJavascript: false, // set to `true` to support custom HTML messages
});

// Enable automatic display of in-app messages
// Required if you want in-app messages to display automatically when triggered
braze.automaticallyShowInAppMessages();

// if you use Content Cards
braze.subscribeToContentCardsUpdates(function(cards){
    // cards have been updated
});

// optionally set the current user's external ID before starting a new session
// you can also call `changeUser` later in the session after the user logs in
if (isLoggedIn){
    braze.changeUser(userIdentifier);
}

// `openSession` should be called last - after `changeUser` and `automaticallyShowInAppMessages`
braze.openSession();
```

{% alert important %}
**Visualización de mensajes dentro de la aplicación**: Para mostrar automáticamente los mensajes dentro de la aplicación cuando se desencadenan, debes llamar a `braze.automaticallyShowInAppMessages()`. Sin esta llamada, los mensajes dentro de la aplicación no se muestran automáticamente. Si deseas administrar manualmente la visualización de mensajes, elimina esta llamada y utiliza `braze.subscribeToInAppMessage()` en su lugar. Para obtener más información, consulta [Desactivar desencadenantes automáticos]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#disabling-automatic-triggers).
{% endalert %}

#### Solución de problemas relacionados con sesiones perdidas para usuarios anónimos {#troubleshooting-missing-sessions-for-anonymous-users}

Si observas un comportamiento de «sesión perdida» o no puedes realizar el seguimiento de la sesión de los usuarios anónimos en la web, asegúrate de que tu integración llama a `braze.openSession()` durante la inicialización.

- **Escenario:** Los usuarios anónimos pueden devolver un ID de Braze, pero los datos de la sesión están en blanco o faltan.
- **Causa:** La implementación no llama a `braze.openSession()`.
- **Resolución:** Siempre llama a `braze.openSession()` después de la inicialización (y después de `braze.changeUser()` si estableces un ID externo).

Para obtener más información, consulta [el Paso 2: Inicializa el SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web&tab=code-based%20integration#step-2-initialize-the-sdk).

{% alert important %}
Los usuarios anónimos en dispositivos móviles o web pueden contabilizarse en tu [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data#monthly-active-users). Como resultado, puede que quieras cargar o inicializar condicionalmente el SDK para excluir a estos usuarios de tu recuento de MAU.
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## Filtrado del tráfico de bots {#bot-filtering}

Los MAU pueden incluir un porcentaje de usuarios bot, lo que infla tu recuento de usuarios activos al mes. Aunque el SDK Web de Braze incluye detección integrada para algunos rastreadores web comunes (como los bots de motores de búsqueda y los bots de vista previa de redes sociales), es especialmente importante mantenerse proactivo con soluciones robustas para detectar bots, ya que las actualizaciones del SDK por sí solas no pueden detectar de forma consistente todos los bots nuevos.

### Limitaciones de la detección de bots por parte del SDK {#limitations-of-sdk-side-bot-detection}

El SDK Web incluye una detección básica de bots basada en agentes de usuario que filtra los rastreadores conocidos. Sin embargo, este enfoque tiene limitaciones:

- **Constantemente surgen nuevos bots**: Las empresas de IA y otros actores crean regularmente nuevos bots que pueden camuflarse para evitar ser detectados.
- **Suplantación de agente de usuario**: Los bots sofisticados pueden imitar los agentes de usuario legítimos de los navegadores.
- **Bots personalizados**: Los usuarios sin conocimientos técnicos ahora pueden crear fácilmente bots utilizando modelos de lenguaje grandes (LLM), lo que hace que el comportamiento de los bots sea impredecible.

### Implementación del filtrado de bots {#implementing-bot-filtering}

{% alert important %}
Las soluciones que se describen a continuación son sugerencias generales. Adapta la lógica para filtrar bots a tu entorno y patrones de tráfico únicos.
{% endalert %}

La solución más sólida es implementar tu propia lógica para filtrar bots antes de inicializar el SDK de Braze. Los enfoques comunes incluyen:

#### Requerir interacción del usuario {#require-user-interaction}

Considera la posibilidad de retrasar la inicialización del SDK hasta que el usuario realice una interacción significativa, como aceptar un banner de consentimiento de cookies, desplazarse por la página o hacer clic. Este enfoque suele ser más fácil de implementar y puede resultar muy eficaz para filtrar el tráfico de bots.

{% alert important %}
Retrasar la inicialización del SDK hasta que se produzca la interacción del usuario puede provocar que los banners y las Content Cards tampoco se muestren hasta que se produzca dicha interacción.
{% endalert %}

#### Detección personalizada de bots {#custom-bot-detection}

Implementa una detección personalizada basada en tus patrones específicos de tráfico de bots, tales como:

- Analizar las cadenas de agente de usuario en busca de patrones que hayas identificado en tu tráfico
- Comprobación de indicadores de navegador sin interfaz gráfica
- Uso de servicios de detección de bots de terceros
- Supervisión de señales de comportamiento específicas de tu sitio web

**Ejemplo de inicialización condicional:**

```javascript
// Only initialize Braze if your custom bot detection determines this is not a bot
if (!isLikelyBot()) {
  braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE"
  });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
}
```

### Buenas prácticas {#best-practices}

- Analiza periódicamente tus datos de MAU y los patrones de tráfico web para identificar nuevos comportamientos de bots.
- Realiza pruebas exhaustivas para asegurarte de que tu filtro de bots no impida el seguimiento de usuarios legítimos.
- Actualiza tu lógica de filtrado basándote en los patrones de tráfico de bots que observes en tu entorno.

## Configuraciones opcionales {#optional-configurations}

### Registro {#logging}

Para habilitar rápidamente el registro, puedes añadir `?brazeLogging=true` como parámetro a la URL de tu sitio web. También puedes habilitar el registro [básico](#web_basic-logging) o [personalizado](#web_custom-logging). Para obtener un resumen centralizado de todas las plataformas, consulta [Registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

#### Registro básico {#basic-logging}

{% tabs local %}
{% tab before initialization %}
Utiliza `enableLogging` para registrar mensajes básicos de depuración en la consola de JavaScript antes de que se inicialice el SDK.

```javascript
enableLogging: true
```

Tu método debe ser similar al siguiente:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab after initialization %}
Utiliza `braze.toggleLogging()` para registrar mensajes básicos de depuración en la consola de JavaScript después de inicializar el SDK. Tu método debe ser similar al siguiente:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
});
braze.openSession();
...
braze.toggleLogging();
```
{% endtab %}
{% endtabs %}

{% alert important %}
Los registros básicos son visibles para todos los usuarios, así que considera desactivarlos o cambia a [`setLogger`](#web_custom-logging) antes de poner tu código en producción.
{% endalert %}

#### Registro personalizado {#custom-logging}

Utiliza `setLogger` para registrar mensajes de depuración personalizados en la consola de JavaScript. A diferencia de los registros básicos, estos registros no son visibles para los usuarios.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Sustituye `STRING` por tu mensaje como parámetro de una sola cadena. Tu método debe ser similar al siguiente:

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## Actualizar el SDK {#upgrading-the-sdk}

{% multi_lang_include archive/web-v4-rename.md %}

Cuando haces referencia al SDK Web de Braze desde nuestra red de entrega de contenidos, por ejemplo, `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (tal y como recomiendan nuestras instrucciones de integración predeterminadas), tus usuarios reciben actualizaciones menores (correcciones de errores y características compatibles con versiones anteriores, versiones `a.a.a` hasta `a.a.z` en este ejemplo) automáticamente cuando actualizan tu sitio.

Sin embargo, cuando lanzamos cambios importantes, es necesario que actualices manualmente el SDK Web de Braze para garantizar que los cambios significativos no afecten a tu integración. Además, si descargas nuestro SDK y lo alojas tú mismo, no recibirás ninguna actualización de versión automáticamente y deberás actualizarlo manualmente para disfrutar de las últimas características y correcciones de errores.

Puedes mantenerte al día de nuestra última versión [siguiendo nuestra fuente de versiones](https://github.com/braze-inc/braze-web-sdk/tags.atom) con el lector RSS o el servicio que prefieras, y consultar [nuestro registro de cambios](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) para conocer el historial completo de versiones de nuestro SDK Web. Para actualizar el SDK Web de Braze:

- Actualiza la versión de la biblioteca Braze cambiando el número de versión de `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js`, o en las dependencias de tu administrador de paquetes.
- Si tienes integrado el push web, actualiza el archivo del prestador de servicios en tu sitio: por defecto, se encuentra en `/service-worker.js`, en el directorio raíz de tu sitio, pero la ubicación puede estar personalizada en algunas integraciones. Debes acceder al directorio raíz para alojar un archivo de prestador de servicios.

Debes actualizar estos dos archivos de forma coordinada para que funcionen correctamente.

## Otros métodos de integración {#other-integration-methods}

### Páginas móviles aceleradas (AMP) {#accelerated-mobile-pages-amp}
{% details Ver más %}
#### Paso 1: Incluir el script de notificación push web AMP {#step-1-include-amp-web-push-script}

Añade la siguiente etiqueta de script asíncrono a tu cabecera:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### Paso 2: Añadir widgets de suscripción {#step-2-add-subscription-widgets}

Añade un widget al cuerpo de tu HTML que permita a los usuarios suscribirse y cancelar la suscripción a las notificaciones push.

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

#### Paso 3: Añadir `helper-iframe` y `permission-dialog` {#step-3-add-helper-iframe-and-permission-dialog}

El componente AMP de notificación push web crea una ventana emergente para gestionar las suscripciones push, por lo que debes añadir los siguientes archivos auxiliares a tu proyecto para habilitar esta característica:

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### Paso 4: Crear un archivo de prestador de servicios {#step-4-create-a-service-worker-file}

Crea un archivo `service-worker.js` en el directorio raíz de tu sitio web y añade el siguiente fragmento de código:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Paso 5: Configurar el elemento HTML de notificación push web de AMP {#step-5-configure-the-amp-web-push-html-element}

Añade el siguiente elemento HTML `amp-web-push` al cuerpo de tu HTML. Ten en cuenta que debes añadir tu [`apiKey` y `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) como parámetros de consulta a `service-worker-URL`.

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```
{% enddetails %}

### Definición de módulo asíncrono (AMD) {#asynchronous-module-definition-amd}

#### Desactivar soporte {#disable-support}

Si tu sitio utiliza RequireJS u otro cargador de módulos AMD, pero prefieres cargar el SDK Web de Braze a través de una de las otras opciones de esta lista, puedes cargar una versión de la biblioteca que no incluya compatibilidad con AMD. Esta versión de la biblioteca puede cargarse desde la siguiente ubicación CDN:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Cargador de módulos {#module-loader}

Si utilizas RequireJS u otros cargadores de módulos AMD, te recomendamos que autoalojes una copia de nuestra biblioteca y la referencies como harías con otros recursos:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electron {#electron}

Electron no admite oficialmente notificaciones push web (consulta esta [incidencia de GitHub](https://github.com/electron/electron/issues/6697)). Hay otras [soluciones de código abierto](https://github.com/MatthieuLemoine/electron-push-receiver) que puedes probar y que no han sido probadas por Braze.

### Marco Jest {#jest}

Al utilizar Jest, es posible que aparezca un error similar a `SyntaxError: Unexpected token 'export'`. Para solucionarlo, ajusta tu configuración en `package.json` para ignorar el SDK de Braze:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### Marcos SSR {#ssr}

El SDK Web se ejecuta en un entorno de navegador. En los marcos SSR, inicializa Braze en un componente exclusivo del cliente para que tu servidor nunca ejecute código del SDK.

#### Importación dinámica agnóstica del marco {#framework-agnostic-dynamic-import}

Si tu marco no aparece en esta sección, puedes importar dinámicamente Braze desde un hook de ciclo de vida exclusivo del cliente.

```javascript
// MyComponent/braze-exports.js
// Export the parts of the SDK that you need.
export { initialize, openSession } from "@braze/web-sdk";

// MyComponent/MyComponent.js
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

Si utilizas webpack, puedes importar dinámicamente solo las exportaciones específicas del SDK.

```javascript
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

#### Hook compartido para Next.js y Remix {#shared-hook-for-nextjs-and-remix}

Crea un hook reutilizable `useBraze` y llámalo cerca de la raíz de tu aplicación.

```tsx
// hooks/useBraze.ts
import { useEffect, useRef } from "react";

export function useBraze() {
  const didInit = useRef(false);

  useEffect(() => {
    if (didInit.current) {
      return;
    }
    didInit.current = true;

    import("@braze/web-sdk")
      .then((braze) => {
        const initialized = braze.initialize("YOUR-API-KEY-HERE", {
          // Use your Braze Web SDK endpoint, such as sdk.iad-01.braze.com.
          baseUrl: "YOUR-SDK-ENDPOINT",
          enableLogging: false,
        });
        if (!initialized) {
          return;
        }

        // Optional: Identify signed-in users before opening a session.
        // braze.changeUser("external-id");

        // Optional: Automatically display in-app messages.
        // braze.automaticallyShowInAppMessages();
        braze.openSession();
      })
      .catch((error) => {
        console.error("Unable to load Braze SDK:", error);
      });
  }, []);
}
```

#### Next.js (App Router)

Llama a `useBraze` en un componente de cliente que envuelva tu aplicación.

```tsx
// app/components/AppRoot.tsx
"use client";

import type { ReactNode } from "react";
import { useBraze } from "../hooks/useBraze";

export function AppRoot({ children }: { children: ReactNode }) {
  useBraze();
  return <>{children}</>;
}
```

```tsx
// app/layout.tsx
import type { ReactNode } from "react";
import { AppRoot } from "./components/AppRoot";

export default function RootLayout({
  children,
}: {
  children: ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <AppRoot>{children}</AppRoot>
      </body>
    </html>
  );
}
```

#### Next.js (Pages Router)

Llama a `useBraze` en la parte superior de tu componente de aplicación personalizado.

```tsx
// pages/_app.tsx
import type { AppProps } from "next/app";
import { useBraze } from "../hooks/useBraze";

export default function App({ Component, pageProps }: AppProps) {
  useBraze();

  return (
    <Component {...pageProps} />
  );
}
```

#### Remix

Llama a `useBraze` en la parte superior de tu componente de ruta raíz.

Para ver ejemplos de validación local de Remix, ejecuta `PORT=4013 npm run dev`.

```tsx
// app/root.tsx
import { Outlet } from "@remix-run/react";
import { useBraze } from "./hooks/useBraze";

export default function App() {
  useBraze();

  return <Outlet />;
}
```

#### Registro de eventos y actualización de usuarios {#logging-events-and-updating-users}

Después de que `useBraze` inicialice el SDK en la raíz de tu aplicación, otros componentes de cliente pueden llamar a los métodos de Braze. Un patrón común es llamarlos dentro de acciones del usuario, como `onClick` u `onSubmit`. En el ejemplo, los métodos del SDK se cargan dentro del controlador de clic en lugar de en la parte superior del archivo. Esto mantiene el SDK Web fuera del código del servidor y carga solo lo que esa acción necesita. El comentario `webpackExports` le indica a webpack qué métodos incluir, de modo que tu paquete se mantiene más pequeño.

```tsx
// app/components/BuyButton.tsx
"use client";

export function BuyButton() {
  const handleClick = async () => {
    const { logCustomEvent, logPurchase, getUser } = await import(
      /* webpackExports: ["logCustomEvent", "logPurchase", "getUser"] */
      "@braze/web-sdk"
    );

    getUser()?.setCustomUserAttribute("last_purchase_date", "2026-05-04");
    logCustomEvent("clicked_buy", { source: "product_page" });
    logPurchase("sku_123", 19.99, "USD");
  };

  return <button onClick={handleClick}>Buy</button>;
}
```

Este ejemplo muestra un componente `BuyButton` que registra actividad cuando alguien hace clic en **Buy**. Primero, importa solo `logCustomEvent`, `logPurchase` y `getUser` en el momento del clic. Luego actualiza un atributo de usuario, registra un evento personalizado y registra una compra. Este patrón te ayuda a mantener la inicialización centralizada en `useBraze`, mientras sigues rastreando acciones significativas desde cualquier componente de cliente.

Si utilizas Remix con Vite y las importaciones desde la raíz del paquete fallan en tiempo de ejecución, usa la solución alternativa existente de Vite. Para obtener más información, consulta [Vite]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_vite).

Para obtener una lista completa de los métodos disponibles, consulta la [documentación de referencia de Braze JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

### Tealium iQ

Tealium iQ ofrece una integración básica de Braze llave en mano. Para configurar la integración, busca Braze en la interfaz de gestión de etiquetas de Tealium y proporciona la clave de API del SDK Web desde tu panel.

Para obtener más detalles o asistencia detallada sobre la configuración de Tealium, consulta nuestra [documentación sobre integración]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium#about-tealium) o ponte en contacto con tu director de cuentas de Tealium.

### Vite {#vite}

Si utilizas Vite y ves una advertencia sobre dependencias circulares o `Uncaught TypeError: Class extends value undefined is not a constructor or null`, puede que necesites excluir el SDK de Braze de su [descubrimiento de dependencias](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior):

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Otros administradores de etiquetas {#other-tag-managers}

Braze también puede ser compatible con otras soluciones de administración de etiquetas siguiendo nuestras instrucciones de integración dentro de una etiqueta HTML personalizada. Ponte en contacto con un representante de Braze si necesitas ayuda para evaluar estas soluciones.