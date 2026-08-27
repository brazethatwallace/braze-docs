---
page_order: 1.1
nav_title: iOSディープリンクガイド
article_title: iOSディープリンクガイド
description: "iOSアプリでどのタイプのディープリンクを使用すべきか、AASAファイルが必要な場合、および実装すべきアプリデリゲートメソッドについて説明します。"
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# iOSディープリンクガイド {#ios-deep-linking-guide}

> このガイドでは、使用するメッセージングチャネルやBranchなどのサードパーティリンクプロバイダーの利用有無に応じて、iOSアプリに適したディープリンク戦略を選択する方法を説明します。

実装の詳細については、[ディープリンク]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift)を参照してください。トラブルシューティングについては、[ディープリンクのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting)を参照してください。

## リンクタイプの選択 {#choosing-a-link-type}

Braze メッセージ内のリンクを iOS アプリで処理する方法は3つあります。それぞれ動作が異なり、適したチャネルやユースケースも異なります。

| リンクタイプ | 例 | 最適な用途 | アプリ未インストールでも開けるか |
|---|---|---|---|
| **カスタムスキーム** | `myapp://products/123` | プッシュ、アプリ内メッセージ、Content Cards | いいえ — リンクは機能しません |
| **ユニバーサルリンク** | `https://myapp.com/products/123` | メール、SMS、クリックトラッキングのあるチャネル | はい — Webにフォールバックします |
| **アプリ内でWeb URLを開く** | 任意の `https://` URL | モーダル WebView での Web コンテンツの表示 | N/A — WebView に表示されます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リンクタイプの選択" }

### カスタムスキームディープリンク {#custom-scheme-deep-links}

カスタムスキームディープリンク（例: `myapp://products/123`）は、アプリを特定の画面に直接開きます。サードパーティによってリンクが変更されないチャネルでは、最もシンプルなオプションです。

**カスタムスキームディープリンクを使用する場合:**
- プッシュ通知、アプリ内メッセージ、またはContent Cardsを送信する場合
- アプリがインストールされていない場合にリンクが機能する必要がない場合
- クリックトラッキング（メールサービスプロバイダー (ESP) のリンクラッピング）が不要な場合

**カスタムスキームディープリンクを使用しない場合:**
- メールを送信する場合 — メールサービスプロバイダー (ESP) はクリックトラッキングのためにリンクをラップするため、カスタムスキームが壊れます
- アプリがインストールされていない場合に Web ページへのフォールバックが必要な場合

### ユニバーサルリンク {#universal-links}

ユニバーサルリンク（例: `https://myapp.com/products/123`）は、iOS がブラウザーで開く代わりにアプリにルーティングできる標準的な HTTPS URL です。サーバー側の設定（AASA ファイル）とアプリ側の設定（Associated Domains エンタイトルメント）が必要です。

**ユニバーサルリンクを使用する場合:**
- メールを送信する場合。メールサービスプロバイダー (ESP) がクリックトラッキングのためにリンクをラップするため、リンクは HTTPS である必要があります。
- SMS やリンクがラップまたは短縮されるその他のチャネルで送信する場合。
- アプリがインストールされていない場合に Web ページへのフォールバックが必要な場合。
- Branch や AppsFlyer などのサードパーティリンクプロバイダーを使用している場合。

**ユニバーサルリンクを使用しない場合:**
- プッシュ、アプリ内メッセージ、またはContent Cardsからのディープリンクのみが必要な場合。カスタムスキームの方がシンプルです。

### 「アプリ内でWeb URLを開く」 {#open-web-url-inside-app}

このオプションは、アプリ内のモーダル WebView で Web ページを開きます。Braze SDKの `Braze.WebViewController` によって完全に処理されるため、URL ハンドリングコードを記述する必要はありません。

**「アプリ内でWeb URLを開く」を使用する場合:**
- アプリを離れずに Web ページ（プロモーションや記事など）を表示したい場合。
- URL が標準的な HTTPS Web ページであり、特定のアプリ画面へのディープリンクではない場合。

**「アプリ内でWeb URLを開く」を使用しない場合:**
- アプリ内の特定のビューに遷移する必要がある場合。代わりにカスタムスキームまたはユニバーサルリンクを使用してください。
- Web ページに認証が必要な場合や、埋め込みをブロックする Content Security Policy ヘッダーがある場合。

## リンクタイプごとに必要なもの {#what-you-need-for-each-link-type}

### カスタムスキームのディープリンク

| 要件 | 詳細 |
|---|---|
| AASAファイル | 不要 |
| `Info.plist` | `CFBundleURLTypes`にスキームを登録し、`LSApplicationQueriesSchemes`に追加します |
| App delegateメソッド | `application(_:open:options:)`を実装してURLを解析し、ナビゲーションを行います |
| Braze SDK設定 | 不要 — SDKはデフォルトでカスタムスキームURLを開きます |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタムスキームのディープリンク" }

### ユニバーサルリンク

| 要件 | 詳細 |
|---|---|
| AASAファイル | 必須 — `https://yourdomain.com/.well-known/apple-app-site-association`でホストします |
| Associated Domains | Xcodeの**Signing & Capabilities**で`applinks:yourdomain.com`を追加します |
| App delegateメソッド | `application(_:continue:restorationHandler:)`を実装して`NSUserActivity`を処理します |
| Braze SDK設定 | `configuration.forwardUniversalLinks = true`を設定します |
| BrazeDelegate（オプション） | カスタムルーティング（例：Branch）のために`braze(_:shouldOpenURL:)`を実装します |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユニバーサルリンク" }

{% alert important %}
Brazeを通じてメールを送信する場合、メールサービスプロバイダー (ESP)（SendGrid、SparkPost、またはAmazon SES）がリンクをクリックトラッキングドメインでラップします。AASAファイルは、プライマリドメインだけでなく、クリックトラッキングドメインにもホストする必要があります。完全な設定については、[ユニバーサルリンクとApp Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links)を参照してください。すべてのメールリンクがアプリを開いてしまう場合は、[すべてのメールリンクがアプリを開く]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting#every-email-link-opens-the-app)を参照してください。
{% endalert %}

### 「アプリ内でWeb URLを開く」

| 要件 | 詳細 |
|---|---|
| AASAファイル | 不要 |
| App delegateメソッド | 不要 — SDKが自動的に処理します |
| Braze SDK設定 | 不要 — キャンペーンコンポーザーで**Open Web URL Inside App**を選択します |
{: .reset-td-br-1 .reset-td-br-2 aria-label="「アプリ内でWeb URLを開く」" }

## AASAファイルが必要な場合 {#when-aasa}

Apple App Site Association（AASA）ファイルは、**ユニバーサルリンク**を使用する場合にのみ必要です。AASAファイルは、アプリが処理できるURLをiOSに伝えます。

AASAファイルが必要な場合：

- メールキャンペーンでディープリンクを送信する場合（メールサービスプロバイダー (ESP)がリンクをHTTPSクリックトラッキングURLでラップするため）。
- SMSキャンペーンでディープリンクを送信する場合（リンクがHTTPS URLに短縮される可能性があるため）。
- Branch、AppsFlyer、またはその他のリンクプロバイダーを使用する場合（独自のHTTPSドメインを使用するため）。
- プッシュ通知、アプリ内メッセージ、またはContent Cardsからユニバーサルリンクを使用する場合（一般的ではありませんが、`forwardUniversalLinks = true`で可能です）。

AASAファイルが不要な場合：

- プッシュ通知、アプリ内メッセージ、またはContent Cardsからカスタムスキームディープリンク（例：`myapp://`）のみを使用する場合。
- **Open Web URL Inside App**オプションを使用する場合。

AASAの設定手順については、[ユニバーサルリンクとアプリリンク]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links)を参照してください。

## リンクを処理するためにアプリコードが必要な場合 {#when-app-code}

実装するデリゲートメソッドは、使用するリンクの種類によって異なります。

| デリゲートメソッド | 処理対象 | 実装するタイミング |
|---|---|---|
| `application(_:open:options:)` | カスタムスキームディープリンク（`myapp://`） | 任意のチャネルからカスタムスキームディープリンクを使用する場合 |
| `application(_:continue:restorationHandler:)` | ユニバーサルリンク（`https://`） | メール、SMSから、または`forwardUniversalLinks = true`でユニバーサルリンクを使用する場合 |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | SDKによって開かれるすべてのURL | カスタムルーティングロジックが必要な場合（例：Branch、条件分岐処理、分析） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="リンクを処理するためにアプリコードが必要な場合" }

{% alert tip %}
Branchなどのサードパーティリンクプロバイダーを使用する場合は、`BrazeDelegate.braze(_:shouldOpenURL:)`を実装してURLをインターセプトし、プロバイダーのSDKに転送します。完全な例については、[ディープリンク用のBranch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking)を参照してください。
{% endalert %}

## BrazeとBranchを併用する {#branch}

[Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking)をリンクプロバイダーとして使用する場合、標準的なユニバーサルリンクの設定に加えて、いくつかの追加ステップが必要です。

1. **Branch SDK**：[Branchのドキュメント](https://help.branch.io/developers-hub/docs/native-sdks-overview)に従ってBranch SDKを統合します。
2. **Associated Domains**：Xcodeの**Signing & Capabilities**でBranchドメイン（例：`applinks:yourapp.app.link`）を追加します。
3. **BrazeDelegate**：BranchリンクをBrazeが直接処理するのではなく、Branch SDKにルーティングするために`braze(_:shouldOpenURL:)`を実装します。
4. **ユニバーサルリンクの転送**：Braze SDKの設定で`configuration.forwardUniversalLinks = true`を設定します。

実装の詳細とデバッグのガイダンスについては、[ディープリンク用のBranch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking)を参照してください。