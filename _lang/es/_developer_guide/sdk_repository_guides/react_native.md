---
nav_title: SDK de React Native
article_title: Guía del repositorio del SDK de React Native
page_order: 7
description: "Referencia del README del SDK de React Native de Braze reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Acerca del SDK de React Native de Braze {#about-the-braze-react-native-sdk}

El SDK de React Native de Braze conecta tus aplicaciones iOS y Android con Braze: perfiles de usuario, superficies de mensajería, análisis y conmutadores de características. Envuelve los SDK nativos [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) y [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk) detrás de una API de JavaScript.

**La inicialización se controla desde JavaScript:** configuras los ajustes nativos (push, registro, delegados) en los recursos de Android y en el `AppDelegate` de iOS, y luego llamas a `Braze.initialize(apiKey, endpoint)` desde JavaScript para iniciar el SDK. Esto te da control total sobre cuándo se inicializa el SDK y con qué credenciales. Después de la inicialización, llama a otros métodos del SDK (por ejemplo, `changeUser`, `logCustomEvent`) según sea necesario.

### Qué puedes hacer {#what-you-can-do}

- **Gestión de usuarios**: identifica usuarios, establece campos de perfil, atributos personalizados, alias y grupos de suscripción
- **Mensajes dentro de la aplicación**: interfaz predeterminada de Braze o gestión personalizada mediante suscripciones y API de registro
- **Content Cards**: interfaz de fuente predeterminada, u obtén tarjetas y construye tu propia interfaz
- **Banners**: banners HTML basados en ubicación, incluyendo `BrazeBannerView`
- **Notificaciones push**: solicitudes de permiso, registro de tokens, listeners de carga útil (consulta las notas de plataforma a continuación)
- **Conmutadores de características**: actualizar, leer propiedades, registrar impresiones
- **Análisis**: eventos personalizados, compras, envío inmediato
- **Controles del SDK**: habilitar/deshabilitar el SDK, borrar datos locales, firmas de Autenticación SDK

## Requisitos previos {#prerequisites}

- **Cuenta de Braze** con clave de API de la aplicación y punto de conexión del SDK
- Entorno de desarrollo de **React Native** ([configuración del entorno de React Native](https://reactnative.dev/docs/set-up-your-environment))
- **iOS**: Xcode, CocoaPods (`cd ios && pod install`)
- **Android**: Android Studio / Gradle; complemento Kotlin Gradle según lo requiera tu plantilla de React Native
- **Push** (si se usa): configuración de FCM (Android) y APNs (iOS) según la [documentación de push]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/push_notifications)

Para la ubicación de las credenciales en el dashboard, sigue el [resumen de integración]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native).

## Instalación {#installation}

``` bash
npm install @braze/react-native-sdk
# or:
# yarn add @braze/react-native-sdk
```

---

## Inicio rápido {#quick-start}

Esta sección muestra la configuración mínima necesaria para inicializar el SDK de React Native de Braze.

1. Instala el paquete npm (arriba).
2. Completa la **configuración nativa** para Android e iOS (configuración, permisos, push si es necesario).
3. Inicializa el SDK desde JavaScript y comienza a usarlo:

``` typescript
import Braze from "@braze/react-native-sdk";

// Initialize the SDK — call early in your app lifecycle (e.g. in a useEffect).
// The API key and endpoint are passed from JavaScript; native configuration
// (push, logging, etc.) is applied automatically from your native setup.
Braze.initialize("<YOUR_API_KEY>", "<YOUR_SDK_ENDPOINT>");

Braze.changeUser("user-123");
Braze.logCustomEvent("button_clicked", { screen: "home" });
```

Los tipos de TypeScript se incluyen con el paquete (`src/index.d.ts` en GitHub).

Llamar a `Braze.initialize` de nuevo con credenciales diferentes destruye la instancia actual y la recrea, lo que permite la reinicialización a mitad de sesión.

---

## Configuración nativa {#native-setup}

> **Fuente de referencia:** Las pantallas paso a paso, los cambios de Gradle/CocoaPods y la lista completa de claves XML de Android están en la [guía para desarrolladores de React Native de Braze]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native). Los fragmentos a continuación son ejemplos mínimos.

### Android

- Añade el **complemento Kotlin Gradle** en tu `build.gradle` raíz si tu plantilla no lo incluye ya (las versiones dependen de tu versión de React Native).
- Añade un archivo de recursos `braze.xml` en `res/values` con tu configuración. Habilita la inicialización diferida para que el SDK espere a que se llame a `Braze.initialize()` desde JavaScript antes de iniciarse. Otros valores de configuración (push, tiempo de espera de sesión, etc.) se siguen leyendo de este archivo y se aplican en el momento de la inicialización.
- Asegúrate de que los permisos básicos como `INTERNET` y `ACCESS_NETWORK_STATE` estén en `AndroidManifest.xml`.
- Para push, completa la integración de FCM y cualquier indicador de ID de remitente / registro específico de Braze descrito en la documentación.

``` xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- Enable delayed initialization so the SDK starts when
       Braze.initialize() is called from JavaScript. -->
  <bool name="com_braze_enable_delayed_initialization">true</bool>

  <!-- Additional native configuration (applied at initialization time) -->
  <bool name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">YOUR_SENDER_ID</string>
</resources>
```

{% alert note %}
La clave de API y el punto de conexión ya no se configuran en `braze.xml` — se pasan desde JavaScript a través de `Braze.initialize(apiKey, endpoint)`.
{% endalert %}
### iOS

``` bash
cd ios && pod install
```

Usa `BrazeReactInitializer.configure` en tu `AppDelegate` para registrar la configuración nativa. Los closures que proporcionas se almacenan y se aplican más tarde cuando se llama a `Braze.initialize(apiKey, endpoint)` desde JavaScript.

``` swift
import BrazeKit
import braze_react_native_sdk

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    // Register native configuration for when JS calls Braze.initialize().
    BrazeReactInitializer.configure { config in
      config.logger.level = .info
      config.push.automation = true
    } postInitialization: { braze in
      AppDelegate.braze = braze
    }

    // ... React Native setup
    return true
  }
}
```

- **Closure `configure`**: recibe un `Braze.Configuration` y te permite establecer propiedades de configuración nativa (registro, push, sesiones, etc.). La clave de API y el punto de conexión se proporcionan desde JavaScript — no los configuras aquí.
- **Closure `postInitialization`** *(opcional)*: recibe la instancia activa de `Braze` después de su creación, para configuraciones que requieren la instancia (por ejemplo, almacenar una referencia, establecer delegados).

{% alert note %}
`BrazeReactInitializer.configure` es una API orientada a Swift que reemplaza el obsoleto `BrazeReactBridge.initBraze(_:)`. También resuelve un problema de resolución de tipos de Swift con `Braze.Configuration` en el puente de Objective-C.
{% endalert %}
---

## Referencia de configuración {#configuration-reference}

En React Native, **la configuración es nativa**: Android lee `res/values/braze.xml`, e iOS usa closures registrados a través de **`BrazeReactInitializer.configure`**. Ambos se aplican cuando se llama a `Braze.initialize(apiKey, endpoint)` desde JavaScript.

### Android (`braze.xml`)

Los valores predeterminados están en XML; [`BrazeConfig.Builder`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) puede anularlos al inicio. La lista autorizada de claves y tipos está en la [guía de integración del SDK de Android]({{site.baseurl}}/developer_guide/platforms/android/sdk_integration) y en [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) (cada propiedad de Kotlin corresponde a recursos documentados `com_braze_*`).

Entradas de uso común:

| Clave | Tipo de recurso | Descripción |
|-------|-----------------|-------------|
| `com_braze_enable_delayed_initialization` | `bool` | **Obligatoria.** Establece en `true` para que el SDK espere a `Braze.initialize()` desde JavaScript. |
| `com_braze_api_key` | `string` | No es necesaria cuando se usa `Braze.initialize()` desde JavaScript (las credenciales se pasan desde JS). Solo es obligatoria para la inicialización nativa heredada. |
| `com_braze_custom_endpoint` | `string` | No es necesaria cuando se usa `Braze.initialize()` desde JavaScript. Solo es obligatoria para la inicialización nativa heredada. |
| `com_braze_server_target` | `string` | Selector opcional de clúster / entorno (por ejemplo, algunas compilaciones internas o de staging). Prefiere `com_braze_custom_endpoint` para producción a menos que tu integración de Braze indique lo contrario. |
| `com_braze_firebase_cloud_messaging_registration_enabled` | `bool` | Cuando es `true`, Braze se registra para FCM (configuración típica de push). |
| `com_braze_firebase_cloud_messaging_sender_id` | `string` | ID de remitente de FCM cuando el registro automático está habilitado. |
| `com_braze_handle_push_deep_links_automatically` | `bool` | Permite que Braze abra vínculos profundos de push automáticamente. |
| `com_braze_trigger_action_minimum_time_interval_seconds` | `integer` | Segundos mínimos entre acciones desencadenantes de mensajes dentro de la aplicación. |
| **Otros** | *varios* | Claves adicionales no mostradas aquí (tiempo de espera de sesión, geovallas, ubicación, valores predeterminados de notificación, listas de dispositivos permitidos, inicialización diferida, Autenticación SDK, etc.). Consulta [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) y la [guía de integración del SDK de Android]({{site.baseurl}}/developer_guide/platforms/android/sdk_integration). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android (braze.xml)" }

### iOS (`Braze.Configuration`)

Establece las propiedades de configuración nativa en el closure `configure` pasado a `BrazeReactInitializer.configure`. El closure recibe una instancia de `Braze.Configuration` — la clave de API y el punto de conexión se establecen automáticamente desde la llamada a `Braze.initialize` en JavaScript. Detalles completos: [`Braze.Configuration`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) y tipos anidados **`api`**, **`push`**, **`logger`**, **`location`**.

| Área | Miembros (representativos) | Notas |
|------|----------------------------|-------|
| **Credenciales** | `api.key`, `api.endpoint` | Se establecen automáticamente desde `Braze.initialize(apiKey, endpoint)` en JavaScript. No los configures en el closure `configure`. |
| **Registro** | `logger.level` | El registro detallado es para desarrollo; reduce el ruido en producción. |
| **Push** | `push.automation`, `push.appGroup`, … | La automatización simplifica el registro; `appGroup` es necesario para Push Stories / extensiones cuando se usan. |
| **Mensajes dentro de la aplicación** | `triggerMinimumTimeInterval` | **30** segundos predeterminados entre desencadenantes. |
| **Sesiones** | `sessionTimeout` | Inactividad antes de una nueva sesión (consulta la documentación de sesiones de Braze). |
| **Privacidad / datos** | `api.trackingPropertyAllowList`, `devicePropertyAllowList`, `api.sdkAuthentication` | Alinea con el [manifiesto de privacidad]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest) y la configuración del producto de Autenticación SDK. |
| **Red** | `api.requestPolicy`, `api.flushInterval` | Política de reintentos de solicitudes y cadencia de envío. |
| **Suscripción push** | `optInWhenPushAuthorized` | Cuando es `true`, la suscripción puede pasar a opted-in después de que el usuario autorice las notificaciones. |
| **IAM y cambios de usuario** | `preventInAppMessageDisplayForDifferentUser` | Reduce los IAM no coincidentes si cambia el ID de usuario. |
| **Otros** | `forwardUniversalLinks`, `ephemeralEvents`, `useUUIDAsDeviceId`, … | Consulta la documentación de Swift para el comportamiento completo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOS (Braze.Configuration)" }

El puente de React Native establece **`api.sdkFlavor`** / metadatos del SDK específicos de React en la inicialización; no los anules a menos que la documentación de Braze te lo indique.

---

## API de JavaScript / TypeScript {#javascript-typescript-api}

La exportación predeterminada del paquete es la clase `Braze` con métodos **estáticos** (por ejemplo, `Braze.changeUser`, `Braze.logPurchase`). Las constantes como `Braze.Events`, `Braze.Genders` y `Braze.NotificationSubscriptionTypes` están adjuntas a la misma exportación.

---

## Características principales {#core-features}

### Gestión de usuarios {#user-management}

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.changeUser("user-123");
Braze.setEmail("user@example.com");
Braze.setCustomUserAttribute("plan", "premium");
Braze.addAlias("external_id", "marketing_id");
Braze.addToSubscriptionGroup("NEWSLETTER_GROUP_UUID");
```

**Autenticación SDK** opcional: pasa una firma como segundo argumento a `changeUser`, o llama a `Braze.setSdkAuthenticationSignature(signature)` cuando esté habilitada en el dashboard.

### Mensajes dentro de la aplicación {#in-app-messages}

- Con la **interfaz predeterminada de Braze**, sigue la [documentación de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=react%20native); normalmente **no** necesitas llamar a `subscribeToInAppMessage` solo para mostrar la interfaz predeterminada.
- Para gestión **personalizada**, suscríbete con `useBrazeUI: false`, y luego registra impresiones/clics según sea necesario:

``` typescript
Braze.subscribeToInAppMessage(false, (event) => {
  const msg = event.inAppMessage;
  // Render your own UI from msg.message, msg.buttons, etc.
  Braze.logInAppMessageImpression(msg);
});
```

### Content Cards

``` typescript
const cards = await Braze.getContentCards();
Braze.requestContentCardsRefresh();
Braze.launchContentCards(); // default Braze UI

Braze.logContentCardImpression(cardId);
Braze.logContentCardClicked(cardId);
```

Escucha las actualizaciones con `Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, ...)`.

### Banners

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.requestBannersRefresh(["homepage_banner"]);
const banner = await Braze.getBanner("homepage_banner");

// Or use the native Banner view:
// <Braze.BrazeBannerView placementID="homepage_banner" />
```

### Notificaciones push {#push-notifications}

``` typescript
Braze.requestPushPermission({
  alert: true,
  badge: true,
  sound: true,
});
// Token registration is usually handled natively; see docs for your setup.
Braze.registerPushToken(token);
```

- **`getInitialPushPayload`**: úsalo cuando la aplicación se abre desde una notificación para evitar condiciones de carrera con `Linking` de RN; requiere hooks nativos (`BrazeReactUtils` en iOS, `BrazeReactUtils.populateInitialPushPayloadFromIntent` en Android) como se describe en los comentarios de documentación de TypeScript y la aplicación de ejemplo.
- **`Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, ...)`** es **solo para Android** según los tipos públicos.

### Conmutadores de características {#feature-flags}

``` typescript
const flag = await Braze.getFeatureFlag("new_checkout");
if (flag?.enabled) {
  const rollout = flag.getNumberProperty("rollout_percentage") ?? 0;
}
Braze.refreshFeatureFlags();
Braze.logFeatureFlagImpression("new_checkout");
```

### Análisis y compras {#analytics-and-purchases}

``` typescript
Braze.logCustomEvent("purchase_completed", { sku: "sku-1" });
Braze.logPurchase("sku-1", "29.99", "USD", 1, { source: "cart" });
Braze.requestImmediateDataFlush();
```

Nota: `logPurchase` toma el **precio como cadena** (consulta los tipos).

### Gestión de datos y estado del SDK {#data-management-and-sdk-state}

**`changeUser`** solo le indica a Braze a qué ID de usuario atribuir la **nueva** actividad. **No** borra los datos del SDK almacenados en caché en el dispositivo. No existe una API separada de "cerrar sesión": si necesitas un cierre de sesión tradicional (borrar el estado local de Braze para que el perfil, los mensajes y los tokens almacenados en caché del usuario anterior desaparezcan de esta instalación), normalmente usas **`wipeData()`**. Esto es un restablecimiento local completo.

``` typescript
Braze.wipeData();
Braze.disableSDK();
Braze.enableSDK();
```

**`wipeData()`** — Borra los datos **locales** de Braze para esta instalación (estado de usuario/sesión/tarjeta en caché, asociación de token de push, etc.). Úsalo para comportamiento de **cierre de sesión** cuando no debes dejar el estado de Braze del usuario anterior en el dispositivo, además de restablecimientos de **"eliminar mis datos en este dispositivo"**, restablecimientos de **QA** sin reinstalar, o flujos estrictos de **privacidad**. **`changeUser`** por sí solo no realiza esa limpieza — solo establece qué ID de usuario recibe los **nuevos** eventos. En **iOS**, el comportamiento puede diferir de Android (por ejemplo, la interacción con el estado del SDK deshabilitado); consulta la documentación nativa de Braze si envías esto a producción.

**`disableSDK()`** — Detiene la operación del SDK (sin recopilación/reenvío según la configuración). Úsalo para alternar la **exclusión del usuario**, **modos restringidos** (cumplimiento, configuración para menores), o **depuración** sin eliminar la dependencia.

**`enableSDK()`** — Reactiva el SDK después de **`disableSDK()`**. En **iOS**, la reactivación puede **no** aplicarse hasta el **siguiente inicio de la aplicación**; verifica en la documentación de Braze Swift/iOS antes de depender de la reactivación inmediata.

---

## Eventos {#events}

Suscríbete con `Braze.addListener(event, callback)`. La llamada devuelve un objeto de suscripción; llama a **`.remove()`** en él para dejar de escuchar.

**Configurar un listener:**

``` typescript
import Braze from "@braze/react-native-sdk";

const subscription = Braze.addListener(
  Braze.Events.CONTENT_CARDS_UPDATED,
  (update) => {
    console.log("Content cards:", update.cards);
  }
);
```

**Eliminar el listener:**

``` typescript
subscription.remove();
```

En un componente de React, almacena la suscripción y llama a `.remove()` en tu limpieza (por ejemplo, el retorno de un `useEffect`):

``` typescript
useEffect(() => {
  const sub = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
    setCards(update.cards);
  });
  return () => sub.remove();
}, []);
```

| Constante de evento | Carga útil (resumen) |
|---------------------|----------------------|
| `Braze.Events.CONTENT_CARDS_UPDATED` | Últimas Content Cards |
| `Braze.Events.BANNER_CARDS_UPDATED` | Últimos banners |
| `Braze.Events.FEATURE_FLAGS_UPDATED` | Array de conmutadores de características |
| `Braze.Events.IN_APP_MESSAGE_RECEIVED` | Evento de mensaje dentro de la aplicación |
| `Braze.Events.SDK_AUTHENTICATION_ERROR` | Detalles de error de autenticación del SDK |
| `Braze.Events.PUSH_NOTIFICATION_EVENT` | Carga útil de push (**solo Android**) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos" }

---

## Notas de integración {#integration-notes}

- **Expo**: usa el [complemento Braze Expo](https://github.com/braze-inc/braze-expo-plugin) para evitar la configuración nativa manual cuando sea posible.
- **Nueva arquitectura / Turbo Modules**: compatible con versiones recientes del complemento; sigue la guía para desarrolladores y la configuración de ejemplo de `AppDelegate` / Gradle si migras.
- **Privacidad (iOS)**: métodos como `updateTrackingPropertyAllowList` admiten la configuración relacionada con el manifiesto de privacidad; consulta el [manifiesto de privacidad de Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest).
## - **Jest**: simula los módulos nativos de `react-native` o el Turbo module de Braze (consulta `__tests__/jest.setup.js` en este repositorio para ver patrones). {#jest-mock-react-native-native-modules-or-the-braze-turbo-module-see-__tests__jestsetupjs-in-this-repo-for-patterns}

## Compatibilidad de versiones {#version-support}

{% alert note %}
Este SDK ha sido probado con la versión **0.85.3** de React Native.
{% endalert %}
La siguiente tabla muestra las versiones de React Native compatibles por lanzamiento del complemento de Braze.

| Complemento de Braze | React Native | Nueva arquitectura |
|-----------------------|--------------|--------------------|
| 9.0.0+                | ≥ 0.71       | Sí                 |
| 6.0.0+                | ≥ 0.68       | Sí (≥ 0.70.0)      |
| 2.0.0+                | ≥ 0.68       | Sí                 |
| ≤ 1.41.0              | ≤ 0.71       | No                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Compatibilidad de versiones" }

Respeta también los requisitos de los SDK nativos:

- [Información de versión del SDK de Android](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
- [Información de versión del SDK de Swift](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

---

## Complemento Braze Expo {#braze-expo-plugin}

Para flujos de trabajo gestionados con Expo, consulta el [repositorio del complemento Braze Expo](https://github.com/braze-inc/braze-expo-plugin).

---

## Aplicación de ejemplo {#sample-app}

`BrazeProject` en este repositorio es un ejemplo completo (gestión de usuarios, Content Cards, conmutadores de características, banners, etc.).

``` bash
cd BrazeProject/
yarn install
npx react-native start
```

**iOS** (desde `BrazeProject`):

``` bash
cd ios && pod install && cd ..
npx react-native run-ios
```

Usa `RCT_NEW_ARCH_ENABLED=0 pod install` si necesitas la arquitectura heredada.

**Android** (desde `BrazeProject`):

``` bash
npx react-native run-android
```

---

## Depuración y solución de problemas {#debugging-and-troubleshooting}

Habilita el registro de Braze en la configuración **nativa** durante el desarrollo para que el SDK escriba en la consola del sistema (Xcode / Android Logcat). Esto ayuda a verificar la inicialización, los cambios de usuario y la entrega de eventos.

- **iOS** — En el closure `configure` pasado a `BrazeReactInitializer.configure`, establece `config.logger.level = .debug` (o `.info`). Reduce o deshabilita en producción para que los registros no sean visibles para los usuarios.
- **Android** — Usa el recurso `com_braze_logger_initial_log_level` en `braze.xml` o establece el equivalente en `BrazeConfig.Builder` (consulta [BrazeConfigurationProvider](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/logger-initial-log-level.html)). Usa un nivel no detallado o elimina la anulación antes del lanzamiento.

Para una solución de problemas más profunda (red, sesión o comportamiento de Campaign), consulta la [guía para desarrolladores de React Native de Braze]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native) y la documentación de los SDK nativos ([Swift](https://github.com/braze-inc/braze-swift-sdk) · [Android](https://github.com/braze-inc/braze-android-sdk)).

---

## Recursos adicionales {#additional-resources}

- [Guía para desarrolladores de Braze — React Native]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native)
- [Notificaciones push — React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/push_notifications)
- [Repositorio de GitHub](https://github.com/braze-inc/braze-react-native-sdk)
- [Paquete npm](https://www.npmjs.com/package/@braze/react-native-sdk)

## Ponte en contacto {#contact}

Si tienes preguntas, ponte en contacto con [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Para detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-react-native-sdk](https://github.com/braze-inc/braze-react-native-sdk).