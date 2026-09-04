{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Einrichten des UI-Delegates (erforderlich) {#setting-up-the-ui-delegate-required}

Um die Darstellung von In-App-Nachrichten anzupassen und auf verschiedene Lifecycle-Ereignisse zu reagieren, müssen Sie [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) einrichten. Dies ist ein Delegate-Protokoll, das zum Empfangen und Verarbeiten von getriggerten In-App-Nachrichten-Payloads, zum Empfangen von Anzeige-Lifecycle-Ereignissen und zur Steuerung des Anzeige-Timings verwendet wird. Um `BrazeInAppMessageUIDelegate` zu verwenden, müssen Sie:
- Die Standard-Implementierung [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) als Ihren `inAppMessagePresenter` verwenden.
- Die `BrazeUI`-Bibliothek in Ihr Projekt einbinden.

### Schritt 1: Implementieren Sie das `BrazeInAppMessageUIDelegate`-Protokoll {#step-1-implement-the-brazeinappmessageuidelegate-protocol}

Implementieren Sie zunächst das `BrazeInAppMessageUIDelegate`-Protokoll und alle entsprechenden Methoden, die Sie verwenden möchten. Im folgenden Beispiel wird dieses Protokoll in der `AppDelegate`-Klasse der Anwendung implementiert.

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

### Schritt 2: Weisen Sie das `delegate`-Objekt zu {#step-2-assign-the-delegate-object}

Weisen Sie das `delegate`-Objekt der `BrazeInAppMessageUI`-Instanz zu, bevor Sie diese In-App-Nachrichten-UI als Ihren `inAppMessagePresenter` festlegen.

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
Nicht alle Delegate-Methoden sind in Objective-C verfügbar, da ihre Parameter mit der Sprach-Laufzeitumgebung nicht kompatibel sind.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Eine schrittweise Implementierung des In-App-Nachrichten-UI-Delegates finden Sie in diesem [Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
{% endalert %}

## Verhalten bei Klick {#on-click-behavior}

Jedes `Braze.InAppMessage`-Objekt enthält eine entsprechende [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction), die das Verhalten beim Klick definiert.

### Klick-Aktionstypen {#click-action-types}

Die Eigenschaft `clickAction` Ihrer `Braze.InAppMessage` ist standardmäßig auf `.none` gesetzt, kann aber auf einen der folgenden Werte eingestellt werden:

| `ClickAction` | Verhalten bei Klick |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | Öffnet die angegebene URL in einem externen Browser. Wenn `useWebView` auf `true` gesetzt ist, wird sie in einer Web-View geöffnet. |
| `.none` | Die Nachricht wird beim Klick geschlossen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Klick-Aktionstypen" }

{% alert important %}
Bei In-App-Nachrichten mit Buttons wird die `clickAction` der Nachricht auch in den endgültigen Payload aufgenommen, wenn die Klick-Aktion vor dem Hinzufügen des Button-Texts hinzugefügt wird.
{% endalert %}

### Verhalten bei Klick anpassen {#customizing-on-click-behavior}

Um dieses Verhalten anzupassen, können Sie die Eigenschaft `clickAction` ändern, indem Sie das folgende Beispiel verwenden:

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

Die Methode `inAppMessage(_:prepareWith:)` ist in Objective-C nicht verfügbar.

{% endtab %}
{% endtabs %}

### Behandlung des angepassten Verhaltens {#handling-the-custom-behavior}

Die folgende Delegate-Methode von [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) wird aufgerufen, wenn Nutzer:innen auf eine In-App-Nachricht klicken. Dieser Callback wird bei nutzer:innen-initiierten Klicks auf Buttons von In-App-Nachrichten und HTML-In-App-Nachrichten-Buttons (Links) ausgelöst, und eine Button-ID wird als optionaler Parameter für diese Interaktionen bereitgestellt. Dieser Callback wird nicht bei programmatischen Klicks aufgerufen, die über `brazeBridge.logClick()` ausgelöst werden.

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

Diese Methode gibt einen booleschen Wert zurück, der angibt, ob Braze die Klick-Aktion weiterhin ausführen soll.

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

## Slideup-Nachrichten durch Wischen schließen {#swiping-to-dismiss-slideup-messages}

Standardmäßig können Slideup-In-App-Nachrichten durch eine Wischgeste geschlossen werden. Die Wischrichtung hängt von der Position des Slideups ab:

- **Wischen nach links oder rechts:** Schließt das Slideup unabhängig von seiner Position.
- **Slideup von unten:** Wischen von oben nach unten schließt die Nachricht. Wischen von unten nach oben schließt sie nicht.
- **Slideup von oben:** Wischen von unten nach oben schließt die Nachricht. Wischen von oben nach unten schließt sie nicht.

Dieses Wischverhalten ist in die Standard-`BrazeInAppMessageUI` [`SlideupView`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/slideupview) integriert und gilt nur für Slideup-In-App-Nachrichten. Modale und Vollbild-In-App-Nachrichten unterstützen das Schließen durch Wischen nicht. Um die Slideup-Ansicht weiter anzupassen, einschließlich des Wischverhaltens, können Sie die [`SlideupView.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/slideupview/attributes-swift.struct) ändern oder eine angepasste Ansicht durch Subklassen bereitstellen.

{% alert note %}
Das Tippen außerhalb einer Slideup-Nachricht schließt diese nicht. Für modale oder Vollbild-In-App-Nachrichten können Sie das Schließen durch Tippen außerhalb der Nachricht mithilfe des Attributs `dismissOnBackgroundTap` aktivieren, das im folgenden Abschnitt beschrieben wird.
{% endalert %}

## Modale Schließvorgänge anpassen {#customizing-modal-dismissals}

Um das Schließen durch Tippen außerhalb der Nachricht zu aktivieren, können Sie die Eigenschaft `dismissOnBackgroundTap` in der `Attributes`-Struktur des In-App-Nachrichtentyps ändern, den Sie anpassen möchten.

Wenn Sie dieses Feature beispielsweise für modale Bild-In-App-Nachrichten aktivieren möchten, können Sie Folgendes konfigurieren:

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

Die Anpassung über `Attributes` ist in Objective-C nicht verfügbar.

{% endtab %}
{% endtabs %}

Der Standardwert ist `false`. Dieser bestimmt, ob die modale In-App-Nachricht geschlossen wird, wenn Nutzer:innen außerhalb der In-App-Nachricht tippen.

| `DismissModalOnOutsideTap` | Beschreibung |
|----------|-------------|
| `true`         | Modale In-App-Nachrichten werden beim Tippen außerhalb geschlossen.     |
| `false`        | Standard – modale In-App-Nachrichten werden beim Tippen außerhalb nicht geschlossen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modale Schließvorgänge anpassen" }

Weitere Informationen zur Anpassung von In-App-Nachrichten finden Sie in diesem [Artikel](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization).

## Nachrichtenausrichtung anpassen {#customizing-message-orientation}

Sie können die Ausrichtung Ihrer In-App-Nachrichten anpassen. Sie können eine neue Standardausrichtung für alle Nachrichten festlegen oder eine benutzerdefinierte Ausrichtung für eine einzelne Nachricht konfigurieren.

{% tabs local %}
{% tab Alle Nachrichten %}
Um eine Standardausrichtung für alle In-App-Nachrichten festzulegen, verwenden Sie die Methode [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog), um die Eigenschaft `preferredOrientation` im `PresentationContext` zu setzen.

Um beispielsweise „Hochformat“ als Standardausrichtung festzulegen:

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

{% tab Einzelne Nachricht %}
Um die Ausrichtung für eine einzelne Nachricht festzulegen, ändern Sie die Eigenschaft `orientation` von `Braze.InAppMessage`:

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

Nachdem die In-App-Nachricht angezeigt wurde, führt jede Änderung der Geräteausrichtung, während die Nachricht noch angezeigt wird, dazu, dass sich die Nachricht mit dem Gerät dreht (vorausgesetzt, dies wird durch die `orientation`-Konfiguration der Nachricht unterstützt).

Die Geräteausrichtung muss außerdem von der `orientation`-Eigenschaft der In-App-Nachricht unterstützt werden, damit die Nachricht angezeigt wird. Zusätzlich wird die Einstellung `preferredOrientation` nur berücksichtigt, wenn sie in den unterstützten Schnittstellenausrichtungen Ihrer Anwendung im Abschnitt **Deployment Info** der Zieleinstellungen in Xcode enthalten ist.

![Unterstützte Ausrichtungen in Xcode.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %}){: width="2038" height="590"}

{% alert note %}
Die Ausrichtung wird nur für die Darstellung der Nachricht angewendet. Nachdem das Gerät die Ausrichtung geändert hat, übernimmt die Nachrichtenansicht eine der von ihr unterstützten Ausrichtungen. Auf kleineren Geräten (iPhones, iPod Touch) kann das Festlegen einer Querformat-Ausrichtung für eine modale oder bildschirmfüllende In-App-Nachricht zu abgeschnittenen Inhalten führen.
{% endalert %}

## Anzeigezeitpunkt anpassen {#customizing-display-timing}

Sie können steuern, ob eine verfügbare In-App-Nachricht an bestimmten Stellen der Nutzererfahrung angezeigt wird. Wenn es Situationen gibt, in denen die In-App-Nachricht nicht erscheinen soll – beispielsweise während eines Vollbildspiels oder auf einem Ladebildschirm –, können Sie ausstehende In-App-Nachrichten verzögern oder verwerfen. Um den Zeitpunkt von In-App-Nachrichten zu steuern, verwenden Sie die [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)`, um die Eigenschaft `BrazeInAppMessageUI.DisplayChoice` festzulegen.

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

Konfigurieren Sie `BrazeInAppMessageUI.DisplayChoice` so, dass einer der folgenden Werte zurückgegeben wird:

| Anzeigeoption                       | Verhalten                                                                                                                   |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `.now`                              | Die Nachricht wird sofort angezeigt. Dies ist der Standardwert.                                                             |
| `.reenqueue`                        | Die Nachricht wird nicht angezeigt und wieder oben auf den Stack gelegt.                                                    |
| `.later`                            | Die Nachricht wird nicht angezeigt und wieder oben auf den Stack gelegt. (Veraltet, bitte verwenden Sie `.reenqueue`)       |
| `.discard`                          | Die Nachricht wird verworfen und nicht angezeigt.                                                                           |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anzeigezeitpunkt anpassen" }

{% alert tip %}
Ein Beispiel für `InAppMessageUI` finden Sie in unserem [Swift-Braze-SDK-Repository](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) und [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI).
{% endalert %}

## Statusleiste ausblenden {#hiding-the-status-bar}

Für In-App-Nachrichten vom Typ `Full`, `FullImage` und `HTML` blendet das SDK die Statusleiste standardmäßig aus. Bei anderen Typen von In-App-Nachrichten bleibt die Statusleiste unverändert. Um dieses Verhalten zu konfigurieren, verwenden Sie die [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)`, um die Eigenschaft `statusBarHideBehavior` im `PresentationContext` festzulegen. Dieses Feld akzeptiert einen der folgenden Werte:

| Verhalten zum Ausblenden der Statusleiste | Beschreibung                                                                          |
| ----------------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                                   | Die Nachrichtenansicht entscheidet über den Ausblendungsstatus der Statusleiste.      |
| `.hidden`                                 | Die Statusleiste wird immer ausgeblendet.                                             |
| `.visible`                                | Die Statusleiste wird immer angezeigt.                                                |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statusleiste ausblenden" }

## Dark Mode deaktivieren {#disabling-dark-mode}

Um zu verhindern, dass In-App-Nachrichten das Dark-Mode-Styling übernehmen, wenn auf dem Gerät der Nutzer:innen der Dark Mode aktiviert ist, implementieren Sie die `inAppMessage(_:prepareWith:)` [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog). Der an die Methode übergebene `PresentationContext` enthält eine Referenz auf das `InAppMessage`-Objekt, das angezeigt werden soll. Jede `InAppMessage` hat eine `themes`-Eigenschaft, die ein `dark`- und ein `light`-Mode-Theme enthält. Wenn Sie die Eigenschaft `themes.dark` auf `nil` setzen, zeigt Braze die In-App-Nachricht automatisch mit dem Light-Theme an.

In-App-Nachrichtentypen mit Buttons haben ein zusätzliches `themes`-Objekt in ihrer `buttons`-Eigenschaft. Um zu verhindern, dass Buttons das Dark-Mode-Styling übernehmen, können Sie [`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d) verwenden, um ein neues Array von Buttons mit einem `light`-Theme und ohne `dark`-Theme zu erstellen.

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

## App Store-Bewertungsaufforderung anpassen {#customizing-the-app-store-review-prompt}

Sie können In-App-Nachrichten in einer Campaign verwenden, um Nutzer:innen um eine App Store-Bewertung zu bitten.

{% alert note %}
Da diese Beispiel-Aufforderung das Standardverhalten von Braze überschreibt, können Impressionen nicht automatisch erfasst werden, wenn sie implementiert wird. Sie müssen [Ihre eigenen Analytics protokollieren]({{site.baseurl}}/developer_guide/analytics).
{% endalert %}

### Schritt 1: In-App-Nachrichten-Delegate einrichten {#step-1-set-the-in-app-message-delegate}

Richten Sie zunächst das [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/in_app_messages/customization#swift_setting-up-the-ui-delegate-required) in Ihrer App ein.

### Schritt 2: Standard-App Store-Bewertungsnachricht deaktivieren {#step-2-disable-the-default-app-store-review-message}

Implementieren Sie als Nächstes die `inAppMessage(_:displayChoiceForMessage:)` [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb), um die Standard-App Store-Bewertungsnachricht zu deaktivieren.

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

### Schritt 3: Deeplink erstellen {#step-3-create-a-deep-link}

Fügen Sie in Ihrem [`scene:openURLContexts:`]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#swift_step-3-implement-a-handler)-Handler den folgenden Code hinzu, um den `{YOUR-APP-SCHEME}:app-store-review`-Deeplink zu verarbeiten. Beachten Sie, dass Sie `StoreKit` importieren müssen, um `SKStoreReviewController` verwenden zu können:

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

### Schritt 4: Angepasstes Klickverhalten festlegen {#step-4-set-custom-on-click-behavior}

Erstellen Sie als Nächstes eine In-App-Messaging-Campaign mit folgenden Einstellungen:

- Das Schlüssel-Wert-Paar `"AppStore Review" : "true"`
- Das Klickverhalten auf „Deeplink in App“ gesetzt, unter Verwendung des Deeplinks `{YOUR-APP-SCHEME}:app-store-review`.

{% endraw %}

{% alert tip %}
Apple beschränkt App Store-Bewertungsaufforderungen auf maximal drei Mal pro Jahr für jede:n Nutzer:in. Daher sollte Ihre Campaign auf drei Mal pro Jahr pro Nutzer:in [frequenzlimitiert]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) werden.<br><br>Nutzer:innen können App Store-Bewertungsaufforderungen deaktivieren. Daher sollte Ihre angepasste Bewertungsaufforderung nicht versprechen, dass eine native App Store-Bewertungsaufforderung erscheint, und auch nicht direkt um eine Bewertung bitten.
{% endalert %}