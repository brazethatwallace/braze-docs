---
nav_title: Guía de actualización a iOS 15
article_title: Guía de actualización al SDK de iOS 15
page_order: 7
platform: iOS
description: "Este artículo de referencia cubre las nuevas actualizaciones del sistema operativo iOS 15, las actualizaciones necesarias del SDK y las nuevas características."
hidden: true
noindex: true
---

# Guía de actualización del SDK de iOS 15 {#ios-15-sdk-upgrade-guide}

> Esta guía describe los cambios introducidos en iOS 15 (WWDC21) y los pasos de actualización necesarios para tu integración del SDK de Braze para iOS. Para obtener una lista completa de las nuevas actualizaciones de iOS 15, consulta [las notas de la versión de iOS 15](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes) de Apple.

## Cambios de transparencia en las navegaciones de la interfaz de usuario {#transparency-changes-to-ui-navigations}

Como parte de nuestras pruebas anuales de las betas de iOS, hemos identificado un cambio realizado por Apple que hace que ciertas barras de navegación de la interfaz de usuario aparezcan transparentes en lugar de opacas. Esto será visible en iOS 15 al usar la interfaz de usuario predeterminada de Braze para Content Cards, o cuando se abran vínculos profundos web dentro de tu aplicación en lugar de en una aplicación de navegador independiente.

Para evitar este cambio visual en iOS 15, te recomendamos encarecidamente que actualices a [Braze iOS SDK v4.3.2](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.2) lo antes posible, antes de que los usuarios comiencen a actualizar sus teléfonos al nuevo sistema operativo iOS 15.

## Nueva configuración de notificaciones {#notification-settings}

iOS 15 introdujo nuevas características de notificación para ayudar a los usuarios a mantenerse concentrados y evitar interrupciones frecuentes a lo largo del día. Nos complace ofrecer compatibilidad con estas nuevas características. Estas características no requieren ninguna actualización adicional del SDK y solo se aplicarán a los usuarios de dispositivos iOS 15.

### Modos de enfoque {#focus-mode}

Ahora, los usuarios de iOS 15 pueden crear "modos de enfoque", es decir, perfiles personalizados que se utilizan para determinar qué notificaciones quieren que atraviesen su enfoque y se muestren de forma destacada.

![Los usuarios de iOS 15 ahora pueden crear "modos de enfoque", perfiles personalizados que se utilizan para determinar qué notificaciones quieren que atraviesen su enfoque y se muestren de forma destacada.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

### Niveles de interrupción {#interruption-levels}

En iOS 15, las notificaciones push pueden enviarse con uno de los cuatro niveles de interrupción:

* **Pasivo** (nuevo): sin sonido, sin vibración, sin despertar la pantalla, sin atravesar la configuración de enfoque.
* **Activo** (predeterminado): permite sonido, vibración, activación de la pantalla, sin atravesar la configuración de enfoque.
* **Sensible al tiempo** (nuevo): permite sonido, vibración, activación de la pantalla, puede atravesar los controles del sistema si se permite.
* **Crítico**: permite sonido, vibración, activación de la pantalla, puede atravesar los controles del sistema y anular el interruptor del timbre.

Consulta [Opciones de notificación de iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#interruption-level) para saber más sobre cómo configurar esta opción en las notificaciones push de iOS.

### Resumen de notificaciones {#notification-summary}

![Captura de pantalla relacionada con el resumen de notificaciones.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

En iOS 15, los usuarios pueden (opcionalmente) elegir determinadas horas a lo largo del día para recibir un resumen de las notificaciones. Las notificaciones que no requieran atención inmediata (como las enviadas como "pasivas" o mientras el usuario está en modo de enfoque) se agruparán para evitar interrupciones constantes a lo largo del día.

Para cada notificación que envíes, pronto podrás especificar una "puntuación de relevancia" para controlar qué notificación debe aparecer en la parte superior del resumen.

Consulta [Opciones de notificación de iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#relevance-score) para saber más sobre cómo establecer la "puntuación de relevancia" de una notificación.

## Botones de ubicación {#location-buttons}

iOS 15 introduce una nueva y cómoda forma para que los usuarios concedan temporalmente acceso a la ubicación dentro de una aplicación.

El nuevo botón de ubicación se basa en el permiso existente "Permitir una vez", sin preguntar repetidamente a los usuarios que hacen clic varias veces en la misma sesión.

Para más información, mira el video de Apple [Meet the Location Button](https://developer.apple.com/videos/play/wwdc2021/10102/) de la Conferencia Mundial de Desarrolladores (WWDC) de este año.

{% alert tip %}
Esta característica te da una oportunidad extra de pedir permiso a los usuarios. A los usuarios que hayan rechazado previamente los permisos de ubicación antes de iOS 15 se les mostrará un aviso al hacer clic en el botón de ubicación como una oportunidad para restablecer el permiso desde el estado rechazado por última vez.
{% endalert %}

### Utilizar botones de ubicación con Braze {#using-location-buttons-with-braze}

No es necesaria ninguna integración adicional cuando se utilizan botones de ubicación con Braze. Tu aplicación debe seguir pasando la ubicación del usuario (una vez que haya concedido permiso) como de costumbre.

Según Apple, para los usuarios que ya hayan compartido el acceso a la ubicación en segundo plano, la opción "Mientras se utiliza la aplicación" seguirá concediendo ese nivel de permiso después de que actualicen a iOS 15.

## Apple Mail {#mail}

Este año, Apple ha anunciado muchas actualizaciones sobre el seguimiento del correo electrónico y la privacidad. Para más información, consulta la [entrada de nuestro blog](https://www.braze.com/resources/articles/9-ways-email-marketers-can-respond-to-apples-mail-privacy-protection-feature).

## Ubicación por dirección IP en Safari {#safari-ip-address-location}

En iOS 15, los usuarios podrán configurar Safari para anonimizar o generalizar la ubicación determinada a partir de sus direcciones IP. Ten esto en cuenta al utilizar la segmentación o segmentación basada en la ubicación.