---
nav_title: Cabeceras de la política de seguridad de contenidos
article_title: Cabeceras de política de seguridad de contenidos para Web
platform: Web
page_order: 21
page_type: reference
description: "Este artículo cubre los encabezados de políticas de seguridad de contenidos necesarios con el SDK Web de Braze."

---

# Cabeceras de la política de seguridad de contenidos {#content-security-policy-headers}

> Content-Security-Policy proporciona seguridad añadida al restringir cómo y dónde se puede cargar contenido en tu sitio web. Este artículo de referencia cubre qué encabezados de políticas de seguridad de contenidos son necesarios con el SDK Web.

{% alert important %}
Este artículo está dirigido a los desarrolladores que trabajan en sitios web que aplican reglas CSP y se integran con Braze. No pretende ser un consejo sobre cómo debes enfocar la seguridad.
{% endalert %}

{% multi_lang_include archive/web-v4-rename.md %}

## Atributos nonce {#nonce}

Si utilizas un valor `nonce` en tus directivas `script-src` o `style-src`, pasa ese valor a la opción de inicialización `contentSecurityNonce` para propagarlo a los scripts y estilos recién creados generados por el SDK:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  contentSecurityNonce: "YOUR-NONCE-HERE", // assumes a "nonce-YOUR-NONCE-HERE" CSP value
});
```

## Directivas {#directives}

### `connect-src` {#connect-src}

{% alert warning %}
Tu URL debe coincidir con el [punto final de SDK de la API]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) de la opción de inicialización `baseUrl` que hayas elegido.
{% endalert %}

| URL | Información |
| --- | ----------- |
| `connect-src https://sdk.iad-01.braze.com` | Permite al SDK comunicarse con las API de Braze. Cambia esta URL para que coincida con el [punto final de SDK de la API]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) de la opción de inicialización `baseUrl` que hayas elegido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="connect-src #connect-src" }

### `script-src` {#script-src}

| URL | Información |
| --- | ----------- |
| `script-src https://js.appboycdn.com` | Obligatorio cuando se utiliza la integración alojada en CDN. |
| `script-src 'unsafe-eval'` | Obligatorio cuando se utiliza el fragmento de código de integración que contiene la referencia a `appboyQueue`. Para evitar el uso de esta directiva, [integra el SDK utilizando NPM]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup?tab=package%20manager). |
| `script-src 'nonce-...'`<br>o<br>`script-src 'unsafe-inline'` | Obligatorio para determinados mensajes dentro de la aplicación, como HTML personalizado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="script-src #script-src" }

### `img-src` {#img-src}

| URL | Información |
| --- | ----------- |
| `img-src: appboy-images.com braze-images.com cdn.braze.com cdn.braze.eu` | Obligatorio cuando se utilizan imágenes alojadas en el CDN de Braze. Incluye los cuatro nombres de host del CDN para asegurar que las imágenes se carguen correctamente en todos los clústeres del panel.<br><br>**Importante:** Si utilizas fuentes personalizadas, también tienes que incluir `font-src`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="img-src #img-src" }

#### Nombres de host del CDN {#cdn-hostnames}

Añade todos los siguientes nombres de host a tu directiva `img-src`:

- `appboy-images.com`
- `braze-images.com`
- `cdn.braze.com`
- `cdn.braze.eu`

## Font Awesome {#font-awesome}

Para desactivar la inclusión automática de Font Awesome, utiliza la opción de inicialización `doNotLoadFontAwesome`:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  doNotLoadFontAwesome: true,
});
```

Si decides utilizar Font Awesome, se requieren las siguientes directivas CSP:

- `font-src https://use.fontawesome.com`
- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` o `style-src 'unsafe-inline'`