> Content Cards用のカスタムUIを構築する場合、インプレッション、クリック、非表示といった分析データを手動で記録する必要があります。これらはデフォルトのカードモデルでのみ自動的に処理されるためです。これらのイベントの記録は、コンテンツカード統合の標準的な部分であり、正確なキャンペーンレポートと請求に不可欠です。これを行うには、カスタムUIにBrazeのデータモデルからデータを入力し、その後手動でイベントを記録します。分析の記録方法を理解したら、Brazeの顧客が[カスタムContent Cardsを作成する]({{site.baseurl}}/developer_guide/content_cards/creating_cards)一般的な方法を確認できます。

## 分析のログ記録 {#logging-analytics}

カスタムContent Cardsを実装する際、Content カードオブジェクトを解析し、`title`、`cardDescription`、`imageUrl`などのペイロードデータを抽出できます。その後、取得したモデルデータを使用してカスタムUIに表示できます。

Content カードのデータモデルを取得するには、Content カードの更新を購読します。特に注意すべきプロパティが2つあります。

* **`id`**：Content カードのID文字列を表します。カスタムContent Cardsから分析をログに記録するために使用される一意の識別子です。
* **`extras`**：Brazeダッシュボードからのすべてのキーと値のペアを含みます。

`id`と`extras`以外のすべてのプロパティは、カスタムContent Cardsの解析においてオプションです。データモデルの詳細については、各プラットフォームの統合記事を参照してください：[Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android)、[iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift)、[Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web)。


{% tabs %}
{% tab Web %}

カードが更新されたときに更新を購読するコールバック関数を登録します。

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
Content Cardsは、`openSession()`の前に購読リクエストが呼び出された場合にのみ、セッション開始時に更新されます。いつでも[手動でフィードを更新]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed)することもできます。
{% endalert %}

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

### ステップ1：プライベートサブスクライバー変数を作成する {#step-1-create-a-private-subscriber-variable}

カードの更新を購読するには、まずカスタムクラスでサブスクライバーを保持するプライベート変数を宣言します。

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### ステップ2：更新を購読する {#step-2-subscribe-to-updates}

次に、以下のコードを追加してBrazeからのContent カードの更新を購読します。通常、カスタムContent Cardsアクティビティの`Activity.onCreate()`内に配置します。

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

### ステップ3：購読を解除する {#step-3-unsubscribe}

カスタムアクティビティが画面外に移動する際に購読を解除することも推奨します。アクティビティの`onDestroy()`ライフサイクルメソッドに以下のコードを追加してください。

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### ステップ1：プライベートサブスクライバー変数を作成する

カードの更新を購読するには、まずカスタムクラスでサブスクライバーを保持するプライベート変数を宣言します。

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### ステップ2：更新を購読する

次に、以下のコードを追加してBrazeからのContent カードの更新を購読します。通常、カスタムContent Cardsアクティビティの`Activity.onCreate()`内に配置します。

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
contentCardsUpdatedSubscriber = IEventSubscriber { event ->
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

### ステップ3：購読を解除する

カスタムアクティビティが画面外に移動する際に購読を解除することも推奨します。アクティビティの`onDestroy()`ライフサイクルメソッドに以下のコードを追加してください。

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Swift %}

Content Cardsのデータモデルにアクセスするには、`braze`インスタンスで[`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards)を呼び出します。

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

{% alert note %}
`contentCards.cards`、`contentCards.unviewedCards`、または`contentCards.lastUpdate`を読み取ると、SDKが初期化後の操作を完了するまで呼び出しスレッドがブロックされます。メインスレッドやレイテンシに敏感なコンテキストでは、[ノンブロッキングスナップショットアクセサー](#non-blocking-snapshot-accessors)のノンブロッキングゲッターを使用してください。
{% endalert %}

さらに、Content Cardsの変更を監視するための購読を維持することもできます。以下の2つの方法があります。
1. キャンセル可能オブジェクトを維持する方法
2. `AsyncStream`を維持する方法

### キャンセル可能オブジェクト {#cancellable}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

### ノンブロッキングスナップショットアクセサー {#non-blocking-snapshot-accessors}

これらのメソッドを使用して、呼び出しスレッドをブロックせずに現在のキャッシュ状態を読み取ります。各完了ハンドラーは常にメインスレッドで配信されます。

```swift
// All cached cards.
AppDelegate.braze?.contentCards.getCachedContentCards { cards in
  // Use `cards` here.
}

// Unviewed cards only (excludes control cards).
AppDelegate.braze?.contentCards.getUnviewedCards { cards in
  // Use `cards` here.
}

// Date of the last server sync for the current user (nil until the first sync completes).
AppDelegate.braze?.contentCards.getLastUpdate { date in
  // Use `date` here.
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

さらに、Content Cardsの購読を維持したい場合は、[`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:))を呼び出すことができます。

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

呼び出しスレッドをブロックせずに現在のキャッシュ状態を読み取るには、以下のメソッドを使用します。各完了ハンドラーはメインスレッドで配信されます。

```objc
// All cached cards.
[AppDelegate.braze.contentCards getCachedContentCardsWithCompletion:^(NSArray<BRZContentCardRaw *> *cards) {
  // Use `cards` here.
}];

// Unviewed cards only (excludes control cards).
[AppDelegate.braze.contentCards getUnviewedCardsWithCompletion:^(NSArray<BRZContentCardRaw *> *cards) {
  // Use `cards` here.
}];

// Date of the last server sync for the current user (nil until the first sync completes).
[AppDelegate.braze.contentCards getLastUpdateWithCompletion:^(NSDate * _Nullable date) {
  // Use `date` here.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}

更新をリッスンするには、Content カードの更新イベントを購読します。

```javascript
const subscription = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to log an impression
    } else {
      // Use card.title, card.cardDescription, card.image, etc.
    }
  });
});
```

最新のキャッシュされたContent カードデータを取得するには：

```javascript
import Braze from "@braze/react-native-sdk";

const cachedCards = await Braze.getCachedContentCards();
```

Brazeサーバーからの手動でのContent Cards更新をリクエストするには：

```javascript
Braze.requestContentCardsRefresh();
```

{% endtab %}
{% endtabs %}

## イベントのログ記録 {#logging-events}

インプレッション、クリック、非表示などの重要な指標のログ記録は、迅速かつ簡単に行えます。カスタムクリックリスナーを設定して、これらの分析を手動で処理できます。

{% tabs %}
{% tab web %}

ユーザーがカードを閲覧した際に、[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)を使用してインプレッションイベントをログに記録します。

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

ユーザーがカードを操作した際に、[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)を使用してカードクリックイベントをログに記録します。

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% tab android %}

[`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt)は、Content Cardsオブジェクト配列リストなどのBraze SDKの依存関係を参照して、[`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)を取得し、Brazeのログ記録メソッドを呼び出すことができます。`ContentCardable`基底クラスを使用して、`BrazeManager`にデータを簡単に参照・提供できます。

カードのインプレッションまたはクリックをログに記録するには、それぞれ[`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html)または[`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html)を呼び出します。

特定のカードに対して、Content Cardsを手動でログに記録したり、Brazeに「非表示」として設定したりするには、[`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html)を使用します。カードがすでに非表示としてマークされている場合、再度非表示としてマークすることはできません。

カスタムクリックリスナーを作成するには、[`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html)を実装するクラスを作成し、[`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html)に登録します。ユーザーがContent Cardsをクリックしたときに呼び出される[`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html)メソッドを実装します。次に、BrazeにContent Cardsのクリックリスナーを使用するよう指示します。

{% subtabs local %}
{% subtab Java %}

例:

```java
BrazeContentCardsManager.getInstance().setContentCardsActionListener(new IContentCardsActionListener() {
  @Override
  public boolean onContentCardClicked(Context context, Card card, IAction cardAction) {
    return false;
  }

  @Override
  public void onContentCardDismissed(Context context, Card card) {

  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

例:

```kotlin
BrazeContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
  override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
    return false
  }

  override fun onContentCardDismissed(context: Context, card: Card) {

  }
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
カスタムUIでコントロールバリアントのContent Cardsを処理するには、[`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)オブジェクトを渡し、他のContent Cardsタイプと同様に`logImpression`メソッドを呼び出します。このオブジェクトは、ユーザーがコントロールカードを閲覧したタイミングを分析に通知するために、コントロールインプレッションを暗黙的にログに記録します。{% endalert %}

{% endtab %}

{% tab swift %}

[`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate)プロトコルを実装し、デリゲートオブジェクトを`BrazeContentCardUI.ViewController`の`delegate`プロパティとして設定します。このデリゲートは、カスタムオブジェクトのデータをBrazeに渡してログに記録する処理を行います。例については、[Content Cards UIチュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/)を参照してください。

{% subtabs local %}
{% subtab Swift %}

```swift
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate

// Method to implement in delegate
func contentCard(
    _ controller: BrazeContentCardUI.ViewController,
    shouldProcess clickAction: Braze.ContentCard.ClickAction,
    card: Braze.ContentCard
  ) -> Bool {
  // Intercept the content card click action here.
  return true
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate;

// Method to implement in delegate
- (BOOL)contentCardController:(BRZContentCardUIViewController *)controller
                shouldProcess:(NSURL *)url
                         card:(BRZContentCardRaw *)card {
  // Intercept the content card click action here.
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
カスタムUIでコントロールバリアントのContent Cardsを処理するには、[`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:))オブジェクトを渡し、他のContent Cardsタイプと同様に`logImpression`メソッドを呼び出します。このオブジェクトは、ユーザーがコントロールカードを閲覧したタイミングを分析に通知するために、コントロールインプレッションを暗黙的にログに記録します。
{% endalert %}
{% endtab %}

{% tab react native %}

ユーザーがカードを閲覧した際に、インプレッションイベントをログに記録します。

```javascript
Braze.logContentCardImpression(card.id);
```

ユーザーがカードを操作した際に、カードクリックイベントをログに記録します。

```javascript
Braze.logContentCardClicked(card.id);
```

ユーザーがカードを非表示にした際に、非表示イベントをログに記録します。

```javascript
Braze.logContentCardDismissed(card.id);
```

{% endtab %}
{% endtabs %}

## クリック時の動作の処理 {#handling-on-click-behavior}

{% tabs %}
{% tab web %}

カスタムフィードでユーザーがContent Cardsをクリックした場合、クリック時の動作（URLへの遷移、ディープリンク、カスタムイベントのログ記録など）は自動的には処理されません。[`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction)を使用して、カードのURLを処理し、Brazeアクション（`brazeActions://` URL）を含む設定済みのクリック時アクションを実行します。

```javascript
import * as braze from "@braze/web-sdk";

// In your card click handler
function onCardClick(card) {
  // Log the click
  braze.logContentCardClick(card);

  // Handle the on-click behavior
  if (card.url) {
    braze.handleBrazeAction(card.url);
  }
}
```

| パラメーター | 説明 |
|---|---|
| `url` | 有効なURL、またはスキーム`brazeActions://`を持つ有効なBrazeアクションURL。 |
| `openLinkInNewTab` | （オプション）URLを新しいタブで開くかどうか。デフォルトは`false`です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="クリック時の動作の処理" }

{% alert important %}
`handleBrazeAction()`を呼び出さない場合、Brazeダッシュボードで設定されたクリック時の動作（「カスタムイベントをログに記録」や「URLに遷移」など）は、カスタムフィードに表示されるカードに対して実行されません。
{% endalert %}

{% endtab %}
{% tab android %}

クリック時の動作は、デフォルトのContent Cards UIによって自動的に処理されます。カスタム実装の場合は、**分析のログ記録**で説明されている[`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html)インターフェイスを使用します。

{% endtab %}
{% tab swift %}

クリック時の動作は、デフォルトのContent Cards UIによって自動的に処理されます。カスタム実装の場合は、**分析のログ記録**で説明されている[`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate)プロトコルを使用します。

{% endtab %}
{% tab React Native %}

カスタムフィードでユーザーがContent Cardsをクリックした場合、クリック時の動作は自動的には処理されません。`Braze.logContentCardClicked(cardId)`でクリックをログに記録した後、`Braze.processContentCardClickAction(cardId)`を呼び出して、ディープリンク、URL、および`brazeActions://`アクションを処理します。メソッドリファレンスについては、[React Native Content Cards]({{site.baseurl}}/developer_guide/content_cards/?sdktab=react%20native)を参照してください。

```javascript
import Braze from "@braze/react-native-sdk";

function onCardPress(card) {
  Braze.logContentCardClicked(card.id);

  if (card.url) {
    Braze.processContentCardClickAction(card.id);
  }
}
```

{% alert important %}
`processContentCardClickAction()`を呼び出さない場合、Brazeダッシュボードで設定されたクリック時の動作は、カスタムフィード内のカードに対して実行されません。
{% endalert %}

{% endtab %}
{% endtabs %}