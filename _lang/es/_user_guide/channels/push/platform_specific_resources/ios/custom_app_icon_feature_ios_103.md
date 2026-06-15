---
nav_title: "Característica de icono de aplicación personalizado (iOS 10.3)"
article_title: "Característica de icono de aplicación personalizado (iOS 10.3)"
page_order: 3
page_type: reference
description: "Este artículo de referencia cubre la actualización de iOS 10.3 sobre el icono de aplicación personalizable."
platform: iOS
channel:
  - push

---

# Característica de icono de aplicación personalizado (iOS 10.3) {#custom-app-icon-feature-ios-103}

> Con iOS 10.3, Apple introdujo la posibilidad de cambiar el icono de la pantalla de inicio de una aplicación sin tener que actualizar la aplicación desde la Apple App Store. El desarrollador ahora puede permitir al usuario cambiar el icono de la pantalla de inicio dentro de su aplicación. Apple requiere que todas las imágenes de iconos de aplicación que el desarrollador quiera poner a disposición del usuario estén incluidas en el binario que se envía a Apple para revisión durante la publicación de la aplicación en la Apple App Store.

Para notificar a tus usuarios sobre esta característica, es posible enviar un mensaje dentro de la aplicación o una notificación push a través de Braze al usuario explicando esta funcionalidad o preguntándole si desea cambiar su icono. El desarrollador solo necesitaría crear un vínculo profundo dentro de la aplicación donde se pueda mostrar el aviso nativo de iOS para realizar el cambio de icono. Esto es similar a la misma orientación que proporcionamos sobre la configuración de un primer de notificación push para APNs hoy en día.

Además, esta mensajería puede aprovechar al máximo la segmentación para hacer que el texto del mensaje sea altamente contextual para un usuario. También puedes aprovechar las pruebas A/B de mensajes para ver qué mensajería tiene el mayor impacto en el resultado deseado.