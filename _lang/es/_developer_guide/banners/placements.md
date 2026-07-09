---
nav_title: Administrar ubicaciones
article_title: Administrar ubicaciones de banners para el SDK de Braze
description: "Aprende a crear y administrar ubicaciones de banners en el SDK de Braze, incluido el acceso a sus propiedades únicas y el registro de impresiones."
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Administrar ubicaciones de banners {#manage-banner-placements}

> Aprende a crear y administrar ubicaciones de banners en el SDK de Braze, incluido el acceso a sus propiedades únicas y el registro de impresiones. Para obtener información más general, consulta [Acerca de los banners]({{site.baseurl}}/developer_guide/banners).

## Acerca de las solicitudes de ubicación {#requests}

{% multi_lang_include banners/placement_requests.md %}

## Crear una ubicación {#create-a-placement}

### Requisitos previos {#prerequisites}

Estas son las versiones mínimas del SDK necesarias para crear ubicaciones de banners:

{% multi_lang_include developer_guide/sdk_versions.md feature='banners' %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### Paso 2: Actualiza las ubicaciones en tu aplicación {#requestBannersRefresh}

Para actualizar las ubicaciones, llama al método de actualización de tu SDK. Si `subscribeToBannersUpdates` está activo, el SDK vuelve a publicar automáticamente los ID de ubicación almacenados en caché al inicio de cada nueva sesión y cuando llamas a `changeUser`. Esta actualización automática no consume un token de límite de velocidad.

{% alert tip %}
Actualiza las ubicaciones lo antes posible para evitar retrasos en la descarga o visualización de los banners.
{% endalert %}

{% tabs %}
{% tab Web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
Braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Paso 3: Escucha las actualizaciones {#subscribeToBannersUpdates}

{% alert tip %}
Si insertas banners utilizando los métodos del SDK de esta guía, todos los eventos de análisis (como impresiones y clics) se gestionan automáticamente, y las impresiones solo se registran cuando el banner está visible.
{% endalert %}

{% tabs %}
{% tab Web %}
{% subtabs %}
{% subtab JavaScript %}
Si utilizas JavaScript vanilla con el SDK Web de Braze, usa [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) para escuchar las actualizaciones de ubicación y, a continuación, llama a [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) para recuperarlas.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log("Banners were updated");
});

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}
{% subtab React %}
Si utilizas React con el SDK Web de Braze, configura [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) dentro de un hook `useEffect` y llama a [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) después de registrar tu listener.

```typescript
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    console.log("Banners were updated");
  });

  // always refresh after your subscriber function has been registered
  braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

  // cleanup listeners
  return () => {
    braze.removeSubscription(subscriptionId);
  }
}, []);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Swift %}

{% alert note %}
Tu listener de actualización de banners refleja el estado en memoria de los banners del SDK. Una sola actualización puede incluir ubicaciones que ya estaban en caché (por ejemplo, de una actualización anterior, otra pantalla o trabajo automático del SDK), no solo los ID de ubicación de tu llamada `requestRefresh` más reciente. Si solo te interesan ciertas ubicaciones, comprueba el ID de ubicación de cada banner en tu listener y omite el resto. Cuando hayas registrado tu listener, llama a `requestRefresh` para las ubicaciones que quieras sincronizar desde Braze.
{% endalert %}

```swift
let placementIds = ["global_banner", "navigation_square_banner"]
let cancellable = brazeClient.braze()?.banners.subscribeToUpdates { banners in
  banners.forEach { placementId, banner in
    print("Received banner: \(banner) with placement ID: \(placementId)")
  }
}
// Always refresh after your subscriber is registered
brazeClient.braze()?.banners.requestRefresh(placementIds: placementIds)
```

{% endtab %}
{% tab Android %}

{% alert note %}
Tu listener de actualización de banners refleja el estado en memoria de los banners del SDK. Una sola actualización puede incluir ubicaciones que ya estaban en caché (por ejemplo, de una actualización anterior, otra pantalla o trabajo automático del SDK), no solo los ID de ubicación de tu llamada `requestBannersRefresh` más reciente. Si solo te interesan ciertas ubicaciones, comprueba el ID de ubicación de cada banner en tu listener y omite el resto. Cuando hayas registrado tu listener, llama a `requestBannersRefresh` para las ubicaciones que quieras sincronizar desde Braze.
{% endalert %}

{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> placementIds = new ArrayList<>();
placementIds.add("global_banner");
placementIds.add("navigation_square_banner");
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
// Always refresh after your subscriber is registered
Braze.getInstance(context).requestBannersRefresh(placementIds);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val placementIds = listOf("global_banner", "navigation_square_banner")
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  for (banner in update.banners) {
    Log.d(TAG, "Received banner: " + banner.placementId)
  }
}
// Always refresh after your subscriber is registered
Braze.getInstance(context).requestBannersRefresh(placementIds)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
const bannerCardsSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  (data) => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map((banner) => banner.placementId)
    );
  }
);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  for (final banner in banners) {
    print("Received banner: " + banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Paso 4: Inserta utilizando el ID de ubicación {#insertBanner}

{% alert tip %}
Para obtener un tutorial completo paso a paso, consulta [Mostrar un banner por ID de ubicación]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners).
{% endalert %}

{% tabs %}
{% tab Web %}

Crea un elemento contenedor para el banner. Asegúrate de establecer su ancho y alto.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

{% subtabs local %}
{% subtab JavaScript %}
Si utilizas JavaScript vanilla con el SDK Web de Braze, llama al método [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) para sustituir el HTML interno del elemento contenedor.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("sdk-api-key", {
  baseUrl: "sdk-base-url",
  allowUserSuppliedJavascript: true, // banners require you to opt-in to user-supplied javascript
});

braze.subscribeToBannersUpdates((banners) => {
  // get this placement's banner. If it's `null` the user did not qualify for one.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  // choose where in the DOM you want to insert the banner HTML
  const container = document.getElementById("global-banner-container");

  // Insert the banner which replaces the innerHTML of that container
  braze.insertBanner(globalBanner, container);

  // Special handling if the user is part of a Control Variant
  if (globalBanner.isControl) {
    // hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}

{% subtab React %}
Si utilizas React con el SDK Web de Braze, llama al método [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) con un `ref` para sustituir el HTML interno del elemento contenedor.

```tsx
import { useRef } from 'react';
import * as braze from "@braze/web-sdk";

export default function App() {
    const bannerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
       const globalBanner = braze.getBanner("global_banner");
       if (!globalBanner || globalBanner.isControl) {
           // hide the container
       } else {
           // insert the banner to the container node
           braze.insertBanner(globalBanner, bannerRef.current);
       }
    }, []);
    return <div ref={bannerRef}></div>
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Para realizar el seguimiento de las impresiones, asegúrate de llamar a `insertBanner` para `isControl`. A continuación, puedes ocultar o contraer el contenedor.
{% endalert %}

{% endtab %}
{% tab Swift %}

```swift
// To get access to the Banner model object:
let globalBanner: Braze.Banner?
AppDelegate.braze?.banners.getBanner(for: "global_banner", { banner in
  self.globalBanner = banner
})

// UIKit implementation:
// If you simply want the Banner view, initialize a `UIView` with the placement ID:
if let braze = AppDelegate.braze {
  let bannerUIView = BrazeBannerUI.BannerUIView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}

// SwiftUI implementation:
// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height according to your parent controller.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}
Para obtener el banner en código Java, utiliza:

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

Puedes crear banners en el diseño de tus vistas Android incluyendo este XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```
{% endsubtab %}

{% subtab Kotlin %}
Si utilizas Android Views, usa este XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

Para usar Jetpack Compose, añade el artefacto `com.braze:android-sdk-jetpack-compose` al módulo de tu aplicación. Usa la misma versión que tus otras dependencias del SDK Android de Braze. Este módulo es independiente de `android-sdk-ui` e incluye el composable [`Banner`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html) bajo `com.braze.jetpackcompose.banners`.

{% alert note %}
Algunas bibliotecas de UI de Compose definen su propio composable `Banner`. Importa `com.braze.jetpackcompose.banners.Banner` explícitamente para asegurarte de llamar a la API de Braze.
{% endalert %}

```kotlin
import com.braze.jetpackcompose.banners.Banner

@Composable
fun myBannerSlot() {
    Banner(placementId = "global_banner")
}
```

Opcionalmente, pasa `heightCallback` para recibir la altura renderizada en dp cuando cambie el tamaño del banner. Como referencia, consulta la [documentación KDoc de `Banner`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html).

Si no añades el módulo de Jetpack Compose, envuelve [`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html) en [`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/AndroidView):

```kotlin
import android.view.ViewGroup
import androidx.compose.runtime.Composable
import androidx.compose.ui.viewinterop.AndroidView
import com.braze.ui.banners.BannerView

@Composable
fun myBannerSlot() {
    AndroidView(
        factory = { context ->
            BannerView(context, "global_banner").apply {
                layoutParams = ViewGroup.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT
                )
            }
        },
        update = { it.placementId = "global_banner" }
    )
}
```

Para obtener el banner en Kotlin, utiliza:
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

Si utilizas [la nueva arquitectura de React Native](https://reactnative.dev/architecture/landing-page), debes registrar `BrazeBannerView` como componente Fabric en tu `AppDelegate.mm`.

```swift
#ifdef RCT_NEW_ARCH_ENABLED
/// Register the `BrazeBannerView` for use as a Fabric component.
- (NSDictionary<NSString *,Class<RCTComponentViewProtocol>> *)thirdPartyFabricComponents {
  NSMutableDictionary * dictionary = [super thirdPartyFabricComponents].mutableCopy;
  dictionary[@"BrazeBannerView"] = [BrazeBannerView class];
  return dictionary;
}
#endif
```
Para una integración más sencilla, añade el siguiente fragmento de código JavaScript XML (JSX) a tu jerarquía de vistas, proporcionando únicamente el ID de ubicación.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```

Para obtener el modelo de datos del banner en React Native, o para comprobar la presencia de esa ubicación en la caché de tu usuario, utiliza:

```javascript
const banner = await Braze.getBanner("global_banner");
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}
Para una integración más sencilla, añade el siguiente widget a tu jerarquía de vistas, proporcionando solo el ID de ubicación.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

Puedes utilizar el método `getBanner` para comprobar si esa ubicación está presente en la caché del usuario.

```dart
braze.getBanner("global_banner").then((banner) {
  if (banner == null) {
    // Handle null cases.
  } else {
    print(banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Paso 5: Enviar un banner de prueba (opcional) {#handling-test-cards}

Antes de lanzar una campaña de banners, puedes [enviar un banner de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=banners) para verificar tu integración. Los banners de prueba se almacenan en una caché independiente en memoria y no se conservan tras reiniciar la aplicación. Aunque no se necesita ninguna configuración adicional, tu dispositivo de prueba debe ser capaz de recibir notificaciones push en primer plano para poder mostrar la prueba.

{% alert note %}
Los banners de prueba son como cualquier otro banner, salvo que se eliminan en la siguiente sesión de la aplicación.
{% endalert %}

## Registrar impresiones {#log-impressions}

Braze registra automáticamente las impresiones de los banners que están a la vista cuando utilizas métodos del SDK para insertar un banner&#8212;por lo que no es necesario realizar un seguimiento manual de las impresiones.

## Registrar clics {#logging-clicks}

El método utilizado para registrar los clics en los banners depende de cómo se muestre el banner y de la ubicación del controlador de clics.

### Contenido estándar del banner (automático) {#standard-banner-content-automatic}

Si utilizas métodos del SDK predeterminados y listos para usar para insertar banners, y tu banner utiliza componentes de editor estándar (imágenes, botones, texto), los clics se registran automáticamente. El SDK añade detectores de clics a estos elementos, sin necesidad de código adicional.

### Bloques de código personalizados {#custom-code-blocks}

Si tu banner utiliza el bloque de editor **Custom Code** en el panel de Braze, debes utilizar `brazeBridge.logClick()` para registrar los clics desde ese HTML personalizado. Esto se aplica incluso cuando se utilizan métodos del SDK para renderizar el banner, ya que el SDK no puede adjuntar automáticamente listeners a elementos dentro de tu código personalizado.

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Para obtener la referencia completa, consulta [Código personalizado y puente JavaScript para banners]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#custom-code). `brazeBridge` proporciona una capa de comunicación entre el HTML interno del banner y el SDK principal de Braze.

### Implementaciones de interfaz de usuario personalizadas (headless) {#custom-ui-implementations-headless}

Si estás creando una interfaz de usuario totalmente personalizada utilizando las [propiedades personalizadas](#custom-properties) del banner en lugar de renderizar el HTML del banner, debes registrar manualmente los clics y las impresiones desde el código de tu aplicación. Dado que el SDK no muestra el banner, no tiene forma de realizar un seguimiento automático de las interacciones con tus elementos de interfaz de usuario personalizados.

Para las firmas de los métodos y todos los detalles, consulta la [documentación de referencia del SDK de Braze]({{site.baseurl}}/developer_guide/references).

#### Registrar impresiones {#logging-impressions}

Llama al método de impresión de banner de la plataforma cuando tu interfaz de usuario personalizada considere que el banner ha sido "visto". Construye una lógica robusta para determinar qué cuenta como una impresión y así evitar eventos duplicados; por ejemplo, registra solo cuando el banner entra en el viewport (o equivalente), y no registres de nuevo cuando el mismo banner vuelva a aparecer al hacer scroll o cuando tu componente se vuelva a renderizar sin un nuevo evento de visualización.

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
const banner = braze.getBanner("placement_id_homepage_top");
if (banner) {
  braze.logBannerImpressions([banner]);
}
```
[Referencia del SDK Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerimpressions)
{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Kotlin %}
```kotlin
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.getInstance(context).logBannerImpression("placement_id_homepage_top")
```
{% endsubtab %}
{% subtab Java %}
```java
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.getInstance(context).logBannerImpression("placement_id_homepage_top");
```
{% endsubtab %}
{% endsubtabs %}
[Referencia del SDK Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-impression.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log an impression on it (for example, once when it enters viewport)
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logImpression()
}
```
[Referencia del SDK Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logimpression())
{% endtab %}
{% tab React Native %}
```javascript
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.logBannerImpression("placement_id_homepage_top");
```
Consulta el [repositorio del SDK React Native](https://github.com/braze-inc/braze-react-native-sdk) para las firmas de métodos más recientes.
{% endtab %}
{% tab Flutter %}
```dart
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
braze.logBannerImpression("placement_id_homepage_top");
```
[Referencia del SDK Flutter](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerImpression.html)
{% endtab %}
{% endtabs %}

#### Registrar clics

Llama al método de clic de banner de la plataforma cuando el usuario toque tu banner personalizado (o un botón específico). Pasa el `buttonId` opcional cuando el clic sea en un botón específico para que los análisis puedan atribuir el clic correctamente.

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

// Log click
braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
[Referencia del SDK Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerclick)
{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Kotlin %}
```kotlin
// Log click
Braze.getInstance(context).logBannerClick("placement_id_homepage_top", buttonId)  // buttonID parameter can be null
```
{% endsubtab %}
{% subtab Java %}
```java
// Log click
Braze.getInstance(context).logBannerClick("placement_id_homepage_top", buttonId);  // buttonID parameter can be null
```
{% endsubtab %}
{% endsubtabs %}
[Referencia del SDK Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-click.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log a click on it
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logClick(buttonId: buttonId)  // buttonID is optional
}
```
[Referencia del SDK Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logclick(buttonid:))
{% endtab %}
{% tab React Native %}
```javascript
// Log click
Braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
Consulta el [repositorio del SDK React Native](https://github.com/braze-inc/braze-react-native-sdk) para las firmas de métodos más recientes.
{% endtab %}
{% tab Flutter %}
```dart
// Log click
braze.logBannerClicked("placement_id_homepage_top", buttonId);  // buttonID parameter can be null
```
[Referencia del SDK Flutter](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerClicked.html)
{% endtab %}
{% endtabs %}

## Registrar descartes {#log-dismissals}

Los descartes de banners eliminan programáticamente un banner de una ubicación cuando un usuario lo descarta activamente. Una vez descartado, el banner se suprime para ese usuario. La próxima vez que se actualice la lista de ubicaciones, se devolverá un nuevo banner si el usuario es elegible para uno.

### Requisitos previos

Estas son las versiones mínimas del SDK necesarias para registrar descartes de banners:

{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 %}

### Integraciones {#integrations}

#### Integraciones estándar de banners (editor de arrastrar y soltar) {#standard-banner-integrations-drag-and-drop-editor}

Si tu banner utiliza el editor de arrastrar y soltar e incluye un componente de botón de descarte, no se necesita código adicional. Cuando un usuario hace clic en el botón de descarte, el mensaje se oculta, se activa un descarte y luego se registra un evento de descarte para los análisis.

#### Bloques de código personalizados

Si tu banner utiliza el bloque de editor **Custom Code**, puedes activar un descarte directamente desde el HTML del banner utilizando `brazeBridge.closeMessage()`.

```html
<button onclick="brazeBridge.closeMessage()">
  Dismiss
</button>
```

#### Descartar un banner programáticamente {#dismiss-a-banner-programmatically}

Si utilizas el `BrazeBannerView` estándar con el botón de descarte creado en el editor de arrastrar y soltar, no se necesita código adicional; el descarte se gestiona automáticamente.

Para integraciones de interfaz de usuario personalizadas, puedes llamar al método de descarte directamente en tu instancia de Braze para descartar un banner programáticamente y registrar un evento de descarte. El método de descarte se puede llamar varias veces de forma segura: el SDK ignora las llamadas duplicadas para el mismo banner.

Estas son las versiones mínimas del SDK necesarias para descartar un banner programáticamente:

{% sdk_min_versions swift:15.1.0 android:42.3.0 web:6.9.0 reactnative:22.0.0 flutter:20.0.0 %}

{% tabs %}
{% tab Web %}
Pasa el objeto `Banner` a `braze.dismissBanner()`. Puedes obtener el objeto `Banner` de `braze.getAllBanners()` o de una devolución de llamada de `subscribeToBannersUpdates`.

{% subtabs %}
{% subtab JavaScript %}
```javascript
import * as braze from "@braze/web-sdk";

const banners = braze.getAllBanners();
const banner = banners["global_banner"];

if (banner) {
  braze.dismissBanner(banner);
}
```
{% endsubtab %}
{% subtab React %}
```typescript
import * as braze from "@braze/web-sdk";

const banners = braze.getAllBanners();
const banner = banners["global_banner"];

if (banner) {
  braze.dismissBanner(banner);
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
Braze.getInstance(context).dismissBanner("your-placement-id");
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
Braze.getInstance(context).dismissBanner("your-placement-id")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift %}

Usa `dismiss()` en el contexto del banner cuando esté disponible. Este método es idempotente y activa la devolución de llamada `onDismiss` automáticamente. Si el contexto no está disponible, llama a `dismiss(using:)` directamente en el banner. Ambos métodos deben llamarse desde el hilo principal.

```swift
// Preferred: dismiss via context.
banner.context?.dismiss()

// Fallback: if context is unavailable.
banner.dismiss(using: braze)
```

En Objective-C, estos están disponibles como `[banner.context dismiss]` y `[banner dismissUsing:braze]`.

{% endtab %}

{% tab React Native %}
```javascript
Braze.dismissBanner("your-placement-id");
```
{% endtab %}

{% tab Flutter %}
```dart
braze.dismissBanner("your-placement-id");
```
{% endtab %}
{% endtabs %}

### Registrar análisis personalizados al descartar un banner {#log-custom-analytics-on-banner-dismissal}

Para ejecutar lógica personalizada cuando se descarta un banner, como registrar análisis, usa la devolución de llamada de descarte de tu SDK. La devolución de llamada recibe un objeto de evento con el `placementId`, `stableKey` y `trackingId` del banner.

{% tabs %}
{% tab Web %}
Usa [`Banner.subscribeToDismissedEvent()`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.banner.html#subscribetodismissedevent) para ejecutar lógica personalizada cuando se descarta un banner específico. Suscríbete al evento antes de mostrar el banner.

{% alert note %}
`Banner.subscribeToDismissedEvent()` requiere el SDK Web 6.9.0 o posterior. En versiones anteriores, usa `braze.subscribeToBannersUpdates()` y detecta el descarte comprobando si el banner ya no está presente en el mapa de banners actualizado.
{% endalert %}

{% subtabs %}
{% subtab JavaScript %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  const banner = banners["global_banner"];

  if (banner) {
    banner.subscribeToDismissedEvent(() => {
      // Run any custom logic here, such as logging custom analytics
      console.log("Banner was dismissed");
    });
  }
});

braze.requestBannersRefresh(["global_banner"]);
```
{% endsubtab %}
{% subtab React %}
```typescript
import { useEffect } from "react";
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    const banner = banners["global_banner"];

    if (banner) {
      banner.subscribeToDismissedEvent(() => {
        // Run any custom logic here, such as logging custom analytics
        console.log("Banner was dismissed");
      });
    }
  });

  braze.requestBannersRefresh(["global_banner"]);

  return () => {
    braze.removeSubscription(subscriptionId);
  };
}, []);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Android %}
Establece la propiedad opcional [`onDismissCallback`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/on-dismiss-callback.html) en [`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html).

{% subtabs %}
{% subtab Java %}

```java
import android.util.Log;
import com.braze.ui.banners.BannerView;
import kotlin.Unit;

// After obtaining your BannerView instance (for example from XML via findViewById, or `new BannerView(context, "global_banner")`)

bannerView.setOnDismissCallback((snapshot) -> {
  Log.d(TAG, "placementId: " + snapshot.getPlacementId()
    + ", stableKey: " + snapshot.getStableKey()
    + ", trackingId: " + snapshot.getTrackingId());

  // Run any custom logic here, such as logging custom analytics
  return Unit.INSTANCE;
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
import android.util.Log
import com.braze.ui.banners.BannerView

// After obtaining your BannerView instance (for example via findViewById or `BannerView(context, "global_banner")`)

bannerView.onDismissCallback = { snapshot ->
  Log.d(TAG, "placementId: ${snapshot.placementId}, stableKey: ${snapshot.stableKey}, trackingId: ${snapshot.trackingId}")

  // Run any custom logic here, such as logging custom analytics
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift %}
```swift
// After initializing your banner view instance using UIKit or SwiftUI

bannerView.onDismiss = { event in
  print("Banner dismissed — placementId: \(event.placementId ?? "unknown")")
  print("  stableKey: \(event.stableKey ?? "unknown")")
  print("  trackingId: \(event.trackingId ?? "unknown")")

  // Run any custom logic here, such as logging custom analytics
}
```
{% endtab %}

{% tab React Native %}
Establece la propiedad `onDismiss` en `Braze.BrazeBannerView` para ejecutar lógica personalizada cuando se descarta un banner.

```javascript
import Braze from "@braze/react-native-sdk";

<Braze.BrazeBannerView
  placementId="global_banner"
  onDismiss={(event) => {
    console.log("placementId:", event.placementId, "stableKey:", event.stableKey, "trackingId:", event.trackingId);
    // Run any custom logic here, such as logging custom analytics
  }}
/>
```
{% endtab %}

{% tab Flutter %}
Establece el parámetro `onDismiss` en `BrazeBannerView` para ejecutar lógica personalizada cuando se descarta un banner.

```dart
BrazeBannerView(
  placementId: 'global_banner',
  onDismiss: (BrazeBannerDismissEvent event) {
    print('placementId: ${event.placementId}, stableKey: ${event.stableKey}, trackingId: ${event.trackingId}');
    // Run any custom logic here, such as logging custom analytics
  },
)
```
{% endtab %}
{% endtabs %}

### Límite de almacenamiento de descartes pendientes {#pending-dismissal-storage-cap}

Los eventos de descarte se almacenan localmente como entradas pendientes hasta que se puedan sincronizar con el servidor de Braze en la siguiente llamada a `requestBannersRefresh`.

{% alert warning %}
En casos excepcionales en los que se acumule un gran número de descartes sin una sincronización exitosa, los descartes pendientes más antiguos pueden eliminarse. Si esto ocurre, los banners descartados anteriormente pueden reaparecer hasta que se complete la siguiente sincronización exitosa. Para minimizar este riesgo, llama a `requestBannersRefresh` cada vez que tu aplicación recupere la conectividad de red.
{% endalert %}

## Dimensiones y tamaños {#dimensions-and-sizing}

Esto es lo que debes saber sobre las dimensiones y el tamaño de los banners:

- Aunque el creador te permite previsualizar los banners en diferentes dimensiones, esa información no se guarda ni se envía al SDK.
- El HTML ocupará todo el ancho del contenedor en el que se muestre.
- Recomendamos crear un elemento de dimensiones fijas y probar esas dimensiones en el creador.

## Propiedades personalizadas {#custom-properties}

Puedes utilizar propiedades personalizadas de tu campaña de banners para recuperar datos clave-valor a través del SDK y modificar el comportamiento o la apariencia de tu aplicación. Por ejemplo, podrías:

- Enviar metadatos para tus análisis o integraciones de terceros.
- Utilizar metadatos como un `timestamp` o un objeto JSON para desencadenar lógica condicional.
- Controlar el comportamiento de un banner basándote en metadatos incluidos como `ratio` o `format`.

### Requisitos previos

Debes [añadir propiedades personalizadas]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#custom-properties) a tu campaña de banners. Además, estas son las versiones mínimas del SDK necesarias para acceder a las propiedades personalizadas:

{% sdk_min_versions swift:13.1.0 android:38.0.0 web:6.1.0 reactnative:17.0.0 flutter:15.1.0 %}

### Acceder a las propiedades personalizadas {#access-custom-properties}

Para acceder a las propiedades personalizadas de un banner, utiliza uno de los siguientes métodos según el tipo de propiedad definido en el panel. Si la clave no coincide con una propiedad de ese tipo o no existe, el método devuelve `null`.

{% tabs local %}
{% tab Web %}
```javascript
// Returns the Banner instance
const banner = braze.getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner) {

  // Returns the string property
  const stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  const booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  const numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a number)
  const timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a string of the URL
  const imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property
  const jsonObjectProperty = banner.getJsonProperty("footer_settings");
}
```
{% endtab %}

{% tab Swift %}
```swift
// Passes the specified banner to the completion handler
AppDelegate.braze?.banners.getBanner(for: "placement_id_homepage_top") { banner in
  // Returns the string property
  let stringProperty: String? = banner.stringProperty(key: "color")

  // Returns the boolean property
  let booleanProperty: Bool? = banner.boolProperty(key: "expanded")

  // Returns the number property as a double
  let numberProperty: Double? = banner.numberProperty(key: "height")

  // Returns the Unix UTC millisecond timestamp property as an integer
  let timestampProperty: Int? = banner.timestampProperty(key: "account_start")

  // Returns the image property as a String of the image URL
  let imageProperty: String? = banner.imageProperty(key: "homepage_icon")

  // Returns the JSON object property as a [String: Any] dictionary
  let jsonObjectProperty: [String: Any]? = banner.jsonObjectProperty(key: "footer_settings")
}
```
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
// Returns the Banner instance
Banner banner = Braze.getInstance(context).getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner != null) {
  // Returns the string property
  String stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  Boolean booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  Number numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a Long)
  Long timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a String of the URL
  String imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property as a JSONObject
  JSONObject jsonObjectProperty = banner.getJSONProperty("footer_settings");
}
```
{% endsubtab %}

{% subtab Kotlin %}
```kotlin
// Returns the Banner instance
val banner: Banner = Braze.getInstance(context).getBanner("placement_id_homepage_top") ?: return

// Returns the string property
val stringProperty: String? = banner.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = banner.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = banner.getNumberProperty("height")

// Returns the timestamp property (as a Long)
val timestampProperty: Long? = banner.getTimestampProperty("account_start")

// Returns the image URL property as a String of the URL
val imageProperty: String? = banner.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = banner.getJSONProperty("footer_settings")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}

```javascript
// Get the Banner instance
const banner = await Braze.getBanner('placement_id_homepage_top');
if (!banner) return;

// Get the string property
const stringProperty = banner.getStringProperty('color');

// Get the boolean property
const booleanProperty = banner.getBooleanProperty('expanded');

// Get the number property
const numberProperty = banner.getNumberProperty('height');

// Get the timestamp property (as a number)
const timestampProperty = banner.getTimestampProperty('account_start');

// Get the image URL property as a string
const imageProperty = banner.getImageProperty('homepage_icon');

// Get the JSON object property
const jsonObjectProperty = banner.getJSONProperty('footer_settings');
```

{% endtab %}
{% tab Flutter %}

```dart
// Fetch the banner asynchronously
_braze.getBanner(placementId).then(('placement_id_homepage_top') {
  // Get the string property
  final String? stringProperty = banner?.getStringProperty('color');

  // Get the boolean property
  final bool? booleanProperty = banner?.getBooleanProperty('expanded');

  // Get the number property
  final num? numberProperty = banner?.getNumberProperty('height');

  // Get the timestamp property
  final int? timestampProperty = banner?.getTimestampProperty('account_start');

  // Get the image URL property
  final String? imageProperty = banner?.getImageProperty('homepage_icon');

  // Get the JSON object property
  final Map<String, dynamic>? jsonObjectProperty = banner?.getJSONProperty('footer_settings');

  // Use these properties as needed in your UI or logic
});
```

{% endtab %}
{% endtabs %}