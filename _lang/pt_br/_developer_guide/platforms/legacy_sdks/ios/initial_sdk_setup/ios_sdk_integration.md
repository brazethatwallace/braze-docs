---
nav_title: Guia de integração de SDK (opcional)
article_title: Guia de integração do SDK da Braze para iOS (opcional)
alias: "/ios_sdk/"
description: "Este guia de integração do iOS leva você a uma jornada passo a passo sobre as práticas recomendadas de configuração ao integrar pela primeira vez o SDK do iOS e seus componentes principais em seu aplicativo. Este guia ajudará você a criar um arquivo auxiliar BrazeManager.swift."
page_order: 10
platform: iOS

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Guia de integração do SDK da Braze para iOS {#braze-ios-sdk-integration-guide}

> Este guia opcional de integração do iOS leva você a uma jornada passo a passo sobre as práticas recomendadas de configuração ao integrar pela primeira vez o SDK do iOS e seus componentes principais em seu aplicativo. Este guia ajudará você a criar um arquivo auxiliar `BrazeManager.swift` que desacoplará todas as dependências do SDK da Braze para iOS do restante do seu código de produção, resultando em um único `import AppboyUI` em todo o seu aplicativo. Essa abordagem limita os problemas decorrentes do excesso de importações de SDK, facilitando o rastreamento, a depuração e a alteração do código.

{% alert important %}
Este guia pressupõe que você já tenha [adicionado o SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) ao seu projeto Xcode.
{% endalert %}

## Visão geral da integração {#integration-overview}

As etapas a seguir ajudam você a criar um arquivo auxiliar `BrazeManager` que seu código de produção pode chamar. Esse arquivo auxiliar lidará com todas as dependências relacionadas à Braze, adicionando várias extensões para os seguintes tópicos de integração listados. Cada tópico incluirá etapas em guias horizontais e snippets de código tanto em Swift quanto em Objective-C. Note que as etapas de Content Cards e mensagens no app não são obrigatórias para a integração se você não planeja usar esses canais na sua aplicação.

- [Criar BrazeManager.swift](#create-brazemanagerswift)
- [Inicializar o SDK](#initialize-the-sdk)
- [Notificações por push](#push-notifications)
- [Acessar variáveis e métodos do usuário](#access-user-variables-and-methods)
- [Registrar análise de dados](#log-analytics)
- [Mensagens no app (opcional)](#in-app-messages)
- [Content Cards (opcional)](#content-cards)
- [Próximas etapas](#next-steps)

### Criar BrazeManager.swift {#create-brazemanagerswift}

{% tabs local %}
{% tab Create BrazeManager swift %}

#### Criar BrazeManager.swift
Para construir o seu arquivo `BrazeManager.swift`, crie um novo arquivo Swift chamado _BrazeManager_ e adicione-o ao seu projeto no local desejado. Em seguida, substitua `import Foundation` por `import AppboyUI` para SPM (`import Appboy_iOS_SDK` para CocoaPods) e depois crie uma classe `BrazeManager` que será usada para hospedar todos os métodos e variáveis relacionados à Braze. `Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager` é uma classe `NSObject` e não uma struct, portanto pode estar em conformidade com delegates ABK, como o `ABKInAppMessageUIDelegate`.
- A `BrazeManager` é uma classe singleton por design, de modo que apenas uma instância dessa classe será usada. Isso é feito para fornecer um ponto de acesso unificado ao objeto.
{% endalert %}

1. Adicione uma variável estática chamada _shared_ que inicializa a classe `BrazeManager`. É garantido que ela será instanciada de forma lazy apenas uma vez.
2. Em seguida, adicione uma variável constante privada chamada _apiKey_ e defina-a como o valor da chave de API do seu espaço de trabalho no dashboard da Braze.
3. Adicione uma variável computada privada chamada _appboyOptions_, que armazenará valores de configuração para o SDK. Ela ficará vazia por enquanto.

{% subtabs global %}
{% subtab Swift %}

```swift
class BrazeManager: NSObject {
  // 1
  static let shared = BrazeManager()

  // 2
  private let apikey = "YOUR-API-KEY"

  // 3
  private var appboyOptions: [String:Any] {
    return [:]
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation BrazeManager

// 1
+ (instancetype)shared {
    static BrazeManager *shared = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        shared = [[BrazeManager alloc] init];
        // Do any other initialisation stuff here
    });
    return shared;
}

// 2
- (NSString *)apiKey {
  return @"YOUR-API-KEY";
}

// 3
- (NSDictionary *)appboyOptions {
  return [NSDictionary dictionary];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Inicializar o SDK {#initialize-the-sdk}

{% tabs local %}
{% tab Step 1: Initialize SDK from BrazeManager swift %}

#### Inicializar o SDK a partir do BrazeManager.swift {#initialize-sdk-from-brazemanagerswift}
Em seguida, você deve inicializar o SDK. Este guia pressupõe que você já [adicionou o SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) ao seu projeto Xcode. Você também deve ter o [endpoint de SDK do espaço de trabalho]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration#step-2-specify-your-data-cluster) e o [`LogLevel`]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#braze-log-level) configurados no seu arquivo `Info.plist` ou em `appboyOptions`.

Adicione o método `didFinishLaunchingWithOptions` do arquivo `AppDelegate.swift` sem um tipo de retorno no seu arquivo `BrazeManager.swift`. Ao criar um método semelhante no arquivo `BrazeManager.swift`, não haverá uma instrução `import AppboyUI` no seu arquivo `AppDelegate.swift`.

Em seguida, inicialize o SDK usando as variáveis `apiKey` e `appboyOptions` recém-declaradas.

{% alert important %}
A inicialização deve ser feita na thread principal.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Step 2: Handle Appboy Initialization %}

##### Lidar com a inicialização do Appboy no AppDelegate.swift {#handle-appboy-initialization-in-the-appdelegateswift}
Em seguida, navegue de volta ao arquivo `AppDelegate.swift` e adicione o seguinte snippet de código no método `didFinishLaunchingWithOptions` do AppDelegate para lidar com a inicialização do Appboy a partir do arquivo auxiliar `BrazeManager.swift`. Lembre-se, não há necessidade de adicionar uma instrução `import AppboyUI` no `AppDelegate.swift`.

{% subtabs global %}
{% subtab Swift %}

```swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
  // Override point for customization after application launch

  BrazeManager.shared.application(application, didFinishLaunchingWithOptions: launchOptions)

  return true
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Override point for customization after application launch

  [[BrazeManager shared] application:application didFinishLaunchingWithOptions:launchOptions];

  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Prossiga para compilar seu código e executar a aplicação.<br><br>Neste ponto, o SDK deve estar funcionando. No seu dashboard, observe que as sessões estão sendo registradas antes de avançar.
{% endalert %}

### Notificações por push {#push-notifications}

{% tabs local %}
{% tab Step 1: Add Push Certificate %}

#### Adicionar certificado de push {#add-push-certificate}

Navegue até o seu espaço de trabalho existente no dashboard da Braze. Em **Push Notification Settings**, faça upload do seu arquivo de certificado de push para o dashboard da Braze e salve.

![Configurações de notificação por push no dashboard da Braze com campos de upload de chave APNs.]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Step 2: Register for Notifications %}

{% alert important %}
Não perca o checkpoint dedicado no final desta etapa!
{% endalert %}

##### Registrar para notificações por push {#register-for-push-notifications}

Em seguida, registre para notificações por push. Este guia pressupõe que você [configurou suas credenciais de push corretamente]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) no portal de desenvolvedores da Apple e no projeto Xcode.

O código para registrar notificações por push será adicionado no método `didFinishLaunching...` no arquivo `BrazeManager.swift`. Seu código de inicialização deve ficar parecido com o seguinte:

1. Configure o conteúdo para solicitar autorização de interação com o usuário. Essas opções estão listadas como exemplo.
2. Solicite autorização para enviar notificações por push aos seus usuários. A resposta do usuário ao permitir ou negar as notificações por push é rastreada na variável `granted`.
3. Encaminhe os resultados da autorização de push para a Braze após o usuário interagir com o prompt de notificação.
4. Inicie o processo de registro com APNs; isso deve ser feito na thread principal. Se o registro for bem-sucedido, o app chama o método `didRegisterForRemoteNotificationsWithDeviceToken` do seu objeto `AppDelegate`.

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey:Any]?) {
  Appboy.start(withAPIKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
  // 1
  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  // 2
  UNUserNotificationCenter.current().requestAuthorization(option: options) { (granted, error) in
  // 3
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }

  // 4
  UIApplications.shared.registerForRemoteNotificiations()
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];

  // 1
  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);

  // 2
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
  // 3
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];

  // 4
  [[UIApplication sharedApplication] registerForRemoteNotifications];
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert checkpoint %}
Prossiga para compilar seu código e executar a aplicação.
- No seu app, confirme que está sendo solicitada a permissão para notificações por push antes de avançar.
- Se não for solicitado, tente excluir e reinstalar o app para garantir que o prompt de notificação por push não foi exibido anteriormente.

Observe que está sendo solicitada a permissão para notificações por push antes de avançar.
{% endalert %}

{% endtab %}
{% tab Step 3: Forward Methods %}

##### Encaminhar métodos de notificação por push {#forward-push-notification-methods}

Em seguida, encaminhe os métodos de notificação por push do sistema de `AppDelegate.swift` para `BrazeManager.swift` para serem tratados pelo SDK iOS da Braze.

###### Etapa 1: Criar extensão para código de notificação por push {#step-1-create-extension-for-push-notification-code}

Crie uma extensão para o seu código de notificação por push no arquivo `BrazeManager.swift` para que fique mais organizado quanto à finalidade que está sendo servida no arquivo auxiliar, assim:

1. Seguindo o padrão de não incluir uma instrução `import AppboyUI` no seu `AppDelegate`, trataremos os métodos de notificação por push no arquivo `BrazeManager.swift`. Os tokens de dispositivo dos usuários precisarão ser passados para a Braze a partir do método `didRegisterForRemote...`. Esse método é necessário para implementar notificações por push silenciosas. Em seguida, adicione o mesmo método do `AppDelegate` na sua classe `BrazeManager`.
2. Adicione a seguinte linha dentro do método para registrar o token de dispositivo na Braze. Isso é necessário para que a Braze associe o token ao dispositivo atual.

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK - Push Notifications
extension BrazeManager {
  // 1
  func application(
    _ application: UIApplication,
    didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
  ) {
    // 2
    Appboy.sharedInstance().?registerDeviceToken(deviceToken)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK - Push Notifications
// 1
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  // 2
  [[Appboy sharedInstance] registerDeviceToken:deviceToken];
}
```
{% endsubtab %}
{% endsubtabs %}

###### Etapa 2: Suportar notificações remotas {#step-2-support-remote-notifications}
Na guia **Signing & Capabilities**, adicione o suporte a **Background Modes** e selecione **Remote notifications** para começar a dar suporte a notificações por push remotas originadas da Braze.<br><br>![Signing & Capabilities]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### Etapa 3: Tratamento de notificações remotas {#step-3-remote-notification-handling}
O SDK da Braze pode tratar notificações por push remotas que se originam da Braze. Encaminhe as notificações remotas para a Braze; o SDK ignorará automaticamente as notificações por push que não se originam da Braze. Adicione o seguinte método ao seu arquivo `BrazeManager.swift` na extensão de notificação por push.

{% subtabs global %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication,
  didReceiveRemoteNotification userInfo: [AnyHashable : Any],
  fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
) {
  Appboy.sharedInstance()?.register(
    application,
    didReceiveRemoteNotification: userInfo,
    fetchCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application didReceiveRemoteNotification:userInfo fetchCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}

###### Etapa 4: Encaminhar respostas de notificação {#step-4-forward-notification-responses}

O SDK da Braze pode tratar a resposta das notificações por push que se originam da Braze. Encaminhe a resposta das notificações para a Braze; o SDK ignorará automaticamente as respostas de notificações por push que não se originam da Braze. Adicione o seguinte método ao seu arquivo `BrazeManager.swift`:

{% subtabs global %}
{% subtab Swift %}

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  didReceive response: UNNotificationResponse,
  withCompletionHandler completionHandler: @escaping () -> Void
) {
  Appboy.sharedInstance()?.userNotificationCenter(
    center,
    didReceive: response,
    withCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response
         withCompletionHandler:(void (^)(void))completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center
                   didReceiveNotificationResponse:response
                            withCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Prossiga para compilar seu código e executar a aplicação. <br><br>Tente enviar uma notificação por push para si mesmo a partir do dashboard da Braze e observe se a análise de dados está sendo registrada a partir das notificações por push antes de avançar.
{% endalert %}

### Acessar variáveis e métodos do usuário {#access-user-variables-and-methods}

{% tabs local %}
{% tab Create User Variables and Methods %}

#### Criar variáveis e métodos do usuário {#create-user-variables-and-methods}

Em seguida, você vai querer ter acesso fácil às variáveis e métodos do `ABKUser`. Crie uma extensão para o código do usuário no arquivo `BrazeManager.swift` para que fique mais organizado quanto à finalidade que está sendo servida no arquivo auxiliar, assim:

1. Um objeto `ABKUser` representa um usuário conhecido ou anônimo na sua aplicação iOS. Adicione uma variável computada para recuperar o `ABKUser`; essa variável será reutilizada para recuperar variáveis sobre o usuário.
2. Consulte a variável do usuário para acessar facilmente o `userId`. Entre as outras variáveis, o objeto `ABKUser` é responsável por (`firstName`, `lastName`, `phone`, `homeCity`, etc.)
3. Defina o usuário chamando `changeUser()` com um `userId` correspondente.

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK: - User
extension BrazeManager {
  // 1
  var user: ABKUser? {
    return Appboy.sharedInstance()?.user
  }

  // 2
  var userId: String? {
    return user?.userID
  }

  // 3
  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - User
  // 1
- (ABKUser *)user {
  return [[Appboy sharedInstance] user];
}

   // 2
- (NSString *)userId {
  return [self user].userID;
}

  // 3
- (void)changeUser:(NSString *)userId {
  [[Appboy sharedInstance] changeUser:userId];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Prossiga para compilar seu código e executar a aplicação.<br><br>Tente identificar usuários a partir de um login/cadastro bem-sucedido. Certifique-se de ter uma compreensão sólida do que é e do que não é um identificador de usuário apropriado. <br><br>No seu dashboard, observe que o identificador de usuário está sendo registrado antes de avançar.
{% endalert %}

### Registrar análise de dados {#log-analytics}

{% tabs local %}
{% tab Step 1: Custom Events %}

#### Criar método para registrar eventos personalizados {#create-log-custom-event-method}

Com base no método `logCustomEvent` do SDK da Braze a seguir, crie um método correspondente.

**Método de referência `logCustomEvent` da Braze**<br>
Isso é proposital, porque apenas o arquivo `BrazeManager.swift` pode acessar diretamente os métodos do SDK iOS da Braze. Portanto, ao criar um método correspondente, o resultado é o mesmo e é feito sem a necessidade de dependências diretas do SDK iOS da Braze no seu código de produção.

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**Método correspondente**<br>
Registre eventos personalizados a partir do objeto `Appboy` para a Braze. `Properties` é um parâmetro opcional com um valor padrão de nil. Eventos personalizados não precisam ter propriedades, mas precisam ter um nome.

{% subtabs global %}
{% subtab Swift %}
```swift
func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
  Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(nullable NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:properties];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 2: Custom Attributes %}

##### Criar método para registrar atributos personalizados {#create-log-custom-attributes-method}

O SDK pode registrar vários tipos como atributos personalizados. Não é necessário criar métodos auxiliares para cada tipo de valor que pode ser definido. Em vez disso, exponha apenas um método que pode filtrar para o valor apropriado.

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

Os atributos personalizados são registrados a partir do objeto `ABKUser`.

Crie **um método** que possa englobar todos os tipos disponíveis que podem ser definidos para um atributo. Adicione esse método no seu arquivo `BrazeManager.swift` na extensão de análise de dados. Isso pode ser feito filtrando os tipos de atributos personalizados válidos e chamando o método associado ao tipo correspondente.

- O parâmetro `value` é um tipo genérico que está em conformidade com o protocolo `Equatable`. Isso é feito explicitamente para que, se o tipo não for o esperado pelo SDK iOS da Braze, haja um erro em tempo de compilação.
- Os parâmetros `key` e `value` são parâmetros opcionais que serão desempacotados condicionalmente no método. Essa é apenas uma maneira de garantir que valores não nulos estejam sendo passados para o SDK iOS da Braze.

{% subtabs global %}
{% subtab Swift %}

```swift
func setCustomAttributeWithKey<T: Equatable>(_ key: String?, andValue value: T?) {
  guard let key = key, let value = value else { return }
  switch value.self {
  case let value as Date:
    user?.setCustomAttributeWithKey(key, andDateValue: value)
  case let value as Bool:
    user?.setCustomAttributeWithKey(key, andBOOLValue: value)
  case let value as String:
    user?.setCustomAttributeWithKey(key, andStringValue: value)
  case let value as Double:
    user?.setCustomAttributeWithKey(key, andDoubleValue: value)
  case let value as Int:
    user?.setCustomAttributeWithKey(key, andIntegerValue: value)
  default:
   return
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)setCustomAttributeWith:(NSString *)key andValue:(id)value {
  if ([value isKindOfClass:[NSDate class]]) {
    [[self user] setCustomAttributeWithKey:key andDateValue:value];
  } else if ([value isKindOfClass:[NSString class]]) {
    [[self user] setCustomAttributeWithKey:key andStringValue:value];
  } else if ([value isKindOfClass:[NSNumber class]]) {
    if (strcmp([value objCType], @encode(double)) == 0) {
      [[self user] setCustomAttributeWithKey:key andDoubleValue:[value doubleValue]];
    } else if (strcmp([value objCType], @encode(int)) == 0) {
      [[self user] setCustomAttributeWithKey:key andIntegerValue:[value integerValue]];
    } else if ([value boolValue]) {
      [[self user] setCustomAttributeWithKey:key andBOOLValue:[value boolValue]];
    }
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 3: Purchases %}

##### Criar método para registrar compras {#create-log-purchase-method}

Em seguida, com base no método `logPurchase` do SDK da Braze a seguir, crie um método correspondente.

**Método de referência `logPurchase` da Braze**<br>
Isso é proposital, porque apenas o arquivo `BrazeManager.swift` pode acessar diretamente os métodos do SDK iOS da Braze. Portanto, ao criar um método correspondente, o resultado é o mesmo e é feito sem a necessidade de dependências diretas do SDK iOS da Braze no seu código de produção.

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**Método correspondente**<br>
Registre compras a partir do objeto `Appboy` para a Braze. O SDK possui múltiplos métodos para registrar compras, e este é apenas um exemplo. Esse método também lida com a criação dos objetos `NSDecimal` e `UInt`. Como você deseja lidar com essa parte fica a seu critério, o que é fornecido é apenas um exemplo.

{% subtabs global %}
{% subtab Swift %}

```swift
func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price:
String, withQuantity quantity: Int) {

  Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quantity))

}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPurchase:(NSString *)productIdentifier inCurrency:(nonnull NSString *)currencyCode atPrice:(nonnull NSDecimalNumber *)price withQuantity:(NSUInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currencyCode atPrice:price withQuantity:quantity];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Prossiga para compilar seu código e executar a aplicação. <br><br>Tente registrar eventos personalizados.<br><br>No seu dashboard, observe que os eventos personalizados estão sendo registrados antes de avançar.
{% endalert %}

### Mensagens no app {#in-app-messages}

{% tabs local %}
{% tab Step 1: Conform to Delegate %}

{% alert important %}
A seguinte seção de mensagens no app não é obrigatória para a integração se você não planeja usar esse canal na sua aplicação.
{% endalert %}

#### Estar em conformidade com ABKInAppMessageUIDelegate {#conform-to-abkinappmessageuidelegate}

Em seguida, habilite o código do seu arquivo `BrazeManager.swift` para estar em conformidade com o `ABKInAppMessageUIDelegate` para tratar diretamente os métodos associados.

O código para estar em conformidade com o delegate será adicionado nos métodos `didFinishLaunching...` no arquivo `BrazeManager.swift`. Seu código de inicialização deve ficar assim:

{% subtabs global %}
{% subtab swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()

  Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];

  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];

  [[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 2: Add Delegate Methods %}

##### Adicionar métodos do delegate {#add-delegate-methods}
Em seguida, crie uma extensão que esteja em conformidade com o `ABKInAppMessageUIDelegate`.

Adicione o seguinte snippet na seção de análise de dados. Observe que o objeto `BrazeManager.swift` é definido como o delegate; é aqui que o arquivo `BrazeManager.swift` tratará todos os métodos do `ABKInAppMessageUIDelegate`.

{% alert important %}
O `ABKInAppMessageUIDelegate` não vem com nenhum método obrigatório, mas o seguinte é um exemplo de um.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - ABKInAppMessage UI Delegate
extension AppboyManager: ABKInAppMessageUIDelegate{
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return ABKInAppMessageSlideupViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageModal:
      return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageFull:
      return ABKInAppMessageFullViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - ABKInAppMessage UI Delegate
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [[ABKInAppMessageSlideupViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [[ABKInAppMessageFullViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  }
  return nil;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Prossiga para compilar seu código e executar a aplicação. <br><br>Tente enviar uma mensagem no app para si mesmo. <br><br>No arquivo `BrazeManager.swift`, defina um breakpoint na entrada do método de exemplo `ABKInAppMessageUIDelegate`. Envie uma mensagem no app para si mesmo e confirme que o breakpoint foi atingido antes de avançar.
{% endalert %}

### Content Cards {#content-cards}

{% tabs local %}
{% tab Create Content Card Variables and Methods %}

{% alert important %}
A seguinte seção de Content Cards não é obrigatória para a integração se você não planeja usar esse canal na sua aplicação.
{% endalert %}

#### Criar variáveis e métodos de Content Cards {#create-content-card-variables-and-methods}

Habilite seu código de produção a exibir o view controller de Content Cards sem a necessidade de instruções `import AppboyUI` desnecessárias.

Crie uma extensão para o código de Content Cards no seu arquivo `BrazeManager.swift`, para que fique mais organizado quanto à finalidade que está sendo servida no arquivo auxiliar, assim:

1. Exiba o `ABKContentCardsTableViewController`. Um `navigationController` opcional é o único parâmetro necessário para apresentar ou empurrar nosso view controller.
2. Inicialize um objeto `ABKContentCardsTableViewController` e opcionalmente altere o título. Você também deve adicionar o view controller inicializado à pilha de navegação.

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - Content Cards
extension BrazeManager {

  // 1
  func displayContentCards(navigationController: UINavigationController?) {

    // 2
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "Content Cards"
    navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - Content Cards
  // 1
- (void)displayContentCards:(UINavigationController *)navigationController {
  // 2
  ABKContentCardsTableViewController *contentCardsVc = [[ABKContentCardsTableViewController alloc] init];
  contentCardsVc.title = @"Content Cards";
  [navigationController pushViewController:contentCardsVc animated:YES];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Prossiga para compilar seu código e executar a aplicação.<br><br>Tente exibir o `ABKContentCardsTableViewController` na sua aplicação antes de avançar.
{% endalert %}

## Próximos passos {#next-steps}

Parabéns! Você concluiu este guia de práticas recomendadas de integração! Um exemplo do arquivo auxiliar `BrazeManager` pode ser encontrado no [GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift).

Agora que você desacoplou todas as dependências do SDK da Braze para iOS do restante do seu código de produção, confira alguns dos nossos guias opcionais de implementação avançada:

{% article_tiles %}
- name: Guia de implementação avançada de notificações por push
  link: /docs/developer_guide/platforms/legacy_sdks/ios/push_notifications/implementation_guide
  description: Padrões avançados opcionais para personalizar o comportamento de notificações por push no seu app iOS.
- name: Guia de implementação avançada de mensagens no app
  link: /docs/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide
  description: Padrões avançados opcionais para personalizar a entrega e exibição de mensagens no app.
- name: Guia de implementação avançada de Content Cards
  link: /docs/developer_guide/platforms/legacy_sdks/ios/content_cards/implementation_guide
  description: Padrões avançados opcionais para personalizar feeds e a interface de Content Cards.
{% endarticle_tiles %}