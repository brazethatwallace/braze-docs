---
nav_title: Gestion personnalisée de l'affichage
article_title: Personnaliser la gestion de l'affichage des messages in-app pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence couvre la gestion personnalisée de l'affichage des messages in-app pour votre application iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Gestion personnalisée de l'affichage des messages in-app {#custom-handling-in-app-message-display}

Lorsque le [`ABKInAppMessageControllerDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h) est défini, la méthode de délégation suivante sera appelée avant l'affichage des messages in-app :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

Si vous n'avez implémenté que [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h), la méthode suivante du délégué d'interface utilisateur sera appelée à la place :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage withKeyboardIsUp:(BOOL)keyboardIsUp;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

Vous pouvez personnaliser la gestion des messages in-app en implémentant cette méthode de délégation et en renvoyant l'une des valeurs suivantes pour `ABKInAppMessageDisplayChoice` :

| `ABKInAppMessageDisplayChoice` | Comportement |
| -------------------------- | -------- |
| Objective-C : `ABKDisplayInAppMessageNow`<br>Swift : `displayInAppMessageNow` | Le message sera affiché immédiatement. |
| Objective-C : `ABKDisplayInAppMessageLater`<br>Swift : `displayInAppMessageLater` | Le message ne sera pas affiché et sera replacé en haut de la pile. |
| Objective-C : `ABKDiscardInAppMessage`<br>Swift : `discardInAppMessage`| Le message sera supprimé et ne sera pas affiché. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestion personnalisée de l'affichage des messages in-app" }

Vous pouvez utiliser la méthode de délégation `beforeInAppMessageDisplayed:` pour ajouter une logique d'affichage des messages in-app, personnaliser les messages in-app avant que Braze ne les affiche, ou vous désengager complètement de la logique d'affichage et de l'interface utilisateur de Braze pour les messages in-app.

Consultez notre [exemple d'application](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m) pour un exemple de mise en œuvre.

## Remplacer les messages in-app avant l'affichage {#overriding-in-app-messages-before-display}

Si vous souhaitez modifier le comportement d'affichage des messages in-app, vous devez ajouter toute logique d'affichage nécessaire à votre méthode de délégation `beforeInAppMessageDisplayed:`. Par exemple, vous pouvez souhaiter afficher le message in-app depuis le haut de l'écran si le clavier est actuellement affiché, ou récupérer le modèle de données du message in-app et afficher le message in-app vous-même.

Si la campagne de messages in-app ne s'affiche pas lorsque la session a été lancée, assurez-vous que la logique d'affichage nécessaire a été ajoutée à votre méthode de délégation `beforeInAppMessageDisplayed:`. Cela permet à la campagne de messages in-app de s'afficher depuis le haut de l'écran même si le clavier est affiché.

## Désactivation du mode sombre {#disabling-dark-mode}

Pour empêcher les messages in-app d'adopter le style du mode sombre lorsque l'appareil de l'utilisateur a activé le mode sombre, utilisez la propriété [`ABKInAppMessage.enableDarkTheme`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message.html#ae89df6090bed623099ab0ecc0a74ad5d). Depuis la méthode `ABKInAppMessageControllerDelegate.beforeInAppMessageDisplayed:` ou la méthode `ABKInAppMessageUIDelegate.beforeInAppMessageDisplayed:`, définissez la propriété `enableDarkTheme` du paramètre `inAppMessage` de la méthode sur `NO`.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// ABKInAppMessageControllerDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}

// ABKInAppMessageUIDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMesssageDisplayed:(ABKInAppMessage *)inAppMessage
                                            withKeyboardIsUp:(BOOL)keyboardIsUp {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}
```

{% endtab %}
{% tab swift %}

```swift
// ABKInAppMessageControllerDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}

// ABKInAppMessageUIDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}
```

{% endtab %}
{% endtabs %}

## Masquer la barre d'état pendant l'affichage {#hiding-the-status-bar-during-display}

Pour les messages in-app `Full` et `HTML`, le SDK tentera par défaut de placer le message par-dessus la barre d'état. Cependant, dans certains cas, la barre d'état peut toujours apparaître au-dessus du message in-app. À partir de la version [3.21.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3211) du SDK iOS, vous pouvez forcer le masquage de la barre d'état lors de l'affichage des messages in-app `Full` et `HTML` en définissant `ABKInAppMessageHideStatusBarKey` sur `YES` dans les `appboyOptions` transmises à `startWithApiKey:`.

## Enregistrement des impressions et des clics {#logging-impressions-and-clicks}

L'enregistrement des impressions et des clics de messages in-app n'est pas automatique lorsque vous implémentez une gestion entièrement personnalisée (c.-à-d. que vous contournez l'affichage des messages in-app de Braze en renvoyant `ABKDiscardInAppMessage` dans votre `beforeInAppMessageDisplayed:`). Si vous choisissez de déployer votre propre interface utilisateur à l'aide de nos modèles de messages in-app, vous devez enregistrer les données analytiques à l'aide des méthodes suivantes sur la classe `ABKInAppMessage` :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Registers that a user has viewed an in-app message with the Braze server.
- (void) logInAppMessageImpression;
// Registers that a user has clicked on an in-app message with the Braze server.
- (void) logInAppMessageClicked;
```

{% endtab %}
{% tab swift %}

```swift
// Registers that a user has viewed an in-app message with the Braze server.
func logInAppMessageImpression()
// Registers that a user has clicked on an in-app message with the Braze server.
func logInAppMessageClicked()
```

{% endtab %}
{% endtabs %}

De plus, vous devriez enregistrer les clics sur les boutons des sous-classes de `ABKInAppMessageImmersive` (*c.-à-d.*, messages in-app `Modal` et `Full`) :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Logs button click analytics
- (void)logInAppMessageClickedWithButtonID:(NSInteger)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
// Logs button click analytics
func logInAppMessageClickedWithButtonID(buttonId: NSInteger)
```

{% endtab %}
{% endtabs %}

## Déclarations de méthode {#method-declarations}

Pour plus d'informations, consultez les fichiers d'en-tête suivants :

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Exemples d'implémentation {#implementation-samples}

Voir l'exemple d'application de messages in-app [`AppDelegate.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m).