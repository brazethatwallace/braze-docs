---
nav_title: Migração do SDK do Airship para a Braze
permalink: /sdk_migration_guide_airship/
hidden: true
page_type: reference
---

# Migrar SDKs do Airship para a Braze (iOS) {#migrate-sdks-from-airship-to-braze-ios}

> Na Braze, entendemos que a mudança para uma plataforma e um SDK totalmente novos pode ser assustadora, mas com o seguinte guia de migração, exemplos diretos em nível de código e o impressionante conjunto de recursos que a plataforma Braze oferece, achamos que você não se importará. Neste artigo, incluímos o equivalente na Braze a muitos dos principais recursos do Airship, bem como trechos de código do SDK para substituir o uso do Airship e tornar sua migração rápida, simples e indolor.

## Além do código {#beyond-the-code}
### Gerenciamento de tokens {#token-management}
A Braze usa o token de dispositivo da Apple para iOS.

| **Perspectiva da Braze:**<br>Garantimos que os clientes possam se comunicar continuamente com seus usuários (como notificações por push) durante o processo de migração do Airship para a Braze (seja uma transição direta de 100% para a Braze ou uma transição granular, como 50% Airship e 50% Braze, etc.). |
{: .reset-td-br-1 aria-label="Gerenciamento de tokens" }

#### Migração de tokens por push {#push-token-migration}

É necessário [migrar os tokens por push via API]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens). A documentação vinculada contém etapas específicas, além de um exemplo de carga útil, mas o processo geral é o seguinte:

1. Importe os tokens pelo [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Para importações em lote de grande volume, temos recursos disponíveis para ajudar a acelerar o processo. Entre em contato com seu COM ou SA para mais detalhes!
2. Se o token já existir na Braze, ele será ignorado; caso contrário, um perfil anônimo será gerado.
3. Realize a garantia de qualidade na integração de push. Certifique-se de que as etapas para [configurar push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) foram concluídas.

Se os perfis de usuário e os tokens por push estiverem armazenados em locais separados, recomendamos importar os tokens por push anonimamente e, em seguida, realizar uma migração subsequente dos perfis de usuário existentes. Não é necessário mapeá-los juntos, pois o SDK da Braze para iOS resolverá o token automaticamente após a integração bem-sucedida.

- Recomendamos migrar os usuários via API, mas se houver necessidade de importar uma lista estática de usuários, isso pode ser feito via CSV. Note que **tokens por push não podem ser importados via CSV** porque o objeto "push_token" não pode ser especificado no CSV. Para visualizar um modelo de importação e saber mais sobre como importar dados para o dashboard, confira nossa [documentação sobre CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#braze-csv-import).

{% alert note %}
Os tokens por push podem aparecer como `subscribed` no dashboard da Braze, mas mudarão para `opted-in` depois que os usuários iniciarem uma sessão com o SDK da Braze.
{% endalert %}

#### Múltiplos tokens por push {#multiple-push-tokens}

Na Braze, um usuário pode ter múltiplos tokens por push (um para cada dispositivo) e, ao direcionar todos os tokens por push válidos, você pode enviar notificações para vários dispositivos do usuário. Também é possível configurar Campaigns para enviar apenas para o dispositivo mais recente de um usuário.

## Configuração de Campaign {#campaign-configuration}

Em linhas gerais, a Braze é uma ferramenta verdadeiramente única no espaço de engajamento do cliente. Devido às nossas extensas opções de personalização e ao conjunto de recursos em constante crescimento, as campanhas migradas para a Braze frequentemente se beneficiam de um replanejamento para aproveitar os benefícios dessas ferramentas. Nosso framework de planejamento de campanhas (entre em contato com seu COM ou SA para mais detalhes) foi criado exatamente para isso.

### Composição {#composition}
#### Notificações por push {#push-notifications}
A Braze requer canais separados para push (um para iOS, outro para Android).

| **Perspectiva da Braze:**<br>Nós permitimos que nossos clientes aproveitem os benefícios de ambos, em vez de precisar fazer concessões. A capacidade de usar cada canal individual em sua capacidade total oferece mais flexibilidade para o profissional de marketing e uma experiência de usuário aprimorada. Isso nos permite adotar os recursos mais recentes de cada sistema operacional; por exemplo, o Android suportou notificações Rich antes do iOS. |
{: .reset-td-br-1 aria-label="Notificações por push" }

A Braze é capaz de enviar notificações por push para usuários que não atualizaram seu aplicativo com o SDK da Braze instalado. Dado que a Braze possui um token por push válido, a Braze pode enviar a notificação por push sem o SDK da Braze, pois o APNs cuidará do restante. É crucial observar que a **análise de dados das mensagens push não estará disponível para compilações sem o SDK da Braze**.

##### Compartilhamento de tokens {#sharing-tokens}

No caso de campanhas específicas de ciclo de vida que precisem continuar durante o processo de migração para o SDK da Braze, os usuários podem ser elegíveis para receber notificações tanto da Braze quanto do Airship, desde que a Braze tenha recebido um token por push válido.

#### Central de mensagens {#message-center}
Para substituir a funcionalidade de campanha da central de mensagens do Airship, recomendamos criar uma campanha multicanal que consista em uma notificação por push e um [cartão de conteúdo]({{site.baseurl}}/user_guide/channels/content_cards). Para saber mais sobre como usar Content Cards em um formato de central de mensagens, confira nosso [guia de implementação de Content Cards para iOS]({{site.baseurl}}/developer_guide/content_cards/creating_cards#message-inbox).

### Segmentação {#segmentation}
A Braze oferece múltiplos filtros de [segmentação]({{site.baseurl}}/user_guide/audience/segments) para proporcionar uma experiência de usuário rica para seus clientes.

| **Perspectiva da Braze**:<br> Os Segments na Braze são totalmente dinâmicos, então os usuários entrarão e sairão do Segment conforme as condições definidas mudarem. |
{: .reset-td-br-1 aria-label="Segmentação" }

#### Migração de Segments de usuários {#user-segment-migration}

Para recriar diretamente um Segment estático do Airship na Braze, existem duas opções:
- **Importar via API - Atribuir um atributo personalizado** (Recomendado)<br>
Recomendamos importar usuários por meio do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) e, ao fazer isso, atribuir um atributo personalizado a esses usuários importados. Por exemplo, você pode criar um Segment de usuários em que cada um tenha um atributo personalizado `Segment_Group_1` definido como `true`. Para segmentar esses usuários posteriormente, você [criaria um Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) com todos os usuários onde `Segment_Group_1` seja `true`.<br><br>
- **Filtrar com base na importação de usuários via CSV**<br>
Existe uma opção na Braze para filtrar especificamente os usuários incluídos em uma importação de CSV específica. Essa opção de filtro pode ser encontrada durante a etapa de direcionamento de usuários das nossas ferramentas de engajamento, em "filtrar usuários por `Updated/Imported via CSV`".
![Filtro de importação de CSV]({% image_buster /assets/img/csv_filter.png %}){: style="max-width:90%;border:0;"}
Observe que, para importações de CSV, um ID externo é necessário para cada usuário importado e **Segments com usuários anônimos ou somente com alias não poderão ser importados**. Para visualizar um modelo de importação e saber mais sobre como importar dados para o dashboard, confira nossa [documentação de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#braze-csv-import).

## Substituir trechos de código do SDK {#replace-sdk-code-snippets}
Para simplificar a migração, destacamos os seguintes trechos do SDK da Airship que existem no seu código e fornecemos os trechos correspondentes do SDK da Braze necessários para substituí-los. Acesse os seguintes tópicos para começar:
- [Instalação](#installation)
- [Obter e definir o ID do usuário](#userid)
- [Tratamento de notificações por push](#pushnotifications)
- [Análise de dados](#analytics)
- [Tratamento de mensagens no app](#iammessages)
- [Content Cards e central de mensagens](#messagecenter)

### Instalação {#installation}
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

### Obter e definir o ID do usuário {#userid}
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

### Tratamento de notificações por push {#pushnotifications}
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

### Análise de dados {#analytics}
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

### Tratamento de mensagens no app {#iammessages}
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

### Content Cards e central de mensagens {#messagecenter}
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