---
nav_title: SDK de React Native
article_title: Guía del repositorio del SDK de React Native
page_order: 7
description: "Referencia del README del SDK de React Native de Braze reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guía del repositorio del SDK de React Native {#react-native-sdk-repository-guide}

## Acerca del SDK de Braze para React Native

El SDK de Braze para React Native conecta tus aplicaciones de iOS y Android con Braze: perfiles de usuario, superficies de mensajería, análisis y conmutadores de características. Envuelve el [SDK nativo de Braze para Swift](https://github.com/braze-inc/braze-swift-sdk) y el [SDK de Braze para Android](https://github.com/braze-inc/braze-android-sdk) detrás de una API de JavaScript.

**La inicialización se realiza desde JavaScript:** configuras la configuración nativa (push, registro, delegados) en los recursos de Android y en `AppDelegate` de iOS, y luego llamas a `Braze.initialize(apiKey, endpoint)` desde JavaScript para iniciar el SDK. Esto te da control total sobre cuándo se inicializa el SDK y con qué credenciales. Después de la inicialización, llama a otros métodos del SDK (por ejemplo, `changeUser`, `logCustomEvent`) según sea necesario.

### Lo que puedes hacer

- **Gestión de usuarios**: Identifica usuarios, establece campos de perfil, atributos personalizados, alias y grupos de suscripción
- **Mensajes dentro de la aplicación**: Interfaz predeterminada de Braze o gestión personalizada a través de suscripciones y API de registro
- **Content Cards**: Interfaz de fuente predeterminada, u obtén tarjetas y construye tu propia interfaz
- **Banners**: Banners HTML basados en ubicación, incluido `BrazeBannerView`
- **Notificaciones push**: Solicitudes de permiso, registro de tokens, listeners de carga útil (consulta las notas de plataforma en **Configuración nativa**)
- **Conmutadores de características**: Actualiza, lee propiedades, registra impresiones
- **Análisis**: Eventos personalizados, compras, vaciado inmediato
- **Controles del SDK**: Habilita/deshabilita el SDK, borra datos locales, firmas de autenticación del SDK

## Requisitos previos

- **Cuenta de Braze** con clave de API de la aplicación y endpoint del SDK
- Entorno de desarrollo de **React Native** ([configuración del entorno de React Native](https://reactnative.dev/docs/set-up-your-environment))
- **iOS**: Xcode, CocoaPods (`cd ios && pod install`)
- **Android**: Android Studio / Gradle; complemento Kotlin Gradle según lo requiera tu plantilla de React Native
- **Push** (si se utiliza): configuración de FCM (Android) y APNs (iOS) según la [documentación de push](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/push_notifications/)

Para conocer la ubicación de las credenciales en el panel, consulta el [resumen de integración](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native).

## Instalación

``` bash
npm install @braze/react-native-sdk
# or:
# yarn add @braze/react-native-sdk
```

---

## Inicio rápido

Esta sección muestra la configuración mínima necesaria para inicializar el SDK de Braze para React Native.

1. Instala el paquete npm (en **Instalación**).
2. Completa la **configuración nativa** para Android e iOS (configuración, permisos, push si es necesario).
3. Inicializa el SDK desde JavaScript y empieza a usarlo:

``` typescript
import Braze from "@braze/react-native-sdk";

// Initialize the SDK — call early in your app lifecycle (e.g. in a useEffect).
// The API key and endpoint are passed from JavaScript; native configuration
// (push, logging, etc.) is applied automatically from your native setup.
Braze.initialize("<YOUR_API_KEY>", "<YOUR_SDK_ENDPOINT>");

Braze.changeUser("user-123");
Braze.logCustomEvent("button_clicked", { screen: "home" });
```

Las tipificaciones de TypeScript se incluyen con el paquete (`src/index.d.ts` en GitHub).

Llamar a `Braze.initialize` de nuevo con credenciales diferentes destruye la instancia actual y la vuelve a crear, lo que permite la reinicialización a mitad de sesión.

---

## Configuración nativa

> **Fuente de referencia:** Las pantallas paso a paso, los cambios de Gradle/CocoaPods y la lista completa de claves XML de Android están en la [guía para desarrolladores de Braze React Native](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native). Los fragmentos de código en esta sección son ejemplos mínimos.

### Android

- Añade el **complemento Kotlin de Gradle** en tu archivo raíz `build.gradle` si tu plantilla aún no lo incluye (las versiones dependen de tu versión de React Native).
- Añade un archivo de recursos `braze.xml` en `res/values` con tu configuración. Habilita la inicialización diferida para que el SDK espere a que se llame a `Braze.initialize()` desde JavaScript antes de iniciarse. Otros valores de configuración (push, tiempo de espera de sesión, etc.) se siguen leyendo desde este archivo y se aplican en el momento de la inicialización.
- Asegúrate de que los permisos básicos como `INTERNET` y `ACCESS_NETWORK_STATE` estén en `AndroidManifest.xml`.
- Para push, completa la integración de FCM y cualquier ID de remitente de Braze o indicadores de registro descritos en la documentación.

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
** La clave de API y el endpoint ya no se configuran en `braze.xml`: se pasan desde JavaScript a través de `Braze.initialize(apiKey, endpoint)`.
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

- **Closure `configure`**: recibe un `Braze.Configuration` y te permite establecer propiedades de configuración nativa (registro, push, sesiones, etc.). La clave de API y el endpoint se proporcionan desde JavaScript; no los configuras aquí.
- **Closure `postInitialization`** *(opcional)*: recibe la instancia activa de `Braze` después de su creación, para configuraciones que requieren la instancia (por ejemplo, almacenar una referencia, establecer delegados).

{% alert note %}
** `BrazeReactInitializer.configure` es una API orientada a Swift que reemplaza al método obsoleto `BrazeReactBridge.initBraze(_:)`. También resuelve un problema de resolución de tipos de Swift con `Braze.Configuration` en el puente de Objective-C.
{% endalert %}
---

## Referencia de configuración

En React Native, **la configuración es nativa**: Android lee `res/values/braze.xml`, e iOS utiliza closures registrados a través de **`BrazeReactInitializer.configure`**. Ambos se aplican cuando se llama a `Braze.initialize(apiKey, endpoint)` desde JavaScript.

### Android (`braze.xml`)

Los valores predeterminados se encuentran en XML; [`BrazeConfig.Builder`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) puede sobreescribirlos al inicio. La lista autorizada de claves y tipos se encuentra en la [guía de integración del SDK de Android](https://www.braze.com/docs/developer_guide/platforms/android/sdk_integration/) y en [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) (cada propiedad de Kotlin corresponde a los recursos documentados `com_braze_*`).

Entradas de uso frecuente:

| Clave | Tipo de recurso | Descripción |
|-------|-----------------|-------------|
| `com_braze_enable_delayed_initialization` | `bool` | **Obligatorio.** Establece en `true` para que el SDK espere a `Braze.initialize()` desde JavaScript. |
| `com_braze_api_key` | `string` | No es necesario cuando se utiliza `Braze.initialize()` desde JavaScript (las credenciales se pasan desde JS). Solo es obligatorio para la inicialización nativa heredada. |
| `com_braze_custom_endpoint` | `string` | No es necesario cuando se utiliza `Braze.initialize()` desde JavaScript. Solo es obligatorio para la inicialización nativa heredada. |
| `com_braze_server_target` | `string` | Selector opcional de clúster/entorno (p. ej., algunas compilaciones internas o de prueba). Prefiere `com_braze_custom_endpoint` para producción a menos que tu integración de Braze indique lo contrario. |
| `com_braze_firebase_cloud_messaging_registration_enabled` | `bool` | Cuando es `true`, Braze se registra para FCM (configuración típica de push). |
| `com_braze_firebase_cloud_messaging_sender_id` | `string` | ID de remitente de FCM cuando el registro automático está habilitado. |
| `com_braze_handle_push_deep_links_automatically` | `bool` | Permite que Braze abra los vínculos profundos de push automáticamente. |
| `com_braze_trigger_action_minimum_time_interval_seconds` | `integer` | Mínimo de segundos entre acciones desencadenantes de mensajes dentro de la aplicación. |
| **Otros** | *varios* | Claves adicionales no mostradas aquí (tiempo de espera de sesión, geovallas, ubicación, valores predeterminados de notificación, listas de dispositivos permitidos, inicialización diferida, autenticación del SDK, entre otros). Consulta [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) y la [guía de integración del SDK de Android](https://www.braze.com/docs/developer_guide/platforms/android/sdk_integration/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android (braze.xml)" }

### iOS (`Braze.Configuration`)

Establece las propiedades de configuración nativas en el closure `configure` pasado a `BrazeReactInitializer.configure`. El closure recibe una instancia de `Braze.Configuration`; la clave de API y el endpoint se configuran automáticamente a partir de la llamada a `Braze.initialize` en JavaScript. Detalles completos: [`Braze.Configuration`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) y los tipos anidados **`api`**, **`push`**, **`logger`**, **`location`**.

| Área | Miembros (representativos) | Notas |
|------|----------------------------|-------|
| **Credenciales** | `api.key`, `api.endpoint` | Se configuran automáticamente a partir de `Braze.initialize(apiKey, endpoint)` en JavaScript. No los establezcas en el closure `configure`. |
| **Registro de logs** | `logger.level` | El registro detallado es para desarrollo; reduce el ruido en producción. |
| **Push** | `push.automation`, `push.appGroup`, … | La automatización simplifica el registro; `appGroup` es necesario para Push Stories o extensiones cuando se utilizan. |
| **Mensajes dentro de la aplicación** | `triggerMinimumTimeInterval` | **30** segundos predeterminados entre desencadenantes. |
| **Sesiones** | `sessionTimeout` | Inactividad antes de que se inicie una nueva sesión (consulta la documentación de sesiones de Braze). |
| **Privacidad / datos** | `api.trackingPropertyAllowList`, `devicePropertyAllowList`, `api.sdkAuthentication` | Alinea con el [manifiesto de privacidad](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/) y la configuración del producto de autenticación del SDK. |
| **Red** | `api.requestPolicy`, `api.flushInterval` | Política de reintentos de solicitudes y cadencia de envío. |
| **Suscripción push** | `optInWhenPushAuthorized` | Cuando es `true`, la suscripción puede cambiar a aceptada después de que el usuario autorice las notificaciones. |
| **IAM + cambios de usuario** | `preventInAppMessageDisplayForDifferentUser` | Reduce los mensajes dentro de la aplicación no coincidentes si cambia el ID de usuario. |
| **Otros** | `forwardUniversalLinks`, `ephemeralEvents`, `useUUIDAsDeviceId`, … | Consulta la documentación de Swift para conocer el comportamiento completo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOS (Braze.Configuration)" }

El puente de React Native establece **`api.sdkFlavor`** / metadatos del SDK específicos de React durante la inicialización; no los sobreescribas a menos que la documentación de Braze te indique hacerlo.

---

## API de JavaScript / TypeScript

La exportación predeterminada del paquete es la clase `Braze` con métodos **estáticos** (por ejemplo, `Braze.changeUser`, `Braze.logPurchase`). Las constantes como `Braze.Events`, `Braze.Genders` y `Braze.NotificationSubscriptionTypes` están asociadas a la misma exportación.

---

## Características principales

### Gestión de usuarios

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.changeUser("user-123");
Braze.setEmail("user@example.com");
Braze.setCustomUserAttribute("plan", "premium");
Braze.addAlias("external_id", "marketing_id");
Braze.addToSubscriptionGroup("NEWSLETTER_GROUP_UUID");
```

**Autenticación del SDK** opcional: pasa una firma como segundo argumento a `changeUser`, o llama a `Braze.setSdkAuthenticationSignature(signature)` cuando esté habilitado en el panel.

### Mensajes dentro de la aplicación

- Con la **interfaz de usuario predeterminada de Braze**, sigue la [documentación de mensajes dentro de la aplicación](https://www.braze.com/docs/developer_guide/in_app_messages?sdktab=react%20native); normalmente **no** necesitas llamar a `subscribeToInAppMessage` solo para mostrar la interfaz predeterminada.
- Para un manejo **personalizado**, suscríbete con `useBrazeUI: false` y luego registra las impresiones o clics según sea necesario:

``` typescript
Braze.subscribeToInAppMessage(false, (event) => {
  const msg = event.inAppMessage;
  // Render your own UI from msg.message, msg.buttons, etc.
  Braze.logInAppMessageImpression(msg);
});
```

### Content Cards

``` typescript
const cards = await Braze.getCachedContentCards();
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
// <Braze.BrazeBannerView placementId="homepage_banner" />
```

### Notificaciones push

``` typescript
Braze.requestPushPermission({
  alert: true,
  badge: true,
  sound: true,
});
// Token registration is usually handled natively; see docs for your setup.
Braze.registerPushToken(token);
```

- **`getInitialPushPayload`**: úsalo cuando la aplicación se abre desde una notificación para evitar condiciones de carrera con `Linking` de RN; requiere hooks nativos (`BrazeReactUtils` en iOS, `BrazeReactUtils.populateInitialPushPayloadFromIntent` en Android) como se describe en los comentarios de la documentación de TypeScript y en la aplicación de ejemplo.
- **`Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, ...)`** es **solo para Android** según las tipificaciones públicas.

### Conmutadores de características

``` typescript
const flag = await Braze.getFeatureFlag("new_checkout");
if (flag?.enabled) {
  const rollout = flag.getNumberProperty("rollout_percentage") ?? 0;
}
Braze.refreshFeatureFlags();
Braze.logFeatureFlagImpression("new_checkout");
```

### Análisis y compras

``` typescript
Braze.logCustomEvent("purchase_completed", { sku: "sku-1" });
Braze.logPurchase("sku-1", "29.99", "USD", 1, { source: "cart" });
Braze.requestImmediateDataFlush();
```

Nota: `logPurchase` recibe el **precio como cadena** (consulta las tipificaciones).

### Gestión de datos y estado del SDK

**`changeUser`** solo le indica a Braze a qué ID de usuario atribuir la **nueva** actividad. **No** borra los datos almacenados en caché del SDK en el dispositivo. No existe una API independiente para "cerrar sesión": si necesitas un cierre de sesión tradicional (borrar el estado local de Braze para que el perfil, los mensajes y los tokens en caché del usuario anterior desaparezcan de esta instalación), normalmente utilizas **`wipeData()`**. Este es un restablecimiento local completo.

``` typescript
Braze.wipeData();
Braze.disableSDK();
Braze.enableSDK();
```

**`wipeData()`** — Borra los datos **locales** de Braze para esta instalación (estado almacenado en caché de usuario/sesión/tarjeta, asociación de token de notificaciones push, etc.). Úsalo para comportamientos de **cierre de sesión** cuando no debas dejar el estado de Braze del usuario anterior en el dispositivo, además de **"eliminar mis datos en este dispositivo"**, restablecimientos de **QA** sin reinstalar, o flujos estrictos de **privacidad**. **`changeUser`** por sí solo no realiza esa limpieza; solo establece qué ID de usuario recibe los **nuevos** eventos. En **iOS**, el comportamiento puede diferir de Android (por ejemplo, la interacción con el estado del SDK deshabilitado); consulta la documentación nativa de Braze si implementas esto en producción.

**`disableSDK()`** — Detiene la operación del SDK (sin recopilación ni reenvío según lo configurado). Úsalo para alternar la **exclusión del usuario**, **modos restringidos** (cumplimiento normativo, configuración infantil) o **depuración** sin eliminar la dependencia.

**`enableSDK()`** — Reactiva el SDK después de **`disableSDK()`**. En **iOS**, la reactivación puede **no** aplicarse hasta el **siguiente inicio de la aplicación**; verifica en la documentación de Braze Swift/iOS antes de depender de una reactivación inmediata.

---

## Eventos

Suscríbete con `Braze.addListener(event, callback)`. La llamada devuelve un objeto de suscripción; llama a **`.remove()`** sobre él para dejar de escuchar.

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

En un componente de React, almacena la suscripción y llama a `.remove()` en tu limpieza (por ejemplo, en el return de un `useEffect`):

``` typescript
useEffect(() => {
  const sub = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
    setCards(update.cards);
  });
  return () => sub.remove();
}, []);
```

| Constante de evento | Carga útil (resumen) |
|----------------|-------------------|
| `Braze.Events.CONTENT_CARDS_UPDATED` | Últimas Content Cards |
| `Braze.Events.BANNER_CARDS_UPDATED` | Últimos banners |
| `Braze.Events.FEATURE_FLAGS_UPDATED` | Array de conmutadores de características |
| `Braze.Events.IN_APP_MESSAGE_RECEIVED` | Evento de mensaje dentro de la aplicación |
| `Braze.Events.SDK_AUTHENTICATION_ERROR` | Detalles de error de autenticación del SDK |
| `Braze.Events.PUSH_NOTIFICATION_EVENT` | Carga útil push (**solo Android**) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos" }

---

## Notas de integración

- **Expo**: utiliza el [complemento Braze Expo](https://github.com/braze-inc/braze-expo-plugin) para evitar la configuración nativa manual siempre que sea posible.
- **New Architecture / Turbo Modules**: compatible con versiones recientes del complemento; sigue la guía del desarrollador y la configuración de ejemplo de `AppDelegate` / Gradle si realizas la migración.
- **Privacidad (iOS)**: métodos como `updateTrackingPropertyAllowList` admiten la configuración relacionada con el manifiesto de privacidad; consulta [Manifiesto de privacidad de Swift](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/).

- **Jest**: simula los módulos nativos de `react-native` o el módulo Braze Turbo (consulta `__tests__/jest.setup.js` en este repositorio para ver ejemplos de patrones).

## Soporte de versiones

{% alert note %}
Este SDK ha sido probado con la versión **0.85.3** de React Native.
{% endalert %}
La siguiente tabla muestra las versiones de React Native compatibles según la versión del complemento de Braze.

| Complemento de Braze | React Native | Nueva arquitectura |
|--------------|--------------|------------------|
| 9.0.0+       | ≥ 0.71       | Sí               |
| 6.0.0+       | ≥ 0.68       | Sí (≥ 0.70.0)    |
| 2.0.0+       | ≥ 0.68       | Sí               |
| ≤ 1.41.0     | ≤ 0.71       | No               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Soporte de versiones" }

Respeta también los requisitos del SDK nativo:

- [Información de versión del SDK de Android](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
- [Información de versión del SDK de Swift](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

---

## Complemento Braze Expo

Para flujos de trabajo gestionados por Expo, consulta el [repositorio del complemento Braze Expo](https://github.com/braze-inc/braze-expo-plugin).

---

## Aplicación de ejemplo

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

## Depuración y solución de problemas

Habilita el registro de Braze en la configuración **nativa** durante el desarrollo para que el SDK escriba en la consola del sistema (Xcode / Android Logcat). Esto ayuda a verificar la inicialización, los cambios de usuario y la entrega de eventos.

- **iOS** — En el cierre `configure` pasado a `BrazeReactInitializer.configure`, establece `config.logger.level = .debug` (o `.info`). Reduce o desactiva en producción para que los registros no sean visibles para los usuarios.
- **Android** — Usa el recurso `com_braze_logger_initial_log_level` en `braze.xml` o establece el equivalente en `BrazeConfig.Builder` (consulta [BrazeConfigurationProvider](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/logger-initial-log-level.html)). Usa un nivel no detallado o elimina la anulación antes de la publicación.

Para una solución de problemas más profunda (red, sesión o comportamiento de Campaign), consulta la [guía del desarrollador de Braze React Native](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native) y la documentación del SDK nativo ([Swift](https://github.com/braze-inc/braze-swift-sdk) · [Android](https://github.com/braze-inc/braze-android-sdk)).

---

## Recursos adicionales

- [Guía para desarrolladores de Braze — React Native](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native)
- [Notificaciones push — React Native](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/push_notifications/)
- [Repositorio de GitHub](https://github.com/braze-inc/braze-react-native-sdk)
- [Paquete npm](https://www.npmjs.com/package/@braze/react-native-sdk)

## Contacto

Si tienes preguntas, contacta con el soporte técnico de Braze para obtener ayuda.
<!-- END GENERATED README CONTENT -->

Para obtener detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-react-native-sdk](https://github.com/braze-inc/braze-react-native-sdk).