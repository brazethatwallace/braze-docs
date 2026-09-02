---
nav_title: ブラウザ拡張機能
article_title: Webのブラウザ拡張機能統合
platform: Web
page_order: 20
page_type: reference
description: "この記事では、Braze Web SDKをブラウザ拡張機能（Google Chrome、Firefox）内で使用する方法について説明します。"

---

# ブラウザ拡張機能 {#browser-extension}

> この記事では、Braze Web SDKをブラウザ拡張機能（Google Chrome、Firefox）内で使用する方法について説明します。

Braze Web SDKをブラウザ拡張機能内に統合し、分析を収集して、リッチなメッセージングをユーザーに表示します。これには、**Google Chrome Extensions**と**Firefox Add-Ons**の両方が含まれます。

## サポートされるもの {#whats-supported}

通常、拡張機能はHTMLおよびJavaScriptであるため、以下の用途にBrazeを使用できます。

* **分析**:カスタムイベント、属性をキャプチャし、拡張機能内のリピートユーザーの識別も行います。これらのプロファイル特性を使用して、クロスチャネルメッセージングを強化します。
* **アプリ内メッセージ**:ネイティブまたはカスタムのHTMLメッセージングを使用して、ユーザーが拡張機能内でアクションを取ったときにアプリ内メッセージをトリガーします。
* **Content Cards**:オンボーディングまたはプロモーションコンテンツ用に、拡張機能にネイティブカードのフィードを追加します。
* **Webプッシュ**:Webページが現在開かれていない場合でも、タイムリーに通知を送信します。

## サポートされていないもの {#whats-not-supported}

* サービスワーカー内からのBraze SDKの使用はサポートされていません。拡張機能のポップアップページや設定ページではBraze SDKを引き続き使用できます。{% multi_lang_include product_feedback_cta.md context="gap" feature="service worker support in the Braze Web SDK" %}

## 拡張機能の種類 {#extension-types}

Brazeは、拡張機能の以下の領域に含めることができます。

| エリア | 詳細 | サポートされるもの |
|--------|-------|------|
| ポップアップページ | [ポップアップ](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups)ページは、ブラウザのツールバーで拡張機能のアイコンをクリックするとユーザーに表示されるダイアログです。| 分析、アプリ内メッセージ、およびContent Cards |
| バックグラウンドスクリプト | [バックグラウンドスクリプト](https://developer.chrome.com/extensions/background_pages)（Manifest v2のみ）は、拡張機能でユーザーナビゲーションの調査および操作や、Webページの変更を行えるようにします（広告ブロッカーがページ上のコンテンツを検出および変更する方法など）。| 分析、アプリ内メッセージ、およびContent Cards。<br><br>バックグラウンドスクリプトはユーザーには表示されないため、メッセージングを行う場合は、メッセージを表示するときにブラウザのタブやポップアップページと通信する必要があります。|
| オプションページ | [オプションページ](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages)を使用すると、ユーザーは拡張機能内で設定を切り替えることができます。これは、新しいタブを開くスタンドアロンのHTMLページです。| 分析、アプリ内メッセージ、およびContent Cards |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 aria-label="拡張機能の種類" }

## 権限 {#permissions}

Braze SDK（`braze.min.js`）を拡張機能にバンドルされたローカルファイルとして統合する場合、`manifest.json`で追加の権限は必要ありません。

ただし、[Google Tag マネージャー]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/)を使用するか、外部URLからBraze SDKを参照するか、拡張機能に厳密なコンテンツセキュリティポリシーを設定した場合は、`manifest.json`の[`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy)設定を調整して、リモートスクリプトソースを許可する必要があります。

## はじめに {#getting-started}

{% alert tip %}
作業を始める前に、Web SDKの[初期SDK設定ガイド]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web)を読んで、JavaScriptの統合全般について理解してください。<br><br>また、[JavaScript SDKリファレンス](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)をブックマークして、さまざまなSDKメソッドと設定オプションの詳細を確認することもお勧めします。
{% endalert %}

Braze Web SDKを統合するには、まず最新のJavaScriptライブラリのコピーをダウンロードする必要があります。これは、NPMを使用するか、[Braze CDN](https://js.appboycdn.com/web-sdk/latest/braze.min.js)から直接ダウンロードすることで実行できます。

または、[Google Tag マネージャー]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/)を使用するか、Braze SDKの外部ホストされたコピーを使用する場合は、外部リソースの読み込みには`manifest.json`の[`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy)設定を調整する必要があることに注意してください。

ダウンロードしたら、`braze.min.js`ファイルを拡張機能のディレクトリ内の任意の場所にコピーします。

### 拡張機能ポップアップ {#popup}

拡張機能のポップアップにBrazeを追加するには、通常のWebサイトと同様に、`popup.html`でローカルJavaScriptファイルを参照します。Google Tag マネージャーを使用している場合は、代わりに[Google Tag マネージャーテンプレート]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/)を使用してBrazeを追加できます。

```html
<html>
    <title>popup.html</title>
    <!-- Add the Braze library -->
    <script src="/relative/path/to/braze.min.js"></script>
    <script>
    // Initialize Braze here
    </script>
</html>
```

### バックグラウンドスクリプト（Manifest v2のみ） {#background-script}

拡張機能のバックグラウンドスクリプト内でBrazeを使用するには、Brazeライブラリを`manifest.json`の`background.scripts`配列に追加します。これにより、グローバル`braze`変数がバックグラウンドスクリプトコンテキストで使用できるようになります。


```json
{
    "manifest_version": 2,
    "background": {
        "scripts": [
            "relative/path/to/braze.min.js",
            "background.js"
        ]
    }
}
```

### オプションページ {#options-page}

オプションページを（`options`または`options_ui`マニフェストプロパティを介して）使用する場合、[`popup.html`の説明](#popup)と同じ方法でBrazeを組み込むことができます。

## 初期化 {#initialization}

SDKが組み込まれると、通常どおりにライブラリを初期化できます。

Cookieはブラウザ拡張機能ではサポートされていないため、`noCookies: true`で初期化することでCookieを無効にできます。

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true,
    noCookies: true
});
```

サポートされている初期化オプションの詳細については、[Web SDKリファレンス](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)を参照してください。

## プッシュ {#push}

拡張機能のポップアップダイアログではプッシュプロンプトを使用できません（ナビゲーションにURLバーがありません）。そのため、拡張機能のポップアップダイアログ内でプッシュ通知の権限を登録してリクエストするには、[代替プッシュドメイン]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain)で説明されているように、代替ドメインの回避策を使用する必要があります。