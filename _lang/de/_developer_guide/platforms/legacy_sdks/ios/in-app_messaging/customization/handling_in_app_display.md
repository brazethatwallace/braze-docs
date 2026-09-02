---
nav_title: Angepasste Anzeige
article_title: Anpassen der Anzeige von In-App-Nachrichten für iOS
platform: iOS
page_order: 4
description: "Dieser Referenzartikel behandelt die angepasste Handhabung der Anzeige von In-App-Nachrichten für Ihre iOS-Anwendung."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Angepasste Handhabung der Anzeige von In-App-Nachrichten {#custom-handling-in-app-message-display}

Wenn die [`ABKInAppMessageControllerDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h) gesetzt ist, wird die folgende Delegatenmethode aufgerufen, bevor In-App-Nachrichten angezeigt werden:

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

Wenn Sie nur [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) implementiert haben, wird stattdessen die folgende UI-Delegate-Methode aufgerufen:

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

Sie können die Behandlung von In-App-Nachrichten anpassen, indem Sie diese Delegatenmethode implementieren und einen der folgenden Werte für `ABKInAppMessageDisplayChoice` zurückgeben:

| `ABKInAppMessageDisplayChoice` | Verhalten |
| -------------------------- | -------- |
| Objective-C: `ABKDisplayInAppMessageNow`<br>Swift: `displayInAppMessageNow` | Die Nachricht wird sofort angezeigt. |
| Objective-C: `ABKDisplayInAppMessageLater`<br>Swift: `displayInAppMessageLater` | Die Nachricht wird nicht angezeigt und wieder oben auf dem Stack abgelegt. |
| Objective-C: `ABKDiscardInAppMessage`<br>Swift: `discardInAppMessage`| Die Nachricht wird verworfen und nicht angezeigt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Angepasste Handhabung der Anzeige von In-App-Nachrichten" }

Mit der Delegatenmethode `beforeInAppMessageDisplayed:` können Sie eine Logik für die Anzeige von In-App-Nachrichten hinzufügen, In-App-Nachrichten anpassen, bevor Braze sie anzeigt, oder die Anzeigelogik und das UI von Braze für In-App-Nachrichten vollständig umgehen.

In unserer [Beispielanwendung](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m) finden Sie ein Implementierungsbeispiel.

## In-App-Nachrichten vor der Anzeige außer Kraft setzen {#overriding-in-app-messages-before-display}

Wenn Sie das Anzeigeverhalten von In-App-Nachrichten ändern möchten, sollten Sie die erforderliche Anzeigelogik zu Ihrer `beforeInAppMessageDisplayed:`-Delegatenmethode hinzufügen. So können Sie z. B. die In-App-Nachricht vom oberen Bildschirmrand aus anzeigen lassen, wenn gerade die Tastatur eingeblendet ist, oder das Datenmodell der In-App-Nachricht übernehmen und die In-App-Nachricht selbst anzeigen.

Wenn die In-App-Nachricht-Campaign nicht angezeigt wird, wenn die Sitzung gestartet wurde, vergewissern Sie sich, dass Sie die notwendige Anzeigelogik zu Ihrer `beforeInAppMessageDisplayed:`-Delegatenmethode hinzugefügt haben. Damit kann die In-App-Nachricht-Campaign auch dann vom oberen Bildschirmrand aus angezeigt werden, wenn die Tastatur eingeblendet ist.

## Dark Mode deaktivieren {#disabling-dark-mode}

Um zu verhindern, dass In-App-Nachrichten das Design des Dark Mode übernehmen, wenn auf dem Gerät der Nutzer:innen der Dark Mode aktiviert ist, verwenden Sie die Eigenschaft [`ABKInAppMessage.enableDarkTheme`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message.html#ae89df6090bed623099ab0ecc0a74ad5d). Setzen Sie entweder in der Methode `ABKInAppMessageControllerDelegate.beforeInAppMessageDisplayed:` oder `ABKInAppMessageUIDelegate.beforeInAppMessageDisplayed:` die Eigenschaft `enableDarkTheme` des Parameters `inAppMessage` auf `NO`.

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

## Ausblenden der Statusleiste während der Anzeige {#hiding-the-status-bar-during-display}

Bei `Full`- und `HTML`-In-App-Nachrichten versucht das SDK or Software-Development-Kit standardmäßig, die Nachricht über der Statusleiste zu platzieren. In einigen Fällen kann die Statusleiste jedoch weiterhin über der In-App-Nachricht erscheinen. Ab Version [3.21.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3211) des iOS SDK or Software-Development-Kit können Sie erzwingen, dass die Statusleiste beim Anzeigen von `Full`- und `HTML`-In-App-Nachrichten ausgeblendet wird, indem Sie `ABKInAppMessageHideStatusBarKey` auf `YES` innerhalb der `appboyOptions` setzen, die an `startWithApiKey:` übergeben werden.

## Impressionen und Klicks protokollieren {#logging-impressions-and-clicks}

Die Protokollierung von Impressionen und Klicks bei In-App-Nachrichten erfolgt nicht automatisch, wenn Sie eine vollständig angepasste Handhabung implementieren (z. B. wenn Sie die Anzeige von In-App-Nachrichten durch Braze umgehen, indem Sie `ABKDiscardInAppMessage` in Ihrer `beforeInAppMessageDisplayed:`-Methode zurückgeben). Wenn Sie sich dafür entscheiden, Ihr eigenes UI unter Verwendung unserer In-App-Nachricht-Modelle zu implementieren, müssen Sie die Analytics mit den folgenden Methoden der Klasse `ABKInAppMessage` protokollieren:

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

Außerdem sollten Sie die Button-Klicks in den Unterklassen von `ABKInAppMessageImmersive` protokollieren (*d. h.* `Modal`- und `Full`-In-App-Nachrichten):

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

## Methoden-Deklarationen {#method-declarations}

Weitere Informationen finden Sie in den folgenden Header-Dateien:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Beispiele für die Implementierung {#implementation-samples}

Siehe die Beispiel-App für In-App-Nachrichten [`AppDelegate.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m).