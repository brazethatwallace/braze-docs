---
nav_title: Déclencher des messages
article_title: Déclencher des messages in-app via le SDK Braze
page_order: 0.2
description: "Découvrez comment déclencher des messages in-app grâce au SDK de Braze, y compris l'enchaînement de messages au cours d'une même session et le remplacement de la limite de débit par défaut."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Déclencher des messages in-app {#trigger-in-app-messages}

> Découvrez comment déclencher des messages in-app grâce au SDK de Braze.

## Déclencheurs et réception des messages {#message-triggers-and-delivery}

Les messages in-app sont déclenchés lorsque le SDK enregistre l'un des types d'événements personnalisés suivants : `Session Start`, `Push Click`, `Any Purchase`, `Specific Purchase` et `Custom Event` (les deux derniers contenant des filtres de propriétés robustes).

Au début de la session d'un utilisateur, Braze envoie tous les messages in-app éligibles à son appareil, tout en préchargeant simultanément les ressources pour minimiser la latence d'affichage. Si l'événement déclencheur comporte plusieurs messages in-app éligibles, seul le message ayant la priorité la plus élevée sera délivré. Pour plus d'informations, voir [Cycle de vie des sessions]({{site.baseurl}}/developer_guide/analytics/tracking_sessions).

{% alert note %}
Les messages in-app ne peuvent pas être déclenchés par l'API ou par des événements de l'API&#8212;uniquement par des événements personnalisés enregistrés par le SDK. Pour en savoir plus sur la journalisation, reportez-vous à la section [Journalisation des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events).
{% endalert %}

## Types de messages in-app {#types-of-in-app-messages}

Braze envoie les types de messages in-app suivants aux appareils des utilisateurs au début de la session : `inapp` et `templated_iam`. En tant qu'utilisateur du tableau de bord, vous ne voyez pas les différents types, mais Braze les traite différemment en fonction de la configuration et du contenu.

### `inapp` (standard) {#inapp-standard}

Un message in-app `inapp` (ou « [standard]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages#standard-message-types) ») est déjà modélisé avec les informations nécessaires, telles que les attributs personnalisés que Braze connaît déjà. En général, lorsque le message in-app est téléchargé sur l'appareil, l'événement déclencheur amène le SDK à afficher le message in-app `inapp` même lorsque l'appareil est hors ligne ou en mode avion.

### `templated_iam` (modélisé) {#templated_iam-templated}

Un message in-app `templated_iam` (ou « modélisé ») n'est pas encore modélisé avec les informations nécessaires. Braze doit effectuer une autre requête pour récupérer les informations avant que le message puisse apparaître.

{% multi_lang_include in-app_messages/templated_iams.md %}

## Paires clé-valeur {#key-value-pairs}

Lorsque vous créez une campagne dans Braze, vous pouvez définir des paires clé-valeur en tant qu'`extras`, que l'objet de message in-app peut utiliser pour envoyer des données à votre application.

{% tabs %}
{% tab web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}
```java
Map<String, String> getExtras()
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Pour plus d'informations, consultez le [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}
{% endtab %}

{% tab swift %}
L'exemple suivant utilise une logique personnalisée pour définir la présentation d'un message in-app en fonction de ses paires clé-valeur dans `extras`. Pour un exemple de personnalisation complète, consultez [notre exemple d'application](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

{% subtabs %}
{% subtab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Désactivation des déclencheurs automatiques {#disabling-automatic-triggers}

Par défaut, les messages in-app se déclenchent automatiquement. Pour désactiver cette fonction :

{% tabs %}

{% tab web %}
Supprimez l'appel à `braze.automaticallyShowInAppMessages()` dans votre extrait de code de chargement, puis créez une logique personnalisée pour gérer l'affichage ou non d'un message in-app.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message

  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }

  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the display capabilities in Braze, you could alternatively pass the in-app message to your own display code here.

  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Si vous appelez `braze.showInAppMessage` sans retirer `braze.automaticallyShowInAppMessages()`, les messages peuvent s'afficher deux fois.
{% endalert %}

Pour un contrôle plus avancé du timing des messages, y compris le report et la restauration des messages déclenchés, veuillez vous référer à notre [tutoriel : Report et restauration des messages déclenchés]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
{% endtab %}

{% tab android %}
1. Implémentez [`IInAppMessageManagerListener`]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android&tab=global%20listener#android_step-1-implement-the-custom-manager-listener) pour définir un écouteur personnalisé.
2. Mettez à jour votre méthode [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html) afin qu'elle renvoie [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html).

Pour un contrôle plus avancé du timing des messages, y compris l'affichage différé et la remise en file d'attente, veuillez consulter notre page [Personnalisation des messages]({{site.baseurl}}/developer_guide/in_app_messages/customization?tab=global%20listener&subtab=kotlin#android_step-2-instruct-braze-to-use-the-custom-manager-listener).
{% endtab %}

{% tab swift %}
1. Implémentez le délégué `BrazeInAppMessageUIDelegate` dans votre application. Pour un guide complet, veuillez vous référer au [tutoriel : Interface utilisateur des messages in-app](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Mettez à jour votre méthode de délégué `inAppMessage(_:displayChoiceForMessage:)` pour qu'elle retourne `.discard`.

Pour un contrôle plus avancé du timing des messages, y compris le report et la restauration des messages déclenchés, veuillez vous référer à notre [tutoriel : Report et restauration des messages déclenchés]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
{% endtab %}

{% tab flutter %}
1. Vérifiez que vous utilisez l'initialisateur d'intégration automatique, qui est activé par défaut dans les versions `2.2.0` et ultérieures.
2. Définissez l'opération par défaut de message in-app sur `DISCARD` en ajoutant la ligne suivante à votre fichier `braze.xml`.
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```
{% endtab %}

{% tab unity %}
{% subtabs %}
{% subtab Android %}
Pour Android, désélectionnez **Automatically Display In-App Messages** dans l'éditeur de configuration de Braze. Vous pouvez également définir `com_braze_inapp_show_inapp_messages_automatically` sur `false` dans le fichier `braze.xml` de votre projet Unity.

L'opération initiale d'affichage des messages in-app peut être définie dans la configuration de Braze à l'aide de « In App Message Manager Initial Display Operation ».
{% endsubtab %}

{% subtab iOS %}
Pour iOS, définissez les écouteurs d'objets de jeu dans l'éditeur de configuration de Braze et assurez-vous que **Braze Displays In-App Messages** n'est pas sélectionné.

L'opération initiale d'affichage des messages in-app peut être définie dans la configuration de Braze à l'aide de « In App Message Manager Initial Display Operation ».
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Enchaîner deux messages in-app au cours d'une même session {#chaining-two-in-app-messages-in-one-session}

Vous pouvez déclencher un message in-app au démarrage de la session, puis déclencher un second message in-app après l'appui sur un bouton du premier. Pour ce faire, enregistrez un événement personnalisé pour le clic sur le bouton qui déclenchera le second message. Le déclencheur du second message doit déjà être présent sur l'appareil (l'utilisateur doit déjà être éligible au second message) et se produire côté appareil (le SDK Braze ne prendra pas en compte les modifications d'attributs personnalisés effectuées sur les serveurs de Braze). Le délai de refroidissement par défaut de 30 secondes entre les déclenchements de messages in-app doit être modifié pour afficher plusieurs messages in-app en succession rapide. Pour la configuration spécifique à chaque plateforme, voir [Remplacement de la limite de débit par défaut](#overriding-the-default-rate-limit).

## Remplacement de la limite de débit par défaut {#overriding-the-default-rate-limit}

Par défaut, le SDK limite le débit des messages in-app déclenchés à une fois toutes les 30 secondes. Pour remplacer ce comportement, ajoutez la propriété suivante à votre fichier de configuration avant l'initialisation de l'instance de Braze. Cette valeur sera utilisée comme nouvelle limite de débit en secondes.

Pour les applications en production, ne définissez pas cette valeur en dessous de 10 secondes, afin que les utilisateurs ne soient pas submergés par des messages in-app successifs. Pour les tests et les flux d'applications de démonstration, 5 secondes est un réglage courant.

Vous pouvez définir cet intervalle sur `0` pour les tests. Cependant, un intervalle de `0` seconde ne force pas l'affichage simultané de plusieurs messages in-app. Si un message in-app est déjà visible, un autre message déclenché ne s'affichera pas tant que le message actuel n'aura pas été fermé.

{% tabs %}
{% tab web %}
```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}

{% tab android %}
```xml
<integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
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
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Déclenchement manuel des messages {#manually-triggering-messages}

Par défaut, les messages in-app sont automatiquement déclenchés lorsque le SDK enregistre un événement personnalisé. Toutefois, vous pouvez également déclencher manuellement des messages à l'aide des méthodes suivantes.

### Utilisation d'un événement côté serveur {#using-a-server-side-event}

{% tabs %}
{% tab web %}
À l'heure actuelle, le SDK Web de Braze ne prend pas en charge le déclenchement manuel de messages à l'aide d'événements côté serveur.
{% endtab %}

{% tab android %}
Pour déclencher un message in-app à l'aide d'un événement envoyé par le serveur, envoyez une notification push silencieuse à l'appareil, ce qui permet à un rappel push personnalisé d'enregistrer un événement basé sur le SDK. Cet événement déclenchera alors le message in-app destiné à l'utilisateur.

#### Étape 1 : Créer un rappel push pour recevoir la notification push silencieuse {#step-1-create-a-push-callback-to-receive-the-silent-push}

Enregistrez votre rappel push personnalisé pour écouter une notification push silencieuse spécifique. Pour plus d'informations, veuillez vous référer à la section [Configuration des notifications push]({{site.baseurl}}/developer_guide/push_notifications#android_setting-up-push-notifications).

Deux événements seront enregistrés pour que le message in-app soit livré, un par le serveur et l'autre à partir de votre rappel push personnalisé. Pour vous assurer que le même événement n'est pas dupliqué, l'événement enregistré dans votre rappel push doit suivre une convention de dénomination générique, par exemple « événement déclencheur de message in-app », et ne pas porter le même nom que l'événement envoyé par le serveur. Si cela n'est pas fait, la segmentation et les données utilisateur peuvent être affectées par des événements enregistrés en double pour une seule action utilisateur.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endsubtab %}
{% endsubtabs %}

#### Étape 2 : Créer une campagne de notification push {#step-2-create-a-push-campaign}

Créez une [campagne de push silencieuse]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android) déclenchée par l'événement envoyé par le serveur.

![Étape de livraison d'une campagne de push silencieuse configurée pour une livraison par événement avec un déclencheur d'événement personnalisé server_event.]({% image_buster /assets/img_archive/serverSentPush.png %})

La campagne de notification push doit inclure des extras de paires clé-valeur qui indiquent que cette campagne est envoyée pour enregistrer un événement personnalisé SDK. Cet événement sera utilisé pour déclencher le message in-app.

![Deux ensembles de paires clé-valeur : IS_SERVER_EVENT défini sur « true » et CAMPAIGN_NAME défini sur « nom de campagne à titre d'exemple ».]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

Le code exemple de rappel push présenté précédemment reconnaît les paires clé-valeur et enregistre l'événement personnalisé SDK approprié.

Si vous souhaitez inclure des propriétés d'événement à joindre à votre événement « déclencheur de message in-app », vous pouvez y parvenir en les transmettant dans les paires clé-valeur du payload de la notification push. Dans cet exemple, le nom de campagne du message in-app suivant a été inclus. Votre rappel push personnalisé peut ensuite transmettre la valeur comme paramètre de la propriété de l'événement lors de l'enregistrement de l'événement personnalisé.

#### Étape 3 : Créer une campagne de message in-app {#step-3-create-an-in-app-message-campaign}

Créez votre campagne de messages in-app visible par l'utilisateur dans le tableau de bord de Braze. Cette campagne doit avoir une livraison par événement et être déclenchée par l'événement personnalisé enregistré à partir de votre rappel push personnalisé.

Dans l'exemple suivant, le message in-app spécifique à déclencher a été configuré en envoyant la propriété de l'événement dans le cadre de la première notification push silencieuse.

![Une campagne de livraison par événement où un message in-app se déclenchera lorsque « campaign_name » est égal à « exemple de nom de campagne IAM ».]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Si un événement envoyé par le serveur est enregistré alors que l'application n'est pas au premier plan, l'événement sera enregistré, mais le message in-app ne s'affichera pas. Si vous souhaitez que l'événement soit retardé jusqu'à ce que l'application soit au premier plan, une vérification doit être incluse dans votre récepteur push personnalisé pour rejeter ou retarder l'événement jusqu'à ce que l'application passe au premier plan.
{% endtab %}

{% tab swift %}
#### Étape 1 : Gérer les notifications push silencieuses et les paires clé-valeur {#step-1-handle-silent-push-and-key-value-pairs}

Implémentez la fonction suivante et appelez-la dans la méthode [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/) :

{% subtabs %}
{% subtab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endsubtab %}
{% endsubtabs %}

Lorsque la notification push silencieuse est reçue, un événement enregistré par le SDK « in-app message trigger » sera consigné dans le profil utilisateur.

{% alert important %}
En raison de l'utilisation d'un message push pour enregistrer un événement personnalisé du SDK, Braze devra stocker un jeton de notification push pour chaque utilisateur afin de permettre cette solution. Pour les utilisateurs iOS, Braze ne stocke un jeton qu'à partir du moment où un utilisateur a reçu l'invite de notification push du système d'exploitation. Avant cela, l'utilisateur ne sera pas joignable par notification push, et la solution précédente ne sera pas possible.
{% endalert %}

#### Étape 2 : Créer une campagne de push silencieuse {#step-2-create-a-silent-push-campaign}

Créez une [campagne de push silencieuse]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift) déclenchée par l'événement envoyé par le serveur.

![Une campagne de messages in-app basée sur l'événement qui sera envoyée aux utilisateurs dont le profil utilisateur comporte l'événement personnalisé « server_event ».]({% image_buster /assets/img_archive/iosServerSentPush.png %})

La campagne de notification push doit inclure des extras de paires clé-valeur qui indiquent que cette campagne est envoyée pour enregistrer un événement personnalisé SDK. Cet événement sera utilisé pour déclencher le message in-app.

![Une campagne de messages in-app basée sur l'événement qui comporte deux paires clé-valeur. « CAMPAIGN_NAME » est défini sur « Exemple de nom de message in-app » et « IS_SERVER_EVENT » est défini sur « true ».]({% image_buster /assets/img_archive/iOSServerPush.png %})

Le code de la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` vérifie la clé `IS_SERVER_EVENT` et enregistrera un événement personnalisé SDK si celle-ci est présente.

Vous pouvez modifier le nom de l'événement ou les propriétés d'événement en envoyant la valeur souhaitée dans les extras de paires clé-valeur du payload de la notification push. Lors de la journalisation de l'événement personnalisé, ces extras peuvent être utilisés comme paramètre du nom de l'événement ou comme propriété de l'événement.

#### Étape 3 : Créer une campagne de message in-app

Créez votre campagne de messages in-app visible par l'utilisateur dans le tableau de bord de Braze. Cette campagne doit avoir une livraison par événement et être déclenchée par l'événement personnalisé enregistré à partir de la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

Dans l'exemple suivant, le message in-app spécifique à déclencher a été configuré en envoyant la propriété de l'événement dans le cadre de la première notification push silencieuse.

![Une campagne de messages in-app basée sur l'événement qui sera envoyée aux utilisateurs qui effectuent l'événement personnalisé « In-app message trigger » où « campaign_name » est égal à « Exemple de nom de campagne IAM ».]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Ces messages in-app ne se déclencheront que si la notification push silencieuse est reçue pendant que l'application se trouve au premier plan.
{% endalert %}
{% endtab %}
{% endtabs %}

### Affichage d'un message prédéfini {#displaying-a-pre-defined-message}

Pour afficher manuellement un message in-app prédéfini, utilisez la méthode suivante :

{% tabs %}
{% tab web %}
Pour le SDK Web, utilisez `braze.showInAppMessage(inAppMessage)` pour afficher tout message in-app. Pour plus de détails et un exemple, consultez [Affichage d'un message en temps réel](#displaying-a-message-in-real-time).
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```
{% endtab %}
{% endtabs %}

### Affichage d'un message en temps réel {#displaying-a-message-in-real-time}

Vous pouvez également créer et afficher des messages in-app locaux en temps réel, en utilisant les mêmes options de personnalisation que celles disponibles sur le tableau de bord. Pour ce faire :

{% tabs %}
{% tab web %}
```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
N'affichez pas les messages in-app lorsque le clavier logiciel est affiché à l'écran, car le rendu n'est pas défini dans ce cas.
{% endalert %}
{% endtab %}

{% tab swift %}
Appelez manuellement la méthode [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) sur votre `inAppMessagePresenter`. Par exemple :

{% subtabs %}
{% subtab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
En créant votre propre message in-app, vous renoncez à tout suivi analytique et devrez gérer manuellement l'enregistrement des clics et des impressions à l'aide de votre `message.context`.
{% endalert %}
{% endtab %}

{% tab unity %}
Pour afficher le message suivant dans la pile, utilisez la méthode `DisplayNextInAppMessage()`. Les messages seront enregistrés dans cette pile si `DISPLAY_LATER` ou `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` est choisi comme action d'affichage des messages in-app.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## Causes des retards de messages in-app {#causes-of-in-app-message-delays}

Si vous recevez une campagne de messages in-app quelques secondes après le démarrage de la session, le retard peut avoir été causé par :

- Un retard dans le déclencheur de la campagne
- Des personnalisations
- L'enregistrement de l'événement déclencheur plus tard que prévu (par exemple avec un `templated_iam`)

## Messages d'intention de sortie pour le web {#exit-intent-messages-for-web}

Les messages d'intention de sortie sont des messages in-app non perturbateurs utilisés pour communiquer des informations importantes aux visiteurs avant qu'ils ne quittent votre site web.

Pour configurer des déclencheurs pour ces types de messages dans le SDK Web, implémentez une bibliothèque d'intention de sortie sur votre site web (telle que la [bibliothèque open source de ouibounce](https://github.com/carlsednaoui/ouibounce)), puis utilisez le code suivant pour enregistrer `'exit intent'` en tant qu'événement personnalisé dans Braze. Désormais, vos futures campagnes de messages in-app peuvent utiliser ce type de message comme déclencheur d'événement personnalisé.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
