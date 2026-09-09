{% multi_lang_include archive/web-v4-rename.md %}

## 前提条件 {#prerequisites}

Content Cardsを使用する前に、アプリに[Braze Web SDKを統合]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)する必要があります。ただし、追加の設定は不要です。独自のUIを構築する場合は、[Content Cardsカスタマイズガイド]({{site.baseurl}}/developer_guide/content_cards)を参照してください。

{% alert note %}
一部の広告ブロッカーやブラウザのプライバシー拡張機能は、Braze Web SDKのスクリプトや関連するネットワークリクエストをブロックし、Content Cardsの読み込みを妨げる場合があります。CDN統合方式を使用している場合は、[NPM統合方式]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web)への切り替えを検討してください。この方式ではSDKライブラリがWebサイト上にローカルで保存されるため、広告ブロッカーに関連する一部の問題を回避できます。
{% endalert %}

## 標準フィードUI {#standard-feed-ui}

組み込みのContent Cards UIを使用するには、Webサイト上でフィードを表示する場所を指定する必要があります。

この例では、Content Cardsフィードを配置する `<div id="feed"></div>` を用意しています。フィードの非表示、表示、またはトグル（現在の状態に基づいて非表示または表示）を行うための3つのボタンを使用します。

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script>
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");

   toggle.onclick = function(){
      braze.toggleContentCards(feed);
   }

   hide.onclick = function(){
      braze.hideContentCards();
   }

   show.onclick = function(){
      braze.showContentCards(feed);
   }
</script>
```

`toggleContentCards(parentNode, filterFunction)` メソッドおよび `showContentCards(parentNode, filterFunction)` メソッドを使用する際、引数が指定されていない場合、すべてのContent Cardsがページ上の固定位置サイドバーに表示されます。引数が指定されている場合、フィードは指定された `parentNode` オプションに配置されます。

|パラメーター | 説明 |
|---|---|
|`parentNode` | Content Cardsをレンダリングする HTML ノードです。親ノードの直下の子要素としてすでにBraze Content Cardsビューがある場合、既存のContent Cardsが置き換えられます。たとえば、`document.querySelector(".my-container")` を渡します。|
|`filterFunction` | このビューに表示されるカードのフィルターまたはソート関数です。`{pinned, date}` でソートされた `Card` オブジェクトの配列で呼び出されます。このユーザーに対してレンダリングするソート済みの `Card` オブジェクトの配列を返すことが期待されます。省略した場合、すべてのカードが表示されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="標準フィードUI" }

Content Cardsのトグルの詳細については、[SDKリファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)を参照してください。

## WebでのContent Cardsのテスト {#testing-content-cards-on-the-web}

ブラウザの開発者ツールを使用して、Content Cardsの統合をテストできます。

1. Content Cardsキャンペーンを作成し、テストユーザーをターゲットに設定します。
2. Web SDK統合が実装されているWebサイトにログインします。
3. ブラウザのコンソールを開きます。Chromeの場合、ページを右クリックし、**検証** を選択してから **Console** タブを選択します。
4. コンソールで以下のコマンドを実行します。
   - `window.braze.getCachedContentCards()`
   - `window.braze.toggleContentCards()`

## カードタイプとプロパティ {#card-types-and-properties}

Content Cardsのデータモデルは Web SDKで利用でき、以下のContent Cardsタイプを提供します: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)、[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)、[ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html)。各タイプは基本モデルの[Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)から共通プロパティを継承し、以下の追加プロパティを持ちます。

{% alert tip %}
Content Cardsのデータをログに記録するには、[分析のログ記録]({{site.baseurl}}/developer_guide/content_cards/logging_analytics)を参照してください。
{% endalert %}

### 基本カードモデル {#base-card-model}

すべてのContent Cardsには以下の共通プロパティがあります:

| プロパティ | 説明 |
|---|---|
| `expiresAt` | カードの有効期限のUNIXタイムスタンプ。|
| `extras`| （オプション）値が文字列の文字列オブジェクトとしてフォーマットされたキーと値のペアデータ。 |
| `id` | （オプション）カードのID。分析目的でイベントとともにBrazeに報告されます。 |
| `pinned` | このプロパティは、カードがダッシュボードで「ピン留め」として設定されたかどうかを反映します。|
| `updated` | このカードが最後に変更されたUNIXタイムスタンプ。 |
| `viewed` | このプロパティは、ユーザーがカードを閲覧したかどうかを反映します。|
| `isControl` | このプロパティは、カードがA/Bテスト内の「コントロール」グループである場合に`true`になります。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="基本カードモデル" }

### 画像のみ {#image-only}

[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)カードは、クリック可能なフルサイズの画像です。

| プロパティ | 説明 |
|---|---|
| `aspectRatio` | カード画像のアスペクト比で、画像の読み込みが完了する前のヒントとして機能します。特定の状況ではこのプロパティが提供されない場合があります。 |
| `categories` | このプロパティは、カスタム実装における整理のためだけに使用されます。これらのカテゴリーはダッシュボードのコンポーザーで設定できます。 |
| `clicked` | このプロパティは、このデバイスでこのカードがクリックされたことがあるかどうかを示します。 |
| `created` | Brazeからのカード作成時刻のUNIXタイムスタンプ。 |
| `dismissed` | このプロパティは、このカードが非表示にされたかどうかを示します。 |
| `dismissible` | このプロパティは、ユーザーがカードを非表示にして表示から削除できるかどうかを反映します。 |
| `imageUrl` | カード画像のURL。|
| `linkText` | URLの表示テキスト。 |
| `url` | カードがクリックされた後に開かれるURL。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="画像のみ" }

### キャプション付き画像 {#captioned-image}

[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)カードは、説明テキストを伴うクリック可能なフルサイズの画像です。

| プロパティ | 説明 |
|---|---|
| `aspectRatio` | カード画像のアスペクト比で、画像の読み込みが完了する前のヒントとして機能します。特定の状況ではこのプロパティが提供されない場合があります。 |
| `categories` | このプロパティは、カスタム実装における整理のためだけに使用されます。これらのカテゴリーはダッシュボードのコンポーザーで設定できます。 |
| `clicked` | このプロパティは、このデバイスでこのカードがクリックされたことがあるかどうかを示します。 |
| `created` | Brazeからのカード作成時刻のUNIXタイムスタンプ。 |
| `dismissed` | このプロパティは、このカードが非表示にされたかどうかを示します。 |
| `dismissible` | このプロパティは、ユーザーがカードを非表示にして表示から削除できるかどうかを反映します。 |
| `imageUrl` | カード画像のURL。|
| `linkText` | URLの表示テキスト。 |
| `title` | このカードのタイトルテキスト。 |
| `url` | カードがクリックされた後に開かれるURL。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="キャプション付き画像" }

### クラシック {#classic}

[ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html)モデルは、テキストなしの画像、または画像付きのテキストを含むことができます。

| プロパティ | 説明 |
|---|---|
| `aspectRatio` | カード画像のアスペクト比で、画像の読み込みが完了する前のヒントとして機能します。特定の状況ではこのプロパティが提供されない場合があります。 |
| `categories` | このプロパティは、カスタム実装における整理のためだけに使用されます。これらのカテゴリーはダッシュボードのコンポーザーで設定できます。 |
| `clicked` | このプロパティは、このデバイスでこのカードがクリックされたことがあるかどうかを示します。 |
| `created` | Brazeからのカード作成時刻のUNIXタイムスタンプ。 |
| `description` | このカードの本文テキスト。 |
| `dismissed` | このプロパティは、このカードが非表示にされたかどうかを示します。 |
| `dismissible` | このプロパティは、ユーザーがカードを非表示にして表示から削除できるかどうかを反映します。 |
| `imageUrl` | カード画像のURL。|
| `linkText` | URLの表示テキスト。 |
| `title` | このカードのタイトルテキスト。 |
| `url` | カードがクリックされた後に開かれるURL。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="クラシック" }

### 画像フォーマット {#image-formats}

Content Cardsの画像（GIFを含む）は、標準のHTML `<img>` タグを使用してレンダリングされます。GIFのサポートはユーザーのブラウザ機能に依存し、Web SDKの最小バージョンは必要ありません。すべてのモダンブラウザはGIF再生をネイティブにサポートしています。

## コントロールグループ {#control-group}

デフォルトのContent Cardsフィードを使用している場合、インプレッションとクリックは自動的に追跡されます。

Content Cardsのカスタム統合を使用している場合、コントロールカードが表示されたであろうタイミングで[インプレッションを記録する]({{site.baseurl}}/developer_guide/content_cards/logging_analytics)必要があります。この際、A/Bテストでインプレッションを記録する場合はコントロールカードを必ず処理するようにしてください。これらのカードは空白であり、ユーザーには表示されませんが、コントロールカード以外のカードとのパフォーマンスを比較するために、インプレッションを記録する必要があります。

Content CardがA/Bテストのコントロールグループに属しているかどうかを判定するには、`card.isControl`プロパティ（Web SDK v4.5.0以降）を確認するか、カードが`ControlCard`インスタンスであるかどうか（`card instanceof braze.ControlCard`）を確認してください。

## カードメソッド {#card-methods}

### デフォルトフィードメソッド {#default-feed-methods}

BrazeのデフォルトフィードのUIを使用してContent Cardsを表示する場合は、以下のメソッドを使用します。

|メソッド | 説明 |
|---|---|
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| デフォルトのContent Cardsフィードを表示します。指定された`parentNode` HTML要素にカードをレンダリングするか、要素が指定されていない場合は固定位置のサイドバーとして表示します。表示前にカードのソートやフィルタリングを行うためのオプションの`filterFunction`を受け取ります。 |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| デフォルトのContent Cardsフィードが現在表示されている場合、それを非表示にします。 |
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| デフォルトのContent Cardsフィードが非表示の場合は表示し、表示中の場合は非表示にします。複数のContent Cardsフィードを同時に表示する必要がある場合は、代わりに`showContentCards`と`hideContentCards`を使用してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="デフォルトフィードメソッド" }

### カスタムフィードメソッド {#custom-feed-methods}

独自のContent Cards UIを構築する場合は、以下のメソッドを使用します。

|メソッド | 説明 |
|---|---|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| セッション開始時など、現在のユーザーのContent Cardsが更新されるたびに呼び出されるコールバック関数を登録します。カスタムフィード用のカードデータを受け取るための主要な方法として使用します。初回セッションの更新を受け取るには、`openSession()`の前に呼び出す必要があります。 |
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)| 最新のContent Cardsリフレッシュから現在利用可能なすべてのカードを返します。新しいサーバーリクエストを待たずにページ読み込み時にカードを即座に表示する場合に使用します。たとえば、アクティブなセッション中にユーザーがページに戻った場合などです。 |
|[`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh)| BrazeサーバーからのContent Cardsの即時リフレッシュをリクエストします。デフォルトでは、カードはセッション開始時およびデフォルトフィードが再度開かれた時にリフレッシュされます。特定のユーザーアクションの後など、他のタイミングでリフレッシュを強制するために使用します。[レート制限]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#rate-limit)にご注意ください。 |
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| カードの配列に対してインプレッションイベントをログに記録します。カードがレンダリングされ、ユーザーに表示された時に呼び出します。カスタムUIを使用する場合、デフォルトフィード外ではインプレッションが自動的に追跡されないため、正確なキャンペーンレポートに必要です。 |
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| 単一のカードに対してクリックイベントをログに記録します。カスタムUI内でユーザーがカードを操作した時に呼び出します。デフォルトフィード外ではクリックが自動的に追跡されないため、正確なキャンペーンレポートに必要です。 |
|[`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction)| カードのURLを処理し、設定されたクリック時のアクション（Brazeアクション（`brazeActions://` URL）および標準URLナビゲーションを含む）を実行します。カードのクリックハンドラーでこのメソッドを呼び出して、Brazeダッシュボードで設定されたクリック時の動作が確実に実行されるようにします。 |
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)| カードをプログラムで非表示にし、ユーザーのフィードから削除します。カスタムUIでユーザーがカードを非表示にできるようにするために使用します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタムフィードメソッド" }

詳細については、[SDKリファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)を参照してください。

## ベストプラクティス {#best-practices}

### メソッドを正しい順序で呼び出す {#call-methods-in-the-correct-order}

カスタムフィードの場合、Content Cardsは`subscribeToContentCardsUpdates()`が`openSession()`より前に呼び出された場合にのみ、セッション開始時にリフレッシュされます。Brazeのメソッドは次の順序で呼び出してください：

```javascript
import * as braze from "@braze/web-sdk";

// Step 1: Initialize the SDK
braze.initialize("YOUR-API-KEY", { baseUrl: "YOUR-SDK-ENDPOINT" });

// Step 2: Subscribe to card updates
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  renderCards(cards);
});

// Step 3: Identify the user
braze.changeUser("USER_ID");

// Step 4: Start the session
braze.openSession();
```

### キャッシュされたカードを使用してページ読み込み間でコンテンツを保持する {#use-cached-cards-to-persist-content-across-page-loads}

`subscribeToContentCardsUpdates()`は新しい更新がある場合（セッション開始時など）にのみコールバックを呼び出すため、ユーザーがセッション中にページを更新するとカスタムフィードからカードが消えることがあります。これを防ぐには、`getCachedContentCards()`を使用してローカルキャッシュからすぐにカードをレンダリングし、新しい更新のサブスクリプションと併用してください：

```javascript
import * as braze from "@braze/web-sdk";

function renderCards(cards) {
  const container = document.getElementById("content-cards");
  container.textContent = "";
  const displayedCards = [];

  cards.forEach(card => {
    if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      const cardElement = document.createElement("div");

      const h3 = document.createElement("h3");
      h3.textContent = card.title || "";
      cardElement.appendChild(h3);

      const p = document.createElement("p");
      p.textContent = card.description || "";
      cardElement.appendChild(p);

      if (card.imageUrl) {
        const img = document.createElement("img");
        img.src = card.imageUrl;
        img.alt = card.title || "";
        cardElement.appendChild(img);
      }

      if (card.url) {
        cardElement.addEventListener("click", () => {
          braze.logContentCardClick(card);
          braze.handleBrazeAction(card.url);
        });
      }

      container.appendChild(cardElement);
      displayedCards.push(card);
    }
  });

  if (displayedCards.length > 0) {
    braze.logContentCardImpressions(displayedCards);
  }
}

// Display cached cards immediately
const cached = braze.getCachedContentCards();
if (cached && cached.cards.length > 0) {
  renderCards(cached.cards);
}

// Subscribe to future updates
braze.subscribeToContentCardsUpdates((updates) => {
  renderCards(updates.cards);
});
```

### カスタムフィードの分析をログに記録する {#log-analytics-for-custom-feeds}

カスタムUIを使用している場合、インプレッション、クリック、非表示は自動的にトラッキングされません。各イベントを手動でログに記録する必要があります：

- **インプレッション：** カードがユーザーに表示されたときに、カードオブジェクトの配列を渡して`logContentCardImpressions([card1, card2, ...])`を呼び出します。
- **クリック：** ユーザーがカードを操作したときに`logContentCardClick(card)`を呼び出します。
- **クリック時の動作：** カードに設定されたクリック時のアクション（URLへのナビゲーションやカスタムイベントのログ記録など）を実行するために`handleBrazeAction(card.url)`を呼び出します。

{% alert warning %}
`logContentCardClick()`に渡す引数は、オリジナルのBraze `Card`オブジェクトである必要があります。カードデータを変換または再構築した場合（シリアライズとデシリアライズなど）、クリックはログに記録されず、「card must be a Card object.」というエラーが表示されます。
{% endalert %}

## Google Tag Managerの使用 {#using-google-tag-manager}

Google Tag Managerは、[Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn)（Web SDKのバージョン）をWebサイトのコードに直接挿入することで動作します。つまり、Content Cardsの実装を除き、Google Tag Managerを使用せずにSDKを統合した場合と同様に、すべてのSDKメソッドを利用できます。

### Content Cardsの設定 {#setting-up-content-cards}

{% tabs local %}
{% tab Google Tag Manager %}
Content Cardsフィードの標準的な統合には、Google Tag Managerで**カスタムHTML**タグを使用できます。カスタムHTMLタグに以下を追加すると、標準のContent Cardsフィードが有効になります。

```html
<script>
   window.braze.showContentCards();
</script>
```

![Content Cardsフィードを表示するカスタムHTMLタグのGoogle Tag Managerでのタグ設定。]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab 手動 %}
Content Cardsとそのフィードの外観をより自由にカスタマイズするには、Content CardsをネイティブWebサイトに直接統合できます。このアプローチには、標準フィードUIを使用する方法とカスタムフィードUIを作成する方法の2つがあります。

{% subtabs local %}
{% subtab 標準フィード %}
[標準フィードUI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration#standard-feed-ui)を実装する場合、Brazeメソッドの先頭に`window.`を追加する必要があります。たとえば、`braze.showContentCards`は`window.braze.showContentCards`にする必要があります。
{% endsubtab %}

{% subtab カスタムフィード %}
[カスタムフィード]({{site.baseurl}}/developer_guide/content_cards/creating_cards)のスタイリングについては、GTMなしでSDKを統合した場合と同じ手順です。たとえば、Content Cardsフィードの幅をカスタマイズしたい場合は、CSSファイルに以下を貼り付けます。

{% raw %}
```css
body .ab-feed {
    width: 800px;
}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### テンプレートのアップグレード {#upgrading}

Braze Web SDKの最新バージョンにアップグレードするには、Google Tag Managerダッシュボードで以下の3つのステップを実行します。

1. **タグテンプレートの更新**<br>ワークスペース内の**テンプレート**ページに移動します。更新が利用可能であることを示すアイコンが表示されます。<br><br>![更新が利用可能であることを示すテンプレートページ]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>そのアイコンをクリックし、変更内容を確認した後、**Accept Update**をクリックします。<br><br>![新旧のタグテンプレートを比較する画面と「Accept Update」ボタン]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **バージョン番号の更新**<br>タグテンプレートが更新されたら、Braze初期化タグを編集し、SDKバージョンを最新の`major.minor`バージョンに更新します。たとえば、最新バージョンが`4.1.2`の場合、`4.1`と入力します。SDKバージョンの一覧は[変更履歴](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)で確認できます。<br><br>![SDKバージョンを変更するための入力フィールドがあるBraze初期化テンプレート]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **QAと公開**<br>タグコンテナへの更新を公開する前に、Google Tag Managerの[デバッグツール](https://support.google.com/tagmanager/answer/6107056?hl=en)を使用して新しいSDKバージョンが正常に動作していることを確認します。

### トラブルシューティング {#troubleshooting}

#### タグデバッグの有効化 {#debugging}

各Brazeタグテンプレートには、オプションの**GTM Tag Debugging**チェックボックスがあり、Webページの JavaScript コンソールにデバッグメッセージをログ出力するために使用できます。

![Google Tag Managerのデバッグツール]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### デバッグモードへの切り替え {#enter-debug-mode}

Google Tag Manager統合のデバッグに役立つもう1つの方法は、Googleの[プレビューモード](https://support.google.com/tagmanager/answer/6107056)機能を使用することです。

これにより、Webページのデータレイヤーから各トリガーされたBrazeタグに送信される値を特定でき、どのタグがトリガーされたか、またはトリガーされなかったかを確認できます。

![Braze初期化タグの概要ページでは、どのタグがトリガーされたかなどのタグに関する情報の概要が表示されます。]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### カスタムイベントのタグシーケンスの確認 {#tag-sequencing}

カスタムイベントやその他のアクションがBrazeにログ記録されない場合、よくある原因は、アクションタグ（**Custom Event**や**Purchase**など）が**Braze Initialization**タグの完了前に発火する競合です。これを修正するには、GTMで[タグシーケンス](https://support.google.com/tagmanager/answer/6238868)を設定します。

1. 正しくログ記録されていないアクションタグを開きます。
2. **Advanced Settings** > **Tag Sequencing**で、**A tag that fires before \[this tag\]**を選択します。
3. セットアップタグとして**Braze Initialization**タグを選択します。

これにより、アクションタグがBrazeにデータを送信する前に、SDKが完全に初期化されます。

#### 詳細ログの有効化 {#enable-verbose-logging}

トラブルシューティングのために詳細なログをキャプチャするには、Google Tag Manager統合で詳細ログを有効にできます。これらのログはブラウザの[開発者ツール](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)の**Console**タブに表示されます。

Google Tag Manager統合で、Braze初期化タグに移動し、**Enable Web SDK Logging**を選択します。

![Web SDKログを有効にするオプションがオンになっているBraze初期化タグの概要ページ。]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md