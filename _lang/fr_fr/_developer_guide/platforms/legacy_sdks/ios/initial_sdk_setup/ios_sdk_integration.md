---
nav_title: Guide d'intégration SDK (facultatif)
article_title: Guide d'intégration SDK de Braze pour iOS (facultatif)
alias: "/ios_sdk/"
description: "Ce guide d'intégration iOS vous accompagne étape par étape dans les meilleures pratiques de configuration lors de la première intégration du SDK iOS et de ses principaux composants dans votre application. Ce guide vous aidera à créer un fichier d'aide BrazeManager.swift."
page_order: 10
platform: iOS

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Guide d'intégration SDK de Braze pour iOS {#braze-ios-sdk-integration-guide}

> Ce guide d'intégration iOS facultatif vous accompagne étape par étape dans les meilleures pratiques de configuration lors de la première intégration du SDK iOS et de ses principaux composants dans votre application. Ce guide vous aidera à créer un fichier d'aide `BrazeManager.swift` qui découplera toutes les dépendances du SDK Braze pour iOS du reste de votre code de production, ce qui se traduira par un seul `import AppboyUI` dans l'ensemble de votre application. Cette approche limite les problèmes liés aux importations excessives du SDK, ce qui facilite le suivi, le débogage et la modification du code.

{% alert important %}
Ce guide suppose que vous avez déjà [ajouté le SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) à votre projet Xcode.
{% endalert %}

## Présentation de l'intégration {#integration-overview}

Les étapes suivantes vous aident à créer un fichier d'aide `BrazeManager` qui sera appelé par votre code de production. Ce fichier d'aide traitera toutes les dépendances liées à Braze en ajoutant diverses extensions pour les sujets d'intégration suivants. Chaque sujet inclura des étapes sous forme d'onglets horizontaux et des extraits de code en Swift et en Objective-C. Notez que les étapes relatives aux Content Cards et aux messages in-app ne sont pas nécessaires pour l'intégration si vous ne prévoyez pas d'utiliser ces canaux dans votre application.

- [Créer BrazeManager.swift](#create-brazemanagerswift)
- [Initialiser le SDK](#initialize-the-sdk)
- [Notifications push](#push-notifications)
- [Accéder aux variables et méthodes utilisateur](#access-user-variables-and-methods)
- [Enregistrer les analyses](#log-analytics)
- [Messages in-app (facultatif)](#in-app-messages)
- [Content Cards (facultatif)](#content-cards)
- [Étapes suivantes](#next-steps)

### Créer BrazeManager.swift {#create-brazemanagerswift}

{% tabs local %}
{% tab Create BrazeManager swift %}

#### Créer BrazeManager.swift
Pour créer votre fichier `BrazeManager.swift`, créez un nouveau fichier Swift nommé _BrazeManager_ à ajouter à votre projet à l'emplacement souhaité. Ensuite, remplacez `import Foundation` par `import AppboyUI` pour SPM (`import Appboy_iOS_SDK` pour CocoaPods), puis créez une classe `BrazeManager` qui servira à héberger toutes les méthodes et variables liées à Braze. `Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager` est une classe `NSObject` et non une structure, ce qui lui permet de se conformer aux délégués ABK tels que `ABKInAppMessageUIDelegate`.
- La classe `BrazeManager` est un singleton par conception, de sorte qu'une seule instance de cette classe sera utilisée. Cela permet de fournir un point d'accès unifié à l'objet.
{% endalert %}

1. Ajoutez une variable statique nommée _shared_ qui initialise la classe `BrazeManager`. Il est garanti qu'elle ne sera initialisée paresseusement qu'une seule fois.
2. Ensuite, ajoutez une variable constante privée nommée _apiKey_ et définissez-la comme la valeur de la clé API de votre espace de travail dans le tableau de bord de Braze.
3. Ajoutez une variable calculée privée nommée _appboyOptions_ qui stockera les valeurs de configuration pour le SDK. Elle sera vide pour l'instant.

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

### Initialiser le SDK {#initialize-the-sdk}

{% tabs local %}
{% tab Step 1: Initialize SDK from BrazeManager swift %}

#### Initialiser le SDK à partir de BrazeManager.swift {#initialize-sdk-from-brazemanagerswift}
Ensuite, vous devez initialiser le SDK. Ce guide suppose que vous avez déjà [ajouté le SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) à votre projet Xcode. Vous devez également avoir défini l'[endpoint SDK de votre espace de travail]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration#step-2-specify-your-data-cluster) et le [`LogLevel`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations#braze-log-level) dans votre fichier `Info.plist` ou dans `appboyOptions`.

Ajoutez la méthode `didFinishLaunchingWithOptions` du fichier `AppDelegate.swift` sans type de retour dans votre fichier `BrazeManager.swift`. En créant une méthode similaire dans le fichier `BrazeManager.swift`, il n'y aura pas de déclaration `import AppboyUI` dans votre fichier `AppDelegate.swift`.

Ensuite, initialisez le SDK en utilisant vos variables nouvellement déclarées `apiKey` et `appboyOptions`.

{% alert important %}
L'initialisation doit être effectuée dans le thread principal.
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

##### Gérer l'initialisation Appboy dans AppDelegate.swift {#handle-appboy-initialization-in-the-appdelegateswift}
Ensuite, revenez au fichier `AppDelegate.swift` et ajoutez l'extrait de code suivant dans la méthode `didFinishLaunchingWithOptions` de l'AppDelegate pour gérer l'initialisation Appboy à partir du fichier d'aide `BrazeManager.swift`. N'oubliez pas qu'il n'est pas nécessaire d'ajouter une déclaration `import AppboyUI` dans `AppDelegate.swift`.

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
Procédez à la compilation de votre code et exécutez votre application.<br><br>À ce stade, le SDK devrait être opérationnel. Dans votre tableau de bord, vérifiez que les sessions sont bien enregistrées avant de poursuivre.
{% endalert %}

### Notifications push {#push-notifications}

{% tabs local %}
{% tab Step 1: Add Push Certificate %}

#### Ajouter un certificat push {#add-push-certificate}

Accédez à votre espace de travail existant dans le tableau de bord de Braze. Sous **Paramètres des notifications push**, téléchargez votre fichier de certificat push dans votre tableau de bord de Braze et enregistrez-le.

![Paramètres des notifications push du tableau de bord de Braze avec les champs de téléchargement de clé APNs.]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Step 2: Register for Notifications %}

{% alert important %}
Ne manquez pas le point de contrôle dédié à la fin de cette étape !
{% endalert %}

##### S'inscrire aux notifications push {#register-for-push-notifications}

Ensuite, inscrivez-vous aux notifications push. Ce guide suppose que vous avez [correctement configuré vos identifiants push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) dans votre portail développeur Apple et dans votre projet Xcode.

Le code d'inscription aux notifications push sera ajouté dans la méthode `didFinishLaunching...` du fichier `BrazeManager.swift`. Votre code d'initialisation devrait ressembler à ceci :

1. Configurez le contenu pour demander l'autorisation d'interagir avec l'utilisateur. Ces options sont présentées à titre d'exemple.
2. Demandez l'autorisation d'envoyer des notifications push à vos utilisateurs. La réponse de l'utilisateur (autoriser ou refuser les notifications push) est suivie dans la variable `granted`.
3. Transmettez les résultats d'autorisation push à Braze après que l'utilisateur a interagi avec l'invite de notification.
4. Lancez le processus d'inscription auprès des APNs ; cela doit être fait dans le thread principal. Si l'inscription réussit, l'application appelle la méthode `didRegisterForRemoteNotificationsWithDeviceToken` de l'objet `AppDelegate`.

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
Procédez à la compilation de votre code et exécutez votre application.
- Dans votre application, confirmez que vous êtes invité à autoriser les notifications push avant de poursuivre.
- Si vous n'êtes pas invité, essayez de supprimer et de réinstaller l'application pour vous assurer que l'invite de notification push n'a pas déjà été affichée.

Vérifiez que vous êtes bien invité à autoriser les notifications push avant de poursuivre.
{% endalert %}

{% endtab %}
{% tab Step 3: Forward Methods %}

##### Transmettre les méthodes de notification push {#forward-push-notification-methods}

Ensuite, transmettez les méthodes système de notification push de `AppDelegate.swift` vers `BrazeManager.swift` pour qu'elles soient gérées par le SDK Braze pour iOS.

###### Étape 1 : Créer une extension pour le code de notification push {#step-1-create-extension-for-push-notification-code}

Créez une extension pour votre code de notification push dans votre fichier `BrazeManager.swift` afin qu'il soit organisé de manière plus lisible quant à l'objectif servi dans le fichier d'aide :

1. En suivant le modèle de non-inclusion d'une déclaration `import AppboyUI` dans votre `AppDelegate`, nous allons gérer les méthodes de notification push dans le fichier `BrazeManager.swift`. Les jetons d'appareil de l'utilisateur devront être transmis à Braze depuis la méthode `didRegisterForRemote...`. Cette méthode est requise pour implémenter les notifications push silencieuses. Ensuite, ajoutez la même méthode de `AppDelegate` dans votre classe `BrazeManager`.
2. Ajoutez la ligne suivante à l'intérieur de la méthode pour enregistrer le jeton d'appareil auprès de Braze. Ceci est nécessaire pour que Braze associe le jeton à l'appareil actuel.

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

###### Étape 2 : Prendre en charge les notifications à distance {#step-2-support-remote-notifications}
Dans l'onglet **Signing & Capabilities**, ajoutez la prise en charge des **Background Modes** et sélectionnez **Remote notifications** pour commencer à prendre en charge les notifications push à distance provenant de Braze.<br><br>![Signing & Capabilities]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### Étape 3 : Gestion des notifications à distance {#step-3-remote-notification-handling}
Le SDK Braze peut gérer les notifications push à distance provenant de Braze. Transmettez les notifications à distance à Braze ; le SDK ignorera automatiquement les notifications push qui ne proviennent pas de Braze. Ajoutez la méthode suivante à votre fichier `BrazeManager.swift` dans l'extension de notification push.

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

###### Étape 4 : Transmettre les réponses aux notifications {#step-4-forward-notification-responses}

Le SDK Braze peut gérer la réponse des notifications push provenant de Braze. Transmettez la réponse des notifications à Braze ; le SDK ignorera automatiquement les réponses des notifications push qui ne proviennent pas de Braze. Ajoutez la méthode suivante à votre fichier `BrazeManager.swift` :

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
Procédez à la compilation de votre code et exécutez votre application. <br><br>Essayez de vous envoyer une notification push depuis le tableau de bord de Braze et vérifiez que les analyses sont bien enregistrées à partir des notifications push avant de poursuivre.
{% endalert %}

### Accéder aux variables et méthodes utilisateur {#access-user-variables-and-methods}

{% tabs local %}
{% tab Create User Variables and Methods %}

#### Créer des variables et des méthodes utilisateur {#create-user-variables-and-methods}

Ensuite, vous souhaiterez accéder facilement aux variables et méthodes `ABKUser`. Créez une extension pour votre code utilisateur dans le fichier `BrazeManager.swift` afin qu'il soit organisé de manière plus lisible quant à l'objectif servi dans le fichier d'aide :

1. Un objet `ABKUser` représente un utilisateur connu ou anonyme dans votre application iOS. Ajoutez une variable calculée pour récupérer l'`ABKUser` ; cette variable sera réutilisée pour récupérer des informations sur l'utilisateur.
2. Interrogez la variable utilisateur pour accéder facilement au `userId`. Parmi les autres variables, l'objet `ABKUser` est responsable de (`firstName`, `lastName`, `phone`, `homeCity`, etc.)
3. Définissez l'utilisateur en appelant `changeUser()` avec un `userId` correspondant.

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
Procédez à la compilation de votre code et exécutez votre application.<br><br>Essayez d'identifier les utilisateurs à partir d'une connexion ou d'une inscription réussie. Assurez-vous de bien comprendre ce qui constitue ou non un identifiant utilisateur approprié. <br><br>Dans votre tableau de bord, vérifiez que l'identifiant utilisateur est bien enregistré avant de poursuivre.
{% endalert %}

### Enregistrer les analyses {#log-analytics}

{% tabs local %}
{% tab Step 1: Custom Events %}

#### Créer une méthode de journalisation d'événements personnalisés {#create-log-custom-event-method}

En vous basant sur la méthode `logCustomEvent` du SDK Braze suivante, créez une méthode correspondante.

**Méthode de référence `logCustomEvent` de Braze**<br>
Cela est fait par conception, car seul le fichier `BrazeManager.swift` peut accéder directement aux méthodes du SDK Braze pour iOS. Par conséquent, en créant une méthode correspondante, le résultat est le même et se fait sans avoir besoin de dépendances directes sur le SDK Braze pour iOS dans votre code de production.

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**Méthode correspondante**<br>
Enregistrez les événements personnalisés depuis l'objet `Appboy` vers Braze. `Properties` est un paramètre facultatif avec une valeur par défaut de nil. Les événements personnalisés n'ont pas besoin d'avoir des propriétés, mais doivent avoir un nom.

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

##### Créer une méthode de journalisation d'attributs personnalisés {#create-log-custom-attributes-method}

Le SDK peut enregistrer plusieurs types comme attributs personnalisés. Il n'est pas nécessaire de créer des méthodes d'aide pour chaque type de valeur pouvant être défini. À la place, exposez une seule méthode permettant de filtrer jusqu'à la valeur appropriée.

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

Les attributs personnalisés sont enregistrés depuis l'objet `ABKUser`.

Créez **une méthode** pouvant englober tous les types disponibles pouvant être définis pour un attribut. Ajoutez cette méthode dans votre fichier `BrazeManager.swift` dans l'extension d'analyse. Cela peut être fait en filtrant les types d'attributs personnalisés valides et en appelant la méthode associée au type correspondant.

- Le paramètre `value` est un type générique conforme au protocole `Equatable`. Cela est fait explicitement, de sorte que si le type n'est pas celui attendu par le SDK Braze pour iOS, il y aura une erreur de compilation.
- Les paramètres `key` et `value` sont des paramètres facultatifs qui seront conditionnellement déballés dans la méthode. C'est un moyen de s'assurer que des valeurs non nulles sont transmises au SDK Braze pour iOS.

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

##### Créer une méthode de journalisation des achats {#create-log-purchase-method}

Ensuite, en vous basant sur la méthode `logPurchase` du SDK Braze suivante, créez une méthode correspondante.

**Méthode de référence `logPurchase` de Braze**<br>
Cela est fait par conception, car seul le fichier `BrazeManager.swift` peut accéder directement aux méthodes du SDK Braze pour iOS. Par conséquent, en créant une méthode correspondante, le résultat est le même et se fait sans avoir besoin de dépendances directes sur le SDK Braze pour iOS dans votre code de production.

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**Méthode correspondante**<br>
Enregistrez les achats depuis l'objet `Appboy` vers Braze. Le SDK dispose de plusieurs méthodes pour enregistrer les achats, et ceci n'est qu'un exemple. Cette méthode gère également la création des objets `NSDecimal` et `UInt`. La façon dont vous souhaitez gérer cette partie vous appartient ; un seul exemple est fourni.

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
Procédez à la compilation de votre code et exécutez votre application. <br><br>Essayez d'enregistrer des événements personnalisés.<br><br>Dans votre tableau de bord, vérifiez que les événements personnalisés sont bien enregistrés avant de poursuivre.
{% endalert %}

### Messages in-app {#in-app-messages}

{% tabs local %}
{% tab Step 1: Conform to Delegate %}

{% alert important %}
La section suivante relative aux messages in-app n'est pas nécessaire pour l'intégration si vous ne prévoyez pas d'utiliser ce canal dans votre application.
{% endalert %}

#### Se conformer à ABKInAppMessageUIDelegate {#conform-to-abkinappmessageuidelegate}

Ensuite, activez votre code du fichier `BrazeManager.swift` pour se conformer à `ABKInAppMessageUIDelegate` afin de gérer directement les méthodes associées.

Le code de conformité au délégué sera ajouté dans les méthodes `didFinishLaunching...` du fichier `BrazeManager.swift`. Votre code d'initialisation devrait ressembler à ceci :

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

##### Ajouter les méthodes du délégué {#add-delegate-methods}
Ensuite, créez une extension conforme à `ABKInAppMessageUIDelegate`.

Ajoutez l'extrait de code suivant dans la section d'analyse. Notez que l'objet `BrazeManager.swift` est défini comme délégué ; c'est là que le fichier `BrazeManager.swift` traitera toutes les méthodes `ABKInAppMessageUIDelegate`.

{% alert important %}
`ABKInAppMessageUIDelegate` ne comporte aucune méthode requise, mais voici un exemple.
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
Procédez à la compilation de votre code et exécutez votre application. <br><br>Essayez de vous envoyer un message in-app. <br><br>Dans le fichier `BrazeManager.swift`, définissez un point d'arrêt à l'entrée de la méthode `ABKInAppMessageUIDelegate` donnée en exemple. Envoyez-vous un message in-app et confirmez que le point d'arrêt est atteint avant de poursuivre.
{% endalert %}

### Content Cards {#content-cards}

{% tabs local %}
{% tab Create Content Card Variables and Methods %}

{% alert important %}
La section suivante relative aux Content Cards n'est pas nécessaire pour l'intégration si vous ne prévoyez pas d'utiliser ce canal dans votre application.
{% endalert %}

#### Créer des variables et des méthodes pour les Content Cards {#create-content-card-variables-and-methods}

Activez votre code de production pour afficher le contrôleur de vue des Content Cards sans avoir besoin de déclarations `import AppboyUI` inutiles.

Créez une extension pour votre code Content Cards dans votre fichier `BrazeManager.swift` afin qu'il soit organisé de manière plus lisible quant à l'objectif servi dans le fichier d'aide :

1. Affichez le `ABKContentCardsTableViewController`. Un `navigationController` facultatif est le seul paramètre nécessaire pour présenter ou pousser notre contrôleur de vue.
2. Initialisez un objet `ABKContentCardsTableViewController` et modifiez éventuellement le titre. Vous devez également ajouter le contrôleur de vue initialisé à la pile de navigation.

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
Procédez à la compilation de votre code et exécutez votre application.<br><br>Essayez d'afficher le `ABKContentCardsTableViewController` dans votre application avant de poursuivre.
{% endalert %}

## Étapes suivantes {#next-steps}

Félicitations ! Vous avez terminé ce guide d'intégration des meilleures pratiques ! Vous trouverez un exemple de fichier d'aide `BrazeManager` sur [GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift).

Maintenant que vous avez découplé toutes les dépendances du SDK Braze pour iOS du reste de votre code de production, consultez certains de nos guides d'implémentation avancée facultatifs :
- [Guide d'implémentation avancée des notifications push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/implementation_guide)
- [Guide d'implémentation avancée des messages in-app]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide)
- [Guide d'implémentation avancée des Content Cards]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/implementation_guide)