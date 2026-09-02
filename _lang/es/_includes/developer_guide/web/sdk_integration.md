## Acerca del SDK or kit de desarrollo de software Web de Braze {#about-the-web-braze-sdk}

El SDK or kit de desarrollo de software Web de Braze te permite recopilar análisis y mostrar mensajes enriquecidos dentro de la aplicación, push y Content Cards a tus usuarios web. Para obtener más información, consulta la [documentación de referencia de JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% multi_lang_include archive/web-v4-rename.md %}

## Integrar el SDK or kit de desarrollo de software Web {#integrate-the-web-sdk}

Puedes integrar el SDK or kit de desarrollo de software Web de Braze utilizando los siguientes métodos. Para opciones adicionales, consulta [otros métodos de integración](#web_other-integration-methods).

- **Integración basada en código:** Integra el SDK or kit de desarrollo de software Web de Braze directamente en tu base de código utilizando tu gestor de paquetes preferido o la CDN de Braze. Esto te da control total sobre cómo se carga y configura el SDK or kit de desarrollo de software.
- **Google Tag Administrador:** Una solución sin código que te permite integrar el SDK or kit de desarrollo de software Web de Braze sin modificar el código de tu sitio. Para más información, consulta [Google Tag Administrador con el SDK or kit de desarrollo de software de Braze]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager).

{% alert important %}
Recomendamos utilizar el [método de integración NPM]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web). Sus ventajas incluyen almacenar las bibliotecas del SDK or kit de desarrollo de software localmente en tu sitio web, proporcionar inmunidad frente a extensiones de bloqueo de anuncios y contribuir a tiempos de carga más rápidos como parte del soporte de bundlers.
{% endalert %}

{% tabs local %}
{% tab integración basada en código %}
### Paso 1: Instala la biblioteca de Braze {#step-1-install-the-braze-library}

Puedes instalar la biblioteca de Braze utilizando uno de los siguientes métodos. Sin embargo, si tu sitio web utiliza una `Content-Security-Policy`, revisa la [Política de seguridad de contenido]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy) antes de continuar.

{% alert important %}
Aunque la mayoría de los bloqueadores de anuncios no bloquean el SDK or kit de desarrollo de software Web de Braze, algunos bloqueadores más restrictivos pueden causar problemas.
{% endalert %}

{% subtabs %}
{% subtab package Administrador %}
Si tu sitio utiliza los gestores de paquetes NPM o Yarn, puedes añadir el [paquete NPM de Braze](https://www.npmjs.com/package/@braze/web-sdk) como dependencia.

Las definiciones de Typescript se incluyen a partir de la versión v3.0.0. Para notas sobre la actualización de 2.x a 3.x, consulta nuestro [registro de cambios](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

Una vez instalado, puedes hacer `import` o `require` de la biblioteca de la forma habitual:

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endsubtab %}

{% subtab braze cdn %}
Añade el SDK or kit de desarrollo de software Web de Braze directamente a tu HTML haciendo referencia a nuestro script alojado en la CDN, que carga la biblioteca de forma asíncrona.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-SDK or kit de desarrollo de software%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
La configuración predeterminada **Prevenir seguimiento entre sitios** en Safari puede impedir que los tipos de mensajes dentro de la aplicación como Banners y Content Cards se muestren cuando utilizas el método de integración CDN. Para evitar este problema, utiliza el método de integración NPM para que Safari no clasifique estos mensajes como tráfico entre sitios y tus usuarios web puedan verlos en todos los navegadores compatibles.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### Paso 2: Inicializa el SDK or kit de desarrollo de software {#step-2-initialize-the-sdk}

Después de añadir el SDK or kit de desarrollo de software Web de Braze a tu sitio web, inicializa la biblioteca con la clave de API y la [URL del endpoint del SDK or kit de desarrollo de software]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) que se encuentran en **Configuración** > **Configuración de la aplicación** dentro de tu panel de Braze. Para una lista completa de opciones de `braze.initialize()`, junto con nuestros otros métodos JavaScript, consulta la [documentación JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

{% alert note %}
**Los dominios personalizados para solicitudes del SDK or kit de desarrollo de software Web no son compatibles**: El `baseUrl` del SDK or kit de desarrollo de software Web debe ser un endpoint del SDK or kit de desarrollo de software de Braze (por ejemplo, `sdk.iad-05.braze.com`). Braze no admite el enrutamiento del tráfico del SDK or kit de desarrollo de software Web a través de un dominio propio del cliente mediante registros CNAME. Si necesitas que las solicitudes del SDK or kit de desarrollo de software Web se originen desde tu propio dominio, contacta con soporte de Braze.
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
**Visualización de In-App Messages**: Para mostrar mensajes dentro de la aplicación automáticamente cuando se desencadenan, debes llamar a `braze.automaticallyShowInAppMessages()`. Sin esta llamada, los mensajes dentro de la aplicación no se muestran automáticamente. Si quieres gestionar la visualización de mensajes manualmente, elimina esta llamada y utiliza `braze.subscribeToInAppMessage()` en su lugar. Para más información, consulta [Desactivar desencadenadores automáticos]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#disabling-automatic-triggers).
{% endalert %}

#### Solución de problemas con sesiones faltantes para usuarios anónimos {#troubleshooting-missing-sessions-for-anonymous-users}

Si observas un comportamiento de "sesión faltante", o no puedes realizar un seguimiento de la sesión para usuarios que permanecen anónimos en la web, asegúrate de que tu integración llame a `braze.openSession()` durante la inicialización.

- **Escenario:** Los usuarios anónimos pueden devolver un ID de Braze, pero los datos de sesión están en blanco o faltan.
- **Causa:** La implementación no llama a `braze.openSession()`.
- **Resolución:** Llama siempre a `braze.openSession()` después de la inicialización (y después de `braze.changeUser()` si estableces un ID externo).

Para más información, consulta [Paso 2: Inicializa el SDK or kit de desarrollo de software]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web&tab=code-based%20integration#step-2-initialize-the-sdk).

{% alert important %}
Los usuarios anónimos en dispositivos móviles o web pueden contarse como parte de tus [MAU or usuarios activos al mes]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data#monthly-active-users). Como resultado, es posible que quieras cargar o inicializar el SDK or kit de desarrollo de software de forma condicional para excluir a estos usuarios de tu recuento de MAU or usuarios activos al mes.
{% endalert %}
{% endtab %}

{% tab Google Tag Administrador %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## Filtrado del tráfico de bots {#bot-filtering}

Los MAU or usuarios activos al mes pueden incluir un porcentaje de usuarios bot, lo que infla tu recuento de MAU or usuarios activos al mes or usuarios activos al mes. Aunque el SDK or kit de desarrollo de software Web de Braze incluye detección integrada para algunos rastreadores web comunes (como los bots de motores de búsqueda y los bots de vista previa de redes sociales), es especialmente importante mantenerse proactivo con soluciones robustas para detectar bots, ya que las actualizaciones del SDK or kit de desarrollo de software por sí solas no pueden detectar de forma consistente todos los bots nuevos.

### Limitaciones de la detección de bots por parte del SDK or kit de desarrollo de software {#limitations-of-sdk-side-bot-detection}

El SDK or kit de desarrollo de software Web incluye una detección básica de bots basada en agentes de usuario que filtra los rastreadores conocidos. Sin embargo, este enfoque tiene limitaciones:

- **Constantemente surgen nuevos bots**: Las empresas de IA y otros actores crean regularmente nuevos bots que pueden camuflarse para evitar ser detectados.
- **Suplantación de agente de usuario**: Los bots sofisticados pueden imitar los agentes de usuario legítimos de los navegadores.
- **Bots personalizados**: Los usuarios sin conocimientos técnicos ahora pueden crear fácilmente bots utilizando modelos de lenguaje grandes (LLM), lo que hace que el comportamiento de los bots sea impredecible.

### Implementación del filtrado de bots {#implementing-bot-filtering}

{% alert important %}
Las soluciones que se describen a continuación son sugerencias generales. Adapta la lógica para filtrar bots a tu entorno y patrones de tráfico únicos.
{% endalert %}

La solución más sólida es implementar tu propia lógica para filtrar bots antes de inicializar el SDK or kit de desarrollo de software de Braze. Los enfoques comunes incluyen:

#### Requerir interacción del usuario {#require-user-interaction}

Considera la posibilidad de retrasar la inicialización del SDK or kit de desarrollo de software hasta que el usuario realice una interacción significativa, como aceptar un banner de consentimiento de cookies, desplazarse por la página o hacer clic. Este enfoque suele ser más fácil de implementar y puede resultar muy eficaz para filtrar el tráfico de bots.

{% alert important %}
Retrasar la inicialización del SDK or kit de desarrollo de software hasta que se produzca la interacción del usuario puede provocar que los banners y las Content Cards tampoco se muestren hasta que se produzca dicha interacción.
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

- Analiza periódicamente tus datos de MAU or usuarios activos al mes y los patrones de tráfico web para identificar nuevos comportamientos de bots.
- Realiza pruebas exhaustivas para asegurarte de que tu filtro de bots no impida el seguimiento de usuarios legítimos.
- Actualiza tu lógica de filtrado basándote en los patrones de tráfico de bots que observes en tu entorno.

## Configuraciones opcionales {#optional-configurations}

### Registro {#logging}

Para habilitar rápidamente el registro, puedes añadir `?brazeLogging=true` como parámetro a la URL de tu sitio web. Alternativamente, puedes habilitar el registro [básico](#web_basic-logging) o [personalizado](#web_custom-logging). Para obtener un resumen centralizado en todas las plataformas, consulta [Registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

#### Registro básico {#basic-logging}

{% tabs local %}
{% tab antes de la inicialización %}
Usa `enableLogging` para registrar mensajes básicos de depuración en la consola de JavaScript antes de que se inicialice el SDK or kit de desarrollo de software.

```javascript
enableLogging: true
```

Tu método debería ser similar al siguiente:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab después de la inicialización %}
Usa `braze.toggleLogging()` para registrar mensajes básicos de depuración en la consola de JavaScript después de que se haya inicializado el SDK or kit de desarrollo de software. Tu método debería ser similar al siguiente:

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
Los registros básicos son visibles para todos los usuarios, así que considera deshabilitarlos o cambiar a [`setLogger`](#web_custom-logging) antes de liberar tu código a producción.
{% endalert %}

#### Registro personalizado {#custom-logging}

Usa `setLogger` para registrar mensajes de depuración personalizados en la consola de JavaScript. A diferencia de los registros básicos, estos registros no son visibles para los usuarios.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Reemplaza `STRING` con tu mensaje como un único parámetro de cadena. Tu método debería ser similar al siguiente:

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## Actualización del SDK or kit de desarrollo de software {#upgrading-the-sdk}

{% multi_lang_include archive/web-v4-rename.md %}

Cuando haces referencia al SDK or kit de desarrollo de software Web de Braze desde nuestra red de entrega de contenido, por ejemplo, `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (como recomiendan nuestras instrucciones de integración predeterminadas), tus usuarios reciben actualizaciones menores (correcciones de errores y características retrocompatibles, versiones `a.a.a` a `a.a.z` en este ejemplo) de forma automática cuando actualizan tu sitio.

Sin embargo, cuando publicamos cambios importantes, requerimos que actualices el SDK or kit de desarrollo de software Web de Braze de forma manual para garantizar que los cambios de ruptura no afecten tu integración. Además, si descargas nuestro SDK or kit de desarrollo de software y lo alojas tú mismo, no recibes ninguna actualización de versión de forma automática y debes actualizarlo manualmente para recibir las últimas características y correcciones de errores.

Puedes mantenerte al día con nuestra última versión [siguiendo nuestro feed de lanzamientos](https://github.com/braze-inc/braze-web-sdk/tags.atom) con el lector RSS o servicio de tu elección, y consultar [nuestro registro de cambios](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) para ver un recuento completo del historial de versiones de nuestro SDK or kit de desarrollo de software Web. Para actualizar el SDK or kit de desarrollo de software Web de Braze:

- Actualiza la versión de la biblioteca de Braze cambiando el número de versión de `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js`, o en las dependencias de tu gestor de paquetes.
- Si tienes notificación push web integrada, actualiza el archivo del prestador de servicios en tu sitio; de forma predeterminada, se encuentra en `/service-worker.js` en el directorio raíz de tu sitio, pero la ubicación puede estar personalizada en algunas integraciones. Debes acceder al directorio raíz para alojar un archivo de prestador de servicios.

Debes actualizar estos dos archivos de forma coordinada para asegurar un funcionamiento correcto.

## Otros métodos de integración {#other-integration-methods}

### Páginas móviles aceleradas (páginas móviles aceleradas) {#accelerated-mobile-pages-amp}
{% details Ver más %}
#### Paso 1: Incluir el script de web push de páginas móviles aceleradas {#step-1-include-amp-web-push-script}

Añade la siguiente etiqueta de script asíncrono a tu encabezado:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### Paso 2: Añadir widgets de suscripción {#step-2-add-subscription-widgets}

Añade un widget al cuerpo de tu HTML que permita a los usuarios suscribirse y cancelar la suscripción a push.

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

El componente páginas móviles aceleradas Web Push crea un popup para gestionar las suscripciones push, por lo que debes añadir los siguientes archivos auxiliares a tu proyecto para habilitar esta característica:

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### Paso 4: Crear un archivo de prestador de servicios {#step-4-create-a-service-worker-file}

Crea un archivo `service-worker.js` en el directorio raíz de tu sitio web y añade el siguiente fragmento de código:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Paso 5: Configurar el elemento HTML de páginas móviles aceleradas web push {#step-5-configure-the-amp-web-push-html-element}

Añade el siguiente elemento HTML `amp-web-push` al cuerpo de tu HTML. Ten en cuenta que necesitas agregar tu [`apiKey` y `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) como parámetros de consulta a `service-worker-URL`.

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

### Definición de módulos asíncronos (AMD) {#asynchronous-module-definition-amd}

#### Desactivar la compatibilidad {#disable-support}

Si tu sitio utiliza RequireJS u otro cargador de módulos AMD, pero prefieres cargar el SDK or kit de desarrollo de software Web de Braze a través de una de las otras opciones de esta lista, puedes cargar una versión de la biblioteca que no incluye compatibilidad con AMD. Esta versión de la biblioteca se puede cargar desde la siguiente ubicación CDN:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-SDK or kit de desarrollo de software%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Cargador de módulos {#module-loader}

Si usas RequireJS u otros cargadores de módulos AMD, te recomendamos alojar una copia de nuestra biblioteca y referenciarla como lo harías con otros recursos:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electron {#electron}

Electron no admite oficialmente las notificaciones push web (consulta este [issue en GitHub](https://github.com/electron/electron/issues/6697)). Hay otras [soluciones alternativas de código abierto](https://github.com/MatthieuLemoine/electron-push-receiver) que puedes probar, aunque no han sido verificadas por Braze.

### Framework Jest {#jest}

Al usar Jest, es posible que veas un error similar a `SyntaxError: Unexpected token 'export'`. Para solucionarlo, ajusta tu configuración en `package.json` para ignorar el SDK or kit de desarrollo de software de Braze:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### Frameworks SSR {#ssr}

El SDK or kit de desarrollo de software Web se ejecuta en un entorno de navegador. En frameworks SSR, inicializa Braze en un componente exclusivo del cliente para que tu servidor nunca ejecute código del SDK or kit de desarrollo de software.

#### Importación dinámica agnóstica al framework {#framework-agnostic-dynamic-import}

Si tu framework no aparece en esta sección, puedes importar Braze dinámicamente desde un hook del ciclo de vida exclusivo del cliente.

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

Si usas webpack, puedes importar dinámicamente solo exportaciones específicas del SDK or kit de desarrollo de software.

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

Llama a `useBraze` en un componente cliente que envuelva tu aplicación.

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

Para ejemplos de validación local de Remix, ejecuta `PORT=4013 npm run dev`.

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

Después de que `useBraze` inicialice el SDK or kit de desarrollo de software en la raíz de tu aplicación, otros componentes cliente pueden llamar a los métodos de Braze. Un patrón común es llamarlos dentro de acciones del usuario, como `onClick` o `onSubmit`. En el ejemplo, los métodos del SDK or kit de desarrollo de software se cargan dentro del controlador de clic en lugar de en la parte superior del archivo. Esto mantiene el SDK or kit de desarrollo de software Web fuera del código del servidor y carga solo lo que esa acción necesita. El comentario `webpackExports` le indica a webpack qué métodos incluir, para que tu bundle se mantenga más pequeño.

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

Este ejemplo muestra un componente `BuyButton` que registra actividad cuando alguien hace clic en **Comprar**. Primero, importa solo `logCustomEvent`, `logPurchase` y `getUser` en el momento del clic. Luego actualiza un atributo de usuario, registra un evento personalizado y registra una compra. Este patrón te ayuda a mantener la inicialización centralizada en `useBraze`, mientras sigues rastreando acciones significativas desde cualquier componente cliente.

Si usas Remix con Vite y las importaciones desde la raíz del paquete fallan en tiempo de ejecución, usa la solución alternativa existente de Vite. Para más información, consulta [Vite]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_vite).

Para una lista completa de los métodos disponibles, consulta la [documentación de referencia de JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

### Tealium iQ

Tealium iQ ofrece una integración básica de Braze lista para usar. Para configurar la integración, busca Braze en la interfaz de Tealium Tag Management y proporciona la clave de API del SDK or kit de desarrollo de software Web desde tu panel.

Para más detalles o asistencia en profundidad sobre la configuración de Tealium, consulta nuestra [documentación de integración]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium#about-tealium) o contacta con tu director de cuentas de Tealium.

### Vite {#vite}

Si usas Vite y ves una advertencia sobre dependencias circulares o `Uncaught TypeError: Class extends value undefined is not a constructor or null`, es posible que necesites excluir el SDK or kit de desarrollo de software de Braze de su [descubrimiento de dependencias](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior):

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Otros gestores de etiquetas {#other-tag-managers}

Braze también puede ser compatible con otras soluciones de gestión de etiquetas siguiendo nuestras instrucciones de integración dentro de una etiqueta HTML personalizada. Contacta con un representante de Braze si necesitas ayuda para evaluar estas soluciones.