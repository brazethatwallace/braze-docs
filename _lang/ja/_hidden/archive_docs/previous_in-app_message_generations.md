---
nav_title: 前の世代
article_title: 以前のアプリ内メッセージ世代
page_order: 20
page_type: reference
description: "この記事では、Brazeのアプリ内メッセージに関する以前の情報を確認します。"
channel: in-app messages
noindex: true
hidden : true
---

# 以前のアプリ内メッセージ世代 {#previous-in-app-message-generations}

{% alert important %}
このページでは、アプリ内メッセージに関する以前の情報を確認します。最新のアプリ内メッセージ世代に関する最新情報については、現在の[アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/)ドキュメントを参照してください。
{% endalert %}

## ユニバーサル {#universal}

ここでは、アプリ内メッセージに関する以前の情報を確認します。最新のアプリ内メッセージ世代に関する最新情報については、[アプリ内メッセージ概要ドキュメント]({{site.baseurl}}/user_guide/channels/in_app_messages/)をご覧ください。

{% details Fullscreen %}
これらは最も魅力的ですが、ユーザーの画面全体を覆うため、最も侵入的でもあります。大きくリッチな画像を表示するのに適しており、重要な新機能や期限が迫っているプロモーションなど、非常に重要な情報を伝えるのに役立ちます。ユーザーエクスペリエンスへの影響が大きいため、最優先のコンテンツに対して控えめに使用してください。

![フルスクリーンメッセージ]({% image_buster /assets/img_archive/braze_fullscreen.png %}){: style="max-width:80%;"}

**カスタマイズ可能な機能**

- ヘッダーと本文のテキスト
- 大きな画像
- クリック時の動作とディープリンクが個別に設定可能なコールトゥアクションボタンを最大2つ
- ヘッダーと本文テキスト、ボタン、背景の色
- キーと値のペア

{% enddetails %}
{% details  Modal %}
これらのメッセージはフルスクリーンメッセージほど侵入的ではなく、ユーザーがアプリのUIの一部を引き続き見ることができます。モーダルメッセージにはボタンと画像が含まれているため、よりインタラクティブで視覚的なキャンペーンが必要な場合は、スライドアップよりもモーダルメッセージの方が適しています。アプリの更新や緊急ではないセールやイベントなど、中優先度のコンテンツに最適です。

![モーダルメッセージ]({% image_buster /assets/img_archive/braze_modal.png %}){: style="max-width:80%;"}

**カスタマイズ可能な機能**

- ヘッダーと本文のテキスト
- 画像またはカスタマイズ可能なバッジアイコン
- クリック時の動作とディープリンクが個別に設定可能なコールトゥアクションボタンを最大2つ
- ヘッダーと本文テキスト、ボタン、背景の色
- キーと値のペア

{% enddetails %}

{% details Traditional Slideup %}
これらは最も控えめなメッセージタイプですが、色やバッジアイコンの使用方法によっては、より目立つこともあります。新しいユーザーをオンボーディングし、特定のアプリ内機能に誘導する際に使用するメッセージ形式として適しています。アプリの体験を中断せず、継続的な探索が可能です。

![スライドアップメッセージ]({% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}){: style="max-width:50%;"}

**カスタマイズ可能な機能**

- 本文テキスト
- 画像またはカスタマイズ可能なバッジアイコン
- スライドアップの背景、テキスト、アイコンの色
- メッセージを閉じる動作
- スライドアップの位置（アプリ画面の上部または下部）
- キーと値のペア

{% enddetails %}

<br>

## Web

ここでは、よりカスタマイズされたアプリ内メッセージに関する以前の情報を確認します。最新のアプリ内メッセージ世代に関する最新情報については、[カスタマイズドキュメント]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/)をご覧ください。

{% details Email capture message %}
メールキャプチャメッセージを使用すると、サイトのユーザーにメールアドレスの送信を簡単に促すことができ、送信後はBrazeシステム内で利用可能になり、すべてのメッセージングキャンペーンで使用できます。

![メールキャプチャメッセージ]({% image_buster /assets/img_archive/web-email-capture.png %}){: style="max-width:60%;"}

>  Web SDKを介してメールキャプチャアプリ内メッセージを有効にするには、`allowUserSuppliedJavascript`初期化オプションをBrazeに指定する必要があります。例：`braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`。これはセキュリティ上の理由によるもので、HTMLアプリ内メッセージはJavaScriptを実行できるため、サイト管理者が有効にする必要があります。

**カスタマイズ可能な機能**

- ヘッダー、本文、および送信ボタンのテキスト
- オプションの画像
- オプションの「利用規約」リンク
- ヘッダーと本文テキスト、ボタン、背景の色
- キーと値のペア

{% enddetails %}

{% details Custom HTML Message %}

Brazeのデフォルトアプリ内メッセージはさまざまな方法でカスタマイズできますが、HTML、CSS、JavaScriptを使用してデザイン・構築されたメッセージを使用することで、キャンペーンのルック＆フィールをさらにコントロールできます。簡単な構成で、あらゆるニーズに合ったカスタム機能とブランディングを実現できます。HTMLアプリ内メッセージを使用すると、メッセージの外観と操作感をより細かくコントロールでき、HTML5でサポートされているものはすべてBrazeでもサポートされます。

**JavaScriptブリッジ（appboyBridge）**

HTMLアプリ内メッセージは、Braze Web SDKへのJavaScript「ブリッジ」インターフェイスをサポートしており、ユーザーがリンクを含む要素をクリックしたり、コンテンツを操作したりしたときに、カスタムBrazeアクションをトリガーできます。次のJavaScriptメソッドは、BrazeのHTMLアプリ内メッセージでサポートされています。

{% multi_lang_include archive/appboyBridge.md platform="web" %}

さらに、分析トラッキングのために、HTML内の`<a>`または`<button>`要素は、アプリ内メッセージに関連付けられたキャンペーンへの「クリック」アクションを自動的に記録します。「ボディクリック」の代わりに「ボタンクリック」を記録するには、リンクのhrefにクエリ文字列値abButtonIdを指定するか（例：`<a href="http://mysite.com?abButtonId=0">click me</a>`）、HTML要素にidを指定します（例：`<a id="0" href="http://mysite.com">click me</a>`）。現在受け入れられているボタンIDは「0」と「1」のみです。ボタンIDが0のリンクはダッシュボード上で「Button 1」として表示され、ボタンIDが1のリンクは「Button 2」として表示されます。

>  Web SDKを介してHTMLアプリ内メッセージを有効にするには、`allowUserSuppliedJavascript`初期化オプションをBrazeに指定する必要があります。例：`braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`。これはセキュリティ上の理由によるもので、HTMLアプリ内メッセージはJavaScriptを実行できるため、サイト管理者が有効にする必要があります。

{% enddetails %}

{% details HTML In App-Message Templates %}

すぐに使い始められるよう、HTML5アプリ内メッセージテンプレートのセットを設計しました。[GitHubリポジトリ](https://github.com/braze-inc/in-app-message-templates)をチェックして、これらのテンプレートをニーズに合わせて使用およびカスタマイズする方法の詳細な手順を確認してください。

**カスタマイズ可能な機能**

- フォント
- スタイル
- 画像 + 動画
- クリック時の動作
- インタラクティブコンポーネント

{% enddetails %}

<br>

## 仕様 {#specifications}

ここでは、アプリ内メッセージのクリエイティブ仕様に関する以前の情報を確認します。最新のアプリ内メッセージ世代に関する最新情報については、[クリエイティブ仕様ドキュメント]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/)をご覧ください。

### 文字数と画像の制限 {#character-and-image-limits}

次の表に記載されているすべてのアプリ内メッセージタイプについて、以下の追加ガイドラインが適用されます。

- **推奨画像サイズ：**500&nbsp;KB
- **最大画像サイズ：**5&nbsp;MB
- **サポートされているファイルタイプ：**PNG、JPEG、GIF

| タイプ | アスペクト比 | 最大文字数 |
| :--------------------------------- | :----------: | :-----------------: |
| ポートレート全画面（画像のみ） | 10:16 | 240 |
| ポートレート全画面（テキスト付き） | 5:4 | 240 |
| ランドスケープ全画面（テキスト付き） | 16:5 | 240 |
| ランドスケープ全画面（画像のみ） | 16:10 | 240 |
| スライドアップ | 1:1 | 140 |
| モーダル（画像のみ） | 1:1 | 140 |
| モーダル（テキスト付き） | 29:10 | 140 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Character and image limits" }

### アプリ内メッセージのファイルサイズを小さく保つ {#keeping-in-app-message-file-sizes-small}

Brazeでは、いくつかの理由から画像やHTMLアセットのZIPファイルをできるだけ小さく保つことをお勧めします。

- HTMLおよび画像メッセージのペイロードが小さいほど、より速くダウンロードされ、顧客にとってより迅速かつ確実に表示されます。
- HTMLと画像メッセージのペイロードを小さくすれば、顧客のデータコストも抑えられます。Brazeのアプリ内メッセージは、セッション開始時にバックグラウンドでダウンロードされるため、選択した任意の基準に基づいてリアルタイムでトリガーできます。その結果、1&nbsp;MBのHTMLアプリ内メッセージが10件ある場合、たとえそれらのメッセージをすべてトリガーしなかったとしても、顧客全員に10&nbsp;MBのデータ料金が発生します。アプリ内メッセージはキャッシュされ、セッションごとに再ダウンロードされないにもかかわらず、時間の経過とともにすぐに増加する可能性があります。

次の戦略は、ファイルサイズを小さく保つのに役立ちます。

- HTMLアセットZIPフォルダーにフォントファイルを含めるのではなく、アプリケーションやWebサイトに埋め込まれたフォントを参照して、HTMLアプリ内メッセージをカスタマイズします。
- HTMLアセットZIPに無関係または重複するCSSやJavaScriptが含まれないようにしてください。
- すべての画像に[ImageOptim](https://imageoptim.com/)を使用して、画質を落とさずに可能な限り最小のサイズに圧縮します。

### iPhone 5の仕様 {#iphone-5-specs}

![iPhone 5の仕様]({% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %})

### iPhone 6の仕様 {#iphone-6-specs}

![iPhone 6の仕様]({% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %})