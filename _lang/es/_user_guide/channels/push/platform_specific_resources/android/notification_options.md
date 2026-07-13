---
nav_title: "Opciones de notificación"
article_title: Opciones de notificación de Android
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre varias opciones de notificación de Android y cómo utilizarlas de la mejor manera en Campaigns de Braze."

platform: Android
channel:
  - Push

---

# Opciones de notificación {#notification-options}

> Estas son algunas de las opciones de notificaciones push específicas de Android disponibles a través de Braze.

## Notificaciones silenciosas {#silent-notifications}

Cuando [redactas tu mensaje de notificación push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message?tab=android#step-4-compose-your-push-message), **no puedes** enviar un mensaje push de Android sin un título&#8212;sin embargo, puedes introducir un solo espacio en su lugar. Ten en cuenta que, si tu mensaje solo contiene un espacio, se enviará como una notificación push silenciosa. Para más información, consulta [Notificaciones push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android).

## Grupos de notificaciones {#notification-groups}

Si deseas categorizar tus mensajes y agruparlos en la bandeja de notificaciones de tu usuario, puedes utilizar la característica de canales de notificación de Android a través de Braze.

Primero, crea tu Campaign de push de Android, luego busca en la parte superior de la pestaña **Compose** el desplegable **Notification Channel**.

![Primero, crea tu Campaign de push de Android, luego busca en la parte superior de la pestaña Compose el desplegable Notification Channel.]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

Selecciona tu canal de notificación en el desplegable. También debes seleccionar un canal alternativo en caso de que la configuración de tu canal de notificación falle.

Si no tienes ningún [canal de notificación]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels) listado aquí, puedes añadir uno utilizando el ID del canal de notificación. Ponte en contacto con tus desarrolladores para identificar cuáles son los ID de tus canales de notificación o para crear nuevos ID según sea necesario.

Para añadir un ID de notificación a tu canal de notificación, haz clic en **Manage Notification Channel** en el menú desplegable **Notification Channel** y completa los campos obligatorios. Los canales de notificación deben definirse en la aplicación antes de poder utilizarse en la plataforma Braze.

![Para añadir un ID de notificación a tu canal de notificación, haz clic en Manage Notification Channel en el menú desplegable Notification Channel y completa los campos obligatorios. Los canales de notificación deben definirse en la aplicación antes de poder utilizarse en la plataforma Braze.]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }