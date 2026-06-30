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
Suchen Sie nach dem grundlegenden Entwicklerleitfaden zur Integration von Content Cards? Finden Sie ihn [hier]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration).
{% endalert %}

# Implementierungsleitfaden für Content Cards {#content-card-implementation-guide}

> Dieser optionale Leitfaden für die erweiterte Implementierung enthält Hinweise zur Code-Anpassung für Content Cards, drei von unserem Team entwickelte angepasste Anwendungsfälle, begleitende Code-Snippets sowie eine Anleitung zur Protokollierung von Impressionen, Klicks und Ausblendungen. Besuchen Sie unser [Braze Demo Repository auf GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Beachten Sie, dass sich dieser Implementierungsleitfaden auf eine Swift-Implementierung konzentriert, aber für Interessierte auch Objective-C-Snippets bereitgestellt werden.

## Hinweise zur Code-Anpassung {#code-considerations}

### Content Cards als angepasste Objekte {#content-cards-as-custom-objects}

Ähnlich wie ein Raketenschiff, das einen Booster hinzufügt, können Ihre eigenen angepassten Objekte erweitert werden, um als Content Cards zu fungieren. Begrenzte API-Oberflächen wie diese bieten die Flexibilität, mit verschiedenen Daten-Backends austauschbar zu arbeiten. Dies kann durch die Konformität mit dem `ContentCardable`-Protokoll und die Implementierung des Initialisierers (wie in den folgenden Code-Snippets zu sehen) erreicht werden. Durch die Verwendung der `ContentCardData`-Struktur können Sie auf die `ABKContentCard`-Daten zugreifen. Die `ABKContentCard`-Payload wird verwendet, um die `ContentCardData`-Struktur und das angepasste Objekt selbst zu initialisieren – alles aus einem `Dictionary`-Typ über den Initialisierer, den das Protokoll mitbringt.

Der Initialisierer enthält auch ein `ContentCardClassType`-enum. Dieses enum wird verwendet, um zu entscheiden, welches Objekt initialisiert werden soll. Durch die Verwendung von Schlüssel-Wert-Paaren im Braze-Dashboard können Sie einen expliziten `class_type`-Schlüssel festlegen, der bestimmt, welches Objekt initialisiert werden soll. Diese Schlüssel-Wert-Paare für Content Cards sind in der Variable `extras` auf der `ABKContentCard` enthalten. Eine weitere zentrale Komponente des Initialisierers ist der Wörterbuchparameter `metaData`. `metaData` enthält alles aus der `ABKContentCard`, aufgeteilt in eine Reihe von Schlüsseln und Werten. Nachdem die relevanten Karten geparst und in Ihre angepassten Objekte umgewandelt wurden, kann die App mit ihnen arbeiten, als ob sie aus JSON oder einer anderen Quelle instanziiert worden wären.

Sobald Sie diese Hinweise zur Code-Anpassung verstanden haben, sehen Sie sich unsere [Anwendungsfälle](#sample-use-cases) an, um mit der Implementierung Ihrer angepassten Objekte zu beginnen.

{% tabs local %}
{% tab ContentCardable %}
{% subtabs global %}
{% subtab Swift %}
**ContentCardable-Protokoll**<br>
Ein `ContentCardData`-Objekt, das die `ABKContentCard`-Daten zusammen mit einem `ContentCardClassType`-enum darstellt. Ein Initialisierer, der zur Instanziierung angepasster Objekte mit `ABKContentCard`-Metadaten verwendet wird.
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
`ContentCardData` stellt die ausgewerteten Werte einer `ABKContentCard` dar.

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
Ein `ContentCardData`-Objekt, das die `ABKContentCard`-Daten zusammen mit einem `ContentCardClassType`-enum darstellt, ein Initialisierer, der zur Instanziierung angepasster Objekte mit `ABKContentCard`-Metadaten verwendet wird.
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
`ContentCardData` stellt die ausgewerteten Werte einer `ABKContentCard` dar.

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
{% tab Custom Objects %}
{% subtabs global %}
{% subtab Swift %}
**Angepasster Objekt-Initialisierer**<br>
Die Metadaten einer `ABKContentCard` werden verwendet, um die Variablen Ihres Objekts zu füllen. Die im Braze-Dashboard eingerichteten Schlüssel-Wert-Paare sind im Wörterbuch „extras“ dargestellt.

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

**Identifizieren von Typen**<br>
Das `ContentCardClassType`-enum stellt den `class_type`-Wert im Braze-Dashboard dar. Dieser Wert wird auch als Filter-Bezeichner verwendet, um Content Cards an verschiedenen Stellen anzuzeigen.

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
**Angepasster Objekt-Initialisierer**<br>
Die Metadaten einer `ABKContentCard` werden verwendet, um die Variablen Ihres Objekts zu füllen. Die im Braze-Dashboard eingerichteten Schlüssel-Wert-Paare sind im Wörterbuch „extras“ dargestellt.


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

**Identifizieren von Typen**<br>
Das `ContentCardClassType`-enum stellt den `class_type`-Wert im Braze-Dashboard dar. Dieser Wert wird auch als Filter-Bezeichner verwendet, um Content Cards an verschiedenen Stellen anzuzeigen.

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

{% tab Handling Content Cards %}
{% subtabs global %}
{% subtab Swift %}
**Content Cards anfordern**<br>
Solange der Beobachter noch im Speicher gehalten wird, kann der Benachrichtigungs-Callback vom Braze SDK erwartet werden.

```swift
func loadContentCards() {
  BrazeManager.shared.addObserverForContentCards(observer: self, selector: #selector(contentCardsUpdated))
  BrazeManager.shared.requestContentCardsRefresh()
}
```

**SDK-Callback für Content Cards verarbeiten**<br>
Leiten Sie den Benachrichtigungs-Callback an die Hilfsdatei weiter, um die Payload-Daten für Ihre angepassten Objekte zu parsen.
```swift
@objc func contentCardsUpdated(_ notification: Notification) {
  guard let contentCards = BrazeManager.shared.handleContentCardsUpdated(notification, for: [.yourValue]) as? [CustomObject],!contentCards.isEmpty else { return }

 // do something with your array of custom objects
}
```

**Mit Content Cards arbeiten**<br>
Der `class_type` wird als Filter übergeben, um nur Content Cards zurückzugeben, die einen passenden `class_type` haben.

```swift
func handleContentCardsUpdated(_ notification: Notification, for classTypes: [ContentCardClassType]) -> [ContentCardable] {
  guard let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool, updateIsSuccessful, let cards = contentCards else { return [] }

  return convertContentCards(cards, for: classTypes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Content Cards anfordern**<br>
Solange der Beobachter noch im Speicher gehalten wird, kann der Benachrichtigungs-Callback vom Braze SDK erwartet werden.

```objc
- (void)loadContentCards {
  [[BrazeManager shared] addObserverForContentCards:self selector:@selector(contentCardsUpdated:)];
  [[BrazeManager shared] requestContentCardsRefresh];
}
```

**SDK-Callback für Content Cards verarbeiten**<br>
Leiten Sie den Benachrichtigungs-Callback an die Hilfsdatei weiter, um die Payload-Daten für Ihre angepassten Objekte zu parsen.
```objc
- (void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeYourValue)];
  NSArray *contentCards = [[BrazeManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes];

  // do something with your array of custom objects
}
```

**Mit Content Cards arbeiten**<br>
Der `class_type` wird als Filter übergeben, um nur Content Cards zurückzugeben, die einen passenden `class_type` haben.

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

{% tab Working with Payload Data %}
{% subtabs global %}
{% subtab Swift %}
**Mit Payload-Daten arbeiten**<br>
Durchläuft das Array der Content Cards in einer Schleife und parst nur die Karten mit einem passenden `class_type`. Die Payload einer ABKContentCard wird in ein `Dictionary` geparst.

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

**Angepasste Objekte aus Content-Card-Payload-Daten initialisieren**<br>
Der `class_type` wird verwendet, um zu bestimmen, welche Ihrer angepassten Objekte aus den Payload-Daten initialisiert werden sollen.

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
Durchläuft das Array der Content Cards in einer Schleife und parst nur die Karten mit einem passenden `class_type`. Die Payload einer ABKContentCard wird in ein `Dictionary` geparst.

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

**Angepasste Objekte aus Content-Card-Payload-Daten initialisieren**<br>
Der `class_type` wird verwendet, um zu bestimmen, welche Ihrer angepassten Objekte aus den Payload-Daten initialisiert werden sollen.

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

## Anwendungsfälle {#sample-use-cases}

Im Folgenden finden Sie drei Anwendungsfälle. Jeder Anwendungsfall enthält eine ausführliche Erklärung, relevante Code-Snippets sowie einen Blick darauf, wie Content-Card-Variablen im Braze-Dashboard aussehen und verwendet werden können:
- [Content Cards als zusätzlicher Inhalt](#content-cards-as-supplemental-content)
- [Content Cards in einer Nachrichtenzentrale](#content-cards-in-a-message-center)
- [Interaktive Content Cards](#interactive-content-cards)

### Content Cards als zusätzlicher Inhalt {#content-cards-as-supplemental-content}

![Feed mit einer hybriden Liste, die lokale Daten und Braze Content Cards kombiniert.]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Sie können Content Cards nahtlos in einen bestehenden Feed einfügen, sodass Daten aus mehreren Feeds gleichzeitig geladen werden können. Dadurch entsteht ein zusammenhängendes, harmonisches Erlebnis mit Braze Content Cards und vorhandenen Feed-Inhalten.

Das Beispiel auf der rechten Seite zeigt eine `UICollectionView` mit einer hybriden Liste von Artikeln, die über lokale Daten und von Braze bereitgestellte Content Cards gefüllt werden. Auf diese Weise können Content Cards nicht von bestehenden Inhalten unterschieden werden.

#### Dashboard-Konfiguration {#dashboard-configuration}

Diese Content Card wird über eine API-getriggerte Campaign mit API-getriggerten Schlüssel-Wert-Paaren zugestellt. Dies ist ideal für Campaigns, bei denen die Werte der Karte von externen Faktoren abhängen, um zu bestimmen, welche Inhalte den Nutzer:innen angezeigt werden sollen. Beachten Sie, dass `class_type` zum Zeitpunkt der Einrichtung bekannt sein sollte.

![Die Schlüssel-Wert-Paare für den Anwendungsfall mit ergänzenden Content Cards. In diesem Beispiel werden verschiedene Aspekte der Karte wie „tile_id“, „tile_deeplink“ und „tile_title“ mit Liquid festgelegt.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

##### Bereit für die Protokollierung von Analytics? {#ready-to-log-analytics}
Im [folgenden Abschnitt](#logging-impressions-clicks-and-dismissals) wird näher beschrieben, wie der Datenfluss aussehen sollte.

### Content Cards in einer Nachrichtenzentrale {#content-cards-in-a-message-center}
<br>
Content Cards können in einem Nachrichtenzentrale-Format verwendet werden, bei dem jede Nachricht eine eigene Karte ist. Jede Nachricht in der Nachrichtenzentrale wird über eine Content-Card-Payload gefüllt, und jede Karte enthält zusätzliche Schlüssel-Wert-Paare für die On-Click-UI/UX. Im folgenden Beispiel verweist eine Nachricht auf eine beliebige angepasste Ansicht, während eine andere eine Webansicht öffnet, die angepasstes HTML anzeigt.

![Content-Card-Nachrichtenzentrale mit einzelnen Nachrichtenkarten.]({% image_buster /assets/img/cc_implementation/message_center.png %}){: style="border:0;"}{: style="max-width:80%;border:0"}

#### Dashboard-Konfiguration

Für die folgenden Nachrichtentypen muss das Schlüssel-Wert-Paar `class_type` zu Ihrer Dashboard-Konfiguration hinzugefügt werden. Die hier zugewiesenen Werte sind willkürlich, sollten aber zwischen den Klassentypen unterscheidbar sein. Diese Schlüssel-Wert-Paare sind die Bezeichner, anhand derer die Anwendung entscheidet, wohin navigiert werden soll, wenn Nutzer:innen auf eine gekürzte Posteingangs-Nachricht klicken.

{% tabs local %}
{% tab Arbitrary custom view message - full page %}

Die Schlüssel-Wert-Paare für diesen Anwendungsfall umfassen:

- `message_header` festgelegt als `Full Page`
- `class_type` festgelegt als `message_full_page`

![Beispiel einer ganzseitigen Content-Card-Nachricht.]({% image_buster /assets/img/cc_implementation/full_page.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Webview message - HTML %}

Die Schlüssel-Wert-Paare für diesen Anwendungsfall umfassen:

- `message_header` festgelegt als `HTML`
- `class_type` festgelegt als `message_webview`
- `message_title`

Diese Nachricht sucht ebenfalls nach einem HTML-Schlüssel-Wert-Paar, aber wenn Sie mit einer Web-Domain arbeiten, ist auch ein URL-Schlüssel-Wert-Paar gültig.

![Content Card, die eine HTML-Webansicht über ein Schlüssel-Wert-Paar öffnet.]({% image_buster /assets/img/cc_implementation/html_webview.png %}){: style="max-width:60%;"}

{% endtab %}
{% endtabs %}

#### Weitere Erklärung {#further-explanation}

Die Logik der Nachrichtenzentrale wird vom `contentCardClassType` gesteuert, der durch die Schlüssel-Wert-Paare von Braze bereitgestellt wird. Mit der Methode `addContentCardToView` können Sie diese Klassentypen sowohl filtern als auch identifizieren.

{% tabs %}
{% tab Swift %}
**Verwendung von `class_type` für On-Click-Verhalten**<br>
Wenn eine Nachricht angeklickt wird, bestimmt `ContentCardClassType`, wie der nächste Bildschirm gefüllt werden soll.
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
**Verwendung von `class_type` für On-Click-Verhalten**<br>
Wenn eine Nachricht angeklickt wird, bestimmt `ContentCardClassType`, wie der nächste Bildschirm gefüllt werden soll.
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

##### Bereit für die Protokollierung von Analytics?
Im [folgenden Abschnitt](#logging-impressions-clicks-and-dismissals) wird näher beschrieben, wie der Datenfluss aussehen sollte.

![Eine interaktive Content Card mit einer 50-Prozent-Rabattaktion erscheint unten links im Bildschirm. Nach dem Klick wird die Aktion auf den Warenkorb angewendet.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

### Interaktive Content Cards {#interactive-content-cards}
<br>
Content Cards können genutzt werden, um dynamische und interaktive Erlebnisse für Ihre Nutzer:innen zu schaffen. Im Beispiel auf der rechten Seite erscheint an der Kasse ein Content-Card-Popup, das den Nutzer:innen Last-Minute-Aktionen bietet.

Gut platzierte Karten wie diese sind eine großartige Möglichkeit, den Nutzer:innen einen „Anstoß“ zu bestimmten Aktionen zu geben.
<br><br><br>
#### Dashboard-Konfiguration

Die Dashboard-Konfiguration für interaktive Content Cards ist unkompliziert. Die Schlüssel-Wert-Paare für diesen Anwendungsfall umfassen einen `discount_percentage`, der als gewünschter Rabattbetrag festgelegt ist, und einen `class_type`, der als `coupon_code` festgelegt ist. Diese Schlüssel-Wert-Paare sorgen dafür, dass typspezifische Content Cards gefiltert und auf dem Checkout-Bildschirm angezeigt werden.

![Interaktive Content Card mit einer Checkout-Aktion.]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:70%;"}

##### Bereit für die Protokollierung von Analytics?
Im [folgenden Abschnitt](#logging-impressions-clicks-and-dismissals) wird näher beschrieben, wie der Datenfluss aussehen sollte.

## Dark-Mode-Anpassung {#dark-mode-customization}

Standardmäßig reagieren die Content-Card-Ansichten automatisch auf Änderungen im Dark Mode auf dem Gerät mit einer Reihe von Themenfarben.

Dieses Verhalten kann wie in unserer [Anleitung für angepasste Stile]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/custom_styling#disabling-dark-mode) beschrieben außer Kraft gesetzt werden.

## Protokollieren von Impressionen, Klicks und Ausblendungen {#logging-impressions-clicks-and-dismissals}

Nachdem Sie Ihre angepassten Objekte so erweitert haben, dass sie als Content Cards fungieren, können Sie wertvolle Metriken wie Impressionen, Klicks und Ausblendungen schnell protokollieren. Dies kann mit Hilfe eines `ContentCardable`-Protokolls geschehen, das auf eine Hilfsdatei verweist und ihr Daten bereitstellt, die vom Braze SDK erfasst werden.

### Komponenten der Implementierung<br><br> {#implementation-components}

{% tabs %}
{% tab Swift %}
**Analytics protokollieren**<br>
Die Protokollierungsmethoden können direkt aus Objekten aufgerufen werden, die dem `ContentCardable`-Protokoll entsprechen.
```swift
customObject.logContentCardImpression()
customObject.logContentCardClicked()
customObject.logContentCardDismissed()
```

**`ABKContentCard` abrufen**<br>
Der von Ihrem angepassten Objekt übergebene `idString` wird verwendet, um die zugehörige Content Card für die Protokollierung von Analytics zu identifizieren.

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
Die Protokollierungsmethoden können direkt aus Objekten aufgerufen werden, die dem `ContentCardable`-Protokoll entsprechen.
```objc
[customObject logContentCardImpression];
[customObject logContentCardClicked];
[customObject logContentCardDismissed];
```

**`ABKContentCard` abrufen**<br>
Der von Ihrem angepassten Objekt übergebene `idString` wird verwendet, um die zugehörige Content Card für die Protokollierung von Analytics zu identifizieren.

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
Für eine Kontrollgruppen-Variante einer Content Card sollte dennoch ein angepasstes Objekt instanziiert werden, und die UI-Logik sollte die entsprechende Ansicht des Objekts als ausgeblendet festlegen. Das Objekt kann dann eine Impression protokollieren, um unsere Analytics darüber zu informieren, wann Nutzer:innen die Kontrollkarte gesehen hätten.
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