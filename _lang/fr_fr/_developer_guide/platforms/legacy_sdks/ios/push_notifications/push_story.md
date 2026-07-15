---
nav_title: Push Stories
article_title: Push Stories pour iOS
platform: iOS
page_order: 27
description: "Cet article de référence montre comment configurer les Push Stories pour votre application iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configurer les Push Stories {#push-story-setup}

La fonctionnalité Push Stories nécessite le framework `UNNotification` et iOS 10. Cette fonctionnalité est uniquement disponible à partir du SDK iOS version 3.2.1.

## Étape 1 : Activer les notifications push dans votre application {#step-1-enable-push-in-your-app}

Suivez l'[intégration de la notification push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) pour activer le push dans votre application.

## Étape 2 : Ajouter la cible de l'extension de contenu de notification {#step-2-adding-the-notification-content-extension-target}

Dans votre projet d'application, sélectionnez **File > New > Target...**, ajoutez une nouvelle cible `Notification Content Extension` et activez-la.

![Dans votre projet d'application, sélectionnez File > New > Target... et ajoutez une nouvelle cible Notification Content Extension et activez-la.]({% image_buster /assets/img/ios/push_story/add_content_extension.png %})

Xcode devrait générer une nouvelle cible et créer automatiquement des fichiers pour vous, notamment :

{% tabs %}
{% tab OBJECTIVE-C %}

- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

{% endtab %}
{% tab swift %}

- `NotificationViewController.swift`
- `MainInterface.storyboard`

{% endtab %}
{% endtabs %}

## Étape 3 : Activer les capacités {#step-3-enable-capabilities}

La fonctionnalité Push Stories nécessite le mode arrière-plan dans la section **Capabilities** de la cible principale de l'application. Après avoir activé les modes d'arrière-plan, sélectionnez **Background fetch** et **Remote notifications**.

![La fonctionnalité Push Stories nécessite le mode arrière-plan dans la section Capabilities de la cible principale de l'application. Après avoir activé les modes d'arrière-plan, sélectionnez Background fetch et Remote notifications.]({% image_buster /assets/img/ios/push_story/enable_background_mode.png %})

### Ajouter un groupe d'applications {#adding-an-app-group}

Vous devez également ajouter `Capability App Groups`. Si vous n'avez pas de groupe d'applications dans votre application, sélectionnez la **Capability** de la cible principale de l'application, activez les `App Groups` et cliquez sur le bouton **+**. Utilisez l'identifiant de bundle de votre application pour créer le groupe d'applications. Par exemple, si l'identifiant de bundle de votre application est `com.company.appname`, vous pouvez nommer votre groupe d'applications `group.com.company.appname.xyz`. Vous devez activer les `App Groups` pour les cibles de l'application principale et de l'extension de contenu.

{% alert important %}
Dans ce contexte, `App Groups` fait référence aux [droits des groupes d'applications](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) d'Apple et non à votre ID d'espace de travail Braze (anciennement groupe d'applications).
{% endalert %}

Si vous n'ajoutez pas votre application à un groupe d'applications, votre application risque de ne pas remplir certains champs de la charge utile push et ne fonctionnera pas complètement comme prévu.

## Étape 4 : Ajouter le framework Push Stories à votre application {#step-4-adding-the-push-story-framework-to-your-app}

{% tabs local %}
{% tab Swift Package Manager %}

Après avoir suivi le [guide d'intégration du gestionnaire de paquets Swift]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager), ajoutez `AppboyPushStory` à votre `Notification Content Extension` :

![Dans Xcode, sous frameworks et bibliothèques, sélectionnez l'icône « + » pour ajouter un framework.]({% image_buster /assets/img/ios/push_story/spm1.png %})

![Après avoir suivi le guide d'intégration du gestionnaire de paquets Swift, ajoutez AppboyPushStory à votre Notification Content Extension.]({% image_buster /assets/img/ios/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Ajoutez la ligne suivante à votre Podfile :

```ruby
target 'YourContentExtensionTarget' do
  pod 'Appboy-Push-Story'
end
```

Après avoir mis à jour le Podfile, naviguez jusqu'au répertoire de votre projet d'application Xcode dans votre terminal et exécutez `pod install`.

{% endtab %}
{% tab Manual %}

Téléchargez la dernière version de `AppboyPushStory.zip` depuis la [page de versions GitHub](https://github.com/Appboy/appboy-ios-sdk/releases), décompressez-la et ajoutez les fichiers suivants à l'`Notification Content Extension` de votre projet :
- `Resources/ABKPageView.nib`
- `AppboyPushStory.xcframework`

![Téléchargez la dernière version de AppboyPushStory.zip depuis la page de versions GitHub, décompressez-la et ajoutez les fichiers suivants à l'extension de contenu de notification de votre projet.]({% image_buster /assets/img/ios/push_story/manual1.png %})

{% alert important %}
Assurez-vous que **Do Not Embed** est sélectionné pour **AppboyPushStory.xcframework** dans la colonne **Embed**.
{% endalert %}

Ajoutez l'indicateur `-ObjC` à l'`Notification Content Extension` de votre projet dans **Build Settings > Other Linker Flags**.

{% endtab %}
{% endtabs %}

## Étape 5 : Mettre à jour votre contrôleur de vue de notification {#step-5-updating-your-notification-view-controller}

{% tabs %}
{% tab OBJECTIVE-C %}

Dans votre `NotificationViewController.h`, ajoutez les lignes suivantes pour ajouter de nouvelles propriétés et importer les fichiers d'en-tête :

```objc
#import <AppboyPushStory/AppboyPushStory.h>
```

```objc
@property (nonatomic) IBOutlet ABKStoriesView *storiesView;
@property (nonatomic) ABKStoriesViewDataSource *dataSource;
```

Dans votre `NotificationViewController.m`, supprimez l'implémentation par défaut et ajoutez le code suivant :

```objc
@implementation NotificationViewController

- (void)didReceiveNotification:(UNNotification *)notification {
  self.dataSource = [[ABKStoriesViewDataSource alloc] initWithNotification:notification
                                                               storiesView:self.storiesView
                                                                  appGroup:@"YOUR-APP-GROUP-IDENTIFIER"];
}

- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response
                     completionHandler:(void (^)(UNNotificationContentExtensionResponseOption option))completion {
  UNNotificationContentExtensionResponseOption option = [self.dataSource didReceiveNotificationResponse:response];
  completion(option);
}

- (void)viewWillDisappear:(BOOL)animated {
  [self.dataSource viewWillDisappear];
  [super viewWillDisappear:animated];
}

@end
```

{% endtab %}
{% tab swift %}

Dans votre `NotificationViewController.swift`, ajoutez la ligne suivante pour importer les fichiers d'en-tête :

```swift
import AppboyPushStory
```

Ensuite, supprimez l'implémentation par défaut et ajoutez le code suivant :

```swift
class NotificationViewController: UIViewController, UNNotificationContentExtension {

  @IBOutlet weak var storiesView: ABKStoriesView!
  var dataSource: ABKStoriesViewDataSource?

  func didReceive(_ notification: UNNotification) {
    dataSource = ABKStoriesViewDataSource(notification: notification, storiesView: storiesView, appGroup: "YOUR-APP-GROUP-IDENTIFIER")
  }

  func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    if dataSource != nil {
      let option: UNNotificationContentExtensionResponseOption = dataSource!.didReceive(response)
      completion(option)
    }
  }

  override func viewWillDisappear(_ animated: Bool) {
    dataSource?.viewWillDisappear()
    super.viewWillDisappear(animated)
  }
}
```

{% endtab %}
{% endtabs %}

## Étape 6 : Configurer le storyboard de l'extension de contenu de notification {#step-6-set-the-notification-content-extension-storyboard}

Ouvrez le storyboard `Notification Content Extension` et placez un nouveau `UIView` dans le contrôleur de vue de notification. Renommez la classe en `ABKStoriesView`. Faites en sorte que la largeur et la hauteur de la vue soient redimensionnables automatiquement pour correspondre au cadre de la vue principale du contrôleur de vue de notification.

![Ouvrez le storyboard Notification Content Extension et placez un nouveau UIView dans le contrôleur de vue de notification. Renommez la classe en ABKStoriesView. Faites en sorte que la largeur et la hauteur de la vue soient redimensionnables automatiquement pour correspondre au cadre de la vue principale du contrôleur de vue de notification.]({% image_buster /assets/img/ios/push_story/abkstoriesview_class.png %})

![Ouvrez le storyboard Notification Content Extension et placez un nouveau UIView dans le contrôleur de vue de notification. Renommez la classe en ABKStoriesView. Faites en sorte que la largeur et la hauteur de la vue soient redimensionnables automatiquement pour correspondre au cadre de la vue principale du contrôleur de vue de notification.]({% image_buster /assets/img/ios/push_story/abkstoriesview_size.png %})

Ensuite, liez l'IBOutlet `storiesView` du contrôleur de vue de notification au `ABKStoriesView` ajouté.

![Capture d'écran relative à l'étape 6 : configurer le storyboard de l'extension de contenu de notification.]({% image_buster /assets/img/ios/push_story/abkstoriesview_outlet.png %})

## Étape 7 : Configurer le plist de l'extension de contenu de notification {#step-7-set-the-notification-content-extension-plist}

Ouvrez le fichier `Info.plist` de `Notification Content Extension` et ajoutez et modifiez les clés suivantes dans `NSExtension \ NSExtensionAttributes` :

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2` (type `String`)
`UNNotificationExtensionDefaultContentHidden` = `YES` (type `Boolean`)
`UNNotificationExtensionInitialContentSizeRatio` = `0.65` (type `Number`)

![Capture d'écran relative à l'étape 7 : configurer le plist de l'extension de contenu de notification.]({% image_buster /assets/img/ios/push_story/notificationcontentextension_plist.png %})

## Étape 8 : Mettre à jour l'intégration Braze dans votre application principale {#step-8-updating-the-braze-integration-in-your-main-app}

### Option 1 : Exécution {#option-1-runtime}

Dans le dictionnaire `appboyOptions` utilisé pour configurer votre instance Braze, ajoutez une entrée `ABKPushStoryAppGroupKey` et définissez la valeur sur l'identifiant API de votre espace de travail.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKPushStoryAppGroupKey] = @"YOUR-APP-GROUP-IDENTIFIER";
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKPushStoryAppGroupKey : "YOUR-APP-GROUP-IDENTIFIER"
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endtab %}
{% endtabs %}

#### Option 2 : Info.plist {#option-2-infoplist}

Alternativement, pour configurer l'espace de travail Push Stories à partir de votre fichier `Info.plist`, ajoutez un dictionnaire nommé `Braze` à votre fichier `Info.plist`. Dans le dictionnaire `Braze`, ajoutez une sous-entrée `PushStoryAppGroup` de type chaîne de caractères et définissez la valeur sur l'identifiant de votre espace de travail. Notez qu'avant le SDK Braze pour iOS v4.0.2, la clé du dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

## Étapes suivantes {#next-steps}

Reportez-vous ensuite aux étapes relatives à l'intégration des [boutons d'action]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons), qui est nécessaire pour que les boutons s'affichent dans un message Push Stories.