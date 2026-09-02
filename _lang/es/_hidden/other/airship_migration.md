---
nav_title: Migración del SDK or kit de desarrollo de software de Airship a Braze
permalink: /sdk_migration_guide_airship/
hidden: true
page_type: reference
---

# Migrar SDKs de Airship a Braze (iOS) {#migrate-sdks-from-airship-to-braze-ios}

> En Braze, entendemos que cambiar a una plataforma y un SDK or kit de desarrollo de software completamente nuevos puede ser desalentador, pero con la siguiente guía de migración, los sencillos ejemplos a nivel de código y el impresionante conjunto de características que aporta la plataforma Braze, no creemos que te importe. En este artículo, hemos incluido el equivalente en Braze de muchas características clave de Airship, así como fragmentos de código del SDK or kit de desarrollo de software para sustituir el uso de Airship y hacer que tu migración sea rápida, sencilla y sin complicaciones.

## Más allá del código {#beyond-the-code}
### Gestión de tokens {#token-management}
Braze utiliza el token de dispositivo de Apple para iOS.

| **Perspectiva de Braze:**<br>Nos aseguramos de que los clientes puedan comunicarse continuamente con sus usuarios (por ejemplo, notificaciones push) durante el proceso de migración de Airship a Braze (ya sea un cambio directo al 100% en Braze o una transición gradual, como 50% Airship y 50% Braze, etc.). |
{: .reset-td-br-1 aria-label="Gestión de tokens" }

#### Migración de tokens de notificaciones push {#push-token-migration}

Es necesario [migrar los tokens de notificaciones push a través de la API]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens). La documentación enlazada contiene pasos específicos, así como un ejemplo de carga útil, pero el proceso general es el siguiente:

1. Importa los tokens a través del [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Para importaciones masivas, tenemos recursos disponibles para ayudar a agilizar el proceso. ¡Contacta a tu COM o SA para más detalles!
2. Si el token ya existe en Braze, se ignorará; de lo contrario, se generará un perfil anónimo.
3. Realiza el aseguramiento de calidad en la integración push. Asegúrate de que se hayan completado los pasos para [configurar push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

Si tus perfiles de usuario y tokens de notificaciones push están almacenados en ubicaciones separadas, recomendamos importar los tokens de notificaciones push de forma anónima y luego realizar una migración posterior de tus perfiles de usuario existentes. No es necesario asociarlos entre sí, ya que el SDK or kit de desarrollo de software de Braze para iOS se encargará de la resolución del token tras una integración exitosa.

- Recomendamos migrar usuarios a través de la API, pero si necesitas importar una lista estática de usuarios, se puede hacer mediante CSV. Ten en cuenta que **los tokens de notificaciones push no se pueden importar a través de CSV** porque el objeto "push_token" no se puede especificar en el CSV. Para ver una plantilla de importación y obtener más información sobre la importación de datos en el panel, consulta nuestra [documentación de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#braze-csv-import).

{% alert note %}
Los tokens de notificaciones push pueden aparecer como `subscribed` en el panel de Braze, pero cambiarán a `opted-in` una vez que los usuarios inicien una sesión con el SDK or kit de desarrollo de software de Braze.
{% endalert %}

#### Múltiples tokens de notificaciones push {#multiple-push-tokens}

Con Braze, un usuario puede tener múltiples tokens de notificaciones push (uno por cada dispositivo) y, al dirigirse a todos los tokens de notificaciones push válidos, puedes enviar notificaciones a múltiples dispositivos del usuario. También es posible configurar Campaigns para que solo se envíen al dispositivo más reciente de un usuario.

## Configuración de Campaign {#campaign-configuration}
A un nivel general, Braze es una herramienta verdaderamente única en el espacio de interacción con los clientes. Debido a nuestras amplias opciones de personalización y nuestro creciente conjunto de características, las Campaigns migradas a Braze a menudo se benefician de una replanificación para aprovechar las ventajas de estas herramientas, y nuestro marco de planificación de Campaigns (contacta a tu COM o SA para más detalles) está diseñado específicamente para eso.

### Composición {#composition}
#### Notificaciones push {#push-notifications}
Braze requiere canales separados para push (uno para iOS y otro para Android).

| **Perspectiva de Braze:**<br>Permitimos a nuestros clientes obtener los beneficios de ambos en lugar de tener que hacer concesiones. Poder utilizar cada canal individual a su máxima capacidad ofrece más flexibilidad para el especialista en marketing y una experiencia de usuario mejorada. Esto nos permite adoptar las últimas características de cada SO; por ejemplo, Android soportó notificaciones enriquecidas antes que iOS. |
{: .reset-td-br-1 aria-label="Notificaciones push" }

Braze puede enviar notificaciones push a usuarios que no actualicen su aplicación con el SDK or kit de desarrollo de software de Braze instalado. Dado que Braze tiene un token de notificaciones push válido, Braze puede enviar la notificación push sin el SDK or kit de desarrollo de software de Braze, ya que APNs se encargará del resto. Es crucial señalar que los **análisis de mensajes push no estarán disponibles para compilaciones sin el SDK or kit de desarrollo de software de Braze**.

##### Compartir tokens {#sharing-tokens}

En el caso de Campaigns específicas del ciclo de vida que necesiten continuar durante tu proceso de migración al SDK or kit de desarrollo de software de Braze, los usuarios pueden ser elegibles para recibir notificaciones tanto de Braze como de Airship, siempre que Braze haya recibido un token de notificaciones push válido.

#### Centro de mensajes {#message-center}
Para reemplazar la funcionalidad del centro de mensajes de Campaign de Airship, recomendamos crear una Campaign multicanal que consista en una notificación push y una [tarjeta de contenido]({{site.baseurl}}/user_guide/channels/content_cards). Para leer más sobre cómo usar Content Cards en un formato de centro de mensajes, consulta nuestra [guía de implementación de Content Cards para iOS]({{site.baseurl}}/developer_guide/content_cards/creating_cards#message-inbox).

### Segmentación {#segmentation}
Braze ofrece múltiples filtros de [segmentación]({{site.baseurl}}/user_guide/audience/segments) para proporcionar una experiencia de usuario enriquecida a tus clientes.

| **Perspectiva de Braze**:<br> Los Segments en Braze son completamente dinámicos, por lo que los usuarios entrarán y saldrán del Segment a medida que cambien las condiciones definidas. |
{: .reset-td-br-1 aria-label="Segmentación" }

#### Migración de Segments de usuarios {#user-segment-migration}

Para recrear directamente un Segment estático de Airship en Braze, existen dos opciones:
- **Importar vía API - Asignar un atributo personalizado** (Recomendado)<br>
Recomendamos importar usuarios a través del [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) y, al hacerlo, asignar un atributo personalizado a esos usuarios importados. Por ejemplo, podrías crear un Segment de usuarios donde cada uno tenga un atributo personalizado `Segment_Group_1` establecido en `true`. Para segmentar posteriormente a estos usuarios, [crearías un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) de todos los usuarios donde `Segment_Group_1` sea `true`.<br><br>
- **Filtrar basándose en la importación de usuarios en CSV**<br>
Existe una opción en Braze para filtrar específicamente a los usuarios que están incluidos en una importación de CSV específica. Esta opción de filtrado se puede encontrar durante el paso de selección de usuarios de nuestras herramientas de participación en "filtrar usuarios por `Updated/Imported via CSV`".
![Filtro de importación CSV]({% image_buster /assets/img/csv_filter.png %}){: style="max-width:90%;border:0;"}
Ten en cuenta que para las importaciones de CSV, se requiere un ID externo para cada usuario importado y **los Segments con usuarios anónimos o de solo alias no podrán ser importados**. Para ver una plantilla de importación y obtener más información sobre cómo importar datos al panel, consulta nuestra [documentación de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#braze-csv-import).

## Sustituir fragmentos de código del SDK or kit de desarrollo de software {#replace-sdk-code-snippets}
Para simplificar la migración, hemos destacado los siguientes fragmentos del SDK or kit de desarrollo de software de Airship que existen en tu código y hemos proporcionado los fragmentos correspondientes del SDK or kit de desarrollo de software de Braze necesarios para sustituirlos. Visita los siguientes temas para empezar:
- [Instalación](#installation)
- [Obtener y configurar el ID de usuario](#userid)
- [Gestión de notificaciones push](#pushnotifications)
- [Análisis](#analytics)
- [Gestión de mensajes dentro de la aplicación](#iammessages)
- [Content Cards y centro de mensajes](#messagecenter)

### Instalación {#installation}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {

    UAirship.takeOff(UAConfig.default())

    UALocation.shared()?.isLocationUpdatesEnabled = true
    UALocation.shared().isBackgroundLocationUpdatesAllowed = true

    UAirship.push()?.notificationOptions = [.alert, .badge, .sound]
    UAirship.push()?.userPushNotificationsEnabled = true
    UAirship.push()?.pushNotificationDelegate = self

    UAInAppAutomation.shared()?.inAppMessageManager.delegate = self
    UAInAppAutomation.shared()?.inAppMessageManager.displayInterval = 30
}
```
**Braze**
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {

    Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

    locationManager.requestAlwaysAuthorization() // locationManager is a CLLocationManager property variable

    // Push Notifications
    let options: UNAuthorizationOptions = [.alert, .sound, .badge]
    UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
      Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
    }
    UIApplication.shared.registerForRemoteNotifications()

    // In-App Messages
    Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endtab %}
{% tab Objective-C %}
**Airship**
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

  [UAirship takeOff:[UAConfig defaultConfig]];

  [[UALocation shared] setLocationUpdatesEnabled:YES];
  [[UALocation shared] setBackgroundLocationUpdatesAllowed:YES];

  [UAirship push].notificationOptions = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  [[UAirship push] setUserPushNotificationsEnabled:YES];
  [[UAirship push] setPushNotificationDelegate:self];

  [UAInAppAutomation shared].inAppMessageManager.delegate = self;
  [UAInAppAutomation shared].inAppMessageManager.displayInterval = 30;

  return YES;
}
```
**Braze**
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

  [Appboy startWithApiKey:self.apiKey inApplication:application withLaunchOptions:launchOptions withAppboyOptions:self.appboyOptions];

  [self.locationManager requestAlwaysAuthorization]; // locationManager is a CLLocationManager property variable

  // Push Notifications
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options
                          completionHandler:^(BOOL granted, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];

  // In-App Messages
  [[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];

  return YES;
}
```

{% endtab %}
{% endtabs %}

### Obtener y configurar el ID de usuario {#userid}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
extension AirshipManager {
  var userId: String? {
    return UAirship.namedUser()?.identifier
   }

  func setUser(_ userId: String) {
    UAirship.namedUser()?.identifier = userId
  }
}
```
**Braze**
```swift
extension AppboyManager {
  var userId: String? {
     return Appboy.sharedInstance()?.user.userID
  }

  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Airship**
```objc

- (NSString *)userId {
  return [UAirship namedUser].identifier
}

- (void)setUser:(NSString *)userId {
  [[UAirship namedUser] setIdentifier:userId];
}
```
**Braze**
```objc
- (NSString *)userId {
  return [Appboy sharedInstance].user.userID;
}

- (void)changeUser:(NSString *)userId {
  [[Appboy sharedInstance] changeUser: userId];
}
```
{% endtab %}
{% endtabs %}

### Gestión de notificaciones push {#pushnotifications}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
extension AirshipManager: UAPushNotificationDelegate {
  func receivedBackgroundNotification(_ notificationContent: UANotificationContent, completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    completionHandler(.noData)
  }

  func receivedForegroundNotification(_ notificationContent: UANotificationContent, completionHandler: @escaping () -> Void) {
    completionHandler()
  }

  func receivedNotificationResponse(_ notificationResponse: UANotificationResponse, completionHandler: @escaping () -> Void) {
    completionHandler()
  }
}
```
**Braze**
```swift
extension AppboyManager {
  func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
  }

  func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    Appboy.sharedInstance()?.register(application, didReceiveRemoteNotification: userInfo, fetchCompletionHandler: completionHandler)
  }

  func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
    Appboy.sharedInstance()?.userNotificationCenter(center, didReceive: response, withCompletionHandler: completionHandler)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Airship**
```objc
- (void)receivedBackgroundNotification:(UANotificationContent *)notificationContent completionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  completionHandler(UIBackgroundFetchResultNoData);
}

- (void)receivedForegroundNotification:(UANotificationContent *)notificationContent completionHandler:(void (^)(void))completionHandler {
  completionHandler();
}

- (void)receivedNotificationResponse:(UANotificationResponse *)notificationResponse completionHandler:(void (^)(void))completionHandler {
  completionHandler();
}
```
**Braze**
```objc
- (void)application:(UIApplication *)application didRegisterForRemoteNotifications
  func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
  }

- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  [[Appboy sharedInstance] registerDeviceToken:deviceToken];
}

- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
}

- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response
         withCompletionHandler:(void (^)(void))completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center didReceiveNotificationResponse:response withCompletionHandler:completionHandler];
}
```
{% endtab %}
{% endtabs %}

### Análisis {#analytics}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
extension AirshipManager {
  func trackEvent(with name: String, value: NSDecimalNumber? = nil, eventProperties: [String: Any]? = nil) {
    let event = UACustomEvent(name: name, value: value)

    if let eventProperties = eventProperties {
      event.properties = eventProperties
    }

    event.track()
  }

  func applyMutationsWithValue(_ value: String, forAttribute attribute: String) {
    let mutations = UAAttributeMutations()
    mutations.setString(value, forAttribute: attribute)
    UAirship.namedUser().apply(mutations)
  }
}
```
**Braze**
```swift
extension AppboyManager {
  func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
    Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
  }

  func setCustomAttributeWithKey(_ key: String, andStringValue value: String) {
    Appboy.sharedInstance()?.user.setCustomAttributeWithKey(key, andStringValue: value)
  }

  func logPurchase(productIdentifier: String, inCurrency currency: String, atPrice price: String, withQuanitity quanity: Int) {
    Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quanity))
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Airship**
```objc
- (void)trackEventWith:(NSString *)name value:(NSDecimalNumber *)value eventProperties:(NSDictionary *)eventProperties {
  UACustomEvent *event = [[UACustomEvent alloc] init];
  event.eventName = name;
  event.eventValue = value;
  event.properties = eventProperties;

  [event track];
}

- (void)applyMutationWith:(NSString *)value forAttribute:(NSString *)attribute {
  UAAttributeMutations* mutations = [[UAAttributeMutations alloc] init];
  [mutations setString:value forAttribute:attribute];
  [[UAirship namedUser] applyAttributeMutations:mutations];
}
```
**Braze**
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties: properties];
}

- (void)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value {
  [[Appboy sharedInstance].user setCustomAttributeWithKey:key andStringValue:value];
}

- (void)logPurchase:(NSString *)productIdentifier inCurrency:(NSString *)currency atPrice:(NSString *)price withQuantity:(NSInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currency atPrice:[[NSDecimalNumber alloc] initWithString:price] withQuantity:quantity];
}
```
{% endtab %}
{% endtabs %}

### Gestión de mensajes dentro de la aplicación {#iammessages}
{% tabs %}
{% tab Swift %}
**Airship**
```swift

extension AirshipManager: UAInAppMessagingDelegate {
  func extend(_ message: UAInAppMessage) -> UAInAppMessage {
      return message
  }

  func messageWillBeDisplayed(_ message: UAInAppMessage, scheduleID: String) {
  }

  func messageFinishedDisplaying(_ message: UAInAppMessage, scheduleID: String, resolution: UAInAppMessageResolution) {
  }
}
```
**Braze**
```swift
extension AppboyManager: ABKInAppMessageControllerDelegate {
  func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
    // This delegate method defines whether the in-app message will be displayed now, displayed later, or discarded.
    return .displayInAppMessageNow
  }

  func beforeControlMessageImpressionLogged(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
    // This delegate method defines the timing of when the control in-app message impression event should be logged: now, later, or discarded.
    return .displayInAppMessageNow
  }
}

extension AppboyManager: ABKInAppMessageUIDelegate {
  func on(inAppMessageDismissed inAppMessage: ABKInAppMessage) {
    // Use this method to perform any custom logic that should execute after the in-app message has been dismissed
  }

  func on(inAppMessageClicked inAppMessage: ABKInAppMessage) -> Bool {
    // This delegate method is fired when the user clicks on a slide-up in-app message or a modal/full in-app message without button(s) on it.
    return true
  }

  func on(inAppMessageButtonClicked inAppMessage: ABKInAppMessageImmersive, button: ABKInAppMessageButton) -> Bool {
    // This delegate method is fired whenever the user clicks a button on the in-app message.
    return true
  }

  func on(inAppMessageHTMLButtonClicked inAppMessage: ABKInAppMessageHTMLBase, clickedURL: URL?, buttonID buttonId: String) -> Bool {
    // This delegate method is fired whenever the user clicks a link on the HTML in-app message.
    return true
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Airship**
```objc
- (UAInAppMessage *)extendMessage:(UAInAppMessage *)message {

  return message;
}

- (void)messageWillBeDisplayed:(UAInAppMessage *)message scheduleID:(NSString *)scheduleID {

}

- (void)messageFinishedDisplaying:(UAInAppMessage *)message scheduleID:(NSString *)scheduleID resolution:(UAInAppMessageResolution *)resolution {

}
```
**Braze**
```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  return ABKDisplayInAppMessageNow;
}

- (ABKInAppMessageDisplayChoice) beforeControlMessageImpressionLogged:(ABKInAppMessage *)inAppMessage {
  return ABKDisplayInAppMessageNow;
}

- (void)onInAppMessageDismissed:(ABKInAppMessage *)inAppMessage {
  // Use this method to perform any custom logic that should execute after the in-app message has been dismissed
}

- (BOOL)onInAppMessageClicked: (ABKInAppMessage *)inAppMessage {
  // This delegate method is fired when the user clicks on a slide-up in-app message or a modal/full in-app message without button(s) on it.
  return YES;
}

- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button {
  return YES;
}

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID {
  return YES;
}
```
{% endtab %}
{% endtabs %}

### Content Cards y centro de mensajes {#messagecenter}
{% tabs %}
{% tab Swift %}
**Airship**
```swift
extension AirshipManager {
  func displayMessageCenter() {
    UAMessageCenter.shared()?.defaultUI.title = "My Message Center"

    let style = UAMessageCenterStyle()
    style.navigationBarColor = .black
    style.titleColor = .white
    style.tintColor = .white

    UAMessageCenter.shared()?.defaultUI.messageCenterStyle = style
    UAMessageCenter.shared()?.display()
  }
}
```
**Braze**
```swift
extension AppboyManager {
  func displayContentCards(navigationController: UINavigationController?) {
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "My Message Center"
    contentCardsVc.disableUnreadIndicator = true
    navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Airship**
```objc
- (void)displayMessageCenter {
  [UAMessageCenter shared].defaultUI.title = @"My Message Center";
  [[UAMessageCenter shared] display];
}
```
**Braze**
```objc
- (void)displayContentCards:(UINavigationController *)navigationController {
  ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
  contentCards.title = @"My Message Center";
  [self.navigationController pushViewController:contentCards animated:YES];
}
```
{% endtab %}
{% endtabs %}