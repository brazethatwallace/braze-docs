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

### 自動更新 {#automatic-refresh}

デフォルトでは、Content Cardsフィードは以下の場合に自動的に更新されます。

- 新しいセッションが開始されたとき
- デフォルトのContent Cardsフィードが閉じられ、最後の更新から60秒以上経過した後に再度開かれたとき

{% alert tip %}
手動で更新せずに最新のContent Cardsをダイナミックに表示するには、カード作成時に**最初のインプレッション時**を選択してください。これらのカードは利用可能になった時点で更新されます。
{% endalert %}

### リアルタイム配信 {#real-time-delivery}

Brazeは、SDKがセッション中に維持するライブ接続を通じて、Content Cardsの更新が発生するとすぐにデバイスに送信します。ユーザーは変更を確認するために新しいセッションを開始したり、更新を待ったりする必要はありません。

リアルタイム配信は以下の更新に対応しています。

- セッション中にユーザーがContent Cardsキャンペーンの対象になった場合
- ユーザーがキャンバスのContent Cardsステップに進んだ場合
- ユーザーのフィードからカードが削除された場合
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)、[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)、[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)エンドポイントなど、APIを通じてカードが送信された場合

リアルタイム配信には以下の最低SDKバージョンが必要です。

{% sdk_min_versions swift:18.0.0 android:43.1.1 web:6.12.0 %}

それ以前のSDKバージョンでは、カードはセッション開始時と更新時に配信されます。

### 手動更新 {#manual-refresh}

特定のタイミングでフィードを手動更新するには、以下を行います。

{% tabs %}
{% tab web %}

Web SDKからBraze Content Cardsの手動更新をいつでもリクエストするには、[`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh)を呼び出します。

また、[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)を呼び出して、最後のContent Cards更新から現在利用可能なすべてのカードを取得することもできます。

```javascript
import * as braze from "@braze/web-sdk";

function refresh() {
  braze.requestContentCardsRefresh();
}
```

Content Cardsのリンクを同じタブではなく新しいブラウザタブで開くには、Web SDK初期化オプションで`openCardsInNewTab: true`を設定します。初期化オプションの詳細については、[Web SDKリポジトリガイド]({{site.baseurl}}/developer_guide/sdk_repository_guides/web)を参照してください。

{% endtab %}
{% tab android %}

Android SDKからBraze Content Cardsの手動更新をいつでもリクエストするには、[`requestContentCardsRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html)を呼び出します。

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

Swift SDKからBraze Content Cardsの手動更新をいつでもリクエストするには、[`Braze.ContentCards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class)クラスの[`requestRefresh`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/requestrefresh(_:))メソッドを呼び出します。

{% subtabs local %}
{% subtab Swift %}

Swiftでは、オプションの完了ハンドラーを使用するか、ネイティブのSwift並行処理APIを使用した非同期リターンでContent Cardsを更新できます。

#### 完了ハンドラー {#completion-handler}

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

### フル同期と部分同期 {#full-sync-vs-partial-sync}

Braze SDKは、サーバーからContent Cardsを取得する際に2種類の同期を使用します。

- **フル同期：** ユーザーが対象となるすべてのContent Cardsを取得します。フル同期は7日ごとに自動的に実行されるか、`changeUser()`が呼び出されたときに実行されます。
- **部分同期：** 前回のリクエスト以降の新しいContent Cardsのみを取得します。ユーザーが新しいカードの対象でない場合、レスポンスはゼロ件のカードを返します。部分同期は`requestContentCardsRefresh()`が呼び出されるたびに実行されます（前回のフル同期から7日が経過している場合を除き、その場合はフル同期がトリガーされます）。

部分同期はサーバーの負荷とデバイスのバッテリー使用量を削減します。すでに受信されたContent CardsはSDKにローカルで保存されるため、部分同期で新しいカードがゼロ件返された場合でも、ユーザーは利用可能なカードを引き続き表示できます。

### レート制限 {#rate-limit}

Brazeはトークンバケットアルゴリズムを使用して、以下のレート制限を適用します。
- デバイスごとに最大5回の更新呼び出し（ユーザー間および`openSession()`の呼び出しと共有）
- 制限に達した後、180秒（3分）ごとに新しい呼び出しが利用可能になります
- システムはいつでも使用できるように最大5回の呼び出しを保持します
- `subscribeToContentCards()`はレート制限中でもキャッシュされたカードを返します

{% alert important %}
Braze SDKはパフォーマンスと信頼性のためにもレート制限を適用します。自動テストの実行や手動QAの実施時にはこの点に留意してください。詳細については、[Braze SDKレート制限]({{site.baseurl}}/developer_guide/sdk_integration/rate_limits)を参照してください。
{% endalert %}

## 表示されるカードの順序のカスタマイズ {#customizing-displayed-card-order}

Content Cardsの表示順序を変更できます。これにより、期間限定のプロモーションなど、特定のタイプのコンテンツを優先してユーザーエクスペリエンスを微調整できます。

{% tabs %}
{% tab web %}

`showContentCards():`の[`filterFunction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)パラメータを使用して、フィード内のContent Cardsの表示順序をカスタマイズします。例：

```javascript
braze.showContentCards(null, (cards) => {
  return sortBrazeCards(cards); // Where sortBrazeCards is your sorting function that returns the sorted card array
});
```

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view controller %}
[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)は、Content Cardsがフィードに表示される前にソートや変更を処理するために[`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html)を利用します。カスタム更新ハンドラーは、`ContentCardsFragment`の[`setContentCardUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html)で設定できます。

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
Jetpack ComposeでContent Cardsをフィルタリングおよびソートするには、`cardUpdateHandler`パラメータを設定します。例：

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

`BrazeContentCardUI.ViewController.Attributes`によるカスタマイズはObjective-Cでは利用できません。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 「フィードが空」のメッセージをカスタマイズする {#customizing-empty-feed-message}

ユーザーがどのContent Cardsにも該当しない場合、SDKは「フィードが空」というエラーメッセージを表示します:「We have no updates. Please check again later.」このエラーメッセージは、以下のようにカスタマイズできます。

![「This is a custom empty state message.」と表示されたフィードが空のエラーメッセージ]({% image_buster/assets/img/content_cards/content-card-customization-empty.png %})

{% tabs %}
{% tab web %}

Web SDKでは、「フィードが空」の表示言語をプログラムで置き換えることはサポートされていません。フィードが表示されるたびに置き換えることは可能ですが、フィードの更新に時間がかかる場合があり、空のフィードテキストがすぐに表示されないため、推奨されません。

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view system %}

[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)がユーザーがどのContent Cardsにも該当しないと判定した場合、フィードが空のエラーメッセージを表示します。

特別なアダプターである[`EmptyContentCardsAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/EmptyContentCardsAdapter.kt)が、標準の[`ContentCardAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/ContentCardAdapter.kt)を置き換えてこのエラーメッセージを表示します。カスタムメッセージを設定するには、文字列リソース`com_braze_feed_empty`をオーバーライドしてください。

このメッセージの表示に使用されるスタイルは[`Braze.ContentCardsDisplay.Empty`](https://github.com/braze-inc/braze-android-sdk/blob/2e386dfa59a87bfc24ef7cb6ff5adf6b16f44d24/android-sdk-ui/src/main/res/values/styles.xml#L522-L530)から確認でき、以下のコードスニペットに記載されています:

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

Content Cardsのスタイル要素のカスタマイズの詳細については、[スタイルのカスタマイズ]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)を参照してください。
{% endsubtab %}
{% subtab Jetpack Compose %}
Jetpack Composeで「フィードが空」のエラーメッセージをカスタマイズするには、[`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html)に`emptyString`を渡します。さらに、`ContentCardListStyling`に[`emptyTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html#1193499348%2FProperties%2F-1725759721)を渡して、このメッセージをさらにカスタマイズすることもできます。

```kotlin
ContentCardsList(
    emptyString = "No messages today",
    style = ContentCardListStyling(
        emptyTextStyle = TextStyle(...)
    )
)
```

代わりにComposableを表示したい場合は、[`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html)に`emptyComposable`を渡します。`emptyComposable`が指定されている場合、`emptyString`は使用されません。

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

Content Cardsのフィードが空の場合に自動的に表示される言語を変更するには、アプリの[`ContentCardsLocalizable.strings`](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization/en.lproj)ファイルでローカライズ可能なContent Cardsの文字列を再定義します。

{% alert note %}
異なるロケール言語でこのメッセージを更新する場合は、[リソースフォルダー構造](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization)で文字列`ContentCardsLocalizable.strings`を持つ対応する言語を見つけてください。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 複数フィードの実装 {#implementing-multiple-feeds}

Content Cardsをアプリ内でフィルタリングすることで、特定のカードのみを表示し、さまざまなユースケースに対応する複数のContent Cardsフィードを持つことができます。たとえば、トランザクションフィードとマーケティングフィードの両方を維持できます。これを実現するには、Brazeダッシュボードでキーと値のペアを設定して、Content Cardsのさまざまなカテゴリを作成します。次に、これらの種類のContent Cardsを異なる方法で処理するフィードをアプリやサイトに作成し、一部の種類をフィルタリングで除外し、他の種類を表示します。

### ステップ1:カードにキーと値のペアを設定する {#step-1-set-key-value-pairs-on-cards}

Content Cardsキャンペーンを作成する際に、各カードに[キーと値のペアデータ]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior)を設定します。このキーと値のペアを使用してカードを分類します。キーと値のペアは、カードのデータモデルの`extras`プロパティに保存されます。

この例では、キー`feed_type`を持つキーと値のペアを設定し、そのContent Cardsがどのフィードに表示されるかを指定します。値は、`home_screen`や`marketing`など、カスタムフィードに応じた任意の値になります。

### ステップ2:Content Cardsをフィルタリングする {#step-2-filter-content-cards}

キーと値のペアが割り当てられたら、表示したいカードを表示し、他の種類のカードをフィルタリングで除外するロジックを持つフィードを作成します。この例では、キーと値のペアが`feed_type: "Transactional"`に一致するカードのみを表示します。

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

詳細については、[SDKメソッドドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)を参照してください。

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view system %}

デフォルトでは、Content Cardsフィードは[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)に表示され、[`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html)がBraze SDKから[`ContentCardsUpdatedEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html)を受信した後に表示するカードのリストを返します。ただし、カードのソートのみを行い、フィルタリングは直接処理しません。

#### ステップ2.1:カスタムハンドラーを作成する {#step-21-create-a-custom-handler}

ダッシュボードで[`Card.getExtras()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html)によって設定されたキーと値のペアを使用してカスタム[`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html)を実装し、Content Cardsをフィルタリングできます。次に、先ほど設定した`feed_type`の値に一致しないカードをリストから削除するように変更します。

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

[`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html)を作成したら、それを使用する[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)を作成します。このカスタムフィードは、他の`ContentCardsFragment`と同様に使用できます。アプリのさまざまな部分で、ダッシュボードで指定したキーに基づいて異なるContent Cardsフィードを表示します。各`ContentCardsFragment`フィードは、各フラグメントのカスタム`IContentCardsUpdateHandler`のおかげで、一意のカードセットを表示します。

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
このフィードで表示するContent Cardsをフィルタリングするには、`cardUpdateHandler`を使用します。例:

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

さらに一歩進めるには、`Attributes`構造体の`transform`プロパティを設定して、ビューコントローラーに表示されるカードをフィルタリングし、条件に一致するカードのみを表示できます。

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