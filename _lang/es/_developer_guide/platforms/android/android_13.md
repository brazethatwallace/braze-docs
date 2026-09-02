---
nav_title: Actualización a Android 13
article_title: Guía de actualización a Android 13
page_order: 9
platform:
  - Android
  - FireOS
description: "En este artículo se cubren Android 13, actualizaciones del SDK or kit de desarrollo de software, cambios en el permiso de notificaciones push, compatibilidad con el SDK or kit de desarrollo de software y más."
---

# Actualización a Android 13 {#upgrading-to-android-13}

> En esta guía se describen los cambios relevantes introducidos en Android 13 (2022) y los pasos de actualización necesarios para tu integración del SDK or kit de desarrollo de software para Android de Braze.

Consulta la [documentación para desarrolladores de Android 13](https://developer.android.com/about/versions/13) para obtener una guía completa de migración.

## SDK or kit de desarrollo de software para Android 13 de Braze {#android-13-braze-sdk}

Para prepararte para Android 13, actualiza tu SDK or kit de desarrollo de software de Braze a la [última versión (v21.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300). Si lo haces, tendrás acceso a nuestra nueva [característica push primer "sin código"]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages).

## Cambios en Android 13 {#changes-in-android-13}

### Permiso de notificaciones push {#push-permission}

Android 13 introduce un [cambio importante](https://developer.android.com/about/versions/13/changes/notification-permission) en la forma en que los usuarios administran las aplicaciones que envían notificaciones push. En Android 13, las aplicaciones deben obtener permisos antes de poder mostrar las notificaciones push.

![Un mensaje push de Android que pregunta "¿Permitir que Kitchenerie te envíe notificaciones?" con dos botones "Permitir" y "No permitir" en la parte inferior del mensaje.]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

Este nuevo permiso sigue un patrón similar al de iOS y las notificaciones push web, en el que solo tienes un intento para obtener el permiso. Si un usuario elige `Don't Allow` o descarta el aviso, tu aplicación no podrá solicitar el permiso de nuevo.

Ten en cuenta que las aplicaciones reciben una [exención](https://developer.android.com/about/versions/13/changes/notification-permission#eligibility) para los usuarios que previamente tenían habilitadas las notificaciones push antes de actualizar a Android 13. Estos usuarios [seguirán siendo elegibles](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps) para recibir notificaciones push cuando actualicen a Android 13 sin necesidad de solicitar permiso.

#### Momento del aviso de permiso {#push-permission-timing}

**Orientado a Android 13**

Las aplicaciones orientadas a Android 13 pueden controlar cuándo solicitar el permiso y mostrar el aviso push nativo.

Si tu usuario actualiza de Android 12 a 13, tu aplicación estaba previamente instalada y ya estabas enviando notificaciones push, el sistema otorga automáticamente el nuevo permiso de notificación a todas las aplicaciones elegibles. En otras palabras, estas aplicaciones pueden seguir enviando notificaciones a los usuarios, y los usuarios no ven un aviso de permiso en tiempo de ejecución.

Para más detalles, consulta la documentación para desarrolladores de Android sobre los [efectos en las actualizaciones de aplicaciones existentes](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps).

**Orientado a Android 12 o anterior**

Si tu aplicación aún no está orientada a Android 13, cuando un nuevo usuario en Android 13 instale tu aplicación, verá automáticamente un aviso de permiso push cuando tu aplicación cree su primer canal de notificación (a través de `notificationManager.createNotificationChannel`). Los usuarios que ya tienen tu aplicación instalada y luego actualizan a Android 13 nunca ven un aviso y se les otorga automáticamente el permiso push.

{% alert note %}
El SDK or kit de desarrollo de software de Braze v23.0.0 crea automáticamente un canal de notificación predeterminado si aún no existe uno cuando se recibe una notificación push. Si no estás orientado a Android 13, esto provoca que se muestre el aviso de permiso push, que es necesario para mostrar la notificación.
{% endalert %}

## Preparación para Android 13 {#next-steps}

Se recomienda encarecidamente que tu aplicación esté orientada a Android 13 para controlar cuándo se solicita a los usuarios el permiso de notificaciones push.

Orientar tu aplicación a Android 13 te permite optimizar tus [tasas de adhesión voluntaria a push](https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps) solicitando a los usuarios en momentos más apropiados y ofrece una mejor experiencia de usuario en cuanto a cómo y cuándo tu aplicación solicita el permiso push.

Para empezar a usar nuestra nueva [característica push primer "sin código"]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages), actualiza tu SDK or kit de desarrollo de software de Android a la [última versión (v23.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300).