---
nav_title: Réception/distribution de messages in-app
article_title: Réception/distribution de messages in-app pour iOS
platform: iOS
page_order: 3
description: "Cet article de référence couvre la réception/distribution de messages in-app sur iOS, en répertoriant les différents types de déclencheurs, les sémantiques de réception/distribution et les étapes de déclenchement d'événements."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Réception/distribution de messages in-app {#in-app-message-delivery}

## Types de déclencheurs {#trigger-types}

Notre produit de messages in-app vous permet de déclencher l'affichage d'un message in-app à la suite de plusieurs types d'événements différents : `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` et `Push Click`. De plus, les déclencheurs `Specific Purchase` et `Custom Event` contiennent des filtres de propriétés robustes.

{% alert note %}
Les messages in-app déclenchés ne fonctionnent qu'avec des événements personnalisés enregistrés via le SDK de Braze. Les messages in-app ne peuvent pas être déclenchés via l'API ou par des événements API (tels que les événements d'achat). Si vous travaillez avec iOS, consultez notre article sur le [suivi des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift) pour en savoir plus.
{% endalert %}

## Sémantiques de réception/distribution {#delivery-semantics}

Tous les messages in-app auxquels un utilisateur est éligible sont envoyés sur l'appareil de l'utilisateur au démarrage de la session. Si deux messages in-app sont déclenchés par un même événement, le message in-app doté de la priorité la plus élevée sera affiché. Pour plus d'informations sur la sémantique de démarrage de session du SDK, consultez notre documentation sur le [cycle de vie des sessions]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions#session-lifecycle). Dès la réception, le SDK précharge les ressources pour qu'elles soient immédiatement disponibles au moment du déclenchement, réduisant ainsi la latence d'affichage.

Lorsqu'un événement déclencheur comporte plus d'un message in-app éligible associé, seul le message in-app avec la priorité la plus élevée sera distribué.

Il peut y avoir une certaine latence pour les messages in-app qui s'affichent immédiatement à la réception (démarrage de session, clic sur une notification push) en raison de ressources n'ayant pas été préchargées.

## Intervalle de temps minimum entre les déclencheurs {#minimum-time-interval-between-triggers}

Par défaut, nous limitons le débit des messages in-app à une fois toutes les 30 secondes afin de favoriser une expérience utilisateur de qualité.

Vous pouvez remplacer cette valeur via la clé `ABKMinimumTriggerTimeIntervalKey` dans le paramètre `appboyOptions` transmis à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définissez `ABKMinimumTriggerTimeIntervalKey` sur la valeur entière souhaitée comme durée minimale en secondes entre les messages in-app :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

## Absence de déclencheur correspondant {#failing-to-find-a-matching-trigger}

Lorsque Braze ne trouve pas de déclencheur correspondant à un événement particulier, il appelle la méthode [noMatchingTriggerForEvent:name:](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html#ab4d57b13c51545d487227945a37d4ab8) du [`ABKInAppMessageControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html). Implémentez cette méthode dans votre classe en adoptant le protocole de délégation pour gérer ce scénario.

## Réception/distribution locale de messages in-app {#local-in-app-message-delivery}

### La pile de messages in-app {#the-in-app-message-stack}

#### Affichage des messages in-app {#showing-in-app-messages}

Lorsqu'un utilisateur est éligible à la réception d'un message in-app, le `ABKInAppMessageController` recevra le dernier message in-app de la pile de messages in-app. La pile ne conserve que les messages in-app stockés en mémoire et est effacée entre les lancements de l'application depuis le mode suspendu.

{% alert important %}
N'affichez pas les messages in-app lorsque le clavier est affiché à l'écran, car le rendu n'est pas défini dans ce cas.
{% endalert %}

#### Ajout de messages in-app à la pile {#adding-in-app-messages-to-the-stack}

Les utilisateurs peuvent recevoir un message in-app dans les situations suivantes :

- Un événement déclencheur de message in-app est déclenché
- Événement de démarrage de session
- L'application est ouverte à partir d'une notification push

Les messages in-app déclenchés sont placés sur la pile lorsque leur événement déclencheur est déclenché. Si plusieurs messages in-app sont dans la pile et en attente d'être affichés, Braze affichera le message in-app le plus récemment reçu (dernier entré, premier sorti).

#### Retour des messages in-app à la pile {#returning-in-app-messages-to-the-stack}

Un message in-app déclenché peut être renvoyé à la pile dans les situations suivantes :

- Le message in-app est déclenché lorsque l'application est en arrière-plan.
- Un autre message in-app est actuellement visible.
- La [méthode de délégation de l'IU]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) obsolète `beforeInAppMessageDisplayed:withKeyboardIsUp:` n'a pas été implémentée et le clavier est actuellement affiché.
- La [méthode de délégation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` ou la [méthode de délégation de l'IU]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) obsolète `beforeInAppMessageDisplayed:withKeyboardIsUp:` a renvoyé `ABKDisplayInAppMessageLater`.

#### Écarter les messages in-app {#discarding-in-app-messages}

Un message in-app déclenché sera écarté dans les situations suivantes :

- La [méthode de délégation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` ou la [méthode de délégation de l'IU]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) obsolète `beforeInAppMessageDisplayed:withKeyboardIsUp:` a renvoyé `ABKDiscardInAppMessage`.
- La ressource (fichier image ou ZIP) du message in-app n'a pas pu être téléchargée.
- Le message in-app est prêt à être affiché, mais a dépassé le délai d'expiration.
- L'orientation de l'appareil ne correspond pas à l'orientation du message in-app déclenché.
- Le message in-app est un message in-app plein écran, mais n'a pas d'image.
- Le message in-app est un message in-app modal composé uniquement d'une image, mais n'a pas d'image.

#### Mettre manuellement en file d'attente l'affichage des messages in-app {#manually-queue-in-app-message-display}

Si vous souhaitez afficher un message in-app à d'autres moments dans votre application, vous pouvez afficher manuellement le message in-app le plus haut sur la pile en appelant la méthode suivante :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage()
```

{% endtab %}
{% endtabs %}

### Création et affichage de messages in-app en temps réel {#real-time-in-app-message-creation-and-display}

Les messages in-app peuvent également être créés localement dans l'application et affichés via Braze. Ceci est particulièrement utile pour afficher les messages que vous souhaitez déclencher dans l'application en temps réel. Braze ne prend pas en charge l'analyse des messages in-app créés localement.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
  ABKInAppMessageSlideup *customInAppMessage = [[ABKInAppMessageSlideup alloc] init];
  customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
  customInAppMessage.duration = 2.5;
  customInAppMessage.extras = @{@"key" : @"value"};
  [[Appboy sharedInstance].inAppMessageController addInAppMessage:customInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
  let customInAppMessage = ABKInAppMessageSlideup.init()
  customInAppMessage.message = "YOUR_CUSTOM_SLIDEUP_MESSAGE"
  customInAppMessage.duration = 2.5
  customInAppMessage.extras = ["key": "value"]
  Appboy.sharedInstance()!.inAppMessageController.add(customInAppMessage)
```

{% endtab %}
{% endtabs %}