## Web Braze SDKについて {#about-the-web-braze-sdk}

Web Braze SDKを使用すると、分析データを収集し、リッチなアプリ内メッセージ、プッシュ通知、Content Cardsメッセージを Web ユーザーに表示できます。詳しくは、[Braze JavaScriptリファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)を参照してください。

{% multi_lang_include archive/web-v4-rename.md %}

## Web SDKを統合する {#integrate-the-web-sdk}

以下の方法でWeb Braze SDKを統合できます。その他のオプションについては、[その他の統合方法](#web_other-integration-methods)を参照してください。

- **コードベースの統合：** お好みのパッケージマネージャーまたはBraze CDNを使用して、Web Braze SDKをコードベースに直接統合します。これにより、SDKの読み込みと設定を完全にコントロールできます。
- **Google Tag マネージャー：** サイトのコードを変更せずにWeb Braze SDKを統合できるノーコードソリューションです。詳しくは、[Google Tag マネージャー with the Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager)を参照してください。

{% alert important %}
[NPM統合方法]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web)の使用を推奨します。この方法には、SDKライブラリをWebサイトにローカル保存できること、広告ブロッカー拡張機能の影響を受けないこと、バンドラーサポートの一部として読み込み時間の短縮に貢献することなどのメリットがあります。
{% endalert %}

{% tabs local %}
{% tab コードベースの統合 %}
### ステップ1：Brazeライブラリをインストールする {#step-1-install-the-braze-library}

以下のいずれかの方法でBrazeライブラリをインストールできます。ただし、Webサイトで`Content-Security-Policy`を使用している場合は、続行する前に[Content Security Policy]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy)を確認してください。

{% alert important %}
ほとんどの広告ブロッカーはBraze Web SDKをブロックしませんが、一部のより制限の厳しい広告ブロッカーでは問題が発生することが知られています。
{% endalert %}

{% subtabs %}
{% subtab package マネージャー %}
サイトでNPMまたはYarnパッケージマネージャーを使用している場合は、[Braze NPMパッケージ](https://www.npmjs.com/package/@braze/web-sdk)を依存関係として追加できます。

Typescriptの型定義はv3.0.0から含まれています。2.xから3.xへのアップグレードに関する注意事項については、[変更ログ](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md)を参照してください。

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

インストール後、通常の方法でライブラリを`import`または`require`できます：

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endsubtab %}

{% subtab braze cdn %}
CDNでホストされているスクリプトを参照して、Braze Web SDKをHTMLに直接追加します。これにより、ライブラリが非同期で読み込まれます。

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
Safariのデフォルトの**クロスサイトトラッキング防止**設定により、CDN統合方法を使用するとバナーやContent Cardsなどのアプリ内メッセージタイプが表示されない場合があります。この問題を回避するには、NPM統合方法を使用してください。これにより、Safariがこれらのメッセージをクロスサイトトラフィックとして分類せず、すべてのサポートされているブラウザでWebユーザーがメッセージを表示できるようになります。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### ステップ2：SDKを初期化する {#step-2-initialize-the-sdk}

Braze Web SDKをWebサイトに追加した後、Brazeダッシュボードの**設定** > **アプリ設定**にあるAPIキーと[SDKエンドポイントURL]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)を使用してライブラリを初期化します。`braze.initialize()`のオプションの完全なリストやその他のJavaScriptメソッドについては、[Braze JavaScriptドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)を参照してください。

{% alert note %}
**Web SDKリクエストのカスタムドメインはサポートされていません：** Web SDKの`baseUrl`はBraze SDKエンドポイント（例：`sdk.iad-05.braze.com`）である必要があります。BrazeはCNAMEレコードを介した顧客所有ドメイン経由でのWeb SDKトラフィックのルーティングをサポートしていません。Web SDKリクエストを独自のドメインから発信する必要がある場合は、Brazeサポートにお問い合わせください。
{% endalert %}

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
    enableLogging: false, // set to `true` for debugging
    allowUserSuppliedJavascript: false, // set to `true` to support custom HTML messages
});

// Enable automatic display of in-app messages
// Required if you want in-app messages to display automatically when triggered
braze.automaticallyShowInAppMessages();

// if you use Content Cards
braze.subscribeToContentCardsUpdates(function(cards){
    // cards have been updated
});

// optionally set the current user's external ID before starting a new session
// you can also call `changeUser` later in the session after the user logs in
if (isLoggedIn){
    braze.changeUser(userIdentifier);
}

// `openSession` should be called last - after `changeUser` and `automaticallyShowInAppMessages`
braze.openSession();
```

{% alert important %}
**アプリ内メッセージの表示：** トリガーされたアプリ内メッセージを自動的に表示するには、`braze.automaticallyShowInAppMessages()`を呼び出す必要があります。この呼び出しがないと、アプリ内メッセージは自動的に表示されません。メッセージの表示を手動で管理する場合は、この呼び出しを削除し、代わりに`braze.subscribeToInAppMessage()`を使用してください。詳しくは、[自動トリガーの無効化]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#disabling-automatic-triggers)を参照してください。
{% endalert %}

#### 匿名ユーザーのセッションが欠落する場合のトラブルシューティング {#troubleshooting-missing-sessions-for-anonymous-users}

「セッションが欠落」する動作が見られる場合、またはWebで匿名のままのユーザーのセッションをトラッキングできない場合は、統合で初期化時に`braze.openSession()`を呼び出していることを確認してください。

- **シナリオ：** 匿名ユーザーはBraze IDを返すことができますが、セッションデータが空または欠落しています。
- **原因：** 実装で`braze.openSession()`が呼び出されていません。
- **解決方法：** 初期化後（およびexternal IDを設定する場合は`braze.changeUser()`の後）に、常に`braze.openSession()`を呼び出してください。

詳しくは、[ステップ2：SDKを初期化する]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web&tab=code-based%20integration#step-2-initialize-the-sdk)を参照してください。

{% alert important %}
モバイルまたはWebデバイスの匿名ユーザーは、[MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data#monthly-active-users)にカウントされる場合があります。その結果、MAUカウントからこれらのユーザーを除外するために、SDKの読み込みまたは初期化を条件付きで行うことを検討してください。
{% endalert %}
{% endtab %}

{% tab Google Tag マネージャー %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## ボットトラフィックのフィルタリング {#bot-filtering}

MAUにはボットユーザーの割合が含まれる場合があり、月間アクティブユーザー数が水増しされることがあります。Braze Web SDKには、検索エンジンのボットやソーシャルメディアのプレビューボットなど、一般的なWebクローラーの検出機能が組み込まれていますが、SDKの更新だけでは常にすべての新しいボットを検出できるわけではないため、ボットを検出するための堅牢なソリューションを積極的に導入することが特に重要です。

### SDK側のボット検出の限界 {#limitations-of-sdk-side-bot-detection}

Web SDKには、既知のクローラーを除外する基本的なユーザーエージェントベースのボット検出機能が組み込まれています。しかし、この方法には限界があります。

- **新しいボットが次々と出現する：** AI企業やその他の関係者は、検出を回避するために偽装する可能性のある新しいボットを定期的に作成しています。
- **ユーザーエージェントの偽装：** 高度なボットは、正当なブラウザーのユーザーエージェントを模倣できます。
- **カスタムボット：** 技術的知識のないユーザーでも、大規模言語モデル（LLM）を使って簡単にボットを作成できるようになり、ボットの挙動は予測不能になっています。

### ボットフィルタリングの実装 {#implementing-bot-filtering}

{% alert important %}
以下に述べるソリューションは一般的な提案です。ボットフィルタリングのロジックを、独自の環境とトラフィックパターンに合わせて調整してください。
{% endalert %}

最も堅牢なソリューションは、Braze SDKを初期化する前に独自のボットフィルタリングロジックを実装することです。一般的な手法には以下が含まれます。

#### ユーザー操作を必須にする {#require-user-interaction}

ユーザーがCookie同意バナーの承諾、スクロール、クリックなどの意味のある操作を行うまで、SDKの初期化を遅らせることを検討してください。この手法は実装が容易な場合が多く、ボットトラフィックのフィルタリングに非常に効果的です。

{% alert important %}
SDKの初期化をユーザー操作まで遅らせると、バナーやContent Cardsもその操作が行われるまで表示されない可能性があります。
{% endalert %}

#### カスタムボット検出 {#custom-bot-detection}

特定のボットトラフィックパターンに基づいてカスタム検出を実装します。例えば：

- トラフィックで識別したパターンについて、ユーザーエージェント文字列を分析する
- ヘッドレスブラウザーの指標を確認する
- サードパーティのボット検出サービスを利用する
- サイト固有の行動シグナルを監視する

**条件付き初期化の例：**

```javascript
// Only initialize Braze if your custom bot detection determines this is not a bot
if (!isLikelyBot()) {
  braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE"
  });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
}
```

### ベストプラクティス {#best-practices}

- MAUデータとWebトラフィックのパターンを定期的に分析し、新たなボットの行動を識別してください。
- ボットフィルタリングが正当なユーザーのトラッキングを妨げないよう、徹底的にテストしてください。
- 環境内で観察されるボットのトラフィックパターンに基づいて、フィルタリングロジックを更新してください。

## オプションの設定 {#optional-configurations}

### ロギング {#logging}

ロギングを素早く有効にするには、Webサイトの URL にパラメーターとして `?brazeLogging=true` を追加します。または、[基本](#web_basic-logging)ロギングや[カスタム](#web_custom-logging)ロギングを有効にすることもできます。すべてのプラットフォームにわたる一元的な概要については、[詳細ログ]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)を参照してください。

#### 基本ロギング {#basic-logging}

{% tabs local %}
{% tab 初期化前 %}
SDKが初期化される前に、基本的なデバッグメッセージをJavaScriptコンソールに記録するには、`enableLogging` を使用します。

```javascript
enableLogging: true
```

メソッドは以下のようになります：

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab 初期化後 %}
SDKが初期化された後に、基本的なデバッグメッセージをJavaScriptコンソールに記録するには、`braze.toggleLogging()` を使用します。メソッドは以下のようになります：

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
});
braze.openSession();
...
braze.toggleLogging();
```
{% endtab %}
{% endtabs %}

{% alert important %}
基本ログはすべてのユーザーに表示されるため、コードを本番環境にリリースする前に、無効にするか、[`setLogger`](#web_custom-logging) に切り替えることを検討してください。
{% endalert %}

#### カスタムロギング {#custom-logging}

カスタムデバッグメッセージをJavaScriptコンソールに記録するには、`setLogger` を使用します。基本ログとは異なり、これらのログはユーザーには表示されません。

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

`STRING` を単一の文字列パラメーターとしてメッセージに置き換えます。メソッドは以下のようになります：

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## SDKのアップグレード {#upgrading-the-sdk}

{% multi_lang_include archive/web-v4-rename.md %}

BrazeのコンテンツデリバリーネットワークからBraze Web SDKを参照している場合（例：`https://js.appboycdn.com/web-sdk/a.a/braze.min.js`、デフォルトの統合手順で推奨されています）、ユーザーがサイトを更新すると、マイナーアップデート（バグ修正や後方互換性のある機能、この例では`a.a.a`から`a.a.z`のバージョン）が自動的に適用されます。

ただし、メジャーチェンジがリリースされた場合は、破壊的変更が統合に影響しないよう、Braze Web SDKを手動でアップグレードする必要があります。また、SDKをダウンロードしてご自身でホストしている場合は、バージョン更新が自動的に行われないため、最新の機能やバグ修正を受け取るには手動でアップグレードする必要があります。

最新リリースの情報は、お好みのRSSリーダーやサービスで[リリースフィードをフォロー](https://github.com/braze-inc/braze-web-sdk/tags.atom)することで確認できます。また、Web SDKのリリース履歴の全記録については、[変更ログ](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)を参照してください。Braze Web SDKをアップグレードするには、以下の手順を行います。

- `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js`のバージョン番号を変更するか、パッケージマネージャーの依存関係を更新して、Brazeライブラリのバージョンを更新します。
- Webプッシュを統合している場合は、サイト上のService Workerファイルを更新します。デフォルトでは、このファイルはサイトのルートディレクトリの`/service-worker.js`に配置されていますが、統合によってはカスタマイズされている場合があります。Service Workerファイルをホストするには、ルートディレクトリにアクセスする必要があります。

正常に機能させるためには、これら2つのファイルを連携して更新する必要があります。

## その他の統合方法 {#other-integration-methods}

### Accelerated Mobile Pages (AMP)
{% details 詳細を見る %}
#### ステップ1：AMP Webプッシュスクリプトを含める {#step-1-include-amp-web-push-script}

以下の非同期スクリプトタグをheadに追加します：

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### ステップ2：購読ウィジェットを追加する {#step-2-add-subscription-widgets}

ユーザーがプッシュの購読および購読解除を行えるウィジェットをHTMLのbodyに追加します。

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

#### ステップ3：`helper-iframe`と`permission-dialog`を追加する {#step-3-add-helper-iframe-and-permission-dialog}

AMP Webプッシュコンポーネントは、プッシュ購読を処理するためのポップアップを作成するので、この機能を有効にするには以下のヘルパーファイルをプロジェクトに追加する必要があります：

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### ステップ4：サービスワーカーファイルを作成する {#step-4-create-a-service-worker-file}

Webサイトのルートディレクトリに`service-worker.js`ファイルを作成し、以下のスニペットを追加します：

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### ステップ5：AMP Webプッシュ HTML要素を設定する {#step-5-configure-the-amp-web-push-html-element}

以下の`amp-web-push` HTML要素をHTMLのbodyに追加します。[`apiKey`と`baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG)をクエリパラメータとして`service-worker-URL`に追加する必要がある点に注意してください。

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```
{% enddetails %}

### Asynchronous Module Definition (AMD)

#### サポートの無効化 {#disable-support}

サイトがRequireJSやその他のAMDモジュールローダーを使用しているが、このリストの他のオプションを通じてBraze Web SDKを読み込みたい場合は、AMDサポートを含まないバージョンのライブラリを読み込むことができます。このバージョンのライブラリは以下のCDNから読み込めます：

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### モジュールローダー {#module-loader}

RequireJSやその他のAMDモジュールローダーを使用する場合は、ライブラリのコピーをセルフホスティングし、他のリソースと同様に参照することを推奨します：

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electron {#electron}

ElectronはWebプッシュ通知を公式にはサポートしていません（この[GitHubイシュー](https://github.com/electron/electron/issues/6697)を参照）。Brazeではテストされていませんが、試すことができる他の[オープンソースの回避策](https://github.com/MatthieuLemoine/electron-push-receiver)があります。

### Jestフレームワーク {#jest}

Jestを使用する際、`SyntaxError: Unexpected token 'export'`のようなエラーが表示されることがあります。これを修正するには、`package.json`の設定を調整してBraze SDKを無視するようにします：

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### SSRフレームワーク {#ssr}

Web SDKはブラウザ環境で動作します。SSRフレームワークでは、サーバーがSDKコードを実行しないように、クライアント専用コンポーネントでBrazeを初期化します。

#### フレームワークに依存しないダイナミックインポート {#framework-agnostic-dynamic-import}

このセクションにフレームワークが記載されていない場合は、クライアント専用のライフサイクルフックからBrazeをダイナミックインポートできます。

```javascript
// MyComponent/braze-exports.js
// Export the parts of the SDK that you need.
export { initialize, openSession } from "@braze/web-sdk";

// MyComponent/MyComponent.js
useEffect(() => {
    import("./braze-exports.js").then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

webpackを使用している場合は、特定のSDKエクスポートのみをダイナミックインポートできます。

```javascript
// MyComponent.js
useEffect(() => {
    import(
        /* webpackExports: ["initialize", "openSession"] */
        "@braze/web-sdk"
    ).then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

#### Next.jsとRemix用の共有フック {#shared-hook-for-nextjs-and-remix}

再利用可能な`useBraze`フックを作成し、アプリのルート付近で呼び出します。

```tsx
// hooks/useBraze.ts
import { useEffect, useRef } from "react";

export function useBraze() {
  const didInit = useRef(false);

  useEffect(() => {
    if (didInit.current) {
      return;
    }
    didInit.current = true;

    import("@braze/web-sdk")
      .then((braze) => {
        const initialized = braze.initialize("YOUR-API-KEY-HERE", {
          // Use your Braze Web SDK endpoint, such as sdk.iad-01.braze.com.
          baseUrl: "YOUR-SDK-ENDPOINT",
          enableLogging: false,
        });
        if (!initialized) {
          return;
        }

        // Optional: Identify signed-in users before opening a session.
        // braze.changeUser("external-id");

        // Optional: Automatically display in-app messages.
        // braze.automaticallyShowInAppMessages();
        braze.openSession();
      })
      .catch((error) => {
        console.error("Unable to load Braze SDK:", error);
      });
  }, []);
}
```

#### Next.js（App Router） {#nextjs-app-router}

クライアントコンポーネントで`useBraze`を呼び出し、アプリをラップします。

```tsx
// app/components/AppRoot.tsx
"use client";

import type { ReactNode } from "react";
import { useBraze } from "../hooks/useBraze";

export function AppRoot({ children }: { children: ReactNode }) {
  useBraze();
  return <>{children}</>;
}
```

```tsx
// app/layout.tsx
import type { ReactNode } from "react";
import { AppRoot } from "./components/AppRoot";

export default function RootLayout({
  children,
}: {
  children: ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <AppRoot>{children}</AppRoot>
      </body>
    </html>
  );
}
```

#### Next.js（Pages Router） {#nextjs-pages-router}

カスタムアプリコンポーネントの先頭で`useBraze`を呼び出します。

```tsx
// pages/_app.tsx
import type { AppProps } from "next/app";
import { useBraze } from "../hooks/useBraze";

export default function App({ Component, pageProps }: AppProps) {
  useBraze();

  return (
    <Component {...pageProps} />
  );
}
```

#### Remix

ルートルートコンポーネントの先頭で`useBraze`を呼び出します。

ローカルのRemix検証例を実行するには、`PORT=4013 npm run dev`を使用します。

```tsx
// app/root.tsx
import { Outlet } from "@remix-run/react";
import { useBraze } from "./hooks/useBraze";

export default function App() {
  useBraze();

  return <Outlet />;
}
```

#### イベントのログとユーザーの更新 {#logging-events-and-updating-users}

`useBraze`がアプリのルートでSDKを初期化した後、他のクライアントコンポーネントからBrazeのメソッドを呼び出すことができます。一般的なパターンは、`onClick`や`onSubmit`などのユーザーアクション内でメソッドを呼び出すことです。この例では、SDKメソッドはファイルの先頭ではなくクリックハンドラー内で読み込まれます。これにより、Web SDKをサーバーコードから分離し、そのアクションに必要なものだけを読み込みます。`webpackExports`コメントは、どのメソッドを含めるかをwebpackに指示するため、バンドルサイズが小さくなります。

```tsx
// app/components/BuyButton.tsx
"use client";

export function BuyButton() {
  const handleClick = async () => {
    const { logCustomEvent, logPurchase, getUser } = await import(
      /* webpackExports: ["logCustomEvent", "logPurchase", "getUser"] */
      "@braze/web-sdk"
    );

    getUser()?.setCustomUserAttribute("last_purchase_date", "2026-05-04");
    logCustomEvent("clicked_buy", { source: "product_page" });
    logPurchase("sku_123", 19.99, "USD");
  };

  return <button onClick={handleClick}>Buy</button>;
}
```

この例は、ユーザーが**Buy**をクリックしたときにアクティビティをログする`BuyButton`コンポーネントを示しています。まず、クリック時に`logCustomEvent`、`logPurchase`、`getUser`のみをインポートします。次に、ユーザー属性を更新し、カスタムイベントをログし、購入をログします。このパターンにより、初期化を`useBraze`に集中させつつ、任意のクライアントコンポーネントから意味のあるアクションをトラッキングできます。

RemixとViteを使用していて、パッケージルートインポートがランタイムで失敗する場合は、既存のViteの回避策を使用してください。詳細については、[Vite]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_vite)を参照してください。

利用可能なメソッドの完全なリストについては、[Braze JavaScriptリファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)を参照してください。

### Tealium iQ

Tealium iQは、基本的なターンキーのBraze統合を提供しています。統合を設定するには、Tealiumタグ管理インターフェイスでBrazeを検索し、ダッシュボードからWeb SDK APIキーを入力します。

詳細やTealiumの設定サポートについては、[統合ドキュメント]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium#about-tealium)を確認するか、Tealiumのアカウントマネージャーにお問い合わせください。

### Vite {#vite}

Viteを使用していて、循環依存関係に関する警告や`Uncaught TypeError: Class extends value undefined is not a constructor or null`が表示される場合は、Braze SDKをViteの[依存関係の検出](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior)から除外する必要があるかもしれません：

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### その他のタグマネージャー {#other-tag-managers}

Brazeは、カスタムHTMLタグ内で統合手順に従うことで、他のタグ管理ソリューションとも互換性がある場合があります。これらのソリューションの評価についてサポートが必要な場合は、Brazeの担当者にお問い合わせください。