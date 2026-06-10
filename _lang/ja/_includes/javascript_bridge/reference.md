カスタムHTMLアプリ内メッセージとバナーは、Braze SDKと連携するためのJavaScript「ブリッジ」をサポートしており、ユーザーがリンク付き要素をクリックしたり、コンテンツと何らかの形でエンゲージメントを行った際に、カスタムBrazeアクションをトリガーできます。これらのメソッドは、グローバル変数`brazeBridge`または`appboyBridge`とともに存在します。

{% alert important %}
Brazeでは、グローバル変数`brazeBridge`の使用を推奨しています。グローバル変数`appboyBridge`は非推奨ですが、既存のユーザー向けに引き続き機能します。`appboyBridge`を使用している場合は、`brazeBridge`に移行することをお勧めします。<br><br>`appboyBridge`は以下のSDKバージョンで非推奨となりました：<br><br>
- Web：[3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android：[14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS：[4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

例えば、カスタム属性とカスタムイベントをログに記録し、メッセージを閉じるには、カスタムHTML内で以下のJavaScriptを使用できます：

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    brazeBridge.logClick("0");
    // Set the user's custom attribute
    brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close the message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

### JavaScriptブリッジメソッド {#bridge}

アプリ内メッセージとバナーのカスタムHTMLでは、以下のJavaScriptメソッドがサポートされています：

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% multi_lang_include archive/appboyBridge.md %}

### ボタンクリックのトラッキング {#button-click-tracking}

カスタムHTML内のクリックをトラッキングするには、`brazeBridge.logClick(button_id)`メソッドを使用します。

{% alert note %}
**バナー：**引数なしの`brazeBridge.logClick()`のみがサポートされています。ボタンIDとカスタムボタントラッキングは、アプリ内メッセージでのみサポートされています。
{% endalert %}

アプリ内メッセージでは、`brazeBridge.logClick('0')`、`brazeBridge.logClick('1')`、`brazeBridge.logClick()`を使用して、それぞれ「ボタン1」、「ボタン2」、「本文クリック」をプログラムでトラッキングできます。

| クリック | メソッド | サポート |
| ---------- | ---------------------------- | --------- |
| 本文クリック | `brazeBridge.logClick()` | アプリ内メッセージとバナー |
| ボタン1 | `brazeBridge.logClick('0')` | アプリ内メッセージのみ |
| ボタン2 | `brazeBridge.logClick('1')` | アプリ内メッセージのみ |
| カスタムボタントラッキング | `brazeBridge.logClick('your custom name here')` | アプリ内メッセージのみ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ボタンクリックのトラッキング" }

アプリ内メッセージでは、1回のインプレッションごとに複数のボタンクリックイベントをトラッキングできます。例えば、メッセージを閉じてボタン2のクリックを記録するには：

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
```

また、新しいカスタムボタン名をトラッキングすることもできます（Campaignあたり最大100個のユニークな名前）。例えば、`brazeBridge.logClick('blue button')`や`brazeBridge.logClick('viewed carousel page 3')`などです。

{% alert tip %}
`onclick`属性内でJavaScriptメソッドを使用する場合、ダブルクォートで囲まれたHTML属性との衝突を避けるため、文字列値はシングルクォートで囲んでください。
{% endalert %}

#### 制限事項（アプリ内メッセージのみ） {#limitations-in-app-messages-only}

- Campaignあたり最大100個のユニークなボタンIDを設定できます。
- ボタンIDはそれぞれ最大255文字です。
- ボタンIDには、英字、数字、スペース、ダッシュ、およびアンダースコアのみを使用できます。