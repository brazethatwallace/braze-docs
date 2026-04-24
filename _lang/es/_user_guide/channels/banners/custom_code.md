---
nav_title: Código personalizado y puente JavaScript
article_title: Código personalizado y puente JavaScript para Banners
page_order: 2
page_type: reference
description: "Aprende a usar HTML personalizado en Banners y el puente JavaScript para registrar clics y desencadenar acciones de Braze."
channel:
  - banners
---

# Código personalizado y puente JavaScript para Banners

> Cuando usas el bloque de editor **Código personalizado** en el compositor de Banner, debes llamar a `brazeBridge.logClick()` desde tu HTML personalizado para registrar clics. Los Banners utilizan el mismo puente JavaScript que los mensajes dentro de la aplicación HTML, por lo que se aplican los mismos métodos y patrones.

Si usas HTML personalizado en el diseño de tu Banner, el SDK de Braze no puede adjuntar automáticamente listeners de clic a los elementos dentro de tu código personalizado. Debes llamar explícitamente a `brazeBridge.logClick()` para cualquier elemento en el que se pueda hacer clic (enlaces, botones y similares) que quieras rastrear en el análisis de la campaña.

Por ejemplo, para registrar un clic cuando un usuario toca un botón en tu HTML personalizado:

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Para la referencia completa del puente JavaScript, incluyendo todos los métodos disponibles y las opciones de seguimiento de clics, consulta la sección a continuación.

## Puente JavaScript {#javascript-bridge}

{% include javascript_bridge/reference.md %}