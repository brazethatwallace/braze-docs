---
nav_title: デフォルトフィード
article_title: Content Cards用のフィードをカスタマイズする
page_order: 3
description: "この記事では、Content Cardsフィードのカスタマイズオプションについて説明します。"
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Content Cards用のフィードをカスタマイズする {#customize-the-feed-for-content-cards}

> Content Cardsフィードは、モバイルまたはWebアプリケーションにおける一連のContent Cardsです。この記事では、フィードの更新タイミングの設定、カードの順序、複数フィードの管理、「空のフィード」エラーメッセージについて説明します。コンテンツカードタイプの完全なリストについては、[Content Cardsについて]({{site.baseurl}}/developer_guide/content_cards)を参照してください。

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## フィードの更新 {#refreshing-the-feed}

### 自動リフレッシュ {#automatic-refresh}

デフォルトでは、次の場合にContent Cardsフィードが自動的に更新されます。

- 新しいセッションが開始された場合
- デフォルトのContent Cardsフィードが閉じられ、最後の更新から60秒以上経過した後に再度開かれた場合

{% alert tip %}
手動で更新せずに最新のContent Cardsをダイナミックに表示するには、カード作成時に**最初のインプレッション発生時**を選択します。これらのカードは、利用可能になると更新されます。
{% endalert %}

### 手動更新 {#manual-refresh}

特定のタイミングでフィードを手動で更新するには:

{% tabs %}
{% tab web %}

Web SDKから[`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh)を呼び出して、いつでも手動でBraze Content Cardsのリフレッシュをリクエストできます。

また、[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)を呼び出して、最新のContent Cards更新から現在利用可能なすべてのカードを取得することもできます。

```javascript
import * as braze from "@braze/web-sdk";

function refresh() {
  braze.requestContentCardsRefresh();
}
```

Content Cardsのリンクを同じタブではなく新しいブラウザタブで開くには、Web SDKの初期化オプションで`openCardsInNewTab: true`を設定します。初期化オプションの詳細については、[Web SDKリポジトリガイド]({{site.baseurl}}/developer_guide/sdk_repository_guides/web)を参照してください。

{% endtab %}
{% tab android %}

Android SDKから[`requestContentCardsRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html)を呼び出すことで、いつでも手動でBraze Content Cardsの更新をリクエストできます。

{% subtabs local %}
{% subtab Java %}

```java
Braze.getInstance(context).requestContentCardsRefresh();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestContentCardsRefresh()
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

[`Braze.ContentCards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class)クラスの[`requestRefresh`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/requestrefresh(_:))メソッドを呼び出すことで、いつでもSwift SDKからBraze Content Cardsの手動更新をリクエストできます。

{% subtabs local %}
{% subtab Swift %}

Swiftでは、オプションの完了ハンドラまたはネイティブのSwift concurrency APIを使用した非同期リターンにより、Content Cardsを更新できます。

#### 完了ハンドラ {#completion-handler}

```swift
AppDelegate.braze?.contentCards.requestRefresh { result in
  // Implement completion handler
}
```

#### Async/Await

```swift
let contentCards = await AppDelegate.braze?.contentCards.requestRefresh()
```
{% endsubtab %}
{% subtab Objective-C %}

```objc
[AppDelegate.braze.contentCards requestRefreshWithCompletion:^(NSArray<BRZContentCardRaw *> * contentCards, NSError * error) {
  // Implement completion handler
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### フル同期とパーシャル同期 {#full-sync-vs-partial-sync}

Braze SDKは、サーバーからContent Cardsを取得する際に2種類の同期を使用します。

- **フル同期:** ユーザーが対象となるすべてのContent Cardsを取得します。フル同期は7日ごとに自動的に実行されるか、`changeUser()`が呼び出されたときに実行されます。
- **パーシャル同期:** 前回のリクエスト以降の新しいContent Cardsのみを取得します。ユーザーが新しいカードの対象でない場合、レスポンスはゼロカードを返します。パーシャル同期は`requestContentCardsRefresh()`が呼び出されるたびに実行されます（前回のフル同期から7日が経過している場合は、代わりにフル同期がトリガーされます）。

パーシャル同期により、サーバー負荷とデバイスのバッテリー使用量が削減されます。すでに受信されたContent CardsはSDKにローカルで保存されるため、パーシャル同期がゼロの新しいカードを返した場合でも、ユーザーは利用可能なカードを引き続き表示できます。

### レート制限 {#rate-limit}

Brazeはトークンバケットアルゴリズムを使用して、次のレート制限を適用します。
- デバイスあたり最大5回の更新呼び出し（ユーザー間および`openSession()`への呼び出しと共有）
- 制限に達すると、180秒（3分）ごとに新しい呼び出しが1回利用可能になります
- システムは、いつでも使用できるように最大5回分の呼び出しを保持します
- `subscribeToContentCards()`はレート制限中でもキャッシュされたカードを返します

{% alert important %}
Braze SDKは、パフォーマンスと信頼性のためにレート制限も適用します。自動テストの実行時や手動QAの実施時には、この点にご注意ください。詳細については、[Braze SDKのレート制限]({{site.baseurl}}/developer_guide/sdk_integration/rate_limits)を参照してください。
{% endalert %}

## 表示されるカードの順序をカスタマイズする {#customizing-displayed-card-order}

Content Cardsの表示順序を変更できます。これにより、時間的制約のあるプロモーションなど、特定のタイプのコンテンツに優先順位を付けることで、ユーザーエクスペリエンスを微調整できます。

{% tabs %}
{% tab web %}

`showContentCards():`の[`filterFunction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)パラメーターを使用して、フィード内のContent Cardsの表示順序をカスタマイズします。以下に例を示します。

```javascript
braze.showContentCards(null, (cards) => {
  return sortBrazeCards(cards); // Where sortBrazeCards is your sorting function that returns the sorted card array
});
```

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view controller %}
[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)は、[`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html)に依存して、フィードに表示される前にContent Cardsのソートまたは変更を処理します。カスタム更新ハンドラは、`ContentCardsFragment`の[`setContentCardUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html)で設定できます。

以下はデフォルトの`IContentCardsUpdateHandler`であり、カスタマイズの出発点として使用できます。

{% details Javaの例を表示 %}
```java
public class DefaultContentCardsUpdateHandler implements IContentCardsUpdateHandler {

  // Interface that must be implemented and provided as a public CREATOR
  // field that generates instances of your Parcelable class from a Parcel.
  public static final Parcelable.Creator<DefaultContentCardsUpdateHandler> CREATOR = new Parcelable.Creator<DefaultContentCardsUpdateHandler>() {
    public DefaultContentCardsUpdateHandler createFromParcel(Parcel in) {
      return new DefaultContentCardsUpdateHandler();
    }

    public DefaultContentCardsUpdateHandler[] newArray(int size) {
      return new DefaultContentCardsUpdateHandler[size];
    }
  };

  @Override
  public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
    List<Card> sortedCards = event.getAllCards();
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    Collections.sort(sortedCards, new Comparator<Card>() {
      @Override
      public int compare(Card cardA, Card cardB) {
        // A displays above B
        if (cardA.getIsPinned() && !cardB.getIsPinned()) {
          return -1;
        }

        // B displays above A
        if (!cardA.getIsPinned() && cardB.getIsPinned()) {
          return 1;
        }

        // At this point, both A & B are pinned or both A & B are non-pinned
        // A displays above B since A is newer
        if (cardA.getUpdated() > cardB.getUpdated()) {
          return -1;
        }

        // B displays above A since A is newer
        if (cardA.getUpdated() < cardB.getUpdated()) {
          return 1;
        }

        // At this point, every sortable field matches so keep the natural ordering
        return 0;
      }
    });

    return sortedCards;
  }

  // Parcelable interface method
  @Override
  public int describeContents() {
    return 0;
  }

  // Parcelable interface method
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    // No state is kept in this class so the parcel is left unmodified
  }
}
```
{% enddetails %}

{% details Kotlinの例を表示 %}
```kotlin
class DefaultContentCardsUpdateHandler : IContentCardsUpdateHandler {
  override fun handleCardUpdate(event: ContentCardsUpdatedEvent): List<Card> {
    val sortedCards = event.allCards
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    sortedCards.sortWith(Comparator sort@{ cardA: Card, cardB: Card ->
      // A displays above B
      if (cardA.isPinned && !cardB.isPinned) {
        return@sort -1
      }

      // B displays above A
      if (!cardA.isPinned && cardB.isPinned) {
        return@sort 1
      }

      // At this point, both A & B are pinned or both A & B are non-pinned
      // A displays above B since A is newer
      if (cardA.updated > cardB.updated) {
        return@sort -1
      }

      // B displays above A since A is newer
      if (cardA.updated < cardB.updated) {
        return@sort 1
      }
      0
    })
    return sortedCards
  }

  // Parcelable interface method
  override fun describeContents(): Int {
    return 0
  }

  // Parcelable interface method
  override fun writeToParcel(dest: Parcel, flags: Int) {
    // No state is kept in this class so the parcel is left unmodified
  }

  companion object {
    // Interface that must be implemented and provided as a public CREATOR
    // field that generates instances of your Parcelable class from a Parcel.
    val CREATOR: Parcelable.Creator<DefaultContentCardsUpdateHandler?> = object : Parcelable.Creator<DefaultContentCardsUpdateHandler?> {
      override fun createFromParcel(`in`: Parcel): DefaultContentCardsUpdateHandler? {
        return DefaultContentCardsUpdateHandler()
      }

      override fun newArray(size: Int): Array<DefaultContentCardsUpdateHandler?> {
        return arrayOfNulls(size)
      }
    }
  }
}
```
{% enddetails %}

{% alert tip %}
`ContentCardsFragment`のソースは[GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.kt)で確認できます。
{% endalert %}
{% endsubtab %}
{% subtab Jetpack Compose %}
Jetpack ComposeでContent Cardsをフィルタリングおよびソートするには、`cardUpdateHandler`パラメータを設定します。以下に例を示します。

```kotlin
ContentCardsList(
    cardUpdateHandler = {
        it.sortedWith { cardA, cardB ->
            // A displays above B
            if (cardA.isPinned && !cardB.isPinned) {
                return@sortedWith -1
            }
            // B displays above A
            if (!cardA.isPinned && cardB.isPinned) {
                return@sortedWith 1
            }
            // At this point, both A & B are pinned or both A & B are non-pinned
            // A displays above B since A is newer
            if (cardA.updated > cardB.updated) {
                return@sortedWith -1
            }
            // B displays above A since A is newer
            if (cardA.updated < cardB.updated) {
                return@sortedWith 1
            }
            0
        }
    }
)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

静的な[`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults)変数を直接変更して、カードフィードの順序をカスタマイズします。

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
    cards.sorted {
        if $0.pinned && !$1.pinned {
            return true
        } else if !$0.pinned && $1.pinned {
            return false
        } else {
            return $0.createdAt > $1.createdAt
        }
    }
}
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

`BrazeContentCardUI.ViewController.Attributes`によるカスタマイズはObjective-Cでは使用できません。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 「空のフィード」メッセージのカスタマイズ {#customizing-empty-feed-message}

ユーザーがどのContent Cardsにも該当しない場合、SDKは「更新はありません。後で再度確認してください。」という「空のフィード」エラーメッセージを表示します。この「空のフィード」エラーメッセージは、次のようにカスタマイズできます。

![「これはカスタムの空状態のメッセージです。」と表示される空のフィードエラーメッセージ]({% image_buster/assets/img/content_cards/content-card-customization-empty.png %})

{% tabs %}
{% tab web %}

Web SDKでは、「空のフィード」の文言をプログラムで置き換えることはサポートされていません。フィードが表示されるたびに置き換えることもできますが、フィードの更新に時間がかかる場合があり、空のフィードテキストがすぐに表示されないため、この方法はお勧めしません。

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view system %}

[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)がユーザーにContent Cardsの対象がないと判断した場合、空のフィードエラーメッセージが表示されます。

特殊なアダプタ[`EmptyContentCardsAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/EmptyContentCardsAdapter.kt)が標準の[`ContentCardAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/ContentCardAdapter.kt)を置き換えてこのエラーメッセージを表示します。カスタムメッセージ自体を設定するには、文字列リソース`com_braze_feed_empty`をオーバーライドします。

このメッセージの表示に使用されるスタイルは[`Braze.ContentCardsDisplay.Empty`](https://github.com/braze-inc/braze-android-sdk/blob/2e386dfa59a87bfc24ef7cb6ff5adf6b16f44d24/android-sdk-ui/src/main/res/values/styles.xml#L522-L530)で確認でき、次のコードスニペットに示されています。

```xml
<style name="Braze.ContentCardsDisplay.Empty">
  <item name="android:lineSpacingExtra">1.5dp</item>
  <item name="android:text">@string/com_braze_feed_empty</item>
  <item name="android:textColor">@color/com_braze_content_card_empty_text_color</item>
  <item name="android:textSize">18.0sp</item>
  <item name="android:gravity">center</item>
  <item name="android:layout_height">match_parent</item>
  <item name="android:layout_width">match_parent</item>
</style>
```

Content Cardsのスタイル要素のカスタマイズについて詳しくは、[スタイルのカスタマイズ]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)を参照してください。
{% endsubtab %}
{% subtab Jetpack Compose %}
Jetpack Composeで「空のフィード」エラーメッセージをカスタマイズするには、`emptyString`を[`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html)に渡します。また、[`emptyTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html#1193499348%2FProperties%2F-1725759721)を`ContentCardListStyling`に渡して、このメッセージをさらにカスタマイズすることもできます。

```kotlin
ContentCardsList(
    emptyString = "No messages today",
    style = ContentCardListStyling(
        emptyTextStyle = TextStyle(...)
    )
)
```

代わりに表示したいComposableがある場合は、`emptyComposable`を[`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html)に渡します。`emptyComposable`を指定した場合、`emptyString`は使用されません。

```kotlin
ContentCardsList(
    emptyComposable = {
        Image(
            painter = painterResource(id = R.drawable.noMessages),
            contentDescription = "No messages"
        )
    }
)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}
{% subtabs local %}
{% subtab Swift %}

関連する[`Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults)を設定して、ビューコントローラーの空の状態をカスタマイズします。

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.emptyStateMessage = "This is a custom empty state message"
attributes.emptyStateMessageFont = .preferredFont(forTextStyle: .title1)
attributes.emptyStateMessageColor = .secondaryLabel
```

{% endsubtab %}
{% subtab Objective-C %}

空のContent Cardsフィードに自動的に表示される文言を変更するには、アプリの[`ContentCardsLocalizable.strings`](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization/en.lproj)ファイルでローカライズ可能なContent Cards文字列を再定義します。

{% alert note %}
別のロケール言語でこのメッセージを更新する場合は、[リソースフォルダ構造](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization)で対応する言語の`ContentCardsLocalizable.strings`を探してください。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 複数フィードの実装 {#implementing-multiple-feeds}

Content Cardsはアプリ内でフィルタリングして特定のカードのみを表示できるため、さまざまなユースケースに対応する複数のContent Cardsフィードを持つことができます。たとえば、トランザクションフィードとマーケティングフィードの両方を維持できます。これを実現するには、Brazeダッシュボードでキーと値のペアを設定して、Content Cardsのさまざまなカテゴリーを作成します。次に、これらのタイプのContent Cardsを異なる方法で処理し、一部のタイプをフィルタリングして他のタイプを表示するフィードをアプリまたはサイトに作成します。

### ステップ1:カードにキーと値のペアを設定する {#step-1-set-key-value-pairs-on-cards}

Content Cards キャンペーンを作成する際に、各カードに[キーと値のペアデータ]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior)を設定します。このキーと値のペアを使用してカードを分類します。キーと値のペアは、カードのデータモデルの`extras`プロパティに保存されます。

この例では、カードが表示されるContent Cardsフィードを指定するキー`feed_type`を使用してキーと値のペアを設定します。値は、`home_screen`や`marketing`など、カスタムフィードに応じた任意の値になります。

### ステップ2:Content Cardsをフィルタリングする {#step-2-filter-content-cards}

キーと値のペアを割り当てたら、表示したいカードを表示し、他のタイプのカードをフィルタリングするロジックを含むフィードを作成します。この例では、`feed_type: "Transactional"`のキーと値のペアが一致するカードのみを表示します。

{% tabs %}
{% tab web %}

次の例では、`Transactional`タイプのカードのContent Cardsフィードを表示します。

```javascript

/**
 * @param {String} feed_type - value of the "feed_type" KVP to filter
 */
function showCardsByFeedType(feed_type) {
  braze.showContentCards(null, function(cards) {
    return cards.filter((card) => card.extras["feed_type"] === feed_type);
  });
}
```

次に、カスタムフィードのトグルを設定できます。

```javascript
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional");
};
```

詳細については、[SDKメソッドのドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)を参照してください。

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view system %}

デフォルトでは、Content Cardsフィードは[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)に表示され、[`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html)はBraze SDKから[`ContentCardsUpdatedEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html)を受け取った後に表示するカードのリストを返します。ただし、カードのソートのみを行い、フィルタリングは直接処理しません。

#### ステップ2.1:カスタムハンドラを作成する {#step-21-create-a-custom-handler}

ダッシュボードで[`Card.getExtras()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html)によって設定されたキーと値のペアを使用してカスタム[`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html)を実装し、先ほど設定した`feed_type`の値と一致しないカードをリストから削除するように変更することで、Content Cardsをフィルタリングできます。

{% details Javaの例を表示 %}
```java
private IContentCardsUpdateHandler getUpdateHandlerForFeedType(final String desiredFeedType) {
  return new IContentCardsUpdateHandler() {
    @Override
    public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
      // Use the default card update handler for a first
      // pass at sorting the cards. This is not required
      // but is done for convenience.
      final List<Card> cards = new DefaultContentCardsUpdateHandler().handleCardUpdate(event);

      final Iterator<Card> cardIterator = cards.iterator();
      while (cardIterator.hasNext()) {
        final Card card = cardIterator.next();

        // Make sure the card has our custom KVP
        // from the dashboard with the key "feed_type"
        if (card.getExtras().containsKey("feed_type")) {
          final String feedType = card.getExtras().get("feed_type");
          if (!desiredFeedType.equals(feedType)) {
            // The card has a feed type, but it doesn't match
            // our desired feed type, remove it.
            cardIterator.remove();
          }
        } else {
          // The card doesn't have a feed
          // type at all, remove it
          cardIterator.remove();
        }
      }

      // At this point, all of the cards in this list have
      // a feed type that explicitly matches the value we put
      // in the dashboard.
      return cards;
    }
  };
}
```
{% enddetails %}

{% details Kotlinの例を表示 %}
```kotlin
private fun getUpdateHandlerForFeedType(desiredFeedType: String): IContentCardsUpdateHandler {
  return IContentCardsUpdateHandler { event ->
    // Use the default card update handler for a first
    // pass at sorting the cards. This is not required
    // but is done for convenience.
    val cards = DefaultContentCardsUpdateHandler().handleCardUpdate(event)

    val cardIterator = cards.iterator()
    while (cardIterator.hasNext()) {
      val card = cardIterator.next()

      // Make sure the card has our custom KVP
      // from the dashboard with the key "feed_type"
      if (card.extras.containsKey("feed_type")) {
        val feedType = card.extras["feed_type"]
        if (desiredFeedType != feedType) {
          // The card has a feed type, but it doesn't match
          // our desired feed type, remove it.
          cardIterator.remove()
        }
      } else {
        // The card doesn't have a feed
        // type at all, remove it
        cardIterator.remove()
      }
    }

    // At this point, all of the cards in this list have
    // a feed type that explicitly matches the value we put
    // in the dashboard.
    cards
  }
}
```
{% enddetails %}

#### ステップ2.2:フラグメントに追加する {#step-22-add-it-to-a-fragment}

[`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html)を作成したら、それを使用する[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)を作成します。このカスタムフィードは、他の`ContentCardsFragment`と同様に使用できます。アプリのさまざまな部分で、ダッシュボードで設定したキーに基づいて、異なるContent Cardsフィードを表示します。各`ContentCardsFragment`フィードには、各フラグメントのカスタム`IContentCardsUpdateHandler`により、固有のカードセットが表示されます。

{% details Javaの例を表示 %}
```java
// We want a Content Cards feed that only shows "Transactional" cards.
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));
```
{% enddetails %}

{% details Kotlinの例を表示 %}
```kotlin
// We want a Content Cards feed that only shows "Transactional" cards.
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")
```
{% enddetails %}
{% endsubtab %}

{% subtab Jetpack Compose %}
このフィードに表示されるContent Cardsをフィルタリングするには、`cardUpdateHandler`を使用します。以下に例を示します。

```kotlin
ContentCardsList(
     cardUpdateHandler = {
         it.filter { card ->
             card.extras["feed_type"] == "Transactional"
         }
     }
 )
 ```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

The following example will show the Content Cards feed for `Transactional` type cards:

{% subtabs %}
{% subtab Swift %}

```swift
// Filter cards by the `Transactional` feed type based on your key-value pair.
let transactionalCards = cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
```

さらに一歩進めて、ビューコントローラーに表示されるカードは、`Attributes`構造体の`transform`プロパティを設定して、条件でフィルタリングされたカードのみを表示するようにフィルタリングできます。

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
}

// Pass your attributes containing the transformed cards to the Content Card UI.
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Filter cards by the `Transactional` feed type based on your key-value pair.
NSMutableArray<BRZContentCardRaw *> *transactionalCards = [[NSMutableArray alloc] init];
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if ([card.extras[@"feed_type"] isEqualToString:@"Transactional"]) {
    [transactionalCards addObject:card];
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}