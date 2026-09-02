## Requisitos previos {#prerequisites}

Antes de comenzar este tutorial, comprueba que tu SDK or kit de desarrollo de software de Braze cumple los requisitos mínimos de versión:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Mostrar banners para el SDK or kit de desarrollo de software Web {#displaying-banners-for-the-web-sdk}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Web" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToBannersUpdates((banners) => {
  // Get this placement's banner. If it's `null`, the user did not qualify for any banners.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    // Hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

```html file=main.html
<!-- your html -->

<div id="global-banner-container" style="width: 100%; height: 450px;"></div>

<!-- ...the rest of your html -->
```

!!step
lines-index.js=5

### 1. Habilitar depuración (opcional) {#1-enable-debugging-optional}

Para facilitar la solución de problemas durante el desarrollo, considera habilitar la depuración.

!!step
lines-index.js=8-23

### 2. Suscríbete a las actualizaciones de banner {#2-subscribe-to-banner-updates}

Utiliza `subscribeToBannersUpdates()` para registrar un controlador que se ejecute cada vez que se actualice un banner. Dentro del controlador, llama a `braze.getBanner("global_banner")` para obtener la última ubicación.

!!step
lines-index.js=15-22

### 3. Inserta el banner y gestiona los grupos de control {#3-insert-the-banner-and-handle-control-groups}

Utiliza `braze.insertBanner(banner, container)` para insertar un banner cuando se devuelva. Para mantener tu diseño limpio, oculta o contrae los banners que forman parte de un grupo de control (por ejemplo, cuando `isControl` es `true`).

!!step
lines-index.js=25

### 4. Actualiza tus banners {#4-refresh-your-banners}

Después de inicializar el SDK or kit de desarrollo de software, llama a `requestBannersRefresh(["global_banner", ...])` para asegurarte de que los banners se actualicen al inicio de cada sesión.

También puedes llamar a esta función en cualquier momento para actualizar posteriormente las ubicaciones de los banners.

!!step
lines-main.html=3

### 5. Añade un contenedor para tu banner {#5-add-a-container-for-your-banner}

En tu HTML, añade un nuevo elemento `<div>` y asígnale un `id` breve relacionado con el banner, como `global-banner-container`. Braze utilizará este `<div>` para insertar tu banner en la página.

{% endscrolly %}