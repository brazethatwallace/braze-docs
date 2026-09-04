{% multi_lang_include developer_guide/prerequisites/web.md %} しかし、追加の設定は必要ない。

## メッセージタイプ {#message-types}

すべてのアプリ内メッセージは、[`InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)からプロトタイプを継承しており、すべてのアプリ内メッセージの基本的な動作と特性を定義しています。プロトタイプのサブクラスには、[`SlideUpMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html)、[`ModalMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html)、[`FullScreenMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html)、および[`HtmlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html)があります。

各アプリ内メッセージタイプは、コンテンツ、画像、アイコン、クリックアクション、分析、表示、配信をカスタマイズできます。

{% tabs %}
{% tab スライドアップ %}

[`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html)アプリ内メッセージは、従来モバイルプラットフォームで画面の上部または下部から「スライドアップ」または「スライドダウン」することからこの名前が付けられています。Braze Web SDKでは、これらのメッセージはWebの主要なパラダイムに合わせて、GrowlまたはToastスタイルの通知として表示されます。画面のごく一部を覆い、効果的で邪魔にならないメッセージング機能を提供します。

![スマートフォン画面の下部からスライドするアプリ内メッセージ。「Humans are complicated. Custom engagement shouldn't be.」と表示されています。背景にはWebページの隅に表示された同じアプリ内メッセージが見えます。]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab モーダル %}

[`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html)アプリ内メッセージは画面の中央に表示され、半透明のパネルで囲まれています。より重要なメッセージングに適しており、クリックアクションと分析が有効な最大2つのボタンを配置できます。

![スマートフォン画面の中央に表示されるモーダルアプリ内メッセージ。「Humans are complicated. Custom engagement shouldn't be.」と表示されています。背景にはWebページの中央に表示された同じアプリ内メッセージが見えます。]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab フルスクリーン %}

[`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html)アプリ内メッセージは、ユーザーコミュニケーションのコンテンツとインパクトを最大化するのに適しています。狭いブラウザウィンドウ（モバイルWebなど）では、`full`アプリ内メッセージはブラウザウィンドウ全体を占めます。大きなブラウザウィンドウでは、`full`アプリ内メッセージは`modal`アプリ内メッセージと同様に表示されます。`full`アプリ内メッセージの上半分には画像が含まれ、下半分には最大8行のテキストと、クリックアクションおよび分析が有効な最大2つのボタンを配置できます。

![スマートフォンの画面全体に表示されるフルスクリーンアプリ内メッセージ。「Humans are complicated. Custom engagement shouldn't be.」と表示されています。背景にはWebページの中央に大きく表示された同じアプリ内メッセージが見えます。]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab カスタムHTML %}

[`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html)アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに適しています。ユーザー定義のHTMLはiFrame内に表示され、画像、フォント、動画、インタラクティブ要素などのリッチコンテンツを含めることができ、メッセージの外観と機能を完全にコントロールできます。HTML内からBraze Web SDKのメソッドを呼び出すためのJavaScript `brazeBridge`インターフェイスをサポートしています。詳細については[ベストプラクティス]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices)を参照してください。

{% alert important %}
Web SDKを通じてHTMLアプリ内メッセージを有効にするには、Brazeに`allowUserSuppliedJavascript`初期化オプションを指定する**必要があります**。例：`braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`。これはセキュリティ上の理由によるものです。HTMLアプリ内メッセージはJavaScriptを実行できるため、サイト管理者が有効にする必要があります。
{% endalert %}

以下の例は、ページ分割されたHTMLアプリ内メッセージを示しています。

![コンテンツのカルーセルとインタラクティブなボタンを含むHTMLアプリ内メッセージ。]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}