---
nav_title: "HTML personalizado"
article_title: "HTML personalizado"
page_order: 4
page_type: reference
description: "Este artículo ofrece un resumen de los mensajes dentro de la aplicación de código personalizado, incluidos los métodos JavaScript, el seguimiento de botones y el uso de la vista previa interactiva de HTML en Braze."
channel:
  - in-app messages
---

# Mensajes dentro de la aplicación con HTML personalizado {#custom-html-messages}

> Aunque nuestros mensajes dentro de la aplicación estándar se pueden personalizar de diversas formas, puedes obtener un control aún mayor sobre la apariencia de tus campañas utilizando mensajes diseñados y creados con HTML, CSS y JavaScript. Con una composición sencilla, puedes desbloquear funcionalidades y branding personalizados que se adapten a cualquiera de tus necesidades.

Este tipo de mensaje está disponible en el [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

## Cómo funciona {#how-it-works}

Los mensajes dentro de la aplicación HTML permiten un mayor control sobre la apariencia de un mensaje, incluyendo lo siguiente:

- Fuentes y estilos personalizados
- Videos
- Múltiples imágenes
- Comportamientos de clic
- Componentes interactivos
- Animaciones personalizadas

Los mensajes HTML personalizados pueden utilizar los métodos del [puente JavaScript](#javascript-bridge) para registrar eventos, establecer atributos personalizados, cerrar el mensaje y más. Consulta nuestro [repositorio de GitHub](https://github.com/braze-inc/in-app-message-templates) que contiene instrucciones detalladas sobre cómo usar y personalizar los mensajes dentro de la aplicación HTML para tus necesidades, y un conjunto de plantillas de mensajes dentro de la aplicación HTML5 para ayudarte a comenzar.

{% alert note %}
Para habilitar los mensajes dentro de la aplicación HTML a través del SDK Web, debes proporcionar la opción de inicialización `allowUserSuppliedJavascript` a Braze: por ejemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Esto es por razones de seguridad, ya que los mensajes dentro de la aplicación HTML pueden ejecutar JavaScript, por lo que requerimos que un administrador del sitio los habilite.
{% endalert %}

## Puente JavaScript {#javascript-bridge}

{% include javascript_bridge/reference.md %}

## Acciones basadas en enlaces {#link-based-actions}

Además de JavaScript personalizado, los SDK de Braze también pueden enviar datos de análisis con estos prácticos atajos de URL. Ten en cuenta que estos parámetros de consulta y esquemas de URL distinguen entre mayúsculas y minúsculas.

### Seguimiento de clics en botones (obsoleto) {#button-click-tracking-deprecated}

{% alert warning %}
El uso de `abButtonID` no es compatible con los tipos de mensaje [HTML con vista previa]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#html-upload-with-preview). Para obtener más información, consulta nuestra [guía de actualización]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#html-upload-with-preview).
{% endalert %}

Para registrar los clics en botones en los análisis de mensajes dentro de la aplicación, puedes añadir `abButtonId` como parámetro de consulta a cualquier vínculo profundo, URL de redirección o elemento de anclaje `<a>`. Usa `?abButtonId=0` para registrar un clic en "Button 1" y `?abButtonId=1` para registrar un clic en "Button 2".

Al igual que con otros parámetros de URL, el primer parámetro debe comenzar con un signo de interrogación `?`, mientras que los parámetros posteriores deben separarse con un ampersand `&`.

#### Ejemplos de URL {#example-urls}

- `https://example.com/?abButtonId=0` - Clic en Button 1
- `https://example.com/?abButtonId=1` - Clic en Button 2
- `https://example.com/?utm_source=braze&abButtonId=0` - Clic en Button 1 con otros parámetros de URL existentes
- `myApp://deep-link?page=home&abButtonId=1` - Vínculo profundo móvil con clic en Button 2
- `<a href="https://example.com/?abButtonId=1">` - Elemento de anclaje `<a>` con clic en Button 2

{% alert note %}
Los mensajes dentro de la aplicación solo admiten clics en Button 1 y Button 2. Las URL que no especifiquen uno de estos dos ID de botón se registrarán como "clics en el cuerpo" genéricos.
{% endalert %}

### Abrir enlace en una nueva ventana (solo móvil) {#open-link-in-new-window-mobile-only}

Para abrir enlaces fuera de tu aplicación en una nueva ventana, establece `?abExternalOpen=true`. El mensaje se descartará antes de abrir el enlace.

Para la vinculación en profundidad, Braze abrirá tu URL independientemente del valor de `abExternalOpen`.

### Abrir como vínculo profundo (solo móvil) {#open-as-deeplink-mobile-only}

Para que Braze gestione tu enlace HTTP o HTTPS como un vínculo profundo, establece `?abDeepLink=true`.

Cuando este parámetro de cadena de consulta está ausente o establecido en `false`, Braze intentará abrir el enlace web en un navegador web interno dentro de la aplicación anfitriona.

### Cerrar mensaje dentro de la aplicación {#close-in-app-message}

Para cerrar un mensaje dentro de la aplicación, puedes usar el método de JavaScript `brazeBridge.closeMessage()`.

Por ejemplo, `<a onclick="brazeBridge.closeMessage()" href="#">Close</a>` cerrará el mensaje dentro de la aplicación.

## Carga HTML con vista previa {#html-upload-with-preview}

Al crear mensajes dentro de la aplicación con HTML personalizado, puedes previsualizar tu contenido interactivo directamente en Braze.

El panel de vista previa del mensaje en el editor muestra una vista previa realista que renderiza el JavaScript incluido en tu mensaje. Puedes previsualizar e interactuar con tus mensajes personalizados desde el panel de vista previa haciendo clic en la paginación, enviando formularios o cuestionarios, viendo animaciones JavaScript y más.

![Interacción con la vista previa HTML deslizando entre páginas.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Los métodos JavaScript de `brazeBridge` que utilices en tu HTML no actualizarán los perfiles de usuario mientras previsualizas en el panel.
{% endalert %}

### Crear una Campaign {#instructions}

#### Archivos de activos {#asset-files}

Al crear mensajes dentro de la aplicación de código personalizado con carga HTML, puedes subir activos de Campaign a la [biblioteca de medios]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) para referenciarlos en tu mensaje.

Los siguientes tipos de archivo son compatibles para la carga:

| Tipo de archivo        | Extensión de archivo              |
| :--------------- | :-------------------------------- |
| Archivos de fuentes       | `.ttf`, `.woff`, `.otf`, `.woff2` |
| Imágenes SVG       | `.svg`                            |
| Archivos JavaScript | `.js`                             |
| Archivos CSS        | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Archivos de activos" }

Braze recomienda subir activos a la biblioteca de medios por dos razones:

1. Los activos añadidos a una Campaign a través de la biblioteca de medios permiten que tus mensajes se muestren incluso cuando el usuario está sin conexión o tiene una conexión a internet deficiente.
2. Los activos subidos a Braze se pueden reutilizar en distintas Campaigns.

##### Añadir archivos de activos {#adding-asset-files}

Puedes añadir activos nuevos o existentes a tu Campaign.

Para añadir nuevos activos a tu Campaign, utiliza la sección de arrastrar y soltar para subir un archivo. Los activos añadidos en esta sección también se agregarán automáticamente a la biblioteca de medios. Para añadir activos que ya hayas subido a la biblioteca de medios, selecciona **Añadir desde la biblioteca de medios**.

Una vez añadidos tus activos, aparecerán en la sección **Activos para esta Campaign**.

Si el nombre de un activo coincide con el de un activo HTML local, se reemplaza automáticamente (por ejemplo, se sube `cat.png` y existe `<img src="cat.png" />`).

De lo contrario, pasa el cursor sobre un activo de la lista y selecciona <i class="fas fa-copy"></i> **Copiar** para copiar la URL del archivo a tu portapapeles. Luego pega la URL del activo copiada en tu HTML como lo harías normalmente al referenciar un activo remoto.

### Editor HTML {#html-editor}

Los cambios que realices en el HTML se renderizan automáticamente en el panel de vista previa a medida que escribes. Los métodos JavaScript de [`brazeBridge`](#bridge) que utilices en tu HTML no actualizarán los perfiles de usuario mientras previsualizas en el panel.

{% alert tip %}
Puedes seleccionar <i class="fa-solid fa-magnifying-glass" aria-label="Buscar"></i> **Buscar** dentro del editor HTML para buscar en tu código.
{% endalert %}

### Seguimiento de botones {#button-tracking-improvements}

Puedes hacer seguimiento del rendimiento dentro de tu mensaje dentro de la aplicación de código personalizado utilizando el método JavaScript [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types). Esto te permite hacer seguimiento programático de "Botón 1", "Botón 2" y "Clics en el cuerpo" usando `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')` o `brazeBridge.logClick()`, respectivamente.

| Clics     | Método                       |
| ---------- | ---------------------------- |
| Botón 1   | `brazeBridge.logClick('0')` |
| Botón 2   | `brazeBridge.logClick('1')` |
| Clic en el cuerpo | `brazeBridge.logClick()`    |
| Seguimiento de botón personalizado |`brazeBridge.logClick('your custom name here')`|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Seguimiento de botones #button-tracking-improvements" }

{% alert note %}
Este método de seguimiento de botones reemplaza los métodos anteriores de seguimiento automático de clics (como `?abButtonId=0`), que han sido eliminados.
{% endalert %}

Utiliza [`brazeBridge.logClick(button_id)`](#button-tracking-improvements) para mensajes HTML con vista previa cuando necesites más de dos botones con seguimiento. El botón 1 y el botón 2 se asignan a `'0'` y `'1'`; los botones adicionales usan ID personalizados (hasta 100 ID únicos por Campaign). Para restricciones de caracteres en los ID de botones, consulta [Seguimiento de botones](#button-tracking-improvements).

### Solucionar problemas con enlaces HTML personalizados y comportamiento de cierre {#troubleshoot-custom-html-links-and-close-behavior}

#### Los clics en botones no abren el enlace {#button-clicks-do-not-open-the-link}

Si un botón en tu mensaje dentro de la aplicación con HTML personalizado no carga al hacer clic, verifica que el enlace utilice una URL válida o un esquema de vínculo profundo compatible. Las URL mal formadas o los esquemas personalizados no compatibles pueden impedir que la acción de clic se complete.

#### Clics en el cuerpo al cerrar el mensaje {#body-clicks-when-closing-the-message}

Llamar a `brazeBridge.closeMessage()` cierra el mensaje pero no registra análisis por sí solo. Para registrar un clic en el cuerpo cuando el usuario cierra el mensaje, llama a `brazeBridge.logClick()` antes de `brazeBridge.closeMessage()` para que el registro de clics sea consistente en todas las plataformas.

### Cambios incompatibles con versiones anteriores {#backward-incompatible-changes}

1. El vínculo profundo `braze://close`, que anteriormente era compatible con aplicaciones móviles, ha sido eliminado en favor del JavaScript `brazeBridge.closeMessage()`. Esto permite mensajes HTML multiplataforma, ya que la Web no admite vínculos profundos.
2. El seguimiento automático de clics, que usaba `?abButtonId=0` para los ID de botones, y el seguimiento de "clic en el cuerpo" en botones de cierre han sido eliminados. Los siguientes ejemplos de código muestran cómo cambiar tu HTML para usar nuestros nuevos métodos JavaScript de seguimiento de clics:

   | Antes | Después |
   |:-------- |:------------|
   |<code>&lt;a href="braze://close"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="braze://close?abButtonId=0"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="app://deeplink?abButtonId=0">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="app://deeplink" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "braze://close?abButtonId=1"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cambios incompatibles con versiones anteriores #backward-incompatible-changes" }