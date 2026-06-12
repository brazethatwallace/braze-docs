---
nav_title: Eventos personalizados efímeros
permalink: /ephemeral_custom_events/
hidden: true
page_type: reference
---

# Eventos personalizados efímeros {#ephemeral-custom-events}

- Los eventos personalizados efímeros no incluyen eventos de compra ni inicio de sesión y fin de sesión (como se describe en la documentación de Braze).
- Braze no transmite ni almacena los eventos personalizados como puntos de datos en Braze para hasta 12 ubicaciones/nombres de evento por implementación de SDK.
- La solución de eventos efímeros está integrada en los SDK de producción de Braze para iOS y Android, y en cualquier futuro SDK de producción de Braze para plataformas en las que Braze haya habilitado la solución de eventos personalizados efímeros. Esto garantiza que el cliente pueda usar dichos SDK de producción y no quede desincronizado con futuras características y correcciones de errores. También garantiza que el cliente pueda aprovechar futuras actualizaciones del SDK sin necesidad de otros procesos personalizados.
<!--
Keep this doc available on the docs site with the above permalink until 1/21/2026. This feature was built as a one-off page for a customer. Reach out to Rod Amies with questions, if needed.
-->