{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Configuration du délégué d'interface utilisateur (obligatoire) {#setting-up-the-ui-delegate-required}

Pour personnaliser la présentation des messages in-app et réagir aux différents événements du cycle de vie, vous devez configurer [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate). Il s'agit d'un protocole de délégation utilisé pour recevoir et traiter les payloads des messages in-app déclenchés, recevoir les événements du cycle de vie d'affichage et contrôler le timing d'affichage. Pour utiliser `BrazeInAppMessageUIDelegate`, vous devez :
- Utiliser l'implémentation par défaut de [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) comme `inAppMessagePresenter`.
- Inclure la bibliothèque `BrazeUI` dans votre projet.

### Étape 1 : Implémenter le protocole `BrazeInAppMessageUIDelegate` {#step-1-implement-the-brazeinappmessageuidelegate-protocol}

Commencez par implémenter le protocole `BrazeInAppMessageUIDelegate` ainsi que les méthodes correspondantes souhaitées. Dans l'exemple suivant, ce protocole est implémenté dans la classe `AppDelegate` de l'application.

{% tabs %}
{% tab swift %}
```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```
{% endtab %}
{% endtabs %}

### Étape 2 : Assigner l'objet `delegate` {#step-2-assign-the-delegate-object}

Assignez l'objet `delegate` sur l'instance `BrazeInAppMessageUI` avant d'assigner cette interface utilisateur de message in-app comme `inAppMessagePresenter`.

{% tabs %}
{% tab swift %}
```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

{% alert important %}
Toutes les méthodes de délégation ne sont pas disponibles en Objective-C en raison de l'incompatibilité de leurs paramètres avec le runtime du langage.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Pour un déploiement étape par étape du délégué d'interface utilisateur des messages in-app, consultez ce [tutoriel](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
{% endalert %}

## Comportement au clic {#on-click-behavior}

Chaque objet `Braze.InAppMessage` contient une [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction) correspondante, qui définit le comportement lors du clic.

### Types d'actions au clic {#click-action-types}

La propriété `clickAction` de votre `Braze.InAppMessage` est définie par défaut sur `.none`, mais peut prendre l'une des valeurs suivantes :

| `ClickAction` | Comportement au clic |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | Ouvre l'URL donnée dans un navigateur externe. Si `useWebView` est défini sur `true`, l'URL s'ouvrira dans une vue web. |
| `.none` | Le message sera fermé lors du clic. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types d'actions au clic" }

{% alert important %}
Pour les messages in-app contenant des boutons, le `clickAction` du message sera également inclus dans le payload final si l'action au clic est ajoutée avant le texte du bouton.
{% endalert %}

### Personnaliser le comportement au clic {#customizing-on-click-behavior}

Pour personnaliser ce comportement, vous pouvez modifier la propriété `clickAction` en vous référant à l'exemple suivant :

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

La méthode `inAppMessage(_:prepareWith:)` n'est pas disponible en Objective-C.

{% endtab %}
{% endtabs %}

### Gérer le comportement personnalisé {#handling-the-custom-behavior}

La méthode déléguée [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) suivante est appelée lorsqu'un utilisateur clique sur un message in-app. Ce rappel est déclenché pour les clics initiés par l'utilisateur sur les boutons de messages in-app et les boutons de messages in-app HTML (liens), et un identifiant de bouton est fourni en tant que paramètre optionnel pour ces interactions. Ce rappel n'est pas invoqué pour les clics programmatiques déclenchés via `brazeBridge.logClick()`.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

Cette méthode renvoie une valeur booléenne pour indiquer si Braze doit continuer à exécuter l'action au clic.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?, message: Braze.InAppMessage, view: InAppMessageView
) -> Bool {
    guard let buttonId,
      let idInt = Int(buttonId)
    else { return true }
    var button: BrazeKit.Braze.InAppMessage.Button? = nil

    switch message {
    case .modal(let modal):
      button = modal.buttons[idInt]

    case .modalImage(let modalImage):
      button = modalImage.buttons[idInt]

    case .full(let full):
      button = full.buttons[idInt]

    case .fullImage(let fullImage):
      button = fullImage.buttons[idInt]

    default:
      break
    }

    print(button?.id)
    print(button?.text)
    print(button?.clickAction)

    return true
  }
```

{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view {
  NSInteger buttonInt = [buttonId integerValue];

  if (message.type == BRZInAppMessageRawTypeFull || message.type == BRZInAppMessageRawTypeModal) {
    BRZInAppMessageRawButton *button = message.buttons[buttonInt];
    NSLog(@"%ld", (long)button.identifier);
    NSLog(@"%@", button.text);
    NSLog(@"%ld", (long)button.clickAction);
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}

## Balayer pour fermer les messages contextuels {#swiping-to-dismiss-slideup-messages}

Par défaut, les messages in-app contextuels peuvent être fermés par un geste de balayage. La direction du balayage dépend de la position du message contextuel :

- **Balayage vers la gauche ou la droite :** Ferme le message contextuel quelle que soit sa position.
- **Message contextuel depuis le bas :** Un balayage de haut en bas ferme le message. Un balayage de bas en haut ne le ferme pas.
- **Message contextuel depuis le haut :** Un balayage de bas en haut ferme le message. Un balayage de haut en bas ne le ferme pas.

Ce comportement de balayage est intégré à la vue [`SlideupView`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/slideupview) par défaut de `BrazeInAppMessageUI` et s'applique uniquement aux messages in-app contextuels. Les messages in-app modaux et plein écran ne prennent pas en charge la fermeture par balayage. Pour personnaliser davantage la vue contextuelle, y compris le comportement de balayage, vous pouvez modifier les [`SlideupView.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/slideupview/attributes-swift.struct) ou fournir une vue personnalisée via le sous-classement.

{% alert note %}
Appuyer en dehors d'un message contextuel ne le ferme pas. Pour les messages in-app modaux ou plein écran, vous pouvez activer la fermeture par appui extérieur à l'aide de l'attribut `dismissOnBackgroundTap` décrit dans la section suivante.
{% endalert %}

## Personnalisation de la fermeture des fenêtres modales {#customizing-modal-dismissals}

Pour permettre la fermeture par un tap en dehors du message, vous pouvez modifier la propriété `dismissOnBackgroundTap` dans la structure `Attributes` du type de message in-app que vous souhaitez personnaliser.

Par exemple, si vous souhaitez activer cette fonctionnalité pour les messages in-app de type image modale, vous pouvez configurer ce qui suit :

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

La personnalisation via `Attributes` n'est pas disponible en Objective-C.

{% endtab %}
{% endtabs %}

La valeur par défaut est `false`. Elle détermine si le message in-app modal sera fermé lorsque l'utilisateur tape en dehors du message in-app.

| `DismissModalOnOutsideTap` | Description |
|----------|-------------|
| `true`         | Les messages in-app modaux seront fermés lors d'un tap en dehors du message.     |
| `false`        | Par défaut, les messages in-app modaux ne seront pas fermés lors d'un tap en dehors du message. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personnalisation de la fermeture des fenêtres modales" }

Pour plus de détails sur la personnalisation des messages in-app, consultez cet [article](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization).

## Personnaliser l'orientation des messages {#customizing-message-orientation}

Vous pouvez personnaliser l'orientation de vos messages in-app. Vous pouvez définir une nouvelle orientation par défaut pour tous les messages ou définir une orientation personnalisée pour un seul message.

{% tabs local %}
{% tab all messages %}
Pour choisir une orientation par défaut pour tous les messages in-app, utilisez la méthode [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) afin de définir la propriété `preferredOrientation` sur le `PresentationContext`.

Par exemple, pour définir le mode portrait comme orientation par défaut :

{% subtabs %}
{% subtab swift %}
```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab single message %}
Pour définir l'orientation d'un seul message, modifiez la propriété `orientation` de `Braze.InAppMessage` :

{% subtabs %}
{% subtab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

Une fois le message in-app affiché, tout changement d'orientation de l'appareil pendant que le message est toujours visible entraînera la rotation du message avec l'appareil (à condition que cette orientation soit prise en charge par la configuration `orientation` du message).

L'orientation de l'appareil doit également être prise en charge par la propriété `orientation` du message in-app pour que celui-ci s'affiche. De plus, le paramètre `preferredOrientation` ne sera respecté que s'il est inclus dans les orientations d'interface prises en charge par votre application, dans la section **Deployment Info** des paramètres de votre cible dans Xcode.

![Orientations prises en charge dans Xcode.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %}){: width="2038" height="590"}

{% alert note %}
L'orientation s'applique uniquement à la présentation du message. Après un changement d'orientation de l'appareil, la vue du message adopte l'une des orientations qu'elle prend en charge. Sur les appareils de petite taille (iPhones, iPod Touch), définir une orientation paysage pour un message in-app modal ou plein écran peut entraîner un contenu tronqué.
{% endalert %}

## Personnaliser le moment d'affichage {#customizing-display-timing}

Vous pouvez contrôler si un message in-app disponible s'affichera à certains moments de l'expérience utilisateur. Si vous ne souhaitez pas que le message in-app apparaisse dans certaines situations, par exemple pendant un jeu en plein écran ou sur un écran de chargement, vous pouvez retarder ou ignorer les messages in-app en attente. Pour contrôler le moment d'affichage des messages in-app, utilisez la [méthode déléguée](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` pour définir la propriété `BrazeInAppMessageUI.DisplayChoice`.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui displayChoiceForMessage:(BRZInAppMessageRaw *)message
```

{% endtab %}
{% endtabs %}

Configurez `BrazeInAppMessageUI.DisplayChoice` pour renvoyer l'une des valeurs suivantes :

| Choix d'affichage                   | Comportement                                                                                                                       |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `.now`                              | Le message sera affiché immédiatement. Il s'agit de la valeur par défaut.                                                          |
| `.reenqueue`                        | Le message ne sera pas affiché et sera replacé en haut de la pile.                                                                 |
| `.later`                            | Le message ne sera pas affiché et sera replacé en haut de la pile. (Obsolète, veuillez utiliser `.reenqueue`)                      |
| `.discard`                          | Le message sera ignoré et ne sera pas affiché.                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personnaliser le moment d'affichage" }

{% alert tip %}
Pour un exemple d'`InAppMessageUI`, consultez notre [dépôt Swift du SDK Braze](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) et [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI).
{% endalert %}

## Masquer la barre d'état {#hiding-the-status-bar}

Pour les messages in-app `Full`, `FullImage` et `HTML`, le SDK masque la barre d'état par défaut. Pour les autres types de messages in-app, la barre d'état reste inchangée. Pour configurer ce comportement, utilisez la [méthode de délégué](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)` pour définir la propriété `statusBarHideBehavior` sur le `PresentationContext`. Ce champ accepte l'une des valeurs suivantes :

| Comportement de masquage de la barre d'état | Description                                                                           |
| -------------------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                                      | La vue du message détermine l'état de masquage de la barre d'état.                    |
| `.hidden`                                    | Toujours masquer la barre d'état.                                                     |
| `.visible`                                   | Toujours afficher la barre d'état.                                                    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Masquer la barre d'état" }

## Désactiver le mode sombre {#disabling-dark-mode}

Pour empêcher les messages in-app d'adopter le style du mode sombre lorsque l'appareil de l'utilisateur a le mode sombre activé, implémentez la [méthode déléguée](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)`. Le `PresentationContext` transmis à la méthode contient une référence à l'objet `InAppMessage` à présenter. Chaque `InAppMessage` possède une propriété `themes` contenant un thème pour le mode `dark` et un pour le mode `light`. Si vous définissez la propriété `themes.dark` sur `nil`, Braze présentera automatiquement le message in-app en utilisant son thème clair.

Les types de messages in-app avec des boutons possèdent un objet `themes` supplémentaire sur leur propriété `buttons`. Pour empêcher les boutons d'adopter le style du mode sombre, vous pouvez utiliser [`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d) pour créer un nouveau tableau de boutons avec un thème `light` et sans thème `dark`.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  switch context.message {
    case .slideup:
      guard var slideup = context.message.slideup else { return }
      slideup.themes.dark = nil
      context.message.slideup = slideup

    case .modal:
      guard var modal = context.message.modal else { return }
      modal.themes.dark = nil
      modal.buttons = modal.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modal = modal

    case .modalImage:
      guard var modalImage = context.message.modalImage else { return }
      modalImage.themes.dark = nil
      modalImage.buttons = modalImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modalImage = modalImage

    case .full:
      guard var full = context.message.full else { return }
      full.themes.dark = nil
      full.buttons = full.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.full = full

    case .fullImage:
      guard var fullImage = context.message.fullImage else { return }
      fullImage.themes.dark = nil
      fullImage.buttons = fullImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.fullImage = fullImage

    default:
      break
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  switch (context.message.type) {
    case BRZInAppMessageRawTypeSlideup: {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;
      break;
    }
    case BRZInAppMessageRawTypeModal:
    case BRZInAppMessageRawTypeFull:
    {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;

      NSMutableArray *updatedButtons = [NSMutableArray arrayWithCapacity:context.message.buttons.count];
      for (BRZInAppMessageRawButton *button in context.message.buttons) {
        BRZInAppMessageRawButtonTheme *lightTheme = BRZInAppMessageRawButtonTheme.defaultLight;
        BRZInAppMessageRawButton *newButton = [button mutableCopy];
        newButton.textColor = lightTheme.textColor;
        newButton.backgroundColor = lightTheme.backgroundColor;
        newButton.borderColor = lightTheme.borderColor;
        [updatedButtons addObject:newButton];
      }
      context.message.buttons = updatedButtons;
      break;
    }
    default:
      break;
  }
}
```

{% endtab %}
{% endtabs %}

## Personnaliser l'invite d'évaluation de l'App Store {#customizing-the-app-store-review-prompt}

Vous pouvez utiliser les messages in-app dans une Campaign pour demander aux utilisateurs de laisser un avis sur l'App Store.

{% alert note %}
Étant donné que cet exemple d'invite remplace le comportement par défaut de Braze, les impressions ne peuvent pas être suivies automatiquement si cette solution est déployée. Vous devez [enregistrer vos propres données analytiques]({{site.baseurl}}/developer_guide/analytics).
{% endalert %}

### Étape 1 : Configurer le délégué de message in-app {#step-1-set-the-in-app-message-delegate}

Tout d'abord, configurez le [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/in_app_messages/customization#swift_setting-up-the-ui-delegate-required) dans votre application.

### Étape 2 : Désactiver le message d'évaluation App Store par défaut {#step-2-disable-the-default-app-store-review-message}

Ensuite, implémentez la [méthode de délégué](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` pour désactiver le message d'évaluation App Store par défaut.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

### Étape 3 : Créer un deep link {#step-3-create-a-deep-link}

Dans votre gestionnaire [`scene:openURLContexts:`]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#swift_step-3-implement-a-handler), ajoutez le code suivant pour traiter le deep link `{YOUR-APP-SCHEME}:app-store-review`. Notez que vous devrez importer `StoreKit` pour utiliser `SKStoreReviewController` :

{% tabs %}
{% tab swift %}

```swift
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
  guard let url = URLContexts.first?.url else { return }
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
  NSURL *url = URLContexts.allObjects.firstObject.URL;
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

### Étape 4 : Définir un comportement personnalisé au clic {#step-4-set-custom-on-click-behavior}

Ensuite, créez une Campaign de messages in-app avec les éléments suivants :

- La paire clé-valeur `"AppStore Review" : "true"`
- Le comportement au clic défini sur « Deep link vers l'application », en utilisant le deep link `{YOUR-APP-SCHEME}:app-store-review`.

{% endraw %}

{% alert tip %}
Apple limite les invites d'évaluation de l'App Store à un maximum de trois fois par an pour chaque utilisateur, votre Campaign devrait donc être [limitée en fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) à trois fois par an et par utilisateur.<br><br>Les utilisateurs peuvent désactiver les invites d'évaluation de l'App Store. Par conséquent, votre invite d'évaluation personnalisée ne doit pas promettre qu'une invite d'évaluation native de l'App Store apparaîtra, ni demander directement un avis.
{% endalert %}