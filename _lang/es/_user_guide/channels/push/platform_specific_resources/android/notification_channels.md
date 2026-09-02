---
nav_title: "Canales de notificación"
article_title: Canales de notificación push
page_order: 4
page_type: reference
description: "Este artículo de referencia cubre temas sobre los canales de notificación push de Android, como la transición a Android O, cómo añadir un canal a Braze, configurar un canal alternativo y más."
platform: Android
channel:
  - push
---

# Canales de notificación {#notification-channels}

> Los [canales de notificación](https://www.braze.com/blog/android-o-push-notifications-channels/) son una forma de organizar las notificaciones push que se añadieron con Android O. A partir de O, todas las notificaciones push deben tener un canal de notificación que indique el tipo de mensaje (por ejemplo, "notificaciones de chat" o "notificaciones de seguimiento"). Tus usuarios pueden entonces controlar aspectos de sus notificaciones (por ejemplo, posponer, configuración de sonido/vibración o desactivar, etc.) en función de los canales individuales.

Los canales de notificación solo se pueden crear en el código de tu aplicación y no se pueden crear programáticamente en el panel de Braze. Recomendamos que tu equipo de ingeniería trabaje con tus especialistas en marketing para asegurar que los canales de notificación deseados se añadan correctamente al panel.

A partir del nivel de API 26 (Android O), las notificaciones push requieren un canal válido para mostrarse. Si tu aplicación tiene como objetivo Android O o posterior, debes usar la versión 2.1.0 o posterior de Braze SDK or kit de desarrollo de software. Tu equipo de desarrollo debe definir los canales que deseas usar, así como la configuración de notificación sugerida (por ejemplo, importancia, sonido, luces) para cada canal en el código de tu aplicación. Para más información, puedes consultar la [documentación para desarrolladores de Android](https://developer.android.com/preview/features/notification-channels.html) y la [documentación para desarrolladores de Braze]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android).

{% alert note %}
Android admite la localización de nombres de canales, por lo que en el código de tu aplicación puedes asociar un ID de canal con múltiples traducciones de un nombre de canal.
{% endalert %}

Una vez creados estos canales, tus ingenieros deberán pasar los ID de canal asociados a tu equipo de marketing. Tu equipo debe introducir los nombres de canal y los ID de canal en el panel de Braze para usarlos en tus Campaigns y Canvas.

Para añadir un canal al panel de Braze, ve al creador de push de Android, selecciona el campo de canales de notificación y luego selecciona **Administrar canales**.
{% alert important %}
Solo los usuarios con permisos que incluyan "administrar aplicaciones" podrán administrar canales.
{% endalert %}

## Canal predeterminado del SDK or kit de desarrollo de software {#sdk-default-channel}

Android requiere un canal válido para mostrar notificaciones push en el nivel de API 26 (Android O) o posterior. Braze Android SDK or kit de desarrollo de software 2.1.0 incluye un canal predeterminado llamado "General", que se creará y utilizará si no especificas canales adicionales en el panel o si intentas enviar a un canal no válido. Puedes renombrar esta etiqueta en el SDK or kit de desarrollo de software y proporcionar una descripción del canal. Te recomendamos que lo consideres para ofrecer una mejor experiencia de usuario.

Una vez que se añade un canal a tu aplicación, puedes optar por eliminarlo. Sin embargo, los consumidores siempre podrán ver el número de canales que hayas [eliminado].[3] El panel de Braze no incluye soporte para la creación programática de canales: los canales deben crearse y definirse en el código de tu aplicación para proporcionar una experiencia fluida.

De nuevo, te recomendamos que te coordines con tu equipo de ingeniería para asegurar una transición fluida a la segmentación de Android O.

## Canal alternativo del panel {#dashboard-fallback-channel}

Braze te permite especificar un canal alternativo del panel. El propósito del canal alternativo del panel es proporcionar un ID de canal para los mensajes push heredados que no tienen una selección de canal explícita. Definimos una selección de canal como la acción de elegir un canal en nuestro creador de notificaciones push de Android.

Los mensajes que no tengan un canal seleccionado se enviarán con el ID del canal alternativo del panel. Cuando cambias tu canal alternativo del panel, cualquier mensaje que no tenga un canal seleccionado explícitamente se enviará con el ID del nuevo canal alternativo.

Este es un ejemplo del comportamiento esperado del canal alternativo del panel:

Tu canal alternativo del panel se llama "Marketing" y tienes 10 mensajes push de Android para los que nunca seleccionaste un canal. Estas campañas se envían a través del canal "Marketing" porque el canal "Marketing" es el canal alternativo del panel.

Además, tienes 15 mensajes que seleccionaste para enviar a través del canal "Social Notifications" y cinco mensajes que seleccionaste para enviar a través del canal "Marketing".

Luego decides cambiar tu canal predeterminado del panel de "Marketing" a "Updates".

En esta situación, las 10 campañas sin selección de canal que se enviaban anteriormente a través del canal "Marketing" ahora se enviarán a través del canal "Updates" porque estos mensajes se envían a través del canal alternativo. Los 15 mensajes que se enviaban a través del canal "Social Notifications" seguirán enviándose a través del canal "Social Notifications". Los cinco mensajes que se enviaban a través del canal "Marketing" seguirán enviándose a través del canal "Marketing".

En el caso de que se proporcione a Braze un ID de canal no válido (por ejemplo, si proporcionas un ID de canal que tus desarrolladores no crearon en el SDK or kit de desarrollo de software), entregaremos la notificación a través de tu canal predeterminado del SDK or kit de desarrollo de software. Por lo tanto, te recomendamos encarecidamente que pruebes tus canales de notificación en el panel de Braze durante el desarrollo.

Para comprender mejor el comportamiento esperado de los canales, consulta la siguiente tabla:

| Escenario | Resultado |
| --- | --- |
| **Company ABC** actualiza a un SDK or kit de desarrollo de software que es compatible con Android O<br>**Company ABC** no añade ningún canal al panel de Braze<br>**Company ABC** no cambia el nombre de su canal predeterminado del SDK or kit de desarrollo de software | Las notificaciones push enviadas a dispositivos Android O crearán un canal llamado "General" y las notificaciones se enviarán a través del canal "General" |
| **Company XYZ** actualiza a un SDK or kit de desarrollo de software que es compatible con Android O<br>**Company XYZ** no añade ningún canal al panel de Braze<br>**Company XYZ** cambia el nombre de su canal predeterminado del SDK or kit de desarrollo de software a "Marketing" | Las notificaciones push enviadas a dispositivos Android O crearán un canal llamado "Marketing" y las notificaciones se enviarán a través del canal "Marketing" |
| **Company LMN** actualiza a un SDK or kit de desarrollo de software que es compatible con Android O<br>**Company LMN** define dos canales en el código de su aplicación, "Promotions" y "Order Updates"<br>**Company LMN** añade los ID de canal para "Promotions" y "Order Updates" al panel de Braze<br>**Company LMN** designa "Promotions" como el canal alternativo del panel<br>**Company LMN** cambia el nombre de su canal predeterminado del SDK or kit de desarrollo de software a "Marketing" | Las notificaciones push enviadas a dispositivos Android O no crearán un canal<br><br>A menos que el especialista en marketing especifique explícitamente que las notificaciones deben enviarse a través del canal "Order Updates" o "Marketing", todas las notificaciones creadas antes de que los canales se añadieran al panel se enviarán a través del canal "Promotions"<br><br>El canal predeterminado del SDK or kit de desarrollo de software, "Marketing", solo se crea y se usa si la empresa intenta enviar una notificación a través de un ID de canal no válido o si se selecciona explícitamente |
| **Company HIJ** actualiza a Android O pero no actualiza a la versión 2.1.0 o posterior del SDK or kit de desarrollo de software de Android de Braze | Las notificaciones enviadas a usuarios con Android O o posterior no aparecen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canal alternativo del panel" }

## Agregar canales al panel de Braze {#adding-channels-to-the-braze-dashboard}

1. Abre o crea cualquier Campaign o Canvas que incluya un push de Android.
2. Navega al creador de mensajes push de Android.
3. Selecciona **Manage Notification Channels**. Todos los canales añadidos aquí estarán disponibles globalmente para todas las Campaigns y Canvas. Debes tener [permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) de "Manage Apps" en tu espacio de trabajo para gestionar canales.

Cuando aplicas un canal de notificación a una Campaign o paso en Canvas específico, el recuento de **Usuarios alcanzables** (ubicado en el paso de público objetivo) para push de Android no parecerá cambiar. Sin embargo, solo los usuarios suscritos al canal de notificación seleccionado verán el mensaje, y los análisis de tu Campaign (como clics) se medirán en función de esta audiencia.

![Creador de push de Android con Manage Notification Channels y una lista de canales configurados.]({% image_buster /assets/img_archive/push_notification_channels.png %})

{:start="4"}
4. Selecciona **Add Notification Channel**.
5. Introduce el nombre y el ID del canal de notificación que deseas agregar.<br><br>![Diálogo de Add Notification Channel con campos para el nombre del canal y el ID del canal.]({% image_buster /assets/img_archive/push_notifications_channels_manage.png %})<br><br>
6. Repite los pasos 4 y 5 para cada canal de notificación que desees agregar.
7. Selecciona **Save** para guardar los cambios.

## Especificar tu canal alternativo {#specifying-your-fallback-channel}

Tu canal alternativo es el canal que Braze intentará utilizar para enviar tu mensaje de Android si no has seleccionado un canal para el mensaje. Las únicas Campaigns y Canvas que tendrán mensajes de Android sin una selección de canal son las Campaigns y Canvas que se crearon antes de que tu equipo añadiera canales al panel de Braze. Si cambias tu canal alternativo, el cambio se aplicará globalmente a todas las Campaigns y Canvas sin una selección de canal explícita.

1. Abre cualquier Campaign o Canvas existente.
2. Navega al creador de notificaciones push de Android.
3. Selecciona **Manage Notification Channels** después de expandir las opciones de canal de notificación.
4. Añade el canal al panel (si no se ha añadido ya).
5. Selecciona el botón de opción junto al canal que deseas designar como canal alternativo.
6. Guarda tus cambios. Tus cambios se aplicarán globalmente.

## Agregar canales a tus mensajes push de Android {#adding-channels-to-your-android-push-messages}

1. Ve al creador de push de Android en cualquier Campaign o Canvas.
2. Selecciona el canal que deseas usar en el menú desplegable. Si no ves un menú desplegable y en su lugar ves la siguiente vista, tendrás que agregar canales antes de seleccionarlos para Campaigns.

![Creador de canales de notificaciones push.]({% image_buster /assets/img_archive/push_notifications_channels_composer.png %})

[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels