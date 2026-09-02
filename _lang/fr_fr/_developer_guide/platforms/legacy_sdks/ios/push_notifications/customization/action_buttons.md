---
nav_title: Boutons d'action
article_title: Boutons d'action push pour iOS
platform: iOS
page_order: 1
description: "Cet article de référence traite de la manière d'implémenter les boutons d'action dans vos notifications push iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Boutons d'action {#push-action-buttons-integration}

Le SDK Braze pour iOS prend en charge les catégories de notifications push par défaut, y compris la prise en charge de la gestion d'URL pour chaque bouton d'action push. Actuellement, les catégories par défaut proposent quatre ensembles de boutons d'action push : `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel` et `More`.

![Un GIF d'une notification push développée pour afficher deux boutons d'action personnalisables.]({% image_buster /assets/img_archive/iOS8Action.gif %})

Pour enregistrer nos catégories push par défaut, suivez les instructions d'intégration :

## Étape 1 : Ajout des catégories push par défaut de Braze {#step-1-adding-braze-default-push-categories}

Utilisez le code suivant pour enregistrer nos catégories push par défaut lorsque vous [vous inscrivez aux notifications push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-4-register-push-tokens-with-braze) :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// For UserNotification.framework (iOS 10+ only)
NSSet *appboyCategories = [ABKPushUtils getAppboyUNNotificationCategorySet];
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:appboyCategories];

// For UIUserNotificationSettings (before iOS 10)
NSSet *appboyCategories = [ABKPushUtils getAppboyUIUserNotificationCategorySet];
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeBadge
                                                                         categories:appboyCategories];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
// For UserNotification.framework (iOS 10+ only)
let appboyCategories = ABKPushUtils.getAppboyUNNotificationCategorySet()
UNUserNotificationCenter.current().setNotificationCategories(appboyCategories)

// For UIUserNotificationSettings (before iOS 10)
let appboyCategories = ABKPushUtils.getAppboyUIUserNotificationCategorySet()
let settings = UIUserNotificationSettings.init(types: .badge, categories: appboyCategories)
UIApplication.shared.registerUserNotificationSettings(settings)
```

{% endtab %}
{% endtabs %}

Appuyer sur les boutons d'action push avec le mode d'activation en arrière-plan ne fait que fermer la notification sans ouvrir l'application. La prochaine fois que l'utilisateur ouvre l'application, les données analytiques de clic sur le bouton pour ces actions seront envoyées au serveur.

Si vous souhaitez créer vos propres catégories de notification personnalisées, consultez la section [personnalisation des boutons d'action]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons#push-category-customization).

## Étape 2 : Activer la gestion interactive des notifications push {#step-2-enable-interactive-push-handling}

Si vous utilisez le framework `UNNotification` et que vous avez implémenté les [délégués]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling) Braze, cette méthode devrait déjà être intégrée.

Pour activer la gestion des boutons d'action push, y compris l'analyse des clics et le routage des URL, ajoutez le code suivant à la méthode déléguée `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` de votre application :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                           didReceiveNotificationResponse:response
                               withCompletionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                                didReceive: response,
                                                withCompletionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

Si vous n'utilisez pas le framework UNNotification, vous devrez ajouter le code suivant à la méthode `application:handleActionWithIdentifier:forRemoteNotification:completionHandler:` de votre application pour activer la gestion des boutons d'action push :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] getActionWithIdentifier:identifier
                           forRemoteNotification:userInfo
                               completionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.getActionWithIdentifier(identifier,
                                                 forRemoteNotification: userInfo,,
                                                 completionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Nous recommandons fortement aux utilisateurs de `handleActionWithIdentifier` de commencer à utiliser le framework `UNNotification`. Cette recommandation est liée à la dépréciation de [`handleActionWithIdentifier`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc).
{% endalert %}

## Personnalisation des catégories de notifications push {#push-category-customization}

En plus de fournir un ensemble de [catégories de notifications push par défaut]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons), Braze prend en charge les catégories et actions de notification personnalisées. Après avoir enregistré des catégories dans votre application, vous pouvez utiliser le tableau de bord de Braze pour envoyer des catégories de notification à vos utilisateurs.

Si vous n'utilisez pas le framework `UserNotifications`, consultez la documentation sur les [catégories alternatives](https://developer.apple.com/documentation/usernotifications/unnotificationcategory).

Ces catégories peuvent ensuite être attribuées aux notifications push via notre tableau de bord pour déclencher les configurations de boutons d'action de votre conception. Voici un exemple qui tire parti de la catégorie `LIKE_CATEGORY` affichée sur l'appareil :

![Un message de notification push affichant deux boutons d'action push « unlike » et « like ».]({% image_buster /assets/img_archive/push_example_category.png %})