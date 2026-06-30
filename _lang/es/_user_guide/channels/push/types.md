---
nav_title: "Tipos de mensaje"
article_title: Tipos de mensajes push
page_order: 3
page_type: reference
description: "Este artículo de referencia enumera los diferentes tipos de notificaciones push que puedes enviar con Braze."
channel: push
---

# Tipos de mensajes push {#push-message-types}

> Existen muchos tipos de notificaciones push que puedes utilizar para interactuar con tus clientes. Puedes configurar la mayoría de estos ajustes en tus campañas push, pero algunos requieren configuraciones de backend como se indica en las descripciones.

## Push estándar {#standard-push}

El mensaje push general. Estos aparecen en el dispositivo de tu usuario con un sonido de notificación y un mensaje que se desliza o aparece en una barra o pila de notificaciones.

**Compatible con:** Web, Android, iOS

Para más información, consulta [Crear un mensaje push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message).

## Notificación push web {#web-push}

Estos mensajes push aparecen en aplicaciones web o navegadores. Requieren permiso para llegar al cliente. Las notificaciones push web no funcionan si el usuario está utilizando un navegador oculto.

**Compatible con:** Web

Para más información, consulta [Notificaciones push web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web).

## Campañas de push primer {#push-primer-campaigns}

Campañas de mensajes dentro de la aplicación utilizadas para obtener una señal explícita de adhesión voluntaria o rechazo de push por parte de los usuarios. A través del primer, puedes evitar enviar notificaciones a usuarios que probablemente desactivarían las notificaciones push a través de la configuración del dispositivo. Para iOS, las campañas push son relevantes ya que las notificaciones push en primer plano (como las notificaciones que activan el dispositivo) no se habilitan hasta que un usuario acepta explícitamente el aviso nativo de push de iOS.

**Compatible con:** Web, Android, iOS

Para más información, consulta [Mensajes dentro de la aplicación de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## Push Stories

Push Stories son mensajes inmersivos que llevan a tu usuario a través de un recorrido visual en forma de carrusel. Están disponibles solo para dispositivos móviles.

**Compatible con:** iOS, Android

Para más información, consulta [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories).

## Push con botones de acción {#push-with-action-buttons}

Las notificaciones push con botones de acción son mensajes que te permiten ofrecer opciones a tus usuarios y proporcionar varias llamadas a la acción.

**Compatible con:** Web, Android, iOS

Para más información, consulta [Botones de acción para notificación push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons).

## Notificaciones push enriquecidas {#rich-push-notifications}

Las notificaciones push enriquecidas son notificaciones con imágenes inmersivas y contenido creativo que pueden expandirse más allá de un icono y un texto de llamada a la acción.

**Compatible con:** iOS, Android

Para más información, consulta [Crear notificaciones enriquecidas para iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications) o [Crear notificaciones enriquecidas para Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications).

## Notificaciones push provisionales para iOS {#provisional-push-notifications-for-ios}

Introducidas por Apple en iOS 12, la autorización provisional ocurre automáticamente durante la instalación de aplicaciones iOS, lo que permite a las marcas enviar notificaciones silenciosas sin mostrar un aviso de push a los usuarios. Cuando la notificación push silenciosa se envía y se visualiza en la bandeja de notificaciones del dispositivo, los usuarios tienen la opción de permitir o interrumpir las notificaciones push.

**Compatible con:** iOS

Para más información, consulta [Opciones de notificación de iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#provisional-push).

## Notificaciones push HTML {#html-push-notifications}

Las notificaciones push HTML son mensajes push codificados directamente en HTML y no utilizan las plantillas push predefinidas que proporciona Braze. Tener la opción de crear notificaciones push HTML permite a tu empresa tener total libertad creativa y una imagen de marca consistente en cuanto a la apariencia de estos mensajes push.

**Compatible con:** Android

## ID de notificación e ID de canal {#notification-ids-and-channel-ids}

Los ID de notificación y los ID de canal te permiten reemplazar o actualizar notificaciones push ya recibidas, pero no abiertas, por el usuario.

**Compatible con:** iOS, Android

Para más información, consulta [Canales de notificación]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels) y [Configuración avanzada de campañas push]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings).

## Notificaciones push en segundo plano o silenciosas {#background-push-notifications}

Notificaciones push que no se muestran en el dispositivo. Generalmente se utilizan para enviar paquetes de información a la aplicación para procesos en segundo plano y Uninstall Tracking. Se requiere un token de push habilitado para segundo plano para enviar una notificación push en segundo plano o silenciosa.

**Compatible con:** Web, Android, iOS

Para más información, consulta [Notificaciones push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent).

## Notificaciones push para dispositivos wearable {#wearable-push-notifications}

Estas notificaciones push permiten a las marcas enviar mensajes directamente a dispositivos wearable como el Apple Watch.

**Compatible con:** iOS