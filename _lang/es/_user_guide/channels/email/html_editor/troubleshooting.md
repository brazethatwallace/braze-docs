---
nav_title: Solución de problemas
article_title: Solución de problemas
page_order: 9
description: "Este artículo de ayuda te guía sobre cómo solucionar problemas con los correos electrónicos HTML."
channel: email
---

# Solución de problemas {#troubleshooting}

> Este artículo cubre problemas comunes con los correos electrónicos HTML y cómo resolverlos, incluyendo conflictos de extensiones, diferencias de renderizado e inlining de CSS.

## El HTML se renderiza incorrectamente en los correos electrónicos de prueba {#html-renders-incorrectly-in-test-emails}

Si tu [correo electrónico de prueba]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) no se ve bien, te recomendamos primero revisar tu configuración HTML. Después, puedes verificar estos problemas:
* [Conflictos de extensiones](#check-conflicts)
* [Renderizado de correo electrónico](#check-rendering)
* [Inlining de CSS](#switch-css-inlining)

### Conflictos de extensiones {#extension-conflicts}

Ciertas extensiones del navegador pueden causar problemas con nuestro editor de correo electrónico. Un ejemplo es [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) cuando se usa con Google Chrome. Si estás usando una de estas extensiones, deberías:
- Editar los correos electrónicos de Braze en un navegador que no tenga Grammarly como extensión del navegador
- Ponerte en contacto con tu director de cuentas de Braze y solicitar cambiar tus editores de correo electrónico a solo HTML o texto plano.

La vista de texto plano elimina tu editor `WYSIWYG` (lo que ves es lo que obtienes), así que primero deberías confirmar que todos los miembros del equipo se sienten cómodos con HTML antes de hacer esta solicitud.

### Renderizado de correo electrónico {#email-rendering}

Los correos electrónicos se renderizan de forma diferente según los navegadores y los clientes de correo electrónico, así que toma nota de con qué navegadores y clientes de correo electrónico estás experimentando problemas.

- Previsualiza tus correos electrónicos usando [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision#inbox-vision) para ver cómo se ven tus correos electrónicos en diferentes navegadores y clientes de correo electrónico.
- Una vez que hayas identificado qué navegadores o clientes de correo electrónico están causando problemas, informa a tu equipo de desarrolladores de que necesitarán modificar su HTML y hacer ajustes para adaptarse a esos navegadores o clientes de correo electrónico.

### Inlining de CSS {#css-inlining}

Hay ocasiones en las que las vistas previas en Inbox Vision aún no coinciden con lo que se envía con Braze. Esto puede deberse a la diferencia en el inlining de CSS realizado por Braze y por otras herramientas. Si sospechas que este es el caso, desactiva el inlining de CSS.

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support).