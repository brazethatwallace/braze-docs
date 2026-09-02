---
nav_title: Erweiterte Implementierung (optional)
article_title: Implementierungsleitfaden für Content Cards für iOS (optional)
platform: iOS
page_order: 7
description: "Dieser Leitfaden für die erweiterte Implementierung enthält Hinweise zur Code-Anpassung von iOS Content Cards, drei von unserem Team entwickelte Anwendungsfälle, begleitende Code-Snippets und eine Anleitung zur Protokollierung von Impressionen, Klicks und Ausblendungen."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
Suchen Sie nach dem grundlegenden Entwicklerleitfaden zur Integration von Content Cards? Finden Sie ihn im [grundlegenden Entwicklerleitfaden zur Integration von Content Cards]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration).
{% endalert %}

# Implementierungsleitfaden für Content Cards {#content-card-implementation-guide}

> Dieser optionale Leitfaden für die erweiterte Implementierung enthält Hinweise zur Code-Anpassung für Content Cards, drei von unserem Team entwickelte angepasste Anwendungsfälle, begleitende Code-Snippets sowie eine Anleitung zur Protokollierung von Impressionen, Klicks und Ausblendungen. Besuchen Sie unser [Braze Demo Repository auf GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Beachten Sie, dass sich dieser Implementierungsleitfaden auf eine Swift-Implementierung konzentriert, aber für Interessierte auch Objective-C-Snippets bereitgestellt werden.

## Hinweise zur Code-Anpassung {#code-considerations}

### Content Cards als angepasste Objekte {#content-cards-as-custom-objects}

Ähnlich wie eine Rakete, die einen Booster erhält, können Ihre eigenen angepassten Objekte erweitert werden, um als Content Cards zu fungieren. Begrenzte API-Oberflächen wie diese bieten die Flexibilität, mit verschiedenen Daten-Backends austauschbar zu arbeiten. Dies kann durch die Konformität mit dem `ContentCardable`-Protokoll und die Implementierung des Initializers (wie in den folgenden Code-Snippets gezeigt) erreicht werden. Durch die Verwendung der `ContentCardData`-Struktur können Sie auf die `ABKContentCard`-Daten zugreifen. Die `ABKContentCard`-Payload wird verwendet, um die `ContentCardData`-Struktur und das angepasste Objekt selbst zu initialisieren – alles aus einem `Dictionary`-Typ über den Initializer, den das Protokoll mitbringt.

Der Initializer enthält auch ein `ContentCardClassType`-Enum. Dieses Enum wird verwendet, um zu entscheiden, welches Objekt initialisiert werden soll. Durch die Verwendung von Schlüssel-Wert-Paaren im Braze-Dashboard können Sie einen expliziten `class_type`-Schlüssel festlegen, der bestimmt, welches Objekt initialisiert wird. Diese Schlüssel-Wert-Paare für Content Cards werden über die Variable `extras` auf der `ABKContentCard` übergeben. Eine weitere zentrale Komponente des Initializers ist der `metaData`-Dictionary-Parameter. Die `metaData` enthalten alles aus der `ABKContentCard`, aufgeteilt in eine Reihe von Schlüsseln und Werten. Nachdem die relevanten Cards geparst und in Ihre angepassten Objekte konvertiert wurden, ist die App bereit, mit ihnen zu arbeiten, als wären sie aus JSON oder einer anderen Quelle instanziiert worden.

Sobald Sie ein solides Verständnis dieser Hinweise zur Code-Anpassung haben, werfen Sie einen Blick auf unsere [Anwendungsfälle](#sample-use-cases), um mit der Implementierung Ihrer angepassten Objekte zu beginnen.

{% tabs local %}
{% tab ContentCardable %}
{% subtabs global %}
{% subtab Swift %}
**ContentCardable-Protokoll**<br>
Ein `ContentCardData`-Objekt, das die `ABKContentCard`-Daten zusammen mit einem `ContentCardClassType`-Enum repräsentiert. Ein Initializer, der verwendet wird, um angepasste Objekte mit `ABKContentCard`-Metadaten zu instanziieren.
```swift
protocol ContentCardable {
  var contentCardData: ContentCardData? { get }
  init?(metaData: [ContentCardKey: Any], classType contentCardClassType: ContentCardClassType)
}

extension ContentCardable {
  var isContentCard: Bool {
    return contentCardData != nil
  }

  func logContentCardClicked() {
    BrazeManager.shared.logContentCardClicked(idString: contentCardData?.contentCardId)
  }

  func logContentCardDismissed() {
    BrazeManager.shared.logContentCardDismissed(idString: contentCardData?.contentCardId)
  }

  func logContentCardImpression() {
    BrazeManager.shared.logContentCardImpression(idString: contentCardData?.contentCardId)
  }
}
```
**Content-Card-Datenstruktur**<br>
`ContentCardData` repräsentiert die geparsten Werte einer `ABKContentCard`.

```swift
struct ContentCardData: Hashable {
  let contentCardId: String
  let contentCardClassType: ContentCardClassType
  let createdAt: Double
  let isDismissable: Bool
  ...
  // other Content Card properties such as expiresAt, pinned, etc.
}

extension ContentCardData: Equatable {
  static func ==(lhs: ContentCardData, rhs: ContentCardData) -> Bool {
    return lhs.contentCardId == rhs.contentCardId
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
**ContentCardable-Protokoll**<br>
Ein `ContentCardData`-Objekt, das die `ABKContentCard`-Daten zusammen mit einem `ContentCardClassType`-Enum repräsentiert, ein Initializer, der verwendet wird, um angepasste Objekte mit `ABKContentCard`-Metadaten zu instanziieren.
```objc
@protocol ContentCardable <NSObject>

@property (nonatomic, strong) ContentCardData *contentCardData;
- (instancetype __nullable)initWithMetaData:(NSDictionary *)metaData
                                  classType:(enum ContentCardClassType)classType;

- (BOOL)isContentCard;
- (void)logContentCardImpression;
- (void)logContentCardClicked;
- (void)logContentCardDismissed;

@end
```
**Content-Card-Datenstruktur**<br>
`ContentCardData` repräsentiert die geparsten Werte einer `ABKContentCard`.

```objc
@interface ContentCardData : NSObject

+ (ContentCardClassType)contentCardClassTypeForString:(NSString *)rawValue;

- (instancetype)initWithIdString:(NSString *)idString
                       classType:(ContentCardClassType)classType
                       createdAt:(double)createdAt isDismissible:(BOOL)isDismissible;

@property (nonatomic, readonly) NSString *contentCardId;
@property (nonatomic) ContentCardClassType classType;
@property (nonatomic, readonly) double *createdAt;
@property (nonatomic, readonly) BOOL isDismissible;
...
// other Content Card properties such as expiresAt, pinned, etc.

@end
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Angepasste Objekte %}
{% subtabs global %}
{% subtab Swift %}
**Initializer für angepasste Objekte**<br>
Metadaten aus einer `ABKContentCard` werden verwendet, um die Variablen Ihres Objekts zu befüllen. Die im Braze-Dashboard eingerichteten Schlüssel-Wert-Paare werden im „extras“-Dictionary dargestellt.

```swift
extension CustomObject: ContentCardable {
  init?(metaData: [ContentCardKey: Any], classType contentCardClassType: ContentCardClassType) {
    guard let idString = metaData[.idString] as? String,
      let createdAt = metaData[.created] as? Double,
      let isDismissable = metaData[.dismissable] as? Bool,
      let extras = metaData[.extras] as? [AnyHashable: Any],
      else { return nil }

    let contentCardData = ContentCardData(contentCardId: idString, contentCardClassType: contentCardClassType, createdAt: createdAt, isDismissable: isDismissable)
    let customObjectProperty = extras["YOUR-CUSTOM-OBJECT-PROPERTY"] as? String

    self.init(contentCardData: contentCardData, property: customObjectProperty)
  }
}
```

**Typen identifizieren**<br>
Das `ContentCardClassType`-Enum repräsentiert den `class_type`-Wert im Braze-Dashboard. Dieser Wert wird auch als Filter-Bezeichner verwendet, um Content Cards an verschiedenen Stellen anzuzeigen.

```swift
enum ContentCardClassType: Hashable {
  case yourValue
  case yourOtherValue
  ...
  case none

  init(rawType: String?) {
    switch rawType?.lowercased() {
    case "your_value": // these values much match the value set in the Braze dashboard
      self = .yourValue
    case "your_other_value": // these values much match the value set in the Braze dashboard
      self = .yourOtherValue
    ...
    default:
      self = .none
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Initializer für angepasste Objekte**<br>
Metadaten aus einer `ABKContentCard` werden verwendet, um die Variablen Ihres Objekts zu befüllen. Die im Braze-Dashboard eingerichteten Schlüssel-Wert-Paare werden im „extras“-Dictionary dargestellt.


```objc
- (id _Nullable)initWithMetaData:(nonnull NSDictionary *)metaData classType:(enum ContentCardClassType)classType {
  self = [super init];
  if (self) {
    if ([metaData objectForKey:ContentCardKeyIdString] && [metaData objectForKey:ContentCardKeyCreated] && [metaData objectForKey:ContentCardKeyDismissible] && [metaData objectForKey:ContentCardKeyExtras]) {
      NSDictionary  *extras = metaData[ContentCardKeyExtras];
      NSString *idString = metaData[ContentCardKeyIdString];
      double createdAt = [metaData[ContentCardKeyCreated] doubleValue];
      BOOL isDismissible = metaData[ContentCardKeyDismissible];

      if ([extras objectForKey: @"YOUR-CUSTOM-PROPERTY")
        _customObjectProperty = extras[@"YOUR-CUSTOM-OBJECT-PROPERTY"];

      self.contentCardData = [[ContentCardData alloc] initWithIdString:idString classType:classType createdAt:createdAt isDismissible:isDismissible];

      return self;
    }
  }
  return nil;
}
```

**Typen identifizieren**<br>
Das `ContentCardClassType`-Enum repräsentiert den `class_type`-Wert im Braze-Dashboard. Dieser Wert wird auch als Filter-Bezeichner verwendet, um Content Cards an verschiedenen Stellen anzuzeigen.

```objc
typedef NS_ENUM(NSInteger, ContentCardClassType) {
  ContentCardClassTypeNone = 0,
  ContentCardClassTypeYourValue,
  ContentCardClassTypeYourOtherValue,
  ...
};

+ (NSArray *)contentCardClassTypeArray {
  return @[ @"", @"your_value", @"your_other_value" ];
}

+ (ContentCardClassType)contentCardClassTypeForString:(NSString*)rawValue {
  if ([[self contentCardClassTypeArray] indexOfObject:rawValue] == NSNotFound) {
    return ContentCardClassTypeNone;
  } else {
    NSInteger value = [[self contentCardClassTypeArray] indexOfObject:rawValue];
    return (ContentCardClassType) value;
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Content Cards verarbeiten %}
{% subtabs global %}
{% subtab Swift %}
**Content Cards anfordern**<br>
Solange der Observer noch im Speicher gehalten wird, kann der Benachrichtigungs-Callback vom Braze SDK or Software-Development-Kit erwartet werden.

```swift
func loadContentCards() {
  BrazeManager.shared.addObserverForContentCards(observer: self, selector: #selector(contentCardsUpdated))
  BrazeManager.shared.requestContentCardsRefresh()
}
```

**Den Content-Cards-SDK or Software-Development-Kit-Callback verarbeiten**<br>
Leiten Sie den Benachrichtigungs-Callback an die Hilfsdatei weiter, um die Payload-Daten für Ihre angepassten Objekte zu parsen.
```swift
@objc func contentCardsUpdated(_ notification: Notification) {
  guard let contentCards = BrazeManager.shared.handleContentCardsUpdated(notification, for: [.yourValue]) as? [CustomObject],!contentCards.isEmpty else { return }

 // do something with your array of custom objects
}
```

**Mit Content Cards arbeiten**<br>
Der `class_type` wird als Filter übergeben, um nur Content Cards zurückzugeben, die einen übereinstimmenden `class_type` haben.

```swift
func handleContentCardsUpdated(_ notification: Notification, for classTypes: [ContentCardClassType]) -> [ContentCardable] {
  guard let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool, updateIsSuccessful, let cards = contentCards else { return [] }

  return convertContentCards(cards, for: classTypes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Content Cards anfordern**<br>
Solange der Observer noch im Speicher gehalten wird, kann der Benachrichtigungs-Callback vom Braze SDK or Software-Development-Kit erwartet werden.

```objc
- (void)loadContentCards {
  [[BrazeManager shared] addObserverForContentCards:self selector:@selector(contentCardsUpdated:)];
  [[BrazeManager shared] requestContentCardsRefresh];
}
```

**Den Content-Cards-SDK or Software-Development-Kit-Callback verarbeiten**<br>
Leiten Sie den Benachrichtigungs-Callback an die Hilfsdatei weiter, um die Payload-Daten für Ihre angepassten Objekte zu parsen.
```objc
- (void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeYourValue)];
  NSArray *contentCards = [[BrazeManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes];

  // do something with your array of custom objects
}
```

**Mit Content Cards arbeiten**<br>
Der `class_type` wird als Filter übergeben, um nur Content Cards zurückzugeben, die einen übereinstimmenden `class_type` haben.

```objc
- (NSArray *)handleContentCardsUpdated:(NSNotification *)notification forClassType:(ContentCardClassType)classType {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    return [self convertContentCards:self.contentCards forClassType:classType];
  } else {
    return @[];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Mit Payload-Daten arbeiten %}
{% subtabs global %}
{% subtab Swift %}
**Mit Payload-Daten arbeiten**<br>
Durchläuft das Array der Content Cards und parst nur die Cards mit einem übereinstimmenden `class_type`. Die Payload einer ABKContentCard wird in ein `Dictionary` geparst.

```swift
func convertContentCards(_ cards: [ABKContentCard], for classTypes: [ContentCardClassType]) -> [ContentCardable] {
  var contentCardables: [ContentCardable] = []

  for card in cards {
    let classTypeString = card.extras?[ContentCardKey.classType.rawValue] as? String
    let classType = ContentCardClassType(rawType: classTypeString)
    guard classTypes.contains(classType) else { continue }

    var metaData: [ContentCardKey: Any] = [:]
    switch card {
    case let banner as ABKBannerContentCard:
      metaData[.image] = banner.image
    case let captioned as ABKCaptionedImageContentCard:
      metaData[.title] = captioned.title
      metaData[.cardDescription] = captioned.cardDescription
      metaData[.image] = captioned.image
    case let classic as ABKClassicContentCard:
      metaData[.title] = classic.title
      metaData[.cardDescription] = classic.cardDescription
    default:
      break
    }

    metaData[.idString] = card.idString
    metaData[.created] = card.created
    metaData[.dismissible] = card.dismissible
    metaData[.urlString] = card.urlString
    metaData[.extras] = card.extras
    ...
    // other Content Card properties such as expiresAt, pinned, etc.

    if let contentCardable = contentCardable(with: metaData, for: classType) {
      contentCardables.append(contentCardable)
    }
  }
  return contentCardables
}
```

**Ihre angepassten Objekte aus Content-Card-Payload-Daten initialisieren**<br>
Der `class_type` wird verwendet, um zu bestimmen, welches Ihrer angepassten Objekte aus den Payload-Daten initialisiert wird.

```swift
func contentCardable(with metaData: [ContentCardKey: Any], for classType: ContentCardClassType) -> ContentCardable? {
  switch classType {
  case .yourValue:
    return CustomObject(metaData: metaData, classType: classType)
  case .yourOtherValue:
    return OtherCustomObject(metaData: metaData, classType: classType)
  ...
  default:
    return nil
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Mit Payload-Daten arbeiten**<br>
Durchläuft das Array der Content Cards und parst nur die Cards mit einem übereinstimmenden `class_type`. Die Payload einer ABKContentCard wird in ein `Dictionary` geparst.

```objc
- (NSArray *)convertContentCards:(NSArray<ABKContentCard*> *)cards forClassType:(ContentCardClassType)classType {
  NSMutableArray *contentCardables = [[NSMutableArray alloc] init];      for (ABKContentCard *card in cards) {
    NSString *classTypeString = [card.extras objectForKey:ContentCardKeyClassType];
    ContentCardClassType cardClassType = [ContentCardData contentCardClassTypeForString: classTypeString];
    if (cardClassType != classType) { continue; }

    NSMutableDictionary *metaData = [[NSMutableDictionary alloc] init];
    if ([card isKindOfClass:[ABKBannerContentCard class]]) {
      ABKBannerContentCard *banner = (ABKBannerContentCard *)card;
      metaData[ContentCardKeyImage] = banner.image;
    } else if ([card isKindOfClass:[ABKCaptionedImageContentCard class]]) {
      ABKCaptionedImageContentCard *captioned = (ABKCaptionedImageContentCard *)card;
      metaData[ContentCardKeyTitle] = captioned.title;
      metaData[ContentCardKeyCardDescription] = captioned.cardDescription;
      metaData[ContentCardKeyImage] = captioned.image;
    } else if ([card isKindOfClass:[ABKClassicContentCard class]]) {
      ABKClassicContentCard *classic = (ABKClassicContentCard *)card;
      metaData[ContentCardKeyCardDescription] = classic.title;
      metaData[ContentCardKeyImage] = classic.image;
    }

    metaData[ContentCardKeyIdString] = card.idString;
    metaData[ContentCardKeyCreated] = [NSNumber numberWithDouble:card.created];
    metaData[ContentCardKeyDismissible] = [NSNumber numberWithBool:card.dismissible];
    metaData[ContentCardKeyUrlString] = card.urlString;
    metaData[ContentCardKeyExtras] = card.extras;
    ...
    // other Content Card properties such as expiresAt, pinned, etc.

    id<ContentCardable> contentCardable = [self contentCardableWithMetaData:metaData forClassType:classType];
    if (contentCardable) {
      [contentCardables addObject:contentCardable];
    }
  }

  return contentCardables;
}
```

**Ihre angepassten Objekte aus Content-Card-Payload-Daten initialisieren**<br>
Der `class_type` wird verwendet, um zu bestimmen, welches Ihrer angepassten Objekte aus den Payload-Daten initialisiert wird.

```obj-c
- (id<ContentCardable>)contentCardableWithMetaData:(NSDictionary *)metaData forClassType:(ContentCardClassType)classType {
  switch (classType) {
    case ContentCardClassTypeYourValue:
      return [[CustomObject alloc] initWithMetaData:metaData classType:classType];
    case ContentCardClassTypeYourOtherValue:
      return nil;
    ...
    default:
      return nil;
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Anwendungsfälle {#use-cases}

Im folgenden Abschnitt haben wir drei Anwendungsfälle bereitgestellt. Jeder Anwendungsfall bietet eine detaillierte Erklärung, relevante Code-Snippets und einen Einblick, wie Content-Card-Variablen im Braze-Dashboard aussehen und verwendet werden können:
- [Content Cards als ergänzende Inhalte](#content-cards-as-supplemental-content)
- [Content Cards in einem Nachrichtencenter](#content-cards-in-a-message-center)
- [Interaktive Content Cards](#interactive-content-cards)

### Content Cards als ergänzende Inhalte {#content-cards-as-supplemental-content}

![Feed mit einer hybriden Liste, die lokale Daten und Braze Content Cards kombiniert.]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Sie können Content Cards nahtlos in einen bestehenden Feed integrieren, sodass Daten aus mehreren Feeds gleichzeitig geladen werden. Dies schafft ein stimmiges, harmonisches Erlebnis mit Braze Content Cards und bestehenden Feed-Inhalten.

Das begleitende Beispiel zeigt eine `UICollectionView` mit einer hybriden Liste von Artikeln, die sowohl über lokale Daten als auch über von Braze bereitgestellte Content Cards befüllt werden. Damit können Content Cards nicht von vorhandenen Inhalten unterschieden werden.

#### Dashboard-Konfiguration {#dashboard-configuration}

Diese Content-Card wird über eine API-getriggerte Campaign mit API-getriggerten Schlüssel-Wert-Paaren ausgeliefert. Dies ist ideal für Campaigns, bei denen die Werte der Karte von externen Faktoren abhängen, um zu bestimmen, welche Inhalte den Nutzer:innen angezeigt werden. Beachten Sie, dass `class_type` zum Zeitpunkt der Einrichtung bekannt sein sollte.

![Die Schlüssel-Wert-Paare für den Anwendungsfall ergänzende Content Cards. In diesem Beispiel werden verschiedene Aspekte der Karte wie „tile_id“, „tile_deeplink“ und „tile_title“ mithilfe von Liquid festgelegt.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

##### Bereit, Analytics zu protokollieren? {#ready-to-log-analytics}
Besuchen Sie den [folgenden Abschnitt](#logging-impressions-clicks-and-dismissals), um ein besseres Verständnis dafür zu bekommen, wie der Datenfluss aussehen sollte.

### Content Cards in einem Nachrichtencenter {#content-cards-in-a-message-center}
<br>
Content Cards können in einem Nachrichtencenter-Format verwendet werden, bei dem jede Nachricht eine eigene Karte ist. Jede Nachricht im Nachrichtencenter wird über ein Content-Card-Payload befüllt, und jede Karte enthält zusätzliche Schlüssel-Wert-Paare, die das On-Klick, der or klicken-UI/UX steuern. Im folgenden Beispiel leitet eine Nachricht Sie zu einer beliebigen angepassten Ansicht weiter, während eine andere ein Webview öffnet, das angepasstes HTML anzeigt.

![Content-Card-Nachrichtencenter mit individuellen Nachrichtenkarten.]({% image_buster /assets/img/cc_implementation/message_center.png %}){: style="border:0;"}{: style="max-width:80%;border:0"}

#### Dashboard-Konfiguration

Für die folgenden Nachrichtentypen sollte das Schlüssel-Wert-Paar `class_type` zu Ihrer Dashboard-Konfiguration hinzugefügt werden. Die hier zugewiesenen Werte sind beliebig, sollten sich jedoch zwischen den Klassentypen unterscheiden lassen. Diese Schlüssel-Wert-Paare sind die Schlüsselkennungen, anhand derer die Anwendung entscheidet, wohin navigiert wird, wenn Nutzer:innen auf eine gekürzte Posteingangs-Nachricht klicken.

{% tabs local %}
{% tab Beliebige angepasste Ansicht – Ganzseitig %}

Die Schlüssel-Wert-Paare für diesen Anwendungsfall umfassen:

- `message_header` gesetzt als `Full Page`
- `class_type` gesetzt als `message_full_page`

![Ganzseitiges Content-Card-Nachrichtenbeispiel.]({% image_buster /assets/img/cc_implementation/full_page.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Webview-Nachricht – HTML %}

Die Schlüssel-Wert-Paare für diesen Anwendungsfall umfassen:

- `message_header` gesetzt als `HTML`
- `class_type` gesetzt als `message_webview`
- `message_title`

Diese Nachricht sucht ebenfalls nach einem HTML-Schlüssel-Wert-Paar. Wenn Sie jedoch mit einer Web-Domain arbeiten, ist auch ein URL-Schlüssel-Wert-Paar gültig.

![Content-Card, die ein HTML-Webview über ein Schlüssel-Wert-Paar öffnet.]({% image_buster /assets/img/cc_implementation/html_webview.png %}){: style="max-width:60%;"}

{% endtab %}
{% endtabs %}

#### Weitere Erläuterung {#further-explanation}

Die Nachrichtencenter-Logik wird durch den `contentCardClassType` gesteuert, der über die Schlüssel-Wert-Paare von Braze bereitgestellt wird. Mithilfe der Methode `addContentCardToView` können Sie diese Klassentypen sowohl filtern als auch identifizieren.

{% tabs %}
{% tab Swift %}
**Verwendung von `class_type` für das On-Klick, der or klicken-Verhalten**<br>
Wenn eine Nachricht angeklickt wird, bestimmt der `ContentCardClassType`, wie der nächste Bildschirm befüllt werden soll.
```swift
func addContentCardToView(with message: Message) {
    switch message.contentCardData?.contentCardClassType {
      case .message(.fullPage):
        loadContentCardFullPageView(with: message as! FullPageMessage)
      case .message(.webView):
        loadContentCardWebView(with: message as! WebViewMessage)
      default:
        break
    }
}
```
{% endtab %}
{% tab Objective-C %}
**Verwendung von `class_type` für das On-Klick, der or klicken-Verhalten**<br>
Wenn eine Nachricht angeklickt wird, bestimmt der `ContentCardClassType`, wie der nächste Bildschirm befüllt werden soll.
```objc
- (void)addContentCardToView:(Message *)message {
  switch (message.contentCardData.classType) {
    case ContentCardClassTypeMessageFullPage:
      [self loadContentCardFullPageView:(FullPageMessage *)message];
      break;
    case ContentCardClassTypeMessageWebview:
      [self loadContentCardWebView:(WebViewMessage *)message];
      break;
    default:
      break;
  }
}
```
{% endtab %}
{% endtabs %}

##### Bereit, Analytics zu protokollieren?
Besuchen Sie den [folgenden Abschnitt](#logging-impressions-clicks-and-dismissals), um ein besseres Verständnis dafür zu bekommen, wie der Datenfluss aussehen sollte.

![Eine interaktive Content-Card mit einer 50-Prozent-Aktion erscheint in der unteren linken Ecke des Bildschirms. Nach dem Klicken wird die Aktion auf den Warenkorb angewendet.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

### Interaktive Content Cards {#interactive-content-cards}
<br>
Content Cards können verwendet werden, um dynamische und interaktive Erlebnisse für Ihre Nutzer:innen zu schaffen. Im begleitenden Beispiel erscheint ein Content-Card-Pop-up beim Checkout, um Nutzer:innen Last-Minute-Aktionen anzubieten.

Gut platzierte Karten wie diese sind eine hervorragende Möglichkeit, Nutzer:innen einen „Anstoß“ in Richtung bestimmter Aktionen zu geben.
<br><br><br>
#### Dashboard-Konfiguration

Die Dashboard-Konfiguration für interaktive Content Cards ist unkompliziert. Die Schlüssel-Wert-Paare für diesen Anwendungsfall umfassen einen `discount_percentage`, der als gewünschter Rabattbetrag festgelegt wird, und einen `class_type`, der als `coupon_code` gesetzt wird. Diese Schlüssel-Wert-Paare bestimmen, wie typspezifische Content Cards gefiltert und auf dem Checkout-Bildschirm angezeigt werden.

![Interaktive Content-Card mit einer Checkout-Aktion.]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:70%;"}

##### Bereit, Analytics zu protokollieren?
Besuchen Sie den [folgenden Abschnitt](#logging-impressions-clicks-and-dismissals), um ein besseres Verständnis dafür zu bekommen, wie der Datenfluss aussehen sollte.

## Anpassung des Dark Mode {#dark-mode-customization}

Standardmäßig reagieren Content-Card-Ansichten automatisch auf Änderungen des Dark Mode auf dem Gerät mit einem Satz thematisch angepasster Farben.

Dieses Verhalten kann wie in unserem [Leitfaden für angepasste Stile]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/customization/custom_styling#disabling-dark-mode) beschrieben überschrieben werden.

## Impressionen, Klicks und Schließungen protokollieren {#logging-impressions-clicks-and-dismissals}

Nachdem Sie Ihre angepassten Objekte so erweitert haben, dass sie als Content Cards fungieren, können Sie wertvolle Metriken wie Impressionen, Klicks und Schließungen schnell protokollieren. Dies kann über ein `ContentCardable`-Protokoll erfolgen, das auf eine Hilfsdatei verweist und ihr Daten zur Protokollierung durch das Braze SDK or Software-Development-Kit bereitstellt.

### Implementierungskomponenten<br><br> {#implementation-components}

{% tabs %}
{% tab Swift %}
**Analytics protokollieren**<br>
Die Protokollierungsmethoden können direkt von Objekten aufgerufen werden, die dem `ContentCardable`-Protokoll entsprechen.
```swift
customObject.logContentCardImpression()
customObject.logContentCardClicked()
customObject.logContentCardDismissed()
```

**Die `ABKContentCard` abrufen**<br>
Der `idString`, der von Ihrem angepassten Objekt übergeben wird, dient zur Identifizierung der zugehörigen Content Card, um Analytics zu protokollieren.

```swift
extension BrazeManager {
  func logContentCardImpression(idString: String?) {
    guard let contentCard = getContentCard(forString: idString) else { return }

    contentCard.logContentCardImpression()
  }

  private func getContentCard(forString idString: String?) -> ABKContentCard? {
    return contentCards?.first(where: { $0.idString == idString })
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Analytics protokollieren**<br>
Die Protokollierungsmethoden können direkt von Objekten aufgerufen werden, die dem `ContentCardable`-Protokoll entsprechen.
```objc
[customObject logContentCardImpression];
[customObject logContentCardClicked];
[customObject logContentCardDismissed];
```

**Die `ABKContentCard` abrufen**<br>
Der `idString`, der von Ihrem angepassten Objekt übergeben wird, dient zur Identifizierung der zugehörigen Content Card, um Analytics zu protokollieren.

```objc
- (void)logContentCardImpression:(NSString *)idString {
  ABKContentCard *contentCard = [self getContentCard:idString];
  [contentCard logContentCardImpression];
}

- (ABKContentCard *)getContentCard:(NSString *)idString {
  NSPredicate *predicate = [NSPredicate predicateWithFormat:@"self.idString == %@", idString];
  NSArray *filteredArray = [self.contentCards filteredArrayUsingPredicate:predicate];

  return filteredArray.firstObject;
}
```
{% endtab %}
{% endtabs %}

{% alert important %}
Für eine Control-Variante einer Content Card sollte dennoch ein angepasstes Objekt instanziiert und die UI-Logik so eingestellt werden, dass die zugehörige Ansicht des Objekts ausgeblendet wird. Das Objekt kann dann eine Impression protokollieren, um unsere Analytics darüber zu informieren, wann Nutzer:innen die Control Card gesehen hätten.
{% endalert %}

## Hilfsdateien {#helper-files}

{% details ContentCardKey-Hilfsdatei %}
{% tabs %}
{% tab Swift %}
```swift
enum ContentCardKey: String {
  case idString
  case created
  case classType = "class_type"
  case dismissible
  case extras
  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
static NSString *const ContentCardKeyIdString = @"idString";
static NSString *const ContentCardKeyCreated = @"created";
static NSString *const ContentCardKeyClassType = @"class_type";
static NSString *const ContentCardKeyDismissible = @"dismissible";
static NSString *const ContentCardKeyExtras = @"extras";
...
```
{% endtab %}
{% endtabs %}
{% enddetails %}