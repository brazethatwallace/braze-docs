---
nav_title: Erweiterte Implementierung (optional)
article_title: Implementierungsleitfaden für In-App-Nachrichten für iOS (optional)
platform: iOS
page_order: 6
description: "Dieser Leitfaden für die erweiterte Implementierung enthält Hinweise zur Code-Anpassung für iOS-In-App-Nachrichten, drei von unserem Team entwickelte Anwendungsfälle und begleitende Code-Snippets."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
Suchen Sie den grundlegenden Entwicklerleitfaden zur Integration von In-App-Nachrichten? Finden Sie ihn im [grundlegenden Entwicklerleitfaden zur Integration von In-App-Nachrichten]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/overview).
{% endalert %}

# Implementierungsleitfaden für In-App-Nachrichten {#in-app-messaging-implementation-guide}

> Dieser optionale Leitfaden für die erweiterte Implementierung enthält Hinweise zur Code-Anpassung für In-App-Nachrichten, drei von unserem Team entwickelte angepasste Anwendungsfälle und begleitende Code-Snippets. Besuchen Sie unser [Braze Demo Repository auf GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Dieser Implementierungsleitfaden konzentriert sich auf eine Swift-Implementierung, aber für Interessierte werden auch Objective-C-Snippets bereitgestellt. Suchen Sie nach HTML-Implementierungen? Werfen Sie einen Blick auf unser [HTML-Template-Repository](https://github.com/braze-inc/in-app-message-templates)!

## Hinweise zur Code-Anpassung {#code-considerations}

Der folgende Leitfaden beschreibt eine optionale angepasste Entwickler-Integration, die zusätzlich zu den standardmäßigen In-App-Nachrichten verwendet werden kann. Zu jedem Anwendungsfall gibt es angepasste View-Controller mit Beispielen, wie Sie die Funktionalität erweitern und Aussehen und Handhabung Ihrer In-App-Nachrichten nativ anpassen können.

### ABKInAppMessage-Unterklassen {#abkinappmessage-subclasses}

Bei dem folgenden Code-Snippet handelt es sich um eine UI-Delegate-Methode aus dem Braze SDK, die festlegt, mit welcher Unterklassenansicht die In-App-Nachricht befüllt werden soll. Wir beschreiben in diesem Leitfaden eine grundlegende Implementierung und zeigen, wie die Unterklassen „Full“, „Slide-up“ und „Modal“ auf ansprechende Weise implementiert werden können. Beachten Sie, dass Sie alle anderen Unterklassen für In-App-Nachrichten einrichten müssen, wenn Sie einen angepassten View-Controller einrichten möchten. Nachdem Sie sich ein solides Verständnis der Konzepte hinter der Einrichtung von Unterklassen angeeignet haben, sehen Sie sich unsere [Anwendungsfälle](#sample-use-cases) an, um mit der Implementierung von Unterklassen für In-App-Nachrichten zu beginnen.

{% tabs %}
{% tab Swift %}
**ABKInAppMessage-Unterklassen**<br>

```swift
extension AppboyManager: ABKInAppMessageUIDelegate {
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return slideupViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageModal:
      return modalViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageFull:
      return fullViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
    }
  }
}
```
{% endtab %}
{% tab Objective-C %}
**ABKInAppMessage-Unterklassen**<br>

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [self slideupViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [self modalViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [self fullViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

## Anwendungsfälle {#use-cases}

Im Folgenden finden Sie drei Anwendungsfälle. Jeder Anwendungsfall enthält eine ausführliche Erklärung, relevante Code-Snippets sowie einen Blick darauf, wie In-App-Nachrichten im Braze-Dashboard aussehen und verwendet werden können:
- [Angepasste Slide-up-In-App-Nachricht](#custom-slide-up-in-app-message)
- [Angepasste modale In-App-Nachricht](#custom-modal-in-app-message)
- [Angepasste Full-In-App-Nachricht](#custom-full-in-app-message)

### Angepasste Slide-up-In-App-Nachricht {#custom-slide-up-in-app-message}

![Zwei iPhones nebeneinander. Beim ersten iPhone berührt die Slide-up-Nachricht den unteren Rand des Displays. Beim zweiten iPhone wird die Slide-up-Nachricht weiter oben auf dem Bildschirm angezeigt, sodass der App-Navigations-Button sichtbar ist.]({% image_buster /assets/img/iam_implementation/slideup.png %}){: style="float:right;max-width:45%;margin-left:15px;border:0;"}

Bei der Erstellung Ihrer Slide-up-In-App-Nachricht werden Sie feststellen, dass Sie die Platzierung der Nachricht mit den Standardmethoden nicht ändern können. Eine solche Änderung wird durch die Erstellung einer Unterklasse von `ABKInAppMessageSlideupViewController` und das Überschreiben der Variable `offset` mit Ihrer eigenen angepassten Variablen ermöglicht. Das nebenstehende Bild zeigt, wie Sie damit Ihre Slide-up-In-App-Nachrichten anpassen können.

Besuchen Sie den [`SlideFromBottomViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/SlideFromBottomViewController.swift), um loszulegen.

#### Hinzufügen von zusätzlichem Verhalten zur Standard-Benutzeroberfläche<br><br> {#adding-additional-behavior-to-our-default-ui}

{% tabs %}
{% tab Swift %}
**Aktualisieren der Variable `offset`**<br>
Aktualisieren Sie die Variable `offset` und legen Sie einen Offset fest, der Ihren Anforderungen entspricht.
```swift
func setSlideConstraint() {
  offset = 0
}
```

```swift
override var offset: CGFloat {
  get {
    return super.offset
  }
  set {
    super.offset = newValue + adjustedOffset
  }
}
```

{% details Version 3.34.0 or earlier  %}
**Aktualisieren der Variable `slideConstraint`**<br>
Die öffentliche Variable `slideConstraint` stammt aus der Superklasse `ABKInAppMessageSlideupViewController`.

```swift
func setSlideConstraint() {
    slideConstraint?.constant = bottomSpacing
}
```

```swift
private var bottomSpacing: CGFloat {
    return AppboyManager.shared.activeApplicationViewController.topMostViewController().view.safeAreaInsets.bottom
}
```
Besuchen Sie das Braze Demo Repository für die Funktion [`topMostViewController()`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/Utils/UIViewController_Util.swift#L17).
{% enddetails %}
{% endtab %}
{% tab Objective-C %}
**Aktualisieren der Variable `offset`**<br>
Aktualisieren Sie die Variable `offset` und legen Sie einen Offset fest, der Ihren Anforderungen entspricht.
```objc
- (void)setOffset {
  self.offset = 0;
}
```

```objc
- (CGFloat)offset {
  return [super offset];
}

- (void)setOffset:(CGFloat)offset {
  [super setOffset:offset + [self adjustedOffset]];
}
```
{% details Version 3.34.0 or earlier  %}
**Aktualisieren der Variable `slideConstraint`**<br>
Die öffentliche Variable `slideConstraint` stammt aus der Superklasse `ABKInAppMessageSlideupViewController`.

```objc
- (void)self.setSlideConstraint:(NSLayoutConstraint *)slideConstraint {
  slideConstraint.constant = bottomSpacing;
}
```

```objc
- (CGFloat)bottomSpacing {
  return [AppboyManager shared].activeApplicationViewController.topMostViewController.view.safeAreaInsets.bottom;
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Angepassten Constraint überschreiben und festlegen**<br>
Überschreiben Sie `beforeMoveInAppMessageViewOnScreen()` und legen Sie einen angepassten Constraint-Wert fest, der Ihren Anforderungen entspricht. Der ursprüngliche Wert wird in der Superklasse festgelegt.

```swift
override func beforeMoveInAppMessageViewOnScreen() {
  super.beforeMoveInAppMessageViewOnScreen()
  setOffset()
}
```

{% details Version 3.34.0 or earlier %}
```swift
override func beforeMoveInAppMessageViewOnScreen() {
  setSlideConstraint()
}
```
{% enddetails %}

{% endtab %}
{% tab Objective-C %}
**Angepassten Constraint überschreiben und festlegen**<br>
Überschreiben Sie `beforeMoveInAppMessageViewOnScreen()` und legen Sie einen angepassten Constraint-Wert fest, der Ihren Anforderungen entspricht. Der ursprüngliche Wert wird in der Superklasse festgelegt.

```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [super beforeMoveInAppMessageViewOnScreen];
  [self setOffset];
}
```

{% details Version 3.34.0 or earlier  %}
```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [self setSlideConstraint:self.slideConstraint];
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

**Constraint für Geräteausrichtung anpassen**<br>
Passen Sie den entsprechenden Wert in `viewWillTransition()` an, da die Unterklasse für die Synchronisierung des Constraints bei Layoutänderungen zuständig ist.

### Angepasste modale In-App-Nachricht {#custom-modal-in-app-message}

![Ein iPhone, das eine modale In-App-Nachricht anzeigt, mit der Sie durch eine Liste von Sportmannschaften blättern und Ihre Lieblingsmannschaft auswählen können. Am Ende dieser In-App-Nachricht befindet sich ein großer blauer Button zum Absenden.]({% image_buster /assets/img/iam_implementation/modal.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

Ein `ABKInAppMessageModalViewController` kann in Unterklassen unterteilt werden, um eine `UIPickerView` zur Erfassung wertvoller Nutzerattribute zu nutzen. Die angepasste modale In-App-Nachricht ermöglicht es Ihnen, Connected-Content oder eine beliebige verfügbare Liste zu verwenden, um Attribute aus einer dynamischen Artikelliste anzuzeigen und zu erfassen.

Sie können Ihre eigenen Ansichten in unterklassifizierte In-App-Nachrichten einfügen. Dieses Beispiel zeigt, wie eine `UIPickerView` genutzt werden kann, um die Funktionalität eines `ABKModalInAppMessageViewController` zu erweitern.

Besuchen Sie den [ModalPickerViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/ModalPickerViewController/ModalPickerViewController.swift), um loszulegen.

#### Dashboard-Konfiguration {#dashboard-configuration}

Um eine modale In-App-Nachricht im Dashboard einzurichten, müssen Sie eine Artikelliste angeben, die als kommagetrennte Zeichenkette formatiert ist. In unserem Beispiel verwenden wir Connected-Content, um eine JSON-Liste mit Teamnamen abzurufen und entsprechend zu formatieren.

![Der In-App-Nachrichten-Editor zeigt eine Vorschau, wie die In-App-Nachricht aussehen wird. Stattdessen wird die Artikelliste angezeigt, die Sie an Braze übermittelt haben. Da die Braze-Benutzeroberfläche Ihre angepasste In-App-Nachrichten-UI nur anzeigt, wenn sie an ein Telefon gesendet wird, gibt die Vorschau keinen Aufschluss darüber, wie Ihre Nachricht tatsächlich aussehen wird. Wir empfehlen daher, vor dem Senden einen Test durchzuführen.]({% image_buster /assets/img/iam_implementation/dashboard1.png %})

Geben Sie in den Schlüssel-Wert-Paaren einen `attribute_key` an. Dieser Schlüssel wird zusammen mit dem von Nutzer:innen ausgewählten Wert als angepasstes Attribut in ihrem Nutzerprofil gespeichert. Ihre angepasste Ansichtslogik muss die an Braze gesendeten Nutzerattribute verarbeiten.

Das Wörterbuch `extras` im Objekt `ABKInAppMessage` ermöglicht Ihnen die Abfrage eines Schlüssels des Typs `view_type` (falls vorhanden), der die korrekte Ansicht für die Anzeige angibt. Es ist wichtig zu wissen, dass In-App-Nachrichten pro Nachricht konfiguriert werden, sodass angepasste und standardmäßige modale Ansichten harmonisch zusammenarbeiten können.

![Zwei Schlüssel-Wert-Paare im Nachrichten-Editor. Das erste Schlüssel-Wert-Paar hat „attribute_key“ als „Favorite Team“ festgelegt, und das zweite hat „view_type“ als „picker“ festgelegt.]({% image_buster /assets/img/iam_implementation/dashboard2.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Swift %}
**Verwendung von `view_type` für das Anzeigeverhalten der Benutzeroberfläche**<br>
Fragen Sie das Wörterbuch `extras` für Ihren `view_type` ab, um den gewünschten untergeordneten View-Controller zu laden.

```swift
func modalViewController(inAppMessage: ABKInAppMessage) -> ABKInAppMessageModalViewController {
  switch inAppMessage.extras?[InAppMessageKey.viewType.rawValue] as? String {
  case InAppMessageViewType.picker.rawValue:
    return ModalPickerViewController(inAppMessage: inAppMessage)
  default:
    return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Verwendung von `view_type` für das Anzeigeverhalten der Benutzeroberfläche**<br>
Fragen Sie das Wörterbuch `extras` für Ihren `view_type` ab, um den gewünschten untergeordneten View-Controller zu laden.

```objc
- (ABKInAppMessageModalViewController *)modalViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyViewType];
  NSString *viewType = [inAppMessageData rawValueForInAppMessageViewType:InAppMessageViewTypePicker];

  if ([inAppMessage.extras objectForKey:key] && [inAppMessage.extras[key] isEqualToString:viewType]) {
    return [[ModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Angepasste Ansicht überschreiben und bereitstellen**<br>
Überschreiben Sie `loadView()` und stellen Sie Ihre eigene angepasste Ansicht ein, die Ihren Anforderungen entspricht.
```swift
override var nibname: String{
  return "ModalPickerViewController"
}

override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```
{% endtab %}
{% tab Objective-C %}
**Angepasste Ansicht überschreiben und bereitstellen**<br>
Überschreiben Sie `loadView()` und stellen Sie Ihre eigene angepasste Ansicht ein, die Ihren Anforderungen entspricht.
```objc
- (void)loadView {
  NSString *nibName = @"ModalPickerViewController";
  [[NSBundle mainBundle] loadNibNamed:nibName owner:self options:nil];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Variablen für eine dynamische Liste formatieren**<br>
Bevor die Komponenten von `UIPickerView` neu geladen werden, wird die Nachrichten-Variable `inAppMessage` als _String_ ausgegeben. Diese Nachricht muss als Array formatiert werden, um korrekt angezeigt zu werden. Dies kann beispielsweise durch die Verwendung von [`components(separatedBy: ", ")`](https://developer.apple.com/documentation/foundation/nsstring/1413214-components) erreicht werden.
```swift
override func viewDidLoad() {
  super.viewDidLoad()

  items = inAppMessage.message.separatedByCommaSpaceValue
  pickerView.reloadAllComponents()
}
```
{% endtab %}
{% tab Objective-C %}
**Variablen für PickerView formatieren**<br>
Bevor die Komponenten von `UIPickerView` neu geladen werden, wird die Nachrichten-Variable `inAppMessage` als _String_ ausgegeben. Diese Nachricht muss als Array formatiert werden, um korrekt angezeigt zu werden. Dies kann beispielsweise durch die Verwendung von [`componentsSeparatedByString`](https://developer.apple.com/documentation/foundation/nsstring/1413214-componentsseparatedbystring?language=objc) erreicht werden.
```objc
- (void)viewDidLoad {
  [super viewDidLoad];

  self.items = [[NSArray alloc] initWithArray:[self.inAppMessage.message componentsSeparatedByString:@", "]];
  [self.pickerView reloadAllComponents];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Angepasstes Attribut zuweisen**<br>
Nachdem Nutzer:innen auf „Senden“ getippt haben, übergeben Sie das Attribut mit dem entsprechend ausgewählten Wert unter Verwendung der Unterklasse an Braze.
```swift
@IBAction func primaryButtonTapped(_ sender: Any) {
  guard let item = selectedItem, !item.isEmpty, let attributeKey = inAppMessage.extras?[InAppMessageKey.attributeKey.rawValue] as? String else { return }

  AppboyManager.shared.setCustomAttributeWithKey(attributeKey, andStringValue: item)
}
```
{% endtab %}
{% tab Objective-C %}
**Angepasstes Attribut zuweisen**<br>
Nachdem Nutzer:innen auf „Senden“ getippt haben, übergeben Sie das Attribut mit dem entsprechend ausgewählten Wert unter Verwendung der Unterklasse an Braze.
```objc
- (IBAction)primaryButtonTapped:(id)sender {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyAttributeKey];

  if (self.selectedItem.length > 0 && [self.inAppMessage.extras objectForKey:key]) {
    [[AppboyManager shared] setCustomAttributeWithKey:self.inAppMessage.extras[key] andStringValue:self.selectedItem];
  }
}
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Möchten Sie unsere angepassten modalen In-App-Nachrichten nutzen, um Videos über FaceTime zu teilen? Sehen Sie sich unseren [Implementierungsleitfaden]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide/shareplay) für In-App-Nachrichten mit SharePlay an.
{% endalert%}

### Angepasste Full-In-App-Nachricht {#custom-full-in-app-message}

![Eine In-App-Nachricht, die eine Liste von Konfigurationsoptionen mit Kippschaltern neben jeder Option anzeigt. Am Ende der Nachricht befindet sich ein großer blauer Button zum Absenden.]({% image_buster /assets/img/iam_implementation/fullscreen.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

Verwenden Sie angepasste Full-In-App-Nachrichten, um interaktive, nutzerfreundliche Aufforderungen zur Erfassung wertvoller Kundendaten zu erstellen. Das nebenstehende Beispiel zeigt die Implementierung einer angepassten Full-In-App-Nachricht, die als interaktiver Push-Primer mit Präferenzen für Benachrichtigungen umgesetzt wurde.

Besuchen Sie den [`FullListViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/FullListViewController/FullListViewController.swift), um loszulegen.

#### Dashboard-Konfiguration

Um eine angepasste Full-In-App-Nachricht im Dashboard einzurichten, müssen Sie eine Liste Ihrer Tags angeben, die als kommagetrennte Zeichenkette formatiert ist.

Geben Sie in den Schlüssel-Wert-Paaren einen `attribute_key` an. Dieser Schlüssel wird zusammen mit den von Nutzer:innen ausgewählten Werten als angepasstes Attribut in ihrem Nutzerprofil gespeichert. Ihre angepasste Ansichtslogik muss die an Braze gesendeten Nutzerattribute verarbeiten.

![Drei Schlüssel-Wert-Paare im Nachrichten-Editor. Das erste „attribute_key“ ist als „Push Tags“ festgelegt, das zweite „subtitle_text“ als „Durch das Aktivieren von Benachrichtigungen wird auch …“ und das dritte „view_type“ als „table_list“.]({% image_buster /assets/img/iam_implementation/dashboard3.png %}){: style="max-width:65%;"}

#### Touch-Ereignisse in der In-App-Nachricht abfangen {#intercepting-in-app-message-touches}
![Ein Apple-Gerät, das Reihen von Einstellungen und Kippschaltern anzeigt. Die angepasste Ansicht verwaltet die Buttons, und alle Berührungen außerhalb der Button-Steuerelemente werden von der In-App-Nachricht verarbeitet und schließen diese.]({% image_buster /assets/img/iam_implementation_guide.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
Das Abfangen von Touch-Ereignissen in der In-App-Nachricht ist entscheidend, damit die Buttons der angepassten Full-In-App-Nachricht korrekt funktionieren. Standardmäßig fügt `ABKInAppMessageImmersive` der Nachricht eine Tippgesten-Erkennung hinzu, sodass Nutzer:innen Nachrichten ohne Buttons ausblenden können. Durch Hinzufügen eines `UISwitch` oder Buttons zur Ansichtshierarchie `UITableViewCell` werden die Berührungen nun von der angepassten Ansicht verarbeitet. Seit iOS 6 haben Buttons und andere Steuerelemente bei der Arbeit mit Gestenerkennung Vorrang, sodass unsere angepasste Full-In-App-Nachricht wie vorgesehen funktioniert.