## Web Braze SDKについて {#about-the-web-braze-sdk}

Web Braze SDKを使えば、分析データを収集し、Webユーザー向けにリッチなアプリ内メッセージ、プッシュ通知、Content Cardsメッセージを表示できます。詳細については、[Braze JavaScriptリファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)を参照してください。

{% multi_lang_include archive/web-v4-rename.md %}

## Web SDKを統合する {#integrate-the-web-sdk}

Web Braze SDKは以下の方法で統合できます。追加のオプションについては、[その他の統合方法](#web_other-integration-methods)を参照してください。

- **コードベースの統合：** お好みのパッケージマネージャーまたはBraze CDNを使って、Web Braze SDKをコードベースに直接統合します。これにより、SDKの読み込み方法と設定方法を完全にコントロールできます。
- **Google Tag Manager：** サイトのコードを変更せずにWeb Braze SDKを統合できるノーコードソリューションです。詳細については、[Google Tag ManagerとBraze SDK]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager)を参照してください。

{% alert important %}
[NPM統合方式]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web)の使用を推奨します。メリットには、SDKライブラリーをWebサイトにローカル保存できること、広告ブロック拡張機能の影響を受けないこと、バンドラーサポートの一環として読み込み速度の向上に寄与することが含まれます。
{% endalert %}

{% tabs local %}
{% tab code-based integration %}
### ステップ1：Brazeライブラリーをインストールする {#step-1-install-the-braze-library}

Brazeライブラリーは、以下のいずれかの方法でインストールできます。ただし、Webサイトが`Content-Security-Policy`を使用している場合は、続行する前に[コンテンツセキュリティポリシー]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy)を確認してください。

{% alert important %}
ほとんどの広告ブロッカーはBraze Web SDKをブロックしませんが、より制限の厳しい広告ブロッカーでは問題が発生することが知られています。
{% endalert %}

{% subtabs %}
{% subtab package manager %}
サイトがNPMまたはYarnパッケージマネージャーを使用している場合、依存関係として[Braze NPMパッケージ](https://www.npmjs.com/package/@braze/web-sdk)を追加できます。

v3.0.0からTypeScriptの定義が含まれるようになりました。2.xから3.xへのアップグレードに関する注意事項については、[changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md)を参照してください。

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

インストール後は、通常の方法でライブラリーを`import`または`require`できます。

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endsubtab %}

{% subtab braze cdn %}
Braze Web SDKをHTMLに直接追加するには、CDNホストスクリプトを参照し、ライブラリーを非同期で読み込みます。

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
Safariのデフォルト設定である**クロスサイトトラッキングの防止**は、CDN統合方式を使用する場合、バナーやContent Cardsなどのアプリ内メッセージタイプの表示を妨げる可能性があります。この問題を回避するには、NPM統合方式を使用してください。そうすればSafariがこれらのメッセージをクロスサイトトラフィックとして分類せず、Webユーザーはすべての対応ブラウザーでそれらを確認できます。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### ステップ2：SDKを初期化する {#step-2-initialize-the-sdk}

Braze Web SDKをWebサイトに追加した後、Brazeダッシュボードの**設定** > **アプリ設定**にあるAPIキーと[SDKエンドポイントURL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)でライブラリーを初期化します。`braze.initialize()`のオプションの完全な一覧と、その他のJavaScriptメソッドについては、[Braze JavaScriptドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)を参照してください。

{% alert note %}
**Web SDKリクエストにおけるカスタムドメインはサポートされていません：** Web SDKの`baseUrl`はBraze SDKエンドポイントでなければなりません（例：`sdk.iad-05.braze.com`）。BrazeはCNAMEレコードを介して顧客所有のドメインを経由するWeb SDKトラフィックのルーティングをサポートしていません。Web SDKのリクエストを自身のドメインから発信する必要がある場合は、Brazeサポートにお問い合わせください。
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
**アプリ内メッセージの表示：** アプリ内メッセージがトリガーされた際に自動的に表示するには、`braze.automaticallyShowInAppMessages()`を呼び出す必要があります。この呼び出しがないと、アプリ内メッセージは自動的に表示されません。メッセージ表示を手動で管理したい場合は、この呼び出しを削除し、代わりに`braze.subscribeToInAppMessage()`を使用してください。詳細については、[アプリ内メッセージ配信]({{site.baseurl}}/developer_guide/in_app_messages/delivery)を参照してください。
{% endalert %}

#### 匿名ユーザーにおけるセッション消失のトラブルシューティング {#troubleshooting-missing-sessions-for-anonymous-users}

「セッションが欠落している」という現象が発生している場合、またはWeb上で匿名のままのユーザーのセッションをトラッキングできない場合は、初期化中に`braze.openSession()`が呼び出されていることを確認してください。

- **シナリオ：** 匿名ユーザーはBraze IDを返すが、セッションデータが空白または欠落している。
- **原因：** 実装で`braze.openSession()`が呼び出されていない。
- **解決策：** 初期化後は必ず`braze.openSession()`を呼び出してください（external IDを設定した場合は`braze.changeUser()`の後にも呼び出してください）。

詳細については、[ステップ2：SDKを初期化する]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web&tab=code-based%20integration#step-2-initialize-the-sdk)を参照してください。

{% alert important %}
モバイルデバイスまたはWebデバイスの匿名ユーザーは、[MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data#monthly-active-users)にカウントされる場合があります。その結果、これらのユーザーをMAUカウントから除外するために、条件付きでSDKを読み込むか、初期化することを検討してください。
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
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

## オプション設定 {#optional-configurations}

### ロギング {#logging}

ロギングをすばやく有効にするには、`?brazeLogging=true`をパラメーターとしてWebサイトURLに追加します。あるいは、[基本](#web_basic-logging)ロギングまたは[カスタム](#web_custom-logging)ロギングを有効にすることもできます。すべてのプラットフォームにわたる一元的な概要については、[詳細ログ]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)を参照してください。

#### 基本的なロギング {#basic-logging}

{% tabs local %}
{% tab 初期化前 %}
SDKが初期化される前に、基本的なデバッグメッセージをJavaScriptコンソールに記録するには`enableLogging`を使用します。

```javascript
enableLogging: true
```

メソッドは次のようになります。

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab 初期化後 %}
SDKが初期化された後、基本的なデバッグメッセージをJavaScriptコンソールに記録するには`braze.toggleLogging()`を使用します。メソッドは次のようになります。

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
基本ログはすべてのユーザーに表示されるため、コードを本番環境にリリースする前に、無効にすることを検討するか、[`setLogger`](#web_custom-logging)に切り替えてください。
{% endalert %}

#### カスタムロギング {#custom-logging}

カスタムデバッグメッセージをJavaScriptコンソールに記録するには、`setLogger`を使用します。基本ログとは異なり、これらのログはユーザーには表示されません。

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

`STRING`を1つの文字列パラメーターとしてメッセージに置き換えます。メソッドは次のようになります。

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## SDKをアップグレードする {#upgrading-the-sdk}

{% multi_lang_include archive/web-v4-rename.md %}

コンテンツ配信ネットワークからBraze Web SDKを参照する場合（デフォルトの統合手順で推奨されている通り）、例えば`https://js.appboycdn.com/web-sdk/a.a/braze.min.js`の場合、ユーザーはサイトを更新する際にマイナー更新（バグ修正や下位互換性のある機能、上記の例でバージョン`a.a.a`から`a.a.z`までの更新）を自動的に受け取ります。

ただし、主要な変更をリリースする際には、互換性を損なう変更が統合に影響しないよう、Braze Web SDKを手動でアップグレードする必要があります。さらに、SDKをダウンロードして自身でホストする場合、バージョン更新は自動的には行われないため、最新の機能やバグ修正を受けるには手動でアップグレードする必要があります。

RSSリーダーまたは任意のサービスを使用して、[リリースフィードをフォロー](https://github.com/braze-inc/braze-web-sdk/tags.atom)することで最新のリリースを把握できます。また、Web SDKのリリース履歴の詳細については、[変更ログ](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)を参照してください。Braze Web SDKをアップグレードするには：

- `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js`のバージョン番号を変更するか、パッケージマネージャーの依存関係でBrazeライブラリーのバージョンを更新します。
- Webプッシュが統合されている場合は、サイトのサービスワーカーファイルを更新します。デフォルトでは、このファイルはサイトのルートディレクトリの`/service-worker.js`にありますが、統合によっては場所がカスタマイズされている場合があります。サービスワーカーファイルをホストするには、ルートディレクトリにアクセスする必要があります。

正常に機能させるために、これら2つのファイルは連携して更新する必要があります。

## その他の統合方法 {#other-integration-methods}

### Accelerated Mobile Pages（AMP） {#accelerated-mobile-pages-amp}
{% details 詳細を見る %}
#### ステップ1：AMP Webプッシュスクリプトを含める {#step-1-include-amp-web-push-script}

次の非同期スクリプトタグをheadに追加します。

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### ステップ2：サブスクリプションウィジェットを追加する {#step-2-add-subscription-widgets}

HTMLのbodyにウィジェットを追加し、ユーザーがプッシュ通知の登録と配信停止を行えるようにします。

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

AMP Webプッシュコンポーネントは、プッシュサブスクリプションを処理するためのポップアップを作成します。この機能を有効にするには、プロジェクトに以下のヘルパーファイルを追加する必要があります。

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### ステップ4：サービスワーカーファイルを作成する {#step-4-create-a-service-worker-file}

Webサイトのルートディレクトリに`service-worker.js`ファイルを作成し、以下のスニペットを追加します。

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### ステップ5：AMP Webプッシュ HTML要素を構成する {#step-5-configure-the-amp-web-push-html-element}

HTMLのbodyに次の`amp-web-push` HTML要素を追加します。[`apiKey`と`baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG)をクエリパラメーターとして`service-worker-URL`に追加する必要があることに注意してください。

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

### 非同期モジュール定義（AMD） {#asynchronous-module-definition-amd}

#### サポートを無効にする {#disable-support}

サイトがRequireJSや他のAMDモジュールローダーを使用しているが、このリストにある他のオプションのいずれかでBraze Web SDKを読み込みたい場合、AMDサポートを含まないバージョンのライブラリーを読み込むことができます。このバージョンのライブラリーは、以下のCDNの場所から読み込めます。

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### モジュールローダー {#module-loader}

RequireJSまたは他のAMDモジュールローダーを使用する場合は、ライブラリーのコピーをセルフホスティングし、他のリソースと同様に参照することをお勧めします。

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electron {#electron}

Electronは公式にはWebプッシュ通知をサポートしていません（参照：この[GitHub issue](https://github.com/electron/electron/issues/6697)）。Brazeがテストしていない[オープンソースの回避策](https://github.com/MatthieuLemoine/electron-push-receiver)を試すこともできます。

### Jestフレームワーク {#jest}

Jestを使用している場合、`SyntaxError: Unexpected token 'export'`のようなエラーが表示されることがあります。これを修正するには、Braze SDKを無視するように`package.json`の設定を調整します。

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### SSRフレームワーク {#ssr}

Web SDKはブラウザー環境で動作します。SSRフレームワークでは、サーバーがSDKコードを実行しないよう、クライアント専用コンポーネントでBrazeを初期化してください。

#### フレームワーク非依存の動的インポート {#framework-agnostic-dynamic-import}

このセクションにフレームワークが記載されていない場合は、クライアント専用のライフサイクルフックからBrazeを動的にインポートできます。

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

webpackを使用している場合は、特定のSDKエクスポートのみを動的にインポートできます。

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

アプリをラップするクライアントコンポーネントで`useBraze`を呼び出します。

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

#### イベントのログ記録とユーザーの更新 {#logging-events-and-updating-users}

`useBraze`がアプリのルートでSDKを初期化した後、他のクライアントコンポーネントからBrazeメソッドを呼び出すことができます。一般的なパターンは、`onClick`や`onSubmit`などのユーザーアクション内でメソッドを呼び出すことです。この例では、SDKメソッドはファイルの先頭ではなく、クリックハンドラー内で読み込まれます。これにより、Web SDKをサーバーコードから分離し、そのアクションに必要なものだけを読み込みます。`webpackExports`コメントは、どのメソッドを含めるかをwebpackに指示するため、バンドルサイズを小さく保てます。

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

この例は、ユーザーが**Buy**をクリックした際にアクティビティを記録する`BuyButton`コンポーネントを示しています。まず、クリック時に`logCustomEvent`、`logPurchase`、`getUser`のみをインポートします。次に、ユーザー属性を更新し、カスタムイベントを記録し、購入を記録します。このパターンにより、初期化を`useBraze`に集中させながら、任意のクライアントコンポーネントから意味のあるアクションをトラッキングできます。

RemixでViteを使用していて、パッケージルートのインポートが実行時に失敗する場合は、既存のViteの回避策を使用してください。詳細については、[Vite]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_vite)を参照してください。

利用可能なメソッドの完全な一覧については、[Braze JavaScriptリファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)を参照してください。

### Tealium iQ

Tealium iQは、基本的なターンキーBraze統合を提供します。統合を構成するには、Tealium Tag ManagementインターフェイスでBrazeを検索し、ダッシュボードからWeb SDK APIキーを指定します。

詳細やTealiumの設定に関する詳しいサポートが必要な場合は、[統合ドキュメント]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium#about-tealium)を参照するか、Tealiumのアカウントマネージャーにお問い合わせください。

### Vite {#vite}

Viteを使用していて、循環依存関係や`Uncaught TypeError: Class extends value undefined is not a constructor or null`に関する警告が表示される場合は、Braze SDKを[依存関係の検出](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior)から除外する必要があるかもしれません。

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### その他のタグマネージャー {#other-tag-managers}

Brazeは、カスタムHTMLタグ内で統合手順に従うことにより、他のタグ管理ソリューションとも互換性を持つ場合があります。これらのソリューションの評価について支援が必要な場合は、Brazeの担当者にお問い合わせください。