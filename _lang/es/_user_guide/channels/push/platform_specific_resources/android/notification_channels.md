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

Los canales de notificación solo se pueden crear en el código de tu aplicación y no se pueden crear programáticamente en el dashboard de Braze. Recomendamos que tu equipo de ingeniería trabaje con tus especialistas en marketing para asegurar que los canales de notificación deseados se añadan correctamente al dashboard.

A partir del nivel de API 26 (Android O), las notificaciones push requieren un canal válido para mostrarse. Si tu aplicación tiene como objetivo Android O o posterior, debes usar la versión 2.1.0 o posterior de Braze SDK. Tu equipo de desarrollo debe definir los canales que deseas usar, así como la configuración de notificación sugerida (por ejemplo, importancia, sonido, luces) para cada canal en el código de tu aplicación. Para más información, puedes consultar la [documentación para desarrolladores de Android](https://developer.android.com/preview/features/notification-channels.html) y la [documentación para desarrolladores de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels).

{% alert note %}
Android admite la localización de nombres de canales, por lo que en el código de tu aplicación puedes asociar un ID de canal con múltiples traducciones de un nombre de canal.
{% endalert %}

Una vez creados estos canales, tus ingenieros deberán pasar los ID de canal asociados a tu equipo de marketing. Tu equipo debe introducir los nombres de canal y los ID de canal en el dashboard de Braze para usarlos en tus Campaigns y Canvas.

Para añadir un canal al dashboard de Braze, navega al creador de push de Android, selecciona el campo de canales de notificación y luego selecciona "administrar canales".
{% alert important %}
Solo los usuarios con permisos que incluyan "administrar aplicaciones" podrán administrar canales.
{% endalert %}

## Canal predeterminado del SDK {#sdk-default-channel}

Android requiere un canal válido para mostrar notificaciones push en el nivel de API 26 (Android O) o posterior. Braze Android SDK 2.1.0 incluye un canal predeterminado llamado "General", que se creará y usará si no especificas canales adicionales en el dashboard o si intentas enviar a un canal no válido. Puedes renombrar esta etiqueta en el SDK y proporcionar una descripción del canal. Te recomendamos que consideres esto para ofrecer una mejor experiencia de usuario.

Una vez que se añade un canal a tu aplicación, puedes optar por eliminarlo. Sin embargo, los consumidores siempre podrán ver el número de canales que has [eliminado][3]. El dashboard de Braze no incluye soporte para crear canales programáticamente; los canales deben crearse y definirse en el código de tu aplicación para proporcionar una experiencia fluida.

De nuevo, te recomendamos que te coordines con tu equipo de ingeniería para asegurar una transición fluida al targeting de Android O.

## Canal alternativo del dashboard {#dashboard-fallback-channel}

Braze te permite especificar un canal alternativo del dashboard. El propósito del canal alternativo del dashboard es proporcionar un ID de canal para mensajes push heredados sin una selección de canal explícita. Definimos una selección de canal como elegir un canal en nuestro creador de push de Android.

Los mensajes que no tengan un canal seleccionado se enviarán con el ID del canal alternativo del dashboard. Cuando cambies tu canal alternativo del dashboard, cualquier mensaje que no tenga un canal seleccionado explícitamente se enviará con el ID del nuevo canal alternativo.

Aquí tienes un ejemplo del comportamiento esperado del canal alternativo del dashboard:

Tu canal alternativo del dashboard se llama "Marketing" y tienes 10 mensajes push de Android para los que nunca has seleccionado un canal. Estas campañas se envían a través del canal "Marketing" porque el canal "Marketing" es el canal alternativo del dashboard.

Además, tienes 15 mensajes que has seleccionado para enviar a través del canal "Social Notifications" y cinco mensajes que has seleccionado para enviar a través del canal "Marketing".

Luego decides cambiar tu canal predeterminado del dashboard de "Marketing" a "Updates".

En esta situación, las 10 campañas sin selección de canal que anteriormente se enviaban a través del canal "Marketing" ahora se enviarán a través del canal "Updates" porque estos mensajes se envían a través del canal alternativo. Los 15 mensajes que se enviaban a través del canal "Social Notifications" seguirán enviándose a través del canal "Social Notifications". Los cinco mensajes que se enviaban a través del canal "Marketing" seguirán enviándose a través del canal "Marketing".

En caso de que se proporcione un ID de canal no válido a Braze (como si proporcionas un ID de canal que tus desarrolladores no crearon en el SDK), entregaremos la notificación a través de tu canal predeterminado del SDK. Por lo tanto, te recomendamos encarecidamente que pruebes tus canales de notificación a través del dashboard de Braze durante el desarrollo.

Para comprender mejor el comportamiento esperado de los canales, consulta la siguiente tabla:

| Escenario | Resultado |
| ---|-------------
| **Empresa ABC** actualiza a un SDK que admite Android O<br>**Empresa ABC** no añade ningún canal al dashboard de Braze<br>**Empresa ABC** no renombra su canal predeterminado del SDK | Las notificaciones push enviadas a dispositivos Android O crearán un canal llamado "General" y las notificaciones se enviarán a través del canal "General"
| **Empresa XYZ** actualiza a un SDK que admite Android O <br>**Empresa XYZ** no añade ningún canal al dashboard de Braze<br>**Empresa XYZ** renombra su canal predeterminado del SDK a "Marketing" | Las notificaciones push enviadas a dispositivos Android O crearán un canal llamado "Marketing" y las notificaciones se enviarán a través del canal "Marketing"
| **Empresa LMN** actualiza a un SDK que admite Android O <br>**Empresa LMN** define dos canales en el código de su aplicación, "Promotions" y "Order Updates" <br>**Empresa LMN** añade los ID de canal para "Promotions" y "Order Updates" al dashboard de Braze <br>**Empresa LMN** designa "Promotions" como el canal alternativo del dashboard<br>**Empresa LMN** renombra su canal predeterminado del SDK a "Marketing" | Las notificaciones push enviadas a dispositivos Android O no crearán un canal<br><br>A menos que el especialista en marketing especifique explícitamente que las notificaciones deben enviarse a través del canal "Order Updates" o "Marketing", todas las notificaciones creadas antes de que los canales se añadieran al dashboard se enviarán a través del canal "Promotions"<br><br>El canal predeterminado del SDK, "Marketing", solo se crea y usa si la empresa intenta enviar una notificación a través de un ID de canal no válido o si se selecciona explícitamente
| **Empresa HIJ** actualiza a Android O pero no actualiza a Braze Android SDK 2.1.0 o posterior | Las notificaciones enviadas a usuarios con Android O o posterior no aparecen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canal alternativo del dashboard" }

## Añadir canales al dashboard de Braze {#adding-channels-to-the-braze-dashboard}

1. Abre o crea cualquier Campaign o Canvas que incluya un push de Android.
2. Navega al creador de mensajes push de Android.
3. Selecciona **Administrar canales de notificación**. Cualquier canal añadido aquí estará disponible globalmente para todas las Campaigns y Canvas. Debes tener [permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#limited-and-team-role-permissions) de "Administrar aplicaciones" para tu espacio de trabajo para administrar canales.

Cuando aplicas un canal de notificación a una Campaign o paso en Canvas específico, tu recuento de **Usuarios alcanzables** (ubicado en el paso de Público objetivo) para push de Android no parecerá cambiar. Sin embargo, solo los usuarios suscritos al canal de notificación seleccionado verán el mensaje, y los análisis de tu Campaign (como clics) se medirán en función de esta audiencia.

![]({% image_buster /assets/img_archive/push_notification_channels.png %})

{:start="4"}
4. Haz clic en **Añadir canal de notificación**.
5. Introduce el nombre y el ID del canal de notificación que deseas añadir.<br><br>![]({% image_buster /assets/img_archive/push_notifications_channels_manage.png %})<br><br>
6. Repite los pasos 4 y 5 para cada canal de notificación que desees añadir.
7. Pulsa **Guardar** para guardar tus cambios.

## Especificar tu canal alternativo {#specifying-your-fallback-channel}

Tu canal alternativo es el canal que Braze intentará usar para enviar tu mensaje de Android si no has seleccionado un canal para el mensaje. Las únicas Campaigns y Canvas que tendrán mensajes de Android sin una selección de canal son las Campaigns y Canvas que se crearon antes de que tu equipo añadiera canales al dashboard de Braze. Si cambias tu canal alternativo, el cambio se aplicará globalmente a todas las Campaigns y Canvas sin una selección de canal explícita.

1. Abre cualquier Campaign o Canvas existente.
2. Navega al creador de push de Android.
3. Selecciona **Administrar canales de notificación** después de expandir las opciones de canal de notificación.
4. Añade el canal al dashboard (si no se ha añadido ya).
5. Selecciona el botón de radio junto al canal que deseas designar como canal alternativo.
6. Guarda tus cambios. Tus cambios se aplicarán globalmente.

## Añadir canales a tus mensajes push de Android {#adding-channels-to-your-android-push-messages}

1. Navega al creador de push de Android en cualquier Campaign o Canvas.
2. Selecciona el canal que deseas usar en el menú desplegable. Si no tienes un menú desplegable sino la siguiente vista, deberás añadir canales antes de seleccionarlos para las Campaigns.

![Creador de canales de notificación push.]({% image_buster /assets/img_archive/push_notifications_channels_composer.png %})

[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels