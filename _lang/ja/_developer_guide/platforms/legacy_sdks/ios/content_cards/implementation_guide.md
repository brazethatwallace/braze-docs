---
nav_title: 高度な実装（任意）
article_title: iOS 用コンテンツカード実装ガイド（オプション）
platform: iOS
page_order: 7
description: "この高度な実装ガイドでは、iOS コンテンツカードのコードに関する考慮事項、当社チームが構築した3つのユースケース、付随するコードスニペット、およびインプレッション、クリック、却下のロギングに関するガイダンスについて説明します。"
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
基本的なコンテンツカード開発者統合ガイドをお探しですか？[基本的なコンテンツカード開発者統合ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration)をご覧ください。
{% endalert %}

# コンテンツカード実装ガイド {#content-card-implementation-guide}

> このオプションの高度な実装ガイドでは、コンテンツカードのコードに関する考慮事項、当社チームが構築した3つのカスタムユースケース、付随するコードスニペット、およびインプレッション、クリック、却下のロギングに関するガイダンスについて説明します。[こちらから Braze Demo リポジトリ](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)にアクセスしてください！この実装ガイドは Swift の実装を中心としていますが、興味のある方のために Objective-C のスニペットも提供されています。

## コードに関する考慮事項 {#code-considerations}

### カスタムオブジェクトとしてのContent Cards {#content-cards-as-custom-objects}

ブースターを追加するロケット船のように、独自のカスタムオブジェクトを拡張してContent Cardsとして機能させることができます。このような限定された API サーフェスは、異なるデータバックエンドとの互換性を保つ柔軟性を提供します。これは、`ContentCardable` プロトコルに準拠し、（次のコードスニペットに示すように）イニシャライザを実装することで実行できます。また、`ContentCardData` 構造体を使用することで、`ABKContentCard` データにアクセスできます。`ABKContentCard` ペイロードは、すべてプロトコルに付属のイニシャライザを使用して `Dictionary` 型から `ContentCardData` 構造体とカスタムオブジェクト自体を初期化するために使用されます。

イニシャライザには `ContentCardClassType` enum も含まれます。この enum は、初期化するオブジェクトを決定するために使用されます。Braze ダッシュボード内のキーと値のペアを使用して、初期化するオブジェクトを決定するために使用する明示的な `class_type` キーを設定できます。Content Cardsのこれらのキーと値のペアは、`ABKContentCard` の `extras` 変数に格納されます。イニシャライザのもう1つのコアコンポーネントは、`metaData` ディクショナリパラメータです。`metaData` には解析された `ABKContentCard` から一連のキーと値までのすべてが含まれます。関連するカードが解析され、カスタムオブジェクトに変換された後、アプリは JSON またはその他のソースからインスタンス化されたかのように、それらのカードで作業を開始する準備ができています。

これらのコードに関する考慮事項をしっかりと理解したら、[ユースケース](#sample-use-cases)をチェックして、カスタムオブジェクトの実装を開始してください。

{% tabs local %}
{% tab ContentCardable %}
{% subtabs global %}
{% subtab Swift %}
**ContentCardable プロトコル**<br>
`ABKContentCard` データと `ContentCardClassType` enumを表す `ContentCardData` オブジェクトです。`ABKContentCard` メタデータを使用してカスタムオブジェクトをインスタンス化するために使用されるイニシャライザです。
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
**コンテンツカードデータ構造体**<br>
`ContentCardData` は、`ABKContentCard` の解析された値を表します。

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
**ContentCardable プロトコル**<br>
`ABKContentCard` データを `ContentCardClassType` enumと共に表す `ContentCardData` オブジェクトです。`ABKContentCard` メタデータを使用してカスタムオブジェクトをインスタンス化するために使用されるイニシャライザです。
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
**コンテンツカードデータ構造体**<br>
`ContentCardData` は、`ABKContentCard` の解析された値を表します。

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
**カスタムオブジェクトイニシャライザ**<br>
`ABKContentCard` からのメタデータは、オブジェクトの変数を設定するために使用されます。Braze ダッシュボードで設定されたキーと値のペアは、「extras」ディクショナリに格納されます。

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

**タイプの識別**<br>
`ContentCardClassType` enumは、Braze ダッシュボードの `class_type` 値を表します。この値は、Content Cardsを異なる場所に表示するためのフィルター識別子としても使用されます。

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
**カスタムオブジェクトイニシャライザ**<br>
`ABKContentCard` からのメタデータは、オブジェクトの変数を設定するために使用されます。Braze ダッシュボードで設定されたキーと値のペアは、「extras」ディクショナリに格納されます。


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

**タイプの識別**<br>
`ContentCardClassType` enumは、Braze ダッシュボードの `class_type` 値を表します。この値は、Content Cardsを異なる場所に表示するためのフィルター識別子としても使用されます。

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
**Content Cardsのリクエスト**<br>
オブザーバがまだメモリ内に保持されている限り、Braze SDKからの通知コールバックが期待できます。

```swift
func loadContentCards() {
  BrazeManager.shared.addObserverForContentCards(observer: self, selector: #selector(contentCardsUpdated))
  BrazeManager.shared.requestContentCardsRefresh()
}
```

**Content Cards SDKコールバックの処理**<br>
通知コールバックをヘルパーファイルに転送して、カスタムオブジェクトのペイロードデータを解析します。
```swift
@objc func contentCardsUpdated(_ notification: Notification) {
  guard let contentCards = BrazeManager.shared.handleContentCardsUpdated(notification, for: [.yourValue]) as? [CustomObject],!contentCards.isEmpty else { return }

 // do something with your array of custom objects
}
```

**Content Cardsの操作**<br>
`class_type` はフィルターとして渡され、一致する `class_type` を持つContent Cardsのみを返します。

```swift
func handleContentCardsUpdated(_ notification: Notification, for classTypes: [ContentCardClassType]) -> [ContentCardable] {
  guard let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool, updateIsSuccessful, let cards = contentCards else { return [] }

  return convertContentCards(cards, for: classTypes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
**Content Cardsのリクエスト**<br>
オブザーバがまだメモリ内に保持されている限り、Braze SDKからの通知コールバックが期待できます。

```objc
- (void)loadContentCards {
  [[BrazeManager shared] addObserverForContentCards:self selector:@selector(contentCardsUpdated:)];
  [[BrazeManager shared] requestContentCardsRefresh];
}
```

**Content Cards SDKコールバックの処理**<br>
通知コールバックをヘルパーファイルに転送して、カスタムオブジェクトのペイロードデータを解析します。
```objc
- (void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeYourValue)];
  NSArray *contentCards = [[BrazeManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes];

  // do something with your array of custom objects
}
```

**Content Cardsの操作**<br>
`class_type` はフィルターとして渡され、一致する `class_type` を持つContent Cardsのみを返します。

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
**ペイロードデータの操作**<br>
Content Cardsの配列をループし、一致する `class_type` を持つカードのみを解析します。ABKContentCard からのペイロードは `Dictionary` に解析されます。

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

**Content Cardsペイロードデータからのカスタムオブジェクトの初期化**<br>
`class_type` は、ペイロードデータから初期化されるカスタムオブジェクトを決定するために使用されます。

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
**ペイロードデータの操作**<br>
Content Cardsの配列をループし、一致する `class_type` を持つカードのみを解析します。ABKContentCard からのペイロードは `Dictionary` に解析されます。

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

**Content Cardsペイロードデータからのカスタムオブジェクトの初期化**<br>
`class_type` は、ペイロードデータから初期化されるカスタムオブジェクトを決定するために使用されます。

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

## ユースケース {#sample-use-cases}

以下に3つのユースケースを紹介します。各ユースケースでは、詳細な説明、関連するコードスニペット、およびContent Cardsの変数がBrazeダッシュボードでどのように表示され、どのように使用されるかを確認できます。
- [補足コンテンツとしてのContent Cards](#content-cards-as-supplemental-content)
- [メッセージセンターのContent Cards](#content-cards-in-a-message-center)
- [インタラクティブContent Cards](#interactive-content-cards)

### 補足コンテンツとしてのContent Cards {#content-cards-as-supplemental-content}

![ローカルデータとBraze Content Cardsを組み合わせたハイブリッドリストを含むフィード。]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Content Cardsを既存のフィードにシームレスにブレンドし、複数のフィードからのデータを同時に読み込むことができます。これにより、Braze Content Cardsと既存のフィードコンテンツとの一体感のある、調和のとれた体験が生まれます。

右の例は、ローカルデータとBrazeを使用したContent Cardsによって設定された項目のハイブリッドリストを含む `UICollectionView` を示しています。これにより、既存のコンテンツとContent Cardsを区別できなくなります。

#### ダッシュボード設定 {#dashboard-configuration}

このContent Cardsは、APIトリガーのキーと値のペアを持つAPIトリガーキャンペーンによって提供されます。これは、カードの値が外部要因に依存して、ユーザーに表示するコンテンツを決定するキャンペーンに最適です。なお、`class_type` はセットアップ時に把握しておく必要があります。

![補足コンテンツカードのユースケースのキーと値のペア。この例では、カードの各要素（「tile_id」、「tile_deeplink」、「tile_title」など）がLiquidを使って設定されています。]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

##### 分析をログに記録する準備はできましたか？ {#ready-to-log-analytics}
データフローの外観について理解を深めるには、[以下のセクション](#logging-impressions-clicks-and-dismissals)を参照してください。

### メッセージセンターのContent Cards {#content-cards-in-a-message-center}
<br>
Content Cardsは、各メッセージが独自のカードであるメッセージセンター形式で使用できます。メッセージセンター内の各メッセージは、Content Cardsペイロードを介して設定され、各カードには、クリック時のUI/UXを起動する追加のキーと値のペアが含まれています。次の例では、1つのメッセージによって任意のカスタムビューが表示され、別のメッセージによってカスタムHTMLを表示するWebビューが開きます。

![個別のメッセージカードを含むContent Cardsメッセージセンター。]({% image_buster /assets/img/cc_implementation/message_center.png %}){: style="border:0;"}{: style="max-width:80%;border:0"}

#### ダッシュボード設定

次のメッセージタイプでは、キーと値のペア `class_type` をダッシュボード設定に追加する必要があります。ここで割り当てる値は任意ですが、クラス型を区別できるようにする必要があります。これらのキーと値のペアは、ユーザーが簡略化された受信トレイメッセージをクリックした際に行き先を決定するときにアプリケーションが参照するキー識別子です。

{% tabs local %}
{% tab 任意のカスタムビューメッセージ - フルページ %}

このユースケースのキーと値のペアは、次のとおりです。

- `message_header` を `Full Page` に設定
- `class_type` を `message_full_page` に設定

![フルページのContent Cardsメッセージの例。]({% image_buster /assets/img/cc_implementation/full_page.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Webビューメッセージ - HTML %}

このユースケースのキーと値のペアは、次のとおりです。

- `message_header` を `HTML` に設定
- `class_type` を `message_webview` に設定
- `message_title`

このメッセージはHTMLキーと値のペアも検索しますが、Webドメインで作業している場合は、URLキーと値のペアも有効です。

![キーと値のペアからHTML Webビューを開くContent Card。]({% image_buster /assets/img/cc_implementation/html_webview.png %}){: style="max-width:60%;"}

{% endtab %}
{% endtabs %}

#### 詳細説明 {#further-explanation}

メッセージセンターのロジックは、Brazeのキーと値のペアによって提供される `contentCardClassType` によって駆動されます。`addContentCardToView` メソッドを使用すると、これらのクラス型をフィルタリングして識別することができます。

{% tabs %}
{% tab Swift %}
**クリック時の動作に `class_type` を使用する**<br>
メッセージをクリックすると、`ContentCardClassType` が次の画面の表示方法を制御します。
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
**クリック時の動作に `class_type` を使用する**<br>
メッセージをクリックすると、`ContentCardClassType` が次の画面の表示方法を制御します。
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

##### 分析をログに記録する準備はできましたか？
データフローの外観について理解を深めるには、[以下のセクション](#logging-impressions-clicks-and-dismissals)を参照してください。

![画面左下に50%のプロモーションを示すインタラクティブなContent Cardが表示されている。クリックすると、カートにプロモーションが適用されます。]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

### インタラクティブContent Cards {#interactive-content-cards}
<br>
Content Cardsを活用して、ユーザーのためのダイナミックでインタラクティブな体験を作成できます。右の例では、Content Cardsのポップアップがチェックアウト時に表示され、ユーザーに最新のプロモーションを提供しています。

このように適切に配置されたカードは、ユーザーが特定のアクションを実行するように「後押し」する優れた方法です。
<br><br><br>
#### ダッシュボード設定

インタラクティブContent Cardsのダッシュボード設定は簡単です。このユースケースのキーと値のペアには、希望する割引額として設定された `discount_percentage` と、`coupon_code` として設定された `class_type` があります。これらのキーと値のペアは、タイプ固有のContent Cardsがどのようにフィルタリングされ、チェックアウト画面に表示されるかを決定します。

![チェックアウトプロモーションを表示するインタラクティブContent Card。]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:70%;"}

##### 分析をログに記録する準備はできましたか？
データフローの外観について理解を深めるには、[以下のセクション](#logging-impressions-clicks-and-dismissals)を参照してください。

## ダークモードのカスタマイズ {#dark-mode-customization}

デフォルトでは、Content Cardsビューは、テーマカラーのセットでデバイスのダークモードの変更に自動的に応答します。

この動作は、[カスタムスタイルガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/custom_styling#disabling-dark-mode)で詳細に説明されているようにオーバーライドできます。

## インプレッション、クリック、却下のロギング {#logging-impressions-clicks-and-dismissals}

カスタムオブジェクトをContent Cardsとして機能するように拡張した後は、インプレッション、クリック、却下などの貴重な指標のロギングを迅速に行えます。これは、`ContentCardable` プロトコルを使用して実行できます。このプロトコルは、Braze SDKによってロギングされるヘルパーファイルを参照し、データを提供します。

### 実装コンポーネント<br><br> {#implementation-components}

{% tabs %}
{% tab Swift %}
**分析のロギング**<br>
ロギングメソッドは、`ContentCardable` プロトコルに準拠するオブジェクトから直接呼び出すことができます。
```swift
customObject.logContentCardImpression()
customObject.logContentCardClicked()
customObject.logContentCardDismissed()
```

**`ABKContentCard` の取得**<br>
カスタムオブジェクトから渡された `idString` は、関連付けられたContent Cardを識別して分析をログに記録するために使用されます。

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
**分析のロギング**<br>
ロギングメソッドは、`ContentCardable` プロトコルに準拠するオブジェクトから直接呼び出すことができます。
```objc
[customObject logContentCardImpression];
[customObject logContentCardClicked];
[customObject logContentCardDismissed];
```

**`ABKContentCard` の取得**<br>
カスタムオブジェクトから渡された `idString` は、関連付けられたContent Cardを識別して分析をログに記録するために使用されます。

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
コントロールバリアントのContent Cardの場合、カスタムオブジェクトは引き続きインスタンス化し、UIロジックでオブジェクトの対応するビューを非表示に設定する必要があります。その後、オブジェクトはインプレッションをログに記録して、ユーザーがいつコントロールカードを表示したかを分析に知らせることができます。
{% endalert %}

## ヘルパーファイル {#helper-files}

{% details ContentCardKey ヘルパーファイル %}
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