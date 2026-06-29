---
nav_title: コンテンツセキュリティポリシーのヘッダー
article_title: Webのコンテンツセキュリティポリシーヘッダー
platform: Web
page_order: 21
page_type: reference
description: "この記事では、Braze Web SDKに必要なコンテンツセキュリティポリシーヘッダーについて説明します。"

---

# コンテンツセキュリティポリシーのヘッダー {#content-security-policy-headers}

> Content-Security-Policyは、Webサイトでコンテンツを読み込む方法と場所を制限することで、追加のセキュリティを提供します。この参考記事では、Web SDKに必要なコンテンツセキュリティポリシーヘッダーについて説明します。

{% alert important %}
この記事は、CSPルールを適用し、Brazeと統合するWebサイトに取り組む開発者を対象としています。セキュリティへのアプローチ方法に関する助言を目的としたものではありません。
{% endalert %}

{% multi_lang_include archive/web-v4-rename.md %}

## Nonce属性 {#nonce}

`script-src`または`style-src`ディレクティブで`nonce`値を使用する場合、その値を`contentSecurityNonce`初期化オプションに渡して、SDKによって新たに作成されるスクリプトやスタイルに伝播させます。

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  contentSecurityNonce: "YOUR-NONCE-HERE", // assumes a "nonce-YOUR-NONCE-HERE" CSP value
});
```

## ディレクティブ {#directives}

### `connect-src` {#connect-src}

{% alert warning %}
URLは、選択した`baseUrl`初期化オプションの[API SDKエンドポイント]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)と一致する必要があります。
{% endalert %}

| URL | 情報 |
|---|-----------|
| `connect-src https://sdk.iad-01.braze.com` | SDKがBraze APIと通信できるようにします。このURLを、選択した`baseUrl`初期化オプションの[API SDKエンドポイント]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)に一致するように変更してください。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="connect-src #connect-src" }

### `script-src` {#script-src}

| URL | 情報 |
|---|-----------|
| `script-src https://js.appboycdn.com` | CDNホスト統合を使用する場合に必要です。|
| `script-src 'unsafe-eval'` | `appboyQueue`への参照を含む統合スニペットを使用する場合に必要です。このディレクティブの使用を避けるには、代わりに[NPMを使用してSDKを統合]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/?tab=package%20manager)してください。|
| `script-src 'nonce-...'`<br>または<br>`script-src 'unsafe-inline'` | カスタムHTMLなど、特定のアプリ内メッセージに必要です。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="script-src #script-src" }

### `img-src` {#img-src}

| URL | 情報 |
|---|-----------|
| `img-src: appboy-images.com braze-images.com cdn.braze.eu` | Braze CDNホスト画像を使用する場合に必要です。ホスト名はダッシュボードクラスタによって異なる場合があります。<br><br>**重要:** カスタムフォントを使用している場合は、`font-src`も含める必要があります。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="img-src #img-src" }

## Font Awesome {#font-awesome}

Font Awesomeの自動組み込みを無効にするには、`doNotLoadFontAwesome`初期化オプションを使用します。

`````````javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  doNotLoadFontAwesome: true,
});
```

Font Awesomeを使用する場合は、次のCSPディレクティブが必要です。

- `font-src https://use.fontawesome.com`
- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'`または`style-src 'unsafe-inline'`