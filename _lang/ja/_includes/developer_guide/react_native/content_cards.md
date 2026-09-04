## React NativeのContent Cardsについて {#about-react-native-content-cards}

Braze SDKには、Content Cardsを使い始めるためのデフォルトのカードフィードが含まれています。カードフィードを表示するには、`Braze.launchContentCards()`メソッドを使用できます。Braze SDKに含まれるデフォルトのカードフィードは、ユーザーのContent Cardsの分析トラッキング、非表示、レンダリングをすべて処理します。

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## カードのメソッド {#cards-methods}

独自のUIを構築するには、利用可能なカードのリストを取得し、カードの更新をリッスンできます。

```javascript
// Set initial cards
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`, or after the timeout period
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, async (update) => {
    setCards(update.cards);
});

// Manually trigger a refresh of cards
Braze.requestContentCardsRefresh();
```

{% alert important %}
カードを表示する独自のUIを構築する場合、それらのカードの分析を受け取るために`logContentCardImpression`を呼び出す必要があります。これには`control`カードも含まれます。コントロールカードはユーザーに表示されませんが、トラッキングする必要があります。
{% endalert %}

以下の追加メソッドを使用して、アプリ内にカスタムContent Cardsフィードを構築できます。

| メソッド                                   | 説明                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | Content CardsのUI要素を起動します。                                                                 |
| `requestContentCardsRefresh()`           | Braze SDKサーバーから最新のContent Cardsをリクエストします。結果として得られるカードのリストは、以前に登録された[コンテンツカードイベントの各リスナー](#reactnative_cards-methods)に渡されます。 |
| `getCachedContentCards()`                | キャッシュから最新のContent Cards配列を返します。                                            |
| `logContentCardClicked(cardId)`          | 指定されたContent カード IDのクリックを記録します。このメソッドは分析専用です。クリックアクションを実行するには、追加で`processContentCardClickAction(cardId)`を呼び出してください。                                                        |
| `logContentCardImpression(cardId)`       | 指定されたContent カード IDのインプレッションを記録します。                                                      |
| `logContentCardDismissed(cardId)`        | 指定されたContent カード IDの非表示を記録します。                                                        |
| `processContentCardClickAction(cardId)`  | 特定のカードのアクションを実行します。                                                               |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カードのメソッド" }

## カードのタイプとプロパティ {#card-types-and-properties}

Content CardsデータモデルはReact Native SDKで利用可能で、以下のContent Cardsカードタイプを提供します：[画像のみ](#image-only)、[キャプション付き画像](#captioned-image)、[クラシック](#classic)。また、特別な[コントロール](#control)カードタイプもあり、指定されたカードのコントロールグループに属するユーザーに返されます。各タイプは、独自のプロパティに加えて、ベースモデルから共通のプロパティを継承します。

{% alert tip %}
Content Cardsデータモデルの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard)のドキュメントを参照してください。
{% endalert %}

### ベースカードモデル {#base-card-model}

ベースカードモデルは、すべてのカードの基本的な動作を提供します。

| プロパティ      | 説明                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
| `id`          | Brazeによって設定されたカードのIDです。                                                                                            |
| `created`     | Brazeからのカード作成時刻のUNIXタイムスタンプです。                                                             |
| `expiresAt`   | カードの有効期限を示すUNIXタイムスタンプです。値が0より小さい場合は、カードの有効期限がないことを意味します。      |
| `viewed`      | カードがユーザーによって既読か未読かを示します。これは分析のログを記録しません。                                           |
| `clicked`     | カードがユーザーによってクリックされたかどうかを示します。                                                                         |
| `pinned`      | カードが固定されているかどうかを示します。                                                                                            |
| `dismissed`   | ユーザーがこのカードを非表示にしたかどうかを示します。すでに非表示にされたカードに非表示マークを付けても何も起こりません。 |
| `dismissible` | ユーザーがカードを非表示にできるかどうかを示します。                                                                           |
| `url`         | （オプション）カードクリックアクションに関連付けられたURL文字列です。                                                       |
| `openURLInWebView` | このカードのURLをBraze WebViewで開くかどうかを示します。                                            |
| `isControl`   | このカードがコントロールカードかどうかを示します。コントロールカードはユーザーに表示しないでください。                                |
| `extras`      | このカードのキーバリューエクストラのマップです。                                                                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ベースカードモデル" }

ベースカードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct)のドキュメントを参照してください。

### 画像のみ {#image-only}

画像のみのカードはクリック可能なフルサイズの画像です。

| プロパティ           | 説明                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | Content Cardsの種類、`IMAGE_ONLY`です。                                                                              |
| `image`            | カードの画像のURLです。                                                                                      |
| `imageAspectRatio` | カード画像のアスペクト比です。画像の読み込みが完了する前のヒントとして利用するためのものです。特定の状況ではプロパティが提供されない場合があることに注意してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="画像のみ" }

画像のみのカードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct)のドキュメントを参照してください。

### キャプション付き画像 {#captioned-image}

キャプション付き画像カードはクリック可能なフルサイズの画像で、説明文が添えられています。

| プロパティ           | 説明                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | Content Cardsの種類、`CAPTIONED`です。                                                                               |
| `image`            | カードの画像のURLです。                                                                                      |
| `imageAspectRatio` | カード画像のアスペクト比です。画像の読み込みが完了する前のヒントとして利用するためのものです。特定の状況ではプロパティが提供されない場合があることに注意してください。 |
| `title`            | カードのタイトルテキストです。                                                                                      |
| `cardDescription`  | カードの説明テキストです。                                                                                |
| `domain`           | （オプション）プロパティURLのリンクテキストです（例：`"braze.com/resources/"`）。カードのUIに表示され、カードをクリックした際のアクションや方向を示すことができます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="キャプション付き画像" }

キャプション付き画像カードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct)のドキュメントを参照してください。

### クラシック {#classic}

クラシックカードには、タイトル、説明、およびオプションの画像がテキストの前に表示されます。

| プロパティ           | 説明                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | Content Cardsの種類、`CLASSIC`です。                                                                                 |
| `image`            | （オプション）カードの画像のURLです。                                                                           |
| `title`            | カードのタイトルテキストです。                                                                                      |
| `cardDescription`  | カードの説明テキストです。                                                                                |
| `domain`           | （オプション）プロパティURLのリンクテキストです（例：`"braze.com/resources/"`）。カードのUIに表示され、カードをクリックした際のアクションや方向を示すことができます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="クラシック" }

クラシック（テキストアナウンス）Content Cardsの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct)のドキュメントを参照してください。クラシック画像（ショートニュース）カードについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct)のドキュメントを参照してください。

### コントロール {#control}

コントロールカードにはベースプロパティがすべて含まれていますが、いくつかの重要な違いがあります。最も重要な点は以下のとおりです。

- `isControl`プロパティは`true`であることが保証されています。
- `extras`プロパティは空であることが保証されています。

コントロールカードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct)のドキュメントを参照してください。