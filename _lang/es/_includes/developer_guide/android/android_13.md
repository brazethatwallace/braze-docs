# Actualización a Android 13 {#upgrading-to-android-13}

> En esta guía se describen los cambios relevantes introducidos en Android 13 (2022) y los pasos de actualización necesarios para tu integración del SDK or kit de desarrollo de software para Android de Braze.

Consulta la [documentación para desarrolladores de Android](https://developer.android.com/about/versions/13) 13 para obtener una guía completa de migración.

## SDK or kit de desarrollo de software para Android 13 de Braze {#android-13-braze-sdk}

Para prepararte para Android 13, actualiza tu SDK or kit de desarrollo de software de Braze a la [última versión (v21.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300). Si lo haces, tendrás acceso a nuestra nueva [característica push primer "sin código"]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## Cambios en Android 13 {#changes-in-android-13}

### Permiso de notificaciones push {#push-permission}

Android 13 introduce un [cambio importante](https://developer.android.com/about/versions/13/changes/notification-permission) en la forma en que los usuarios administran las aplicaciones que envían notificaciones push. En Android 13, las aplicaciones deben obtener permisos antes de poder mostrar las notificaciones push.

![Un mensaje push de Android que pregunta "¿Permitir que Kitchenerie te envíe notificaciones?" con dos botones "Permitir" y "No permitir" en la parte inferior del mensaje.]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

Este nuevo permiso sigue un patrón similar al push en iOS y Web, en el que solo tienes un intento para obtener el permiso. Si un usuario elige `Don't Allow` o descarta el mensaje, tu aplicación no podrá solicitar el permiso de nuevo.

Ten en cuenta que las aplicaciones cuentan con una [exención](https://developer.android.com/about/versions/13/changes/notification-permission#eligibility) para los usuarios que previamente tenían las notificaciones push habilitadas antes de actualizar a Android 13. Estos usuarios [seguirán siendo elegibles](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps) para recibir notificaciones push cuando actualicen a Android 13 sin necesidad de solicitar permiso.

#### Momento de la solicitud de permiso {#push-permission-timing}

**Dirigido a Android 13**

Las aplicaciones dirigidas a Android 13 pueden controlar cuándo solicitar el permiso y mostrar el mensaje push nativo.

Si tu usuario actualiza de Android 12 a 13, tu aplicación estaba previamente instalada y ya estabas enviando notificaciones push, el sistema otorga automáticamente el nuevo permiso de notificación a todas las aplicaciones elegibles. En otras palabras, estas aplicaciones pueden seguir enviando notificaciones a los usuarios, y los usuarios no ven una solicitud de permiso en tiempo de ejecución.

Para más detalles, consulta la documentación para desarrolladores de Android sobre los [efectos en las actualizaciones de aplicaciones existentes](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps).

**Dirigido a Android 12 o anterior**

Si tu aplicación aún no está dirigida a Android 13, cuando un nuevo usuario con Android 13 instale tu aplicación, verá automáticamente una solicitud de permiso push cuando tu aplicación cree su primer canal de notificación (a través de `notificationManager.createNotificationChannel`). Los usuarios que ya tienen tu aplicación instalada y luego actualizan a Android 13 nunca verán una solicitud y se les otorgará automáticamente el permiso push.

{% alert note %}
El SDK or kit de desarrollo de software de Braze v23.0.0 crea automáticamente un canal de notificación predeterminado si no existe uno cuando se recibe una notificación push. Si no tienes tu aplicación dirigida a Android 13, esto provocará que se muestre la solicitud de permiso push, que es necesaria para mostrar la notificación.
{% endalert %}

## Preparación para Android 13 {#next-steps}

Se recomienda encarecidamente que tu aplicación se dirija a Android 13 para controlar cuándo se solicita permiso push a los usuarios.

Esto te permitirá optimizar tus [tasas de adhesión voluntaria push](https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps) al solicitar permiso a los usuarios en momentos más apropiados y mejorará la experiencia del usuario en cuanto a cómo y cuándo tu aplicación solicita permiso push.

Para empezar a utilizar nuestra nueva [característica push primer "sin código"]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages), actualiza tu SDK or kit de desarrollo de software de Android a la [última versión (v23.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300).