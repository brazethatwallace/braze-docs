---
nav_title: カードを作成する
article_title: コンテンツカードを作成する
page_order: 0
description: "この記事では、カスタムコンテンツカード UI を作成するコンポーネントについて説明します。"
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# コンテンツカードを作成する {#create-content-cards}

> この記事では、カスタムコンテンツカードを実装するときに使用する基本的なアプローチと、3つの一般的なユースケースについて説明します。Content Cardsカスタマイズガイドの他の記事をすでに読んで、デフォルトでできることとカスタムコードが必要なことを理解していることを前提としています。特に、カスタムコンテンツカードの[分析を記録]({{site.baseurl}}/developer_guide/content_cards/logging_analytics)する方法を理解しておくと役立ちます。

{% multi_lang_include banners/content_card_alert.md %}

## カードの作成 {#creating-a-card}

### ステップ1:カスタムUIを作成する {#step-1-create-a-custom-ui}

{% tabs local %}
{% tab web %}

まず、カードのレンダリングに使用するカスタムHTMLコンポーネントを作成します。

{% endtab %}
{% tab android %}

まず、独自のカスタムフラグメントを作成します。デフォルトの[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)はデフォルトのContent Cardsタイプのみを処理するように設計されていますが、出発点として適しています。

{% endtab %}
{% tab swift %}

まず、独自のカスタムビューコントローラーコンポーネントを作成します。デフォルトの[`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller)はデフォルトのContent Cardsタイプのみを処理するように設計されていますが、出発点として適しています。

{% endtab %}
{% endtabs %}

### ステップ2:カードの更新をサブスクライブする {#step-2-subscribe-to-card-updates}

カードが更新されたときにデータの更新をサブスクライブするコールバック関数を登録します。Content Cardsオブジェクトを解析し、`title`、`cardDescription`、`imageUrl`などのペイロードデータを抽出してから、結果のモデルデータを使用してカスタムUIを生成できます。

Content Cardsのデータモデルを取得するには、Content Cardsの更新をサブスクライブします。特に以下のプロパティに注意してください。

* **`id`：** Content CardsのID文字列を表します。カスタムContent Cardsから分析をログに記録するために使用される一意の識別子です。
* **`extras`：** Brazeダッシュボードからのすべてのキーと値のペアを含みます。

`id`と`extras`以外のすべてのプロパティは、カスタムContent Cardsの解析ではオプションです。データモデルの詳細については、各プラットフォームの統合記事を参照してください：[Android]({{site.baseurl}}/developer_guide/content_cards?sdktab=android)、[iOS]({{site.baseurl}}/developer_guide/content_cards?sdktab=swift)、[Web]({{site.baseurl}}/developer_guide/content_cards?sdktab=web)。

{% tabs local %}
{% tab web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
// For example:
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to call `logContentCardImpressions([card])`
    }
    else if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      // Use `card.title`, `card.imageUrl`, etc.
    }
    else if (card instanceof braze.ImageOnly) {
      // Use `card.imageUrl`, etc.
    }
  })
});

braze.openSession();
```

{% alert note %}
Content Cardsは、`subscribeToContentCardsUpdates()`が`openSession()`の前に呼び出された場合にのみ、セッション開始時に更新されます。いつでも[フィードを手動で更新する]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed)こともできます。
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

#### ステップ2a:プライベートサブスクライバー変数を作成する {#step-2a-create-a-private-subscriber-variable}

カードの更新をサブスクライブするには、まずカスタムクラスでサブスクライバーを保持するプライベート変数を宣言します。

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

#### ステップ2b:更新をサブスクライブする {#step-2b-subscribe-to-updates}

以下のコードを追加して、BrazeからのContent Cardsの更新をサブスクライブします。通常、カスタムContent Cardsアクティビティの`Activity.onCreate()`内に配置します。

```java
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // List of all Content Cards
        List<Card> allCards = event.getAllCards();

        // Your logic below
    }
};
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh();
```

#### ステップ2c:サブスクライブを解除する {#step-2c-unsubscribe}

カスタムアクティビティがビューから移動するときにサブスクライブを解除します。アクティビティの`onDestroy()`ライフサイクルメソッドに以下のコードを追加します。

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

#### ステップ2a:プライベートサブスクライバー変数を作成する

カードの更新をサブスクライブするには、まずカスタムクラスでサブスクライバーを保持するプライベート変数を宣言します。

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

#### ステップ2b:更新をサブスクライブする

以下のコードを追加して、BrazeからのContent Cardsの更新をサブスクライブします。通常、カスタムContent Cardsアクティビティの`Activity.onCreate()`内に配置します。

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh()
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

#### ステップ2c:サブスクライブを解除する

カスタムアクティビティがビューから移動するときにサブスクライブを解除します。アクティビティの`onDestroy()`ライフサイクルメソッドに以下のコードを追加します。

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Content Cardsのデータモデルにアクセスするには、`braze`インスタンスで[`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards)を呼び出します。

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

さらに、Content Cardsの変更を監視するためのサブスクリプションを維持できます。これには2つの方法があります。
1. キャンセル可能なオブジェクトを維持する方法、または
2. `AsyncStream`を維持する方法。

##### キャンセル可能なオブジェクト {#cancellable}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

##### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

さらに、Content Cardsのサブスクリプションを維持したい場合は、[`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:))を呼び出すことができます。

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}


### ステップ3:分析を実装する {#step-3-implement-analytics}

Content Cardsのインプレッション、クリック、および却下は、カスタムビューでは自動的にログに記録されません。すべてのメトリクスをBrazeダッシュボードの分析に適切にログ記録するために、[それぞれのメソッドを実装する]({{site.baseurl}}/developer_guide/content_cards/logging_analytics)必要があります。

### ステップ4:カードをテストする（オプション） {#step-4-test-your-card-optional}

Content Cardsをテストするには、以下の手順に従います。

1. [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)メソッドを呼び出して、アプリケーションにアクティブユーザーを設定します。
2. Brazeで**キャンペーン**に移動し、[新しいContent Cardsキャンペーンを作成]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card)します。
3. キャンペーンで**テスト**を選択し、テストユーザーの`user-id`を入力します。準備ができたら、**テストを送信**を選択します。まもなくデバイスでContent Cardsを起動できます。

![テスト受信者として独自のユーザーIDを追加してContent Cardsをテストできることを示すBraze Content Cardsキャンペーン。]({% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test")

## Content カードの配置 {#content-card-placements}

Content Cardsはさまざまな方法で使用できます。一般的な実装として、メッセージセンター、ダイナミック画像広告、画像カルーセルの3つがあります。これらの配置それぞれで、Content Cardsに[キーと値のペア]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior)（データモデルの`extras`プロパティ）を割り当て、その値に基づいてランタイム時にカードの動作、外観、機能をダイナミックに調整します。

![メッセージ受信トレイ、ダイナミック画像広告、画像カルーセルの3つのContent カード配置例を示す図。]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### メッセージ受信トレイ {#message-inbox}

Content Cardsはメッセージセンターをシミュレートするために使用できます。この形式では、各メッセージがそれぞれのカードとなり、クリック時のイベントを制御する[キーと値のペア]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior)を含んでいます。これらのキーと値のペアは、ユーザーが受信トレイのメッセージをクリックしたときに遷移先を決定するためにアプリケーションが参照するキー識別子です。キーと値のペアの値は任意です。

#### 例 {#example}

たとえば、おすすめ記事を有効にするための行動喚起カードと、新規購読者セグメント向けのクーポンコードカードの2つのメッセージカードを作成したい場合を考えます。

`body`、`title`、`buttonText`のようなキーには、マーケターが設定できるシンプルな文字列値を持たせることができます。`terms`のようなキーには、法務部門が承認したフレーズの小さなコレクションを提供する値を持たせることができます。`style`や`class_type`のようなキーには、カードがアプリやサイトでどのようにレンダリングされるかを決定する文字列値を設定できます。

{% tabs local %}
{% tab おすすめ記事 %}
おすすめ記事カードのキーと値のペア：

| キー | 値 |
|------------|----------------------------------------------------------------------|
| `body`       | Add your interests to your Politer Weekly profile for personal reading recommendations. |
| `style`      | info                                                                 |
| `class_type` | notification_center                                                 |
| `card_priority` | 1                                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="例" }
{% endtab %}

{% tab 新規購読者クーポン %}
新規購読者クーポンのキーと値のペア：

| キー | 値 |
|------------|------------------------------------------------------------------|
| `title`      | Subscribe for unlimited games                                    |
| `body`       | End of Summer Special - Enjoy 10% off Politer games              |
| `buttonText` | Subscribe Now                                                    |
| `style`      | promo                                                            |
| `class_type` | notification_center                                              |
| `card_priority` | 2                                                              |
| `terms`      | new_subscribers_only                                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="例" }
{% endtab %}
{% endtabs %}

{% details Androidの追加情報 %}

AndroidおよびFireOS SDKでは、メッセージセンターのロジックは、Brazeのキーと値のペアから提供される`class_type`の値によって制御されます。[`createContentCardable`]({{site.baseurl}}/developer_guide/content_cards)メソッドを使用して、これらのクラスタイプをフィルタリングおよび識別できます。

{% tabs local %}
{% tab Kotlin %}
**クリック時の動作に`class_type`を使用する**<br>
Content Cardsのデータをカスタムクラスに展開する際、データの`ContentCardClass`プロパティを使用して、データを格納するために使用する具体的なサブクラスを決定します。

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.NOTIFICATION_CENTER -> FullPageMessage(metadata)
            ContentCardClass.ITEM_GROUP -> Group(metadata)
            ContentCardClass.ITEM_TILE -> Tile(metadata)
            ContentCardClass.COUPON -> Coupon(metadata)
            else -> null
        }
    }
```

次に、メッセージリストに対するユーザーのインタラクションを処理する際、メッセージのタイプを使用してユーザーに表示するビューを決定できます。

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
        listView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, WebViewActivity::class.java)
                    val bundle = Bundle()
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
                is FullPageMessage -> {
                    val intent = Intent(this, FullPageContentCard::class.java)
                    val bundle = Bundle()
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.icon)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.messageTitle)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        }
    }
```
{% endtab %}
{% tab Java %}
**クリック時の動作に`class_type`を使用する**<br>
Content Cardsのデータをカスタムクラスに展開する際、データの`ContentCardClass`プロパティを使用して、データを格納するために使用する具体的なサブクラスを決定します。

```java
private ContentCardable createContentCardable(Map<String, ?> metadata,  ContentCardClass type){
    switch(type){
        case ContentCardClass.AD:{
            return new Ad(metadata);
        }
        case ContentCardClass.MESSAGE_WEB_VIEW:{
            return new WebViewMessage(metadata);
        }
        case ContentCardClass.NOTIFICATION_CENTER:{
            return new FullPageMessage(metadata);
        }
        case ContentCardClass.ITEM_GROUP:{
            return new Group(metadata);
        }
        case ContentCardClass.ITEM_TILE:{
            return new Tile(metadata);
        }
        case ContentCardClass.COUPON:{
            return new Coupon(metadata);
        }
        default:{
            return null;
        }
    }
}

```

次に、メッセージリストに対するユーザーのインタラクションを処理する際、メッセージのタイプを使用してユーザーに表示するビューを決定できます。

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
               ContentCardable card = dataProvider.get(position);
               if (card instanceof WebViewMessage){
                    Bundle intent = new Intent(this, WebViewActivity.class);
                    Bundle bundle = new Bundle();
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intent.putExtras(bundle);
                    startActivity(intent);
                }
                else if (card instanceof FullPageMessage){
                    Intent intent = new Intent(this, FullPageContentCard.class);
                    Bundle bundle = Bundle();
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.getIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.getMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.getCardDescription());
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        });
    }
```

{% endtab %}
{% endtabs %}
{% enddetails %}

### カルーセル {#carousel}

完全にカスタムされたカルーセルフィードにContent Cardsを設定し、ユーザーがスワイプして追加のおすすめカードを表示できるようにすることができます。デフォルトでは、Content Cardsは作成日順（最新のものが最初）にソートされ、ユーザーは対象となるすべてのカードを表示できます。

Content Cardsカルーセルを実装するには：

1. [Content Cardsの変更]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed)を監視し、Content Cardsの到着を処理するカスタムロジックを作成します。
2. カルーセルに一度に表示するカードの特定数を決定するカスタムクライアントサイドロジックを作成します。たとえば、配列から最初の5つのContent カードオブジェクトを選択したり、キーと値のペアを導入して条件ロジックを構築したりできます。

{% alert tip %}
カルーセルをセカンダリのContent Cardsフィードとして実装する場合は、[キーと値のペアを使用してカードを正しいフィードにソート]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed)してください。
{% endalert %}

### 画像のみ {#image-only}

Content Cardsは必ずしも「カード」のような外観である必要はありません。たとえば、Content Cardsはホームページや指定されたページの上部に永続的に表示されるダイナミック画像として表示できます。

これを実現するには、マーケターが**画像のみ**タイプのContent Cardsを使用してキャンペーンまたはキャンバスステップを作成します。次に、[Content Cardsを補足コンテンツとして使用する]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior)のに適切なキーと値のペアを設定します。