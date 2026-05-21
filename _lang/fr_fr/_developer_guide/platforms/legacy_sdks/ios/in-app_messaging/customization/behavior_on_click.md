---
nav_title: Comportement personnalisé en cas de clic
article_title: Personnaliser le comportement des messages in-app sur clic pour iOS
platform: iOS
page_order: 5
description: "Cet article de référence couvre le comportement au clic personnalisé du message in-app pour votre application iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Personnaliser le comportement des messages in-app au clic {#customize-in-app-message-behavior-on-click}

La propriété `inAppMessageClickActionType` sur l'objet `ABKInAppMessage` définit le comportement de l'action après le clic sur le message in-app. Cette propriété est en lecture seule. Si vous souhaitez modifier le comportement au clic du message in-app, vous pouvez appeler la méthode suivante sur `ABKInAppMessage` :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[inAppMessage setInAppMessageClickAction:clickActionType withURI:uri];
```

{% endtab %}
{% tab swift %}

```swift
inAppMessage.setInAppMessageClickAction(clickActionType: clickActionType, withURI: uri)
```

{% endtab %}
{% endtabs %}

Le `inAppMessageClickActionType` peut être défini sur l'une des valeurs suivantes :

| `ABKInAppMessageClickActionType` | Comportement au clic |
| -------------------------- | -------- |
| `ABKInAppMessageRedirectToURI` | L'URI donné s'affiche lorsque l'on clique sur le message, et le message est fermé. Notez que le paramètre `uri` ne peut pas être nul. |
| `ABKInAppMessageNoneClickAction` | Le message sera fermé lorsque l'on clique dessus. Notez que le paramètre `uri` sera ignoré, et la propriété `uri` sur l'objet `ABKInAppMessage` sera définie sur nul. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personnaliser le comportement des messages in-app au clic" }

{% alert important %}
Pour les messages in-app contenant des boutons, le `clickAction` du message sera également inclus dans le payload final si l'action de clic est ajoutée avant l'ajout du texte du bouton.
{% endalert %}

## Personnaliser les clics sur le corps du message in-app {#customizing-in-app-message-body-clicks}

La méthode de délégation [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) suivante est appelée lorsque l'on clique sur un message in-app :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL) onInAppMessageClicked:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageClicked(inAppMessage: ABKInAppMessage!) -> Bool
```

{% endtab %}
{% endtabs %}

## Personnaliser les clics sur les boutons du message in-app {#customizing-in-app-message-button-clicks}

Pour les clics sur les boutons de message in-app et les boutons de message in-app HTML (tels que les liens), [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) inclut les méthodes de délégation suivantes :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button;

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageButtonClicked(inAppMessage: ABKInAppMessageImmersive!,
                                 button: ABKInAppMessageButton) -> Bool

func onInAppMessageHTMLButtonClicked(inAppMessage: ABKInAppMessageHTML!,
                                     clickedURL: URL, buttonID: String) -> Bool
```

{% endtab %}
{% endtabs %}

Chaque méthode renvoie une valeur `BOOL` pour indiquer si Braze doit continuer à exécuter l'action de clic.

Pour accéder au type d'action de clic d'un bouton dans une méthode de délégation, vous pouvez utiliser le code suivant :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if ([inAppMessage isKindOfClass:[ABKInAppMessageImmersive class]]) {
      ABKInAppMessageImmersive *immersiveIAM = (ABKInAppMessageImmersive *)inAppMessage;
      NSArray<ABKInAppMessageButton *> *buttons = immersiveIAM.buttons;
      for (ABKInAppMessageButton *button in buttons) {
         // Button action type is accessible via button.buttonClickActionType
      }
   }
```

{% endtab %}
{% tab swift %}

```swift
if inAppMessage is ABKInAppMessageImmersive {
      let immersiveIAM = inAppMessage as! ABKInAppMessageImmersive;
      for button in inAppMessage.buttons as! [ABKInAppMessageButton]{
        // Button action type is accessible via button.buttonClickActionType
      }
    }
```

{% endtab %}
{% endtabs %}

Lorsqu'un message in-app comporte des boutons, les seules actions de clic exécutées sont celles du modèle `ABKInAppMessageButton`. Le corps du message in-app ne sera pas cliquable, même si le modèle `ABKInAppMessage` dispose de l'action de clic par défaut.

## Déclarations de méthode {#method-declarations}

Pour plus d'informations, consultez les fichiers d'en-tête suivants :

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)