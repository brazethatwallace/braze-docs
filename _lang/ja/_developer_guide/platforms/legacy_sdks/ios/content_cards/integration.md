---
nav_title: 統合
article_title: iOS 用コンテンツカードビューコントローラーの統合
platform: iOS
page_order: 1
description: "この参考記事では、iOS アプリケーションで使用できる統合手順、データモデル、カード固有のプロパティについて説明します。"
channel:
  - content cards
search_rank: 3
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# コンテンツカード統合 {#content-card-integration}

## コンテンツカードデータモデル {#content-cards-data-model}

コンテンツカードデータモデルはiOS SDKで使用できます。

### データを取得する {#getting-the-data}

コンテンツカードデータモデルにアクセスするには、コンテンツカード更新イベントを購読してください。

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
// Subscribe to Content Cards updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(contentCardsUpdated:)
                                             name:ABKContentCardsProcessedNotification
                                           object:nil];
```

`````````objc
// Called when Content Cards are refreshed (via `requestContentCardsRefresh`)
- (void)contentCardsUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // get the cards using [[Appboy sharedInstance].contentCardsController getContentCards];
  }
}
```
{% endtab %}
{% tab swift %}
`````````swift
// Subscribe to content card updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(contentCardsUpdated),
  name:NSNotification.Name.ABKContentCardsProcessed, object: nil)
```

`````````swift
// Called when the Content Cards are refreshed (via `requestContentCardsRefresh`)
@objc private func contentCardsUpdated(_ notification: Notification) {
  if let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool {
    if (updateIsSuccessful) {
      // get the cards using Appboy.sharedInstance()?.contentCardsController.contentCards
    }
  }
}
```
{% endtab %}
{% endtabs %}

Brazeから送信された後にカードデータを変更したい場合は、カードデータのディープコピーをローカルに保存し、データを更新してから自分で表示することをおすすめします。カードには[`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html)経由でアクセスできます。

## コンテンツカードモデル {#content-card-model}

Brazeには、バナー、キャプション付き画像、クラシックの3種類のContent Cardsが用意されています。各タイプはベース`ABKContentCard`クラスから共通のプロパティを継承し、以下の追加プロパティを持ちます。

### ベースコンテンツカードモデルプロパティ - ABKContentCard {#base-content-card-model-properties-abkcontentcard}

| プロパティ | 説明 |
|---|---|
| `idString` | (読み取り専用) Brazeで設定されたカードのID。 |
| `viewed` | このプロパティは、ユーザーがカードを閲覧したかどうかを反映します。|
| `created` | (読み取り専用) このプロパティは、Brazeからのカードの作成時刻のUNIXタイムスタンプです。 |
| `expiresAt` | (読み取り専用) このプロパティは、カードの有効期限のUNIXタイムスタンプです。|
| `dismissible` | このプロパティは、ユーザーがカードを非表示にできるかどうかを反映します。|
| `pinned` | このプロパティは、カードがダッシュボードで「ピン留め」されているかどうかを反映します。|
| `dismissed` | このプロパティは、ユーザーがカードを非表示にしたかどうかを反映します。|
| `url` | カードをクリックした後に開かれるURL。HTTP(S) URLでもプロトコルURLでもかまいません。|
| `openURLInWebView` | このプロパティは、URLをアプリ内で開くか、外部Webブラウザーで開くかを決定します。|
| `extras`| `NSString`値のオプションの`NSDictionary`。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Base Content Card model properties - ABKContentCard" }

### バナーコンテンツカードのプロパティ - ABKBannerContentCard {#banner-content-card-properties-abkbannercontentcard}

| プロパティ | 説明 |
|---|---|
| `image` | このプロパティはカードの画像のURLです。|
| `imageAspectRatio` | このプロパティはカードの画像の縦横比であり、画像の読み込みが完了する前のヒントとして機能します。ただし、場合によってはプロパティが提供されないことがあります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Banner Content Card properties - ABKBannerContentCard" }

### キャプション付き画像コンテンツカードのプロパティ - ABKCaptionedImageCard {#captioned-image-content-card-properties-abkcaptionedimagecard}

| プロパティ | 説明 |
|---|---|
| `image` | このプロパティはカードの画像のURLです。|
| `imageAspectRatio` | このプロパティはカードの画像の縦横比です。|
| `title` | カードのタイトルテキスト。|
| `cardDescription` | カードの本文テキスト。|
| `domain` | @"blog.braze.com" のようなプロパティURLのリンクテキスト。カードのUIに表示して、カードをクリックしたときのアクション/方向を示すことができます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captioned image Content Card properties - ABKCaptionedImageCard" }

### クラシックコンテンツカードのプロパティ - ABKClassicContentCard {#classic-content-card-properties-abkclassiccontentcard}

| プロパティ | 説明 |
|---|---|
| `image` | (オプション) このプロパティはカードの画像のURLです。|
| `title` | カードのタイトルテキスト。 |
| `cardDescription` | カードの本文テキスト。 |
| `domain` | @"blog.braze.com" のようなプロパティURLのリンクテキスト。カードのUIに表示して、カードをクリックしたときのアクションと方向を示すことができます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classic Content Card properties - ABKClassicContentCard" }

## カードメソッド {#card-methods}

| メソッド | 説明 |
|---|---|
| `logContentCardImpression` | 特定のカードのインプレッションを手動でBrazeに記録します。 |
| `logContentCardClicked` | 特定のカードのクリックを手動でBrazeに記録します。SDKは、カードに有効な値の`url`プロパティがある場合にのみカードクリックを記録します。 |
| `logContentCardDismissed` | 特定のカードの非表示を手動でBrazeに記録します。カードの`dismissed`プロパティがまだ`true`に設定されていない場合にのみ、SDKはカードの非表示を記録します。 |
| `isControlCard` | カードがA/Bテストのコントロールカードであるかどうかを判断します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Card methods" }

詳細については、[クラスリファレンスドキュメント](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html)を参照してください。

## コンテンツカードビューコントローラーの統合 {#content-cards-view-controller-integration}

コンテンツカードは、ナビゲーションまたはモーダルという2つのビューコントローラーコンテキストで統合できます。

### ナビゲーションコンテキスト {#navigation-context}

ナビゲーションコントローラーに`ABKContentCardsTableViewController`インスタンスをプッシュする例:

{% tabs %}
{% tab OBJECTIVE-C %}

`````````objc
ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
contentCards.title = @"Content Cards Title";
contentCards.disableUnreadIndicator = YES;
[self.navigationController pushViewController:contentCards animated:YES];
```

{% endtab %}
{% tab swift %}

`````````swift
let contentCards = ABKContentCardsTableViewController()
contentCards.title = "Content Cards Title"
contentCards.disableUnreadIndicator = true
navigationController?.pushViewController(contentCards, animated: true)
```

{% endtab %}
{% endtabs %}

{% alert note %}
ナビゲーションバーのタイトルをカスタマイズするには、`ABKContentCardsTableViewController`インスタンスの`navigationItem`のタイトルプロパティを設定します。
{% endalert %}

### モーダルコンテキスト {#modal-context}

このモーダルは、ビューコントローラーをモーダルビューに表示するために使用され、上部にナビゲーションバー、バーの横に**Done**ボタンが表示されます。

{% tabs %}
{% tab OBJECTIVE-C %}

`````````objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
contentCards.contentCardsViewController.title = @"Content Cards Title";
contentCards.contentCardsViewController.disableUnreadIndicator = YES;
[self.navigationController presentViewController:contentCards animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

`````````swift
let contentCards = ABKContentCardsViewController()
contentCards.contentCardsViewController.title = "Content Cards Title"
contentCards.contentCardsViewController.disableUnreadIndicator = true
self.present(contentCards, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

ビューコントローラーの例については、[Content Cardsサンプルアプリ](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp)をご覧ください。

{% alert note %}
ヘッダーをカスタマイズするには、親`ABKContentCardsViewController`インスタンスに埋め込まれている`ABKContentCardsTableViewController`インスタンスに属する`navigationItem`のタイトルプロパティを設定します。
{% endalert %}