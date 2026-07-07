---
nav_title: "Opciones de notificación"
article_title: Opciones de notificación de iOS
page_order: 2
page_layout: reference
description: "Este artículo de referencia cubre las opciones de notificación de iOS, como alertas críticas, notificaciones silenciosas, notificaciones push provisionales y más."

platform: iOS
channel:
  - push

---

# Opciones de notificación {#notification-options}

> Con el lanzamiento de iOS 12 de Apple, Braze ofrece compatibilidad con varias de sus características, incluyendo [grupos de notificaciones](#notification-groups), [notificaciones silenciosas/autorización provisional](#provisional-push-authentication--quiet-notifications) y [alertas críticas](#critical-alerts).

## Grupos de notificaciones {#notification-groups}

Si deseas categorizar tus mensajes y agruparlos en la bandeja de notificaciones de tu usuario, puedes utilizar la característica de grupos de notificaciones de iOS a través de Braze.

Crea tu Campaign de push para iOS, luego ve a la pestaña **Settings** y abre el desplegable **Notification group**.

![La pestaña "Settings" con un desplegable "Notification group" que tiene seleccionado un valor de "Coupons".]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Selecciona tus grupos de notificaciones en el desplegable. Si la configuración de tu grupo de notificaciones no funciona correctamente o seleccionas **None** en el desplegable, el mensaje se enviará automáticamente de forma normal a todos los usuarios definidos en el espacio de trabajo.

Si no tienes ningún grupo de notificaciones listado aquí, puedes agregar uno usando el ID de hilo de iOS. Necesitarás un ID de hilo de iOS por cada grupo de notificaciones que quieras agregar. Luego, agrégalo a tus grupos de notificaciones haciendo clic en **Manage Notification Groups** en el desplegable y completando los campos obligatorios en la ventana **Manage iOS Push Notification Groups** que aparece.

![Ventana para administrar grupos de notificaciones push de iOS.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Crea tu Campaign de push para iOS, luego busca en la parte superior del compositor. Allí verás un desplegable etiquetado como **Notification Groups**.

### Argumentos de resumen {#summary-arguments}

Además de agrupar notificaciones por ID de hilo, Apple te permite editar los resúmenes que aparecen cuando las notificaciones están agrupadas. Los usuarios de Braze pueden especificar la categoría de resumen, el conteo de resumen y el argumento de resumen al redactar una Campaign de push usando nuestra herramienta.

{% alert tip %}
Ten en cuenta que la forma en que las notificaciones con el mismo ID de hilo se agrupan en la bandeja de notificaciones está bajo el control del sistema operativo. iOS puede elegir mostrar las notificaciones con el mismo ID de hilo por separado o en grupos dependiendo de lo que considere óptimo.
{% endalert %}

Marca la casilla **Alert Options** en el **Push Composer**.

Luego, selecciona `summary-arg` y `summary-arg-count` como claves e ingresa esos valores en la columna correspondiente. Si no estableces un valor para `summary-arg`, se usará el valor predeterminado de 1.

### Categorías de resumen {#summary-categories}

Las categorías de resumen te permiten personalizar todo el resumen que aparece cuando las notificaciones están agrupadas. Puedes crear y aplicar múltiples categorías.

Para usar una categoría en tu mensaje, trabaja con tus desarrolladores para implementarla usando el siguiente ejemplo:

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
Esto no requerirá una actualización del SDK.
{% endalert %}

{% alert tip %}
Ten en cuenta que `%u` y `%@` son cadenas de formato para el conteo de resumen y el argumento de resumen, respectivamente. Cuando se muestra el resumen, estos marcadores de posición se reemplazarán con los valores de `summary-count` y `summary-arg`.
{% endalert %}

Una vez que esto esté configurado en tu aplicación, usa la categoría de resumen marcando la casilla **Notification Buttons** y seleccionando **Enter Pre-registered iOS Category**.

Luego, ingresa el identificador de categoría de resumen que configuraste en tu aplicación.

### Autenticación push provisional y notificaciones silenciosas {#provisional-push}

Apple permite a las marcas la opción de enviar notificaciones push silenciosas al centro de notificaciones de sus usuarios antes de que estos se adhieran oficial y explícitamente, dándote la oportunidad de demostrar el valor de tus mensajes de forma anticipada. Todo lo que necesitas hacer es [configurar las notificaciones push provisionales](#set-up-provisional-push-notifications) en tu aplicación, y cualquier usuario que tenga un token de push provisional recibirá tus mensajes.

A diferencia de un token de push de iOS tradicional, un token de push provisional actúa como un "pase de prueba" que permite a las marcas llegar a nuevos usuarios antes de que hayan visto y hecho clic en el mensaje nativo de adhesión voluntaria de push de Apple. Con esta característica, tu notificación push se entregará directamente en la bandeja de notificaciones de tu nuevo usuario con la opción de "Mantener" o "Desactivar" futuras notificaciones. En lugar de experimentar un proceso de "adhesión voluntaria", los usuarios experimentarán algo más parecido a un proceso de "exclusión voluntaria".

{% alert tip %}
La autorización provisional tiene el potencial de aumentar drásticamente tu tasa de adhesión voluntaria, pero solo si los usuarios ven valor en tus mensajes. Asegúrate de usar nuestras características de [segmentación de usuarios]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), [segmentación por ubicación]({{site.baseurl}}/user_guide/audience/locations_and_geofences) y [personalización]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) para garantizar que los usuarios apropiados reciban estas notificaciones de "prueba" en el momento adecuado. Luego, puedes animar a los usuarios a adherirse completamente a tus notificaciones push, sabiendo que agregan valor a la experiencia de tus usuarios con tu aplicación.
{% endalert %}

Cualquiera que sea la opción que el usuario elija, se agregará el token apropiado o el [estado de suscripción]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states) a su [configuración de contacto]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) en la pestaña **Engagement** de su perfil de usuario.

![Configuración de contacto con un estado de suscripción push.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Podrás segmentar a tus usuarios en función de si están autorizados provisionalmente o no usando nuestros [filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

![Panel de detalles de Segment con el filtro de ejemplo "Provisionally Authorized on iOS Stopwatch (iOS) is true" para segmentar usuarios.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Si los usuarios eligen "Desactivar" el push provisional de tu parte, no verán más mensajes push provisionales tuyos. ¡Sé cuidadoso con el contenido del mensaje y la cadencia de envío usando esta funcionalidad!
{% endalert %}

{% alert important %}
Si utilizas mensajes push adicionales o [primers de push dentro de la aplicación](https://www.braze.com/resources/glossary/priming-for-push/) (un mensaje dentro de la aplicación que anima a los usuarios a adherirse a las notificaciones push), ponte en contacto con tu representante de Braze para obtener orientación adicional.
{% endalert %}

#### Configurar notificaciones push provisionales {#set-up-provisional-push-notifications}

Braze te permite registrarte para la autenticación provisional actualizando tu código en el fragmento de registro de tokens dentro de tu implementación del SDK de Braze para iOS usando los siguientes fragmentos como ejemplo (envíalos a tus desarrolladores o asegúrate de que [implementen la autenticación push provisional durante el proceso de integración]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#using-usernotification-framework-ios-10)).

{% alert warning %}
La implementación de la autenticación push provisional solo es compatible con iOS 12+ y generará un error si el objetivo de despliegue es anterior. Puedes obtener más información sobre esto [en nuestra documentación de implementación más detallada aquí]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#using-usernotification-framework-ios-10).
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**Swift**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

**Objective-C**

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### Nivel de interrupción (iOS 15+) {#interruption-level}

Con el nuevo modo Enfoque de iOS 15, los usuarios tienen más control sobre cuándo las notificaciones de las aplicaciones pueden "interrumpirlos" con un sonido o vibración.

![Página de configuración de notificaciones de iOS que muestra las notificaciones habilitadas para entrega inmediata y con notificaciones urgentes habilitadas.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Las aplicaciones ahora pueden especificar qué nivel de interrupción debe incluir una notificación, según su urgencia.

Para cambiar el nivel de interrupción de una notificación push de iOS, selecciona la pestaña **Settings** y elige el nivel deseado en el menú desplegable **Interruption Level**.

![Desplegable para seleccionar el nivel de interrupción.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

Esta característica no tiene requisitos mínimos de versión del SDK, pero solo se aplica a dispositivos con iOS 15+.

Ten en cuenta que los usuarios son en última instancia quienes controlan su enfoque, e incluso si se entrega una notificación urgente, pueden especificar qué aplicaciones no tienen permitido interrumpir su enfoque.

Consulta la siguiente tabla para los niveles de interrupción y sus descripciones.

| Nivel de interrupción | Descripción | Cuándo usar | Interrumpe el modo Enfoque |
|--|--|--|--|
| [Passive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive) | Envía una notificación sin sonido, vibración ni encender la pantalla. | Notificaciones que no requieren atención inmediata. | No |
| [Active](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (predeterminado) | Solo emitirá un sonido, vibración y encenderá la pantalla si el usuario no está en modo Enfoque. | Notificaciones que requieren atención inmediata, a menos que el usuario tenga el modo Enfoque habilitado. | No |
| [Time Sensitive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive) | Emitirá un sonido, vibrará y encenderá la pantalla incluso en modo Enfoque. Esto requiere que la capacidad **Time Sensitive Notifications** se agregue a tu aplicación en Xcode. | Notificaciones oportunas que deben interrumpir a los usuarios independientemente de su modo Enfoque, como una notificación de viaje compartido o entrega. | Sí |
| [Critical](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical) | Emitirá un sonido, vibrará y encenderá la pantalla incluso si el interruptor de **Do Not Disturb** del teléfono está habilitado. Esto [requiere aprobación explícita de Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/). | Emergencias como alertas de clima severo o seguridad. | Sí |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Nivel de interrupción (iOS 15+)" }

### Puntuación de relevancia (iOS 15+) {#relevance-score}

![Un resumen de notificaciones de iOS titulado "Your Evening Summary" con tres notificaciones.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 también introduce una nueva forma para que los usuarios programen opcionalmente una agrupación de resumen de múltiples notificaciones en horarios designados a lo largo del día. Esto se hace para evitar interrupciones constantes durante el día para notificaciones que no necesitan atención inmediata.

Las aplicaciones pueden especificar qué notificaciones push son más relevantes estableciendo una **puntuación de relevancia**. Apple usará esta puntuación para determinar qué notificaciones deben destacarse en el resumen de notificaciones programado, mientras que otras estarán disponibles cuando los usuarios hagan clic en el resumen.

Todas las notificaciones seguirán siendo accesibles en el centro de notificaciones del usuario.

Para establecer la puntuación de relevancia de una notificación de iOS, ingresa un valor entre `0.0` y `1.0` en la pestaña **Settings**. Por ejemplo, el mensaje más importante debe enviarse con `1.0`, mientras que un mensaje de importancia media puede enviarse con `0.5`.

![Puntuación de relevancia de "0.5".]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

Esta característica no tiene requisitos mínimos de versión del SDK, pero solo se aplica a dispositivos con iOS 15+.

Para más información sobre las longitudes máximas de mensaje para diferentes tipos de mensaje, consulta los siguientes recursos:

- [Especificaciones de imagen y texto]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)
- [Directrices de conteo de caracteres de iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications#character-count)