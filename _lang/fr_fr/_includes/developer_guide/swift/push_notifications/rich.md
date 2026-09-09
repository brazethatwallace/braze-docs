{% multi_lang_include developer_guide/prerequisites/swift.md %} Il vous sera également nécessaire de [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Mise en place de notifications push riches {#setting-up-rich-push-notifications}

### Étape 1 : Créer une extension de service de notification {#step-1-creating-a-service-extension}

Pour créer une [extension de service de notification](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension), accédez à **File > New > Target** dans Xcode et sélectionnez **Notification Service Extension**.

![Le sélecteur de cible Xcode pour créer une extension de service de notification pour les notifications push riches.]({% image_buster /assets/img_archive/ios10_se_at.png %}){: width="1442" height="1030" style="max-width:90%"}

Vérifiez que l'option **Embed In Application** est configurée de manière à intégrer l'extension dans votre application.

### Étape 2 : Configurer l'extension de service de notification {#step-2-setting-up-the-notification-service-extension}

Une extension de service de notification est un binaire distinct qui est fourni avec votre application. Elle doit être configurée dans le [portail développeur Apple](https://developer.apple.com) avec son propre identifiant d'application et son propre profil de provisionnement.

L'identifiant de bundle de l'extension de service de notification doit être distinct de celui de la cible principale de votre application. Par exemple, si l'identifiant de bundle de votre application est `com.company.appname`, vous pouvez utiliser `com.company.appname.AppNameServiceExtension` pour votre extension de service.

### Étape 3 : Ajouter un groupe d'applications {#step-3-adding-an-app-group}

Dans Xcode, ajoutez la fonctionnalité App Groups depuis le panneau **Signing & Capabilities** à la fois à la cible principale de votre application et à celle de l'extension de service de notification. Cliquez ensuite sur le bouton **+**. Utilisez l'identifiant de bundle de votre application pour créer le groupe d'applications. Par exemple, si l'identifiant de bundle de votre application est `com.company.appname`, vous pouvez nommer votre groupe d'applications `group.com.company.appname.xyz`.

{% alert important %}
Dans ce contexte, les groupes d'applications font référence à l'[App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) d'Apple et non à l'identifiant de votre espace de travail Braze (anciennement groupe d'applications).
{% endalert %}

Un groupe d'applications partagé est nécessaire pour que votre application principale et l'extension de service de notification puissent accéder aux données partagées. Si vous n'ajoutez pas votre application à un groupe d'applications, votre application pourrait ne pas renseigner certains champs du payload de la notification push et ne fonctionnera pas entièrement comme prévu.

### Étape 4 : Intégrer les notifications push riches {#step-4-integrating-rich-push-notifications}

Pour un guide pas à pas sur l'intégration des notifications push riches avec `BrazeNotificationService`, consultez notre [tutoriel](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

Pour voir un exemple, consultez l'utilisation dans [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) de notre application d'exemples.

#### Ajouter le framework de notification push riche à votre application {#adding-the-rich-push-framework-to-your-app}

{% tabs local %}
{% tab Gestionnaire de paquets Swift %}

Après avoir suivi le [guide d'intégration du gestionnaire de paquets Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), ajoutez `BrazeNotificationService` à votre `Notification Service Extension` en procédant comme suit :

1. Dans Xcode, sous frameworks et bibliothèques, sélectionnez l'icône d'ajout <i class="fas fa-plus" aria-label="Ajouter un framework"></i> pour ajouter un framework. <br><br>![L'icône plus se trouve sous frameworks et bibliothèques dans Xcode.]({% image_buster /assets/img_archive/rich_notification.png %}){: width="1930" height="446"}<br><br>

2. Sélectionnez le framework « BrazeNotificationService ». <br><br>![Le framework « BrazeNotificationService » peut être sélectionné dans la fenêtre modale qui s'ouvre.]({% image_buster /assets/img_archive/rich_notification2.png %}){: width="2248" height="1102"}

{% endtab %}
{% tab CocoaPods %}

Ajoutez ce qui suit à votre Podfile :

```ruby
target 'YourAppTarget' do
  pod 'BrazeKit'
  pod 'BrazeUI'
  pod 'BrazeLocation'
end

target 'YourNotificationServiceExtensionTarget' do
  pod 'BrazeNotificationService'
end

# Only include the below if you want to also integrate Push Stories
target 'YourNotificationContentExtensionTarget' do
  pod 'BrazePushStory'
end
```

{% alert note %}
Pour obtenir les instructions relatives à l'implémentation de Push Stories, consultez la [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager).
{% endalert %}

Après avoir mis à jour le Podfile, accédez au répertoire de votre projet d'application Xcode dans votre terminal et exécutez `pod install`.

{% endtab %}

{% tab Manuel %}

Pour ajouter `BrazeNotificationService.xcframework` à votre `Notification Service Extension`, consultez la section [Intégration manuelle]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=manual/).

![Projet Xcode avec BrazeNotificationService.xcframework ajouté à l'extension de service de notification.]({% image_buster /assets/img/swift/rich_push/manual1.png %}){: width="1069" height="170"}

{% endtab %}
{% endtabs %}

#### Utiliser votre propre UNNotificationServiceExtension {#using-your-own-unnotificationserviceextension}

Si vous devez utiliser votre propre UNNotificationServiceExtension, vous pouvez appeler [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) dans votre méthode `didReceive`.

```swift
import BrazeNotificationService
import UserNotifications

class NotificationService: UNNotificationServiceExtension {

  override func didReceive(
    _ request: UNNotificationRequest,
    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
  ) {
    if brazeHandle(request: request, contentHandler: contentHandler) {
      return
    }

    // Custom handling here

    contentHandler(request.content)
  }
}
```

### Étape 5 : Configurer le groupe d'applications dans Braze {#step-5-configuring-the-app-group-in-braze}

Avant d'initialiser Braze, attribuez le nom de votre groupe d'applications à la propriété [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) de votre configuration Braze.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```

### Étape 6 : Créer une notification riche dans votre tableau de bord {#step-6-creating-a-rich-notification-in-your-dashboard}

Votre équipe marketing peut également créer des notifications riches depuis le tableau de bord. Créez une notification push via le compositeur de notifications push et joignez une image ou un GIF, ou fournissez une URL hébergeant une image, un GIF ou une vidéo. Notez que les ressources sont téléchargées à la réception des notifications push, vous devez donc anticiper des pics importants et synchrones de requêtes si vous hébergez votre contenu.