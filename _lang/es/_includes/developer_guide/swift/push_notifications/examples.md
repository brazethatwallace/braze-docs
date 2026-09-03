{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

{% alert note %}
Esta guía de implementación se centra en una implementación Swift, pero se proporcionan fragmentos de código Objective-C para los interesados.
{% endalert %}

## Extensiones de contenido de notificación de la aplicación {#notification-content-app-extensions}

![Dos mensajes push mostrados uno al lado del otro. El mensaje de la izquierda muestra cómo se ve un push con la interfaz predeterminada. El mensaje de la derecha muestra un push de tarjeta de sellos de café creado al implementar una interfaz push personalizada.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

Las extensiones de contenido de notificación de la aplicación te ofrecen una excelente opción para personalizar las notificaciones push. Las extensiones de contenido de notificación de la aplicación muestran una interfaz personalizada para las notificaciones de tu aplicación cuando se expande una notificación push.

Las notificaciones push se pueden expandir de tres maneras diferentes:
- Manteniendo presionado el banner de push
- Deslizando hacia abajo en el banner de push
- Deslizando el banner horizontalmente y seleccionando "Ver"

Estas vistas personalizadas ofrecen formas inteligentes de interactuar con los clientes mostrando tipos distintos de contenido, incluyendo notificaciones interactivas, notificaciones con datos de usuario e incluso mensajes push que pueden capturar información como números de teléfono y correos electrónicos. Una de nuestras características más conocidas en Braze, [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories), es un ejemplo perfecto de cómo puede verse una extensión de contenido de notificación push.

### Requisitos {#requirements}

![Pantalla de Xcode para elegir una plantilla para tu nuevo target con la opción Notification Content Extension seleccionada en Application Extension.]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) integradas correctamente en tu aplicación
- Los siguientes archivos generados por Xcode según tu lenguaje de programación:

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## Notificación push interactiva {#interactive-push-notification}

Las notificaciones push pueden responder a las acciones de los usuarios dentro de una extensión de contenido de la aplicación. Para los usuarios que ejecutan iOS 12 o posterior, esto significa que puedes convertir tus notificaciones push en mensajes totalmente interactivos. Esto ofrece una opción interesante para incorporar interactividad a tus promociones y aplicaciones. Por ejemplo, tu notificación push puede incluir un juego para que los usuarios jueguen, una ruleta de descuentos o un botón "me gusta" para guardar un anuncio o una canción.

El siguiente ejemplo muestra una notificación push en la que los usuarios pueden jugar un juego de parejas dentro de la notificación expandida.

![Un diagrama de cómo podrían verse las fases de una notificación push interactiva. Una secuencia muestra a un usuario presionando una notificación push que muestra un juego interactivo de parejas.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### Configuración del panel {#dashboard-configuration}

Para crear una notificación push interactiva, debes configurar una vista personalizada en tu panel.

1. Desde la página **Campaigns**, haz clic en **Create Campaign** para iniciar una nueva Campaign de notificación push.
2. En la pestaña **Compose**, activa **Notification Buttons**.
3. Introduce una categoría iOS personalizada en el campo **iOS Notification Category**.
4. En el `.plist` de tu Notification Content Extension Target, establece el atributo `UNNotificationExtensionCategory` con tu categoría iOS personalizada. El valor proporcionado aquí debe coincidir con lo configurado en el panel de Braze en **iOS Notification Category**.
5. Establece la clave `UNNotificationExtensionInteractionEnabled` en `true` para habilitar las interacciones de usuario en una notificación push.

![Las opciones de botones de notificación que se encuentran en la configuración del creador de mensajes push.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![Un plist que muestra NSExtension con UNNotificationExtensionCategory configurado como "your_custom_category", UNNotificationExtensionDefaultContentHidden configurado como 1 y UNNotificationExtensionInitialContentSizeRatio configurado como 1.]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## Notificaciones push personalizadas {#personalized-push-notifications}

![Dos iPhones mostrados uno junto al otro. El primero muestra la vista compacta del mensaje push. El segundo muestra la versión expandida del mensaje push con una imagen de "progreso" que indica cuánto han avanzado en un curso, el nombre de la siguiente sesión y cuándo debe completarse.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Las notificaciones push pueden mostrar información específica del usuario dentro de una extensión de contenido. Esto te permite crear contenido push enfocado en el usuario, como añadir la opción de compartir tu progreso en diferentes plataformas, mostrar logros desbloqueados o mostrar listas de verificación de incorporación. Este ejemplo muestra una notificación push que se muestra a un usuario después de haber completado una tarea específica en el Curso de Braze Learning. Al expandir la notificación, el usuario puede ver su progreso a lo largo de su ruta de aprendizaje. La información proporcionada aquí es específica del usuario y puede activarse cuando se completa una sesión o cuando el usuario realiza una acción específica, mediante un desencadenador de API.

### Configuración del panel

Para crear una notificación push personalizada, debes configurar una vista personalizada en tu panel.

1. Desde la página **Campaigns**, haz clic en **Create Campaign** para iniciar una nueva Campaign de notificación push.
2. En la pestaña **Compose**, activa **Notification Buttons**.
3. Introduce una categoría personalizada de iOS en el campo **iOS Notification Category**.
4. En la pestaña **Settings**, crea pares clave-valor utilizando Liquid estándar. Configura los atributos de usuario adecuados que deseas que el mensaje muestre. Estas vistas pueden personalizarse en función de atributos de usuario específicos de un perfil de usuario determinado.
5. En el `.plist` de tu Notification Content Extension Target, configura el atributo `UNNotificationExtensionCategory` con tu categoría personalizada de iOS. El valor proporcionado aquí debe coincidir con lo configurado en el panel de Braze en **iOS Notification Category**.

![Cuatro conjuntos de pares clave-valor, donde "next_session_name" y "next_session_complete_date" se configuran como una propiedad de desencadenador de API mediante Liquid, y "completed_session count" y "total_session_count" se configuran como un atributo de usuario personalizado mediante Liquid.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### Manejo de pares clave-valor {#handling-key-value-pairs}

El método `didReceive` se llama cuando la extensión de contenido de notificación ha recibido una notificación. Este método se encuentra dentro del `NotificationViewController`. Los pares clave-valor proporcionados en el panel se representan en el código mediante el uso de un diccionario `userInfo`.

#### Análisis de pares clave-valor de notificaciones push {#parsing-key-value-pairs-from-push-notifications}

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

Las notificaciones push pueden capturar información del usuario dentro de una extensión de contenido de la aplicación, ampliando los límites de lo posible con una notificación push. Solicitar datos del usuario a través de notificaciones push te permite no solo pedir información básica como el nombre o el correo electrónico, sino también invitar a los usuarios a enviar comentarios o completar un perfil de usuario incompleto.

{% alert tip %}
Para más información, consulta [Registrar datos de notificaciones push]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications).
{% endalert %}

En el siguiente flujo, la vista personalizada puede responder a cambios de estado. Los componentes de cambio de estado se representan en cada imagen.

1. El usuario recibe una notificación push.
2. Se abre la notificación push. Al expandirse, la notificación solicita información al usuario. En este ejemplo, se pide la dirección de correo electrónico del usuario, pero podrías solicitar cualquier tipo de información.
3. Se proporciona la información y, si tiene el formato esperado, se muestra el botón de registro.
3. Se muestra la vista de confirmación y la notificación push se descarta.


### Configuración del panel

Para crear una notificación push de captura de información, debes establecer una vista personalizada en tu panel.

1. Desde la página **Campaigns**, haz clic en **Create Campaign** para iniciar una nueva Campaign de notificación push.
2. En la pestaña **Compose**, activa **Notification Buttons**.
3. Introduce una categoría iOS personalizada en el campo **iOS Notification Category**.
4. En la pestaña **Settings**, crea pares clave-valor utilizando Liquid estándar. Establece los atributos de usuario adecuados que quieras que muestre el mensaje.
5. En el `.plist` de tu Notification Content Extension Target, establece el atributo `UNNotificationExtensionCategory` con tu categoría iOS personalizada. El valor proporcionado aquí debe coincidir con lo establecido en el panel de Braze en **iOS Notification Category**.

Como se ve en el ejemplo, también puedes incluir una imagen en tu notificación push. Para ello, debes integrar las [notificaciones enriquecidas]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift), establecer el estilo de notificación en tu Campaign como notificación enriquecida e incluir una imagen de notificación push enriquecida.

![Un mensaje push con tres conjuntos de pares clave-valor. 1. "Braze_id" configurado como una llamada Liquid para obtener el ID de Braze. 2. "cert_title" configurado como "Braze Marketer Certification". 3. "Cert_description" configurado como "Certified Braze marketers drive...".]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### Gestión de acciones de botones {#handling-button-actions}

Cada botón de acción se identifica de forma única. El código comprueba si tu identificador de respuesta es igual al `actionIdentifier` y, de ser así, sabe que el usuario hizo clic en el botón de acción.

**Gestión de respuestas de botones de acción de notificaciones push**<br>

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

Las notificaciones push se pueden descartar automáticamente al pulsar un botón de acción. Hay tres opciones predefinidas de descarte de notificaciones push que recomendamos:

1. `completion(.dismiss)` - Descarta la notificación
2. `completion(.doNotDismiss)` - La notificación permanece abierta
3. `completion(.dismissAndForward)` - La notificación push se descarta y el usuario es redirigido a la aplicación