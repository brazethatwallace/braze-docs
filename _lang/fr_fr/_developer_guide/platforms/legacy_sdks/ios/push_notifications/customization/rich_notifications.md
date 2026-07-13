---
nav_title: Créer des notifications enrichies
article_title: Notifications push enrichies pour iOS
platform: iOS
page_order: 3
description: "Cet article de référence explique comment implémenter les notifications push enrichies dans votre application iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Notifications enrichies iOS 10 {#ios-10-rich-notifications}

iOS 10 offre la possibilité d'envoyer des notifications push avec des images, des GIF et des vidéos. Pour activer cette fonctionnalité, les clients doivent créer un `Service Extension`, un nouveau type d'extension qui permet la modification d'un payload de notification push avant qu'il ne soit affiché.

## Création d'une extension de service {#creating-a-service-extension}

Pour créer un [`Notification Service Extension`](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension), accédez à **File > New > Target** dans Xcode et sélectionnez **Notification Service Extension**.

![Sélecteur de cible Xcode créant une Notification Service Extension pour les notifications enrichies.]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

Assurez-vous que l'option **Embed In Application** est activée pour intégrer l'extension dans votre application.

## Configuration de l'extension de service {#setting-up-the-service-extension}

Un `Notification Service Extension` est son propre binaire fourni avec votre application. Il doit être configuré dans le [portail des développeurs Apple](https://developer.apple.com) avec son propre ID d'application et son propre profil de provisionnement.

L'ID de lot du `Notification Service Extension` doit être différent de l'ID de lot de la cible de votre application principale. Par exemple, si l'ID de lot de votre application est `com.company.appname`, vous pouvez utiliser `com.company.appname.AppNameServiceExtension` pour votre extension de service.

### Configuration de l'extension de service pour fonctionner avec Braze {#configuring-the-service-extension-to-work-with-braze}

Braze envoie un payload de pièce jointe dans le payload APNs sous la clé `ab` que nous utilisons pour configurer, télécharger et afficher du contenu enrichi. Par exemple :

```json
{
  "ab" :
    {
    ...

    "att" :
      {
       "url" : "http://mysite.com/myimage.jpg",
       "type" : "jpg"
       }
    },
  "aps" :
    {
    ...
    }
}
```

Les valeurs de payload pertinentes sont les suivantes :

```objc
// The Braze dictionary key
static NSString *const AppboyAPNSDictionaryKey = @"ab";

// The attachment dictionary
static NSString *const AppboyAPNSDictionaryAttachmentKey = @"att";

// The attachment URL
static NSString *const AppboyAPNSDictionaryAttachmentURLKey = @"url";

// The type of the attachment - a suffix for the file you save
static NSString *const AppboyAPNSDictionaryAttachmentTypeKey = @"type";
```

Pour afficher manuellement la notification push avec un payload Braze, téléchargez le contenu de la valeur `AppboyAPNSDictionaryAttachmentURLKey`, enregistrez-le comme fichier avec le type de fichier stocké sous la clé `AppboyAPNSDictionaryAttachmentTypeKey` et ajoutez-le aux pièces jointes de la notification.

### Exemple de code {#example-code}

Vous pouvez écrire l'extension de service en Objective-C ou en Swift.

Pour utiliser notre exemple de code Objective-C, remplacez le contenu du fichier `NotificationService.m` généré automatiquement dans la cible de votre `Notification Service Extension` par le contenu du fichier Appboy [`NotificationService.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/StopwatchNotificationService/NotificationService.m).

Pour utiliser notre exemple de code Swift, remplacez le contenu du fichier `NotificationService.swift` généré automatiquement dans la cible de votre `Notification Service Extension` par le contenu du fichier Appboy [`NotificationService.swift`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftNotificationExtension/NotificationService.swift).

## Créer une notification enrichie dans votre tableau de bord {#creating-a-rich-notification-in-your-dashboard}

Pour créer une notification enrichie dans votre tableau de bord de Braze, créez une notification push iOS, joignez une image ou un GIF, ou fournissez une URL hébergeant une image, un GIF ou une vidéo. Notez que les ressources sont téléchargées à la réception des notifications push, vous devez donc prévoir des pics importants et synchrones de requêtes si vous hébergez votre contenu.

Consultez [`unnotificationattachment`](https://developer.apple.com/reference/usernotifications/unnotificationattachment) pour obtenir la liste des types et tailles de fichiers pris en charge.