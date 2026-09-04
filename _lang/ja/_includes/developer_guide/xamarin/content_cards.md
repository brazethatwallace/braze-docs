## .NET MAUI Content Cardsについて {#about-net-maui-content-cards}

Braze .NET MAUI（旧称Xamarin）SDKには、Content Cardsの利用を開始するためのデフォルトのカードフィードが含まれています。Braze SDKに含まれるデフォルトのカードフィードは、ユーザーのContent Cardsのすべての分析トラッキング、却下、レンダリングを処理します。

{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## カードのタイプとプロパティ {#card-types-and-properties}

Braze .NET MAUI SDKには、共通のベースモデルを持つ3種類のユニークなContent Cardsカードタイプがあります：[バナー](#xamarin_banner)、[キャプション付き画像](#xamarin_captioned-image)、[クラシック](#xamarin_classic)。各タイプはベースモデルから共通のプロパティを継承し、以下の追加プロパティを持ちます。

### 基本カードモデル {#base-card-model}

| プロパティ | 説明 |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| `idString` | Brazeによって設定されたカードのID。 |
| `created` | Brazeからのカード作成時間のUNIXタイムスタンプ。 |
| `expiresAt` | カードの有効期限を示すUNIXタイムスタンプ。値が0より小さい場合は、カードの有効期限がないことを意味します。 |
| `viewed` | カードがユーザーによって既読か未読か。これは分析のログを記録しません。 |
| `clicked` | カードがユーザーによってクリックされたかどうか。 |
| `pinned` | カードが固定されているかどうか。 |
| `dismissed` | ユーザーがこのカードを却下したかどうか。すでに却下されたカードに却下マークを付けても何も起こりません。 |
| `dismissible` | ユーザーがカードを却下できるかどうか。 |
| `urlString` | （オプション）カードクリックアクションに関連付けられたURL文字列。 |
| `openUrlInWebView` | このカードのURLをBraze WebViewで開くかどうか。 |
| `isControlCard` | このカードがコントロールカードかどうか。コントロールカードはユーザーに表示しないでください。 |
| `extras` | このカードのキーバリューエクストラのマップ。 |
| `isTest` | このカードがテストカードかどうか。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="基本カードモデル" }

ベースカードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct)のドキュメントを参照してください。

### バナー {#xamarin_banner}

バナーカードはクリック可能なフルサイズの画像です。

| プロパティ | 説明 |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `image` | カードの画像のURL。 |
| `imageAspectRatio` | カード画像のアスペクト比。画像の読み込みが完了する前のヒントとして利用されます。特定の状況ではこのプロパティが提供されない場合があることに注意してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="バナー" }

バナーカードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct)のドキュメント（現在は「画像のみ」に名称変更）を参照してください。

### キャプション付き画像 {#xamarin_captioned-image}

キャプション付き画像カードはクリック可能なフルサイズの画像で、説明テキストが添えられています。

| プロパティ | 説明 |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `image` | カードの画像のURL。 |
| `imageAspectRatio` | カード画像のアスペクト比。画像の読み込みが完了する前のヒントとして利用されます。特定の状況ではこのプロパティが提供されない場合があることに注意してください。 |
| `title` | カードのタイトルテキスト。 |
| `cardDescription` | カードの説明テキスト。 |
| `domain` | （オプション）プロパティURLのリンクテキスト（例：`"braze.com/resources/"`）。カードのUIに表示され、カードをクリックした際のアクション/方向を示すことができます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="キャプション付き画像" }

キャプション付き画像カードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct)のドキュメントを参照してください。

### クラシック {#xamarin_classic}

クラシックカードには、タイトル、説明、およびテキストの前にオプションの画像が表示されます。

| プロパティ | 説明 |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `image` | （オプション）カードの画像のURL。 |
| `title` | カードのタイトルテキスト。 |
| `cardDescription` | カードの説明テキスト。 |
| `domain` | （オプション）プロパティURLのリンクテキスト（例：`"braze.com/resources/"`）。カードのUIに表示され、カードをクリックした際のアクション/方向を示すことができます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="クラシック" }

クラシック（テキストアナウンス）Content Cardsの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct)のドキュメントを参照してください。クラシック画像（ショートニュース）カードの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct)のドキュメントを参照してください。

## カードメソッド {#card-methods}

以下の追加メソッドを使用して、アプリ内にカスタムContent Cardsフィードを構築できます。

| メソッド | 説明 |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()` | Braze SDKサーバーから最新のContent Cardsをリクエストします。 |
| `getContentCards()` | Braze SDKからContent Cardsを取得します。サーバーからの最新のカードリストが返されます。 |
| `logContentCardClicked(cardId)` | 指定されたContent カード IDのクリックを記録します。このメソッドは分析のみに使用されます。 |
| `logContentCardImpression(cardId)` | 指定されたContent カード IDのインプレッションを記録します。 |
| `logContentCardDismissed(cardId)` | 指定されたContent カード IDの却下を記録します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カードメソッド" }