## 前提条件 {#prerequisites}

Brazeのコンテンツカードを使用する前に、アプリに[Braze Android SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)を統合する必要があります。ただし、追加のセットアップは不要です。

## Googleフラグメント {#google-fragments}

Androidでは、Content Cardsフィードは Braze Android UIプロジェクトで使用可能な[フラグメント](https://developer.android.com/guide/components/fragments.html)として実装されます。[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html)クラスは、Content Cardsの内容を自動的に更新して表示し、使用状況の分析をログに記録します。ユーザーの`ContentCards`に表示できるカードは、Brazeダッシュボードで作成されます。

アクティビティにフラグメントを追加する方法については、[Googleのフラグメントに関するドキュメント](https://developer.android.com/guide/fragments#Adding)を参照してください。

## カードのタイプとプロパティ {#card-types-and-properties}

Content Cardsデータモデルは Android SDKで利用可能であり、以下の固有のコンテンツカードタイプを提供します。各タイプはベースモデルを共有しており、独自のプロパティを持つことに加え、ベースモデルから共通のプロパティを継承できます。完全な参照ドキュメントについては、[`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)を参照してください。

### 基本カードモデル {#base-card-for-android}

[ベースカード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)モデルは、すべてのカードの基本的な動作を規定します。

| プロパティ | 説明 |
|---|---|
| `getId()` | Brazeで設定されたカードのIDを返します。|
| `getViewed()` | カードがユーザーによって既読か未読かを反映したブール値を返します。|
| `getExtras()` | このカードのキーと値のエクストラのマップを返します。|
| `getCreated()` | カードの作成時刻をBrazeからunixタイムスタンプで返します。|
| `isPinned` | カードがピン留めされているかどうかを示すブール値を返します。|
| `getOpenUriInWebView()` | このカードのURIをBraze WebViewで開くべきかどうかを示すブール値を返します。|
| `getExpiredAt()` | カードの有効期限を取得します。|
| `isRemoved()` | エンドユーザーがこのカードを非表示にしたかどうかを示すブール値を返します。|
| `isDismissibleByUser()` | そのカードがユーザーによって閉じられるかどうかを示すブール値を返します。|
| `isClicked()` | このカードのクリック状態を反映したブール値を返します。|
| `isDismissed` | カードが却下されたかどうかを示すブール値を返します。カードを却下済みとしてマークするには、`true`に設定します。カードがすでに却下済みとしてマークされている場合、そのカードを再度却下済みとしてマークすることはできません。|
| `isControl()` | このカードがコントロールカードであり、レンダリングされるべきでない場合にブール値を返します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Base card model #base-card-for-android" }

### 画像のみ {#banner-image-card-for-android}

[画像のみのカード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html)はクリック可能なフルサイズの画像です。

| プロパティ | 説明 |
|---|---|
| `getImageUrl()` | カードの画像のURLを返します。|
| `getUrl()` | カードがクリックされた後に開かれるURLを返します。HTTP(s) URLでもプロトコルURLでもかまいません。|
| `getDomain()` | プロパティURLのリンクテキストを返します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image only #banner-image-card-for-android" }

### キャプション付き画像 {#captioned-image-card-for-android}

[キャプション付き画像カード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html)はクリック可能なフルサイズの画像で、説明文が添えられています。

| プロパティ | 説明 |
|---|---|
| `getImageUrl()` | カードの画像のURLを返します。|
| `getTitle()` | カードのタイトルテキストを返します。|
| `getDescription()` | カードの本文テキストを返します。|
| `getUrl()` | カードがクリックされた後に開かれるURLを返します。HTTP(s) URLでもプロトコルURLでもかまいません。|
| `getDomain()` | プロパティURLのリンクテキストを返します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captioned image #captioned-image-card-for-android" }

### クラシック {#text-Announcement-card-for-android}

画像が含まれていないクラシックカードは、[テキストアナウンスカード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html)になります。画像が含まれている場合は、[ショートニュースカード](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html)を受け取ります。

| プロパティ | 説明 |
|---|---|
| `getTitle()` | カードのタイトルテキストを返します。 |
| `getDescription()` | カードの本文テキストを返します。 |
| `getUrl()` | カードがクリックされた後に開かれるURLを返します。HTTP(s) URLでもプロトコルURLでもかまいません。 |
| `getDomain()` | プロパティURLのリンクテキストを返します。 |
| `getImageUrl()` | カードの画像のURLを返します。クラシックショートニュースカードにのみ適用されます。 |
| `isDismissed` | カードが却下されたかどうかを示すブール値を返します。カードを却下済みとしてマークするには、`true`に設定します。カードがすでに却下済みとしてマークされている場合、そのカードを再度却下済みとしてマークすることはできません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classic #text-Announcement-card-for-android" }

## カードメソッド {#card-methods}

すべての[`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)データモデルオブジェクトは、ユーザーイベントをBrazeサーバーに記録するための以下の分析メソッドを提供します。

| メソッド | 説明 |
|---|---|
| `logImpression()` | 特定のカードのインプレッションを手動でBrazeに記録します。 |
| `logClick()` | 特定のカードのクリックを手動でBrazeに記録します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Card methods" }