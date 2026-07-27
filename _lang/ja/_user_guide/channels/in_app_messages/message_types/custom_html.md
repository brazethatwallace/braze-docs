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

> 標準のアプリ内メッセージはさまざまな方法でカスタマイズできますが、HTML、CSS、JavaScriptを使用してデザイン・構築されたメッセージを使用することで、キャンペーンの外観と操作感をさらに細かくコントロールできます。シンプルな構成で、あらゆるニーズに合わせたカスタム機能やブランディングを実現できます。

このメッセージタイプは[従来のエディター]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)で利用できます。

## 仕組み {#how-it-works}

HTMLアプリ内メッセージを使用すると、メッセージの外観をより細かくコントロールできます。以下のようなカスタマイズが可能です。

- カスタムフォントとスタイル
- 動画
- 複数の画像
- クリック時の動作
- インタラクティブなコンポーネント
- カスタムアニメーション

カスタムHTMLメッセージでは、[JavaScript Bridge](#javascript-bridge)のメソッドを使用して、イベントの記録、カスタム属性の設定、メッセージの閉じるなどの操作が可能です。HTMLアプリ内メッセージの使用方法やカスタマイズ方法の詳細な手順、およびすぐに使い始められるHTML5アプリ内メッセージテンプレートのセットについては、[GitHubリポジトリ](https://github.com/braze-inc/in-app-message-templates)をご覧ください。

{% alert note %}
Web SDKを通じてHTMLアプリ内メッセージを有効にするには、Brazeに`allowUserSuppliedJavascript`初期化オプションを指定する必要があります（例：`braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`）。これはセキュリティ上の理由によるもので、HTMLアプリ内メッセージはJavaScriptを実行できるため、サイト管理者が有効化する必要があります。
{% endalert %}

## JavaScript bridge {#javascript-bridge}

{% include javascript_bridge/reference.md %}

## リンクベースのアクション {#link-based-actions}

カスタムJavaScriptに加えて、Braze SDKは便利なURLショートカットを使用して分析データを送信することもできます。これらのクエリパラメーターとURLスキームはすべて大文字と小文字が区別されることに注意してください。

### ボタンクリックトラッキング（非推奨） {#button-click-tracking-deprecated}

{% alert warning %}
`abButtonID`の使用は、[プレビュー付きHTML]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#html-upload-with-preview)メッセージタイプではサポートされていません。詳細については、[アップグレードガイド]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#html-upload-with-preview)を参照してください。
{% endalert %}

アプリ内メッセージの分析でボタンクリックを記録するには、ディープリンク、リダイレクトURL、またはアンカー要素`<a>`にクエリパラメーターとして`abButtonId`を追加します。「Button 1」のクリックを記録するには`?abButtonId=0`を使用し、「Button 2」のクリックを記録するには`?abButtonId=1`を使用します。

他のURLパラメーターと同様に、最初のパラメーターは疑問符`?`で始め、後続のパラメーターはアンパサンド`&`で区切る必要があります。

#### URLの例 {#example-urls}

- `https://example.com/?abButtonId=0` - Button 1クリック
- `https://example.com/?abButtonId=1` - Button 2クリック
- `https://example.com/?utm_source=braze&abButtonId=0` - 他の既存のURLパラメーターを含むButton 1クリック
- `myApp://deep-link?page=home&abButtonId=1` - Button 2クリック付きモバイルディープリンク
- `<a href="https://example.com/?abButtonId=1">` - Button 2クリック付きアンカー要素`<a>`

{% alert note %}
アプリ内メッセージはButton 1とButton 2のクリックのみをサポートしています。これら2つのボタンIDのいずれも指定しないURLは、一般的な「ボディクリック」として記録されます。
{% endalert %}

### 新しいウィンドウでリンクを開く（モバイルのみ） {#open-link-in-new-window-mobile-only}

アプリ外のリンクを新しいウィンドウで開くには、`?abExternalOpen=true`を設定します。リンクを開く前にメッセージは閉じられます。

ディープリンクの場合、Brazeは`abExternalOpen`の値に関係なくURLを開きます。

### ディープリンクとして開く（モバイルのみ） {#open-as-deeplink-mobile-only}

BrazeにHTTPまたはHTTPSリンクをディープリンクとして処理させるには、`?abDeepLink=true`を設定します。

このクエリ文字列パラメーターが存在しないか`false`に設定されている場合、Brazeはホストアプリ内の内部Webブラウザーでウェブリンクを開こうとします。

### アプリ内メッセージを閉じる {#close-in-app-message}

アプリ内メッセージを閉じるには、`brazeBridge.closeMessage()`というJavaScriptメソッドを使用できます。

たとえば、`<a onclick="brazeBridge.closeMessage()" href="#">Close</a>`はアプリ内メッセージを閉じます。

## プレビュー付きHTMLアップロード {#html-upload-with-preview}

カスタムHTMLアプリ内メッセージを作成する際、インタラクティブなコンテンツをBraze内で直接プレビューできます。

エディターのメッセージプレビューパネルには、メッセージに含まれるJavaScriptをレンダリングしたリアルなプレビューが表示されます。プレビューパネルでは、ページネーションのクリック、フォームやアンケートの送信、JavaScriptアニメーションの確認など、カスタムメッセージのプレビューと操作が可能です。

![ページをスワイプしてHTMLプレビューを操作する様子。]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
HTMLで使用する`brazeBridge` JavaScriptメソッドは、ダッシュボードでのプレビュー中にユーザープロファイルを更新しません。
{% endalert %}

### キャンペーンの作成 {#instructions}

#### アセットファイル {#asset-files}

HTMLアップロードでカスタムコードのアプリ内メッセージを作成する際、キャンペーンアセットを[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)にアップロードして、メッセージ内で参照できます。

以下のファイルタイプがアップロードに対応しています：

| ファイルタイプ | ファイル拡張子 |
| :--------------- | :-------------------------------- |
| フォントファイル | `.ttf`, `.woff`, `.otf`, `.woff2` |
| SVG画像 | `.svg` |
| JavaScriptファイル | `.js` |
| CSSファイル | `.css` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アセットファイル" }

Brazeでは、以下の2つの理由からアセットをメディアライブラリにアップロードすることを推奨しています：

1. メディアライブラリ経由でキャンペーンに追加されたアセットにより、ユーザーがオフラインの場合やインターネット接続が不安定な場合でもメッセージを表示できます。
2. Brazeにアップロードされたアセットは、キャンペーン間で再利用できます。

##### アセットファイルの追加 {#adding-asset-files}

キャンペーンに新規または既存のアセットを追加できます。

キャンペーンに新しいアセットを追加するには、ドラッグ＆ドロップセクションを使用してファイルをアップロードします。このセクションで追加されたアセットは、メディアライブラリにも自動的に追加されます。既にメディアライブラリにアップロード済みのアセットを追加するには、**メディアライブラリから追加**を選択します。

アセットが追加されると、**このキャンペーンのアセット**セクションに表示されます。

アセットのファイル名がローカルHTMLアセットのファイル名と一致する場合、自動的に置き換えられます（例：`cat.png`がアップロードされ、`<img src="cat.png" />`が存在する場合）。

それ以外の場合は、リストからアセットにカーソルを合わせ、<i class="fas fa-copy"></i> **コピー**を選択してファイルのURLをクリップボードにコピーします。次に、リモートアセットを参照する場合と同様に、コピーしたアセットURLをHTMLに貼り付けます。

### HTMLエディター {#html-editor}

HTMLで行った変更は、入力に応じてプレビューパネルに自動的にレンダリングされます。HTMLで使用する[`brazeBridge` JavaScript](#bridge)メソッドは、ダッシュボードでのプレビュー中にユーザープロファイルを更新しません。

{% alert tip %}
HTMLエディター内で<i class="fa-solid fa-magnifying-glass" aria-label="検索"></i> **検索**を選択すると、コード内を検索できます。
{% endalert %}

### ボタントラッキング {#button-tracking-improvements}

[`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types) JavaScriptメソッドを使用して、カスタムコードのアプリ内メッセージ内のパフォーマンスをトラッキングできます。これにより、`brazeBridge.logClick('0')`、`brazeBridge.logClick('1')`、または`brazeBridge.logClick()`を使用して、それぞれ「ボタン1」、「ボタン2」、「ボディクリック」をプログラムでトラッキングできます。

| クリック | メソッド |
| ---------- | ---------------------------- |
| ボタン1 | `brazeBridge.logClick('0')` |
| ボタン2 | `brazeBridge.logClick('1')` |
| ボディクリック | `brazeBridge.logClick()` |
| カスタムボタントラッキング | `brazeBridge.logClick('your custom name here')` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ボタントラッキング #button-tracking-improvements" }

{% alert note %}
このボタントラッキング方法は、以前の自動クリックトラッキング方法（`?abButtonId=0`など）に代わるもので、それらは削除されました。
{% endalert %}

プレビュー付きHTMLメッセージで3つ以上のトラッキングボタンが必要な場合は、[`brazeBridge.logClick(button_id)`](#button-tracking-improvements)を使用します。ボタン1とボタン2は`'0'`と`'1'`にマッピングされ、追加のボタンにはカスタムIDを使用します（キャンペーンごとに最大100個のユニークID）。ボタンIDの文字制限については、[ボタントラッキング](#button-tracking-improvements)を参照してください。

### カスタムHTMLリンクと閉じる動作のトラブルシューティング {#troubleshoot-custom-html-links-and-close-behavior}

#### ボタンクリックでリンクが開かない {#button-clicks-do-not-open-the-link}

カスタムHTMLアプリ内メッセージのボタンがクリックしても読み込まれない場合は、リンクが有効なURLまたはサポートされているディープリンクスキームを使用しているか確認してください。不正なURLやサポートされていないカスタムスキームは、クリックアクションの完了を妨げる可能性があります。

#### メッセージを閉じる際のボディクリック {#body-clicks-when-closing-the-message}

`brazeBridge.closeMessage()`を呼び出すとメッセージは閉じますが、それ自体では分析を記録しません。ユーザーがメッセージを閉じる際にボディクリックを記録するには、`brazeBridge.closeMessage()`の前に`brazeBridge.logClick()`を呼び出して、プラットフォーム間でクリックログの一貫性を保ちます。

### 後方互換性のない変更 {#backward-incompatible-changes}

1. 以前モバイルアプリでサポートされていた`braze://close`ディープリンクは、JavaScript `brazeBridge.closeMessage()`に置き換えられ削除されました。これにより、Webがディープリンクをサポートしていないため、クロスプラットフォームのHTMLメッセージが可能になります。
2. ボタンIDに`?abButtonId=0`を使用した自動クリックトラッキングと、閉じるボタンの「ボディクリック」トラッキングは削除されました。以下のコード例は、新しいクリックトラッキングJavaScriptメソッドを使用するようにHTMLを変更する方法を示しています：

   | 変更前 | 変更後 |
   |:-------- |:------------|
   |<code>&lt;a href="braze://close"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="braze://close?abButtonId=0"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="app://deeplink?abButtonId=0">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="app://deeplink" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "braze://close?abButtonId=1"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|
{: .reset-td-br-1 .reset-td-br-2 aria-label="後方互換性のない変更 #backward-incompatible-changes" }