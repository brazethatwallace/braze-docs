{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Déclencheurs de messages {#message-triggers}

### Types de déclencheurs {#trigger-types}

Les messages in-app sont automatiquement déclenchés lorsque le SDK enregistre l'un des types d'événements personnalisés suivants : `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` et `Push Click`. Notez que les déclencheurs `Specific Purchase` et `Custom Event` contiennent également des filtres de propriétés robustes.

{% alert note %}
Les messages in-app ne peuvent pas être déclenchés par l'API ou par des événements de l'API — uniquement par des événements personnalisés enregistrés par le SDK. Pour en savoir plus sur la journalisation, consultez la section [Journalisation des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift).
{% endalert %}

### Sémantique de distribution {#delivery-semantics}

Tous les messages in-app éligibles sont envoyés sur l'appareil de l'utilisateur au début de sa session. À la réception, le SDK précharge les ressources afin qu'elles soient disponibles au moment du déclenchement, ce qui minimise la latence d'affichage. Si l'événement déclencheur comporte plusieurs messages in-app éligibles, seul le message ayant la priorité la plus élevée sera distribué.

Pour plus d'informations sur la sémantique de démarrage de session du SDK, consultez la section [Cycle de vie de la session]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift).

### Limite de débit par défaut {#default-rate-limit}

Par défaut, le SDK limite le déclenchement des messages in-app à une fois toutes les 30 secondes.

Pour les applications en production, ne définissez pas cette valeur en dessous de 10 secondes, afin d'éviter que les utilisateurs ne soient submergés par des messages in-app successifs. Pour les tests et les flux d'applications de démonstration, 5 secondes est un réglage courant.

Vous pouvez définir cet intervalle à `0` pour les tests. Cependant, un intervalle de `0` seconde ne force pas l'affichage simultané de plusieurs messages in-app. Si un message est visible, un autre message déclenché attend dans la pile de messages in-app jusqu'à ce qu'un message puisse être affiché.

Pour modifier ce comportement, mettez à jour la propriété `triggerMinimumTimeInterval` dans votre configuration Braze avant l'initialisation de l'instance Braze. Elle peut être définie sur n'importe quel entier non négatif et représente l'intervalle de temps minimum en secondes. Par exemple :

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% endtabs %}

## Paires clé-valeur {#key-value-pairs}

Lorsque vous créez une campagne dans Braze, vous pouvez définir des paires clé-valeur en tant qu'`extras`, que l'objet de message in-app peut utiliser pour envoyer des données à votre application. Par exemple :

{% tabs %}
{% tab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```

{% endtab %}
{% endtabs %}

Pour une implémentation complète, vous pouvez consulter les exemples de personnalisation des messages in-app dans notre [application d'exemple](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

## Désactivation des déclencheurs automatiques {#disabling-automatic-triggers}

Pour empêcher les messages in-app de se déclencher automatiquement :

1. Implémentez le délégué `BrazeInAppMessageUIDelegate` comme décrit dans notre [article iOS ici](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Mettez à jour votre méthode de délégué `inAppMessage(_:displayChoiceForMessage:)` pour qu'elle retourne `.discard`.

## Déclenchement manuel des messages {#manually-triggering-messages}

### Utilisation d'un événement côté serveur {#using-a-server-side-event}

Pour déclencher des messages in-app à l'aide d'événements côté serveur, envoyez une notification push silencieuse à l'appareil pour lui permettre d'enregistrer un événement basé sur le SDK. Cet événement SDK peut ensuite déclencher le message in-app destiné à l'utilisateur.

#### Étape 1 : Gérer les notifications push silencieuses et les paires clé-valeur {#step-1-handle-silent-push-and-key-value-pairs}

Implémentez la fonction suivante et appelez-la dans la méthode [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/) :

{% tabs %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

Lorsque la notification push silencieuse est reçue, un événement enregistré par le SDK « in-app message trigger » sera consigné dans le profil utilisateur.

{% alert important %}
Étant donné qu'un message push est utilisé pour enregistrer un événement personnalisé via le SDK, Braze devra stocker un jeton de notification push pour chaque utilisateur afin de permettre cette solution. Pour les utilisateurs iOS, Braze ne stocke un jeton qu'à partir du moment où l'utilisateur a reçu l'invite de notification push du système. Avant cela, l'utilisateur ne sera pas joignable par notification push, et la solution décrite ci-dessus ne sera pas possible.
{% endalert %}

#### Étape 2 : Créer une campagne de notification push silencieuse {#step-2-create-a-silent-push-campaign}

Créez une [campagne de notification push silencieuse]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) déclenchée par l'événement envoyé par le serveur.

![Une campagne de messages in-app avec livraison par événement qui sera envoyée aux utilisateurs dont le profil utilisateur comporte l'événement personnalisé « server_event ».]({% image_buster /assets/img_archive/iosServerSentPush.png %})

La campagne de notification push doit inclure des extras de paires clé-valeur indiquant que cette campagne est envoyée pour enregistrer un événement personnalisé SDK. Cet événement sera utilisé pour déclencher le message in-app.

![Une campagne de messages in-app avec livraison par événement comportant deux paires clé-valeur. « CAMPAIGN_NAME » défini sur « Exemple de nom de message in-app » et « IS_SERVER_EVENT » défini sur « true ».]({% image_buster /assets/img_archive/iOSServerPush.png %})

Le code de la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` vérifie la clé `IS_SERVER_EVENT` et enregistre un événement personnalisé SDK si celle-ci est présente.

Vous pouvez modifier le nom de l'événement ou les propriétés d'événement en envoyant la valeur souhaitée dans les extras de paires clé-valeur du payload de la notification push. Lors de la journalisation de l'événement personnalisé, ces extras peuvent être utilisés comme paramètre du nom de l'événement ou comme propriété d'événement.

#### Étape 3 : Créer une campagne de messages in-app {#step-3-create-an-in-app-message-campaign}

Créez votre campagne de messages in-app visible par l'utilisateur dans le tableau de bord de Braze. Cette campagne doit avoir une livraison par événement et être déclenchée par l'événement personnalisé enregistré depuis la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

Dans l'exemple suivant, le message in-app spécifique à déclencher a été configuré en envoyant la propriété d'événement dans le cadre de la notification push silencieuse initiale.

![Une campagne de messages in-app avec livraison par événement qui sera envoyée aux utilisateurs effectuant l'événement personnalisé « In-app message trigger » où « campaign_name » est égal à « IAM Campaign Name Example ».]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Notez que ces messages in-app ne se déclencheront que si la notification push silencieuse est reçue pendant que l'application est au premier plan.
{% endalert %}

### Affichage d'un message prédéfini {#displaying-a-pre-defined}

Pour afficher manuellement un message in-app prédéfini, utilisez la méthode suivante :

```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```

### Affichage d'un message en temps réel {#displaying-a-message-in-real-time}

Vous pouvez également afficher des messages in-app locaux en temps réel en appelant manuellement la méthode [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) sur votre `inAppMessagePresenter`. Par exemple :

{% tabs %}
{% tab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endtab %}
{% endtabs %}

{% alert note %}
En créant votre propre message in-app, vous renoncez à tout suivi analytique et devrez gérer manuellement l'enregistrement des clics et des impressions à l'aide de votre `message.context`.
{% endalert %}

## La pile de messages in-app {#the-in-app-message-stack}

### Ajout de messages in-app à la pile {#adding-in-app-messages-to-the-stack}

Les utilisateurs peuvent recevoir un message in-app dans les situations suivantes :

- Un événement déclencheur de message in-app est déclenché
- Une session est démarrée
- L'application est ouverte à partir d'une notification push

Lorsque l'événement déclencheur d'un message in-app est déclenché, celui-ci est placé sur une « pile ». Si plusieurs messages in-app sont dans la pile et en attente d'affichage, Braze affichera le message in-app le plus récemment reçu en premier (dernier entré, premier sorti).

Lorsqu'un utilisateur est éligible pour recevoir un message in-app, le `BrazeInAppMessagePresenter` demande le dernier message in-app de la pile. La pile ne conserve les messages in-app stockés qu'en mémoire et est vidée entre les lancements de l'application depuis le mode suspendu.

### Renvoi des messages in-app à la pile {#returning-in-app-messages-to-the-stack}

Un message in-app déclenché peut être renvoyé à la pile dans les situations suivantes :

- Le message in-app est déclenché lorsque l'application est en arrière-plan.
- Un autre message in-app est actuellement visible.
- La [méthode de délégation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` a renvoyé `.reenqueue`.

Le message in-app déclenché sera placé en haut de la pile pour un affichage ultérieur lorsqu'un utilisateur sera éligible pour recevoir un message in-app.

### Rejet des messages in-app {#discarding-in-app-messages}

Un message in-app déclenché sera rejeté dans les situations suivantes :

- La [méthode de délégation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` a renvoyé `.discard`.
- La ressource (fichier image ou ZIP) du message in-app n'a pas pu être téléchargée.
- Le message in-app est prêt à être affiché mais a dépassé le délai d'expiration.
- L'orientation de l'appareil ne correspond pas à l'orientation du message in-app déclenché.

Le message in-app sera retiré de la pile. Après avoir été rejeté, le message in-app peut être déclenché ultérieurement par une autre instance de l'événement déclencheur.