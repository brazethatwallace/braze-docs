{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Configurar notificaciones push {#setting-up-push-notifications}

### Paso 1: Completar la configuración inicial {#step-1-complete-the-initial-setup}

{% tabs %}
{% tab Android %}
#### Paso 1.1: Registrarse para push {#step-11-register-for-push}

Regístrate para push utilizando la API de Firebase Cloud Messaging (FCM) de Google. Para un recorrido completo, consulta los siguientes pasos de la [guía de integración push nativa de Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/):

1. [Añadir Firebase a tu proyecto]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-1-add-firebase-to-your-project).
2. [Añadir Cloud Messaging a tus dependencias]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-2-add-cloud-messaging-to-your-dependencies).
3. [Crear una cuenta de servicio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-3-create-a-service-account).
4. [Generar credenciales JSON]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-generate-json-credentials).
5. [Subir tus credenciales JSON a Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-5-upload-your-json-credentials-to-braze).

#### Paso 1.2: Obtener tu ID de remitente de Google {#step-12-get-your-google-sender-id}

Primero, ve a Firebase Console, abre tu proyecto y selecciona <i class="fa-solid fa-gear" aria-label="Configuración"></i>&nbsp;**Settings** > **Project settings**.

![El proyecto de Firebase con el menú "Settings" abierto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Selecciona **Cloud Messaging** y, en **Firebase Cloud Messaging API (V1)**, copia el **Sender ID** a tu portapapeles.

![La página "Cloud Messaging" del proyecto de Firebase con el "Sender ID" resaltado.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

#### Paso 1.3: Actualizar tu `braze.xml` {#step-13-update-your-brazexml}

Añade lo siguiente a tu archivo `braze.xml`. Sustituye `FIREBASE_SENDER_ID` por el ID de remitente que copiaste anteriormente.

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
#### Paso 1.1: Subir certificados de APN {#step-11-upload-apns-certificates}

Genera un certificado del servicio de notificaciones push de Apple (APN) y súbelo al panel de Braze. Para un recorrido completo, consulta [Subir tu certificado de APN]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-upload-your-apns-certificate).

#### Paso 1.2: Añadir compatibilidad con notificaciones push a tu aplicación {#step-12-add-push-notification-support-to-your-app}

Sigue la [guía de integración nativa de iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

{% endtab %}
{% endtabs %}

### Paso 2: Escuchar eventos de notificaciones push (opcional) {#step-2-listen-for-push-notification-events-optional}

Para escuchar eventos de notificaciones push que Braze ha detectado y gestionado, llama a `subscribeToPushNotificationEvents()` y pasa un argumento para ejecutar.

{% alert note %}
Los eventos de notificaciones push de Braze están disponibles tanto en Android como en iOS. Debido a diferencias de plataforma, iOS solo detectará eventos push de Braze cuando un usuario haya interactuado con una notificación.
{% endalert %}

```dart
// Create stream subscription
StreamSubscription pushEventsStreamSubscription;

pushEventsStreamSubscription = braze.subscribeToPushNotificationEvents((BrazePushEvent pushEvent) {
  print("Push Notification event of type ${pushEvent.payloadType} seen. Title ${pushEvent.title}\n and deeplink ${pushEvent.url}");
  // Handle push notification events
});

// Cancel stream subscription
pushEventsStreamSubscription.cancel();
```

#### Campos de eventos de notificaciones push {#push-notification-event-fields}

{% alert note %}
Debido a limitaciones de la plataforma en iOS, el SDK or kit de desarrollo de software de Braze solo puede procesar cargas útiles push mientras la aplicación está en primer plano. Los listeners solo se activarán para el tipo de evento `push_opened` en iOS después de que un usuario haya interactuado con una notificación push.
{% endalert %}

Para una lista completa de los campos de notificaciones push, consulta la siguiente tabla:

| Nombre del campo    | Tipo      | Descripción |
| ------------------ | --------- | ----------- |
| `payloadType`     | String    | Especifica el tipo de carga útil de la notificación. Los dos valores que envía el SDK or kit de desarrollo de software Flutter de Braze son `push_opened` y `push_received`. Solo los eventos `push_opened` son compatibles en iOS. |
| `url`              | String    | Especifica la URL que fue abierta por la notificación. |
| `useWebview`      | Boolean   | Si es `true`, la URL se abre dentro de la aplicación en un webview modal. Si es `false`, la URL se abre en el navegador del dispositivo. |
| `title`            | String    | Representa el título de la notificación. |
| `body`             | String    | Representa el cuerpo o texto de contenido de la notificación. |
| `summaryText`     | String    | Representa el texto de resumen de la notificación. Se mapea desde `subtitle` en iOS. |
| `badgeCount`      | Number   | Representa el recuento de señales de la notificación. |
| `timestamp`        | Number | Representa la hora en que la carga útil fue recibida por la aplicación. |
| `isSilent`        | Boolean   | Si es `true`, la carga útil se recibe de forma silenciosa. Para más detalles sobre el envío de notificaciones push silenciosas en Android, consulta [Notificaciones push silenciosas en Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Para más detalles sobre el envío de notificaciones push silenciosas en iOS, consulta [Notificaciones push silenciosas en iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `isBrazeInternal`| Boolean   | Es `true` si la carga útil de la notificación fue enviada para una característica interna del SDK or kit de desarrollo de software, como la sincronización de conmutadores de características o Uninstall Tracking. La carga útil se recibe de forma silenciosa para el usuario. |
| `imageUrl`        | String    | Especifica la URL asociada con la imagen de la notificación. |
| `brazeProperties` | Object    | Representa las propiedades de Braze asociadas con la Campaign (pares clave-valor). |
| `ios`              | Object    | Representa campos específicos de iOS. |
| `android`          | Object    | Representa campos específicos de Android. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos de eventos de notificaciones push" }

### Paso 3: Probar la visualización de notificaciones push {#step-3-test-displaying-push-notifications}

Para probar tu integración después de configurar las notificaciones push en la capa nativa:

1. Establece un usuario activo en la aplicación Flutter. Para ello, inicializa tu plugin llamando a `braze.changeUser('your-user-id')`.
2. Ve a **Campaigns** y crea una nueva Campaign de notificación push. Elige las plataformas que deseas probar.
3. Redacta tu notificación de prueba y ve a la pestaña **Test**. Añade el mismo `user-id` como usuario de prueba y haz clic en **Send Test**.
4. Deberías recibir la notificación en tu dispositivo en breve. Es posible que necesites revisar el centro de notificaciones o actualizar la configuración si no se muestra.

{% alert tip %}
A partir de Xcode 14, puedes probar notificaciones push remotas en un simulador de iOS.
{% endalert %}

### Paso 4: Añadir vínculos profundos (Android) {#step-4-add-deep-links-android}

{% alert warning %}
En Android, `com_braze_handle_push_deep_links_automatically` tiene como valor predeterminado `false`. Con el valor predeterminado, al tocar una notificación push se envía un evento `push_opened` a tu listener de Dart, pero el SDK or kit de desarrollo de software nativo no lleva tu aplicación al primer plano ni abre el destino del vínculo profundo automáticamente. Si tu aplicación no se abre al tocar una notificación, esta opción es la causa más probable.
{% endalert %}

Para habilitar que Braze abra automáticamente tu aplicación y cualquier vínculo profundo cuando se toque una notificación push, establece `com_braze_handle_push_deep_links_automatically` en `true` en tu `braze.xml`:

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Esta opción también se puede establecer mediante [configuración en tiempo de ejecución]({{site.baseurl}}/developer_guide/sdk_integration#android_runtime-configuration) en tu código nativo de Android:

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build()
Braze.configure(this, brazeConfig)
```

Si prefieres gestionar los vínculos profundos de forma personalizada, utiliza el listener `subscribeToPushNotificationEvents()` descrito en el paso 2 para enrutar el campo `url` del evento `push_opened` tú mismo. Para más información, consulta [Vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=flutter).