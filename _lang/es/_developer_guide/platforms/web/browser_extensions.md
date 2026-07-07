---
nav_title: Extensiones del navegador
article_title: Integración de extensiones de navegador para Web
platform: Web
page_order: 20
page_type: reference
description: "Este artículo describe cómo utilizar el SDK Web de Braze dentro de las extensiones de tu navegador (Google Chrome, Firefox)."

---

# Extensión del navegador {#browser-extension}

> Este artículo describe cómo utilizar el SDK Web de Braze dentro de las extensiones de tu navegador (Google Chrome, Firefox).

Integra el SDK Web de Braze en la extensión de tu navegador para recopilar análisis y mostrar mensajes enriquecidos a los usuarios. Esto incluye tanto **las extensiones de Google Chrome** como **los complementos de Firefox**.

## Qué se admite {#whats-supported}

En general, dado que las extensiones son HTML y JavaScript, puedes usar Braze para lo siguiente:

* **Análisis**: Captura eventos personalizados, atributos e incluso identifica a usuarios recurrentes dentro de tu extensión. Usa estos rasgos de perfil para potenciar la mensajería de canales cruzados.
* **Mensajes dentro de la aplicación**: Desencadena mensajes dentro de la aplicación cuando los usuarios realicen una acción dentro de tu extensión, utilizando nuestra mensajería nativa o HTML personalizada.
* **Content Cards**: Añade una fuente de tarjetas nativas a tu extensión para la incorporación o el contenido promocional.
* **Notificación push web**: Envía notificaciones puntuales aunque tu página web no esté abierta en ese momento.

## Lo que no se admite {#whats-not-supported}

* Los prestadores de servicios no son compatibles con el SDK Web de Braze; sin embargo, esto está en la hoja de ruta para considerarlo en el futuro.

## Tipos de extensión {#extension-types}

Braze puede incluirse en las siguientes áreas de tu extensión:

| Área | Detalles | Qué se admite |
|--------|-------|------|
| Página emergente | La página [emergente](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups) es un diálogo que puede mostrarse a los usuarios al hacer clic en el icono de tu extensión en la barra de herramientas del navegador. | Análisis, mensajes dentro de la aplicación y Content Cards |
| Scripts de fondo | [Los scripts de fondo](https://developer.chrome.com/extensions/background_pages) (solo Manifest v2) permiten a tu extensión inspeccionar e interactuar con la navegación del usuario o modificar páginas web (por ejemplo, cómo los bloqueadores de anuncios detectan y cambian el contenido de las páginas). | Análisis, mensajes dentro de la aplicación y Content Cards.<br><br>Los scripts de fondo no son visibles para los usuarios, por lo que para la mensajería, necesitarías comunicarte con las pestañas del navegador o con tu página emergente al mostrar los mensajes. |
| Páginas de opciones | La [página de opciones](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages) permite a tus usuarios alternar configuraciones dentro de tu extensión. Es una página HTML independiente que abre una nueva pestaña. | Análisis, mensajes dentro de la aplicación y Content Cards |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 aria-label="Tipos de extensión" }

## Permisos {#permissions}

No se requieren permisos adicionales en tu `manifest.json` cuando se integra el SDK de Braze (`braze.min.js`) como un archivo local incluido con tu extensión.

Sin embargo, si utilizas [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/), o haces referencia al SDK de Braze desde una URL externa, o has establecido una política de seguridad de contenidos estricta para tu extensión, tendrás que ajustar la configuración de [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) en tu `manifest.json` para permitir fuentes de scripts remotas.

## Cómo empezar {#getting-started}

{% alert tip %}
Antes de empezar, asegúrate de haber leído la [guía de configuración inicial del SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) Web para saber más sobre nuestra integración de JavaScript en general.  <br><br>También puedes marcar la [referencia del SDK de JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) para obtener información detallada sobre los distintos métodos y opciones de configuración del SDK.
{% endalert %}

Para integrar el SDK Web de Braze, primero debes descargar una copia de la última biblioteca JavaScript. Esto se puede hacer utilizando NPM o descargándolo directamente desde el [CDN de Braze](https://js.appboycdn.com/web-sdk/latest/braze.min.js).

Alternativamente, si prefieres utilizar [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/) o utilizar una copia alojada externamente del SDK de Braze, ten en cuenta que cargar recursos externos requerirá que ajustes la configuración de [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) en tu `manifest.json`.

Una vez descargado, asegúrate de copiar el archivo `braze.min.js` en algún lugar del directorio de tu extensión.

### Ventanas emergentes de extensión {#popup}

Para añadir Braze a una ventana emergente de extensión, haz referencia al archivo JavaScript local en tu `popup.html`, como harías en un sitio web normal. Si utilizas Google Tag Manager, puedes añadir Braze utilizando nuestras [plantillas de Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/).

```html
<html>
    <title>popup.html</title>
    <!-- Add the Braze library -->
    <script src="/relative/path/to/braze.min.js"></script>
    <script>
    // Initialize Braze here
    </script>
</html>
```

### Script de fondo (solo Manifest v2) {#background-script}

Para utilizar Braze dentro del script de fondo de tu extensión, añade la biblioteca Braze a tu `manifest.json` en la matriz `background.scripts`. Esto hará que la variable global `braze` esté disponible en el contexto de tu script de fondo.


```json
{
    "manifest_version": 2,
    "background": {
        "scripts": [
            "relative/path/to/braze.min.js",
            "background.js"
        ]
    }
}
```

### Página de opciones {#options-page}

Si utilizas una página de opciones (a través de las propiedades del manifiesto `options` o `options_ui`), puedes incluir Braze tal y como lo harías en las [instrucciones de `popup.html`](#popup).

## Inicialización {#initialization}

Una vez incluido el SDK, puedes inicializar la biblioteca como de costumbre.

Dado que las extensiones del navegador no admiten cookies, puedes desactivarlas inicializando con `noCookies: true`.

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true,
    noCookies: true
});
```

Para más información sobre las opciones de inicialización admitidas, visita la [referencia del SDK Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

## Push {#push}

Los diálogos emergentes de las extensiones no permiten las solicitudes push (no tienen la barra de URL en la navegación). Así que para registrarte y solicitar el permiso push en el diálogo emergente de una extensión, tendrás que utilizar una solución alternativa de dominio, como se describe en [Dominio push alternativo]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain).