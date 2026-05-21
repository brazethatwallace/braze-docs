{% multi_lang_include developer_guide/prerequisites/android.md %}

## HTMLメッセージについて {#about-html-messages}

Braze JavaScriptインターフェイスを使用すると、アプリ内のカスタムWebViewでBrazeを活用できます。[`InAppMessageJavascriptInterface`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.jsinterface/-in-app-message-javascript-interface/index.html)は以下の役割を担います。

1. [ユーザーガイド：HTMLアプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages)に記載されているように、WebViewにBraze JavaScriptブリッジを挿入します。
2. WebViewから受け取ったブリッジメソッドを[Braze Android SDK](https://github.com/braze-inc/braze-android-sdk)に渡します。

## WebViewへのインターフェイスの追加 {#adding-the-interface-to-a-webview}

アプリのWebViewからBraze機能を使用するには、WebViewにBraze JavaScriptインターフェイスを追加します。インターフェイスが追加されると、[ユーザーガイド：HTMLアプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages)で利用可能な同じAPIがカスタムWebView内でも利用できるようになります。

{% tabs %}
{% tab JAVA %}

```java
String javascriptString = BrazeFileUtils.getAssetFileStringContents(context.getAssets(), "braze-html-bridge.js");
myWebView.loadUrl("javascript:" + javascriptString);

final InAppMessageJavascriptInterface javascriptInterface = new InAppMessageJavascriptInterface(context, inAppMessage);
myWebView.addJavascriptInterface(javascriptInterface, "brazeInternalBridge");
```

{% endtab %}
{% tab KOTLIN %}

`````````kotlin
val javascriptString = context.assets.getAssetFileStringContents("braze-html-bridge.js")
myWebView.loadUrl("javascript:" + javascriptString!!)

val javascriptInterface = InAppMessageJavascriptInterface(context, inAppMessage)
myWebView.addJavascriptInterface(javascriptInterface, "brazeInternalBridge")
```

{% endtab %}
{% endtabs %}

## YouTubeコンテンツの埋め込み {#embedding-youtube-content}

YouTubeやその他のHTML5コンテンツは、HTMLアプリ内メッセージで再生できます。これには、アプリ内メッセージが表示されるアクティビティでハードウェアアクセラレーションが有効になっている必要があります。詳細については、[Android開発者ガイド](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling)を参照してください。ハードウェアアクセラレーションは、Android APIバージョン11以降でのみ利用できます。

以下は、HTMLスニペットにYouTube動画を埋め込んだ例です。

`````````html
<body>
    <div class="box">
        <div class="relativeTopRight">
            <a href="appboy://close">X</a>
        </div>
        <iframe width="60%" height="50%" src="https://www.youtube.com/embed/_x45EB3BWqI" title="YouTube video player">
        </iframe>
    </div>
</body>
```

## ディープリンクの使用 {#using-deep-links}

AndroidのHTMLアプリ内メッセージでディープリンクや外部リンクを使用する場合、JavaScriptで`brazeBridge.closeMessage()`を呼び出さ**ないでください**。SDKの内部ロジックは、リンクにリダイレクトする際にアプリ内メッセージを自動的に閉じます。`brazeBridge.closeMessage()`を呼び出すとこのプロセスが妨げられ、ユーザーがアプリに戻った際にメッセージが応答しなくなる可能性があります。

以下は、コードスニペットにおけるディープリンクの例です。

{% raw %}
`````````javascript
<script>
document.querySelectorAll('[data-button-id]').forEach(function (node)
Unknown macro: { node.addEventListener('click', function () { brazeBridge.logClick(node.dataset.buttonId); brazeBridge.closeMessage(); }); }
);
</script>
```
{% endraw %}