---
nav_title: ディープリンクのトラブルシューティング
article_title: ディープリンクのトラブルシューティング
description: "症状インデックス、標準的な調査パス、プラットフォーム固有のチェックを使用して、iOSのディープリンクの問題を診断します。"
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# ディープリンクのトラブルシューティング {#troubleshoot-deep-linking}

> このページでは、iOSにおける一般的なディープリンクの問題を診断する方法について説明します。適切なリンクタイプの選び方については、[iOSディープリンクガイド]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide)を参照してください。実装の詳細については、[ディープリンク]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift)を参照してください。

## ここから始めましょう：症状を確認する {#start-here-match-your-symptom}

以下の表からお使いの環境で発生している動作を見つけ、該当セクションの手順に従ってください。どのセクションが該当するかわからない場合は、[標準的な調査パス](#standard-investigation-path)をご利用ください。

| 症状 | 参照先 |
| --- | --- |
| カスタムスキームリンクでアプリは開くが、画面が正しくない | [カスタムスキームのディープリンクで正しいビューが開かない](#custom-scheme-deep-link-does-not-open-the-correct-view) |
| ユニバーサルリンクでアプリではなくSafariが開く | [ユニバーサルリンクがアプリではなくSafariで開く](#universal-link-opens-in-safari-instead-of-the-app) |
| メールのリンクでアプリが開かない | [メールからのディープリンクでアプリが開かない](#deep-link-from-email-does-not-open-the-app) |
| プッシュ通知では動作するがアプリ内メッセージでは動作しない（またはその逆） | [ディープリンクがプッシュ通知では動作するがアプリ内メッセージでは動作しない](#deep-link-works-from-push-but-not-from-in-app-message) |
| 「Open Web URL Inside App」で空白のWebViewが表示される | [「Open Web URL Inside App」で空白または壊れたページが表示される](#open-web-url-inside-app-shows-a-blank-or-broken-page) |
| Branchリンクでアプリが開かない、または正しくルーティングされない | [BranchとBrazeのトラブルシューティング](#branch) |
| 明確な原因なくディープリンクが失敗する | [一般的なデバッグのヒント](#general-debugging-tips) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ディープリンクの症状" }

## 標準的な調査パス {#standard-investigation-path}

すべてのディープリンクのインシデントに対して、このワークフローを使用してください。ステップ1から開始します。

1. Braze外でリンクをテストします。カスタムスキームの場合は、ターミナルで`xcrun simctl openurl booted "<URL>"`を実行します（例: `xcrun simctl openurl booted "myapp://products/123"`）。ユニバーサルリンクの場合は、物理デバイスのメモアプリにURLを貼り付けてタップします。
2. [詳細ログを有効にし]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)、問題を再現します。`Opening '<URL>':` エントリで `channel`、`useWebView`、`isUniversalLink` を確認します。
3. ユニバーサルリンクの場合は、AASAファイルとAssociated Domainsエンタイトルメントを検証します。
4. メールリンクの場合は、クリックトラッキングドメインが有効なAASAファイルをホストしていることを確認します。
5. `BrazeDelegate.braze(_:shouldOpenURL:)` を実装している場合は、チャネル間でリンクが一貫して処理されていることを確認します。
6. 問題が解決しない場合は、詳細ログとリンクURLを添えて [Brazeサポート]({{site.baseurl}}/braze_support)に連絡してください。

## カスタムスキームのディープリンクが正しいビューを開かない {#custom-scheme-deep-link-does-not-open-the-correct-view}

**症状:** カスタムスキームのディープリンク（例: `myapp://products/123`）でアプリは開きますが、意図した画面に遷移しません。

1. **スキームが登録されていることを確認します。** Xcodeで、`Info.plist`の`CFBundleURLTypes`にスキームが登録されているか確認してください。
2. **ハンドラーを確認します。** `application(_:open:options:)`にブレークポイントを設定し、呼び出されていることと`url`パラメーターの内容を確認してください。
3. **リンクを単独でテストします。** ターミナルから以下のコマンドを実行して、Braze外でディープリンクをテストしてください:
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   ここでリンクが動作しない場合、問題はBrazeではなくアプリのURL処理にあります。
4. **URLの形式を確認します。** キャンペーンのURLがハンドラーの期待する形式と一致しているか確認してください。よくある間違いとして、パスコンポーネントの欠落や大文字・小文字の不一致があります。

## ユニバーサルリンクがアプリではなくSafariで開く {#universal-link-opens-in-safari-instead-of-the-app}

**症状：** ユニバーサルリンク（例：`https://myapp.com/products/123`）がアプリではなくSafariで開きます。

### Associated Domainsエンタイトルメントを確認する {#verify-the-associated-domains-entitlement}

Xcodeで、アプリターゲット > **Signing & Capabilities** に移動し、**Associated Domains** の下に`applinks:yourdomain.com`がリストされていることを確認してください。

### AASAファイルを検証する {#validate-the-aasa-file}

Apple App Site Association（AASA）ファイルは、以下のいずれかの場所にホストされている必要があります：

- `https://yourdomain.com/.well-known/apple-app-site-association`
- `https://yourdomain.com/apple-app-site-association`

以下を確認してください：

- ファイルが有効な証明書を使用してHTTPS経由で提供されていること。
- `Content-Type`が`application/json`であること。
- ファイルサイズが128 KB未満であること。
- `appID`がチームIDとバンドルIDに一致していること（例：`ABCDE12345.com.example.myapp`）。
- `paths`または`components`配列に、期待するURLパターンが含まれていること。

AASAの検証は、[Appleの検索検証ツール](https://search.developer.apple.com/appsearch-validation-tool/)を使用するか、以下のコマンドを実行して行えます：

```bash
swcutil dl -d yourdomain.com
```

### `AppDelegate`を確認する {#check-the-appdelegate}

`application(_:continue:restorationHandler:)`が`AppDelegate`に実装されており、`NSUserActivity`を正しく処理していることを確認してください：

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
    return false
  }
  // Handle the URL
  return true
}
```

### Braze SDKの設定を確認する {#verify-braze-sdk-configuration}

Brazeから配信されるプッシュ通知、アプリ内メッセージ、またはContent Cardsからユニバーサルリンクを使用している場合、`forwardUniversalLinks`が有効になっていることを確認してください：

```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
```

{% alert note %}
ユニバーサルリンクの転送には、アプリケーションのエンタイトルメントへのアクセスが必要です。シミュレーターで実行している場合、これらのエンタイトルメントは直接利用できません。シミュレーターでテストするには、**Copy Bundle Resources** ビルドフェーズに`.entitlements`ファイルを追加してください。
{% endalert %}

### 長押しの問題を確認する {#check-for-the-long-press-issue}

ユニバーサルリンクを長押しして**開く**を選択すると、iOSがそのドメインのユニバーサルリンクの関連付けを「解除」する場合があります。これはiOSの既知の動作です。リセットするには、リンクをもう一度長押しして**[アプリ名]で開く**を選択してください。

## メールからのディープリンクでアプリが開かない {#deep-link-from-email-does-not-open-the-app}

**症状:** メール内のリンクがユニバーサルリンクを通じてアプリを開きません。

メールのリンクはメールサービスプロバイダー (ESP) のクリックトラッキングシステムを経由するため、リンクがトラッキングドメインでラップされます（例: `https://click.yourdomain.com/...`）。メールからユニバーサルリンクを機能させるには、プライマリドメインだけでなく、クリックトラッキングドメインにもAASAファイルを設定する必要があります。

### クリックトラッキングドメインのAASAを確認する {#verify-click-tracking-domain-aasa}

1. メールサービスプロバイダー (ESP) の設定（SendGrid、SparkPost、またはAmazon SES）からクリックトラッキングドメインを特定します。
2. `https://your-click-tracking-domain/.well-known/apple-app-site-association` にAASAファイルをホストします。
3. クリックトラッキングドメインのAASAファイルに、同じ`appID`と有効なパスパターンが含まれていることを確認します。

メールサービスプロバイダー (ESP) 固有の設定手順については、[ユニバーサルリンクとApp Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links)を参照してください。

### リダイレクトチェーンを確認する {#check-the-redirect-chain}

一部のメールサービスプロバイダー (ESP) は、クリックトラッキングURLから最終URLへのリダイレクトを実行します。ユニバーサルリンクは、iOSが*最初の*ドメイン（クリックトラッキングドメイン）をアプリに関連付けられたものとして認識した場合にのみ機能します。リダイレクトがAASAチェックをバイパスすると、リンクはSafariで開かれます。

テスト方法:

1. 自分宛てにテストメールを送信します。
2. リンクを長押ししてURLを確認します — これがクリックトラッキングURLです。
3. このドメインに有効なAASAファイルがあることを確認します。

## ディープリンクがプッシュでは動作するがアプリ内メッセージでは動作しない（またはその逆） {#deep-link-works-from-push-but-not-from-in-app-message}

**症状:** 同じディープリンクが、あるBrazeチャネルでは動作するが、別のチャネルでは動作しません。

### BrazeDelegateを確認する {#check-the-brazedelegate}

`BrazeDelegate.braze(_:shouldOpenURL:)` を実装している場合、チャネル間でリンクが一貫して処理されているか確認してください。`context` パラメーターにはソースチャネルが含まれています。特定のチャネルからのリンクを誤ってフィルタリングしている条件分岐がないか確認してください。

### 詳細ログを有効にする {#enable-verbose-logging}

[詳細ログを有効にして]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)、問題を再現してください。`Opening` ログエントリを確認します：

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

動作するチャネルと動作しないチャネルのログ出力を比較してください。`useWebView` や `isUniversalLink` の違いは、SDKがリンクをどのように異なる方法で解釈しているかを示しています。

### カスタム表示デリゲートを確認する {#check-for-custom-display-delegates}

カスタムのアプリ内メッセージ表示デリゲートやContent Cardsクリックハンドラーを使用している場合、リンクイベントが正しくBraze SDKに渡されて処理されているか確認してください。

## 「アプリ内でWeb URLを開く」で空白ページや壊れたページが表示される {#open-web-url-inside-app-shows-a-blank-or-broken-page}

**症状：** **アプリ内でWeb URLを開く**を選択すると、WebViewが空白または壊れた状態で表示されます。

1. **URLがHTTPSを使用していることを確認します。** SDKのWebViewはATS準拠のURLを必要とします。HTTPリンクはサイレントに失敗します。
2. **Content Security Policyヘッダーを確認します。** 対象のWebページが`X-Frame-Options: DENY`または制限的な`Content-Security-Policy`を設定している場合、WebViewでのレンダリングがブロックされます。
3. **カスタムスキームへのリダイレクトを確認します。** Webページがカスタムスキーム（例：`myapp://`）にリダイレクトする場合、WebViewはそれを処理できません。
4. **SafariでURLをテストします。** デバイス上のSafariでページが読み込まれない場合、WebViewでも読み込まれません。

## BranchとBrazeのトラブルシューティング {#branch}

[Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking)をリンクプロバイダーとして使用している場合：

### BrazeDelegateがBranchにルーティングしていることを確認する {#verify-the-brazedelegate-routes-to-branch}

`BrazeDelegate`がBranchリンクをインターセプトし、Branch SDKに渡す必要があります。以下を確認してください：

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host, host.contains("app.link") {
    // Route to Branch SDK
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle other links
  return true
}
```

`shouldOpenURL`がBranchリンクに対して`true`を返す場合、BrazeはBranchにルーティングせず直接処理します。

### Branchリンクドメインを確認する {#check-branch-link-domain}

`BrazeDelegate`内のBranchドメインが、実際のBranchリンクドメインと一致していることを確認してください。Branchはいくつかのドメイン形式を使用します：

- `yourapp.app.link`（デフォルト）
- `yourapp-alternate.app.link`（代替）
- カスタムドメイン（Branchダッシュボードで設定されている場合）

### 両方のSDKのログを有効にする {#enable-both-sdks-logging}

リンクがチェーンのどこで途切れているかを診断するには：

1. [Brazeの詳細ログ]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)を有効にします。SDKがリンクを受信したことを確認するために、`Opening '<URL>':`エントリを探してください。
2. [Branchテストモード](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking)を有効にします。Branchダッシュボードでリンククリックイベントを確認してください。
3. Brazeがリンクを記録しているのにBranchがクリックを認識しない場合、`BrazeDelegate`のルーティングロジックに問題がある可能性が高いです。

### Branchダッシュボードの設定を確認する {#check-branch-dashboard-configuration}

Branchダッシュボードで以下を確認してください：

- アプリの**バンドルID**と**チームID**がXcodeプロジェクトと一致していること。
- **Associated Domains**にBranchリンクドメインが含まれていること。
- BranchのAASAファイルが有効であること（Branchは`app.link`ドメイン上で自動的にホストします）。

### Branchリンクを単独でテストする {#test-branch-links-independently}

問題を切り分けるために、Brazeの外でBranchリンクをテストしてください：

1. デバイスのSafariでBranchリンクを開きます。アプリが開かない場合、問題はBranchまたはAASAの設定にあり、Brazeの問題ではありません。
2. Branchリンクをメモアプリに貼り付けてタップします。ユニバーサルリンクは、Safariのアドレスバーからよりもメモアプリからの方が確実に動作します。

## 一般的なデバッグのヒント {#general-debugging-tips}

### 詳細ログを使用する {#use-verbose-logging}

[詳細ログを有効にする]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)ことで、SDKがリンクをどのように処理しているかを正確に確認できます。確認すべき主なエントリは以下のとおりです。

| ログエントリ | 意味 |
|---|---|
| `Opening '<URL>': - channel: notification` | SDKがプッシュ通知からのリンクを処理しています |
| `Opening '<URL>': - channel: inAppMessage` | SDKがアプリ内メッセージからのリンクを処理しています |
| `Opening '<URL>': - channel: contentCard` | SDKがContent Cardsからのリンクを処理しています |
| `useWebView: true` | SDKがアプリ内WebViewでURLを開きます |
| `isUniversalLink: true` | SDKがURLをユニバーサルリンクとして識別しました |
{: .reset-td-br-1 .reset-td-br-2 aria-label="詳細ログの使用" }

これらのログの読み方の詳細については、[詳細ログの読み方]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)を参照してください。

### リンクを単独でテストする {#test-links-in-isolation}

Brazeを通じてテストする前に、ディープリンクまたはユニバーサルリンクが単独で動作するかを確認してください。

- **カスタムスキーム**: ターミナルで `xcrun simctl openurl booted "myapp://path"` を実行します。
- **ユニバーサルリンク**: 物理デバイスのメモアプリにURLを貼り付けてタップします。Safariのアドレスバーからはテストしないでください。iOSは入力されたURLとタップされたリンクを異なる方法で処理します。
- **Branchリンク**: デバイスのメモアプリからBranchリンクを開きます。

### 物理デバイスでテストする {#test-on-a-physical-device}

ユニバーサルリンクはiOSシミュレーターでのサポートが限定的です。正確な結果を得るために、必ず物理デバイスでテストしてください。シミュレーターでテストする必要がある場合は、`.entitlements` ファイルを **Copy Bundle Resources** ビルドフェーズに追加してください。