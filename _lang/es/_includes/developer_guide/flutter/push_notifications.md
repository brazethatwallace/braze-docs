{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Configuración de las notificaciones push {#setting-up-push-notifications}

### Paso 1: Completa la configuración inicial {#step-1-complete-the-initial-setup}

{% tabs %}
{% tab Android %}
#### Paso 1.1: Registro para push {#step-11-register-for-push}

Regístrate para recibir mensajes push mediante la API Firebase Cloud Messaging (FCM) de Google. Para una guía completa, consulta los siguientes pasos de la [guía de integración push para Android nativo]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/):

1. [Añade Firebase a tu proyecto]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [Añade Cloud Messaging a tus dependencias]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [Crea una cuenta de servicio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [Genera credenciales JSON]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [Carga tus credenciales JSON en Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

#### Paso 1.2: Obtén tu ID de remitente de Google {#step-12-get-your-google-sender-id}

Primero, ve a la consola de Firebase, abre tu proyecto y selecciona <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **Project settings**.

![El proyecto Firebase con el menú "Settings" abierto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Selecciona **Cloud Messaging** y, a continuación, en **Firebase Cloud Messaging API (V1)**, copia el **Sender ID** en el portapapeles.

![La página "Cloud Messaging" del proyecto Firebase con el "Sender ID" resaltado.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

#### Paso 1.3: Actualiza tu `braze.xml` {#step-13-update-your-brazexml}

Añade lo siguiente a tu archivo `braze.xml`. Sustituye `FIREBASE_SENDER_ID` por el ID de remitente que copiaste anteriormente.

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
#### Paso 1.1: Carga los certificados de APN {#step-11-upload-apns-certificates}

Genera un certificado del servicio de notificaciones push de Apple (APN) y cárgalo en el panel de Braze. Para una guía completa, consulta [Cargar tu certificado de APN]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate).

#### Paso 1.2: Añade compatibilidad con notificaciones push a tu aplicación {#step-12-add-push-notification-support-to-your-app}

Sigue la [guía de integración nativa de iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

{% endtab %}
{% endtabs %}

### Paso 2: Escuchar eventos de notificación push (opcional) {#step-2-listen-for-push-notification-events-optional}

Para escuchar los eventos de notificación push que Braze ha detectado y gestionado, llama a `subscribeToPushNotificationEvents()` y pasa un argumento para ejecutar.

{% alert note %}
Los eventos de notificación push de Braze están disponibles tanto en Android como en iOS. Debido a las diferencias de plataforma, iOS solo detectará los eventos push de Braze cuando un usuario haya interactuado con una notificación.
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

##### Campos de evento de notificación push {#push-notification-event-fields}

{% alert note %}
Debido a las limitaciones de la plataforma en iOS, el SDK de Braze solo puede procesar cargas útiles push mientras la aplicación está en primer plano. Los listeners solo se activarán para el tipo de evento `push_opened` en iOS después de que un usuario haya interactuado con un push.
{% endalert %}

Para obtener una lista completa de los campos de notificación push, consulta la tabla siguiente:

| Nombre del campo | Tipo | Descripción |
| ------------------ | --------- | ----------- |
| `payloadType` | Cadena | Especifica el tipo de carga útil de la notificación. Los dos valores que se envían desde el SDK Flutter de Braze son `push_opened` y `push_received`. En iOS solo se admiten eventos de `push_opened`. |
| `url` | Cadena | Especifica la URL abierta por la notificación. |
| `useWebview` | Booleano | Si `true`, la URL se abrirá dentro de la aplicación en una vista web modal. Si `false`, la URL se abrirá en el navegador del dispositivo. |
| `title` | Cadena | Representa el título de la notificación. |
| `body` | Cadena | Representa el cuerpo o texto del contenido de la notificación. |
| `summaryText` | Cadena | Representa el texto resumido de la notificación. Está mapeado desde `subtitle` en iOS. |
| `badgeCount` | Número | Representa el recuento de señales de la notificación. |
| `timestamp` | Número | Representa la hora a la que la aplicación recibió la carga útil. |
| `isSilent` | Booleano | Si `true`, la carga útil se recibe en silencio. Para más detalles sobre el envío de notificaciones push silenciosas en Android, consulta [Notificaciones push silenciosas en Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Para más detalles sobre el envío de notificaciones push silenciosas en iOS, consulta [Notificaciones push silenciosas en iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `isBrazeInternal` | Booleano | Esto será `true` si se envió una carga útil de notificación para una función interna del SDK, como la sincronización de conmutadores de características o Uninstall Tracking. La carga útil se recibe de forma silenciosa para el usuario. |
| `imageUrl` | Cadena | Especifica la URL asociada a la imagen de notificación. |
| `brazeProperties` | Objeto | Representa las propiedades de Braze asociadas a la campaña (pares clave-valor). |
| `ios` | Objeto | Representa campos específicos de iOS. |
| `android` | Objeto | Representa campos específicos de Android. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push notification event fields" }

### Paso 3: Prueba de visualización de notificaciones push {#step-3-test-displaying-push-notifications}

Para probar tu integración después de configurar las notificaciones push en la capa nativa:

1. Configura un usuario activo en la aplicación Flutter. Para ello, inicializa tu plugin llamando a `braze.changeUser('your-user-id')`.
2. Ve a **Campaigns** y crea una nueva Campaign de notificación push. Elige las plataformas que deseas probar.
3. Redacta tu notificación de prueba y dirígete a la pestaña **Test**. Añade el mismo `user-id` que el usuario de prueba y haz clic en **Send Test**.
4. En breve recibirás la notificación en tu dispositivo. Puede que tengas que comprobarlo en el centro de notificaciones o actualizar la configuración si no se muestra.

{% alert tip %}
A partir de Xcode 14, puedes probar las notificaciones push remotas en un simulador de iOS.
{% endalert %}