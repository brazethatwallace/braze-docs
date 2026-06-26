---
nav_title: "カスタムHTML"
article_title: "カスタムHTML"
page_order: 4
page_type: reference
description: "この記事では、カスタムコードのアプリ内メッセージについて、JavaScriptメソッド、ボタントラッキング、BrazeでのインタラクティブHTMLプレビューの使用方法を含めて概要を説明します。"
channel:
  - in-app messages
---

# カスタムHTMLアプリ内メッセージ {#custom-html-messages}

> 標準のアプリ内メッセージはさまざまな方法でカスタマイズできますが、HTML、CSS、JavaScriptを使用してデザイン・構築されたメッセージを使用することで、Campaignsの外観と操作感をさらに細かくコントロールできます。シンプルな構成で、あらゆるニーズに合わせたカスタム機能やブランディングを実現できます。

このメッセージタイプは[従来のエディター]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)で利用できます。

## 仕組み {#how-it-works}

HTMLアプリ内メッセージでは、以下を含むメッセージの外観と操作感をより細かくコントロールできます。

- カスタムフォントとスタイル
- 動画
- 複数の画像
- クリック時の動作
- インタラクティブコンポーネント
- カスタムアニメーション

カスタムHTMLメッセージでは、[JavaScript Bridge](#javascript-bridge)メソッドを使用して、イベントの記録、カスタム属性の設定、メッセージを閉じるなどの操作が可能です。HTMLアプリ内メッセージの使用方法やカスタマイズ方法の詳細な手順、およびHTML5アプリ内メッセージテンプレートのセットについては、[GitHubリポジトリ](https://github.com/braze-inc/in-app-message-templates)をご覧ください。

{% alert note %}
Web SDKでHTMLアプリ内メッセージを有効にするには、Brazeに`allowUserSuppliedJavascript`初期化オプションを指定する必要があります。例：`braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`。これはセキュリティ上の理由によるもので、HTMLアプリ内メッセージはJavaScriptを実行できるため、サイト管理者が有効化する必要があります。
{% endalert %}

## JavaScript bridge {#javascript-bridge}

{% include javascript_bridge/reference.md %}

## リンクベースのアクション {#link-based-actions}

カスタムJavaScriptに加えて、Braze SDKはこれらの便利なURLショートカットを使用して分析データを送信することもできます。これらのクエリパラメーターとURLスキームはすべて大文字と小文字が区別されることに注意してください。

### ボタンクリックトラッキング（非推奨） {#button-click-tracking-deprecated}

{% alert warning %}
`abButtonID`の使用は、[プレビュー付きHTML]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/#html-upload-with-preview/)メッセージタイプではサポートされていません。詳細については、[アップグレードガイド]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/#html-upload-with-preview)をご覧ください。
{% endalert %}

アプリ内メッセージ分析のボタンクリックを記録するには、任意のディープリンク、リダイレクトURL、またはアンカー要素`<a>`にクエリパラメーターとして`abButtonId`を追加します。「ボタン1」のクリックを記録するには`?abButtonId=0`を、「ボタン2」のクリックを記録するには`?abButtonId=1`を使用します。

他のURLパラメーターと同様に、最初のパラメーターは疑問符`?`で始め、後続のパラメーターはアンパサンド`&`で区切る必要があります。

#### URLの例 {#example-urls}

- `https://example.com/?abButtonId=0` - ボタン1クリック
- `https://example.com/?abButtonId=1` - ボタン2クリック
- `https://example.com/?utm_source=braze&abButtonId=0` - 他の既存URLパラメーターを含むボタン1クリック
- `myApp://deep-link?page=home&abButtonId=1` - ボタン2クリック付きモバイルディープリンク
- `<a href="https://example.com/?abButtonId=1">` - ボタン2クリック付きアンカー要素`<a>`

{% alert note %}
アプリ内メッセージはボタン1とボタン2のクリックのみをサポートしています。これら2つのボタンIDのいずれも指定しないURLは、一般的な「ボディクリック」として記録されます。
{% endalert %}

### リンクを新しいウィンドウで開く（モバイルのみ） {#open-link-in-new-window-mobile-only}

アプリ外のリンクを新しいウィンドウで開くには、`?abExternalOpen=true`を設定します。リンクを開く前にメッセージは閉じられます。

ディープリンクの場合、Brazeは`abExternalOpen`の値に関係なくURLを開きます。

### ディープリンクとして開く（モバイルのみ） {#open-as-deeplink-mobile-only}

BrazeにHTTPまたはHTTPSリンクをディープリンクとして処理させるには、`?abDeepLink=true`を設定します。

このクエリ文字列パラメーターが存在しないか`false`に設定されている場合、Brazeはホストアプリ内の内部Webブラウザーでウェブリンクを開こうとします。

### アプリ内メッセージを閉じる {#close-in-app-message}

アプリ内メッセージを閉じるには、`brazeBridge.closeMessage()` JavaScriptメソッドを使用できます。

例えば、`<a onclick="brazeBridge.closeMessage()" href="#">閉じる</a>`はアプリ内メッセージを閉じます。

## プレビュー付きHTMLアップロード {#html-upload-with-preview}

カスタムHTMLアプリ内メッセージを作成する際、インタラクティブなコンテンツをBraze内で直接プレビューできます。

エディターのメッセージプレビューパネルには、メッセージに含まれるJavaScriptをレンダリングしたリアルなプレビューが表示されます。プレビューパネルから、ページネーションのクリック、フォームやアンケートの送信、JavaScriptアニメーションの視聴など、カスタムメッセージのプレビューと操作が可能です。

![ページをスワイプしてHTMLプレビューを操作する様子。]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
ダッシュボードでプレビュー中は、HTMLで使用する`brazeBridge` JavaScriptメソッドはユーザープロファイルを更新しません。
{% endalert %}

### SDKの要件 {#supported-sdk-versions}

アプリ内メッセージのHTMLプレビューを使用するには、以下の最小Braze SDKバージョンにアップグレードする必要があります。

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
このメッセージタイプは特定の新しいSDKバージョンでのみ受信できるため、サポートされていないSDKバージョンのユーザーにはメッセージが表示されません。ユーザー群の大部分がリーチ可能になった後にこのメッセージタイプを採用するか、アプリバージョンが要件を満たすユーザーのみをターゲットにすることを検討してください。[最新のアプリバージョンによるフィルタリング]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)の詳細をご覧ください。
{% endalert %}

### Campaignの作成 {#instructions}

モバイルアプリのユーザーが**カスタムコード**のアプリ内メッセージを受信するには、サポートされているSDKバージョンにアップグレードする必要があります。新しいBraze SDKバージョンに依存するCampaignsを開始する前に、[ユーザーにモバイルアプリのアップグレードを促す]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features/)ことをお勧めします。

#### アセットファイル {#asset-files}

HTMLアップロードでカスタムコードのアプリ内メッセージを作成する際、Campaignアセットを[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/)にアップロードして、メッセージ内で参照できます。

以下のファイルタイプがアップロードに対応しています。

| ファイルタイプ | ファイル拡張子 |
| :--------------- | :-------------------------------- |
| フォントファイル | `.ttf`、`.woff`、`.otf`、`.woff2` |
| SVG画像 | `.svg` |
| JavaScriptファイル | `.js` |
| CSSファイル | `.css` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アセットファイル" }

Brazeでは、以下の2つの理由からアセットをメディアライブラリにアップロードすることを推奨しています。

1. メディアライブラリ経由でCampaignに追加されたアセットにより、ユーザーがオフラインの場合やインターネット接続が不安定な場合でもメッセージを表示できます。
2. Brazeにアップロードされたアセットは、複数のCampaignsで再利用できます。

##### アセットファイルの追加 {#adding-asset-files}

Campaignに新規または既存のアセットを追加できます。

Campaignに新しいアセットを追加するには、ドラッグ＆ドロップセクションを使用してファイルをアップロードします。このセクションで追加されたアセットは、メディアライブラリにも自動的に追加されます。メディアライブラリに既にアップロード済みのアセットを追加するには、**Add from Media Library**を選択します。

アセットが追加されると、**Assets for this campaign**セクションに表示されます。

アセットのファイル名がローカルHTMLアセットのファイル名と一致する場合、自動的に置き換えられます（例：`cat.png`がアップロードされ、`<img src="cat.png" />`が存在する場合）。

それ以外の場合は、リストからアセットにカーソルを合わせ、<i class="fas fa-copy"></i> **Copy**を選択してファイルのURLをクリップボードにコピーします。次に、リモートアセットを参照する場合と同様に、コピーしたアセットURLをHTMLに貼り付けます。

### HTMLエディター {#html-editor}

HTMLで行った変更は、入力に応じてプレビューパネルに自動的にレンダリングされます。HTMLで使用する[`brazeBridge` JavaScript](#bridge)メソッドは、ダッシュボードでのプレビュー中はユーザープロファイルを更新しません。

{% alert tip %}
HTMLエディター内で<i class="fa-solid fa-magnifying-glass"></i> **Search**を選択すると、コード内を検索できます。
{% endalert %}

### ボタントラッキング {#button-tracking-improvements}

[`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/) JavaScriptメソッドを使用して、カスタムコードのアプリ内メッセージ内のパフォーマンスをトラッキングできます。これにより、`brazeBridge.logClick('0')`、`brazeBridge.logClick('1')`、または`brazeBridge.logClick()`を使用して、それぞれ「ボタン1」、「ボタン2」、「ボディクリック」をプログラムでトラッキングできます。

| クリック | メソッド |
| ---------- | ---------------------------- |
| Button 1   | `brazeBridge.logClick('0')` |
| Button 2   | `brazeBridge.logClick('1')` |
| Body click | `brazeBridge.logClick()`    |
| カスタムボタントラッキング | `brazeBridge.logClick('your custom name here')` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ボタントラッキング" }

{% alert note %}
このボタントラッキング方法は、以前の自動クリックトラッキング方法（`?abButtonId=0`など）に代わるもので、それらは削除されました。
{% endalert %}

トラッキング対象のボタンが3つ以上必要な場合は、プレビュー付きHTMLメッセージで[`brazeBridge.logClick(button_id)`](#button-tracking-improvements)を使用します。ボタン1とボタン2はそれぞれ`'0'`と`'1'`にマッピングされ、追加のボタンにはカスタムIDを使用します（Campaignあたり最大100個のユニークID）。ボタンIDの文字制限については、[ボタントラッキング](#button-tracking-improvements)を参照してください。

### カスタムHTMLリンクと閉じる動作のトラブルシューティング {#troubleshoot-custom-html-links-and-close-behavior}

#### ボタンクリックでリンクが開かない {#button-clicks-do-not-open-the-link}

カスタムHTMLアプリ内メッセージのボタンがクリックしても読み込まれない場合は、リンクが有効なURLまたはサポートされているディープリンクスキームを使用しているか確認してください。不正なURLやサポートされていないカスタムスキームは、クリックアクションの完了を妨げる可能性があります。

#### メッセージを閉じる際のボディクリック {#body-clicks-when-closing-the-message}

`brazeBridge.closeMessage()`を呼び出すとメッセージは閉じられますが、それ自体では分析を記録しません。ユーザーがメッセージを閉じる際にボディクリックを記録するには、`brazeBridge.closeMessage()`の前に`brazeBridge.logClick()`を呼び出して、プラットフォーム間でクリックログの一貫性を保ちます。

### 後方互換性のない変更 {#backward-incompatible-changes}

1. この新しいメッセージタイプで最も注目すべき互換性のない変更は、SDKの要件です。アプリのSDKが最小[SDKバージョン要件](#supported-sdk-versions)を満たしていないユーザーにはメッセージが表示されません。
2. 以前モバイルアプリでサポートされていた`braze://close`ディープリンクは、JavaScript `brazeBridge.closeMessage()`に置き換えられ削除されました。これにより、Webがディープリンクをサポートしていないため、クロスプラットフォームのHTMLメッセージが可能になります。
3. ボタンIDに`?abButtonId=0`を使用していた自動クリックトラッキングと、閉じるボタンの「ボディクリック」トラッキングは削除されました。以下のコード例は、新しいクリックトラッキングJavaScriptメソッドを使用するようにHTMLを変更する方法を示しています。

   | 導入前 | 導入後 |
   |:-------- |:------------|
   |<code>&lt;a href="braze://close"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="braze://close?abButtonId=0"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="app://deeplink?abButtonId=0">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="app://deeplink" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "braze://close?abButtonId=1"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|
{: .reset-td-br-1 .reset-td-br-2 aria-label="後方互換性のない変更" }