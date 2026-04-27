{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

{% alert note %}
Esta guía de implementación se centra en una implementación Swift, pero se proporcionan fragmentos de código Objective-C para los interesados.
{% endalert %}

## Extensiones de la aplicación de contenido de notificación {#notification-content-app-extensions}

![Dos mensajes push mostrados uno al lado del otro. El mensaje de la izquierda muestra el aspecto de un push con la interfaz predeterminada. El mensaje de la derecha muestra un push de una tarjeta perforada de café realizado mediante la implementación de una interfaz de usuario push personalizada.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

Las extensiones de la aplicación de contenido de notificación te ofrecen una gran opción para personalizar las notificaciones push. Las extensiones de aplicación de contenido de notificación muestran una interfaz personalizada para las notificaciones de tu aplicación cuando se expande una notificación push.

Las notificaciones push se pueden ampliar de tres formas distintas:
- Una pulsación larga en el banner push
- Deslizar hacia abajo el banner push
- Deslizar el banner hacia la izquierda y seleccionar "Ver"

Estas vistas personalizadas ofrecen formas inteligentes de interactuar con los clientes mostrando distintos tipos de contenido, como notificaciones interactivas, notificaciones rellenadas con datos de usuario e incluso mensajes push que pueden capturar información como números de teléfono y correo electrónico. Una de nuestras características más conocidas en Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), es un excelente ejemplo de cómo puede ser una extensión de aplicación de contenido de notificación push.

### Requisitos {#requirements}

![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) integradas con éxito en tu aplicación
- Los siguientes archivos generados por Xcode en función de tu lenguaje de codificación:

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## Notificación push interactiva {#interactive-push-notification}

Las notificaciones push pueden responder a acciones del usuario dentro de una extensión de aplicación de contenido. Para los usuarios con iOS 12 o posterior, esto significa que puedes convertir tus notificaciones push en mensajes totalmente interactivos. Esto proporciona una opción interesante para introducir interactividad en tus promociones y aplicaciones. Por ejemplo, tu notificación push puede incluir un juego para que jueguen los usuarios, una ruleta para ganar descuentos o un botón "me gusta" para guardar un anuncio o una canción.

El siguiente ejemplo muestra una notificación push en la que los usuarios pueden jugar a un juego de correspondencias dentro de la notificación expandida.

![Un diagrama de cómo podrían ser las fases de una notificación push interactiva. Una secuencia muestra a un usuario pulsando en una notificación push que muestra un juego de correspondencias interactivo.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### Configuración del dashboard {#dashboard-configuration}

Para crear una notificación push interactiva, debes establecer una vista personalizada en tu dashboard.

1. En la página **Campaigns**, haz clic en **Create Campaign** para iniciar una nueva campaña de notificaciones push.
2. En la pestaña **Compose**, activa **Notification Buttons**.
3. Introduce una categoría iOS personalizada en el campo **iOS Notification Category**.
4. En el `.plist` de tu objetivo de extensión de contenido de notificación, establece el atributo `UNNotificationExtensionCategory` en tu categoría personalizada de iOS. El valor proporcionado aquí debe coincidir con lo establecido en el panel de Braze en **iOS Notification Category**.
5. Establece la clave `UNNotificationExtensionInteractionEnabled` en `true` para habilitar las interacciones del usuario en una notificación push.

![Las opciones del botón de notificación que se encuentran en la configuración del creador de mensajes push.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## Notificaciones push personalizadas {#personalized-push-notifications}

![Dos iPhones mostrados uno al lado del otro. El primer iPhone muestra la vista no expandida del mensaje push. El segundo iPhone muestra la versión expandida del mensaje push mostrando una imagen del "progreso" que llevan en un curso, el nombre de la siguiente sesión y cuándo debe completarse.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Las notificaciones push pueden mostrar información específica del usuario dentro de una extensión de contenido. Esto te permite crear contenido push centrado en el usuario, como añadir la opción de compartir tu progreso en distintas plataformas, mostrar logros desbloqueados o mostrar listas de control de incorporación. Este ejemplo muestra una notificación push mostrada a un usuario después de que haya completado una tarea específica en el curso de Braze Learning. Al expandir la notificación, el usuario puede ver su progreso a través de su ruta de aprendizaje. La información proporcionada aquí es específica del usuario y puede dispararse cuando se completa una sesión o se realiza una acción específica del usuario aprovechando un desencadenante de la API.

### Configuración del dashboard {#dashboard-configuration-1}

Para crear una notificación push personalizada, debes establecer una vista personalizada en tu dashboard.

1. En la página **Campaigns**, haz clic en **Create Campaign** para iniciar una nueva campaña de notificaciones push.
2. En la pestaña **Compose**, activa **Notification Buttons**.
3. Introduce una categoría iOS personalizada en el campo **iOS Notification Category**.
4. En la pestaña **Settings**, crea pares clave-valor utilizando Liquid estándar. Configura los atributos de usuario adecuados que quieres que muestre el mensaje. Estas vistas pueden personalizarse en función de atributos específicos de un perfil de usuario concreto.
5. En el `.plist` de tu objetivo de extensión de contenido de notificación, establece el atributo `UNNotificationExtensionCategory` en tu categoría personalizada de iOS. El valor proporcionado aquí debe coincidir con lo establecido en el panel de Braze en **iOS Notification Category**.

![Cuatro conjuntos de pares clave-valor, en los que "next_session_name" y "next_session_complete_date" se configuran como una propiedad desencadenante de la API mediante Liquid, y "completed_session count" y "total_session_count" se configuran como un atributo personalizado del usuario mediante Liquid.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### Manejo de pares clave-valor {#handling-key-value-pairs}

Se llama al método `didReceive` cuando la extensión de la aplicación de contenido de notificación ha recibido una notificación. Este método se encuentra en `NotificationViewController`. Los pares clave-valor proporcionados en el dashboard se representan en el código mediante el uso de un diccionario `userInfo`.

#### Análisis sintáctico de los pares clave-valor de las notificaciones push {#parsing-key-value-pairs-from-push-notifications}

{% tabs %}
{% tab Swift %}
``` swift
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo

  guard let value = userInfo["YOUR-KEY-VALUE-PAIR"] as? String,
        let otherValue = userInfo["YOUR-OTHER-KEY-VALUE-PAIR"] as? String,
  else { fatalError("Key-Value Pairs are incorrect.")}

  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;

  if (userInfo[@"YOUR-KEY-VALUE-PAIR"] && userInfo[@"YOUR-OTHER-KEY-VALUE-PAIR"]) {

  ...

  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```
{% endtab %}
{% endtabs %}

## Notificación push de captura de información {#information-capture-push-notification}

Las notificaciones push pueden capturar información del usuario dentro de una extensión de aplicación de contenido, ampliando los límites de lo que es posible con un push. Solicitar la entrada del usuario a través de notificaciones push te permite no solo solicitar información básica como el nombre o el correo electrónico, sino también pedir a los usuarios que envíen comentarios o completen un perfil de usuario inacabado.

{% alert tip %}
Para más información, consulta [Registrar datos de notificaciones push]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications/).
{% endalert %}

En el siguiente flujo, la vista personalizada es capaz de responder a los cambios de estado. Esos componentes de cambio de estado están representados en cada imagen.

1. El usuario recibe una notificación push.
2. Se abre el push. Una vez expandido, el push solicita información al usuario. En este ejemplo, se solicita la dirección de correo electrónico del usuario, pero podrías solicitar cualquier tipo de información.
3. Se proporciona la información y, si está en el formato esperado, se muestra el botón de registro.
3. Se muestra la vista de confirmación y se descarta la notificación push.

![]({% image_buster /assets/img/push_implementation_guide/push8.png %}){: style="border:0;"}

### Configuración del dashboard {#dashboard-configuration-2}

Para crear una notificación push de captura de información, debes establecer una vista personalizada en tu dashboard.

1. En la página **Campaigns**, haz clic en **Create Campaign** para iniciar una nueva campaña de notificaciones push.
2. En la pestaña **Compose**, activa **Notification Buttons**.
3. Introduce una categoría iOS personalizada en el campo **iOS Notification Category**.
4. En la pestaña **Settings**, crea pares clave-valor utilizando Liquid estándar. Configura los atributos de usuario adecuados que quieres que muestre el mensaje.
5. En el `.plist` de tu objetivo de extensión de contenido de notificación, establece el atributo `UNNotificationExtensionCategory` en tu categoría personalizada de iOS. El valor proporcionado aquí debe coincidir con lo establecido en el panel de Braze en **iOS Notification Category**.

Como se ve en el ejemplo, también puedes incluir una imagen en tu notificación push. Para ello, debes integrar [notificaciones enriquecidas]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift), establecer el estilo de notificación de tu campaña en notificación enriquecida e incluir una imagen de notificación push enriquecida.

![Un mensaje push con tres conjuntos de pares clave-valor. 1. "Braze_id" configurado como llamada Liquid para recuperar el ID de Braze. 2. "cert_title" configurado como "Braze Marketer Certification". 3. "Cert_description" configurado como "Certified Braze marketers drive...".]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### Manejar las acciones de los botones {#handling-button-actions}

Cada botón de acción tiene un identificador único. El código comprueba si tu identificador de respuesta es igual al `actionIdentifier`, y si es así, sabe que el usuario hizo clic en el botón de acción.

**Manejar las respuestas del botón de acción de notificaciones push**<br>

{% tabs %}
{% tab Swift %}
``` swift
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  if response.actionIdentifier == "YOUR-REGISTER-IDENTIFIER" {
    // do something
  } else {
    // do something else
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier isEqualToString:@"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }
}
```
{% endtab %}
{% endtabs %}

### Descartar notificaciones push {#dismissing-pushes}

Las notificaciones push pueden descartarse automáticamente al pulsar un botón de acción. Hay tres opciones predefinidas de descarte push que recomendamos:

1. `completion(.dismiss)` - Descarta la notificación
2. `completion(.doNotDismiss)` - La notificación permanece abierta
3. `completion(.dismissAndForward)` - Se descarta el push y el usuario es redirigido a la aplicación