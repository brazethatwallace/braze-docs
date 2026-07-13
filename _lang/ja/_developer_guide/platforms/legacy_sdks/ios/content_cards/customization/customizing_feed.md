---
nav_title: フィードをカスタマイズする
article_title: iOSのContent Cardsフィードをカスタマイズする
platform: iOS
page_order: 2
description: "この記事では、iOSアプリケーションのContent Cardsフィードのカスタマイズオプションについて説明します。"
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Content Cardsのフィードをカスタマイズする {#customize-the-content-cards-feed}

`ABKContentCardsTableViewController` を拡張してすべてのUI要素とContent Cardsの動作をカスタマイズすることで、独自のContent Cardsインターフェイスを作成できます。Content Cardsセルをサブクラス化してからプログラムで使用することも、新しいクラスを登録するカスタムストーリーボードを導入することによって使用することもできます。完全な例については、Content Cardsの[サンプルアプリ](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp)をご確認ください。

また、サブクラス化戦略を使用すべきか、完全にカスタムのビューコントローラーを使用して[データ更新を配信登録]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration)すべきかを検討することも重要です。たとえば、`ABKContentCardsTableViewController` をサブクラス化する場合は、[`populateContentCards` メソッド](#overriding-populated-content-cards)を使用してカードのフィルター処理と順序付けを行うことができます（推奨）。ただし、ビューコントローラーを完全にカスタマイズすると、カルーセルでの表示やインタラクティブ要素の追加など、カードの動作をより詳細に制御できるようになりますが、順序付けとフィルター処理のロジックを実装するためにオブザーバーに頼らなければなりません。また、インプレッション、却下イベント、クリックを適切に記録するには、それぞれの分析メソッドを実装する必要もあります。

## UIをカスタマイズする {#customizing-ui}

次のコードスニペットは、SDKが提供するメソッドを使用して、UIのニーズに合わせてContent Cardsのスタイル設定と変更を行う方法を示しています。これらのメソッドによって、カスタムフォント、カスタマイズされたカラーコンポーネント、カスタマイズされたテキストなど、Content Cards UIのあらゆる側面をカスタマイズすることができます。

Content Cards UIをカスタマイズする方法は2通りあります。
- ダイナミックメソッド: カードごとにカードUIを更新する
- スタティックメソッド: すべてのカードでUIを更新する

### ダイナミックUI {#dynamic-ui}

Content Cardsの `applyCard` メソッドはカードオブジェクトを参照し、UIの更新に使用されるキーと値のペアを渡すことができます。

{% tabs %}
{% tab Objective-C %}
```objc
- (void)applyCard:(ABKCaptionedImageContentCard *)captionedImageCard {
  [super applyCard:captionedImageCard];

  if ([card.extras objectForKey:ContentCardKeyBackgroundColorValue]) {
    NSString *backgroundColor = [card.extras objectForKey:ContentCardKeyBackgroundColor];
    if ([backgroundColor colorValue]) {
      self.rootView.backgroundColor = [backgroundColor colorValue];
    } else {
      self.rootView.backgroundColor = [UIColor lightGray];
    }
  } else {
    self.rootView.backgroundColor = [UIColor lightGray];
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
override func apply(_ captionedImageCard: ABKCaptionedImageContentCard!) {
  super.apply(captionedImageCard)

  if let backgroundColor = card.extras?[ContentCardKey.backgroundColor.rawValue] as? String,
     let backgroundColorValue = backgroundColor.colorValue() {
    rootView.backgroundColor = backgroundColorValue
  } else {
    rootView.backgroundColor = .lightGray
  }
}
```
{% endtab %}
{% endtabs %}

### スタティックUI {#static-ui}

`setUpUI` メソッドは、すべてのカードで静的なContent Cardsコンポーネントに値を割り当てることができます。

{% tabs %}
{% tab Objective-C %}
```objc
#import "CustomClassicContentCardCell.h"

@implementation CustomClassicContentCardCell

- (void)setUpUI {
  [super setUpUI];
  self.rootView.backgroundColor = [UIColor lightGrayColor];
  self.rootView.layer.borderColor = [UIColor purpleColor].CGColor;
  self.unviewedLineView.backgroundColor = [UIColor redColor];
  self.titleLabel.font = [UIFont italicSystemFontOfSize:20];
}
```
{% endtab %}
{% tab Swift %}
```swift
override func setUpUI() {
  super.setUpUI()

  rootView.backgroundColor = .lightGray
  rootView.layer.borderColor = UIColor.purple.cgColor
  unviewedLineViewColor = .red
  titleLabel.font = .italicSystemFont(ofSize: 20)
}
```
{% endtab %}
{% endtabs %}

## カスタムインターフェイスを提供する {#providing-custom-interfaces}

カスタムインターフェイスを提供するには、必要なカードタイプごとにカスタムクラスを登録します。

![バナーContent Card。バナーのContent Cardには、バナーの右側に画像が表示され、「Thanks for downloading Braze Demo!」というテキストが添えられている。]({% image_buster /assets/img/interface1.png %}){: style="max-width:35%;margin-left:15px;"}
![キャプション付き画像Content Card。キャプション付きのContent Cardには、Brazeの画像が表示され、その下部に「Thanks for downloading Braze Demo!」というキャプションが重ねて表示されている。]({% image_buster /assets/img/interface2.png %}){: style="max-width:25%;margin-left:15px;"}
![クラシックContent Card。クラシックなContent Cardは、カードの中央に画像を表示し、その下に「Thanks for downloading Braze Demo」という文字が表示される。]({% image_buster /assets/img/interface3.png %}){: style="max-width:18%;margin-left:15px;"}

Brazeには、3つのContent Cardsテンプレート（バナー、キャプション付き画像、クラシック）が用意されています。独自のカスタムインターフェイスを提供する場合は、次のコードスニペットを参照してください。

{% tabs %}
{% tab Objective-C %}
```objc
- (void)registerTableViewCellClasses {
  [super registerTableViewCellClasses];

  // Replace the default class registrations with custom classes for these two types of cards
  [self.tableView registerClass:[CustomCaptionedImageContentCardCell class] forCellReuseIdentifier:@"ABKCaptionedImageContentCardCell"];
  [self.tableView registerClass:[CustomClassicContentCardCell class] forCellReuseIdentifier:@"ABKClassicCardCell"];
}
```
{% endtab %}
{% tab Swift %}
```swift
override func registerTableViewCellClasses() {
  super.registerTableViewCellClasses()

  // Replace the default class registrations with custom classes
  tableView.register(CustomCaptionedImageContentCardCell.self, forCellReuseIdentifier: "ABKCaptionedImageContentCardCell")
  tableView.register(CustomBannerContentCardCell.self, forCellReuseIdentifier: "ABKBannerContentCardCell")
  tableView.register(CustomClassicImageContentCardCell.self, forCellReuseIdentifier: "ABKClassicImageCardCell")
  tableView.register(CustomClassicContentCardCell.self, forCellReuseIdentifier: "ABKClassicCardCell")
}
```
{% endtab %}
{% endtabs %}

## 値が挿入されたContent Cardsをオーバーライドする {#overriding-populated-content-cards}

Content Cardsをプログラムで変更するには、`populateContentCards` メソッドを使用します。

{% tabs %}
{% tab Objective-C %}
```objc
- (void)populateContentCards {
  NSMutableArray<ABKContentCard *> *cards = [NSMutableArray arrayWithArray:[Appboy.sharedInstance.contentCardsController getContentCards]];
  for (ABKContentCard *card in cards) {
    // Replaces the card description for all Classic Content Cards
    if ([card isKindOfClass:[ABKClassicContentCard class]]) {
      ((ABKClassicContentCard *)card).cardDescription = @"Custom Feed Override title [classic cards only]!";
    }
  }
  super.cards = cards;
}
```
{% endtab %}
{% tab Swift %}
```swift
override func populateContentCards() {
  guard let cards = Appboy.sharedInstance()?.contentCardsController.contentCards else { return }
  for card in cards {
    // Replaces the card description for all Classic Content Cards
    if let classicCard = card as? ABKClassicContentCard {
      classicCard.cardDescription = "Custom Feed Override title [classic cards only]!"
    }
  }
  super.cards = (cards as NSArray).mutableCopy() as? NSMutableArray
}
```
{% endtab %}
{% endtabs %}